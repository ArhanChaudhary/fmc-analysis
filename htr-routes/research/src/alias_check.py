#!/usr/bin/env python3
"""Mirror aliases: a normal-first reading and the inverse-first reading of the same split of the same finish are the same
(A, B) pair, so a class and its mirror should work on exactly the same states.  Checked on the C-level classes of every
subset x edges at the optimum (budget none): out/checks/check_aliases.txt."""
import collections
import numpy as np
from common import *
K = keys(); mirror, nf = aliases()
lines = []; tot = same = 0
for s in SUBS:
    rt = Routes(s)
    m = rt.delta == 0
    sets = collections.defaultdict(set)
    for st, rid in zip(rt.state[m], rt.rid[m]):
        k = K[int(rid)]
        if k[0] == 'H': sets[level_of(k, 'C')].add(int(st))
    pairs = set()
    for a in nf:
        b = mirror[a]
        ca, cb = level_of(K[a], 'C'), level_of(K[b], 'C')
        if ca != cb and ca in sets and cb in sets: pairs.add((ca, cb))
    for ca, cb in pairs:
        tot += 1; same += sets[ca] == sets[cb]
msg = f'C-level mirror pairs checked over all 48 subsets: {tot}; identical state sets: {same}.'
print(msg); open(f'{OUT}/checks/check_aliases.txt', 'w').write(msg + '\n')
