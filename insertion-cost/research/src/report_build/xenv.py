#!/usr/bin/env python3
"""Names available inside {= ... =} in the write-up and errata sources.  Every number in the text comes through here.

Most of them read a cell of a generated table (CELL), so that the prose and the tables cannot disagree; the rest read
the same result files the tables are made from."""
import sys, json, csv, os, re, math, collections, functools
sys.path.insert(0, '/data/fmc/insertion-cost/research/src')
import iv
from iv import O, fmt, num, f2, f1, f0, f2s, SHOW
D = '/data/fmc/insertion-cost/report/data/'
def _j(name):
    p = O + name
    return json.load(open(p)) if os.path.exists(p) else {}
REAL = _j('real.json'); FACTS = _j('facts.json'); TYPESJ = _j('types.json'); GREEDY = _j('greedy.json'); WIT = _j('witness.json'); CORP = _j('real_corpus.json')
# ---- cells of the generated tables
@functools.lru_cache(None)
def _table(name):
    lines = [l for l in open(D + name + '.md').read().split('\n') if l.startswith('|')]
    cells = lambda l: [c.strip() for c in l.strip().strip('|').split('|')]
    head = cells(lines[0]); rows = [cells(l) for l in lines[2:]]
    assert len(set(head)) == len(head), (name, 'two columns with one name')
    return head, rows
def CELL(name, row, col):
    """The cell of table `name` in the row whose first column is `row` (or whose first columns are the tuple `row`)."""
    head, rows = _table(name); key = (row,) if isinstance(row, str) else tuple(row)
    hit = [r for r in rows if tuple(x.replace('**', '') for x in r[:len(key)]) == key]
    assert len(hit) == 1, (name, row, len(hit))
    return hit[0][head.index(col)]
D6 = O + 'data6/'
@functools.lru_cache(None)
def _table6(name):
    lines = [l for l in open(D6 + name + '.md').read().split('\n') if l.startswith('|')]
    cells = lambda l: [c.strip() for c in l.strip().strip('|').split('|')]
    return cells(lines[0]), [cells(l) for l in lines[2:]]
def X(name, row, col):
    """The number in a cell before rounding (six decimals, from the twin tables of tables6.py), for arithmetic: a
    difference of two cells is then rounded once, not three times.  The twin must round to the printed cell."""
    head, rows = _table6(name); key = (row,) if isinstance(row, str) else tuple(row)
    hit = [r for r in rows if tuple(x.replace('**', '') for x in r[:len(key)]) == key]
    assert len(hit) == 1, (name, row, len(hit))
    v = float(hit[0][head.index(col)].rstrip('%').split(' ')[0]); shown = CELL(name, row, col).split(' ')[0]
    if re.fullmatch(r'-?\d+\.\d\d', shown): assert f2(v) == shown, ('the six-decimal tables are stale: run tables6.py', name, row, col, v, shown)
    return v
def COL(name, col):
    head, rows = _table(name); return [r[head.index(col)] for r in rows]
def _pc(txt): return float(txt.rstrip('%').replace('<', ''))
# ---- types and algs
def WITHIN2(kind): return f"{TYPESJ[kind]['states_within_two']:,}"
def THREE(what):
    """The corner leftovers that need exactly three 3-cycles: 'types' (the two twist directions counted apart, as the
    Lean statement does), 'names' (rows of the table) or 'states'."""
    head, rows = _table('types_three'); last = [c.replace('**', '') for c in rows[-1]]
    return {'types': last[3], 'names': str(len(rows) - 1), 'states': last[2]}[what]
def TWO(kind, what):
    """The leftovers two 3-cycles make ('corner' or 'edge'): 'names' (rows of the table, without the 3-cycle itself) or
    'types' (twist directions apart)."""
    head, rows = _table('types'); names = [SHOW[t] for t in (iv.CORNER if kind == 'corner' else iv.EDGE)][1:]
    r = [x for x in rows if x[0] in names]; assert len(r) == len(names)
    return str(len(r)) if what == 'names' else str(sum(int(x[4]) for x in r))
def THREE_ROW(name): return CELL('types_three', name, 'States')
@functools.lru_cache(None)
def _algs():
    import xtables
    return xtables.alg_summary()
def STATES(typ): return f'{_algs()[0][typ][0]:,}'
def ALGN(typ, k): return f"{_algs()[0][typ][2].get(str(k), 0):,}"
def ALGS(typ, k): return f'{_algs()[1][typ].get(k, 0):,}'
def F8(k): return f"{FACTS['eight_movers_per_3c'][str(k)]:,}"
def F8PCT(): return num(100 * FACTS['eight_movers_per_3c']['2'] / (FACTS['eight_movers_per_3c']['1'] + FACTS['eight_movers_per_3c']['2']))
def FACT(key): return FACTS[key]
def FACTN(key): return f'{FACTS[key]:,}'
def _le(typ, k):
    d = _algs()[0][typ][2]; return sum(v for x, v in d.items() if x != '>12' and int(x) <= k)
def EDGE8(): return num(100 * _le('3e', 8) / _algs()[0]['3e'][0])
def CORNER8(): return num(100 * _le('3c', 8) / _algs()[0]['3c'][0])
# ---- costs
def _c(typ, n, L, model, src): return iv.cell(typ, n, L, model or iv.head(typ), src)
def M(typ, n=20, L=8, model=None, src='sample'): return f2(iv.mean(_c(typ, n, L, model, src)))
def NSK(typ, n=20, L=8, model=None, src='sample'): return f"{_c(typ, n, L, model, src)['n']:,}"
def P(typ, k, n=20, L=8, model=None, src='sample'): return iv.pct(_c(typ, n, L, model, src), k)
def WORSE(typ, k, n=20, L=8):
    c = _c(typ, n, L, None, 'sample'); return fmt(c['n'] - iv.count_le(c, k - 1), c['n'])
def DIFF(a, b, n=20, L=8): return f2(iv.mean(_c(a, n, L, None, 'sample')) - iv.mean(_c(b, n, L, None, 'sample')))
def DIFFL(typ, L1, L2, n=20): return f2(iv.mean(_c(typ, n, L1, None, 'sample')) - iv.mean(_c(typ, n, L2, None, 'sample')))
_PK = {'8': 'Cap 8: mean added where something fits', '10': 'Cap 10: mean added', '10m': 'Cap 10, a comm plus an alg: mean added', '12': 'Cap 12: mean added'}
def PAIR(typ, key): return CELL('caps_paired', SHOW[typ], _PK[key])
def PAIRD(typ, a, b): return f2(X('caps_paired', SHOW[typ], _PK[a]) - X('caps_paired', SHOW[typ], _PK[b]))
def PAIRN(typ): return CELL('caps_paired', SHOW[typ], 'Skeletons')
def NEST(typ): return f2(X('nesting', SHOW[typ], 'No nesting: mean added') - X('nesting', SHOW[typ], 'Nesting allowed: mean added'))
def APART(typ): return f2(X('nesting', SHOW[typ], 'The two not touching: mean added') - X('nesting', SHOW[typ], 'Nesting allowed: mean added'))
def CH(typ, n, T, L=8): return num(100 * iv.exact(iv.chance(typ, n, L, T)))
def EXACT(typ, n, k, L=8):
    c = _c(typ, n, L, None, 'sample'); return fmt(c['h'].get(str(k), 0), c['n'])
def TOTAL(typ, n, L=8):
    import xtables
    return f1(n + xtables.mean_at(typ, n, L))
def TOTALX(typ, n, L=8):
    """The expected total before rounding, for differences."""
    import xtables
    return n + xtables.mean_at(typ, n, L)
def CPX(typ, cap, what): return CORP[typ][str(cap)][what]
def EXR(typ, L=8):
    v = [float(x) for x in COL(f'exchange_cap{L}', f'{SHOW[typ]} shorter by') if x]
    return f'{f1(min(v))} to {f1(max(v))}'
def EXM(typ, n): return CELL('exchange_mean', str(n), f'{SHOW[typ]} shorter by')
def NESTED10(typ, n=20):
    """Share of skeletons whose best at cap 10 is a pair of comms that has to be nested (no pair kept apart and no single
    alg is as short)."""
    c = iv.cell(typ, n, 10, 'best'); return fmt(c['nested'], c['n'])
def _twist():
    rows = [l.split('\t') for l in open(O + 'twistmin_L12.txt').read().strip().split('\n')[1:]]
    return {int(r[0]): (int(r[1]), int(r[2]), int(r[3]), r[4] if len(r) > 4 else '') for r in rows}
def TW(key):
    """torchlight's statement: corner-only sequences (all edges kept) that leave a corner twisted in its place.
    'min': the shortest length at which there is one; 'seq', 'states': how many sequences and distinct states at that
    length; 'checked': the longest length looked at; '2tc', '3c1t', 'other': the states at that length by what they do."""
    t = _twist(); L = min(k for k, v in t.items() if v[1]); assert all(t[k][1] == 0 for k in t if k < L) and min(t) == 2
    if key == 'min': return str(L)
    if key == 'checked': return str(max(t))
    if key == 'seq': return f'{t[L][1]:,}'
    if key == 'states': return f'{t[L][2]:,}'
    by = dict((a.strip(), int(b)) for a, b in (x.split(':') for x in t[L][3].split(',')))
    return f'{by[key]:,}'
def _cap12(run):
    ts = [t for t in iv.TYPES if t not in ('3c', '3e') and bool(iv.cell(t, 20, 12, 'best', 'two12')) == run]
    names = [SHOW[t] for t in ts]; return ', '.join(names[:-1]) + ' and ' + names[-1]
def CAP12RUN(): return _cap12(True)
def CAP12NOT(): return _cap12(False)
def PERTEN(typ='3c', L=8): return f2((iv.mean(_c(typ, 10, L, None, 'sample')) - iv.mean(_c(typ, 30, L, None, 'sample'))) / 2)
# ---- one comm
def GE(n, k):
    """Share of 3c skeletons of length n whose best 8-mover insertion cancels k moves or more."""
    c = _c('3c', int(n), 8, 'one', 'sample'); return fmt(iv.count_le(c, 8 - k), c['n'])
def ONEIN(n, col): return f0(100 / _pc(CELL('one_longer', n, col)))
_NEAR = 'Of those, next to two opposite-face moves'; _MISS = 'Best is 8-3 or better and every other move missed it: walks'
def SKIPN():
    tot = 0
    for x in COL('one_skip_good', _MISS): tot += int(x)
    return f'{tot:,}'
def SKIPNEAR(n=None):
    """Misses of a best of 8-3 or better that sit next to two opposite-face moves: at one length, or over all lengths."""
    if n is not None: return f"{CELL('one_skip_good', str(n), _NEAR)} of {CELL('one_skip_good', str(n), _MISS)}"
    a = sum(int(x) for x in COL('one_skip_good', _NEAR)); b = sum(int(x) for x in COL('one_skip_good', _MISS))
    return 'every one' if a == b else f'{a:,} of {b:,}'
def SKIPALL(n=20): return CELL('one_skip', str(n), 'All misses of every other move: next to two opposite-face moves')
def SKIPWORST():
    """The best insertion that every other move ever missed, over all lengths of the table: '8-4'."""
    head, rows = _table('one_skip_good')
    ks = [int(re.search(r'the best was 8-(\d+)$', h).group(1)) for h in head if h.startswith('Of those, the best was') and any(int(r[head.index(h)]) for r in rows)]
    return f'8-{max(ks)}'
TENSKIP = _j('ten_skip.json')
def TS(n, key): return f"{TENSKIP[str(n)][key]:,}"
def TSP(n, a, b): return fmt(TENSKIP[str(n)][a], TENSKIP[str(n)][b])
def _gap2c2c(col): return X('nesting', 'pure 2c2c', col) - X('nesting', 'twisted 2c2c', col)
def GAP2C2C(col): return f2(_gap2c2c(col))
def GAP2C2CNEST(): return f2(_gap2c2c('Nesting allowed: mean added') - _gap2c2c('No nesting: mean added'))
# ---- greedy (the first comm of a two-comm leftover)
def G(typ, key, n=20, L=8): return GREEDY[f'{typ}_n{n}_L{L}'][key]
# ---- real skeletons
def RL(key, sub=None, sub2=None):
    v = REAL[key]
    if sub is not None: v = v[sub]
    if sub2 is not None: v = v[sub2]
    return f'{v:,}' if isinstance(v, int) else f2(v) if isinstance(v, float) else str(v)
def RC(group, cap, what):
    v = REAL['comp'][group][str(cap)][what]
    return f'{v:,}' if isinstance(v, int) else f2(v)
def RDIFF(group, cap):
    d = REAL['comp'][group][str(cap)]; return f2s(d['diff'])
def RSE(group, cap): return f2(REAL['comp'][group][str(cap)]['se'])
def AU(table, key, what):
    v = REAL[table][key][what]
    return f'{v:,}' if isinstance(v, int) else f2(v)
def AUP(table, key, what): return fmt(REAL[table][key][what], REAL[table][key]['k'])
def AUW(table, key):
    d = REAL[table][key]; return fmt(d['shorter'] + d['same'], d['k'])
def AUWN(table, key, noun=''):
    """'76 of 79 (96%)': posted solutions as short as the best at this cap, or shorter."""
    d = REAL[table][key]; return f"{d['shorter'] + d['same']} of {d['k']}{noun} ({fmt(d['shorter'] + d['same'], d['k'])})"
def DUPS(key): return str(REAL['author_dups'][key])
def RMIX(group, key): return f2(REAL['mixed'][group][key])
def DOUG(key): return str(REAL['doug'][key])
def DOUGT(i, who='thirds'):
    d = REAL['doug']; w = d[who]; return num(100 * w[i] / sum(w))
def EO(key, k):
    v = REAL['eo'][key][str(k)]; return f2(v) if isinstance(v, float) else f'{v:,}'
def EOSHARE(key, ks, of=None):
    """Share of the edge 3-cycles (or, key = 'real', of the real 3e skeletons) oriented on a number of axes in ks."""
    d = REAL['eo'][key]; return fmt(sum(d[str(k)] for k in ks), sum(d.values()))
def EON(key, ks): return str(sum(REAL['eo'][key][str(k)] for k in ks))
def SHORTROWS():
    x = REAL['shorter12']; hand = sum(1 for r in x if r['source'] == 'hand')
    return f"{len(x)} solutions, all by hand" if hand == len(x) else f"{len(x)} solutions, {hand} by hand and {len(x) - hand} from Insertion Finder"
def IFBETTER():
    """The pages where the search at cap 12 is shorter than Insertion Finder's result, as text."""
    head, rows = _table('if_pages'); out = []
    for r in rows:
        a, b = int(r[head.index('Insertion Finder, moves')]), int(r[head.index('Cap 12, moves')]); assert b <= a, r
        if b < a: out.append(f"{re.match(r'\[([^\]]+)\]', r[0]).group(1)}: {b} against {a}")
    words = ['no', 'one', 'two', 'three', 'four']
    return f"{words[len(out)]} page{'s' if len(out) != 1 else ''}" + (f" ({'; '.join(out)})" if out else '')
def GNONE(typ, g=0, n=20, L=8): return str(GREEDY[f'{typ}_n{n}_L{L}'][f'g{g}_none'])
def CP(typ, cap, what):
    v = CORP[typ][str(cap)][what]
    return f'{v:,}' if isinstance(v, int) else f2(v)
def CPN(typ, what): return f"{CORP[typ][what]:,}"
def REALN(group):
    bt = REAL['by_type']
    if group == '2c2c': return str(bt.get('2c2c-pure', 0) + bt.get('2c2c-twisted', 0))
    return str(sum(v for k, v in bt.items() if k not in ('3c', '5c', '3c1t', '2c2c-pure', '2c2c-twisted', '3e')))
def SUB(name, typ):
    d = REAL['subsets'][name][typ]; return f"{f2s(d['diff'])} ± {f2(d['se'])}"
def SUBN(name, typ): return str(REAL['subsets'][name][typ]['k'])
def AUL(table, key):
    d = REAL[table][key]; return fmt(d['plus1'] + d['plus2'] + d['plus3'], d['k'])
def AUL_N(table, key):
    d = REAL[table][key]; return str(d['plus1'] + d['plus2'] + d['plus3'])
def SHORTN(source): return str(sum(1 for x in REAL['shorter12'] if x['source'] == source))
def IFN(what):
    a, b = len(_table('if_pages')[1]), len(_table('if_pages_not')[1])
    return {'all': a + b, 'compared': a, 'not': b}[what]
def NOTESGE3(row):
    head, rows = _table('real_notes'); col = head.index(row[0].upper() + row[1:] + ': insertions')
    n = int(rows[0][col]); assert rows[0][0] == 'all of them'
    k = sum(int(r[col]) for r in rows if r[0] in ('8-3', '8-4', '8-5', '8-6 or more'))
    return fmt(k, n)
def NEGSHARE():
    c = iv.cell('3c', 20, 8, 'one'); return fmt(sum(v for k, v in c['h'].items() if int(k) < 0), c['n'])
def FC(typ): return CELL('first_choices', SHOW[typ], 'Ways to choose the first comm at one spot')
def SE2(typ, n=20, L=8, model=None, src='sample'): return f2(2 * iv.se(_c(typ, n, L, model, src)))
def SKIPTOTAL(): return f'{20000 * len(_table("one_skip")[1]):,}'
@functools.lru_cache(None)
def _rows(): return json.load(open(O + 'real_rows.json'))
def _posted(typ): return [r['L8'] for r in _rows() if r['type'] == typ and not r['dup_of'] and r['L8'] is not None]
def POSTED(typ): return str(len(_posted(typ)))
def POSTEDM(typ): v = _posted(typ); return f2(sum(v) / len(v))
def SPOT(which, i):
    sp = REAL['spots']
    return num(100 * sp['real'][i] / sp['k_real']) if which == 'real' else num(100 * iv.exact(sp[which][i]))
def RRLEN(eid, key):
    r = next(x for x in _rows() if x['id'] == eid); return str(r['n'] + r[key])
def REALTHIRDS():
    sp = REAL['spots']; k = sp['k_real']; d = REAL['doug']
    return (f", not on the {k} posted 3c skeletons (first third {num(100 * sp['real'][0] / k)}, middle {num(100 * sp['real'][1] / k)}, "
            f"last {num(100 * sp['real'][2] / k)}), and not on the {d['skeletons_3c']} of those that are DougCube's own ({DOUGT(0)}, {DOUGT(1)}, {DOUGT(2)}; 9.4). "
            f"Not refuted either: DougCube's stats count the insertions DougCube found, of every kind, which is a different count.")
def IFP(label, col):
    """The length in a cell of the Insertion Finder table, for the page whose label is given ('16 to 3C1T')."""
    head, rows = _table('if_pages'); r = next(x for x in rows if x[0].startswith(f'[{label}]'))
    return r[head.index(col + ', moves')]
def NCLASS(t): return str(len(_table(f'classes_{t}')[1]))
def ALGLEN(key): return str(FACTS['algs'][key]['moves'])
CHECKS = _j('checks.json')
def CHECK(key): return CHECKS[key]
def W(key, sub=None):
    v = WIT[key] if sub is None else WIT[key][sub]
    return str(v)
def _g(typ, n=20, L=8): return GREEDY[f'{typ}_n{n}_L{L}']
def GLOSS(typ, g, n=20, L=8):
    d = _g(typ, n, L); return fmt(d['n'] - d[f'g{g}_hit'], d['n'])
def GHIT(typ, g, n=20, L=8):
    d = _g(typ, n, L); return fmt(d[f'g{g}_hit'], d['n'])
def GM(typ, key, n=20, L=8): return f2(_g(typ, n, L)[key])
def GN(typ, n=20, L=8): return f"{_g(typ, n, L)['n']:,}"
def GONEIN(n, col): return f0(100 / _pc(CELL('greedy_first', n, col)))
def G10(key):
    d = GREEDY['5c_cap10_vs_8']
    if key in ('n', 'run'): return f"{d[key]:,}"
    if key == 'worse': return fmt(d['g0_10_worse'], d['n'])
    if key == 'better': return fmt(d['g0_10_better'], d['n'])
    return f2(d[key])
def SUBD(name, typ): return f2s(REAL['subsets'][name][typ]['diff'])
def D16RANGE():
    v = [iv.mean(_c(t, 16, 8, None, 'sample')) - iv.mean(_c(t, 20, 8, None, 'sample')) for t in ('2tc', '2c2c-twisted', '2c2c-pure', '3tc', '3c1t', '5c')]
    return f'{f2(min(v))} to {f2(max(v))}'
def DRN():
    """Skeletons per kind of 17-move sequence in the trig0n runs (the same for every kind and cap)."""
    J = _j('dr17.json'); n = {sum(h.values()) for kind in J.values() for h in kind.values()}
    assert len(n) == 1, n
    return f'{n.pop():,}'
def DRGAP(): return f2(X('dr17', ('EO in 4, DR in 10, then DR moves; a 3c that DR moves can leave', '8'), 'Mean moves added') - X('dr17', ('random moves', '8'), 'Mean moves added'))
def GV(key):
    """Verdict cells of the claims table that depend on the greedy runs."""
    if key == 'first83':
        return (f"**Yes for an 8-3**: there on {CELL('greedy_first', '20', '5c: 8-3 or better')} of 20-move 5c skeletons and {CELL('greedy_first', '16', '5c: 8-3 or better')} of 16-move ones. "
                f"An 8-4 or better: {CELL('greedy_first', '20', '5c: 8-4 or better')} and {CELL('greedy_first', '16', '5c: 8-4 or better')} (8.4).")
    if key == 'subopt':
        return (f"**True**: on a 20-move 5c, the best first comm followed by the best second misses the best pair on {GLOSS('5c', 0)} of skeletons (8.4) [f].")
    if key == 'greedy':
        return (f"**What the settings give**, with pure comms on a 20-move 5c: {CELL('greedy', '5c', 'Best first comm only: mean added')} at greedy 0 (longer than the best pair on {GLOSS('5c', 0)} of skeletons), "
                f"{CELL('greedy', '5c', 'First comms within 1 move: mean added')} at greedy 1 ({GLOSS('5c', 1)}), {CELL('greedy', '5c', 'Best pair of comms: mean added')} for the best pair. What is findable is not measured.")
    if key == 'morealgs':
        return (f"**It can happen, and it is uncommon**: on {G10('n')} random 20-move 5c skeletons, greedy 0 with every 3c alg of up to 10 moves is longer than greedy 0 with 8-movers on {G10('worse')} and shorter on {G10('better')} [l]. tave_789's line is the reason: in each of those the longer list has a better first comm, and it is the wrong one to follow.")
    if key == 'bugs':
        return (f"on a 20-move 5c the best first comm followed by the best second misses the best pair of 8-movers on {GLOSS('5c', 0)} of skeletons; also following the first comms that are one move worse, on {GLOSS('5c', 1)}. "
                f"On average {CELL('greedy', '5c', 'Best first comm only: mean added')}, {CELL('greedy', '5c', 'First comms within 1 move: mean added')} and {CELL('greedy', '5c', 'Best pair of comms: mean added')}. One where the best first comm is the wrong one:")
    raise KeyError(key)
# ---- the separate check of the every-other-move rule (research/verify/every_other.py -> out/verify/every_other.json)
EVO = _j('verify/every_other.json')
def EV(run, key):
    """A count of the separate check; run is '3c_fixed', '3c_free' or '5c_fixed' (see every_other.py for the keys)."""
    return f"{EVO['runs'][run][key]:,}"
def EVP(run, a='good_found', b='good_walks'):
    """A share of the separate check; by default the walks that find a best of 8-3 or better."""
    r = EVO['runs'][run]; return fmt(r[a], r[b])
def EVALL(run, key):
    """How many of the misses of a run have a property: 'every one' or 'k of n'."""
    r = EVO['runs'][run]; return 'every one' if r[key] == r['good_missed'] else f"{r[key]:,} of {r['good_missed']:,}"
def PAIR1IN(which):
    """Opposite-face pairs among neighbouring pairs of moves, the N of '1 in N': the study's 20-move 3c sample
    ('study_sample_3c_n20'), the posted skeletons ('posted') or the skeletons of a run of the separate check."""
    if which == 'study_sample_3c_n20' and which not in EVO['pairs']: which = '3c_fixed'      # the sample file was not there: the check's own skeletons, made by the same rule
    d = EVO['pairs'].get(which) or EVO['runs'][which]; return f0(d['joins'] / d['pairs'])
def PAIRN1(which, key): return f"{EVO['pairs'][which][key]:,}"
def EVTEXT():
    """What the table of the separate check shows, in words; each statement is checked against the counts first."""
    R = EVO['runs']; a, b, c = R['3c_fixed'], R['3c_free'], R['5c_fixed']
    miss = lambda r: r['good_missed'] / r['good_walks']
    assert abs(100 * a['good_found'] / a['good_walks'] - _pc(CELL('one_skip_good', '20', 'Best is 8-3 or better: every other move finds it'))) < 0.5
    assert 1.7 < b['pairs'] / a['pairs'] < 2 and 1.8 < miss(b) / miss(a) < 2.3 and 0.4 < miss(c) / miss(a) < 0.6
    assert all(r['missed_next_to_pair'] == r['good_missed'] == r['missed_found_once_a_pair_is_swapped'] for r in R.values())
    return ("The first row is the measurement above again and gives the same share. With a pair written either way round there are nearly twice as many pairs, "
            "and the share of walks that miss about doubles. The first comm of a 5c, the search notkevin was talking about, is missed about half as often as the comm of a 3c. "
            "In all three, every miss is next to an opposite-face pair, and the same walk finds it once one such pair of the skeleton is written the other way round.")
@functools.lru_cache(None)
def _skipsetup():
    """Example [c] one spot earlier: the same comm with the move between as a setup.  Replayed on the sticker model, and
    it has to cancel to the printed solution."""
    import cube
    w = WIT['skip']; scr = cube.parse(w['scramble']); sk = cube.parse(w['skeleton']); j = w['spot']
    txt = open(os.path.dirname(os.path.abspath(__file__)) + '/wit_skip.md').read()
    alg = cube.parse(re.search(r'(?m)^\* = (.+?) //', txt).group(1)); sol = cube.parse(re.search(r'(?m)^Solution: (.+?) \(\d+\)$', txt).group(1))
    m = sk[j - 1]; setup = [m] + alg + cube.inv_seq([m]); full = sk[:j - 1] + setup + sk[j - 1:]
    assert cube.do(cube.SOLVED, scr + full) == cube.SOLVED and cube.cancel(full) == sol, 'the setup version of example [c] does not replay'
    return {'spot': str(j - 1), 'alg': ' '.join(setup), 'note': f'{len(setup)}-{len(full) - len(sol)}', 'total': str(len(sol)), 'move': m}
def SKS(key):
    """Example [c] with one setup move: 'spot', 'alg', 'note' (alg length and moves cancelled), 'total', 'move'."""
    return _skipsetup()[key]
def GDIFF(a, b, col='Best first comm only: mean added'):
    """Difference of two rows of the greedy table (rows by their printed names), rounded once."""
    return f2(X('greedy', a, col) - X('greedy', b, col))
ENV = {k: v for k, v in globals().items() if not k.startswith('_')}
