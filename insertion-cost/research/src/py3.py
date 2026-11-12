#!/usr/bin/env python3
"""A second, independent implementation of one inserted 3-cycle, in Python on the sticker model.

  table(kind, L)       every sequence of at most L moves of every corner ('c') or edge ('e') 3-cycle, read from
                       `instools list` once and cached in out/algs3<kind>_L<L>.json; each sequence is replayed on the
                       sticker model before it is used
  clen(seq)            length of a sequence of move numbers with all cancelling done (same rule as cube.cancel)
  per_position(...)    for a skeleton and a 3-cycle leftover: the fewest added moves at every position 0..n

Move numbers: 3 * face + (quarter turns - 1), faces in the order U D R L F B (cubie.NAMES)."""
import os, json, subprocess, itertools, functools
import cube, cubie
OUT = '/data/fmc/insertion-cost/research/out/'
BIN = '/data/fmc/insertion-cost/research/instools/target/release/instools'
NAMES = cubie.NAMES; NUM = {n: i for i, n in enumerate(NAMES)}
MS = [cube.do(cube.SOLVED, [n]) for n in NAMES]                       # state of each move
MI = [cube.inverse(s) for s in MS]
def nums(seq): return [NUM[t] for t in (cube.parse(seq) if isinstance(seq, str) else seq)]
def text(seq): return ' '.join(NAMES[m] for m in seq)
def runs(seq):
    out = []
    for m in seq:
        f = m // 3; ax = f >> 1
        if out and out[-1][0] == ax:
            r = out[-1]; r[1 + (f & 1)] = (r[1 + (f & 1)] + m % 3 + 1) & 3
            if not r[1] and not r[2]: out.pop()
        else:
            r = [ax, 0, 0]; r[1 + (f & 1)] = m % 3 + 1; out.append(r)
    return out
def clen(seq): return sum((r[1] != 0) + (r[2] != 0) for r in runs(seq))
def cancel(seq):
    out = []
    for ax, a, b in runs(seq):
        if a: out.append(3 * (2 * ax) + a - 1)
        if b: out.append(3 * (2 * ax + 1) + b - 1)
    return out
def state(seq):
    s = cube.SOLVED
    for m in seq: s = cube.compose(s, MS[m])
    return s
def elements(kind):
    """All 3-cycles of corners or of edges as (cp, ct, ep, ef)."""
    n, m = (8, 3) if kind == 'c' else (12, 2); out = []
    for i, j, k in itertools.permutations(range(n), 3):
        if not (i < j and i < k): continue
        for oi in range(m):
            for oj in range(m):
                p = list(range(n)); t = [0] * n
                p[j], p[k], p[i] = i, j, k; t[j], t[k], t[i] = oi, oj, (-oi - oj) % m
                out.append((p, t, list(range(12)), [0] * 12) if kind == 'c' else (list(range(8)), [0] * 8, p, t))
    return out
def elem_text(e): return ';'.join(','.join(map(str, part)) for part in e)
@functools.lru_cache(None)
def table(kind, L):
    """{sticker state of the 3-cycle: [sequences as tuples of move numbers, shortest first]}"""
    path = f'{OUT}algs3{kind}_L{L}.json'
    if not os.path.exists(path):
        d = {}
        for e in elements(kind):
            out = subprocess.run([BIN, 'list', elem_text(e), str(L)], capture_output=True, text=True, check=True).stdout
            d[elem_text(e)] = [l for l in out.split('\n') if l.strip()]
        json.dump(d, open(path, 'w'))
    d = json.load(open(path)); T = {}; n = 0
    for key, seqs in d.items():
        cp, ct, ep, ef = [[int(x) for x in part.split(',')] for part in key.split(';')]
        s = cubie.make(cp, ct, ep, ef); lst = []
        for q in seqs:
            a = tuple(nums(q)); assert len(a) <= L and cancel(a) == list(a) and state(a) == s, q
            lst.append(a); n += 1
        T[s] = sorted(lst, key=len)
    return T
def per_position(T, skel, c, L, positions=None):
    """skel: move numbers; c: sticker state of the leftover (scramble then skeleton).  Returns a list of n + 1 entries:
    the fewest added moves with one sequence of T (length <= L) inserted at that position, None where there is none."""
    n = len(skel); g = cube.inverse(c); out = [None] * (n + 1)
    for i in range(n, -1, -1):
        if i < n: g = cube.compose(cube.compose(MS[skel[i]], g), MI[skel[i]])
        if positions is not None and i not in positions: continue
        best = None; pre = skel[:i]; post = skel[i:]
        for a in T.get(g, ()):
            if len(a) > L: break
            v = clen(pre + list(a) + post) - n
            if best is None or v < best: best = v
        out[i] = best
    return out
if __name__ == '__main__':
    import random
    rnd = random.Random(5)
    for _ in range(3000):
        s = [rnd.randrange(18) for _ in range(rnd.randrange(0, 30))]
        assert [NAMES[m] for m in cancel(s)] == cube.cancel([NAMES[m] for m in s])
    print('cancel agrees with cube.cancel on 3000 random sequences')
    for kind, L in (('c', 8), ('c', 10), ('e', 8), ('e', 10)):
        T = table(kind, L); import collections
        c = collections.Counter(len(a) for v in T.values() for a in v)
        print(kind, L, 'elements', len(T), 'sequences by length', dict(sorted(c.items())))
