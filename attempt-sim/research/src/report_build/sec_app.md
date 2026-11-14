## Appendix A: full tables

**Each change of the tuned plan alone, against the baseline** (round 2, held-out scrambles). Each row is one change:

{{T:r2_ingredients}}

**The other one-at-a-time curves**, around the tuned plan. Each row of each table is a value of that one setting:

{{T:r3_e5_rzp_per_eo_long}}

{{T:r3_e5_rzp_depth}}

{{T:r3_e5_rzp_more}}

{{T:r3_e5_dr_per_line}}

{{T:r3_e5_dr_cap}}

{{T:r3_e5_fin_min_p}}

{{T:r3_e5_reserve}}

**Every plan of round 3** on the held-out scrambles, best score first. Names are the policy names in `research/policies/t_all.toml`: `te1` time split, `te2` order, `te3` adaptive, `te4` safety, `te5` one setting at a time. Each row is a plan:

{{T:r3_all}}

## Appendix B: how it was computed, and what checks it

**The program.** `research/attemptsim`, written in Rust. It reads judging-a-dr's exact optimal finish of every DR state (1.3 GB, proved in Lean in that study), htr-routes' checklist per subset, and the EO-to-DR tables. It plays one attempt per plan and scramble, with every random draw (misses, step times, the day's pace) fixed per scramble, so plans differ only by their decisions. Every solution the simulated solver writes is replayed on the cube, and a run fails if one doesn't solve its scramble; no run has failed.

**The runs.** All with the costs of section 4 (`research/costs.toml`), on uniformly random states written as scrambles (`research/data/scrambles_uniform.txt`):

- *Round 1* tried the five experiments around the baseline with the first costs. Two calibration rounds then tried spreads of the pace and of the form from attempt to attempt. A pace spread of 0.15 gives the top 5's DNF rate. A form spread adds DNFs and bad results but no sub-20s, so it stayed at 0. The costs did not change after that.
- *Round 2* (`policies/all.toml`, 237 plans) ran on 3,400 training scrambles and on held-out scrambles 4,000 to 7,999. The tuned plan's three changes were chosen on the training scrambles. Appendix A's first table is the held-out check.
- *Round 3* (`policies/t_all.toml`, the same experiments around the tuned plan) ran on scrambles 0 to 7,999. Every table of sections 1 and 6 to 10 uses only 4,000 to 7,999.
- *Round 4* (`policies/scale.toml`): the length of the attempt and the solver, 2,000 held-out scrambles each.
- *Sensitivity* (`policies/conclusions.toml`, `src/sensitivity_jobs.sh`): section 11.
- *The official scrambles*: the scrambles of the top 10's official attempts since 2024, from the WCA export (`src/wca_top.py`).

Every table and number on the page comes out of `research/src/tables.py` from the result files and gets filled in by `report_build/assemble.py`. Nothing is typed by hand.

**The Lean certificate** (`lean/AttemptSim`, 56 theorems, no `sorry`) checks what the numbers rest on:

- the cube model, and that every table the simulator prunes and judges with is exact;
- that its candidate lists of EOs and DRs are complete on exported scrambles;
- that its DR moves are the ones of judging-a-dr's exact table;
- that a fixed sample of simulated attempts of the baseline and the tuned plan does what the log says: every solution solves its scramble in the stated length, the clock is the sum of the step costs, and the result is the shortest solution found before the last writing that ended in time.

Lean checks individual attempts, not the averages, which stay **sampled**.

## Docs referred to

- Yura Riabov, [*Hitchhiker's Guide to FMC*](https://docs.google.com/document/d/16nu10y1JkUmVDC11c1h_ULzAl4Vze7zR/edit) (Google Doc).
- Yura Riabov, [*FMC Jan-May 2025*](https://docs.google.com/spreadsheets/d/1Cb7M3KqB5W99sSNOIKLG3xqZ-k58koIexTLahUiPNhs/edit?usp=sharing), a log of 138 attempts (Google Sheet, posted [[D12481]]).
- [*Sub 22 Official Mean Stats*](https://docs.google.com/spreadsheets/d/17L6vArP8t_5yPIeCpiQpp66YBZcLcbxS10hzYtnB-XE/edit?gid=0) (Google Sheet, first linked here by Yura Riabov, [[N1100]]).
- The WCA results export, version 2.0.2 of 13 November 2026 ([worldcubeassociation.org/export/results](https://www.worldcubeassociation.org/export/results)): official FMC results of the top 10 by mean since 2024, and their scrambles. This information is based on competition results owned and maintained by the World Cube Association, published at https://worldcubeassociation.org/results as of November 13, 2026.
- The other studies on this site: [*Judging a DR by hand*](../judging-a-dr/), [*Which HTR routes to try from a DR*](../htr-routes/), [*EO to DR, and scramble to DR*](../eo-to-dr/), [*When to switch an EO*](../eo-switch/).
