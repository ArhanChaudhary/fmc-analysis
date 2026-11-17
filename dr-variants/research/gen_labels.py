#!/usr/bin/env python3
"""The 216 NISS@1qt cases of Rodney Kinney's sheet "Adv DR Bounding" (tab "Optimals (Advanced)") as HTR states.

Each row's setup alg is applied to a solved cube; the resulting HTR state is written as DR arrays (piece at each
position: 8 corners, 8 U/D edges, 4 E-slice edges) together with the row's labels.  The Rust tool maps every HTR
state to one of these rows through its KF class (judging-a-dr's quotient whose classes are exactly the 216 cases)."""
import csv, sys
sys.path.insert(0, '/data/fmc/judging-a-dr/research/tool'); import fmccube as fc
SRC = '/data/fmc/kb/docs/gsheet/1jRvikzLlm3yHlDQmQ0DLyj3Aw6uinL3Oa-U9_U7R5mY/Optimals_Advanced_.csv'
KIND = {'H-H': 0, 'R-D': 1, 'F-D': 2, 'R-V': 3, 'F-V': 4, 'D-D': 5}
ET = {'H': 0, 'D': 1, 'V': 2}
rows = [r for r in csv.reader(open(SRC))][1:]
out = open('data/cases216.tsv', 'w')
n = 0
for r in rows:
    if len(r) < 11 or not r[0]: continue
    if r[:4] == ['F-V', 'F-D', 'R-H', "M R2 U2 M'"]:
        # known typo (judging-a-dr section 10): this alg gives R-V + F-D R-V; M F2 U2 M' is the labelled case
        r[3] = "M F2 U2 M'"
    a = fc.to_dr_arrays(fc.state_after(r[3]))
    if a is None:   # an E2 or M/S move left the side centres turned: look at the same cube with centres home
        for rot in ('y2', 'y', "y'", 'x2', 'z2'):
            a = fc.to_dr_arrays(fc.state_after(r[3] + ' ' + rot))
            if a is not None: print('re-oriented with', rot, ':', r[:4]); break
    assert a is not None, r
    vals = [KIND[r[0]], ET[r[1][-1]], ET[r[2][-1]], int(float(r[5])), int(float(r[6])), int(float(r[7])), int(float(r[8])),
            int(float(r[9])), int(float(r[10])), int(float(r[4]))]
    out.write('\t'.join(map(str, vals + list(a[0]) + list(a[1]) + list(a[2]))) + '\t' + r[3] + '\n'); n += 1
print('rows', n)
