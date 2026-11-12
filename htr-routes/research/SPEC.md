# Which HTR routes to try from a DR: what to compute

Fifth case study for fmc.arhan.sh. The user picked it as the most-demanded open topic; a top solver "would be
surprised if you could find anything novel", so every result must say plainly what is new against what exists.

## Inputs
- What the server says: `/data/fmc/kb/reread/htr_theory_A.md`, `_B`, `_C`, `htr_discussion_1.md` … `_5`, and
  `htr_docs.md` (all quotes checked against the export). The demand evidence: `/data/fmc/kb/reread/idea_*.md`.
- The first study, `/data/fmc/judging-a-dr/` (README.md, research/drtools, research/data): exact optimal finish of all
  19,508,428,800 DR states (`research/data/drbfs`, `lean_exact_table.u8`), optimal leave slice from HTR
  (`ls_depth.u8`), subset/corner-case naming and the hand reads (`research/drtools/src/hand.rs`, `class.rs`). Use its
  conventions for subset names and say which name each doc uses where they conflict (2qt a/b; 4c5 vs 4b5).
- Model and checks: `/data/fmc/is-dr-xs-worth-it/research/src/cube.py` (sticker model), nissy for cross-checks.

## What already exists (credit it; the study is new only where it goes past these)
- **Optimal NISS-HTR path shares per subset**: "Sub-13 Optimal Niss-HTR Paths" (doc 396, forwarded by Daichi,
  2026-06-13) and "Optimal Niss-HTR Paths" (doc 410, deven): for each subset × edge count, the share of states whose
  optimal passes through each chain of corner subsets, NISS switches bracketed. Sample size, solver, E-slice and
  DR-breaking treatment not stated; shares do not add up (all distinct paths per state counted, D19661). Daichi's
  cheat sheet (image D18340) turns 396 into a per-subset checklist.
- beef beans' "allcases" (doc 171, linear paths, one optimal per state, ties ignored D8302), extra-QT sheets
  (docs 66, 9), Aedan Bryant's HTR Subset Stats (doc 15, 1000 states per subset: mean optimal vs shortest linear and
  NISS HTR), Joba's exact per-subset finish distribution (doc 580), docs 566/567 (DR→HTR optimal per subset),
  DougCube's 663,552-HTR-state distribution (mean 10.13), JTuu's 2c3 2e linear-vs-bounding sim (T5744: 64.65% /
  86.05%), trangium's HTR-length vs finish heat map (T11191, 20–100 samples per cell), rodneykinney's corner
  "normal forms" and Advanced DR Bounding, FakeMMAP's tables, Tom Nelson's DR Finish Move Counts.
- Hand checklists to grade: Zagros's 8-step 4b2 order ("optimal in 15 minutes like 80% of the time", D15884–D15885),
  Daichi's cheat sheet, Lewis Isom's 4a2 2e/0e list (T6743) and 2c3 extension list (T7116–T7118), Jay's 3qt 2c0e
  checks and rodneykinney's reductions (T328–T344), beef beans' bounding verdicts per subset (T7074), "4a3 is
  philosophically 5qt; go through 2c3" (T6390), Yura/rogo/Adri/Jay on 4b2 4e (D6409–D6439).
- Numbers people quote, to check: rodneykinney "57% … uses 4QT for a 2QT corner case" (T539); Lichi ">60% of optimals
  for 2qt(a) 4c4e use 4qt" (D2306, nissy first optimal only); "about 25% of 4c3 needs 5qt"; "4b2 0e optimal goes
  through 4c3 4%"; "4a1 4e 5qt-only 3–6%"; Fanti's 4b2 4e split 40% 2qt / 45% via 2c3 / 8% via 0c0 (D10034); "5/6 of
  HTRs are fake" (D3093); "only 8 HTR cases solve in ≤5" (D371); Jay's 7 corner cases that skip 4qt (D463);
  "2/3 of 3QT and 1/6 of 4QT cases reduce straight to 2QT" (T509); "R U2 R'" 2c4 95% / 2c3 72.5% (D9053–D9062);
  "9-move HTRs rarely give an optimal"; "switching after more than 2 (or 3) moves is rarely useful"; Kai Cui's
  85% of 2c3 2e need <2 half turns before the first qt (T5573); Yura's 1/6 for inverting the last DR move (T4606).

## Definitions
- A *finish* from a DR state X is a sequence in the DR group (U, D, R2, L2, F2, B2) solving X; optimal = shortest
  (the first study's table). Count *all* optimal finishes (ties), and also all finishes of optimal + 1.
- The *corner path* of a finish: the sequence of named corner subsets (study 1's naming) of the states it passes
  through, recorded at each quarter turn (U/D quarter turn), until the corners are in HTR. A finish reaches HTR at
  the first point where the state is in the HTR group (corners and edges); the moves before that are its *HTR*, the
  rest its *post-HTR* part.
- *NISS readings*: a linear finish S of X can be found as A on normal then B on inverse with S = A·B⁻¹ for any split;
  the inverse side visits the states at the end of S in reverse. A NISS route = (path on normal up to the split,
  path on inverse after it). Count a route as *working* on X if some finish of the target length is found that way.
- *Route class* (what a solver decides to try): the named chain of corner subsets with the side of each step,
  as in docs 396/410 and Daichi's sheet (e.g. "4b2 → 2c3 → HTR, NISS after 2c3"). Make the list of classes from the
  data and from those docs; report how each doc's class maps to ours.
- *Variations*: the DR's last move turned the other way (when it is a quarter turn of the DR axis that can be
  inverted), as in the first study's "invertible last move"; report routes with and without it.

## Questions (exact over all DR states where feasible; otherwise a uniform sample per subset × edge count, at least
## 20,000 states each, exact per state)
1. **Per subset (× bad edges): how often each route class works**, at the optimal and at optimal + 1, counting all
   optimal finishes and all NISS readings. Compare with docs 396/410/171 and the quoted numbers above, cell by cell.
2. **The checklist**: per subset, the ordered list of route classes that finds an optimal finish (and one within +1)
   on the most states for the fewest classes tried (greedy cover, report the cumulative share after 1, 2, 3, … classes,
   and how far greedy is from the best possible set of that size). This is the main deliverable: "on 4c3, try these
   three: 86%". Also weight by a cost proxy (number of distinct HTRs a human writes for that class, e.g. shortest HTR
   length of the class) and say which classes are cheap and which only pay at the margin.
3. **Shortest HTR vs optimal**: how often the optimal finish uses a shortest linear HTR on one side, a shortest NISS
   HTR, an HTR 1 / 2 / 3+ longer than the shortest (T554, T4167, T10409); how often linear and NISS HTR lengths differ
   (T624); the post-HTR length of optimal finishes (average slice in DR optimals, D12508; post-HTR on DR optimals,
   D18095); "9-move HTRs rarely give an optimal".
4. **Extra quarter turns**: share of states whose every optimal uses more qts than the corners need, by subset; the
   share where some optimal does (the two readings explain several quoted numbers apart); half turns before the
   first quarter turn (Kai's 85%).
5. **Last-move variation**: what inverting the last DR move adds to each route class and to the checklist (Yura's 1/6).
6. **Grading hand checklists**: Zagros's 4b2 order, Daichi's cheat sheet, Lewis's lists, Jay/rodney's 3qt 2c0e checks,
   the 4b2 4e disagreement: for each, the exact share of states where it finds the optimal (or +1).
7. Claims: every checkable claim in the reading notes on this topic, with verdict and an example DR for each
   correction.

## Checks
- Reproduce exactly: the first study's per-subset optimal distribution (= Joba's doc 580); DougCube's HTR-state
  distribution (10.13); docs 566/567 where they are not double counted.
- Every route-class membership spot-checked by an independent search on the sticker model on 1,000 random states;
  every printed finish replayed. nissy cross-check of optimal lengths on samples.

## Output layout
`research/src` (Python), `research/htrtools` (Rust; reuse judging-a-dr drtools sources by `#[path]`), `research/out`
(small outputs committed, big ones git-ignored), `out/SUMMARY.md` with every answer, sample sizes and the most striking
findings, `out/witness.json`, `out/claims.tsv`. Lean later for small exact tables.

## Added 2026-11-12: DR bounding effectiveness (request relayed from a professional solver)
"I'd like to see if there's something to be said about how effective DR bounding is, that is how often it does find
optimal (for a given subset), and how many reductions to 2q/1q you need to check to find optimal, which may depend on
the threshold. I also wanna see if my linear programming estimates can be useful for pruning some branches."
8. **DR bounding as a route**: the method of beef beans' DR Bounding doc and rodneykinney's Advanced DR Bounding
   (reduce to 1q (4a1 4e) or 2q in up to R moves on either side, NISS-trace, bound, finish only what the bound
   allows). Per subset and per target M (optimal, optimal+1; and fixed targets 10–13): how often checking all
   reductions to 1q / 2q of length ≤ R finds an optimal (or ≤ M) finish, as a function of R; the smallest R that
   finds it (distribution); how many reductions that is (count of distinct reduction sequences / resulting states
   per DR, as a human would write them). Compare with beef beans' "all reductions ≤4 find optimal about 75–80% on
   2c3" and JTuu's 2c3 2e sim (T5744: linear 7 + bounding 4 = 64.65%, 8 + 5 = 86.05%).
9. **FakeMMAP's reduction-length bound** (T11501–T11504, 2026-04-08): R = max of the expressions in T11502 in M,
   A (shortest HTR normal), B (shortest HTR inverse), C (shortest HTR in the subset) and the section bounds α_i; and the
   multi-qt lower bounds of T11503. Implement exactly as written (read the full messages and FakeMMAP's follow-ups;
   rodneykinney T11512 asked for per-case tables). Check: (a) is R always sufficient (never a finish of ≤ M that needs a
   longer reduction)? any counterexample with a DR written out; (b) how much it prunes: the share of reductions it lets
   you skip per subset and target, against checking every reduction up to the empirical maximum; (c) the T11503 lower
   bounds: how often they prove "no M" beyond the trivial bounds. Produce the per-subset tables rodneykinney asked for.
