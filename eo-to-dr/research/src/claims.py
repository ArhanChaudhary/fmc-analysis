#!/usr/bin/env python3
"""D: register claims and questions on these themes that the computations settle.  Writes out/claims.tsv with the
entry, what was said, our number with its conditions, and a verdict; a witness id where the verdict is a
correction or a counterexample (out/witness.json)."""
import csv, json, os, collections
from fractions import Fraction
from math import comb

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, '..', 'out')
J = lambda n: json.load(open(os.path.join(OUT, n)))
def rd(name):
    return list(csv.DictReader((l for l in open(os.path.join(OUT, name)) if not l.startswith('#')), delimiter='\t'))
A = J('a50k_stats.json'); B = J('b_stats.json'); C = J('c_stats.json')
wit = J('witness.json')
dl = J('default_listing.json'); be = J('both_eo.json')
def wid(question, word):
    for w in wit:
        if w['question'] == question and word in w['finding']:
            return w['id']
    return ''
a1 = {r['what']: r for r in rd('a50k_a1.tsv')}
c6 = {r['case']: r for r in rd('c6_by_case.tsv')}
c7 = {r['option']: r for r in rd('c7_typical.tsv')}
ax = rd('eo_axis.tsv')
byb = {int(r['bad']): r for r in rd('b5_by_bad.tsv')}
a2 = rd('a50k_a2.tsv')
b4 = rd('a50k_b4.tsv')
n = A['n']
pct = lambda x, d=2: f'{100 * float(x):.{d}f}%'
rows = []
def claim(entry, said, ours, verdict, cond, w=''):
    rows.append({'entry': entry, 'said': said, 'ours': ours, 'verdict': verdict, 'conditions': cond, 'witness': w})

# ---- S-DR
ex = a1['fixed axis, exact (all 2,217,093,120 cosets)']
claim('S-DR-15', 'Louis: 6.2% of axes are within 8 turns of DR without NISS (43% within 9)',
      f"{pct(ex['p_le8'])} within 8, {pct(ex['p_le9'])} within 9", 'confirmed (one axis, linear, as Louis restated)',
      'exact over all 2,217,093,120 cosets of one DR axis (all_dr table)')
b6 = a1['best of 6 (3 axes x normal/inverse, linear)']; bn = a1['best of 3 axes, normal (linear)']; bx = a1['NISS (moves on both sides), best of 3 axes']
claim('S-DR-7', 'Daichi: a sub-10 DR seems to exist on most, maybe all, scrambles',
      f"sub-10 DR: {pct(bn['p_le9'])} on normal (3 axes), {pct(b6['p_le9'])} with normal or inverse, {pct(bx['p_le9'])} with NISS; the rest are 10 (none longer with NISS in the sample)",
      'most: yes; all: no', f'{n} random-state scrambles; any turns; findability not considered', wid('A1', 'no sub-10'))
sfw = next(w for w in wit if 'superflip' in w['finding'])
_ol = open(os.path.join(OUT, 'optimal_no_sub10.tsv')).read().splitlines()
_or = list(csv.DictReader(_ol[1:], delimiter='\t'))
opt_note = (_ol[0].strip('# ') + ': optimal ' + ', '.join(r['optimal_length'] for r in _or) + ' moves, so not all 20-movers (Daichi: no)' +
            ' [e.g. sample scramble ' + _or[0]['sample_index'] + ': ' + _or[0]['scramble'] + ', optimal ' + _or[0]['optimal_solution'] + ']')
claim('S-DR-8', 'wen: sub-10 DR is impossible for the superflip; is it the worst case? Daichi: are all states without sub-10 DR 20-movers?',
      sfw['finding'] + f"; in the sample {pct(1 - float(b6['p_le9']), 3)} of random scrambles have no sub-10 DR on 6 tries and {pct(1 - float(bx['p_le9']), 3)} none even with NISS",
      'superflip: confirmed; worst case: no, it is not alone, and ' + opt_note,
      'exact for the superflip; sample for the rest; optimal solutions by nissy solve optimal', wid('A1', 'superflip'))
claim('S-DR-13', 'bpaul: DR skip about 1 in 2^11·3^7·12!/8!', '1 in 2,217,093,120 on a given axis (= 2^11·3^7·495); about 1 in 739 million on some axis',
      "corrected (a hedged aside): 12!/8! should be 12!/(8!·4!) = 495", 'exact (coset count); the three axes overlap only on a much smaller set')
claim('S-DR-6', 'wen: is the distribution of scramble-to-DR lengths known?',
      f"fixed axis mean {ex['mean']} (exact); best of 3 normal {bn['mean']}, best of 6 {b6['mean']}, NISS {bx['mean']}; P(<=8) {pct(bn['p_le8'])} / {pct(b6['p_le8'])} / {pct(bx['p_le8'])}",
      'answered (out/a50k_a1.tsv)', f'{n} random-state scrambles; fixed axis exact')
# A2
def a2row(kind, k):
    return next(r for r in a2 if r['eo_kind'].startswith(kind) and r['k'] == str(k))
r5 = a2row('normal EOs', 5); r4 = a2row('normal EOs', 4); r6 = a2row('normal EOs', 6)
claim('S-DR-46', 'Zagros: what share of good DRs have an EO under 6 moves? JTuu: very low (for optimal solutions), guessing low for DRs too',
      f"the optimal normal DR starts with an EO of <=5 turns on {pct(r5['p_estar_le_k'])} of scrambles (<=4: {pct(r4['p_estar_le_k'])}, <=6: {pct(r6['p_estar_le_k'])}); mean EO inside the optimal DR {A['estar_mean']} turns",
      f"answered per scramble: on about {round(float(r5['p_estar_le_k']) * 100)}% of scrambles some optimal DR starts with an EO of <=5 (JTuu guessed 'low'); the share among all DRs, which Zagros asked, is not measured", f'{n} scrambles; optimal DR over 3 axes on normal; shortest EO prefix over all optimal DRs', wid('A2', 'starts with an EO'))
claim('S-DR-47', 'Zagros: stats on scramble -> DR without an EO step; are the best DRs findable, or random 8-move DRs from 7-move EOs?',
      f"best through an EO of <=5 (normal): mean {r5['mean_best_given_eo']} against the optimal {bn['mean']}; equal on {pct(r5['p_equals_optimal'])}, 1 worse {pct(r5['p_loss1'])}, 2 worse {pct(r5['p_loss2'])}, 3+ {pct(r5['p_loss3plus'])}",
      'answered (out/a50k_a2.tsv): the optimal DR usually needs a 6+ turn EO', f'{n} scrambles; DR keeps the EO', wid('A2', 'the best DR through'))
rx = lambda N: next(r for r in a2 if r['eo_kind'].startswith('normal EOs') and r['k'] == '5')
claim('S-DR-26', 'Michael Smith sub7: chance of an N-move DR that begins with an EO of at most 5 moves (not analysed, said JTuu)',
      'see out/a50k_a2.tsv (mean_best_given_eo) and out/a50k_a3.tsv (p_none for N = 9..12)', 'answered', f'{n} scrambles')
g = A['a3_gains']
def yields(N):
    y = g[f'normal_N{N}']
    return 25 * y['drs_per_eo_le4'], 200 * y['drs_per_5move_eo']
parts = []
for N in (9, 10, 11, 12):
    a, b = yields(N)
    parts.append(f"total <={N}: 25 four-movers ~{a:.1f} DRs, 200 five-movers ~{b:.1f}")
win = [N for N in (9, 10, 11, 12) if yields(N)[1] > yields(N)[0]]
claim('S-DR-261', 'Somebodyidk: 25 four-move EOs or 200 five-move EOs?',
      '; '.join(parts) + " (expected (EO, DR axis) pairs, normal side, per-EO yields over all EOs of that length on 50,000 scrambles; '<=4' yield used for the four-movers)",
      ('answered: the 25 four-movers give more short DRs up to a total of ' + str(min(win) - 1) + ', the 200 five-movers more from ' + str(min(win)) + ' on') if win and min(win) > 9 else ('answered: the 200 five-movers give more DRs' if win else 'answered: the 25 four-movers give more DRs'),
      'per-EO yields averaged over 50,000 scrambles; EOs on one scramble are correlated, so this is an expectation, not a per-scramble guarantee; EOs counted as nissy -a (counted the server\'s way both piles about double, same answer)')
# ---- EO -> DR
allc = c6['all']
plain = c7['one DR axis, EO kept, normal (the known table)']
claim('EO-DR-50', 'KrzychXyz: the longest EO->DR is 10, about 3% of cases; zakimoshi: so only 6.3% of cases are sub-7',
      f"10 is the longest; 3114 of 1,082,565 cases = 0.29%; sub-7 (<=6): {pct(plain['p_le6'])}; with the last EO turn invertible {pct(c7['one DR axis, EO kept, last EO turn inverted if better']['p_le6'])}, with the other DR axis too {pct(c7['two DR axes x last turn inverted, EO kept, normal']['p_le6'])}",
      'corrected: the 10s are 0.29% (not 3%); zakimoshi\'s 6.3% sub-7 was a question (5.92%)', 'exact over the 1,082,565 EO-solved cosets, one DR axis, EO kept')
k44 = c6['4c4e']
claim('EO-DR-79', "Cale's sheet (quoted by Lichi Fang): DR-4e4c reaches DR in <=6 1 in 5.2, or 1 in 3.6 when the last move may be switched",
      f"exact: <=6 on {pct(k44['plain_p_le6'])} (1 in {1 / float(k44['plain_p_le6']):.2f}); with the last EO turn inverted if better {pct(k44['switch_last_p_le6'])} (1 in {1 / float(k44['switch_last_p_le6']):.2f})",
      'confirmed', 'exact over all 4c4e cosets (EO kept; the case is the one before switching)', wid('C6c', '4c4e'))
p = float(k44['switch_last_p_le6'])
tail = sum(comb(27, i) * p ** i * (1 - p) ** (27 - i) for i in range(4))
claim('EO-DR-80', 'Lichi Fang: only 3 of 27 DR-4e4c (first one nissy found per scramble) reach DR in <=6, switching allowed',
      f'with the exact {pct(p)} the chance of 3 or fewer in 27 independent 4c4e is {tail:.4f}', 'open: p = %.3f under the exact rate for EO-solved states (%.3f at Cale\'s 19226/70560 for switching the RZP\'s last move, which is what Lichi Fang switched; a report with questions, not a claim the sheet is wrong), while Cale\'s 25 (same method) fit it; both are first-found RZPs from nissy online, which need not be uniform EO-solved states' % (tail, sum(comb(27, i) * (19226 / 70560) ** i * (1 - 19226 / 70560) ** (27 - i) for i in range(4))),
      'binomial with the exact rate; does not model how nissy picks the first RZP')
claim('EO-DR-22', "Mike (Cale's sheet): 4c4e comes up in 1 in 15.3 EOs", f"{k44['cosets']} of 1,082,565 cosets = 1 in {k44['one_in']}",
      'confirmed', 'exact; one DR axis')
co = collections.Counter()
for v in range(2187):
    t = [(v // 3 ** i) % 3 for i in range(7)]
    t.append((-sum(t)) % 3)
    co[sum(x != 0 for x in t)] += 1
claim('EO-DR-18', 'Emma: after a random EO, 3 misoriented corners ~5.12%, 4 ~19.20%',
      f"3: {co[3]}/2187 = {pct(co[3] / 2187)}; 4: {co[4]}/2187 = {pct(co[4] / 2187)}", 'confirmed', 'exact over 3^7 corner orientations')
six = [v for v in range(2187)]
cnt60 = cnt33 = 0
for v in range(2187):
    t = [(v // 3 ** i) % 3 for i in range(7)]
    t.append((-sum(t)) % 3)
    if sum(x != 0 for x in t) == 6:
        cw = sum(x == 1 for x in t)
        if cw in (0, 6):
            cnt60 += 1
        else:
            cnt33 += 1
claim('EO-DR-5', 'wen: 50% of 6cXe cases are 6+0; Zagros: 1 in 11', f'6+0: {cnt60} of {cnt60 + cnt33} six-twist orientations = {Fraction(cnt60, cnt60 + cnt33)}',
      'Zagros is right (1 in 11)', 'exact over 3^7 corner orientations; edges are independent')
ranks = sorted(((int(r['cosets']), r['case']) for k, r in c6.items() if k != 'all'), reverse=True)
top = ', '.join(f'{c} {pct(m / 1082565)}' for m, c in ranks[:5])
claim('EO-DR-32', 'Jay: DR-5c6e is tied for the most common DRM after a random EO (torchlight: 6c more common, 3+3 tied with 5c)',
      f'most common cases: {top}', 'confirmed, both: in Cale\'s split (6c as 3+3 and 6+0) 5c6e is tied with 6c6e(3+3) (the same number of states), as Jay and torchlight\'s edit say; 6c6e as a whole is the most common',
      'exact over the 1,082,565 EO-solved cosets')
anyrow = c7['one DR axis, any turns (EO may break)']
claim('S-DR-76', "torchlight: EO->DR with EO-breaking turns allowed (7.797 against 7.803)",
      f"exact means: EO kept {plain['mean']}, any turns {anyrow['mean']}; <=6: {pct(plain['p_le6'])} against {pct(anyrow['p_le6'])}", 'confirmed',
      'exact over the 1,082,565 EO-solved cosets')
claim('S-DR-77', 'DougCube, KrzychXyz: how much do EO-breaking DRs change the EO->DR distribution?',
      f"mean {plain['mean']} -> {anyrow['mean']}; <=5 {pct(plain['p_le5'])} -> {pct(anyrow['p_le5'])}; <=6 {pct(plain['p_le6'])} -> {pct(anyrow['p_le6'])}",
      f"answered: hardly at all (of the {be['states_shorter_with_any_turns']} states shorter with any turns, {be['all_0e_cases']['shorter_with_any_turns']} are xc0e, where the other EO is solved and a DR as short keeps it)", 'exact', 'X6 (witness_extra.json; W12 is a 3c0e state)')
ni = {r['case']: r for r in rd('c6_normal_inverse.tsv')}
claim('EO-DR-326', 'Jay: RZP->DR on normal and on inverse are uncorrelated (Tom Nelson, rodneykinney: regression to the mean)',
      f"correlation of the EO-kept DR length on normal and on inverse (same axis): {ni['all']['correlation']} over all EO states; P(inverse <=6) = {ni['all']['p_inv_le6']}, given normal 9: {ni['all']['p_inv_le6_given_normal_9']}, given normal 6: {ni['all']['p_inv_le6_given_normal_6']}",
      'true for a known case, as after an RZP (Tom Nelson agreed, D850): within a case the correlation is between -0.015 and 0.063 (35 cases with 1000+ samples, out/c6_normal_inverse.tsv), within +-0.006 for the cases people switch from (4c4e, 4c2e, 3c2e, 7c8e, 3c4e, 8c8e), largest where 6c and 8c lump sub-cases (3+3/6+0, 4+4/7+1) that inversion keeps; the 0.17 overall, case not known, is almost all the case', f"{C['sampled_states']} uniform EO-solved states, exact lookups")
claim('EO-DR-336', 'DanielEgdal: EO->DR length as the minimum of normal and inverse?',
      f"mean {c7['one DR axis, EO kept, better of normal and inverse']['mean']} (against {plain['mean']}), <=6 {pct(c7['one DR axis, EO kept, better of normal and inverse']['p_le6'])}",
      'answered', 'sampled, exact lookups')
claim('EO-DR-334', 'DanielEgdal: EO->DR statistics with both DR axes of one EO (T3226-T3347: thought infeasible, ~5e9 states per FakeMMAP, a run stalled at 3e8)',
      f"exact: mean {c7['better of the two DR axes, EO kept']['mean']}, <=6 {pct(c7['better of the two DR axes, EO kept']['p_le6'])}, <=7 {pct(c7['better of the two DR axes, EO kept']['p_le7'])}",
      'answered exactly', 'exact: corners 8!·3^7 x E/M-slice places 34650, both axes from eo-fb_dr', wid('C6a', 'two DR axes'))
# ---- S-EO
L = B['layouts']
claim('S-EO-67', 'torchlight: an EO skip on some axis is 103741/70963200', f"{L['states_some_axis_eo_solved']}/{L['total_arrangement_flip_states']}", 'confirmed', 'exact over all edge states')
claim('S-EO-44', 'EG-1 grind?: 13.907% chance that all three axes have 0, 2, 4 or 8 bad edges', L['p_all_axes_in_0_2_4_8'], 'confirmed', 'exact')
claim('S-EO-39', 'torchlight: the sum of bad edges over three axes peaks at 18 with 23.93%', pct(L['sum_distribution_p']['18']), 'confirmed', 'exact')
claim('S-EO-41', 'Yura: 6/6/4 or 6/6/8 (sorted) is more likely than 6/6/6', f"sorted 4/6/6 {L['sorted_6/6/4']}, 6/6/6 {L['sorted_6/6/6']}, 6/6/8 {L['sorted_6/6/8']}", 'confirmed', 'exact')
claim('S-EO-43', 'wen: 0/0/2 is more common than 0/0/8', f"0/0/2 {L['sorted_0/0/2']}, 0/0/8 {L['sorted_0/0/8']}", 'confirmed', 'exact')
claim('S-EO-45', 'wen: no two axes differ by more than 8; 10/10/2 exists', f"largest difference {L['max_difference_between_two_axes']}; 2/10/10 has {L['sorted_2/10/10']}", 'confirmed', 'exact')
claim('S-EO-46', 'Aneurin: 12 bad on one axis forces at least 4 on the others', f"fewest on another axis given 12: {L['min_other_axes_given_12_on_fb']}", 'confirmed' if L['min_other_axes_given_12_on_fb'] >= 4 else 'refuted', 'exact')
claim('S-EO-47', 'Jay: after EO the other two axes have 0-8 bad edges, never 10 or 12', f"possible counts on the other axes: {L['other_axes_range_given_0_on_fb']}", 'confirmed' if max(L['other_axes_range_given_0_on_fb']) <= 8 else 'refuted', 'exact')
claim('S-EO-17', 'Tom Nelson, Aneurin: odds of all edges bad on all three axes', L['p_all_bad_all_axes_12_12_12'], 'answered', 'exact')
ten = [r for r in ax if r['bad'] == '10']
tw = collections.Counter(r['optimal'] for r in ten)
claim('S-EO-24/25/26', 'beef beans: any linear 10-bad 5-move EOs? Zagros: some 10 bad need 7; KrzychXyz: 2 cases (good edges both on F)',
      f"the 66 ten-bad states of one axis: optimal linear EO {dict(sorted(tw.items()))}", 'no 5-movers; 7-movers exist' + (f' ({tw["7"]} states)' if '7' in tw else ''),
      'exact over the 2048 EO states of one axis; states, not cases up to symmetry')
tw12 = [r['optimal'] for r in ax if r['bad'] == '12']
claim('S-EO-23', 'wen: the optimal linear EO for 12 bad edges is 7', f'{tw12[0]}', 'confirmed' if tw12 == ['7'] else 'refuted', 'exact')
claim('S-EO-141', 'wen, EG-1 grind?: a 4-move EO is likelier from 8 bad than from 6 bad (kyh: 8 is worse)',
      f"linear <=4: 6 bad {pct(byb[6]['p_linear_le4'])}, 8 bad {pct(byb[8]['p_linear_le4'])}; with NISS (sampled) {pct(byb[6]['p_niss_le4'])} against {pct(byb[8]['p_niss_le4'])}",
      ('depends: confirmed linearly; with NISS 6 bad is a little better' if float(byb[8]['p_niss_le4']) < float(byb[6]['p_niss_le4']) else 'confirmed') if float(byb[8]['p_linear_le4']) > float(byb[6]['p_linear_le4']) else 'refuted', 'linear: exact over one axis; NISS: 1,000,000 random states x 3 axes')
claim('S-EO-140', 'wen: probability of a <5 move EO with 8 bad edges (feels no better than 6 bad)',
      f"linear {pct(byb[8]['p_linear_le4'])}, NISS {pct(byb[8]['p_niss_le4'])}", 'answered', 'as above')
claim('S-EO-137', 'trig0n: odds of a <=4-move EO for 10 bad', f"linear {pct(byb[10]['p_linear_le4'])}, normal or inverse {pct(byb[10]['p_lin_or_inv_le4'])}, NISS {pct(byb[10]['p_niss_le4'])}", 'answered', 'as above')
anyl, anyn = B['any_axis_linear'], B['any_axis_niss']
claim('S-EO-85/86', 'argonblue: how rare are 3-move EOs? wen: probability of a 3-move NISS EO (all three forms)',
      f"EO in <=3 on some axis: linear {pct(anyl['p_le3'])}, normal or inverse {pct(B['any_axis_lin_or_inv']['p_le3'])}, NISS {pct(anyn['p_le3'])}", 'answered',
      '1,000,000 random states, all three axes')
claim('S-EO-6/9', 'Joba / DougCube: fixed-axis EO mean 4.609, best NISS EO over all axes 3.455', f"{B['one_axis_optimal_mean']} (exact); {anyn['mean']} (sampled)", 'confirmed', 'exact; 1,000,000 random states')
sf = sfw
claim('S-EO-12/13', 'Aneurin: superflip EO is 7 even with NISS; alkamaass: is NISS useless for EO on the superflip?', sf['finding'].split('; ')[-1],
      'confirmed: 7 even with NISS (the same author\'s later "6 with NISS" is wrong); NISS does not shorten the superflip EO; most other 12/12/12 states do have a NISS EO under 7 (Joba T9374: 1792 edge states need 7, against 13824 with 12/12/12; torchlight T9414: superflip + M 3-cycle has 6-move NISS EOs, replayed as X7)' if sf['finding'].endswith('7 linear, 7 with NISS') else 'see value', 'exact for the superflip', sf['id'])
lin_all = {(r['eos'], r['axes'], r['length']): r for r in b4}
k = lambda e, a, l: lin_all[(e, a, str(l))]
claim('S-EO-75/76', 'wen: about 200 EOs of <=5 and 17 of <=4 per scramble; Lichi Fang: median for <=4 about 14, skewed, up to 50-60',
      f"linear normal, all axes, every EO (nissy -a): <=4 mean {k('linear (normal)', 'all three axes', 4)['mean_le']} (median {k('linear (normal)', 'all three axes', 4)['median_le']}), <=5 mean {k('linear (normal)', 'all three axes', 5)['mean_le']}; with NISS <=4 mean {k('NISS (normal, inverse, both)', 'all three axes', 4)['mean_le']} (median {k('NISS (normal, inverse, both)', 'all three axes', 4)['median_le']}), <=5 mean {k('NISS (normal, inverse, both)', 'all three axes', 5)['mean_le']}; nissy's default NISS listing on the first {dl['scrambles']} scrambles: <=5 mean {dl['le5']['niss_default_per_scramble']['mean']:.1f} (median {dl['le5']['niss_default_per_scramble']['median']}), <=4 mean {dl['le4']['niss_default_per_scramble']['mean']:.1f} (median {dl['le4']['niss_default_per_scramble']['median']}); it keeps {pct(dl['le5']['one_sided']['default'] / dl['le5']['one_sided']['all'], 1)} of one-sided and {pct(dl['le5']['two_sided']['default'] / dl['le5']['two_sided']['all'], 1)} of two-sided EOs of <=5, {pct(dl['le5']['niss']['default'] / dl['le5']['niss']['all'], 1)} in all",
      "true as Cale's sheet of official scrambles counts them (NISS, all axes, nissy's default listing: mean 246, median 217 for <=5; mean 17.3, median 14 for <=4); every EO (-a) gives more; see value", f'{n} random-state scrambles; default listing: out/default_listing.json')
claim('S-EO-88', 'Kai Cui: a scramble never has more 3-move than 4-move EOs (kalindumaxxer: "i literally got one"; Yura: U (R2 U))',
      f"linear (normal, all axes): {pct(A['more3than4_linear'], 3)} of scrambles; with NISS {pct(A['more3than4_niss'], 3)}",
      'withdrawn at the time (Kai Cui: "oh bruh", "nvm then"); with every EO counted it happens with NISS (rare), never linearly in the sample; kalindumaxxer asked excluding HTR-equivalent variants, a convention not counted here' if A['more3than4_linear'] == 0 else 'refuted', f'{n} scrambles; every EO counted (nissy -a)', wid('B4', 'more 3-move'))
fw = next(w for w in wit if w['question'] == 'B4' and 'fewest' in w['finding'])
claim('S-EO-91', 'Enrico: fewest EOs in 5 on a scramble (Dunni 26 with 29 sub-6 in total; Yura 7 on cubers.io)', fw['finding'], 'answered for the sample', f'{n} scrambles', fw['id'])
gap = A['gap_linear']
claim('S-EO-87', 'Ben: how often does a scramble have an N-move EO but no (N+1)-move EO? JTuu: maybe only for N = 0, 1, 2',
      'linear, all axes: ' + ', '.join(f"{kk.replace('_but_no_', ' but no ')}: {pct(v, 3)}" for kk, v in gap.items()), 'answered', f'{n} scrambles')
keys = ['entry', 'said', 'ours', 'verdict', 'conditions', 'witness']
with open(os.path.join(OUT, 'claims.tsv'), 'w') as f:
    f.write('\t'.join(keys) + '\n')
    for r in rows:
        f.write('\t'.join(str(r[k]).replace('\t', ' ') for k in keys) + '\n')
print(f'{len(rows)} claims written')
