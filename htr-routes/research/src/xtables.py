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
def cls(c): return '`' + c.replace(' | ht', '') + '`' if c.endswith(' | ht') else '`' + c + '`'
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
    rows.append([g, cls2(a[0]), cls2(a[1]), cls2(a[2]),
                 ' / '.join(pc(a[i]['cumulative']) for i in (0, 1, 2, 4)), pc(s[2]['cum_p1']), pc(lst(g, 'inf')[2]['cumulative'])])
write('checklist_corner', ['Subset', 'Try first', 'Then', 'Then', 'Optimal after 1 / 2 / 3 / 5 classes', 'Within +1, same 3', 'No HTR limit, 3 classes'], rows)
rows = []
for s_ in SUBS:
    a = lst(s_, '2'); s = sm(s_, '2')
    rows.append([s_, cls2(a[0]), cls2(a[1]), cls2(a[2]),
                 ' / '.join(pc(a[i]['cumulative']) for i in (0, 1, 2)), pc(s[2]['cum_p1'])])
write('checklist_edges', ['Subset', 'Try first', 'Then', 'Then', 'Optimal after 1 / 2 / 3', 'Within +1, same 3'], rows)
rows = []
for g in CGROUPS:
    r_ = [g]
    for b in ('0', '1', '2', 'inf'):
        a = lst(g, b); r_.append(f"{pc(a[0]['cumulative'])} / {pc(a[2]['cumulative'])}")
    rows.append(r_)
write('budgets', ['Subset', 'Budget 0 (shortest HTRs only): 1 / 3 classes', 'Budget 1', 'Budget 2', 'No limit'], rows)
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
# ------------------------------------------------------------------ docs 396 / 410 / 171 / 15 / 66
rr = {(r['doc'], r['rule'], r['population_note']): r for r in T('compare_docs_reading_rules.tsv')}
rows = []
# (removed)
    for rule, rn in (('shortest-HTR readings per finish', 'every optimal finish, read only where its HTR is shortest'), ('all readings', 'every optimal finish, every NISS reading'), ('linear only', 'every optimal finish, linear readings only')):
        r = rr[(doc, rule, '0c0 0e tab = states in HTR')]
        rows.append([nm, rn, r['paths'], f"{float(r['mean_abs_diff']) * 100:.1f}", f"{float(r['correlation']):.3f}", pc(r['share_within_0.05'])])
write('docs_rules', ['Sheet', 'How a state counts a path', 'Paths', 'Mean difference (points)', 'Correlation', 'Paths within 5 points'], rows)
E['rr'] = {f'{k[0]}|{k[1]}': {kk: v for kk, v in r.items()} for k, r in rr.items() if k[2] == '0c0 0e tab = states in HTR'}
def mad(f):
    r = T(f); a = np.array([float(x['doc_share']) for x in r]); o = np.array([float(x['our_expected_share_random_tiebreak']) for x in r])
    return len(r), float(abs(a - o).mean()), float(np.corrcoef(a, o)[0, 1])
E['d171_ls'] = mad('compare_doc171_leave_slice.tsv'); E['d171_full'] = mad('compare_doc171.tsv')
tabs = T('compare_docs_396_410_cells.tsv')
rows = []
for s_ in SUBS:
    t4 = [r for r in tabs if r['doc'] == '410' and r['tab'] == s_]
    if not t4: continue
    top = max(t4, key=lambda r: float(r['doc_share']))
    t3 = [r for r in tabs if r['doc'] == '396' and r['tab'] == s_]
    top3 = max(t3, key=lambda r: float(r['doc_share'])) if t3 else None
    rows.append([s_, '`' + top['path'] + '`', pc(top['doc_share']), pc(top['ours_shortest_htr_readings']),
                 ('`' + top3['path'] + '`') if top3 else '', pc(top3['doc_share']) if top3 else '', pc(top3['ours_shortest_htr_readings']) if top3 else ''])
# (removed)
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
write('htr_lengths', ['Subset', 'Shortest NISS HTR', 'Shortest linear, better side', 'Normal side', 'NISS = linear', 'NISS 1 shorter', 'NISS 2+ shorter'], rows)
rows = []
for g in CGROUPS + ['all']:
    r = q3[g]
    rows.append([g if g != 'all' else 'all DRs', pc(r['opt_uses_shortest_niss']), pc(r['opt_htr_plus1']), pc(r['opt_htr_plus2']), pc(r['opt_htr_plus3more']),
                 pc(r['every_opt_htr_ge9']), pc(float(r['every_opt_htr_ge9']) - float(r['niss_htr_ge9'])), f"{float(r['mean_post_htr_longest_in_an_optimal']):.2f}"])
write('htr_vs_opt', ['Subset', 'Shortest HTR', '+1', '+2', '+3 or more', 'Every optimal needs 9+', '… though a sub-9 HTR exists', 'Post-HTR moves'], rows)
bl = [r for r in T('q3_htr_by_length.tsv') if r['group'] == 'all' and float(r['states_share_with_shortest_niss_L']) >= 0.004]
E['bylen_cov'] = sum(float(r['states_share_with_shortest_niss_L']) for r in bl); E['bylen_out'] = [r['L'] for r in T('q3_htr_by_length.tsv') if r['group'] == 'all' and 0 < float(r['states_share_with_shortest_niss_L']) < 0.004]
write('htr_by_length', ['Shortest NISS HTR (L)', 'Share of DRs', 'An optimal uses an L-move HTR'], [[r['L'], pc(r['states_share_with_shortest_niss_L']), pc(r['opt_uses_an_L_move_htr'])] for r in bl])
# ------------------------------------------------------------------ Q4 / Q5
q4 = {r['group']: r for r in T('q4_qt.tsv')}; E['q4'] = q4
write('extra_qt', ['Subset', 'Every optimal uses extra qts', 'Some optimal does', 'Every leave-slice optimal does'],
      [[g if g != 'all' else 'all DRs', pc(q4[g]['every_opt_extra_qt_vs_corners']), pc(q4[g]['some_opt_extra_qt_vs_corners']), pc(q4[g]['ls_every_opt_extra_qt_vs_corners'])] for g in CGROUPS + ['all']])
q5 = {r['group']: r for r in T('q5_states.tsv')}; E['q5'] = q5
write('variation', ['Subset', 'Mean optimal', 'Last move either way', 'One shorter', 'Same', 'Optimal 15+', '15+ either way'],
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
def fr(g, q, R_, t='opt'):
    r = V[(g, q, str(R_))]
    if R_ >= 7: return pc(r['found_' + t])
    return f"{pc(r['found_' + t])} / {float(r['mean_reductions_le_R']):,.0f}"
rows = []
for g in CGROUPS + ['all']:
    rows.append([g if g != 'all' else 'all DRs', fr(g, '1', 3), fr(g, '1', 4), fr(g, '1', 5), fr(g, '1', 6), fr(g, '1', 7), pc(V[(g, '1', '4')]['found_p1']), pc(V[(g, '1', '5')]['found_M12']), fr(g, '2', 3)])
write('bounding', ['Subset', 'R ≤ 3: optimal / reductions', 'R ≤ 4', 'R ≤ 5', 'R ≤ 6', 'R ≤ 7 (optimal only)', 'Within +1, R ≤ 4', '12 or better, R ≤ 5', '2q, R ≤ 3'], rows)
rows = []
for g in CGROUPS:
    rr_ = next((R_ for R_ in range(0, 8) if float(V[(g, '1', str(R_))]['found_opt']) >= 0.8), None)
    bstr = (f"{rr_} ({float(V[(g, '1', str(rr_))]['mean_reductions_le_R']):,.0f})" if rr_ < 7 else "7 (count not reported)") if rr_ is not None else f"more than 7 ({pc(V[(g, '1', '7')]['found_opt'])} at 7)"
    def kfor(b):
        a = lst(g, b); k = next((int(x['step']) for x in a if float(x['cumulative']) >= 0.8), None)
        return str(k) if k else f"more than {len(a)} ({pc(a[-1]['cumulative'])} at {len(a)})"
    rows.append([g, bstr, kfor('2'), kfor('inf')])
write('bounding_vs_checklist', ['Subset', 'Bounding: R for 80% (reductions)', 'Checklist classes for 80%, budget 2', 'Checklist classes, no HTR limit'], rows)
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
    Q9[tg] = {c: agg(tg, c) for c in ('insuff_literal', 'insuff_no_term1', 'insuff_exact_Clin', 'insuff_exact_Cniss', 'mean_R_literal', 'mean_R_no_term1', 'mean_R_exact_Cniss', 'mean_R_needed', 'LB_valid', 'LB_beats_trivial', 'LB_exact_beats_trivial', 'LB_reaches_opt')}
    Q9[tg].update({c: agg(tg, c, 'states') for c in ('mean_Rstate_literal', 'mean_Rstate_no_term1', 'mean_Rstate_exact_Cniss', 'R_empirical_max', 'skip_vs_empirical_no_term1', 'skip_vs_empirical_exact', 'state_insuff_no_term1', 'state_insuff_exact_Cniss')})
    Q9[tg]['cases'] = sum(int(r['cases_state_path']) for r in q9v if r['target'] == tg)
    Q9[tg]['p90'] = agg(tg, 'p90_needed'); Q9[tg]['max'] = max(int(r['max_needed']) for r in q9v if r['target'] == tg)
E['q9'] = Q9
TN = {'opt': 'optimal', 'p1': 'optimal + 1', 'M10': '10 or better', 'M11': '11 or better', 'M12': '12 or better'}
write('fake_summary', ['Target', '(state, path) cases', 'R as written', 'Without term 1', 'Exact model', 'Needed: mean / largest', 'R too short: as written / exact model with linear C'],
      [[TN[tg], f"{Q9[tg]['cases']:,}", f"{Q9[tg]['mean_R_literal']:.1f}", f"{Q9[tg]['mean_R_no_term1']:.1f}", f"{Q9[tg]['mean_R_exact_Cniss']:.1f}",
        f"{Q9[tg]['mean_R_needed']:.1f} / {Q9[tg]['max']}", f"{pc(Q9[tg]['insuff_literal'])} / {pc(Q9[tg]['insuff_exact_Clin'])}"] for tg in TN])
rod = T('q9_rodney_table.tsv')
rows = []
for s_ in SUBS:
    r_ = [s_]
    for M in ('M10:M=10', 'M11:M=11', 'M12:M=12'):
        x = [r for r in rod if r['subset'] == s_ and r['M_minus_opt_or_M'] == M]
        r_.append(f"{x[0]['R_no_term1_worst_case']} / {x[0]['R_exact_worst_case_Cniss']} / {x[0]['R_needed_max']}" if x else '')
    rows.append(r_)
write('rodney_table', ['Subset', 'M = 10: formula / exact / needed', 'M = 11', 'M = 12'], rows)
t5 = T('q9_t11503_examples.tsv')
E['t11503_n'] = len(t5); E['t11503_subsets'] = sorted({r['subset'].split()[0] for r in t5})
E['t11503_cases_opt'] = Q9['opt']['cases']
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
E['top00'] = [float(r['doc_share']) for r in tabs if r['doc'] == '410' and r['tab'] == '0c0 0e' and r['path'] == '0c0 0e'][0]
cd = open(f'{OUT}/checks/check_dist.txt').read()
E['cells473'] = int(_re.search(r'census.csv: (\d+) \(subset, depth\) cells, 0 differ', cd).group(1))
# first budget-2 route against the sheets' top path (edge counts dropped)
import re as _re2
def _c(p): return _re2.sub(r' \de', '', p)
m410 = m396 = tot = 0
for s_ in SUBS:
    t4 = [r for r in tabs if r['doc'] == '410' and r['tab'] == s_]; t3 = [r for r in tabs if r['doc'] == '396' and r['tab'] == s_]
    f0 = lst(s_, '2')[0]; first = {f0['class'].replace(' | ht', ''), f0.get('mirror_alias', '').replace(' | ht', '')} - {''}
    tot += 1
    if t4 and _c(max(t4, key=lambda r: float(r['doc_share']))['path']) in first: m410 += 1
    if t3 and _c(max(t3, key=lambda r: float(r['doc_share']))['path']) in first: m396 += 1
E['top_match'] = [m410, m396, tot]
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
    write('lb_values', ['Subset', '(state, path) cases', 'Lower bound: median / mean', 'Trivial bound: median / mean', 'Mean optimum', 'Bound above trivial', 'Bound reaches the optimum', 'Bound 11 or more'],
          [[g, f"{int(lv[g]['cases']):,}", f"{float(lv[g]['median_lb']):g} / {float(lv[g]['mean_lb']):.2f}", f"{float(lv[g]['median_trivial']):g} / {float(lv[g]['mean_trivial']):.2f}", lv[g]['mean_opt'],
            pc(lv[g]['lb_beats_trivial']), pc(lv[g]['lb_reaches_opt']), pc(lv[g]['lb_ge_11'])] for g in CGROUPS if g in lv])
rows = []
for s_ in ['0c0 0e', '0c0 2e', '0c0 4e', '0c0 6e', '0c0 8e', '4a1 0e', '4a1 2e', '4a1 4e', '4a2 0e', '4a2 2e', '4a2 4e', '4b2 0e', '4b2 2e', '4b2 4e', '2c3 0e', '2c3 2e', '2c3 4e', '2c3 6e', '2c3 8e', '4c3 0e', '4c3 2e', '4c3 4e']:
    rows.append([s_, pc(V[(s_, '1', '4')]['found_opt']), pc(V[(s_, '1', '5')]['found_opt']), pc(lst(s_, '2')[2]['cumulative']), pc(lst(s_, '2')[4]['cumulative'])])
write('bound_vs_routes_edges', ['Subset', 'Bounding, R ≤ 4', 'Bounding, R ≤ 5', 'Checklist, 3 routes', 'Checklist, 5 routes'], rows)
_m = _re.search(r'mirror pairs checked over all 48 subsets: (\d+); identical state sets: (\d+)', open(f'{OUT}/SUMMARY.md').read())
E['alias_pairs'] = [int(_m.group(1)), int(_m.group(2))]
json.dump(E, open(f'{OUT}/report_extra.json', 'w'), indent=1, default=str)
print('tables:', len(os.listdir(D)))
