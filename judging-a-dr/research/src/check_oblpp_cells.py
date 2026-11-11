#!/usr/bin/env python3
"""Independent test of the four classes where FakeMMAP's "OBL++" sheet (KB doc 428) lists 8 and our all-move search says 9.
For each class we list all 3,072 HTR states in it (breadth-first search over the 663,552 HTR states) and ask nissy's
optimal solver for a solution of at most 8 face turns.  If none of the 3,072 has one, the class value is at least 9."""
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
# the four disputed labels -> class ids, via FakeMMAP's own example scrambles
want = {}
for line in open('/data/fmc/assets/attachments/1546077758189477989_0_message.txt'):
    m = re.match(r'^(\S+ \S) F-(\S) R-(\S)\s+(even|odd) E-parity: (\d+) Example scramble: ?(.*)$', line.rstrip('\n'))
    if not m: continue
    lab = f'{m.group(1)} F-{m.group(2)} R-{m.group(3)} {m.group(4)}'
    if lab in ('D-D + F-H R-H even', 'D-D - F-H R-H even', 'R-V + F-D R-H even', 'R-V + F-D R-D odd'):
        want[seen_class := cls[keys.index(fc_state := None) if False else 0]] = None  # placeholder, replaced below
        a = fc.to_dr_arrays(fc.state_after(m.group(6)))
        o = subprocess.run(Q, input=' '.join(map(str, a[0] + a[1] + a[2])) + '\n', capture_output=True, text=True, env=dict(os.environ, DRQ_NOEXACT='1')).stdout
        want[int(re.search(r'kfclass=(\d+)', o).group(1))] = lab
want = {c: l for c, l in want.items() if l}
for c, lab in want.items():
    words = [seen[k] for k, cc in zip(keys, cls) if cc == c]
    r = subprocess.run(['systemd-run', '--user', '--scope', '-q', '-p', 'MemoryMax=1500M', '/data/fmc/tools/nissy-2.0.8/nissy', 'solve', 'light', '-M', '8', '-i'],
                       input='\n'.join(words) + '\n', capture_output=True, text=True, timeout=3000, env=dict(os.environ, NISSYDATA='/data/fmc/tools/nissy-data'))
    sols = [l for l in r.stdout.split('\n') if re.search(r'\(\d+\)\s*$', l)]
    print(f'{lab}: {len(words)} states in the class; nissy found a solution of <= 8 face turns for {len(sols)} of them', flush=True)
    for l in sols[:2]: print('    e.g.', l)
