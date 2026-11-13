## Appendix A: full tables

**Every checklist, budget 2**: one row per route, per subset × edges the first eight routes in greedy order, the cumulative share of DRs where the routes so far find an optimal finish, and where the same routes find a finish within +1 (same HTR budget). Sampled, {= n(25000) =} per subset × edges.

{{checklist_full}}

**Edge-path checklists, computer only**: per subset × edges, the budget-2 checklist built over routes read with the bad-edge count at every step (section 4), against the corner-only one. An answer key, not a list to check in an attempt. Sampled, {= n(25000) =} per subset × edges. First the corner-only checklist: each row is a subset × edges, each cell the share where the first 1, 2, 3 or 5 corner routes find the optimal:

{{edge_refined}}

The edge-path checklist, same rows: the share after 1, 2, 3 and 5 edge paths, the first edge path, and how many edge paths it takes to find what the first corner-only route finds:

{{edge_refined_paths}}

**Edge counts along the route**, per starting subset × edges (section 4), one table per intermediate subset. Each row is a starting subset × edges whose optimal (budget 2) can pass the intermediate subset: the share that can pass it at all, then the share that can pass it with each edge count (one DR can pass with several, so they add up to more; shares under 0.5% left out, starting cells under 0.5% not listed; 4a3 and 4b3 together as 4c3).

Through 4b2, one row per starting subset × edges:

{{edge_via_4b2}}

Through 2c3, same columns:

{{edge_via_2c3}}

Through 4a1, same columns:

{{edge_via_4a1}}

Through 4a2, same columns:

{{edge_via_4a2}}

Through 4c3 (4a3 or 4b3), same columns:

{{edge_via_4c3}}

**Checklists with no HTR limit**, first four routes, one row per route with the cumulative share finding the optimal. With no limit the routes overlap so much that these lists tell you more about which readings exist than about what to try:

{{checklist_nolimit}}

**rodneykinney's table** for FakeMMAP's bound: per subset × edges and target M, "reduce to 1q in at most R moves" with nothing read off the DR (A, B and C the subset's shortest linear HTR, worst case over the subset's corner paths). Each row is a subset × edges and a target M; the three columns are reduction lengths in moves: the formula of FakeMMAP's message without its first term, the exact model of section 9 (*computer only*), and the longest reduction any sampled finish of at most M needed. Sampled, {= n(25000) =} per subset × edges; a blank row means no sampled finish reaches that M.

{{rodney_table}}

**Late switches**: share of DRs whose shortest HTR among all readings of all optimal finishes is reached only by readings that switch after 3 or more moves, or after 4 or more (sampled, 25,000 per subset × edges, edges pooled by size), one row per corner subset:

{{late_switch}}

## Appendix B: how it was computed, and what checks it

**The model.**

- The DR group ⟨U, D, R2, L2, F2, B2⟩ with the first study's exact table of the optimal finish of all 19,508,428,800 DR states (proved in Lean there) and of the optimal leave-slice.
- Subsets are the first study's 48 (corner subset from the bad corners, the quarter turns the corners need and the 4a/4b shape; bad edges counted up to turning a layer).
- A Rust tool samples states uniformly within each subset × edges and enumerates every finish of the optimal length and one longer (both orders of commuting moves), using the exact table to prune. Each finish is read at every split, either side first, and its route, HTR length and quarter-turn counts recorded.
- Shortest HTRs (normal, inverse, NISS) come from an exact search. Reductions are counted from coset tables.
- Fixed targets of 10 to 12 use finishes up to max(optimal + 1, min(optimal + 2, 12)) moves.
- About an hour on four cores, at most 5 GB per job.

**What checks it.**

- The optimal distribution of every subset equals the first study's and Joba's in all {= E['cells473'] =} cells; DougCube's 663,552 HTR states give mean 10.13432557 exactly; Joba's DR-to-HTR lengths per subset agree.
- An independent sticker model (a 54-sticker cube built from geometry, with its own subset labels, HTR test and NISS reading) re-reads every optimal finish of 1,240 states (1,000 random DR scrambles and 5 per subset × edges from the sample): every finish replayed, every route and HTR length of every reading equal to the tool's. nissy 2.0.8 lists the same optimal finishes for all 1,240.
- Reduction counts from the coset tables equal a brute-force enumeration of every pair of sequences for reductions of up to 5 moves on 4,800 states (the first 100 of every subset × edges), and up to 7 moves on 40 states of 0c0 (the brute force for 7 moves was stopped there), which is why counts for 7 moves are not reported. Which reductions find the optimal comes from an exact search, not from the counts.
- The leave-slice maximum of 4a1 4e (15) is a count over the first study's exact leave-slice table, every state.
- A Lean 4 certificate in the study's folder recomputes the small exact tables from its own cube model and proves they equal the study's: the 663,552 HTR states, the corner quarter-turn counts and subsets of all 40,320 corner arrangements, the shortest linear HTR of every subset (all 29,400 HTR cosets), FakeMMAP's $\alpha$ for every corner path used, the *5/6 fake* count, the bare-qt reductions of 3qt and 4qt cases, and the 2qt(a)/(b) labels of Aedan Bryant's and the *Extra Quarter-Turn Stats* sheets from their own example triggers.
- Every move sequence in this write-up, the errata and the worked examples is replayed on the sticker model (the examples page states its count).

**Formally verified.** Two Lean 4 libraries in the study's folder, no Mathlib, no `sorry`. What they prove for this study:

- *HTRRoutes* (lean/HTRRoutes): the small exact tables, as in the bullet above.
- *FakeBound* (lean/FakeBound/FakeBound), FakeMMAP's bound as arithmetic for every N:
  - Finish.lean: each of the five terms is an upper bound on the reduction a finish needs, with term 2 as derived and $\alpha_{i+1}$ (`term1_sound` … `term5_sound`, `cover_sum`, `chain_bound`); the multi-qt lower bounds with $\alpha_{i+1}$ (`lower_stupid`, `lower_free`, `lower_A`, `lower_B`, `lower_C`).
  - Formula.lean: the smallest term is sound (`Rmin_sound`) and so is the largest, the formula as written (`Rmax_sound`).
  - Counter.lean: the counterexamples to the printed forms (`printed_term2_fails`, `literal_min_fails`, `witness_0c3`, `alpha_i_fails`), that the smallest term isn't always the exact worst case (`Rmin_not_tight`), and where C goes (`C_placement`).
  - Subset.lean, on the cube: half turns keep the subset × bad edges (`half_turns_keep_subset_data`, `labels_keep`), FakeMMAP's $C = 5$ and 6 (`fake_C_examples`), and $\alpha$ of the two counterexample paths (`counter_alphas`).
- *Corrections* (lean/FakeBound/Corrections/Examples.lean), the errata examples: the optimal finish of every DR state in a, c, d, e and f (`dr_optima_correct`, from the first study's proved table) and the printed finishes of a, d and f (`dr_solutions_valid`); the HTR lengths and printed HTRs of b and c (`htr_4c4`, `htr_13`); the subset names of a, d, e and f (`labels_htr_routes`); f's index example end to end (`index_example`, `index_example_arith`) and the C example (`C_example`). Each errata item says how much of its example is Lean-checked.

**Computed, not proved**: every share and mean from the samples ({= n(25000) =} states per subset × edges, 4,000 for bounding), the exact model of section 9 (an enumeration in Python), the shortest NISS HTRs (the Rust tool's search, cross-checked with nissy), which finishes are optimal and how they read (the Rust tool, cross-checked on the sticker model and with nissy), the reduction counts, and the means over the first study's exact table, such as the gain from the last DR move.

## Docs referred to

- Levi Gibson, [*allcases*](https://docs.google.com/spreadsheets/d/1Vo6XzCFtJ-HEAuaBmk_pac-sJ3TbxEBb7BKsRJ_2wpA), [*Extra Quarter-Turn Stats (By HTR Subset)*](https://docs.google.com/spreadsheets/d/1fPCjS1ZQlP_Munut9MQkSbsL3CEdtT3LC5h3R8OMHGw), [*DR Bounding*](https://docs.google.com/document/d/1q7rig4GEo26GunBMtuagZdGyzyjCGlduH84CHLpGLSA).
- Aedan Bryant, [*HTR Subset Stats*](https://docs.google.com/spreadsheets/d/17iChOoeB205t3wHTXMLrjM9si2vtxRgFeYR2z3pn1i0).
- rodneykinney, [*DR Finish Move Counts*](https://docs.google.com/spreadsheets/d/1tv8rwo2GF9IWuywFTnde_YlikIPBQvHqW9pysNG6BPM) and [*Advanced DR Bounding [Beta]*](https://docs.google.com/document/d/13F8HonrKJyHjU9EwfiHDRyY4X77vPriYeaVSrh5guq0).
- DougCube, [*Tables of Distinct Positions*](https://docs.google.com/spreadsheets/d/1p5goyNTGe_rlIqVslV4bJJzHNmKETUlrU-ndj9EIWAo).
- Yura Riabov, [*Hitchhiker’s Guide to HTR*](https://docs.google.com/document/d/1_NMlyPh2Ifd1E0ivos-15Sp-by-KPxoOsj9JD4pJuHI).
- Joba's exact optimal distribution per subset: a text file posted in #fmc-theory ([[T9115]]).
- My first study, [*Judging a DR by hand*](../judging-a-dr/).
- nissy 2.0.8, by Sebastiano Tronto ([nissy.tronto.net](https://nissy.tronto.net)), used for the cross-checks.
