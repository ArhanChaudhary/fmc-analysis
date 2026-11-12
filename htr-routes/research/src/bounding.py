#!/usr/bin/env python3
"""Questions 8 and 9: DR bounding as a route, and FakeMMAP's reduction-length bound (T11501-T11504).

Input: out/big/bound.tsv (htrtools bound: the same 25,000 states per subset as the main pass; per state and per
(finish length - optimum, number of quarter turns N): the shortest reduction to 1q and to 2q over all finishes of
that length with N quarter turns, and the sections s_0..s_N of a finish achieving the 1q minimum);
out/big/redcount.tsv (htrtools redcount: 300 states per subset, number of reductions a solver writes of each
length r <= 5); out/checks/htr48.tsv (C = shortest HTR in the subset; also our per-state shortest NISS HTR).

Reading a finish as DR bounding: its N quarter turns cut it into sections s_0..s_N of half turns.  Keeping one
quarter turn q with the sections around it as the 1q finish, the rest (a prefix done on normal, a suffix on inverse)
is the reduction to 1q, of length len - 1 - s_{q-1} - s_q; the best choice of q gives the shortest reduction that
finds this finish.  To 2q the same with two consecutive quarter turns.  "Checking all reductions to 1q of length
<= R finds a finish of length <= M" = some finish of length <= M has a 1q reduction of length <= R (and the solver
then finishes each reduced state optimally with one quarter turn).

FakeMMAP's bound (T11502), with sections numbered 0..N and alpha_i a lower bound on section i, A / B the shortest
HTR on normal / inverse, C the shortest HTR in the subset: R is the max of
  (1) M - alpha_i - alpha_{i+1} - 1
  (2) ((|S|-1) M - (N - |S|) + sum alpha) / |S|, S subset of {0..N-1} with 0, N-1 in S, no two consecutive missing
  (3) M - (A - (N - |S|) + sum alpha) / |S|, S subset of {0..N-2} with 0, N-2 in S, same covering rule
  (4) the same with B, S subset of {1..N-1} with 1, N-1;   (5) the same with C, S subset of {1..N-2} (dropped if N=2)
implemented literally (minimal S only, then all S), with alpha = 0 (the only value valid for every subset).
Our exact version of the same model: R*(M, N, A, B, C) = max over integer sections s_i >= 0 with N + sum s <= M,
len - s_N >= A (linear HTR on normal), len - s_0 >= B (inverse), len - s_j >= C for 0 < j < N (a NISS HTR whose
post-HTR part is section j) of the shortest reduction min_q (len - 1 - s_{q-1} - s_q).
T11503 lower bounds after all reductions shorter than R' failed: M >= (|S|(R'+1) - N + sum alpha) / (|S| - 1) and
M >= 1 + R' + (A - N + sum alpha) / |S| (B, C alike); our exact version: the shortest len over the same sections with
every reduction >= R'.

Outputs: out/q8_bounding.tsv, out/q8_reduction_counts.tsv, out/q9_fakemmap.tsv, out/q9_counterexamples.tsv,
out/q9_tables.tsv (R per subset class, N, M, A, B for rodneykinney's request)."""
import csv, collections, itertools, functools, math, os
import numpy as np
from common import *

def load_bound():
    rows = collections.defaultdict(list)
    for r in csv.DictReader(open(f'{R}/out/big/bound.tsv'), delimiter='\t'):
        cells = {}
        for c in r['cells'].split(';') if r['cells'] else []:
            dl, nq, r1, r2, sec = c.split(':')
            cells[(int(dl), int(nq))] = (int(r1), int(r2), [int(x) for x in sec.split(",") if x])
        rows[r['subset']].append((int(r['d']), int(r['htrN']), int(r['htrI']), cells))
    return rows

NISS = {s: load_states(s)['htrNiss'] for s in SUBS}   # same states, same order as bound.tsv

C_SUB = {}
for r in csv.DictReader(open(f'{R}/out/checks/htr48.tsv'), delimiter='\t'):
    C_SUB[r['subset']] = min(C_SUB.get(r['subset'], 99), int(r['htr_len']))

def red_needed(cells, maxdl, q):
    """shortest reduction to q quarter turns over finishes of length <= optimum + maxdl (99 if none)"""
    v = [c[q - 1] for (dl, nq), c in cells.items() if dl <= maxdl]
    v = [x if x < 99 else 99 for x in v]
    # a finish with no quarter turn (the state is in HTR) needs no reduction
    if any(nq == 0 for (dl, nq) in cells if dl <= maxdl): v.append(0)
    return min(v) if v else 99

# ------------------------------------------------------------------ Q8
def q8(B):
    out = open(f'{OUT}/q8_bounding.tsv', 'w')
    out.write('group\ttarget\tq\tn_states\tshare_target_reachable\t' + '\t'.join(f'R<={r}' for r in range(0, 11)) + '\tmean_R_needed\tmedian_R_needed\tR_needed_p90\tR_needed_max\n')
    groups = [(s, [s]) for s in SUBS] + [(g, [s for s in SUBS if CORNER(s) == g]) for g in CGROUPS] + [('all', SUBS)]
    for g, subs in groups:
        for tg in ['opt', 'p1', 'M10', 'M11', 'M12', 'M13']:
            for q in (1, 2):
                vals = []; ws = []; reach = []
                for s in subs:
                    w = SIZE[s] / len(B[s])
                    for d, A, Bv, cells in B[s]:
                        if tg == 'opt': mdl = 0
                        elif tg == 'p1': mdl = 1
                        else:
                            M = int(tg[1:])
                            if M < d: reach.append((0, w)); vals.append(99); ws.append(w); continue
                            mdl = min(M - d, 1)   # M >= d + 2 uses the +1 finishes: an upper bound on the R needed
                        reach.append((1, w)); vals.append(red_needed(cells, mdl, q)); ws.append(w)
                v = np.array(vals); w = np.array(ws)
                ok = v < 99
                cum = [(w[v <= r].sum() / w.sum()) for r in range(0, 11)]
                vv = v[ok]; wv = w[ok]
                if len(vv):
                    o = np.argsort(vv); c = np.cumsum(wv[o]) / wv.sum()
                    med = vv[o][np.searchsorted(c, 0.5)]; p90 = vv[o][np.searchsorted(c, 0.9)]
                    mean = (vv * wv).sum() / wv.sum(); mx = vv.max()
                else: med = p90 = mean = mx = float('nan')
                reachable = sum(x * ww for x, ww in reach) / sum(ww for _, ww in reach)
                out.write(f'{g}\t{tg}\t{q}\t{len(v)}\t{reachable:.4f}\t' + '\t'.join(f'{x:.4f}' for x in cum) +
                          f'\t{mean:.3f}\t{med}\t{p90}\t{mx}\n')

def q8_counts():
    if not os.path.exists(f'{R}/out/big/redcount.tsv'): return
    acc = collections.defaultdict(lambda: collections.defaultdict(list))
    for r in csv.DictReader(open(f'{R}/out/big/redcount.tsv'), delimiter='\t'):
        acc[(r['subset'], int(r['target_q']))][int(r['r'])].append((int(r['pairs']), int(r['states'])))
    out = open(f'{OUT}/q8_reduction_counts.tsv', 'w')
    out.write('subset\ttarget_q\tr\tn_states\tmean_pairs_of_length_r\tmean_cumulative_pairs_le_r\tmean_distinct_states_le_r_upper\tshare_with_some_reduction_le_r\n')
    for (s, q), byr in sorted(acc.items()):
        n = len(byr[0])
        cum = np.zeros(n); cums = np.zeros(n)
        for r in sorted(byr):
            p = np.array([x[0] for x in byr[r]]); st = np.array([x[1] for x in byr[r]])
            cum += p; cums += st
            out.write(f'{s}\t{q}\t{r}\t{n}\t{p.mean():.2f}\t{cum.mean():.2f}\t{cums.mean():.2f}\t{(cum > 0).mean():.4f}\n')

# ------------------------------------------------------------------ Q9
def covering_sets(lo, hi, minimal):
    """subsets S of {lo..hi} with lo, hi in S and no two consecutive elements both missing"""
    el = list(range(lo, hi + 1))
    out = []
    for mask in range(1 << len(el)):
        S = [el[i] for i in range(len(el)) if mask >> i & 1]
        if lo not in S or hi not in S: continue
        if any(j not in S and j + 1 not in S for j in range(lo, hi)): continue
        out.append(frozenset(S))
    if minimal:
        out = [S for S in out if not any(T < S for T in out)]
    return out

def edge_sum(S, alpha):
    return sum(alpha[i] for i in S if i + 1 in S)

@functools.lru_cache(maxsize=None)
def fake_R(M, N, A, B, C, minimal=True, term1=True):
    alpha = [0] * (N + 1)
    cands = []
    if term1:
        cands += [M - alpha[i] - alpha[i + 1] - 1 for i in range(N)]
    for S in covering_sets(0, N - 1, minimal):
        if len(S) > 0:
            cands.append(((len(S) - 1) * M - (N - len(S)) + edge_sum(S, alpha)) / len(S))
    if N >= 2:
        for S in covering_sets(0, N - 2, minimal):
            cands.append(M - (A - (N - len(S)) + edge_sum(S, alpha)) / len(S))
        for S in covering_sets(1, N - 1, minimal):
            cands.append(M - (B - (N - len(S)) + edge_sum(S, alpha)) / len(S))
    if N > 2:
        for S in covering_sets(1, N - 2, minimal):
            cands.append(M - (C - (N - len(S)) + edge_sum(S, alpha)) / len(S))
    return math.floor(max(cands) + 1e-9)

def compositions(total, parts):
    if parts == 1:
        yield (total,); return
    for i in range(total + 1):
        for rest in compositions(total - i, parts - 1):
            yield (i,) + rest

@functools.lru_cache(maxsize=None)
def exact_R(M, N, A, B, C):
    """max over feasible sections of the shortest 1q reduction; -1 if no section vector is feasible"""
    best = -1
    for L in range(N, M + 1):
        for s in compositions(L - N, N + 1):
            if L - s[N] < A or L - s[0] < B: continue
            if any(L - s[j] < C for j in range(1, N)): continue
            red = min(L - 1 - s[q - 1] - s[q] for q in range(1, N + 1))
            best = max(best, red)
    return best

@functools.lru_cache(maxsize=None)
def exact_LB(Rp, N, A, B, C, Mmax=20):
    """shortest finish length L with N qts consistent with A, B, C whose every 1q reduction is >= Rp"""
    for L in range(N, Mmax + 1):
        for s in compositions(L - N, N + 1):
            if L - s[N] < A or L - s[0] < B: continue
            if any(L - s[j] < C for j in range(1, N)): continue
            if min(L - 1 - s[q - 1] - s[q] for q in range(1, N + 1)) >= Rp: return L
    return 99

def fake_LB(Rp, N, A, B, C):
    """T11503 bounds (alpha = 0), with the trivial ones M >= A, M >= B"""
    v = [A, B]
    if N >= 2:
        for S in covering_sets(0, N - 1, True):
            if len(S) > 1: v.append((len(S) * (Rp + 1) - N) / (len(S) - 1))
        for S in covering_sets(0, N - 2, True):
            v.append(1 + Rp + (A - N) / len(S))
        for S in covering_sets(1, N - 1, True):
            v.append(1 + Rp + (B - N) / len(S))
        if N > 2:
            for S in covering_sets(1, N - 2, True):
                v.append(1 + Rp + (C - N) / len(S))
    return math.ceil(max(v) - 1e-9)

def q9(B):
    out = open(f'{OUT}/q9_fakemmap.tsv', 'w')
    out.write('group\ttarget\tn_cases\tfake_literal_insufficient\tfake_without_term1_insufficient\texact_C_niss_insufficient\t'
              'exact_C_linear_insufficient\tmean_R_fake_literal\tmean_R_fake_without_term1\tmean_R_exact\tmean_R_needed\t'
              'R_needed_max\tLB_fake_valid\tLB_fake_beats_trivial\tLB_exact_beats_trivial\n')
    cex = open(f'{OUT}/q9_counterexamples.tsv', 'w')
    cex.write('subset\tidx\tversion\tM\tN\tA\tB\tC\tR_bound\tR_needed_for_N\tsections_of_finish\n')
    groups = [(s, [s]) for s in SUBS] + [('all', SUBS)]
    allres = {}
    for s in SUBS:
        C = C_SUB[s]
        res = collections.defaultdict(list)
        for idx, (d, A, Bv, cells) in enumerate(B[s]):
            Cn = int(NISS[s][idx])
            for tg, mdl in (('opt', 0), ('p1', 1)):
                M = d + mdl
                for N in sorted({nq for (dl, nq) in cells if dl <= mdl and nq >= 2}):
                    need = min(c[0] for (dl, nq), c in cells.items() if dl <= mdl and nq == N)
                    sec = next(c[2] for (dl, nq), c in cells.items() if dl <= mdl and nq == N and c[0] == need)
                    rl = fake_R(M, N, A, Bv, C, True, True); rn = fake_R(M, N, A, Bv, C, True, False)
                    re_ = exact_R(M, N, A, Bv, Cn); rc = exact_R(M, N, A, Bv, C)
                    res[tg].append((need > rl, need > rn, need > re_, need > rc, rl, rn, re_, need))
                    for ver, rb, cc in (('fake_literal', rl, C), ('fake_without_term1', rn, C), ('exact_C_niss', re_, Cn), ('exact_C_linear', rc, C)):
                        if need > rb:
                            cex.write(f'{s}\t{idx}\t{ver}\t{M}\t{N}\t{A}\t{Bv}\t{cc}\t{rb}\t{need}\t{",".join(map(str, sec))}\n')
        allres[s] = res
    # lower bounds, per state: every reduction shorter than R' (= what the optimal needs with its N) found nothing
    lb = {}
    for s in SUBS:
        C = C_SUB[s]; v = []; ok = []; beat = []; beat_e = []
        for idx, (d, A, Bv, cells) in enumerate(B[s]):
            for (dl, N), c in cells.items():
                if dl != 0 or N < 2: continue
                Rp = c[0]
                f = fake_LB(Rp, N, A, Bv, C); e = exact_LB(Rp, N, A, Bv, int(NISS[s][idx]))
                ok.append(f <= d); beat.append(f > max(A, Bv)); beat_e.append(e > max(A, Bv))
        lb[s] = (np.mean(ok), np.mean(beat), np.mean(beat_e))
    for g, subs in groups:
        for tg in ('opt', 'p1'):
            rows = [x for s in subs for x in allres[s][tg]]
            if not rows: continue
            a = np.array(rows, dtype=float)
            emp = max(x[7] for x in rows)
            lbv = [lb[s] for s in subs]
            out.write(f'{g}\t{tg}\t{len(rows)}\t{a[:, 0].mean():.4f}\t{a[:, 1].mean():.4f}\t{a[:, 2].mean():.4f}\t{a[:, 3].mean():.4f}\t'
                      f'{a[:, 4].mean():.2f}\t{a[:, 5].mean():.2f}\t{a[:, 6].mean():.2f}\t{a[:, 7].mean():.2f}\t{emp}\t'
                      f'{np.mean([x[0] for x in lbv]):.4f}\t{np.mean([x[1] for x in lbv]):.4f}\t{np.mean([x[2] for x in lbv]):.4f}\n')
    # rodneykinney's tables: R for each N, M, A, B with C fixed per subset
    t = open(f'{OUT}/q9_tables.tsv', 'w')
    t.write('C\tN\tM\tA\tB\tR_fake_without_term1\tR_exact\n')
    for C in sorted(set(C_SUB.values())):
        for N in (2, 3, 4, 5):
            for M in range(10, 15):
                for A in range(C, 12):
                    for Bv in range(C, 12):
                        if Bv < A: continue
                        t.write(f'{C}\t{N}\t{M}\t{A}\t{Bv}\t{fake_R(M, N, A, Bv, C, True, False)}\t{exact_R(M, N, A, Bv, C)}\n')

if __name__ == '__main__':
    B = load_bound()
    q8(B); q8_counts(); q9(B)
    print('done')
