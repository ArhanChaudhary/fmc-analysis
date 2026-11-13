"""Tests of what the server proposed or asked, beyond analysis.py.   usage: venv/bin/python src/claims_extra.py
A. corner QT of the scramble (Levi Gibson) against the corner cases of its DRs and the difficulty targets
B. per-axis features: Zagros' shared bad edges, Levi Gibson's seven counts, rodneykinney's DRM-style pairs
C. which EO axis the DRs come from (kalindumaxxer's recalled tip, JTuu's question)   [needs out/eoaxis_*.tsv]
D. details for the claims table: counting conventions, 10/8/8 with a short EO, short texts, how lopsided the axes are
out: out/claims_extra.txt"""
import csv, os, math, sys
import numpy as np
from collections import defaultdict, Counter
from sklearn.linear_model import LinearRegression
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
sys.path.insert(0, 'src')
O = open('out/claims_extra.txt', 'w')
def P(*a):
    s = ' '.join(str(x) for x in a); print(s); O.write(s + '\n'); O.flush()
AX = ['UD', 'FB', 'RL']
RNG = np.random.default_rng(20261113); B = 400
def read(p): return list(csv.DictReader(open(p), delimiter='\t'))
def rank(x):
    x = np.asarray(x, float); o = np.argsort(x, kind='mergesort'); r = np.empty(len(x)); r[o] = np.arange(len(x))
    xs = x[o]; i = 0
    while i < len(x):
        j = i
        while j + 1 < len(x) and xs[j + 1] == xs[i]: j += 1
        if j > i: r[o[i:j + 1]] = (i + j) / 2
        i = j + 1
    return r
def spear_ci(a, b):
    ra, rb = rank(a), rank(b); n = len(ra); est = float(np.corrcoef(ra, rb)[0, 1]); bs = []
    for _ in range(B):
        i = RNG.integers(0, n, n); bs.append(np.corrcoef(ra[i], rb[i])[0, 1])
    lo, hi = np.nanpercentile(bs, [2.5, 97.5]); return f'{est:+.3f} [{lo:+.3f}, {hi:+.3f}]'
def r2(y, p): return float(1 - np.sum((y - p) ** 2) / np.sum((y - y.mean()) ** 2))

dates = {}
for i, l in enumerate(open('big/real_unique.tsv')):
    if i: dates[f'r{i - 1}'] = l.rstrip('\n').split('\t')
ROWS = []
for tag in ('uni', 'real', 'gen'):
    T = {r['id']: r for r in read(f'out/tgt_{tag}.tsv')}
    TA = {(r['id'], r['axis']): r for r in read(f'out/tgt_{tag}_axis.tsv')}
    F2 = {r['id']: r for r in read(f'out/feat2_{tag}.tsv')}; F3 = {r['id']: r for r in read(f'out/feat3_{tag}.tsv')}
    Q = {r['id']: [int(r[f'h{k}']) for k in range(6)] for r in read(f'out/drqt_{tag}.tsv')}
    EA = {r['id']: r for r in read(f'out/eoaxis_{tag}.tsv')} if os.path.exists(f'out/eoaxis_{tag}.tsv') else {}
    for r in read(f'out/feat_{tag}.tsv'):
        k = r['id']; F = {}
        for src in (r, F2[k], F3[k]):
            for x, v in src.items():
                if x == 'id': continue
                try: F[x] = float(v)
                except ValueError: F[x] = v
        t = T.get(k)
        n10 = float(t['n10']) if t else 0.0; best = float(t['best']) if t else 27.0
        if best == 99: best = 27.0
        ta = {a: (float(TA[(k, a)]['n10']) if (k, a) in TA else 0.0) for a in AX}
        pop = tag if tag != 'real' else ('real_old' if dates[k][2] < '2020-08' else 'real_new')
        ROWS.append(dict(id=k, pop=pop, F=F, n10=n10, best=best, good22=float(t['good22']) if t else 0.0, gsub=float(t['gsub10']) if t else 0.0,
                         ta=ta, q=Q.get(k, [0] * 6), ea=EA.get(k)))
N = len(ROWS); P('scrambles', N)
for r in ROWS:
    F = r['F']
    r['be'] = sorted(F[f'be_{e}'] for e in AX)
    r['eo_best'] = min(F[f'eo_opt_{e}_{s}'] for e in AX for s in 'NI')
    r['n_eo4'] = sum(F[f'n_eo4_{e}_{s}'] for e in AX for s in 'NI'); r['n_eo5'] = sum(F[f'n_eo5_{e}_{s}'] for e in AX for s in 'NI')
    r['easy'] = r['best'] <= 19; r['hard'] = r['best'] >= 23
def stats(rs):
    return (len(rs), np.mean([r['easy'] for r in rs]), np.mean([r['hard'] for r in rs]), np.median([r['n10'] for r in rs]), np.mean([r['best'] for r in rs]))
def line(name, rs):
    s = stats(rs); P(f'  {name}: n={s[0]} ({100 * s[0] / N:.1f}% of scrambles), easy {100 * s[1]:.1f}%, hard {100 * s[2]:.1f}%, median DRs {s[3]:.0f}, mean best {s[4]:.2f}')

# ------------------------------------------------------------------ A. corner QT
P('\n## A. Corner QT of the scramble (same on the three axes and on the inverse: checked in features3.py selftest)')
for r in ROWS:
    F = r['F']; assert len({F[f'cqt_{a}_{s}'] for a in AX for s in 'NI'}) == 1
    r['cqt'] = F['cqt_UD_N']
P('  scramble corner QT histogram:', sorted(Counter(r['cqt'] for r in ROWS).items()), '(uniform: 96, 1152, 5856, 11328, 14208, 7680 of 40320)')
W = [r for r in ROWS if sum(r['q']) > 0]
dq = np.array([sum(k * h for k, h in enumerate(r['q'])) / sum(r['q']) for r in W])
lo2 = np.array([sum(r['q'][:3]) / sum(r['q']) for r in W])
gs = np.array([r['gsub'] / r['n10'] for r in W])
cq = np.array([r['cqt'] for r in W])
P(f'  scrambles with a DR of <= 10: {len(W)}')
P('  Spearman(scramble QT, mean corner QT of its DRs) =', spear_ci(cq, dq))
P('  Spearman(scramble QT, share of its DRs with QT <= 2) =', spear_ci(cq, lo2))
P('  Spearman(scramble QT, share of its DRs in a good subset) =', spear_ci(cq, gs))
allq = np.array([r['cqt'] for r in ROWS])
for nm, v in (('DRs of <= 10 (log)', [math.log2(1 + r['n10']) for r in ROWS]), ('best DR + finish', [r['best'] for r in ROWS]),
              ('good DRs (log)', [math.log2(1 + r['good22']) for r in ROWS]), ('DRs in a good subset (log)', [math.log2(1 + r['gsub']) for r in ROWS])):
    P(f'  Spearman(scramble QT, {nm}) =', spear_ci(allq, np.array(v)))
P('  by scramble QT: n | mean corner QT of DRs | share of DRs with QT <= 2 | share of DRs in a good subset | median DRs | mean best | easy % | hard %')
tot = np.zeros(6)
for q in range(6):
    rs = [r for r in ROWS if r['cqt'] == q]; ws = [r for r in rs if sum(r['q']) > 0]
    hs = np.sum([r['q'] for r in ws], axis=0) if ws else np.zeros(6)
    s = stats(rs)
    P(f'   QT {q}: {len(rs)} | {sum(k * h for k, h in enumerate(hs)) / max(1, hs.sum()):.2f} | {100 * hs[:3].sum() / max(1, hs.sum()):.1f}% | '
      f'{100 * sum(r["gsub"] for r in ws) / max(1, sum(r["n10"] for r in ws)):.1f}% | {s[3]:.0f} | {s[4]:.2f} | {100 * s[1]:.1f} | {100 * s[2]:.1f}')
    P(f'        DR corner-QT mix (pooled DRs), QT 0..5: ' + ' '.join(f'{100 * h / max(1, hs.sum()):.1f}%' for h in hs))
    tot += hs
P('   all DRs pooled, QT 0..5: ' + ' '.join(f'{100 * h / tot.sum():.1f}%' for h in tot))
# per-scramble version (each scramble once): mean share with QT<=2 by scramble QT, with bootstrap CI
for q in range(6):
    v = lo2[cq == q]
    if len(v) < 5: continue
    bs = [v[RNG.integers(0, len(v), len(v))].mean() for _ in range(B)]
    P(f'   QT {q}: per-scramble mean share of DRs with QT <= 2: {100 * v.mean():.1f}% [{100 * np.percentile(bs, 2.5):.1f}, {100 * np.percentile(bs, 97.5):.1f}] (n={len(v)})')
# held-out gain over the bad-edge baseline
idx = np.random.default_rng(7).permutation(N); ntr = int(0.67 * N); tr, te = idx[:ntr], idx[ntr:]
Xb = np.array([r['be'] for r in ROWS], float); Xq = np.column_stack([Xb, allq])
for nm, y in (('DRs of <= 10 (log)', np.array([math.log2(1 + r['n10']) for r in ROWS])), ('best DR + finish', np.array([r['best'] for r in ROWS])),
              ('DRs in a good subset (log)', np.array([math.log2(1 + r['gsub']) for r in ROWS])), ('good DRs (log)', np.array([math.log2(1 + r['good22']) for r in ROWS]))):
    pb = LinearRegression().fit(Xb[tr], y[tr]).predict(Xb[te]); pq = LinearRegression().fit(Xq[tr], y[tr]).predict(Xq[te])
    g = [];
    for _ in range(B):
        i = RNG.integers(0, len(te), len(te)); g.append(r2(y[te][i], pq[i]) - r2(y[te][i], pb[i]))
    P(f'  held-out R^2, {nm}: bad edges {r2(y[te], pb):.3f}, + corner QT {r2(y[te], pq):.3f}, gain {r2(y[te], pq) - r2(y[te], pb):+.4f} [{np.percentile(g, 2.5):+.4f}, {np.percentile(g, 97.5):+.4f}]')

# check of the QT table against the labels: 3,000 DRs of the official lists, state rebuilt from the moves
import cube, features3
def split_niss(moves):
    n, i, ins = [], [], False
    for t in moves.replace('(', ' ( ').replace(')', ' ) ').split():
        if t == '(': ins = True
        elif t == ')': ins = False
        else: (i if ins else n).append(t)
    return n, i
scr = {l.split('\t')[0]: l.rstrip('\n').split('\t')[1] for l in open('big/in_real.tsv')}
fl = open('big/real_label_10.tsv'); next(fl); ok = bad = 0; k = 0
for ln in open('big/real_raw_10.tsv'):
    if ln.startswith('#') or ln.startswith('scr\t'): continue
    lab = next(fl); k += 1
    if k % 190: continue
    r = ln.rstrip('\n').split('\t'); n, i = split_niss(r[5]); a = r[1].replace('/', '')
    st = cube.seq(cube.inv_moves(i) + cube.parse(scr[r[0]]) + n)
    assert cube.is_dr(st, a)
    if r[2] == 'I': st = cube.inv(st)
    q = features3.QT(a)[st[0]]
    if q == int(lab.split('\t')[0].split()[0][-1]): ok += 1
    else: bad += 1
P(f'  QT table against the corner case of the label on {ok + bad} DRs of the official lists: {ok} agree, {bad} differ')

# ------------------------------------------------------------------ B. per-axis features
P('\n## B. Per-axis features proposed on the server (all scrambles; hit rate = the favoured axis is among the axes with the most DRs of <= 10)')
def afeat(r, a):
    F = r['F']; es = [e for e in AX if e != a]
    D = dict(un=F[f'un_{a}'], ov=F[f'ov_{a}'], be_sum2=F[f'be_{es[0]}'] + F[f'be_{es[1]}'], be_min2=min(F[f'be_{es[0]}'], F[f'be_{es[1]}']),
             mc=F[f'mc_{a}'], drmp_N=F[f'drmp_{a}_N'], drmp_I=F[f'drmp_{a}_I'], drmp=F[f'drmp_{a}_N'] + F[f'drmp_{a}_I'], drmp_max=max(F[f'drmp_{a}_N'], F[f'drmp_{a}_I']),
             n_eo5_2=sum(F[f'n_eo5_{e}_{s}'] for e in es for s in 'NI'), eo_own=min(F[f'eo_opt_{a}_N'], F[f'eo_opt_{a}_I']))
    for t in ('L1', 'L2', 'Lb', 'S1', 'S2', 'Sb'): D['lg_' + t] = F[f'lg_{a}_{t}']
    # Levi Gibson's counts do not depend on the order of the two EO axes: use sums and the both-count
    D['lg_Lone'] = D['lg_L1'] + D['lg_L2']; D['lg_Sone'] = D['lg_S1'] + D['lg_S2']
    return D
G = [[(r, a, afeat(r, a)) for a in AX] for r in ROWS]
def hit(G_, score):
    per = []; ch = []
    for g in G_:
        tv = np.array([r['ta'][a] for r, a, D in g]); sv = np.array([score(D) for r, a, D in g])
        w = set(np.flatnonzero(tv == tv.max())); top = np.flatnonzero(sv == sv.max())
        per.append(np.mean([i in w for i in top])); ch.append(len(w) / 3)
    per = np.array(per); bs = [per[RNG.integers(0, len(per), len(per))].mean() for _ in range(B)]
    return f'{per.mean():.3f} [{np.percentile(bs, 2.5):.3f}, {np.percentile(bs, 97.5):.3f}] (chance {np.mean(ch):.3f})'
def within_r(f):
    x = np.array([[D[f] for r, a, D in g] for g in G], float); y = np.array([[math.log2(1 + r['ta'][a]) for r, a, D in g] for g in G])
    x = x - x.mean(1, keepdims=True); y = y - y.mean(1, keepdims=True)
    return float(np.corrcoef(x.ravel(), y.ravel())[0, 1])
for f, sgn, lab in (('be_sum2', -1, 'fewest bad edges on the two EO axes, summed'), ('un', -1, 'fewest edges bad on either EO axis (Zagros: sum minus shared)'),
                    ('ov', 1, 'most shared bad edges'), ('ov', -1, 'fewest shared bad edges'),
                    ('mc', -1, 'fewest misoriented corners'), ('drmp_N', 1, 'most DRM-style pairs, normal'), ('drmp', 1, 'most DRM-style pairs, normal + inverse'),
                    ('drmp_max', 1, 'most DRM-style pairs on the better side'), ('n_eo5_2', 1, 'most EOs of <= 5 on the two EO axes')):
    P(f'  {lab:62s} within r {within_r(f):+.3f} | hit rate {hit(G, lambda D: sgn * D[f])}')
ids = np.random.default_rng(3).permutation(N); trs = set(ids[:int(0.67 * N)].tolist())
Gtr = [g for i, g in enumerate(G) if i in trs]; Gte = [g for i, g in enumerate(G) if i not in trs]
def fit(fs):
    X = []; y = []
    for g in Gtr:
        m = np.array([[D[f] for f in fs] for r, a, D in g], float); X.append(m - m.mean(0))
        t = np.array([math.log2(1 + r['ta'][a]) for r, a, D in g]); y.append(t - t.mean())
    m = LinearRegression(fit_intercept=False).fit(np.vstack(X), np.concatenate(y)); return dict(zip(fs, m.coef_))
for fs, lab in ((['be_sum2'], 'bad edges of the two EO axes, summed'), (['be_sum2', 'ov'], '+ shared bad edges (Zagros)'),
                (['mc', 'lg_Lone', 'lg_Lb', 'lg_Sone', 'lg_Sb'], "Levi Gibson's counts (corners; layer and slice pieces bad on one / both EO axes)"),
                (['be_sum2', 'ov', 'mc', 'drmp'], '+ shared bad edges + corners + DRM-style pairs'),
                (['be_sum2', 'lg_Lb'], 'bad-edge sum + layer pieces bad on both'),
                (['lg_Lone', 'lg_Lb', 'lg_Sone', 'lg_Sb'], "Levi Gibson's six edge counts without the corners"),
                (['n_eo5_2', 'lg_Lb'], 'EOs of <= 5 on the two EO axes + layer pieces bad on both'),
                (['n_eo5_2'], 'EOs of <= 5 on the two EO axes'), (['n_eo5_2', 'eo_own', 'un', 'drmp'], 'EOs + own EO + union + pairs')):
    c = fit(fs)
    P(f'  held-out linear, {lab}: hit rate {hit(Gte, lambda D: sum(c[f] * D[f] for f in fs))} | coefficients ' + ', '.join(f'{f} {v:+.3f}' for f, v in c.items()))
# the overlap, bad-edge sums held fixed: mean log DRs by overlap within the most common (be1, be2) pair
cell = defaultdict(list)
for g in G:
    for r, a, D in g:
        es = [e for e in AX if e != a]; key = tuple(sorted((r['F'][f'be_{es[0]}'], r['F'][f'be_{es[1]}'])))
        cell[(key, D['ov'])].append(r['ta'][a])
for key in ((6.0, 6.0), (4.0, 6.0), (6.0, 8.0), (4.0, 4.0)):
    P(f'  two EO axes with {int(key[0])} and {int(key[1])} bad: shared -> axes, median DRs on the third axis, share with none: ' +
      '; '.join(f'{int(o)}: {len(v)}, {np.median(v):.0f}, {100 * np.mean(np.array(v) == 0):.0f}%' for (k2, o), v in sorted(cell.items()) if k2 == key and len(v) >= 30))

# ------------------------------------------------------------------ C. which EO axis the DRs come from
EAR = [r for r in ROWS if r['ea']]
P(f'\n## C. Which EO axis the DRs come from (scrambles with the per-EO-axis lists: {len(EAR)})')
if EAR:
    by = defaultdict(lambda: [0, 0.0, 0.0, 0, 0.0])
    for r in EAR:
        for e in AX:
            drs = sum(float(r['ea'][f'dr_{e}_{a}']) for a in AX if a != e)
            eos5 = r['F'][f'n_eo5_{e}_N'] + r['F'][f'n_eo5_{e}_I']
            b = by[int(r['F'][f'be_{e}'])]; b[0] += 1; b[1] += drs; b[2] += eos5; b[3] += (eos5 > 0); b[4] += float(r['ea'][f'eos_{e}'])
    P('  by bad edges on the EO axis: axes | mean EOs of <= 5 (N + I) | mean DR states of <= 10 through an EO on this axis | DR states per EO of <= 5 | share of axes with an EO of <= 5')
    for k in sorted(by):
        b = by[k]
        if b[0] < 30: continue
        P(f'   {k:2d} bad: {b[0]} | {b[2] / b[0]:.1f} | {b[1] / b[0]:.1f} | {b[1] / max(1, b[2]):.3f} | {100 * b[3] / b[0]:.1f}%')
    tw = defaultdict(list)
    for r in EAR:
        for e in AX:
            for a in AX:
                if a == e: continue
                t = [x for x in AX if x not in (e, a)][0]
                tw[(int(r['F'][f'be_{e}']), int(r['F'][f'be_{t}']))].append(float(r['ea'][f'dr_{e}_{a}']))
    P('  DR states of <= 10 on DR axis a through an EO on axis e, by bad edges on e (rows) and on the third axis t (columns): mean (pairs)')
    cols = [2, 4, 6, 8, 10]
    P('   e \\ t   ' + ' '.join(f'{c:>14d}' for c in cols))
    for be_e in cols:
        P(f'   {be_e:5d}   ' + ' '.join((f'{np.mean(tw[(be_e, c)]):8.1f} ({len(tw[(be_e, c)]):4d})' if len(tw[(be_e, c)]) >= 30 else f'{"-":>14s}') for c in cols))
    # JTuu: EOs piled on one axis
    sh = []
    for r in EAR:
        e5 = {e: r['F'][f'n_eo5_{e}_N'] + r['F'][f'n_eo5_{e}_I'] for e in AX}; tot = sum(e5.values())
        dr = {e: sum(float(r['ea'][f'dr_{e}_{a}']) for a in AX if a != e) for e in AX}; dt = sum(dr.values())
        if tot < 20 or dt == 0: continue
        top = max(AX, key=lambda e: e5[e])
        if e5[top] / tot >= 0.8: sh.append((e5[top] / tot, dr[top] / dt, dt))
    sh = np.array(sh)
    if len(sh):
        d = sh[:, 1] - sh[:, 0]; bs = [d[RNG.integers(0, len(d), len(d))].mean() for _ in range(B)]
        P(f'  scrambles with >= 20 EOs of <= 5 and >= 80% of them on one EO axis, and a DR of <= 10: {len(sh)}; that axis holds {100 * sh[:, 0].mean():.1f}% of the EOs and '
          f'{100 * sh[:, 1].mean():.1f}% of the DR states (mean of per-scramble shares); difference {100 * d.mean():+.1f} points [{100 * np.percentile(bs, 2.5):+.1f}, {100 * np.percentile(bs, 97.5):+.1f}]; '
          f'pooled DR share {100 * (sh[:, 1] * sh[:, 2]).sum() / sh[:, 2].sum():.1f}%')
    # all scrambles: EO share vs DR share of the EO-richest axis
    a_ = []
    for r in EAR:
        e5 = {e: r['F'][f'n_eo5_{e}_N'] + r['F'][f'n_eo5_{e}_I'] for e in AX}; tot = sum(e5.values())
        dr = {e: sum(float(r['ea'][f'dr_{e}_{a}']) for a in AX if a != e) for e in AX}; dt = sum(dr.values())
        if tot == 0 or dt == 0: continue
        top = max(AX, key=lambda e: e5[e]); a_.append((e5[top] / tot, dr[top] / dt))
    a_ = np.array(a_); P(f'  all scrambles with EOs and DRs ({len(a_)}): the EO-richest axis holds {100 * a_[:, 0].mean():.1f}% of the EOs of <= 5 and {100 * a_[:, 1].mean():.1f}% of the DR states')

# ------------------------------------------------------------------ D. details for the claims
P('\n## D. Claim details')
line('fewer than 4 EOs of <= 4 (N + I, quarter-turn ending counted once) = fewer than 8 with both endings counted', [r for r in ROWS if r['n_eo4'] < 4])
line('  the rest', [r for r in ROWS if r['n_eo4'] >= 4])
line('fewer than 8 EOs of <= 4 (N + I)', [r for r in ROWS if r['n_eo4'] < 8])
line('10/8/8 with an EO of <= 3', [r for r in ROWS if r['be'] == [8, 8, 10] and r['eo_best'] <= 3])
line('10/8/8 with shortest EO 4', [r for r in ROWS if r['be'] == [8, 8, 10] and r['eo_best'] == 4])
line('10/8/8 with no EO under 5', [r for r in ROWS if r['be'] == [8, 8, 10] and r['eo_best'] >= 5])
line('10/8/8, all', [r for r in ROWS if r['be'] == [8, 8, 10]])
line('50 or more EOs of <= 4 and best DR + finish >= 22', [r for r in ROWS if r['n_eo4'] >= 50 and r['best'] >= 22])
line('50 or more EOs of <= 4', [r for r in ROWS if r['n_eo4'] >= 50])
for r in sorted([r for r in ROWS if r['be'] == [8, 8, 10] and r['eo_best'] <= 3 and r['pop'].startswith('real')], key=lambda r: r['best'])[:3]:
    P(f"  10/8/8 with a short EO, official: {dates[r['id']][1]} ({dates[r['id']][2]}): {dates[r['id']][0]} | shortest EO {int(r['eo_best'])}, EOs<=4 {int(r['n_eo4'])}, DRs {int(r['n10'])}, best {int(r['best'])}")
for r in sorted([r for r in ROWS if r['n_eo4'] >= 50 and r['best'] >= 22 and r['pop'].startswith('real')], key=lambda r: -r['best'])[:3]:
    P(f"  50+ four-movers and best >= 22, official: {dates[r['id']][1]} ({dates[r['id']][2]}): {dates[r['id']][0]} | shortest EO {int(r['eo_best'])}, EOs<=4 {int(r['n_eo4'])}, DRs {int(r['n10'])}, best {int(r['best'])}, bad edges {r['be']}")
TN = [r for r in ROWS if r['pop'] in ('real_new', 'gen')]
for lab, f in (('middle <= 17 moves', lambda L: L <= 17), ('middle 18', lambda L: L == 18), ('middle 19', lambda L: L == 19), ('middle 20', lambda L: L == 20), ('middle 21', lambda L: L == 21)):
    rs = [r for r in TN if f(r['F']['t_len'])]; s = stats(rs)
    P(f'  current-era scrambles, {lab}: n={s[0]}, easy {100 * s[1]:.1f}%, hard {100 * s[2]:.1f}%, median DRs {s[3]:.0f}, mean best {s[4]:.2f}')
ex = sorted([r for r in ROWS if r['pop'] == 'real_new' and r['F']['t_len'] <= 16 and r['best'] <= 19], key=lambda r: (r['best'], -r['n10']))
for r in ex[:3]:
    P(f"  short and easy: {dates[r['id']][1]} ({dates[r['id']][2]}): {dates[r['id']][0]} | middle {int(r['F']['t_len'])}, bad edges {r['be']}, DRs {int(r['n10'])}, best {int(r['best'])}")
ex = sorted([r for r in ROWS if r['pop'] == 'real_new' and r['F']['t_len'] >= 21 and r['best'] >= 23], key=lambda r: (r['n10']))
for r in ex[:2]:
    P(f"  long and hard: {dates[r['id']][1]} ({dates[r['id']][2]}): {dates[r['id']][0]} | middle {int(r['F']['t_len'])}, bad edges {r['be']}, DRs {int(r['n10'])}, best {int(r['best'])}")
# how lopsided the three axes are
v = [max(r['ta'].values()) / sum(r['ta'].values()) for r in ROWS if sum(r['ta'].values()) >= 10]
P(f'  scrambles with >= 10 DRs (summed over axes): {len(v)}; the best axis holds {100 * np.mean(v):.1f}% of them on average (median {100 * np.median(v):.1f}%); '
  f'over half on one axis: {100 * np.mean(np.array(v) > 0.5):.1f}%; over 80%: {100 * np.mean(np.array(v) > 0.8):.1f}%')
z = [sum(1 for a in AX if r['ta'][a] == 0) for r in ROWS if r['n10'] > 0]
P(f'  scrambles with a DR of <= 10: an axis with none: {100 * np.mean(np.array(z) >= 1):.1f}%; two axes with none: {100 * np.mean(np.array(z) == 2):.1f}%')
P('done')
