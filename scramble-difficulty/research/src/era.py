import collections, sys, cube, textfeat as tf
def stats(scrs, label):
    L = collections.Counter(); X = collections.Counter(); Y = collections.Counter(); H = collections.Counter(); A = collections.Counter()
    for s in scrs:
        m, _ = tf.strip(s); ax, x, h, y, d = tf.text_dr(m)
        L[len(m)] += 1; X[min(x, y)] += 1; Y[max(x, y)] += 1; H[h] += 1; A[ax] += 1
    n = len(scrs)
    f = lambda c: ' '.join(f'{k}:{100*v/n:.1f}' for k, v in sorted(c.items()))
    print(f'== {label} n={n}\n len {f(L)}\n short block {f(X)}\n long block {f(Y)}\n H-run {f(H)}\n axis {f(A)}')
real = [l.split('\t') for l in open('../big/real_unique.tsv')][1:]
stats([r[0] for r in real if r[2] < '2021'], 'real 2016-2020')
stats([r[0] for r in real if r[2] >= '2021'], 'real 2021-2026')
gen = [x for x in (l.rstrip('\n').split('\t') for l in open('../big/gen12k.tsv')) if len(x) == 12][1:]
stats([r[1] for r in gen], 'generated')
