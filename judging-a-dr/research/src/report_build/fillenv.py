"""The names available inside {= ... =} in the report sources.  Every number in the guide comes through these."""
import sys
sys.path.insert(0, '/data/fmc/judging-a-dr/research/src')
import pv
from pv import q, q2, tri, quad, pct, share, avg
T = tri
def S(ids): return frozenset(ids.split()) if isinstance(ids, str) else frozenset(ids)
def _ok(h, what):
    assert sum(h) > 0, f'no DR states match: {what}'
    return h
def E(cs, e): return tri(_ok(q(cs=cs, e=e), (cs, e)))
def PR(cs, n, e=None): return tri(_ok(q(cs=cs, e=e, pairs=n), (cs, 'pairs', n, e)))
def HX(cs, x, e=None): return tri(_ok(q(cs=cs, e=e, hmax=x), (cs, 'hmax', x, e)))
def HB(cs, a, b, e=None): return tri(_ok(q(cs=cs, e=e, htr=(a, b)), (cs, 'htr', a, b, e)))
def C1(cs, ids, e=None): return tri(_ok(q(cs=cs, e=e, cc=S(ids)), (cs, 'cc', ids, e)))
def C2(cs, X, Y, e=None): return tri(_ok(q(cs=cs, e=e, both=(S(X), S(Y))), (cs, 'both', X, Y, e)))
def SH(cs, h): return f'{100 * sum(h) / sum(q(cs=cs)):.0f}%'
def _pairs(cs):
    ids = sorted(pv.cases(cs), key=int); out = []
    for i, a in enumerate(ids):
        for b in ids[i:]:
            h = q(cs=cs, both=({a}, {b}))
            if sum(h): out.append((avg(h), h))
    out.sort(key=lambda t: t[0]); return out
def XPH(cs, which): return _pairs(cs)[0 if which == 'best' else -1][1]
def KEEP(cs, keep_if, T):
    """Share of the finishes in T that survive when only DRs whose shorter HTR satisfies keep_if are kept."""
    kept = q(cs=cs, hmin=keep_if); allh = q(cs=cs)
    return f'{100 * sum(kept[:T + 1]) / sum(allh[:T + 1]):.0f}%'
def XP(cs, which): return tri(_pairs(cs)[0 if which == 'best' else -1][1])
def XPS(cs, which): return SH(cs, _pairs(cs)[0 if which == 'best' else -1][1])
# ---- the prune list for an 11-move DR (guide.md): what needs no solving, boiled down
_HIGH = ('2c5', '4b5', '4c4', '0c3', '0c4')
_G24 = S('8 7 24')       # 2c4: not stacked, and a qt goes straight to 2c3 or 4b3
_G43 = S('32 30')        # 4c3: the 4a3 side is 2-2 with a qt straight to 4b2
_W42 = S('31 4')         # 4a2: 2-2 with the pairs on opposite sides, or all four on one layer
def _dropped(cs, e, a, b, tp, lo, hi):
    if cs in _HIGH: return True
    if cs == '2c4': return not ((a in _G24 and b in _G24) or tp >= 4)
    if cs == '4c3': return not (a in _G43 or b in _G43 or tp >= 4)
    if cs == '4a2':
        if e == 4: return a in _W42 and b in _W42
        return a != '42' and b != '42'
    return False
def _prune(group=None):
    n = [0] * 19; dn = [0] * 19
    for cs, e, a, b, tp, lo, hi, d, c in pv._k5():
        if group and pv.QT[cs] != group: continue
        n[d] += c
        if _dropped(cs, e, a, b, tp, lo, hi): dn[d] += c
    return n, dn
def PRUNE(what, T=11, group=None):
    """'drop': share of DRs the list drops.  'stay': share of DRs it keeps.  'lose': share of the finishes in T it
    loses.  'keep': share of them it keeps.  'base' / 'kept': share finishing in T, of all of them / of what it keeps."""
    n, dn = _prune(group)
    if what == 'drop': return f'{100 * sum(dn) / sum(n):.0f}%'
    if what == 'stay': return f'{100 - 100 * sum(dn) / sum(n):.0f}%'
    if what == 'base': return pv.pct(n, T)
    if what == 'kept': return pv.pct([x - y for x, y in zip(n, dn)], T)
    lost = 100 * sum(dn[:T + 1]) / sum(n[:T + 1])
    return pv.num(lost) if what == 'lose' else f'{100 - lost:.0f}%'
def LOSS(cs, rule, T=11):
    """Share of the finishes in T of corner subset cs lost by a rule: 'list' (the prune list) or a predicate on the row."""
    n = dn = 0
    for xs, e, a, b, tp, lo, hi, d, c in pv._k5():
        if xs != cs or d > T: continue
        n += c
        if (_dropped(xs, e, a, b, tp, lo, hi) if rule == 'list' else rule(e, a, b, tp, lo, hi)): dn += c
    return f'{100 * dn / n:.0f}%'
def PRUNE_HIGHQT():
    """Share of the DRs the list drops that are 4qt or 5qt."""
    tot = sum(_prune()[1]); return f"{100 * (sum(_prune('4qt')[1]) + sum(_prune('5qt')[1])) / tot:.0f}%"
def _attempts():
    """Rows of out/hand/attempt_run.csv (many_examples.py --rerun): per random scramble, every EO-first DR up to 12
    moves by length class, with the best solution through them (optimal finishes) with and without the prune list."""
    import csv
    with open(pv.H + 'attempt_run.csv') as f:
        rd = csv.reader(l for l in f if not l.startswith('#')); head = next(rd)
        return [dict(zip(head, map(int, r))) for r in rd]
def ATT(what):
    """The prune list on the 11-movers of real scrambles.  'n': scrambles in the run; 'have': those with a DR of 10
    moves or less; 'drs_all' / 'drs_kept': DRs to finish per scramble (10 or less, plus every 11-mover / plus the
    kept ones); 'res_all' / 'res_kept': average best solution."""
    run = _attempts(); have = [x for x in run if x['n9'] + x['n10'] > 0]; a = lambda xs: sum(xs) / len(have)
    if what == 'n': return str(len(run))
    if what == 'have': return str(len(have))
    if what == 'drs_all': return f"{a(x['n9'] + x['n10'] + x['n11'] for x in have):,.0f}"
    if what == 'drs_kept': return f"{a(x['n9'] + x['n10'] + x['kept11'] for x in have):,.0f}"
    if what == 'res_all': return f"{a(min(x['best9'], x['best10'], x['best11']) for x in have):.2f}"
    if what == 'res_kept': return f"{a(min(x['best9'], x['best10'], x['best_kept11']) for x in have):.2f}"
    raise KeyError(what)
def QTSHARE(*groups):
    """Share of all DR states in these qt groups."""
    return pv.num(100 * sum(sum(_prune(g)[0]) for g in groups) / sum(_prune()[0]))
def PPR(cs, T):
    """What one more pair multiplies the odds of a finish in T by (geometric mean of the steps from 0 to 4 pairs)."""
    return f"{(share(q(cs=cs, pairs=4), T) / share(q(cs=cs, pairs=0), T)) ** 0.25:.1f}"
def P05(cs, T):
    """Odds of a finish in T with five or more pairs, as a multiple of the odds with none."""
    return f"{share(q(cs=cs, pairs=5), T) / share(q(cs=cs, pairs=0), T):.0f}"
def PRUNE_TABLE():
    L = ['| DRs | Dropped | 10s lost | 11s lost | 12s lost | All of them: in 10 / 11 / 12 | What you keep: in 10 / 11 / 12 |', '|---|---:|---:|---:|---:|---|---|']
    for g in pv.GROUPS + [None]:
        n, dn = _prune(g); kept = [x - y for x, y in zip(n, dn)]
        L.append(f"| {pv.GROUP_NAME[g] if g else '**all DR states**'} | {100 * sum(dn) / sum(n):.0f}% | " + ' | '.join(pv.num(100 * sum(dn[:T + 1]) / sum(n[:T + 1])) for T in (10, 11, 12)) + f' | {tri(n)} | {tri(kept) if sum(kept) else "nothing is kept"} |')
    return '\n'.join(L)
ENV = {k: v for k, v in globals().items() if not k.startswith('_')}
# ---- real DRs and DR-breaking finishes: the gaps study's outputs (/data/fmc/gaps/research/out); computed, not in Lean
import csv as _csv, json as _json, collections as _col
_GP = '/data/fmc/gaps/research/'
def _gt(name): return list(_csv.DictReader(open(_GP + 'out/' + name), delimiter='\t'))
_CORN = ['0c0', '2c5', '2c4', '0c3', '4a2', '4a1', '2c3', '0c4', '4c3', '4c4', '4b2', '4b5']
def _gaps():
    G = {}
    ov = _json.load(open(_GP + 'out/a_overview.json')); G['scr'] = ov['scrambles']; G['dr11'] = ov['drs_le11']
    a = {(r['group'], r['pop']): r for r in _gt('a_subsets.tsv')}; P = ('dr11', 'scr11')
    G['share'] = max(abs(float(a[(c, p)]['share']) - float(a[(c, p)]['uniform_share'])) * 100 for c in _CORN for p in P)
    G['mean'] = max(abs(float(a[(c, p)]['mean_opt']) - float(a[(c, p)]['uniform_mean'])) for c in _CORN for p in P)
    G['le11'] = max(abs(float(a[(c, p)]['le11']) - float(a[(c, p)]['uniform_le11'])) * 100 for c in _CORN for p in P)
    G['le11_at'] = max(((abs(float(a[(c, p)]['le11']) - float(a[(c, p)]['uniform_le11'])) * 100, c) for c in _CORN for p in P))[1]
    G['le11_ex'] = max(abs(float(a[(c, p)]['le11']) - float(a[(c, p)]['uniform_le11'])) * 100 for c in _CORN if c != G['le11_at'] for p in P)
    mix = {}
    for c in _CORN:
        for k in '02468':
            s = f'{c} {k}e'
            if (s, 'scr11') in a:
                mix[s] = (float(a[(s, 'scr11')]['share']) / float(a[(c, 'scr11')]['share'])) / (float(a[(s, 'scr11')]['uniform_share']) / float(a[(c, 'scr11')]['uniform_share']))
    G['e0'] = (1 - min(v for s, v in mix.items() if s.endswith(' 0e'))) * 100; G['e6'] = (max(v for s, v in mix.items() if s.endswith(' 6e')) - 1) * 100
    q = {(r['group'], r['pop'], r['metric']): r for r in _gt('b_q3.tsv')}
    G['q3all'] = max(abs(float(q[('all', p, m)]['value']) - float(q[('all', 'uniform', m)]['value'])) * 100 for p in P
                     for m in ('niss_eq_linear', 'niss_shorter_by_1', 'niss_shorter_by_2plus', 'opt_uses_shortest_niss', 'no_opt_through_shortest_niss', 'every_opt_htr_ge9', 'xr2_one_shorter'))
    g2 = {(r['group'], r['pop']): r for r in _gt('g2.tsv')}
    G['g2'] = {p: {k: float(g2[('all', p)][k]) for k in ('shorter', 'se', 'mean_gain')} for p in ('uniform',) + P if ('all', p) in g2}
    G['g2n'] = int(g2[('all', 'uniform')]['n'])
    cells = sorted([r for r in _gt('g2.tsv') if r['pop'] == 'uniform' and ' ' in r['group']], key=lambda r: -float(r['shorter']))
    G['worst'] = [(r['group'], float(r['shorter']) * 100) for r in cells[:3]]
    rows = [l.rstrip('\n').split('\t') for l in open(_GP + 'big/g2/uni1000.out')]; SZ = _SIZE()
    n = _col.Counter(r[0] for r in rows); W = _col.Counter(); S = _col.Counter(); Gn = _col.Counter()
    for r in rows:
        w = SZ[r[0]] / n[r[0]]
        d = int(r[5]); W[d] += w; Gn[d - int(r[9])] += w
        if int(r[9]) < d: S[d] += w
    G['le12'] = sum(S[d] for d in W if d <= 12) / sum(W[d] for d in W if d <= 12) * 100
    G['at'] = {d: S[d] / W[d] * 100 for d in W}
    G['by1'] = Gn[1] / sum(v for k, v in Gn.items() if k > 0) * 100
    ex = _json.load(open(_GP + 'out/g2_examples.json'))
    G['ex'] = max(ex['examples'], key=lambda e: e['dr_optimum'] - e['true_optimum'])
    G['ex_sol'] = [s['moves'] for s in G['ex']['solutions'] if s['moves'].startswith('R L')][0]
    return G
def _SIZE():
    """exact subset x edges sizes (htr-routes' dist48 table)"""
    out = {}
    for l in open('/data/fmc/htr-routes/research/out/checks/dist48.tsv').read().split('\n')[1:]:
        if l:
            f = l.split('\t'); out[f[0]] = out.get(f[0], 0) + int(f[2])
    return out
import functools as _ft
GAPS = _ft.lru_cache(None)(_gaps)
ENV = {k: v for k, v in globals().items() if not k.startswith('_')}
