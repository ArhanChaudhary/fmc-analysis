#!/usr/bin/env python3
"""Counterexamples to FakeMMAP's T11503 lower bounds (alpha per path, C = the subset's shortest linear HTR, as in
bounding2.py): an optimal finish of a corner path whose shortest 1q reduction is R' while the bound says every finish
of that path needs more moves.  Checked as written (alpha_i in the sum) and with alpha_(i+1), the section windows i
and i+1 share.  Writes out/q9_t11503_examples.tsv (as-written violations) and out/checks/t11503_counts.txt."""
from bounding2 import by_subset, all_paths, alphas, LB_fake, C_LIN, NAMES
from common import *
AL = alphas(all_paths())
out = open(f'{OUT}/q9_t11503_examples.tsv', 'w')
out.write('subset\tidx\topt\tpath\tN\talpha\tA\tB\tC\tR_prime\tLB_T11503\tsections\n')
n = bad = bad_shared = 0
for sub, rows in by_subset():
    for r in rows:
        d = int(r['d']); A, Bv = int(r['htrN']), int(r['htrI'])
        for dl, p, r1, r2, sec in r['cells']:
            N = len(p.split('-')) - 1
            if dl != 0 or N < 2: continue
            n += 1
            if LB_fake(r1, N, AL[p], A, Bv, C_LIN[sub], True) > d: bad_shared += 1
            lb = LB_fake(r1, N, AL[p], A, Bv, C_LIN[sub])
            if lb > d:
                bad += 1
                out.write(f"{sub}\t{r['idx']}\t{d}\t{' > '.join(NAMES[int(i)] for i in p.split('-'))}\t{N}\t{','.join(map(str, AL[p]))}\t{A}\t{Bv}\t{C_LIN[sub]}\t{r1}\t{lb}\t{','.join(map(str, sec))}\n")
msg = f'cases {n} violations_as_written {bad} violations_alpha_i_plus_1 {bad_shared}\n'
open(f'{OUT}/checks/t11503_counts.txt', 'w').write(msg); print(msg, end='')
