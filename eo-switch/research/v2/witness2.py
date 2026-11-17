#!/usr/bin/env python3
"""Witness cases for the write-up: for each named condition the first case in index order, with a setup (the inverse
of an optimal DR) and the DR, both replayed on the sticker model; and one real attempt worked out in full on the
normal side.  Writes out/witness2.json."""
import os, sys, json, csv
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, '..', 'src')); sys.path.insert(0, HERE)
from lib import *
import cards as C
from cards import P, ARM, CC, CCS, SIDE, FAKE, EP, HC, UDS, ESL, CA, EA, CARDS, BASE, card_mask
import geom, trace2
from geom import cube
dd = d
def state(ix):
    sol = geom.path_to_dr(int(ix), F['d']); setup = cube.inv_seq(sol)
    s = cube.do(cube.SOLVED, ' '.join(setup))
    assert geom.ix_of_state(s) == int(ix) and geom.is_dr_ud(cube.do(s, ' '.join(sol))) and len(sol) == int(dd[ix])
    cc = int(F['corner_case'][ix])
    return dict(ix=int(ix), setup=' '.join(setup), dr=' '.join(sol), d=int(dd[ix]), pairs=int(P[ix]), fake=int(FAKE[ix]), side=int(SIDE[ix]), arm=f'{int(CA[ix])}{int(EA[ix])}',
                case=('4' + 'abcd'[cc] + '-' + str(int(F['case_suffix'][ix]))) if cc >= 0 else '', paired_edges=int(EP[ix]), holes=int(HC[ix]), hbar=int(F['hbar'][ix]))
def first(mask, pick=0):
    idx = np.flatnonzero(mask); assert idx.size, 'no case'
    return state(idx[min(pick, idx.size - 1)])
m44 = drm_mask(4, 4); G44 = {label: g for label, g, v in CARDS[(4, 4)]}
hb = F['hbar']
W = {}
W['0p_4mover'] = first(m44 & (P == 0) & (dd == 4))                                                  # pairs rule misses, card catches
W['1p_4d_4mover'] = first(G44['1 pair, ARM 21, 4d corners'] & (dd == 4))
W['1p_4b_side2_5mover'] = first(G44['1 pair, ARM 21, 4b corners, 0 or 2 side pairs'] & (dd == 5))
W['1p_4b_side1_8mover'] = first(G44['1 pair, ARM 21, 4b corners, exactly 1 side pair'] & (dd == 8))
W['bar_holes_bad_8mover'] = first(G44['2 pairs on one edge (a bar), holes not on one R/L face, 0 or 1 fake pairs'] & (F['hole_cfg'] == 2) & (dd == 8))
W['bar_fake2_5mover'] = first(G44['2 pairs on one edge (a bar), holes not on one R/L face, 2 fake pairs'] & (dd == 5))   # holes off, 2 fake pairs, DR in 5
W['bar_holes_good_5mover'] = first(G44['2 pairs on one edge (a bar), holes on one R/L face'] & (dd == 5))
W['card_miss_5mover'] = first(G44['1 pair, anything else'] & (dd == 5))                              # a 5-mover the card skips
W['card_miss_0p_5mover'] = first(G44['0 pairs, anything else'] & (dd == 5))
W['count3_5mover'] = first(m44 & (hb == 3) & (dd == 5))                                             # two bars says 3, DR in 5
W['count2_7mover'] = first(m44 & (hb == 2) & (dd == 7) & (P == 2))
W['count4_6mover'] = first(m44 & (hb == 4) & (dd == 6))
W['count3_1pair_6mover'] = first(m44 & (hb == 3) & (P == 1) & (dd == 6))
m42 = drm_mask(4, 2); G42 = {label: g for label, g, v in CARDS[(4, 2)]}
W['42_jzp_5mover'] = first(G42['0 pairs, JZP (ARM 00) with 4b corners'] & (dd == 5))
W['42_4b0_6mover'] = first(G42['1 pair, no side pair, 4b-0 corners'] & (dd == 6))
m78 = drm_mask(7, 8)
W['78_5p_arm20'] = first(m78 & (P == 5) & (ARM == 20))
W['78_4p_arm21_5mover'] = first(m78 & (P == 4) & (ARM == 21) & (dd == 5))
m88 = drm_mask(8, 8); G88 = {label: g for label, g, v in CARDS[(8, 8)]}
W['88_4p_arm42_5mover'] = first(G88['4 pairs, ARM 42'] & (dd == 5) & ~BASE[(8, 8)][0][3])
W['88_2p_arm42_5mover'] = first(G88['2 pairs, ARM 42'] & (dd == 5))
G4A = G44['1 pair, ARM 20, 21 or 22, 4a corners in two columns, 1+ side pairs']
W['1p_4a_cols_5mover'] = first(G4A & (ARM == 21) & (dd == 5))
W['1p_4a_cols_arm22_5mover'] = first(G4A & (ARM == 22) & (dd == 5))                                 # stacked 4a outside ARM 21
W['1p_4a_cols_arm20_5mover'] = first(G4A & (ARM == 20) & (dd == 5))
W['1p_4a_cols_noside_8mover'] = first(G44['1 pair, ARM 20, 21 or 22, 4a corners in two columns, no side pair'] & (dd == 8))
W['1p_4a_nocols'] = first(G44['1 pair, ARM 20, 21 or 22, 4a corners not in two columns'] & (ARM == 21) & (dd == 8))
W['54_pocket_4mover'] = first(drm_mask(5, 4) & card_mask((5, 4)) & (dd == 4))
W['66_pocket_4mover'] = first(drm_mask(6, 6) & card_mask((6, 6)) & (dd == 4))
W['46_pocket_4mover'] = first(drm_mask(4, 6) & card_mask((4, 6)) & (dd == 4) & (ARM != 0))
W['32_skip_6mover'] = first(drm_mask(3, 2) & (P == 0) & (FAKE == 0) & (F['split_pairs'] == 0) & (dd == 6))
W['22_0p_side_6mover'] = first(drm_mask(2, 2) & (P == 0) & (SIDE == 1) & np.isin(ARM, (0, 11)) & (dd == 6))
# ---------------------------------------------------------------- one real attempt, read on normal
COL = {'U': 'white', 'D': 'yellow', 'F': 'green', 'B': 'blue', 'R': 'red', 'L': 'orange'}
scr = open(os.path.join(HERE, '..', 'out', 'scrambles.txt')).read().split('\n')
def attempt(group, want_d, pick=0):
    k = 0
    for r in csv.DictReader(open(os.path.join(HERE, '..', 'out', 'big', 'att_examples.tsv')), delimiter='\t'):
        if not (r['eo_axis'] == 'FB' and r['dr_axis'] == 'UD' and r['side'] == '0' and r['length'] == '5' and r['drm_normal'] == '4c4e'): continue
        ix = int(r['ix_switched'])
        if not (group[ix] and dd[ix] in want_d): continue
        if k < pick: k += 1; continue
        S = scr[int(r['scr'])]; seq = S + ' ' + r['eo'] + ' ' + r['rzp']
        s = cube.do(cube.SOLVED, seq); si = cube.inverse(s)
        assert geom.ix_of_state(si) == ix
        rd = trace2.reads(s)
        for kk, t in trace2.TRUTH.items():
            if kk in rd: assert rd[kk] == int(F[t][ix]), kk
        sol = geom.path_to_dr(ix, F['d']); assert geom.is_dr_ud(cube.do(si, ' '.join(sol)))
        cs = trace2.corners(s); es = trace2.ud_edges_in_E(s); hs = trace2.E_edges_out(s)
        return dict(scramble=S, eo=r['eo'], rzp=r['rzp'], dr=' '.join(sol), d=len(sol), ix=ix, reads={k_: int(v) for k_, v in rd.items()},
                    edges=[f'{COL[a]}-{COL[b]}' for a, b in es],
                    corners=[f"{COL[ud]}-{'-'.join(sorted(COL[x] for x in (sides | {top}) - {ud}))} showing {COL[top]}" for top, sides, ud in cs],
                    out=['-'.join(sorted(COL[x] for x in h)) for h in hs], case=state(ix)['case'], arm=state(ix)['arm'])
    raise SystemExit('no attempt')
W['attempt_1p_4b_side2'] = attempt(G44['1 pair, ARM 21, 4b corners, 0 or 2 side pairs'], (5, 6))
W['attempt_bar_holes_bad'] = attempt(G44['2 pairs on one edge (a bar), holes not on one R/L face, 0 or 1 fake pairs'], (7, 8))
json.dump(W, open(os.path.join(HERE, 'out', 'witness2.json'), 'w'), indent=1)
for k, v in W.items(): print(k, {a: b for a, b in v.items() if a not in ('ix',)})
