#!/usr/bin/env python3
"""S-DR-8 (Daichi: are all states without a sub-10 DR 20 moves optimal?): the optimal solution, by nissy's optimal
solver, of the first few sample scrambles that have no DR under 10 even with NISS (or, if there are none, none
under 10 on any axis normal or inverse).  Each solution is replayed on the sticker model.  Heavy: nissy loads a
2.5 GB table; run alone.  Writes out/optimal_no_sub10.tsv.

usage: optimal_check.py [how many, default 3]"""
import csv, os, re, subprocess, sys
import sticker, cube

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, '..', 'out')
csv.field_size_limit(10**7)
k = int(sys.argv[1]) if len(sys.argv) > 1 else 3
AX = ['RL', 'UD', 'FB']
rows = list(csv.DictReader(open(os.path.join(OUT, 'big', 'scr50k.tsv')), delimiter='\t'))
scr = [l.strip() for l in open(os.path.join(OUT, 'scrambles.txt')) if l.strip()]
d6 = lambda r: min(int(r[f'd_{s}_{a}']) for s in 'ni' for a in AX)
pick = [r for r in rows if int(r['dniss']) >= 10] or [r for r in rows if d6(r) >= 10]
kind = 'no sub-10 DR even with NISS' if int(pick[0]['dniss']) >= 10 else 'no sub-10 DR on 6 tries (NISS gives 9)'
out = []
for r in pick[:k]:
    s = scr[int(r['i']) - 1]
    res = subprocess.run(['nissy', 'solve', 'optimal', '-t', '4', s], capture_output=True, text=True, check=True).stdout.strip().splitlines()[-1]
    m = re.match(r'(.*)\((\d+)\)\s*$', res)
    sol, n = m.group(1).strip(), int(m.group(2))
    assert cube.do(cube.do(cube.SOLVED, s), sol) == cube.SOLVED and len(sol.split()) == n
    out.append((r['i'], s, d6(r), r['dniss'], n, sol))
    print(r['i'], 'best of 6', d6(r), 'NISS', r['dniss'], 'optimal', n, sol, flush=True)
with open(os.path.join(OUT, 'optimal_no_sub10.tsv'), 'w') as f:
    f.write(f'# {kind}: {len(pick)} of {len(rows)} sample scrambles; the optimal solution of the first {len(out)} (nissy solve optimal), replayed\n')
    f.write('sample_index\tscramble\tbest_of_6_dr\tniss_dr\toptimal_length\toptimal_solution\n')
    for t in out:
        f.write('\t'.join(map(str, t)) + '\n')
