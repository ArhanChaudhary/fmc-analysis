"""The standard meta's cap against the skeleton/variant meta's, on the same HTRs in the same order.

Both metas finish HTRs in one order: by moves to HTR, fewest first, the most pairs first among HTRs equally far, ties
at random (torder.places).  Both look in the same places: every skeleton on normal and on inverse, and the premove
pass, whose premove counts as a move.  Neither uses a lower bound for N or step 4.  What differs is the cap:

  standard            every HTR at most c moves away, whatever its extra moves              (`abs`)
  skeleton/variant    every HTR with P <= 1 and P+S+T <= k, however far (k = 5 is the page's)   (`pen`)
  both together       P <= 1, P+S+T <= 5 and at most c moves away                            (`both`)

The HTRs are the page's records: an HTR is listed when its moves plus the corner moves left after it fit the goal, so
c = the goal is no cap at all, and every listed HTR has L+P+S+T within the goal.

Per corner case and cap: HTRs to finish per DR, reach (within-goal DRs with a within-goal HTR among the kept ones),
found within 5 / 10 / 20 and the median place of the first within-goal HTR; the same on normal and inverse alone (no
premove pass).  `below` / `above` are the standard caps on either side of the skeleton/variant meta's HTRs per DR
(median) and `match` the closer of the two.  At the match: the DRs and HTRs each cap has and the other doesn't, what
stops the other one, and candidates for the examples (mkstd.py finds their solutions).

Two checks of the standard side, which doesn't depend on the records' reading:
  * `own`: the standard meta on a list of its own (`drvar metastdlist`, ../out/meta/stdl{M}.r12): every HTR within the
    cap on normal, on inverse or with one NISS after up to 3 moves, any number of quarter turns, the pairs counted at
    the HTR.  Ties are random there too and the chances exact: with n HTRs of one length and pair count of which k are
    within goal, the first of the k is among the first j with chance 1 - C(n-j, k) / C(n, k).
  * the solutions of `drvar metastd` (tstd.checks).

usage: tord.py [M ...] -> ../out/meta/tord.json"""
import sys, json, os
import numpy as np
from tcommon import T, BYQT, drs, path
from tmeta import Rule
from torder import places, _order

KS = (5, 10, 20)
DTS = np.dtype([('dr', '<u4'), ('view', 'u1'), ('lev', 'u1'), ('sid', 'u1'), ('moves', 'u1'), ('total', 'u1'), ('pairs', 'u1'), ('q', 'u1'), ('lc', 'u1')])
assert DTS.itemsize == 12
# the highest cap of the standard meta's own list for each corner case (drvar metastdlist ... CAPMAX, STDORD_CAPS)
CAPMAX = {'4b2': 11, '4a2': 12, '2c3': 12, '4c3': 12, '0c3': 13, '2c4': 13, '0c4': 13, '4c4': 13}
PENK = [3, 4, 5, 6, None]         # P+S+T caps of the skeleton/variant side (None = no cap, P <= 1 alone); 5 is the page's
NCAND = 60                        # candidates kept for the examples of each kind
OWN = os.environ.get('TORD_OWN', '1') == '1'       # TORD_OWN=0: without the standard meta's own list (a test run)

def pen_rule(k):
    return Rule(caps={} if k is None else {'P+S+T': k}, floor=False, pmax=1)
def pen_name(k): return 'none' if k is None else str(k)
def abs_caps(g): return list(range(g - 5, g + 1))

def med_pos(fp, w):
    """Median place (1 = first) of the first within-goal HTR over the within-goal DRs `w` and the tie orders; None
    when half of them or more have none in the list."""
    v = fp[:, w].ravel()
    if not len(v): return None
    m = float(np.median(v))
    return None if m >= 10**8 else m + 1

def stat(t, mask, sel, w, fp):
    """What a cap keeps (`mask`) in one corner case (`sel`: its DRs, `w`: its within-goal DRs; fp: torder.places)."""
    per = t.per_dr(mask); f = t.found(mask)
    assert ((fp < 10**9).all(axis=0) == f).all() and ((fp < 10**9).any(axis=0) == f).all()
    return dict(htr_med=float(np.median(per[sel])), htr_mean=float(per[sel].mean()), n=int(mask.sum()), nok=int((mask & t.ok).sum()),
                reach=float(f[w].mean()) if w.any() else 0.0, found=int(f[w].sum()), pass_htrs=int((mask & t.pre).sum()),
                within=[float((fp[:, w] < K).mean()) if w.any() else 0.0 for K in KS], med_pos=med_pos(fp, w))

def first_per_dr(t, rows, cols):
    """Of the rows (indices into the records), the first of each DR in increasing order of the columns."""
    o = rows[_order([t.dr[rows]] + [c[rows] for c in cols])]
    return o[np.r_[True, t.dr[o][1:] != t.dr[o][:-1]]] if len(o) else o

def cand(t, rows):
    """Records as candidates for an example."""
    return [dict(dr=int(t.dr[r]), side='NI'[int(t.side[r])], pre=bool(t.pre[r]), q=int(t.q[r]), L=int(t.L[r]), P=int(t.P[r]), S=int(t.S[r]), T=int(t.T[r]),
                 moves=int(t.wl[r]), total=int(t.total[r])) for r in rows]

# ---------------------------------------------------------------------------- the standard meta on its own list
LF = np.r_[0.0, np.cumsum(np.log(np.arange(1, 2_000_000)))]        # log of n!

def lnC(n, k):
    return LF[n] - LF[k] - LF[n - k]

def p_within(B, n, k, K):
    """Chance that the first of k marked items among n in random order, after B others, is among the first K of all."""
    j = np.minimum(np.clip(K - B, 0, None), n)             # places of the cell that count
    none = np.where(j <= n - k, np.exp(lnC(np.maximum(n - j, k), k) - lnC(n, k)), 0.0)
    return np.where((k > 0) & (j > 0), 1 - none, 0.0)

class Std:
    """The standard meta's own HTRs of one DR type as counts per (DR, moves before the NISS, moves, pairs)."""
    def __init__(self, m, t):
        r = np.fromfile(path(f'stdl{m}.r12'), dtype=DTS)
        r = r[np.isin(r['dr'], t.d.index.values)]
        self.g = t.g; self.ndr = t.ndr
        shape = (self.ndr, 4, 16, 17)
        flat = ((r['dr'].astype(np.int64) * 4 + r['lev']) * 16 + r['moves']) * 17 + r['pairs']
        size = int(np.prod(shape))
        self.n = np.bincount(flat, minlength=size).reshape(shape)
        self.k = np.bincount(flat[r['total'] <= self.g], minlength=size).reshape(shape)
        self.best = np.full((self.ndr, 4, 16), 255, np.int64)          # best total by (DR, level, moves)
        np.minimum.at(self.best, (r['dr'].astype(np.int64), r['lev'].astype(np.int64), r['moves'].astype(np.int64)), r['total'])
        self.rows = len(r); self.r = r
        lin = r[r['lev'] == 0]                                          # on normal and inverse: quarter turns over the DR's
        self.q_over = (lin['dr'].astype(np.int64), lin['moves'].astype(np.int64), lin['q'].astype(np.int64) - m)

    def simulate(self, sel, w, lev, cap, reps=40, seed=7):
        """Found within K at this cap and NISS depth from random tie orders of the records themselves, most pairs
        first (a check of the exact chances of `stats`)."""
        r = self.r
        k = r[np.isin(r['dr'], np.nonzero(sel)[0]) & (r['lev'] <= lev) & (r['moves'] <= cap)]
        rng = np.random.default_rng(seed)
        dr = k['dr'].astype(np.int64); ok = k['total'] <= self.g
        cols = [dr, k['moves'].astype(np.int64), -k['pairs'].astype(np.int64)]
        fp = np.full((reps, self.ndr), 10**9, np.int64)
        for rep in range(reps):
            o = _order(cols, pre=np.argsort(rng.random(len(k)), kind='stable'))
            d = dr[o]; okk = ok[o]
            new = np.r_[True, d[1:] != d[:-1]]
            pos = np.arange(len(d)) - np.maximum.accumulate(np.where(new, np.arange(len(d)), 0))
            np.minimum.at(fp[rep], d[okk], pos[okk])
        return dict(reps=reps, within=[float((fp[:, w] < K).mean()) if w.any() else 0.0 for K in KS], med_pos=med_pos(fp, w))

    def stats(self, sel, w, lev, cap):
        """sel: the corner case's DRs; w: its within-goal DRs.  The cells of the order: by moves, and by most pairs
        within one number of moves."""
        n = self.n[:, :lev + 1].sum(axis=1); k = self.k[:, :lev + 1].sum(axis=1)        # (DR, moves, pairs)
        n = n[:, :, ::-1].reshape(self.ndr, -1); k = k[:, :, ::-1].reshape(self.ndr, -1)
        inc = np.repeat(np.arange(16), 17) <= cap
        n = n[:, inc]; k = k[:, inc]
        per = n.sum(axis=1)
        found = k.sum(axis=1) > 0
        # the first cell with a within-goal HTR, and the HTRs before it
        first = np.argmax(k > 0, axis=1)
        B = np.cumsum(n, axis=1) - n
        i = np.arange(self.ndr)
        Bf, nf, kf = B[i, first], n[i, first], np.where(found, k[i, first], 0)
        ww = np.nonzero(w)[0]
        within = [float(p_within(Bf[ww], nf[ww], kf[ww], K).mean()) if len(ww) else 0.0 for K in KS]
        # median place: the smallest x with a chance of 1/2 that the first within-goal HTR is among the first x
        med = None
        if len(ww) and found[ww].mean() >= 0.5:
            lo, hi = 1, int(per[ww].max()) + 1
            F = lambda x: p_within(Bf[ww], nf[ww], kf[ww], x).mean()
            if F(hi) >= 0.5:
                while lo < hi:
                    mid = (lo + hi) // 2
                    if F(mid) >= 0.5: hi = mid
                    else: lo = mid + 1
                med = float(lo)
        return dict(htr_med=float(np.median(per[sel])), htr_mean=float(per[sel].mean()), n=int(per[sel].sum()), nok=int(k.sum(axis=1)[sel].sum()),
                    reach=float(found[ww].mean()) if len(ww) else 0.0, found=int(found[ww].sum()), within=within, med_pos=med), found

def check_std(m, t, S, d):
    """The own list against `drvar metastd` (which only has the HTRs with a within-goal finish, by another search):
    for every DR, cap and number of moves before the NISS, the best within-goal total within the cap is the same."""
    from tstd import CAPS, LEVELS
    ncheck = 0
    for c in CAPS:
        for L in LEVELS:
            mine = np.minimum.reduce(S.best[:, :L + 1, :c + 1].reshape(S.ndr, -1), axis=1)[d.index.values]
            mine = np.where(mine <= t.g, mine, 255)
            theirs = d[f'std{L}_{c}'].values
            ok = np.array([c <= CAPMAX[x] for x in t.case[d.index.values]])
            assert (mine[ok] == theirs[ok]).all(), (m, c, L, int((mine[ok] != theirs[ok]).sum()))
            ncheck += int(ok.sum())
    return ncheck

def closest(stats, target):
    """The key of the entry whose HTRs per DR (median) come closest to the target, as a ratio."""
    return min(stats, key=lambda kk: abs(np.log(max(stats[kk]['htr_med'], 0.5) / target)))

if __name__ == '__main__':
    ms = [int(a) for a in sys.argv[1:]] or [2, 3, 4]
    out = {}
    for m in ms:
        t = T(m, uniss='add', rest_floor=False)
        g = t.g
        Z = np.zeros(t.n, np.int16)
        pst = t.P + t.S + t.T
        assert (pst <= t.spare).all() and (t.wl <= g).all(), 'a listed HTR is in reach of the goal'
        assert (t.wl + t.lc == t.L + pst).all(), 'moves to HTR = L + P + S + T less the corner moves left'
        # the solutions of `drvar metastd` against these records, and the standard meta's own list against them
        from tstd import checks
        d, _, differ = checks(m, t)
        S = Std(m, t) if OWN else None
        nchk = check_std(m, t, S, d) if S else None
        print(m, t.n, 'records;', 'own list:', S.rows if S else None, 'HTRs, against metastd:', nchk, 'comparisons the same', flush=True)
        pen = {k: pen_rule(k).admit(t, Z) for k in PENK}
        for k in PENK: assert (pen[k] == ((t.P <= 1) & ((pst <= k) if k is not None else True))).all()
        full = ~t.pre
        for case in BYQT[m]:
            sel = t.case == case; w = sel & t.wg; kc = t.rcase == case
            R = dict(m=m, goal=g, drs=int(sel.sum()), wg=int(w.sum()), rest_both=bool(getattr(t, 'rest_both', False)), lmin=int(t.L[kc].min()),
                     abs={}, pen={}, both={}, nopass=dict(abs={}, pen={}, both={}))
            names, masks = [], []
            for c in abs_caps(g):
                names += [('abs', str(c), True), ('abs', str(c), False)]; masks += [kc & (t.wl <= c), kc & (t.wl <= c) & full]
            for k in PENK:
                names += [('pen', pen_name(k), True), ('pen', pen_name(k), False)]; masks += [kc & pen[k], kc & pen[k] & full]
            for c in abs_caps(g)[:-1]:           # the two caps together: P <= 1, P+S+T <= 5 and at most c moves away
                names += [('both', str(c), True), ('both', str(c), False)]; masks += [kc & pen[5] & (t.wl <= c), kc & pen[5] & (t.wl <= c) & full]
            fp = places(t, masks)
            M = {}
            for (kind, key, ps), mk, f in zip(names, masks, fp):
                (R[kind] if ps else R['nopass'][kind])[key] = stat(t, mk, sel, w, f)
                M[(kind, key, ps)] = mk
            assert R['abs'][str(g)]['n'] == int(kc.sum())            # the goal as a cap keeps every listed HTR
            # the standard caps on either side of the skeleton/variant meta's HTRs per DR, and the closer one
            for ps, D in ((True, R), (False, R['nopass'])):
                target = D['pen']['5']['htr_med']
                lo = [c for c in abs_caps(g) if D['abs'][str(c)]['htr_med'] <= target]
                hi = [c for c in abs_caps(g) if D['abs'][str(c)]['htr_med'] >= target]
                D['below'] = max(lo) if lo else None; D['above'] = min(hi) if hi else None
                D['match'] = int(closest(D['abs'], target))
            cm = R['match']
            A, B = M[('abs', str(cm), True)], M[('pen', '5', True)]
            fa, fb = t.found(A), t.found(B)
            # the same DRs under both caps, for every standard cap
            R['cross'] = {}
            for c in abs_caps(g):
                f = t.found(M[('abs', str(c), True)])
                R['cross'][str(c)] = dict(both=int((f & fb)[w].sum()), abs_only=int((f & ~fb)[w].sum()), pen_only=int((~f & fb)[w].sum()), neither=int((~f & ~fb)[w].sum()))
            # the HTRs of each cap at the match: kept by both, by one only; how many, and how many within goal
            R['htrs'] = {name: dict(n=int(mk.sum()), nok=int((mk & t.ok).sum()))
                         for name, mk in (('both', A & B), ('abs_only', A & ~B), ('pen_only', B & ~A))}
            # ... and what the skeleton/variant cap has against the HTRs it doesn't keep
            x = A & ~B
            R['htrs']['abs_only_why'] = {name: dict(n=int((x & mk).sum()), nok=int((x & mk & t.ok).sum()))
                                         for name, mk in (('P', (t.P > 1) & (pst <= 5)), ('P+S+T', (t.P <= 1) & (pst > 5)), ('both', (t.P > 1) & (pst > 5)))}
            # how far over the cap the HTRs only the skeleton/variant cap keeps are
            x = B & ~A
            R['htrs']['pen_only_over'] = {str(int(v)): dict(n=int((x & (t.wl - cm == v)).sum()), nok=int((x & (t.wl - cm == v) & t.ok).sum())) for v in np.unique(t.wl[x] - cm)}
            # within-goal DRs only the standard cap reaches: what its within-goal HTR within the cap breaks, the
            # one that breaks the least
            drs_a = np.nonzero(w & fa & ~fb)[0]
            rows = np.nonzero(A & t.ok & np.isin(t.dr, drs_a))[0]
            brP = (t.P > 1).astype(np.int64); brK = (pst > 5).astype(np.int64)
            pick = first_per_dr(t, rows, [brP + brK, t.P, pst, t.total, t.wl])
            assert len(pick) == len(drs_a) and ((brP + brK)[pick] > 0).all()
            why = np.where(brP[pick] & brK[pick], 'both', np.where(brP[pick] == 1, 'P', 'P+S+T'))
            R['why_abs_only'] = {k: int((why == k).sum()) for k in ('P', 'P+S+T', 'both')}
            R['ex_abs'] = [dict(c, why=str(y)) for c, y in zip(cand(t, pick), why)]
            R['ex_abs'] = sorted(R['ex_abs'], key=lambda c: (c['total'], c['moves'], c['dr']))[:NCAND]
            # within-goal DRs only the skeleton/variant cap reaches: how far over the cap its nearest within-goal HTR is
            drs_b = np.nonzero(w & fb & ~fa)[0]
            rows = np.nonzero(B & t.ok & np.isin(t.dr, drs_b))[0]
            pick = first_per_dr(t, rows, [t.wl, t.total, pst])
            assert len(pick) == len(drs_b) and (t.wl[pick] > cm).all()
            over = t.wl[pick] - cm
            R['over_pen_only'] = {str(int(v)): int((over == v).sum()) for v in np.unique(over)}
            R['ex_pen'] = sorted(cand(t, pick), key=lambda c: (c['total'], c['moves'], c['dr']))[:NCAND]
            # the order without the pairs, for the two caps at the match
            f2 = places(t, [A, B], pairs=False)
            R['nopairs'] = dict(abs=dict(within=[float((f2[0][:, w] < K).mean()) if w.any() else 0.0 for K in KS], med_pos=med_pos(f2[0], w)),
                                pen=dict(within=[float((f2[1][:, w] < K).mean()) if w.any() else 0.0 for K in KS], med_pos=med_pos(f2[1], w)))
            # the standard meta's own search on normal and inverse (`drvar metastd`): within-goal DRs it reaches
            # inside each cap, and how many of those the records don't reach there
            dc = d[(d.case == case) & d.wg]
            R['own_search'] = {}
            for c in abs_caps(g):
                if f'std0_{c}' not in d.columns: continue
                own = (dc[f'std0_{c}'] <= g).values
                rec = t.found(M[('abs', str(c), False)])[dc.index.values]
                assert not (rec & ~own).any()
                R['own_search'][str(c)] = dict(reach=float(own.mean()) if len(dc) else 0.0, found=int(own.sum()), more=int((own & ~rec).sum()),
                                               more_drs=[int(v) for v in dc.index.values[own & ~rec]][:20], own3=int((dc[f'std3_{c}'] <= g).sum()))
            # the standard meta on its own list, at every cap and number of moves before the NISS
            if S:
                R['own'] = {}; R['capmax'] = CAPMAX[case]
                for cap in range(g - 5, CAPMAX[case] + 1):
                    for lev in range(4):
                        e, f = S.stats(sel, w, lev, cap)
                        e['cross'] = dict(both=int((f & fb)[w].sum()), abs_only=int((f & ~fb)[w].sum()), pen_only=int((~f & fb)[w].sum()), neither=int((~f & ~fb)[w].sum()))
                        R['own'][f'{cap}_{lev}'] = e
                target = R['pen']['5']['htr_med']
                R['own_match'] = closest(R['own'], target)
                # the exact chances against random orders of the list itself, at that match
                co, lo_ = map(int, R['own_match'].split('_'))
                R['sim'] = S.simulate(sel, w, lo_, co)
                assert max(abs(x - y) for x, y in zip(R['sim']['within'], R['own'][R['own_match']]['within'])) < 0.05, (case, R['sim'], R['own'][R['own_match']]['within'])
                # HTRs of the own list on normal and inverse with more than two quarter turns over the DR's (the
                # records don't have them), within the matched cap of the comparison without the pass
                dq, mq, oq = S.q_over
                k = sel[dq] & (mq <= min(R['nopass']['match'], CAPMAX[case]))
                R['own_more_qt'] = dict(cap=int(min(R['nopass']['match'], CAPMAX[case])), n=int(k.sum()), more=int((k & (oq > 2)).sum()))
                R['std_check'] = nchk
            out[case] = R
            a = R['pen']['5']; b = R['abs'][str(cm)]
            print(case, 'pen5', a['htr_med'], round(a['reach'], 4), [round(v, 3) for v in a['within']], a['med_pos'],
                  '| abs', cm, b['htr_med'], round(b['reach'], 4), [round(v, 3) for v in b['within']], b['med_pos'],
                  '| below/above', R['below'], R['above'], '| cross', R['cross'][str(cm)], R['why_abs_only'], R['over_pen_only'],
                  '| own', R.get('own_match'), flush=True)
        del t, S, pen
    json.dump(out, open(path('tord.json' if len(ms) == 3 else f"tord_part{''.join(map(str, ms))}.json"), 'w'), indent=1)
