#!/usr/bin/env python3
"""Names available inside {= ... =} in the write-up and errata sources.  Every number in the text comes through here:
from a cell of a generated table (report/data), or from the result files the tables are made from (research/out)."""
import json, csv, os, re, math, functools
O = '/data/fmc/htr-routes/research/out/'
D = '/data/fmc/htr-routes/report/data/'
csv.field_size_limit(10**8)
def _j(name): return json.load(open(O + name))
E = _j('report_extra.json')
W = {w['id']: w for w in _j('witness.json')}
WX = _j('witness_extra.json')

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
def n(x): return f'{int(x):,}'

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

@functools.lru_cache(None)
def _tsv(name): return list(csv.DictReader(open(O + name), delimiter='\t'))
def BUD(g, b, step, col='cumulative', tg='opt'):
    """q2_checklist_budget: group, budget ('0','1','2','inf'), step -> column (cumulative / class / marginal / alone)"""
    r = [r for r in _tsv('q2_checklist_budget.tsv') if r['group'] == g and r['level'] == 'C' and r['target'] == tg and r['budget'] == b and r['step'] == str(step)]
    assert len(r) == 1, (g, b, step)
    v = r[0][col]
    return pc(v) if col in ('cumulative', 'marginal', 'alone') else '`' + v.replace(' | ht', '') + '`'
def SAME(g, b, step, col='cum_p1'):
    r = [r for r in _tsv('q2_same_classes_p1.tsv') if r['group'] == g and r['budget'] == b and r['step'] == str(step)]
    return pc(r[0][col])
def Q3(g, col): return E['q3'][g][col]
def Q4(g, col): return E['q4'][g][col]
def Q5(g, col): return E['q5'][g][col]
def Q8(g, q, R, col): return E['q8'][f'{g}|{q}|{R}'][col]
def Q9(tg, col): return E['q9'][tg][col]
def C11(g, col): return E['c11'][g][col]
def BYLEN(L, col):
    r = [r for r in _tsv('q3_htr_by_length.tsv') if r['group'] == 'all' and r['L'] == str(L)][0]
    return pc(r[col])
def GR(name, step, col):
    r = [r for r in E['q6'] if r['checklist'] == name and r['step'] == str(step)][0]
    return pc(r[col])
def NM(doc, label): return E['names'][f'{doc}|{label}']
def MINLIN(s): return str(E['minlin'][s])
def MAXLIN(s): return str(E['maxlin'][s])
def NLE(k, skip00=True):
    """number of subsets x edges whose shortest linear HTR is at most k (0c0 0e, already HTR or U D', left out)"""
    return str(sum(1 for s, v in E['minlin'].items() if v <= k and not (skip00 and s == '0c0 0e')))
def ROD(sub, M, col):
    r = [r for r in _tsv('q9_rodney_table.tsv') if r['subset'] == sub and r['M_minus_opt_or_M'] == M][0]
    return r[col]
def WIT(i, *path):
    v = W[i]
    for p in path: v = v[p]
    return v
def WXX(i, *path):
    v = WX[i]
    for p in path: v = v[p]
    return v
def NTOK(seq): return str(len(seq.split()))
def INV(seq):
    out = []
    for m in reversed(seq.split()):
        out.append(m[0] if m.endswith("'") else m if m.endswith('2') else m + "'")
    return ' '.join(out)
def SE(p, nn): return f'{math.sqrt(float(p) * (1 - float(p)) / nn) * 100:.1f}'
ENV = {k: v for k, v in globals().items() if not k.startswith('_')}
def DOC9(q, col):
    r = [r for r in _tsv('compare_doc9.tsv') if r['quantity'] == q][0]
    return r[col]
def D171(which, i):
    return E[which][i]
ENV = {k: v for k, v in globals().items() if not k.startswith('_')}
def JT():
    """JTuu's four shares (T5744) against mine, in points: linear <= 7, 4a1 <= 4, both, both with 8 / 5"""
    e = E['claims']['C26']['evidence']
    mine = [e.split('(linear alone ')[1].split(',')[0], e.split('bounding alone ')[1].split(')')[0], e.split('<= 4 in ')[1].split(' ')[0], e.split('<= 8 / <= 5: ')[1].split(' ')[0]]
    return list(zip([47.30, 53.55, 64.65, 86.05], [float(m.rstrip('%')) for m in mine]))
ENV = {k: v for k, v in globals().items() if not k.startswith('_')}
def SECTIONS(fin):
    """half turns between quarter turns of a finish (U/D quarter turns)"""
    out = [0]
    for m in fin.split():
        if m[0] in 'UD' and not m.endswith('2'): out.append(0)
        else: out[-1] += 1
    return out
def WINDOWS(fin):
    """1q reduction length leaving quarter turn q with its two sections: L - 1 - s_(q-1) - s_q"""
    s = SECTIONS(fin); L = len(fin.split())
    return [L - 1 - s[q - 1] - s[q] for q in range(1, len(s))]
def LB11503(Rp, N, S, al, shared=False):
    """FakeMMAP's first T11503 bound, ceil((|S|(R'+1) - N + sum alpha) / (|S| - 1)); alpha_i (as written) or alpha_(i+1)"""
    sm = sum(al[i + 1] if shared else al[i] for i in S if i + 1 in S)
    return (len(S) * (Rp + 1) - N + sm) / (len(S) - 1)
def T2(M, N, S, al, derived=False):
    """T11502 term 2: as printed ((|S|-1)M - (N-|S|) + sum alpha_i)/|S|, derived ((|S|-1)M + (N-|S|) - sum alpha_(i+1))/|S|"""
    k = len(S)
    if derived: return ((k - 1) * M + (N - k) - sum(al[i + 1] for i in S if i + 1 in S)) / k
    return ((k - 1) * M - (N - k) + sum(al[i] for i in S if i + 1 in S)) / k
ENV ={k: v for k, v in globals().items() if not k.startswith('_')}
def EV(cid, before, after=None):
    """a piece of a claims.tsv evidence string: the text after `before` up to `after` (default: the next space)"""
    s = E['claims'][cid]['evidence'].split(before, 1)[1]
    return s.split(after if after else ' ', 1)[0].rstrip('.,;')
ENV = {k: v for k, v in globals().items() if not k.startswith('_')}
G12 = ['0c0', '2c5', '2c4', '0c3', '4a2', '4a1', '2c3', '0c4', '4c3', '4c4', '4b2', '4b5']
def BUDF(g, b, step, tg='opt'):
    r = [r for r in _tsv('q2_checklist_budget.tsv') if r['group'] == g and r['level'] == 'C' and r['target'] == tg and r['budget'] == b and r['step'] == str(step)]
    return float(r[0]['cumulative'])
ENV = {k: v for k, v in globals().items() if not k.startswith('_')}
def SAMEF(g, b, step):
    return float([r for r in _tsv('q2_same_classes_p1.tsv') if r['group'] == g and r['budget'] == b and r['step'] == str(step)][0]['cum_p1'])
def ARGMIN(f): return min(G12, key=f)
def ARGMAX(f): return max(G12, key=f)
ENV = {k: v for k, v in globals().items() if not k.startswith('_')}
def BIGSTEP(name, col='cumulative_opt_htr_budget2'):
    """the step after the first that adds the most: (step, points added, description)"""
    rows = sorted([r for r in E['q6'] if r['checklist'] == name], key=lambda r: int(r['step']))
    best = max(range(1, len(rows)), key=lambda i: float(rows[i][col]) - float(rows[i - 1][col]))
    return rows[best]['step'], f"{(float(rows[best][col]) - float(rows[best - 1][col])) * 100:.1f}", rows[best]['step_description']
ENV = {k: v for k, v in globals().items() if not k.startswith('_')}
# what the edge count is worth (edge_gain.py) and edge counts along the route (edge_steps.py)
def EGA(tg, k): return f"{E['eg']['all'][tg][str(k)] * 100:.1f}"
def EGC(g, tg, k): return f"{E['eg']['corner'][g][tg][str(k)] * 100:.1f}"
def EGR(s, k, which='own', tg='opt'): return pc(E['eg']['rows'][s][tg][f'{which}{k}'])
def EGG(s, k, tg='opt'): return f"{E['eg']['rows'][s][tg][f'gain{k}'] * 100:.1f}"
def EGF(s, col='own_first'): return '`' + E['eg']['rows'][s]['opt'][col].replace(' | ht', '') + '`'
def EGRANK(s): return E['eg']['rows'][s]['opt']['pooled_first_rank']
def EGMAX(corners, tg='opt'):
    return f"{max(r[tg][f'gain{k}'] for s, r in E['eg']['rows'].items() if s.split()[0] in corners for k in '1235') * 100:.1f}"
def ESV(s, via, tg='opt'): return pc(E['es']['via'][f'{s}|{tg}'].get(via, 0))
def ESR(x, e, tg='opt'): return pc(E['es']['rev'][f'{x}|{tg}'][e])
def ESA(tg, which, i): return pc(E['es']['all'][tg][which][i])
def ESM(k, tg='opt'): return str(E['es']['all'][tg]['match1'].get(str(k), 0))
def ESL(f, tg='opt'): return [k.split('|')[0] for k, v in E['es']['ref'].items() if k.endswith('|' + tg) and f(v)]
ENV = {k: v for k, v in globals().items() if not k.startswith('_')}
# edge paths of the finish, read forward (edge_paths.py, xedgepaths.py)
def _ep(): return _j('edge_paths_extra.json')
_EPX = []
def EPX():
    if not _EPX: _EPX.append(_ep())
    return _EPX[0]
def EPP(s, path, tg='opt'):
    """share of DRs of subset x edges s with a finish of form `path` ('2c4 2e > 2c3 2e > ... > HTR'); 0 if under 0.1%"""
    r = [r for r in _tsv('edge_paths.tsv') if r['subset'] == s and r['target'] == tg and r['path'] == path]
    return pc(r[0]['share']) if r else '0%'
def EPT(s, rank, col='share', tg='opt'):
    v = EPX()['top'][f'{s}|{tg}|{rank}'][col]
    return v if col == 'path' else pc(v)
def EPS1(s, nxt, e='any', tg='opt'): return pc(EPX()['step1'][f'{s}|{tg}|{nxt}'][e])
def EPS2(s, first, nxt, e='any', tg='opt'): return pc(EPX()['step2'][f'{s}|{tg}|{first}|{nxt}'][e])
def EPN80(s, tg='opt'): return str(EPX()['need80'][f'{s}|{tg}'])
def EPM(s, col): return EPX()['meta'][s][col]
def EPW(*path):
    v = EPX()['witness']
    for p in path: v = v[p]
    return v
ENV = {k: v for k, v in globals().items() if not k.startswith('_')}
# exact over every DR state: the shortest NISS HTR (verify/vhtr nissall -> out/checks/niss_exact.tsv)
def _nx(g): return [r for r in _tsv('checks/niss_exact.tsv') if g == 'all' or r['subset'] == g or r['subset'].split()[0] == g]
def NXD(g, k):
    """share of the DR states of g ('all', a corner subset or a subset x edges) whose shortest NISS HTR is k moves
    shorter than the shortest linear HTR on the better side (k = 0, 1; k = 2 means 2 or more)"""
    rs = _nx(g)
    return sum(int(r['states']) for r in rs if (int(r['linear_minus_niss']) == k if k < 2 else int(r['linear_minus_niss']) >= 2)) / sum(int(r['states']) for r in rs)
def NXMAX(g='all'): return max(int(r['niss_htr']) for r in _nx(g))
def NXMIN(g): return min(int(r['niss_htr']) for r in _nx(g))
def NXN(k, g='all'): return sum(int(r['states']) for r in _nx(g) if int(r['niss_htr']) == k)
def LM():
    """(pairs with X m one move shorter than X, all pairs) over every DR state X and side half turn m, exact
    (research/verify/out/lastmove.txt)"""
    m = re.search(r'half turns: (\d+); one shorter: (\d+)', open(O + '../verify/out/lastmove.txt').read())
    return int(m.group(2)), int(m.group(1))
def V9():
    """(cases where the smallest term as printed is too short, all cases) at the optimum, unweighted, from the
    independent recount of section 9 (research/verify/out/recount_t11503.txt)"""
    t = open(O + '../verify/out/recount_t11503.txt').read()
    return (int(re.search(r'as printed \(term 2 signs, alpha_i\) below the need: (\d+)', t).group(1)),
            int(re.search(r'at the optimum: (\d+)', t).group(1)))
ENV = {k: v for k, v in globals().items() if not k.startswith('_')}
