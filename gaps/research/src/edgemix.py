#!/usr/bin/env python3
"""Markdown table: share of each corner subset's DRs in each bad-edge count, uniform (exact) vs the four populations."""
import csv
G = '/data/fmc/gaps/research/out'
R = list(csv.DictReader(open(f'{G}/a_subsets.tsv'), delimiter='\t'))
d = {(r['group'], r['pop']): r for r in R}
corners = list(dict.fromkeys(r['group'] for r in R if ' ' not in r['group']))
print('| subset | uniform | dr11 | scr11 | dr10 | scr10 |')
print('|---|---|---|---|---|---|')
for c in corners:
    for r in R:
        if r['pop'] == 'dr11' and r['group'].startswith(c + ' '):
            g = r['group']; row = []
            u = float(r['uniform_share']) / float(d[(c, 'dr11')]['uniform_share'])
            for p in ['dr11', 'scr11', 'dr10', 'scr10']:
                x = d.get((g, p))
                if not x or x['n_drs'] == '0': row.append('-'); continue
                s = float(x['share']) / float(d[(c, p)]['share']); se = float(x['se']) / float(d[(c, p)]['share'])
                row.append(f'{100 * s:.1f} ± {100 * se:.1f}')
            print(f'| {g} | {100 * u:.1f} | ' + ' | '.join(row) + ' |')
