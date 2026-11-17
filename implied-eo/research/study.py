#!/usr/bin/env python3
"""The 691 sets by type, with readable sequences, the per-side dictionary, test scrambles, and how often a
uniformly random scramble has one.  -> out/study.json"""
import sys, os, json, random, collections
import numpy as np
from eomodel import *
import census as E
HERE = os.path.dirname(os.path.abspath(__file__))
D = E.DIST
multi = json.load(open(os.path.join(HERE, 'out', 'classes5.json')))['multi']
def nice(seqs):
    def cost(s): return (sum(m.endswith("'") for m in s), sum(m.endswith('2') for m in s), [FACES.index(m[0]) for m in s], s)
    return min(seqs, key=cost)
SOL = {}
def sol(w, ax):
    if (w, ax) not in SOL:
        s = E.solutions(w, ax); SOL[(w, ax)] = (' '.join(nice(s)), len(s))
    return SOL[(w, ax)]
def eo_text(a, u, v):
    n, i = sol(v, a)[0], sol(u, a)[0]
    return (n + (' ' if n and i else '') + (f'({i})' if i else '')) or '(EO skip)'
def side_lengths(p): a, u, v, _ = p; return (D[a][v], D[a][u])
def typ(pres):
    L = sorted(p[3] for p in pres)
    sides = sorted(sorted(side_lengths(p)) for p in pres)
    if L == [4, 4, 4]: return 'T1'
    if L == [3, 5, 5]: return 'T2'
    if L == [3, 5]: return 'P1'
    if L == [4, 4]: return 'P3' if [0, 4] in sides else 'P2'
    if L == [5, 5]: return 'P4' if [2, 3] in sides and sides == [[2, 3], [2, 3]] else 'P5'
    raise ValueError(L)
sets = []
for pres in multi:
    pres = sorted(pres, key=lambda q: (q[3], -q[0]))
    sets.append({'type': typ(pres), 'pres': pres, 'text': [f'{eo_text(a, u, v)} on {AXIS_NAME[a]}' for a, u, v, _ in pres],
                 'len': [p[3] for p in pres], 'key': list(E.to_fb(*pres[0][:3]))})
cnt = collections.Counter(s['type'] for s in sets)
print(cnt, sum(cnt.values()))
# P4 really is (3,3)+(2,2) and P5 (1,3)+(4,2):
for s in sets:
    sd = sorted(tuple(sorted(side_lengths(p))) for p in s['pres'])
    assert (s['type'] != 'P4' or sd == [(2, 3), (2, 3)]) and (s['type'] != 'P5' or sd == [(1, 4), (2, 3)]), (s['type'], sd)

# the per-side dictionary F/B <-> R/L: cases whose partner (8 edges off the E slice toggled) is also short
T8 = FULL ^ SLICE[1]
dic = collections.defaultdict(list)
for w in D[2]:
    la, lb = D[2][w], D[0][w ^ T8]
    if la + lb <= 6 and max(la, lb) <= 4: dic[(la, lb)].append((sol(w, 2)[0], sol(w ^ T8, 0)[0], mask_names(w), mask_names(w ^ T8)))
for k in sorted(dic):
    print(k, len(dic[k]))
    for x in sorted(dic[k])[:30]: print('    ', x[0] or '-', ' <-> ', x[1] or '-')

# a test scramble per set: inverse part, then moves that keep the EO of the first presentation's axis, then the
# normal part undone; checked by turning the stickers
rng = random.Random(7)
KEEP = {ax: [m for m in MOVE_NAMES if AX[m[0]][0] != ax or m.endswith('2')] for ax in range(3)}
def cancel(seq):
    out = []
    for m in seq:
        if out and out[-1][0] == m[0]:
            t = ({'': 1, '2': 2, "'": 3}[out[-1][1:]] + {'': 1, '2': 2, "'": 3}[m[1:]]) % 4
            out.pop()
            if t: out.append(m[0] + {1: '', 2: '2', 3: "'"}[t])
        else: out.append(m)
    return out
def holds(scr, a, n, i):
    T = compose(compose(apply(inv_seq(parse(i))), apply(scr)), apply(parse(n)))
    return eo_solved(T, a)
for s in sets:
    a, u, v, _ = s['pres'][0]
    while True:
        mid = []
        while len(mid) < 16:
            m = rng.choice(KEEP[a])
            if mid and AX[mid[-1][0]][0] == AX[m[0]][0]: continue
            mid.append(m)
        scr = cancel(parse(sol(u, a)[0]) + mid + inv_seq(parse(sol(v, a)[0])))
        if len(scr) >= 17: break
    for b, u2, v2, _ in s['pres']: assert holds(scr, b, sol(v2, b)[0], sol(u2, b)[0]), s['text']
    s['scramble'] = ' '.join(scr)
print('test scrambles: every EO of every set checked by turning the stickers')

# how often: uniformly random edge states (any permutation, any flips with an even count)
N = int(sys.argv[1]) if len(sys.argv) > 1 else 2_000_000
nrng = np.random.default_rng(11)
U = np.array([s['key'][0] for s in sets], dtype=np.int32); V = np.array([s['key'][1] for s in sets], dtype=np.int32)
tix = {t: np.array([i for i, s in enumerate(sets) if s['type'] == t]) for t in cnt}
short = np.array([i for i, s in enumerate(sets) if max(s['len']) <= 4])
hit = collections.Counter(); nsets = collections.Counter(); done = 0
CH = 20000
while done < N:
    n = min(CH, N - done)
    perm = np.argsort(nrng.random((n, 12)), axis=1)                     # perm[s, h] = place of the edge with home h
    bits = nrng.integers(0, 2, (n, 12)); bits[:, 11] = bits[:, :11].sum(1) % 2
    B = (bits << np.arange(12)).sum(1).astype(np.int32)                 # bad on F/B, by home
    A = B[:, None] ^ U[None, :]                                         # (state, set): edges whose place must be in V
    W = np.zeros_like(A)
    for h in range(12): W |= ((A >> h) & 1) << perm[:, h][:, None]
    ok = W == V[None, :]
    anyhit = ok.any(1); hit['any'] += int(anyhit.sum()); nsets['total'] += int(ok.sum())
    hit['le4'] += int(ok[:, short].any(1).sum())
    for t, ix in tix.items(): hit[t] += int(ok[:, ix].any(1).sum())
    k = ok.sum(1)
    for j in range(1, 6): hit[f'n{j}'] += int((k == j).sum())
    done += n
freq = {k: (v / N, 1.96 * (v / N * (1 - v / N) / N) ** 0.5) for k, v in hit.items()}
for k, (p, e) in sorted(freq.items()): print(f'{k}: {100*p:.3f}% ± {100*e:.3f}')
print('mean sets per scramble', nsets['total'] / N, 'expected', len(sets) / 2048)
json.dump({'sets': sets, 'counts': cnt, 'freq': freq, 'n_sample': N,
           'dict': {f'{k[0]}-{k[1]}': sorted(v) for k, v in dic.items()}}, open(os.path.join(HERE, 'out', 'study.json'), 'w'), indent=0)
