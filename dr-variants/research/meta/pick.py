"""Pick example DRs from the sample."""
import sys, json
from common import *
PF = {0: 4, 2: 5, 4: 3, 6: 3, 8: 2, 10: 3, 12: 1, 16: 0}
m = int(sys.argv[1])
df, d, q, mm, g = frame(m)
df['plive'] = df.pn0.map(PF) <= (g - df.len); df['both'] = df.plive & (df.rs >= 0)
ok = df[df.ok]
mn = ok[ok.side == 0].groupby('dr').ex.min().reindex(d.index).fillna(99); mi = ok[ok.side == 1].groupby('dr').ex.min().reindex(d.index).fillna(99)
mdq = ok.groupby('dr').dq.min().reindex(d.index).fillna(99)
nb = df[df.both].groupby('dr').size().reindex(d.index).fillna(0)
nr3 = df[(df.rs >= 0) & (df.ex <= 3)].groupby('dr').size().reindex(d.index).fillna(0)
nw = ok.groupby('dr').size().reindex(d.index).fillna(0)
M = []
for l in open(f'../out/meta/niss{m}.tsv'):
    f = l.split('\t')
    if f[0] == 'M': M.append([int(v) for v in f[1:]])
M = pd.DataFrame(M, columns=['dr', 'm', 'j', 'pfx', 'extra', 'slack', 'plive', 'n', 'ns'])
nj = M[(M.ns > 0) & (M.pfx == 0)].assign(lev=lambda t: t.extra).groupby('dr').lev.min().reindex(d.index).fillna(99)
def show(name, sel, k=4):
    s = d[sel]
    print(f'## {name}: {len(s)} DRs')
    for i, r in s.head(k).iterrows():
        print(f'  dr {i} {r.subset} ls {r.ls} normal_min_extra {int(mn[i])} inverse_min_extra {int(mi[i])} niss_min {int(nj[i])} within {int(nw[i])} both-live {int(nb[i])} | {r.scramble}')
show('found on normal with 1 extra, few candidates', d.solv & (mn == 1) & (nb <= 30) & (nb >= 12) & (d.ls == g))
show('only on inverse at low level', d.solv & (mn >= 4) & (mi <= 1))
show('only by NISS after a quarter turn (0-extra prefix, level <= 1)', d.solv & (mn >= 3) & (mi >= 3) & (nj <= 1))
show('only in a skeleton with two more quarter turns', d.solv & (mdq == 2) & (np.minimum(mn, mi) <= 2))
show('no solution; no rule-live variant with S+T <= 3', (~d.solv) & (nr3 == 0))
show('solution exists; no rule-live variant with S+T <= 3', d.solv & (nr3 == 0))
show('needs many extra moves on both sides', d.solv & (mn >= 5) & (mi >= 5))
# baseline rank
df['np0'] = -df.pn0
p0 = policy(df, d, np.ones(len(df), bool), ['len', 'np0'])
p1 = policy(df, d, df.both, ['np0', 'len'])
e0, e1 = p0['exp'], p1['exp']
sel = (e0 > 150) & (e1 <= 2)
print('## baseline needs more than 150 checks, both floors + most pairs needs at most 2:', int(sel.sum()))
for i in e0[sel].index[:4]:
    r = d.loc[i]; print(f'  dr {i} {r.subset} ls {r.ls} baseline {e0[i]:.0f} floors {e1[i]:.1f} | {r.scramble}')
W = ok.assign(fin=ok.total - ok.len)
s = W[(W.keptfin < W.sp0) & (W.fin == 5)].head(2); print('## finish splits a pair that stood at HTR (5-move finish):'); print(s[['dr', 'side', 'len', 'total', 'sp0', 'keptfin']].to_string()); print([d.loc[i].scramble for i in s.dr])
s = W[(W.keep20 == 0) & (W.pn2 >= 4) & (W.ex <= 2)].head(2); print('## trigger splits all 2qt pairs (>= 4 of them):'); print(s[['dr', 'side', 'len', 'total', 'pn2', 'keep20', 'pn0']].to_string()); print([d.loc[i].scramble for i in s.dr])
