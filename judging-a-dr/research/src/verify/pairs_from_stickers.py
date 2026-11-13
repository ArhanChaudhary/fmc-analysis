#!/usr/bin/env python3
"""True pairs counted from the stickers (corner and edge next to each other in the U or D layer, top stickers and side
stickers both matching) on 2,000 random DR states, against drtools read.

  python3 research/src/verify/pairs_from_stickers.py"""
import sys, subprocess, random, re
sys.path.insert(0, '/data/fmc/judging-a-dr/research/tool'); import fmccube as fc
s0 = fc.solved(); k0 = next(iter(s0)); print('state key/value example:', k0, s0[k0])
def true_pairs(st):
    n = 0
    for y in (1, -1):
        for x in (1, -1):
            for z in (1, -1):
                c = (x, y, z)
                for e, side in (((x, y, 0), (x, 0, 0)), ((0, y, z), (0, 0, z))):
                    top = (0, y, 0)
                    if st[(c, top)] == st[(e, top)] and st[(c, side)] == st[(e, side)]: n += 1
    return n
random.seed(7); M = ["U", "U2", "U'", "D", "D2", "D'", "R2", "L2", "F2", "B2"]
scr = [' '.join(random.choice(M) for _ in range(random.randint(1, 30))) for _ in range(2000)]
sts = [fc.state_after(s) for s in scr]; mine = [true_pairs(s) for s in sts]
inp = ''.join(' '.join(map(str, sum(fc.to_dr_arrays(s), []))) + '\n' for s in sts)
out = subprocess.run(['/data/fmc/judging-a-dr/research/drtools/target/release/drtools', 'read', '/data/fmc/judging-a-dr/research/data/drbfs', '/data/fmc/judging-a-dr/research/data/ls_depth.u8'], input=inp, capture_output=True, text=True).stdout
theirs = [int(x) for x in re.findall(r'^true_pairs: (\d+)', out, re.M)]
print(len(mine), len(theirs), 'mismatches:', sum(a != b for a, b in zip(mine, theirs)), 'distribution', sorted(set(mine)))
