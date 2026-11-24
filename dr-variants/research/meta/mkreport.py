"""Writes the page, /data/fmc/dr-variants/report/WRITEUP.md, from the computed tables.  Every number is read from the data."""
import json, io
import numpy as np, pandas as pd
from exmd import block

OUT = '/data/fmc/dr-variants/report/WRITEUP.md'
QT = (2, 3, 4)
R = {m: json.load(open(f'../out/meta/res{m}.json')) for m in QT}
B = {m: json.load(open(f'../out/meta/res{m}b.json')) for m in QT}
N = {m: json.load(open(f'../out/meta/niss{m}.json')) for m in QT}
O = json.load(open('../out/meta/orders.json'))
import pairtabs as PT
PR = PT.PR
import re
# within-goal solutions of the second search (drvar metacheck), summed over the three logs
MC = sum(int(re.search(r'both sides: (\d+) within-goal paths', open(f'../out/meta/metacheck{m}.log').read()).group(1)) for m in QT)
# HTRs counted by the version of 17 November 2026 (commit 7097773), before a sequence stopped at its first HTR
OLD_REC = {2: 10013121, 3: 21449915, 4: 34715064}; OLD_TOTAL = sum(OLD_REC.values())
OLD_BEST5 = {2: 0.6122058018609743, 3: 0.6277176501629281, 4: 0.6939672924033955}     # found within 5 finishes, both floors and most pairs first, same version
base = pd.read_csv('../out/meta/base.tsv', sep='\t').set_index('qt')
hp = pd.read_csv('../out/meta/htrpairs.tsv', sep='\t')
cases = pd.read_csv('../out/meta/cases.tsv', sep='\t'); cases.columns = list(cases.columns[:-1]) + ['hs']

def pct(x, d=0): return f'{100 * x:.{d}f}%'
def num(x, d=0): return f'{x:,.{d}f}'
def table(head, rows, align=None):
    align = align or (['---'] + ['---:'] * (len(head) - 1))
    s = '| ' + ' | '.join(head) + ' |\n|' + '|'.join(align) + '|\n'
    for r in rows: s += '| ' + ' | '.join(str(c) for c in r) + ' |\n'
    return s
nd = {m: R[m]['drs'] for m in QT}; ns = {m: R[m]['solvable'] for m in QT}; G = {m: R[m]['goal'] for m in QT}
F = {m: R[m]['funnel'] for m in QT}
def lv(m, name, k): return R[m]['levels'][name][k]
def grid(m, name, a, b): return [x for x in R[m]['grid'][name] if x['a'] == a and x['b'] == b][0]
def od(m, K, name): return O[f'{m}|{K}|{name}']

# ---- tables -------------------------------------------------------------------------------------------------
t_base = table(['DR', 'Share of all DR states', f'Goal', 'Solution within goal − 2', 'Within goal − 1', 'Within goal', 'Mean optimal leave-slice'],
               [[f'{m}qt', pct(base.loc[m, 'share'], 1), G[m], pct(base.loc[m, 'P(ls<=goal-2)'], 1), pct(base.loc[m, 'P(ls<=goal-1)'], 1), pct(base.loc[m, 'P(ls<=goal)'], 1), f"{base.loc[m, 'mean_ls']:.2f}"] for m in QT])
def subset_rows(m):
    return [[a, int(n), pct(s / n)] for a, n, s in R[m]['by_subset'] if n >= 40]
t_subset = table(['Subset', 'DRs in the sample', 'With a solution within goal'], [r for m in QT for r in subset_rows(m)])

t_levels = {m: table(['S+T at most', 'Normal only', 'Normal and inverse', 'Both, shortest-qt skeletons only'],
                     [[k, pct(lv(m, 'normal_all', k)['recall']), pct(lv(m, 'both_all', k)['recall']), pct(lv(m, 'both_min', k)['recall'])] for k in range(0, 6)]) for m in QT}
t_grid = table(['DR', 'Extra moves before 2qt', 'Reached with S+T after 2qt ≤ 2', 'With ≤ 3', 'With ≤ 4', 'Routes to 2qt per DR (at ≤ 3)'],
               [[f'{m}qt', f'at most {a}' if a else 'none', pct(grid(m, 'both_all', a, 2)['recall']), pct(grid(m, 'both_all', a, 3)['recall']), pct(grid(m, 'both_all', a, 4)['recall']),
                 num(grid(m, 'both_all', a, 3)['routes'])] for m in (3, 4) for a in (0, 1, 2)])
mindq = {m: B[m]['min_dq'] for m in QT}
plus2_only = {m: mindq[m].get('2', 0) / ns[m] for m in QT}
unreached = {m: R[m]['unreached'] / ns[m] for m in QT}

stages = [('Every HTR in reach', 'all'), ('Bad slices only, no parity (0 / +3, +2 for R-V and F-V / +5)', 'intermediate'), ('Rule bound (the Advanced rule)', 'rule'),
          ('Pair floor alone', 'pair_simple'), ('Rule bound and pair floor', 'rule+pair_simple'), ('Rule bound and exact pair floor', 'rule+pair'),
          ('216-case table and exact pair floor (computer only)', 'table+pair')]
t_funnel = table(['HTRs left per DR after', '2qt', '3qt', '4qt'], [[nm] + [num(F[m][k]['per_dr']) for m in QT] for nm, k in stages])
t_funnel_p = table(['Share within goal among the HTRs left after', '2qt', '3qt', '4qt'], [[nm] + [pct(F[m][k]['precision'], 1 if F[m][k]['precision'] < 0.1 else 0) for m in QT] for nm, k in stages])
within_total = sum(F[m]['all']['within'] for m in QT)
def by(m, key, val):
    for a, n, s in R[m][key]:
        if a == val: return n, s
    return 0, 0
def rs_row(lo, hi, label):
    out = [label]
    for m in QT:
        n = sum(x[1] for x in R[m]['by_rs'] if lo <= x[0] <= hi); s = sum(x[2] for x in R[m]['by_rs'] if lo <= x[0] <= hi)
        out += [num(n / nd[m], 1), pct(s / n, 1) if n else '–']
    return out
t_rs = table(['Rule bound against the goal', '2qt: HTRs per DR', '2qt: within goal', '3qt: HTRs per DR', '3qt: within goal', '4qt: HTRs per DR', '4qt: within goal'],
             [rs_row(-99, -1, 'over the goal'), rs_row(0, 0, 'equal to the goal'), rs_row(1, 1, '1 under'), rs_row(2, 2, '2 under'), rs_row(3, 99, '3 or more under')])
# rule tightness over all HTR states
H = np.array([[int(v) for v in s.split()] for s in cases['hs']])
tight = [float(np.mean([h[:r + j + 1].sum() / 3072 for h, r in zip(H, cases.rule)])) for j in range(5)]
hpg = hp.groupby('pairs').apply(lambda t: pd.Series(dict(states=t.states.sum(), minfin=t.finish.min(), mean=(t.finish * t.states).sum() / t.states.sum(), maxfin=t.finish.max())))
t_hp = table(['Pairs at HTR', 'HTR states', 'Shortest finish of any of them', 'Mean finish', 'Longest finish'],
             [[int(p), num(r.states), int(r.minfin), f'{r["mean"]:.1f}', int(r.maxfin)] for p, r in hpg.iterrows()])
# card pooled
card = {}
for m in QT:
    for a, p, n, s in R[m]['card_A_pairs']:
        c = card.setdefault((int(a), int(p)), [0, 0]); c[0] += n; c[1] += s
PFX = {0: 4, 2: 5, 4: 3, 6: 3, 8: 2, 10: 3, 12: 1, 16: 0}
def cell(a, p):
    if PFX[p] > a: return '×'
    n, s = card.get((a, p), [0, 0])
    return pct(s / n) if n >= 150 else '·'
t_card = table(['Moves left for the finish'] + [f'{p} pairs' for p in (0, 2, 4, 6, 8, 10, 12, 16)], [[a] + [cell(a, p) for p in (0, 2, 4, 6, 8, 10, 12, 16)] for a in range(0, 7)])
card_n = sum(v[0] for v in card.values())
def auc_row(key): return [pct(R[m][key]['pn2']), pct(R[m][key]['pn1']), pct(R[m][key]['pn0'])]
t_auc = table(['DR', 'Pairs at 2qt', 'Pairs at 1qt', 'Pairs at HTR'], [[f'{m}qt'] + [f"{R[m]['auc'][k]:.2f}" for k in ('pn2', 'pn1', 'pn0')] for m in QT])
def bucket(m, key, lo, hi):
    n = sum(x[1] for x in R[m][key] if lo <= x[0] <= hi); s = sum(x[2] for x in R[m][key] if lo <= x[0] <= hi)
    return pct(s / n, 1) if n else '–'
t_p0 = table(['Pairs at HTR', '2qt', '3qt', '4qt'], [[lab] + [bucket(m, 'rule_by_pn0', lo, hi) for m in QT] for lab, lo, hi in [('0', 0, 0), ('2', 2, 2), ('4', 4, 4), ('6', 6, 6), ('8', 8, 8), ('10', 10, 10), ('12 or 16', 12, 16)]])
t_p2 = table(['Pairs at 2qt', '2qt', '3qt', '4qt'], [[lab] + [bucket(m, 'rule_by_pn2', lo, hi) for m in QT] for lab, lo, hi in [('0–1', 0, 1), ('2–3', 2, 3), ('4–5', 4, 5), ('6–7', 6, 7), ('8 or more', 8, 16)]])
PW = {m: R[m]['pairs_within'] for m in QT}
t_break = table(['Among within-goal HTRs', '2qt', '3qt', '4qt'], [
    ['Pairs at 2qt (mean)'] + [f"{PW[m]['p2']:.1f}" for m in QT],
    ['Of those, still together at HTR (mean)'] + [f"{PW[m]['keep20']:.1f}" for m in QT],
    ['Setup or trigger splits at least one 2qt pair'] + [pct(PW[m]['trig_split']) for m in QT],
    ['Same, among all HTRs that pass the rule'] + [pct(PW[m]['trig_split_rule_live']) for m in QT],
    ['Pairs at HTR (mean)'] + [f"{PW[m]['p0']:.1f}" for m in QT],
    ['Every optimal finish splits a pair that stood at HTR'] + [pct(PW[m]['fin_split'], 1) for m in QT]])
def fs(m, f):
    for a, n, s in PW[m]['fin_split_by_fin']:
        if a == f: return pct(s) if n >= 20 else '·'
    return '·'
t_fsplit = table(['Finish length', '2qt', '3qt', '4qt'], [[f'{f} moves'] + [fs(m, f) for m in QT] for f in (3, 4, 5, 6, 7)])
ORD = [('No floors, shortest HTR first, ties at random', 'no floors: by moves to HTR, random'),
       ('No floors, shortest first, most pairs among equals', 'no floors: by moves to HTR, most pairs'),
       ('**Pair floor, shortest first, most pairs among equals (the baseline)**', 'pair floor only: by moves to HTR, most pairs'),
       ('Pair floor, look at all, then most pairs first', 'pair floor only: most pairs first (look at all first)'),
       ('Rule bound, shortest first, most pairs among equals', 'rule only: by moves to HTR, most pairs'),
       ('Rule bound, look at all, then most pairs first', 'rule only: most pairs first (look at all first)'),
       ('Both floors, in random order', 'both floors: random'),
       ('Both floors, shortest first, most pairs among equals', 'both floors: by moves to HTR, most pairs'),
       ('Both floors, level by level, most pairs first inside a level', 'both floors: level by level, most pairs'),
       ('Both floors, skeleton by skeleton (largest M first)', 'both floors: skeleton by skeleton (largest M first), level, pairs'),
       ('Both floors, 12+ pairs on sight, the rest level by level', 'both floors: 12+ pairs first, then level by level'),
       ('**Both floors, look at all, then most pairs first**', 'both floors: most pairs first (look at all first)')]
def t_orders(m, K=3):
    rows = []
    for lab, key in ORD:
        v = od(m, K, key)
        rows.append([lab, num(v['per_dr'], 0 if v['per_dr'] >= 100 else 1), num(v['per_unsolv'], 0 if v['per_unsolv'] >= 100 else 1)] + [pct(v['R'][k]) for k in ('3', '5', '10', '20', '40')])
    return table(['Order', 'HTRs to finish per DR', 'Same, on a DR with no solution', 'Found within 3 finishes', 'Within 5', 'Within 10', 'Within 20', 'Within 40'], rows)
def skv(m, M, dq=0):
    x = [r for r in R[m]['skeleton_by_M'] if r[0] == dq and r[1] == M]
    return pct(x[0][3] / x[0][2])
def skrow(dq, M):
    out = [M]
    for m in QT:
        x = [r for r in R[m]['skeleton_by_M'] if r[0] == dq and r[1] == M]
        out.append(pct(x[0][3] / x[0][2]) if x and x[0][2] >= 60 else '·')
    return out
t_skm = table(['Maximum penalty M', '2qt', '3qt', '4qt'], [skrow(0, M) for M in range(1, 10)])
t_skp = table(['Maximum penalty M', '2qt', '3qt', '4qt'], [skrow(2, M) for M in range(1, 8)])
def t_level_mi(m):
    rows = []
    for r in B[m]['level_both_all'][:7]:
        plook = r['within'] / max(1, r['looks'] * nd[m]); pgen = r['within'] / max(1, r['generated'] * nd[m])
        rows.append([r['k'], num(r['generated']), num(r['looks'], 1), num(r['finishes'], 1), pct(plook, 1), pct(r['precision']), pct(r['drs'] / ns[m]), num(plook * r['drs'] / nd[m] * 1000, 1)])
    return table(['S+T exactly', 'HTRs per DR', 'Pass the rule', 'Pass both floors', 'Within goal, of those passing the rule', 'Within goal, of those passing both floors', 'Solvable DRs with a within-goal HTR here', 'Mutual info per 1,000 DRs'], rows)
def mi_peak(m):
    rows = B[m]['level_both_all'][:7]
    return max(rows, key=lambda r: r['within'] / max(1, r['looks'] * nd[m]) * r['drs'])['k']
def nrow(m, k):
    r = N[m]['rows'][k]
    return [f'{m}qt', k, pct(r['normal']), pct(r['both']), pct(r['both'] + r['niss1_p0_adds']), num(r['niss1_p0_fin'], 1), pct(r['with_all_niss']), num(sum(r[f'niss{j}_p1_fin'] for j in range(1, m)), 1)]
t_niss = table(['DR', 'S+T at most', 'Normal only', 'Normal and inverse', 'Plus NISS after the first qt (shortest routes)', 'Extra finishes per DR for that', 'Plus NISS after any qt (routes with ≤ 1 extra)', 'Extra finishes per DR for that'],
               [nrow(m, k) for m in QT for k in (1, 2, 3)])
def ab(m, key, f): a, b = R[m]['abandon'][key][f]; return a, b
def abrow(lab, f, key):
    out = [lab]
    for m in QT:
        a, b = ab(m, key, f); out += [pct(a / nd[m], 1), pct(b / a) if a >= 30 else '·']
    return out
ABH = ['Signal', '2qt: share of DRs', '2qt: still has a solution', '3qt: share of DRs', '3qt: still has a solution', '4qt: share of DRs', '4qt: still has a solution']
t_ab = table(ABH, [abrow('No HTR with S+T ≤ 2 passes the rule', 'no_rule_live', 'all|9|2'), abrow('No HTR with S+T ≤ 3 passes the rule', 'no_rule_live', 'all|9|3'),
                   abrow('No HTR with S+T ≤ 3 passes both floors', 'no_both_live', 'all|9|3'), abrow('Everything with S+T ≤ 2 finished, nothing within goal', 'nothing_found', 'all|9|2'),
                   abrow('Everything with S+T ≤ 3 finished, nothing', 'nothing_found', 'all|9|3'), abrow('Everything with S+T ≤ 4 finished, nothing', 'nothing_found', 'all|9|4'),
                   abrow('Same with at most 1 extra move before 2qt, S+T ≤ 3', 'nothing_found', 'all|1|3'), abrow('Same, S+T ≤ 4', 'nothing_found', 'all|1|4')])
def st(m, K, nm='all'): return B[m]['staged'][f'{nm}|{K}']
BASEK = 'pair floor only: by moves to HTR, most pairs'; SAMEK = 'both floors: by moves to HTR, most pairs'
BESTK = 'both floors: most pairs first (look at all first)'; NOFLK = 'no floors: by moves to HTR, most pairs'
PAIRBESTK = 'pair floor only: most pairs first (look at all first)'; RULEK = 'rule only: by moves to HTR, most pairs'; RULEBESTK = 'rule only: most pairs first (look at all first)'
t_staged = table(['DR', 'S+T at most', 'Solvable DRs it can reach', 'Routes to 2qt per DR', 'HTRs that pass the rule, on a DR with a solution', 'Finishes on a DR with no solution',
                  'Found within 5 finishes (most pairs first)', 'Within 10', 'The baseline: found within 5', 'The baseline: within 10'],
                 [[f'{m}qt', K, pct(st(m, K)['recall']), num(st(m, K)['routes']), num(st(m, K)['looks_solv']), num(st(m, K)['finishes_unsolv'], 1), pct(st(m, K)['lookfirst_R']['5']), pct(st(m, K)['lookfirst_R']['10']),
                   pct(od(m, K, BASEK)['R']['5']), pct(od(m, K, BASEK)['R']['10'])] for m in QT for K in (2, 3, 4)])

# ---- examples -----------------------------------------------------------------------------------------------
def nth(n): return {1: 'first', 2: 'second', 3: 'third', 4: 'fourth', 5: 'fifth', 6: 'sixth', 7: 'seventh', 8: 'eighth'}.get(n, f'number {n}')
EX = [
 ('A', "The doc's first walkthrough", "U D L2 D' B2 U R2 F2 B2 D2 L2 D' R2 L2 D2 B2",
  lambda b: f"This is the first random scramble of the doc. None of its 13s is cheap: the F-V one, the 13 the doc finds first, has S+T = 3 and the H-H one 5, so only the F-V one is in reach here. It has 6 pairs with 4 moves left, a long shot on the card of section 7, which is why it's the {nth(b['ff'])} finish and not the first. The baseline gets to it at number {b['fb']} too: on this DR the rule only shortens the list, from {b['nbase']} HTRs to {b['both']}."),
 ('B', "A 4qt DR where the floors leave one obvious HTR", "B2 L2 D' R2 D F2 D F2 D2 B2 R2 D R2 D' U'",
  lambda b: f"The baseline has {b['nbase']} HTRs past the pair floor and reaches the 14 at number {b['fb']}. With the rule there are {b['rl']} to look at and {b['both']} to finish, and the one with 8 pairs and 2 moves left is the solution."),
 ('C', "Only the inverse has it cheaply", "D B2 R2 D L2 D R2 D' B2 D' L2 R2 D2",
  lambda b: "On normal the only 13 needs 3 extra moves before 2qt. On the inverse it's a 1-extra variant of a skeleton with two more quarter turns."),
 ('D', "A mid-skeleton NISS", "D2 R2 U' L2 B2 L2 R2 D2 F2 D' B2 U' B2",
  lambda b: "Both sides need S+T = 3 here. After `B2 U B2 U` on normal, a shortest route to 1qt, the inverse reaches HTR in 3 moves with nothing extra. The 6-move finish there is the long insertion, and on normal it sits in the middle of the solution."),
 ('E', "Only a skeleton with two more quarter turns", "R2 D2 U L2 B2 D' L2 U' F2 D L2 U2",
  lambda b: "Every within-goal solution of this 4b2 has four quarter turns. Both 11s sit one or two extra moves into an 8-move 4qt skeleton, with 12 pairs at HTR."),
 ('F', "Nothing passes the rule: abandon", "D2 F2 L2 D F2 L2 D2 R2 D' B2 D2 L2 B2",
  lambda b: f"A 4a2 4e whose optimal leave-slice is 13. Not one HTR with S+T ≤ 3 on either side passes the rule bound for 12, so there's nothing to look at. The baseline would still finish the {b['nbase']} that pass the pair floor."),
 ('G', "Nothing passes the rule with S+T ≤ 3, and a 12 exists", "D' B2 D2 F2 L2 B2 U' B2 D2 L2 F2 U2",
  lambda b: "The counterexample to abandoning on that signal: the 12s are there, but the cheapest needs S+T = 4 on the inverse. The DR has 12 HTR-equivalent pairs on both sides, the most a 4b2 4e has, and that's a read on how far HTR is, not on whether the HTRs finish (section 9)."),
 ('H', "Within goal after splitting every pair it had at 2qt", "L2 B2 D U2 L2 U' R2 F2 L2 B2 U' F2",
  lambda b: "The first 13 above has 4 pairs at 2qt, keeps none of them through the trigger and lands on an HTR with 0 pairs and 5 moves left. Rare, but it happens. The 11s of this DR are the ordinary kind: `F2 D L2 F2 R2 B2 D R2 D | B2 L2` has 8 pairs at HTR and a 2-move finish."),
 ('I', "A finish that splits a pair", "R2 U B2 D2 B2 R2 U' R2 D2 L2 U' F2 U",
  lambda b: "The one to look at is `B2 U' L2 F2 U L2 U' B2 U' | F2 L2 U2 R2 B2` (14): 10 pairs at HTR and a 5-move finish, and every optimal finish splits some of them (6 of the 10 survive at best). This only shows up with 5 or more moves left."),
 ('J', "Deep on both sides", "U F2 D2 L2 U2 R2 D' L2 D' L2 B2 R2 U'",
  lambda b: "The 12s need S+T = 6 on normal and on inverse. Nothing within reach finds them; this is the kind of DR the abandon numbers are about."),
]
ex_md = ''
EXB = {}
for tag, title, scr, remark in EX:
    b = block(scr); EXB[tag] = b
    s = f"**{tag}. {title}**, `{scr}` ({b['info'].replace('  ', ', ')}).\n\n"
    s += f"- **In reach** (S+T ≤ 3, at most 1 extra move before 2qt, both sides): {num(b['gen'])} HTRs. {b['nbase']} pass the pair floor, {b['rl']} pass the rule, {b['both']} pass both, {b['within']} {'is' if b['within'] == 1 else 'are'} within goal.\n"
    if b['within']:
        s += f"- **First within-goal HTR:** number {b['fb']} in the baseline order, number {b['fs']} with both floors in the same order, number {b['ff']} with both floors and most pairs first.\n"
    else:
        s += f"- **Nothing within goal in reach.** At any depth: {num(b['all'])} HTRs, {b['all_rule']} pass the rule, {b['all_both']} pass both floors, {b['all_within']} are within goal.\n"
    w = b['w']
    if len(w):
        s += "- **Within-goal solutions, cheapest first:**\n"
        for _, x in w.head(3).iterrows(): s += f"  - {b['sol'](x)}.\n"
    if tag == 'D':
        for f in b['niss'][1:2]: s += f"- **NISS:** `{f[1]}` then `{f[2]}`, the parts in brackets on the inverse, {f[8].split()[-1]} moves.\n"
    s += f"- {remark(b)}\n\n"
    ex_md += s
    print('example', tag, 'ok')
# what the remarks say in words, against the data
assert EXB['A']['ff'] == EXB['A']['fb'] and EXB['A']['w'].iloc[0].pairs_htr == 6 and EXB['A']['w'].iloc[0].extra == 3
assert EXB['B']['ff'] == 1 and EXB['B']['w'].iloc[0].pairs_htr == 8 and EXB['B']['r']['goal'] - EXB['B']['w'].iloc[0].len == 2
assert EXB['F']['rl'] == 0 and EXB['F']['r']['ls'] == 13 and EXB['G']['rl'] == 0 and EXB['G']['w'].iloc[0].extra == 4 and EXB['G']['w'].iloc[0].side == 'I'
assert set(EXB['G']['w'].htrpairs_2qt) == {12} and set(EXB['G']['w'].htrpairs_2qt_inv) == {12}
assert (EXB['E']['w'].q == 4).all() and (EXB['J']['w'].extra == 6).all() and EXB['J']['within'] == 0
h0 = EXB['H']['w'].iloc[0]; assert h0.pairs_2qt == 4 and h0.kept_trigger == 0 and h0.pairs_htr == 0 and EXB['H']['r']['goal'] - h0.len == 5

# ---- text ---------------------------------------------------------------------------------------------------
def Rk(m, K, key, k): return pct(od(m, K, key)['R'][str(k)])
def tri(f, sep=' / '): return sep.join(f(m) for m in QT)
def span(f, d=0):
    v = [f(m) for m in QT]
    a, b = pct(min(v), d), pct(max(v), d)
    return a if a == b else f'{a[:-1]}–{b}'
def abp(m, key, f): a, b = ab(m, key, f); return pct(b / a)
# the rule against the best state of each case (leave-slice finishes in DR moves)
case_min = np.array([np.nonzero(h)[0][0] for h in H]); case_gap = case_min - cases.rule.values
assert (case_gap >= 0).all() and len(case_gap) == 216
gap0, gap1, gap2 = int((case_gap == 0).sum()), int((case_gap == 1).sum()), int((case_gap >= 2).sum())

DISCORD = 'https://discord.com/channels/1007840975726575667'
ADV = 'https://docs.google.com/document/d/13F8HonrKJyHjU9EwfiHDRyY4X77vPriYeaVSrh5guq0'
ADV_MSG = f'{DISCORD}/1007841335434285126/1543125354120609832'
SHEET = 'https://docs.google.com/spreadsheets/d/1jRvikzLlm3yHlDQmQ0DLyj3Aw6uinL3Oa-U9_U7R5mY'
SHEET_MSG = f'{DISCORD}/1007841335434285126/1550498925528485992'
LEVI_DOC = 'https://docs.google.com/document/d/1q7rig4GEo26GunBMtuagZdGyzyjCGlduH84CHLpGLSA'
LEVI_DOC_MSG = f'{DISCORD}/1007841273111117924/1311464464737898589'
DRMS = 'https://docs.google.com/document/d/1AUQVrecEFZyR6okXAyJgtQZA-A0AJmAUevhJZlQMjAs'
DRMS_MSG = f'{DISCORD}/1007841335434285126/1383615680179601449'
PAIRS = 'https://docs.google.com/spreadsheets/d/1jY9dLAO6CbxF9Eu7BR-kD34KNnIvAVC8uh49aVDBTn8'
PAIRS_MSG = f'{DISCORD}/1007841335434285126/1148330628358623242'
PAIRS_Q = f'{DISCORD}/1007841335434285126/1148362613500162228'
PSEUDO_MSG = f'{DISCORD}/1007841335434285126/1542387618862465055'

# ---- the two headline tables: what a search finds first, then the filters
t_found = table(['What a search finds', '2qt, goal 12', '3qt, goal 13', '4qt, goal 14'], [
    ['**Solvable DRs it can reach** with S+T ≤ 2'] + [pct(st(m, 2)['recall']) for m in QT],
    ['Solvable DRs it can reach with S+T ≤ 3'] + [pct(st(m, 3)['recall']) for m in QT],
    ['Solvable DRs it can reach with S+T ≤ 4'] + [pct(st(m, 4)['recall']) for m in QT],
    ['**Found within 5 finishes** at S+T ≤ 3: the baseline'] + [Rk(m, 3, BASEK, 5) for m in QT],
    ['Found within 5 finishes: both floors, same order'] + [Rk(m, 3, SAMEK, 5) for m in QT],
    ['Found within 5 finishes: both floors, most pairs first'] + [Rk(m, 3, BESTK, 5) for m in QT],
    ['**Found within 10 finishes**: the baseline'] + [Rk(m, 3, BASEK, 10) for m in QT],
    ['Found within 10 finishes: both floors, same order'] + [Rk(m, 3, SAMEK, 10) for m in QT],
    ['Found within 10 finishes: both floors, most pairs first'] + [Rk(m, 3, BESTK, 10) for m in QT],
    ['Found within 20 finishes: the baseline'] + [Rk(m, 3, BASEK, 20) for m in QT],
    ['Found within 40 finishes: the baseline'] + [Rk(m, 3, BASEK, 40) for m in QT],
    ['HTRs to finish on a DR with no solution: the baseline'] + [num(od(m, 3, BASEK)['per_unsolv'], 1) for m in QT],
    ['HTRs to finish on a DR with no solution: both floors'] + [num(od(m, 3, BESTK)['per_unsolv'], 1) for m in QT]])
t_head = table(['The filters', '2qt, goal 12', '3qt, goal 13', '4qt, goal 14'], [
    ['DRs that have a solution within goal'] + [pct(base.loc[m, 'P(ls<=goal)']) for m in QT],
    ['HTRs in reach of the goal, per DR'] + [num(F[m]['all']['per_dr']) for m in QT],
    ['Of those, HTRs that pass the rule bound'] + [num(F[m]['rule']['per_dr']) for m in QT],
    ['HTRs that pass the pair floor'] + [num(F[m]['pair_simple']['per_dr']) for m in QT],
    ['HTRs that pass the rule bound and the pair floor'] + [num(F[m]['rule+pair_simple']['per_dr']) for m in QT],
    ['Share of those that are within goal'] + [pct(F[m]['rule+pair_simple']['precision']) for m in QT],
    ['Within-goal HTRs that fail the rule bound'] + ['0' for m in QT]])
assert sum(R[m]['funnel']['all']['within'] - R[m]['funnel']['rule']['within'] for m in QT) == 0     # the '0' row above
for m in QT: assert abs(od(m, 3, BESTK)['recall'] - st(m, 3)['recall']) < 1e-9
ratio_int = [F[m]['intermediate']['per_dr'] / F[m]['rule']['per_dr'] for m in QT]
rule_cut = lambda m: 1 - F[m]['rule']['per_dr'] / F[m]['all']['per_dr']
niss1 = lambda m: N[m]['rows'][2]['niss1_p0_adds']
routes_e = lambda m, a: grid(m, 'both_all', a, 3)['routes']
def rs_share(m):     # of the HTRs that pass the rule: the share at the goal or 1 under
    tot = sum(x[1] for x in R[m]['by_rs'] if x[0] >= 0)
    return sum(x[1] for x in R[m]['by_rs'] if 0 <= x[0] <= 1) / tot
def lvl(m, k): return B[m]['level_both_all'][k]
keep_rule = lambda m, k: lvl(m, k)['looks'] / lvl(m, k)['generated']
prec_rule = lambda m, k: lvl(m, k)['within'] / (lvl(m, k)['looks'] * nd[m])
def pooled(f, ks): return [f(m, k) for m in QT for k in ks]
kr0 = pooled(keep_rule, [0]); kr3 = pooled(keep_rule, [3, 4, 5, 6]); pr0 = pooled(prec_rule, [0]); pr2 = pooled(prec_rule, [2, 3, 4, 5, 6])
no_rule = lambda m: ab(m, 'all|9|3', 'no_rule_live')
stop3 = lambda m: ab(m, 'all|9|3', 'nothing_found')
P2 = PT
assert PT.exact_min(2, 12) == 3 and PT.exact_min(2, 10) == 4 and all(PT.exact_min(2, k) >= 5 for k in (0, 4, 6, 8)) and PT.exact_min(3, 10) == 5 and PT.exact_min(3, 12) == 5
assert PT.exact_min(2, 8) == 5 and PT.exact_min(2, 6) == 6 and PT.exact_min(2, 4) == 5      # the floor says 4, 5 and 5
assert int(PT.HT[PT.HT.subset == '4b2 4e'].htr_pairs.max()) == 12 and (PT.HT[(PT.HT.subset == '0c3 0e')].htr_pairs == 16).all()
def hratio(m):
    k12 = PT.keep(m, KK, 12); k10 = PT.keep(m, KK, 10); k0 = PT.keep(m, KK, 0)
    return (k12['reach'] / k12['states']) / ((k0['reach'] - k10['reach']) / (k0['states'] - k10['states']))
def tri2(f, sep=' / '): return sep.join(f(m) for m in (3, 4))
assert all(PT.exact_min(3, k) >= 6 for k in (0, 2, 4, 6, 8, 14, 16)) and PT.exact_mean(2, '4b2 4e', 12) > PT.exact_mean(2, '4b2 2e', 8)
hs2 = lambda m: PT.st(m, '2|2')
KK = '2|2|min' 
pooled_short = lambda c: np.mean([hs2(m)['auc_short'][c] for m in QT])
sr4 = PT.sides_right('2|2', 4); sr2 = PT.sides_right('2|2', 2); sr3 = PT.sides_right('3|3', 4)
drs = {m: PT.dr_sides(m) for m in (2, 3)}

T = f"""# Pruning the search for a DR solution

You have a DR and a goal: a leave-slice solution in 12 from a 2qt DR, 13 from a 3qt, 14 from a 4qt. You go through corner skeletons and their variants, and nearly every HTR you could finish is a waste of time. This page measures which ones are: what the rule bound of Advanced DR Bounding removes, what a pair count at HTR removes on top of it, what pairs and HTR-equivalent pairs tell you before HTR, in which order to finish what's left, what NISS adds, and when to give up on the DR.

Every HTR in reach of the goal was finished exactly, on normal and on inverse, for about 2,000 uniformly random DRs of each kind ({num((R[2]['records'] + R[3]['records'] + R[4]['records']) / 1e6)} million HTRs). The two pair floors are proved in Lean.

November 2026. A date in brackets is a link to that message on the FMC solvers Discord (#fmc-theory or #fmc-discussion).

**This builds on:**

- **Levi Gibson's [DR Bounding]({LEVI_DOC})** ([27 Nov 2024]({LEVI_DOC_MSG})) and **Rodney Kinney's [Advanced DR Bounding [Beta]]({ADV})** ([29 Aug 2026]({ADV_MSG})): corner skeletons and variants, the penalty L + S + T (+N), the NISS@1qt cases, bad slices and parity, and the rules that bound N from below. On the server Levi posts as beef beans; this page says Levi.
- **The doc's *HTR Search Meta***, which is the search this page prunes: "Start by writing down all of the distinct ways to reach 2qt, and explore each one in turn. DR Bounding will prune the search heavily." The goals are the ones of its random-scramble examples: "a leave-E-slice solution in 12 moves for 2qt, 13 for 3qt, and 14 for 4qt".
- **Rodney Kinney's sheet [Adv DR Bounding]({SHEET})** ([18 Sep 2026]({SHEET_MSG})), tab *Optimals (Advanced)*: the 216 NISS@1qt cases with the rule's value for each (column *Heuristic*). From the doc: "Lorenzo Mauro has computed optimal algorithms for all 216 of the corner/edge combined cases."
- **Rodney Kinney on pseudo-pairs** ([27 Aug 2026]({PSEUDO_MSG})): "Pseudo-pairs are HTR-equivalent corner-edge pairs that are not true pairs." He uses the ones that go with a corner case to bound the finish. Here true pairs and pseudo-pairs are counted together, as HTR-equivalent pairs, to read how far HTR is.
- **Rodney Kinney's [DRM Subsets]({DRMS})** ([14 Jun 2025]({DRMS_MSG})): precision, recall, and the score used here to weigh them, "mutual info ≡ p(objective | subset) \\* N(subset, objective)".
- **Levi Gibson's sheet [Pairs in DR]({PAIRS})** ([4 Sep 2023]({PAIRS_MSG})) on how much pairs matter in each DR subset, and what Levi said about it ([4 Sep 2023]({PAIRS_Q})): "There are wild departures. HTR for example! In HTR, pairs matter so little compared to other DR states".
- **[*Judging a DR by hand*](../judging-a-dr/)** on this site: the exact optimal leave-slice finish of every DR state, the sorting of the HTR states into the 216 cases, and the Lean cube model the floors are proved on.

**What it adds:**

- **What the rule bound is worth as a filter**: how many HTRs it removes, and that it never removes a within-goal one (section 5).
- **A second floor, read at HTR by counting pairs.** With n moves left for the finish you need 16 − 4n pairs. It's proved in Lean, and together with the rule it leaves a few dozen HTRs per DR (sections 6 and 7).
- **What pairs tell you at 2qt, at 1qt and at HTR**, with and without the rule, and how often a within-goal solution has to split them (section 8).
- **What HTR-equivalent pairs tell you with 2 and 3 quarter turns left**, on normal and on inverse: a floor on the moves to HTR (proved in Lean), the exact table for every subset, which side has the shorter HTR, and what's left of the read once S+T is known (section 9).
- **Which order to finish HTRs in**, against a baseline that counts pairs too, which skeleton to start with, what NISS adds and when to abandon, in precision, recall and mutual info (sections 10 to 13).
- **How often a within-goal solution exists and where it sits**: how many extra moves, which side, how many quarter turns (sections 3 and 4).

**Terms.**

- **Leave-slice solution.** DR moves that solve the corners and the eight U/D edges and leave the E slice as it falls. Lengths are HTM. Finishes that leave the DR group (the M-slice algs of the sheet, 3e insertions) aren't counted.
- **HTR, variant.** Here an HTR is a sequence of DR moves that ends with a quarter turn and lands in HTR, on the normal scramble or on the inverse. Checking it means finishing from there: the solution has (moves to HTR) + (finish) moves.
  - U and D are the same quarter turn for a leave-slice solution (the doc: "we can freely choose between U and D moves in our variants"), and the direction of the last quarter turn is settled while finishing. HTRs that differ only in those choices are counted once.
  - A sequence stops at the first HTR it reaches. Going on from there with more quarter turns is that HTR's finish, not another HTR.
- **Skeleton, L, M.** The skeleton of an HTR is (side, number of quarter turns, NISS@1qt corner case). L is the length of the shortest corner path of that kind. The corner case then needs 0 more moves for H-H, 1 for R-D and F-D, 2 for R-V and F-V, 3 for D-D. **M**, the doc's maximum penalty, is the goal minus both.
- **S+T, extra moves.** Moves to HTR minus L. The part spent before 2qt is given separately where it matters.
- **Level.** All the HTRs with the same S+T, on both sides and in every skeleton: level 0 is the skeletons as they are, level 1 the HTRs one move longer than their own skeleton, and so on. *Level by level* means finishing all of level 0, then level 1, and so on, with the most pairs at HTR first inside a level. *One level deeper* means raising the cap on S+T by one.
- **2qt, 3qt (on a route).** The state with 2 or 3 quarter turns left before HTR. For a 2qt DR's shortest skeletons the 2qt state is the DR itself.
- **Rule bound.** Moves to HTR + the corner case's own moves + the rule's N for the case the HTR lands on. An HTR **passes the rule** if that is at most the goal.
- **Pairs.** True corner-edge pairs in the U and D layers: a corner and an edge of the same layer joined as on a solved cube. 16 when the layers are solved. The count is the same on the inverse of any state (a pair there is a pair here, somewhere else), so there is nothing extra to read on the inverse.
- **HTR-equivalent pairs.** A corner and an edge next to each other in the U or D layer whose two stickers on the shared side face are the same colour or opposite colours. A true pair is one, and so is a pseudo-pair. 16 in HTR. Unlike true pairs, the count is not the same on the inverse.
- **Pair floor.** With n moves left for the finish (goal minus moves to HTR), the HTR needs at least 16 − 4n pairs.
- **Within goal.** The HTR's optimal leave-slice finish fits the goal. A **solvable** DR is one with a leave-slice solution within the goal.
- **Reach, found within N finishes.** The reach of a search is the share of solvable DRs that have a within-goal HTR among the HTRs it generates. *Found within N finishes* is the share of solvable DRs for which one of the first N HTRs it finishes is within goal. The **fixed reach** used for comparing orders is every HTR with S+T ≤ 3 and at most 1 extra move before 2qt, on both sides.
- **The baseline.** The pair floor, shortest HTR first, most pairs first among HTRs of the same length. It counts pairs, so it gets the same floor on pairs at HTR as the meta it's compared with.
- **Precision, recall, mutual info.** For a set of HTRs: the share that are within goal; the share of solvable DRs with a within-goal HTR in the set; and precision times the number of such DRs, as in *DRM Subsets*.
- **Ranker score.** For a count read on each HTR: the chance that a within-goal HTR has a higher count than one that isn't. 0.5 is useless, 1 is perfect.
- **Population.** Uniformly random DR states with 2, 3 or 4 quarter turns (4a2 and 4b2; 0c3, 2c3, 4a3, 4b3; 0c4, 2c4, 4a4, 4b4). The tables write 4c3 for 4a3 and 4b3 together, which swap on the inverse, and 4c4 likewise. Not states as they come up in attempts.

**How to read this.** Section 1 is the whole answer. Section 14 puts it in the order you'd use it, and section 15 walks ten scrambles through it. Sections 3 to 13 are the tables behind each line of section 1, always for 2qt, 3qt and 4qt DRs side by side, each with its own goal.

What each read takes at the table:

| Read | What it takes |
|---|---|
| L, M, S+T | finding the skeleton and the HTR (a search), then arithmetic |
| Rule bound | tracing the NISS@1qt case by colour at 1qt, per the doc |
| Pair floor | counting pairs at HTR, at a glance |
| HTR-equivalent pairs | counting 16 slots by colour at 2qt or 3qt, at a glance on the side you're on; the other side's count is read on the inverse scramble |
| Finishing an HTR | a search |
| 216-case table | **computer only** |

Counts per DR are exact for the DRs in the sample. A share of DRs carries about ±3 points.

| Section | What is in it |
|---|---|
| [1. The short version](#1-the-short-version) | The answer, with the headline numbers. |
| [2. What was asked](#2-what-was-asked) | The eight questions. |
| [3. How often a within-goal solution exists](#3-how-often-a-within-goal-solution-exists) | Base rates by quarter turns and by subset. |
| [4. Where the within-goal solutions are](#4-where-the-within-goal-solutions-are) | By extra moves, by side, before or after 2qt. |
| [5. The rule bound as a filter](#5-the-rule-bound-as-a-filter) | What it removes, what it never removes, how much slack it leaves. |
| [6. The pair floor](#6-the-pair-floor) | The floor, its proof, and why it only bites under a goal. |
| [7. Both floors together](#7-both-floors-together) | The card: chance of a within-goal finish by pairs at HTR and moves left. |
| [8. Pairs along the route](#8-pairs-along-the-route) | Pairs at 2qt, at 1qt and at HTR, with and without the rule, and how often they get split. |
| [9. HTR-equivalent pairs](#9-htr-equivalent-pairs) | The count on normal and on inverse at 2qt and 3qt: a floor, the exact table, which side, and what it adds to S+T. |
| [10. Which order to finish in](#10-which-order-to-finish-in) | Twelve orders, the baseline among them. |
| [11. Skeletons: which first, how far](#11-skeletons-which-first-how-far) | By maximum penalty M, and the mutual info level by level. |
| [12. NISS](#12-niss) | The inverse, and NISS in the middle of a skeleton. |
| [13. When to abandon](#13-when-to-abandon) | Each stop signal: how often it comes up, how often it's wrong. |
| [14. The meta](#14-the-meta) | The steps, and what they cost and find. |
| [15. Examples](#15-examples) | Ten scrambles. |
| [16. The claims, checked](#16-the-claims-checked) | What the doc, Levi and the questions themselves say, against the numbers. |
| [17. What this does not cover](#17-what-this-does-not-cover) | Limits. |
| [Appendix: how it was computed, and what is proved in Lean](#appendix-how-it-was-computed-and-what-is-proved-in-lean) | The sample, the checks, the Lean theorems by name, what changed. |

## 1. The short version

What a search finds. A row is one measure, a column one kind of DR with its goal. The searches go on both sides with at most 1 extra move before 2qt, and every share is among the DRs that have a solution.

{t_found}
The filters behind it:

{t_head}
- **The rule bound removes {span(rule_cut)} of the HTRs and never a within-goal one.** None of the {num(within_total)} within-goal HTRs in the sample fails it, and it is a floor on all 663,552 HTR states. The parity half of the rule matters: counting bad slices alone keeps {min(ratio_int):.1f} to {max(ratio_int):.1f} times as many.

- **A pair floor at HTR does the same job again.** A side half turn makes at most 4 pairs. So with n moves left for the finish you need at least 16 − 4n pairs at HTR: 16 with none left, 12 with one, 8 with two, 4 with three. That's proved in Lean. On its own it leaves as few HTRs as the rule or fewer, and the two overlap little, which is how thousands of HTRs become a few dozen.

- **The baseline has the pair floor too, and the rule still changes the search.** At S+T ≤ 3 the baseline has {tri(lambda m: num(od(m, 3, BASEK)['per_dr']))} HTRs to finish per DR and finds a solution within 5 finishes for {tri(lambda m: Rk(m, 3, BASEK, 5))} of the solvable DRs (2qt / 3qt / 4qt). Both floors leave {tri(lambda m: num(od(m, 3, BESTK)['per_dr'], 1))} and find {tri(lambda m: Rk(m, 3, SAMEK, 5))} in the same order, {tri(lambda m: Rk(m, 3, BESTK, 5))} with most pairs first. On a DR with no solution the baseline finishes {tri(lambda m: num(od(m, 3, BASEK)['per_unsolv']))} HTRs before it can stop, both floors {tri(lambda m: num(od(m, 3, BESTK)['per_unsolv'], 1))}.

- **Most pairs first is the order to use past the rule.** With both floors it finds {tri(lambda m: Rk(m, 3, BESTK, 5))} within 5 finishes against {tri(lambda m: Rk(m, 3, SAMEK, 5))} shortest first. With the pair floor alone the same switch gives {tri(lambda m: Rk(m, 3, PAIRBESTK, 5))} against {tri(lambda m: Rk(m, 3, BASEK, 5))}: it helps at 4qt and hurts at 2qt.

- **New: pairs at 2qt are worth acting on once the rule is passed.** Among HTRs of the fixed reach that pass the rule, one whose route had 6–7 pairs at 2qt is within goal {tri(lambda m: PT.sh(*PT.binrow(m, 'rule_reach', '6–7')))} of the time, against {tri(lambda m: PT.sh(*PT.binrow(m, 'rule_reach', '0–1')))} with 0–1. Without the rule it's {tri(lambda m: PT.sh(*PT.binrow(m, 'reach', '6–7')))} against {tri(lambda m: PT.sh(*PT.binrow(m, 'reach', '0–1')))}. Finishing most pairs at 2qt first then finds {tri(lambda m: PT.pct(PT.orow(m, 'rule|pairs at 2qt')['R']['5']))} within 5 finishes, against {tri(lambda m: PT.pct(PT.orow(m, 'rule|random')['R']['5']))} in any order and {tri(lambda m: PT.pct(PT.orow(m, 'none|pairs at 2qt')['R']['5']))} with the same order and no rule. The count itself is no sharper a read than before (ranker score {tri(lambda m: f"{PR[m]['auc']['reach']['pn2']:.2f}")} without the rule, {tri(lambda m: f"{PR[m]['auc']['rule_reach']['pn2']:.2f}")} with): the rule has cleared out most of what it couldn't tell apart. Pairs at HTR still do better, {tri(lambda m: PT.pct(PT.orow(m, 'rule|pairs at HTR')['R']['5']))}.

- **New: HTR-equivalent pairs are a good read on how far HTR is, on the side you count them.** With t quarter turns left and k of them, HTR is at least t + (16 − k) / 4 moves away (proved in Lean). Exactly, over all 2qt states: with 12, an HTR within 4 moves exists {pct(PT.exact_cell(2, None, 12, 4))} of the time; with 10, {pct(PT.exact_cell(2, None, 10, 4))}; with 8 or fewer, never. At 2qt the counts on normal and on inverse are unrelated, and each one speaks for its own side: when one side has 4 or more extra, that side has the shorter HTR {pct(sr4[0])} of the time and the longer one {pct(sr4[1])}.

- **New: and they are redundant with S+T.** Once an HTR is in reach and passes the rule, the count its route had at 2qt says nothing about whether it's within goal: the ranker score is {tri(lambda m: f"{PR[m]['auc']['rule_reach']['hn2']:.2f}")}, and finishing most HTR-equivalent pairs first finds nothing sooner than any order. The count on the side you're on only depends on the moves from there to HTR. The count on the inverse also feels the finish and scores {tri(lambda m: f"{PR[m]['auc']['rule_reach']['hi2']:.2f}")}, which true pairs do as well or better ({tri(lambda m: f"{PR[m]['auc']['rule_reach']['pn2']:.2f}")}). Use HTR-equivalent pairs before the trigger is found, to pick the side and the 2qt states to look at first.

- **Within-goal solutions rarely split pairs.** The finish splits a pair that stood at HTR in {tri(lambda m: pct(PW[m]['fin_split']))} of them (2qt / 3qt / 4qt), and only with 5 or more moves left. The setup or trigger splits a 2qt pair in {tri(lambda m: pct(PW[m]['trig_split']))}, against {tri(lambda m: pct(PW[m]['trig_split_rule_live']))} for HTRs in general.

- **One extra move before 2qt is worth it, a second mostly isn't.** For 4qt DRs, allowing none caps the reach at {pct(grid(4, 'both_all', 0, 3)['recall'])} (S+T ≤ 3 after 2qt), allowing one gives {pct(grid(4, 'both_all', 1, 3)['recall'])}, two {pct(grid(4, 'both_all', 2, 3)['recall'])}, while the routes to 2qt go from {num(routes_e(4, 0))} to {num(routes_e(4, 1))} to {num(routes_e(4, 2))}.

- **The inverse is worth about one extra move.** Normal and inverse to S+T ≤ k reach about what normal alone reaches at k + 1. A NISS after the first quarter turn of each shortest route adds {tri(lambda m: pct(niss1(m), 1))} more at S+T ≤ 2.

- **Skeletons with two more quarter turns can't be skipped.** They hold the only within-goal solutions of {pct(plus2_only[2])} of solvable 2qt DRs, {pct(plus2_only[3])} of 3qt and {pct(plus2_only[4])} of 4qt.

- **Start with the skeleton with the most room.** Among skeletons with the fewest quarter turns of a 3qt DR, one with maximum penalty M = 3 holds a within-goal HTR {skv(3, 3)} of the time, with M = 5 {skv(3, 5)}, with M = 7 {skv(3, 7)}. Skip M ≤ 1.

- **Abandoning.** If no HTR with S+T ≤ 3 passes the rule on either side, a solution still exists in {abp(2, 'all|9|3', 'no_rule_live')} of 2qt DRs. If you've finished everything that passes both floors through S+T ≤ 3 and found nothing, one still exists {tri(lambda m: abp(m, 'all|9|3', 'nothing_found'))} of the time; through S+T ≤ 4, {tri(lambda m: abp(m, 'all|9|4', 'nothing_found'))}.

- **The hand rule is close to what the 216 cases can give.** Looking every case up in an exact table instead (**computer only**) would leave {tri(lambda m: num(F[m]['table+pair']['per_dr']))} HTRs per DR instead of {tri(lambda m: num(F[m]['rule+pair']['per_dr']))}.

- **What's left is depth.** The floors only help with HTRs you get to, and a within-goal solution is rarely cheap: skeletons as they are (S+T = 0) hold one for {pct(lv(2, 'both_all', 0)['recall'])} to {pct(lv(4, 'both_all', 0)['recall'])} of solvable DRs.

## 2. What was asked

The search is the usual one from a DR. You go through corner skeletons one at a time, add extra moves to a skeleton's variants up to some point, then move to the next skeleton or give up on the DR. You know the moves to HTR at any point, you can work out the Advanced DR Bounding lower bound for what comes after HTR, and you can count corner-edge pairs on both sides of the scramble, with no finer tracing on the inverse. Long insertions have too many possibilities to try speculatively, so NISS is there to find the solutions with a long insertion near the beginning of the skeleton, and sometimes in the middle.

The baseline is to check variants in order of moves to HTR, on both sides, with no speculative mid-skeleton NISS, preferring variants that form pairs.

1. **What are the best heuristics for pruning that search, and how does the DR Bounding lower bound fit into a better meta than the baseline?** *Answer*: two floors and one order. The rule bound and the pair floor decide what to finish (sections 5 to 7), most pairs first decides the order (section 10), and section 14 puts it together.
2. **How good is each heuristic in precision and recall terms?** The weighing is the mutual info of *DRM Subsets*: how likely a variant is to give a leave-slice solution within the goal, against how many DRs have a within-goal solution starting with that variant's prefix. *Answer*: the tables give precision as the share within goal and recall as the share of solvable DRs covered. The mutual info level by level is in section 11.
3. **Where does NISS belong?** *Answer*: the inverse from the start is worth about one extra move. A NISS after the first quarter turn is cheap and adds a few points. Later ones find less than going a level deeper does (section 12).
4. **When should you abandon a DR that has no solution within the goal?** *Answer*: there is one safe signal and it's rare. After that it's a trade, with the numbers in section 13.
5. **Is forming pairs a poor heuristic?** The suspicion: pairs often have to be broken up after HTR or during the trigger, but forming pairs is a good way of telling apart variants with similar lower bounds. *Answer*: pairs seldom have to be broken up in a within-goal solution, and they tell variants apart well at HTR, weakly before the trigger (section 8).
6. **Shouldn't the baseline have the pair floor too?** It counts pairs, so a fair comparison gives it the same floor on pairs at HTR as the meta that uses the rule bound. *Answer*: yes, and it is the baseline of every table here. The floor takes its list from {tri(lambda m: num(od(m, 3, NOFLK)['per_dr']))} HTRs per DR to {tri(lambda m: num(od(m, 3, BASEK)['per_dr']))}, but it hardly changes what it finds early, because it goes shortest first and the floor only bites on long HTRs. The rule on top is what moves found-within-5 (sections 1 and 10).
7. **How useful is the pair count at 2qt once the S+T rule has been passed?** The intuition: much more useful than pairs alone. *Answer*: yes, in what it finds. The chance behind each pair count is {tri(lambda m: f"{PR[m]['sets']['rule_reach']['precision'] / PR[m]['sets']['reach']['precision']:.0f}")} times higher with the rule, and finishing most pairs at 2qt first finds {tri(lambda m: PT.pct(PT.orow(m, 'rule|pairs at 2qt')['R']['5']))} within 5 finishes against {tri(lambda m: PT.pct(PT.orow(m, 'none|pairs at 2qt')['R']['5']))} without it. The count itself separates good HTRs from bad ones no better than before; what changes is the list it has to rank. Pairs at HTR do better still (section 8).
8. **Are HTR-equivalent pairs, counted on normal and on inverse at 2qt and 3qt, a fair signal of a short HTR, or redundant with the S+T threshold?** *Answer*: both. They say how far HTR is on the side you count them, with a floor and an exact table, and which side is shorter. Once you hold an HTR and know its S+T, they add nothing (section 9).

Only 2qt, 3qt and 4qt DRs, with goals of 12, 13 and 14.

## 3. How often a within-goal solution exists

Share of DR states whose optimal leave-slice solution is within the goal (20 million random states, exact lengths).

{t_base}
The same by subset, in the sample. A row is one subset with its number of bad edges.

{t_subset}
A solvable DR has few within-goal HTRs: the median is {tri(lambda m: f"{B[m]['within_per_solvable']['median']:.0f}")} over both sides, against thousands in reach.

## 4. Where the within-goal solutions are

**By extra moves and side.** Share of solvable DRs with a within-goal HTR at that S+T or less.

2qt, goal 12:

{t_levels[2]}
3qt, goal 13:

{t_levels[3]}
4qt, goal 14:

{t_levels[4]}
- **You need extra moves.** Skeletons as they are (S+T = 0) cover {pct(lv(2, 'both_all', 0)['recall'])}–{pct(lv(4, 'both_all', 0)['recall'])}.
- **The inverse is worth about one extra move.** Both sides at S+T ≤ 2 reach {tri(lambda m: pct(lv(m, 'both_all', 2)['recall']))}, normal alone at 3 reaches {tri(lambda m: pct(lv(m, 'normal_all', 3)['recall']))}. Both at 3 reach {tri(lambda m: pct(lv(m, 'both_all', 3)['recall']))}, normal alone at 4 {tri(lambda m: pct(lv(m, 'normal_all', 4)['recall']))}.
- **Shortest-qt skeletons run out.** The last column stalls at {tri(lambda m: pct(lv(m, 'both_min', 5)['recall']))}. For {tri(lambda m: pct(plus2_only[m]))} of solvable DRs every within-goal solution has two more quarter turns than the minimum. A further {tri(lambda m: pct(unreached[m], 1))} need four more and are outside this page.

**Before or after 2qt.** Share of solvable DRs reached on both sides, all skeletons, by where the extra moves may sit. A 2qt DR has no moves before 2qt in its shortest-qt skeletons, so the table is for 3qt and 4qt.

{t_grid}
The first extra move before 2qt buys a lot and the second little, while the routes to 2qt multiply. That's the split of section 2: short insertions early, the longer ones in the setup and the trigger, where the bound tells you which to make.

## 5. The rule bound as a filter

HTRs left per DR on both sides, at any depth, after each filter.

{t_funnel}
The share of them that are within goal:

{t_funnel_p}
- **It never loses a solution.** All {num(within_total)} within-goal HTRs pass the rule, and the rule is a floor on every HTR state (appendix).
- **It's a floor, not an estimate.** Over all HTR states, only {pct(tight[0], 1)} sit exactly at the rule's value, {pct(tight[1])} within 1, {pct(tight[2])} within 2. Case by case, the best state of a case sits exactly at the rule's value in {gap0} of the 216 cases, 1 over in {gap1} and 2 or more over in {gap2}. An H-H HTR with zero bad slices and good parity can still need 12 moves: `R2 U2 D2 F2 U2 L2 U2 B2 L2 F2 U2 B2 U2 B2` is one.
- **Slack under the goal is rare.** How far the rule bound is under the goal:

{t_rs}
Of the HTRs that pass, {span(rs_share)} sit exactly at the goal or 1 under, and that's also where most within-goal HTRs are. An HTR 2 or more under is a better bet, but there are few of them. Ordering by the bound doesn't get you far; you need another read.

- **Bad slices.** Of the HTRs that pass the rule, {tri(lambda m: pct(B[m]['bad_rule'][0][1] / sum(x[1] for x in B[m]['bad_rule'])))} have zero bad slices. At these goals a bad slice almost always means the HTR is out. The one-bad-slice HTRs that do pass are within goal more often ({pct(B[3]['bad_rule'][1][2] / B[3]['bad_rule'][1][1], 1)} against {pct(B[3]['bad_rule'][0][2] / B[3]['bad_rule'][0][1], 1)} at 3qt).

## 6. The pair floor

U and D moves never change the number of pairs in the U and D layers: each layer turns as a whole. A side half turn carries four corner-edge slots as a whole and splits four, so it changes the count by at most 4. A leave-slice finish ends with all 16 pairs. So:

| Moves left for the finish | Pairs needed at HTR |
|---:|---:|
| 0 | 16 |
| 1 | 12 |
| 2 | 8 |
| 3 | 4 |
| 4 or more | any |

- **Proved in Lean.** `pair_floor`: if a sequence of DR moves solves the corners and the U/D edges of a state with p pairs, it has at least (16 − p) / 4 side half turns. It holds for any DR state, not only at HTR, and for full finishes too. The proof is on the cube model the exact table of DR finishes is certified on, and uses no computation outside the kernel. The floor is reached at every step: `R2` (12 pairs), `R2 L2` (8), `R2 L2 F2` (4), `R2 L2 F2 B2` (0).
- **Two refinements at HTR** (exact over all 663,552 HTR states, not in Lean): 10 pairs need 3 moves, not 2 (`R2 U2 R2`), and 2 pairs need 5, not 4 (`R2 U2 R2 F2 B2`). The tables call the floor with these two the exact pair floor. From section 8 on, the pair floor is the exact one: the two refinements are as easy to remember as the floor.
- **Pairs aren't an estimate either.** Over all HTR states the pair count hardly moves the finish, which is what Levi said in 2023:

{t_hp}
`U2 R2 L2 U2 R2 L2 F2 R2 L2 B2` has all 16 pairs and needs 10 moves. The floor only bites because the goal leaves so few moves.

## 7. Both floors together

Neither floor knows what the other knows: the rule reads the NISS@1qt case, the pairs read how close the layers are.

The card: of the HTRs that pass the rule, the share that are within goal, by pairs at HTR and moves left ({num(card_n)} HTRs, 2qt to 4qt pooled). × fails the pair floor, · has under 150 HTRs.

{t_card}
- **At the floor with 0 or 1 move left, it's close to a coin flip:** {cell(0, 16)} for 16 pairs with nothing left, {cell(1, 12)} for 12 with 1.
- **At the floor with 2 or more moves left, it's a long shot:** {cell(2, 8)} for 8 pairs with 2 left, {cell(3, 4)} and {cell(3, 6)} for 4 and 6 pairs with 3 left.
- **A step above the floor is the good bet:** 12 pairs with 2 or 3 left ({cell(2, 12)}, {cell(3, 12)}), 8 pairs with 3 or 4 left ({cell(3, 8)}, {cell(4, 8)}).

## 8. Pairs along the route

How well the pair count ranks the HTRs that pass the rule, at any depth (the ranker score of the terms).

{t_auc}
Share within goal of the HTRs that pass the rule, by pairs at 2qt:

{t_p2}
The same by pairs at HTR:

{t_p0}
**Pairs at 2qt, with and without the rule.** Now inside the fixed reach, where the comparison with a search without the rule makes sense. Share within goal by pairs at 2qt, among all HTRs of the reach and among those that pass the rule. · is under 150 HTRs.

{P2.t_p2rule}
The rule multiplies the chance in every row, {tri(lambda m: f"{PR[m]['sets']['rule_reach']['precision'] / PR[m]['sets']['reach']['precision']:.0f}")} times over all rows (2qt / 3qt / 4qt). It doesn't make the count a better ranker: 6–7 pairs against 0–1 is {tri(lambda m: f"{PT.lift(m, 'reach'):.1f}")} to 1 without the rule and {tri(lambda m: f"{PT.lift(m, 'rule_reach'):.1f}")} to 1 with it. The second ranker row compares HTRs of the same DR only, which is the choice a solver has.

The same HTRs, rule passed, by how many extra moves follow 2qt. 4qt DRs:

{P2.t_p2post[4]}
3qt DRs:

{P2.t_p2post[3]}
As an order of finishing, inside the fixed reach:

{P2.t_p2order}
And on the routes to 2qt of the fixed reach, 4qt DRs. A route holds a within-goal HTR if one of its HTRs in reach is within goal.

{P2.t_routes_p2[4]}
How often pairs get split, among within-goal HTRs:

{t_break}
Share of within-goal HTRs whose every optimal finish splits a pair that stood at HTR, by finish length:

{t_fsplit}
- **Forming pairs on the way to 2qt says little about the HTRs behind it.** Past the rule, an HTR whose route had 6–7 pairs at 2qt is within goal {tri(lambda m: bucket(m, 'rule_by_pn2', 6, 7))} of the time against {tri(lambda m: bucket(m, 'rule_by_pn2', 0, 1))} with 0–1, and few routes have that many.
- **Once the rule is passed the same pair count is a bigger bet, not a sharper one.** Every row of the table is higher with the rule and the ranker score is about the same.
- **As an order it pays once the rule is passed.** Past the rule, most pairs at 2qt first finds {tri(lambda m: PT.pct(PT.orow(m, 'rule|pairs at 2qt')['R']['5']))} within 5 finishes against {tri(lambda m: PT.pct(PT.orow(m, 'rule|random')['R']['5']))} in any order. Without the rule it's {tri(lambda m: PT.pct(PT.orow(m, 'none|pairs at 2qt')['R']['5']))} against {tri(lambda m: PT.pct(PT.orow(m, 'none|random')['R']['5']))}: the list is too long for any order by pairs at 2qt to matter. Most pairs at HTR first still finds more, {tri(lambda m: PT.pct(PT.orow(m, 'rule|pairs at HTR')['R']['5']))}. A 2qt DR's shortest skeletons all start from the same 2qt state, the DR itself, so there the count only tells skeletons with two more quarter turns apart.
- **The count at 2qt fades with the moves that follow.** Its ranker score among HTRs with nothing extra after 2qt is {tri(lambda m: f"{PR[m]['p2_by_post'][0][2]:.2f}")}, and with 3 extra moves {tri(lambda m: f"{PR[m]['p2_by_post'][3][2]:.2f}")}.
- **Routes with many pairs are rare.** Of the routes to 2qt of the fixed reach, {tri(lambda m: pct(sum(r[2] for r in PR[m]['routes_by_p2'][3:]) / sum(r[2] for r in PR[m]['routes_by_p2']), 1))} have 6 or more pairs.
- **The suspicion of section 2, checked.** Pairs seldom need to be broken after HTR: not at all in finishes of up to 3 moves, and those are {pct(sum(x[1] for x in PW[3]['fin_split_by_fin'] if x[0] <= 3) / PW[3]['n'])} of the within-goal HTRs at 3qt. During the setup and trigger a 2qt pair is split in {tri(lambda m: pct(PW[m]['trig_split']))} of within-goal solutions, against {tri(lambda m: pct(PW[m]['trig_split_rule_live']))} of HTRs at large. So a split pair is a mild warning, not a need.
- **Where pairs do separate variants with similar bounds is at HTR.** With the same moves left and the same rule bound, the pair count is what tells the HTRs apart: that's the card of section 7.

## 9. HTR-equivalent pairs

A corner and an edge next to each other in the U or D layer are an HTR-equivalent pair when their two stickers on the shared side face are the same colour or opposite colours. A true pair is one. The others are pseudo-pairs. Count the 16 slots: 16 means every slot looks paired once opposite colours are taken as the same, which is what an HTR looks like.

The same count another way: a slot counts when its corner and its edge are both in their own half-turn orbit (the corner in its tetrad, the edge in its slice) or both out of it.

**The floor.** U and D moves never change the count, a side half turn changes it by at most 4, and an HTR has all 16. So with t quarter turns left on a route and k HTR-equivalent pairs, HTR is at least t + (16 − k) / 4 moves away. With 2 quarter turns left:

| HTR-equivalent pairs at 2qt | Moves to HTR, at least |
|---:|---:|
| 16 | 2 |
| 12 | 3 |
| 8 or 10 | 4 |
| 4 or 6 | 5 |
| 0 | 6 |

- **Proved in Lean** (`htr_pair_floor`, `htr_pair_floor_length`), the same way as the pair floor of section 6.
- **Reached at every step:** `U R2 U` has 12, `U R2 L2 U` 8, `U R2 F2 B2 U` 4 and `U R2 L2 F2 B2 U` 0. Among 4a2 and 4b2 states it is exact at 12, 10 and 4 and one move short at 8 and 6 (next table): `U R2 L2 U` isn't a 4a2 or a 4b2.
- **16 isn't only HTR.** A 0c3 with no bad edges has all 16 and is three quarter turns away.
- **On the inverse it's another number.** The state `U' B2 F2 R2 U'` has 4 and its inverse has 12. Over the 4a2 and 4b2 states with 2 quarter turns left in the sample the two counts differ for {span(lambda m: hs2(m)['differ'])} of them and are unrelated (correlation {max(abs(hs2(m)['corr']['hn_hi']) for m in QT):.2f}). With 3 quarter turns left they go together a little (correlation {min(PT.st(m, '3|3')['corr']['hn_hi'] for m in (3, 4)):+.2f} to {max(PT.st(m, '3|3')['corr']['hn_hi'] for m in (3, 4)):+.2f}).

**The exact table.** The count and the fewest moves to HTR are both the same on every state of a class (an HTR state followed by the same moves), and the 29,400 classes are of equal size. One state per class gives the table over all DR states. States with 2 quarter turns left (4a2 and 4b2, {pct(PT.qt_share(2), 1)} of all DR states):

{PT.t_hexact[2]}
States with 3 quarter turns left ({pct(PT.qt_share(3), 1)} of all DR states):

{PT.t_hexact[3]}
Mean moves to HTR by subset and count, 2qt:

{PT.t_hsub[2]}
3qt:

{PT.t_hsub[3]}
- **12 at 2qt is the read.** An HTR within 4 moves needs 10 or 12, and a 3-move HTR needs 12. Over all 2qt states an HTR within 4 moves is there {pct(PT.exact_cell(2, None, 12, 4))} of the time with 12 and {pct(PT.exact_cell(2, None, 10, 4))} with 10. In a 4b2 2e it's {pct(PT.exact_cell(2, '4b2 2e', 12, 4))} with 12 and {pct(PT.exact_cell(2, '4b2 2e', 10, 4))} with 10.
- **The subset comes first.** A 4b2 4e with 12 is still further from HTR on average ({PT.exact_mean(2, '4b2 4e', 12):.1f} moves) than a 4b2 2e with 8 ({PT.exact_mean(2, '4b2 2e', 8):.1f}). Inside 4b2 2e the mean goes from {PT.exact_mean(2, '4b2 2e', 6):.1f} with 6 to {PT.exact_mean(2, '4b2 2e', 12):.1f} with 12, inside 4b2 4e from {PT.exact_mean(2, '4b2 4e', 4):.1f} with 4 to {PT.exact_mean(2, '4b2 4e', 12):.1f} with 12. In 4a2 the count says little.
- **At 3qt it's the same shape, flatter.** An HTR within 5 moves needs 10 or 12, and it's there {pct(PT.exact_cell(3, None, 12, 5))} of the time with 12 and {pct(PT.exact_cell(3, None, 10, 5))} with 10.

**Which side.** States with 2 quarter turns left in the sample (2qt, 3qt and 4qt DRs pooled, routes with at most 1 extra move so far), by how the count on the state and on its inverse compare:

{PT.t_hsides['2|2']}
With 3 quarter turns left:

{PT.t_hsides['3|3']}
- **Each count speaks for its own side.** As a ranker of the 2qt states with an HTR within 4 moves on normal, the count on normal scores {pooled_short('hn'):.2f}, the count on the inverse {pooled_short('hi_for_normal'):.2f}, true pairs {pooled_short('pn'):.2f}. For an HTR within 4 moves on the inverse it's the count on the inverse that scores {pooled_short('hi'):.2f}.
- **Go to the side with more.** With 4 or more extra on one side, that side has the shorter HTR {pct(sr4[0])} of the time and the longer one {pct(sr4[1])} at 2qt, {pct(sr3[0])} and {pct(sr3[1])} at 3qt. A gap of 2 is a weak hint.
- **For the DR itself** (a 2qt DR is its own 2qt state, a 3qt DR its own 3qt state): when the two counts differ, the first within-goal solution, the one with the least S+T, is on the side with more for {pct(drs[2][1] / drs[2][0])} of the solvable 2qt DRs and on the other side for {pct(drs[2][3] / drs[2][0])}; for 3qt DRs {pct(drs[3][1] / drs[3][0])} and {pct(drs[3][3] / drs[3][0])}. A short HTR isn't yet a solution.

**Against the goal.** HTRs of the fixed reach, by the count their route had at 2qt. 4qt DRs:

{PT.t_hgoal[4]}
Ranker scores of each read at 2qt, among the HTRs of the fixed reach that pass the rule:

{PT.t_hauc}
As an order of finishing:

{PT.t_horder}
- **Redundant with S+T.** An HTR in reach already has a short route. Among those, the count at 2qt doesn't separate the ones that finish: {tri(lambda m: f"{PR[m]['auc']['rule_reach']['hn2']:.2f}")} as a ranker, and finishing most HTR-equivalent pairs first is no better than any order.
- **Why: the count on your side can't see the finish.** What an HTR state does first never changes the count (`hpairs_after_htr`, in Lean). So the count at 2qt is the same whichever HTR state the route lands on. It depends on the moves from 2qt to HTR and on nothing else.
- **The inverse count can see it, like a pair count.** The inverse of the 2qt state is the rest of the solution played backwards from solved, trigger and finish, and each side half turn in it costs at most 4. So the count on the inverse goes down with a long finish: it scores {tri(lambda m: f"{PR[m]['auc']['rule_reach']['hi2']:.2f}")}. True pairs at 2qt read the same thing and score {tri(lambda m: f"{PR[m]['auc']['rule_reach']['pn2']:.2f}")}, and a state never has fewer HTR-equivalent pairs than true pairs, so the pair count is the tighter of the two. Taking the inverse count among HTRs with the same pairs at 2qt gives {tri(lambda m: f"{PR[m]['auc']['rule_reach']['p2hi']:.2f}")}.
- **Its use is before the trigger.** At 2qt you don't know S+T yet. The count says which states can have a short trigger at all, and on which side, and that's where the HTRs in reach come from.

The 4a2 and 4b2 states one quarter turn into the shortest skeletons of a 3qt DR (at most 1 extra move so far, both sides):

{PT.t_hstate[(3, '2|2|min')]}
Two quarter turns into the shortest skeletons of a 4qt DR:

{PT.t_hstate[(4, '2|2|min')]}
Looking only at the 2qt states with enough of them:

{PT.t_hkeep}
- **It's an order, not a filter.** A state with 12 holds {tri2(lambda m: f"{hratio(m):.1f}")} times as many HTRs in reach as a state with 8 or fewer (3qt / 4qt), but every cut loses solutions, which the two floors of sections 5 and 6 never do. Start with the 2qt states that have 12, on the side that has more.
- **Knowing the trigger beats it.** As a ranker of the 2qt states that hold a within-goal HTR in reach, the count scores {tri(lambda m: f"{PT.st(m, KK)['auc_has']['hn']:.2f}" if PT.st(m, KK) and PT.st(m, KK)['auc_has']['hn'] else '·')}, true pairs {tri(lambda m: f"{PT.st(m, KK)['auc_has']['pn']:.2f}" if PT.st(m, KK) and PT.st(m, KK)['auc_has']['pn'] else '·')}, and the fewest moves to HTR from the state, which is what you know once you've found the trigger, {tri(lambda m: f"{1 - PT.st(m, KK)['auc_has']['dn']:.2f}" if PT.st(m, KK) and PT.st(m, KK)['auc_has']['dn'] else '·')}.

## 10. Which order to finish in

Fix what's in reach: S+T ≤ 3, at most 1 extra move before 2qt, both sides, all skeletons. A row is one order. The first two columns say how many HTRs it has to finish, the others the chance of having found a within-goal solution after so many finishes, among DRs that have one.

2qt (the reach is {pct(od(2, 3, BESTK)['recall'])}):

{t_orders(2)}
3qt (the reach is {pct(od(3, 3, BESTK)['recall'])}):

{t_orders(3)}
4qt (the reach is {pct(od(4, 3, BESTK)['recall'])}):

{t_orders(4)}
- **The pair floor alone shortens the baseline's list, not its search.** It takes {tri(lambda m: num(od(m, 3, NOFLK)['per_dr']))} HTRs per DR down to {tri(lambda m: num(od(m, 3, BASEK)['per_dr']))}, and found-within-5 goes from {tri(lambda m: Rk(m, 3, NOFLK, 5))} to {tri(lambda m: Rk(m, 3, BASEK, 5))}: shortest first meets the long HTRs, the ones the floor removes, last.
- **The rule is what the baseline is missing.** Same order, both floors: {tri(lambda m: Rk(m, 3, SAMEK, 5))} within 5 and {tri(lambda m: Rk(m, 3, SAMEK, 10))} within 10, against {tri(lambda m: Rk(m, 3, BASEK, 5))} and {tri(lambda m: Rk(m, 3, BASEK, 10))}. On a DR with no solution you're done after {tri(lambda m: num(od(m, 3, BESTK)['per_unsolv'], 1))} finishes instead of {tri(lambda m: num(od(m, 3, BASEK)['per_unsolv']))}.
- **Most pairs first is the order past the rule.** With both floors it beats shortest first at every kind of DR ({tri(lambda m: Rk(m, 3, BESTK, 5))} against {tri(lambda m: Rk(m, 3, SAMEK, 5))} within 5), and with the rule alone too ({tri(lambda m: Rk(m, 3, RULEBESTK, 5))} against {tri(lambda m: Rk(m, 3, RULEK, 5))}). With the pair floor alone it's {tri(lambda m: Rk(m, 3, PAIRBESTK, 5))} against {tri(lambda m: Rk(m, 3, BASEK, 5))}: better at 4qt, worse at 2qt, where a list the rule hasn't thinned still holds HTRs with many pairs and a bad case.
- **Skeleton by skeleton costs a few points at most** against level by level ({tri(lambda m: Rk(m, 3, 'both floors: skeleton by skeleton (largest M first), level, pairs', 5))} against {tri(lambda m: Rk(m, 3, 'both floors: level by level, most pairs', 5))} within 5), so the order of section 2 works as long as pairs decide inside it.
- **12+ pairs on sight** finds {tri(lambda m: Rk(m, 3, 'both floors: 12+ pairs first, then level by level', 5))} within 5 without looking at everything first.

## 11. Skeletons: which first, how far

Share of skeletons that hold a within-goal HTR, by maximum penalty M. First the skeletons with the fewest quarter turns (· is under 60 skeletons):

{t_skm}
Then the skeletons with two more quarter turns:

{t_skp}
- **More room, more often.** The doc starts its walkthrough with the longer skeleton, "since DR Bounding works best with longer skeletons". A longer skeleton has a smaller M, so fewer of its HTRs pass the rule, but it's also the one that holds a within-goal HTR less often.
- **How far to go in a skeleton.** Level by level, both sides and all skeletons. The mutual info is the share within goal among the HTRs that pass the rule, times the number of DRs with a within-goal HTR at that level, per 1,000 DRs.

4qt:

{t_level_mi(4)}
3qt:

{t_level_mi(3)}
2qt:

{t_level_mi(2)}
The rule keeps 1 HTR in {1 / max(kr0):.0f} to {1 / min(kr0):.0f} at S+T = 0 and 1 in {1 / max(kr3):.0f} to {1 / min(kr3):.0f} from S+T = 3 on. Of those that pass, {pct(min(pr0))[:-1]}–{pct(max(pr0))} are within goal at S+T = 0, {pct(min(pr2))[:-1]}–{pct(max(pr2))} from S+T = 2 on. The mutual info peaks at S+T = {mi_peak(2)} for 2qt, {mi_peak(3)} for 3qt and {mi_peak(4)} for 4qt. Past that the HTRs multiply faster than the DRs they add.

## 12. NISS

Share of solvable DRs reached, and what a mid-skeleton NISS costs in finishes after both floors. The NISS is: do a route's moves through a quarter turn on normal, switch, and search the inverse from there to the same S+T.

{t_niss}
- **The inverse is the big one.** It finds the solutions whose first section is long, because on the inverse that section is the finish.
- **A NISS after the first quarter turn of a shortest route is cheap and adds a few points.** There are only one or two such routes per DR.
- **After later quarter turns, or from routes with 1 extra move, it adds more,** but from many more starting points: about {num(N[4]['prefixes'][1][2])} routes after the second quarter turn of a 4qt DR and {num(N[4]['prefixes'][2][2])} after the third.
- **Against going one level deeper on both sides.** After both sides at S+T ≤ 2, the next level reaches {tri(lambda m: pct(N[m]['rows2'][2]['deeper_gets']))} more of the solvable DRs for {tri(lambda m: num(N[m]['rows2'][2]['deeper_fin'], 1))} finishes per DR. NISS at S+T ≤ 2 (any quarter turn, routes with at most 1 extra) reaches {tri(lambda m: pct(N[m]['rows2'][2]['niss_gets']))} more for {tri(lambda m: num(N[m]['rows2'][2]['niss_fin'], 1))}.

## 13. When to abandon

How often each signal comes up, and how often a within-goal solution exists all the same. *Finished* means every HTR that passes both floors.

{t_ab}
- **Before any search,** the subset is the first signal (section 3): a 0c3 has a 13 less than one time in five, a 4a2 2e has a 12 about as rarely.
- **Nothing passes the rule with S+T ≤ 3: a safe stop,** but it only comes up for {pct(no_rule(2)[0] / nd[2], 1)} of 2qt DRs, {pct(no_rule(3)[0] / nd[3], 1)} of 3qt and {pct(no_rule(4)[0] / nd[4], 1)} of 4qt. Example F is one; example G is one of the {abp(2, 'all|9|3', 'no_rule_live')} where a solution exists anyway.
- **After the finishes** the numbers are what they are: stopping at S+T ≤ 3 gives up a solution on {tri(lambda m: pct(stop3(m)[1] / stop3(m)[0]))} of the DRs you stop on.
- **On a DR with no solution** the whole of S+T ≤ 3 costs {tri(lambda m: num(od(m, 3, BESTK)['per_unsolv'], 1))} finishes.

## 14. The meta

What the numbers above add up to, for one DR and one goal.

1. **Check the subset.** Drop the ones that rarely make the goal.
2. **List the skeletons on both sides,** two more quarter turns included, with M for each. Skip M ≤ 1. Take them in order of M, largest first.
3. **At 2qt, count HTR-equivalent pairs** before looking for triggers. Start with the states that have 12, and with the side that has more.
4. **In a skeleton, go by S+T,** with at most one extra move before 2qt. For each HTR work out the rule bound at 1qt. If it's over the goal, don't execute it.
5. **Execute the ones that pass and count pairs.** With n moves left you need 16 − 4n, and 10 pairs need 3 moves, 2 pairs 5. Below that, move on.
6. **Finish on sight** anything with 12 or more pairs. Keep the rest in a list.
7. **When a level is done, finish the list, most pairs first.**
8. **NISS** after the first quarter turn of each shortest route, same steps on the inverse.
9. **Stop** at S+T = 3 unless the DR is one you'd rather not leave. Section 13 says what you leave behind.

What that costs and finds, with everything looked at before finishing. A row is one kind of DR and one depth, and the last two columns are the baseline at the same depth.

{t_staged}
The routes to 2qt are the part no floor shortens: tens for a 2qt DR, hundreds for a 4qt one at S+T ≤ 3. Step 3 only puts them in order.

## 15. Examples

Each scramble is a sequence of DR moves; apply it to a solved cube to get the DR. A `|` marks HTR. Solutions on the inverse are given as found there and as a normal solution. The pair counts at 2qt are those of the state with 2 quarter turns left on that solution's route.

{ex_md}
## 16. The claims, checked

| Claim | Who | Result |
|---|---|---|
| "Tweaking the baseline by hand to minimize the difference with the computed optimal yields these improved rules, which give a correct lower bound 100% of the time, and are within 1 of the true lower bound 80% of the time." | Rodney Kinney, [*Advanced DR Bounding*]({ADV}) | **The lower bound holds** for leave-slice finishes in DR moves on all 663,552 HTR states. The 80% is against the sheet's penalties, which allow finishes that leave DR, and isn't rechecked here. Against leave-slice finishes in DR moves the rule is exact for {gap0} of the 216 cases and 1 under for {gap1} (section 5). |
| "There are wild departures. HTR for example! In HTR, pairs matter so little compared to other DR states" | Levi Gibson ([4 Sep 2023]({PAIRS_Q})) | **Holds** over all HTR states: the mean finish is {hpg.loc[0, 'mean']:.1f} moves with 0 pairs and {hpg.loc[8, 'mean']:.1f} with 8. Under a goal it's another matter: the pair floor removes most HTRs (section 6). |
| "In the standard meta, one rarely makes a long-ish insertion (such as a non-cancelling corner swap) in the middle of the skeleton, because there are too many possible insertions to consider, and the ones that actually help can't be identified just by looking at pairs formed." | Rodney Kinney, [*Advanced DR Bounding*]({ADV}), *HTR Search Meta* | **In line with section 8**: pairs at 2qt are a weak read on which routes lead to a within-goal HTR ({R[2]['auc']['pn2']:.2f} to {R[4]['auc']['pn2']:.2f} as a ranker, where 0.5 is useless). Long insertions weren't tested on their own. |
| "Worthwhile long insertions at 3qt are still best found via NISS, but in general there is no need to ever NISS mid-skeleton when using DR Bounding." | Rodney Kinney, [*Advanced DR Bounding*]({ADV}), *HTR Search Meta* | **Mostly.** After both sides at S+T ≤ 2, one more level reaches {tri(lambda m: pct(N[m]['rows2'][2]['deeper_gets']))} more of the solvable DRs. NISS in the middle of a route reaches {tri(lambda m: pct(N[m]['rows2'][2]['niss_gets']))} more, and {tri(lambda m: pct(N[m]['rows'][2]['niss1_p0_adds'], 1))} if it's kept to the first quarter turn of each shortest route (section 12). |
| "Let's start with skeleton #2, since DR Bounding works best with longer skeletons" | Rodney Kinney, [*Advanced DR Bounding*]({ADV}), first random scramble | **Depends on what you want from it.** A longer skeleton has a smaller M, so the rule leaves less to finish. The within-goal solutions are more often in the skeleton with the larger M (section 11). |
| Pairs often have to be broken up after HTR | Section 2, question 5 | **Not at these goals**: {tri(lambda m: pct(PW[m]['fin_split']))} of within-goal HTRs. Example I is one. |
| Pairs often have to be broken up during the trigger | Section 2, question 5 | **Sometimes**: in {tri(lambda m: pct(PW[m]['trig_split']))} of within-goal HTRs, about half the rate of HTRs at large. Example H. |
| Forming pairs is a good way of telling apart variants with similar lower bounds | Section 2, question 5 | **Yes at HTR, weakly at 2qt** (section 8). |
| The pair count at 2qt is much more useful once the S+T rule has been passed than pairs alone | Section 2, question 7 | **Holds for what it finds; the count itself is no sharper.** With the rule the chance behind every pair count is {tri(lambda m: f"{PR[m]['sets']['rule_reach']['precision'] / PR[m]['sets']['reach']['precision']:.0f}")} times higher, and most pairs at 2qt first finds {tri(lambda m: PT.pct(PT.orow(m, 'rule|pairs at 2qt')['R']['5']))} within 5 finishes against {tri(lambda m: PT.pct(PT.orow(m, 'none|pairs at 2qt')['R']['5']))} without the rule. The ranker score is {tri(lambda m: f"{PR[m]['auc']['reach']['pn2']:.2f}")} without the rule and {tri(lambda m: f"{PR[m]['auc']['rule_reach']['pn2']:.2f}")} with it (section 8). |
| HTR-equivalent pairs on normal and on inverse at 2qt and 3qt are a fair signal of a short HTR | Section 2, question 8 | **Holds**, for the side they're counted on: {pooled_short('hn'):.2f} as a ranker of the 2qt states with an HTR within 4 moves, against {pooled_short('pn'):.2f} for true pairs. There is a floor, and an exact table (section 9). |
| That signal may be redundant with the S+T threshold | Section 2, question 8 | **Holds** for the count on the side of the HTR: among HTRs in reach that pass the rule it scores {tri(lambda m: f"{PR[m]['auc']['rule_reach']['hn2']:.2f}")}. The count on the inverse keeps a little, {tri(lambda m: f"{PR[m]['auc']['rule_reach']['hi2']:.2f}")}, because it feels the finish (section 9). |

Nothing checked here turned out wrong, so there is no errata page.

## 17. What this does not cover

- **Uniform DRs.** Real attempts reach DRs through EO and a trigger; the mix of subsets and of pairs differs.
- **DR moves only.** A finish that leaves the DR group can be shorter than the best leave-slice finish counted here.
- **Counts, not minutes.** A route to 2qt, a rule read, a look at HTR and a finish don't cost the same, and how fast a solver finds the setups that pass the rule isn't measured.
- **Depth.** The floors only help with HTRs you get to. Solutions with S+T of 5 or more on both sides stay out of reach by hand (example J).
- **The doc's NISS advice by subset** (convert 4a3 to 4b3; from 0c4, 4a4 and 4b4, NISS after the first qt and set up to 4b3) isn't tested subset by subset. Section 12 pools all 3qt and all 4qt DRs.
- **Pseudo-pairs by kind.** Rodney Kinney reads which pseudo-pairs go with a corner case. Section 9 only counts them, together with the true pairs.
- **Other goals.** One goal per kind of DR. A looser goal lets more HTRs past both floors.

## Appendix: how it was computed, and what is proved in Lean

**The sample.** 2,000 uniformly random DRs for each of 2qt, 3qt and 4qt. {2000 - nd[2]} of the 2qt draws have 0c0 corners up to a turn of both layers and are left out. Of the {num(nd[2])}, {num(nd[3])} and {num(nd[4])} DRs, {num(ns[2])}, {num(ns[3])} and {num(ns[4])} have a within-goal solution, so a share of DRs carries about ±3 points (95%).

**Every HTR in reach.** For each DR, on normal and on inverse, every HTR with up to two quarter turns more than the minimum whose moves plus corner-case moves fit the goal: {num(R[2]['records'] + R[3]['records'] + R[4]['records'])} HTRs in all. Each one gets its optimal leave-slice finish from the exact table of HTR states, its rule value, its pairs at 2qt, 1qt and HTR, and the HTR-equivalent pairs of its 2qt and 3qt states on both sides. The case of an HTR is read the way the sheet lists it, on the inverse of the state the HTR lands on.

**The states on the way.** For the same DRs, every state with 2 or 3 quarter turns left on a route with at most 1 extra move so far, on both sides ({num(sum(PR[m]['states']['2|2']['n'] for m in QT))} 4a2 and 4b2 states with 2 left): pairs, HTR-equivalent pairs on the state and on its inverse, and the fewest moves to HTR on both sides.

**Checks.**

- The best HTR of each side equals the optimal leave-slice length of the DR, for every solvable DR in the sample but {R[2]['unreached'] + R[3]['unreached'] + R[4]['unreached']}: {R[2]['unreached']} of the 2qt DRs and {R[3]['unreached']} of the 3qt DRs have all their within-goal solutions four quarter turns past the minimum (section 4), and the search stops at two.
- A second search that prunes with the exact leave-slice table instead finds the same within-goal HTRs with the same totals (450 DRs, {num(MC)} solutions).
- Every solution printed on this page was replayed on an independent sticker model, and the pair counts of the examples, true and HTR-equivalent, at 2qt on both sides and at HTR, were read off its stickers.
- The HTR-equivalent pair count: 16 on all 663,552 HTR states and on their inverses; on 300,000 random DR states the sticker form agrees with the orbit form, U and D moves keep it, a side half turn moves it by at most 4, an HTR state played first changes neither the count nor the fewest moves to HTR, and the floor holds on the state and on its inverse.

**Base rates** come from 20 million random DR states looked up in the exact table.

**The rule on all HTR states.** In each of the 216 cases, the shortest leave-slice finish over its 3,072 states is at least the corner moves plus the rule's value. That is all 663,552 HTR states.

**Lean** (project *PairFloor*, no library, on the cube model of [*Judging a DR by hand*](../judging-a-dr/); builds in under a minute).

| Theorem | What it says |
|---|---|
| `pairs_move_ud` | U and D moves, quarter or half, keep the number of pairs. |
| `pairs_step` | One DR move changes the number of pairs by at most 4 if it's a side half turn, and not at all otherwise. |
| `pairs_of_lsSolved` | With the corners and the U/D edges solved there are 16 pairs. |
| `pair_floor` | If a sequence of DR moves solves the corners and the U/D edges of a state with p pairs, then 16 ≤ p + 4 × (its side half turns). |
| `pair_floor_length` | The same with the length of the sequence: a finish of n moves needs at least 16 − 4n pairs. |
| `pair_floor_full` | The same for a full solve. |
| `htrPair_iff_orbits` | A slot holds an HTR-equivalent pair exactly when its corner is out of its tetrad and its edge out of its slice orbit, or neither is. |
| `pairs_le_hpairs` | A state has at least as many HTR-equivalent pairs as true pairs. |
| `hpairs_move_ud`, `hpairs_step` | U and D moves keep the number of HTR-equivalent pairs, and a side half turn changes it by at most 4. |
| `hpairs_of_isHTR` | A state reached from the solved cube by half turns has all 16. |
| `hpairs_after_htr` | After the same moves, an HTR state and the solved cube have the same number of HTR-equivalent pairs: the count on the way to HTR doesn't depend on the HTR state the route lands on. |
| `htr_pair_floor` | If a sequence of DR moves takes a state with k HTR-equivalent pairs to HTR, then 16 ≤ k + 4 × (its side half turns). |
| `htr_pair_floor_length` | The same with the length: 16 + 4 × (its quarter turns) ≤ k + 4 × (its length). |

All of them are checked by Lean's kernel, with no compiled computation. Examples in the same files show the floors are reached: `R2`, `R2 L2`, `R2 L2 F2`, `R2 L2 F2 B2` for pairs; `U R2 U`, `U R2 L2 U`, `U R2 F2 B2 U`, `U R2 L2 F2 B2 U` for HTR-equivalent pairs.

Not in Lean: the two refinements at HTR (10 pairs need 3 moves, 2 pairs need 5), which are exact counts over the 663,552 HTR states; that the pair count is the same on the inverse, which held on every state of the sample and on 300,000 random DR states; the exact table of section 9; and every percentage on this page.

**Changed on 18 November 2026.**

- **A sequence now stops at the first HTR it reaches.** Before, a route that reached an HTR and went on through two more quarter turns to another HTR state was counted as a further HTR. Most of those were the same HTR with a `U D` after it, which is a `U2` of its finish. They were {pct(1 - (R[2]['records'] + R[3]['records'] + R[4]['records']) / OLD_TOTAL)} of the {num(OLD_TOTAL)} HTRs counted, so every count of HTRs per DR came down, by {tri(lambda m: pct(1 - R[m]['records'] / OLD_REC[m]))} (2qt / 3qt / 4qt), and the shares within goal went up with it. No DR lost a solution: the reach of every search, the share of DRs left with nothing found and the NISS reach are what they were. With fewer repeats to finish, found-within-5 for both floors and most pairs first went from {tri(lambda m: pct(OLD_BEST5[m]))} to {tri(lambda m: Rk(m, 3, BESTK, 5))}.
- **The baseline has the pair floor.** It was shortest HTR first with pairs as the tie-break and no floor.
- **New:** pairs at 2qt with and without the rule (section 8), HTR-equivalent pairs (section 9) and the Lean theorems that go with them.
"""
import os
assert R[4]['unreached'] == 0     # the appendix sentence names only the 2qt and 3qt DRs
os.makedirs(os.path.dirname(OUT), exist_ok=True)
open(OUT, 'w').write(T)
print('written', OUT, len(T.split('\n')), 'lines')
# the solutions quoted inside example remarks and the doc's first 13, replayed
from exview import check_normal
assert check_normal("L2 B2 D U2 L2 U' R2 F2 L2 B2 U' F2", "F2 D L2 F2 R2 B2 D R2 D B2 L2")
assert check_normal("R2 U B2 D2 B2 R2 U' R2 D2 L2 U' F2 U", "B2 U' L2 F2 U L2 U' B2 U' F2 L2 U2 R2 B2")
assert check_normal("U D L2 D' B2 U R2 F2 B2 D2 L2 D' R2 L2 D2 B2", "R2 B2 U' L2 B2 U L2 B2 D B2 R2 D2 F2")
print('remark solutions replay')
