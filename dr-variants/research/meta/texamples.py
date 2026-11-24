"""The examples and the summary numbers of the skeleton/variant meta page that aren't per-corner-case tables:
the inverse-swap example, the most-pairs step telling two variants apart, a DR the meta misses, a DR lost to the
most-pairs step, a DR lost to the bound's one too-strict cell, a DR only the premove pass finds and a DR the pass
alone loses (after trule.py), the cap optimisation summary, and the checks.  Every
printed solution is replayed on an independent sticker model (tex.py), and every printed pair count is counted on
its stickers.
usage: texamples.py -> ../out/meta/texamples.json"""
import json
import numpy as np
from tcommon import drs, ORDER, BYQT, path, HCAP
import subprocess
from tex import table, check, inv_txt, solves, DRVAR, RULES, meta_rows, insertion_cut, pairs_after
from topt import CAPS
from tfinal import META
from tmeta import quantity

J = {m: json.load(open(path(f'tfinal{m}.json'))) for m in (2, 3, 4)}
D = {m: drs(m) for m in (2, 3, 4)}
out = {}
def tup(r): return f"{r.P}, {r.S}, {r['T']}, {r.N}" if r.q >= 3 else f"{r.S}, {r['T']}, {r.N}"
def breaks(r):
    b = []
    if r.P > META.pmax: b.append('P')
    for k, c in META.caps.items():
        if quantity(k, r.P, r.S, r['T'], r.N) > c: b.append(k)
    return b

# ---- the inverse swap: a 3qt-skeleton solution with four different values
m, dr = 3, 16
scr = D[m].scramble[dr]
head, t = table(scr)
r = t[(t.side == 'N') & (t.q == 3) & (t.P == 1) & (t.S == 0) & (t['T'] == 2) & (t.N == 4) & (t.total == 13)].iloc[0]
assert check(scr, r)
sol = (r.path + ' ' + r.finish).strip(); isol = inv_txt(sol)
# the same solution on the other side, read by `drvar metaread`, and replayed on the sticker model
def metaread(scr, sol, inverse=False):
    o = subprocess.run([DRVAR, 'metaread', scr, sol] + (['inverse'] if inverse else []), capture_output=True, text=True).stdout.strip().split('\t')
    d = dict(zip(o[::2], o[1::2]))
    return int(d['L']), (int(d['P']), int(d['S']), int(d['T']), int(d['N'])), d['sections']
assert solves(scr, 'N', sol) and solves(scr, 'I', isol)
Ln, tn_, _ = metaread(scr, sol); Li, ti_, _ = metaread(scr, isol, True)
assert Ln == Li == r.L and tn_ == (r.P, r.S, r['T'], r.N) and ti_ == (r.N, r['T'], r.S, r.P)
ri = {'P': ti_[0], 'S': ti_[1], 'T': ti_[2], 'N': ti_[3]}
out['swap'] = dict(case=D[m].case[dr], scramble=scr, solution=sol, L=int(r.L), tuple=tup(r), inverse=isol, inv_tuple=', '.join(map(str, ti_)))
# the two examples of the definition
assert metaread("U' F2 R2 U'", 'U R2 F2 U')[:2] == (3, (0, 0, 1, 0)) and solves("U' F2 R2 U'", 'N', 'U R2 F2 U')
assert metaread("R2 F2 R2 U' R2 U'", 'U R2 U R2 F2 R2')[:2] == (3, (0, 0, 0, 3)) and solves("R2 F2 R2 U' R2 U'", 'N', 'U R2 U R2 F2 R2')

# ---- a cancelling pair: two quarter turns with only a slice between them
pscr = "F2 D' L2 R2 U B2 D R2 D U2 L2"; psol = "L2 U B2 U' F2 D' F2 B2 U F2"; pskel = "L2 U B2 U' F2 D' U F2"
assert solves(pscr, 'N', psol)
Lp, tp, secp = metaread(pscr, psol)
assert (Lp, tp) == (len(pskel.split()), (0, 0, 2, 0)) and secp == '0,0,0,2,0'
dp = D[2][D[2].scramble == pscr]
assert len(dp) == 1 and dp.ls.iloc[0] == len(psol.split())
out['pair'] = dict(case=dp.case.iloc[0], scramble=pscr, solution=psol, skeleton=pskel, L=Lp, T=tp[2], slice='F2 B2')

# ---- the most-pairs step
def sol_of(r): return (r.path + ' ' + r.finish).strip()
def exlist(r): return [int(v) for v in r.extras.split(',')]
def cut_of(r):
    """Where the printed path's pairs are counted, and the count on the stickers (must be the record's)."""
    cut = insertion_cut(r.path, exlist(r))
    return cut, pairs_after(scr, r.side, cut)
def own_reading(scr, r):
    """The printed solution read by `drvar metaread` must be the row's reading."""
    L_, t_, _x = metaread(scr, sol_of(r), r.side == 'I')
    assert L_ == r.L and t_ == (r.P, r.S, r['T'], r.N), 'the printed reading is not the solution\'s own'
def st_txt(r): return (f'(P, S, T) = ({r.rP}, {r.rS}, {r.rT})' if r.q >= 3 else f'(S, T) = ({r.rS}, {r.rT})')

# two variants of one skeleton with the same (P, S, T, N): the one with more pairs is within goal, the other is not
pick = None
m, case = 2, '4b2'
g = J[m]['goal']
for dr in D[m].index[(D[m].case == case) & D[m].wg][:60]:
    scr = D[m].scramble[dr]
    head, t = table(scr); t = meta_rows(t, g, META)
    a = t[t.adm]
    for _, grp in a.groupby('grp'):
        if len(grp) != 2 or grp.pairs.nunique() != 2 or not grp.same_read.all(): continue
        hi = grp.loc[grp.pairs.idxmax()]; lo = grp.loc[grp.pairs.idxmin()]
        if hi.total > g or lo.total <= g or hi.rP + hi.rS + hi.rT == 0: continue
        score = (int(hi.total), len(hi.path.split()), -int(hi.pairs - lo.pairs), int(dr))
        if pick is None or score < pick[0]: pick = (score, scr, hi, lo)
_, scr, hi, lo = pick
assert check(scr, hi) and check(scr, lo)
own_reading(scr, hi); own_reading(scr, lo)
(chi, phi), (clo, plo) = cut_of(hi), cut_of(lo)
assert phi == hi.pairs and plo == lo.pairs and phi > plo
# (one skeleton and the same extra moves: the two HTRs are equally far, so the pairs settle which goes first)
assert len(hi.path.split()) == len(lo.path.split())
out['step'] = dict(case=case, scramble=scr, side='' if hi.side == 'N' else 'the inverse of ', L=int(hi.rec_L), st=st_txt(hi), nb=int(hi.rec_N_cca), moves=len(hi.path.split()),
                   hi_path=hi.path, hi_cut=chi, hi_pairs=int(phi), hi_finish=hi.finish, hi_total=int(hi.total),
                   lo_path=lo.path, lo_cut=clo, lo_pairs=int(plo), lo_total=int(lo.total))

# a DR lost to the step: its within-goal HTR passes steps 3 to 5, and another variant of the skeleton with the same
# (P, S, T, N) has more pairs
pick = None
for m, case in ((2, '4b2'), (3, '2c3'), (4, '2c4'), (3, '4c3'), (2, '4a2'), (4, '4c4'), (4, '0c4'), (3, '0c3')):
    g = J[m]['goal']
    for dr, cat, br, _ in J[m]['cases'][case]['miss']['detail']:
        if cat != 'pairs': continue
        scr = D[m].scramble[dr]
        head, t = table(scr); t = meta_rows(t, g, META)
        assert not (t.fin & (t.total <= g)).any() and (t.adm & (t.total <= g)).any(), 'not a DR lost to the most-pairs step'
        for _, lo in t[t.adm & ~t.fin & (t.total <= g) & t.same_read].iterrows():
            rivals = t[t.fin & (t.grp == lo.grp) & t.same_read]
            if not len(rivals): continue
            hi = rivals.sort_values(['total', 'path']).iloc[0]
            score = (len(rivals), int(lo.rP), int(lo.total), len(scr.split()), int(dr))
            if pick is None or score < pick[0]: pick = (score, m, case, scr, lo, hi, len(rivals))
    if pick: break
if pick:
    _, m, case, scr, lo, hi, nriv = pick
    assert check(scr, lo) and check(scr, hi) and hi.total > J[m]['goal'] >= lo.total
    own_reading(scr, lo); own_reading(scr, hi)
    (clo, plo), (chi, phi) = cut_of(lo), cut_of(hi)
    assert plo == lo.pairs and phi == hi.pairs and phi > plo
    out['lostpairs'] = dict(case=case, scramble=scr, side='' if lo.side == 'N' else 'the inverse of ', L=int(lo.rec_L), st=st_txt(lo), nb=int(lo.rec_N_cca),
                            lo_solution=sol_of(lo), lo_total=int(lo.total), lo_cut=clo, lo_pairs=int(plo), lo_tuple=tup(lo),
                            hi_path=hi.path, hi_cut=chi, hi_pairs=int(phi), hi_total=int(hi.total), rivals=int(nriv))
else:
    out['lostpairs'] = None

# ---- a DR the meta misses: its nearest within-goal HTR needs a second pre-2qt move on both sides
def nearest(t, side, goal):
    w = t[(t.side == side) & (t.total <= goal)]
    if not len(w): return None
    rows = [x for _, x in w.iterrows()]
    rows.sort(key=lambda x: (len(breaks(x)), x.P, x.P + x.S + x['T'], x.total, x.path))
    return rows[0]
pick = None
for m, case in ((3, '2c3'), (2, '4b2'), (4, '2c4')):
    for dr, cat, br, _ in J[m]['cases'][case]['miss']['detail']:
        if cat != 'P': continue
        scr = D[m].scramble[dr]
        head, t = table(scr)
        a, b = nearest(t, 'N', J[m]['goal']), nearest(t, 'I', J[m]['goal'])
        if a is None or b is None or breaks(a) != ['P'] or breaks(b) != ['P']: continue
        if a.P != 2 or b.P != 2: continue
        assert check(scr, a) and check(scr, b)
        score = (a.total + b.total, len(scr))
        if pick is None or score < pick[0]: pick = (score, m, case, scr, a, b)
    if pick: break
_, m, case, scr, a, b = pick
for row_, side_ in ((a, False), (b, True)):
    L_, t_, _x = metaread(scr, (row_.path + ' ' + row_.finish).strip(), side_)
    assert L_ == row_.L and t_ == (row_.P, row_.S, row_['T'], row_.N), 'the printed reading is not the solution\'s own'
out['missed'] = dict(case=case, scramble=scr, n_total=int(a.total), n_solution=(a.path + ' ' + a.finish).strip(), n_tuple=tup(a), n_L=int(a.L),
                     i_solution=(b.path + ' ' + b.finish).strip(), i_tuple=tup(b), i_L=int(b.L))

# ---- a DR lost to the bound: the HTR passes every cap and fits the goal, but the bound's N is one too many
pick = None
for m, case in ((3, '2c3'), (2, '4b2'), (3, '4c3'), (4, '2c4')):
    for dr, cat, br, _ in J[m]['cases'][case]['miss']['detail']:
        if cat != 'bound': continue
        scr = D[m].scramble[dr]
        head, t = table(scr)
        g = J[m]['goal']
        w = t[(t.total <= g) & (t.P <= 1) & (t.P + t.S + t['T'] <= 5) & (t.L + t.P + t.S + t['T'] + t.N_cca > g)]
        for _, x in w.iterrows():
            if not breaks(x) and x.N_cca == x.N + 1:
                assert check(scr, x)
                if pick is None or x.total < pick[4].total: pick = (m, case, dr, scr, x, g)
    if pick: break
if pick:
    m, case, dr, scr, x, g = pick
    L_, t_, _x = metaread(scr, (x.path + ' ' + x.finish).strip(), x.side == 'I')
    assert L_ == x.L and t_ == (x.P, x.S, x['T'], x.N)
    out['bound'] = dict(case=case, scramble=scr, side='' if x.side == 'N' else 'the inverse of ', path=x.path, len=len(x.path.split()), finish=x.finish,
                        fin=len(x.finish.split()), total=int(x.total), kind=x.kind, L=int(x.L), tuple=tup(x), nb=int(x.N_cca),
                        says=int(x.L + x.P + x.S + x['T'] + x.N_cca))
    assert out['bound']['says'] == x.total + 1 > g
else:
    out['bound'] = None           # no DR of the sample is lost to the bound alone

# ---- the premove pass
NPRE = 12          # DRs per corner case looked at for the premove example
def rest_table(scr):
    """The within-goal solutions of the left-over DRs of one DR (`drvar metarest1`): side, path, finish, the turn made
    first on the other side, and the reading of the left-over skeleton (L and total count that turn)."""
    o = subprocess.run([DRVAR, 'metarest1', RULES, scr], capture_output=True, text=True).stdout
    rows = []
    for l in o.split('\n'):
        if not l.startswith('  sol'): continue
        f = l.split('\t')
        v = f[7].split(); pst = dict(zip(v[::2], map(int, v[1::2])))
        rows.append(dict(side=f[1], path=f[2], finish=f[3], turn=f[4], q=int(f[5].split()[1]), L=int(f[6].split()[1]), P=pst['P'], S=pst['S'], T=pst['T'], N=pst['N'],
                         bound=int(f[8].split()[1]), total=int(f[9].split()[1]), same=f[10].split()[1] == '1', sections=f[11].split()[1], first=int(f[12].split()[1])))
    # on normal the pass is not made for a skeleton that also starts with a quarter turn (it is made on inverse),
    # unless the run makes it on both sides
    return [r for r in rows if r['side'] == 'I' or r['first'] > 0 or J[2].get('rest_both', False)]
def secs_txt(sections):
    """'0,3,0,3,0' (the extra moves of each section, the finish last) -> '(P, P, S, T, N) = (0, 3, 0, 3, 0)'."""
    v = sections.split(',')
    return f"({', '.join(['P'] * (len(v) - 3) + ['S', 'T', 'N'])}) = ({', '.join(v)})"
def lets_through(r, g):
    """Steps 3 and 5 on a left-over reading (no step 4 there)."""
    return (r['P'] <= META.pmax and r['P'] + r['S'] + r['T'] <= META.caps['P+S+T'] and r['L'] + r['P'] + r['S'] + r['T'] + r['bound'] <= g
            and (not HCAP or 1 + len(r['path'].split()) <= g - 1))          # (the premove counts as a move to HTR)

if J[2]['uniss'] == 'add':
    # a DR the pass finds and the full search doesn't: the solution has too many early extra moves on both sides
    pick = None
    for m in (2, 3, 4):
        g = J[m]['goal']
        for case in BYQT[m]:
            # (the first DRs of each corner case are enough to pick from: with the cap on the moves to HTR the pass finds
            # some two hundred of them, and each takes several runs of the tool)
            for dr in J[m]['cases'][case]['uniss']['gained_drs'][:NPRE]:
                scr = D[m].scramble[dr]
                for r in rest_table(scr):
                    if not r['same'] or r['total'] > g or not lets_through(r, g): continue
                    sol = ' '.join(x for x in (r['path'], r['finish'], r['turn']) if x)
                    inv = r['side'] == 'I'
                    Lf, tf, sf = metaread(scr, sol, inv); Lo, to, so = metaread(scr, inv_txt(sol), not inv)
                    if tf[0] < 2 or to[0] < 2: continue
                    score = (inv, sf != so, r['total'], r['q'], len(scr.split()), int(dr), sol)
                    if pick is None or score < pick[0]: pick = (score, m, case, scr, r, sol, (Lf, tf, sf), (Lo, to, so))
    _, m, case, scr, r, sol, (Lf, tf, sf), (Lo, to, so) = pick
    side = r['side']; other = 'I' if side == 'N' else 'N'; name = {'N': 'normal', 'I': 'inverse'}
    assert solves(scr, side, sol) and solves(scr, other, inv_txt(sol)) and len(sol.split()) == r['total'] <= J[m]['goal']
    assert Lf + sum(tf) == Lo + sum(to) == r['total'] and int(sf.split(',')[-1]) == tf[3]
    # the left-over DR on its own: the premove, then the scramble of that side; the rest of the solution solves it and reads as printed
    rscr = r['turn'] + ' ' + (scr if side == 'N' else inv_txt(scr)); rsol = (r['path'] + ' ' + r['finish']).strip()
    assert solves(rscr, 'N', rsol)
    Lr, tr, sr = metaread(rscr, rsol)
    assert Lr == r['L'] - 1 and tr == (r['P'], r['S'], r['T'], r['N']) and sr == r['sections'] + ',' + str(r['N']), 'the left-over reading is not the solution\'s own'
    why = (f"{tf[0]} extra moves before 2qt either way" if tf[0] == to[0] else f"{tf[0]} extra moves before 2qt on {name[side]} and {to[0]} on {name[other]}")
    out['premove'] = dict(case=case, scramble=scr, total=int(r['total']), solution=sol, side=name[side], q=len(sf.split(',')) - 1, full=secs_txt(sf), same=sf == so, other=secs_txt(so),
                          other_side=name[other], why=why, turn=r['turn'], rest=secs_txt(sr), rest_q=int(r['q']), rest_L=int(r['L']))

    # a DR that the pass in place of the full search loses: its only within-goal solution goes on after the last quarter
    # turn of a skeleton that ends in HH, and the pass has nothing within the goal
    TRJ = {m: json.load(open(path(f'trule{m}.json'))) for m in (2, 3, 4)}
    def after_kind(fin):
        ax = lambda mv: {'U': 0, 'D': 0, 'R': 1, 'L': 1, 'F': 2, 'B': 2}[mv[0]]
        if len(fin) == 2 and ax(fin[0]) == ax(fin[1]) and fin[0] != fin[1]: return 'the slice'
        if len(fin) == 3 and fin[0] == fin[2] and ax(fin[0]) != ax(fin[1]): return 'the corner swap'
        return 'the moves'
    pick = None
    for m, case in ((3, '4c3'), (3, '2c3'), (4, '2c4'), (2, '4b2'), (4, '4c4'), (2, '4a2'), (4, '0c4'), (3, '0c3')):
        g = J[m]['goal']
        for dr in TRJ[m][case]['written']['lost_drs']:
            scr = D[m].scramble[dr]
            head, t = table(scr); t = meta_rows(t, g, META)
            ok = t[t.fin & (t.total <= g)]
            if len(ok) != 1 or not ok.same_read.all(): continue
            x = ok.iloc[0]; fin = x.finish.split()
            if x.q < 3 or x.N != len(fin) or len(fin) < 2 or after_kind(fin) == 'the moves': continue
            sol = sol_of(x); other = 'I' if x.side == 'N' else 'N'
            Lo, to, so = metaread(scr, inv_txt(sol), other == 'I')
            if to[0] < 2: continue
            if any(v['total'] <= g for v in rest_table(scr)): continue        # nothing within the goal on what is left, on either side
            score = (int(x.total), len(scr.split()), int(dr))
            if pick is None or score < pick[0]: pick = (score, m, case, scr, x, sol, other, (Lo, to, so))
        if pick: break
    _, m, case, scr, x, sol, other, (Lo, to, so) = pick
    assert check(scr, x); own_reading(scr, x)
    Lx, tx, sx = metaread(scr, sol, x.side == 'I')
    turn = x.path.split()[-1]
    assert not turn.endswith('2') and Lo + sum(to) == x.total
    out['premove_lost'] = dict(case=case, scramble=scr, side='normal' if x.side == 'N' else 'inverse', solution=sol, total=int(x.total), tuple=secs_txt(sx), turn=turn,
                               after=x.finish, after_kind=after_kind(x.finish.split()), other_side='normal' if other == 'N' else 'inverse', other=secs_txt(so), other_P=int(to[0]))

# ---- found within K: meta against baseline
big = [k for k in ORDER if k not in ('0c3', '0c4')]
ratios = [J[m]['cases'][k]['orders']['cca_len'][j] / J[m]['cases'][k]['orders']['none_len'][j] for m in (2, 3, 4) for k in BYQT[m] if k in big for j in (1, 2)]
out['boost'] = f'{min(ratios):.1f}x-{max(ratios):.1f}x'
out['boost_all'] = [round(x, 2) for x in ratios]

# ---- the cap optimisation (rules with the mirror floor on or off, every skeleton length)
z = np.load(path('opt3.npz'))
rules, miss, work = z['rules'], z['miss'], z['work']
nc = len(CAPS)
fam = (rules[:, nc] <= 1) & (rules[:, nc + 1] == 0)
ncap = (rules[:, :nc] < 99).sum(axis=1)
bi = [ORDER.index(k) for k in big]
ref = np.nonzero(fam & (ncap == 0) & (rules[:, nc] == 0))[0][0]
dm = miss - miss[ref]; gw = np.exp(np.log(work[:, bi] / work[ref, bi]).mean(axis=1))
worst = dm[:, bi].max(axis=1); mean = dm[:, bi].mean(axis=1)
def find(caps, floor):
    want = np.full(nc, 99); [want.__setitem__(CAPS.index(k), v) for k, v in caps.items()]
    i = np.nonzero(fam & (rules[:, :nc] == want).all(axis=1) & (rules[:, nc] == floor))[0]
    assert len(i) == 1; return int(i[0])
def desc(i):
    r = rules[i]
    return ', '.join(f'{CAPS[j]} ≤ {r[j]}' for j in range(nc) if r[j] < 99)
def row(name, i):
    wc = big[int(np.argmax(dm[i, bi]))]
    return dict(name=name, work=f'{100 * gw[i]:.0f}%', mean=f'+{100 * mean[i]:.1f} points', worst=f'+{100 * worst[i]:.1f} points ({wc})' if worst[i] > 5e-4 else '+0.0 points')
meta = find({'P+S+T': 5}, 1); fl = find({}, 1)
rows = [row('Step 4', fl), row('Step 4, P+S+T ≤ 6', find({'P+S+T': 6}, 1)), row('**Step 4, P+S+T ≤ 5**', meta), row('Step 4, P+S+T ≤ 4', find({'P+S+T': 4}, 1))]
best = {}
for k in (2, 3):
    ok = np.nonzero(fam & (ncap == k) & (worst <= worst[meta] + 1e-9))[0]
    i = int(ok[np.argmin(gw[ok])]); best[k] = i
    rows.append(row(f"Step 4, the best {'two' if k == 2 else 'three'} caps that miss no more than the meta in any corner case ({desc(i)})", i))
# caps that include N: the best single one at the meta's misses, and the two the doc and the request name
withn = [CAPS.index(k) for k in ('N', 'T+N', 'S+T+N', 'P+S+T+N')]
ok = np.nonzero(fam & (ncap == 1) & (rules[:, nc] == 1) & (rules[:, withn] < 99).any(axis=1) & (worst <= worst[meta] + 1e-9))[0]
i = int(ok[np.argmin(gw[ok])])
rows.append(row(f'Step 4, the best single cap that includes N and misses no more than the meta ({desc(i)})', i))
rows.append(row('Step 4, S+T+N ≤ 5', find({'S+T+N': 5}, 1)))
rows.append(row('Step 4, T+N ≤ 4', find({'T+N': 4}, 1)))
rows.append(row('P+S+T+N ≤ 5, without step 4 (the doc\'s S+T+N ≤ min(G−L, 5) − P)', find({'P+S+T+N': 5}, 0)))
nfam = int(fam.sum())
wgs = np.array([J[m]['cases'][k]['wg'] for k in ORDER for m in (2, 3, 4) if k in BYQT[m]])
lost_fl = int(round(float(np.nansum(dm[fl] * wgs))))        # (a corner case with no within-goal DR, in a test run, has no misses)
out['opt'] = dict(rows=rows, nrules=nfam, floor_cut=f'{100 * (1 - gw[fl]):.0f}%', floor_lost_n=lost_fl,
                  floor_lost=('no within-goal DR' if lost_fl == 0 else f"{lost_fl} of the sample's {sum(wgs):,} within-goal DRs"),
                  after='', meta_work=float(gw[meta]), best2=float(gw[best[2]]), best3=float(gw[best[3]]))
json.dump(out, open(path('texamples.json'), 'w'), indent=1, ensure_ascii=False)
for k, v in out.items(): print(k, json.dumps(v, ensure_ascii=False, indent=1)[:1500])
