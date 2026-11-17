#!/usr/bin/env python3
"""The edge model of the implied-EO study, from geometry (no typed-in tables).

An edge cubie sits at a point of {-1,0,1}^3 with exactly one 0; x = R(+)/L(-), y = U(+)/D(-), z = F(+)/B(-).
A facelet is (cubie, axis of its normal).  A face turn is a quarter turn of the layer about its outward normal,
clockwise seen from outside.  A state is where every sticker has gone (facelet -> facelet).

EO on an axis: every edge has a key sticker and every place a key facelet; the edge is good when its key sticker is
on a key facelet.  For the F/B axis the key is the U/D one if there is one, else the F/B one (so U, D, R, L, F2, B2
keep every edge good or bad and F, B flip the four edges they turn).  The other axes are the same rule turned.
"""
import itertools
AX = {'R': (0, 1), 'L': (0, -1), 'U': (1, 1), 'D': (1, -1), 'F': (2, 1), 'B': (2, -1)}
FACES = 'UDRLFB'
AXIS_NAME = {0: 'RL', 1: 'UD', 2: 'FB'}
# key priority per EO axis: (first, second, third); the EO axis is always in the middle
PRIO = {2: (1, 2, 0), 0: (1, 0, 2), 1: (2, 1, 0)}

CUBIES = [c for c in itertools.product((-1, 0, 1), repeat=3) if sum(1 for v in c if v == 0) == 1]
def name(c):
    s = ''
    for ax, pos, neg in ((1, 'U', 'D'), (2, 'F', 'B'), (0, 'R', 'L')):
        if c[ax] == 1: s += pos
        elif c[ax] == -1: s += neg
    return s
ORDER = ['UF', 'UB', 'DF', 'DB', 'UR', 'UL', 'DR', 'DL', 'FR', 'FL', 'BR', 'BL']   # M slice, S slice, E slice
CUBIES.sort(key=lambda c: ORDER.index(name(c)))
POS = {c: i for i, c in enumerate(CUBIES)}
NAMES = [name(c) for c in CUBIES]
FACELETS = [(c, a) for c in CUBIES for a in range(3) if c[a] != 0]
FID = {f: i for i, f in enumerate(FACELETS)}

def rot(v, ax, sgn):
    """quarter turn about the outward normal (axis ax, sign sgn), clockwise seen from outside"""
    x, y, z = v
    if ax == 1: r = (-z, y, x)       # U: front -> left
    elif ax == 0: r = (x, z, -y)     # R: front -> up
    else: r = (y, -x, z)             # F: up -> right
    if sgn == 1: return r
    # the opposite face turns the other way about the same axis: apply the inverse (three times)
    return rot(rot(r, ax, 1), ax, 1)

def quarter(face):
    ax, sgn = AX[face]
    perm = list(range(24))
    for (c, a), i in FID.items():
        if c[ax] == sgn:
            c2 = rot(c, ax, sgn); n = [0, 0, 0]; n[a] = 1; n2 = rot(tuple(n), ax, sgn)
            a2 = [k for k in range(3) if n2[k] != 0][0]
            perm[i] = FID[(c2, a2)]
    return tuple(perm)

IDENT = tuple(range(24))
def compose(s, t):
    """do s, then t"""
    return tuple(t[s[i]] for i in range(24))
Q = {f: quarter(f) for f in FACES}
MOVES = {}
for f in FACES:
    MOVES[f] = Q[f]; MOVES[f + '2'] = compose(Q[f], Q[f]); MOVES[f + "'"] = compose(MOVES[f + '2'], Q[f])
MOVE_NAMES = [f + s for f in FACES for s in ('', '2', "'")]
def inv_move(m): return m[0] + {'': "'", '2': '2', "'": ''}[m[1:]]
def inv_seq(seq): return [inv_move(m) for m in reversed(seq)]
def apply(seq, s=IDENT):
    for m in seq: s = compose(s, MOVES[m])
    return s
def parse(txt): return txt.split()

def is_key(i, eo_axis):
    c, a = FACELETS[i]
    axes = [k for k in range(3) if c[k] != 0]
    best = min(axes, key=lambda k: PRIO[eo_axis].index(k))
    return a == best
KEY = {ax: [is_key(i, ax) for i in range(24)] for ax in range(3)}
KEYF = {ax: [i for i in range(24) if KEY[ax][i]] for ax in range(3)}     # one per cubie, in cubie order
for ax in range(3): assert [POS[FACELETS[i][0]] for i in KEYF[ax]] == list(range(12))

def bad_mask(s, eo_axis):
    """bit p set: the edge now at place p is bad on that axis"""
    m = 0
    for i in KEYF[eo_axis]:
        j = s[i]
        if not KEY[eo_axis][j]: m |= 1 << POS[FACELETS[j][0]]
    return m
def eo_solved(s, eo_axis): return bad_mask(s, eo_axis) == 0
def place_of(s):
    """place_of[h] = where the edge whose home is h sits now"""
    return [POS[FACELETS[s[KEYF[2][h]]][0]] for h in range(12)]
def mask_names(m): return ' '.join(NAMES[p] for p in range(12) if m >> p & 1) or '-'
def mask_of(names): return sum(1 << NAMES.index(n) for n in names.split())
SLICE = {0: mask_of('UF UB DF DB'), 1: mask_of('FR FL BR BL'), 2: mask_of('UR UL DR DL')}  # slice across each axis: M, E, S
FULL = (1 << 12) - 1

if __name__ == '__main__':
    # sanity: the EO-keeping moves keep every edge, the axis' quarter turns flip their four edges
    for ax in range(3):
        for m in MOVE_NAMES:
            a, sgn = AX[m[0]]
            b = bad_mask(MOVES[m], ax)
            if a == ax and m[1:] != '2':
                assert bin(b).count('1') == 4 and all(CUBIES[p][a] == sgn for p in range(12) if b >> p & 1), (ax, m)
            else: assert b == 0, (ax, m)
    print('edges:', NAMES)
    print('U cycle:', [NAMES[place_of(MOVES['U'])[h]] for h in range(12)])
    for f in FACES: print(f, [(NAMES[h], NAMES[place_of(MOVES[f])[h]]) for h in range(12) if place_of(MOVES[f])[h] != h])
