#!/usr/bin/env python3
"""Our NISS DR length against `nissy solve dr -N -t 4` (slow above 7 turns, so only on sample scrambles whose NISS
DR is at most 7 and shorter than the best of 6 linear tries: the cases where NISS matters and nissy is quick).
usage: check_niss_dr.py [how many, default 40]       appends its line to out/checks_counts.tsv"""
import csv, os, re, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(HERE, '..', 'out')
csv.field_size_limit(10**7)
k = int(sys.argv[1]) if len(sys.argv) > 1 else 40
AX = ('RL', 'UD', 'FB')
scr = [l.strip() for l in open(os.path.join(OUT, 'scrambles.txt'))]
sel = []
for r in csv.DictReader(open(os.path.join(OUT, 'big', 'scr50k.tsv')), delimiter='\t'):
    if int(r['dniss']) <= 7 and min(int(r[f'd_{s}_{a}']) for s in 'ni' for a in AX) > int(r['dniss']):
        sel.append(r)
        if len(sel) == k:
            break
ok = 0
for r in sel:
    out = subprocess.run(['nissy', 'solve', 'dr', '-N', '-t', '4', scr[int(r['i']) - 1]], capture_output=True, text=True, timeout=600).stdout
    v = int(re.search(r'\((\d+)\)\s*$', out.strip()).group(1))
    ok += v == int(r['dniss'])
    if v != int(r['dniss']):
        print('DISAGREE', r['i'], r['dniss'], out)
line = f"dr NISS (nissy dr -N), scrambles where NISS <= 7 beats linear\t{len(sel)}\t{ok}\n"
open(os.path.join(OUT, 'checks_counts.tsv'), 'a').write(line)
print(line.strip())
sys.exit(0 if ok == len(sel) else 1)
