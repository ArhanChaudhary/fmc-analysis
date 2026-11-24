"""Found within K finishes in the solver's order: skeletons shortest first (ties at random), each skeleton's variants
fewest extra moves first (ties at random), at most C finishes per skeleton before moving on.  The meta's limits:
S+T <= 5, at most 1 pre-2qt move, both sides.  Averaged over R random tie orders.
usage: found_order.py M -> ../out/meta/found{M}.json"""
import sys, json
import numpy as np, pandas as pd
from load import DT, LC, load
m = int(sys.argv[1]); R = 20; KS = (5, 10, 20); CAPS = (0, 10, 5, 3, 2, 1)   # 0 = no cap
pref = f'../out/meta/run{m}'
r = np.fromfile(pref + '.rec', dtype=DT)
_, d, _, _ = load(pref)
g = int(d.goal.iloc[0]); d['wg'] = d.ls <= g; d['case'] = d.subset.str.slice(0, 3)
d = d[d.case != '0c0']
rules = np.fromfile(pref + ('.rules' if m == 3 else '.rules4'), dtype=np.uint8).reshape(-1, 4 if m == 3 else 5)
keep = np.isin(r['dr'], d.index.values)
r, rules = r[keep], rules[keep]
ex = r['len'].astype(np.int16) - r['lsk']
lim = (ex <= 5) & (r['e2'] <= 1) & (r['lbc'] <= g)
BOUND = {'none': r['lbc'], 'cca': rules[:, 1]}
res = {'m': m, 'goal': g, 'cases': {}}
rng = np.random.default_rng(1)
for bname, bv in BOUND.items():
    mk = lim & (bv <= g)
    t = pd.DataFrame({'dr': r['dr'][mk], 'side': r['side'][mk], 'q': r['q'][mk], 'kind': r['kind'][mk],
                      'sl': (r['lsk'][mk] + LC[r['kind'][mk]]).astype(np.int16), 'ex': ex[mk], 'ok': r['total'][mk] <= g})
    t['skel'] = t.groupby(['dr', 'side', 'q', 'kind'], sort=False).ngroup().values
    nsk = t.skel.max() + 1
    acc = {}
    for rep in range(R):
        u = rng.random(len(t)); v = rng.random(nsk)[t.skel.values]
        o = np.lexsort((u, t.ex.values, t.skel.values, v, t.sl.values, t.dr.values))   # last key sorts first
        s = t.iloc[o]
        rank_in_skel = s.groupby('skel', sort=False).cumcount().values
        for cap in CAPS:
            for mode in (('cap', 'two') if cap else ('cap',)):
                if mode == 'cap':
                    sc = s[rank_in_skel < cap] if cap else s
                else:   # a first pass of at most `cap` per skeleton, then the rest in the same order
                    o2 = np.lexsort((np.arange(len(s)), rank_in_skel >= cap, s.dr.values))
                    sc = s.iloc[o2]
                pos = sc.groupby('dr', sort=False).cumcount().values
                first = pd.Series(np.where(sc.ok.values, pos, 10**9), index=sc.dr.values).groupby(level=0).min()
                n = sc.groupby('dr').size()
                key = f'{cap}' if mode == 'cap' else f'{cap}+rest'
                for case in d.case.unique():
                    dg = d[d.case == case]; w = dg.index[dg.wg]
                    fw = first.reindex(w).fillna(10**9).values
                    a = acc.setdefault((case, key), {'found': np.zeros(len(KS)), 'all': 0.0, 'n': 0.0})
                    a['found'] += [(fw < k).mean() for k in KS]
                    a['all'] += (fw < 10**9).mean()
                    a['n'] += n.reindex(dg.index).fillna(0).median()
    for (case, cap), a in acc.items():
        res['cases'].setdefault(case, {}).setdefault(bname, {})[cap] = {
            'found': {str(k): a['found'][j] / R for j, k in enumerate(KS)}, 'found_all': a['all'] / R, 'htr_med': a['n'] / R}
    print(bname, 'done', flush=True)
for case, v in sorted(res['cases'].items()):
    for b in ('none', 'cca'):
        for cap in v[b]:
            x = v[b][cap]
            print(f"{case} {b:4s} cap {cap:>7s}: within 5/10/20 {x['found']['5']:.2f} {x['found']['10']:.2f} {x['found']['20']:.2f} | at all {x['found_all']:.3f} | finished per DR {x['htr_med']:.0f}")
json.dump(res, open(f'../out/meta/found{m}.json', 'w'), indent=1)
