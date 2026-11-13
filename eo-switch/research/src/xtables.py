#!/usr/bin/env python3
"""report/data/*.md (the tables of the write-up) and out/report_extra.json (numbers the text quotes that are not a
table cell), all from the result files in out/ (the per-coset features and distances of out/big/feat.npz, the
population weights of out/big, and the TSVs).  About a minute, under 1.5 GB.  usage: xtables.py"""
import os, sys, csv, json, collections
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import pop
from halfup import hu
OUT = os.path.normpath(os.path.join(HERE, '..', 'out')) + '/'
D = os.path.normpath(os.path.join(HERE, '..', '..', 'report', 'data')) + '/'
os.makedirs(D, exist_ok=True)
F = pop.feat(); d = F['d'].astype(int); P = pop.populations()
def T(name): return list(csv.DictReader(open(OUT + name), delimiter='\t'))
def pc(x, dd=None, rounded=None):
    """A share as a percentage.  One computed here from the counts: an exact half goes up (halfup.hu).  One read
    from a result file (text, or rounded=True) is 4 or 5 decimals of a number that has more, a 5 in its last place is
    no half, and it is formatted from the float as it always was."""
    if rounded is None: rounded = isinstance(x, str)
    share, x = x, float(x) * 100
    if x == 0: return '0%'
    if 99.95 <= x and dd is None: return '>99.9%'
    if dd is None: dd = 1 if x >= 1 else 2 if x >= 0.1 else 3
    return f'{x:.{dd}f}%' if rounded else f'{hu(share, dd, 100):.{dd}f}%'
def n_(x): return f'{int(x):,}'
def write(name, head, rows):
    out = ['| ' + ' | '.join(head) + ' |', '|' + '---|' * len(head)] + ['| ' + ' | '.join(str(x) for x in r) + ' |' for r in rows]
    open(D + name + '.md', 'w').write('\n'.join(out) + '\n')
E = {}
DRMS = ['4c4e', '4c2e', '3c2e', '7c8e', '8c8e', '2c2e', '4c6e', '3c4e', '3c6e', '5c4e', '5c6e', '6c6e']
def M(drm): return pop.drm_mask(int(drm[0]), int(drm[2]))
f = lambda k: F[k].astype(int)
pairs, side, ep, earm, carm, case, jzp = f('pairs'), f('side'), f('edges_paired'), f('earm'), f('carm'), f('corner_case'), f('jzp')
pph = f('pairs_plus_half_side_x2')
def stats(drm, mask):
    """share of the DRM, sub-7 (P1 exact), sub-6 and sub-8 (P1), P3 at L=5 (DR <= 6), P3 at L=6 (DR <= 5), attempts."""
    m = M(drm); sel = m & mask; n = sel.sum(); nm = m.sum()
    if n == 0: return None
    r = dict(n=int(n), share=n / nm, p6=(d[sel] <= 6).mean(), p5=(d[sel] <= 5).mean(), p7=(d[sel] <= 7).mean(),
             hits=int((d[sel] <= 6).sum()), hits_all=int((d[m] <= 6).sum()))
    for L, k in ((5, 6), (6, 5)):
        w = P[f'P3_{L}'][sel]; r[f'a{L}'] = int(w.sum()); r[f'q{L}'] = (w * (d[sel] <= k)).sum() / w.sum() if w.sum() else float('nan')
    return r
def verdict(p): return 'switch' if p > 0.5 else 'discard' if p < 0.1 else 'check'
def shown(v): return 'your call' if v == 'check' else v     # as printed: the cards call the middle band *your call*

# ------------------------------------------------------------------------------------------------------------------
# The rule cards: per DRM, groups of cells as a solver reads them on the switched side (first match wins).
ALL = np.ones(len(d), dtype=bool)
RULES = {
 '4c4e': [('switch', 'both bad U/D edges paired', ep == 2),
          ('check', 'one paired, edge ARM 1 (the two bad edges in different slices)', (ep == 1) & (earm == 1)),
          ('discard', 'one paired, edge ARM 0 or 2 (both bad edges in one slice)', ep == 1),
          ('discard', 'no bad edge paired', ALL)],
 '4c2e': [('switch', 'pairs + side pairs/2 is 1.5 or more', pph >= 3),
          ('check', 'pairs + side pairs/2 is exactly 1', pph == 2),
          ('discard', 'pairs + side pairs/2 is 0 or 0.5', ALL)],
 '3c2e': [('switch', 'always', ALL)],
 '7c8e': [('switch', '5 or 6 pairs', pairs >= 5),
          ('check', '4 pairs', pairs == 4),
          ('discard', '3 pairs or fewer', ALL)],
 '8c8e': [('check', 'corner ARM 0, 4 or 8', np.isin(carm, [0, 4, 8])),
          ('discard', 'corner ARM 2, 3, 5 or 6', ALL)],
 '2c2e': [('switch', 'a bad U/D edge with a pair', ep >= 1),
          ('check', 'no pair, but JZP', jzp == 1),
          ('discard', 'no pair, not JZP', ALL)],
 '4c6e': [('switch', 'JZP', jzp == 1),
          ('check', '4 pairs', pairs == 4),
          ('discard', 'anything else', ALL)],
 '3c4e': [('check', '2 pairs', pairs == 2),
          ('discard', '0 or 1 pair', ALL)],
 '3c6e': [('discard', 'always', ALL)],
 '5c4e': [('check', '3 pairs', pairs == 3),
          ('discard', '2 pairs or fewer', ALL)],
 '5c6e': [('check', '4 pairs', pairs == 4),
          ('discard', '3 pairs or fewer', ALL)],
 '6c6e': [('check', 'JZP, or 5 or 6 pairs', (jzp == 1) | (pairs >= 5)),
          ('discard', 'anything else', ALL)],
}
READ = {'4c4e': 'paired edges, then edge ARM', '4c2e': 'pairs and side pairs', '3c2e': 'nothing', '7c8e': 'pairs',
        '8c8e': 'corner ARM', '2c2e': 'paired edges, JZP', '4c6e': 'JZP, pairs', '3c4e': 'pairs', '3c6e': 'nothing',
        '5c4e': 'pairs', '5c6e': 'pairs', '6c6e': 'JZP, pairs'}
cards, cards_sum, cells, E['rule'] = [], [], [], {}
for drm in DRMS:
    m = M(drm); taken = np.zeros(len(d), dtype=bool); grp = collections.defaultdict(lambda: np.zeros(len(d), dtype=bool))
    rows = []
    for lab, txt, mask in RULES[drm]:
        sel = mask & ~taken & m; taken |= sel; grp[lab] |= sel
        s = stats(drm, sel); assert s, (drm, txt)
        assert verdict(s['p6']) == lab, (drm, txt, s['p6'])           # every printed verdict is the cell's own band
        rows.append((lab, txt, s))
    al = stats(drm, ALL); g = {k: stats(drm, v) for k, v in grp.items()}
    decided = sum(g[k]['share'] for k in g if k != 'check')
    kept = g['switch']['hits'] / al['hits'] if 'switch' in g else 0.0
    lost = g['discard']['hits'] / al['hits'] if 'discard' in g else 0.0
    for k, name in (('switch', 'switch'), ('check', 'your call'), ('discard', 'discard')):
        if k in g: cards.append([drm if k == next(x for x in ('switch', 'check', 'discard') if x in g) else '', f'**{name}**',
                                 '; '.join(t for lab, t, _ in rows if lab == k), pc(g[k]['share']), pc(g[k]['p6'])])
    cards_sum.append([drm, pc(al['p6']), pc(decided), pc(kept), pc(lost)])
    E['rule'][drm] = {'all': al, 'groups': g, 'decided': decided, 'kept': kept, 'lost': lost,
                      'cells': [(lab, t, s) for lab, t, s in rows]}
write('rule_cards', ['DRM', 'Verdict', 'What the switched case shows', 'Share of the DRM', 'Sub-7 rate'], cards)
write('rule_cards_sum', ['DRM', 'Sub-7 rate, whole DRM', 'Settled (share of the DRM in switch or discard)', "Sub-7 states switched (share of the DRM's sub-7s)", "Sub-7 states discarded (share of the DRM's sub-7s)"], cards_sum)
# cells table: drm shown once
seen = set(); rows = []; rows2 = []
for drm in DRMS:
    for lab, t, s in E['rule'][drm]['cells']:
        rows.append([drm if drm not in seen else '', t, shown(lab), n_(s['n']), pc(s['share']), pc(s['p6'])])
        rows2.append([drm if drm not in seen else '', t, pc(s['q5']), n_(s['a5']), pc(s['p7']), pc(s['p5'])])
        seen.add(drm)
write('rule_cells', ['DRM', 'Cell (read on the switched side)', 'Verdict', 'States', 'Share of the DRM', 'Sub-7 rate, exact'], rows)
write('rule_cells_rzp', ['DRM', 'Cell (read on the switched side)', 'Sub-7 rate, real attempts (RZP to 5)', 'Real attempts (RZP to 5)',
                         'DR in 7 or fewer, exact (for a 4-move RZP)', 'DR in 5 or fewer, exact (for a 6-move RZP)'], rows2)

# ------------------------------------------------------------------------------------------------------------------
# finer tables
def pl(n, w):
    """'1 pair', '2 pairs'"""
    return f'{n} {w}' + ('' if n == 1 else 's')
def cross(drm, rowsdef, name, head0):
    rows = []
    for txt, mask in rowsdef:
        s = stats(drm, mask)
        if s is None: continue
        rows.append([txt, n_(s['n']), pc(s['share']), pc(s['p6']), pc(s['q5']), n_(s['a5']), shown(verdict(s['p6']))])
    write(name, [head0, 'States', 'Share of the DRM', 'Sub-7 rate, exact', 'Sub-7 rate, real attempts (RZP to 5)', 'Real attempts (RZP to 5)', 'Band'], rows)
cross('4c4e', [(f'{e} paired, edge ARM {a}', (ep == e) & (earm == a)) for e in (0, 1, 2) for a in (0, 1, 2)], 'c44_paired_earm', 'Paired edges, edge ARM')
chk = (ep == 1) & (earm == 1)
cross('4c4e', [('4d corners (always corner ARM 2: ARM 21)', chk & (case == 3)),
               ('corner ARM 2 (ARM 21), 4b corners', chk & (carm == 2) & (case == 1)),
               ('corner ARM 2 (ARM 21), 4a corners', chk & (carm == 2) & (case == 0)),
               ('corner ARM 0 or 4, 4a corners', chk & np.isin(carm, [0, 4]) & (case == 0)),
               ('corner ARM 1 or 3 (4c corners)', chk & np.isin(carm, [1, 3])),
               ('corner ARM 0 or 4, 4b corners', chk & np.isin(carm, [0, 4]) & (case == 1))], 'c44_check', 'Inside *one paired, edge ARM 1*')
cross('4c4e', [(f"{pl(p, 'pair')} on {pl(e, 'edge')}" + (' (a bar)' if p == 2 and e == 1 else ''), (pairs == p) & (ep == e)) for p in range(5) for e in range(3)], 'c44_bars', 'Pairs, paired edges')
cross('4c2e', [(f"{pl(p, 'pair')}, {pl(s, 'side pair')}", (pairs == p) & (side == s)) for p in range(3) for s in range(3)], 'c42_cells', 'Pairs, side pairs')
c42 = pph == 2
cross('4c2e', [(f'corner ARM {a}', c42 & (carm == a)) for a in range(5)] + [(f'edge ARM {a}', c42 & (earm == a)) for a in range(3)]
      + [(f'4{"abcd"[c]} corners', c42 & (case == c)) for c in range(4)] + [('JZP', c42 & (jzp == 1))], 'c42_check', 'Inside *exactly 1*')
cross('8c8e', [(pl(p, 'pair'), pairs == p) for p in range(9)], 'c88_pairs', 'Pairs')
cross('7c8e', [(f'4 pairs, edge ARM {a}', (pairs == 4) & (earm == a)) for a in range(5)], 'c78_check', 'Inside *4 pairs*')
cross('7c8e', [(pl(p, 'pair'), pairs == p) for p in range(1, 7)], 'c78_pairs', 'Pairs')
cross('3c2e', [(pl(p, 'pair'), pairs == p) for p in range(2)], 'c32_pairs', 'Pairs')
cross('8c8e', [(f'corner ARM {a}', carm == a) for a in range(9)], 'c88_carm', 'Corner ARM')
# show the DRM once per block
out, last = [], None
for drm in ['4c6e', '3c4e', '3c6e', '5c4e', '5c6e', '6c6e']:
    for p in list(range(7)) + ['JZP']:
        s = stats(drm, (jzp == 1) if p == 'JZP' else (pairs == p))
        if not s: continue
        out.append([drm if drm != last else '', 'JZP' if p == 'JZP' else pl(p, 'pair'), n_(s['n']), pc(s['share']), pc(s['p6']), shown(verdict(s['p6']))]); last = drm
E['pairs_max'] = {drm: max(stats(drm, pairs == p)['p6'] for p in range(9) if stats(drm, pairs == p)) for drm in ['4c6e', '3c4e', '3c6e', '5c4e', '5c6e', '6c6e', '8c8e']}
E['arm_rate'] = {drm: {f'{a}{b}': stats(drm, (carm == a) & (earm == b))['p6'] for a in range(9) for b in range(5) if stats(drm, (carm == a) & (earm == b))} for drm in ['4c4e', '4c2e', '7c8e', '8c8e']}
write('low_pairs', ['DRM', 'Pairs on the switched case', 'States', 'Share of the DRM', 'Sub-7 rate, exact', 'Band'], out)
# 4c4e: ARM x paired edges (appendix)
rows, rowsn = [], []
for a in sorted(set((carm[M('4c4e')] * 10 + earm[M('4c4e')]).tolist())):
    r, rn = [f'{a // 10}{a % 10}'], [f'{a // 10}{a % 10}']
    for e in range(3):
        s = stats('4c4e', (carm == a // 10) & (earm == a % 10) & (ep == e))
        r.append(pc(s['p6']) if s else '-'); rn.append(n_(s['n']) if s else '-')
    s = stats('4c4e', (carm == a // 10) & (earm == a % 10)); r.append(pc(s['p6'])); rn.append(n_(s['n']))
    rows.append(r); rowsn.append(rn)
write('c44_arm_paired', ['ARM', 'No bad edge paired: sub-7 rate', 'One paired: sub-7 rate', 'Both paired: sub-7 rate', 'All: sub-7 rate'], rows)
write('c44_arm_paired_n', ['ARM', 'No bad edge paired: states', 'One paired: states', 'Both paired: states', 'All: states'], rowsn)

# ------------------------------------------------------------------------------------------------------------------
# strict separation of single features and of the rules (share of the DRM in cells under 10% or over 50%)
def strict(drm, keys):
    m = M(drm); vals = np.stack([F[k][m] for k in keys], 1)
    u, inv = np.unique(vals, axis=0, return_inverse=True); inv = inv.reshape(-1)
    n = np.bincount(inv); pos = np.bincount(inv, weights=(d[m] <= 6)); p = pos / n
    return float(n[(p < 0.1) | (p > 0.5)].sum() / n.sum())
E['strict'] = {drm: {k: strict(drm, k.split('+')) for k in ['carm+earm', 'pairs', 'edges_paired', 'pairs+carm+earm', 'corner_case+case_suffix', 'pairs+corner_case+case_suffix', 'edges_paired+earm', 'pairs_plus_half_side_x2']}
               for drm in ['4c4e', '4c2e', '7c8e', '8c8e', '2c2e']}

# ------------------------------------------------------------------------------------------------------------------
# existing rules graded (grades.tsv), with the rules of this study added
WHO = {
 '44-yura-good': ('ARM 00, 10, 21, 32, 42 ("good")', 'Yura Riabov [[D7871]] [[D7872]], Lewis Isom [[D7116]]'),
 '44-yura-decent': ('the "good" ARMs and the "decent" 31, 11', 'Yura Riabov [[D7872]]'),
 '44-yura-nottrash': ('anything but ARM 02, 12, 30, 40', 'Yura Riabov [[D7086]]'),
 '44-wen-reject': ('anything but ARM 01, 02, 12', 'wen [[D7282]] [[D7283]]'),
 '44-armthenpairs': ('ARM above 10% sub-7, then 2+ pairs', 'Yura Riabov [[D11021]]'),
 '44-caycala-5': ('RZP in 5: 3-4 pairs; 2 pairs with ARM 10, 11, 20, 21, 31, 32, 42a; 1 pair with 21; 0 pairs with 42', 'caycala (chart) [[D11016]]'),
 '44-caycala-5-strict': ("caycala's RZP-in-5 chart without the bracketed (10), (11), (20), (31)", 'caycala (chart) [[D11016]]'),
 '44-caycala-6': ('RZP in 6: 3-4 pairs, or 0 pairs with 42', 'caycala (chart) [[D11016]]'),
 '44-2pairs': ('2+ pairs', 'Jay [[T610]], rodneykinney [[T3225]], tseitsei89 [[D14265]] [[T9325]]'),
 '44-3pairs': ('3+ pairs', 'rodneykinney, *Domino Setup Theory*'),
 '44-3anypairs': ('3+ pairs counting side pairs', 'rodneykinney\'s older advice, as Jay put it [[T610]]'),
 '44-rodney-case': ('3-4 pairs; 2 pairs unless 4b-0; 1 pair if 4d-2', 'rodneykinney [[T8108]]'),
 '44-rodney-case+0p': ('3-4 pairs; 2 pairs unless 4b-0; 1 pair if 4d-2; 0 pairs if 4a-0 or 4d-2 with no fake pairs', 'rodneykinney [[T8108]] [[T8123]]'),
 '44-tetrad': ('4d needs 1+ pair, 4b-0 3+, everything else 2+', 'rodneykinney [[D12095]]'),
 '44-complex': ('3+ pairs; 2 pairs unless 4b; 1 pair only if 4d', 'compLex [[D13425]]'),
 '44-tseitsei': ('2+ pairs, or 1 pair and 4d', 'tseitsei89 [[T9321]]'),
 '44-subsets': ('per corner case: 4a-0 2+p, 4a-2 1+p, 4a-4 edge ARM 2, 4b-0 3+p, 4b-2 2+p and edge ARM 1, 4c 2+p, 4d 1+p and edge ARM 1', 'rodneykinney, *DRM Subsets*'),
 '44-jay': ('2+ pairs; fewer only if JZP or anti-JZP, or 1 pair and 4d', 'Jay [[D12085]]'),
 '44-wen': ('2+ pairs; 1 pair if 4d or one U/D turn from 4d; 0 pairs if anti-AR', 'wen [[D14326]] [[D14347]]'),
 '44-fanti': ('2+ pairs; 1 pair with ARM 21; 0 pairs with JZP or ARM 42', 'Fanti, *armpairs_1.txt* [[D15160]]'),
 '44-daichi-4': ('RZP in 4 (DR in 7): 2-4 pairs; 1 pair except 20d, 22d; 0 pairs except 02, 30, 40, 01b, 41b, 20d, 2c with all corners on U', 'Daichi [[D18953]]'),
 '44-caycala-3p': ('3+ pairs unless all bad corners on one layer', 'caycala [[D13393]]'),
 '44-always-4': ('RZP in 4 (DR in 7): always', 'Zagros [[D18940]]'),
 '42-noah': ('ARM 00, 10, 31', 'Noah Swor [[D7838]], Lewis Isom [[D7116]]'),
 '42-yura': ('ARM 00, 10, 31, 20, 21, 41', 'Noah Swor, Yura Riabov [[D7838]] [[D7840]] [[D7842]]'),
 '42-caycala': ('2 pairs; 1 pair with edge ARM 1 or ARM 10; 0 pairs only JZP', 'caycala [[D12728]]'),
 '42-jay': ('1 pair and 1 side pair, or 2 pairs', 'Jay [[T8144]]'),
 '42-rodney': ('1+ pair and 1+ side pair', 'rodneykinney [[T9257]], *DRM Subsets*'),
 '42-tseitsei': ('2 pairs, or 1 pair and a side pair', 'tseitsei89 [[T9321]]'),
 '42-rodney-case': ('2 pairs unless 4a; 1 pair unless 4a or 4b-2', 'rodneykinney (table) [[T8140]]'),
 '42-fanti': ('any pair; 0 pairs with JZP', 'Fanti, *armpairs_1.txt* [[D15160]]'),
 '42-15': ('"1.5+ pairs" (pairs + side pairs/2)', 'rodneykinney [[T9468]]'),
 '78-lewis': ('ARM 10, 21, 11, 63', 'Lewis Isom [[D7116]]'),
 '78-rodney': ('5 or 6 pairs', 'rodneykinney [[T8142]]'),
 '78-tseitsei-a': ('5 pairs; 4 pairs with edge ARM under 2', 'tseitsei89 [[T9314]]'),
 '78-tseitsei-b': ('4+ pairs, then edge ARM under 2, or edge ARM 1 or 3 and corner ARM over 3', 'tseitsei89 [[T9282]]'),
 '78-image': ('5-6 pairs; 4 pairs with ARM 21, 31, 43; 3 pairs with 21', 'chart attached to Brayan'"'"'s question [[D13502]]'),
 '78-fanti': ('5+ pairs; 4 pairs with ARM 21, 31, 43; 3 pairs with 21', 'Fanti, *armpairs_1.txt* [[D15160]]'),
 '78-tseitsei-c': ('drop the 0% ARMs, then 5+ pairs, or 4 pairs with edge ARM under 2', 'tseitsei89 [[T9321]]'),
 '32-always': ('always', 'rodneykinney [[T9294]], tseitsei89 [[T9321]] [[D7286]]'),
 '32-wen': ('a pair, a fake pair or a split pair', 'wen [[D16512]]'),
 '32-fanti-6': ('RZP in 6 (DR in 5): a pair; 0 pairs with ARM 00, 21, 31', 'Fanti, *armpairs_1.txt* [[D15160]]'),
 '46-jzp': ('only JZP', 'Yura Riabov [[D6915]], *Hitchhiker\'s Guide to DR*'),
 '46-radek': ('4 pairs or JZP', 'Radek B [[D7471]] [[D7472]]'),
 '46-tseitsei': ('JZP with b corners', 'tseitsei89 [[T9321]]'),
 '46-rodney': ('3+ pairs and corner ARM under 4', 'rodneykinney, *DRM Subsets*'),
 '88-lewis': ('ARM 00, 84, 01, 31, 63', 'Lewis Isom [[D7116]]'),
 '88-tseitsei': ('3+ fake pairs and edge ARM not 2', 'tseitsei89 [[T9568]] [[T9572]]'),
 '88-correct': ('R L (one R/L quarter-turn pair) gives JZP', 'Jay [[T3767]], Yura Riabov [[D16930]]'),
 '34-rodney': ('2+ pairs', 'rodneykinney [[T8312]], *DRM Subsets*'),
 '34-fanti': ('2 pairs; 1 pair with ARM 00 or 21', 'Fanti [[D15179]]'),
 '36-jay': ('ARM 21 only', 'Jay [[D6982]]'),
 '36-fanti': ('3 pairs with ARM 00, or 2 pairs with ARM 21', 'Fanti [[D15179]]'),
 '54-doc319': ('3+ pairs', 'rodneykinney, *DRM Subsets Meta*'),
 '54-subset': ('2+ pairs and 2+ side pairs', 'rodneykinney, *DRM Subsets*'),
 '56-doc319': ('4+ pairs', 'rodneykinney, *DRM Subsets Meta*'),
 '66-doc319': ('3+ pairs', 'rodneykinney, *DRM Subsets Meta*'),
 '22-doc319': ('1+ pairs', 'rodneykinney, *DRM Subsets Meta*'),
}
BOTH = {'4c4e': 'both bad edges paired, or one paired with edge ARM 1', '4c2e': 'pairs + side pairs/2 is 1 or more', '7c8e': '4 or more pairs',
        '2c2e': 'a paired edge, or JZP', '4c6e': 'JZP or 4 pairs'}
G = T('grades.tsv'); gi = collections.defaultdict(dict)
for r in G: gi[r['id']][r['population']] = r
assert set(gi) == set(WHO), set(gi) ^ set(WHO)
rows = []; E['grade'] = {}
order = ['4c4e', '4c2e', '3c2e', '7c8e', '8c8e', '2c2e', '4c6e', '3c4e', '3c6e', '5c4e', '5c6e', '6c6e']
for drm in order:
    ids = [i for i in gi if gi[i]['P1']['drm'] == drm]
    first = True
    # this study's rule: switch group, and switch + your-call group
    g = E['rule'][drm]['groups']; al = E['rule'][drm]['all']
    for lab, sel in (('switch', ('switch',)), ('switch + your call', ('switch', 'check'))):
        if not all(k in g for k in sel) or 'switch' not in g: continue
        sh = sum(g[k]['share'] for k in sel); hits = sum(g[k]['hits'] for k in sel)
        att = sum(g[k]['a5'] for k in sel); ah = sum(g[k]['a5'] * g[k]['q5'] for k in sel)
        txt = '; '.join(t for l2, t, _ in E['rule'][drm]['cells'] if l2 in sel) if lab == 'switch' else BOTH[drm]
        rows.append([drm if first else '', f'**{txt}**', '**this study** (' + lab + ')', pc(sh), pc(hits / (sh * al['n'])), pc(hits / al['hits']), pc((al['hits'] - hits) / al['n']), pc(ah / att)])
        first = False
    for i in sorted(ids, key=lambda i: -float(gi[i]['P1']['precision'])):
        a, b = gi[i]['P1'], gi[i]['P3_5']; rule, who = WHO[i]
        if a['target'] != 'DR<=6' and 'DR in' not in rule: rule += f" (target {a['target'].replace('DR<=', 'DR in ')})"
        rows.append([drm if first else '', rule, who, pc(a['share_switched']), pc(a['precision']), pc(a['recall']), pc(a['target_states_discarded']), pc(b['precision'])])
        first = False
        E['grade'][i] = {k: float(a[k]) for k in ('share_switched', 'precision', 'recall', 'target_states_discarded')}
        E['grade'][i]['p3'] = float(b['precision'])
write('grades', ['DRM', 'Switch when', 'Who', 'Switches (share of the DRM)', 'Sub-7 among switched', "Sub-7 states switched (share of the DRM's sub-7s)", 'Sub-7 states discarded (share of the DRM)', 'Real attempts: sub-7 among switched'], rows)

# ------------------------------------------------------------------------------------------------------------------
# populations: the RZP bias and the switch
pp = T('populations.tsv')
def popv(drm, popn, side, L, col='p_le6'):
    r = [r for r in pp if r['drm'] == drm and r['population'] == popn and r['side'] == side and r['L'] == str(L)]
    assert len(r) == 1, (drm, popn, side, L); return float(r[0][col])
rows = []; E['pop'] = {}
for drm in DRMS:
    v = [popv(drm, 'P1', 'any', 0), popv(drm, 'P2', 'same side', 5), popv(drm, 'P2', 'switched', 5), popv(drm, 'P3', 'switched', 5), popv(drm, 'P3', 'switched', 6, 'p_le5')]
    n5 = int(float([r for r in pp if r['drm'] == drm and r['population'] == 'P3' and r['side'] == 'switched' and r['L'] == '5'][0]['weight_or_attempts']))
    rows.append([drm] + [pc(x, rounded=True) for x in v] + [n_(n5)]); E['pop'][drm] = v
write('populations', ['DRM', 'Sub-7 rate, uniform (the tables)', 'Sub-7 rate after an RZP of 5, same side', 'Sub-7 rate after an RZP of 5, switched', 'Sub-7 rate, real attempts, RZP to 5, switched', 'DR in 5 or fewer, real attempts, RZP to 6, switched', 'Real attempts (RZP to 5)'], rows)
su = T('checks_switch_uniform.tsv')
E['uniform_worst_z'] = max(abs(float(r['z_20_batches'])) for r in su); E['uniform_cells'] = len(su)
E['attempts_total'] = 121527134
# options after the switch (P3, L = 5)
rows = []; E['opt'] = {}
for drm in ['4c4e', '4c2e', '3c2e', '7c8e', '8c8e']:
    m = M(drm); n0 = P['P3_5'][m].sum()
    v = [(P['P3_5'][m] * (d[m] <= 6)).sum() / n0, P['P3_5_alt6'][m].sum() / n0, P['P3_5_two6'][m].sum() / n0, P['P3_5_all6'][m].sum() / n0]
    rows.append([drm] + [pc(x) for x in v]); E['opt'][drm] = v
write('options', ['DRM', 'Sub-7 rate, switched', 'Sub-7 rate, also EO\'s last turn either way', 'Sub-7 rate, also the better DR axis', 'Sub-7 rate, both'], rows)
vb = {r['drm']: r for r in T('variants_by_drm.tsv')}
E['var'] = {k: {c: float(v) for c, v in r.items() if c != 'drm'} for k, r in vb.items()}
rows, rows2 = [], []
for drm in DRMS:
    r = vb[drm]
    rows.append([drm, n_(r['cosets']), r['mean_d'], pc(r['plain_le5']), pc(r['plain_le6']), pc(r['plain_le7'])])
    rows2.append([drm, pc(r['lastF_le6']), pc(r['lastFB_le6']), pc(r['two_le6']), pc(r['inv_le6'])])
write('variants', ['DRM', 'States', 'Mean turns to DR', 'DR in 5 or fewer', 'DR in 6 or fewer', 'DR in 7 or fewer'], rows)
write('variants_options', ['DRM', 'DR in 6 or fewer, EO\'s last turn free', 'DR in 6 or fewer, last two EO turns free (F B)', 'DR in 6 or fewer, better DR axis', 'DR in 6 or fewer, better of normal and inverse'], rows2)
E['last_rzp'] = open(OUT + 'checks_last_rzp_turn.txt').read().split()[:2]

# ------------------------------------------------------------------------------------------------------------------
# which feature adds most (computer only: information measures), from q4.tsv and feature_value.tsv
q4 = T('q4.tsv'); E['q4'] = {r['what']: r['answer'] for r in q4}
FD = ['4c4e', '4c2e', '7c8e', '8c8e', '2c2e']
rows = [[lab] + [pc(E['strict'][drm][k]) for drm in FD] for k, lab in [('carm+earm', 'ARM'), ('pairs', 'Pairs'), ('edges_paired', 'Paired edges'), ('corner_case+case_suffix', 'Corner case (4 corners)'),
        ('pairs+carm+earm', 'Pairs + ARM'), ('pairs+corner_case+case_suffix', 'Pairs + corner case'), ('edges_paired+earm', 'Paired edges + edge ARM'), ('pairs_plus_half_side_x2', 'Pairs + side pairs/2')]]
write('decided_by_feature', ['Split by'] + [f'{drm}: settled' for drm in FD], rows)
# bars vs two edges, per 4c4e ARM (q4.tsv)
rows = []; E['bars'] = {}
for r in q4:
    w = r['what']
    if w.startswith('4c4e ARM ') and 'as a bar' in w:
        arm = w.split()[2].rstrip(','); a = r['answer'].split(' / '); nn = r['size'].replace(' states', '').split(' / ')
        rows.append([arm, pc(a[0]), pc(a[1]), n_(nn[0]), n_(nn[1])]); E['bars'][arm] = [float(a[0]), float(a[1])]
write('bars', ['ARM', 'Sub-7 rate, bar on one edge', 'Sub-7 rate, pairs on the two edges', 'States, bar on one edge', 'States, pairs on the two edges'], rows)
# wen's 2-of-3 (q4)
E['wen23'] = {}
for r in q4:
    w = r['what']
    if 'switching the best' in w or w == '4c4e, 2+ pairs alone':
        key = w.split('), ')[-1] if 'switching' in w else 'pairs alone'
        E['wen23'][key] = r['answer']
# the search: best rules per size (computer-only ones marked)
st = T('search_top.tsv')
E['search'] = {f"{r['drm']}|{r['features']}": r for r in st}
NICE = {'fam_4c4e': 'setup turns to an R/L-quarter-turn finish', 'fam_7c8e': 'setup turns to an R U L finish', 'fam_4c6e': 'setup turns to an R h L finish',
        'fam_4c2e': 'setup turns to an R h R finish', 'corner_dist': 'moves to orient the corners', 'earm': 'edge ARM', 'carm': 'corner ARM', 'pairs': 'pairs',
        'arm_corner_case': 'orbit case of the out-of-AR corners', 'edges_same_layer': 'bad edges in one layer', 'lr_split': 'bad corners split L/R',
        'pairs_plus_half_side_x2': 'pairs + side pairs/2', 'edges_paired': 'paired edges', 'jzp': 'JZP', 'bars': 'bars', 'fake': 'fake pairs'}
rows = []
for r in st:
    if r['pareto'] != 'yes': continue
    comp = any(k.startswith(('fam_', 'corner_dist', 'moves_to', 'udmoves')) for k in r['features'].split('+')) or int(r['cells']) > 12
    usable = '**computer only**' if comp else 'by hand'
    if r['features'] == 'fam_4c4e': usable = 'its half turns by hand (section 4); with the U/D turns **computer only**'
    rows.append([r['drm'], ' + '.join(NICE.get(k, k) for k in r['features'].split('+')), r['cells'], pc(r['strict_sep_P1']), usable])
write('search_pareto', ['DRM', 'Features crossed', 'Cells in the table', 'Settled (share of the DRM in cells under 10% or over 50%)', 'Usable'], rows)
E['c88_65'] = E['search']['8c8e|earm+pairs+arm_corner_case']
E['fam44'] = E['search']['4c4e|fam_4c4e']
E['low_best'] = {}
for line in open(OUT + 'SUMMARY.md'):
    if 'put at most 4c6e' in line:
        s = line.split('put at most ')[1].split(' of their')[0]
        for part in s.split(', '):
            k, v = part.split(); E['low_best'][k] = float(v)

# ------------------------------------------------------------------------------------------------------------------
# reproduction of published numbers
rp = T('reproduce.tsv'); E['repro'] = {'n': len(rp), 'match': sum(1 for r in rp if r['verdict'].startswith(('match', 'within')))}
by = collections.OrderedDict()
SRCN = {'C1': 'Cale, *DR setup stats*', 'C2': 'Cale, *DR setup stats (switching last move of EO)*', 'A1': 'rodneykinney, *DRM Subsets*', 'A2': 'FakeMMAP; my EO-to-DR study',
        'A5': 'rodneykinney (which ARM each corner case can have)', 'C6': 'Louis, twist splits', 'C7': 'Louis, corner case by ARM', 'C8': 'rodneykinney, *DRM corner variant+pair stats*',
        'C9': 'rodneykinney, *DRM Subsets* ranking and trees', 'C12': 'Evan, *4c4e ARM subtype stats* (sampled)', 'C13': 'Evan, *arm/pairs* (sampled)',
        'C15': 'Radek B, tables from Louis\'s data (images)', 'C16': 'Levi Gibson, *Sub-7 simulations* (sampled)', 'C18': 'my EO-to-DR study'}
for r in rp:
    k = r['source'].split()[0]
    if k == 'A1' and 'C9' in r['source']: k = 'C9'
    by.setdefault(k, [0, 0]); by[k][0] += 1; by[k][1] += r['verdict'].startswith(('match', 'within'))
rows = [[SRCN[k], n_(v[0]), n_(v[1])] for k, v in by.items()]
write('reproduce', ['Source', 'Numbers compared', 'Reproduced'], rows)
E['repro_by'] = {k: v for k, v in by.items()}
E['mismatch'] = [{k: r[k] for k in ('source', 'quantity', 'published', 'ours', 'verdict')} for r in rp if not r['verdict'].startswith(('match', 'within'))]
# claims
E['claims'] = {r['id']: r for r in T('claims.tsv')}
E['checks_niss'] = {r['check']: [int(r['cubes']), int(r['holds'])] for r in T('checks_niss.tsv')}
E['checks_trace'] = {f"{r['check']}|{r['sample']}": [int(r['cubes']), int(r['holds'])] for r in T('checks_trace.tsv')}
E['checks_variants'] = {r['quantity']: r for r in T('checks_variants.tsv')}
E['nissy'] = T('checks_nissy.tsv')[0]
E['features_tests'] = sum(1 for l in open(OUT + 'checks_features.txt') if l.startswith('ok'))
E['features_lines'] = sum(1 for l in open(OUT + 'checks_features.txt') if l.strip())
E['dist'] = [l.split() for l in open(OUT + 'dist_hist.txt') if not l.startswith('#')]
E['dist_mean'] = open(OUT + 'dist_hist.txt').readline().split('mean ')[1].strip()
# the 4c4e rule's 6 cells, as one number each (text), and the shares of the four hand rules quoted in section 1
json.dump(E, open(OUT + 'report_extra.json', 'w'), indent=1, default=lambda o: float(o) if isinstance(o, (np.floating, np.integer)) else str(o))
print('tables:', len(os.listdir(D)), 'extra keys:', len(E))
