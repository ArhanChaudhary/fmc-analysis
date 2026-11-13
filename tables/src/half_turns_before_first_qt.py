#!/usr/bin/env python3
"""Writes tables/half-turns-before-first-qt.md: for every subset x edges, how many half turns an optimal finish needs
before its first quarter turn, on the better of the two sides and on normal alone, for all DRs and for DRs whose
optimal is at most 13 or at most 12.

Data: the HTR-routes study's sample (htr-routes/research/out/big/run1/states_*.tsv, 25,000 uniformly random DR states
per subset x edges; git-ignored, rebuilt by htr-routes/research/run_all.sh).  Columns used: d (optimal finish, from the
exact table of all DR states), ht_first_n / ht_first_i (fewest moves before the first quarter turn over every optimal
finish, read from its first move / from its last move).  Pooled rows weight each subset x edges by its exact size.
usage: python3 tables/src/half_turns_before_first_qt.py   (from the repository root, with env.sh sourced)"""
import os, sys
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
doc = f"""# Half turns before the first quarter turn

From a DR, how many half turns does an optimal finish make before its first quarter turn, if you start on the better side? Per subset × edges, for all DRs and for the DRs that matter in an attempt: those with an optimal of 13 or less, or 12 or less.

**How it's counted.** Take every optimal finish of the DR (U, D, R2, L2, F2, B2) and count the moves before its first U or D quarter turn. They're all half turns; U2 and D2 count. Read each finish from its first move (normal) and from its last move (inverse) and keep the smaller number: that's *the better side*, chosen with hindsight. The *normal side alone* columns keep only the first reading. Sampled: {N:,} uniformly random DRs per subset × edges, each with every optimal finish from the exact table of all DR states, so a share is good to about ±0.3 points, more on the rows with few DRs (the tables give the count). November 2026.

**The short answer.**

- Over all DRs, {pc(allr[0][3][0])} need no half turn first, {pc(allr[0][3][1])} need one, and {pc(two(allr[0]))} need two or more. Among DRs with an optimal of 13 or less it's {pc(two(allr[1]))} that need two or more, and with 12 or less {pc(two(allr[2]))}.
- It depends on the subset and on the edge count. With an optimal of 12 or less, two or more half turns first are needed on {pc(two(worst[0]))} of {worst[0][0]}, {pc(two(worst[1]))} of {worst[1][0]}, {pc(two(worst[2]))} of {worst[2][0]} and {pc(two(worst[3]))} of {worst[3][0]}, and on none of the sampled DRs of {', '.join(none12[:-1])} or {none12[-1]}.
- Checking both sides matters: on the normal side alone, {pc(two_n(allr[0]))} of all DRs need two or more, against {pc(two(allr[0]))} on the better side.

The same question for 2c4 2e. Each row is a group of its DRs; each cell is the share needing exactly that many half turns first, on the better side:

{EX}

**What existed.** Kai Cui's 2c3 2e stats ([5 Nov 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1303457432898633840)): "baically 85 percent chance that you dont need to check 2 ht before first qt". This sample gives {pc(g(ALL, '2c3 2e')[3][0] + g(ALL, '2c3 2e')[3][1])} for 2c3 2e with 0 or 1 on the better side. [*Which HTR routes to try from a DR*](../htr-routes/) (section 7) has that row and the all-DRs figure. The tables below give every subset × edges.

**One row reads differently.** On 0c0 0e the cube is already in HTR, so many optimal finishes have no quarter turn at all, and those count as 3 or more.

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

## How it was computed

The sample is the one behind [*Which HTR routes to try from a DR*](../htr-routes/): {N:,} uniformly random DR states for each of the 48 subset × edges. For each state every optimal finish is enumerated against the exact optimal-finish table of all 19,508,428,800 DR states ([*Judging a DR by hand*](../judging-a-dr/)), and the fewest moves before the first quarter turn is kept for each reading direction. Pooled rows weight each subset × edges by its exact number of DR states (with a cut on the optimal, by that number times the share that qualifies). The script is `tables/src/half_turns_before_first_qt.py` in the repository.
"""
open(os.path.join(ROOT, 'tables', 'half-turns-before-first-qt.md'), 'w').write(doc)
print(len(doc.split('\n')), 'lines')
