#!/usr/bin/env python3
"""Step 4a: grade every rule of rules.py on each population: share switched, precision (target among switched),
recall (switched among target), target states discarded (share of all), Rodney's score p*N.  Populations: P1 uniform
(exact), P2_5 (switched after an RZP of length 5, exact), P3_5 and P3_6 (sampled attempts at total length 5, 6).
The target is DR <= k (k = 6, "sub-7", unless the rule says otherwise).  Output: out/grades.tsv."""
import os, sys
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import pop, rules
F = pop.feat(); d = F['d'].astype(int); P = pop.populations()
POPS = [('P1', P['P1']), ('P2_5', P['P2_5']), ('P3_5', P['P3_5']), ('P3_6', P['P3_6'])]
def grade(mask_drm, sw, k, w):
    w = w[mask_drm]; y = (d[mask_drm] <= k); s = sw[mask_drm]
    tot = w.sum(); ny = (w * y).sum(); ns = (w * s).sum(); nys = (w * y * s).sum()
    return dict(share=ns / tot, prec=nys / ns if ns else float('nan'), recall=nys / ny if ny else float('nan'),
                lost=(ny - nys) / tot, base=ny / tot, total_hit=nys / tot)
out = ['id\tdrm\tsource\trule\ttarget\tpopulation\tbase_rate\tshare_switched\tprecision\trecall\ttarget_states_discarded\tswitched_and_hit\tscore_pN_states']
for rid, (c, e), src, text, f, k in rules.RULES:
    m = pop.drm_mask(c, e); sw = np.asarray(f(F), bool)
    for pn, w in POPS:
        g = grade(m, sw, k, w)
        score = g['prec'] * g['total_hit'] * m.sum() if pn == 'P1' else float('nan')
        out.append(f"{rid}\t{c}c{e}e\t{src}\t{text}\tDR<={k}\t{pn}\t{g['base']:.9f}\t{g['share']:.9f}\t{g['prec']:.9f}\t{g['recall']:.9f}\t{g['lost']:.9f}\t{g['total_hit']:.9f}\t{score:.0f}")
open(os.path.join(pop.OUT, 'grades.tsv'), 'w').write('\n'.join(out) + '\n')
import csv
rows = list(csv.DictReader(open(os.path.join(pop.OUT, 'grades.tsv')), delimiter='\t'))
for r in rows:
    if r['population'] == 'P1':
        r3 = next(x for x in rows if x['id'] == r['id'] and x['population'] == 'P3_5')
        print(f"{r['id']:22s} {r['drm']} {r['target']}  share {float(r['share_switched']):.3f} prec {float(r['precision']):.3f} recall {float(r['recall']):.3f} lost {float(r['target_states_discarded']):.4f} | P3_5 share {float(r3['share_switched']):.3f} prec {float(r3['precision']):.3f}")
