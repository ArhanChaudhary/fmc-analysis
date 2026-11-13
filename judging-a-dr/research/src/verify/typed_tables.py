#!/usr/bin/env python3
"""Independent recount of the tables of the write-up body that used to be typed by hand: the other-parity cost of a
corner solution, Levi's formula against the optimal and the leave slice, setup + HTR, and the width of a DR.

  python3 research/src/verify/typed_tables.py > research/out/verify/typed_tables.txt"""
import csv, collections
from fractions import Fraction as F
H = '/data/fmc/judging-a-dr/research/out/hand/'
def rows(n):
    with open(H + n) as f:
        r = csv.reader(f); next(r); return [x for x in r]
QT = {'0c0': 0, '4a1': 1, '4a2': 2, '4b2': 2, '0c3': 3, '2c3': 3, '4c3': 3, '0c4': 4, '2c4': 4, '4c4': 4, '2c5': 5, '4b5': 5}
G = lambda s: {0: '0qt', 1: '1-2qt', 2: '1-2qt', 3: '3qt', 4: '4qt', 5: '5qt'}[QT[s.split()[0]]]
h2 = [(r[0], int(r[1]), int(r[2]), int(r[3]), int(r[4]), int(r[5]), int(r[6]), int(r[7])) for r in rows('h2_lengths.csv')]
print('== other parity cost per corner subset: share of corner states with |L_even - L_odd| = k  (2 x share of DR states with dLp = k)')
for cs in ['4a2', '0c3', '0c4', '4c3', '4c4', '2c4', '2c5', '4b5', '4b2', '2c3', '4a1', '0c0']:
    A = [r for r in h2 if r[0].split()[0] == cs]; N = sum(r[7] for r in A); c = collections.Counter()
    for r in A: c[r[4]] += r[7]
    d = {k: 200 * v / N for k, v in c.items() if k > 0}; same = 100 - sum(d.values())
    print(f'  {cs}: same {same:.2f}%  ' + '  '.join(f'+{k}: {v:.2f}%' for k, v in sorted(d.items())))
print('== Levi formula on 4a1 4e (optimal minus hmin+hmax-1)')
A = [r for r in h2 if r[0] == '4a1 4e']; N = sum(r[7] for r in A); c = collections.Counter()
for r in A: c[r[6] - (r[1] + r[2] - 1)] += r[7]
print('  states', N, ' below %.3f%%  by1 %.3f%% by2 %.3f%% by3+ %.3f%% equal %.3f%% above %.3f%%' % (
    100 * sum(v for k, v in c.items() if k < 0) / N, 100 * c[-1] / N, 100 * c[-2] / N, 100 * sum(v for k, v in c.items() if k <= -3) / N, 100 * c[0] / N, 100 * sum(v for k, v in c.items() if k > 0) / N))
for T in (11, 12, 13):
    B = [r for r in A if r[1] + r[2] - 1 <= T]; n = sum(r[7] for r in B)
    print(f'  formula <= {T}: {100*n/N:.2f}% of subset; below formula in {100*sum(r[7] for r in B if r[6] < r[1]+r[2]-1)/n:.3f}%')
for s in ('4a1 2e', '4a1 0e'):
    B = [r for r in h2 if r[0] == s]; n = sum(r[7] for r in B); print(f'  {s}: below {100*sum(r[7] for r in B if r[6] < r[1]+r[2]-1)/n:.2f}%')
print('== leave slice minus formula, 4a1 4e (h4)')
h4 = [(r[0], int(r[1]), int(r[2]), int(r[3]), int(r[4])) for r in rows('h4_htr_leaveslice.csv') if r[0] == '4a1 4e']
N = sum(r[4] for r in h4); c = collections.Counter()
for r in h4: c[max(-3, min(4, r[3] - (r[1] + r[2] - 1)))] += r[4]
print('  ' + '  '.join(f'{k:+d}: {100*v/N:.2f}%' for k, v in sorted(c.items())))
print('== setup + HTR bound (h7): optimal minus bound')
h7 = [(r[0], int(r[1]), int(r[2]), int(r[3]), int(r[4])) for r in rows('h7_setup_bound.csv')]
for g in ('1-2qt', '3qt', '4qt', '5qt'):
    A = [r for r in h7 if G(r[0]) == g]; N = sum(r[4] for r in A); c = collections.Counter()
    for r in A: c['beaten' if r[3] < r[2] else min(r[3] - r[2], 3)] += r[4]
    print(f'  {g}: ' + '  '.join(f'{k}: {100*c[k]/N:.4f}%' for k in ('beaten', 0, 1, 2, 3)) + f'   mean bound {sum(r[2]*r[4] for r in A)/N:.3f} mean hmax {sum(r[1]*r[4] for r in A)/N:.3f} mean opt {sum(r[3]*r[4] for r in A)/N:.3f}')
sub = collections.defaultdict(lambda: [0, 0])
for r in h7:
    sub[r[0]][0] += r[4]
    if r[3] < r[2]: sub[r[0]][1] += r[4]
print('  beaten by subset: ' + ', '.join(f'{s} {100*b/n:.3f}%' for s, (n, b) in sorted(sub.items(), key=lambda t: -t[1][1] / t[1][0]) if b))
print('== width (h10): optimal first moves by depth')
h10 = [(r[0], int(r[1]), int(r[2]), int(r[3]), int(r[4])) for r in rows('h10_first_moves.csv')]
for d in range(10, 17):
    A = [r for r in h10 if r[1] == d]; N = sum(r[4] for r in A)
    print(f'  {d}: avg {sum(r[2]*r[4] for r in A)/N:.3f}  exactly one {100*sum(r[4] for r in A if r[2] == 1)/N:.3f}%')
for q_ in (2, 5):
    A = [r for r in h10 if QT[r[0].split()[0]] == q_ and r[1] > 0]; N = sum(r[4] for r in A); print(f'  {q_}qt avg optimal first moves {sum(r[2]*r[4] for r in A)/N:.3f}')
