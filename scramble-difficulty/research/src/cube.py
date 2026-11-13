"""Cubie model of the 3x3 (Kociemba conventions) + facelets, axis-relative orientation, DR tests.

State = (cp, co, ep, eo): position i holds piece cp[i] with twist co[i] (corner 0..2, edge 0..1).
Product a*b = apply a, then b.  A move sequence applied to solved gives the state the scramble makes.
Corners: URF UFL ULB UBR DFR DLF DBL DRB.  Edges: UR UF UL UB DR DF DL DB FR FL BL BR.
Facelets: 54 chars, faces in order U R F D L B, 9 each, reading order (Kociemba / min2phase string).
"""
import itertools

FACES = 'URFDLB'
U, R, F, D, L, B = range(6)
# facelet index of sticker k (1..9) on face f
def fi(f, k): return 'URFDLB'.index(f) * 9 + k - 1
CF = [[fi('U',9),fi('R',1),fi('F',3)], [fi('U',7),fi('F',1),fi('L',3)], [fi('U',1),fi('L',1),fi('B',3)],
      [fi('U',3),fi('B',1),fi('R',3)], [fi('D',3),fi('F',9),fi('R',7)], [fi('D',1),fi('L',9),fi('F',7)],
      [fi('D',7),fi('B',9),fi('L',7)], [fi('D',9),fi('R',9),fi('B',7)]]
CC = [['U','R','F'], ['U','F','L'], ['U','L','B'], ['U','B','R'], ['D','F','R'], ['D','L','F'], ['D','B','L'], ['D','R','B']]
EF = [[fi('U',6),fi('R',2)], [fi('U',8),fi('F',2)], [fi('U',4),fi('L',2)], [fi('U',2),fi('B',2)],
      [fi('D',6),fi('R',8)], [fi('D',2),fi('F',8)], [fi('D',4),fi('L',8)], [fi('D',8),fi('B',8)],
      [fi('F',6),fi('R',4)], [fi('F',4),fi('L',6)], [fi('B',6),fi('L',4)], [fi('B',4),fi('R',6)]]
EC = [['U','R'], ['U','F'], ['U','L'], ['U','B'], ['D','R'], ['D','F'], ['D','L'], ['D','B'],
      ['F','R'], ['F','L'], ['B','L'], ['B','R']]
CNAME = ['URF', 'UFL', 'ULB', 'UBR', 'DFR', 'DLF', 'DBL', 'DRB']
ENAME = ['UR', 'UF', 'UL', 'UB', 'DR', 'DF', 'DL', 'DB', 'FR', 'FL', 'BL', 'BR']

_B = {  # basic quarter turns (Kociemba cubie definitions)
 'U': ([3,0,1,2,4,5,6,7],[0]*8,[3,0,1,2,4,5,6,7,8,9,10,11],[0]*12),
 'R': ([4,1,2,0,7,5,6,3],[2,0,0,1,1,0,0,2],[8,1,2,3,11,5,6,7,4,9,10,0],[0]*12),
 'F': ([1,5,2,3,0,4,6,7],[1,2,0,0,2,1,0,0],[0,9,2,3,4,8,6,7,1,5,10,11],[0,1,0,0,0,1,0,0,1,1,0,0]),
 'D': ([0,1,2,3,5,6,7,4],[0]*8,[0,1,2,3,5,6,7,4,8,9,10,11],[0]*12),
 'L': ([0,2,6,3,4,1,5,7],[0,1,2,0,0,2,1,0],[0,1,10,3,4,5,9,7,8,2,6,11],[0]*12),
 'B': ([0,1,3,7,4,5,2,6],[0,0,1,2,0,0,2,1],[0,1,2,11,4,5,6,10,8,9,3,7],[0,0,0,1,0,0,0,1,0,0,1,1]),
}
SOLVED = (tuple(range(8)), (0,)*8, tuple(range(12)), (0,)*12)

def mul(a, b):
    acp, aco, aep, aeo = a; bcp, bco, bep, beo = b
    return (tuple(acp[bcp[i]] for i in range(8)), tuple((aco[bcp[i]] + bco[i]) % 3 for i in range(8)),
            tuple(aep[bep[i]] for i in range(12)), tuple((aeo[bep[i]] + beo[i]) % 2 for i in range(12)))

def inv(a):
    cp, co, ep, eo = a
    icp = [0]*8; ico = [0]*8; iep = [0]*12; ieo = [0]*12
    for i in range(8): icp[cp[i]] = i
    for i in range(8): ico[i] = (-co[icp[i]]) % 3
    for i in range(12): iep[ep[i]] = i
    for i in range(12): ieo[i] = eo[iep[i]]
    return (tuple(icp), tuple(ico), tuple(iep), tuple(ieo))

MOVES = {}
for f in 'URFDLB':
    m = SOLVED
    for p, suf in ((1, ''), (2, '2'), (3, "'")):
        m = mul(m, _B[f]); MOVES[f + suf] = m

def parse(s):
    return [t for t in s.replace('(', ' ').replace(')', ' ').split() if t]

def apply(state, moves):
    for t in (parse(moves) if isinstance(moves, str) else moves):
        state = mul(state, MOVES[t])
    return state

def seq(moves): return apply(SOLVED, moves)

def inv_moves(moves):
    ms = parse(moves) if isinstance(moves, str) else moves
    out = []
    for t in reversed(ms):
        out.append(t[0] if t.endswith("'") else (t if t.endswith('2') else t + "'"))
    return out

def facelets(st):
    cp, co, ep, eo = st
    f = [None] * 54
    for i in range(6): f[i * 9 + 4] = FACES[i]
    for i in range(8):
        for n in range(3):
            f[CF[i][(n + co[i]) % 3]] = CC[cp[i]][n]
    for i in range(12):
        for n in range(2):
            f[EF[i][(n + eo[i]) % 2]] = EC[ep[i]][n]
    return ''.join(f)

def from_facelets(s):
    cp = [0]*8; co = [0]*8; ep = [0]*12; eo = [0]*12
    for i in range(8):
        for ori in range(3):
            if s[CF[i][ori]] in 'UD': break
        c1, c2 = s[CF[i][(ori + 1) % 3]], s[CF[i][(ori + 2) % 3]]
        for j in range(8):
            if CC[j][1] == c1 and CC[j][2] == c2:
                cp[i] = j; co[i] = ori % 3
    for i in range(12):
        for j in range(12):
            if s[EF[i][0]] == EC[j][0] and s[EF[i][1]] == EC[j][1]: ep[i] = j; eo[i] = 0
            if s[EF[i][0]] == EC[j][1] and s[EF[i][1]] == EC[j][0]: ep[i] = j; eo[i] = 1
    return (tuple(cp), tuple(co), tuple(ep), tuple(eo))

# ---- axis-relative features (sticker rules, checked by move invariance in selftest) ----
AX = {'UD': 'UD', 'FB': 'FB', 'RL': 'RL'}
AXES = ['UD', 'FB', 'RL']
OTHER = {'UD': ('FB', 'RL'), 'FB': ('UD', 'RL'), 'RL': ('UD', 'FB')}
def faxis(face): return 'UD' if face in 'UD' else ('FB' if face in 'FB' else 'RL')

def co_axis(fl, ax):
    """per corner position: twist w.r.t. axis ax (0 = the ax-coloured sticker is on an ax face)."""
    out = []
    for i in range(8):
        cols = [fl[k] for k in CF[i]]
        # the sticker of corner position i that lies on an ax face
        faces = [FACES[k // 9] for k in CF[i]]
        pos = [n for n in range(3) if faxis(faces[n]) == ax][0]
        cn = [n for n in range(3) if faxis(cols[n]) == ax][0]
        out.append((cn - pos) % 3 if faces[(pos + 1) % 3] else 0)
    return out

def eo_axis(fl, ax):
    """per edge position: 1 = bad edge for EO on axis ax (ax quarter turns flip it).
    Reference axis Q = first other axis in order UD, FB, RL; primary colour = Q colour if the piece has one else ax colour;
    primary face = Q face of the position if it has one else its ax face."""
    Q = [a for a in AXES if a != ax][0]
    out = []
    for i in range(12):
        cols = [fl[k] for k in EF[i]]
        faces = [FACES[k // 9] for k in EF[i]]
        cax = [faxis(c) for c in cols]
        pc = cax.index(Q) if Q in cax else (cax.index(ax) if ax in cax else None)
        fax = [faxis(f) for f in faces]
        pf = fax.index(Q) if Q in fax else fax.index(ax)
        if pc is None:  # piece has colours of Q? impossible: every edge has two of the three axes
            raise ValueError
        out.append(0 if pc == pf else 1)
    return out

SLICE = {'UD': {8, 9, 10, 11}, 'FB': {0, 2, 4, 6}, 'RL': {1, 3, 5, 7}}   # middle-slice positions of each axis (E, S, M)

def is_dr(st, ax):
    fl = facelets(st)
    if any(co_axis(fl, ax)): return False
    if any(eo_axis(fl, OTHER[ax][0])): return False
    ep = st[2]
    return all(ep[i] in SLICE[ax] for i in SLICE[ax])

def selftest():
    import random
    rnd = random.Random(1)
    for _ in range(50):
        s = [rnd.choice(list(MOVES)) for _ in range(25)]
        st = seq(s)
        assert mul(st, inv(st)) == SOLVED and seq(inv_moves(s)) == inv(st)
        fl = facelets(st)
        assert from_facelets(fl) == st
        for ax in AXES:
            c0 = sum(1 for x in co_axis(fl, ax) if x); e0 = sum(eo_axis(fl, ax))
            for m in MOVES:
                fl2 = facelets(mul(st, MOVES[m]))
                c1 = sum(1 for x in co_axis(fl2, ax) if x); e1 = sum(eo_axis(fl2, ax))
                if faxis(m[0]) == ax or m.endswith('2'):
                    assert c1 == c0, (ax, m)          # ax turns and half turns keep ax-CO count
                if not (faxis(m[0]) == ax and not m.endswith('2')):
                    assert e1 == e0, (ax, m)          # only ax quarter turns change ax-EO
                else:
                    assert (e1 - e0) % 2 == 0
    # Kociemba eo is EO on F/B
    st = seq("R U F' L2 D B R'")
    assert list(st[3]) == eo_axis(facelets(st), 'FB')
    assert list(st[1]) == [ (x) for x in st[1]] and [1 if x else 0 for x in st[1]] == [1 if x else 0 for x in co_axis(facelets(st), 'UD')]
    assert is_dr(seq("U R2 F2 D' L2 B2 U2"), 'UD') and not is_dr(seq("U R F2"), 'UD')
    assert is_dr(seq("R U2 F2 L' D2"), 'RL')
    print('cube selftest ok')

if __name__ == '__main__':
    selftest()
