#!/usr/bin/env python3
"""The sets of scrambles with two or more EOs of at most MAXLEN moves, up to the 48 symmetries of the cube and
swapping normal with inverse.  -> out/families{MAXLEN}.json"""
import sys, os, json, itertools, collections
from eomodel import *
import census as E
HERE = os.path.dirname(os.path.abspath(__file__))
MAXLEN = E.MAXLEN
# the 48 symmetries: signed permutations of the coordinates
SYMS = []
for perm in itertools.permutations(range(3)):
    for signs in itertools.product((1, -1), repeat=3):
        pp = [POS[tuple(signs[k] * c[perm[k]] for k in range(3))] for c in CUBIES]   # new coordinate k = sign * old coordinate perm[k]
        axmap = {perm[k]: k for k in range(3)}
        SYMS.append((pp, axmap))
def mperm(w, pp):
    r = 0
    for p in range(12):
        if w >> p & 1: r |= 1 << pp[p]
    return r
for pp, axmap in SYMS:        # a symmetry carries the EO cases of an axis to those of its image, same lengths
    for ax in range(3):
        for w in list(E.DIST[ax])[::37]: assert E.DIST[axmap[ax]][mperm(w, pp)] == E.DIST[ax][w]
multi = json.load(open(os.path.join(HERE, 'out', f'classes{MAXLEN}.json')))['multi']
def canon(pres):
    best = None
    for pp, axmap in SYMS:
        for swap in (0, 1):
            t = tuple(sorted((axmap[a], mperm(v if swap else u, pp), mperm(u if swap else v, pp)) for a, u, v, _ in pres))
            if best is None or t < best: best = t
    return best
fam = collections.defaultdict(list)
for pres in multi: fam[canon(pres)].append(pres)
def seqs(w, ax, k=3):
    s = E.solutions(w, ax)
    return len(s), [' '.join(x) for x in s[:k]]
def show(a, u, v):
    nv, sv = seqs(v, a); nu, su = seqs(u, a)
    return f"{AXIS_NAME[a]}: {sv[0] or '-'} ({su[0] or '-'})   [{E.DIST[a][v]}+{E.DIST[a][u]}; normal case {mask_names(v)} | inverse case {mask_names(u)}]"
out = []
print(f'{len(multi)} sets of scrambles, {len(fam)} families up to symmetry and inversion')
def rep_key(pres):
    # prefer: the shortest EO on F/B, normal part not longer than inverse part... just a stable choice
    p = sorted(pres, key=lambda q: (q[3], q[0] != 2))
    return (p[0][0] != 2, p[0][3], E.DIST[p[0][0]][p[0][1]] , p)
for key, members in sorted(fam.items(), key=lambda kv: (len(kv[1][0]), sorted(q[3] for q in kv[1][0]), -len(kv[1]))):
    rep = min(members, key=rep_key)
    rep = sorted(rep, key=lambda q: (q[3], q[0] != 2))
    print(f'\nfamily of {len(members)} sets; lengths {[q[3] for q in rep]}')
    for a, u, v, l in rep: print('   ', show(a, u, v))
    out.append({'size': len(members), 'rep': rep, 'members': members})
json.dump(out, open(os.path.join(HERE, 'out', f'families{MAXLEN}.json'), 'w'))
