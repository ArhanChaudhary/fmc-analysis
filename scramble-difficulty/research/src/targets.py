"""Difficulty targets per scramble (and per scramble x DR axis) from an EO-first DR list + its labels.

usage: targets.py raw.tsv label.tsv prefix out_scr.tsv out_axis.tsv [cap]
  cap       : only DRs of at most cap moves count (default 10; the population lists go to 11 or 10)
  raw.tsv   : population.py / enum_drs.py output (one row per distinct DR state of <= 11 moves)
  label.tsv : htrtools label output, row-aligned with raw.tsv (subset, d = optimal DR-move finish, ...)
  prefix    : id prefix when raw's scr column is a bare index ('u' for the gaps population), '' otherwise
Targets (each DR = a distinct DR state reached by EO <= 5 (NISS allowed) then DR, total <= cap moves):
  n8 n9 n10 n11     number of DRs of at most k moves
  best              min over DRs of (DR length + optimal finish)   [missing -> no DR <= 11]
  n_near            DRs with length + finish <= best + 1
  good19..good22    DRs with length + finish <= T
  gsub10            DRs of <= 10 moves in a good corner case (0c0, 2c3, 4a1, 4b2) with <= 4 bad edges
  bestdr            shortest DR length
Per axis the same with the axis' DRs only."""
import sys
from collections import defaultdict

GOODC = {'0c0', '2c3', '4a1', '4b2'}
TS = (19, 20, 21, 22)

def new():
    return {'n8': 0, 'n9': 0, 'n10': 0, 'n11': 0, 'best': 99, 'bestdr': 99, 'gsub10': 0, 'tots': [], **{f'good{t}': 0 for t in TS}}

def add(A, L, tot, good):
    for k in (8, 9, 10, 11):
        if L <= k: A[f'n{k}'] += 1
    A['best'] = min(A['best'], tot); A['bestdr'] = min(A['bestdr'], L)
    for t in TS:
        if tot <= t: A[f'good{t}'] += 1
    if L <= 10 and good: A['gsub10'] += 1
    A['tots'].append(tot)

def fin(A):
    b = A['best']
    A['n_near'] = sum(1 for t in A['tots'] if t <= b + 1)
    del A['tots']
    return A

def main():
    raw, lab, prefix, o1, o2 = sys.argv[1:6]
    cap = int(sys.argv[6]) if len(sys.argv) > 6 else 10
    S = defaultdict(new); X = defaultdict(new)
    fr = open(raw); fl = open(lab)
    next(fl)
    for line in fr:
        if line.startswith('#') or line.startswith('scr\t'): continue
        r = line.rstrip('\n').split('\t'); l = next(fl).rstrip('\n').split('\t')
        k = prefix + r[0] if prefix else r[0]
        L = int(r[3]); d = int(l[1]); sub = l[0].split()
        if L > cap: continue
        good = sub[0] in GOODC and int(sub[1][:-1]) <= 4
        add(S[k], L, L + d, good); add(X[(k, r[1].replace('/', ''))], L, L + d, good)
    assert next(fl, None) is None, 'label file longer than raw'
    keys = ['n8', 'n9', 'n10', 'n11', 'best', 'n_near'] + [f'good{t}' for t in TS] + ['gsub10', 'bestdr']
    with open(o1, 'w') as f:
        f.write('id\t' + '\t'.join(keys) + '\n')
        for k, A in S.items():
            A = fin(A); f.write(k + '\t' + '\t'.join(str(A[x]) for x in keys) + '\n')
    with open(o2, 'w') as f:
        f.write('id\taxis\t' + '\t'.join(keys) + '\n')
        for (k, a), A in X.items():
            A = fin(A); f.write(f'{k}\t{a}\t' + '\t'.join(str(A[x]) for x in keys) + '\n')

if __name__ == '__main__':
    main()
