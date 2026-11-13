#!/usr/bin/env python3
"""Writes tables/half-turns-before-first-qt.md: for every subset x edges, how many half turns an optimal finish needs
before its first quarter turn, on the better of the two sides and on normal alone, for all DRs and for DRs whose
optimal is at most 13 or at most 12.

Data: the HTR-routes study's sample (htr-routes/research/out/big/run1/states_*.tsv, 25,000 uniformly random DR states
per subset x edges; git-ignored, rebuilt by htr-routes/research/run_all.sh).  Columns used: d (optimal finish, from the
exact table of all DR states), ht_first_n / ht_first_i (fewest moves before the first quarter turn over every optimal
finish, read from its first move / from its last move).  Pooled rows weight each subset x edges by its exact size.
The sections on what predicts it, on a finish within one move of the optimal and on U2 / D2 are rendered from
htr-routes/research/out/ht_first_extra.json and ht_first_witness.json (written by htr-routes/research/src/xhtfirst.py
and ht_first_witness.py from a second, independent count; see the block before `doc`).
usage: python3 tables/src/half_turns_before_first_qt.py   (from the repository root, with env.sh sourced)"""
import os, sys, json
import numpy as np
ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'htr-routes', 'research', 'src'))
from common import SUBS, CGROUPS, CORNER, SIZE, load_states   # noqa: E402

def pc(x):
    if x == 0: return '0%'
    if x < 0.0005: return '<0.1%'
    return f'{100 * x:.1f}%'
def dist(v, w):
    tot = w.sum()
    return [float(w[v == k].sum() / tot) for k in (0, 1, 2)] + [float(w[v >= 3].sum() / tot)]

ST = {s: load_states(s) for s in SUBS}
N = len(ST[SUBS[0]]['d'])
def rows(cut):
    """(label, share qualifying, DRs in the sample, better-side distribution, normal-side distribution)"""
    out, acc = [], {}
    for s in SUBS:
        t = ST[s]; m = t['d'] <= cut if cut else np.ones(len(t['d']), bool)
        b = np.minimum(t['ht_first_n'], t['ht_first_i'])[m]; n = t['ht_first_n'][m]
        w = np.full(int(m.sum()), SIZE[s] / len(t['d']))
        out.append((s, float(m.mean()), int(m.sum()), dist(b, np.ones(len(b))), dist(n, np.ones(len(n)))))
        for g in (CORNER(s), 'all DRs'): acc.setdefault(g, []).append((b, n, w, SIZE[s]))
    pooled = []
    for g in list(CGROUPS) + ['all DRs']:
        b = np.concatenate([x[0] for x in acc[g]]); n = np.concatenate([x[1] for x in acc[g]])
        w = np.concatenate([x[2] for x in acc[g]])
        pooled.append((g, float(w.sum() / sum(x[3] for x in acc[g])), len(b), dist(b, w), dist(n, w)))
    return out, pooled

def table(rs, first, share):
    head = [first] + (['Share of its DRs that short', 'DRs in the sample'] if share else []) + \
           ['0 half turns', '1 half turn', '2 half turns', '3 or more'] + \
           ['Normal side alone: 0', 'Normal side alone: 1', 'Normal side alone: 2', 'Normal side alone: 3 or more']
    L = ['| ' + ' | '.join(head) + ' |', '|' + '---|' * len(head)]
    for lab, sh, k, b, n in rs:
        L.append('| ' + ' | '.join([lab] + ([pc(sh), f'{k:,}'] if share else []) + [pc(x) for x in b] + [pc(x) for x in n]) + ' |')
    return '\n'.join(L)

ALL, ALLP = rows(None); R13, P13 = rows(13); R12, P12 = rows(12)
g = lambda rs, lab: next(r for r in rs if r[0] == lab)
two = lambda r: r[3][2] + r[3][3]
ex = [g(ALL, '2c4 2e'), g(R13, '2c4 2e'), g(R12, '2c4 2e')]
exl = ['all its DRs', f'optimal ≤ 13 ({pc(ex[1][1])} of 2c4 2e)', f'optimal ≤ 12 ({pc(ex[2][1])} of 2c4 2e)']
EX = '\n'.join(['| 2c4 2e | 0 half turns | 1 half turn | 2 half turns | 3 or more |', '|---|---|---|---|---|'] +
               [f'| {l} | ' + ' | '.join(pc(x) for x in r[3]) + ' |' for l, r in zip(exl, ex)])
allr = [g(ALLP, 'all DRs'), g(P13, 'all DRs'), g(P12, 'all DRs')]
worst = sorted([r for r in R12 if r[0] != '0c0 0e'], key=two, reverse=True)[:4]   # 0c0 0e reads differently (see the page)
two_n = lambda r: r[4][2] + r[4][3]
none12 = [r[0] for r in P12 if r[0] != 'all DRs' and two(r) == 0]

# ---------------------------------------------------------------------------------------------------------------------
# What you can see that predicts it; a finish within one move of the optimal; U2 and D2 not counted.
# Numbers and tables: htr-routes/research/out/ht_first_extra.json (src/xhtfirst.py, from the second count of
# htr-routes/research/htfirst and the reads of src/ht_first.py), the worked DRs: out/ht_first_witness.json
# (src/ht_first_witness.py), the checks: out/checks/check_ht_first.txt and check_ht_first_reads.txt.
HO = os.path.join(ROOT, 'htr-routes', 'research', 'out')
J = json.load(open(os.path.join(HO, 'ht_first_extra.json')))
WIT = {w['id']: w for w in json.load(open(os.path.join(HO, 'ht_first_witness.json')))}
assert all(w['replayed_ok'] for w in WIT.values())
assert J['compare']['normal_differs'] == 0 and J['compare']['inverse_differs'] == 0     # the second count equals the columns used above
def chk(name):
    out = {}
    for l in open(os.path.join(HO, 'checks', name)).read().split('\n'):
        p = l.split('\t')
        if len(p) >= 2 and p[1].isdigit(): out[p[0]] = int(p[1])
    assert 'ALL EQUAL' in open(os.path.join(HO, 'checks', name)).read(), name
    return out
C1, C2 = chk('check_ht_first.txt'), chk('check_ht_first_reads.txt')
def T(name):
    t = J['tables'][name]
    return '\n'.join(['| ' + ' | '.join(t['head']) + ' |', '|' + '---|' * len(t['head'])] + ['| ' + ' | '.join(r) + ' |' for r in t['rows']])
def rd(grp, key, col, p='le13'):
    v = J['reads'][f'{grp}|{p}|{key}'][col]
    return f'{v:,}' if col == 'n' else pc(v)
def ds(grp, k, p='le13', tg='opt', side='either'):
    d = J['dist'][f'{grp}|{p}|{tg}|{side}']['d']
    return pc(d[2] + d[3] if k == '2+' else d[1] + d[2] + d[3] if k == '1+' else d[0] + d[1] if k == '<2' else d[k])
def sd(case, k, where='2c4 2e le13'): return J['side'][f'{case}|{where}']['d'][k]
def rng(vals): return f'{100 * min(vals):.0f}% to {100 * max(vals):.0f}%'
def half(k): return f'{k} half turn' + ('' if k == 1 else 's')
def looks(cs): return '; '.join(f"{J['setup_look'][f'{cs}|{k}'].replace('2-2, ', '2-2 with the ').replace('with the diagonal over diagonal', 'with a diagonal over a diagonal')}: {k}" for k in range(4))
def pair(name):
    a, b = name.split(' and ')
    return f'{a} on both sides' if a == b else name
def xq(sub):                # share of the subset where every optimal finish uses extra quarter turns (htr-routes, section 7)
    for l in open(os.path.join(ROOT, 'htr-routes', 'report', 'data', 'extra_qt.md')):
        c = [x.strip() for x in l.strip().strip('|').split('|')]
        if c[0] == sub: return c[1]
    raise KeyError(sub)
def wit(wid):
    w = WIT[wid]
    L = [f"{w['scramble']} // {w['sample'].split(' #')[0]}, {w['optimal']} optimal; corners {w['corner_case']['normal']} on normal, {w['corner_case']['inverse']} on inverse"]
    for i, f in enumerate(w['optimal_finishes']):
        L.append(f"{f['finish']} // {'optimal finish' if i == 0 else 'the other optimal finish' if len(w['optimal_finishes']) == 2 else 'optimal finish'}: "
                 f"{half(f['half_turns_before_first_qt_normal'])} before the first qt on normal, {f['half_turns_before_first_qt_inverse']} on inverse")
    return '```\n' + '\n'.join(L) + '\n```'
GOOD = ('2c4', '0c3', '4a2', '2c3', '4c3', '4c4')
LOW3 = ('2c5', '2c4', '0c3', '0c4', '4c3', '4c4', '4b5')         # corner subsets where 3 or more is rare
ready13 = {r[0]: r for r in J['tables']['ready_corner_le13']['rows']}
pcf = lambda s: float(s.rstrip('%')) / 100
P = J['pairs_2c4_2e']['le13']
nr_ready = [sd(c, 0) for c in ('2c4-1', '2c4-3', '2c4-5')]; nr_setup = [sd(c, 0) for c in ('2c4-4', '2c4-6', '2c4-7')]
READS = f"""## What you can see that predicts it

Before you solve anything you can read the corner case on normal and on inverse, where the bad edges sit, the pairs and the E slice. Measured against the tables above: the corner case tells you a lot about needing **one** half turn first, the bad-corner layout gives one usable rule for **two or more** (on 4a2), the pairs and the E slice tell you nothing, and where the bad edges sit next to nothing. Jay suggested the split in 2023 ([3 Nov 2023](https://discord.com/channels/1007840975726575667/1007841273111117924/1169972245620342794)): "4qt 2cxe could be divided into a bunch of mini cases ranging from needing 0 half turns on both sides of the scramble to make ideal qt progress, all the way to needing 2 half turns before you can do that ideal qt".

Below, *needs 1+* means that on both sides every optimal finish has at least one half turn before its first quarter turn, and *needs 2+* at least two. DRs with an optimal of 13 or less come first, all DRs after. The corner case names (2c4-3 and so on) and the column *A qt takes it straight to* are those of [*Judging a DR by hand*](../judging-a-dr/), appendix E.

**How far to look, whatever you see.** With an optimal of 13 or less, starting the first quarter turn after 0 or 1 half turns finds an optimal on {ds('all', '<2')} of DRs if you get the side right, and 0 to 2 half turns on {pc(1 - J['dist']['all|le13|opt|either']['d'][3])}. Noah Swor's rule ([2 Oct 2023](https://discord.com/channels/1007840975726575667/1007841273111117924/1158302491075690507): "also idk if this is a good rule but I only usually write at most 2 moves before the first quarter turn") loses the optimal on the other {ds('all', 3)}; that's {ds('4a1 4e', 3)} of 4a1 4e, {ds('4b2 2e', 3)} of 4b2 2e and {ds('4a2 4e', 3)} of 4a2 4e, and at most {pc(max(J['dist'][f'{s}|le13|opt|either']['d'][3] for s in SUBS if CORNER(s) in LOW3))} on every row of {', '.join(LOW3[:-1])} and {LOW3[-1]}.

### A ready side

Call a side **ready** when some U or D quarter turn, done right away, takes the corners to a subset with one quarter turn less: 2c4 to 2c3 or 4b3, 2c3 to 4b2, 4a2 to 4a1, 4a1 to 0c0. You see it by recognising the corner case on that side; the table [per corner case](#every-corner-case-one-side-at-a-time) says which cases are ready. On 2c4 the bad-corner layout alone doesn't tell you, because each of its three layouts has a ready case and one that needs a setup. 2c5, 0c4 and 4b5 are always ready and 0c0 has nothing to lower, so the read exists on eight corner subsets.

**Rule 1: if neither side is ready, expect a half turn before the first quarter turn.** DRs with an optimal of 13 or less, edge counts pooled. Each row is a corner subset. *Neither side ready* is the share of those DRs with the sign; the other cells are the shares needing 1+ and 2+, with the sign and without it:

{T('ready_corner_le13')}

On {', '.join(GOOD[:-1])} and {GOOD[-1]} the sign separates well for 1+: {rng([pcf(ready13[s][2]) for s in GOOD])} with it against {rng([pcf(ready13[s][3]) for s in GOOD])} without. On 4a1 and 4b2 it's weak ({ready13['4a1'][2]} against {ready13['4a1'][3]}, {ready13['4b2'][2]} against {ready13['4b2'][3]}): every optimal finish takes extra quarter turns on {xq('4a1')} of 4a1 and {xq('4b2')} of 4b2 ([*Which HTR routes to try from a DR*](../htr-routes/), section 7), so the finish often doesn't start where the corners say. For 2+ the sign is worth much less: {ready13['2c4'][4]} against {ready13['2c4'][5]} on 2c4.

2c4 2e. Each row is a group of its DRs:

{T('ready_2c4_2e')}

So on a 2c4 2e with an optimal of 13 or less: if neither side is ready, expect to need a half turn first, {rd('2c4 2e', 'neither', 'needs_1plus')} against {rd('2c4 2e', 'a side', 'needs_1plus')}.

The same on all DRs, where the sign is duller. It's a read about the DRs you'd keep:

{T('ready_corner_all')}

A 2c4 2e where neither side is ready, replayed. Both optimal finishes need half turns first on both sides:

{wit('H1')}

And one that's ready on normal only: there any U or D quarter turn takes the corners from 2c4 to 2c3, and both optimal finishes start with one.

{wit('H2')}

### One side at a time

The same read per side, which is how you'd use it: look at a side, know its odds. Each row is a corner case on one side of a 2c4 2e with an optimal of 13 or less (a DR gives two sides). The last four cells are the shares of such sides on which the optimal finishes, read from that side, reach their first quarter turn after exactly that many half turns:

{T('cases_2c4_2e_le13')}

A side that needs a setup starts with a quarter turn on {rng(nr_setup)} (finishes that go up a quarter turn first). A ready side starts with one on {rng(nr_ready)} (2c4-1, 2c4-3, 2c4-5), and on {pc(sd('2c4-2', 0))} for 2c4-2. On 2c4-3 and 2c4-5 it's a quarter turn at once or at least two half turns, almost never exactly one ({pc(sd('2c4-3', 1))} and {pc(sd('2c4-5', 1))}).

### Two or more: the 4a2 rule

On 4a2, 4a1 and 4b2 the corners can need up to three half turns before any quarter turn lowers them. On 4a2 the layout gives the count ({looks('4a2')}). Take the side that needs fewer.

4a2 4e with an optimal of 13 or less. Each row is that count; the last four cells are the shares of those DRs needing exactly that many half turns before the first quarter turn on the better side:

{T('setup_4a2_4e_le13')}

**Rule 2: on 4a2 4e, if on both sides the bad corners are 4-0 or 2-2 with the pairs on opposite sides, expect two or more half turns first: {rd('4a2 4e', 'setup2+', 'needs_2plus')} against {rd('4a2 4e', 'setup<2', 'needs_2plus')}.** That's with an optimal of 13 or less, where {rd('4a2 4e', 'setup2+', 'share')} have the sign ({rd('4a2 4e', 'setup2+', 'n')} DRs in the sample). With 12 or less it's {rd('4a2 4e', 'setup2+', 'needs_2plus', 'le12')} against {rd('4a2 4e', 'setup<2', 'needs_2plus', 'le12')} ({rd('4a2 4e', 'setup2+', 'n', 'le12')} DRs with the sign), and on all 4a2 4e {rd('4a2 4e', 'setup2+', 'needs_2plus', 'all')} against {rd('4a2 4e', 'setup<2', 'needs_2plus', 'all')}, with the sign on {rd('4a2 4e', 'setup2+', 'share', 'all')}.

The same sign, the corners needing 2 or 3 half turns on both sides, on every row where it exists. Optimal of 13 or less:

{T('setup_rule_le13')}

It carries over to 4a2 2e and 4b2 0e. On the other rows it's a slope, not a rule. For 4a1 the count is {looks('4a1')}. On 4b2 the layout isn't enough (3-1 is 1 or 2, pairs sharing one column 0 or 3), so there it takes the corner case.

All DRs:

{T('setup_rule_all')}

A 4a2 4e with the pairs on opposite sides on both sides, replayed:

{wit('H3')}

And one with 4-0 on both sides:

{wit('H5')}

### Two or more on 2c4 2e: nothing you can see

{ds('2c4 2e', '2+')} of 2c4 2e with an optimal of 13 or less need 2+. What moves that number:

- A ready side or not (rule 1): {rd('2c4 2e', 'neither', 'needs_2plus')} against {rd('2c4 2e', 'a side', 'needs_2plus')}.
- The two bad corners stacked, one above the other, on both sides: {rd('2c4 2e', 'stacked both', 'needs_2plus')} against {rd('2c4 2e', 'stacked not both', 'needs_2plus')}, but only {rd('2c4 2e', 'stacked both', 'share')} of them look like that ({rd('2c4 2e', 'stacked both', 'n')} DRs in the sample). Stacked on at least one side ({rd('2c4 2e', 'stacked a side', 'share')}): {rd('2c4 2e', 'stacked a side', 'needs_2plus')} against {rd('2c4 2e', 'stacked no side', 'needs_2plus')}.
- The exact pair of corner cases ({P['pairs']} pairs): from {pc(P['lowest_row']['needs_2plus'])} ({pair(P['lowest'])}, {P['lowest_row']['n']:,} DRs) to {pc(P['highest_row']['needs_2plus'])} ({pair(P['highest'])}, {P['highest_row']['n']:,} DRs). Picking the worst and the best pair on half the sample and reading them on the other half gives {pc(P['worst_heldout'])} ({pair(P['worst'])}, {P['worst_heldout_n']:,} DRs) and {pc(P['best_heldout'])} ({pair(P['best'])}, {P['best_heldout_n']:,} DRs).
- True pairs, slice pairs, the E slice: nothing measurable. Where the bad edges sit: next to nothing (second table below).

So the best a read does on 2c4 2e is single out one DR in fifty where the odds of 2+ are about two in five, and leave the rest near the base rate.

*Computer only*, to put a number on it: the share of the uncertainty about *needs 2+* that each read removes (mutual information as a share of the entropy, with the chance level of a read with that many values taken off), DRs with an optimal of 13 or less. Each column is a subset × edges:

{T('explained_2plus')}

Only 4a2 4e gets anywhere, through rule 2. The bad edges, *computer only* again: the same share for one side at a time (does this side need 2+), knowing its corner case, and knowing on top of that where every bad edge sits:

{T('explained_side_2plus')}

That's 1 to 5 points more, most on 4a2 4e and 4a1 4e, and it would take a table of hundreds of layouts to use. The last row of the first table shows why so little is visible: what decides it is mostly how many optimal finishes the DR has, and that can't be seen. *Computer only*, the share needing 2+ by the number of optimal finishes:

{T('nopt')}

A 2c4 2e that's ready on both sides and still needs two half turns first on both, replayed. Its two optimal finishes differ only in the order of the first two moves:

{wit('H4')}

### If you already have the HTRs

Not a read of a few seconds, but you find these anyway. Each row is a subset × edges and the length of the shorter of its two shortest HTRs (normal, inverse), among DRs with an optimal of 13 or less:

{T('htr_le13')}

A 4b2 2e with a 3- or 4-move HTR on a side almost never needs 2+: {rd('4b2 2e', 'htr short', 'needs_2plus')} against {rd('4b2 2e', 'htr long', 'needs_2plus')} ({rd('4b2 2e', 'htr short', 'share')} of them have one). On 4a1 4e it's the other way round: with a 3- or 4-move HTR {rd('4a1 4e', 'htr 3-4', 'needs_2plus')} need 2+, against {rd('4a1 4e', 'htr 5+', 'needs_2plus')} from 5 moves up and {rd('4a1 4e', 'htr 1-2', 'needs_2plus')} with 1 or 2. On 2c4 2e a 9-move shorter HTR means {rd('2c4 2e', 'htr 9+', 'needs_2plus')} against {rd('2c4 2e', 'htr 8-', 'needs_2plus')}.

### Every corner case, one side at a time

Each row is a corner case on one side, edge counts pooled, DRs with an optimal of 13 or less. The last four cells are the shares of such sides on which the optimal finishes, read from that side, reach their first quarter turn after exactly that many half turns. A case with an entry under *A qt takes it straight to* is ready.

{T('cases_le13')}

All DRs:

{T('cases_all')}

### Rule 1 on every subset × edges

Optimal of 13 or less. Same columns as the rule 1 table:

{T('ready_rows_le13')}

All DRs:

{T('ready_rows_all')}

## A finish within one move of the optimal

If a finish one move over the optimal will do, the half turns mostly stop mattering. Each row is a corner subset; each cell is the share of its DRs whose best start among all finishes of at most optimal + 1 moves has that many half turns before the first quarter turn, on the better side:

{T('p1_corner')}

With an optimal of 13 or less, {ds('all', '2+', 'le13', 'p1')} of DRs have no such finish starting its first quarter turn after 0 or 1 half turns, against {ds('all', '2+')} for the optimal itself. Every subset × edges:

{T('p1_rows')}

0c0 0e reads differently here too: its finishes with no quarter turn count as 3 or more.

## If U2 and D2 don't count

Count only R2, L2, F2 and B2 before the first quarter turn, so that `U2 R2 U` has one and not two. That changes the number on {pc(J['differs_side_count']['le13'])} of DRs with an optimal of 13 or less ({pc(J['differs_side_count']['all'])} of all DRs). The 0 column can't change. Over all subsets, each row is a group of DRs, with the shares needing exactly that many under each count:

{T('side_pop')}

So about a third of the *2 or more* moves down a column, and the picture stays: the rows that need the most are the same four, {', '.join(J['side_rank']['le13']['side_count'][:3])} and {J['side_rank']['le13']['side_count'][3]}. The tables on this page count every half turn, because that's the number of moves you write before the quarter turn. Both counts for every row are in `htr-routes/research/out/ht_first.tsv` in the repository.
"""
assert J['side_rank']['le13']['side_count'][:4] == J['side_rank']['le13']['all_count'][:4]
assert len(WIT['H2']['qt_that_lowers_now']['normal']) == 4 and not WIT['H2']['qt_that_lowers_now']['inverse']
assert all(f['half_turns_before_first_qt_normal'] == 0 for f in WIT['H2']['optimal_finishes'])
CHECKS = f"""**Checked.** A second program (`htr-routes/research/htfirst`: a search over half-turn starts against the same exact table, with the first program's cube model but none of its enumeration) gives the same number on all {J['compare']['states']:,} sampled DRs, on both sides. A third count in Python, with its own move tables, agrees on {C1['states']:,} DRs (the first 3,000 of 2c4 2e, 4a1 4e, 2c3 2e and 0c0 0e) and replays every optimal finish of {C1['sticker_states']:,} of them on a 54-sticker cube ({C1['sticker_finishes']:,} finishes, all solve). The within-one-move numbers come from the second program and agree with the third count on {C1['p1_states']:,} DRs. The reads: the half turns the corners need on each side were recomputed on the sticker cube for {C2['states']:,} DRs (60 of every subset × edges) and the corner case names by the first study's reader for {C2['drread_states']:,}, with no difference. Every example on this page is replayed on the sticker cube and re-read by that reader. Scripts: `htr-routes/research/src/ht_first.py`, `xhtfirst.py`, `check_ht_first.py`, `ht_first_witness.py`."""
doc = f"""# Half turns before the first quarter turn

From a DR, how many half turns does an optimal finish make before its first quarter turn, if you start on the better side? Per subset × edges, for all DRs and for the DRs that matter in an attempt: those with an optimal of 13 or less, or 12 or less.

**How it's counted.** Take every optimal finish of the DR (U, D, R2, L2, F2, B2) and count the moves before its first U or D quarter turn. They're all half turns; U2 and D2 count. Read each finish from its first move (normal) and from its last move (inverse) and keep the smaller number: that's *the better side*, chosen with hindsight. The *normal side alone* columns keep only the first reading. Sampled: {N:,} uniformly random DRs per subset × edges, each with every optimal finish from the exact table of all DR states, so a share is good to about ±0.3 points, more on the rows with few DRs (the tables give the count). November 2026.

**The short answer.**

- Over all DRs, {pc(allr[0][3][0])} need no half turn first, {pc(allr[0][3][1])} need one, and {pc(two(allr[0]))} need two or more. Among DRs with an optimal of 13 or less it's {pc(two(allr[1]))} that need two or more, and with 12 or less {pc(two(allr[2]))}.
- It depends on the subset and on the edge count. With an optimal of 12 or less, two or more half turns first are needed on {pc(two(worst[0]))} of {worst[0][0]}, {pc(two(worst[1]))} of {worst[1][0]}, {pc(two(worst[2]))} of {worst[2][0]} and {pc(two(worst[3]))} of {worst[3][0]}, and on none of the sampled DRs of {', '.join(none12[:-1])} or {none12[-1]}.
- Checking both sides matters: on the normal side alone, {pc(two_n(allr[0]))} of all DRs need two or more, against {pc(two(allr[0]))} on the better side.
- What you can see: the corner case says whether to expect **one** half turn first. Call a side ready when a quarter turn takes its corners straight down a quarter turn. A 2c4 2e with an optimal of 13 or less needs a half turn first on {rd('2c4 2e', 'neither', 'needs_1plus')} if neither side is ready, against {rd('2c4 2e', 'a side', 'needs_1plus')} if one is. Needing **two or more** barely shows: only 4a2 has a usable sign, the bad-corner layout on both sides ({rd('4a2 4e', 'setup2+', 'needs_2plus')} against {rd('4a2 4e', 'setup<2', 'needs_2plus')} on 4a2 4e). Pairs and the E slice say nothing, the bad edges next to nothing ([what you can see](#what-you-can-see-that-predicts-it)).
- One move over the optimal it nearly stops mattering: with an optimal of 13 or less, {ds('all', '2+', 'le13', 'p1')} of DRs have no finish within one move of the optimal that reaches its first quarter turn after 0 or 1 half turns ([within one move](#a-finish-within-one-move-of-the-optimal)).

The same question for 2c4 2e. Each row is a group of its DRs; each cell is the share needing exactly that many half turns first, on the better side:

{EX}

**What existed.** Kai Cui asked for these ([27 Oct 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1300060647719043174): "Are there stats on how many ht before first qt including niss for Dr finishes?"), got no answer, and measured 2c3 2e on 540 generated states ([5 Nov 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1303457154635665448)): 60.0% with 0 half turns, 24.8% with 1, 10.9% with 2 and 4.3% with 3. Kai Cui's summary ([5 Nov 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1303457432898633840)): "baically 85 percent chance that you dont need to check 2 ht before first qt". This sample gives {' / '.join(pc(x) for x in g(ALL, '2c3 2e')[3])} for uniform 2c3 2e, so {pc(g(ALL, '2c3 2e')[3][0] + g(ALL, '2c3 2e')[3][1])} with 0 or 1 on the better side. Nothing else on the server has it per subset. [*Which HTR routes to try from a DR*](../htr-routes/) (section 7) has that row and the all-DRs figure. The tables below give every subset × edges.

**One row reads differently.** Half of 0c0 0e is already in HTR. On {pc(J['0c0_0e']['no_qt_in_any_optimal'])} of the sampled row no optimal finish has a quarter turn at all, and those DRs count as 3 or more.

## Optimal of 13 or less

Each row is a subset × edges, restricted to its DRs with an optimal finish of at most 13. *Share of its DRs that short* is how much of the subset × edges that is. The next four cells are the shares needing exactly 0, 1, 2, or 3 or more half turns before the first quarter turn on the better side; the last four are the same on the normal side alone.

{table(R13, 'Subset × edges', True)}

The same, edge counts pooled by their exact sizes. Each row is a corner subset:

{table(P13, 'Corner subset', True)}

## Optimal of 12 or less

Same columns, DRs with an optimal finish of at most 12. The high-qt rows rest on a few hundred DRs each.

{table(R12, 'Subset × edges', True)}

Edge counts pooled. Each row is a corner subset:

{table(P12, 'Corner subset', True)}

## All DRs

Same columns, every DR of the subset × edges ({N:,} sampled each).

{table(ALL, 'Subset × edges', False)}

Edge counts pooled. Each row is a corner subset:

{table(ALLP, 'Corner subset', False)}

{READS}
## How it was computed

The sample is the one behind [*Which HTR routes to try from a DR*](../htr-routes/): {N:,} uniformly random DR states for each of the 48 subset × edges. For each state every optimal finish is enumerated against the exact optimal-finish table of all 19,508,428,800 DR states ([*Judging a DR by hand*](../judging-a-dr/)), and the fewest moves before the first quarter turn is kept for each reading direction. Pooled rows weight each subset × edges by its exact number of DR states (with a cut on the optimal, by that number times the share that qualifies). The script is `tables/src/half_turns_before_first_qt.py` in the repository.

{CHECKS}
"""
open(os.path.join(ROOT, 'tables', 'half-turns-before-first-qt.md'), 'w').write(doc)
print(len(doc.split('\n')), 'lines')
