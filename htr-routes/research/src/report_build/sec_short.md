There isn't much new in the routes themselves: the checklists below put them in the order Daichi's cheat sheet already suggests. What's new is everything around them: how much each route covers, how long its HTRs are, how bounding compares, and whether FakeMMAP's bound helps. Shares are over uniformly random DR states of the subset ({= n(25000) =} per subset × edges); *finds the optimal* means some optimal finish can be read along that route.

**What's new here**

**How far a short checklist gets you, per subset.** Count a route only when its HTR is at most 2 moves longer than the DR's shortest NISS HTR (budget 2, section 3). Then three routes find the optimal on this share of each corner subset's DRs:

| Subset | Optimal found, 3 routes |
|---|---|
| 0c4 | {= CELL('checklist_corner_shares', '0c4', 'Optimal found, 3 routes') =} |
| 2c5 | {= CELL('checklist_corner_shares', '2c5', 'Optimal found, 3 routes') =} |
| 2c4 | {= CELL('checklist_corner_shares', '2c4', 'Optimal found, 3 routes') =} |
| 2c3 | {= CELL('checklist_corner_shares', '2c3', 'Optimal found, 3 routes') =} |
| 4c3 | {= CELL('checklist_corner_shares', '4c3', 'Optimal found, 3 routes') =} |
| 4b2 | {= CELL('checklist_corner_shares', '4b2', 'Optimal found, 3 routes') =} |
| 0c0 | {= CELL('checklist_corner_shares', '0c0', 'Optimal found, 3 routes') =} |
| 4a1 | {= CELL('checklist_corner_shares', '4a1', 'Optimal found, 3 routes') =} |

The same three get a finish within +1 on {= pc(min(SAMEF(g, '2', 3) for g in G12)) =} ({= ARGMIN(lambda g: SAMEF(g, '2', 3)) =}) to {= pc(max(SAMEF(g, '2', 3) for g in G12)) =} ({= ARGMAX(lambda g: SAMEF(g, '2', 3)) =}). After the third route each extra route adds at most {= f1(E['marg_after3_max'] * 100) =} points, and under 3 points in {= pc(E['marg_after3_share_lt3']) =} of the checklists (section 4).

**The bad-edge count matters, on a few subsets.** A checklist built for the subset × edges beats the corner subset's list (edges pooled) by {= EGA('opt', 1) =} points of all DRs after one route and {= EGA('opt', 3) =} after three. Not much on average, a lot on some. Each row is a subset × edges where it matters, and the share where each list finds the optimal after that many routes:

| Subset × edges | What changes | After | Own list finds the optimal | Pooled list finds the optimal |
|---|---|---|---|---|
| 0c0 0e | its own order | 2 routes | {= EGR('0c0 0e', 2) =} | {= EGR('0c0 0e', 2, 'pooled') =} |
| 2c4 0e | go linear first | 1 route | {= EGR('2c4 0e', 1) =} | {= EGR('2c4 0e', 1, 'pooled') =} |
| 2c3 6e (same on 0e and 8e) | switch at 4b2 first | 1 route | {= EGR('2c3 6e', 1) =} | {= EGR('2c3 6e', 1, 'pooled') =} |
| 4a2 0e | start with the 4b3 regression | 1 route | {= EGR('4a2 0e', 1) =} | {= EGR('4a2 0e', 1, 'pooled') =} |
| 4a1 0e | start with {= EGF('4a1 0e') =} | 3 routes | {= EGR('4a1 0e', 3) =} | {= EGR('4a1 0e', 3, 'pooled') =} |

On 2c5, 0c3, 0c4, 4c3, 4c4 and 4b2 the pooled list loses at most {= EGMAX(('2c5', '0c3', '0c4', '4c3', '4c4', '4b2')) =} points (section 4).

**Which edge count you pass on the way.** Of the DRs whose optimal (budget 2) can go through 4b2, {= ESR('4b2', '2e') =} can go through 4b2 2e, {= ESR('4b2', '4e') =} through 4b2 4e and {= ESR('4b2', '0e') =} through 4b2 0e. From 2c3 it depends on the edges. Each row is a 2c3 edge count; each cell is the share of its DRs that can go through that 4b2:

| From | Can pass 4b2 2e | Can pass 4b2 4e |
|---|---|---|
| 2c3 2e | {= ESV('2c3 2e', '4b2 2e') =} | {= ESV('2c3 2e', '4b2 4e') =} |
| 2c3 0e | {= ESV('2c3 0e', '4b2 2e') =} | {= ESV('2c3 0e', '4b2 4e') =} |

The 4a1 before HTR is always 4a1 4e (proved in Lean), the 4a2 is 4a2 4e ({= ESR('4a2', '4e') =}), and 2c3 is 4e, 2e or 6e. Aiming for one edge count at each step doesn't give a better checklist, though: the first edge path finds {= ESA('opt', 'edge', 0) =} of DRs against {= ESA('opt', 'corner', 0) =} for the first corner route, because on 2c5 2e to 6e, 4b5 2e and 4e, and 4c4 2e and 4e one corner route is many edge paths. Per-step edge checklists are computer only (section 4).

**The HTR budget is what a checklist is really about, not the route.** A NISS reading of a finish is also a linear finish, so *some optimal follows this route* barely separates routes. The share of a corner subset's DRs the best single route covers, lowest to highest corner subset, per budget:

| HTR budget | Best single route covers |
|---|---|
| no limit | {= p0(E['single_inf'][0]) =} to {= p0(E['single_inf'][1]) =} |
| 0 (shortest HTRs only) | {= p0(E['single_b0'][0]) =} to {= p0(E['single_b0'][1]) =} |
| 2 | {= p0(E['single_b2'][0]) =} to {= p0(E['single_b2'][1]) =} |

(section 4).

**Linear vs NISS HTR** (rodneykinney asked in 2023, [[T624]]). Over all DRs the shortest NISS HTR is as long as the shortest linear one (better side) on {= pc(Q3('all', 'niss_eq_linear')) =}, 1 shorter on {= pc(Q3('all', 'niss_shorter_by_1')) =} and 2 or more shorter on {= pc(Q3('all', 'niss_shorter_by_2plus')) =}. On 0c3 it's 2+ shorter on {= pc(Q3('0c3', 'niss_shorter_by_2plus')) =} (section 6).

**The optimal rarely goes through a shortest HTR.** The shortest HTR that any optimal uses, against the DR's shortest NISS HTR, as a share of all DRs:

| Shortest HTR in an optimal | Share of DRs |
|---|---|
| a shortest NISS HTR | {= pc(Q3('all', 'opt_uses_shortest_niss')) =} |
| 1 longer | {= pc(Q3('all', 'opt_htr_plus1')) =} |
| 2 longer | {= pc(Q3('all', 'opt_htr_plus2')) =} |
| 3 or more longer | {= pc(Q3('all', 'opt_htr_plus3more')) =} |

On {= pc(Q3('all', 'every_opt_htr_ge9')) =} of all DRs every optimal needs an HTR of 9 moves or more, and on {= pc(float(Q3('all', 'every_opt_htr_ge9')) - float(Q3('all', 'niss_htr_ge9'))) =} that's the case even though a shorter HTR exists (section 6).

**DR bounding, measured.** Check every reduction to 1q (4a1 4e) of at most R moves, on either side or split. Each row is a value of R, over all DRs:

| R | Finds the optimal | Reductions on average |
|---|---|---|
| 4 | {= pc(Q8('all', '1', '4', 'found_opt')) =} | {= n(round(float(Q8('all', '1', '4', 'mean_reductions_le_R')))) =} |
| 5 | {= pc(Q8('all', '1', '5', 'found_opt')) =} | {= n(round(float(Q8('all', '1', '5', 'mean_reductions_le_R')))) =} |
| 6 | {= pc(Q8('all', '1', '6', 'found_opt')) =} | {= n(round(float(Q8('all', '1', '6', 'mean_reductions_le_R')))) =} |

Which subsets suit it depends on R. At R ≤ 4 it's best on 0c0 ({= pc(Q8('0c0', '1', '4', 'found_opt')) =}), 4a2 ({= pc(Q8('4a2', '1', '4', 'found_opt')) =}) and 4a1 ({= pc(Q8('4a1', '1', '4', 'found_opt')) =}). Reducing to 2q instead, reductions of at most 3 moves reach {= pc(Q8('all', '2', '3', 'found_opt')) =}.

**By hand it stops at about R ≤ 4.** The counts grow about eightfold per move, and only up to 4 do they stay in the low hundreds, the size of the "check all sub-5 reductions" Levi Gibson calls "super quick" ([[D9108]]). Past that it's **computer only, an answer key and not advice**. What it takes to find the optimal on 80% of a subset, one row per subset:

| Subset | Every reduction up to | About this many to write |
|---|---|---|
| 0c0 (eight budget-2 routes stay under 80%) | 3 | {= n(round(float(Q8('0c0', '1', '3', 'mean_reductions_le_R')))) =}, in reach |
| 4a1 | 5 | {= n(round(float(Q8('4a1', '1', '5', 'mean_reductions_le_R')))) =} |
| 4b2 | 6 | {= n(round(float(Q8('4b2', '1', '6', 'mean_reductions_le_R')))) =} |
| 2c5, 4b5 | nothing under 6 moves works | |

Nobody writes the 4a1 or 4b2 lists in an hour (section 8).

**FakeMMAP's bound, tested the way FakeMMAP asked.**

- *R as written* is the largest of its five terms. That's proved never too short (Lean), but only because term 1, about $M - 1$, is one of them: it asks for reductions of {= f1(Q9('opt', 'mean_R_literal')) =} moves on average where {= f1(Q9('opt', 'mean_R_needed')) =} were needed ({= n(Q9('opt', 'cases')) =} state-and-path cases at the optimum), longer than anyone writes. So it's safe to use but prunes nothing in practice.
- *The smallest term*, the bound FakeMMAP's derivation actually gives, is also proved sound once two slips in the printed formulas are fixed: term 2's signs, which as printed make it too short, and the $\alpha$ in every sum, which has to be $\alpha_{i+1}$, the section the two windows share, not $\alpha_i$. It averages {= f1(Q9('opt', 'mean_R_min_terms')) =} moves, the same to one decimal as the exact model of the same constraints ({= f1(Q9('opt', 'mean_R_exact')) =}, *computer only*).
- *C* bounds the middle block of the finish, a linear HTR of a DR in the same subset, so C is the subset's shortest linear HTR, as FakeMMAP defined it (proved in Lean).
- *The multi-qt lower bounds* ([[T11503]]) fail on {= n(E['t11503_n']) =} of those cases with $\alpha_i$; with $\alpha_{i+1}$ they never fail, and they're proved valid.

FakeMMAP asked whether "the typical bound is M \geq 11, rather than M \geq 7" ([[T11504]]). Once every reduction shorter than the one the optimal needs has failed, the corrected bound on a typical path (the median, in moves) is:

| Subset | Corrected bound, median |
|---|---|
| 2c3 | {= CELL('lb_values', '2c3', 'Corrected bound, median') =} |
| 4b2 | {= CELL('lb_values', '4b2', 'Corrected bound, median') =} |
| 0c0 | {= CELL('lb_values', '0c0', 'Corrected bound, median') =} |

That's one or two above the trivial bound, and it reaches the optimum in only {= CELL('lb_shares', '2c3', 'Bound reaches the optimum') =} of 2c3 cases. The per-subset tables rodneykinney asked for ([[T11512]]) are in section 9 and appendix A.

**Hand checklists graded.** Zagros's eight-step 4b2 order finds the optimal on {= GR('Zagros 4b2 order (D15884)', 5, 'cumulative_opt_htr_budget2') =} with budget-2 HTRs and a finish within +1 on {= GR('Zagros 4b2 order (D15884)', 5, 'cumulative_p1_htr_budget2') =}. On 4b2 4e, the share each approach finds the optimal on:

| Approach | Optimal found |
|---|---|
| Yura Riabov's order (trigger, then regress to 2c3), after two steps | {= GR('Yura 4b2 4e order (D6409-D6416)', 2, 'cumulative_opt_htr_budget2') =} |
| same, after three steps | {= GR('Yura 4b2 4e order (D6409-D6416)', 3, 'cumulative_opt_htr_budget2') =} |
| reduce to 1q first, every reduction of at most 4 moves | {= pc(Q8('4b2 4e', '1', '4', 'found_opt')) =} |
| same, at most 5 moves | {= pc(Q8('4b2 4e', '1', '5', 'found_opt')) =} |

(section 10).

**Breaking DR rarely beats the DR-move optimum.** Solved with all 18 face turns (nissy, *computer only*), a finish outside DR is shorter on this share of DRs:

| DRs | Shorter finish outside DR |
|---|---|
| all | {= pc(E['gaps']['g2_all']['shorter']) =} |
| DR-move optimum 12 or less | {= pc(E['gaps']['g2_le12']) =} |
| DR-move optimum 16 | {= pc(E['gaps']['g2_at']['16']) =} |

It's almost always by one move (mean gain {= f3(E['gaps']['g2_all']['mean_gain']) =} moves). Besides long finishes it matters on {= ', '.join(f'{c} ({x:.0f}%)' for c, x, y in E['gaps']['g2_worst']) =}, where shapes like this one win (section 3):

```
R L F2 B2 R' L'   // the type of finish that beats the DR-move optimum there
```

**What it confirms or corrects**

**Confirmed: the routes.** The first route of the budget-2 checklist is what Daichi's cheat sheet says: switch after 4b2 on 4c3 and 0c4, go through 2c3 on 2c4 and 2c5, 4a2 4e switch on 0c3. Graded against my first three routes, Daichi's sheet finds the optimal more often, about as often or less often on these subsets (section 10):

| Daichi's sheet | Where |
|---|---|
| more often | 4b2, 4a1, 2c3 0e and 8e, 0c0 2e to 6e |
| about as often | 2c4 0e to 6e, 4a2 2e, 0c4 2e |
| less often | all of 2c5, 0c3, 4c3, 4c4 and 4b5; 0c4 except 2e; 4a2 0e and 4e; 2c3 2e to 6e |

**Confirmed: uniform states are the right model.** Take the DRs cubelib finds on {= n(E['gaps']['n_scr']) =} random scrambles (every EO-first DR of at most 11 moves, {= n(E['gaps']['n_dr11']) =} of them). Corner-subset shares are within {= f1(E['gaps']['share_maxdiff']) =} points of uniform and mean optimal finishes within {= f2(E['gaps']['mean_maxdiff']) =} moves. Per corner subset, every checklist share, bounding share and HTR headline of this section moves by under a point, with two exceptions (share of DRs):

| Number | Real DRs | Uniform |
|---|---|---|
| 0c0, first route | {= f1(min(E['gaps']['c0c0_first'][:2])) =}–{= f1(max(E['gaps']['c0c0_first'][:2])) =}% | {= f1(E['gaps']['c0c0_first'][2]) =}% |
| 0c3, NISS HTR 2+ shorter | {= f1(E['gaps']['c0c3_2plus'][1]) =}% (each DR once) | {= f1(E['gaps']['c0c3_2plus'][0]) =}% |

The first route is the same on every corner subset, and the first three are the same everywhere but 0c4, where a near-tie changes the third. What shifts is the bad-edge mix inside a subset: 0e up to {= int(round(E['gaps']['e0_max_rarer'])) =}% rarer, 6e up to {= int(round(E['gaps']['e6_max_more'])) =}% commoner (section 12).

**Confirmed: the known tables**, exactly: Joba's optimal distribution, DougCube's 663,552 HTR states (mean 10.13), Joba's DR-to-HTR lengths; Aedan Bryant's sheet except four rows that carry another row's numbers and its two fake-HTR rows, whose states were built around one trigger; the *Extra Quarter-Turn Stats* sheet on every comparable row (sections 5, 11).

**The 2qt(a)/(b) labels.** Aedan Bryant's sheet and *allcases* call 4b2 "2qt(a)", as Tzak, Levi Gibson and Zagros said at the time. The one thing added here: the *Extra Quarter-Turn Stats* sheet uses the opposite letters, as its own example triggers show. So mrauo's "Only 1/3 of 2q 4b2e cases use 2qt" read the 4a2 2e row (section 5).

**Explained: the quoted extra-qt numbers.** They depend on whether you ask about every optimal, some optimal or one optimal from a solver; rodneykinney's 57% and Lichi Fang's "over 60%" fit different readings, and both fit (section 7).

**Corrected, with the first study's table: the last DR move.** Turning it the other way gives a finish one move shorter on {= pc(Q5('all', 'share_variation_shorter')) =} of DRs, never more than one, so about a third of a move on average, not the 1/6 Yura Riabov estimated in 2024 (Yura called it "very rough"). It doesn't change which routes to try (section 7).

**Corrected** (errata, each with an example). Levi Gibson's "check all sub-5 reductions … gets optimal like 75% of the time, and it gets optimal +1 the rest of the time", with bounding alone and every reduction of at most 4, share of DRs where it finds the optimal and a finish within +1:

| Subset | Optimal | Within +1 |
|---|---|---|
| 4a2 (the one Levi Gibson had just named) | {= pc(Q8('4a2', '1', '4', 'found_opt')) =} | {= pc(Q8('4a2', '1', '4', 'found_p1')) =} |
| 2c3 | {= pc(Q8('2c3', '1', '4', 'found_opt')) =} | {= pc(Q8('2c3', '1', '4', 'found_p1')) =} |

So on 4a2 the 75% holds, but +1 doesn't cover the rest. The other corrections:

- 4c4 0e has 10-move linear HTRs.
- The longest shortest HTR is 13 linear and 12 with NISS.
- The optimal through its shortest HTR needs a switch after more than 2 moves on {= pc(E['late_excl_gt2']) =} of the DRs outside the subsets Evan named as exceptions, an upper bound on how often a late switch is needed (Yura Riabov's "more like 3" holds outside 0c4, 4c4 and 2c5).
- In FakeMMAP's reduction bound and multi-qt lower bounds: the index of $\alpha$ ($\alpha_{i+1}$, not $\alpha_i$) and, when R is read as the smallest term, the signs of term 2 (proved in Lean, with counterexamples).

**Confirmed**: Levi Gibson's "pretty sure 15 is gods number for 4a1 4e" is right for the leave slice, which is what Levi Gibson measures ({= E['lsmax']['4a1 4e'] =}, exact); the full finish can need 17.
