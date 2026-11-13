#!/usr/bin/env python3
"""Independent recount of the budget-2 checklists (section 1 and 4) from htrtools' per-state route records.

Only the input records are shared with the study (they are checked state by state by vhtr cmp); the class names,
the budget rule, the greedy cover and the pooling by exact cell size are written here from section 3's definitions,
without the study's Python.  Cell sizes: cosets per label from vhtr qtcos (every HTR coset holds 663,552 states).
Output: verify/out/recount_checklist.tsv (group, target, step, class, cumulative) and a comparison with
out/q2_checklist_budget.tsv (level C, budget 2) printed at the end.
Usage: recount_checklist.py [budget]     (0, 1, 2; 99 = no HTR limit)"""
import sys, re, csv, struct, collections
import numpy as np
B = '/data/fmc/htr-routes/research/'
RUN = B + 'out/big/run1/'
BUD = int(sys.argv[1]) if len(sys.argv) > 1 else 2

def corner_class(key):            # 'H:4b2 2e > (4a1 4e > 0c0 0e) | ht' -> '4b2 > (4a1 > 0c0) | ht'
    k = key[2:]
    return re.sub(r' \d+e', '', k)

keys = {}
with open(RUN + 'route_keys.tsv') as f:
    next(f)
    for line in f:
        i, k = line.rstrip('\n').split('\t', 1)
        if k.startswith('H:'):
            keys[int(i)] = k
cls_id, cls_name, key2cls = {}, [], {}
for i, k in keys.items():
    c = corner_class(k)
    if c not in cls_id:
        cls_id[c] = len(cls_name); cls_name.append(c)
    key2cls[i] = cls_id[c]
print(len(keys), 'H keys,', len(cls_name), 'corner classes', file=sys.stderr)

size = collections.Counter()
for line in open(B + 'verify/out/cosets_per_label.tsv'):
    lab, n = line.split('\t')
    sub, e = lab.split()
    sub = '4c3' if sub in ('4a3', '4b3') else '4c4' if sub in ('4a4', '4b4') else sub
    size[f'{sub} {e}'] += int(n)

def load(cell):
    """per state: dict class -> (opt ok, p1 ok) at the budget"""
    rows = list(csv.DictReader(open(RUN + f'states_{cell.replace(" ", "_")}.tsv'), delimiter='\t'))
    raw = open(RUN + f'routes_{cell.replace(" ", "_")}.bin', 'rb').read()
    w = np.frombuffer(raw, dtype='<u8')
    pos = 0
    opt_pairs, p1_pairs = [], []
    for si, r in enumerate(rows):
        niss = int(r['htrNiss'])
        n = int(w[pos]); rec = w[pos + 1: pos + 1 + n]; pos += 1 + n
        n2 = int(w[pos]); pos += 1 + n2
        o, p = set(), set()
        for x in rec.tolist():
            kid = x >> 11
            if kid not in key2cls:
                continue
            hl, hany, delta = (x >> 6) & 31, (x >> 1) & 31, x & 1
            c = key2cls[kid]
            if delta == 0 and hl <= niss + BUD:
                o.add(c)
            if hany <= niss + BUD:
                p.add(c)
        opt_pairs += [(si, c) for c in o]
        p1_pairs += [(si, c) for c in p]
    assert pos == len(w)
    return len(rows), np.array(opt_pairs, dtype=np.int64), np.array(p1_pairs, dtype=np.int64)

def greedy(n, pairs, wt, steps=8):
    """pairs: (global state, class); wt: weight per state. Ties: linear first, then by name."""
    covered = np.zeros(n, bool)
    order, cum = [], []
    tot = wt.sum()
    for _ in range(steps):
        m = ~covered[pairs[:, 0]]
        g = np.bincount(pairs[m, 1], weights=wt[pairs[m, 0]], minlength=len(cls_name))
        best = g.max()
        if best <= 0:
            break
        cand = [c for c in np.flatnonzero(g >= best - 1e-9)]
        cand.sort(key=lambda c: ('(' in cls_name[c], cls_name[c]))
        c = cand[0]
        order.append(c)
        covered[pairs[pairs[:, 1] == c, 0]] = True
        cum.append(wt[covered].sum() / tot)
    return order, cum

def share(n, pairs, wt, classes):
    hit = np.zeros(n, bool)
    sel = np.isin(pairs[:, 1], classes)
    hit[pairs[sel, 0]] = True
    return wt[hit].sum() / wt.sum()

cells = sorted(size)
groups = collections.OrderedDict()
for c in cells:
    groups.setdefault(c.split()[0], []).append(c)
out = open(B + f'verify/out/recount_checklist_b{BUD}.tsv', 'w')
out.write('group\ttarget\tstep\tclass\tcumulative\n')
res = {}
for g, cs in groups.items():
    data = [load(c) for c in cs]
    offs = np.cumsum([0] + [d[0] for d in data])
    n = int(offs[-1])
    wt = np.concatenate([np.full(d[0], size[c] / d[0]) for c, d in zip(cs, data)])
    for name, sel in [(c, [i]) for i, c in enumerate(cs)] + [(g, list(range(len(cs))))]:
        op = np.concatenate([data[i][1] + [offs[i], 0] for i in sel])
        pp = np.concatenate([data[i][2] + [offs[i], 0] for i in sel])
        wsel = wt * np.isin(np.arange(n), np.concatenate([np.arange(offs[i], offs[i + 1]) for i in sel]))
        order, cum = greedy(n, op, wsel)
        p1_3 = share(n, pp, wsel, order[:3])
        res[name] = (order, cum, p1_3)
        for k, (c, v) in enumerate(zip(order, cum), 1):
            out.write(f'{name}\topt\t{k}\t{cls_name[c]}\t{v:.4f}\n')
        out.write(f'{name}\tp1_same3\t3\t\t{p1_3:.4f}\n')
    print(g, 'done', file=sys.stderr)
out.close()

# compare with the study's table
pub = collections.defaultdict(dict)
for r in csv.DictReader(open(B + 'out/q2_checklist_budget.tsv'), delimiter='\t'):
    if r['level'] == 'C' and r['target'] == 'opt' and r['budget'] == ('inf' if BUD >= 99 else str(BUD)):
        pub[r['group']][int(r['step'])] = (r['class'], float(r['cumulative']))
worst = 0
for name, (order, cum, p1_3) in res.items():
    diffs = []
    for k in range(min(5, len(order))):
        pc, pv = pub[name].get(k + 1, ('?', -1))
        same = pc == cls_name[order[k]]
        d = abs(pv - cum[k])
        worst = max(worst, d)
        if not same or d > 0.0005:
            diffs.append(f'step {k+1}: mine {cls_name[order[k]]} {cum[k]:.4f} / study {pc} {pv:.4f}')
    print(name, 'OK' if not diffs else '; '.join(diffs), f'| +1 with same 3: {p1_3:.4f}')
print('largest cumulative difference in the first 5 steps:', worst)
first = {g: res[g][1][0] for g in groups}
print('best single route per corner subset: from', round(100 * min(first.values()), 1), 'to', round(100 * max(first.values()), 1))
