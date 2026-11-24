"""Scoring a rule of the skeleton/variant meta on the cell tables: work, misses, and the chance of a within-goal finish
in the first K HTRs finished, in the meta's order (skeletons shortest first, then (P, S, T, N) in increasing order,
ties at random; the chance is exact over the tie order)."""
import numpy as np
from tcells import Cells

CAPS = ['S', 'T', 'N', 'P+S', 'S+T', 'T+N', 'P+S+T', 'S+T+N', 'P+S+T+N']
ORDERS = {
    'lex': lambda c: (c.g_L, c.P, c.S, c.T, c.N),                       # skeleton length, then (P, S, T, N)
    'pst': lambda c: (c.g_L, c.P + c.S + c.T, c.P, c.S, c.T, c.N),      # fewest extra moves before HTR first
    'pen': lambda c: (c.g_L, c.P + c.S + c.T + c.N, c.P, c.S, c.T, c.N),
    'total': lambda c: (c.g_L + c.P + c.S + c.T + c.N, c.P, c.S, c.T, c.N),
    'doc': lambda c: (c.g_L, c.P + c.S + c.T + c.N, c.P + c.S + c.T, c.S),
}

_LF = np.r_[0.0, np.cumsum(np.log(np.arange(1, 4_000_000)))]
def lgc(n, k):
    n = n.astype(np.int64); k = k.astype(np.int64)
    return _LF[n] - _LF[k] - _LF[n - k]

class Ev(Cells):
    def __init__(self, z, case, bound='cca', goal=None):
        super().__init__(z, case, bound)
        self.g_L = -self.sp          # same order as L within one DR type (L = G - spare)
        self.pd_dr = z[f'{bound}_{case}_pd_dr']; self.pd_cell = z[f'{bound}_{case}_pd_cell']
        self.pd_n = z[f'{bound}_{case}_pd_n'].astype(np.float64); self.pd_s = z[f'{bound}_{case}_pd_s'].astype(np.float64)
        self.qv = {'S': self.S, 'T': self.T, 'N': self.N, 'P+S': self.P + self.S, 'S+T': self.S + self.T, 'T+N': self.T + self.N,
                   'P+S+T': self.P + self.S + self.T, 'S+T+N': self.S + self.T + self.N, 'P+S+T+N': self.P + self.S + self.T + self.N}
        self._ord = {}

    def admit(self, caps=None, floor=1, s0=0, pmax=1, extra=None, pairs=False):
        """caps: {name: value}.  floor: 0 none, 1 mirror floor, 2 the same with T+N >= P+S on 3qt skeletons.
        pairs: with the most-pairs step (not with `extra`, which may cut a group in two)."""
        a = (self.P <= pmax) & (self.sp >= s0)
        fl = [np.zeros_like(self.N), self.mirror_floor, np.where((self.q == 3) & ~self.nofloor, self.P + self.S - self.T, self.mirror_floor)][floor]
        a &= self.P + self.S + self.T + np.maximum(self.N, fl) <= self.sp
        for k, v in (caps or {}).items(): a &= self.qv[k] <= v
        if extra is not None: a &= extra(self)
        if pairs:
            assert extra is None
            a &= self.top(floor)
        return a

    def order(self, name):
        if name not in self._ord:
            keys = ORDERS[name](self)
            # rank of each cell's sort key, then the per-DR pairs sorted by (dr, rank)
            kk = np.stack(keys, axis=1)
            _, rank = np.unique(kk, axis=0, return_inverse=True); rank = rank.ravel()
            o = np.lexsort((rank[self.pd_cell], self.pd_dr))
            dr = self.pd_dr[o]; rk = rank[self.pd_cell][o]
            newg = np.r_[True, (dr[1:] != dr[:-1]) | (rk[1:] != rk[:-1])]
            gid = np.cumsum(newg) - 1
            gdr = dr[newg]
            self._ord[name] = (o, gid, gdr, int(gid[-1]) + 1)
        return self._ord[name]

    def within(self, adm, Ks=(5, 10, 20), order='lex'):
        """Share of within-goal DRs with a within-goal finish among the first K HTRs finished."""
        o, gid, gdr, ng = self.order(order)
        a = adm[self.pd_cell[o]]
        gn = np.bincount(gid, self.pd_n[o] * a, minlength=ng); gs = np.bincount(gid, self.pd_s[o] * a, minlength=ng)
        cum = np.cumsum(gn) - gn                       # HTRs before this group, over all DRs
        start = np.r_[True, gdr[1:] != gdr[:-1]]
        base = np.maximum.accumulate(np.where(start, cum, 0))
        before = cum - base                            # within the DR
        hit = gs > 0
        # first hitting group of each DR
        idx = np.nonzero(hit)[0]
        fdr, fi = np.unique(gdr[idx], return_index=True)
        idx = idx[fi]
        out = []
        for K in Ks:
            k = np.minimum(K - before[idx], gn[idx])
            n = gn[idx]; s = gs[idx]
            p = np.where(k <= 0, 0.0, np.where(k > n - s, 1.0, 1 - np.exp(lgc(n - s, np.clip(k, 0, n - s)) - lgc(n, np.clip(k, 0, n)))))
            out.append(p.sum() / self.nwg)
        return out
