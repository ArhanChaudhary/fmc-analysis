"""Every number of the skeleton/variant meta page, for one DR type, under the reading of drvar/src/tuple.rs.
The meta and the variations shown beside it are defined in `rules()`.

The most-pairs step is part of the meta and of every variation but `nopairs`.  Whether the baseline (no DR Bounding,
N = 0, so its groups are (skeleton, P, S, T)) takes the step too is the switch BASELINE_PAIRS; SVM_BASELINE_PAIRS=0
turns it off for one run.
usage: tfinal.py M -> ../out/meta/tfinal{M}.json"""
import os, sys, json
import numpy as np
from tcommon import T, BYQT, path, HCAP
from tcells import Cells
from teval import Ev
from tmeta import Rule, quantity, most_pairs, PAIRS_MODE
from torder import found_within

META = Rule(caps={'P+S+T': 5}, floor=True, pmax=1, label='meta', pairs=PAIRS_MODE == 'drop')
ORDER_KEY = 'len'       # the page's order of finishing: by moves to HTR, most pairs first among HTRs equally far (torder.py)
BASELINE_PAIRS = os.environ.get('SVM_BASELINE_PAIRS', '1') == '1'

def rules():
    """The rows of appendix B: (key, rule)."""
    m = META
    P = m.pairs
    out = [('pmax1', Rule(floor=False, pairs=P)), ('floor', Rule(floor=True, pairs=P))]
    for k in (3, 4, 5, 6):
        out.append((f'pst{k}', m.but(caps={'P+S+T': k})))
    out.append(('nofloor', m.but(floor=False)))
    out.append(('nopairs', m.but(pairs=False)))
    out.append(('p0', m.but(pmax=0)))
    out.append(('p2', m.but(pmax=2)))
    out.append(('pany', m.but(pmax=99)))
    out.append(('tn4', Rule(caps={'T+N': 4}, floor=True, pairs=P)))
    out.append(('stn5', Rule(caps={'S+T+N': 5}, floor=True, pairs=P)))
    out.append(('doc', Rule(caps={'P+S+T+N': 5}, floor=False, pairs=P)))
    out.append(('s3t5', Rule(caps={'S': 3, 'T': 5}, floor=True, pairs=P)))
    out.append(('spare2', m.but(s0=2)))
    out.append(('p1own', m.but(only='p1own')))
    out.append(('nopair', m.but(only='nopair')))
    out.append(('own', m.but(only='own')))
    return out

def missr(found, w):
    """Share of the within-goal DRs `w` that are not found (0 when a part of the sample has no within-goal DR)."""
    return float(1 - found[w].mean()) if w.any() else 0.0

def steps(rule, bound):
    """Does this rule take the most-pairs step under this bound?"""
    return rule.pairs and (bound != 'none' or BASELINE_PAIRS)

_MASKS = {}
def masks(t, rule, bound):
    """(HTRs the rule lets through under a bound, the ones left after the most-pairs step), kept for the next corner case."""
    key = (id(t), rule.text(), rule.only, rule.pairs, bound)
    if key not in _MASKS:
        N = t.N(bound)
        adm = rule.admit(t, N)
        _MASKS[key] = (adm, most_pairs(t, adm, N) if steps(rule, bound) else adm)
    return _MASKS[key]

def finished(t, rule, bound):
    """The HTRs the rule finishes under a bound, most-pairs step included."""
    return masks(t, rule, bound)[1]

def stats(t, e, rule, bound, case):
    k = t.rcase == case
    adm, fin = masks(t, rule, bound)
    before = adm & k; mask = fin & k
    sel = t.case == case; w = sel & t.wg
    c = t.per_dr(mask); f = t.found(mask)
    nok = int((mask & t.ok).sum()); n = int(mask.sum())
    if not rule.only:      # the same rule on the cell tables must give the same misses and work, before the step and after it
        for pairs, mk in ((False, before), (steps(rule, bound), mask)):
            a = rule.finish(e[bound], e[bound].N, pairs=pairs)
            assert abs(e[bound].miss(a) - missr(t.found(mk), w)) < 1e-9 and abs(e[bound].work(a) - t.per_dr(mk)[sel].mean()) < 1e-6, 'cells and records disagree'
    c0 = t.per_dr(before); f0 = t.found(before)
    return dict(htr_med=float(np.median(c[sel])), htr_mean=float(c[sel].mean()), n=n, nok=nok, miss=missr(f, w), found=int(f[w].sum()),
                step=bool(steps(rule, bound)),
                # the same before the most-pairs step
                htr_med0=float(np.median(c0[sel])), htr_mean0=float(c0[sel].mean()), n0=int(before.sum()), nok0=int((before & t.ok).sum()),
                miss0=missr(f0, w), found0=int(f0[w].sum()))

def effort(t, rule, case):
    """Routes to 2qt and skeletons, counted before any bound and before the most-pairs step (N = 0, the floor still
    applies): what has to be gone through to tell which variants are finished."""
    pre = rule.admit(t, np.zeros(t.n, np.int16)) & (t.rcase == case)
    post = finished(t, rule, 'cca') & (t.rcase == case)
    sel = t.case == case
    return dict(routes_med=float(np.median(t.routes(pre)[sel])), skel_med=float(np.median(t.skeletons(pre)[sel])),
                skel_finish_med=float(np.median(t.skeletons(post)[sel])))

def own_miss(t, case):
    """The meta's chance of missing with only the skeletons that have the DR's own quarter turns."""
    f = t.found(finished(t, META, 'cca') & (t.rcase == case) & (t.qsk == t.m))
    return missr(f, (t.case == case) & t.wg)

def breakdown(t, rule, case):
    """Each within-goal DR the meta misses, filed under what its nearest within-goal HTR breaks.  A DR with a
    within-goal HTR that passes everything but the most-pairs step is filed under 'pairs'."""
    N = t.N('cca')
    sel = (t.rcase == case)
    w = (t.case == case) & t.wg
    adm, fin = masks(t, rule, 'cca')
    adm = adm & sel; fin = fin & sel
    found = t.found(fin)
    before = t.found(adm)
    lost = np.nonzero(w & ~found)[0]
    inuni = t.found(sel)
    v = rule.violations(t, N)
    names = [k for k in v if k != 'goal']
    out = {'outside': 0, 'bound': 0, 'several': 0, 'pairs': 0}
    for k in names: out[k] = 0
    detail = []
    for dr in lost:
        if not inuni[dr]: out['outside'] += 1; continue
        if before[dr]:
            # the within-goal HTR the step drops that comes first in the meta's order
            rows = np.nonzero(adm & (t.dr == dr) & t.ok)[0]
            r = min(rows, key=lambda r: (t.L[r], t.P[r] + t.S[r] + t.T[r], t.P[r], t.S[r], t.T[r], N[r], t.total[r]))
            out['pairs'] += 1
            detail.append((int(dr), 'pairs', ['pairs'], int(r)))
            continue
        rows = np.nonzero(sel & (t.dr == dr) & t.ok)[0]
        # with the true N in place of the bound's, what does each within-goal HTR break?
        best = None
        for r in rows:
            Ntrue = t.tn[r]
            br = []
            if t.P[r] > rule.pmax: br.append('P')
            for k, c in rule.caps.items():
                if quantity(k, t.P[r], t.S[r], t.T[r], N[r]) > c: br.append(k)
            if rule.floor and t.P[r] + t.S[r] + t.T[r] + max(Ntrue, t.floor[r]) > t.spare[r]: br.append('floor')
            if rule.s0 and t.spare[r] < rule.s0: br.append('spare')
            if not br and t.P[r] + t.S[r] + t.T[r] + max(N[r], t.floor[r] if rule.floor else 0) > t.spare[r]: br = ['bound']
            key = (len(br), t.P[r], t.P[r] + t.S[r] + t.T[r])
            if best is None or key < best[0]: best = (key, br, r)
        br = best[1]
        cat = br[0] if len(br) == 1 else ('several' if br else 'bound')
        out[cat] = out.get(cat, 0) + 1
        detail.append((int(dr), cat, br, int(best[2])))
    return dict(counts=out, lost=len(lost), detail=detail)

def pairs_step(t, case):
    """The pairs among the HTRs that pass the caps, step 4 and the corner-case-aware bound: how many stand alone, how
    many share their skeleton and (P, S, T, N) with others, how many don't have the most pairs of their group
    ('dropped', whether the meta drops them or only takes them later), and how often each kind is within goal."""
    N = t.N('cca')
    adm = masks(t, META, 'cca')[0]
    if 'top' not in _MASKS: _MASKS['top'] = most_pairs(t, adm, N)      # whether or not the meta drops the others
    fin = _MASKS['top']
    adm = adm & (t.rcase == case)
    idx = np.nonzero(adm)[0]
    g = (((t.skel[idx].astype(np.int64) * 32 + t.P[idx]) * 32 + t.S[idx]) * 32 + t.T[idx]) * 32 + N[idx]
    _, inv, cnt = np.unique(g, return_inverse=True, return_counts=True)
    size = cnt[inv.ravel()]
    kept = fin[idx]
    okk = t.ok[idx]
    return dict(htrs=int(len(idx)), groups=int(len(cnt)), alone=int((size == 1).sum()), shared=int((size > 1).sum()),
                dropped=int((~kept).sum()), ok=int(okk.sum()), ok_dropped=int((okk & ~kept).sum()),
                # share within goal among the kept and among the dropped
                ok_kept_share=float(okk[kept].mean()) if kept.any() else None, ok_dropped_share=float(okk[~kept].mean()) if (~kept).any() else None,
                group_max=int(cnt.max()) if len(cnt) else 0)

def without_cap(m):
    """The meta without step 3's cap on the moves to HTR (every HTR in reach), premove pass included: per corner case
    what is needed to show what the cap changes."""
    t0 = T(m, hcap=False)
    out = {}
    for case in BYQT[m]:
        k = t0.rcase == case; sel = t0.case == case; w = sel & t0.wg
        e = dict(inuni=t0.found(k))
        for b in ('cca', 'none'):
            mask = finished(t0, META, b) & k
            per = t0.per_dr(mask)
            e[b] = dict(found=t0.found(mask), htr_med=float(np.median(per[sel])), htr_mean=float(per[sel].mean()), n=int(mask.sum()), nok=int((mask & t0.ok).sum()))
        fw = found_within(t0, finished(t0, META, 'cca') & k, t0.N('cca'), ORDER_KEY)
        e['within'] = [float(fw[w][:, j].mean()) if w.any() else 0.0 for j in range(3)]
        out[case] = e
    _MASKS.clear()
    return out

def without_rule(m, hcap=None):
    """The meta with every skeleton searched in full on both sides (no NISS rule): per corner case what is needed to
    show what the rule changes.  Also the best total of the HTRs the rule takes off each side of each DR.
    hcap=False: without the cap on the moves to HTR either (the reading on its own, for the list of changes)."""
    t0 = T(m, uniss=False, hcap=hcap)
    N = t0.N('cca')
    fin = finished(t0, META, 'cca')
    out = {}
    for case in BYQT[m]:
        k = t0.rcase == case; sel = t0.case == case; w = sel & t0.wg
        mask = fin & k
        fw = found_within(t0, mask, N, ORDER_KEY)
        pre = META.admit(t0, np.zeros(t0.n, np.int16)) & k
        out[case] = dict(found=t0.found(mask), per=t0.per_dr(mask), n=int(mask.sum()), nok=int((mask & t0.ok).sum()),
                         within=[float(fw[w][:, j].mean()) if w.any() else 0.0 for j in range(3)],
                         routes_med=float(np.median(t0.routes(pre)[sel])), skel_med=float(np.median(t0.skeletons(pre)[sel])))
    # what the rule takes off: 3 or more quarter turns, no corner move after the last one, and on normal only when
    # the skeleton doesn't start with a quarter turn too (as in tcommon.T)
    off = (t0.q >= 3) & (t0.lc == 0) & ~((t0.ell[:, 0] == 0) & (t0.side == 0))
    best = np.full(t0.ndr * 2, 99, np.int16)
    np.minimum.at(best, (t0.dr * 2 + t0.side)[off], t0.total[off])
    out['best_off'] = best; out['n_off'] = int(off.sum()); out['n'] = int(t0.n)
    _MASKS.clear()
    return out

if __name__ == '__main__':
    m = int(sys.argv[1])
    C0 = without_cap(m) if HCAP else None
    WO = without_rule(m, hcap=False) if HCAP else None
    W0 = without_rule(m) if T(m).uniss else None      # (the loader is cheap next to what follows)
    t = T(m)
    if W0:
        # every solution that ends on a quarter turn and a finish has a twin of the same length with the finish
        # before that turn, so on each side of each DR the left-over DRs must do at least as well as what they replace
        best = np.full(t.ndr * 2, 99, np.int16)
        np.minimum.at(best, (t.dr * 2 + t.side)[t.pre], t.total[t.pre])
        # (a solution that goes on after that quarter turn, with a slice or a corner swap or more, is not a solution of
        # the left-over DR: these are the sides where the best one of the skeletons taken off is of that kind)
        worse = (W0['best_off'] <= t.g) & (best > W0['best_off'])
        W0['sides_worse'] = [(int(k // 2), int(k % 2), int(W0['best_off'][k]), int(best[k])) for k in np.nonzero(worse)[0]]
    z = np.load(path(f'cells{m}.npz'))
    res = dict(m=m, goal=t.g, meta=META.text(), baseline_pairs=BASELINE_PAIRS, pairs_mode=PAIRS_MODE, uniss=t.uniss, rest_both=bool(getattr(t, 'rest_both', False)), cases={})
    if W0: res['rule'] = dict(htrs_full=W0['n'], taken_off=W0['n_off'], left_over=int(t.pre.sum()), sides_worse=W0['sides_worse'])
    # HTRs in reach whatever their distance (both sides; the premove pass), and the ones the cap on the moves to HTR keeps
    res['hcap'] = dict(on=bool(t.hcap), reach=int(t.nreach), reach_pre=int(getattr(t, 'nreach_pre', 0)), kept=int((~t.pre).sum()), kept_pre=int(t.pre.sum()))
    for case in BYQT[m]:
        e = {b: Ev(z, case, b) for b in ('none', 'simple', 'cca', 'comp')}
        sel = t.case == case
        lmin = int(t.L[t.rcase == case].min())
        R = dict(drs=int(sel.sum()), wg=int((sel & t.wg).sum()), lmin=lmin, bounds={}, var={}, orders={})
        for b in ('none', 'simple', 'cca', 'comp'):
            R['bounds'][b] = stats(t, e, META, b, case)
        R['effort'] = effort(t, META, case)
        R['own_miss'] = own_miss(t, case)
        # found within K in the page's order, with the bound and without
        w = (t.case == case) & t.wg
        for b in ('cca', 'none'):
            N = t.N(b); mask = finished(t, META, b) & (t.rcase == case)
            # (SVM_BASELINE_PAIRS=0: the baseline doesn't count the pairs)
            fw = found_within(t, mask, N, ORDER_KEY if b != 'none' or BASELINE_PAIRS else 'len_nopairs')
            R['orders'][f'{b}_len'] = [float(fw[w][:, j].mean()) for j in range(3)]
        # the meta's HTRs in the order of the 19 Nov page (skeletons shortest first, a skeleton's premove pass before
        # its linear check, fewest P+S+T, then (P, S, T, N), at most 3 per skeleton in a first pass) and in the page's
        # order without the pairs, for the list of changes
        N = t.N('cca'); mask = finished(t, META, 'cca') & (t.rcase == case)
        fw = found_within(t, mask, N, 'pst', 3)
        R['orders']['cca_before'] = [float(fw[w][:, j].mean()) for j in range(3)]
        fw = found_within(t, mask, N, 'len_nopairs')
        R['orders']['cca_len_nopairs'] = [float(fw[w][:, j].mean()) for j in range(3)]
        R['pairs'] = pairs_step(t, case)
        # step 4 under the cap, DR by DR
        k = t.rcase == case
        f1 = t.found(finished(t, META, 'cca') & k); f0 = t.found(finished(t, META.but(floor=False), 'cca') & k)
        # ... and before step 6
        g1 = t.found(masks(t, META, 'cca')[0] & k); g0 = t.found(masks(t, META.but(floor=False), 'cca')[0] & k)
        R['step4'] = dict(lost=int((f0 & ~f1)[w].sum()), gained=int((f1 & ~f0)[w].sum()), lost0=int((g0 & ~g1)[w].sum()), gained0=int((g1 & ~g0)[w].sum()))
        assert R['step4']['gained0'] == 0
        # the NISS rule: the meta with it (f1) against the meta with every skeleton in full (W0)
        if W0:
            a = W0[case]; sel = t.case == case
            fin = finished(t, META, 'cca') & k
            R['uniss'] = dict(lost=int((a['found'] & ~f1)[w].sum()), gained=int((f1 & ~a['found'])[w].sum()), found0=int(a['found'][w].sum()),
                              lost_drs=[int(v) for v in np.nonzero(a['found'] & ~f1 & w)[0]], gained_drs=[int(v) for v in np.nonzero(f1 & ~a['found'] & w)[0]],
                              miss0=missr(a['found'], w), htr_med0=float(np.median(a['per'][sel])), htr_mean0=float(a['per'][sel].mean()), n0=a['n'], nok0=a['nok'],
                              within0=a['within'], routes_med0=a['routes_med'], skel_med0=a['skel_med'],
                              # the HTRs the meta finishes on the left-over DRs, and their share of all it finishes
                              pre=int((fin & t.pre).sum()), pre_ok=int((fin & t.pre & t.ok).sum()))
        if C0:
            # the cap on the moves to HTR: what the meta finishes and finds without it
            a = C0[case]; fb = t.found(finished(t, META, 'none') & k)
            assert (t.found(k)[w] == a['inuni'][w]).all(), 'the cap on the moves to HTR takes a within-goal DR out of reach of the sample\'s HTRs'
            R['hcap'] = dict(lost=int((a['cca']['found'] & ~f1)[w].sum()), lost_base=int((a['none']['found'] & ~fb)[w].sum()), within0=a['within'],
                             **{f'{kk}0': a['cca'][kk] for kk in ('htr_med', 'htr_mean', 'n', 'nok')}, base_htr_med0=a['none']['htr_med'],
                             miss0=missr(a['cca']['found'], w))
            # ... and the same with no premove pass (every skeleton in full on both sides)
            if W0:
                wo = WO[case]
                R['hcap'].update(lost_nopass=int((wo['found'] & ~W0[case]['found'])[w].sum()), miss_nopass0=missr(wo['found'], w), routes_med_nopass0=wo['routes_med'])
        for key, rule in rules():
            s = stats(t, e, rule, 'cca', case); s.update(effort(t, rule, case)); s['text'] = rule.text()
            R['var'][key] = s
        R['miss'] = breakdown(t, META, case)
        res['cases'][case] = R
        print(case, 'meta:', {k: (round(v, 3) if isinstance(v, float) else v) for k, v in R['bounds']['cca'].items()}, R['effort'], R['miss']['counts'], flush=True)
    json.dump(res, open(path(f'tfinal{m}.json'), 'w'), indent=1)
