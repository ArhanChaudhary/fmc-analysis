#!/usr/bin/env python3
"""Question B from the exact EO tables and the EO sample.

inputs  out/eo_axis.tsv     (eodrtools eo axis: each of the 2048 EO states of one axis, optimal EO, EO counts)
        out/eo_layouts.tsv  (eodrtools eo layouts: bad-edge triples over all edge states)
        out/eo_sample.tsv   (eodrtools eo sample: optimal EO per axis and over all axes, random states)
outputs out/b4_one_axis_exact.tsv, out/b5_layouts.tsv, out/b5_sorted.tsv, out/b5_by_bad.tsv, out/b_stats.json"""
import csv, json, os, collections, itertools
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, '..', 'out')

def rd(name):
    return list(csv.DictReader((l for l in open(os.path.join(OUT, name)) if not l.startswith('#')), delimiter='\t'))

def write(name, rows):
    keys = list(rows[0].keys())
    with open(os.path.join(OUT, name), 'w') as f:
        f.write('\t'.join(keys) + '\n')
        for r in rows:
            f.write('\t'.join(str(r[k]) for k in keys) + '\n')

stats = {}
# ---------------- one axis, linear: exact over 2048 states
ax = rd('eo_axis.tsv')
L = 9
assert len(ax) == 2048
opt = collections.Counter(int(r['optimal']) for r in ax)
stats['one_axis_optimal_hist'] = {str(k): opt[k] for k in sorted(opt)}
stats['one_axis_optimal_mean'] = str(Fraction(sum(k * v for k, v in opt.items()), 2048)) + f" = {sum(k * v for k, v in opt.items()) / 2048:.5f}"
rows = []
for l in range(L):
    v = [int(r[f'n{l}']) for r in ax]
    cum = [sum(int(r[f'n{j}']) for j in range(l + 1)) for r in ax]
    rows.append({'length': l, 'mean': round(sum(v) / 2048, 4), 'p_at_least_one': round(sum(x > 0 for x in v) / 2048, 5), 'max': max(v),
                 'mean_le': round(sum(cum) / 2048, 4), 'p_none_le': round(sum(x == 0 for x in cum) / 2048, 5), 'max_le': max(cum),
                 'median_le': sorted(cum)[1023]})
write('b4_one_axis_exact.tsv', rows)
# by bad-edge count: chance of a linear EO of at most k turns, and the optimal EO
byb = []
for b in range(0, 13, 2):
    grp = [r for r in ax if int(r['bad']) == b]
    row = {'bad': b, 'states': len(grp), 'p_state': f'{len(grp)}/2048'}
    for k in range(8):
        row[f'p_linear_le{k}'] = round(sum(int(r['optimal']) <= k for r in grp) / len(grp), 5)
    row['optimal_hist'] = ' '.join(f'{k}:{v}' for k, v in sorted(collections.Counter(int(r['optimal']) for r in grp).items()))
    byb.append(row)
# NISS by bad count (sampled): per axis pooled
sm = rd('eo_sample.tsv')
per = collections.defaultdict(collections.Counter)
anyax = collections.Counter()
for r in sm:
    if r['what'] == 'axis':
        per[int(r['bad'])][(int(r['linear']), int(r['inverse']), int(r['niss']))] += int(r['count'])
    else:
        anyax[(int(r['linear']), int(r['inverse']), int(r['niss']))] += int(r['count'])
nsamp = sum(anyax.values())
stats['sample_states'] = nsamp
for row in byb:
    c = per[row['bad']]
    t = sum(c.values())
    row['sampled_axes'] = t
    for k in (3, 4, 5):
        row[f'p_linear_le{k}_sampled'] = round(sum(v for (l, i, x), v in c.items() if l <= k) / t, 5) if t else ''
        row[f'p_lin_or_inv_le{k}'] = round(sum(v for (l, i, x), v in c.items() if min(l, i) <= k) / t, 5) if t else ''
        row[f'p_niss_le{k}'] = round(sum(v for (l, i, x), v in c.items() if x <= k) / t, 5) if t else ''
write('b5_by_bad.tsv', byb)
# any axis
def hist(f):
    h = collections.Counter()
    for k, v in anyax.items():
        h[f(k)] += v
    return h
for name, f in (('linear', lambda k: k[0]), ('lin_or_inv', lambda k: k[1]), ('niss', lambda k: k[2])):
    h = hist(f)
    stats[f'any_axis_{name}'] = {'hist': {str(k): h[k] for k in sorted(h)}, 'mean': round(sum(k * v for k, v in h.items()) / nsamp, 5),
                                 'p_le3': round(sum(v for k, v in h.items() if k <= 3) / nsamp, 5),
                                 'p_le2': round(sum(v for k, v in h.items() if k <= 2) / nsamp, 5)}
# per-axis optimal NISS EO (pooled over axes)
hx = collections.Counter()
for b, c in per.items():
    for (l, i, x), v in c.items():
        hx[x] += v
t = sum(hx.values())
stats['one_axis_niss'] = {'hist': {str(k): hx[k] for k in sorted(hx)}, 'mean': round(sum(k * v for k, v in hx.items()) / t, 5)}
# ---------------- bad-edge layouts: exact
lay = rd('eo_layouts.tsv')
tot = sum(int(r['states']) for r in lay)
assert tot == 34650 * 2048
perm = 24 ** 3  # each arrangement x flip pattern stands for 4!^3 permutations
rows = []
for r in lay:
    n = int(r['states'])
    rows.append({'bad_fb': r['bad_fb'], 'bad_rl': r['bad_rl'], 'bad_ud': r['bad_ud'], 'states_over_4!^3': n,
                 'probability': f'{Fraction(n, tot)}', 'p': round(n / tot, 8)})
write('b5_layouts.tsv', rows)
srt = collections.Counter()
for r in lay:
    srt[tuple(sorted((int(r['bad_fb']), int(r['bad_rl']), int(r['bad_ud']))))] += int(r['states'])
write('b5_sorted.tsv', [{'sorted_triple': '/'.join(map(str, k)), 'states_over_4!^3': v, 'probability': str(Fraction(v, tot)), 'p': round(v / tot, 8)}
                         for k, v in sorted(srt.items(), key=lambda kv: -kv[1])])
P = lambda pred: Fraction(sum(int(r['states']) for r in lay if pred(int(r['bad_fb']), int(r['bad_rl']), int(r['bad_ud']))), tot)
fl = lambda f: f'{f} = {float(f):.6%}'
stats['layouts'] = {
    'total_arrangement_flip_states': tot,
    'p_all_bad_all_axes_12_12_12': fl(P(lambda a, b, c: a == b == c == 12)),
    'p_some_axis_eo_solved': fl(P(lambda a, b, c: 0 in (a, b, c))),
    'states_some_axis_eo_solved': sum(int(r['states']) for r in lay if '0' in (r['bad_fb'], r['bad_rl'], r['bad_ud'])),
    'p_all_axes_in_0_2_4_8': fl(P(lambda a, b, c: all(x in (0, 2, 4, 8) for x in (a, b, c)))),
    'max_difference_between_two_axes': max(max(abs(int(r['bad_fb']) - int(r['bad_rl'])), abs(int(r['bad_fb']) - int(r['bad_ud'])), abs(int(r['bad_rl']) - int(r['bad_ud']))) for r in lay),
    'min_other_axes_given_12_on_fb': min(min(int(r['bad_rl']), int(r['bad_ud'])) for r in lay if r['bad_fb'] == '12'),
    'other_axes_range_given_0_on_fb': sorted({int(r['bad_rl']) for r in lay if r['bad_fb'] == '0'} | {int(r['bad_ud']) for r in lay if r['bad_fb'] == '0'}),
    'mean_bad_per_axis': str(Fraction(sum(int(r['bad_fb']) * int(r['states']) for r in lay), tot)),
}
sums = collections.Counter()
for r in lay:
    sums[int(r['bad_fb']) + int(r['bad_rl']) + int(r['bad_ud'])] += int(r['states'])
stats['layouts']['sum_distribution_p'] = {str(k): round(v / tot, 6) for k, v in sorted(sums.items())}
for t3 in ((6, 6, 4), (6, 6, 6), (6, 6, 8), (0, 0, 2), (0, 0, 8), (2, 10, 10), (10, 10, 10), (12, 12, 12)):
    stats['layouts'][f'sorted_{t3[0]}/{t3[1]}/{t3[2]}'] = fl(Fraction(srt[tuple(sorted(t3))], tot))
for t3 in ((6, 6, 4), (6, 6, 6)):
    stats['layouts'][f'ordered_{t3[0]}/{t3[1]}/{t3[2]}'] = fl(P(lambda a, b, c, t3=t3: (a, b, c) == t3))
json.dump(stats, open(os.path.join(OUT, 'b_stats.json'), 'w'), indent=1)
print('B tables written')
