#!/usr/bin/env python3
"""An independent enumeration, on the sticker model and in Python, of all reduced sequences of length <= 8 with a given
product, compared with the lists of `instools` (subcommand `list`).

Meet in the middle with a dictionary of sticker states: for every reduced sequence B of length floor(l/2), the state
g · B^-1 is looked up among the states of the reduced sequences A of length ceil(l/2); A + B is kept when it is reduced.
The elements tested: for each class of 3c and 3e (and 2e2e, 5e) that has a sequence of length <= 8, the element of its
shortest sequence conjugated by a random setup of one or two moves."""
import random, subprocess, sys, collections
import cube
from cubie import cubie, NAMES
B = '/data/fmc/insertion-cost/research/instools/target/release/instools'
OUT = '/data/fmc/insertion-cost/research/out'
AXF = {'U': 0, 'D': 0, 'R': 1, 'L': 1, 'F': 2, 'B': 2}; FIRST = 'URF'
def follows(a, b): return a[0] != b[0] and not (AXF[a[0]] == AXF[b[0]] and a[0] not in FIRST)
def level(k):
    out = [((), cube.SOLVED)]
    for _ in range(k):
        out = [(s + (m,), cube.apply(st, cube.MOVES[m])) for s, st in out for m in NAMES if not s or follows(s[-1], m)]
    return out
def main(per_family=6, L=8):
    random.seed(3)
    levels = [level(k) for k in range(L // 2 + 1)]
    index = []
    for lv in levels:
        d = collections.defaultdict(list)
        for s, st in lv: d[st].append(s)
        index.append(d)
    inv_states = [[(s, cube.inverse(st)) for s, st in lv] for lv in levels]
    total = 0; n = 0
    for fam in ('3c', '3e', '2e2e', '5e'):
        rows = [l.rstrip('\n').split('\t') for l in open(f'{OUT}/cases_{fam}_L{L}.tsv')][1:]
        rows = [r for r in rows if r[1] != '-']
        for r in random.sample(rows, min(per_family, len(rows))):
            setup = [random.choice(NAMES) for _ in range(random.randint(1, 2))]
            g = cube.do(cube.SOLVED, setup + cube.parse(r[1]) + cube.inv_seq(setup))
            found = set()
            for l in range(1, L + 1):
                ka, kb = (l + 1) // 2, l // 2
                for sb, bi in inv_states[kb]:
                    for sa in index[ka].get(cube.compose(g, bi), ()):
                        if not sb or follows(sa[-1], sb[0]): found.add(' '.join(sa + sb))
            cp, ct, ep, ef = cubie(g)
            txt = ';'.join(','.join(map(str, v)) for v in (cp, ct, ep, ef))
            have = set(subprocess.run([B, 'list', txt, str(L)], capture_output=True, text=True, check=True).stdout.split('\n')) - {''}
            assert found == have, (fam, r[1], setup, len(found), len(have))
            assert all(cube.do(cube.SOLVED, a) == g for a in found)
            total += len(found); n += 1
            print(f'  {fam}: {" ".join(setup)} [{r[1]}] undo: {len(found)} sequences of length <= {L}, same set from instools', flush=True)
    print(f'sticker-model enumeration: {n} elements, {total} sequences, all lists identical to those of instools (L = {L})')
if __name__ == '__main__':
    main(*map(int, sys.argv[1:]))
