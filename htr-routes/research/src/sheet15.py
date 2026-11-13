#!/usr/bin/env python3
"""Aedan Bryant's HTR Subset Stats (doc 15) as it stands in the knowledge base, read cell by cell.

Stats.csv: per row label (the sheet's own, "4qt 4C", "3qt 4E", ...) five length distributions over its 1,000 states
and their means: the optimal solution, the optimal "QT Break DR" solution (the DR plus one quarter turn that breaks
it), the optimal leave-slice solution, the shortest linear HTR (normal side) and the shortest NISS HTR.
Examples.csv: the QT-break solutions the sheet lists; they are counted here by whether they are "R or R', then DR
moves" (the reading where the extra move goes one way or the other and the finish stays in the DR group) or use
other moves, which shows the column was solved with any moves.

summary() is what xtables.py puts in out/report_extra.json (key d15x) and what claims.py quotes.
usage: sheet15.py   (prints the summary and writes out/sheet15.json)"""
import csv, re, json, os, sys
P = '/data/fmc/kb/docs/gsheet/17iChOoeB205t3wHTXMLrjM9si2vtxRgFeYR2z3pn1i0/'
COLS = (('Optimal Solution Length Distribution:', 'sol'), ('Optimal QT Break DR Solution Length Distribution:', 'qtbreak'),
        ('Optimal No E Solution Length Distribution:', 'noe'), ('Optimal Linear HTR Length Distribution:', 'lin'),
        ('Optimal NISS HTR Length Distribution:', 'niss'))

def rows():
    """label -> {'sol': {length: share}, 'mean_sol': x, 'qtbreak': ..., 'noe': ..., 'lin': ..., 'niss': ...}"""
    t = list(csv.reader(open(P + 'Stats.csv', errors='replace')))
    out = {}
    for ri, r in enumerate(t):
        for ci, cell in enumerate(r):
            if cell.strip() != COLS[0][0]: continue
            label = ' '.join(t[ri - 1][ci].split()); ent = {}
            for k, (head, key) in enumerate(COLS):
                assert r[ci + k].strip() == head, (label, head)
                dist = {}; mean = None
                for d in range(ri + 1, min(ri + 20, len(t))):
                    x = t[d][ci + k].strip() if ci + k < len(t[d]) else ''
                    m = re.match(r'^(\d+)\s+([\d.]+)%$', x)
                    if m: dist[m.group(1)] = float(m.group(2)) / 100
                    elif x.startswith('Mean:'): mean = float(x.split(':')[1]); break
                assert dist and mean is not None, (label, key)
                ent[key] = dist; ent['mean_' + key] = mean
            assert label not in out, label
            out[label] = ent
    return out

def qtbreak_solutions():
    """(QT-break solutions listed, how many are not "R or R', then DR moves")"""
    t = list(csv.reader(open(P + 'Examples.csv', errors='replace')))
    n = other = 0
    for ri, r in enumerate(t):
        for ci, cell in enumerate(r):
            if cell.strip() != 'QT Break DR Solution': continue
            for d in range(ri + 1, len(t)):
                x = t[d][ci].strip().replace('’', "'") if ci < len(t[d]) else ''
                mv = x.split()
                if not mv or not all(re.match(r"^[UDRLFB][2']?$", y) for y in mv): break
                n += 1
                other += mv[0] not in ('R', "R'") or any(y[0] in 'RLFB' and not y.endswith('2') for y in mv[1:])
    return n, other

def summary():
    s = rows(); n, other = qtbreak_solutions()
    ml = {k: max(int(x) for x in v['lin']) for k, v in s.items()}; top = max(ml.values())
    return dict(rows=s, n_rows=len(s), maxlin=top, maxlin_rows=[k for k, v in ml.items() if v == top],
                maxlin_elsewhere=max(v for v in ml.values() if v < top),
                maxniss=max(int(x) for v in s.values() for x in v['niss']),
                qtbreak_mean_diff=sum(v['mean_qtbreak'] - v['mean_sol'] for v in s.values()) / len(s),
                qtbreak_solutions=n, qtbreak_not_dr_moves=other)

if __name__ == '__main__':
    S = summary()
    out = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'out', 'sheet15.json'))
    json.dump(S, open(out, 'w'), indent=1)
    print({k: v for k, v in S.items() if k != 'rows'})
    for k in ('4qt 4C', '3qt 4E', '4qt 8E'): print(k, 'linear', S['rows'][k]['lin'], 'NISS', S['rows'][k]['niss'])
