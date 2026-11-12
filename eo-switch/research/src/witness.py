#!/usr/bin/env python3
"""Witnesses (out/witness.json): (1) every claim example of claims.py (state = setup from solved, F/B EO, DR on U/D,
with an optimal EO-kept DR; replayed again here); (2) real attempts from the
uniform scrambles (out/scrambles.txt, eodrtools mkscr) for each cell of the headline rules: scramble, EO, RZP, the
switched state's features, and an optimal EO-kept DR of the switched state from nissy (`solve dr<X>-eo<Y>` on the
inverse of scramble + EO + RZP), replayed on the sticker model (src/cube.py) in the attempt's own frame."""
import os, sys, json, csv, re, subprocess, collections
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import pop, geom, features as fx
from geom import cube
F = pop.feat(); d = F['d'].astype(int)
AX = {'RL': 0, 'UD': 1, 'FB': 2}; FACE_AX = {'R': 0, 'L': 0, 'U': 1, 'D': 1, 'F': 2, 'B': 2}
def nissy(cmds):
    res = subprocess.run(['nissy', '-b'], input=''.join(c + '\n' for c in cmds), capture_output=True, text=True, check=True).stdout
    lines = res.splitlines(); out = []
    for i, l in enumerate(lines):
        if l.startswith('>>> Executing command'):
            j = i + 1
            while lines[j].startswith('>>>'): j += 1
            m = re.search(r'^(.*)\((\d+)\)\s*$', lines[j]); out.append((m.group(1).strip(), int(m.group(2))))
    return out
def is_dr(s, a):
    """DR on axis a, read off the stickers: the two faces of axis a show only axis-a colours, and every edge of the
    middle slice of axis a has each sticker on a face of its colour's axis."""
    for i, (p, n) in enumerate(cube.ST):
        ax = max(range(3), key=lambda k: abs(n[k]))
        if ax == a and FACE_AX[cube.colour(s, i)] != a: return False
        if p[a] == 0 and sum(1 for k in range(3) if p[k] == 0) == 1 and FACE_AX[cube.colour(s, i)] != ax: return False
    return True
def eo_ok(s, y):
    """EO on axis y: every edge's reference sticker (axis-y-relative good/bad as in the usual rule) - checked through
    the coordinate of the cube turned so that y is F/B."""
    rot = {0: 'y', 1: 'x', 2: ''}[y]
    if rot:
        r = cube.do(cube.SOLVED, rot); ri = cube.do(cube.SOLVED, ' '.join(cube.inv_seq(rot)))
        s = cube.compose(cube.compose(ri, s), r)
    return geom.coords.coords(s)[1] == 0
def drm_axis(s, a):
    """(bad corners, bad edges) for DR on axis a: corners whose axis-a sticker is not on an axis-a face; 2 x the
    edges with no axis-a colour that are outside the middle slice of axis a."""
    c = 0
    for i in range(8):
        for k in range(3):
            pl = geom.coords.CF[i][k]; n = cube.ST[pl][1]; ax = max(range(3), key=lambda q: abs(n[q]))
            if FACE_AX[cube.colour(s, pl)] == a and ax != a: c += 1
    e = 0
    for i, p in enumerate(geom.EDGES):
        cols = {FACE_AX[cube.colour(s, pl)] for pl in geom.coords.EF[i]}
        if a not in cols and p[a] != 0: e += 1
    return c, 2 * e

W = {'claims': {}, 'attempts': [], 'notes': 'claims: state = setup applied to a solved cube (F/B EO, DR on U/D); attempts: the switched state is the inverse scramble with the inverse of EO+RZP as premoves, i.e. the moves inverse(scramble + EO + RZP) from solved.'}
EX = json.load(open(os.path.join(pop.BIG, 'claims_examples.json')))
for cid, ex in EX.items():
    s = cube.do(cube.SOLVED, ex['setup']); t = cube.do(s, ex['dr'])
    assert geom.is_dr_ud(t) and geom.eo_fb_ok(t) and is_dr(t, 1) and eo_ok(t, 2)
    ex['replayed'] = 'DR on U/D reached with F/B EO kept (cube.py)'
    W['claims'][cid] = ex
# attempts for the headline cells
scr = open(os.path.join(pop.OUT, 'scrambles.txt')).read().split('\n')
rows = list(csv.DictReader(open(os.path.join(pop.BIG, 'att_examples.tsv')), delimiter='\t'))
CELLS = [('4c4e', 'both bad edges paired (switch)', lambda ix: F['edges_paired'][ix] == 2),
         ('4c4e', 'no bad edge paired (discard)', lambda ix: F['edges_paired'][ix] == 0),
         ('4c4e', 'one edge paired, edges in one slice (discard)', lambda ix: F['edges_paired'][ix] == 1 and F['edges_same_slice'][ix] == 1),
         ('4c4e', '2 pairs as a bar on one edge', lambda ix: F['pairs'][ix] == 2 and F['edges_paired'][ix] == 1),
         ('4c2e', 'pairs + side/2 >= 1.5 (switch)', lambda ix: F['pairs_plus_half_side_x2'][ix] >= 3),
         ('4c2e', 'pairs + side/2 <= 0.5 (discard)', lambda ix: F['pairs_plus_half_side_x2'][ix] <= 1),
         ('7c8e', '5-6 pairs (switch)', lambda ix: F['pairs'][ix] >= 5),
         ('7c8e', '3 or fewer pairs (discard)', lambda ix: F['pairs'][ix] <= 3),
         ('2c2e', 'a paired edge (switch)', lambda ix: F['edges_paired'][ix] >= 1),
         ('3c2e', 'any (switch)', lambda ix: True)]
chosen = []
for drm, label, cond in CELLS:
    got = 0
    for r in rows:
        if r['drm_normal'] != drm or int(r['length']) != 5: continue
        ix = int(r['ix_switched'])
        if not cond(ix): continue
        want_hit = got == 0          # first example: one that reaches DR in 6 if the cell has any; second: any
        if want_hit and d[ix] > 6 and 'discard' not in label: continue
        chosen.append((drm, label, r)); got += 1
        if got == 2: break
cmds = []
for drm, label, r in chosen:
    S = scr[int(r['scr'])]; S_side = S if r['side'] == '0' else ' '.join(cube.inv_seq(S))
    inv = ' '.join(cube.inv_seq(' '.join(x for x in [S_side, r['eo'], r['rzp']] if x)))
    cmds.append(f"solve dr{r['dr_axis'].lower()}-eo{r['eo_axis'].lower()} {inv}")
ans = nissy(cmds)
for (drm, label, r), (sol, n) in zip(chosen, ans):
    x, y = AX[r['dr_axis']], AX[r['eo_axis']]
    S = scr[int(r['scr'])]; S_side = S if r['side'] == '0' else ' '.join(cube.inv_seq(S))
    normal = cube.do(cube.SOLVED, ' '.join(q for q in [S_side, r['eo'], r['rzp']] if q))
    assert eo_ok(normal, y) and '%dc%de' % drm_axis(normal, x) == drm, (r, drm_axis(normal, x))
    sw = cube.inverse(normal)
    t = cube.do(sw, sol)
    assert is_dr(t, x) and n == int(r['d_switched']), (r, sol, n)
    assert not any(m[0] in {0: 'RL', 1: 'UD', 2: 'FB'}[y] and not m.endswith('2') for m in sol.split()), 'EO broken'
    W['attempts'].append(dict(cell=f'{drm}: {label}', scramble=S, side='normal' if r['side'] == '0' else 'inverse (EO and RZP written on the inverse scramble)',
        eo_axis=r['eo_axis'], dr_axis=r['dr_axis'], eo=r['eo'], rzp=r['rzp'], total=int(r['length']), case_before_switch=drm,
        switched_state=fx.describe(F, int(r['ix_switched'])), switched_dr=f'{sol} ({n})',
        replayed='EO+RZP gives the stated DRM on its axis; after the switch the DR reaches DR on that axis with the EO kept (cube.py), nissy length = table length'))
json.dump(W, open(os.path.join(pop.OUT, 'witness.json'), 'w'), indent=1)
print(len(W['claims']), 'claim examples,', len(W['attempts']), 'attempts, all replayed')
