#!/usr/bin/env python3
"""Write out/tables/cubie.txt for the Rust tools: the 18 face turns and the 24 whole-cube rotations as maps on
corner and edge places with their twist / flip changes, the place numbering of judging-a-dr's DR tables, and test
vectors.  Everything is computed from the sticker model (cube.py) with the conventions of coords.py."""
import random, itertools
import cube, fe, coords
from coords import CF, EF, CORNERS, EDGES, NAMES

def corner_at(pl): return next(i for i in range(8) if set(CF[i]) == set(pl))
def edge_at(pl): return next(i for i in range(12) if set(EF[i]) == set(pl))
def as_map(P):
    """A sticker map P (place i -> place P[i]) as: corner place -> place, offset; edge place -> place, offset,
    where offset says where the reference facelet of the old place lands in the new place's facelet order."""
    cd, ca, ed, ea = [], [], [], []
    for i in range(8):
        img = [P[x] for x in CF[i]]; j = corner_at(img); cd.append(j); ca.append(CF[j].index(img[0]))
        assert [CF[j][(ca[-1] + k) % 3] for k in range(3)] == img, 'not clockwise'
    for i in range(12):
        img = [P[x] for x in EF[i]]; j = edge_at(img); ed.append(j); ea.append(EF[j].index(img[0]))
    return cd, ca, ed, ea

def cubie(s):
    """(cp, ct, ep, ef) of a sticker state: piece at each place and its twist / flip."""
    cp, ct, ep, ef = [], [], [], []
    for i in range(8):
        home = [s[x] for x in CF[i]]; p = corner_at(home); cp.append(p); ct.append(home.index(CF[p][0])); 
    for i in range(12):
        home = [s[x] for x in EF[i]]; p = edge_at(home); ep.append(p); ef.append(home.index(EF[p][0]))
    return cp, ct, ep, ef

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

def name_of(p): return ''.join(ch for ch, (a, sg) in (('U', (1, 1)), ('D', (1, -1)), ('F', (2, 1)), ('B', (2, -1)), ('R', (0, 1)), ('L', (0, -1))) if p[a] == sg)

if __name__ == '__main__':
    random.seed(7)
    L = []
    L.append('moves')
    for nm in NAMES:
        cd, ca, ed, ea = as_map(cube.MOVES[nm]); L.append(' '.join(map(str, cd + ca + ed + ea)))
    rots = rotations()
    L.append('rotations')
    for R, nm in rots:
        cd, ca, ed, ea = as_map(R)
        # where each axis goes: axis of the face that R carries the +face of axis a to
        ax = []
        for a in range(3):
            i = next(k for k, (p, n) in enumerate(cube.ST) if sum(abs(v) for v in p) == 1 and n[a] == 1)
            ax.append(fe.nax(R[i]))
        # where each face goes (U D R L F B)
        fm = []
        for fc in 'UDRLFB':
            a, sg = cube.AX[fc]
            i = next(k for k, (p, n) in enumerate(cube.ST) if sum(abs(v) for v in p) == 1 and n[a] == sg)
            fm.append('UDRLFB'.index(cube.FACE_OF[R[i]]))
        L.append(' '.join(map(str, cd + ca + ed + ea + ax + fm)))
    cnames = [name_of(p) for p in CORNERS]; enames = [name_of(p) for p in EDGES]
    def cidx(n): return next(i for i, x in enumerate(cnames) if set(x) == set(n))
    def eidx(n): return next(i for i, x in enumerate(enames) if set(x) == set(n))
    L.append('drmap')
    L.append(' '.join(str(cidx(n)) for n in 'UFR UFL UBL UBR DFR DFL DBL DBR'.split()))
    L.append(' '.join(str(eidx(n)) for n in 'UF UL UB UR DF DL DB DR'.split()))
    L.append(' '.join(str(eidx(n)) for n in 'FR FL BL BR'.split()))
    L.append('slotkind')          # kind of each edge place: 0 E-slice, 1 M-slice, 2 S-slice
    L.append(' '.join(str(0 if p[1] == 0 else 1 if p[0] == 0 else 2) for p in EDGES))
    L.append('tests')
    for _ in range(60):
        seq = [random.choice(NAMES) for _ in range(25)]; s = cube.do(cube.SOLVED, seq)
        cp, ct, ep, ef = cubie(s); co, eo, sl = coords.coords(s)
        r = random.randrange(24); cs = conj(s, rots[r][0]); cc = cubie(cs)
        inv = cubie(cube.inverse(s))
        L.append(' '.join(str(NAMES.index(m)) for m in seq) + ' | ' + ' '.join(map(str, cp + ct + ep + ef)) + f' | {co} {eo} {sl} | {r} | '
                 + ' '.join(map(str, cc[0] + cc[1] + cc[2] + cc[3])) + ' | ' + ' '.join(map(str, inv[0] + inv[1] + inv[2] + inv[3])))
    open('/data/fmc/is-dr-xs-worth-it/research/out/tables/cubie.txt', 'w').write('\n'.join(L) + '\n')
    print('corner places:', ' '.join(cnames)); print('edge places:', ' '.join(enames))
    print('rotations:', [nm or 'id' for _, nm in rots])
    print('wrote cubie.txt,', len(L), 'lines')
