## Appendix A: full tables

**4c4e by ARM and paired edges**: sub-7 share (cases in brackets).

{{c44_arm_paired}}

**4c4e by pairs and paired edges** (bars against separate pairs):

{{c44_bars}}

**4c2e, inside *pairs + side pairs/2 is exactly 1***:

{{c42_check}}

**8c8e by pairs**:

{{c88_pairs}}

**EO to DR by DRM, with the free options** (every case once; from my EO-to-DR study's definitions, recomputed here):

{{variants}}

## Appendix B: how it was computed, and what checks it

**The model.** A case is the twists of the 8 corners and the set of places holding the 4 E-slice edges, for an F/B EO and a U/D DR ({= n(1082565) =} cases). A breadth-first search with the 14 turns that keep the EO (U, D, R, L, F2, B2, each way) gives the exact distance to DR of every case: {= ', '.join(f'{a}: {n(b)}' for a, b in E['dist']) =}, mean {= E['dist_mean'][:6] =}. Features are defined from the faces the stickers are on (a sticker model of the cube), not from index strings. The RZP weights count every sequence of EO-keeping turns that first reaches its DRM, exactly. The real attempts use {= n(6000) =} uniformly random scrambles (random state, not nissy's scrambler, which has a bias). Everything runs in about six minutes on four cores, with each job capped at 4 GB.

**What checks it.**

- **The distances** equal my EO-to-DR study's table on all {= n(1082565) =} cases, and nissy 2.0.8 (`solve drud-eofb`) agrees on {= n(E['nissy']['agree']) =} of {= n(E['nissy']['positions']) =} random cases, with every nissy solution replayed to DR on the sticker model.
- **The options** (EO's last turn, the second axis, normal or inverse) equal the EO-to-DR study's per-case tables in all {= E['checks_variants']['plain']['compared'].split()[0] =} cells, to their printed rounding.
- **The features** pass {= E['features_tests'] =} unit tests on hand-made cases from the server's examples (`R` is 4c4e JZP with 4 pairs; `R U` is 4c4e ARM 21; `U' F2 B2 R2 U2 R` is ARM 02 with no pairs and 6 moves, and so on). They also agree with rodneykinney's own string code (DRM, ARM, pairs, fake pairs, side pairs, AR pairs) on all {= n(1082565) =} cases, once the corner order is read the way both Louis's and rodneykinney's comments mean it.
- **The NISS readings** of section 5 hold on every sampled cube ({= n(NISS('ARM axis swap: ARM for U/D DR on normal = ARM for R/L DR on inverse (uniform)')[0]) =} uniform and {= n(NISS('ARM axis swap: ARM for U/D DR on normal = ARM for R/L DR on inverse (4c4e)')[0]) =} 4c4e cubes per reading; {= n(TRACE('side pairs', '4c2e')[0]) =} more from 4c2e for the new ones).
- **Switched cases are uniform** within their class: the real attempts' rate against the uniform rate of their own class mix in {= n(E['uniform_cells']) =} DRM × length cells, worst {= f2(E['uniform_worst_z']) =} standard errors (20 batches of 300 scrambles).
- **Every example** in this write-up, the errata and the worked examples is replayed on the sticker model of my DR-xs study (`cube.py`): the scramble and EO + RZP give the stated DRM, the switched case has the stated features, and the DR written out reaches DR with the EO kept, in the stated number of moves.
- **Lean.** A Lean 4 certificate in the study's folder (`lean/EOSwitch`, no Mathlib, no `sorry`) builds its own cube from stickers and runs its own BFS over all {= n(1082565) =} cases with the 14 EO-keeping turns. An independent checker confirms each entry: 0 exactly at DR, never more than one above a neighbour, and one below some neighbour. It defines the features from stickers (pairs, fake pairs, paired edges, bars, side pairs, same slice, the ARM counts, JZP) and redoes 27 of the feature unit tests. It proves the distance histogram (mean {= E['dist_mean'][:6] =}), the per-DRM counts for 4c4e, 4c2e, 3c2e, 7c8e, 8c8e and 2c2e, and every cell of the card tables: 4c4e by paired edges and by paired edges × same slice, pairs × paired edges, 4c2e by pairs + side pairs/2, 7c8e by pairs, 2c2e by paired edge × JZP, and 3c2e. It also proves that the study's printed tables match those cells. Build: `lake build`, under a minute. **Not proved in Lean**: the corner case and its suffix and every ARM-based rule (except the shortest case per 4c4e ARM set, below), the rule search, the free options (last turn, second axis, inverse), the RZP-weighted and real-attempt populations, and the result that switched cases are uniform within their class (an argument plus the sampled test above).

**Formally verified.** What Lean proves for this study, and what it doesn't:

- *Proved* (lean/EOSwitch, as in the last bullet above): the EO-kept distance to DR of all {= n(1082565) =} cases, the features defined from stickers, the distance histogram, the per-DRM counts and every cell of the card tables, and that the printed tables match them.
- *Proved, for the errata* (the Corrections library in the folder of [*Which HTR routes to try from a DR*](../htr-routes/), lean/FakeBound/Corrections/Examples.lean, built on lean/EOSwitch): each errata example's DRM, ARM, pairs and distance to DR, and that its printed DR is valid (`eo_switch_examples`, items a, b and c), and the shortest case of each of the 15 4c4e ARM sets, so 11 sets sub-6 and 7 sub-5 (`arm_sets`, item a).
- *Computed, not proved*: the corner cases and every share by corner case (errata b and c), the rule search and its rules, the RZP-weighted populations and the real attempts ({= n(6000) =} scrambles), and the NISS readings, including the one-move NISS DR of errata a's example (nissy and the sticker model).

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
