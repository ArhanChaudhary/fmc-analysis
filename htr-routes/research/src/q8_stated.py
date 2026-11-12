#!/usr/bin/env python3
"""Question 8 under the method's own definition: some reduction to 1q (or 2q) of at most R moves, on normal, on
inverse or split by NISS, followed by the OPTIMAL finish of the reduced state (any number of quarter turns), gives an
optimal finish (or one within +1, or of at most M = 10, 11, 12 moves).

Input: out/big/bound4.tsv (htrtools bound4: exact search on reductions, first 4,000 states of every subset x edges,
the states of the main pass), out/big/redcount2.tsv (the number of reductions of each length a solver writes, same
states).  The "window" reading of q8_bounding_v2.tsv (a reduction followed by a finish with exactly one quarter turn,
what JTuu's sim measured) is kept beside it.
Output: out/q8_bounding_stated.tsv (group, q, R, n, mean reductions <= R and its standard error, share found per target
and its standard error)."""
import csv, collections
import numpy as np
from common import *
TARGETS = ['opt', 'p1', 'M10', 'M11', 'M12']
B4 = {}
for r in csv.DictReader(open(f'{R}/out/big/bound4.tsv'), delimiter='\t'):
    B4[(r['subset'], int(r['idx']))] = {x.split(':')[0]: (int(x.split(':')[1]), int(x.split(':')[2])) for x in r['targets'].split(';')}
RC = {(r['subset'], int(r['idx'])): r for r in csv.DictReader(open(f'{R}/out/big/redcount2.tsv'), delimiter='\t')}
def cum(r, q, R_): return sum(int(r[f'q{q}_r{k}']) for k in range(0, min(R_, 7) + 1))
NS = collections.Counter(k[0] for k in B4)
BYSUB = collections.defaultdict(list)
for k in B4: BYSUB[k[0]].append(k)
groups = [(s, [s]) for s in SUBS] + [(g, [s for s in SUBS if CORNER(s) == g]) for g in CGROUPS] + [('all', SUBS)]
with open(f'{OUT}/q8_bounding_stated.tsv', 'w') as f:
    f.write('group\tq\tR\tn_states\tmean_reductions_le_R\tse_reductions\t' + '\t'.join(f'found_{t}\tse_{t}' for t in TARGETS) + '\n')
    for g, subs in groups:
        keys_ = [k for s in subs for k in BYSUB[s]]
        w = np.array([SIZE[s] / NS[s] for s, i in keys_])
        for q in (1, 2):
            for Rv in range(0, 8):
                c = np.array([cum(RC[k], q, Rv) for k in keys_], float)
                mu = (c * w).sum() / w.sum(); se = np.sqrt(((c - mu) ** 2 * w).sum() / w.sum() / max(len(c) - 1, 1))
                line = f'{g}\t{q}\t{Rv}\t{len(c)}\t{mu:.1f}\t{se:.1f}'
                for t in TARGETS:
                    v = np.array([B4[k][t][q - 1] <= Rv for k in keys_], float)
                    p = (v * w).sum() / w.sum(); line += f'\t{p:.4f}\t{np.sqrt(p * (1 - p) / len(v)):.4f}'
                f.write(line + '\n')
print('done')
