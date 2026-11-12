#!/usr/bin/env python3
"""What knowing the bad-edge count is worth: per subset x edges, budget 2, the share found after 1/2/3/5 routes by
(a) that group's own greedy checklist and (b) the pooled corner-subset checklist (edge counts pooled by exact size)
applied to that group.  Targets optimal and optimal + 1 (each with its own checklists, as in checklist_cost.py).
Also: whether the first route differs, and the rank of the pooled first route in the group's own greedy order.
Membership and greedy are checklist_cost.py's (same tie-break); (a) is checked against q2_checklist_budget.tsv.
Output: out/q2_edge_gain.tsv.  Light: one corner subset in memory at a time (~1.3 GB)."""
import time
import numpy as np
import checklist_cost as cc
from common import SUBS, SIZE, CGROUPS, CORNER, OUT
import csv

STEPS = (1, 2, 3, 5)
DEEP = 60                                       # greedy depth for the rank of the pooled first route
B = 2

def main():
    t0 = time.time()
    cc.load_aliases()
    ref = {(r['group'], r['target'], r['step']): r for r in csv.DictReader(open(f'{OUT}/q2_checklist_budget.tsv'), delimiter='\t')
           if r['level'] == 'C' and r['budget'] == str(B)}
    f = open(f'{OUT}/q2_edge_gain.tsv', 'w')
    f.write('subset\tcorner\ttarget\tweight_in_corner\t' + '\t'.join(f'own{k}' for k in STEPS) + '\t'
            + '\t'.join(f'pooled{k}' for k in STEPS) + '\town_first\tpooled_first\tfirst_differs\tpooled_first_rank\n')
    for g in CGROUPS:
        subs = [s for s in SUBS if CORNER(s) == g]
        if len(subs) < 2: continue
        mem = [(s,) + cc.member(s) for s in subs]
        tot = sum(SIZE[s] for s in subs)
        for tg in ('opt', 'p1'):
            key = ('C', tg, B)
            # pooled checklist, exactly as checklist_cost.py builds it
            w = np.concatenate([np.full(n, SIZE[s] / n) for s, n, _ in mem])
            offs = 0; S = []; C = []
            for s, n, out in mem:
                S.append(out[key][0] + offs); C.append(out[key][1]); offs += n
            pooled = [c for c, *_ in cc.greedy(np.concatenate(S), np.concatenate(C), w, 'C', steps=max(STEPS))]
            assert cc.names['C'][pooled[0]] == ref[(g, tg, '1')]['class'], (g, tg)
            for s, n, out in mem:
                si, ci = out[key]
                own = cc.greedy(si, ci, np.ones(n), 'C', steps=DEEP)
                for k in (1, 2, 3):
                    assert abs(own[k - 1][2] - float(ref[(s, tg, str(k))]['cumulative'])) < 6e-5, (s, tg, k)
                    assert cc.names['C'][own[k - 1][0]] == ref[(s, tg, str(k))]['class'], (s, tg, k)
                ownc = [own[min(k, len(own)) - 1][2] for k in STEPS]
                pc_ = []
                for k in STEPS:
                    got = np.zeros(n, bool); got[si[np.isin(ci, pooled[:k])]] = True
                    pc_.append(got.mean())
                ids = [c for c, *_ in own]
                rank = ids.index(pooled[0]) + 1 if pooled[0] in ids else f'>{len(ids)}'
                f.write(f'{s}\t{g}\t{tg}\t{SIZE[s] / tot:.6f}\t' + '\t'.join(f'{x:.4f}' for x in ownc) + '\t'
                        + '\t'.join(f'{x:.4f}' for x in pc_) + f'\t{cc.names["C"][ids[0]]}\t{cc.names["C"][pooled[0]]}\t'
                        + f'{int(ids[0] != pooled[0])}\t{rank}\n')
        f.flush(); print(g, f'{time.time() - t0:.0f}s', flush=True)

if __name__ == '__main__':
    main()
