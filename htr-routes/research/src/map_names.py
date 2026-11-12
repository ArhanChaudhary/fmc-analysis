#!/usr/bin/env python3
"""Which of our subsets each older sheet's row label means, decided by the sheet's own example for that row:
doc 15 (HTR Subset Stats, Notes tab: one trigger per row) and doc 66 (Extra Quarter-Turn Stats, "Random Example").
Doc 171 (allcases) uses the same labels as doc 66 (beef beans' scheme, D8537).  Each example is run through
`htrtools nisshtr`, which prints its subset; a label is mapped when its example lands in one subset.
Output: out/name_map.tsv"""
import csv, re, subprocess, os, sys
from common import R, OUT
TOOL = os.environ.get('HTRTOOLS', f'{R}/htrtools/target/release/htrtools')
EXACT = '/data/fmc/judging-a-dr/research/data/lean_exact_table.u8'
G = '/data/fmc/kb/docs/gsheet'
rows = []
for r in csv.reader(open(f'{G}/17iChOoeB205t3wHTXMLrjM9si2vtxRgFeYR2z3pn1i0/Notes.csv')):
    if len(r) > 2 and re.search(r'qt', r[1] or '') and r[0].strip():
        rows.append(('doc15', r[1].strip(), r[0].strip()))
for r in csv.reader(open(f'{G}/1fPCjS1ZQlP_Munut9MQkSbsL3CEdtT3LC5h3R8OMHGw/No_Sorting.csv')):
    if len(r) > 13 and re.match(r'^\d', r[0] or '') and r[13].strip():
        rows.append(('doc66', r[1].strip(), re.sub(r'\s*\(\d+\)\s*$', '', r[13]).strip()))
inp = '\n'.join(x[2].replace('’', "'") for x in rows) + '\n'
p = subprocess.run(['systemd-run', '--user', '--scope', '-q', '-p', 'MemoryMax=3G', TOOL, 'nisshtr', EXACT],
                   input=inp, capture_output=True, text=True, check=True)
res = [l.split('\t') for l in p.stdout.strip().split('\n')]
with open(f'{OUT}/name_map.tsv', 'w') as f:
    f.write('doc\tlabel\texample\tour_subset\tnormal_label\tinverse_label\n')
    for (doc, lab, ex), r in zip(rows, res):
        f.write(f'{doc}\t{lab}\t{ex}\t{r[1]}\t{r[2]}\t{r[3]}\n')
        print(doc, lab, '->', r[1], r[2], r[3])
