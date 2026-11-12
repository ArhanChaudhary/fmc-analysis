#!/usr/bin/env python3
"""Routes read with the bad-edge count at every step.  The route keys of `htrtools routes` already carry the label of
every state on the route (corner subset and bad edges, the same labels as the subset x edges groups: checked here
against the states files), so no new enumeration is needed: the edge-refined class is the key itself (level 'H' of
common.level_of), the corner-only class the existing level 'C'.

Budget 2 (HTR at most the shortest NISS HTR + 2), targets optimal and optimal + 1, membership as checklist_cost.member.
Outputs:
  out/q2_edge_steps_checklist.tsv  per subset x edges and target: greedy over edge-refined classes (steps 1-8), its
                                   cumulative share, and the corner-only greedy's cumulative share at the same step
  out/q2_edge_steps_via.tsv        per subset x edges, target and intermediate label (subset x edges, or subset with
                                   any edges, 'Xyz *'): share of states where some budget-2 route passes through it
                                   (a state after a quarter turn, before HTR; start and HTR not counted;
                                   4a3 / 4b3 also counted together as 4c3, 4a4 / 4b4 as 4c4)
  out/checks/check_edge_steps.txt  the label checks and the corner-only reproduction check
Light: one subset in memory at a time (~1 GB)."""
import csv, time, collections
import numpy as np
import checklist_cost as cc
from common import SUBS, OUT, CORNER, load_states, Routes, parse_key, level_of, aliases

B = 2; STEPS = 8
MERGE = {'4a3': '4c3', '4b3': '4c3', '4a4': '4c4', '4b4': '4c4'}
for d in (cc.cache, cc.names, cc.ids, cc.MIRROR): d['H'] = {} if d is not cc.names else []
cc.NF['H'] = set()

def main():
    t0 = time.time(); K = cc.K
    cc.load_aliases()
    mirror, nf = aliases()
    for a, b in mirror.items():
        if a in nf and K[a][0] == 'H' and K[b][0] == 'H':
            ha, hb = level_of(K[a], 'H'), level_of(K[b], 'H')
            if ha != hb:
                cc.NF['H'].add(ha); cc.MIRROR['H'].setdefault(ha, hb); cc.MIRROR['H'].setdefault(hb, ha)
    ref = {(r['group'], r['target'], r['step']): r for r in csv.DictReader(open(f'{OUT}/q2_checklist_budget.tsv'), delimiter='\t')
           if r['level'] == 'C' and r['budget'] == str(B)}
    fc = open(f'{OUT}/q2_edge_steps_checklist.tsv', 'w')
    fc.write('subset\ttarget\tstep\tclass\tcumulative\tcorner_only_class\tcorner_only_cumulative\ttied_classes\tmirror_alias\n')
    fv = open(f'{OUT}/q2_edge_steps_via.tsv', 'w')
    fv.write('subset\ttarget\tvia\tshare\n')
    chk = open(f'{OUT}/checks/check_edge_steps.txt', 'w')
    for s in SUBS:
        st = load_states(s); rt = Routes(s); n = rt.n
        # 1. the state's own label carries the group's edge count; every route starts at the state's label on its side
        e = s.split()[1]
        assert all(l.split()[1] == e for l in st['lab_n']), s
        u, inv = np.unique(rt.rid, return_inverse=True)
        start = np.array([parse_key(K[x])[1][0] if K[x][0] == 'H' else '' for x in u])[inv]
        h = start != ''
        ok = (start[h] == st['lab_n'][rt.state[h]]) | (start[h] == st['lab_i'][rt.state[h]])
        assert ok.all(), (s, (~ok).sum())
        chk.write(f'{s}\tstate label edges = group edges: {n} states\troute starts at lab_n or lab_i: {int(h.sum())} entries\n')
        niss = st['htrNiss'][rt.state]
        hcls = np.array([cc.cls(int(x), 'H') for x in u])[inv]
        inter = [set(parse_key(K[x])[1][1:-1]) if K[x][0] == 'H' else set() for x in u]
        for tg in ('opt', 'p1'):
            m = (hcls >= 0) & ((rt.delta == 0) & (rt.htr <= niss + B) if tg == 'opt' else (rt.htr1 <= niss + B))
            pair = np.unique(rt.state[m] * (1 << 24) + hcls[m]); si, ci = pair >> 24, pair & ((1 << 24) - 1)
            res = cc.greedy(si, ci, np.ones(n), 'H', steps=STEPS)
            for i, (c, marg, cum, al, nt) in enumerate(res):
                r = ref.get((s, tg, str(i + 1)))
                nm = cc.names['H'][c]
                fc.write(f'{s}\t{tg}\t{i + 1}\t{nm}\t{cum:.4f}\t{r["class"] if r else ""}\t{r["cumulative"] if r else ""}\t{nt}\t{cc.MIRROR["H"].get(nm, "")}\n')
            # 2. via: states with some qualifying route through each intermediate label
            via = collections.defaultdict(set)
            mi = np.nonzero(m)[0]
            # group qualifying entries by unique route, then add their states to each label of that route
            order = np.argsort(inv[mi], kind='stable'); mi = mi[order]
            ur, starts = np.unique(inv[mi], return_index=True)
            ends = list(starts[1:]) + [len(mi)]
            for r_, a, b in zip(ur, starts, ends):
                labs = inter[r_]
                if not labs: continue
                ss = rt.state[mi[a:b]]
                for l in labs:
                    c, e = l.split()
                    for c2 in {c, MERGE.get(c, c)}:          # 4a3 / 4b3 are also counted as 4c3, 4a4 / 4b4 as 4c4
                        via[f'{c2} {e}'].update(ss.tolist()); via[c2 + ' *'].update(ss.tolist())
            for l in sorted(via):
                fv.write(f'{s}\t{tg}\t{l}\t{len(via[l]) / n:.4f}\n')
        # 3. corner-only reproduction (the existing numbers): C-level own greedy equals q2_checklist_budget.tsv
        st_n, out = cc.member(s)
        for tg in ('opt', 'p1'):
            si, ci = out[('C', tg, B)]
            for i, (c, marg, cum, al, nt) in enumerate(cc.greedy(si, ci, np.ones(st_n), 'C', steps=STEPS)):
                r = ref[(s, tg, str(i + 1))]
                assert cc.names['C'][c] == r['class'] and abs(cum - float(r['cumulative'])) < 6e-5, (s, tg, i)
        chk.write(f'{s}\tcorner-only budget-2 greedy (opt, +1, 8 steps) reproduces q2_checklist_budget.tsv\n')
        fc.flush(); fv.flush(); chk.flush()
        print(s, f'{time.time() - t0:.0f}s', flush=True)

if __name__ == '__main__':
    main()
