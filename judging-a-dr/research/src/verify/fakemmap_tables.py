#!/usr/bin/env python3
"""FakeMMAP's two HTR-breaking tables (6 Sep and 7 Sep 2026 attachments), cell by cell against the any-move column of
Appendix C as printed in report/WRITEUP.md.  Own parser of the CSV grids.

  python3 research/src/verify/fakemmap_tables.py > research/out/verify/fakemmap_tables.txt"""
import csv, re, collections
A = '/data/fmc/assets/attachments/'
def grid(fn):
    rows = [[c.strip() for c in r] for r in csv.reader(open(A + fn))]
    g = {}
    for i, r in enumerate(rows):
        for j in range(len(r) - 1):
            if re.fullmatch(r'[HDRFV]-[HDV] [+-]', r[j]) and r[j + 1] in ('even', 'odd'):
                cols = rows[i + 1][j + 1:j + 4]
                for k in range(3):
                    rr = rows[i + 2 + k]; f = rr[j]
                    for t, c in enumerate(cols):
                        if rr[j + 1 + t] != '': g[(r[j], f, c, r[j + 1])] = int(float(rr[j + 1 + t]))
    return g
g7 = grid('1546599572644696075_0_RK_OBL_table_DS_2e.csv'); g6 = grid('1546263650015256606_0_RK_OBL_table_HTR_breaking.csv')
W = open('/data/fmc/judging-a-dr/report/WRITEUP.md').read().split('\n')
i = [k for k, l in enumerate(W) if l.startswith('| Corners | M-slice edges (F)')][0]
app = {}
for l in W[i + 2:]:
    if not l.startswith('|'): break
    c = [x.strip() for x in l.strip('|').split('|')]
    app[(c[0], c[1], c[2], c[3])] = (int(c[4]), int(c[5]), int(c[6]))
print('cells: 7 Sep', len(g7), '6 Sep', len(g6), 'appendix C', len(app))
cmp = collections.Counter(); hi = []
for k, v in g7.items():
    am = app[k][2]; cmp[v - am] += 1
    if v != am: hi.append((k, v, am, g6[k]))
print('7 Sep table minus any-move optimum:', dict(cmp))
for x in hi: print('  ', x, '(6 Sep value', x[3], ')')
print('7 Sep cells with 8/9/10 whose optimum is 7:', [k for k, v in g7.items() if v in (8, 9, 10) and app[k][2] == 7])
c6 = collections.Counter(v - app[k][2] for k, v in g6.items()); print('6 Sep table minus any-move optimum:', dict(c6))
print('6 Sep: values <= 7 that are not optimal:', [(k, v, app[k][2]) for k, v in g6.items() if v <= 7 and v != app[k][2]])
print('6 Sep: 8/9/10 cells whose optimum is 7 or less:', len([k for k, v in g6.items() if v in (8, 9, 10) and app[k][2] <= 7]))
print('any move vs DR move vs HT (appendix C):', collections.Counter(a[1] - a[2] for a in app.values()), collections.Counter(a[0] - a[2] for a in app.values()))
