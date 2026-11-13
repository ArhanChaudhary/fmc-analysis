#!/usr/bin/env python3
"""Markdown tables for the report, every one with the same targets (in 10 / 11 / 12 / 13).

  appendix_a.md            the 48 subsets: share, average, fastest, longest, odds for 9..13; and what is proven
  appendix_b.md            odds by corner length and E-slice parity, the big 3-5qt subsets
  odds_by_true_pairs.md    odds by number of true pairs, all 48 subsets, one table per target
  htr_square_tables.md     odds by the two HTR lengths, all 48 subsets
  main_pairs.md            section "Pairs": the big corner subsets
  main_squares.md          section "HTR length on both sides": the four big high-qt subsets
  main_zagros.md           Zagros's 4c3 rule"""
import collections, csv, sys
sys.path.insert(0, '/data/fmc/judging-a-dr/research/src')
import pv
OUT = '/data/fmc/judging-a-dr/report/data/'
def write(name, lines):
    open(OUT + name, 'w').write('\n'.join(lines) + '\n'); print(f'{name}: {len(lines)} lines')

h3 = collections.defaultdict(lambda: [0] * 19)
for s, d, ls, c in pv.rows('h3_leaveslice.csv'): h3[s][int(d)] += int(c)
subs = sorted(h3, key=pv.sub_order)
assert len(subs) == 48 and sum(sum(h) for h in h3.values()) == pv.TOT

# ---- Appendix A
L = ['| Subset | Share of all DRs | Average optimal, moves | Fastest, moves | Longest, moves |', '|---|---:|---:|---:|---:|']
for s in subs:
    h = h3[s]
    L.append(f'| {s} | {100*sum(h)/pv.TOT:.2f}% | {pv.avg(h):.2f} | {pv.fastest(h)} | {max(d for d, c in enumerate(h) if c)} |')
L += ['', 'The same subsets, with the share of each that finishes in 9, 10, 11, 12 and 13 or less:', '', '| Subset | In 9 | In 10 | In 11 | In 12 | In 13 |', '|---|---:|---:|---:|---:|---:|']
for s in subs:
    L.append(f'| {s} | ' + pv.cells(h3[s], pv.WIDE) + ' |')
lat = collections.defaultdict(collections.Counter)
with open('/data/fmc/judging-a-dr/research/out/lattice.csv') as f:
    for r in csv.DictReader(f):
        if r['sides'] == '2' and r['spec'] in ('KF', 'c+2520+F'): lat[(r['spec'], r['subset'])][int(r['bound'])] += int(r['count'])
hand = collections.defaultdict(collections.Counter)
for s, lo, hi, l, dlp, par, d, c in pv.rows('h2_lengths.csv'): hand[s][max(int(hi), int(l) + int(dlp))] += int(c)
def pr(c, T): return pv.num(100 * sum(n for b, n in c.items() if b > T) / sum(c.values()))
for i, T in enumerate((10, 11, 12)):
    L += ['', (('What is proven, per subset. "Hand" is the better of the two guaranteed hand bounds (longer HTR, corner length with the right parity). The other two are the computer tables of section 7. '
                'Each cell is the share of the subset for which that bound proves there is no finish in ') if i == 0 else 'The same for a finish in ') + f'{T} or less:', '',
          f'| Subset | No {T}: hand bound proves it | No {T}: NISS@DR proves it | No {T}: everything visible proves it |', '|---|---:|---:|---:|']
    for s in subs:
        L.append(f"| {s} | {pr(hand[s], T)} | {pr(lat[('KF', s)], T)} | {pr(lat[('c+2520+F', s)], T)} |")
write('appendix_a.md', L)

# ---- Appendix B
L = ['| Subset | L | E-slice | Share of subset | Fastest, moves | Fastest minus L | Average optimal, moves |', '|---|---:|---|---:|---:|---:|---:|']
L2 = ['', 'The same rows, with the share finishing in 10, 11, 12 and 13 or less:', '', '| Subset | L | E-slice | In 10 | In 11 | In 12 | In 13 |', '|---|---:|---|---:|---:|---:|---:|']
for s in ['4c3 4e', '0c3 4e', '2c4 4e', '0c4 4e', '4c4 4e', '2c5 4e', '4b5 4e']:
    g = collections.defaultdict(lambda: [0] * 19)
    for x, lo, hi, l, dlp, par, d, c in pv.rows('h2_lengths.csv'):
        if x == s: g[(int(l), int(par))][int(d)] += int(c)
    tot = sum(sum(h) for h in g.values())
    for (l, par), h in sorted(g.items()):
        m = pv.fastest(h)
        L.append(f"| {s} | {l} | {'odd' if par else 'even'} | {100*sum(h)/tot:.1f}% | {m} | +{m-l} | {pv.avg(h):.2f} |")
        L2.append(f"| {s} | {l} | {'odd' if par else 'even'} | {pv.cells(h)} |")
write('appendix_b.md', L + L2)

# ---- pairs
g = collections.defaultdict(lambda: collections.defaultdict(lambda: [0] * 19))
gc = collections.defaultdict(lambda: collections.defaultdict(lambda: [0] * 19))
for s, tp, _, _, _, d, c in pv.rows('h5_pairs.csv'):
    g[s][min(int(tp), 6)][int(d)] += int(c); gc[s.split()[0]][min(int(tp), 5)][int(d)] += int(c)
L = []
for T in pv.TARGETS:
    L += ['', f'**Share finishing in {T} or less.** Each row is a subset, each column a number of true pairs:', '', '| Subset | 0 pairs | 1 | 2 | 3 | 4 | 5 | 6 or more |', '|---|---:|---:|---:|---:|---:|---:|---:|']
    for s in subs:
        L.append(f'| {s} | ' + ' | '.join(pv.pct(g[s][k], T) if sum(g[s][k]) else '' for k in range(7)) + ' |')
tot = [sum(sum(g[s][k]) for s in subs) for k in range(7)]
L += ['', 'Share of all DRs with that many pairs: ' + ', '.join(f'{k}{" or more" if k == 6 else ""}: {100*tot[k]/pv.TOT:.1f}%' for k in range(7)) + '.']
write('odds_by_true_pairs.md', L[1:])
L = ['| Corners | Finish in | 0 pairs | 1 | 2 | 3 | 4 | 5 or more |', '|---|---|---:|---:|---:|---:|---:|---:|']
for cs in ['4a1', '4b2', '2c3', '4c3', '2c4', '4c4', '2c5', '4b5']:
    for T in (10, 11, 12):
        L.append(f'| {cs} | {T} or less | ' + ' | '.join(pv.pct(gc[cs][k], T) for k in range(6)) + ' |')
tp = [sum(sum(gc[cs][k]) for cs in gc) for k in range(6)]
L.append('| share of all DRs | | ' + ' | '.join(f'{100*x/pv.TOT:.0f}%' for x in tp) + ' |')
write('main_pairs.md', L)

# ---- HTR on both sides
sq = collections.defaultdict(lambda: collections.defaultdict(lambda: [0] * 19))
for s, lo, hi, l, dlp, par, d, c in pv.rows('h2_lengths.csv'): sq[s][(int(lo), int(hi))][int(d)] += int(c)
L = []
for s in subs:
    tot = sum(sum(h) for h in sq[s].values())
    L += ['', f'**{s}**. Each row is a pair of HTR lengths:', '', '| HTR, shorter and longer side | Share of subset | Average optimal, moves | Fastest, moves | In 10 | In 11 | In 12 | In 13 |', '|---|---:|---:|---:|---:|---:|---:|---:|']
    for (a, b), h in sorted(sq[s].items()):
        L.append(f'| {a} and {b} | {pv.num(100*sum(h)/tot)} | {pv.avg(h):.2f} | {pv.fastest(h)} | {pv.cells(h)} |')
write('htr_square_tables.md', L[1:])
L = []
for s in ['4c3 4e', '2c4 4e', '2c5 4e', '0c3 4e']:
    cellsq = {k: h for k, h in sq[s].items() if sum(h) / sum(sum(x) for x in sq[s].values()) >= 0.001}
    L += ['', f'**{s}**, one row per pair of HTR lengths:', '', '| HTR, shorter and longer side | In 10 | In 11 | In 12 |', '|---|---:|---:|---:|']
    for a, b in sorted(cellsq):
        L.append(f'| {a} and {b} | ' + pv.cells(cellsq[(a, b)], (10, 11, 12)) + ' |')
write('main_squares.md', L[1:])

# ---- Zagros's rule
def z(pred):
    h = [0] * 19
    for s in subs:
        if s.startswith('4c3'):
            for (a, b), v in sq[s].items():
                if pred(a, b):
                    for d, c in enumerate(v): h[d] += c
    return h
allc = z(lambda a, b: True)
L = ['| 4c3 that is… | Share of 4c3 | Average optimal, moves | In 10 | In 11 | In 12 | In 13 |', '|---|---:|---:|---:|---:|---:|---:|']
for name, pred in (('9+ to HTR on both sides (what the rule throws away)', lambda a, b: a >= 9), ('the rest', lambda a, b: a < 9), ('7 or less to HTR on at least one side', lambda a, b: a <= 7)):
    h = z(pred); L.append(f'| {name} | {100*sum(h)/sum(allc):.0f}% | {pv.avg(h):.2f} | {pv.cells(h)} |')
h = z(lambda a, b: a < 9)
L += ['', 'Share of the 4c3 finishes the rule keeps: ' + ', '.join(f'{100*sum(h[:T+1])/sum(allc[:T+1]):.0f}% of those in {T}' for T in pv.TARGETS) + '.']
write('main_zagros.md', L)
