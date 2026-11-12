#!/usr/bin/env python3
"""Replay, on the sticker model (cube.py), the solutions printed by `instools best` and by `instools sample`.

  check_solutions.py best <file>...      output of `instools best`: for every SOL line the insertions are carried out one
                                         after the other with cube.cancel, the lengths and cancellation counts are compared,
                                         and scramble + final solution must give the solved cube
  check_solutions.py sample <file>...    sample files: for every line that carries a solution, the scramble is rebuilt
                                         from skeleton and leftover (Z = c · S^-1) and Z + solution must be solved, and the
                                         solution's length minus the skeleton's must be the printed best cost
  check_solutions.py algs                a few named algorithms on the sticker model"""
import sys
import cube
from cubie import make, cubie, CNAMES, ENAMES

def moved(s):
    cp, ct, ep, ef = cubie(s)
    return ([CNAMES[i] for i in range(8) if cp[i] != i or ct[i]], [ENAMES[i] for i in range(12) if ep[i] != i or ef[i]])

def check_best(path):
    n_sol = 0; scr = skel = None
    for line in open(path):
        line = line.rstrip('\n')
        if line.startswith('scramble: '): scr = cube.parse(line[10:])
        elif line.startswith('skeleton: '): skel = cube.parse(line[10:].split(' (')[0])
        elif line.startswith('SOL\t'):
            _, case, L, model, cost, length, nested, insd, final = line.split('\t')
            cur = list(skel)
            for part in insd.split('|'):
                pos, alg, canc = part.split(':'); pos = int(pos); alg = cube.parse(alg)
                assert len(alg) <= int(L), (path, case, 'algorithm longer than the bound')
                assert cube.cancel(alg) == alg, (path, case, 'algorithm not reduced')
                new = cube.cancel(cur[:pos] + alg + cur[pos:])
                assert len(cur) + len(alg) - len(new) == int(canc), (path, case, model, 'cancelled count')
                cur = new
            final = cube.parse(final)
            assert cur == final, (path, case, model, 'final sequence')
            assert len(final) == int(length) and len(final) - len(skel) == int(cost), (path, case, model, 'length')
            assert cube.do(cube.SOLVED, scr + final) == cube.SOLVED, (path, case, model, 'does not solve the scramble')
            n_sol += 1
    print(f'{path}: {n_sol} printed solutions replayed on the sticker model: all solve their scramble with the printed length')

def check_sample(path):
    n = 0; rows = 0
    with open(path) as f:
        head = f.readline().rstrip('\n').split('\t')
        sol_cols = [i for i, h in enumerate(head) if h.endswith('_solution')]
        for line in f:
            p = line.rstrip('\n').split('\t'); rows += 1
            skel = cube.parse(p[1]); assert cube.cancel(skel) == skel
            for i in sol_cols:
                if p[i] == '-': continue
                cp, ct, ep, ef = [[int(x) for x in part.split(',')] for part in p[2].split(';')]
                c = make(cp, ct, ep, ef)
                z = cube.compose(c, cube.inverse(cube.do(cube.SOLVED, skel)))
                assert cube.compose(z, cube.do(cube.SOLVED, skel)) == c
                final = cube.parse(p[i]); assert cube.cancel(final) == final, 'solution not reduced'
                assert cube.compose(z, cube.do(cube.SOLVED, final)) == cube.SOLVED, (path, p[0], head[i], 'does not solve')
                best = p[head.index(head[i].replace('_solution', '_best'))]                                   # the L<l>_best column
                assert len(final) - len(skel) == int(best), (path, p[0], head[i], 'cost')
                n += 1
    print(f'{path}: {rows} lines, {n} solutions replayed on the sticker model: all solve and have the printed cost')
    return n

if __name__ == '__main__':
    mode = sys.argv[1]
    if mode == 'best':
        for f in sys.argv[2:]: check_best(f)
    elif mode == 'sample':
        tot = sum(check_sample(f) for f in sys.argv[2:])
        print('total solutions replayed:', tot)
    elif mode == 'algs':
        for alg in ["R U R' D R U' R' D'", "U L U' D F' D'", "R2 L2 U2 R2 L2 D2"] + sys.argv[2:]:
            s = cube.do(cube.SOLVED, alg); c, e = moved(s)
            print(f'{alg}  ({len(cube.parse(alg))} moves): corners touched {c or "none"}, edges touched {e or "none"}, order', end=' ')
            t = s; k = 1
            while t != cube.SOLVED: t = cube.compose(t, s); k += 1
            print(k)
