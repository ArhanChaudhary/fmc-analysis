#!/usr/bin/env python3
"""Compare our exact census with Joba's per-subset DR-finish distribution (Discord T9115, 2025-08)."""
import csv, re, collections, sys
mine = collections.defaultdict(lambda: collections.Counter())
for r in csv.DictReader(open('/data/fmc/judging-a-dr/research/out/census.csv')):
    mine[r['subset']][int(r['depth'])] += int(r['count'])
joba = collections.defaultdict(dict); cur = None
for line in open('/data/fmc/assets/attachments/1406633631165714492_0_drfin_subset_dist.txt'):
    line = line.rstrip()
    m = re.match(r'^\s*-\s*(\d+):\s*(\d+)', line)
    if m: joba[cur][int(m.group(1))] = int(m.group(2))
    elif line.strip(): cur = line.strip().replace('4c5', '4b5')   # Mallard prints 4c5 for the subset others call 4b5
ok = bad = 0
names = sorted(set(mine) | set(joba))
for n in names:
    a = dict(mine.get(n, {})); b = joba.get(n, {})
    if a == b: ok += 1
    else:
        bad += 1; print('MISMATCH', n, 'mine', sorted(a.items())[:6], 'joba', sorted(b.items())[:6])
print(f'subsets compared: {len(names)}  identical: {ok}  different: {bad}')
print('Joba total', sum(sum(v.values()) for v in joba.values()), ' ours', sum(sum(v.values()) for v in mine.values()))
tot = collections.Counter()
for n in mine:
    for d, c in mine[n].items(): tot[d] += c
print('overall depth distribution:', [tot[d] for d in range(19)])
