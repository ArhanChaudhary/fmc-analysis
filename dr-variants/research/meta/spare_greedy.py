"""Greedy choice of (skeleton qt, pre, S, T) cells: which cells reach the most within-goal DRs per variant considered,
with the canonical floor (spare.py) and the corner-case-aware bound deciding which HTRs get finished.
Also lists within-goal DRs with no canonical within-goal HTR (premise failures) for witnesses.
usage: spare_greedy.py M -> ../out/meta/greedy{M}.json"""
import sys, json
import numpy as np, pandas as pd
from load import DT, DTX, LC, load

m = int(sys.argv[1])
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
c = {k: np.asarray(rm[k][idx]) for k in ['dr', 'side', 'q', 'kind', 'len', 'lsk', 'e2', 'e1', 'total']}
cca = np.asarray(rules[idx, 1]).astype(np.int16); e3 = np.asarray(xm['e3'][idx]).astype(np.int16)
del rm, xm, rules, keep, idx
I = lambda a: a.astype(np.int16)
q = I(c['q']); lc = LC[c['kind']].astype(np.int16); L = I(c['lsk']) + lc; B = g - L
pre = I(c['e2']); S = I(c['e1']) - pre; ex = I(c['len']) - I(c['lsk']); T = ex - I(c['e1'])
N = I(c['total']) - I(c['len']) - lc; Nlb = cca - I(c['len']) - lc; ok = c['total'] <= g
floor = np.select([q == 2, q == 3, q == 4, q == 5, q == 6], [S, pre, pre - T, pre - S - T, e3 - S - T], 0).astype(np.int16)
fin = ex + np.maximum(Nlb, floor) <= B
dr = c['dr']; nd = len(d)
cell = ((q - m) // 2 * 1000 + pre * 100 + S * 10 + T).astype(np.int32)
lim = (pre <= 4) & (ex <= 8)
t = pd.DataFrame({'dr': dr[lim], 'cell': cell[lim], 'good': (ok & fin)[lim], 'fin': fin[lim]})
cost = t.groupby('cell').size() / nd                          # variants considered per DR
fcost = t[t.fin].groupby('cell').size() / nd                  # HTRs finished per DR
cov = t[t.good].groupby('cell').dr.apply(lambda s: set(s.unique()))
wg = set(d.index[d.wg]); W = len(wg)
covered, chosen, spent, fspent, out = set(), [], 0.0, 0.0, []
cand = set(cov.index)
while cand:
    best = max(cand, key=lambda k: (len(cov[k] - covered) / cost[k], -cost[k]))
    gain = len(cov[best] - covered)
    if gain == 0: break
    covered |= cov[best]; cand.discard(best); spent += cost[best]; fspent += fcost.get(best, 0.0)
    out.append(dict(cell=int(best), skel=f'+{best // 1000 * 2}qt' if best >= 1000 else 'own', pre=int(best % 1000 // 100),
                    S=int(best % 100 // 10), T=int(best % 10), gain=gain, cost=float(cost[best]),
                    reach=len(covered) / W, considered=spent, finished=fspent))
    if len(covered) / W > 0.995 or len(out) > 80: break
# where the published meta and alternatives sit on the same cost scale
def region(mask):
    mk = mask & lim
    tt = pd.DataFrame({'dr': dr[mk], 'good': (ok & fin)[mk]})
    return dict(reach=tt[tt.good].dr.nunique() / W, considered=len(tt) / nd, finished=float(fin[mk].sum() / nd))
ref = {'published caps + floor': region((pre <= 1) & (ex <= 5)), 'pre<=2, S+T<=5 + floor': region((pre <= 2) & (ex <= 5)),
       'pre<=2, S+T<=4 + floor': region((pre <= 2) & (ex <= 4)), 'pre<=1, S+T<=4 + floor': region((pre <= 1) & (ex <= 4))}
# premise failures: within-goal DRs with no canonical within-goal HTR anywhere
can = set(dr[ok & (N >= floor)])
fails = sorted(i for i in wg if i not in can)
fl = []
for i in fails[:40]:
    k = (dr == i) & ok
    fl.append(dict(dr=int(i), case=d.case[i], scramble=d.scramble[i], ls=int(d.ls[i]),
                   htrs=[dict(side=int(c['side'][j]), q=int(q[j]), L=int(L[j]), pre=int(pre[j]), S=int(S[j]), T=int(T[j]), N=int(N[j]), floor=int(floor[j]))
                         for j in np.nonzero(k)[0][:12]]))
json.dump(dict(m=m, goal=g, W=W, greedy=out, ref=ref, fails=fl, nfails=len(fails)), open(f'../out/meta/greedy{m}.json', 'w'), indent=1)
print(f'{m}qt: {W} within-goal DRs, {len(fails)} with no canonical within-goal HTR')
for r in ref.items(): print(' ', r)
for o in out[:40]:
    print(f"  {o['skel']:>5} pre {o['pre']} S {o['S']} T {o['T']}: +{o['gain']:4d} DRs for {o['cost']:7.1f} variants -> reach {o['reach']:.3f}, considered {o['considered']:7.0f}, finished {o['finished']:6.0f}")
