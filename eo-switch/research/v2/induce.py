"""Greedy rule-list induction under the miss-weighted loss (fast version).  A rule: within one pair count, a
conjunction of up to two atoms sets the verdict of every case it covers.  Later rules override earlier ones."""
import numpy as np, sys, itertools
from lib import *
F['ccs'] = F['corner_case']*10+F['case_suffix']; F['arm'] = F['carm']*10+F['earm']; F['cc'] = F['corner_case']
QUICK = ['arm','carm','earm','cc','ccs','side','fake','edges_paired','ud_split','hole_cfg','edges_same_layer']
CATEG = ('arm', 'ccs', 'cc', 'hole_cfg')
def atoms(idx, feats):
    out = []
    for f in feats:
        v = np.asarray(F[f])[idx].astype(np.int64); us = np.unique(v)
        if len(us) < 2: continue
        for u in us: out.append((f, f'{f}={u}', v == u))
        if f not in CATEG and len(us) > 2:
            for u in us[1:-1]:
                out.append((f, f'{f}>={u}', v >= u)); out.append((f, f'{f}<={u}', v <= u))
    return out
def induce(m, feats=QUICK, K=6, w=None, eps=0.002, maxrules=12, strat='pairs', verbose=True, pen2=0.0005):
    idx = np.flatnonzero(m); n = idx.size; dd = d[idx]
    w = (weights(K) if w is None else w)[dd]; bad = (dd > K).astype(float)
    g = (w - bad) / n                       # gain of switching a case (vs not), per case of the DRM
    st = np.asarray(F[strat])[idx]
    cur = np.zeros(n, bool); rules = []
    for p in np.unique(st):
        s = st == p
        if g[s].sum() > 0: cur[s] = True
        rules.append((int(p), 'default', 'switch' if g[s].sum() > 0 else 'skip', 0.0, int(s.sum())))
    A = atoms(idx, feats); fam = [a[0] for a in A]; names = [a[1] for a in A]
    M = np.stack([a[2] for a in A]).astype(np.float32)                 # [atoms, n]
    samefam = np.array([[fam[i] == fam[j] for j in range(len(A))] for i in range(len(A))])
    loss = lambda c: float((w[~c].sum() + bad[c].sum()) / n)
    hist = [(0, loss(cur), float(cur.mean()))]
    if verbose: print(f'start loss {loss(cur):.4f} switch {cur.mean()*100:.1f}%')
    for it in range(maxrules):
        best = (eps, None)
        for p in np.unique(st):
            s = (st == p)
            for verdict, gv in (('switch', np.where(s & ~cur, g, 0.0)), ('skip', np.where(s & cur, -g, 0.0))):
                gv = gv.astype(np.float32)
                if not gv.any(): continue
                single = M @ gv
                i = int(np.argmax(single))
                if single[i] > best[0]: best = (float(single[i]), (p, names[i], verdict, s & (M[i] > 0)))
                pair = (M * gv) @ M.T - pen2
                pair[samefam] = -1
                i, j = np.unravel_index(int(np.argmax(pair)), pair.shape)
                if pair[i, j] > best[0]: best = (float(pair[i, j]), (p, names[i] + ' & ' + names[j], verdict, s & (M[i] > 0) & (M[j] > 0)))
        if best[1] is None: break
        p, name, verdict, cov = best[1]
        cur[cov] = (verdict == 'switch')
        rules.append((int(p), name, verdict, best[0], int(cov.sum())))
        hist.append((it + 1, loss(cur), float(cur.mean())))
        if verbose: print(f'  {it+1:2d}. {strat}={p} & {name:42s} -> {verdict:6s} gain {best[0]:.4f} covers {cov.sum():6d} loss {loss(cur):.4f} switch {cur.mean()*100:.1f}%')
    sw = np.zeros(N0, bool); sw[idx] = cur
    return rules, sw, hist
if __name__ == '__main__':
    c, e = int(sys.argv[1]), int(sys.argv[2])
    m = drm_mask(c, e)
    feats = sys.argv[3].split(',') if len(sys.argv) > 3 and sys.argv[3] != '-' else QUICK
    w6 = float(sys.argv[4]) if len(sys.argv) > 4 else 3.0; rho = float(sys.argv[5]) if len(sys.argv) > 5 else 3.0
    K = int(sys.argv[6]) if len(sys.argv) > 6 else 6
    rules, sw, hist = induce(m, feats, K=K, w=weights(K, w6, rho))
    print(fmt(profile(m, sw, K, weights(K, w6, rho))))
