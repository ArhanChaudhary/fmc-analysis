#!/usr/bin/env python3
"""After the 4c4e card: the best single rows left to add, when the pair trace (pairs, where they sit, fake pairs) and
ARM are read on every case and the slower reads (corner case, side pairs, columns, corner layers, the edges out of the
slice) are priced by how many cases you have to make them on.

A row is: one pair count, up to two conditions on the fast reads (its footprint: the share of 4c4e where the slower
reads are then needed), up to two conditions on the slower reads, and a verdict that differs from the card's.
Its gain is the drop in cost per case.  Rows covering the same cases are listed once.  -> out/nextrows.json"""
import sys, os, json, itertools, hashlib
import numpy as np
from cards import *
from induce import atoms
HERE = os.path.dirname(os.path.abspath(__file__))
m = drm_mask(4, 4); idx = np.flatnonzero(m); n = idx.size; dd = d[idx]; w = weights()[dd]; bad = (dd > 6).astype(float)
g = (w - bad) / n                                   # gain of switching a case, per 4c4e case
cur = card_mask((4, 4))[idx]
FAST = ['arm', 'carm', 'earm', 'edges_paired', 'fake']
SLOW = ['cc', 'ccs', 'side', 'cols_bad', 'ud_split', 'hole_cfg']
p = np.asarray(F['pairs'])[idx]
fa = atoms(idx, FAST); sa = atoms(idx, SLOW)
S = np.stack([a[2] for a in sa]).astype(np.float32); sfam = [a[0] for a in sa]; snames = [a[1] for a in sa]
same = np.array([[sfam[i] == sfam[j] for j in range(len(sa))] for i in range(len(sa))])
MIN = 0.0008
res = {}
def add(gain, foot, pname, sname, verdict, cov):
    key = hashlib.md5(cov.tobytes()).hexdigest()
    r = dict(gain=float(gain), footprint=float(foot), fast=pname, slow=sname, verdict=verdict, cases=int(cov.sum()))
    if key not in res or (r['footprint'], len(pname) + len(sname)) < (res[key]['footprint'], len(res[key]['fast']) + len(res[key]['slow'])): res[key] = r
for pv in np.unique(p):
    prefixes = [(f'pairs={pv}', p == pv)] + [(f'pairs={pv} & {nm}', (p == pv) & msk) for _, nm, msk in fa]
    for (f1, n1, m1), (f2, n2, m2) in itertools.combinations(fa, 2):
        if f1 == f2 or ({f1, f2} & {'carm', 'earm'} and 'arm' in (f1, f2)): continue
        mm = (p == pv) & m1 & m2
        if mm.any(): prefixes.append((f'pairs={pv} & {n1} & {n2}', mm))
    for pname, pm in prefixes:
        foot = pm.mean()
        for verdict, gv in (('switch', np.where(pm & ~cur, g, 0.0)), ('skip', np.where(pm & cur, -g, 0.0))):
            tot = gv.sum(); nz = gv != 0
            if tot > MIN: add(tot, 0.0, pname, '', verdict, nz)
            gv32 = gv.astype(np.float32); single = S @ gv32
            for i in np.argsort(-single)[:3]:
                if single[i] > MIN and single[i] > tot + 0.0005: add(single[i], foot, pname, snames[i], verdict, (S[i] > 0) & nz)
            pair = (S * gv32) @ S.T; pair[same] = -1
            for f in np.argsort(-pair.ravel())[:3]:
                i, j = np.unravel_index(f, pair.shape)
                if i < j and pair[i, j] > MIN and pair[i, j] > max(single[i], single[j]) + 0.0005:
                    add(pair[i, j], foot, pname, snames[i] + ' & ' + snames[j], verdict, (S[i] > 0) & (S[j] > 0) & nz)
rows = sorted(res.values(), key=lambda r: -r['gain'])[:25]
json.dump({'card_loss': float(profile(m, card_mask((4, 4)))['loss']), 'rows': rows}, open(os.path.join(HERE, 'out', 'nextrows.json'), 'w'), indent=1)
for r in rows[:12]:
    print(f"{r['gain']:.4f}  slower reads on {100*r['footprint']:5.1f}%   {r['fast']} | {r['slow'] or '(fast reads only)'} -> {r['verdict']}  ({r['cases']} cases)")
