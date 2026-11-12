#!/usr/bin/env python3
"""Write out/tables/cubie.txt for the Rust crate: the 18 face turns and the 24 whole-cube rotations as maps on corner
and edge places with their twist / flip changes, the place names, and test vectors (states, rotated states, inverses,
and `cancel`).  Everything is computed from the sticker model (cube.py)."""
import random, os
import cube
from cubie import CF, EF, CNAMES, ENAMES, NAMES, as_map, cubie, make, rotations, conj

OUT = '/data/fmc/insertion-cost/research/out/tables'
if __name__ == '__main__':
    random.seed(11)
    L = ['moves']
    for nm in NAMES:
        cd, ca, ed, ea = as_map(cube.MOVES[nm]); L.append(' '.join(map(str, cd + ca + ed + ea)))
    rots = rotations()
    L.append('rotations')
    for R, nm in rots:
        cd, ca, ed, ea = as_map(R)
        fm = []
        for fc in 'UDRLFB':                      # where each face goes
            a, sg = cube.AX[fc]
            i = next(k for k, (p, n) in enumerate(cube.ST) if sum(abs(v) for v in p) == 1 and n[a] == sg)
            fm.append('UDRLFB'.index(cube.FACE_OF[R[i]]))
        L.append(' '.join(map(str, cd + ca + ed + ea + fm)))
    L.append('names'); L.append(' '.join(CNAMES)); L.append(' '.join(ENAMES))
    L.append('tests')
    for _ in range(200):
        seq = [random.choice(NAMES) for _ in range(random.randint(1, 30))]; s = cube.do(cube.SOLVED, seq)
        cp, ct, ep, ef = cubie(s); assert make(cp, ct, ep, ef) == s
        r = random.randrange(24); cc = cubie(conj(s, rots[r][0])); inv = cubie(cube.inverse(s))
        L.append(' '.join(str(NAMES.index(m)) for m in seq) + ' | ' + ' '.join(map(str, cp + ct + ep + ef)) + f' | {r} | '
                 + ' '.join(map(str, cc[0] + cc[1] + cc[2] + cc[3])) + ' | ' + ' '.join(map(str, inv[0] + inv[1] + inv[2] + inv[3])))
    L.append('cancel')
    for k in range(600):
        pool = NAMES if k % 3 == 0 else [m for m in NAMES if m[0] in random.choice(['UD', 'UDR', 'RLF', 'UDRL', 'FB'])]
        seq = [random.choice(pool) for _ in range(random.randint(0, 30))]; c = cube.cancel(seq)
        assert cube.do(cube.SOLVED, seq) == cube.do(cube.SOLVED, c)
        L.append(' '.join(str(NAMES.index(m)) for m in seq) + ' | ' + ' '.join(str(NAMES.index(m)) for m in c))
    os.makedirs(OUT, exist_ok=True)
    open(OUT + '/cubie.txt', 'w').write('\n'.join(L) + '\n')
    print('corner places:', ' '.join(CNAMES)); print('edge places:', ' '.join(ENAMES))
    print('rotations:', [nm or 'id' for _, nm in rots])
    print('wrote cubie.txt,', len(L), 'lines')
