"""The premove pass in the versions it can be made in, against the meta with every skeleton searched in full on both
sides and no pass.

The pass (the NISS rule of the Suggested Meta): for a skeleton of 3 or more quarter turns that ends with its last one
(HH corners), that turn is made first on the other side and what is left is a DR with one quarter turn fewer, one
move less to the goal, gone through with the meta (its own reading, P <= 1, P+S+T <= 5, the bound; no step 4, since
only one of its sides is searched).

  none      no pass
  written   the pass in place of the full search of those skeletons (the doc)
  added     the pass, then those skeletons in full as well (the meta)

Per corner case and version: chance of missing, within-goal DRs lost and gained against `none`, HTRs to finish,
routes to 2qt and skeletons per DR, found within 5 / 10 / 20 in the page's order.
usage: trule.py M -> ../out/meta/trule{M}.json"""
import sys, json
import numpy as np
from tcommon import T, BYQT, path
from tfinal import META, ORDER_KEY, missr
from torder import found_within

# (in the doc's version one side has to keep its full search, so a skeleton that starts and ends with a quarter turn is
# searched in full on normal and gets the pass on inverse, whatever the run's SVM_REST_BOTH says for the meta)
VERSIONS = [('none', dict(uniss=False)), ('written', dict(uniss=True, rest_hh='keep', rest_both=False)), ('added', dict(uniss='add', rest_hh='keep'))]

if __name__ == '__main__':
    m = int(sys.argv[1])
    res = {}; base = {}
    for name, kw in VERSIONS:
        t = T(m, rest_floor=False, **kw)
        N = t.N('cca')
        fin = META.admit(t, N)
        pre0 = META.admit(t, np.zeros(t.n, np.int16))
        for case in BYQT[m]:
            k = t.rcase == case; sel = t.case == case; w = sel & t.wg
            mask = fin & k
            f = t.found(mask); c = t.per_dr(mask)
            fw = found_within(t, mask, N, ORDER_KEY)
            R = dict(wg=int(w.sum()), drs=int(sel.sum()), miss=missr(f, w), found=int(f[w].sum()), htr_med=float(np.median(c[sel])), htr_mean=float(c[sel].mean()),
                     n=int(mask.sum()), nok=int((mask & t.ok).sum()), within=[float(fw[w][:, j].mean()) if w.any() else 0.0 for j in range(3)],
                     routes_med=float(np.median(t.routes(pre0 & k)[sel])), skel_med=float(np.median(t.skeletons(pre0 & k)[sel])),
                     left_over=int((mask & t.pre).sum()), left_over_ok=int((mask & t.pre & t.ok).sum()))
            if name == 'none':
                # the within-goal HTRs the meta finishes, and which of them are on a skeleton the pass would take the
                # place of (3 or more quarter turns, no corner move after the last one, and on normal no quarter turn
                # at the start as well) with moves after that last quarter turn
                rows = mask & t.ok
                off = (t.q >= 3) & (t.lc == 0) & ~((t.ell[:, 0] == 0) & (t.side == 0))
                base[case] = (f, t.dr[rows], t.tn[rows], (off & (t.tn >= 2))[rows])
            else:
                b, rdr, rtn, rkind = base[case]
                lost = np.nonzero(b & ~f & w)[0]
                R.update(lost=int(len(lost)), gained=int((f & ~b)[w].sum()), lost_drs=[int(v) for v in lost], gained_drs=[int(v) for v in np.nonzero(f & ~b & w)[0]])
                # what the lost DRs have in common: every within-goal HTR the meta finishes without the pass goes on
                # after the last quarter turn of a skeleton the pass takes the place of
                sel_l = np.isin(rdr, lost)
                R.update(lost_all_after=bool(rkind[sel_l].all()), lost_after=[int(rtn[sel_l].min()), int(rtn[sel_l].max())] if sel_l.any() else None)
            res.setdefault(case, {})[name] = R
            print(case, name, {kk: (round(v, 4) if isinstance(v, float) else v) for kk, v in R.items() if not kk.endswith('_drs')}, flush=True)
        del t
    json.dump(res, open(path(f'trule{m}.json'), 'w'), indent=1)
