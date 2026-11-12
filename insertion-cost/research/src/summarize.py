#!/usr/bin/env python3
"""out/summary.tsv from the sample files out/sample_<type>_n<n>.tsv.

One row per (type, n, model, L): number of skeletons for which the model was computed, how many of them have no
solution within the bound, the mean cost of those that have one, and the share (of all computed skeletons) with
cost <= 2, 3, ..., 12.  For the model `best` also: how often the best solution is the two-insertion one, and how often
that one needs nesting."""
import glob, re, sys, os
OUT = '/data/fmc/insertion-cost/research/out'
MODELS = ['one', 'direct', 'two', 'two_flat', 'two_apart', 'mixed', 'best']
def main(pattern='sample_*_n*.tsv', dest='summary.tsv'):
    rows = []
    rx = re.compile(r'.*/[a-z0-9]+_(.+)_n(\d+)\.tsv')
    for path in sorted(glob.glob(f'{OUT}/{pattern}'), key=lambda p: (rx.match(p).group(1), int(rx.match(p).group(2)))):
        typ, n = rx.match(path).groups()
        with open(path) as f:
            head = f.readline().rstrip('\n').split('\t')
            cols = {h: i for i, h in enumerate(head)}
            Ls = sorted({int(h[1:].split('_')[0]) for h in head if re.match(r'L\d+_', h)})
            data = [line.rstrip('\n').split('\t') for line in f]
        for L in Ls:
            for model in MODELS:
                vals = [r[cols[f'L{L}_{model}']] for r in data]
                vals = [v for v in vals if v not in ('na', 'nc')]
                if not vals: continue
                fin = [int(v) for v in vals if v != 'inf']
                mean = sum(fin) / len(fin) if fin else float('nan')
                shares = [sum(1 for v in fin if v <= k) / len(vals) for k in range(2, 13)]
                extra = ['', '']
                if model == 'best':
                    bm = [(r[cols[f'L{L}_best_model']], r[cols[f'L{L}_nested']]) for r in data if r[cols[f'L{L}_best']] not in ('na', 'nc', 'inf')]
                    if bm:
                        extra = [f"{sum(1 for m, _ in bm if m == 'two') / len(bm):.4f}", f"{sum(1 for m, ne in bm if m == 'two' and ne == '1') / len(bm):.4f}"]
                rows.append([typ, n, model, str(L), str(len(vals)), str(len(vals) - len(fin)), f'{mean:.4f}'] + [f'{s:.4f}' for s in shares] + extra)
    with open(f'{OUT}/{dest}', 'w') as f:
        f.write('\t'.join(['type', 'n', 'model', 'L', 'skeletons', 'unsolved', 'mean_cost'] + [f'share_le{k}' for k in range(2, 13)] + ['best_is_two', 'best_needs_nesting']) + '\n')
        for r in rows: f.write('\t'.join(r) + '\n')
    print(f'wrote {OUT}/{dest}: {len(rows)} rows')
if __name__ == '__main__':
    main(*sys.argv[1:])
