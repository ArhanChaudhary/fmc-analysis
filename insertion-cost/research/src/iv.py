#!/usr/bin/env python3
"""Shared numbers of the insertion-cost report.

  cell(typ, n, L, model, src)   one histogram of added moves from out/hist.json (built by histograms.py):
                                {"n": skeletons, "inf": without a solution within the cap, "h": {cost: count}}
                                src = 'sample' (the main runs, even lengths), 'base' (the same at odd lengths),
                                'mixed' (200 skeletons, n = 20, L = 10, with the model `mixed`), 'two12' (100
                                skeletons, n = 20, L = 12)
  mean(c), le(c, k), pct(c, k)  mean over the skeletons that have a solution; share of all skeletons with cost <= k
  head(typ)                     the model that is "the best that applies": `one` for 3c and 3e, `best` otherwise
Formatting is the first study's: 10% and up whole, 1-10% one decimal, under 1% two."""
import sys, json, functools, math
sys.path.insert(0, '/data/fmc/judging-a-dr/research/src')
from pv import fmt, num
O = '/data/fmc/insertion-cost/research/out/'
TYPES = ['3c', '2tc', '3tc', '2c2c-pure', '2c2c-twisted', '3c1t', '5c', '3c3c', '3e', '2f', '2e2e', '2e2e-flipped', '3e1f', '5e', '3e3e']
CORNER = TYPES[:8]; EDGE = TYPES[8:]
MAIN = ['3c', '2tc', '3tc', '2c2c-pure', '2c2c-twisted', '3c1t', '5c', '3e', '2e2e', '5e']
SHOW = {'3c': '3c', '2tc': '2tc', '3tc': '3tc', '2c2c-pure': 'pure 2c2c', '2c2c-twisted': 'twisted 2c2c', '3c1t': '3c1t', '5c': '5c', '3c3c': '3c3c',
        '3e': '3e', '2f': '2fe', '2e2e': '2e2e', '2e2e-flipped': 'flipped 2e2e', '3e1f': '3e1f', '5e': '5e', '3e3e': '3e3e'}
LONG = {'3c': 'a corner 3-cycle', '2tc': 'two corners twisted in place', '3tc': 'three corners twisted in place, all the same way',
        '2c2c-pure': 'two corner swaps, no twist', '2c2c-twisted': 'two corner swaps, each with a twist', '3c1t': 'a twisted corner 3-cycle and one twisted corner',
        '5c': 'a corner 5-cycle', '3c3c': 'two separate corner 3-cycles',
        '3e': 'an edge 3-cycle', '2f': 'two edges flipped in place', '2e2e': 'two edge swaps, no flip', '2e2e-flipped': 'two edge swaps, each with a flip',
        '3e1f': 'a flipped edge 3-cycle and one flipped edge', '5e': 'an edge 5-cycle', '3e3e': 'two separate edge 3-cycles'}
NS = [10, 14, 18, 20, 22, 26, 30]; ALLN = list(range(10, 31, 2))
@functools.lru_cache(None)
def _H(): return json.load(open(O + 'hist.json'))
def cell(typ, n, L, model, src='sample'):
    try: return _H()[src][typ][str(n)][str(L)][model]
    except KeyError: return None
def head(typ): return 'one' if typ in ('3c', '3e') else 'best'
def solved(c): return c['n'] - c['inf']
def mean(c):
    s = solved(c); return sum(int(k) * v for k, v in c['h'].items()) / s if s else float('nan')
def count_le(c, k): return sum(v for x, v in c['h'].items() if int(x) <= k)
def le(c, k): return count_le(c, k) / c['n']
def pct(c, k):
    g = count_le(c, k)
    return f"0 of {c['n']:,}" if g == 0 else fmt(g, c['n'])
def se(c):
    s = solved(c); m = mean(c)
    return (sum(v * (int(k) - m) ** 2 for k, v in c['h'].items()) / max(s - 1, 1) / s) ** 0.5
def _half_up(x, q):
    """x to the step q ('0.01'), an exact half rounded away from zero.  A mean like 40275 / 5000 = 8.055 is an exact
    half, and formatting the float alone sends such a value up or down by its binary digits (8.055 -> 8.05,
    8.685 -> 8.69).  Every number formatted here is a ratio of small whole numbers, so rounding to 9 places first
    gives its exact decimal back."""
    import decimal
    if x != x: return 'nan'
    return str(decimal.Decimal(repr(round(x, 9))).quantize(decimal.Decimal(q), rounding=decimal.ROUND_HALF_UP))
def f2(x): return _half_up(x, '0.01')
def f1(x): return _half_up(x, '0.1')
def what(typ, L, model=None, src='sample'):
    """The model in plain words."""
    model = model or head(typ); k = 'c' if typ in CORNER else 'e'
    if model == 'one': return f'one 3{k} comm of at most {L} moves'
    if model == 'direct': return f'one alg of at most {L} moves that does the whole leftover'
    if model in ('two', 'two_flat', 'two_apart'):
        tail = {'two': ', nesting allowed', 'two_flat': ', no nesting', 'two_apart': ', the two not touching'}[model]
        return f'two 3{k} comms of at most {L} moves each' + tail
    if model == 'mixed': return f'a 3{k} comm and one more comm or alg, each of at most {L} moves'
    return f'the best of two 3{k} comms and one alg for the whole leftover, each of at most {L} moves'
# ---- exchange rates between types
def cell_at(typ, n, L, model=None):
    """The histogram at a whole skeleton length: the main sample at the even lengths, the samples of the odd lengths
    (out/base_*, same generator and sizes) at the odd ones."""
    model = model or head(typ)
    return cell(typ, n, L, model, 'sample' if n % 2 == 0 else 'base')
def chance(typ, n, L, t, model=None):
    """P(total <= t) for a skeleton of length n.  A whole length is its own sample; a length between two whole ones
    (only used to read off a crossing) is the two neighbouring whole lengths mixed."""
    def at(m):
        c = cell_at(typ, m, L, model)
        return le(c, t - m) if c else None
    lo = int(math.floor(n + 1e-9))
    if abs(n - lo) < 1e-9: return at(lo)
    a, b = at(lo), at(lo + 1)
    if a is None or b is None: return None
    w = n - lo
    return (1 - w) * a + w * b
def equal_length(typ, L, t, p, model=None):
    """The skeleton length (real number) at which a `typ` skeleton has chance p of a total <= t: every whole length
    10..30 is evaluated on its own sample, and the crossing is interpolated on the log-odds."""
    pts = []
    for m in range(10, 31):
        v = chance(typ, m, L, t, model)
        if v is not None: pts.append((m, v))
    lg = lambda v: math.log(max(min(v, 1 - 1e-6), 1e-6) / (1 - max(min(v, 1 - 1e-6), 1e-6)))
    for (m0, v0), (m1, v1) in zip(pts, pts[1:]):
        if v0 >= p >= v1 and v0 > v1:
            return m0 + (lg(v0) - lg(p)) / (lg(v0) - lg(v1))
    return None
if __name__ == '__main__':
    for t in TYPES:
        for L in (8, 10):
            c = cell(t, 20, L, head(t))
            print(f"{t:14s} L={L} {head(t):5s} n={c['n']:6d} none={c['inf']:5d} mean={mean(c):.2f} +-{se(c):.3f}  <=6 {pct(c, 6)}  <=8 {pct(c, 8)}  <=10 {pct(c, 10)}")
    print('3c n=24 for 30:', chance('3c', 24, 8, 30), ' 5c with the same chance:', equal_length('5c', 8, 30, chance('3c', 24, 8, 30)))
