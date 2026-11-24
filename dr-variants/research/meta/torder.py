"""Found within K finishes, in a meta's order of finishing, on the records themselves.

The page's order ('len', since 24 Nov 2026) is the standard meta's: the HTRs of a DR by their moves to HTR, fewest
first, whatever skeleton, side or pass they are on (a premove counts as a move); among HTRs equally far the ones with
the most pairs first ('len_nopairs': without that); ties at random.  With it, what a rule keeps is all that tells two
metas apart (`places`).

The order before that is kept for the page's list of changes (`first_positions`): skeletons shortest first (among
those of one length the premove pass's first, then ties at random), each skeleton's variants in increasing order of a
key (ties at random), and optionally a first pass of at most `first` finishes per skeleton before the rest follow in
the same order.  Its keys: 'lex' (P, S, T, N); 'pst' fewest P+S+T first, then (P, S, T, N); 'pen' fewest P+S+T+N first;
'pstp' = 'pst', and among variants with the same (P, S, T, N) the ones with more pairs first.

Averaged over `reps` random tie orders."""
import numpy as np, pandas as pd

def keys(t, N, name):
    pst = t.P + t.S + t.T
    if name == 'len': return [t.wl, -t.pairs]          # one skeleton at a time, its HTRs by moves to HTR, most pairs first
    if name == 'pstp': return [pst, t.P, t.S, t.T, N, -t.pairs]
    return {'lex': [t.P, t.S, t.T, N], 'pst': [pst, t.P, t.S, t.T, N], 'pen': [pst + N, t.P, t.S, t.T, N]}[name]

def _order(cols, pre=None):
    """Row order by the columns, the first one sorting first, stable (rows that tie keep the order of `pre`, or their
    own).  The columns are packed into one integer when they fit, which is several times faster than a lexsort."""
    n = len(cols[0])
    base = np.arange(n) if pre is None else pre
    key = np.zeros(n, np.int64); bits = 0
    for c in cols:
        c = c.astype(np.int64); lo = int(c.min()) if n else 0
        w = max(1, int(c.max() - lo).bit_length()) if n else 1
        bits += w
        if bits > 62: break
        key = (key << w) | (c - lo)
    if bits > 62:
        return base[np.lexsort(tuple(c[base] for c in cols[::-1]))]
    return base[np.argsort(key[base], kind='stable')]

def first_positions(t, mask, N, order='lex', first=0, reps=20, seed=1):
    """(reps, DR index): the place (0 = first) of the first within-goal HTR among the masked ones in that order, for
    each random tie order; 10**9 where the masked set has none."""
    rng = np.random.default_rng(seed)
    idx = np.nonzero(mask)[0]
    dr = t.dr[idx]; skel = t.skel[idx]; L = t.L[idx]; ok = t.ok[idx]
    full = ~t.pre[idx]                       # the premove pass of a skeleton comes before the skeleton in full
    ks = [k[idx] for k in keys(t, N, order)]
    nsk = int(t.skel.max()) + 1
    out = np.full((reps, t.ndr), 10**9, np.int64)
    for rep in range(reps):
        u = rng.random(len(idx)); v = rng.random(nsk)
        # by DR, skeleton length, pass before full, skeletons of one length at random, the key, ties at random
        vr = np.empty(nsk, np.int64); vr[np.argsort(v, kind='stable')] = np.arange(nsk)
        o = _order([dr, L, full, vr[skel]] + ks, pre=np.argsort(u, kind='stable'))
        d = dr[o]; sk = skel[o]; okk = ok[o]
        if first:
            newsk = np.r_[True, sk[1:] != sk[:-1]]
            start = np.maximum.accumulate(np.where(newsk, np.arange(len(o)), 0))
            rank = np.arange(len(o)) - start
            o2 = _order([d, rank >= first])
            d = d[o2]; okk = okk[o2]
        newdr = np.r_[True, d[1:] != d[:-1]]
        pos = np.arange(len(d)) - np.maximum.accumulate(np.where(newdr, np.arange(len(d)), 0))
        np.minimum.at(out[rep], d[okk], pos[okk])
    return out

def skeleton_places(t, mask, firsts=(0,), reps=20, seed=1):
    """One skeleton at a time: skeletons shortest first (L; among those of one length the premove pass's first, then
    at random), a skeleton's HTRs by moves to HTR, most pairs first among HTRs equally far, ties at random.  For each
    value of `firsts`: 0 = every skeleton gone through in full before the next; k = a first pass of at most k HTRs
    per skeleton, then the rest in the same order.  Returns {first: (reps, DR index)}, the place (0 = first) of the
    first within-goal HTR among the masked ones, 10**9 where there is none.  One sort per tie order serves every
    value of `firsts`."""
    rng = np.random.default_rng(seed)
    idx = np.nonzero(mask)[0]
    out = {f: np.full((reps, t.ndr), 10**9, np.int64) for f in firsts}
    if not len(idx): return out
    dr = t.dr[idx]; skel = t.skel[idx]; L = t.L[idx]; ok = t.ok[idx]
    full = ~t.pre[idx]
    ks = [t.wl[idx], -t.pairs[idx]]
    nsk = int(t.skel.max()) + 1
    for rep in range(reps):
        u = rng.random(len(idx)); v = rng.random(nsk)
        vr = np.empty(nsk, np.int64); vr[np.argsort(v, kind='stable')] = np.arange(nsk)
        o = _order([dr, L, full, vr[skel]] + ks, pre=np.argsort(u, kind='stable'))
        d = dr[o]; sk = skel[o]; okk = ok[o]
        newsk = np.r_[True, sk[1:] != sk[:-1]]
        rank = np.arange(len(o)) - np.maximum.accumulate(np.where(newsk, np.arange(len(o)), 0))      # place within its skeleton
        for f in firsts:
            if f:
                o2 = _order([d, rank >= f])
                d2 = d[o2]; ok2 = okk[o2]
            else:
                d2, ok2 = d, okk
            newdr = np.r_[True, d2[1:] != d2[:-1]]
            pos = np.arange(len(d2)) - np.maximum.accumulate(np.where(newdr, np.arange(len(d2)), 0))
            np.minimum.at(out[f][rep], d2[ok2], pos[ok2])
    return out

def skeleton_places_multi(t, masks, first=0, reps=20, seed=1):
    """`skeleton_places` for several sets of kept HTRs at once (one value of `first`): shape (masks, reps, DR index).
    One sort of the union per tie order serves every mask: a kept HTR's place within its skeleton, and then within
    its pass, is a count of the kept HTRs before it."""
    union = np.zeros(t.n, bool)
    for mk in masks: union |= mk
    idx = np.nonzero(union)[0]
    out = np.full((len(masks), reps, t.ndr), 10**9, np.int64)
    if not len(idx): return out
    rng = np.random.default_rng(seed)
    dr = t.dr[idx]; skel = t.skel[idx]; L = t.L[idx]; ok = t.ok[idx]
    full = ~t.pre[idx]
    ks = [t.wl[idx], -t.pairs[idx]]
    nsk = int(t.skel.max()) + 1
    kept = [mk[idx] for mk in masks]
    for rep in range(reps):
        u = rng.random(len(idx)); v = rng.random(nsk)
        vr = np.empty(nsk, np.int64); vr[np.argsort(v, kind='stable')] = np.arange(nsk)
        o = _order([dr, L, full, vr[skel]] + ks, pre=np.argsort(u, kind='stable'))
        d = dr[o]; sk = skel[o]; okk = ok[o]
        newsk = np.r_[True, sk[1:] != sk[:-1]]; skstart = np.nonzero(newsk)[0]; wsk = np.cumsum(newsk) - 1
        newdr = np.r_[True, d[1:] != d[:-1]]; drstart = np.nonzero(newdr)[0]; wdr = np.cumsum(newdr) - 1
        for j, kp in enumerate(kept):
            kk = kp[o]
            before = np.cumsum(kk) - kk                       # kept rows before each row
            hit = np.nonzero(kk & okk)[0]
            if first:
                rank = before - before[skstart][wsk]          # ... of its own skeleton
                p1 = kk & (rank < first); p2 = kk & ~p1
                c1 = np.cumsum(p1); b1 = c1 - p1; b2 = np.cumsum(p2) - p2
                tot1 = np.diff(np.r_[b1[drstart], c1[-1]])     # first-pass rows of each DR
                h = wdr[hit]
                pos = np.where(p1[hit], b1[hit] - b1[drstart][h], tot1[h] + b2[hit] - b2[drstart][h])
            else:
                pos = before[hit] - before[drstart][wdr[hit]]
            np.minimum.at(out[j, rep], d[hit], pos)
    return out

def tier_places(o, masks, firsts=(0,), late2=False, reps=20, seed=1):
    """One skeleton at a time, with NISS in its place.  `o` has one row per HTR with its skeleton `skel` (the linear
    skeleton its whole solution is on), that skeleton's length `Lsk`, and `tier`: 0 after a single quarter turn made
    first on the other side (a premove), 1 linear, 2 after a longer start.  Skeletons shortest first, those of one
    length at random; a skeleton's HTRs by tier (the premove's before the linear ones, the longer starts' after all
    of them), then by moves to HTR, then most pairs, ties at random.  For each value of `firsts`: 0 = every skeleton
    in full before the next; k = a first pass of at most k HTRs per skeleton, then the rest in the same order.
    late2: the HTRs of tier 2 are never in the first pass.
    Returns (masks, firsts, reps, DR index): the place (0 = first) of the first within-goal HTR among the kept ones,
    10**9 where there is none.  One sort of the union per tie order serves every mask and first pass."""
    union = np.zeros(o.n, bool)
    for mk in masks: union |= mk
    idx = np.nonzero(union)[0]
    out = np.full((len(masks), len(firsts), reps, o.ndr), 10**9, np.int64)
    if not len(idx): return out
    rng = np.random.default_rng(seed)
    dr = o.dr[idx]; skel = o.skel[idx]; ok = o.ok[idx]; tier = o.tier[idx]
    cols = [o.Lsk[idx], None, tier, o.wl[idx], -o.pairs[idx]]
    nsk = int(o.skel.max()) + 1
    kept = [mk[idx] for mk in masks]
    for rep in range(reps):
        u = rng.random(len(idx)); v = rng.random(nsk)
        vr = np.empty(nsk, np.int64); vr[np.argsort(v, kind='stable')] = np.arange(nsk)
        cols[1] = vr[skel]
        od = _order([dr] + cols, pre=np.argsort(u, kind='stable'))
        d = dr[od]; sk = skel[od]; okk = ok[od]; t2 = tier[od] == 2
        newsk = np.r_[True, sk[1:] != sk[:-1]]; skstart = np.nonzero(newsk)[0]; wsk = np.cumsum(newsk) - 1
        newdr = np.r_[True, d[1:] != d[:-1]]; drstart = np.nonzero(newdr)[0]; wdr = np.cumsum(newdr) - 1
        for j, kp in enumerate(kept):
            kk = kp[od]
            before = np.cumsum(kk) - kk                       # kept rows before each row
            hit = np.nonzero(kk & okk)[0]
            h = wdr[hit]
            rank = None
            for i, first in enumerate(firsts):
                if first:
                    if rank is None: rank = before - before[skstart][wsk]          # kept rows of its skeleton before it
                    p1 = kk & (rank < first)
                    if late2: p1 &= ~t2
                    p2 = kk & ~p1
                    c1 = np.cumsum(p1); b1 = c1 - p1; b2 = np.cumsum(p2) - p2
                    tot1 = np.diff(np.r_[b1[drstart], c1[-1]])     # first-pass rows of each DR
                    pos = np.where(p1[hit], b1[hit] - b1[drstart][h], tot1[h] + b2[hit] - b2[drstart][h])
                else:
                    pos = before[hit] - before[drstart][h]
                np.minimum.at(out[j, i, rep], d[hit], pos)
    return out

def first_positions_lexsort(t, mask, N, order='lex', first=0, reps=20, seed=1):
    """The same with a plain lexsort, as a check of the packed order (same random numbers, so the same result)."""
    rng = np.random.default_rng(seed)
    idx = np.nonzero(mask)[0]
    dr = t.dr[idx]; skel = t.skel[idx]; L = t.L[idx]; ok = t.ok[idx]
    full = ~t.pre[idx]
    ks = [k[idx] for k in keys(t, N, order)]
    nsk = int(t.skel.max()) + 1
    out = np.full((reps, t.ndr), 10**9, np.int64)
    for rep in range(reps):
        u = rng.random(len(idx)); v = rng.random(nsk)[skel]
        o = np.lexsort(tuple([u] + ks[::-1] + [skel, v, full, L, dr]))      # last key sorts first
        d = dr[o]; sk = skel[o]; okk = ok[o]
        if first:
            newsk = np.r_[True, sk[1:] != sk[:-1]]
            start = np.maximum.accumulate(np.where(newsk, np.arange(len(o)), 0))
            rank = np.arange(len(o)) - start
            o2 = np.lexsort((np.arange(len(o)), rank >= first, d))
            d = d[o2]; okk = okk[o2]
        newdr = np.r_[True, d[1:] != d[:-1]]
        pos = np.arange(len(d)) - np.maximum.accumulate(np.where(newdr, np.arange(len(d)), 0))
        np.minimum.at(out[rep], d[okk], pos[okk])
    return out

RBITS = 30          # random bits under the key: the ties' order

def places(t, masks, reps=20, seed=1, pairs=True):
    """The order 'len'.  For each mask (the HTRs a rule keeps), each random tie order and each DR: the place (0 =
    first) of the first within-goal HTR among the kept ones; 10**9 where the kept set has none.  Shape (masks, reps,
    DR index).  One sort per tie order serves every mask, since a kept HTR's place is the number of kept HTRs of its
    DR before it; the masks are sorted over their union only."""
    union = np.zeros(t.n, bool)
    for mk in masks: union |= mk
    idx = np.nonzero(union)[0]
    out = np.full((len(masks), reps, t.ndr), 10**9, np.int64)
    if not len(idx): return out
    dr = t.dr[idx].astype(np.int64); ok = t.ok[idx]
    wl = t.wl[idx].astype(np.int64)
    assert 0 <= wl.min() and wl.max() < 64 and t.ndr < (1 << 20)
    key = dr * 64 + wl
    if pairs:
        pr = t.pairs[idx].astype(np.int64)
        assert 0 <= pr.min() and pr.max() <= 16
        key = key * 32 + (16 - pr)
    key <<= RBITS
    kept = [mk[idx] for mk in masks]
    rng = np.random.default_rng(seed)
    for rep in range(reps):
        o = np.argsort(key | rng.integers(0, 1 << RBITS, len(idx)), kind='stable')
        d = dr[o]; okk = ok[o]
        start = np.r_[0, np.nonzero(d[1:] != d[:-1])[0] + 1]          # the first row of each DR
        for j, kp in enumerate(kept):
            ks = kp[o]
            before = np.cumsum(ks) - ks                                 # kept rows before each row
            hit = np.nonzero(ks & okk)[0]
            base = before[start[np.searchsorted(start, hit, side='right') - 1]]
            np.minimum.at(out[j, rep], d[hit], before[hit] - base)
    return out

def found_within(t, mask, N=None, order='len', first=0, Ks=(5, 10, 20), reps=20, seed=1):
    """Returns per DR (array over DR index) the chance of a within-goal finish among the first K, K in Ks.  N and
    `first` only matter to the orders that go skeleton by skeleton."""
    if order in ('len', 'len_nopairs'): fp = places(t, [mask], reps, seed, pairs=order == 'len')[0]
    else: fp = first_positions(t, mask, N, order, first, reps, seed)
    return np.stack([(fp < K).mean(axis=0) for K in Ks], axis=1)
