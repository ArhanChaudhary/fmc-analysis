#!/usr/bin/env python3
"""Independent check of the edge paths of `htrtools edgepaths` (edge_paths.py), with nissy and the sticker model.

For each checked state (the first N states of one subset x edges of the main sample, plus the first 5 of every other
subset x edges):
  1. `htrtools trace` gives one optimal finish, only to write the state as a DR scramble (its inverse);
  2. nissy (an independent solver) lists every optimal DR finish (`solve drudfin -o -a`); its length must equal the
     optimum in the edgepaths file;
  3. each nissy finish is expanded to every order of its commuting opposite-face pairs (U D / D U, R2 L2 / L2 R2, ...),
     the form htrtools enumerates; the count must equal htrtools' number of optimal finishes;
  4. each finish is replayed on the sticker model (sticker.py, geometry only): it must solve the cube; its edge path
     (sticker labels at the start and after each quarter turn, up to the first HTR state, normal side only) and its
     HTR length are recorded;
  5. per state, the set of edge paths of optimal finishes, and the shortest HTR of each, must equal the edgepaths file;
  6. for the chosen subset x edges, the share of each edge path over the checked states is recomputed from the sticker
     paths alone and printed next to the share from the edgepaths file on the same states and on all 25,000.
Output: out/checks/check_edge_paths.txt.
usage: check_edge_paths.py <ep dir> <states dir> <htrtools> <exact.u8> <subset, e.g. 2c4_2e> <N>"""
import sys, os, json, subprocess, collections, re, csv, time, itertools
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import sticker
from sticker import do, SOLVED, inv_seq, QT
EPD, STD, TOOL, EXACT, SUB, N = sys.argv[1:7]; N = int(N)
OUTF = sys.argv[7] if len(sys.argv) > 7 else os.path.join(HERE, '..', 'out', 'checks', 'check_edge_paths.txt')
NISSY = '/data/fmc/tools/nissy-2.0.8/nissy'

def keys():
    K = {}
    with open(f'{EPD}/ep_keys.tsv') as f:
        next(f)
        for l in f:
            i, p = l.rstrip('\n').split('\t'); K[int(i)] = p
    return K
K = keys()
def ep_rows(sub):
    out = []
    with open(f'{EPD}/ep_{sub}.tsv') as f:
        next(f)
        for l in f:
            v = l.rstrip('\n').split('\t')
            out.append((int(v[0]), int(v[1]), int(v[2]), int(v[3]),
                        {K[int(x.split(':')[0])]: int(x.split(':')[2]) for x in v[4:] if x.split(':')[1] == '0'}))
    return {r[0]: r for r in out}
subs = sorted(f[7:-4] for f in os.listdir(STD) if f.startswith('states_'))
todo = []                       # (sub, idx, '#c,e,s')
for s in subs:
    rows = list(csv.DictReader(open(f'{STD}/states_{s}.tsv'), delimiter='\t'))
    for r in rows[:N if s == SUB else 5]:
        todo.append((s, int(r['idx']), f"#{r['c']},{r['e']},{r['s']}"))
EP = {s: ep_rows(s) for s in {t[0] for t in todo}}

t0 = time.time()
p = subprocess.run([TOOL, 'trace', EXACT, '0'], input='\n'.join(t[2] for t in todo) + '\n', capture_output=True, text=True, check=True)
tr = [json.loads(l) for l in p.stdout.strip().split('\n')]
assert len(tr) == len(todo)
scr = [' '.join(inv_seq(j['all'][0])) if j['all'] else '' for j in tr]
print(f'trace {len(tr)} in {time.time() - t0:.0f}s', flush=True)

env = dict(os.environ, NISSYDATA='/data/fmc/tools/nissy-data')
p = subprocess.run([NISSY], input='\n'.join(f'solve drudfin -o -a -n 1000000 {s}' for s in scr) + '\n',
                   capture_output=True, text=True, env=env)
chunks = p.stdout.split('nissy-# ')[1:]
assert len(chunks) >= len(todo), (len(chunks), len(todo))
print(f'nissy in {time.time() - t0:.0f}s', flush=True)

AX = {'U': 0, 'D': 0, 'R': 1, 'L': 1, 'F': 2, 'B': 2}
def orders(fin):
    """every order of the adjacent opposite-face pairs of a finish"""
    ms = fin.split(); runs = []; i = 0
    while i < len(ms):
        if i + 1 < len(ms) and AX[ms[i][0]] == AX[ms[i + 1][0]] and ms[i][0] != ms[i + 1][0]:
            runs.append([ms[i:i + 2], ms[i + 1:i + 2] + ms[i:i + 1]]); i += 2
        else:
            runs.append([ms[i:i + 1]]); i += 1
    return {' '.join(sum(c, [])) for c in itertools.product(*runs)}

def path(X, fin):
    st = X; labs = [sticker.label(st)]
    if sticker.in_htr(st): return labs, 0
    for i, m in enumerate(fin):
        st = do(st, m)
        if m in QT:
            labs.append(sticker.label(st))
            if sticker.in_htr(st): return labs, i + 1
    raise AssertionError('no HTR')

stats = collections.Counter(); bad = []
share_chk = collections.Counter(); share_ep = collections.Counter(); nsub = 0
for (s, idx, _), j, sc, ch in zip(todo, tr, scr, chunks):
    idx_, d, capped, nopt, epset = EP[s][idx]
    lines = [l for l in ch.strip().split('\n') if re.search(r'\(\d+\)\s*$', l)]
    sols = [re.sub(r'\s*\(\d+\)\s*$', '', l).strip() for l in lines]
    lens = {int(re.search(r'\((\d+)\)\s*$', l).group(1)) for l in lines}
    stats['states'] += 1
    ok_len = lens == {d} or (d == 0 and not sols)
    stats['nissy optimum = edgepaths optimum'] += ok_len
    if not ok_len: bad.append(('length', s, idx, sorted(lens), d))
    fins = set().union(*[orders(x) for x in sols]) if sols else {''}
    stats['finish count = htrtools count'] += len(fins) == nopt
    if len(fins) != nopt and not capped: bad.append(('count', s, idx, len(fins), nopt))
    X = do(SOLVED, sc)
    mine = {}
    for f in fins:
        mv = f.split()
        if do(X, mv) != SOLVED: bad.append(('replay', s, idx, f)); continue
        stats['finishes replayed'] += 1
        labs, h = path(X, mv)
        key = ' > '.join(labs)
        mine[key] = min(mine.get(key, 99), h)
    eq = mine == epset
    stats['edge-path sets and HTR lengths equal'] += eq
    if not eq: bad.append(('paths', s, idx, sorted(set(mine) ^ set(epset))[:4], capped))
    if s == SUB:
        nsub += 1
        for k in mine: share_chk[k] += 1
        for k in epset: share_ep[k] += 1
print(f'sticker done in {time.time() - t0:.0f}s', flush=True)

# shares of the chosen row: sticker paths on the checked states, edgepaths file on the same states and on all states
allrows = ep_rows(SUB); full = collections.Counter(k for r in allrows.values() for k in r[4])
fmt = lambda k: ' > '.join(k.split(' > ')[:-1] + ['HTR'])
out = [f'states {stats["states"]} (the first {N} of {SUB.replace("_", " ")}, the first 5 of every other subset x edges)']
out += [f'{k}: {v}' for k, v in stats.items()]
out.append(f'failures: {len(bad)}')
out += [repr(b)[:400] for b in bad[:20]]
out.append(f'\n{SUB.replace("_", " ")}: share of DRs with some optimal finish of each form (forms with >= 1% on all states)')
out.append('form\tsticker, checked states\tedgepaths, same states\tedgepaths, all ' + str(len(allrows)))
for k, c in full.most_common():
    if c / len(allrows) < 0.01: break
    out.append(f'{fmt(k)}\t{share_chk[k] / nsub:.4f}\t{share_ep[k] / nsub:.4f}\t{c / len(allrows):.4f}')
print('\n'.join(out))
open(OUTF, 'w').write('\n'.join(out) + '\n')
