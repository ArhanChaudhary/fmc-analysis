"""Cost-weighted linear score: logistic regression with case weights (w[d] for good, 1 for bad), then the best
threshold; and a small-integer rounding of it."""
import numpy as np, sys, itertools
from lib import *
F['ccs'] = F['corner_case']*10+F['case_suffix']
def design(m, spec):
    """spec: list of (name, 'num'|'cat').  Returns X [n, p], column names."""
    idx = np.flatnonzero(m); cols = []; names = []
    for k, kind in spec:
        v = np.asarray(F[k])[idx].astype(float)
        if kind == 'num': cols.append(v); names.append(k)
        else:
            us = np.unique(v)
            for u in us[1:]: cols.append((v == u).astype(float)); names.append(f'{k}={int(u)}')
    return idx, np.stack(cols, 1), names
def fit(m, spec, K=6, iters=60, l2=1e-3):
    idx, X, names = design(m, spec)
    dd = d[idx]; w = weights(K)[dd]; y = (dd <= K).astype(float); sw = np.where(y == 1, w, 1.0)
    # aggregate identical rows
    key = np.ascontiguousarray(X).view([('', X.dtype)] * X.shape[1]).ravel()
    u, inv = np.unique(key, return_inverse=True)
    Xa = np.zeros((len(u), X.shape[1])); Xa[inv] = X
    pos = np.bincount(inv, weights=sw * y, minlength=len(u)); neg = np.bincount(inv, weights=sw * (1 - y), minlength=len(u))
    A = np.hstack([np.ones((len(u), 1)), Xa]); beta = np.zeros(A.shape[1])
    for _ in range(iters):
        z = A @ beta; p = 1 / (1 + np.exp(-z)); tot = pos + neg
        g = A.T @ (pos - tot * p) - l2 * beta; H = (A * (tot * p * (1 - p))[:, None]).T @ A + l2 * np.eye(A.shape[1])
        step = np.linalg.solve(H, g); beta += step
        if np.abs(step).max() < 1e-8: break
    score = np.hstack([np.ones((X.shape[0], 1)), X]) @ beta
    return idx, X, names, beta, score
def best_threshold(m, idx, score, K=6):
    dd = d[idx]; w = weights(K)[dd]
    order = np.argsort(-score); s = score[order]
    cum_bad = np.cumsum((dd[order] > K)); cum_w = np.cumsum(w[order]); totw = w.sum()
    loss = (totw - cum_w + cum_bad) / idx.size
    # only cut between distinct scores
    ok = np.r_[s[1:] != s[:-1], True]
    i = np.flatnonzero(ok)[np.argmin(loss[ok])]
    sw = np.zeros(N0, bool); sw[idx[order[:i + 1]]] = True
    return loss[i], s[i], sw
if __name__ == '__main__':
    m = drm_mask(4, 4)
    specs = {
     'pairs': [('pairs','num')],
     'pairs+side': [('pairs','num'),('side','num')],
     'pairs+side+fake': [('pairs','num'),('side','num'),('fake','num')],
     'pairs+side+fake+arm(cat)': [('pairs','num'),('side','num'),('fake','num'),('carm','cat'),('earm','cat')],
     'pairs+side+fake+arm+ccs': [('pairs','num'),('side','num'),('fake','num'),('carm','cat'),('earm','cat'),('ccs','cat')],
     'pairs+earm+ccs': [('pairs','num'),('earm','cat'),('ccs','cat')],
     'pairs(cat)+earm+ccs': [('pairs','cat'),('earm','cat'),('ccs','cat')],
     'big': [('pairs','num'),('side','num'),('fake','num'),('carm','cat'),('earm','cat'),('ccs','cat'),('hole_cfg','cat'),('edges_paired','cat'),('edges_same_layer','cat'),('ud_split','cat'),('pairs_out','num'),('side_rl','num'),('hole_bars','num'),('pair_over_hole','num'),('split_pairs','num'),('c_loose','num'),('e_naked','num')],
    }
    for name, spec in specs.items():
        idx, X, names, beta, score = fit(m, spec)
        L, thr, sw = best_threshold(m, idx, score)
        print(f'{name:28s}', fmt(profile(m, sw)))
        if len(names) <= 20: print('     ', ' '.join(f'{n}:{b:+.2f}' for n, b in zip(['1'] + names, beta)))
