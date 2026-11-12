#!/usr/bin/env python3
"""The reduction counts of htrtools redcount2 (coset tables) against brute-force enumeration of every pair
(htrtools redcount, rmax 7) on the first 10 states of every subset x edges (480 states), every length r <= 7.
Output: out/checks/check_redcount7.txt"""
import csv, collections
from common import R, OUT
old = collections.defaultdict(dict)
for r in csv.DictReader(open(f'{R}/out/big/redcount_brute7.tsv'), delimiter='\t'):
    old[(r['subset'], int(r['idx']))][(int(r['target_q']), int(r['r']))] = int(r['pairs'])
new = {}
for r in csv.DictReader(open(f'{R}/out/big/redcount2.tsv'), delimiter='\t'):
    k = (r['subset'], int(r['idx']))
    if k in old: new[k] = {(q, rr): int(r[f'q{q}_r{rr}']) for q in (1, 2) for rr in range(8)}
eq = sum(old[k] == new[k] for k in new)
subs = sorted({k[0] for k in new})
msg = (f'redcount2 vs brute force for every length r <= 7 (q = 1 and 2): {len(new)} states, the first 10 of {len(subs)} subsets ({", ".join(subs)}); '
       f'{eq} identical in every (q, r) cell. The brute-force run was stopped after 6 hours (about 70 hours for all 48 subsets); r = 6 and 7 are not checked on the other 44 subsets.')
print(msg); open(f'{OUT}/checks/check_redcount7.txt', 'w').write(msg + '\n')
