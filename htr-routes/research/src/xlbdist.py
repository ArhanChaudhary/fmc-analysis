#!/usr/bin/env python3
"""What FakeMMAP asked of the multi-qt lower bounds (T11504): their typical value.  For every sampled state and every
corner path of its optimal finishes (N >= 2 quarter turns), with R' = the shortest 1q reduction a finish of that path
needs (so every shorter reduction has failed), the T11503 lower bound on M with alpha_(i+1) in the sum (the corrected
form; as written it uses alpha_i), next to the trivial bound max(A + alpha_N, B + alpha_0) and the optimum.
Streams out/big/bound2.tsv one row at a time.  Output: out/q9_lb_values.tsv (corner subset, statistic, value)."""
import csv, collections, math, statistics
from common import R, OUT, SUBS, SIZE, CORNER, CGROUPS
from bounding import covering_sets
import bounding2 as b2

def esum(S, al, shared):
    return sum((al[i + 1] if shared else al[i]) for i in S if i + 1 in S)

def LB(Rp, N, al, A, B, C, shared=True):
    v = []
    for S in b2.cov(0, N - 1):
        if len(S) > 1: v.append((len(S) * (Rp + 1) - N + esum(S, al, shared)) / (len(S) - 1))
    for S in b2.cov(0, N - 2): v.append(1 + Rp + (A - N + esum(S, al, shared)) / len(S))
    for S in b2.cov(1, N - 1): v.append(1 + Rp + (B - N + esum(S, al, shared)) / len(S))
    if N > 2:
        for S in b2.cov(1, N - 2): v.append(1 + Rp + (C - N + esum(S, al, shared)) / len(S))
    return math.ceil(max(v) - 1e-9) if v else 0

paths = set(); rows_by = collections.defaultdict(list)
acc = collections.defaultdict(lambda: collections.defaultdict(list))
first = True
AL = None
for r in csv.DictReader(open(f'{R}/out/big/bound2.tsv'), delimiter='\t'):
    for c in (r['cells'].split(';') if r['cells'] else []):
        paths.add(c.split(':')[1])
AL = b2.alphas(paths)
for r in csv.DictReader(open(f'{R}/out/big/bound2.tsv'), delimiter='\t'):
    d = int(r['d']); A, B, C = int(r['htrN']), int(r['htrI']), int(r['niss'])
    need = {}
    for c in (r['cells'].split(';') if r['cells'] else []):
        dl, p, r1, r2, sec = c.split(':')
        if int(dl) == 0 and (p not in need or int(r1) < need[p]): need[p] = int(r1)
    g = CORNER(r['subset']); w = SIZE[r['subset']]
    for p, rp in need.items():
        N = len(p.split('-')) - 1
        if N < 2: continue
        al = AL[p]
        lb = LB(rp, N, al, A, B, C, True)
        triv = max(A + al[N], B + al[0])
        for key in (g, 'all'):
            acc[key]['lb'].append(lb); acc[key]['triv'].append(triv); acc[key]['opt'].append(d)
            acc[key]['beats'].append(lb > triv); acc[key]['reach'].append(lb >= d); acc[key]['ge11'].append(lb >= 11)
with open(f'{OUT}/q9_lb_values.tsv', 'w') as f:
    f.write('group\tcases\tmedian_lb\tmean_lb\tmedian_trivial\tmean_trivial\tmean_opt\tlb_beats_trivial\tlb_reaches_opt\tlb_ge_11\n')
    for g in CGROUPS + ['all']:
        a = acc[g]
        if not a['lb']: continue
        f.write(f"{g}\t{len(a['lb'])}\t{statistics.median(a['lb'])}\t{statistics.mean(a['lb']):.2f}\t{statistics.median(a['triv'])}\t"
                f"{statistics.mean(a['triv']):.2f}\t{statistics.mean(a['opt']):.2f}\t{statistics.mean(a['beats']):.4f}\t{statistics.mean(a['reach']):.4f}\t{statistics.mean(a['ge11']):.4f}\n")
print(open(f'{OUT}/q9_lb_values.tsv').read())
