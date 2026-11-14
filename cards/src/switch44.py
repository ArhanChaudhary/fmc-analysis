#!/usr/bin/env python3
"""Decision card "Should I switch this EO?", 4c4e part: the current switch rule (2+ top pairs, or 1 top pair with
ARM 21) split by what NISS tracing adds, the half turns to two bars.  Exact over every EO-solved 4c4e case of the
EO-switch study (research/out/big: feat.npz features, d.u8 optimal DR after the switch, rings.npz half turns to two
bars); the switched case is uniform whatever RZP made it (EO-switch section 8), so these are the odds after a switch.
JZP (DR on the other axis reachable with that axis's DR moves; on 4c4e exactly ARM 00) is a row of its own.

Output: cards/data/switch44.tsv (one row per group) and cards/data/switch44_rules.tsv (one row per rule).
usage: switch44.py"""
import os, sys
import numpy as np
sys.path.insert(0, '/data/fmc/eo-switch/research/src')
import pop
HERE = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(HERE, '..', 'data')
F = pop.feat(); d = F['d'].astype(int)
hb = np.load('/data/fmc/eo-switch/research/out/big/rings.npz')['hbar']
m44 = pop.drm_mask(4, 4)
jz = m44 & (F['jzp'] == 1); m = m44 & (F['jzp'] == 0)
p, ca, ea, h = F['pairs'], F['carm'], F['earm'], hb
groups = [
    ('jzp', 'JZP (ARM 00 on 4c4e)', jz),
    ('p2_le2', '2+ top pairs, 2 or fewer half turns to two bars', m & (p >= 2) & (h <= 2)),
    ('p2_3', '2+ top pairs, 3 half turns to two bars', m & (p >= 2) & (h == 3)),
    ('p2_45', '2+ top pairs, 4 or 5 half turns to two bars', m & (p >= 2) & (h >= 4)),
    ('p1_arm21', '1 top pair, ARM 21', m & (p == 1) & (ca == 2) & (ea == 1)),
    ('p1_other', '1 top pair, other ARM', m & (p == 1) & ~((ca == 2) & (ea == 1))),
    ('p0', 'no top pair', m & (p == 0)),
]
y5, y6 = d <= 5, d <= 6
N44, NN = int(m44.sum()), int(m.sum())
with open(os.path.join(OUT, 'switch44.tsv'), 'w') as f:
    f.write('key\tgroup\tcases\tshare_of_4c4e\tshare_of_nonjzp\tp_le6\tp_le5\tof_nonjzp_le6\tof_nonjzp_le5\n')
    for k, name, g in groups:
        n = int(g.sum())
        f.write(f"{k}\t{name}\t{n}\t{n / N44:.9f}\t{(n / NN if k != 'jzp' else float('nan')):.9f}\t{y6[g].mean():.9f}\t{y5[g].mean():.9f}\t"
                f"{((g & y6).sum() / (m & y6).sum() if k != 'jzp' else float('nan')):.9f}\t{((g & y5).sum() / (m & y5).sum() if k != 'jzp' else float('nan')):.9f}\n")
cur = m & ((p >= 2) | ((p == 1) & (ca == 2) & (ea == 1)))
rules = [('current', '2+ top pairs, or 1 top pair with ARM 21 (what people switch now)', cur),
         ('first', 'only 2+ top pairs with 2 or fewer half turns to two bars', m & (p >= 2) & (h <= 2)),
         ('first_arm21', 'that, plus 1 top pair with ARM 21', m & (((p >= 2) & (h <= 2)) | ((p == 1) & (ca == 2) & (ea == 1))))]
with open(os.path.join(OUT, 'switch44_rules.tsv'), 'w') as f:
    f.write('key\trule\tshare_switched\tp_le6\tp_le5\tcaught_le6\tcaught_le5\n')
    for k, name, s in rules:
        f.write(f"{k}\t{name}\t{s.sum() / NN:.9f}\t{y6[s].mean():.9f}\t{y5[s].mean():.9f}\t{(s & y6).sum() / (m & y6).sum():.9f}\t{(s & y5).sum() / (m & y5).sum():.9f}\n")
print('4c4e', N44, 'non-JZP', NN, 'JZP', int(jz.sum()), '| wrote switch44.tsv, switch44_rules.tsv')
