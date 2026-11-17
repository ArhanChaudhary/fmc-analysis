#!/usr/bin/env python3
"""Implied EOs that are not the trick: the superflip on both sides.  First examples (6 moves between two axes,
7 moves on one axis), each checked on scrambles by turning the stickers.  -> out/beyond.json"""
import os, json, random
from eomodel import *
import census as E
HERE = os.path.dirname(os.path.abspath(__file__))
D = E.DIST
rng = random.Random(5)
KEEP = {ax: [m for m in MOVE_NAMES if AX[m[0]][0] != ax or m.endswith('2')] for ax in range(3)}
def nice(seqs):
    return min(seqs, key=lambda s: (sum(m.endswith("'") for m in s), sum(m.endswith('2') for m in s), [FACES.index(m[0]) for m in s]))
def sol(w, ax): return nice(E.solutions(w, ax))
def txt(n, i): return (' '.join(n) + (' ' if n and i else '') + (f"({' '.join(i)})" if i else '')) or '(skip)'
def holds(scr, a, n, i): return eo_solved(compose(compose(apply(inv_seq(i)), apply(scr)), apply(n)), a)
def example(ax, bx, t, la, lb, want_sides):
    """cases u, v on ax with side lengths as wanted, partner on bx by toggling t"""
    cands = [w for w in D[ax] if (D[ax][w], D[bx][w ^ t]) in want_sides]
    cands.sort(key=lambda w: (len(E.solutions(w, ax)), w))
    for v in cands:
        for u in cands:
            if D[ax][u] + D[ax][v] == la and D[bx][u ^ t] + D[bx][v ^ t] == lb:
                X = (sol(v, ax), sol(u, ax)); Y = (sol(v ^ t, bx), sol(u ^ t, bx))
                scr = None
                for _ in range(200):
                    s = X[1] + [rng.choice(KEEP[ax]) for _ in range(18)] + inv_seq(X[0])
                    assert holds(s, ax, *X) and holds(s, bx, *Y)
                    scr = s
                return {'X': txt(*X), 'X_axis': AXIS_NAME[ax], 'Y': txt(*Y), 'Y_axis': AXIS_NAME[bx], 'scramble': ' '.join(scr),
                        'X_cases': [mask_names(v), mask_names(u)], 'Y_cases': [mask_names(v ^ t), mask_names(u ^ t)]}
out = {}
out['six'] = example(2, 0, SLICE[1], 6, 6, {(3, 3)})
out['seven'] = example(2, 2, FULL, 7, 7, {(3, 4), (4, 3)})
# counts
import collections
def pairs(ax, bx, t, L):
    side = collections.Counter((D[ax][w], D[bx][w ^ t]) for w in D[ax])
    return sum(n1 * n2 for (a1, b1), n1 in side.items() for (a2, b2), n2 in side.items() if a1 + a2 <= L and b1 + b2 <= L)
out['counts'] = {'trick': {L: pairs(2, 0, FULL ^ SLICE[1], L) for L in (4, 5, 6)},
                 'slice': {L: pairs(2, 0, SLICE[1], L) for L in (5, 6)},
                 'same_axis': {L: pairs(2, 2, FULL, L) // 2 for L in (6, 7)}}
print(json.dumps(out, indent=1))
json.dump(out, open(os.path.join(HERE, 'out', 'beyond.json'), 'w'), indent=1)
