#!/usr/bin/env python3
"""Cell-by-cell comparison with doc 171 ("allcases"): one optimal per state, linear, no ties (D8302); compared
with `htrtools tie` (expected share of each linear chain when one optimal is picked uniformly at random), translated
to beef beans' labels with out/name_map.tsv (doc 171 uses the same row labels as doc 66, whose examples fix the
meaning).

Outputs: out/compare_doc171.tsv (full finish), out/compare_doc171_leave_slice.tsv"""
import csv, os, re, collections, glob
import numpy as np
from common import *

G = '/data/fmc/kb/docs/gsheet'

def doc171(src='tie'):
    # doc 171's 2qt(a)/(b) are the reverse of doc 66's (doc 66's own examples fix its labels; doc 171 lists
    # "3qt 0cXe > 2qt(b) 4c4e", which only exists if 2qt(b) = 4a2): doc 171 2qt(a) = 4b2, 2qt(b) = 4a2, as in doc 15
    nm = {}
    for r in csv.DictReader(open(f'{OUT}/name_map.tsv'), delimiter='\t'):
        if r['doc'] == 'doc66':
            lab = r['label']
            lab = lab.replace('2qt(a)', 'X').replace('2qt(b)', '2qt(a)').replace('X', '2qt(b)')
            nm[r['our_subset']] = lab
    # beef beans' labels for the subsets the doc 66 examples did not cover: "<q>qt <n>c<e>e", 2qt(a)/(b) from doc 66
    def lab(s):
        if s in nm: return nm[s]
        c, e = s.split(); q = c[-1]; nc = c[0]
        return f'{q}qt {nc}c{e}'
    tie = collections.defaultdict(dict)
    for r in csv.DictReader(open(f'{R}/out/big/{src}.tsv'), delimiter='\t'):
        tie[r['subset']][r['chain']] = (float(r['expected_share']), float(r['share_some']), float(r['share_all']))
    rows = []
    for r in csv.reader(open(f'{G}/1Vo6XzCFtJ-HEAuaBmk_pac-sJ3TbxEBb7BKsRJ_2wpA/allcases.csv.csv')):
        r = [x.strip() for x in r if x.strip()]
        if len(r) >= 2 and re.match(r'^[\d.]+$', r[0]):
            rows.append((float(r[0]), r[1:]))
    rev = {}
    for s in SUBS: rev[lab(s)] = s
    out = open(f'{OUT}/compare_doc171{"_leave_slice" if src == "tiels" else ""}.tsv', 'w')
    out.write('doc171_start\tour_subset\tdoc_chain\tdoc_share\tour_expected_share_random_tiebreak\tour_share_some_optimal\tour_share_every_optimal\n')
    for p, chain in rows:
        start = chain[0]
        s = rev.get(start)
        if s is None: continue
        # translate every label of the chain
        ours = []
        ok = True
        for x in chain:
            t = rev.get(x)
            if t is None: ok = False; break
            ours.append(t)
        if not ok: continue
        # our chains are written with side letters (4a3/4b3, 4a4/4b4) and frame edges; compare after mapping 4a3/4b3 -> 4c3
        def norm(c):
            return re.sub(r'4[ab]([34])', r'4c\1', c)
        key = norm(' > '.join(ours))
        e = s_ = a = 0.0
        for ch, (ex, so, al) in tie[s].items():
            if norm(ch[2:]) == key:
                e += ex; s_ = max(s_, so); a = max(a, al)
        out.write(f'{start}\t{s}\t{" > ".join(chain)}\t{p}\t{e:.4f}\t{s_:.4f}\t{a:.4f}\n')

if __name__ == '__main__':
    import sys
    doc171('tie'); doc171('tiels')
