#!/usr/bin/env python3
"""Step 5: every checkable claim of the notes with a verdict, the exact numbers, and for each correction (and each
existence claim) an example state, replayed on is-dr-xs-worth-it's sticker model (src/cube.py): the state is given as a
setup from solved (F/B EO solved; DR on U/D), with an optimal EO-kept DR (moves U D R L F2 B2) whose length is the
table's value.  Output: out/claims.tsv, out/claims_examples.json (read by witness.py)."""
import os, sys, json, csv
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import pop, geom, features as fx
from geom import cube
F = pop.feat(); d = F['d'].astype(int); P = pop.populations()
DA = np.fromfile('/data/fmc/eo-to-dr/research/out/big/all_dr_eo0.u8', dtype=np.uint8).astype(int)
rows = []; EX = {}
def m_(c, e): return pop.drm_mask(c, e)
def arm(a, b): return (F['carm'] == a) & (F['earm'] == b)
def cc(l, s=None):
    m = F['corner_case'] == 'abcd'.index(l)
    return m if s is None else m & (F['case_suffix'] == s)
def p6(m, dd=None): dd = d if dd is None else dd; return float((dd[m] <= 6).mean()) if m.sum() else float('nan')
def example(ix, note=''):
    """A replayed example: setup from solved, optimal DR, features."""
    ix = int(ix); setup = geom.setup_for(ix, d); sol = geom.path_to_dr(ix, d)
    s = cube.do(cube.SOLVED, ' '.join(setup))
    assert geom.ix_of_state(s) == ix
    t = cube.do(s, ' '.join(sol)); assert geom.is_dr_ud(t) and geom.eo_fb_ok(t) and len(sol) == d[ix]
    return dict(setup=' '.join(setup), dr=' '.join(sol), length=len(sol), state=fx.describe(F, ix), note=note)
def pick(m, cond=None, seed=0):
    idx = np.flatnonzero(m if cond is None else m & cond)
    return int(idx[np.random.default_rng(seed).integers(len(idx))]) if len(idx) else None
def tidy(numbers):
    """As printed: thousands separators, and Python lists written out ("['21']" -> "21")."""
    import re
    numbers = re.sub(r"\[([^\]]*)\]", lambda m: m.group(1).replace("'", ''), numbers)
    return re.sub(r'(?<![\w.,-])\d{4,}(?![\w.])', lambda m: f'{int(m.group(0)):,}', numbers)
def claim(cid, tag, text, verdict, numbers, ex=None):
    numbers = tidy(numbers)
    rows.append((cid, tag, text, verdict, numbers, json.dumps(ex) if ex else ''))
    if ex: EX[cid] = ex

CELLS = {}                                   # numbers the text quotes, one value per key (out/claims_cells.json)
def cells(cid, **kw): CELLS.setdefault(cid, {}).update(kw)
def frac(m, k=6): return float((d[m] <= k).sum()) / int(m.sum()) if m.sum() else float('nan')
def cols_along(axis):
    """The bad corners form columns along `axis`: every bad corner's mirror image across that axis is bad too."""
    mir = [next(j for j, q in enumerate(geom.CORNERS) if all(q[k] == (-p[k] if k == axis else p[k]) for k in range(3))) for p in geom.CORNERS]
    return fx.per_co((fx.bad == fx.bad[:, mir]).all(1))
def qt_from(co_targets):
    """Per corner twist pattern: the fewest U/D quarter turns to reach one of the patterns co_targets, half turns free."""
    H = [m for m in geom.EOK if geom.NAMES[m].endswith('2')]
    Q = [m for m in geom.EOK if geom.NAMES[m][0] in 'UD' and not geom.NAMES[m].endswith('2')]
    dist = np.full(geom.N_CO, 99); cur = set(int(c) for c in co_targets); k = 0
    while cur:
        stack = list(cur)
        while stack:
            c = stack.pop()
            for m in H:
                c2 = int(geom.MCO[c, m])
                if dist[c2] == 99 and c2 not in cur: cur.add(c2); stack.append(c2)
        for c in cur: dist[c] = k
        cur = {c2 for c2 in (int(geom.MCO[c, m]) for c in cur for m in Q) if dist[c2] == 99}; k += 1
    return dist

m44, m42, m32, m78, m88, m46, m36, m54, m56, m66, m34 = [m_(*x) for x in [(4, 4), (4, 2), (3, 2), (7, 8), (8, 8), (4, 6), (3, 6), (5, 4), (5, 6), (6, 6), (3, 4)]]
claim('A1-64000', 'doc 275 rodneykinney', 'about 64,000 of about 1 million EO-solved states have a sub-7 DR', 'correct', f'{int((d <= 6).sum())} of {geom.N0}')
claim('C1-15.3', 'doc 6 Cale', '4c4e is 1 in 15.3 EOs', 'correct', f'{geom.N0 / m44.sum():.2f}')
claim('C2-lastmove', 'D2200 Tom Nelson / doc 40 Cale', '4e4c in 6: 1 in 5.2, 1 in 3.6 if the last move can be switched', 'correct', f'1 in {1 / p6(m44):.2f}; 1 in {1 / pop.targets(6)["lastF"][m44].mean():.2f}')
a = {c: p6(m44 & arm(int(c[0]), int(c[1]))) for c in ['10', '12', '11', '30', '31', '32']}
claim('T7438-mirror', 'T7438 rodneykinney / T7455 Louis', 'AR-3c-0/1/2e is the same as AR-1c-2/1/0e (4c4e); Louis: not exactly (.28 vs .29)', 'nearly: the mirror rows differ by under 0.01',
      f"30 {a['30']:.4f} vs 12 {a['12']:.4f}; 31 {a['31']:.4f} vs 11 {a['11']:.4f}; 32 {a['32']:.4f} vs 10 {a['10']:.4f}")
v = {c: p6(m44 & arm(int(c[0]), int(c[1]))) for c in ['02', '12', '30', '40', '00', '10', '21', '32', '42']}
claim('D7086-never', 'D7086 Yura Riabov', '4e4c ARM 02, 12, 30, 40 are never worth switching', 'correct (all under 4%)', ', '.join(f'{c} {v[c]:.3f}' for c in ['02', '12', '30', '40']))
claim('D7866-sub5', 'D7866 Yura Riabov', '02, 12, 03, 04 for 4e4c are under 5% sub-7', 'partly: 03 and 04 do not exist in 4c4e (edge ARM is at most 2); 02 and 12 are under 5%', f"02 {v['02']:.4f}, 12 {v['12']:.4f}; edge ARM values in 4c4e: {sorted(set(F['earm'][m44].tolist()))}")
claim('D7872-20', 'D7871-D7872 tseitsei89', '00, 10, 21, 32, 42 are more than 20% sub-7 for 4c4e', 'correct', ', '.join(f'{c} {v[c]:.3f}' for c in ['00', '10', '21', '32', '42']))
# Jay T4256: 10 of 15 sets can be sub 6, 7 can be sub 5
sets = sorted(set((F['carm'][m44] * 10 + F['earm'][m44]).tolist()))
mins = {s_: int(d[m44 & (F['carm'] * 10 + F['earm'] == s_)].min()) for s_ in sets}
n6 = sum(1 for x in mins.values() if x <= 5); n5 = sum(1 for x in mins.values() if x <= 4)
claim('T4256-sets', 'T4256 Jay (vibing)', '10 of the 15 4C4E AR sets can be sub 6 (7 of 15 can be sub 5)', 'correct' if (len(sets), n6, n5) == (15, 10, 7) else f'off by one: {n6} sets can be sub 6 (the sub-5 count, {n5}, is right)',
      f'{len(sets)} ARM sets; {n6} have a state of at most 5, {n5} of at most 4; shortest per set ' + ', '.join(f'{s_:02d}:{mins[s_]}' for s_ in sets),
      example(pick(m44 & arm(4, 1), d == 5), 'a 5-move AR-4c1e (41) state'))
m41 = m44 & arm(4, 1); louis41 = fx.state_solved_by("D' B2 F2 D R'"); assert m41[louis41] and d[louis41] == 5      # the best 4c4e AR-4c1e solution on Louis's sheet
cells('T4256-sets', n41=int(m41.sum()), n41_5=int((m41 & (d == 5)).sum()), sub6_41=frac(m41, 5), sets=len(sets), n6=n6, n5=n5)
mn = {k: int(d[m44 & (F['pairs'] == k)].min()) for k in range(5)}
mn2 = int(d[m44 & ((F['pairs'] + F['side']) <= 1)].min())
claim('T597-4movers', 'T597 rodneykinney (answering T591 Jay: "1 or 0 pairs (side pair or top pair)")', 'no 4-move 4c4e DR with 0 or 1 pairs ("any 4 moves from solved leave at least 2 bad pairs")', f'correct: with top and side pairs counted, as in the question, the shortest with at most 1 is {mn2} (with top pairs alone F2 B2 R has none, 4 side pairs, and is 3 moves)',
      'shortest by top pairs: ' + ', '.join(f'{k}p {mn[k]}' for k in range(5)), example(fx.state_solved_by('F2 B2 R'), 'state solved by F2 B2 R'))
cells('T597-4movers', min_any=mn2, min_top=[mn[k] for k in range(5)])
mm = m44 & ((F['pairs'] + F['side']) <= 1)
claim('T604-5', 'T604 Radek B', '0 or 1 top and side pairs => at best 5 moves (4c4e)', 'correct' if d[mm].min() >= 5 else 'wrong', f'shortest {int(d[mm].min())} over {int(mm.sum())} states', example(pick(mm, d == d[mm].min())))
# Evan / caycala 02 layouts
m02 = m44 & arm(0, 2)
u = m02 & (F['corners_one_layer'] == 1); nu = m02 & (F['corners_one_layer'] == 0); ce = m02 & (F['corners_edges_opposite'] == 1)
claim('D12760-02U', 'D12760-D12763 Evan / caycala', '4c4e AR 02: all corners on one layer is the only sub-7 case, 5.60%; corners on U and edges on D: 33%',
      'correct' if p6(nu) == 0 else 'wrong', f'corners on one layer {p6(u):.4f} ({int(u.sum())} states), otherwise {p6(nu):.4f} ({int(nu.sum())}); corners on one layer and both bad edges on the other {p6(ce):.4f} ({int(ce.sum())})', example(pick(ce, d <= 6)))
# Evan 4d + 1 pair by ARM; 1 pair + AR-21 by case; 4a by 2X
r = {a_: p6(m44 & cc('d') & (F['pairs'] == 1) & arm(int(a_[0]), int(a_[1]))) for a_ in ['20', '21', '22']}
claim('D14342-4d1', 'D14342 Evan', '4d + 1 pair is ~90% sub-7 for AR-21 and 0% for other AR (4c4e)', 'correct', ', '.join(f'4d 1p {k} {x:.3f}' for k, x in r.items()))
r = {l: p6(m44 & cc(l) & (F['pairs'] == 1) & arm(2, 1)) for l in 'abd'}
# "stacked" as in the sheet Evan linked in the next message (arm/pairs, tab 44-more: "all-F means all bad corners are on
# F/B", "col-F means the bad corners make columns orthogonal to F/B"): each bad corner directly above or below another,
# i.e. the layouts allF, allR and colU; the other three layouts (allU, colF, colR) are the "otherwise"
ms = m44 & cc('a') & (F['pairs'] == 1) & arm(2, 1)
allF, allR, allU = F['fb_split'] == 4, F['lr_split'] == 4, F['ud_split'] == 4
LAY = {'allF': allF, 'allR': allR, 'colU': cols_along(1) & ~allF & ~allR, 'allU': allU, 'colF': cols_along(2) & ~allU & ~allR, 'colR': cols_along(0) & ~allU & ~allF}
assert (sum(v.astype(int) for v in LAY.values())[ms] == 1).all()
st = ms & cols_along(1); ns = ms & ~cols_along(1)
assert (st == (ms & (LAY['allF'] | LAY['allR'] | LAY['colU']))).all()
lay = {k: (frac(ms & v), int((ms & v).sum())) for k, v in LAY.items()}
ok = abs(r['b'] - .29) < .006 and abs(r['d'] - .89) < .006 and abs(frac(st) - .34) < .015 and all(lay[k][0] < .05 for k in ('allU', 'colF', 'colR'))
exU = fx.state_solved_by("L U2 F2 L2 U2 D L"); assert (ms & LAY['allU'])[exU] and d[exU] == d[ms & LAY['allU']].min()
claim('D14402-21-1p', 'D14402-D14403 Evan', '1 pair + AR-21: b corners 29%, d corners 89%, a corners ~34% if stacked, < 5% otherwise', 'correct, with stacked = each bad corner directly above or below another (the layouts allF, allR, colU of the sheet Evan linked)' if ok else 'wrong',
      ', '.join(f'{l} {x:.3f}' for l, x in r.items()) + f'; a stacked {frac(st):.3f} ({int(st.sum())} states), a not stacked {frac(ns):.3f} ({int(ns.sum())}); by layout ' + ', '.join(f'{k} {x:.3f} ({n_})' for k, (x, n_) in lay.items()),
      example(exU, 'a 4a, 1 pair, AR-21 state with all four bad corners in one layer (allU, not stacked): the shortest of its layout'))
cells('D14402-21-1p', b=frac(m44 & cc('b') & (F['pairs'] == 1) & arm(2, 1)), d=frac(m44 & cc('d') & (F['pairs'] == 1) & arm(2, 1)), a=frac(ms), n_a=int(ms.sum()), stacked=frac(st), n_stacked=int(st.sum()), other=frac(ns), n_other=int(ns.sum()), min_allU=int(d[ms & LAY['allU']].min()),
      **{k: x for k, (x, n_) in lay.items()}, **{'n_' + k: n_ for k, (x, n_) in lay.items()})
r = {a_: p6(m44 & cc('a') & arm(2, int(a_))) for a_ in '012'}
claim('D14348-4a2X', 'D14348 Evan', '4a corners are basically the same for all AR-2X (4c4e)', 'wrong: 4a 20 / 21 / 22 differ by a factor of 1.1-1.8' if max(r.values()) > 1.3 * min(r.values()) else 'correct', ', '.join(f'4a 2c{k}e {x:.3f}' for k, x in r.items()))
r = {k: p6(m44 & cc(k[0], int(k[1]))) for k in ['a0', 'a2', 'b0', 'b2']}
claim('T8122-a0b0', 'T8122 rodneykinney', '4c4e without pairs: 4a-0 is better than 4a-2, but 4b-0 is worse than 4b-2', 'correct' if r['a0'] > r['a2'] and r['b0'] < r['b2'] else 'wrong', ', '.join(f'4{k[0]}-{k[1]} {x:.3f}' for k, x in r.items()))
fbr = fx.state_solved_by('F2 B2 R'); dfbr = fx.state_solved_by('D F2 B2 R')
claim('T8123-0p', 'T8123 rodneykinney (answer to T8107 Nico)', 'to catch 0-pair F2 B2 R-type DRs, switch 4a-0 and 4d-2 with no fake pairs', 'incomplete: the F2 B2 R state is 4a-0 with no fake pairs, but one U/D turn earlier (D F2 B2 R, 0 pairs, no fake pairs, 4 moves) it is 4b-2 and the rule discards it',
      f"F2 B2 R state: {fx.describe(F, fbr)}; D F2 B2 R state: {fx.describe(F, dfbr)}; 4c4e 0 pairs, no fake pairs: 4a-0 {p6(m44 & (F['pairs'] == 0) & (F['fake'] == 0) & cc('a', 0)):.3f}, 4d {p6(m44 & (F['pairs'] == 0) & (F['fake'] == 0) & cc('d')):.3f}, 4b-2 {p6(m44 & (F['pairs'] == 0) & (F['fake'] == 0) & cc('b', 2)):.3f}", example(dfbr, 'state solved by D F2 B2 R'))
z4 = m44 & (F['pairs'] == 0) & (d <= 4); caught = z4 & (cc('a', 0) | cc('d')) & (F['fake'] == 0)
assert ((z4 & ~caught) == (z4 & cc('b', 2))).all()
cells('T8123-0p', n4=int(z4.sum()), missed=int((z4 & ~caught).sum()))
mins = {k: int(d[m42 & cc(k[0], int(k[1]))].min()) for k in ['a0', 'a2', 'b0', 'b2', 'c1', 'd2']}
claim('T8149-4b2', 'T8149 rodneykinney', '4c2e 4b-2: 6 moves is the absolute minimum; 4a-2 is good', 'correct' if mins['b2'] == 6 else 'wrong', 'shortest per case: ' + ', '.join(f'4{k[0]}-{k[1]} {x}' for k, x in mins.items()) + f"; 4a-2 sub-7 {p6(m42 & cc('a', 2)):.3f}, 4b-2 {p6(m42 & cc('b', 2)):.3f}")
# rodneykinney T8147: "3qt corners" in 4c2e.  rodneykinney counts quarter turns from the trigger of the DRM in hand
# (T8132 "0qt from the trigger"; T8149: 4c2e 4b-2 "corners are 2qt"), and the 4c2e table T8140 leaves out 4a at every
# pair count.  The corners of R U2 R are 4b-0; three U/D quarter turns from them (half turns free) are 4a-0 and 4a-4,
# which the sheet of the time (DRM corner variant+pair stats) folds into one row, 4a-0.
trig = fx.state_solved_by('R U2 R'); assert m42[trig] and cc('b', 0)[trig] and F['carm'][trig] == 0
co_trig = sorted({fx.state_solved_by(' '.join([a_, x_, b_])) // geom.N_SL for f_ in 'RL' for a_ in (f_, f_ + "'") for x_ in ('U2', 'D2') for b_ in (f_, f_ + "'")})
qd = qt_from(co_trig); nc_co = fx.bad.sum(1); cc_co = fx.corner_case(fx.bad); ca_co = fx.arm_c.sum(1)
qt = {}
for c_ in np.flatnonzero(nc_co == 4):
    qt.setdefault(f"4{'abcd'[cc_co[c_]]}-{int(ca_co[c_])}", set()).add(int(qd[c_]))
assert all(len(v) == 1 for v in qt.values()); qt = {k: v.pop() for k, v in sorted(qt.items())}
assert qt['4b-0'] == 0 and qt['4b-2'] == 2 and [k for k, v in qt.items() if v == 3] == ['4a-0', '4a-4']
fold = m42 & cc('a') & (F['carm'] != 2); a0 = m42 & cc('a', 0); a4 = m42 & cc('a', 4)
pf = [frac(fold & (F['pairs'] == k)) for k in range(3)]; p0_ = [frac(a0 & (F['pairs'] == k)) for k in range(3)]; p4_ = [frac(a4 & (F['pairs'] == k)) for k in range(3)]
ex3 = fx.state_solved_by("R F2 B2 R F2 R'"); assert (a0 & (F['pairs'] == 2))[ex3] and d[ex3] == 6
claim('T8147-3qt', 'T8147 rodneykinney (4c2e table T8140; T8132, T8149)', '4c2e: because it is a three-move trigger, no number of pairs saves 3qt corners (4a-0: three U/D quarter turns from the corners of R U2 R, which are 4b-0)',
      'depends on the fold: no 4a-0 case is under 6 moves and the row as the sheet folds it (corner ARM 0 or 4) is at most 25% sub-7; with corner ARM 0 alone, 2 pairs are 50%',
      '4a-0 as the sheet folds it (corner ARM 0 or 4): ' + ', '.join(f'{k}p {x:.3f}' for k, x in enumerate(pf)) + '; corner ARM 0: ' + ', '.join(f'{k}p {x:.3f}' for k, x in enumerate(p0_))
      + '; corner ARM 4: ' + ', '.join(f'{k}p {x:.3f}' for k, x in enumerate(p4_)) + f'; shortest: corner ARM 0 {int(d[a0].min())}, corner ARM 4 {int(d[a4].min())}'
      + '; U/D quarter turns (half turns free) from the corners of R U2 R: ' + ', '.join(f'{k} {v}' for k, v in qt.items()),
      example(ex3, 'a 4c2e with 4a-0 corners (corner ARM 0) and 2 pairs: 6 moves, with three R quarter turns'))
assert max(p4_) == 0
cells('T8147-3qt', fold=pf, arm0=p0_, arm4=p4_, min_arm0=int(d[a0].min()), min_arm4=int(d[a4].min()), n_arm0_2p=int((a0 & (F['pairs'] == 2)).sum()), qt=qt)
ja = m42 & (F['jzp'] == 1) & cc('a'); jb = m42 & (F['jzp'] == 1) & cc('b')
claim('D16268-4a', 'D16268 tseitsei89 (answering D16267 Zagros: "Even jzp you can get 4a1 corners and it can just be bad")', '4c2e with 4a corners almost always sucks', 'depends: right for JZP, which is what the exchange is about; over all of 4c2e 4a is at the 4c2e rate',
      f"4c2e JZP: 4a {frac(ja):.3f} ({int(ja.sum())} states), 4b {frac(jb):.3f} ({int(jb.sum())}); all 4c2e: 4a {p6(m42 & cc('a')):.3f} vs {p6(m42):.3f}")
cells('D16268-4a', jzp_a=frac(ja), n_jzp_a=int(ja.sum()), jzp_b=frac(jb), n_jzp_b=int(jb.sum()), all_a=frac(m42 & cc('a')), all=frac(m42))
claim('D15161-jzp-b', 'D15161 Daichi', '4c2e 0 pairs: JZP with b corners is way better than with a corners', 'correct' if p6(m42 & (F['pairs'] == 0) & (F['jzp'] == 1) & cc('b')) > p6(m42 & (F['pairs'] == 0) & (F['jzp'] == 1) & cc('a')) else 'wrong',
      f"b {p6(m42 & (F['pairs'] == 0) & (F['jzp'] == 1) & cc('b')):.3f}, a {p6(m42 & (F['pairs'] == 0) & (F['jzp'] == 1) & cc('a')):.3f}")
claim('D12737-41', 'D12737 caycala', '4c2e ARM 41 with 0 pairs is 0% sub-7?', 'correct' if p6(m42 & arm(4, 1) & (F['pairs'] == 0)) == 0 else 'wrong', f"{p6(m42 & arm(4, 1) & (F['pairs'] == 0)):.4f} over {int((m42 & arm(4, 1) & (F['pairs'] == 0)).sum())} states")
q7 = {nm: float((d[m] <= 7).mean()) for nm, m in [('3c6e', m36), ('4c4e', m44), ('8c8e', m88), ('7c8e', m78), ('4c2e', m42)]}
T6 = pop.targets(6)
qi = {nm: float(T6['inv'][m].mean()) for nm, m in [('3c6e', m36), ('4c4e', m44), ('8c8e', m88), ('7c8e', m78), ('4c2e', m42)]}
ql = {nm: float(T6['lastF'][m].mean()) for nm, m in [('3c6e', m36), ('4c4e', m44), ('8c8e', m88), ('7c8e', m78), ('4c2e', m42)]}
# Cale's last-move sheet (doc 40) has 8e8c as the 4,900 cases with a 4-4 twist split (and 8e7c as one of its two mirror halves)
m88_44 = m88 & (F['tw1'] == 4) & (F['tw2'] == 4); ql88_44 = float(T6['lastF'][m88_44].mean())
qfb = {nm: float(T6['lastFB'][m].mean()) for nm, m in [('3c6e', m36), ('4c4e', m44), ('8c8e', m88), ('7c8e', m78), ('4c2e', m42)]}
cells('D6979-3c6e', last={k: 1 / x for k, x in ql.items()}, lastfb={k: 1 / x for k, x in qfb.items()}, last88_44=1 / ql88_44, n88_44=int(m88_44.sum()), plain6=1 / frac(m36), plain7=1 / frac(m36, 7))
claim('D6979-3c6e', 'D6979 Noah Swor', '3c6e: 1/7 for 7 moves, against 1/3 for 4e4c, 8c8e, 8e7c, 2e4c', f"direction right, but no reading gives both numbers: the 1/3 fits DR in 6 with the EO's last two turns free (Cale's last-move sheet, tab F B), on which 3c6e is 1 in {1 / qfb['3c6e']:.1f}; with the last turn free it is 1 in {1 / ql['3c6e']:.1f}; one side, DR <= 7, it is 1 in {1 / frac(m36, 7):.1f}, so the 1/7 is not reproduced",
      f"EO's last move switchable, DR <= 6 (8c8e with a 4-4 twist split, the sheet's 8e8c tab, 1 in {1 / ql88_44:.2f}): " + ', '.join(f'{k} 1 in {1 / x:.2f}' for k, x in ql.items()) + '; better of normal and inverse, DR <= 6: ' + ', '.join(f'{k} 1 in {1 / x:.2f}' for k, x in qi.items()) + '; one side DR <= 7: ' + ', '.join(f'{k} 1 in {1 / x:.2f}' for k, x in q7.items()))
mins = {f'{a_}{b_}': int(d[m36 & arm(a_, b_)].min()) for a_ in range(4) for b_ in range(4) if (m36 & arm(a_, b_)).sum()}
claim('D6982-3c6e', 'D6982 Jay', '3c6e: AR-2C1E is the only subset where +4 to DR is possible', 'correct' if [k for k, x in mins.items() if x <= 4] == ['21'] else 'wrong', 'shortest per ARM: ' + ', '.join(f'{k} {x}' for k, x in mins.items()))
claim('T1805-4c6e', 'T1805 Cale', '4c6e: even with the full move set, sub-7 is 1 in 22', 'correct', f'any turns: 1 in {1 / p6(m46, DA):.1f}; EO kept: 1 in {1 / p6(m46):.1f}')
claim('D7854-5c4e21', 'D7854 Yura Riabov / D10597 beef beans', '5c4e AR 21 (the 4-move trigger one) is only 15%; 5c4e/5c6e/6c6e 2c1e all around 15%', 'correct',
      ', '.join(f'{nm} 21 {p6(m & arm(2, 1)):.3f}' for nm, m in [('5c4e', m54), ('5c6e', m56), ('6c6e', m66)]))
claim('T9348-5c4e', 'T9348 rodneykinney', '5c4e with 2 pairs has 40% chance of sub-8', 'not reproduced: any optimal DR gives 57% (rodneykinney may count findable solutions only)', f"DR <= 7: {float((d[m54 & (F['pairs'] == 2)] <= 7).mean()):.3f} EO-kept, {float((DA[m54 & (F['pairs'] == 2)] <= 7).mean()):.3f} any turns")
mm = m78 & (F['drm_c'] == 7)
nb_in = (F['drm_c'] - F['carm']); ok = (F['side'][m78] == nb_in[m78]).all()
claim('T9450-7c8e-side', 'T9450 rodneykinney', '7c8e: every bad in-ARM corner forms a side pair', 'correct' if ok else 'wrong', f"side pairs = bad corners not out of AR on {int((F['side'][m78] == nb_in[m78]).sum())} of {int(m78.sum())} 7c8e states")
v78 = {f'{a_}{b_}': (int(d[m78 & arm(a_, b_)].min()), int(d[m78 & arm(a_, b_)].max())) for a_ in range(8) for b_ in range(5) if (m78 & arm(a_, b_)).sum()}
claim('D5086-7c8e', 'D5086 Jay', '7c8e: 1C0E is always 5-6 and 2C1E is the only one that can give sub 4', 'correct' if v78['10'] == (5, 6) and [k for k, x in v78.items() if x[0] <= 3] == ['21'] else 'wrong', f"1C0E {v78['10'][0]}–{v78['10'][1]}" + '; ARMs with a state of 3 or fewer: ' + str([k for k, x in v78.items() if x[0] <= 3]))
e4 = p6(m78 & (F['earm'] == 4)); e3 = {c_: p6(m78 & arm(c_, 3)) for c_ in range(8) if (m78 & arm(c_, 3)).sum()}; e2 = p6(m78 & (F['earm'] == 2)); e3a = p6(m78 & (F['earm'] == 3))
claim('T9279-7c8e', 'T9279 tseitsei89', '7c8e: edge ARM 4 is always 0% sub-7; 3 is much better than 2 but only good if corner ARM >= 4', 'correct for edge ARM 4; "3 better than 2" holds', f'edge ARM 4 {e4:.4f}; edge ARM 3 {e3a:.3f} vs 2 {e2:.3f}; edge ARM 3 by corner ARM ' + ', '.join(f'{k} {x:.3f}' for k, x in e3.items()))
zero = sum(int((m78 & arm(a_, b_)).sum()) for a_ in range(8) for b_ in range(5) if (m78 & arm(a_, b_)).sum() and p6(m78 & arm(a_, b_)) == 0)
nsets = sum(1 for a_ in range(8) for b_ in range(5) if (m78 & arm(a_, b_)).sum()); nzero = sum(1 for a_ in range(8) for b_ in range(5) if (m78 & arm(a_, b_)).sum() and p6(m78 & arm(a_, b_)) == 0)
claim('D7884-half', 'D7884-D7889 Yura Riabov', 'for 7c8e, half the cases are 0% chance of sub-7 DR', f'correct by ARM set ({nzero} of {nsets}); those sets hold {zero / m78.sum():.3f} of the states', f'{nzero} of {nsets} ARM sets have no sub-7 state')
claim('D7800-7c8e21', 'D7800 / D7889 Yura Riabov', 'DR-7C8E AR-2C1E is over 70% sub-7', 'correct', f'{p6(m78 & arm(2, 1)):.3f}')
mm = m78 & arm(2, 1) & (d > 6)
claim('E7-counter', 'D11819-D11825 tseitsei89', 'a 7c8e AR-2c1e with no sub-7 solution exists', 'correct', f'{int(mm.sum())} of {int((m78 & arm(2, 1)).sum())} 7c8e AR-2c1e states have no sub-7 DR', example(pick(mm)))
m5 = m78 & (F['pairs'] == 5)
r = {c_: p6(m5 & arm(int(c_[0]), int(c_[1]))) for c_ in ['20', '54']}
claim('D15161-5p', 'D15161 Daichi / D15170 Fanti', '7c8e with 5 pairs: 20 and 54 are 0% sub-7, the rarest 5p cases; 5 pairs is still 54% in general', 'correct' if max(r.values()) == 0 else 'wrong', f"20 {r['20']:.3f} ({int((m5 & arm(2, 0)).sum())} states), 54 {r['54']:.3f} ({int((m5 & arm(5, 4)).sum())}); 5 pairs {p6(m5):.3f}")
m4 = m78 & (F['pairs'] == 4)
r = {c_: p6(m4 & arm(int(c_[0]), int(c_[1]))) for c_ in ['11', '12', '33', '41', '62', '21']}
sub6 = [f'{a_}{b_}' for a_ in range(8) for b_ in range(5) if (m4 & arm(a_, b_)).sum() and d[m4 & arm(a_, b_)].min() <= 5]
claim('D15175-4p', 'D15175-D15176 Fanti', '7c8e 4 pairs: 11/12/33/41/62 are 20-23% sub-7; only 21 can be sub-6 on 4p', 'partly: ' + ('the sub-6 part is correct' if sub6 == ['21'] else 'the sub-6 part is wrong'),
      ', '.join(f'{k} {x:.3f}' for k, x in r.items()) + f'; ARMs with a 4-pair state of at most 5: {sub6}')
# 3c2e always / wen never misses a 5-mover / sub-6 for RZP in 6
claim('D7286-3c2e', 'D7286 / T9321 tseitsei89', '3c2e is pretty much always worth NISSing, even as a 6-move RZP', 'depends on the threshold: after a 6-move RZP the target is DR in 5', f'DR <= 6 {p6(m32):.3f}; DR <= 5 {float((d[m32] <= 5).mean()):.3f}')
mm = m32 & ((F['pairs'] + F['fake'] + F['split_pairs']) == 0)
claim('D16512-wen', 'D16512 wen', '3c2e: switching on a pair, fake pair or split pair never misses a 5-mover', 'correct' if d[mm].min() >= 6 else 'wrong', f'states with none of the three: {int(mm.sum())}, shortest DR {int(d[mm].min())}, sub-7 {p6(mm):.3f}')
# torchlight / KrzychXyz
claim('T4250-bias', 'T4250 torchlight', 'RZP-reached 4c4e cases are biased toward cases that leave 4c4e in more ways', 'correct on the same side, gone after a switch',
      f"4c4e sub-7 uniform {p6(m44):.4f}; after an RZP of 5, same side {float((P['P2n_5'][m44] * (d[m44] <= 6)).sum() / P['P2n_5'][m44].sum()):.4f}; after the switch {float((P['P2_5'][m44] * (d[m44] <= 6)).sum() / P['P2_5'][m44].sum()):.4f}")
claim('T4265-natural', 'T4265 KrzychXyz', 'are naturally occurring 4c4e better than set-up ones?', 'yes, slightly, on the same side (0.192 vs 0.183); identical after a switch', 'see T4250-bias')
claim('D14218-indep', 'D14218 caycala / D14220 Daichi', 'the two DR axes are roughly independent', 'correct to within 0.004 for the better-of-two chance (a small positive dependence)', 'see q4.tsv')
claim('T4357-sameaxis', 'T4357 Louis (corrected in T4361)', 'ARM remains the same on the same axis after a switch', 'wrong (Louis corrected it himself): the same-axis ARM is kept on about 10% of cubes; the other axis gets it on 100%', 'see checks_niss.tsv')
claim('T4202-swap', 'T4202 Cale / D7896 wen', 'the ARM of one DR axis on normal is the ARM of the other DR axis on inverse', 'correct (every sampled cube)', 'see checks_niss.tsv')
claim('doc320-rlcount', 'doc 320 rodneykinney', 'R/L stickers on the U/D faces = corners out of AR on inverse', 'correct (every sampled cube)', 'see checks_niss.tsv')
claim('doc320-flow', 'doc 320 rodneykinney (flow chart); EO-DR-618 asks for a proof', 'NISS flow chart for the corner case on inverse', 'correct on every sampled 4c4e cube (a check by sampling, not a proof)', 'see checks_niss.tsv')
claim('doc384-trace', 'doc 384 (wen), D12044-D12080 cuber, doc 69 rodneykinney', 'pair tracing: bad edge in E + misoriented corner whose E-side stickers show its colours = a pair on inverse', 'correct (every sampled cube)', 'see checks_niss.tsv')
any3 = (F['pairs'] + F['side']) >= 3
claim('doc69-3p', 'doc 69 rodneykinney', 'for DR <= 6 look for an inverse with at least three pairs (top and side pairs together: the lazy estimate 12 - 2pt - 2ps is then 6 or less); otherwise save the NISS', 'depends on the cut: 3+ top and side pairs is 39% sub-7 and holds 64% of the sub-7 states',
      f"3+ top and side pairs: share {float(any3[m44].mean()):.3f}, sub-7 {p6(m44 & any3):.3f}, recall {float((any3 & (d <= 6))[m44].sum() / (d[m44] <= 6).sum()):.3f}; 3+ top pairs alone: share {float((F['pairs'][m44] >= 3).mean()):.3f}, sub-7 {p6(m44 & (F['pairs'] >= 3)):.3f}, recall {float(((F['pairs'] >= 3) & (d <= 6))[m44].sum() / (d[m44] <= 6).sum()):.3f}")
# caycala D13393: the 3-pair group left out, on its own
g3 = m44 & (F['pairs'] == 3) & (F['corners_one_layer'] == 1); g4 = m44 & (F['pairs'] == 4) & (F['corners_one_layer'] == 1)
claim('D13393-3p', 'D13393 caycala', '4c4e: the only 3+ pairs case not worth switching is 3 pairs with all white or all yellow corners (all four bad corners in one layer)', 'depends on the cut: a third of the group is sub-7 and none of it under 6 moves, against about four in five for 3 pairs',
      f"3 pairs, all bad corners in one layer: {frac(g3):.3f} ({int(g3.sum())} states, shortest {int(d[g3].min())}); all 3 pairs {frac(m44 & (F['pairs'] == 3)):.3f}; 4 pairs, all bad corners in one layer: {int(g4.sum())} states, longest {int(d[g4].max())}", example(pick(g3, d == d[g3].min())))
cells('D13393-3p', p=frac(g3), n=int(g3.sum()), min=int(d[g3].min()), p3=frac(m44 & (F['pairs'] == 3)), n4=int(g4.sum()), max4=int(d[g4].max()))
# Yura Riabov D16930: 8c8e with JZP on the other axis (ARM 00 after the switch) is R L
j88 = m88 & (F['jzp'] == 1)
claim('D16930-8c8e-jzp', 'D16930 Yura Riabov (T3767 Jay: the R L U D premove technique)', '8c8e with JZP on the other axis is guaranteed to be R L to DR after the switch', 'correct' if (d[j88] == 2).all() and j88[fx.state_solved_by('R L')] else 'wrong',
      f'{int(j88.sum())} 8c8e case with ARM 00 after the switch, DR in {int(d[j88].max())}', example(fx.state_solved_by('R L'), 'state solved by R L'))
cells('D16930-8c8e-jzp', n=int(j88.sum()), d=int(d[j88].max()))
jt = fx.state_solved_by("F2 U' F2 R")
claim('T3210-lazy', 'T3210 JTuu on doc 69', "Rodney's lazy estimate 12 - 2pt - 2ps gives 7 for F2 U' F2 R", 'correct', f"state solved by F2 U' F2 R: {fx.describe(F, jt)}; estimate {12 - 2 * int(F['pairs'][jt]) - 2 * int(F['side'][jt])}", example(jt, "state solved by F2 U' F2 R"))
r = {k: p6(m88 & arm(4, 2) & (F['arm_corner_case'] == 'abcd'.index(k))) for k in 'ab'}
claim('T11488-8c8e', 'T11488-T11500 trangium (from the arm/pairs sheet)', '8c8e AR-4c2e by corner case of the out-of-AR corners: 4b 12%, 4a 43%', 'correct' if abs(r['b'] - .12) < .006 and abs(r['a'] - .43) < .006 else f'EO-kept numbers differ', f"4a {r['a']:.3f} (any-turn {p6(m88 & arm(4, 2) & (F['arm_corner_case'] == 0), DA):.3f}), 4b {r['b']:.3f} (any-turn {p6(m88 & arm(4, 2) & (F['arm_corner_case'] == 1), DA):.3f})")
# Fanti's measured rule performance
G = list(csv.DictReader(open(os.path.join(pop.OUT, 'grades.tsv')), delimiter='\t'))
for rid, drm, txt in [('44-fanti', '4c4e', '35.2% switches, 42.6% success, 15.0% total, 4.3% discarded with sub-7'), ('42-fanti', '4c2e', '43.9%, 38.8%, 17.0%, 2.2%'),
                      ('78-fanti', '7c8e', '23.5%, 51.5%, 12.1%, 4.3%'), ('32-fanti-6', '3c2e', '50.0%, 34.4% sub-6, 17.2%, 2.0%'), ('34-fanti', '3c4e', '23.7%, 26.2%, 6.2%, 3.9%')]:
    g = next(x for x in G if x['id'] == rid and x['population'] == 'P1')
    import rules as rl
    rr = next(x for x in rl.RULES if x[0] == rid); mm = m_(*rr[1]); sw = rr[4](F)[mm]; y = DA[mm] <= rr[5]
    claim(f'doc583-{drm}', 'doc 583 Fanti (armpairs_1.txt)', f'{drm} rule performance: {txt}', 'correct (exactly, with the any-turn optimum)',
          f"any-turn: share {sw.mean():.3f}, success {y[sw].mean():.3f}, total {(y & sw).mean():.3f}, discarded {(y & ~sw).mean():.4f}; EO-kept: success {float(g['precision']):.3f}, discarded {float(g['target_states_discarded']):.4f}")
# Rodney T9480: DRMs outside the top 10
outside = []
for c_ in range(9):
    for e_ in range(0, 10, 2):
        if (c_, e_) in [(4, 4), (3, 2), (7, 8), (5, 4), (5, 6), (4, 2), (6, 6), (4, 6), (3, 4), (8, 8)]: continue
        mm = m_(c_, e_)
        if mm.sum() and (c_, e_) != (0, 0): outside.append((p6(mm), int((d[mm] <= 6).sum()), f'{c_}c{e_}e'))
outside.sort(reverse=True)
claim('T9480-rest', 'T9479-T9480 zakimoshi / rodneykinney', 'the DRMs outside the top 10 are not worth looking at', 'by sub-7 chance some are better than most of the top 10 but rare: ' + ', '.join(f'{n} {p:.3f} ({k} sub-7 states)' for p, k, n in outside[:5]), '')
with open(os.path.join(pop.OUT, 'claims.tsv'), 'w') as f:
    f.write('id\tsource\tclaim\tverdict\tnumbers\texample (setup from solved, optimal DR, replayed on cube.py)\n')
    for r_ in rows: f.write('\t'.join(r_) + '\n')
# Jay's leads for the low DRMs (D10593, 23 Mar 2025): switched-case share and sub-7 rate of each named group
lead = {}
for key, drm_m, m in [('66_jzp', m66, F['jzp'] == 1), ('66_anti', m66, F['anti_ar'] == 1), ('66_10', m66, arm(1, 0)), ('66_53', m66, arm(5, 3)),
                      ('54_fake', m54, F['fake_jzp'] == 1), ('56_fake', m56, F['fake_jzp'] == 1), ('56_10', m56, arm(1, 0))]:
    g = drm_m & m
    lead[key] = dict(n=int(g.sum()), share=float(g.sum()) / int(drm_m.sum()), p=frac(g), base=frac(drm_m))
cells('D10593-low', **lead)
json.dump(EX, open(os.path.join(pop.BIG, 'claims_examples.json'), 'w'), indent=1)
json.dump(CELLS, open(os.path.join(pop.OUT, 'claims_cells.json'), 'w'), indent=1)
for r_ in rows: print(f'{r_[0]:16s} | {r_[3][:90]:90s} | {r_[4][:150]}')
