"""Tables of the page's sections on pairs before HTR (true pairs at 2qt once the rule is passed, HTR-equivalent
pairs), from ../out/meta/pairs{m}.json and the exact table ../out/meta/htable.tsv.  Used by mkreport.py."""
import json
import numpy as np, pandas as pd

import os
QT = tuple(int(c) for c in os.environ.get('PAIRTABS_QT', '234'))      # the page uses all three; fewer only for a partial look
PR = {m: json.load(open(f'../out/meta/pairs{m}.json')) for m in QT}
HT = pd.read_csv('../out/meta/htable.tsv', sep='\t', comment='#')
NCLASS = int(HT.classes.sum())
assert NCLASS == 29400

def pct(x, d=0): return f'{100 * x:.{d}f}%'
def num(x, d=0): return f'{x:,.{d}f}'
def table(head, rows, align=None):
    align = align or (['---'] + ['---:'] * (len(head) - 1))
    s = '| ' + ' | '.join(head) + ' |\n|' + '|'.join(align) + '|\n'
    for r in rows: s += '| ' + ' | '.join(str(c) for c in r) + ' |\n'
    return s
def sh(n, w, d=1, least=150): return pct(w / n, d) if n >= least else '·'
P2L = ['0–1', '2–3', '4–5', '6–7', '8 or more']
def binrow(m, key, lab):
    for l, n, w in PR[m]['p2_bins'][key]:
        if l == lab: return n, w
    return 0, 0
def orow(m, key): return PR[m]['orders'][key]

# ---- true pairs at 2qt, with and without the rule (HTRs of the fixed reach) --------------------------------
t_p2rule = table(['Pairs at 2qt'] + [x for m in QT for x in (f'{m}qt: no rule', f'{m}qt: rule passed')],
                 [[lab] + [sh(*binrow(m, k, lab)) for m in QT for k in ('reach', 'rule_reach')] for lab in P2L]
                 + [['**Ranker score**'] + [f"{PR[m]['auc'][k]['pn2']:.2f}" for m in QT for k in ('reach', 'rule_reach')]]
                 + [['Ranker score inside one DR'] + [f"{PR[m]['wauc'][k]['pn2'][0]:.2f}" for m in QT for k in ('reach', 'rule_reach')]])
def lift(m, key):
    lo = binrow(m, key, '0–1'); hi = binrow(m, key, '6–7')
    return (hi[1] / hi[0]) / (lo[1] / lo[0])
def p2post(m):
    rows = []
    for post, bins, a, _, _ in PR[m]['p2_by_post']:
        if post > 3: continue
        rows.append([post] + [sh(n, w, 0, 100) for _, n, w in bins] + [f'{a:.2f}' if a is not None else '·'])
    return table(['S+T after 2qt'] + [f'{l} pairs at 2qt' for l in P2L] + ['Ranker score'], rows)
t_p2post = {m: p2post(m) for m in QT}
ORD2 = [('No rule, any order', 'none|random'), ('No rule, most pairs at 2qt first', 'none|pairs at 2qt'),
        ('Rule passed, any order', 'rule|random'), ('Rule passed, most pairs at 2qt first', 'rule|pairs at 2qt'),
        ('Rule passed, most pairs at HTR first', 'rule|pairs at HTR'),
        ('Both floors, any order', 'both|random'), ('Both floors, most pairs at 2qt first', 'both|pairs at 2qt'),
        ('Both floors, most pairs at HTR first', 'both|pairs at HTR')]
OH = ['Order of finishing'] + [x for m in QT for x in (f'{m}qt: found within 5', f'{m}qt: within 10')]
t_p2order = table(OH,
                  [[lab] + [pct(orow(m, key)['R'][k]) for m in QT for k in ('5', '10')] for lab, key in ORD2])
def routes_p2(m):
    rows = []
    for lab, per, n, has, nr, hasr, _, _ in PR[m]['routes_by_p2']:
        rows.append([lab, num(per, 1), sh(n, has, 1, 100), sh(n, nr, 0, 100), sh(nr, hasr, 0, 100)])
    return table(['Pairs at 2qt', 'Routes to 2qt per DR', 'Hold a within-goal HTR', 'Have an HTR that passes the rule', 'Hold a within-goal HTR, of those'], rows)
t_routes_p2 = {m: routes_p2(m) for m in QT}

# ---- HTR-equivalent pairs: the exact table ------------------------------------------------------------------
def exact(qt, lo):
    s = HT[HT.qt == qt]; tot = s.classes.sum()
    rows = []
    for k, v in s.groupby('htr_pairs'):
        n = v.classes.sum()
        if n / tot < 0.002: continue
        mean = (v.moves_to_htr * v.classes).sum() / n
        cum = [v[v.moves_to_htr <= lo + i].classes.sum() / n for i in range(4)]
        rows.append([int(k), pct(n / tot, 1), int(v.moves_to_htr.min()), f'{mean:.1f}'] + [pct(c) if c > 0 else '–' for c in cum])
    return table(['HTR-equivalent pairs', 'Share of states', 'Shortest HTR', 'Mean moves to HTR'] + [f'HTR within {lo + i} moves' for i in range(4)], rows)
t_hexact = {2: exact(2, 3), 3: exact(3, 5)}
def exact_sub(qt, subs, ks):
    rows = []
    s = HT[HT.qt == qt]
    for sub in subs:
        v = s[s.subset == sub]
        r = [sub, pct(v.classes.sum() / s.classes.sum())]
        for k in ks:
            w = v[v.htr_pairs == k]
            r.append(f'{(w.moves_to_htr * w.classes).sum() / w.classes.sum():.1f}' if w.classes.sum() else '–')
        rows.append(r)
    return table(['Subset', 'Share of states'] + [f'{k} pairs' for k in ks], rows)
t_hsub = {2: exact_sub(2, ['4b2 2e', '4b2 4e', '4b2 0e', '4a2 4e', '4a2 2e'], [4, 6, 8, 10, 12]),
          3: exact_sub(3, ['2c3 2e', '2c3 4e', '2c3 6e', '4c3 2e', '4c3 4e', '0c3 4e'], [4, 6, 8, 10, 12])}
def exact_cell(qt, sub, k, upto):
    v = HT[(HT.qt == qt) & (HT.htr_pairs == k)]
    if sub: v = v[v.subset == sub]
    return v[v.moves_to_htr <= upto].classes.sum() / v.classes.sum()
def exact_mean(qt, sub, k):
    v = HT[(HT.qt == qt) & (HT.htr_pairs == k)]
    if sub: v = v[v.subset == sub]
    return (v.moves_to_htr * v.classes).sum() / v.classes.sum()
def exact_min(qt, k):
    return int(HT[(HT.qt == qt) & (HT.htr_pairs == k)].moves_to_htr.min())
def qt_share(qt): return HT[HT.qt == qt].classes.sum() / NCLASS

# ---- HTR-equivalent pairs in the sample ---------------------------------------------------------------------
def st(m, key): return PR[m]['states'].get(key)
def sides_table(key, gaps=(-8, -6, -4, -2, 0, 2, 4, 6, 8)):
    """States with 2 (or 3) quarter turns left, 2qt to 4qt DRs pooled: which side has the shorter HTR, by the gap."""
    acc = {}
    for m in QT:
        o = st(m, key)
        if not o: continue
        for gap, n, a, b, c, d in o['sides_by_gap']:
            x = acc.setdefault(gap, [0, 0, 0, 0, 0.0]); x[0] += n; x[1] += a; x[2] += b; x[3] += c; x[4] += d * n
    rows = []
    for gap in gaps:
        if gap not in acc or acc[gap][0] < 300: continue
        n, a, b, c, d = acc[gap]
        lab = 'the same on both' if gap == 0 else (f'{gap} more on normal' if gap > 0 else f'{-gap} more on inverse')
        rows.append([lab, pct(n / sum(v[0] for v in acc.values()), 1), pct(a / n), pct(b / n), pct(c / n), f'{d / n:+.1f}'])
    return table(['HTR-equivalent pairs', 'Share of states', 'HTR is shorter on normal', 'Same length', 'Shorter on inverse', 'Moves saved on normal (mean)'], rows), acc
t_hsides, SIDES = {}, {}
for key in ('2|2', '3|3'):
    t_hsides[key], SIDES[key] = sides_table(key)
def sides_right(key, mingap):
    """Among states whose counts differ by at least `mingap`: the side with more has the shorter HTR / the longer one."""
    acc = SIDES[key]; n = a = c = 0
    for gap, v in acc.items():
        if abs(gap) >= mingap:
            n += v[0]; a += v[1] if gap > 0 else v[3]; c += v[3] if gap > 0 else v[1]
    return a / n, c / n
def hvals(m, key, col='hn2'):
    return {int(k): (n, w) for k, n, w in PR[m][col + '_vals'][key]}
KS = (4, 6, 8, 10, 12)
def t_hgoal_for(m):
    rows = []
    for k in KS:
        r = [k]
        for key, col in (('reach', 'hn2'), ('rule_reach', 'hn2'), ('rule_reach', 'hi2')):
            v = hvals(m, key, col); n, w = v.get(k, (0, 0)); tot = sum(x[0] for x in v.values())
            r += [pct(n / tot), sh(n, w, 1, 100)]
        rows.append(r)
    rows.append(['**Ranker score**', '–', f"{PR[m]['auc']['reach']['hn2']:.2f}", '–', f"{PR[m]['auc']['rule_reach']['hn2']:.2f}", '–', f"{PR[m]['auc']['rule_reach']['hi2']:.2f}"])
    return table(['HTR-equivalent pairs at 2qt', 'In reach: share of HTRs', 'In reach: within goal', 'Rule passed: share of HTRs', 'Rule passed: within goal',
                  'Rule passed, counted on the inverse: share of HTRs', 'Rule passed, counted on the inverse: within goal'], rows)
t_hgoal = {m: t_hgoal_for(m) for m in QT}
t_hauc = table(['Read at 2qt'] + [f'{m}qt' for m in QT],
               [[lab] + [f"{PR[m]['auc']['rule_reach'][c]:.2f}" for m in QT] for lab, c in (('True pairs', 'pn2'), ('HTR-equivalent pairs', 'hn2'), ('HTR-equivalent pairs on the inverse', 'hi2'),
                                                                                   ('True pairs, then the inverse count among equals', 'p2hi'))]
               + [['Fewer moves from 2qt to HTR'] + [f"{1 - PR[m]['auc']['rule_reach']['rem2']:.2f}" for m in QT]]
               + [['Pairs at HTR, for comparison'] + [f"{PR[m]['auc']['rule_reach']['pn0']:.2f}" for m in QT]])
ORDH = [('Rule passed, any order', 'rule|random'), ('Rule passed, most HTR-equivalent pairs at 2qt first', 'rule|htr pairs at 2qt'),
        ('Rule passed, most true pairs at 2qt first', 'rule|pairs at 2qt'), ('Rule passed, most pairs at HTR first', 'rule|pairs at HTR')]
t_horder = table(OH,
                 [[lab] + [pct(orow(m, key)['R'][k]) for m in QT for k in ('5', '10')] for lab, key in ORDH])
def state_rows(m, key):
    o = st(m, key); rows = []
    for r in o['by_hn']:
        if r['n'] / o['n'] < 0.004: continue
        rows.append([r['k'], num(r['per_dr'], 1), f"{r['mean_d']:.1f}", pct(r['any_reach'] / r['n']), pct(r['any_rule'] / r['n'], 1), pct(r['has'] / r['n'], 2)])
    return table(['HTR-equivalent pairs', 'States per DR', 'Mean moves to HTR', 'Have an HTR in reach', 'Have one that passes the rule', 'Hold a within-goal HTR'], rows)
t_hstate = {(m, key): state_rows(m, key) for m in QT for key in ('2|2', '2|2|min', '3|3', '3|3|min') if st(m, key)}
def fixed_dn(m, key='2|2'):
    """Ranker score of the count for 'this state holds a within-goal HTR in reach', among states at the same distance."""
    o = st(m, key)
    return [(dn, n, a) for dn, n, a, _ in o['auc_has_fixed_dn'] if a is not None and n >= 2000]
def keep(m, key, th, which='keep_hn'):
    for r in st(m, key)[which]:
        if r[0] == th: return dict(states=r[1], reach=r[2], rule=r[3], both=r[4], recall=r[5])
KEEPKEY = '2|2|min'
KM = [m for m in QT if m >= 3]
t_hkeep = table(['Keep the 2qt states with at least'] + [x for m in KM for x in (f'{m}qt: states per DR', f'{m}qt: HTRs in reach per DR', f'{m}qt: solvable DRs still reached')],
                [[f'{th} HTR-equivalent pairs' if th else 'any number'] + [x for m in KM for x in (num(keep(m, KEEPKEY, th)['states'], 1), num(keep(m, KEEPKEY, th)['reach']), pct(keep(m, KEEPKEY, th)['recall']))] for th in (0, 6, 8, 10, 12)])
def dr_sides(m):
    """The DR itself: more HTR-equivalent pairs on one side against where the first within-goal HTR (fewest S+T) is."""
    n = a = c = e = 0
    for gap, nn, s1, s2, s3, nsol, f1, f2, f3 in PR[m]['dr_sides']:
        if gap == 0: continue
        n += nsol; a += f1 if gap > 0 else f3; c += f3 if gap > 0 else f1; e += f2
    return n, a, e, c
def state_auc(m, key, what, col): return st(m, key)[what][col]
if __name__ == '__main__':
    print(t_p2rule); print(t_p2order)
    for m in QT: print(m, 'qt'); print(t_p2post[m]); print(t_routes_p2[m]); print(t_hgoal[m])
    print(t_hexact[2]); print(t_hexact[3]); print(t_hsub[2]); print(t_hsub[3]); print(t_hsides['2|2']); print(t_hsides['3|3']); print(t_hauc); print(t_horder); print(t_hkeep)
    for k, v in t_hstate.items(): print(k); print(v)
    for m in QT: print(m, 'fixed dn', fixed_dn(m), 'dr sides', dr_sides(m), 'short auc', st(m, '2|2')['auc_short'], 'corr', st(m, '2|2')['corr'])
