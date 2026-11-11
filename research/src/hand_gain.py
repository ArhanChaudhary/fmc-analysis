#!/usr/bin/env python3
"""Triage power: if you rank DRs by what you can read and only keep the best-looking share, how many of the
short finishes do you keep?  Per corner-qt group.  Uses hand_kill.table()."""
import sys
sys.path.insert(0, '/data/fmc/research/src')
from hand_kill import load, table, QT

def gain(g, T, want, shares=(0.10, 0.25, 0.50)):
    cl = []
    for sub, classes in g.items():
        if not want(sub): continue
        for h in classes.values():
            n = sum(h); good = sum(h[:T + 1]); cl.append((good / n, n, good))
    cl.sort(reverse=True)
    N = sum(c[1] for c in cl); G = sum(c[2] for c in cl)
    out = []; accn = accg = 0; i = 0
    for s in shares:
        while i < len(cl) and accn + cl[i][1] <= s * N:
            accn += cl[i][1]; accg += cl[i][2]; i += 1
        # take a fraction of the next class to hit the share exactly
        extra = 0
        if i < len(cl):
            extra = (s * N - accn) / cl[i][1] * cl[i][2]
        out.append((accg + extra) / G)
    return G / N, out

if __name__ == '__main__':
    hdr, rows = load('h2_lengths.csv'); I = {n: i for i, n in enumerate(hdr)}
    sub = lambda r: r[0]; dep = lambda r: int(r[I['depth']]); cnt = lambda r: int(r[I['count']])
    feats = [
        ('subset only', table(rows, sub, lambda r: 0, dep, cnt)),
        ('E-slice parity', table(rows, sub, lambda r: r[I['parity']], dep, cnt)),
        ('longer HTR', table(rows, sub, lambda r: r[I['hmax']], dep, cnt)),
        ('HTR both sides', table(rows, sub, lambda r: (r[I['hmin']], r[I['hmax']]), dep, cnt)),
        ('L', table(rows, sub, lambda r: r[I['L']], dep, cnt)),
        ('L + parity fit', table(rows, sub, lambda r: (r[I['L']], r[I['dLp']]), dep, cnt)),
        ('L + parity fit + HTR both', table(rows, sub, lambda r: (r[I['L']], r[I['dLp']], r[I['hmin']], r[I['hmax']]), dep, cnt)),
    ]
    h1 = load('h1_coset.csv')[1]; cos = {r[0]: r for r in load('cosets.csv')[1]}
    feats.append(('visible case (normal)', table(h1, lambda r: cos[r[0]][2], lambda r: cos[r[0]][1], lambda r: int(r[2]), lambda r: int(r[3]))))
    feats.append(('visible case + hI', table(h1, lambda r: cos[r[0]][2], lambda r: (cos[r[0]][1], r[1]), lambda r: int(r[2]), lambda r: int(r[3]))))
    h5 = load('h5_pairs.csv')[1]
    feats.append(('true pairs', table(h5, lambda r: r[0], lambda r: r[1], lambda r: int(r[5]), lambda r: int(r[6]))))
    feats.append(('all four pair counts', table(h5, lambda r: r[0], lambda r: tuple(r[1:5]), lambda r: int(r[5]), lambda r: int(r[6]))))
    h9 = load('h9_true_slice_pairs.csv')[1]
    feats.append(('true + slice pairs', table(h9, lambda r: r[0], lambda r: (r[1], r[2]), lambda r: int(r[3]), lambda r: int(r[4]))))
    h3 = load('h3_leaveslice.csv')[1]
    feats.append(('[optimal leave slice]', table(h3, lambda r: r[0], lambda r: r[2], lambda r: int(r[1]), lambda r: int(r[3]))))
    for T in (12, 13):
        print(f'\n=== share of the finishes <= {T} that you keep if you keep only the best-looking 10% / 25% / 50% of DRs ===')
        print(f'{"ranked by":28s} | ' + ' | '.join(f'{q:^17s}' for q in ('1-2qt', '3qt', '4qt', '5qt', 'all DRs')))
        for name, g in feats:
            cells = []
            for q in ('1-2qt', '3qt', '4qt', '5qt', 'all'):
                base, out = gain(g, T, (lambda s: True) if q == 'all' else (lambda s, q=q: QT[s.split()[0]] == q))
                cells.append(' '.join(f'{100*x:4.0f}%' for x in out))
            print(f'{name:28s} | ' + ' | '.join(f'{c:^17s}' for c in cells))
