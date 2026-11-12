#!/usr/bin/env python3
"""Errata B3: 8 bad edges on F/B, the four good ones the E-slice pieces, U/D colours on the F/B faces of every corner.

Over the 70 such layouts (patterns.ROWS): how the four flipped edges split by the slice they belong to (their home
slice) and by the slice they sit in, and the fewest turns to a real DR.  For the witness of out/witness.json
('eight_bad_split'): the same read off the stickers, and nissy's shortest DR (any axis, any moves) on the scramble
and on its inverse.  Writes out/witness_split.json.  Needs nissy on the PATH (source /data/fmc/env.sh)."""
import json, collections, subprocess, pickle
import cube, fe, coords, export_cubie, patterns
from fecosets import path
O = '/data/fmc/is-dr-xs-worth-it/research/out/'
d = pickle.load(open(O + 'fecosets.pkl', 'rb')); dmv, bm = d['dmv'], d['bm']
KIND = ['E' if p[1] == 0 else 'M' if p[0] == 0 else 'S' for p in coords.EDGES]     # home slice of the piece / of the place
home = {k: [i for i in range(12) if KIND[i] == k] for k in 'EMS'}
base = cube.do(cube.SOLVED, "R L'"); cp, ct, _, _ = export_cubie.cubie(base)
par = lambda p: sum(1 for i in range(len(p)) for j in range(i + 1, len(p)) if p[i] > p[j]) % 2
LAYER = [p for p in fe.EDGES if p[2] != 0]
def split(c): v = sorted(c.values(), reverse=True) + [0]; return f'{v[0]}-{v[1]}'
def read(s):
    """(home split, place split, places, fewest turns to DR, a shortest fix) of a state of this kind."""
    g = fe.look(s, 1, 2); assert g is not None and sum(g[0]) == 4
    bad = coords.flips(s); ep = export_cubie.cubie(s)[2]
    assert collections.Counter(KIND[ep[i]] for i in range(12) if bad[i]) == {'M': 4, 'S': 4}
    idx = [coords.EDGES.index(p) for p, b in zip(LAYER, g[0]) if b]
    sig = (2,) + g
    return (split(collections.Counter(KIND[ep[i]] for i in idx)), split(collections.Counter(KIND[i] for i in idx)),
            sorted(export_cubie.name_of(coords.EDGES[i]) for i in idx), dmv[(sig, 3)], path(bm, sig))
rows = collections.Counter()
for arr in patterns.ROWS:
    if not (arr['f'] == 'FB' and arr['pat']['FB'] == (0, 4, 4) and arr['slices'] == 1): continue
    for swap in (False, True):
        it = {k: iter(home[k]) for k in 'EMS'}; ep = [next(it[arr['piece'][i]]) for i in range(12)]
        if swap:
            a, b = [i for i in range(12) if KIND[ep[i]] == 'S'][:2]; ep[a], ep[b] = ep[b], ep[a]
        if par(cp) == par(ep): break
    s = coords.make(cp, ct, ep, [arr['ef'][i] for i in range(12)])
    h, p, _, t, fix = read(s); rows[(h, p, t, fix)] += 1
assert len({r[2] for r in rows}) == 1 and len({r[3] for r in rows}) == 1, 'not every layout has the same fix'
W = json.load(open(O + 'witness.json'))['eight_bad_split']
s = cube.do(cube.SOLVED, cube.parse(W['scramble'])); h, p, places, t, fix = read(s)
ep = export_cubie.cubie(s)[2]; LBL = {p: export_cubie.name_of(p) for p in coords.EDGES}
pieces = sorted((LBL[coords.EDGES[ep[coords.EDGES.index(q)]]], KIND[ep[coords.EDGES.index(q)]]) for q, b in zip(LAYER, fe.look(s, 1, 2)[0]) if b)
def nissy(*a): return subprocess.run(['nissy'] + list(a), capture_output=True, text=True, check=True).stdout.strip()
inv = nissy('invert', W['scramble'])
dn, di = nissy('solve', 'dr', W['scramble']), nissy('solve', 'dr', inv)
ln = lambda x: int(x.rsplit('(', 1)[1].rstrip(')'))
OUT = dict(layouts={f'{a}|{b}|{c}|{e}': v for (a, b, c, e), v in sorted(rows.items())},
           home_split={k: sum(v for (a, *_), v in rows.items() if a == k) for k in ('2-2', '3-1', '4-0')},
           place_split={k: sum(v for (_, b, *_), v in rows.items() if b == k) for k in ('2-2', '3-1', '4-0')},
           turns={str(k): sum(v for (_, _, c, _), v in rows.items() if c == k) for k in sorted({r[2] for r in rows})},
           witness=dict(scramble=W['scramble'], home_split=h, place_split=p, places=places, pieces=pieces, turns=t, fix=fix,
                        nissy_dr=dn, nissy_dr_len=ln(dn), nissy_dr_inverse=di, nissy_dr_inverse_len=ln(di)))
json.dump(OUT, open(O + 'witness_split.json', 'w'), indent=1)
print(json.dumps(OUT, indent=1))
