#!/usr/bin/env python3
"""Independent sticker-level implementation of everything the route study reads off a state, for the checks.

Nothing here comes from the Rust code: moves, pieces, tetrads, bad pieces, the corner quarter-turn count, the
4a/4b shape, the HTR test and the NISS readings are all rebuilt from the 54-sticker model of
is-dr-xs-worth-it/research/src/cube.py (geometry only).

  corner tetrad      sign of x*y*z of the position (UFR UBL DFL DBR = +1)
  bad corner         a corner whose home is in the other tetrad
  bad edge           an M-slice edge (home x = 0) in an S-slice position (z = 0) or the reverse; counted both ways
  corner qt count    0-1 BFS over the 40320 corner arrangements: quarter turns cost 1, half turns 0, targets the
                     arrangements reachable from solved or from U D' by half turns
  shape              4 bad corners: 'a' if half turns can bring the four positions onto one face, else 'b'
  frame              more than 4 bad corners, or 4 and more than 4 bad edges: count 8 - n of each
  HTR                corners reachable from solved by half turns and no bad edge
"""
import sys, collections, itertools
sys.path.insert(0, '/data/fmc/is-dr-xs-worth-it/research/src')
import cube
from cube import SOLVED, ST, MOVES, do, apply, inv_seq

DRM = ["U", "U2", "U'", "D", "D2", "D'", "R2", "L2", "F2", "B2"]
HALF = ["U2", "D2", "R2", "L2", "F2", "B2"]
QT = {"U", "U'", "D", "D'"}
CPOS = sorted({p for p, n in ST if all(abs(v) == 1 for v in p)})
EPOS = sorted({p for p, n in ST if sorted(abs(v) for v in p) == [0, 1, 1] and p[1] != 0})   # U/D-layer edges
FIRST = {}
for i, (p, n) in enumerate(ST):
    FIRST.setdefault(p, i)
TETRAD = {p: p[0] * p[1] * p[2] for p in CPOS}
FACESET = {f: frozenset(p for p in CPOS if p[a] == sg) for f, (a, sg) in cube.AX.items()}

def corners(s):
    """tuple: home position index of the corner at each corner position"""
    return tuple(CPOS.index(ST[s[FIRST[p]]][0]) for p in CPOS)
def edges(s):
    return tuple(EPOS.index(ST[s[FIRST[p]]][0]) for p in EPOS)

def _arr_of(m):
    return corners(apply(SOLVED, MOVES[m]))
CMOV = {m: _arr_of(m) for m in DRM}
def cmul(a, b):          # arrangement of (a then b)
    return tuple(a[b[p]] for p in range(8))

def _qt_table():
    ident = tuple(range(8))
    ud = cmul(CMOV['U'], CMOV["D'"])
    dist = {}
    dq = collections.deque()
    for t in (ident, ud):
        dist[t] = 0; dq.append(t)
    while dq:                       # 0-1 BFS
        x = dq.popleft()
        for m in DRM:
            y = cmul(x, CMOV[m]); w = 1 if m in QT else 0
            if y not in dist or dist[x] + w < dist[y]:
                dist[y] = dist[x] + w
                (dq.append if w else dq.appendleft)(y)
    hc = {ident}; st = [ident]
    while st:
        x = st.pop()
        for m in HALF:
            y = cmul(x, CMOV[m])
            if y not in hc: hc.add(y); st.append(y)
    return dist, hc
QTC, HC = _qt_table()
assert len(QTC) == 40320 and len(HC) == 96

POSMAP = {m: {p: ST[MOVES[m][FIRST[p]]][0] for p in CPOS} for m in HALF}   # position p goes to POSMAP[m][p]
_shape_cache = {}
def shape(mask):
    mask = frozenset(mask)
    if mask in _shape_cache: return _shape_cache[mask]
    seen = {mask}; st = [mask]; ok = False
    while st:
        x = st.pop()
        if x in FACESET.values(): ok = True
        for m in HALF:
            y = frozenset(POSMAP[m][p] for p in x)
            if y not in seen: seen.add(y); st.append(y)
    _shape_cache[mask] = 'a' if ok else 'b'
    return _shape_cache[mask]

def label(s):
    c = corners(s); e = edges(s)
    badpos = [CPOS[i] for i in range(8) if TETRAD[CPOS[i]] != TETRAD[CPOS[c[i]]]]
    n = len(badpos)
    ne = sum(1 for i in range(8) if (EPOS[i][0] == 0) != (EPOS[e[i]][0] == 0))
    if n > 4 or (n == 4 and ne > 4):
        nb, ne = 8 - n, 8 - ne
    else:
        nb = n
    q = QTC[c]
    letter = shape(badpos) if nb == 4 else 'c'
    return f'{nb}{letter}{q} {ne}e'
def in_htr(s):
    c = corners(s); e = edges(s)
    return c in HC and all((EPOS[i][0] == 0) == (EPOS[e[i]][0] == 0) for i in range(8))

def key(kind, labels, sw, post_qt=None):
    parts = []
    for i, l in enumerate(labels):
        parts.append(('(' if sw is not None and i == sw else '') + l)
    out = ' > '.join(parts) + (')' if sw is not None else '')
    if kind == 'H':
        out += ' | qt' if post_qt else ' | ht'
    return f'{kind}:{out}'

def reading(scr, fin, k, inverse_first):
    """Simulate one NISS reading of finish `fin` (list of moves) of the DR scramble `scr` (list), split at k.
    Normal first: fin[:k] on normal, then inv(fin[k:]) on inverse.  Inverse first: inv(fin[k:]) on inverse,
    then fin[:k] on normal.  Returns (H key, F key, HTR length), with a side that holds no quarter turn folded
    into the other side (the reading is then linear)."""
    n = len(fin)
    A, B = list(fin[:k]), inv_seq(fin[k:])
    if inverse_first:
        s1 = do(SOLVED, inv_seq(scr)); part1 = B
        s2_of = lambda: do(SOLVED, inv_seq(inv_seq(scr) + B)); part2 = A
    else:
        s1 = do(SOLVED, scr); part1 = A
        s2_of = lambda: do(SOLVED, inv_seq(scr + A)); part2 = B
    q1 = any(m in QT for m in part1); q2 = any(m in QT for m in part2)
    if not q1 and part2:            # nothing happens on the first side: linear on the second
        s1, part1, part2 = s2_of(), part2, []
        pre = len(A) if not inverse_first else len(B)
    else:
        pre = 0
    if not q2 and part2:            # nothing happens on the second side: linear on the first (the half turns
        part2 = []                  # left are post-HTR on the other side)
    seq = [(1, m) for m in part1] + [(2, m) for m in part2]
    hl, fl = [label(s1)], [label(s1)]
    hsw = fsw = None
    hdone = in_htr(s1); htr_len = pre if hdone else None
    done_at = 0 if hdone else None
    st = s1; side = 1; moved = pre
    rest_moves = [m for _, m in seq]
    for idx, (sd, m) in enumerate(seq):
        if sd == 2 and side == 1:
            side = 2; st = s2_of()
            fsw = len(fl)
            if not hdone: hsw = len(hl)
        st = apply(st, MOVES[m]); moved += 1
        if m in QT:
            l = label(st)
            fl.append(l)
            if not hdone:
                hl.append(l)
                if in_htr(st):
                    hdone = True; htr_len = moved; done_at = idx + 1
    # post-HTR part: every move of the reading after the HTR point, plus the half turns folded away above
    post = rest_moves[done_at:] + ([m for m in (B if not inverse_first else A)] if (not q2 and (B if not inverse_first else A)) else [])
    return key('H', hl, hsw, any(m in QT for m in post)), key('F', fl, fsw), htr_len
