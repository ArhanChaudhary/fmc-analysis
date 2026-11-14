#!/usr/bin/env python3
"""Adaptive budgets by scramble features: per feature bucket, the policy with the best training score; the composite
(each scramble played by its bucket's policy) against the best single policy, both chosen on the training scrambles
and judged on the held-out ones (paired, same scrambles).  usage: adaptive.py TRAIN_GLOB TEST_GLOB [REF]"""
import sys, glob, collections
import simstats as S, tables as T

def run(train, test, ref='base', cands=None, quiet=False):
    tr = S.load(sorted(glob.glob(train)), *T.TRAIN); te = S.load(sorted(glob.glob(test)), *T.TEST)
    cands = [p for p in tr if p in te and (cands is None or p in cands)]
    sc = lambda by, p, ss: sum(S.score(by[p][s]) for s in ss) / len(ss)
    trs = list(tr[ref]); tes = list(te[ref])
    best_fixed = min(cands, key=lambda p: sc(tr, p, trs))
    out = {}
    for fname in T.FEATURES:
        btr = collections.defaultdict(list); bte = collections.defaultdict(list)
        for s in trs: btr[T.bucket_of(tr[ref][s], fname)].append(s)
        for s in tes: bte[T.bucket_of(te[ref][s], fname)].append(s)
        choice = {b: min(cands, key=lambda p: sc(tr, p, ss)) for b, ss in btr.items()}
        # held-out: composite against the best fixed policy, and against the reference
        d_fixed = [S.score(te[choice[b]][s]) - S.score(te[best_fixed][s]) for b, ss in bte.items() for s in ss]
        d_ref = [S.score(te[choice[b]][s]) - S.score(te[ref][s]) for b, ss in bte.items() for s in ss]
        rows = []
        for b in [lab for _, lab in T.FEATURES[fname][1]]:
            ss = bte.get(b, [])
            if not ss: continue
            dd = [S.score(te[choice[b]][s]) - S.score(te[best_fixed][s]) for s in ss]
            rows.append((b, len(ss), choice[b], sc(te, choice[b], ss), sc(te, best_fixed, ss), *S.mse(dd)))
        out[fname] = dict(rows=rows, d_fixed=S.mse(d_fixed), d_ref=S.mse(d_ref))
        if not quiet:
            m, se = S.mse(d_fixed)
            print(f'== {fname}: composite − best fixed ({best_fixed}) on held-out: {m:+.3f} ± {se:.3f}; composite − {ref}: {S.mse(d_ref)[0]:+.3f} ± {S.mse(d_ref)[1]:.3f}')
            for r in rows: print(f'   {r[0]:45s} n {r[1]:5d}  {r[2]:28s} {r[3]:.3f} vs fixed {r[4]:.3f}  d {r[5]:+.3f} ± {r[6]:.3f}')
    return best_fixed, out

if __name__ == '__main__':
    a = sys.argv[1:]
    run(a[0], a[1], a[2] if len(a) > 2 else 'base')
