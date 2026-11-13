The question is whether there are switch guidelines, checkable at the table, that get closer to 100% or 0% sub-7 than ARM, DRM, pairs and the corner case do. There are, once you count the right thing. A U or D turn never makes or breaks a pair, so judge the setup as if U and D turns were free and count only the turns of the side faces. For 4c4e that is the number of half turns to two bars: at 0 or 1 a sub-7 is certain, at 2 it is {= pcx(RH(2)) =} ✓, at 3 it is {= pcx(RH(3)) =} ✓, at 4 it is {= pcx(RH(4)) =} ✓ and at 5 never. All the rules are about the case on the switched side; section 7 shows how to see it on normal before you switch.

**What is new here**

**A switched case is two rings.** Forget how the U and D layers are turned. Each layer is then a ring of 8 places, with its bad edges and its bad corners, and every bad corner points along the ring at the edge place it would pair with. Between the rings sit the four E-slice places. On that picture (section 4.1):

- U and D turns do nothing.
- A half turn swaps one *row* (corner, edge, corner on one side face) between the two rings, any row of U with any row of D, and swaps the two E-slice places of the face you do it on.
- An R or L quarter turn moves the face's four corners one step: a good corner comes out pointing at the face's edge, one that pointed at it comes out good, one pointing away stays pointing away.

The three rules hold on every one of the {= n(1082565) =} cases ✓.

**4c4e: count the half turns to two bars.** A 4c4e is one quarter turn from DR when each ring has a bar and the two holes (the U/D edges in the E slice) are on one R or L face. The count is the fewest half turns that get there, U and D turns free. One row per count, with its share of 4c4e, its sub-7 rate and the share of all of 4c4e's sub-7 cases it holds (section 4.3):

| Half turns to two bars | Verdict | Share of 4c4e | Sub-7 rate | Share of 4c4e's sub-7s |
|---|---|---|---|---|
| 0 or 1 | **switch**, certain | {= pcx(RHG('le1', 'share')) =} ✓ | {= pcx(RHG('le1')) =} ✓ | {= pcx(RHG('le1', 'of_hits')) =} ✓ |
| 2 | **switch** | {= pcx(RH(2, 'share')) =} ✓ | {= pcx(RH(2)) =} ✓ | {= pcx(RH(2, 'of_hits')) =} ✓ |
| 3 | **your call** | {= pcx(RH(3, 'share')) =} ✓ | {= pcx(RH(3)) =} ✓ | {= pcx(RH(3, 'of_hits')) =} ✓ |
| 4 or 5 | **discard** | {= pcx(RHG('ge4', 'share')) =} ✓ | {= pcx(RHG('ge4')) =} ✓ | {= pcx(RHG('ge4', 'of_hits')) =} ✓ |

Against the best rule a pair trace gives, the paired-edge card further down: its switch group is {= pcx(RCARD('switch', 'share')) =} ✓ of 4c4e at {= pcx(RCARD('switch')) =} ✓, this one is {= pcx(RHG('le2', 'share')) =} ✓ at {= pcx(RHG('le2')) =} ✓. Its discard group throws away {= pcx(RCARD('discard', 'of_hits')) =} ✓ of the sub-7s, this one {= pcx(RHG('ge4', 'of_hits')) =} ✓. And the card's own groups split: both edges paired is {= pcx(RCS('switch', '2 or fewer')) =} ✓ with 2 half turns or fewer and {= pcx(RCS('switch', '3')) =} ✓ with 3.

The count is the larger of two readings ✓ (section 4.2):

- *Row swaps*: the fewest row swaps that leave a bar in each ring.
- *The holes*: 0 if the two holes are on one R/L face, 1 if diagonal, 2 if on one F/B face.

**How to count the row swaps** (section 4.4). There is no formula, and I say why there. Pairs tell you where to look:

- **4 pairs**: 0, or 1 if both bars are in one layer.
- **3 pairs**: 1, plus 1 if the unpaired corner is in the layer of the edge that lacks it, plus 1 if a bad piece sits in the two places behind it, plus 1 if both bad edges are in one layer and opposite. Exact ✓.
- **2 pairs**: look one swap ahead. {= pcx(RJ['ph']['2|le2']['n'] / RJ['ph']['2|all']['n']) =} ✓ of 2-pair cases are at 2 or less, and those are {= pcx(RJ['ph']['2|le2']['p6']) =} ✓ sub-7 against {= pcx(RJ['ph']['2|ge3']['p6']) =} ✓ for the others.
- **0 or 1 pair**: 3 or more, apart from four pictures. A swap makes at most two new pairs ✓.

```
{= RXF('h2_sub7', '4c4e, 2 pairs', '2 swaps, L2 then R2') =}
```

**Every DRM: count the side turns** (section 5). Side turns are the R and L quarter turns and the half turns of a DR, U and D turns not counted.

- **2 side turns or fewer is a certain sub-7** in any DRM: all {= n(RJ['sig_all']['0']['n'] + RJ['sig_all']['1']['n'] + RJ['sig_all']['2']['n']) =} ✓ such cases. They are the trigger cases (`R U R`, `R U2 R`, `R U L`, `R U2 L`, `R L`, `R U D2 L` with any U/D turns around them) and the 4c4e cases one half turn from two bars.
- **3 side turns with no extra quarter turn** is the switch group: one half turn from a trigger case, or one R/L quarter turn from a 4c4e that is one half turn from two bars. Call a case *short* if it needs 3 side turns or fewer of that kind. One row per DRM:

| DRM | Short: share of the DRM | Short: sub-7 rate | Not short: sub-7 rate | Share of the DRM's sub-7s that are short |
|---|---|---|---|---|
| 4c4e | {= pcx(RSHORT('4c4e', 'short', 'share')) =} ✓ | {= pcx(RSHORT('4c4e')) =} ✓ | {= pcx(RSHORT('4c4e', 'long')) =} ✓ | {= pcx(RSHORT('4c4e', 'short', 'of_hits')) =} ✓ |
| 4c2e | {= pcx(RSHORT('4c2e', 'short', 'share')) =} ✓ | {= pcx(RSHORT('4c2e')) =} ✓ | {= pcx(RSHORT('4c2e', 'long')) =} ✓ | {= pcx(RSHORT('4c2e', 'short', 'of_hits')) =} ✓ |
| 3c2e | {= pcx(RSHORT('3c2e', 'short', 'share')) =} ✓ | {= pcx(RSHORT('3c2e')) =} ✓ | {= pcx(RSHORT('3c2e', 'long')) =} ✓ | {= pcx(RSHORT('3c2e', 'short', 'of_hits')) =} ✓ |
| 7c8e | {= pcx(RSHORT('7c8e', 'short', 'share')) =} ✓ | {= pcx(RSHORT('7c8e')) =} ✓ | {= pcx(RSHORT('7c8e', 'long')) =} ✓ | {= pcx(RSHORT('7c8e', 'short', 'of_hits')) =} ✓ |
| 8c8e | {= pcx(RSHORT('8c8e', 'short', 'share')) =} ✓ | {= pcx(RSHORT('8c8e')) =} ✓ | {= pcx(RSHORT('8c8e', 'long')) =} ✓ | {= pcx(RSHORT('8c8e', 'short', 'of_hits')) =} ✓ |
| 2c2e | {= pcx(RSHORT('2c2e', 'short', 'share')) =} ✓ | {= pcx(RSHORT('2c2e')) =} ✓ | {= pcx(RSHORT('2c2e', 'long')) =} ✓ | {= pcx(RSHORT('2c2e', 'short', 'of_hits')) =} ✓ |
| 4c6e | {= pcx(RSHORT('4c6e', 'short', 'share')) =} ✓ | {= pcx(RSHORT('4c6e')) =} ✓ | {= pcx(RSHORT('4c6e', 'long')) =} ✓ | {= pcx(RSHORT('4c6e', 'short', 'of_hits')) =} ✓ |
| 3c4e | {= pcx(RSHORT('3c4e', 'short', 'share')) =} ✓ | {= pcx(RSHORT('3c4e')) =} ✓ | {= pcx(RSHORT('3c4e', 'long')) =} ✓ | {= pcx(RSHORT('3c4e', 'short', 'of_hits')) =} ✓ |
| 3c6e | {= pcx(RSHORT('3c6e', 'short', 'share')) =} ✓ | {= pcx(RSHORT('3c6e')) =} ✓ | {= pcx(RSHORT('3c6e', 'long')) =} ✓ | {= pcx(RSHORT('3c6e', 'short', 'of_hits')) =} ✓ |
| 5c4e | {= pcx(RSHORT('5c4e', 'short', 'share')) =} ✓ | {= pcx(RSHORT('5c4e')) =} ✓ | {= pcx(RSHORT('5c4e', 'long')) =} ✓ | {= pcx(RSHORT('5c4e', 'short', 'of_hits')) =} ✓ |
| 5c6e | {= pcx(RSHORT('5c6e', 'short', 'share')) =} ✓ | {= pcx(RSHORT('5c6e')) =} ✓ | {= pcx(RSHORT('5c6e', 'long')) =} ✓ | {= pcx(RSHORT('5c6e', 'short', 'of_hits')) =} ✓ |
| 6c6e | {= pcx(RSHORT('6c6e', 'short', 'share')) =} ✓ | {= pcx(RSHORT('6c6e')) =} ✓ | {= pcx(RSHORT('6c6e', 'long')) =} ✓ | {= pcx(RSHORT('6c6e', 'short', 'of_hits')) =} ✓ |

**The cards and the side turns stack** (section 5.5). The card's group, short against not short:

| Case | Short: sub-7 rate | Not short: sub-7 rate |
|---|---|---|
| 7c8e with 5 or 6 pairs | {= pcx(RCROSS('7c8e', '5 or 6 pairs', 'short')) =} ✓ | {= pcx(RCROSS('7c8e', '5 or 6 pairs', 'not short')) =} ✓ |
| 2c2e with a paired edge | {= pcx(RCROSS('2c2e', 'a bad edge with a pair', 'short')) =} ✓ | {= pcx(RCROSS('2c2e', 'a bad edge with a pair', 'not short')) =} ✓ |
| 4c6e JZP | {= pcx(RCROSS('4c6e', 'JZP', 'short')) =} ✓ | {= pcx(RCROSS('4c6e', 'JZP', 'not short')) =} ✓ |
| 4c4e with both bad edges paired | {= pcx(RCROSS('4c4e', 'both bad edges paired', 'short')) =} ✓ | {= pcx(RCROSS('4c4e', 'both bad edges paired', 'not short')) =} ✓ |
| 3c2e | {= pcx(RCROSS('3c2e', 'any', 'short')) =} ✓ | {= pcx(RCROSS('3c2e', 'any', 'not short')) =} ✓ |
| 4c2e with 1.5+ pairs | {= pcx(RCROSS('4c2e', 'pairs + side pairs/2 is 1.5 or more', 'short')) =} ✓ | {= pcx(RCROSS('4c2e', 'pairs + side pairs/2 is 1.5 or more', 'not short')) =} ✓ |

So rodneykinney's 5-6 pairs for 7c8e was an average of a near-certain group and a one-in-three group, and "3c2e: just always switch" hides {= pcx(RCROSS('3c2e', 'any', 'not short', 'share')) =} ✓ of 3c2e at {= pcx(RCROSS('3c2e', 'any', 'not short')) =} ✓.

**The low DRMs have a rescue where you can see a short setup.** Short 4c6e is {= pcx(RSHORT('4c6e')) =} ✓ and holds {= pcx(RSHORT('4c6e', 'short', 'of_hits')) =} ✓ of 4c6e's sub-7s, short 5c6e is {= pcx(RSHORT('5c6e')) =} ✓, short 5c4e {= pcx(RSHORT('5c4e')) =} ✓. The other side is the cleaner discard: 3c6e that is not short is {= pcx(RSHORT('3c6e', 'long')) =} ✓, 4c6e {= pcx(RSHORT('4c6e', 'long')) =} ✓. By a pair trace alone they still have none: no rule of up to three of the features in section 11 puts more than {= pc(max(E['low_best'].values())) =} of their sub-7 cases into a cell above 50%.

**What the count leaves open.**

- *How the layers line up.* 2 half turns are a sub-7 when the setup needs 3 U/D turns or fewer, which is {= pcx(RU('u_le_2', 'n') / RH(2, 'n')) =} of them. Nothing cheap predicts that, but you see it while you find the two swaps (section 4.5).
- *A 3 stays a 3.* Inside 3 half turns no pair, ARM or side-pair group gets above {= pcx(RIN3('3 pairs')) =} (section 4.5). ARM adds almost nothing once you have the count: most of what it knew was the count.
- *It takes a look, not a tally.* For 4c4e with 2 pairs you search one swap deep, and for the other DRMs one half turn deep towards a trigger picture. Where that is more than a solver would do, the page says so.

**The rings read on normal.** Each U/D edge in the E slice marks its own edge place. Each misoriented corner marks its own corner place and points at the edge place of its U/D colour and the side colour that is *not* showing on the U/D face. Each E-slice edge in the U or D layer marks its own slot as a hole. It gave the inverse's rings and holes on {= n(TRR('both rings', 'uniform')[1]) =} of {= n(TRR('both rings', 'uniform')[0]) =} random cubes (section 7).

**What a pair trace alone gives.** If you only trace pairs, these are the best rules, each from the search of section 11.

**4c4e: count paired edges, then look at edge ARM.** Of the two bad U/D edges on the switched side, how many have a pair? Each row is a group of switched 4c4e cases, with its share of 4c4e and its sub-7 rate:

| Switched case (4c4e) | Verdict | Share of 4c4e | Sub-7 rate |
|---|---|---|---|
| both bad edges paired | **switch** | {= pcx(RG('4c4e', 'switch', 'share')) =} ✓ | {= pcx(RG('4c4e', 'switch')) =} ✓ |
| one paired, edge ARM 1 (the two bad edges in different slices) | **your call** | {= pcx(RG('4c4e', 'check', 'share')) =} ✓ | {= pcx(RG('4c4e', 'check')) =} ✓ |
| one paired with both edges in one slice (edge ARM 0 or 2), or none paired | **discard** | {= pcx(RG('4c4e', 'discard', 'share')) =} ✓ | {= pcx(RG('4c4e', 'discard')) =} ✓ |

That settles {= pcx(RULE('4c4e', 'decided')) =} ✓ of 4c4e. ARM alone settles {= pc(STRICT('4c4e', 'carm+earm')) =} ✓ (its full 15-row table), pairs alone {= pc(STRICT('4c4e', 'pairs')) =} ✓, and the full pairs × ARM table {= pc(STRICT('4c4e', 'pairs+carm+earm')) =} ✓ (section 6.1).

**The 4c4e your-call group, split.** With one paired edge and edge ARM 1, the corners decide. Each row is a corner group inside it:

| Corners (one paired edge, edge ARM 1) | Sub-7 rate |
|---|---|
| 4d (rare: {= CELL('c44_check', '4d corners (always corner ARM 2: ARM 21)', 'Share of the DRM') =} ✓ of 4c4e) | {= CELL('c44_check', '4d corners (always corner ARM 2: ARM 21)', 'Sub-7 rate, exact') =} ✓ |
| 4b, ARM 21 | {= CELL('c44_check', 'corner ARM 2 (ARM 21), 4b corners', 'Sub-7 rate, exact') =} ✓ |
| 4b, corner ARM 0 or 4 | {= CELL('c44_check', 'corner ARM 0 or 4, 4b corners', 'Sub-7 rate, exact') =} ✓ |

That answers tseitsei89's "It would be really nice to find a way to filter out good 1 pair cases but there doesnt seem to be one currently" ([[T9334]]).

**A bar is worth half as much as two separate pairs.** In 4c4e, the sub-7 rate of two pairs on one edge against two pairs on the two edges:

| Two pairs (4c4e) | Sub-7 rate |
|---|---|
| on one edge (a bar) | {= CELL('c44_bars', '2 pairs on 1 edge (a bar)', 'Sub-7 rate, exact') =} ✓ |
| on the two edges | {= CELL('c44_bars', '2 pairs on 2 edges', 'Sub-7 rate, exact') =} ✓ |

The gap holds in every ARM ({= f1(min((BARS(a, 1) - BARS(a, 0)) * 100 for a in E['bars'])) =} ✓ to {= f1(max((BARS(a, 1) - BARS(a, 0)) * 100 for a in E['bars'])) =} ✓ points). That's why the card counts paired edges and not pairs, and it settles bpaul's question about pairs per edge ([[D12986]]) and Yura Riabov's "1 bar is worse than 2 pairs for most arms" ([[D12993]]) (section 10).

**Side pairs and edge ARM on the inverse, read on normal**, without switching axes:

- *Side pairs*: for each E-slice edge sitting in the U or D layer, count the misoriented corners that carry both its colours and show the EO axis's colour (green/blue for an F/B EO) on the U/D face.
- *Edge ARM*: count the U/D edges in the E slice whose other colour is green/blue.

Both held on {= n(TRACE('side pairs', 'uniform')[1]) =} of {= n(TRACE('side pairs', 'uniform')[0]) =} random cubes (section 7).

**7c8e: 3 pairs or fewer is a safe discard** ({= pcx(RG('7c8e', 'discard', 'share')) =} ✓ of 7c8e at {= pcx(RG('7c8e', 'discard')) =} ✓). With 4 pairs, edge ARM 1 is {= CELL('c78_check', '4 pairs, edge ARM 1', 'Sub-7 rate, exact') =} ✓ and every other edge ARM {= CELL('c78_check', '4 pairs, edge ARM 3', 'Sub-7 rate, exact') =} ✓ or less.

**After a switch the RZP bias is gone.** torchlight was right that an RZP biases the case it reaches ([[T4250]]). The 4c4e sub-7 rate in three populations:

| 4c4e population | Sub-7 rate |
|---|---|
| uniform | {= pc(POP('4c4e', 0)) =} ✓ |
| end state of a 5-move RZP, same side | {= pc(POP('4c4e', 1)) =} |
| the same, switched | {= pc(POP('4c4e', 2)) =} |

The switched state is exactly uniform again, for every DRM, because the inverse of a cube with a given case is uniform over that case. So every exhaustive table is right for the cases you actually switch. On the {= n(E['attempts_total']) =} real attempts, no DRM × RZP length is more than {= f2(E['uniform_worst_z']) =} standard errors off the uniform rate (section 8).

**After a switch the last-turn options are worth little.** Turning the RZP's last move the other way never changes the switched case ({= n(E['last_rzp'][0]) =} of {= n(E['last_rzp'][1]) =} pairs of attempts; proved in Lean ✓). For 4c4e (section 8), each row is an option; the points are its sub-7 rate minus the rate without it:

| Option (4c4e) | Sub-7 rate after a switch, without the option | With the option | Points added after a switch | Points added without a switch |
|---|---|---|---|---|
| EO's last turn | {= pc(OPT('4c4e', 0)) =} | {= pc(OPT('4c4e', 1)) =} | {= f1((OPT('4c4e', 1) - OPT('4c4e', 0)) * 100) =} | {= f1((VAR('4c4e', 'lastF_le6') - VAR('4c4e', 'plain_le6')) * 100) =} ✓ |
| other DR axis | {= pc(OPT('4c4e', 0)) =} | {= pc(OPT('4c4e', 2)) =} | {= f1((OPT('4c4e', 2) - OPT('4c4e', 0)) * 100) =} | {= f1((VAR('4c4e', 'two_le6') - VAR('4c4e', 'plain_le6')) * 100) =} |

**RZP length moves every band.** After a 4-move RZP (DR in 7 is enough), 4c4e with 3 half turns to two bars is still {= pcx(RH(3, 'p7')) =} ✓ and with 2 or fewer {= pcx(RHG('le2', 'p7')) =} ✓; every 4c4e case with a paired edge is around 50% or more, and only the no-pair group stays low ({= pcx(RCELL('4c4e', 3, 'p7')) =} ✓). After a 6-move RZP (DR in 5 needed), only 0 or 1 half turn is a switch ({= pcx(RHG('le1', 'p5')) =} ✓; 2 half turns are {= pcx(RH(2, 'p5')) =} ✓), and no common pair cell reaches 25%: 4c4e with both edges paired is {= pcx(RCELL('4c4e', 0, 'p5')) =} ✓ and 3c2e is {= pcx(RCELL('3c2e', 0, 'p5')) =} ✓ (section 6).

**The low DRMs, by pairs and ARM.** For 4c6e, 3c4e, 3c6e, 5c4e, 5c6e and 6c6e the best small cells a pair trace finds, with their sub-7 rates (the short setups above do better where you can see them):

| Cell | Sub-7 rate |
|---|---|
| 4c6e JZP ({= pcx(RG('4c6e', 'switch', 'share')) =} ✓ of 4c6e) | {= pcx(RG('4c6e', 'switch')) =} ✓ |
| 5c6e with 4 pairs | {= pcx(RG('5c6e', 'check')) =} ✓ |
| 3c4e with 2 pairs | {= pcx(RG('3c4e', 'check')) =} ✓ |

**Fanti's rule figures are any-turn numbers**: they allow F/B quarter turns, which break the EO. With the EO kept they move by about a point at most (4c2e switch success: {= pc(EV('doc583-4c2e', 'success ', ',')) =} any-turn, {= pc(EV('doc583-4c2e', 'EO-kept: success ', ',')) =} EO kept) (section 12).

**What it confirms or corrects**

- **Confirmed: the 4c2e rule.** "1.5+ pairs" (rodneykinney, [[T9468]]) switches exactly the same cases as Jay's 1 pair + 1 side pair or 2 pairs ([[T8144]]) and tseitsei89's version ([[T9321]]): {= pcx(RG('4c2e', 'switch', 'share')) =} ✓ of 4c2e at {= pcx(RG('4c2e', 'switch')) =} ✓. What I add is the other end: 0 or 0.5 is {= pcx(RG('4c2e', 'discard')) =} ✓, so the rule settles {= pcx(RULE('4c2e', 'decided')) =} ✓ of 4c2e.
- **Confirmed: the rest of the switch list.** rodneykinney's 5-6 pairs for 7c8e ({= pc(GR('78-rodney', 'precision')) =} ✓), "3c2e: just always switch" (tseitsei89, [[T9321]]: {= pcx(RULE('3c2e', 'all', 'p6')) =} ✓), 1+ pairs for 2c2e ({= pc(GR('22-doc319', 'precision')) =} ✓), JZP-only for 4c6e, and Yura Riabov's "trash" ARMs for 4c4e (all under 4% ✓). The search found nothing cheap that does much better on those DRMs (section 11).
- **Confirmed: Zagros's 8c8e condition**, "8e8c - R L but only if four corners are clockwise and four are ccw (7/1 is possible)" ([[T6505]]): all {= n(RJ['c88']['n44']) =} 8c8e cases with a 4-4 split have a DR with two quarter turns, and none of the {= n(RJ['c88']['n71']) =} with a 7-1 split has (section 13).
- **Confirmed: the NISS predictors.** The ARM axis swap, R/L stickers on U/D for corner ARM, rodneykinney's corner-case flow chart and wen's pair tracing each held on every one of {= n(NISS('ARM axis swap: ARM for U/D DR on normal = ARM for R/L DR on inverse (uniform)')[0]) =} sampled cubes. Louis's same-axis version, which Louis took back at the time, holds on only {= pc(NISS('ARM for U/D DR on normal = ARM for U/D DR on inverse, same axis')[1] / NISS('ARM for U/D DR on normal = ARM for U/D DR on inverse, same axis')[0]) =} (section 7).
- **Confirmed: the published tables.** {= n(E['repro']['match']) =} of {= n(E['repro']['n']) =} published numbers reproduce. The two that don't are sampled cells in Evan's *arm/pairs*, low by {= f3(float(REP('4c4e 2 pairs sub-7', 'ours', 'C13')) - float(REP('4c4e 2 pairs sub-7', 'published', 'C13'))) =} and {= f3(float(REP('4c4e 3 pairs sub-7', 'ours', 'C13')) - float(REP('4c4e 3 pairs sub-7', 'published', 'C13'))) =} (section 12).
- **Corrected** (errata, each with an example). One claim per row:

| Claim | Who | What the numbers say |
|---|---|---|
| 10 4c4e ARM sets can be sub-6 after a switch | Jay ([[T4256]]) | 11 ✓: AR-4c1e is missing |
| "no number of pairs will save 3qt corners" (4c2e) | rodneykinney ([[T8147]]) | 3qt corners (4b-0) with 2 pairs are {= pc(EV('T8147-3qt', '4b-0 2p ')) =} ✓ sub-7 |
| 1 pair + AR-21 with a corners, "< 5% otherwise" | Evan ([[D14402]]) | {= pc(EV('D14402-21-1p', 'a not stacked ', ' ')) =} ✓ |

- **Depends**: rodneykinney's "there aren't any 4-movers with 0 or 1 pairs" ([[T597]]) holds with side pairs counted, not for top pairs alone (first line below); and the 0-pair catch for that case misses the same case one U/D turn earlier (second line) (section 13).

```
F2 B2 R    // 4c4e with no top pair
D F2 B2 R  // 0 pairs, no fake pairs, missed by the 0-pair catch
```
