#!/usr/bin/env python3
"""Step 3: the three populations per DRM.  For the state the solver sees after the switch (W = T^-1, T the RZP's end
state) and, for comparison, for T itself (continuing on the same side):
  P1 uniform; P2 exact RZP weights (RZP length 1..6 from a uniform EO-solved state, eoswtools rzp); P3 sampled
  attempts (6,000 uniform scrambles, every EO <= 6 on 3 axes x 2 sides x 2 DR axes, every RZP, total length 4/5/6).
Test of the switch theorem: given its class (twist counts, E pieces out), W is uniform; so P3's switched sub-7 rate
must equal the P1 class rates averaged over P3's own class mix.  Output: out/populations.tsv, out/checks_switch_uniform.tsv."""
import os, sys, math
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import pop
F = pop.feat(); d = F['d'].astype(int); P = pop.populations()
key = pop.cls_key(F)
def rate(w, m, k=6):
    tw = w[m].sum()
    return (float((w[m] * (d[m] <= k)).sum() / tw) if tw else float('nan')), tw
lines = ['drm\tpopulation\tside\tL\tweight_or_attempts\tp_le5\tp_le6\tp_le7\tp_le_11minusL\tmean_d']
chk = ['drm\tL\tattempts\tP3_switched_p_le6\tpredicted_from_class_mix\tz_20_batches\tP3_normal_p_le6\tP1_p_le6']
cls_p1 = {k: np.bincount(key, weights=(d <= k).astype(float), minlength=405) / np.maximum(np.bincount(key, minlength=405), 1) for k in (5, 6, 7)}
worst = 0
BT = np.fromfile(os.path.join(pop.BIG, 'att_batches.u64'), dtype='<u8').reshape(20, 3, 405, 16).astype(float)
for c, e in pop.DRMS_NAMED:
    m = pop.drm_mask(c, e)
    def row(name, side, L, w):
        vals = [rate(w, m, k)[0] for k in (5, 6, 7)]
        kk = 11 - L if L else 6
        v11 = rate(w, m, kk)[0]
        tw = w[m].sum(); md = float((w[m] * d[m]).sum() / tw) if tw else float('nan')
        lines.append(f"{pop.drm_name(c, e)}\t{name}\t{side}\t{L}\t{tw:.6g}\t" + '\t'.join(f'{v:.5f}' for v in vals) + f'\t{v11:.5f}\t{md:.4f}')
    row('P1', 'any', 0, P['P1'])
    for L in range(1, 7):
        row('P2', 'switched', L, P[f'P2_{L}']); row('P2', 'same side', L, P[f'P2n_{L}'])
    for L in (4, 5, 6):
        row('P3', 'switched', L, P[f'P3_{L}']); row('P3', 'same side', L, P[f'P3n_{L}'])
        w = P[f'P3_{L}']; n = w[m].sum()
        if n == 0: continue
        obs = float((w[m] * (d[m] <= 6)).sum() / n)
        pred = float((w[m] * cls_p1[6][key[m]]).sum() / n)
        # attempts are clustered by scramble (about 20,000 per scramble): the error comes from 20 batches of 300 scrambles
        cm = np.zeros(405, bool); cm[np.unique(key[m])] = True
        B = BT[:, L - 4][:, cm]                               # [batch][class][d]
        nb = B.sum((1, 2)); ob = B[:, :, :7].sum((1, 2)) / nb
        pb = (B.sum(2) * cls_p1[6][cm][None, :]).sum(1) / nb
        diff = ob - pb; se = diff.std(ddof=1) / math.sqrt(len(diff))
        z = (obs - pred) / se if se > 0 else 0.0
        worst = max(worst, abs(z))
        chk.append(f"{pop.drm_name(c, e)}\t{L}\t{int(n)}\t{obs:.5f}\t{pred:.5f}\t{z:.2f}\t{rate(P[f'P3n_{L}'], m)[0]:.5f}\t{rate(P['P1'], m)[0]:.5f}")
open(os.path.join(pop.OUT, 'populations.tsv'), 'w').write('\n'.join(lines) + '\n')
open(os.path.join(pop.OUT, 'checks_switch_uniform.tsv'), 'w').write('\n'.join(chk) + '\n')
print('\n'.join(chk)); print('worst |z|', round(worst, 2))

# The RZP's last quarter turn either way gives the same switched coset (a DR-group premove on the inverse keeps the
# coset): checked on every pair of example attempts (out/big/att_examples.tsv, the first 40 scrambles).
import csv, collections
g = collections.defaultdict(set)
for r in csv.DictReader(open(os.path.join(pop.BIG, 'att_examples.tsv')), delimiter='\t'):
    rz = r['rzp'].split()
    if not rz or rz[-1].endswith('2'): continue
    g[(r['scr'], r['side'], r['eo_axis'], r['dr_axis'], r['eo'], ' '.join(rz[:-1]), rz[-1][0])].add(r['ix_switched'])
same = sum(1 for v in g.values() if len(v) == 1)
open(os.path.join(pop.OUT, 'checks_last_rzp_turn.txt'), 'w').write(f'{same}\t{len(g)}\tpairs of attempts differing only in the direction of the RZP\'s last quarter turn with the same switched coset\n')
print('last RZP turn either way, same switched coset:', same, 'of', len(g))
