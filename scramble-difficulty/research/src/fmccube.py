"""fmccube.py — a small facelet-level 3x3x3 simulator, enough to turn "scramble + moves to DR" into a DR state.

Stickers are (position, normal) pairs with coordinates in {-1,0,1}: x = R(+)/L(-), y = U(+)/D(-), z = F(+)/B(-).
Conventions agree with src/drcore.h (checked by `python fmccube.py --selftest`).
"""
import re, sys

FACE_NORMAL = {'U': (0, 1, 0), 'D': (0, -1, 0), 'R': (1, 0, 0), 'L': (-1, 0, 0), 'F': (0, 0, 1), 'B': (0, 0, -1)}
NORMAL_FACE = {v: k for k, v in FACE_NORMAL.items()}

def rot_u(v): x, y, z = v; return (-z, y, x)      # U direction (clockwise seen from above)
def rot_r(v): x, y, z = v; return (x, z, -y)      # R direction
def rot_f(v): x, y, z = v; return (y, -x, z)      # F direction
def inv(f): return lambda v: f(f(f(v)))
ROT = {'U': (rot_u, 1, [1]), 'D': (inv(rot_u), 1, [-1]), 'E': (inv(rot_u), 1, [0]), 'y': (rot_u, 1, [-1, 0, 1]),
       'R': (rot_r, 0, [1]), 'L': (inv(rot_r), 0, [-1]), 'M': (inv(rot_r), 0, [0]), 'x': (rot_r, 0, [-1, 0, 1]),
       'F': (rot_f, 2, [1]), 'B': (inv(rot_f), 2, [-1]), 'S': (rot_f, 2, [0]), 'z': (rot_f, 2, [-1, 0, 1]),
       'Uw': (rot_u, 1, [0, 1]), 'Dw': (inv(rot_u), 1, [-1, 0]), 'Rw': (rot_r, 0, [0, 1]), 'Lw': (inv(rot_r), 0, [-1, 0]),
       'Fw': (rot_f, 2, [0, 1]), 'Bw': (inv(rot_f), 2, [-1, 0])}
for a in 'udrlfb': ROT[a] = ROT[a.upper() + 'w']

def solved():
    st = {}
    for f, n in FACE_NORMAL.items():
        axis = [i for i in range(3) if n[i]][0]
        for a in (-1, 0, 1):
            for b in (-1, 0, 1):
                p = [a, b]; p.insert(axis, n[axis]); st[(tuple(p), n)] = f
    return st

def turn(st, base, times):
    f, axis, layers = ROT[base]
    for _ in range(times % 4):
        st = {((f(p), f(n)) if p[axis] in layers else (p, n)): c for (p, n), c in st.items()}
    return st

TOKEN = re.compile(r"([UDRLFBMESxyzudrlfb]w?)(2'?|'2?|3|’)?")
def parse(seq):
    """-> list of (base, quarter turns)"""
    out = []
    for m in TOKEN.finditer(seq.replace('’', "'").replace('`', "'")):
        base, suf = m.group(1), m.group(2) or ''
        out.append((base, 2 if '2' in suf else 3 if ("'" in suf or suf == '3') else 1))
    return out

def invert(moves): return [(b, (4 - t) % 4) for b, t in reversed(moves)]

def split_niss(seq):
    """'R U (F B) D' -> (normal moves, inverse-side moves)"""
    normal, inverse, depth, buf = [], [], 0, ''
    def flush(d):
        nonlocal buf
        (inverse if d else normal).extend(parse(buf)); buf = ''
    for ch in seq:
        if ch == '(': flush(depth); depth = 1
        elif ch == ')': flush(depth); depth = 0
        else: buf += ch
    flush(depth)
    return normal, inverse

def apply(st, moves):
    for b, t in moves: st = turn(st, b, t)
    return st

def state_after(scramble, solution=''):
    """Cube as seen on the normal side after `solution` (which may contain NISS brackets)."""
    n, i = split_niss(solution)
    return apply(apply(apply(solved(), invert(i)), parse(scramble)), n)

def conj_rotation(st, f):
    """Look at the same cube with the axes renamed by rotation f (positions, normals and colours all rotate)."""
    return {(f(p), f(n)): NORMAL_FACE[f(FACE_NORMAL[c])] for (p, n), c in st.items()}

CORNERS = [(1, 1, 1), (-1, 1, 1), (-1, 1, -1), (1, 1, -1), (1, -1, 1), (-1, -1, 1), (-1, -1, -1), (1, -1, -1)]
UD_EDGES = [(0, 1, 1), (-1, 1, 0), (0, 1, -1), (1, 1, 0), (0, -1, 1), (-1, -1, 0), (0, -1, -1), (1, -1, 0)]
E_EDGES = [(1, 0, 1), (-1, 0, 1), (-1, 0, -1), (1, 0, -1)]

def colours_at(st, p):
    return {n: st[(p, n)] for n in FACE_NORMAL.values() if (p, n) in st and sum(abs(v) for v in p) > 1}

def home_colours(p):
    return frozenset(NORMAL_FACE[tuple((p[i] if j == i else 0) for j in range(3))] for i in range(3) if p[i])

def to_dr_arrays(st):
    """If st is domino-reduced on U/D (pieces oriented, E-slice edges in the E slice): (c, e, s) arrays, else None."""
    for (p, n), c in st.items():
        if sum(abs(v) for v in p) == 1 and NORMAL_FACE[n] != c: return None          # centres must be home
    out = []
    for group in (CORNERS, UD_EDGES, E_EDGES):
        homes = {home_colours(p): i for i, p in enumerate(group)}
        arr = []
        for p in group:
            cols = colours_at(st, p)
            key = frozenset(cols.values())
            if key not in homes: return None
            if p[1] != 0:
                if cols[(0, p[1], 0)] not in 'UD': return None                        # U/D sticker must face U/D
            else:
                if cols[(0, 0, p[2])] not in 'FB': return None                        # E-slice edges oriented
            arr.append(homes[key])
        out.append(arr)
    return tuple(out)

def find_dr(st):
    """-> (axis name, (c, e, s)) for the first axis on which st is a DR, looking at it with that axis vertical."""
    views = [('U/D', lambda v: v), ('F/B', rot_r), ('R/L', inv(rot_f))]   # x turns F up; z' turns R up
    for name, f in views:
        arrs = to_dr_arrays(conj_rotation(st, f) if name != 'U/D' else st)
        if arrs: return name, arrs
    return None, None

if __name__ == '__main__' and '--selftest' in sys.argv:
    # the ten DR moves must give the same arrays as src/genlean.c prints
    expect = {"U": [3,0,1,2,4,5,6,7], "D": [0,1,2,3,5,6,7,4], "R2": [7,1,2,4,3,5,6,0], "L2": [0,6,5,3,4,2,1,7], "F2": [5,4,2,3,1,0,6,7], "B2": [0,1,7,6,4,5,3,2]}
    for mv, c in expect.items():
        got = to_dr_arrays(state_after(mv))
        assert got and got[0] == c, (mv, got)
    assert to_dr_arrays(state_after("R")) is None and find_dr(state_after("R U F"))[0] is None
    assert to_dr_arrays(state_after("R U R' U' R' F R2 U' R' U' R U R' F'")) is not None      # a PLL is a DR state
    assert find_dr(state_after("M2 U M2 U2 M2 U M2"))[0] == 'U/D'
    assert find_dr(state_after("R L' F2 R' L"))[0] is not None
    s = state_after("R' U' F D2 L2", "L2 D2 (R' U' F)")     # a full solution written with NISS => solved
    assert to_dr_arrays(s) == ([0,1,2,3,4,5,6,7], [0,1,2,3,4,5,6,7], [0,1,2,3]), to_dr_arrays(s)
    print('selftest ok')
