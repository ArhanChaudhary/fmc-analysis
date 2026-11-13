#!/usr/bin/env python3
"""Shared numbers of the DR-xs report.

  dr(cs)                 histogram of the optimal finish of all DR states of a corner subset (exact, first study)
  one_s(cs=, turns=)     histogram of the finish of the sampled DR-1s states (setup + slice + DR finish, exact per state)
  eight(cs=)             the same for DR-2s 8fe (setup + both slices + DR finish)
  share(h, t), pct(h, t), avg(h)

Corner subsets are named as in the first study, with 4a3/4b3 merged into 4c3 and 4a4/4b4 into 4c4.  Formatting is
the first study's: 10% and up whole, 1-10% one decimal, under 1% two, '<0.01%', and 0 when nothing gets there."""
import sys, csv, collections, functools, os
sys.path.insert(0, '/data/fmc/judging-a-dr/research/src')
import pv
from pv import fmt, num, avg, share, pct, hu, CS_ORDER
O = '/data/fmc/is-dr-xs-worth-it/research/out/'
def merged(s): return pv.merged(s)

@functools.lru_cache(None)
def _rows(name):
    with open(O + name) as f: return list(csv.DictReader(f, delimiter='\t'))
def _hist(rows, col='finish'):
    h = [0] * 30
    for r in rows: h[int(r[col])] += 1
    return h
def one_s(cs=None, turns=None, col='finish'):
    return _hist([r for r in _rows('sample1s.tsv') if (cs is None or merged(r['subset']) == cs) and (turns is None or int(r['turns_to_dr']) in turns)], col)
def eight(cs=None):
    return _hist([r for r in _rows('sample8fe.tsv') if cs is None or merged(r['subset']) == cs])
def dr(cs=None): return [int(round(x)) for x in pv.q(cs=cs)]
def n(h): return sum(h)
def se(h):
    """Standard error of the mean of a sampled histogram."""
    m = avg(h); N = sum(h); var = sum(c * (d - m) ** 2 for d, c in enumerate(h)) / max(N - 1, 1)
    return (var / N) ** 0.5

if __name__ == '__main__':
    print('DR-1s sample:', n(one_s()), 'states; average finish', round(avg(one_s()), 3), '+-', round(se(one_s()), 3), '| all DRs', round(avg(dr()), 3))
    print('subset     share of DR-1s   DR avg   DR-1s avg   diff    setup<=4 own side   n')
    for cs in CS_ORDER:
        h = one_s(cs)
        if not n(h): continue
        print(f'{cs:6s} {100 * n(h) / n(one_s()):8.2f}%  {avg(dr(cs)):8.3f} {avg(h):9.3f}  {avg(h) - avg(dr(cs)):+.3f} (+-{se(h):.3f})  {avg(one_s(cs, col="finish_setup4")) if 99 not in [d for d, c in enumerate(one_s(cs, col="finish_setup4")) if c] else float("nan"):8.3f}  {n(h)}')
    print('by turns to DR:')
    for t in (2, 3, 4, 5, 6):
        h = one_s(turns=(t,)); print(f'  {t}: share {100 * n(h) / n(one_s()):.2f}%  avg finish {avg(h):.3f}' if n(h) else f'  {t}: none')
    print('finish <= t:   ' + ' '.join(f'{t:>7d}' for t in range(10, 19)))
    print('  DR           ' + ' '.join(f'{pct(dr(), t):>7s}' for t in range(10, 19)))
    print('  DR-1s        ' + ' '.join(f'{pct(one_s(), t):>7s}' for t in range(10, 19)))
    if os.path.exists(O + 'sample8fe.tsv'):
        print('  DR-2s 8fe    ' + ' '.join(f'{pct(eight(), t):>7s}' for t in range(10, 19)), '| avg', round(avg(eight()), 3), 'n', n(eight()))
