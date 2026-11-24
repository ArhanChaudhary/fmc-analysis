"""Within a fixed generation depth (S+T <= K, at most 1 extra move before 2qt, both sides): which order of finishing?
The baseline is the pairs-aware one: the pair floor, shortest HTR first, most pairs first among equals."""
import sys, json
from common import *
PF = {0: 4, 2: 5, 4: 3, 6: 3, 8: 2, 10: 3, 12: 1, 16: 0}
out = {}
for m in [2, 3, 4]:
    df, d, q, mm, g = frame(m)
    df['A'] = g - df.len
    df['plive'] = df.pn0.map(PF) <= df.A; df['rlive'] = df.rs >= 0; df['both'] = df.plive & df.rlive
    df['np0'] = -df.pn0; df['negM'] = -df.M; df['zero'] = 0
    df['skid'] = df.side * 100 + df.q * 10 + df.kind
    Ks = (1, 2, 3, 5, 10, 20, 40)
    for K in [2, 3, 4]:
        reg = (df.cs >= 0) & (df.e2 <= 1) & (df.ex <= K)
        pols = {
            'no floors: by moves to HTR, random': (reg, ['len']),
            'no floors: by moves to HTR, most pairs': (reg, ['len', 'np0']),
            'no floors: most pairs first (look at all first)': (reg, ['np0', 'len']),
            'rule only: random': (reg & df.rlive, ['zero']),
            'rule only: by moves to HTR, most pairs': (reg & df.rlive, ['len', 'np0']),
            'rule only: most pairs first (look at all first)': (reg & df.rlive, ['np0', 'len']),
            'pair floor only: random': (reg & df.plive, ['zero']),
            'pair floor only: by moves to HTR, most pairs': (reg & df.plive, ['len', 'np0']),
            'pair floor only: most pairs first (look at all first)': (reg & df.plive, ['np0', 'len']),
            'both floors: random': (reg & df.both, ['zero']),
            'both floors: level by level, most pairs': (reg & df.both, ['ex', 'np0']),
            'both floors: by moves to HTR, most pairs': (reg & df.both, ['len', 'np0']),
            'both floors: skeleton by skeleton (largest M first), level, pairs': (reg & df.both, ['negM', 'skid', 'ex', 'np0']),
            'both floors: min-qt skeletons first, then level, pairs': (reg & df.both, ['dq', 'ex', 'np0']),
            'both floors: most pairs first (look at all first)': (reg & df.both, ['np0', 'len']),
            'both floors: 12+ pairs first, then level by level': (reg & df.both, [None]),
        }
        df['p12'] = np.where(df.pn0 >= 12, 0, 1)
        pols['both floors: 12+ pairs first, then level by level'] = (reg & df.both, ['p12', 'ex', 'np0'])
        for name, (mask, keys) in pols.items():
            p = policy(df, d, mask, keys, Ks=Ks)
            out[f'{m}|{K}|{name}'] = dict(recall=float(p['found']), median=float(p['median']), mean=float(p['mean_found']), R={str(k): float(v) for k, v in p['recall'].items()},
                                          per_dr=float(p['size_all']), per_unsolv=float(p['size_unsolv']))
            print(f"m={m} K={K} {name:66s} reach {p['found']:.3f} med {p['median']:5.1f} mean {p['mean_found']:6.1f} R@3 {p['recall'][3]:.2f} R@5 {p['recall'][5]:.2f} R@10 {p['recall'][10]:.2f} R@20 {p['recall'][20]:.2f} R@40 {p['recall'][40]:.2f} | per DR {p['size_all']:.0f} unsolv {p['size_unsolv']:.0f}")
json.dump(out, open('../out/meta/orders.json', 'w'), indent=1)
