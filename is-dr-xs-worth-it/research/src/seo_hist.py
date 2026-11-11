#!/usr/bin/env python3
"""From a slice-EO skip, how far is the nearest DR-1s / DR-2s 8fe / real DR?  Exact, over every coset.

The view: the slice is the E slice (its pieces have no U/D colour); the slice EO is for the F/B axis (family A, which
also covers R/L by symmetry) or for the slice's own axis U/D (family B); all four pieces oriented, or all misoriented.
Each of the four skip conditions picks 1/16 of the 2,217,093,120 cosets.  The distance tables come from
`xstools bfs` (out/bfs/<rule>_<class>.u8): rule eo-fb / eo-ud = no quarter turns of the F/B resp. U/D faces (every
edge keeps its orientation for that axis), rule all = any turns.  255 = cannot be reached under the rule."""
import sys, os, json, itertools
import numpy as np
import coords
B = '/data/fmc/is-dr-xs-worth-it/research/out/bfs/'
NCO, NEO, NSL = 2187, 2048, 495
KIND_M = np.array([1 if p[0] == 0 and p[1] != 0 else 0 for p in coords.EDGES], dtype=np.uint8)     # M-slice places
bits = np.array([[(v >> i) & 1 for i in range(11)] + [bin(v).count('1') & 1] for v in range(NEO)], dtype=np.uint8)   # eo -> 12 bits
def masks():
    out = {k: np.zeros((NEO, NSL), dtype=bool) for k in ('A oriented', 'A misoriented', 'B oriented', 'B misoriented')}
    for sl, comb in enumerate(coords.COMB_LIST):
        idx = list(comb)
        b = bits[:, idx]; s = b.sum(axis=1)
        out['A oriented'][:, sl] = s == 0; out['A misoriented'][:, sl] = s == 4
        bu = b ^ KIND_M[idx]; s = bu.sum(axis=1)
        out['B oriented'][:, sl] = s == 0; out['B misoriented'][:, sl] = s == 4
    return {k: v.reshape(-1) for k, v in out.items()}
def hist(table, mask):
    t = np.memmap(B + table + '.u8', dtype=np.uint8, mode='r')
    h = np.zeros(256, dtype=np.int64); n = NEO * NSL
    for co in range(NCO):
        h += np.bincount(np.asarray(t[co * n:(co + 1) * n])[mask], minlength=256)
    return {int(d): int(c) for d, c in enumerate(h) if c}
if __name__ == '__main__':
    M = masks()
    for k, v in M.items(): assert v.sum() * 16 == NEO * NSL, k
    res = {}
    want = sys.argv[1:] or ['eo-fb_1s', 'eo-fb_2s8fe', 'eo-fb_dr', 'eo-ud_1s', 'eo-ud_2s8fe', 'eo-ud_dr', 'all_1s', 'all_2s8fe', 'all_dr']
    for tab in want:
        if not os.path.exists(B + tab + '.hist'): print('missing', tab); continue
        fams = ('A oriented', 'A misoriented') if tab.startswith(('eo-fb', 'seo-fb')) else ('B oriented', 'B misoriented') if tab.startswith(('eo-ud', 'seo-ud')) else tuple(M)
        for fam in fams:
            h = hist(tab, M[fam]); res[f'{tab} | {fam}'] = h
            tot = sum(h.values()); reach = tot - h.get(255, 0)
            mean = sum(d * c for d, c in h.items() if d != 255) / max(reach, 1)
            print(f'{tab:14s} {fam:14s} reachable {100 * reach / tot:6.2f}%  mean {mean:5.2f}  ' + ' '.join(f'{d}:{100 * c / tot:.2f}%' for d, c in sorted(h.items()) if d != 255 and 100 * c / tot >= 0.005))
    p = '/data/fmc/is-dr-xs-worth-it/research/out/seo_hist.json'
    old = json.load(open(p)) if os.path.exists(p) else {}
    old.update(res); json.dump(old, open(p, 'w'), indent=0)
