"""Pairs before HTR, for one quarter-turn count -> ../out/meta/pairs{m}.json

1. True pairs at 2qt once the rule bound is passed: as a read on one HTR, as an order of finishing, and on the
   routes to 2qt.
2. HTR-equivalent pairs (true pairs and pseudo-pairs) with 2 and 3 quarter turns left, on the state and on its
   inverse: against the moves to HTR from there, against the goal, and against S+T.
The fixed reach is the one of orders.py: S+T <= 3, at most 1 extra move before 2qt, both sides, all skeletons."""
import sys, json
from common import *
PF = {0: 4, 2: 5, 4: 3, 6: 3, 8: 2, 10: 3, 12: 1, 16: 0}
m = int(sys.argv[1])
df, d, q, mm, g = frame(m, ext=True)
nd = len(d); ns = int(d.solv.sum())
df['A'] = g - df.len
df['plive'] = df.pn0.map(PF) <= df.A; df['rlive'] = df.rs >= 0; df['both'] = df.plive & df.rlive
df['post'] = df.ex - df.e2                 # S+T after 2qt
df['rem2'] = df.len - df.a2                # moves from the state with 2 quarter turns left to HTR
df['fl2'] = 2 + (16 - df.hn2 + 3) // 4     # the floor on those moves
assert (df.rem2 >= df.fl2).all(), 'the HTR-equivalent pair floor fails on a record'
assert (df.rem2 >= df.d2n).all() and (df.d2n >= df.fl2).all()
assert (df.hn1 >= 16 - 4 * (df.len - df.a1 - 1)).all()
has3 = df.q >= 3
assert (df[has3].len - df[has3].a3 >= 3 + (16 - df[has3].hn3 + 3) // 4).all()
reach = (df.cs >= 0) & (df.e2 <= 1) & (df.ex <= 3)
df['p2hi'] = 4 * df.pn2 + df.hi2          # true pairs at 2qt, ties broken by the inverse count
df['hi2p'] = 16 * df.hi2 + df.pn2
# the columns no table below uses go, and the per-HTR reads get a narrow copy: the 4qt frame is 30 million rows
df.drop(columns=['pre1', 'pre2', 'lsk', 'e1', 'maxsec', 'lbc', 'lbr', 'lbt', 'bad', 'csfr', 'pi0', 'pn1', 'pi1', 'pi2', 'keep20', 'keep10', 'keptfin', 'sp0', 'm', 'goal',
                 'sn0', 'si0', 'S', 'T', 'ts', 'nr', 'M', 'kind', 'hn1', 'hi1', 'a1', 'a3', 'e3', 'd3n', 'd3i', 'ls2', 'fl2', 'A', 'total'], inplace=True)
dn = df[['dr', 'ok', 'pn2', 'pn0', 'hn2', 'hi2', 'post', 'rem2', 'p2hi', 'hi2p', 'hn3', 'hi3', 'pn3']]
R = {'m': m, 'goal': g, 'drs': nd, 'solvable': ns, 'records': int(len(df)), 'reach_recall': df[reach & df.ok].dr.nunique() / ns}

def auc(col, s):
    a = s[s.ok][col].values; b = s[~s.ok][col].values
    if len(a) == 0 or len(b) == 0: return None
    r = pd.Series(np.concatenate([a, b])).rank().values
    return float((r[:len(a)].sum() - len(a) * (len(a) + 1) / 2) / (len(a) * len(b)))
def wauc(col, s):
    """The same inside one DR (which of its HTRs), averaged over the DRs that have both kinds."""
    out = []
    for _, gdr in s.groupby('dr'):
        if gdr.ok.any() and not gdr.ok.all():
            out.append(auc(col, gdr))
    return [float(np.mean(out)), len(out)] if out else [None, 0]
def bins(s, col, edges, labels):
    b = pd.cut(s[col], edges, labels=labels)
    t = s.groupby(b, observed=False).ok.agg(['size', 'sum'])
    return [[str(k), int(n), int(w)] for k, n, w in zip(t.index, t['size'], t['sum'])]
def vals(s, col):
    t = s.groupby(col).ok.agg(['size', 'sum'])
    return [[int(k), int(n), int(w)] for k, n, w in zip(t.index, t['size'], t['sum'])]
P2E, P2L = [-1, 1, 3, 5, 7, 16], ['0–1', '2–3', '4–5', '6–7', '8 or more']
sets = {'goal': df.cs >= 0, 'reach': reach, 'rule': df.rlive, 'rule_reach': reach & df.rlive, 'pair_reach': reach & df.plive, 'both_reach': reach & df.both}
R['sets'] = {k: dict(per_dr=float(v.sum() / nd), within=int((v & df.ok).sum()), precision=float(df.ok[v].mean())) for k, v in sets.items()}

# ---- 1. true pairs at 2qt, on one HTR
SUB = {k: dn[v] for k, v in sets.items()}
R['p2_bins'] = {k: bins(SUB[k], 'pn2', P2E, P2L) for k in sets}
R['auc'] = {k: {c: auc(c, SUB[k]) for c in ['pn2', 'pn0', 'hn2', 'hi2', 'post', 'rem2', 'p2hi', 'hi2p']} for k in sets}
# true pairs at 2qt with the inverse count held fixed, and the other way round (rule passed, in reach)
t = SUB['rule_reach']
R['pn2_fixed_hi2'] = [[int(k), int(len(v)), auc('pn2', v)] for k, v in t.groupby('hi2') if len(v) >= 500]
R['hi2_fixed_pn2'] = [[int(k), int(len(v)), auc('hi2', v)] for k, v in t.groupby('pn2') if len(v) >= 500]
R['wauc'] = {k: {c: wauc(c, SUB[k]) for c in ['pn2', 'pn0', 'hn2', 'hi2']} for k in sets if k != 'goal' and k != 'rule'}
# ... and with S+T after 2qt held fixed (rule passed, in reach)
s = SUB['rule_reach']
R['p2_by_post'] = [[int(k), bins(v, 'pn2', P2E, P2L), auc('pn2', v), auc('hn2', v), auc('hi2', v)] for k, v in s.groupby('post')]

# ---- 2. as an order of finishing, inside the fixed reach
df['np2'] = -df.pn2; df['np0'] = -df.pn0; df['nh2'] = -df.hn2; df['nhi2'] = -df.hi2; df['zero'] = 0
df['nhmax'] = -np.maximum(df.hn2, df.hi2)
Ks = (1, 2, 3, 5, 10, 20, 40)
pols = {}
for fn, fm in [('none', reach), ('pair', reach & df.plive), ('rule', reach & df.rlive), ('both', reach & df.both)]:
    pols[fn + '|random'] = (fm, ['zero'])
    pols[fn + '|pairs at 2qt'] = (fm, ['np2'])
    pols[fn + '|by moves, pairs at 2qt'] = (fm, ['len', 'np2'])
    pols[fn + '|by moves, pairs at HTR'] = (fm, ['len', 'np0'])
    pols[fn + '|pairs at HTR'] = (fm, ['np0', 'len'])
    pols[fn + '|htr pairs at 2qt'] = (fm, ['nh2'])
    pols[fn + '|htr pairs at 2qt, pairs at HTR'] = (fm, ['nh2', 'np0'])
    pols[fn + '|pairs at 2qt, pairs at HTR'] = (fm, ['np2', 'np0'])
O = {}
for name, (mask, keys) in pols.items():
    p = policy(df, d, mask, keys, Ks=Ks)
    O[name] = dict(recall=float(p['found']), mean=float(p['mean_found']), median=float(p['median']), R={str(k): float(v) for k, v in p['recall'].items()},
                   per_dr=float(p['size_all']), per_unsolv=float(p['size_unsolv']))
R['orders'] = O

# ---- 3. routes to 2qt in the fixed reach
V = df[reach]
Rt = V.groupby(['dr', 'side', 'key2']).agg(p2=('pn2', 'first'), h2=('hn2', 'first'), hi2=('hi2', 'first'), n=('ok', 'size'), nrule=('rlive', 'sum'), nboth=('both', 'sum'),
                                           has=('ok', 'any'), d2n=('d2n', 'first'), d2i=('d2i', 'first'), a2=('a2', 'first')).reset_index()
R['routes_per_dr'] = len(Rt) / nd
def route_rows(col, edges=None, labels=None):
    key = pd.cut(Rt[col], edges, labels=labels) if edges else Rt[col]
    out = []
    for k, t in Rt.groupby(key, observed=False):
        tr = t[t.nrule > 0]
        out.append([str(k), len(t) / nd, int(len(t)), int(t.has.sum()), int(len(tr)), int(tr.has.sum()), float(t.nrule.sum() / nd), float(t.nboth.sum() / nd)])
    return out
R['routes_by_p2'] = route_rows('p2', P2E, P2L)
R['routes_by_h2'] = route_rows('h2')
R['routes_by_hi2'] = route_rows('hi2')
R['routes_auc'] = {c: auc(c, Rt.rename(columns={'has': 'ok'})) for c in ['p2', 'h2', 'hi2']}
R['routes_auc_rule'] = {c: auc(c, Rt[Rt.nrule > 0].rename(columns={'has': 'ok'})) for c in ['p2', 'h2', 'hi2']}
def keep_rows(col, ths):
    out = []
    for th in ths:
        t = Rt[Rt[col] >= th]
        out.append([int(th), len(t) / nd, float(t.nrule.sum() / nd), float(t.nboth.sum() / nd), t[t.has].dr.nunique() / ns])
    return out
R['routes_keep_p2'] = keep_rows('p2', [0, 1, 2, 3, 4, 5, 6])
R['routes_keep_h2'] = keep_rows('h2', [0, 4, 6, 8, 10, 12, 16])

# ---- 4. HTR-equivalent pairs on one HTR's route
for c in ['hn2', 'hi2']:
    R[c + '_vals'] = {k: vals(SUB[k], c) for k in sets}
t = SUB['rule_reach']
R['h2_by_post'] = [[int(k), vals(v, 'hn2')] for k, v in t.groupby('post')]
R['rem2_by_h2'] = [[int(k)] + [int((v.rem2 == r).sum()) for r in range(2, 9)] + [int((v.rem2 >= 9).sum())] for k, v in SUB['goal'].groupby('hn2')]
T3 = {'goal': dn[has3 & sets['goal']], 'rule': dn[has3 & sets['goal'] & df.rlive], 'rule_reach': dn[has3 & sets['goal'] & df.rlive & reach]}
R['hn3_vals'] = {k: vals(v, 'hn3') for k, v in T3.items()}
R['hi3_vals'] = {k: vals(v, 'hi3') for k, v in T3.items()}
R['auc3'] = {k: {c: auc(c, v) for c in ['hn3', 'hi3', 'pn3']} for k, v in T3.items()}
del SUB, T3

# ---- 5. the states on the way (every state with 2 or 3 quarter turns left, at most 1 extra move so far)
S = load_states(m, d)
SUB = open(f'../out/meta/states{m}.bin.sub').read().split('\n')
S = S[S.e <= 1].copy()
S['sub'] = S.m.map(lambda i: SUB[i])
# cq = quarter turns the corners need, in the frame with the fewest: t for a true t-qt state, t - 2 when the route
# is at HTR corners (t = 2) or at 1qt corners (t = 3) and still has that many quarter turns to make
S['fl'] = S.cq + (16 - S.hn + 3) // 4; S['fli'] = S.cq + (16 - S.hi + 3) // 4
assert (S.dn >= S.fl).all(), 'the floor fails on a state'
assert S.cq.isin([0, 1, 2, 3]).all() and ((S.t - S.cq) % 2 == 0).all()
S['thru'] = (S.a + S.ls) <= g                       # a within-goal solution starts with this path
agg = V.groupby(['dr', 'side', 'key2']).agg(nreach=('ok', 'size'), nrule=('rlive', 'sum'), nboth=('both', 'sum'), has=('ok', 'any')).reset_index().rename(columns={'key2': 'key'})
V3 = V[V.q >= 3]
agg3 = V3.groupby(['dr', 'side', 'key3']).agg(nreach=('ok', 'size'), nrule=('rlive', 'sum'), nboth=('both', 'sum'), has=('ok', 'any')).reset_index().rename(columns={'key3': 'key'})
ST = {}
# 'all': routes with m or m + 2 quarter turns; 'min': the shortest skeletons only (m quarter turns)
for t, cq, ag, fam in [(2, 2, agg, 'all'), (2, 0, agg, 'all'), (3, 3, agg3, 'all'), (3, 1, agg3, 'all'), (2, 2, agg, 'min'), (3, 3, agg3, 'min')]:
    sall = S[(S.t == t) & ((S.q == m) | (fam == 'all'))].merge(ag, on=['dr', 'side', 'key'], how='left')
    for c in ['nreach', 'nrule', 'nboth']: sall[c] = sall[c].fillna(0).astype(int)
    sall['has'] = sall.has.fillna(False).astype(bool)
    if t == 2 and fam == 'all':
        assert sall.nreach.sum() == len(V), 'a reach HTR is not matched to a state'
    s = sall[sall.cq == cq]
    if len(s) == 0: continue
    o = {'per_dr': len(s) / nd, 'n': int(len(s)), 'differ': float((s.hn != s.hi).mean()), 'tight': float((s.dn == s.fl).mean()),
         'share_of_t': len(s) / len(sall), 'reach_htrs': float(s.nreach.sum() / nd), 'has': int(s.has.sum()),
         'by_sub': [[k, int(len(v)), float(v.dn.mean()), float(v.hn.mean())] + [int((v.hn == h).sum()) for h in (0, 4, 6, 8, 10, 12, 16)] for k, v in s.groupby('sub')]}
    def srows(col, dcol):
        out = []
        for k, v in s.groupby(col):
            out.append(dict(k=int(k), n=int(len(v)), per_dr=len(v) / nd, mean_d=float(v[dcol].mean()), min_d=int(v[dcol].min()),
                            hist=[int((v[dcol] == r).sum()) for r in range(max(cq, 2), max(cq, 2) + 6)] + [int((v[dcol] >= max(cq, 2) + 6).sum())],
                            thru=int(v.thru.sum()), any_reach=int((v.nreach > 0).sum()), any_rule=int((v.nrule > 0).sum()), has=int(v.has.sum()),
                            rule_per=float(v.nrule.mean()), both_per=float(v.nboth.mean())))
        return out
    o['by_hn'] = srows('hn', 'dn'); o['by_hi'] = srows('hi', 'di'); o['by_pn'] = srows('pn', 'dn')
    # how well each count ranks "HTR within t + 2 moves" and "a within-goal HTR in reach from here"
    def a2(col, target):
        return auc(col, s.assign(ok=target))
    short = s.dn <= cq + 2; shorti = s.di <= cq + 2
    o['auc_short'] = dict(hn=a2('hn', short), pn=a2('pn', short), hi_for_normal=a2('hi', short), hi=a2('hi', shorti), hn_for_inverse=a2('hn', shorti))
    o['short_share'] = [float(short.mean()), float(shorti.mean())]
    o['corr'] = dict(hn_dn=float(np.corrcoef(s.hn, s.dn)[0, 1]), hi_di=float(np.corrcoef(s.hi, s.di)[0, 1]), hi_dn=float(np.corrcoef(s.hi, s.dn)[0, 1]),
                     pn_dn=float(np.corrcoef(s.pn, s.dn)[0, 1]), hn_hi=float(np.corrcoef(s.hn, s.hi)[0, 1]))
    o['auc_has'] = dict(hn=a2('hn', s.has), hi=a2('hi', s.has), pn=a2('pn', s.has), dn=a2('dn', s.has))
    o['auc_thru'] = dict(hn=a2('hn', s.thru), hi=a2('hi', s.thru), pn=a2('pn', s.thru), dn=a2('dn', s.thru))
    # with the moves to HTR held fixed: does the count still say something about the goal?
    o['has_by_dn_hn'] = [[int(dn), int(k), int(len(v)), int(v.has.sum()), int(v.thru.sum())] for (dn, k), v in s.groupby(['dn', 'hn'])]
    o['auc_has_fixed_dn'] = [[int(dn), int(len(v)), a2_ if (a2_ := auc('hn', v.assign(ok=v.has))) is not None else None, auc('pn', v.assign(ok=v.has))] for dn, v in s.groupby('dn')]
    # which side has the shorter HTR, against which side has more HTR-equivalent pairs
    sg = np.sign(s.hn - s.hi); dg = np.sign(s.di - s.dn)          # > 0: more on normal; > 0: normal is shorter
    o['sides'] = [[int(a), int(b), int(((sg == a) & (dg == b)).sum())] for a in (-1, 0, 1) for b in (-1, 0, 1)]
    o['sides_by_gap'] = [[int(gap), int(len(v)), int((v.dn < v.di).sum()), int((v.dn == v.di).sum()), int((v.dn > v.di).sum()), float((v.di - v.dn).mean())]
                         for gap, v in s.assign(gap=s.hn - s.hi).groupby('gap')]
    # skipping the states with few HTR-equivalent pairs
    keep = []
    for th in [0, 4, 6, 8, 10, 12, 16]:
        v = s[s.hn >= th]
        keep.append([th, len(v) / nd, float(v.nreach.sum() / nd), float(v.nrule.sum() / nd), float(v.nboth.sum() / nd), v[v.has].dr.nunique() / ns, int(v.has.sum())])
    o['keep_hn'] = keep
    keep = []
    for th in [0, 4, 6, 8, 10, 12, 16]:
        v = s[np.maximum(s.hn, s.hi) >= th]
        keep.append([th, len(v) / nd, float(v.nreach.sum() / nd), float(v.nrule.sum() / nd), float(v.nboth.sum() / nd), v[v.has].dr.nunique() / ns, int(v.has.sum())])
    o['keep_hmax'] = keep
    ST[f'{t}|{cq}' + ('|min' if fam == 'min' else '')] = o
R['states'] = ST

# ---- 6. the DR itself: which side to start on
x = S[(S.a == 0) & (S.side == 0)].drop_duplicates('dr').set_index('dr')
ok = df[df.ok & reach]
bn = ok[ok.side == 0].groupby('dr').ex.min().reindex(d.index); bi = ok[ok.side == 1].groupby('dr').ex.min().reindex(d.index)
x = x.join(pd.DataFrame({'bn': bn, 'bi': bi}))
x['gap'] = x.hn - x.hi
rows = []
for gap, v in x.groupby('gap'):
    sol = v[v.bn.notna() | v.bi.notna()]
    fn = sol.bn.fillna(99); fi = sol.bi.fillna(99)
    rows.append([int(gap), int(len(v)), int((v.dn < v.di).sum()), int((v.dn == v.di).sum()), int((v.dn > v.di).sum()), int(len(sol)), int((fn < fi).sum()), int((fn == fi).sum()), int((fn > fi).sum())])
R['dr_sides'] = rows
R['dr_differ'] = float((x.hn != x.hi).mean())
json.dump(R, open(f'../out/meta/pairs{m}.json', 'w'), indent=1, default=lambda o: int(o) if isinstance(o, (np.integer,)) else float(o))
print('done', m, 'records', len(df), 'states', len(S))
