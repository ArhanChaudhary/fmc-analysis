## Appendix A: full tables

**Every checklist, budget 2**: per subset × edges, the first eight routes in greedy order, the cumulative share of DRs where the routes so far find an optimal finish, and where the same routes find a finish within +1 (same HTR budget). Sampled, {= n(25000) =} per subset × edges.

{{checklist_full}}

**Checklists with no HTR limit**, first four routes. With no limit the routes overlap so much that these lists say more about which readings exist than what to try:

{{checklist_nolimit}}

**The path sheets' top paths.** Per tab, the path with the largest share in *Optimal Niss-HTR Paths* and in *Sub-13 Optimal Niss-HTR Paths*, the sheet's share and mine (same counting rule, section 5):

{{docs_top}}

**rodneykinney's table** for FakeMMAP's bound: per subset × edges and target M, "reduce to 1q in at most R moves" with nothing read off the DR (A and B the subset's shortest linear HTR, worst case over the subset's corner paths): the formula of FakeMMAP's message without its first term (C the subset's shortest linear HTR) / the exact model (C the shortest NISS HTR) / the longest reduction any sampled finish of at most M needed. Sampled, {= n(25000) =} per subset × edges; a blank cell means no sampled finish reaches that M.

{{rodney_table}}

**Late switches**: share of DRs whose shortest HTR among all readings of all optimal finishes is reached only by readings that switch after 3 or more moves, or after 4 or more (sampled, 25,000 per subset × edges, edges pooled by size):

{{late_switch}}

## Appendix B: how it was computed, and what checks it

**The model.** The DR group ⟨U, D, R2, L2, F2, B2⟩ with the first study's exact table of the optimal finish of all 19,508,428,800 DR states (proved in Lean there) and of the optimal leave-slice. Subsets are the first study's 48 (corner subset from the bad corners, the quarter turns the corners need and the 4a/4b shape; bad edges counted up to turning a layer). A Rust tool samples states uniformly within each subset × edges and enumerates every finish of the optimal length and one longer (both orders of commuting moves), using the exact table to prune; each finish is read at every split, either side first, and its route, HTR length and quarter-turn counts recorded. Shortest HTRs (normal, inverse, NISS) come from an exact search. Reductions are counted from coset tables. About an hour on four cores, at most 5 GB per job. Fixed targets of 10 to 12 use finishes up to max(optimal + 1, min(optimal + 2, 12)) moves.

**What checks it.**

- The optimal distribution of every subset equals the first study's and Joba's in all {= E['cells473'] =} cells; DougCube's 663,552 HTR states give mean 10.13432557 exactly; Joba's DR-to-HTR lengths per subset agree.
- An independent sticker model (a 54-sticker cube built from geometry, with its own subset labels, HTR test and NISS reading) re-reads every optimal finish of 1,240 states (1,000 random DR scrambles and 5 per subset × edges from the sample): every finish replayed, every route and HTR length of every reading equal to the tool's. nissy 2.0.8 lists the same optimal finishes for all 1,240.
- Reduction counts from the coset tables equal a brute-force enumeration of every pair of sequences for reductions of up to 5 moves on 4,800 states (the first 100 of every subset × edges), and up to 7 moves on 40 states of 0c0 (the brute force for 7 moves was stopped there), which is why counts for 7 moves are not reported. Which reductions find the optimal comes from an exact search, not from the counts.
- The leave-slice maximum of 4a1 4e (15) is a count over the first study's exact leave-slice table, every state.
- A Lean 4 certificate in the study's folder recomputes the small exact tables from its own cube model and proves they equal the study's: the 663,552 HTR states, the corner quarter-turn counts and subsets of all 40,320 corner arrangements, the shortest linear HTR of every subset (all 29,400 HTR cosets), FakeMMAP's α for every corner path used, the *5/6 fake* count, the bare-qt reductions of 3qt and 4qt cases, and the 2qt(a)/(b) labels of Aedan Bryant's and the *Extra Quarter-Turn Stats* sheets from their own example triggers.
- Every move sequence in this write-up, the errata and the worked examples is replayed on the sticker model (the examples page states its count).

## Docs referred to

- [*Sub-13 Optimal Niss-HTR Paths*](https://docs.google.com/spreadsheets/d/1etiCnl6U-OHQAjEZIVIlk9iE64OXK3lrCyy14TLE_wE), forwarded by Daichi; [*Optimal Niss-HTR Paths*](https://docs.google.com/spreadsheets/d/1D4qUhLOsJrwsBEzUVfmnLikuQNNB_eSZiPq-nS8KPN4), posted by deven. The maker of the data is not stated.
- Levi Gibson, [*allcases*](https://docs.google.com/spreadsheets/d/1Vo6XzCFtJ-HEAuaBmk_pac-sJ3TbxEBb7BKsRJ_2wpA), [*Extra Quarter-Turn Stats (By HTR Subset)*](https://docs.google.com/spreadsheets/d/1fPCjS1ZQlP_Munut9MQkSbsL3CEdtT3LC5h3R8OMHGw), [*DR Bounding*](https://docs.google.com/document/d/1q7rig4GEo26GunBMtuagZdGyzyjCGlduH84CHLpGLSA).
- Aedan Bryant, [*HTR Subset Stats*](https://docs.google.com/spreadsheets/d/17iChOoeB205t3wHTXMLrjM9si2vtxRgFeYR2z3pn1i0).
- rodneykinney, [*DR Finish Move Counts*](https://docs.google.com/spreadsheets/d/1tv8rwo2GF9IWuywFTnde_YlikIPBQvHqW9pysNG6BPM) and [*Advanced DR Bounding [Beta]*](https://docs.google.com/document/d/13F8HonrKJyHjU9EwfiHDRyY4X77vPriYeaVSrh5guq0).
- DougCube, [*Tables of Distinct Positions*](https://docs.google.com/spreadsheets/d/1p5goyNTGe_rlIqVslV4bJJzHNmKETUlrU-ndj9EIWAo).
- Yura Riabov, [*Hitchhiker’s Guide to HTR*](https://docs.google.com/document/d/1_NMlyPh2Ifd1E0ivos-15Sp-by-KPxoOsj9JD4pJuHI).
- Joba's exact optimal distribution per subset: a text file posted in #fmc-theory ([[T9115]]).
- My first study, [*Judging a DR by hand*](../judging-a-dr/).
- nissy 2.0.8, by Sebastiano Tronto ([nissy.tronto.net](https://nissy.tronto.net)), used for the cross-checks.
