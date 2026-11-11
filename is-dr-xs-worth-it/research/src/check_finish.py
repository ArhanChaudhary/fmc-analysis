#!/usr/bin/env python3
"""Independent check of the Rust DR-1s finisher on a few dumped states: rebuild each state at the sticker level,
try every setup of at most 3 turns that keeps the DR-1s, do the slice turn, and ask judging-a-dr's `drtools query`
for the optimal finish of the DR that comes out.  The best total must equal the Rust column finish_setup3."""
import csv, itertools, subprocess, sys
import cube, fe, coords, export_cubie
R = '/data/fmc/judging-a-dr/research/'
cn = [export_cubie.name_of(p) for p in coords.CORNERS]; en = [export_cubie.name_of(p) for p in coords.EDGES]
ci = [next(i for i, x in enumerate(cn) if set(x) == set(n)) for n in 'UFR UFL UBL UBR DFR DFL DBL DBR'.split()]
ei = [next(i for i, x in enumerate(en) if set(x) == set(n)) for n in 'UF UL UB UR DF DL DB DR'.split()]
si = [next(i for i, x in enumerate(en) if set(x) == set(n)) for n in 'FR FL BL BR'.split()]
def dr_numbers(s):
    cp, ct, ep, ef = export_cubie.cubie(s)
    assert not any(ct) and not any(ef)
    return [ci.index(cp[i]) for i in ci] + [ei.index(ep[i]) for i in ei] + [si.index(ep[i]) for i in si]
def optimal(states):
    inp = '\n'.join(' '.join(map(str, dr_numbers(s))) for s in states) + '\n'
    out = subprocess.run([R + 'drtools/target/release/drtools', 'query', R + 'data/drbfs', R + 'data/tables'], input=inp, capture_output=True, text=True).stdout
    return [int(l.split('exact=')[1].split()[0]) for l in out.strip().split('\n')]
SETUP = ['F', 'F2', "F'", 'B', 'B2', "B'", 'U2', 'D2', 'R2', 'L2']
SLICES = ["R L'", "R' L", 'R L', "R' L'"]
rows = list(csv.DictReader(open('/data/fmc/is-dr-xs-worth-it/research/out/sample1s_test.tsv'), delimiter='\t'))
n = bad = 0
for r in rows:
    if r['finish_setup3'] == '99' or n >= int(sys.argv[1]) if len(sys.argv) > 1 else n >= 12: continue
    v = list(map(int, r['state'].split())); s = coords.make(v[0:8], v[8:16], v[16:28], v[28:40])
    assert fe.look(s, 1, 2) is not None and sum(fe.look(s, 1, 2)[0]) == 4
    cand = []
    for k in range(4):
        for seq in itertools.product(SETUP, repeat=k):
            if any(seq[i][0] == seq[i + 1][0] for i in range(k - 1)): continue
            t = cube.do(s, list(seq))
            for sl in SLICES:
                u = cube.do(t, sl); g = fe.look(u, 1, 1)
                if g and fe.is_dr((1, 1) + g): cand.append((k, u))
    opt = optimal([u for _, u in cand])
    best = min(k + 2 + d for (k, _), d in zip(cand, opt))
    n += 1; bad += best != int(r['finish_setup3'])
    print(r['subset'], 'rust', r['finish_setup3'], 'python', best, 'candidates', len(cand))
print(n, 'states checked,', bad, 'mismatches')
