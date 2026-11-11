#!/usr/bin/env python3
"""Per corner subset: everything the per-subset guide in the write-up quotes."""
import csv, collections, sys
sys.path.insert(0, '/data/fmc/judging-a-dr/research/src')
from hand_kill import load
def S(h):
    n = sum(h); return (100*sum(h[:13])/n, 100*sum(h[:14])/n, sum(d*c for d, c in enumerate(h))/n, n)
def f(h): s = S(h); return f'{s[0]:.1f}/{s[1]:.0f}'
TOT = 19508428800
h3 = load('h3_leaveslice.csv')[1]; h5 = load('h5_pairs.csv')[1]; k1 = load('k1_corner_cases.csv')[1]; h2 = load('h2_lengths.csv')[1]
cc = {r[0]: r for r in load('corner_cases.csv')[1]}
POS_ADJ = {(0, 1), (1, 2), (2, 3), (0, 3)}
def layout(mask):
    bad = [p for p in range(8) if mask >> p & 1]; u = [p for p in bad if p < 4]; d = [p-4 for p in bad if p >= 4]
    sh = lambda x: 'adj' if tuple(sorted(x)) in POS_ADJ else 'diag'
    if not bad: return 'none'
    if len(bad) == 2:
        if len(u) == 1: return 'stacked' if u[0] == d[0] else ('across-face' if (min(u[0], d[0]), max(u[0], d[0])) in POS_ADJ else 'opposite')
        return 'same-layer-' + sh(u or d)
    if len(u) in (0, 4): return '4-0'
    if len(u) in (1, 3): return '3-1'
    return '2-2:' + ('stackedpairs' if set(u) == set(d) and sh(u) == 'adj' else 'oppositesides' if not set(u) & set(d) and sh(u) == sh(d) == 'adj' else 'onecolumn' if sh(u) == sh(d) == 'adj' else sh(u)+'/'+sh(d))
for cs in ['0c0', '4a1', '4a2', '4b2', '2c3', '4c3', '0c3', '2c4', '0c4', '4c4', '2c5', '4b5']:
    by_e = collections.defaultdict(lambda: [0]*19); allh = [0]*19
    for s, d, ls, c in h3:
        if s.split()[0] == cs: by_e[s.split()[1]][int(d)] += int(c); allh[int(d)] += int(c)
    print(f'\n=== {cs}: {100*sum(allh)/TOT:.2f}% of DRs, avg {S(allh)[2]:.2f}, in12/in13 {f(allh)}; min {min(d for d,c in enumerate(allh) if c)} max {max(d for d,c in enumerate(allh) if c)}')
    print('  by edges: ' + '  '.join(f'{e}: {100*sum(h)/sum(allh):.0f}% of it, {f(h)}, avg {S(h)[2]:.2f}' for e, h in sorted(by_e.items())))
    pp = collections.defaultdict(lambda: [0]*19)
    for r in h5:
        if r[0].split()[0] == cs: pp[min(int(r[1]), 5)][int(r[5])] += int(r[6])
    print('  pairs: ' + '  '.join(f'{k}{"+" if k==5 else ""}: {100*sum(h)/sum(allh):.0f}% {f(h)}' for k, h in sorted(pp.items())))
    one = collections.defaultdict(lambda: [0]*19); two = collections.defaultdict(lambda: [0]*19)
    for s, a, b, d, c in k1:
        if s.split()[0] == cs: one[a][int(d)] += int(c); two[tuple(sorted((a, b)))][int(d)] += int(c)
    lab = lambda k: f'{layout(int(cc[k][2]))}[L{cc[k][5]}-{cc[k][6]},qt->{cc[k][10] or "setup"}]'
    print('  corner cases: ' + ' | '.join(f'{lab(k)} {100*sum(h)/sum(allh):.0f}% {f(h)}' for k, h in sorted(one.items(), key=lambda kv: S(kv[1])[2])))
    t = sorted(two.items(), key=lambda kv: S(kv[1])[2])
    if len(t) > 1: print(f'  both sides best: {lab(t[0][0][0])}+{lab(t[0][0][1])} {100*sum(t[0][1])/sum(allh):.1f}% {f(t[0][1])};  worst: {lab(t[-1][0][0])}+{lab(t[-1][0][1])} {100*sum(t[-1][1])/sum(allh):.1f}% {f(t[-1][1])}')
    hh = collections.defaultdict(lambda: [0]*19); hx = collections.defaultdict(lambda: [0]*19)
    for r in h2:
        if r[0].split()[0] == cs: hh[(int(r[1]), int(r[2]))][int(r[6])] += int(r[7]); hx[int(r[2])][int(r[6])] += int(r[7])
    print('  longer HTR: ' + '  '.join(f'{k}: {100*sum(h)/sum(allh):.0f}% {f(h)}' for k, h in sorted(hx.items()) if sum(h)/sum(allh) > 0.005))
    big = [(k, h) for k, h in hh.items() if sum(h)/sum(allh) >= 0.02]
    print('  HTR both (cells >=2%): ' + '  '.join(f'{k[0]}/{k[1]}: {100*sum(h)/sum(allh):.0f}% {f(h)}' for k, h in sorted(big)))
