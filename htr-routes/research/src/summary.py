#!/usr/bin/env python3
"""Writes out/witness_specs.json (the states the witnesses are built from) and out/SUMMARY.md from the tables in out/.
Run witness.py between the two passes: `python3 summary.py specs && python3 witness.py && python3 summary.py`."""
import csv, json, sys, collections, os
import numpy as np
from common import *

def T(name):
    return list(csv.DictReader(open(f'{OUT}/{name}'), delimiter='\t'))
pct = lambda x: f'{100 * float(x):.1f}%'

# ------------------------------------------------------------------------------------------------ witnesses
def find_route_state(sub, key, budget=2, start=0):
    st = load_states(sub); rt = Routes(sub); K = keys()
    want = [i for i, k in enumerate(K) if k == key]
    if not want: return None
    rid = want[0]
    for j in np.nonzero((rt.rid == rid) & (rt.delta == 0))[0]:
        i = rt.state[j]
        if i >= start and rt.htr[j] <= st['htrNiss'][i] + budget and st['nopt'][i] <= 60:
            return f"#{st['c'][i]},{st['e'][i]},{st['s'][i]}", int(st['d'][i])
    return None
def find_state(sub, pred):
    st = load_states(sub)
    for i in range(len(st['d'])):
        if pred(st, i): return f"#{st['c'][i]},{st['e'][i]},{st['s'][i]}", int(st['d'][i])
    return None

def specs():
    S = []
    def add(id_, finding, sub, state_d, kind, route='', maxlen=0, value=0):
        if state_d is None: print('no state for', id_); return
        S.append(dict(id=id_, finding=finding, subset=sub, state=state_d[0], kind=kind, route=route,
                      maxlen=maxlen or state_d[1], value=value))
    k = 'H:4a3 4e > 4b2 2e > (4a1 4e > 0c0 0e) | ht'
    add('W01', '4c3 checklist, first class: 4a3 > 4b2, switch, 4a1 > HTR finds the optimal (here with an HTR within 2 of the shortest)', '4c3 4e', find_route_state('4c3 4e', k), 'follows', k)
    k = 'H:2c4 4e > 2c3 4e > (4b2 2e > 4a1 4e > 0c0 0e) | ht'
    add('W02', '2c4 checklist, first class: one qt to 2c3, switch, then 4b2 > 4a1 > HTR on the other side', '2c4 4e', find_route_state('2c4 4e', k), 'follows', k)
    k = 'H:4b2 4e > 2c3 4e > (4b2 2e > 4a1 4e > 0c0 0e) | ht'
    add('W03', '4b2 4e: regress to 2c3, switch (Yura\'s step 2 / Zagros step 5)', '4b2 4e', find_route_state('4b2 4e', k), 'follows', k)
    st = find_state('4b2 4e', lambda t, i: t['qmin'][i] == 4 and t['nopt'][i] <= 60)
    add('W04', '4b2 4e where no optimal finish uses 2 quarter turns (63.7% of 4b2 4e): the 2qt route 4b2 4e > 4a1 4e > HTR only gives optimal + 1 or worse',
        '4b2 4e', st, 'none_optimal', 'H:4b2 4e > 4a1 4e > 0c0 0e | ht', st[1] + 1 if st else 0)
    st = find_state('2c3 2e', lambda t, i: t['best_any'][i] >= 9 and t['nopt'][i] <= 40)
    add('W05', 'a 2c3 2e whose every optimal finish needs an HTR of 9+ moves in every NISS reading (65% of all DRs are like this; context for C12)',
        '2c3 2e', st, 'min_htr', value=9)
    st = find_state('4b2 2e', lambda t, i: t['dvar'][i] < t['d'][i])
    add('W06', 'Last DR move turned the other way (X -> X R2) gives a finish one move shorter (32.5% of DRs; Yura said 1/6)', '4b2 2e', st, 'variation')
    S.append(dict(id='W07', finding='4a1 4e can need 17 moves (C56 said 15); exact count 32 of 286,654,464 4a1 4e states', subset='4a1 4e',
                  state='#10807,5165,23', kind='optimal', route='', maxlen=17, value=17))
    st = find_state('4c4 0e', lambda t, i: min(t['htrN'][i], t['htrI'][i]) == 10)
    add('W08', '4c4 0e has linear HTRs of 10 moves (C51 said the minimum is 11)', '4c4 0e', st, 'htr_linear', value=10)
    st = find_state('0c3 4e', lambda t, i: min(t['htrN'][i], t['htrI'][i]) == 13) or find_state('4c4 0e', lambda t, i: min(t['htrN'][i], t['htrI'][i]) == 13)
    add('W09', 'The longest shortest linear HTR is 13 moves (Daichi T11594 right, Lewis T4100\'s 12 wrong)', '0c3 4e', st, 'htr_linear', value=13)
    # Q9: a NISS HTR shorter than the subset's shortest linear HTR, used by an optimal finish (breaks C as a NISS bound)
    st = load_states('0c0 2e'); i = 8076
    add('W10', 'FakeMMAP\'s C (shortest HTR in the subset) is not a bound on NISS HTRs: this 0c0 2e state (shortest linear HTR in 0c0 2e: 5) has an optimal 7-move finish whose NISS reading reaches HTR in 4',
        '0c0 2e', (f"#{st['c'][i]},{st['e'][i]},{st['s'][i]}", int(st['d'][i])), 'min_htr_at_most', value=4)
    st = find_state('4b2 0e', lambda t, i: t['nopt'][i] <= 60)
    k = None
    rt = Routes('4b2 0e'); K = keys(); t = load_states('4b2 0e')
    for j in np.nonzero(rt.delta == 0)[0]:
        kk = K[int(rt.rid[j])]
        if kk.startswith('H:4b2 0e > 4a3') or kk.startswith('H:4b2 0e > 4b3'):
            i = rt.state[j]
            if t['nopt'][i] <= 60:
                k = kk; st = (f"#{t['c'][i]},{t['e'][i]},{t['s'][i]}", int(t['d'][i])); break
    add('W11', '4b2 0e whose optimal goes through 4c3 (C04: 4%; ours 6% with a random optimal)', '4b2 0e', st, 'follows', k or '')
    # C13: the shortest-HTR optimal readings all switch after 3+ moves
    st = None
    for r in csv.DictReader(open(f'{R}/out/big/bound2.tsv'), delimiter='\t'):
        if r['subset'] == '2c3 2e' and r['linear_at_best'] == '0' and int(r['minfirst_at_best']) >= 4 and int(r['nopt_canon']) <= 10:
            t = load_states('2c3 2e'); i = int(r['idx']); st = (f"#{t['c'][i]},{t['e'][i]},{t['s'][i]}", int(t['d'][i])); break
    add('W12', 'C13 corrected: a 2c3 2e whose shortest HTR among all readings of all optimal finishes needs a NISS switch after 4+ moves (28% of DRs need a switch after more than 2 moves for their shortest optimal HTR)',
        '2c3 2e', st, 'switch', value=4)
    t = load_states('0c4 0e'); i = 21
    S.append(dict(id='W13', finding='T11503 lower bound as written (alpha_i summed over i with i, i+1 in S) is invalid here: this 0c4 0e has optimal 14 with a finish on 0c4 > 4a3 > 4b2 > 4a1 > HTR, sections 2,1,3,1,3, '
                  'shortest 1q reduction 9, while the bound with R\' = 9 gives M >= 15 (S = {0,2,3} adds alpha_2 = 3); summing the shared section alpha_(i+1) instead gives 14',
                  subset='0c4 0e', state=f"#{t['c'][i]},{t['e'][i]},{t['s'][i]}", kind='optimal', route='', maxlen=14, value=14))
    json.dump(S, open(f'{OUT}/witness_specs.json', 'w'), indent=1)
    print(len(S), 'witness specs')

if __name__ == '__main__' and len(sys.argv) > 1 and sys.argv[1] == 'specs':
    specs(); sys.exit(0)

# ------------------------------------------------------------------------------------------------ SUMMARY.md
L = []
w = L.append
cd = open(f'{OUT}/checks/check_dist.txt').read().strip().split('\n')
cs = open(f'{OUT}/checks/check_sticker.txt').read().strip().split('\n')
W = {x['id']: x for x in json.load(open(f'{OUT}/witness.json'))}
q3 = {r['group']: r for r in T('q3_htr.tsv')}; q4 = {r['group']: r for r in T('q4_qt.tsv')}; q5 = {r['group']: r for r in T('q5_states.tsv')}
cl = {r['id']: r for r in T('claims.tsv')}
bud = T('q2_checklist_budget.tsv')
q8 = {(r['group'], r['target'], r['q']): r for r in T('q8_bounding.tsv')}
q9 = {(r['group'], r['target']): r for r in T('q9_fakemmap.tsv')}
rr = T('compare_docs_reading_rules.tsv')
gr = T('q6_grading.tsv')

def checklist(g, budget, target, n=3):
    rows = [r for r in bud if r['group'] == g and r['level'] == 'C' and r['target'] == target and r['budget'] == budget]
    return rows[:n]
def wref(*ids): return ' (witness ' + ', '.join(ids) + ')'

w('# Which HTR routes to try from a DR: results\n')
w('Fifth case study. Everything below is computed on the DR group <U, D, R2, L2, F2, B2> with the first study\'s exact optimal-finish table '
  '(all 19,508,428,800 DR states). Route questions use **25,000 uniform states per subset x edge count (48 x 25,000 = 1,200,000 states)**, '
  'each solved exactly: every optimal finish and every optimal + 1 finish (all orders of commuting moves), every NISS reading of each '
  '(split after any move, either side first), plus the same for the DR with its last move turned the other way (X R2). Exact over all DR states '
  'where stated. Finishes stay in the DR group (no DR-breaking moves); E slice solved unless "leave slice".\n')
w('Labels: study 1 / Mallard subsets ("4b2 4e"); the corner letter of 3- and 4-qt subsets is the side\'s own (4a3 / 4b3, 4a4 / 4b4). '
  'Where docs disagree: doc 15 and doc 171 call 4b2 "2qt(a)" and 4a2 "2qt(b)"; doc 66 the reverse (its own examples prove it, out/name_map.tsv); Joba\'s 4c5 = 4b5.\n')
w('Route notation: `4b2 > 2c3 > (4b2 > 4a1 > 0c0) | ht` = the corner subset at the start and after each quarter turn until HTR, the part in '
  'brackets done on the other side after a NISS switch, `| ht` = the rest of the finish is half turns (`| qt` = HTR-breaking finish).\n')
w('**One fact governs every route question**: a NISS reading of a finish is also a finish read linearly, so "some optimal follows route X" '
  'cannot tell linear from NISS routes. What NISS changes is the length of the HTR the solver must find. Checklists below therefore carry an '
  '**HTR budget**: a class counts only if its HTR is at most the state\'s shortest NISS HTR + 2 (budget 2); "no limit" rows are the plain class.\n')

w('Samples: route questions 25,000 uniform states per subset x edges (seed 20261112); Q8 shares and reduction counts the first 4,000 of them; '
  '"one optimal at random" numbers (docs 171 comparison, C01-C06, C41, C42) 5,000 other uniform states per subset x edges (htrtools tie / tiels, seed 7); '
  'the docs 396/410 reading-rule comparison 5,000 per subset x edges (htrtools docpaths, seed 11).\n')
w('## Checks (all passed before any number was used)\n')
for l in cd: w(f'- {l}')
w('- Independent sticker model (sticker.py, built from cube geometry only) on ' + cs[0].split(';')[0].replace('states ', '') + ' states: ' +
  '; '.join(l for l in cs[1:] if ':' in l and not l.startswith('failures')) + '; ' + [l for l in cs if l.startswith('failures')][0] + '.')
w('- ' + ' '.join(open(f'{OUT}/checks/check_redcount2.txt').read().split()))
if os.path.exists(f'{OUT}/checks/check_redcount7.txt'): w('- ' + ' '.join(open(f'{OUT}/checks/check_redcount7.txt').read().split()))
w('- Every finish printed in this file and in witness.json is replayed on the sticker model (witness.json, `replayed_ok`).\n')

w('## Q2. The checklist per subset (main deliverable)\n')
w('Greedy order of route classes (corner chain + switch), counting a class only with an HTR at most 2 over the shortest NISS HTR. '
  'At +1 a class counts if any of its finishes within optimal + 1 has such an HTR (it may be shorter than on the optimal finishes). '
  'Ties (classes covering exactly the same states) are broken the same way everywhere: linear first, then the normal-first reading of a mirror pair '
  '(a split of a finish read starting on normal or on inverse is the same pair of moves; such mirror pairs of classes are in out/route_aliases_C.tsv and each '
  'chosen class\'s mirror is in q2_checklist_budget.tsv; as classes they do not cover the same states, since each also collects other finishes: '
  + open(f'{OUT}/checks/check_aliases.txt').read().strip() + '), then the name. '
  'Cumulative share of states where the classes so far find an optimal finish; last column: the same three classes at optimal + 1. '
  'Edge counts pooled by their exact sizes; 25,000 states per subset x edges. Per subset x edges, all budgets (0, 1, 2, none) and up to 8 classes: '
  'out/q2_checklist_budget.tsv. Without a budget the first one or two classes reach 90-99% (out/q2_checklist.tsv, out/q2_best.tsv: greedy is within 0.5 points of the best possible '
  'set of the same size (k = 1-4, best set searched among the top 25-40 classes) in 2,192 of 2,208 cases, at most 1.8 points off).\n')
w('| subset | 1st class | 2nd | 3rd | after 1 / 2 / 3 | +1 after 3 |')
w('|---|---|---|---|---|---|')
for g in CGROUPS:
    a = checklist(g, '2', 'opt'); b = checklist(g, '2', 'p1')
    if not a: continue
    cls_ = [r['class'].replace(' | ht', '') if r['class'].endswith('| ht') else r['class'] for r in a] + ['', '', '']
    w(f'| {g} | `{cls_[0]}` | `{cls_[1]}` | `{cls_[2]}` | {" / ".join(pct(r["cumulative"]) for r in a)} | {pct(b[-1]["cumulative"]) if b else ""} |')
w('\nPer subset x edges (budget 2, optimal; first class and cumulative after 1/2/3):\n')
w('| subset | first class | 1 / 2 / 3 | +1 after 3 |')
w('|---|---|---|---|')
for s in SUBS:
    a = checklist(s, '2', 'opt'); b = checklist(s, '2', 'p1')
    if a:
        w(f'| {s} | `{a[0]["class"].replace(" | ht", "")}` | {" / ".join(pct(r["cumulative"]) for r in a)} | {pct(b[-1]["cumulative"]) if b else ""} |')
w('')
w('Cheap vs marginal classes: with budget 0 (only shortest HTRs) the best single class finds the optimal in 13-48% of states per corner subset, '
  'with budget 2 in 29-84%, with no limit in 51-98% (out/q2_checklist_budget.tsv). After the third class each further class adds at most 8 points, '
  'usually under 3: these pay only at the margin. The cost proxy (mean shortest HTR of the class where it works) is in out/q1_routes.tsv and out/q2_checklist.tsv. Striking findings:')
a4c3 = checklist('4c3', '2', 'opt'); a2c4 = checklist('2c4', '2', 'opt'); a4b2 = checklist('4b2', '2', 'opt')
w(f'- NEW: on 4c3 the single class `4a3 > 4b2 > (4a1 > 0c0)` (one qt to 4b2 from the a side, switch) finds the optimal in {pct(a4c3[0]["cumulative"])} of states with a near-shortest HTR; '
  f'three classes {pct(a4c3[2]["cumulative"])}{wref("W01")}. KNOWN in spirit: Daichi\'s sheet "always switch after 4b2 4e"; doc 396 lists this as the top 4c3 path.')
w(f'- NEW: on 2c4, `2c4 > 2c3 > (4b2 > 4a1 > 0c0)` alone gives {pct(a2c4[0]["cumulative"])}, three classes {pct(a2c4[2]["cumulative"])}{wref("W02")}. KNOWN as advice (Daichi D18331).')
w(f'- NEW: on 4b2 the linear 2qt route comes first ({pct(a4b2[0]["cumulative"])}) but three classes only reach {pct(a4b2[2]["cumulative"])}: 4b2 needs the 4qt regressions through 2c3{wref("W03")}.\n')

w('## Q1. How often each route class works\n')
w('Per subset x edges, share of states where a class finds an optimal / within +1 / with the last DR move inverted: out/q1_routes.tsv (levels C corner chain, '
  'H with edges, Q quarter-turn shape, F the full-finish chain of docs 396/410). Cell-by-cell with docs 396/410: out/compare_docs_396_410_cells.tsv.')
r410 = {(x['doc'], x['rule'], x['population_note']): x for x in rr}
best410 = r410[('410', 'shortest-HTR readings per finish', '0c0 0e tab = states in HTR')]
all410 = r410[('410', 'all readings', '0c0 0e tab = states in HTR')]
lin410 = r410[('410', 'linear only', '0c0 0e tab = states in HTR')]
b396 = r410[('396', 'shortest-HTR readings per finish', '0c0 0e tab = states in HTR')]
w(f'- KNOWN + NEW (method found): docs 396/410 are reproduced when each optimal finish is read only with its shortest-HTR NISS readings: doc 410 (7,007 paths) '
  f'mean |difference| {float(best410["mean_abs_diff"]):.3f}, correlation {float(best410["correlation"]):.3f}, {pct(best410["share_within_0.05"])} of paths within 5 points; '
  f'every reading: {float(all410["mean_abs_diff"]):.3f}; linear only: {float(lin410["mean_abs_diff"]):.3f}. Doc 396 (768 paths, sub-13 states, ~1000 per tab) {float(b396["mean_abs_diff"]):.3f}. '
  'So 396/410 count, per state, every distinct shortest-NISS-HTR path of every optimal finish (D19661). Their 0c0 0e tab holds HTR states only '
  '(96% "no quarter turn"), while the 0c0 0e subset is half HTR, half U D\' times HTR.')
def mad(f):
    r = T(f); d = np.array([float(x['doc_share']) for x in r]); o = np.array([float(x['our_expected_share_random_tiebreak']) for x in r])
    return len(r), abs(d - o).mean(), np.corrcoef(d, o)[0, 1]
n171, m171, c171 = mad('compare_doc171_leave_slice.tsv'); _, m171f, c171f = mad('compare_doc171.tsv')
w(f'- KNOWN + CORRECTS: doc 171 (allcases) is reproduced by one leave-slice optimal per state with a random tie-break ({n171} paths: mean |difference| {m171:.4f}, '
  f'correlation {c171:.3f}; full finish {m171f:.4f} / {c171f:.3f}), with its tie-break slightly favouring the fewest-qt path (~5 points). Its "2qt(b)" is 4a2: mrauo\'s "only 1/3 of 2q 4b2e use 2qt" (D9450) read the 4a2 2e row; Zagros\'s "a and b flipped" (D9451) is right for doc 66 vs doc 171.')
w('- Doc 15 (1000 states per subset): solution means within 0.06 of exact; its "Linear HTR" is the normal side only (ours 6.156 vs 6.213 for 4b2 2e), its NISS HTR mean matches ours to 0.05 (out/compare_doc15.tsv).\n')

w('## Q3. Shortest HTR vs optimal\n')
a = q3['all']
w(f'All DRs (25,000 per subset, weighted): shortest NISS HTR {float(a["mean_htr_niss"]):.2f}, shortest linear (better side) {float(a["mean_htr_linear_best_side"]):.2f}, normal side {float(a["mean_htr_normal"]):.2f}. '
  f'Some optimal uses a shortest NISS HTR in {pct(a["opt_uses_shortest_niss"])} of states; the best HTR an optimal uses is +1 in {pct(a["opt_htr_plus1"])}, +2 in {pct(a["opt_htr_plus2"])}, +3 or more in {pct(a["opt_htr_plus3more"])}; '
  f'post-HTR part of that optimal {float(a["mean_post_htr_longest_in_an_optimal"]):.2f} moves. Per subset: out/q3_htr.tsv, by HTR length out/q3_htr_by_length.tsv.')
w(f'- NEW (T624 answered): linear and NISS shortest HTRs are equal in {pct(a["niss_eq_linear"])} of DRs, NISS 1 shorter in {pct(a["niss_shorter_by_1"])}, 2+ shorter in {pct(a["niss_shorter_by_2plus"])}; '
  f'0c3: 2+ shorter in {pct(q3["0c3"]["niss_shorter_by_2plus"])}, 0c4 {pct(q3["0c4"]["niss_shorter_by_2plus"])}.')
w(f'- NEW (C12 stays open): in {pct(a["every_opt_htr_ge9"])} of all DRs every optimal finish needs an HTR of 9+ moves; given a shortest HTR of L moves, an optimal uses an L-move HTR in about a third of states for every L from 6 to 9{wref("W05")}. '
  '"9-move HTRs rarely give an optimal" is about each 9-move HTR a solver writes, which this does not measure.')
w(f'- NEW: two thirds of DRs ({pct(1 - float(a["opt_uses_shortest_niss"]))}) have no optimal finish through any shortest HTR (T554, T4167, T10409).')
w(f'- CORRECTS "DR > slice ~ DR > solved - 1" (C23): optimal minus optimal leave-slice is {cl["C23"]["evidence"].split(": ")[1].split(" moves")[0]} moves on average; ~0.7 only for 0c0 / 4a1. KNOWN from doc 15\'s own No-E column.\n')

w('## Q4. Extra quarter turns\n')
w('Share of states where every optimal uses more qts than the corner subset\'s count / where some optimal does (full finish), and every leave-slice optimal (doc 66\'s reading):\n')
w('| subset | every optimal | some optimal | every leave-slice optimal |')
w('|---|---|---|---|')
for g in CGROUPS:
    r = q4[g]; w(f'| {g} | {pct(r["every_opt_extra_qt_vs_corners"])} | {pct(r["some_opt_extra_qt_vs_corners"])} | {pct(r["ls_every_opt_extra_qt_vs_corners"])} |')
w(f'\n- KNOWN: doc 66 "% with extra qts" = every leave-slice optimal uses extra qts; all 47 comparable rows agree within sampling error (out/compare_doc66.tsv). Its 0qt 0c0e row is HTR states only.')
w(f'- NEW: the two readings explain the quoted numbers: rodney\'s 57% (2qt subsets, T539) is the "every optimal" reading ({cl["C01"]["evidence"].split(";")[0].split(": ")[-1]}), Lichi\'s >60% for 4b2 4e (nissy\'s first optimal) matches a random optimal ({cl["C02"]["evidence"].split(" uses 4+ qt ")[1].split(" ")[0]}).')
w(f'- AGREES (Kai T5573): 2c3 2e, some optimal has <2 half turns before its first qt on one of the two sides in {pct(q4["2c3 2e"]["ht_before_first_qt_lt2_either_side"])} (85% claimed); normal side alone {pct(q4["2c3 2e"]["ht_before_first_qt_lt2_normal"])}.')
w('- Doc 9: its corner-QT shares (17.1/27.5/32.9/22.5%) match neither the fewest quarter turns to solve corners (exact 17.6/28.1/35.2/19.1%) nor that count among move-optimal corner solutions; its "+0/+2" extra-qt shares sit between our fewest-qt and most-qt optimal readings (out/compare_doc9.tsv).\n')

w('## Q5. Inverting the last DR move\n')
w(f'- CORRECTS Yura (T4606, 1/6): X R2 is one move shorter in {pct(q5["all"]["share_variation_shorter"])} of DRs (exact over all DR states 32.47%), never more; mean gain {float(q5["all"]["mean_gain"]):.3f} move{wref("W06")}. A qt break costs {float(q5["all"]["qt_break_minus_opt"]):.2f} moves on average (trangium ~0.5).')
w('- With the variation allowed, route-class shares rise by about the same amount for every class (out/q1_routes.tsv columns share_vopt / share_vp1, checklists target vopt / vp1 in out/q2_checklist.tsv); it adds no new class to any checklist.\n')

w('## Q6. Hand checklists graded\n')
w('Cumulative share of states where the checklist finds an optimal (budget 2 HTRs; no-limit in brackets), out/q6_grading.tsv:\n')
for name in ['Zagros 4b2 order (D15884)', 'Yura 4b2 4e order (D6409-D6416)', 'rogo/Adri 4b2 4e order (D6422-D6424)', 'Lewis 4a2 0e/2e list (T6743)', 'Jay/rodney 2c3 0e checks (T328-T344)', 'Fanti 4b2 4e split (D10034), cumulative']:
    rows = [r for r in gr if r['checklist'] == name]
    w(f'- {name}: ' + '; '.join(f'{r["step_description"]}: {pct(r["cumulative_opt_htr_budget2"])} ({pct(r["cumulative_opt"])})' for r in rows))
dch = [r for r in gr if r['checklist'].startswith('Daichi')]
w('- Daichi\'s cheat sheet (D18340): ' + ', '.join(f'{r["subsets"]} {pct(r["cumulative_opt_htr_budget2"])}' for r in dch) + '.')
w('- KNOWN: Zagros\'s "optimal in 15 minutes like 80% of the time" fits: his eight steps reach 71% optimal / 91% within +1 with near-shortest HTRs. NEW: Yura\'s 4b2 4e order (regress to 2c3) finds about twice as many optimals as rogo/Adri\'s (trigger, then 4a1 switch).\n')

w('## Q7. Claims\n')
cnt = collections.Counter(r['verdict'] for r in cl.values())
w(f'{len(cl)} claims from the reading notes (out/claims.tsv): ' + ', '.join(f'{k} {v}' for k, v in cnt.most_common()) + '. Corrections with a witness: C15 (W06), C56 (W07), C51 (W08), C53 (W09). The SPEC\'s quoted numbers:\n')
for cid in ['C01', 'C02', 'C03', 'C04', 'C05', 'C06', 'C07', 'C08', 'C09', 'C10', 'C12', 'C14', 'C15', 'C26', 'C27', 'C48']:
    r = cl[cid]; w(f'- {cid} {r["author"]} ({r["number_claimed"]}): **{r["verdict"]}**. {r["evidence"]}')
w('')

w('## Q8. DR bounding as a route\n')
w('The method as stated: some reduction to 1q (reach 4a1 4e; or to 2q) of at most R moves, on normal, on inverse or split by NISS, followed by the '
  'optimal finish of the reduced state (any number of quarter turns), gives an optimal finish (or one within +1, or of at most M = 10, 11, 12). Exact search '
  'on reductions (htrtools bound4: along each side, length + optimum never decreases, so the search is cut at the target), first 4,000 states of every '
  'subset x edges (the states of the main pass). Reductions counted as a solver writes them: pairs (moves on normal, moves on inverse), each empty or ending in a '
  'quarter turn, counted exactly with coset tables for r <= 6 (checked against brute force on 4,800 states for r <= 5 and on 40 states of 0c0 0e/2e/4e/6e for r <= 7; '
  'reduction counts for R = 7 are not reported: the brute-force check of them was stopped after 6 hours). The R <= 7 column gives the share found only. '
  'out/q8_bounding_stated.tsv has every subset x edges, R = 0-7, every target, with standard errors.\n')
V = {(r['group'], r['q'], r['R']): r for r in T('q8_bounding_stated.tsv')}
VW = {(r['group'], r['q'], r['R']): r for r in T('q8_bounding_v2.tsv')}
w('| subset | R<=3: found / reductions | R<=4 | R<=5 | R<=6 | R<=7 | +1 at R<=4 | <=12 at R<=5 | 2q R<=3 |')
w('|---|---|---|---|---|---|---|---|---|')
def fr(g, q, R_, t='opt'):
    r = V[(g, q, str(R_))]; return f"{pct(r['found_' + t])} / {float(r['mean_reductions_le_R']):.0f}"
for g in CGROUPS:
    w(f"| {g} | {fr(g, '1', 3)} | {fr(g, '1', 4)} | {fr(g, '1', 5)} | {fr(g, '1', 6)} | {pct(V[(g, '1', '7')]['found_opt'])} | {pct(V[(g, '1', '4')]['found_p1'])} | {pct(V[(g, '1', '5')]['found_M12'])} | {fr(g, '2', 3)} |")
w('\nStandard errors: shares at most 0.8 points per corner subset (4,000-20,000 states). A stricter reading, the reduction followed by a finish with exactly one '
  'quarter turn (what JTuu\'s T5744 sim measured, out/q8_bounding_v2.tsv), finds less: 2c3 at R <= 4 / 5: '
  f"{pct(VW[('2c3', '1', '4')]['found_opt'])} / {pct(VW[('2c3', '1', '5')]['found_opt'])} against {pct(V[('2c3', '1', '4')]['found_opt'])} / {pct(V[('2c3', '1', '5')]['found_opt'])} as stated; "
  f"4b2 {pct(VW[('4b2', '1', '4')]['found_opt'])} / {pct(VW[('4b2', '1', '5')]['found_opt'])} against {pct(V[('4b2', '1', '4')]['found_opt'])} / {pct(V[('4b2', '1', '5')]['found_opt'])}.\n")
w('Bounding against the route checklist of Q2: smallest R reaching 80% optimal and the reductions it takes, against the classes the budget-2 checklist needs for 80%:\n')
w('| subset | bounding: R for 80% (reductions) | checklist: classes for 80% (budget 2) | checklist, no HTR limit |')
w('|---|---|---|---|')
k80 = {}
for g in CGROUPS:
    rr = next((R_ for R_ in range(0, 8) if float(V[(g, '1', str(R_))]['found_opt']) >= 0.8), None)
    bstr = (f"{rr} ({float(V[(g, '1', str(rr))]['mean_reductions_le_R']):.0f})" if rr is not None and rr <= 6 else (f"7 (count not reported)" if rr == 7 else f"> 7 ({pct(V[(g, '1', '7')]['found_opt'])} at 7)"))
    def kfor(bg):
        rows = [r for r in bud if r['group'] == g and r['level'] == 'C' and r['target'] == 'opt' and r['budget'] == bg]
        k = next((int(r['step']) for r in rows if float(r['cumulative']) >= 0.8), None)
        return str(k) if k else f"> {len(rows)} ({pct(rows[-1]['cumulative'])})"
    k80[g] = (rr, kfor('2'))
    w(f'| {g} | {bstr} | {kfor("2")} | {kfor("inf")} |')
v4 = V[('2c3', '1', '4')]; v5 = V[('2c3', '1', '5')]
w(f"\n- CORRECTS beef beans / Levi (\"all reductions <= 4 find optimal about 75-80% on 2c3\", D9086): {pct(v4['found_opt'])} (+- {100 * float(v4['se_opt']):.1f}) at <= 4 moves "
  f"({float(v4['mean_reductions_le_R']):.0f} reductions), {pct(v5['found_opt'])} at <= 5 ({float(v5['mean_reductions_le_R']):.0f} reductions); "
  f"within +1 at <= 4: {pct(v4['found_p1'])}.")
w(f'- JTuu\'s T5744 sim (linear HTRs <= 7 + 1q reductions <= 4: 64.65%) uses the stricter one-quarter-turn finish; on that reading: {cl["C26"]["evidence"]}')
w(f"- NEW: reducing to 2q needs far shorter reductions: 2q reductions of <= 3 moves reach an optimal in {pct(V[('all', '2', '3')]['found_opt'])} of all DRs "
  f"vs {pct(V[('all', '1', '3')]['found_opt'])} for 1q.")
good = [g for g in CGROUPS if k80[g][0] is not None and k80[g][0] <= 5]
w(f"- NEW: bounding reaches 80% optimal with reductions of <= 5 moves on {', '.join(good) or 'no subset'}; elsewhere it needs 6 (thousands to tens of thousands of reductions) or 7, or does not get there by 7. "
  "The budget-2 route checklist reaches 80% with a handful of classes on most subsets (table). A class and a reduction are not the same amount of work; "
  "the comparison is only in kind.\n")

w("## Q9. FakeMMAP's reduction-length bound (T11501-T11504), with the section bounds\n")
q9v = T('q9_v2.tsv')
def agg(tg, col, wcol='cases_state_path'):
    rs = [r for r in q9v if r['target'] == tg]
    W_ = sum(int(r[wcol]) * SIZE[r['subset']] for r in rs)
    return sum(float(r[col]) * int(r[wcol]) * SIZE[r['subset']] for r in rs if r[col] != 'nan') / W_
w('alpha_i computed per corner path (corners only, over every permutation following the path; 4a3 > 4b2 > 4a1 gives alpha = 0,3,1,0, FakeMMAP\'s example; '
  'out/q9_alpha.tsv). Sum of alpha over i with i and i+1 in S, as written. Per (state, path of a finish of length <= M) the reduction that finish needs '
  'against R. 25,000 states per subset; targets optimal, +1 and fixed M = 10, 11, 12 (out/q9_v2.tsv, counterexamples out/q9_v2_counterexamples.tsv).\n')
for tg in ('opt', 'p1'):
    w(f"- target {tg}: insufficient: literal {pct(agg(tg, 'insuff_literal'))}, without term 1 {pct(agg(tg, 'insuff_no_term1'))}, "
      f"exact model with C = shortest linear HTR of the subset {pct(agg(tg, 'insuff_exact_Clin'))}, with C = the state's shortest NISS HTR {pct(agg(tg, 'insuff_exact_Cniss'))}. "
      f"Mean R: literal {agg(tg, 'mean_R_literal'):.2f}, without term 1 {agg(tg, 'mean_R_no_term1'):.2f}, exact {agg(tg, 'mean_R_exact_Cniss'):.2f}; needed {agg(tg, 'mean_R_needed'):.2f}.")
w(f"- Not knowing the path (R = max over the subset's paths, with the state's own A and B): mean R without term 1 {agg('opt', 'mean_Rstate_no_term1', 'states'):.2f}, exact {agg('opt', 'mean_Rstate_exact_Cniss', 'states'):.2f}; "
  f"insufficient {pct(agg('opt', 'state_insuff_no_term1', 'states'))} / {pct(agg('opt', 'state_insuff_exact_Cniss', 'states'))}. "
  f"Pruning: the longest reduction any optimal needed is {agg('opt', 'R_empirical_max', 'states'):.1f} moves on average over subsets (25,000 states each), so R from the formula "
  f"({agg('opt', 'mean_Rstate_no_term1', 'states'):.1f}) asks for longer reductions than the empirical maximum and prunes nothing against it; the exact R "
  f"({agg('opt', 'mean_Rstate_exact_Cniss', 'states'):.1f}) is about the empirical maximum. Against the reductions a solver can actually write (R <= 6-7), "
  f"neither prunes: every extra move multiplies the reductions by about 7.5 (out/q8_bounding_v2.tsv).")
w(f"- CORRECTS T11503 as written: with alpha summed over i with i and i+1 in S, the lower bound is wrong in 923 of 1,914,809 (state, path) cases (0.05%; 0c4, 4c4, 4b2, 4c3; out/q9_t11503_examples.tsv; witness W13). "
  "Summing the section shared by windows i and i+1 (alpha_(i+1)) instead makes every lower bound valid and keeps R sufficient (0 violations): that is probably what was meant.")
w(f"- T11503 lower bounds as written (after every reduction shorter than the one the optimal needs failed): valid in {pct(agg('opt', 'LB_valid'))}; better than the trivial M >= A + alpha_N, B + alpha_0 in "
  f"{pct(agg('opt', 'LB_beats_trivial'))} (exact model {pct(agg('opt', 'LB_exact_beats_trivial'))}); reach the optimum itself in {pct(agg('opt', 'LB_reaches_opt'))}.")
w("- C as \"the shortest HTR in the subset\" must be the shortest NISS HTR, not linear: a linear C makes the model wrong (W10: 0c0 2e, optimal 7 with a 4-move NISS HTR, below the subset's linear minimum 5).")
w('\nrodneykinney\'s table (T11512), "reduce to 1q in at most R moves", per subset x edges and target M, worst case over the subset\'s paths with A = B = the subset\'s shortest linear HTR (nothing read off the DR), formula without term 1 '
  '(C = shortest linear HTR, as FakeMMAP defined it) / exact model (C = shortest NISS HTR seen in the subset); then the mean with the DR\'s own A, B; and what was actually needed (90th percentile / max). '
  'Full table: out/q9_rodney_table.tsv. M = 12 rows:\n')
w('| subset | R (formula) | R (exact) | mean R, own A/B (formula / exact) | needed p90 / max |')
w('|---|---|---|---|---|')
for r in T('q9_rodney_table.tsv'):
    if r['M_minus_opt_or_M'] == 'M12:M=12':
        w(f"| {r['subset']} | {r['R_no_term1_worst_case']} | {r['R_exact_worst_case_Cniss']} | {r['R_no_term1_mean_with_own_A_B']} / {r['R_exact_mean_with_own_A_B']} | {r['R_needed_p90']} / {r['R_needed_max']} |")
w('')
w('## Half turns between quarter turns (C11, C13)\n')
c = {r['group']: r for r in T('c11_c13.tsv')}
for cid in ('C11', 'C13'):
    w(f'- {cid}: **{cl[cid]["verdict"]}**. {cl[cid]["evidence"]}')
w('')
w('## Witnesses\n')
for k, x in W.items():
    w(f'- {k} ({x["subset"]}): {x["finding"]}. Scramble `{x["scramble"]}`, optimal {x["optimal"]}: `{x["optimal_finish"]}`'
      + (f'; route reading: `{x["finish"]}` ({x["first_side"]} first, normal `{x["normal_moves"]}`, inverse `{x["inverse_moves"]}`, HTR {x["htr_length"]})' if x.get('finish') else '')
      + f'; replayed {"ok" if x["replayed_ok"] else "FAILED"}.')
w('')
w('## Run times and memory\n')
w('See research/README.md.\n')
open(f'{OUT}/SUMMARY.md', 'w').write('\n'.join(L) + '\n')
print('SUMMARY.md written,', len(L), 'lines')
