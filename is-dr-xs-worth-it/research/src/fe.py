#!/usr/bin/env python3
"""DR with flipped edges (DR-xs): what kind of state a cube is in, read off the stickers.

For a colour axis c and a face axis f (0 = R/L, 1 = U/D, 2 = F/B) a state "looks like a DR with colours c on faces f"
when
  * every corner has its c-coloured sticker on an f face,
  * the four edges without a c colour (the slice pieces) sit in the slice between the two f faces,
    and the eight other edges sit in the two f layers.
Then the signature records what is left to fix:
  flips   for each of the eight f-layer edge places, 1 if the edge there has its c colour on the side
  slice   for each of the four slice places, 1 if the slice edge there agrees with the centers (see slice_bit)
A true DR is c == f, no flips, all four slice bits 1.

Centers stay where they are in this model (a slice turn is written as the two outer turns), so "centers off by one
slice" shows up as c != f."""
import cube
from cube import ST, FACE_OF, AX

AXIS_OF_FACE = {f: AX[f][0] for f in 'UDRLFB'}
def nax(i): return max(range(3), key=lambda k: abs(ST[i][1][k]))          # axis of the face a place is on
def cax(s, i): return AXIS_OF_FACE[FACE_OF[s[i]]]                          # colour axis of the sticker at place i
CUBIES = {}
for i, (p, n) in enumerate(ST): CUBIES.setdefault(p, []).append(i)
CORNERS = sorted(p for p in CUBIES if len(CUBIES[p]) == 3)
EDGES = sorted(p for p in CUBIES if len(CUBIES[p]) == 2)

def look(s, c, f):
    """None if s does not look like a DR with colours c on faces f, else (flips, slice): two tuples of 0/1 in the
    order of EDGES restricted to the f layers / to the f slice."""
    for p in CORNERS:
        if not any(cax(s, i) == c and nax(i) == f for i in CUBIES[p]): return None
    h = next(a for a in (2, 1, 0) if a != f and a != c)
    flips = []; sl = []
    for p in EDGES:
        pl = CUBIES[p]; has_c = any(cax(s, i) == c for i in pl)
        if (p[f] == 0) == has_c: return None                # slice piece outside the slice, or the reverse
        if has_c: flips.append(0 if any(cax(s, i) == c and nax(i) == f for i in pl) else 1)
        else:
            i = next(i for i in pl if nax(i) == h)
            sl.append(1 if cax(s, i) == h else 0)
    return tuple(flips), tuple(sl)

def looks(s):
    """All (c, f, flips, slice) the state looks like."""
    out = []
    for c in range(3):
        for f in range(3):
            r = look(s, c, f)
            if r: out.append((c, f) + r)
    return out
def is_dr(sig): c, f, fl, sl = sig; return c == f and not any(fl) and all(sl)

FACES_OF_AXIS = {0: 'RL', 1: 'UD', 2: 'FB'}
SUF = {1: '', 2: '2', 3: "'"}
def gens(f):
    """The turns allowed on a DR-xs whose corners are oriented on faces f, grouped by axis so that no cancelling is
    possible between groups: (axis, text, cost in face turns, slices)."""
    out = []
    for a in range(3):
        p, q = FACES_OF_AXIS[a]
        for i in range(4):
            for j in range(4):
                if i == j == 0: continue
                if a != f and (i + j) % 2: continue                       # a lone quarter turn of a side face: not allowed
                if a != f and i % 2 == 0 and j % 2: continue
                txt = ' '.join(x for x in ((p + SUF[i]) if i else '', (q + SUF[j]) if j else '') if x)
                out.append((a, txt, (i > 0) + (j > 0), 1 if (a != f and i % 2) else 0))
    return out

if __name__ == '__main__':
    s = cube.SOLVED
    assert [x[:2] for x in looks(s)] == [(0, 0), (1, 1), (2, 2)] and all(is_dr(x) for x in looks(s))
    t = cube.do(s, "R L'")                # one slice: U/D colours now on F/B faces, the four M-slice edges flipped
    print('after R L\':', looks(t))
    t = cube.do(s, "U R2 F2 D' B2")
    print('a DR:', looks(t))
