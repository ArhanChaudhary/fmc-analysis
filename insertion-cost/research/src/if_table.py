#!/usr/bin/env python3
"""The Insertion Finder comparison as a table: out/if_cases.tsv (what the saved pages say) next to out/if_best.txt
(what `instools best` finds), written to out/if_compare.tsv."""
import re, sys
OUT = '/data/fmc/insertion-cost/research/out'
best = sys.argv[1] if len(sys.argv) > 1 else f'{OUT}/if_best.txt'
cases = [l.rstrip('\n').split('\t') for l in open(f'{OUT}/if_cases.tsv')]
blocks = re.split(r'^CASE\t', open(best).read(), flags=re.M)[1:]
Ls = sorted({int(x) for x in re.findall(r'^L=(\d+) ', open(best).read(), flags=re.M)})
models = ['direct', 'two', 'two-flat', 'two-apart', 'mixed', 'best']
head = ['page', 'IF says', 'skeleton length', 'our type', 'IF length'] + [f'L{L} {m}' for L in Ls for m in models]
rows = [head]
for c, b in zip(cases, blocks):
    typ = re.search(r'^leftover: ([^|]+) \|', b, flags=re.M)
    n = re.search(r'^skeleton: .*\((\d+)\)', b, flags=re.M)
    row = [c[2], c[3], n.group(1) if n else '?', typ.group(1).strip() if typ else '?', c[4]]
    for L in Ls:
        for m in models:
            x = re.search(rf'^L={L} {m}: cost (-?\d+), length (\d+)( \(nested\))?', b, flags=re.M)
            row.append((x.group(2) + ('n' if x.group(3) and m != 'best' else '')) if x else ('none' if re.search(rf'^L={L} {m}: no solution', b, flags=re.M) else '-'))
    rows.append(row)
open(f'{OUT}/if_compare.tsv', 'w').write('\n'.join('\t'.join(r) for r in rows) + '\n')
for r in rows: print('\t'.join(r))
