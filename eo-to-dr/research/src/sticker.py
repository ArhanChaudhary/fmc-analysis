#!/usr/bin/env python3
"""DR and EO read off the stickers, independently of the coordinates and tables of the Rust side.

Uses the sticker model of is-dr-xs-worth-it (`cube.py`, built from geometry).  Axes: 0 R/L (x), 1 U/D (y), 2 F/B (z),
the coordinate index of cube.ST positions.

  is_dr(s, X)   every sticker on a face of axis X has a colour of axis X, and the four edges of the middle layer
                of X have every sticker on a face of its own colour's axis (so the X-slice edges sit in their slice
                and are not flipped)
  is_eo(s, Y)   every edge is good for Y, by the usual rule with a reference axis A != Y: look at the edge's sticker
                of A's colours (or, if it has none, of Y's colours) and at the edge place's facelet on an A face (or,
                if it has none, on a Y face); good iff that sticker is on that facelet.  Both choices of A give the
                same answer (checked in __main__).
  replay(scramble, normal, inverse)   the state B S A with B = inverse(inverse-side moves), from solved."""
import os, sys, random
sys.path.insert(0, '/data/fmc/is-dr-xs-worth-it/research/src')
import cube

FACE_AXIS = {'R': 0, 'L': 0, 'U': 1, 'D': 1, 'F': 2, 'B': 2}
PLACE_AXIS = [FACE_AXIS[f] for f in cube.FACE_OF]
EDGES = []  # each edge place: its two sticker places
_by_pos = {}
for i, (p, n) in enumerate(cube.ST):
    _by_pos.setdefault(p, []).append(i)
for p, ids in _by_pos.items():
    if len(ids) == 2:
        EDGES.append((p, ids))
assert len(EDGES) == 12

def col_axis(s, i):
    return FACE_AXIS[cube.colour(s, i)]

def is_dr(s, X):
    for i in range(54):
        if PLACE_AXIS[i] == X and col_axis(s, i) != X:
            return False
    for p, ids in EDGES:
        if p[X] == 0:
            for i in ids:
                if col_axis(s, i) != PLACE_AXIS[i]:
                    return False
    return True

def edge_good(s, ids, Y, A):
    cols = [col_axis(s, i) for i in ids]
    ref_col = A if A in cols else Y
    k = cols.index(ref_col)                        # the sticker carrying the reference colour
    places = [PLACE_AXIS[i] for i in ids]
    ref_place = A if A in places else Y
    return places[k] == ref_place

def bad_edges(s, Y, A=None):
    if A is None:
        A = min(a for a in range(3) if a != Y)
    return sum(not edge_good(s, ids, Y, A) for p, ids in EDGES)

def is_eo(s, Y):
    return bad_edges(s, Y) == 0

def replay(scramble, normal='', inverse=''):
    s = cube.do(cube.SOLVED, cube.inv_seq(inverse) if inverse.strip() else [])
    s = cube.do(s, scramble)
    return cube.do(s, normal) if normal.strip() else s

if __name__ == '__main__':
    random.seed(3)
    names = [f + x for f in 'UDRLFB' for x in ('', '2', "'")]
    for Y in range(3):
        others = [a for a in range(3) if a != Y]
        for _ in range(300):
            seq = [random.choice(names) for _ in range(25)]
            s = cube.do(cube.SOLVED, seq)
            assert bad_edges(s, Y, others[0]) == bad_edges(s, Y, others[1])
            # turns that are not quarter turns of Y keep each edge's goodness; quarter turns of Y flip four edges
            for m in names:
                t = cube.apply(s, cube.MOVES[m])
                quarter = FACE_AXIS[m[0]] == Y and not m.endswith('2')
                if not quarter:
                    assert bad_edges(t, Y) == bad_edges(s, Y)
        assert all(is_eo(cube.SOLVED, Y) for Y in range(3)) and all(is_dr(cube.SOLVED, X) for X in range(3))
    assert is_dr(cube.do(cube.SOLVED, "U R2 D' F2"), 1) and not is_dr(cube.do(cube.SOLVED, "U R"), 1)
    assert is_dr(cube.do(cube.SOLVED, "R U2 L' F2"), 0) and is_dr(cube.do(cube.SOLVED, "F R2 B U2"), 2)
    assert bad_edges(cube.do(cube.SOLVED, 'F'), 2) == 4 and bad_edges(cube.do(cube.SOLVED, 'F'), 0) == 0
    # the superflip: every edge bad on every axis, corners solved
    sf = cube.do(cube.SOLVED, "U R2 F B R B2 R U2 L B2 R U' D' R2 F R' L B2 U2 F2")
    assert all(bad_edges(sf, Y) == 12 for Y in range(3))
    print('sticker DR/EO checks ok')
