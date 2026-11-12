#!/usr/bin/env python3
"""Cell-by-cell comparison with docs 396 ("Sub-13 Optimal Niss-HTR Paths") and 410 ("Optimal Niss-HTR Paths") and
with doc 171 ("allcases").

Docs 396/410: for each subset x edge tab, each listed path P with share p.  Our share of P = the share of sampled
states (25,000 per tab; for doc 396 only those with optimal <= 12, which is how its header cell reads) for which some
NISS reading of some optimal finish has the full chain P (F keys: a label at the start and after every quarter turn
of the whole finish, bracket = after the switch).  For the 0c0 tabs also the share among states that are already
in HTR (half of 0c0 0e is HTR, the other half is U D' times HTR).

Doc 171: one optimal per state, linear, no ties (D8302); compared with `htrtools tie` (expected share of each linear
chain when one optimal is picked uniformly at random), translated to beef beans' labels with out/name_map.tsv
(doc 171 uses the same row labels as doc 66, whose examples fix the meaning).

Outputs: out/compare_docs_396_410.tsv (every doc path), out/compare_docs_396_410_tabs.tsv (per tab summary),
out/compare_doc171.tsv"""
import csv, os, re, collections, glob
import numpy as np
from common import *

G = '/data/fmc/kb/docs/gsheet'
DOCS = {'396': f'{G}/1etiCnl6U-OHQAjEZIVIlk9iE64OXK3lrCyy14TLE_wE', '410': f'{G}/1D4qUhLOsJrwsBEzUVfmnLikuQNNB_eSZiPq-nS8KPN4'}

def doc_paths(path):
    rows = []; header = None
    for r in csv.reader(open(path)):
        r = [x.strip() for x in r]
        if not any(r): continue
        if header is None and r[0] == '' and len(r) > 1:
            header = r[1]; continue
        for i, x in enumerate(r):
            if re.match(r'^\d*\.?\d+$', x) and i + 1 < len(r) and LAB.match(r[i + 1].lstrip('(')):
                labs = [y for y in r[i + 1:] if y]
                rows.append((float(x), ' > '.join(labs)))
                break
    return header, rows

def main():
    K = keys()
    out = open(f'{OUT}/compare_docs_396_410.tsv', 'w')
    out.write('doc\ttab\tpath\tdoc_share\tour_share\tdiff\tour_share_htr_states\tour_share_non_htr_states\tn_states\n')
    tabs = open(f'{OUT}/compare_docs_396_410_tabs.tsv', 'w')
    tabs.write('doc\ttab\tdoc_header\tour_share_opt_le12\tpaths_listed\tpaths_never_seen\tmean_abs_diff\tmax_abs_diff\t'
               'top_doc_path\ttop_doc_share\tour_top_path\tour_top_share\tour_paths_ge5pct_missing_in_doc\n')
    for sub in SUBS:
        st = load_states(sub); rt = Routes(sub)
        n = rt.n
        is_f = np.array([K[r][0] == 'F' for r in rt.rid])
        sel = is_f & (rt.delta == 0)
        s_idx, r_idx = rt.state[sel], rt.rid[sel]
        le12 = st['d'] <= 12
        inh = st['htrN'] == 0
        for doc, base in DOCS.items():
            fn = f'{base}/{fname(sub)}.csv'
            if not os.path.exists(fn): continue
            header, paths = doc_paths(fn)
            pop = le12 if doc == '396' else np.ones(n, bool)
            m = pop[s_idx]
            cnt = collections.Counter(r_idx[m].tolist())
            npop = pop.sum()
            share = {K[r][2:]: c / npop for r, c in cnt.items()}
            cnt_h = collections.Counter(r_idx[m & inh[s_idx]].tolist()); nh = (pop & inh).sum()
            cnt_n = collections.Counter(r_idx[m & ~inh[s_idx]].tolist()); nn = (pop & ~inh).sum()
            sh_h = {K[r][2:]: c / nh for r, c in cnt_h.items()} if nh else {}
            sh_n = {K[r][2:]: c / nn for r, c in cnt_n.items()} if nn else {}
            diffs = []; unseen = 0
            for p, path in paths:
                o = share.get(path, 0.0)
                if path not in share: unseen += 1
                diffs.append(abs(o - p))
                out.write(f'{doc}\t{sub}\t{path}\t{p}\t{o:.4f}\t{o - p:+.4f}\t{sh_h.get(path, 0):.4f}\t{sh_n.get(path, 0):.4f}\t{npop}\n')
            listed = {p for _, p in paths}
            ours_top = sorted(share.items(), key=lambda x: -x[1])
            missing = [f'{k} ({v:.3f})' for k, v in ours_top if v >= 0.05 and k not in listed]
            tp = max(paths) if paths else (0, '')
            tabs.write(f'{doc}\t{sub}\t{header}\t{le12.mean():.4f}\t{len(paths)}\t{unseen}\t{np.mean(diffs):.4f}\t{max(diffs):.4f}\t'
                       f'{tp[1]}\t{tp[0]}\t{ours_top[0][0]}\t{ours_top[0][1]:.4f}\t{"; ".join(missing[:6])}\n')
        print(sub, flush=True)

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
    if 'doc171' in sys.argv: doc171('tie'); doc171('tiels')
    else: main()
