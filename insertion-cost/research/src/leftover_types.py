#!/usr/bin/env python3
"""Leftover types and how many 3-cycles each needs, for corners and for edges, by exhaustive multiplication.

A corner state is (perm, twist): piece perm[i] sits at place i with twist[i] in Z3; an edge state the same with flips
in Z2.  The type of a state is its cycle structure with the twist (flip) sum of each cycle, for example a corner
3-cycle is {(3, 0)}, two twisted corners {(1, 1), (1, 2)}.  Only legal states are considered (total twist 0, even
permutation of each kind of piece, since an insertion skeleton leaves corners and edges solvable on their own).

Output: for every type reachable with one, two or three 3-cycles, how many states it has and the fewest 3-cycles."""
import itertools, collections, sys, json
def mul(a, b, m):
    """a then b: place i gets what b brings there from the state a."""
    (pa, ta), (pb, tb) = a, b
    return tuple(pa[pb[i]] for i in range(len(pa))), tuple((ta[pb[i]] + tb[i]) % m for i in range(len(pa)))
def ident(n): return tuple(range(n)), (0,) * n
def three_cycles(n, m):
    out = set()
    for i, j, k in itertools.permutations(range(n), 3):
        if not (i < j and i < k): continue                  # each cyclic order once: i is the smallest
        for oi in range(m):
            for oj in range(m):
                ok = (-oi - oj) % m
                p = list(range(n)); t = [0] * n
                # the piece at i goes to j, j to k, k to i
                p[j], p[k], p[i] = i, j, k; t[j], t[k], t[i] = oi, oj, ok
                out.add((tuple(p), tuple(t)))
    return out
def ctype(s, m):
    p, t = s; seen = [False] * len(p); out = []
    for i in range(len(p)):
        if seen[i]: continue
        j = i; L = 0; tw = 0
        while not seen[j]: seen[j] = True; tw += t[j]; j = p[j]; L += 1
        if L > 1 or tw % m: out.append((L, tw % m))
    return tuple(sorted(out, reverse=True))
def name(tp, kind):
    c = 'c' if kind == 'corner' else 'e'
    d = collections.Counter(tp)
    if not tp: return 'solved'
    if kind == 'corner':
        table = {((3, 0),): '3c', ((1, 2), (1, 1)): '2tc', ((1, 1),) * 3: '3tc', ((1, 2),) * 3: '3tc', ((2, 0), (2, 0)): '2c2c-pure', ((2, 2), (2, 1)): '2c2c-twisted',
                 ((3, 1), (1, 2)): '3c1t', ((3, 2), (1, 1)): '3c1t', ((5, 0),): '5c', ((3, 0), (3, 0)): '3c3c', ((3, 2), (3, 1)): '3c3c-twisted'}
    else:
        table = {((3, 0),): '3e', ((1, 1), (1, 1)): '2f', ((2, 0), (2, 0)): '2e2e', ((2, 1), (2, 1)): '2e2e-flipped', ((5, 0),): '5e', ((3, 0), (3, 0)): '3e3e', ((3, 1), (1, 1)): '3e1f', ((3, 1), (3, 1)): '3e3e-flipped'}
    return table.get(tp, ' '.join(f'{L}{c}' + (f'+{tw}' if tw else '') if L > 1 else f'1{c}+{tw}' for L, tw in tp))
def run(kind):
    n, m = (8, 3) if kind == 'corner' else (12, 2)
    C3 = sorted(three_cycles(n, m)); e = ident(n)
    need = {}; count = collections.Counter(); level = {e}; seen = {e}
    res = {'three_cycles': len(C3)}
    types = collections.OrderedDict()
    for k in (1, 2):
        nxt = set()
        for s in level:
            for g in C3:
                t = mul(s, g, m)
                if t not in seen: seen.add(t); nxt.add(t)
        for s in nxt:
            nm = name(ctype(s, m), kind); types.setdefault(nm, [k, 0]); types[nm][1] += 1
        level = nxt
    res['types'] = {nm: dict(fewest_3_cycles=v[0], states=v[1]) for nm, v in types.items()}
    res['states_within_two'] = len(seen)
    return res
if __name__ == '__main__':
    out = {}
    for kind in ('corner', 'edge'):
        r = run(kind); out[kind] = r
        print(kind, ': 3-cycles', r['three_cycles'], '| states reachable with at most two:', r['states_within_two'])
        for nm, v in sorted(r['types'].items(), key=lambda kv: (kv[1]['fewest_3_cycles'], -kv[1]['states'])): print(f"   {nm:22s} needs {v['fewest_3_cycles']}  states {v['states']}")
    json.dump(out, open('/data/fmc/insertion-cost/research/out/types.json', 'w'), indent=1)
