#!/usr/bin/env python3
"""The checklists of out/q2_checklist_budget.tsv read again at optimal + 1: for each group (corner subset, edges
pooled by exact size, and each subset x edges), each HTR budget and the greedy order found at the optimum, the
cumulative share of states where the first k classes of that same list find a finish within optimal + 1 (with the
same HTR budget).  The +1 rows of q2_checklist_budget.tsv are a separate greedy order; this file keeps the order a
solver would use (the one built for the optimum).

Input: out/q2_checklist_budget.tsv, out/big/run1 (via common.py / checklist_cost.py)
Output: out/q2_same_classes_p1.tsv (group, budget, step, class, cum_opt, cum_p1)"""
import csv, collections
import numpy as np
from common import *
import checklist_cost as cc

BUD = {'0': 0, '1': 1, '2': 2, 'inf': 99}
rows = list(csv.DictReader(open(f'{OUT}/q2_checklist_budget.tsv'), delimiter='\t'))
order = collections.defaultdict(list)
for r in rows:
    if r['level'] == 'C' and r['target'] == 'opt':
        order[(r['group'], r['budget'])].append(r)

out = open(f'{OUT}/q2_same_classes_p1.tsv', 'w')
out.write('group\tbudget\tstep\tclass\tcum_opt\tcum_p1\n')
for g in CGROUPS:
    subs = [s for s in SUBS if CORNER(s) == g]
    mem = []
    for s in subs:
        n, o = cc.member(s); mem.append((s, n, o))
    groups = [(s, [(s, n, o)]) for s, n, o in mem] + ([(g, mem)] if len(mem) > 1 else [])
    for gname, ms in groups:
        w = np.concatenate([np.full(n, SIZE[s] / n) for s, n, _ in ms]); W = w.sum()
        for bname, b in BUD.items():
            lst = order[(gname, bname)]
            sets = {}
            for tg in ('opt', 'p1'):
                offs = 0; S = []; C = []
                for s, n, o in ms:
                    S.append(o[('C', tg, b)][0] + offs); C.append(o[('C', tg, b)][1]); offs += n
                sets[tg] = (np.concatenate(S), np.concatenate(C))
            cov = {tg: np.zeros(len(w), bool) for tg in sets}
            for r in lst:
                cid = cc.ids['C'].get(r['class'])
                for tg, (si, ci) in sets.items():
                    if cid is not None: cov[tg][si[ci == cid]] = True
                out.write(f"{gname}\t{bname}\t{r['step']}\t{r['class']}\t{w[cov['opt']].sum() / W:.4f}\t{w[cov['p1']].sum() / W:.4f}\n")
    out.flush()
    print(g, flush=True)
