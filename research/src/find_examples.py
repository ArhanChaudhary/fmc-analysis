#!/usr/bin/env python3
"""Pick example DRs for EXAMPLES.md: the first random DR state (fixed seed) that has a given read.  The pick never
looks at the optimal, so the examples are not chosen for their outcome."""
import random, sys, importlib.machinery, importlib.util
loader = importlib.machinery.SourceFileLoader('drread', '/data/fmc/research/tool/drread')
spec = importlib.util.spec_from_loader('drread', loader); dr = importlib.util.module_from_spec(spec); loader.exec_module(dr)
random.seed(20261111)
MOVES = ["U", "U2", "U'", "D", "D2", "D'", "R2", "L2", "F2", "B2"]
def scramble(n=30):
    out = []; last = None
    while len(out) < n:
        m = random.choice(MOVES)
        if m[0] == last: continue
        out.append(m); last = m[0]
    return ' '.join(out)
names = dr.corner_names()
scr = [scramble() for _ in range(12000)]
kvs = dr.read_states(scr)
want = {
    '2c5, stacked on both sides': lambda k, cn, ci: cn == '2c5-3' and ci == '2c5-3',
    '2c4 4e, best corners on both sides': lambda k, cn, ci: k['subset'] == '2c4 4e' and cn == '2c4-1' and ci == '2c4-1',
    '2c4, stacked on both sides': lambda k, cn, ci: k['subset'].startswith('2c4') and {cn, ci} <= {'2c4-5', '2c4-7'},
    '4c3 4e, 9+ to HTR on both sides': lambda k, cn, ci: k['subset'] == '4c3 4e' and min(map(int, k['htr'].split())) >= 9,
    '4c3 4e, 7 or 8 to HTR on both sides': lambda k, cn, ci: k['subset'] == '4c3 4e' and max(map(int, k['htr'].split())) <= 8,
    '5qt or 4c4 with five or more pairs': lambda k, cn, ci: k['subset'].split()[0] in ('2c5', '4b5', '4c4') and int(k['true_pairs'].split()[0]) >= 5,
    '4b2 4e, no pairs': lambda k, cn, ci: k['subset'] == '4b2 4e' and int(k['true_pairs'].split()[0]) == 0,
}
found = {}
for s, k in zip(scr, kvs):
    if 'subset' not in k: continue
    cn, ci = (names[x] for x in k['corner_case'].split())
    for w, f in want.items():
        if w not in found and f(k, cn, ci):
            # present the state by a shortest scramble: the inverse of its optimal finish
            inv = {"U": "U'", "U'": "U", "D": "D'", "D'": "D"}
            short = ' '.join(inv.get(m, m) for m in reversed(k['optimal_finish'].split()))
            found[w] = short
for w in want: print(f'{w} :: {found.get(w)}')
