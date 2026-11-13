#!/usr/bin/env python3
"""Decision card "Should I NISS in the middle of this route?".  For each corner subset, follow the normal-side part of
the first route of the HTR-routes budget-2 checklist.  After each quarter turn on it (you are at that subset on
normal), compare the two ways on:
  linear   keep going on normal: a route with no switch whose subsets start the same way;
  switch   switch now: a route whose normal part is exactly the subsets so far, the rest on the other side.
Same data and definitions as htr-routes (research/src/checklist_cost.py): a route "works" on a DR state when some
optimal finish follows it with an HTR at most 2 moves longer than the state's shortest NISS HTR (budget 2); 25,000
uniformly random DR states per subset x edges, pooled by the exact number of DR states.  Route classes at level C
(corner subsets only, post-HTR part either kind).

Output: cards/data/niss_mid.tsv: subset, the subsets so far on normal, quarter turns so far, share where continuing
linearly works, share where switching now works, share where either works.  usage: niss_mid.py"""
import os, sys, csv, collections
import numpy as np
sys.path.insert(0, '/data/fmc/htr-routes/research/src')
from common import keys, load_states, Routes, SUBS, SIZE, CORNER, CGROUPS, level_of, parse_key

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, '..', 'data', 'niss_mid.tsv')
BUDGET = 2
K = keys()

first = {}
for r in csv.DictReader(open('/data/fmc/htr-routes/research/out/q2_checklist_budget.tsv'), delimiter='\t'):
    if r['level'] == 'C' and r['target'] == 'opt' and r['budget'] == str(BUDGET) and r['step'] == '1' and ' ' not in r['group']:
        first[r['group']] = r['class']

parsed = {}
def shape(rid):
    """(subset labels, switch index or None) of a route id at level C, or None for a non-HTR key"""
    p = parsed.get(rid, 0)
    if p == 0:
        k = K[rid]
        if k[0] != 'H':
            p = None
        else:
            _, labs, sw, _ = parse_key('H:' + level_of(k, 'C'))
            p = (tuple(labs), sw)
        parsed[rid] = p
    return p

rows = []
for g in CGROUPS:
    _, labs, sw, _ = parse_key('H:' + first[g])
    normal = labs[:sw] if sw is not None else labs[:-1]     # the subsets reached on normal before any switch, not HTR
    steps = list(range(1, len(normal)))                      # j quarter turns done on normal
    acc = collections.defaultdict(float); total = 0.0
    for s in [s for s in SUBS if CORNER(s) == g]:
        st = load_states(s); rt = Routes(s)
        w = SIZE[s] / rt.n; total += SIZE[s]
        u, inv = np.unique(rt.rid, return_inverse=True)
        shapes = [shape(int(x)) for x in u]
        niss = st['htrNiss'][rt.state]
        ok = (rt.delta == 0) & (rt.htr <= niss + BUDGET)
        for j in steps:
            pre = tuple(normal[:j + 1])
            lin_u = np.array([p is not None and p[1] is None and p[0][:j + 1] == pre for p in shapes])
            sw_u = np.array([p is not None and p[1] == j + 1 and p[0][:j + 1] == pre for p in shapes])
            covL = np.zeros(rt.n, bool); covL[rt.state[ok & lin_u[inv]]] = True
            covS = np.zeros(rt.n, bool); covS[rt.state[ok & sw_u[inv]]] = True
            acc[(j, 'lin')] += covL.sum() * w; acc[(j, 'sw')] += covS.sum() * w; acc[(j, 'either')] += (covL | covS).sum() * w
        print(s, flush=True)
    for j in steps:
        rows.append((g, ' > '.join(normal[:j + 1]), j, acc[(j, 'lin')] / total, acc[(j, 'sw')] / total, acc[(j, 'either')] / total))

os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, 'w') as f:
    f.write('subset\tso_far\tqt_done\tcontinue_linear\tswitch_now\teither\n')
    for g, sofar, j, a, b, c in rows:
        f.write(f'{g}\t{sofar}\t{j}\t{a:.6f}\t{b:.6f}\t{c:.6f}\n')
print('wrote', OUT)
