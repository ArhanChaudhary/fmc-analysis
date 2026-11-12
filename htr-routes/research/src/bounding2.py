#!/usr/bin/env python3
"""Questions 8 and 9 redone (coordinator follow-up), and the half-turn claims C11 / C13.

Inputs:
  out/big/bound2.tsv      htrtools bound2: 25,000 states per subset (the states of the main pass); per state the
                          finishes up to max(opt + 1, min(opt + 2, 12)) moves, grouped by (length - opt, corner path
                          read on normal): shortest reduction to 1q and to 2q, sections of the finish achieving the 1q
                          one; trigger flags (C11) and switch positions of the shortest-HTR readings (C13)
  out/big/redcount2.tsv   htrtools redcount2: the first 4,000 of those states per subset; number of reductions to 1q
                          / 2q of each length r <= 7 a solver writes (pairs A on normal, B on inverse, each empty or
                          ending in a quarter turn), counted exactly (checked against brute force on 4,800 states)
  htrtools alpha          FakeMMAP's alpha_i for each corner path: fewest half turns section i must have over every
                          corner permutation following the path (alpha_1 = 3 for 4a3 > 4b2 > 4a1, as in T11501)
Q9 (T11502 as written, alpha from the path, the alpha sum over i with i and i+1 in S):
  R_lit (all five terms), R_no1 (without term 1), R_exact (max over integer sections s_i >= alpha_i of the shortest 1q
  reduction under the same constraints; C as stated = shortest linear HTR of the subset, and C = the state's
  shortest NISS HTR).  Sufficiency per (state, path, M): the reduction a finish of that path and length <= M needs
  vs R.  Per state, not knowing the path: R_state = max over the (N, alpha) of the subset's paths.
Outputs: out/q8_bounding_v2.tsv, out/q8_vs_checklist.tsv, out/q9_v2.tsv, out/q9_v2_counterexamples.tsv,
out/q9_rodney_table.tsv, out/q9_alpha.tsv, out/c11_c13.tsv"""
import csv, collections, functools, itertools, math, subprocess, os, sys
import numpy as np
from common import *
from bounding import covering_sets
TOOL = os.environ.get('HTRTOOLS', f'{R}/htrtools/target/release/htrtools')
NAMES = ["0c0", "4a1", "4a2", "4b2", "0c3", "2c3", "4a3", "4b3", "0c4", "2c4", "4a4", "4b4", "2c5", "4b5"]
C_LIN = {}
for r in csv.DictReader(open(f'{R}/out/checks/htr48.tsv'), delimiter='\t'):
    C_LIN[r['subset']] = min(C_LIN.get(r['subset'], 99), int(r['htr_len']))
TARGETS = ['opt', 'p1', 'M10', 'M11', 'M12']

def load():
    B = {}
    paths = set()
    for r in csv.DictReader(open(f'{R}/out/big/bound2.tsv'), delimiter='\t'):
        cells = []
        for c in r['cells'].split(';') if r['cells'] else []:
            dl, p, r1, r2, sec = c.split(':')
            cells.append((int(dl), p, int(r1), int(r2), tuple(int(x) for x in sec.split(',') if x)))
            paths.add(p)
        B.setdefault(r['subset'], []).append(dict(r, cells=cells))
    return B, paths

def alphas(paths):
    p = subprocess.run([TOOL, 'alpha'], input='\n'.join(sorted(paths)) + '\n', capture_output=True, text=True, check=True)
    out = {}
    for l in p.stdout.strip().split('\n'):
        k, a, f = l.split('\t')
        out[k] = tuple(int(x) for x in a.split(','))
    return out

def target_dl(tg, d, budget):
    """largest (length - optimum) a target allows; None if the target is below the optimum"""
    if tg == 'opt': return 0
    if tg == 'p1': return 1
    M = int(tg[1:])
    if M < d: return None
    return min(M - d, budget - d)

# ------------------------------------------------------------------ formulas
@functools.lru_cache(maxsize=None)
def cov(lo, hi):
    return covering_sets(lo, hi, True) if hi >= lo else []
def esum(S, al):
    return sum(al[i] for i in S if i + 1 in S)

@functools.lru_cache(maxsize=None)
def R_fake(M, N, al, A, B, C, term1=True):
    c = []
    if term1: c += [M - al[i] - al[i + 1] - 1 for i in range(N)]
    for S in cov(0, N - 1): c.append(((len(S) - 1) * M - (N - len(S)) + esum(S, al)) / len(S))
    if N >= 2:
        for S in cov(0, N - 2): c.append(M - (A - (N - len(S)) + esum(S, al)) / len(S))
        for S in cov(1, N - 1): c.append(M - (B - (N - len(S)) + esum(S, al)) / len(S))
    if N > 2:
        for S in cov(1, N - 2): c.append(M - (C - (N - len(S)) + esum(S, al)) / len(S))
    return math.floor(max(c) + 1e-9)

@functools.lru_cache(maxsize=None)
def comps(T, parts):
    """all compositions of T into `parts` non-negative parts, as an array"""
    if T < 0: return np.zeros((0, parts), int)
    rows = []
    for bars in itertools.combinations(range(T + parts - 1), parts - 1):
        prev = -1; r = []
        for b in bars: r.append(b - prev - 1); prev = b
        r.append(T + parts - 2 - prev); rows.append(r)
    return np.array(rows, int).reshape(-1, parts)

@functools.lru_cache(maxsize=None)
def R_exact(M, N, al, A, B, C):
    best = -1
    al_ = np.array(al)
    for L in range(N + sum(al), M + 1):
        s = comps(L - N - sum(al), N + 1) + al_
        if not len(s): continue
        ok = (L - s[:, N] >= A) & (L - s[:, 0] >= B)
        for j in range(1, N): ok &= L - s[:, j] >= C
        if not ok.any(): continue
        s = s[ok]
        red = np.min(np.stack([L - 1 - s[:, q - 1] - s[:, q] for q in range(1, N + 1)], 1), 1)
        best = max(best, int(red.max()))
    return best

@functools.lru_cache(maxsize=None)
def LB_exact(Rp, N, al, A, B, C, Mmax=22):
    al_ = np.array(al)
    for L in range(N + sum(al), Mmax + 1):
        s = comps(L - N - sum(al), N + 1) + al_
        if not len(s): continue
        ok = (L - s[:, N] >= A) & (L - s[:, 0] >= B)
        for j in range(1, N): ok &= L - s[:, j] >= C
        red = np.min(np.stack([L - 1 - s[:, q - 1] - s[:, q] for q in range(1, N + 1)], 1), 1)
        if (ok & (red >= Rp)).any(): return L
    return 99

def LB_fake(Rp, N, al, A, B, C):
    v = [A + al[N], B + al[0]]
    for S in cov(0, N - 1):
        if len(S) > 1: v.append((len(S) * (Rp + 1) - N + esum(S, al)) / (len(S) - 1))
    for S in cov(0, N - 2): v.append(1 + Rp + (A - N + esum(S, al)) / len(S))
    for S in cov(1, N - 1): v.append(1 + Rp + (B - N + esum(S, al)) / len(S))
    if N > 2:
        for S in cov(1, N - 2): v.append(1 + Rp + (C - N + esum(S, al)) / len(S))
    return math.ceil(max(v) - 1e-9)

# ------------------------------------------------------------------ main
def main():
    B, paths = load()
    AL = alphas(paths)
    with open(f'{OUT}/q9_alpha.tsv', 'w') as f:
        f.write('path\tN\talpha_0..alpha_N\n')
        for p in sorted(AL, key=lambda x: (len(x), x)):
            f.write(f"{' > '.join(NAMES[int(i)] for i in p.split('-'))}\t{len(p.split('-')) - 1}\t{','.join(map(str, AL[p]))}\n")
    RC = {}
    for r in csv.DictReader(open(f'{R}/out/big/redcount2.tsv'), delimiter='\t'):
        RC[(r['subset'], int(r['idx']))] = r
    rmax = 7
    def cum(r, q, R_):
        return sum(int(r[f'q{q}_r{k}']) for k in range(0, min(R_, rmax) + 1))

    q8 = open(f'{OUT}/q8_bounding_v2.tsv', 'w')
    q8.write('group\tq\tR\tn_states\tmean_reductions_le_R\tse_reductions\t' + '\t'.join(f'found_{t}\tse_{t}' for t in TARGETS) + '\n')
    q9 = open(f'{OUT}/q9_v2.tsv', 'w')
    q9.write('subset\ttarget\tcases_state_path\tinsuff_literal\tinsuff_no_term1\tinsuff_exact_Clin\tinsuff_exact_Cniss\t'
             'mean_R_literal\tmean_R_no_term1\tmean_R_exact_Cniss\tmean_R_needed\tp50_needed\tp90_needed\tmax_needed\t'
             'states\tstate_insuff_no_term1\tstate_insuff_exact_Cniss\tmean_Rstate_literal\tmean_Rstate_no_term1\tmean_Rstate_exact_Cniss\t'
             'R_empirical_max\tskip_vs_empirical_no_term1\tskip_vs_empirical_exact\tLB_valid\tLB_beats_trivial\tLB_exact_beats_trivial\tLB_reaches_opt\n')
    cex = open(f'{OUT}/q9_v2_counterexamples.tsv', 'w')
    cex.write('subset\tidx\tversion\tM\tpath\tN\talpha\tA\tB\tC\tR_bound\tR_needed\tsections\n')
    rod = open(f'{OUT}/q9_rodney_table.tsv', 'w')
    rod.write('subset\tM_minus_opt_or_M\tR_no_term1_worst_case\tR_exact_worst_case_Cniss\tR_no_term1_mean_with_own_A_B\tR_exact_mean_with_own_A_B\tR_needed_p90\tR_needed_max\tpaths_used\n')
    c11 = open(f'{OUT}/c11_c13.tsv', 'w')
    c11.write('group\tn\tsome_opt_ends_qt_ht_qt\teither_end_qt_ht_qt\trandom_opt_ends_qt_ht_qt\tsome_opt_ends_RU2Rp\teither_end_RU2Rp\trandom_opt_ends_RU2Rp\t'
              'shortest_htr_needs_switch_after_gt2\tshortest_htr_needs_switch_after_gt3\tbudget2_needs_switch_after_gt2\tbudget2_needs_switch_after_gt3\n')

    acc8 = collections.defaultdict(lambda: collections.defaultdict(list))
    acc11 = collections.defaultdict(list)
    for sub in SUBS:
        rows = B[sub]; w = SIZE[sub] / len(rows)
        Cl = C_LIN[sub]
        Cn_min = min(int(r['niss']) for r in rows)   # shortest NISS HTR seen in the subset's sample
        # 11 / 13
        for r in rows:
            acc11[sub].append([int(r['trig_end_normal']), int(r['trig_either_end']), float(r['trig_frac_canon']),
                               int(r['rur_end_normal']), int(r['rur_either_end']), float(r['rur_frac_canon']),
                               int(r['linear_at_best'] == '0' and int(r['minfirst_at_best']) > 2),
                               int(r['linear_at_best'] == '0' and int(r['minfirst_at_best']) > 3),
                               int(r['linear_at_b2'] == '0' and int(r['minfirst_at_b2']) > 2),
                               int(r['linear_at_b2'] == '0' and int(r['minfirst_at_b2']) > 3)])
        for tg in TARGETS:
            sigs = set()
            per = []
            for r in rows:
                d = int(r['d']); budget = max(d + 1, min(d + 2, 12))
                mdl = target_dl(tg, d, budget)
                if mdl is None: continue
                M = d + mdl
                A, Bv, Cn = int(r['htrN']), int(r['htrI']), int(r['niss'])
                need_path = {}
                for dl, p, r1, r2, sec in r['cells']:
                    if dl <= mdl:
                        if p not in need_path or r1 < need_path[p][0]: need_path[p] = (r1, sec, r2)
                need1 = min([v[0] for v in need_path.values()] or [99]); need2 = min([v[2] for v in need_path.values()] or [99])
                if any(len(p.split('-')) == 1 for p in need_path): need1 = need2 = 0
                per.append((r, M, A, Bv, Cn, need_path, need1, need2))
                for p in need_path:
                    N = len(p.split('-')) - 1
                    if N >= 2: sigs.add((N, AL[p]))
            # Q8 accumulation
            for (r, M, A, Bv, Cn, need_path, need1, need2) in per:
                key = (sub, int(r['idx']))
                if key in RC:
                    acc8[(sub, tg)]['n1'].append(need1); acc8[(sub, tg)]['n2'].append(need2)
                    acc8[(sub, tg)]['rc'].append(RC[key])
            # Q9 per (state, path)
            res = []; st_res = []; lbs = []
            emp = max([x[6] for x in per if x[6] < 99] or [0])
            for (r, M, A, Bv, Cn, need_path, need1, need2) in per:
                for p, (nd, sec, _) in need_path.items():
                    N = len(p.split('-')) - 1
                    if N < 2: continue
                    al = AL[p]
                    rl = R_fake(M, N, al, A, Bv, Cl, True); rn = R_fake(M, N, al, A, Bv, Cl, False)
                    rec = R_exact(M, N, al, A, Bv, Cl) if N <= 8 else 99
                    ren = R_exact(M, N, al, A, Bv, Cn) if N <= 8 else 99
                    res.append((nd > rl, nd > rn, nd > rec, nd > ren, rl, rn, ren, nd))
                    for ver, rb, cc in (('literal', rl, Cl), ('no_term1', rn, Cl), ('exact_C_linear', rec, Cl), ('exact_C_niss', ren, Cn)):
                        if nd > rb:
                            cex.write(f"{sub}\t{r['idx']}\t{ver}\t{M}\t{' > '.join(NAMES[int(i)] for i in p.split('-'))}\t{N}\t{','.join(map(str, al))}\t{A}\t{Bv}\t{cc}\t{rb}\t{nd}\t{','.join(map(str, sec))}\n")
                    if tg == 'opt' and N <= 8:
                        lf = LB_fake(nd, N, al, A, Bv, Cl); le = LB_exact(nd, N, al, A, Bv, Cn)
                        triv = max(A + al[N], Bv + al[0])
                        lbs.append((lf <= M, lf > triv, le > triv, max(lf, le) >= M))
                # per state: the path is unknown
                rs_l = max([R_fake(M, N, al, A, Bv, Cl, True) for N, al in sigs] or [0])
                rs_n = max([R_fake(M, N, al, A, Bv, Cl, False) for N, al in sigs] or [0])
                rs_e = max([R_exact(M, N, al, A, Bv, Cn) for N, al in sigs if N <= 8] or [0])
                skip_n = skip_e = None
                key = (sub, int(r['idx']))
                if key in RC:
                    ce = cum(RC[key], 1, emp)
                    if ce > 0:
                        skip_n = 1 - cum(RC[key], 1, rs_n) / ce; skip_e = 1 - cum(RC[key], 1, rs_e) / ce
                st_res.append((need1 > rs_n, need1 > rs_e, rs_l, rs_n, rs_e, skip_n, skip_e, need1))
            if not res: continue
            a = np.array([x[:8] for x in res], float); sr = st_res
            nd = np.array([x[7] for x in res]); nd = nd[nd < 99]
            sk_n = [x[5] for x in sr if x[5] is not None]; sk_e = [x[6] for x in sr if x[6] is not None]
            lb = np.array(lbs, float) if lbs else np.zeros((1, 4))
            q9.write(f"{sub}\t{tg}\t{len(res)}\t{a[:, 0].mean():.4f}\t{a[:, 1].mean():.4f}\t{a[:, 2].mean():.4f}\t{a[:, 3].mean():.4f}\t"
                     f"{a[:, 4].mean():.2f}\t{a[:, 5].mean():.2f}\t{a[:, 6][a[:, 6] < 99].mean():.2f}\t{nd.mean():.2f}\t{np.percentile(nd, 50):.0f}\t{np.percentile(nd, 90):.0f}\t{nd.max()}\t"
                     f"{len(sr)}\t{np.mean([x[0] for x in sr]):.4f}\t{np.mean([x[1] for x in sr]):.4f}\t{np.mean([x[2] for x in sr]):.2f}\t{np.mean([x[3] for x in sr]):.2f}\t{np.mean([x[4] for x in sr]):.2f}\t"
                     f"{emp}\t{(np.mean(sk_n) if sk_n else float('nan')):.4f}\t{(np.mean(sk_e) if sk_e else float('nan')):.4f}\t"
                     f"{lb[:, 0].mean():.4f}\t{lb[:, 1].mean():.4f}\t{lb[:, 2].mean():.4f}\t{lb[:, 3].mean():.4f}\n")
            # rodneykinney's table: worst case over the subset's paths with no knowledge of A, B (A = B = C)
            Mtab = per[0][1] if tg.startswith('M') else None
            need_all = [x[7] for x in sr if x[7] < 99]
            for Mval in ([int(tg[1:])] if tg.startswith('M') else sorted({x[1] for x in per})):
                if not tg.startswith('M') and Mval not in range(10, 16): continue
                wc_n = max([R_fake(Mval, N, al, Cl, Cl, Cl, False) for N, al in sigs] or [0])
                wc_e = max([R_exact(Mval, N, al, Cl, Cl, Cn_min) for N, al in sigs if N <= 8] or [0])
                sel = [x for x, pp in zip(sr, per) if pp[1] == Mval]
                if not sel: continue
                ne = [x[7] for x in sel if x[7] < 99]
                rod.write(f"{sub}\t{tg}:M={Mval}\t{wc_n}\t{wc_e}\t{np.mean([x[3] for x in sel]):.2f}\t{np.mean([x[4] for x in sel]):.2f}\t"
                          f"{(np.percentile(ne, 90) if ne else float('nan')):.0f}\t{(max(ne) if ne else -1)}\t{len(sigs)}\n")
            for f_ in (q9, cex, rod): f_.flush()
        print(sub, flush=True)
    # Q8 tables per subset and per corner subset
    groups = [(s, [s]) for s in SUBS] + [(g, [s for s in SUBS if CORNER(s) == g]) for g in CGROUPS] + [('all', SUBS)]
    for g, subs in groups:
        for q in (1, 2):
            for Rv in range(0, rmax + 1):
                cnts = []; ws = []; found = {t: [] for t in TARGETS}
                for s in subs:
                    A_ = acc8[(s, 'opt')]
                    if not A_: continue
                    w = SIZE[s] / len(A_['rc'])
                    for rr in A_['rc']:
                        cnts.append(cum(rr, q, Rv)); ws.append(w)
                    for t in TARGETS:
                        B_ = acc8[(s, t)]
                        need = B_['n1'] if q == 1 else B_['n2']
                        # states below the target count as not found: pad to the opt sample size
                        nmiss = len(A_['rc']) - len(need)
                        found[t] += [(int(x <= Rv), w) for x in need] + [(0, w)] * nmiss
                c = np.array(cnts, float); wv = np.array(ws)
                mu = (c * wv).sum() / wv.sum(); n = len(c)
                se = np.sqrt(((c - mu) ** 2 * wv).sum() / wv.sum() / max(n - 1, 1))
                line = f'{g}\t{q}\t{Rv}\t{n}\t{mu:.1f}\t{se:.1f}'
                for t in TARGETS:
                    v = np.array([x[0] for x in found[t]], float); ww = np.array([x[1] for x in found[t]])
                    p = (v * ww).sum() / ww.sum(); line += f'\t{p:.4f}\t{np.sqrt(p * (1 - p) / len(v)):.4f}'
                q8.write(line + '\n')
    for g, subs in groups:
        rows = [x for s in subs for x in acc11[s]]
        ws = [SIZE[s] / len(acc11[s]) for s in subs for _ in acc11[s]]
        a = np.array(rows, float); wv = np.array(ws)
        m = (a * wv[:, None]).sum(0) / wv.sum()
        c11.write(f'{g}\t{len(rows)}\t' + '\t'.join(f'{x:.4f}' for x in m) + '\n')
    print('done')

if __name__ == '__main__':
    main()
