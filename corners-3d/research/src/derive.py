#!/usr/bin/env python3
"""Everything the analysis needs that `c3d tables` did not write, as .npy files in research/out/big.

    parity.npy     0 even / 1 odd placement (one bit per state)
    inverse.npy    the rank of the inverse state
    pid.npy        the kinds at the seven places as one number (base 6): "the types", 25,515 values
    cls.npy        the types up to half turns: the smallest pid reachable with R2, U2, F2 (1,284 values)
    colour.npy     N x 3: for each axis, the places holding a corner with DBL's colour of that axis, as 7 bits
    dperm, qperm   moves / quarter turns to an HTR placement when twists are ignored (5,040 placements)
    ddr.npy        N x 3: moves to HTR with DR turns of that axis only (99 off the DR states)
    qdr.npy        N x 3: the same in quarter turns (the HTR subset number)
    staged.npy     N x 3: optimal corner orientation on that axis first, then the best DR-only finish
    sym.npy        6 x N: the six symmetries that keep DBL (rank of the image)

usage: derive.py
"""
import os
import numpy as np

import c3

N = c3.N
B = c3.BIG


def save(name, a):
    np.save(os.path.join(B, name + ".npy"), a)


def index(P, O):
    """Rank of states given as arrays (n x 7) of placements and twists: the same rule as cube.rs."""
    rank = np.zeros(len(P), dtype=np.int64)
    for i in range(7):
        smaller = np.zeros(len(P), dtype=np.int64)
        for j in range(i + 1, 7):
            smaller += P[:, j] < P[:, i]
        rank = rank * (7 - i) + smaller
    tw = np.zeros(len(P), dtype=np.int64)
    for i in range(6):
        tw = tw * 3 + O[:, i]
    return rank * 729 + tw


def parity(P):
    par = np.zeros(len(P), dtype=np.uint8)
    for i in range(7):
        for j in range(i + 1, 7):
            par ^= (P[:, i] > P[:, j]).astype(np.uint8)
    return par


def distance(mv, sources, start, moves, cost=lambda m: 1, n=N):
    """Fewest (weighted) turns to the nearest source; `start[i]` is the cost already on source i."""
    dist = np.full(n, 99, dtype=np.int16)
    for s, c in sorted(zip(sources.tolist(), start.tolist()), key=lambda t: t[1]):
        dist[s] = c
    # level by level (costs are 0 or 1): numpy sweeps
    level = 0
    while True:
        frontier = np.where(dist == level)[0]
        if len(frontier) == 0:
            if level > dist[dist < 99].max():
                break
            level += 1
            continue
        # close the level under zero-cost turns
        zero = [m for m in moves if cost(m) == 0]
        grew = True
        while grew and zero:
            grew = False
            for m in zero:
                t = mv[m][frontier]
                new = t[dist[t] > level]
                if len(new):
                    dist[new] = level
                    frontier = np.concatenate([frontier, np.unique(new)])
                    grew = True
        for m in moves:
            if cost(m) == 1:
                t = mv[m][frontier]
                dist[t] = np.minimum(dist[t], level + 1)
        level += 1
    return dist


def main():
    mv = c3.moves()
    K = c3.kinds()
    P = c3.perm()
    O = c3.ori()
    rows = np.arange(N)

    par = parity(P)
    save("parity", par)

    Pinv = np.zeros_like(P)
    Oinv = np.zeros_like(O)
    for p in range(7):
        Pinv[rows, P[:, p]] = p
        Oinv[rows, P[:, p]] = (3 - O[:, p]) % 3
    inv = index(Pinv, Oinv)
    assert (inv[inv] == rows).all()
    save("inverse", inv.astype(np.uint32))

    pid = np.zeros(N, dtype=np.int64)
    for p in range(7):
        pid = pid * 6 + K[:, p]
    save("pid", pid.astype(np.int32))

    # the types up to half turns
    lab = pid.copy()
    changed = True
    while changed:
        changed = False
        for m in (1, 4, 7):
            new = np.minimum(lab, lab[mv[m]])
            if (new != lab).any():
                changed = True
                lab = new
    save("cls", lab.astype(np.int32))

    # colour pictures: which places hold a piece whose home is on the - side of the axis (DBL's side)
    col = np.zeros((N, 3), dtype=np.uint8)
    for a in range(3):
        minus = c3.XYZ[:, a] < 0
        for p in range(7):
            col[:, a] |= (minus[P[:, p]].astype(np.uint8) << p)
    save("colour", col)

    # placement-only puzzle
    pm = np.stack([mv[m][np.arange(5040) * 729] // 729 for m in range(9)])
    for m in range(9):
        assert (mv[m] // 729 == pm[m][rows // 729]).all()
    dh = c3.u8("d_htr")
    htr = np.where(dh == 0)[0]
    hp = np.unique(htr // 729)
    zero = np.zeros(len(hp), dtype=np.int16)
    dperm = distance(pm, hp, zero, range(9), n=5040)
    qperm = distance(pm, hp, zero, range(9), cost=lambda m: int(m % 3 != 1), n=5040)
    save("dperm", dperm[rows // 729].astype(np.int8))
    save("qperm", qperm[rows // 729].astype(np.int8))

    # DR-only tables, per axis: quarter turns of that axis' face, half turns of the other two
    dco = [c3.u8("d_co_" + a) for a in "xyz"]
    ddr = np.zeros((N, 3), dtype=np.int8)
    qdr = np.zeros((N, 3), dtype=np.int8)
    staged = np.zeros((N, 3), dtype=np.int8)
    z = np.zeros(len(htr), dtype=np.int16)
    for a in range(3):
        drm = [3 * a, 3 * a + 1, 3 * a + 2] + [3 * b + 1 for b in range(3) if b != a]
        d = distance(mv, htr, z, drm)
        qq = distance(mv, htr, z, drm, cost=lambda m: int(m % 3 != 1))
        assert ((d < 99) == (dco[a] == 0)).all()
        ddr[:, a] = d
        qdr[:, a] = qq
        # optimal orientation first: walk down d_co, keeping the best DR-only finish
        c = np.where(dco[a] == 0, d, 99).astype(np.int16)
        for j in range(1, int(dco[a].max()) + 1):
            S = np.where(dco[a] == j)[0]
            best = np.full(len(S), 99, dtype=np.int16)
            for m in range(9):
                t = mv[m][S]
                best = np.where(dco[a][t] == j - 1, np.minimum(best, c[t] + 1), best)
            c[S] = best
        staged[:, a] = c
    save("ddr", ddr)
    save("qdr", qdr)
    save("staged", staged)

    # the six symmetries that keep DBL: permute the axes (x, y, z); an odd permutation is a mirror
    sym = np.zeros((6, N), dtype=np.uint32)
    sig = sigma(P, O)
    perms = [(0, 1, 2), (1, 2, 0), (2, 0, 1), (0, 2, 1), (2, 1, 0), (1, 0, 2)]
    for k, ax in enumerate(perms):
        # place p at xyz goes to the place with coordinates xyz[ax]
        to = [int(np.where((c3.XYZ == c3.XYZ[p][list(ax)]).all(1))[0][0]) for p in range(7)]
        P2 = np.zeros_like(P)
        to_arr = np.array(to)
        for p in range(7):
            P2[:, to[p]] = to_arr[P[:, p]]
        # the sticker facing new axis f at the new place faced old axis ax[f]; its home axis is renamed too
        axinv = np.array([ax.index(i) for i in range(3)])
        sig2 = np.zeros_like(sig)
        for p in range(7):
            for f in range(3):
                sig2[:, to[p], f] = axinv[sig[:, p, ax[f]]]
        sym[k] = index(P2, twist_from_sigma(sig2))
        # a symmetry carries each turn to a turn: for every turn m there is a turn m2 with g(s m) = g(s) m2
        for m in range(9):
            assert any((sym[k][mv[m]] == mv[m2][sym[k]]).all() for m2 in range(9)), (k, m)
    assert (dh[sym] == dh[None, :]).all(), "a symmetry must keep the distance to HTR"
    save("sym", sym)
    print("derived tables written to", B)


def clockwise(p):
    """Axes around place p clockwise from U/D (cube.rs: clockwise)."""
    return [1, 2, 0] if c3.TETRAD[p] else [1, 0, 2]


def sigma(P, O):
    """N x 7 x 3: for the corner at each place, the home axis of the sticker facing axis 0, 1, 2.

    A corner in its own tetrad carries an even permutation of the axes (the identity or a 3-cycle, that is a
    shift a -> a + c mod 3); a corner in the other tetrad carries a transposition (a -> c - a mod 3).  The
    constant c follows from where the U/D sticker faces."""
    sig = np.zeros((len(P), 7, 3), dtype=np.int8)
    for p in range(7):
        f = np.array(clockwise(p))[O[:, p]]            # the axis the U/D sticker faces
        same = c3.TETRAD[p] == c3.TETRAD[P[:, p]]
        for a in range(3):
            sig[:, p, a] = np.where(same, (a + 1 - f) % 3, (f + 1 - a) % 3)
    return sig


def twist_from_sigma(sig):
    """The twist of each corner from its sticker permutation: where the U/D sticker faces, clockwise from U/D."""
    n = len(sig)
    O = np.zeros((n, 7), dtype=np.uint8)
    for p in range(7):
        cw = clockwise(p)
        f = (sig[:, p, :] == 1).argmax(1)       # the axis facing which the home-U/D sticker sits
        O[:, p] = np.array([cw.index(a) for a in range(3)])[f]
    return O


if __name__ == "__main__":
    main()
