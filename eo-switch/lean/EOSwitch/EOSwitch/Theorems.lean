/-
  EOSwitch.Theorems — checked statements, parts B to D (see README.md).  Every one is a closed statement about the
  definitions in Cube / Pieces / Search / Switch / Parse, proved by running them: `native_decide` evaluates the
  statement with compiled code and accepts the answer (this trusts the Lean compiler; see README.md).  Statements
  that are plain arithmetic on numbers are proved by `decide` (Lean's kernel alone).

  Reading aid.  `run.cells`: every (DRM, features) cell that occurs, with its histogram of EO-kept distances to DR.
  `split run.cells x y key`: the states of DRM xcye grouped by the value of `key`, each group as
  (key value, [states, DR in ≤ 5, DR in ≤ 6 ("sub-7"), DR in ≤ 7]).  Feature names as in Switch.lean.
-/
import EOSwitch.Parse

namespace EOSwitch
open sw

set_option maxHeartbeats 0

/-! ## B. EO-kept DR distance over the 1,082,565 states -/

/-- The BFS over (corner twists, places of the E-slice pieces) with the 14 EO-keeping turns passes the independent
check `search.ruleHolds` (so each entry is the fewest such turns to DR on U/D); the states it reaches are exactly
the twist vectors with sum ≡ 0 (mod 3) times the sets of 4 places, 1,082,565 of them; and every state's features
fit the cell table. -/
theorem dist_checked :
    run.rule = true ∧ run.reachedIsValid = true ∧ run.states = 1082565 ∧ run.encodable = true := by
  native_decide

/-- EO kept, one DR axis: 0 … 10 turns for 1, 2, 17, 134, 1065, 8190, 54694, 267576, 560568, 187204, 3114 states
(Cale's table); the distances sum to 8,447,364; 64,103 states have DR in at most 6. -/
theorem dist_hist :
    total run.cells = [1, 2, 17, 134, 1065, 8190, 54694, 267576, 560568, 187204, 3114, 0] ∧
    weighted (total run.cells) = 8447364 ∧ le (total run.cells) 6 = 64103 := by
  native_decide

/-- 2187 × 495 = 1,082,565; the mean 8447364 / 1082565 = 7.8031… (Cale's 7.80). -/
theorem dist_mean_digits : 2187 * 495 = 1082565 ∧ 8447364 * 10000 / 1082565 = 78031 := by decide

/-- Per DRM of the study's main rules: [states, DR in ≤ 5, ≤ 6, ≤ 7, Σ distance]. -/
theorem drm_stats :
    parse.stats (total (drm run.cells 4 4)) = [70560, 3064, 13576, 41926, 507090] ∧
    parse.stats (total (drm run.cells 4 2)) = [13440, 448, 2512, 8432, 96232] ∧
    parse.stats (total (drm run.cells 3 2)) = [3584, 688, 2208, 3536, 22088] ∧
    parse.stats (total (drm run.cells 7 8)) = [23520, 744, 3856, 13496, 170624] ∧
    parse.stats (total (drm run.cells 8 8)) = [6020, 100, 872, 3794, 43522] ∧
    parse.stats (total (drm run.cells 2 2)) = [1792, 48, 424, 1536, 12328] := by
  native_decide

/-! ## C. The cells of the headline rules (P1: every state once) -/

/-- 4c4e by the number of bad U/D edges with a pair (`edgesPaired`). -/
theorem cells_4c4e_edges_paired :
    split run.cells 4 4 (fun k => [k.edgesPaired]) =
      [([0], [21000, 74, 910, 6658]),
       ([1], [38640, 800, 6124, 24772]),
       ([2], [10920, 2190, 6542, 10496])] := by
  native_decide

/-- 4c4e by paired edges and whether the two bad U/D edges are in one slice (both in M places or both in S
places: `sameSlice`, 1 = yes). -/
theorem cells_4c4e_edges_paired_same_slice :
    split run.cells 4 4 (fun k => [k.edgesPaired, b2n k.sameSlice]) =
      [([0, 0], [11568, 48, 608, 4160]),
       ([0, 1], [9432, 26, 302, 2498]),
       ([1, 0], [22944, 656, 4592, 16776]),
       ([1, 1], [15696, 144, 1532, 7996]),
       ([2, 0], [5808, 1376, 3800, 5680]),
       ([2, 1], [5112, 814, 2742, 4816])] := by
  native_decide

/-- 4c4e by pairs and paired edges: 2 pairs as a bar on one edge ([2, 1]) or on both edges ([2, 2]).  With two bad
U/D edges, bars = pairs − paired edges, and Lean's `bars` agrees. -/
theorem cells_4c4e_pairs_edges_paired :
    split run.cells 4 4 (fun k => [k.pairs, k.edgesPaired]) =
      [([0, 0], [21000, 74, 910, 6658]),
       ([1, 1], [31200, 480, 4144, 18560]),
       ([2, 1], [7440, 320, 1980, 6212]),
       ([2, 2], [8400, 1336, 4528, 7992]),
       ([3, 2], [2400, 760, 1896, 2384]),
       ([4, 2], [120, 94, 118, 120])] ∧
    (drm run.cells 4 4).all (fun r => r.1.bars + r.1.edgesPaired == r.1.pairs) := by
  native_decide

/-- 4c2e by 2 × (pairs + side pairs / 2) = 2 · pairs + side pairs (Rodney's "1.5+ pairs" is a value ≥ 3). -/
theorem cells_4c2e_pairs_plus_half_side :
    split run.cells 4 2 (fun k => [2 * k.pairs + k.side]) =
      [([0], [4376, 8, 64, 1256]),
       ([1], [2768, 0, 224, 1592]),
       ([2], [3304, 0, 520, 2648]),
       ([3], [1664, 144, 856, 1624]),
       ([4], [904, 128, 520, 888]),
       ([5], [368, 144, 280, 368]),
       ([6], [56, 24, 48, 56])] := by
  native_decide

/-- 7c8e by pairs. -/
theorem cells_7c8e_pairs :
    split run.cells 7 8 (fun k => [k.pairs]) =
      [([1], [480, 0, 0, 32]),
       ([2], [3360, 0, 72, 792]),
       ([3], [7920, 0, 264, 3232]),
       ([4], [7920, 40, 1256, 5840]),
       ([5], [3360, 480, 1824, 3120]),
       ([6], [480, 224, 440, 480])] := by
  native_decide

/-- 2c2e by whether its bad U/D edge has a pair, and by JZP (1 = yes). -/
theorem cells_2c2e_edges_paired_jzp :
    split run.cells 2 2 (fun k => [k.edgesPaired]) =
      [([0], [1376, 0, 176, 1120]),
       ([1], [416, 48, 248, 416])] ∧
    split run.cells 2 2 (fun k => [k.edgesPaired, b2n k.jzp]) =
      [([0, 0], [1232, 0, 120, 976]),
       ([0, 1], [144, 0, 56, 144]),
       ([1, 0], [304, 32, 168, 304]),
       ([1, 1], [112, 16, 80, 112])] := by
  native_decide

/-- 3c2e, one cell ("always switch"): 3,584 states, 2,208 with DR in at most 6. -/
theorem cells_3c2e :
    split run.cells 3 2 (fun _ => []) = [([], [3584, 688, 2208, 3536])] := by
  native_decide

/-- The headline percentages of SUMMARY's findings, from the cells above (cut, not rounded, after the digits
shown; the study rounds).
* 4c4e: neither bad edge paired 910/21000 = 4.33% of 21000/70560 = 29.7%; both paired 6542/10920 = 59.9% of
  10920/70560 = 15.47%; 2 pairs as a bar 1980/7440 = 26.6%, on both edges 4528/8400 = 53.9%; 2+ pairs:
  18360/70560 = 26.0% of states at 8522/18360 = 46.4%.
* 4c4e, one paired edge: same slice 1532/15696 = 9.76%, otherwise 4592/22944 = 20.01%; the 6-cell rule's cells
  under 10% or over 50% hold 47616/70560 = 67.48%.
* 4c2e: value ≥ 3 ("1.5+ pairs"): 1704/2992 = 56.95% sub-7 on 2992/13440 = 22.26% of 4c2e, holding 1704/2512 =
  67.8% of its sub-7 states; values 0, 1: 1.46%, 8.09%; value 2: 15.7%; verdict (0, 1, ≥ 3) on 10136/13440 = 75.4%.
* 7c8e: 3 or fewer pairs 336/11760 = 2.85%; 5-6 pairs 2264/3840 = 58.9%.
* 3c2e: 2208/3584 = 61.6%; 2c2e with a paired edge 248/416 = 59.6%. -/
theorem headline_digits :
    910 * 1000 / 21000 = 43 ∧ 21000 * 1000 / 70560 = 297 ∧ 6542 * 1000 / 10920 = 599 ∧ 10920 * 10000 / 70560 = 1547 ∧
    1980 * 1000 / 7440 = 266 ∧ 4528 * 1000 / 8400 = 539 ∧
    7440 + 8400 + 2400 + 120 = 18360 ∧ 1980 + 4528 + 1896 + 118 = 8522 ∧
    18360 * 1000 / 70560 = 260 ∧ 8522 * 1000 / 18360 = 464 ∧
    1532 * 10000 / 15696 = 976 ∧ 4592 * 10000 / 22944 = 2001 ∧
    11568 + 9432 + 15696 + 5808 + 5112 = 47616 ∧ 47616 * 10000 / 70560 = 6748 ∧
    1664 + 904 + 368 + 56 = 2992 ∧ 856 + 520 + 280 + 48 = 1704 ∧
    1704 * 10000 / 2992 = 5695 ∧ 2992 * 10000 / 13440 = 2226 ∧ 1704 * 1000 / 2512 = 678 ∧
    64 * 10000 / 4376 = 146 ∧ 224 * 10000 / 2768 = 809 ∧ 520 * 1000 / 3304 = 157 ∧
    4376 + 2768 + 2992 = 10136 ∧ 10136 * 1000 / 13440 = 754 ∧
    0 + 72 + 264 = 336 ∧ 480 + 3360 + 7920 = 11760 ∧ 336 * 10000 / 11760 = 285 ∧
    1824 + 440 = 2264 ∧ 2264 * 1000 / 3840 = 589 ∧
    2208 * 1000 / 3584 = 616 ∧ 248 * 1000 / 416 = 596 := by
  decide

/-! ## D. Agreement with the research's output files -/

/-- The research's histogram (`out/dist_hist.txt`, `eoswtools dist`) is Lean's, value by value. -/
theorem dist_matches_study :
    parse.distHist = ((List.range 12).map fun v => (v, (total run.cells)[v]!)).filter (·.2 != 0) := by
  native_decide

/-- Every row of `out/variants_by_drm.tsv` (41 DRMs and "all") agrees with Lean: the number of states is equal, and
the share of all states, the mean distance and the plain ≤ 5, ≤ 6, ≤ 7 shares are Lean's exact fractions rounded
to the printed digits; the DRM rows cover all 1,082,565 states. -/
theorem variants_match_study : parse.variantsOk run.cells = true := by
  native_decide

/-- The seven tables of `out/SUMMARY.md` that these numbers come from agree with Lean.  Section 1's table (12 DRMs
and "all"): states equal; plain (≤ 6), ≤ 5 and ≤ 7 shares and the mean are the exact values rounded to the printed
3 digits, except the 2c2e mean (`summary_2c2e_mean`).  The six feature tables of section 4: the rows are, in order,
Lean's cells with the same feature values, with the same number of states, and their "share" and "p<=6 P1" columns
are Lean's exact values rounded. -/
theorem summary_tables_match_study :
    parse.plainOk run.cells ["2c2e"] = true ∧
    parse.featTableOk run.cells study.SUM_4C4E_PAIRED 4 4 1 (fun k => [k.edgesPaired]) = true ∧
    parse.featTableOk run.cells study.SUM_4C4E_SLICE 4 4 2 (fun k => [k.edgesPaired, b2n k.sameSlice]) = true ∧
    parse.featTableOk run.cells study.SUM_4C4E_BARS 4 4 2 (fun k => [k.pairs, k.edgesPaired]) = true ∧
    parse.featTableOk run.cells study.SUM_4C2E_P2S 4 2 1 (fun k => [2 * k.pairs + k.side]) = true ∧
    parse.featTableOk run.cells study.SUM_7C8E_PAIRS 7 8 1 (fun k => [k.pairs]) = true ∧
    parse.featTableOk run.cells study.SUM_2C2E 2 2 2 (fun k => [k.edgesPaired, b2n k.jzp]) = true := by
  native_decide

/-- The one printed digit that is off: SUMMARY section 1 prints the 2c2e mean as 6.880; the exact mean is
12328/1792 = 6.87946…, which rounds to 6.879 (6.880 is variants_by_drm.tsv's 6.8795 rounded again). -/
theorem summary_2c2e_mean :
    parse.plainMean "2c2e" = "6.880" ∧ weighted (total (drm run.cells 2 2)) = 12328 ∧
    parse.roundsTo 12328 1792 "6.880" = false ∧ parse.roundsTo 12328 1792 "6.879" = true ∧
    parse.roundsTo 12328 1792 "6.8795" = true := by
  native_decide

end EOSwitch
