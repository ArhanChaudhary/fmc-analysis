#!/usr/bin/env python3
"""Step 1: exact EO-kept DR distance per DRM with the variants (last EO turn free, both DR axes, normal or inverse),
compared with eo-to-dr's per-case table (out/c6_by_case.tsv of that study: plain, switch_last and two_axes exact there
too; normal_or_inverse sampled there on 10,000,000 states, exact here).  Output: out/variants_by_drm.tsv,
out/checks_variants.tsv."""
import os, sys, csv, math
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import pop, geom
F = pop.feat(); d = F['d'].astype(int)
OUT = pop.OUT
T = {k: pop.targets(k) for k in (5, 6, 7)}
rows = []
drms = sorted({(int(c), int(e)) for c, e in zip(F['drm_c'][::7], F['drm_e'][::7])} | {(0, 0)})
drms = sorted(set(zip(F['drm_c'].tolist(), F['drm_e'].tolist())))
cols = ['plain', 'lastF', 'lastFB', 'two', 'inv']
with open(os.path.join(OUT, 'variants_by_drm.tsv'), 'w') as f:
    f.write('drm\tcosets\tshare\tmean_d\t' + '\t'.join(f'{c}_le{k}' for c in cols for k in (5, 6, 7)) + '\n')
    for c, e in drms + [('all', 'all')]:
        m = np.ones(geom.N0, bool) if c == 'all' else pop.drm_mask(c, e)
        vals = [T[k][cn][m].mean() for cn in cols for k in (5, 6, 7)]
        name = 'all' if c == 'all' else pop.drm_name(c, e)
        f.write(f"{name}\t{m.sum()}\t{m.mean():.6f}\t{d[m].mean():.4f}\t" + '\t'.join(f'{v:.5f}' for v in vals) + '\n')
        rows.append((name, m.sum(), {(cn, k): T[k][cn][m].mean() for cn in cols for k in (5, 6, 7)}, d[m].mean()))
# compare with eo-to-dr
ref = {r['case']: r for r in csv.DictReader(open('/data/fmc/eo-to-dr/research/out/c6_by_case.tsv'), delimiter='\t')}
cmp = [('plain', 'plain'), ('lastF', 'switch_last'), ('two', 'two_axes'), ('inv', 'normal_or_inverse')]
worst = {}
for name, n, v, mean in rows:
    if name not in ref: continue
    r = ref[name]
    for mine, theirs in cmp:
        for k in (5, 6, 7):
            a = v[(mine, k)]; b = float(r[f'{theirs}_p_le{k}'])
            if theirs == 'normal_or_inverse':
                share = float(r['share']); nsamp = 1e7 * share
                se = math.sqrt(max(a * (1 - a), 1e-12) / max(nsamp, 1)); z = abs(a - b) / se if se > 0 else 0
                worst.setdefault(theirs, []).append((z, name, k, a, b))
            else:
                worst.setdefault(theirs, []).append((abs(a - b), name, k, a, b))
    worst.setdefault('mean', []).append((abs(mean - float(r['plain_mean'])), name, 0, mean, float(r['plain_mean'])))
with open(os.path.join(OUT, 'checks_variants.tsv'), 'w') as f:
    f.write('quantity\tcompared\tworst\tdrm\tk\tours\teo-to-dr\n')
    for q, lst in worst.items():
        w = max(lst)
        kind = 'z-score (their sample of 10,000,000)' if q == 'normal_or_inverse' else 'abs difference (both exact, theirs rounded to 5 significant digits)'
        f.write(f'{q}\t{len(lst)} cells, {kind}\t{w[0]:.3g}\t{w[1]}\t{w[2]}\t{w[3]:.5f}\t{w[4]:.5f}\n')
        print(f'{q:20s} {len(lst):4d} cells  worst {kind}: {w[0]:.3g} at {w[1]} k={w[2]} ours {w[3]:.5f} theirs {w[4]:.5f}')
for name, n, v, mean in rows:
    if name in ('4c4e', 'all', '4c2e', '3c2e', '7c8e'):
        print(name, n, f'mean {mean:.4f}', ' '.join(f'{c}:{v[(c, 6)]:.4f}' for c in cols))
