#!/usr/bin/env python3
"""Step 4b: search small rules per DRM.  A rule = the cross-table of 1, 2 or 3 human-readable features (of the state
after the switch); each cell is labelled 'switch' (p(DR <= 6) > 0.5), 'discard' (< 0.1) or 'check' (between).
  strict separation = share of states in cells that are themselves in a band (every reading of the rule is a verdict)
  pooled separation = cells taken in order of p into a switch group (pooled p > 0.5) and a discard group (pooled
                      p < 0.1), as large as possible; the rest 'check'
Ranked on P1 (exact, uniform = the switched state after any RZP for every DRM but 6cXe/8cXe, see populations.py),
then held out on P2_5 (exact) and P3_5, P3_6 (sampled attempts): a rule 'holds' if every labelled cell keeps its
band in that population (cells with fewer than 200 attempts skipped) and the pooled groups keep theirs.
Output: out/search_<drm>.tsv (all rules), out/search_top.tsv (Pareto front and the best per size), out/feature_value.tsv."""
import os, sys, itertools, math
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import pop
F = pop.feat(); d = F['d'].astype(int); PP = pop.populations()
# feature: (name in feat.npz, how a solver reads it on the switched side, rough cost)
FEATS = [
    ('carm', 'corner ARM (U/D stickers on R/L), read by the axis swap', 'ARM, 2 s'),
    ('earm', 'edge ARM (bad edges in M), axis swap', 'ARM, 2 s'),
    ('carm_fold', 'corner ARM folded min(a, c-a)', 'ARM, 2 s'),
    ('pairs', 'top pairs (pair tracing)', 'trace, 5 s'),
    ('fake', 'fake pairs', 'trace, 5 s'),
    ('side', 'side pairs', 'trace, 5 s'),
    ('edges_paired', 'bad U/D edges with at least one pair', 'trace, 5 s'),
    ('bars', 'bars (edge paired on both sides)', 'trace, 5 s'),
    ('pair_fake_same_edge', 'edges with a pair and a fake pair', 'trace, 5 s'),
    ('unpaired_corners', 'bad corners in no pair', 'trace, 5 s'),
    ('unpaired_edges', 'bad U/D edges in no pair', 'trace, 5 s'),
    ('split_pairs', 'split pairs (wen)', 'trace, 5 s'),
    ('ar_bars', 'AR pairs / AR bars (n_ar)', 'trace, 8 s'),
    ('pairs_plus_half_side_x2', '2 x (pairs + side/2)', 'trace, 5 s'),
    ('corner_case', 'corner orbit case a/b/c/d (4 bad corners)', 'corner trace, 5-10 s'),
    ('case_suffix', 'corner case ARM suffix', 'corner trace, 5-10 s'),
    ('twist_major', 'twist split (larger of cw/ccw count)', 'corner trace, 3 s'),
    ('ud_split', 'bad corners split U/D layers', 'corner trace, 3 s'),
    ('lr_split', 'bad corners split L/R', 'corner trace, 3 s'),
    ('fb_split', 'bad corners split F/B', 'corner trace, 3 s'),
    ('corners_one_layer', 'bad corners all on one U/D layer', 'corner trace, 3 s'),
    ('corners_edges_opposite', 'bad corners on one layer, bad edges on the other', 'trace, 5 s'),
    ('edges_same_slice', 'bad U/D edges all in one slice (M or S)', 'edge trace, 3 s'),
    ('edges_same_layer', 'bad U/D edges all in one layer', 'edge trace, 3 s'),
    ('edges_same_side', 'bad U/D edges on one side face', 'edge trace, 3 s'),
    ('jzp', 'JZP (ARM 0, even corners)', 'ARM, 2 s'),
    ('anti_ar', 'anti-AR (every bad piece out of AR)', 'ARM, 2 s'),
    ('a_one_from_d', '4a one U/D turn from 4d', 'corner trace, 10 s'),
    ('arm_corner_case', 'orbit case of the out-of-AR corners', 'corner trace, 10 s'),
    ('udmoves_to_ar', 'U/D turns to AR (99 = none)', 'mental search, 10 s'),
    ('moves_to_ar', 'moves to AR (EO kept)', 'mental search, 15 s+'),
    ('corner_dist', 'moves to orient the corners (EO kept)', 'mental search, 15 s+'),
    ('fam_4c4e', 'setup turns (U, D, half turns) to an R/L-quarter-turn finish', 'mental search, 15 s+'),
    ('fam_4c2e', 'setup turns to an R h R finish', 'mental search, 15 s+'),
    ('fam_3c2e', 'setup turns to an R U R finish', 'mental search, 15 s+'),
    ('fam_7c8e', 'setup turns to an R U L finish', 'mental search, 15 s+'),
    ('fam_4c6e', 'setup turns to an R h L finish', 'mental search, 15 s+'),
    ('fam_8c8e', 'setup turns to an R L finish', 'mental search, 15 s+'),
]
NAMES = [f[0] for f in FEATS]
CHEAP = [f[0] for f in FEATS if 'mental' not in f[2]]
DRMS = pop.DRMS_NAMED

def codes(x):
    u, inv = np.unique(x, return_inverse=True); return u, inv
def evaluate(key, y, w=None):
    """cells -> (n, positives) using weights w (default 1)."""
    n = np.bincount(key, weights=w); pos = np.bincount(key, weights=(y if w is None else w * y))
    return n, pos
def separation(n, pos):
    tot = n.sum(); ok = n > 0
    p = np.where(ok, pos / np.where(ok, n, 1), np.nan)
    strict = n[ok & ((p < 0.1) | (p > 0.5))].sum() / tot
    # switch group first (cells by p descending, largest prefix with pooled p > 0.5), then the discard group among the
    # remaining cells (by p ascending, largest prefix with pooled p < 0.1)
    order2 = np.argsort(np.where(ok, -p, np.inf)); order2 = order2[ok[order2]]
    cn2 = np.cumsum(n[order2]); cp2 = np.cumsum(pos[order2])
    with np.errstate(invalid='ignore', divide='ignore'): hi = np.where(cp2 / cn2 > 0.5)[0]
    ks = hi.max() + 1 if hi.size else 0
    sw = set(order2[:ks].tolist())
    rest = np.array([i for i in np.argsort(np.where(ok, p, np.inf)) if ok[i] and i not in sw], dtype=np.int64)
    cn = np.cumsum(n[rest]); cp = np.cumsum(pos[rest])
    with np.errstate(invalid='ignore', divide='ignore'): lo = np.where(cp / cn < 0.1)[0]
    kd = lo.max() + 1 if lo.size else 0
    disc = set(rest[:kd].tolist())
    pooled = (n[list(disc)].sum() + n[list(sw)].sum()) / tot
    return strict, pooled, p, disc, sw

def mi(n, pos):
    """Shannon mutual information (bits) between the cell and the target, within the DRM."""
    tot = n.sum(); py = pos.sum() / tot
    h = lambda q: 0.0 if q <= 0 or q >= 1 else -(q * math.log2(q) + (1 - q) * math.log2(1 - q))
    hc = sum(n[i] / tot * h(pos[i] / n[i]) for i in range(len(n)) if n[i] > 0)
    return h(py) - hc

def held_out(key_all, m, p1, disc, sw, popw):
    """Does the labelling keep its bands in another population?  Returns (holds, switch p, discard p, strict sep)."""
    w = popw[m]
    if w.sum() == 0: return None
    n, pos = evaluate(key_all, (d[m] <= 6).astype(float), w)
    n = np.pad(n, (0, len(p1) - len(n))); pos = np.pad(pos, (0, len(p1) - len(pos)))
    ok = True
    attempts = PP is not None
    for i in range(len(p1)):
        if n[i] < (200 if popw is not PP['P1'] else 1): continue
        q = pos[i] / n[i]
        if p1[i] < 0.1 and q >= 0.1: ok = False
        if p1[i] > 0.5 and q <= 0.5: ok = False
    ds, ss = list(disc), list(sw)
    pd_ = pos[ds].sum() / n[ds].sum() if ds and n[ds].sum() else float('nan')
    ps_ = pos[ss].sum() / n[ss].sum() if ss and n[ss].sum() else float('nan')
    if ds and not (pd_ < 0.1): ok = False
    if ss and not (ps_ > 0.5): ok = False
    st = n[[i for i in range(len(p1)) if n[i] > 0 and (pos[i] / n[i] < 0.1 or pos[i] / n[i] > 0.5)]].sum() / n.sum()
    return ok, ps_, pd_, st

def run(drm, feats, maxk=3):
    c, e = drm; m = pop.drm_mask(c, e); y = (d[m] <= 6).astype(float)
    cols = {}
    for f in feats:
        u, inv = codes(F[f][m])
        if len(u) > 1: cols[f] = (u, inv)
    fl = list(cols)
    res = []
    for k in range(1, maxk + 1):
        for combo in itertools.combinations(fl, k):
            key = np.zeros(m.sum(), np.int64); mult = 1
            for f in combo:
                u, inv = cols[f]; key = key * len(u) + inv; mult *= len(u)
            uk, kk = np.unique(key, return_inverse=True)
            n, pos = evaluate(kk, y)
            strict, pooled, p, disc, sw = separation(n, pos)
            hi = p > 0.5; lo = p < 0.1
            rec = pos[hi].sum() / pos.sum() if pos.sum() else 0.0          # sub-7 states in switch cells
            lost = pos[lo].sum() / pos.sum() if pos.sum() else 0.0         # sub-7 states in discard cells
            res.append((strict, pooled, combo, len(uk), mi(n, pos), rec, lost))
    return res, m

def cells(m, combo):
    key = np.zeros(m.sum(), np.int64)
    for f in combo:
        u, inv = codes(F[f][m]); key = key * len(u) + inv
    uk, kk = np.unique(key, return_inverse=True)
    return kk

if __name__ == '__main__':
    which = sys.argv[1:] or [pop.drm_name(*x) for x in DRMS]
    top_lines = ['drm\tfeatures\tsize\tcells\tstrict_sep_P1\tpooled_sep_P1\tswitch_share_P1\tswitch_p_P1\tdiscard_share_P1\tdiscard_p_P1\tMI_bits\tholds_P2_5\tholds_P3_5\tholds_P3_6\tstrict_sep_P3_5\tswitch_p_P3_5\tdiscard_p_P3_5\tpareto\tcheap_only\tsub7_in_switch_cells\tsub7_in_discard_cells']
    fv = ['drm\tfeature\tMI_given_DRM_bits\tstrict_sep\tpooled_sep\tMI_given_DRM_ARM_bits']
    for name in which:
        drm = next(x for x in DRMS if pop.drm_name(*x) == name)
        res, m = run(drm, NAMES)
        c, e = drm; y = (d[m] <= 6)
        base = y.mean()
        # feature value: alone, and given ARM (carm, earm)
        armkey = np.unique(F['carm'][m] * 10 + F['earm'][m], return_inverse=True)[1]
        na, pa = evaluate(armkey, y.astype(float)); mi_arm = mi(na, pa)
        for r in res:
            if len(r[2]) == 1:
                f = r[2][0]
                key = np.unique(armkey * 1000 + np.unique(F[f][m], return_inverse=True)[1], return_inverse=True)[1]
                n2, p2 = evaluate(key, y.astype(float))
                fv.append(f'{name}\t{f}\t{r[4]:.5f}\t{r[0]:.4f}\t{r[1]:.4f}\t{mi(n2, p2) - mi_arm:.5f}')
        fv.append(f'{name}\t(ARM pair carm+earm)\t{mi_arm:.5f}\t\t\t')
        # all rules to a file
        with open(os.path.join(pop.OUT, f'search_{name}.tsv'), 'w') as f:
            f.write('features\tsize\tcells\tstrict_sep\tpooled_sep\tMI_bits\tsub7_in_switch_cells\tsub7_in_discard_cells\n')
            for r in sorted(res, key=lambda r: (-r[0], -r[5], r[6])):
                f.write(f"{'+'.join(r[2])}\t{len(r[2])}\t{r[3]}\t{r[0]:.4f}\t{r[1]:.4f}\t{r[4]:.5f}\t{r[5]:.4f}\t{r[6]:.4f}\n")
        # best per size by strict and by pooled, all features and cheap only; Pareto front (size vs strict)
        picks = []
        for k in (1, 2, 3):
            for cheap in (False, True):
                for cap in (12, 10**9):
                    cand = [r for r in res if len(r[2]) == k and r[3] <= cap and (not cheap or all(x in CHEAP for x in r[2]))]
                    if not cand: continue
                    for keyf in (lambda r: (round(r[0], 4), r[5], -r[6]), lambda r: (round(r[1], 4), r[5], -r[6]), lambda r: (r[5], -r[6])):
                        for r in sorted(cand, key=keyf, reverse=True)[:2]:
                            picks.append((r, k, cheap))
        seen = set(); best_strict = -1
        for r, k, cheap in sorted(picks, key=lambda t: (t[1], -t[0][0], -t[0][5])):
            if r[2] in seen: continue
            seen.add(r[2])
            strict, pooled, combo, ncell, mibits, rec, lost = r
            kk = cells(m, combo); n, pos = evaluate(kk, y.astype(float)); _, _, p, disc, sw = separation(n, pos)
            ho = {pn: held_out(kk, m, p, disc, sw, PP[pn]) for pn in ('P2_5', 'P3_5', 'P3_6')}
            ss = n[list(sw)].sum() / n.sum() if sw else 0; sp = pos[list(sw)].sum() / n[list(sw)].sum() if sw else float('nan')
            ds = n[list(disc)].sum() / n.sum() if disc else 0; dp = pos[list(disc)].sum() / n[list(disc)].sum() if disc else float('nan')
            pareto = (strict, rec) > best_strict if isinstance(best_strict, tuple) else True
            best_strict = max(best_strict, (strict, rec)) if isinstance(best_strict, tuple) else (strict, rec)
            h = lambda pn: ('yes' if ho[pn][0] else 'no') if ho[pn] else '-'
            top_lines.append(f"{name}\t{'+'.join(combo)}\t{k}\t{ncell}\t{strict:.4f}\t{pooled:.4f}\t{ss:.4f}\t{sp:.4f}\t{ds:.4f}\t{dp:.4f}\t{mibits:.5f}\t{h('P2_5')}\t{h('P3_5')}\t{h('P3_6')}\t{ho['P3_5'][3]:.4f}\t{ho['P3_5'][1]:.4f}\t{ho['P3_5'][2]:.4f}\t{'yes' if pareto else ''}\t{'yes' if all(x in CHEAP for x in combo) else ''}\t{rec:.4f}\t{lost:.4f}")
        print(name, 'done', len(res), 'rules; base', round(base, 4), 'ARM MI', round(mi_arm, 4))
    open(os.path.join(pop.OUT, 'search_top.tsv'), 'w').write('\n'.join(top_lines) + '\n')
    open(os.path.join(pop.OUT, 'feature_value.tsv'), 'w').write('\n'.join(fv) + '\n')
