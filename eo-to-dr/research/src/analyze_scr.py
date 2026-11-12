#!/usr/bin/env python3
"""Questions A1-A3 and B4 from the per-scramble table of `eodrtools scr`.

usage: analyze_scr.py <scr.tsv> <tag>        writes out/<tag>_a1.tsv, _a1_counts.tsv, _a2.tsv, _a3.tsv, _b4.tsv, _stats.json

Conventions (see README): lengths in face turns (HTM); "normal" = moves after the scramble, "inverse" = after the
inverse scramble, NISS = moves on both sides.  An EO counts once per canonical move sequence that solves it for the
first time at its end (the convention of `nissy solve eo* -a`); for NISS EOs each side ends in a quarter turn of the
EO axis.  A route through an EO: that EO, then turns keeping it (no quarter turns of its axis) to a DR on one of the
two other axes; on the normal side for normal EOs, on the inverse side for inverse EOs, on either side for NISS EOs."""
import csv, json, os, sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, '..', 'out')
AX = ['RL', 'UD', 'FB']
K = 6
csv.field_size_limit(10**7)

def load(path):
    rows = list(csv.DictReader(open(path), delimiter='\t'))
    num = {}
    for key in rows[0]:
        try:
            num[key] = np.array([int(r[key]) for r in rows])
        except ValueError:
            pass
    return rows, num

def dist_row(name, v, maxlen=13, extra=None):
    v = np.asarray(v)
    n = len(v)
    h = [int((v == d).sum()) for d in range(maxlen)]
    row = {'what': name, 'n': n, 'mean': round(float(v.mean()), 4),
           'p_le8': round(float((v <= 8).mean()), 5), 'p_le9': round(float((v <= 9).mean()), 5),
           'p_le10': round(float((v <= 10).mean()), 5), 'max': int(v.max())}
    for d in range(maxlen):
        row[f'n{d}'] = h[d]
    if extra:
        row.update(extra)
    return row

def write(path, rows):
    keys = []
    for r in rows:
        for k in r:
            if k not in keys:
                keys.append(k)
    with open(path, 'w') as f:
        f.write('\t'.join(keys) + '\n')
        for r in rows:
            f.write('\t'.join(str(r.get(k, '')) for k in keys) + '\n')

def main(path, tag):
    rows, c = load(path)
    n = len(rows)
    dn = np.stack([c[f'd_n_{a}'] for a in AX], 1)
    di = np.stack([c[f'd_i_{a}'] for a in AX], 1)
    dlin = dn.min(1)
    d6 = np.minimum(dn.min(1), di.min(1))
    dniss = c['dniss']
    stats = {'n': n}
    # ---------------- A1
    a1 = []
    # exact fixed-axis distribution: the all_dr table histogram (2,217,093,120 cosets, each equally likely)
    hist = [int(l.split()[1]) for l in open('/data/fmc/is-dr-xs-worth-it/research/out/bfs/all_dr.hist') if l[0].isdigit() and len(l.split()) == 2]
    tot = sum(hist)
    ex = {'what': 'fixed axis, exact (all 2,217,093,120 cosets)', 'n': tot,
          'mean': round(sum(d * h for d, h in enumerate(hist)) / tot, 4),
          'p_le8': round(sum(hist[:9]) / tot, 5), 'p_le9': round(sum(hist[:10]) / tot, 5), 'p_le10': round(sum(hist[:11]) / tot, 5),
          'max': len(hist) - 1}
    for d in range(13):
        ex[f'n{d}'] = hist[d] if d < len(hist) else 0
    a1.append(ex)
    a1.append(dist_row('fixed axis (U/D), sampled', dn[:, 1]))
    a1.append(dist_row('fixed axis, all three axes pooled, sampled', dn.reshape(-1)))
    a1.append(dist_row('best of 3 axes, normal (linear)', dlin))
    a1.append(dist_row('best of 3 axes, inverse (linear)', di.min(1)))
    a1.append(dist_row('best of 6 (3 axes x normal/inverse, linear)', d6))
    a1.append(dist_row('NISS (moves on both sides), best of 3 axes', dniss))
    write(os.path.join(OUT, f'{tag}_a1.tsv'), a1)
    stats['a1'] = {r['what']: {k: r[k] for k in ('mean', 'p_le8', 'p_le9', 'p_le10', 'max')} for r in a1}
    stats['a1']['niss_gain_over_6'] = {str(g): int(((d6 - dniss) == g).sum()) for g in range(0, 4)}
    stats['a1']['lin_gain_6_over_3'] = {str(g): int(((dlin - d6) == g).sum()) for g in range(0, 4)}
    # number of DR solutions of each length (normal side, 3 axes; canonical sequences reaching DR first at their end)
    cap = max(int(k.split('_')[2]) for k in c if k.startswith('ndr_UD_'))
    cnt = {L: sum(c[f'ndr_{a}_{L}'] for a in AX) for L in range(cap + 1)}
    a1c = []
    for L in range(6, cap + 1):
        v = cnt[L]
        cum = sum(cnt[l] for l in range(L + 1))
        a1c.append({'length': L, 'mean_dr_solutions': round(float(v.mean()), 3), 'median': float(np.median(v)),
                    'p_at_least_one': round(float((v > 0).mean()), 5), 'p90': float(np.percentile(v, 90)), 'max': int(v.max()),
                    'mean_up_to_L': round(float(cum.mean()), 3), 'median_up_to_L': float(np.median(cum)),
                    'fixed_axis_mean (U/D)': round(float(c[f'ndr_UD_{L}'].mean()), 3)})
    nopt = c['nopt']
    a1c.append({'length': 'optimal', 'mean_dr_solutions': round(float(nopt.mean()), 3), 'median': float(np.median(nopt)),
                'p_at_least_one': 1.0, 'p90': float(np.percentile(nopt, 90)), 'max': int(nopt.max()),
                'p_at_most_2 (one, up to the last turn\'s direction)': round(float((nopt <= 2).mean()), 5)})
    write(os.path.join(OUT, f'{tag}_a1_counts.tsv'), a1c)
    # ---------------- A2
    best = {kind: np.stack([np.stack([c[f'best_{kind}_{y}_{k}'] for k in range(K + 1)], 1) for y in AX], 1) for kind in 'nix'}
    # [scramble, axis, k] -> over axes
    bn = best['n'].min(1)
    bb = np.minimum(best['n'], best['i']).min(1)
    bx = np.minimum(np.minimum(best['n'], best['i']), best['x']).min(1)
    brk = np.stack([np.stack([c[f'brk_{y}_{k}'] for k in range(K + 1)], 1) for y in AX], 1).min(1)
    estar = c['estar']
    a2 = []
    for kname, b, ref, refname in (('normal EOs, DR on normal', bn, dlin, 'optimal normal DR'),
                                   ('normal or inverse EOs, DR on the same side', bb, d6, 'optimal DR, best of 6'),
                                   ('normal, inverse and NISS EOs, NISS DR side rule', bx, dniss, 'optimal NISS DR'),
                                   ('normal, inverse and NISS EOs, against the best of 6', bx, d6, 'optimal DR, best of 6')):
        for k in range(K + 1):
            v = b[:, k]
            has = v < 99
            loss = (v - ref)[has]
            r = {'eo_kind': kname, 'reference': refname, 'k': k, 'p_has_eo': round(float(has.mean()), 5),
                 'mean_best_given_eo': round(float(v[has].mean()), 4) if has.any() else '',
                 'p_equals_optimal': round(float((v == ref).mean()), 5),
                 'mean_loss_given_eo': round(float(loss.mean()), 4) if has.any() else '',
                 'p_loss0': round(float((loss == 0).sum() / n), 5), 'p_loss1': round(float((loss == 1).sum() / n), 5),
                 'p_loss2': round(float((loss == 2).sum() / n), 5), 'p_loss3plus': round(float((loss >= 3).sum() / n), 5),
                 'p_better_than_optimal_ref': round(float((loss < 0).sum() / n), 5)}
            if kname.startswith('normal EOs'):
                r['p_estar_le_k'] = round(float((estar <= k).mean()), 5)
                bk = brk[:, k]
                r['p_any_turns_after_eo_equals_optimal'] = round(float((bk == ref).mean()), 5)
                r['p_needs_eo_breaking'] = round(float(((bk == ref) & (v > ref)).mean()), 5)
                r['mean_best_any_turns_after_eo'] = round(float(bk[bk < 99].mean()), 4) if (bk < 99).any() else ''
            a2.append(r)
    write(os.path.join(OUT, f'{tag}_a2.tsv'), a2)
    stats['estar_hist'] = {str(e): int((estar == e).sum()) for e in range(int(estar.max()) + 1)}
    stats['estar_mean'] = round(float(estar.mean()), 4)
    # ---------------- A3
    a3 = []
    for kname, kinds in (('normal', 'n'), ('normal + inverse', 'ni'), ('normal + inverse + NISS', 'nix')):
        for scope in ('one axis (F/B)', 'all three axes'):
            ys = ['FB'] if scope.startswith('one') else AX
            for k in (4, 5):
                neo = sum(c[f'neo_{kd}_{y}_{l}'] for kd in kinds for y in ys for l in range(k + 1))
                for N in (9, 10, 11, 12):
                    p = sum(c[f'pairs_{kd}_{y}_{k}_{N}'] for kd in kinds for y in ys)
                    a3.append({'eos': kname, 'axes': scope, 'eo_max': k, 'dr_total_max': N, 'mean_pairs': round(float(p.mean()), 3),
                               'median_pairs': float(np.median(p)), 'p_none': round(float((p == 0).mean()), 5),
                               'p10': float(np.percentile(p, 10)), 'p90': float(np.percentile(p, 90)),
                               'mean_eos': round(float(neo.mean()), 3), 'pairs_per_eo': round(float(p.sum() / max(neo.sum(), 1)), 5)})
    write(os.path.join(OUT, f'{tag}_a3.tsv'), a3)
    # per-EO yield of exactly-4 and exactly-5 EOs, and the gains
    g = {}
    for kname, kinds in (('normal', 'n'), ('nix', 'nix')):
        for N in (9, 10, 11, 12):
            p4 = sum(c[f'pairs_{kd}_{y}_4_{N}'] for kd in kinds for y in AX)
            p5 = sum(c[f'pairs_{kd}_{y}_5_{N}'] for kd in kinds for y in AX)
            e4 = sum(c[f'neo_{kd}_{y}_{l}'] for kd in kinds for y in AX for l in range(5))
            e5 = sum(c[f'neo_{kd}_{y}_5'] for kd in kinds for y in AX)
            g[f'{kname}_N{N}'] = {'drs_per_eo_le4': round(float(p4.sum() / e4.sum()), 5),
                                  'drs_per_5move_eo': round(float((p5 - p4).sum() / e5.sum()), 5),
                                  'mean_drs_from_le4_eos': round(float(p4.mean()), 3), 'mean_drs_from_5move_eos': round(float((p5 - p4).mean()), 3),
                                  'mean_le4_eos': round(float(e4.mean()), 2), 'mean_5move_eos': round(float(e5.mean()), 2)}
    for kname, b in (('normal', bn), ('normal_inverse', bb), ('nix', bx)):
        d45 = (b[:, 4] - b[:, 5])
        g[f'gain_5_over_4_{kname}'] = {'p_no_eo_le4': round(float((b[:, 4] >= 99).mean()), 5),
                                       'p_improves_given_eo_le4': round(float((d45[b[:, 4] < 99] > 0).mean()), 5),
                                       'mean_gain_given_eo_le4': round(float(d45[b[:, 4] < 99].mean()), 4),
                                       'mean_best_le4_given_eo': round(float(b[b[:, 4] < 99, 4].mean()), 4),
                                       'mean_best_le5': round(float(b[b[:, 5] < 99, 5].mean()), 4)}
    for kname, arr in (('normal', best['n']), ('nix', np.minimum(np.minimum(best['n'], best['i']), best['x']))):
        for k in (4, 5, 6):
            fixed = arr[:, 2, k]          # F/B only
            allax = arr[:, :, k].min(1)
            ok = fixed < 99
            g[f'gain_other_axes_{kname}_k{k}'] = {'p_fixed_axis_has_eo': round(float(ok.mean()), 5),
                                                 'mean_fixed_given_eo': round(float(fixed[ok].mean()), 4),
                                                 'mean_all_axes_same_scrambles': round(float(allax[ok].mean()), 4),
                                                 'p_other_axes_better': round(float((allax[ok] < fixed[ok]).mean()), 5),
                                                 'mean_all_axes': round(float(allax[allax < 99].mean()), 4)}
    stats['a3_gains'] = g
    # ---------------- B4
    b4 = []
    for kname, kinds in (('linear (normal)', 'n'), ('normal or inverse (linear)', 'ni'), ('NISS (normal, inverse, both)', 'nix')):
        for scope in ('one axis (F/B)', 'all three axes'):
            ys = ['FB'] if scope.startswith('one') else AX
            for L in range(K + 1):
                v = sum(c[f'neo_{kd}_{y}_{L}'] for kd in kinds for y in ys)
                cum = sum(c[f'neo_{kd}_{y}_{l}'] for kd in kinds for y in ys for l in range(L + 1))
                b4.append({'eos': kname, 'axes': scope, 'length': L, 'mean': round(float(v.mean()), 3), 'median': float(np.median(v)),
                           'p_at_least_one': round(float((v > 0).mean()), 5), 'min': int(v.min()), 'max': int(v.max()),
                           'mean_le': round(float(cum.mean()), 3), 'median_le': float(np.median(cum)), 'p_none_le': round(float((cum == 0).mean()), 5),
                           'min_le': int(cum.min()), 'max_le': int(cum.max()), 'p10_le': float(np.percentile(cum, 10)), 'p90_le': float(np.percentile(cum, 90))})
    write(os.path.join(OUT, f'{tag}_b4.tsv'), b4)
    eoopt = {kind: np.stack([c[f'eoopt_{kind}_{y}'] for y in AX], 1) for kind in 'nix'}
    stats['eo_optimal'] = {
        'fixed_axis_linear_mean': round(float(eoopt['n'][:, 2].mean()), 4),
        'any_axis_linear_mean': round(float(eoopt['n'].min(1).mean()), 4),
        'any_axis_lin_or_inv_mean': round(float(np.minimum(eoopt['n'], eoopt['i']).min(1).mean()), 4),
        'any_axis_niss_mean': round(float(eoopt['x'].min(1).mean()), 4),
        'any_axis_niss_hist': {str(d): int((eoopt['x'].min(1) == d).sum()) for d in range(8)},
        'any_axis_linear_hist': {str(d): int((eoopt['n'].min(1) == d).sum()) for d in range(8)},
        'any_axis_lin_or_inv_hist': {str(d): int((np.minimum(eoopt['n'], eoopt['i']).min(1) == d).sum()) for d in range(8)},
    }
    # S-EO-87: an N-move EO but no (N+1)-move EO (all axes); S-EO-88: more 3-move than 4-move EOs
    for kname, kinds in (('linear', 'n'), ('niss', 'nix')):
        cntL = {L: sum(c[f'neo_{kd}_{y}_{L}'] for kd in kinds for y in AX) for L in range(K + 1)}
        stats[f'gap_{kname}'] = {f'{L}_but_no_{L+1}': round(float(((cntL[L] > 0) & (cntL[L + 1] == 0)).mean()), 5) for L in range(1, K)}
        stats[f'more3than4_{kname}'] = round(float((cntL[3] > cntL[4]).mean()), 5)
    json.dump(stats, open(os.path.join(OUT, f'{tag}_stats.json'), 'w'), indent=1)
    print(f'{tag}: {n} scrambles analysed')

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
