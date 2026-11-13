## 4. Two rings: count the half turns (4c4e)

A U or D turn never makes or breaks a pair. So when you size up a setup, don't count them: let both layers turn freely and ask how many turns of the side faces the DR needs. For 4c4e the finish is one R or L quarter turn and everything before it is half turns, so the question is *how many half turns to two bars*. That count sorts 4c4e far better than pairs, ARM or the corner case, and its two ends are near 100% and near 0%.

The target is rodneykinney's. *DR - 4c4e Theory* says "The final trigger must have two full “bars” formed with the bad corners and edges.", calls each side half turn "an opportunity to form a pair for free", and notes that "An additional 0-2 moves may be needed to solve the E slice." That doc builds a minimum move count from it (corner moves, a pairs penalty, a slice penalty). Here I count the half turns themselves, exactly, with U and D turns free, and measure what the count is worth.

### 4.1 The picture

Take the switched case and forget how the U and D layers are turned. What is left of a layer is a *ring*: its 8 places, read clockwise as you look at that face.

```
      UB
 UBL      UBR      U ring, clockwise from above:   UB UBR UR UFR UF UFL UL UBL
 UL        UR      D ring, clockwise from below:   DB DBL DL DFL DF DFR DR DBR
 UFL      UFR      between them, the E-slice places:   FR FL BL BR
      UF
```

Three things sit on it:

- **Bad edge places.** A ring edge place holding an E-slice edge, the usual bad U/D edge.
- **Bad corners, each pointing at an edge place.** A bad corner has its U/D sticker on one of its two side faces. It *points* along the layer away from that sticker, at the edge place next to it on its other side face. That is the edge place it would pair with. So a pair is a bad corner pointing at a bad edge, a fake pair is a bad corner next to a bad edge and pointing away from it, and a bar is a bad edge with a corner pointing at it from each side.
- **Holes.** The E-slice places that hold a U/D edge. 4c4e has two.

Examples on this page are a scramble from solved in EO-keeping moves (hold the cube with the EO on F/B), then an optimal DR of the case it gives.

I write a ring as 8 characters, clockwise, starting at any corner: `>` is a corner pointing clockwise (at the next place), `<` a corner pointing counter-clockwise (at the place before it), `o` a good corner, `E` a bad edge place, `-` a good one. The string closes on itself, and where it starts doesn't matter. A bar reads `>E<`.

```
{= RXF('h0', '', 'a bar in each layer; U2 D2 puts both on the holes\' face, then R') =}
```

What each turn does to the picture:

| Turn | What it does |
|---|---|
| U, D | Turns one ring. Nothing else changes, so the picture doesn't see it. |
| R2, L2, F2, B2 | Swaps the *row* of that face between the two rings, and swaps the face's two E-slice places. A row is the corner, edge, corner of one layer on one side face. R2 swaps UBR UR UFR with DFR DR DBR, so the clockwise order is kept. |
| R, L (quarter turns) | The four corners on the face move one step round it. A good corner comes out pointing at the face's edge place. A corner that pointed at the face's edge place comes out good. A corner that pointed away keeps pointing away. The four edges on the face move one step round it, layer to slot to layer to slot. |

All three rules hold on every one of the {= n(1082565) =} cases ✓ (Lean: `ring_turns`), and the picture loses nothing: two different cases never have the same rings and holes ✓ (`ring_faithful`).

Because U and D are free, **a half turn can swap any row of the U ring with any row of the D ring**: turn the two rows onto the same face first. Which face you do it on is your choice, and it only matters for the holes.

### 4.2 The count

A 4c4e is one quarter turn from DR when each layer has a bar, both bars are on the same R or L face, and the two holes are on that face. In ring terms: a bar in each ring, and the holes on one R/L face.

**Half turns to two bars** is the fewest half turns that get you there, U and D turns not counted. It is the larger of two things you read separately:

- **Row swaps.** The fewest row swaps that leave a bar in each ring. This is a small puzzle on the two rings alone. Up to turning each ring there are only {= n(sum(RJ['classes'].values())) =} ring pairs in 4c4e, {= RJ['classes']['0'] =} of them needs 0 swaps, {= RJ['classes']['1'] =} need 1, {= RJ['classes']['2'] =} need 2, {= RJ['classes']['3'] =} need 3, {= RJ['classes']['4'] =} need 4 and {= RJ['classes']['5'] =} need 5 ✓ (`ring_swaps_checked`).
- **The holes.** 0 if the two holes are on one R or L face (FR and BR, or FL and BL), 1 if they are diagonal, 2 if they are on one F or B face. F2 or B2 moves a hole between *one R/L face* and *diagonal*. R2 or L2 moves one between *diagonal* and *one F/B face*.

That the count is the larger of the two holds on all {= n(RJ['all44']['n']) =} cases of 4c4e ✓ (`half_turns_to_bars`). The reason is short. Every half turn does one row swap, on a face of your choice, so the same turn can also fix the holes or leave them alone. A swap you don't need can exchange the two bars, which changes nothing.

Each row below is a number of row swaps with one hole layout. The count, and how the sub-7 rate follows it:

{{ring44_swaps_slot}}

The holes only bite when the rings are nearly done. Two bars with the holes on an F/B face is a 2, not a 0:

```
{= RXF('h0_slot2', 'a bar in each layer, holes on the F face', '0 swaps, but 2 half turns, and this one takes 7') =}
```

### 4.3 The bands

One row per count. *Share of 4c4e's sub-7s* is how much of all the sub-7 cases of 4c4e sit in that row. Exact over every case, then the same on the real attempts:

{{ring44_bands}}

- **0 or 1: a certain sub-7.** One half turn, at most two U/D turns before it and two after, then the quarter turn: 6 moves at most. It holds for all {= n(RHG('le1', 'n')) =} ✓ cases.
- **2: switch.** {= pcx(RH(2)) =} ✓ of them are sub-7, and they hold half of 4c4e's sub-7s.
- **3: your call.** {= pcx(RH(3)) =} ✓, on half of 4c4e.
- **4 or 5: discard.** {= pcx(RHG('ge4')) =} ✓ on {= pcx(RHG('ge4', 'share')) =} ✓ of 4c4e. A 5 is never sub-7.

The same rows for the other RZP lengths. After a 4-move RZP a DR in 7 is enough, and after a 6-move RZP you need a DR in 5:

{{ring44_bands_rzp}}

So with a 4-move RZP, 3 half turns is still a switch ({= pcx(RH(3, 'p7')) =}), and with a 6-move RZP only 0 or 1 is.

**Against the paired-edge card** (section 6.1), three groups each:

{{ring44_vs_card}}

The switch group is as large as the card's and {= f1((RHG('le2') - RCARD('switch')) * 100) =} points better, and the discard group throws away {= pcx(RHG('ge4', 'of_hits')) =} of the sub-7s where the card's throws away {= pcx(RCARD('discard', 'of_hits')) =}. What you pay is a bigger middle. The card's own groups, split by the count, show where it goes wrong:

{{ring44_card_split}}

Both edges paired with 3 half turns to go is a {= pcx(RCS('switch', '3')) =} case, not a 60% one. And {= n(RCS('discard', '2 or fewer', 'n')) =} cases the card discards are 2 half turns from two bars, {= pcx(RCS('discard', '2 or fewer')) =} sub-7:

```
{= RXF('h3_card_switch', 'both bad edges paired', '3 swaps') =}

{= RXF('h2_card_discard', 'no pair at all', '2 swaps') =}
```

### 4.4 Reading the count

There is no formula for the row swaps. I looked for one. No score read off one layer at a time can work: the {= RJ['ring_single'] =} different single rings fall into {= RJ['ring_eqv'] =} groups that need different swap counts against some partner ring (**computer only**). And a table over pair counts, which layer each piece is in and which corners are blocked puts {= pcx(RJ['count_table_acc']) =} of 4c4e in the right band (1 or fewer, 2, 3, 4 or more) with {= RJ['count_table_cells'] =} cells. So you count by finding the swaps. That is less work than it sounds, because pairs tell you where to look.

**A swap makes at most two new pairs** ✓ (`pair_change`). So with 0 or 1 pair you need at least 2 swaps, and in practice 3 or more. Each row is a pair count with a count of half turns:

{{ring44_pairs}}

Read it as a recipe:

1. **4 pairs.** 0 swaps if the bars are in different layers, 1 if both are in one layer.
2. **3 pairs.** One corner is unpaired and one edge lacks a corner. Start at 1 swap. Add 1 if the unpaired corner is in the same layer as the edge that lacks it. Add 1 if it is *blocked*: a bad piece in the two places behind it (the edge place and corner on the side it points away from). Add 1 if both bad edges are in one layer, opposite each other. This is exact on every 3-pair case ✓ (`three_pair_rule`):

{{ring44_3pairs}}

3. **2 pairs.** Look one swap ahead: you are at 2 if some swap leaves one of the 1-swap pictures below. {= pcx(RJ['ph']['2|le2']['n'] / RJ['ph']['2|all']['n']) =} of 2-pair cases are at 2 or less, and those are {= pcx(RJ['ph']['2|le2']['p6']) =} sub-7 against {= pcx(RJ['ph']['2|ge3']['p6']) =} for the rest. This is the look that pays.
4. **0 or 1 pair.** Call it 3 or more and move on. You lose {= n(RU('p01le2', 'n')) =} cases that are really at 2 ({= pcx(RU('p01le2', 'n') / RU('p01', 'n')) =} of the 0- and 1-pair cases), one 0-pair picture and three 1-pair pictures in appendix A.

The pictures with at most 1 swap, up to exchanging the layers and mirror image. Know the four with 1 swap and the rest is one swap of look-ahead:

| Row swaps | One layer | The other layer | What it is |
|---|---|---|---|
| 0 | `>E<-o-o-` | `>E<-o-o-` | a bar in each layer |
| 1 | `>E<->E<-` | `o-o-o-o-` | both bars in one layer: swap one over |
| 1 | `>E<E<-o-` | `>-o-o-o-` | 3 pairs, the two bad edges next to each other in one layer, the fourth corner alone in the other: swap the bar out and the corner in |
| 1 | `oE<-o-o-` | `>E<-o->-` | 3 pairs, the fourth corner in the bar's layer with nothing behind it: swap it across |
| 1 | `oE<-o-<-` | `>Eo->-o-` | one pair on each edge, and each layer holds the corner the other needs, two places from where it has to land: one swap trades them |

All ring pairs with at most 2 swaps, {= RJ['patterns_n']['0'] + RJ['patterns_n']['1'] + RJ['patterns_n']['2'] =} pictures up to layer exchange and mirror image, are listed in appendix A ✓ (`patterns_le2`).

Three worked ones:

```
{= RXF('h1_three_pairs', '3 pairs', '1 swap, L2 carries the fourth corner across') =}

{= RXF('h1_trade', 'one pair on each edge', '1 swap, L2 trades the two corners') =}

{= RXF('h2_sub7', '2 pairs', '2 swaps, L2 then R2, one corner each') =}

{= RXF('h2_not', '2 pairs, 2 swaps again', 'but the layers don\'t line up: 7 moves') =}
```

**What the look costs.** You trace the same six pieces as for pairs. On top of that you note which layer each piece is in, and for each unpaired corner where it sits and which way it points: one more look per unpaired corner, and one at the holes. With 3 or 4 pairs the recipe is a count. With 2 pairs it is a one-swap search. I timed none of it.

### 4.5 What the U and D turns add

The count ignores U and D turns, and they are what is left. A setup with h half turns and u U/D turns before the quarter turn is a DR in h + u + 1 moves, so 2 half turns are sub-7 with up to 3 U/D turns and 3 half turns with up to 2. Each row is a half-turn count with the U/D turns its shortest setup needs:

{{ring44_align_sum}}

So for a 2, about two in three line up, and once you have found the two swaps you check that in the same breath: every swap whose two rows are already on the same face costs no U/D turn. For a 3 it is one in nine. The rest of the 3s that are sub-7 take another route (section 4.6). The full table is in appendix A.

**Nothing cheap splits a 3 well.** Each row is a group inside *3 half turns*:

{{ring44_inside3}}

**ARM adds little once you have the count.** In information terms (section 11) ARM removes {= f3(RJ['info']['arm']) =} of the uncertainty about sub-7 in 4c4e on its own, and {= f3(RJ['info']['h+arm'] - RJ['info']['h']) =} once the count is known. The count alone removes {= f3(RJ['info']['h']) =}, pairs {= f3(RJ['info']['pairs']) =}, pairs and ARM together {= f3(RJ['info']['pairs+arm']) =}. Inside *2 half turns* every ARM is between {= pcx(min(v for k, v in RJ['arm_in'].items() if k.startswith('2|'))) =} and {= pcx(max(v for k, v in RJ['arm_in'].items() if k.startswith('2|'))) =}. And ARM says next to nothing about how the layers line up: it removes {= f3(RJ['arm_align']['2']) =} of the uncertainty about whether a 2 needs 3 U/D turns or fewer, and {= f3(RJ['arm_align']['3']) =} of the same question for a 3. So most of what ARM knew about sub-7 was the half-turn count.

### 4.6 The DRs that don't finish with one quarter turn

{= pcx(1 - RJ['qopt']['1'] / RJ['all44']['hits']) =} of 4c4e's sub-7 cases have no optimal DR with a single quarter turn. Each row is the fewest quarter turns in an optimal DR:

{{ring44_routes}}

```
{= RXF('q2_route', '3 half turns to two bars, but a DR in 6 with two quarter turns') =}

{= RXF('q3_route', 'three quarter turns, no half turn') =}
```

Pairs don't see these and the half-turn count doesn't either: most of them sit at 3. They are why a 3 is {= pcx(RH(3)) =} and not {= pcx(RU('u_le_3', 'n') / RH(3, 'n')) =}. Counting side turns of any kind catches some of them, and that is the next section.
