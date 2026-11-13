#!/usr/bin/env python3
"""trig0n's question (T73), all three versions: a 3c insertion on a 17-move skeleton made of
  1. random moves,
  2. EO in 5, then random moves that do not break EO,
  3. EO in 4, DR in 10, then DR moves.
The skeletons are modelled, not solved: (1) 17 random moves; (2) 5 random moves, then 12 moves without quarter turns
of F or B; (3) 4 random moves, 6 moves without quarter turns of F or B, then 7 moves of the DR group <U, D, R2, L2,
F2, B2>.  The 3c is uniform among all corner 3-cycles, except in "3, DR leftover": there it is uniform among the 112
3-cycles that keep the three corners' U/D stickers on U and D, which is what moves of the DR group can leave.
Computed with py3.py (Python, sticker model): best insertion with 8-movers and with every alg of up to 10 moves.
Writes out/dr17.json and report/data/dr17.md."""
import json, random, sys, multiprocessing, collections
import cube, cubie, py3, iv
from iv import fmt, f2
N = 17; COUNT = 20000
ALL = list(range(18))
EOSAFE = [m for m in ALL if not (m // 3 in (4, 5) and m % 3 != 1)]            # no F, F', B, B'
DRM = [m for m in ALL if m // 3 in (0, 1) or m % 3 == 1]                       # U, D any; the others half turns
def ok(prev, m): return prev is None or not (m // 3 == prev // 3 or (m // 6 == prev // 6 and m // 3 < prev // 3))
def seq(rnd, parts):
    out = []
    for k, moves in parts:
        for _ in range(k):
            while True:
                m = rnd.choice(moves)
                if ok(out[-1] if out else None, m): out.append(m); break
    return out
def work(job):
    name, seed = job
    T = py3.table('c', 10); rnd = random.Random(seed)
    els = sorted(T); ori = [cubie.make(*e) for e in py3.elements('c') if not any(e[1])]
    parts = {'1': [(17, ALL)], '2': [(5, ALL), (12, EOSAFE)], '3': [(4, ALL), (6, EOSAFE), (7, DRM)], '3dr': [(4, ALL), (6, EOSAFE), (7, DRM)]}[name]
    h8 = collections.Counter(); h10 = collections.Counter()
    for _ in range(COUNT // 4):
        sk = seq(rnd, parts); c = rnd.choice(ori if name == '3dr' else els); n = len(sk); g = cube.inverse(c); b8 = b10 = None
        for i in range(n, -1, -1):
            if i < n: g = cube.compose(cube.compose(py3.MS[sk[i]], g), py3.MI[sk[i]])
            pre = sk[:i]; post = sk[i:]
            for a in T.get(g, ()):
                v = py3.clen(pre + list(a) + post) - n
                if b10 is None or v < b10: b10 = v
                if len(a) == 8 and (b8 is None or v < b8): b8 = v
        h8['none' if b8 is None else b8] += 1; h10['none' if b10 is None else b10] += 1
    return name, dict(h8), dict(h10)
def main():
    py3.table('c', 10)
    jobs = [(name, 1000 * k + i) for k, name in enumerate(('1', '2', '3', '3dr')) for i in range(4)]
    with multiprocessing.Pool(3) as pool: res = pool.map(work, jobs)
    J = {}
    for name, h8, h10 in res:
        d = J.setdefault(name, {'8': collections.Counter(), '10': collections.Counter()})
        d['8'].update(h8); d['10'].update(h10)
    J = {k: {c: {str(x): v for x, v in h.items()} for c, h in d.items()} for k, d in J.items()}
    json.dump(J, open(iv.O + 'dr17.json', 'w'), indent=1)
    table(J)
def table(J, D='/data/fmc/insertion-cost/report/data/'):
    """report/data/dr17.md from out/dr17.json (`xdr.py --table` rewrites it without the run)."""
    NAME = {'1': 'random moves', '2': 'EO in 5, then moves that keep EO', '3': 'EO in 4, DR in 10, then DR moves; any 3c', '3dr': 'EO in 4, DR in 10, then DR moves; a 3c that DR moves can leave'}
    L = ['| 17 to 3c with | Cap | Mean moves added | Adds 4 or less | Adds 5 or less | Adds 6 or less | Adds 7 or less | Adds 8 or less | Nothing fits |', '|---|---:|---:|---:|---:|---:|---:|---:|---:|']
    for name in ('1', '2', '3', '3dr'):
        for cap in ('8', '10'):
            h = J[name][cap]; tot = sum(h.values()); fin = {int(k): v for k, v in h.items() if k != 'none'}
            le = lambda k: fmt(sum(v for x, v in fin.items() if x <= k), tot)
            L.append(f"| {NAME[name]} | {cap} | {f2(sum(k * v for k, v in fin.items()) / sum(fin.values()))} | {le(4)} | {le(5)} | {le(6)} | {le(7)} | {le(8)} | {fmt(h.get('none', 0), tot) if h.get('none') else '0'} |")
    open(D + 'dr17.md', 'w').write('\n'.join(L) + '\n')
    print('\n'.join(L))
if __name__ == '__main__':
    if '--table' in sys.argv: table(json.load(open(iv.O + 'dr17.json')))
    else: main()
