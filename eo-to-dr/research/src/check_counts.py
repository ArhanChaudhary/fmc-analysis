#!/usr/bin/env python3
"""Counts and NISS values of `eodrtools scr` against nissy 2.0.8 on the first scrambles of out/scrambles.txt.

  ndr_UD_L        nissy solve drud -a -c -m L -M L          (DR solutions on U/D of exactly L turns, normal side)
  neo_n_FB_L      nissy solve eofb -a -c -m L -M L          (linear EOs on F/B of exactly L turns)
  neo_{n,i,x}     nissy solve eofb -N -a -c -m L -M L       (NISS EOs: normal + inverse + both sides)
  d6              nissy solve dr -L                          (best of 3 axes x normal/inverse, linear)
  (nissy solve dr -N, the NISS DR, takes minutes per scramble; not run here: our NISS value is exact by the
  shorter-side argument and every NISS solution is replayed)
  nissy default   nissy solve eofb -c -m L -M L (no -a)     (recorded only: nissy drops EOs ending in F'/B')

usage: check_counts.py <scr.tsv> [n]       output: out/checks_counts.tsv"""
import csv, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, '..', 'out')
csv.field_size_limit(10**7)
n = int(sys.argv[2]) if len(sys.argv) > 2 else 30
rows = [r for _, r in zip(range(n), csv.DictReader(open(sys.argv[1]), delimiter='\t'))]
scr = [l.strip() for l in open(os.path.join(OUT, 'scrambles.txt')) if l.strip()][:n]
AX = ['RL', 'UD', 'FB']
jobs = []  # (label, command, expected or None)
for r, s in zip(rows, scr):
    for L in (9, 10):
        jobs.append((f'drud count L={L}', f'solve drud -a -c -m {L} -M {L} {s}', int(r[f'ndr_UD_{L}'])))
    for L in (4, 5, 6):
        jobs.append((f'eofb linear count L={L}', f'solve eofb -a -c -m {L} -M {L} {s}', int(r[f'neo_n_FB_{L}'])))
        jobs.append((f'eofb nissy-default count L={L}', f'solve eofb -c -m {L} -M {L} {s}', None))
    for L in (4, 5):
        jobs.append((f'eofb NISS count L={L}', f'solve eofb -N -a -c -m {L} -M {L} {s}', sum(int(r[f'neo_{k}_FB_{L}']) for k in 'nix')))
    jobs.append(('dr best of 6 (dr -L)', f'solve dr -L {s}', min(int(r[f'd_{side}_{a}']) for side in 'ni' for a in AX)))
res = subprocess.run(['nissy', '-b'], input=''.join(c + '\n' for _, c, _ in jobs), capture_output=True, text=True, check=True).stdout
lines = res.splitlines()
ans = []
for i, l in enumerate(lines):
    if l.startswith('>>> Executing command'):
        j = i + 1
        while lines[j].startswith('>>>'):
            j += 1
        m = re.search(r'\((\d+)\)\s*$', lines[j])
        ans.append(int(m.group(1)) if m else int(lines[j].strip()))
assert len(ans) == len(jobs)
tally = {}
default_ratio = {}
for (label, cmd, exp), a in zip(jobs, ans):
    t = tally.setdefault(label, [0, 0])
    t[0] += 1
    if exp is None:
        L = label.split('=')[1]
        default_ratio.setdefault(L, [0, 0])[0] += a
        continue
    if a == exp:
        t[1] += 1
    else:
        print('DISAGREE', label, cmd, 'ours', exp, 'nissy', a)
# the default/all ratio
lin = {}
for (label, cmd, exp), a in zip(jobs, ans):
    if label.startswith('eofb linear count'):
        lin.setdefault(label.split('=')[1], 0)
        lin[label.split('=')[1]] += a
with open(os.path.join(OUT, 'checks_counts.tsv'), 'w') as f:
    f.write('check\tscrambles\tagree\n')
    for label, (tot, ok) in tally.items():
        if 'default' in label:
            L = label.split('=')[1]
            f.write(f'{label}\t{tot}\tnot a check: nissy default lists {default_ratio[L][0]} EOs where -a lists {lin[L]}\n')
            print(f'{label}: nissy default {default_ratio[L][0]} vs -a {lin[L]}')
        else:
            f.write(f'{label}\t{tot}\t{ok}\n')
            print(f'{label}: {ok}/{tot} agree')
bad = [1 for label, (tot, ok) in tally.items() if 'default' not in label and ok != tot]
sys.exit(1 if bad else 0)
