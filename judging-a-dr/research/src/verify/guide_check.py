#!/usr/bin/env python3
"""Independent re-evaluation of every {= =} cell of the guide (and of the other sources) that is an odds read:
own loaders, exact Fractions, own formatter; compared string by string with what pv/fillenv produce."""
import csv, re, sys, collections
from fractions import Fraction as F
from decimal import Decimal, ROUND_HALF_UP
H = '/data/fmc/judging-a-dr/research/out/hand/'
def rows(n):
    with open(H + n) as f:
        r = csv.reader(f); next(r); return [x for x in r]
K5 = [(r[0].split()[0], int(r[0].split()[1][0]), r[1], r[2], int(r[3]), int(r[4]), int(r[5]), int(r[6]), int(r[7])) for r in rows('k5_quick_reads.csv')]
H2 = [(r[0].split()[0], int(r[0].split()[1][0]), int(r[1]), int(r[2]), int(r[3]), int(r[4]), int(r[5]), int(r[6]), int(r[7])) for r in rows('h2_lengths.csv')]
CC = {r[0]: r for r in rows('corner_cases.csv')}
def merged(sub): return '4c' + sub[2] if sub[:2] in ('4a', '4b') and sub[2] in '34' else sub
def ok(v, want):
    if want is None: return True
    if callable(want): return bool(want(v))
    if isinstance(want, (tuple, list, set, frozenset)): return v in want
    return v == want
def q(cs=None, e=None, pairs=None, hmin=None, hmax=None, cc=None, both=None, group=None, htr=None):
    h = [F(0)] * 19
    for xs, xe, a, b, tp, lo, hi, d, c in K5:
        if not (ok(xs, cs) and ok(xe, e) and ok(tp, pairs) and ok(lo, hmin) and ok(hi, hmax)): continue
        if htr is not None and (lo, hi) != tuple(sorted(htr)): continue
        w = F(1)
        if cc is not None:
            w = F((a in cc) + (b in cc), 2)
            if w == 0: continue
        if both is not None:
            X, Y = both
            if not ((a in X and b in Y) or (a in Y and b in X)): continue
        h[d] += w * c
    return h
def q2(cs=None, e=None, hmin=None, hmax=None, L=None, Lp=None, parity=None):
    h = [F(0)] * 19
    for xs, xe, lo, hi, l, dlp, par, d, c in H2:
        if ok(xs, cs) and ok(xe, e) and ok(lo, hmin) and ok(hi, hmax) and ok(l, L) and ok(l + dlp, Lp) and ok(par, parity): h[d] += c
    return h
def dec(x, nd):
    return str(Decimal(x.numerator) / Decimal(x.denominator)) if False else format((Decimal(x.numerator) / Decimal(x.denominator)).quantize(Decimal(1).scaleb(-nd), rounding=ROUND_HALF_UP), 'f')
def fmt(good, n):
    if n == 0: return ''
    if good == 0: return '0'
    p = 100 * F(good) / F(n)
    if p >= F('99.95') and good < n: return '99.9%'
    if p >= F('99.05') and good < n: return dec(p, 1) + '%'
    if p >= F('9.95'): return dec(p, 0) + '%'
    if p >= F('0.995'): return dec(p, 1) + '%'
    if p >= F('0.00995'): return dec(p, 2) + '%'
    return '<0.01%'
def pct(h, T): return fmt(sum(h[:T + 1]), sum(h))
def tri(h, targets=(10, 11, 12)): return ' / '.join(pct(h, T) for T in targets)
T = tri
def S(ids): return frozenset(ids.split()) if isinstance(ids, str) else frozenset(ids)
def need(h): assert sum(h) > 0; return h
def E(cs, e): return tri(need(q(cs=cs, e=e)))
def PR(cs, n, e=None): return tri(need(q(cs=cs, e=e, pairs=n)))
def HX(cs, x, e=None): return tri(need(q(cs=cs, e=e, hmax=x)))
def HB(cs, a, b, e=None): return tri(need(q(cs=cs, e=e, htr=(a, b))))
def C1(cs, ids, e=None): return tri(need(q(cs=cs, e=e, cc=S(ids))))
def C2(cs, X, Y, e=None): return tri(need(q(cs=cs, e=e, both=(S(X), S(Y)))))
def SH(cs, h): return dec(100 * sum(h) / sum(q(cs=cs)), 0) + '%'
def CELLS(s): return s.replace(' / ', ' | ')
def avg(h): return sum(d * c for d, c in enumerate(h)) / sum(h)
def casepairs(cs):
    ids = sorted((k for k, r in CC.items() if merged(r[1]) == cs), key=int); out = []
    for i, a in enumerate(ids):
        for b in ids[i:]:
            h = q(cs=cs, both=({a}, {b}))
            if sum(h): out.append((avg(h), h))
    out.sort(key=lambda t: t[0]); return out
def XPH(cs, which): return casepairs(cs)[0 if which == 'best' else -1][1]
def XP(cs, which): return tri(XPH(cs, which))
def XPS(cs, which): return SH(cs, XPH(cs, which))
def KEEP(cs, keep_if, T):
    kept = q(cs=cs, hmin=keep_if); allh = q(cs=cs)
    return dec(100 * sum(kept[:T + 1]) / sum(allh[:T + 1]), 0) + '%'
ENV = {k: v for k, v in globals().items() if not k.startswith('_')}
FAM = re.compile(r"^(E|PR|HX|HB|C1|C2|SH|T|CELLS|XP|XPS|KEEP|pct|tri)\(")
B = '/data/fmc/judging-a-dr/research/src/report_build/'
sys.path.insert(0, B); sys.path.insert(0, '/data/fmc/judging-a-dr/research/src')
import fillenv, pv
tot = bad = skipped = 0
for fn in ('guide.md', 'new_front.md', 'new_tail.md', 'throwing.md'):
    for e in re.findall(r'\{=\s*(.+?)\s*=\}', open(B + fn).read()):
        if not FAM.match(e) or 'LAYH' in e or 'group=' in e or 'pv.' in e: skipped += 1; continue
        theirs = str(eval(e, fillenv.ENV)); mine = str(eval(e, ENV)); tot += 1
        if theirs != mine: bad += 1; print('MISMATCH', fn, e, '| page:', theirs, '| recount:', mine)
print(f'cells re-evaluated: {tot}, mismatches: {bad}, skipped (other families): {skipped}')
