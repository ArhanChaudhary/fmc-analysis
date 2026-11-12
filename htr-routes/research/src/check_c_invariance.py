#!/usr/bin/env python3
"""FakeMMAP's C (T11501/T11502): the middle block q_1 h_1 ... q_N of a finish h_0 q_1 h_1 ... q_N h_N is a linear HTR
of the state after h_0.  C (the subset's shortest linear HTR) bounds it only if the subset x bad-edge label does not
change when a half turn is applied after the scramble (and, for the record, before it).  Checked on the sticker model
(sticker.py, independent of the Rust code) on random DR states.  Output: out/checks/check_c_invariance.txt"""
import random, sys
from sticker import label, DRM, HALF, SOLVED
from cube import do
from common import OUT
random.seed(20261113)
n = int(sys.argv[1]) if len(sys.argv) > 1 else 3000
bad_after = bad_before = 0; seen = set()
for _ in range(n):
    scr = [random.choice(DRM) for _ in range(random.randint(8, 30))]
    lab = label(do(SOLVED, scr))
    seen.add(lab)
    for h in HALF:
        if label(do(SOLVED, scr + [h])) != lab: bad_after += 1
        if label(do(SOLVED, [h] + scr)) != lab: bad_before += 1
msg = (f'{n} random DR states x 6 half turns ({len(seen)} distinct labels seen): label changed by a half turn after the '
       f'scramble {bad_after} times, before it {bad_before} times\n')
open(f'{OUT}/checks/check_c_invariance.txt', 'w').write(msg); print(msg, end='')
