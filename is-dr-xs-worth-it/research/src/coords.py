#!/usr/bin/env python3
"""The three coordinates of a cube state that say how far it is from a DR on U/D colours, read off the stickers:

  co  (0..2186)  where the U/D-coloured sticker of each corner place points (twist 0, 1, 2 clockwise from the U/D face)
  eo  (0..2047)  for each edge place, whether the edge there is good for the F/B axis (the usual EO)
  sl  (0..494)   which four edge places hold the E-slice pieces (the edges with no U/D colour)

A state's kind of DR-xs (fe.look with c = U/D) is a function of these three, and a face turn acts on each of them
separately, so searches run on tables.  `export()` writes the move tables and the list of DR-xs kinds for the Rust
searcher."""
import itertools, struct, pickle, os, sys, random
import cube, fe
from cube import ST, IDX, FACE_OF

def det(a, b, c):
    return (a[0] * (b[1] * c[2] - b[2] * c[1]) - a[1] * (b[0] * c[2] - b[2] * c[0]) + a[2] * (b[0] * c[1] - b[1] * c[0]))
def corner_facelets(p):
    """Places of corner p: the U/D one first, then clockwise seen from outside."""
    pl = fe.CUBIES[p]; ud = next(i for i in pl if fe.nax(i) == 1); rest = [i for i in pl if i != ud]
    a, b = rest
    if det(ST[ud][1], ST[a][1], ST[b][1]) > 0: a, b = b, a           # det < 0 is clockwise
    return [ud, a, b]
def edge_facelets(p):
    """Places of edge p: the primary one first (U/D face if it has one, else F/B)."""
    pl = fe.CUBIES[p]
    pri = next((i for i in pl if fe.nax(i) == 1), None)
    if pri is None: pri = next(i for i in pl if fe.nax(i) == 2)
    return [pri, next(i for i in pl if i != pri)]
CORNERS = fe.CORNERS; EDGES = fe.EDGES
CF = [corner_facelets(p) for p in CORNERS]; EF = [edge_facelets(p) for p in EDGES]
E_PIECE = [p[1] == 0 for p in EDGES]                    # the edge whose home is this place has no U/D colour
COMB = {c: i for i, c in enumerate(itertools.combinations(range(12), 4))}
COMB_LIST = list(itertools.combinations(range(12), 4))

def twists(s): return [next(k for k in range(3) if fe.cax(s, CF[i][k]) == 1) for i in range(8)]
def flips(s):
    out = []
    for i in range(12):
        a, b = EF[i]
        has_ud = fe.cax(s, a) == 1 or fe.cax(s, b) == 1
        pri_col = 1 if has_ud else 2
        out.append(0 if fe.cax(s, a) == pri_col else 1)
    return out
def slice_places(s): return tuple(i for i in range(12) if fe.cax(s, EF[i][0]) != 1 and fe.cax(s, EF[i][1]) != 1)
def coords(s):
    t = twists(s); f = flips(s)
    assert sum(t) % 3 == 0 and sum(f) % 2 == 0
    return sum(t[i] * 3 ** i for i in range(7)), sum(f[i] << i for i in range(11)), COMB[slice_places(s)]

def make(cp=None, ct=None, ep=None, ef=None):
    """Sticker state with corner piece cp[i] at place i twisted ct[i], edge piece ep[i] at place i flipped ef[i]."""
    cp = cp or list(range(8)); ct = ct or [0] * 8; ep = ep or list(range(12)); ef = ef or [0] * 12
    s = list(range(54))
    for i in range(8):
        for k in range(3): s[CF[i][(k + ct[i]) % 3]] = CF[cp[i]][k]
    for i in range(12):
        for k in range(2): s[EF[i][(k + ef[i]) % 2]] = EF[ep[i]][k]
    return tuple(s)

NAMES = [f + s for f in 'UDRLFB' for s in ('', '2', "'")]          # move numbering: 3 * face + (quarter turns - 1)
def tables():
    co = [[0] * 18 for _ in range(2187)]; eo = [[0] * 18 for _ in range(2048)]; sl = [[0] * 18 for _ in range(495)]
    for v in range(2187):
        t = [(v // 3 ** i) % 3 for i in range(7)]; t.append((-sum(t)) % 3); s = make(ct=t)
        for m, nm in enumerate(NAMES): co[v][m] = coords_part(cube.apply(s, cube.MOVES[nm]), 0)
    for v in range(2048):
        f = [(v >> i) & 1 for i in range(11)]; f.append(sum(f) % 2); s = make(ef=f)
        for m, nm in enumerate(NAMES): eo[v][m] = coords_part(cube.apply(s, cube.MOVES[nm]), 1)
    home_e = [i for i in range(12) if E_PIECE[i]]; home_o = [i for i in range(12) if not E_PIECE[i]]
    for v, comb in enumerate(COMB_LIST):
        ep = [None] * 12; rest = iter(home_o)
        for k, i in enumerate(comb): ep[i] = home_e[k]
        for i in range(12):
            if ep[i] is None: ep[i] = next(rest)
        s = make(ep=ep)
        for m, nm in enumerate(NAMES): sl[v][m] = coords_part(cube.apply(s, cube.MOVES[nm]), 2)
    return co, eo, sl
def coords_part(s, which):
    if which == 0:
        t = twists(s); return sum(t[i] * 3 ** i for i in range(7))
    if which == 1:
        f = flips(s); return sum(f[i] << i for i in range(11))
    return COMB[slice_places(s)]

def export(outdir):
    os.makedirs(outdir, exist_ok=True)
    co, eo, sl = tables()
    with open(outdir + '/moves.bin', 'wb') as f:
        for tab in (co, eo, sl):
            for row in tab: f.write(struct.pack('<18H', *row))
    # which faces' layers hold a slice piece, per sl value: bit k set if a slice piece sits in the layer of face k (U D R L F B)
    with open(outdir + '/sl_layers.bin', 'wb') as f:
        for comb in COMB_LIST:
            b = 0
            for i in comb:
                p = EDGES[i]
                for k, fc in enumerate('UDRLFB'):
                    a, sg = cube.AX[fc]
                    if p[a] == sg: b |= 1 << k
            f.write(bytes([b]))
    print('wrote move tables to', outdir)

if __name__ == '__main__':
    random.seed(1)
    # coordinates commute with moves: random legal states, random moves
    co, eo, sl = tables()
    for _ in range(300):
        seq = [random.choice(NAMES) for _ in range(30)]; s = cube.do(cube.SOLVED, seq); c = coords(s)
        m = random.randrange(18); t = cube.apply(s, cube.MOVES[NAMES[m]])
        assert coords(t) == (co[c[0]][m], eo[c[1]][m], sl[c[2]][m])
    assert coords(cube.SOLVED) == (0, 0, COMB[tuple(i for i in range(12) if E_PIECE[i])])
    # F and B quarter turns are the only turns that change eo of a solved cube; all moves keep co of solved except side quarters
    assert [NAMES[m] for m in range(18) if eo[0][m] != 0] == ['F', "F'", 'B', "B'"]
    assert [NAMES[m] for m in range(18) if co[0][m] != 0] == ['R', "R'", 'L', "L'", 'F', "F'", 'B', "B'"]
    print('coordinates ok; solved =', coords(cube.SOLVED))
    export('/data/fmc/is-dr-xs-worth-it/research/out/tables')
