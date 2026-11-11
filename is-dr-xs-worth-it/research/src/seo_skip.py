#!/usr/bin/env python3
"""How often a scramble has a slice-EO skip: exact, over every way the twelve edges can be placed and oriented.

A slice EO is "the four edges belonging to one slice (E, M or S) all oriented, or all misoriented, for one axis
(U/D, R/L or F/B)": 9 slice-and-axis pairs, each in two flavours, on normal and on inverse.

Whether a state has one depends only on (a) which kind of piece (E, M or S) sits at each of the 12 edge places
and (b) the 12 orientation bits for the F/B axis: 34,650 x 2,048 = 70,963,200 equally likely configurations.
  orientation for axis e of a piece of kind t sitting at a place of kind u, F/B bit b:   b ^ g_e(u) ^ g_e(t)
  with g_FB = 0, g_UD = 1 on M places / M pieces, g_RL = 1 on E places / E pieces
(the place and the piece each have a reference sticker per axis; they change between axes exactly there).
On inverse the roles of "kind of the place" and "kind of the piece" swap."""
import itertools, sys, collections
import numpy as np
import cube, fe, coords

KIND = ['E' if p[1] == 0 else 'M' if p[0] == 0 else 'S' for p in coords.EDGES]     # kind of each edge place
G = {'FB': {'E': 0, 'M': 0, 'S': 0}, 'UD': {'E': 0, 'M': 1, 'S': 0}, 'RL': {'E': 1, 'M': 0, 'S': 0}}

def check_rule():
    """The rule above against the sticker model, on random states: orientation for U/D and R/L computed by turning the
    cube so that axis becomes F/B."""
    import random
    random.seed(5)
    rot = {'UD': 'x', 'RL': 'y'}        # x carries the F face to U; y carries F to L: the rotated cube's F/B axis is the old U/D resp. R/L
    for _ in range(200):
        s = cube.do(cube.SOLVED, [random.choice(coords.NAMES) for _ in range(40)])
        b = coords.flips(s)
        piece_kind = []
        for i in range(12):
            cols = {fe.cax(s, j) for j in coords.EF[i]}
            piece_kind.append('E' if 1 not in cols else 'M' if 0 not in cols else 'S')
        for ax, r in rot.items():
            # conjugate: turn the whole cube (stickers and colours) so that axis `ax` is where F/B was
            R = cube.MOVES[r]; Rinv = cube.inverse(tuple(R))
            # state seen after rotating the cube by r: place R[i] holds the sticker that was at i, recoloured by R
            t = [0] * 54
            for i in range(54): t[R[i]] = R[s[i]]
            bt = coords.flips(tuple(t))
            for i in range(12):
                # place i of the original is place j of the rotated cube
                j = next(k for k in range(12) if set(coords.EF[k]) == {R[x] for x in coords.EF[i]})
                assert bt[j] == b[i] ^ G[ax][KIND[i]] ^ G[ax][piece_kind[i]], (ax, i)
    return True

def main():
    assert check_rule()
    bits = np.array([[(v >> i) & 1 for i in range(11)] + [bin(v).count('1') & 1] for v in range(2048)], dtype=np.uint8)   # 2048 x 12
    names = [(T, e, fl, side) for side in ('normal', 'inverse') for T in 'EMS' for e in ('UD', 'RL', 'FB') for fl in ('oriented', 'misoriented')]
    tot = 0
    count_each = np.zeros(len(names), dtype=np.int64)
    hist = {k: collections.Counter() for k in ('normal', 'both', 'normal oriented', 'both oriented')}
    slots = range(12)
    for E in itertools.combinations(slots, 4):
        rest = [i for i in slots if i not in E]
        for Mi in itertools.combinations(rest, 4):
            S = [i for i in rest if i not in Mi]
            kind_at = [None] * 12
            for i in E: kind_at[i] = 'E'
            for i in Mi: kind_at[i] = 'M'
            for i in S: kind_at[i] = 'S'
            ev = []
            for side in ('normal', 'inverse'):
                for T in 'EMS':
                    if side == 'normal': idx = [i for i in slots if kind_at[i] == T]        # places holding the T pieces
                    else: idx = [i for i in slots if KIND[i] == T]                          # the T places
                    for e in ('UD', 'RL', 'FB'):
                        g = np.array([G[e][KIND[i]] ^ G[e][kind_at[i]] for i in idx], dtype=np.uint8)
                        o = bits[:, idx] ^ g                                                 # 2048 x 4
                        sm = o.sum(axis=1)
                        ev.append(sm == 0); ev.append(sm == 4)
            ev = np.array(ev)                                                                # 36 x 2048
            count_each += ev.sum(axis=1); tot += 2048
            nn = ev[:18].sum(axis=0); nb = ev.sum(axis=0); no = ev[0:18:2].sum(axis=0); bo = ev[0::2].sum(axis=0)
            for k, arr in (('normal', nn), ('both', nb), ('normal oriented', no), ('both oriented', bo)):
                u, c = np.unique(arr, return_counts=True)
                for a, b in zip(u, c): hist[k][int(a)] += int(b)
    assert tot == 34650 * 2048
    out = open('/data/fmc/is-dr-xs-worth-it/research/out/seo_skip.txt', 'w')
    def P(*a):
        print(*a); print(*a, file=out)
    P('configurations', tot)
    P('each single slice EO (slice, axis, flavour, side): share of states')
    for nm, c in zip(names, count_each): P('  ', *nm, f'{c}/{tot} = {c / tot:.6f}')
    for k in hist:
        h = hist[k]; P(f'number of slice-EO skips, {k}:')
        for a in sorted(h): P(f'   {a}: {h[a]} = {100 * h[a] / tot:.4f}%')
        P(f'   at least one: {100 * (1 - h[0] / tot):.4f}%   mean {sum(a * c for a, c in h.items()) / tot:.4f}')
main()
