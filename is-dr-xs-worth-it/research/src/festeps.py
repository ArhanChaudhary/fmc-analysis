#!/usr/bin/env python3
"""Steps between kinds of DR-xs: fewest face turns from a DR-3s to a DR-2s, from a DR-2s to a DR-1s, and from each to
a real DR, with and without the saving when the move just before was a quarter turn of a side face (a trigger's last
move), which a slice about the same axis merges with (R then R' L is just L)."""
import pickle, heapq, collections, sys
import fe
from fecosets import C
d = pickle.load(open('/data/fmc/is-dr-xs-worth-it/research/out/fecosets.pkl', 'rb'))
nbr, dsl, dmv = d['nbr'], d['dsl'], d['dmv']
def to_set(target):
    """dist[(g, last axis)] = fewest turns from kind g to the target set when the previous group was about `last` (3 = none)."""
    rev = collections.defaultdict(list)
    for g, out in nbr.items():
        for a, txt, cost, sl, h in out: rev[h].append((g, a, cost))
    dist = {}; heap = []
    for g in nbr:
        if target(g):
            for last in range(4): dist[(g, last)] = 0; heapq.heappush(heap, (0, g, last))
    while heap:
        dd, h, a_in = heapq.heappop(heap)
        if dist[(h, a_in)] < dd: continue
        for g, a, w in rev[h]:
            if a != a_in: continue
            for last in range(4):
                if last == a: continue
                if dd + w < dist.get((g, last), 99): dist[(g, last)] = dd + w; heapq.heappush(heap, (dd + w, g, last))
    return dist
def after_quarter(g, dist):
    """Fewest extra turns from kind g to the target when the move just made was a quarter turn of a side face:
    min over the two side axes of the last move.  A group about that axis merges with it."""
    f = g[0]; best = {}
    for ax in range(3):
        if ax == f: continue
        b = dist.get((g, ax), 99)                           # not touching that axis first
        for a, txt, cost, sl, h in nbr[g]:
            if a != ax: continue
            # txt is "P^i Q^j" on axis ax; the last move was a quarter of P or of Q: try both faces and both directions
            parts = {t[0]: (2 if t.endswith('2') else 3 if t.endswith("'") else 1) for t in txt.split()}
            for face in fe.FACES_OF_AXIS[ax]:
                for q0 in (1, 3):
                    i = parts.get(face, 0); other = [v for k, v in parts.items() if k != face]
                    new = ((q0 + i) % 4 != 0) + (1 if other else 0) - 1          # change in turn count
                    if i == 0 and not other: continue
                    if (q0 + i) % 4 == 0 and not other: continue                   # that just undoes the last move
                    b = min(b, new + dist.get((h, ax), 99))
        best[ax] = b
    return best
P = print
import json
RES = {}
to1 = to_set(lambda g: dsl[(g, 3)] <= 1); to2 = to_set(lambda g: dsl[(g, 3)] <= 2); to0 = to_set(lambda g: dsl[(g, 3)] == 0)
for name, X, dist in (('DR-2s -> DR-1s (or better)', 2, to1), ('DR-3s -> DR-2s (or better)', 3, to2), ('DR-1s -> DR', 1, to0), ('DR-2s -> DR', 2, to0), ('DR-3s -> DR', 3, to0)):
    free = collections.Counter(); ctx_best = collections.Counter(); ctx_worst = collections.Counter()
    for g in nbr:
        if dsl[(g, 3)] != X: continue
        free[dist[(g, 3)]] += 1
        b = after_quarter(g, dist); ctx_best[min(b.values())] += 1; ctx_worst[max(b.values())] += 1
    n = sum(free.values())
    RES[name] = dict(kinds=n, scratch=dict(sorted(free.items())), after_quarter_better=dict(sorted(ctx_best.items())), after_quarter_worse=dict(sorted(ctx_worst.items())))
    P(f'{name}: {n} kinds')
    P('   turns, counted from scratch:                 ', dict(sorted(free.items())), f'mean {sum(k * v for k, v in free.items()) / n:.2f}')
    P('   after a side quarter turn, the better axis:  ', dict(sorted(ctx_best.items())), f'mean {sum(k * v for k, v in ctx_best.items()) / n:.2f}')
    P('   after a side quarter turn, the worse axis:   ', dict(sorted(ctx_worst.items())), f'mean {sum(k * v for k, v in ctx_worst.items()) / n:.2f}')
# 2s by number of flips and centers
P('DR-2s -> DR-1s from scratch, by (corners on the colour\'s own faces, flips):')
tab = collections.defaultdict(collections.Counter)
for g in nbr:
    if dsl[(g, 3)] == 2: tab[(g[0] == C, sum(g[1]))][to1[(g, 3)]] += 1
for k in sorted(tab): P('  ', k, dict(sorted(tab[k].items())))
json.dump(RES, open('/data/fmc/is-dr-xs-worth-it/research/out/festeps.json', 'w'), indent=1)
