"""One DR, the way the report shows it: the funnel, the HTRs that pass both floors (most pairs first), where the
first within-goal one sits in the baseline order (pair floor, shortest HTR first, most pairs among equals), and every
printed solution replayed on the sticker model.  The pair counts are checked against the stickers too."""
import sys, subprocess, io
sys.path.insert(0, '/data/fmc/judging-a-dr/research/tool')
import fmccube as fc
import pandas as pd, numpy as np
PF = {0: 4, 2: 5, 4: 3, 6: 3, 8: 2, 10: 3, 12: 1, 16: 0}
DRVAR = '/data/fmc/dr-variants/research/drvar/target/release/drvar'
def ls_solved(st):
    sol = fc.solved()
    return all(st[k] == sol[k] for k in st if k[0][1] != 0)
def check_normal(scr, sol): return ls_solved(fc.state_after(scr, sol))
def check_inverse(pre, inv_moves):      # moves `pre` on normal, then `inv_moves` on the inverse
    return ls_solved(fc.apply(fc.solved(), fc.invert(fc.parse(pre)) + fc.parse(inv_moves)))
def nmoves(s): return len(s.split())
# pairs read off the stickers, as an independent check of the counts the search tool prints
SIDE = [(1, 0, 0), (-1, 0, 0), (0, 0, 1), (0, 0, -1)]
AXIS = {'F': 'FB', 'B': 'FB', 'R': 'RL', 'L': 'RL', 'U': 'UD', 'D': 'UD'}
def slots():
    out = []
    for c in fc.CORNERS:
        for e in fc.UD_EDGES:
            if e[1] == c[1] and sum(a != b for a, b in zip(c, e)) == 1:      # same layer, touching
                n = [v for v in SIDE if all(v[i] == 0 or (v[i] == c[i] and v[i] == e[i]) for i in range(3))][0]
                out.append((c, e, n))
    assert len(out) == 16
    return out
SLOTS = slots()
def pairs_sticker(st):
    """(true pairs, HTR-equivalent pairs): the two side stickers match (same colour, or same or opposite colour)."""
    true = htr = 0
    for c, e, n in SLOTS:
        up = (0, c[1], 0)
        a, b = st[(c, n)], st[(e, n)]
        htr += AXIS[a] == AXIS[b]
        true += a == b and st[(c, up)] == st[(e, up)]
    return true, htr
def state_on(scr, side, moves):        # the state after `moves` on the normal ('N') or the inverse ('I') scramble
    start = fc.parse(scr) if side == 'N' else fc.invert(fc.parse(scr))
    return fc.apply(fc.solved(), start + fc.parse(moves))
def inverse_state_on(scr, side, moves):
    start = fc.parse(scr) if side == 'N' else fc.invert(fc.parse(scr))
    return fc.apply(fc.solved(), fc.invert(start + fc.parse(moves)))
def view(scr, top=10, show_niss=3, quiet=False):
    out = subprocess.run([DRVAR, 'metax', scr], capture_output=True, text=True).stdout
    head = [l for l in out.split('\n') if l.startswith('#')]
    body = [l for l in out.split('\n') if l and not l.startswith('#') and not l.startswith('NISS')]
    niss = [l.split('\t') for l in out.split('\n') if l.startswith('NISS')]
    t = pd.read_csv(io.StringIO('\n'.join(body)), sep='\t', keep_default_na=False)
    info = head[1][2:]
    g = int(info.split('goal ')[1].split()[0]); ls = int(info.split('optimal leave-slice ')[1])
    t['len'] = t.L + t.extra
    t['A'] = g - t.len
    t['plive'] = t.pairs_htr.map(PF) <= t.A
    t['rlive'] = t.rule_bound <= g
    t['ok'] = t.total <= g
    for _, r in t[t.ok].iterrows():     # replay every within-goal solution
        full = (r.path + ' ' + r.finish).strip()
        good = check_normal(scr, full) if r.side == 'N' else check_inverse(scr, full)
        assert good and nmoves(full) == r.total, ('replay failed', scr, r.side, full)
    # the pair counts at 2qt and at HTR against the sticker model: every within-goal HTR and a spread of the others
    chk = pd.concat([t[t.ok], t[~t.ok].iloc[::max(1, len(t) // 150)]])
    for _, r in chk.iterrows():
        pre = ' '.join(r.path.split()[:int(r.moves_2qt)])
        assert pairs_sticker(state_on(scr, r.side, pre)) == (r.pairs_2qt, r.htrpairs_2qt), ('pairs at 2qt differ from the sticker model', scr, r.path)
        assert pairs_sticker(inverse_state_on(scr, r.side, pre)) == (r.pairs_2qt_inv, r.htrpairs_2qt_inv), ('pairs at 2qt on the inverse differ', scr, r.path)
        assert pairs_sticker(state_on(scr, r.side, r.path)) == (r.pairs_htr, 16), ('pairs at HTR differ from the sticker model', scr, r.path)
    both = t[t.rlive & t.plive].sort_values(['pairs_htr', 'len'], ascending=[False, True]).reset_index(drop=True)
    base = t[t.plive].sort_values(['len', 'pairs_htr'], ascending=[True, False]).reset_index(drop=True)
    first_base = base.index[base.ok][0] + 1 if base.ok.any() else None
    first_both = both.index[both.ok][0] + 1 if both.ok.any() else None
    res = dict(info=info, goal=g, ls=ls, n_all=len(t), n_rule=int(t.rlive.sum()), n_both=len(both), n_within=int(t.ok.sum()), first_base=first_base, first_both=first_both, both=both, t=t, niss=niss)
    for f in niss:      # replay NISS solutions
        pre, q = f[1].split(' (')[0], f[1].split(' (')[1].rstrip(')')
        fin = f[2].strip('()')
        assert check_inverse(scr + ' ' + pre, q + ' ' + fin), ('niss replay failed', scr, f)
    if not quiet:
        print(f'**{scr}**  ({info})')
        print(f'- HTRs in reach: {len(t)}; pass the rule bound: {res["n_rule"]}; also pass the pair floor: {len(both)}; within goal: {res["n_within"]}')
        print(f'- first within-goal HTR: number {first_base} in the baseline order (pair floor, moves to HTR, then pairs), number {first_both} with both floors, most pairs first')
        cols = ['side', 'path', 'finish', 'kind', 'L', 'extra', 'case', 'rule_N', 'rule_bound', 'pairs_htr', 'total']
        print(both.head(top)[cols].to_string())
        for f in niss[:show_niss]: print('  ', ' | '.join(f))
    return res
if __name__ == '__main__':
    view(sys.argv[1], top=int(sys.argv[2]) if len(sys.argv) > 2 else 10)
