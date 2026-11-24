"""How to split the spare moves G-L between pre-2qt, S, T and N, using inversion (both sides are searched).
Reading a finish on the inverse reverses its sections, so for a q-qt skeleton the inverse's pre-2qt moves are the
normal's last sections:  q=2: S<->N (T stays);  q=3: pre<->N, S<->T;  q=4: pre(2 sections)<->T+N, S stays;
q=5: pre(3)<->S+T+N;  q=6: pre(4)<->e4+S+T+N.  If extras moved with their sections, every finish would be found on a
side where pre <= its mirror ("canonical" side), so each side may assume N >= floor:
    q=2: S   q=3: pre   q=4: pre-T   q=5: pre-S-T   q=6: e3-S-T   (e3 = extras by the state with 3 qt left)
This script checks that premise (does every within-goal DR have a canonical within-goal HTR?) and grades metas.
usage: spare.py M -> ../out/meta/spare{M}.json"""
import sys, json
import numpy as np, pandas as pd
from load import DT, DTX, LC, load
from common import first_hit

m = int(sys.argv[1]); R = 6; KS = (5, 10, 20)
SKEL = '--skel' in sys.argv          # read sections against the skeleton's own section lengths (acct.py)
SUF = '_skel' if SKEL else ''
pref = f'../out/meta/run{m}'
_, d, _, _ = load(pref)
g = int(d.goal.iloc[0])
d['wg'] = d.ls <= g; d['case'] = d.subset.str.slice(0, 3)
d = d[d.case != '0c0'].copy()
rm = np.memmap(pref + '.rec', dtype=DT, mode='r')
xm = np.memmap(pref + '.ext', dtype=DTX, mode='r')
rules = np.memmap(pref + ('.rules' if m == 3 else '.rules4'), dtype=np.uint8, mode='r').reshape(-1, 4 if m == 3 else 5)
keep = np.isin(rm['dr'], d.index.values) & (rm['lbc'] <= g)
idx = np.nonzero(keep)[0]
c = {k: np.asarray(rm[k][idx]) for k in ['dr', 'side', 'q', 'kind', 'len', 'lsk', 'e2', 'e1', 'total', 'pre2']}
cca = np.asarray(rules[idx, 1]).astype(np.int16)
e3 = np.asarray(xm['e3'][idx]).astype(np.int16)
xa = {k: np.asarray(xm[k][idx]) for k in ['a1', 'a2', 'a3']} if SKEL else None
del rm, xm, rules, keep, idx
I = lambda a: a.astype(np.int16)
q = I(c['q']); lc = LC[c['kind']].astype(np.int16)
L = I(c['lsk']) + lc; B = g - L
pre = I(c['e2']); S = I(c['e1']) - pre; ex = I(c['len']) - I(c['lsk']); T = ex - I(c['e1'])
N = I(c['total']) - I(c['len']) - lc; Nlb = cca - I(c['len']) - lc; ok = c['total'] <= g
assert (pre[q == 2] == 0).all() and (S >= 0).all() and (T >= 0).all()
fits = np.ones(len(q), bool)
if SKEL:
    from acct import skel_acct
    p2, S2, T2, c32, fits = skel_acct(m, c['dr'], c['side'], c['q'], c['kind'], xa['a1'], xa['a2'], xa['a3'], ex)
    print(f'fits a shortest skeleton: {fits.mean():.4f} of HTRs, {fits[c["total"] <= g].mean():.4f} of within-goal ones', flush=True)
    pre = np.where(fits, p2, pre); S = np.where(fits, S2, S); T = np.where(fits, T2, T); e3 = np.where(fits, c32, e3)
    assert (pre + S + T == ex).all()
print(f'bound above the true N (the known cca table error): {(N < Nlb).mean():.5f} of HTRs', flush=True)
assert (ex + N == I(c['total']) - L).all()
floor = np.select([q == 2, q == 3, q == 4, q == 5, q == 6], [S, pre, pre - T, pre - S - T, e3 - S - T], 0).astype(np.int16)
assert ((q != 6) | (e3 <= pre)).all() or SKEL
canon = N >= floor
Neff = np.maximum(Nlb, floor)
dr = c['dr']; side = c['side']; own = q == m
print(f'{m}qt goal {g}: {len(dr):,} corner-feasible HTRs, {d.wg.sum()} within-goal DRs of {len(d)}', flush=True)

res = dict(m=m, goal=g, premise={}, cost={}, pol={})
# 1. the premise: share of within-goal DRs with a canonical within-goal HTR (100% if extras moved with sections)
wgset = d.index[d.wg]
for case in sorted(d.case.unique()):
    dg = d[d.case == case]; w = dg.index[dg.wg]
    inw = np.isin(dr, w)
    any_ok = set(dr[ok & inw]); can_ok = set(dr[ok & canon & inw])
    lim = (pre <= 1) & (ex <= 5) & (ex + Nlb <= B)
    meta_ok = set(dr[ok & inw & lim]); meta_can = set(dr[ok & inw & lim & canon])
    res['premise'][case] = dict(wg=len(w), any=len(any_ok), canon=len(can_ok), meta=len(meta_ok), meta_canon=len(meta_can))
# per qt: share of within-goal HTRs that are canonical, and how far the non-canonical ones miss
for qq in sorted(set(q.tolist())):
    k = ok & (q == qq)
    gap = (floor - N)[k]
    res['premise'][f'q{qq}'] = dict(htrs=int(k.sum()), canon=float(canon[k].mean()),
                                    gap={int(v): int(n) for v, n in zip(*np.unique(gap[gap > 0], return_counts=True))})

# 2. cost: corner-feasible variants per DR (both sides) by (pre, S, T), own quarter turns and +2qt
nd = len(d)
for qq in (m, m + 2):
    k = q == qq
    t = pd.DataFrame({'pre': pre[k], 'S': S[k], 'T': T[k]})
    t = t[(t['pre'] + t['S'] + t['T']) <= 6]
    cnt = t.groupby(['pre', 'S', 'T']).size() / nd
    res['cost'][str(qq)] = {f'{a},{b},{cc}': float(v) for (a, b, cc), v in cnt.items()}

# 3. metas
def found(mask, dg):
    """Found within K finishes, the published order: skeletons shortest first, a first pass of 3 per skeleton,
    fewest extra moves first, ties at random (R orders)."""
    t = pd.DataFrame({'dr': dr[mask], 'sk': (side[mask].astype(np.int64) * 8 + q[mask]) * 8 + c['kind'][mask],
                      'sl': L[mask], 'ex': ex[mask], 'ok': ok[mask]})
    t = t[t.dr.isin(dg.index)]
    t['skel'] = t.groupby(['dr', 'sk'], sort=False).ngroup().values
    rng = np.random.default_rng(1); acc = np.zeros(len(KS)); w = dg.index[dg.wg]
    for _ in range(R):
        u = rng.random(len(t)); v = rng.random(t.skel.max() + 1)[t.skel.values]
        s = t.iloc[np.lexsort((u, t.ex.values, t.skel.values, v, t.sl.values, t.dr.values))]
        rk = s.groupby('skel', sort=False).cumcount().values
        s = s.iloc[np.lexsort((np.arange(len(s)), rk >= 3, s.dr.values))]
        pos = s.groupby('dr', sort=False).cumcount().values
        first = pd.Series(np.where(s.ok.values, pos, 10**9), index=s.dr.values).groupby(level=0).min()
        fw = first.reindex(w).fillna(10**9).values
        acc += [(fw < kk).mean() for kk in KS]
    return {str(kk): float(a / R) for kk, a in zip(KS, acc)}

def grade(name, gen, fin):
    out = {}
    for case in sorted(d.case.unique()):
        dg = d[d.case == case]; inG = np.isin(dr, dg.index.values)
        g_, f_ = gen & inG, fin & inG
        w = dg.index[dg.wg]
        hit = set(dr[f_ & ok])
        nfin = pd.Series(dr[f_]).value_counts().reindex(dg.index).fillna(0)
        ngen = pd.Series(dr[g_]).value_counts().reindex(dg.index).fillna(0)
        rt = pd.DataFrame({'dr': dr[g_], 'side': side[g_], 'p': c['pre2'][g_]}).drop_duplicates().dr.value_counts().reindex(dg.index).fillna(0)
        out[case] = dict(miss=1 - sum(i in hit for i in w) / len(w), fin_med=float(nfin.median()), fin_mean=float(nfin.mean()),
                         gen_med=float(ngen.median()), routes_med=float(rt.median()), found=found(f_, dg))
    res['pol'][name] = out
    print(name, ' | '.join(f"{k} miss {v['miss']:.3f} fin {v['fin_med']:.0f} gen {v['gen_med']:.0f} rt {v['routes_med']:.0f} f20 {v['found']['20']:.2f}" for k, v in out.items()), flush=True)

cap = lambda a, kk: (pre <= a) & (ex <= kk)
INF = 99
if 'rules' in sys.argv[2:]:   # simple hand rules for where the second pre-2qt move goes
    for name, gen in [('published + floor', cap(1, 5)),
                      ('2nd pre-2qt move only with S=0', cap(1, 5) | ((pre == 2) & (S == 0) & (ex <= 5))),
                      ('2nd pre-2qt move only with S=0, T<=2', cap(1, 5) | ((pre == 2) & (S == 0) & (T <= 2))),
                      ('pre counts double: 2pre+S+T<=6', (2 * pre + S + T <= 6)),
                      ('pre counts double: 2pre+S+T<=5', (2 * pre + S + T <= 5)),
                      ('pre<=2, S+T<=5', cap(2, 5)),
                      ('early counts double: 2e+rest<=6', np.where(q == 2, 2 * S + T, 2 * pre + S + T) <= 6),
                      ('early counts double: 2e+rest<=5', np.where(q == 2, 2 * S + T, 2 * pre + S + T) <= 5)]:
        grade(name, gen, gen & (ex + Neff <= B))
    json.dump(res['pol'], open(f'../out/meta/spare{m}_rules{SUF}.json', 'w'), indent=1)
    sys.exit()
grade('published: S+T<=5, pre<=1, cca', cap(1, 5), cap(1, 5) & (ex + Nlb <= B))
grade("doc's wording: S+T+N<=min(G-L,5), pre<=1", cap(1, 5), cap(1, 5) & (ex + Nlb <= np.minimum(B, 5)))
grade('published + floor', cap(1, 5), cap(1, 5) & (ex + Neff <= B))
grade('S+T<=5, pre<=2, floor', cap(2, 5), cap(2, 5) & (ex + Neff <= B))
grade('S+T<=6, pre<=2, floor', cap(2, 6), cap(2, 6) & (ex + Neff <= B))
grade('no caps, floor', cap(INF, INF), ex + Neff <= B)
grade('no caps, no floor', cap(INF, INF), ex + Nlb <= B)
json.dump(res, open(f'../out/meta/spare{m}{SUF}.json', 'w'), indent=1)
print(json.dumps(res['premise'], indent=None))
