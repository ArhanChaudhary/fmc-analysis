#!/usr/bin/env python3
"""Names available inside {= ... =} in the write-up and errata sources.  Every number in the text comes through here:
from a cell of a generated table (report/data), or from the result files the tables are made from (research/out)."""
import json, csv, os, re, math, functools, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from halfup import hu, exact
O = '/data/fmc/eo-to-dr/research/out/'
D = '/data/fmc/eo-to-dr/report/data/'
csv.field_size_limit(10**8)
def _j(name): return json.load(open(O + name))
A = _j('a50k_stats.json'); B = _j('b_stats.json'); C = _j('c_stats.json'); E = _j('report_extra.json'); NB = _j('nissy50k_stats.json')
S500 = _j('s500_stats.json')
W = {w['id']: w for w in _j('witness.json')}
WX = _j('witness_extra.json')

def pc(x, d=None, rounded=False):
    """A share as a percentage: one decimal, two below 1%, more below 0.1%.  An exact half goes up (halfup.hu).
    rounded=True is for a share its result file has already rounded (5 decimals of a number that has more): a 5 in
    its last place is no half then, and it is formatted from the float as it always was.  So are the means of the
    result files (f2, f3, f4): they are kept to 3 or 4 decimals there."""
    share, x = x, float(x) * 100
    if x == 0: return '0%'
    if 99.95 <= x < 100 and d is None: return '>99.9%'
    if d is None: d = 1 if x >= 1 else 2 if x >= 0.1 else 3 if x >= 0.01 else 4
    return f'{x:.{d}f}%' if rounded else f'{hu(share, d, 100):.{d}f}%'
def f2(x): return f'{float(x):.2f}'
def f3(x): return f'{float(x):.3f}'
def f4(x): return f'{float(x):.4f}'
def n(x): return f'{int(x):,}'
def onein(p): return f'1 in {1 / float(p):.1f}' if isinstance(p, str) else f'1 in {hu(round(1 / p, 9), 1):.1f}'          # text: a share as its result file rounded it

@functools.lru_cache(None)
def _table(name):
    lines = [l for l in open(D + name + '.md').read().split('\n') if l.startswith('|')]
    cells = lambda l: [c.strip() for c in l.strip().strip('|').split('|')]
    return cells(lines[0]), [cells(l) for l in lines[2:]]
def CELL(name, row, col):
    head, rows = _table(name); key = (row,) if isinstance(row, str) else tuple(row)
    hit = [r for r in rows if tuple(r[:len(key)]) == key]
    assert len(hit) == 1, (name, row, len(hit))
    return hit[0][head.index(col)]

# ---- A1
A1N = {'fixed': 'fixed axis, exact (all 2,217,093,120 cosets)', 'pooled': 'fixed axis, all three axes pooled, sampled',
       'lin': 'best of 3 axes, normal (linear)', 'inv': 'best of 3 axes, inverse (linear)', 'six': 'best of 6 (3 axes x normal/inverse, linear)',
       'niss': 'NISS (moves on both sides), best of 3 axes'}
def A1(key, what, src=None):
    """A1 statistic: key in A1N, what = mean / p_le8 / p_le9 / p_le10 / max; src = None (uniform 50,000), 'nissy', '500'."""
    d = {None: A, 'nissy': NB, '500': S500}[src]['a1'][A1N[key]][what]
    return f2(d) if what == 'mean' else str(d) if what == 'max' else pc(d, rounded=key in ('fixed', 'pooled'))     # the others are counts out of 50,000 or 500
def A1D(key, what):
    """Difference uniform - nissy scramble of an A1 statistic (mean in turns, shares in points)."""
    a, b = A['a1'][A1N[key]][what], NB['a1'][A1N[key]][what]
    return f2(a - b) if what == 'mean' else f'{hu(abs(exact(a) - exact(b)), 1, 100):.1f}'
def SE(key):
    """Standard error of an A1 mean on the 50,000."""
    return f'{hu(E["sd_" + key] / math.sqrt(E["n"]), 3):.3f}'
def GAIN(which, g):
    d = A['a1'][which]; return pc(d[str(g)] / E['n'])
def GAINGE(which, g):
    d = A['a1'][which]; return pc((E['n'] - sum(v for k, v in d.items() if int(k) < g)) / E['n'])
def X(key): return E[key]
def XP(key): return pc(E[key])
def NOPT(): return f'{E["nopt_mean"]:.1f}'
def EST(k, op='le'):
    h = A['estar_hist']; t = sum(h.values())
    return pc(sum(v for kk, v in h.items() if (int(kk) <= k if op == 'le' else int(kk) >= k)) / t)

# ---- A2
@functools.lru_cache(None)
def _a2():
    return {(r['eo_kind'], int(r['k'])): r for r in csv.DictReader(open(O + 'a50k_a2.tsv'), delimiter='\t')}
A2K = {'n': 'normal EOs, DR on normal', 'b': 'normal or inverse EOs, DR on the same side',
       'x': 'normal, inverse and NISS EOs, NISS DR side rule', 'x6': 'normal, inverse and NISS EOs, against the best of 6'}
def A2(kind, k, col):
    v = _a2()[(A2K[kind], k)][col]
    return f2(v) if col.startswith('mean') else pc(v)
def A2NOT(kind, k):
    """Share of scrambles where the best route through an EO of at most k is longer than the optimal (reference)."""
    return pc(1 - exact(_a2()[(A2K[kind], k)]['p_equals_optimal']) - exact(_a2()[(A2K[kind], k)]['p_better_than_optimal_ref'] or 0))
def G(key, what):
    v = A['a3_gains'][key][what]
    return pc(v, rounded=what in ('p_improves_given_eo_le4', 'p_other_axes_better')) if what.startswith('p_') else f2(v)     # those two are shares of a part of the scrambles

# ---- B
def BOPT(kind, what):
    d = B[kind]
    if what == 'mean': return f3(d['mean'])
    if what.startswith('le'):
        k = int(what[2:]); t = sum(d['hist'].values())
        return pc(sum(v for kk, v in d['hist'].items() if int(kk) <= k) / t)
    if what.startswith('eq'):
        k = what[2:]; t = sum(d['hist'].values()); return pc(d['hist'].get(k, 0) / t)
def B4(eos, axes, k, what):
    r = E['b4'][f'{eos}|{axes}|{k}'][what]
    return pc(r) if what.startswith('p_') else f'{float(r):.1f}' if what == 'mean_le' else f'{hu(float(r)):,.0f}'
def B5(bad, col): return pc(E['b5'][str(bad)][col], rounded=True)
def LAY(key): return B['layouts'][key]
def GAP(kind, key): return pc(A[f'gap_{kind}'][key])
def MORE3(kind): return pc(A[f'more3than4_{kind}'])

# ---- C
def C7(opt, col):
    r = E['c7'][opt]
    return f3(r[col]) if col == 'mean' else r[col] if col in ('one_in_le6', 'max', 'states') else pc(r[col], rounded=True)
C7N = {'plain': 'one DR axis, EO kept, normal (the known table)', 'any': 'one DR axis, any turns (EO may break)',
       'switch': 'one DR axis, EO kept, last EO turn inverted if better', 'anyswitch': 'one DR axis, any turns, last EO turn inverted if better',
       'two': 'better of the two DR axes, EO kept', 'inv': 'one DR axis, EO kept, on the inverse only',
       'ni': 'one DR axis, EO kept, better of normal and inverse', 'twosw': 'two DR axes x last turn inverted, EO kept, normal',
       'twoni': 'two DR axes x normal/inverse, EO kept', 'allkept': 'two axes x normal/inverse x last turn, EO kept',
       'anytwo': 'two DR axes, any turns, normal', 'all': 'everything above (EO kept or not)'}
def CT(key, col): return C7(C7N[key], col)
def C6(case, col):
    v = E['c6'][case][col]; file = isinstance(v, str)          # as the result file rounded it; a float was recomputed from the counts (xtables.c6rows)
    return (f2(v) if file else f'{hu(v, 2):.2f}') if col.endswith('mean') else f'{float(v):,.1f}' if col == 'one_in' else n(v) if col == 'cosets' else pc(v, rounded=file)
def C6ONEIN(case, col): return onein(E['c6'][case][col])
def NI(case, col):
    v = E['c6ni'][case][col]
    return v if col == 'correlation' else pc(v, rounded=True) if v else '–'
def NIRANGE(minstates=1000):
    v = [float(r['correlation']) for k, r in E['c6ni'].items() if k != 'all' and int(r['states']) >= minstates]
    return f'{min(v):.3f}', f'{max(v):.3f}', str(len(v))
def CSTAT(*path):
    v = C
    for p in path: v = v[p]
    return v
def BINOM(k, nn, p):
    """P(at most k successes in nn independent trials with chance p)."""
    return sum(math.comb(nn, i) * p ** i * (1 - p) ** (nn - i) for i in range(k + 1))

# ---- witnesses
def WIT(i, *path):
    v = W[i]
    for p in path: v = v[p]
    return v
def WXX(i, *path):
    v = WX[i]
    for p in path: v = v[p] if not isinstance(v, list) else v[int(p)]
    return v
def NTOK(seq): return str(len(seq.split()))
@functools.lru_cache(None)
def _checks():
    rows = list(csv.DictReader(open(O + 'checks_nissy.tsv'), delimiter='\t'))
    return sum(int(r['positions']) for r in rows), sum(int(r['agree']) for r in rows), len(rows)
def CHK(i): return f'{_checks()[i]:,}'
ENV = {k: v for k, v in globals().items() if not k.startswith('_')}

# ---- bad-edge layouts (exact, ordered triples)
@functools.lru_cache(None)
def _lay():
    from fractions import Fraction
    rows = list(csv.DictReader(open(O + 'b5_layouts.tsv'), delimiter='\t'))
    return [((int(r['bad_fb']), int(r['bad_rl']), int(r['bad_ud'])), Fraction(r['probability'])) for r in rows]
def LAYP(pred):
    """Exact probability that the (F/B, R/L, U/D) bad-edge counts satisfy pred, as a share."""
    return pc(sum(p for t, p in _lay() if pred(t)))
def LAYF(pred):
    from fractions import Fraction
    f = sum(p for t, p in _lay() if pred(t)); return f'{f.numerator}/{f.denominator}'
def INDEP(triple):
    """The chance of a sorted triple if the three axes were independent (each binomial without odd counts)."""
    from math import comb
    from itertools import permutations
    one = lambda b: comb(12, b) / 2048
    return pc(sum(one(a) * one(b) * one(c) for a, b, c in set(permutations(triple))))
def RATIO_2_10_10():
    from itertools import permutations
    from math import comb
    ex = float(sum(p for t, p in _lay() if sorted(t) == [2, 10, 10]))
    ind = sum(comb(12, a) * comb(12, b) * comb(12, c) / 2048 ** 3 for a, b, c in set(permutations((2, 10, 10))))
    return f'{hu(ind / ex, 1):.1f}'
ENV.update({k: v for k, v in list(globals().items()) if not k.startswith('_')})
def B4X(L, col):
    r = [r for r in csv.DictReader(open(O + 'b4_one_axis_exact.tsv'), delimiter='\t') if r['length'] == str(L)][0]
    return f'{float(r[col]):.1f}' if col.startswith('mean') else r[col]
def B5H(bad, L):
    h = dict(x.split(':') for x in E['b5'][str(bad)]['optimal_hist'].split())
    return h.get(str(L), '0')
def B5N(bad): return str(sum(int(v) for v in dict(x.split(':') for x in E['b5'][str(bad)]['optimal_hist'].split()).values()))
def NONE5(): return str(round(float(E['b4']['NISS (normal, inverse, both)|all three axes|5']['p_none_le']) * E['n']))
ENV.update({k: v for k, v in list(globals().items()) if not k.startswith('_')})
def PRIOR(measure, col):
    r = [r for r in csv.DictReader(open(O + 'compare_prior.tsv'), delimiter='\t') if r['measure'] == measure][0]
    return n(r[col]) if col.endswith('_n') else r[col]
ENV.update({k: v for k, v in list(globals().items()) if not k.startswith('_')})
@functools.lru_cache(None)
def _eo0(which='eo-fb_dr'):
    return {int(a): int(b) for a, b in (l.split() for l in open(O + f'eo0_hist_{which}.txt') if l[0].isdigit())}
def EODR(k, which='eo-fb_dr', op='eq'):
    """Exact share of EO-solved states at EO-to-DR distance k (op 'eq', 'le', 'ge'); which = eo-fb_dr (EO kept) or all_dr."""
    h = _eo0(which); t = sum(h.values())
    v = sum(c for d, c in h.items() if (d == k if op == 'eq' else d <= k if op == 'le' else d >= k))
    return pc(v / t)
def EODRN(k, which='eo-fb_dr'): return n(_eo0(which).get(k, 0))
def EODRT(which='eo-fb_dr'): return n(sum(_eo0(which).values()))
def EO1(): return f"{float(B['one_axis_optimal_mean'].split('=')[1]):.3f}"
def CHI(scr, axis, what):
    r = [r for r in csv.DictReader(open(O + 'checks_scrambles.tsv'), delimiter='\t') if r['scrambles'] == scr and r['axis'] == axis and r['what'] == what][0]
    return r['chi2']
def CHIMAX(scr):
    return max(float(r['chi2']) for r in csv.DictReader(open(O + 'checks_scrambles.tsv'), delimiter='\t') if r['scrambles'] == scr)
def NSAMP(which): return n({'c': C['sampled_states'], 'b': B['sample_states']}[which])
ENV.update({k: v for k, v in list(globals().items()) if not k.startswith('_')})
def COSETS(): return n([r for r in csv.DictReader(open(O + 'a50k_a1.tsv'), delimiter='\t')][0]['n'])
def B5P(bad):
    from fractions import Fraction
    return pc(float(Fraction(E['b5'][str(bad)]['p_state'])))
@functools.lru_cache(None)
def _co():
    """Every corner orientation on one axis (3^7, the last corner fixed by the others): (twisted count, cw, ccw)."""
    from itertools import product
    out = []
    for t in product(range(3), repeat=7):
        t = t + ((-sum(t)) % 3,)
        out.append((sum(1 for x in t if x), t.count(1), t.count(2)))
    return out
def TWIST(k): return str(sum(1 for c in _co() if c[0] == k))
def TWIST_ALL(): return n(len(_co()))
def TWIST6SAME(): return str(sum(1 for c in _co() if c[0] == 6 and (c[1] == 6 or c[2] == 6)))
ENV.update({k: v for k, v in list(globals().items()) if not k.startswith('_')})

def CHIP(scr, axis, what):
    """p-value of a chi-squared test row of checks_scrambles.tsv (upper tail, by the series of the regularized gamma)."""
    r = [r for r in csv.DictReader(open(O + 'checks_scrambles.tsv'), delimiter='\t') if r['scrambles'] == scr and r['axis'] == axis and r['what'] == what][0]
    x, k = float(r['chi2']) / 2, int(r['df']) / 2
    s, term, i = 0.0, 1.0 / k, 0
    while term > 1e-15:
        s += term; i += 1; term *= x / (k + i)
    p = 1 - math.exp(-x + k * math.log(x) - math.lgamma(k)) * s
    if p >= 0.001:
        return f'{p:.1g}'
    m, e = f'{p:.0e}'.split('e')
    return f'${m}\\cdot 10^{{{int(e)}}}$'
ENV.update({k: v for k, v in list(globals().items()) if not k.startswith('_')})
def COSETS3(): return f"{hu(int(COSETS().replace(',', '')) / 3 / 1e6):.0f} million"
ENV.update({k: v for k, v in list(globals().items()) if not k.startswith('_')})
def CASELE(c, e, k, option='eo'):
    """Exact share of the EO-solved states of case <c>c<e>e at distance at most k (option eo, any, eo_switchF, ...)."""
    r = [r for r in csv.DictReader(open(O + 'eodr_exact.tsv'), delimiter='\t') if r['corners'] == str(c) and r['edges'] == str(e) and r['option'] == option][0]
    h = [int(r[f'd{i}']) for i in range(12)]
    from fractions import Fraction
    return Fraction(sum(h[:k + 1]), sum(h))
ENV.update({k: v for k, v in list(globals().items()) if not k.startswith('_')})
def SCR(i):
    """A witness scramble as printed: adjacent same-face turns merged (same position, checked in xwitness.py)."""
    return WX['scr'][i]
ENV.update({k: v for k, v in list(globals().items()) if not k.startswith('_')})
# nissy 2.0.8 `scramble`: ep = rand() % 12! with glibc's rand() in [0, 2^31 - 1]
RANDN = 2 ** 31; F12 = math.factorial(12)
def NISSYBIAS(what):
    low = RANDN - (RANDN // F12) * F12           # indices below this come up RANDN // F12 + 1 times, the rest RANDN // F12
    if what == 'ratio': return f'{hu(RANDN / F12, 2):.2f}'
    if what == 'low': return n(low)
    if what == 'lowshare': return pc(low / F12)
    if what == 'more': return pc((RANDN // F12 + 1) / (RANDN // F12) - 1, 0)
def XN(key, d=2): return f'{hu(E[key], d):.{d}f}'
def XC(key): return n(round(E[key] * E['n'])) if isinstance(E[key], float) else n(E[key])
def BRK(k): return n(round(float(_a2()[(A2K['n'], k)]['p_needs_eo_breaking']) * E['n']))
ENV.update({k: v for k, v in list(globals().items()) if not k.startswith('_')})
def A1COUNT(key, d):
    r = [r for r in csv.DictReader(open(O + 'a50k_a1.tsv'), delimiter='\t') if r['what'] == A1N[key]][0]
    return n(r[f'n{d}'])
ENV.update({k: v for k, v in list(globals().items()) if not k.startswith('_')})
# ---- nissy's default EO listing against -a (out/default_listing.json, default_listing.py: the first 150 scrambles)
DL = _j('default_listing.json')
def DLK(k, kind, which): return DL[f'le{k}'][kind][which]
def DLP(k, kind):
    """Share of the -a EOs of at most k (normal, inverse, one_sided, two_sided, niss) that nissy's default listing keeps."""
    from fractions import Fraction
    return pc(Fraction(DLK(k, kind, 'default'), DLK(k, kind, 'all')))
def DLPER(k, what, which='niss_default_per_scramble'):
    """Mean or median per scramble of the default NISS listing (all axes) of EOs of at most k, on those scrambles."""
    v = DL[f'le{k}'][which][what]
    return f'{hu(v, 1):.1f}' if what == 'mean' else f'{hu(v, 1):g}' if v != int(v) else str(int(v))
# ---- the cases with no edge out of place, where the other EO is solved too (out/both_eo.json, both_eo.py)
BE = _j('both_eo.json')
def BOTH(key, what=None):
    v = BE[key] if what is None else BE[key][what]
    return n(v)
def BOTHCASES(): ks = sorted(BE['cases'], key=lambda c: int(c.split('c')[0])); return f'{ks[0]} to {ks[-1]}'
# ---- Cale's table for switching the RZP's last move on a 4c4e ([[T4264]], its image): 19,226 of 70,560 in 6 or fewer
CALE_RZP_4C4E = (19226, 70560)
def CALE_RZP(what):
    from fractions import Fraction
    k, t = CALE_RZP_4C4E
    assert t == int(E['c6']['4c4e']['cosets'])                # the same 4c4e states as here
    p = Fraction(k, t)
    return pc(p) if what == 'p' else pc(BINOM(3, 27, p))
def EDGESTATES(pred):
    """Edge states (12! * 2^11) whose bad-edge counts satisfy pred: the exact share of the layouts times the states."""
    from fractions import Fraction
    v = Fraction(LAYF(pred)) * math.factorial(12) * 2 ** 11
    assert v.denominator == 1
    return n(v.numerator)
ENV.update({k: v for k, v in list(globals().items()) if not k.startswith('_')})
SWITCHED = ('4c4e', '4c2e', '3c2e', '7c8e', '3c4e', '8c8e')      # the cases people switch from (sec_claims, Noah Swor's and mrauo's lists, Jay's T1802)
def SWCORR():
    """A bound on |correlation| of normal and inverse within those cases: the largest, rounded up to 3 decimals."""
    return f'{math.ceil(max(abs(float(E["c6ni"][c]["correlation"])) for c in SWITCHED) * 1000) / 1000:.3f}'
ENV.update({k: v for k, v in list(globals().items()) if not k.startswith('_')})
