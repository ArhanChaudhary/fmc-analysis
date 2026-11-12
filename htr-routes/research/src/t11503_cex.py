#!/usr/bin/env python3
"""Counterexamples to FakeMMAP's T11503 lower bounds (alpha per path, as in bounding2.py): an optimal finish of a
corner path whose shortest 1q reduction is R' while the bound says every finish of that path needs more moves.
Appends rows (version T11503) to out/q9_v2_counterexamples.tsv and writes out/q9_t11503_examples.tsv."""
import csv, subprocess
from bounding2 import load, alphas, LB_fake, C_LIN, NAMES
from common import *
B, paths = load(); AL = alphas(paths)
out = open(f'{OUT}/q9_t11503_examples.tsv', 'w')
out.write('subset\tidx\topt\tpath\tN\talpha\tA\tB\tC\tR_prime\tLB_T11503\tsections\n')
n = bad = 0
for sub in SUBS:
    for r in B[sub]:
        d = int(r['d']); A, Bv = int(r['htrN']), int(r['htrI'])
        for dl, p, r1, r2, sec in r['cells']:
            N = len(p.split('-')) - 1
            if dl != 0 or N < 2: continue
            n += 1
            lb = LB_fake(r1, N, AL[p], A, Bv, C_LIN[sub])
            if lb > d:
                bad += 1
                out.write(f"{sub}\t{r['idx']}\t{d}\t{' > '.join(NAMES[int(i)] for i in p.split('-'))}\t{N}\t{','.join(map(str, AL[p]))}\t{A}\t{Bv}\t{C_LIN[sub]}\t{r1}\t{lb}\t{','.join(map(str, sec))}\n")
print('cases', n, 'violations', bad)
