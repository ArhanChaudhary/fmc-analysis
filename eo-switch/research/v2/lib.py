"""v2 analysis library: cost-weighted grading of switch policies on the exact table.
State space: F/B EO, DR on U/D, 1,082,565 cosets; d = exact EO-kept distance to DR (out/big/d.u8)."""
import os, sys
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'src'))
_f = np.load(os.path.join(HERE, '..', 'out', 'big', 'feat.npz'))
_r = np.load(os.path.join(HERE, '..', 'out', 'big', 'rings.npz'))
F = {k: _f[k] for k in _f.files}
for k in ('sigma', 'qsig', 'hbar', 'swaps', 'slot', 'cls'):
    F[k] = _r[k]
_x = os.path.join(HERE, 'out', 'feat2.npz')
if os.path.exists(_x):
    _g = np.load(_x)
    for k in _g.files: F[k] = _g[k]
d = F['d'].astype(np.int64)
N0 = d.size
DRMS = [(4, 4), (4, 2), (3, 2), (7, 8), (8, 8), (2, 2), (4, 6), (3, 4), (3, 6), (5, 4), (5, 6), (6, 6)]
def drm_mask(c, e): return (F['drm_c'] == c) & (F['drm_e'] == e)

# ---- the loss: a wasted switch (d >= K+1) costs 1; a declined d-mover costs W[d]
def weights(K=6, w6=3.0, rho=3.0):
    """w[d] for d = 0..10: cost of declining a case that is d from DR, in wasted switches. K = longest DR that counts
    as good (6 after a 5-move RZP).  Lengths K-2 and shorter share one class."""
    w = np.zeros(11)
    for dd in range(11):
        if dd <= K: w[dd] = w6 * rho ** min(K - dd, 2)
    return w
def profile(m, sw, K=6, w=None):
    """Grade the switch mask sw on the population mask m.  Returns a dict."""
    w = weights(K) if w is None else w
    dd = d[m]; s = sw[m]
    n = dd.size
    out = {'n': n, 'switch': s.mean()}
    for name, sel in (('le4', dd <= K - 2), ('d5', dd == K - 1), ('d6', dd == K), ('good', dd <= K)):
        tot = sel.sum()
        out['n_' + name] = int(tot); out['miss_' + name] = float((sel & ~s).sum() / tot) if tot else 0.0
        out['missn_' + name] = int((sel & ~s).sum())
    out['wasted'] = float((s & (dd > K)).sum() / n)                  # share of all cases: switched and too long
    out['precision'] = float((s & (dd <= K)).sum() / max(1, s.sum()))
    out['loss'] = float((w[dd][~s].sum() + (s & (dd > K)).sum()) / n)
    out['wmiss'] = float(w[dd][~s].sum() / w[dd].sum())
    return out
def fmt(p):
    return (f"switch {100*p['switch']:5.1f}%  miss le4 {100*p['miss_le4']:5.1f}% ({p['missn_le4']})  d5 {100*p['miss_d5']:5.1f}% ({p['missn_d5']})  "
            f"d6 {100*p['miss_d6']:5.1f}% ({p['missn_d6']})  prec {100*p['precision']:5.1f}%  loss {p['loss']:.4f}")

def cells(m, keys):
    idx = np.flatnonzero(m)
    K_ = np.stack([np.asarray(F[k] if isinstance(k, str) else k)[idx].astype(np.int64) for k in keys], 1)
    u, inv = np.unique(K_, axis=0, return_inverse=True)
    return idx, u, inv.ravel()
def best_cells(m, keys, K=6, w=None, lam=1.0):
    """Loss-optimal policy that is a function of the keys: switch a cell iff the declined cost exceeds lam x wasted.
    Returns (switch mask over all cosets, number of cells, cells switched)."""
    w = weights(K) if w is None else w
    idx, u, inv = cells(m, keys)
    dd = d[idx]
    cost_decl = np.bincount(inv, weights=w[dd], minlength=len(u))
    cost_sw = np.bincount(inv, weights=(dd > K).astype(float), minlength=len(u))
    take = cost_decl > lam * cost_sw
    sw = np.zeros(N0, bool); sw[idx] = take[inv]
    return sw, len(u), int(take.sum())
def frontier(m, keys, K=6, w=None, lams=(8, 4, 2, 1.5, 1, 0.7, 0.5, 0.35, 0.25, 0.15, 0.1, 0.05)):
    return [(lam,) + tuple(best_cells(m, keys, K, w, lam)) for lam in lams]
