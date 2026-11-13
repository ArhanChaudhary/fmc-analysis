#!/usr/bin/env python3
"""Numbers and tables for "what you can see that predicts the half turns before the first qt" (the reads section of
the reference page tables/half-turns-before-first-qt.md, rendered by tables/src/half_turns_before_first_qt.py).

Input: out/big/htfirst/htfirst.tsv and tables.json (research/htfirst), the per-state files of the main pass (number of
optimal finishes, and ht_first_n / ht_first_i for the comparison), the first study's corner cases.  Output:
  out/ht_first.tsv            group x population x target x side: shares of DRs whose first qt comes after 0 / 1 / 2 / 3+
                              half turns (target opt / p1 = within +1 / opt_side, p1_side = only R2 L2 F2 B2 counted)
  out/ht_first_reads.tsv      the reads: group x population x read x value -> n, shares
  out/ht_first_extra.json     numbers the page quotes, and under "tables" every table of the section as head + rows
Populations: DRs with optimal <= 13, <= 12, all DRs.  Pooled groups weight each sampled state by the exact size of its
subset x edges.  "Needs k+" = on both sides every optimal finish has at least k half turns before its first quarter
turn.  A DR with no quarter turn in any optimal finish counts as 3 or more, as on the page (0c0 0e only).
usage: xhtfirst.py"""
import sys, os, json, csv, collections, math
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import ht_first as H, common
sys.path.insert(0, '/data/fmc/judging-a-dr/research/src')
import pv
R = H.R; OUT = os.path.join(R, 'out')
SUBS, CG, SIZE = common.SUBS, common.CGROUPS, common.SIZE

X = H.Data(); D = X.D; N = X.n
cnt = collections.Counter(X.sub.tolist())
wt = np.array([SIZE[s] / cnt[s] for s in SUBS])[np.array([SUBS.index(s) for s in X.sub])]
POP = {'le13': X.d <= 13, 'le12': X.d <= 12, 'all': np.ones(N, bool)}
POPNAME = {'all': 'All DRs', 'le13': 'Optimal ≤ 13', 'le12': 'Optimal ≤ 12'}
E = {'tables': {}}

# ------------------------------------------------------------------ against the columns of the main pass
nopt = np.zeros(N, np.int64); cmp_ = collections.Counter()
for s in SUBS:
    st = common.load_states(s); m = X.sub == s
    assert (D['idx'][m] == st['idx']).all() and (D['c'][m] == st['c']).all() and (D['d'][m] == st['d']).all()
    nopt[m] = st['nopt']
    a, b = D['a0n'][m], D['a0i'][m]
    # the main pass writes the finish length where no optimal finish has a quarter turn
    cmp_['states'] += int(m.sum())
    cmp_['normal_differs'] += int((np.where(a == 99, st['d'], a) != st['ht_first_n']).sum())
    cmp_['inverse_differs'] += int((np.where(b == 99, st['d'], b) != st['ht_first_i']).sum())
    cmp_['no_qt_in_any_optimal'] += int(((a == 99) | (b == 99)).sum())
    cmp_['some_optimal_without_qt'] += int(D['noqt0'][m].sum())
    if s == '0c0 0e':
        E['0c0_0e'] = dict(n=int(m.sum()), no_qt_in_any_optimal=float((a == 99).mean()), some_optimal_without_qt=float(D['noqt0'][m].mean()))
E['compare'] = dict(cmp_)
assert cmp_['normal_differs'] == 0 and cmp_['inverse_differs'] == 0, cmp_
# as on the page: no quarter turn in any optimal finish -> the finish length (3 or more in practice)
fix = lambda a: np.where(a == 99, X.d, a)
T0 = np.minimum(fix(D['a0n']), fix(D['a0i'])); T0n = fix(D['a0n'])
T1 = np.minimum(fix(D['a1n']), fix(D['a1i'])); T1n = fix(D['a1n'])
U0 = np.minimum(fix(D['b0n']), fix(D['b0i'])); U1 = np.minimum(fix(D['b1n']), fix(D['b1i']))
A2 = (fix(D['a0n']), fix(D['a0i']))
GROUPS = [(s, X.sub == s) for s in SUBS] + [(g, X.cs == g) for g in CG] + [('all', np.ones(N, bool))]
GM = dict(GROUPS)
TGT = {('opt', 'either'): T0, ('opt', 'normal'): T0n, ('p1', 'either'): T1, ('p1', 'normal'): T1n,
       ('opt_side', 'either'): U0, ('p1_side', 'either'): U1}

def pc(x):                      # as on the reference page
    x = float(x)
    if x == 0: return '0%'
    if x < 0.0005: return '<0.1%'
    return f'{pv.hu(round(x, 9), 1, 100):.1f}%'         # round(x, 9): a share is a sum of float weights over their total, a count ratio like 9/400 comes out as 0.022500000000000006
def dist(t, m):
    w = wt[m]; tot = w.sum()
    if tot == 0: return None
    v = t[m]
    return [float(w[v == k].sum() / tot) for k in range(3)] + [float(w[v >= 3].sum() / tot)]
def rate(t, m, k):
    w = wt[m]; tot = w.sum()
    return float(w[t[m] >= k].sum() / tot) if tot else None
def write(name, head, rows):
    E['tables'][name] = dict(head=head, rows=[[str(x) for x in r] for r in rows])
def cells(dd): return [pc(x) for x in dd] if dd else ['–'] * 4
H4 = ['0 half turns', '1 half turn', '2 half turns', '3 or more']

# ------------------------------------------------------------------ distributions
DIST = {}
with open(f'{OUT}/ht_first.tsv', 'w') as f:
    f.write('group\tpopulation\ttarget\tside\tn\tshare_of_group\tafter_0\tafter_1\tafter_2\tafter_3plus\n')
    for g, gm in GROUPS:
        for p, pm in POP.items():
            m = gm & pm
            n = int(m.sum()); share = float(wt[m].sum() / wt[gm].sum())
            for (tg, side), t in TGT.items():
                dd = dist(t, m)
                DIST[(g, p, tg, side)] = (n, share, dd)
                f.write('\t'.join([g, p, tg, side, str(n), f'{share:.4f}'] + ([f'{x:.4f}' for x in dd] if dd else [''] * 4)) + '\n')
E['dist'] = {f'{g}|{p}|{tg}|{side}': dict(n=n, share=sh, d=dd) for (g, p, tg, side), (n, sh, dd) in DIST.items()}
# within +1 of the optimal
P3 = ('le13', 'le12', 'all')
def p1row(g, lab):
    r = [lab]
    for p in P3:
        dd = DIST[(g, p, 'p1', 'either')][2]
        r += [pc(dd[0]), pc(dd[1]), pc(dd[2] + dd[3])] if dd else ['–'] * 3
    return r
hp1 = sum(([f'{POPNAME[p]}: 0 half turns', f'{POPNAME[p]}: 1', f'{POPNAME[p]}: 2 or more'] for p in P3), [])
write('p1_rows', ['Subset × edges'] + hp1, [p1row(s, s) for s in SUBS])
write('p1_corner', ['Corner subset'] + hp1, [p1row(g, g) for g in CG] + [p1row('all', 'all DRs')])
# only R2 L2 F2 B2 counted
write('side_pop', ['DRs counted', 'Every half turn counted: 0', 'Every half turn counted: 1', 'Every half turn counted: 2', 'Every half turn counted: 3 or more',
                   'U2 and D2 not counted: 0', 'U2 and D2 not counted: 1', 'U2 and D2 not counted: 2', 'U2 and D2 not counted: 3 or more'],
      [[POPNAME[p]] + cells(DIST[('all', p, 'opt', 'either')][2]) + cells(DIST[('all', p, 'opt_side', 'either')][2]) for p in P3])
E['differs_side_count'] = {p: float(wt[POP[p] & (U0 != T0)].sum() / wt[POP[p]].sum()) for p in POP}
def two(g, p, tg='opt'):
    d = DIST[(g, p, tg, 'either')][2]; return d[2] + d[3] if d else None
E['side_rank'] = {p: dict(all_count=[s for _, s in sorted(((two(s, p), s) for s in SUBS if s != '0c0 0e' and two(s, p) is not None), reverse=True)[:6]],
                          side_count=[s for _, s in sorted(((two(s, p, 'opt_side'), s) for s in SUBS if s != '0c0 0e' and two(s, p) is not None), reverse=True)[:6]]) for p in POP}
E['p1_worst'] = {p: sorted(((two(s, p, 'p1'), s) for s in SUBS if two(s, p, 'p1') is not None), reverse=True)[:5] for p in POP}

# ------------------------------------------------------------------ reads
SC = np.minimum(X.sC[0], X.sC[1]); SCmax = np.maximum(X.sC[0], X.sC[1])
CC = pv.corner_cases()
def layout(k): return CC[str(k)]['layout']
READ = []
def read_row(g, p, read, value, m):
    m = m & GM[g] & POP[p]
    n = int(m.sum())
    r = dict(group=g, population=p, read=read, value=value, n=n, share=float(wt[m].sum() / wt[GM[g] & POP[p]].sum()) if n else 0.0)
    for k in (1, 2, 3): r[f'needs_{k}plus'] = rate(T0, m, k) if n else None
    dd = dist(T0, m) if n else None
    for k in range(4): r[f'after_{k}'] = dd[k] if dd else None
    READ.append(r); return r
def c(r, key): return pc(r[key]) if r['n'] else '–'
RD = {}
READY_ROWS = [s for s in SUBS if ((X.sub == s) & (SC == 0)).any() and ((X.sub == s) & (SC >= 1) & (SC < 9)).any()]
READY_CG = [g for g in CG if any(s.split()[0] == g for s in READY_ROWS)]
E['ready_rows'] = READY_ROWS; E['ready_corner'] = READY_CG
for g in READY_ROWS + READY_CG:
    for p in POP:
        RD[(g, p, 'neither')] = read_row(g, p, 'ready', 'neither side', SC >= 1)
        RD[(g, p, 'a side')] = read_row(g, p, 'ready', 'a side', SC == 0)
        RD[(g, p, 'both')] = read_row(g, p, 'ready', 'both sides', SCmax == 0)
        for k in range(int(SC[GM[g]].max()) + 1):
            RD[(g, p, f'setup{k}')] = read_row(g, p, 'corner_setup_smaller_side', str(k), SC == k)
        if int(SC[GM[g]].max()) >= 2:
            RD[(g, p, 'setup2+')] = read_row(g, p, 'corner_setup_smaller_side', '2 or 3', SC >= 2)
            RD[(g, p, 'setup<2')] = read_row(g, p, 'corner_setup_smaller_side', '0 or 1', SC < 2)
RH = ['Neither side ready', 'Needs 1+, neither side ready', 'Needs 1+, a side ready', 'Needs 2+, neither side ready', 'Needs 2+, a side ready']
def ready_row(g, p, lab=None):
    a, b = RD[(g, p, 'neither')], RD[(g, p, 'a side')]
    return ([lab] if lab else [g]) + [c(a, 'share'), c(a, 'needs_1plus'), c(b, 'needs_1plus'), c(a, 'needs_2plus'), c(b, 'needs_2plus')]
for p in POP:
    write(f'ready_rows_{p}', ['Subset × edges'] + RH, [ready_row(g, p) for g in READY_ROWS])
    write(f'ready_corner_{p}', ['Corner subset'] + RH, [ready_row(g, p) for g in READY_CG])
write('ready_2c4_2e', ['2c4 2e'] + RH, [ready_row('2c4 2e', p, f"{POPNAME[p][0].lower() + POPNAME[p][1:]} ({RD[('2c4 2e', p, 'neither')]['n'] + RD[('2c4 2e', p, 'a side')]['n']:,} sampled)") for p in P3])

# corner setup count on the subsets where it goes up to 3
SETUP_LOOK = {}
for a, v in enumerate(X.sC_t):
    kk = int(X.case_t[a]); SETUP_LOOK.setdefault((CC[str(kk)]['cs'], int(v)), set()).add(layout(kk))
def look(cs, k): return ' or '.join(sorted(SETUP_LOOK.get((cs, k), {'–'})))
E['setup_look'] = {f'{cs}|{k}': look(cs, k) for (cs, k) in SETUP_LOOK}
SH = ['Half turns the corners need, smaller side', 'Bad corners on that side', 'DRs in the sample', 'Share of those DRs'] + H4
for p in POP:
    rows = []
    for g in [s for s in READY_ROWS if s.split()[0] in ('4a2', '4a1', '4b2')]:
        for k in range(4):
            r = RD[(g, p, f'setup{k}')]
            if r['n']: rows.append([g, str(k), look(g.split()[0], k), f"{r['n']:,}", c(r, 'share')] + [c(r, f'after_{j}') for j in range(4)])
    write(f'setup_rows_{p}', ['Subset × edges'] + SH, rows)
    write(f'setup_4a2_4e_{p}', SH, [[str(k), look('4a2', k), f"{RD[('4a2 4e', p, f'setup{k}')]['n']:,}", c(RD[('4a2 4e', p, f'setup{k}')], 'share')] +
                                    [c(RD[('4a2 4e', p, f'setup{k}')], f'after_{j}') for j in range(4)] for k in range(4)])
    rows = []
    for g in ('4a2 4e', '4a2 2e', '4a2 0e', '4b2 0e', '4a1 4e', '4b2 2e', '4a1 2e', '4b2 4e', '4a1 0e'):
        a, b = RD[(g, p, 'setup2+')], RD[(g, p, 'setup<2')]
        rows.append([g, c(a, 'share'), f"{a['n']:,}", c(a, 'needs_2plus'), c(b, 'needs_2plus'), c(a, 'needs_3plus'), c(b, 'needs_3plus')])
    write(f'setup_rule_{p}', ['Subset × edges', 'Corners need 2 or 3 half turns on both sides', 'DRs in the sample with that',
                              'Needs 2+, with that', 'Needs 2+, without', 'Needs 3+, with that', 'Needs 3+, without'], rows)

# per side, by corner case: what a case says about its own side
def side_dist(gm, k):
    w = np.concatenate([wt[gm & (X.case[i] == k)] for i in (0, 1)]); a = np.concatenate([A2[i][gm & (X.case[i] == k)] for i in (0, 1)])
    tot = w.sum()
    return len(a), ([float(w[a == j].sum() / tot) for j in range(3)] + [float(w[a >= 3].sum() / tot)] if tot else None)
CASES = sorted(X.case_name, key=lambda k: (CG.index(X.case_name[k].split('-')[0]), int(X.case_name[k].split('-')[1])))
SIDE = {}
CH = ['Corner case on that side', 'Bad corners', 'A qt takes it straight to']
for p in POP:
    rows = []
    for k in CASES:
        cs = X.case_name[k].split('-')[0]
        gm = GM[cs] & POP[p]
        n, dd = side_dist(gm, k)
        tot_sides = 2 * wt[gm].sum()
        sh = (wt[gm & (X.case[0] == k)].sum() + wt[gm & (X.case[1] == k)].sum()) / tot_sides if tot_sides else 0
        SIDE[(X.case_name[k], p)] = (n, float(sh), dd)
        if cs == '0c0': continue
        rows.append([X.case_name[k], layout(k), CC[str(k)]['straight'] or 'nothing, needs a setup', pc(sh), f'{n:,}'] + cells(dd))
    write(f'cases_{p}', CH + ['Share of the sides of its subset', 'Sides in the sample'] + H4, rows)
    rows = []
    gm = GM['2c4 2e'] & POP[p]
    for k in [k for k in CASES if X.case_name[k].startswith('2c4-')]:
        n, dd = side_dist(gm, k)
        SIDE[(X.case_name[k], f'2c4 2e {p}')] = (n, None, dd)
        rows.append([X.case_name[k], layout(k), CC[str(k)]['straight'] or 'nothing, needs a setup', f'{n:,}'] + cells(dd))
    write(f'cases_2c4_2e_{p}', CH + ['Sides in the sample'] + H4, rows)
E['side'] = {f'{a}|{b}': dict(n=n, share=sh, d=dd) for (a, b), (n, sh, dd) in SIDE.items()}

# shorter HTR (a read that needs the HTR)
hmin = np.minimum(X.htr[0], X.htr[1])
E['htr'] = {}
for p in POP:
    rows = []
    for g in ('4b2 2e', '4a1 4e', '2c4 2e'):
        m = GM[g] & POP[p]
        for v in sorted(set(hmin[m].tolist())):
            r = read_row(g, p, 'shorter_htr', str(v), hmin == v)
            E['htr'][f'{g}|{p}|{v}'] = r
            if r['n'] >= 100: rows.append([g, str(v), f"{r['n']:,}", c(r, 'share'), c(r, 'needs_1plus'), c(r, 'needs_2plus')])
    write(f'htr_{p}', ['Subset × edges', 'Shorter of the two HTRs, moves', 'DRs in the sample', 'Share of those DRs', 'Needs 1+', 'Needs 2+'], rows)
    for nm, g, f in (('4b2 2e short', '4b2 2e', hmin <= 4), ('4b2 2e long', '4b2 2e', hmin >= 5), ('4a1 4e 1-2', '4a1 4e', hmin <= 2),
                     ('4a1 4e 3-4', '4a1 4e', (hmin >= 3) & (hmin <= 4)), ('4a1 4e 5+', '4a1 4e', hmin >= 5), ('2c4 2e 9+', '2c4 2e', hmin >= 9), ('2c4 2e 8-', '2c4 2e', hmin <= 8)):
        RD[(g, p, 'htr ' + nm.split(' ', 2)[2])] = read_row(g, p, 'shorter_htr', nm.split(' ', 2)[2], f)

# number of optimal finishes (computer only)
BUCK = [(1, 1, '1'), (2, 3, '2 or 3'), (4, 7, '4 to 7'), (8, 15, '8 to 15'), (16, 10**9, '16 or more')]
for g in ('2c4 2e', 'all'):
    for p in POP:
        for lo, hi, nm in BUCK:
            RD[(g, p, 'nopt ' + nm)] = read_row(g, p, 'optimal_finishes', nm, (nopt >= lo) & (nopt <= hi))
write('nopt', ['Optimal finishes of the DR', '2c4 2e, optimal ≤ 13: share of those DRs', '2c4 2e, optimal ≤ 13: needs 2+', '2c4 2e, all: needs 2+',
               'Every subset, optimal ≤ 13: needs 2+', 'Every subset, all DRs: needs 2+'],
      [[nm, c(RD[('2c4 2e', 'le13', 'nopt ' + nm)], 'share'), c(RD[('2c4 2e', 'le13', 'nopt ' + nm)], 'needs_2plus'), c(RD[('2c4 2e', 'all', 'nopt ' + nm)], 'needs_2plus'),
        c(RD[('all', 'le13', 'nopt ' + nm)], 'needs_2plus'), c(RD[('all', 'all', 'nopt ' + nm)], 'needs_2plus')] for lo, hi, nm in BUCK])

# ------------------------------------------------------------------ how much each read tells
def ent(p):
    p = p[p > 0]; return float(-(p * np.log2(p)).sum())
def explained(f, y):
    """share of the entropy of y removed by knowing f, minus what a read with as many values removes by chance"""
    hy = ent(np.bincount(y, minlength=2) / len(y))
    if hy == 0: return 0.0
    vals, inv = np.unique(f, return_inverse=True)
    h = sum((inv == v).mean() * ent(np.bincount(y[inv == v], minlength=2) / (inv == v).sum()) for v in range(len(vals)))
    return max(0.0, 1 - h / hy - (len(vals) - 1) / (2 * len(y) * math.log(2)) / hy)
side_feat = []
for i in (0, 1):
    cp, ep, sp = X.perm[i]
    tp, tU, tD = H.true_pairs(cp, ep)
    side_feat.append(dict(pairs=np.minimum(tp, 5), slice=np.minimum(H.slice_pairs(cp, sp), 4)))
esolved = (X.perm[0][2].astype(int) == np.arange(4)[None, :]).sum(1)
spar = np.array([sum(1 for a in range(4) for b in range(a) if q[b] > q[a]) % 2 for q in H.PERM4])[D['s']]
LAY = np.array([layout(k) for k in range(max(X.case_name) + 1)])
lay_pair = np.array([' / '.join(sorted(x)) for x in zip(LAY[X.case[0]], LAY[X.case[1]])])
case_pair = np.minimum(X.case[0], X.case[1]) * 100 + np.maximum(X.case[0], X.case[1])
coset = [D['ccn'].astype(np.int64) * 70 + D['epn'], D['cci'].astype(np.int64) * 70 + D['epi']]
FEAT = {
    'a side ready or not': (SC == 0).astype(int),
    'bad-corner layout on both sides': np.unique(lay_pair, return_inverse=True)[1],
    'corner case on both sides': case_pair,
    'corner cases and both HTR lengths (needs the HTRs)': case_pair * 10000 + np.minimum(X.htr[0], X.htr[1]) * 100 + np.maximum(X.htr[0], X.htr[1]),
    'both HTR lengths (needs the HTRs)': np.minimum(X.htr[0], X.htr[1]) * 100 + np.maximum(X.htr[0], X.htr[1]),
    'true pairs on both sides': np.minimum(side_feat[0]['pairs'], side_feat[1]['pairs']) * 10 + np.maximum(side_feat[0]['pairs'], side_feat[1]['pairs']),
    'slice pairs on both sides': np.minimum(side_feat[0]['slice'], side_feat[1]['slice']) * 10 + np.maximum(side_feat[0]['slice'], side_feat[1]['slice']),
    'E-slice edges solved': esolved, 'E-slice parity': spar,
    'optimal length (not a read)': X.d, 'number of optimal finishes (not a read)': np.minimum(np.floor(np.log2(np.maximum(nopt, 1))).astype(int), 6),
}
KEY = ['2c4 2e', '2c3 2e', '4a2 4e', '4a1 4e', '4b2 2e']
E['explained'] = {}
for g in KEY:
    for p in POP:
        m = GM[g] & POP[p]
        for k in (1, 2):
            y = (T0[m] >= k).astype(int)
            for nm, f in FEAT.items():
                E['explained'][f'{g}|{p}|{k}|{nm}'] = explained(f[m], y)
            y = np.concatenate([(A2[i][m] >= k).astype(int) for i in (0, 1)])
            E['explained'][f'{g}|{p}|{k}|side: corner case'] = explained(np.concatenate([X.case[i][m] for i in (0, 1)]), y)
            E['explained'][f'{g}|{p}|{k}|side: every bad piece'] = explained(np.concatenate([coset[i][m] for i in (0, 1)]), y)
write('explained_2c4_2e', ['Read on 2c4 2e', 'Optimal ≤ 13: needs 1+', 'Optimal ≤ 13: needs 2+', 'All 2c4 2e: needs 1+', 'All 2c4 2e: needs 2+'],
      [[nm] + [pc(E['explained'][f'2c4 2e|{p}|{k}|{nm}']) for p in ('le13', 'all') for k in (1, 2)] for nm in FEAT])
write('explained_2plus', ['Read', '2c4 2e', '2c3 2e', '4a2 4e', '4a1 4e', '4b2 2e'],
      [[nm] + [pc(E['explained'][f'{g}|le13|2|{nm}']) for g in KEY] for nm in FEAT])
write('explained_side_2plus', ['Known about one side', '2c4 2e', '2c3 2e', '4a2 4e', '4a1 4e', '4b2 2e'],
      [[lab] + [pc(E['explained'][f'{g}|le13|2|{nm}']) for g in KEY] for lab, nm in (('its corner case', 'side: corner case'), ('its corner case and where every bad edge sits', 'side: every bad piece'))])

# 2c4 2e: layouts and case pairs; the extremes are picked on the even-numbered states and quoted on the odd ones
E['pairs_2c4_2e'] = {}
anyst = np.array(['stacked' in x for x in lay_pair]); bothst = lay_pair == '1 up 1 down, stacked / 1 up 1 down, stacked'
cpn = np.array([' and '.join(sorted((X.case_name[a], X.case_name[b]))) for a, b in zip(X.case[0], X.case[1])])
for p in POP:
    m = GM['2c4 2e'] & POP[p]
    even = m & (D['idx'] % 2 == 0); odd = m & (D['idx'] % 2 == 1)
    RD[('2c4 2e', p, 'stacked a side')] = read_row('2c4 2e', p, 'layout', 'stacked on a side', anyst)
    RD[('2c4 2e', p, 'stacked no side')] = read_row('2c4 2e', p, 'layout', 'stacked on no side', ~anyst)
    RD[('2c4 2e', p, 'stacked both')] = read_row('2c4 2e', p, 'layout', 'stacked on both sides', bothst)
    RD[('2c4 2e', p, 'stacked not both')] = read_row('2c4 2e', p, 'layout', 'not stacked on both sides', ~bothst)
    vals = sorted(set(cpn[m].tolist()))
    tab = {v: read_row('2c4 2e', p, 'corner_case_pair', v, cpn == v) for v in vals}
    big = [v for v in vals if (even & (cpn == v)).sum() >= 100]
    worst = max(big, key=lambda v: rate(T0, even & (cpn == v), 2)); best = min(big, key=lambda v: rate(T0, even & (cpn == v), 2))
    hi = max(vals, key=lambda v: tab[v]['needs_2plus'] if tab[v]['n'] >= 100 else -1); lo = min(vals, key=lambda v: tab[v]['needs_2plus'] if tab[v]['n'] >= 100 else 9)
    E['pairs_2c4_2e'][p] = dict(pairs=len(vals), highest=hi, highest_row=tab[hi], lowest=lo, lowest_row=tab[lo],
                               worst=worst, worst_heldout=rate(T0, odd & (cpn == worst), 2), worst_heldout_n=int((odd & (cpn == worst)).sum()),
                               best=best, best_heldout=rate(T0, odd & (cpn == best), 2), best_heldout_n=int((odd & (cpn == best)).sum()))

# ------------------------------------------------------------------ optimal finishes with no extra quarter turn
# qtf = the fewest quarter turns any finish of the state can have; a finish with exactly that many has no extra one.
qmin = np.zeros(N, np.int64); qmax = np.zeros(N, np.int64)
for s in SUBS:
    st = common.load_states(s); m = X.sub == s
    qmin[m] = st['qmin']; qmax[m] = st['qmax']; assert (st['qtfull'] == X.qtf[m]).all()
hasmin = X.hasmin
assert (hasmin == (qmin == X.qtf)).all()                     # the main pass's fewest quarter turns in an optimal finish
some_extra = qmax > X.qtf
# no quarter turn in a finish without extra ones (an HTR state solved by half turns): the finish length, as above
ET = np.minimum(np.where(X.e0[0] == 99, X.d, X.e0[0]), np.where(X.e0[1] == 99, X.d, X.e0[1]))
assert ((X.e0[0] == 99) == (X.e0[1] == 99)).all() and (ET[hasmin] >= T0[hasmin]).all()
def dist5(m):
    w = wt[m]; tot = w.sum()
    if tot == 0: return None
    hm = hasmin[m]; v = ET[m]
    return [float(w[~hm].sum() / tot)] + [float(w[hm & (v == k)].sum() / tot) for k in range(3)] + [float(w[hm & (v >= 3)].sum() / tot)]
def qts(gm):
    v = sorted(set(X.qtf[gm].tolist()))
    return str(v[0]) if len(v) == 1 else f'{v[0]} or {v[1]}' if len(v) == 2 else f'{v[0]} to {v[-1]}'
NX = {}
H5 = ['No optimal without extra quarter turns', '0 half turns', '1 half turn', '2 half turns', '3 or more']
for g, gm in GROUPS:
    for p in POP:
        m = gm & POP[p]
        d5 = dist5(m); z = rate(T0, m, 0) if m.sum() else None
        zero = float(wt[m & (T0 == 0)].sum() / wt[m].sum()) if m.sum() else None
        zmin = d5[1] if d5 else None
        NX[(g, p)] = dict(n=int(m.sum()), share=float(wt[m].sum() / wt[gm].sum()), qts=qts(gm), d5=d5, zero=zero, zero_min=zmin,
                          zero_extra=(zero - zmin) if d5 else None,
                          every_extra=float(wt[m & ~hasmin].sum() / wt[m].sum()) if m.sum() else None,
                          some_extra=float(wt[m & some_extra].sum() / wt[m].sum()) if m.sum() else None)
        assert d5 is None or abs(float(wt[m & (T0 == 0) & ~(hasmin & (ET == 0))].sum() / wt[m].sum()) - (zero - zmin)) < 1e-9
E['noextra'] = {f'{g}|{p}': v for (g, p), v in NX.items()}
def c5(v): return [pc(x) for x in v] if v else ['–'] * 5
for p in POP:
    cut = p != 'all'
    def row(g, lab):
        v = NX[(g, p)]
        return [lab] + ([pc(v['share']), f"{v['n']:,}"] if cut else []) + [v['qts']] + c5(v['d5'])
    head = (['Share of its DRs that short', 'DRs in the sample'] if cut else []) + ['Quarter turns in such a finish'] + H5
    write(f'noextra_rows_{p}', ['Subset × edges'] + head, [row(s, s) for s in SUBS])
    write(f'noextra_corner_{p}', ['Corner subset'] + head, [row(g, g) for g in CG] + [row('all', 'all DRs')])
    def srow(g, lab):
        v = NX[(g, p)]
        return [lab] + ([pc(v['zero']), pc(v['zero_min']), pc(v['zero_extra'])] if v['d5'] else ['–'] * 3)
    write(f'zero_split_rows_{p}', ['Subset × edges', '0 half turns, as in the main table', 'A finish with no extra quarter turn starts with the quarter turn', 'Only finishes with extra quarter turns do'],
          [srow(s, s) for s in SUBS])
rows = []
for g in CG + ['all']:
    r = [g if g != 'all' else 'all DRs']
    for p in ('all', 'le13'):
        v = NX[(g, p)]; r += [pc(v['zero']), pc(v['zero_min']), pc(v['zero_extra'])]
    rows.append(r)
write('zero_split_corner', ['Corner subset', 'All DRs: 0 half turns, as in the main table', 'All DRs: a finish with no extra quarter turn starts with the quarter turn', 'All DRs: only finishes with extra quarter turns do',
                            'Optimal ≤ 13: 0 half turns, as in the main table', 'Optimal ≤ 13: a finish with no extra quarter turn starts with the quarter turn', 'Optimal ≤ 13: only finishes with extra quarter turns do'], rows)
rows = []
for g in ('4b2 0e', '4b2 2e', '4b2 4e', '4b2', '4a2 0e', '4a2 2e', '4a2 4e', '4a2'):
    for p in ('all', 'le13'):
        v = NX[(g, p)]
        rows.append([g if ' ' in g else f'{g}, edge counts pooled', POPNAME[p], pc(v['every_extra']), pc(v['some_extra']), pc(v['zero']), pc(v['zero_min']), pc(v['zero_extra'])])
write('two_qt', ['Subset', 'DRs counted', 'Every optimal has 4 or more quarter turns', 'Some optimal has 4 or more', '0 half turns, as in the main table',
                 'A 2qt optimal starts with the quarter turn', 'Only an optimal with 4 or more quarter turns does'], rows)
# the ready side again, on the optimal finishes with no extra quarter turn.  Where qtf equals the corners' count
# (every row but 4a1 0e, 4a1 2e and 0c0) the first quarter turn of such a finish lowers the corners' count, so on a
# side it cannot come before the half turns the corners need there: a floor, checked here on every state.
same = X.qtf == X.cq
for i in (0, 1):
    e = np.where(X.e0[i] == 99, 99, X.e0[i])
    assert (e[hasmin & same & (X.cq > 0)] >= X.sC[i][hasmin & same & (X.cq > 0)]).all()
RN = {}
for g in [s for s in READY_ROWS if (X.qtf[GM[s]] == X.cq[GM[s]]).all()] + [cg for cg in READY_CG if cg != '4a1']:
    for p in POP:
        m = GM[g] & POP[p] & same
        hm = m & hasmin
        def sh(a, b): return float(wt[a].sum() / wt[b].sum()) if wt[b].sum() else None
        nr, rd_ = hm & (SC >= 1), hm & (SC == 0)
        RN[(g, p)] = dict(n=int(hm.sum()), has=sh(hm, m), neither=sh(nr, hm), zero_neither=sh(nr & (ET == 0), nr), zero_ready=sh(rd_ & (ET == 0), rd_),
                          two_neither=sh(nr & (ET >= 2), nr), two_ready=sh(rd_ & (ET >= 2), rd_), at_floor=sh(hm & (ET == SC), hm),
                          n_neither=int(nr.sum()), n_ready=int(rd_.sum()))
E['ready_noextra'] = {f'{g}|{p}': v for (g, p), v in RN.items()}
def o(x): return pc(x) if x is not None else '–'
RNH = ['Has an optimal with no extra quarter turn', 'DRs in the sample that have one', 'Of those: neither side ready', '0 half turns, neither side ready', '0 half turns, a side ready',
       'Needs 2+, neither side ready', 'Needs 2+, a side ready', 'First quarter turn as early as the corners allow']
for p in POP:
    write(f'ready_noextra_low_{p}', ['Subset × edges'] + RNH,
          [[g, o(RN[(g, p)]['has']), f"{RN[(g, p)]['n']:,}"] + [o(RN[(g, p)][k]) for k in ('neither', 'zero_neither', 'zero_ready', 'two_neither', 'two_ready', 'at_floor')] for g in ('4b2 0e', '4b2 2e', '4b2 4e', '4a2 0e', '4a2 2e', '4a2 4e', '4a1 4e')])
    write(f'ready_noextra_corner_{p}', ['Corner subset'] + RNH,
          [[g, o(RN[(g, p)]['has']), f"{RN[(g, p)]['n']:,}"] + [o(RN[(g, p)][k]) for k in ('neither', 'zero_neither', 'zero_ready', 'two_neither', 'two_ready', 'at_floor')] for g in READY_CG if g != '4a1'])

E['reads'] = {f'{g}|{p}|{k}': r for (g, p, k), r in RD.items()}
E['kai'] = dict(ours=DIST[('2c3 2e', 'all', 'opt', 'either')][2], kai=[0.6, 0.248148, 0.109259, 0.042593], kai_n=540)
with open(f'{OUT}/ht_first_reads.tsv', 'w') as f:
    cols = ['group', 'population', 'read', 'value', 'n', 'share', 'needs_1plus', 'needs_2plus', 'needs_3plus', 'after_0', 'after_1', 'after_2', 'after_3']
    f.write('\t'.join(cols) + '\n')
    for r in READ:
        f.write('\t'.join('' if r[k] is None else (f'{r[k]:.4f}' if isinstance(r[k], float) else str(r[k])) for k in cols) + '\n')
json.dump(E, open(f'{OUT}/ht_first_extra.json', 'w'), indent=0, default=float)
print('compare with the main pass:', E['compare'])
print('wrote', len(READ), 'read rows,', len(E['tables']), 'tables')
for p in P3:
    print(p, 'pooled', [round(100 * x, 1) for x in DIST[('all', p, 'opt', 'either')][2]], 'share', round(100 * DIST[('all', p, 'opt', 'either')][1], 1),
          '| side only', [round(100 * x, 1) for x in DIST[('all', p, 'opt_side', 'either')][2]], '| +1', [round(100 * x, 1) for x in DIST[('all', p, 'p1', 'either')][2]])
