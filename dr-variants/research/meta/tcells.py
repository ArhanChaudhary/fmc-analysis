"""Cells of the (P, S, T, N) search for the cap optimisation: the sample's HTRs counted by (corner case, skeleton
quarter turns, spare moves G-L, P, S, T, N at 2qt), and for every DR the cells that hold a within-goal HTR.  A rule
that only reads these numbers admits whole cells, so its work is a sum over cells and a DR is found when one of its
within-goal cells is admitted.

The most-pairs step on cells.  The step keeps, among the admitted HTRs of one skeleton with the same (P, S, T, N), the
ones with the most pairs.  Such a group has one (quarter turns, spare moves, P, S, T, N), so a rule admits all of it
or none of it, except on a 6qt skeleton with the mirror floor: there the floor is P - Pm - S - T (Pm = the extra
moves of the middle section), so the rule admits the members with Pm >= k* = max(0, 2P - spare).  Every HTR carries
kt = the smallest k for which it has the most pairs among its group's members with Pm >= k (NEVER if there is none;
having the most for one k means having it for every larger k up to its own Pm).  An admitted HTR passes the step
exactly when kt <= k*, and kt is part of the cell.
usage: tcells.py M  -> ../out/meta/cells{M}.npz"""
import sys
import numpy as np
from tcommon import T, BOUNDS, BYQT, path

NEVER = 15
def enc(q, sp, P, S, Tr, N, Pm, kt, pre):
    return (((((((q.astype(np.int64) * 16 + sp) * 16 + P) * 16 + S) * 16 + Tr) * 16 + N) * 16 + Pm) * 16 + kt) * 2 + pre
def dec(k):
    """-> q, sp, P, S, T, N, Pm, kt, pre (pre: an HTR of a left-over DR of the NISS rule)"""
    pre = k % 2; k = k // 2
    kt = k % 16; k = k // 16
    Pm = k % 16; k = k // 16
    N = k % 16; k = k // 16; Tr = k % 16; k //= 16; S = k % 16; k //= 16; P = k % 16; k //= 16; sp = k % 16; q = k // 16
    return q, sp, P, S, Tr, N, Pm, kt, pre

def group_max(gid, v, n):
    """Per group id (0..n-1) the largest v, -1 for a group with no row."""
    out = np.full(n, -1, np.int16)
    if len(gid):
        o = np.argsort(gid, kind='stable'); gs = gid[o]
        starts = np.nonzero(np.r_[True, gs[1:] != gs[:-1]])[0]
        out[gs[starts]] = np.maximum.reduceat(v[o], starts)
    return out

def top_from(t, N, rows):
    """kt of the HTRs `rows` (indices), the groups being taken among these rows only."""
    g = (((t.skel[rows].astype(np.int64) * 32 + t.P[rows]) * 32 + t.S[rows]) * 32 + t.T[rows]) * 32 + N[rows]
    _, gid = np.unique(g, return_inverse=True); gid = gid.ravel()
    ng = int(gid.max()) + 1 if len(gid) else 0
    pr = t.pairs[rows]; Pm = t.Pm[rows]
    kt = np.full(len(rows), NEVER, np.int64)
    for k in range(int(Pm.max()) + 1 if len(rows) else 0):
        sub = np.nonzero(Pm >= k)[0]
        mx = group_max(gid[sub], pr[sub], ng)
        hit = sub[(pr[sub] == mx[gid[sub]]) & (kt[sub] == NEVER)]
        kt[hit] = k
    return kt

def build(m):
    t = T(m)
    assert t.pairs is not None, 'these records have no pair counts (a 48-byte file): run drvar metatuple again'
    out = {'fmt': np.array(3), 'rest_floor': np.array(int(t.rest_floor))}
    for b in ('none', 'simple', 'cca', 'comp'):
        N = t.N(b)
        reach = t.P + t.S + t.T + N <= t.spare
        assert max(t.P[reach].max(), t.S[reach].max(), t.T[reach].max(), N[reach].max(), t.spare.max()) < 16
        assert t.Pm[reach].max() < NEVER
        kt = np.full(t.n, NEVER, np.int64)
        rows = np.nonzero(reach)[0]
        kt[rows] = top_from(t, N, rows)
        key = enc(t.q, t.spare, t.P, t.S, t.T, N, t.Pm, kt, t.pre)
        for case in BYQT[m]:
            sel = reach & (t.rcase == case)
            cells, inv, cnt = np.unique(key[sel], return_inverse=True, return_counts=True)
            okp = np.unique(np.stack([t.dr[sel][t.ok[sel]], inv.ravel()[t.ok[sel]]], axis=1), axis=0)
            out[f'{b}_{case}_cells'] = cells; out[f'{b}_{case}_cnt'] = cnt
            out[f'{b}_{case}_okdr'] = okp[:, 0]; out[f'{b}_{case}_okcell'] = okp[:, 1]
            # per DR: its cells with the number of HTRs and of within-goal HTRs in each (for the order of finishing)
            pk = t.dr[sel] * (1 << 20) + inv.ravel()
            u, n = np.unique(pk, return_counts=True)
            us, ns = np.unique(pk[t.ok[sel]], return_counts=True)
            sarr = np.zeros(len(u), np.int64); sarr[np.searchsorted(u, us)] = ns
            out[f'{b}_{case}_pd_dr'] = (u >> 20).astype(np.int32); out[f'{b}_{case}_pd_cell'] = (u & ((1 << 20) - 1)).astype(np.int32)
            out[f'{b}_{case}_pd_n'] = n.astype(np.int32); out[f'{b}_{case}_pd_s'] = sarr.astype(np.int32)
    for case in BYQT[m]:
        out[f'{case}_drs'] = np.nonzero(t.case == case)[0]
        out[f'{case}_wg'] = np.nonzero((t.case == case) & t.wg)[0]
    np.savez_compressed(path(f'cells{m}.npz'), **out)
    for case in BYQT[m]:
        print(case, {b: len(out[f'{b}_{case}_cells']) for b in ('none', 'simple', 'cca', 'comp')}, 'ok pairs (cca)', len(out[f'cca_{case}_okdr']))

class Cells:
    """One corner case under one bound."""
    def __init__(self, z, case, bound='cca'):
        self.case = case
        assert 'fmt' in z and int(z['fmt']) == 3, 'cells of an earlier version: run tcells.py again'
        self.q, self.sp, self.P, self.S, self.T, self.N, self.Pm, self.kt, self.pre = dec(z[f'{bound}_{case}_cells'])
        self.nofloor = (self.pre == 1) & (int(z['rest_floor']) == 0)         # no step 4 on the left-over DRs
        self.cnt = z[f'{bound}_{case}_cnt'].astype(np.float64)
        self.okdr = z[f'{bound}_{case}_okdr']; self.okcell = z[f'{bound}_{case}_okcell']
        self.drs = z[f'{case}_drs']; self.wg = z[f'{case}_wg']
        self.ndr = len(self.drs); self.nwg = len(self.wg)
        self.nmax = int(max(self.drs.max(), self.okdr.max() if len(self.okdr) else 0)) + 1
        # the mirror floor (see tcommon.T)
        self.mirror_floor = np.where(self.q == 2, self.S, np.where(self.q == 3, self.P, np.where(self.q == 4, self.P - self.T,
                            np.where(self.q == 5, self.P - self.S - self.T, self.P - self.Pm - self.S - self.T))))

        self.mirror_floor = np.where(self.nofloor, -99, self.mirror_floor)
        self.spare = self.sp; self.floor = self.mirror_floor

    def kstar(self, floor):
        """The smallest Pm a rule admits in each cell's group: only the mirror floor on a 6qt skeleton makes it more than 0."""
        return np.where((self.q == 6) & bool(floor), np.maximum(0, 2 * self.P - self.sp), 0)
    def top(self, floor):
        """The cells that pass the most-pairs step under a rule with (floor > 0) or without (0) the mirror floor."""
        return self.kt <= self.kstar(floor)
    def work(self, adm):
        """Mean HTRs to finish per DR."""
        return float(self.cnt[adm].sum()) / self.ndr
    def miss(self, adm):
        """Share of within-goal DRs with no admitted within-goal HTR."""
        hit = np.unique(self.okdr[adm[self.okcell]])
        return 1 - len(hit) / self.nwg if self.nwg else 0.0

if __name__ == '__main__':
    build(int(sys.argv[1]))
