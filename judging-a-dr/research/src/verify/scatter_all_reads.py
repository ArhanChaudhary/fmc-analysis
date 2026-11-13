#!/usr/bin/env python3
"""The sd left and the "under 1% for a 12" shares from the all-reads census (k6_all_reads_ordered.csv, drtools hcensus4),
with normal and inverse kept apart and merged, and with the feature sets of the older censuses (k5, k2) for comparison.

  python3 research/src/verify/scatter_all_reads.py > research/out/verify/scatter_all_reads.txt"""
import csv, collections, math
from fractions import Fraction as F
QT = {'0c0': 0, '4a1': 1, '4a2': 2, '4b2': 2, '0c3': 3, '2c3': 3, '4c3': 3, '0c4': 4, '2c4': 4, '4c4': 4, '2c5': 5, '4b5': 5}
GRP = {0: '0qt', 1: '1-2qt', 2: '1-2qt', 3: '3qt', 4: '4qt', 5: '5qt'}
R = []
with open('/data/fmc/judging-a-dr/research/out/hand/k6_all_reads_ordered.csv') as f:
    r = csv.reader(f); next(r)
    for x in r: R.append((x[0], x[1], x[2], int(x[3]), int(x[4]), int(x[5]), int(x[6]), int(x[7]), int(x[8])) + tuple(int(v) for v in x[9:]))
# idx: 0 sub,1 cn,2 ci,3 tp,4 hn,5 hi,6 L,7 dL,8 par,9 n,10 s,11 s2,12 le10,13 le11,14 le12
N = sum(r[9] for r in R); S = sum(r[10] for r in R); S2 = sum(r[11] for r in R)
assert N == 19508428800
var = F(S2, N) - F(S, N) ** 2
def sd(kf, rows=R):
    g = collections.defaultdict(lambda: [0, 0, 0])
    for r in rows:
        k = kf(r); g[k][0] += r[9]; g[k][1] += r[10]; g[k][2] += r[11]
    W = sum(F(s2) - F(s * s, n) for n, s, s2 in g.values())
    return len(g), 100 * (1 - float(W / N / var)), math.sqrt(W / N)
print('total sd %.4f' % math.sqrt(var))
for name, kf in [
    ('subset', lambda r: r[0]),
    ('k5-like unordered: sub, {cn,ci}, {hn,hi}', lambda r: (r[0], tuple(sorted((r[1], r[2]))), tuple(sorted((r[4], r[5]))))),
    ('ordered: sub, cn, ci, hn, hi', lambda r: (r[0], r[1], r[2], r[4], r[5])),
    ('ordered, no edge count: corner subset, cn, ci, hn, hi', lambda r: (r[0].split()[0], r[1], r[2], r[4], r[5])),
    ('Zagros literal: cn, ci, hn, hi (no subset at all)', lambda r: (r[1], r[2], r[4], r[5])),
    ('k5-like + pairs(cap5) unordered', lambda r: (r[0], tuple(sorted((r[1], r[2]))), min(r[3], 5), tuple(sorted((r[4], r[5]))))),
    ('ordered + pairs', lambda r: (r[0], r[1], r[2], r[3], r[4], r[5])),
    ('k2-like: sub, {h}, L, misfit, pairs(cap5)', lambda r: (r[0], tuple(sorted((r[4], r[5]))), r[6], r[7] > 0, min(r[3], 5))),
    ('everything ordered: sub, cn, ci, pairs, hn, hi, L, dLp, par', lambda r: r[:9]),
    ('everything unordered', lambda r: (r[0], tuple(sorted((r[1], r[2]))), r[3], tuple(sorted((r[4], r[5]))), r[6], r[7], r[8])),
    ('everything except HTR (no solving but L): sub, cn, ci, pairs', lambda r: (r[0], r[1], r[2], r[3])),
    ]:
    n, ex, s = sd(kf); print(f'{name}: classes {n}, explains {ex:.2f}%, sd left {s:.4f}')
GR = lambda s: GRP[QT[s.split()[0]]]
def dead(kf, g, col=14):
    cl = collections.defaultdict(lambda: [0, 0])
    for r in R:
        if GR(r[0]) != g: continue
        k = kf(r); cl[k][0] += r[col]; cl[k][1] += r[9]
    tot = sum(n for _, n in cl.values()); return 100 * sum(n for x, n in cl.values() if 100 * x <= n) / tot
for g in ('3qt', '4qt', '5qt'):
    print(g, 'dead for 12: everything ordered %.2f%%  unordered %.2f%%  k2-like %.2f%%' % (dead(lambda r: r[:9], g), dead(lambda r: (r[0], tuple(sorted((r[1], r[2]))), r[3], tuple(sorted((r[4], r[5]))), r[6], r[7], r[8]), g),
          dead(lambda r: (r[0], tuple(sorted((r[4], r[5]))), r[6], r[7] > 0, min(r[3], 5)), g)))
