#!/usr/bin/env python3
"""Questions 1, 2 and 5: how often each route class finds the optimal (and a finish within +1), the greedy
checklist per subset, and what inverting the last DR move adds.

A class "works" on a state at a target length if some finish of at most that length follows it in some NISS
reading (all optimal and all optimal+1 finishes, every split, either side first).  Targets:
  opt   the state's optimal                        p1   optimal + 1
  vopt  with the last DR move inverted allowed: t* = min(opt(X), opt(X*R2)), the class works on X or on X*R2 at t*
  vp1   the same at t* + 1
Groups: each of the 48 subsets (25,000 uniform states each) and each of the 14 corner subsets (its edge subsets pooled,
weighted by their exact sizes).

Outputs: out/q1_routes.tsv, out/q2_checklist.tsv, out/q2_best.tsv, out/q5_variation.tsv, out/big/membership_<level>.npz
(cached matrices for the grading and claims scripts)."""
import sys, os, itertools, collections, time
import numpy as np
from common import *

LEVELS = ['C', 'H', 'Q', 'F']
TARGETS = ['opt', 'p1', 'vopt', 'vp1']
N = None

class_ids = {lv: {} for lv in LEVELS}      # class string -> id
class_names = {lv: [] for lv in LEVELS}
rid2cls = {lv: {} for lv in LEVELS}
def cls_of(rid, lv):
    m = rid2cls[lv]
    c = m.get(rid)
    if c is None:
        k = keys()[rid]
        if (k[0] == 'F') != (lv == 'F'):
            c = -1
        else:
            name = level_of(k, lv) if lv != 'F' else k[2:]
            c = class_ids[lv].get(name)
            if c is None:
                c = class_ids[lv][name] = len(class_names[lv]); class_names[lv].append(name)
        m[rid] = c
    return c

def map_cls(rids, lv):
    u, inv = np.unique(rids, return_inverse=True)
    return np.array([cls_of(int(r), lv) for r in u], dtype=np.int64)[inv] if len(u) else np.zeros(0, np.int64)

def memberships(sub):
    """{(level, target): (state index array, class id array)} with (state, class) pairs unique"""
    st = load_states(sub); rt = Routes(sub)
    d, dv = st['d'], st['dvar']
    tstar = np.minimum(d, dv)
    out = {}
    for lv in LEVELS:
        cx = map_cls(rt.rid, lv)
        cv = map_cls(rt.vrid, lv)
        lx = d[rt.state] + rt.delta          # finish length via this route on X
        lvv = dv[rt.vstate] + rt.vdelta      # on X*R2
        for tg in TARGETS:
            if lv == 'F' and tg != 'opt':
                continue
            if lv == 'H' and tg in ('vopt', 'vp1'):
                continue
            if tg == 'opt': mx = rt.delta == 0; mv = np.zeros(len(cv), bool)
            elif tg == 'p1': mx = np.ones(len(cx), bool); mv = np.zeros(len(cv), bool)
            elif tg == 'vopt': mx = lx <= tstar[rt.state]; mv = lvv <= tstar[rt.vstate]
            else: mx = lx <= tstar[rt.state] + 1; mv = lvv <= tstar[rt.vstate] + 1
            mx &= cx >= 0; mv &= cv >= 0
            s = np.concatenate([rt.state[mx], rt.vstate[mv]]); c = np.concatenate([cx[mx], cv[mv]])
            pair = np.unique(s * (1 << 24) + c)
            out[(lv, tg)] = (pair >> 24, pair & ((1 << 24) - 1))
    # mean shortest HTR via each class among the states where it works at the optimum (cost proxy)
    hsum = {}
    for lv in ('C', 'H', 'Q'):
        cx = map_cls(rt.rid, lv)
        m = (rt.delta == 0) & (cx >= 0)
        # per (state, class) the shortest HTR
        key = rt.state[m] * (1 << 24) + cx[m]
        order = np.lexsort((rt.htr[m], key))
        k2, h2 = key[order], rt.htr[m][order]
        first = np.r_[True, k2[1:] != k2[:-1]]
        hsum[lv] = (k2[first] & ((1 << 24) - 1), h2[first])
    return st, out, hsum

def greedy(states, classes, w, steps=10, cand_best=40, kmax=4, lv='C'):
    """weighted greedy max coverage; returns [(class, marginal, cumulative)], and exact best coverage for k <= kmax
    over the top cand_best classes by single coverage"""
    W = w.sum()
    cov = np.bincount(classes, weights=w[states])
    covered = np.zeros(len(w), bool)
    seq = []
    cum = 0.0
    for _ in range(steps):
        m = ~covered[states]
        g = np.bincount(classes[m], weights=w[states[m]], minlength=len(cov))
        if not len(g) or g.max() <= 0: break
        top = np.nonzero(g >= g.max() - 1e-9)[0]          # deterministic tie-break, common.tie_rank
        best = int(min(top, key=lambda c: tie_rank(class_names[lv][c])))
        cum += g[best]
        seq.append((best, g[best] / W, cum / W, cov[best] / W))
        covered[states[classes == best]] = True
    top = np.argsort(-cov)[:cand_best]
    bits = []
    for c in top:
        b = np.zeros(len(w), bool); b[states[classes == c]] = True; bits.append(b)
    bestk = {}
    for k in range(1, kmax + 1):
        mm = top if k <= 2 else top[: (cand_best if k == 3 else 25)]
        best = (0, None)
        for comb in itertools.combinations(range(len(mm)), k):
            u = np.zeros(len(w), bool)
            for i in comb: u |= bits[i]
            v = w[u].sum()
            if v > best[0]: best = (v, [int(top[i]) for i in comb])
        bestk[k] = (best[0] / W, best[1])
    return seq, bestk, cov / W

def write_group(gname, members, q1, q2, q2b, levels):
    """members: list of (sub, mem, hs, n)"""
    offs = 0; parts = collections.defaultdict(list); ws = []; hparts = collections.defaultdict(list)
    for s, mem, hs, n in members:
        for key, (si, ci) in mem.items():
            if key[0] in levels:
                parts[key].append((si + offs, ci))
        for lv, (sc, h) in hs.items():
            hparts[lv].append((sc, h))
        ws.append(np.full(n, SIZE[s] / n))
        offs += n
    w = np.concatenate(ws)
    _mh_cache.clear()
    for lv in levels:
        shares = {}
        for tg in TARGETS:
            if (lv, tg) not in parts: continue
            si = np.concatenate([p[0] for p in parts[(lv, tg)]]); ci = np.concatenate([p[1] for p in parts[(lv, tg)]])
            shares[tg] = np.bincount(ci, weights=w[si], minlength=len(class_names[lv])) / w.sum()
            if lv != 'F':
                seq, bestk, alone = greedy(si, ci, w, steps=10 if tg in ('opt', 'p1') else 6, kmax=4 if lv != 'H' else 3, lv=lv)
                mh = mean_htr(hparts, lv, len(class_names[lv]))
                for i, (c, marg, cum, al) in enumerate(seq):
                    q2.write(f'{gname}\t{lv}\t{tg}\t{i + 1}\t{class_names[lv][c]}\t{marg:.4f}\t{cum:.4f}\t{al:.4f}\t{mh[c]:.2f}\n')
                for k, (v, bs) in bestk.items():
                    gc = seq[k - 1][2] if len(seq) >= k else (seq[-1][2] if seq else 0)
                    q2b.write(f'{gname}\t{lv}\t{tg}\t{k}\t{gc:.4f}\t{v:.4f}\t{" || ".join(class_names[lv][c] for c in bs)}\n')
        mh = mean_htr(hparts, lv, len(class_names[lv])) if lv != 'F' else None
        base = shares.get('p1', shares['opt'])
        for c in np.nonzero(base >= 0.002)[0]:
            vals = [shares[t][c] if t in shares else float('nan') for t in TARGETS]
            q1.write(f'{gname}\t{lv}\t{class_names[lv][c]}\t' + '\t'.join(f'{v:.4f}' for v in vals) +
                     f'\t{(mh[c] if mh is not None else float("nan")):.2f}\t{offs}\n')
    for f in (q1, q2, q2b): f.flush()

def main():
    t0 = time.time()
    q1 = open(os.path.join(OUT, 'q1_routes.tsv'), 'w')
    q1.write('group\tlevel\tclass\tshare_opt\tshare_p1\tshare_vopt\tshare_vp1\tmean_htr_at_opt\tn_states\n')
    q2 = open(os.path.join(OUT, 'q2_checklist.tsv'), 'w')
    q2.write('group\tlevel\ttarget\tstep\tclass\tmarginal\tcumulative\talone\tmean_htr_at_opt\n')
    q2b = open(os.path.join(OUT, 'q2_best.tsv'), 'w')
    q2b.write('group\tlevel\ttarget\tk\tgreedy_cumulative\tbest_possible\tbest_set\n')
    for g in CGROUPS:
        members = []
        for sub in [s for s in SUBS if CORNER(s) == g]:
            st, mem, hs = memberships(sub)
            n = len(st['d'])
            write_group(sub, [(sub, mem, hs, n)], q1, q2, q2b, ['C', 'Q', 'H', 'F'])
            members.append((sub, {k: v for k, v in mem.items() if k[0] in 'CQ'}, {k: v for k, v in hs.items() if k in 'CQ'}, n))
            print(f'{sub}: {n} states, {time.time() - t0:.0f}s', flush=True)
        if len(members) > 1:
            write_group(g, members, q1, q2, q2b, ['C', 'Q'])
        print(f'group {g} done {time.time() - t0:.0f}s', flush=True)

_mh_cache = {}
def mean_htr(hparts, lv, ncls):
    key = (id(hparts), lv)
    if key not in _mh_cache:
        sc = np.concatenate([p[0] for p in hparts[lv]]); h = np.concatenate([p[1] for p in hparts[lv]])
        s = np.bincount(sc, weights=h, minlength=ncls); c = np.bincount(sc, minlength=ncls)
        _mh_cache[key] = np.where(c > 0, s / np.maximum(c, 1), np.nan)
    return _mh_cache[key]

if __name__ == '__main__':
    main()
