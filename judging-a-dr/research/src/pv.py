#!/usr/bin/env python3
"""Shared numbers for the report: the share of DRs finishing in T or less, for any target T and any combination
of hand reads.  Everything is a sum over the census histograms in out/hand/ (exact counts over all DR states).

  q(cs=, e=, pairs=, hmin=, hmax=, cc=, both=)   histogram of the optimal finish (index = length) for the DRs matching
  share(h, T) / pct(h, T)                        share finishing in T or less, as a number / formatted
  tri(h), quad(h)                                'a / b / c' for targets 10 / 11 / 12, and with 13 added

Formatting, used everywhere so the tables agree with each other: 10% and up as whole numbers, 1% to 10% with one
decimal, under 1% with two, '<0.01%' when some states get there but fewer than that, and 0 when no state does."""
import csv, collections, functools, re

H = '/data/fmc/judging-a-dr/research/out/hand/'
TOT = 19508428800
TARGETS = (10, 11, 12, 13)          # the targets every odds table shows
WIDE = (9, 10, 11, 12, 13)          # the targets of the by-target tables
QT = {'0c0': '0qt', '4a1': '1-2qt', '4a2': '1-2qt', '4b2': '1-2qt', '0c3': '3qt', '2c3': '3qt', '4c3': '3qt',
      '0c4': '4qt', '2c4': '4qt', '4c4': '4qt', '2c5': '5qt', '4b5': '5qt'}
CS_ORDER = ['0c0', '4a1', '4a2', '4b2', '2c3', '4c3', '0c3', '2c4', '0c4', '4c4', '2c5', '4b5']
GROUPS = ['1-2qt', '3qt', '4qt', '5qt']
GROUP_NAME = {'0qt': '0qt (0c0)', '1-2qt': '1–2qt (4a1, 4a2, 4b2)', '3qt': '3qt (2c3, 4c3, 0c3)', '4qt': '4qt (2c4, 4c4, 0c4)', '5qt': '5qt (2c5, 4b5)', 'all': 'all DRs'}
sub_order = lambda s: (int(s.split()[0][-1]), s.split()[0], int(s.split()[1][0]))

@functools.lru_cache(None)
def rows(name):
    with open(H + name) as f:
        r = csv.reader(f); next(r); return [tuple(x) for x in r]

def fmt(good, n):
    if n == 0: return ''
    if good == 0: return '0'
    p = 100 * good / n
    if p >= 99.95 and good < n: return '99.9%'
    if p >= 99.05 and good < n: return f'{p:.1f}%'
    if p >= 9.95: return f'{p:.0f}%'
    if p >= 0.995: return f'{p:.1f}%'
    if p >= 0.00995: return f'{p:.2f}%'
    return '<0.01%'
def share(h, T): return 100 * sum(h[:T + 1]) / sum(h)
def pct(h, T): return fmt(sum(h[:T + 1]), sum(h))
def tri(h, targets=(10, 11, 12)): return ' / '.join(pct(h, T) for T in targets)
def quad(h): return tri(h, TARGETS)
def cells(h, targets=TARGETS): return ' | '.join(pct(h, T) for T in targets)
def avg(h): return sum(d * c for d, c in enumerate(h)) / sum(h)
def fastest(h): return min(d for d, c in enumerate(h) if c)
def num(x, digits=1):
    """A share (0..100) as text, same rounding rule as fmt."""
    if 99.95 <= x < 100: return '99.9%'
    if 99.05 <= x < 100: return f'{x:.1f}%'
    if x >= 9.95: return f'{x:.0f}%'
    if x >= 0.995: return f'{x:.1f}%'
    if x >= 0.00995: return f'{x:.2f}%'
    return '0' if x == 0 else '<0.01%'

# ---- corner cases
POS_ADJ = {(0, 1), (1, 2), (2, 3), (0, 3)}
def layout(mask):
    bad = [p for p in range(8) if mask >> p & 1]
    u = [p for p in bad if p < 4]; d = [p - 4 for p in bad if p >= 4]
    shape = lambda x: ('adjacent' if tuple(sorted(x)) in POS_ADJ else 'diagonal') if len(x) == 2 else ''
    if not bad: return 'none bad'
    if len(bad) == 2:
        if len(u) == 1: return '1 up 1 down, stacked' if u[0] == d[0] else ('1 up 1 down, across a face' if (min(u[0], d[0]), max(u[0], d[0])) in POS_ADJ else '1 up 1 down, opposite')
        return 'both on one layer, ' + shape(u or d)
    if len(bad) == 4:
        if len(u) in (0, 4): return '4-0'
        if len(u) in (1, 3): return '3-1'
        su, sd = shape(u), shape(d)
        if su == sd == 'adjacent':
            return '2-2, pairs stacked' if set(u) == set(d) else ('2-2, pairs on opposite sides' if not set(u) & set(d) else '2-2, pairs sharing one column')
        return f'2-2, {su} over {sd}'
    return f'{len(bad)} bad'
def merged(sub):          # 4a3 / 4b3 -> 4c3, 4a4 / 4b4 -> 4c4
    return '4c' + sub[2] if sub[:2] in ('4a', '4b') and sub[2] in '34' else sub
@functools.lru_cache(None)
def corner_cases():
    """id -> dict(sub, cs, layout, lmin, lmax, straight, setup).  cs is the merged corner subset (4c3, 4c4)."""
    out = {}
    for r in rows('corner_cases.csv'):
        out[r[0]] = dict(id=r[0], sub=r[1], cs=merged(r[1]), layout=layout(int(r[2])), lmin=int(r[5]), lmax=int(r[6]), straight=r[10], setup=r[9])
    return out
def cases(cs, pred=lambda c: True):
    return frozenset(k for k, c in corner_cases().items() if c['cs'] == cs and pred(c))

# ---- queries
def _match(v, want):
    if want is None: return True
    if callable(want): return want(v)
    if isinstance(want, (tuple, list, set, frozenset)): return v in want
    return v == want
@functools.lru_cache(None)
def _k5():
    out = []
    for s, a, b, tp, lo, hi, d, c in rows('k5_quick_reads.csv'):
        cs, e = s.split(); out.append((cs, int(e[0]), a, b, int(tp), int(lo), int(hi), int(d), int(c)))
    return out
def q(cs=None, e=None, pairs=None, hmin=None, hmax=None, cc=None, both=None, group=None, htr=None):
    """Histogram of optimal finish lengths.
    cs: corner subset or several.  e: bad edge count(s).  pairs: true pairs, 5 means five or more.
    hmin / hmax: shorter / longer of the two HTR lengths.  htr=(a, b): exactly those two lengths.
    cc: set of corner cases, the case on ONE side (each state counts half for each of its two sides).
    both=(X, Y): one side's case in X and the other side's in Y, in either order."""
    h = [0.0] * 19
    for xs, xe, a, b, tp, lo, hi, d, c in _k5():
        if not _match(xs, cs) or not _match(xe, e) or not _match(tp, pairs) or not _match(lo, hmin) or not _match(hi, hmax): continue
        if group is not None and QT[xs] != group: continue
        if htr is not None and (lo, hi) != tuple(sorted(htr)): continue
        w = 1.0
        if cc is not None:
            w = ((a in cc) + (b in cc)) / 2
            if not w: continue
        if both is not None:
            X, Y = both
            if not ((a in X and b in Y) or (a in Y and b in X)): continue
        h[d] += w * c
    return h
@functools.lru_cache(None)
def _h2():
    out = []
    for s, lo, hi, L, dLp, par, d, c in rows('h2_lengths.csv'):
        cs, e = s.split(); out.append((cs, int(e[0]), int(lo), int(hi), int(L), int(dLp), int(par), int(d), int(c)))
    return out
def q2(cs=None, e=None, hmin=None, hmax=None, L=None, Lp=None, parity=None, group=None, where=None):
    """Same, from the pass that has the corner length: L (optimal corner solution), Lp (best corner solution with the
    E-slice's parity of side turns), parity (0 even, 1 odd E-slice)."""
    h = [0] * 19
    for xs, xe, lo, hi, l, dlp, par, d, c in _h2():
        if not _match(xs, cs) or not _match(xe, e) or not _match(lo, hmin) or not _match(hi, hmax) or not _match(l, L) or not _match(l + dlp, Lp) or not _match(par, parity): continue
        if group is not None and QT[xs] != group: continue
        if where is not None and not where(dict(cs=xs, e=xe, hmin=lo, hmax=hi, L=l, Lp=l + dlp, parity=par)): continue
        h[d] += c
    return h

def fill(text, env):
    """Replace every {= python expression =} in text by its value."""
    def one(m):
        v = eval(m.group(1), env)
        return v if isinstance(v, str) else str(v)
    return re.sub(r'\{=\s*(.+?)\s*=\}', one, text)

if __name__ == '__main__':
    assert sum(q()) == TOT and sum(q2()) == TOT
    for cs in CS_ORDER:
        h = q(cs=cs); print(f'{cs}: {100*sum(h)/TOT:5.2f}% of DRs, average {avg(h):.2f}, in 9..13: ' + ' | '.join(pct(h, T) for T in WIDE), ' cases', len(cases(cs)))
