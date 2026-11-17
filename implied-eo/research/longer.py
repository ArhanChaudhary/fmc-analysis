#!/usr/bin/env python3
"""Sub-6 EOs implied by a longer EO.  Y has at most 5 moves; its partner X on another axis (or, by the superflip,
on the same axis) has 6 or more.  X is still usable when one of its sides is short: you apply that side ('the
probe'), trace, and recognise the case on the other side ('the pattern') without solving it.
-> out/longer.json"""
import os, json, collections, re, sys
import numpy as np
from eomodel import *
import census as E
HERE = os.path.dirname(os.path.abspath(__file__))
D = E.DIST
NS = int(sys.argv[1]) if len(sys.argv) > 1 else 1_000_000
def parse_eo(txt):
    m = re.match(r'^\s*([^()]*?)\s*(?:\(([^()]*)\))?\s*([^()]*?)\s*$', txt)
    normal = (m.group(1) + ' ' + m.group(3)).split(); inverse = (m.group(2) or '').split()
    axes = {AX[s[-1][0]][0] for s in (normal, inverse) if s}; assert len(axes) == 1, txt
    return axes.pop(), normal, inverse
def key(txt): a, n, i = parse_eo(txt); return E.to_fb(a, E.case_of(i, a), E.case_of(n, a))
def nice(seqs):
    return min(seqs, key=lambda s: (sum(m.endswith("'") for m in s), sum(m.endswith('2') for m in s), [FACES.index(m[0]) for m in s]))
def sol(w, ax): return ' '.join(nice(E.solutions(w, ax)))
def eo(n, i): return (n + (' ' if n and i else '') + (f'({i})' if i else '')) or '(skip)'
def mes(w): return [bin(w & SLICE[k]).count('1') for k in (0, 1, 2)]      # bad places in M, E, S
out = {}
# 1. the case that was pointed out, and the rule: after U D, flip the R- and L-layer places of what you see
X, Y = "U D (D U2 F U)", "F B (F U2 B)"
assert key(X) == key(Y)
u = E.case_of(parse_eo(X)[2], 1); u2 = E.case_of(parse_eo(Y)[2], 2)
assert u2 ^ (FULL ^ SLICE[0]) == u and D[1][u] == 4 and D[2][u2] == 3
out['pointed'] = {'X': X, 'Y': Y, 'pattern': mask_names(u), 'good': mask_names(FULL ^ u), 'pattern_len': D[1][u], 'case': mask_names(u2)}

# 2. counts: every Y of at most 5 with a partner of 6 or more, by link and by the short side of the partner
def side_table(ax, bx, t): return collections.Counter((D[bx][w2], D[ax][w2 ^ t]) for w2 in D[bx])   # (Y side, X side)
rows = collections.Counter()
for name, ax, bx, t in (('trick', 2, 0, FULL ^ SLICE[1]), ('trick+superflip', 2, 0, SLICE[1]), ('superflip', 2, 2, FULL)):
    side = side_table(ax, bx, t)
    for (y1, x1), n1 in side.items():
        for (y2, x2), n2 in side.items():
            if y1 + y2 <= 5 and x1 + x2 >= 6: rows[(name, min(x1, x2), x1 + x2, y1 + y2)] += n1 * n2
out['counts'] = [[list(k), v] for k, v in sorted(rows.items())]
out['by_probe'] = {name: {p: sum(v for k, v in rows.items() if k[0] == name and k[1] == p) for p in range(8)} for name in ('trick', 'trick+superflip', 'superflip')}
print('by link and probe length:', out['by_probe'])

# 3. the probe F B, target R/L: R L (c') for every R/L case c' of at most 3 moves; what you see after F B is c
T8 = FULL ^ SLICE[1]
probe = []
for c2 in sorted(D[0], key=lambda w: (D[0][w], w)):
    if D[0][c2] > 3: continue
    c = c2 ^ T8
    probe.append({'rl_case': c2, 'pattern': c, 'pattern_names': mask_names(c), 'good_names': mask_names(FULL ^ c), 'mes': mes(c), 'nbad': bin(c).count('1'),
                  'pattern_len': D[2][c], 'Y': eo('R L', sol(c2, 0)), 'X': eo('F B', sol(c, 2)), 'ylen': 2 + D[0][c2], 'xlen': 2 + D[2][c],
                  'key': list(E.to_fb(0, c2, E.case_of(['R', 'L'], 0)))})
    assert key(probe[-1]['X']) == key(probe[-1]['Y']) == tuple(probe[-1]['key'])
hist = collections.Counter((r['ylen'] - 2, r['pattern_len']) for r in probe)
print('probe F B -> R L (c): (moves of c, moves of the pattern): count', sorted(hist.items()), 'total', len(probe))
out['probe'] = probe; out['probe_hist'] = [[list(k), v] for k, v in sorted(hist.items())]

# 4. Jay's and wen's shape: 8 bad after two opposite quarter turns, 3 of the 4 good places in the slice across the axis
shape = []
for g3 in range(4):
    Sm = [p for p in range(12) if SLICE[2] >> p & 1]
    for lone in [p for p in range(12) if not SLICE[2] >> p & 1]:
        good = sum(1 << p for k, p in enumerate(Sm) if k != g3) | 1 << lone
        c = FULL ^ good                                                    # the pattern, on F/B
        t_ud, t_rl = c ^ (FULL ^ SLICE[0]), c ^ (FULL ^ SLICE[1])          # read on U/D and on R/L
        lone_on_ud = bool(SLICE[0] >> lone & 1)                            # the lone good place has a U or D sticker place
        shape.append((D[2][c], D[1][t_ud], D[0][t_rl], lone_on_ud, bin(t_ud).count('1'), bin(t_rl).count('1')))
sh = collections.Counter(shape)
print('8 bad, 3 good on S + 1 elsewhere (pattern len, U/D case len, R/L case len, lone on U/D face, bad U/D, bad R/L):', sorted(sh.items()))
ok = all((ud == 3) == lone_ud and (rl == 3) == (not lone_ud) for pl, ud, rl, lone_ud, _, _ in shape if pl != 3)
out['shape'] = {'n': len(shape), 'three_move': sum(1 for s in shape if s[0] == 3), 'rule_holds': ok,
                'others': sorted(collections.Counter((s[0], 3 if s[3] else s[1], s[2] if s[3] else 3) for s in shape if s[0] != 3).items())}
print('rule holds:', ok, out['shape'])

# 5. the other links with a probe of at most 2 moves: one example each
def example(name, ax, bx, t, want):
    for v2 in sorted(D[bx], key=lambda w: (D[bx][w], w)):
        for u2 in sorted(D[bx], key=lambda w: (D[bx][w], w)):
            if D[bx][v2] + D[bx][u2] > 5: continue
            v, u = v2 ^ t, u2 ^ t
            if (min(D[ax][v], D[ax][u]), D[ax][v] + D[ax][u], D[bx][v2] + D[bx][u2]) == want and D[ax][v] <= D[ax][u]:
                Xt, Yt = eo(sol(v, ax), sol(u, ax)), eo(sol(v2, bx), sol(u2, bx))
                assert E.to_fb(ax, u, v) == E.to_fb(bx, u2, v2)
                return {'X': Xt, 'Y': Yt, 'pattern': mask_names(u), 'pattern_len': D[ax][u], 'key': list(E.to_fb(bx, u2, v2))}
out['ex_slice'] = example('trick+superflip', 2, 0, SLICE[1], (2, 7, 5))
out['ex_super'] = example('superflip', 2, 2, FULL, (2, 9, 5))
out['ex_xf'] = {'X': 'U F (R L F B)', 'Y': 'U B R L'}; assert key('U F (R L F B)') == key('U B R L')
print(out['ex_slice'], out['ex_super'])

# 6. how often: a 5-move EO of the form (two opposite quarter turns) + (3-move case) whose partners are all longer than 5
keys = set()
main = {tuple(s['key']) for s in json.load(open(os.path.join(HERE, 'out', 'study.json')))['sets']}
for ax in range(3):
    two = E.case_of({2: ['F', 'B'], 0: ['R', 'L'], 1: ['U', 'D']}[ax], ax)
    for c in D[ax]:
        if D[ax][c] == 3:
            keys.add(E.to_fb(ax, c, two)); keys.add(E.to_fb(ax, two, c))
new = sorted(keys - main)
print('5-move EOs of that form:', len(keys), 'of which with no partner of 5 or less:', len(new))
U = np.array([k[0] for k in new], dtype=np.int32); V = np.array([k[1] for k in new], dtype=np.int32)
nrng = np.random.default_rng(12); hit = 0; done = 0
while done < NS:
    n = min(10000, NS - done)
    perm = np.argsort(nrng.random((n, 12)), axis=1)
    bits = nrng.integers(0, 2, (n, 12)); bits[:, 11] = bits[:, :11].sum(1) % 2
    B = (bits << np.arange(12)).sum(1).astype(np.int32)
    A = B[:, None] ^ U[None, :]; W = np.zeros_like(A)
    for h in range(12): W |= ((A >> h) & 1) << perm[:, h][:, None].astype(np.int32)
    hit += int((W == V[None, :]).any(1).sum()); done += n
p = hit / NS
out['freq'] = {'n': NS, 'sets_all': len(keys), 'sets_new': len(new), 'p': p, 'ci': 1.96 * (p * (1 - p) / NS) ** 0.5}
print('scrambles with at least one of the new ones:', f'{100*p:.2f}% ± {100*out["freq"]["ci"]:.2f}')
json.dump(out, open(os.path.join(HERE, 'out', 'longer.json'), 'w'))
