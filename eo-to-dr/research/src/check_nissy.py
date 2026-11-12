#!/usr/bin/env python3
"""Check every table mapping against nissy 2.0.8, an independent solver with its own tables.

`eodrtools check pos` writes positions with the value our tables give (out/big/checkpos.tsv): the fewest turns to DR
on each of the three axes (all_dr seen through a rotation), the optimal EO per axis and with NISS over all axes, and
for EO-solved positions on each axis Y the fewest EO-keeping turns to DR on each other axis X (eo-fb_dr through a
rotation) and the fewest turns of any kind (all_dr, EO-solved part).  This script asks nissy the same questions in
batch mode and compares.  Output: out/checks_nissy.tsv (one row per mapping) and a printed summary.

usage: check_nissy.py [n]      (n positions per mapping, default 1000)"""
import csv, os, re, subprocess, sys, collections

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, '..', 'out')
BIN = os.path.join(HERE, '..', 'eodrtools', 'target', 'release', 'eodrtools')
n = int(sys.argv[1]) if len(sys.argv) > 1 else 1000

pos_file = os.path.join(OUT, 'big', 'checkpos.tsv')
with open(pos_file, 'w') as f:
    subprocess.run([BIN, 'check', 'pos', os.path.join(OUT, 'scrambles.txt'), str(n), '5'], stdout=f, check=True)
rows = list(csv.DictReader(open(pos_file), delimiter='\t'))
cmds = ''.join(f"solve {r['step']} {r['moves']}\n" for r in rows)
res = subprocess.run(['nissy', '-b'], input=cmds, capture_output=True, text=True, check=True).stdout
# one answer per command: the line after each ">>> Executing command" banner, ending in "(n)"
answers = []
lines = res.splitlines()
for i, l in enumerate(lines):
    if l.startswith('>>> Executing command'):
        j = i + 1
        while lines[j].startswith('>>>'):
            j += 1
        m = re.search(r'\((\d+)\)\s*$', lines[j])
        assert m, lines[j]
        answers.append(int(m.group(1)))
assert len(answers) == len(rows), (len(answers), len(rows))

tally = collections.OrderedDict()
bad = []
for r, a in zip(rows, answers):
    key = (r['kind'], r['step'])
    t = tally.setdefault(key, [0, 0, collections.Counter()])
    t[0] += 1
    t[2][a] += 1
    if int(r['expected']) == a:
        t[1] += 1
    else:
        bad.append((r, a))
with open(os.path.join(OUT, 'checks_nissy.tsv'), 'w') as f:
    f.write('kind\tnissy_step\tpositions\tagree\tdistribution (nissy value: positions)\n')
    for (k, s), (tot, ok, dist) in tally.items():
        d = ' '.join(f'{v}:{dist[v]}' for v in sorted(dist))
        f.write(f'{k}\t{s}\t{tot}\t{ok}\t{d}\n')
        print(f'{k:7s} {s:12s} {ok}/{tot} agree   ({d})')
for r, a in bad[:10]:
    print('DISAGREE', r, 'nissy', a)
print('all agree' if not bad else f'{len(bad)} disagreements')
sys.exit(1 if bad else 0)
