#!/usr/bin/env python3
"""Second census: combined reads, corner cases on both sides, pairs on both sides, edge-only length."""
import csv, collections, math, sys
sys.path.insert(0, '/data/fmc/research/src')
from hand_kill import load, table, QT, power
from hand_gain import gain
def st(h):
    n = sum(h); m = sum(d*c for d, c in enumerate(h))/n
    return n, m, math.sqrt(max(sum(d*d*c for d, c in enumerate(h))/n - m*m, 0))
def P(h, T): return 100*sum(h[:T+1])/sum(h)
k2 = load('k2_combined.csv')[1]   # subset,hmin,hmax,L,parity_misfit,true_pairs,depth,count
dep = lambda r: int(r[6]); cnt = lambda r: int(r[7]); sub = lambda r: r[0]
feats = [('subset only', table(k2, sub, lambda r: 0, dep, cnt)),
         ('true pairs', table(k2, sub, lambda r: r[5], dep, cnt)),
         ('pairs + L', table(k2, sub, lambda r: (r[5], r[3]), dep, cnt)),
         ('pairs + L + parity', table(k2, sub, lambda r: (r[5], r[3], r[4]), dep, cnt)),
         ('pairs + longer HTR', table(k2, sub, lambda r: (r[5], r[2]), dep, cnt)),
         ('pairs + HTR both', table(k2, sub, lambda r: (r[5], r[1], r[2]), dep, cnt)),
         ('HTR both + L + parity', table(k2, sub, lambda r: (r[1], r[2], r[3], r[4]), dep, cnt)),
         ('all: pairs, HTR both, L, parity', table(k2, sub, lambda r: tuple(r[1:6]), dep, cnt))]
k3 = load('k3_pairs_both_sides.csv')[1]
feats.append(('true pairs, both sides', table(k3, sub, lambda r: (r[1], r[2]), lambda r: int(r[3]), lambda r: int(r[4]))))
k4 = load('k4_edge_length.csv')[1]
feats.append(('L + edge length', table(k4, sub, lambda r: (r[1], r[2]), lambda r: int(r[3]), lambda r: int(r[4]))))
feats.append(('edge length', table(k4, sub, lambda r: r[2], lambda r: int(r[3]), lambda r: int(r[4]))))
k1 = load('k1_corner_cases.csv')[1]
feats.append(('corner case, normal', table(k1, sub, lambda r: r[1], lambda r: int(r[3]), lambda r: int(r[4]))))
feats.append(('corner case, both sides', table(k1, sub, lambda r: (r[1], r[2]), lambda r: int(r[3]), lambda r: int(r[4]))))
print('keep the best-looking 10% / 25% / 50%: share of the finishes <= 12 kept | sd left | dead% (<=1% reach 12) per group')
for name, g in feats:
    cells = []
    for q in ('3qt', '4qt', '5qt', 'all'):
        base, out = gain(g, 12, (lambda s: True) if q == 'all' else (lambda s, q=q: QT[s.split()[0]] == q))
        cells.append(' '.join(f'{100*x:3.0f}' for x in out))
    N = W = 0
    for classes in g.values():
        for h in classes.values():
            n, m, sd = st(h); N += n; W += sd*sd*n
    pw = power(g, 12, lambda s: QT[s.split()[0]])
    print(f'{name:32s} | ' + ' | '.join(cells) + f' | sd left {math.sqrt(W/N):.3f} | dead: 4qt {100*pw["4qt"][2]/pw["4qt"][0]:.0f}% 5qt {100*pw["5qt"][2]/pw["5qt"][0]:.0f}%')

print('\ncorner cases inside a corner subset: mean optimal and P(<=12) by corner case (normal side), all edge counts together')
cc = {r[0]: r for r in load('corner_cases.csv')[1]}
g = collections.defaultdict(lambda: collections.defaultdict(lambda: [0]*19))
gb = collections.defaultdict(lambda: collections.defaultdict(lambda: [0]*19))
for r in k1:
    cs = r[0].split()[0]
    g[cs][r[1]][int(r[3])] += int(r[4]); gb[cs][tuple(sorted((r[1], r[2])))][int(r[3])] += int(r[4])
for cs in ['4b2', '2c3', '4c3', '2c4', '4c4', '2c5', '4b5']:
    tot = sum(sum(h) for h in g[cs].values())
    items = sorted(g[cs].items(), key=lambda kv: st(kv[1])[1])
    print(f'  {cs}: ' + ' | '.join(f'#{k}[{cc[k][1]} m{cc[k][2]} L{cc[k][5]}-{cc[k][6]}] {100*sum(h)/tot:.0f}% {st(h)[1]:.2f} {P(h,12):.1f}%' for k, h in items))
    items = sorted(gb[cs].items(), key=lambda kv: st(kv[1])[1])
    print(f'     both sides, best 3: ' + ' | '.join(f'#{k[0]}+#{k[1]} {100*sum(h)/tot:.1f}% {st(h)[1]:.2f} {P(h,12):.1f}%' for k, h in items[:3]) + '   worst 3: ' + ' | '.join(f'#{k[0]}+#{k[1]} {100*sum(h)/tot:.1f}% {st(h)[1]:.2f} {P(h,12):.1f}%' for k, h in items[-3:]))
