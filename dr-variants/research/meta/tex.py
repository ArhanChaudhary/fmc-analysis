"""One DR's HTRs as the page reads them (`drvar metax2`), with every printed solution replayed on an independent
sticker model (judging-a-dr's fmccube) on the side it was found on, and its inverse replayed on the other side."""
import sys, subprocess, io
sys.path.insert(0, '/data/fmc/judging-a-dr/research/tool')
import fmccube as fc
import pandas as pd
from tcommon import HCAP
DRVAR = '/data/fmc/dr-variants/research/drvar/target/release/drvar'
RULES = '/data/fmc/dr-variants/research/out/meta/rules_1123.tsv'
def ls_solved(st):
    sol = fc.solved()
    return all(st[k] == sol[k] for k in st if k[0][1] != 0)
def inv_txt(moves):
    out = []
    for mv in reversed(moves.split()):
        out.append(mv[:-1] if mv.endswith("'") else (mv if mv.endswith('2') else mv + "'"))
    return ' '.join(out)
def solves(scr, side, sol):
    start = fc.parse(scr) if side == 'N' else fc.invert(fc.parse(scr))
    return ls_solved(fc.apply(fc.solved(), start + fc.parse(sol)))
def true_pairs(st):
    """True pairs counted from the stickers: a corner and an edge next to each other in the U or D layer whose top
    stickers match and whose side stickers match (0 to 16)."""
    n = 0
    for y in (1, -1):
        for x in (1, -1):
            for z in (1, -1):
                c = (x, y, z); top = (0, y, 0)
                for e, side in (((x, y, 0), (x, 0, 0)), ((0, y, z), (0, 0, z))):
                    if st[(c, top)] == st[(e, top)] and st[(c, side)] == st[(e, side)]: n += 1
    return n
def is_qt(mv): return not mv.endswith('2')
def insertion_cut(path, extras):
    """The moves of `path` up to where its pairs are counted: right after its last insertion, that is before the
    quarter turn that closes the last section with extra moves (before the last quarter turn when no section has any).
    extras: the extra moves of each section before HTR, first to last."""
    mv = path.split()
    qpos = [i for i, x in enumerate(mv) if is_qt(x)]
    assert len(qpos) == len(extras)
    last = max([j for j, e in enumerate(extras) if e > 0], default=len(extras) - 1)
    return ' '.join(mv[:qpos[last]])
def pairs_after(scr, side, moves):
    """True pairs, on the sticker model, of the DR (or its inverse) after `moves`."""
    start = fc.parse(scr) if side == 'N' else fc.invert(fc.parse(scr))
    return true_pairs(fc.apply(fc.solved(), start + fc.parse(moves)))
def table(scr, m=None):
    out = subprocess.run([DRVAR, 'metax2', RULES, scr] + ([str(m)] if m else []), capture_output=True, text=True).stdout
    head = [l for l in out.split('\n') if l.startswith('#')]
    body = [l for l in out.split('\n') if l and not l.startswith('#')]
    t = pd.read_csv(io.StringIO('\n'.join(body)), sep='\t', keep_default_na=False, dtype={'route': str, 'rec_route': str, 'extras': str, 'rec_extras': str})
    return head, t
def meta_rows(t, g, rule):
    """The table of one DR with the meta applied the way the records have it: the reading of each HTR's shortest
    member (rec_*; the path printed is the member with the best total), what the caps, step 4 and the
    corner-case-aware bound let through (adm), and what is left after the most-pairs step (fin)."""
    t = t.copy()
    ex = [[int(v) for v in x.split(',')] for x in t.rec_extras]
    t['rP'] = [sum(e[:-2]) for e in ex]; t['rS'] = [e[-2] for e in ex]; t['rT'] = [e[-1] for e in ex]
    t['rPm'] = [e[3] if len(e) == 6 else 0 for e in ex]
    q = t.q
    floor = (t.rS.where(q == 2, t.rP.where(q == 3, (t.rP - t.rT).where(q == 4, (t.rP - t.rS - t.rT).where(q == 5, t.rP - t.rPm - t.rS - t.rT)))))
    pst = t.rP + t.rS + t.rT
    N = t.rec_N_cca
    adm = (t.rP <= rule.pmax) & (t.rec_L + pst + (N.where(N > floor, floor) if rule.floor else N) <= g)
    for k, v in rule.caps.items():
        adm &= {'P+S+T': pst}[k] <= v
    if HCAP: adm &= t.path.str.split().str.len() <= g - 1          # step 3: at most G-1 moves to HTR
    t['adm'] = adm
    t['grp'] = t.side + ' ' + t.rec_route + ' ' + t.rP.astype(str) + ' ' + t.rS.astype(str) + ' ' + t.rT.astype(str) + ' ' + N.astype(str)
    top = t[t.adm].groupby('grp').pairs.max()
    t['fin'] = t.adm & (t.pairs == t.grp.map(top)) if rule.pairs else t.adm
    t['same_read'] = (t.L == t.rec_L) & (t.extras == t.rec_extras)
    return t
def check(scr, row):
    """The row's solution solves its side, and its inverse solves the other side (both leave the E slice)."""
    sol = (row.path + ' ' + row.finish).strip()
    other = 'I' if row.side == 'N' else 'N'
    return solves(scr, row.side, sol) and solves(scr, other, inv_txt(sol)) and len(sol.split()) == row.total
if __name__ == '__main__':
    scr = sys.argv[1]; m = int(sys.argv[2]) if len(sys.argv) > 2 else None
    head, t = table(scr, m)
    print('\n'.join(head))
    g = int(head[1].split('goal ')[1].split()[0])
    w = t[t.total <= g]
    for _, r in w.iterrows():
        print(r.side, f'L={r.L} q={r.q} {r.kind}', f'P={r.P} S={r.S} T={r["T"]} N={r.N} (bound {r.N_cca})', f'total {r.total}', '|', r.path, '+', r.finish, '| replay', 'ok' if check(scr, r) else 'FAILED')
