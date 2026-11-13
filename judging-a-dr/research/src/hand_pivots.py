#!/usr/bin/env python3
"""Everything by target: for "a finish in T or less", T = 9..13 (8..14 for the base rates).

  pivots_base.md        how rare each target is, per corner subset and per corner-qt group
  pivots_rank.md        the finishes in T that sit in the best-looking quarter, by read
  pivots_drop.md        the DRs you can drop and still keep 95% of the finishes in T, by read
  pivots_dead.md        the DRs in classes where at most 1% finish in T, and what dropping them loses
  pivots_rules.md       plain HTR-length rules: what each drops and what it loses
  pivots_htr.md         share finishing in T by longer HTR, per qt group
  pivots_bounds.md      what the guaranteed bounds, and the computer tables, prove at each target
  pivots_lastmove.md    pure DR against a DR whose last move can be turned the other way
  pivots_full.md        every read, every target, every measure (the appendix)

A "class" is a set of DRs that look the same to the read.  Classes are ranked by their true share of finishes in T,
so each number is the best any rule based on that read could do."""
import collections, csv, sys
sys.path.insert(0, '/data/fmc/judging-a-dr/research/src')
import pv
OUT = '/data/fmc/judging-a-dr/report/data/'

def classes(rs, keyf, depth_i, count_i):
    g = collections.defaultdict(lambda: [0] * 19)
    for r in rs: g[(r[0],) + tuple(keyf(r))][int(r[depth_i])] += int(r[count_i])
    return g
def in_group(key, grp): return grp == 'all' or pv.QT[key[0].split()[0]] == grp
def measures(g, grp, T, eps=0.01):
    cl = [(sum(h[:T + 1]), sum(h)) for k, h in g.items() if in_group(k, grp)]
    N = sum(n for _, n in cl); G = sum(x for x, _ in cl)
    out = dict(base=100 * G / N)
    dead = [(x, n) for x, n in cl if x <= eps * n]
    out['dead'] = 100 * sum(n for _, n in dead) / N
    out['lost'] = 100 * sum(x for x, _ in dead) / G if G else 0.0
    cl.sort(key=lambda t: t[0] / t[1], reverse=True)
    for s in (0.10, 0.25, 0.50):                       # share of the finishes kept by the best-looking share s
        acc_g = acc_n = 0.0
        for x, n in cl:
            if acc_n + n > s * N:
                acc_g += (s * N - acc_n) / n * x; break
            acc_g += x; acc_n += n
        out[f'top{round(100*s)}'] = 100 * acc_g / G if G else float('nan')
    for rcl in (0.90, 0.95, 0.99):                     # share of DRs dropped while keeping rcl of the finishes
        acc_g = acc_n = 0.0
        for x, n in cl:
            if acc_g + x >= rcl * G:
                acc_n += (rcl * G - acc_g) / x * n if x else 0; break
            acc_g += x; acc_n += n
        out[f'drop{round(100*rcl)}'] = 100 * (1 - acc_n / N) if G else 100.0
    return out

k5 = pv.rows('k5_quick_reads.csv')      # subset,ca,cb,tp,hmin,hmax,depth,count
h2 = pv.rows('h2_lengths.csv')          # subset,hmin,hmax,L,dLp,parity,depth,count
k2 = pv.rows('k2_combined.csv')         # subset,hmin,hmax,L,misfit,tp,depth,count
READS = [
    ('subset', 'subset', classes(k5, lambda r: (), 6, 7)),
    ('pairs', '+ true pairs', classes(k5, lambda r: (r[3],), 6, 7)),
    ('corners', '+ corner case on both sides', classes(k5, lambda r: (r[1], r[2]), 6, 7)),
    ('pairs+corners', '+ pairs and corner cases', classes(k5, lambda r: (r[1], r[2], r[3]), 6, 7)),
    ('htr', '+ HTR length on both sides', classes(k5, lambda r: (r[4], r[5]), 6, 7)),
    ('Lp', '+ corner length L and E-parity', classes(h2, lambda r: (r[3], r[4]), 6, 7)),
    ('pairs+htr', '+ pairs and HTR', classes(k5, lambda r: (r[3], r[4], r[5]), 6, 7)),
    ('quick', '+ pairs, corner cases and HTR', classes(k5, lambda r: tuple(r[1:6]), 6, 7)),
    ('all', '+ pairs, HTR, L and E-parity', classes(k2, lambda r: tuple(r[1:6]), 6, 7)),
]
R = {k: g for k, _, g in READS}
HEAD = ['subset', 'pairs', 'corners', 'pairs+corners', 'htr', 'quick', 'all']
HEAD_NAMES = ['Subset alone', 'Subset and pairs', 'Subset and corner case on both sides', 'Subset, pairs and corner cases',
              'Subset and HTR on both sides', 'Subset, pairs, corner cases and HTR', 'Subset, pairs, HTR, L and E-parity']
COST = {'subset': 'look', 'pairs': 'look', 'corners': 'recognise', 'pairs+corners': 'recognise', 'htr': 'solve', 'Lp': 'solve', 'pairs+htr': 'solve', 'quick': 'solve', 'all': 'solve'}
M = {(k, grp, T): measures(g, grp, T) for k, _, g in READS for grp in pv.GROUPS + ['all'] for T in pv.WIDE}
def n0(x): return f'{pv.hu(x):.0f}%'
def write(name, lines):
    open(OUT + name, 'w').write('\n'.join(lines) + '\n'); print(f'--- {name}'); print('\n'.join(lines))

# ---- base rates
sub = R['subset']
def hist(pred):
    h = [0] * 19
    for k, v in sub.items():
        if pred(k[0].split()[0]):
            for d, c in enumerate(v): h[d] += c
    return h
def base_rows(first, targets):
    out = []
    for grp in ['0qt'] + pv.GROUPS:
        h = hist(lambda cs: pv.QT[cs] == grp)
        out.append(f'| **{pv.GROUP_NAME[grp]}** | ' + first(h) + pv.cells(h, targets) + ' |')
        for cs in pv.CS_ORDER:
            if pv.QT[cs] == grp and grp != '0qt':
                h = hist(lambda x: x == cs); out.append(f'| {cs} | ' + first(h) + pv.cells(h, targets) + ' |')
    h = hist(lambda cs: True); out.append(f'| **all DRs** | ' + first(h, True) + pv.cells(h, targets) + ' |')
    return out
L = (['| DRs | Share of all DRs | In 8 | In 9 | In 10 | In 11 |', '|---|---:|---:|---:|---:|---:|']
     + base_rows(lambda h, last=False: '100% | ' if last else f'{pv.hu(100*sum(h)/pv.TOT, 1):.1f}% | ', range(8, 12))
     + ['', 'The same rows for the longer finishes, 12, 13 and 14 or less:', '', '| DRs | In 12 | In 13 | In 14 |', '|---|---:|---:|---:|']
     + base_rows(lambda h, last=False: '', range(12, 15)))
write('pivots_base.md', L)

# ---- the three by-read tables: rows = (qt group, target), columns = reads
LOOK, SOLVE = HEAD[:4], HEAD[4:]           # the reads that need no solving, and the ones that do
def by_read(keys, cell, first=None):
    L = ['| Corner qt | Finish needed | ' + ' | '.join(([first[0]] if first else []) + [HEAD_NAMES[HEAD.index(k)] for k in keys]) + ' |', '|---|---|' + '---:|' * (len(keys) + (1 if first else 0))]
    for grp in pv.GROUPS:
        for T in pv.WIDE:
            L.append(f'| {grp.replace("-", "–")} | {T} or less | ' + ' | '.join(([first[1](grp, T)] if first else []) + [cell(M[(k, grp, T)]) for k in keys]) + ' |')
    return L
write('pivots_rank.md', by_read(LOOK, lambda m: n0(m['top25']), first=('DRs that finish in T at all', lambda grp, T: pv.num(M[('subset', grp, T)]['base'])))
      + ['', 'The reads you have to solve for, on the same rows: the share of the finishes in T kept in the best-looking quarter.', '']
      + by_read(SOLVE, lambda m: n0(m['top25'])))
write('pivots_drop.md', by_read(LOOK, lambda m: n0(m['drop95']))
      + ['', 'The reads you have to solve for, on the same rows: the share of the qt group you can drop and keep 95% of the finishes in T.', '']
      + by_read(SOLVE, lambda m: n0(m['drop95'])))
write('pivots_dead.md', by_read(LOOK, lambda m: n0(m['dead']))
      + ['', 'What dropping those classes costs. Same rows; each number is the share of all the finishes in T of the qt group that sit in the classes under 1%.', '']
      + by_read(LOOK, lambda m: n0(m['lost']))
      + ['', 'The same two measures for the reads you have to solve for. First the share of the qt group in classes under 1%:', '']
      + by_read(SOLVE, lambda m: n0(m['dead']))
      + ['', 'and the share of the finishes in T those classes hold:', '']
      + by_read(SOLVE, lambda m: n0(m['lost'])))

# ---- plain HTR rules
g_h = collections.defaultdict(lambda: [0] * 19)       # (group, hmin, hmax) -> hist
for r in h2: g_h[(pv.QT[r[0].split()[0]], int(r[1]), int(r[2]))][int(r[6])] += int(r[7])
def rule(grp, T, pred):
    n = good = dn = dg = 0
    for (q, lo, hi), h in g_h.items():
        if q != grp: continue
        a = sum(h); b = sum(h[:T + 1]); n += a; good += b
        if pred(lo, hi): dn += a; dg += b
    return 100 * dn / n, (100 * dg / good if good else 0.0)
def rc(x, proven=False):
    """Two cells, dropped and lost (one for a proven rule, which loses nothing). Nothing dropped: 0 and a dash."""
    d, l = x
    if proven: return '0' if d == 0 else pv.num(d)
    return '0 | —' if d == 0 else f'{pv.num(d)} | {pv.num(l)}'
L = ['| Corner qt | Finish needed, $T$ | Longer side more than $T$: dropped (proven, loses nothing) | Longer side $T$ or more: dropped | Longer side $T$ or more: finishes lost | Longer side $T-1$ or more: dropped | Longer side $T-1$ or more: finishes lost |', '|---|---|---:|---:|---:|---:|---:|']
for grp in pv.GROUPS:
    for T in pv.WIDE:
        L.append(f'| {grp.replace("-", "–")} | {T} | ' + rc(rule(grp, T, lambda lo, hi: hi > T), True) + ' | ' + ' | '.join(rc(rule(grp, T, f)) for f in (
            lambda lo, hi: hi >= T, lambda lo, hi: hi >= T - 1)) + ' |')
L += ['', 'The rules on both sides, same rows. Again each rule has two numbers: the share of the qt group it drops, and the share of the finishes in T it loses (a dash where it drops nothing).', '',
      '| Corner qt | Finish needed, $T$ | Both sides $T$ or more: dropped | Both sides $T$ or more: finishes lost | Both sides $T-1$ or more: dropped | Both sides $T-1$ or more: finishes lost | Both sides $T-2$ or more: dropped | Both sides $T-2$ or more: finishes lost |', '|---|---|---:|---:|---:|---:|---:|---:|']
for grp in pv.GROUPS:
    for T in pv.WIDE:
        L.append(f'| {grp.replace("-", "–")} | {T} | ' + ' | '.join(rc(rule(grp, T, f)) for f in (
            lambda lo, hi: lo >= T, lambda lo, hi: lo >= T - 1, lambda lo, hi: lo >= T - 2)) + ' |')
write('pivots_rules.md', L)

# ---- plain pair rules (no solving)
g_p = collections.defaultdict(lambda: [0] * 19)
for r in k5: g_p[(pv.QT[r[0].split()[0]], int(r[3]))][int(r[6])] += int(r[7])
def prule(grp, T, k):
    n = good = dn = dg = 0
    for (q, tp), h in g_p.items():
        if q != grp: continue
        a = sum(h); b = sum(h[:T + 1]); n += a; good += b
        if tp <= k: dn += a; dg += b
    return 100 * dn / n, (100 * dg / good if good else 0.0)
L = ['| Corner qt | Finish needed | No pairs: dropped | No pairs: finishes lost | One pair or none: dropped | One pair or none: finishes lost | Two pairs or fewer: dropped | Two pairs or fewer: finishes lost |', '|---|---|---:|---:|---:|---:|---:|---:|']
for grp in pv.GROUPS:
    for T in pv.WIDE:
        L.append(f'| {grp.replace("-", "–")} | {T} or less | ' + ' | '.join(rc(prule(grp, T, k)) for k in (0, 1, 2)) + ' |')
write('pivots_pair_rules.md', L)

# ---- share finishing in T by longer HTR
L = ['| Corner qt | Longer HTR, moves | Share of the group | In 9 | In 10 | In 11 | In 12 | In 13 |', '|---|---:|---:|---:|---:|---:|---:|---:|']
for grp in pv.GROUPS:
    tot = sum(sum(h) for (q, lo, hi), h in g_h.items() if q == grp)
    for hi in range(1, 14):
        h = [0] * 19
        for (q, lo, x), v in g_h.items():
            if q == grp and x == hi:
                for d, c in enumerate(v): h[d] += c
        if sum(h) / tot < 0.001: continue
        L.append(f'| {grp.replace("-", "–")} | {hi} | {pv.num(100*sum(h)/tot)} | ' + pv.cells(h, pv.WIDE) + ' |')
write('pivots_htr.md', L)

# ---- what is proven at each target
lat = collections.defaultdict(lambda: collections.Counter())      # (spec, group) -> {(bound, depth): count}, both sides
with open('/data/fmc/judging-a-dr/research/out/lattice.csv') as f:
    for r in csv.DictReader(f):
        if r['sides'] == '2': lat[(r['spec'], pv.QT[r['subset'].split()[0]])][(int(r['bound']), int(r['depth']))] += int(r['count'])
def proves(spec, grp, T):
    c = lat[(spec, grp)]; return 100 * sum(n for (b, d), n in c.items() if b > T) / sum(c.values())
hb = collections.defaultdict(lambda: [0, 0, 0, 0, 0])     # (group, T) -> n, truth, htr, Lp, either
for r in h2:
    grp = pv.QT[r[0].split()[0]]; hi = int(r[2]); lp = int(r[3]) + int(r[4]); d = int(r[6]); c = int(r[7])
    for T in pv.WIDE:
        o = hb[(grp, T)]; o[0] += c; o[1] += c * (d > T); o[2] += c * (hi > T); o[3] += c * (lp > T); o[4] += c * (max(hi, lp) > T)
sb = collections.defaultdict(lambda: [0, 0, 0, 0])      # (group, T) -> n, finishes in T, setup+HTR bound above T, those among the finishes
for x, hmax, G, d, c in pv.rows('h7_setup_bound.csv'):
    for T in pv.WIDE:
        o = sb[(pv.QT[x.split()[0]], T)]; c_ = int(c); o[0] += c_; o[1] += c_ * (int(d) <= T); o[2] += c_ * (int(G) > T); o[3] += c_ * (int(G) > T and int(d) <= T)
def setup_cell(grp, T):
    o = sb[(grp, T)]
    return '0 | —' if o[2] == 0 else f'{pv.num(100 * o[2] / o[0])} | {pv.num(100 * o[3] / o[1]) if o[1] else "0"}'
L = ['| Corner qt | Finish needed | DRs with no such finish | Longer HTR proves it | Corner length with parity proves it | Either one proves it |', '|---|---|---:|---:|---:|---:|']
for grp in pv.GROUPS:
    for T in pv.WIDE:
        o = hb[(grp, T)]
        assert abs(100 * o[2] / o[0] - proves('htr', grp, T)) < 1e-9 and abs(100 * o[3] / o[0] - proves('c+p', grp, T)) < 1e-9
        L.append(f'| {grp.replace("-", "–")} | {T} or less | {pv.num(100*o[1]/o[0])} | ' + ' | '.join(pv.num(100 * o[i] / o[0]) for i in (2, 3, 4)) + ' |')
L += ['', 'Same rows, against the setup + HTR bound and two computer tables. The setup + HTR bound is not a proof, so next to the share it rules out is the share of the finishes in T it is wrong about (a dash where it rules out nothing).', '',
      '| Corner qt | Finish needed | Setup + HTR says no | Finishes in T it is wrong about | NISS@DR table proves it | Everything visible proves it |', '|---|---|---:|---:|---:|---:|']
for grp in pv.GROUPS:
    for T in pv.WIDE:
        L.append(f'| {grp.replace("-", "–")} | {T} or less | {setup_cell(grp, T)} | {pv.num(proves("KF", grp, T))} | {pv.num(proves("c+2520+F", grp, T))} |')
write('pivots_bounds.md', L)

# ---- the last DR move
lm = collections.defaultdict(lambda: [[0] * 19, [0] * 19])
for s, d, d2, c in pv.rows('h8_last_move.csv'):
    grp = pv.QT[s.split()[0]]; lm[grp][0][int(d)] += int(c); lm[grp][1][min(int(d), int(d2))] += int(c)
L = ['| Corner qt | Last DR move | In 9 | In 10 | In 11 | In 12 | In 13 |', '|---|---|---:|---:|---:|---:|---:|']
for grp in pv.GROUPS:
    L.append(f'| {grp.replace("-", "–")} | one way only (pure DR) | ' + pv.cells(lm[grp][0], pv.WIDE) + ' |')
    L.append(f'| {grp.replace("-", "–")} | last move can go either way | ' + pv.cells(lm[grp][1], pv.WIDE) + ' |')
write('pivots_lastmove.md', L)

# ---- the appendix: every read, every target, every measure
L = []
for grp in pv.GROUPS:
    L += ['', f'**{pv.GROUP_NAME[grp]}.** Share of the group that finishes in ' + ', '.join(f'{T}' for T in pv.WIDE[:-1]) + f' or {pv.WIDE[-1]} or less: '
          + ', '.join(pv.num(M[('subset', grp, T)]['base']) for T in pv.WIDE) + '. Ranking first: each row is one read at one target, and the last three columns are the share of the finishes in T you keep if you keep the best-looking 10%, 25% or 50% of the group.', '',
          '| Finish needed | What you know | How you get it | Best 10% keeps | Best 25% keeps | Best 50% keeps |', '|---|---|---|---:|---:|---:|']
    for T in pv.WIDE:
        L.append(f'| **{T} or less** | nothing | | 10% | 25% | 50% |')
        for k, name, _ in READS:
            m = M[(k, grp, T)]
            L.append(f'| {T} or less | {name} | {COST[k]} | ' + ' | '.join(n0(m[x]) for x in ('top10', 'top25', 'top50')) + ' |')
    L += ['', f'Throwing away, {grp.replace("-", "–")}, same rows: the share of the group you can drop and still keep 90%, 95% or 99% of the finishes in T, then the share in classes under 1% and the finishes those classes hold.', '',
          '| Finish needed | What you know | Drop, keeping 90% | Drop, keeping 95% | Drop, keeping 99% | In classes under 1% | Finishes lost by dropping those |', '|---|---|---:|---:|---:|---:|---:|']
    for T in pv.WIDE:
        b = M[('subset', grp, T)]['base']
        L.append(f'| **{T} or less** | nothing | 10% | 5% | 1% | {"100%" if b <= 1 else "0%"} | {"100%" if b <= 1 else "0%"} |')
        for k, name, _ in READS:
            m = M[(k, grp, T)]
            L.append(f'| {T} or less | {name} | ' + ' | '.join(n0(m[x]) for x in ('drop90', 'drop95', 'drop99', 'dead', 'lost')) + ' |')
write('pivots_full.md', L[1:])

# ---- the computer ladder at each target (section "What a computer can prove")
LEVELS = [('htr', 'HTR length'), ('c+p', 'L with parity'), ('c+bad+p', 'L+S+T'), ('KF', 'NISS@DR'), ('K0+F', 'NISS@DR + H-perm parity'), ('c+2520+F', 'Everything visible')]
lat_all = collections.defaultdict(lambda: collections.Counter())
with open('/data/fmc/judging-a-dr/research/out/lattice.csv') as f:
    for r in csv.DictReader(f):
        if r['sides'] == '2':
            lat_all[(r['spec'], pv.QT[r['subset'].split()[0]])][(int(r['bound']), int(r['depth']))] += int(r['count'])
            lat_all[(r['spec'], r['subset'])][(int(r['bound']), int(r['depth']))] += int(r['count'])
def pr(spec, key, T):
    c = lat_all[(spec, key)]; return pv.num(100 * sum(n for (b, d), n in c.items() if b > T) / sum(c.values()))
def truth(key, T):
    c = lat_all[('htr', key)]; return pv.num(100 * sum(n for (b, d), n in c.items() if d > T) / sum(c.values()))
L = ['| Corner qt | Finish needed | DRs with no such finish | ' + ' | '.join(n for _, n in LEVELS[:3]) + ' |', '|---|---|---:|' + '---:|' * 3]
for grp in pv.GROUPS:
    for T in (10, 11, 12, 13):
        L.append(f'| {pv.GROUP_NAME[grp]} | {T} or less | {truth(grp, T)} | ' + ' | '.join(pr(sp, grp, T) for sp, _ in LEVELS[:3]) + ' |')
L += ['', 'The three biggest levels, same rows: the share of the qt group for which each proves there is no finish in T.', '',
      '| Corner qt | Finish needed | ' + ' | '.join(n for _, n in LEVELS[3:]) + ' |', '|---|---|' + '---:|' * 3]
for grp in pv.GROUPS:
    for T in (10, 11, 12, 13):
        L.append(f'| {pv.GROUP_NAME[grp]} | {T} or less | ' + ' | '.join(pr(sp, grp, T) for sp, _ in LEVELS[3:]) + ' |')
write('pivots_ladder.md', L)
BIG = ['4b2 4e', '2c3 4e', '4c3 4e', '2c4 4e', '0c3 4e', '4c4 4e', '2c5 4e', '4b5 4e']
L = ['| Subset | Share of all DRs | Average optimal, moves | In 11 | In 12 |', '|---|---:|---:|---:|---:|']
for s in BIG:
    h = sub[(s,)]
    L.append(f'| {s} | {pv.hu(100*sum(h)/pv.TOT, 2):.2f}% | {pv.hu(pv.avg(h), 2):.2f} | {pv.pct(h, 11)} | {pv.pct(h, 12)} |')
L += ['', 'The same subsets: the share of each for which NISS@DR, and everything visible, proves there is no finish in 11, and in 12.', '',
      '| Subset | No 11: NISS@DR proves it | No 11: everything visible proves it | No 12: NISS@DR proves it | No 12: everything visible proves it |', '|---|---:|---:|---:|---:|']
for s in BIG:
    L.append(f'| {s} | ' + ' | '.join(pr(sp, s, T) for T in (11, 12) for sp in ('KF', 'c+2520+F')) + ' |')
write('pivots_ladder_subsets.md', L)
def every_dead(grp, T):
    """Everything readable together (k6_all_reads_ordered.csv, drtools hcensus4: subset, corner cases, pairs, HTR on
    normal and on inverse, L, Lp - L, E-parity): share of the qt group in classes where at most 1% finish in T."""
    col = {10: 12, 11: 13, 12: 14}[T]; g = collections.defaultdict(lambda: [0, 0])
    with open(pv.H + 'k6_all_reads_ordered.csv') as f:
        r = csv.reader(f); next(r)
        for x in r:
            if pv.QT[x[0].split()[0]] != grp: continue
            g[tuple(x[:9])][0] += int(x[col]); g[tuple(x[:9])][1] += int(x[9])
    return n0(100 * sum(n for k, n in g.values() if 100 * k <= n) / sum(n for _, n in g.values()))
L = ['| Corner qt | Finish needed | Everything readable puts it under 1% | The two hand bounds prove it | A table that sees the corners exactly and the colours of the edges proves it | DRs that really have no such finish |', '|---|---|---:|---:|---:|---:|']
for grp in ('3qt', '4qt', '5qt'):
    for T in (10, 11, 12):
        o = hb[(grp, T)]
        L.append(f"| {grp} | {T} or less | {every_dead(grp, T)} | {pv.num(100*o[4]/o[0])} | {pr('c+2520+F', grp, T)} | {truth(grp, T)} |")
write('pivots_compare.md', L)
