#!/usr/bin/env python3
"""Print a rule's cross-table: each cell's share of the DRM, p(DR <= 6) on P1 (exact) and on the sampled attempts
P3_5 / P3_6 (switched states), and its label.  usage: explain.py <drm> <feature>[+<feature>...] [markdown]"""
import os, sys
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import pop
F = pop.feat(); d = F['d'].astype(int); P = pop.populations()
CASE = {0: 'a', 1: 'b', 2: 'c', 3: 'd', -1: '-'}
def fmt(f, v):
    if f in ('corner_case', 'arm_corner_case'): return CASE[int(v)]
    return str(int(v))
def table(drm, combo, md=False, k=6):
    c, e = (int(drm[0]), int(drm[2])) if len(drm) == 4 else (int(drm[0]), int(drm[2]))
    m = pop.drm_mask(c, e); y = d[m] <= k
    vals = np.stack([F[f][m] for f in combo], 1)
    u, inv = np.unique(vals, axis=0, return_inverse=True); inv = inv.reshape(-1)
    n = np.bincount(inv); pos = np.bincount(inv, weights=y)
    out = []
    for pn in ('P3_5', 'P3_6'):
        w = P[pn][m]; out.append((np.bincount(inv, weights=w), np.bincount(inv, weights=w * y)))
    lines = []
    hdr = combo + ['states', 'share', 'p<=%d P1' % k, 'P3_5', 'P3_6', 'label']
    lines.append('| ' + ' | '.join(hdr) + ' |'); lines.append('|' + '---|' * len(hdr))
    for i in range(len(u)):
        p = pos[i] / n[i]; lab = 'switch' if p > 0.5 else ('discard' if p < 0.1 else 'check')
        q = [f'{o[1][i] / o[0][i]:.3f} ({int(o[0][i])})' if o[0][i] else '-' for o in out]
        lines.append('| ' + ' | '.join([fmt(f, v) for f, v in zip(combo, u[i])] + [str(n[i]), f'{n[i] / m.sum():.3f}', f'{p:.3f}'] + q + [lab]) + ' |')
    return '\n'.join(lines)
if __name__ == '__main__':
    print(table(sys.argv[1], sys.argv[2].split('+')))
