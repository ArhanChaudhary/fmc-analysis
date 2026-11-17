#!/usr/bin/env python3
"""Extra traceable features of the switched case, for every coset (F/B EO, DR on U/D).  Writes out/feat2.npz.
Each one is something a pair trace or a colour count gives; the normal-side reading of each is in trace.py."""
import os, sys
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, '..', 'src'))
import geom, features as fx
from geom import CT, ESET, N_CO, N_SL, N0, CORNERS, EDGES
from features import UD_EDGE, E_SLOT, M_POS, layer_nb, vert_nb, free_axis, bad, ax, arm_c, fb_c, per_co, per_sl

def build():
    G = {}
    z8 = lambda: np.zeros(N0, np.int8)
    # per U/D-layer edge place: holds a bad edge?  pairs / fake pairs on it
    pe = {}; fe = {}; hold = {}
    for e in UD_EDGE:
        h = per_sl(ESET[:, e]); hold[e] = h
        p = z8(); f = z8()
        for c in layer_nb(e):
            p += h & per_co(bad[:, c] & (ax[:, c] == free_axis(e)))
            f += h & per_co(bad[:, c] & (ax[:, c] != free_axis(e)))
        pe[e] = p; fe[e] = f
    # pairs out of AR (the edge in the M slice, the corner's U/D sticker on R/L) and in AR
    p_out = z8(); p_in = z8(); f_m = z8(); f_s = z8()
    for e in UD_EDGE:
        if e in M_POS: p_out += pe[e]; f_m += fe[e]
        else: p_in += pe[e]; f_s += fe[e]
    G['pairs_out'] = p_out; G['pairs_in'] = p_in
    G['fake_m'] = f_m; G['fake_s'] = f_s           # fake pairs on an M-slice edge / on an S-slice edge
    # pair pattern over the bad U/D-layer edges: how many have 2, 1, 0 pairs
    n2 = z8(); n1 = z8(); n0 = z8(); nf_only = z8(); n_naked = z8()
    for e in UD_EDGE:
        n2 += hold[e] & (pe[e] == 2); n1 += hold[e] & (pe[e] == 1); n0 += hold[e] & (pe[e] == 0)
        nf_only += hold[e] & (pe[e] == 0) & (fe[e] >= 1)
        n_naked += hold[e] & (pe[e] == 0) & (fe[e] == 0)
    G['e_bar'] = n2; G['e_one'] = n1; G['e_none'] = n0
    G['e_fakeonly'] = nf_only                       # bad edges with no pair but a fake pair
    G['e_naked'] = n_naked                          # bad edges with no bad corner pointing at or away next to them
    # edges with a pair and a fake pair (already 'pair_fake_same_edge'); edges with 1 pair and a good corner on the other side
    n_pg = z8()
    for e in UD_EDGE: n_pg += hold[e] & (pe[e] == 1) & (fe[e] == 0)
    G['e_pair_clean'] = n_pg
    # bad corners: in a pair, in a fake pair only, loose (next to no bad edge of their layer)
    in_pair = np.zeros((N0, 8), bool); in_fake = np.zeros((N0, 8), bool)
    for e in UD_EDGE:
        for c in layer_nb(e):
            in_pair[:, c] |= hold[e] & per_co(bad[:, c] & (ax[:, c] == free_axis(e)))
            in_fake[:, c] |= hold[e] & per_co(bad[:, c] & (ax[:, c] != free_axis(e)))
    badf = np.repeat(bad, N_SL, axis=0)
    loose = badf & ~in_pair & ~in_fake
    G['c_loose'] = loose.sum(1).astype(np.int8)
    armf = np.repeat(arm_c, N_SL, axis=0)
    G['c_loose_arm'] = (loose & armf).sum(1).astype(np.int8)       # loose corners out of AR
    G['c_unpaired_arm'] = (badf & ~in_pair & armf).sum(1).astype(np.int8)
    # layers: bad corners in U; bad edges in U; corners in the layer of an unpaired edge, etc.
    U_C = np.array([p[1] > 0 for p in CORNERS])
    cu = per_co((bad & U_C).sum(1)); nc = per_co(bad.sum(1))
    eu = per_sl(ESET[:, [e for e in UD_EDGE if EDGES[e][1] > 0]].sum(1)); ne = per_sl(ESET[:, UD_EDGE].sum(1))
    G['c_in_U'] = cu.astype(np.int8); G['e_in_U'] = eu.astype(np.int8)
    # corners sharing a layer with at least one bad edge
    with_e = np.where(eu > 0, cu, 0) + np.where(ne - eu > 0, nc - cu, 0)
    G['c_with_edge_layer'] = with_e.astype(np.int8)
    # holes (U/D edges in the E slice): which places
    hole = {e: per_sl(~ESET[:, e]) for e in E_SLOT}
    nh = sum(hole[e].astype(np.int8) for e in E_SLOT)
    G['holes'] = nh
    # two holes: 0 = on one R/L face, 1 = diagonal, 2 = on one F/B face (-1 otherwise)
    cfg = np.full(N0, -1, np.int8)
    for i, a in enumerate(E_SLOT):
        for b in E_SLOT[i + 1:]:
            both = hole[a] & hole[b] & (nh == 2)
            if EDGES[a][0] == EDGES[b][0]: v = 0
            elif EDGES[a][2] == EDGES[b][2]: v = 2
            else: v = 1
            cfg[both] = v
    G['hole_cfg'] = cfg
    # side pairs per kind: corner above/below a hole with its U/D sticker on F/B (the server's side pair) or on R/L
    s_fb = z8(); s_rl = z8(); h_full = z8()
    for e in E_SLOT:
        k = z8()
        for c in vert_nb(e):
            s_fb += hole[e] & per_co(fb_c[:, c]); s_rl += hole[e] & per_co(arm_c[:, c])
            k += hole[e] & per_co(fb_c[:, c])
        h_full += k == 2
    G['side_rl'] = s_rl; G['hole_bars'] = h_full   # holes with a side pair above and below
    # a top pair whose corner also side-pairs a hole ("pair over a hole")
    pos = z8()
    for e in UD_EDGE:
        for c in layer_nb(e):
            pr = hold[e] & per_co(bad[:, c] & (ax[:, c] == free_axis(e)))
            for s in E_SLOT:
                if c in vert_nb(s): pos += pr & hole[s] & per_co(fb_c[:, c])
    G['pair_over_hole'] = pos
    # columns: the two corners above and below an E-slice place; how many columns have both corners bad
    cols = np.zeros(N_CO, np.int8)
    for e in E_SLOT:
        v = vert_nb(e); cols += (bad[:, v[0]] & bad[:, v[1]])
    G['cols_bad'] = per_co(cols)
    return G

if __name__ == '__main__':
    G = build()
    np.savez_compressed(os.path.join(HERE, 'out', 'feat2.npz'), **G)
    F = np.load(os.path.join(HERE, '..', 'out', 'big', 'feat.npz'))
    assert (G['pairs_out'] + G['pairs_in'] == F['pairs']).all()
    assert (G['fake_m'] + G['fake_s'] == F['fake']).all()
    assert (2 * G['e_bar'] + G['e_one'] == F['pairs']).all()
    r = np.load(os.path.join(HERE, '..', 'out', 'big', 'rings.npz'))
    m = (F['drm_c'] == 4) & (F['drm_e'] == 4)
    assert (G['hole_cfg'][m] == r['slot'][m]).all()
    ix = geom.ix_of_moves('R'); print({k: int(v[ix]) for k, v in G.items()})
    print('wrote feat2.npz', len(G))
