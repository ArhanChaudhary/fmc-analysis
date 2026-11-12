#!/usr/bin/env python3
"""Independent checks of the route machinery on random DR states (SPEC "Checks").

For each state (1,000 random DR-move scrambles of length 25-40, plus 5 states of every subset from the main sample):
  1. htrtools trace lists every optimal finish (all orders of commuting moves) and, for the first CAP of them, every
     NISS reading with its H key (route to HTR), F key (labels over the whole finish) and HTR length;
  2. every listed finish is replayed on the sticker model (must solve the scrambled cube, length = optimum);
  3. sticker.py re-reads every finish at every split k = 0..n, both sides first, with its own labels and HTR test;
     the set of H keys, of F keys, and the shortest HTR of each H key must equal what htrtools printed;
  4. nissy (an independent solver) lists all optimal DR finishes (`solve drudfin -o -a`); after putting commuting
     opposite-face moves in one order, its set must equal htrtools' set.
Output: out/checks/check_sticker.txt.  Usage: check_sticker.py [n_random] [cap]"""
import sys, os, json, random, subprocess, collections, re, glob, csv, time
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import sticker
from sticker import do, SOLVED, inv_seq, DRM
R = os.path.join(HERE, '..')
EXACT = '/data/fmc/judging-a-dr/research/data/lean_exact_table.u8'
TOOL = os.environ.get('HTRTOOLS', f'{R}/htrtools/target/release/htrtools')
NR = int(sys.argv[1]) if len(sys.argv) > 1 else 1000
CAP = int(sys.argv[2]) if len(sys.argv) > 2 else 60
rng = random.Random(20261112)

def rand_scr():
    s = []
    n = rng.randint(25, 40)
    while len(s) < n:
        m = rng.choice(DRM)
        if s and s[-1][0] == m[0]: continue
        s.append(m)
    return ' '.join(s)
inputs = [rand_scr() for _ in range(NR)]
for f in sorted(glob.glob(f'{R}/out/big/run1/states_*.tsv')):
    rows = list(csv.DictReader(open(f), delimiter='\t'))[:5]
    inputs += [f"#{r['c']},{r['e']},{r['s']}" for r in rows]

def run_trace(lines, cap):
    p = subprocess.run(['systemd-run', '--user', '--scope', '-q', '-p', 'MemoryMax=5G', TOOL, 'trace', EXACT, str(cap)],
                       input='\n'.join(lines) + '\n', capture_output=True, text=True, check=True)
    return [json.loads(l) for l in p.stdout.strip().split('\n')]
t0 = time.time()
tr = run_trace(inputs, CAP)
print(f'trace: {len(tr)} states in {time.time() - t0:.0f}s', flush=True)

stats = collections.Counter(); bad = []
def norm_comm(moves):
    """put adjacent commuting opposite-face moves in the order U D, R L, F B"""
    ms = moves.split(); ch = True
    order = 'UDRLFB'
    while ch:
        ch = False
        for i in range(len(ms) - 1):
            a, b = ms[i][0], ms[i + 1][0]
            if order.index(a) // 2 == order.index(b) // 2 and order.index(a) > order.index(b):
                ms[i], ms[i + 1] = ms[i + 1], ms[i]; ch = True
    return ' '.join(ms)

nissy_cmds = []
for j in tr:
    scr = j['input']
    if scr.startswith('#'):
        scr = ' '.join(inv_seq(j['all'][0])) if j['all'] else ''
    j['scr'] = scr
    X = do(SOLVED, scr)
    # 2. replay every finish
    for f in j['all']:
        ok = do(X, f) == SOLVED and len(f.split()) == j['d']
        stats['finish replayed'] += 1; stats['finish replay ok'] += ok
        if not ok: bad.append(('replay', scr, f))
    if len(set(j['all'])) != len(j['all']): bad.append(('duplicate finishes', scr))
    # 3. readings
    for fin in j['finishes']:
        mv = fin['moves'].split(); n = len(mv)
        rh, rf = {}, set()
        for r in fin['readings']:
            rh[r['h']] = min(rh.get(r['h'], 99), r['htr']); rf.add(r['f'])
        ph, pf = {}, set()
        for k in range(n + 1):
            for inv_first in (False, True):
                h, f, hl = sticker.reading(scr.split(), mv, k, inv_first)
                ph[h] = min(ph.get(h, 99), hl); pf.add(f)
        stats['finish read'] += 1
        stats['H key sets equal'] += rh.keys() == ph.keys()
        stats['F key sets equal'] += rf == pf
        stats['HTR lengths equal'] += rh == ph
        if rh != ph or rf != pf:
            bad.append(('readings', scr, fin['moves'], sorted(rh.items()), sorted(ph.items()), sorted(rf ^ pf)))
    nissy_cmds.append(f'solve drudfin -o -a -n 1000000 {scr}')
print(f'sticker checks done in {time.time() - t0:.0f}s', flush=True)

# 4. nissy
env = dict(os.environ, NISSYDATA='/data/fmc/tools/nissy-data')
p = subprocess.run(['systemd-run', '--user', '--scope', '-q', '-p', 'MemoryMax=3G', '/data/fmc/tools/nissy-2.0.8/nissy'],
                   input='\n'.join(nissy_cmds) + '\n', capture_output=True, text=True, env=env)
chunks = p.stdout.split('nissy-# ')[1:]
for j, ch in zip(tr, chunks):
    sols = [re.sub(r'\s*\(\d+\)\s*$', '', l).strip() for l in ch.strip().split('\n') if re.search(r'\(\d+\)\s*$', l)]
    lens = {int(re.search(r'\((\d+)\)\s*$', l).group(1)) for l in ch.strip().split('\n') if re.search(r'\(\d+\)\s*$', l)}
    ns = {norm_comm(s) for s in sols}
    rs = {norm_comm(s) for s in j['all']}
    stats['nissy states'] += 1
    stats['nissy optimal length equal'] += lens == {j['d']} or (j['d'] == 0 and not sols)
    stats['nissy finish sets equal'] += ns == rs
    stats['nissy count == nopt_canon'] += len(sols) == j['nopt_canon']
    if ns != rs: bad.append(('nissy', j['scr'], j['d'], sorted(lens), len(ns), len(rs)))
lines = [f'states {len(tr)} ({NR} random-move scrambles + 5 per subset from the main sample); readings checked for the '
         f'first {CAP} optimal finishes of each state']
lines += [f'{k}: {v}' for k, v in stats.items()]
lines.append(f'failures: {len(bad)}')
lines += [repr(b)[:600] for b in bad[:20]]
print('\n'.join(lines))
open(f'{R}/out/checks/check_sticker.txt', 'w').write('\n'.join(lines) + '\n')
