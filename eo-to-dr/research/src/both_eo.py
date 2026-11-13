#!/usr/bin/env python3
"""The cases with no edge out of place (xc0e), where the state has both EOs.

An EO-solved state (F/B EO) whose E-slice pieces are all in the E slice also has the R/L EO solved.  For such a state
the 'any turns' distance to DR on U/D (out/big/all_dr_eo0.u8) can be shorter than the distance keeping the F/B EO
(out/big/eo-fb_dr_eo0.u8) without any EO being given up: a DR that keeps the R/L EO instead.  This counts, per case,
the states where any turns are shorter, and how many of them have a DR of that length keeping the R/L EO.

The distance keeping the R/L EO is read from the same table through a quarter rotation of the cube about U/D: it
carries R/L to F/B, keeps every corner's twist and moves the corner places round.  Checks: the rotation carries each
corner's three places onto the next corner's in the same order; the any-turn distance is the same before and after it
for every one of the 2,187 states; and a search of its own with every turn but the R/L quarter turns gives the same
R/L-kept distance as the rotated lookup for all 2,187.
Writes out/both_eo.json.   usage: both_eo.py"""
import json, os, sys, collections
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import sticker                                     # puts is-dr-xs-worth-it/research/src on the path
import cube, coords

OUT = os.path.join(HERE, '..', 'out')
keep = np.fromfile(os.path.join(OUT, 'big', 'eo-fb_dr_eo0.u8'), dtype=np.uint8)
anyt = np.fromfile(os.path.join(OUT, 'big', 'all_dr_eo0.u8'), dtype=np.uint8)
NSL = 495
assert len(keep) == len(anyt) == 2187 * NSL
sl0 = coords.coords(cube.SOLVED)[2]                 # the E-slice pieces in the E slice
assert keep[sl0] == 0 and anyt[sl0] == 0
# the quarter rotation about U/D on the corner places
y = cube.MOVES['y']
perm = []
for i in range(8):
    j = next(j for j in range(8) if coords.CF[j][0] == y[coords.CF[i][0]])
    assert [y[p] for p in coords.CF[i]] == coords.CF[j], 'the rotation keeps the order of a corner\'s places'
    perm.append(j)
assert sorted(perm) == list(range(8))
def twists(co):
    t = [(co // 3 ** i) % 3 for i in range(7)]
    return t + [(-sum(t)) % 3]
def rotated(co):
    t = twists(co); u = [0] * 8
    for i in range(8):
        u[perm[i]] = t[i]
    return sum(u[i] * 3 ** i for i in range(7))
# the rotation is a symmetry of the any-turn distance, and permutes the F/B-kept distances
for co in range(2187):
    assert anyt[rotated(co) * NSL + sl0] == anyt[co * NSL + sl0], co
assert sorted(keep[co * NSL + sl0] for co in range(2187)) == sorted(keep[rotated(co) * NSL + sl0] for co in range(2187))
# and it really is the distance keeping the R/L EO: a search of its own, from DR with every turn but R, R', L, L',
# over the coordinates (co, F/B eo, sl), set against the rotated lookup for all 2,187 states
co_t, eo_t, sl_t = (np.array(t, dtype=np.int64) for t in coords.tables())
moves = [m for m, nm in enumerate(coords.NAMES) if not (nm[0] in 'RL' and not nm.endswith('2'))]
assert len(moves) == 14
key = lambda c, e, s: (c * 2048 + e) * NSL + s
dist = {}; front = np.array([key(0, 0, sl0)], dtype=np.int64); seen = front.copy(); d = 0
rl_kept = {}
while len(front):
    c, e, s = front // (2048 * NSL), (front // NSL) % 2048, front % NSL
    hit = (e == 0) & (s == sl0)
    for cc in c[hit].tolist():
        rl_kept[cc] = d
    nxt = np.unique(np.concatenate([key(co_t[c, m], eo_t[e, m], sl_t[s, m]) for m in moves]))
    nxt = nxt[~np.isin(nxt, seen, assume_unique=True)]
    seen = np.union1d(seen, nxt); front = nxt; d += 1
assert len(seen) == len(keep), len(seen)             # the R/L-EO-solved states, as many as the F/B ones
assert len(rl_kept) == 2187
for co in range(2187):
    assert rl_kept[co] == keep[rotated(co) * NSL + sl0], co
tab = collections.OrderedDict()
tot = {'states': 0, 'shorter_with_any_turns': 0, 'of_which_a_dr_keeping_the_other_eo_is_as_short': 0}
for co in range(2187):
    c = sum(1 for x in twists(co) if x)
    if c == 0:
        continue
    k, a, o = int(keep[co * NSL + sl0]), int(anyt[co * NSL + sl0]), int(keep[rotated(co) * NSL + sl0])
    assert a <= min(k, o)
    r = tab.setdefault(f'{c}c0e', {'states': 0, 'shorter_with_any_turns': 0, 'of_which_a_dr_keeping_the_other_eo_is_as_short': 0})
    for d in (r, tot):
        d['states'] += 1
        if a < k:
            d['shorter_with_any_turns'] += 1
            if o == a:
                d['of_which_a_dr_keeping_the_other_eo_is_as_short'] += 1
allshorter = int((anyt < keep).sum())
out = {'cases': dict(sorted(tab.items())), 'all_0e_cases': tot,
       'eo_solved_states': int(len(keep)), 'states_shorter_with_any_turns': allshorter,
       'states_shorter_with_any_turns_outside_0e_cases': allshorter - tot['shorter_with_any_turns']}
json.dump(out, open(os.path.join(OUT, 'both_eo.json'), 'w'), indent=1)
for k, r in out['cases'].items():
    print(k, r)
print('all xc0e:', tot)
print(f"all EO-solved states: {allshorter} of {len(keep)} are shorter with any turns; {out['states_shorter_with_any_turns_outside_0e_cases']} of them outside the xc0e cases")
