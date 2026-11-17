# When to switch an EO

You have an EO and an RZP, and you're deciding whether to switch: go to the inverse, keep the EO, and look for a short DR there. Right now the main thing people go by is the number of pairs on the inverse, sometimes with ARM or the corner case on top. This page asks whether there's a better policy that you can still run in a few seconds, and it grades every policy by what it *misses*: not switching a 4-mover hurts more than not switching a 5-mover, and both hurt more than switching something that turns out to be a 7. Everything is counted exactly over all {= n(R['N0']) =} EO-solved cases of one EO axis and one DR axis. The one sampled thing is a check on real attempts ({= n(R['real_attempts']['5']) =} 5-move EO + RZPs on {= n(R['real_scrambles']) =} uniformly random scrambles).

November 2026. A date in brackets is a link to that message on the FMC solvers Discord (#fmc-theory, #fmc-discussion or #non-dr-discussion). Docs and sheets are listed with links at the end. An earlier version of this page (13 November 2026) led with a different rule, the number of half turns to two bars. Section 7 says what that count is worth and why it isn't the recommendation here.

**This builds on** what the server already had. Most of the card is other people's reads put together:

- **The pairs policy**, as rodneykinney's [*DRM Subsets Meta*](https://docs.google.com/document/d/1Jnd1Qy_6b1W5dR5fZQScloMoMPR2LCAF7VPrgeTaRgg) puts it: one pair threshold per DRM, "Discard if not one of the identified subsets." It comes out of the decision trees of [*DRM Subsets*](https://docs.google.com/document/d/1AUQVrecEFZyR6okXAyJgtQZA-A0AJmAUevhJZlQMjAs). tseitsei89's short form: "So just simply if >1 pair = switch, else discard" ([[T9325]]).
- **Pairs + corner case.**
  - rodneykinney's corner cases 4a to 4d ([*DR - 4c4e Theory*](https://docs.google.com/document/d/1DsxAAB2WRfpgDR-VWZZrXq2W4y_YMXBufRRYNLAGGoU)), the [*DRM corner variant+pair stats*](https://docs.google.com/spreadsheets/d/174ClwBFl-T2zJAq8MVyK1bKsIIuzxQU0_XmQGv82LPQ) sheet and the rule that came with it ([[T8108]]).
  - rodneykinney's read for 0 pairs: "To catch this case, you can switch 4a-0 and 4d-2, but only if there also are no fake pairs" ([[T8123]]).
  - tseitsei89's working list ([[T9321]]), wen's and Jay's own versions ([[D14328]], [[D12085]]).
  - Evan's split of 1 pair + ARM 21 by corner type: "b corners - 29%", "d corners - 89%", "a corners - ~34% if corners are stacked, < 5% otherwise" ([[D14402]]), and "interestingly 4a corners are basically the same for all ar-2X" ([[D14348]]). That split is the base of the card's 1-pair rows.
  - wen's check on 1 pair: "1 pair then I check if it's 4d or one U/D turn away from 4d" ([[D14328]]).
- **Pairs + ARM.**
  - Louis's [*DRM/ARM average optimals*](https://docs.google.com/spreadsheets/d/13fSwUROzP0hZQV1Cn96GndWbPy4UrsHiYTaWFSeWtJs) and Evan's [*arm/pairs*](https://docs.google.com/spreadsheets/d/1YZYyokxYXwDdBTgN7ojpPAFHKKz48hCyNO2l6-iwmVk) sheet.
  - caycala's chart ([[D11016]]): for 4c4e it already has 1 pair with ARM 21 and 0 pairs with ARM 42, and its 7c8e list is this page's 7c8e card.
  - Fanti's rule sets with their measured performance (*armpairs_1.txt*, [[D15160]]). On the yardstick used here Fanti's 4c4e list is the best thing on the server for 4c4e.
- **The other reads the cards use.**
  - Side pairs and the 1.5+ pairs rule for 4c2e (rodneykinney, [[T9468]]; Jay, [[T8144]]).
  - wen's 3c2e rule with fake pairs and split pairs ([[D16512]]).
  - Daichi's dead 5-pair ARMs for 7c8e and JZP with b corners for 4c2e ([[D15161]]), and "8c8e 2 pair 42a is a good switch" ([[T11352]]).
  - Jay's 5c rule: "iirc, need 2 pairs + ar21 for 5c4e to be good (3 pairs if it's another arm), same for 5c6e but need one extra pair" ([[D12983]]).
  - bpaul's idea of looking at pairs per edge ([[D12986]]) and Yura Riabov's "From my experience with pairs 1 bar is worse than 2 pairs for most arms" ([[D12993]]).
- **How to read the inverse from normal**: wen's pair tracing in the [*Hitchhiker's Guide to DR*](https://docs.google.com/document/d/1E_5wSKvQFXXZY4f3xLM76qMUrVGp9Pe7vgotS0X-T4U), rodneykinney's side-pair read in [*Domino Setup Theory*](https://docs.google.com/document/d/1Z3O8BY1LbAMF6m55ufXtSdtBVwSJpMArtRrDT-p_CwM) and the corner-case flow chart in *DR - 4c4e Theory*, Jay's ARM by colour ([[T4389]]).
- **The two bars** as the 4c4e target: Andrew's video [*How to do Domino Reductions: The Secret They Don't Want You To Know*](https://www.youtube.com/watch?v=oAbPQOfui2U) (FewestMoves channel, 2019) and *DR - 4c4e Theory* ("The final trigger must have two full “bars” formed with the bad corners and edges.").
- **Cale's [*DR setup stats*](https://docs.google.com/spreadsheets/d/11bTZ4Y7_6qKlIWo4a4TLW45M2ZkctQZAVxgQqEtlUs0)** for the DR length of every case, and two of my own studies: [*EO to DR, and scramble to DR*](../eo-to-dr/) (the same table, proved in Lean) and [*Judging a DR by hand*](../judging-a-dr/) (what a move of DR length is worth at the finish).

**What this adds**:

- **A yardstick that counts misses by length.** For every policy: how much it switches, and which share of the 4-or-less, the 5-movers and the 6-movers it leaves on the table. The current rules hadn't been broken down that way.
- **A switch card per DRM**: pairs first, then one or two more looks that depend on the pair count. On 4c4e, 4c2e, 3c2e and 7c8e together it switches a little less than the pairs policy and misses less at every length.
- **Four reads that I didn't find in anyone's rule**:
  - for 2 pairs on one edge, where the two holes are, and whether there are 2 fake pairs;
  - for 1 pair with ARM 21 and 4b corners, whether there's exactly one side pair;
  - for 1 pair with Evan's stacked 4a corners, whether there's a side pair, which also makes them a switch at ARM 20 and 22;
  - for 0 pairs and no fake pairs (rodneykinney's read), that the corners are 2 and 2 in the layers.
- **How often each read is needed.** ARM, the fast one, on every 1-pair case. The slower ones (the corners, the side pairs) on a minority, with what the card is worth if you drop any of them.
- **New cards for 8c8e and 2c2e**, and side pairs in the 5c pockets.
- **The half-turn count judged as a switch test**, on what it catches and on what it takes to read.
- **What doesn't help**, and **how far any rule could go** from the quick reads, so you know what's left on the table.
- **Every read done on the normal side by colour**, checked on {= n(65000) =} random cubes.

**Terms**, as the server uses them. *Switch* means NISS: after EO + RZP you go to the inverse and keep the EO. *DRM* is bad corners then bad edges (4c4e), counting all edges out of DR. *AR* (axial reduction) is the state you can finish with DR moves on the R/L axis, and *ARM* is how far you are from it, two digits, corners then edges (21 = AR-2c1e). *Pairs* are top pairs, *fake pairs* are the same two pieces with the corner twisted the other way, *side pairs* are E-slice pairs. A *bar* is two pairs on one edge. *4a* to *4d* are rodneykinney's corner cases, with the corner ARM as suffix (4b-0). *JZP* is ARM 00 with an even number of bad corners. *Sub-7* is a DR in 6 or less with the EO kept, and an *N-mover* is a case whose shortest such DR has N moves. One word is not the server's: a *hole* is an E-slice place of the inverse that holds a U/D edge. On normal you see it as an E-slice edge that's out of the slice. Section 3 has the exact definitions, section 6 how to read each thing before you switch.

**How to read it.**

- **Start with [section 1](#1-the-short-version)**. If you only want the rule, it's the 4c4e card there and the other cards in [section 5](#5-the-cards).
- **[Section 6](#6-reading-the-card-on-normal-and-how-long-it-takes)** is how each read looks on the cube in your hand. The **[worked examples](examples.html)** are real attempts to play along with: what you see, what the card says, what the pairs rule says, and the DR after the switch, folded away.
- **Sections 7 to 10** are the evidence: the two-bars count, what didn't work, the ceilings, other RZP lengths. Anything marked **computer only** is an answer key, not something to do in an attempt.
- **The [errata](errata.html)** have one statement from the server that the numbers go against.

---

{{CONTENTS}}

---

## 1. The short version

**Is there a better switch policy than pairs? Yes, and it stays a matter of seconds.** On 4c4e it switches as much as 2+ pairs and misses no case of 4 or less and {= pc(X44['card']['miss_d5']) =} of the 5-movers, where 2+ pairs misses {= pc(B('4c4e', 'pairs')['miss_le4']) =} and {= pc(B('4c4e', 'pairs')['miss_d5']) =}. Keep counting pairs first. What changes is the look you take after it, which depends on the pair count: ARM on 1 pair, which is fast, then the corners and the side pairs on the few ARMs where they matter. No quick read beats pairs as the first look: I tried every relation between two bad pieces, points systems, corner-only counts and trees that don't start from pairs, and pairs stays the first split every time (section 8).

**The yardstick.** After a 5-move RZP a case is *good* if the DR after the switch is 6 or less. A policy is graded on four numbers: how much it switches, and the share of the 4-or-less, of the 5-movers and of the 6-movers that it doesn't switch. When one number is needed, a declined 6-mover costs 3 wasted switches, a 5-mover 9 and a 4-or-less 27 (section 3 says where that comes from, section 10 what happens with other prices).

**4c4e: the card.** One row per group of switched cases. The last three columns say how much of all of 4c4e's 4-or-less, 5-movers and 6-movers sits in the group.

{{ t_card('4c4e', ('switch', 'time')) }}

Everything else is a skip: 1 pair with any other ARM, 0 pairs with a fake pair, and the exceptions inside the 1-pair rows: 4b corners with exactly one side pair ({= grate('4c4e', '1 pair, ARM 21, 4b corners, exactly 1 side pair') =} sub-7), 4a corners that aren't in two columns ({= grate('4c4e', '1 pair, ARM 20, 21 or 22, 4a corners not in two columns') =}) or that have no side pair ({= grate('4c4e', '1 pair, ARM 20, 21 or 22, 4a corners in two columns, no side pair') =}).

**What it's worth on 4c4e.** Each row is a policy. *Cost per case* is the one-number version: misses and wasted switches, priced as above, per 4c4e case.

{{ t_cmp('4c4e') }}

So against **2+ pairs** the card switches the same share of 4c4e ({= n(X44['card']['switch'] * X44['n']) =} cases against {= n(B('4c4e', 'pairs')['switch'] * X44['n']) =}) and misses less at every length: no 4-or-less at all (pairs: {= n(B('4c4e', 'pairs')['missn_le4']) =} of {= n(X44['n_le4']) =}), {= pc(X44['card']['miss_d5']) =} of the 5-movers instead of {= pc(B('4c4e', 'pairs')['miss_d5']) =}, {= pc(X44['card']['miss_d6']) =} of the 6-movers instead of {= pc(B('4c4e', 'pairs')['miss_d6']) =}. Against **pairs + ARM** (Fanti's list) it switches {= pts(B('4c4e', 'pairs+arm')['switch'] - X44['card']['switch']) =} less, misses no 4-or-less (Fanti's list: {= n(B('4c4e', 'pairs+arm')['missn_le4']) =}) and a few 5-movers fewer, and leaves more 6-movers ({= pc(X44['card']['miss_d6']) =} against {= pc(B('4c4e', 'pairs+arm')['miss_d6']) =}). Take the two *if you have time* groups as well and you miss less than Fanti's list at every length, for {= pts(X44['card_time']['switch'] - B('4c4e', 'pairs+arm')['switch']) =} more switches. Fanti's list is exactly the best rule there is on the pair count and ARM alone (section 9). What the card adds to those two reads is where the pairs sit, a look at the corners on 1 pair with ARM 20, 21 or 22, and the edges out of the slice on a bar. Leave that last read out and switch every 2-pair case, and the card still misses less than Fanti's list at every length ({= pc(AF['no_bar_split']['miss_le4']) =}, {= pc(AF['no_bar_split']['miss_d5']) =} and {= pc(AF['no_bar_split']['miss_d6']) =}) for {= pts(B('4c4e', 'pairs+arm')['switch'] - AF['no_bar_split']['switch']) =} fewer switches (section 6).

**The four DRMs people switch, together.** 4c4e, 4c2e, 3c2e and 7c8e, every case once ({= n(nmain()) =} cases):

{{ t_main4() }}

**What's in the card, and whose it is.**

- **2 pairs on one edge is not 2 pairs on two edges** (new here). Two edges: {= grate('4c4e', '2 pairs on two edges') =} sub-7. A bar: it depends on the two holes. Holes on one R/L face (the two E-slice edges that are out of the slice share red or orange): {= grate('4c4e', '2 pairs on one edge (a bar), holes on one R/L face') =}. Otherwise {= pc(AF['bar_off']['rate']) =}, which is {= pc(AF['bar_off']['share']) =} of 4c4e that the pairs rule switches at a 1-pair rate. The exception is a bar with 2 fake pairs: {= grate('4c4e', '2 pairs on one edge (a bar), holes not on one R/L face, 2 fake pairs') =} even with the holes off. bpaul asked about pairs per edge and Yura Riabov said a bar is worse. The holes are what makes it a rule.
- **1 pair + ARM 21, by corner type** (Evan's split, exact: 4d {= pc(EX['p1_arm21_by_cc']['d']['rate']) =}, 4b {= pc(EX['p1_arm21_by_cc']['b']['rate']) =}, 4a in two columns {= pc(AF['stacked']['21']['rate']) =} and {= pc(AF['stacked']['not_stacked_21']['rate']) =} otherwise). New here is what the side pairs do inside it. They split the 4b cases: with none it's {= pc(EX['4b_side']['0']['rate']) =}, with exactly one {= pc(EX['4b_side']['1']['rate']) =}, with two {= pc(EX['4b_side']['2']['rate']) =}. And they split Evan's stacked 4a: {= pc(AF['stacked']['21_side']['rate']) =} with a side pair, {= pc(AF['stacked']['21_noside']['rate']) =} without.
- **Stacked 4a with a side pair is a switch at ARM 20 and 22 too.** Evan saw it: "interestingly 4a corners are basically the same for all ar-2X" ([[D14348]]). And wen's check on 1 pair, "4d or one U/D turn away from 4d" ([[D14328]]), has the short ones: all {= n(AF['one_from_4d']['yes']['d5']) =} 5-movers with 1 pair and 4a corners are one U/D turn from 4d. 1 pair with ARM 20 or 22 is {= pc(AF['stacked']['p1_2022']['rate']) =} sub-7 overall and the ARM lists skip it, but its 4a corners in two columns with a side pair are {= n(AF['stacked']['2022_side']['n']) =} cases at {= pc(AF['stacked']['2022_side']['rate']) =}, with every one of its {= n(AF['stacked']['p1_2022']['d5']) =} 5-movers. New here are the side pair and the exact numbers. With 4d corners ARM 20 and 22 are {= pc(AF['stacked']['p1_2022_4d']['rate']) =}, as Evan said.
- **0 pairs: no fake pairs either, and the corners 2 and 2.** No fake pairs with 0 pairs is rodneykinney's read for the `F2 B2 R` setups, and wen has it for `D F2 B2 R` ("there are 2 'columns' of corners and no fake pairs", [[D14333]]). Adding that the misoriented corners are two white and two yellow gives {= gshare('4c4e', '0 pairs, no fake pairs, corners 2 and 2 in the layers') =} of 4c4e that holds every 0-pair case of 4 moves or less:

{{ wit('0p_4mover', '4c4e, 0 pairs, no fake pairs, 2 white and 2 yellow corners', 'DR in 4. The pairs rule says discard') }}

**The other DRMs** (section 5). One row per DRM, the card against everything in that DRM:

{{ t_all_card() }}

- **4c2e**: 1.5+ pairs stays, plus two small groups: 0 pairs with JZP and 4b corners (Daichi's read), and 1 pair without a side pair when the corners are 4b-0 (in rodneykinney's corner table).
- **3c2e**: wen's rule is the card (a pair, a fake pair or a split pair). What it skips is {= gshare('3c2e', '0 pairs, no fake pair, no split pair') =} of 3c2e at {= grate('3c2e', '0 pairs, no fake pair, no split pair') =}, with no 5-mover in it, as wen said.
- **7c8e**: caycala's chart is the card. Fanti's list is the same thing without the chart's ban on edge ARM 0 and 4.
- **8c8e and 2c2e**: new cards (section 5.5). The 8c8e one costs {= f3(D('8c8e')['card']['loss']) =} per case against {= f3(B('8c8e', 'pairs')['loss']) =} for the tree rule.
- **The low DRMs hold {= lowshare('d5') =} of the 5-movers.** Counting the 12 DRMs of this page, 4c6e, 3c4e, 3c6e, 5c4e, 5c6e and 6c6e hold {= lowshare('le4') =} of the 4-or-less, {= lowshare('d5') =} of the 5-movers and {= lowshare('d6') =} of the 6-movers. Small pockets hold a good part of them (5c4e with 3 pairs and 2 side pairs is {= grate('5c4e', '3 pairs, 2+ side pairs') =}), but a short DR out of 5c4e costs about {= timeratio('5c4e') =} times the tracing and switching it costs out of 4c4e (section 5.6).

**How long it takes.** Every read on the card is a count or a colour match on the pieces you already look at for the pair trace: the U/D edges in the E slice, the misoriented corners, and the E-slice edges that are out. None of them needs you to work out where a piece sits on the inverse. On {= pc(EX['reads44']['two_plus'] - EX['reads44']['bar_lt2fake'] + EX['reads44']['zero'] - EX['reads44']['zero_nofake']) =} of 4c4e cases the pair trace settles it. ARM, the fast read ("Arm is very fast to check for me", Yura Riabov, [[D14249]]), is asked for on every 1-pair case, {= pc(EX['reads44']['one_pair']) =} of them. The slower reads come up much less: a look at the corners on 1 pair with ARM 20, 21 or 22 ({= pc(EX['reads44']['one_pair_arm2x']) =} of cases), and the side pairs after it on {= pc(EX['reads44']['one_pair_arm21_4b'] + EX['reads44']['stacked_2x']) =}. That's {= extra_looks() =} extra looks per 4c4e RZP on average, on top of a pairs + ARM check that Yura Riabov puts at "Like 5 seconds" ([[D14244]]). I haven't timed anyone on the card itself, so that's an argument from what the reads are and how often they come up, not a measurement (section 6).

**Two bars: a good read, not a switch test yet.** The numbers are good. Switch at 2 half turns or fewer and you switch {= pc(TB['le2']['switch']) =} of 4c4e, with every 4-or-less in it, including all {= n(TB['pairs_missed_le2']['le4'][0]) =} that the pairs rule misses and {= frac(TB['pairs_missed_le2']['d5']) =} 5-movers it misses. Its cost per case is {= f3(TB['le2']['loss']) =}: better than any list on the server, behind the card ({= f3(X44['card']['loss']) =}), because it leaves {= pc(TB['le2']['miss_d6']) =} of the 6-movers. On top of the card it would help: the card plus *2 or fewer* costs {= f3(TB['card_or_le2']['loss']) =}.

The problem is reading it. The count needs the place of all eight bad pieces on the inverse and then a search, where the card needs colour matches. Zagros is convinced full NISS tracing of 4c4e is the way ("I think the optimal system is 100% niss tracing 4c4e", [[D15171]]), tried it, "did it for like four solves and gave up", because "I niss trace and then I just don't know if it has a 6 move DR or not. I need to actually do a few moves to check" ([[D16255]]). caycala timed a whole switch at about 20 seconds and concluded about tracing instead: "tldr i dont think it’s worth it + it is much more mistake prone" ([[D12776]]). The count is exactly a way to judge the DR after a trace, so it might be what Zagros was missing, but nobody has shown it done in a few seconds. Until someone does, I don't recommend it as the test before switching. If you can read it, add *2 or fewer: switch* to the card (section 7).

**How much is left.** **Computer only**: the best rule that uses every quick read at once ({= n(X44['ceil']['quick']['cells']) =} cells for 4c4e) would switch {= pc(X44['ceil']['quick']['switch']) =}, miss no 5-mover and {= pc(X44['ceil']['quick']['miss_d6']) =} of the 6-movers. So the information is in the colours. It just doesn't fit in a rule you can carry: going from the card's {= len(X44['groups']) =} groups to 40 only moves the cost from {= f3(X44['card']['loss']) =} to {= f3(EX['trees_free']['40']['loss']) =} (section 9).

**Other RZP lengths.** After a 4-move RZP a DR in 7 is enough, and {= pc(X44['K7']['always']['precision']) =} of 4c4e has one. At the same prices every group of the card is then worth a switch, the 0-pair leftovers included, so "It seems like you should pretty much always switch a 4 move DR-4c4e." (Zagros, [[D18940]]) holds. After a 6-move RZP only 3 or 4 pairs and 1 pair with ARM 21 and 4d corners are left (section 10).

---

## 2. What was asked

**Is there a better switching policy than pairs, with ARM and the corner case for some cases?** A way to switch more good cases or fewer bad ones, computable by a human from the cube state in seconds, without a full NISS trace of the bad pieces, where missing a good continuation counts for more than switching a bad one. *Answer*: the cards of section 5, graded in section 4 against the current policies. The gain over pairs is real and costs no extra switches overall (fewer on 4c4e, 3c2e and 7c8e, more on 4c2e). The gain over the pairs + ARM lists is small.

**Is the two-bars count fast enough to use?** *Answer*: nobody has shown that it is, and what people have said points the other way. Its numbers are good, so it's worth someone trying (section 7).

**The same questions, as people on the server asked them.**

- wen ([[D14349]]): "Interestingly now we have basically 3 criteria for NISS that we can trace, >1pair/ARM/corner structure", "if we pick 2 out of 3 to stick to, which gives the lowest false negative rate?" *Answer*, with the best rule each pair of reads allows (section 9, **computer only**): on 4c4e pairs + ARM misses the least of the short ones ({= pc(X44['ceil']['pairs+arm']['miss_d5']) =} of the 5-movers, against {= pc(X44['ceil']['pairs+case']['miss_d5']) =} for pairs + corner case), and it switches more to do it. Nothing without pairs is close.
- wen ([[T8125]]): "I personally think that the false positive rate isn't that important because switching something that ends up being bad isnt the worst thing, it's much worse to not switch something that is actually good, but the method says don't switch". And later: "false negative are more important because it will be the one that has an 18 then you will be sad" ([[D14400]]). That's the yardstick of this page. The other side, for the record: "false positives are more important because i only have time to fully check a few EOs, and if im switching an RZP then i damn well better get a short DR out of it, lmao" (compLex, [[D14406]]), and rodneykinney on 2+ pairs: "It does miss some good cases, but I never have enough time to NISS every EO, so I'm mostly looking for excuses to avoid NISSing, and this is a pretty good one." ([[T3225]]). The tables give all four numbers, so you can read them your own way.
- tseitsei89 ([[T9334]]): "It would be really nice to find a way to filter out good 1 pair cases but there doesnt seem to be one currently". *Answer*: ARM 21 first, then Evan's corner types, then the side pairs for 4b (section 5.1). That takes the switched 1-pair cases from {= pc(EX['p1_arm21']['rate']) =} sub-7 (all of 1 pair + ARM 21) to {= pc(EX['p1_arm21_card']['rate']) =}.
- bpaul ([[D12986]]): "random thought i wonder whether looking at pair stats not just on the count but also based on the number of pairs per edge could be good". *Answer*: yes for 2 pairs on 4c4e, once you add where the holes are (section 5.1).
- Zagros ([[D14350]]), on not wanting to miss anything when switching: "seems like that would cause an absurd amount of rescrambling, maybe I'm just far too slow at solving at 3x3". *Answer*: here's the number. Missing no case of 5 or less on 4c4e by pairs and ARM alone means switching {= pc(EX['pairs_arm_no_miss5']['switch']) =} of the cases. The card with its *if you have time* groups gets to {= pc(X44['card_time']['miss_d5']) =} of the 5-movers missed at {= pc(X44['card_time']['switch']) =}.

What's left open is in section 12.

---

## 3. Definitions and the yardstick

Everything is written for an F/B EO and a DR on U/D. With white on top and green in front the U/D colours are white and yellow, the F/B colours green and blue, the R/L colours red and orange. Other axes are the same thing turned.

**Case, switched case.** What matters for the DR is the *case*: which corners are twisted and how, and which places hold the four E-slice edges (2187 × 495 = {= n(R['N0']) =} cases). After EO + RZP you have a case on normal. Switching means doing the DR on the inverse with the EO kept, so the case that matters is the inverse's, the *switched case*. Every rule here is about the switched case, read from the normal side (section 6).

**DR length, good.** The fewest turns of U, D, R, L, F2, B2 that take the switched case to DR (linear, EO kept). After a 5-move RZP a case is *good* if that's 6 or less, the usual sub-7: "we are normally looking for rzp in 5 or less and dr in 11 or less. So sub-7 from 5 move rzp gives that" (tseitsei89, [[D15188]]). For a 4-move RZP good means 7 or less, for a 6-move RZP 5 or less (section 10).

**What a policy is graded on.** A policy says switch or don't for every case of a DRM. Its grade is four numbers:

- *Switched*: the share of the DRM's cases it switches.
- *Missed: 4 or less*, *missed: 5-movers*, *missed: 6-movers*: of the cases with a DR that long, the share it doesn't switch.

If policy A switches no more than B and misses no more at each of the three lengths, A is better whatever you think a miss is worth. Where neither wins that way you need prices.

**The prices.** A switch that finds no DR in 6 costs 1. Not switching a 6-mover costs 3, a 5-mover 9, a 4-or-less 27. *Cost per case* is the total over the DRM divided by its cases, so lower is better. Two choices went into that:

- *Each move shorter counts three times as much.* A DR one move shorter leaves one more move for the finish. Over every DR state, an optimal finish in 10 or less is 0.74%, in 11 or less 3.6%, in 12 or less 15%, in 13 or less 44% (from *Judging a DR by hand*). So one move of DR length is worth a factor of 4 to 5 in the odds of a tight result and about 3 for a loose one. I use 3, the careful end, so the short cases aren't over-weighted. That's the asymmetry the grading has to carry: a declined 4-mover is worth nine declined 6-movers.
- *A declined 6-mover costs 3 wasted switches.* With that, a group whose good cases are all 6-movers is worth switching from 25% sub-7, and a group with 4c4e's usual mix of lengths from about 16%. The server's own cut-offs sit around there: "i switch for around 20% and above" (Yura Riabov, [[D7082]]), "I would say below 20% is never and above 30% is pretty much always.", with "Of course as we get better estimators and statistics those might/will change." (tseitsei89, [[T9318]]), "i think it's best to find the <10% ones and dont switch for those and switch everything else maybe" (wen, [[D7081]]).

Section 10 redoes the comparison with a 6-mover at 2 and at 5 and with a factor of 2 and of 4.5. The card stays ahead of every current policy in each of them, and at 5 its wider version is the cheapest.

**The reads.** All on the switched case; section 6 has each one as you see it on normal.

- *Pairs*: a bad edge in the U or D layer (an E-slice edge sitting there) and a bad corner next to it in its layer, twisted so that its U/D sticker is on the side face the edge doesn't touch. As after R from solved, which has 4 pairs. *On one edge* or *on two edges* says where 2 pairs are. Two on one edge is a *bar*.
- *Fake pair*: the same two pieces with the corner twisted the other way.
- *Side pair*: a bad edge in the E slice (a U/D edge sitting there) and the corner above or below it with its U/D sticker on F or B.
- *ARM*: corner ARM is the number of bad corners with their U/D sticker on R or L, edge ARM the number of bad edges in the M slice (at UF, UB, DF, DB). A piece that doesn't count is *in AR*. ARM 21 is what `U' R` leaves.
- *Corner case*, for four bad corners: by how they split between the two HTR orbits. 4d is all four in one orbit, 4c is 3 and 1. 2 and 2 is 4b if some U, D, R or L face has exactly 1 or 3 of them, and 4a otherwise. The suffix is the corner ARM (folded to 0 to 2, except for 4a).
- *Columns*: a column is the two corner places above each other. Four bad corners are *in two columns* when each one sits above or below another one. That's Evan's *stacked*.
- *Holes*: the E-slice places that hold a U/D edge. With two holes: on one R/L face (FR and BR, or FL and BL), on one F/B face, or diagonal.
- *Layers*: how many bad corners are in the U layer and how many in the D layer (*2 and 2*, *3 and 1*, all in one).
- *Split pair* (wen, for 3c2e): a bad edge and a bad corner in the same layer, not next to each other, both in AR or both out of AR.

**Verdicts.** *Switch*: the group is worth it at the prices above. *If you have time*: the next groups down, between about 15% and 25% sub-7. They're just under break-even at these prices and above it for anyone who prices a 6-mover higher. *Skip*: the rest.

**Populations.** *Exact*: every case of the DRM counts once. That's the right weighting for switched cases. Do any sequence of DR moves (U, D, R2, L2, F2, B2) before the scramble: the case on normal stays what it was (same EO, same RZP, same DRM), and the inverse runs evenly over every case with the same DRM and the same number of clockwise and counter-clockwise corners. Both scrambles are equally likely, so whatever you did on normal, the switched case is uniform over those. For 4 bad corners that's the whole DRM. For 8c8e it's two classes, 4 and 4 or 7 and 1 (section 12). *Real attempts*: {= n(R['real_scrambles']) =} uniformly random scrambles, every EO of up to 5 moves on every axis and side, every RZP after it that first reaches its DRM at a total of 5 moves: {= n(R['real_attempts']['5']) =} switched cases. It's a sample, used as a check (section 10).

---

## 4. The current policies, by what they miss

Three kinds of rule are in use. Here's each as its author wrote it, graded on 4c4e. Each row is a policy.

{{ t_cmp('4c4e', time=False) }}

**Pairs only.** 2+ pairs switches {= pc(B('4c4e', 'pairs')['switch']) =} of 4c4e at {= pc(B('4c4e', 'pairs')['precision']) =} sub-7. What it leaves behind: {= n(B('4c4e', 'pairs')['missn_le4']) =} of the {= n(X44['n_le4']) =} cases of 4 or less, {= n(B('4c4e', 'pairs')['missn_d5']) =} of the {= n(X44['n_d5']) =} 5-movers and {= n(B('4c4e', 'pairs')['missn_d6']) =} of the {= n(X44['n_d6']) =} 6-movers. So a fifth of the 5-movers have 0 or 1 pair. Here's one with 1 pair, ARM 21 and 4d corners:

{{ wit('1p_4d_4mover', '4c4e, 1 pair, ARM 21, 4d corners', 'DR in 4') }}

**Pairs + corner case.** Adding 4d for 1 pair (tseitsei89, rodneykinney) gets most of the 4-or-less back and little else: the 5-movers go from {= pc(B('4c4e', 'pairs')['miss_d5']) =} missed to {= pc(B('4c4e', 'pairs+case')['miss_d5']) =}. wen's version (1 pair with 4d corners or one U/D turn from 4d; 0 pairs if it's anti-AR, every bad piece out of AR, or the `D F2 B2 R` case) does better, {= pc(B('4c4e', 'wen')['miss_d5']) =}.

**Pairs + ARM.** 1 pair with ARM 21 was on caycala's chart in April 2025, next to 0 pairs with ARM 42, and ben kyle wrote "I've gotten a lot better results recently from blindly switching 2 pairs and 1pair + arm2c1e since it's so fast to check" ([[D13420]]). Fanti's list is that with every 2-pair case and JZP for 0 pairs. It misses {= pc(B('4c4e', 'pairs+arm')['miss_d5']) =} of the 5-movers and {= pc(B('4c4e', 'pairs+arm')['miss_d6']) =} of the 6-movers, the least of any rule on the server, and pays for it with {= pc(B('4c4e', 'pairs+arm')['switch']) =} of 4c4e switched. It's also exactly the best rule you can build from the pair count and the two ARM digits at these prices: the search of section 9 lands on the same list. Fanti's own figures for it, "35.2% switches", "42.6% sub-7 switch success (15.0% total)" and "4.3% of cases will be discarded with sub-7", come out at {= pc(B('4c4e', 'pairs+arm')['switch']) =}, {= pc(B('4c4e', 'pairs+arm')['precision']) =} and {= pc(B('4c4e','pairs+arm')['miss_good'] * X44['sub7']) =} with the EO kept.

**Where the room is.** Two places.

- *Inside 2 pairs.* Most people switch every 2-pair case ("2 pairs I just always switch.", tseitsei89, [[D14265]]; "I just switch regardless", wen, [[D14395]]). rodneykinney's rule and compLex drop 4b-0, and caycala's chart keeps 2 pairs only with some ARMs. {= pc(AF['bar_off']['share']) =} of 4c4e is a bar with the holes off the R/L faces, at {= pc(AF['bar_off']['rate']) =}.
- *Inside 1 pair + ARM 21.* It's {= pc(EX['reads44']['one_pair_arm21']) =} of 4c4e, and {= pc(grp('4c4e','1 pair, ARM 21, 4b corners, exactly 1 side pair')['share'] + AF['stacked']['not_stacked_21']['share']) =} of 4c4e inside it is under 6% sub-7.

Both are places where a list *switches too much*. Dropping them is what pays for switching the good 0- and 1-pair groups without more switches in total. The one place where every list switches too little is 1 pair with ARM 20 or 22: {= pc(AF['stacked']['p1_2022']['rate']) =} sub-7 overall, with {= n(AF['stacked']['p1_2022']['d5']) =} 5-movers that all sit in one small group (section 5.1).

The same grading for the other DRMs is in section 5 and appendix A.

---

## 5. The cards

Every card starts with the pair count, because no other quick read comes close as a first look (section 8). After that it's one or two looks, and which ones depends on the DRM and the pair count. The groups of a card don't overlap and cover the whole DRM. All numbers are exact, every case of the DRM once.

How the cards were found: a search over short rule lists on the quick reads, scored with the prices of section 3, then written down by hand in the server's words and graded again (appendix B). Where the search landed on a rule somebody already had, the card is that rule and says whose.

### 5.1 4c4e

{{ t_card('4c4e') }}

Read it top down:

- **3 or 4 pairs**: switch.
- **2 pairs**: on two edges, switch. On one edge with 2 fake pairs, switch. On one edge otherwise, look at the two E-slice edges that are out of the slice. If they share red or orange, switch. If not, it's an *if you have time* case.
- **1 pair**: check ARM.
  - ARM 21: look at the corners. 4d: switch. 4b: switch unless there's exactly one side pair. 4a: switch if the corners are in two columns and there's a side pair.
  - ARM 20 or 22: only the last of those. 4a corners in two columns with a side pair: switch. Anything else: skip.
  - Any other ARM: skip. The one *if you have time* pocket is ARM 10 or 11 with 2 or 3 side pairs.
- **0 pairs**: switch only if there's no fake pair either and the misoriented corners are two white and two yellow.

**The bar.** 2 pairs on one edge, by where the holes are and the fake pairs. Each row is a group:

| 2 pairs on one edge | Share of 4c4e | Sub-7 rate | 5-movers |
|---|---|---|---|
| holes on one R/L face | {= pc(AF['bar_on']['share']) =} | {= pc(AF['bar_on']['rate']) =} | {= n(AF['bar_on']['d5']) =} |
| holes not on one R/L face, 2 fake pairs | {= pc(AF['bar_off_fake']['2']['share']) =} | {= pc(AF['bar_off_fake']['2']['rate']) =} | {= n(AF['bar_off_fake']['2']['d5']) =} |
| holes not on one R/L face, 1 fake pair | {= pc(AF['bar_off_fake']['1']['share']) =} | {= pc(AF['bar_off_fake']['1']['rate']) =} | {= n(AF['bar_off_fake']['1']['d5']) =} |
| holes not on one R/L face, no fake pair | {= pc(AF['bar_off_fake']['0']['share']) =} | {= pc(AF['bar_off_fake']['0']['rate']) =} | {= n(AF['bar_off_fake']['0']['d5']) =} |

A bar with the holes off and 2 fake pairs, 5 moves:

{{ wit('bar_fake2_5mover', '4c4e, 2 pairs on one edge, 2 fake pairs, holes on one F/B face', 'DR in 5') }}

**The side pairs on 4b.** 1 pair, ARM 21, 4b corners, by the number of side pairs. Each row is a count:

| Side pairs (1 pair, ARM 21, 4b corners) | Share of 4c4e | Sub-7 rate | 5-movers |
|---|---|---|---|
| 0 | {= pc(EX['4b_side']['0']['share']) =} | {= pc(EX['4b_side']['0']['rate']) =} | {= n(EX['4b_side']['0']['d5']) =} |
| 1 | {= pc(EX['4b_side']['1']['share']) =} | {= pc(EX['4b_side']['1']['rate']) =} | {= n(EX['4b_side']['1']['d5']) =} |
| 2 | {= pc(EX['4b_side']['2']['share']) =} | {= pc(EX['4b_side']['2']['rate']) =} | {= n(EX['4b_side']['2']['d5']) =} |

A 1-pair case the card switches and the pairs rule doesn't, 5 moves:

{{ wit('1p_4b_side2_5mover', '4c4e, 1 pair, ARM 21, 4b corners, 2 side pairs', 'DR in 5') }}

**Stacked 4a corners.** 1 pair and 4a corners, by ARM, by whether the corners are in two columns (Evan's stacked corners) and by side pairs. Each row is a group:

| 1 pair, 4a corners | Share of 4c4e | Sub-7 rate | 5-movers |
|---|---|---|---|
| ARM 21, in two columns, 1+ side pairs | {= pc(AF['stacked']['21_side']['share']) =} | {= pc(AF['stacked']['21_side']['rate']) =} | {= n(AF['stacked']['21_side']['d5']) =} |
| ARM 21, in two columns, no side pair | {= pc(AF['stacked']['21_noside']['share']) =} | {= pc(AF['stacked']['21_noside']['rate']) =} | {= n(AF['stacked']['21_noside']['d5']) =} |
| ARM 21, not in two columns | {= pc(AF['stacked']['not_stacked_21']['share']) =} | {= pc(AF['stacked']['not_stacked_21']['rate']) =} | {= n(AF['stacked']['not_stacked_21']['d5']) =} |
| ARM 20 or 22, in two columns, 1+ side pairs | {= pc(AF['stacked']['2022_side']['share']) =} | {= pc(AF['stacked']['2022_side']['rate']) =} | {= n(AF['stacked']['2022_side']['d5']) =} |
| ARM 20 or 22, in two columns, no side pair | {= pc(AF['stacked']['2022_noside']['share']) =} | {= pc(AF['stacked']['2022_noside']['rate']) =} | {= n(AF['stacked']['2022_noside']['d5']) =} |
| ARM 20 or 22, not in two columns | {= pc(AF['stacked']['not_stacked_2022']['share']) =} | {= pc(AF['stacked']['not_stacked_2022']['rate']) =} | {= n(AF['stacked']['not_stacked_2022']['d5']) =} |

The 4a corners that are one U/D turn from 4d (wen's check) are all in two columns, and they hold all {= n(AF['one_from_4d']['yes']['d5']) =} of these 5-movers: {= n(AF['one_from_4d']['yes_2x']['n']) =} cases with ARM 20, 21 or 22 at {= pc(AF['one_from_4d']['yes_2x']['rate']) =}. The card's row is wider. It also takes the stacked corners that aren't one turn from 4d when there's a side pair ({= n(AF['one_from_4d']['row_not']['n']) =} cases at {= pc(AF['one_from_4d']['row_not']['rate']) =}, {= n(AF['one_from_4d']['row_not']['d6']) =} 6-movers and nothing shorter).

Evan's stacked 4a corners with ARM 21, 5 moves:

{{ wit('1p_4a_cols_5mover', '4c4e, 1 pair, ARM 21, 4a corners in two columns, 2 side pairs', 'DR in 5') }}

The same with ARM 22, which every ARM list skips, 5 moves:

{{ wit('1p_4a_cols_arm22_5mover', '4c4e, 1 pair, ARM 22, 4a corners in two columns, 2 side pairs', 'DR in 5') }}

And stacked 4a corners with no side pair, 8 moves:

{{ wit('1p_4a_cols_noside_8mover', '4c4e, 1 pair, ARM 21, 4a corners in two columns, no side pair', 'DR in 8, and nothing shorter') }}

A 2-pair case the pairs rule switches and the card leaves for later, 8 moves:

{{ wit('bar_holes_bad_8mover', '4c4e, 2 pairs on one edge, holes on one F/B face', 'DR in 8, and nothing shorter') }}

And the card isn't free of misses. This 5-mover has 1 pair and ARM 32, and the card skips it like every other list does:

{{ wit('card_miss_5mover', '4c4e, 1 pair, ARM 32, 4c corners', 'DR in 5') }}

### 5.2 4c2e

{{ t_card('4c2e') }}

The same DRM, one row per policy:

{{ t_cmp('4c2e') }}

The 1.5+ pairs rule (2 pairs, or 1 pair and a side pair) is the top two rows, and it holds up: {= pc(B('4c2e', 'pairs')['miss_d5']) =} of the 5-movers missed. The card adds the two groups under it, and both were on the server:

- *0 pairs with JZP and 4b corners.* JZP for 0 pairs is in caycala's and Fanti's rules. The corners are Daichi's: "for 4c2e with 0p, I think niss tracing corner positions is worth it because JZP with b corners is way better than a corners" ([[D15161]]). Exactly: {= pc(EX['42_jzp_4b']['rate']) =} with 4b corners, {= pc(EX['42_jzp_4a']['rate']) =} with 4a.
- *1 pair with no side pair and 4b-0 corners*, {= grate('4c2e', '1 pair, no side pair, 4b-0 corners') =} sub-7. rodneykinney's corner table for 4c2e ([[T8140]]) switches it.

{{ wit('42_jzp_5mover', '4c2e, 0 pairs, JZP, 4b-0 corners', 'DR in 5. 1.5+ pairs says discard') }}

Fanti's 4c2e rule (any pair, or JZP) misses less than the card, {= pc(B('4c2e', 'pairs+arm2')['miss_d6']) =} of the 6-movers, and switches {= pc(B('4c2e', 'pairs+arm2')['switch']) =} of 4c2e to do it. rodneykinney's corner table is graded with 4a-2 let in, as Moritz pointed out ("4a-2 seems fine (great even) and only 4a-0 is not that great", [[T8148]]) and rodneykinney agreed ("4a-2 is good. 4b-2 is the bad case, because corners are 2qt, so 6 moves is the absolute minimum to DR", [[T8149]]). It misses fewer 6-movers than 1.5+ pairs and switches {= pts(B('4c2e', 'pairs+case')['switch'] - B('4c2e', 'pairs')['switch']) =} more.

### 5.3 3c2e

{{ t_card('3c2e') }}

The same DRM, one row per policy:

{{ t_cmp('3c2e') }}

"3c2e: just always switch" (tseitsei89, [[T9321]]) misses nothing and switches a {= grate('3c2e', '0 pairs, no fake pair, no split pair') =} group along with the rest. wen's rule ([[D16512]]) is exactly the cut the search finds, so it's the card. Its "At the very least you will never miss a 5 mover by doing this" is right: the skipped group has no 5-mover and no 4-mover, only 6-movers.

{{ wit('32_skip_6mover', '3c2e, no pair, no fake pair, no split pair', 'DR in 6, the best that group has') }}

### 5.4 7c8e

{{ t_card('7c8e') }}

The same DRM, one row per policy:

{{ t_cmp('7c8e') }}

The card is caycala's chart ([[D11016]]): never switch edge ARM 0 or 4 (with one exception that I read as ARM 10), 5 or 6 pairs always, 4 pairs with ARM 21, 31 or 43, 3 pairs with ARM 21. It's the best list on the server for 7c8e and the search has nothing to add to it. Fanti's list is the same without the edge-ARM ban, and Daichi said what the ban is worth at 5 pairs: "for 7c8e with 5p, 20/54 has a 0% chance of sub7" ([[D15161]]), which is exact. The *if you have time* row is Fanti's too: "also 78 4p has a weird silver lining with 11/12/33/41/62 where they're all just slightly worse so consider those if you want" ([[D15175]]).

{{ wit('78_5p_arm20', '7c8e, 5 pairs, ARM 20', 'DR in 7, the shortest any 5-pair ARM 20 case has') }}

5 or 6 pairs alone ([[T8142]]) misses {= pc(B('7c8e', 'pairs0')['miss_d5']) =} of the 5-movers. All of them are 4 pairs with ARM 21:

{{ wit('78_4p_arm21_5mover', '7c8e, 4 pairs, ARM 21', 'DR in 5') }}

### 5.5 8c8e and 2c2e

{{ t_card('8c8e') }}

The same DRM, one row per policy:

{{ t_cmp('8c8e') }}

The rule on the server is rodneykinney's tree: "The decision tree for 8c8e (all difficulties) actually identifies fake pairs <= 3 as the most important feature" ([[T9558]]), then edge ARM not 2, with a branch tseitsei89 read out for edge ARM 2 with 6 or more pairs ([[T9569]]). In 8c8e every corner is bad, so 3 or fewer fake pairs is the same as 5 or more pairs. What the tree leaves out is the even pair counts with ARM 42. 2 pairs with ARM 42 is Daichi's ("8c8e 2 pair 42a is a good switch", [[T11352]]), {= grate('8c8e', '2 pairs, ARM 42') =} sub-7. 4 pairs with ARM 42 is {= grate('8c8e', '4 pairs, ARM 42') =} and holds {= pc(grp('8c8e', '4 pairs, ARM 42')['d5'] / D('8c8e')['n_d5']) =} of 8c8e's 5-movers:

{{ wit('88_4p_arm42_5mover', '8c8e, 4 pairs, ARM 42', 'DR in 5. The tree rule says discard (4 fake pairs)') }}

{{ t_card('2c2e') }}

The same DRM, one row per policy:

{{ t_cmp('2c2e') }}

For 2c2e the side pair is the second read: 0 pairs with one side pair and ARM 00 or 11 is {= grate('2c2e', '0 pairs, 1 side pair, ARM 00 or 11') =}.

### 5.6 The low DRMs

The *DRM Subsets Meta* table says never for 4c6e, 5c4e, 5c6e and 6c6e, sometimes for 3c4e, and doesn't list 3c6e. On average that's right, they're 5% to 10% sub-7. But they're big DRMs: of the 12 DRMs on this page these six hold {= lowshare('le4') =} of the 4-or-less, {= lowshare('d5') =} of the 5-movers and {= lowshare('d6') =} of the 6-movers. And some people do switch them. Yura Riabov: "Not for every rzp but 5c ones are decent" ([[D12981]]). Jay's rule for the 5c ones (2 pairs with ARM 21 or 3 pairs for 5c4e, one pair more for 5c6e, [[D12983]]) is graded in appendix A: it costs {= f3(B('5c4e', 'jay')['loss']) =} per case on 5c4e against {= f3(B('5c4e', 'pairs')['loss']) =} for never.

The short ones sit in small pockets. The 5c pockets below are inside Jay's rule. What narrows them is the side pairs. Each row is a pocket worth switching:

{{ t_card('4c6e', ('switch', 'time')) }}

{{ t_card('3c4e', ('switch', 'time')) }}

{{ t_card('3c6e', ('switch', 'time')) }}

{{ t_card('5c4e', ('switch', 'time')) }}

{{ t_card('5c6e', ('switch', 'time')) }}

{{ t_card('6c6e', ('switch', 'time')) }}

A 5c4e that's 4 from DR after the switch:

{{ wit('54_pocket_4mover', '5c4e, 3 pairs, 2 side pairs', 'DR in 4') }}

**Is it worth the tracing?** Rough arithmetic, with 5 seconds for a trace (Yura Riabov's pairs + ARM time on 4c4e) and 20 for a switch (caycala's): seconds of tracing and switching per short DR found, if you trace every RZP of the DRM and switch what the card says.

{{ t_time() }}

So a short DR out of 5c4e or 5c6e costs about four times what it costs out of 4c4e, and that's with a 5-second trace, which is too kind for 5 or 6 bad corners. It's something for when the good DRMs have run dry, not a habit. The pockets do catch every 4-or-less of 4c6e, 3c6e, 5c4e and 5c6e.

---

## 6. Reading the card on normal, and how long it takes

You never look at the inverse. Three kinds of piece on the side you're on tell you everything the card asks:

- **the U/D edges sitting in the E slice** (white or yellow edges in the middle layer). On the inverse they're the bad edges in the U/D layers;
- **the misoriented corners** (no white or yellow on the U/D face). For each one, the colour it shows on the U/D face, and its two side stickers;
- **the E-slice edges that are out of the slice**. On the inverse they're the holes.

**The reads.** Each one is tagged with what it takes: *at a glance* (a count of colours), or *by tracing* (matching a few pieces against each other). Nothing here needs a search. The count of section 7 does.

- *Pairs*, by tracing (wen's tracing, [*Hitchhiker's Guide to DR*](https://docs.google.com/document/d/1E_5wSKvQFXXZY4f3xLM76qMUrVGp9Pe7vgotS0X-T4U)): "look at one of the edges in the E slice that don't belong there, then look at a misoriented corner, if the 2 stickers on the corner that are touching the E slice match with that E slice edge, then that's a pair on inverse". Do it edge by edge and you know for free whether 2 pairs are on one edge or on two.
- *Fake pairs*, free with the pair trace: a misoriented corner that has both colours of the edge but shows the edge's side colour on the U/D face. They're the near misses.
- *Edge ARM*, at a glance: how many of those U/D edges have green or blue as their other colour.
- *Corner ARM*, at a glance: how many misoriented corners show red or orange on the U/D face ("count the number of R/L stickers on the U/D face", *DR - 4c4e Theory*).
- *Corner case*, by tracing (rodneykinney's flow chart, same doc), for four misoriented corners with corner ARM 2: if some colour is on exactly 1 or 3 of the four corners it's 4b. If not, and two of the corners have two colours in common, 4a. Otherwise 4d.
- *4a in two columns*, by tracing: the four corners are two twins. Each twin is a white corner and a yellow corner with the same two other colours.
- *Side pairs*, by tracing (rodneykinney, *Domino Setup Theory*: "To predict side pairs on the inverse, look at the bad edges on the top/bottom faces. If there is also a bad corner showing the same color on the U/D face, then the inverse will have a side pair."). As checked: for each E-slice edge that's out of the slice, count the misoriented corners that carry both its colours and show the green or blue one on the U/D face.
- *Holes on one R/L face*, at a glance: the two E-slice edges that are out of the slice share red or orange. Sharing green or blue is one F/B face, sharing nothing is diagonal.
- *Corners 2 and 2*, at a glance: two misoriented corners are white, two are yellow.
- *Split pair*, by tracing: a U/D edge in the E slice and a misoriented corner with the same white or yellow that doesn't carry the edge's other colour. It counts when the edge has green or blue and the corner shows red or orange, or the other way round.

**The check.** Each read done on normal, by colour only, against the value on the inverse, on uniformly random EO-solved cubes (5,000 of each of the 12 DRMs and 5,000 with no DRM fixed):

{{ t_trace() }}

**One attempt, start to finish.**

```
{= W['attempt_1p_4b_side2']['scramble'] =}
{= W['attempt_1p_4b_side2']['eo'] =}   // EO on F/B, and it's already 4c4e
```

What's on the cube now:

- U/D edges in the E slice: {= ', '.join(W['attempt_1p_4b_side2']['edges']) =}.
- Misoriented corners: {= '; '.join(W['attempt_1p_4b_side2']['corners']) =}.
- E-slice edges out of the slice: {= ', '.join(W['attempt_1p_4b_side2']['out']) =}.

Pairs: white-blue needs a corner with white and blue on its sides, and there's none. White-orange has one (the white-blue-orange corner, showing blue). 1 pair. Two corners have an edge's colours the wrong way round, so 2 fake pairs. ARM: two corners show red or orange, one edge has blue, so 21. Corners: white is on two, yellow on two, green on one. One colour on exactly one corner: 4b. Side pairs: both blue-orange corners show blue, so 2. The card says switch (1 pair, ARM 21, 4b corners, 0 or 2 side pairs: {= grate('4c4e', '1 pair, ARM 21, 4b corners, 0 or 2 side pairs') =}). The pairs rule says discard.

```
({= W['attempt_1p_4b_side2']['dr'] =})   // DR on the inverse, {= W['attempt_1p_4b_side2']['d'] =} moves: {= 5 + W['attempt_1p_4b_side2']['d'] =} to DR
```

**How long.** I haven't timed anyone, so here's what the card asks for and what people have said the pieces of it take.

- *The pair trace is the base.* Everyone who switches by pairs does it already.
- *ARM is the fast read, and the card leans on it.* With pairs it takes Yura Riabov "Like 5 seconds", "±2", "That's for 4c4e btw, for 7c8e it's longer" ([[D14244]], [[D14245]], [[D14248]]), and "Arm is very fast to check for me", "It's like, just look at the cube" ([[D14249]], [[D14251]]). ben kyle switches 1 pair + ARM 21 blind "since it's so fast to check" ([[D13420]]). Daichi: "7c8e is probably just double my 4c4e times" ([[D14324]]). Not everybody reads it, though. In the same exchange Dunni says "I take longer to check only for pairs" ([[D14247]]) and dropped ARM: "Saves me from misrecognizing arm-2c1e, which definitely did not happen, ever" ([[D14255]]). And wen: "I don't even count ARM for 4c4e tbh" ([[D14326]]). The card asks for ARM on every 1-pair case, {= pc(EX['reads44']['one_pair']) =} of 4c4e RZPs, and nowhere else.
- *The slower reads are the corners and the side pairs, and the card keeps them to a minority of cases.* What it adds on 4c4e, by how often you need it. It comes to {= extra_looks() =} extra looks per RZP on average, {= f2(EX['reads44']['one_pair']) =} of that being ARM:

| Extra look (4c4e) | When | Share of 4c4e cases |
|---|---|---|
| none: the pair trace settles it | 3 or 4 pairs, 2 pairs on two edges, 2 pairs on one edge with 2 fake pairs, 0 pairs with a fake pair | {= pc(EX['reads44']['two_plus'] - EX['reads44']['bar_lt2fake'] + EX['reads44']['zero'] - EX['reads44']['zero_nofake']) =} |
| ARM | 1 pair | {= pc(EX['reads44']['one_pair']) =} |
| the corners: 4d, 4b or 4a, and if 4a, are they two twins? (with ARM 20 or 22 only the twins matter) | 1 pair and ARM 20, 21 or 22 | {= pc(EX['reads44']['one_pair_arm2x']) =} |
| the side pairs | 1 pair, ARM 21 and 4b corners; or 1 pair, ARM 20, 21 or 22 and 4a corners that are two twins | {= pc(EX['reads44']['one_pair_arm21_4b'] + EX['reads44']['stacked_2x']) =} |
| the two E-slice edges out of the slice: do they share red or orange? | 2 pairs on one edge, fewer than 2 fake pairs | {= pc(EX['reads44']['bar_lt2fake']) =} |
| white and yellow on the four corners | 0 pairs and no fake pair | {= pc(EX['reads44']['zero_nofake']) =} |

- *You can run the card with fewer reads, and here's what each one is worth.* Each row is a policy on 4c4e. Dropping the corner look at ARM 20 and 22 halves the cases that need it ({= pc(EX['reads44']['one_pair_arm21']) =} instead of {= pc(EX['reads44']['one_pair_arm2x']) =}) and gives back {= n(AF['stacked']['2022_side']['d5']) =} 5-movers. The edges out of the slice are the one read on the card that nobody on the server uses yet. If you'd rather not learn it, read the bar with ARM: switch a bar with ARM 00, 11, 21 or 31, or with 2 fake pairs. Or keep switching every 2-pair case.

{{ t_variants() }}

- *More ARM doesn't help.* Reading ARM on every row of the card, not just on 1 pair, and switching the best ARMs of each row would bring the cost from {= f3(X44['card']['loss']) =} to {= f3(AF['card_arm']['loss']) =} at best, with {= n(AF['card_arm']['cells']) =} row-and-ARM combinations to know. Nothing in there is worth a line.

- *Nothing on the card needs a place on the inverse.* Every read is of the kind *does this piece have these colours, and which one is on top*. That's the difference with a full NISS trace, where you work out where each piece goes.
- *The corner case is the slowest read on the card*, and it's only asked for on 1 pair with ARM 20, 21 or 22. People check corners on 1 pair today. tseitsei89: "I often check that if I trace 1 pair. It is usually very fast to see that it is NOT d  corners since if you see 3 of any one color or you see any 2 corners that share more than 1 color you instantly know it wont be d corners." ([[D14264]]). Evan, on checking the corner type with 1 pair + ARM 21: "I only started to recently but i think it's been beneficial" ([[D14405]]). With ARM 21 the corner ARM is 2, so the flow chart is two questions.
- *More reads, more chances to misread.* Dunni's ARM 21 is the example. I have no numbers on how often a read goes wrong, and a wrong read costs what a miss or a wasted switch costs.

If you only take one thing from the card, take 1 pair + ARM 21 with 4d corners, or with 4b corners and 0 or 2 side pairs. Those two rows are worth the most, then the stacked 4a row. The 2-pair split is what pays for them in switches.

---

## 7. Two bars, evaluated

**What it is.** A 4c4e is one R or L turn from DR when each layer has a bar and both holes are on that face. The *half turns to two bars* is the fewest half turns (R2, L2, F2, B2) that get there, with U and D turns free. The two bars as the target are in Andrew's 2019 video and in rodneykinney's *DR - 4c4e Theory*. The count is exact for every case and proved in Lean.

**What it's worth.** Each row is a value of the count.

{{ t_count() }}

That's a clean scale. 0 to 2 holds every case of 4 or less and {= pc(1 - TB['le2']['miss_d5']) =} of the 5-movers, at {= pc(TB['le2']['precision']) =} sub-7. As a switch rule on this page's yardstick, one row per policy:

| Policy (4c4e) | Switched | Missed: 4 or less | Missed: 5-movers | Missed: 6-movers | Cost per case |
|---|---|---|---|---|---|
| 2+ pairs | {= pc(B('4c4e','pairs')['switch']) =} | {= pc(B('4c4e','pairs')['miss_le4']) =} | {= pc(B('4c4e','pairs')['miss_d5']) =} | {= pc(B('4c4e','pairs')['miss_d6']) =} | {= f3(B('4c4e','pairs')['loss']) =} |
| pairs + ARM (Fanti) | {= pc(B('4c4e','pairs+arm')['switch']) =} | {= pc(B('4c4e','pairs+arm')['miss_le4']) =} | {= pc(B('4c4e','pairs+arm')['miss_d5']) =} | {= pc(B('4c4e','pairs+arm')['miss_d6']) =} | {= f3(B('4c4e','pairs+arm')['loss']) =} |
| 2 half turns or fewer | {= pc(TB['le2']['switch']) =} | {= pc(TB['le2']['miss_le4']) =} | {= pc(TB['le2']['miss_d5']) =} | {= pc(TB['le2']['miss_d6']) =} | {= f3(TB['le2']['loss']) =} |
| 3 half turns or fewer | {= pc(TB['le3']['switch']) =} | {= pc(TB['le3']['miss_le4']) =} | {= pc(TB['le3']['miss_d5']) =} | {= pc(TB['le3']['miss_d6']) =} | {= f3(TB['le3']['loss']) =} |
| the card | {= pc(X44['card']['switch']) =} | {= pc(X44['card']['miss_le4']) =} | {= pc(X44['card']['miss_d5']) =} | {= pc(X44['card']['miss_d6']) =} | {= f3(X44['card']['loss']) =} |
| the card, or 2 half turns or fewer | {= pc(TB['card_or_le2']['switch']) =} | {= pc(TB['card_or_le2']['miss_le4']) =} | {= pc(TB['card_or_le2']['miss_d5']) =} | {= pc(TB['card_or_le2']['miss_d6']) =} | {= f3(TB['card_or_le2']['loss']) =} |

So the count cut at 2 beats every list on the server on cost, with far fewer switches. It finds a lot of what pairs miss: of the cases with 0 or 1 pair, {= n(TB['low_pair_le2']['n']) =} are at 2 or fewer ({= pc(TB['low_pair_le2']['share']) =} of 4c4e) and {= pc(TB['low_pair_le2']['rate']) =} of them are sub-7. That's all {= n(TB['pairs_missed_le2']['le4'][0]) =} of the 4-or-less that 2+ pairs misses, {= frac(TB['pairs_missed_le2']['d5']) =} 5-movers and {= frac(TB['pairs_missed_le2']['d6']) =} 6-movers. It also holds {= frac(TB['card_missed_le2']['d5']) =} 5-movers the card misses, which is why the last row is the best of the table.

Where it's weak is the 6-movers: more than half of them are at 3, and a 3 is {= pc(TB['by_count'][3]['rate']) =} sub-7 on average. The count has nothing more to say about which 3s are the good ones. Cut at 3 it misses almost nothing and switches two thirds of 4c4e.

```
{= W['count3_5mover']['setup'] =}   // setup: 4c4e, 1 pair, 3 half turns to two bars
{= W['count3_5mover']['dr'] =}   // DR in 5, with two quarter turns of L and no stop at two bars
```

```
{= W['count2_7mover']['setup'] =}   // setup: 4c4e, 2 pairs, 2 half turns to two bars
{= W['count2_7mover']['dr'] =}   // DR in 7: the two half turns need four U/D turns around them
```

**Where the count sits against pairs.** Each row is a pair count:

{{ t_count_pairs() }}

**What it takes to read.** This is the problem.

- *It needs places, not colours.* The count is made from where the four bad corners, the two bad edges and the two holes sit on the inverse, layer by layer, and which way each corner points. That's the full NISS trace of all eight pieces. The card's reads are colour matches on the same pieces.
- *Then it needs a search.* With 3 or 4 pairs there's a formula. With 2 pairs you have to try one half turn ahead, in your head, on a cube you can't see. With 0 or 1 pair there's no hand rule that tells a 2 from a 3, and those {= n(TB['low_pair_le2']['n']) =} cases are where the count would pay most.
- *What people have said about tracing 4c4e in full.* Zagros thinks it's the right idea: "I dont do this but ngl I am super convinced that more niss tracing is clearly optimal, I think the optimal system is 100% niss tracing 4c4e, and I think if someone were to commit to doing this, they would probably get good at it pretty fast" ([[D15171]]). Then tried it: "btw i talked here earlier about niss tracing 4c4e rzp cases and I did it for like four solves and gave up. i still have hope in the concept, but I quickly found that I'm just not good enough at rzp->dr to be able to do it effectively. I niss trace and then I just don't know if it has a 6 move DR or not. I need to actually do a few moves to check" ([[D16255]]), and "Still believe it is optimal, especially for stuff like 21 1 pair that is borderline on if I want to switch, but it is no help if I can't actually tell how many moves to DR after niss tracing half the time" ([[D16256]]). So the trace was doable and the judging wasn't. A count is a way of judging, so this cuts both ways: it's the thing Zagros was missing, and it's four solves by one person.
- *And time.* caycala: "I just timed me switching an rzp and going back to solved cube, and it took ~20 seconds including some time to look specifically at the rzp. So you would have to be able to niss trace in that time (definitely doable for 4c4e and less, but also consider extra time for E slice) and also be able to determine if the case is good." ([[D12774]]), and the conclusion: "tldr i dont think it’s worth it + it is much more mistake prone" ([[D12776]]).

So: on what it catches, the count deserves a place on top of the card. On what it takes, nobody has shown a full trace plus the count done in a few seconds, and the two people who wrote about full tracing of 4c4e either stopped or advised against it. I can't make the case that it's fast enough, so it's not on the card. If you can do it, the rule is simple: *2 or fewer, switch*, whatever the card says.

**On a cube you can see** the count costs nothing. After the switch, or for an RZP on the side you're on, the bars and the holes are in front of you. Then the first table is the read: 2 or fewer is {= pc(TB['le2']['precision']) =}, 4 or 5 is {= pc(TB['by_count'][4]['rate']) =} and under.

**How the count splits the card** (**computer only**). Each row is a group of the card:

{{ t_count_groups() }}

Two things in there. A bar is at 2 or fewer in {= pc(TB['bar']['on']['le2_share']) =} of its cases wherever the holes are, so the holes are not the count in disguise: at the same count, a bar with the holes on one R/L face is {= pc(TB['bar']['on']['le2']['rate']) =} and one without is {= pc(TB['bar']['off']['le2']['rate']) =}. And 1 pair + ARM 21 with 4b corners is always a 3, good or bad, so there the side pairs see something the count doesn't.

---

## 8. What didn't help

Briefly, on 4c4e unless said otherwise. *Cost per case* of the best rule that uses the pair count and the read. Pairs alone is {= f3(R['tried44_pairs']['loss']) =}, the card {= f3(X44['card']['loss']) =}. Each row is a read:

{{ t_tried() }}

*Side turns* in that table are the turns of R, L, F and B in the DR with the fewest of them, U and D turns free. Like the half-turn count they need the whole trace. *AR bars* are rodneykinney's: an edge with the two corners next to it each in AR or paired with it ([[T8595]]). *Moves to AR* is the fewest moves to a JZP state.

- **The bar and the holes, one at a time.** Knowing only that 2 pairs sit on one edge changes nothing: a bar is {= bar_rate() =} sub-7 overall, still a switch. Knowing only where the holes are changes nothing either. It's the two together that split 2 pairs.
- **A new kind of pair.** I took every way two bad pieces can sit relative to each other (corner and edge, corner and hole, corner and corner, edge and edge, edge and hole, hole and hole: {= EX['rel_classes'] =} classes up to the symmetries that keep the EO and DR axes; top pairs, fake pairs and side pairs are three of them) and asked which one, counted next to pairs, helps most. The best is a corner-corner relation that just restates the corner case ({= f3(EX['rel_best']) =}), then side pairs ({= f3(EX['rel_second']) =}). There's no fourth pair hiding.
- **Points systems.** rodneykinney's old estimate 12 − 2 × top pairs − 2 × side pairs ([*Domino Setup Theory*](https://docs.google.com/document/d/1Z3O8BY1LbAMF6m55ufXtSdtBVwSJpMArtRrDT-p_CwM)), which switches at 3 pairs of any kind: {= f3(EX['any3']['loss']) =}. A top pair as 2 points and a side pair as 1, switch at 4: {= f3(EX['pts_2p_s_ge4']['loss']) =}. The best weighted sum of pairs, side pairs, fake pairs, ARM, corner case, holes and layers ({= EX['lin_big']['terms'] =} terms, fitted to these prices): {= f3(EX['lin_big']['loss']) =}. A sum can't do it because the reads don't add up: one side pair is worse than none for 4b corners.
- **Corner-only counts.** The moves to orient the corners alone, and that number plus the missing pairs (the bones of the lower bound in *DR - 4c4e Theory*, used as a switch rule at 6): {= f3(EX['lb6']['loss']) =}. It's a bound for finding the DR, not a predictor.
- **Corners not in a pair** (Zagros's question, [[T11345]]): the same thing as pairs once you know the DRM.
- **Fake pairs, on 4c4e with 1 pair or with 2 pairs on two edges**, and **AR bars**: nothing. Fake pairs matter with 0 pairs and on a bar (the card), for 3c2e (wen's rule), and in 3c6e and 6c6e.
- **The bad edges' layers.** Both bad edges in one layer splits 1 pair + ARM 21 with 4a corners into {= pc(EX['4a_layer']['same']['rate']) =} and {= pc(EX['4a_layer']['diff']['rate']) =}. Evan's stacked corners do it better ({= pc(AF['stacked']['21']['rate']) =} and {= pc(AF['stacked']['not_stacked_21']['rate']) =}), so that's what the card uses.
- **wen's "one U/D turn away from 4d"**, as a read next to pairs: a little, less than ARM does for the same effort. It does hold every 5-mover with 1 pair and 4a corners, and those are inside the card's stacked 4a row (section 5.1).
- **ARM on the bar, instead of the edges out of the slice.** Edge ARM 1 is the good one ({= pc(AF['bar_earm']['1']['rate']) =} against {= pc(AF['bar_earm']['0']['rate']) =} and {= pc(AF['bar_earm']['2']['rate']) =} for edge ARM 0 and 2), but the holes split a bar better: {= pc(AF['bar_on']['rate']) =} against {= pc(AF['bar_off']['rate']) =}. The best short ARM version of the row is in section 6.
- **ARM for 0 pairs.** 0 pairs with ARM 00 or 42 is {= n(AF['zero_arm']['n']) =} cases at {= pc(AF['zero_arm']['rate']) =}, but it has only {= n(AF['zero_arm']['le4']) =} of the {= n(EX['zero_pairs']['le4']) =} zero-pair cases of 4 or less. The others are ARM 21, so you'd still need the card's row there.
- **Leading with something other than pairs.** A tree that's free to split on any quick read first still splits on pairs first (2 or more against fewer), then ARM 21. With 8 leaves it costs {= f3(EX['trees_free']['8']['loss']) =}, with 16 {= f3(EX['trees_free']['16']['loss']) =}.
- **Bigger lists.** 40 leaves: {= f3(EX['trees_free']['40']['loss']) =}. The card is where the curve flattens.

---

## 9. How far a rule can go

**Computer only.** For a set of reads, the best possible rule switches exactly the cells (combinations of values) that are worth it at the prices of section 3. No rule on those reads can cost less. These are lookups in hundreds or thousands of cells, so they're ceilings to measure a card against, not cards.

{{ t_ceil('4c4e') }}

Three things in there.

- *Pairs + ARM at its best is Fanti's list.* Same cells, same numbers.
- *The card beats every two-read ceiling and the four-read one* (pairs, ARM, corner case and side pairs: {= f3(X44['ceil']['pairs+arm+case+side']['loss']) =} with {= n(X44['ceil']['pairs+arm+case+side']['cells']) =} cells, the card {= f3(X44['card']['loss']) =} with {= len(X44['groups']) =} groups). It can, because it also reads where the pairs sit, the columns and the edges out of the slice.
- *The quick reads together know almost everything about the short cases.* All of them at once miss no 5-mover and {= pc(X44['ceil']['quick']['miss_d6']) =} of the 6-movers at {= pc(X44['ceil']['quick']['switch']) =} switched. That's a table of {= n(X44['ceil']['quick']['cells']) =} cells. The gap between it and the card is what a much better memory, or a trainer, could still get.

**Where the slower reads pay.** Say the pair trace (pairs, where they sit, fake pairs) and ARM are read on every case, and the slower reads only on the groups where they help most per case. The best possible cost on 4c4e, by how many cases get the slower reads. Each row is a budget:

{{ t_budget() }}

The card asks for a slower read on {= pc(EX['reads44']['one_pair_arm2x'] + EX['reads44']['bar_lt2fake'] + EX['reads44']['zero_nofake']) =} of cases and costs {= f3(X44['card']['loss']) =}. The numbers in the table are lookups again ({= n(AF['budget_cc_side']['all_cells']) =} cells for the middle column, {= n(AF['budget_all']['all_cells']) =} for the last), so they say what a perfect memory would get on the same budget, not what a card can. With the corner case and the side pairs alone there's little beyond the card even then: {= f3(AF['budget_cc_side']['everywhere']) =} if you read them on every case. And the first place the slower reads pay is the one everybody found: 1 pair with ARM 21. After the card, the best single row a search can still add (one pair count, up to two conditions on the pair trace and ARM, up to two on the slower reads) is worth {= f3(NX['rows'][0]['gain']) =} a case, against {= f3(B('4c4e', 'pairs')['loss'] - X44['card']['loss']) =} for the whole card over the pairs rule. The rows left are small and take four or five conditions each.

**Which second read helps most**, per DRM. Cost per case of the best rule on pairs and one more read, the best one in bold:

{{ t_second() }}

ARM for 4c4e, 7c8e and 8c8e, side pairs for 4c2e and 2c2e. That's where the server ended up too.

The same ceilings for 4c2e and 7c8e:

{{ t_ceil('4c2e') }}

{{ t_ceil('7c8e') }}

---

## 10. Other RZP lengths, real attempts, other weights

**After a 4-move or a 6-move RZP.** The target moves: a DR in 7 is enough after 4, and you need 5 after 6. The same groups, with the share that makes the target and the verdict at the same prices (a just-good-enough DR at 3, one move shorter at 9, shorter still at 27):

{{ t_k('4c4e') }}

- *4-move RZP*: every row is a switch at these prices, even 0 pairs ({= pc(grp('4c4e', '0 pairs, anything else')['K7']['rate']) =} of the leftovers have a DR in 7 or less). That's "It seems like you should pretty much always switch a 4 move DR-4c4e." (Zagros, [[D18940]]) and "yeah 4 is almost always a switch on normal scramble" (tseitsei89, [[T9330]]). If you want to trim, trim from the bottom: Daichi's 4-move list ([[D18953]]) drops a few 0-pair and 1-pair ARMs.
- *6-move RZP*: 3 or 4 pairs, and 1 pair with ARM 21 and 4d corners. 2 pairs on two edges is down to {= pc(grp('4c4e', '2 pairs on two edges')['K5']['rate']) =}.

The other DRMs are in appendix A.

**On real attempts.** The card's numbers on the {= n(R['real_attempts']['5']) =} real 5-move attempts, next to the exact ones. It's a sample of {= n(R['real_scrambles']) =} scrambles. Even if every attempt of a scramble counted as one, a standard error on a share would be about 0.6 points.

{{ t_real() }}

Same thing. For the four DRMs together the cards switch {= pc(M4R['card']['switch']) =} of the real attempts and miss {= pc(M4R['card']['miss_le4']) =}, {= pc(M4R['card']['miss_d5']) =} and {= pc(M4R['card']['miss_d6']) =}; the pairs policy switches {= pc(M4R['pairs']['switch']) =} and misses {= pc(M4R['pairs']['miss_le4']) =}, {= pc(M4R['pairs']['miss_d5']) =} and {= pc(M4R['pairs']['miss_d6']) =}.

**Other prices.** Cost per case on 4c4e when a declined 6-mover costs 2, 3 or 5 wasted switches and each move shorter counts 2, 3 or 4.5 times as much. The page uses 3 and 3.

{{ t_sens() }}

The card is the cheapest in every row but the last three, where a 6-mover at 5 wasted switches makes switching more the right call and the wider card takes over. Only one verdict on the card flips anywhere in that grid: with a 6-mover at 2 and a factor of 2, the 0-pair group drops to *if you have time*.

---

## 11. The claims, checked

Things people said about these rules, with the exact numbers. The one that doesn't hold is on the [errata](errata.html) page.

| Who and what | Exact |
|---|---|
| tseitsei89, [[T9321]]: "4c4e: >1 pairs = switch (43%), 1 pair and d corners = switch (44%)" | 2+ pairs is {= pc(B('4c4e','pairs')['precision']) =} sub-7 (the 43% is rodneykinney's findable sub-7). 1 pair with 4d corners is {= pc(EX['p1_4d']['rate']) =}. |
| Evan, [[D14342]]: "4d+1 is extremely good for AR-21 (~90% sub-7) but 0% for other AR" | {= grate('4c4e', '1 pair, ARM 21, 4d corners') =} with ARM 21, 0% with ARM 20 or 22. |
| Evan, [[D14402]], on 1 pair + ARM 21: "b corners - 29%", "d corners - 89%", "a corners - ~34% if corners are stacked, < 5% otherwise" | All three right: 4b {= pc(EX['p1_arm21_by_cc']['b']['rate']) =}, 4d {= pc(EX['p1_arm21_by_cc']['d']['rate']) =}, 4a in two columns {= pc(AF['stacked']['21']['rate']) =} and {= pc(AF['stacked']['not_stacked_21']['rate']) =} otherwise. The stacked ones split again on side pairs: {= pc(AF['stacked']['21_side']['rate']) =} with one or more, {= pc(AF['stacked']['21_noside']['rate']) =} with none. |
| Evan, [[D14348]]: "interestingly 4a corners are basically the same for all ar-2X" | With 1 pair: in two columns {= pc(AF['stacked']['21']['rate']) =} for ARM 21 and {= pc(AF['stacked']['2022']['rate']) =} for ARM 20 and 22, not in two columns {= pc(AF['stacked']['not_stacked_21']['rate']) =} and {= pc(AF['stacked']['not_stacked_2022']['rate']) =}. Close enough that the card's stacked 4a row takes all three ARMs. |
| wen, [[D14328]]: "1 pair then I check if it's 4d or one U/D turn away from 4d" | 1 pair with 4a corners one U/D turn from 4d is {= n(AF['one_from_4d']['yes']['n']) =} cases at {= pc(AF['one_from_4d']['yes']['rate']) =}, with all {= n(AF['one_from_4d']['yes']['d5']) =} 5-movers that 1 pair and 4a corners have. The other 4a corners are {= pc(AF['one_from_4d']['no']['rate']) =}. |
| rodneykinney, [[T8123]], for 0 pairs: "To catch this case, you can switch 4a-0 and 4d-2, but only if there also are no fake pairs" | Those are {= n(EX['rk_0p']['n']) =} cases at {= pc(EX['rk_0p']['rate']) =}, with {= n(EX['rk_0p']['le4']) =} of the {= n(EX['zero_pairs']['le4']) =} zero-pair cases of 4 or less. No fake pairs with the corners 2 and 2, any corner case, is {= n(grp('4c4e', '0 pairs, no fake pairs, corners 2 and 2 in the layers')['n']) =} cases at {= grate('4c4e', '0 pairs, no fake pairs, corners 2 and 2 in the layers') =} with all {= n(EX['zero_pairs']['le4']) =}. |
| rodneykinney, [[D12098]]: "Zero pairs + zero pseudo-pairs would be a likely setup to F2 B2 R. But I don't have stats that include the pseudo-pair count." | The stats: 0 pairs and 0 fake pairs is {= n(EX['nofake0']['n']) =} cases at {= pc(EX['nofake0']['rate']) =}, against {= pc(EX['zero_pairs']['rate']) =} for 0 pairs overall. |
| rodneykinney, [[T8108]]: "2 pairs: Switch unless 4b-0" | 2 pairs with 4b-0 corners is {= pc(EX['p2_4b0']['rate']) =} sub-7, a skip at these prices too. {= n(EX['p2_4b0_in_bar_off']) =} of its {= n(EX['p2_4b0']['n']) =} cases are in the card's *if you have time* row (a bar with the holes off the R/L faces and fewer than 2 fake pairs). |
| compLex, [[D13425]]: "you only need to actually learn to spot 4d (the only case worth switching 1 pair) and 4b (the only case not worth switching 2 pairs)" | By pairs and corner case alone the 4d half holds: 1 pair is {= pc(EX['p1_4d']['rate']) =} with 4d and {= pc(EX['p1_other_max']) =} or less otherwise. The 4b half holds for 4b-0 ({= pc(EX['p2_4b0']['rate']) =} with 2 pairs), not for 4b-2 ({= pc(EX['p2_4b2']['rate']) =}). |
| Fanti, *armpairs_1.txt* ([[D15160]]): "35.2% switches", "42.6% sub-7 switch success (15.0% total)", "4.3% of cases will be discarded with sub-7" | {= pc(B('4c4e', 'pairs+arm')['switch']) =}, {= pc(B('4c4e', 'pairs+arm')['precision']) =}, {= pc(B('4c4e','pairs+arm')['miss_good'] * X44['sub7']) =} with the EO kept. |
| Yura Riabov, [[D12993]]: "From my experience with pairs 1 bar is worse than 2 pairs for most arms" | True in {= EX['bar_arms'][0] =} of the {= EX['bar_arms'][1] =} ARMs that have both. Overall a bar is {= bar_rate() =}, two edges {= grate('4c4e', '2 pairs on two edges') =}. |
| wen, [[D16512]], on the 3c2e rule: "At the very least you will never miss a 5 mover by doing this" | True. The skipped group has {= n(grp('3c2e', '0 pairs, no fake pair, no split pair')['d6']) =} 6-movers, no 5-mover, no 4-mover. |
| Daichi, [[D15161]]: "for 7c8e with 5p, 20/54 has a 0% chance of sub7" | True, 48 cases each, none under 7. |
| Daichi, same message: "JZP with b corners is way better than a corners" (4c2e, 0 pairs) | {= pc(EX['42_jzp_4b']['rate']) =} against {= pc(EX['42_jzp_4a']['rate']) =}. |
| Daichi, [[T11352]]: "8c8e 2 pair 42a is a good switch" | 2 pairs with ARM 42 is {= grate('8c8e', '2 pairs, ARM 42') =} sub-7, on the card. |
| Jay, [[D12983]]: "iirc, need 2 pairs + ar21 for 5c4e to be good (3 pairs if it's another arm), same for 5c6e but need one extra pair" | As a rule it switches {= pc(B('5c4e', 'jay')['switch']) =} of 5c4e at {= pc(B('5c4e', 'jay')['precision']) =} and {= pc(B('5c6e', 'jay')['switch']) =} of 5c6e at {= pc(B('5c6e', 'jay')['precision']) =}. With 2 or more side pairs on top the 5c4e groups are {= grate('5c4e', '3 pairs, 2+ side pairs') =} and {= grate('5c4e', '2 pairs, ARM 21, 2+ side pairs') =}. |
| Zagros, [[D18940]]: "It seems like you should pretty much always switch a 4 move DR-4c4e." | {= pc(X44['K7']['always']['precision']) =} of 4c4e is 7 or less, and every group of the card is a switch at 4. |

---

## 12. What this does not cover

- **Whether you find the DR.** A case counts as good if a DR in 6 exists. A 6-mover through three half turns is harder to see than `U' R` with setup, and I haven't weighed that in. rodneykinney's *findable* is the server's attempt at it.
- **What the DR is worth after.** A short DR into a bad DR case isn't worth what its length says. That's [*Judging a DR by hand*](../judging-a-dr/).
- **The other DR axis and the EO's last move.** One EO axis, one DR axis, linear. Both options help a little after a switch (the EO's last move either way: about 2 points of sub-7 on 4c4e; the other DR axis: about 6), and neither changes which groups are better.
- **Human timing and misreads.** Section 6 is an argument from what the reads are and what people have said they take. Nobody has timed this card or counted how often a read goes wrong. If you do, tell me.
- **The twist split.** How many corners are twisted clockwise and how many counter-clockwise isn't a read on the cards. It matters for 8c8e: with 4 and 4 it's {= pc(EX['88_twist']['44']['rate']) =} sub-7, with 7 and 1 it's {= pc(EX['88_twist']['71']['rate']) =} and nothing under 6 moves.
- **DRMs outside the 12.** 6c4e, 7c6e and the rest are not carded.

---

## Appendix A: full tables

**Every current policy, per DRM.** One row per DRM: the pairs policy, the best list I found on the server, and the card, each with its *cost per case* at the prices of section 3.

{{ t_all_cost() }}

**The cards after a 4-move and a 6-move RZP.** One table per DRM. Each row is a group of the card, with the share that makes the target at each RZP length and the verdict at the same prices.

{{ t_k('4c2e') }}

{{ t_k('3c2e') }}

{{ t_k('7c8e') }}

{{ t_k('8c8e') }}

{{ t_k('2c2e') }}

**The low DRMs in full.** The card of each low DRM with all its groups, followed by the current policies where there are any. Radek B's 4c6e rule came with a hedge ("If the numbers are correct, then it seems to me like tracing pairs is a really good way of deciding whether to switch for 4c6e. Like only if there are 4 pairs (or if it's jzp)", [[D7471]]), and Fanti's 3c4e list is "my rough sketch of 34 (maybe not final)" ([[D15179]]).

{{ t_card('4c6e') }}

{{ t_cmp('4c6e') }}

{{ t_card('3c4e') }}

{{ t_cmp('3c4e') }}

{{ t_card('3c6e') }}

{{ t_cmp('3c6e') }}

{{ t_card('5c4e') }}

{{ t_cmp('5c4e') }}

{{ t_card('5c6e') }}

{{ t_cmp('5c6e') }}

{{ t_card('6c6e') }}

More pockets, one example each:

{{ wit('46_pocket_4mover', '4c6e, 4 pairs on three edges', 'DR in 4') }}

{{ wit('66_pocket_4mover', '6c6e, 3 pairs, 3 fake pairs, corners 3 and 3', 'DR in 4') }}

{{ wit('22_0p_side_6mover', '2c2e, 0 pairs, 1 side pair, ARM 00', 'DR in 6') }}

---

## Appendix B: how it was computed, and what checks it

**The table.** The DR length of every case comes from a breadth-first search over the {= n(R['N0']) =} cases with the 14 turns that keep an F/B EO. It's the table of my EO-to-DR study, it agrees with Cale's sheet, and its histogram is proved in Lean.

**The reads.** Defined from stickers, on the switched case. Pairs, fake pairs, side pairs and ARM agree with rodneykinney's own code on every case. The normal-side versions are the ones of section 6, checked there.

**The search for the cards.** Per DRM, over the quick reads (ARM, corner case, side pairs, fake pairs, edges with a pair, holes, layers, columns): a greedy list of rules of up to two conditions inside a pair count, and a small tree grown to rank well at three prices of a wasted switch. Both score with the prices of section 3. I then wrote each card by hand from what they agreed on, in as few groups as kept the cost, took the server's rule wherever it did as well or better (wen's for 3c2e, caycala's chart for 7c8e, Evan's stacked corners for 4a), and graded the written card from scratch. A second search starts from the written 4c4e card, with the pair trace and ARM free on every case and the slower reads priced by how many cases need them, and lists the single rows still worth adding. The bar with 2 fake pairs and the stacked 4a row at ARM 20 and 22 come from that pass, and it's where the *0.005 a case* of section 9 comes from. The ceilings of section 9 come from the same code with every combination of values as its own group.

**What *the best list on the server* is.** For each DRM, the rule with the lowest cost per case among the ones I found stated: the *DRM Subsets Meta* row, Fanti's lists, caycala's chart, tseitsei89's, rodneykinney's, wen's, Jay's and Radek B's. Appendix A names it per DRM.

**Real attempts.** The scrambles are uniformly random states, not nissy's scrambler. For each one, on both sides and all three EO axes: every EO of at most 5 moves, every RZP after it, kept when it first reaches its DRM at a total of 5.

**Examples.** Every setup and DR printed on this page was replayed on a sticker-level cube, and the DR lengths are the table's.

**Lean.** The Lean 4 project that goes with this study (no Mathlib) recounts the tables on its own model of the cube: its own breadth-first search for the DR lengths, the reads defined from stickers, and then, for each of the 12 DRMs, every group of the card with its cases by DR length, and every policy with what it switches and what it misses at each length. Every theorem is checked by compiled evaluation (`native_decide`), and every one equals the number printed here. Three of them spelled out:

| Policy (4c4e) | Cases switched | Missed: 4 or less | Missed: 5-movers | Missed: 6-movers | Switched with a DR of 7 or more |
|---|---|---|---|---|---|
| the card | {= n(round(X44['card']['switch'] * X44['n'])) =} | {= n(X44['card']['missn_le4']) =} | {= n(X44['card']['missn_d5']) =} | {= n(X44['card']['missn_d6']) =} | {= n(round(X44['card']['wasted'] * X44['n'])) =} |
| 2+ pairs | {= n(round(B('4c4e','pairs')['switch'] * X44['n'])) =} | {= n(B('4c4e','pairs')['missn_le4']) =} | {= n(B('4c4e','pairs')['missn_d5']) =} | {= n(B('4c4e','pairs')['missn_d6']) =} | {= n(round(B('4c4e','pairs')['wasted'] * X44['n'])) =} |
| pairs + ARM (Fanti) | {= n(round(B('4c4e','pairs+arm')['switch'] * X44['n'])) =} | {= n(B('4c4e','pairs+arm')['missn_le4']) =} | {= n(B('4c4e','pairs+arm')['missn_d5']) =} | {= n(B('4c4e','pairs+arm')['missn_d6']) =} | {= n(round(B('4c4e','pairs+arm')['wasted'] * X44['n'])) =} |

Computed but not proved: the prices and the cost per case, the gradings after a 4-move and a 6-move RZP, the ceilings and the search, the real attempts, and the colour reads on normal (those are checked on a sample, section 6). The half-turn count of section 7 was proved in the same project earlier.

---

## Docs referred to

- rodneykinney, [*DRM Subsets Meta*](https://docs.google.com/document/d/1Jnd1Qy_6b1W5dR5fZQScloMoMPR2LCAF7VPrgeTaRgg), [*DRM Subsets*](https://docs.google.com/document/d/1AUQVrecEFZyR6okXAyJgtQZA-A0AJmAUevhJZlQMjAs), [*DR - 4c4e Theory*](https://docs.google.com/document/d/1DsxAAB2WRfpgDR-VWZZrXq2W4y_YMXBufRRYNLAGGoU), [*Domino Setup Theory*](https://docs.google.com/document/d/1Z3O8BY1LbAMF6m55ufXtSdtBVwSJpMArtRrDT-p_CwM), [*DRM corner variant+pair stats*](https://docs.google.com/spreadsheets/d/174ClwBFl-T2zJAq8MVyK1bKsIIuzxQU0_XmQGv82LPQ).
- Louis, [*DRM/ARM average optimals*](https://docs.google.com/spreadsheets/d/13fSwUROzP0hZQV1Cn96GndWbPy4UrsHiYTaWFSeWtJs). Cale, [*DR setup stats*](https://docs.google.com/spreadsheets/d/11bTZ4Y7_6qKlIWo4a4TLW45M2ZkctQZAVxgQqEtlUs0). Evan, [*arm/pairs*](https://docs.google.com/spreadsheets/d/1YZYyokxYXwDdBTgN7ojpPAFHKKz48hCyNO2l6-iwmVk).
- caycala's chart, attached to the message of [[D11016]]. Fanti, *armpairs_1.txt*, attached to the message of [[D15160]].
- wen and others, [*Hitchhiker's Guide to DR*](https://docs.google.com/document/d/1E_5wSKvQFXXZY4f3xLM76qMUrVGp9Pe7vgotS0X-T4U).
- Andrew, [*How to do Domino Reductions: The Secret They Don't Want You To Know*](https://www.youtube.com/watch?v=oAbPQOfui2U) (FewestMoves channel, 6 Feb 2019).
- On this site: [*EO to DR, and scramble to DR*](../eo-to-dr/), [*Judging a DR by hand*](../judging-a-dr/).
