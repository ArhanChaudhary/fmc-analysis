The question is whether there are switch guidelines, checkable at the table, that get closer to 100% or 0% sub-7 than ARM, DRM, pairs and the corner case do. Short answer: nothing you can check at the table gets close to 100%. The best common switch groups sit around 60% sub-7, and only rare cells reach 80% to 90%. What cheap checks *can* do is sort most cases into clear bands: over 50% (switch), under 10% (discard), and a middle group where your own cut decides (*your call* below). All the rules are about the case on the switched side; section 5 shows how to see each feature on normal before you switch.

**What is new here**

**4c4e: count paired edges, then look at edge ARM.** Of the two bad U/D edges on the switched side, how many have a pair? Each row is a group of switched 4c4e cases, with its share of 4c4e and its sub-7 rate:

| Switched case (4c4e) | Verdict | Share of 4c4e | Sub-7 rate |
|---|---|---|---|
| both bad edges paired | **switch** | {= pc(RG('4c4e', 'switch', 'share')) =} ✓ | {= pc(RG('4c4e', 'switch')) =} ✓ |
| one paired, edge ARM 1 (the two bad edges in different slices) | **your call** | {= pc(RG('4c4e', 'check', 'share')) =} ✓ | {= pc(RG('4c4e', 'check')) =} ✓ |
| one paired with both edges in one slice (edge ARM 0 or 2), or none paired | **discard** | {= pc(RG('4c4e', 'discard', 'share')) =} ✓ | {= pc(RG('4c4e', 'discard')) =} ✓ |

That settles {= pc(RULE('4c4e', 'decided')) =} ✓ of 4c4e. ARM alone settles {= pc(STRICT('4c4e', 'carm+earm')) =} ✓ (its full 15-row table), pairs alone {= pc(STRICT('4c4e', 'pairs')) =} ✓, and the full pairs × ARM table {= pc(STRICT('4c4e', 'pairs+carm+earm')) =} ✓ (section 4.1).

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

The gap holds in every ARM ({= f1(min((BARS(a, 1) - BARS(a, 0)) * 100 for a in E['bars'])) =} ✓ to {= f1(max((BARS(a, 1) - BARS(a, 0)) * 100 for a in E['bars'])) =} ✓ points). That's why the card counts paired edges and not pairs, and it settles bpaul's question about pairs per edge ([[D12986]]) and Yura Riabov's "1 bar is worse than 2 pairs for most arms" ([[D12993]]) (section 8).

**Side pairs and edge ARM on the inverse, read on normal**, without switching axes:

- *Side pairs*: for each E-slice edge sitting in the U or D layer, count the misoriented corners that carry both its colours and show the EO axis's colour (green/blue for an F/B EO) on the U/D face.
- *Edge ARM*: count the U/D edges in the E slice whose other colour is green/blue.

Both held on {= n(TRACE('side pairs', 'uniform')[1]) =} of {= n(TRACE('side pairs', 'uniform')[0]) =} random cubes (section 5).

**7c8e: 3 pairs or fewer is a safe discard** ({= pc(RG('7c8e', 'discard', 'share')) =} ✓ of 7c8e at {= pc(RG('7c8e', 'discard')) =} ✓). With 4 pairs, edge ARM 1 is {= CELL('c78_check', '4 pairs, edge ARM 1', 'Sub-7 rate, exact') =} ✓ and every other edge ARM {= CELL('c78_check', '4 pairs, edge ARM 3', 'Sub-7 rate, exact') =} ✓ or less.

**After a switch the RZP bias is gone.** torchlight was right that an RZP biases the case it reaches ([[T4250]]). The 4c4e sub-7 rate in three populations:

| 4c4e population | Sub-7 rate |
|---|---|
| uniform | {= pc(POP('4c4e', 0)) =} ✓ |
| end state of a 5-move RZP, same side | {= pc(POP('4c4e', 1)) =} |
| the same, switched | {= pc(POP('4c4e', 2)) =} |

The switched state is exactly uniform again, for every DRM, because the inverse of a cube with a given case is uniform over that case. So every exhaustive table is right for the cases you actually switch. On the {= n(E['attempts_total']) =} real attempts, no DRM × RZP length is more than {= f2(E['uniform_worst_z']) =} standard errors off the uniform rate (section 6).

**After a switch the last-turn options are worth little.** Turning the RZP's last move the other way never changes the switched case ({= n(E['last_rzp'][0]) =} of {= n(E['last_rzp'][1]) =} pairs of attempts; proved in Lean ✓). For 4c4e (section 6), each row is an option; the points are its sub-7 rate minus the rate without it:

| Option (4c4e) | Sub-7 rate after a switch, without the option | With the option | Points added after a switch | Points added without a switch |
|---|---|---|---|---|
| EO's last turn | {= pc(OPT('4c4e', 0)) =} | {= pc(OPT('4c4e', 1)) =} | {= f1((OPT('4c4e', 1) - OPT('4c4e', 0)) * 100) =} | {= f1((VAR('4c4e', 'lastF_le6') - VAR('4c4e', 'plain_le6')) * 100) =} ✓ |
| other DR axis | {= pc(OPT('4c4e', 0)) =} | {= pc(OPT('4c4e', 2)) =} | {= f1((OPT('4c4e', 2) - OPT('4c4e', 0)) * 100) =} | {= f1((VAR('4c4e', 'two_le6') - VAR('4c4e', 'plain_le6')) * 100) =} |

**RZP length moves every band.** After a 4-move RZP (DR in 7 is enough), every 4c4e case with a paired edge is around 50% or more, and only the no-pair group stays low ({= pc(RCELL('4c4e', 3, 'p7')) =} ✓). After a 6-move RZP (DR in 5 needed), no common cell reaches 25%: 4c4e with both edges paired is {= pc(RCELL('4c4e', 0, 'p5')) =} ✓ and 3c2e is {= pc(RCELL('3c2e', 0, 'p5')) =} ✓ (section 4).

**The low DRMs have no cheap rescue.** For 4c6e, 3c4e, 3c6e, 5c4e, 5c6e and 6c6e, no rule of up to three traceable features puts more than {= pc(max(E['low_best'].values())) =} of their sub-7 cases into a cell above 50%. The best small cells, with their sub-7 rates:

| Cell | Sub-7 rate |
|---|---|
| 4c6e JZP ({= pc(RG('4c6e', 'switch', 'share')) =} ✓ of 4c6e) | {= pc(RG('4c6e', 'switch')) =} ✓ |
| 5c6e with 4 pairs | {= pc(RG('5c6e', 'check')) =} ✓ |
| 3c4e with 2 pairs | {= pc(RG('3c4e', 'check')) =} ✓ |

**Fanti's rule figures are any-turn numbers**: they allow F/B quarter turns, which break the EO. With the EO kept they move by about a point at most (4c2e switch success: {= pc(EV('doc583-4c2e', 'success ', ',')) =} any-turn, {= pc(EV('doc583-4c2e', 'EO-kept: success ', ',')) =} EO kept) (section 10).

**What it confirms or corrects**

- **Confirmed: the 4c2e rule.** "1.5+ pairs" (rodneykinney, [[T9468]]) switches exactly the same cases as Jay's 1 pair + 1 side pair or 2 pairs ([[T8144]]) and tseitsei89's version ([[T9321]]): {= pc(RG('4c2e', 'switch', 'share')) =} ✓ of 4c2e at {= pc(RG('4c2e', 'switch')) =} ✓. What I add is the other end: 0 or 0.5 is {= pc(RG('4c2e', 'discard')) =} ✓, so the rule settles {= pc(RULE('4c2e', 'decided')) =} ✓ of 4c2e.
- **Confirmed: the rest of the switch list.** rodneykinney's 5-6 pairs for 7c8e ({= pc(GR('78-rodney', 'precision')) =} ✓), "3c2e: just always switch" (tseitsei89, [[T9321]]: {= pc(RULE('3c2e', 'all', 'p6')) =} ✓), 1+ pairs for 2c2e ({= pc(GR('22-doc319', 'precision')) =} ✓), JZP-only for 4c6e, and Yura Riabov's "trash" ARMs for 4c4e (all under 4% ✓). The search found nothing cheap that does much better on those DRMs (section 9).
- **Confirmed: the NISS predictors.** The ARM axis swap, R/L stickers on U/D for corner ARM, rodneykinney's corner-case flow chart and wen's pair tracing each held on every one of {= n(NISS('ARM axis swap: ARM for U/D DR on normal = ARM for R/L DR on inverse (uniform)')[0]) =} sampled cubes. Louis's same-axis version, which Louis took back at the time, holds on only {= pc(NISS('ARM for U/D DR on normal = ARM for U/D DR on inverse, same axis')[1] / NISS('ARM for U/D DR on normal = ARM for U/D DR on inverse, same axis')[0]) =} (section 5).
- **Confirmed: the published tables.** {= n(E['repro']['match']) =} of {= n(E['repro']['n']) =} published numbers reproduce. The two that don't are sampled cells in Evan's *arm/pairs*, low by {= f3(float(REP('4c4e 2 pairs sub-7', 'ours', 'C13')) - float(REP('4c4e 2 pairs sub-7', 'published', 'C13'))) =} and {= f3(float(REP('4c4e 3 pairs sub-7', 'ours', 'C13')) - float(REP('4c4e 3 pairs sub-7', 'published', 'C13'))) =} (section 10).
- **Corrected** (errata, each with an example). One claim per row:

| Claim | Who | What the numbers say |
|---|---|---|
| 10 4c4e ARM sets can be sub-6 after a switch | Jay ([[T4256]]) | 11 ✓: AR-4c1e is missing |
| "no number of pairs will save 3qt corners" (4c2e) | rodneykinney ([[T8147]]) | 3qt corners (4b-0) with 2 pairs are {= pc(EV('T8147-3qt', '4b-0 2p ')) =} ✓ sub-7 |
| 1 pair + AR-21 with a corners, "< 5% otherwise" | Evan ([[D14402]]) | {= pc(EV('D14402-21-1p', 'a not stacked ', ' ')) =} ✓ |

- **Depends**: rodneykinney's "there aren't any 4-movers with 0 or 1 pairs" ([[T597]]) holds with side pairs counted, not for top pairs alone (first line below); and the 0-pair catch for that case misses the same case one U/D turn earlier (second line) (section 11).

```
F2 B2 R    // 4c4e with no top pair
D F2 B2 R  // 0 pairs, no fake pairs, missed by the 0-pair catch
```
