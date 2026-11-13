#!/usr/bin/env python3
"""The main checklist of section 4 with edge counts: for each subset x edges and each of the first three routes of its
own budget-2 checklist (corner routes, out/q2_checklist_budget.tsv, level C), how the route splits into edge paths.

Membership as checklist_cost.member: an optimal finish, read the route's way, with HTR at most the shortest NISS HTR
+ 2.  The edge path of a reading is its H key (the label with bad edges at the start and after each quarter turn up to
HTR, brackets at the switch); every H key lies in exactly one corner route (level C).  All shares are of all sampled
DRs of the subset x edges:
  alone      the route finds the optimal (equals the 'alone' column of q2_checklist_budget.tsv: checked)
  top        it finds the optimal along its most common edge path
  fork       the first step (position after a quarter turn, start and HTR excluded) where no single edge count
             carries 80% of the route's DRs; at that step the share of DRs where the route finds the optimal
             passing each edge count ('' if the route has no such step)
Output: out/edge_paths_checklist.tsv.  Light: one subset at a time (about 1 GB)."""
import csv, collections, time
import numpy as np
from common import SUBS, OUT, load_states, Routes, keys, parse_key, level_of

B = 2; STEPS = 3; FORK = 0.8
EDG = ('0e', '2e', '4e', '6e', '8e')

def main():
    t0 = time.time(); K = keys()
    bud = [r for r in csv.DictReader(open(f'{OUT}/q2_checklist_budget.tsv'), delimiter='\t')
           if r['level'] == 'C' and r['target'] == 'opt' and r['budget'] == str(B) and int(r['step']) <= STEPS]
    f = open(f'{OUT}/edge_paths_checklist.tsv', 'w')
    f.write('subset\tstep\tclass\talone\ttop_path\ttop\tn_paths\tfork_pos\tfork_corner\tfork_side\t' + '\t'.join(EDG) + '\n')
    for s in SUBS:
        want = {r['class']: r for r in bud if r['group'] == s}
        st = load_states(s); rt = Routes(s); n = rt.n
        niss = st['htrNiss'][rt.state]
        u, inv = np.unique(rt.rid, return_inverse=True)
        cu = [level_of(K[x], 'C') if K[x][0] == 'H' else '' for x in u]     # class of each distinct route id
        m = (rt.delta == 0) & (rt.htr <= niss + B)
        for c, r in sorted(want.items(), key=lambda kv: int(kv[1]['step'])):
            sel = np.nonzero(m & np.array([x == c for x in cu])[inv])[0]
            byh = collections.defaultdict(set)
            for i in sel: byh[int(rt.rid[i])].add(int(rt.state[i]))
            states = set().union(*byh.values()) if byh else set()
            alone = len(states) / n
            assert abs(alone - float(r['alone'])) < 6e-5, (s, c, alone, r['alone'])
            top = max(byh, key=lambda h: (len(byh[h]), K[h]))
            kind, labs, sw, post = parse_key(K[top])
            fork = None
            for pos in range(1, len(labs) - 1):
                per = collections.defaultdict(set)
                for h, ss in byh.items():
                    per[parse_key(K[h])[1][pos].split()[1]] |= ss
                if max(len(v) for v in per.values()) < FORK * len(states):
                    fork = (pos, labs[pos].split()[0], 'inverse' if sw is not None and pos >= sw else 'normal', per); break
            row = [s, r['step'], c, f'{alone:.4f}', K[top][2:], f'{len(byh[top]) / n:.4f}', str(len(byh))]
            if fork:
                pos, corner, side, per = fork
                row += [str(pos), corner, side] + [f'{len(per[e]) / n:.4f}' if e in per else '' for e in EDG]
            else:
                row += [''] * (3 + len(EDG))
            f.write('\t'.join(row) + '\n')
        f.flush()
        print(s, f'{time.time() - t0:.0f}s', flush=True)

if __name__ == '__main__':
    main()
