#!/usr/bin/env python3
"""The corner-case section of the write-up, generated from the counts: one small table per corner subset
(case, odds, a typical DR) and one for the two sides together.  Writes corner_section.md."""
import sys, collections
sys.path.insert(0, '/data/fmc/judging-a-dr/research/src')
import hand_corner_tables as H          # also rewrites report/data/corner_cases.md

MERGE = [('25', '21'), ('11', '13')]     # look-alike cases with no visible test: one pooled row
def single(cs, named=False):
    tot = sum(sum(h) for h in H.one[cs].values())
    pooled = {}
    for a, b in MERGE:
        if a in H.one[cs] and b in H.one[cs]:
            pooled[a] = (b, [x + y for x, y in zip(H.one[cs][a], H.one[cs][b])])
    head = '| Bad corners |' + (' Subset |' if named else '') + f' L | A qt takes it straight to | Share | {H.ODDS_HEAD} | A typical DR (its optimal) |'
    out = [head, '|---|' + ('---|' if named else '') + '---|---|---:|---:|---:|---:|---:|---|']
    items = [(k, pooled[k][1] if k in pooled else h) for k, h in H.one[cs].items() if k not in {b for b, _ in pooled.values()}]
    for k, h in sorted(items, key=lambda kv: H.st(kv[1])[1]):
        c = H.cc[k]
        if k in pooled:
            o = H.cc[pooled[k][0]]
            lo, hi = min(int(c[5]), int(o[5])), max(int(c[6]), int(o[6]))
            out.append(f"| {H.layout(int(c[2]))} (two cases that look the same) |" + (f" {c[1]} |" if named else '') + f" {lo}–{hi} | {c[10] or 'nothing, needs a setup'} | {100*sum(h)/tot:.0f}% | {H.odds(h)} | `{H.TYP[k][0]}` ({H.TYP[k][1]}) or `{H.TYP[pooled[k][0]][0]}` ({H.TYP[pooled[k][0]][1]}) |")
            continue
        tell = {'8': '; back-face diagonals agree', '7': '; back-face diagonals differ'}.get(k, '')
        out.append(f"| {H.layout(int(c[2]))}{tell} |" + (f" {c[1]} |" if named else '') + f" {c[5]}–{c[6]} | {c[10] or 'nothing, needs a setup'} | {100*sum(h)/tot:.0f}% | {H.odds(h)} | `{H.TYP[k][0]}` ({H.TYP[k][1]}) |")
    return '\n'.join(out)

BOTH_HEAD = [f'| Normal and inverse | Share | {H.ODDS_HEAD} |', '|---|---:|---:|---:|---:|---:|']
def pair_hist(cs, pred):
    acc = [0] * 19
    for k, h in H.two[cs].items():
        if pred(H.NAME[k[0]], H.NAME[k[1]]):
            for d, c in enumerate(h): acc[d] += c
    assert sum(acc), cs
    return acc
def both(cs, rows):
    """rows: (label, predicate on the pair of case names).  Sums the pairs that match."""
    tot = sum(sum(h) for h in H.two[cs].values())
    out = list(BOTH_HEAD)
    for label, pred in rows:
        acc = pair_hist(cs, pred)
        out.append(f'| {label} | {100*sum(acc)/tot:.1f}% | {H.odds(acc)} |')
    return '\n'.join(out)

def extremes(cs):
    t = sorted(H.two[cs].items(), key=lambda kv: H.st(kv[1])[1]); tot = sum(sum(h) for h in H.two[cs].values())
    f = lambda kv: f'{100*sum(kv[1])/tot:.1f}% | {H.odds(kv[1])}'
    return '\n'.join(BOTH_HEAD + [f'| the best pair of cases | {f(t[0])} |', f'| the worst pair of cases | {f(t[-1])} |'])

import pv
Q = pv.quad
def lohi(cs, T):
    v = sorted(H.one[cs].values(), key=lambda h: pv.share(h, T)); return f'{pv.pct(v[0], T)} to {pv.pct(v[-1], T)}'
lay = {k: H.layout(int(H.cc[k][2])) for k in H.cc}
name_of = {v: k for k, v in H.NAME.items()}
stk = lambda n: 'stacked' in lay[name_of[n]]
adj = lambda n: 'adjacent' in lay[name_of[n]]
opp = lambda n: 'opposite' in lay[name_of[n]]
straight = lambda n: bool(H.cc[name_of[n]][10])
txt = f"""This is what Daichi, JTuu and wen asked for. There are 46 corner cases once you merge rotations, mirrors and turning a layer. Inside a corner subset they are *not* equally good, and since the corner case on inverse is a different one, there are two reads.

How to read the tables:

- "A qt takes it straight to" means some U or D quarter turn lowers the corner qt count right away, with no setup.
- L is the range of optimal corner solution lengths the case can have.
- The last column is a typical DR of the case: a state whose optimal is the median for that case, with that optimal in brackets.

**2c4** (wen's stacks). Seven cases. Two of them have the same bad corners and are told apart by the back face, as explained under the table:

{single('2c4')}

{H.BACK_FACE_NOTE}

Both sides together:

{both('2c4', [('the best case on both sides (adjacent, a qt straight to 2c3, first row)', lambda a, b: a == b == '2c4-1'),
              ('a qt goes straight to 2c3 or 4b3 on both sides', lambda a, b: straight(a) and straight(b) and not stk(a) and not stk(b)),
              ('a stack on one side only', lambda a, b: stk(a) != stk(b)),
              ('a stack on both sides', lambda a, b: stk(a) and stk(b))])}

So a double stack is as dead as a 5qt at every target ({Q(pair_hist('2c4', lambda a, b: stk(a) and stk(b)))} against {Q(pv.q(group='5qt'))} for all 5qt DRs, in 10 / 11 / 12 / 13), and the best layout on both sides is as good as an average 2c3 4e ({Q(pv.q(cs='2c3', e=4))}).

    U2 L2 D' F2 U' R2 U F2 D L2 U2   // the fastest any double-stacked 2c4 finishes: 11

**2c5.** Three cases:

{single('2c5')}

Both sides together:

{both('2c5', [('adjacent on both sides', lambda a, b: adj(a) and adj(b)),
              ('adjacent and opposite', lambda a, b: (adj(a) and opp(b)) or (opp(a) and adj(b))),
              ('opposite on both sides', lambda a, b: opp(a) and opp(b)),
              ('adjacent and stacked', lambda a, b: (adj(a) and stk(b)) or (stk(a) and adj(b))),
              ('opposite and stacked', lambda a, b: (opp(a) and stk(b)) or (stk(a) and opp(b))),
              ('stacked on both sides', lambda a, b: stk(a) and stk(b))])}

The last two rows are 19% of all 2c5, and you can drop them on sight whatever your target: a 2c5 that is stacked on both sides never finishes in 12, and stacked on one side with opposite on the other never finishes in 11 and is {pv.pct(pair_hist('2c5', lambda a, b: (opp(a) and stk(b)) or (stk(a) and opp(b))), 12)} for a 12.

    U2 F2 U' R2 U F2 D' L2 U B2 U' L2 U2   // the fastest any double-stacked 2c5 finishes: 13

**4c3** (JTuu's question). Nine cases, seven of them 4a3 and two 4b3. Eight rows, because two of the 4a3 cases look the same:

{single('4c3', named=True)}

The row marked "two cases that look the same" is two corner cases with the same bad corners and no quarter turn that lowers the count. I have not found a visible test that separates them, so the row gives their odds together. Apart, they are {Q(H.one['4c3']['11'])} and {Q(H.one['4c3']['13'])} (in 10 / 11 / 12 / 13), and only the optimal corner solution tells you which: 8 moves is the better one, 10 the worse one, and with 9 it can be either.

Both sides together:

{extremes('4c3')}

**4b2** (Daichi's four: 2-2 and 3-1, each with good and bad parity). Three rows, because the two 3-1 cases look the same:

{single('4b2')}

The 3-1 row is two corner cases that look the same (Daichi's "3-1 good parity" and "3-1 bad parity"). I have not found a visible test that separates them, so the row gives their odds together. Apart, they are {Q(H.one['4b2']['25'])} and {Q(H.one['4b2']['21'])} (in 10 / 11 / 12 / 13), and only the optimal corner solution tells you which: 4 moves is the better one, 8 the worse one, and with 5 to 7 it can be either.

Both sides together:

{extremes('4b2')}

**4a2.** The widest spread of the low-qt subsets:

{single('4a2')}

Both sides together:

{extremes('4a2')}

**4c4** and **4b5** are too rare at 10 and 11 for the case to matter (under 1% in 11 for every case). For a 12, 4c4 runs from {lohi('4c4', 12)} by case and 4b5 from {lohi('4b5', 12)}.

Appendix E lists all 46 cases with a typical DR and the shortest setup for each, the L range (which is what Evan asked for), and the full both-sides tables.
"""
open('/data/fmc/judging-a-dr/research/src/report_build/corner_section.md', 'w').write(txt)
print(len(txt))
