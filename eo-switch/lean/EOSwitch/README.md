# EOSwitch: a Lean 4 certificate for the exact tables of "When to switch on an EO"

Lean 4.35.0, no Mathlib (only the library that ships with Lean). About 690 lines written by hand (`Switch.lean`, `Parse.lean`, `Model.lean`, `Theorems.lean`, `Audit.lean`), plus `Cube.lean`, `Pieces.lean` and `Search.lean` copied from eo-to-dr's certificate, and `EOSwitch/Study.lean`, which is generated. No `sorry`.

The study's switch rules rest on exact tables over the 1,082,565 EO-solved states: every corner twist (3^7) × every placement of the four E-slice pieces (C(12,4) = 495), F/B EO solved, target DR on U/D, EO kept (turns U D R L F2 B2). The research computes the distances in Rust (`research/eoswtools dist`) and the features in Python (`research/src/features.py`). This project computes both again in Lean, from its own definitions of the cube and the face turns, and states each table as a theorem. Then it checks the research's output against them: `out/dist_hist.txt` and `out/variants_by_drm.tsv` are copied verbatim into `EOSwitch/Study.lean`, along with seven tables of `out/SUMMARY.md`. The theorems named `…_matches_study` say that Lean's numbers equal those files. They all do. One printed digit was off (the 2c2e mean in SUMMARY section 1, 6.880 for 6.879); `summary.py` was fixed on 2026-11-13 and `summary_2c2e_mean` now pins 6.879.

The full BFS fits easily: Lean does it directly, over 26.9 million slots (1,082,565 reached), and `search.ruleHolds` checks the result independently (see Trust). No distance table is taken from the research.

Words, as in the research's `features.py`. A corner is *bad* when it is twisted. Its *U/D sticker axis* is the axis of the face its U or D sticker is on. A *bad U/D edge* is an E-slice piece in a U/D-layer place. The *M places* are UF UB DF DB; the *S places* are UR UL DR DL. The two corners *next to* an edge place are those that agree with it on its two non-zero coordinates. A *pair* is a bad U/D edge plus a bad corner next to it whose U/D sticker is on the face the edge does not touch (R/L for an M place, F/B for an S place). With the U/D sticker on the other axis it is a *fake pair*. *Paired edges* are the bad U/D edges with at least one pair. *Side pairs* count, over the E-slice places that hold a non-E piece, the bad corners next to them whose U/D sticker is on F or B. *Same slice* means at least two bad U/D edges, all in M places or all in S places. The DRM is *xcye*: x bad corners, y = 2 × bad U/D edges. *JZP* means no bad corner with its U/D sticker on R/L, no E piece in an M place, and an even number of bad corners. *Sub-7* means DR in at most 6.

## What is proved

**A. The model and the features** (`EOSwitch/Model.lean`)

| Theorem | It says |
|---|---|
| `model_size` | 54 stickers, all different; 18 face turns with the usual names, each a permutation of the 54 places. |
| `places` | 12 edge places of 2 stickers and 8 corner places of 3, together the 48 non-centre stickers. The E-slice places are the four with no U or D sticker, and the solved cube's E-slice mask marks them. |
| `keep_fb_eo` | A turn changes an edge's F/B goodness exactly when it is an F or B quarter turn and the edge is on that face. So the turns that keep F/B EO are exactly the 14 of the BFS (`KEEP`). |
| `turns_permute_pieces` | Each turn permutes the edge places and the corner places. It carries each corner's sticker list (U/D sticker first, then round the corner) onto the destination's list, shifted cyclically. The shifts sum to 0 mod 3. |
| `coordinates_follow_stickers` | On every sticker state within 3 turns of solved, and for every turn, the twist number and the E-slice mask after the turn are what `coAct` and `maskAct` compute from those before it. The solved cube has twist 0, F/B EO and its E pieces home. |
| `feature_places` | The geometry the features use. There are 8 U/D-layer places and 4 E-slice places. The M places are the U/D-layer places with no R or L sticker; the S places have no F or B sticker. Every edge place has exactly two corners next to it, each sharing two faces with it. For a U/D-layer place they are in its layer, and its zero axis is R/L (M) or F/B (S). For each corner, twist 0 puts the U/D sticker on U/D, and twists 0, 1, 2 put it on the three axes, one each. |
| `feature_examples` | 27 states from the research's feature unit tests, redone on the sticker model: the 25 distinct states of `features.py` TESTS and the two of E1, as printed in `out/checks_features.txt`. E14 is not redone. Each state is built with a move sequence (for example "solved by U' F2 B2 R2 U2 R"). For each, the state has F/B EO, and every value the file prints comes out the same: DRM, ARM (corners, edges), pairs, fake pairs, side pairs and the distance to DR. R L is JZP. |

**B. EO-kept DR distance** (`EOSwitch/Theorems.lean`; the research's `eoswtools dist`)

| Theorem | It says |
|---|---|
| `dist_checked` | `dist` is a BFS over (twist number 0 … 6560) × (12-bit E-slice mask) with the 14 EO-keeping turns, to DR on U/D. It passes `search.ruleHolds`, so each entry is the fewest such turns to DR. It reaches exactly the twist vectors with sum ≡ 0 (mod 3) × the 4-bit masks, 1,082,565 states. Every state's features fit the cell table. |
| `dist_hist` | 0 … 10 turns: **1, 2, 17, 134, 1065, 8190, 54694, 267576, 560568, 187204, 3114** (Cale's table). Σ = 8,447,364, and 64,103 states are sub-7. |
| `dist_mean_digits` | 2187 × 495 = 1,082,565; 8447364/1082565 = **7.8031**… (Cale's 7.80). |
| `drm_stats` | [states, ≤ 5, ≤ 6, ≤ 7, Σ distance] per DRM. 4c4e [70560, 3064, 13576, 41926, 507090]; 4c2e [13440, 448, 2512, 8432, 96232]; 3c2e [3584, 688, 2208, 3536, 22088]; 7c8e [23520, 744, 3856, 13496, 170624]; 8c8e [6020, 100, 872, 3794, 43522]; 2c2e [1792, 48, 424, 1536, 12328]. |

**C. The cells of the headline rules** (`EOSwitch/Theorems.lean`; P1, every state once). Each cell is [states, ≤ 5, ≤ 6 (sub-7), ≤ 7].

| Theorem | Cells |
|---|---|
| `cells_4c4e_edges_paired` | Paired edges 0: [21000, 74, 910, 6658]; 1: [38640, 800, 6124, 24772]; 2: [10920, 2190, **6542**, 10496]. |
| `cells_4c4e_edges_paired_same_slice` | (paired, same slice) (0,0) [11568, 48, 608, 4160]; (0,1) [9432, 26, 302, 2498]; (1,0) [22944, 656, **4592**, 16776]; (1,1) [15696, 144, **1532**, 7996]; (2,0) [5808, 1376, 3800, 5680]; (2,1) [5112, 814, 2742, 4816]. |
| `cells_4c4e_pairs_edges_paired` | (pairs, paired edges) (0,0) [21000, 74, 910, 6658]; (1,1) [31200, 480, 4144, 18560]; (2,1) bar [7440, 320, **1980**, 6212]; (2,2) [8400, 1336, **4528**, 7992]; (3,2) [2400, 760, 1896, 2384]; (4,2) [120, 94, 118, 120]. In 4c4e, bars = pairs − paired edges. |
| `cells_4c2e_pairs_plus_half_side` | 2·pairs + side pairs, i.e. 2 × (pairs + side/2): 0 [4376, 8, 64, 1256]; 1 [2768, 0, 224, 1592]; 2 [3304, 0, 520, 2648]; 3 [1664, 144, 856, 1624]; 4 [904, 128, 520, 888]; 5 [368, 144, 280, 368]; 6 [56, 24, 48, 56]. |
| `cells_7c8e_pairs` | Pairs 1 [480, 0, 0, 32]; 2 [3360, 0, 72, 792]; 3 [7920, 0, 264, 3232]; 4 [7920, 40, 1256, 5840]; 5 [3360, 480, 1824, 3120]; 6 [480, 224, 440, 480]. |
| `cells_2c2e_edges_paired_jzp` | Paired edge 0 [1376, 0, 176, 1120], 1 [416, 48, 248, 416]. Split by JZP, (paired, JZP): (0,0) [1232, 0, 120, 976]; (0,1) [144, 0, 56, 144]; (1,0) [304, 32, 168, 304]; (1,1) [112, 16, 80, 112]. |
| `cells_3c2e` | One cell: [3584, 688, **2208**, 3536] (61.6%, "always switch"). |
| `headline_digits` | The percentages of SUMMARY's findings 2–5 from these cells (kernel arithmetic). 4c4e neither paired 4.33% of 29.7%, both paired 59.9% of 15.47%. Bar 26.6% vs on both edges 53.9%. 2+ pairs: 26.0% of states at 46.4%. With one paired edge, same slice 9.76% vs 20.01%. The 6-cell verdict covers 67.48%. 4c2e "1.5+": 56.95% on 22.26%, holding 67.8% of sub-7; values 0, 1, 2: 1.46%, 8.09%, 15.7%; verdict on 75.4%. 7c8e ≤ 3 pairs 2.85%, 5–6 pairs 58.9%. 3c2e 61.6%. 2c2e with a paired edge 59.6%. |

**D. Agreement with the research's files** (`EOSwitch/Theorems.lean`)

| Theorem | It says |
|---|---|
| `dist_matches_study` | `out/dist_hist.txt` is Lean's histogram, value by value. |
| `variants_match_study` | Every row of `out/variants_by_drm.tsv` (41 DRMs and "all") has Lean's number of states. Its share, mean and plain ≤ 5/≤ 6/≤ 7 columns are Lean's exact fractions rounded to the printed digits (|exact − printed| ≤ half a unit of the last digit). The DRM rows cover all 1,082,565 states. |
| `summary_tables_match_study` | Seven tables of `out/SUMMARY.md`. Section 1 (12 DRMs + all): states equal; plain, ≤ 5, ≤ 7 and the mean rounded correctly, except the 2c2e mean. The six feature tables of section 4 (4c4e paired edges; paired × same slice; pairs × paired edges; 4c2e pairs + side/2; 7c8e pairs; 2c2e paired × JZP): the rows are Lean's cells in order, with equal states, and "share" and "p<=6 P1" rounded correctly. |
| `summary_2c2e_mean` | **The one printed digit that is off.** SUMMARY section 1 prints the 2c2e mean as 6.880. The exact mean is 12328/1792 = 6.87946…, which rounds to 6.879. `summary.py` re-rounds variants_by_drm.tsv's 6.8795 to three places. Cosmetic only. |

**E. Recounts for the pages and the errata** (`EOSwitch/Full.lean`, `EOSwitch/Recount.lean`; added 2026-11-13)

`Full.lean` adds the remaining features the rules use, defined from places and stickers as in `features.py`: the corner case 4a–4d (tetrad {ULF URB DRF DLB} = places with x·y·z = −1), its suffix, "stacked" (all bad corners on one R/L side), corners on one layer, anti-AR, wen's split pairs, "4a one U/D turn from 4d", "R L gives JZP", the twist-1 count; and per state the distances with the EO's last turn free (min over s, s·F2) and the last two free (s, s·F2, s·B2, s·F2·B2). `T` groups all 1,082,565 states by their feature record (39,140 groups) with the three distance histograms. `cell c e p` = [states, ≤ 5, ≤ 6, ≤ 7] of DRM xcye with property p.

| Theorem | It says |
|---|---|
| `full_table` | `T` has every reached state; every feature record survives packing; JZP from the tables equals `feat`'s. |
| `corner_case_your_call` | 4c4e, one paired edge, edge ARM 1, by corners: 4d [576, 128, 512, 576] (88.9%); 4b ARM 21 1488/4512; 4a ARM 21 432/2304; 4a corner ARM 0/4 408/1728; corner ARM 1/3 1560/10368; 4b corner ARM 0/4 192/3456. |
| `errata_b_3qt` | 4c2e 4b-0 by pairs 0, 1, 2: 80/960, 232/384, 152/192 (8.3%, 60.4%, 79.2%). |
| `errata_c_stacked` | 4c4e, 1 pair, ARM 21: a 392/2016, b 1104/3840 (28.75%), d 512/576; a stacked 120/336 (35.7%), a not stacked 272/1680 (16.2%). |
| `corner_case_claims` | Claims T8122 (4a-0, 4a-2, 4b-0, 4b-2), T8123 (0 pairs, 0 fake: 4a-0 28/120, no 4d, 4b-2 112/576), D14342 (4d, 1 pair, ARM 20/21/22: 0, 512/576, 0), D14348 (4a by ARM 2X). |
| `arm_4c4e` | 4c4e by ARM × paired edges, all 15 ARMs (Appendix A); the "trash" ARMs 02, 12, 30, 40 are all under 4%. |
| `paired_edge_arm_4c4e` | 4c4e by paired edges × edge ARM (9 cells); on 4c4e, both bad edges in one slice exactly when edge ARM ≠ 1 (all 70,560 states). |
| `pairs4_7c8e` | 7c8e with 4 pairs by edge ARM (528/1744 for edge ARM 1) and by ARM 11, 12, 33, 41, 62, 21 (claim D15175). |
| `bars_by_arm` | 4c4e, 2 pairs, per ARM: bar on one edge against pairs on the two edges (gap 11.8 to 31.2 points). |
| `strict_separation` | Settled shares (cells under 10% or over 50%) of 8 keys on 4c4e, 4c2e, 7c8e, 8c8e, 2c2e (`decided_by_feature`; ARM 22032/70560, pairs 23520, pairs + ARM 34992). |
| `rule_cards` | The 12 switch cards, each row as [states, ≤ 5, ≤ 6, ≤ 7], first matching row wins. |
| `low_drm_pairs` | 4c6e, 3c4e, 3c6e, 5c4e, 5c6e, 6c6e by pairs and JZP. |
| `graded_rules` | 4c2e: "1.5+ pairs", Jay's and tseitsei89's rules switch exactly the same states; 4c4e 2+ pairs, 3+ pairs, T8108, caycala's 3+ off one layer, Daichi's and Zagros's 4-move rules (DR ≤ 7); 7c8e 5-6 pairs; 2c2e 1+ pairs. |
| `last_turn_4c4e` | 4c4e sub-7: 13,576; with the EO's last turn free 19,798 (+8.8 points); last two free 25,304. |
| `inverse_option` | Better of normal and inverse, DR ≤ 6, as the class average of the uniformity argument (the argument itself is not proved): 3c6e 1 in 10.57, 4c4e 2.875, 8c8e 3.724, 7c8e 3.322, 4c2e 2.950. |
| `example_labels` | The errata examples' DRM, ARM, pairs, corner case and suffix, lr and distance (a 4a-4, b 4b-0, c 4a not stacked); T8123's `F2 B2 R` (4a-0, 3) and `D F2 B2 R` (4b-2, 4); errata a's NISS DR: `U F2 B2 U L` then L is DR. |
| `cax_map_eq`, `coset_of_relabel` | Proved by rewriting, for every sticker array: two relabellings that agree on every label's colour axis give the same twists and E-slice places. |
| `rzp_last_turn` | For every face, X and X' agree on the colour axis of every label; and a premove is a relabelling (checked on every sequence of up to 3 turns). So the RZP's last quarter turn either way gives the same switched case. |

Every number of E was compared with the pages (WRITEUP section 1, the cards, Appendix A, the errata, the claims table) on 2026-11-13: all agree with the printed rounding. One tie: errata c prints b corners as 28.7%, the exact value is 1104/3840 = 28.75% exactly (28.8% under round-half-up); either is a correct rounding.

## Files

| File | Content |
|---|---|
| `EOSwitch/Cube.lean` | The sticker model: 54 stickers and the 18 face turns built from geometry. Copied from eo-to-dr's certificate, changing only the namespace and the header. **Read this to convince yourself the model is the cube.** |
| `EOSwitch/Pieces.lean`, `EOSwitch/Search.lean` | Copied from eo-to-dr's certificate (namespace and first header line changed). Edge places, corner twist and the E-slice mask read off stickers, with what each turn does to them; `bfs` and the independent check `ruleHolds`. |
| `EOSwitch/Switch.lean` | The BFS (`dist`), the geometry of the places (`UD_PLACES`, `M_PLACES`, `NB`, `ZAX`, `UDAX`), the features (`feat`), the tally of (DRM, features) cells with their distance histograms (`run`), and the readings (`split`, `drm`, `total`). |
| `EOSwitch/Study.lean` | Generated by `gen_study.py`: `research/out/dist_hist.txt`, `variants_by_drm.tsv`, and seven tables of `SUMMARY.md` (each from its heading line to the table's end), verbatim. |
| `EOSwitch/Parse.lean` | Reads those files and checks a printed decimal against an exact fraction (`roundsTo`). |
| `EOSwitch/Model.lean`, `EOSwitch/Theorems.lean` | The theorems: A, and B to D. |
| `EOSwitch/Audit.lean` | `#print axioms` for every theorem. |
| `EOSwitch/Full.lean`, `EOSwitch/Recount.lean` | Part E: the extra features, the grouped table `T`, and its theorems. |
| `gen_study.py` | Writes `EOSwitch/Study.lean`. Rerun it after the research's outputs change; if a number changed, the build fails. |

## Build

    source /data/fmc/env.sh
    cd /data/fmc/eo-switch/lean/EOSwitch
    systemd-run --user --scope -q -p MemoryMax=5G lake build

From a clean tree (`rm -rf .lake/build`) on the 4-core VM, this took 263 s wall time, 179 s CPU and 0.72 GB peak memory (2026-11-13, with part E; before it, 37 s). `Full.lean` takes 29 s and `Recount.lean` 93 s (building the grouped table `T` and running its theorems). The BFS and the tally (`run`) take about 7.7 s. They are top-level constants, so the compiled code computes them once per Lean process, when the module is loaded. Each file that imports `Switch` therefore takes about 8 s, even when it uses neither: `Parse.lean` 7.9 s, `Model.lean` 8.6 s, `Theorems.lean` 9.3 s, `Audit.lean` and the root about 7.7 s each. Within a file, all theorems share one computation. The last step prints the audit.

`lakefile.toml` sets `precompileModules = true`, as in the earlier certificates. EODR's two notes apply here too. Large tables are top-level constants, and `tally` is `@[noinline]` and receives the BFS table as an argument. After editing a definition file, build the whole project.

## Trust

- Every theorem that runs a computation is proved by `native_decide`. Lean compiles the statement, runs it, and accepts the answer `true`. This trusts the Lean compiler and the C compiler, not only Lean's kernel. `Audit.lean` shows one axiom per such theorem (`<theorem>._native.native_decide.ax_…`), next to Lean's standard axioms. A wrong number does fail: for example, `split run.cells 3 2 (fun _ => []) = [([], [3584, 688, 2209, 3536])]` and `parse.roundsTo 6542 10920 "0.598" = true` are both rejected.
- `dist_mean_digits` and `headline_digits` (arithmetic) are proved by `decide`, the kernel alone, with no axioms.
- `search.ruleHolds` does not trust `bfs`. For every state with an entry, it checks three things. The entry is 0 exactly at DR. Every turn leads to a state with an entry, with d(x) ≤ d(after the turn) + 1. A non-DR state has a turn to an entry one lower. So the entries are the true fewest-turn counts, whatever `bfs` did. The argument is in `Search.lean`'s header; it is not a Lean theorem.
- `run.encodable` checks that every state's features lie inside the ranges of the cell table and survive `encode`/`decode`. So no state is lost or mixed into another cell. An early version capped `bars` at 2, and this check plus the histogram caught the 4 states with more.
- What a theorem says is exactly what its Lean statement says about the Lean definitions. That those definitions are the cube and the study's features is for the reader to check. The evidence is in A. The coordinates follow the sticker model. `feature_places` checks the geometry. `feature_examples` gives every printed feature value on 27 of the research's worked examples. The cell tables equal the research's: by count in D, and exactly, cell by cell, against the research's `out/big/feat.npz` in a check outside Lean (see below).

## Where the Lean differs from the research

- **Coordinates.** The research indexes states as co · 495 + rank of the E-slice set, with its own corner order and twist numbering (`geom.py`). The Lean uses Σ twist·3^c over its own corner places, with a raw 12-bit mask. The features never use the twist number itself, only the face that the U/D sticker is on (`UDAX`, read off the stickers), so numbering conventions cannot matter. All comparisons are by content (histograms, cells by feature value), never by index.
- **Cell tables against the research's exact counts.** The research's files print shares, not counts, for the cells. To compare exact counts, the per-cell [states, ≤ 5, ≤ 6, ≤ 7] were also computed from the research's `out/big/feat.npz` (its features and distances for every coset) in Python. All the cells of C were equal. That check is not part of the build, because `feat.npz` is a 2 MB generated file in `out/big/`. The build compares with the printed tables (D).

## Not proved in Lean

- **The rule search** over 38 features (`search_*.tsv`) and the features only it uses (AR bars, layer layouts other than one-layer, corner-only distance, trigger-family distances); most graded rules of section 7 (those used in section 1 and the claims are in E).
- **The free options**: the second DR axis; normal-or-inverse beyond E's class-average figures (which rest on the uniformity argument); lastF/lastFB beyond 4c4e (EODR proves lastF per case). Also the RZP-weighted population P2 (`eoswtools rzp`) and the sampled real attempts P3 (121,527,134 attempts). Their columns in SUMMARY and variants_by_drm.tsv are not checked.
- **That the switched state is uniform within its class** (finding 1). This is the study's argument plus a sampled test, and is what lets the P1 counts stand for real switched attempts.
- The research's checks against eo-to-dr's table, nissy, the NISS predictors and Rodney's string code are research-side and not redone here. The distance table is redone from scratch, so the eo-to-dr comparison is covered in substance: eo-to-dr's own certificate proves the same histogram.
