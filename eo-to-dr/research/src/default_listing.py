#!/usr/bin/env python3
"""What nissy's default listing keeps of a scramble's EOs, against `-a`, on the first scrambles of out/scrambles.txt.

Without `-a` nissy 2.0.8 lists an EO only if each side ends in a clockwise quarter turn, and, where a side's last two
turns are of opposite faces, both are clockwise quarter turns (src/steps.c, validate_singlecw_ending).  So of the
`-a` EOs that differ only in the direction of a last turn it keeps one: half of the one-sided EOs with a single last
turn, fewer of those ending in two opposite faces, and each side of a two-sided (NISS) EO is filtered on its own.
The EO counts quoted on the server (Cale's sheet of official scrambles) are of the default kind.

  normal    nissy solve eo [-a] -c -m 1 -M k <scramble>             EOs on the normal side, all three axes
  inverse   the same on the inverse scramble
  niss      nissy solve eo -N [-a] -c -m 1 -M k <scramble>          normal, inverse and two-sided together
  two-sided niss - normal - inverse

The `-a` counts are set next to the study's own (out/big/scr50k.tsv).  On F/B the two are equal scramble by scramble
(check_counts.py).  On the other two axes nissy writes two opposite faces in the other order (D before U where the
study writes U before D), so an EO such as `... D2 U` is one of nissy's and `... U2 D` one of the study's: single
scrambles differ by a few EOs, the totals by a fraction of a percent (recorded here, and required to be under 1%).
Writes out/default_listing.json: the totals over the scrambles, and the mean and median per scramble of the default
NISS listing.
usage: default_listing.py [n = 150]"""
import csv, json, os, re, statistics, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import sticker, cube

OUT = os.path.join(HERE, '..', 'out')
csv.field_size_limit(10**7)
n = int(sys.argv[1]) if len(sys.argv) > 1 else 150
AX = ['RL', 'UD', 'FB']
rows = [r for _, r in zip(range(n), csv.DictReader(open(os.path.join(OUT, 'big', 'scr50k.tsv')), delimiter='\t'))]
scr = [l.strip() for l in open(os.path.join(OUT, 'scrambles.txt')) if l.strip()][:n]
assert len(rows) == len(scr) == n
KINDS = (('normal', '', False), ('inverse', '', True), ('niss', '-N ', False))
jobs = []          # (scramble index, k, kind, 'default' or 'all')
cmds = []
for i, s in enumerate(scr):
    inv = ' '.join(cube.inv_seq(s))
    for k in (4, 5):
        for kind, flag, on_inverse in KINDS:
            for which, a in (('default', ''), ('all', '-a ')):
                jobs.append((i, k, kind, which))
                cmds.append(f'solve eo {flag}{a}-c -m 1 -M {k} {inv if on_inverse else s}')
res = subprocess.run(['nissy', '-b'], input=''.join(c + '\n' for c in cmds), capture_output=True, text=True, check=True).stdout
lines = res.splitlines(); ans = []
for j, l in enumerate(lines):
    if l.startswith('>>> Executing command'):
        t = j + 1
        while lines[t].startswith('>>>'):
            t += 1
        m = re.search(r'\((\d+)\)\s*$', lines[t])
        ans.append(int(m.group(1)) if m else int(lines[t].strip()))
assert len(ans) == len(jobs), (len(ans), len(jobs))
cnt = {j: a for j, a in zip(jobs, ans)}
# the -a counts next to the study's own
ours = lambda r, kinds, k: sum(int(r[f'neo_{c}_{a}_{l}']) for c in kinds for a in AX for l in range(1, k + 1))
OURS = {'normal': 'n', 'inverse': 'i', 'niss': 'nix'}
out = {'scrambles': n}
for k in (4, 5):
    d = {}
    for kind in ('normal', 'inverse', 'niss'):
        d[kind] = {w: sum(cnt[(i, k, kind, w)] for i in range(n)) for w in ('default', 'all')}
        d[kind]['all_study'] = sum(ours(r, OURS[kind], k) for r in rows)
        d[kind]['scrambles_equal_to_study'] = sum(cnt[(i, k, kind, 'all')] == ours(r, OURS[kind], k) for i, r in enumerate(rows))
        assert abs(d[kind]['all'] - d[kind]['all_study']) < 0.01 * d[kind]['all_study'], (kind, k, d[kind])
    d['one_sided'] = {w: d['normal'][w] + d['inverse'][w] for w in ('default', 'all')}
    d['two_sided'] = {w: d['niss'][w] - d['one_sided'][w] for w in ('default', 'all')}
    per = [cnt[(i, k, 'niss', 'default')] for i in range(n)]
    d['niss_default_per_scramble'] = {'mean': sum(per) / n, 'median': statistics.median(per), 'none': sum(1 for x in per if x == 0)}
    pera = [cnt[(i, k, 'niss', 'all')] for i in range(n)]
    d['niss_all_per_scramble'] = {'mean': sum(pera) / n, 'median': statistics.median(pera)}
    out[f'le{k}'] = d
    print(f'at most {k}: ' + '; '.join(f"{kind} {d[kind]['default']} of {d[kind]['all']} ({d[kind]['default'] / d[kind]['all']:.1%})" for kind in ('normal', 'inverse', 'one_sided', 'two_sided', 'niss'))
          + f"; default NISS listing per scramble: mean {sum(per) / n:.1f}, median {statistics.median(per)}")
json.dump(out, open(os.path.join(OUT, 'default_listing.json'), 'w'), indent=1)
print(f"out/default_listing.json: {n} scrambles; -a totals against the study's: " + '; '.join(
    f"at most {k} {kind} {out[f'le{k}'][kind]['all']} / {out[f'le{k}'][kind]['all_study']} ({out[f'le{k}'][kind]['scrambles_equal_to_study']} scrambles equal)" for k in (4, 5) for kind in ('normal', 'inverse', 'niss')))
