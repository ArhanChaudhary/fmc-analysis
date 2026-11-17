"""The switch cards (v2): per DRM, an ordered list of groups of switched cases, each defined by quick reads.
A group is (label, mask, verdict) with verdict 'switch', 'time' (the next ones to add if you have time) or 'skip'.
The groups of a DRM partition it.  BASE holds the current policies they are compared with.
`python cards.py` prints every card with its exact numbers."""
import numpy as np, sys, os
from lib import *
import rules as R0
F['ccs'] = F['corner_case'] * 10 + F['case_suffix']; F['arm'] = F['carm'] * 10 + F['earm']; F['cc'] = F['corner_case']
P = F['pairs']; ARM = F['arm']; CA = F['carm']; EA = F['earm']; CC = F['cc']; CCS = F['ccs']; SIDE = F['side']; FAKE = F['fake']
COLS = F['cols_bad']; EP = F['edges_paired']; HC = F['hole_cfg']; UDS = F['ud_split']; ESL = F['edges_same_layer'].astype(bool); SPLIT = F['split_pairs']
A, B, C, D = 0, 1, 2, 3
def arm_in(*codes): return np.isin(ARM, codes)
CARDS = {}
def card(drm, groups):
    """Append the 'anything else' group and check the partition."""
    c, e = drm; m = drm_mask(c, e); tot = np.zeros(N0, bool); out = []
    for name, g, v in groups:
        g = g & m & ~tot if name.startswith('+') else g & m
        name = name.lstrip('+')
        assert not (g & tot).any(), (drm, name)
        assert g.any(), (drm, name)
        tot |= g; out.append((name, g, v))
    if (m & ~tot).any(): out.append(('anything else', m & ~tot, 'skip'))
    CARDS[drm] = out
# ------------------------------------------------------------------ 4c4e
card((4, 4), [
 ('3 or 4 pairs', P >= 3, 'switch'),
 ('2 pairs on two edges', (P == 2) & (EP == 2), 'switch'),
 ('2 pairs on one edge (a bar), holes on one R/L face', (P == 2) & (EP == 1) & (HC == 0), 'switch'),
 ('2 pairs on one edge (a bar), holes not on one R/L face, 2 fake pairs', (P == 2) & (EP == 1) & (HC >= 1) & (FAKE == 2), 'switch'),
 ('1 pair, ARM 21, 4d corners', (P == 1) & (ARM == 21) & (CC == D), 'switch'),
 ('1 pair, ARM 21, 4b corners, 0 or 2 side pairs', (P == 1) & (ARM == 21) & (CC == B) & (SIDE != 1), 'switch'),
 ('1 pair, ARM 20, 21 or 22, 4a corners in two columns, 1+ side pairs', (P == 1) & (CA == 2) & (CC == A) & (COLS == 2) & (SIDE >= 1), 'switch'),
 ('0 pairs, no fake pairs, corners 2 and 2 in the layers', (P == 0) & (FAKE == 0) & (UDS == 2), 'switch'),
 ('2 pairs on one edge (a bar), holes not on one R/L face, 0 or 1 fake pairs', (P == 2) & (EP == 1) & (HC >= 1) & (FAKE <= 1), 'time'),
 ('1 pair, ARM 10 or 11, 2 or 3 side pairs', (P == 1) & arm_in(10, 11) & (SIDE >= 2), 'time'),
 ('1 pair, ARM 20, 21 or 22, 4a corners in two columns, no side pair', (P == 1) & (CA == 2) & (CC == A) & (COLS == 2) & (SIDE == 0), 'skip'),
 ('1 pair, ARM 20, 21 or 22, 4a corners not in two columns', (P == 1) & (CA == 2) & (CC == A) & (COLS != 2), 'skip'),
 ('1 pair, ARM 21, 4b corners, exactly 1 side pair', (P == 1) & (ARM == 21) & (CC == B) & (SIDE == 1), 'skip'),
 ('+1 pair, anything else', P == 1, 'skip'),
 ('+0 pairs, anything else', P == 0, 'skip'),
])
# ------------------------------------------------------------------ 4c2e
card((4, 2), [
 ('2 pairs (a bar)', P == 2, 'switch'),
 ('1 pair and a side pair', (P == 1) & (SIDE >= 1), 'switch'),
 ('0 pairs, JZP (ARM 00) with 4b corners', (P == 0) & (ARM == 0) & (CC == B), 'switch'),
 ('1 pair, no side pair, 4b-0 corners', (P == 1) & (SIDE == 0) & (CCS == 10), 'switch'),
 ('1 pair, no side pair, 4a-2 corners', (P == 1) & (SIDE == 0) & (CCS == 2), 'time'),
 ('1 pair, no side pair, ARM 31', (P == 1) & (SIDE == 0) & (ARM == 31) & (CCS != 2) & (CCS != 10), 'time'),
 ('+1 pair, anything else', P == 1, 'skip'),
 ('+0 pairs, anything else', P == 0, 'skip'),
])
# ------------------------------------------------------------------ 3c2e
card((3, 2), [
 ('1 pair', P == 1, 'switch'),
 ('0 pairs, a fake pair or a split pair', (P == 0) & ((FAKE >= 1) | (SPLIT >= 1)), 'switch'),
 ('0 pairs, no fake pair, no split pair', (P == 0) & (FAKE == 0) & (SPLIT == 0), 'time'),
])
# ------------------------------------------------------------------ 7c8e
card((7, 8), [
 ('6 pairs, not ARM 64', (P == 6) & (ARM != 64), 'switch'),
 ('5 pairs, not ARM 20 or 54', (P == 5) & ~arm_in(20, 54), 'switch'),
 ('4 pairs, ARM 21, 31 or 43', (P == 4) & arm_in(21, 31, 43), 'switch'),
 ('3 pairs, ARM 21', (P == 3) & (ARM == 21), 'switch'),
 ('4 pairs, ARM 11, 12, 33, 41 or 62', (P == 4) & arm_in(11, 12, 33, 41, 62), 'time'),
 ('+4 pairs, anything else', P == 4, 'skip'),
 ('+5 or 6 pairs with ARM 20, 54 or 64', P >= 5, 'skip'),
 ('+3 pairs or fewer', P <= 3, 'skip'),
])
# ------------------------------------------------------------------ 8c8e
card((8, 8), [
 ('8 pairs', P == 8, 'switch'),
 ('6 pairs, corner ARM 4', (P == 6) & (CA == 4), 'switch'),
 ('5 pairs, edge ARM 1 or 3', (P == 5) & np.isin(EA, (1, 3)), 'switch'),
 ('2 pairs, ARM 42', (P == 2) & (ARM == 42), 'switch'),
 ('4 pairs, ARM 42', (P == 4) & (ARM == 42), 'switch'),
 ('4 pairs, ARM 02, 43, 63 or 82', (P == 4) & arm_in(2, 43, 63, 82), 'time'),
 ('+6 pairs, corner ARM not 4', P == 6, 'skip'),
 ('+5 pairs, edge ARM 2', P == 5, 'skip'),
])
# ------------------------------------------------------------------ 2c2e
card((2, 2), [
 ('1 pair', P == 1, 'switch'),
 ('2 pairs and a side pair', (P == 2) & (SIDE >= 1), 'switch'),
 ('0 pairs, 1 side pair, ARM 00 or 11', (P == 0) & (SIDE == 1) & arm_in(0, 11), 'switch'),
 ('0 pairs, JZP (ARM 00), no side pair', (P == 0) & (SIDE != 1) & (ARM == 0), 'time'),
])
# ------------------------------------------------------------------ the low DRMs
card((4, 6), [
 ('4 pairs on three edges', (P == 4) & (EP == 3), 'switch'),
 ('3 pairs, JZP (ARM 00)', (P == 3) & (ARM == 0), 'switch'),
 ('3 pairs on three edges, the three bad edges in one layer', (P == 3) & (ARM != 0) & (EP == 3) & ESL, 'switch'),
 ('3 pairs on three edges, corners 2 and 2 in the layers', (P == 3) & (ARM != 0) & (EP == 3) & ~ESL & (UDS == 2), 'switch'),
])
card((3, 4), [
 ('2 pairs and a side pair', (P == 2) & (SIDE >= 1), 'switch'),
 ('2 pairs, no side pair, a fake pair', (P == 2) & (SIDE == 0) & (FAKE >= 1), 'switch'),
 ('1 pair, 2 side pairs', (P == 1) & (SIDE == 2), 'switch'),
 ('1 pair, ARM 21, 1 side pair, 2 fake pairs or holes on one R/L face', (P == 1) & (ARM == 21) & (SIDE == 1) & ((FAKE == 2) | (HC == 0)), 'switch'),
 ('1 pair, ARM 21, 1 side pair, the rest', (P == 1) & (ARM == 21) & (SIDE == 1) & ~((FAKE == 2) | (HC == 0)), 'time'),
])
card((3, 6), [
 ('2 pairs, ARM 21, 1 or 2 fake pairs', (P == 2) & (ARM == 21) & (FAKE >= 1), 'switch'),
 ('2 pairs, ARM 12, 2 fake pairs', (P == 2) & (ARM == 12) & (FAKE == 2), 'switch'),
 ('2 pairs, ARM 01', (P == 2) & (ARM == 1), 'switch'),
])
card((5, 4), [
 ('3 pairs, 2+ side pairs', (P == 3) & (SIDE >= 2), 'switch'),
 ('2 pairs, ARM 21, 2+ side pairs', (P == 2) & (ARM == 21) & (SIDE >= 2), 'switch'),
 ('1 pair, ARM 21, 2+ side pairs, 2+ fake pairs', (P == 1) & (ARM == 21) & (SIDE >= 2) & (FAKE >= 2), 'switch'),
 ('3 pairs, 0 or 1 side pair', (P == 3) & (SIDE <= 1), 'time'),
])
card((5, 6), [
 ('4 pairs', P == 4, 'switch'),
 ('3 pairs, ARM 21, 3 side pairs', (P == 3) & (ARM == 21) & (SIDE == 3), 'switch'),
 ('2 pairs, ARM 21, 3 side pairs', (P == 2) & (ARM == 21) & (SIDE == 3), 'switch'),
 ('3 pairs, ARM 21, fewer than 3 side pairs', (P == 3) & (ARM == 21) & (SIDE != 3), 'time'),
])
card((6, 6), [
 ('5 or 6 pairs', P >= 5, 'switch'),
 ('3 pairs, 3 fake pairs, corners 3 and 3 in the layers', (P == 3) & (FAKE == 3) & (UDS == 3), 'switch'),
])

# ------------------------------------------------------------------ the current policies
def rule(rid): return [r for r in R0.RULES if r[0] == rid][0][4](F)
NEVER = np.zeros(N0, bool)
CCS2 = (CC == A) & (CCS != 2)                      # 4a-0 and 4a-4
BASE = {   # drm -> list of (key, short name, who / where, mask); the first one is the pairs policy
 (4, 4): [('pairs', '2+ pairs', 'DRM Subsets Meta; tseitsei89', P >= 2),
          ('pairs+case', '2+ pairs, or 1 pair with 4d corners', 'tseitsei89', rule('44-tseitsei')),
          ('pairs+case2', '3-4 pairs; 2 pairs unless 4b-0; 1 pair if 4d-2; 0 pairs if 4a-0 or 4d-2 with no fake pairs', 'rodneykinney', rule('44-rodney-case+0p')),
          ('wen', '2+ pairs; 1 pair if 4d or one U/D turn from 4d; 0 pairs if anti-AR or the D F2 B2 R case', 'wen', rule('44-wen')),
          ('chart', '3-4 pairs; 2 pairs with ARM 10, 11, 20, 21, 31, 32 or 42a; 1 pair with ARM 21; 0 pairs with ARM 42', 'caycala', rule('44-caycala-5')),
          ('pairs+arm', '2+ pairs; 1 pair with ARM 21; 0 pairs with JZP or ARM 42', 'Fanti', rule('44-fanti'))],
 (4, 2): [('pairs', '1.5+ pairs (2 side pairs = 1 pair)', 'DRM Subsets Meta; rodneykinney; Jay', rule('42-15')),
          ('pairs+case', '2 pairs unless 4a-0 or 4a-4; 1 pair unless 4a-0, 4a-4 or 4b-2', 'rodneykinney', ((P == 2) & ~CCS2) | ((P == 1) & ~CCS2 & (CCS != 12))),
          ('pairs+arm', '2 pairs; 1 pair with edge ARM 1 or ARM 10; 0 pairs only JZP', 'caycala', rule('42-caycala')),
          ('pairs+arm2', '1+ pairs; 0 pairs with JZP', 'Fanti', rule('42-fanti'))],
 (3, 2): [('pairs', 'always', 'DRM Subsets Meta; tseitsei89', drm_mask(3, 2)),
          ('wen', 'a pair, a fake pair or a split pair', 'wen', rule('32-wen'))],
 (7, 8): [('pairs', '5+ pairs, counting edge ARM under 2 as a pair', 'DRM Subsets Meta; tseitsei89', rule('78-tseitsei-a')),
          ('pairs0', '5 or 6 pairs', 'rodneykinney', P >= 5),
          ('chart', '5-6 pairs; 4 pairs with ARM 21, 31, 43; 3 pairs with ARM 21; never edge ARM 0 or 4, except ARM 10', 'caycala', rule('78-caycala')),
          ('pairs+arm', '5+ pairs; 4 pairs with ARM 21, 31, 43; 3 pairs with ARM 21', 'Fanti', rule('78-fanti'))],
 (8, 8): [('pairs', '3 or fewer fake pairs (5+ pairs), with edge ARM not 2 or 6+ pairs', 'rodneykinney\'s tree', rule('88-tree-6p'))],
 (2, 2): [('pairs', '1+ pairs', 'DRM Subsets Meta', P >= 1)],
 (4, 6): [('pairs', 'never', 'DRM Subsets Meta', NEVER), ('jzp', 'only JZP', 'Yura Riabov', rule('46-jzp')), ('radek', '4 pairs or JZP', 'Radek B', rule('46-radek'))],
 (3, 4): [('pairs', '2+ pairs', 'DRM Subsets Meta (sometimes)', P >= 2), ('pairs+arm', '2 pairs; 1 pair with ARM 00 or 21', 'Fanti', rule('34-fanti'))],
 (3, 6): [('pairs', 'never', 'not on the DRM Subsets Meta list', NEVER), ('pairs+arm', '3 pairs with ARM 00; 2 pairs with ARM 21', 'Fanti', rule('36-fanti'))],
 (5, 4): [('pairs', 'never', 'DRM Subsets Meta', NEVER), ('jay', '2 pairs with ARM 21, or 3+ pairs', 'Jay', ((P == 2) & (ARM == 21)) | (P >= 3))],
 (5, 6): [('pairs', 'never', 'DRM Subsets Meta', NEVER), ('jay', '3 pairs with ARM 21, or 4+ pairs', 'Jay', ((P == 3) & (ARM == 21)) | (P >= 4))],
 (6, 6): [('pairs', 'never', 'DRM Subsets Meta', NEVER)],
}
# where each current policy was stated: Discord message ids (expanded to dated links by the report builder)
SRC = {((4, 4), 'pairs'): '[[T9325]]', ((4, 4), 'pairs+case'): '[[T9321]]', ((4, 4), 'pairs+case2'): '[[T8108]], [[T8123]]', ((4, 4), 'wen'): '[[D14328]]',
       ((4, 4), 'chart'): '[[D11016]]', ((4, 4), 'pairs+arm'): '[[D15160]]',
       ((4, 2), 'pairs'): '[[T9468]], [[T8144]]', ((4, 2), 'pairs+case'): '[[T8140]], [[T8149]]', ((4, 2), 'pairs+arm'): '[[D12728]]', ((4, 2), 'pairs+arm2'): '[[D15160]]',
       ((3, 2), 'pairs'): '[[T9321]]', ((3, 2), 'wen'): '[[D16512]]',
       ((7, 8), 'pairs'): '[[T9321]]', ((7, 8), 'pairs0'): '[[T8142]]', ((7, 8), 'chart'): '[[D11016]]', ((7, 8), 'pairs+arm'): '[[D15160]]',
       ((8, 8), 'pairs'): '[[T9558]], [[T9569]]', ((4, 6), 'jzp'): '[[D6915]]', ((4, 6), 'radek'): '[[D7471]]', ((3, 4), 'pairs+arm'): '[[D15179]]', ((3, 6), 'pairs+arm'): '[[D15179]]',
       ((5, 4), 'jay'): '[[D12983]]', ((5, 6), 'jay'): '[[D12983]]'}
def card_mask(drm, tiers=('switch',)):
    sw = np.zeros(N0, bool)
    for name, g, v in CARDS[drm]:
        if v in tiers: sw |= g
    return sw
if __name__ == '__main__':
    w = weights()
    for (c, e), groups in CARDS.items():
        m = drm_mask(c, e); n = m.sum(); cum = np.zeros(N0, bool)
        dd = d[m]
        print(f'===== {c}c{e}e  n={n} le4 {(dd<=4).sum()} d5 {(dd==5).sum()} d6 {(dd==6).sum()}')
        for name, g, v in groups:
            cum |= g
            h = np.bincount(d[g], minlength=11); a = w[d[g]].sum(); b = (d[g] > 6).sum()
            pr = profile(m, cum)
            print(f'{v:6s} {name:62s} {100*g.sum()/n:5.1f}% sub7 {100*h[:7].sum()/max(g.sum(),1):5.1f}% le4 {h[:5].sum():4d} d5 {h[5]:4d} d6 {h[6]:5d} ratio {a/max(b,1):6.2f} | sw {100*pr["switch"]:5.1f}% miss {100*pr["miss_le4"]:4.1f} {100*pr["miss_d5"]:4.1f} {100*pr["miss_d6"]:4.1f} loss {pr["loss"]:.4f}')
        print(f'   CARD            ', fmt(profile(m, card_mask((c, e)))))
        print(f'   CARD + time     ', fmt(profile(m, card_mask((c, e), ('switch', 'time')))))
        for key, name, who, sw in BASE[(c, e)]:
            print(f'   {key:12s}    ', fmt(profile(m, sw)), '|', name, '(' + who + ')')
