"""Real WCA 333fm scrambles (WCA results export v2, table scrambles): dedupe, date, text split, DR check.
out: big/real_unique.tsv (scramble, first competition, date, n_uses), printed stats."""
import collections, cube, textfeat as tf
dates = {}
for l in open('../big/comp_dates.tsv'):
    r = l.rstrip('\n').split('\t')
    if r[0] != 'id': dates[r[0]] = f'{r[1]}-{int(r[2]):02d}-{int(r[3]):02d}'
seen = collections.OrderedDict()
for l in open('../big/fm_scrambles.tsv'):
    r = l.rstrip('\n').split('\t')
    s = ' '.join(r[0].split()); comp = r[2]
    seen.setdefault(s, []).append((dates.get(comp, '?'), comp))
print('rows', sum(len(v) for v in seen.values()), 'unique', len(seen))
byyear = collections.defaultdict(collections.Counter); out = []
nonpad = collections.Counter()
for s, uses in seen.items():
    uses.sort(); d, comp = uses[0]
    m, padded = tf.strip(s)
    y = d[:4]
    if not padded:
        nonpad[y] += 1; continue
    ax, x, h, yy, drl = tf.text_dr(m)
    ok = tf.check_dr(m, ax, x, h)
    byyear[y]['n'] += 1; byyear[y]['ok'] += ok; byyear[y]['len'] += len(m); byyear[y]['len19'] += len(m) <= 19
    byyear[y]['drl'] += drl
    out.append((s, comp, d, len(uses)))
print('not padded by year', dict(sorted(nonpad.items())))
for y in sorted(byyear):
    b = byyear[y]
    print(y, b['n'], 'drOK', b['ok'], 'meanlen %.2f' % (b['len'] / b['n']), 'len<=19 %.2f' % (b['len19'] / b['n']), 'mean text DR %.2f' % (b['drl'] / b['n']))
with open('../big/real_unique.tsv', 'w') as f:
    f.write('scramble\tcompetition\tdate\tn_uses\n')
    for r in out: f.write('\t'.join(map(str, r)) + '\n')
