#!/usr/bin/env python3
"""One inserted 3c comm, position by position: for the 3c skeletons of out/sample_3c_n<n>.tsv, the fewest added moves
at every position of the skeleton with a sequence of at most 8, 9 and 10 moves.  Done by py3.py (Python, sticker
model), so it is also a check of `instools`: the minimum over the positions must be the tool's L8_one and L10_one.

Writes out/onepos_3c_n<n>.tsv: idx, then for L = 8, 9, 10 the n + 1 costs (x = no sequence within the cap there)."""
import sys, multiprocessing
import cube, cubie, py3
OUT = py3.OUT
def work(job):
    idx, sk, left, l8, l10 = job
    T = py3.table('c', 10)
    skel = py3.nums(sk); cp, ct, ep, ef = [[int(x) for x in part.split(',')] for part in left.split(';')]
    c = cubie.make(cp, ct, ep, ef); n = len(skel); g = cube.inverse(c); res = {8: [None] * (n + 1), 9: [None] * (n + 1), 10: [None] * (n + 1)}
    for i in range(n, -1, -1):
        if i < n: g = cube.compose(cube.compose(py3.MS[skel[i]], g), py3.MI[skel[i]])
        pre = skel[:i]; post = skel[i:]; b = {8: None, 9: None, 10: None}
        for a in T.get(g, ()):
            v = py3.clen(pre + list(a) + post) - n
            for L in (8, 9, 10):
                if len(a) <= L and (b[L] is None or v < b[L]): b[L] = v
        for L in (8, 9, 10): res[L][i] = b[L]
    mn = lambda v: min((x for x in v if x is not None), default=None)
    tool = lambda v: None if v == 'inf' else int(v)
    assert mn(res[8]) == tool(l8) and mn(res[10]) == tool(l10), (idx, mn(res[8]), l8, mn(res[10]), l10)
    return idx + '\t' + '\t'.join(','.join('x' if x is None else str(x) for x in res[L]) for L in (8, 9, 10))
if __name__ == '__main__':
    ns = [int(x) for x in sys.argv[1].split(',')]; count = int(sys.argv[2]) if len(sys.argv) > 2 else 20000
    py3.table('c', 10)
    for n in ns:
        jobs = []
        with open(f'{OUT}sample_3c_n{n}.tsv') as f:
            head = f.readline().rstrip('\n').split('\t'); col = {h: i for i, h in enumerate(head)}
            for line in f:
                p = line.rstrip('\n').split('\t')
                if len(jobs) >= count: break
                jobs.append((p[0], p[1], p[2], p[col['L8_one']], p[col['L10_one']]))
        with multiprocessing.Pool(3) as pool: lines = pool.map(work, jobs, chunksize=200)
        with open(f'{OUT}onepos_3c_n{n}.tsv', 'w') as f:
            f.write('idx\tL8\tL9\tL10\n'); f.write('\n'.join(lines) + '\n')
        print(f'n = {n}: {len(lines)} skeletons, the minimum over positions equals instools at L = 8 and L = 10 for all of them', flush=True)
