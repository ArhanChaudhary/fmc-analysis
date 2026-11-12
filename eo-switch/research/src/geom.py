#!/usr/bin/env python3
"""Geometry of the state space, read off is-dr-xs-worth-it's sticker model (src/cube.py, coords.py), so that every
feature is defined by faces and stickers, not by an index string.

State: F/B EO solved, DR on U/D.  Coset index ix = co * 495 + sl, co = sum ct[i] 3^i (i < 7; ct[7] fixed by the
twist sum), ct[i] = which facelet of corner place i, counted clockwise (seen from outside) from its U/D facelet, holds
the corner's U/D sticker; sl = rank of the 4 places holding E-slice pieces (itertools.combinations order).
Axes: x = R(+)/L(-), y = U(+)/D(-), z = F(+)/B(-)."""
import os, sys, itertools
import numpy as np
XS = '/data/fmc/is-dr-xs-worth-it/research/src'
sys.path.insert(0, XS)
import cube, coords, fe  # noqa: E402

N_CO, N_SL = 2187, 495
N0 = N_CO * N_SL
CORNERS = coords.CORNERS          # place -> (x, y, z)
EDGES = coords.EDGES
FACE_OF_NORMAL = {(1, 0, 0): 'R', (-1, 0, 0): 'L', (0, 1, 0): 'U', (0, -1, 0): 'D', (0, 0, 1): 'F', (0, 0, -1): 'B'}

def pname(p):
    """Name of a place, e.g. UFR, UF, FR (U/D first, then F/B, then R/L for corners)."""
    x, y, z = p
    s = ''
    if y: s += 'U' if y > 0 else 'D'
    if z: s += 'F' if z > 0 else 'B'
    if x: s += 'R' if x > 0 else 'L'
    return s
C_NAME = [pname(p) for p in CORNERS]
E_NAME = [pname(p) for p in EDGES]

# face holding the U/D sticker of the corner at place i when its twist is t
UD_FACE = [[FACE_OF_NORMAL[cube.ST[coords.CF[i][t]][1]] for t in range(3)] for i in range(8)]
UD_AXIS = np.array([[{'U': 1, 'D': 1, 'R': 0, 'L': 0, 'F': 2, 'B': 2}[UD_FACE[i][t]] for t in range(3)] for i in range(8)])

def decode_co(co):
    t = [(co // 3 ** i) % 3 for i in range(7)]
    t.append((-sum(t)) % 3)
    return t
CT = np.array([decode_co(co) for co in range(N_CO)], dtype=np.int8)          # [co][place]
COMB = list(itertools.combinations(range(12), 4))
ESET = np.zeros((N_SL, 12), dtype=bool)                                       # [sl][edge place] holds an E piece
for k, c in enumerate(COMB): ESET[k, list(c)] = True

def ix_of_state(s):
    co, eo, sl = coords.coords(s)
    assert eo == 0, 'F/B EO not solved'
    return co * N_SL + sl
def ix_of_moves(seq):
    return ix_of_state(cube.do(cube.SOLVED, seq))
SOLVED_IX = ix_of_state(cube.SOLVED)

def is_dr_ud(s):
    co, eo, sl = coords.coords(s)
    return co == 0 and sl == SOLVED_IX % N_SL
def eo_fb_ok(s):
    return coords.coords(s)[1] == 0

# move tables on cosets (moves.bin of is-dr-xs-worth-it, rows of 18 moves U U2 U' D .. B')
NAMES = coords.NAMES
EOK = [m for m in range(18) if NAMES[m][0] not in 'FB' or NAMES[m].endswith('2')]
def load_moves():
    raw = np.fromfile('/data/fmc/is-dr-xs-worth-it/research/out/tables/moves.bin', dtype='<u2').reshape(-1, 18)
    co, sl = raw[:N_CO].astype(np.int64), raw[N_CO + 2048:].astype(np.int64)
    return co, sl
MCO, MSL = load_moves()
def move_ix(ix, m):
    """Coset index after move m (ix may be an array)."""
    return MCO[ix // N_SL, m] * N_SL + MSL[ix % N_SL, m]

def bfs(targets, moves):
    """Distance from a boolean target mask over the N0 cosets with the given move set (closed under inverses)."""
    d = np.full(N0, 255, dtype=np.uint8)
    d[targets] = 0
    front = np.flatnonzero(targets); k = 0
    while front.size:
        nxt = np.unique(np.concatenate([move_ix(front, m) for m in moves]))
        nxt = nxt[d[nxt] == 255]
        d[nxt] = k + 1; front = nxt; k += 1
    return d

def load_d():
    d = np.fromfile(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'out', 'big', 'd.u8'), dtype=np.uint8)
    assert d.size == N0
    return d

def path_to_dr(ix, d=None):
    """A shortest EO-kept move sequence (names) from coset ix to DR, by the table."""
    d = load_d() if d is None else d
    out = []
    while d[ix] > 0:
        for m in EOK:
            j = move_ix(ix, m)
            if d[j] == d[ix] - 1:
                out.append(NAMES[m]); ix = j; break
    return out

def setup_for(ix, d=None):
    """A move sequence from solved that reaches coset ix (inverse of a shortest path to DR)."""
    return cube.inv_seq(path_to_dr(ix, d))

if __name__ == '__main__':
    for i in range(8): print(i, C_NAME[i], UD_FACE[i])
    print([(i, n) for i, n in enumerate(E_NAME)])
    print('solved ix', SOLVED_IX)
