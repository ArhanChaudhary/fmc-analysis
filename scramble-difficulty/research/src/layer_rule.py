"""Hit rates of unfitted per-axis rules built on Levi Gibson's split (all scrambles; and the held-out third used in
claims_extra.py for the weighted score, whose weight came from the fit on the other two thirds).
flipped layer edges of DR axis a = a-coloured edges sitting in an a layer with the a sticker on the side
                                 = layer pieces bad on both EO axes (lg_<a>_Lb, checked piece by piece)."""
import csv, numpy as np
AX = ['UD', 'FB', 'RL']
rows = []
for tag in ('uni', 'real', 'gen'):
    TA = {(r['id'], r['axis']): float(r['n10']) for r in csv.DictReader(open(f'out/tgt_{tag}_axis.tsv'), delimiter='\t')}
    F3 = {r['id']: r for r in csv.DictReader(open(f'out/feat3_{tag}.tsv'), delimiter='\t')}
    for r in csv.DictReader(open(f'out/feat_{tag}.tsv'), delimiter='\t'):
        k = r['id']; f3 = F3[k]
        g = []
        for a in AX:
            es = [e for e in AX if e != a]
            g.append(dict(t=TA.get((k, a), 0.0), lb=float(f3[f'lg_{a}_Lb']), lone=float(f3[f'lg_{a}_L1']) + float(f3[f'lg_{a}_L2']),
                          sone=float(f3[f'lg_{a}_S1']) + float(f3[f'lg_{a}_S2']), sb=float(f3[f'lg_{a}_Sb']),
                          bs=float(r[f'be_{es[0]}']) + float(r[f'be_{es[1]}'])))
        rows.append(g)
N = len(rows); rng = np.random.default_rng(20261113)
def hit(G, score):
    per = []; ch = []
    for g in G:
        tv = np.array([x['t'] for x in g]); sv = np.array([score(x) for x in g])
        w = set(np.flatnonzero(tv == tv.max())); top = np.flatnonzero(sv == sv.max())
        per.append(np.mean([i in w for i in top])); ch.append(len(w) / 3)
    per = np.array(per); bs = [per[rng.integers(0, len(per), len(per))].mean() for _ in range(400)]
    return f'{per.mean():.3f} [{np.percentile(bs, 2.5):.3f}, {np.percentile(bs, 97.5):.3f}] (chance {np.mean(ch):.3f})'
ids = np.random.default_rng(3).permutation(N); trs = set(ids[:int(0.67 * N)].tolist())
te = [g for i, g in enumerate(rows) if i not in trs]
out = open('out/layer_rule.txt', 'w')
def P(s): print(s); out.write(s + '\n')
P(f'all {N} scrambles:')
P('  fewest flipped layer edges: ' + hit(rows, lambda x: -x['lb']))
P('  fewest layer-coloured edges out of place or flipped (in the slice, or flipped in a layer): ' + hit(rows, lambda x: -(x['lb'] + x['lone'])))
P('  fewest bad edges on the two EO axes (sum): ' + hit(rows, lambda x: -x['bs']))
P('  bad edges on the two EO axes + 4 x flipped layer edges: ' + hit(rows, lambda x: -(x['bs'] + 4 * x['lb'])))
P('  4 x flipped layer edges + every other bad-on-one-or-both count: ' + hit(rows, lambda x: -(4 * x['lb'] + x['lone'] + x['sone'] + x['sb'])))
P(f'held-out third ({len(te)} scrambles):')
P('  bad edges on the two EO axes + 4 x flipped layer edges: ' + hit(te, lambda x: -(x['bs'] + 4 * x['lb'])))
P('  4 x flipped layer edges + the other three counts: ' + hit(te, lambda x: -(4 * x['lb'] + x['lone'] + x['sone'] + x['sb'])))
P('  fewest flipped layer edges: ' + hit(te, lambda x: -x['lb']))
# distribution and mean DRs by flipped layer edges
import collections
c = collections.defaultdict(list)
for g in rows:
    for x in g: c[int(x['lb'])].append(x['t'])
P('flipped layer edges on a DR axis -> axes, mean DRs of <= 10 on that axis, median, share with none')
for k in sorted(c): P(f'  {k}: {len(c[k])}, {np.mean(c[k]):.1f}, {np.median(c[k]):.0f}, {100 * np.mean(np.array(c[k]) == 0):.1f}%')
