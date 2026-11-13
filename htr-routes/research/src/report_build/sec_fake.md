## 9. FakeMMAP's reduction-length bound

**What FakeMMAP proposed.** From [[T11501]]: "Let's say we're looking for a finish in M moves (or less), assuming we're only allowed to use N>1 qts. We want to know how long our reductions to 1q should be, in order to find that solution. Let R be the biggest possible length of a reduction to 1q you have to check".

The inputs:

- **A** and **B**: the optimal HTR on normal and on inverse.
- **C**: "the shortest possible HTR in the subset" ("so 2c3 2e would have C=5, 4b2 0e would have C=6").
- **$\alpha_i$**, the section bounds: "Numbering these sections from 0 to N, let \alpha_i be the bound for the ith section. For example 4a3 2e would have \alpha_1=3, because you have to to the 4b2 parity fix."

Then [[T11502]]: "R is the max of the following", five families of terms over sets S of consecutive windows, solved "with Fourier-Motzkin elimination by hand". And [[T11503]], "multi-qt DR bounding... well, sort of": lower bounds on M once every reduction shorter than R' has failed. On those lower bounds FakeMMAP added "I don't know how useful these bounds really are, I have to put in the numbers to see if there are situations where the typical bound is M \geq 11, rather than M \geq 7 lol." ([[T11504]]). This section puts in the numbers, for the upper bound R too.

**The model behind the five terms.** A finish with $N$ quarter turns is $h_0\, q_1\, h_1 \ldots q_N\, h_N$: sections $h_i$ of $s_i \geq \alpha_i$ half turns, length $L = N + \sum_i s_i \leq M$. FakeMMAP's term 1 ([[T11502]]), "M-\alpha_i-\alpha_{i+1}-1 (basically leaving those two as the 1q finish, unlikely to be the maximum, unless M is VERY small)", fixes the windows. Window $i$ is sections $i$ and $i+1$ around quarter turn $q_{i+1}$, and the 1q reduction that leaves it as the finish is $L - 1 - s_i - s_{i+1}$ moves (the moves before it on normal, the ones after it on inverse). Three blocks of the finish are HTRs, so you get three constraints:

- **A**, all but the last section: $L - s_N \geq A$.
- **B**, all but the first section, read on inverse: $L - s_0 \geq B$.
- **C**, the middle $q_1\, h_1 \ldots q_N$, without the first and last sections: $L - s_0 - s_N \geq C$.

The middle is a linear HTR of the DR you have after the first section's half turns. A half turn, before or after, never changes the subset or the bad-edge count (proved in Lean over all 40,320 corner and 40,320 U/D-edge arrangements and all six half turns: `half_turns_keep_subset_data` and `labels_keep`, lean/FakeBound/FakeBound/Subset.lean). So the right bound is the shortest linear HTR anywhere in the subset × edges, which is C exactly as FakeMMAP defined it (2c3 2e: {= MINLIN('2c3 2e') =}, 4b2 0e: {= MINLIN('4b2 0e') =}; Lean `fake_C_examples`, same file).

Every term is the sum of the window bounds over a set $S$ of windows covering a run of sections, plus one constraint on the total of that run. Two windows $i$, $i+1$ share section $i+1$, which gets counted twice. The five terms, one row each:

| Term | Sections covered | Windows S | Constraint used |
|---|---|---|---|
| 1 | one window | a single window | none |
| 2 | 0 to $N$ | $S \subset \{0, \ldots, N-1\}$ | the length |
| 3 | 0 to $N-1$ | $\{0, \ldots, N-2\}$ | A |
| 4 | 1 to $N$ | $\{1, \ldots, N-1\}$ | B |
| 5 | the middle, 1 to $N-1$ | $\{1, \ldots, N-2\}$ | C |

For $N = 2$ no window avoids both end sections, which is why FakeMMAP says to "just discard this constraint". Nothing in the derivation needs a NISS HTR.

The Lean theorems cited here are in the study's folder lean/FakeBound (Lean 4, no Mathlib, no `sorry`), in the files FakeBound/Finish.lean, Formula.lean, Counter.lean and Subset.lean, and Corrections/Examples.lean.

*Fixed 12 Nov 2026.* Until then this section said C must be the shortest NISS HTR. That was wrong: it modelled C as bounding every finish minus one middle section, which is a NISS HTR of the DR itself and not FakeMMAP's constraint.

**How I tested it.** First $\alpha_i$ for every corner path that occurs: the fewest half turns section i needs over every corner arrangement following the path. For 4a3 > 4b2 > 4a1 > HTR that's {= E['alpha_4a3'] =}, FakeMMAP's $\alpha_1 = 3$, and the study's Lean certificate re-derives every $\alpha$ (appendix B). Then for every sampled state, every corner path of its optimal (or +1, or ≤ 10, 11, 12) finishes, and the shortest reduction such a finish needs. I compared that need with R four ways:

1. the formula of [[T11502]] as written, the largest of its terms;
2. the same without term 1;
3. the smallest term, with term 2's signs and the $\alpha$ index fixed (see (a));
4. the exact optimum of the same model, *computer only*: the largest shortest-reduction any whole-number section lengths allowed by $\alpha$, A, B and C can force, solved by enumeration instead of by hand.

Each row is a target finish length. It gives the number of (state, path) cases, the mean R in moves for each of the four readings with the corner path known, and the mean reduction the finishes actually needed. Sampled, {= n(25000) =} states per subset × edges; the means and shares in this section weight each case by the size of its subset × edges, so they are over uniformly random DRs.

{{fake_summary}}

Same rows: the longest reduction any finish needed, and the share of cases where each reading of R was too short:

{{fake_short}}

**(a) What is proved.** Each verdict below is a Lean theorem, with its file.

**C is the subset's shortest linear HTR, as FakeMMAP defined it.** Term 5 follows from $L - s_0 - s_N \geq C$ (`term5_sound`, FakeBound/Finish.lean), and half turns keep the subset × edges (`labels_keep`, above). A smaller C, like the DR's own shortest NISS HTR, is still a valid input but only weakens R. A bound on the middle block and a bound on the finish minus one middle section are different statements, and neither implies the other (`C_placement`, FakeBound/Counter.lean).

**Every sum needs $\alpha_{i+1}$, not $\alpha_i$**, in the terms of [[T11502]] and in the lower bounds of [[T11503]]. Windows $i$ and $i+1$ share section $i+1$, and that's the section counted twice (`cover_sum`, FakeBound/Finish.lean). Counterexample to $\alpha_i$ (`alpha_i_fails`, FakeBound/Counter.lean). The row is one finish: its $\alpha$ per section, its length, its section lengths $s_i$, and the 1q reduction each window needs:

| Corner path | $\alpha$ per section | Finish | Section lengths | 1q reduction per window |
|---|---|---|---|---|
| 4b2 > 4a3 > 4b2 > 4a1 > 0c0 | 0, 0, 3, 1, 0 | 14 | 2, 1, 3, 1, 3 | 10, 9, 9, 9 |

So a 9-move reduction is needed. With $\alpha_i$ the smallest term is 8, whatever A, B and C are, and the first bound of [[T11503]] claims $28 \geq 29$. (c) has a real DR on which the lower bound fails.

**R as written is sound, but only because term 1 is among the terms.** [[T11502]] says "R is the max of the following". The largest term is never too short, with any signs and either $\alpha$ index (`Rmax_sound`, FakeBound/Formula.lean), because it's at least term 1, about $M - 1$. So R as written is safe to use, just loose. In the sample it was never too short in any case, at any target.

**The smallest term is sound for every finish** (`Rmin_sound`, FakeBound/Formula.lean), with term 2 as derived and $\alpha_{i+1}$. It's the bound the derivation gives, and it fits FakeMMAP's own remarks in [[T11502]]: term 1 is "unlikely to be the maximum, unless M is VERY small", which is true of the smallest term and false of the largest, and "You only need to consider minimal such S's". It isn't always the exact worst case (`Rmin_not_tight`, FakeBound/Counter.lean): with $N = 3$, $\alpha = 0$, $M = 5$, $A = B = 5$ and $C = 0$ it gives 3, but every finish allowed has a reduction of at most 2, because the terms use A, B and C one at a time, never together. On the sample it equals the exact model in {= pc(Q9('opt', 'min_terms_eq_exact')) =} of cases at the optimum, and was never too short.

**Read as the smallest term, term 2 as printed is unsound: its signs are flipped.** The derivation gives

$$\frac{(|S|-1)M + (N-|S|) - \sum \alpha}{|S|};$$

[[T11502]] prints "\frac{(|S|-1)M-(N-|S|)+\sum_{i edge} \alpha_i}{|S|}", which renders as

$$\frac{(|S|-1)M-(N-|S|)+\sum_{i\ \mathrm{edge}} \alpha_i}{|S|}.$$

 The first bound of [[T11503]] is the same inequality solved for M, and it has the derived signs, so the two messages disagree with each other. Counterexample (`printed_term2_fails`, FakeBound/Counter.lean), read as the table above:

| Corner path | $\alpha$ per section | Finish | Section lengths | 1q reduction per window |
|---|---|---|---|---|
| 4a1 > 0c0 > 4a1 > 0c0 | 0 | 10 | 0, 3, 0, 4 | 6, 6, 5 |

Term 2 as printed with $S = \{0, 2\}$ gives 4, whatever A, B and C are; derived, it gives 5. With the printed $\alpha_i$ as well it's still 4 (`literal_min_fails`). On the sample, the smallest term with term 2 and the index exactly as printed is too short on {= pc(Q9('opt', 'insuff_min_terms_as_written')) =} of cases at the optimum ({= n(V9()[0]) =} of the {= n(V9()[1]) =} cases, {= pc(V9()[0] / V9()[1]) =}, before weighting).

A real DR where it bites, replayed ($N = 3$; every optimal finish takes the path in the table):

```
{= WIT('W14', 'scramble') =} // 0c3 2e
{= WIT('W14', 'optimal_finish') =} // optimal finish
```

Its finish, read as the tables above:

| Corner path | $\alpha$ per section | Finish | Section lengths | 1q reduction per window |
|---|---|---|---|---|
| 0c3 > 4a2 > 4a1 > HTR | 0, 3, 3, 0 | {= WIT('W14', 'optimal') =} | {= ', '.join(map(str, SECTIONS(WIT('W14', 'optimal_finish')))) =} | {= ', '.join(map(str, WINDOWS(WIT('W14', 'optimal_finish')))) =} |

Term 2 with $S = \{0, 2\}$ as printed gives {= f1(T2(14, 3, [0, 2], [0, 3, 3, 0])) =}, so 6. Derived, it gives {= f1(T2(14, 3, [0, 2], [0, 3, 3, 0], True)) =}, so 7. The arithmetic from the sections on is checked in Lean (`witness_0c3`); the state's optimum and its paths come from the exact table and two independent enumerations, not from Lean.

The other choices are readings, not corrections:

- A and B are the shortest *linear* HTR on each side.
- C is per subset × edges, as in FakeMMAP's examples.
- $\alpha$ counts corners only, so it stays a valid lower bound.
- R is taken over finishes of M moves or fewer and rounded down.
- FakeMMAP's advice to use C + 1, A + 1, B + 1 in an attempt is not modelled.
- Five families aren't everything Fourier–Motzkin elimination gives (for example A and B together raise C to $A + B - M$), which is why the smallest term sits a move above the exact model in a few cases.

**(b) It doesn't prune at the reduction lengths solvers write.** Each row is a case; each cell is the mean R in moves for that reading:

| Case | As written | Without term 1 | Smallest term | Exact model |
|---|---|---|---|---|
| at the optimum, corner path known | {= f1(Q9('opt', 'mean_R_literal')) =} | {= f1(Q9('opt', 'mean_R_no_term1')) =} | {= f1(Q9('opt', 'mean_R_min_terms')) =} | {= f1(Q9('opt', 'mean_R_exact')) =} |
| at the optimum, path unknown | {= f1(Q9('opt', 'mean_Rstate_literal')) =} | {= f1(Q9('opt', 'mean_Rstate_no_term1')) =} | {= f1(Q9('opt', 'mean_Rstate_min_terms')) =} | {= f1(Q9('opt', 'mean_Rstate_exact')) =} |
| 12 or better, path unknown | {= f1(Q9('M12', 'mean_Rstate_literal')) =} | {= f1(Q9('M12', 'mean_Rstate_no_term1')) =} | {= f1(Q9('M12', 'mean_Rstate_min_terms')) =} | {= f1(Q9('M12', 'mean_Rstate_exact')) =} |

*Path unknown* is the worst case over the subset's corner paths, with the DR's own A and B. What the finishes actually needed:

- at the optimum, path known: {= f1(Q9('opt', 'mean_R_needed')) =} on average and {= Q9('opt', 'max') =} at most;
- at the optimum, path unknown: the longest need per subset × edges is {= f1(Q9('opt', 'R_empirical_max')) =} on average, so none of them lets you skip a reduction you would have checked anyway;
- hunting a fixed M is the same story (last row): the longest need per subset × edges averages {= f1(Q9('M12', 'R_empirical_max')) =} and is {= Q9('M12', 'max') =} at most.

Solvers check reductions of 4 to 6 moves (section 8), and a bound that says *go to 9 or 10* never tells you to stop earlier than that. Where the bound could help is the other direction, proving that a short M is impossible, and that's (c).

**rodneykinney's tables.** rodneykinney asked for "some tables for specific cases" ([[T11512]]). They cover each subset × edges at target $M = 10$, 11, 12, and give R when nothing is read off the DR (A, B and C all set to the subset's shortest linear HTR, worst case over the subset's corner paths) three ways: from the formula without term 1, from the exact model (*computer only*), and as the longest reduction any sampled finish of that length needed. Each is one number per subset, so you can use it in an attempt. At $M = 12$ for a few subsets (all in appendix A), each row a subset × edges and each cell a reduction length in moves:

| Subset | R from the formula without term 1 | R from the exact model | Longest reduction needed |
|---|---|---|---|
| 2c3 2e | {= CELL('rodney_table', ('2c3 2e', '12'), 'R from the formula without term 1') =} | {= CELL('rodney_table', ('2c3 2e', '12'), 'R from the exact model') =} | {= CELL('rodney_table', ('2c3 2e', '12'), 'Longest reduction needed') =} |
| 4b2 4e | {= CELL('rodney_table', ('4b2 4e', '12'), 'R from the formula without term 1') =} | {= CELL('rodney_table', ('4b2 4e', '12'), 'R from the exact model') =} | {= CELL('rodney_table', ('4b2 4e', '12'), 'Longest reduction needed') =} |
| 4c3 2e | {= CELL('rodney_table', ('4c3 2e', '12'), 'R from the formula without term 1') =} | {= CELL('rodney_table', ('4c3 2e', '12'), 'R from the exact model') =} | {= CELL('rodney_table', ('4c3 2e', '12'), 'Longest reduction needed') =} |
| 4a2 2e | {= CELL('rodney_table', ('4a2 2e', '12'), 'R from the formula without term 1') =} | {= CELL('rodney_table', ('4a2 2e', '12'), 'R from the exact model') =} | {= CELL('rodney_table', ('4a2 2e', '12'), 'Longest reduction needed') =} |
| 2c4 4e | {= CELL('rodney_table', ('2c4 4e', '12'), 'R from the formula without term 1') =} | {= CELL('rodney_table', ('2c4 4e', '12'), 'R from the exact model') =} | {= CELL('rodney_table', ('2c4 4e', '12'), 'Longest reduction needed') =} |

**(c) The multi-qt lower bounds, and one index.** The first bound of [[T11503]] is

$$M \geq \frac{|S|(R'+1) - N + \sum \alpha_i}{|S| - 1},$$

the sum "over all i's such that i, i+1 are both in S" (as in [[T11502]]). Windows $i$ and $i+1$ share section $i+1$, so the section counted twice is $\alpha_{i+1}$, not $\alpha_i$. That follows from term 1's numbering alone (`cover_sum`).

As written, the bounds are wrong in {= n(E['t11503_n']) =} of {= n(E['t11503_counts']['cases']) =} cases at the optimum (subsets {= ', '.join(E['t11503_subsets']) =}): {= n(E['t11503_kinds'].get('first', 0)) =} times the first bound and {= n(E['t11503_kinds'].get('B', 0)) =} times the one with B. With $\alpha_{i+1}$ they never fail ({= n(E['t11503_counts']['violations_alpha_i_plus_1']) =} cases), and they're proved valid for every finish, along with the "very stupid bounds" (`lower_free`, `lower_A`, `lower_B`, `lower_C`, `lower_stupid`, FakeBound/Finish.lean).

A real DR where the index matters, replayed:

```
{= WIT('W13', 'scramble') =} // 0c4 0e
{= WIT('W13', 'optimal_finish') =} // optimal finish
```

Its finish, read as the tables above:

| Corner path | $\alpha$ per section | Finish | Section lengths | 1q reduction per window |
|---|---|---|---|---|
| 0c4 > 4a3 > 4b2 > 4a1 > HTR ($N = 4$) | 0, 1, 3, 1, 0 | {= WIT('W13', 'optimal') =} | {= ', '.join(map(str, SECTIONS(WIT('W13', 'optimal_finish')))) =} | {= ', '.join(map(str, WINDOWS(WIT('W13', 'optimal_finish')))) =} |

So every reduction shorter than $R' = {= min(WINDOWS(WIT('W13', 'optimal_finish'))) =}$ fails. With $S = \{0, 2, 3\}$:

- as written, the bound adds $\alpha_2 = 3$ and gives $M \geq {= f1(LB11503(9, 4, [0, 2, 3], [0, 1, 3, 1, 0])) =}$, so 15, but the finish is 14;
- with $\alpha_3 = 1$ it gives {= f1(LB11503(9, 4, [0, 2, 3], [0, 1, 3, 1, 0], True)) =}, so 14.

This one is checked in Lean end to end: the optimum (`dr_optima_correct`, from the first study's proved table), the finish (`dr_solutions_valid`), its corner path, $\alpha$, sections and reductions, and both inequalities (`index_example`, `index_example_arith`, Corrections/Examples.lean).

**The typical bound, FakeMMAP's question.** I took every (state, corner path) at the optimum with at least two quarter turns, set $R'$ to the shortest 1q reduction a finish of that path needs (so every shorter reduction has failed), and computed the corrected bounds ($\alpha_{i+1}$, C the subset's shortest linear HTR). They sit next to the "very stupid bounds" $M \geq A + \alpha_N$, $M \geq B + \alpha_0$ and the optimum itself (sampled, 25,000 per subset × edges; each corner subset's rows count every (state, path) case). Each row is a corner subset; the bounds and the optimum are in moves:

{{lb_values}}

How often the corrected bound beats the trivial one, reaches the optimum, and is 11 or more, as a share of the subset's cases:

{{lb_shares}}

So on most subsets the answer to FakeMMAP's question is yes. The corrected bound on a typical path (the median) is one or two above the trivial bound. Each row is a bound and the subsets where it is the median:

| Typical bound (median) | Subsets |
|---|---|
| $M \geq {= CELL('lb_values', '0c3', 'Corrected bound, median') =}$ | 0c3 |
| $M \geq {= CELL('lb_values', '0c4', 'Corrected bound, median') =}$ | 2c5, 4a2, 0c4, 4c4 |
| $M \geq {= CELL('lb_values', '2c3', 'Corrected bound, median') =}$ | 2c4, 2c3, 4c3, 4b5 |
| $M \geq {= CELL('lb_values', '4a1', 'Corrected bound, median') =}$ | 4a1 |
| $M \geq {= CELL('lb_values', '4b2', 'Corrected bound, median') =}$ | 4b2 |
| $M \geq {= CELL('lb_values', '0c0', 'Corrected bound, median') =}$ | 0c0 |

It's 11 or more on {= CELL('lb_shares', '2c3', 'Bound 11 or more') =} of 2c3 paths. It stays two to four and a half moves below the mean optimum, though, and reaches the optimum itself on at most {= p0(max(float(CELL('lb_shares', g, 'Bound reaches the optimum').rstrip('%')) for g in G12) / 100) =} of a subset's cases. So it only tells you to stop writing longer reductions if you're hunting a finish well below the optimum.

How often the bounds beat the trivial one, size-weighted over all subsets, as a share of cases:

| Bound | Beats the trivial bound |
|---|---|
| as written, with $\alpha_i$ | {= pc(Q9('opt', 'LB_beats_trivial')) =} |
| with $\alpha_{i+1}$ | {= pc(Q9('opt', 'LB_shared_beats_trivial')) =} |
| exact model, *computer only* | {= pc(Q9('opt', 'LB_exact_beats_trivial')) =} |
