## Appendix A: full tables

**Every 4c4e ring picture with 2 row swaps or fewer** (section 4.4), up to exchanging the layers and mirror image. One row per picture, in the ring notation of section 4.1 (`>` and `<` bad corners pointing clockwise and counter-clockwise, `o` a good corner, `E` a bad edge place, `-` a good one). *States* counts all 4c4e cases with that picture, whatever the holes:

{{ring_patterns}}

**4c4e: U/D turns by half-turn count** (section 4.5). Each row is a half-turn count with the number of U/D turns its shortest one-quarter-turn setup needs, **computer only** as a table:

{{ring44_align}}

**4c4e by ARM inside 2 and 3 half turns** (section 4.5), one row per ARM:

{{ring44_arm}}

**The side-turn setups on the real attempts and for the other RZP lengths** (section 5.2), the rows of that section's table:

{{ring_profiles_rzp}}

**4c4e by ARM and paired edges.** One row per ARM; each cell is the sub-7 rate of the ARM's cases with that many bad edges paired:

{{c44_arm_paired}}

The number of states behind each cell of that table:

{{c44_arm_paired_n}}

**4c4e by pairs and paired edges** (bars against separate pairs). One row per count of pairs and of the edges they sit on:

{{c44_bars}}

**4c2e, inside *pairs + side pairs/2 is exactly 1*.** Each row splits that group by one feature value:

{{c42_check}}

**8c8e by pairs**, one row per pair count:

{{c88_pairs}}

**EO to DR by DRM, with the free options** (every case once; from my EO-to-DR study's definitions, recomputed here). One row per DRM: the mean distance to DR and the share of cases with a DR in at most 5, 6 and 7:

{{variants}}

The share with a DR in at most 6 when one free option is allowed, one row per DRM:

{{variants_options}}

## Appendix B: how it was computed, and what checks it

**The model.** A case is the twists of the 8 corners and the set of places holding the 4 E-slice edges, for an F/B EO and a U/D DR ({= n(1082565) =} cases). A breadth-first search with the 14 turns that keep the EO (U, D, R, L, F2, B2, each way) gives the exact distance to DR of every case: {= ', '.join(f'{a}: {n(b)}' for a, b in E['dist']) =}, mean {= E['dist_mean'][:6] =}. Features are defined from the faces the stickers are on (a sticker model of the cube), not from index strings. The side turns of a case come from the same turn tables with the U and D turns free: the cases a solution with q quarter turns and h half turns of the side faces reaches are built up one side turn at a time, each step closed under U and D turns. The row swaps of 4c4e are a second, separate search on the {= n(sum(RJ['classes'].values())) =} ring pairs alone. The RZP weights count every sequence of EO-keeping turns that first reaches its DRM, exactly. The real attempts use {= n(6000) =} uniformly random scrambles (random state, not nissy's scrambler, which has a bias). The whole thing runs in about six minutes on four cores, each job capped at 4 GB.

**What checks it.**

- **The distances** equal my EO-to-DR study's table on all {= n(1082565) =} cases, and nissy 2.0.8 (`solve drud-eofb`) agrees on {= n(E['nissy']['agree']) =} of {= n(E['nissy']['positions']) =} random cases, with every nissy solution replayed to DR on the sticker model.
- **The options** (EO's last turn, the second axis, normal or inverse) equal the EO-to-DR study's per-case tables in all {= E['checks_variants']['plain']['compared'].split()[0] =} cells, to their printed rounding.
- **The features** pass {= E['features_tests'] =} unit tests on hand-made cases from the server's examples, for instance:

  ```
  R                 // 4c4e JZP with 4 pairs
  R U               // 4c4e ARM 21
  U' F2 B2 R2 U2 R  // ARM 02 with no pairs and 6 moves
  ```

  They also agree with rodneykinney's own string code (DRM, ARM, pairs, fake pairs, side pairs, AR pairs) on all {= n(1082565) =} cases, once the corner order is read the way both Louis's and rodneykinney's comments mean it.
- **The ring picture** is checked against the turn tables on every twist state and every edge set: U and D turns rotate one ring and nothing else ({= n(int(RJ['checks'][0][0])) =} of {= n(int(RJ['checks'][0][1])) =} checks), half turns swap the face's two rows and its two E-slice places ({= n(int(RJ['checks'][2][0])) =} of {= n(int(RJ['checks'][2][1])) =}), quarter turns follow the rule of section 4.1 ({= n(int(RJ['checks'][3][0])) =} of {= n(int(RJ['checks'][3][1])) =}). Half turns to two bars equals the larger of row swaps and hole number on {= n(int(RJ['checks'][9][0])) =} of {= n(int(RJ['checks'][9][1])) =} 4c4e cases, with the two sides computed separately (on the cases, and on the rings).
- **The NISS readings** of section 7 hold on every sampled cube ({= n(NISS('ARM axis swap: ARM for U/D DR on normal = ARM for R/L DR on inverse (uniform)')[0]) =} uniform and {= n(NISS('ARM axis swap: ARM for U/D DR on normal = ARM for R/L DR on inverse (4c4e)')[0]) =} 4c4e cubes per reading; {= n(TRACE('side pairs', '4c2e')[0]) =} more from 4c2e for the new ones).
- **Switched cases are uniform** within their class: the real attempts' rate against the uniform rate of their own class mix in {= n(E['uniform_cells']) =} DRM × length cells, worst {= f2(E['uniform_worst_z']) =} standard errors (20 batches of 300 scrambles).
- **Every example** in this write-up, the errata and the worked examples is replayed on the sticker model of my DR-xs study (`cube.py`): the scramble and EO + RZP give the stated DRM, the switched case has the stated features, and the DR written out reaches DR with the EO kept, in the stated number of moves.
- **Lean.** A Lean 4 certificate in the study's folder (`lean/EOSwitch`, no Mathlib, no `sorry`) builds its own cube from stickers and runs its own BFS over all {= n(1082565) =} cases with the 14 EO-keeping turns. An independent checker confirms each entry: 0 exactly at DR, never more than one above a neighbour, and one below some neighbour. It defines the features from stickers (pairs, fake pairs, paired edges, bars, side pairs, same slice, the ARM counts, JZP) and redoes 27 of the feature unit tests. It proves the distance histogram (mean {= E['dist_mean'][:6] =}), the per-DRM counts for 4c4e, 4c2e, 3c2e, 7c8e, 8c8e and 2c2e, and every cell of the card tables: 4c4e by paired edges and by paired edges × same slice, pairs × paired edges, 4c2e by pairs + side pairs/2, 7c8e by pairs, 2c2e by paired edge × JZP, and 3c2e. It also proves that the study's printed tables match those cells. A second part recounts, from the same BFS, the corner case (4a to 4d, suffix, stacked) and the other features the rules use, and proves the counts behind section 1, the switch cards and the errata (listed under *Formally verified* below). Build: `lake build`, about four minutes from clean on two cores, under 1 GB.

  A third part (`Rings.lean`, `RingsThm.lean`) defines the ring picture from the same places and stickers, a bad corner pointing at the edge place it pairs with by the pair definition above. It proves the three turn rules of section 4.1 on every case and every EO-keeping turn (`ring_turns`) and that the picture determines the case (`ring_faithful`). The side turns come from a direct definition, not a search: the cases reached with q quarter and h half turns of the side faces, closed under U and D turns at each step. From it: the side-turn histogram and the sub-7 count of each value (`side_turns`), a DR in 6 or less for every case with 2 side turns or fewer (`side_turns_certain`), and every cell of the per-DRM tables of section 5 (`side_turns_by_drm`, `profiles_by_drm`, `cross_by_drm`). For 4c4e: the row-swap table of the ring pairs, checked independently like the distances (`ring_swaps_checked`); half turns to two bars equal to the larger of row swaps and hole number on every case (`half_turns_to_bars`); every cell of the tables by half turns, by row swaps and holes, by pairs, of the card's groups and inside 3 half turns (`bands_4c4e`, `swaps_slot_4c4e`, `pairs_bands_4c4e`, `card_split_4c4e`, `inside3_4c4e`); that a row swap changes the pair count by at most 2 (`pair_change`); the 3-pair recipe on every ring pair with 3 pairs (`three_pair_rule`); and that the ring pictures of appendix A are exactly the ones with 2 row swaps or fewer (`patterns_le2`). The numbers it asserts are copied by a script from the study's output, not typed.

  **Not proved in Lean**: the rule search, most of the graded rules of section 9, the second-axis option, the RZP-weighted and real-attempt populations, and the result that switched cases are uniform within their class (an argument plus the sampled test above).

**Formally verified.** What Lean proves for this study, and what it doesn't:

- *Proved* (lean/EOSwitch, as in the last bullet above): the EO-kept distance to DR of all {= n(1082565) =} cases, the features defined from stickers, the distance histogram, the per-DRM counts and every cell of the card tables, and that the printed tables match them.
- *Proved, added 13 Nov 2026* (lean/EOSwitch, Recount.lean; marked ✓ in section 1 and the errata): the twelve switch cards (every row's states and sub-7 count, so each card's share, rate and settled share); the 4c4e your-call split by corner case; 4c4e by ARM × paired edges (Appendix A) and by paired edges × edge ARM, with both bad edges in one slice exactly when edge ARM is 0 or 2, on every 4c4e case; the settled shares of every feature (ARM, pairs, paired edges, corner case, pairs + ARM, pairs + corner case, paired edges + edge ARM, pairs + side pairs/2) for 4c4e, 4c2e, 7c8e, 8c8e and 2c2e; bars against two edges in every ARM; 7c8e with 4 pairs by edge ARM; the low DRMs by pairs and JZP; the EO's-last-turn option for 4c4e; the corner-case claims of rodneykinney ([[T8122]], [[T8123]]), Evan ([[D14342]], [[D14348]]) and Fanti ([[D15175]]) and the graded rules quoted in section 1 and the claims table (4c2e "1.5+ pairs" switches exactly Jay's and tseitsei89's cases; 2+ and 3+ pairs; rodneykinney's pair and corner-case rule ([[T8108]]); caycala's 3+ pairs; Daichi's and Zagros's 4-move rules; 7c8e 5-6 pairs; 2c2e 1+ pairs); errata b and c's shares by corner case; the corner case of every errata example and errata a's one-move NISS DR; and that the RZP's last quarter turn either way leaves the switched case unchanged (a general proof on the sticker model, with the premove step checked on every sequence of up to 3 turns).
- *Proved, for the ring sections* (lean/EOSwitch, Rings.lean and RingsThm.lean; marked ✓ in section 1 and sections 4 and 5): the turn rules of the ring picture on every case; side turns of every case, and that 2 or fewer means a DR in 6 or less; half turns to two bars as the larger of row swaps and hole number on every 4c4e case; the band tables (by half turns, by row swaps and holes, by pairs, the card's groups split, inside 3 half turns); at most two new pairs per row swap; the 3-pair recipe; the list of ring pictures with 2 swaps or fewer; side turns, setups and the cards crossed with them for the twelve DRMs.
- *An argument on top of those facts, not a Lean theorem*: why 2 side turns can't take more than 6 moves (two U/D turns before each side turn, none after the last) and why the half-turn count is the larger of the two readings (section 4.2). Lean checks both statements case by case; the reasons are on paper.
- *Proved, given the uniformity argument* (lean/EOSwitch): the better-of-normal-and-inverse option for 3c6e, 4c4e, 8c8e, 7c8e and 4c2e (Noah Swor's comparison, [[D6979]]), as the class average the uniformity argument gives.
- *Proved, for the errata* (the Corrections library in the folder of [*Which HTR routes to try from a DR*](../htr-routes/), lean/FakeBound/Corrections/Examples.lean, built on lean/EOSwitch): each errata example's DRM, ARM, pairs and distance to DR, and that its printed DR is valid (`eo_switch_examples`, items a, b and c), and the shortest case of each of the 15 4c4e ARM sets, so 11 sets sub-6 and 7 sub-5 (`arm_sets`, item a).
- *Computed, not proved*: the U/D turns per half-turn count (section 4.5 and appendix A), the DRs by quarter turns (section 4.6), where the half turn of a setup goes (section 5.4), the information measures, the two findings behind *no formula* (section 4.4), the ring reading on normal (sampled), the rule search and most of section 9's graded rules, the second-axis option, the RZP-weighted populations and the real attempts ({= n(6000) =} scrambles, including the sampled figures after a switch in section 1), the uniformity of switched cases within their class, and the NISS readings (sampled).

## Docs referred to

- Cale, [*DR setup stats*](https://docs.google.com/spreadsheets/d/11bTZ4Y7_6qKlIWo4a4TLW45M2ZkctQZAVxgQqEtlUs0) and [*DR setup stats (switching last move of EO)*](https://docs.google.com/spreadsheets/d/1_2PmFv1KyBX335SjSb4oweS0sx804fIhbuP50D-gBj4).
- Louis, [*DRM/ARM average optimals*](https://docs.google.com/spreadsheets/d/13fSwUROzP0hZQV1Cn96GndWbPy4UrsHiYTaWFSeWtJs), code at [github.com/LouisSart/DRM-ARM-stats](https://github.com/LouisSart/DRM-ARM-stats).
- rodneykinney, [*DRM corner variant+pair stats*](https://docs.google.com/spreadsheets/d/174ClwBFl-T2zJAq8MVyK1bKsIIuzxQU0_XmQGv82LPQ), [*DRM Subsets*](https://docs.google.com/document/d/1AUQVrecEFZyR6okXAyJgtQZA-A0AJmAUevhJZlQMjAs) with its [sheet](https://docs.google.com/spreadsheets/d/1gJxjQD77bb0u124cPBLQcS5IT2_6F97s-1qorfCKK2M) and [decision trees](https://rodneykinney.github.io/DRM-ARM-stats/drm_trees/), [*DRM Subsets Meta*](https://docs.google.com/document/d/1Jnd1Qy_6b1W5dR5fZQScloMoMPR2LCAF7VPrgeTaRgg), [*DR - 4c4e Theory*](https://docs.google.com/document/d/1DsxAAB2WRfpgDR-VWZZrXq2W4y_YMXBufRRYNLAGGoU), [*Axial Reduction Theory*](https://docs.google.com/document/d/1TomrUJ9XWAQXBp7ghSB-iXs1WpPm20FGUw5OBoKgn7g), [*Domino Setup Theory*](https://docs.google.com/document/d/1Z3O8BY1LbAMF6m55ufXtSdtBVwSJpMArtRrDT-p_CwM), and code at [github.com/rodneykinney/DRM-ARM-stats](https://github.com/rodneykinney/DRM-ARM-stats).
- Evan, [*4c4e ARM subtype stats*](https://docs.google.com/spreadsheets/d/1PAVonITR4HLBMml1-uxJwGRwHIoRWIGdNsK-A_KG_yA) and [*arm/pairs*](https://docs.google.com/spreadsheets/d/1YZYyokxYXwDdBTgN7ojpPAFHKKz48hCyNO2l6-iwmVk).
- Fanti, *armpairs_1.txt*, attached to the message of [[D15160]].
- Levi Gibson, [*Sub-7 simulations*](https://docs.google.com/spreadsheets/d/1Nqr2yICQqXuKrs1pkXWizsYw7-OU6FU4F7hzaE7pN2E).
- [*Hitchhiker’s Guide to DR*](https://docs.google.com/document/d/1E_5wSKvQFXXZY4f3xLM76qMUrVGp9Pe7vgotS0X-T4U) (the pair-tracing section is credited to wen).
- My earlier studies: [*EO to DR, and scramble to DR*](../eo-to-dr/) and [*Is DR-xs worth it?*](../is-dr-xs-worth-it/) (the sticker model).
- nissy 2.0.8, by Sebastiano Tronto ([nissy.tronto.net](https://nissy.tronto.net)), used for the cross-checks.
