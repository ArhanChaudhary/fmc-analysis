#!/usr/bin/env python3
"""Are the scrambles random states?  For each scramble file: replay on the sticker model and compare, on each of
the three axes, the number of twisted corners, of bad edges and of E-slice pieces in their slice with the exact
distribution for a uniformly random state (chi-square, bins with expected count >= 5).

Done because nissy 2.0.8's `scramble` (first used here, and by judging-a-dr's 500 scrambles) turned out not to be
uniform in corner orientation; the study's sample (out/scrambles.txt) is drawn by `eodrtools mkscr` instead.
Writes out/checks_scrambles.tsv.   usage: check_scrambles.py <name>=<file> ..."""
import os, sys, collections
from math import comb
import sticker, cube

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, '..', 'out')
corner_places = [i for i, (p, n) in enumerate(cube.ST) if all(x != 0 for x in p)]
exp_tw = collections.Counter()
for v in range(2187):
    t = [(v // 3 ** i) % 3 for i in range(7)]; t.append((-sum(t)) % 3)
    exp_tw[sum(x != 0 for x in t)] += 1
exp_tw = {k: v / 2187 for k, v in exp_tw.items()}
exp_bad = {b: comb(12, b) / 2048 for b in range(0, 13, 2)}
exp_sl = {k: comb(4, k) * comb(8, 4 - k) / 495 for k in range(5)}

def chi2(obs, exp, n):
    stat, df, acc_e, acc_o = 0.0, 0, 0.0, 0
    for k in sorted(exp):
        acc_e += exp[k] * n; acc_o += obs.get(k, 0)
        if acc_e >= 5:
            stat += (acc_o - acc_e) ** 2 / acc_e; df += 1; acc_e, acc_o = 0.0, 0
    return stat, df - 1

rows = []
for arg in sys.argv[1:]:
    name, path = arg.split('=')
    scr = [l.strip() for l in open(path) if l.strip() and not l.startswith('#')]
    for X in range(3):
        tw, bad, sl = collections.Counter(), collections.Counter(), collections.Counter()
        for s in scr:
            st = cube.do(cube.SOLVED, s)
            tw[sum(1 for i in corner_places if sticker.col_axis(st, i) == X and sticker.PLACE_AXIS[i] != X)] += 1
            bad[sticker.bad_edges(st, X)] += 1
            sl[sum(1 for p, ids in sticker.EDGES if p[X] == 0 and all(sticker.col_axis(st, i) != X for i in ids))] += 1
        for what, obs, exp in (('twisted corners', tw, exp_tw), ('bad edges', bad, exp_bad), ('slice pieces in slice', sl, exp_sl)):
            c, df = chi2(obs, exp, len(scr))
            rows.append((name, len(scr), 'RL UD FB'.split()[X], what, round(c, 1), df,
                         ' '.join(f'{k}:{obs.get(k, 0) / len(scr):.4f}/{exp[k]:.4f}' for k in sorted(exp))))
with open(os.path.join(OUT, 'checks_scrambles.tsv'), 'w') as f:
    f.write('scrambles\tn\taxis\twhat\tchi2\tdf\tobserved/expected share by value\n')
    for r in rows:
        f.write('\t'.join(map(str, r)) + '\n')
        print(*r[:6])
