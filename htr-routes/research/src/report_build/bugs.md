# Which HTR routes to try from a DR: corrections

*Goes with the write-up on which HTR routes to try from a DR, but reads on its own. The write-up has the measurements and the tables.*

November 2026. A date in brackets is a link to that message on the FMC solvers Discord (#fmc-theory, #fmc-discussion or #non-dr-discussion).

**What everything below is measured against:**

- **The exact optimal finish of every DR state** (all 19,508,428,800, from the first study, proved in Lean there), and the shortest linear HTR of every one of the 29,400 HTR cosets.
- **{= n(25000) =} uniformly random DR states per subset × edges** ({= n(1200000) =} in all), each solved exactly: every optimal and +1 finish, every NISS reading, the shortest HTR on each side and with NISS, every reduction to 1q.

Every scramble and move sequence below was replayed on a sticker-level cube. Each item also says how much of its example is checked in Lean (the study's folder lean/FakeBound: Corrections/Examples.lean and the FakeBound files); the rest is computed, not proved. These are only the statements the numbers go against. Most of what was said holds up, and that's in the write-up's section 11.

---

**a. "so yeah, should be 1/6"** (Yura Riabov, [[T4606]], on how much turning the last DR move the other way improves the finish).

Over all DRs the better of X and X·R2 is {= f3(Q5('all', 'mean_gain')) =} moves shorter on average: X·R2 is one move shorter on {= pc(Q5('all', 'share_variation_shorter')) =} of DRs and never more than one, so the gain is about 1/3 of a move, twice the estimate. Yura Riabov called the estimate "very rough" and said "i doubt it will be more than a half move difference with 1 move inverted" ([[T4610]]); that ceiling holds. The first study had the exact third.

Example. Think of the first line as the end of a DR on U/D whose last move was a quarter turn of R (say R). Turning that move the other way (R') gives the same state followed by R2, the second line:

```
{= WIT('W06', 'scramble') =} // 4b2 2e, optimal {= WIT('W06', 'optimal') =}
{= WIT('W06', 'variation_scramble') =} // with R2 appended, optimal {= WIT('W06', 'variation_optimal') =}
```

```
{= WIT('W06', 'optimal_finish') =} // optimal finish of the first
{= WIT('W06', 'variation_finish') =} // optimal finish of the second
```

*Lean-checked*: both optima, both finishes and the subset (`dr_optima_correct`, `dr_solutions_valid`, `labels_htr_routes`). The share and the mean gain are counted over the first study's exact table, not proved in Lean.

**b. "Interesting that it seems 4qt 4C0E is the only HTR subset that is guaranteed 11 moves without NISS"** (Jay, [[T619]]).

Over all 29,400 HTR cosets: 4c4 0e ("4qt 4C0E") has linear HTRs of {= MINLIN('4c4 0e') =} moves, and the one subset whose shortest linear HTR is always {= MINLIN('0c4 8e') =} or more is 0c4 8e (fake HTR corners with 8 bad edges). Lewis Isom noticed the 10 in Aedan Bryant's sheet in 2024 ([[T4104]]: "also under 4qt 4c0e the trigger given is 11 moves but stats say 10 is possible").

Example, with the linear HTR nissy finds on inverse:

```
{= WIT('W08', 'scramble') =} // 4c4 0e
{= WIT('W08', 'nissy_linear_htr') =} // linear HTR on inverse
```

*Lean-checked*, all of it: the subset, the 10-move linear HTR on inverse and that the printed one is valid, and that 0c4 8e is the only subset × edges whose shortest linear HTR is never below 11 (`htr_4c4`).

**c. "No, the maximum it takes is 12 moves linearly, and 11 moves using NISS."** (Lewis Isom, [[T4100]], answering whether DR to HTR takes at most 9.)

Both are one short. 0c3 4e and 4c4 0e have HTR cosets whose shortest linear HTR is {= MAXLIN('0c3 4e') =}, and in the sample some DRs need 13 on both sides and 12 with NISS. Daichi had the 13 right later ([[T11594]]: "0c3 4e and 4c4 0e have 13 move optimal HTR cases").

Example, with nissy's shortest HTRs:

```
{= WXX('X2', 'scramble') =} // 0c3 4e, optimal {= WXX('X2', 'optimal') =}
{= WXX('X2', 'nissy_linear') =} // shortest linear HTR, either side
{= WXX('X2', 'nissy_niss') =} // shortest with NISS
```

*Lean-checked*: the optimum, the subset, the 13-move shortest linear HTR on each side, and that both printed HTRs are valid (`dr_optima_correct`, `htr_13`). That no NISS HTR of 11 exists is from nissy and the study's search, not Lean.

**d. "this isn't the worst practice but it's pretty rare for switching after doing more than 2 moves to actually be useful, unless you're variationmaxing"** (Evan, [[D11196]]).

The optimal through its shortest HTR needs a switch after more than 2 moves on {= pc(C11('all', 'shortest_htr_needs_switch_after_gt2')) =} of DRs (sampled, {= n(25000) =} per subset × edges). That is: take the shortest HTR that any reading of any optimal finish reaches; every reading that reaches it switches after 3 or more moves. It's an upper bound on how often a late switch is needed for the optimal. On some of these DRs another optimal finish, with a longer HTR, may be readable linearly or with an early switch, which isn't measured here.

Evan named exceptions in the same thread ("the b side of 4c3", "4c4 and 0c4 ofc but those are pretty rare", [[D11237]], [[D11238]]). Leaving out all of 4c3, 4c4 and 0c4 it's still {= pc(E['late_excl_gt2']) =}. Yura Riabov's "More like 3 imo" ([[D11235]]) fits much better: after 4 or more moves it's small except on 0c4, 4c4 and 2c5.

| Switch needed after | 2c3 | 4b2 | 2c4 | 2c5 |
|---|---|---|---|---|
| more than 2 moves | {= pc(C11('2c3', 'shortest_htr_needs_switch_after_gt2')) =} | {= pc(C11('4b2', 'shortest_htr_needs_switch_after_gt2')) =} | {= pc(C11('2c4', 'shortest_htr_needs_switch_after_gt2')) =} | {= pc(C11('2c5', 'shortest_htr_needs_switch_after_gt2')) =} |
| 4 or more moves | {= pc(C11('2c3', 'shortest_htr_needs_switch_after_gt3')) =} | {= pc(C11('4b2', 'shortest_htr_needs_switch_after_gt3')) =} | | |

Yura Riabov added "i almost never do this but i think it is useful" and "i really don't like switching after more than 2 moves or for badish cases, which is why i'm worse at finishes than i could be" ([[D11239]], [[D11240]]).

Example with a single optimal finish ({= WIT('W12', 'optimal') =}). Its shortest HTR in any reading is {= WIT('W12', 'shortest_htr_in_any_reading_of_any_optimal') =} moves, and every reading with that HTR switches after {= WIT('W12', 'readings_with_it', 0, 'moves_before_switch') =} moves:

```
{= WIT('W12', 'scramble') =} // 2c3 2e
{= WIT('W12', 'optimal_finish') =} // the only optimal finish
{= ' '.join(WIT('W12', 'optimal_finish').split()[:4]) =} // on normal
({= INV(' '.join(WIT('W12', 'optimal_finish').split()[4:])) =}) // then on inverse
```

With a single optimal finish the upper bound is exact: here the late switch is needed. *Lean-checked*: the optimum, the finish and the subset (`dr_optima_correct`, `dr_solutions_valid`, `labels_htr_routes`). That it's the only optimal finish, and the HTR lengths of its readings, come from the study's enumeration (nissy also finds one optimal), not Lean.

**e. "I like to check all sub-5 reductions. This can be done super quick and gets optimal like 75% of the time, and it gets optimal +1 the rest of the time"** (Levi Gibson, [[D9108]]; "sub-5" is "4 or less", [[D9221]]).

Just before, Levi Gibson wrote "for the 4a2 subset I use full DR Bounding" ([[D9106]]), and a few minutes later "I don't use it fully for any subsets other than 4a2 and 2c3" ([[D9113]]). So: write every reduction to 1q of at most 4 moves, on normal, on inverse and split by NISS, and finish each reduced state optimally, with any number of quarter turns (sampled, 4,000 states per subset × edges).

| Subset | Optimal | Within +1 | Reductions on average |
|---|---|---|---|
| 4a2 | {= pc(Q8('4a2', '1', '4', 'found_opt')) =} | {= pc(Q8('4a2', '1', '4', 'found_p1')) =} | {= n(round(float(Q8('4a2', '1', '4', 'mean_reductions_le_R')))) =} |
| 2c3 | {= pc(Q8('2c3', '1', '4', 'found_opt')) =} | {= pc(Q8('2c3', '1', '4', 'found_p1')) =} | {= n(round(float(Q8('2c3', '1', '4', 'mean_reductions_le_R')))) =} |
| 2c3 2e | {= pc(Q8('2c3 2e', '1', '4', 'found_opt')) =} | | |
| 2c3 4e | {= pc(Q8('2c3 4e', '1', '4', 'found_opt')) =} | | |

On 4a2 the 75% holds, but "+1 the rest of the time" doesn't. On 2c3 both fall short. On 2c3 2e and 4e Levi Gibson adds triggers: "For 2c3 2e and 4e I do full DR Bounding + checking the 5-move triggers, and that seems to catch everything" ([[D9117]]). The triggers aren't measured here, so this corrects the share for bounding alone. Levi Gibson's later answer to "Would it be around 80 percent?" for 2c3 was a guess ("yeah something like that I'd guess", [[D9209]]), with the advice to check "a bunch of half turns into a 5-move trigger" as well ([[D9212]]).

Example, {= WXX('X1', 'optimal') =} optimal. I enumerated all {= WXX('X1', 'reductions_le4') =} different states reached by a reduction to 4a1 4e of at most 4 moves on the sticker model and finished each optimally from the exact table: the best total is {= WXX('X1', 'best_with_reduction_le4') =}, optimal + 2. The optimal needs a 5-move reduction:

```
{= WXX('X1', 'scramble') =} // 2c3 2e
{= WXX('X1', 'normal') =} // reduction on normal
{= WXX('X1', 'rest') =} // then the rest
```

*Lean-checked*: the optimum and the subset (`dr_optima_correct`, `labels_htr_routes`). The enumeration of the reductions and their finishes is computed, not Lean.

**f. FakeMMAP's reduction bound and its multi-qt lower bounds** ([[T11502]]: "R is the max of the following", five families of terms, the sums "over all i's such that i, i+1 are both in S"; [[T11503]]: "M \geq \frac{|S|(R'+1)-N+\sum_{i edge} \alpha_i}{|S|-1}").

Of the lower bounds FakeMMAP wrote "I don't know how useful these bounds really are, I have to put in the numbers to see if there are situations where the typical bound is M \geq 11, rather than M \geq 7 lol." ([[T11504]]); this is that test (the write-up's section 9 gives the typical values). R as written is safe to use: the largest term is never too short, proved for every finish (`Rmax_sound`, lean/FakeBound/FakeBound/Formula.lean), but only because term 1, about M − 1, is among the terms, so it's loose. Two things in the formulas are wrong, each proved in Lean with a counterexample.

*The $\alpha$ index, in both messages.* Windows $i$ and $i+1$ share section $i+1$, so the section counted twice is $\alpha_{i+1}$, not $\alpha_i$ (`cover_sum`, FakeBound/Finish.lean).

- In the lower bounds: over {= n(E['t11503_counts']['cases']) =} sampled (state, corner path) cases at the optimum, the bounds as written were wrong in {= n(E['t11503_n']) =}: {= n(E['t11503_kinds'].get('first', 0)) =} times the first bound, {= n(E['t11503_kinds'].get('B', 0)) =} times the one with B. With $\alpha_{i+1}$ they were never wrong ({= n(E['t11503_counts']['violations_alpha_i_plus_1']) =} cases), and they're proved valid for every finish (`lower_free`, `lower_A`, `lower_B`, `lower_C`, FakeBound/Finish.lean).
- In the terms of the upper bound the same index makes a term too short (`alpha_i_fails`, FakeBound/Counter.lean): on the path 4b2 > 4a3 > 4b2 > 4a1 > 0c0, a 14-move finish with sections 2, 1, 3, 1, 3 needs a 9-move reduction, but the smallest term with $\alpha_i$ is 8. Under "max" that does no harm; under the smallest-term reading below it does.

Example for the index, corner path 0c4 > 4a3 > 4b2 > 4a1 > HTR, $N = 4$, $\alpha = 0, 1, 3, 1, 0$:

```
{= WIT('W13', 'scramble') =} // 0c4 0e, optimal {= WIT('W13', 'optimal') =}
{= WIT('W13', 'optimal_finish') =} // optimal finish
```

Its sections of half turns are {= ', '.join(map(str, SECTIONS(WIT('W13', 'optimal_finish')))) =}, its 1q reductions {= ', '.join(map(str, WINDOWS(WIT('W13', 'optimal_finish')))) =}, so all reductions shorter than R' = {= min(WINDOWS(WIT('W13', 'optimal_finish'))) =} fail. With $S = \{0, 2, 3\}$ the bound as written gives $M \geq {= f1(LB11503(9, 4, [0, 2, 3], [0, 1, 3, 1, 0])) =}$, so 15; with $\alpha_{i+1}$, {= f1(LB11503(9, 4, [0, 2, 3], [0, 1, 3, 1, 0], True)) =}, so 14, the optimum. *Lean-checked end to end*: the optimum, the finish, the subset, the corner path, $\alpha$, the sections, the reductions and both inequalities (`dr_optima_correct`, `dr_solutions_valid`, `labels_htr_routes`, `index_example`, `index_example_arith`, Corrections/Examples.lean).

*Term 2's signs, when R is the smallest term.* Every term is an upper bound on the reduction a finish needs, so the bound the derivation gives is the smallest term. With $\alpha_{i+1}$ and term 2 as derived it's sound for every finish (`Rmin_sound`, FakeBound/Formula.lean; it isn't always the exact worst case, `Rmin_not_tight`). Term 2 as printed, "\frac{(|S|-1)M-(N-|S|)+\sum_{i edge} \alpha_i}{|S|}", that is $\frac{(|S|-1)M-(N-|S|)+\sum_{i\ \mathrm{edge}} \alpha_i}{|S|}$, has both signs flipped: the derivation gives $\frac{(|S|-1)M + (N-|S|) - \sum \alpha}{|S|}$, and so does FakeMMAP's own first lower bound ([[T11503]]) solved for R'. With the printed term 2 the smallest term is too short: on a 10-move finish with sections 0, 3, 0, 4 (path 4a1 > 0c0 > 4a1 > 0c0) the reductions are 6, 6, 5, but printed term 2 with $S = \{0, 2\}$ gives 4, whatever A, B and C are, and still 4 with the printed $\alpha_i$ as well (`printed_term2_fails`, `literal_min_fails`, FakeBound/Counter.lean). In the sample it's too short on {= pc(Q9('opt', 'insuff_min_terms_as_written')) =} of cases at the optimum.

Example for the signs. Every optimal finish of this one takes the path 0c3 > 4a2 > 4a1 > HTR ($N = 3$, $\alpha = 0, 3, 3, 0$):

```
{= WIT('W14', 'scramble') =} // 0c3 2e, optimal {= WIT('W14', 'optimal') =}
{= WIT('W14', 'optimal_finish') =} // optimal finish
```

Its sections are {= ', '.join(map(str, SECTIONS(WIT('W14', 'optimal_finish')))) =}, so its 1q reductions are {= ', '.join(map(str, WINDOWS(WIT('W14', 'optimal_finish')))) =} and a 7-move reduction is needed. Term 2 as printed with S = {0, 2} gives {= f1(T2(14, 3, [0, 2], [0, 3, 3, 0])) =}, so 6; derived, {= f1(T2(14, 3, [0, 2], [0, 3, 3, 0], True)) =}, so 7. *Lean-checked*: the arithmetic from the sections on (`witness_0c3`). The state's optimum and its paths come from the exact table and the study's enumeration, not Lean.

*Fixed 12 Nov 2026.* Until then this entry also said that C, "the shortest possible HTR in the subset", must be the shortest NISS HTR. That was wrong. C bounds the middle of the finish, a linear HTR of a DR in the same subset (half turns keep the subset, proved in Lean: `labels_keep`), so FakeMMAP's linear C is right (section 9 of the write-up). The mistake was to bound the finish minus one middle section instead, which is a NISS HTR of the DR itself. Dropping the middle of the optimal finish leaves a 4-move NISS HTR, below the subset's shortest linear HTR of 5 (Lean-checked: `C_example`, `dr_optima_correct`):

```
F2 U' B2 R2 B2 U R2 // 0c0 2e, optimal 7
R2 U' B2 R2 B2 U F2 // optimal finish
B2 R2 B2 // its middle
R2 U' // what's left on normal
(F2 U') // and on inverse
```
