#!/usr/bin/env python3
"""Question 4 and the open questions of the notes (section D) that the exact tables answer.  Output: out/q4.tsv
(one line per answer) and printed text.  All on P1 (uniform; equal to the switched state after any RZP for every
DRM but 6cXe/8cXe)."""
import os, sys, math
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import pop, search
F = pop.feat(); d = F['d'].astype(int)
L = []
def put(q, what, val, n=''):
    L.append(f'{q}\t{what}\t{val}\t{n}'); print(f'[{q}] {what}: {val} {n}')
def key(m, combo):
    k = np.zeros(m.sum(), np.int64)
    for f in combo:
        u, inv = np.unique(F[f][m], return_inverse=True); k = k * len(u) + inv
    return np.unique(k, return_inverse=True)[1]
def info(m, combo, k=6):
    y = (d[m] <= k).astype(float); kk = key(m, combo) if combo else np.zeros(m.sum(), np.int64)
    n, pos = search.evaluate(kk, y); st, po, p, disc, sw = search.separation(n, pos)
    return search.mi(n, pos), st, po, n, pos, p
def best_at_share(m, combo, share, k=6):
    """Switch the best cells (by p) until the share is reached (the last cell split proportionally): recall, precision."""
    y = (d[m] <= k).astype(float); kk = key(m, combo); n, pos = search.evaluate(kk, y)
    o = np.argsort(-pos / n); tot = n.sum(); target = share * tot; got = 0; hit = 0
    for i in o:
        take = min(n[i], target - got)
        if take <= 0: break
        got += take; hit += pos[i] * take / n[i]
    return hit / pos.sum(), hit / got
ARM = ['carm', 'earm']; CASE = ['corner_case', 'case_suffix']
for drm in [(4, 4), (4, 2), (4, 6)]:
    m = pop.drm_mask(*drm); nm = pop.drm_name(*drm)
    h = info(m, [])[0]
    for label, combo in [('ARM', ARM), ('pairs', ['pairs']), ('corner case + suffix', CASE), ('edges with a pair', ['edges_paired']),
                         ('ARM + pairs', ARM + ['pairs']), ('ARM + corner case', ARM + CASE), ('pairs + corner case', ['pairs'] + CASE),
                         ('ARM + pairs + corner case', ARM + ['pairs'] + CASE), ('pairs + side/2', ['pairs_plus_half_side_x2']),
                         ('edges with a pair + slice', ['edges_paired', 'edges_same_slice'])]:
        mi_, st, po, n, pos, p = info(m, combo)
        rec, prec = best_at_share(m, combo, 0.25)
        put('Q4', f'{nm}: {label}', f'MI {mi_:.4f} bits, strict sep {st:.3f}, pooled sep {po:.3f}, best 25% of states switched: recall {rec:.3f}, precision {prec:.3f}', f'{int(m.sum())} states')
# wen D14349: pick 2 of 3 (>1 pair / ARM / corner structure): lowest false-negative rate at the same switch share as '2+ pairs'
m = pop.drm_mask(4, 4); share2 = float((F['pairs'][m] >= 2).mean())
for label, combo in [('pairs + ARM', ['pairs'] + ARM), ('pairs + corner case', ['pairs'] + CASE), ('ARM + corner case', ARM + CASE), ('all three', ['pairs'] + ARM + CASE)]:
    rec, prec = best_at_share(m, combo, share2)
    put('D14349 wen', f'4c4e, switching the best {share2:.3f} of states (the share of 2+ pairs), {label}', f'false negatives {1 - rec:.3f} of sub-7 states, precision {prec:.3f}')
rec, prec = best_at_share(m, ['pairs'], share2); put('D14349 wen', '4c4e, 2+ pairs alone', f'false negatives {1 - rec:.3f}, precision {prec:.3f}')
# bars vs separate pairs (bpaul D12986, Yura D12993, Pritam EO-DR-526)
for drm in [(4, 4), (7, 8), (4, 2), (8, 8)]:
    m = pop.drm_mask(*drm)
    for npairs in (2, 3, 4):
        for e_ in sorted(set(F['edges_paired'][m & (F['pairs'] == npairs)].tolist())):
            mm = m & (F['pairs'] == npairs) & (F['edges_paired'] == e_)
            if mm.sum(): put('bars', f'{pop.drm_name(*drm)}: {npairs} pairs on {e_} edge(s) ({int(F["bars"][mm].max())} bar(s) max)', f'{(d[mm] <= 6).mean():.3f}', f'{int(mm.sum())} states')
m = pop.drm_mask(4, 4)
for a in ['00', '10', '21', '32', '42', '11', '31', '20', '22']:
    mm = m & (F['carm'] == int(a[0])) & (F['earm'] == int(a[1])) & (F['pairs'] == 2)
    b = mm & (F['edges_paired'] == 1); s = mm & (F['edges_paired'] == 2)
    if b.sum() and s.sum(): put('bars', f'4c4e ARM {a}, 2 pairs: as a bar / on both edges', f'{(d[b] <= 6).mean():.3f} / {(d[s] <= 6).mean():.3f}', f'{int(b.sum())} / {int(s.sum())} states')
# JTuu T4332: when is ARM most informative (share of the target entropy explained by ARM, per DRM)
for drm in pop.DRMS_NAMED:
    m = pop.drm_mask(*drm); y = (d[m] <= 6).mean()
    hy = -(y * math.log2(y) + (1 - y) * math.log2(1 - y)) if 0 < y < 1 else 0
    mi_a = info(m, ARM)[0]; mi_p = info(m, ['pairs'])[0]; mi_ap = info(m, ARM + ['pairs'])[0]
    put('T4332 JTuu / T8206 eff', f'{pop.drm_name(*drm)}: entropy of sub-7 {hy:.3f} bits; explained by ARM / pairs / both', f'{mi_a / hy:.3f} / {mi_p / hy:.3f} / {mi_ap / hy:.3f}', f'p(sub-7) {y:.3f}')
# Zagros T11345: corners not in a pair vs pairs, across DRMs (pooled over the named DRMs, without conditioning on DRM)
mm = np.zeros(len(d), bool)
for drm in pop.DRMS_NAMED: mm |= pop.drm_mask(*drm)
for f in ['pairs', 'unpaired_corners', 'unpaired_edges', 'pairs_minus_udbad']:
    put('T11345 Zagros / rodneykinney', f'all named DRMs pooled, without the DRM: {f}', f'MI {info(mm, [f])[0]:.4f} bits; with the DRM known: {info(mm, ["drm_c", "drm_e", f])[0] - info(mm, ["drm_c", "drm_e"])[0]:.4f} added')
# tseitsei T9334: good 1-pair 4c4e cases; caycala D11050; FakeMMAP D12097 (0 pairs)
m1 = pop.drm_mask(4, 4) & (F['pairs'] == 1)
best = []
for f in search.CHEAP:
    for g in search.CHEAP:
        if g <= f: continue
        mi_, st, po, n, pos, p = info(m1, [f, g])
        hi = p > 0.5
        best.append((pos[hi].sum() / pos.sum(), n[hi].sum() / n.sum(), f, g))
best.sort(reverse=True)
for r in best[:3]: put('T9334 tseitsei89', f'4c4e with 1 pair: cells over 50% by {r[2]} + {r[3]}', f'hold {r[0]:.3f} of the sub-7 1-pair states, {r[1]:.3f} of the 1-pair states')
m = pop.drm_mask(4, 4) & (F['carm'] == 2) & (F['earm'] == 1) & (F['pairs'] == 0)
for sp in sorted(set(F['side'][m].tolist())):
    mm = m & (F['side'] == sp); put('D11050 caycala', f'4c4e ARM 21, 0 pairs, {sp} side pair(s)', f'{(d[mm] <= 6).mean():.3f}', f'{int(mm.sum())} states')
m0 = pop.drm_mask(4, 4) & (F['pairs'] == 0)
for a in sorted(set((F['carm'][m0] * 10 + F['earm'][m0]).tolist())):
    mm = m0 & (F['carm'] * 10 + F['earm'] == a)
    put('D12097 FakeMMAP', f'4c4e, 0 pairs, ARM {a:02d}', f'{(d[mm] <= 6).mean():.3f}', f'{int(mm.sum())} states')
# both axes independent? (caycala D14218, Daichi D14220)
T = pop.targets(6); prl = T['p_rl']; pud = (d <= 6).astype(float)
for drm in [(4, 4), (4, 2), (3, 2), (7, 8), None]:
    m = np.ones(len(d), bool) if drm is None else pop.drm_mask(*drm)
    both = (pud[m] * prl[m]).mean(); a = pud[m].mean(); b = prl[m].mean()
    put('D14218 caycala / D14220 Daichi', f'{"all states" if drm is None else pop.drm_name(*drm)} (DRM of the U/D axis): P(U/D <= 6), P(R/L <= 6), P(both), independence would give', f'{a:.4f}, {b:.4f}, {both:.4f}, {a * b:.4f}; better of two {T["two"][m].mean():.4f} vs 1-(1-a)(1-b) {1 - (1 - a) * (1 - b):.4f}')
open(os.path.join(pop.OUT, 'q4.tsv'), 'w').write('question\twhat\tanswer\tsize\n' + '\n'.join(L) + '\n')
