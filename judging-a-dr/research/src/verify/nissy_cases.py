#!/usr/bin/env python3
"""All 3,072 HTR states of a 216-case (FakeMMAP label), each given to nissy's optimal solver with a cap of M face turns:
how many of them have a solution of M or less.  0 at M and some at M + 1 says the case's any-move value is M + 1.

  python3 research/src/verify/nissy_cases.py "F-D + F-V R-H odd" 5 "F-D + F-V R-H odd" 6 ...   (label, cap) pairs"""
import sys, os, re, subprocess, collections, numpy as np
sys.path.insert(0, '/data/fmc/judging-a-dr/research/tool'); import fmccube as fc
sys.path.insert(0, '/data/fmc/judging-a-dr/research/src')
Q = ['/data/fmc/judging-a-dr/research/drtools/target/release/drtools', 'query', '/data/fmc/judging-a-dr/research/data/drbfs', '/data/fmc/judging-a-dr/research/data/tables']
locs = sorted(k for k in fc.solved() if sum(abs(v) for v in k[0]) > 1); idx = {k: i for i, k in enumerate(locs)}
def move_perm(base, times):
    f, axis, layers = fc.ROT[base]; perm = np.arange(48)
    for _ in range(times):
        step = np.arange(48)
        for (p, n), i in idx.items():
            if p[axis] in layers: step[idx[(f(p), f(n))]] = i
        perm = perm[step]
    return perm
HALF = {f + '2': move_perm(f, 2) for f in 'UDRLFB'}
start = np.arange(48, dtype=np.uint8)
seen = {start.tobytes(): ''}; frontier = [start]
while frontier:
    nxt = []
    for s in frontier:
        w = seen[s.tobytes()]
        for name, p in HALF.items():
            t = s[p]; k = t.tobytes()
            if k not in seen: seen[k] = (w + ' ' + name).strip(); nxt.append(t)
    frontier = nxt
print('HTR states:', len(seen), file=sys.stderr)
def sticker(p, n): return idx[(tuple(p), tuple(n))]
cor_loc = [sticker(p, (0, p[1], 0)) for p in fc.CORNERS]; ude_loc = [sticker(p, (0, p[1], 0)) for p in fc.UD_EDGES]; ee_loc = [sticker(p, (0, 0, p[2])) for p in fc.E_EDGES]
cor_of = {l: i for i, l in enumerate(cor_loc)}; ude_of = {l: i for i, l in enumerate(ude_loc)}; ee_of = {l: i for i, l in enumerate(ee_loc)}
keys = list(seen)
lines = []
for k in keys:
    s = np.frombuffer(k, dtype=np.uint8)
    lines.append(' '.join(str(cor_of[int(s[l])]) for l in cor_loc) + ' ' + ' '.join(str(ude_of[int(s[l])]) for l in ude_loc) + ' ' + ' '.join(str(ee_of[int(s[l])]) for l in ee_loc))
out = subprocess.run(Q, input='\n'.join(lines) + '\n', capture_output=True, text=True, env=dict(os.environ, DRQ_NOEXACT='1')).stdout.strip().split('\n')
cls = [int(re.search(r'kfclass=(\d+)', l).group(1)) for l in out]
sizes = collections.Counter(cls); print('classes:', len(sizes), 'sizes:', set(sizes.values()), file=sys.stderr)

import json
def cls_of(seq):
    a = fc.to_dr_arrays(fc.state_after(seq))
    o = subprocess.run(Q, input=' '.join(map(str, a[0] + a[1] + a[2])) + '\n', capture_output=True, text=True, env=dict(os.environ, DRQ_NOEXACT='1')).stdout
    return int(re.search(r'kfclass=(\d+)', o).group(1))
# five corrected cells: example state (DR moves are not enough for two of them: use the any-move state's class via its HT word)
cases = {}
for line in open('/data/fmc/assets/attachments/1546077758189477989_0_message.txt'):
    m = re.match(r'^(\S+ \S) F-(\S) R-(\S)\s+(even|odd) E-parity: (\d+) Example scramble: ?(.*)$', line.rstrip('\n'))
    if m: cases[f'{m.group(1)} F-{m.group(2)} R-{m.group(3)} {m.group(4)}'] = (int(m.group(5)), m.group(6))
want = [(sys.argv[i], int(sys.argv[i + 1])) for i in range(1, len(sys.argv), 2)]
res = {}
for lab, M in want:
    c = cls_of(cases[lab][1])
    words = [seen[k] for k, cc in zip(keys, cls) if cc == c]
    for MM in (M,):
        r = subprocess.run(['systemd-run', '--user', '--scope', '-q', '-p', 'MemoryMax=1500M', '/data/fmc/tools/nissy-2.0.8/nissy', 'solve', 'light', '-M', str(MM), '-i'],
                           input='\n'.join(words) + '\n', capture_output=True, text=True, timeout=6000, env=dict(os.environ, NISSYDATA='/data/fmc/tools/nissy-data'))
        lines = r.stdout.split('\n')
        sols = [l for l in lines if re.search(r'\(\d+\)\s*$', l)]
        print(f'{lab} (FakeMMAP HT value {cases[lab][0]}): {len(words)} states; nissy solutions of <= {MM}: {len(sols)}; output lines {len(lines)}; e.g. {sols[:1]} / raw {lines[:2]}', flush=True)
