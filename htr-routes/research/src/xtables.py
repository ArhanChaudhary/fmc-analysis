#!/usr/bin/env python3
"""report/data/*.md (the tables of the write-up) and out/report_extra.json (numbers the text quotes that are not a
table cell), all from the result files in out/.  Light: reads TSVs and the per-state files of the main pass.
usage: xtables.py"""
import csv, json, collections, os, math
import numpy as np
from common import R, OUT, SUBS, SIZE, CGROUPS, CORNER, load_states
D = os.path.normpath(os.path.join(R, '..', 'report', 'data')) + '/'
os.makedirs(D, exist_ok=True)
def T(name): return list(csv.DictReader(open(f'{OUT}/{name}'), delimiter='\t'))
def pc(x, d=None):
    x = float(x) * 100
    if x == 0: return '0%'
    if 99.95 <= x and d is None: return '>99.9%'
    if d is None: d = 1 if x >= 1 else 2 if x >= 0.1 else 3
    return f'{x:.{d}f}%'
def cls2(r):
    m = r.get('mirror_alias', '')
    return cls(r['class']) + (f" (mirror: {cls(m)})" if m else '')
def cls(c): return '`' + (c[:-5] if c.endswith(' | ht') else c).replace('|', '\\|') + '`'   # (an escaped pipe: these go in table cells)
def write(name, head, rows):
    out = ['| ' + ' | '.join(head) + ' |', '|' + '---|' * len(head)] + ['| ' + ' | '.join(str(x) for x in r) + ' |' for r in rows]
    open(D + name + '.md', 'w').write('\n'.join(out) + '\n')
E = {}
# ------------------------------------------------------------------ checklists
bud = T('q2_checklist_budget.tsv')
same = T('q2_same_classes_p1.tsv')
def lst(g, b, tg='opt'):
    return [r for r in bud if r['group'] == g and r['level'] == 'C' and r['target'] == tg and r['budget'] == b]
def sm(g, b): return [r for r in same if r['group'] == g and r['budget'] == b]
rows = []
for g in CGROUPS:
    a = lst(g, '2'); s = sm(g, '2')
    rows.append([g, cls2(a[0]), cls2(a[1]), cls2(a[2])]
                + [pc(a[i]['cumulative']) for i in (0, 1, 2, 4)] + [pc(s[2]['cum_p1']), pc(lst(g, 'inf')[2]['cumulative'])])
# one table of routes, one of shares (one value per cell, at most 7 columns)
SH = ['Optimal found, 1 route', 'Optimal found, 2 routes', 'Optimal found, 3 routes', 'Optimal found, 5 routes', 'Within +1, same 3 routes']
write('checklist_corner', ['Subset', 'Try first', 'Then', 'Then'], [r[:4] for r in rows])
write('checklist_corner_shares', ['Subset'] + SH + ['Optimal found, 3 routes, no HTR limit'], [r[:1] + r[4:] for r in rows])
rows = []
for s_ in SUBS:
    a = lst(s_, '2'); s = sm(s_, '2')
    rows.append([s_, cls2(a[0]), cls2(a[1]), cls2(a[2])] + [pc(a[i]['cumulative']) for i in (0, 1, 2, 4)] + [pc(s[2]['cum_p1'])])
write('checklist_edges', ['Subset', 'Try first', 'Then', 'Then'], [r[:4] for r in rows])
write('checklist_edges_shares', ['Subset'] + SH, [r[:1] + r[4:] for r in rows])
BH = ['Subset', 'Budget 0 (shortest HTRs only)', 'Budget 1', 'Budget 2', 'No HTR limit']
for k, name in ((0, 'budgets_1'), (2, 'budgets_3')):
    write(name, BH, [[g] + [pc(lst(g, b)[k]['cumulative']) for b in ('0', '1', '2', 'inf')] for g in CGROUPS])
# full appendix: per subset x edges, budget 2, 8 classes, opt and +1 (same classes)
rows = []
for s_ in SUBS:
    for r, q in zip(lst(s_, '2'), sm(s_, '2')):
        rows.append([s_ if r['step'] == '1' else '', r['step'], cls2(r), pc(r['cumulative']), pc(q['cum_p1'])])
write('checklist_full', ['Subset', '#', 'Class', 'Optimal, cumulative', 'Within +1, cumulative'], rows)
rows = []
for s_ in SUBS:
    for r in lst(s_, 'inf')[:4]:
        rows.append([s_ if r['step'] == '1' else '', r['step'], cls(r['class']), pc(r['cumulative'])])
write('checklist_nolimit', ['Subset', '#', 'Class', 'Optimal, cumulative'], rows)
# best-set check
best = T('q2_best.tsv')
d = [float(r['best_possible']) - float(r['greedy_cumulative']) for r in best]
E['best_cases'] = len(d); E['best_within_05'] = sum(x <= 0.005 for x in d); E['best_max_gap'] = max(d)
E['single_b0'] = [min(float(lst(g, '0')[0]['cumulative']) for g in CGROUPS), max(float(lst(g, '0')[0]['cumulative']) for g in CGROUPS)]
E['single_b2'] = [min(float(lst(g, '2')[0]['cumulative']) for g in CGROUPS), max(float(lst(g, '2')[0]['cumulative']) for g in CGROUPS)]
E['single_inf'] = [min(float(lst(g, 'inf')[0]['cumulative']) for g in CGROUPS), max(float(lst(g, 'inf')[0]['cumulative']) for g in CGROUPS)]
mg = [float(r['marginal']) for g in CGROUPS for r in lst(g, '2') if int(r['step']) > 3]
E['marg_after3_max'] = max(mg); E['marg_after3_share_lt3'] = sum(x < 0.03 for x in mg) / len(mg)
# what the edge count is worth (edge_gain.py): own subset x edges checklist vs the pooled corner checklist, budget 2
eg = T('q2_edge_gain.tsv'); KS = ('1', '2', '3', '5')
def gain(r, k): return float(r[f'own{k}']) - float(r[f'pooled{k}'])
tot = sum(SIZE[r['subset']] for r in eg if r['target'] == 'opt')
EG = {'rows': {}, 'all': {}, 'corner': {}}
for tg in ('opt', 'p1'):
    rs = [r for r in eg if r['target'] == tg]
    EG['all'][tg] = {k: sum(SIZE[r['subset']] * gain(r, k) for r in rs) / tot for k in KS}
    for g in CGROUPS:
        EG['corner'].setdefault(g, {})[tg] = {k: sum(float(r['weight_in_corner']) * gain(r, k) for r in rs if r['corner'] == g) for k in KS}
    for r in rs:
        EG['rows'].setdefault(r['subset'], {})[tg] = dict(r, **{f'gain{k}': gain(r, k) for k in KS})
big = lambda s: max(abs(EG['rows'][s][tg][f'gain{k}']) for tg in ('opt', 'p1') for k in KS) >= 0.01
od = [s for s in EG['rows'] if EG['rows'][s]['opt']['first_differs'] == '1']
EG['n'] = len(EG['rows']); EG['first_differs'] = od; EG['first_differs_share'] = sum(SIZE[s] for s in od) / tot
EG['big'] = [s for s in EG['rows'] if big(s)]; EG['flat'] = [s for s in EG['rows'] if not big(s)]
EG['flat_corners'] = [g for g in CGROUPS if all(s in EG['flat'] for s in EG['rows'] if CORNER(s) == g)]
EG['max'] = {k: max(EG['rows'], key=lambda s: EG['rows'][s]['opt'][f'gain{k}']) for k in KS}
E['eg'] = EG
GH = ['After 1 route (own − pooled, points)', 'After 2 routes', 'After 3 routes', 'After 5 routes']
rows, rows_p1, rows_sh = [], [], []
for s_ in EG['big']:
    o, p = EG['rows'][s_]['opt'], EG['rows'][s_]['p1']
    rows.append([s_, 'same' if o['first_differs'] == '0' else cls(o['own_first']), o['pooled_first_rank']] + [f"{gain(o, k) * 100:+.1f}" for k in KS])
    rows_p1.append([s_] + [f"{gain(p, k) * 100:+.1f}" for k in KS])
    rows_sh.append([s_, 'own'] + [pc(o[f'own{k}']) for k in KS])
    rows_sh.append([s_, 'pooled'] + [pc(o[f'pooled{k}']) for k in KS])
write('edge_gain', ['Subset', 'Own list: first route', "Pooled list's first route: place in own list"] + GH, rows)
write('edge_gain_p1', ['Subset'] + GH, rows_p1)
write('edge_gain_shares', ['Subset', 'List', 'Optimal found, 1 route', 'Optimal found, 2 routes', 'Optimal found, 3 routes', 'Optimal found, 5 routes'], rows_sh)
# routes read with the edge count at every step (edge_steps.py)
from common import level_of
VIA = collections.defaultdict(dict)
for r in T('q2_edge_steps_via.tsv'): VIA[(r['subset'], r['target'])][r['via']] = float(r['share'])
XS = ('4b2', '2c3', '4a1', '4a2', '4c3'); EDG = ('0e', '2e', '4e', '6e', '8e')
tot = sum(SIZE[s] for s in SUBS)
ES = {'rev': {}, 'via': {}, 'ref': {}, 'all': {}}
for tg in ('opt', 'p1'):
    for x in XS:
        anyx = sum(SIZE[s] * VIA[(s, tg)].get(x + ' *', 0) for s in SUBS) / tot
        ES['rev'][f'{x}|{tg}'] = {'any': anyx, **{e: sum(SIZE[s] * VIA[(s, tg)].get(f'{x} {e}', 0) for s in SUBS) / tot / anyx for e in EDG}}
    for s in SUBS:
        ES['via'][f'{s}|{tg}'] = VIA[(s, tg)]
rows = []
for x in XS:
    for tg in ('opt', 'p1'):
        r = ES['rev'][f'{x}|{tg}']
        rows.append([x if tg == 'opt' else '', {'opt': 'optimal', 'p1': 'within +1'}[tg], pc(r['any'])]
                    + [pc(r[e]) if r[e] > 0 else '–' for e in EDG])
write('edge_via_reverse', ['Intermediate subset', 'Target', 'DRs that can pass it', 'of those, via 0e', 'via 2e', 'via 4e', 'via 6e', 'via 8e'], rows)
# per starting subset x edges and intermediate subset: share that can pass it at all, then per edge count (under 0.5% left out)
for x in XS:
    rows = []
    for s in SUBS:
        v = VIA[(s, 'opt')]
        if v.get(x + ' *', 0) < 0.005: continue
        rows.append([s, pc(v[x + ' *'])] + [pc(v[f'{x} {e}']) if v.get(f'{x} {e}', 0) >= 0.005 else '–' for e in EDG])
    write('edge_via_' + x, ['Subset', f'Can pass {x}' if x != '4c3' else 'Can pass 4c3 (4a3 or 4b3)', 'via 0e', 'via 2e', 'via 4e', 'via 6e', 'via 8e'], rows)
# edge-refined checklists against corner-only
ck = T('q2_edge_steps_checklist.tsv')
alias = {}
for r in bud:
    if r['level'] == 'C' and r['budget'] == '2' and r['step'] == '1': alias[(r['group'], r['target'])] = (r['class'], r['mirror_alias'])
KS4 = (1, 2, 3, 5)
for s in SUBS:
    for tg in ('opt', 'p1'):
        rr = sorted([r for r in ck if r['subset'] == s and r['target'] == tg], key=lambda r: int(r['step']))
        at = lambda k, col: float(rr[min(k, len(rr)) - 1][col])
        proj = level_of('H:' + rr[0]['class'], 'C')
        c1 = at(1, 'corner_only_cumulative')
        match = next((int(r['step']) for r in rr if float(r['cumulative']) >= c1 - 5e-5), None)
        ES['ref'][f'{s}|{tg}'] = {'edge': [at(k, 'cumulative') for k in KS4], 'corner': [at(k, 'corner_only_cumulative') for k in KS4],
                                  'first': rr[0]['class'], 'first_mirror': rr[0]['mirror_alias'],
                                  'first_same_corner': proj in alias[(s, tg)], 'match1': match}
for tg in ('opt', 'p1'):
    ES['all'][tg] = {'edge': [sum(SIZE[s] * ES['ref'][f'{s}|{tg}']['edge'][i] for s in SUBS) / tot for i in range(4)],
                     'corner': [sum(SIZE[s] * ES['ref'][f'{s}|{tg}']['corner'][i] for s in SUBS) / tot for i in range(4)],
                     'n_same_first': sum(ES['ref'][f'{s}|{tg}']['first_same_corner'] for s in SUBS),
                     'match1': collections.Counter(ES['ref'][f'{s}|{tg}']['match1'] for s in SUBS)}
ES['n'] = len(SUBS)
E['es'] = ES
rows, rows_e = [], []
for s in SUBS:
    o = ES['ref'][f'{s}|opt']
    rows.append([s] + [pc(x) for x in o['corner']])
    rows_e.append([s] + [pc(x) for x in o['edge']] + [cls(o['first']) + (f" (mirror: {cls(o['first_mirror'])})" if o['first_mirror'] else ''), o['match1'] or '>8'])
write('edge_refined', ['Subset', 'Optimal found, 1 corner route', '2 routes', '3 routes', '5 routes'], rows)
write('edge_refined_paths', ['Subset', 'Optimal found, 1 edge path', '2 paths', '3 paths', '5 paths', 'First edge path', 'Edge paths to match the first corner route'], rows_e)
# ------------------------------------------------------------------ docs 171 / 15 / 66
def mad(f):
    r = T(f); a = np.array([float(x['doc_share']) for x in r]); o = np.array([float(x['our_expected_share_random_tiebreak']) for x in r])
    return len(r), float(abs(a - o).mean()), float(np.corrcoef(a, o)[0, 1])
E['d171_ls'] = mad('compare_doc171_leave_slice.tsv'); E['d171_full'] = mad('compare_doc171.tsv')
d15 = T('compare_doc15.tsv')
dd = [abs(float(r['doc_solution_mean']) - float(r['exact_mean_opt'])) for r in d15 if r['doc_solution_mean'] not in ('', 'nan')]
E['d15_sol_max'] = max(dd); E['d15_n'] = len(dd)
dn = [abs(float(r['doc_niss_htr_mean']) - float(r['our_niss_htr'])) for r in d15 if r['doc_niss_htr_mean'] not in ('', 'nan')]
E['d15_niss_max'] = max(dn)
x = [r for r in d15 if r['our_subset'] == '4b2 2e'][0]
E['d15_4b2'] = dict(doc=x['doc_linear_htr_mean'], normal=x['our_linear_htr_normal'], best=x['our_linear_htr_best_side'])
d66 = T('compare_doc66.tsv')
E['d66_rows'] = len(d66)
nm = T('name_map.tsv')
E['names'] = {f"{r['doc']}|{r['label']}": r['our_subset'] for r in nm}
# ------------------------------------------------------------------ Q3
q3 = {r['group']: r for r in T('q3_htr.tsv')}
E['q3'] = q3
rows = []
for g in CGROUPS + ['all']:
    r = q3[g]
    rows.append([g if g != 'all' else 'all DRs', f"{float(r['mean_htr_niss']):.2f}", f"{float(r['mean_htr_linear_best_side']):.2f}", f"{float(r['mean_htr_normal']):.2f}",
                 pc(r['niss_eq_linear']), pc(r['niss_shorter_by_1']), pc(r['niss_shorter_by_2plus'])])
write('htr_lengths', ['Subset', 'Shortest NISS HTR, mean (moves)', 'Shortest linear, better side (moves)', 'Normal side (moves)', 'NISS = linear', 'NISS 1 shorter', 'NISS 2+ shorter'], rows)
rows = []
for g in CGROUPS + ['all']:
    r = q3[g]
    rows.append([g if g != 'all' else 'all DRs', pc(r['opt_uses_shortest_niss']), pc(r['opt_htr_plus1']), pc(r['opt_htr_plus2']), pc(r['opt_htr_plus3more']),
                 pc(r['every_opt_htr_ge9']), pc(float(r['every_opt_htr_ge9']) - float(r['niss_htr_ge9'])), f"{float(r['mean_post_htr_longest_in_an_optimal']):.2f}"])
write('htr_vs_opt', ['Subset', 'Optimal uses a shortest HTR', 'Best is 1 longer', '2 longer', '3 or more longer', 'Every optimal needs 9+', '… though a sub-9 HTR exists', 'Post-HTR moves, mean'], rows)
bl = [r for r in T('q3_htr_by_length.tsv') if r['group'] == 'all' and float(r['states_share_with_shortest_niss_L']) >= 0.004]
E['bylen_cov'] = sum(float(r['states_share_with_shortest_niss_L']) for r in bl); E['bylen_out'] = [r['L'] for r in T('q3_htr_by_length.tsv') if r['group'] == 'all' and 0 < float(r['states_share_with_shortest_niss_L']) < 0.004]
write('htr_by_length', ['Shortest NISS HTR (L)', 'Share of DRs', 'An optimal uses an L-move HTR'], [[r['L'], pc(r['states_share_with_shortest_niss_L']), pc(r['opt_uses_an_L_move_htr'])] for r in bl])
# ------------------------------------------------------------------ Q4 / Q5
q4 = {r['group']: r for r in T('q4_qt.tsv')}; E['q4'] = q4
write('extra_qt', ['Subset', 'Every optimal uses extra qts', 'Some optimal does', 'Every leave-slice optimal does'],
      [[g if g != 'all' else 'all DRs', pc(q4[g]['every_opt_extra_qt_vs_corners']), pc(q4[g]['some_opt_extra_qt_vs_corners']), pc(q4[g]['ls_every_opt_extra_qt_vs_corners'])] for g in CGROUPS + ['all']])
q5 = {r['group']: r for r in T('q5_states.tsv')}; E['q5'] = q5
write('variation', ['Subset', 'Mean optimal (moves)', 'Mean, last move either way (moves)', 'One shorter', 'Same', 'Optimal 15+', '15+ either way'],
      [[g if g != 'all' else 'all DRs', f"{float(q5[g]['mean_opt']):.2f}", f"{float(q5[g]['mean_opt_with_variation']):.2f}", pc(q5[g]['share_variation_shorter']), pc(q5[g]['share_variation_equal']),
        pc(q5[g]['share_ge15']), pc(q5[g]['share_ge15_with_variation'])] for g in CGROUPS + ['all']])
# ------------------------------------------------------------------ Q6
gr = T('q6_grading.tsv'); E['q6'] = gr
def grade(name, label):
    rows = [[r['step'], r['step_description'].replace('~', ''), pc(r['cumulative_opt_htr_budget2']), pc(r['cumulative_p1_htr_budget2']), pc(r['cumulative_opt'])] for r in gr if r['checklist'] == name]
    write(label, ['Step', 'What', 'Optimal (budget 2)', 'Within +1 (budget 2)', 'Optimal, no HTR limit'], rows)
grade('Zagros 4b2 order (D15884)', 'grade_zagros'); grade('Yura 4b2 4e order (D6409-D6416)', 'grade_yura'); grade('rogo/Adri 4b2 4e order (D6422-D6424)', 'grade_rogo')
grade('Lewis 4a2 0e/2e list (T6743)', 'grade_lewis'); grade('Fanti 4b2 4e split (D10034), cumulative', 'grade_fanti')
dch = [r for r in gr if r['checklist'].startswith('Daichi')]
rows = []
for r in dch:
    s_ = r['subsets']; a = lst(s_, '2')
    k = next((i + 1 for i, x in enumerate(a) if float(x['cumulative']) >= float(r['cumulative_opt_htr_budget2'])), None)
    rows.append([s_, pc(r['cumulative_opt_htr_budget2']), pc(r['cumulative_p1_htr_budget2']), pc(r['cumulative_opt']), pc(a[2]['cumulative']), str(k) if k else '> 8'])
write('grade_daichi', ['Subset', 'Optimal (budget 2)', 'Within +1 (budget 2)', 'Optimal, no HTR limit', 'My 3 classes (budget 2)', 'My classes to match'], rows)
# ------------------------------------------------------------------ Q8
V = {(r['group'], r['q'], r['R']): r for r in T('q8_bounding_stated.tsv')}
V1 = {(r['group'], r['q'], r['R']): r for r in T('q8_bounding_v2.tsv')}
E['q8w'] = {f'{k[0]}|{k[1]}|{k[2]}': v for k, v in V1.items()}
E['q8'] = {f'{k[0]}|{k[1]}|{k[2]}': v for k, v in V.items()}
def fo(g, q, R_, t='opt'): return pc(V[(g, q, str(R_))]['found_' + t])
def fn(g, q, R_): return f"{float(V[(g, q, str(R_))]['mean_reductions_le_R']):,.0f}"
GG = lambda g: g if g != 'all' else 'all DRs'
write('bounding', ['Subset', 'Optimal found, R ≤ 3', 'R ≤ 4', 'R ≤ 5', 'R ≤ 6', 'R ≤ 7'],
      [[GG(g)] + [fo(g, '1', R_) for R_ in (3, 4, 5, 6, 7)] for g in CGROUPS + ['all']])
write('bounding_counts', ['Subset', 'Reductions on average, R ≤ 3', 'R ≤ 4', 'R ≤ 5', 'R ≤ 6'],
      [[GG(g)] + [fn(g, '1', R_) for R_ in (3, 4, 5, 6)] for g in CGROUPS + ['all']])
write('bounding_other', ['Subset', 'Within +1 found, R ≤ 4', '12 or better found, R ≤ 5', 'To 2q, R ≤ 3: optimal found', 'To 2q, R ≤ 3: reductions on average'],
      [[GG(g), pc(V[(g, '1', '4')]['found_p1']), pc(V[(g, '1', '5')]['found_M12']), fo(g, '2', 3), fn(g, '2', 3)] for g in CGROUPS + ['all']])
rows = []
for g in CGROUPS:
    rr_ = next((R_ for R_ in range(0, 8) if float(V[(g, '1', str(R_))]['found_opt']) >= 0.8), None)
    if rr_ is None: bR, bN, b7 = 'more than 7', '', pc(V[(g, '1', '7')]['found_opt'])
    else: bR, bN, b7 = str(rr_), (f"{float(V[(g, '1', str(rr_))]['mean_reductions_le_R']):,.0f}" if rr_ < 7 else 'not reported'), ''
    def kfor(b):
        a = lst(g, b); k = next((int(x['step']) for x in a if float(x['cumulative']) >= 0.8), None)
        return (str(k), '') if k else (f"more than {len(a)}", pc(a[-1]['cumulative']))
    k2, k2f = kfor('2'); ki, kif = kfor('inf'); assert kif == ''
    rows.append([g, bR, bN, b7, k2, k2f, ki])
write('bounding_vs_checklist', ['Subset', 'Bounding: smallest R for 80%', 'Reductions on average at that R', 'If not reached: found at R ≤ 7',
                                'Checklist routes for 80%, budget 2', 'If not reached: found after 8 routes', 'Routes for 80%, no HTR limit'], rows)
se = [float(r['se_opt']) for k, r in V.items() if k[0] in CGROUPS]
E['q8_se_max_corner'] = max(se)
# reductions grow per extra move
gr7 = [float(V[(g, '1', '6')]['mean_reductions_le_R']) / float(V[(g, '1', '5')]['mean_reductions_le_R']) for g in CGROUPS if float(V[(g, '1', '5')]['mean_reductions_le_R']) > 0]
E['q8_growth'] = [min(gr7), max(gr7)]
# ------------------------------------------------------------------ Q9
q9v = T('q9_v2.tsv')
def agg(tg, col, wcol='cases_state_path'):
    rs = [r for r in q9v if r['target'] == tg and r[col] not in ('nan', '')]
    W_ = sum(int(r[wcol]) * SIZE[r['subset']] for r in rs)
    return sum(float(r[col]) * int(r[wcol]) * SIZE[r['subset']] for r in rs) / W_
Q9 = {}
for tg in ('opt', 'p1', 'M10', 'M11', 'M12'):
    _V = ('literal', 'no_term1', 'min_terms', 'min_terms_as_written', 'exact')
    Q9[tg] = {c: agg(tg, c) for c in [f'insuff_{v}' for v in _V] + [f'mean_R_{v}' for v in _V] +
              ['min_terms_eq_exact', 'mean_R_needed', 'LB_valid', 'LB_shared_valid', 'LB_beats_trivial', 'LB_shared_beats_trivial', 'LB_exact_beats_trivial', 'LB_reaches_opt']}
    Q9[tg].update({c: agg(tg, c, 'states') for c in ('mean_Rstate_literal', 'mean_Rstate_no_term1', 'mean_Rstate_min_terms', 'mean_Rstate_exact', 'R_empirical_max', 'skip_vs_empirical_no_term1', 'skip_vs_empirical_exact', 'state_insuff_no_term1', 'state_insuff_exact')})
    Q9[tg]['cases'] = sum(int(r['cases_state_path']) for r in q9v if r['target'] == tg)
    Q9[tg]['p90'] = agg(tg, 'p90_needed'); Q9[tg]['max'] = max(int(r['max_needed']) for r in q9v if r['target'] == tg)
E['q9'] = Q9
TN = {'opt': 'optimal', 'p1': 'optimal + 1', 'M10': '10 or better', 'M11': '11 or better', 'M12': '12 or better'}
write('fake_summary', ['Target', '(state, path) cases', 'Mean R, as written (largest term)', 'Without term 1', 'Smallest term', 'Exact model', 'Mean reduction needed'],
      [[TN[tg], f"{Q9[tg]['cases']:,}", f"{Q9[tg]['mean_R_literal']:.1f}", f"{Q9[tg]['mean_R_no_term1']:.1f}", f"{Q9[tg]['mean_R_min_terms']:.1f}", f"{Q9[tg]['mean_R_exact']:.1f}",
        f"{Q9[tg]['mean_R_needed']:.1f}"] for tg in TN])
write('fake_short', ['Target', 'Longest reduction needed (moves)', 'R too short: as written', 'Smallest term', 'Exact model'],
      [[TN[tg], Q9[tg]['max'], pc(Q9[tg]['insuff_literal']), pc(Q9[tg]['insuff_min_terms']), pc(Q9[tg]['insuff_exact'])] for tg in TN])
rod = T('q9_rodney_table.tsv')
rows = []
for s_ in SUBS:
    for M in ('M10:M=10', 'M11:M=11', 'M12:M=12'):
        x = [r for r in rod if r['subset'] == s_ and r['M_minus_opt_or_M'] == M]
        rows.append([s_, M.split('=')[1]] + ([x[0]['R_no_term1_worst_case'], x[0]['R_exact_worst_case'], x[0]['R_needed_max']] if x else ['', '', '']))
write('rodney_table', ['Subset', 'Target M', 'R from the formula without term 1', 'R from the exact model', 'Longest reduction needed'], rows)
t5 = T('q9_t11503_examples.tsv')
E['t11503_n'] = len(t5); E['t11503_subsets'] = sorted({r['subset'].split()[0] for r in t5})
E['t11503_cases_opt'] = Q9['opt']['cases']
_tc = open(f'{OUT}/checks/t11503_counts.txt').read().split()
E['t11503_counts'] = {_tc[i]: int(_tc[i + 1]) for i in range(0, len(_tc), 2)}
alpha = {r['path']: r['alpha_0..alpha_N'] for r in T('q9_alpha.tsv')}
E['alpha_4a3'] = alpha.get('4a3 > 4b2 > 4a1 > 0c0')
# ------------------------------------------------------------------ C11 / C13
c = {r['group']: r for r in T('c11_c13.tsv')}; E['c11'] = c
write('late_switch', ['Subset', 'Needs a switch after 3+ moves', 'After 4+ moves'],
      [[g if g != 'all' else 'all DRs', pc(c[g]['shortest_htr_needs_switch_after_gt2']), pc(c[g]['shortest_htr_needs_switch_after_gt3'])] for g in CGROUPS + ['all']])
# ------------------------------------------------------------------ claims evidence
E['claims'] = {r['id']: r for r in T('claims.tsv')}
# shortest linear HTR per subset (exact over cosets)
h = collections.defaultdict(lambda: 99)
for r in T('checks/htr48.tsv'):
    if int(r['cosets']) > 0: h[r['subset']] = min(h[r['subset']], int(r['htr_len']))
E['minlin'] = dict(h)
hm = collections.defaultdict(int)
for r in T('checks/htr48.tsv'): hm[r['subset']] = max(hm[r['subset']], int(r['htr_len']))
E['maxlin'] = dict(hm)
# allcases (doc 171) a/b: rows that go from 2qt(x) to a 3qt 2c case with one quarter turn
import re as _re, glob as _g
ac = open(_g.glob('/data/fmc/kb/docs/gsheet/1Vo6XzCFtJ-HEAuaBmk_pac-sJ3TbxEBb7BKsRJ_2wpA/allcases*.csv')[0]).read().split('\n')
E['ac_a_to_2c'] = sum(1 for l in ac if _re.match(r'^[0-9.]+,2qt\(a\)[^,]*,3qt 2c', l))
E['ac_b_to_2c'] = sum(1 for l in ac if _re.match(r'^[0-9.]+,2qt\(b\)[^,]*,3qt 2c', l))
E['ac_b_rows'] = sum(1 for l in ac if _re.match(r'^[0-9.]+,2qt\(b\)', l))
cd = open(f'{OUT}/checks/check_dist.txt').read()
E['cells473'] = int(_re.search(r'census.csv: (\d+) \(subset, depth\) cells, 0 differ', cd).group(1))
d15u = {r['doc15_label']: r for r in d15 if r['doc_solution_mean'] not in ('', 'nan')}
E['d15_rows'] = len(d15u)
E['d15_bad'] = {k: [r['our_subset'], abs(float(r['doc_solution_mean']) - float(r['exact_mean_opt'])), abs(float(r['doc_niss_htr_mean']) - float(r['our_niss_htr']))]
                for k, r in d15u.items() if abs(float(r['doc_solution_mean']) - float(r['exact_mean_opt'])) > 0.06 or abs(float(r['doc_niss_htr_mean']) - float(r['our_niss_htr'])) > 0.06}
# allcases' own shares for the paths Fanti and Levi Gibson summed
def _acsplit(start):
    one = two = reg = zz = five = 0.0
    for l in ac:
        p = l.strip().split(',')
        if len(p) > 2 and p[1] == start:
            sh = float(p[0]); q = len(p) - 2
            if q == 2: two += sh
            if q >= 5: five += sh
            if len(p) > 3 and p[2].startswith('3qt 2c'): reg += sh
            if len(p) > 3 and p[3].startswith('0qt 0c') and p[3] != '0qt 0c0e': zz += sh
    return dict(two=two, reg=reg, zz=zz, five=five)
E['ac_4b2_4e'] = _acsplit('2qt(a) 4c4e'); E['ac_4a1_4e'] = _acsplit('1qt 4c4e')
ls = collections.defaultdict(dict)
for l in open(f'{OUT}/checks/lsdist48.tsv'):
    a_, b_, c_ = l.split('\t'); ls[a_][int(b_)] = int(c_)
E['lsmax'] = {k: max(v) for k, v in ls.items()}
E['lsmax_count'] = {k: v[max(v)] for k, v in ls.items()}
E['size'] = dict(SIZE)
_w = {s_: SIZE[s_] for s_ in SUBS}
def _late(col, excl):
    ss = [s_ for s_ in SUBS if CORNER(s_) not in excl]
    return sum(float(c[s_][col]) * _w[s_] for s_ in ss) / sum(_w[s_] for s_ in ss)
E['late_excl_gt2'] = _late('shortest_htr_needs_switch_after_gt2', ('0c4', '4c4', '4c3'))
E['late_excl_gt3'] = _late('shortest_htr_needs_switch_after_gt3', ('0c4', '4c4', '4c3'))
# the same among readings with an HTR within budget 2 (DRs with no optimal reading within the budget are not counted)
E['late_b2_excl_gt2'] = _late('budget2_needs_switch_after_gt2', ('0c4', '4c4', '4c3'))
E['late_b2_excl_gt3'] = _late('budget2_needs_switch_after_gt3', ('0c4', '4c4', '4c3'))
# which T11503 bound fails in each counterexample: the first (|S|(R'+1)...), or the A / B / C versions
def _cov(lo, hi, minimal):
    """covering sets as in bounding.py: S of {lo..hi} with lo, hi in S, no two consecutive missing; minimal ones"""
    el = list(range(lo, hi + 1)); out = []
    for mask in range(1 << len(el)):
        S = [el[i] for i in range(len(el)) if mask >> i & 1]
        if lo not in S or hi not in S: continue
        if any(j not in S and j + 1 not in S for j in range(lo, hi)): continue
        out.append(frozenset(S))
    return [S for S in out if not any(T < S for T in out)] if minimal else out
def _es(S, al): return sum(al[i] for i in S if i + 1 in S)
_kinds = collections.Counter()
for r in t5:
    N = int(r['N']); al = [int(x) for x in r['alpha'].split(',')]; Rp = int(r['R_prime']); opt = int(r['opt'])
    A, B, C = int(r['A']), int(r['B']), int(r['C'])
    k = []
    if any(math.ceil((len(S) * (Rp + 1) - N + _es(S, al)) / (len(S) - 1) - 1e-9) > opt for S in _cov(0, N - 1, True) if len(S) > 1): k.append('first')
    if any(math.ceil(1 + Rp + (A - N + _es(S, al)) / len(S) - 1e-9) > opt for S in _cov(0, N - 2, True)): k.append('A')
    if any(math.ceil(1 + Rp + (B - N + _es(S, al)) / len(S) - 1e-9) > opt for S in _cov(1, N - 1, True)): k.append('B')
    if N > 2 and any(math.ceil(1 + Rp + (C - N + _es(S, al)) / len(S) - 1e-9) > opt for S in _cov(1, N - 2, True)): k.append('C')
    _kinds['+'.join(k) or 'none'] += 1
E['t11503_kinds'] = dict(_kinds)
if os.path.exists(f'{OUT}/q9_lb_values.tsv'):
    lv = {r['group']: r for r in T('q9_lb_values.tsv')}
    write('lb_values', ['Subset', '(state, path) cases', 'Corrected bound, median', 'Corrected bound, mean', 'Trivial bound, median', 'Trivial bound, mean', 'Mean optimum'],
          [[g, f"{int(lv[g]['cases']):,}", f"{float(lv[g]['median_lb']):g}", f"{float(lv[g]['mean_lb']):.2f}", f"{float(lv[g]['median_trivial']):g}", f"{float(lv[g]['mean_trivial']):.2f}", lv[g]['mean_opt']]
           for g in CGROUPS if g in lv])
    write('lb_shares', ['Subset', 'Bound above the trivial one', 'Bound reaches the optimum', 'Bound 11 or more'],
          [[g, pc(lv[g]['lb_beats_trivial']), pc(lv[g]['lb_reaches_opt']), pc(lv[g]['lb_ge_11'])] for g in CGROUPS if g in lv])
rows = []
for s_ in ['0c0 0e', '0c0 2e', '0c0 4e', '0c0 6e', '0c0 8e', '4a1 0e', '4a1 2e', '4a1 4e', '4a2 0e', '4a2 2e', '4a2 4e', '4b2 0e', '4b2 2e', '4b2 4e', '2c3 0e', '2c3 2e', '2c3 4e', '2c3 6e', '2c3 8e', '4c3 0e', '4c3 2e', '4c3 4e']:
    rows.append([s_, pc(V[(s_, '1', '4')]['found_opt']), pc(V[(s_, '1', '5')]['found_opt']), pc(lst(s_, '2')[2]['cumulative']), pc(lst(s_, '2')[4]['cumulative'])])
write('bound_vs_routes_edges', ['Subset', 'Bounding, R ≤ 4', 'Bounding, R ≤ 5', 'Checklist, 3 routes', 'Checklist, 5 routes'], rows)
_m = _re.search(r'mirror pairs checked over all 48 subsets: (\d+); identical state sets: (\d+)', open(f'{OUT}/SUMMARY.md').read())
E['alias_pairs'] = [int(_m.group(1)), int(_m.group(2))]
# ------------------------------------------------------------------ real DRs and DR-breaking finishes (gaps study)
# Everything from /data/fmc/gaps/research/out (and big/g2/uni1000.out for the table by DR-move optimum).
GP = '/data/fmc/gaps/research/'
def GT(name): return list(csv.DictReader(open(GP + 'out/' + name), delimiter='\t'))
GA = {}
_ov = json.load(open(GP + 'out/a_overview.json'))
GA['n_scr'] = _ov['scrambles']; GA['n_dr11'] = _ov['drs_le11']; GA['n_dr10'] = _ov['drs_le10']; GA['side_inv'] = _ov['side_inverse_share_dr11']
_as = {(r['group'], r['pop']): r for r in GT('a_subsets.tsv')}
P11 = ('dr11', 'scr11')
def _pse(v, s, flag=False, d=1):
    x = f"{float(v) * 100:.{d}f} ± {float(s) * 100:.{d}f}"
    return f"**{x}**" if flag else x
def _flag(u, su, r, sr):
    d = abs(float(r) - float(u)); return d > 0.02 and d > 2 * math.sqrt(float(su) ** 2 + float(sr) ** 2)
write('real_subsets', ['Subset', 'Share of DRs, uniform', 'Share, each DR once (± SE)', 'Share, each scramble once (± SE)', 'Mean optimal (moves), uniform', 'Mean optimal, each DR once', 'Mean optimal, each scramble once'],
      [[g, f"{float(_as[(g, 'dr11')]['uniform_share']) * 100:.2f}%"] + [_pse(_as[(g, p)]['share'], _as[(g, p)]['se'], d=2) for p in P11]
       + [f"{float(_as[(g, 'dr11')]['uniform_mean']):.3f}"] + [f"{float(_as[(g, p)]['mean_opt']):.3f} ± {float(_as[(g, p)]['se_mean']):.3f}" for p in P11] for g in CGROUPS])
GA['share_maxdiff'] = max(abs(float(_as[(g, p)]['share']) - float(_as[(g, p)]['uniform_share'])) * 100 for g in CGROUPS for p in P11)
GA['mean_maxdiff'] = max(abs(float(_as[(g, p)]['mean_opt']) - float(_as[(g, p)]['uniform_mean'])) for g in CGROUPS for p in P11)
GA['share_maxdiff10'] = max(abs(float(_as[(g, p)]['share']) - float(_as[(g, p)]['uniform_share'])) * 100 for g in CGROUPS for p in ('dr10', 'scr10'))
GA['mean_maxdiff10'] = max(abs(float(_as[(g, p)]['mean_opt']) - float(_as[(g, p)]['uniform_mean'])) for g in CGROUPS for p in ('dr10', 'scr10'))
# the bad-edge mix inside a corner subset, each scramble once: ratio of a cell's share of its corner subset to uniform
_mix = {}
for g in CGROUPS:
    for k in '02468':
        c = f'{g} {k}e'
        if (c, 'scr11') in _as:
            _mix[c] = (float(_as[(c, 'scr11')]['share']) / float(_as[(g, 'scr11')]['share'])) / (float(_as[(c, 'scr11')]['uniform_share']) / float(_as[(g, 'scr11')]['uniform_share']))
_r0 = sorted(v for c, v in _mix.items() if c.endswith(' 0e')); _r6 = sorted(v for c, v in _mix.items() if c.endswith(' 6e'))
GA['e0_rarer_n'] = sum(v < 1 for v in _r0); GA['e0_n'] = len(_r0); GA['e0_max_rarer'] = (1 - _r0[0]) * 100
GA['e0_max_cells'] = [c for c, v in sorted(_mix.items(), key=lambda kv: kv[1]) if c.endswith(' 0e')][:2]
GA['e6_max_more'] = (_r6[-1] - 1) * 100
# checklists (Q2), budget 2, greedy on each population
_bc = GT('b_checklist.tsv')
_u = {r['group']: r for r in _bc if r['run'] == 'uniform'}
_o = {(r['group'], r['pop']): r for r in _bc if r['run'] == 'real' and r['classes'] == 'own'}
_cols = (('after1', 'se1'), ('after2', 'se2'), ('after3', 'se3'), ('p1_after3', 'se_p1'))
def _same(g, p):
    a = [_u[g][f'class{i}'] for i in (1, 2, 3)]; b = [_o[(g, p)][f'class{i}'] for i in (1, 2, 3)]
    return 'yes' if a == b else 'same three, 2nd and 3rd swapped' if sorted(a) == sorted(b) and a[0] == b[0] else \
        'first two the same' if a[:2] == b[:2] else 'first the same' if a[0] == b[0] else 'no'
rows = []; GA['chk_flags'] = []
PN = {'dr11': 'each DR once', 'scr11': 'each scramble once'}
for g in CGROUPS:
    rows.append([g, 'uniform'] + [f"{float(_u[g][a]) * 100:.1f}" for a, s in _cols] + [''])
    for p in P11:
        r = _o[(g, p)]; fl = [_flag(_u[g][a], _u[g][s], r[a], r[s]) for a, s in _cols]
        if any(fl): GA['chk_flags'].append((g, p))
        rows.append(['', PN[p]] + [_pse(r[a], r[s], f) for (a, s), f in zip(_cols, fl)] + [_same(g, p)])
write('real_checklist', ['Subset', 'DRs', 'Optimal found, 1 route (%)', '2 routes', '3 routes', 'Within +1, 3 routes', 'Same three routes, same order as uniform'], rows)
GA['chk_maxdiff_ex0c0'] = max(abs(float(_o[(g, p)][a]) - float(_u[g][a])) * 100 for g in CGROUPS if g != '0c0' for p in P11 for a, s in _cols)
GA['first_same'] = all(_o[(g, p)]['class1'] == _u[g]['class1'] for g in CGROUPS for p in P11)
GA['order_changed'] = sorted({g for g in CGROUPS for p in P11 if _same(g, p) != 'yes'})
GA['c0c0_first'] = [float(_o[('0c0', p)]['after1']) * 100 for p in P11] + [float(_u['0c0']['after1']) * 100]
_m = lambda r, i: float(r[f'after{i}']) - float(r[f'after{i - 1}']) if i > 1 else float(r['after1'])
GA['c0c4_marg'] = [_m(_u['0c4'], 2) * 100, _m(_u['0c4'], 3) * 100]
_uc = {(r['group'], r['pop']): r for r in _bc if r['run'] == 'real' and r['classes'] == 'uniform classes'}
_cl = lambda c: '`' + c.replace(' | ht', '') + '`'
GA['c0c4'] = {'uni3': _cl(_u['0c4']['class3']), 'uni2': _cl(_u['0c4']['class2']),
              'new': _cl([c for c in (_o[('0c4', 'dr11')][f'class{i}'] for i in (1, 2, 3)) if c not in [_u['0c4'][f'class{j}'] for j in (1, 2, 3)]][0]),
              'pos': {p: [_o[('0c4', p)][f'class{i}'] for i in (1, 2, 3)].index([c for c in (_o[('0c4', 'dr11')][f'class{i}'] for i in (1, 2, 3)) if c not in [_u['0c4'][f'class{j}'] for j in (1, 2, 3)]][0]) + 1 for p in P11},
              'gap': {p: (float(_o[('0c4', p)]['after3']) - float(_uc[('0c4', p)]['after3'])) * 100 for p in P11}}
GA['cell_first_same'] = {p: sum(_o[(s, p)]['class1'] == _u[s]['class1'] for s in SUBS) for p in P11}
_c23 = _o[('2c3 0e', 'scr11')]; GA['c2c3_0e'] = [float(_c23['after1']) * 100, float(_c23['se1']) * 100, float(_u['2c3 0e']['after1']) * 100]
GA['c2c3_0e'] += [float(_o[('2c3 0e', 'dr11')]['after1']) * 100]           # the population that is not flagged, so the row has every cell
_c08 = _o[('0c0 8e', 'dr11')]; GA['c0c0_8e'] = [float(_c08['after1']) * 100, float(_c08['se1']) * 100, float(_u['0c0 8e']['after1']) * 100]
GA['c0c0_8e'] += [float(_o[('0c0 8e', 'scr11')]['after1']) * 100]
GA['cell_flag_list'] = sorted({s for p in P11 for s in SUBS if any(_flag(_u[s][a], _u[s][se], _o[(s, p)][a], _o[(s, p)][se]) for a, se in _cols)}, key=SUBS.index)
GA['cell_flags'] = {p: sum(any(_flag(_u[s][a], _u[s][se], _o[(s, p)][a], _o[(s, p)][se]) for a, se in _cols) for s in SUBS) for p in P11}
# the other headlines of section 1: Q3, bounding, hand checklists
_q3 = {(r['group'], r['pop'], r['metric']): r for r in GT('b_q3.tsv')}
_bd = {(r['group'], r['pop'], r['q'], r['R']): r for r in GT('b_bounding.tsv')}
_gr = {(r['checklist'], r['pop'], r['step']): r for r in GT('b_grades.tsv') if r['target'] == 'opt' and r['budget'] == '2'}
HL = [('Shortest NISS HTR = shortest linear, all DRs (section 6)', lambda p: _q3[('all', p, 'niss_eq_linear')], 'value', 'se'),
      ('NISS HTR 1 shorter, all DRs', lambda p: _q3[('all', p, 'niss_shorter_by_1')], 'value', 'se'),
      ('NISS HTR 2+ shorter, all DRs', lambda p: _q3[('all', p, 'niss_shorter_by_2plus')], 'value', 'se'),
      ('NISS HTR 2+ shorter, 0c3', lambda p: _q3[('0c3', p, 'niss_shorter_by_2plus')], 'value', 'se'),
      ('Some optimal uses a shortest NISS HTR, all DRs', lambda p: _q3[('all', p, 'opt_uses_shortest_niss')], 'value', 'se'),
      ('Every optimal needs an HTR of 9+, all DRs', lambda p: _q3[('all', p, 'every_opt_htr_ge9')], 'value', 'se'),
      ('Bounding to 1q, R ≤ 4, all DRs (section 8)', lambda p: _bd[('all', p, '1', '4')], 'found_opt', 'se_opt'),
      ('Bounding to 1q, R ≤ 5, all DRs', lambda p: _bd[('all', p, '1', '5')], 'found_opt', 'se_opt'),
      ('Bounding to 1q, R ≤ 3, 0c0', lambda p: _bd[('0c0', p, '1', '3')], 'found_opt', 'se_opt'),
      ('Bounding to 1q, R ≤ 5, 4a2', lambda p: _bd[('4a2', p, '1', '5')], 'found_opt', 'se_opt'),
      ('Bounding to 1q, R ≤ 5, 4a1', lambda p: _bd[('4a1', p, '1', '5')], 'found_opt', 'se_opt'),
      ('Bounding to 2q, R ≤ 3, all DRs', lambda p: _bd[('all', p, '2', '3')], 'found_opt', 'se_opt'),
      ("Zagros's 4b2 order, all five steps (section 10)", lambda p: _gr[('Zagros 4b2 order (D15884)', p, '5')], 'cumulative', 'se'),
      ("Yura Riabov's 4b2 4e order, three steps", lambda p: _gr[('Yura 4b2 4e order (D6409-D6416)', p, '3')], 'cumulative', 'se')]
rows = []; GA['hl_flags'] = []
for name, f, v, s in HL:
    u = f('uniform'); row = [name, _pse(u[v], u[s])]
    for p in P11:
        r = f(p); fl = _flag(u[v], u[s], r[v], r[s])
        if fl: GA['hl_flags'].append((name, p))
        row.append(_pse(r[v], r[s], fl))
    rows.append(row)
write('real_headlines', ['Headline', 'Uniform (± SE)', 'Each DR once (± SE)', 'Each scramble once (± SE)'], rows)
GA['hl_maxdiff_ex0c3'] = max(abs(float(f(p)[v]) - float(f('uniform')[v])) * 100 for name, f, v, s in HL if '0c3' not in name for p in P11)
GA['c0c3_2plus'] = [float(_q3[('0c3', p, 'niss_shorter_by_2plus')]['value']) * 100 for p in ('uniform',) + P11]
GA['b4a2_r5'] = [float(_bd[('4a2', p, '1', '5')]['found_opt']) * 100 for p in ('uniform',) + P11]
_q3c = [abs(float(_q3[(g, p, m)]['value']) - float(_q3[(g, 'uniform', m)]['value'])) * 100 for g in CGROUPS if g != '0c0' for p in P11
        for m in ('niss_eq_linear', 'niss_shorter_by_1', 'opt_uses_shortest_niss', 'every_opt_htr_ge9', 'opt_htr_plus1', 'opt_htr_plus2', 'opt_htr_plus3more')]
GA['q3_corner_max'] = max(_q3c)
GA['bd_maxdiff'] = max(abs(float(_bd[(g, p, q, R_)]['found_opt']) - float(_bd[(g, 'uniform', q, R_)]['found_opt'])) * 100
                       for g in CGROUPS + ['all'] for p in P11 for q in '12' for R_ in '345')
# DR-breaking finishes: nissy's any-move optimum against the DR-move optimum
_g2 = {(r['group'], r['pop']): r for r in GT('g2.tsv')}
_A = _g2[('all', 'uniform')]
GA['g2_all'] = {k: float(_A[k]) for k in ('shorter', 'se', 'by1', 'by2plus', 'mean_gain', 'mean_dr_opt', 'mean_true_opt')}
GA['g2_n'] = int(_A['n'])
GA['g2_real'] = {p: {k: float(_g2[('all', p)][k]) for k in ('shorter', 'se', 'mean_gain')} for p in P11 if ('all', p) in _g2}
GA['g2_real_n'] = int(_g2[('all', 'dr11')]['n']) if ('all', 'dr11') in _g2 else 0
_hasreal = bool(GA['g2_real'])
rows = []; rows_m = []
for g in CGROUPS + ['all']:
    r = _g2[(g, 'uniform')]
    row = [g if g != 'all' else 'all DRs', _pse(r['shorter'], r['se']) + '%']
    if _hasreal: row += [_pse(_g2[(g, p)]['shorter'], _g2[(g, p)]['se']) + '%' for p in P11]
    row += [f"{float(r['by1']) * 100:.1f}", f"{float(r['by2plus']) * 100:.1f}"]
    rows.append(row)
    rows_m.append([row[0], f"{float(r['mean_gain']):.3f}", f"{float(r['mean_dr_opt']):.2f}", f"{float(r['mean_true_opt']):.2f}"])
write('g2_subsets', ['Subset', 'Shorter finish outside DR, uniform (± SE)'] + (['Real DRs, each DR once', 'Real DRs, each scramble once'] if _hasreal else [])
      + ['Shorter by 1 move, uniform (%)', 'By 2 or more (%)'], rows)
write('g2_means', ['Subset', 'Mean gain (moves)', 'Mean DR-move optimum (moves)', 'Mean any-move optimum (moves)'], rows_m)
_cellrows = sorted([r for r in GT('g2.tsv') if r['pop'] == 'uniform' and ' ' in r['group']], key=lambda r: -float(r['shorter']))
GA['g2_worst'] = [(r['group'], float(r['shorter']) * 100, float(r['by2plus']) * 100) for r in _cellrows[:3]]
GA['g2_cells_over10'] = [r['group'] for r in _cellrows if float(r['shorter']) > 0.10]
# by DR-move optimum, uniform states weighted by exact subset size
_rows = [l.rstrip('\n').split('\t') for l in open(GP + 'big/g2/uni1000.out')]
_n = collections.Counter(r[0] for r in _rows); _W = collections.Counter(); _S = collections.Counter(); _C = collections.Counter(); _G = collections.Counter()
for r in _rows:
    w = SIZE[r[0]] / _n[r[0]]; d = int(r[5]); _W[d] += w; _C[d] += 1; _G[d - int(r[9])] += w
    if int(r[9]) < d: _S[d] += w
_tot = sum(_W.values())
# the share of DR states with each optimum is exact (the first study's table, out/checks/dist48.tsv), not the sample's
_X = collections.Counter()
for r in T('checks/dist48.tsv'): _X[int(r['depth'])] += int(r['states'])
_xtot = sum(_X.values())
write('g2_bylen', ['DR-move optimum', 'Share of DR states (exact)', 'Sampled', 'A shorter finish outside DR exists'],
      [[d, pc(_X[d] / _xtot), f'{_C[d]:,}', pc(_S[d] / _W[d])] for d in sorted(_W) if d >= 8])
GA['g2_le12'] = sum(_S[d] for d in _W if d <= 12) / sum(_W[d] for d in _W if d <= 12)
GA['g2_at'] = {str(d): _S[d] / _W[d] for d in _W}
GA['g2_by1_of_shorter'] = _G[1] / sum(v for k, v in _G.items() if k > 0)
GA['g2_maxgain'] = max(k for k in _G)
_ex = json.load(open(GP + 'out/g2_examples.json'))
GA['g2_ex'] = max(_ex['examples'], key=lambda e: e['dr_optimum'] - e['true_optimum'])
GA['g2_ex_fail'] = _ex['failures']; GA['g2_ex_nsol'] = sum(len(e['solutions']) for e in _ex['examples'])
E['gaps'] = GA
json.dump(E, open(f'{OUT}/report_extra.json', 'w'), indent=1, default=str)
print('tables:', len(os.listdir(D)))
