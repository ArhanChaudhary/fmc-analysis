#!/usr/bin/env python3
"""Step 2: reproduce the published tables of the notes (section C) from the exact distances and the features.
Exact tables must match to their printed rounding; sampled ones within 3 standard errors.  Output:
out/reproduce.tsv (one line per published number) and a printed summary of mismatches."""
import os, sys, math
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import pop, geom
F = pop.feat(); d = F['d'].astype(int); N0 = geom.N0
sub7 = d <= 6
rows = []
MODE = {'d': d}
def dec(x):
    s = str(x)
    return len(s.split('.')[1]) if '.' in s else 0
def check(source, what, pub, ours, n=None, kind='exact', sample_n=None, note=''):
    """pub: printed number (float or int; None = printed as '-'), ours: exact value."""
    if kind == 'set':
        ok = pub == ours; verdict = 'match' if ok else 'mismatch'
    elif pub is None:
        ok = (n == 0 or n is None); verdict = 'match' if ok else 'mismatch'; tol = ''
    elif kind == 'exact':
        tol = 0.5 * 10 ** -dec(pub) + 1e-9
        if isinstance(pub, str): pub = float(pub)
        ok = abs(ours - float(pub)) <= tol; verdict = 'match' if ok else 'mismatch'
    elif kind == 'percent':
        tol = 0.5 * 10 ** -dec(pub) + 1e-9
        ok = abs(100 * ours - float(pub)) <= tol; verdict = 'match' if ok else 'mismatch'
    else:  # sampled: binomial, sample_n draws
        se = math.sqrt(max(ours * (1 - ours), 1e-9) / sample_n)
        half = 0.5 * 10 ** -dec(pub) * (0.01 if kind == 'sampled_percent' else 1)
        pv = float(pub) * (0.01 if kind == 'sampled_percent' else 1)
        z = max(0.0, abs(pv - ours) - half) / se; ok = z <= 3
        verdict = f'within error (z={z:.2f})' if ok else f'outside error (z={z:.2f})'
    rows.append((source, what, '-' if pub is None else str(pub), f'{ours:.5f}' if isinstance(ours, float) else str(ours), '' if n is None else str(n), verdict, note))
    return ok

def stat(m):
    dd = MODE['d']; n = int(m.sum())
    return n, (float(dd[m].mean()) if n else float('nan')), (float((dd[m] <= 6).mean()) if n else float('nan'))
def drm(c, e): return (F['drm_c'] == c) & (F['drm_e'] == e)
def arm(a, b): return (F['carm'] == a) & (F['earm'] == b)
CASES = {'a': 0, 'b': 1, 'c': 2, 'd': 3}
def case(letter, suffix=None, rodney=False):
    m = F['corner_case'] == CASES[letter]
    if suffix is not None:
        if rodney and letter == 'a' and suffix == 0: m &= (F['carm'] == 0) | (F['carm'] == 4)   # stats.py select(): 4a-0 -> corner_arm in [0, 4]
        else: m &= F['case_suffix'] == suffix
    return m

# ---- C1 Cale, C9 Rodney ranking, A1 counts
m44 = drm(4, 4)
check('C1 Cale (doc 6)', '4c4e: 1 in 15.3 EOs', 15.3, N0 / m44.sum(), m44.sum())
check('A1 Rodney (doc 275)', 'states with a sub-7 solution, "approximately 64,000"', 64000, int(sub7.sum()), N0, kind='exact', note='printed as approximate; 64,103')
rows[-1] = rows[-1][:5] + ('match (approximate figure)',) + rows[-1][6:]
check('A1 / C9 Rodney', 'N(sub-7) 4c4e', 13576, int(sub7[m44].sum()), m44.sum())
for (c, e), p, N in [((4, 4), .192, 13576), ((3, 2), .616, 2208), ((7, 8), .164, 3856), ((5, 4), .072, 6784), ((5, 6), .061, 7696),
                     ((4, 2), .187, 2512), ((6, 6), .056, 7712), ((4, 6), .046, 4344), ((3, 4), .099, 1872), ((8, 8), .145, 872)]:
    m = drm(c, e)
    check('C9 Rodney DRM_Ranking.csv', f'{c}c{e}e p(sub-7)', p, float(sub7[m].mean()), m.sum())
    check('C9 Rodney DRM_Ranking.csv', f'{c}c{e}e N(sub-7)', N, int(sub7[m].sum()), m.sum())
# doc 521 tree counts (4c4e)
for what, mm, cnt in [('n_pairs = 0', F['pairs'] == 0, 21000), ('n_pairs >= 2', F['pairs'] >= 2, 18360), ('n_pairs >= 3', F['pairs'] >= 3, 2520)]:
    check('C9 Rodney trees (doc 521)', f'4c4e {what}: cases', cnt, int((m44 & mm).sum()), m44.sum())
# A2 counts
six = F['drm_c'] == 6
co_six = np.array([sum(1 for t in geom.CT[co] if t) == 6 for co in range(geom.N_CO)])
co_60 = np.array([sorted([list(geom.CT[co]).count(1), list(geom.CT[co]).count(2)]) == [0, 6] for co in range(geom.N_CO)])
check('A2 WRITEUP 6', 'six-twist orientations', 616, int(co_six.sum()))
check('A2 WRITEUP 6', '6+0 among them', 56, int(co_60.sum()))
co_44 = np.array([sorted([list(geom.CT[co]).count(1), list(geom.CT[co]).count(2)]) == [4, 4] for co in range(geom.N_CO)])
co_71 = np.array([sorted([list(geom.CT[co]).count(1), list(geom.CT[co]).count(2)]) == [1, 7] for co in range(geom.N_CO)])
check('A2 FakeMMAP (T9543-T9549)', '4+4 orientations', 70, int(co_44.sum()))
check('A2 FakeMMAP (T9543-T9549)', '7+1 orientations', 16, int(co_71.sum()))
# T7422: which ARM each case can have
for letter, allowed in [('a', {0, 2, 4}), ('b', {0, 2, 4}), ('c', {1, 3}), ('d', {2})]:
    got = set(np.unique(F['carm'][m44 & case(letter)]).tolist())
    check('A5 Rodney (T7422)', f'4{letter} corner ARM values {sorted(allowed)}', str(sorted(allowed)), str(sorted(got)), kind='set', note='as sets')

m78 = drm(7, 8); m42 = drm(4, 2)
# ---- C6 Louis twist splits (edges ignored)
for nc, maj, p in [(6, 3, .03694), (6, 6, .07186), (8, 4, .03097), (8, 7, .01616)]:
    mm = (F['drm_c'] == nc) & (F['twist_major'] == maj)
    check('C6 Louis (T4511-T4512)', f'{nc}c twist split {maj}+{nc - maj} sub-7', p, stat(mm)[2], int(mm.sum()))
# ---- C7 Louis corner case x ARM (4c4e)
for letter, code, p in [('a', '00', .67), ('b', '00', .38), ('d', '21', .78), ('b', '21', .36), ('a', '21', .20), ('a', '42', .66), ('b', '42', .22)]:
    mm = m44 & case(letter) & arm(int(code[0]), int(code[1]))
    check('C7 Louis (T7454-T7455)', f'4c4e 4{letter} ARM {code} sub-7', p, stat(mm)[2], int(mm.sum()))
check('C7 Louis (T7455)', '4c4e AR-1c0e sub-7 ("0.28 vs 0.29")', .28, stat(m44 & arm(1, 0))[2], int((m44 & arm(1, 0)).sum()), note='read as the mirror pair AR-1c0e / AR-3c2e (T7438)')
check('C7 Louis (T7455)', '4c4e AR-3c2e sub-7 ("0.28 vs 0.29")', .29, stat(m44 & arm(3, 2))[2], int((m44 & arm(3, 2)).sum()))
# ---- C8 Rodney corner case x pairs
c8 = {('a', 0): ([.0463, .1597, .5185, None, .9722], [1512, 1152, 1296, 0, 72]),
      ('a', 2): ([.04861, .1731, .3681, .5278], [2304, 3744, 1728, 288]),
      ('b', 0): ([0, .02778, .1528, .6389], [2880, 2880, 1728, 576]),
      ('b', 2): ([.09107, .1601, .5192, .9167, 1], [4656, 7296, 3744, 384, 48]),
      ('c', 1): ([.02257, .1036, .39, .8889], [9216, 14976, 6912, 1152]),
      ('d', 2): ([.2222, .4444, .6852], [432, 1152, 432])}
for (letter, suf), (ps, ns) in c8.items():
    for k, (p, n) in enumerate(zip(ps, ns)):
        mm = m44 & case(letter, suf, rodney=True) & (F['pairs'] == k); N, A, P = stat(mm)
        check('C8 Rodney corner variant+pair (doc 274)', f'4c4e 4{letter}-{suf} {k} pairs n', n, N)
        if p is not None: check('C8 Rodney corner variant+pair (doc 274)', f'4c4e 4{letter}-{suf} {k} pairs sub-7', p, P, N)
c8b = {('a', 0): [.017, .083, .25], ('a', 2): [.056, .417, .833], ('b', 0): [.083, .604, .792], ('b', 2): [.028, .208, .375], ('c', 1): [.042, .326, .646], ('d', 2): [.167, .5]}
for (letter, suf), ps in c8b.items():
    for k, p in enumerate(ps):
        mm = m42 & case(letter, suf, rodney=True) & (F['pairs'] == k)
        check('C8 Rodney corner variant+pair (doc 274)', f'4c2e 4{letter}-{suf} {k} pairs sub-7', p, stat(mm)[2], int(mm.sum()))
for k, p in zip(range(1, 7), [0, .02143, .03333, .1586, .5429, .9167]):
    mm = m78 & (F['pairs'] == k)
    check('C8 Rodney corner variant+pair (doc 274)', f'7c8e {k} pairs sub-7', p, stat(mm)[2], int(mm.sum()))
# ---- C15 Radek (percent)
for k, p in [(0, 4.33), (1, 13.28), (2, 41.09), (3, 79), (4, 98.33)]:
    mm = m44 & (F['pairs'] == k)
    check('C15 Radek B (image D7480)', f'4c4e {k} pairs sub-7 (%)', p, stat(mm)[2], int(mm.sum()), kind='percent')
# ---- C16 beef beans (exact meaning: p(sub-7 | DRM, ARM))
for (c, e), (a, b), p in [((4, 4), (2, 1), .3429), ((5, 4), (2, 1), .1515)]:
    mm = drm(c, e) & arm(a, b)
    check('C16 beef beans (doc 209)', f'{c}c{e}e/{a}c{b}e p', p, stat(mm)[2], int(mm.sum()), kind='sampled', sample_n=max(1, int(5994 * 0.0784)) if c == 4 else 300,
          note='sampled (5994 sub-7 EOs); per-cell sample size not stated, taken as the cell share of 5994')
# ---- C12 Evan subtypes (sample, ~1000 per subtype)
ev = {'0c0e': [.663, .384, None], '0c1e': [.187, .032, None], '0c2e': [.009, 0, None], '2c0e': [.189, .106, .009], '2c1e': [.203, .366, .782], '2c2e': [.179, .069, .005]}
for code, ps in ev.items():
    for letter, p in zip('abd', ps):
        if p is None: continue
        mm = m44 & arm(int(code[0]), int(code[2])) & case(letter)
        check('C12 Evan subtypes (doc 110)', f'4c4e AR-{code} {"2/2A 2/2B 4/0".split()["abd".index(letter)]} sub-7', p, stat(mm)[2], int(mm.sum()), kind='sampled', sample_n=1000)
# ---- C13 Evan arm/pairs 44 tab (sample)
check('C13 Evan arm/pairs (doc 276)', '4c4e ARM 21 sub-7', .344, stat(m44 & arm(2, 1))[2], int((m44 & arm(2, 1)).sum()), kind='sampled', sample_n=int(1171847 * 14976 / 70560))
for k, p in [(2, .394), (3, .758)]:
    mm = m44 & (F['pairs'] == k)
    check('C13 Evan arm/pairs (doc 276)', f'4c4e {k} pairs sub-7', p, stat(mm)[2], int(mm.sum()), kind='sampled', sample_n=int(1171847 * mm.sum() / 70560))
# Evan's arm/pairs, tab 44 (sampled): the ALL and PAIRS blocks are one sample of 1,171,847 whose own sub-7 total is 0.185;
# the ARM block is a separate sample (its fifteen ARM totals add up to exactly 1,000,000) and matches the uniform rates.
# The sheet's exact tab, 44-more (70,560 cases), has 2 pairs 0.411 and 3 pairs 0.79.  Written to out/sheet_notes.json.
import json
_ev = dict(n=1171847, all6=.185, n_arm=1000000, more2=.411, more3=.79, more_n=70560)
_p = float(sub7[m44].mean()); _ev['uniform6'] = _p
_ev['z_all'] = (abs(_ev['all6'] - _p) - 0.0005) / math.sqrt(_p * (1 - _p) / _ev['n'])      # beyond the rounding of 0.185
_ev['z_plain'] = abs(_ev['all6'] - _p) / math.sqrt(_p * (1 - _p) / _ev['n'])               # from the printed 0.185
_ev['exact2'] = float(stat(m44 & (F['pairs'] == 2))[2]); _ev['exact3'] = float(stat(m44 & (F['pairs'] == 3))[2])
assert abs(_ev['exact2'] - _ev['more2']) < 0.0005 and abs(_ev['exact3'] - _ev['more3']) < 0.005 and int(m44.sum()) == _ev['more_n']
json.dump(dict(evan=_ev), open(os.path.join(pop.OUT, 'sheet_notes.json'), 'w'), indent=1)
# ---- C18 WRITEUP (exact one axis; options)
T6 = pop.targets(6)
for nm, key, p in [('one axis', 'plain', 19.2), ('last turn', 'lastF', 28.1), ('two axes', 'two', 25.4), ('normal or inverse', 'inv', 34.8)]:
    check('C18 WRITEUP 5.1', f'4c4e <=6 {nm} (%)', p, float(T6[key][m44].mean()), int(m44.sum()), kind='percent')
for nm, key, p in [('one axis', 'plain', 5.9), ('last EO turn either way', 'lastF', 9.5), ('better of two DR axes', 'two', 11.3)]:
    check('C18 WRITEUP 5.1', f'all states <=6 {nm} (%)', p, float(T6[key].mean()), N0, kind='percent')
check('C18 WRITEUP 5.1', 'all states <=6 better of normal and inverse (%)', 11.2, float(T6['inv'].mean()), N0, kind='sampled_percent', sample_n=10**7, note='sampled there (10,000,000 states, 11.15%), printed 11.2; exact 11.14%')
# ---- C2 Cale switching the last move
check('C2 Cale (doc 40) / D2200 Tom Nelson', '4e4c in 6: 1 in 5.2 normally', 5.2, 1 / float(T6['plain'][m44].mean()), int(m44.sum()))
check('C2 Cale (doc 40) / D2200 Tom Nelson', '4e4c in 6: 1 in 3.6 with the last move switchable', 3.6, 1 / float(T6['lastF'][m44].mean()), int(m44.sum()))
# ---- write
with open(os.path.join(pop.OUT, 'reproduce.tsv'), 'w') as f:
    f.write('source\tquantity\tpublished\tours\tstates\tverdict\tnote\n')
    for r in rows: f.write('\t'.join(r) + '\n')
bad = [r for r in rows if not (r[5].startswith('match') or r[5].startswith('within'))]
print(f'{len(rows)} published numbers checked; {len(rows) - len(bad)} match / within error; {len(bad)} do not')
for r in bad: print('  ', ' | '.join(r))
