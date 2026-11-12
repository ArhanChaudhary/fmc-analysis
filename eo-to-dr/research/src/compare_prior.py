#!/usr/bin/env python3
"""Our sampled DR lengths against is-dr-xs-worth-it section 6.4 (out/nearest.tsv: 2,000,000 random states, shortest
DR over the 3 axes, normal and normal+inverse, linear), and the exact one-axis distribution against all_dr.hist.
Writes out/compare_prior.tsv: for each measure both distributions, both means, and a chi-square statistic with its
degrees of freedom (lengths with fewer than 5 expected scrambles pooled)."""
import csv, os, collections
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, '..', 'out')
csv.field_size_limit(10**7)
prior = collections.defaultdict(dict)
for r in csv.DictReader(open('/data/fmc/is-dr-xs-worth-it/research/out/nearest.tsv'), delimiter='\t'):
    if r['what'] == 'dr':
        prior[r['sides']][int(r['turns'])] = int(r['states'])
rows = list(csv.DictReader(open(os.path.join(OUT, 'big', 'scr50k.tsv')), delimiter='\t'))
AX = ['RL', 'UD', 'FB']
ours = {'normal': collections.Counter(min(int(r[f'd_n_{a}']) for a in AX) for r in rows),
        'both': collections.Counter(min(int(r[f'd_{s}_{a}']) for s in 'ni' for a in AX) for r in rows)}
hist = [int(l.split()[1]) for l in open('/data/fmc/is-dr-xs-worth-it/research/out/bfs/all_dr.hist') if l[0].isdigit() and len(l.split()) == 2]
prior['one axis (exact table)'] = dict(enumerate(hist))
ours['one axis (exact table)'] = collections.Counter(int(r[f'd_n_{a}']) for r in rows for a in AX)

def chi2(p, o):
    P, O = sum(p.values()), sum(o.values())
    ks = sorted(set(p) | set(o))
    bins, cur_e, cur_o = [], 0.0, 0
    for k in ks:
        cur_e += p.get(k, 0) / P * O
        cur_o += o.get(k, 0)
        if cur_e >= 5:
            bins.append((cur_e, cur_o)); cur_e, cur_o = 0.0, 0
    if cur_e > 0:
        e, x = bins.pop() if bins else (0, 0)
        bins.append((e + cur_e, x + cur_o))
    stat = sum((x - e) ** 2 / e for e, x in bins)
    return round(stat, 2), len(bins) - 1

with open(os.path.join(OUT, 'compare_prior.tsv'), 'w') as f:
    f.write('measure\tprior_n\tprior_mean\tours_n\tours_mean\tchi2\tdf\tprior_dist\tours_dist\n')
    for key, okey, name in (('normal', 'normal', 'best of 3 axes, normal'), ('both', 'both', 'best of 6 (normal or inverse)'),
                            ('one axis (exact table)', 'one axis (exact table)', 'one axis')):
        p, o = prior[key], ours[okey]
        pm = sum(k * v for k, v in p.items()) / sum(p.values())
        om = sum(k * v for k, v in o.items()) / sum(o.values())
        c, df = chi2(p, o)
        f.write(f"{name}\t{sum(p.values())}\t{pm:.4f}\t{sum(o.values())}\t{om:.4f}\t{c}\t{df}\t"
                f"{' '.join(f'{k}:{p[k]}' for k in sorted(p))}\t{' '.join(f'{k}:{o[k]}' for k in sorted(o))}\n")
        print(f'{name}: prior mean {pm:.4f} (n={sum(p.values())}), ours {om:.4f} (n={sum(o.values())}), chi2 {c} on {df} df')
