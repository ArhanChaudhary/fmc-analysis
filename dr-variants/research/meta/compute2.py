"""Second batch of report numbers: per-level mutual info, the staged meta, bad slices, sides."""
import sys, json
from common import *
PF = {0: 4, 2: 5, 4: 3, 6: 3, 8: 2, 10: 3, 12: 1, 16: 0}
m = int(sys.argv[1])
df, d, q, mm, g = frame(m)
nd = len(d); ns = int(d.solv.sum())
df['A'] = g - df.len
df['plive'] = df.pn0.map(PF) <= df.A; df['rlive'] = df.rs >= 0; df['both'] = df.plive & df.rlive
df['np0'] = -df.pn0
R = {}
def cov(s): return s[s.ok].dr.nunique()
# per level, exact
def per_level(mask, name):
    rows = []
    for k in range(0, 8):
        s = df[mask & (df.ex == k)]
        rows.append(dict(k=k, generated=len(s) / nd, looks=float(s.rlive.sum() / nd), finishes=float(s.both.sum() / nd), within=int(s.ok.sum()), drs=cov(s),
                         precision=float(s.ok.sum() / max(1, s.both.sum())), mi=float(s.ok.sum() / max(1, s.both.sum()) * cov(s))))
    R['level_' + name] = rows
cl = df.cs >= 0
per_level(cl, 'both_all'); per_level(cl & (df.dq == 0), 'both_min'); per_level(cl & (df.dq == 2), 'both_plus2')
per_level(cl & (df.side == 0), 'normal_all'); per_level(cl & (df.side == 1), 'inverse_all'); per_level(cl & (df.e2 <= 1), 'both_all_e2le1')
# by bad slices among rule-live and among both-live
for nm, mask in [('rule', df.rlive), ('both', df.both)]:
    s = df[mask]
    t = s.groupby('bad').agg(n=('ok', 'size'), w=('ok', 'sum'), drs=('dr', lambda v: v[s.loc[v.index, 'ok']].nunique())).reset_index()
    R['bad_' + nm] = t.values.tolist()
    t = s.groupby('nr').agg(n=('ok', 'size'), w=('ok', 'sum'), drs=('dr', lambda v: v[s.loc[v.index, 'ok']].nunique())).reset_index()
    R['nr_' + nm] = t.values.tolist()
# pre-2qt extra among within-goal: fewest e2 per solvable DR
ok = df[df.ok]
for nm, mask in [('all', ok.len > 0), ('min', ok.dq == 0)]:
    t = ok[mask].groupby('dr').e2.min().reindex(d.index[d.solv]).fillna(99).astype(int).value_counts().sort_index()
    R['min_e2_' + nm] = {int(k): int(v) for k, v in t.items()}
    t = ok[mask].groupby('dr').maxsec.min().reindex(d.index[d.solv]).fillna(99).astype(int).value_counts().sort_index()
    R['min_maxsec_' + nm] = {int(k): int(v) for k, v in t.items()}
t = ok.groupby('dr').ex.min().reindex(d.index[d.solv]).fillna(99).astype(int).value_counts().sort_index(); R['min_ex'] = {int(k): int(v) for k, v in t.items()}
t = ok.groupby('dr').dq.min().reindex(d.index[d.solv]).fillna(99).astype(int).value_counts().sort_index(); R['min_dq'] = {int(k): int(v) for k, v in t.items()}
# number of within-goal HTRs per solvable DR (both sides)
t = ok.groupby('dr').size().reindex(d.index[d.solv]).fillna(0)
R['within_per_solvable'] = dict(mean=float(t.mean()), median=float(t.median()), q25=float(t.quantile(.25)), q75=float(t.quantile(.75)), one_or_two=float((t <= 2).mean()))
# staged meta: levels 0..K on both sides, e2 <= 1; finish as you go (most pairs first inside a level) or look first
Ks = (1, 2, 3, 5, 10, 20, 40)
S = {}
for K in [2, 3, 4, 5]:
    for nm, base in [('all', cl), ('min', cl & (df.dq == 0))]:
        mask = base & df.both & (df.e2 <= 1) & (df.ex <= K)
        a = policy(df, d, mask, ['ex', 'np0'], Ks=Ks); b = policy(df, d, mask, ['np0', 'len'], Ks=Ks)
        lk = df[base & df.rlive & (df.e2 <= 1) & (df.ex <= K)].groupby('dr').size().reindex(d.index).fillna(0)
        S[f'{nm}|{K}'] = dict(recall=float(a['found']), asyougo_mean=float(a['mean_found']), asyougo_median=float(a['median']), asyougo_R={str(k): float(v) for k, v in a['recall'].items()},
                              lookfirst_mean=float(b['mean_found']), lookfirst_median=float(b['median']), lookfirst_R={str(k): float(v) for k, v in b['recall'].items()},
                              finishes_unsolv=float(a['size_unsolv']), looks_solv=float(lk[d.solv].mean()), looks_unsolv=float(lk[~d.solv].mean()),
                              routes=df[base & (df.e2 <= 1) & (df.ex <= K)].groupby(['dr', 'side', 'pre2']).ngroups / nd,
                              generated=float((base & (df.e2 <= 1) & (df.ex <= K)).sum() / nd))
R['staged'] = S
# share of solvable DRs where the first within-goal HTR in baseline order is beyond 40 / 100 checks
json.dump(R, open(f'../out/meta/res{m}b.json', 'w'), indent=1, default=lambda o: int(o) if isinstance(o, (np.integer,)) else float(o))
print('done', m)
