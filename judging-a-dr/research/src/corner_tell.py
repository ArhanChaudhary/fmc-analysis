#!/usr/bin/env python3
"""What visibly separates corner cases that have the same bad corners?  Brute force over colour relations.

Two corners of the same tetrad share exactly one colour axis (U/D, F/B or R/L).  For every pair of positions
of one tetrad that currently holds two pieces of one tetrad, record which axis those pieces share.  Then look
for the smallest set of such pairs whose values never coincide between two look-alike cases (over every state
of both cases, turned so that the bad corners sit in the same places)."""
import csv, collections, itertools, sys
rows = list(csv.reader(open('/data/fmc/judging-a-dr/research/out/hand/corner_perm_cases.csv')))[1:]
NAME = ['UFR', 'UFL', 'UBL', 'UBR', 'DFR', 'DFL', 'DBL', 'DBR']
COL = [n for n in NAME]
TET = [0, 1, 0, 1, 1, 0, 1, 0]
AX = ['U/D', 'F/B', 'R/L']
def shared(a, b):
    s = [ax for ax in range(3) if NAME[a][ax] == NAME[b][ax]]
    assert len(s) == 1; return s[0]
Y = [1, 2, 3, 0, 5, 6, 7, 4]; X2 = [7, 6, 5, 4, 3, 2, 1, 0]; M = [1, 0, 3, 2, 5, 4, 7, 6]
def compose(a, b): return [b[a[p]] for p in range(8)]
SYMS = []
for mir in range(2):
    for x2 in range(2):
        for yp in range(4):
            t = list(range(8))
            if mir: t = compose(t, M)
            if x2: t = compose(t, X2)
            for _ in range(yp): t = compose(t, Y)
            SYMS.append(t)
def conj(perm, t):
    new = [0] * 8
    for p in range(8): new[t[p]] = t[perm[p]]
    return new
def badset(perm): return frozenset(p for p in range(8) if TET[perm[p]] != TET[p])
PAIRS = [(a, b) for tet in (0, 1) for a, b in itertools.combinations([p for p in range(8) if TET[p] == tet], 2)]
bycase = collections.defaultdict(list)
for perm, case in rows: bycase[case].append([int(ch) for ch in perm])
def variants(case, target):
    out = []
    for perm in bycase[case]:
        for t in SYMS:
            q = conj(perm, t)
            if badset(q) == target: out.append(q)
    return out
def feat(perm, pair):
    x, y = perm[pair[0]], perm[pair[1]]
    return AX[shared(x, y)] if TET[x] == TET[y] else '-'
for group in sys.argv[1:]:
    cases = group.split(',')
    target = min((badset(conj(bycase[cases[0]][0], t)) for t in SYMS), key=lambda s: sorted(s))
    V = {c: variants(c, target) for c in cases}
    print(f"cases {cases}: bad corners at {[NAME[p] for p in sorted(target)]}; states in that frame: {[len(V[c]) for c in cases]}")
    found = False
    for size in (1, 2, 3):
        for combo in itertools.combinations(PAIRS, size):
            vals = {c: {tuple(feat(p, pr) for pr in combo) for p in V[c]} for c in cases}
            if all(vals[a].isdisjoint(vals[b]) for a, b in itertools.combinations(cases, 2)):
                found = True
                print('  separates:', [(NAME[a], NAME[b]) for a, b in combo])
                for c in cases: print('     case', c, sorted(vals[c]))
        if found: break
    if not found: print('  no set of up to three pairs separates them')
