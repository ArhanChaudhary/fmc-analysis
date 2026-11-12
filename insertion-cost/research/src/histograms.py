#!/usr/bin/env python3
"""out/hist.json: for every sample file (sample_*, mixed_*, two12_*, base_* = odd lengths for the real-skeleton comparison), every cap L and every model, the histogram of the
added moves, so that the report scripts do not have to read a gigabyte of sample lines each time.

  hist[prefix][type][n][L][model] = {"n": skeletons the model was computed for, "inf": of them without a solution
                                     within the cap, "h": {cost: count}}
For the model `best` also "two": how many best solutions are the two-insertion one, "nested": how many of those need
nesting, and for the one-insertion types "len": {algorithm length of the reported best: count}."""
import glob, re, json, collections, sys
OUT = '/data/fmc/insertion-cost/research/out'
MODELS = ['one', 'direct', 'two', 'two_flat', 'two_apart', 'mixed', 'best']
def main():
    H = {}
    rx = re.compile(r'.*/(sample|mixed|two12|base)_(.+)_n(\d+)\.tsv')
    for path in sorted(glob.glob(f'{OUT}/sample_*_n*.tsv') + glob.glob(f'{OUT}/mixed_*_n*.tsv') + glob.glob(f'{OUT}/two12_*_n*.tsv') + glob.glob(f'{OUT}/base_*_n*.tsv')):
        pre, typ, n = rx.match(path).groups()
        with open(path) as f:
            head = f.readline().rstrip('\n').split('\t'); col = {h: i for i, h in enumerate(head)}
            Ls = sorted({int(h[1:].split('_')[0]) for h in head if re.match(r'L\d+_', h)})
            acc = {L: {m: collections.Counter() for m in MODELS} for L in Ls}
            ext = {L: collections.Counter() for L in Ls}
            for line in f:
                p = line.rstrip('\n').split('\t')
                for L in Ls:
                    for m in MODELS:
                        acc[L][m][p[col[f'L{L}_{m}']]] += 1
                    if p[col[f'L{L}_best']] not in ('na', 'nc', 'inf'):
                        if p[col[f'L{L}_best_model']] == 'two':
                            ext[L]['two'] += 1
                            if p[col[f'L{L}_nested']] == '1': ext[L]['nested'] += 1
                        if p[col[f'L{L}_best_model']] == 'mixed': ext[L]['mixed'] += 1
        for L in Ls:
            for m in MODELS:
                c = acc[L][m]; tot = sum(v for k, v in c.items() if k not in ('na', 'nc'))
                if not tot: continue
                d = {'n': tot, 'inf': c.get('inf', 0), 'h': {k: v for k, v in sorted(c.items(), key=lambda kv: (kv[0] in ('inf', 'na', 'nc'), int(kv[0]) if kv[0].lstrip('-').isdigit() else 0)) if k not in ('na', 'nc', 'inf')}}
                if m == 'best': d.update({'two': ext[L]['two'], 'nested': ext[L]['nested'], 'mixed': ext[L]['mixed']})
                H.setdefault(pre, {}).setdefault(typ, {}).setdefault(n, {}).setdefault(str(L), {})[m] = d
        print(path.split('/')[-1], end=' ', flush=True)
    json.dump(H, open(f'{OUT}/hist.json', 'w'))
    print('\nwrote', f'{OUT}/hist.json')
if __name__ == '__main__': main()
