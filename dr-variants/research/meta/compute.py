"""Every number of the search-meta report for one quarter-turn count -> ../out/meta/res{m}.json"""
import sys, json
from common import *
PF = {0: 4, 2: 5, 4: 3, 6: 3, 8: 2, 10: 3, 12: 1, 16: 0}     # exact pair floor over the 663,552 HTR states
m = int(sys.argv[1])
df, d, q, mm, g = frame(m)
nd = len(d); ns = int(d.solv.sum())
df['A'] = g - df.len
df['pf'] = df.pn0.map(PF).astype(int); df['ps'] = df.A - df.pf
df['plive'] = df.ps >= 0; df['rlive'] = df.rs >= 0; df['clive'] = df.cs >= 0; df['tlive'] = df.ts >= 0
df['both'] = df.rlive & df.plive
df['post'] = df.ex - df.e2
# the intermediate rule: bad slices only (0 / +3, +2 for R-V and F-V corners / +5)
nint = np.where(df.bad == 0, 0, np.where(df.bad == 1, np.where(df.kind.isin([3, 4]), 2, 3), 5))
df['ilive'] = (df.len + LC[df.kind.values] + nint) <= g
# simple pair floor a solver can remember: 16 - 4 * moves left
df['plive_simple'] = df.pn0 >= 16 - 4 * df.A
assert not (df.ok & ~df.plive).any() and not (df.ok & ~df.rlive).any() and not (df.ok & ~df.tlive).any() and not (df.ok & ~df.plive_simple).any()
R = {'m': m, 'goal': g, 'drs': nd, 'solvable': ns, 'records': int(len(df))}
R['ls_hist'] = d.ls.value_counts().sort_index().to_dict()
R['unreached'] = int(ns - df[df.ok].dr.nunique())    # solvable DRs whose within-goal solutions all have more than m+2 quarter turns

def cov(s): return s[s.ok].dr.nunique() / ns
def funnel(mask):
    s = df[mask]
    return dict(per_dr=len(s) / nd, per_unsolv=len(s[~s.dr.map(d.solv)]) / (nd - ns), within=int(s.ok.sum()), precision=float(s.ok.mean()) if len(s) else 0.0, recall=cov(s))
allm = np.ones(len(df), bool)
R['funnel'] = {k: funnel(v) for k, v in {
    'all': allm, 'corner': df.clive, 'intermediate': df.ilive, 'rule': df.rlive, 'table': df.tlive, 'pair': df.plive, 'pair_simple': df.plive_simple,
    'rule+pair': df.both, 'rule+pair_simple': df.rlive & df.plive_simple, 'intermediate+pair': df.ilive & df.plive, 'table+pair': df.tlive & df.plive}.items()}
# rule violations would show here (none): within-goal variants per filter are equal
# by level (cumulative total extra moves), sides and skeleton sets
def levels(mask):
    rows = []
    for k in range(0, 9):
        s = df[mask & (df.ex <= k)]
        rows.append(dict(k=k, generated=len(s) / nd, looks=float(s.rlive.sum() / nd), finishes=float(s.both.sum() / nd), within=float(s.ok.sum() / nd), recall=cov(s),
                         unsolv_finishes=float(s.both[~s.dr.map(d.solv)].sum() / (nd - ns))))
    return rows
cl = df.clive
R['levels'] = {'both_all': levels(cl), 'both_min': levels(cl & (df.dq == 0)), 'normal_all': levels(cl & (df.side == 0)), 'normal_min': levels(cl & (df.side == 0) & (df.dq == 0)),
               'inverse_all': levels(cl & (df.side == 1)), 'inverse_min': levels(cl & (df.side == 1) & (df.dq == 0))}
# grid: extra moves before 2qt (a) and after (b)
def grid(mask):
    out = []
    for a in range(0, 4):
        for b in range(0, 8):
            s = df[mask & (df.e2 <= a) & (df.post <= b)]
            out.append(dict(a=a, b=b, routes=s.groupby(['dr', 'side', 'pre2']).ngroups / nd, generated=len(s) / nd, looks=float(s.rlive.sum() / nd), finishes=float(s.both.sum() / nd),
                            recall=cov(s), precision=float(s.ok.sum() / max(1, s.both.sum()))))
    return out
R['grid'] = {'both_min': grid(cl & (df.dq == 0)), 'both_all': grid(cl), 'normal_min': grid(cl & (df.dq == 0) & (df.side == 0)), 'normal_all': grid(cl & (df.side == 0))}
# precision cards among rule-live HTRs
L = df[df.rlive]
t = L.groupby(['A', 'pn0']).ok.agg(['size', 'sum']).reset_index()
R['card_A_pairs'] = t.values.tolist()
t = L[L.plive].groupby(['rs', 'ps']).ok.agg(['size', 'sum']).reset_index(); R['card_rs_ps'] = t.values.tolist()
for col in ['rs', 'ts', 'cs']:
    t = df.groupby(col).ok.agg(['size', 'sum']).reset_index(); R['by_' + col] = t.values.tolist()
t = L.groupby('ex').agg(n=('ok', 'size'), w=('ok', 'sum')).reset_index(); R['rule_by_ex'] = t.values.tolist()
for col in ['pn0', 'pn1', 'pn2']:
    t = L.groupby(col).ok.agg(['size', 'sum']).reset_index(); R['rule_by_' + col] = t.values.tolist()
t = df[df.both].groupby('pn0').ok.agg(['size', 'sum']).reset_index(); R['both_by_pn0'] = t.values.tolist()
# AUC of pair counts
def auc(col, src):
    a = src[src.ok][col].values; b = src[~src.ok][col].values
    if len(a) == 0 or len(b) == 0: return None
    r = pd.Series(np.concatenate([a, b])).rank().values
    return float((r[:len(a)].sum() - len(a) * (len(a) + 1) / 2) / (len(a) * len(b)))
R['auc'] = {c: auc(c, L) for c in ['pn2', 'pn1', 'pn0']}
R['auc_all'] = {c: auc(c, df) for c in ['pn2', 'pn1', 'pn0']}
# pairs broken
W = df[df.ok]
R['pairs_within'] = dict(n=int(len(W)), p2=float(W.pn2.mean()), keep20=float(W.keep20.mean()), trig_split=float((W.keep20 < W.pn2).mean()), p0=float(W.sp0.mean()),
                         keptfin=float(W.keptfin.mean()), fin_split=float((W.keptfin < W.sp0).mean()),
                         fin_split_by_fin=W.assign(fin=W.total - W.len, b=(W.keptfin < W.sp0)).groupby('fin').b.agg(['size', 'mean']).reset_index().values.tolist(),
                         trig_split_rule_live=float((L.keep20 < L.pn2).mean()), gain=float((W.pn0 - W.pn2).mean()), gain_rule_live=float((L.pn0 - L.pn2).mean()))
# skeletons
V = df[cl]
sk = V.groupby(['dr', 'side', 'q', 'kind']).agg(M=('M', 'first'), dq=('dq', 'first'), has=('ok', 'any'), live=('both', 'sum')).reset_index()
R['skeletons_per_dr'] = {'min': len(sk[sk.dq == 0]) / nd, 'plus2': len(sk[sk.dq == 2]) / nd}
t = sk.groupby(['dq', 'M']).agg(n=('has', 'size'), has=('has', 'sum'), drs=('dr', lambda v: v[sk.loc[v.index, 'has']].nunique())).reset_index()
R['skeleton_by_M'] = t.values.tolist()
best = sk[sk.dq == 0].sort_values('M', ascending=False).groupby('dr').head(1)
R['best_skeleton_has'] = float(best.has.sum() / ns)     # share of solvable DRs whose largest-M min-qt skeleton holds a within-goal variant
t = sk[sk.dq == 0].assign(rank=sk[sk.dq == 0].groupby('dr').M.rank(ascending=False, method='first'))
R['skeleton_rank'] = t.groupby('rank').agg(n=('has', 'size'), has=('has', 'sum')).reset_index().values.tolist()
t = sk.groupby(['dq', 'kind']).agg(n=('has', 'size'), has=('has', 'sum')).reset_index(); R['skeleton_by_kind'] = t.values.tolist()
# cells (M, extra) among both-live
t = df[df.both].groupby(['dq', 'M', 'ex']).agg(n=('ok', 'size'), w=('ok', 'sum'), drs=('dr', lambda v: v[df.loc[v.index, 'ok']].nunique())).reset_index()
R['cells_M_ex'] = t.values.tolist()
# routes to 2qt
Rt = V.groupby(['dr', 'side', 'pre2']).agg(e2=('e2', 'first'), p2=('pn2', 'first'), dq=('dq', 'first'), M=('M', 'max'), live=('both', 'sum'), rlive=('rlive', 'sum'), has=('ok', 'any')).reset_index()
t = Rt.groupby(['dq', 'e2']).agg(n=('has', 'size'), anylive=('rlive', lambda v: (v > 0).sum()), has=('has', 'sum'), drs=('dr', lambda v: v[Rt.loc[v.index, 'has']].nunique())).reset_index()
R['routes_by_e2'] = t.values.tolist()
r2 = Rt[(Rt.e2 <= 1) & (Rt.dq == 0)]
t = r2.groupby('p2').agg(n=('has', 'size'), has=('has', 'sum'), drs=('dr', lambda v: v[r2.loc[v.index, 'has']].nunique())).reset_index()
R['routes_by_p2'] = t.values.tolist()
R['routes_auc_p2'] = auc('p2', r2.rename(columns={'has': 'ok'}))
# DR-level abandon signals
d['lmin'] = d[['lminN', 'lminI']].min(axis=1)
R['by_lmin'] = d.groupby('lmin').solv.agg(['size', 'sum']).reset_index().values.tolist()
R['by_subset'] = d.groupby('subset').solv.agg(['size', 'sum']).reset_index().values.tolist()
ab = {}
for name, mask in {'all': cl, 'min': cl & (df.dq == 0)}.items():
    for a in [0, 1, 2, 9]:
        for k in range(0, 8):
            s = df[mask & (df.e2 <= a) & (df.ex <= k)]
            nlive = s[s.rlive].groupby('dr').size().reindex(d.index).fillna(0)
            nboth = s[s.both].groupby('dr').size().reindex(d.index).fillna(0)
            found = d.index.isin(s[s.ok].dr)
            ab[f'{name}|{a}|{k}'] = dict(
                no_rule_live=[int((nlive == 0).sum()), int(((nlive == 0) & d.solv).sum())],
                no_both_live=[int((nboth == 0).sum()), int(((nboth == 0) & d.solv).sum())],
                nothing_found=[int((~found).sum()), int((~found & d.solv).sum())],
                looks_solv=float(nlive[d.solv].mean()), looks_unsolv=float(nlive[~d.solv].mean()), fin_unsolv=float(nboth[~d.solv].mean()), fin_solv=float(nboth[d.solv].mean()))
R['abandon'] = ab
# policies
df['np0'] = -df.pn0; df['np2'] = -df.pn2; df['zero'] = 0
df['fl'] = np.maximum(df.lbr, df.len + df.pf)
Ks = (1, 2, 3, 5, 10, 20, 40, 80, 160)
pols = {
 'baseline, ties random': (allm, ['len']),
 'baseline, pairs at 2qt': (allm, ['len', 'np2']),
 'baseline, pairs at HTR': (allm, ['len', 'np0']),
 'corner bound, pairs at HTR': (df.clive, ['lbc', 'np0']),
 'pair floor only, by moves to HTR': (df.plive, ['len', 'np0']),
 'pair floor only, most pairs first': (df.plive, ['np0', 'len']),
 'intermediate rule only, by moves to HTR, pairs': (df.ilive, ['len', 'np0']),
 'rule only, by moves to HTR, ties random': (df.rlive, ['len']),
 'rule only, by moves to HTR, pairs': (df.rlive, ['len', 'np0']),
 'rule only, by rule bound, pairs': (df.rlive, ['lbr', 'np0']),
 'both floors, random': (df.both, ['zero']),
 'both floors, by moves to HTR, pairs': (df.both, ['len', 'np0']),
 'both floors, by extra moves, pairs': (df.both, ['ex', 'np0']),
 'both floors, by rule bound, pairs': (df.both, ['lbr', 'np0']),
 'both floors, by larger floor, pairs': (df.both, ['fl', 'np0']),
 'both floors, most pairs first': (df.both, ['np0', 'len']),
 'table + pair floor, most pairs first': (df.tlive & df.plive, ['np0', 'len']),
 'both floors, min-qt skeletons, most pairs first': (df.both & (df.dq == 0), ['np0', 'len']),
 'both floors, normal side only, most pairs first': (df.both & (df.side == 0), ['np0', 'len']),
 'both floors, S+T <= 3, most pairs first': (df.both & (df.ex <= 3), ['np0', 'len']),
 'both floors, e2 <= 1, most pairs first': (df.both & (df.e2 <= 1), ['np0', 'len']),
 'both floors, level by level, pairs': (df.both, ['ex', 'np0']),
}
P = {}
for name, (mask, keys) in pols.items():
    p = policy(df, d, mask, keys, Ks=Ks)
    P[name] = dict(reachable=float(p['found']), median=float(p['median']), mean=float(p['mean_found']), recall={str(k): float(v) for k, v in p['recall'].items()},
                   per_dr=float(p['size_all']), per_unsolv=float(p['size_unsolv']))
R['policies'] = P
json.dump(R, open(f'../out/meta/res{m}.json', 'w'), indent=1, default=lambda o: int(o) if isinstance(o, (np.integer,)) else float(o))
print('done', m)
