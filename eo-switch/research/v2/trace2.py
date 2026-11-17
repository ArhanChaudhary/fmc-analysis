#!/usr/bin/env python3
"""Every read the cards use, done on the NORMAL side with colours only, checked against the feature of the inverse
on uniformly random F/B-EO-solved cubes (the sampler of src/niss_checks.py).  Colours are named by the face they
belong to (U D R L F B); for an F/B EO and a U/D DR the U/D colours are white/yellow, F/B green/blue, R/L red/orange.

Pieces looked at on normal:
  misoriented corners (U/D colour not on U/D): `top` = the colour showing on the U/D face, `sides` = the other two.
  U/D edges sitting in the E slice (they are the bad U/D-layer edges of the inverse): its U/D colour and side colour.
  E-slice edges sitting in a U/D layer (they are the holes of the inverse): its two colours.
Output: out/checks_trace2.tsv.   usage: trace2.py [cubes per DRM]"""
import os, sys, random, collections
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, '..', 'src')); sys.path.insert(0, HERE)
import geom
from geom import cube, coords
from niss_checks import rand_state, CF, EF
from lib import F
import niss_checks
def corners(s):
    """Misoriented corners of the normal cube: (top colour, set of the two side colours, U/D colour)."""
    out = []
    for i in range(8):
        cols = [cube.colour(s, CF[i][k]) for k in range(3)]          # cols[0] is the sticker on the U/D face
        if cols[0] in 'UD': continue
        ud = [c for c in cols if c in 'UD'][0]
        out.append((cols[0], frozenset(cols[1:]), ud))
    return out
def ud_edges_in_E(s):
    """U/D edges sitting in the E slice: (U/D colour, side colour)."""
    out = []
    for i, p in enumerate(geom.EDGES):
        if p[1] == 0:
            cols = [cube.colour(s, EF[i][0]), cube.colour(s, EF[i][1])]
            if set(cols) & set('UD'):
                ud = [c for c in cols if c in 'UD'][0]; sd = [c for c in cols if c not in 'UD'][0]
                out.append((ud, sd))
    return out
def E_edges_out(s):
    out = []
    for i, p in enumerate(geom.EDGES):
        if p[1] != 0:
            cols = {cube.colour(s, EF[i][0]), cube.colour(s, EF[i][1])}
            if not cols & set('UD'): out.append(frozenset(cols))
    return out
def reads(s):
    cs = corners(s); es = ud_edges_in_E(s); hs = E_edges_out(s)
    r = {}
    per_edge = []; fake = 0
    for ud, sd in es:
        ec = frozenset((ud, sd))
        n = sum(1 for top, sides, _ in cs if sides == ec)                          # both of the edge's colours on the corner's side stickers
        f = sum(1 for top, sides, cud in cs if top == sd and cud == ud)            # the corner has both colours but shows the edge's side colour on top
        per_edge.append(n); fake += f
    r['pairs'] = sum(per_edge)
    r['edges_paired'] = sum(1 for n in per_edge if n >= 1)
    r['fake'] = fake
    r['carm'] = sum(1 for top, _, _ in cs if top in 'RL')
    r['earm'] = sum(1 for ud, sd in es if sd in 'FB')
    # side pairs: an E-slice edge out of the slice, and a corner with both its colours showing the F/B one on top
    r['side'] = sum(1 for h in hs for top, sides, _ in cs if h <= (sides | {top}) and top in 'FB')
    # holes: the two E-slice edges out of the slice share an R/L colour (0), nothing (1), an F/B colour (2)
    if len(hs) == 2:
        common = hs[0] & hs[1]
        r['hole_cfg'] = 0 if common & set('RL') else (2 if common & set('FB') else 1)
    # layers
    nu = sum(1 for _, _, cud in cs if cud == 'U')
    r['ud_split'] = max(nu, len(cs) - nu)
    if len(es) >= 2: r['edges_same_layer'] = int(len({ud for ud, _ in es}) == 1)
    # corner case (4 bad corners): rodneykinney's flow chart
    if len(cs) == 4:
        r['cc'] = niss_checks.flow_chart(s)
    # columns: two misoriented corners with the same two side colours (one white, one yellow) sit above each other on the inverse
    r['cols_bad'] = sum(1 for i in range(len(cs)) for j in range(i + 1, len(cs)) if (cs[i][1] | {cs[i][0]}) - {cs[i][2]} == (cs[j][1] | {cs[j][0]}) - {cs[j][2]})
    # split pairs (wen): a U/D edge in the E slice and a misoriented corner with the same U/D colour, not sharing its
    # side colour, both out of AR or both in AR on the inverse (edge side colour F/B <-> corner top colour R/L)
    r['split_pairs'] = sum(1 for ud, sd in es for top, sides, cud in cs if cud == ud and sd not in sides and sd != top and ((sd in 'FB') == (top in 'RL')))
    return r
TRUTH = {'pairs': 'pairs', 'edges_paired': 'edges_paired', 'fake': 'fake', 'carm': 'carm', 'earm': 'earm', 'side': 'side',
         'hole_cfg': 'hole_cfg', 'ud_split': 'ud_split', 'edges_same_layer': 'edges_same_layer', 'cc': 'corner_case', 'split_pairs': 'split_pairs', 'cols_bad': 'cols_bad'}
if __name__ == '__main__':
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 2000
    rng = random.Random(2026)
    ok = collections.Counter(); tot = collections.Counter(); ex = {}
    for want in [None, (4, 4), (4, 2), (3, 2), (7, 8), (8, 8), (2, 2), (4, 6), (3, 4), (3, 6), (5, 4), (5, 6), (6, 6)]:
        tag = 'any' if want is None else f'{want[0]}c{want[1]}e'
        for t in range(N):
            s = rand_state(rng, want); ix = geom.ix_of_state(cube.inverse(s))
            for k, v in reads(s).items():
                truth = int(F[TRUTH[k]][ix])
                tot[(k, tag)] += 1; good = (v == truth); ok[(k, tag)] += good
                if not good and (k, tag) not in ex: ex[(k, tag)] = (v, truth, int(ix))
    with open(os.path.join(HERE, 'out', 'checks_trace2.tsv'), 'w') as f:
        f.write('read\tsample\tcubes\tholds\n')
        for (k, tag), n in sorted(tot.items()):
            f.write(f'{k}\t{tag}\t{n}\t{ok[(k, tag)]}\n')
            if ok[(k, tag)] != n: print('FAIL', k, tag, ok[(k, tag)], n, ex.get((k, tag)))
    allk = sorted({k for k, _ in tot})
    for k in allk:
        print(f'{k:18s}', sum(ok[(kk, t)] for (kk, t) in tot if kk == k), '/', sum(tot[(kk, t)] for (kk, t) in tot if kk == k))
