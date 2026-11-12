#!/usr/bin/env python3
"""Every candidate feature of the notes' list F (kb/reread/eoswitch_notes.md), for each of the 1,082,565 cosets
(F/B EO, DR on U/D), defined by faces and stickers (geom.py).  `python3 features.py` builds out/big/feat.npz and runs
the unit tests on the notes' worked examples; `python3 features.py test` runs only the tests.

Index conventions: Louis's / Rodney's code numbers corners [ULF URF URB ULB DLF DRF DRB DLB] and edges [UF UR UB UL FL
FR BR BL DF DR DB DL]; their twist digit equals ours place by place (checked below on every coset: their string-based
ARM, pairs, fake pairs, side pairs and AR pairs equal the geometric definitions)."""
import os, sys
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import geom
from geom import CT, ESET, N_CO, N_SL, N0, CORNERS, EDGES, UD_AXIS, cube

OUT = os.path.join(HERE, '..', 'out')
# ---------------------------------------------------------------- per-place geometry
UD_EDGE = [i for i, p in enumerate(EDGES) if p[1] != 0]               # 8 places in the U/D layers
E_SLOT = [i for i, p in enumerate(EDGES) if p[1] == 0]                # 4 E-slice places
M_POS = [i for i in UD_EDGE if EDGES[i][0] == 0]                       # UF UB DF DB
def layer_nb(e):
    """The two corners next to U/D-layer edge place e in its layer."""
    x, y, z = EDGES[e]
    return [i for i, c in enumerate(CORNERS) if c[1] == y and (c[0] == x if x else c[2] == z)]
def vert_nb(e):
    x, y, z = EDGES[e]
    return [i for i, c in enumerate(CORNERS) if c[0] == x and c[2] == z]
def free_axis(e):
    """Axis (0 = x, 2 = z) along which U/D-layer edge place e has coordinate 0: a corner next to it pairs with it when
    its U/D sticker is on the face of that axis (the face the edge does not touch)."""
    return 0 if EDGES[e][0] == 0 else 2

ct = CT                                     # [co][8]
bad = ct != 0                               # [co][8]
ax = np.take_along_axis(np.broadcast_to(UD_AXIS, (N_CO, 8, 3)), ct[:, :, None].astype(np.int64), 2)[:, :, 0]   # axis of U/D sticker
arm_c = bad & (ax == 0)                     # U/D sticker on R or L
fb_c = bad & (ax == 2)                      # U/D sticker on F or B
ORBIT1 = np.array([p[0] * p[1] * p[2] == -1 for p in CORNERS])         # {ULF URB DRF DLB}
U_C = np.array([p[1] > 0 for p in CORNERS]); R_C = np.array([p[0] > 0 for p in CORNERS])
F_C = np.array([p[2] > 0 for p in CORNERS])

def outer(a_co, b_sl):
    """Combine a per-co array and a per-sl array into a per-coset array (ix = co * 495 + sl)."""
    return (a_co[:, None] + b_sl[None, :]).reshape(-1) if a_co.dtype != bool else (a_co[:, None] & b_sl[None, :]).reshape(-1)
def per_co(a): return np.repeat(a, N_SL)
def per_sl(b): return np.tile(b, N_CO)

def corner_case(mask):
    """Rodney's corner case of a 4-corner set (per co): 'a', 'b', 'c', 'd' (0..3), or -1 if not 4 corners."""
    n = mask.sum(1)
    a = (mask & ORBIT1).sum(1); b = n - a
    split = np.minimum.reduce([a, b, 4 - a, 4 - b])
    face_min = np.minimum.reduce([(mask & U_C).sum(1), (mask & ~U_C).sum(1), (mask & R_C).sum(1), (mask & ~R_C).sum(1)])
    case = np.where(split == 0, 3, np.where(split == 1, 2, np.where(face_min == 1, 1, 0)))
    return np.where(n == 4, case, -1)

def build():
    F = {}
    d = geom.load_d()
    F['d'] = d
    nc = bad.sum(1); ca = arm_c.sum(1)
    n_out_sl = ESET[:, UD_EDGE].sum(1)                     # E pieces in the U/D layers
    F['drm_c'] = per_co(nc); F['drm_e'] = per_sl(2 * n_out_sl)
    F['carm'] = per_co(ca); F['carm_fold'] = per_co(np.minimum(ca, nc - ca))
    F['earm'] = per_sl(ESET[:, M_POS].sum(1))
    # corner orbit case and suffix
    cc = corner_case(bad)
    a1 = (bad & ORBIT1).sum(1); split = np.minimum.reduce([a1, nc - a1, 4 - a1, 4 - (nc - a1)])
    F['orbit_split'] = per_co(split)
    F['corner_case'] = per_co(cc)                          # 0 a, 1 b, 2 c, 3 d (4 bad corners only)
    suffix = np.where(cc == 0, ca, np.minimum(ca, 4 - ca))
    F['case_suffix'] = per_co(np.where(nc == 4, suffix, -1))
    n1 = (ct == 1).sum(1); n2 = (ct == 2).sum(1)
    F['tw1'] = per_co(n1); F['tw2'] = per_co(n2)
    F['twist_major'] = per_co(np.maximum(n1, n2))         # 6 for 6+0, 3 for 3+3, 7 for 7+1, 4 for 4+4
    # pairs, fake pairs, per edge
    n_p = np.zeros(N0, np.int8); n_f = np.zeros(N0, np.int8); edges1 = np.zeros(N0, np.int8); bars = np.zeros(N0, np.int8)
    paired_c = np.zeros((N0, 8), bool); pf_same = np.zeros(N0, np.int8)
    for e in UD_EDGE:
        hold = per_sl(ESET[:, e])
        pe = np.zeros(N0, np.int8); fe_ = np.zeros(N0, np.int8)
        for c in layer_nb(e):
            pair = hold & per_co(bad[:, c] & (ax[:, c] == free_axis(e)))
            fake = hold & per_co(bad[:, c] & (ax[:, c] != free_axis(e)))
            pe += pair; fe_ += fake
            paired_c[:, c] |= pair
        n_p += pe; n_f += fe_
        edges1 += pe >= 1; bars += pe == 2; pf_same += (pe >= 1) & (fe_ >= 1)
    F['pairs'] = n_p; F['fake'] = n_f; F['edges_paired'] = edges1; F['bars'] = bars
    F['pair_fake_same_edge'] = pf_same
    F['paired_corners'] = paired_c.sum(1).astype(np.int8)
    nc_full = F['drm_c']; ud_bad = per_sl(n_out_sl)
    F['unpaired_corners'] = (nc_full - F['paired_corners']).astype(np.int8)
    F['unpaired_edges'] = (ud_bad - edges1).astype(np.int8)
    F['pairs_minus_udbad'] = (n_p - ud_bad).astype(np.int8)
    # side pairs
    n_s = np.zeros(N0, np.int8)
    for e in E_SLOT:
        hold_ud = per_sl(~ESET[:, e])
        for c in vert_nb(e):
            n_s += hold_ud & per_co(fb_c[:, c])
    F['side'] = n_s
    F['pairs_plus_half_side_x2'] = (2 * n_p + n_s).astype(np.int8)   # 2 x (pairs + side/2)
    # split pairs (wen): bad edge in a U/D layer and a misoriented corner of that layer not next to it, same AR state
    sp = np.zeros(N0, np.int8)
    for e in UD_EDGE:
        hold = per_sl(ESET[:, e]); e_arm = e in M_POS
        for c in range(8):
            if CORNERS[c][1] == EDGES[e][1] and c not in layer_nb(e):
                sp += hold & per_co(bad[:, c] & (arm_c[:, c] == e_arm))
    F['split_pairs'] = sp
    # AR pairs / AR bars (Rodney's n_ar; doc 304's "AR bar")
    n_ar = np.zeros(N0, np.int8)
    for e in UD_EDGE:
        if e in M_POS: continue
        ok = per_sl(~ESET[:, e]); both = np.ones(N0, bool)
        for c in layer_nb(e): both &= per_co(~bad[:, c] | arm_c[:, c])
        n_ar += ok & both
    for e in E_SLOT:
        ok = per_sl(~ESET[:, e]); both = np.ones(N0, bool)
        for c in vert_nb(e): both &= per_co(bad[:, c])
        n_ar += ok & both
    F['ar_bars'] = n_ar
    # AR / JZP
    jzp = (F['carm'] == 0) & (F['earm'] == 0) & (nc_full % 2 == 0)
    F['jzp'] = jzp.astype(np.int8)
    F['fake_jzp'] = ((F['carm'] == 0) & (F['earm'] == 0) & (nc_full % 2 == 1)).astype(np.int8)
    F['anti_ar'] = ((F['carm'] == nc_full) & (F['earm'] == ud_bad) & (nc_full > 0)).astype(np.int8)
    eok = geom.EOK
    UDM = [m for m in eok if geom.NAMES[m][0] in 'UD']
    F['moves_to_ar'] = geom.bfs(jzp, eok)
    F['udmoves_to_ar'] = np.minimum(geom.bfs(jzp, UDM), 99).astype(np.uint8)
    # layer layouts
    u_bad = (bad & U_C).sum(1); r_bad = (bad & R_C).sum(1); f_bad = (bad & F_C).sum(1)
    F['ud_split'] = per_co(np.maximum(u_bad, nc - u_bad))           # 4 for 4-0, 3 for 3-1, 2 for 2-2 (4 corners)
    F['lr_split'] = per_co(np.maximum(r_bad, nc - r_bad))
    F['fb_split'] = per_co(np.maximum(f_bad, nc - f_bad))
    e_u = ESET[:, [e for e in UD_EDGE if EDGES[e][1] > 0]].sum(1); e_d = n_out_sl - e_u
    corners_one_layer = (u_bad == nc) | (u_bad == 0)
    F['corners_one_layer'] = per_co(corners_one_layer & (nc > 0))
    # bad corners all on one U/D layer and the bad U/D-layer edges all on the other
    cu = per_co((u_bad == nc) & (nc > 0)); cd = per_co((u_bad == 0) & (nc > 0))
    F['corners_edges_opposite'] = ((cu & per_sl((e_u == 0) & (e_d > 0))) | (cd & per_sl((e_d == 0) & (e_u > 0)))).astype(np.int8)
    # wen: everything on U in one AR class and everything on D in the other (bad pieces of U all in-AR / all out, D the reverse)
    F['edges_same_slice'] = per_sl(np.array([(n_out_sl[s] >= 2) and (all(EDGES[e][0] == 0 for e in UD_EDGE if ESET[s, e]) or all(EDGES[e][2] == 0 for e in UD_EDGE if ESET[s, e])) for s in range(N_SL)]))
    F['edges_same_layer'] = per_sl((n_out_sl >= 2) & ((e_u == 0) | (e_d == 0)))
    F['edges_same_side'] = per_sl(np.array([(n_out_sl[s] >= 2) and any(all(EDGES[e][k] == v for e in UD_EDGE if ESET[s, e]) for k in (0, 2) for v in (-1, 1)) for s in range(N_SL)]))
    # corner-only optimal (moves to orient corners, EO kept), and Rodney's 4c4e lower bound without the half-turn term
    cod = np.full(N_CO, 255, np.uint8); cod[0] = 0; front = [0]; k = 0
    while front:
        nxt = sorted({int(geom.MCO[c, m]) for c in front for m in eok} - {c for c in range(N_CO) if cod[c] != 255})
        for c in nxt: cod[c] = k + 1
        front = nxt; k += 1
    F['corner_dist'] = per_co(cod)
    F['lb_simple'] = (F['corner_dist'] + np.maximum(0, 4 - n_p) * (nc_full > 0)).astype(np.int8)
    # distance to trigger families with setup turns {U, D, F2, B2, R2, L2}
    SET = [m for m in eok if geom.NAMES[m][0] in 'UD' or geom.NAMES[m].endswith('2')]
    fams = trigger_families()
    for name, seqs in fams.items():
        tgt = np.zeros(N0, bool)
        for s in seqs: tgt[geom.ix_of_moves(cube.inv_seq(s))] = True
        F['fam_' + name] = np.minimum(geom.bfs(tgt, SET), 99).astype(np.uint8)
        F['famud_' + name] = np.minimum(geom.bfs(tgt, UDM), 99).astype(np.uint8)
    # 4a one U/D turn from 4d; 4b + JZP
    cc_full = F['corner_case']
    one = np.zeros(N0, bool)
    for m in UDM: one |= cc_full[geom.move_ix(np.arange(N0), m)] == 3
    F['a_one_from_d'] = ((cc_full == 0) & one).astype(np.int8)
    F['b_jzp'] = ((cc_full == 1) & jzp).astype(np.int8)
    # case of the out-of-AR corners (trangium, 8c8e)
    F['arm_corner_case'] = per_co(corner_case(arm_c))
    # 8c8e "correct": an R/L quarter-turn pair gives JZP
    rl = np.zeros(N0, bool)
    for m1 in [m for m in eok if geom.NAMES[m] in ('R', "R'")]:
        for m2 in [m for m in eok if geom.NAMES[m] in ('L', "L'")]:
            rl |= jzp[geom.move_ix(geom.move_ix(np.arange(N0), m1), m2)]
    F['rl_to_jzp'] = rl.astype(np.int8)
    return F

def trigger_families():
    q = ['U', "U'", 'D', "D'"]; h = ['U2', 'D2', 'F2', 'B2']; R = ['R', "R'"]; L = ['L', "L'"]
    fam = {}
    fam['4c4e'] = [[r] for r in R + L]
    fam['4c2e'] = [[a, x, b] for a in R for x in h for b in R] + [[a, x, b] for a in L for x in h for b in L]
    fam['4c6e'] = [[a, x, b] for a in R for x in h for b in L] + [[a, x, b] for a in L for x in h for b in R]
    fam['3c2e'] = [[a, x, b] for a in R for x in q for b in R] + [[a, x, b] for a in L for x in q for b in L]
    fam['7c8e'] = [[a, x, b] for a in R for x in q for b in L] + [[a, x, b] for a in L for x in q for b in R]
    fam['8c8e'] = [[a, b] for a in R for b in L]
    return fam

# ---------------------------------------------------------------- Rodney's / Louis's string code, for the check
RK_C = ['UFL', 'UFR', 'UBR', 'UBL', 'DFL', 'DFR', 'DBR', 'DBL']
RK_E = ['UF', 'UR', 'UB', 'UL', 'FL', 'FR', 'BR', 'BL', 'DF', 'DR', 'DB', 'DL']
RK_CI = [geom.C_NAME.index(n) for n in RK_C]; RK_EI = [geom.E_NAME.index(n) for n in RK_E]
corner_arm_orientations = "21211212"; edge_arm_orientations = "1.1.....1.1."
corner_neighbours = [((0, 1), (2, 1)), ((1, 2), (2, 1)), ((2, 3), (2, 1)), ((3, 0), (2, 1)),
                     ((0, 4), (1, 2)), ((1, 5), (2, 1)), ((2, 6), (1, 2)), ((3, 7), (2, 1)),
                     ((4, 5), (1, 2)), ((5, 6), (1, 2)), ((6, 7), (1, 2)), ((7, 4), (1, 2))]
def rk_strings(ix):
    co, sl = ix // N_SL, ix % N_SL
    return ''.join(str(CT[co][i]) for i in RK_CI), ''.join('1' if ESET[sl][i] else '0' for i in RK_EI)
def rk_features(co, eo):
    """Rodney's stats.py get_drm, get_arm, get_pair_counts (copied logic)."""
    drm = (sum(o != '0' for o in co), 8 - 2 * sum(int(eo[i]) for i in range(4, 8)))
    arm = (sum(a == b for a, b in zip(co, corner_arm_orientations)), sum(a == b for a, b in zip(eo, edge_arm_orientations)))
    n_pairs = n_pseudo = n_side = n_ar = 0
    for e in (0, 1, 2, 3, 8, 9, 10, 11):
        ids, tg = corner_neighbours[e]
        if eo[e] == '1':
            for i, t in zip(ids, tg):
                if int(co[i]) == t: n_pairs += 1
                elif int(co[i]) != 0: n_pseudo += 1
        elif e not in (0, 2, 8, 10):
            ar = sum(1 for i in ids if co[i] == '0' or co[i] == corner_arm_orientations[i])
            if ar == 2: n_ar += 1
    for e in (4, 5, 6, 7):
        if eo[e] == '0':
            ids, tg = corner_neighbours[e]; ar = 0
            for i, t in zip(ids, tg):
                if int(co[i]) == t: n_side += 1; ar += 1
                elif co[i] == corner_arm_orientations[i]: ar += 1
            if ar == 2: n_ar += 1
    return drm, arm, (n_pairs, n_pseudo, n_side, n_ar)

def check_against_strings(F, n=None):
    """Rodney's string code against the geometric features, on every coset (or a sample of n)."""
    rng = np.random.default_rng(1)
    ixs = np.arange(N0) if n is None else rng.choice(N0, n, replace=False)
    bad = 0
    for ix in ixs:
        co, eo = rk_strings(int(ix))
        drm, arm, pr = rk_features(co, eo)
        mine = ((F['drm_c'][ix], F['drm_e'][ix]), (F['carm'][ix], F['earm'][ix]), (F['pairs'][ix], F['fake'][ix], F['side'][ix], F['ar_bars'][ix]))
        if (drm, arm, pr) != tuple(tuple(int(v) for v in t) for t in mine):
            bad += 1
            if bad < 5: print('MISMATCH', ix, co, eo, drm, arm, pr, mine)
    return len(ixs), bad

# ---------------------------------------------------------------- unit tests on the notes' examples
CASE = 'abcd'
def describe(F, ix):
    c, e = int(F['drm_c'][ix]), int(F['drm_e'][ix])
    s = f"{c}c{e}e AR-{int(F['carm'][ix])}c{int(F['earm'][ix])}e pairs {int(F['pairs'][ix])} fake {int(F['fake'][ix])} side {int(F['side'][ix])} d {int(F['d'][ix])}"
    if c == 4: s += f" case 4{CASE[int(F['corner_case'][ix])]}-{int(F['case_suffix'][ix])}"
    return s

def state_after(seq): return geom.ix_of_moves(seq)
def state_solved_by(seq): return geom.ix_of_moves(cube.inv_seq(seq))
REMAP = str.maketrans({'R': 'U', 'L': 'D', 'U': 'F', 'D': 'B', 'F': 'R', 'B': 'L'})   # U/D EO + R/L DR -> F/B EO + U/D DR

TESTS = [
    # (where in the notes, how the state is made, sequence, expected)
    ('A3/F: R from solved', 'after', 'R', dict(drm_c=4, drm_e=4, carm=0, earm=0, pairs=4, bars=2, d=1)),
    ('A3/F: R U from solved (D7118-D7119)', 'after', 'R U', dict(drm_c=4, drm_e=4, carm=2, earm=1)),
    ('E16/F: U\' F2 B2 R2 U2 R is AR 02, 0 pairs, 6 moves', 'solved_by', "U' F2 B2 R2 U2 R", dict(drm_c=4, drm_e=4, carm=0, earm=2, pairs=0, d=6)),
    ('E3: D F2 B2 L2 U2 R, 4e4c AR-0C2E in 6', 'solved_by', 'D F2 B2 L2 U2 R', dict(drm_c=4, drm_e=4, carm=0, earm=2, d=6)),
    ('E4: AR-0C0E, 4 optimal (R F2 U2 R)', 'solved_by', 'R F2 U2 R', dict(drm_c=4, drm_e=4, carm=0, earm=0, d=4)),
    ('E4: AR-2C1E, 5 optimal (U\' R2 D B2 R)', 'solved_by', "U' R2 D B2 R", dict(drm_c=4, drm_e=4, carm=2, earm=1, d=5)),
    ('E4: AR-3C2E/1C0E, 5 optimal (D R\' U2 F2 R)', 'solved_by', "D R' U2 F2 R", dict(drm_c=4, drm_e=4, carm_fold=1, d=5)),
    ('E4: AR-4C2E, 6 optimal (U\' R2 D R2 D L)', 'solved_by', "U' R2 D R2 D L", dict(drm_c=4, drm_e=4, carm=4, earm=2, d=6)),
    ('E17: 4 pairs, both edges on front (R2 U D\' F2 L)', 'solved_by', "R2 U D' F2 L", dict(drm_c=4, drm_e=4, pairs=4)),
    ('E17: AR-2c1e, 3 pairs on one face (R\' U2 F2 L2 U R)', 'solved_by', "R' U2 F2 L2 U R", dict(drm_c=4, drm_e=4, carm=2, earm=1, pairs=3)),
    ('E17: same case (R U2 B2 R2 D\' R)', 'solved_by', "R U2 B2 R2 D' R", dict(drm_c=4, drm_e=4, carm=2, earm=1, pairs=3)),
    ('E18: 7c8e AR-2c2e, 6 moves (U B2 D2 L D R)', 'solved_by', 'U B2 D2 L D R', dict(drm_c=7, drm_e=8, carm=2, earm=2, d=6)),
    ('E18: (D L U R2 U\' R)', 'solved_by', "D L U R2 U' R", dict(drm_c=7, drm_e=8, carm=2, earm=2, d=6)),
    ('E18: (D\' L\' D L2 D\' R)', 'solved_by', "D' L' D L2 D' R", dict(drm_c=7, drm_e=8, carm=2, earm=2, d=6)),
    ('A5 (Louis orbit_stats): 4a is R-like', 'solved_by', 'R', dict(corner_case=0, case_suffix=0)),
    ('A5: 4b is U\' R-like', 'solved_by', "U' R", dict(corner_case=1, case_suffix=2)),
    ('A5: 4c is U\' R2 U R-like', 'solved_by', "U' R2 U R", dict(corner_case=2, case_suffix=1)),
    ('A5: 4d is U F2 R-like', 'solved_by', 'U F2 R', dict(corner_case=3, case_suffix=2)),
    ('B2 (D14333): D F2 B2 R, 0 pairs, no fake pairs, 4 moves', 'solved_by', 'D F2 B2 R', dict(drm_c=4, drm_e=4, pairs=0, fake=0, d=4)),
    ('B2 (T8107/T8123): F2 B2 R type, 0 pairs, no fake pairs, corner case 4a-0', 'solved_by', 'F2 B2 R', dict(drm_c=4, drm_e=4, pairs=0, fake=0, d=3, corner_case=0, case_suffix=0)),
    ('A2: R U2 R is 4c2e', 'solved_by', 'R U2 R', dict(drm_c=4, drm_e=2, d=3)),
    ('A2: R U R is 3c2e', 'solved_by', 'R U R', dict(drm_c=3, drm_e=2, d=3)),
    ('B5: R U L is 7c8e', 'solved_by', 'R U L', dict(drm_c=7, drm_e=8, d=3)),
    ('B5: R L is 8c8e', 'solved_by', 'R L', dict(drm_c=8, drm_e=8, d=2)),
    ('B5: R U2 L is 4c6e', 'solved_by', 'R U2 L', dict(drm_c=4, drm_e=6, d=3)),
    ('B5 (T3767): 8c8e, R L gives JZP', 'solved_by', 'R L', dict(rl_to_jzp=1, jzp=1)),
]

def run_tests(F):
    ok = 0; lines = []
    for where, how, seq, exp in TESTS:
        ix = state_after(seq) if how == 'after' else state_solved_by(seq)
        got = {k: int(F[k][ix]) for k in exp}
        good = got == exp
        ok += good
        lines.append(f"{'ok  ' if good else 'FAIL'}\t{where}\t{how} {seq}\t{describe(F, ix)}\texpected {exp}")
    # E1: setup R U D2 L U' R U2, then L' makes a pair and stays 4c4e, then D' F2 R2 U' D L reaches DR
    a = state_after("R U D2 L U' R U2"); b = state_after("R U D2 L U' R U2 L'")
    s = cube.do(cube.SOLVED, "R U D2 L U' R U2 L' D' F2 R2 U' D L")
    good = (int(F['drm_c'][a]), int(F['drm_e'][a]), int(F['carm'][a]), int(F['earm'][a])) == (4, 4, 2, 1) and int(F['drm_c'][b]) == 4 and int(F['drm_e'][b]) == 4 and int(F['pairs'][b]) > int(F['pairs'][a]) and geom.is_dr_ud(s)
    ok += good
    lines.append(f"{'ok  ' if good else 'FAIL'}\tE1 (T4262): setup R U D2 L U' R U2 is 4C4E AR-2C1E; L' makes a pair, stays 4C4E; D' F2 R2 U' D L reaches DR\t\t{describe(F, a)} -> after L': {describe(F, b)}")
    # E14: WRITEUP example, U/D EO + R/L DR, written in our frame by the relabelling R->U L->D U->F D->B F->R B->L
    scr = "L2 D2 U' F2 L2 U' L2 B2 U' R2 B2 L2 R' D L F' D F2 D' F2".translate(REMAP)
    eo1 = "R' D2 L' D".translate(REMAP); eo2 = "R' D2 L' D'".translate(REMAP)
    i1 = geom.ix_of_state(cube.do(cube.SOLVED, scr + ' ' + eo1)); i2 = geom.ix_of_state(cube.do(cube.SOLVED, scr + ' ' + eo2))
    sol1 = 'D2 R2 B2 F2 L F'.translate(REMAP); sol2 = 'R2 B2 F2 L F'.translate(REMAP)
    good = (int(F['drm_c'][i1]), int(F['drm_e'][i1]), int(F['d'][i1]), int(F['d'][i2])) == (4, 4, 6, 5) and geom.is_dr_ud(cube.do(cube.SOLVED, scr + ' ' + eo1 + ' ' + sol1)) and geom.is_dr_ud(cube.do(cube.SOLVED, scr + ' ' + eo2 + ' ' + sol2)) and geom.move_ix(i1, geom.NAMES.index('B2')) == i2
    ok += good
    lines.append(f"{'ok  ' if good else 'FAIL'}\tE14 (WRITEUP): 4c4e, 6 to DR; with the last EO turn inverted 5; the inverted EO = state times B2 (the EO's last turn D is B in our frame)\t\t{describe(F, i1)} / {describe(F, i2)}")
    # E15 (T10704), informational: F B' U R2 U leaves EO on R/L only (the inverse keeps that EO axis); the only DR axis
    # where both sides are 4c2e is F/B: seen with R/L -> F/B, F/B -> U/D (conjugation by x y)
    seq = "F B' U R2 U"; rot = cube.do(cube.SOLVED, 'x y'); roti = cube.do(cube.SOLVED, ' '.join(cube.inv_seq('x y')))
    ixs = [geom.ix_of_state(cube.compose(cube.compose(roti, cube.do(cube.SOLVED, q)), rot)) for q in (seq, ' '.join(cube.inv_seq(seq)))]
    lines.append(f"info\tE15 (T10704): F B' U R2 U, claimed 4c2e with 2 pairs on normal and 0 pairs on inverse\t\tnormal {describe(F, ixs[0])} / inverse {describe(F, ixs[1])}")
    return ok, len(TESTS) + 2, lines

if __name__ == '__main__':
    F = build()
    ok, tot, lines = run_tests(F)
    print('\n'.join(lines)); print(f'unit tests: {ok}/{tot} pass')
    n, bad = check_against_strings(F, None if 'full' in sys.argv else 200000)
    print(f"Rodney's string code (stats.py logic, index map {RK_C} / {RK_E}) vs geometric features: {n - bad}/{n} cosets agree")
    with open(os.path.join(OUT, 'checks_features.txt'), 'w') as f:
        f.write('\n'.join(lines) + f'\nunit tests: {ok}/{tot} pass\n')
        f.write(f"Rodney's string code vs geometric features (DRM, ARM, pairs, fake pairs, side pairs, AR pairs): {n - bad}/{n} cosets agree\n")
    if 'test' not in sys.argv:
        np.savez_compressed(os.path.join(OUT, 'big', 'feat.npz'), **F)
        print('wrote out/big/feat.npz with', len(F), 'features')
