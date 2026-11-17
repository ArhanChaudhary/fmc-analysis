"""Fast ranking of feature subsets by cell-optimal weighted loss within a population mask."""
import numpy as np, itertools, sys
from lib import *
F['ccs'] = F['corner_case']*10+F['case_suffix']
F['arm'] = F['carm']*10+F['earm']
class Pop:
    def __init__(self, m, K=6, w=None):
        self.m = m; self.idx = np.flatnonzero(m); self.n = self.idx.size
        self.dd = d[self.idx]; self.K = K
        self.w = (weights(K) if w is None else w)[self.dd]
        self.bad = (self.dd > K).astype(float)
        self.codes = {}
    def code(self, k):
        if k not in self.codes:
            v = np.asarray(F[k])[self.idx]
            u, inv = np.unique(v, return_inverse=True)
            self.codes[k] = (inv.astype(np.int64), len(u))
        return self.codes[k]
    def loss(self, keys, lam=1.0, detail=False):
        code = np.zeros(self.n, np.int64); size = 1
        for k in keys:
            c, s = self.code(k); code = code * s + c; size *= s
        a = np.bincount(code, weights=self.w, minlength=size); b = np.bincount(code, weights=self.bad, minlength=size)
        take = a > lam * b
        L = (np.where(take, b, a)).sum() / self.n
        if not detail: return L
        sw = np.zeros(N0, bool); sw[self.idx] = take[code]
        return L, sw, int(((a + b) > 0).sum()), int((take & ((a + b) > 0)).sum())
    def rank(self, lib, kmax, top=8, must=()):
        out = {}
        for k in range(1, kmax + 1):
            res = []
            for keys in itertools.combinations(lib, k):
                keys = tuple(must) + keys
                res.append((self.loss(keys), keys))
            res.sort(); out[k] = res[:top]
        return out
LIB = ['pairs','carm','earm','ccs','fake','side','edges_paired','edges_same_layer','edges_same_slice','edges_same_side','ud_split','hole_cfg','pairs_out','fake_m','e_fakeonly','e_naked','c_loose','c_loose_arm','c_unpaired_arm','c_with_edge_layer','side_rl','hole_bars','pair_over_hole','lr_split','fb_split','twist_major','split_pairs','ar_bars']
if __name__ == '__main__':
    c, e = int(sys.argv[1]), int(sys.argv[2]); kmax = int(sys.argv[3])
    m = drm_mask(c, e); P = Pop(m)
    lib = [k for k in LIB if len(np.unique(F[k][m])) > 1]
    print('DRM', c, e, 'n', P.n, 'never', P.w.sum()/P.n, 'always', P.bad.sum()/P.n)
    for k, res in P.rank(lib, kmax).items():
        for L, keys in res:
            L2, sw, nc, nt = P.loss(keys, detail=True)
            pr = profile(m, sw)
            print(f'{k} {L:.4f} {"+".join(keys):60s} cells {nc:5d}/{nt:5d} sw {100*pr["switch"]:5.1f}% miss {100*pr["miss_le4"]:4.1f} {100*pr["miss_d5"]:4.1f} {100*pr["miss_d6"]:4.1f} prec {100*pr["precision"]:.0f}%')
