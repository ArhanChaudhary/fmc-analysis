#!/usr/bin/env python3
"""Check a file written by `xstools attempts` against the sticker model: every route really ends on a DR-xs of the
stated class (on its side of the scramble), and every written solution solves the scramble in the stated number of
turns, which is never more than route + finish."""
import csv, sys, collections
import cube, fe
SCR = [l.strip() for l in open('/data/fmc/judging-a-dr/research/out/hand/attempt_scrambles.txt') if l.strip() and not l.startswith('#')]
def kinds_of(s):
    out = []
    for c in range(3):
        for f in range(3):
            g = fe.look(s, c, f)
            if g and len(set(g[1])) == 1: out.append((c, f, sum(g[0]), g[1][0]))
    return out
rows = list(csv.DictReader(open(sys.argv[1]), delimiter='\t'))
bad = 0
for r in rows:
    scr = SCR[int(r['scramble']) - 1]
    x = cube.do(cube.SOLVED, scr)
    side = cube.inverse(x) if r['side'] == '1' else x
    w = cube.do(side, r['moves'])
    ks = kinds_of(w)
    if r['class'] == '1': ok = any(c != f and n == 4 for c, f, n, b in ks)
    else: ok = any(c != f and n == 8 for c, f, n, b in ks)
    sol = cube.parse(r['solution'])
    ok2 = cube.do(x, sol) == cube.SOLVED and len(sol) == int(r['total']) and int(r['total']) <= int(r['length']) + int(r['finish'])
    assert len(cube.parse(r['moves'])) == int(r['length'])
    if not (ok and ok2): bad += 1; print('BAD', r['scramble'], r['side'], r['class'], r['moves'], '|', r['solution'], ok, ok2, ks)
print(len(rows), 'rows checked,', bad, 'bad')
