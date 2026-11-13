#!/usr/bin/env python3
"""Rodney's 216 rows (KB doc 418) against the all-move optima: is any listed alg shorter than our "complete" optimum
(which would expose a hole in our search), and is any row's stated optimum beatable?"""
import csv, sys, json, subprocess, collections, itertools
sys.path.insert(0, '/data/fmc/judging-a-dr/research/tool'); import fmccube as fc
rows = [r for r in list(csv.reader(open('/data/fmc/kb/docs/gsheet/1jRvikzLlm3yHlDQmQ0DLyj3Aw6uinL3Oa-U9_U7R5mY/Optimals_Advanced_.csv')))[1:] if len(r) > 10 and r[0]]
LC = {'H-H': 0, 'R-D': 1, 'F-D': 1, 'R-V': 2, 'F-V': 2, 'D-D': 3}
ROTS = ['', 'y', 'y2', "y'", 'x2', 'x2 y', 'x2 y2', "x2 y'", 'x', "x'", 'z', "z'", 'x y', "x y'", 'x y2', "x' y", "x' y'", "x' y2", 'z y', "z y'", 'z y2', "z' y", "z' y'", "z' y2"]
def htm(seq):   # face turns count 1, slice moves count 2, rotations 0
    return sum(2 if b in 'MES' else 0 if b in 'xyz' else 1 for b, t in fc.parse(seq))
# A slice move is two outer turns and a cube rotation: M = x' L' R, E = y' U D', S = z F' B (fmccube's directions).
# HTM after cancelling: write the alg as outer turns on the cube's own faces (the rotation relabels every later
# move), then merge turns on the same axis that stand next to each other, as often as that changes something.
SLICE = {'M': ('x', 3, 'R', 'L'), 'E': ('y', 3, 'U', 'D'), 'S': ('z', 1, 'B', 'F')}   # rotation, its quarter turns, outer face turned +t, outer face turned -t
AXIS = {'U': 1, 'D': 1, 'R': 0, 'L': 0, 'F': 2, 'B': 2}
def htm_cancel(seq):
    phys = {f: f for f in fc.FACE_NORMAL}          # face label in space -> the cube's own face now there
    out = []
    def rotate(base, times):
        f = fc.ROT[base][0]
        for _ in range(times % 4):
            back = {fc.NORMAL_FACE[f(n)]: lab for lab, n in fc.FACE_NORMAL.items()}   # space position after the turn <- before
            phys.update({lab: p for lab, p in {lab: phys[back[lab]] for lab in phys}.items()})
    for b, t in fc.parse(seq):
        if b in AXIS: out.append((phys[b], t))
        elif b in SLICE:
            rot, k, with_, against = SLICE[b]
            out += [(phys[with_], t), (phys[against], (4 - t) % 4)]
            rotate(rot, k * t)
        elif b in 'xyz': rotate(b, t)
        else: raise ValueError(b)
    while True:
        new, i = [], 0
        while i < len(out):
            j = i; acc = collections.Counter()
            while j < len(out) and AXIS[out[j][0]] == AXIS[out[i][0]]: acc[out[j][0]] += out[j][1]; j += 1
            new += [(f, v % 4) for f, v in acc.items() if v % 4]; i = j
        if new == out: return len(out)
        out = new
assert htm_cancel("M R2 U2 M'") == 5 and htm_cancel("M F2 U2 M'") == 6 and htm_cancel("R2 M' F2 M U2 F2") == 7
assert all(fc.state_after(a) == fc.state_after(b) for a, b in [("M", "x' L' R"), ("E", "y' U D'"), ("S", "z F' B")])
lines, meta = [], []
for r in rows + [['F-V', 'F-D', 'R-H', "M F2 U2 M'", 'fixed alg']]:   # the last one: the mislabelled row's alg with F2 for R2
    st = fc.state_after(r[3]); arrs = None
    for rot in ROTS:
        arrs = fc.to_dr_arrays(fc.apply(st, fc.parse(rot)))
        if arrs: break
    if not arrs: meta.append((r, None)); continue
    lines.append(' '.join(map(str, arrs[0] + arrs[1] + arrs[2]))); meta.append((r, len(lines) - 1))
out = subprocess.run(['/data/fmc/judging-a-dr/research/drtools/target/release/drtools', 'query', '/data/fmc/judging-a-dr/research/data/drbfs', '/data/fmc/judging-a-dr/research/data/tables'], input='\n'.join(lines) + '\n', capture_output=True, text=True).stdout.strip().split('\n')
allm = json.load(open('/data/fmc/judging-a-dr/research/out/allmoves216.json'))
stat = collections.Counter()
fixed = meta.pop()
kvf = dict(t.split('=', 1) for t in out[fixed[1]].split(' ') if '=' in t)
for r, i in meta:
    if i is None: stat['no DR state even after rotating'] += 1; continue
    kv = dict(t.split('=', 1) for t in out[i].split(' ') if '=' in t)
    if kv['htr_normal'] != '0': stat['setup is not an HTR state'] += 1; continue
    kf = int(kv['KF'].split('/')[0]); am = min(allm.get(kv['kfclass'], (kf, kf)))
    sheet = float(r[4]) + LC[r[0]]; alg = htm_cancel(r[3]); heur = float(r[10]) + LC[r[0]]
    stat['rows'] += 1
    stat[f'sheet optimum - our all-move optimum (of the case the listed alg gives) = {sheet - am:+.0f}'] += 1
    stat[f'length of listed alg (HTM, cancelled across slice moves) - our all-move optimum = {alg - am:+d}'] += 1
    stat[f'length of listed alg - sheet penalty, corner case {r[0]}: {alg - float(r[4]):+.0f}'] += 1
    if heur > am: stat['RULE VALUE ABOVE all-move optimum (rule is not a lower bound there)'] += 1; print('  rule too high:', r[:4], 'cs/fr', r[5], r[6], 'rule total', heur, 'all-move optimum', am, 'DR-move', kf)
    if alg < am: print('  !! listed alg shorter than our optimum:', r[:5], alg, am)
    if sheet != am: print('  sheet differs:', r[:5], 'cs/fr', r[5], r[6], 'sheet', sheet, 'ours', am, 'alg HTM', alg, 'case of the alg', kv['kfclass'])
for k, v in sorted(stat.items()): print(f'{v:5d}  {k}')
kff = int(kvf['KF'].split('/')[0])
FIXED = "M F2 U2 M'"
print(f"  {FIXED} (F2 for R2 in the row labelled F-V / F-D / R-H): case {kvf['kfclass']}, all-move optimum {min(allm.get(kvf['kfclass'], (kff, kff)))}, alg HTM {htm_cancel(FIXED)}")
print("(HTM here cancels across slice moves: `M R2 U2 M'` is 5, the R turn inside the M merging with the R2. The first\n"
      " version of this script counted a slice as 2 turns without cancelling and wrote 6, and 51 rows with the alg longer\n"
      " than the optimum; that output is superseded by this one. The row labelled F-V / F-D / R-H lists `M R2 U2 M'`, which\n"
      " gives another case: its 'sheet differs' line compares the labelled case's 6 with the 5 of the case the alg gives,\n"
      " and its alg-minus-penalty is the one F-V row at +1. With F2 for R2 (line above) the alg is 6.)")
