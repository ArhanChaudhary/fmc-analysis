#!/usr/bin/env python3
"""Rodney's 216 rows (KB doc 418) against the all-move optima: is any listed alg shorter than our "complete" optimum
(which would expose a hole in our search), and is any row's stated optimum beatable?"""
import csv, sys, json, subprocess, collections, itertools
sys.path.insert(0, '/data/fmc/research/tool'); import fmccube as fc
rows = [r for r in list(csv.reader(open('/data/fmc/kb/docs/gsheet/1jRvikzLlm3yHlDQmQ0DLyj3Aw6uinL3Oa-U9_U7R5mY/Optimals_Advanced_.csv')))[1:] if len(r) > 10 and r[0]]
LC = {'H-H': 0, 'R-D': 1, 'F-D': 1, 'R-V': 2, 'F-V': 2, 'D-D': 3}
ROTS = ['', 'y', 'y2', "y'", 'x2', 'x2 y', 'x2 y2', "x2 y'", 'x', "x'", 'z', "z'", 'x y', "x y'", 'x y2', "x' y", "x' y'", "x' y2", 'z y', "z y'", 'z y2', "z' y", "z' y'", "z' y2"]
def htm(seq):   # face turns count 1, slice moves count 2, rotations 0
    return sum(2 if b in 'MES' else 0 if b in 'xyz' else 1 for b, t in fc.parse(seq))
lines, meta = [], []
for r in rows:
    st = fc.state_after(r[3]); arrs = None
    for rot in ROTS:
        arrs = fc.to_dr_arrays(fc.apply(st, fc.parse(rot)))
        if arrs: break
    if not arrs: meta.append((r, None)); continue
    lines.append(' '.join(map(str, arrs[0] + arrs[1] + arrs[2]))); meta.append((r, len(lines) - 1))
out = subprocess.run(['/data/fmc/research/drtools/target/release/drtools', 'query', '/data/fmc/research/data/drbfs', '/data/fmc/research/data/tables'], input='\n'.join(lines) + '\n', capture_output=True, text=True).stdout.strip().split('\n')
allm = json.load(open('/data/fmc/research/out/allmoves216.json'))
stat = collections.Counter()
for r, i in meta:
    if i is None: stat['no DR state even after rotating'] += 1; continue
    kv = dict(t.split('=', 1) for t in out[i].split(' ') if '=' in t)
    if kv['htr_normal'] != '0': stat['setup is not an HTR state'] += 1; continue
    kf = int(kv['KF'].split('/')[0]); am = min(allm.get(kv['kfclass'], (kf, kf)))
    sheet = float(r[4]) + LC[r[0]]; alg = htm(r[3]); heur = float(r[10]) + LC[r[0]]
    stat['rows'] += 1
    stat[f'sheet optimum - our all-move optimum = {sheet - am:+.0f}'] += 1
    stat[f'length of listed alg (HTM) - our all-move optimum = {alg - am:+d}'] += 1
    if heur > am: stat['RULE VALUE ABOVE all-move optimum (rule is not a lower bound there)'] += 1; print('  rule too high:', r[:4], 'cs/fr', r[5], r[6], 'rule total', heur, 'all-move optimum', am, 'DR-move', kf)
    if alg < am: print('  !! listed alg shorter than our optimum:', r[:5], alg, am)
    if sheet != am: print('  sheet differs:', r[:5], 'cs/fr', r[5], r[6], 'sheet', sheet, 'ours', am, 'alg HTM', alg)
for k, v in sorted(stat.items()): print(f'{v:5d}  {k}')
