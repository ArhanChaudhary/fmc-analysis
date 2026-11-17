"""Mid-skeleton NISS: what it adds over searching the normal and the inverse scramble."""
import sys, json
from common import *
pd.set_option('display.width', 250); pd.set_option('display.max_rows', 400)
PF = {0: 4, 2: 5, 4: 3, 6: 3, 8: 2, 10: 3, 12: 1, 16: 0}
m = int(sys.argv[1])
df, d, q, mm, g = frame(m)
nd = len(d); ns = int(d.solv.sum())
df['plive'] = df.pn0.map(PF) <= (g - df.len); df['both'] = df.plive & (df.rs >= 0)
Q, M = [], []
for l in open(f'../out/meta/niss{m}.tsv'):
    f = l.split('\t')
    if f[0] == 'Q': Q.append([int(v) for v in f[1:]])
    elif f[0] == 'M': M.append([int(v) for v in f[1:]])
Q = pd.DataFrame(Q, columns=['dr', 'm', 'j', 'npre0', 'npre1'])
M = pd.DataFrame(M, columns=['dr', 'm', 'j', 'pfx', 'extra', 'slack', 'plive', 'n', 'ns'])
M = M[M.dr.isin(d.index)]; Q = Q[Q.dr.isin(d.index)]
M['lev'] = M.pfx + M.extra
solv = set(d.index[d.solv])
out = {'prefixes': Q.groupby('j')[['npre0', 'npre1']].mean().round(2).reset_index().values.tolist()}
print(f'm={m} goal={g} solvable {ns}')
print('prefixes per DR (0 extra, 1 extra) by quarter turn of the NISS:'); print(Q.groupby('j')[['npre0', 'npre1']].mean().round(1).to_string())
rows = []
for k in range(0, 7):
    A = set(df[df.ok & (df.ex <= k) & (df.side == 0)].dr); B = set(df[df.ok & (df.ex <= k) & (df.side == 1)].dr)
    AB = A | B
    row = dict(k=k, normal=len(A) / ns, both=len(AB) / ns)
    allj = set()
    for j in sorted(M.j.unique()):
        for pmax in [0, 1]:
            s = M[(M.j == j) & (M.pfx <= pmax) & (M.lev <= k)]
            J = set(s[s.ns > 0].dr)
            row[f'niss{j}_p{pmax}_alone'] = len(J) / ns
            row[f'niss{j}_p{pmax}_adds'] = len(J - AB) / ns
            row[f'niss{j}_p{pmax}_looks'] = s[s.slack >= 0].n.sum() / nd
            row[f'niss{j}_p{pmax}_fin'] = s[(s.slack >= 0) & (s.plive == 1)].n.sum() / nd
            row[f'niss{j}_p{pmax}_within'] = s.ns.sum() / nd
            if pmax == 1: allj |= J
    row['with_all_niss'] = len(AB | allj) / ns
    s = df[(df.ex <= k)]
    row['ni_looks'] = float((s.rs >= 0).sum() / nd); row['ni_fin'] = float(s.both.sum() / nd)
    rows.append(row)
t = pd.DataFrame(rows)
print(t[['k', 'normal', 'both', 'with_all_niss', 'ni_looks', 'ni_fin']].round(3).to_string(index=False))
for j in sorted(M.j.unique()):
    cols = ['k'] + [f'niss{j}_p{p}_{x}' for p in [0, 1] for x in ['alone', 'adds', 'looks', 'fin']]
    print(f'NISS after quarter turn {j}:'); print(t[cols].round(3).to_string(index=False))
out['rows'] = rows
# what is left after both sides at level k: found by going one level deeper on both sides, or by NISS at level k?
rows2 = []
for k in range(0, 6):
    AB = set(df[df.ok & (df.ex <= k)].dr); AB1 = set(df[df.ok & (df.ex <= k + 1)].dr)
    s = M[(M.pfx <= 1) & (M.lev <= k)]; J = set(s[s.ns > 0].dr)
    rows2.append(dict(k=k, missed=1 - len(AB) / ns, deeper_gets=len(AB1 - AB) / ns, niss_gets=len(J - AB) / ns,
                      deeper_looks=float(((df.ex == k + 1) & (df.rs >= 0)).sum() / nd), deeper_fin=float(((df.ex == k + 1) & df.both).sum() / nd),
                      niss_looks=float(s[s.slack >= 0].n.sum() / nd), niss_fin=float(s[(s.slack >= 0) & (s.plive == 1)].n.sum() / nd)))
print('after both sides to level k: what the next level on both sides gets, and what NISS (all quarter turns, prefix <= 1 extra, level <= k) gets')
print(pd.DataFrame(rows2).round(3).to_string(index=False))
out['rows2'] = rows2
# precision of NISS candidates that pass both floors
s = M[(M.slack >= 0) & (M.plive == 1) & (M.pfx <= 1)]
t2 = s.groupby(['j', 'lev']).agg(n=('n', 'sum'), ns=('ns', 'sum')).reset_index(); t2['prec'] = t2.ns / t2.n
print('precision of a NISS candidate that passes both floors, by quarter turn and level'); print(t2.round(3).to_string(index=False))
out['prec'] = t2.values.tolist()
json.dump(out, open(f'../out/meta/niss{m}.json', 'w'), indent=1, default=float)
