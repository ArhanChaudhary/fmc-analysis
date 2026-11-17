#!/usr/bin/env python3
"""Which change of cases links two EOs on the same scrambles, and how short each kind can be.
Between axes a != b the two sides change by the same set t: either the 8 edges off the slice across the third axis
(what adding the two axes' four quarter turns to both sides does) or the 4 edges of that slice (the same plus a
superflip on both sides).  On one axis the only link is the superflip on both sides (complement both cases)."""
import sys, collections, json, os
from eomodel import *
import census as E
D = E.DIST
INF = 99
# shortest pair for each kind, any length: min over (u, v) of max(len X, len Y) and of len X + len Y
def best(ax, bx, t):
    la = sorted(D[ax].items(), key=lambda kv: kv[1])
    # per side: cost pairs (l_a(w), l_b(w ^ t)); the pair's lengths are sums over the two sides
    side = collections.Counter((D[ax][w], D[bx][w ^ t]) for w in D[ax])
    res = collections.Counter()
    for (a1, b1), n1 in side.items():
        for (a2, b2), n2 in side.items():
            res[(a1 + a2, b1 + b2)] += n1 * n2
    return side, res
for label, ax, bx, t in (('F/B -> R/L, 8 edges off the E slice (the trick)', 2, 0, FULL ^ SLICE[1]),
                         ('F/B -> R/L, the 4 E-slice edges (trick + superflip)', 2, 0, SLICE[1]),
                         ('F/B -> F/B, all 12 (superflip on both sides)', 2, 2, FULL)):
    side, res = best(ax, bx, t)
    m = min(max(k) for k in res)
    print(label)
    print('   per side (length on first axis, length on second axis): count', sorted(side.items()))
    print('   shortest pair: both at most', m, '->', sorted((k, v) for k, v in res.items() if max(k) == m))
    for L in (5, 6, 7):
        print(f'   pairs with both at most {L}:', sum(v for k, v in res.items() if max(k) <= L) // (2 if ax == bx else 1))
