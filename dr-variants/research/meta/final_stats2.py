"""Stats for the skeleton/variant meta at S+T <= K (default 4), at most 1 pre-2qt move, both sides, per corner case.
Everything the doc needs for one DR type: the four bounds at the meta's limits, the S+T x pre-2qt grid (S+T 2..5) with
the corner-case-aware bound, where the meta's misses come from, the cost of each bound's too-strict cell inside the
meta, and the corner-case ranking.  "Within-goal DR" = a DR with a leave-slice finish within goal.
usage: final_stats2.py M [K]  -> ../out/meta/final{M}_st{K}.json"""
import sys, json
import numpy as np, pandas as pd
from load import DT, LC, load
from common import first_hit

m = int(sys.argv[1]); K = int(sys.argv[2]) if len(sys.argv) > 2 else 4
pref = f'../out/meta/run{m}'
r = np.fromfile(pref + '.rec', dtype=DT)
_, d, _, _ = load(pref)
g = int(d.goal.iloc[0])
d['wg'] = d.ls <= g
d['case'] = d.subset.str.slice(0, 3)
d = d[d.case != '0c0'].copy()
keepdr = np.isin(r['dr'], d.index.values)
if m == 3:
    x = np.fromfile(pref + '.rules', dtype=np.uint8).reshape(-1, 4)
    fx = np.fromfile(pref + '.compfix', dtype=np.uint8).reshape(-1, 2)
    assert len(x) == len(r) and (x[:, 3] == r['total']).all() and (fx[:, 1] == r['total']).all()
    raw = {'simple': x[:, 0], 'cca': x[:, 1], 'comp': fx[:, 0], 'comp_raw': x[:, 2]}
else:
    x = np.fromfile(pref + '.rules4', dtype=np.uint8).reshape(-1, 5)
    assert len(x) == len(r) and (x[:, 4] == r['total']).all()
    raw = {'simple': x[:, 0], 'cca': x[:, 1], 'comp': x[:, 3], 'comp_raw': x[:, 2]}
r = r[keepdr]; raw = {k: v[keepdr] for k, v in raw.items()}
df = pd.DataFrame({c: r[c] for c in ['dr', 'side', 'pre2', 'q']})
for c in ['kind', 'len', 'lsk', 'total', 'lbc', 'e2']: df[c] = r[c].astype(np.int16)
df['ex'] = df.len - df.lsk
df['sk'] = df.lsk + LC[df.kind.values]
df['ok'] = df.total <= g
del r
inr = df.lbc.values <= g
B = {'none': inr}
for k, v in raw.items(): B[k] = v.astype(np.int16) <= g
for k in ['simple', 'cca', 'comp']: assert not (B[k] & ~inr).any()
print(f'{m}qt: pre-2qt moves on the DR\'s own quarter-turn skeletons:', df.e2[df.q == m].value_counts().to_dict(),
      '| on +2qt skeletons:', df.e2[df.q == m + 2].value_counts().sort_index().to_dict())

KS = (3, 5, 10, 20)
def found(s, dsol):
    grp = s.groupby(['dr', 'sk', 'ex'], sort=True).agg(n=('ok', 'size'), s=('ok', 'sum')).reset_index()
    rec = {}
    for dr, gg in grp.groupby('dr'):
        n = gg.n.values; sc = gg.s.values
        hit = np.nonzero(sc)[0]
        if len(hit) == 0: continue
        i = hit[0]; before = int(n[:i].sum())
        rec[dr] = [first_hit(int(n[i]), int(sc[i]), k - before) for k in KS]
    a = np.array([rec.get(i, [0.0] * len(KS)) for i in dsol])
    return {k: float(a[:, j].mean()) for j, k in enumerate(KS)}

def stats(mask, dg, with_found=True):
    s = df[mask]
    nw = int(dg.wg.sum())
    n = s.groupby('dr').size().reindex(dg.index).fillna(0)
    reached = s[s.ok].dr.nunique()
    return dict(htr_med=float(n.median()), htr_mean=float(n.mean()), share=float(s.ok.mean()) if len(s) else 0.0,
                miss=1 - reached / nw if nw else None, found_all=reached / len(dg),
                found=found(s, dg.index[dg.wg]) if (nw and with_found) else None)

def routes(mask, dg):
    s = df[mask]
    return float(s.groupby(['dr', 'side', 'pre2']).size().groupby('dr').size().reindex(dg.index).fillna(0).median())

EX = df.ex.values; E2 = df.e2.values; Q = df.q.values; OK = df.ok.values
res = dict(m=m, goal=g, K=K, cases={})
for case in sorted(d.case.unique()):
    dg = d[d.case == case]
    inG = df.dr.isin(dg.index).values
    nw = int(dg.wg.sum())
    R = dict(drs=len(dg), wg=nw, bounds={}, grid={}, miss={}, cells={})
    base = inG & (EX <= K) & (E2 <= 1)
    R['routes_meta'] = routes(base & inr, dg)
    for b in ['none', 'simple', 'cca', 'comp']:
        R['bounds'][b] = stats(base & B[b], dg)
    for k in (2, 3, 4, 5):
        for a in (0, 1, 2, 9):
            if a != 9 and a >= k and not (a == 0): continue
            mk = inG & (EX <= k) & (E2 <= a)
            st = stats(mk & B['cca'], dg, with_found=False)
            st['routes'] = routes(mk & inr, dg)
            R['grid'][f'{k},{a}'] = st
    # where the meta's misses come from
    wgd = set(dg.index[dg.wg])
    okm = inG & OK & inr
    s = df[okm & df.dr.isin(wgd).values]
    meta = s[(s.ex <= K) & (s.e2 <= 1) & B['cca'][s.index.values]]
    hit = set(meta.dr); own = set(meta[meta.q == m].dr)
    missed = [i for i in sorted(wgd) if i not in hit]
    # a missed DR with a within-goal HTR inside the meta's limits was lost to the bound; the rest are filed under
    # their cheapest within-goal HTR (fewest S+T, then fewest pre-2qt moves)
    bound = set(s[(s.ex <= K) & (s.e2 <= 1)].dr) - hit
    rest = [i for i in missed if i not in bound]
    bb = s[s.dr.isin(rest)].sort_values(['ex', 'e2']).groupby('dr').head(1)
    assert int(((bb.ex <= K) & (bb.e2 <= 1)).sum()) == 0
    R['miss'] = dict(own=1 - len(own) / nw, meta=1 - len(hit) / nw, next=int((bb.ex == K + 1).sum()),
                     pre2=int(((bb.ex <= K) & (bb.e2 >= 2)).sum()), more=int((bb.ex >= K + 2).sum()),
                     bound=len(bound), beyond=len(rest) - len(bb))
    assert sum(R['miss'][k] for k in ['next', 'pre2', 'more', 'bound', 'beyond']) == len(missed)
    # cost of each bound's too-strict cell inside the meta
    for b in ['simple', 'cca', 'comp_raw']:
        lost = base & OK & inr & ~B[b]
        drs_ok = set(df.dr[base & OK & inr]); drs_kept = set(df.dr[base & OK & B[b]])
        R['cells'][b] = dict(htrs=int(lost.sum()), drs_lost=len(drs_ok - drs_kept))
    res['cases'][case] = R
    bm, bc = R['bounds']['none'], R['bounds']['cca']
    print(f"{case}: DRs {R['drs']} wg {nw} routes {R['routes_meta']:.0f} | none {bm['htr_med']:.0f} 1/{1/bm['share']:.0f} miss {bm['miss']:.3f} f10 {bm['found'][10]:.2f}"
          f" | cca {bc['htr_med']:.0f} 1/{1/bc['share']:.0f} miss {bc['miss']:.3f} f10 {bc['found'][10]:.2f} | miss {R['miss']} | cells {R['cells']}")
json.dump(res, open(f'../out/meta/final{m}_st{K}.json', 'w'), indent=1)
