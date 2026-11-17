#!/usr/bin/env python3
"""Everything the report prints, into out/results.json: the cards and the current policies graded on the exact
table (uniform within a DRM), at the three RZP lengths, on the real attempts, under other weights; the ceilings;
the two-bars count; the features that did not help."""
import json, os, sys, itertools
import numpy as np
from lib import *
import cards as C
from cards import CARDS, BASE, card_mask
from fastsearch import Pop
HERE = os.path.dirname(os.path.abspath(__file__))
W0 = weights()
att = np.memmap(os.path.join(HERE, '..', 'out', 'big', 'att_counts.u32'), dtype='<u4', mode='r').reshape(3, 11, N0)
NSW = {L: np.asarray(att[i, 0]).astype(np.float64) for i, L in enumerate((4, 5, 6))}
def prof(m, sw, K=6, w=None, pop=None):
    """profile() with optional population weights (pop: weight per coset)."""
    w = weights(K) if w is None else w
    if pop is None: return profile(m, sw, K, w)
    pw = pop[m]; dd = d[m]; s = sw[m]; tot = pw.sum()
    out = {'n': float(tot), 'switch': float((pw * s).sum() / tot)}
    for name, sel in (('le4', dd <= K - 2), ('d5', dd == K - 1), ('d6', dd == K), ('good', dd <= K)):
        t = (pw * sel).sum()
        out['n_' + name] = float(t); out['miss_' + name] = float((pw * (sel & ~s)).sum() / t) if t else 0.0
    out['wasted'] = float((pw * (s & (dd > K))).sum() / tot)
    out['precision'] = float((pw * (s & (dd <= K))).sum() / max(1e-12, (pw * s).sum()))
    out['loss'] = float(((pw * w[dd])[~s].sum() + (pw * (s & (dd > K))).sum()) / tot)
    return out
def grp(m, g, K=6, w=None):
    w = weights(K) if w is None else w
    h = np.bincount(d[g], minlength=11); n = int(g.sum()); a = float(w[d[g]].sum()); b = int((d[g] > K).sum())
    return dict(n=n, share=n / int(m.sum()), le4=int(h[:K - 1].sum()), d5=int(h[K - 1]), d6=int(h[K]), d7=int(h[K + 1]) if K + 1 < 11 else 0,
                longer=int(h[K + 2:].sum()) if K + 2 < 11 else 0, bad=b, good=int(h[:K + 1].sum()), rate=float(h[:K + 1].sum() / n), ratio=(a / b if b else None))
QUICKALL = ['pairs', 'arm', 'cc', 'side', 'fake', 'edges_paired', 'hole_cfg', 'edges_same_layer', 'ud_split', 'cols_bad']
F['cc'] = F['corner_case']; F['arm'] = F['carm'] * 10 + F['earm']; F['ccs'] = F['corner_case'] * 10 + F['case_suffix']
R = {'weights': {'w6': 3, 'rho': 3, 'le4': 27, 'd5': 9, 'd6': 3, 'wasted': 1}, 'drm': {}, 'N0': int(N0)}
ALLSW = {k: np.zeros(N0, bool) for k in ('card', 'card_time', 'pairs', 'best_old')}
for drm, groups in CARDS.items():
    c, e = drm; m = drm_mask(c, e); name = f'{c}c{e}e'; dd = d[m]
    X = {'n': int(m.sum()), 'hist': [int(v) for v in np.bincount(dd, minlength=11)], 'n_le4': int((dd <= 4).sum()), 'n_d5': int((dd == 5).sum()), 'n_d6': int((dd == 6).sum()),
         'sub7': float((dd <= 6).mean())}
    cum = np.zeros(N0, bool); G = []
    for label, g, v in groups:
        cum = cum | g
        r = grp(m, g); r.update(label=label, verdict=v, cum=prof(m, cum))
        r['K5'] = grp(m, g, 5); r['K7'] = grp(m, g, 7)
        G.append(r)
    X['groups'] = G
    cs = card_mask(drm); ct = card_mask(drm, ('switch', 'time'))
    X['card'] = prof(m, cs); X['card_time'] = prof(m, ct)
    X['always'] = prof(m, m.copy()); X['never'] = prof(m, np.zeros(N0, bool)); X['exact'] = prof(m, d <= 6)
    X['base'] = {key: dict(name=nm, who=who, **prof(m, sw)) for key, nm, who, sw in BASE[drm]}
    # other RZP lengths: the same switch sets, graded with the target moved; and the best set of card groups
    for K in (5, 7):
        wk = weights(K)
        X[f'K{K}'] = {'card': prof(m, cs, K, wk), 'card_time': prof(m, ct, K, wk), 'base': {key: prof(m, sw, K, wk) for key, nm, who, sw in BASE[drm]},
                      'always': prof(m, m.copy(), K, wk), 'never': prof(m, np.zeros(N0, bool), K, wk)}
        best = np.zeros(N0, bool)
        for label, g, v in groups:
            if wk[d[g]].sum() > (d[g] > K).sum(): best |= g
        X[f'K{K}']['regroup'] = prof(m, best, K, wk)
    # real attempts (5-move RZPs)
    X['real'] = {'attempts': float(NSW[5][m].sum()), 'card': prof(m, cs, pop=NSW[5]), 'card_time': prof(m, ct, pop=NSW[5]),
                 'base': {key: prof(m, sw, pop=NSW[5]) for key, nm, who, sw in BASE[drm]}}
    # other weights
    S = {}
    for w6 in (2.0, 3.0, 5.0):
        for rho in (2.0, 3.0, 4.5):
            ww = weights(6, w6, rho)
            S[f'{w6:g},{rho:g}'] = {'card': prof(m, cs, 6, ww)['loss'], 'card_time': prof(m, ct, 6, ww)['loss'], **{key: prof(m, sw, 6, ww)['loss'] for key, nm, who, sw in BASE[drm]},
                                    'flips': [label for label, g, v in groups if (v == 'switch') != (ww[d[g]].sum() > (d[g] > 6).sum()) and v != 'time']}
    X['sens'] = S
    # ceilings: the best any rule could do from a set of reads (cell-optimal; computer only)
    P = Pop(m); ceil = {}
    for key, feats in (('pairs', ['pairs']), ('pairs+arm', ['pairs', 'arm']), ('pairs+case', ['pairs', 'ccs']), ('pairs+side', ['pairs', 'side']), ('pairs+fake', ['pairs', 'fake']),
                       ('pairs+arm+case', ['pairs', 'arm', 'cc']), ('pairs+arm+side', ['pairs', 'arm', 'side']), ('pairs+arm+case+side', ['pairs', 'arm', 'cc', 'side']), ('quick', QUICKALL)):
        feats = [f for f in feats if len(np.unique(F[f][m])) > 1]
        L, sw, nc, nt = P.loss(feats, detail=True)
        ceil[key] = dict(cells=nc, taken=nt, **prof(m, sw))
    ceil['sigma'] = dict(cells=0, taken=0, **prof(m, best_cells(m, ['sigma', 'qsig'])[0]))
    X['ceil'] = ceil
    R['drm'][name] = X
    ALLSW['card'] |= cs; ALLSW['card_time'] |= ct
    ALLSW['pairs'] |= BASE[drm][0][3] & m
    bo = min(BASE[drm], key=lambda b: prof(m, b[3])['loss'])
    ALLSW['best_old'] |= bo[3] & m; X['best_old'] = bo[0]
# ---------------------------------------------------------------- all DRMs together, weighted by the real 5-move attempts
allm = np.zeros(N0, bool)
for drm in CARDS: allm |= drm_mask(*drm)
R['all'] = {'attempts5': float(NSW[5].sum()), 'attempts5_card_drms': float(NSW[5][allm].sum()),
            'uniform': {k: prof(allm, v) for k, v in ALLSW.items()}, 'real': {k: prof(allm, v, pop=NSW[5]) for k, v in ALLSW.items()}}
main = drm_mask(4, 4) | drm_mask(4, 2) | drm_mask(3, 2) | drm_mask(7, 8)
R['main4'] = {'uniform': {k: prof(main, v) for k, v in ALLSW.items()}, 'real': {k: prof(main, v, pop=NSW[5]) for k, v in ALLSW.items()}, 'attempts5': float(NSW[5][main].sum())}
R['real_scrambles'] = 6000
R['real_attempts'] = {str(L): float(NSW[L].sum()) for L in (4, 5, 6)}
# ---------------------------------------------------------------- two bars (4c4e) and side turns
m = drm_mask(4, 4); hb = F['hbar']
T = {'by_count': []}
for h in range(6):
    g = m & (hb == h); r = grp(m, g); r['count'] = h; T['by_count'].append(r)
T['le2'] = prof(m, m & (hb <= 2)); T['le3'] = prof(m, m & (hb <= 3)); T['le1'] = prof(m, m & (hb <= 1))
# what the count adds to the card, and the card to the count (cell-optimal over card group x count)
gid = np.full(N0, -1, np.int64)
for i, (label, g, v) in enumerate(CARDS[(4, 4)]): gid[g] = i
F['gid'] = gid
T['card_x_count'] = dict(prof(m, best_cells(m, ['gid', 'hbar'])[0]))
T['count_x_pairs'] = dict(prof(m, best_cells(m, ['hbar', 'pairs'])[0]))
# how the count splits the card's groups
T['groups'] = []
for label, g, v in CARDS[(4, 4)]:
    row = {'label': label, 'verdict': v}
    for key, sel in (('le2', hb <= 2), ('eq3', hb == 3), ('ge4', hb >= 4)):
        gg = g & sel; row[key] = grp(m, gg) if gg.any() else None
    T['groups'].append(row)
# the bar by where its holes are: share at 2 half turns or fewer, and the sub-7 rate there
T['bar'] = {}
for key, sel in (('on', C.HC == 0), ('off', C.HC >= 1)):
    gg = m & (C.P == 2) & (C.EP == 1) & sel
    T['bar'][key] = {'le2_share': float((gg & (hb <= 2)).sum() / gg.sum()), 'le2': grp(m, gg & (hb <= 2))}
# by pairs: share of each pair count with 2 half turns or fewer, and of the good cases there
T['by_pairs'] = []
for p in range(5):
    g = m & (F['pairs'] == p)
    T['by_pairs'].append({'pairs': p, 'n': int(g.sum()), 'le2': int((g & (hb <= 2)).sum()), 'eq3': int((g & (hb == 3)).sum()), 'ge4': int((g & (hb >= 4)).sum()),
                          'good': int((g & (d <= 6)).sum()), 'good_le2': int((g & (hb <= 2) & (d <= 6)).sum()), 'good_eq3': int((g & (hb == 3) & (d <= 6)).sum())})
# can the quick reads tell 2-or-fewer from 3-or-more?  cells of all quick reads that hold both
P = Pop(m)
code = np.zeros(P.n, np.int64)
for f in QUICKALL:
    cc_, s = P.code(f); code = code * s + cc_
le2 = (hb[P.idx] <= 2)
n_le2 = np.bincount(code, weights=le2); n_all = np.bincount(code)
mixed = (n_le2 > 0) & (n_le2 < n_all)
T['quick_cells'] = int((n_all > 0).sum()); T['quick_mixed_share'] = float(n_all[mixed].sum() / P.n)
T['quick_err'] = float(np.minimum(n_le2, n_all - n_le2).sum() / P.n)        # error of the best guess of "2 or fewer" from all quick reads
code2 = np.zeros(P.n, np.int64)
for f in ['pairs', 'edges_paired']:
    cc_, s = P.code(f); code2 = code2 * s + cc_
a = np.bincount(code2, weights=le2); b = np.bincount(code2)
T['pairs_err'] = float(np.minimum(a, b - a).sum() / P.n)
# what the count at 2 or fewer holds of what the pairs rule and the card leave behind
pm = m & (F['pairs'] <= 1); le2 = hb <= 2; cm = m & ~card_mask((4, 4))
T['pairs_missed_le2'] = {k: [int((pm & sel & le2).sum()), int((pm & sel).sum())] for k, sel in (('le4', d <= 4), ('d5', d == 5), ('d6', d == 6))}
T['card_missed_le2'] = {k: [int((cm & sel & le2).sum()), int((cm & sel).sum())] for k, sel in (('le4', d <= 4), ('d5', d == 5), ('d6', d == 6))}
T['low_pair_le2'] = grp(m, pm & le2)
T['card_or_le2'] = prof(m, card_mask((4, 4)) | (m & le2))
T['fanti_or_le2'] = prof(m, (BASE[(4, 4)][5][3] & m) | (m & le2))
R['twobars'] = T
# ---------------------------------------------------------------- features tried (4c4e): cell-optimal loss with pairs + one read
P = Pop(m); tried = []
for key, label in (('carm', 'corner ARM'), ('earm', 'edge ARM'), ('arm', 'ARM (both digits)'), ('ccs', 'corner case with its suffix'), ('side', 'side pairs'), ('fake', 'fake pairs'),
                   ('edges_paired', 'paired edges (bar or two edges)'), ('hole_cfg', 'where the two holes are'), ('edges_same_layer', 'bad edges in one layer'), ('ud_split', 'corners per layer'),
                   ('unpaired_corners', 'corners not in a pair'), ('split_pairs', 'split pairs'), ('ar_bars', 'AR bars (rodneykinney)'), ('pair_fake_same_edge', 'a pair and a fake pair on one edge'), ('cols_bad', 'corners in columns'),
                   ('corner_dist', 'moves to orient the corners alone (computer only)'), ('lb_simple', 'corner moves + missing pairs (computer only)'),
                   ('moves_to_ar', 'moves to AR (computer only)'), ('a_one_from_d', '4a corners one U/D turn from 4d (wen)'),
                   ('hbar', 'half turns to two bars (needs the whole trace)'), ('sigma', 'side turns (needs the whole trace)')):
    L, sw, nc, nt = P.loss(['pairs', key], detail=True)
    L1, sw1, nc1, nt1 = P.loss([key], detail=True)
    tried.append(dict(key=key, label=label, cells=nc, with_pairs=prof(m, sw), alone=prof(m, sw1)))
R['tried44'] = tried
R['tried44_pairs'] = prof(m, P.loss(['pairs'], detail=True)[1])
json.dump(R, open(os.path.join(HERE, 'out', 'results.json'), 'w'), indent=1)
print('wrote results.json')
for k, v in R['all']['real'].items(): print('all DRMs, real 5-move attempts', k, fmt_ := f"switch {100*v['switch']:.1f}% miss {100*v['miss_le4']:.1f} {100*v['miss_d5']:.1f} {100*v['miss_d6']:.1f} loss {v['loss']:.4f}")
for k, v in R['all']['uniform'].items(): print('all DRMs, uniform', k, f"switch {100*v['switch']:.1f}% miss {100*v['miss_le4']:.1f} {100*v['miss_d5']:.1f} {100*v['miss_d6']:.1f} loss {v['loss']:.4f}")
for k, v in R['main4']['real'].items(): print('main 4 DRMs, real', k, f"switch {100*v['switch']:.1f}% miss {100*v['miss_le4']:.1f} {100*v['miss_d5']:.1f} {100*v['miss_d6']:.1f} loss {v['loss']:.4f}")
print('two bars: quick cells', T['quick_cells'], 'mixed share', T['quick_mixed_share'], 'err', T['quick_err'], 'pairs err', T['pairs_err'])
print('card x count', fmt(T['card_x_count'])); print('count x pairs', fmt(T['count_x_pairs']))
x = R['drm']['4c4e']
print('4c4e real card', x['real']['card']); print('4c4e K7', x['K7']['card'], x['K7']['regroup']); print('4c4e K5', x['K5']['card'], x['K5']['regroup'])
print('sens', {k: (round(v['card'], 3), round(v['pairs'], 3), round(v['pairs+arm'], 3), v['flips']) for k, v in x['sens'].items()})
# ---------------------------------------------------------------- extras for the write-up (4c4e)
import linfit, relfeat, tree as TR
m = drm_mask(4, 4); EX = {}
# reads the card needs, as shares of 4c4e
EX['reads44'] = {'one_pair': float(((C.P == 1) & m).sum() / m.sum()), 'one_pair_arm21': float(((C.P == 1) & (C.ARM == 21) & m).sum() / m.sum()),
                 'one_pair_arm21_4b': float(((C.P == 1) & (C.ARM == 21) & (C.CC == 1) & m).sum() / m.sum()), 'bar': float(((C.P == 2) & (C.EP == 1) & m).sum() / m.sum()),
                 'zero_nofake': float(((C.P == 0) & (C.FAKE == 0) & m).sum() / m.sum()), 'one_pair_arm21_4a': float(((C.P == 1) & (C.ARM == 21) & (C.CC == 0) & m).sum() / m.sum()), 'two_plus': float(((C.P >= 2) & m).sum() / m.sum()), 'zero': float(((C.P == 0) & m).sum() / m.sum())}
# points systems
EX['any3'] = prof(m, (F['pairs'] + F['side']) >= 3)
EX['pts_2p_s_ge4'] = prof(m, (2 * F['pairs'] + F['side']) >= 4)
EX['lb6'] = prof(m, F['lb_simple'] <= 6)
for key, spec in (('lin_pairs_side', [('pairs', 'num'), ('side', 'num')]),
                  ('lin_big', [('pairs', 'num'), ('side', 'num'), ('fake', 'num'), ('carm', 'cat'), ('earm', 'cat'), ('ccs', 'cat'), ('hole_cfg', 'cat'), ('edges_paired', 'cat'), ('edges_same_layer', 'cat'), ('ud_split', 'cat')])):
    idx, Xm, names, beta, score = linfit.fit(m, spec); L, thr, sw = linfit.best_threshold(m, idx, score)
    EX[key] = dict(terms=len(names), **prof(m, sw))
# pairwise relations between two bad pieces: best class to add to the pair count
idx = np.flatnonzero(m); M = relfeat.counts(idx); ddx = d[idx]; wv = W0[ddx]; bv = (ddx > 6).astype(float)
def cl(code):
    u, inv = np.unique(code, return_inverse=True); a = np.bincount(inv, weights=wv); b = np.bincount(inv, weights=bv); return float(np.minimum(a, b).sum() / idx.size)
pr = F['pairs'][idx].astype(np.int64)
rel = sorted((cl(pr * 16 + M[:, k]), relfeat.describe(k)) for k in range(relfeat.NCLS) if M[:, k].max() > 0)
EX['rel_classes'] = relfeat.NCLS; EX['rel_best'] = rel[0][0]; EX['rel_best_desc'] = rel[0][1]; EX['rel_second'] = rel[1][0]; EX['rel_second_desc'] = rel[1][1]
# trees: size against cost, led by pairs or free
F['one'] = np.zeros(N0, np.int8)
def tree_loss(feats, L, strat):
    ix, leaves = TR.grow(m, feats, max_leaves=L, strat=strat, verbose=False, min_gain=0.0005)
    sw = np.zeros(N0, bool)
    for r in leaves:
        if r['ratio'] > 1: sw[ix[r['mask']]] = True
    return dict(leaves=len(leaves), **prof(m, sw))
EX['trees_free'] = {str(L): tree_loss(['pairs'] + TR.QUICK, L, 'one') for L in (8, 16, 40)}
EX['trees_pairs'] = {str(L): tree_loss(TR.QUICK, L, 'pairs') for L in (8, 16, 40)}
# smallest pairs x ARM rule that misses no case of 5 or less (4c4e): every cell that holds one
code = (F['pairs'].astype(np.int64) * 100 + F['arm'])[m]; dm = d[m]
cells_short = np.unique(code[dm <= 5])
EX['pairs_arm_no_miss5'] = prof(m, m & np.isin(F['pairs'].astype(np.int64) * 100 + F['arm'], cells_short))
# numbers for the claims table and the text
g2 = m & (C.P == 2)
EX['p2_4b0'] = grp(m, g2 & (C.CCS == 10)); EX['p2_4b2'] = grp(m, g2 & (C.CCS == 12))
EX['p2_4b0_in_bar_off'] = int((g2 & (C.CCS == 10) & (C.EP == 1) & (C.HC >= 1) & (C.FAKE <= 1)).sum())
EX['p1_4d'] = grp(m, m & (C.P == 1) & (C.CC == 3))
EX['p1_other_max'] = max(grp(m, m & (C.P == 1) & (C.CC == k))['rate'] for k in (0, 1, 2))
bars = []; 
for a_ in np.unique(C.ARM[g2]):
    b1 = g2 & (C.ARM == a_) & (C.EP == 1); b2 = g2 & (C.ARM == a_) & (C.EP == 2)
    if b1.any() and b2.any(): bars.append(bool((d[b1] <= 6).mean() < (d[b2] <= 6).mean()))
EX['bar_arms'] = [int(sum(bars)), len(bars)]
g1 = m & (C.P == 1) & (C.ARM == 21) & (C.CC == 1)
EX['4b_side'] = {str(k): grp(m, g1 & (C.SIDE == k)) for k in (0, 1, 2)}
g4a = m & (C.P == 1) & (C.ARM == 21) & (C.CC == 0)
EX['4a_layer'] = {'same': grp(m, g4a & C.ESL), 'diff': grp(m, g4a & ~C.ESL), 'all': grp(m, g4a)}
EX['4a_both'] = grp(m, g4a & C.ESL & (C.COLS == 2))
EX['rk_0p'] = grp(m, m & (C.P == 0) & (C.FAKE == 0) & ((C.CCS == 0) | (C.CCS == 32)))
EX['nofake0'] = grp(m, m & (C.P == 0) & (C.FAKE == 0)); EX['zero_pairs'] = grp(m, m & (C.P == 0))
g21 = m & (C.P == 1) & (C.ARM == 21); EX['p1_arm21'] = grp(m, g21); EX['p1_arm21_card'] = grp(m, g21 & card_mask((4, 4)))
EX['p1_arm21_by_cc'] = {k: grp(m, g21 & (C.CC == i)) for k, i in (('a', 0), ('b', 1), ('d', 3))}
m42 = drm_mask(4, 2)
EX['42_jzp_4a'] = grp(m42, m42 & (C.P == 0) & (C.ARM == 0) & (C.CC == 0)); EX['42_jzp_4b'] = grp(m42, m42 & (C.P == 0) & (C.ARM == 0) & (C.CC == 1))
m88 = drm_mask(8, 8)
EX['88_twist'] = {'44': grp(m88, m88 & (F['twist_major'] == 4)), '71': grp(m88, m88 & (F['twist_major'] == 7))}
# ---------------------------------------------------------------- what ARM on every case, and the slower reads on more cases, would add (4c4e)
card44 = card_mask((4, 4)) & m; n44 = int(m.sum())
leaf = np.full(N0, -1)
for i_, (label, g, v) in enumerate(CARDS[(4, 4)]): leaf[g] = i_
F['leaf'] = leaf
AF = {}
sw_, nc_, nt_ = best_cells(m, ['leaf', 'arm']); AF['card_arm'] = dict(cells=nc_, **prof(m, sw_))                       # ARM read on every group of the card
sw_, nc_, nt_ = best_cells(m, ['pairs', 'arm']); AF['pairs_arm'] = dict(cells=nc_, switched=nt_, **prof(m, sw_))        # the best rule on pairs + ARM alone
AF['pairs_arm_is_fanti'] = bool((sw_ == ([b for b in BASE[(4, 4)] if b[0] == 'pairs+arm'][0][3] & m)).all())
sw_, nc_, nt_ = best_cells(m, ['pairs', 'edges_paired', 'fake', 'arm']); AF['trace_arm'] = dict(cells=nc_, switched=nt_, **prof(m, sw_))
bar = m & (C.P == 2) & (C.EP == 1)
AF['no_bar_split'] = prof(m, card44 | bar)                                                                                # every 2-pair case, no look at the edges out of the slice
bar_arm = bar & (np.isin(C.ARM, (0, 11, 21, 31)) | (C.FAKE == 2))
AF['bar_by_arm'] = prof(m, (card44 & ~bar) | bar_arm); AF['bar_by_arm_grp'] = grp(m, bar_arm)                             # the bar row read with ARM instead
AF['bar_earm'] = {str(k): grp(m, bar & (C.EA == k)) for k in (0, 1, 2)}
AF['bar_fake2'] = grp(m, bar & (C.FAKE == 2)); AF['bar_off_fake'] = {str(k): grp(m, bar & (C.HC >= 1) & (C.FAKE == k)) for k in (0, 1, 2)}
AF['bar_on'] = grp(m, bar & (C.HC == 0)); AF['bar_off'] = grp(m, bar & (C.HC >= 1))
AF['bar_off_arm'] = grp(m, bar & (C.HC >= 1) & (C.FAKE <= 1) & np.isin(C.ARM, (21, 31)))
z0 = m & (C.P == 0)
AF['zero_arm'] = grp(m, z0 & np.isin(C.ARM, (0, 42))); AF['zero_arm21_row'] = grp(m, z0 & (C.ARM == 21) & (C.FAKE == 0) & (C.UDS == 2))
AF['zero_by_arm'] = prof(m, (card44 & ~z0) | (z0 & (np.isin(C.ARM, (0, 42)) | ((C.ARM == 21) & (C.FAKE == 0) & (C.UDS == 2)))))
# the slower reads, spent on the groups (pairs, where the pairs are, fake pairs, ARM) where they pay most per case
def budget(fast, slow, marks=(0.05, 0.10, 0.15, 0.20, 0.30)):
    idx_, uf, invf = cells(m, fast); _, us, invs = cells(m, fast + slow)
    wd = W0[d[idx_]]; bd = (d[idx_] > 6).astype(float)
    cd = np.bincount(invf, weights=wd, minlength=len(uf)); cs_ = np.bincount(invf, weights=bd, minlength=len(uf)); cnt = np.bincount(invf, minlength=len(uf))
    sd = np.bincount(invs, weights=wd, minlength=len(us)); ss = np.bincount(invs, weights=bd, minlength=len(us))
    first_ = np.zeros(len(us), np.int64); first_[invs] = invf
    direct = np.minimum(cd, cs_); fine = np.bincount(first_, weights=np.minimum(sd, ss), minlength=len(uf)); gain = direct - fine
    out = {'fast_only': float(direct.sum() / n44), 'everywhere': float(fine.sum() / n44), 'fast_cells': len(uf), 'all_cells': len(us), 'steps': []}
    tot = direct.sum(); used = 0; mi = 0
    for j in np.argsort(-(gain / cnt)):
        if gain[j] <= 0: break
        if mi < len(marks) and (used + cnt[j]) / n44 > marks[mi]:
            out['steps'].append({'mark': marks[mi], 'share': float(used / n44), 'loss': float(tot / n44)}); mi += 1
        tot -= gain[j]; used += cnt[j]
    out['any_gain'] = {'share': float(used / n44), 'loss': float(tot / n44)}
    return out
AF['budget_cc_side'] = budget(['pairs', 'edges_paired', 'fake', 'arm'], ['cc', 'side'])
AF['budget_all'] = budget(['pairs', 'edges_paired', 'fake', 'arm'], ['cc', 'side', 'cols_bad', 'ud_split', 'hole_cfg'])
# the card's own use of the slower reads: where it asks for the corner case, the side pairs, the columns, the edges out of the slice, the corner layers
# the stacked 4a row: by ARM and by side pairs; the card with that row kept to ARM 21
st4a = m & (C.P == 1) & (C.CC == 0) & (C.COLS == 2) & (C.CA == 2)
AF['stacked'] = {'21': grp(m, st4a & (C.ARM == 21)), '2022': grp(m, st4a & (C.ARM != 21)), '2022_side': grp(m, st4a & (C.ARM != 21) & (C.SIDE >= 1)),
                 '2022_noside': grp(m, st4a & (C.ARM != 21) & (C.SIDE == 0)), '21_side': grp(m, st4a & (C.ARM == 21) & (C.SIDE >= 1)),
                 '21_noside': grp(m, st4a & (C.ARM == 21) & (C.SIDE == 0)), 'side': grp(m, st4a & (C.SIDE >= 1)), 'noside': grp(m, st4a & (C.SIDE == 0)),
                 'not_stacked_21': grp(m, m & (C.P == 1) & (C.CC == 0) & (C.COLS != 2) & (C.ARM == 21)),
                 'not_stacked_2022': grp(m, m & (C.P == 1) & (C.CC == 0) & (C.COLS != 2) & (C.CA == 2) & (C.ARM != 21)),
                 'p1_2022': grp(m, m & (C.P == 1) & (C.CA == 2) & (C.ARM != 21)), 'p1_2022_4d': grp(m, m & (C.P == 1) & (C.CA == 2) & (C.ARM != 21) & (C.CC == 3)),
                 'p1_2022_4b': grp(m, m & (C.P == 1) & (C.CA == 2) & (C.ARM != 21) & (C.CC == 1))}
ofd = F['a_one_from_d'].astype(bool); p4a = m & (C.P == 1) & (C.CC == 0)
AF['one_from_4d'] = {'yes': grp(m, p4a & ofd), 'no': grp(m, p4a & ~ofd), 'yes_2x': grp(m, p4a & ofd & (C.CA == 2)), 'yes_in_row': grp(m, p4a & ofd & st4a & (C.SIDE >= 1)),
                     'row_not': grp(m, st4a & (C.SIDE >= 1) & ~ofd), 'yes_stacked': bool((C.COLS[p4a & ofd] == 2).all())}
AF['card_arm21_only'] = prof(m, card44 & ~(st4a & (C.ARM != 21)))                                                         # the card without the ARM 20 / 22 part of that row
AF['card_old_4a'] = prof(m, (card44 & ~st4a) | (st4a & (C.ARM == 21)))                                                    # ... and without the side pair on it (Evan's split as he gave it)
AF['time_pocket'] = grp(m, m & (C.P == 1) & np.isin(C.ARM, (10, 11)) & (C.SIDE == 3))
EX['reads44'].update({'one_pair_arm2x': float((m & (C.P == 1) & (C.CA == 2)).sum() / n44), 'one_pair_arm2022': float((m & (C.P == 1) & (C.CA == 2) & (C.ARM != 21)).sum() / n44),
                      'stacked_2x': float(st4a.sum() / n44), 'bar_lt2fake': float((bar & (C.FAKE <= 1)).sum() / n44), 'bar_fake2': float((bar & (C.FAKE == 2)).sum() / n44)})
EX['armfree'] = AF
print('ARM on every case:', {k: round(v['loss'], 4) for k, v in AF.items() if isinstance(v, dict) and 'loss' in v}, 'pairs+ARM best = Fanti:', AF['pairs_arm_is_fanti'])
print('budget cc+side', AF['budget_cc_side']); print('budget all', AF['budget_all']); print('stacked', {k: (v['n'], round(v['rate'], 3), v['d5']) for k, v in AF['stacked'].items()})
R['extra'] = EX
json.dump(R, open(os.path.join(HERE, 'out', 'results.json'), 'w'), indent=1)
print('extras', {k: (round(v['loss'], 4) if isinstance(v, dict) and 'loss' in v else v) for k, v in EX.items() if k not in ('trees_free', 'trees_pairs')})
print({k: (v['leaves'], round(v['loss'], 4)) for k, v in EX['trees_free'].items()}, {k: (v['leaves'], round(v['loss'], 4)) for k, v in EX['trees_pairs'].items()})
