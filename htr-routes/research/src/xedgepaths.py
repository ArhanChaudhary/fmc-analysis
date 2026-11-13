#!/usr/bin/env python3
"""Tables for "Edge paths of the finish" (section 4 and appendix A) from edge_paths.py's outputs:
report/data/edge_paths_*.md and out/edge_paths_extra.json (numbers the text quotes).  Light.
usage: xedgepaths.py"""
import csv, json, collections, os
from common import R, OUT, SUBS
D = os.path.normpath(os.path.join(R, '..', 'report', 'data')) + '/'
def T(name): return list(csv.DictReader(open(f'{OUT}/{name}'), delimiter='\t'))
def pc(x, d=None):
    x = float(x) * 100
    if x == 0: return '0%'
    if 99.95 <= x and d is None: return '>99.9%'
    if d is None: d = 1 if x >= 1 else 2 if x >= 0.1 else 3
    return f'{x:.{d}f}%'
def write(name, head, rows):
    out = ['| ' + ' | '.join(head) + ' |', '|' + '---|' * len(head)] + ['| ' + ' | '.join(str(x) for x in r) + ' |' for r in rows]
    open(D + name + '.md', 'w').write('\n'.join(out) + '\n')
EDG = ('0e', '2e', '4e', '6e', '8e')
LABELS = set(SUBS)                               # 'corner edges' labels that exist
def cell(corner, e, v):
    """a share, or '–' where the corner subset has no such edge count"""
    return pc(v) if f'{corner} {e}' in LABELS else '–'
paths = T('edge_paths.tsv')
for r in paths:
    if r['path'] == 'HTR': r['path'] = 'already HTR'      # a start state in HTR (0c0 0e only)
s1 = T('edge_paths_step1.tsv'); s2 = T('edge_paths_step2.tsv')
meta = json.load(open(f'{OUT}/edge_paths_meta.json'))
P = collections.defaultdict(list)
for r in paths: P[(r['subset'], r['target'])].append(r)
X = {'meta': meta, 'top': {}, 'need80': {}, 'step1': {}, 'step2': {}}

def need(rows, q):
    for r in rows:
        if float(r['union']) >= q: return int(r['rank'])
    return None
# 1. the three most common forms per subset x edges, and how many forms cover 80%
for tg, name in (('opt', 'edge_paths_top'), ('p1', 'edge_paths_top_p1')):
    rows = []
    for s in SUBS:
        L = P[(s, tg)]
        k = need(L, 0.8)
        X['need80'][f'{s}|{tg}'] = k
        for r in L[:3]:
            X['top'][f"{s}|{tg}|{r['rank']}"] = {'path': r['path'], 'share': float(r['share']), 'union': float(r['union'])}
            rows.append([s if r['rank'] == '1' else '', r['rank'], r['path'], pc(r['share']), pc(r['union']),
                         (str(k) if k else 'more than listed') if r['rank'] == '1' else ''])
    # the last column only on a row's first line; blank cells there would be dashed, so repeat it instead
    for i, r in enumerate(rows):
        if r[5] == '': r[5] = rows[i - 1][5]
        if r[0] == '': r[0] = rows[i - 1][0]
    write(name, ['Subset × edges', 'Rank', 'Form of the finish', 'DRs with an optimal finish of this form' if tg == 'opt' else 'DRs with a finish within +1 of this form',
                 'DRs with one of the forms so far', 'Forms needed for 80% of DRs'], rows)
# 2. every form with at least 2% (optimal)
rows = []
for s in SUBS:
    for r in P[(s, 'opt')]:
        if float(r['share']) < 0.02: break
        rows.append([s, r['rank'], r['path'], pc(r['share']), pc(r['union'])])
write('edge_paths_full', ['Subset × edges', 'Rank', 'Form of the finish', 'DRs with an optimal finish of this form', 'DRs with one of the forms so far'], rows)
# 3. first step: where the first quarter turn goes, with each edge count
S1 = collections.defaultdict(list)
for r in s1: S1[(r['subset'], r['target'])].append(r)
for k, L in S1.items():
    for r in L:
        X['step1'][f"{k[0]}|{k[1]}|{r['next']}"] = {e: (float(r[e]) if r[e] else 0.0) for e in ('any',) + EDG}
def s1rows(tg, only_top, cut=0.005):
    rows = []
    for s in SUBS:
        L = sorted(S1[(s, tg)], key=lambda r: -float(r['any']))
        for r in (L[:1] if only_top else L):
            if float(r['any']) < cut: continue
            c = r['next']
            if c == 'HTR':
                rows.append([s, 'HTR', pc(r['any'])] + ['–'] * len(EDG)); continue
            rows.append([s, c, pc(r['any'])] + [cell(c, e, r[e]) for e in EDG])
    return rows
H1 = ['From', 'First quarter turn to', 'DRs that can go there, any edge count'] + [f'with {e} (DRs)' for e in EDG]
write('edge_paths_step1', H1, s1rows('opt', True))
write('edge_paths_step1_full', H1, s1rows('opt', False))
write('edge_paths_step1_p1', H1, s1rows('p1', True))
# 4. second step, on the route: of the DRs whose optimal finish can take a first step, where the second qt can go
for r in s2:
    X['step2'][f"{r['subset']}|{r['target']}|{r['first']}|{r['next']}"] = {'first_share': float(r['first_share']), **{e: (float(r[e]) if r[e] else 0.0) for e in ('any',) + EDG}}
rows = []
for r in s2:
    if r['target'] != 'opt' or float(r['first_share']) < 0.2 or float(r['any']) < 0.1 or r['next'] == 'HTR': continue
    c = r['next']
    rows.append([r['subset'], r['first'], pc(r['first_share']), c, pc(r['any'])] + [cell(c, e, r[e]) for e in EDG])
write('edge_paths_step2', ['From', 'First quarter turn to', 'DRs that can go there', 'Second quarter turn to', 'Of those, can go on to it (any edge count)']
      + [f'with {e} (of those)' for e in EDG], rows)
X['witness'] = json.load(open(f'{OUT}/edge_paths_witness.json'))
# 5. the main checklist with edge counts (edge_paths_checklist.py): one table per corner subset
MERGE = {'4a3': '4c3', '4b3': '4c3', '4a4': '4c4', '4b4': '4c4'}
def hpath(k):
    """'2c4 2e > 2c3 4e > (4b2 2e > 4a1 4e > 0c0 0e) | ht' -> '`2c4 2e > 2c3 4e > (4b2 2e > 4a1 4e > HTR)`'"""
    body, post = k.rsplit(' | ', 1)
    parts = body.split(' > ')
    last = parts[-1]
    parts[-1] = ('(' if last.startswith('(') else '') + 'HTR' + (')' if last.endswith(')') else '')
    if len(parts) == 1: s = 'already HTR'
    else: s = ' > '.join(parts)
    s += ' \\| qt' if post == 'qt' else ''
    return '`' + s + '`' if len(parts) > 1 else s
def croute(c):
    if c in ('0c0 | ht', '0c0 | qt'): return 'already HTR' + (' \\| qt' if c.endswith('qt') else '')
    return '`' + (c[:-5] if c.endswith(' | ht') else c).replace('|', '\\|') + '`'
X['ck'] = {}
CK = T('edge_paths_checklist.tsv')
for g in dict.fromkeys(s.split()[0] for s in SUBS):
    rows = []
    for r in CK:
        if r['subset'].split()[0] != g: continue
        X['ck'][f"{r['subset']}|{r['step']}"] = r
        if r['fork_pos']:
            fc = r['fork_corner']
            fork = f"{fc}, qt {r['fork_pos']}" + (', inverse' if r['fork_side'] == 'inverse' else '')
            ec = [pc(r[e] or 0) if f'{MERGE.get(fc, fc)} {e}' in LABELS else '–' for e in EDG]
        else:
            fork = 'none'; ec = ['–'] * len(EDG)
        rows.append([r['subset'].split()[1], r['step'], croute(r['class']), pc(r['alone']), hpath(r['top_path']), pc(r['top']), fork] + ec)
    keep = [i for i in range(len(EDG)) if any(row[7 + i] != '–' for row in rows)]
    write(f'checklist_edges_{g}', ['Edges', 'Try', 'Corner route', 'Route finds the optimal', 'Most common edge path', 'Along that path', 'Forks at']
          + [f'{EDG[i]} there' for i in keep], [row[:7] + [row[7 + i] for i in keep] for row in rows])
json.dump(X, open(f'{OUT}/edge_paths_extra.json', 'w'), indent=1)
print('ok')
