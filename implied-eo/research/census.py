#!/usr/bin/env python3
"""Every EO of 5 moves or less (normal + inverse), and which of them hold on exactly the same scrambles.

An EO  N (I)  on an axis is described by two sets of edges (section 'the two masks' of the write-up):
  v = the EO case N solves on normal (which places are bad),  u = the EO case I solves on the inverse.
N (I) is an EO on a scramble  <=>  every edge's badness on that axis = [its home place in u] xor [its place in v].
Two EOs on the same scrambles <=> same axis and (u, v) equal or both complemented, or axes a != b and
(u, v) differ on both sides by the slice across the third axis, or by its complement.
-> out/classes.json"""
import sys, os, json, itertools, random, collections
from eomodel import *
HERE = os.path.dirname(os.path.abspath(__file__))
MAXLEN = int(sys.argv[1]) if __name__ == '__main__' and len(sys.argv) > 1 else 5
PERM = {m: place_of(MOVES[m]) for m in MOVE_NAMES}
FLIP = {ax: {m: bad_mask(MOVES[m], ax) for m in MOVE_NAMES} for ax in range(3)}
def step(w, m, ax):
    r = FLIP[ax][m]
    for p in range(12):
        if w >> p & 1: r ^= 1 << PERM[m][p]
    return r
# EO length of every case, per axis, with every optimal solution's first moves kept for writing sequences
DIST = {}
for ax in range(3):
    dist = {0: 0}; frontier = [0]
    while frontier:
        nxt = []
        for w in frontier:
            for m in MOVE_NAMES:
                w2 = step(w, m, ax)
                if w2 not in dist: dist[w2] = dist[w] + 1; nxt.append(w2)
        frontier = nxt
    DIST[ax] = dist
    assert len(dist) == 2048
hist = collections.Counter(DIST[2].values())
print('EO cases by length (F/B):', [hist[i] for i in range(8)])
def solutions(w, ax, limit=None):
    """all optimal solutions of the case w (bad places) on that axis"""
    out = []
    def rec(w, seq):
        if limit and len(out) >= limit: return
        if w == 0: out.append(seq); return
        for m in MOVE_NAMES:
            if seq and (m[0] == seq[-1][0] or (AX[m[0]][0] == AX[seq[-1][0]][0] and FACES.index(m[0]) < FACES.index(seq[-1][0]))): continue
            w2 = step(w, m, ax)
            if DIST[ax][w2] == DIST[ax][w] - 1: rec(w2, seq + [m])
    rec(w, [])
    return out
def case_of(seq, ax): return bad_mask(apply(inv_seq(seq)), ax)

# --- checks of the two facts everything rests on, on random scrambles -------------------------------------------
rng = random.Random(1)
def rand_seq(n): return [rng.choice(MOVE_NAMES) for _ in range(n)]
for _ in range(20000):
    S = apply(rand_seq(25)); ax = rng.randrange(3); N = rand_seq(rng.randrange(0, 4)); I = rand_seq(rng.randrange(0, 4))
    v = case_of(N, ax); u = case_of(I, ax)
    T = compose(compose(apply(inv_seq(I)), S), apply(N))
    b = bad_mask(S, ax); pl = place_of(S)
    want = all(((b >> pl[h]) & 1) == ((u >> h) & 1) ^ ((v >> pl[h]) & 1) for h in range(12))
    assert eo_solved(T, ax) == want
    # change of axis
    ax2 = (ax + 1 + rng.randrange(2)) % 3; c = SLICE[3 - ax - ax2]; b2 = bad_mask(S, ax2)
    assert all(((b2 >> pl[h]) & 1) == ((b >> pl[h]) & 1) ^ ((c >> h) & 1) ^ ((c >> pl[h]) & 1) for h in range(12))
print('criterion and change of axis: 20,000 random scrambles, no mismatch')

# --- every presentation of at most MAXLEN moves, grouped by the set of scrambles it holds on ---------------------
def to_fb(ax, u, v):
    c = 0 if ax == 2 else SLICE[3 - ax - 2]
    u, v = u ^ c, v ^ c
    return min((u, v), (u ^ FULL, v ^ FULL))
by_len = {ax: collections.defaultdict(list) for ax in range(3)}
for ax in range(3):
    for w, l in DIST[ax].items(): by_len[ax][l].append(w)
classes = collections.defaultdict(list)
npres = 0
for ax in range(3):
    for lu in range(MAXLEN + 1):
        for lv in range(MAXLEN + 1 - lu):
            for u in by_len[ax][lu]:
                for v in by_len[ax][lv]:
                    classes[to_fb(ax, u, v)].append((ax, u, v, lu + lv)); npres += 1
multi = {k: p for k, p in classes.items() if len(p) > 1}
print(f'EOs of at most {MAXLEN} moves as (axis, inverse case, normal case): {npres:,}; sets of scrambles: {len(classes):,}; with two or more: {len(multi):,}')
pat = collections.Counter()
for k, p in multi.items():
    pat[tuple(sorted((AXIS_NAME[a] if False else a, lu_lv) for a, lu_lv in ((q[0], (DIST[q[0]][q[2]], DIST[q[0]][q[1]])) for q in p)))] += 1
for k, c in sorted(pat.items(), key=lambda kv: (len(kv[0]), kv[0])): print(c, [(AXIS_NAME[a], f'{n}({i})') for a, (n, i) in k])
json.dump({'maxlen': MAXLEN, 'npres': npres, 'nclasses': len(classes),
           'multi': [[list(q) for q in p] for p in multi.values()]}, open(os.path.join(HERE, 'out', f'classes{MAXLEN}.json'), 'w'))
