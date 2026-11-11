#!/usr/bin/env python3
"""Rodney Kinney's sheet "Adv DR Bounding" (KB doc 418, tab "Optimals (Advanced)"): 216 NISS@1qt cases with a setup alg,
the computed optimal penalty (HTR-breaking moves allowed) and the penalty predicted by his rules ("Heuristic").
Compare with our KF table (DR moves only), evaluated on the HTR state produced by the setup alg."""
import csv, sys, subprocess, collections
sys.path.insert(0, '/data/fmc/research/tool'); import fmccube as fc
rows = list(csv.reader(open('/data/fmc/kb/docs/gsheet/1jRvikzLlm3yHlDQmQ0DLyj3Aw6uinL3Oa-U9_U7R5mY/Optimals_Advanced_.csv')))
hdr, rows = rows[0], [r for r in rows[1:] if len(r) > 10 and r[0]]
LC = {'H-H': 0, 'R-D': 1, 'F-D': 1, 'R-V': 2, 'F-V': 2, 'D-D': 3}
lines, meta = [], []
for r in rows:
    corners, fe, re_, setup, pen, cs, fr = r[0], r[1], r[2], r[3], float(r[4]), r[5], r[6]
    heur = float(r[10])
    st = fc.state_after(setup)
    arrs = fc.to_dr_arrays(st)
    if arrs is None: meta.append((r, None)); continue
    lines.append(' '.join(map(str, arrs[0] + arrs[1] + arrs[2]))); meta.append((r, len(lines) - 1))
out = subprocess.run(['/data/fmc/research/drtools/target/release/drtools', 'query', '/data/fmc/research/data/drbfs', '/data/fmc/research/data/tables'], input='\n'.join(lines) + '\n', capture_output=True, text=True).stdout.strip().split('\n')
stat = collections.Counter(); notes = []
for r, i in meta:
    if i is None: stat['setup does not give a DR state'] += 1; notes.append(('not DR', r[:5])); continue
    kv = dict(t.split('=', 1) for t in out[i].split(' ') if '=' in t)
    kf = int(kv['KF'].split('/')[0]); exact = int(kv['exact']); lc = LC[r[0]]
    pen, heur = float(r[4]), float(r[10])
    nmoves = len(fc.parse(r[3]))
    stat['rows'] += 1
    stat[f'KF(DR moves) - (penalty+Lc) = {kf - (pen + lc):+.0f}'] += 1
    if heur + lc > kf: stat['rule value above our DR-move table'] += 1; notes.append(('rule > table', r[0], r[1], r[2], r[3], 'pen', pen, 'heur', heur, 'KF', kf))
    if heur > pen: stat['rule value above sheet optimum'] += 1
    if kf - (pen + lc) > 0: notes.append(('HTR/DR-breaking alg is shorter than any DR-move finish', r[0], r[1], r[2], r[3], 'sheet', pen + lc, 'KF', kf))
    if kf - (pen + lc) < 0: notes.append(('sheet optimum is longer than our DR-move table', r[0], r[1], r[2], r[3], 'sheet', pen + lc, 'KF', kf, 'exact', exact))
for k, v in sorted(stat.items()): print(f'{v:5d}  {k}')
for n in notes[:40]: print('  ', n)
