#!/usr/bin/env python3
"""Which reading rule docs 396 / 410 used: their path shares against ours under three rules (htrtools docpaths,
5,000 states per subset): every NISS reading of every optimal finish; per optimal finish only its shortest-HTR
readings; linear readings only.  Doc 396 is compared on states with optimal <= 12; the 0c0 0e tab also on the
states already in HTR only.  Output: out/compare_docs_reading_rules.tsv (per doc and rule: mean absolute difference
over all listed paths, correlation, share of paths within 0.05)."""
import csv, collections
import numpy as np
from common import *
from compare_docs import DOCS, doc_paths
D = collections.defaultdict(dict)
for r in csv.DictReader(open(f'{R}/out/big/docpaths.tsv'), delimiter='\t'):
    D[(r['subset'], r['population'])][r['chain'][2:]] = (float(r['share_all_readings']), float(r['share_shortest_htr_reading']), float(r['share_linear']))
out = open(f'{OUT}/compare_docs_reading_rules.tsv', 'w')
out.write('doc\trule\tpopulation_note\tpaths\tmean_abs_diff\tcorrelation\tshare_within_0.05\n')
for doc, base in DOCS.items():
    for ri, rule in enumerate(['all readings', 'shortest-HTR readings per finish', 'linear only']):
        for note in ('0c0 0e tab = all its states', '0c0 0e tab = states in HTR'):
            d = []; o = []
            for sub in SUBS:
                hdr, paths = doc_paths(f'{base}/{fname(sub)}.csv')
                pop = 'le12' if doc == '396' else 'all'
                if sub == '0c0 0e' and 'in HTR' in note: pop = 'htr'
                for p, path in paths:
                    d.append(p); o.append(D[(sub, pop)].get(path, (0, 0, 0))[ri])
            d = np.array(d); o = np.array(o)
            out.write(f'{doc}\t{rule}\t{note}\t{len(d)}\t{abs(d - o).mean():.4f}\t{np.corrcoef(d, o)[0, 1]:.4f}\t{(abs(d - o) <= 0.05).mean():.4f}\n')
out.close()
# cell by cell under the matching rule (shortest-HTR readings), every listed path
with open(f'{OUT}/compare_docs_396_410_cells.tsv', 'w') as f:
    f.write('doc\ttab\tpath\tdoc_share\tours_shortest_htr_readings\tours_all_readings\tours_linear\tdiff\n')
    for doc, base in DOCS.items():
        for sub in SUBS:
            hdr, paths = doc_paths(f'{base}/{fname(sub)}.csv')
            pop = 'le12' if doc == '396' else 'all'
            for p_, path in paths:
                a, b, c = D[(sub, pop)].get(path, (0, 0, 0))
                f.write(f'{doc}\t{sub}\t{path}\t{p_}\t{b:.4f}\t{a:.4f}\t{c:.4f}\t{b - p_:+.4f}\n')
print(open(f'{OUT}/compare_docs_reading_rules.tsv').read())
