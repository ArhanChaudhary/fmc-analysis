#!/usr/bin/env python3
"""Rewrite the 'Should I switch this EO?' card of cards/decision-cards.md from the v2 results (same numbers as the
write-up; nothing typed by hand)."""
import os, re, sys
B = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, B)
from env2 import *
def others():
    rows = ['| DRM | Switch when | Share of the DRM | DR in 6 or less after the switch (share of the row) |', '|---|---|---|---|']
    for drm in ('4c2e', '3c2e', '7c8e', '8c8e', '2c2e', '4c6e', '3c4e', '3c6e', '5c4e', '5c6e', '6c6e'):
        for g in D(drm)['groups']:
            if g['verdict'] == 'switch': rows.append(f"| {drm} | {g['label']} | {pc(g['share'])} | {pc(g['rate'])} |")
    return '\n'.join(rows)
X = D('4c4e'); c = X['card']; p = B_ = X['base']['pairs']; f = X['base']['pairs+arm']
text = f"""### Should I switch this EO?

**Count the pairs on the inverse like you do now, then take one more look, and which one depends on the pair count. On 4c4e: 3 or 4 pairs, switch. 2 pairs on two edges, switch. 2 pairs on one edge, switch if the two E-slice edges that are out of the slice share red or orange. 1 pair, switch if it's ARM 21, unless the corners are 4b with exactly one side pair, or 4a and not in two columns (Evan's stacked corners). 0 pairs, only if there's no fake pair either and the misoriented corners are two white and two yellow. That switches {pc(c['switch'])} of 4c4e, a little less than 2+ pairs ({pc(p['switch'])}), and it misses no case of 4 or less (2+ pairs: {pc(p['miss_le4'])}), {pc(c['miss_d5'])} of the 5-movers ({pc(p['miss_d5'])}) and {pc(c['miss_d6'])} of the 6-movers ({pc(p['miss_d6'])}).**

Switching means: after EO + RZP, go to the inverse, keep the EO and look for a DR there. All the odds on this card are for the switched side and are exact, over every EO-solved case of the DRM. They hold after any RZP, because given what you see on normal the switched case is spread evenly over its DRM ([section 3](eo-switch/#3-definitions-and-the-yardstick)). A case is an N-mover if its shortest DR after the switch has N moves.

*What you check:* everything is a colour match on the side you're on ([section 6](eo-switch/#6-reading-the-card-on-normal-and-how-long-it-takes)): the U/D edges in the E slice, the misoriented corners with the colour they show on the U/D face, and the E-slice edges that are out of the slice. Pairs by wen's tracing, edge by edge, so you know whether 2 pairs sit on one edge or on two. Fake pairs are the corners that have an edge's two colours the wrong way round. ARM is the red/orange on U/D and the green/blue on those edges.

**4c4e.** Each row is a group of switched cases. The last three columns say how much of all of 4c4e's 4-or-less, 5-movers and 6-movers sits in the row:

{t_card('4c4e', ('switch', 'time'))}

Everything else is a skip.

**Against what people switch now.** Each row is a rule over all 4c4e cases:

{t_cmp('4c4e', keys=('pairs', 'pairs+case', 'pairs+arm'))}

So it beats 2+ pairs at every length for no more switches. Against the pairs + ARM list (2+ pairs, 1 pair with ARM 21, 0 pairs with JZP or ARM 42) it's a trade, fewer switches for more missed 5- and 6-movers, and with the two *if you have time* rows it misses less at every length for {pts(X['card_time']['switch'] - f['switch'])} more switches.

**The other DRMs.** What to switch, one row per group ([section 5](eo-switch/#5-the-cards) has the full cards, with the groups to add if you have time):

{others()}

For 4c6e, 3c4e, 3c6e, 5c4e, 5c6e and 6c6e these are small pockets in DRMs that are 5% to 10% sub-7 overall. A short DR out of them costs about four times the tracing it costs on 4c4e, so they're for when the good DRMs have run dry.

**Half turns to two bars** (how many R2, L2, F2, B2 until each layer has a bar and both stuck E-slice edges are on that R/L side, U and D turns free) is a good read on a cube you can see: 2 or fewer is {pc(TB['le2']['precision'])} sub-7 and holds every 4-or-less. Before switching it needs the place of all eight bad pieces on the inverse and then a search, and nobody has shown that done in a few seconds, so it's not on this card. If you can read it, *2 or fewer: switch* on top of the card takes the missed 5-movers from {pc(X['card']['miss_d5'])} to {pc(TB['card_or_le2']['miss_d5'])} ([section 7](eo-switch/#7-two-bars-evaluated)).

One more thing after you switch: checking the other DR axis beats turning the EO's last move the other way. On 4c4e it adds 5.9 percentage points to the share of switched cases with a DR in 6 or less, against 2.1 for the last move.

"""
for path in ('/data/fmc/cards/decision-cards.md', '/data/fmc/cards/src/cards.md'):
    doc = open(path).read()
    a = doc.index('### Should I switch this EO?'); b = doc.index('### Should I add some random moves to this EO?')
    doc = doc[:a] + text + doc[b:]
    # the link to the old section 8 (real RZPs) now goes to section 10 (other RZP lengths, real attempts)
    doc = doc.replace('{{sec eo-switch 8}}', '[section 10](eo-switch/#10-other-rzp-lengths-real-attempts-other-weights)')
    doc = doc.replace('[section 8](eo-switch/#8-real-rzps-does-the-uniform-table-apply-after-a-switch)', '[section 10](eo-switch/#10-other-rzp-lengths-real-attempts-other-weights)')
    open(path, 'w').write(doc)
    print('decision card rewritten in', path, len(text), 'bytes')
