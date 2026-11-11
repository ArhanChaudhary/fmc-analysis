#!/usr/bin/env python3
"""How many turns to a slice EO for one given slice: exact over all 495 x 16 = 7,920 ways its four pieces can be
placed and oriented (all equally likely).  A slice EO = the four pieces all oriented or all misoriented for one of
the three axes.  Also for one given axis only, and for "all oriented" only."""
import collections, itertools
import coords
co, eo, sl = coords.tables()
KIND = ['E' if p[1] == 0 else 'M' if p[0] == 0 else 'S' for p in coords.EDGES]
def bits_for(e, comb, axis):
    out = []
    for i in comb:
        b = (e >> i) & 1 if i < 11 else bin(e & 2047).count('1') & 1
        if axis == 'UD': b ^= KIND[i] == 'M'
        if axis == 'RL': b ^= (KIND[i] == 'E') ^ 1
        out.append(int(b))
    return out
def canon(e, s):
    """Keep only the orientation bits at the slice pieces' places (bit 11 is carried by the parity of the rest: store 12 bits)."""
    comb = coords.COMB_LIST[s]; full = [(e >> i) & 1 for i in range(11)] + [bin(e & 2047).count('1') & 1]
    return tuple(full[i] for i in comb), s
def step(state, m):
    bits, s = state; comb = coords.COMB_LIST[s]
    full = [0] * 12
    for b, i in zip(bits, comb): full[i] = b
    # make the eo coordinate consistent (even number of flips) by using a non-slice place as scratch
    scratch = next(i for i in range(12) if i not in comb)
    full[scratch] = sum(full) & 1
    e = sum(full[i] << i for i in range(11))
    assert (sum(full[:11]) & 1) == full[11]
    return canon(eo[e][m], sl[s][m])
def dist(goal):
    states = [(bits, s) for s in range(495) for bits in itertools.product((0, 1), repeat=4)]
    d = {st: 0 for st in states if goal(st)}
    frontier = list(d)
    while frontier:
        nxt = []
        for st in frontier:
            for m in range(18):
                # moves are invertible and the move set is closed under inverses: search backwards = forwards
                t = step(st, m)
                if t not in d: d[t] = d[st] + 1; nxt.append(t)
        frontier = nxt
    assert len(d) == 7920
    return collections.Counter(d.values())
def uniform(st, axes, flavours):
    bits, s = st; comb = coords.COMB_LIST[s]
    full = [0] * 12
    for b, i in zip(bits, comb): full[i] = b
    e = sum(full[i] << i for i in range(11))
    for ax in axes:
        out = []
        for b, i in zip(bits, comb):
            if ax == 'UD': b ^= KIND[i] == 'M'
            if ax == 'RL': b ^= (KIND[i] == 'E') ^ 1
            out.append(int(b))
        if sum(out) in flavours: return True
    return False
import json
RES = {}
for name, axes, fl in (('any axis, oriented or misoriented', ('FB', 'UD', 'RL'), (0, 4)), ('any axis, oriented only', ('FB', 'UD', 'RL'), (0,)),
                       ('F/B only, oriented or misoriented', ('FB',), (0, 4)), ('F/B only, oriented', ('FB',), (0,)),
                       ('the slice\'s own axis (U/D) only, either', ('UD',), (0, 4))):
    c = dist(lambda st: uniform(st, axes, fl))
    print(f'{name:45s}', ' '.join(f'{k}: {v} ({100 * v / 7920:.1f}%)' for k, v in sorted(c.items())))
    RES[name] = dict(sorted(c.items()))
json.dump(RES, open('/data/fmc/is-dr-xs-worth-it/research/out/seo_dist.json', 'w'), indent=1)
