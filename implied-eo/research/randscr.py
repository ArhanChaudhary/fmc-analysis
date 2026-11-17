#!/usr/bin/env python3
"""Ordinary scrambles for the examples: random-move scrambles of 25 moves, searched until every one of the 691 sets
(and the few other EOs the write-up shows) has one.  Each scramble is then checked by turning the stickers.
-> out/scrambles.json"""
import os, json, re
import numpy as np
from eomodel import *
import census as E
HERE = os.path.dirname(os.path.abspath(__file__))
S = json.load(open(os.path.join(HERE, 'out', 'study.json'))); BY = json.load(open(os.path.join(HERE, 'out', 'beyond.json')))
def parse_eo(txt):
    m = re.match(r'^\s*([^()]*?)\s*(?:\(([^()]*)\))?\s*([^()]*?)\s*$', txt)
    normal = (m.group(1) + ' ' + m.group(3)).split(); inverse = (m.group(2) or '').split()
    axes = {AX[s[-1][0]][0] for s in (normal, inverse) if s}; assert len(axes) == 1, txt
    return axes.pop(), normal, inverse
def key(txt): a, n, i = parse_eo(txt); return E.to_fb(a, E.case_of(i, a), E.case_of(n, a))
def holds(scr, txt):
    a, n, i = parse_eo(txt); return eo_solved(compose(compose(apply(inv_seq(i)), apply(scr)), apply(n)), a)
LG = json.load(open(os.path.join(HERE, 'out', 'longer.json')))
EXTRA = ['F (B)', BY['six']['X'], BY['seven']['X'], 'F B (F R2 B)', 'B (F U2 B)', LG['pointed']['Y'], LG['ex_slice']['Y'], LG['ex_super']['Y'], LG['ex_xf']['Y']]
EXTRA += [r['Y'] for r in LG['probe'] if r['Y'] not in EXTRA]
keys = [tuple(s['key']) for s in S['sets']] + [key(t) for t in EXTRA]
U = np.array([k[0] for k in keys], dtype=np.int64); V = np.array([k[1] for k in keys], dtype=np.int64)
T = np.array([MOVES[m] for m in MOVE_NAMES]); FACE_AX = np.array([AX[f][0] for f in FACES])
cub = np.array([POS[FACELETS[j][0]] for j in range(24)]); iskey = np.array(KEY[2])
rng = np.random.default_rng(2026)
found = {}; WANT = 3
while len(found) < len(keys) or min(len(v) for v in found.values()) < WANT:
    n = 20000
    faces = np.zeros((n, 25), dtype=np.int64)
    for t in range(25):
        f = rng.integers(0, 6, n)
        while True:
            bad = np.zeros(n, dtype=bool)
            if t >= 1: bad |= f == faces[:, t - 1]
            if t >= 2: bad |= (FACE_AX[f] == FACE_AX[faces[:, t - 1]]) & (FACE_AX[f] == FACE_AX[faces[:, t - 2]])
            if not bad.any(): break
            f[bad] = rng.integers(0, 6, int(bad.sum()))
        faces[:, t] = f
    mv = faces * 3 + rng.integers(0, 3, (n, 25))
    st = np.tile(np.arange(24), (n, 1))
    for t in range(25): st = T[mv[:, t][:, None], st]
    j = st[:, KEYF[2]]                                   # where each edge's key sticker is
    perm = cub[j]; B = ((~iskey[j]).astype(np.int64) << np.arange(12)).sum(1)
    A = B[:, None] ^ U[None, :]; W = np.zeros_like(A)
    for h in range(12): W |= ((A >> h) & 1) << perm[:, h][:, None]
    A2 = A ^ FULL; W2 = np.zeros_like(A)                  # the complemented form of the same set
    for h in range(12): W2 |= ((A2 >> h) & 1) << perm[:, h][:, None]
    ok = (W == V[None, :]) | (W2 == (V ^ FULL)[None, :])
    for s_, k_ in zip(*np.nonzero(ok)):
        lst = found.setdefault(int(k_), [])
        if len(lst) < WANT: lst.append(' '.join(MOVE_NAMES[x] for x in mv[s_]))
out = {'sets': [], 'extra': {}}
for i, s in enumerate(S['sets']):
    scr = found[i][0]
    for t in s['text']: assert holds(scr.split(), t.rsplit(' on ', 1)[0]), (scr, t)
    out['sets'].append(scr)
for t, i in zip(EXTRA, range(len(S['sets']), len(keys))):
    for scr in found[i]: assert holds(scr.split(), t)
    out['extra'][t] = found[i]
json.dump(out, open(os.path.join(HERE, 'out', 'scrambles.json'), 'w'), indent=0)
print('random scrambles found for', len(out['sets']), 'sets and', len(out['extra']), 'other EOs; all checked')
