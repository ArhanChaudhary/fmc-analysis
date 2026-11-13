#!/usr/bin/env python3
"""Independent recount of the section 9 / errata f counts for FakeMMAP's multi-qt lower bounds (T11503).

Written from FakeMMAP's messages, not from the study's Python: for every (state, corner path) at the optimum with
N >= 2 quarter turns, R' = the shortest 1q reduction a finish of that path needs, M = the optimum, and the four
families of bounds
    M >= (|S|(R'+1) - N + sum alpha) / (|S| - 1)        S in {0..N-1}, with 0 and N-1
    M >= 1 + R' + (A - N + sum alpha) / |S|             S in {0..N-2}, with 0 and N-2
    the same with B                                     S in {1..N-1}, with 1 and N-1
    the same with C                                     S in {1..N-2}, with 1 and N-2
(S meets every {j, j+1}; the sum is over i with i, i+1 both in S), once with alpha_i as printed and once with
alpha_(i+1).  A bound "fails" on a case when it asks for more than M although a finish of M moves on that path has
every window reduction >= R'.  Also the largest R as written is checked (never below the need), and the smallest-term
reading with the printed term 2 (share of cases where it is below the need).

Inputs: out/big/bound2.tsv (checked state by state by vhtr b2), out/q9_alpha.tsv (Lean: alpha_matches_study),
out/checks/htr48.tsv (Lean: htr48_matches_study).  Usage: recount_t11503.py"""
import csv, sys, itertools, collections, functools
from fractions import Fraction as F
B = '/data/fmc/htr-routes/research/'
SUB = ["0c0", "4a1", "4a2", "4b2", "0c3", "2c3", "4a3", "4b3", "0c4", "2c4", "4a4", "4b4", "2c5", "4b5"]
ALPHA = {}
for r in csv.DictReader(open(B + 'out/q9_alpha.tsv'), delimiter='\t'):
    ALPHA[r['path']] = [int(x) for x in r['alpha_0..alpha_N'].split(',')]
C = {}
for r in csv.DictReader(open(B + 'out/checks/htr48.tsv'), delimiter='\t'):
    C[r['subset']] = min(C.get(r['subset'], 99), int(r['htr_len']))

@functools.lru_cache(None)
def covers(lo, hi):
    """sets S of windows in lo..hi containing lo and hi and meeting every {j, j+1}"""
    if lo > hi: return ()
    out = []
    mid = list(range(lo + 1, hi))
    for bits in itertools.product((0, 1), repeat=len(mid)):
        S = [lo] + [m for m, b in zip(mid, bits) if b] + ([hi] if hi > lo else [])
        if all(b - a <= 2 for a, b in zip(S, S[1:])):
            out.append(tuple(S))
    return tuple(out)
@functools.lru_cache(None)
def minimal(lo, hi):
    """the covering sets with no smaller covering set inside (FakeMMAP: "You only need to consider minimal such S's")"""
    all_ = set(covers(lo, hi))
    return tuple(S for S in all_ if not any(S[:i] + S[i + 1:] in all_ for i in range(1, len(S) - 1)))
def esum(S, al, shift):
    s = set(S)
    return sum(al[i + shift] for i in S if i + 1 in s)

size = collections.Counter()
for line in open(B + 'verify/out/cosets_per_label.tsv'):
    lab, n = line.split('\t'); sb, e = lab.split()
    sb = '4c3' if sb in ('4a3', '4b3') else '4c4' if sb in ('4a4', '4b4') else sb
    size[f'{sb} {e}'] += int(n)
per = collections.defaultdict(lambda: collections.Counter())      # per subset x edges: sums for the weighted means
cases = 0
fail = collections.Counter(); fail1 = collections.Counter(); bysub = collections.Counter()
rmax_short = 0; printed_min_short = 0; derived_min_short = 0
with open(B + 'out/big/bound2.tsv') as f:
    hdr = f.readline().rstrip('\n').split('\t')
    ci = {h: i for i, h in enumerate(hdr)}
    for line in f:
        v = line.rstrip('\n').split('\t')
        sub, d, A, Bi = v[ci['subset']], int(v[ci['d']]), int(v[ci['htrN']]), int(v[ci['htrI']])
        Cc = C[sub]
        for cell in v[ci['cells']].split(';'):
            off, path, r1, r2, secs = cell.split(':')
            if off != '0': continue
            ids = path.split('-'); N = len(ids) - 1
            if N < 2: continue
            cases += 1
            al = ALPHA[' > '.join(SUB[int(i)] for i in ids)]
            Rp = int(r1); M = d
            s = [int(x) for x in secs.split(',')]
            assert len(s) == N + 1 and sum(s) + N == d and all(a >= b for a, b in zip(s, al)), (v[:3], cell, al)
            assert min(d - 1 - s[i] - s[i + 1] for i in range(N)) == Rp
            which = {0: None, 1: None}
            for shift in (0, 1):                       # 0: alpha_i as printed, 1: alpha_(i+1)
                for S in covers(0, N - 1):
                    if len(S) >= 2 and F(len(S) * (Rp + 1) - N + esum(S, al, shift), len(S) - 1) > M: which[shift] = which[shift] or 'first'
                for name, X, lo, hi in (('A', A, 0, N - 2), ('B', Bi, 1, N - 1), ('C', Cc, 1, N - 2)):
                    for S in covers(lo, hi):
                        if 1 + Rp + F(X - N + esum(S, al, shift), len(S)) > M: which[shift] = which[shift] or name
            if which[0]: fail[which[0]] += 1; bysub[sub.split()[0]] += 1
            if which[1]: fail1[which[1]] += 1
            # the upper bound R: terms 1-5 (floors), as printed and as derived
            def terms(printed, covers=covers):
                sh = 0 if printed else 1
                t = [M - al[i] - al[i + 1] - 1 for i in range(N)]
                for S in covers(0, N - 1):
                    k = len(S)
                    num = (k - 1) * M - (N - k) + esum(S, al, sh) if printed else (k - 1) * M + (N - k) - esum(S, al, sh)
                    t.append(num // k)
                for X, lo, hi in ((A, 0, N - 2), (Bi, 1, N - 1), (Cc, 1, N - 2)):
                    for S in covers(lo, hi):
                        k = len(S)
                        t.append((k * M - (X - (N - k) + esum(S, al, sh))) // k)
                return t
            tp, td = terms(True), terms(False)
            if max(tp) < Rp: rmax_short += 1
            if min(tp) < Rp: printed_min_short += 1
            if min(td) < Rp: derived_min_short += 1
            a = per[sub]
            a['n'] += 1; a['written'] += max(tp); a['no_term1'] += max(tp[N:]); a['smallest'] += min(td); a['need'] += Rp
            tm, tdm = terms(True, minimal), terms(False, minimal)
            a['written_minimal_S'] += max(tm); a['no_term1_minimal_S'] += max(tm[N:]); a['smallest_minimal_S'] += min(tdm)
            a['printed_short_minimal_S'] += min(tm) < Rp
            a['printed_short'] += min(tp) < Rp
print('cases (state, path, N >= 2) at the optimum:', cases)
print('lower bounds as printed (alpha_i) fail:', sum(fail.values()), dict(fail), 'by corner subset', dict(bysub))
print('lower bounds with alpha_(i+1) fail:', sum(fail1.values()), dict(fail1))
print('R as written (largest term) below the need:', rmax_short)
print('smallest term, as printed (term 2 signs, alpha_i) below the need:', printed_min_short, f'{100 * printed_min_short / cases:.1f}%')
print('smallest term, derived (alpha_(i+1)) below the need:', derived_min_short)
W = sum(a['n'] * size[c] for c, a in per.items())
for k in ('written', 'no_term1', 'smallest', 'need', 'printed_short', 'written_minimal_S', 'no_term1_minimal_S', 'smallest_minimal_S', 'printed_short_minimal_S'):
    raw = sum(a[k] for a in per.values()) / cases
    wtd = sum(a[k] * size[c] for c, a in per.items()) / W
    print(f'{k}: mean over the cases {raw:.4f}; each case weighted by the size of its subset x edges {wtd:.4f}')
