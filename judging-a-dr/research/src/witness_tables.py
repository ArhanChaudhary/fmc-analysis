#!/usr/bin/env python3
"""Markdown tables of explicit witnesses for the report, from out/witnesses.txt (every scramble there has been
re-read by verify_witnesses.py)."""
import re
L = open('/data/fmc/judging-a-dr/research/out/witnesses.txt').read().split('\n')
W = {}
for i, l in enumerate(L):
    m = re.match(r'^\s*(.+?) :: ([UDRLFB2\' ]*)$', l)
    if m and i + 1 < len(L) and L[i + 1].strip().startswith('subset'):
        d = L[i + 1]
        W[m.group(1).strip()] = dict(scr=m.group(2).strip(), sub=re.search(r'subset (\S+ \S+)', d).group(1), opt=int(re.search(r'optimal (\d+)', d).group(1)),
                                     fin=re.search(r'optimal \d+ \(([^)]*)\)', d).group(1), htr=re.search(r'HTR (\d+) / (\d+)', d).groups(),
                                     bound=int(re.search(r'setup\+HTR bound (\d+)', d).group(1)), qt=int(re.search(r'qt (\d+)', d).group(1)))
order = lambda s: (int(s.split()[0][-1]), s.split()[0], int(s.split()[1][0]))
subs = sorted({w['sub'] for k, w in W.items() if k.endswith('longest')}, key=order)
out = ['| Subset | A longest one | Its optimal, moves | One that finishes in exactly its longer HTR | Its shortest HTR, normal | Its shortest HTR, inverse | Its optimal, moves |', '|---|---|---:|---|---:|---:|---:|']
for s in subs:
    a, b = W[f'{s} longest'], W[f'{s} optimal equal to the longer HTR']
    out.append(f"| {s} | `{a['scr']}` | {a['opt']} | `{b['scr'] or '(solved)'}` | {b['htr'][0]} | {b['htr'][1]} | {b['opt']} |")
open('/data/fmc/judging-a-dr/report/data/witnesses_by_subset.md', 'w').write('\n'.join(out) + '\n')
out = ['| Subset | Scramble | Setup + HTR bound | Optimal finish | Its length | Quarter turns in it | Fewest the subset needs |', '|---|---|---:|---|---:|---:|---:|']
for s in subs:
    k = f'{s} optimal below the setup+HTR bound'
    if k in W:
        w = W[k]; nq = sum(1 for m in w['fin'].split() if m in ("U", "U'", "D", "D'"))
        out.append(f"| {s} | `{w['scr']}` | {w['bound']} | `{w['fin']}` | {w['opt']} | {nq} | {w['qt']} |")
open('/data/fmc/judging-a-dr/report/data/setup_bound_examples.md', 'w').write('\n'.join(out) + '\n')
print('\n'.join(out))
for k in ['0c0 2e shortest', '0c0 6e shortest', '4a1 2e shortest', '4a1 0e shortest', '0c0 8e longest', '0c3 4e longest', '2c5 0e longest', '2c5 4e longest', '4b2 4e longest', '2c3 4e longest', '4a1 4e longest']:
    w = W[k]; print(f"{k}: `{w['scr']}` optimal {w['opt']} ({w['fin']}) qt_min {w['qt']} HTR {w['htr']}")
