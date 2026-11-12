#!/usr/bin/env python3
"""The 'read it on the other side' predictors of the notes, tested on uniformly random full cubes (F/B EO solved) of
is-dr-xs-worth-it's sticker model (cube.py, coords.make): the prediction is read off the stickers of the normal cube
S, the truth is the feature of the inverse S^-1 (geometric features of features.py).
  1. ARM axis swap (Cale T4202, wen D7896): ARM for DR on one axis on normal = ARM for DR on the other axis on inverse.
  2. doc 320: number of R/L stickers on the U/D faces (corners) = corner ARM on inverse (same DR axis).
  3. doc 320 flow chart: corner case on inverse from the colours of the misoriented corners.
  4. Pair tracing (doc 384 wen; cuber D12044-D12080; doc 69 Rodney): pairs on inverse from the E-slice bad edges and
     the misoriented corners' colours.
Output: out/checks_niss.tsv; mismatches are kept as examples (scramble = a sequence reaching S)."""
import os, sys, random, collections
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import geom, pop
from geom import cube, coords
F = pop.feat(); d = F['d']
FACES = 'UDRLFB'; AXF = {'U': 1, 'D': 1, 'R': 0, 'L': 0, 'F': 2, 'B': 2}
CF, EF = coords.CF, coords.EF
def rand_state(rng, want=None):
    """Uniform F/B-EO-solved cube; with want=(c, e), uniform within that DRM (coset first, then the permutations)."""
    if want is None:
        ix = rng.randrange(geom.N0)
    else:
        idx = np.flatnonzero((F['drm_c'] == want[0]) & (F['drm_e'] == want[1])); ix = int(idx[rng.randrange(len(idx))])
    co, sl = divmod(ix, geom.N_SL)
    ct = [int(x) for x in geom.CT[co]]
    epos = list(geom.COMB[sl]); home_e = [i for i in range(12) if coords.E_PIECE[i]]; home_o = [i for i in range(12) if not coords.E_PIECE[i]]
    while True:
        cp = list(range(8)); rng.shuffle(cp)
        e_p = home_e[:]; rng.shuffle(e_p); o_p = home_o[:]; rng.shuffle(o_p)
        ep = [None] * 12; it_e = iter(e_p); it_o = iter(o_p)
        for i in range(12): ep[i] = next(it_e) if i in epos else next(it_o)
        par = lambda p: sum(1 for a in range(len(p)) for b in range(a + 1, len(p)) if p[a] > p[b]) % 2
        if par(cp) == par(ep): break
    s = coords.make(cp=cp, ct=ct, ep=ep, ef=[0] * 12)
    assert geom.ix_of_state(s) == ix
    return s
Y_TO = {}  # conjugation that carries R/L to U/D keeping F/B: the view of the cube after a z rotation
def view_rl(s):
    """The cube turned so that R/L becomes U/D (F/B stays F/B): z' s z as stickers."""
    z = cube.do(cube.SOLVED, 'z'); zi = cube.do(cube.SOLVED, "z'")
    return cube.compose(cube.compose(zi, s), z)
def arm_of(s):
    ix = geom.ix_of_state(s); return int(F['carm'][ix]), int(F['earm'][ix])
def rl_on_ud(s):
    """R/L-coloured stickers on the U/D faces, corner places only."""
    n = 0
    for i in range(8):
        for k in range(3):
            pl = CF[i][k]
            if geom.FACE_OF_NORMAL[cube.ST[pl][1]] in 'UD' and cube.colour(s, pl) in 'RL': n += 1
    return n
def bad_corner_colours(s):
    """Colours of the misoriented corners (U/D sticker not on U/D)."""
    out = []
    for i in range(8):
        cols = [cube.colour(s, CF[i][k]) for k in range(3)]
        if cols[0] not in 'UD': out.append(cols)
    return out
def flow_chart(s):
    """doc 320: odd R/L stickers on U/D -> 4c; even -> some colour exactly 1 or 3 times among the bad corners -> 4b;
    else two corners sharing two colours -> 4a; else 4d."""
    if rl_on_ud(s) % 2 == 1: return 2
    bc = bad_corner_colours(s)
    cnt = collections.Counter(c for cols in bc for c in cols)
    if any(v in (1, 3) for v in cnt.values()): return 1
    for a in range(len(bc)):
        for b in range(a + 1, len(bc)):
            if len(set(bc[a]) & set(bc[b])) >= 2: return 0
    return 3
def flow_chart_ud_rl(s):
    """The same with only U, D, R, L colours counted in the 1-or-3 test (Rodney's code uses those faces)."""
    if rl_on_ud(s) % 2 == 1: return 2
    bc = bad_corner_colours(s)
    cnt = collections.Counter(c for cols in bc for c in cols if c in 'UDRL')
    if any(cnt.get(c, 0) in (1, 3) for c in 'UDRL'): return 1
    for a in range(len(bc)):
        for b in range(a + 1, len(bc)):
            if len(set(bc[a]) & set(bc[b])) >= 2: return 0
    return 3
def traced_pairs(s, variant):
    """Pairs on inverse by tracing on normal.  Bad edges in E: U/D pieces in the E slice; their two colours.
    variant 'side': a misoriented corner whose two side-face stickers (the ones touching the E slice) show the edge's
    two colours; 'notud': a misoriented corner showing the edge's two colours, neither on the U/D face (doc 69).
    Counted per (edge, corner) match."""
    edges = []
    for i, p in enumerate(geom.EDGES):
        if p[1] == 0:
            cols = {cube.colour(s, EF[i][0]), cube.colour(s, EF[i][1])}
            if cols & set('UD'): edges.append(cols)
    n = 0
    for i in range(8):
        cols = [cube.colour(s, CF[i][k]) for k in range(3)]
        if cols[0] in 'UD': continue
        side = {cols[1], cols[2]}
        for ec in edges:
            if variant == 'side' and side == ec: n += 1
            if variant == 'notud' and ec <= set(cols) and all(cube.colour(s, CF[i][k]) != c or k != 0 for k in range(3) for c in ec): n += 1
    return n

if __name__ == '__main__':
    rng = random.Random(6)
    nsamp = int(sys.argv[1]) if len(sys.argv) > 1 else 4000
    res = collections.defaultdict(lambda: [0, 0, None])
    def tally(name, ok, ex):
        r = res[name]; r[0] += 1; r[1] += ok
        if not ok and r[2] is None: r[2] = ex
    for t in range(nsamp):
        for want in (None, (4, 4)):
            s = rand_state(rng, want); si = cube.inverse(s)
            ex = ' '.join(cube.inv_seq(geom.path_to_dr(geom.ix_of_state(s), d)))   # a sequence with the same coset only
            tag = 'uniform' if want is None else '4c4e'
            # 1. axis swap: ARM(U/D DR, normal) vs ARM(R/L DR, inverse)
            tally(f'ARM axis swap: ARM for U/D DR on normal = ARM for R/L DR on inverse ({tag})', arm_of(s) == arm_of(view_rl(si)), None)
            tally(f'ARM for U/D DR on normal = ARM for U/D DR on inverse, same axis (Louis T4357, retracted in T4361; not expected) ({tag})', arm_of(s) == arm_of(si), None)
            # 2. R/L stickers on U/D = corner ARM on inverse
            tally(f'R/L stickers on U/D faces (normal) = corner ARM on inverse ({tag})', rl_on_ud(s) == arm_of(si)[0], None)
            if want == (4, 4):
                truth = int(F['corner_case'][geom.ix_of_state(si)])
                tally('doc 320 flow chart (all six colours) = corner case on inverse (4c4e)', flow_chart(s) == truth, None)
                tally('doc 320 flow chart (U D R L colours in the 1-or-3 test) = corner case on inverse (4c4e)', flow_chart_ud_rl(s) == truth, None)
            tp = int(F['pairs'][geom.ix_of_state(si)])
            tally(f'pair tracing, side stickers match the E-slice bad edge = pairs on inverse ({tag})', traced_pairs(s, 'side') == tp, None)
    with open(os.path.join(pop.OUT, 'checks_niss.tsv'), 'w') as f:
        f.write('check\tcubes\tholds\n')
        for k, (n, ok, ex) in res.items():
            f.write(f'{k}\t{n}\t{ok}\n'); print(f'{ok:6d}/{n:6d}  {k}')
