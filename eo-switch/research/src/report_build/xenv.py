#!/usr/bin/env python3
"""Names available inside {= ... =} in the write-up and errata sources.  Every number in the text comes through here:
from a cell of a generated table (report/data), or from the result files the tables are made from (research/out,
report_extra.json written by xtables.py)."""
import json, csv, os, math, functools, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from halfup import hu
O = '/data/fmc/eo-switch/research/out/'
D = '/data/fmc/eo-switch/report/data/'
def _j(name): return json.load(open(O + name))
E = _j('report_extra.json')
class _Rd(float):
    """A number as a result file keeps it (grades.tsv, populations.tsv, variants_by_drm.tsv, q4.tsv: 4 or 5 decimals of
    a number that has more).  A 5 in its last place is no half, so pc, p0, f1, f2 and f3 format it from the float as
    they always did; text read from a result file is treated the same.  Everything else goes through halfup.hu."""
def _mark(o): return _Rd(o) if isinstance(o, float) else {k: _mark(v) for k, v in o.items()} if isinstance(o, dict) else [_mark(v) for v in o] if isinstance(o, list) else o
for _k in ('grade', 'pop', 'var', 'bars', 'low_best', 'uniform_worst_z'): E[_k] = _mark(E[_k])
def _old(x): return isinstance(x, (str, _Rd))
W = _j('witness.json')

def pc(x, d=None):
    """A share as a percentage: one decimal, two below 1%, three below 0.1%."""
    share, x = x, float(x) * 100
    if x == 0: return '0%'
    if 99.95 <= x and d is None: return '>99.9%'
    if d is None: d = 1 if x >= 1 else 2 if x >= 0.1 else 3
    return f'{x:.{d}f}%' if _old(share) else f'{hu(share, d, 100):.{d}f}%'
def pcx(x, d=None):
    """pc, but an exact 100% prints as 100% (pc prints >99.9% for anything from 99.95% up)"""
    return '100%' if float(x) == 1.0 else pc(x, d)
def p0(x): return f'{float(x) * 100:.0f}%' if _old(x) else f'{hu(x, 0, 100):.0f}%'
def f1(x): return f'{float(x):.1f}' if _old(x) else f'{hu(x, 1):.1f}'
def f2(x): return f'{float(x):.2f}' if _old(x) else f'{hu(x, 2):.2f}'
def f3(x): return f'{float(x):.3f}' if _old(x) else f'{hu(x, 3):.3f}'
def n(x): return f'{int(float(x)):,}'
def oneIn(x): return f'1 in {1 / float(x):.1f}' if _old(x) else f'1 in {hu(round(1 / x, 9), 1):.1f}'

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

def RULE(drm, *path):
    """E['rule'][drm]: 'all' / 'groups'[g] / 'decided' / 'kept' / 'lost'; stats keys n share p6 p5 p7 q5 a5 q6 a6 hits"""
    v = E['rule'][drm]
    for p in path: v = v[p]
    return v
def RG(drm, g, k='p6'): return RULE(drm, 'groups', g, k)
def RCELL(drm, i, k='p6'): return RULE(drm, 'cells', i, 2, k)
def STRICT(drm, k): return E['strict'][drm][k]
def GR(i, k): return E['grade'][i][k]
def POP(drm, i): return E['pop'][drm][i]
def OPT(drm, i): return E['opt'][drm][i]
def VAR(drm, col): return E['var'][drm][col]
def CL(i, field='numbers'): return E['claims'][i][field]
def EV(i, before, after=None):
    """a piece of a claims.tsv numbers string: the text after `before` up to `after` (default: the next space)"""
    s = E['claims'][i]['numbers'].split(before, 1)[1]
    return s.split(after if after else ' ', 1)[0].rstrip('.,;')
def WC(i, k): return W['claims'][i][k]
def WA(cell, j, k):
    a = [x for x in W['attempts'] if x['cell'] == cell][j]
    return a[k]
def NISS(check):
    hit = [(k, v) for k, v in E['checks_niss'].items() if k.startswith(check)]
    if len(hit) > 1: hit = [(k, v) for k, v in hit if k.endswith('(uniform)')]
    assert len(hit) == 1, check; return hit[0][1]
def TRACE(check, sample):
    hit = [v for k, v in E['checks_trace'].items() if k.startswith(check) and k.endswith('|' + sample)]
    assert len(hit) == 1, (check, sample); return hit[0]
def Q4(what): return E['q4'][what]
def Q4P(what, i, sep=', '):
    """the i-th comma-separated piece of a q4 answer"""
    return E['q4'][what].split(sep)[i]
def BARS(arm, i): return E['bars'][arm][i]
def INV(seq):
    out = []
    for m in reversed(seq.split()):
        out.append(m[0] if m.endswith("'") else m if m.endswith('2') else m + "'")
    return ' '.join(out)
ENV = {k: v for k, v in globals().items() if not k.startswith('_')}
@functools.lru_cache(None)
def _rep(): return list(csv.DictReader(open(O + 'reproduce.tsv'), delimiter='\t'))
def REP(quantity, col='published', source=''):
    hit = [r for r in _rep() if r['quantity'] == quantity and source in r['source']]
    assert len(hit) == 1, (quantity, len(hit)); return hit[0][col]
ENV = {k: v for k, v in globals().items() if not k.startswith('_')}

# ---- the two-ring sections (xrings.py): out/rings.json and out/ring_examples.json
RJ = _j('rings.json'); XJ = _j('ring_examples.json')
def RH(h, k='p6'):
    """4c4e by half turns to two bars: RH(2) the sub-7 rate; keys n share p5 p6 p7 of_hits q4 q5 q6 a4 a5 a6"""
    return RJ['h'][str(h)][k]
def RHG(g, k='p6'): return RJ['hg'][g][k]                    # groups le1 le2 eq2 eq3 ge3 ge4
def RSS(a, t, k='p6'): return RJ['ss'][f'{a}{t}'][k]          # row swaps x slot type
def RCARD(g, k='p6'): return RJ['card'][g][k]
def RCS(g, h, k='p6'): return RJ['card_split'][f'{g}|{h}'][k]
def RPH(p, h, k='p6'): return RJ['ph'][f'{p}|{h}'][k]
def RU(name, k='p6'): return RJ[name][k]
def RIN3(txt, k='p6'): return RJ['in3'][txt][k]
def RPROF(drm, q, h, k='p6'): return RJ['prof'][drm][f'{q}{h}'][k]
def RSIG(drm, s, k='p6'): return RJ['sig'][drm][str(s)][k]
def RSHORT(drm, which='short', k='p6'): return RJ['short'][drm][which][k]
def RCROSS(drm, txt, lab, k='p6'): return RJ['cross'][f'{drm}|{txt}|{lab}'][k]
def RTHREE(key, k='p6'): return RJ['three'][key][k]
def RX(name, k): return XJ[name][k]
def RXB(name, comment=''):
    """an example as two code lines: the scramble and its optimal DR"""
    e = XJ[name]
    return f"{e['scramble']}   // scramble" + (f", {comment}" if comment else '') + f"\n{e['dr']}   // optimal DR, {e['d']} moves"
def RXF(name, comment='', note=''):
    """an example as three code lines: scramble, optimal DR, and its rings and holes"""
    e = XJ[name]
    return RXB(name, comment) + f"\n// U ring {e['Un']}, D ring {e['Dn']}, holes {' '.join(e['holes'])}" + (f": {note}" if note else '')
def RINGS(name):
    e = XJ[name]
    return f"`{e['Un']}` and `{e['Dn']}`"
def TRR(check, sample):
    import csv as _c
    hit = [r for r in _c.DictReader(open(O + 'checks_trace_rings.tsv'), delimiter='\t') if r['check'].startswith(check) and r['sample'] == sample]
    assert len(hit) == 1, (check, sample); return [int(hit[0]['cubes']), int(hit[0]['holds'])]
ENV = {k: v for k, v in globals().items() if not k.startswith('_')}
