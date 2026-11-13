#!/usr/bin/env python3
"""Independent recount of the section-1 and errata numbers from the census CSVs (research/out/hand).
Does not import pv.py / fillenv.py: own loaders, own layout classifier, own implementation of the prune list from the
guide's prose, exact Fractions where it matters.  Prints the unrounded values to compare with the page.

  python3 research/src/verify/recount.py > research/out/verify/recount.txt"""
import csv, collections, math
from fractions import Fraction as F
H = '/data/fmc/judging-a-dr/research/out/hand/'
def rows(n):
    with open(H + n) as f:
        r = csv.reader(f); next(r); return [x for x in r]
QT = {'0c0': 0, '4a1': 1, '4a2': 2, '4b2': 2, '0c3': 3, '2c3': 3, '4c3': 3, '0c4': 4, '2c4': 4, '4c4': 4, '2c5': 5, '4b5': 5}
GRP = {0: '0qt', 1: '1-2qt', 2: '1-2qt', 3: '3qt', 4: '4qt', 5: '5qt'}
def grp(sub): return GRP[QT[sub.split()[0]]]

h2 = [(r[0], int(r[1]), int(r[2]), int(r[3]), int(r[4]), int(r[5]), int(r[6]), int(r[7])) for r in rows('h2_lengths.csv')]
k5 = [(r[0], r[1], r[2], int(r[3]), int(r[4]), int(r[5]), int(r[6]), int(r[7])) for r in rows('k5_quick_reads.csv')]
TOT = sum(r[-1] for r in h2); assert TOT == sum(r[-1] for r in k5) == 19508428800, TOT
cc = {r[0]: (r[1], int(r[2])) for r in rows('corner_cases.csv')}
def layout(mask):
    u = [p for p in range(4) if mask >> p & 1]; d = [p for p in range(4) if mask >> (p + 4) & 1]
    n = len(u) + len(d)
    if n == 2 and len(u) == 1:
        if u[0] == d[0]: return 'stacked'
        return 'across' if (u[0] - d[0]) % 4 in (1, 3) else 'opposite'
    if n == 4 and len(u) in (0, 4): return '4-0'
    return 'other'
LAY = {k: layout(m) for k, (s, m) in cc.items()}

def hist(it):
    h = collections.Counter()
    for d, c in it: h[d] += c
    return h
def le(h, T): return sum(c for d, c in h.items() if d <= T)
def pc(h, T): return 100 * F(le(h, T), sum(h.values()))
def fastest(h): return min(d for d, c in h.items() if c)
out = []
def say(*a): print(*a); out.append(' '.join(map(str, a)))

say('== dead on sight')
def both(sub, A, B, e=None):
    return hist((d, c) for s, a, b, tp, lo, hi, d, c in k5 if s.split()[0] == sub and (e is None or s.split()[1] == e)
                and ((LAY[a] == A and LAY[b] == B) or (LAY[a] == B and LAY[b] == A)))
for name, h in [('2c5 stacked/stacked', both('2c5', 'stacked', 'stacked')), ('2c5 stacked/opposite', both('2c5', 'stacked', 'opposite')),
                ('2c4 stacked/stacked', both('2c4', 'stacked', 'stacked')), ('4a2 2e 4-0/4-0', both('4a2', '4-0', '4-0', '2e'))]:
    say(f'  {name}: in10 {float(pc(h,10)):.4f}% in11 {float(pc(h,11)):.4f}% in12 {float(pc(h,12)):.4f}% fastest {fastest(h)}')
t2c5 = sum(c for s, *_, c in k5 if s.startswith('2c5'))
x = sum(both('2c5', 'stacked', 'stacked').values()) + sum(both('2c5', 'stacked', 'opposite').values())
say(f'  first two rows share of 2c5: {100*x/t2c5:.3f}%')

say('== base rates by qt group (h2)')
for g in ['1-2qt', '3qt', '4qt', '5qt']:
    h = hist((r[6], r[7]) for r in h2 if grp(r[0]) == g)
    say(f'  {g}: in11 {float(pc(h,11)):.4f}%  in10 {float(pc(h,10)):.4f}%')

say('== variance / sd')
def within(keyf, data):
    g = collections.defaultdict(collections.Counter)
    for r in data: g[keyf(r)][r[-2]] += r[-1]
    N = S = S2 = 0; W = F(0)
    for h in g.values():
        n = sum(h.values()); s = sum(d * c for d, c in h.items()); s2 = sum(d * d * c for d, c in h.items())
        N += n; S += s; S2 += s2; W += F(s2) - F(s * s, n)
    var = F(S2, N) - F(S, N) ** 2
    return float(var), float(W / N), len(g)
var, w, n = within(lambda r: 0, h2); say(f'  total sd {math.sqrt(var):.4f}')
for name, data, kf in [('subset (48)', h2, lambda r: r[0]),
                       ('subset+cc both(unordered)+HTR both(unordered) [k5, no pairs]', k5, lambda r: (r[0], r[1], r[2], r[4], r[5])),
                       ('subset+cc both+HTR both+pairs [k5]', k5, lambda r: r[:6]),
                       ('subset+HTR both+L+Lp+parity [h2]', h2, lambda r: r[:6])]:
    v, w, n = within(kf, data)
    say(f'  {name}: classes {n}, explains {100*(1-w/var):.2f}%, sd left {math.sqrt(w):.4f}')

say('== B1 / B2 / B5 (h2)')
hm13 = sum(r[7] for r in h2 if r[2] == 13); b13 = sum(r[7] for r in h2 if r[1] == 13)
say(f'  hmax=13 states {hm13:,}; both 13 {b13:,}; on a given side (hmax13+both)/2 = {(hm13 + b13)//2:,} rem {(hm13+b13)%2}')
say('  subsets with hmax 13:', sorted({r[0] for r in h2 if r[2] == 13}), ' with both 13:', sorted({r[0] for r in h2 if r[1] == 13}))
d18 = collections.Counter()
for r in h2:
    if r[6] == 18: d18[r[0]] += r[7]
say('  depth 18 by subset:', dict(d18), 'total', sum(d18.values()))
d16 = collections.Counter(); allsub = collections.Counter()
for r in h2:
    allsub[r[0]] += r[7]
    if r[6] >= 16: d16[r[0]] += r[7]
t16 = sum(d16.values())
other = sum(c for s, c in d16.items() if not (s.startswith('0c3') or QT[s.split()[0]] == 5))
say(f'  16+: {t16:,} = {100*t16/TOT:.3f}% of all; outside 0c3/5qt {100*other/t16:.2f}%; subsets with some {len([s for s in d16 if d16[s]])} of {len(allsub)}; without: {sorted(s for s in allsub if not d16[s])}')
k2 = [(r[0], int(r[1]), int(r[2]), int(r[3]), int(r[4]), int(r[5]), int(r[6]), int(r[7])) for r in rows('k2_combined.csv')]
for name, kf in [('k2 all: pairs,HTR both,L,parity', lambda r: r[:6]), ('k2 HTR both+L+parity', lambda r: r[:5])]:
    v, w, n = within(kf, k2); say(f'  {name}: classes {n}, explains {100*(1-w/var):.2f}%, sd left {math.sqrt(w):.4f}')
h5 = [(r[0], int(r[1]), int(r[2]), int(r[3]), int(r[4]), int(r[5]), int(r[6])) for r in rows('h5_pairs.csv')]
for name, kf in [('h5 true pairs', lambda r: r[:2]), ('h5 all four pair counts', lambda r: r[:5]), ('h5 true+pseudo', lambda r: r[:3])]:
    v, w, n = within(kf, h5); say(f'  {name}: classes {n}, explains {100*(1-w/var):.2f}%, sd left {math.sqrt(w):.4f}')
say('== scatter table rows')
for name, data, kf in [('k5 +pairs (capped)', k5, lambda r: (r[0], r[3])), ('k5 +cc both', k5, lambda r: (r[0], r[1], r[2])),
                       ('k5 +pairs+cc', k5, lambda r: (r[0], r[1], r[2], r[3])), ('k5 +HTR both', k5, lambda r: (r[0], r[4], r[5])),
                       ('k5 +pairs+HTR', k5, lambda r: (r[0], r[3], r[4], r[5])), ('k2 +pairs+HTR', k2, lambda r: (r[0], r[1], r[2], r[5])),
                       ('h2 +L,dLp', h2, lambda r: (r[0], r[3], r[4])), ('h2 +L,parity', h2, lambda r: (r[0], r[3], r[5])),
                       ('h2 +HTR both', h2, lambda r: (r[0], r[1], r[2]))]:
    v, w, n = within(kf, data); say(f'  {name}: classes {n}, explains {100*(1-w/var):.2f}%, sd left {math.sqrt(w):.4f}')
ls = [(r[0], int(r[2]), int(r[1]), int(r[3])) for r in rows('h3_leaveslice.csv')]
v, w, n = within(lambda r: (r[0], r[1]), ls); say(f'  leave slice: sd left {math.sqrt(w):.4f}')
say('== prune list (own implementation from the guide prose)')
def corner_reach(i): return [r for r in rows('corner_cases.csv') if r[0] == i][0][10]
def mask(i): return cc[i][1]
def is22(i): m = mask(i); return bin(m & 15).count('1') == 2 and bin(m >> 4).count('1') == 2
def pair_shape(bits):
    p = [x for x in range(4) if bits >> x & 1]; return 'diag' if (p[1] - p[0]) == 2 else 'adj'
def keep(sub, e, a, b, tp):
    cs = sub
    if cs in ('2c5', '4b5', '4c4', '0c3', '0c4'): return False
    if cs == '2c4':
        ok = lambda i: LAY[i] != 'stacked' and corner_reach(i) in ('2c3', '4b3')
        return (ok(a) and ok(b)) or tp >= 4
    if cs == '4c3':
        ok = lambda i: cc[i][0] == '4a3' and is22(i) and corner_reach(i) == '4b2'
        return ok(a) or ok(b) or tp >= 4
    if cs == '4a2':
        def good4(i):
            m = mask(i)
            if not is22(i): return False
            u, d = m & 15, m >> 4
            return (u == d and pair_shape(u) == 'adj') or (pair_shape(u) == 'diag' and pair_shape(d) == 'diag')
        def diag(i):
            m = mask(i); return is22(i) and pair_shape(m & 15) == 'diag' and pair_shape(m >> 4) == 'diag'
        return (good4(a) or good4(b)) if e == 4 else (diag(a) or diag(b))
    return True
n = collections.defaultdict(collections.Counter); kept = collections.defaultdict(collections.Counter)
for s, a, b, tp, lo, hi, d, c in k5:
    cs, e = s.split(); g = grp(s)
    for G in (g, 'all'):
        n[G][d] += c
        if keep(cs, int(e[0]), a, b, tp): kept[G][d] += c
for G in ['1-2qt', '3qt', '4qt', '5qt', 'all']:
    N = sum(n[G].values()); K = sum(kept[G].values())
    say(f'  {G}: drops {100*(N-K)/N:.3f}%  loses of 11s {100*(1-le(kept[G],11)/le(n[G],11)):.3f}%  of 10s {100*(1-le(kept[G],10)/le(n[G],10)):.3f}%')
say('== attempts')
with open(H + 'attempt_run.csv') as f:
    L = [l for l in f if not l.startswith('#')]
hd = L[0].strip().split(','); R = [dict(zip(hd, map(int, l.strip().split(',')))) for l in L[1:]]
have = [x for x in R if x['n9'] + x['n10'] > 0]
say(f'  n {len(R)} have {len(have)}')
say('  res_kept %.4f res_all %.4f drs_kept %.2f drs_all %.2f' % (
    sum(min(x['best9'], x['best10'], x['best_kept11']) for x in have) / len(have), sum(min(x['best9'], x['best10'], x['best11']) for x in have) / len(have),
    sum(x['n9'] + x['n10'] + x['kept11'] for x in have) / len(have), sum(x['n9'] + x['n10'] + x['n11'] for x in have) / len(have)))
say('== pairs')
def ph(cs, p, e=None):
    return hist((d, c) for s, a, b, tp, lo, hi, d, c in k5 if s.split()[0] == cs and (tp == p if p < 5 else tp >= 5))
for cs in ('4a1', '2c4', '2c5'):
    say(f'  {cs}: one more pair x{float(pc(ph(cs,4),11)/pc(ph(cs,0),11))**0.25:.3f}  (5+ / 0 = {float(pc(ph(cs,5),11)/pc(ph(cs,0),11)):.2f}: {float(pc(ph(cs,5),11)):.3f}% vs {float(pc(ph(cs,0),11)):.3f}%)')
say('== 2c4 corner cases')
def one(cs, ids):
    h = collections.Counter()
    for s, a, b, tp, lo, hi, d, c in k5:
        if s.split()[0] != cs: continue
        w = F((a in ids) + (b in ids), 2)
        if w: h[d] += w * c
    return h
for i in ('7', '8'):
    h = one('2c4', {i}); say(f'  case {i} one side: ' + ' / '.join(f'{float(pc(h,T)):.3f}%' for T in (10, 11, 12)))
    h = hist((d, c) for s, a, b, tp, lo, hi, d, c in k5 if s.startswith('2c4') and a == i and b == i); say(f'  case {i} both sides: ' + ' / '.join(f'{float(pc(h,T)):.3f}%' for T in (10, 11, 12)))
say('== plain rules (h2)')
for g in ('3qt', '4qt'):
    for name, pred in [('T-1 both (hmin>=10)', lambda r: r[1] >= 10), ('T-2 both (hmin>=9)', lambda r: r[1] >= 9)]:
        A = [r for r in h2 if grp(r[0]) == g]; N = sum(r[7] for r in A); N11 = sum(r[7] for r in A if r[6] <= 11)
        D = sum(r[7] for r in A if pred(r)); D11 = sum(r[7] for r in A if pred(r) and r[6] <= 11)
        say(f'  {g} {name}: drops {100*D/N:.3f}% loses {100*D11/N11:.3f}%')
for g in ('1-2qt', '3qt', '4qt', '5qt'):
    A = [x for x in k5 if grp(x[0]) == g]; N = sum(x[7] for x in A); N11 = sum(x[7] for x in A if x[6] <= 11)
    D = sum(x[7] for x in A if x[3] == 0); D11 = sum(x[7] for x in A if x[3] == 0 and x[6] <= 11)
    say(f'  no pair {g}: drops {100*D/N:.3f}% loses {100*D11/N11:.3f}%')
say('== hand bounds (h2): longer HTR or L with parity (L+dLp) proves no T')
for g in ('4qt', '5qt'):
    A = [r for r in h2 if grp(r[0]) == g]; N = sum(r[7] for r in A)
    for T in (12, 10):
        P = sum(r[7] for r in A if max(r[2], r[3] + r[4]) > T)
        say(f'  {g} proves no {T}: {100*P/N:.3f}%')
say('== best quarter')
def top(data, kf, g, T, s=F(1, 4)):
    cl = collections.defaultdict(lambda: [0, 0])
    for r in data:
        if grp(r[0]) != g: continue
        k = kf(r); cl[k][1] += r[-1]
        if r[-2] <= T: cl[k][0] += r[-1]
    L = sorted(cl.values(), key=lambda t: F(t[0], t[1]), reverse=True)
    N = sum(n for _, n in L); G = sum(x for x, _ in L); acc_n = 0; acc_g = F(0)
    for x, n in L:
        if acc_n + n > s * N: acc_g += (s * N - acc_n) / n * x; break
        acc_g += x; acc_n += n
    return float(100 * acc_g / G)
for g in ('1-2qt', '3qt', '4qt', '5qt'):
    for T in (10, 11, 12, 13):
        pc_ = top(k5, lambda r: (r[0], r[1], r[2], r[3]), g, T); q_ = top(k5, lambda r: r[:6], g, T); h_ = top(k5, lambda r: (r[0], r[4], r[5]), g, T)
        say(f'  {g} T{T}: pairs+corners {pc_:.2f}  htr {h_:.2f}  quick {q_:.2f}  (quick - p+c {q_-pc_:+.2f})')
say('== trangium (h7: d < G)')
h7 = [(r[0], int(r[1]), int(r[2]), int(r[3]), int(r[4])) for r in rows('h7_setup_bound.csv')]
for g in ('1-2qt', '3qt', '4qt', '5qt', '3qt+'):
    A = [r for r in h7 if (grp(r[0]) == g or (g == '3qt+' and grp(r[0]) in ('3qt', '4qt', '5qt')))]
    N = sum(r[4] for r in A); B = sum(r[4] for r in A if r[3] < r[2])
    say(f'  {g}: beaten {100*B/N:.4f}%  subsets where beaten: {len({r[0] for r in A if r[3] < r[2] and r[4]})}')
say('  subsets beaten anywhere:', len({r[0] for r in h7 if r[3] < r[2] and r[4]}))
say('== dead classes (<=1% finish in T)')
def dead(data, kf, g, T):
    cl = collections.defaultdict(lambda: [0, 0])
    for r in data:
        if grp(r[0]) != g: continue
        k = kf(r); cl[k][1] += r[-1]
        if r[-2] <= T: cl[k][0] += r[-1]
    N = sum(n for _, n in cl.values()); return 100 * sum(n for x, n in cl.values() if 100 * x <= n) / N
for g in ('4qt', '5qt'):
    say(f'  {g} T12: quick(k5) {dead(k5, lambda r: r[:6], g, 12):.2f}%  all(k2) {dead(k2, lambda r: r[:6], g, 12):.2f}%')
say('== misc')
h4 = [(r[0], int(r[1]), int(r[2]), int(r[3]), int(r[4])) for r in rows('h4_htr_leaveslice.csv')]
A = [r for r in h4 if r[0] == '4a1 4e']; N = sum(r[4] for r in A)
say(f'  Levi vs leave slice (4a1 4e): mean ls-formula {sum((r[3]-(r[1]+r[2]-1))*r[4] for r in A)/N:+.4f}; ls below formula {100*sum(r[4] for r in A if r[3] < r[1]+r[2]-1)/N:.3f}%')
mo = sum(r[6] * r[7] for r in h2) / TOT; mb = sum(max(r[2], r[3] + r[4]) * r[7] for r in h2) / TOT
say(f'  mean optimal {mo:.3f}; mean max(longer HTR, L with parity) {mb:.3f}; gap {mo-mb:.3f}')
for g in ('1-2qt', '3qt', '4qt', '5qt'):
    say(f'  shortest HTR in {g}: {min(r[1] for r in h2 if grp(r[0]) == g and r[7])}')
for q_ in (1, 2, 3, 4, 5):
    say(f'  shortest HTR at {q_}qt: {min(r[1] for r in h2 if QT[r[0].split()[0]] == q_ and r[7])}')
h3 = [(r[0], int(r[1]), int(r[2]), int(r[3])) for r in rows('h3_leaveslice.csv')]
for g in (None, '1-2qt', '3qt', '4qt', '5qt'):
    A = [r for r in h3 if g is None or grp(r[0]) == g]
    say(f'  slice free {g or "all"}: {100*sum(r[3] for r in A if r[1] == r[2])/sum(r[3] for r in A):.3f}%')
h10 = [(r[0], int(r[1]), int(r[2]), int(r[3]), int(r[4])) for r in rows('h10_first_moves.csv')]
A = [r for r in h10 if r[1] in (10, 11)]
say(f'  depth 10/11 with exactly one optimal first move: {100*sum(r[4] for r in A if r[2] == 1)/sum(r[4] for r in A):.3f}%')
for d in (10, 11):
    A = [r for r in h10 if r[1] == d]; say(f'    depth {d}: {100*sum(r[4] for r in A if r[2] == 1)/sum(r[4] for r in A):.3f}%')
avgs = {}
for cs in QT:
    A = [r for r in h2 if r[0].split()[0] == cs]; avgs[cs] = sum(r[6]*r[7] for r in A)/sum(r[7] for r in A)
say('  averages:', {k: round(v, 3) for k, v in sorted(avgs.items(), key=lambda t: t[1])})
for s in ('4a2 2e', '4a2 0e', '2c4 0e', '2c4 2e', '2c4 4e'):
    A = [r for r in h2 if r[0] == s]; h = hist((r[6], r[7]) for r in A); say(f'  {s}: avg {sum(d*c for d,c in h.items())/sum(h.values()):.3f} in10/11/12 ' + ' / '.join(f'{float(pc(h,T)):.3f}' for T in (10,11,12)))
A = [r for r in h2 if r[0].startswith('4c3')]; N = sum(r[7] for r in A); D = [r for r in A if r[1] >= 9]
say(f'  Zagros 4c3 9+ both: drops {100*sum(r[7] for r in D)/N:.2f}%; keeps ' + ' / '.join(f'{100*(1-sum(r[7] for r in D if r[6]<=T)/sum(r[7] for r in A if r[6]<=T)):.2f}%' for T in (10, 11, 12)))
say(f'    9-and-9 finishing in 9 exists: {any(r[1]==9 and r[2]==9 and r[6]==9 and r[7] for r in A)}; min depth with hmin>=9: {min(r[6] for r in D if r[7])}')
def within1(kf):
    g = collections.defaultdict(collections.Counter)
    for r in h2: g[kf(r)][r[6]] += r[7]
    ok = 0
    for h in g.values():
        n = sum(h.values()); acc = 0
        for d in sorted(h):
            acc += h[d]
            if 2 * acc >= n: med = d; break
        ok += h[med - 1] + h[med] + h[med + 1]
    return 100 * ok / TOT
say(f'  within 1 of class median: subset+L+hmax {within1(lambda r: (r[0], r[3], r[2])):.2f}%  subset alone {within1(lambda r: r[0]):.2f}%')
say('== last move (h8)')
h8 = [(r[0], int(r[1]), int(r[2]), int(r[3])) for r in rows('h8_last_move.csv')]
N = sum(r[3] for r in h8)
say(f'  states {N}; mean min {sum(min(r[1],r[2])*r[3] for r in h8)/N:.4f}; gain {sum((r[1]-min(r[1],r[2]))*r[3] for r in h8)/N:.4f}')
th = collections.defaultdict(collections.Counter)
for s_, d, d2, c in h8: th[s_][d2 - d] += c
gains = sorted((sum(-k * v for k, v in t.items() if k < 0) / sum(t.values()), s_) for s_, t in th.items())
say(f'  gain by subset: lowest {gains[0][0]:.3f} ({gains[0][1]}), highest {gains[-1][0]:.3f} ({gains[-1][1]})')
tot = collections.Counter()
for t in th.values(): tot.update(t)
say('  other way is: ' + ', '.join(f'{k:+d}: {100*v/sum(tot.values()):.2f}%' for k, v in sorted(tot.items())))
g3 = [(d, d2, c) for s, d, d2, c in h8 if grp(s) == '3qt']; n3 = sum(c for *_, c in g3)
say(f'  3qt in11 pure {100*sum(c for d,d2,c in g3 if d<=11)/n3:.3f}% either {100*sum(c for d,d2,c in g3 if min(d,d2)<=11)/n3:.3f}%')
say('== prune table, full (own rule implementation)')
for G in ['1-2qt', '3qt', '4qt', '5qt', 'all']:
    N = sum(n[G].values()); K = sum(kept[G].values())
    say(f'  {G}: dropped {100*(N-K)/N:.2f}%  lost in10 {100*(1-le(kept[G],10)/le(n[G],10)):.3f}% in11 {100*(1-le(kept[G],11)/le(n[G],11)):.3f}% in12 {100*(1-le(kept[G],12)/le(n[G],12)):.3f}%   all: ' + ' / '.join(f'{100*le(n[G],T)/N:.3f}' for T in (10,11,12)) + '   kept: ' + (' / '.join(f'{100*le(kept[G],T)/K:.3f}' for T in (10,11,12)) if K else '-'))
dn = {G: sum(n[G].values()) - sum(kept[G].values()) for G in n}
say(f"  4qt+5qt share of all DRs {100*(sum(n['4qt'].values())+sum(n['5qt'].values()))/sum(n['all'].values()):.2f}%; of what the list drops, 4-5qt is {100*(dn['4qt']+dn['5qt'])/dn['all']:.2f}%")
A = [x for x in k5 if x[0].startswith('4c3') and x[6] <= 11]; N = sum(x[7] for x in A)
say(f"  4c3 11s lost: by hmin>=9 rule {100*sum(x[7] for x in A if x[4] >= 9)/N:.2f}%; by the list {100*sum(x[7] for x in A if not keep('4c3', int(x[0].split()[1][0]), x[1], x[2], x[3]))/N:.2f}%")
