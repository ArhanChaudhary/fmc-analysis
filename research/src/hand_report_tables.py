#!/usr/bin/env python3
"""Markdown tables for the report: odds by true pairs, square HTR tables, per-subset extremes, HTR floor per qt."""
import csv, collections, math, sys
sys.path.insert(0, '/data/fmc/research/src')
from hand_kill import load, QT
OUT = '/data/fmc/report/data/'
def st(h):
    n = sum(h); return n, sum(d*c for d, c in enumerate(h))/n
def P(h, T): return 100*sum(h[:T+1])/sum(h)
order = lambda s: (int(s.split()[0][-1]), s.split()[0], int(s.split()[1][0]))
# --- pairs
h5 = [(r[0], int(r[1]), int(r[5]), int(r[6])) for r in load('h5_pairs.csv')[1]]
subs = sorted({r[0] for r in h5}, key=order)
g = collections.defaultdict(lambda: collections.defaultdict(lambda: [0]*19))
gc = collections.defaultdict(lambda: collections.defaultdict(lambda: [0]*19))
for s, tp, d, c in h5:
    g[s][min(tp, 6)][d] += c; gc[s.split()[0]][min(tp, 6)][d] += c
L = ['| Subset | 0 pairs | 1 | 2 | 3 | 4 | 5 | 6+ |', '|---|---:|---:|---:|---:|---:|---:|---:|']
tot = collections.Counter()
for s in subs:
    L.append(f'| {s} | ' + ' | '.join(f'{P(g[s][k],12):.1f} / {P(g[s][k],13):.0f}' if sum(g[s][k]) else '' for k in range(7)) + ' |')
    for k in range(7): tot[k] += sum(g[s][k])
L.append('| share of DRs | ' + ' | '.join(f'{100*tot[k]/sum(tot.values()):.1f}%' for k in range(7)) + ' |')
open(OUT + 'odds_by_true_pairs.md', 'w').write('\n'.join(L) + '\n')
print('pairs share:', {k: round(100*tot[k]/sum(tot.values()), 1) for k in range(7)})
# --- square tables
h2 = [(r[0], int(r[1]), int(r[2]), int(r[6]), int(r[7])) for r in load('h2_lengths.csv')[1]]
sq = collections.defaultdict(lambda: collections.defaultdict(lambda: [0]*19))
for s, a, b, d, c in h2: sq[s][(a, b)][d] += c
L = []
dead = []
for s in subs:
    tot = sum(sum(h) for h in sq[s].values())
    hs = sorted({k[1] for k in sq[s]}); lo = sorted({k[0] for k in sq[s]})
    L.append(f'\n**{s}**\n\n| shorter \\ longer | ' + ' | '.join(str(h) for h in hs) + ' |\n|---|' + '---:|'*len(hs))
    for a in lo:
        cells = []
        for b in hs:
            h = sq[s].get((a, b))
            if h and sum(h):
                cells.append(f'{100*sum(h)/tot:.1f}% · {st(h)[1]:.2f} · {P(h,12):.1f} · {P(h,13):.0f}')
                if P(h, 12) < 1 and 100*sum(h)/tot >= 0.5: dead.append((s, a, b, 100*sum(h)/tot, P(h, 12), P(h, 13), min(d for d, c in enumerate(h) if c)))
            else: cells.append('')
        L.append(f'| {a} | ' + ' | '.join(cells) + ' |')
open(OUT + 'htr_square_tables.md', 'w').write('\n'.join(L) + '\n')
print('cells (>=0.5% of subset) where under 1% finish in <=12:')
for x in dead: print(f'   {x[0]} HTR {x[1]}/{x[2]}: {x[3]:.1f}% of the subset, <=12 {x[4]:.2f}%, <=13 {x[5]:.1f}%, min {x[6]}')
# --- per subset min / max / HTR floor
h3 = [(r[0], int(r[1]), int(r[3])) for r in load('h3_leaveslice.csv')[1]]
ext = collections.defaultdict(lambda: [0]*19)
for s, d, c in h3: ext[s][d] += c
print('max optimal per subset:', '  '.join(f'{s} {max(d for d, c in enumerate(ext[s]) if c)}' for s in subs))
cos = load('cosets.csv')[1]
fl = collections.defaultdict(lambda: [99, 0]); flq = collections.defaultdict(lambda: 99)
for r in cos:
    q = int(r[5]); h = int(r[7]); flq[q] = min(flq[q], h)
print('shortest HTR of any case by corner qt (Joba assumed 2/1/2/4/6/8 with NISS):', dict(sorted(flq.items())))
