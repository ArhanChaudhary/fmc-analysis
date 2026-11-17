"""Pairwise relations between the bad pieces of a switched case, up to the 8 reflections that keep the EO axis
(F/B), the DR axis (U/D) and so R/L.  Objects: a bad corner (place, axis of its U/D sticker: 0 = on R/L, 2 = on F/B),
a bad edge (an E piece in a U/D-layer place), a hole (a U/D piece in an E-slice place).  A relation class is an orbit
of unordered object pairs.  Top pair, fake pair and side pair are three of these classes."""
import os, sys, itertools
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, '..', 'src'))
import geom
from geom import CT, ESET, N_CO, N_SL, N0, CORNERS, EDGES, UD_AXIS

OBJ = []      # (kind, pos, axis)
for i, p in enumerate(CORNERS):
    for a in (0, 2): OBJ.append(('c', tuple(p), a))
for i, p in enumerate(EDGES):
    if p[1] != 0: OBJ.append(('e', tuple(p), -1))
for i, p in enumerate(EDGES):
    if p[1] == 0: OBJ.append(('h', tuple(p), -1))
OIX = {o: i for i, o in enumerate(OBJ)}
def refl(o, s):
    k, p, a = o
    return (k, tuple(p[i] * s[i] for i in range(3)), a)
SIGNS = list(itertools.product((1, -1), repeat=3))
def canon(o1, o2):
    best = None
    for s in SIGNS:
        t = tuple(sorted((refl(o1, s), refl(o2, s))))
        if best is None or t < best: best = t
    return best
CLASSES = {}; CLS = np.full((len(OBJ), len(OBJ)), -1, np.int16)
for i, a in enumerate(OBJ):
    for j, b in enumerate(OBJ):
        if i == j: continue
        if a[0] == 'c' and b[0] == 'c' and a[1] == b[1]: continue       # same corner place
        key = canon(a, b)
        if key not in CLASSES: CLASSES[key] = len(CLASSES)
        CLS[i, j] = CLASSES[key]
NCLS = len(CLASSES)
CKEY = {v: k for k, v in CLASSES.items()}

def pname(p): return geom.pname(p)
def describe(cid):
    (k1, p1, a1), (k2, p2, a2) = CKEY[cid]
    def o(k, p, a):
        if k == 'c': return f"corner {pname(p)}({'RL' if a == 0 else 'FB'})"
        return f"{'edge' if k == 'e' else 'hole'} {pname(p)}"
    return o(k1, p1, a1) + ' ~ ' + o(k2, p2, a2)

def objects(ixs):
    """Object index lists for the cosets ixs (all of one DRM): array [n, nobj]."""
    co = ixs // N_SL; sl = ixs % N_SL
    out = []
    for c, s in zip(co, sl):
        row = []
        for i in range(8):
            t = CT[c][i]
            if t: row.append(OIX[('c', tuple(CORNERS[i]), int(UD_AXIS[i][t]))])
        for i, p in enumerate(EDGES):
            if p[1] != 0 and ESET[s][i]: row.append(OIX[('e', tuple(p), -1)])
            if p[1] == 0 and not ESET[s][i]: row.append(OIX[('h', tuple(p), -1)])
        out.append(row)
    return np.array(out, dtype=np.int16)
def counts(ixs):
    ob = objects(ixs); n, k = ob.shape
    M = np.zeros((n, NCLS), np.int8)
    rows = np.arange(n)
    for a in range(k):
        for b in range(a + 1, k):
            np.add.at(M, (rows, CLS[ob[:, a], ob[:, b]]), 1)
    return M
if __name__ == '__main__':
    print(NCLS, 'relation classes')
    kinds = {}
    for cid in range(NCLS):
        (k1, _, _), (k2, _, _) = CKEY[cid]; kinds.setdefault(k1 + k2, []).append(cid)
    for k, v in kinds.items(): print(k, len(v))
    for cid in range(NCLS): print(cid, describe(cid))
