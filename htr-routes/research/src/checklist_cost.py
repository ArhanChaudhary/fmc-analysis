#!/usr/bin/env python3
"""The checklist with a cost: the main deliverable of question 2.

Every finish has a linear reading on each side, so "some optimal follows route class X" says nothing about NISS:
a NISS reading of a finish is also a linear finish.  What NISS changes is how long the HTR is that the solver has
to find.  So a class is graded with an HTR budget: it "works with budget k" on a state if some optimal finish has a
reading in the class whose HTR (moves until the cube is in HTR, both sides counted) is at most the state's shortest
NISS HTR + k.  k = 0 means "only the shortest HTRs", k = 2 "HTRs up to two moves longer than the shortest";
k = inf is the plain class.

Classes: level C (corner subsets at the start and after each quarter turn up to HTR, the switch marked, post-HTR in
half turns or not) and level Q (quarter turns on each side only).  Greedy cover per corner subset (edge counts pooled,
weighted by exact size) and per subset x edges; targets optimal and optimal + 1.
Ties (classes covering exactly the same extra states) are broken by common.tie_rank: linear first, then the
normal-first member of a mirror pair (the reading of the same split started on normal), then the name; the number of
tied classes and the chosen class's mirror alias are written out.
+1 uses htr1 (the shortest HTR over every finish of the route within optimal + 1), not the optimal finishes' HTR.
Output: out/q2_checklist_budget.tsv (group, level, target, budget, step, class, marginal, cumulative, alone,
tied_classes, mirror_alias), out/route_aliases_C.tsv."""
import collections, time
import numpy as np
from common import *

K = keys()
cache = {lv: {} for lv in ('C', 'Q')}
names = {lv: [] for lv in ('C', 'Q')}
ids = {lv: {} for lv in ('C', 'Q')}
def cls(rid, lv):
    c = cache[lv].get(rid)
    if c is None:
        k = K[rid]
        if k[0] != 'H': c = -1
        else:
            n = level_of(k, lv)
            c = ids[lv].get(n)
            if c is None: c = ids[lv][n] = len(names[lv]); names[lv].append(n)
        cache[lv][rid] = c
    return c

BUDGETS = [0, 1, 2, 99]
def member(sub):
    st = load_states(sub); rt = Routes(sub)
    u, inv = np.unique(rt.rid, return_inverse=True)
    out = {}
    niss = st['htrNiss'][rt.state]
    for lv in ('C', 'Q'):
        c = np.array([cls(int(x), lv) for x in u])[inv]
        for tg in ('opt', 'p1'):
            for b in BUDGETS:
                # optimum: an optimal finish of the route with HTR <= niss + b; +1: any finish <= opt + 1 (htr1)
                if tg == 'opt': m = (c >= 0) & (rt.delta == 0) & (rt.htr <= niss + b)
                else: m = (c >= 0) & (rt.htr1 <= niss + b)
                pair = np.unique(rt.state[m] * (1 << 24) + c[m])
                out[(lv, tg, b)] = (pair >> 24, pair & ((1 << 24) - 1))
    return rt.n, out

NF = {lv: set() for lv in ('C', 'Q')}      # class names that occur as the normal-first member of a mirror pair
MIRROR = {lv: {} for lv in ('C', 'Q')}
def load_aliases():
    mirror, nf = aliases()
    pairs = collections.Counter()
    for a, b in mirror.items():
        if a in nf:
            for lv in ('C', 'Q'):
                ca, cb = level_of(K[a], lv), level_of(K[b], lv)
                if ca != cb:
                    NF[lv].add(ca); MIRROR[lv].setdefault(ca, cb); MIRROR[lv].setdefault(cb, ca)
                    if lv == 'C': pairs[(ca, cb)] += 1
    with open(f'{OUT}/route_aliases_C.tsv', 'w') as f:
        f.write('normal_first_class\tinverse_first_class\troute_key_pairs\n')
        for (a, b), n in pairs.most_common():
            f.write(f'{a}\t{b}\t{n}\n')

def greedy(si, ci, w, lv, steps=8):
    """weighted greedy cover; ties (equal gain) broken by tie_rank: linear first, then the normal-first member of a
    mirror pair, then the name"""
    W = w.sum(); covered = np.zeros(len(w), bool); res = []; cum = 0.0
    alone = np.bincount(ci, weights=w[si])
    for _ in range(steps):
        m = ~covered[si]
        g = np.bincount(ci[m], weights=w[si[m]])
        if not len(g) or g.max() <= 0: break
        top = np.nonzero(g >= g.max() - 1e-9)[0]
        b = int(min(top, key=lambda c: tie_rank(names[lv][c], NF[lv])))
        cum += g[b]
        res.append((b, g[b] / W, cum / W, alone[b] / W, len(top)))
        covered[si[ci == b]] = True
    return res

def main():
    t0 = time.time()
    f = open(f'{OUT}/q2_checklist_budget.tsv', 'w')
    load_aliases()
    f.write('group\tlevel\ttarget\tbudget\tstep\tclass\tmarginal\tcumulative\talone\ttied_classes\tmirror_alias\n')
    for g in CGROUPS:
        subs = [s for s in SUBS if CORNER(s) == g]
        mem = []
        for s in subs:
            n, out = member(s); mem.append((s, n, out))
        groups = [(s, [(s, n, out)]) for s, n, out in mem] + ([(g, mem)] if len(mem) > 1 else [])
        for gname, ms in groups:
            w = np.concatenate([np.full(n, SIZE[s] / n) for s, n, _ in ms])
            for key in ms[0][2]:
                lv, tg, b = key
                offs = 0; S = []; C = []
                for s, n, out in ms:
                    S.append(out[key][0] + offs); C.append(out[key][1]); offs += n
                si = np.concatenate(S); ci = np.concatenate(C)
                for i, (c, marg, cum, al, nt) in enumerate(greedy(si, ci, w, lv)):
                    f.write(f'{gname}\t{lv}\t{tg}\t{"inf" if b == 99 else b}\t{i + 1}\t{names[lv][c]}\t{marg:.4f}\t{cum:.4f}\t{al:.4f}\t{nt}\t{MIRROR[lv].get(names[lv][c], "")}\n')
        f.flush()
        print(g, f'{time.time() - t0:.0f}s', flush=True)

if __name__ == '__main__':
    main()
