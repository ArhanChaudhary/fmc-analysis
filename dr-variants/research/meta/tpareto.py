"""Reads ../out/meta/opt{K}.npz (topt.py) and lists, for each allowance of extra misses, the rules that finish the
fewest HTRs.  Extra misses are measured against "P <= 1 and the goal" with no cap and no floor, per corner case; the
work of a rule is its mean HTRs to finish per DR relative to that reference, as a geometric mean over the corner
cases.  0c3 (15 within-goal DRs) and 0c4 (66) are shown but don't steer the choice.
usage: tpareto.py K [maxcaps]"""
import sys
import numpy as np
from topt import CAPS
from tcommon import ORDER, path

K = int(sys.argv[1]); maxcaps = int(sys.argv[2]) if len(sys.argv) > 2 else K
z = np.load(path(f'opt{K}.npz'))
rules, miss, work = z['rules'], z['miss'], z['work']
big = [i for i, c in enumerate(ORDER) if c not in ('0c3', '0c4')]
ncap = (rules[:, :len(CAPS)] < 99).sum(axis=1)
ref = np.nonzero((ncap == 0) & (rules[:, len(CAPS)] == 0) & (rules[:, len(CAPS) + 1] == 0))[0][0]
dm = miss - miss[ref]
rel = work / work[ref]
gw = np.exp(np.log(rel[:, big]).mean(axis=1))
worst = dm[:, big].max(axis=1); mean = dm[:, big].mean(axis=1)

def name(i):
    r = rules[i]
    s = ', '.join(f'{CAPS[j]}≤{r[j]}' for j in range(len(CAPS)) if r[j] < 99)
    return f'floor {r[len(CAPS)]} spare≥{r[len(CAPS) + 1]} ' + (s or '(no cap)')
print('reference:', name(ref), ' miss', ' '.join(f'{c} {100 * miss[ref, i]:.1f}' for i, c in enumerate(ORDER)), ' work', ' '.join(f'{work[ref, i]:.0f}' for i in range(len(ORDER))))
for nc in range(0, maxcaps + 1):
    for lim in (0.0, 0.005, 0.01, 0.015, 0.02, 0.03, 0.05):
        ok = (ncap == nc) & (worst <= lim + 1e-9)
        if not ok.any(): continue
        idx = np.nonzero(ok)[0]
        o = idx[np.argsort(gw[idx])][:4]
        print(f'\n{nc} caps, worst extra miss ≤ {100 * lim:.1f} pts:')
        for i in o:
            print(f'  work ×{gw[i]:.3f}  mean +{100 * mean[i]:.2f}  {name(i):52s} | miss ' + ' '.join(f'{100 * miss[i, j]:4.1f}' for j in range(len(ORDER))) + ' | work ' + ' '.join(f'{work[i, j]:4.0f}' for j in range(len(ORDER))))
