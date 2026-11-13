"""Is the official middle the first solution min2phase finds?  big/first_real.tsv = FirstSol's output (the call with
0 ms of extra search) for the state of every official middle.  Compared by text and by length, by era."""
import collections, cube, textfeat as tf
real = [l.rstrip('\n').split('\t') for l in open('../big/real_unique.tsv')][1:]
first = dict(l.rstrip('\n').split('\t') for l in open('../big/first_real.tsv'))
O = open('../out/first_check.txt', 'w')
def P(*a):
    s = ' '.join(map(str, a)); print(s); O.write(s + '\n')
ex = None
for lab, lo, hi in (('2016-04 to 2020-07', '0', '2020-08'), ('2020-08 to 2026-10', '2020-08', '9')):
    c = collections.Counter(); n = 0; dl = collections.Counter()
    for i, r in enumerate(real):
        if not (lo <= r[2] < hi): continue
        m, _ = tf.strip(r[0]); f = cube.parse(first[f'r{i}'])
        assert cube.seq(f) == cube.seq(m), i      # the first solution, inverted, makes the same state
        n += 1; c['same text'] += (f == m); c['official shorter'] += len(m) < len(f); c['same length'] += len(m) == len(f); c['official longer'] += len(m) > len(f)
        dl[len(f) - len(m)] += 1
        if lab.startswith('2020') and len(m) < len(f) and r[2] >= '2026-10': ex = (r, f, m)
    P(f'{lab}: n={n}; ' + ', '.join(f'{k}: {v} ({100 * v / n:.1f}%)' for k, v in c.items()))
    P('   first-found length minus official length:', sorted(dl.items()))
    P('   mean first-found length', sum(len(cube.parse(first[f"r{i}"])) for i, r in enumerate(real) if lo <= r[2] < hi) / n)
r, f, m = ex
P(f'example: {r[1]} ({r[2]}): {r[0]}\n   official middle ({len(m)}): {" ".join(m)}\n   first found ({len(f)}): {" ".join(f)}')
