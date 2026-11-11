#!/usr/bin/env python3
"""Exact answers to specific questions asked on the server, from out/hand/*.csv."""
import csv, collections, math, sys
sys.path.insert(0, '/data/fmc/research/src')
from hand_kill import load, QT
def st(h):
    n = sum(h); m = sum(d*c for d, c in enumerate(h))/n
    return n, m, math.sqrt(max(sum(d*d*c for d, c in enumerate(h))/n - m*m, 0))
def P(h, T): return 100*sum(h[:T+1])/sum(h)
def add(a, b):
    for i, x in enumerate(b): a[i] += x

hdr, rows = load('h2_lengths.csv'); I = {n: i for i, n in enumerate(hdr)}
R = [(r[0], int(r[1]), int(r[2]), int(r[3]), int(r[4]), int(r[5]), int(r[6]), int(r[7])) for r in rows]  # sub,hmin,hmax,L,dLp,par,depth,count
subs = sorted({r[0] for r in R}, key=lambda s: (int(s.split()[0][-1]), s))
def group(keyf, want=lambda r: True):
    g = collections.defaultdict(lambda: [0]*19)
    for r in R:
        if want(r): g[keyf(r)][r[6]] += r[7]
    return g

print('## 1. Zagros: does corner case + HTR on both sides pin the optimal to sd ~0.25?  Does L + longer HTR predict within ~1 move?')
print('corner subset | sd of optimal | sd left: +edges(subset) | +HTR both | +L,longer HTR | +L,parity,HTR both | within 1 of the class median: L+longer HTR | all four')
for cs in ['0c0','4a1','4a2','4b2','0c3','2c3','4c3','0c4','2c4','4c4','2c5','4b5','ALL']:
    want = (lambda r: True) if cs == 'ALL' else (lambda r, cs=cs: r[0].split()[0] == cs)
    tot = [0]*19
    for h in group(lambda r: 0, want).values(): add(tot, h)
    N, m, sd = st(tot)
    def left(keyf):
        g = group(keyf, want); return math.sqrt(sum(st(h)[2]**2 * sum(h) for h in g.values())/N)
    def within1(keyf):
        g = group(keyf, want); ok = 0
        for h in g.values():
            n = sum(h); acc = 0
            for d, c in enumerate(h):
                acc += c
                if acc*2 >= n: med = d; break
            ok += sum(h[max(med-1, 0):med+2])
        return 100*ok/N
    print(f'{cs:5s} | {sd:.2f} | {left(lambda r: r[0]):.2f} | {left(lambda r: (r[0], r[1], r[2])):.2f} | {left(lambda r: (r[0], r[3], r[2])):.2f} | {left(lambda r: (r[0], r[1], r[2], r[3], r[4])):.2f} | {within1(lambda r: (r[0], r[3], r[2])):.1f}% | {within1(lambda r: (r[0], r[1], r[2], r[3], r[4])):.1f}%   [subset alone: {within1(lambda r: r[0]):.1f}%]')

print('\n## 2. Zagros throws away 4c3 that is 9+ to HTR on both sides (T11190)')
for name, want in [('4c3, HTR >= 9 on both sides', lambda r: r[0].startswith('4c3') and r[1] >= 9), ('4c3, the rest', lambda r: r[0].startswith('4c3') and r[1] < 9),
                   ('4c3, HTR <= 7 on at least one side', lambda r: r[0].startswith('4c3') and r[1] <= 7), ('4c3 all', lambda r: r[0].startswith('4c3'))]:
    h = [0]*19
    for x in group(lambda r: 0, want).values(): add(h, x)
    n, m, sd = st(h)
    print(f'  {name:36s} share of DRs {100*n/19508428800:5.2f}%  mean {m:.2f}  <=11 {P(h,11):5.2f}%  <=12 {P(h,12):5.2f}%  <=13 {P(h,13):5.1f}%  <=14 {P(h,14):5.1f}%')

print('\n## 3. Square tables: mean optimal / P(<=12)% by HTR length on the two sides (shorter side down, longer side across)')
for s in ['4b2 4e', '2c3 4e', '4c3 4e', '4c3 2e', '2c4 4e', '2c4 2e', '4c4 4e', '2c5 4e', '0c3 4e']:
    g = group(lambda r: (r[1], r[2]), lambda r, s=s: r[0] == s)
    tot = sum(sum(h) for h in g.values())
    hs = sorted({k[1] for k in g}); lo = sorted({k[0] for k in g})
    print(f'  {s}: share of the subset % | mean | P(<=12)%')
    print('   min\\max ' + ' '.join(f'{h:>17d}' for h in hs))
    for a in lo:
        cells = []
        for b in hs:
            h = g.get((a, b))
            cells.append(f'{100*sum(h)/tot:5.1f} {st(h)[1]:5.2f} {P(h,12):5.1f}' if h and sum(h) else ' '*17)
        print(f'   {a:7d} ' + ' '.join(cells))

print('\n## 4. count quackula: 4a1 4e bound (hN + hI - 1) vs the actual leave slice (D16164)')
h4 = [(r[0], int(r[1]), int(r[2]), int(r[3]), int(r[4])) for r in load('h4_htr_leaveslice.csv')[1]]
diff = collections.Counter()
for s, hn, hi, ls, c in h4:
    if s == '4a1 4e': diff[ls - (hn + hi - 1)] += c
n = sum(diff.values())
print('  leave slice minus bound: ' + '  '.join(f'{k:+d}: {100*v/n:.2f}%' for k, v in sorted(diff.items())) + f'   mean {sum(k*v for k,v in diff.items())/n:+.2f}')

print('\n## 5. Cost of the slice: optimal finish minus optimal leave slice (D7946)')
h3 = [(r[0], int(r[1]), int(r[2]), int(r[3])) for r in load('h3_leaveslice.csv')[1]]
for q in ['0qt', '1-2qt', '3qt', '4qt', '5qt', 'all']:
    dd = collections.Counter(); lsd = [0]*19
    for s, d, ls, c in h3:
        if q == 'all' or QT[s.split()[0]] == q: dd[d - ls] += c; lsd[ls] += c
    n = sum(dd.values())
    print(f'  {q:6s} mean leave slice {st(lsd)[1]:.2f}  ' + '  '.join(f'+{k}: {100*v/n:.1f}%' for k, v in sorted(dd.items())) + f'   mean +{sum(k*v for k,v in dd.items())/n:.2f}')

print('\n## 6. "Setup + HTR" bound G = max(hN + setup on inverse, hI + setup on normal): Levi at 1qt, trangium at 2qt, any qt')
h7 = [(r[0], int(r[1]), int(r[2]), int(r[3]), int(r[4])) for r in load('h7_setup_bound.csv')[1]]
print('  qt group | G below optimal by: fails (optimal < G) | exact | 1 | 2 | 3+ || mean G | mean max(hN,hI) | mean optimal | states where G > max(hN,hI)')
for q in ['1-2qt', '3qt', '4qt', '5qt']:
    dd = collections.Counter(); n = sg = sh = sdp = better = 0
    for s, hm, G, d, c in h7:
        if QT[s.split()[0]] != q: continue
        k = d - G; dd['fail' if k < 0 else min(k, 3)] += c; n += c; sg += G*c; sh += hm*c; sdp += d*c; better += c*(G > hm)
    print(f'  {q:6s} | {100*dd["fail"]/n:5.2f}% | {100*dd[0]/n:5.2f}% | {100*dd[1]/n:5.2f}% | {100*dd[2]/n:5.2f}% | {100*dd[3]/n:5.2f}% || {sg/n:.2f} | {sh/n:.2f} | {sdp/n:.2f} | {100*better/n:.1f}%')
print('  by subset (fails%):  ' + '  '.join(f'{s} {100*sum(c for x,hm,G,d,c in h7 if x==s and d<G)/sum(c for x,hm,G,d,c in h7 if x==s):.1f}' for s in subs if not s.startswith('0c0')))

print('\n## 7. Pairs: P(<=12)% and mean by number of true pairs (of 16), per corner subset')
h5 = [(r[0], int(r[1]), int(r[5]), int(r[6])) for r in load('h5_pairs.csv')[1]]
for cs in ['4b2', '2c3', '4c3', '2c4', '4c4', '2c5', '4b5']:
    g = collections.defaultdict(lambda: [0]*19)
    for s, tp, d, c in h5:
        if s.split()[0] == cs: g[min(tp, 6)][d] += c
    tot = sum(sum(h) for h in g.values())
    print(f'  {cs}: ' + ' | '.join(f'{k}{"+" if k==6 else ""} pairs: {100*sum(h)/tot:4.1f}% of DRs, mean {st(h)[1]:.2f}, <=12 {P(h,12):4.1f}%' for k, h in sorted(g.items())))
