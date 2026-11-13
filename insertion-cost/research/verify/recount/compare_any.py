#!/usr/bin/env python3
"""Written-order best (study column) against the best over every rewriting of the skeleton (opposite-face pairs
in either order, for both comms).  usage: compare_any.py res_dir"""
import sys, glob, os
from collections import Counter
R = sys.argv[1]
def num(x):
    if x in ('inf', 'na', 'nc'): return None
    x = int(x); return x - 2**64 if x >= 2**63 else x
for f in sorted(glob.glob(R + '/any_*.out')):
    rows = [l.split('\t') for l in open(f).read().split('\n')[1:] if l]
    a = [(r[0], num(r[1]), num(r[2])) for r in rows]
    worse = [x for x in a if x[1] is not None and x[2] is not None and x[1] > x[2]]
    better = [x for x in a if (x[1] is not None and x[2] is None) or (x[1] is not None and x[2] is not None and x[1] < x[2])]
    gain = Counter(('fits now' if w is None else w - v) for _, v, w in better)
    fa = [v for _, v, w in a if v is not None]; fw = [w for _, v, w in a if w is not None]
    both = [(v, w) for _, v, w in a if v is not None and w is not None]
    print(f'{os.path.basename(f)}: rows {len(a)}; any-order worse than written {len(worse)} (must be 0); strictly better on {len(better)} ({100*len(better)/len(a):.2f}%), by {dict(gain)}')
    print(f'   mean written order {sum(fw)/len(fw):.4f} over {len(fw)}; any order {sum(fa)/len(fa):.4f} over {len(fa)}; on the {len(both)} where both fit: {sum(w for v, w in both)/len(both):.4f} vs {sum(v for v, w in both)/len(both):.4f}')
    print('   first better rows (idx, any, written):', better[:8])
