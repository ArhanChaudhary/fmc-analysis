#!/usr/bin/env python3
"""Two 3c comms done the way a person (or Insertion Finder at a given "greedy") does them: find the best first
insertion, keep every first insertion within g moves of it, and take the best second insertion after each.

For the skeletons of out/sample_<type>_n<n>.tsv, with sequences of at most L moves (py3.py: Python, sticker model):
  m1        the fewest added moves of a first insertion (one that leaves a 3c)
  firsts    how many first insertions there are in all (position, cycle, sequence), and how many at m1
  g0..g3    the best total when only first insertions within 0, 1, 2, 3 moves of m1 are followed up
  exact     `instools`' L<L>_two for the same skeleton (the true minimum over every pair, nesting allowed)
With --full every first insertion is followed up, and the result must equal `exact`: a second check of the tool.
Writes out/greedy_<type>_n<n>_L<L>.tsv."""
import sys, multiprocessing
import cube, cubie, py3
OUT = py3.OUT
def splits(T, c):
    """The 3-cycles d with c·d a 3-cycle (d is what the first insertion does, seen at the end of the skeleton)."""
    return [d for d in T if cube.compose(c, d) in T]
def work(job):
    idx, sk, left, tool, L, full = job
    T = py3.table('c', 10 if L > 8 else 8)
    skel = py3.nums(sk); cp, ct, ep, ef = [[int(x) for x in part.split(',')] for part in left.split(';')]
    c = cubie.make(cp, ct, ep, ef); n = len(skel)
    ds = splits(T, c); cur = list(ds); firsts = []
    for i in range(n, -1, -1):
        if i < n:
            m, mi = py3.MS[skel[i]], py3.MI[skel[i]]
            cur = [cube.compose(cube.compose(m, a), mi) for a in cur]
        pre = skel[:i]; post = skel[i:]
        for k, a in enumerate(cur):
            for alg in T[a]:
                if len(alg) > L: break
                s1 = py3.cancel(pre + list(alg) + post)
                firsts.append((len(s1) - n, k, s1))
    if not firsts: return f'{idx}\t{len(ds)}\t0\t0\tinf\tinf\tinf\tinf\tinf\t{tool}'
    m1 = min(f[0] for f in firsts); memo = {}
    def second(f):
        key = (f[1], tuple(f[2]))
        if key not in memo:
            v = [x for x in py3.per_position(T, f[2], cube.compose(c, ds[f[1]]), L) if x is not None]
            memo[key] = min(v) if v else None
        return memo[key]
    res = []
    for g in (0, 1, 2, 3) + ((99,) if full else ()):
        best = None
        for f in firsts:
            if f[0] <= m1 + g:
                v = second(f)
                if v is not None and (best is None or f[0] + v < best): best = f[0] + v
        res.append(best)
    if full: assert (res[-1] is None and tool == 'inf') or str(res[-1]) == tool, (idx, res, tool)
    t = lambda v: 'inf' if v is None else str(v)
    return f"{idx}\t{len(ds)}\t{len(firsts)}\t{sum(1 for f in firsts if f[0] == m1)}\t{m1}\t" + '\t'.join(t(v) for v in res[:4]) + f'\t{tool}'
if __name__ == '__main__':
    typ, n, L, count = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]); full = '--full' in sys.argv
    py3.table('c', 10 if L > 8 else 8); jobs = []
    with open(f'{OUT}sample_{typ}_n{n}.tsv') as f:
        head = f.readline().rstrip('\n').split('\t'); col = {h: i for i, h in enumerate(head)}
        for line in f:
            p = line.rstrip('\n').split('\t')
            if len(jobs) >= count or p[col[f'L{L}_two']] == 'nc': break
            jobs.append((p[0], p[1], p[2], p[col[f'L{L}_two']], L, full))
    with multiprocessing.Pool(3) as pool: lines = pool.map(work, jobs, chunksize=20)
    name = f'{OUT}greedy_{typ}_n{n}_L{L}' + ('_full' if full else '') + '.tsv'
    with open(name, 'w') as f:
        f.write('idx\tsplits\tfirsts\tfirsts_at_best\tm1\tg0\tg1\tg2\tg3\texact\n'); f.write('\n'.join(lines) + '\n')
    print(f'{typ} n = {n} L = {L}: {len(lines)} skeletons' + ('; following up every first insertion gives the tool\'s `two` for all of them' if full else ''), flush=True)
