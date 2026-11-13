#!/usr/bin/env python3
"""The DR-in-6 and DR-in-7 lines of Cale's two sheets, read from the knowledge base's copies (kb/docs/gsheet), for the
readings of Noah Swor's "1/7 … instead of 1/3" (D6979): the first sheet *DR setup stats* (doc 6, one side, EO kept) and
its last-move version (doc 40), whose tab "EO ends in F*" lets the EO's last turn go either way and whose tab "EO ends
in F* B*" lets the EO's last two turns (F and B) go either way.  Each line is checked against this study's own count
(pop.targets: plain, lastF, lastFB).  Output: out/cale_sheets.json, {tab: {total, le6, le7}}.  usage: cale_sheets.py"""
import os, sys, csv, json, re
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import numpy as np
import pop
KB = '/data/fmc/kb/docs/gsheet/'
FIRST = KB + '11bTZ4Y7_6qKlIWo4a4TLW45M2ZkctQZAVxgQqEtlUs0/'      # DR setup stats
LAST = KB + '1_2PmFv1KyBX335SjSb4oweS0sx804fIhbuP50D-gBj4/'      # DR setup stats (switching last move of EO)
# tab file -> (DRM of this study, which count, extra mask)
TABS = {
 'last F 4e4c': (LAST + '4e4c_F_.csv', '4c4e', 'lastF', None),
 'last F 2e4c': (LAST + '2e4c_F_.csv', '4c2e', 'lastF', None),
 'last F 8e7c': (LAST + '8e7c_F_.csv', '7c8e', 'lastF', None),            # one of the two mirror halves of 7c8e
 'last F 8e8c(4+4)': (LAST + '8e8c_4_4_F_.csv', '8c8e', 'lastF', '44'),  # the cases with a 4-4 twist split
 'last F B 4e4c': (LAST + '4e4c_F_B_.csv', '4c4e', 'lastFB', None),
 'last F B 2e4c': (LAST + '2e4c_F_B_.csv', '4c2e', 'lastFB', None),
 'first 6e3c': (FIRST + 'DR-6e3c.csv', '3c6e', 'plain', None),            # one of the two mirror halves of 3c6e
}
def read(path):
    rows = list(csv.reader(open(path, encoding='utf-8')))
    total = int(re.search(r'out of ([\d,]+)', rows[0][3]).group(1).replace(',', ''))
    le = {}
    for r in rows:
        m = re.match(r'\s*≤(\d+) moves?', r[0]) if r else None
        if m: le[int(m.group(1))] = int(float(r[3]))
    return dict(total=total, le6=le[6], le7=le.get(7))
F = pop.feat(); out = {}
T = {k: pop.targets(k) for k in (6, 7)}
for tab, (path, drm, key, extra) in TABS.items():
    s = read(path); out[tab] = s
    m = pop.drm_mask(int(drm[0]), int(drm[2]))
    if extra == '44': m = m & (F['tw1'] == 4) & (F['tw2'] == 4)
    for k in (6, 7):
        if s[f'le{k}'] is None: continue
        ours = float(T[k][key][m].mean()); sheet = s[f'le{k}'] / s['total']
        assert abs(ours - sheet) < 1e-9, (tab, k, ours, sheet)
    print(f"{tab:18s} DR <= 6: {s['le6']:>6,} of {s['total']:>6,} = 1 in {s['total'] / s['le6']:.2f}" + (f"; DR <= 7: 1 in {s['total'] / s['le7']:.2f}" if s['le7'] else '') + '  (equals this study)')
json.dump(out, open(os.path.join(pop.OUT, 'cale_sheets.json'), 'w'), indent=1)
