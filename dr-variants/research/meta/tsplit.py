"""Where the meta's skeletons and routes to 2qt come from: skeletons with the DR's own quarter turns, skeletons with
two more, and among those the ones with a cancelling pair (two quarter turns with nothing between them in the
skeleton, e.g. `D' F2 B2 U` in a solution).  Skeletons and routes are counted before the bound and the most-pairs
step, like the page's; HTRs and misses after both.
usage: tsplit.py -> ../out/meta/tsplit.json"""
import sys, json
import numpy as np
from tcommon import T, BYQT, path
from tfinal import META, finished

res = {}
for m in (2, 3, 4):
    t = T(m)
    Z = np.zeros(t.n, np.int16)
    post = finished(t, META, 'cca'); pre = META.admit(t, Z)
    own = t.qsk == m; pair = t.emptymid
    assert not (own & pair).any() or m > 2
    for case in BYQT[m]:
        sel = t.case == case; w = sel & t.wg
        k = t.rcase == case
        def med(x): return float(np.median(x[sel]))
        def miss(mask): return float(1 - t.found(post & k & mask)[w].mean()) if w.any() else None
        parts = {'all': np.ones(t.n, bool), 'own': own, 'more': ~own, 'more_plain': ~own & ~pair, 'more_pair': ~own & pair, 'no_pair': ~pair}
        r = {}
        for nm, mk in parts.items():
            r[nm] = dict(skeletons=med(t.skeletons(pre & k & mk)), routes=med(t.routes(pre & k & mk)), htrs=med(t.per_dr(post & k & mk)), miss=miss(mk))
        res[case] = r
        print(case, {nm: (v['skeletons'], v['routes'], round(100 * v['miss'], 1) if v['miss'] is not None else None) for nm, v in r.items()}, flush=True)
json.dump(res, open(path('tsplit.json'), 'w'), indent=1)
