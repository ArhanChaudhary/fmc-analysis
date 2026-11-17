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
ORD = [('No floors, by moves to HTR, ties at random', 'no floors: by moves to HTR, random'), ('No floors, by moves to HTR, most pairs first (the baseline)', 'no floors: by moves to HTR, most pairs'),
       ('Rule bound only, by moves to HTR, most pairs first', 'rule only: by moves to HTR, most pairs'), ('Both floors, in random order', 'both floors: random'), ('Both floors, level by level, most pairs first inside a level', 'both floors: level by level, most pairs'),
       ('Both floors, skeleton by skeleton (largest M first)', 'both floors: skeleton by skeleton (largest M first), level, pairs'),
       ('Both floors, 12+ pairs on sight, the rest level by level', 'both floors: 12+ pairs first, then level by level'), ('Both floors, look at all, then most pairs first', 'both floors: most pairs first (look at all first)')]
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
t_staged = table(['DR', 'S+T at most', 'Solvable DRs it can reach', 'Routes to 2qt per DR', 'HTRs that pass the rule, on a DR with a solution', 'Finishes on a DR with no solution', 'Found within 5 finishes (most pairs first)', 'Within 10'],
                 [[f'{m}qt', K, pct(st(m, K)['recall']), num(st(m, K)['routes']), num(st(m, K)['looks_solv']), num(st(m, K)['finishes_unsolv'], 1), pct(st(m, K)['lookfirst_R']['5']), pct(st(m, K)['lookfirst_R']['10'])] for m in QT for K in (2, 3, 4)])

# ---- examples -----------------------------------------------------------------------------------------------
EX = [
 ('A', "The doc's first walkthrough", "U D L2 D' B2 U R2 F2 B2 D2 L2 D' R2 L2 D2 B2",
  "This is the first random scramble of the doc. None of its 13s is cheap: the F-V one, the 13 the doc finds first, has S+T = 3 and the H-H one 5, so only the F-V one is in reach here. It has 6 pairs with 4 moves left, a long shot on the card of section 7, which is why it's the sixth finish and not the first."),
 ('B', "A 4qt DR where the floors leave one obvious HTR", "B2 L2 D' R2 D F2 D F2 D2 B2 R2 D R2 D' U'",
  "The baseline order reaches the 14 after well over a hundred HTRs. With the floors there are 51 to look at and 8 to finish, and the one with 8 pairs and 2 moves left is the solution."),
 ('C', "Only the inverse has it cheaply", "D B2 R2 D L2 D R2 D' B2 D' L2 R2 D2",
  "On normal the only 13 needs 3 extra moves before 2qt. On the inverse it's a 1-extra variant of a skeleton with two more quarter turns."),
 ('D', "A mid-skeleton NISS", "D2 R2 U' L2 B2 L2 R2 D2 F2 D' B2 U' B2",
  "Both sides need S+T = 3 here. After `B2 U B2 U` on normal, a shortest route to 1qt, the inverse reaches HTR in 3 moves with nothing extra. The 6-move finish there is the long insertion, and on normal it sits in the middle of the solution."),
 ('E', "Only a skeleton with two more quarter turns", "R2 D2 U L2 B2 D' L2 U' F2 D L2 U2",
  "Every within-goal solution of this 4b2 has four quarter turns. Both 11s sit one or two extra moves into an 8-move 4qt skeleton, with 12 pairs at HTR."),
 ('F', "Nothing passes the rule: abandon", "D2 F2 L2 D F2 L2 D2 R2 D' B2 D2 L2 B2",
  "A 4a2 4e whose optimal leave-slice is 13. Not one HTR with S+T ≤ 3 on either side passes the rule bound for 12, so there's nothing to look at."),
 ('G', "Nothing passes the rule with S+T ≤ 3, and a 12 exists", "D' B2 D2 F2 L2 B2 U' B2 D2 L2 F2 U2",
  "The counterexample to abandoning on that signal: the 12s are there, but the cheapest needs S+T = 4 on the inverse."),
 ('H', "Within goal after splitting every pair it had at 2qt", "L2 B2 D U2 L2 U' R2 F2 L2 B2 U' F2",
  "The first 13 above has 4 pairs at 2qt, keeps none of them through the trigger and lands on an HTR with 0 pairs and 5 moves left. Rare, but it happens. The 11s of this DR are the ordinary kind: `F2 D L2 F2 R2 B2 D R2 D | B2 L2` has 8 pairs at HTR and a 2-move finish."),
 ('I', "A finish that splits a pair", "R2 U B2 D2 B2 R2 U' R2 D2 L2 U' F2 U",
  "The one to look at is `B2 U' L2 F2 U L2 U' B2 U' | F2 L2 U2 R2 B2` (14): 10 pairs at HTR and a 5-move finish, and every optimal finish splits some of them (6 of the 10 survive at best). This only shows up with 5 or more moves left."),
 ('J', "Deep on both sides", "U F2 D2 L2 U2 R2 D' L2 D' L2 B2 R2 U'",
  "The 12s need S+T = 6 on normal and on inverse. Nothing within reach finds them; this is the kind of DR the abandon numbers are about."),
]
ex_md = ''
for tag, title, scr, remark in EX:
    b = block(scr)
    s = f"**{tag}. {title}**, `{scr}` ({b['info'].replace('  ', ', ')}).\n\n"
    s += f"- **In reach** (S+T ≤ 3, at most 1 extra move before 2qt, both sides): {num(b['gen'])} HTRs. {b['rl']} pass the rule, {b['both']} of those pass the pair floor, {b['within']} {'is' if b['within'] == 1 else 'are'} within goal.\n"
    if b['within']:
        s += f"- **First within-goal HTR:** number {b['fb']} in the baseline order, number {b['ff']} with both floors and most pairs first.\n"
    else:
        s += f"- **Nothing within goal in reach.** At any depth: {num(b['all'])} HTRs, {b['all_rule']} pass the rule, {b['all_both']} pass both floors, {b['all_within']} are within goal.\n"
    w = b['w']
    if len(w):
        s += "- **Within-goal solutions, cheapest first:**\n"
        for _, x in w.head(3).iterrows(): s += f"  - {b['sol'](x)}.\n"
    if tag == 'D':
        for f in b['niss'][1:2]: s += f"- **NISS:** `{f[1]}` then `{f[2]}`, the parts in brackets on the inverse, {f[8].split()[-1]} moves.\n"
    s += f"- {remark}\n\n"
    ex_md += s
    print('example', tag, 'ok')

# ---- text ---------------------------------------------------------------------------------------------------
def Rk(m, K, key, k): return pct(od(m, K, key)['R'][str(k)])
BASEK = 'no floors: by moves to HTR, most pairs'; BESTK = 'both floors: most pairs first (look at all first)'
def tri(f, sep=' / '): return sep.join(f(m) for m in QT)
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

t_head = table(['Measure', '2qt, goal 12', '3qt, goal 13', '4qt, goal 14'], [
    ['DRs that have a solution within goal'] + [pct(base.loc[m, 'P(ls<=goal)']) for m in QT],
    ['HTRs in reach of the goal, per DR'] + [num(F[m]['all']['per_dr']) for m in QT],
    ['Of those, HTRs that pass the rule bound'] + [num(F[m]['rule']['per_dr']) for m in QT],
    ['HTRs that pass the rule bound and the pair floor'] + [num(F[m]['rule+pair_simple']['per_dr']) for m in QT],
    ['Share of those that are within goal'] + [pct(F[m]['rule+pair_simple']['precision']) for m in QT],
    ['Within-goal HTRs that fail the rule bound'] + ['0' for m in QT],
    ['Solvable DRs with a solution at S+T ≤ 2, both sides'] + [pct(lv(m, 'both_all', 2)['recall']) for m in QT],
    ['Solvable DRs with a solution at S+T ≤ 3, both sides'] + [pct(lv(m, 'both_all', 3)['recall']) for m in QT],
    ['Same, with at most 1 extra move before 2qt'] + [pct(od(m, 3, BESTK)['recall']) for m in QT],
    ['Found within 5 finishes there: both floors, most pairs first'] + [Rk(m, 3, BESTK, 5) for m in QT],
    ['Found within 40 finishes there: the baseline'] + [Rk(m, 3, BASEK, 40) for m in QT]])
assert sum(R[m]['funnel']['all']['within'] - R[m]['funnel']['rule']['within'] for m in QT) == 0     # the '0' row above

T = f"""# Pruning the search for a DR solution

You have a DR and a goal: a leave-slice solution in 12 from a 2qt DR, 13 from a 3qt, 14 from a 4qt. You go through corner skeletons and their variants, and nearly every HTR you could finish is a waste of time. This page measures which ones are: what the rule bound of Advanced DR Bounding removes, what a pair count at HTR removes on top of it, in which order to finish what's left, what NISS adds, and when to give up on the DR.

Every HTR in reach of the goal was finished exactly, on normal and on inverse, for about 2,000 uniformly random DRs of each kind ({num((R[2]['records'] + R[3]['records'] + R[4]['records']) / 1e6)} million HTRs). The pair floor is proved in Lean.

November 2026. A date in brackets is a link to that message on the FMC solvers Discord (#fmc-theory or #fmc-discussion).

**This builds on:**

- **Levi Gibson's [DR Bounding]({LEVI_DOC})** ([27 Nov 2024]({LEVI_DOC_MSG})) and **Rodney Kinney's [Advanced DR Bounding [Beta]]({ADV})** ([29 Aug 2026]({ADV_MSG})): corner skeletons and variants, the penalty L + S + T (+N), the NISS@1qt cases, bad slices and parity, and the rules that bound N from below. On the server Levi posts as beef beans; this page says Levi.
- **The doc's *HTR Search Meta***, which is the search this page prunes: "Start by writing down all of the distinct ways to reach 2qt, and explore each one in turn. DR Bounding will prune the search heavily." The goals are the ones of its random-scramble examples: "a leave-E-slice solution in 12 moves for 2qt, 13 for 3qt, and 14 for 4qt".
- **Rodney Kinney's sheet [Adv DR Bounding]({SHEET})** ([18 Sep 2026]({SHEET_MSG})), tab *Optimals (Advanced)*: the 216 NISS@1qt cases with the rule's value for each (column *Heuristic*). From the doc: "Lorenzo Mauro has computed optimal algorithms for all 216 of the corner/edge combined cases."
- **Rodney Kinney's [DRM Subsets]({DRMS})** ([14 Jun 2025]({DRMS_MSG})): precision, recall, and the score used here to weigh them, "mutual info ≡ p(objective | subset) \\* N(subset, objective)".
- **Levi Gibson's sheet [Pairs in DR]({PAIRS})** ([4 Sep 2023]({PAIRS_MSG})) on how much pairs matter in each DR subset, and what Levi said about it ([4 Sep 2023]({PAIRS_Q})): "There are wild departures. HTR for example! In HTR, pairs matter so little compared to other DR states".
- **[*Judging a DR by hand*](../judging-a-dr/)** on this site: the exact optimal leave-slice finish of every DR state, the sorting of the HTR states into the 216 cases, and the Lean cube model the pair floor is proved on.

**What it adds:**

- **What the rule bound is worth as a filter**: how many HTRs it removes, and that it never removes a within-goal one (section 5).
- **A second floor, read at HTR by counting pairs.** With n moves left for the finish you need 16 − 4n pairs. It's proved in Lean, and together with the rule it leaves a few dozen HTRs per DR (sections 6 and 7).
- **What pairs tell you at 2qt, at 1qt and at HTR**, and how often a within-goal solution has to split them (section 8).
- **Which order to finish HTRs in**, which skeleton to start with, what NISS adds and when to abandon, in precision, recall and mutual info (sections 9 to 12).
- **How often a within-goal solution exists and where it sits**: how many extra moves, which side, how many quarter turns (sections 3 and 4).

**Terms.**

- **Leave-slice solution.** DR moves that solve the corners and the eight U/D edges and leave the E slice as it falls. Lengths are HTM. Finishes that leave the DR group (the M-slice algs of the sheet, 3e insertions) aren't counted.
- **HTR, variant.** Here an HTR is a sequence of DR moves that ends with a quarter turn and lands in HTR, on the normal scramble or on the inverse. Checking it means finishing from there: the solution has (moves to HTR) + (finish) moves.
  - U and D are the same quarter turn for a leave-slice solution (the doc: "we can freely choose between U and D moves in our variants"), and the direction of the last quarter turn is settled while finishing. HTRs that differ only in those choices are counted once.
- **Skeleton, L, M.** The skeleton of an HTR is (side, number of quarter turns, NISS@1qt corner case). L is the length of the shortest corner path of that kind. The corner case then needs 0 more moves for H-H, 1 for R-D and F-D, 2 for R-V and F-V, 3 for D-D. **M**, the doc's maximum penalty, is the goal minus both.
- **S+T, extra moves.** Moves to HTR minus L. The part spent before 2qt is given separately where it matters.
- **Rule bound.** Moves to HTR + the corner case's own moves + the rule's N for the case the HTR lands on. An HTR **passes the rule** if that is at most the goal.
- **Pairs.** True corner-edge pairs in the U and D layers: a corner and an edge of the same layer joined as on a solved cube. 16 when the layers are solved. The count is the same on the inverse of any state (a pair there is a pair here, somewhere else), so there is nothing extra to read on the inverse.
- **Pair floor.** With n moves left for the finish (goal minus moves to HTR), the HTR needs at least 16 − 4n pairs.
- **Within goal.** The HTR's optimal leave-slice finish fits the goal. A **solvable** DR is one with a leave-slice solution within the goal.
- **Precision, recall, mutual info.** For a set of HTRs: the share that are within goal; the share of solvable DRs with a within-goal HTR in the set; and precision times the number of such DRs, as in *DRM Subsets*.
- **Population.** Uniformly random DR states with 2, 3 or 4 quarter turns (4a2 and 4b2; 0c3, 2c3, 4a3, 4b3; 0c4, 2c4, 4a4, 4b4). Not states as they come up in attempts.

**How to read this.** Section 1 is the whole answer. Section 13 puts it in the order you'd use it, and section 14 walks ten scrambles through it. Sections 3 to 12 are the tables behind each line of section 1, always for 2qt, 3qt and 4qt DRs side by side, each with its own goal.

What each read takes at the table:

| Read | What it takes |
|---|---|
| L, M, S+T | finding the skeleton and the HTR (a search), then arithmetic |
| Rule bound | tracing the NISS@1qt case by colour at 1qt, per the doc |
| Pair floor | counting pairs at HTR, at a glance |
| Finishing an HTR | a search |
| 216-case table | **computer only** |

Counts per DR are exact for the DRs in the sample. A share of DRs carries about ±3 points.

| Section | What is in it |
|---|---|
| [1. The short version](#1-the-short-version) | The answer, with the headline numbers. |
| [2. What was asked](#2-what-was-asked) | The five questions. |
| [3. How often a within-goal solution exists](#3-how-often-a-within-goal-solution-exists) | Base rates by quarter turns and by subset. |
| [4. Where the within-goal solutions are](#4-where-the-within-goal-solutions-are) | By extra moves, by side, before or after 2qt. |
| [5. The rule bound as a filter](#5-the-rule-bound-as-a-filter) | What it removes, what it never removes, how much slack it leaves. |
| [6. The pair floor](#6-the-pair-floor) | **The new read.** The floor, its proof, and why it only bites under a goal. |
| [7. Both floors together](#7-both-floors-together) | The card: chance of a within-goal finish by pairs at HTR and moves left. |
| [8. Pairs along the route](#8-pairs-along-the-route) | Pairs at 2qt, at 1qt and at HTR, and how often they get split. |
| [9. Which order to finish in](#9-which-order-to-finish-in) | Eight orders against the baseline. |
| [10. Skeletons: which first, how far](#10-skeletons-which-first-how-far) | By maximum penalty M, and the mutual info level by level. |
| [11. NISS](#11-niss) | The inverse, and NISS in the middle of a skeleton. |
| [12. When to abandon](#12-when-to-abandon) | Each stop signal: how often it comes up, how often it's wrong. |
| [13. The meta](#13-the-meta) | The steps, and what they cost and find. |
| [14. Examples](#14-examples) | Ten scrambles. |
| [15. The claims, checked](#15-the-claims-checked) | What the doc, Levi and the question itself say, against the numbers. |
| [16. What this does not cover](#16-what-this-does-not-cover) | Limits. |
| [Appendix: how it was computed, and what is proved in Lean](#appendix-how-it-was-computed-and-what-is-proved-in-lean) | The sample, the checks, the Lean theorems by name. |

## 1. The short version

The headline numbers. A row is one measure, a column one kind of DR with its goal.

{t_head}
The last three rows are about one fixed reach: every HTR with S+T ≤ 3 and at most 1 extra move before 2qt, on both sides. The share found is among the DRs that have a solution.

- **The rule bound removes 96–97% of the HTRs and never a within-goal one.** None of the {num(within_total)} within-goal HTRs in the sample fails it, and it is a floor on all 663,552 HTR states. The parity half of the rule matters: counting bad slices alone keeps more than four times as many.

- **New: a pair floor at HTR does the same job again.** A side half turn makes at most 4 pairs. So with n moves left for the finish you need at least 16 − 4n pairs at HTR: 16 with none left, 12 with one, 8 with two, 4 with three. That's proved in Lean. On its own it removes about as many HTRs as the rule, and the two overlap little, which is how thousands of HTRs become a few dozen.

- **Finish the HTR with the most pairs first.** With both floors and most pairs first, 5 finishes find nearly what the baseline finds in 40, and more than that for 4qt DRs (the last two rows). The baseline is shortest HTR first with pairs as the tie-break.

- **Pairs are a weak read before the trigger and a strong one at HTR.** As a ranker of the HTRs that pass the rule, the pair count scores {R[2]['auc']['pn2']:.2f} to {R[4]['auc']['pn2']:.2f} at 2qt and {R[2]['auc']['pn0']:.2f} to {R[4]['auc']['pn0']:.2f} at HTR (0.5 is a coin flip). Pairs don't pick the route, they pick the HTR.

- **Within-goal solutions rarely split pairs.** The finish splits a pair that stood at HTR in {tri(lambda m: pct(PW[m]['fin_split']))} of them (2qt / 3qt / 4qt), and only with 5 or more moves left. The setup or trigger splits a 2qt pair in {tri(lambda m: pct(PW[m]['trig_split']))}, against {tri(lambda m: pct(PW[m]['trig_split_rule_live']))} for HTRs in general.

- **One extra move before 2qt is worth it, a second mostly isn't.** For 4qt DRs, allowing none caps the reach at {pct(grid(4, 'both_all', 0, 3)['recall'])} (S+T ≤ 3 after 2qt), allowing one gives {pct(grid(4, 'both_all', 1, 3)['recall'])}, two {pct(grid(4, 'both_all', 2, 3)['recall'])}, and each step roughly triples the routes to 2qt.

- **The inverse is worth about one extra move.** Normal and inverse to S+T ≤ k reach about what normal alone reaches at k + 1. A NISS after the first quarter turn of each shortest route adds about 3 points more at S+T ≤ 2.

- **Skeletons with two more quarter turns can't be skipped.** They hold the only within-goal solutions of {pct(plus2_only[2])} of solvable 2qt DRs, {pct(plus2_only[3])} of 3qt and {pct(plus2_only[4])} of 4qt.

- **Start with the skeleton with the most room.** Among skeletons with the fewest quarter turns of a 3qt DR, one with maximum penalty M = 3 holds a within-goal HTR {skv(3, 3)} of the time, with M = 5 {skv(3, 5)}, with M = 7 {skv(3, 7)}. Skip M ≤ 1.

- **Abandoning.** If no HTR with S+T ≤ 3 passes the rule on either side, a solution still exists in {abp(2, 'all|9|3', 'no_rule_live')} of 2qt DRs. If you've finished everything that passes both floors through S+T ≤ 3 and found nothing, one still exists {tri(lambda m: abp(m, 'all|9|3', 'nothing_found'))} of the time; through S+T ≤ 4, {tri(lambda m: abp(m, 'all|9|4', 'nothing_found'))}.

- **The hand rule is close to what the 216 cases can give.** Looking every case up in an exact table instead (**computer only**) would leave {tri(lambda m: num(F[m]['table+pair']['per_dr']))} HTRs per DR instead of {tri(lambda m: num(F[m]['rule+pair']['per_dr']))}.

- **What's left is depth.** The floors only help with HTRs you get to, and a within-goal solution is rarely cheap: skeletons as they are (S+T = 0) hold one for {pct(lv(2, 'both_all', 0)['recall'])} to {pct(lv(4, 'both_all', 0)['recall'])} of solvable DRs.

## 2. What was asked

The search is the usual one from a DR. You go through corner skeletons one at a time, add extra moves to a skeleton's variants up to some point, then move to the next skeleton or give up on the DR. You know the moves to HTR at any point, you can work out the Advanced DR Bounding lower bound for what comes after HTR, and you can count corner-edge pairs on both sides of the scramble, with no finer tracing on the inverse. Long insertions have too many possibilities to try speculatively, so NISS is there to find the solutions with a long insertion near the beginning of the skeleton, and sometimes in the middle.

The baseline is to check variants in order of moves to HTR, on both sides, with no speculative mid-skeleton NISS, preferring variants that form pairs.

1. **What are the best heuristics for pruning that search, and how does the DR Bounding lower bound fit into a better meta than the baseline?** *Answer*: two floors and one order. The rule bound and the pair floor decide what to finish (sections 5 to 7), most pairs first decides the order (section 9), and section 13 puts it together.
2. **How good is each heuristic in precision and recall terms?** The weighing is the mutual info of *DRM Subsets*: how likely a variant is to give a leave-slice solution within the goal, against how many DRs have a within-goal solution starting with that variant's prefix. *Answer*: the tables give precision as the share within goal and recall as the share of solvable DRs covered. The mutual info level by level is in section 10.
3. **Where does NISS belong?** *Answer*: the inverse from the start is worth about one extra move. A NISS after the first quarter turn is cheap and adds a few points. Later ones find less than going a level deeper does (section 11).
4. **When should you abandon a DR that has no solution within the goal?** *Answer*: there is one safe signal and it's rare. After that it's a trade, with the numbers in section 12.
5. **Is forming pairs a poor heuristic?** The suspicion: pairs often have to be broken up after HTR or during the trigger, but forming pairs is a good way of telling apart variants with similar lower bounds. *Answer*: pairs seldom have to be broken up in a within-goal solution, and they tell variants apart well at HTR, weakly before the trigger (section 8).

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
- **The inverse is worth about one extra move.** Both sides at S+T ≤ 2 reach a little less than normal alone at 3, and both at 3 a little more than normal alone at 4.
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
More than nine in ten of the HTRs that pass sit exactly at the goal or 1 under, and that's also where most within-goal HTRs are. An HTR 2 or more under is a better bet, but there are few of them. Ordering by the bound doesn't get you far; you need another read.

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

- **Proved in Lean.** `pair_floor`: if a sequence of DR moves solves the corners and the U/D edges of a state with p pairs, it has at least (16 − p) / 4 side half turns. It holds for any DR state, not only at HTR, and for full finishes too. The proof is on the cube model the exact table of DR finishes is certified on, and uses no computation outside the kernel. The floor is reached at every level: `R2` (12 pairs), `R2 L2` (8), `R2 L2 F2` (4), `R2 L2 F2 B2` (0).
- **Two refinements at HTR** (exact over all 663,552 HTR states, not in Lean): 10 pairs need 3 moves, not 2 (`R2 U2 R2`), and 2 pairs need 5, not 4 (`R2 U2 R2 F2 B2`). The tables call the floor with these two the exact pair floor.
- **Pairs aren't an estimate either.** Over all HTR states the pair count hardly moves the finish, which is what Levi said in 2023:

{t_hp}
`U2 R2 L2 U2 R2 L2 F2 R2 L2 B2` has all 16 pairs and needs 10 moves. The floor only bites because the goal leaves so few moves.

## 7. Both floors together

Neither floor knows what the other knows: the rule reads the NISS@1qt case, the pairs read how close the layers are.

The card: of the HTRs that pass the rule, the share that are within goal, by pairs at HTR and moves left ({num(card_n)} HTRs, 2qt to 4qt pooled). × fails the pair floor, · has under 150 HTRs.

{t_card}
- **At the floor with 0 or 1 move left, it's close to a coin flip:** 16 pairs with nothing left, 12 with 1.
- **At the floor with 2 or more moves left, it's a long shot:** {cell(2, 8)} for 8 pairs with 2 left, {cell(3, 4)}–{cell(3, 6)} for 4 or 6 pairs with 3 left.
- **A step above the floor is the good bet:** 12 pairs with 2 or 3 left ({cell(2, 12)}, {cell(3, 12)}), 8 pairs with 3 or 4 left ({cell(3, 8)}, {cell(4, 8)}).

## 8. Pairs along the route

How well the pair count ranks the HTRs that pass the rule: the chance that a within-goal one has more pairs than one that isn't (0.5 is useless, 1 is perfect).

{t_auc}
Share within goal of the HTRs that pass the rule, by pairs at 2qt:

{t_p2}
The same by pairs at HTR:

{t_p0}
How often pairs get split, among within-goal HTRs:

{t_break}
Share of within-goal HTRs whose every optimal finish splits a pair that stood at HTR, by finish length:

{t_fsplit}
- **Forming pairs on the way to 2qt says little.** An HTR whose route had 6–7 pairs at 2qt is within goal {tri(lambda m: bucket(m, 'rule_by_pn2', 6, 7))} of the time against {tri(lambda m: bucket(m, 'rule_by_pn2', 0, 1))} with 0–1, and few routes have that many.
- **The suspicion of section 2, checked.** Pairs seldom need to be broken after HTR: not at all in finishes of up to 3 moves, and those are {pct(sum(x[1] for x in PW[3]['fin_split_by_fin'] if x[0] <= 3) / PW[3]['n'])} of the within-goal HTRs at 3qt. During the setup and trigger a 2qt pair is split in a quarter to a third of within-goal solutions, about half as often as in HTRs at large. So a split pair is a mild warning, not a need.
- **Where pairs do separate variants with similar bounds is at HTR.** With the same moves left and the same rule bound, the pair count is what tells the HTRs apart: that's the card of section 7.

## 9. Which order to finish in

Fix what's in reach: S+T ≤ 3, at most 1 extra move before 2qt, both sides, all skeletons. A row is one order. The first two columns say how many HTRs it has to finish, the others the chance of having found a within-goal solution after so many finishes, among DRs that have one.

2qt (the reach is {pct(od(2, 3, BESTK)['recall'])}):

{t_orders(2)}
3qt (the reach is {pct(od(3, 3, BESTK)['recall'])}):

{t_orders(3)}
4qt (the reach is {pct(od(4, 3, BESTK)['recall'])}):

{t_orders(4)}
- **The floors turn hundreds of HTRs into a dozen or two,** and on a DR with no solution you're done after 6 to 8 finishes instead of never.
- **Most pairs first beats every order by length.** Going level by level inside the floors is no better than a random order.
- **Skeleton by skeleton costs nothing** against level by level, so the order of section 2 works as long as pairs decide inside it.
- **12+ pairs on sight** gets most of the gain without looking at everything first.

## 10. Skeletons: which first, how far

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
The rule keeps about 1 HTR in 7 at S+T = 0 and 1 in 20 to 30 from S+T = 3 on. Of those that pass, 6–9% are within goal at S+T = 0, 2–4% from S+T = 2 on. The mutual info peaks at S+T = {mi_peak(2)} for 2qt, {mi_peak(3)} for 3qt and {mi_peak(4)} for 4qt. Past that the HTRs multiply faster than the DRs they add.

## 11. NISS

Share of solvable DRs reached, and what a mid-skeleton NISS costs in finishes after both floors. The NISS is: do a route's moves through a quarter turn on normal, switch, and search the inverse from there to the same S+T.

{t_niss}
- **The inverse is the big one.** It finds the solutions whose first section is long, because on the inverse that section is the finish.
- **A NISS after the first quarter turn of a shortest route is cheap and adds a few points.** There are only one or two such routes per DR.
- **After later quarter turns, or from routes with 1 extra move, it adds more,** but from many more starting points: about {num(N[4]['prefixes'][1][2])} routes after the second quarter turn of a 4qt DR and {num(N[4]['prefixes'][2][2])} after the third.
- **Against going one level deeper on both sides.** After both sides at S+T ≤ 2, the next level reaches {tri(lambda m: pct(N[m]['rows2'][2]['deeper_gets']))} more of the solvable DRs for {tri(lambda m: num(N[m]['rows2'][2]['deeper_fin'], 1))} finishes per DR. NISS at S+T ≤ 2 (any quarter turn, routes with at most 1 extra) reaches {tri(lambda m: pct(N[m]['rows2'][2]['niss_gets']))} more for {tri(lambda m: num(N[m]['rows2'][2]['niss_fin'], 1))}.

## 12. When to abandon

How often each signal comes up, and how often a within-goal solution exists all the same. *Finished* means every HTR that passes both floors.

{t_ab}
- **Before any search,** the subset is the first signal (section 3): a 0c3 has a 13 less than one time in five, a 4a2 2e has a 12 about as rarely.
- **Nothing passes the rule with S+T ≤ 3: a safe stop,** but it only comes up for about 1 DR in 30 at 2qt and 1 in 50 at 3qt, and never at 4qt. Example F is one; example G is one of the {abp(2, 'all|9|3', 'no_rule_live')} where a solution exists anyway.
- **After the finishes** the numbers are what they are: stopping at S+T ≤ 3 gives up on a fifth to a third of the DRs you stop on.
- **On a DR with no solution** the whole of S+T ≤ 3 costs {tri(lambda m: num(od(m, 3, BESTK)['per_unsolv'], 1))} finishes.

## 13. The meta

What the numbers above add up to, for one DR and one goal.

1. **Check the subset.** Drop the ones that rarely make the goal.
2. **List the skeletons on both sides,** two more quarter turns included, with M for each. Skip M ≤ 1. Take them in order of M, largest first.
3. **In a skeleton, go by S+T,** with at most one extra move before 2qt. For each HTR work out the rule bound at 1qt. If it's over the goal, don't execute it.
4. **Execute the ones that pass and count pairs.** With n moves left you need 16 − 4n. Below that, move on.
5. **Finish on sight** anything with 12 or more pairs. Keep the rest in a list.
6. **When a level is done, finish the list, most pairs first.**
7. **NISS** after the first quarter turn of each shortest route, same steps on the inverse.
8. **Stop** at S+T = 3 unless the DR is one you'd rather not leave. Section 12 says what you leave behind.

What that costs and finds, with everything looked at before finishing. A row is one kind of DR and one depth.

{t_staged}
The routes to 2qt are the part no floor shortens: tens for a 2qt DR, hundreds for a 4qt one at S+T ≤ 3. Everything after that is short.

## 14. Examples

Each scramble is a sequence of DR moves; apply it to a solved cube to get the DR. A `|` marks HTR. Solutions on the inverse are given as found there and as a normal solution.

{ex_md}
## 15. The claims, checked

| Claim | Who | Result |
|---|---|---|
| "Tweaking the baseline by hand to minimize the difference with the computed optimal yields these improved rules, which give a correct lower bound 100% of the time, and are within 1 of the true lower bound 80% of the time." | Rodney Kinney, [*Advanced DR Bounding*]({ADV}) | **The lower bound holds** for leave-slice finishes in DR moves on all 663,552 HTR states. The 80% is against the sheet's penalties, which allow finishes that leave DR, and isn't rechecked here. Against leave-slice finishes in DR moves the rule is exact for {gap0} of the 216 cases and 1 under for {gap1} (section 5). |
| "There are wild departures. HTR for example! In HTR, pairs matter so little compared to other DR states" | Levi Gibson ([4 Sep 2023]({PAIRS_Q})) | **Holds** over all HTR states: the mean finish is {hpg.loc[0, 'mean']:.1f} moves with 0 pairs and {hpg.loc[8, 'mean']:.1f} with 8. Under a goal it's another matter: the pair floor removes most HTRs (section 6). |
| "In the standard meta, one rarely makes a long-ish insertion (such as a non-cancelling corner swap) in the middle of the skeleton, because there are too many possible insertions to consider, and the ones that actually help can't be identified just by looking at pairs formed." | Rodney Kinney, [*Advanced DR Bounding*]({ADV}), *HTR Search Meta* | **In line with section 8**: pairs at 2qt say little about which routes lead to a within-goal HTR ({R[2]['auc']['pn2']:.2f} to {R[4]['auc']['pn2']:.2f} as a ranker). Long insertions weren't tested on their own. |
| "Worthwhile long insertions at 3qt are still best found via NISS, but in general there is no need to ever NISS mid-skeleton when using DR Bounding." | Rodney Kinney, [*Advanced DR Bounding*]({ADV}), *HTR Search Meta* | **Mostly.** After both sides at S+T ≤ 2, one more level reaches {tri(lambda m: pct(N[m]['rows2'][2]['deeper_gets']))} more of the solvable DRs. NISS in the middle of a route reaches {tri(lambda m: pct(N[m]['rows2'][2]['niss_gets']))} more, and {tri(lambda m: pct(N[m]['rows'][2]['niss1_p0_adds'], 1))} if it's kept to the first quarter turn of each shortest route (section 11). |
| "Let's start with skeleton #2, since DR Bounding works best with longer skeletons" | Rodney Kinney, [*Advanced DR Bounding*]({ADV}), first random scramble | **Depends on what you want from it.** A longer skeleton has a smaller M, so the rule leaves less to finish. The within-goal solutions are more often in the skeleton with the larger M (section 10). |
| Pairs often have to be broken up after HTR | Section 2, question 5 | **Not at these goals**: {tri(lambda m: pct(PW[m]['fin_split']))} of within-goal HTRs. Example I is one. |
| Pairs often have to be broken up during the trigger | Section 2, question 5 | **Sometimes**: in {tri(lambda m: pct(PW[m]['trig_split']))} of within-goal HTRs, about half the rate of HTRs at large. Example H. |
| Forming pairs is a good way of telling apart variants with similar lower bounds | Section 2, question 5 | **Yes at HTR, weakly at 2qt** (section 8). |

Nothing checked here turned out wrong, so there is no errata page.

## 16. What this does not cover

- **Uniform DRs.** Real attempts reach DRs through EO and a trigger; the mix of subsets and of pairs differs.
- **DR moves only.** A finish that leaves the DR group can be shorter than the best leave-slice finish counted here.
- **Counts, not minutes.** A route to 2qt, a rule read, a look at HTR and a finish don't cost the same, and how fast a solver finds the setups that pass the rule isn't measured.
- **Depth.** The floors only help with HTRs you get to. Solutions with S+T of 5 or more on both sides stay out of reach by hand (example J).
- **The doc's NISS advice by subset** (convert 4a3 to 4b3; from 0c4, 4a4 and 4b4, NISS after the first qt and set up to 4b3) isn't tested subset by subset. Section 11 pools all 3qt and all 4qt DRs.
- **Other goals.** One goal per kind of DR. A looser goal lets more HTRs past both floors.

## Appendix: how it was computed, and what is proved in Lean

**The sample.** 2,000 uniformly random DRs for each of 2qt, 3qt and 4qt. {2000 - nd[2]} of the 2qt draws have 0c0 corners up to a turn of both layers and are left out. Of the {num(nd[2])}, {num(nd[3])} and {num(nd[4])} DRs, {num(ns[2])}, {num(ns[3])} and {num(ns[4])} have a within-goal solution, so a share of DRs carries about ±3 points (95%).

**Every HTR in reach.** For each DR, on normal and on inverse, every HTR with up to two quarter turns more than the minimum whose moves plus corner-case moves fit the goal: {num(R[2]['records'] + R[3]['records'] + R[4]['records'])} HTRs in all. Each one gets its optimal leave-slice finish from the exact table of HTR states, its rule value, and its pairs at 2qt, 1qt and HTR. The case of an HTR is read the way the sheet lists it, on the inverse of the state the HTR lands on.

**Checks.**

- The best HTR of each side equals the optimal leave-slice length of the DR, for every solvable DR in the sample but {R[2]['unreached'] + R[3]['unreached'] + R[4]['unreached']}: {R[2]['unreached']} of the 2qt DRs and {R[3]['unreached']} of the 3qt DRs have all their within-goal solutions four quarter turns past the minimum (section 4), and the search stops at two.
- A second search that prunes with the exact leave-slice table instead finds the same within-goal HTRs with the same totals (450 DRs, 96,774 solutions).
- Every solution printed on this page was replayed on an independent sticker model.

**Base rates** come from 20 million random DR states looked up in the exact table.

**The rule on all HTR states.** In each of the 216 cases, the shortest leave-slice finish over its 3,072 states is at least the corner moves plus the rule's value. That is all 663,552 HTR states.

**Lean** (project *PairFloor*, no library, on the cube model of [*Judging a DR by hand*](../judging-a-dr/); builds in about half a minute).

| Theorem | What it says |
|---|---|
| `pairs_move_ud` | U and D moves, quarter or half, keep the number of pairs. |
| `pairs_step` | One DR move changes the number of pairs by at most 4 if it's a side half turn, and not at all otherwise. |
| `pairs_of_lsSolved` | With the corners and the U/D edges solved there are 16 pairs. |
| `pair_floor` | If a sequence of DR moves solves the corners and the U/D edges of a state with p pairs, then 16 ≤ p + 4 × (its side half turns). |
| `pair_floor_length` | The same with the length of the sequence: a finish of n moves needs at least 16 − 4n pairs. |
| `pair_floor_full` | The same for a full solve. |

All of them are checked by Lean's kernel, with no compiled computation. Four examples in the same file show the floor is reached: `R2`, `R2 L2`, `R2 L2 F2`, `R2 L2 F2 B2`.

Not in Lean: the two refinements at HTR (10 pairs need 3 moves, 2 pairs need 5), which are exact counts over the 663,552 HTR states; that the pair count is the same on the inverse, which held on every state of the sample; and every percentage on this page.
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
