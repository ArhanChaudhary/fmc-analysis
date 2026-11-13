#!/usr/bin/env python3
"""Replayed examples for "Edge paths of the finish" (section 4): one 2c4 2e DR of the sample that has two optimal
finishes with different edge paths, 2c4 2e > 2c3 2e > 4b2 2e > 4a1 4e > HTR and 2c4 2e > 2c3 4e > 4b2 2e > 4a1 4e > HTR.
The finishes come from `htrtools trace` (every optimal finish); each is replayed on the sticker model, its edge path
read there (labels at the start and after each quarter turn up to HTR), and its length checked against nissy's optimum.
Output: out/edge_paths_witness.json (scramble, optimum, per form: finish, the moves split at each quarter turn with
the label reached, HTR length).
usage: edge_paths_witness.py <ep dir> <states dir> <htrtools> <exact.u8> [out.json]"""
import sys, os, json, subprocess, csv, re
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import sticker
from sticker import do, SOLVED, inv_seq, QT
EPD, STD, TOOL, EXACT = sys.argv[1:5]
OUTF = sys.argv[5] if len(sys.argv) > 5 else os.path.join(HERE, '..', 'out', 'edge_paths_witness.json')
WANT = ['2c4 2e > 2c3 2e > 4b2 2e > 4a1 4e > 0c0 0e', '2c4 2e > 2c3 4e > 4b2 2e > 4a1 4e > 0c0 0e']
K = {}
for l in list(open(f'{EPD}/ep_keys.tsv'))[1:]:
    i, p = l.rstrip('\n').split('\t'); K[p] = int(i)
ids = [K[w] for w in WANT]
states = {int(r['idx']): r for r in csv.DictReader(open(f'{STD}/states_2c4_2e.tsv'), delimiter='\t')}
pick = None
for l in list(open(f'{EPD}/ep_2c4_2e.tsv'))[1:]:
    v = l.rstrip('\n').split('\t')
    opt = {int(x.split(':')[0]) for x in v[4:] if x.split(':')[1] == '0'}
    if all(i in opt for i in ids) and int(v[1]) <= 12 and int(v[3]) <= 6:     # short, few optimal finishes
        pick = int(v[0]); break
r = states[pick]
p = subprocess.run([TOOL, 'trace', EXACT, '0'], input=f"#{r['c']},{r['e']},{r['s']}\n", capture_output=True, text=True, check=True)
j = json.loads(p.stdout)
scr = ' '.join(inv_seq(j['all'][0]))
X = do(SOLVED, scr)
assert sticker.label(X) == '2c4 2e'
env = dict(os.environ, NISSYDATA='/data/fmc/tools/nissy-data')
ns = subprocess.run(['/data/fmc/tools/nissy-2.0.8/nissy'], input=f'solve drudfin -o -a {scr}\n', capture_output=True, text=True, env=env).stdout
lens = {int(x) for x in re.findall(r'\((\d+)\)\s*$', ns, re.M)}
assert lens == {j['d']}, (lens, j['d'])
out = {'state': f"2c4 2e, sample index {pick}", 'scramble': scr, 'optimal': j['d'], 'optimal_finishes': len(j['all']), 'forms': []}
for w in WANT:
    for f in j['all']:
        mv = f.split(); st = X; labs = [sticker.label(st)]; steps = []; cur = []; h = None
        for i, m in enumerate(mv):
            st = do(st, m); cur.append(m)
            if m in QT:
                labs.append(sticker.label(st)); steps.append({'moves': ' '.join(cur), 'reaches': 'HTR' if sticker.in_htr(st) else labs[-1]}); cur = []
                if sticker.in_htr(st): h = i + 1; break
        if ' > '.join(labs) == w:
            assert do(X, mv) == SOLVED and len(mv) == j['d']
            rest = mv[h:]
            out['forms'].append({'form': ' > '.join(labs[:-1] + ['HTR']), 'finish': f, 'steps': steps,
                                 'after_htr': ' '.join(rest), 'htr_length': h})
            break
assert len(out['forms']) == 2
json.dump(out, open(OUTF, 'w'), indent=1)
print(json.dumps(out, indent=1))
