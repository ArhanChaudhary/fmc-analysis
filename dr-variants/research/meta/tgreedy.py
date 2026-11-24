"""How much better could a rule on (L; P, S, T, N) do than one constant cap on P+S+T?  Starting from "P <= 1, the
goal, the mirror floor, the most-pairs step", cells are dropped greedily (most HTRs saved per within-goal DR lost) inside richer and richer
families of rules, fitted on half of the DRs and scored on the other half:

  const   one cap on P+S+T for every skeleton (the sweep's family)
  spare   a cap on P+S+T for each number of spare moves G-L
  qps     a cap on P+S+T for each (skeleton quarter turns, P, spare moves)
  spn     a cap on P+S+T for each (spare moves, N of the bound)
  qpsn    a cap on P+S+T for each (skeleton quarter turns, P, spare moves, N of the bound)
  cells   any set of (skeleton quarter turns, spare moves, P, S, T, N) cells: the limit of what such a rule can do

Averaged over 8 random splits.
usage: tgreedy.py -> ../out/meta/greedy_frontier.json"""
import sys, json, heapq
import numpy as np
from teval import Ev
from tcommon import BYQT, ORDER, path
from tmeta import PAIRS_MODE

BIG = [k for k in ORDER if k not in ('0c3', '0c4')]

class Half:
    """One corner case, one half of its DRs."""
    def __init__(self, e, keep):
        sel = keep[e.pd_dr]
        self.ncell = len(e.cnt)
        self.work = np.bincount(e.pd_cell[sel], e.pd_n[sel], minlength=self.ncell)
        wg = np.zeros(len(keep), bool); wg[e.wg] = True
        okp = sel & (e.pd_s > 0) & wg[e.pd_dr]
        self.okdr = e.pd_dr[okp]; self.okcell = e.pd_cell[okp]
        self.ndr = int(keep[e.drs].sum()); self.nwg = int((keep & wg).sum())
        o = np.argsort(self.okcell, kind='stable')
        self.okdr = self.okdr[o]; self.okcell = self.okcell[o]
        self.start = np.searchsorted(self.okcell, np.arange(self.ncell + 1))
    def reset(self, adm):
        self.adm = adm.copy()
        self.cov = np.bincount(self.okdr[adm[self.okcell]], minlength=int(self.okdr.max()) + 1 if len(self.okdr) else 1)
        self.w = float(self.work[adm].sum()); self.lost = 0
        self.found0 = int((self.cov > 0).sum())
    def drs_of(self, cells):
        if len(cells) == 0: return np.zeros(0, np.int64)
        return np.concatenate([self.okdr[self.start[c]:self.start[c + 1]] for c in cells])
    def cost(self, cells):
        """(HTRs saved, DRs lost) if these admitted cells are dropped."""
        cells = cells[self.adm[cells]]
        d = self.drs_of(cells)
        if len(d) == 0: return float(self.work[cells].sum()), 0
        u, n = np.unique(d, return_counts=True)
        return float(self.work[cells].sum()), int((self.cov[u] == n).sum())
    def drop(self, cells):
        cells = cells[self.adm[cells]]
        d = self.drs_of(cells)
        if len(d):
            u, n = np.unique(d, return_counts=True)
            self.lost += int((self.cov[u] == n).sum()); self.cov[u] -= n
        self.w -= float(self.work[cells].sum()); self.adm[cells] = False

def load():
    ev = {}
    for m in (2, 3, 4):
        z = np.load(path(f'cells{m}.npz'))
        for case in BYQT[m]:
            if case in BIG: ev[case] = Ev(z, case)
    return ev

def atoms(ev, family):
    """Ordered lists of atoms: within a list an atom may only be dropped after the ones before it.  An atom is
    {case: array of cells}."""
    lists = {}
    for case, e in ev.items():
        pst = e.P + e.S + e.T
        if family == 'const': g = [() for _ in pst]
        elif family == 'spare': g = list(zip(e.sp))
        elif family == 'qps': g = list(zip(e.q, e.P, e.sp))
        elif family == 'spn': g = list(zip(e.sp, e.N))
        elif family == 'qpsn': g = list(zip(e.q, e.P, e.sp, e.N))
        elif family == 'cells': g = list(zip(e.q, e.sp, e.P, e.S, e.T, e.N))
        for i in range(len(pst)):
            key = tuple(int(v) for v in g[i])
            lvl = int(pst[i]) if family != 'cells' else 0
            lists.setdefault(key, {}).setdefault(lvl, {}).setdefault(case, []).append(i)
    out = []
    for key, lv in lists.items():
        out.append([(key, l, {c: np.array(v) for c, v in lv[l].items()}) for l in sorted(lv, reverse=True)])
    return out

def run(ev, family, train, test, base):
    for c in ev: train[c].reset(base[c]); test[c].reset(base[c])
    w0 = {c: train[c].w for c in ev}; t0 = {c: test[c].w for c in ev}
    lists = atoms(ev, family)
    def score(a):
        dw = 0.0; dm = 0.0
        for c, cells in a[2].items():
            w, l = train[c].cost(cells); dw += w / w0[c]; dm += l / train[c].nwg
        return dw, dm
    heap = []
    for li, L in enumerate(lists):
        dw, dm = score(L[0]); heapq.heappush(heap, (-(dw / (dm + 1e-6)), li, 0))
    front = []; picked = []
    def snap():
        tr = dict(work=float(np.exp(np.mean([np.log(max(train[c].w, 1e-9) / w0[c]) for c in ev]))), miss=float(np.mean([train[c].lost / train[c].nwg for c in ev])),
                  worst=float(max(train[c].lost / train[c].nwg for c in ev)))
        te = dict(work=float(np.exp(np.mean([np.log(max(test[c].w, 1e-9) / t0[c]) for c in ev]))), miss=float(np.mean([test[c].lost / test[c].nwg for c in ev])),
                  worst=float(max(test[c].lost / test[c].nwg for c in ev)))
        front.append((tr, te))
    snap()
    while heap:
        r, li, pos = heapq.heappop(heap)
        a = lists[li][pos]
        dw, dm = score(a)
        cur = -(dw / (dm + 1e-6))
        if heap and cur > heap[0][0] + 1e-12:          # stale: its ratio fell, put it back
            heapq.heappush(heap, (cur, li, pos)); continue
        for c, cells in a[2].items(): train[c].drop(cells); test[c].drop(cells)
        picked.append((a[0], a[1])); snap()
        if pos + 1 < len(lists[li]):
            dw, dm = score(lists[li][pos + 1]); heapq.heappush(heap, (-(dw / (dm + 1e-6)), li, pos + 1))
        if front[-1][0]['miss'] > 0.08: break
    return front, picked

def split_run(ev, seed):
    """One random split: for the constant caps 6, 5 and 4 the work and extra misses on the held-out half, and for every
    family the least held-out work among its rules that miss no more on the held-out half than that constant cap."""
    rng = np.random.default_rng(seed)
    half = {}
    for c, e in ev.items():
        keep = np.zeros(e.nmax + 1, bool); keep[e.drs[rng.random(len(e.drs)) < 0.5]] = True
        half[c] = keep
    train = {c: Half(e, half[c]) for c, e in ev.items()}
    test = {c: Half(e, ~half[c]) for c, e in ev.items()}
    base = {c: e.admit({}, floor=1, pairs=PAIRS_MODE == 'drop') for c, e in ev.items()}
    out = {}
    fronts = {}
    for fam in FAMILIES:
        fronts[fam] = run(ev, fam, train, test, base)
    cfront, cpicked = fronts['const']
    for cap in (6, 5, 4):
        i = [j for j, (k, l) in enumerate(cpicked) if l == cap + 1]
        if not i: continue
        ref = cfront[i[0] + 1][1]
        row = dict(const_miss=ref['miss'], const_work=ref['work'])
        for fam in FAMILIES:
            ok = [f for f in fronts[fam][0] if f[1]['miss'] <= ref['miss'] + 1e-9]
            best = min(ok, key=lambda f: f[1]['work'])
            row[fam] = best[1]['work']; row[fam + '_train'] = best[0]['work']; row[fam + '_trainmiss'] = best[0]['miss']
        out[cap] = row
    return out

FAMILIES = ('const', 'spare', 'qps', 'spn', 'qpsn', 'cells')
if __name__ == '__main__':
    ev = load()
    seeds = list(range(1, 9))
    runs = [split_run(ev, sd) for sd in seeds]
    res = {}
    for cap in (6, 5, 4):
        rows = [r[cap] for r in runs if cap in r]
        res[cap] = {k: float(np.mean([r[k] for r in rows])) for k in rows[0]}
        res[cap]['splits'] = len(rows)
        print(f"cap {cap}: held-out extra misses {100 * res[cap]['const_miss']:.2f} pts | held-out work: " +
              ' '.join(f"{f} {100 * res[cap][f]:.1f}%" for f in FAMILIES) + ' | fitted-half work: ' +
              ' '.join(f"{f} {100 * res[cap][f + '_train']:.1f}%" for f in FAMILIES), flush=True)
    json.dump(dict(seeds=seeds, caps=res), open(path('greedy_frontier.json'), 'w'), indent=1)
