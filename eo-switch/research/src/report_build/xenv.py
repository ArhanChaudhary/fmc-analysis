#!/usr/bin/env python3
"""Names available inside {= ... =} in the write-up and errata sources.  Every number in the text comes through here:
from a cell of a generated table (report/data), or from the result files the tables are made from (research/out,
report_extra.json written by xtables.py)."""
import json, csv, os, math, functools
O = '/data/fmc/eo-switch/research/out/'
D = '/data/fmc/eo-switch/report/data/'
def _j(name): return json.load(open(O + name))
E = _j('report_extra.json')
W = _j('witness.json')

def pc(x, d=None):
    """A share as a percentage: one decimal, two below 1%, three below 0.1%."""
    x = float(x) * 100
    if x == 0: return '0%'
    if 99.95 <= x and d is None: return '>99.9%'
    if d is None: d = 1 if x >= 1 else 2 if x >= 0.1 else 3
    return f'{x:.{d}f}%'
def p0(x): return f'{float(x) * 100:.0f}%'
def f1(x): return f'{float(x):.1f}'
def f2(x): return f'{float(x):.2f}'
def f3(x): return f'{float(x):.3f}'
def n(x): return f'{int(float(x)):,}'
def oneIn(x): return f'1 in {1 / float(x):.1f}'

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
