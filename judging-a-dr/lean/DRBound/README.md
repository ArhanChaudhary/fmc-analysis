# DRBound — a Lean 4 certificate for lower bounds on domino-reduction finishes, and for their exact optimal length

Lean 4.35.0, no Mathlib. About 2,500 lines, no `sorry`, plus 200 lines of checks of the published page and a generated list of its examples.

## What is proved

For the cube after domino reduction (DR on U/D), with the ten moves U U2 U' D D2 D' R2 L2 F2 B2 each counted as one:

| Theorem | Statement |
|---|---|
| `solution_length_ge` (`Certificate.lean`) | Abstract: if features commute with moves and a table changes by at most 1 per move and is 0 at the solved state, every solution of `s` has at least `T (feat s)` moves. |
| `Rung.lower_bound` (`Theorems.lean`) | For a checked rung `R`, every legal state `g` and every move list `w` with `g.apply w = solved`: `R.bound g ≤ w.length`. |
| `Rung.lower_bound_inverse` | The same with the bound read from the inverse state of `g`. |
| `Rung.bound_attained` | `R.bound g` moves suffice to make `g` look solved through `R` (the table is exact for what `R` sees). |
| `Rung.half_lower_bound` | Half-turn-only version. |
| `corner_length_bound`, `corner_parity_bound`, `htr_length_bound`, `cbadp_bound`, `cbadp_bound_inverse`, `kf_bound`, `kf_bound_inverse`, `kf_bound_attained`, `kf_half_bound`, `k0f_bound`, `k0f_bound_inverse` (`Certified.lean`) | The instances for the rungs `c`, `c+p`, `htr`, `c+bad+p`, `KF`, `K0+F`. |
| `fakemmap_classes`, `fakemmap_values`, `fakemmap_shorter_with_quarter_turns` | FakeMMAP's 216 listed cases are 216 distinct `KF` classes; each listed value equals the half-turn-only table; with quarter turns allowed exactly 2 get shorter. |
| `full_bound`, `full_bound_inverse`, `full_bound_attained` (`CertifiedFull.lean`) | The instances for the finest rung (406,425,600 classes). |
| `exact_lower`, `exact_attained`, `exact_optimal` (`CertifiedExact.lean`) | For every legal state `g` with consistent parities (`g.Valid`, `g.ParityOK`): every solution has at least `exactDist g` moves, and some solution has exactly `exactDist g` moves. `exactDist g` is the entry of `g`'s symmetry-reduced image in a table of 2768 × 40320 × 12 = 1,339,269,120 entries. |
| `reachable_good` | Every state reached from solved by DR moves is `Valid` and `ParityOK` (with `exact_attained`: these are exactly the states of the DR group). |
| `exact_le_18`, `exact_solvable_18`, `exact_needs_18` | No state needs more than 18 moves; some state needs 18 (`U2 L2 D B2 U' B2 U' L2 D B2 R2 U R2 U R2 U2 R2 U'`). |
| `exact_depth_counts`, `exactCounts_total` | The numbers of table entries with value 0 … 18, each entry weighted by 16 / (number of symmetries fixing its corner class representative), are 1, 10, 67, …, 1575608, 1352; they sum to 19,508,428,800. **Not proved:** that this weighted count is the number of states (orbit–stabiliser). |
| `page_optima_correct` (`PageChecks.lean`, table run in `PageTable.lean`) | Every DR state on the published write-up that comes with a stated optimal finish (198 statements about 167 different states: the typical DRs of section 6.3 and Appendix E, both columns of Appendix G, the setup + HTR examples of section 7, the code-block examples) has exactly that optimal (`exact_optimal`). The list, `PageData.lean`, is generated from `report/WRITEUP.md` by `research/src/gen_page_checks.py`. |
| `page_solves`, `page_htr`, `page_in_htr`, `page_levels` | The printed finishes solve their states in the stated length (20); the stated shortest HTR on normal and inverse is the HTR rung's value (55 states); the printed HTRs land in HTR; the stated levels (HTR, L, L with parity, L+S+T, NISS@DR, + H-perm parity) of Rodney's two examples, the corner length with parity of the 2c4 4e of section 6.5, and HTR and corner length 7 on both sides for errata B4's pair. |
| `rung_maxima` | Largest value of the six smaller rungs: 13, 13, 14, 15, 15, 16 (the seven-levels table); so the longest shortest DR → HTR is 13 (errata B1). |
| `niss_htr` | Errata B1, the NISS half: B1's two 0c3 4e states have a NISS HTR of 11; the 0c3 4e `B2 U B2 R2 D' L2 U B2 D' F2 D' L2 F2 U' R2 U` has none of 11 or less (`nissHTR5` = 12) and one of 12, so 11 is not the NISS maximum. Paper step, not in Lean: a NISS HTR of 11 or less has a side of at most 5 moves, and `nissHTR5` minimises over all such sides on the scramble and on its inverse. |

## Files

| File | Content |
|---|---|
| `DRBound/Certificate.lean` | The general lemma. Depends only on `propext` and `Quot.sound`. |
| `DRBound/Cube.lean` | Positions, the ten moves as explicit tables, states, legality, inverse states, enumeration of all 8-tuples. **This is the file to read to convince yourself the model is the cube.** |
| `DRBound/Search.lean` | Features ("codes"), class numbering, breadth-first search, and the checkers. Nothing here is assumed correct; it is only run. |
| `DRBound/Theorems.lean` | From the three exhaustive checks (`Rung.Checked`) to the theorems above. |
| `DRBound/FakeMMAPData.lean` | The 216 (scramble, value) pairs of Discord message T12061, generated mechanically from the attachment. |
| `DRBound/Certified.lean`, `DRBound/CertifiedFull.lean` | The checks, run by `native_decide`, and the resulting theorems. |
| `DRBound/Examples.lean` | `#eval` of the bounds on positions from the source documents; `levi_example_htr_lengths`, `levi_example_solved_in_7` (a 1qt state where Levi's formula gives 10 and the optimum is 7). |
| `DRBound/Audit.lean` | `#print axioms` for the main theorems. |
| `DRBound/Exact.lean` | Exact optimal length: the 16 symmetries fixing the U/D axis, corner classes, the reduced index, the search, the checkers, and all proofs from "the checks pass" to the theorems, for any table. Imports only `Cube` (and `Certificate`); has its own copies of `rank8` etc. in namespace `DRBound.Exact`, so edits to `Search.lean` do not rerun the long check. |
| `DRBound/CertifiedExactTable.lean` | Only the `native_decide` runs: nine model checks (seconds) and the one big run that builds the table, checks every entry against the ten moves and the stabiliser symmetries, checks the maximum, counts, and looks up the sample. **Editing this file or `Exact.lean`, comments included, reruns 17 minutes.** |
| `DRBound/CertifiedExact.lean` | `exactDist` and the theorems. |
| `DRBound/AuditExact.lean` | `#print axioms` for them. |
| `DRBound/PageData.lean` | Generated by `research/src/gen_page_checks.py` from the built write-up: every DR state with a stated length. Regenerate after the page changes. |
| `DRBound/PageTable.lean` | The one `Exact.tableValues 18` run over the page's states (rebuilds the exact table: 13.5 minutes on a busy 8-core machine, 1.9 GB). Also the strict move parser. |
| `DRBound/PageDefs.lean`, `DRBound/PageChecks.lean`, `DRBound/AuditPage.lean` | The NISS-HTR search, the page theorems, and `#print axioms` for them. |

## Build

    source /data/fmc/env.sh
    cd /data/fmc/judging-a-dr/lean/DRBound
    systemd-run --user --scope -q -p MemoryMax=3G lake build DRBound.CertifiedExactTable   # 17 minutes, 1.9 GB; run it on its own first
    systemd-run --user --scope -q -p MemoryMax=3G lake build DRBound.PageTable             # the page's examples: rebuilds the exact table, 13.5 minutes, 1.9 GB; on its own too
    systemd-run --user --scope -q -p MemoryMax=3G lake build     # the rest: about 10 minutes, under 3 GB, plus 2.5 minutes and 0.6 GB for PageChecks; prints the audits and the examples

From a clean tree a plain `lake build` may run the exact-table check (1.9 GB) next to `Certified`/`CertifiedFull` (about 0.9 GB) or next to `PageTable` (1.9 GB) and hit the cap, hence the separate steps.

The page checks (`PageData`, `PageTable`, `PageDefs`, `PageChecks`, `AuditPage`) were timed on an 8-core machine that was busy with other jobs: `PageTable` 806 s wall (511 s CPU), peak 1.87 GB; `PageChecks` 148 s, peak 0.56 GB. After the write-up is rebuilt, run `python3 research/src/gen_page_checks.py` (from anywhere): if `PageData.lean` changes, `PageTable` runs again; if only the prose changed it doesn't, because the list carries section names and no line numbers.

`lakefile.toml` sets `precompileModules = true`; without it the exhaustive checks would run in the interpreter and not finish.

## Trust

- Kernel-checked: the general lemma, and every step from the checks to the theorems.
- Run as compiled code and accepted through `native_decide` (one axiom per check, listed by `Audit.lean`): that all 8⁸ fillings of eight positions satisfy the feature/move-table agreement, that the E-slice parity behaves, and that every table entry satisfies the ±1 condition, the zero condition and the descent condition.
- For the exact table the same pattern: nine exhaustive checks of the symmetry bookkeeping over all arrangements of 8 and of 4 pieces, and one run over all 1,339,269,120 entries (`exact_checked`).
- Do not add `rfl`/`decide` proofs over `cclass`, `symTo`, `mkTable` or `ridx solved`: the kernel would try to evaluate the tables. `exactDist` is noncomputable on purpose; `Exact.tableValues 18 gs` is the evaluable version (it rebuilds the table, about 6 minutes).
- The page checks state exactly what is in `PageData.lean`: `page_optima_correct` is `exact_optimal` at each listed state; `page_htr`, `page_in_htr` and `page_levels` are values of the rung tables (`rungHTR` is the BFS distance to the HTR coset by `Rung.bound_attained`); `niss_htr` needs the paper step in its docstring. Subset names, corner cases and the setup + HTR bound of the listed states are not checked here (the errata's subset names are, in `htr-routes/lean/FakeBound/Corrections`).
- Not in Lean: the statistics over all DR states (they are counts over the proven optimal lengths, made by the Rust program; `research/src/check_lean_exact.py` compares its table with the Lean one entry by entry), the orbit–stabiliser step for the depth counts, and the all-move version of the 216 table. See `report/WRITEUP.md`.
