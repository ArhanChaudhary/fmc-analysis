#!/usr/bin/env python3
"""The two-ring model of a switched case, and the counts that ignore U and D turns.

A layer (U or D) is a ring of 8 places read clockwise from outside the cube (U from above, D from below):
    U: UB UBR UR UFR UF UFL UL UBL        D: DB DBL DL DFL DF DFR DR DBR
written here as 4 edge places e[0..3] and 4 corner places c[0..3], corner k between edge k and edge k+1.
An edge place is *bad* when it holds an E-slice piece.  A bad corner *points* at the one of its two neighbouring edge
places it would pair with (the one on the side face its U/D sticker is not on): clockwise (1, '>') or
counter-clockwise (2, '<'); 0 ('o') is a good corner.  A *row* is corner-edge-corner of one layer on one side face.
The four E-slice places FR FL BL BR are *holes* when they hold a U/D-layer piece.

What the turns do (all checked below on every case, separately on the 2,187 twist states and the 495 edge sets):
  * U, D: rotate one ring; nothing else changes.
  * R2, L2, F2, B2: exchange the U row and the D row of that face, keeping the clockwise order, and exchange the two
    E-slice places of that face.
  * R, L quarter turns: the four corners of the face move one step round the face; a good corner arrives pointing at
    the face's edge place of its new layer, a corner that pointed at the face's edge place arrives good, a corner
    that pointed away keeps pointing away.  The four edges of the face move one step round it (layer, slot, layer,
    slot), each staying an E-slice piece or a U/D piece.

Counts (exact, every one of the 1,082,565 cases; U and D turns are free in all of them):
  sigma      fewest side turns (R, R', R2, L, L', L2, F2, B2) to DR
  prof       the (quarter turns, half turns) of the side-turn-optimal solutions: Q[q][h] = fewest moves (HTM, U/D
             turns counted) of a solution with exactly q quarter-turn moves and h half-turn moves on the side faces
  hbar       4c4e only: fewest half turns before a single R/L quarter turn finishes ("half turns to two bars")
  swaps      4c4e only: fewest row exchanges to a bar in each ring, on the rings alone (780 ring pairs)
  slot       4c4e only: 0 if the two holes share an R/L face, 1 if they are diagonal, 2 if they share an F/B face

`python3 rings.py` builds out/big/rings.npz and writes out/checks_rings.txt."""
import os, sys, itertools, collections
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import geom
from geom import N_CO, N_SL, N0, NAMES, EOK, ESET, CT, UD_FACE, C_NAME, E_NAME, move_ix
OUT = os.path.join(HERE, '..', 'out')

# ---------------------------------------------------------------------------------------------- places of the rings
def _nm(a):
    for perm in itertools.permutations(a):
        s = ''.join(perm)
        if s in C_NAME: return C_NAME.index(s)
        if s in E_NAME: return E_NAME.index(s)
    raise KeyError(a)
U_E = [_nm(x) for x in ('UB', 'UR', 'UF', 'UL')]; U_C = [_nm(x) for x in ('UBR', 'UFR', 'UFL', 'UBL')]
D_E = [_nm(x) for x in ('DB', 'DL', 'DF', 'DR')]; D_C = [_nm(x) for x in ('DBL', 'DFL', 'DFR', 'DBR')]
SLOT = [_nm(x) for x in ('FR', 'FL', 'BL', 'BR')]; SLOT_NAME = ['FR', 'FL', 'BL', 'BR']
U_FACE = ['B', 'R', 'F', 'L']; D_FACE = ['B', 'L', 'F', 'R']        # side face of edge place k of each ring
# per side face: index of its edge place in the U ring, in the D ring, and its two slots (indices in SLOT)
FACE = {'R': (1, 3, (0, 3)), 'L': (3, 1, (1, 2)), 'F': (2, 2, (0, 1)), 'B': (0, 0, (2, 3))}
SYM = {0: 'o', 1: '>', 2: '<'}

def _hook(c, t, prv, nxt):
    """0 good; 1 points clockwise (at the next edge place); 2 points counter-clockwise (at the previous one)."""
    if t == 0: return 0
    sf = UD_FACE[c][t]; assert sf in (prv, nxt)
    return 1 if sf == prv else 2
UH = np.array([[_hook(c, CT[co][c], U_FACE[k], U_FACE[(k + 1) % 4]) for k, c in enumerate(U_C)] for co in range(N_CO)], dtype=np.int8)
DH = np.array([[_hook(c, CT[co][c], D_FACE[k], D_FACE[(k + 1) % 4]) for k, c in enumerate(D_C)] for co in range(N_CO)], dtype=np.int8)
UE = ESET[:, U_E].astype(np.int8); DE = ESET[:, D_E].astype(np.int8)          # [sl][4]: bad edge places
HOLE = (~ESET[:, SLOT]).astype(np.int8)                                       # [sl][4]: FR FL BL BR hold a U/D piece

def rings_of(ix):
    """((U edges, U corners), (D edges, D corners), holes) of a case, as tuples."""
    co, sl = divmod(int(ix), N_SL)
    return (tuple(int(x) for x in UE[sl]), tuple(int(x) for x in UH[co])), (tuple(int(x) for x in DE[sl]), tuple(int(x) for x in DH[co])), tuple(int(x) for x in HOLE[sl])
def rot(r, k):
    e, h = r; return (e[k:] + e[:k], h[k:] + h[:k])
def canon(r): return min(rot(r, k) for k in range(4))
def swap_rows(U, D, p, q):
    """Exchange the row of U at edge place p (corner p-1, edge p, corner p) with the row of D at edge place q."""
    (ue, uh), (de, dh) = U, D
    ue, uh, de, dh = list(ue), list(uh), list(de), list(dh)
    ue[p], de[q] = de[q], ue[p]
    uh[(p - 1) % 4], dh[(q - 1) % 4] = dh[(q - 1) % 4], uh[(p - 1) % 4]
    uh[p], dh[q] = dh[q], uh[p]
    return (tuple(ue), tuple(uh)), (tuple(de), tuple(dh))
def has_bar(r):
    e, h = r
    return any(e[k] and h[(k - 1) % 4] == 1 and h[k] == 2 for k in range(4))
def mirror(r):
    """The ring seen in a mirror: order reversed, clockwise and counter-clockwise exchanged."""
    e, h = r
    return canon((tuple(e[(-k) % 4] for k in range(4)), tuple({0: 0, 1: 2, 2: 1}[h[(-k - 1) % 4]] for k in range(4))))
def sym_key(k):
    """A ring pair up to exchanging the layers and mirroring."""
    U, D = k
    return min([(U, D), (D, U), (mirror(U), mirror(D)), (mirror(D), mirror(U))])
def ring_str(r):
    """Clockwise, starting at a corner: corner, edge, corner, edge, ...  ('>E<-o-o-': a bar)."""
    e, h = r
    return ''.join(SYM[h[(k - 1) % 4]] + ('E' if e[k] else '-') for k in range(4))
def nice(r):
    """The rotation of a ring that reads best: starts at the corner before a bad edge, with the bad edges not split
    over the end of the string where that can be avoided, the edge with the most pairs first."""
    e, h = r
    def score(k):
        rr = rot(r, k); ee, hh = rr
        return (-(ee[0]), ee[3], -((hh[3] == 1) + (hh[0] == 2)) if ee[0] else 0, ring_str(rr))
    return ring_str(rot(r, min(range(4), key=score)))

def quarter(U, D, H, face, cw):
    """The rings and holes after a quarter turn of side face R or L (cw: clockwise seen from that face)."""
    p, q, (sf, sb) = FACE[face]
    (ue, uh), (de, dh) = U, D
    ue, uh, de, dh, H = list(ue), list(uh), list(de), list(dh), list(H)
    # the face's 4 corners in the order a clockwise turn (seen from the face) carries them, and the hooks 'at the face'
    # U row: corners p-1 (before the face's edge: it points at it when clockwise, 1) and p (points at it when 2)
    cyc = [('U', p), ('U', (p - 1) % 4), ('D', q), ('D', (q - 1) % 4)]      # U after -> U before -> D after -> D before
    at = {('U', p): 2, ('U', (p - 1) % 4): 1, ('D', q): 2, ('D', (q - 1) % 4): 1}
    get = lambda pos: (uh if pos[0] == 'U' else dh)[pos[1]]
    def put(pos, v): (uh if pos[0] == 'U' else dh)[pos[1]] = v
    old = {pos: get(pos) for pos in cyc}
    order = cyc if cw else cyc[::-1]
    for i, src in enumerate(order):
        dst = order[(i + 1) % 4]; v = old[src]
        away = 3 - at[src]
        new = at[dst] if v == 0 else 0 if v == at[src] else 3 - at[dst]
        assert v != away or new == 3 - at[dst]
        put(dst, new)
    # edges: U edge -> slot under U's 'before' corner -> D edge -> slot under U's 'after' corner -> U edge (clockwise)
    # slot under U corner p-1 is above D corner q; slot under U corner p is above D corner q-1
    s_before, s_after = _slot_under(face)
    ecyc = [('U', p), ('S', s_before), ('D', q), ('S', s_after)]
    def eget(pos): return ue[pos[1]] if pos[0] == 'U' else de[pos[1]] if pos[0] == 'D' else 1 - H[pos[1]]   # 1 = E piece
    def eput(pos, v):
        if pos[0] == 'U': ue[pos[1]] = v
        elif pos[0] == 'D': de[pos[1]] = v
        else: H[pos[1]] = 1 - v
    eold = {pos: eget(pos) for pos in ecyc}
    eorder = ecyc if cw else ecyc[::-1]
    for i, src in enumerate(eorder): eput(eorder[(i + 1) % 4], eold[src])
    return (tuple(ue), tuple(uh)), (tuple(de), tuple(dh)), tuple(H)
def _slot_under(face):
    """Slots (indices in SLOT) under the U corner before and after the face's U edge place, clockwise from above."""
    p = FACE[face][0]
    before = U_FACE[(p - 1) % 4]; after = U_FACE[(p + 1) % 4]       # the other face of corner p-1, of corner p
    idx = lambda a, b: next(i for i, n in enumerate(SLOT_NAME) if set(n) == {a, b})
    return idx(face, before), idx(face, after)

# ------------------------------------------------------------------------------------------------- the turn checks
def check_turns():
    """Every turn against the ring rules, on all 2,187 twist states x all 495 edge sets (corner and edge parts are
    independent, so each part is checked on its own table; a sample of full cases is checked through rings_of)."""
    mv = {n: NAMES.index(n) for n in NAMES}; res = collections.OrderedDict()
    co_of = lambda co: ((tuple(int(x) for x in UH[co])), (tuple(int(x) for x in DH[co])))
    sl_of = lambda sl: (tuple(int(x) for x in UE[sl]), tuple(int(x) for x in DE[sl]), tuple(int(x) for x in HOLE[sl]))
    def full(co, sl): (uh, dh), (ue, de, H) = co_of(co), sl_of(sl); return (ue, uh), (de, dh), H
    def split(U, D, H): return (U[1], D[1]), (U[0], D[0], H)
    blank_e = (0, 0, 0, 0); blank_h = (0, 0, 0, 0)
    ok = tot = 0
    for name, layer in (('U', 0), ("U'", 0), ('U2', 0), ('D', 1), ("D'", 1), ('D2', 1)):
        for co in range(N_CO):
            a, b = co_of(co), co_of(int(geom.MCO[co, mv[name]]))
            tot += 1; ok += (canon((blank_e, a[layer])) == canon((blank_e, b[layer])) and a[1 - layer] == b[1 - layer])
        for sl in range(N_SL):
            a, b = sl_of(sl), sl_of(int(geom.MSL[sl, mv[name]]))
            tot += 1; ok += (canon((a[layer], blank_h)) == canon((b[layer], blank_h)) and a[1 - layer] == b[1 - layer] and a[2] == b[2])
    res['U and D turns rotate one ring and change nothing else (twist states + edge sets, 6 turns)'] = (ok, tot)
    # a U or D turn rotates edges and corners of its ring by the same step: checked on full cases
    rng = np.random.default_rng(5); ok = tot = 0
    for ix in rng.choice(N0, 20000, replace=False):
        U, D, H = rings_of(ix)
        for name, layer in (('U', 0), ("U'", 0), ('U2', 0), ('D', 1), ("D'", 1), ('D2', 1)):
            U2, D2, H2 = rings_of(move_ix(int(ix), mv[name]))
            tot += 1; ok += ((canon(U2), D2) == (canon(U), D) if layer == 0 else (U2, canon(D2)) == (U, canon(D))) and H2 == H
    res['the same on 20,000 random full cases (edges and corners of the ring turn together)'] = (ok, tot)
    ok = tot = 0
    for f, (p, q, (a, b)) in FACE.items():
        m = mv[f + '2']
        for co in range(N_CO):
            uh, dh = co_of(co); U2, D2 = swap_rows((blank_e, uh), (blank_e, dh), p, q)
            tot += 1; ok += co_of(int(geom.MCO[co, m])) == (U2[1], D2[1])
        for sl in range(N_SL):
            ue, de, H = sl_of(sl); U2, D2 = swap_rows((ue, blank_h), (de, blank_h), p, q); Hs = list(H); Hs[a], Hs[b] = Hs[b], Hs[a]
            tot += 1; ok += sl_of(int(geom.MSL[sl, m])) == (U2[0], D2[0], tuple(Hs))
    res['R2 L2 F2 B2 exchange the two rows of the face and its two E-slice places (twist states + edge sets, 4 turns)'] = (ok, tot)
    ok = tot = 0
    for f in 'RL':
        for name, cw in ((f, True), (f + "'", False)):
            m = mv[name]
            for co in range(N_CO):
                uh, dh = co_of(co); U2, D2, _ = quarter((blank_e, uh), (blank_e, dh), (0, 0, 0, 0), f, cw)
                tot += 1; ok += co_of(int(geom.MCO[co, m])) == (U2[1], D2[1])
            for sl in range(N_SL):
                ue, de, H = sl_of(sl); U2, D2, H2 = quarter((ue, blank_h), (de, blank_h), H, f, cw)
                tot += 1; ok += sl_of(int(geom.MSL[sl, m])) == (U2[0], D2[0], H2)
    res["R R' L L' follow the quarter-turn rule (twist states + edge sets, 4 turns)"] = (ok, tot)
    return res

# ------------------------------------------------------------------------------------------------ counts on cases
UDM = [m for m in range(18) if NAMES[m][0] in 'UD']
HTM_ = [m for m in range(18) if NAMES[m].endswith('2') and NAMES[m][0] not in 'UD']
QTM = [m for m in range(18) if NAMES[m][0] in 'RL' and not NAMES[m].endswith('2')]
def ud_closure(mask):
    out = mask.copy(); idx = np.flatnonzero(mask)
    us = [idx] + [move_ix(idx, NAMES.index(x)) for x in ('U', 'U2', "U'")]
    for a in us:
        out[a] = True
        for x in ('D', 'D2', "D'"): out[move_ix(a, NAMES.index(x))] = True
    return out
def image(mask, moves):
    idx = np.flatnonzero(mask); out = np.zeros(N0, bool)
    for m in moves: out[move_ix(idx, m)] = True
    return out
def reach_sets(qmax=5, hmax=6):
    """R[q][h]: cases with a solution of exactly q quarter-turn moves and h half-turn moves on the side faces (in any
    order, any U/D turns between).  A solution with the fewest side turns never has two side turns that merge."""
    R = np.zeros((qmax + 1, hmax + 1, N0), bool)
    s0 = np.zeros(N0, bool); s0[geom.SOLVED_IX] = True
    for q in range(qmax + 1):
        for h in range(hmax + 1):
            m = s0.copy() if q == 0 and h == 0 else np.zeros(N0, bool)
            if q: m |= image(R[q - 1, h], QTM)
            if h: m |= image(R[q, h - 1], HTM_)
            R[q, h] = ud_closure(m)
    return R
def profile_moves(qmax=4, hmax=6):
    """Q[q][h][case]: fewest moves (U/D turns counted) of a solution with exactly q quarter-turn moves and h half-turn
    moves on the side faces, no two of which merge (99 if none).  Side turns that would merge (same face with nothing
    or only the opposite face between) are not allowed, so R R is never counted for R2."""
    INF = 99; ALL = np.arange(N0); mv = {n: NAMES.index(n) for n in NAMES}
    G = []; um = [None] + [move_ix(ALL, mv[x]) for x in ('U', 'U2', "U'")]
    for a in range(4):
        for b in range(4):
            if a == 0 and b == 0: continue
            j = ALL if a == 0 else um[a]
            if b: j = move_ix(j, mv[('D', 'D2', "D'")[b - 1]])
            G.append(((a > 0) + (b > 0), j))
    SETS = [frozenset(), frozenset('R'), frozenset('L'), frozenset('RL'), frozenset('F'), frozenset('B'), frozenset('FB')]
    OPP = {'R': 'L', 'L': 'R', 'F': 'B', 'B': 'F'}
    def nb(b, face):
        if face in SETS[b]: return None
        return SETS.index(frozenset({face} | (SETS[b] & {OPP[face]})))
    QT = [(n[0], move_ix(ALL, mv[n])) for n in ('R', "R'", 'L', "L'")]
    HT = [(n[0], move_ix(ALL, mv[n])) for n in ('R2', 'L2', 'F2', 'B2')]
    T = np.full((qmax + 1, hmax + 1, 7, N0), INF, np.uint8)
    for q in range(qmax + 1):
        for h in range(hmax + 1):
            cur = T[q, h]
            if q == 0 and h == 0: cur[0, geom.SOLVED_IX] = 0
            for src, moves in (((q - 1, h), QT), ((q, h - 1), HT)):
                if src[0] < 0 or src[1] < 0: continue
                prev = T[src]
                for b in range(7):
                    if not (prev[b] < INF).any(): continue
                    for face, j in moves:
                        k = nb(b, face)
                        if k is None: continue
                        cand = prev[b][j]; cand = np.where(cand < INF, cand + 1, INF).astype(np.uint8)
                        np.minimum(cur[k], cand, out=cur[k])
            anyb = cur.min(axis=0) if (q or h) else cur[0].copy()
            for cost, j in G:
                cand = anyb[j]; cand = np.where(cand < INF, cand + cost, INF).astype(np.uint8)
                np.minimum(cur[0], cand, out=cur[0])
    return T.min(axis=2)

def ring_swaps():
    """Row exchanges to a bar in each ring, by breadth-first search over the ring pairs of the 4c4e cases (rings up
    to rotation): {ring pair: swaps}."""
    goal_ring = canon(((1, 0, 0, 0), (2, 0, 0, 1)))
    assert has_bar(goal_ring)
    dist = {(goal_ring, goal_ring): 0}; front = [(goal_ring, goal_ring)]; n = 0
    while front:
        n += 1; nxt = []
        for U, D in front:
            for p in range(4):
                for q in range(4):
                    U2, D2 = swap_rows(U, D, p, q); k = (canon(U2), canon(D2))
                    if k not in dist: dist[k] = n; nxt.append(k)
        front = nxt
    return dist
def slot_type(H):
    idx = frozenset(i for i in range(4) if H[i]); assert len(idx) == 2
    return 0 if idx in (frozenset((0, 3)), frozenset((1, 2))) else 2 if idx in (frozenset((0, 1)), frozenset((2, 3))) else 1

def build():
    lines = []
    for k, (ok, tot) in check_turns().items():
        lines.append(f'{ok}\t{tot}\t{k}'); assert ok == tot, k
    F = np.load(os.path.join(OUT, 'big', 'feat.npz')); d = F['d']
    c4 = (F['drm_c'] == 4) & (F['drm_e'] == 4)
    R = reach_sets()
    assert R.any(axis=(0, 1)).all()
    sigma = np.full(N0, 99, np.int8); qsig = np.full(N0, 99, np.int8)
    for q in range(R.shape[0]):
        for h in range(R.shape[1]):
            m = R[q, h] & ((q + h < sigma) | ((q + h == sigma) & (q < qsig)))
            sigma[m] = q + h; qsig[m] = q
    lines.append(f"{int(((sigma <= 2) & (d <= 6)).sum())}\t{int((sigma <= 2).sum())}\tcases with at most 2 side turns that have a DR in 6 or fewer")
    assert (d[sigma <= 2] <= 6).all()
    lines.append('side turns 0..5: ' + ' '.join(str(int(x)) for x in np.bincount(sigma)))
    Q = profile_moves()
    dq = Q.reshape(-1, N0).min(axis=0)
    lines.append(f"{int((dq == d).sum())}\t{N0}\tfewest moves over the (quarter, half) profiles with at most 4 quarter and 6 half turns equals the distance to DR (the rest are at 7 or more: {np.bincount(d[dq != d]).tolist()})")
    assert (d[dq != d] >= 7).all()
    # the side-turn-optimal profiles from the reach sets agree with the merge-free search
    agree = all((R[q, h] & (sigma == q + h) == (Q[q, h] < 99) & (sigma == q + h)).all() for q in range(5) for h in range(7))
    lines.append(f"{int(agree)}\t1\ton side-turn-optimal profiles, plain reachability equals the merge-free search (no optimal solution merges side turns)")
    assert agree
    # 4c4e: half turns before one quarter turn; rings
    hbar = np.full(N0, -1, np.int8)
    for h in range(R.shape[1] - 1, -1, -1): hbar[R[1, h] & c4] = h
    assert (hbar[c4] >= 0).all() and not R[0].any(axis=0)[c4].any()
    dist = ring_swaps()
    swaps = np.full(N0, -1, np.int8); slot = np.full(N0, -1, np.int8); cls = np.full(N0, -1, np.int32)
    keys = sorted(dist); kid = {k: i for i, k in enumerate(keys)}
    for ix in np.flatnonzero(c4):
        U, D, H = rings_of(ix); k = (canon(U), canon(D))
        swaps[ix] = dist[k]; slot[ix] = slot_type(H); cls[ix] = kid[k]
    used = set(int(x) for x in cls[c4])
    lines.append(f"{len(used)}\t{len(keys)}\tring pairs reached by row exchanges from two bars that occur among the 4c4e cases")
    assert len(used) == len(keys) == 780
    okm = int((np.maximum(swaps[c4], slot[c4]) == hbar[c4]).sum())
    lines.append(f"{okm}\t{int(c4.sum())}\t4c4e cases where half turns to two bars = max(ring swaps, slot type)")
    assert okm == c4.sum()
    lines.append('ring pairs by swaps 0..5: ' + ' '.join(str(v) for _, v in sorted(collections.Counter(dist.values()).items())))
    open(os.path.join(OUT, 'checks_rings.txt'), 'w').write('\n'.join(lines) + '\n')
    print('\n'.join(lines))
    np.savez_compressed(os.path.join(OUT, 'big', 'rings.npz'), sigma=sigma, qsig=qsig, hbar=hbar, swaps=swaps, slot=slot, cls=cls,
                        Q=Q, R=np.packbits(R.reshape(-1, N0), axis=1), Rshape=np.array(R.shape))
    import pickle
    pickle.dump({'keys': keys, 'dist': dist}, open(os.path.join(OUT, 'big', 'ring_classes.pkl'), 'wb'))

def load():
    z = np.load(os.path.join(OUT, 'big', 'rings.npz'))
    return z

if __name__ == '__main__':
    build()
