#!/usr/bin/env python3
"""Extra witnesses for the write-up and the errata (out/witness_extra.json), each replayed on the sticker model.

  X1  a 2c3 state where no reduction to 1q (4a1 4e) of at most 4 moves, on normal, on inverse or split, leads to a
      finish within optimal + 1 (Levi Gibson's "all sub-5 reductions ... optimal like 75% of the time, and optimal
      +1 the rest of the time").  Every reduction (P on normal, U on inverse, each empty or ending in a U/D quarter
      turn, |P| + |U| <= 4) is enumerated here on the sticker model; the reduced state is inv(U) + scramble + P,
      read with sticker.label; its optimal finish comes from the exact table (htrtools trace).  Also the shortest
      reduction that does give the optimal, with the rest of the finish, replayed.
  X2  a 0c3 4e whose shortest linear HTR is 13 on both sides and whose shortest NISS HTR is 12 (Lewis Isom: "12
      moves linearly, and 11 moves using NISS"), the lengths confirmed by nissy (`solve htr-drud -L`, `-N`), and an
      HTR of each length found by nissy replayed on the sticker model.
usage: xwitness.py"""
import json, os, subprocess, sys, csv, itertools
from common import R, OUT
import sticker
from sticker import do, SOLVED, inv_seq, DRM, QT
TOOL = f'{R}/htrtools/target/release/htrtools'
EXACT = '/data/fmc/judging-a-dr/research/data/lean_exact_table.u8'
CAP = ['systemd-run', '--user', '--scope', '-q', '-p', 'MemoryMax=4G']
NISSY = '/data/fmc/tools/nissy-2.0.8/nissy'
ENV = dict(os.environ, NISSYDATA='/data/fmc/tools/nissy-data')
checks = [0]; bad = []
def check(ok, what):
    checks[0] += 1
    if not ok: bad.append(what)

def trace(lines):
    p = subprocess.run(CAP + [TOOL, 'trace', EXACT, '0'], input='\n'.join(lines) + '\n', capture_output=True, text=True, check=True)
    return [json.loads(l) for l in p.stdout.strip().split('\n')]

def seqs(n):
    """DR-move sequences of length n, no two moves on one face in a row, ending in a U/D quarter turn"""
    out = []
    def rec(cur):
        if len(cur) == n:
            if cur[-1] in QT: out.append(tuple(cur))
            return
        for m in DRM:
            if cur and cur[-1][0] == m[0]: continue
            rec(cur + [m])
    if n == 0: return [()]
    rec([]); return out

out = {}
# ------------------------------------------------------------------ X1
rows = [r for r in csv.DictReader(open(f'{R}/out/big/bound2.tsv'), delimiter='\t') if r['subset'] in ('2c3 2e', '2c3 4e')]
cand = None
for r in rows:
    need = 99
    for c in r['cells'].split(';'):
        dl, p, r1, r2, sec = c.split(':')
        if int(dl) <= 1: need = min(need, 0 if '-' not in p else int(r1))
    if need > 4 and int(r['d']) <= 13:
        cand = r; break
t = trace([f"#{cand['c']},{cand['e']},{cand['s']}"])[0] if False else None
# the state index of bound2 rows is the states file's (c, e, s)
st = {x['idx']: x for x in csv.DictReader(open(f"{R}/out/big/run1/states_{cand['subset'].replace(' ', '_')}.tsv"), delimiter='\t')}[cand['idx']]
t = trace([f"#{st['c']},{st['e']},{st['s']}"])[0]
scr = ' '.join(inv_seq(t['all'][0].split()))
opt = t['d']
X = do(SOLVED, scr)
check(do(X, t['all'][0]) == SOLVED, 'X1 optimal')
check(sticker.label(X) == cand['subset'], ('X1 label', sticker.label(X)))
red = {}
for a in range(0, 5):
    for b in range(0, 5 - a):
        if a + b == 0: continue
        for P in seqs(a):
            for U in seqs(b):
                rs = ' '.join(list(inv_seq(list(U))) + scr.split() + list(P))
                s = do(SOLVED, rs)
                if sticker.label(s) == '4a1 4e':
                    k = s if isinstance(s, (str, bytes, tuple)) else tuple(s)
                    if k not in red or a + b < red[k][0]: red[k] = (a + b, P, U, rs)
items = list(red.values())
tr = trace([x[3] for x in items])
best = min(x[0] + y['d'] for x, y in zip(items, tr))
check(best > opt + 1, ('X1 best', best, opt))
# the shortest reduction that does give the optimal: from the optimal finishes, split P | Q | T
short = None
for fin in t['all']:
    mv = fin.split(); n = len(mv)
    for i in range(n + 1):
        for j in range(i, n + 1):
            P, Qm, T = mv[:i], mv[i:j], mv[j:]
            if (P and P[-1] not in QT) or (T and T[0] not in QT): continue
            if sum(m in QT for m in Qm) != 1: continue
            if short is None or len(P) + len(T) < short[0]:
                short = (len(P) + len(T), P, Qm, T, fin)
L, P, Qm, T, fin = short
Ustr = inv_seq(T)
rs = ' '.join(list(T) + scr.split() + list(P))
s = do(SOLVED, rs)
check(sticker.label(s) == '4a1 4e' and do(s, ' '.join(Qm)) == SOLVED, 'X1 reduction')
check(do(X, ' '.join(P + Qm + T)) == SOLVED and len(P + Qm + T) == opt, 'X1 finish')
out['X1'] = dict(subset=cand['subset'], scramble=scr, optimal=opt, optimal_finish=t['all'][0], n_optimal=t['nopt'],
                 reductions_le4=len(items), best_with_reduction_le4=best,
                 shortest_reduction=L, normal=' '.join(P), inverse=' '.join(Ustr), rest=' '.join(Qm), finish=fin)

# ------------------------------------------------------------------ X2
st = {x['idx']: x for x in csv.DictReader(open(f'{R}/out/big/run1/states_0c3_4e.tsv'), delimiter='\t')}['878']
t = trace([f"#{st['c']},{st['e']},{st['s']}"])[0]
scr = ' '.join(inv_seq(t['all'][0].split()))
X = do(SOLVED, scr)
check(do(X, t['all'][0]) == SOLVED, 'X2 optimal')
def nissy(opt, s):
    p = subprocess.run([NISSY, 'solve', 'htr-drud', opt, s], capture_output=True, text=True, env=ENV)
    return p.stdout.strip().split('\n')[0]
lin = nissy('-L', scr); nis = nissy('-N', scr)
def parse(line):
    body, n = line.rsplit('(', 1)[0].strip(), int(line.rsplit('(', 1)[1].rstrip(')'))
    nm, im = body, ''
    if '(' in body:
        nm, im = body.split('(', 1); im = im.rstrip(')').strip(); nm = nm.strip()
    return nm.split(), im.split(), n
nm, im, nl = parse(lin)
check(sticker.in_htr(do(do(SOLVED, ' '.join(inv_seq(scr.split()) if not nm else scr.split())), ' '.join(im if not nm else nm))) and nl == 13, ('X2 linear', lin))
nm2, im2, nn = parse(nis)
s1 = sticker.replay(scr, ' '.join(nm2), ' '.join(im2)) if hasattr(sticker, 'replay') else None
# NISS: normal moves A, inverse moves B: the inverse-side state (X A)^-1 B must be in HTR
sB = do(SOLVED, ' '.join(inv_seq(scr.split() + nm2) + im2))
check(sticker.in_htr(sB) and nn == 12, ('X2 niss', nis))
check(int(st['htrN']) == 13 and int(st['htrI']) == 13 and int(st['htrNiss']) == 12, 'X2 states row')
out['X2'] = dict(subset='0c3 4e', scramble=scr, optimal=t['d'], optimal_finish=t['all'][0],
                 nissy_linear=lin, nissy_niss=nis, htr_normal=int(st['htrN']), htr_inverse=int(st['htrI']), htr_niss=int(st['htrNiss']))
out['checks'] = checks[0]; out['failed'] = bad
json.dump(out, open(f'{OUT}/witness_extra.json', 'w'), indent=1)
print(json.dumps(out, indent=1)[:3000])
print(f'{checks[0]} checks, {len(bad)} failed', bad)
sys.exit(1 if bad else 0)
