#!/usr/bin/env python3
"""Gap 1: from the population (big/pop_raw.tsv + big/pop_label.tsv, row by row) to the states the route code runs on.

Populations (weightings), each a distribution over (scramble, DR) pairs:
  dr11   every DR of <= 11 moves found counts once (a scramble with 3,000 DRs weighs 3,000 times one with one)
  scr11  every scramble counts once, split equally over its DRs of <= 11 moves
  dr10, scr10   the same over DRs of <= 10 moves (scrambles without one drop out)
Sample: per subset x edges, up to CAP DRs drawn uniformly without replacement from the pooled <= 11 DRs of that cell
(seed SEED).  Each sampled DR carries the Horvitz-Thompson weight of every population: (population weight of the DR)
x (pool size of the cell) / (sample size of the cell), so a weighted mean over the sample estimates the population
mean; DRs of <= 10 moves in the sample are a uniform sample of the cell's <= 10 pool, so the same weights serve dr10
and scr10.

Outputs (big/real/):
  list.txt     "c e s" per sampled DR (the side's own state), grouped by cell; htrtools (gaps fork) GAPS_STATES input:
               state i of a subset there = the i-th line of that subset here
  meta.tsv     subset, i, pop row, scr, len, side, eolen, w_dr11, w_scr11, w_dr10, w_scr10
  pool.tsv     per cell: pooled counts and population weights (all DRs, not the sample): n11, n10, scr11, scr10 (sum
               of per-scramble weights), and the optimal-finish histogram under each population (for part a)
usage: make_sample.py [CAP] [SEED]"""
import sys, os, collections
import numpy as np
B = '/data/fmc/gaps/research/big'
CAP = int(sys.argv[1]) if len(sys.argv) > 1 else 25000
SEED = int(sys.argv[2]) if len(sys.argv) > 2 else 20261113

def load():
    scr, ln, side, eol, ces = [], [], [], [], []
    with open(f'{B}/pop_raw.tsv') as f:
        for l in f:
            if l[0] == '#' or l.startswith('scr\t'): continue
            p = l.split('\t')
            scr.append(int(p[0])); side.append(p[2] == 'I'); ln.append(int(p[3])); eol.append(int(p[4]))
            ces.append(f'{p[6]} {p[7]} {p[8]}')
    sub, d, lsd = [], [], []
    with open(f'{B}/pop_label.tsv') as f:
        next(f)
        for l in f:
            p = l.split('\t'); sub.append(p[0]); d.append(int(p[1])); lsd.append(int(p[2]))
    assert len(sub) == len(scr), (len(sub), len(scr))
    return (np.array(scr), np.array(ln), np.array(side), np.array(eol), ces, np.array(sub), np.array(d), np.array(lsd))

def main():
    scr, ln, side, eol, ces, sub, d, lsd = load()
    N = len(scr); nscr = scr.max() + 1
    n11 = np.bincount(scr, minlength=nscr).astype(float)
    n10 = np.bincount(scr[ln <= 10], minlength=nscr).astype(float)
    wd11 = np.ones(N); ws11 = 1.0 / n11[scr]
    is10 = ln <= 10
    wd10 = is10.astype(float); ws10 = np.where(is10, 1.0 / np.maximum(n10[scr], 1), 0.0)
    subs = sorted(set(sub))
    os.makedirs(f'{B}/real', exist_ok=True)
    rng = np.random.default_rng(SEED)
    order = np.argsort(sub, kind='stable')
    with open(f'{B}/real/pool.tsv', 'w') as fp:
        fp.write('subset\tpop\tweight\tn_rows\t' + '\t'.join(f'd{k}' for k in range(19)) + '\tlsd_mean\n')
        for s in subs:
            idx = np.nonzero(sub == s)[0]
            for pname, w in (('dr11', wd11), ('scr11', ws11), ('dr10', wd10), ('scr10', ws10)):
                ww = w[idx]; h = np.bincount(d[idx], weights=ww, minlength=19)
                lm = (lsd[idx] * ww).sum() / ww.sum() if ww.sum() > 0 else float('nan')
                fp.write(f'{s}\t{pname}\t{ww.sum():.6f}\t{(ww > 0).sum()}\t' + '\t'.join(f'{x:.6f}' for x in h) + f'\t{lm:.4f}\n')
    with open(f'{B}/real/list.txt', 'w') as fl, open(f'{B}/real/meta.tsv', 'w') as fm:
        fl.write(f'# make_sample.py CAP={CAP} SEED={SEED}: per subset x edges up to CAP DRs of the pool, uniform without replacement\n')
        fm.write('subset\ti\trow\tscr\tlen\tside\teolen\tw_dr11\tw_scr11\tw_dr10\tw_scr10\n')
        tot = 0
        for s in subs:
            idx = np.nonzero(sub == s)[0]
            k = min(CAP, len(idx))
            pick = np.sort(rng.choice(idx, size=k, replace=False))
            f = len(idx) / k
            for i, r in enumerate(pick):
                fl.write(ces[r] + '\n')
                fm.write(f'{s}\t{i}\t{r}\t{scr[r]}\t{ln[r]}\t{"I" if side[r] else "N"}\t{eol[r]}\t{wd11[r] * f:.6g}\t{ws11[r] * f:.6g}\t{wd10[r] * f:.6g}\t{ws10[r] * f:.6g}\n')
            tot += k
            print(s, len(idx), k, flush=True)
    print('sampled', tot, 'of', N)

if __name__ == '__main__':
    main()
