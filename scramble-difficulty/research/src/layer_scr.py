"""Scramble level: do the three axes' flipped-layer-edge counts add to the bad-edge triple?  (held-out linear R^2)"""
import csv, math, numpy as np
from sklearn.linear_model import LinearRegression
AX = ['UD', 'FB', 'RL']; X = []; Xl = []; Y = []; B_ = []
for tag in ('uni', 'real', 'gen'):
    T = {r['id']: r for r in csv.DictReader(open(f'out/tgt_{tag}.tsv'), delimiter='\t')}
    F3 = {r['id']: r for r in csv.DictReader(open(f'out/feat3_{tag}.tsv'), delimiter='\t')}
    for r in csv.DictReader(open(f'out/feat_{tag}.tsv'), delimiter='\t'):
        t = T.get(r['id']); n10 = float(t['n10']) if t else 0; best = float(t['best']) if t else 27
        if best == 99: best = 27
        X.append(sorted(float(r[f'be_{e}']) for e in AX)); Xl.append(sorted(float(F3[r['id']][f'lg_{a}_Lb']) for a in AX))
        Y.append(math.log2(1 + n10)); B_.append(best)
X = np.array(X); Xl = np.array(Xl); Y = np.array(Y); B_ = np.array(B_); N = len(Y)
idx = np.random.default_rng(7).permutation(N); tr, te = idx[:int(0.67 * N)], idx[int(0.67 * N):]
def r2(y, p): return 1 - np.sum((y - p) ** 2) / np.sum((y - y.mean()) ** 2)
def rk(x):
    o = np.argsort(x, kind='mergesort'); r = np.empty(len(x)); r[o] = np.arange(len(x)); return r
for nm, y in (('DRs of <= 10 (log)', Y), ('best DR + finish', B_)):
    for lab, M in (('bad edges', X), ('flipped layer edges', Xl), ('both', np.hstack([X, Xl]))):
        p = LinearRegression().fit(M[tr], y[tr]).predict(M[te]); print(f'{nm}: {lab}: held-out R^2 {r2(y[te], p):.3f}')
print('Spearman(fewest flipped layer edges over the axes, DRs):', np.corrcoef(rk(Xl[:, 0]), rk(Y))[0, 1], ' Spearman(sum over axes, DRs):', np.corrcoef(rk(Xl.sum(1)), rk(Y))[0, 1])
print('Spearman(flipped sum, bad-edge sum):', np.corrcoef(rk(Xl.sum(1)), rk(X.sum(1)))[0, 1])
