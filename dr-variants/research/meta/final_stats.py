"""Stats for the skeleton/variant meta, per corner case, for the 2qt / 3qt / 4qt DR samples (goals 12 / 13 / 14).

The meta: on both sides, every variant with S+T <= 3 (extra moves over the skeleton on the way to HTR, counting any
before 2qt), at most 1 of them before 2qt; a variant is finished when its bound fits the goal.  Bounds: none (moves to
HTR + the corner case's own moves), simple, corner-case-aware, comprehensive (with its one cell that isn't a floor set
to the case's own minimum).  Finishing order: shortest skeleton first (moves to HTR + corner moves), then fewest
extra moves; ties in random order (expected first hit).

usage: final_stats.py M  -> ../out/meta/final{M}.json
"""
import sys, json
import numpy as np, pandas as pd
from load import DT, LC, load
from common import first_hit

m = int(sys.argv[1])
pref = f'../out/meta/run{m}'
r = np.fromfile(pref + '.rec', dtype=DT)
_, d, _, _ = load(pref)
g = int(d.goal.iloc[0])
d['solv'] = d.ls <= g
d['case'] = d.subset.str.slice(0, 3)
d = d[d.case != '0c0'].copy()             # a 2qt DR is a 4a2 or 4b2 (as in common.frame)
keepdr = np.isin(r['dr'], d.index.values)
r = r[keepdr]
df = pd.DataFrame({c: r[c] for c in ['dr', 'side', 'pre2', 'e2']})
for c in ['kind', 'len', 'lsk', 'total', 'lbc']: df[c] = r[c].astype(np.int16)
df['ex'] = df.len - df.lsk
df['sk'] = df.lsk + LC[df.kind.values]   # skeleton length: moves to HTR + the corner case's own moves
df['ok'] = df.total <= g
del r

if m == 3:
    x = np.fromfile(pref + '.rules', dtype=np.uint8).reshape(-1, 4)
    fx = np.fromfile(pref + '.compfix', dtype=np.uint8).reshape(-1, 2)
    x, fx = x[keepdr], fx[keepdr]
    assert len(x) == len(df) and (x[:, 3] == df.total.values).all() and (fx[:, 1] == df.total.values).all()
    B = {'none': df.lbc.values, 'simple': x[:, 0], 'cca': x[:, 1], 'comp': fx[:, 0]}
else:
    x = np.fromfile(pref + '.rules4', dtype=np.uint8).reshape(-1, 5)[keepdr]
    assert len(x) == len(df) and (x[:, 4] == df.total.values).all()
    B = {'none': df.lbc.values, 'simple': x[:, 0], 'cca': x[:, 1], 'comp': x[:, 3]}
B = {k: (np.asarray(v).astype(np.int16) <= g) for k, v in B.items()}
inr = B['none']
for k, v in B.items():
    assert not (v & ~inr).any(), f'{k} keeps an HTR out of reach'
    lost = inr & df.ok.values & ~v
    print(f'{k:6s} within-goal HTRs it discards: {int(lost.sum())} on {df.dr[lost].nunique()} DRs')

KS = (3, 5, 10, 20)
def found(s, dsol):
    """Per solvable DR: chance that one of the first K finishes (skeleton length, then extra moves) is within goal."""
    grp = s.groupby(['dr', 'sk', 'ex'], sort=True).agg(n=('ok', 'size'), s=('ok', 'sum')).reset_index()
    rec = {}
    for dr, gg in grp.groupby('dr'):
        n = gg.n.values; sc = gg.s.values
        hit = np.nonzero(sc)[0]
        if len(hit) == 0: continue
        i = hit[0]; before = int(n[:i].sum())
        rec[dr] = [first_hit(int(n[i]), int(sc[i]), K - before) for K in KS]
    a = np.array([rec.get(i, [0.0] * len(KS)) for i in dsol])
    return {K: float(a[:, j].mean()) for j, K in enumerate(KS)}

def stats(mask, dg, routes=True):
    s = df[mask]
    ns = int(dg.solv.sum())
    n = s.groupby('dr').size().reindex(dg.index).fillna(0)
    nu = n[~dg.solv.values]
    reached = s[s.ok].dr.nunique()
    out = dict(htr_med=float(n.median()), htr_mean=float(n.mean()), htr_nosol_med=float(nu.median()) if len(nu) else None,
               share=float(s.ok.mean()) if len(s) else 0.0, miss=1 - reached / ns if ns else None,
               found=found(s, dg.index[dg.solv]) if ns else None)
    return out

def routes(mask, dg):
    s = df[mask]
    return float(s.groupby(['dr', 'side', 'pre2']).size().groupby('dr').size().reindex(dg.index).fillna(0).median())

res = dict(m=m, goal=g, cases={})
EX = df.ex.values; E2 = df.e2.values
for case in sorted(d.case.unique()):
    dg = d[d.case == case]
    inG = df.dr.isin(dg.index).values
    R = dict(drs=len(dg), solvable=int(dg.solv.sum()), meta={}, bounds={}, grid={})
    base = inG & (EX <= 3) & (E2 <= 1)
    R['routes_meta'] = routes(base & inr, dg)
    for b in B:
        R['bounds'][b] = stats(base & B[b], dg)
    for k in (2, 3, 4):
        for a in (0, 1, 2, 9):
            if a != 9 and a > k: continue
            mk = inG & (EX <= k) & (E2 <= a)
            st = stats(mk & B['cca'], dg)
            st['routes'] = routes(mk & inr, dg)
            R['grid'][f'{k},{a}'] = st
    res['cases'][case] = R
    bm, bc = R['bounds']['none'], R['bounds']['cca']
    print(f"{case}: DRs {R['drs']} solvable {R['solvable']} routes {R['routes_meta']:.0f} | none {bm['htr_med']:.0f} 1/{1/bm['share']:.0f} miss {bm['miss']:.3f} f5 {bm['found'][5]:.2f} f10 {bm['found'][10]:.2f}"
          f" | cca {bc['htr_med']:.0f} 1/{1/bc['share']:.0f} miss {bc['miss']:.3f} f5 {bc['found'][5]:.2f} f10 {bc['found'][10]:.2f}")
json.dump(res, open(f'../out/meta/final{m}.json', 'w'), indent=1)
