#!/usr/bin/env python3
"""The corner-case section of the write-up, generated from the counts: one small table per corner subset
(case, odds, a typical DR) and one for the two sides together.  Writes corner_section.md."""
import sys, collections
sys.path.insert(0, '/data/fmc/judging-a-dr/research/src')
import hand_corner_tables as H          # also rewrites report/data/corner_cases.md

def single(cs, named=False):
    tot = sum(sum(h) for h in H.one[cs].values())
    head = '| Bad corners |' + (' Subset |' if named else '') + ' L | A qt takes it straight to | Share | In 12 | In 13 | A typical DR (its optimal) |'
    out = [head, '|---|' + ('---|' if named else '') + '---|---|---:|---:|---:|---|']
    for k, h in sorted(H.one[cs].items(), key=lambda kv: H.st(kv[1])[1]):
        c = H.cc[k]
        out.append(f"| {H.layout(int(c[2]))} |" + (f" {c[1]} |" if named else '') + f" {c[5]}–{c[6]} | {c[10] or 'nothing, needs a setup'} | {100*sum(h)/tot:.0f}% | {H.P(h,12):.1f}% | {H.P(h,13):.0f}% | `{H.TYP[k][0]}` ({H.TYP[k][1]}) |")
    return '\n'.join(out)

def both(cs, rows):
    """rows: (label, predicate on the pair of case names).  Sums the pairs that match."""
    tot = sum(sum(h) for h in H.two[cs].values())
    out = ['| Normal and inverse | Share | In 12 | In 13 |', '|---|---:|---:|---:|']
    for label, pred in rows:
        acc = [0] * 19
        for k, h in H.two[cs].items():
            if pred(H.NAME[k[0]], H.NAME[k[1]]):
                for d, c in enumerate(h): acc[d] += c
        assert sum(acc), (cs, label)
        out.append(f'| {label} | {100*sum(acc)/tot:.1f}% | {H.P(acc,12):.1f}% | {H.P(acc,13):.1f}% |')
    return '\n'.join(out)

def extremes(cs):
    t = sorted(H.two[cs].items(), key=lambda kv: H.st(kv[1])[1]); tot = sum(sum(h) for h in H.two[cs].values())
    f = lambda kv: f'{100*sum(kv[1])/tot:.1f}% | {H.P(kv[1],12):.1f}% | {H.P(kv[1],13):.1f}%'
    return '\n'.join(['| Normal and inverse | Share | In 12 | In 13 |', '|---|---:|---:|---:|', f'| the best pair of cases | {f(t[0])} |', f'| the worst pair of cases | {f(t[-1])} |'])

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

**2c4** (wen's stacks). Seven cases:

{single('2c4')}

Both sides together:

{both('2c4', [('the best case on both sides (adjacent, a qt straight to 2c3, first row)', lambda a, b: a == b == '2c4-1'),
              ('a qt goes straight to 2c3 or 4b3 on both sides', lambda a, b: straight(a) and straight(b) and not stk(a) and not stk(b)),
              ('a stack on one side only', lambda a, b: stk(a) != stk(b)),
              ('a stack on both sides', lambda a, b: stk(a) and stk(b))])}

So a double stack is as dead as a 5qt, and the best layout on both sides is as good as an average 2c3 4e (27% in 12).

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

The last two rows are 19% of all 2c5, and you can drop them on sight: a 2c5 that is stacked on both sides never finishes in 12.

    U2 F2 U' R2 U F2 D' L2 U B2 U' L2 U2   // the fastest any double-stacked 2c5 finishes: 13

**4c3** (JTuu's question). Nine cases, seven of them 4a3 and two 4b3:

{single('4c3', named=True)}

Both sides together:

{extremes('4c3')}

**4b2** (Daichi's four). They are exactly his list, 2-2 and 3-1 with good and bad parity:

{single('4b2')}

Both sides together:

{extremes('4b2')}

**4a2.** The widest spread of the low-qt subsets:

{single('4a2')}

Both sides together:

{extremes('4a2')}

**4c4** runs from 0.6% to 4.3% in 12 by case, and **4b5** from 1.3% to 2.2%. Nothing to see there.

Appendix E lists all 46 cases with a typical DR and the shortest setup for each, the L range (which is what Evan asked for), and the full both-sides tables.
"""
open('/data/fmc/judging-a-dr/research/src/report_build/corner_section.md', 'w').write(txt)
print(txt[1100:2600])
