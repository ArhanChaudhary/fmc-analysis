# FakeBound: a Lean 4 check of FakeMMAP's reduction bound, and of the corrections' examples

Lean 4.35.0, no Mathlib, no `sorry`. Two libraries:

- **FakeBound**: FakeMMAP's bound on the length of reductions to 1q (Discord #fmc-theory, 8 Apr 2026, KB messages T11501–T11504), as arithmetic for every N, plus the cube facts it uses (on HTRRoutes' sticker model).
- **Corrections**: the examples of the published corrections (`report/BUGS.md` of each study) whose lengths come from tables that a Lean certificate already proves (DRBound, HTRRoutes, EOSwitch, EODR).

## The model (from FakeMMAP's text)

A finish with N quarter turns is s_0 Q_1 s_1 … Q_N s_N, with sections of half turns of lengths s_j ≥ α_j. Its length is L = N + Σ s_j. Window i (i = 0 … N−1) keeps Q_{i+1} with sections i and i+1 as the 1q finish, so its reduction has length L − 1 − s_i − s_{i+1}. Term 1 ("M − α_i − α_{i+1} − 1") fixes this indexing. The hypotheses are:

- A ≤ L − s_N (normal HTR)
- B ≤ L − s_0 (inverse HTR)
- C ≤ L − s_0 − s_N, for N ≥ 3: the middle block Q_1 … Q_N solves s_N·X·s_0, a state of the same HTR subset (Part 2), so it is a linear HTR of the subset.

## What is proved

| Theorem | File | It says |
|---|---|---|
| `cover_sum` | Finish | For FakeMMAP's sets S (`Chain m lo hi`), the windows of S cover sections lo … hi+1 once, plus once more for each edge (i, i+1 ∈ S): the twice-covered section is **i+1**. |
| `chain_bound` | Finish | If every reduction is ≥ t: \|S\|·t ≤ \|S\|(L−1) − Σ_{lo..hi+1} s − Σ_edges α_{i+1}. |
| `term1_sound` … `term5_sound` | Finish | Each of T11502's five terms is an upper bound on every finish's shortest reduction (term 2 with the derived signs, all with α_{i+1}). This holds for every N. |
| `lower_stupid`, `lower_free`, `lower_A`, `lower_B`, `lower_C` | Finish | T11503's lower bounds, with α_{i+1}. |
| `Rmin_sound` | Formula | R = the **minimum** of all the terms over all the sets S (computable `Rmin`) is ≥ the shortest reduction of every finish satisfying the hypotheses. |
| `Rmax_sound` | Formula | R = the **maximum** (T11502's word), with any signs and any α index, is sound too, but only because term 1 is among the terms. |
| `printed_term2_fails`, `…_any_ABC`, `…_small`, `witness_0c3`, `literal_min_fails` | Counter | Min reading with T11502's printed signs in term 2 is too short: path 4a1 > 0c0 > 4a1 > 0c0, s = 0,3,0,4, M = 10, it gives 4, while 5 is needed. The 0c3 witness (α = 0,3,3,0, s = 2,3,3,3, M = 14) gives 6, while 7 is needed. |
| `alpha_i_fails`, `…_any_ABC` | Counter | With α_i (as printed) the min reading and T11503 both fail: path 4b2 > 4a3 > 4b2 > 4a1 > 0c0, s = 2,1,3,1,3, M = 14. R = 8 while 9 is needed, and T11503 claims 28 ≥ 29. |
| `Rmin_not_tight` | Counter | The minimum of the terms is not always the exact worst case: N = 3, α = 0, M = 5, A = B = 5, C = 0 gives R = 3, but every allowed finish has a reduction of at most 2. The terms never use A and B together. |
| `C_placement` | Counter | "L − s_0 − s_N ≥ C" and "L − s_j ≥ C" for a middle j are different statements: neither implies the other. |
| `half_turns_keep_subset_data`, `labels_keep` | Subset | Over all 40,320 corner and 40,320 U/D-edge arrangements and the six half turns, applied before or after: the bad-corner and qt counts, the shape, the 14-name subset, the bad-edge count, and both subset names (`label48`, `label`) are unchanged. |
| `fake_C_examples` | Subset | C(2c3 2e) = 5 and C(4b2 0e) = 6, FakeMMAP's examples. |
| `counter_alphas` | Subset | α of the two paths used above, computed from the cube. |
| `dr_optima_correct` | Corrections | The 16 DR-finish optima in judging-a-dr B2/B4/B5 and htr-routes a/c/d/e/f are exact (labels as in the Lean files: "d" is the late-switch example, now in the write-up's section 11; "e" and "f" are errata d and e on the page) (DRBound's `exact_optimal`). |
| `dr_solutions_valid` | Corrections | The 5 printed optimal finishes solve their states, with the stated lengths. |
| `htr_13`, `htr_4c4`, `labels_judging`, `labels_htr_routes`, `C_example` | Corrections | HTR lengths (shortest linear, from HTRRoutes' coset BFS), validity of the printed linear and NISS HTRs, and the subset names in judging-a-dr A1/B1/B2/B4/B5 and htr-routes a–f. |
| `index_example`, `index_example_arith` | Corrections | htr-routes f end to end: corner path, α = 0,1,3,1,0, sections 2,1,3,1,3, reductions 10,9,9,9; T11503 with α_i claims 28 ≥ 29. |
| `any_move_solutions_valid`, `arith_B3` | Corrections | judging-a-dr A2/A3: the any-move solutions are valid (the optima themselves are not checked). B3: 24⁴/12 = 27648. |
| `eo_switch_examples`, `arm_sets` | Corrections | eo-switch a/b/c: features and EO-kept distance to DR, plus the printed DRs. The list of the shortest case for each ARM set: 11 sets sub-6 and 7 sub-5. |
| `eo_to_dr_examples`, `superflip` | Corrections | eo-to-dr 1/3: distances 10 and 8 and the printed DRs, checked after a whole-cube rotation. eo-to-dr 2: the superflip has 12 bad edges on every axis (so 7 to EO linearly, by EODR's `eo_by_bad`), and the printed NISS EO is valid. |

Parts 1 (Finish, Formula, Counter) use only `decide` and Lean's standard axioms. Subset and Corrections use `native_decide` (`FakeBound/Audit.lean` lists the axioms).

## Build

    source /data/fmc/env.sh
    cd /data/fmc/htr-routes/lean/FakeBound
    systemd-run --user --scope -q -p MemoryMax=4G lake build              # FakeBound
    systemd-run --user --scope -q -p MemoryMax=4G lake build Corrections  # needs DRBound's exact table (built already there)

`dr_table_lookup` (in `Corrections/DRTable.lean`, kept apart so it is built once) rebuilds DRBound's 1.34-billion-entry table (`Exact.tableValues 18`). On the 4-core VM this took 392 s and about 2.6 GB at peak. The rest:

- Finish, Formula and Counter: about 3 s together.
- Subset: 53 s.
- Corrections.Examples: 62 s.
- Rebuilding both libraries without the table: 190 s wall, 2.6 GB peak.

The first build of Corrections also rebuilt DRBound's `Certified`/`Examples` modules (artifacts only): about 8 minutes.
