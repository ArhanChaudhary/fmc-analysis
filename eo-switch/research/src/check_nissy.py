#!/usr/bin/env python3
"""Check the exact EO-kept DR table (out/big/d.u8) against nissy 2.0.8 (`solve drud-eofb`, an independent solver).

`eoswtools checkpos` draws uniformly random cosets and writes each as a scramble (12 random DR-group turns, then the
inverse of a shortest path from the coset to DR), with the table's value; nissy is asked the optimal EO-kept DR length
of each; each nissy solution is also replayed on is-dr-xs-worth-it's sticker model (src/cube.py) to check it reaches
DR on U/D with F/B EO kept.  Output: out/checks_nissy.tsv."""
import csv, os, re, subprocess, sys, collections
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__))))
import geom
HERE = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(HERE, '..', 'out')
rows = list(csv.DictReader(open(os.path.join(OUT, 'big', 'checkpos.tsv')), delimiter='\t'))
cmds = ''.join(f"solve drud-eofb {r['scramble']}\n" for r in rows)
res = subprocess.run(['nissy', '-b'], input=cmds, capture_output=True, text=True, check=True).stdout
lines = res.splitlines(); answers = []
for i, l in enumerate(lines):
    if l.startswith('>>> Executing command'):
        j = i + 1
        while lines[j].startswith('>>>'): j += 1
        m = re.search(r'^(.*)\((\d+)\)\s*$', lines[j]); assert m, lines[j]
        answers.append((int(m.group(2)), m.group(1).strip()))
assert len(answers) == len(rows)
agree = 0; dist = collections.Counter(); bad = []
for r, (n, sol) in zip(rows, answers):
    dist[n] += 1
    s = geom.cube.do(geom.cube.SOLVED, r['scramble'] + ' ' + sol)
    assert geom.is_dr_ud(s) and geom.eo_fb_ok(s), (r, sol)
    if n == int(r['expected']): agree += 1
    else: bad.append((r, n))
with open(os.path.join(OUT, 'checks_nissy.tsv'), 'w') as f:
    f.write('check\tpositions\tagree\tnissy distribution\n')
    f.write(f"EO-kept DR (drud-eofb) on uniformly random cosets\t{len(rows)}\t{agree}\t{' '.join(f'{k}:{dist[k]}' for k in sorted(dist))}\n")
print(f'{agree}/{len(rows)} agree with nissy; every nissy solution replayed to DR on the sticker model')
for b in bad[:10]: print('DISAGREE', b)
sys.exit(1 if bad else 0)
