"""Baseline for the text structure: longest one-axis DR-move run in random-move sequences (canonical: no face twice
in a row, opposite faces not in both orders), 19 moves, 100,000 samples, seed 1."""
import random, collections, textfeat as tf, cube
rnd = random.Random(1)
F = 'URFDLB'; OPPO = {'U': 'D', 'D': 'U', 'R': 'L', 'L': 'R', 'F': 'B', 'B': 'F'}; ORD = {f: i for i, f in enumerate('UDRLFB')}
c = collections.Counter(); N = 100000
for _ in range(N):
    s = []
    while len(s) < 19:
        f = rnd.choice(F)
        if s and (s[-1][0] == f or (OPPO[f] == s[-1][0] and ORD[f] < ORD[s[-1][0]])): continue
        s.append(f + rnd.choice(['', '2', "'"]))
    c[max(tf.runs(s, a)[1] for a in cube.AXES)] += 1
print('random-move 19-move sequences: longest DR-move run:', {k: f'{100*v/N:.2f}%' for k, v in sorted(c.items())})
