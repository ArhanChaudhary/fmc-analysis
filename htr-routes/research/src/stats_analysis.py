#!/usr/bin/env python3
"""Questions 3 and 4 and the per-state parts of 5, from the per-state columns of out/big/run1/states_*.tsv, and the
cell-by-cell comparisons with doc 15 (HTR Subset Stats), doc 66 (Extra Quarter-Turn Stats) and doc 9 (DR Finish
Move Counts).

Per-state columns used (htrtools routes):
  d, dvar        optimal finish of X and of X*R2 (last DR move turned the other way)
  htrN, htrI     shortest linear DR->HTR on normal / inverse;  htrNiss  shortest NISS HTR (exact, IDA*)
  best_lin_n/_i  shortest HTR among the linear normal / inverse readings of all optimal finishes
  best_any       shortest HTR among all NISS readings of all optimal finishes; best_any1 the same for <= opt+1
  mask_lin/_any  bit L set = some optimal finish has a linear / any reading whose HTR has L moves
  qmin, qmax     fewest / most quarter turns in an optimal finish; ccqt = the corner subset's quarter-turn count;
  qtfull         fewest quarter turns of any sequence reaching HTR (corners and edges)
  ht_first_n/_i  fewest moves (all half turns) before the first quarter turn of an optimal finish, read on normal /
                 on inverse (= after its last quarter turn)
  lsd, ls_qmin, ls_qmax   optimal leave-slice finish (E slice ignored) and its fewest / most quarter turns
Groups are weighted by exact subset sizes when pooled.
Outputs: out/q3_htr.tsv, out/q4_qt.tsv, out/q5_states.tsv, out/compare_doc15.tsv, out/compare_doc66.tsv,
out/compare_doc9.tsv"""
import csv, collections, os, re
import numpy as np
from common import *

ST = {s: load_states(s) for s in SUBS}
def groups():
    for s in SUBS: yield s, [s]
    for g in CGROUPS: yield g, [s for s in SUBS if CORNER(s) == g]
    yield 'all', SUBS
def cat(subs, f):
    v = np.concatenate([f(ST[s]) for s in subs]).astype(float)
    w = np.concatenate([np.full(len(ST[s]['d']), SIZE[s] / len(ST[s]['d'])) for s in subs])
    return v, w
def mean(subs, f):
    v, w = cat(subs, f); return float((v * w).sum() / w.sum())
bit = lambda m, L: (m >> L) & 1

def q3():
    cols = [
        ('mean_opt', lambda t: t['d']),
        ('mean_htr_normal', lambda t: t['htrN']), ('mean_htr_inverse', lambda t: t['htrI']),
        ('mean_htr_linear_best_side', lambda t: np.minimum(t['htrN'], t['htrI'])),
        ('mean_htr_niss', lambda t: t['htrNiss']),
        # T624: linear vs NISS, normal vs inverse
        ('niss_eq_linear', lambda t: np.minimum(t['htrN'], t['htrI']) == t['htrNiss']),
        ('niss_shorter_by_1', lambda t: np.minimum(t['htrN'], t['htrI']) - t['htrNiss'] == 1),
        ('niss_shorter_by_2plus', lambda t: np.minimum(t['htrN'], t['htrI']) - t['htrNiss'] >= 2),
        ('normal_eq_inverse', lambda t: t['htrN'] == t['htrI']),
        ('normal_inverse_differ_by_2plus', lambda t: abs(t['htrN'] - t['htrI']) >= 2),
        # does an optimal finish use a shortest HTR?
        ('opt_uses_shortest_linear_on_its_side', lambda t: (t['best_lin_n'] == t['htrN']) | (t['best_lin_i'] == t['htrI'])),
        ('opt_uses_linear_of_best_side_length', lambda t: np.minimum(t['best_lin_n'], t['best_lin_i']) == np.minimum(t['htrN'], t['htrI'])),
        ('opt_uses_shortest_niss', lambda t: t['best_any'] == t['htrNiss']),
        ('opt_htr_plus1', lambda t: t['best_any'] - t['htrNiss'] == 1),
        ('opt_htr_plus2', lambda t: t['best_any'] - t['htrNiss'] == 2),
        ('opt_htr_plus3more', lambda t: t['best_any'] - t['htrNiss'] >= 3),
        ('p1_uses_shortest_niss', lambda t: t['best_any1'] == t['htrNiss']),
        ('mean_shortest_htr_in_an_optimal', lambda t: t['best_any']),
        ('mean_post_htr_longest_in_an_optimal', lambda t: t['d'] - t['best_any']),
        ('mean_opt_minus_leave_slice', lambda t: t['d'] - t['lsd']),
        # 9-move HTRs
        ('some_opt_uses_htr_ge9', lambda t: (t['mask_any'] >> 9) > 0),
        ('every_opt_htr_ge9', lambda t: t['best_any'] >= 9),
        ('niss_htr_ge9', lambda t: t['htrNiss'] >= 9),
        ('linear_htr_ge9', lambda t: np.minimum(t['htrN'], t['htrI']) >= 9),
    ]
    with open(f'{OUT}/q3_htr.tsv', 'w') as f:
        f.write('group\tn\t' + '\t'.join(c for c, _ in cols) + '\n')
        for g, subs in groups():
            n = sum(len(ST[s]['d']) for s in subs)
            f.write(f'{g}\t{n}\t' + '\t'.join(f'{mean(subs, fn):.9f}' for _, fn in cols) + '\n')
    # "does an L-move HTR give an optimal": among states whose shortest NISS (resp. linear) HTR is L,
    # share where some optimal finish uses an HTR of exactly L moves (resp. a linear one)
    with open(f'{OUT}/q3_htr_by_length.tsv', 'w') as f:
        f.write('group\tL\tstates_share_with_shortest_niss_L\topt_uses_an_L_move_htr\tstates_share_with_shortest_linear_L\topt_uses_a_linear_L_move_htr\n')
        for g, subs in groups():
            if g not in ('all',) and g not in CGROUPS: continue
            for L in range(3, 14):
                v1, w = cat(subs, lambda t: t['htrNiss'] == L)
                u1, _ = cat(subs, lambda t: (t['htrNiss'] == L) & (bit(t['mask_any'], L) == 1))
                v2, _ = cat(subs, lambda t: np.minimum(t['htrN'], t['htrI']) == L)
                u2, _ = cat(subs, lambda t: (np.minimum(t['htrN'], t['htrI']) == L) & (bit(t['mask_lin'], L) == 1))
                a, b, c, d = (v1 * w).sum(), (u1 * w).sum(), (v2 * w).sum(), (u2 * w).sum()
                if a + c == 0: continue
                f.write(f'{g}\t{L}\t{a / w.sum():.4f}\t{(b / a if a else float("nan")):.4f}\t{c / w.sum():.4f}\t{(d / c if c else float("nan")):.4f}\n')

def q4():
    cols = [
        ('mean_ccqt', lambda t: t['ccqt']),
        ('every_opt_extra_qt_vs_corners', lambda t: t['qmin'] > t['ccqt']),
        ('some_opt_extra_qt_vs_corners', lambda t: t['qmax'] > t['ccqt']),
        ('every_opt_extra_qt_vs_htr_min', lambda t: t['qmin'] > t['qtfull']),
        ('some_opt_extra_qt_vs_htr_min', lambda t: t['qmax'] > t['qtfull']),
        ('ls_every_opt_extra_qt_vs_corners', lambda t: t['ls_qmin'] > t['ccqt']),
        ('ls_some_opt_extra_qt_vs_corners', lambda t: t['ls_qmax'] > t['ccqt']),
        ('mean_min_qt_opt', lambda t: t['qmin']), ('mean_min_qt_ls', lambda t: t['ls_qmin']),
        ('every_opt_plus4_vs_corners', lambda t: t['qmin'] >= t['ccqt'] + 4),
        ('mean_opt', lambda t: t['d']), ('mean_ls', lambda t: t['lsd']),
        ('ht_before_first_qt_lt2_normal', lambda t: t['ht_first_n'] < 2),
        ('ht_before_first_qt_lt2_either_side', lambda t: np.minimum(t['ht_first_n'], t['ht_first_i']) < 2),
        ('ht_before_first_qt_ge3_either_side', lambda t: np.minimum(t['ht_first_n'], t['ht_first_i']) >= 3),
        ('mean_ht_before_first_qt_either_side', lambda t: np.minimum(t['ht_first_n'], t['ht_first_i'])),
    ]
    with open(f'{OUT}/q4_qt.tsv', 'w') as f:
        f.write('group\tn\t' + '\t'.join(c for c, _ in cols) + '\n')
        for g, subs in groups():
            n = sum(len(ST[s]['d']) for s in subs)
            f.write(f'{g}\t{n}\t' + '\t'.join(f'{mean(subs, fn):.9f}' for _, fn in cols) + '\n')

def q5():
    cols = [
        ('mean_opt', lambda t: t['d']),
        ('mean_opt_with_variation', lambda t: np.minimum(t['d'], t['dvar'])),
        ('mean_gain', lambda t: t['d'] - np.minimum(t['d'], t['dvar'])),
        ('share_variation_shorter', lambda t: t['dvar'] < t['d']),
        ('share_variation_equal', lambda t: t['dvar'] == t['d']),
        ('share_ge15', lambda t: t['d'] >= 15), ('share_ge15_with_variation', lambda t: np.minimum(t['d'], t['dvar']) >= 15),
        ('share_16', lambda t: t['d'] >= 16), ('share_16_with_variation', lambda t: np.minimum(t['d'], t['dvar']) >= 16),
        ('qt_break_minus_opt', lambda t: 1 + np.minimum(t['d'], t['dvar']) - t['d']),
    ]
    with open(f'{OUT}/q5_states.tsv', 'w') as f:
        f.write('group\tn\t' + '\t'.join(c for c, _ in cols) + '\n')
        for g, subs in groups():
            n = sum(len(ST[s]['d']) for s in subs)
            f.write(f'{g}\t{n}\t' + '\t'.join(f'{mean(subs, fn):.9f}' for _, fn in cols) + '\n')

def name_map():
    m = {}
    for r in csv.DictReader(open(f'{OUT}/name_map.tsv'), delimiter='\t'):
        m[(r['doc'], r['label'])] = r['our_subset']
    return m

def exact_mean_opt(sub):
    tot = n = 0
    for r in csv.DictReader(open(f'{R}/out/checks/dist48.tsv'), delimiter='\t'):
        if r['subset'] == sub: tot += int(r['depth']) * int(r['states']); n += int(r['states'])
    return tot / n

def doc15():
    nm = name_map()
    with open(f'{OUT}/compare_doc15.tsv', 'w') as f:
        f.write('doc15_label\tour_subset\tdoc_solution_mean\texact_mean_opt\tdoc_no_e_mean\tour_mean_leave_slice\t'
                'doc_linear_htr_mean\tour_linear_htr_best_side\tour_linear_htr_normal\tdoc_niss_htr_mean\tour_niss_htr\n')
        for r in csv.reader(open('/data/fmc/kb/docs/gsheet/17iChOoeB205t3wHTXMLrjM9si2vtxRgFeYR2z3pn1i0/Notes.csv')):
            if len(r) > 6 and ('doc15', r[1].strip()) in nm:
                s = nm[('doc15', r[1].strip())]; t = ST[s]
                f.write(f'{r[1].strip()}\t{s}\t{r[2]}\t{exact_mean_opt(s):.3f}\t{r[4]}\t{t["lsd"].mean():.3f}\t{r[5]}\t'
                        f'{np.minimum(t["htrN"], t["htrI"]).mean():.3f}\t{t["htrN"].mean():.3f}\t{r[6]}\t{t["htrNiss"].mean():.3f}\n')

def doc66():
    nm = name_map()
    with open(f'{OUT}/compare_doc66.tsv', 'w') as f:
        f.write('doc66_label\tour_subset\tdoc_pct_extra_qt\tour_ls_every_opt_extra\tour_ls_some_opt_extra\tour_full_every_opt_extra\t'
                'doc_avg_moves_with_extra\tour_mean_leave_slice\tdoc_probability\texact_probability\tdoc_DRs_checked\n')
        for r in csv.reader(open('/data/fmc/kb/docs/gsheet/1fPCjS1ZQlP_Munut9MQkSbsL3CEdtT3LC5h3R8OMHGw/No_Sorting.csv')):
            if len(r) > 12 and ('doc66', r[1].strip()) in nm:
                s = nm[('doc66', r[1].strip())]; t = ST[s]
                f.write(f'{r[1].strip()}\t{s}\t{r[6]}\t{(t["ls_qmin"] > t["ccqt"]).mean():.4f}\t{(t["ls_qmax"] > t["ccqt"]).mean():.4f}\t'
                        f'{(t["qmin"] > t["ccqt"]).mean():.4f}\t{r[8]}\t{t["lsd"].mean():.3f}\t{r[11]}\t{SIZE[s] / 19508428800:.6f}\t{r[12]}\n')

# ---- doc 9: corner quarter turns = fewest quarter turns of a corner solution, in the first study's move maps
MAPS = {0: [1, 2, 3, 0, 4, 5, 6, 7], 3: [0, 1, 2, 3, 7, 4, 5, 6], 6: [7, 1, 2, 4, 3, 5, 6, 0],
        7: [0, 6, 5, 3, 4, 2, 1, 7], 8: [5, 4, 2, 3, 1, 0, 6, 7], 9: [0, 1, 7, 6, 4, 5, 3, 2]}
def corner_moves():
    def ap(p, t):
        r = [0] * 8
        for i in range(8): r[t[i]] = p[i]
        return tuple(r)
    mv = {}
    for m, t in MAPS.items():
        mv[m] = t
    full = []
    for m in range(10):
        base = {0: 0, 1: 0, 2: 0, 3: 3, 4: 3, 5: 3}.get(m, m); times = {1: 2, 2: 3, 4: 2, 5: 3}.get(m, 1)
        full.append((base, times, m in (0, 2, 3, 5)))
    def apply(p, m):
        base, times, _ = full[m]
        for _ in range(times): p = ap(p, MAPS[base])
        return p
    return apply, [f[2] for f in full]
def rank(p):
    import math
    r = 0; n = len(p)
    for i in range(n):
        r += sum(1 for x in p[i + 1:] if x < p[i]) * math.factorial(n - 1 - i)
    return r
def corner_solve_qt():
    import collections
    apply, isqt = corner_moves()
    dist = {tuple(range(8)): 0}; dq = collections.deque([tuple(range(8))])
    while dq:
        x = dq.popleft()
        for m in range(10):
            y = apply(x, m); w = 1 if isqt[m] else 0
            if y not in dist or dist[x] + w < dist[y]:
                dist[y] = dist[x] + w
                (dq.append if w else dq.appendleft)(y)
    out = np.zeros(40320, int)
    for p, d in dist.items(): out[rank(p)] = d
    return out
def doc9():
    cq = corner_solve_qt()
    allc = collections.Counter(cq)
    v = {s: cq[ST[s]['c']] for s in SUBS}
    lines = ['quantity\tdoc9\tours\tnote']
    tot = sum(allc.values())
    for lab, sel, doc in (('P(corner QTs <= 2)', lambda q: q <= 2, 0.171), ('P(corner QTs = 3)', lambda q: q == 3, 0.275),
                          ('P(corner QTs = 4)', lambda q: q == 4, 0.329), ('P(corner QTs = 5)', lambda q: q == 5, 0.225)):
        ours = sum(c for q, c in allc.items() if sel(q)) / tot
        lines.append(f'{lab}\t{doc}\t{ours:.4f}\texact over the 40320 corner permutations (every one holds the same number of DR states)')
    d = np.concatenate([ST[s]['d'] for s in SUBS]); w = np.concatenate([np.full(len(ST[s]['d']), SIZE[s] / len(ST[s]['d'])) for s in SUBS])
    q = np.concatenate([v[s] for s in SUBS])
    qmin = np.concatenate([ST[s]['qmin'] for s in SUBS]); qmax = np.concatenate([ST[s]['qmax'] for s in SUBS])
    def wq(x, ww, p):
        o = np.argsort(x); c = np.cumsum(ww[o]) / ww.sum(); return x[o][np.searchsorted(c, p)]
    for cqv, med in ((2, 13.3), (3, 13.7), (4, 14.4), (5, 14.8)):
        m = (q <= 2) if cqv == 2 else (q == cqv)
        lines.append(f'median optimal, corner QTs {"<=2" if cqv == 2 else cqv}\t{med}\t{wq(d[m], w[m], 0.5)}\tdoc 9 medians are interpolated on a 10k sample')
        if cqv in (2, 3, 4):
            m2 = q == cqv
            docv = {2: (0.3723, 0.5730, 0.0546), 3: (0.6237, 0.3591, 0.0172), 4: (0.7726, 0.2265, 0.0009)}[cqv]
            for (k, lab), dv in zip(((0, '+0'), (2, '+2'), (4, '+4 or more')), docv):
                if k < 4:
                    every = ((qmin - q == k) & m2); some = ((qmax - q == k) & m2)
                else:
                    every = ((qmin - q >= 4) & m2); some = ((qmax - q >= 4) & m2)
                lines.append(f'corner QTs {cqv}: additional qts {lab}\t{dv}\t{(w[every].sum() / w[m2].sum()):.4f} (fewest-qt optimal) / '
                             f'{(w[some].sum() / w[m2].sum()):.4f} (most-qt optimal)\tdoc 9: one optimal per state')
    open(f'{OUT}/compare_doc9.tsv', 'w').write('\n'.join(lines) + '\n')

if __name__ == '__main__':
    q3(); q4(); q5(); doc15(); doc66(); doc9()
    print('done')
