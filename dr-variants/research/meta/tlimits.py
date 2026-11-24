"""The three sections of "HTR search order and limits": how many HTRs to check on a skeleton before moving on, which
HTRs to check, and when to NISS.  The report's notation: E = P+S+T, the extra moves added to the corner skeleton to
reach HTR; H = the number of moves at which HTR is reached (a start made before a NISS counted; the skeleton's corner
moves after HTR not counted).  Nothing uses a lower bound for N or step 4.

Always: H <= G-1, and at most 1 extra move before 2qt (P <= 1).

The HTRs are read from a list that has, for each one, the linear skeleton its whole solution is on (`drvar
metastdlist`, ../out/meta/stdn{M}.r40): every HTR at most G-1 moves away on normal, on inverse, or with one NISS
after a start of 1 to 3 moves; kept here when the whole path has the DR's quarter turns or two more, as the page's
records are.  After a start, P, S, T are read on the skeleton of what is left.  The list is checked against the
page's records, DR by DR: on normal and inverse it is the records' HTRs, and its HTRs after a single quarter turn,
with 3 or more quarter turns in all and a finish of at least one move, are the records' premove pass.

A skeleton at a time (torder.tier_places): skeletons shortest first; a skeleton's HTRs are those after a single
quarter turn (a NISS after 1 move) first, then the linear ones, then those after a longer start, which are never in
the first pass; each by H, most pairs first.  Two passes: at most k HTRs per skeleton in the first, then the rest in
the same order.

  order   section 1: the HTRs with E <= 5 (normal, inverse, NISS after 1 move) breadth first (by H), depth first
          (one skeleton at a time), and in two passes with k = 2..6, 8, 10
  grid    section 2, with FIRST per skeleton (normal, inverse, NISS after 1 move): k, c = E <= k (k = 3..6 or none)
          and H <= c (c = G-5 .. G-1)
  niss    section 3, with FIRST per skeleton, E <= 5 and H <= G-2: no NISS, a NISS after 1 move, after 1-2, after 1-3

Per entry: HTRs per DR, reach (within-goal DRs with a within-goal HTR among the kept ones), and how many HTRs are
finished before 50% and 95% of within-goal DRs have a within-goal finish (None where the kept HTRs don't reach that
share), over the DRs and 20 random tie orders.

usage: tlimits.py [M ...] -> ../out/meta/tlimits.json"""
import sys, json
import numpy as np
from tcommon import T, BYQT, path
from torder import places, tier_places

FIRST = 5                         # HTRs per skeleton in the first pass (sections 2 and 3)
FIRSTS = (0, 2, 3, 4, 5, 6, 8, 10)
PENK = [3, 4, 5, 6, None]         # P+S+T caps (None: P <= 1 alone)
DT40 = np.dtype([('dr', '<u4'), ('view', 'u1'), ('lev', 'u1'), ('sid', 'u1'), ('moves', 'u1'), ('total', 'u1'), ('pairs', 'u1'), ('q', 'u1'), ('lc', 'u1'),
                 ('l', 'u1'), ('p', 'u1'), ('s', 'u1'), ('t', 'u1'), ('ipairs', 'u1'), ('ll', 'u1'), ('pad', 'u1', (6,)), ('route', '<u8'), ('lroute', '<u8')])
assert DT40.itemsize == 40

def kname(k): return 'none' if k is None else str(k)

def needed(fp, w, share):
    """HTRs to finish so that this share of the within-goal DRs `w` have a within-goal finish (over the tie orders)."""
    v = np.sort(fp[:, w].ravel())
    if not len(v): return None
    x = v[int(np.ceil(share * len(v))) - 1]
    return None if x >= 10**8 else int(x) + 1

class Own:
    """The list of one DR type, one row per HTR."""
    def __init__(self, m, t):
        r = np.fromfile(path(f'stdn{m}.r40'), dtype=DT40)
        r = r[np.isin(r['dr'], t.d.index.values) & (r['q'] <= m + 2) & (r['moves'] <= t.g - 1)]
        self.n = len(r); self.ndr = t.ndr; self.g = t.g
        self.dr = r['dr'].astype(np.int64); self.wl = r['moves'].astype(np.int16)
        self.P = r['p'].astype(np.int16); self.S = r['s'].astype(np.int16); self.T = r['t'].astype(np.int16)
        self.pairs = r['ipairs'].astype(np.int16)          # right after the last insertion, as the records count them
        self.ok = r['total'] <= t.g
        self.lev = r['lev']
        # 0 after a single quarter turn (a premove), 1 linear, 2 after a longer start
        self.tier = np.where(self.lev == 0, 1, np.where(self.lev == 1, 0, 2)).astype(np.int8)
        # the premove pass of the page: a premove, 3 or more quarter turns in all, and something left to finish
        self.passed = (self.lev == 1) & (r['q'] >= 3) & (r['total'] > r['moves'])
        self.side = np.where(r['view'] < 2, r['view'], 3 - r['view']).astype(np.int64)     # the side the path is on
        self.rcase = t.case[self.dr]
        key = np.stack([self.dr * 2 + self.side, r['lroute'].astype(np.int64)], axis=1)
        _, self.skel = np.unique(key, axis=0, return_inverse=True)
        self.skel = self.skel.ravel()
        # the skeleton's length (one for all its HTRs)
        L = np.full(int(self.skel.max()) + 1, 99, np.int16)
        np.minimum.at(L, self.skel, r['ll'].astype(np.int16))
        self.Lsk = L[self.skel]
        assert (self.Lsk == r['ll']).all(), 'the HTRs of one skeleton have one L'
    def per_dr(self, mask): return np.bincount(self.dr[mask], minlength=self.ndr)
    def found(self, mask): return self.per_dr(mask & self.ok) > 0
    def skeletons(self, mask):
        k = np.unique(self.skel[mask])
        first = np.zeros(int(self.skel.max()) + 1, np.int64); first[self.skel] = self.dr
        return np.bincount(first[k], minlength=self.ndr)

def summary(o, mk, sel, w, fp, fl=None):
    per = o.per_dr(mk); f = o.found(mk)
    assert ((fp < 10**9).all(axis=0) == f).all()
    e = dict(htr_med=float(np.median(per[sel])), htr_mean=float(per[sel].mean()), n=int(mk.sum()), nok=int((mk & o.ok).sum()),
             reach=float(f[w].mean()) if w.any() else 0.0, found=int(f[w].sum()), p50=needed(fp, w, 0.5), p95=needed(fp, w, 0.95))
    if fl is not None: e.update(p50_len=needed(fl, w, 0.5), p95_len=needed(fl, w, 0.95))
    return e

if __name__ == '__main__':
    ms = [int(a) for a in sys.argv[1:]] or [2, 3, 4]
    out = {}
    for m in ms:
        t = T(m, uniss='add', rest_floor=False)
        assert t.hcap and (t.wl <= t.g - 1).all()
        g = t.g; caps = list(range(g - 5, g))
        o = Own(m, t)
        pst = o.P + o.S + o.T
        pen = {k: (o.P <= 1) & ((pst <= k) if k is not None else True) for k in PENK}
        lin = o.lev == 0
        one = o.lev <= 1                 # normal, inverse and a NISS after a single quarter turn
        tpst = t.P + t.S + t.T; tpen5 = (t.P <= 1) & (tpst <= 5)
        for case in BYQT[m]:
            sel = t.case == case; w = sel & t.wg; oc = o.rcase == case; kc = t.rcase == case
            # the list against the records, DR by DR: normal and inverse, the premove pass; any extra moves, and the page's cap
            for a, b in ((oc & lin, kc & ~t.pre), (oc & o.passed, kc & t.pre), (oc & lin & pen[5], kc & ~t.pre & tpen5), (oc & o.passed & pen[5], kc & t.pre & tpen5)):
                assert (o.per_dr(a)[sel] == t.per_dr(b)[sel]).all() and (o.per_dr(a & o.ok)[sel] == t.per_dr(b & t.ok)[sel]).all(), ('the list is not the records', case)
            R = dict(m=m, goal=g, cap=g - 1, first=FIRST, drs=int(sel.sum()), wg=int(w.sum()), grid={}, niss={})
            # ---- section 1: the order
            base = oc & one & pen[5]
            fl = places(o, [base])[0]
            ft = tier_places(o, [base], firsts=FIRSTS)[0]
            R['order'] = dict(htr_med=float(np.median(o.per_dr(base)[sel])), reach=float(o.found(base)[w].mean()) if w.any() else 0.0,
                              skel_med=float(np.median(o.skeletons(base)[sel])),
                              len=dict(p50=needed(fl, w, 0.5), p95=needed(fl, w, 0.95)),
                              **{('skel' if k == 0 else f'two{k}'): dict(p50=needed(ft[i], w, 0.5), p95=needed(ft[i], w, 0.95)) for i, k in enumerate(FIRSTS)})
            # ---- section 2: the caps
            names = [f'{kname(k)}_{c}' for k in PENK for c in caps]
            masks = [oc & one & pen[k] & (o.wl <= c) for k in PENK for c in caps]
            fl = places(o, masks); ft = tier_places(o, masks, firsts=(FIRST,))
            for key, mk, a, b in zip(names, masks, fl, ft): R['grid'][key] = summary(o, mk, sel, w, b[0], a)
            # what the limit of 1 extra move before 2qt takes out: the same with any number of them (H+L <= G-1, any H)
            anyp = oc & one
            R['anyp'] = dict(htr_med=float(np.median(o.per_dr(anyp)[sel])), reach=float(o.found(anyp)[w].mean()) if w.any() else 0.0, found=int(o.found(anyp)[w].sum()))
            # ---- section 3: NISS, under H <= 5 and H+L <= G-2; a longer start's HTRs never in the first pass
            cap = oc & pen[5] & (o.wl <= g - 2)
            opts = [('none', lin), ('n1', o.lev <= 1), ('n2', o.lev <= 2), ('n3', o.lev <= 3)]
            masks = [cap & k for _, k in opts]
            ft = tier_places(o, masks, firsts=(FIRST,), late2=True)
            R['niss'] = {nm: summary(o, mk, sel, w, b[0]) for (nm, _), mk, b in zip(opts, masks, ft)}
            out[case] = R
            x = R['order']; b = R['grid'][f'5_{g - 1}']; c2 = R['grid'][f'5_{g - 2}']
            print(case, 'order', x['htr_med'], round(x['reach'], 4), {k: (x[k]['p50'], x[k]['p95']) for k in ('len', 'skel', 'two3', 'two5', 'two10')},
                  '| H<=5', b['htr_med'], round(b['reach'], 4), b['p50'], '| H<=5, G-2', c2['htr_med'], round(c2['reach'], 4), c2['p50'],
                  '| niss', [(R['niss'][k]['htr_med'], round(R['niss'][k]['reach'], 4), R['niss'][k]['p50']) for k in ('none', 'n1', 'n2', 'n3')], flush=True)
        del t, o, pen
    json.dump(out, open(path('tlimits.json' if len(ms) == 3 else f"tlimits_part{''.join(map(str, ms))}.json"), 'w'), indent=1)
