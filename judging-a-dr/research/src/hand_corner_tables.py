#!/usr/bin/env python3
"""Corner-case tables (markdown): finish by corner case on the normal side, and on both sides."""
import csv, collections, math, sys
sys.path.insert(0, '/data/fmc/judging-a-dr/research/src')
from hand_kill import load
def st(h):
    n = sum(h); return n, sum(d*c for d, c in enumerate(h))/n
def P(h, T): return 100*sum(h[:T+1])/sum(h)
import pv
ODDS_HEAD = 'In 10 | In 11 | In 12 | In 13'
def odds(h): return pv.cells(h)
POS = ['UFR', 'UFL', 'UBL', 'UBR', 'DFR', 'DFL', 'DBL', 'DBR']
ADJ_U = {(0, 1), (1, 2), (2, 3), (0, 3)}
def layout(mask):
    bad = [p for p in range(8) if mask >> p & 1]
    u = [p for p in bad if p < 4]; d = [p - 4 for p in bad if p >= 4]
    def shape(x):
        if len(x) == 2: return 'adjacent' if tuple(sorted(x)) in ADJ_U else 'diagonal'
        return ''
    if not bad: return 'none bad'
    if len(bad) == 2:
        if len(u) == 1: return '1 up 1 down, stacked' if u[0] == d[0] else ('1 up 1 down, across a face' if (min(u[0], d[0]), max(u[0], d[0])) in ADJ_U else '1 up 1 down, opposite')
        return 'both on one layer, ' + shape(u or d)
    if len(bad) == 4:
        if len(u) in (0, 4): return '4-0'
        if len(u) in (1, 3): return '3-1'
        su, sd = shape(u), shape(d)
        if su == sd == 'adjacent':
            return '2-2, pairs stacked' if set(u) == set(d) else ('2-2, pairs on opposite sides' if not set(u) & set(d) else '2-2, pairs sharing one column')
        return f'2-2, {su} over {sd}'
    return f'{len(bad)} bad'
cc = {r[0]: r for r in load('corner_cases.csv')[1]}   # id -> row
import re as _re
_W = open('/data/fmc/judging-a-dr/research/out/witnesses.txt').read().split('\n')
TYP = {}
for _i, _l in enumerate(_W):
    _m = _re.match(r'^corner case (\d+) typical :: (.*)$', _l)
    if _m: TYP[_m.group(1)] = (_m.group(2).strip() or '(solved)', int(_re.search(r'optimal (\d+)', _W[_i + 1]).group(1)))
NAME = {}
# Cases that have the same bad corners and the same answer to "a qt takes it straight to".
# 8 / 7: separated by a colour test on the face opposite the bad corners (research/src/corner_tell.py).
# 25 / 21 and 11 / 13: no visible test found; their corner solutions are one move apart.
TELL = {
    '8': 'the two diagonals of the back face agree (see the note under the table)',
    '7': 'the two diagonals of the back face differ (see the note under the table)',
    '25': 'looks the same as the 3-1 case with L 5–8. Only the corner solution separates them: L = 4 is this one',
    '21': 'looks the same as the 3-1 case with L 4–7. Only the corner solution separates them: L = 8 is this one',
    '11': 'looks the same as the 4-0 case with L 9–10. Only the corner solution separates them: L = 8 is this one',
    '13': 'looks the same as the 4-0 case with L 8–9. Only the corner solution separates them: L = 10 is this one',
}
BACK_FACE_NOTE = ("**Telling the two look-alike 2c4 cases apart.** Hold the cube so the two bad corners are on the front edge of one layer "
    "(if you see six bad corners, turn both layers, U D', and you will see two). The four corners of the back face are then all good. "
    "Take each diagonal of the back face. Its two corners share exactly one colour: their sticker on the back face, their U/D sticker, "
    "or their sticker on the side. If both diagonals share the same kind of sticker, the diagonals agree; otherwise they differ.")
def label(k):
    r = cc[k]; return f'{NAME[k]} ({layout(int(r[2]))}, L {r[5]}–{r[6]})'
k1 = load('k1_corner_cases.csv')[1]
one = collections.defaultdict(lambda: collections.defaultdict(lambda: [0]*19))
two = collections.defaultdict(lambda: collections.defaultdict(lambda: [0]*19))
for s, a, b, d, c in k1:
    cs = cc[a][1][:1] + ('c' if cc[a][1][1] in 'ab' and cc[a][1][2] in '345' else cc[a][1][1]) + cc[a][1][2]   # 4a3/4b3 -> 4c3 etc.
    one[s.split()[0]][a][int(d)] += int(c); two[s.split()[0]][tuple(sorted((a, b), key=int))][int(d)] += int(c)
out = []
for cs in ['0c0', '4a1', '4a2', '4b2', '0c3', '2c3', '4c3', '0c4', '2c4', '4c4', '2c5', '4b5']:
    tot = sum(sum(h) for h in one[cs].values())
    rows = sorted(one[cs].items(), key=lambda kv: st(kv[1])[1])
    for i, (k, h) in enumerate(rows): NAME[k] = f'{cs}-{i+1}'
    out.append(f'\n**{cs}**. Each row is one corner case: what it looks like.\n\n| Case | Bad corners | L | A qt takes it straight to | Told apart from a look-alike by |\n|---|---|---|---|---|')
    for k, h in rows:
        out.append(f'| {NAME[k]} | {layout(int(cc[k][2]))} | {cc[k][5]}–{cc[k][6]} | {cc[k][10] or "nothing, needs a setup"} | {TELL.get(k, '')} |')
    out.append(f'\nThe same cases with a typical DR and the shortest setup of their corners:\n\n| Case | A typical DR | Its optimal, moves | Shortest setup of these corners |\n|---|---|---:|---|')
    for k, h in rows:
        out.append(f'| {NAME[k]} | `{TYP[k][0]}` | {TYP[k][1]} | {('`' + cc[k][9] + '`') if cc[k][9] else 'none needed'} |')
    out.append(f'\nHow each case finishes: its share of {cs}, its average optimal, and the share finishing in 10, 11, 12 and 13 or less.\n\n| Case | Share of the subset | Average optimal, moves | {ODDS_HEAD} |\n|---|---:|---:|---:|---:|---:|---:|')
    for k, h in rows:
        out.append(f'| {NAME[k]} | {pv.hu(100*sum(h)/tot, 1):.1f}% | {pv.hu(st(h)[1], 2):.2f} | {odds(h)} |')
    if cs == '2c4':
        out.append('\n' + BACK_FACE_NOTE)
    if len(one[cs]) > 1:
        out.append(f'\n{cs}, corner case on both sides. Each row is a pair of cases, one on normal and one on inverse, in either order:\n\n| Cases on the two sides | Share of the subset | Average optimal, moves | {ODDS_HEAD} |\n|---|---:|---:|---:|---:|---:|---:|')
        for k, h in sorted(two[cs].items(), key=lambda kv: st(kv[1])[1]):
            out.append(f'| {NAME[k[0]]} and {NAME[k[1]]} | {pv.hu(100*sum(h)/tot, 1):.1f}% | {pv.hu(st(h)[1], 2):.2f} | {odds(h)} |')
open('/data/fmc/judging-a-dr/report/data/corner_cases.md', 'w').write('\n'.join(out) + '\n')
print(len(out), 'lines')
