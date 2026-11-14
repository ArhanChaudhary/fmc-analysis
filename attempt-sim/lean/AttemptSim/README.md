# AttemptSim — a Lean 4 certificate for the attempt simulator

Lean 4.35.0, no Mathlib, no `sorry`; about 2,100 lines plus judging-a-dr's two DRBound files (260 lines, copied
unchanged) and the generated data. 56 theorems. It checks the parts of the simulator (`research/attemptsim`) that a reader has to
trust for the numbers to mean anything: that its cube is the cube, that the tables its search prunes and judges with
are exact, that the candidate lists the simulated solver picks from are complete, that its DR moves are the ones
judging-a-dr's exact table is about, and that a fixed sample of simulated attempts (several policies) does what the
log says: every solution solves its scramble in the stated length, the clock is the sum of the step costs, and the
result is the shortest solution found before the last writing that ended in time began. The statistics of the study
are over many more attempts than the sample and stay **sampled**: Lean checks individual attempts, not averages.

## What is proved

Moves are numbers 0 … 17 (3 · face + quarter turns − 1, faces U D R L F B); the sticker cube is the one of the
earlier studies (built from geometry, nothing typed by hand). "Checked by running" means the statement is a closed
Boolean computation run as compiled code and accepted through `native_decide`.

| Theorem (file) | Statement |
|---|---|
| `perm.run_invert`, `perm.solved_rotate`, `perm.niss_convention`, `perm.cancel_run`, `perm.cancel_solves`, `perm.written_solution` (`Perm.lean`) | For **every** sequence (kernel-checked induction): a sequence and its inverse undo each other; if A B does nothing, B A does nothing; the NISS convention `I⁻¹ S N` solved ⇔ `N ++ invert I` solves S; `cancel` (the HTM form) never changes what a sequence does; so the written solution `cancel (N ++ invert I)` solves S exactly when `I⁻¹ S N` is solved. |
| `sticker_model`, `turn_directions` (`ModelThm.lean`) | 54 different stickers; the 18 turns are permutations with the usual names and directions; X2 = X X, X' = X X X; R U R' U' has order 6, R U2 D' B D' order 1260. |
| `model_shape`, `moves_match` | data/model.txt (the simulator's own dump) has 18 move tables, 24 rotations, 3 EO and 6 DR views; **each move table is the one read off the sticker turn**, twists and flips included. |
| `cubie_follows_stickers`, `then_inverse_follow`, `compose_is_concatenation`, `run_is_apply`, `conj_follows` | The simulator's piece model, its composition, inverse (used for NISS) and change of view agree with the sticker cube (on every state within 3 turns, every pair within 2, every sequence of up to 4). |
| `rotations_match`, `views_ok`, `views_read_axes`, `dr_numbering` | The 24 rotations are the cube's; the nine views put the EO axis on F/B and the DR axis on U/D and rename moves correctly; what a view reads as EO or DR is EO or DR on the real axes; the DR tables' place numbering (`drmap`) is UFR … DBR, UF … DR, FR … BR; the 14 EO-keeping turns are exactly the turns that flip nothing. |
| `cancel_shape` | On all 2,000,719 sequences of up to 5 turns, `cancel` leaves no two turns of one face together (also across the opposite face), is idempotent and never lengthens. |
| `move_tables_match`, `coords_follow`, `coords_are_stickers` (`TablesThm.lean`) | The twist, flip and slice move tables are the model's, and the coordinates mean what they say (F/B EO, E-slice places). |
| `eodist_checked` | **EO distance**: each of the 2,048 entries is the fewest turns to F/B EO (checked entry by entry: 0 only at the goal, never more than one above a neighbour, one below some neighbour), histogram 1, 2, 25, 202, 620, 900, 285, 13. |
| `drdist_checked` | **EO-kept distance to DR**: each of the 1,082,565 entries is the fewest of the 14 EO-keeping turns to DR on U/D; histogram 1, 2, 17, 134, 1065, 8190, 54694, 267576, 560568, 187204, 3114 (Cale's table, also proved in the EO-switch certificate). |
| `dr_group`, `cosets_ok`, `htrdist_checked` | The ten DR moves on judging-a-dr's positions; the 420 HTR corner cosets and 70 edge patterns are judging-a-dr's; **fewest DR moves to HTR** of all 29,400 HTR cosets, longest 13. |
| `drlink.dr_moves_are_drbound` (`DRLink.lean`) | **The simulator's ten DR move tables are DRBound's** (`DRBound.Move.srcC/srcE/srcS`, judging-a-dr's model, copied unchanged): through `drmap`, each move sends the piece at the place of position src[p] to the place of p, with no twist or flip. |
| `drlink.dr_sequences_follow_drbound` | For all 11,111 sequences of at most 4 DR moves, the simulator's cube read through `drmap` is DRBound's `solved.apply w`. |
| `drlink.sticker_dr_moves_are_drbound` | The DR moves built from the 54-sticker turns (`tables.CT`, `ET`, and the E-slice positions) are DRBound's tables too. |
| `eo_candidates_complete`, `eo_candidates_are_eos` (`CompleteThm.lean`) | On 12 exported scrambles: the simulator's list of EOs of at most 4 turns (normal, inverse and NISS, three axes; 522 in all) is exactly the set found by trying every sequence on the sticker cube, and each listed EO is one. |
| `dr_candidates_complete`, `dr_candidates_are_drs`, `fast_tests_agree`, `candidate_files` | The same for the EO-first DRs of at most 9 turns through those EOs (164), DR read off the stickers. |
| `sample_counts` (`SampleThm.lean`) | The sample file has the generator's number of attempts, and per policy the same attempts, DNFs, total moves and solutions found (Lean's reading against Python's). |
| `sample_attempts_ok` | **Every sampled attempt passes `attemptOk`**: every solution found and the result solve the scramble, in HTM form, in the stated number of moves; solution and writing clocks sit at the ends of their steps; no examination starts after the hour; each writing writes the shortest solution found before it began; the result is the last writing that ended in the hour. |
| `sample_ledger` | **The time log sums to the reported time**: for every sampled attempt, the step costs add up to `t_end_ms`. |
| `sample_result_is_shortest` | **The result is the shortest solution found before the last in-time writing began**; a DNF exactly when no writing ended in the hour. |
| `sample_late_better_count` | How many sampled attempts found something shorter only after their last in-time writing began (Lean's count = the generator's). |
| `sample_results_solve` | Spelled out: each solved attempt has a solution X with `perm.solved (scramble ++ X)` and \|X\| = its length. |
| `page_solutions_ok` | Every solution printed on the page (data/lean_page_solutions.tsv, if the write-up lists any) solves its scramble in the stated length. |

`AttemptSim/Audit.lean` prints the axioms of every theorem above (`lake env lean AttemptSim/Audit.lean`).

## Why to believe it

- **What runs.** Most statements are closed Boolean computations accepted by `native_decide`: the compiled code ran
  and returned `true`. That trusts the Lean compiler and the runtime on top of the kernel; `Audit.lean` lists one
  `_native` axiom per such run and no other axiom besides `propext`, `Classical.choice`, `Quot.sound`. The general
  facts about sequences (`Perm.lean`) are kernel proofs for sequences of any length.
- **What the data is.** Everything in `data/` is written by the simulator itself (`attemptsim export`, `attemptsim run
  --log`) and copied by `gen.py` byte for byte (drdist one letter per byte); sizes and sha256 are in `data/MANIFEST.txt`
  and in `manifest.FILES` / `manifest.SAMPLE_FILES`. The tables are not trusted: each distance table is checked entry by
  entry with a rule that makes every entry the exact distance whatever program wrote it.
- **Copied Lean files.** `DRBound/Certificate.lean` and `DRBound/Cube.lean` are judging-a-dr's files, byte for byte
  (gen.py stops if they differ; sha256 in `manifest.VENDORED`). `AttemptSim/Cube.lean`, `Pieces.lean` and `Search.lean`
  are the EO-switch certificate's with the namespace renamed (gen.py checks all three below their header comment).
- **The exact table.** The simulator bounds its finish search with judging-a-dr's exact optimal-finish table
  `lean_exact_table.u8` (1,339,269,120 bytes, sha256 `26cc1c0a7a7fe124934d0d9c44ff8d4d086a449ccde140e58808958d9a5e1fe0`,
  the same on this VM, on fmc2 and on fmc3; `manifest.EXACT_SHA256`, written by refresh.sh from the file the sample run
  read). That file was written by an `#eval` of `DRBound.Exact.mkTable 18`, the table DRBound proves exact for every
  legal DR state (`exact_checked`, `exact_optimal`; judging-a-dr/research/src/check_lean_exact.py also compares it
  entry by entry with that study's Rust BFS). This project does not re-prove the 1.3 GB table; the hash ties the file
  to that proof, and `DRLink.lean` ties the simulator's DR moves to DRBound's model. Nothing reported depends on the
  table for correctness: every solution is replayed (`sample_attempts_ok`); the table only decides how far the
  finish search looks (optimal + 2) and gives the computer-only answer key.

## Not proved here

- **The policy logic** (when the simulated solver writes EOs, works RZPs, finishes DRs, writes a solution) and
  whether it is a good model of a human. Lean checks what the logs say happened, not why.
- **The time costs and the human-limit model** (`research/costs.toml`): inputs, not facts.
- **The statistics** (means, shares, standard errors, the policy comparisons): computed over thousands of attempts by
  the simulator and Python; only the sample is checked. They stay "sampled".
- **The route tables beyond replay**: which finishes a route to HTR finds is computed by htr-routes' code; Lean only
  replays the finishes that end up in solutions.
- **`dist48.tsv` and `checklist.tsv`** (from htr-routes: the optimal-finish distribution per subset, the route
  checklists): used by the simulated solver to judge DRs and order routes, not checked here.
- **The candidate lists beyond the 12 scrambles and caps** (EO ≤ 4, DR ≤ 9) of `CompleteThm`: the simulator runs with
  EO ≤ 5 and DR ≤ 11; the same code, checked on the smaller caps.

## Build

On fmc2 (`export PATH=/data/disk/elan/bin:$PATH ELAN_HOME=/data/disk/elan`), in the project folder:

    lake build AttemptSim AttemptSim.Audit
    lake env lean AttemptSim/Audit.lean        # prints the axioms

Measured on fmc2 (8 cores, busy with other jobs) with `/usr/bin/time -v`, 13 Nov 2026:

| Build | Wall time | Peak memory | Note |
|---|---|---|---|
| Everything from scratch | 5 min 44 s | 0.58 GB | `CompleteThm` is 5 min 26 s of it (the brute-force enumeration of the candidate lists); `ModelThm` 10 s, `TablesThm` 9 s, the rest a few seconds each |
| New sample only (refresh.sh, 3 policies × 67 scrambles = 201 attempts, 50,486 logged steps, 660 KB) | 12 s for the whole script | 0.53 GB | `Sample` 0.7 s, `SampleThm` 0.7 s, `Audit` 2 s; the parse and the checks run as compiled code, so a few hundred attempts cost nothing |

Then `python3 check_build.py` (refresh.sh runs it) checks that the data files on disk are the ones in
`data/MANIFEST.txt`, that the axioms are only `propext`, `Classical.choice`, `Quot.sound` and one `native_decide` axiom
per checked run (53 of the 56 theorems use one), and that no source contains `sorry`.

**Lake does not track `include_str` files.** A module is rebuilt when a file it imports changes; every module that
embeds data imports a manifest carrying the data's sha256 (`Manifest.lean` for the tables, `SampleManifest.lean` for
the sample), so data written through `gen.py` always rebuilds what embeds it. Data copied in by hand would not:
always go through `gen.py` (or refresh.sh), and `check_build.py` catches a mismatch between the data on disk and the
manifests. A negative test (one step cost of the sample changed by 1 ms, manifest hash changed) fails
`sample_attempts_ok` and `sample_ledger`, as it should.

## Refresh the data

    lean/AttemptSim/refresh.sh POLICYFILE NSCR [--no-build]

runs every policy of POLICYFILE on the NSCR held-out scrambles 4000 … 4000 + NSCR − 1 of
`research/data/scrambles_uniform.txt` with full logs (`research/out/lean_sample.jsonl`), re-exports the model and
tables (`research/out/lean_export`), records the exact table's sha256, runs `gen.py`, copies the project to fmc2,
builds it there and prints the axiom summary. It needs the static simulator build
(`research/attemptsim/target/x86_64-unknown-linux-musl/release/attemptsim`), the exact table (`EXACT=`, default
judging-a-dr's), python3 and the ssh alias fmc2. The tables go into `Manifest.lean` and the sample into
`SampleManifest.lean`, so a new sample rebuilds only Sample, SampleThm and Audit.

## Files

| File | Content |
|---|---|
| `AttemptSim/Cube.lean`, `Pieces.lean`, `Search.lean` | The sticker cube, EO / twist / E-slice read off stickers, the table checker (from the EO-switch certificate). |
| `AttemptSim/Perm.lean` | Sequences as permutations; NISS convention; `cancel` and its proofs. |
| `AttemptSim/Cubie.lean` | The simulator's piece model (vendor/cubie.rs line for line) and data/model.txt. |
| `AttemptSim/ModelThm.lean` | Part A: the model is the cube. |
| `AttemptSim/Tables.lean`, `TablesThm.lean` | Part B: the coordinate tables, EO and DR distances, HTR cosets and distances. |
| `AttemptSim/Complete.lean`, `CompleteThm.lean` | Part D: the candidate lists, by brute force on the stickers. |
| `AttemptSim/Sample.lean`, `SampleThm.lean` | Parts C and E: the sampled attempts. |
| `AttemptSim/DRLink.lean`, `DRBound/*.lean` | Part F: the DR moves are judging-a-dr's (DRBound's files copied unchanged). |
| `AttemptSim/Manifest.lean`, `SampleManifest.lean` | Generated by `gen.py`: hashes and counts. |
| `AttemptSim/Audit.lean` | `#print axioms` for every theorem. |
| `gen.py`, `refresh.sh`, `check_build.py`, `data/` | Generator, refresh script, post-build check, embedded data (`data/MANIFEST.txt`). |
