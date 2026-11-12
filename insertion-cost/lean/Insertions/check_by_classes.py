#!/usr/bin/env python3
"""A second count of the tables certified in Lean, by another method.  Not used by the Lean build.

The Lean (like leftover_types.py) multiplies everything out.  This script uses a fact about the group instead:
conjugating a 3-cycle by anything (a permutation of the places, a twist of single pieces) gives a 3-cycle again,
and two states have the same type exactly when one is a conjugate of the other.  So the states that k 3-cycles
make are whole types, and it is enough to multiply ONE state of each type by every 3-cycle and note the types that
come out.  The size of a type is a closed formula.  Runs in a second; prints, for corners and edges and k = 0..3,
the types that need k 3-cycles with their sizes.

    /data/fmc/venv/bin/python check_by_classes.py
"""
import sys, math, collections
sys.dont_write_bytecode = True                              # leave no __pycache__ next to the reference
sys.path.insert(0, '/data/fmc/insertion-cost/research/src')
from leftover_types import mul, ident, three_cycles, ctype, name

def type_size(tp, n, m):
    """Number of states of the type on n places.  Write the n places in a row and cut the row into the cycles
    (n! rows); a group of k cycles of the same length L and the same twist sum is then counted L^k * k! times
    (each cycle can start anywhere, the k cycles can come in any order); a cycle of length L has m^(L-1) twists."""
    full = list(tp) + [(1, 0)] * (n - sum(L for L, _ in tp))
    size = math.factorial(n)
    for (L, tw), k in collections.Counter(full).items(): size //= L ** k * math.factorial(k)
    for L, tw in full: size *= m ** (L - 1)
    return size

def fewest(kind, depth):
    n, m = (8, 3) if kind == 'corner' else (12, 2)
    C3 = sorted(three_cycles(n, m)); e = ident(n)
    need = {(): 0}; rep = {(): e}; frontier = [()]
    for k in range(1, depth + 1):
        new = []
        for tp in frontier:
            for g in C3:
                s = mul(rep[tp], g, m); t2 = ctype(s, m)
                if t2 not in need: need[t2] = k; rep[t2] = s; new.append(t2)
        frontier = new
    return need, n, m

if __name__ == '__main__':
    for kind in ('corner', 'edge'):
        need, n, m = fewest(kind, 3)
        for k in range(4):
            tps = sorted((tp for tp in need if need[tp] == k), key=lambda tp: (-type_size(tp, n, m), tp))
            print(f'{kind}: {len(tps)} types need {k}, {sum(type_size(tp, n, m) for tp in tps)} states')
            for tp in tps: print(f'    {type_size(tp, n, m):>10}  {list(tp)}  {name(tp, kind)}')
        print(f'{kind}: {sum(type_size(tp, n, m) for tp in need)} states within three')
