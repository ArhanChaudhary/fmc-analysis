#!/usr/bin/env python3
"""From an edge-orientation pattern to the kind of DR-xs you land on, exhaustively.

Frame: the DR-xs is for the U/D colours (its slice pieces are the E-slice pieces) with the corners oriented on faces f.
The edges of such a state are described by: which of the eight layer places hold an M-slice piece and which an
S-slice piece (70 ways), which layer edges are flipped (128 ways), and whether the slice pieces agree with the
centers (2 ways).  For each of these 17,920 arrangements per f this computes the orientation of every edge for each
axis, and the kind of the state (slices needed, flips, how the flipped edges split between the M and S pieces).

Routes that never turn the faces of axis e by a quarter keep every edge's orientation for e, so "pattern for e before"
= "pattern for e in the DR-xs".  A pattern here is uniform by class of piece: (E bad?, M bad?, S bad?)."""
import itertools, collections, sys
import coords, fe
EF = coords.EF; EDGES = coords.EDGES
KIND = ['E' if p[1] == 0 else 'M' if p[0] == 0 else 'S' for p in EDGES]
G = {'FB': {'E': 0, 'M': 0, 'S': 0}, 'UD': {'E': 0, 'M': 1, 'S': 0}, 'RL': {'E': 1, 'M': 0, 'S': 0}}
AX = {'RL': 0, 'UD': 1, 'FB': 2}
def slices(on_axis, nflips, bit):
    if on_axis: return (0 if nflips == 0 else 2) if bit else 3
    return (1 if nflips == 4 else 3) if bit else 2
def arrangements(fname):
    f = AX[fname]
    slice_slots = [i for i in range(12) if EDGES[i][f] == 0]; layer_slots = [i for i in range(12) if EDGES[i][f] != 0]
    h = next(a for a in (2, 1, 0) if a != f and a != 1)
    for mset in itertools.combinations(range(8), 4):                       # layer places holding M pieces
        for fl in range(256):
            if bin(fl).count('1') % 2: continue
            for bit in (0, 1):
                piece = {}; ef = {}
                for k, i in enumerate(layer_slots):
                    piece[i] = 'M' if k in mset else 'S'
                    flipped = (fl >> k) & 1
                    # ef = 0 puts the U/D sticker on the place's reference facelet
                    on_f = fe.nax(EF[i][0]) == f
                    ef[i] = 0 if (on_f != bool(flipped)) else 1
                for i in slice_slots:
                    piece[i] = 'E'
                    # slice bit: the sticker at the h place has colour h
                    for e in (0, 1):
                        hplace = next(x for x in EF[i] if fe.nax(x) == h)
                        fb_sticker_place = EF[i][e]
                        col_at_h = 2 if fb_sticker_place == hplace else 0
                        if (col_at_h == h) == bool(bit): ef[i] = e
                assert sum(ef.values()) % 2 == 0
                pat = {}
                for ax in ('FB', 'UD', 'RL'):
                    bad = collections.Counter()
                    for i in range(12):
                        if ef[i] ^ G[ax][KIND[i]] ^ G[ax][piece[i]]: bad[piece[i]] += 1
                    pat[ax] = (bad['E'], bad['M'], bad['S'])
                nfl = bin(fl).count('1')
                fm = sum(1 for k, i in enumerate(layer_slots) if (fl >> k) & 1 and piece[i] == 'M')
                yield dict(f=fname, bit=bit, flips=nfl, split=(max(fm, nfl - fm), min(fm, nfl - fm)), slices=slices(f == 1, nfl, bit), pat=pat, piece=dict(piece), ef=dict(ef))
ROWS = [r for f in ('UD', 'RL', 'FB') for r in arrangements(f)]
def outcomes(axis, pattern, f):
    """What the DR-xs on faces f can be when, for `axis`, exactly the classes in `pattern` are bad (each class all bad
    or all good): a counter of (slices, flips, split)."""
    want = tuple(4 if c in pattern else 0 for c in 'EMS')
    return collections.Counter((r['slices'], r['flips'], r['split']) for r in ROWS if r['f'] == f and r['pat'][axis] == want)
def describe(c):
    if not c: return 'cannot happen'
    n = sum(c.values())
    return '; '.join(f"{'DR' if s == 0 else f'DR-{s}s'} {fl} flipped{'' if fl in (0, 8) else f' split {sp[0]}-{sp[1]}'}{'' if len(c) == 1 else f' ({100 * v / n:.0f}%)'}" for (s, fl, sp), v in sorted(c.items()))
if __name__ == '__main__':
    print(len(ROWS), 'arrangements')
    print('--- uniform patterns: slice EO axis, bad classes (E = the slice pieces, M and S = the other two slices), faces of the corners')
    for axis in ('FB', 'UD'):
        for pattern in ('', 'E', 'M', 'S', 'EM', 'ES', 'MS', 'EMS'):
            for f in ('UD', 'RL', 'FB'):
                print(f"axis {axis}  bad {pattern or '-':3s}  corners on {f}:  {describe(outcomes(axis, pattern, f))}")
    # share of DR-1s among slice-EO states by number of bad edges among the other eight (any arrangement), for the route rules
    print('--- by flavour: chance that the DR-xs on faces f is a DR-1s, over all arrangements with the slice pieces all good / all bad for the axis')
    for axis in ('FB', 'UD'):
        for flav in (0, 4):
            for f in ('UD', 'RL', 'FB'):
                rs = [r for r in ROWS if r['f'] == f and r['pat'][axis][0] == flav]
                c = collections.Counter(r['slices'] for r in rs)
                print(f"axis {axis}  slice pieces {'bad ' if flav else 'good'}  corners on {f}:  " + '  '.join(f'{k} slices {100 * v / len(rs):.1f}%' for k, v in sorted(c.items())))
