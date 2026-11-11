#!/usr/bin/env python3
"""Compare the exact table with nissy's optimal DR-finish solver (step drudfin) on random DR positions."""
import random, subprocess, re, os
random.seed(20261111)
MOVES = ["U", "U2", "U'", "D", "D2", "D'", "R2", "L2", "F2", "B2"]
Q = ['/data/fmc/judging-a-dr/research/drtools/target/release/drtools', 'query', '/data/fmc/judging-a-dr/research/data/drbfs', '/data/fmc/judging-a-dr/research/data/tables']
scrs = []
for _ in range(40):
    s = []
    while len(s) < random.randint(14, 28):
        m = random.choice(MOVES)
        if s and s[-1][0] == m[0]: continue
        s.append(m)
    scrs.append(' '.join(s))
out = subprocess.run(Q, input='\n'.join(scrs) + '\n', capture_output=True, text=True).stdout.strip().split('\n')
ours = [int(l.rsplit('exact=', 1)[1]) for l in out]
agree = 0
for s, o in zip(scrs, ours):
    r = subprocess.run(['/data/fmc/tools/nissy-2.0.8/nissy', 'solve', 'drudfin', '-o', s], capture_output=True, text=True, timeout=900,
                       env=dict(os.environ, NISSYDATA='/data/fmc/tools/nissy-data')).stdout.strip().split('\n')[0]
    n = int(re.search(r'\((\d+)\)\s*$', r).group(1))
    agree += (n == o)
    print(f'ours {o:2d}  nissy {n:2d}  | {s}')
print(f'nissy drudfin optimal length == exact table: {agree}/{len(scrs)}')
