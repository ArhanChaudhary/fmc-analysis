"""Loader and helpers for the (L; P, S, T, N) records of `drvar metatuple` (../out/meta/tup{M}.t50): every HTR in
reach of the goal on both sides of the sample DRs, read against its own corner skeleton (see drvar/src/tuple.rs).

P = extra moves before the state with 2 quarter turns left, S = extra moves of the setup at 2qt, T = extra moves of
the trigger, N = extra moves after HTR; L = the skeleton's length, so L + P + S + T + N = the solution's length.
pairs = true corner/edge pairs in the U and D layers right after the variant's last insertion: on the state just
before the quarter turn that closes the last section with extra moves (the last quarter turn when there are none).

The premove pass (the NISS rule of the Suggested Meta of Advanced DR Bounding; `drvar metarest`,
../out/meta/rest{M}.t50): for a skeleton of 3 or more quarter turns that ends with its last one (HH corners), that
turn is made first on the other side, and what is left is a DR with one quarter turn fewer and one move less to the
goal, gone through with the meta.  A skeleton that also starts with a quarter turn gets the pass on both sides
(SVM_REST_BOTH=0: on inverse only).
The meta makes the pass and then goes through the skeleton in full as well (SVM_UNISS=add, the default).  In the doc
the pass takes the place of the full search of that side (SVM_UNISS=1), which loses the solutions that go on after
that quarter turn.  SVM_UNISS=0 leaves the pass out.

A test run on part of the sample: SVM_SUFFIX=x SVM_NDRS=200 makes every script read tup{M}x.t50 and the first 200 DRs,
and write its own files with the same suffix (cells{M}x.npz, tfinal{M}x.json, ...)."""
import os
import numpy as np, pandas as pd

SUF = os.environ.get('SVM_SUFFIX', '')
# 'add': the left-over DRs of the premove pass are gone through as well as the skeletons they come from (the meta);
# '1': they take the place of those skeletons (the doc's NISS rule as written); '0': no premove pass
UNISS = {'1': True, '0': False, 'add': 'add'}[os.environ.get('SVM_UNISS', 'add')]
# The left-over DR is "a one-fewer-qt case" gone through with the meta on one side only, so step 4 (leaving a variant
# to the other side) is not applied to it unless SVM_REST_FLOOR=1.  SVM_REST_HH=drop leaves out the left-over
# skeletons of 3 or more quarter turns that again end with their last one (the whole skeleton ends with two quarter
# turns in a row); the default keeps them and goes through them in full.
REST_FLOOR = os.environ.get('SVM_REST_FLOOR', '0') == '1'
REST_HH = os.environ.get('SVM_REST_HH', 'keep')
assert REST_HH in ('keep', 'drop')
# A skeleton that starts and ends with a quarter turn ends with one on both sides.  '1' (the meta): it gets the pass on
# both sides; '0': on inverse only (the first quarter turn is the premove, made on normal), which also leaves out its
# variants with extra half turns before the first quarter turn.
REST_BOTH = os.environ.get('SVM_REST_BOTH', '1') == '1'
# The meta leaves out the HTRs that are G moves away (step 3: at most G-1 moves to HTR, a premove counted): such an HTR
# has no move left for a finish.  '1' (the meta): those records are dropped when the file is read, so every table,
# cell and example is counted without them; '0': every HTR in reach (the checks of the reading, and what the cap
# changes).
HCAP = os.environ.get('SVM_HCAP', '1') == '1'
NDRS = int(os.environ.get('SVM_NDRS', '0')) or None
def path(name, suffix=None):
    """../out/meta/NAME, with the run's suffix before the extension."""
    stem, ext = name.rsplit('.', 1)
    return f"../out/meta/{stem}{SUF if suffix is None else suffix}.{ext}"

DTT = np.dtype([('dr', '<u4'), ('pre2', '<u4'), ('route', '<u8'), ('side', 'u1'), ('q', 'u1'), ('kind', 'u1'), ('wl', 'u1'),
                ('L', 'u1'), ('lc', 'u1'), ('e', 'u1', (6,)), ('nb', 'u1', (4,)), ('total', 'u1'), ('tL', 'u1'), ('tlen', 'u1'),
                ('te', 'u1', (6,)), ('tn', 'u1'), ('fam', 'u1'), ('a2', 'u1'), ('shape', '<u4')])
assert DTT.itemsize == 48
# the record with the pair counts (true pairs, HTR-equivalent pairs)
DTP = np.dtype(DTT.descr + [('pairs', 'u1'), ('hpairs', 'u1')])
assert DTP.itemsize == 50
BOUNDS = {'none': None, 'simple': 0, 'cca': 1, 'comp': 2, 'casemin': 3}
ORDER = ['4b2', '4a2', '2c3', '4c3', '2c4', '0c3', '0c4', '4c4']       # shortest skeleton first, as on the page
BYQT = {2: ['4a2', '4b2'], 3: ['0c3', '2c3', '4c3'], 4: ['0c4', '2c4', '4c4']}

def drs(m):
    D = []
    for l in open(f'../out/meta/run{m}.tsv'):
        f = l.rstrip('\n').split('\t')
        if f[0] == 'D': D.append(f[1:])
    d = pd.DataFrame(D, columns=['dr', 'm', 'goal', 'ls', 'subset', 'lminN', 'nN', 'lminI', 'nI', 'scramble'])
    for c in ['dr', 'm', 'goal', 'ls', 'lminN', 'nN', 'lminI', 'nI']: d[c] = d[c].astype(int)
    d = d.set_index('dr')
    d['case'] = d.subset.str.slice(0, 3)
    d['wg'] = d.ls <= d.goal
    return d

class T:
    """The records of one DR type as flat arrays.  A 2qt DR is a 4a2 or 4b2: the few states that are 0c0 up to a turn
    of both layers are dropped."""
    def __init__(self, m, sections=False, suffix=None, ndrs=None, uniss=None, rest_floor=None, rest_hh=None, rest_both=None, hcap=None):
        """uniss: with the NISS rule (default: the run's UNISS).  With it the rows are the HTRs of the skeletons gone
        through in full plus the HTRs of the left-over DRs (`pre`); for those q, P, S, T, N are the left-over
        skeleton's, and L, wl and the totals count the turn made on the other side."""
        self.m = m
        d = drs(m)
        self.d = d[d.case != '0c0'].copy()
        self.g = int(d.goal.iloc[0])
        suffix = SUF if suffix is None else suffix
        ndrs = ndrs or NDRS
        if ndrs: self.d = self.d[self.d.index < ndrs].copy()       # a run on the first `ndrs` DRs only
        # 50-byte records carry the pair counts; a 48-byte file of an earlier run doesn't (pairs = None)
        base = f'../out/meta/tup{m}{suffix}'
        r = np.fromfile(base + '.t50', dtype=DTP) if os.path.exists(base + '.t50') else np.fromfile(base + '.t48', dtype=DTT)
        r = r[np.isin(r['dr'], self.d.index.values)]
        self.hcap = HCAP if hcap is None else hcap          # only the HTRs at most G-1 moves away
        self.nreach = len(r)                    # HTRs in reach on both sides, whatever their distance
        if self.hcap: r = r[r['wl'] <= self.g - 1]
        self.uniss = UNISS if uniss is None else uniss
        self.nfull = len(r)                     # HTRs of the sample, every skeleton in full
        pre = np.zeros(len(r), bool)
        if self.uniss:
            assert 'pairs' in r.dtype.names, 'the NISS rule needs the 50-byte records'
            rr = np.fromfile(f'../out/meta/rest{m}{suffix}.t50', dtype=DTP)
            rr = rr[np.isin(rr['dr'], self.d.index.values)]
            self.nreach_pre = len(rr)
            if self.hcap: rr = rr[rr['wl'] <= self.g - 1]       # (wl counts the premove)
            # taken off a side: 3 or more quarter turns and no corner move after the last one; on normal only when
            # the skeleton doesn't start with a quarter turn as well (the first section's skeleton moves are the low
            # bits of `shape`)
            first0 = lambda a: ((a['shape'] & 7) == 0) & (a['side'] == 0)
            drop = (r['q'] >= 3) & (r['lc'] == 0) & ~first0(r)
            if self.uniss == 'add': drop &= False
            self.rest_both = REST_BOTH if rest_both is None else rest_both
            keep = np.ones(len(rr), bool) if self.rest_both else ~first0(rr)
            if (REST_HH if rest_hh is None else rest_hh) == 'drop': keep &= ~((rr['q'] >= 3) & (rr['lc'] == 0))
            self.replaced = (int(drop.sum()), int(keep.sum()))        # HTRs taken off, HTRs of the left-over DRs put in
            r = np.concatenate([r[~drop], rr[keep]])
            pre = np.r_[np.zeros(int((~drop).sum()), bool), np.ones(int(keep.sum()), bool)]
        self.pre = pre
        self.n = len(r)
        q = r['q'].astype(np.int64)
        e = r['e'].astype(np.int16)
        cs = np.cumsum(e, axis=1)
        i = np.arange(self.n)
        self.dr = r['dr'].astype(np.int64); self.side = r['side']; self.q = r['q']; self.kind = r['kind']
        self.qsk = (r['q'] + pre).astype(np.uint8)        # quarter turns of the whole skeleton
        self.L = r['L'].astype(np.int16)
        self.S = e[i, q - 2]; self.T = e[i, q - 1]
        self.P = (cs[i, q - 1] - self.S - self.T).astype(np.int16)
        self.P1 = np.where(q >= 3, e[i, np.maximum(q - 3, 0)], 0).astype(np.int16)   # the last section before 2qt
        # 6qt skeletons: the middle section (the 4th of 7), which the inverse also reads as its middle
        self.Pm = np.where(q == 6, e[i, 3], 0).astype(np.int16)
        # the mirror floor: the N this side may assume, because with a smaller N the inverse reads the same solution
        # with fewer early extra moves.  2qt skeleton (S,T,N) <-> (N,T,S): N >= S.  3qt (P,S,T,N) <-> (N,T,S,P):
        # N >= P.  4qt (P,P,S,T,N) <-> (N,T,S,P,P): T+N >= P.  5qt: S+T+N >= P.  6qt: S+T+N >= P without its middle.
        self.floor = np.where(q == 2, self.S, np.where(q == 3, self.P, np.where(q == 4, self.P - self.T,
                     np.where(q == 5, self.P - self.S - self.T, self.P - self.Pm - self.S - self.T)))).astype(np.int16)
        self.rest_floor = REST_FLOOR if rest_floor is None else rest_floor
        if not self.rest_floor: self.floor[pre] = -99          # no step 4 on the left-over DRs
        self.nb = r['nb'].astype(np.int16)
        self.total = r['total'].astype(np.int16)
        self.ok = self.total <= self.g
        self.spare = self.g - self.L
        self.wl = r['wl'].astype(np.int16); self.fam = r['fam'].astype(np.int16)
        self.pre2 = r['pre2'].astype(np.int64); self.route = r['route']
        # skeleton moves of each section before HTR (3 bits each) and of the last one
        sh = r['shape'].astype(np.int64)
        self.ell = np.stack([(sh >> (3 * j)) & 7 for j in range(6)], axis=1).astype(np.int8)
        self.lc = r['lc'].astype(np.int16)
        self.pairs = r['pairs'].astype(np.int16) if 'pairs' in r.dtype.names else None
        j = np.arange(6)[None, :]
        # a middle section with no skeleton move: two quarter turns that cancel on the corners
        self.emptymid = ((self.ell == 0) & (j >= 1) & (j < q[:, None])).any(axis=1)
        self.emptymid |= pre & (r['lc'] == 0)             # ... or the turn made on the other side right after the left-over skeleton's last
        self.tn = r['tn'].astype(np.int16); self.tL = r['tL'].astype(np.int16)
        te = r['te'].astype(np.int16); tcs = np.cumsum(te, axis=1)
        self.tS = te[i, q - 2]; self.tT = te[i, q - 1]; self.tP = (tcs[i, q - 1] - self.tS - self.tT).astype(np.int16)
        if sections: self.e = e; self.te = te
        self.ndr = int(self.d.index.max()) + 1
        self.case = self.d.case.reindex(range(self.ndr)).fillna('').values
        self.wg = self.d.wg.reindex(range(self.ndr)).fillna(False).values.astype(bool)
        self.rcase = self.case[self.dr]
        # routes to 2qt: one id per (DR, side, path up to the state with 2 quarter turns left)
        assert self.pre2.max() < (1 << 22)
        self.rkey = ((self.dr * 2 + self.side) * 2 + pre) * (1 << 22) + self.pre2
        # skeletons: one id per (DR, side, corner cases at the quarter turns)
        _, self.skel = np.unique(np.stack([(self.dr * 2 + self.side) * 2 + pre, self.route.astype(np.int64)], axis=1), axis=0, return_inverse=True)
        self.skel = self.skel.ravel()

    def N(self, bound):
        """The N a solver has at 2qt under this bound (0 without DR Bounding)."""
        return np.zeros(self.n, np.int16) if BOUNDS[bound] is None else self.nb[:, BOUNDS[bound]]

    def per_dr(self, mask):
        return np.bincount(self.dr[mask], minlength=self.ndr)

    def found(self, mask):
        """Per DR: does the masked set hold a within-goal HTR?"""
        return self.per_dr(mask & self.ok) > 0

    def routes(self, mask):
        """Per DR: distinct paths to the state with 2 quarter turns left among the masked HTRs, both sides."""
        k = np.unique(self.rkey[mask])
        return np.bincount((k >> 24), minlength=self.ndr)

    def skeletons(self, mask):
        """Per DR: distinct skeletons among the masked HTRs.  When the premove pass comes on top of the full search,
        its skeletons are ones the full search has too (one quarter turn shorter, with the premove), so they are
        counted there."""
        if self.uniss == 'add': mask = mask & ~self.pre
        k = np.unique(self.skel[mask])
        first = np.zeros(self.skel.max() + 1, np.int64); first[self.skel] = self.dr
        return np.bincount(first[k], minlength=self.ndr)

def pct(x): return f'{100 * x:.1f}%'
