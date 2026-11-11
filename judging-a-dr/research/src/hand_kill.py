#!/usr/bin/env python3
"""Discard power of hand-readable quantities, per corner-qt group and per subset.

For a feature set F and a target T: a class of F is "dead" if at most EPS of its states finish in <= T moves.
Reported: share of all states that sit in dead classes (what you may throw away), share of the <= T finishes
lost by doing so, and the share in classes where no state at all finishes in <= T (a hard bound)."""
import csv, collections, sys
D = '/data/fmc/judging-a-dr/research/out/hand/'
EPS = float(sys.argv[1]) if len(sys.argv) > 1 else 0.01
QT = {'0c0': '0qt', '4a1': '1-2qt', '4a2': '1-2qt', '4b2': '1-2qt', '0c3': '3qt', '2c3': '3qt', '4a3': '3qt', '4b3': '3qt', '4c3': '3qt',
      '0c4': '4qt', '2c4': '4qt', '4a4': '4qt', '4b4': '4qt', '4c4': '4qt', '2c5': '5qt', '4b5': '5qt', '4c5': '5qt'}

def load(name):
    with open(D + name) as f:
        r = csv.reader(f); hdr = next(r)
        return hdr, [row for row in r]

def table(rows, subf, keyf, depthf, cntf):
    g = collections.defaultdict(lambda: collections.defaultdict(lambda: [0] * 19))
    for row in rows:
        g[subf(row)][keyf(row)][depthf(row)] += cntf(row)
    return g

def power(g, T, group):
    out = collections.defaultdict(lambda: [0, 0, 0, 0, 0])   # n, good, dead_n, dead_good, hard_n
    for sub, classes in g.items():
        o = out[group(sub)]
        for h in classes.values():
            n = sum(h); good = sum(h[:T + 1])
            o[0] += n; o[1] += good
            if good <= EPS * n:
                o[2] += n; o[3] += good
            if good == 0:
                o[4] += n
    return out

if __name__ == '__main__':
    hdr, rows = load('h2_lengths.csv'); I = {n: i for i, n in enumerate(hdr)}
    sub = lambda r: r[0]; dep = lambda r: int(r[I['depth']]); cnt = lambda r: int(r[I['count']])
    feats = [
        ('subset only', table(rows, sub, lambda r: 0, dep, cnt)),
        ('longer HTR', table(rows, sub, lambda r: r[I['hmax']], dep, cnt)),
        ('HTR both sides', table(rows, sub, lambda r: (r[I['hmin']], r[I['hmax']]), dep, cnt)),
        ('L', table(rows, sub, lambda r: r[I['L']], dep, cnt)),
        ('L + parity fit', table(rows, sub, lambda r: (r[I['L']], r[I['dLp']]), dep, cnt)),
        ('L + parity fit + HTR both', table(rows, sub, lambda r: (r[I['L']], r[I['dLp']], r[I['hmin']], r[I['hmax']]), dep, cnt)),
    ]
    h1h, h1 = load('h1_coset.csv'); cos = {r[0]: r for r in load('cosets.csv')[1]}
    feats.append(('visible case (normal)', table(h1, lambda r: cos[r[0]][2], lambda r: cos[r[0]][1], lambda r: int(r[2]), lambda r: int(r[3]))))
    feats.append(('visible case + hI', table(h1, lambda r: cos[r[0]][2], lambda r: (cos[r[0]][1], r[1]), lambda r: int(r[2]), lambda r: int(r[3]))))
    h5h, h5 = load('h5_pairs.csv')
    feats.append(('true pairs', table(h5, lambda r: r[0], lambda r: r[1], lambda r: int(r[5]), lambda r: int(r[6]))))
    feats.append(('all four pair counts', table(h5, lambda r: r[0], lambda r: tuple(r[1:5]), lambda r: int(r[5]), lambda r: int(r[6]))))
    for T in (12, 13):
        print(f'\n=== target: finish <= {T}; a class is dead if <= {100*EPS:g}% of it gets there ===')
        print(f'{"what you read":28s} | ' + ' | '.join(f'{q:>22s}' for q in ('1-2qt', '3qt', '4qt', '5qt', 'all')))
        print(f'{"":28s} | ' + ' | '.join(f'{"dead% lost% hard%":>22s}' for _ in range(5)))
        for name, g in feats:
            p = power(g, T, lambda s: QT[s.split()[0]]); allp = power(g, T, lambda s: 'all')['all']
            cells = []
            for q in ('1-2qt', '3qt', '4qt', '5qt'):
                o = p[q]; cells.append(f'{100*o[2]/o[0]:6.1f} {100*o[3]/max(o[1],1):6.2f} {100*o[4]/o[0]:6.1f}  ')
            o = allp; cells.append(f'{100*o[2]/o[0]:6.1f} {100*o[3]/max(o[1],1):6.2f} {100*o[4]/o[0]:6.1f}  ')
            print(f'{name:28s} | ' + ' | '.join(cells))
        o = power(feats[0][1], T, lambda s: QT[s.split()[0]])
        print('share of states that really finish in <= %d: ' % T + ', '.join(f'{q} {100*o[q][1]/o[q][0]:.1f}%' for q in ('1-2qt', '3qt', '4qt', '5qt')))
