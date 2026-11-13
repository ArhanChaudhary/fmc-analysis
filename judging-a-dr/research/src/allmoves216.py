#!/usr/bin/env python3
"""Exact optimal length, with ALL 18 face turns allowed (HTM), of the 216 NISS@1qt classes (FakeMMAP / Rodney Kinney).

Method (meet in the middle, complete up to 10 moves): every sequence of <= 10 face turns is a product a·b of two
sequences of <= 5 turns.  If a·b is an HTR state then a and b^-1 show the same "axis colouring" (each sticker replaced
by its axis U/D, R/L or F/B) and the product passes an exact HTR test.  So we list all 624,124 canonical sequences of
length <= 5 twice, join them on that key, and keep the shortest product for every HTR state reached.
Since the DR-move table never exceeds 10 on these classes, this decides every class."""
import sys, os, subprocess, collections, numpy as np
sys.path.insert(0, '/data/fmc/judging-a-dr/research/tool'); import fmccube as fc

# ---- facelet model with 48 stickers
locs = sorted(k for k in fc.solved() if sum(abs(v) for v in k[0]) > 1)
idx = {k: i for i, k in enumerate(locs)}
def move_perm(base, times):
    f, axis, layers = fc.ROT[base]
    perm = np.arange(48)
    for _ in range(times):
        step = np.arange(48)
        for (p, n), i in idx.items():
            if p[axis] in layers: step[idx[(f(p), f(n))]] = i      # sticker at i goes to f(i): new[f(i)] = old[i]
        perm = perm[step]
    return perm
FACES = 'UDRLFB'
PERM = {(f, t): move_perm(f, t) for f in FACES for t in (1, 2, 3)}
axis_of = np.array([[i for i in range(3) if n[i]][0] for (p, n) in locs], dtype=np.uint8)

def levels(depth):
    states = [np.arange(48, dtype=np.uint8)[None, :]]; last = [np.array([-1], dtype=np.int8)]
    global PARENT, MOVE
    par, mov, offset = [np.array([-1])], [np.array([-1])], 0
    for d in range(depth):
        S, L = states[-1], last[-1]; ns, nl, np_, nm = [], [], [], []
        for fi, f in enumerate(FACES):
            ok = (L != fi) & ~((fi % 2 == 0) & (L == fi + 1))     # no repeat face; opposite faces only in order U D / R L / F B
            for t in (1, 2, 3):
                ns.append(S[ok][:, PERM[(f, t)]]); nl.append(np.full(ok.sum(), fi, dtype=np.int8))
                np_.append(np.nonzero(ok)[0] + offset); nm.append(np.full(ok.sum(), fi * 3 + t - 1))
        offset += len(S)
        states.append(np.concatenate(ns)); last.append(np.concatenate(nl)); par.append(np.concatenate(np_)); mov.append(np.concatenate(nm))
    PARENT, MOVE = np.concatenate(par), np.concatenate(mov)
    return states
def word(i):
    out = []
    while PARENT[i] >= 0:
        m = int(MOVE[i]); out.append(FACES[m // 3] + ['', '2', "'"][m % 3]); i = int(PARENT[i])
    return ' '.join(reversed(out))
D = int(sys.argv[1]) if len(sys.argv) > 1 else 5
lv = levels(D)
A = np.concatenate(lv); LEN = np.concatenate([np.full(len(s), i, dtype=np.uint8) for i, s in enumerate(lv)])
print('sequences of length <=', D, ':', len(A), file=sys.stderr)
INV = np.empty_like(A); INV[np.arange(len(A))[:, None], A] = np.arange(48, dtype=np.uint8)[None, :]
# a·b is in H  <=>  b^-1 = h^-1·a for some h in H  =>  a and b^-1 have the same axis colouring
# (the colouring of a state x is unchanged when x is preceded by half turns, i.e. on the coset H·x).
keyA = axis_of[A]              # key of a
keyB = axis_of[INV]            # key of b^-1
def pack(K): return [r.tobytes() for r in K]
bucket = collections.defaultdict(list)
for i, k in enumerate(pack(keyA)): bucket[k].append(i)
bB = collections.defaultdict(list)
for i, k in enumerate(pack(keyB)): bB[k].append(i)
print('distinct keys a^-1:', len(bucket), ' b:', len(bB), ' common:', len(set(bucket) & set(bB)), file=sys.stderr)

# ---- facelets -> DR arrays (vectorised)
def sticker(p, n): return idx[(tuple(p), tuple(n))]
cor_loc = np.array([sticker(p, (0, p[1], 0)) for p in fc.CORNERS]); ude_loc = np.array([sticker(p, (0, p[1], 0)) for p in fc.UD_EDGES]); ee_loc = np.array([sticker(p, (0, 0, p[2])) for p in fc.E_EDGES])
cor_of = np.full(48, 255, dtype=np.uint8); ude_of = np.full(48, 255, dtype=np.uint8); ee_of = np.full(48, 255, dtype=np.uint8)
for i, l in enumerate(cor_loc): cor_of[l] = i
for i, l in enumerate(ude_loc): ude_of[l] = i
for i, l in enumerate(ee_loc): ee_of[l] = i

best = {}; wit = {}
pairs = 0
for k, ia in bucket.items():
    ib = bB.get(k)
    if not ib: continue
    ia = np.array(ia); ib = np.array(ib)
    for s in range(0, len(ia), 2000):
        a = ia[s:s + 2000]
        P = A[a][:, A[ib]]                       # (na, nb, 48): a then b
        L = (LEN[a][:, None] + LEN[ib][None, :]).reshape(-1)
        P = P.reshape(-1, 48); pairs += len(P)
        c = cor_of[P[:, cor_loc]]; e = ude_of[P[:, ude_loc]]; se = ee_of[P[:, ee_loc]]
        ok = (c != 255).all(1) & (e != 255).all(1) & (se != 255).all(1)
        arr = np.concatenate([c[ok], e[ok], se[ok]], axis=1); Lk = L[ok]
        order = np.argsort(Lk, kind='stable'); arr = arr[order]; Lk = Lk[order]
        _, first = np.unique(arr.view([('', arr.dtype)] * 20), return_index=True)
        flat = np.nonzero(ok)[0][order]
        for j in first:
            key = arr[j].tobytes()
            if key not in best or Lk[j] < best[key]:
                best[key] = int(Lk[j]); wit[key] = (int(a[flat[j] // len(ib)]), int(ib[flat[j] % len(ib)]))
print('pairs joined:', pairs, ' DR-shaped products:', len(best), file=sys.stderr)
keys = list(best)
inp = '\n'.join(' '.join(map(str, np.frombuffer(k, dtype=np.uint8))) for k in keys) + '\n'
out = subprocess.run(['/data/fmc/judging-a-dr/research/drtools/target/release/drtools', 'query', '/data/fmc/judging-a-dr/research/data/drbfs', '/data/fmc/judging-a-dr/research/data/tables'], input=inp, capture_output=True, text=True, env=dict(os.environ, DRQ_NOEXACT='1')).stdout.strip().split('\n')
cls = {}; witc = {}       # KF class -> (all-move best, DR-move table); a shortest sequence producing a state of the class
nhtr = 0
for k, line in zip(keys, out):
    kv = dict(t.split('=', 1) for t in line.split(' ') if '=' in t)
    if 'htr_normal' not in kv or kv['htr_normal'] != '0': continue
    nhtr += 1
    c = int(kv['kfclass']); t = int(kv['KF'].split('/')[0])
    cur = cls.get(c, (99, t))
    if best[k] < cur[0]: witc[c] = word(wit[k][0]) + ' ' + word(wit[k][1])
    cls[c] = (min(cur[0], best[k]), t)
print('HTR states with an all-move solution of <= %d moves: %d ; classes touched: %d' % (2 * D, nhtr, len(cls)), file=sys.stderr)
import json
json.dump({str(c): v for c, v in cls.items()}, open('/data/fmc/judging-a-dr/research/out/allmoves216.json', 'w'))
json.dump({str(c): w for c, w in witc.items()}, open('/data/fmc/judging-a-dr/research/out/allmoves216_witness.json', 'w'))
diff = collections.Counter(v[1] - min(v) for v in cls.values())
print('classes by (DR-move table) - (all-move optimum):', dict(sorted(diff.items())))
