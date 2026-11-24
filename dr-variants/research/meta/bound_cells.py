"""What the too-strict cells of each bound cost: within-goal HTRs discarded and solvable DRs lost, in the whole
sample (every HTR in reach) and inside the meta (S+T <= 3, at most 1 pre-2qt move).  Comprehensive as written
(H-H 0 bad cs/fr 0/0 = +1).  usage: bound_cells.py M"""
import sys, json
import numpy as np
from load import DT, load
m = int(sys.argv[1]); pref = f'../out/meta/run{m}'
r = np.fromfile(pref + '.rec', dtype=DT)
_, d, _, _ = load(pref)
g = int(d.goal.iloc[0])
keep = np.isin(r['dr'], d.index[~d.subset.str.startswith('0c0')].values)
if m == 3:
    x = np.fromfile(pref + '.rules', dtype=np.uint8).reshape(-1, 4); cols = {'simple': 0, 'cca': 1, 'comp': 2}; tot = 3
else:
    x = np.fromfile(pref + '.rules4', dtype=np.uint8).reshape(-1, 5); cols = {'simple': 0, 'cca': 1, 'comp': 2}; tot = 4
assert len(x) == len(r) and (x[:, tot] == r['total']).all()
r, x = r[keep], x[keep]
ok = (r['total'] <= g) & (r['lbc'] <= g)
meta = (r['len'].astype(int) - r['lsk'] <= 3) & (r['e2'] <= 1)
out = {}
for b, j in cols.items():
    kept = x[:, j] <= g
    res = {}
    for scope, mk in [('all', np.ones(len(r), bool)), ('meta', meta)]:
        lost = ok & mk & ~kept
        drs_ok = set(r['dr'][ok & mk]); drs_kept = set(r['dr'][ok & mk & kept])
        res[scope] = dict(htrs=int(lost.sum()), drs_hit=int(len(set(r['dr'][lost]))), drs_lost=len(drs_ok - drs_kept))
    out[b] = res
    print(m, b, res)
json.dump(out, open(f'../out/meta/cells{m}.json', 'w'))
