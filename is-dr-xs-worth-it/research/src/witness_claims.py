#!/usr/bin/env python3
"""Scrambles and pattern checks behind rows of the write-up's section 8 (out/witness_claims.json), each read off the
stickers, looked up in the table of kinds and checked with nissy.

  six_both     a DR-1s whose shortest DR takes 6 turns from the normal side and 6 from the inverse
  ninth        8 bad edges on F/B, the four good ones the S-slice pieces, the F/B colours on the F and B faces of every
               corner: the number of flipped edges is not fixed (the printed scramble has two and is a DR-2s)
  t11239       trangium's example "(U R2 F2 D2 R' U) // guaranteed extra-good dr-1s": 8 bad on F/B, the good ones the
               E-slice pieces, U/D colours on the F/B faces, the four flipped edges in the E-slice places; from the
               other side the flipped edges are the four E-slice pieces
  quarter_turns  the quarter turns a DR-1s needs before the slice, by how many of the four flipped edges already sit in
               the slice that fixes (4: none, 2: one, 3, 1 or 0: two), over all 70 layouts
  patterns     for the patterns of Rodney's list and its restatement that give a DR-1s with the flipped edges 4-0:
               the fewest turns to a real DR on the side it was made and from the other side, over every layout
               (2 from the other side = the four belong to the slice that fixes, 4 = to the other slice)

The table of kinds (out/fecosets.pkl) is for the U/D colours; a DR-xs of another colour is turned (whole-cube
rotation) so that its colour becomes U/D before it is looked up.  Needs nissy on the PATH (source /data/fmc/env.sh)."""
import json, collections, pickle, subprocess
import cube, fe, coords, export_cubie, patterns
from fecosets import path
O = '/data/fmc/is-dr-xs-worth-it/research/out/'
d = pickle.load(open(O + 'fecosets.pkl', 'rb')); dsl, dmv, bm = d['dsl'], d['dmv'], d['bm']
EDGES = coords.EDGES
KIND = ['E' if p[1] == 0 else 'M' if p[0] == 0 else 'S' for p in EDGES]        # home slice of the piece / of the place
NAME = [export_cubie.name_of(p) for p in EDGES]
ROT = {1: None, 2: 'x', 0: 'z'}                                                 # the rotation that makes colour c the U/D colour

def turned(s, c):
    """The same state with the cube turned so that colour axis c is the U/D colour axis."""
    if ROT[c] is None: return s
    r = ROT[c]
    return cube.do(cube.compose(cube.do(cube.SOLVED, [r + "'"]), s), [r])
def kinds(s):
    """Every way s looks like a DR-xs: colour, faces, flipped places, the pieces there, slices and fewest turns to a real DR."""
    out = []
    ep = export_cubie.cubie(s)[2]
    for c in range(3):
        for f in range(3):
            g = fe.look(s, c, f)
            if g is None: continue
            layer = [i for i in range(12) if EDGES[i][f] != 0]
            at = [i for i, b in zip(layer, g[0]) if b]
            t = turned(s, c); sig = next((ff,) + fe.look(t, 1, ff) for ff in range(3) if fe.look(t, 1, ff) is not None)
            out.append(dict(colour='RL UD FB'.split()[c], faces='RL UD FB'.split()[f], flipped=len(at), places=sorted(NAME[i] for i in at),
                            pieces=sorted(NAME[ep[i]] for i in at), piece_slices=''.join(sorted(KIND[ep[i]] for i in at)),
                            place_slices=''.join(sorted(KIND[i] for i in at)), slices=dsl[(sig, 3)], turns=dmv[(sig, 3)]))
    return out
def one(s, colour, faces): return next(k for k in kinds(s) if k['colour'] == colour and k['faces'] == faces)
def bad_fb(s):
    """(number of edges bad for F/B, home slices of the good pieces)."""
    b = coords.flips(s); ep = export_cubie.cubie(s)[2]
    return sum(b), ''.join(sorted(KIND[ep[i]] for i in range(12) if not b[i]))
def nissy(*a): return subprocess.run(['nissy'] + list(a), capture_output=True, text=True, check=True).stdout.strip()
def shortest_dr(scr):
    """nissy's shortest DR on any axis, any face turns: (moves, length)."""
    out = nissy('solve', 'dr', scr); mv, ln = out.rsplit(' (', 1) if ' (' in out else ('', out.strip('()'))
    return mv.strip(), int(ln.rstrip(')'))
def txt(seq): return ' '.join(seq)
OUT = {}

# ---- a DR-1s that is 6 turns from a real DR from either side
scr = "B2 D B2 D R L B L2 D2 F'"
s = cube.do(cube.SOLVED, scr); si = cube.inverse(s)
k, ki = one(s, 'UD', 'FB'), one(si, 'FB', 'UD')
dn, di = shortest_dr(scr), shortest_dr(txt(cube.inv_seq(scr)))
assert k['slices'] == ki['slices'] == 1 and k['turns'] == ki['turns'] == 6 and dn[1] == di[1] == 6, (k, ki, dn, di)
assert fe.is_dr((1, 1) + fe.look(cube.do(s, dn[0]), 1, 1)) and fe.is_dr((2, 2) + fe.look(cube.do(si, di[0]), 2, 2))
OUT['six_both'] = dict(scramble=scr, normal=dn[0], normal_len=dn[1], inverse=di[0], inverse_len=di[1], places=k['places'])

# ---- the ninth case: 8 bad on F/B, the S-slice pieces good, F/B colours on the F and B faces
scr = "F B U D L F2 L U D'"
s = cube.do(cube.SOLVED, scr)
assert bad_fb(s) == (8, 'SSSS')
k = one(s, 'FB', 'FB'); dn = shortest_dr(scr)
assert k['flipped'] == 2 and k['slices'] == 2 and k['turns'] == dn[1] == 7, (k, dn)
# the same case in the frame of Appendix B (U/D colours on their own faces, EO axis U/D, M and S bad): every even number of flips happens
counts = sorted({fl for (sl, fl, sp) in patterns.outcomes('UD', 'MS', 'UD')})
assert counts == [0, 2, 4, 6, 8], counts
OUT['ninth'] = dict(scramble=scr, flipped=k['flipped'], places=k['places'], slices=k['slices'], turns=k['turns'], nissy_dr=dn[0], nissy_dr_len=dn[1], flip_counts=counts)

# ---- trangium's example
T = "R' U' F U2 B' L2 B D2 R2 F2 L2 B' F2 U' L' D' B' F2 R' D2 U B' L' R' U' F"
pre, route, rest = "U' B'", "U R2 F2 D2 R' U", "D R2 F2 B2 U D2 R' L F B L2"
a = cube.do(cube.do(cube.SOLVED, cube.inv_seq(T)), pre); assert bad_fb(a) == (8, 'EEEE')
b = cube.do(a, route); assert bad_fb(b) == (8, 'EEEE')
k = one(b, 'UD', 'FB'); ko = one(cube.inverse(b), 'FB', 'UD')
assert k['slices'] == 1 and k['flipped'] == 4 and k['place_slices'] == 'EEEE' and k['turns'] == 4, k
assert ko['slices'] == 1 and ko['piece_slices'] == 'EEEE', ko
sol = cube.parse(rest) + cube.inv_seq(pre + ' ' + route)
assert cube.do(cube.do(cube.SOLVED, T), sol) == cube.SOLVED
OUT['t11239'] = dict(places=k['places'], pieces=k['pieces'], piece_slices=k['piece_slices'], turns=k['turns'], other_side_pieces=ko['pieces'], solution_len=len(sol))

# ---- the 4-0 patterns: turns on the side they are made and from the other side, over every layout
# (frame of Appendix B: the DR-xs is for the U/D colours; axis = EO axis, pat = (E bad, M bad, S bad), f = faces of the corners)
BASE = {'FB': "R L'", 'RL': "F B'"}
par = lambda p: sum(1 for i in range(len(p)) for j in range(i + 1, len(p)) if p[i] > p[j]) % 2
home = {x: [i for i in range(12) if KIND[i] == x] for x in 'EMS'}
def states(axis, pat, f):
    cp, ct, _, _ = export_cubie.cubie(cube.do(cube.SOLVED, BASE[f]))
    for arr in patterns.ROWS:
        if not (arr['f'] == f and arr['pat'][axis] == pat and arr['slices'] == 1): continue
        for swap in (False, True):
            it = {x: iter(home[x]) for x in 'EMS'}; ep = [next(it[arr['piece'][i]]) for i in range(12)]
            if swap:
                p, q = [i for i in range(12) if KIND[ep[i]] == 'S'][:2]; ep[p], ep[q] = ep[q], ep[p]
            if par(cp) == par(ep): break
        yield coords.make(cp, ct, ep, [arr['ef'][i] for i in range(12)])
CASES = [('all oriented, FB on UD (Rodney, line 2)', 'UD', (0, 0, 0), 'FB'),
         ('FB-colored misoriented, RL on UD (Rodney, line 5)', 'FB', (4, 4, 0), 'RL'),
         ('UD-colored misoriented, RL on UD (Rodney, line 6)', 'FB', (4, 0, 4), 'RL'),
         ('FB-colored misoriented, FB on UD (trangium)', 'UD', (0, 4, 4), 'FB'),
         ('E-slice pieces good, UD on FB (restatement, third axis)', 'FB', (0, 4, 4), 'FB')]
OUT['patterns'] = {}
for name, axis, pat, f in CASES:
    here = collections.Counter(); other = collections.Counter(); split_here = collections.Counter(); n = 0
    for s in states(axis, pat, f):
        k = one(s, 'UD', f); ko = one(cube.inverse(s), f, 'UD')            # the other side: colours f on the U/D faces
        assert k['slices'] == ko['slices'] == 1
        here[k['turns']] += 1; other[ko['turns']] += 1; n += 1
        split_here['pieces 4-0' if len(set(k['piece_slices'])) == 1 else 'places 4-0' if len(set(k['place_slices'])) == 1 else 'neither'] += 1
    # one arrangement of the pieces per layout, so the other side is only recorded where it is the same for all of them
    OUT['patterns'][name] = dict(layouts=n, turns_here={str(t): v for t, v in sorted(here.items())}, four_together=dict(split_here))
    if len(other) == 1: OUT['patterns'][name]['turns_other_side'] = next(iter(other))
# ---- quarter turns a DR-1s needs before the slice, by how many of its four flipped edges already sit in the slice that fixes
# (corners on F/B, the slice that fixes is R L, its places are UF UB DF DB; face turns only, staying a DR-1s on F/B)
import heapq
nbr = d['nbr']
layer = [p for p in fe.EDGES if p[2] != 0]; inside = [1 if p[0] == 0 else 0 for p in layer]
ones = [g for g in nbr if g[0] == 2 and dsl[(g, 3)] == 1]; assert len(ones) == 70
goal = [g for g in ones if list(g[1]) == inside]; assert len(goal) == 1 and dmv[(goal[0], 3)] == 2
qt = {goal[0]: 0}; pq = [(0, 0, goal[0])]; cnt = 0
while pq:
    q0, _, g = heapq.heappop(pq)
    if q0 > qt[g]: continue
    for a, text, cost, sl, h in nbr[g]:
        if sl or h[0] != 2 or dsl[(h, 3)] != 1: continue
        q = q0 + sum(1 for m in text.split() if not m.endswith('2'))
        if q < qt.get(h, 99): qt[h] = q; cnt += 1; heapq.heappush(pq, (q, cnt, h))
by = collections.defaultdict(set)
for g in ones: by[sum(b for b, i in zip(g[1], inside) if i)].add(qt[g])
OUT['quarter_turns'] = {str(k): sorted(v) for k, v in sorted(by.items())}
assert OUT['quarter_turns'] == {'0': [2], '1': [2], '2': [1], '3': [2], '4': [0]}, OUT['quarter_turns']

P = OUT['patterns']
assert P['all oriented, FB on UD (Rodney, line 2)']['turns_other_side'] == 2
assert P['FB-colored misoriented, RL on UD (Rodney, line 5)']['turns_other_side'] == 2
assert P['UD-colored misoriented, RL on UD (Rodney, line 6)']['turns_other_side'] == 4
assert P['FB-colored misoriented, FB on UD (trangium)']['turns_other_side'] == 4
assert set(P['E-slice pieces good, UD on FB (restatement, third axis)']['turns_here']) == {'4'}
json.dump(OUT, open(O + 'witness_claims.json', 'w'), indent=1)
print(json.dumps(OUT, indent=1))
