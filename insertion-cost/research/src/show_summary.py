#!/usr/bin/env python3
"""Print the rows of out/summary.tsv for one skeleton length (default 20) as a compact table."""
import sys
OUT = '/data/fmc/insertion-cost/research/out'
n = sys.argv[1] if len(sys.argv) > 1 else '20'
src = sys.argv[2] if len(sys.argv) > 2 else 'summary.tsv'
rows = [l.rstrip('\n').split('\t') for l in open(f'{OUT}/{src}')]
head = rows[0]; ix = {h: i for i, h in enumerate(head)}
order = ['3c', '2tc', '3tc', '2c2c-pure', '2c2c-twisted', '3c1t', '5c', '3c3c', '3e', '2f', '2e2e', '2e2e-flipped', '5e', '3e1f', '3e3e']
print('type\tmodel\tL\tskeletons\tunsolved\tmean\t<=2\t<=3\t<=4\t<=5\t<=6\t<=7\t<=8\t<=9\t<=10\t<=11\t<=12\tbest=two\tneeds nesting')
for t in order:
    for r in rows[1:]:
        if r[ix['type']] == t and r[ix['n']] == n:
            sh = [f"{100 * float(x):.1f}" for x in r[7:18]]
            print('\t'.join([t, r[2], r[3], r[4], r[5], f"{float(r[6]):.2f}"] + sh + r[18:20]))
