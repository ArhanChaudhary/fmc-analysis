#!/usr/bin/env python3
"""Corner / edge pieces of the sticker cube of cube.py: place numbering, facelet order, and the conversion between a
sticker state and (cp, ct, ep, ef), the form the Rust crate `instools` works in.

  corner places   the 8 corner cubies sorted by coordinates; facelets: the U/D one first, then clockwise seen from outside
  edge places     the 12 edge cubies sorted by coordinates; facelets: the U/D one first if there is one, else the F/B one
  cp[i], ct[i]    the corner piece now at place i (named by its home place) and its twist: the index, in the facelet
                  order of place i, of the facelet holding the piece's reference (U/D) sticker
  ep[i], ef[i]    the same for edges (0 or 1)"""
import cube
from cube import ST

def nax(i): return max(range(3), key=lambda k: abs(ST[i][1][k]))          # axis of the face a facelet is on
CUBIES = {}
for _i, (_p, _n) in enumerate(ST): CUBIES.setdefault(_p, []).append(_i)
CORNERS = sorted(p for p in CUBIES if len(CUBIES[p]) == 3)
EDGES = sorted(p for p in CUBIES if len(CUBIES[p]) == 2)

def det(a, b, c):
    return (a[0] * (b[1] * c[2] - b[2] * c[1]) - a[1] * (b[0] * c[2] - b[2] * c[0]) + a[2] * (b[0] * c[1] - b[1] * c[0]))
def corner_facelets(p):
    pl = CUBIES[p]; ud = next(i for i in pl if nax(i) == 1); a, b = [i for i in pl if i != ud]
    if det(ST[ud][1], ST[a][1], ST[b][1]) > 0: a, b = b, a           # det < 0 is clockwise
    return [ud, a, b]
def edge_facelets(p):
    pl = CUBIES[p]
    pri = next((i for i in pl if nax(i) == 1), None)
    if pri is None: pri = next(i for i in pl if nax(i) == 2)
    return [pri, next(i for i in pl if i != pri)]
CF = [corner_facelets(p) for p in CORNERS]; EF = [edge_facelets(p) for p in EDGES]
def name_of(p): return ''.join(ch for ch, (a, sg) in (('U', (1, 1)), ('D', (1, -1)), ('F', (2, 1)), ('B', (2, -1)), ('R', (0, 1)), ('L', (0, -1))) if p[a] == sg)
CNAMES = [name_of(p) for p in CORNERS]; ENAMES = [name_of(p) for p in EDGES]
NAMES = [f + s for f in 'UDRLFB' for s in ('', '2', "'")]          # move numbering: 3 * face + (quarter turns - 1)

def corner_at(pl): return next(i for i in range(8) if set(CF[i]) == set(pl))
def edge_at(pl): return next(i for i in range(12) if set(EF[i]) == set(pl))
def cubie(s):
    """(cp, ct, ep, ef) of a sticker state."""
    cp, ct, ep, ef = [], [], [], []
    for i in range(8):
        home = [s[x] for x in CF[i]]; p = corner_at(home); cp.append(p); ct.append(home.index(CF[p][0]))
    for i in range(12):
        home = [s[x] for x in EF[i]]; p = edge_at(home); ep.append(p); ef.append(home.index(EF[p][0]))
    return cp, ct, ep, ef
def make(cp, ct, ep, ef):
    """The sticker state with corner piece cp[i] at place i twisted ct[i], edge piece ep[i] at place i flipped ef[i]."""
    s = list(range(54))
    for i in range(8):
        for k in range(3): s[CF[i][(k + ct[i]) % 3]] = CF[cp[i]][k]
    for i in range(12):
        for k in range(2): s[EF[i][(k + ef[i]) % 2]] = EF[ep[i]][k]
    return tuple(s)
def as_map(P):
    """A sticker map P (place i -> place P[i]) as corner place -> place, offset; edge place -> place, offset."""
    cd, ca, ed, ea = [], [], [], []
    for i in range(8):
        img = [P[x] for x in CF[i]]; j = corner_at(img); cd.append(j); ca.append(CF[j].index(img[0]))
        assert [CF[j][(ca[-1] + k) % 3] for k in range(3)] == img, 'not clockwise'
    for i in range(12):
        img = [P[x] for x in EF[i]]; j = edge_at(img); ed.append(j); ea.append(EF[j].index(img[0]))
    return cd, ca, ed, ea
def rotations():
    gens = [cube.MOVES[n] for n in ('x', 'y', 'z')]
    seen = {tuple(range(54)): ''}; todo = [tuple(range(54))]
    while todo:
        P = todo.pop()
        for g, nm in zip(gens, 'xyz'):
            Q = tuple(g[P[i]] for i in range(54))            # P then g
            if Q not in seen: seen[Q] = (seen[P] + ' ' + nm).strip(); todo.append(Q)
    assert len(seen) == 24
    return sorted(seen.items(), key=lambda kv: (len(kv[1]), kv[1]))
def conj(s, R):
    """The state seen after turning the whole cube by R (stickers and colours)."""
    t = [0] * 54
    for i in range(54): t[R[i]] = R[s[i]]
    return tuple(t)
