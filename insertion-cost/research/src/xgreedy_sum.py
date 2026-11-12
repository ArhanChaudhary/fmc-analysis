#!/usr/bin/env python3
"""Tables and numbers from the greedy runs (xgreedy.py): report/data/greedy*.md and out/greedy.json."""
import csv, json, os, glob, re, collections
import iv
from iv import O, SHOW, fmt, num, f2
D = '/data/fmc/insertion-cost/report/data/'
def write(name, lines):
    open(D + name + '.md', 'w').write('\n'.join(lines) + '\n'); print(name, len(lines), 'lines')
def load(typ, n, L, full=False):
    p = f"{O}greedy_{typ}_n{n}_L{L}{'_full' if full else ''}.tsv"
    if not os.path.exists(p): return None
    rows = list(csv.DictReader(open(p), delimiter='\t'))
    return [r for r in rows if r['exact'] not in ('inf', 'nc')]          # skeletons that two comms within the cap can solve
def stats(rows):
    """A rule that ends without a second comm within the cap (g = inf) counts as a loss and is left out of that rule's mean."""
    N = len(rows); ex = [int(r['exact']) for r in rows]; out = {'n': N, 'exact': sum(ex) / N, 'splits': int(rows[0]['splits']), 'firsts_per_spot': None}
    for g in ('g0', 'g1', 'g2', 'g3'):
        x = [None if r[g] == 'inf' else int(r[g]) for r in rows]; fin = [v for v in x if v is not None]
        out[g] = sum(fin) / len(fin); out[g + '_hit'] = sum(1 for a, b in zip(x, ex) if a == b); out[g + '_none'] = N - len(fin)
        assert all(a is None or a >= b for a, b in zip(x, ex)), 'a greedy result below the exact minimum'
    m1 = [int(r['m1']) for r in rows]
    out['m1'] = dict(collections.Counter(m1)); out['m1_mean'] = sum(m1) / N
    out['ties'] = sum(int(r['firsts_at_best']) for r in rows) / N
    return out
def main():
    J = {}
    for p in sorted(glob.glob(O + 'greedy_*_n*_L*.tsv')):
        m = re.match(r'.*/greedy_(.+)_n(\d+)_L(\d+)(_full)?\.tsv', p); typ, n, L, full = m.group(1), int(m.group(2)), int(m.group(3)), bool(m.group(4))
        rows = load(typ, n, L, full)
        if not rows: continue
        s = stats(rows); s['firsts_per_spot'] = sum(int(r['firsts']) for r in rows) / len(rows) / (n + 1)
        J[f"{typ}_n{n}_L{L}" + ('_full' if full else '')] = s
    # table: two comms the way people do them, 20 moves, 8-movers
    L = ['| Leftover | Skeletons | Best pair of comms | Best first comm only | Best first comm only: loses | Best first comm only: no second comm fits | First comms within 1 move | Within 1 move: loses | First comms within 2 moves | Within 2 moves: loses |', '|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|']
    for typ in ['2tc', '3tc', '2c2c-pure', '2c2c-twisted', '3c1t', '5c', '3c3c']:
        s = J.get(f'{typ}_n20_L8')
        if not s: continue
        ls = lambda g: fmt(s['n'] - s[g + '_hit'], s['n'])
        L.append(f"| {SHOW[typ]} | {s['n']:,} | {f2(s['exact'])} | {f2(s['g0'])} | {ls('g0')} | {s['g0_none']} | {f2(s['g1'])} | {ls('g1')} | {f2(s['g2'])} | {ls('g2')} |")
    write('greedy', L)
    # how good the best first comm is: 5c by length, next to the best comm of a 3c of that length
    L = ['| Skeleton length | 5c: best first comm, mean added | 8-3 or better | 8-4 or better | 8-5 or better | 3c: best comm, mean added | 3c: 8-3 or better | 3c: 8-4 or better |', '|---:|---:|---:|---:|---:|---:|---:|---:|']
    for n in (12, 14, 16, 18, 20, 24):
        s = J.get(f'5c_n{n}_L8')
        if not s: continue
        le = lambda k: fmt(sum(v for x, v in s['m1'].items() if int(x) <= k), s['n'])
        c = iv.cell('3c', n, 8, 'one')
        L.append(f"| {n} | {f2(s['m1_mean'])} | {le(5)} | {le(4)} | {le(3)} | {f2(iv.mean(c))} | {iv.pct(c, 5)} | {iv.pct(c, 4)} |")
    write('greedy_first', L)
    # first comms to choose from
    L = ['| Leftover | Ways to choose the first comm at one spot | 8-move first comms at one spot, on average |', '|---|---:|---:|']
    for typ in ['2tc', '3tc', '2c2c-pure', '2c2c-twisted', '3c1t', '5c', '3c3c']:
        s = J.get(f'{typ}_n20_L8')
        if s: L.append(f"| {SHOW[typ]} | {s['splits']} | {s['firsts_per_spot']:.1f} |")
    write('first_choices', L)
    # cap 10 against cap 8 at greedy 0, same skeletons (5c, 20 moves)
    a, b = load('5c', 20, 8), load('5c', 20, 10)
    if a and b:
        A = {r['idx']: r for r in a}; common = [(A[r['idx']], r) for r in b if r['idx'] in A and r['g0'] != 'inf' and A[r['idx']]['g0'] != 'inf']
        J['5c_cap10_vs_8'] = {'run': len(b), 'n': len(common), 'g0_10_worse': sum(1 for x, y in common if int(y['g0']) > int(x['g0'])), 'g0_10_better': sum(1 for x, y in common if int(y['g0']) < int(x['g0'])),
                              'g0_8': sum(int(x['g0']) for x, y in common) / len(common), 'g0_10': sum(int(y['g0']) for x, y in common) / len(common),
                              'exact_8': sum(int(x['exact']) for x, y in common) / len(common), 'exact_10': sum(int(y['exact']) for x, y in common) / len(common)}
    json.dump(J, open(O + 'greedy.json', 'w'), indent=1)
    for k, s in J.items(): print(k, {x: (round(v, 3) if isinstance(v, float) else v) for x, v in s.items() if x in ('n', 'exact', 'g0', 'g1', 'g2', 'g0_hit', 'g1_hit', 'g2_hit', 'splits', 'firsts_per_spot', 'm1_mean', 'g0_10_worse', 'g0_10_better', 'g0_8', 'g0_10')})
if __name__ == '__main__': main()
