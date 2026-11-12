#!/usr/bin/env python3
"""Printed scrambles: adjacent turns of the same face merged (`U2 R2 R' B'` -> `U2 R B'`), repeatedly, so no printed
sequence has two turns of one face in a row.  The study's scrambles are written as a DR path followed by a DR finish,
and the join can put two turns of one face next to each other."""
AMOUNT = {'': 1, '2': 2, "'": 3}
NAME = {1: '', 2: '2', 3: "'"}
def simplify(seq):
    out = []
    for m in seq.split():
        f, a = m[0], AMOUNT[m[1:]]
        if out and out[-1][0] == f:
            s = (out[-1][1] + a) % 4
            out.pop()
            if s:
                out.append((f, s))
        else:
            out.append((f, a))
    return ' '.join(f + NAME[a] for f, a in out)
