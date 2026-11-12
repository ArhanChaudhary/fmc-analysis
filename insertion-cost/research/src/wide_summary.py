#!/usr/bin/env python3
"""One line per (type, L) for one n: mean cost (and how many skeletons have no solution / how many were computed) per model."""
import sys
OUT = '/data/fmc/insertion-cost/research/out'
n = sys.argv[1] if len(sys.argv) > 1 else '20'
src = sys.argv[2] if len(sys.argv) > 2 else 'summary.tsv'
rows = [l.rstrip('\n').split('\t') for l in open(f'{OUT}/{src}')]
ix = {h: i for i, h in enumerate(rows[0])}
d = {(r[0], r[1], r[2], r[3]): r for r in rows[1:]}
order = ['3c', '2tc', '3tc', '2c2c-pure', '2c2c-twisted', '3c1t', '5c', '3c3c', '3e', '2f', '2e2e', '2e2e-flipped', '5e', '3e1f', '3e3e']
models = [m for m in ['direct', 'two', 'two_flat', 'two_apart', 'mixed', 'best'] if any(k[2] == m for k in d)]
def cell(t, L, m):
    r = d.get((t, n, m, L))
    if not r: return '-'
    k, uns, mean = int(r[4]), int(r[5]), r[6]
    if uns == k: return f'none ({k})'
    return f'{float(mean):.2f} ({uns}/{k})' if uns else f'{float(mean):.2f} ({k})'
print('\t'.join(['type', 'L'] + [f'{m}: mean (unsolved/skeletons)' for m in models] + ['best: % <=6', '% <=8', '% <=10', 'best is two', 'needs nesting']))
for t in order:
    for L in sorted({k[3] for k in d}, key=int):
        if not any((t, n, m, L) in d for m in models): continue
        b = d.get((t, n, 'best', L))
        extra = [f'{100*float(b[ix["share_le6"]]):.1f}', f'{100*float(b[ix["share_le8"]]):.1f}', f'{100*float(b[ix["share_le10"]]):.1f}', b[ix['best_is_two']], b[ix['best_needs_nesting']]] if b else ['-'] * 5
        print('\t'.join([t, L] + [cell(t, L, m) for m in models] + extra))
