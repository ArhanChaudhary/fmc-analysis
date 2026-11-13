"""All statistics of the report.  usage: venv/bin/python src/analysis.py  (from /data/scramble-difficulty)
Reads out/feat_*.tsv and out/tgt_*.tsv; writes out/analysis.txt (every table) and out/results.json."""
import json, sys, os, csv, math
import numpy as np
from collections import defaultdict
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.ensemble import HistGradientBoostingRegressor, HistGradientBoostingClassifier
from sklearn.tree import DecisionTreeRegressor, export_text
from sklearn.metrics import roc_auc_score

os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
OUT = open('out/analysis.txt', 'w')
RES = {}
def P(*a):
    s = ' '.join(str(x) for x in a); print(s); OUT.write(s + '\n'); OUT.flush()

AX = ['UD', 'FB', 'RL']
RNG = np.random.default_rng(20261113)
B = 400  # bootstrap resamples

def read(path):
    with open(path) as f:
        return list(csv.DictReader(f, delimiter='\t'))

# ------------------------------------------------------------------ load
dates = {}
for i, l in enumerate(open('big/real_unique.tsv')):
    if i == 0: continue
    r = l.rstrip('\n').split('\t'); dates[f'r{i - 1}'] = r[2]
POPS = []
for tag, ff, tt, ta in (('uni', 'out/feat_uni.tsv', 'out/tgt_uni.tsv', 'out/tgt_uni_axis.tsv'),
                        ('real', 'out/feat_real.tsv', 'out/tgt_real.tsv', 'out/tgt_real_axis.tsv'),
                        ('gen', 'out/feat_gen.tsv', 'out/tgt_gen.tsv', 'out/tgt_gen_axis.tsv')):
    if not (os.path.exists(ff) and os.path.exists(tt)): P('missing', tag); continue
    POPS.append((tag, ff, tt, ta))

TKEYS = ['n8', 'n9', 'n10', 'n11', 'best', 'n_near', 'good19', 'good20', 'good21', 'good22', 'gsub10', 'bestdr']
def empty_t(): return {'n8': 0, 'n9': 0, 'n10': 0, 'n11': 0, 'best': 27, 'n_near': 0, 'good19': 0, 'good20': 0, 'good21': 0, 'good22': 0, 'gsub10': 0, 'bestdr': 12}

rows = []          # per scramble dicts
axrows = []        # per scramble x axis
for tag, ff, tt, ta in POPS:
    T = {r['id']: r for r in read(tt)}
    F2 = {r['id']: r for r in read(ff.replace('feat_', 'feat2_'))}
    TA = {(r['id'], r['axis']): r for r in read(ta)}
    for r in read(ff):
        k = r['id']
        F = {}
        for x, v in list(r.items()) + [(a, b) for a, b in F2[r['id']].items() if a != 'id']:
            if x == 'id': continue
            try: F[x] = float(v)
            except ValueError: F[x] = v
        t = T.get(k)
        tg = {x: float(t[x]) for x in TKEYS} if t else {x: float(v) for x, v in empty_t().items()}
        if tg['best'] == 99: tg['best'] = 27
        pop = tag
        if tag == 'real': pop = 'real_old' if dates[k] < '2020-08' else 'real_new'
        rows.append({'id': k, 'pop': pop, 'F': F, 'T': tg})
        for a in AX:
            t = TA.get((k, a))
            tg = {x: float(t[x]) for x in TKEYS} if t else {x: float(v) for x, v in empty_t().items()}
            if tg['best'] == 99: tg['best'] = 27
            if tg['bestdr'] == 99: tg['bestdr'] = 12
            axrows.append({'id': k, 'pop': pop, 'axis': a, 'F': rows[-1]['F'], 'T': tg})
P('scrambles per population:', {p: sum(1 for r in rows if r['pop'] == p) for p in ('uni', 'real_old', 'real_new', 'gen')})

# ------------------------------------------------------------------ derived scramble-level features
def derive(F, tnoodle):
    D = {}
    be = sorted(F[f'be_{e}'] for e in AX); mc = sorted(F[f'mc_{a}'] for a in AX)
    D['be_min'], D['be_mid'], D['be_max'] = be; D['be_sum'] = sum(be)
    D['mc_min'], D['mc_mid'], D['mc_max'] = mc; D['mc_sum'] = sum(mc)
    sl = sorted(F[f'slin_{a}'] for a in AX); D['slin_max'] = sl[-1]; D['slin_sum'] = sum(sl)
    D['lucky'] = float(all(F[f'be_{e}'] not in (6, 10, 12) for e in AX))
    D['ce_min'] = min(F[f'mc_{a}'] + min(F[f'be_{e}'] for e in AX if e != a) for a in AX)
    eo = [min(F[f'eo_opt_{e}_N'], F[f'eo_opt_{e}_I']) for e in AX]
    D['eo_best'] = min(eo); D['eo_sum'] = sum(eo); D['eo_best_N'] = min(F[f'eo_opt_{e}_N'] for e in AX)
    D['eo_n_axes_le4'] = sum(1 for x in eo if x <= 4)
    D['n_eo4'] = sum(F[f'n_eo4_{e}_{s}'] for e in AX for s in 'NI')
    D['n_eo5'] = sum(F[f'n_eo5_{e}_{s}'] for e in AX for s in 'NI')
    D['n_eo4_N'] = sum(F[f'n_eo4_{e}_N'] for e in AX)
    D['n_eo4_maxaxis'] = max(F[f'n_eo4_{e}_N'] + F[f'n_eo4_{e}_I'] for e in AX)
    D['n_eo4_minaxis'] = min(F[f'n_eo4_{e}_N'] + F[f'n_eo4_{e}_I'] for e in AX)
    pe = [(e, a, s) for e in AX for a in AX if a != e for s in 'NI']
    D['post_c_min'] = min(F[f'post_eo_c_{e}_{a}_{s}'] for e, a, s in pe)
    D['post_ce_min'] = min(F[f'post_eo_ce_{e}_{a}_{s}'] for e, a, s in pe)
    D['post_lc_min'] = min(F[f'post_eo_lc_{e}_{a}_{s}'] for e, a, s in pe)
    D['post_neasy'] = sum(F[f'post_eo_neasy_{e}_{a}_{s}'] for e, a, s in pe)
    D['post_neasy_max'] = max(sum(F[f'post_eo_neasy_{e}_{a}_{s}'] for e in AX if e != a for s in 'NI') for a in AX)
    D['be1_min'] = min(F[f'be_1mv_{e}_{s}'] for e in AX for s in 'NI')
    D['mc1_min'] = min(F[f'mc_1mv_{a}_{s}'] for a in AX for s in 'NI')
    assert F['pairs_N'] == F['pairs_I']   # a corner-edge pair of the scramble is a pair of its inverse too
    D['pairs'] = F['pairs_N']
    D['solved'] = F['solved_c'] + F['solved_e']
    D['tetrad_split_min'] = min(F[f'tetrad_split_{a}_{s}'] for a in AX for s in 'NI')
    D['cface_arm_min'] = min(F[f'cface_{a}_{t}_{s}'] for a in AX for t in AX if t != a for s in 'NI')
    D['cw_ccw_imbal'] = min(abs(F[f'cw_{a}_N'] - F[f'ccw_{a}_N']) for a in AX)
    D['be_in_own_slice_min'] = min(F[f'be_in_slice_{e}_{a}_{s}'] for e in AX for a in AX for s in 'NI')
    D['cparity'] = F['cparity']
    D['ar_c'] = F['ar_c']; D['ar_e'] = F['ar_e']; D['ar_sum'] = F['ar_c'] + F['ar_e']
    D['eb3'] = F['eb3']; D['cb3'] = F['cb3']; D['eb1'] = F['eb1']
    if tnoodle:
        for x in ('t_len', 't_dr', 't_short', 't_long', 't_p1_end'): D[x] = F[x]
        D['t_run'] = F['t_len'] - F['t_dr']
        D['t_qt'] = sum(F[f't_qt_{a}'] for a in AX)
    return D

GROUPS = {
    'EO+CO counts (baseline)': ['be_min', 'be_mid', 'be_max', 'mc_min', 'mc_mid', 'mc_max'],
    'slice edges placed': ['slin_max', 'slin_sum'],
    'EO-search: optimal EO length': ['eo_best', 'eo_sum', 'eo_best_N', 'eo_n_axes_le4'],
    'EO-search: number of short EOs': ['n_eo4', 'n_eo5', 'n_eo4_N', 'n_eo4_maxaxis', 'n_eo4_minaxis'],
    'EO-search: DR case after the EOs': ['post_c_min', 'post_ce_min', 'post_lc_min', 'post_neasy', 'post_neasy_max'],
    'one-move lookahead': ['be1_min', 'mc1_min'],
    'pairs and solved pieces': ['pairs', 'solved'],
    'corner geometry (tetrads, ARM corners, twist)': ['tetrad_split_min', 'cface_arm_min', 'cw_ccw_imbal', 'ce_min'],
    'misc (lucky EO, slice bad edges, parity)': ['lucky', 'be_in_own_slice_min', 'cparity'],
    'axial reduction, multi-axis badness': ['ar_c', 'ar_e', 'ar_sum', 'eb3', 'cb3', 'eb1'],
}
TEXTG = ['t_len', 't_dr', 't_short', 't_long', 't_p1_end', 't_run', 't_qt']
for r in rows:
    r['D'] = derive(r['F'], r['pop'] != 'uni')

def tvec(rs):
    return {
        'n10 (log2 1+n)': np.array([math.log2(1 + r['T']['n10']) for r in rs]),
        'best DR+finish': np.array([r['T']['best'] for r in rs]),
        'good22 (log2 1+n)': np.array([math.log2(1 + r['T']['good22']) for r in rs]),
        'gsub10 (log2 1+n)': np.array([math.log2(1 + r['T']['gsub10']) for r in rs]),
        'n9 (log2 1+n)': np.array([math.log2(1 + r['T']['n9']) for r in rs]),
        'n_near (log2)': np.array([math.log2(r['T']['n_near']) if r['T']['n_near'] > 0 else 0 for r in rs]),
    }
MAIN = ['n10 (log2 1+n)', 'best DR+finish', 'good22 (log2 1+n)', 'gsub10 (log2 1+n)']

def rank(x):
    o = np.argsort(x, kind='mergesort'); r = np.empty(len(x)); r[o] = np.arange(len(x))
    # average ties
    xs = x[o]; i = 0
    while i < len(x):
        j = i
        while j + 1 < len(x) and xs[j + 1] == xs[i]: j += 1
        if j > i: r[o[i:j + 1]] = (i + j) / 2
        i = j + 1
    return r
def spear(a, b):
    ra, rb = rank(a), rank(b)
    return float(np.corrcoef(ra, rb)[0, 1])
def spear_ci(a, b):
    ra, rb = rank(a), rank(b); n = len(a)
    est = float(np.corrcoef(ra, rb)[0, 1])
    bs = []
    for _ in range(B):
        i = RNG.integers(0, n, n); bs.append(np.corrcoef(ra[i], rb[i])[0, 1])
    lo, hi = np.nanpercentile(bs, [2.5, 97.5])
    return est, float(lo), float(hi)
def auc(score, lab):
    if lab.min() == lab.max(): return float('nan')
    return float(roc_auc_score(lab, score))
def auc_ci(score, lab):
    n = len(lab); est = auc(score, lab); bs = []
    for _ in range(B // 2):
        i = RNG.integers(0, n, n)
        if lab[i].min() != lab[i].max(): bs.append(roc_auc_score(lab[i], score[i]))
    lo, hi = np.percentile(bs, [2.5, 97.5]); return est, float(lo), float(hi)
def r2(y, p): return float(1 - np.sum((y - p) ** 2) / np.sum((y - y.mean()) ** 2))
def r2_ci(y, p):
    n = len(y); est = r2(y, p); bs = []
    for _ in range(B):
        i = RNG.integers(0, n, n); bs.append(r2(y[i], p[i]))
    lo, hi = np.percentile(bs, [2.5, 97.5]); return est, float(lo), float(hi)
def fmt(e, lo, hi, d=3): return f'{e:.{d}f} [{lo:.{d}f}, {hi:.{d}f}]'

ALL = rows
TN = [r for r in rows if r['pop'] != 'uni']
TNNEW = [r for r in rows if r['pop'] in ('real_new', 'gen')]

# ------------------------------------------------------------------ 0. target distributions and agreement
P('\n## 0. Targets')
Y = tvec(ALL)
for k in MAIN:
    v = Y[k]; P(f'{k}: mean {v.mean():.3f}, quartiles {np.percentile(v, [25, 50, 75]).tolist()}')
for p in ('uni', 'real_old', 'real_new', 'gen'):
    rs = [r for r in rows if r['pop'] == p]
    if not rs: continue
    yy = tvec(rs)
    P(f'pop {p} n={len(rs)}: mean n10 {np.mean([r["T"]["n10"] for r in rs]):.1f}, median n10 {np.median([r["T"]["n10"] for r in rs]):.0f}, '
      f'mean best {yy["best DR+finish"].mean():.3f}, share best<=19 {np.mean(yy["best DR+finish"] <= 19):.3f}, share no DR<=10 {np.mean([r["T"]["n10"] == 0 for r in rs]):.4f}')
best = Y['best DR+finish']
P('best DR+finish histogram:', {int(k): int(v) for k, v in zip(*np.unique(best, return_counts=True))})
P('target agreement (Spearman, all scrambles):')
tk = list(Y)
for a in tk:
    P('  ' + a.ljust(20) + ' '.join(f'{spear(Y[a], Y[b]):+.3f}' for b in tk))
RES['agreement'] = {a: {b: spear(Y[a], Y[b]) for b in tk} for a in tk}
EASY = best <= 19
HARD = best >= 23
P(f'easy (best <= 19): {EASY.mean():.3f}; hard (best >= 22): {HARD.mean():.3f}')

# ------------------------------------------------------------------ 1. single features
def single_table(rs, feats, label):
    if not rs: return {}
    Yl = tvec(rs); bl = Yl['best DR+finish']; easy = (bl <= 19).astype(int)
    P(f'\n## 1. Single features ({label}, n={len(rs)}): Spearman rho [95% bootstrap CI] with each target; AUC for easy (best<=19), oriented')
    out = {}
    for f in feats:
        x = np.array([r['D'][f] for r in rs])
        if np.all(x == x[0]): continue
        cells = []
        res = {}
        for k in MAIN:
            e, lo, hi = spear_ci(x, Yl[k]); res[k] = (e, lo, hi); cells.append(fmt(e, lo, hi))
        sgn = 1 if spear(x, Yl['best DR+finish']) < 0 else -1
        a = auc_ci(sgn * x, easy); res['auc_easy'] = a
        P(f'  {f:22s} ' + ' | '.join(cells) + f' | AUC {fmt(*a)}')
        out[f] = res
    return out
featlist = [f for g in GROUPS.values() for f in g]
RES['single_all'] = single_table(ALL, featlist, 'all populations')
RES['single_text'] = single_table(TNNEW, TEXTG + ['be_min', 'mc_min', 'n_eo4', 'eo_best'], 'TNoodle 2020-08 to 2026 + generated')
old = [r for r in rows if r['pop'] == 'real_old']
if old: RES['single_text_old'] = single_table(old, TEXTG, 'real TNoodle 2016-2020')

# ------------------------------------------------------------------ 2. nested models (held out)
def split(rs, frac=0.67, seed=7):
    rng = np.random.default_rng(seed); idx = rng.permutation(len(rs)); n = int(frac * len(rs))
    return [rs[i] for i in idx[:n]], [rs[i] for i in idx[n:]]
def X_of(rs, feats): return np.array([[r['D'][f] for f in feats] for r in rs], dtype=float)
def raw_all(rs, text=False):
    keys = sorted(k for k in rs[0]['F'] if not isinstance(rs[0]['F'][k], str) and (text or not k.startswith('t_')))
    dk = sorted(k for k in rs[0]['D'] if text or not k.startswith('t_'))
    return np.array([[r['F'][k] for k in keys] + [r['D'][k] for k in dk] for r in rs], dtype=float), keys + dk

def nested(rs, label, text=False):
    if not rs: return {}
    tr, te = split(rs)
    Ytr, Yte = tvec(tr), tvec(te)
    P(f'\n## 2. Held-out models ({label}): train {len(tr)}, test {len(te)}. Test R^2 [95% bootstrap CI over test scrambles]')
    out = {}
    for k in MAIN:
        base = GROUPS['EO+CO counts (baseline)']
        m = LinearRegression().fit(X_of(tr, base), Ytr[k]); pb = m.predict(X_of(te, base))
        rb = r2_ci(Yte[k], pb)
        P(f' target {k}: baseline EO+CO linear R^2 {fmt(*rb)}')
        eo3 = ['be_min', 'be_mid', 'be_max']
        pe3 = LinearRegression().fit(X_of(tr, eo3), Ytr[k]).predict(X_of(te, eo3))
        P(f'   (bad edges only, no CO: R^2 {fmt(*r2_ci(Yte[k], pe3))}; CO adds {rb[0] - r2(Yte[k], pe3):+.4f})')
        out[k] = {'baseline': rb, 'add': {}}
        allf = list(base)
        groups = dict(GROUPS)
        if text: groups['scramble text'] = TEXTG
        for g, fs in groups.items():
            if g.startswith('EO+CO'): continue
            fs2 = base + fs
            m = LinearRegression().fit(X_of(tr, fs2), Ytr[k]); p = m.predict(X_of(te, fs2))
            e = r2(Yte[k], p)
            # bootstrap of the gain over baseline
            n = len(te); gains = []
            for _ in range(B):
                i = RNG.integers(0, n, n); gains.append(r2(Yte[k][i], p[i]) - r2(Yte[k][i], pb[i]))
            lo, hi = np.percentile(gains, [2.5, 97.5])
            P(f'   + {g:46s} R^2 {e:.3f}  gain {e - rb[0]:+.3f} [{lo:+.3f}, {hi:+.3f}]')
            out[k]['add'][g] = (e, e - rb[0], float(lo), float(hi))
            allf += [f for f in fs if f not in allf]
        m = LinearRegression().fit(X_of(tr, allf), Ytr[k]); pl = m.predict(X_of(te, allf))
        rl = r2_ci(Yte[k], pl); P(f'   all derived features, linear: R^2 {fmt(*rl)}')
        Xtr, names = raw_all(tr, text); Xte, _ = raw_all(te, text)
        g = HistGradientBoostingRegressor(max_iter=400, learning_rate=0.05, max_leaf_nodes=31, random_state=1).fit(Xtr, Ytr[k])
        pg = g.predict(Xte); rg = r2_ci(Yte[k], pg)
        P(f'   COMPUTER-ONLY gradient boosting on all {Xtr.shape[1]} raw+derived features: R^2 {fmt(*rg)}')
        out[k]['linear_all'] = rl; out[k]['gbm'] = rg
        if k == 'best DR+finish':
            easy_te = (Yte[k] <= 19).astype(int)
            P(f'   AUC easy: baseline {fmt(*auc_ci(-pb, easy_te))}; all linear {fmt(*auc_ci(-pl, easy_te))}; GBM {fmt(*auc_ci(-pg, easy_te))}')
            out[k]['auc'] = {'baseline': auc_ci(-pb, easy_te), 'linear_all': auc_ci(-pl, easy_te), 'gbm': auc_ci(-pg, easy_te)}
            # permutation importance of GBM (top 12)
            base_r = r2(Yte[k], pg); imp = []
            for j in range(Xte.shape[1]):
                Xp = Xte.copy(); Xp[:, j] = RNG.permutation(Xp[:, j]); imp.append((base_r - r2(Yte[k], g.predict(Xp)), names[j]))
            imp.sort(reverse=True)
            P('   GBM permutation importance (drop in test R^2), top 12: ' + ', '.join(f'{n} {v:.3f}' for v, n in imp[:12]))
            out[k]['gbm_importance'] = imp[:20]
    return out
RES['nested_all'] = nested(ALL, 'all populations, state features')
RES['nested_text'] = nested(TNNEW, 'TNoodle 2020-08 to 2026 + generated, state + text', text=True)

# ------------------------------------------------------------------ 3. human rules
P('\n## 3. Human-usable scores (fit on train, test numbers)')
tr, te = split(ALL); Ytr, Yte = tvec(tr), tvec(te)
CANDS = {
    'bad edges min+mid': ['be_min', 'be_mid'],
    'n_eo4': ['n_eo4'],
    'eo_best + n_eo4': ['eo_best', 'n_eo4'],
    'be_min + mc_min': ['be_min', 'mc_min'],
    'be_min + be_mid + mc_min': ['be_min', 'be_mid', 'mc_min'],
    'n_eo4 + post_c_min': ['n_eo4', 'post_c_min'],
    'n_eo4 + post_neasy': ['n_eo4', 'post_neasy'],
    'n_eo4 + eo_best + post_c_min': ['n_eo4', 'eo_best', 'post_c_min'],
    'n_eo5 + post_neasy': ['n_eo5', 'post_neasy'],
    'post_neasy': ['post_neasy'],
    'n_eo4_maxaxis + n_eo4': ['n_eo4_maxaxis', 'n_eo4'],
}
RES['human'] = {}
for name, fs in CANDS.items():
    line = f'  {name:32s}'
    RES['human'][name] = {}
    for k in MAIN:
        Xt = X_of(tr, fs); Xe = X_of(te, fs)
        # log-transform counts of EOs so a linear score is sensible
        Xt = np.where(np.char.startswith(np.array(fs), 'n_') | np.char.startswith(np.array(fs), 'post_neasy'), np.log2(1 + Xt), Xt)
        Xe = np.where(np.char.startswith(np.array(fs), 'n_') | np.char.startswith(np.array(fs), 'post_neasy'), np.log2(1 + Xe), Xe)
        m = LinearRegression().fit(Xt, Ytr[k]); p = m.predict(Xe)
        e = r2_ci(Yte[k], p); line += f' | {k.split()[0]} {e[0]:.3f}'
        RES['human'][name][k] = {'r2': e, 'coef': m.coef_.tolist(), 'icpt': float(m.intercept_)}
        if k == 'best DR+finish':
            a = auc_ci(-p, (Yte[k] <= 19).astype(int)); line += f' AUCeasy {a[0]:.3f}'
            RES['human'][name]['auc'] = a
    P(line)
# decision trees on cheap / EO-search features
for depth in (2, 3):
    for fs, lab in ((['be_min', 'be_mid', 'be_max', 'mc_min', 'mc_mid', 'mc_max', 'slin_max', 'lucky', 'pairs', 'solved'], 'cube-only counts'),
                    (['be_min', 'be_mid', 'mc_min', 'eo_best', 'n_eo4', 'n_eo5', 'post_c_min', 'post_neasy', 'post_neasy_max'], 'counts + EO search')):
        for k in ('best DR+finish', 'n10 (log2 1+n)'):
            t = DecisionTreeRegressor(max_depth=depth, min_samples_leaf=200, random_state=0).fit(X_of(tr, fs), Ytr[k])
            p = t.predict(X_of(te, fs)); e = r2_ci(Yte[k], p)
            P(f'  tree depth {depth} on {lab}, target {k}: test R^2 {fmt(*e)}')
            if depth == 2 or k == 'best DR+finish':
                P('    ' + export_text(t, feature_names=fs, decimals=1).replace('\n', '\n    '))
            RES.setdefault('trees', {})[f'{depth}|{lab}|{k}'] = e

# ------------------------------------------------------------------ 4. which axis
P('\n## 4. Which DR axis (per scramble, 3 axes)')
def axfeat(r, a):
    F = r['F']; es = [e for e in AX if e != a]; third = {e: [x for x in AX if x not in (a, e)][0] for e in es}
    D = {}
    D['mc'] = F[f'mc_{a}']; D['slin'] = F[f'slin_{a}']
    be = sorted(F[f'be_{e}'] for e in es); D['be_min2'], D['be_max2'] = be; D['be_sum2'] = sum(be)
    D['be_own'] = F[f'be_{a}']
    D['eo_min2'] = min(min(F[f'eo_opt_{e}_N'], F[f'eo_opt_{e}_I']) for e in es)
    D['eo_own'] = min(F[f'eo_opt_{a}_N'], F[f'eo_opt_{a}_I'])
    D['n_eo4_2'] = sum(F[f'n_eo4_{e}_{s}'] for e in es for s in 'NI')
    D['n_eo5_2'] = sum(F[f'n_eo5_{e}_{s}'] for e in es for s in 'NI')
    D['n_eo4_own'] = sum(F[f'n_eo4_{a}_{s}'] for s in 'NI')
    D['post_c'] = min(F[f'post_eo_c_{e}_{a}_{s}'] for e in es for s in 'NI')
    D['post_ce'] = min(F[f'post_eo_ce_{e}_{a}_{s}'] for e in es for s in 'NI')
    D['post_neasy'] = sum(F[f'post_eo_neasy_{e}_{a}_{s}'] for e in es for s in 'NI')
    D['arm_c'] = min(F[f'cface_{a}_{third[e]}_{s}'] for e in es for s in 'NI')
    D['tetrad'] = min(F[f'tetrad_split_{a}_{s}'] for s in 'NI')
    D['clayer'] = min(F[f'clayer_diff_{a}_{s}'] for s in 'NI')
    D['mc_1mv'] = min(F[f'mc_1mv_{a}_{s}'] for s in 'NI')
    D['be_in_slice'] = min(F[f'be_in_slice_{e}_{a}_{s}'] for e in es for s in 'NI')
    if 't_len' in F:
        D['t_run'] = F[f't_run_{a}']; D['t_is_axis'] = float(F['t_axis'] == a); D['t_qt'] = F[f't_qt_{a}']
    return D
for r in axrows: r['A'] = axfeat(r, r['axis'])
def by_scr(ar):
    g = defaultdict(list)
    for r in ar: g[r['id']].append(r)
    return [v for v in g.values() if len(v) == 3]
def topacc(groups, score_fn, tkey, higher_better):
    hit = 0; chance = 0; n = 0
    for g in groups:
        tv = np.array([x['T'][tkey] for x in g]); sv = np.array([score_fn(x) for x in g])
        bestv = tv.max() if higher_better else tv.min()
        winners = set(np.flatnonzero(tv == bestv))
        top = np.flatnonzero(sv == sv.max())
        hit += np.mean([1.0 if i in winners else 0.0 for i in top]); chance += len(winners) / 3; n += 1
    return hit / n, chance / n
def topacc_ci(groups, score_fn, tkey, hb):
    e, ch = topacc(groups, score_fn, tkey, hb)
    per = []
    for g in groups:
        tv = np.array([x['T'][tkey] for x in g]); sv = np.array([score_fn(x) for x in g])
        bestv = tv.max() if hb else tv.min(); winners = set(np.flatnonzero(tv == bestv)); top = np.flatnonzero(sv == sv.max())
        per.append(np.mean([1.0 if i in winners else 0.0 for i in top]))
    per = np.array(per); bs = [per[RNG.integers(0, len(per), len(per))].mean() for _ in range(B)]
    lo, hi = np.percentile(bs, [2.5, 97.5]); return e, float(lo), float(hi), ch
AXT = [('n10', True), ('bestdr', False), ('best', False)]
def axis_section(ar, label, text=False):
    G = by_scr(ar)
    if not G: return {}
    P(f'\n### axis question, {label}: {len(G)} scrambles. Top-1 accuracy of "the axis this feature favours" [95% CI] (chance = share of tied winners)')
    feats = list(G[0][0]['A'])
    out = {}
    for f in feats:
        # orientation: sign of within-scramble correlation with n10 on the pooled data
        x = np.array([r['A'][f] for g in G for r in g]); y = np.array([r['T']['n10'] for g in G for r in g])
        xm = x - np.repeat([np.mean([r['A'][f] for r in g]) for g in G], 3)
        ym = np.log2(1 + y); ym = ym - np.repeat([np.mean([math.log2(1 + r['T']['n10']) for r in g]) for g in G], 3)
        c = float(np.corrcoef(xm, ym)[0, 1]) if xm.std() > 0 else 0.0
        sgn = 1 if c >= 0 else -1
        cells = []
        for tkey, hb in AXT:
            e, lo, hi, ch = topacc_ci(G, lambda r: sgn * r['A'][f], tkey, hb); cells.append(f'{tkey}: {e:.3f} [{lo:.3f}, {hi:.3f}] (chance {ch:.3f})')
        P(f'  {f:12s} within-scramble r with log n10 {c:+.3f} | ' + ' | '.join(cells))
        out[f] = {'r': c, 'sign': sgn}
    # held-out linear model on within-scramble demeaned features
    ids = sorted({g[0]['id'] for g in G}); rng = np.random.default_rng(3); rng.shuffle(ids)
    trs = set(ids[:int(0.67 * len(ids))])
    Gtr = [g for g in G if g[0]['id'] in trs]; Gte = [g for g in G if g[0]['id'] not in trs]
    def mat(GG, fs):
        X = []; y = []
        for g in GG:
            m = np.array([[r['A'][f] for f in fs] for r in g], dtype=float); X.append(m - m.mean(0))
            t = np.array([math.log2(1 + r['T']['n10']) for r in g]); y.append(t - t.mean())
        return np.vstack(X), np.concatenate(y)
    for fs, lab in ((['mc', 'be_min2', 'be_sum2', 'slin'], 'cube counts'),
                    (['mc', 'be_min2', 'eo_min2', 'n_eo4_2', 'n_eo5_2', 'post_c', 'post_neasy'], 'counts + EO search'),
                    (feats, 'all per-axis features')):
        Xt, yt = mat(Gtr, fs); m = LinearRegression(fit_intercept=False).fit(Xt, yt)
        coef = dict(zip(fs, m.coef_))
        cells = []
        for tkey, hb in AXT:
            e, lo, hi, ch = topacc_ci(Gte, lambda r: sum(coef[f] * r['A'][f] for f in fs), tkey, hb); cells.append(f'{tkey}: {e:.3f} [{lo:.3f}, {hi:.3f}] (chance {ch:.3f})')
        P(f'  held-out linear ({lab}; {len(Gte)} test scrambles): ' + ' | '.join(cells))
        P('    coefficients: ' + ', '.join(f'{f} {c:+.3f}' for f, c in coef.items()))
        out[f'model {lab}'] = {'coef': coef}
    # computer-only GBM per axis row
    fs = feats
    Xt = np.array([[r['A'][f] for f in fs] for g in Gtr for r in g]); yt = np.array([math.log2(1 + r['T']['n10']) for g in Gtr for r in g])
    gb = HistGradientBoostingRegressor(max_iter=300, learning_rate=0.05, random_state=1).fit(Xt, yt)
    pred = {}
    Xe = np.array([[r['A'][f] for f in fs] for g in Gte for r in g]); pe = gb.predict(Xe)
    for (g, r), p in zip([(g, r) for g in Gte for r in g], pe): pred[(r['id'], r['axis'])] = p
    cells = []
    for tkey, hb in AXT:
        e, lo, hi, ch = topacc_ci(Gte, lambda r: pred[(r['id'], r['axis'])], tkey, hb); cells.append(f'{tkey}: {e:.3f} [{lo:.3f}, {hi:.3f}]')
    P(f'  COMPUTER-ONLY GBM on all per-axis features: ' + ' | '.join(cells))
    return out
RES['axis_all'] = axis_section([r for r in axrows], 'all populations')
RES['axis_text'] = axis_section([r for r in axrows if r['pop'] in ('real_new', 'gen')], 'TNoodle 2020-08 to 2026 + generated (with text)', text=True)
oldax = [r for r in axrows if r['pop'] == 'real_old']
if oldax: RES['axis_text_old'] = axis_section(oldax, 'real TNoodle 2016-2020 (with text)', text=True)

# ------------------------------------------------------------------ 5. the scramble's own DR axis
P('\n## 5. The text DR axis')
for lab, pops in (('2020-08 to 2026 + generated', ('real_new', 'gen')), ('2016-2020', ('real_old',))):
    G = by_scr([r for r in axrows if r['pop'] in pops])
    if not G: continue
    n = len(G); hits = defaultdict(float); ch = defaultdict(float); mean_on = defaultdict(list); mean_off = defaultdict(list)
    for g in G:
        for tkey, hb in AXT:
            tv = np.array([x['T'][tkey] for x in g]); bv = tv.max() if hb else tv.min(); w = set(np.flatnonzero(tv == bv))
            i = [j for j, x in enumerate(g) if x['A']['t_is_axis'] == 1][0]
            hits[tkey] += (i in w); ch[tkey] += len(w) / 3
            mean_on[tkey].append(tv[i]); mean_off[tkey].extend(tv[j] for j in range(3) if j != i)
    dd = []
    for g in G:
        i = [j for j, x in enumerate(g) if x['A']['t_is_axis'] == 1][0]
        v = [math.log2(1 + x['T']['n10']) for x in g]; dd.append(v[i] - (sum(v) - v[i]) / 2)
    dd = np.array(dd); bs = [dd[RNG.integers(0, n, n)].mean() for _ in range(B)]
    P(f'  {lab}: log2(1+n10) on the text axis minus the mean of the other two: {dd.mean():+.3f} [{np.percentile(bs, 2.5):+.3f}, {np.percentile(bs, 97.5):+.3f}] (a factor {2 ** dd.mean():.3f} in 1+n10)')
    RES.setdefault('text_axis_diff', {})[lab] = (float(dd.mean()), float(np.percentile(bs, 2.5)), float(np.percentile(bs, 97.5)))
    for tkey, _ in AXT:
        per = None
        P(f'  {lab}: text axis is a best axis by {tkey}: {hits[tkey] / n:.3f} (chance {ch[tkey] / n:.3f}); mean {tkey} on text axis {np.mean(mean_on[tkey]):.3f} vs other axes {np.mean(mean_off[tkey]):.3f}  (n={n})')
    RES.setdefault('text_axis', {})[lab] = {k: (hits[k] / n, ch[k] / n, float(np.mean(mean_on[k])), float(np.mean(mean_off[k]))) for k, _ in AXT}


# ------------------------------------------------------------------ 7. lookup tables a solver can use
def cell_stats(rs):
    if not rs: return None
    b = np.array([r['T']['best'] for r in rs]); n10 = np.array([r['T']['n10'] for r in rs])
    return len(rs), float(np.mean(b <= 19)), float(np.median(n10)), float(np.mean(b)), float(np.mean(b >= 23))
def lookup(rs, rowf, rowlab, colf, collab, title):
    P(f'\n### {title} (n={len(rs)}): per cell n | share easy (best<=19) | median n10 | mean best | share hard (best>=23 or none)')
    rows_ = sorted({rowf(r) for r in rs}, key=lambda x: rowlab.index(x)); cols_ = sorted({colf(r) for r in rs}, key=lambda x: collab.index(x))
    out = {}
    for a in rows_:
        line = f'  {a:>10s}'
        for c in cols_:
            st = cell_stats([r for r in rs if rowf(r) == a and colf(r) == c])
            if st: line += f' || {c}: {st[0]} | {st[1]:.2f} | {st[2]:.0f} | {st[3]:.2f} | {st[4]:.2f}'; out[f'{a}|{c}'] = st
        P(line)
    return out
def eoclass(r):
    x = r['D']['eo_best']; return '<=2' if x <= 2 else ('3' if x == 3 else ('4' if x == 4 else '>=5'))
def n4class(r):
    x = r['D']['n_eo4']; return '0' if x == 0 else ('1-7' if x < 8 else ('8-19' if x < 20 else ('20-49' if x < 50 else '>=50')))
def triple(r):
    be = (r['D']['be_min'], r['D']['be_mid'], r['D']['be_max'])
    if be[0] <= 4 and be[1] <= 4: return 'two<=4'
    if be[0] <= 4: return 'one<=4'
    if be[2] <= 8: return 'none<=4,max<=8'
    return 'none<=4,max>=10'
P('\n## 7. Lookup tables (all populations)')
RES['lookup_eo'] = lookup(ALL, eoclass, ['<=2', '3', '4', '>=5'], n4class, ['0', '1-7', '8-19', '20-49', '>=50'],
                          'shortest EO (any axis, normal or inverse) x number of EOs of <= 4 moves (all axes, normal + inverse)')
RES['lookup_be'] = lookup(ALL, triple, ['two<=4', 'one<=4', 'none<=4,max<=8', 'none<=4,max>=10'], lambda r: 'all', ['all'], 'bad-edge triple class')
for cl in ['two<=4', 'one<=4', 'none<=4,max<=8', 'none<=4,max>=10']:
    P(f'  share of scrambles in {cl}: {np.mean([triple(r) == cl for r in ALL]):.3f}')

# ------------------------------------------------------------------ 8. claims from the server, tested
P('\n## 8. Claims tested (all populations)')
def contrast(name, pred):
    a = [r for r in ALL if pred(r)]; b = [r for r in ALL if not pred(r)]
    sa, sb = cell_stats(a), cell_stats(b)
    # bootstrap CI of the difference in share easy and in mean best
    ea = np.array([r['T']['best'] <= 19 for r in a], float); eb = np.array([r['T']['best'] <= 19 for r in b], float)
    ba = np.array([r['T']['best'] for r in a]); bb = np.array([r['T']['best'] for r in b])
    d1 = []; d2 = []
    for _ in range(B):
        i = RNG.integers(0, len(a), len(a)); j = RNG.integers(0, len(b), len(b))
        d1.append(ea[i].mean() - eb[j].mean()); d2.append(ba[i].mean() - bb[j].mean())
    P(f'  {name}: yes n={sa[0]} ({sa[0] / len(ALL):.3f}) easy {sa[1]:.3f} hard {sa[4]:.3f} median n10 {sa[2]:.0f} mean best {sa[3]:.2f} | no n={sb[0]} easy {sb[1]:.3f} hard {sb[4]:.3f} median n10 {sb[2]:.0f} mean best {sb[3]:.2f} | diff easy {np.mean(ea) - np.mean(eb):+.3f} [{np.percentile(d1, 2.5):+.3f}, {np.percentile(d1, 97.5):+.3f}], diff mean best {np.mean(ba) - np.mean(bb):+.2f} [{np.percentile(d2, 2.5):+.2f}, {np.percentile(d2, 97.5):+.2f}]')
    RES.setdefault('claims', {})[name] = (sa, sb)
contrast('fewer than 8 EOs of <= 4 moves (normal + inverse, all axes)', lambda r: r['D']['n_eo4'] < 8)
contrast('fewer than 8 EOs of <= 4 moves (normal only)', lambda r: r['D']['n_eo4_N'] < 8)
contrast('fewer than 30 EOs of exactly 5 moves (normal + inverse) and at most 2 of <= 4', lambda r: r['D']['n_eo5'] - r['D']['n_eo4'] < 30 and r['D']['n_eo4'] <= 2)
contrast('some axis has 2 or 4 bad edges', lambda r: r['D']['be_min'] in (2, 4))
contrast('lucky: no axis with 6, 10 or 12 bad edges', lambda r: r['D']['lucky'] == 1)
contrast('10/8/8 bad edges and no EO under 5 moves', lambda r: (r['D']['be_min'], r['D']['be_mid'], r['D']['be_max']) == (8, 8, 10) and r['D']['eo_best'] >= 5)
contrast('an EO of <= 2 moves', lambda r: r['D']['eo_best'] <= 2)
P(f"  share lucky: {np.mean([r['D']['lucky'] for r in ALL]):.4f}")

# ------------------------------------------------------------------ 6. optimal length (official scrambles, DougCube's sheet)
OPT = {r['id']: float(r['opt']) for r in read('out/opt_real.tsv')}
R6 = [r for r in rows if r['id'] in OPT]
if R6:
    P(f'\n## 6. Optimal solution length (official scrambles with DougCube sheet optimum, n={len(R6)})')
    o = np.array([OPT[r['id']] for r in R6]); Yo = tvec(R6)
    P('  optimal length histogram:', {int(k): int(v) for k, v in zip(*np.unique(o, return_counts=True))})
    for k in MAIN:
        P(f'  Spearman(optimal length, {k}) = {fmt(*spear_ci(o, Yo[k]))}')
    for f in ['n_eo5', 'n_eo4', 'eo_sum', 'be_min', 'mc_min', 'pairs', 'solved', 't_len', 't_dr']:
        x = np.array([r['D'][f] for r in R6]); P(f'  Spearman(optimal length, {f}) = {fmt(*spear_ci(o, x))}')
    RES['opt'] = True

json.dump(RES, open('out/results.json', 'w'), indent=1, default=lambda o: float(o) if isinstance(o, (np.floating,)) else str(o))
P('\ndone')
