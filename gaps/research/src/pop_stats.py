#!/usr/bin/env python3
"""Gap 1 (a): how the real DR population differs from uniform, per subset x edges and per corner subset.

Every DR of the population (big/pop_raw.tsv, labelled row by row in big/pop_label.tsv), no subsampling.
Populations: dr11 / dr10 (each DR of <= 11 / <= 10 moves counts once), scr11 / scr10 (each scramble counts once,
split equally over its DRs of that length).  Standard errors clustered by scramble.
Uniform: exact, from htr-routes out/checks/dist48.tsv (all 19,508,428,800 DR states).

Output: out/a_subsets.tsv  group, pop, share, se, uniform share, mean optimal, se, uniform mean, share opt <= 10/11/12
        (and uniform), mean leave-slice optimal
        out/a_depth.tsv    group, pop, depth, share (and uniform)
        out/a_overview.json  totals (scrambles, DRs, per scramble, side, length counts)"""
import json, collections
import numpy as np
G = '/data/fmc/gaps/research'
HR = '/data/fmc/htr-routes/research'

def wstat(x, w, cl):
    keep = w > 0; x, w, cl = np.asarray(x, float)[keep], w[keep], cl[keep]
    W = w.sum(); p = (w * x).sum() / W
    t = np.bincount(cl, weights=w * (x - p)); t = t[t != 0] if False else t
    K = len(np.unique(cl))
    return p, np.sqrt((t ** 2).sum() * K / max(K - 1, 1)) / W

def main():
    scr, ln, side = [], [], []
    with open(f'{G}/big/pop_raw.tsv') as f:
        for l in f:
            if l[0] == '#' or l.startswith('scr\t'): continue
            p = l.split('\t', 5); scr.append(int(p[0])); side.append(p[2] == 'I'); ln.append(int(p[3]))
    sub, d, lsd = [], [], []
    with open(f'{G}/big/pop_label.tsv') as f:
        next(f)
        for l in f:
            p = l.split('\t'); sub.append(p[0]); d.append(int(p[1])); lsd.append(int(p[2]))
    scr = np.array(scr); ln = np.array(ln); side = np.array(side); d = np.array(d); lsd = np.array(lsd)
    names = sorted(set(sub)); si = {s: i for i, s in enumerate(names)}; sub = np.array([si[s] for s in sub])
    nscr = scr.max() + 1
    n11 = np.bincount(scr, minlength=nscr).astype(float); n10 = np.bincount(scr[ln <= 10], minlength=nscr).astype(float)
    POPS = {'dr11': np.ones(len(scr)), 'scr11': 1 / n11[scr], 'dr10': (ln <= 10).astype(float),
            'scr10': np.where(ln <= 10, 1 / np.maximum(n10[scr], 1), 0)}
    # uniform, exact
    U = collections.defaultdict(lambda: np.zeros(19))
    for l in open(f'{HR}/out/checks/dist48.tsv').read().split('\n')[1:]:
        if l: s, dd, n = l.split('\t'); U[s][int(dd)] += int(n)
    order = list(U)
    tot = sum(v.sum() for v in U.values())
    cg = list(dict.fromkeys(s.split()[0] for s in order))
    groups = [(s, [s]) for s in order] + [(g, [s for s in order if s.split()[0] == g]) for g in cg]
    ov = {'scrambles': int(nscr), 'drs_le11': int(len(scr)), 'drs_le10': int((ln <= 10).sum()),
          'scrambles_with_le10': int((n10 > 0).sum()),
          'per_scramble_le11_mean': float(n11.mean()), 'per_scramble_le11_median': float(np.median(n11)),
          'per_scramble_le11_max': int(n11.max()), 'per_scramble_le10_mean': float(n10.mean()),
          'side_inverse_share_dr11': float(side.mean()),
          'length_counts': {int(k): int(v) for k, v in zip(*np.unique(ln, return_counts=True))}}
    fa = open(f'{G}/out/a_subsets.tsv', 'w'); fd = open(f'{G}/out/a_depth.tsv', 'w')
    fa.write('group\tpop\tn_drs\tshare\tse\tuniform_share\tmean_opt\tse_mean\tuniform_mean\t'
             'le10\tse_le10\tuniform_le10\tle11\tse_le11\tuniform_le11\tle12\tse_le12\tuniform_le12\tmean_ls\n')
    fd.write('group\tpop\tdepth\tshare\tuniform\n')
    for pop, w in POPS.items():
        for g, ss in groups:
            ing = np.isin(sub, [si[s] for s in ss if s in si])
            uh = sum(U[s] for s in ss); us = uh.sum() / tot; um = (uh * np.arange(19)).sum() / uh.sum()
            sh, se = wstat(ing, w, scr)
            m = ing & (w > 0)
            if m.sum() == 0:
                fa.write(f'{g}\t{pop}\t0\t0\t0\t{us:.5f}\n'); continue
            mm, mse = wstat(d[m], w[m], scr[m])
            line = f'{g}\t{pop}\t{m.sum()}\t{sh:.5f}\t{se:.5f}\t{us:.5f}\t{mm:.3f}\t{mse:.3f}\t{um:.3f}'
            for k in (10, 11, 12):
                p, pse = wstat(d[m] <= k, w[m], scr[m]); line += f'\t{p:.4f}\t{pse:.4f}\t{uh[:k + 1].sum() / uh.sum():.4f}'
            line += f'\t{(lsd[m] * w[m]).sum() / w[m].sum():.3f}'
            fa.write(line + '\n')
            h = np.bincount(d[m], weights=w[m], minlength=19); h = h / h.sum()
            for k in range(19):
                if h[k] > 0 or uh[k] > 0: fd.write(f'{g}\t{pop}\t{k}\t{h[k]:.5f}\t{uh[k] / uh.sum():.5f}\n')
        print(pop, flush=True)
    json.dump(ov, open(f'{G}/out/a_overview.json', 'w'), indent=1)
    print(ov)

if __name__ == '__main__':
    main()
