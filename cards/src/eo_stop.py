#!/usr/bin/env python3
"""Decision card "Should I stop looking for EOs and move to the next stage?".  On the EO-to-DR study's 50,000
uniformly random scrambles (eo-to-dr/research/out/big/scr50k.tsv, one row per scramble), take the best DR (EO plus
EO-keeping turns to a DR on either other axis; total length) through the EOs of at most 4 moves, and ask how often the
EOs of exactly 5 give a shorter one, and the EOs of 6 a shorter one than everything up to 5.  Two scopes: normal EOs
only, and normal + inverse + NISS EOs (a NISS EO takes its DR on the better side), all three EO axes.  The DRs are
the best that exist through each EO (computer only); what a solver can use is how the odds change with what the short
EOs already gave.

Output: cards/data/eo_stop.tsv.  usage: eo_stop.py"""
import csv, os, numpy as np
csv.field_size_limit(10**8)
HERE = os.path.dirname(os.path.abspath(__file__))
SRC = '/data/fmc/eo-to-dr/research/out/big/scr50k.tsv'
OUT = os.path.join(HERE, '..', 'data', 'eo_stop.tsv')
NONE = 99                     # no EO of that length or less on that axis/kind
r = csv.reader(open(SRC), delimiter='\t')
head = next(r); ix = {h: i for i, h in enumerate(head)}
keys = [(k, a, L) for k in 'nix' for a in ('RL', 'UD', 'FB') for L in range(7)]
A = np.array([[int(row[ix[f'best_{k}_{a}_{L}']]) for (k, a, L) in keys] for row in r])
def best(kinds, L):
    return A[:, [j for j, (k, a, l) in enumerate(keys) if k in kinds and l == L]].min(axis=1)
rows = []
for kinds, scope in (('n', 'normal'), ('nix', 'normal, inverse and NISS')):
    b4, b5, b6 = best(kinds, 4), best(kinds, 5), best(kinds, 6)
    groups = [('8 or less', b4 <= 8), ('9', b4 == 9), ('10', b4 == 10), ('11', b4 == 11), ('12 or more', (b4 >= 12) & (b4 < NONE)),
              ('no EO of 4 or less', b4 >= NONE), ('9 or less', b4 <= 9), ('10 or less', b4 <= 10), ('all', b4 >= 0)]
    def gain(m, a, b):                          # mean shortening, over the scrambles where both have a DR (else nan)
        k = m & (a < NONE) & (b < NONE)
        return float((a[k] - b[k]).mean()) if k.any() else float('nan')
    for name, m in groups:
        n = int(m.sum())
        rows.append(dict(scope=scope, best_le4=name, scrambles=n, share=n / len(b4),
                         five_better=float((b5[m] < b4[m]).mean()), five_gain=gain(m, b4, b5),
                         six_better=float((b6[m] < b5[m]).mean()), six_gain=gain(m, b5, b6)))
os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, 'w') as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0]), delimiter='\t'); w.writeheader()
    for x in rows: w.writerow({k: (f'{v:.6f}' if isinstance(v, float) else v) for k, v in x.items()})
print('wrote', OUT, len(rows), 'rows; max finite best:', int(A[A < NONE].max()))
