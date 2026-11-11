#!/usr/bin/env python3
"""How much of the finish does each hand-readable quantity explain?  Reads out/hand/*.csv.

For every feature set F: share of the variance of the optimal finish explained by F (overall and inside each
subset), and the spread of P(finish <= 12) across the classes of F."""
import csv, collections, math, sys
D = '/data/fmc/research/out/hand/'

def load(name):
    with open(D + name) as f:
        r = csv.reader(f); hdr = next(r)
        return hdr, [row for row in r]

def explained(groups):
    """groups: key -> Counter(depth -> count).  Returns (N, total var, within var)."""
    N = S = S2 = 0; within = 0.0
    for h in groups.values():
        n = sum(h.values()); s = sum(d * c for d, c in h.items()); s2 = sum(d * d * c for d, c in h.items())
        N += n; S += s; S2 += s2
        within += s2 - s * s / n
    var = S2 / N - (S / N) ** 2
    return N, var, within / N

def report(label, rows, keyf, subf, depthf, cntf):
    allg = collections.defaultdict(collections.Counter); bysub = collections.defaultdict(lambda: collections.defaultdict(collections.Counter))
    subonly = collections.defaultdict(collections.Counter)
    for row in rows:
        c = cntf(row); d = depthf(row); s = subf(row)
        allg[(s, keyf(row))][d] += c; bysub[s][keyf(row)][d] += c; subonly[s][d] += c
    N, var, w = explained(allg)
    _, _, wsub = explained(subonly)
    print(f'{label:46s} classes {len(allg):7d}  explains {100*(1-w/var):5.1f}% of all variance, {100*(1-w/wsub):5.1f}% of what the subset leaves; sd left {math.sqrt(w):.3f}')
    return bysub

if __name__ == '__main__':
    hdr, rows = load('h2_lengths.csv')   # subset,hmin,hmax,L,dLp,parity,depth,count
    I = {n: i for i, n in enumerate(hdr)}
    cnt = lambda r: int(r[I['count']]); dep = lambda r: int(r[I['depth']]); sub = lambda r: r[I['subset']]
    N, var, _ = explained({0: collections.Counter({dep(r): 0 for r in rows})} if False else {'all': sum((collections.Counter({dep(r): cnt(r)}) for r in rows), collections.Counter())})
    print(f'all states {N}, sd of the optimal finish {math.sqrt(var):.3f}')
    report('subset alone', rows, lambda r: 0, sub, dep, cnt)
    report('+ E-slice parity', rows, lambda r: r[I['parity']], sub, dep, cnt)
    report('+ longer HTR (hmax)', rows, lambda r: r[I['hmax']], sub, dep, cnt)
    report('+ HTR both sides (hmin,hmax)', rows, lambda r: (r[I['hmin']], r[I['hmax']]), sub, dep, cnt)
    report('+ corner length L', rows, lambda r: r[I['L']], sub, dep, cnt)
    report('+ L and parity fit (Lp-L)', rows, lambda r: (r[I['L']], r[I['dLp']]), sub, dep, cnt)
    report('+ L, hmax', rows, lambda r: (r[I['L']], r[I['hmax']]), sub, dep, cnt)
    report('+ L, HTR both sides', rows, lambda r: (r[I['L']], r[I['hmin']], r[I['hmax']]), sub, dep, cnt)
    report('+ L, Lp-L, HTR both sides', rows, lambda r: (r[I['L']], r[I['dLp']], r[I['hmin']], r[I['hmax']]), sub, dep, cnt)
    hdr, rows = load('h1_coset.csv')     # coset,hI,depth,count
    cos = {r[0]: r for r in load('cosets.csv')[1]}   # coset,orbit,subset,...
    sub1 = lambda r: cos[r[0]][2]
    report('+ visible case (HTR coset, normal)', rows, lambda r: cos[r[0]][1], sub1, lambda r: int(r[2]), lambda r: int(r[3]))
    report('+ visible case and hI', rows, lambda r: (cos[r[0]][1], r[1]), sub1, lambda r: int(r[2]), lambda r: int(r[3]))
    hdr, rows = load('h5_pairs.csv')     # subset,true_pairs,pseudo_pairs,side_semi,top_semi,depth,count
    c5 = lambda r: int(r[6]); d5 = lambda r: int(r[5]); s5 = lambda r: r[0]
    report('+ true pairs', rows, lambda r: r[1], s5, d5, c5)
    report('+ true and pseudo pairs', rows, lambda r: (r[1], r[2]), s5, d5, c5)
    report('+ all four pair counts', rows, lambda r: (r[1], r[2], r[3], r[4]), s5, d5, c5)
    hdr, rows = load('h9_true_slice_pairs.csv')   # subset,true_pairs,slice_pairs,depth,count
    report('+ slice pairs', rows, lambda r: r[2], lambda r: r[0], lambda r: int(r[3]), lambda r: int(r[4]))
    report('+ true + slice pairs (sum)', rows, lambda r: int(r[1]) + int(r[2]), lambda r: r[0], lambda r: int(r[3]), lambda r: int(r[4]))
    hdr, rows = load('h3_leaveslice.csv')    # subset,depth,ls,count
    report('+ optimal leave slice (not hand-readable)', rows, lambda r: r[2], lambda r: r[0], lambda r: int(r[1]), lambda r: int(r[3]))
