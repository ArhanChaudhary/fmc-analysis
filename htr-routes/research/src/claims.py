#!/usr/bin/env python3
"""Question 7: verdicts on the checkable claims of the reading notes (out/claims_raw.tsv, 125 rows extracted from
kb/reread/htr_theory_*.md, htr_discussion_*.md and htr_docs.md Part B, quotes checked against the export).

Each verdict is computed from the study's outputs; rows that need something the study does not measure are marked
"not checked" with the reason.  Verdicts: AGREES, CORRECTS (the claim is off; what is true), PARTLY (one reading
agrees, another does not), ANSWERED (a question, now with a number), NOT CHECKED.
Output: out/claims.tsv (id, msg_ids, author, claim (number), verdict, evidence)."""
import csv, collections, re, itertools
import numpy as np
from common import *

ST = {s: load_states(s) for s in SUBS}
def grp(g):
    if g == 'all': return SUBS
    if g in SUBS: return [g]
    return [s for s in SUBS if CORNER(s) == g or s in g.split('+')] if '+' not in g else [s for s in SUBS if CORNER(s) in g.split('+')]
def share(g, f):
    subs = grp(g); num = den = 0.0
    for s in subs:
        t = ST[s]; w = SIZE[s] / len(t['d'])
        v = f(t); num += w * v.sum(); den += w * len(v)
    return num / den
def exact_mean(s):
    tot = n = 0
    for r in csv.DictReader(open(f'{R}/out/checks/dist48.tsv'), delimiter='\t'):
        if r['subset'] == s or (s in CGROUPS and CORNER(r['subset']) == s):
            tot += int(r['depth']) * int(r['states']); n += int(r['states'])
    return tot / n
def exact_dist(s):
    h = collections.Counter()
    for r in csv.DictReader(open(f'{R}/out/checks/dist48.tsv'), delimiter='\t'):
        if r['subset'] == s or (s in CGROUPS and CORNER(r['subset']) == s): h[int(r['depth'])] += int(r['states'])
    return h
H48 = collections.defaultdict(collections.Counter)
for r in csv.DictReader(open(f'{R}/out/checks/htr48.tsv'), delimiter='\t'):
    H48[r['subset']][int(r['htr_len'])] += int(r['cosets'])
TIE = collections.defaultdict(dict); TIELS = collections.defaultdict(dict)
for f, D in (('tie', TIE), ('tiels', TIELS)):
    for r in csv.DictReader(open(f'{R}/out/big/{f}.tsv'), delimiter='\t'):
        D[r['subset']][r['chain'][2:]] = (float(r['expected_share']), float(r['share_some']), float(r['share_all']))
def tie_share(D, g, pred):
    num = den = 0.0
    for s in grp(g):
        w = SIZE[s]
        num += w * sum(v[0] for c, v in D[s].items() if pred(c.split(' > '))); den += w
    return num / den
Q1 = collections.defaultdict(dict)
for r in csv.DictReader(open(f'{OUT}/q1_routes.tsv'), delimiter='\t'):
    Q1[(r['group'], r['level'])][r['class']] = r
def q1(g, lv, pred, col='share_opt'):
    """share of states where SOME class satisfying pred works: not additive, so only usable for single classes"""
    return {c: float(r[col]) for c, r in Q1[(g, lv)].items() if pred(c)}
GR = collections.defaultdict(list)
for r in csv.DictReader(open(f'{OUT}/q6_grading.tsv'), delimiter='\t'):
    GR[r['checklist']].append(r)
Q8 = {(r['group'], r['target'], r['q']): r for r in csv.DictReader(open(f'{OUT}/q8_bounding.tsv'), delimiter='\t')}
Q8V = {(r['group'], r['q'], r['R']): r for r in csv.DictReader(open(f'{OUT}/q8_bounding_stated.tsv'), delimiter='\t')}
qts = lambda chain: len(chain) - 1
pct = lambda x: f'{100 * x:.1f}%'

V = {}
def put(cid, verdict, ev): V[cid] = (verdict, ev)

# ------------------------------------------------------------------------------------------- qt claims
two = '4a2+4b2'
put('C01', 'PARTLY', f"2qt corner cases (4a2+4b2, all edges, weighted by size): every optimal uses 4+ qt {pct(share(two, lambda t: t['qmin'] > 2))}; "
    f"some optimal does {pct(share(two, lambda t: t['qmax'] > 2))}; one optimal picked at random {pct(tie_share(TIE, two, lambda c: qts(c) > 2))} "
    f"(leave-slice {pct(tie_share(TIELS, two, lambda c: qts(c) > 2))}). 57% fits only the 'every optimal' reading. 25,000 states per subset.")
put('C02', 'CORRECTS' if tie_share(TIE, '4b2 4e', lambda c: qts(c) > 2) < 0.6 else 'AGREES',
    f"4b2 4e: one optimal at random uses 4+ qt {pct(tie_share(TIE, '4b2 4e', lambda c: qts(c) > 2))} (leave-slice {pct(tie_share(TIELS, '4b2 4e', lambda c: qts(c) > 2))}); "
    f"every optimal {pct(share('4b2 4e', lambda t: t['qmin'] > 2))}; some optimal {pct(share('4b2 4e', lambda t: t['qmax'] > 2))}.")
put('C03', 'AGREES', f"4c3: every leave-slice optimal uses 5+ qt {pct(share('4c3', lambda t: t['ls_qmin'] > 3))}; full finish {pct(share('4c3', lambda t: t['qmin'] > 3))}; "
    f"by edges 0e/2e/4e (leave slice) {', '.join(pct(share(s, lambda t: t['ls_qmin'] > 3)) for s in ('4c3 0e', '4c3 2e', '4c3 4e'))}.")
put('C04', 'PARTLY',
    f"4b2 0e: one leave-slice optimal at random passes 4c3: {pct(tie_share(TIELS, '4b2 0e', lambda c: any(x[:3] in ('4a3', '4b3') for x in c)))} "
    f"(full finish {pct(tie_share(TIE, '4b2 0e', lambda c: any(x[:3] in ('4a3', '4b3') for x in c)))}); doc 171's tie-break favours fewer qts (see its comparison), which lowers 4qt paths like this one.")
put('C05', 'PARTLY', f"Depends on the reading. 4a1 4e: every optimal uses 5+ qt: leave slice {pct(share('4a1 4e', lambda t: t['ls_qmin'] >= 5))}, full finish {pct(share('4a1 4e', lambda t: t['qmin'] >= 5))}; "
    f"one optimal at random has 5+ qt {pct(tie_share(TIELS, '4a1 4e', lambda c: qts(c) >= 5))} (leave slice). beef's 3-4% fits 'every leave-slice optimal'; Fanti's 6.10% is the sum of the allcases 5qt rows; full finishes give 10%.")
a = tie_share(TIELS, '4b2 4e', lambda c: qts(c) == 2); b = tie_share(TIELS, '4b2 4e', lambda c: qts(c) == 4 and c[1].startswith('2c3'))
c_ = tie_share(TIELS, '4b2 4e', lambda c: qts(c) == 4 and c[2].startswith('0c0'))
put('C06', 'AGREES', f"4b2 4e, one leave-slice optimal at random: 2qt {pct(a)}, 4qt via 2c3 {pct(b)}, 4qt via 4a1 > 0c0 {pct(c_)} (Fanti: 40/45/8 from doc 171); "
    f"full finish {pct(tie_share(TIE, '4b2 4e', lambda c: qts(c) == 2))} / {pct(tie_share(TIE, '4b2 4e', lambda c: qts(c) == 4 and c[1].startswith('2c3')))} / "
    f"{pct(tie_share(TIE, '4b2 4e', lambda c: qts(c) == 4 and c[2].startswith('0c0')))}.")
# C07 fake HTR: corner arrangements with 0 bad corners
import sticker
nb0 = [a_ for a_ in sticker.QTC if all(sticker.TETRAD[sticker.CPOS[i]] == sticker.TETRAD[sticker.CPOS[a_[i]]] for i in range(8))]
real = sum(1 for a_ in nb0 if sticker.QTC[a_] == 0)
put('C07', 'AGREES', f"Corner permutations with no bad corner (DR on all three axes): {len(nb0)}; of these {real} are 0c0 (HTR corners or U D' of them), "
    f"so {len(nb0) - real}/{len(nb0)} = {(len(nb0) - real) / len(nb0):.4f} are fake (0c3, 0c4). Exact.")
mins = {s: min(H48[s]) for s in SUBS}
put('C08', 'AGREES' if sum(v <= 5 for v in mins.values()) == 8 else 'CORRECTS',
    f"Shortest linear (normal-side) HTR per subset, exact over HTR cosets: {sum(v <= 4 for v in mins.values())} subsets <= 4, "
    f"{sum(v <= 5 for v in mins.values())} <= 5, {sum(v <= 6 for v in mins.values())} <= 6. <=5: {', '.join(s for s, v in mins.items() if v <= 5)}.")
put('C09', 'AGREES', f"Corner subsets with at most 3 qt: 0c0 4a1 4a2 4b2 0c3 2c3 4c3 (7). Mean optimal 0c3 {exact_mean('0c3'):.3f} vs 2c4 {exact_mean('2c4'):.3f} (exact): 0c3 is worse.")
# C10: a single qt (no setup) on normal or inverse reduces 3qt -> 2qt / 4qt -> 2qt (corners, exact over the arrangements)
def inv_arr(a_):
    r = [0] * 8
    for i, x in enumerate(a_): r[x] = i
    return tuple(r)
cnt = collections.Counter()
for a_, q in sticker.QTC.items():
    if q not in (3, 4): continue
    hit = any(sticker.QTC[sticker.cmul(x, sticker.CMOV[m])] == 2 for x in (a_, inv_arr(a_)) for m in ("U", "U'", "D", "D'"))
    cnt[(q, hit)] += 1
f3 = cnt[(3, True)] / (cnt[(3, True)] + cnt[(3, False)]); f4 = cnt[(4, True)] / (cnt[(4, True)] + cnt[(4, False)])
put('C10', 'PARTLY', f"Corners, exact over the 40320 permutations: a bare quarter turn (no setup) on normal or on inverse takes a 3qt case to 2qt in {pct(f3)} "
    f"(rodney: 2/3, agrees). A 4qt case cannot reach 2qt with one quarter turn ({pct(f4)}); rodney's 1/6 for 4qt counted something else (his corner_h_sections column on the optimal corner solution, T507).")
C11T = {r['group']: r for r in csv.DictReader(open(f'{OUT}/c11_c13.tsv'), delimiter='\t')}
def c11(g):
    r = C11T[g]
    return (f"{g}: some optimal ends with an R U2 R'-shape trigger (last two qts on one face, opposite directions, one half turn between) {pct(float(r['some_opt_ends_RU2Rp']))}, "
            f"at either end {pct(float(r['either_end_RU2Rp']))}, a random optimal {pct(float(r['random_opt_ends_RU2Rp']))}; any qt-half turn-qt ending {pct(float(r['some_opt_ends_qt_ht_qt']))} "
            f"(random optimal {pct(float(r['random_opt_ends_qt_ht_qt']))})")
put('C11', 'PARTLY', c11('2c4') + '; ' + c11('2c3') + f". Either end with qt-half turn-qt: 2c4 {pct(float(C11T['2c4']['either_end_qt_ht_qt']))}, 2c3 {pct(float(C11T['2c3']['either_end_qt_ht_qt']))}. beef beans' 94.9% (2c4) / 72.5% (2c3) "
    "sit near the loose readings (any qt-half turn-qt), far above the strict R U2 R' shape (41% / 35% some optimal, 14% / 12% a random optimal); 25,000 states per subset.")
put('C13', 'AGREES' if float(C11T['all']['budget2_needs_switch_after_gt2']) < 0.1 else 'CORRECTS',
    f"All DRs: the shortest-HTR optimal readings all need a switch after more than 2 moves in {pct(float(C11T['all']['shortest_htr_needs_switch_after_gt2']))} of states "
    f"(after more than 3: {pct(float(C11T['all']['shortest_htr_needs_switch_after_gt3']))}); with HTRs up to 2 over the shortest allowed: "
    f"{pct(float(C11T['all']['budget2_needs_switch_after_gt2']))} / {pct(float(C11T['all']['budget2_needs_switch_after_gt3']))}. Per subset in c11_c13.tsv.")
e9 = share('all', lambda t: t['best_any'] >= 9)
put('C12', 'OPEN', f"The claim is about each 9-move HTR a solver writes, which is not measured here. What is measured: all DR states: every optimal finish needs an HTR of 9+ moves (its shortest HTR over all NISS readings) in {pct(e9)} of states; "
    f"2c3 2e {pct(share('2c3 2e', lambda t: t['best_any'] >= 9))}, 4b2 4e {pct(share('4b2 4e', lambda t: t['best_any'] >= 9))}, 4c3 {pct(share('4c3', lambda t: t['best_any'] >= 9))}, "
    f"2c4 {pct(share('2c4', lambda t: t['best_any'] >= 9))}. Among states whose shortest NISS HTR is 9, an optimal uses a 9-move HTR in "
    f"{[r for r in csv.DictReader(open(f'{OUT}/q3_htr_by_length.tsv'), delimiter=chr(9)) if r['group'] == 'all' and r['L'] == '9'][0]['opt_uses_an_L_move_htr']} "
    f"(about the same as for 6-8 moves). So 9-move HTRs are often the only way to an optimal, but the share of written 9-move HTRs that extend to an optimal is not computed.")
put('C14', 'AGREES', f"2c3 2e: some optimal has <2 half turns before its first quarter turn, read on normal or inverse: {pct(share('2c3 2e', lambda t: np.minimum(t['ht_first_n'], t['ht_first_i']) < 2))}; "
    f"normal side only {pct(share('2c3 2e', lambda t: t['ht_first_n'] < 2))}; 3+ needed {pct(share('2c3 2e', lambda t: np.minimum(t['ht_first_n'], t['ht_first_i']) >= 3))}.")
put('C15', 'CORRECTS', f"Turning the DR's last move the other way (X -> X*R2): shorter by one move in {pct(share('all', lambda t: t['dvar'] < t['d']))} of states "
    f"(exact over all DR states from the first study's h8 table: 32.47%), never by more; mean gain {share('all', lambda t: t['d'] - np.minimum(t['d'], t['dvar'])):.3f} move. "
    f"Neither 1/6 move nor 1/6 of DRs: about 1/3.")
put('C16', 'PARTLY', f"A qt break costs 1 + min(opt(X), opt(X*R2)) - opt(X) = {share('all', lambda t: 1 + np.minimum(t['d'], t['dvar']) - t['d']):.3f} moves on average (trangium: ~0.5).")
h8 = collections.Counter()
for r in csv.DictReader(open('/data/fmc/judging-a-dr/research/out/hand/h8_last_move.csv')):
    if r['depth'] == '18': h8[(r['subset'], r['depth_after_side_half_turn'])] += int(r['count'])
subs18 = sorted({k[0] for k in h8})
put('C17', 'AGREES' if all(k[1] == '17' for k in h8) else 'CORRECTS',
    f"Exact (first study's h8 table): the 18-move states lie in {', '.join(subs18)}; after one side half turn their depths are {sorted({k[1] for k in h8})}.")
put('C18', 'ANSWERED', f"Every optimal finish uses an HTR longer than the shortest NISS HTR in {pct(share('all', lambda t: t['best_any'] > t['htrNiss']))} of states "
    f"(+1 {pct(share('all', lambda t: t['best_any'] - t['htrNiss'] == 1))}, +2 {pct(share('all', lambda t: t['best_any'] - t['htrNiss'] == 2))}, +3 or more {pct(share('all', lambda t: t['best_any'] - t['htrNiss'] >= 3))}).")
put('C19', 'ANSWERED', f"Some optimal finish uses a shortest NISS HTR in {pct(share('all', lambda t: t['best_any'] == t['htrNiss']))} of states (4qt subsets 2c4 {pct(share('2c4', lambda t: t['best_any'] == t['htrNiss']))}, "
    f"5qt 4b5 {pct(share('4b5', lambda t: t['best_any'] == t['htrNiss']))}, 0c3 {pct(share('0c3', lambda t: t['best_any'] == t['htrNiss']))}).")
put('C20', 'ANSWERED', f"Some optimal starts with a shortest linear HTR of its side in {pct(share('all', lambda t: (t['best_lin_n'] == t['htrN']) | (t['best_lin_i'] == t['htrI'])))}; "
    f"through a shortest NISS HTR {pct(share('all', lambda t: t['best_any'] == t['htrNiss']))}.")
put('C21', 'AGREES', f"0c0 2e: no optimal uses a shortest NISS HTR in {pct(share('0c0 2e', lambda t: t['best_any'] > t['htrNiss']))}; no optimal uses a shortest linear HTR of its side in "
    f"{pct(share('0c0 2e', lambda t: (t['best_lin_n'] > t['htrN']) & (t['best_lin_i'] > t['htrI'])))}.")
put('C22', 'ANSWERED', f"All DR states: shortest NISS HTR = shortest linear (better side) in {pct(share('all', lambda t: np.minimum(t['htrN'], t['htrI']) == t['htrNiss']))}, "
    f"1 shorter {pct(share('all', lambda t: np.minimum(t['htrN'], t['htrI']) - t['htrNiss'] == 1))}, 2+ shorter {pct(share('all', lambda t: np.minimum(t['htrN'], t['htrI']) - t['htrNiss'] >= 2))}; "
    f"normal and inverse linear lengths equal in {pct(share('all', lambda t: t['htrN'] == t['htrI']))}, differ by 2+ in {pct(share('all', lambda t: abs(t['htrN'] - t['htrI']) >= 2))}. Per subset in q3_htr.tsv.")
put('C23', 'CORRECTS', f"Optimal finish minus optimal leave-slice, mean over all DR states: {share('all', lambda t: t['d'] - t['lsd']):.3f} moves (0c0 {share('0c0', lambda t: t['d'] - t['lsd']):.2f}, "
    f"4a1 {share('4a1', lambda t: t['d'] - t['lsd']):.2f}, 2c4 {share('2c4', lambda t: t['d'] - t['lsd']):.2f}, 4c4 {share('4c4', lambda t: t['d'] - t['lsd']):.2f}); ~0.9-1 holds only for 0qt subsets. "
    f"Doc 15's own 'No E Difference' column shows the same.")
put('C24', 'ANSWERED', f"Longest post-HTR part among optimal readings (opt - shortest HTR used), mean: {share('all', lambda t: t['d'] - t['best_any']):.2f} moves; per subset in q3_htr.tsv.")
put('C25', 'AGREES', f"Mean shortest HTR used by an optimal / post-HTR: 0c0 {share('0c0', lambda t: t['best_any']):.2f}/{share('0c0', lambda t: t['d'] - t['best_any']):.2f}, "
    f"4b2 {share('4b2', lambda t: t['best_any']):.2f}/{share('4b2', lambda t: t['d'] - t['best_any']):.2f}, 2c4 {share('2c4', lambda t: t['best_any']):.2f}/{share('2c4', lambda t: t['d'] - t['best_any']):.2f}, "
    f"4b5 {share('4b5', lambda t: t['best_any']):.2f}/{share('4b5', lambda t: t['d'] - t['best_any']):.2f}: more qts, longer HTR, shorter post-HTR.")
# JTuu T5744 (2c3 2e): checking linear HTRs up to L moves plus bounding with 1q reductions up to B moves; share of
# states where that finds an optimal (some optimal has a linear reading with HTR <= L and a half-turn post-HTR, or a
# 1q reduction of <= B moves)
def jtuu(L, Bm):
    rt = Routes('2c3 2e'); K = keys()
    lin = np.zeros(rt.n, bool)
    for j in np.nonzero((rt.delta == 0) & (rt.htr <= L))[0]:
        k = K[int(rt.rid[j])]
        if k.startswith('H:') and '(' not in k and k.endswith('| ht'): lin[rt.state[j]] = True
    red = np.full(rt.n, 99)
    i = 0
    for r in csv.DictReader(open(f'{R}/out/big/bound.tsv'), delimiter='\t'):
        if r['subset'] != '2c3 2e': continue
        v = [int(c.split(':')[2]) for c in r['cells'].split(';') if c and c.split(':')[0] == '0' and int(c.split(':')[1]) >= 1]
        red[int(r['idx'])] = min(v) if v else 99
    return (lin | (red <= Bm)).mean(), lin.mean(), (red <= Bm).mean()
j1 = jtuu(7, 4); j2 = jtuu(8, 5)
put('C26', 'OPEN', f"Same definitions as JTuu (linear HTR within L moves, or a reduction of at most B moves to 4a1 4e followed by one quarter turn), uniform 2c3 2e, 25,000 states: an optimal is found by linear HTRs <= 7 or 1q reductions <= 4 in {pct(j1[0])} (linear alone {pct(j1[1])}, bounding alone {pct(j1[2])}); "
    f"<= 8 / <= 5: {pct(j2[0])} ({pct(j2[1])}, {pct(j2[2])}). JTuu's sim: 64.65% / 86.05%, 6-9 points more; his states were probably drawn differently (e.g. with the last DR move inverted).")
def grade_line(name):
    rows = GR.get(name, [])
    return '; '.join(f"step {r['step']} {pct(float(r['cumulative_opt']))} (+1: {pct(float(r['cumulative_p1']))})" for r in rows)
def grade_line2(name):
    return '; '.join(f"step {r['step']} {pct(float(r['cumulative_opt_htr_budget2']))} (+1: {pct(float(r['cumulative_p1_htr_budget2']))})" for r in GR.get(name, []))
put('C27', 'AGREES', f"Zagros's 4b2 order on 4b2 (0/2/4e, weighted), only HTRs at most 2 moves over the shortest NISS HTR: {grade_line2('Zagros 4b2 order (D15884)')}; "
    f"with no HTR limit: {grade_line('Zagros 4b2 order (D15884)')}. ~71% optimal (91% within +1) with realistic HTRs, close to his 80%.")
put('C28', 'ANSWERED', f"Lewis's 4a2 0e/2e list, HTR budget 2: {grade_line2('Lewis 4a2 0e/2e list (T6743)')}; no limit: {grade_line('Lewis 4a2 0e/2e list (T6743)')}.")
put('C32', 'ANSWERED', f"2c3 0e, one qt to 4b2 4e then switch (any prefix): {grade_line('Jay/rodney 2c3 0e checks (T328-T344)')}. Prefix restrictions (Jay's 11, rodney's 9/4/2) are not graded separately.")
put('C33', 'NOT CHECKED', 'Prefix sets need the exact setup moves before the first quarter turn; see C32 for the route class itself.')
put('C34', 'ANSWERED', 'Checking every reduction to 1q of <= 4 / <= 5 moves (both sides, NISS), then the optimal finish of the reduced state, reaches an optimal in: ' +
    ', '.join(f"{g} {pct(float(Q8V[(g, '1', '4')]['found_opt']))}/{pct(float(Q8V[(g, '1', '5')]['found_opt']))}" for g in ('0c0', '4a1', '4a2', '4b2', '2c3', '4c3', '2c4')) +
    ' (4,000 states per subset x edges).')
put('C36', 'ANSWERED', f"Yura's 4b2 4e order (HTR budget 2): {grade_line2('Yura 4b2 4e order (D6409-D6416)')}; no limit: {grade_line('Yura 4b2 4e order (D6409-D6416)')}; every optimal of 4b2 4e uses 4qt in {pct(share('4b2 4e', lambda t: t['qmin'] > 2))}.")
put('C37', 'ANSWERED', f"rogo/Adri order (trigger, then reduce to 4a1 and switch), HTR budget 2: {grade_line2('rogo/Adri 4b2 4e order (D6422-D6424)')}; no limit {grade_line('rogo/Adri 4b2 4e order (D6422-D6424)')}. Yura's regress-to-2c3 order finds about twice as many optimals.")
put('C39', 'AGREES', f"4b2 4e: every optimal uses 4qt {pct(share('4b2 4e', lambda t: t['qmin'] > 2))} (leave slice {pct(share('4b2 4e', lambda t: t['ls_qmin'] > 2))}): about half.")
put('C40', 'AGREES', f"4b2 4e: every optimal 4qt {pct(share('4b2 4e', lambda t: t['qmin'] > 2))}.")
put('C41', 'AGREES', f"4b2 2e: one leave-slice optimal at random is 2qt {pct(tie_share(TIELS, '4b2 2e', lambda c: qts(c) == 2))} (doc 171 row 0.595 under its own labels); "
    f"4a2 2e: {pct(tie_share(TIELS, '4a2 2e', lambda c: qts(c) == 2))}, so mrauo's 1/3 is the 4a2 2e row (doc 171's 2qt(b) = 4a2). Every optimal 4qt in 4b2 2e: {pct(share('4b2 2e', lambda t: t['qmin'] > 2))}.")
put('C42', 'AGREES', f"4a2 0e: one leave-slice optimal at random is 2qt {pct(tie_share(TIELS, '4a2 0e', lambda c: qts(c) == 2))} (beef: 2%); every optimal 4+qt {pct(share('4a2 0e', lambda t: t['qmin'] > 2))}.")
put('C44', 'AGREES', f"4b5 4e: every leave-slice optimal uses 7qt {pct(share('4b5 4e', lambda t: t['ls_qmin'] > 5))} (the 1.33% was called a bug, but it is the every-optimal reading).")
put('C45', 'AGREES', 'Every optimal 5qt: ' + ', '.join(f"{s} {pct(share(s, lambda t: t['qmin'] > 3))}" for s in ('2c3 0e', '2c3 2e', '2c3 4e', '2c3 6e', '2c3 8e', '4c3', '0c3')) + '.')
def budget_shares(g, lv, budget):
    K = keys(); acc = collections.Counter(); W = 0.0
    for s_ in grp(g):
        rt = Routes(s_); niss = ST[s_]['htrNiss']; w = SIZE[s_] / rt.n; W += SIZE[s_]
        m = (rt.delta == 0) & (rt.htr <= niss[rt.state] + budget)
        seen = set()
        for st_, rid in zip(rt.state[m], rt.rid[m]):
            k = K[int(rid)]
            if k[0] != 'H': continue
            seen.add((int(st_), level_of(k, lv)))
        for _, c in seen: acc[c] += w
    return {c: v / W for c, v in acc.items()}
q48 = budget_shares('2c4', 'Q', 2)
put('C48', 'AGREES' if q48.get('2+(2) | ht', 0) < 0.2 else 'CORRECTS', '2c4: share of states where an optimal is reached through each route shape using an HTR at most 2 moves over the shortest NISS HTR: ' +
    ', '.join(f'{c} {pct(v)}' for c, v in sorted(q48.items(), key=lambda x: -x[1])[:7]) + '. (Without an HTR limit every shape that a finish can be read in ties, ~94%.)')
put('C49', 'AGREES' if [mins[f'2c4 {e}e'] for e in (0, 2, 4, 6, 8)] == [7, 7, 7, 8, 9] else 'CORRECTS', f"Shortest linear HTR 2c4 0/2/4/6/8e (exact): {[mins[f'2c4 {e}e'] for e in (0, 2, 4, 6, 8)]}.")
put('C51', 'AGREES' if mins['4c4 0e'] == 11 and mins['2c5 6e'] == 9 else 'CORRECTS', f"Exact: 4c4 0e {mins['4c4 0e']}, 2c5 6e {mins['2c5 6e']}; subsets with minimum >= 11: {[s for s, v in mins.items() if v >= 11]}.")
nm = lambda s: int(ST[s]['htrNiss'].min())
put('C52', 'PARTLY', f"Shortest linear HTR (exact) / shortest NISS HTR (minimum over 25,000 states): 2c4 0e {mins['2c4 0e']}/{nm('2c4 0e')}, 0c4 0e {mins['0c4 0e']}/{nm('0c4 0e')}, 0c3 0e {mins['0c3 0e']}/{nm('0c3 0e')}.")
maxlin = max(max(H48[s]) for s in SUBS)
put('C53', 'ANSWERED', f"Longest shortest linear HTR on one side (exact over cosets): {maxlin} ({[s for s in SUBS if max(H48[s]) == maxlin]}); "
    f"longest over states of min(normal, inverse) in the sample {max(int(np.minimum(ST[s]['htrN'], ST[s]['htrI']).max()) for s in SUBS)}, longest NISS {max(int(ST[s]['htrNiss'].max()) for s in SUBS)} (sample).")
put('C56', 'AGREES' if max(exact_dist('4a1 4e')) == 15 else 'CORRECTS', f"4a1 4e longest optimal (exact): {max(exact_dist('4a1 4e'))}.")
put('C59', 'AGREES', f"Mean optimal (exact) 2c4 {exact_mean('2c4'):.3f}, 0c3 {exact_mean('0c3'):.3f}, 0c4 {exact_mean('0c4'):.3f}.")
put('C61', 'AGREES', f"2c3: 3+ half turns needed before the first qt on both sides {pct(share('2c3', lambda t: np.minimum(t['ht_first_n'], t['ht_first_i']) >= 3))}.")
dch = [r for k, rs in GR.items() if k.startswith('Daichi') for r in rs]
put('C67', 'ANSWERED', "Daichi's cheat sheet routes reach an optimal (HTR budget 2 / no limit) in: " + ', '.join(f"{r['subsets']} {pct(float(r['cumulative_opt_htr_budget2']))}/{pct(float(r['cumulative_opt']))}" for r in dch) + '. "Linear" options (2c5, 4b5) admit every finish, so those rows are only meaningful with the budget.')
put('C77', 'AGREES', 'Mean optimal (exact): ' + ', '.join(f'{s} {exact_mean(s):.3f}' for s in ('2c4 0e', '2c4 2e', '2c4 4e', '2c4 6e', '2c4 8e', '2c3 0e', '2c3 8e')) + '.')
put('C80', 'AGREES', f"Mean optimal 2c4 2e {exact_mean('2c4 2e'):.3f}, 2c4 4e {exact_mean('2c4 4e'):.3f}, 2c3 4e {exact_mean('2c3 4e'):.3f}: difference < 1.")
put('C81', 'AGREES', f"Mean optimal 2c4 {exact_mean('2c4'):.3f}, 4b2 2e {exact_mean('4b2 2e'):.3f}.")
put('C83', 'ANSWERED', '2c4, optimal >= 15 without / with the last DR move inverted: ' + ', '.join(f"{s} {pct(share(s, lambda t: t['d'] >= 15))}/{pct(share(s, lambda t: np.minimum(t['d'], t['dvar']) >= 15))}" for s in ('2c4 0e', '2c4 2e', '2c4 4e', '2c4 6e', '2c4 8e')) + '.')
v4, v5 = Q8V[('2c3', '1', '4')], Q8V[('2c3', '1', '5')]
put('C90', 'CORRECTS', f"2c3 (all edges, 4,000 states per subset x edges): checking every 1q reduction of <= 4 moves (both sides, NISS; {float(v4['mean_reductions_le_R']):.0f} +- {float(v4['se_reductions']):.0f} reductions) "
    f"reaches an optimal in {pct(float(v4['found_opt']))} (+- {100 * float(v4['se_opt']):.1f}), <= 5 moves ({float(v5['mean_reductions_le_R']):.0f} reductions) {pct(float(v5['found_opt']))}; "
    f"a finish within +1 at <= 4: {pct(float(v4['found_p1']))}. Reduction followed by the optimal finish of the reduced state, exact search. Not 75-80%.")
dd = exact_dist('4b2 0e'); n_ = sum(dd.values())
put('C106', 'AGREES', f"4b2 0e: optimal 12-14 in {pct(sum(dd[k] for k in (12, 13, 14)) / n_)} (exact); shortest linear HTR (exact, normal side) {min(H48['4b2 0e'])}-{max(H48['4b2 0e'])}.")
put('C111', 'AGREES', 'Exact subset sizes: see out/checks/dist48.tsv (= Joba doc 580 and the first study, 473 cells equal).')
put('C112', 'AGREES', 'HTR states: 663,552, half-turn-only optimal mean 10.13432557 = DougCube exactly (out/checks/check_dist.txt); with DR moves allowed 9.887.')
put('C114', 'ANSWERED', '3qt subsets, every optimal needs 5qt: ' + ', '.join(f"{s} {pct(share(s, lambda t: t['qmin'] > 3))}" for s in ('2c3', '4c3', '0c3')) + '.')
put('C102', 'AGREES', f"4a1 2e: every optimal 3+ qt {pct(share('4a1 2e', lambda t: t['qmin'] >= 3))}.")
put('C101', 'ANSWERED', f"4a1 0e/2e every optimal 3+ qt {pct(share('4a1 0e', lambda t: t['qmin'] >= 3))}/{pct(share('4a1 2e', lambda t: t['qmin'] >= 3))}; 4a1 4e some optimal 3qt or more {pct(share('4a1 4e', lambda t: t['qmax'] >= 3))}.")
put('C103', 'AGREES', 'Some optimal uses only the corner minimum of qts: ' + ', '.join(f"{g} {pct(share(g, lambda t: t['qmin'] == t['ccqt']))}" for g in CGROUPS) + '.')
put('C110', 'NOT CHECKED', 'Outside DR-group finishes.'); put('C113', 'NOT CHECKED', 'DR-breaking finishes are outside this study.')

def main():
    rows = list(csv.DictReader(open(f'{OUT}/claims_raw.tsv'), delimiter='\t'))
    with open(f'{OUT}/claims.tsv', 'w') as f:
        f.write('id\tmsg_ids\tauthor\tclaim\tnumber_claimed\tverdict\tevidence\n')
        for r in rows:
            v, ev = V.get(r['id'], ('NOT CHECKED', 'Qualitative, a procedure without a number, or needs data the study does not keep (see what_to_compute in claims_raw.tsv).'))
            q = r['quote'][:300].replace('\t', ' ')
            f.write(f"{r['id']}\t{r['msg_ids']}\t{r['author']}\t{q}\t{r['number_claimed']}\t{v}\t{ev}\n")
    print(collections.Counter(v for v, _ in V.values()), len(rows))

if __name__ == '__main__':
    main()
