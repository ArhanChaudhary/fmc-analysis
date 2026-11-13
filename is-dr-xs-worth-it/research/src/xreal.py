#!/usr/bin/env python3
"""The 500 scrambles: what DR-xs adds to the normal DRs.  Reads out/attempts_1s.tsv and out/attempts_8fe.tsv
(xstools attempts) and the first study's out/hand/attempt_run.csv (every EO-first DR up to 12 moves, cubelib-cli).
Writes report/data/real_*.md and out/real.json."""
import csv, json, collections, sys
import xv
from xv import fmt, num, hu, O
D = '/data/fmc/is-dr-xs-worth-it/report/data/'
def load(name): return list(csv.DictReader(open(O + name), delimiter='\t'))
base = {}
for l in open('/data/fmc/judging-a-dr/research/out/hand/attempt_run.csv'):
    if l.startswith('#'): continue
    v = l.strip().split(',')
    if v[0] == 'scramble': head = v; continue
    base[int(v[0])] = {k: int(x) for k, x in zip(head, v)}
N = len(base)
one = collections.defaultdict(list); eight = collections.defaultdict(list)
for r in load('attempts_1s.tsv'): one[int(r['scramble'])].append(r)
for r in load('attempts_8fe.tsv'): eight[int(r['scramble'])].append(r)
def best(rows, maxlen, starts=None):
    v = [int(r['total']) for r in rows if int(r['length']) <= maxlen and (starts is None or r['start'] in starts)]
    return min(v) if v else 99
def count(rows, maxlen, starts=None): return sum(1 for r in rows if int(r['length']) <= maxlen and (starts is None or r['start'] in starts))
def classic(b, maxlen): return min(b[f'best{c}'] for c in (9, 10, 11, 12) if c <= maxlen)
def nclassic(b, maxlen): return sum(b[f'n{c}'] for c in (9, 10, 11, 12) if c <= maxlen)
def avg(xs): xs = list(xs); return sum(xs) / len(xs)
R = {}
def write(name, L): open(D + name + '.md', 'w').write('\n'.join(L) + '\n'); print(name, len(L))
S = sorted(base)
# ---- what there is
L = ['| On a scramble | Share of the 500 that have one | Average number per scramble |', '|---|---:|---:|']
def there(nm, f): L.append(f'| {nm} | {fmt(sum(1 for s in S if f(s) > 0), N)} | {hu(avg(f(s) for s in S), 1):,.1f} |')
TH = {}
def there(nm, f):
    L.append(f'| {nm} | {fmt(sum(1 for s in S if f(s) > 0), N)} | {hu(avg(f(s) for s in S), 1):,.1f} |'); TH[nm] = (fmt(sum(1 for s in S if f(s) > 0), N), f'{hu(avg(f(s) for s in S), 1):,.1f}')
there('a normal DR of 9 moves or less', lambda s: base[s]['n9']); there('a normal DR of 10 or less', lambda s: nclassic(base[s], 10)); there('a normal DR of 11 or less', lambda s: nclassic(base[s], 11))
for ln in (6, 7, 8): there(f'a DR-1s of {ln} or less from a slice-EO skip', lambda s, ln=ln: count(one[s], ln, ('0',)))
for ln in (6, 7, 8): there(f'a DR-1s of {ln} or less from a skip or a one-move slice EO', lambda s, ln=ln: count(one[s], ln))
for ln in (7, 8, 9): there(f'a DR-2s 8fe of {ln} or less (from a slice EO or an EO of 4 or less)', lambda s, ln=ln: count(eight[s], ln))
write('real_there', L); R['there'] = TH
R['share_1s8'] = fmt(sum(1 for s in S if count(one[s], 8) > 0), N); R['share_1s7'] = fmt(sum(1 for s in S if count(one[s], 7) > 0), N); R['n_1s8'] = f'{hu(avg(count(one[s], 8) for s in S)):.0f}'
sh = collections.Counter(min([int(r['length']) for r in one[s]] or [99]) for s in S)
R['shortest_1s'] = {k: v for k, v in sorted(sh.items())}
# ---- what it finishes in: the 491 scrambles that have a normal DR of 10 or less
H = [s for s in S if nclassic(base[s], 10) > 0]
pol = [('every normal DR of 10 or less', lambda s: (nclassic(base[s], 10), classic(base[s], 10))),
       ('normal DRs of 10 or less, and every DR-1s of 7 or less', lambda s: (nclassic(base[s], 10) + count(one[s], 7), min(classic(base[s], 10), best(one[s], 7)))),
       ('normal DRs of 10 or less, and every DR-1s of 8 or less', lambda s: (nclassic(base[s], 10) + count(one[s], 8), min(classic(base[s], 10), best(one[s], 8)))),
       ('normal DRs of 10 or less, every DR-1s of 8 or less and every DR-2s 8fe of 9 or less', lambda s: (nclassic(base[s], 10) + count(one[s], 8) + count(eight[s], 9), min(classic(base[s], 10), best(one[s], 8), best(eight[s], 9)))),
       ('every normal DR of 11 or less', lambda s: (nclassic(base[s], 11), classic(base[s], 11))),
       ('normal DRs of 11 or less, every DR-1s of 8 or less and every DR-2s 8fe of 9 or less', lambda s: (nclassic(base[s], 11) + count(one[s], 8) + count(eight[s], 9), min(classic(base[s], 11), best(one[s], 8), best(eight[s], 9)))),
       ('every normal DR of 12 or less', lambda s: (nclassic(base[s], 12), classic(base[s], 12))),
       ('normal DRs of 12 or less, every DR-1s of 8 or less and every DR-2s 8fe of 9 or less', lambda s: (nclassic(base[s], 12) + count(one[s], 8) + count(eight[s], 9), min(classic(base[s], 12), best(one[s], 8), best(eight[s], 9))))]
L = ['| You finish | Things to finish, per scramble | Average best solution, moves | Best solution in 20 or less | 19 or less |', '|---|---:|---:|---:|---:|']
for nm, f in pol:
    v = [f(s) for s in H]
    L.append(f'| {nm} | {hu(avg(c for c, _ in v)):,.0f} | {hu(avg(b for _, b in v), 2):.2f} | {fmt(sum(b <= 20 for _, b in v), len(H))} | {fmt(sum(b <= 19 for _, b in v), len(H))} |')
    R[nm] = dict(n=avg(c for c, _ in v), result=avg(b for _, b in v))
    R.setdefault('policies', []).append(dict(name=nm, n=avg(c for c, _ in v), result=avg(b for _, b in v)))
write('real_result', L); R['H'] = len(H)
# ---- head to head, all 500
L = ['| Against the best through a normal DR of | Best DR-xs solution shorter, share of scrambles | Equal | Longer, or no DR-xs |', '|---|---:|---:|---:|']
for ln in (10, 11, 12):
    w = e = l = 0
    for s in S:
        x = min(best(one[s], 8), best(eight[s], 9)); c = classic(base[s], ln)
        w += x < c; e += x == c and x < 99; l += x > c or (x == 99 and c == 99)
    L.append(f'| {ln} moves or less | {fmt(w, N)} | {fmt(e, N)} | {fmt(l, N)} |'); R[f'win{ln}'] = fmt(w, N); R[f'tie{ln}'] = fmt(e, N)
write('real_head', L)
# ---- per candidate: how they finish against the uniform samples, and how often one reaches the best normal-DR solution
allr = [r for s in S for r in one[s]]; alle = [r for s in S for r in eight[s]]
L = ['| Kind and length | Number on the 500 scrambles | Their average finish, moves | Average finish of the uniform sample, moves | Setup searched, real and sample alike |', '|---|---:|---:|---:|---|']
for ln in (6, 7, 8):
    rs = [r for r in allr if int(r['length']) == ln]
    L.append(f"| DR-1s in {ln} | {len(rs):,} | {hu(avg(int(r['finish']) for r in rs), 2):.2f} | {hu(xv.avg(xv.one_s()), 2):.2f} | any length from either end |")
for ln in (7, 8, 9):
    rs = [r for r in alle if int(r['length']) == ln]
    L.append(f"| DR-2s 8fe in {ln} | {len(rs):,} | {hu(avg(int(r['finish']) for r in rs), 2):.2f} | {hu(avg(int(x['finish_setup3']) for x in xv._rows('sample8fe.tsv')), 2):.2f} | up to 3 moves from either end |")
write('real_candidates', L)
L = ['| What you finish | How many per scramble | Share that reach the scramble\'s best normal-DR solution | One in this many reaches it |', '|---|---:|---:|---:|']
Y = {}
def yrow(nm, n, reach, key):
    L.append(f'| {nm} | {hu(n / N, 1):,.1f} | {fmt(reach, n)} | {hu(n / reach):,.0f} |' if reach else f'| {nm} | {hu(n / N, 1):,.1f} | 0 | |'); Y[key] = reach / n if n else 0
for c, nm in ((9, 'a normal DR of 9 or less'), (10, 'a normal DR of 10'), (11, 'a normal DR of 11'), (12, 'a normal DR of 12')):
    yrow(nm, sum(base[s][f'n{c}'] for s in S), sum(base[s][f'reach{c}'] for s in S), f'dr{c}')
for lo, hi, nm in ((0, 6, 'a DR-1s of 6 or less'), (7, 7, 'a DR-1s of 7'), (8, 8, 'a DR-1s of 8')):
    rs = [(int(r['total']), s) for s in S for r in one[s] if lo <= int(r['length']) <= hi]
    yrow(nm, len(rs), sum(t <= base[s]['best'] for t, s in rs), f'1s{hi}')
for lo, hi, nm in ((0, 8, 'a DR-2s 8fe of 8 or less'), (9, 9, 'a DR-2s 8fe of 9')):
    rs = [(int(r['total']), s) for s in S for r in eight[s] if lo <= int(r['length']) <= hi]
    yrow(nm, len(rs), sum(t <= base[s]['best'] for t, s in rs), f'8fe{hi}')
L = L[:2] + sorted(L[2:], key=lambda l: -float(l.split('|')[3].strip().rstrip('%').lstrip('<') or 0))
write('real_yield', L); R['yield'] = Y
R['cancel_1s'] = avg(int(r['length']) + int(r['finish']) - int(r['total']) for r in allr)
R['n1s'] = len(allr); R['n8'] = len(alle)
R['by_start_1s'] = dict(collections.Counter(r['start'] for r in allr)); R['by_start_8'] = dict(collections.Counter(r['start'] for r in alle))
json.dump(R, open(O + 'real.json', 'w'), indent=1)
for k, v in R.items(): print(k, v)

# ---- against 5-move EOs: the normal route by EO length (out/eo_run.tsv, xeo.py)
import os
if os.path.exists(O + 'eo_run.tsv'):
    eo = {int(r['scramble']): {k: int(v) for k, v in r.items()} for r in csv.DictReader(open(O + 'eo_run.tsv'), delimiter='\t')}
    R['eo'] = dict(eos4=avg(eo[s]['eos4'] for s in S), eos5=avg(eo[s]['eos5'] for s in S), none4=sum(eo[s]['eos4'] == 0 for s in S),
                   drs10_4=avg(eo[s]['drs10_eo4'] for s in S), drs10_5=avg(eo[s]['drs10_eo5'] for s in S), drs11_4=avg(eo[s]['drs11_eo4'] for s in S), drs11_5=avg(eo[s]['drs11_eo5'] for s in S))
    for cap, key in ((10, 'eo10'), (11, 'eo11')):
        Hs = [s for s in S if eo[s][f'best{cap}_eo4'] < 99]
        pol = [(f'EOs of 4 or less: every DR of {cap} or less', lambda s: (eo[s][f'drs{cap}_eo4'], eo[s][f'best{cap}_eo4'])),
               (f'EOs of 4 or less: DRs of {cap} or less, and every DR-1s of 7 or less from a slice EO', lambda s: (eo[s][f'drs{cap}_eo4'] + count(one[s], 7), min(eo[s][f'best{cap}_eo4'], best(one[s], 7)))),
               (f'EOs of 4 or less: DRs of {cap} or less, and every DR-1s of 8 or less from a slice EO', lambda s: (eo[s][f'drs{cap}_eo4'] + count(one[s], 8), min(eo[s][f'best{cap}_eo4'], best(one[s], 8)))),
               (f'EOs of 4 or less: DRs of {cap} or less, every DR-1s of 8 or less and every DR-2s 8fe of 9 or less', lambda s: (eo[s][f'drs{cap}_eo4'] + count(one[s], 8) + count(eight[s], 9), min(eo[s][f'best{cap}_eo4'], best(one[s], 8), best(eight[s], 9)))),
               (f'EOs of 5 or less: every DR of {cap} or less', lambda s: (eo[s][f'drs{cap}_eo5'], eo[s][f'best{cap}_eo5'])),
               (f'EOs of 5 or less: DRs of {cap} or less, every DR-1s of 8 or less and every DR-2s 8fe of 9 or less', lambda s: (eo[s][f'drs{cap}_eo5'] + count(one[s], 8) + count(eight[s], 9), min(eo[s][f'best{cap}_eo5'], best(one[s], 8), best(eight[s], 9))))]
        L = ['| You check and finish | Normal EOs to check, per scramble | Things to finish, per scramble | Average best solution, moves |', '|---|---:|---:|---:|']; P = []
        for i, (nm, f) in enumerate(pol):
            v = [f(s) for s in Hs]; ne = avg(eo[s]['eos4' if i < 4 else 'eos5'] for s in Hs)
            L.append(f'| {nm} | {hu(ne):,.0f} | {hu(avg(c for c, _ in v)):,.0f} | {hu(avg(b for _, b in v), 2):.2f} |'); P.append(dict(name=nm, eos=ne, n=avg(c for c, _ in v), result=avg(b for _, b in v)))
        write('real_' + key, L); R[key] = dict(H=len(Hs), policies=P)
    json.dump(R, open(O + 'real.json', 'w'), indent=1)
