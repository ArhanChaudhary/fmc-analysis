"""Writes the skeleton/variant meta page from ../out/meta/tfinal{2,3,4}.json (tfinal.py), ../out/meta/opt3.npz
(topt.py) and the examples of texamples.json (texamples.py).  Every number on the page is read from those files.
usage: mkpage_svm.py OUT.md"""
import sys, json
import numpy as np
from tcommon import ORDER, BYQT, path

DOC = 'https://docs.google.com/document/d/13F8HonrKJyHjU9EwfiHDRyY4X77vPriYeaVSrh5guq0'
J = {m: json.load(open(path(f'tfinal{m}.json'))) for m in (2, 3, 4)}
EX = json.load(open(path('texamples.json')))
MR = json.load(open(path('mirror.json')))
SP = json.load(open(path('tsplit.json')))
GF = json.load(open(path('greedy_frontier.json')))
BASE_STEP = J[2]['baseline_pairs']            # does the baseline use the pairs the way the meta does?
MODE = J[2]['pairs_mode']                     # 'drop': step 6 drops the less-paired variants; 'first': they are only taken later
DROP = MODE == 'drop'
assert all(J[m]['baseline_pairs'] == BASE_STEP and J[m]['pairs_mode'] == MODE for m in (2, 3, 4))
assert not DROP, 'the page is written for SVM_PAIRS=first: nothing is dropped for its pairs, and the order of finishing is by moves to HTR'
PAIRS_HOW = 'Count the corner/edge pairs in the U and D layers right after the variant\'s last insertion, before the next quarter turn.'
GOAL = {2: 12, 3: 13, 4: 14}
# the 19 Nov page's numbers that the change list quotes
OLD = {'4b2': dict(miss='8.2%', routes='77'), '2c3': dict(miss='6.9%', routes='169')}
ALL = [(m, k) for m in (2, 3, 4) for k in BYQT[m]]
C = {k: J[m]['cases'][k] for m, k in ALL}
# the premove pass: 'add' = the pass, then every skeleton in full (the meta); False = no pass
PASS = J[2]['uniss']
assert PASS in (False, 'add') and all(J[m]['uniss'] == PASS for m in (2, 3, 4)), 'the page is written for the premove pass followed by the full search'
# a skeleton that starts and ends with a quarter turn: the pass on both sides (True) or on inverse only
BOTH = bool(J[2].get('rest_both', False))
assert all(bool(J[m].get('rest_both', False)) == BOTH for m in (2, 3, 4))
if PASS:
    # the three versions of trule.py: no pass, the pass in place of the full search (the doc), the pass then full (the meta)
    TR = {m: json.load(open(path(f'trule{m}.json'))) for m in (2, 3, 4)}
    V3 = {k: TR[m][k] for m, k in ALL}
    for k in V3:
        a, b = V3[k]['added'], C[k]['bounds']['cca']
        assert abs(a['miss'] - b['miss']) < 1e-9 and a['htr_med'] == b['htr_med'] and a['n'] == b['n'], ('trule and tfinal disagree', k)
        assert abs(V3[k]['none']['miss'] - C[k]['uniss']['miss0']) < 1e-9 and C[k]['uniss']['lost'] == 0 and a['lost'] == 0

def one_in(n, nok):
    if nok == 0: return 'none'
    v = n / nok
    return f'1 in {v:.1f}' if v < 10 else f'1 in {v:,.0f}'
def pct(x, dec=1): return '—' if x is None or x != x else f'{100 * x:.{dec}f}%'
def num(x): return f'{x:,.0f}'
def who(c): return f"{c['drs']:,} DRs, {c['wg']:,} within-goal" + (' (a small sample)' if c['wg'] < 100 else '')
def times(a, b): return f'{a / b:.0f}×' if b else '—'
def an(n): return 'an' if n in (8, 11, 18) else 'a'
def pts(d): return f'{abs(100 * d):.1f} points ' + ('higher' if d > 0 else 'lower')
BN = {'none': 'Baseline (no DR Bounding)', 'simple': 'Simple', 'cca': 'Corner-case-aware', 'comp': 'Comprehensive'}

out = []
def w(s=''): out.append(s)
# the comparison of the orders (mkstd.py), next to this page
STD_TITLE, STD_LINK = 'HTR search order and limits', 'ORDER-AND-LIMITS.md'

# ------------------------------------------------------------------------------------------------------- intro
w('# The skeleton/variant meta')
w()
w('24 Nov 2026')
w()
w(f'A meta for finding DR finishes within a certain goal move count, based on [*Advanced DR Bounding*]({DOC}).')
w('The meta is based on the extra moves needed on top of a corner skeleton: any algorithm that solves corners, modulo corner swaps and rotations. Its length L is counted after removing any corner swaps.')
w('The extra moves are broken down as in the doc:')
w()
w(' - **P**: Additional moves used to reach 2qt')
w(' - **S**: Additional moves used to set up the 2qt trigger')
w(' - **T**: Additional moves in the trigger')
w(' - **N**: Additional moves after reaching HTR ')
w()
w('With L the length of the skeleton and G the goal, a solution has L+P+S+T+N moves, and G−L is the number of spare moves.')
w()
w('These stats use a goal of 12/13/14 moves for 2qt/3qt/4qt cases, counting the moves from DR to a leave-slice finish.')
w()
e = EX['swap']
pe = EX['pair']
w('**What a skeleton looks like.** Between two quarter turns it has a single half turn, an X2 U2 Y2 sequence, or nothing. '
  'Before its first quarter turn it has nothing, X2, U2 X2 or X2 U2 Y2, and after its last one nothing, X2, X2 U2 or X2 U2 Y2 (X and Y are side faces on different axes). '
  'Whatever else a solution has is extra moves:')
w()
w('- `U R2 F2 U` is a 3-move skeleton with T=1. `R2 F2` is `R2` with a corner swap in it (`R2 F2 R2` then `R2`), so the skeleton is `U R2 U`.')
w('- `U R2 U R2 F2 R2` is also a 3-move skeleton, with N=3.')
w(f"- On the {pe['case']} DR `{pe['scramble']}`, the solution `{pe['solution']}` has the {pe['L']}-move skeleton `{pe['skeleton']}` and T={pe['T']}: "
  f"the slice `{pe['slice']}` sits between two quarter turns that have nothing between them in the skeleton (a cancelling pair).")
w()
w('Every corner solution of that shape is a skeleton, with its own L, so a DR has many of them (section 2 counts them). Every solution in these stats is read against its own skeleton, section by section (appendix C).')
w()
w('**The inverse reads a solution backwards**, so the values swap places:')
w()
w('| Skeleton | On normal | On inverse |')
w('|---|---|---|')
w('| 2qt | (S, T, N) | (N, T, S) |')
w('| 3qt | (P, S, T, N) | (N, T, S, P) |')
w('| 4qt | (P, P, S, T, N) | (N, T, S, P, P) |')
w('| 5qt | (P, P, P, S, T, N) | (N, T, S, P, P, P) |')
w()
w(f"For example, on the {e['case']} DR `{e['scramble']}`, the solution `{e['solution']}` has {an(e['L'])} {e['L']}-move skeleton and reads "
  f"(P, S, T, N) = ({e['tuple']}). Its inverse, `{e['inverse']}`, solves the inverse scramble and reads ({e['inv_tuple']}).")
w()

# ------------------------------------------------------------------------------------------------------- section 1
w('## 1. The meta')
w()
w('The standard meta, roughly speaking, is to spam HTRs whose length is not too far from the goal, on both normal and inverse.')
w('You don\'t want too many extra moves early in the skeleton, and block building is of limited value, because preserving blocks is often incompatible')
w('with the approach to HTR.  ')
w()
w('Here, we formalize the meta in terms of skeletons and their variants. We quantify "not too far from the goal"')
w('and "too many extra early moves" as follows:')
w()
w('1. **Sort the attempt\'s DRs by corner case**, shortest skeleton first, in the order of the table below.')
w('2. **Within a DR, find the skeletons on normal and inverse.** Skeletons with two more quarter turns than the DR count too.')
w('3. **For each skeleton, take the variants with P ≤ 1 and P+S+T ≤ 5 whose HTR is at most G−1 moves away.** At G moves there is no move left for a finish.')
w('4. **Leave a variant to the other side when it comes earlier there.** A variant\'s early extra moves on one side are its late extra moves on the other, so each side only needs the variants with:')
w('    - N ≥ S on a 2qt skeleton')
w('    - N ≥ P on a 3qt skeleton')
w('    - T+N ≥ P on a 4qt skeleton')
w('    - S+T+N ≥ P on a 5qt skeleton')
w('5. **Discard a variant when L+P+S+T+N > G**, where N is the bound\'s N, or the smallest N step 4 allows if that is larger.')
w(f'6. **Finish the rest in order of moves to HTR, fewest first**, with the skeletons and the two sides mixed. Among HTRs equally far, take the ones with the most pairs first. {PAIRS_HOW}')
if DROP:
    w('6. **Among a skeleton\'s remaining variants with the same (P, S, T, N), finish only the ones with the most pairs.** '
      f'{PAIRS_HOW} Variants tied for the most are all finished.')
w()
w('For example, a 2qt skeleton of 6 moves has 6 spare moves at goal 12. With step 4, a setup with S=2 can only take a trigger with T ≤ 2, and a setup with S=3 only T=0, whatever the bound says.')
w()
e = EX['step']
w('The pairs settle which of two HTRs equally far goes first. '
  + f"On {e['side']}the {e['case']} DR `{e['scramble']}`, `{e['hi_path']}` and `{e['lo_path']}` are variants of the same {e['L']}-move skeleton, "
  f"both with {e['st']}, and both reach HTR in {e['moves']} moves. There are {e['hi_pairs']} pairs after `{e['hi_cut']}` and {e['lo_pairs']} after `{e['lo_cut']}`, "
  + ('so only the first is finished: ' if DROP else 'so the first is finished first: ')
  + (f"`{e['hi_finish']}` makes it {e['hi_total']} moves." if e['hi_finish'] else f"it is solved in {e['hi_total']} moves as it stands.")
  + f" The second can't be finished in fewer than {e['lo_total']}.")
w()
if PASS:
    e = EX['premove']
    w('**A skeleton that ends in HH gets a premove pass as well.** When a skeleton of 3 or more quarter turns ends with its last quarter turn (HH corners), '
      'apply that turn as a premove on the other side and NISS. What is left is a one-fewer-qt case with a goal one lower: take its variants with steps 2, 3 and 5. '
      'The premove counts as a move to HTR in steps 3 and 6. The skeleton is also checked linearly, as in the steps above. '
      + ('A skeleton that also starts with a quarter turn ends with one on both sides, and gets the pass on both.' if BOTH else
         'When the skeleton also starts with a quarter turn, make the pass on inverse only: its first quarter turn is the premove, made on normal.'))
    w()
    w('Checking a skeleton linearly means going through its variants on the side it is on, with no premove, as in steps 3 to 5. '
      'The pass reads the same moves one section later: the last section before 2qt becomes the setup, the setup becomes the trigger, and the trigger becomes the finish. '
      'So it gets to solutions that have too many early extra moves on both sides. '
      + (f"For example, on the {e['case']} DR `{e['scramble']}`, the {e['total']}-move solution `{e['solution']}` reads {e['full']} on its {e['q']}qt skeleton, " if e['side'] == 'normal' else
         f"For example, on the inverse of the {e['case']} DR `{e['scramble']}`, the {e['total']}-move solution `{e['solution']}` reads {e['full']} on its {e['q']}qt skeleton, ")
      + (f"and the same on {e['other_side']}" if e['same'] else f"and {e['other']} on {e['other_side']}") + f": {e['why']}. "
      f"With its last `{e['turn']}` as a premove, what is left reads {e['rest']} on a {e['rest_q']}qt skeleton, and steps 3 and 5 let it through.")
    w()
    w(f'This is the NISS rule of the Suggested Meta in [*Advanced DR Bounding*]({DOC}), with one difference. There the pass takes the place of checking that side linearly. '
      'Here the skeleton is still checked linearly as well, because the pass alone loses the solutions that go on after that quarter turn (section 2).')
    w()
if DROP: bl = ', so step 6 compares the variants with the same (P, S, T).' if BASE_STEP else ', and step 6 is left out.'
else: bl = '. The order of step 6 is the same.' if BASE_STEP else '. The order of step 6 is the same, without the pairs.'
w('In the **baseline** meta, you do the same without DR Bounding: the only N you have is the one from step 4' + bl)
w('Advanced DR Bounding adds a way to compute N. The stats below show the benefit of using it')
w('to discard variants. ')
w()
OPT = EX['opt']
BIG = [k for k in ORDER if C[k]['wg'] >= 100]
WG = sum(C[k]['wg'] for k in ORDER)
# step 4 under the cap: within-goal DRs found without it and not with it, and the other way round (step 6 can drop a
# within-goal variant for one that step 4 would have left to the other side)
lost4 = sum(C[k]['step4']['lost'] for k in ORDER); gain4 = sum(C[k]['step4']['gained'] for k in ORDER)
cut = 1 - float(np.exp(np.mean([np.log(C[k]['var']['pst5']['htr_mean'] / C[k]['var']['nofloor']['htr_mean']) for k in BIG])))
lost40 = sum(C[k]['step4']['lost0'] for k in ORDER)       # the same before step 6
def step4_txt():
    """What step 4 costs with P+S+T <= 5 in place, before step 6 and with it."""
    alone = 'it loses no within-goal DR of the sample' if lost40 == 0 else f"it loses {lost40} of the sample's {WG:,} within-goal DRs"
    if not DROP: return alone[0].upper() + alone[1:]
    if lost4 == lost40 and gain4 == 0: return f'On its own and with step 6, {alone}'
    t = f"On its own {alone}. With step 6 it loses {lost4} of the {WG:,}: a variant it leaves to the other side can be dropped there for one with more pairs"
    if gain4: t += f" (and it finds {gain4} that step 6 drops without it)"
    return t
SAME_CAPS = abs(OPT['best2'] - OPT['meta_work']) < 1e-9 and abs(OPT['best3'] - OPT['meta_work']) < 1e-9
s3 = ('No two or three caps together do better than P+S+T ≤ 5 alone without missing more in some corner case' if SAME_CAPS else
      f"The best two or three caps together finish {pct(1 - min(OPT['best2'], OPT['best3']) / OPT['meta_work'], 0)} fewer HTRs than P+S+T ≤ 5 alone without missing more in any corner case")
w(f"The cap of step 3 was chosen by scoring every combination of up to three caps on S, T, N and their partial sums (appendix B). "
  f"Step 4 cuts the HTRs to finish by {pct(cut, 0)}. {step4_txt()}. "
  f"{s3}, and caps that include N, like S+T+N or T+N, "
  f"give up more within-goal finishes than they save in HTRs.")
w()
w('### Corner cases')
w()
w('These stats are based on a random sample of 2qt/3qt/4qt DRs, 2,000 of each (1,960 for 2qt; see appendix C). This table gives the chance that ')
w('a corner case has a within-goal solution, and the chance that the recommended meta will miss it.')
w()
w('| Corner case | Shortest skeleton length | Within-goal DRs | The meta misses a within-goal finish | DRs in the sample |')
w('|---|---|---|---|---|')
for k in ORDER:
    c = C[k]
    w(f"| {k} | {c['lmin']} | {pct(c['wg'] / c['drs'])} | {pct(c['bounds']['cca']['miss'])} | {c['drs']:,} |")
w()
e = EX['missed']
DM = {k: C[k]['bounds']['cca']['miss'] - C[k]['bounds']['none']['miss'] for k in ORDER}
dmax = max(abs(v) for v in DM.values())
MC = {key: sum(C[k]['miss']['counts'].get(key, 0) for k in ORDER) for key in ('P', 'P+S+T', 'several', 'pairs', 'bound', 'outside')}
MLOST = sum(C[k]['miss']['lost'] for k in ORDER)
assert sum(MC.values()) == MLOST
def base_txt(lead):
    """How the baseline's chance of missing differs from the meta's (DM = meta - baseline, per corner case)."""
    lo, hi = min(DM.values()), max(DM.values())
    if dmax < 5e-4: return None
    if hi <= 5e-4:
        return (f"{lead} misses up to {-100 * lo:.1f} points more" +
                (': without the bound, its step 6 has more variants to compare on each skeleton and drops more of them.' if BASE_STEP and DROP else '.'))
    if lo >= -5e-4: return f"{lead} misses up to {100 * hi:.1f} points less" + ('.' if BASE_STEP or not DROP else ': it has no step 6.')
    return f"{lead}'s chance of missing is {-100 * hi:+.1f} to {-100 * lo:+.1f} points away from the meta's, depending on the corner case."
bt = base_txt('The baseline')
w('As we\'ll see below, the miss percentages do not depend on whether you use DR Bounding to prune the search.' if bt is None else
  f'These are the misses with DR Bounding. {bt}')
rest = MC['bound'] + MC['outside']
if DROP:
    w(f"The misses come from the two caps of step 3 and from step 6. Of the {MLOST:,} within-goal DRs the meta misses in the sample, a second move before 2qt is needed for {MC['P']:,}, "
      f"P+S+T of 6 or more for {MC['P+S+T']:,} and both for {MC['several']:,}, and step 6 drops the within-goal variant of {MC['pairs']:,} for one with more pairs."
      + (' Section 2 has the rest.' if rest else ''))
else:
    assert MC['pairs'] == 0
    w(f"The misses come from the two caps of step 3. Of the {MLOST:,} within-goal DRs the meta misses in the sample, a second move before 2qt is needed for {MC['P']:,}, "
      f"P+S+T of 6 or more for {MC['P+S+T']:,} and both for {MC['several']:,}." + (' Section 2 has the rest.' if rest else ''))
w('Extra moves before 2qt on normal are extra moves at the end on inverse, ')
w('so a cap loses a DR when its solutions need two moves before 2qt on both sides, or more than 5 extra moves before HTR on both sides.')
w(f"For example, the {e['case']} DR `{e['scramble']}` has a {e['n_total']}-move solution on normal, `{e['n_solution']}`, "
  f"which reads (P, S, T, N) = ({e['n_tuple']}) on its {e['n_L']}-move skeleton. On inverse, the nearest it gets is `{e['i_solution']}`, "
  f"which reads ({e['i_tuple']}) on {an(e['i_L'])} {e['i_L']}-move skeleton: 2 extra moves before 2qt again. The meta finds neither"
  + (', with or without a premove.' if PASS else '.'))
w()

# ------------------------------------------------------------------------------------------------------- section 2
w('## 2. Stats for the recommended meta')
w()
ratios = [C[k]['bounds']['none']['htr_med'] / C[k]['bounds']['cca']['htr_med'] for _, k in ALL]
dmiss = max(C[k]['bounds']['cca']['miss'] - C[k]['bounds']['none']['miss'] for _, k in ALL)
dms = [C[k]['bounds']['cca']['miss'] - C[k]['bounds']['none']['miss'] for _, k in ALL]
if max(abs(v) for v in dms) < 5e-3: tail = 'with only a negligible change in missed within-goal finishes.'
elif max(dms) <= 5e-4: tail = f'and lowers the chance of missing a within-goal finish by up to {-100 * min(dms):.1f} points.'
elif min(dms) >= -5e-4: tail = f'and raises the chance of missing a within-goal finish by up to {100 * max(dms):.1f} points.'
else: tail = f'and moves the chance of missing a within-goal finish by {100 * min(dms):+.1f} to {100 * max(dms):+.1f} points, depending on the corner case.'
w(f'Filtering by the DR Bounding lower limit **reduces the number of HTRs to check by {min(ratios):.0f}-{max(ratios):.0f}x**, ' + tail)
w()
w(f'The stats below use the "corner-case-aware" bound from [*Advanced DR Bounding*]({DOC}), without the reflection penalty (which would improve the numbers). See the doc for details.')
w()
w('How to read the columns:')
w()
w('- **HTRs to finish per DR.** The variants the search finishes, as a median over all the case\'s DRs, within-goal or not.')
w('- **Within goal.** The share of those HTRs whose finish fits the goal.')
w('- **Chance of missing a within-goal finish.** The share of within-goal DRs where none of them does.')
w()
for m in (2, 3, 4):
    w(f'### {m}qt DRs (goal {GOAL[m]})')
    w()
    for k in BYQT[m]:
        c = C[k]; b0, b1 = c['bounds']['none'], c['bounds']['cca']; ef = c['effort']
        dm = 100 * (b1['miss'] - b0['miss'])
        miss = 'no change in the chance of missing' if abs(dm) < 0.05 else f'a chance of missing {pts(dm / 100)}'
        w(f"**{k}** · {who(c)} · {num(ef['skel_med'])} skeletons and {num(ef['routes_med'])} routes to 2qt per DR (median, both searches). "
          f"The bound finishes {times(b0['htr_med'], b1['htr_med'])} fewer HTRs with {miss}.")
        w()
        w('| Search | HTRs to finish per DR (median) | Within goal | Chance of missing a within-goal finish |')
        w('|---|---|---|---|')
        w(f"| {BN['none']} | {num(b0['htr_med'])} | {one_in(b0['n'], b0['nok'])} | {pct(b0['miss'])} |")
        w(f"| **{BN['cca']}** | {num(b1['htr_med'])} | {one_in(b1['n'], b1['nok'])} | {pct(b1['miss'])} |")
        w()

# ---- misses
w('### Where the misses come from')
w()
own = {k: C[k]['own_miss'] for _, k in ALL}
big = sorted([k for _, k in ALL if own[k] - C[k]['bounds']['cca']['miss'] > 0.1], key=lambda k: -own[k])
nout = max(C[k]['miss']['counts']['outside'] for _, k in ALL)
w(f"Skeletons with two more quarter turns are part of the meta. Without them, {big[0]} would miss {pct(own[big[0]])} of the time instead of {pct(C[big[0]]['bounds']['cca']['miss'])}, "
  f"and {big[1]} {pct(own[big[1]])} instead of {pct(C[big[1]]['bounds']['cca']['miss'])}. "
  f"Skeletons with four more quarter turns would save at most {nout} within-goal DR{'s' if nout != 1 else ''} in any corner case.")
w()
w('Each missed DR is filed under what its nearest within-goal HTR breaks, on the side where it breaks the least' + (', in the premove pass or linearly' if PASS else '') + '. Cells are shares of within-goal DRs, '
  f"and the {'six' if DROP else 'five'} columns on the right add up to the meta\'s chance of missing, up to rounding.")
w()
e = EX['lostpairs']
if not DROP:
    assert e is None and MC['pairs'] == 0
elif e:
    w(f"**Dropped by step 6** counts DRs with a within-goal variant that passes steps 3 to 5 and loses to another variant of its skeleton with more pairs. "
      f"For example, on {e['side']}the {e['case']} DR `{e['scramble']}`, `{e['lo_solution']}` is {an(e['lo_total'])} {e['lo_total']}-move solution on {an(e['L'])} {e['L']}-move skeleton, "
      f"with {e['st']} and N = {e['nb']} from the bound. It has {e['lo_pairs']} pairs after `{e['lo_cut']}`. "
      f"`{e['hi_path']}` is on the same skeleton with the same values and has {e['hi_pairs']} pairs after `{e['hi_cut']}`, so that one is finished instead, "
      f"and it can't be finished in fewer than {e['hi_total']}.")
else:
    assert MC['pairs'] == 0
    w('**Dropped by step 6** counts DRs with a within-goal variant that passes steps 3 to 5 and loses to another variant of its skeleton with more pairs. There is none in the sample.')
if DROP: w()
e = EX['bound']
assert e or MC['bound'] == 0
w(f"**Error in DR Bound** counts DRs lost because the corner-case-aware table asks +5 for RD or FD corners with 1 bad slice and cs/fr 1/1, where +4 is enough. "
  + (f"For example, on {e['side']}the {e['case']} DR `{e['scramble']}`, `{e['path']}` reaches HTR in that case in {e['len']} moves and `{e['finish']}` finishes in {e['fin']}, "
     f"{e['total']} in all. That reads ({e['tuple']}) on a {e['L']}-move skeleton, but the bound says N ≥ {e['nb']}, which makes {e['says']}." if e else 'There is none in the sample.'))
w()
w('| Corner case | Missed with only the DR\'s own quarter turns | Missed | Needs a second pre-2qt move | Needs P+S+T of 6 or more | Needs both | '
  + ('Dropped by step 6 | ' if DROP else '') + 'Error in DR Bound | Needs four more quarter turns |')
w('|---|---|---|---|---|---|---|---|' + ('---|' if DROP else ''))
for m, k in ALL:
    x = C[k]['miss']['counts']; n = max(C[k]['wg'], 1)
    assert x.get('floor', 0) == 0, (k, x)
    w(f"| {k} | {pct(own[k])} | {pct(C[k]['bounds']['cca']['miss'])} | {pct(x['P'] / n)} | {pct(x['P+S+T'] / n)} | {pct(x['several'] / n)} | "
      + (f"{pct(x['pairs'] / n)} | " if DROP else '') + f"{pct(x['bound'] / n)} | {pct(x['outside'] / n)} |")
w()

# ---- what the pairs do
PS = {key: sum(C[k]['pairs'][key] for k in ORDER) for key in ('htrs', 'shared', 'dropped', 'ok', 'ok_dropped')}
kept = PS['htrs'] - PS['dropped']; okkept = PS['ok'] - PS['ok_dropped']
if DROP:
    w('### What step 6 changes')
    w()
    w(f"Of the HTRs that pass steps 3 to 5 in the sample, {pct(PS['shared'] / PS['htrs'], 0)} share their skeleton and (P, S, T, N) with at least one other, and step 6 drops {pct(PS['dropped'] / PS['htrs'], 0)} of all of them. "
      f"An HTR it keeps is within goal {one_in(kept, okkept)} times, one it drops {one_in(PS['dropped'], PS['ok_dropped'])}.")
    w()
    w('This table shows the meta without step 6 and with it, with the corner-case-aware bound. Found within 10 is the chance of a within-goal finish among the first 10 HTRs finished, in the order of the next section. '
      'The last column is a variation that drops nothing: among variants with the same (P, S, T, N), the ones with the most pairs are finished first. Its HTRs to finish and its chance of missing are those without step 6.')
    w()
    w('| Corner case | HTRs to finish per DR without step 6 (median) | HTRs to finish per DR with step 6 (median) | Chance of missing without step 6 | Chance of missing with step 6 | Found within 10 without step 6 | Found within 10 with step 6 | Found within 10, most pairs first and nothing dropped |')
    w('|---|---|---|---|---|---|---|---|')
    for k in ORDER:
        b = C[k]['bounds']['cca']; o = C[k]['orders']
        w(f"| {k} | {num(b['htr_med0'])} | {num(b['htr_med'])} | {pct(b['miss0'])} | {pct(b['miss'])} | {pct(o['cca_pst_3_nopairs'][1], 0)} | {pct(o['cca_pst_3'][1], 0)} | {pct(o['cca_pstp_3_nopairs'][1], 0)} |")
    w()
# (without a step 6 the pairs only change the order of finishing, and this page keeps the order fixed: what the pairs
# are worth in it is in the comparison with the standard meta, mkstd.py)

# ---- what the cap on the moves to HTR changes
HC = {k: C[k]['hcap'] for k in ORDER}
assert all(J[m]['hcap']['on'] for m in (2, 3, 4)), 'the page is written for the cap on the moves to HTR (SVM_HCAP=1)'
w('### What the cap on the moves to HTR changes')
w()
hl = sum(HC[k]['lost'] for k in ORDER); hlb = sum(HC[k]['lost_base'] for k in ORDER)
hcut = [1 - C[k]['bounds']['cca']['htr_med'] / HC[k]['htr_med0'] for k in ORDER]
w('An HTR that is G moves away is within goal only when it solves the DR as it stands. Step 3 leaves those out. '
  f"That takes {pct(min(hcut), 0)} to {pct(max(hcut), 0)} off the HTRs to finish, and "
  + ('loses no within-goal DR of the sample: every DR with such a solution has a nearer within-goal HTR that the meta finishes.' if hl == 0 else
     f"loses {hl} of the sample's {WG:,} within-goal DRs.")
  + (f" Without the premove pass it would lose {sum(HC[k]['lost_nopass'] for k in ORDER)}." if PASS else ''))
w()
w('This table shows the meta with the corner-case-aware bound, with HTRs at any distance and with the cap.')
w()
w('| Corner case | HTRs to finish per DR, any distance (median) | HTRs to finish per DR, at most G−1 moves (median) | Within-goal DRs lost |')
w('|---|---|---|---|')
for k in ORDER:
    w(f"| {k} | {num(HC[k]['htr_med0'])} | {num(C[k]['bounds']['cca']['htr_med'])} | {HC[k]['lost']} |")
w()

# ---- what the premove pass changes
if PASS:
    w('### What the premove pass changes')
    w()
    WGK = {k: C[k]['wg'] for k in ORDER}
    tot = {v: sum(V3[k][v]['wg'] - V3[k][v]['found'] for k in ORDER) for v in ('none', 'written', 'added')}
    lostw = sum(V3[k]['written']['lost'] for k in ORDER); gainw = sum(V3[k]['written']['gained'] for k in ORDER); gaina = sum(V3[k]['added']['gained'] for k in ORDER)
    assert tot['written'] == tot['none'] + lostw - gainw and tot['added'] == tot['none'] - gaina
    w(f"The pass finds within-goal DRs that the linear check misses under the caps: {gaina} of the sample's {WG:,}. "
      f"Without it the meta would miss {tot['none']:,} of them ({pct(tot['none'] / WG)}), and with it {tot['added']:,} ({pct(tot['added'] / WG)}). "
      f"With the pass in place of the linear check of that side, as the doc has it, it would miss {tot['written']:,} ({pct(tot['written'] / WG)}): "
      + (f"the same {gainw} gained, and {lostw} lost." if gainw == gaina else f"{gainw} gained and {lostw} lost."))
    w()
    w('This table shows the chance of missing a within-goal finish in the three versions. Lost and gained count within-goal DRs against the meta with no pass.')
    w()
    w('| Corner case | Within-goal DRs | Missed, no pass | Missed, pass instead of linear | Lost, pass instead of linear | Gained by the pass | Missed, pass and linear (the meta) |')
    w('|---|---|---|---|---|---|---|')
    for k in ORDER:
        v = V3[k]
        # what the pass finds is the same whether or not the full search follows (and more with the pass on both sides)
        assert set(v['written']['gained_drs']) <= set(v['added']['gained_drs']) and (BOTH or v['written']['gained_drs'] == v['added']['gained_drs'])
        w(f"| {k} | {v['none']['wg']:,} | {pct(v['none']['miss'])} | {pct(v['written']['miss'])} | {v['written']['lost']} | {v['added']['gained']} | {pct(v['added']['miss'])} |")
    w(f"| All | {WG:,} | {pct(tot['none'] / WG)} | {pct(tot['written'] / WG)} | {lostw} | {gaina} | {pct(tot['added'] / WG)} |")
    w()
    e = EX['premove_lost']
    assert all(V3[k]['written']['lost_all_after'] for k in ORDER if V3[k]['written']['lost'])
    rng = [V3[k]['written']['lost_after'] for k in ORDER if V3[k]['written']['lost']]
    lo_, hi_ = min(r[0] for r in rng), max(r[1] for r in rng)
    w('**Why the pass alone loses DRs.** What is left after the premove only holds the solutions that end on that quarter turn. '
      'A solution that goes on after it, with a slice or a corner swap, is not among them, and on the other side those moves come before 2qt. '
      f"All {lostw} lost DRs are of that kind: every within-goal solution the linear check finds for them has {lo_} to {hi_} moves after the last quarter turn of a skeleton that ends in HH. "
      f"For example, on the {e['case']} DR `{e['scramble']}`, the only within-goal solution the meta finishes is `{e['solution']}` on {e['side']}, which reads {e['tuple']}. "
      f"Its skeleton ends with the `{e['turn']}`, and {e['after_kind']} `{e['after']}` comes after. On {e['other_side']} it reads {e['other']}: {e['other_P']} extra moves before 2qt, so it isn't found there. "
      f"With the `{e['turn']}` as a premove, what is left has no solution within the goal.")
    w()
    w('This table shows the work and how soon a finish is found: the HTRs to finish per DR (median), and the chance of a within-goal finish among the first 10 HTRs finished, in the order of the last table of this section.')
    w()
    w('| Corner case | HTRs to finish, no pass | HTRs to finish, pass instead of linear | HTRs to finish, pass and linear | Within 10, no pass | Within 10, pass instead of linear | Within 10, pass and linear |')
    w('|---|---|---|---|---|---|---|')
    for k in ORDER:
        v = V3[k]
        w(f"| {k} | {num(v['none']['htr_med'])} | {num(v['written']['htr_med'])} | {num(v['added']['htr_med'])} | {pct(v['none']['within'][1], 0)} | {pct(v['written']['within'][1], 0)} | {pct(v['added']['within'][1], 0)} |")
    w()

# ---- skeletons and routes
w('### Where the skeletons and routes come from')
w()
w('Most of a DR\'s skeletons have two more quarter turns than the DR, and that is where most routes to 2qt are. '
  'Some of those have a cancelling pair: two quarter turns with nothing between them in the skeleton, like the `D\' U` of the example at the top. '
  f"The counts are medians per DR over both sides, before the bound{' and before step 6' if DROP else ''}, so the parts don\'t add up exactly to the totals of the tables above."
  + (' The routes of the premove pass are counted too, under the quarter turns of the whole skeleton, premove included. '
     'A left-over skeleton that again ends with its last quarter turn counts as a cancelling pair, since the premove comes right after that turn. '
     'Skeletons are counted in the linear check only.' if PASS else ''))
w()
w('| Corner case | Skeletons, own quarter turns | Skeletons, two more, no cancelling pair | Skeletons, two more, cancelling pair | Routes to 2qt, own quarter turns | Routes to 2qt, two more, no cancelling pair | Routes to 2qt, two more, cancelling pair | Missed without the cancelling pairs |')
w('|---|---|---|---|---|---|---|---|')
for m, k in ALL:
    x = SP[k]
    w(f"| {k} | {num(x['own']['skeletons'])} | {num(x['more_plain']['skeletons'])} | {num(x['more_pair']['skeletons'])} | {num(x['own']['routes'])} | {num(x['more_plain']['routes'])} | {num(x['more_pair']['routes'])} | {pct(x['no_pair']['miss'])} |")
w()

# ---- found within K
w('### Found within K finishes')
w()
w('Here are the chances of finding a within-goal solution within the first several HTRs, in the order of step 6: fewest moves to HTR first, and the most pairs first among HTRs equally far.')
w()
fw = {k: (C[k]['orders']['cca_len'], C[k]['orders']['none_len']) for _, k in ALL}
br = [fw[k][0][j] / fw[k][1][j] for k in ORDER for j in (1, 2)]
w(f'Compared to the baseline, using DR bounding boosts the chances of success within 10 or 20 finishes by {min(br):.1f}x-{max(br):.1f}x.')
w()
w(f'The order is the same in every table of this page, and it is the standard meta\'s; only what is discarded changes. [{STD_TITLE}]({STD_LINK}) compares it with going through one skeleton at a time, compares the caps of step 3 with a cap on the moves to HTR alone, and looks at what more NISS would add.')
w()
w('| Corner case | Meta, within 5 | Meta, within 10 | Meta, within 20 | Baseline, within 5 | Baseline, within 10 | Baseline, within 20 |')
w('|---|---|---|---|---|---|---|')
for k in ORDER:
    a, b = fw[k]
    w(f'| {k} | ' + ' | '.join(pct(v, 0) for v in a) + ' | ' + ' | '.join(pct(v, 0) for v in b) + ' |')
w()

# ------------------------------------------------------------------------------------------------------- appendix A
w('## Appendix A. Varying the bound')
w()
w(f'[*Advanced DR Bounding*]({DOC}) doc ')
w('defines three estimates for the lower bound: simple, corner-case-aware, and comprehensive. We have chosen')
w('the middle one. Each level prunes the HTRs by a factor of roughly 2x, at the cost of more complicated recognition,')
w('but the biggest jump is between using any type of DR Bounding vs. none.')
if DROP: w('Step 6 compares variants with the same N, so each bound makes its own groups' + ('.' if BASE_STEP else ', and the baseline has no step 6.'))
w()
for m in (2, 3, 4):
    w(f'### {m}qt DRs (goal {GOAL[m]})')
    w()
    for k in BYQT[m]:
        c = C[k]; B = c['bounds']
        sh = {b: B[b]['nok'] / B[b]['n'] for b in B}
        w(f"**{k}** · {who(c)}. Corner-case-aware makes a finished HTR {sh['cca'] / sh['none']:.1f}× likelier to be within goal than the baseline does; "
          f"comprehensive adds {sh['comp'] / sh['cca']:.1f}× on top.")
        w()
        w('| Bound | HTRs to finish per DR (median) | Within goal | Chance of missing a within-goal finish |')
        w('|---|---|---|---|')
        for b in ('none', 'simple', 'cca', 'comp'):
            nm = f'**{BN[b]}**' if b == 'cca' else BN[b]
            w(f"| {nm} | {num(B[b]['htr_med'])} | {one_in(B[b]['n'], B[b]['nok'])} | {pct(B[b]['miss'])} |")
        w()

# ------------------------------------------------------------------------------------------------------- appendix B
w('## Appendix B. Varying the caps')
w()
w(f"The cap on P+S+T of step 3 and the rule of step 4 come from a sweep. A rule is P ≤ 1, the goal, at most G−1 moves to HTR, step 4 on or off, and up to three caps taken from "
  f"S, T, N, P+S, S+T, T+N, P+S+T, S+T+N and P+S+T+N, each set to anything from 0 to 8: {OPT['nrules']:,} rules in all. "
  f"Each one was scored on every corner case with the corner-case-aware bound{', with step 6 applied to what the rule lets through' if DROP else ''}.")
w()
w('This table compares a few of them with the rule that has no cap and no step 4. HTRs to finish is the mean per DR as a share of that rule\'s, '
  'averaged over the six corner cases with at least 100 within-goal DRs (a geometric mean). Extra misses are points added to the chance of missing a within-goal finish.')
w()
w('| Rule on top of P ≤ 1 and the goal | HTRs to finish, against no cap | Extra misses, average | Extra misses, worst corner case |')
w('|---|---|---|---|')
for r in OPT['rows']:
    if SAME_CAPS and ('best two' in r['name'] or 'best three' in r['name']): continue
    w(f"| {r['name']} | {r['work']} | {r['mean']} | {r['worst']} |")
w()
w('What the sweep says:')
w()
if lost4 == lost40 and gain4 == 0:
    w(f"- **Step 4 {'costs nothing' if lost4 == 0 else 'costs little'}.** With P+S+T ≤ 5 in place, {step4_txt()[0].lower() + step4_txt()[1:]}. With no cap{' and step 6' if DROP else ''} it loses {OPT['floor_lost']}.")
else:
    w(f"- **Step 4 {'costs nothing' if lost40 == 0 else 'costs little'} on its own, and more with step 6.** With P+S+T ≤ 5 in place and no step 6, it loses "
      + ('no within-goal DR of the sample' if lost40 == 0 else f"{lost40} of the sample's {WG:,} within-goal DRs")
      + f". With step 6 it loses {lost4} of the {WG:,}, because a variant it leaves to the other side can be dropped there for one with more pairs"
      + (f" (it also finds {gain4} that step 6 drops without it)" if gain4 else '')
      + f". With no cap and step 6 it loses {OPT['floor_lost']}.")
w('- **One cap on P+S+T is enough.** ' + ('Among the rules that miss no more than the meta in any corner case, none with two or three caps finishes fewer HTRs than P+S+T ≤ 5 alone.' if SAME_CAPS else
  f"Among the rules that miss no more than the meta in any corner case, the best with two or three caps finishes {pct(1 - min(OPT['best2'], OPT['best3']) / OPT['meta_work'], 0)} fewer HTRs than P+S+T ≤ 5 alone (the two rows of the table that name them)."))
w('- **Caps that include N don\'t pay.** N is read off the bound at 2qt for free, and a variant with a big N is already discarded by the goal. '
  f"S+T+N ≤ 5 and T+N ≤ 4 finish about as many HTRs as P+S+T ≤ 5, and miss {pct(C['4b2']['var']['stn5']['miss'])} and {pct(C['4b2']['var']['tn4']['miss'])} of the time on 4b2 "
  f"instead of {pct(C['4b2']['var']['pst5']['miss'])}: a short skeleton leaves room for a long finish.")
g5 = GF['caps']['5']
finer = [g5[f] for f in ('spare', 'qps', 'spn', 'qpsn', 'cells')]
w(f"- **Finer caps don't help either.** The sweep's caps are the same for every skeleton. Caps on P+S+T that change with the spare moves, with P, with the skeleton's quarter turns or with the bound's N, "
  f"and arbitrary sets of (quarter turns, spare moves, P, S, T, N), were fitted on half of the DRs and scored on the other half, over {len(GF['seeds'])} random splits. "
  f"At the misses of P+S+T ≤ 5, the single cap finishes {pct(g5['const'], 0)} of the HTRs that step 4 alone does on the held-out half, and the finer rules {pct(min(finer), 0)} to {pct(max(finer), 0)}.")
w()
w('The tables below show the stats of each corner case with different caps, using the corner-case-aware bound. The meta\'s row is in bold. '
  + ('Every row has step 6 except the one that says otherwise. ' if DROP else '')
  + f"Skeletons and routes to 2qt are counted before the bound{' and before step 6' if DROP else ''}, so they only change with the caps.")
w()
ROWS = [('pmax1', 'P ≤ 1'), ('floor', 'P ≤ 1, step 4'), ('pst3', 'P ≤ 1, step 4, P+S+T ≤ 3'), ('pst4', 'P ≤ 1, step 4, P+S+T ≤ 4'),
        ('pst5', '**P ≤ 1, step 4, P+S+T ≤ 5**'), ('pst6', 'P ≤ 1, step 4, P+S+T ≤ 6'), ('nofloor', 'P ≤ 1, P+S+T ≤ 5, without step 4'),
        ('nopairs', 'P ≤ 1, step 4, P+S+T ≤ 5, without step 6'),
        ('p0', 'P = 0, step 4, P+S+T ≤ 5'), ('p2', 'P ≤ 2, step 4, P+S+T ≤ 5'), ('pany', 'Any P, step 4, P+S+T ≤ 5'),
        ('tn4', 'P ≤ 1, step 4, T+N ≤ 4'), ('stn5', 'P ≤ 1, step 4, S+T+N ≤ 5'),
        ('spare2', 'The meta on skeletons with 2 or more spare moves'), ('p1own', 'The meta with P = 0 on skeletons with two more quarter turns'),
        ('nopair', 'The meta without skeletons that have a cancelling pair'), ('own', 'The meta on skeletons with the DR\'s own quarter turns only'), ('doc', 'P ≤ 1, P+S+T+N ≤ 5, without step 4 (the doc\'s S+T+N ≤ min(G−L, 5) − P)')]
for m in (2, 3, 4):
    w(f'### {m}qt DRs (goal {GOAL[m]})')
    w()
    for k in BYQT[m]:
        c = C[k]; V = c['var']
        a, b, p2 = V['pst4'], V['pst5'], V['p2']
        s1 = (f"P+S+T ≤ 4 misses no more often ({pct(a['miss'])})" if abs(a['miss'] - b['miss']) < 5e-4 else
              f"P+S+T ≤ 4 misses {pct(a['miss'])} of the time instead of {pct(b['miss'])}")
        same_miss = abs(p2['miss'] - b['miss']) < 5e-4
        cost = f"{num(p2['htr_med'])} HTRs instead of {num(b['htr_med'])} and {num(p2['routes_med'])} routes to 2qt instead of {num(b['routes_med'])}"
        if same_miss and p2['htr_med'] == b['htr_med'] and p2['routes_med'] == b['routes_med']: s2 = 'a second pre-2qt move changes nothing'
        elif same_miss: s2 = f'a second pre-2qt move finds nothing more, for {cost}'
        else: s2 = f"a second pre-2qt move takes it to {pct(p2['miss'])}, for {cost}"
        w(f"**{k}** · {who(c)}. {s1}; {s2}.")
        w()
        w('| Rule | Skeletons per DR (median) | Routes to 2qt per DR (median) | HTRs to finish per DR (median) | Within goal | Chance of missing a within-goal finish |')
        w('|---|---|---|---|---|---|')
        for key, nm in ROWS:
            if key == 'nopairs' and not DROP: continue
            v = V[key]
            bold = key == 'pst5'
            cells = [num(v['skel_med']), num(v['routes_med']), num(v['htr_med']), one_in(v['n'], v['nok']), pct(v['miss'])]
            if bold: cells = [f'**{x}**' for x in cells]
            w(f"| {nm} | " + ' | '.join(cells) + ' |')
        w()

# ------------------------------------------------------------------------------------------------------- appendix C
w('## Appendix C. Data and method')
w()
w('Every number above comes from an exhaustive search of random DRs, with each HTR\'s finish taken from an exact table.')
w()
CK = dict(htrs=f"{sum(MR[m]['htrs'] for m in '234'):,}", dp_routes=f"{sum(MR[m]['dp_routes'] for m in '234'):,}", mirror=f"{sum(MR[m]['mirror'] for m in '234'):,}",
          wg=sum(MR[m]['within_goal_htrs'] for m in '234'), nomirror=sum(MR[m]['no_mirror'] for m in '234'))
assert all(MR[m]['dp_differ'] == 0 and MR[m]['mirror_bad'] == 0 for m in '234')
w('- **Sample.** 2,000 uniformly random DR states each with 2, 3 and 4 quarter turns to HTR. 40 of the 2qt states are 0c0 up to a turn of both layers and are dropped, leaving 1,960.')
w('- **Search.** On both sides, every HTR in reach with the DR\'s quarter turns or two more, up to 6. In reach means the moves to HTR plus the corner moves left after it fit the goal. '
  f"That's {CK['htrs']} HTRs" + (f", and the premove pass adds {sum(J[m]['hcap']['reach_pre'] for m in (2, 3, 4)):,}" if PASS else '')
  + f". Of those, {sum(J[m]['hcap']['kept'] + J[m]['hcap']['kept_pre'] for m in (2, 3, 4)):,} are at most G−1 moves away. Every table is counted on these, with its own caps on top.")
w('- **Finish.** The shortest leave-slice finish in half turns from that HTR, from an exact table. An HTR is within goal when its moves plus that finish fit the goal.')
w('- **Reading a solution.** A solution is cut at its quarter turns into sections. The skeleton of a section is the fewest half turns that do the same to the corners, '
  'up to a corner swap of the side axes (`R2 F2 R2`), a slice, and a U2 or D2 next to a quarter turn, which only turns that quarter turn the other way. '
  'L is the quarter turns plus those moves, and a section\'s extra moves are its length minus its skeleton\'s. '
  'P is the extra moves of the sections before 2qt, S of the setup at 2qt, T of the trigger and N of the finish. '
  'Two HTRs are on the same skeleton when they are in the same corner case at every quarter turn.')
w(f"- **Checks of that reading.** On {CK['dp_routes']} skeletons (the first 100 DRs of each sample), L is the length of the shortest corner-only path through the same corner cases at each quarter turn. "
  f"All {CK['mirror']} within-goal solutions of those DRs read as mirror images on normal and inverse. "
  f"Over the whole sample, all but {CK['nomirror']} of the {CK['wg']:,} within-goal HTRs have their mirror image among the other side's HTRs.")
w('- **Step 4 on a 6qt skeleton.** S+T+N ≥ P, not counting an extra move in the skeleton\'s middle section, which the inverse also reads as its middle.')
if PASS:
    w('- **Premove pass.** On each side, a quarter turn is made first on the other side, and every HTR of what is left is listed on skeletons with one quarter turn fewer than the DR or one more, '
      'so the whole skeleton, premove included, has the DR\'s quarter turns or two more. The premove is made all four ways, on the U or the D layer and in either direction. The same paths reach HTR each time, '
      'so a path counts as one HTR with the best of its four finishes. '
      'P, S, T and N are read on the left-over skeleton, with the cap, the bound and the goal as in steps 3 and 5. L and the solution\'s length count the premove. '
      'Step 4 is not applied, because only one side of what is left is searched. '
      'A left-over skeleton that again ends with its last quarter turn is gone through like any other, with no second premove. '
      'A left-over path that is solved at its last quarter turn is left out: with the premove it ends on two U/D quarter turns in a row, which is a solution of the skeleton two quarter turns shorter. '
      + ('A skeleton that starts and ends with a quarter turn gets the pass on both sides. ' if BOTH else
         'On normal, left-over skeletons that start with a quarter turn are left out, since that pass is made on inverse. ') +
      'A solution that ends on its last quarter turn is reached twice, in the pass and linearly, and counts as an HTR in each.')
w('- **Pairs.** A pair is a corner and an edge next to each other in the U or D layer with both stickers matching, so there are 0 to 16. '
  'A variant\'s pairs are counted right after its last insertion: on the state just before the quarter turn that closes its last section with extra moves, '
  'or just before its last quarter turn when it has no extra moves. A quarter turn of U or D keeps the count, and so does turning D where the variant turns U. '
  'Every pair count printed on this page was counted again on the stickers.')
if DROP:
    w('- **Step 6.** Variants are compared within one skeleton (one side of one DR, the same corner cases at every quarter turn) and one (P, S, T, N), with the N the bound gives. '
      'The most pairs are taken among the variants that pass steps 3 to 5.')
w('- **Order of finishing.** By moves to HTR, fewest first, over all the DR\'s skeletons on both sides' + (' and the premove pass, whose premove counts as a move' if PASS else '')
  + '. Among HTRs equally far, the ones with the most pairs go first' + ('' if BASE_STEP else ' (the baseline doesn\'t count them)')
  + '. Ties are taken in random order, and the found-within-K shares are averages over 20 such orders.')
w('- **Routes to 2qt.** Distinct move sequences, on either side, up to the point where the skeleton has 2 quarter turns left, that lead to at least one HTR the table\'s limits allow. '
  + ('They\'re counted before any bound and before step 6, so they don\'t depend on either: the insertions have to be made before their pairs can be compared.' if DROP else
     'They\'re counted before any bound, so they don\'t depend on it.'))
w('- **Skeletons.** Counted the same way: the skeletons with at least one HTR the table\'s limits allow, before any bound' + (' and before step 6.' if DROP else '.')
  + (' They are counted in the linear check only: a skeleton of the premove pass is a skeleton of the DR with its last quarter turn made first.' if PASS else ''))
w()
w('### Changes from the 19 Nov version')
w()
o4, o2 = OLD['4b2'], OLD['2c3']
n4, n2 = C['4b2'], C['2c3']
# what the own-skeleton reading changed, without what the premove pass adds on top
# (and without the cap on the moves to HTR, which the pass makes up for)
assert PASS
OWN4, OWN2 = [(c['hcap']['miss_nopass0'], c['hcap']['routes_med_nopass0']) for c in (n4, n2)]
w('- **P is its own number**, as in the doc. Before, the moves before 2qt were counted inside S.')
w('- **Every solution is read against its own skeleton.** Before, extra moves were counted against the shortest corner path with the same quarter turns and the same NISS@1qt corner case, '
  'so a solution on a longer corner route looked like a variant with extra moves, often before 2qt. Now that route is a skeleton of its own, with a longer L and fewer spare moves. '
  f"More solutions fit P ≤ 1 this way, so, before the premove pass and the cap on the moves to HTR, the meta misses less (4b2 {pct(OWN4[0])} instead of {o4['miss']}, 2c3 {pct(OWN2[0])} instead of {o2['miss']}) "
  f"and has more routes to 2qt to go through (4b2 {num(OWN4[1])} instead of {o4['routes']}, 2c3 {num(OWN2[1])} instead of {o2['routes']}).")
w('- **Step 4 is new.**')
if DROP:
    w(f"- **Step 6 is new.** It takes the HTRs to finish per DR from {num(n4['bounds']['cca']['htr_med0'])} to {num(n4['bounds']['cca']['htr_med'])} on 4b2 and from {num(n2['bounds']['cca']['htr_med0'])} to {num(n2['bounds']['cca']['htr_med'])} on 2c3, "
      f"and the chance of missing from {pct(n4['bounds']['cca']['miss0'])} to {pct(n4['bounds']['cca']['miss'])} and from {pct(n2['bounds']['cca']['miss0'])} to {pct(n2['bounds']['cca']['miss'])} (section 2).")
else:
    ob = lambda k, key: pct(C[k]['orders'][key][1], 0)
    w('- **The order of finishing is new.** HTRs are finished by moves to HTR, fewest first, and the most pairs first among HTRs equally far. '
      'Before, the skeletons were gone through shortest first and each skeleton\'s variants by fewest P+S+T, at most 3 per skeleton in a first pass. '
      f"On the HTRs the meta finishes now, that order finds a within-goal finish within 10 for {ob('4b2', 'cca_before')} of 4b2's within-goal DRs and {ob('2c3', 'cca_before')} of 2c3's, "
      f"and the new one for {ob('4b2', 'cca_len')} and {ob('2c3', 'cca_len')} ({ob('4b2', 'cca_len_nopairs')} and {ob('2c3', 'cca_len_nopairs')} without the pairs).")
if PASS:
    u4, u2 = n4['uniss'], n2['uniss']
    w(f"- **The premove pass is new.** With the cap on the moves to HTR in place, it takes the chance of missing from {pct(u4['miss0'])} to {pct(n4['bounds']['cca']['miss'])} on 4b2 and from {pct(u2['miss0'])} to {pct(n2['bounds']['cca']['miss'])} on 2c3, "
      f"and the HTRs to finish per DR from {num(u4['htr_med0'])} to {num(n4['bounds']['cca']['htr_med'])} and from {num(u2['htr_med0'])} to {num(n2['bounds']['cca']['htr_med'])} (section 2).")
w(f"- **The cap on the moves to HTR is new.** HTRs G moves away are left out. It takes the HTRs to finish per DR from {num(n4['hcap']['htr_med0'])} to {num(n4['bounds']['cca']['htr_med'])} on 4b2 "
  f"and from {num(n2['hcap']['htr_med0'])} to {num(n2['bounds']['cca']['htr_med'])} on 2c3, and "
  + ('loses no within-goal DR of the sample' if hl == 0 else f"loses {hl} of the sample's within-goal DRs") + ' (section 2).')

w()
w('### Left out of the meta')
w()
w('- **Reflection penalties.** The doc\'s "+2 per reflected slice" terms aren\'t tracked here.')
w('- **cs-parity.** Only the comprehensive bound needs it, and checking it during a solve is slow.')
open(sys.argv[1], 'w').write('\n'.join(out) + '\n')
print('written', sys.argv[1], len(out), 'lines')
