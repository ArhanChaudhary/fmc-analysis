#!/usr/bin/env python3
"""Gap 2: true optimum (any face turns) vs DR-group optimum vs leave-slice optimum.

Inputs (g2_solve.py outputs, columns: subset, idx, c, e, s, d, lsd, dvar, scramble, true_opt, shorter solution):
  big/g2/uni1000.out   the first 1,000 uniform states of every subset x edges of htr-routes' main pass
  big/g2/real.out      up to 500 states per subset x edges of the real-population sample (big/real/meta.tsv), with
                       that sample's population weights scaled to the subsample
Pooled groups (corner subset, all): uniform weighted by exact subset size, real by population weight; SE clustered
by scramble for the real population.
Output: out/g2.tsv (group, pop, n, share shorter, se, share shorter by 1, by 2+, mean gain, se, mean DR optimum,
        mean true optimum, mean leave-slice, share true optimum < leave-slice optimum, share true <= leave slice)"""
import sys, csv, collections
import numpy as np
sys.path.insert(0, '/data/fmc/gaps/research/src')
from real_analysis import wstat, SUBS, SIZE, CORNER, CGROUPS, meta
G = '/data/fmc/gaps/research'

def load(p):
    rows = [l.rstrip('\n').split('\t') for l in open(p)]
    return rows

def main():
    out = open(f'{G}/out/g2.tsv', 'w')
    out.write('group\tpop\tn\tshorter\tse\tby1\tby2plus\tmean_gain\tse_gain\tmean_dr_opt\tmean_true_opt\tmean_ls\ttrue_lt_ls\ttrue_le_ls\tclusters\n')
    sets = []
    U = load(f'{G}/big/g2/uni1000.out')
    nU = collections.Counter(r[0] for r in U)
    sets.append(('uniform', U, lambda r: SIZE[r[0]] / nU[r[0]], lambda r: SUBS.index(r[0]) * 10 ** 7 + int(r[1])))
    try:
        R = load(f'{G}/big/g2/real.out')
        M = meta(); nR = collections.Counter(r[0] for r in R)
        for pop in ('dr11', 'scr11', 'dr10', 'scr10'):
            sets.append((pop, R, (lambda pop: lambda r: M[r[0]]['w_' + pop][int(r[1])] * len(M[r[0]]['scr']) / nR[r[0]])(pop),
                         lambda r: int(M[r[0]]['scr'][int(r[1])])))
    except FileNotFoundError:
        pass
    for pop, rows, wf, cf in sets:
        by = collections.defaultdict(list)
        for r in rows: by[r[0]].append(r)
        for g, subs in [(s, [s]) for s in SUBS] + [(g, [s for s in SUBS if CORNER(s) == g]) for g in CGROUPS] + [('all', SUBS)]:
            rs = [r for s in subs for r in by[s]]
            if not rs: continue
            d = np.array([int(r[5]) for r in rs]); ls = np.array([int(r[6]) for r in rs]); t = np.array([int(r[9]) for r in rs])
            w = np.array([wf(r) for r in rs]); cl = np.array([cf(r) for r in rs])
            if w.sum() <= 0: continue
            gain = d - t
            p, se, K = wstat(gain > 0, w, cl); mg, mse, _ = wstat(gain, w, cl)
            f = lambda x: (w * x).sum() / w.sum()
            out.write(f'{g}\t{pop}\t{(w > 0).sum()}\t{p:.4f}\t{se:.4f}\t{f(gain == 1):.4f}\t{f(gain >= 2):.4f}\t{mg:.4f}\t{mse:.4f}\t'
                      f'{f(d):.3f}\t{f(t):.3f}\t{f(ls):.3f}\t{f(t < ls):.4f}\t{f(t <= ls):.4f}\t{K}\n')
    out.close()

if __name__ == '__main__':
    main()
