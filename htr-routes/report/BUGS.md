# Which HTR routes to try from a DR: corrections

*Goes with the write-up on which HTR routes to try from a DR, but reads on its own. The write-up has the measurements and the tables.*

November 2026. A date in brackets is a link to that message on the FMC solvers Discord (#fmc-theory, #fmc-discussion or #non-dr-discussion).

**What everything below is measured against:**

- **The exact optimal finish of every DR state** (all 19,508,428,800, from the first study, proved in Lean there), and the shortest linear HTR of every one of the 29,400 HTR cosets.
- **25,000 uniformly random DR states per subset × edges** (1,200,000 in all), each solved exactly: every optimal and +1 finish, every NISS reading, the shortest HTR on each side and with NISS, every reduction to 1q.

Every scramble and move sequence below was replayed on a sticker-level cube. Each item also says how much of its example is checked in Lean (the study's folder lean/FakeBound: Corrections/Examples.lean and the FakeBound files); the rest is computed, not proved. These are only the statements the numbers go against. Most of what was said holds up, and that's in the write-up's section 11.

---

**a. "Interesting that it seems 4qt 4C0E is the only HTR subset that is guaranteed 11 moves without NISS (I'm pretty sure 2C6E 5qt will be 10)"** (Jay, [29 Jan 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1069455768782385294), while filling in the last cases of the [*HTR subset WIP*](https://docs.google.com/document/d/1cQb_UMFvcVr4-SOR42u8gNMP9Ovx6WXxxUA5tolY8v0) doc; the bracket was settled soon after: "Turns out a 9 mover for 5qt 2C6E actually exists", [29 Jan 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1069462114693021726)).

Over all 29,400 HTR cosets: 4c4 0e ("4qt 4C0E") has linear HTRs of 10 moves, and the one subset whose shortest linear HTR is always 11 or more is 0c4 8e (fake HTR corners with 8 bad edges). Jay's doc, as it stands, lists that one at 11 too. The 10 was in Aedan Bryant's sheet (Aedan on Discord; [*HTR Subset Stats*](https://docs.google.com/spreadsheets/d/17iChOoeB205t3wHTXMLrjM9si2vtxRgFeYR2z3pn1i0), started the next day, [30 Jan 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1069557424949833759)): 34.1% of its "4qt 4C" states have one. Lewis Isom pointed that out in 2024 ([23 Jan 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1199494282223038485): "also under 4qt 4c0e the trigger given is 11 moves but stats say 10 is possible").

Example, with the linear HTR nissy finds on inverse:

```
D F2 R2 U2 B2 U' F2 U' F2 U L2 B2 U' R2 U' // 4c4 0e
(D R2 U R2 B2 U2 B2 U B2 U) (10) // linear HTR on inverse
```

*Lean-checked*, all of it: the subset, the 10-move linear HTR on inverse and that the printed one is valid, and that 0c4 8e is the only subset × edges whose shortest linear HTR is never below 11 (`htr_4c4`).

**b. "No, the maximum it takes is 12 moves linearly, and 11 moves using NISS. See HTR subset stats under fmc-stats for more info."** (Lewis Isom, [23 Jan 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1199490255921877022), answering whether DR to HTR takes at most 9, from Aedan Bryant's sheet.)

Both are one short. The sheet is a sample of 1,000 states per subset. Its own "3qt 4E" row (0c3 4e) already has 13-move linear HTRs, on 7.6% of its states, and 12 is its longest everywhere else. Its longest NISS HTR is 11 because the 12s are too rare to sample: a search over every DR state finds 64,128 states that need 12 (all 0c3 4e or 2c5), about 3 in a million, and none that needs more. Linearly, 0c3 4e and 4c4 0e have HTR cosets whose shortest linear HTR is 13, and some DRs need 13 on both sides. Lewis Isom doubted the sheet for other reasons a few minutes later ("its kinda hard to know what the correct info is imo", [23 Jan 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1199494282223038485)). Daichi named both 13s in 2026 ([14 May 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1504408526444040192): "0c3 4e and 4c4 0e have 13 move optimal HTR cases").

Example, with nissy's shortest HTRs:

```
B2 U B2 R2 D' L2 U B2 D' F2 D' L2 F2 U' R2 U // 0c3 4e, optimal 16
U R2 U B2 U' B2 U F2 U' R2 U B2 U (13) // shortest linear HTR, either side
U R2 U2 F2 U' F2 R2 U (B2 U L2 U) (12) // shortest with NISS
```

And a 4c4 0e with 13 on one side. On the other side it has the 10 of item a:

```
D L2 U2 F2 U' L2 D2 L2 F2 D' F2 L2 U L2 R2 // 4c4 0e, optimal 15
U R2 F2 U F2 U2 R2 U' L2 U2 R2 F2 D (13) // shortest linear HTR on normal
(U R2 U L2 B2 U2 F2 U R2 D) (10) // shortest linear HTR on inverse
```

*Lean-checked*, for the 0c3 4e: the optimum, the subset, the 13-move shortest linear HTR on each side, and that both printed HTRs are valid (`dr_optima_correct`, `htr_13`). That no NISS HTR of 11 exists is from nissy and two independent searches, and the 12 as the longest over every DR state from a search over the whole DR group; neither is Lean. The 4c4 0e's lengths are from the exact table, the sample's search and nissy, not Lean.

**c. "I like to check all sub-5 reductions. This can be done super quick and gets optimal like 75% of the time, and it gets optimal +1 the rest of the time", then "If I REALLY want to solve a DR optimally I'll check all sub-6 reductions"** (Levi Gibson, beef beans on Discord, [28 Nov 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1311670582601060354); "sub-5" is "4 or less", [29 Nov 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1312051485760163880)).

Just before, Levi Gibson wrote "for the 4a2 subset I use full DR Bounding" ([28 Nov 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1311669869900464138)), and a few minutes later "I don't use it fully for any subsets other than 4a2 and 2c3" ([28 Nov 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1311671487379279872)). So: write every reduction to 1q of at most 4 moves, on normal, on inverse and split by NISS, and finish each reduced state optimally, with any number of quarter turns (sampled, 4,000 states per subset × edges).

| Subset | Optimal | Within +1 | Reductions on average |
|---|---|---|---|
| 4a2 | 76.6% | 93.6% | 207 |
| 2c3 | 48.1% | 78.8% | 140 |
| 2c3 2e | 52.1% | 80.2% | 146 |
| 2c3 4e | 46.2% | 77.3% | 138 |

On 4a2 the 75% holds, but "+1 the rest of the time" doesn't. On 2c3 both fall short. With every reduction of at most 5, the "sub-6" of the second sentence, it's 80.0% on 4a2 and 71.1% on 2c3.

Yura Riabov called the split in the same exchange: "i think it could be very good for 4a2 but for 2c3 trigger knowledge covers most cases" ([28 Nov 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1311671177948823554)), and of 2c3 2e, "<3 half turns> U R2 U R2 U <5 half turns> often enough, and bounding won't catch that i think" ([28 Nov 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1311673888832487506)). Levi Gibson agreed that "missing lots of half turns into a trigger is the blind spot that DR Bounding has" ([28 Nov 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1311674439833751573)), and on 2c3 2e and 4e adds triggers: "For 2c3 2e and 4e I do full DR Bounding + checking the 5-move triggers, and that seems to catch everything" ([28 Nov 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1311674286389334026)). The triggers aren't measured here, so this corrects the share for bounding alone. Levi Gibson's later answer to "Would it be around 80 percent?" for 2c3 was a guess ("yeah something like that I'd guess", [29 Nov 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1312051081831780434)), with the advice to check "a bunch of half turns into a 5-move trigger" as well ([29 Nov 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1312051209158525018)).

Example, 12 optimal. I enumerated all 168 different states reached by a reduction to 4a1 4e of at most 4 moves on the sticker model and finished each optimally from the exact table: the best total is 14, optimal + 2. The optimal needs a 5-move reduction:

```
R2 B2 D2 B2 D U2 R2 U L2 F2 U' B2 // 2c3 2e
B2 U F2 L2 U' // reduction on normal
R2 U2 D' B2 D2 B2 R2 // then the rest
```

*Lean-checked*: the optimum and the subset (`dr_optima_correct`, `labels_htr_routes`). The enumeration of the reductions and their finishes is computed (twice, independently), not Lean.

**d. FakeMMAP's reduction bound and its multi-qt lower bounds** ([8 Apr 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1491531409959948369): "R is the max of the following", five families of terms, the sums "over all i's such that i, i+1 are both in S"; [8 Apr 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1491533155201716475): "M \geq \frac{|S|(R'+1)-N+\sum_{i edge} \alpha_i}{|S|-1}").

Of the lower bounds FakeMMAP wrote "I don't know how useful these bounds really are, I have to put in the numbers to see if there are situations where the typical bound is M \geq 11, rather than M \geq 7 lol." ([8 Apr 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1491533429198553178)); this is that test (the write-up's section 9 gives the typical values). R as written is safe to use: the largest term is never too short, proved for every finish (`Rmax_sound`, lean/FakeBound/FakeBound/Formula.lean), but only because term 1, about M − 1, is among the terms, so it's loose. Two things in the formulas are wrong, each proved in Lean with a counterexample.

*The $\alpha$ index, in both messages.* Windows $i$ and $i+1$ share section $i+1$, so the section counted twice is $\alpha_{i+1}$, not $\alpha_i$ (`cover_sum`, FakeBound/Finish.lean).

- In the lower bounds: over 1,914,809 sampled (state, corner path) cases at the optimum, the bounds as written were wrong in 923: 904 times the first bound, 19 times the one with B. With $\alpha_{i+1}$ they were never wrong (0 cases), and they're proved valid for every finish (`lower_free`, `lower_A`, `lower_B`, `lower_C`, FakeBound/Finish.lean).
- In the terms of the upper bound the same index makes a term too short (`alpha_i_fails`, FakeBound/Counter.lean): on the path 4b2 4a3 4b2 4a1 0c0, a 14-move finish with sections 2, 1, 3, 1, 3 needs a 9-move reduction, but the smallest term with $\alpha_i$ is 8. Under "max" that does no harm; under the smallest-term reading below it does.

Example for the index, corner path 0c4 4a3 4b2 4a1 HTR, $N = 4$, $\alpha = 0, 1, 3, 1, 0$:

```
D2 F2 L2 U' B2 U' L2 U2 B2 U' L2 D R2 D2 // 0c4 0e, optimal 14
D2 R2 D' L2 U B2 U2 L2 U B2 U L2 F2 D2 // optimal finish
```

Its sections of half turns are 2, 1, 3, 1, 3, its 1q reductions 10, 9, 9, 9, so all reductions shorter than R' = 9 fail. With $S = \{0, 2, 3\}$ the bound as written gives $M \geq 14.5$, so 15; with $\alpha_{i+1}$, 13.5, so 14, the optimum. *Lean-checked end to end*: the optimum, the finish, the subset, the corner path, $\alpha$, the sections, the reductions and both inequalities (`dr_optima_correct`, `dr_solutions_valid`, `labels_htr_routes`, `index_example`, `index_example_arith`, Corrections/Examples.lean). The same finish shows the index error in the upper bound: its sections are those of the path above and so are $\alpha_2 = 3$ and $\alpha_3 = 1$, so with $\alpha_i$ term 2 for $S = \{0, 2, 3\}$ again gives 8.7, so 8, against the 9-move reduction the finish needs.

*Term 2's signs, when R is the smallest term.* Term 2 of the upper bound and the first of the lower bounds ([8 Apr 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1491531409959948369), [8 Apr 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1491533155201716475)) are one inequality, solved for R and for M, and they come out with opposite signs. The derivation gives the lower bound's signs. Term 2 as printed, "\frac{(|S|-1)M-(N-|S|)+\sum_{i edge} \alpha_i}{|S|}", that is $\frac{(|S|-1)M-(N-|S|)+\sum_{i\ \mathrm{edge}} \alpha_i}{|S|}$, has both signs flipped: the derivation gives $\frac{(|S|-1)M + (N-|S|) - \sum \alpha}{|S|}$, which is FakeMMAP's own first lower bound solved for R'. This matters when R is the smallest term. Every term is an upper bound on the reduction a finish needs, so the bound the derivation gives is the smallest term, and FakeMMAP's own aside on term 1, "unlikely to be the maximum, unless M is VERY small" ([8 Apr 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1491531409959948369)), is true of the smallest term and false of the largest. With $\alpha_{i+1}$ and term 2 as derived it's sound for every finish (`Rmin_sound`, FakeBound/Formula.lean; it isn't always the exact worst case, `Rmin_not_tight`). With the printed term 2 the smallest term is too short: on a 10-move finish with sections 0, 3, 0, 4 (path 4a1 0c0 4a1 0c0) the reductions are 6, 6, 5, but printed term 2 with $S = \{0, 2\}$ gives 4, whatever A, B and C are, and still 4 with the printed $\alpha_i$ as well (`printed_term2_fails`, `literal_min_fails`, FakeBound/Counter.lean). In the sample it's too short on 9.2% of cases at the optimum (each subset × edges weighted by its size; 172,497 of the 1,914,809 cases, 9.0%, before weighting).

Example for the signs. Every optimal finish of this one takes the path 0c3 4a2 4a1 HTR ($N = 3$, $\alpha = 0, 3, 3, 0$):

```
F2 D2 R2 D' R2 U2 B2 D' L2 U2 F2 U L2 R2 // 0c3 2e, optimal 14
R2 L2 U' F2 U2 L2 D B2 U2 R2 D R2 D2 F2 // optimal finish
```

Its sections are 2, 3, 3, 3, so its 1q reductions are 8, 7, 7 and a 7-move reduction is needed. Term 2 as printed with S = {0, 2} gives 6.5, so 6; derived, 7.5, so 7. *Lean-checked*: the arithmetic from the sections on (`witness_0c3`). The state's optimum and its paths come from the exact table and two independent enumerations, not Lean.

*Fixed 12 Nov 2026.* Until then this entry also said that C, "the shortest possible HTR in the subset", must be the shortest NISS HTR. That was wrong. C bounds the middle of the finish, a linear HTR of a DR in the same subset (half turns keep the subset, proved in Lean: `labels_keep`), so FakeMMAP's linear C is right (section 9 of the write-up). The mistake was to bound the finish minus one middle section instead, which is a NISS HTR of the DR itself. Dropping the middle of the optimal finish leaves a 4-move NISS HTR, below the subset's shortest linear HTR of 5 (Lean-checked: `C_example`, `dr_optima_correct`):

```
F2 U' B2 R2 B2 U R2 // 0c0 2e, optimal 7
R2 U' B2 R2 B2 U F2 // optimal finish
B2 R2 B2 // its middle
R2 U' // what's left on normal
(F2 U') // and on inverse
```
