#!/usr/bin/env python3
"""Example scrambles for the claims in the write-up (out/witness.json), each checked on the sticker model.

  six         a DR-1s whose shortest fix to a real DR is 6 turns
  twelve_bad  all twelve edges bad on F/B, F/B colours on the U and D faces of every corner: a DR-2s, not a DR-1s
  layouts     every DR-1s layout with corners on F/B: flipped places, turns, a shortest fix, and a scramble that makes it"""
import json, pickle, subprocess, collections, itertools, random
import cube, fe, coords, export_cubie
from fecosets import path, C
R = '/data/fmc/judging-a-dr/research/'
d = pickle.load(open('/data/fmc/is-dr-xs-worth-it/research/out/fecosets.pkl', 'rb')); nbr, dsl, dmv, bm = d['nbr'], d['dsl'], d['dmv'], d['bm']
cn = [export_cubie.name_of(p) for p in coords.CORNERS]; en = [export_cubie.name_of(p) for p in coords.EDGES]
ci = [next(i for i, x in enumerate(cn) if set(x) == set(n)) for n in 'UFR UFL UBL UBR DFR DFL DBL DBR'.split()]
ei = [next(i for i, x in enumerate(en) if set(x) == set(n)) for n in 'UF UL UB UR DF DL DB DR'.split()]
si = [next(i for i, x in enumerate(en) if set(x) == set(n)) for n in 'FR FL BL BR'.split()]
def dr_numbers(s):
    cp, ct, ep, ef = export_cubie.cubie(s); assert not any(ct) and not any(ef)
    return [ci.index(cp[i]) for i in ci] + [ei.index(ep[i]) for i in ei] + [si.index(ep[i]) for i in si]
def optimal(states):
    inp = '\n'.join(' '.join(map(str, dr_numbers(s))) for s in states) + '\n'
    out = subprocess.run([R + 'drtools/target/release/drtools', 'query', R + 'data/drbfs', R + 'data/tables'], input=inp, capture_output=True, text=True).stdout
    return [int(l.split('exact=')[1].split()[0]) for l in out.strip().split('\n')]
DRM = ['U', 'U2', "U'", 'D', 'D2', "D'", 'R2', 'L2', 'F2', 'B2']
def solve_dr(s):
    """An optimal finish of a DR state on U/D, by walking down the exact table."""
    out = []; dcur = optimal([s])[0]
    while dcur:
        nx = [cube.do(s, m) for m in DRM]; ds = optimal(nx)
        k = ds.index(dcur - 1); s = nx[k]; out.append(DRM[k]); dcur -= 1
    return out
def sig(s):
    for f in range(3):
        g = fe.look(s, C, f)
        if g: return (f,) + g
def solve_xs(s):
    """A solution of a DR-xs for the U/D colours: a shortest fix to DR, then an optimal DR finish."""
    g = sig(s); fix = cube.parse(path(bm, g)) if path(bm, g) else []
    t = cube.do(s, fix); assert fe.is_dr((C,) + sig(t))
    return fix, solve_dr(t)
def relabel(seq, rot):
    """The sequence that does to the turned cube what seq does to the cube (rot = a whole-cube rotation name)."""
    Rp = cube.MOVES[rot]; Rinv = cube.inverse(tuple(Rp)); out = []
    for m in seq:
        P = cube.MOVES[m]; Q = tuple(Rp[P[Rinv[i]]] for i in range(54))
        out.append(next(n for n in coords.NAMES if tuple(cube.MOVES[n]) == Q))
    return out
def txt(seq): return ' '.join(seq)
def scr_txt(seq):
    c = cube.cancel(seq); assert cube.do(cube.SOLVED, c) == cube.do(cube.SOLVED, seq); return ' '.join(c)
OUT = {}
# ---- a DR-1s that needs 6 turns
D0 = "U R2 F2 D' B2 U2 L2 D"
g6 = min(g for g in nbr if dsl[(g, 3)] == 1 and dmv[(g, 3)] == 6 and g[0] == 2)
fix6 = cube.parse(path(bm, g6)); scr = cube.parse(D0) + cube.inv_seq(fix6)
s = cube.do(cube.SOLVED, scr); assert sig(s) == g6 and dmv[(sig(s), 3)] == 6
OUT['six'] = dict(scramble=scr_txt(scr), fix=txt(fix6))
# ---- every DR-1s layout on F/B
pl = [p for p in fe.EDGES if p[2] != 0]
rows = []
for g in sorted(nbr):
    if dsl[(g, 3)] != 1 or g[0] != 2: continue
    fix = cube.parse(path(bm, g)); scr = cube.parse(D0) + cube.inv_seq(fix); s = cube.do(cube.SOLVED, scr)
    assert sig(s) == g
    h = next(x[4] for x in nbr[g] if x[1] == 'U2')
    rows.append(dict(flipped=' '.join(export_cubie.name_of(p) for p, b in zip(pl, g[1]) if b), turns=dmv[(g, 3)], fix=txt(fix), scramble=scr_txt(scr), other_direction=dmv[(h, 3)]))
OUT['layouts'] = rows
c = collections.Counter(min(r['turns'], r['other_direction']) for r in rows); OUT['simon'] = [c[t] for t in range(2, 7)]
# ---- 12 bad on F/B with F/B colours on U/D: build it in the U/D-colour frame (corners on F/B, every edge bad for U/D), then turn the cube
KIND = ['E' if p[1] == 0 else 'M' if p[0] == 0 else 'S' for p in coords.EDGES]
G_UD = {'E': 0, 'M': 1, 'S': 0}
base = cube.do(cube.SOLVED, "R L'"); cp, ct, _, _ = export_cubie.cubie(base)
slice_slots = [i for i in range(12) if coords.EDGES[i][2] == 0]; layer_slots = [i for i in range(12) if coords.EDGES[i][2] != 0]
home = {k: [i for i in range(12) if KIND[i] == k] for k in 'EMS'}
random.seed(3); found = None
for mset in itertools.combinations(layer_slots, 4):
    for efbits in itertools.product((0, 1), repeat=12):
        pass
    break
def build(mset, ef):
    ep = [None] * 12; it = {k: iter(home[k]) for k in 'EMS'}
    for i in range(12):
        k = 'E' if i in slice_slots else ('M' if i in mset else 'S'); ep[i] = next(it[k])
    return ep
for mset in itertools.combinations(layer_slots, 4):
    ep = build(mset, None)
    # every edge bad for U/D: ef ^ g(place) ^ g(piece) = 1
    ef = [1 ^ G_UD[KIND[i]] ^ G_UD[KIND[ep[i]]] for i in range(12)]
    if sum(ef) % 2: continue
    for swap in (False, True):
        e2 = list(ep)
        if swap:
            a, b = [i for i in range(12) if KIND[e2[i]] == 'S'][:2]; e2[a], e2[b] = e2[b], e2[a]
        s = coords.make(cp, ct, e2, ef)
        par = lambda p: sum(1 for i in range(len(p)) for j in range(i + 1, len(p)) if p[i] > p[j]) % 2
        if par(cp) != par(e2): continue
        g = fe.look(s, 1, 2)
        if g is None: continue
        found = (s, g); break
    if found: break
s, g = found
gs = (2,) + g; assert gs in nbr
fix, fin = solve_xs(s)
sol = fix + fin; scr = cube.inv_seq(sol); assert cube.do(cube.SOLVED, scr) == s
# turn the cube so that the U/D colours become the F/B colours and the F/B faces become the U/D faces
for rot in ('x', "x'"):
    scr2 = relabel(scr, rot); s2 = cube.do(cube.SOLVED, scr2)
    look = fe.look(s2, 2, 1)
    if look is not None: break
assert look is not None and all(coords.flips(s2)), 'not 12 bad on F/B'
fix2 = relabel(fix, rot)
OUT['twelve_bad'] = dict(scramble=scr_txt(scr2), flipped=sum(look[0]), slices=dsl[(gs, 3)], turns=dmv[(gs, 3)], fix=txt(fix2), dr_finish=len(fin))
t2 = cube.do(s2, fix2); assert any(fe.look(t2, c, c) is not None and fe.is_dr((c, c) + fe.look(t2, c, c)) for c in range(3))
# ---- 8 bad on F/B with the good edges all E-slice pieces, U/D colours on the F/B faces: a DR-1s whose flipped edges split 3-1
import patterns
arr = next(r for r in patterns.ROWS if r['f'] == 'FB' and r['pat']['FB'] == (0, 4, 4) and r['slices'] == 1 and r['split'] == (3, 1))
par = lambda p: sum(1 for i in range(len(p)) for j in range(i + 1, len(p)) if p[i] > p[j]) % 2
for swap in (False, True):
    it = {k: iter(home[k]) for k in 'EMS'}; ep = [next(it[arr['piece'][i]]) for i in range(12)]
    if swap:
        a, b = [i for i in range(12) if KIND[ep[i]] == 'S'][:2]; ep[a], ep[b] = ep[b], ep[a]
    if par(cp) == par(ep): break
s = coords.make(cp, ct, ep, [arr['ef'][i] for i in range(12)])
g = fe.look(s, 1, 2); assert g is not None and sum(g[0]) == 4
bad_fb = coords.flips(s); kinds_bad = collections.Counter(KIND[export_cubie.cubie(s)[2][i]] for i in range(12) if bad_fb[i])
assert kinds_bad == {'M': 4, 'S': 4}, kinds_bad
fix, fin = solve_xs(s); scr = cube.inv_seq(fix + fin); assert cube.do(cube.SOLVED, scr) == s
OUT['eight_bad_split'] = dict(scramble=scr_txt(scr), split='3-1', turns=dmv[((2,) + g, 3)], fix=txt(fix))
json.dump(OUT, open('/data/fmc/is-dr-xs-worth-it/research/out/witness.json', 'w'), indent=1)
print('six:', OUT['six']); print('simon:', OUT['simon']); print('twelve_bad:', OUT['twelve_bad']); print(len(rows), 'layouts'); print('eight_bad_split:', OUT['eight_bad_split'])
