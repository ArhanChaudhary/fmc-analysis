#!/usr/bin/env python3
"""Every kind of DR-xs state (U/D colours on some pair of faces, slice pieces in their slice, any flips), and for each
the fewest slices and the fewest face turns to a real DR using only DR-xs moves: turns of the two oriented faces,
half turns of the others, and slice turns written as two outer turns (R L', F B, ...).

The kind of a state is its signature (fe.look with c = U/D colours): which faces the corners are oriented on, which
of the eight layer-edge places hold a flipped edge, and the four slice bits.  Costs are counted in face turns with
all cancelling done: consecutive turns about one axis are one group (R2 then R L' is R' L', two turns)."""
import heapq, sys, collections
import cube, fe
C = 1
def sig_of(s, f):
    r = fe.look(s, C, f); assert r is not None
    return (f,) + r
def third(a, b): return 3 - a - b

def explore():
    start = sig_of(cube.SOLVED, 1)
    rep = {start: cube.SOLVED}; nbr = {}; todo = [start]; checked = 0
    while todo:
        g = todo.pop(); s = rep[g]; out = []
        for a, txt, cost, sl in fe.gens(g[0]):
            t = cube.do(s, txt); f2 = third(a, g[0]) if sl else g[0]
            h = sig_of(t, f2); out.append((a, txt, cost, sl, h))
            if h not in rep: rep[h] = t; todo.append(h)
            elif checked < 20000:
                # same signature reached through another state: its moves must lead to the same signatures
                checked += 1
                u = rep[h]
                for a2, txt2, _, sl2 in fe.gens(h[0])[:6]:
                    f3 = third(a2, h[0]) if sl2 else h[0]
                    assert sig_of(cube.do(t, txt2), f3) == sig_of(cube.do(u, txt2), f3), 'signature is not a complete invariant'
        nbr[g] = out
    return start, rep, nbr

def dijkstra(nbr, weight):
    """dist[(sig, last axis)] to a real DR; last axis 3 = free start.  weight(cost, slices) -> edge weight."""
    # search backwards from the DR: build reverse edges
    rev = collections.defaultdict(list)
    for g, out in nbr.items():
        for a, txt, cost, sl, h in out: rev[h].append((g, a, txt, weight(cost, sl)))
    INF = 10 ** 9
    # forward formulation by relaxation over (sig, last): small graph, do Bellman-Ford style with a heap from targets
    dist = {}
    # d(g, last) = 0 if g is a DR, else min over (a != last) of w + d(h, a)
    # compute by Dijkstra on reversed graph over nodes (g, last): edge (h, a) <- (g, last) for every last != a
    heap = []
    for g in nbr:
        if fe.is_dr((C,) + g):
            for last in range(4): dist[(g, last)] = 0; heapq.heappush(heap, (0, g, last))
    best_move = {}
    while heap:
        d, h, a_in = heapq.heappop(heap)
        if dist.get((h, a_in), INF) < d: continue
        # predecessors: states g with a move on axis a to h, where that move's axis a == a_in is what "last" means at h
        for g, a, txt, w in rev[h]:
            if a != a_in and not fe.is_dr((C,) + h): continue
            if fe.is_dr((C,) + h) and a_in != a: continue
            for last in range(4):
                if last == a: continue
                nd = d + w
                if nd < dist.get((g, last), INF):
                    dist[(g, last)] = nd; best_move[(g, last)] = (txt, h, a); heapq.heappush(heap, (nd, g, last))
    return dist, best_move

def path(best_move, g, last=3):
    out = []
    while (g, last) in best_move:
        txt, h, a = best_move[(g, last)]; out.append(txt); g, last = h, a
    return ' '.join(out)

if __name__ == '__main__':
    start, rep, nbr = explore()
    print(len(nbr), 'kinds of DR-xs state (signatures) reachable from a DR')
    by_f = collections.Counter(g[0] for g in nbr); print('by face axis (0 R/L, 1 U/D, 2 F/B):', dict(by_f))
    print('slice-bit patterns seen:', collections.Counter(g[2] for g in nbr))
    print('number of flips seen:', sorted(collections.Counter((g[0] == C, sum(g[1])) for g in nbr).items()))
    dsl, _ = dijkstra(nbr, lambda cost, sl: sl)
    dmv, bm = dijkstra(nbr, lambda cost, sl: cost)
    tab = collections.Counter()
    for g in nbr: tab[(dsl[(g, 3)], g[0] == C, sum(g[1]), dmv[(g, 3)])] += 1
    print('slices | centers on axis | flips | turns to DR | kinds')
    for k in sorted(tab): print(' ', k, tab[k])
    import pickle
    pickle.dump(dict(rep=rep, nbr=nbr, dsl=dsl, dmv=dmv, bm=bm), open('/data/fmc/is-dr-xs-worth-it/research/out/fecosets.pkl', 'wb'))
