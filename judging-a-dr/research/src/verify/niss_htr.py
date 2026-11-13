#!/usr/bin/env python3
"""Shortest NISS DR->HTR of a DR state: min over premove words a (|a| <= 6) on the scramble and on its inverse of
|a| + shortest linear HTR of a.g (drtools' HTR table).  Cross-check of DRBound.Page.nissHTR."""
import sys, os, subprocess, re, numpy as np
sys.path.insert(0, '/data/fmc/judging-a-dr/research/tool'); import fmccube as fc
locs = sorted(k for k in fc.solved() if sum(abs(v) for v in k[0]) > 1); idx = {k: i for i, k in enumerate(locs)}
def move_perm(base, times):
    f, axis, layers = fc.ROT[base]; perm = np.arange(48)
    for _ in range(times):
        step = np.arange(48)
        for (p, n), i in idx.items():
            if p[axis] in layers: step[idx[(f(p), f(n))]] = i
        perm = perm[step]
    return perm
MOVES = [('U', 1), ('U', 2), ('U', 3), ('D', 1), ('D', 2), ('D', 3), ('R', 2), ('L', 2), ('F', 2), ('B', 2)]
NAME = ["U", "U2", "U'", "D", "D2", "D'", "R2", "L2", "F2", "B2"]
PERM = [move_perm(f, t) for f, t in MOVES]; FACE = [0, 0, 0, 1, 1, 1, 2, 3, 4, 5]
def seq_perm(seq):
    s = np.arange(48, dtype=np.uint8)
    for t in seq.split(): s = s[PERM[NAME.index(t)]]
    return s
def inv_seq(seq): return ' '.join({"U": "U'", "U'": "U", "D": "D'", "D'": "D"}.get(t, t) for t in reversed(seq.split()))
# all canonical premove words of length <= 6 (no two consecutive turns of one face; opposite faces in a fixed order)
levels = [(np.arange(48, dtype=np.uint8)[None, :], np.array([-1]))]
for d in range(6):
    S, L = levels[-1]; ns, nl = [], []
    for m in range(10):
        f = FACE[m]; ok = (L != f) & ~((f % 2 == 0) & (L == f + 1))
        ns.append(S[ok][:, PERM[m]]); nl.append(np.full(ok.sum(), f))
    levels.append((np.concatenate(ns), np.concatenate(nl)))
A = np.concatenate([s for s, _ in levels]); LEN = np.concatenate([np.full(len(s), i) for i, (s, _) in enumerate(levels)])
print('premove words:', len(A), file=sys.stderr)
def sticker(p, n): return idx[(tuple(p), tuple(n))]
cor_loc = np.array([sticker(p, (0, p[1], 0)) for p in fc.CORNERS]); ude_loc = np.array([sticker(p, (0, p[1], 0)) for p in fc.UD_EDGES]); ee_loc = np.array([sticker(p, (0, 0, p[2])) for p in fc.E_EDGES])
cor_of = np.full(48, 255, dtype=np.uint8); ude_of = np.full(48, 255, dtype=np.uint8); ee_of = np.full(48, 255, dtype=np.uint8)
for i, l in enumerate(cor_loc): cor_of[l] = i
for i, l in enumerate(ude_loc): ude_of[l] = i
for i, l in enumerate(ee_loc): ee_of[l] = i
Q = ['/data/fmc/judging-a-dr/research/drtools/target/release/drtools', 'query', '/data/fmc/judging-a-dr/research/data/drbfs', '/data/fmc/judging-a-dr/research/data/tables']
def side(scr):
    g = seq_perm(scr)
    X = A[:, g]                      # premoves a, then the scramble
    arr = np.concatenate([cor_of[X[:, cor_loc]], ude_of[X[:, ude_loc]], ee_of[X[:, ee_loc]]], axis=1)
    assert (arr != 255).all()
    inp = '\n'.join(' '.join(map(str, r)) for r in arr) + '\n'
    out = subprocess.run(Q, input=inp, capture_output=True, text=True, env=dict(os.environ, DRQ_NOEXACT='1')).stdout.strip().split('\n')
    h = np.array([int(re.search(r'htr_normal=(\d+)', l).group(1)) for l in out])
    tot = LEN + h; k = int(tot.argmin())
    return int(tot.min()), int(h[0]), int(LEN[k]), int(h[k])
for scr in sys.argv[1:]:
    a = side(scr); b = side(inv_seq(scr))
    print(f'{scr}: linear {a[1]} / {b[1]}; NISS {min(a[0], b[0])}  (premoves on normal side search: {a[0]} = {a[2]} + {a[3]}; on the inverse scramble: {b[0]} = {b[2]} + {b[3]})', flush=True)
