#!/usr/bin/env python3
"""Summaries from the independent per-row values (column `mine`, moves added; inf = nothing fits)."""
import sys, os, glob
from decimal import Decimal, ROUND_HALF_EVEN
R = sys.argv[1]
def load(f):
    rows = [l.split('\t') for l in open(f).read().split('\n')[1:] if l]
    return rows
def num(x):
    if x in ("inf", "na", "nc"): return None
    x = int(x); return x - 2**64 if x >= 2**63 else x   # runs before the signed fix wrote x - n as an unsigned number
for f in sorted(glob.glob(R + '/*.out')):
    name = os.path.basename(f)[:-4]; n = int(name.rsplit('_n', 1)[1])
    rows = load(f)
    mism = [r for r in rows if num(r[1]) != num(r[2])]
    sol = sum(r[3] == 'ok' for r in rows); bad = sum(r[3] == 'BAD' for r in rows)
    v = [num(r[1]) for r in rows]; fin = [x for x in v if x is not None]
    mean = Decimal(sum(fin)) / len(fin) if fin else None
    m2 = mean.quantize(Decimal('0.01'), ROUND_HALF_EVEN) if mean is not None else None
    m3 = mean.quantize(Decimal('0.0001')) if mean is not None else None
    N = len(v)
    def share(pred): return 100 * sum(1 for x in v if pred(x)) / N
    print(f'{name}: rows {N}, mismatches {len(mism)}, study solutions replayed ok {sol} bad {bad}, nothing fits {N-len(fin)}, mean {m2} ({m3}, over {len(fin)})')
    for r in mism[:10]: print('   MISMATCH idx', r[0], 'mine', num(r[1]), 'study', r[2])
    tot = lambda x: None if x is None else x + n
    fs = lambda k: sum(1 for x in fin if x <= k); print(f'   over the {len(fin)} where something fits: +4 or better {100*fs(4)/max(1,len(fin)):.3f}%  +5 {100*fs(5)/max(1,len(fin)):.3f}%  +6 {100*fs(6)/max(1,len(fin)):.3f}%')
    print(f'   sub-30 (total<=29): {share(lambda x: x is not None and x + n <= 29):.3f}%')
    from collections import Counter
    c = Counter(tot(x) for x in v); print('   totals:', sorted((k, c[k]) for k in c if k is not None)[:20], 'none', c[None])
    for k in (4, 5, 6): print(f'   +{k} or better {share(lambda x: x is not None and x <= k):.3f}%', end='')
    print()
    for k in (9, 11, 12, 13): print(f'   +{k} or worse {share(lambda x: x is None or x >= k):.3f}% (finite only {share(lambda x: x is not None and x >= k):.3f}%)', end='')
    print()
