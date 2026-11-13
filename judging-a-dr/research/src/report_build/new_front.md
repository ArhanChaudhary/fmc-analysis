# Judging a DR by hand: what the full BFS says

What you can read off a DR, how much each read says about the finish, and which lower bounds hold, measured on the whole DR group: I BFSed all 19,508,428,800 states, so nothing below is sampled.

November 2026. A name with a date is a link to that message on the FMC solvers Discord (#fmc-theory or #fmc-discussion). Docs and sheets are listed with links at the end.

**This builds on** the bounding docs and tables people already use:

- **Levi Gibson's [DR Bounding](https://docs.google.com/document/d/1q7rig4GEo26GunBMtuagZdGyzyjCGlduH84CHLpGLSA)** and **Rodney Kinney's [Advanced DR Bounding [Beta]](https://docs.google.com/document/d/13F8HonrKJyHjU9EwfiHDRyY4X77vPriYeaVSrh5guq0)**: DR bounding by hand, which this study tries to take to 3qt, 4qt and 5qt (section 1). Levi's formula and the worked examples of both docs are checked here, and Rodney's NISS@1qt features are the basis of section 7. On the server Levi posts as beef beans; this page says Levi.
- **Rodney Kinney's sheet [Adv DR Bounding](https://docs.google.com/spreadsheets/d/1jRvikzLlm3yHlDQmQ0DLyj3Aw6uinL3Oa-U9_U7R5mY)**: the bounding rules against the 216 computed cases, checked in section 9.
- **FakeMMAP's 216-case tables**: the half-turn-only values ([[T12061]]), the HTR-breaking table ([[T12175]]) and the sheet [OBL++](https://docs.google.com/spreadsheets/d/1kax7evfA85p_4ArXKO7si3FrCpj7PEeFwoz4GY5wRAE), all checked in section 9; and FakeMMAP's corner counts per qt.
- **Joba's optimal distribution for all 48 subsets** ([[T9115]]), matched here in every cell, and **Mallard** ([cubelib](https://github.com/Jobarion/cubelib)), whose table is built from the same 48 subsets.
- **wen's sheet [HTR better smh (v2)](https://docs.google.com/spreadsheets/d/1ZhulzHeNgv2Hiy4x9R1MzsMRlPlI-E8DRiHFJlPlboM)**: the corner subsets, with 4a3 and 4b3 swapping on inverse.
- **trangium's "true 2q bound"** ([[T11428]]), good "if you don't use extra qts", taken to any qt in section 5.
- **Levi Gibson's sheet [Corner Solution Length x DR Finish length](https://docs.google.com/spreadsheets/d/14rZI1Nf84Og1jS8dN1MfT0sYhvdIWu9gPXkHDs1iVU4)**: sampled; Appendix B is the exact version.

**What this adds**: the exact numbers for the reads a solver can make by hand.

- **A guide per subset**: for each of the 12 corner subsets, how often it finishes in 10, 11 and 12, what to read, when to drop it for the finish you need, what not to conclude.
- **Every read against the exact finish**, for each finish you might need from 9 to 13: ranking, throwing away, plain rules with their price, what is proven.
- **What each read is worth**: subset, pairs, corner case on both sides, HTR length on both sides, corner length and E-slice parity, the last DR move.
- **The bounds people use, graded**: Levi's formula, trangium's 2q bound at any qt, HTR length, the parity bound. Which never fail, how often the others do.
- **What a computer can prove from the DR**: table lookups that prove "no 12" for most 4–5qt DRs and "no 11" for nearly all, and why no hand read gets there.
- **The 216 NISS@1qt cases, three ways**: FakeMMAP's and Rodney's tables checked with half turns, with DR moves and with any move.
- **A Lean proof** of the optimal finish of every DR state, so every stat here is a count over proven optimals.

**Terms**, as the server uses them. "Optimal" is the shortest finish in DR moves (U, D, R2, L2, F2, B2), and "in 11" means an optimal finish of 11 or less. Bad corners and edges are counted the way the server counts them, up to turning a layer: the Q in 2c**4** is the corner qt count, the 4e in 2c4 4e the number of bad edges, and 4c3 = 4a3 and 4b3 together (they swap on inverse), same for 4c4. *Pairs* are true pairs: corner and edge next to each other in the U or D layer, both touching stickers matching. Every count treats each DR state as equally likely.

## 0. The short version

The finishes that matter are 10 and 11, which is what an 11- or 12-move DR needs (why is under **Which finish** in section 1).

What is new here:

- **Some DRs are dead on sight, no solving needed.** By where the bad corners sit on normal and on inverse. Each row is a layout, with the finish it never reaches, its odds for an 11 and a 12 where they aren't zero, and its fastest finish:

  | Bad corners | Never finishes in | In 11 | In 12 | Fastest, moves |
  |---|---:|---:|---:|---:|
  | 2c5, stacked on both sides | 12 | | | {= pv.fastest(LAYH('2c5', 'stacked', 'stacked')) =} |
  | the same subset, stacked on one side and opposite on the other | 11 | | {= pv.pct(LAYH('2c5', 'stacked', 'opposite'), 12) =} | {= pv.fastest(LAYH('2c5', 'stacked', 'opposite')) =} |
  | 2c4, stacked on both sides | 10 | {= pv.pct(LAYH('2c4', 'stacked', 'stacked'), 11) =} | {= pv.pct(LAYH('2c4', 'stacked', 'stacked'), 12) =} | {= pv.fastest(LAYH('2c4', 'stacked', 'stacked')) =} |
  | 4a2 2e, all four bad corners on one layer on both sides | 12 | | | {= pv.fastest(LAYH('4a2', '4-0', '4-0', 2)) =} |

  The first two rows are {= SH('2c5', [a + b for a, b in zip(LAYH('2c5', 'stacked', 'stacked'), LAYH('2c5', 'stacked', 'opposite'))]) =} of all 2c5, and the third is as dead as a 5qt. The fastest double-stacked 2c4 and 2c5 are in section 4.3.
- **A five-line prune list for an 11-move DR that needs no solving** (section 8). What it does in each qt group:

  | Share of the group | 1–2qt | 3qt | 4qt | 5qt |
  |---|---:|---:|---:|---:|
  | DRs it drops | {= PRUNE('drop',11,'1-2qt') =} | {= PRUNE('drop',11,'3qt') =} | {= PRUNE('drop',11,'4qt') =} | all |
  | finishes in 11 it loses | {= PRUNE('lose',11,'1-2qt') =} | {= PRUNE('lose',11,'3qt') =} | {= PRUNE('lose',11,'4qt') =} | {= 'all' if PRUNE('lose',11,'5qt') == '100%' else PRUNE('lose',11,'5qt') =} |

  Over all DR states it drops {= PRUNE('drop') =} and keeps {= PRUNE('keep',11) =} of the 11s and {= PRUNE('keep',10) =} of the 10s. On real scrambles, {= ATT('have') =} of {= ATT('n') =} random ones (those with an EO-first DR of 10 or less), each row is what you finish:

  | What you finish | Best solution, average moves | DRs per scramble |
  |---|---:|---:|
  | every DR of 10 or less, plus only the 11-movers the list keeps | {= ATT('res_kept') =} | {= ATT('drs_kept') =} |
  | the same, but every 11-mover | {= ATT('res_all') =} | {= ATT('drs_all') =} |

  That table finishes every DR optimally, so it's **computer only**, the answer key for what the list costs. What you take into an attempt is the list itself, which needs no solving.
- **For a 10 or an 11, the subset does most of the pruning.** Share of DRs that finish, by qt group:

  | Finishes | 1–2qt | 3qt | 4qt | 5qt |
  |---|---:|---:|---:|---:|
  | in 11 | {= pv.pct(q(group='1-2qt'), 11) =} | {= pv.pct(q(group='3qt'), 11) =} | {= pv.pct(q(group='4qt'), 11) =} | {= pv.pct(q(group='5qt'), 11) =} |
  | in 10 | {= pv.pct(q(group='1-2qt'), 10) =} | {= pv.pct(q(group='3qt'), 10) =} | {= pv.pct(q(group='4qt'), 10) =} | {= pv.pct(q(group='5qt'), 10) =} |
- **Still no clean yes/no: tseitsei89's "100% cases and 0% cases" don't exist at any target.** The subset explains {= VAREXP('sub') =} of the variance of the optimal, everything readable together (subset, pairs, corner case and HTR length on both sides, L and E-parity) {= VAREXP(*ALLREADS) =}, and what's left has an sd of {= SDLEFT(*ALLREADS) =} moves. Zagros hypothesized that corner case + HTR on both sides gives the optimal "with a standard deviation of like 0.25 moves" ([[T11482]]); tested, it's {= SDLEFT('ccn', 'cci', 'hn', 'hi') =}. Two 2c4 4e with the same corner case on both sides, 7 to HTR on both sides and the same corner length finish in 7 and in 16 (section 3). The sd figures are **computer only**: they measure the reads over every DR state, nothing you work out in an attempt. What you use there are the odds each read gives, in the guide per subset.
- **The lower the target, the more the reads tell you, and the free reads tell the most.** Keep only the best-looking quarter of a qt group, going by pairs and corner case (no solving needed). Share of the finishes you keep:

  | Finishes in | 3qt | 4qt |
  |---|---:|---:|
  | 12 | 52% | 65% |
  | 11 | 63% | 77% |
  | 10 | 74% | 89% |

  From 3qt up, pairs plus corner cases rank better than the two HTR lengths at every target from 10 up, and the HTR lengths on top add 3 to 7 points for a 10 or an 11, 1 to 2 for a 12, and about 1 or less for a 13. At 1–2qt it's the other way round: HTR length is the best single read. These shares rank DRs by the exact odds of every combination of reads, a table of thousands of classes, so they're **computer only**: a ceiling for what a rule built on those reads can do. The versions you carry are the prune list above and the plain rules below.
- **Plain rules, with their price.** Zagros's rule ("4c3 that is 9+ on both sides I throw away"), turned into a rule against your target T. For an 11, each row is a rule, with the share of 3qt and 4qt DRs it drops and the share of their 11s it loses:

  | Rule | DRs dropped, 3qt | DRs dropped, 4qt | 11s lost, 3qt | 11s lost, 4qt |
  |---|---:|---:|---:|---:|
  | safe: $T-1$ or more to HTR on both sides (10+ for an 11) | {= HRULE('3qt', 10, 'drop') =} | {= HRULE('4qt', 10, 'drop') =} | {= HRULE('3qt', 10, 'lose') =} | {= HRULE('4qt', 10, 'lose') =} |
  | aggressive: $T-2$ or more (Zagros's 9+ when you need an 11) | {= HRULE('3qt', 9, 'drop') =} | {= HRULE('4qt', 9, 'drop') =} | {= HRULE('3qt', 9, 'lose') =} | {= HRULE('4qt', 9, 'lose') =} |

  With no solving, dropping every DR without a pair drops {= pv.num(max(NOPAIR('drop'))) =} at every qt and loses {= RANGE(NOPAIR('lose')) =} of the 11s.
- **For judging a DR, count true pairs and stop.** What one more pair multiplies the odds of an 11 by, per corner subset:

  | 4a1 | 2c4 | 2c5 |
  |---:|---:|---:|
  | {= PPR('4a1', 11) =} | {= PPR('2c4', 11) =} | {= PPR('2c5', 11) =} |

  A 2c4 with five or more pairs finishes in 11 {= {'16': 'sixteen'}.get(P05('2c4', 11), P05('2c4', 11)) =} times as often as one with none ({= pv.pct(q(cs='2c4', pairs=5), 11) =} against {= pv.pct(q(cs='2c4', pairs=0), 11) =}). Adding pseudo-pairs and semi-pairs moves the sd left from {= SDPAIRS(1) =} to {= SDPAIRS(4) =} (an sd over every DR state, **computer only**). The pair count is the same on inverse for every DR state, so count once.
- **Inside a subset the corner case on both sides is a big read.** For 2c4, each row is a corner case (on both sides for the first two), with the share finishing in 10, 11 and 12 or less:

  | Corner case | In 10 | In 11 | In 12 |
  |---|---:|---:|---:|
  | the best layout, on both sides | {= CELLS(C2('2c4', '8', '8')) =} |
  | a stack on both | {= CELLS(tri(LAYH('2c4', 'stacked', 'stacked'))) =} |
  | one of the two 2c4 cases with the same bad corners | {= CELLS(C1('2c4', '8')) =} |
  | the other one | {= CELLS(C1('2c4', '7')) =} |

  The last two are told apart by the diagonals of the back face (section 4.3). At 3qt stacked is the *best* layout; at 4qt and 5qt it's the worst. In 4b2 (3-1) and 4c3 (4-0) two cases look the same, and only the optimal corner solution separates them.
- **The two guaranteed hand bounds wake up at low targets.** The longer HTR, and the corner solution with the right E-parity (the number of side turns in any finish has the parity of the E-slice: Rodney's fr-parity used on the whole finish). They prove almost nothing for a 12 (5% of 4qt DRs, 13% of 5qt). For a 10 they rule out half of 4qt and 80% of 5qt DRs.
- **trangium's 2q bound, taken to any qt, is as good as a true bound from 3qt up.** On each side: fewest half turns before a quarter turn lowers the qt count, plus the shortest HTR of the other side. How often a finish with extra quarter turns gets under it, by qt group:

  | 1–2qt | 3qt and up |
  |---:|---:|
  | 2.6% | 0.002% |

  Section 5 has a scramble for each of the 13 subsets where it happens. At 3qt it rules out 19% of DRs for a 10 and 6% for an 11, more than the two proven bounds together.
- **Levi's formula, measured.** It bounds every finish with one quarter turn, as Levi's doc says. Examples for the rest are in section 5.
  - A finish with three quarter turns is shorter for 11.7% of 4a1 4e, and for 2.5% when the formula says 12 or less.
  - For 72 of the 432 cases of 4a1 4e (one in six) the shortest HTR is a 3qt one, and the formula wants the shortest 1qt length.
  - Against the real leave slice (count quackula's question) it's +0.70 on average and too high 19.7% of the time.
- **How far off they all sit.** The guaranteed bounds you can compute by hand are on average four moves under optimal.
- **A last DR move you can turn the other way is worth about a third of a move**: {= LASTMOVE('gain') =} on average, from {= LASTMOVE('lo') =} to {= LASTMOVE('hi') =} by subset (Zagros's question). At 3qt it takes the share finishing in 11 from 4.6% to 7.5%.
- **Where the information is.** Rodney's NISS@1qt features read straight off the DR state give a bound at any qt with no skeleton: on HTR states with half turns only it *is* FakeMMAP's 216-case table, at the DR it has 6,350,400 cases. With the H-perm parity and the real colours added it's exact 44% of the time and within one 86%, and it proves Rodney's 4a4 13-mover optimal from the DR alone. What a computer gets against what you can read, as a share of 4qt and 5qt DRs:

  | What it is | 4qt DRs | 5qt DRs |
  |---|---:|---:|
  | corners exactly plus the edge colours: proves "no 12" | 81% | 95% |
  | the same: proves "no 11" | 97% | 99% |
  | everything readable put together: under 1% for a 12 | {= DEAD('4qt', 12) =} | {= DEAD('5qt', 12) =} |

  The gap is the corner–edge relation, which is what Rodney's NISS@1qt tracing looks at. No count of visible features replaces it. All three rows are **computer only**: NISS@DR is a lookup in millions of cases, and "everything readable put together" ranks by the exact odds of every class of reads. They show where the information is. In an attempt the version you have is Rodney's tracing, per skeleton.
- **Exact numbers that were guesses.**
  - The shortest HTR at 1 to 5 corner qts is 1 / 3 / 5 / 7 / 9 on one side. With NISS it gets down to 1 / 2 / 4 / 6 / 8, the lower bound Joba was assuming (section 4.1).
  - Only four subsets ever need 18: 0c0 8e, 0c3 4e, 2c5 0e and 2c5 4e. To leave the slice it's the last three, which is how zakimoshi remembered the 18s (section 4.1).
  - The slice is free (finish = leave slice) for 73% of DRs, from 56% at 1–2qt to 85% at 5qt. **Computer only**: it needs the optimal finish and the optimal leave slice.
  - A DR whose optimal is 10 or 11 has exactly one optimal first move three times in four. **Computer only**, from the optimal finish of every state.
  - 0c3 is the worst subset on average (14.46), worse than 5qt, and 4a2 2e and 0e finish like a 2c4.
- **Questions from the server, answered exactly**: stats by bad corner position (Daichi, JTuu, wen), by pairs (Rodney, Levi), the normal × inverse HTR table (Zagros), the 4a1 4e bound against the real leave slice (count quackula), the cost of the slice and the width of a DR (JTuu), an invertible last move (Zagros), error stats for bounding (compLex), God's number per subset (compLex), optimal lengths of all corner cases (Evan).
- **Proven in Lean**: the optimal finish of every DR state (so every stat here is a count over proven optimals) and its maximum of 18, the HTR and corner-length-with-parity bounds, the 216 HT-only values, a 4a1 4e where a 3qt finish beats Levi's formula, and the stated optimal of the example scrambles in this write-up (section 10 lists which, and what else).

What it confirms or corrects in the docs and sheets people use:

- **FakeMMAP's HTR-breaking table is right in 211 of 216 cells.** Two cells labelled 7 are 6-movers, which goes against "Anything labeled with 7 or less is proven to be a lower bound, and the lower bound is proven optimal" ([[T12129]]). Three of the 9s, which FakeMMAP left unproven, are 8. Rodney's "Adv DR Bounding" sheet's penalties are built on the same optimals, so the same five are one too high, plus one alg with R2 for F2. Rodney's rules stay a true lower bound in all 216. A state of each case is in section 9.
- **FakeMMAP's HT-only table is not a bound once other moves are allowed**, as FakeMMAP said: with U and D quarter turns 2 of the 216 values drop from 9 to 8 (the count is proven in Lean), with any face turn 66 drop (section 9).
- **OBL++**, collapsed to the 216 labels, matches on 140 of the 144 cases it covers and is one lower in four. nissy finds no 8 in any of the 3,072 states of each of those four, so 9 stands for the cases as labelled here.
- **Zagros's "4c3 that is 9+ on both sides I throw away"** drops half of all 4c3 and keeps 92% of the 10s, 83% of the 11s and 73% of the 12s. It does throw away real finds: one 9 to HTR on both sides finishes in 9 (section 4.4).
- **Zagros's hunch** that optimal corner length and longest direct HTR "might have a low standard deviation. Like it is possible you could consistently predict the opt finish length within ~1 move based on those two things" ([[T6905]]): 93.3% of DRs are within one move of the typical finish for their subset and those two, but the subset alone does that for 91.3%.
- **Levi's question** ([[T6965]]), "has anyone noticed that blocky 2c4s are way better than not-so-blocky 2c4s? Idk if this is confirmation bias but it seems like block matter a lot more than with other DRs": blocky 2c4s are better, the ×16 above. Whether blocks matter more than with other DRs depends on the others: more than at 4a1 (×{= P05('4a1',11) =}) and 2c3 (×{= P05('2c3',11) =}), less than at 2c5 (×{= P05('2c5',11) =}).
- **wen's "luckily they are all(?) 0c3 or 5q shit so you realistically will never get them"**, on the DRs with the longest finishes ([[T6881]]): {= TOP(18, 'worst') =} of the states at 18 are 0c3 or 5qt, {= TOP(17, 'worst') =} of those at 17 or more, and {= TOP(16, 'worst') =} of those at 16 or more, where the biggest share is 4c4 (section 4.1).
- **Rodney's two worked examples** in the Advanced DR Bounding doc are optimal 13s (**computer only**, a table lookup: the answer key), and Levi's "14-move optimal finish, giving a 24" in the DR Bounding doc holds: the 24 either way, the 14 with the last DR move turned the other way (section 7).
- **Checked and matching**: Joba's optimal distribution for all 48 subsets, in every cell; FakeMMAP's corner counts per qt; the 1,352 states at 18 that Reid gave (section 11).
- The errata page that goes with this doc has the rest: two typos in Rodney's doc, the longest DR→HTR (13, not 12) and how many subsets reach 18 (four, not five), each with a scramble.

---

## 1. What people asked for

**Bounding at high qt.** With a computer, DR bounding works at any qt. Look at part of the DR, tabulate the fewest moves that solve that part, and you have a lower bound at any qt with no skeleton. With the right table it proves "no finish in 12" for 59% of 5qt DRs and "no finish in 11" for 94% (section 7). The catch is that the tables have millions of cases, so that's **computer only**: nobody can use them in an attempt, and the bar on the server is clear:

> "is the lower bound fast to determine by human methods? If it takes too long to figure out the lower bound, you can just as well try to actually solve the DR" ([[T9871]])

> "I don't expect anyone to use the decision trees directly. I'm just hoping to use them to find the most important 2-3 features for each DRM, then make some simple rules out of just those features" ([[T8337]], said of the DRM decision trees; the same bar applies here)

So the question that matters is the human one. Take what you can actually read off a DR (subset, pairs, corner case, HTR length on both sides, corner solution length, E-slice parity) and measure exactly what each one tells you about the finish.

The gap, in the words of the people who bound in real solves:

- Levi uses it at 2q and 3q. At 4q: "Too many variations unfortunately. It kinda works with 4q, but it is slower than just checking reductions to 2c3" ([[D10081]]). And: "If there are other metrics (i.e blocks, HTR patterns, etc) that you can bound 2q cases with that would be incredible" ([[T7084]]).
- Rodney: "+3 or lower penalties are really quite rare … That's what makes 4qt cases so intractable currently" ([[T12094]]).
- tseitsei89: "Being able to quickly tell when a DR has a short finish would be a real holy grail" ([[T10831]]). tseitsei89's test for a good stat: "Optimally you would only have 100% cases and 0% cases" ([[T8208]]).

And the specific questions, each with a section below:

| Asked | By | Where |
|---|---|---|
| Can Levi's and Rodney's DR bounding be pushed to 3qt, 4qt and 5qt DRs, so you can toss a DR because its bound is high instead of wasting time on it? | Levi, Rodney and tseitsei89 (quoted above) | §3, §7 |
| Corner case + HTR on normal + HTR on inverse "can tell you the optimal solution with a standard deviation of like 0.25 moves"? | [[T11482]] | §3 |
| Stats by optimal corner length and longest direct HTR: "I believe this stat might have a low standard deviation. Like it is possible you could consistently predict the opt finish length within ~1 move based on those two things" | [[T6904]], [[T6905]] | §3 |
| A square table, moves to HTR on both sides. "4c3 that is 9+ on both sides I throw away" | [[T11190]] | §4.4 |
| "I suspect, however, that you won't get very clean stats from just the corner case plus bad edge count. You would need to break cases down by some kind of pair counts." | [[T11478]] | §4.2 |
| "has anyone noticed that blocky 2c4s are way better than not-so-blocky 2c4s?" | [[T6965]] | §4.2 |
| "stats on just bad corner positions for each subset", good/bad parity, on both sides | [[D17577]], [tseitsei89](@D17579) | §4.3 |
| "stats on 4c3 that take 4a3 corner position/parity into account?" | [[D18667]] | §4.3 |
| Average optimal of the 2c4 layouts: "double stack vs single stack vs no stack" | [[T12423]] | §4.3 |
| "is there a doc with optimal lengths for all corner cases?" | [[D16938]] | Appendix E |
| "average difference between a 4a1 4e bound and the actual leave slice? And how likely it is to be +0, +1, +2" | [[D16164]] | §5 |
| "anybody know if there are publicly available statistics for the errors on bounding? ie, if bounding says >= +8 to slice, what's the distribution of actual optimal solutions for that 1q reduction?" | [[T7177]] | §5 |
| trangium's "true 2q bound", good "if you don't use extra qts": how good is it? And bpaul: "actually doesn't this work for any number of quarter turns?" | [[T11428]], [[T11454]] | §5 |
| "it's prob not that important but do we know probability distribution of +N to solve slice given #qt in the htr section?" | [[D7946]] | §6 |
| "how does the optimal change from a pure DR vs. a DR in a solve where you have one move you can invert?" | [[T11467]] | §4.6 |
| The "width" of a DR | [[T11473]] | §6 |
| "are god's numbers known for htr subsets?" | [[T9096]] | Appendix A |

**Which finish.** A 9- or 10-move DR gets checked whatever it looks like. The DRs worth pruning are the 11- and 12-movers, and what they need is a finish in 10 or 11 (one more if the first finish move merges with the last DR move). So every table gives the share finishing in 10, 11, 12 and 13 or less, and the pruning is measured at each target from 9 to 13.

---

## 2. The data

- **Optimal finish of every DR state.** BFS of the group ⟨U, D, R2, L2, F2, B2⟩, all 19,508,428,800 states. "Optimal" means the shortest finish with those ten moves, same as nissy's `drudfin` and Joba's table. Average 13.58, max 18.
- **Optimal leave slice of every DR state.** Same thing ignoring the E-slice: fewest DR moves that solve corners and the eight U/D-layer edges. Average 13.29, and the max is 18 as well:

  ```
  U2 L2 D B2 U' B2 U' L2 D B2 R2 U R2 U R2 U2 R2 U'   // needs 18 for the leave slice and 18 for the full finish
  ```
- **Every count treats each DR state as equally likely.** That is also close to how the DRs you reach are spread. On the EO-first DRs of at most 11 moves that cubelib finds on {= '{:,}'.format(GAPS()['scr']) =} random scrambles, every corner subset's share is within {= '%.1f' % GAPS()['share'] =} points of the share here and its average optimal within {= '%.2f' % GAPS()['mean'] =} moves. What differs is the bad-edge mix inside a subset (section 12), so the edge-count cells are uniform-state numbers.
- Bad corners and edges are counted the way the server counts them, up to turning a layer. The Q in 2c**4** is the corner qt count. 4c3 = 4a3 and 4b3 together (they swap on inverse), same for 4c4. That's not how many qts the finish needs: 0c0 0e has states like `U D'` that need two, every 0c0 with bad edges needs two, and 4a1 0e and 4a1 2e need three:

  ```
  D F2 R2 F2 D          // 0c0 2e
  D' F2 R2 F2 D'        // solved by
  D F2 U' B2 F2 D'      // 4a1 2e
  D F2 B2 U F2 D'       // solved by
  U L2 R2 U L2 R2 U'    // 4a1 0e
  U R2 L2 U' R2 L2 U'   // solved by
  ```

  Mallard keeps both numbers (`qt_corners` and `qt`). Mallard and Joba's files say `4c5` where wen's "HTR better smh (v2)" sheet and most people say `4b5`: same 48 of 420 cosets.
- The 48 subsets are double cosets of ⟨half turns, U D⟩ merged with their inverses, as KrzychXyz said ([[T6648]]), which is how Mallard builds its table (https://github.com/Jobarion/cubelib); the 29,400 one-sided cosets decide HTR length. Built that way, all 48 sizes match Joba's.
- Daichi's "90+% of 4b2 0e cases are 12-14 optimal" ([[T11457]]): 92.1%.
- "In 11" always means an optimal finish of 11 moves or fewer. A cell that says 0 means no state at all; "<0.01%" means a few.

How it was checked, and what's proven, is in sections 10 and 11.

---

## 3. How much can a read tell you?

**Which finish you need.** Your result is the DR length plus the finish (one less if the first finish move merges with the last DR move). A 9- or 10-move DR gets a look whatever it is, and a 12 from it is a good result. The DRs you want to prune are the 11- and 12-movers, and those need a 10 or an 11. So this section measures everything for each target from 9 to 13.

How rare each target is. Each row is a corner subset, or in bold a corner-qt group; after its share of all DR states come the shares of its DRs whose optimal finish is 8 or less, 9 or less, and so on:

{{PIV_BASE}}

For a 10 or an 11 the subset has already done most of the pruning: one 4qt DR in 90 finishes in 11, one 5qt DR in 400. The reads matter most where the odds are still alive, at 1–3qt, and for finding the few high-qt DRs worth keeping. (The tables below go by corner-qt group from 1–2qt up. 0c0, half a percent of DR states, has its own entry in section 8.)

**Two kinds of read.** Some need no solving: the subset, the true pairs, the corner case on normal and on inverse. Some need you to solve something: the shortest HTR on both sides, the optimal corner solution and its parity. The tables keep the two apart, because a read you have to work for costs time, and because the HTR numbers assume you found the *shortest* HTR. If yours is longer than the shortest, the DR looks worse than it is, and an HTR rule drops more than it should.

### Ranking

Rank the DRs of a qt group by what the read says, keep only the best-looking quarter, and count how many of the finishes in T you kept. With no information that's 25%. Each number is the best any rule based on that read could do, which makes these tables **computer only**: a rule that gets there ranks by the exact odds of every class of DRs, thousands of them. They're ceilings, and the plain rules further down are what you carry. Each row is a qt group and a target; the reads that need no solving come first, with the share of the group that finishes in T at all for scale:

{{PIV_RANK}}

- **The lower the target, the more a read tells you.** Share of the finishes that pairs and corner cases put in the best-looking quarter:

  | Finishes kept | 3qt | 4qt |
  |---|---:|---:|
  | the 12s | 52% | 65% |
  | the 11s | 63% | 77% |
  | the 10s | 74% | 89% |

  For a 13 nothing does much.
- **Most of it needs no solving.** From 3qt up, pairs plus the corner case on both sides rank better than the two HTR lengths do, at every target from 10 up. Adding the HTR lengths on top is worth 1 to 7 points.
- **At 1–2qt it's the other way round.** HTR length is the best single read there (72% of the 10s against 64% for pairs and corner cases), and at 1–2qt you find the HTR quickly anyway.

### Throwing away

The other direction: how many DRs can you drop and still keep 95% of the finishes in T? Like the ranking, these are ceilings, **computer only**. Each cell is the share of the qt group you can drop, for the reads that need no solving first:

{{PIV_DROP}}

For an 11 that's a third of the 1–2qt DRs, two in five at 3qt and more than half at 4–5qt. For a 12 it's a fifth to two in five.

Another way to cut it. Say a class of DRs is "under 1%" if at most one in a hundred of it finishes in T. Each cell below is the share of the qt group's DRs in such classes; the tables after it give the share of all the finishes in T those classes hold, which is what you lose by dropping them. Reads that need no solving first:

{{PIV_DEAD}}

Read the rows "4qt, 11 or less" like this. By subset alone 35% of 4qt DRs are under 1% (that's 4c4, 0c4 with four or more bad edges, and 2c4 8e). With pairs and corner cases it's 69%, and those 69% hold 17% of the 11s. For a 10, all of 4qt is under 1% as a group, and the reads work the other way: with pairs, corner cases and HTR they pick out the 4% of 4qt DRs that hold half of the 10s. For a 13 no read puts more than 4% of any qt group under 1%.

So tseitsei89's "100% cases and 0% cases" don't exist at any target. There is no feature count that sorts DRs into good and bad. What exists is a set of reads that each multiply your hit rate by two or three, more the lower your target, and a handful of corners of the tables that really are dead.

### Plain rules

The tables above are ceilings, **computer only**: a rule that reaches them needs a table of thousands of classes. These are rules you can carry in your head, for the attempt.

**HTR length against your target** (needs the shortest HTR on both sides). This is Zagros's "4c3 that is 9+ on both sides I throw away" ([[T11190]]) moved to the finish you need, T. Each rule gets two columns: the share of the qt group it drops, and the share of the finishes in T it loses. The rules on the longer side first:

{{PIV_RULES}}

- **The first rule, longer side more than $T$, is a proof**: no finish is shorter than the longer HTR. For a 12 it is next to nothing (0.15% of 4qt DRs). For a 10 it rules out a quarter of 4qt and 44% of 5qt.
- **"Both sides $T-1$ or more" is the safe rule.** For an 11 that's 10+ on both sides: it drops 31% of 4qt DRs and loses 2.5% of the 11s, and at 3qt it drops 8% and loses 0.2%.
- **"Both sides $T-2$ or more" is the aggressive one**, and for an 11 it is exactly 9+ on both sides: it drops 28% of 3qt and 67% of 4qt DRs and loses 5% and 20% of the 11s.
- A DR that is exactly T to HTR on the longer side can still finish in T. Appendix G has such a state for every subset. This one is 9 to HTR on both sides:

  ```
  U' L2 D' B2 U' B2 U L2 D   // 4c3 4e, finishes in 9
  ```

**Pairs against your target** (no solving). Each rule gets two columns, the share of the qt group dropped and the share of the finishes in T lost:

{{PIV_PAIR_RULES}}

Pairs are spread the same way in every qt group, so each rule drops the same share everywhere. What changes is the price: dropping the DRs with no pairs costs 2–7% of the 11s, dropping one pair or none costs 9–23%.

The corner-case rules are per subset. They are in section 8 and section 4.3.

**What is proven at each target.** Two bounds hold for every finish and can be worked out by hand: the longer HTR, and the best corner solution with the right E-parity (section 4.5). Each row is a qt group and a target; the columns are the share of its DRs for which a bound proves there is no finish in T. Two of the computer tables of section 7 follow in the second table, **computer only**: NISS@DR and everything visible are lookups in millions of cases.

{{PIV_BOUNDS}}

For a 12 the hand bounds prove next to nothing below 5qt. For a 10 they rule out half of the 4qt DRs and 80% of the 5qt ones, and for an 11 a fifth and 38%. So the lower your target, the more a guaranteed bound is worth working out, on the high-qt DRs where it bites.

The setup + HTR bound of section 5 (trangium's 2q bound taken to any qt) is not a proof, because a finish with extra quarter turns can get under it. From 3qt up that almost never happens: it is wrong about 0.2% of the finishes in T at most. Share of DRs it rules out, for a 10 and for an 11:

| Corner qt | Rules out a 10 | Rules out an 11 |
|---|---:|---:|
| 1–2qt | a third | a sixth |
| 3qt | 19% | 6% |

The second row is more than the two proven bounds together, so that's where this hand bound does something. The first row comes at a price: there it is wrong about 5–7% of those finishes.

Appendix H has every read at every target with more cut-offs (best 10%, 25%, 50%; keeping 90%, 95%, 99%).

### Scatter

The same thing without a target: how much scatter is left in the optimal once you know the read (sd, in moves). **Computer only**: it measures the reads over every DR state, it isn't something to work out in an attempt. Each row is what you know; the last column is the sd of the optimal among DRs that look the same to it.

| What you know | Needs solving | Scatter left, sd in moves |
|---|---|---:|
| nothing | | {= SDLEFT() =} |
| subset | no | {= SDLEFT('sub') =} |
| + true pairs | no | {= SDLEFT('sub', 'pairs') =} |
| + corner case on both sides | no | {= SDLEFT('sub', 'ccn', 'cci') =} |
| + pairs and corner cases | no | {= SDLEFT('sub', 'ccn', 'cci', 'pairs') =} |
| + HTR length on both sides | yes | {= SDLEFT('sub', 'hn', 'hi') =} |
| + corner case and HTR on both sides | yes | {= SDLEFT('sub', 'ccn', 'cci', 'hn', 'hi') =} |
| + corner length L and E-parity | yes | {= SDLEFT('sub', 'L', 'dLp', 'par') =} |
| + pairs, corner cases and HTR | yes | {= SDLEFT('sub', 'ccn', 'cci', 'pairs', 'hn', 'hi') =} |
| + pairs, HTR, L and E-parity | yes | {= SDLEFT('sub', 'pairs', 'hn', 'hi', 'L', 'dLp', 'par') =} |
| + all of these together | yes | {= SDLEFT(*ALLREADS) =} |
| *the optimal leave slice (for scale, you can't read this)* | | 0.43 |

**Zagros's two hunches, tested.**

- "I hypothesize that corner case + moves to HTR on normal + moves to HTR on inverse can tell you the optimal solution with a standard deviation of like 0.25 moves" ([[T11482]]). The sd left is {= SDLEFT('sub', 'ccn', 'cci', 'hn', 'hi') =} over all DRs ({= SDLEFT('ccn', 'cci', 'hn', 'hi') =} without the bad-edge count, which Zagros didn't list). Adding pairs makes it {= SDLEFT('sub', 'ccn', 'cci', 'pairs', 'hn', 'hi') =}, and every read together {= SDLEFT(*ALLREADS) =}.
- "Like it is possible you could consistently predict the opt finish length within ~1 move based on those two things" ([[T6905]]), the two being the optimal corner length L and the longest direct HTR. True, 93.3% of DRs are within one move of the typical value for their (subset, L, longer HTR). But 91.3% are within one move of the typical value for their subset alone. The finish just doesn't vary much inside a subset.

A pair that shows what the first one is up against. Both are 2c4 4e, with the same corner case on normal and on inverse, 7 to HTR on both sides, and the same corner length (7) (✓ Lean, all but the corner case):

    D F2 U' F2 D B2 D'                                 // optimal 7
    D' R2 B2 U' F2 D B2 U B2 F2 U' F2 U' L2 D' U'      // optimal 16

---

## 4. The reads, cheapest first

### 4.1 Subset

The baseline, and still the biggest single piece of information. Appendix A has all 48 with average, share finishing in 9 to 13, and the fastest and longest optimal in each (God's number per subset, which compLex asked about). The longest, in DR moves: 18 for 0c0 8e, 0c3 4e, 2c5 0e and 2c5 4e, 17 or 16 for most others, 13 for 0c0 0e. One of each 18:

    F2 L2 U B2 F2 R2 B2 F2 R2 U F2 R2 D U F2 R2 D' U'      // 0c0 8e
    F2 D' F2 D' F2 R2 U2 R2 U' B2 R2 B2 L2 U B2 U2 R2 U'   // 0c3 4e
    U2 L2 D B2 U' B2 U' L2 D B2 R2 U R2 U R2 U2 R2 U'      // 2c5 0e
    R2 F2 L2 D' F2 D' B2 F2 R2 U2 F2 D' B2 U2 L2 U' R2 U'  // 2c5 4e

Appendix G has a longest one for every subset.

zakimoshi: "We calculated all the 18 optimals once I remember it being either 5qt or the bad 3qt ons" ([[T3924]], under Levi's table of "every possible DR state (ignoring e slice)", [[T3896]]). For the leave slice that's exact: the {= LSTOP('n') =} states that need 18 to leave the slice are all {= LSTOP('subsets') =}. For the full finish the eight 0c0 8e states join them. They leave the slice in {= LSTOP('0c0 8e') =} and the slice costs 2. In the September 2023 thread on the leave slice, zakimoshi had found and linked Tomas Rokicki's list of the distance-18 positions ([[T3092]]), "This is including slice minus symmetries tho" ([[T3093]]). The list has the same four subsets, and its 0c0 8e positions are the ones that leave the slice in 16. For the 0c0 8e above (replayed with nissy):

    U R2 L2 F2 R2 L2 F2 U R2 B2 U2 F2 R2 U2 R2 B2   // leaves the slice in 16: the U and D layers are solved, half a turn off the E layer

wen's "luckily they are all(?) 0c3 or 5q shit so you realistically will never get them" ([[T6881]], in a thread on whether any DR is 16 or more optimal) depends on how far up "they" starts. Joba's per-subset file ([[T9115]]) already has what's needed for the 16-or-more row. Each row is a cut-off, with the DR states at or above it, how rare they are, and the share of them that is 0c3 or 5qt:

| Optimal finish, moves | DR states | One DR state in | In 0c3, 2c5 or 4b5 |
|---|---:|---:|---:|
| 18 | {= TOP(18, 'n') =} | {= TOP(18, 'onein') =} | {= TOP(18, 'worst') =} |
| 17 or more | {= TOP(17, 'n') =} | {= TOP(17, 'onein') =} | {= TOP(17, 'worst') =} |
| 16 or more | {= TOP(16, 'n') =} | {= TOP(16, 'onein') =} | {= TOP(16, 'worst') =} |

At 16 or more the biggest share is 4c4 with {= TOP(16, '4c4') =}, which is where wen says a 16 turns up: "usually this presents itself as like +15 from a 4c4 but with some weird dr breaking nonsense then I know it's a 16 optimal or something lol" ([[T6888]]). {= TOP(16, 'nsub') =} of the 48 subsets have a state at 16 or more, all but {= TOP(16, 'without') =}. The second half, "you realistically will never get them", holds wherever the cut is. Three at 16 or more that are neither 0c3 nor 5qt (✓ Lean: the optimal of each):

    F2 D2 B2 R2 U' F2 R2 B2 R2 U' F2 L2 D2 R2 D U'      // 4b2 4e, optimal 16
    R2 U L2 D F2 L2 B2 D2 B2 U' B2 U' R2 F2 R2 U'       // 2c3 4e, optimal 16
    R2 U2 B2 L2 F2 L2 D2 F2 R2 U' B2 F2 L2 R2 U' R2 D'  // 4a1 4e, optimal 17

The shortest possible HTR by corner qt, one row per qt count, with a state that has exactly that on both sides (✓ Lean: the HTR length of each state, on both sides):

| Corner qt | Shortest HTR | A state with exactly that on both sides |
|---:|---:|---|
| 1 | 1 | `D` |
| 2 | 3 | `D B2 D'` |
| 3 | 5 | `D' B2 D' B2 D'` |
| 4 | 7 | `D B2 D' B2 D B2 D'` |
| 5 | 9 | `U' L2 U R2 U' L2 U R2 D` |

That's the floor on one side. Joba wanted a lower bound for an HTR with NISS: "But that's without niss. I guess I'll assume that the assumption that the lower bound is 2/1/2/4/6/8 moves for 0/1/2/3/4/5 qt cases for now, with the possible exception of 0c3" ([[T6639]]). From 1qt to 5qt those are reached. `D` is one move from HTR either way, and each row below is one of the other four states of the table above with a NISS HTR of that length, the bracket on inverse (replayed with nissy):

| Corner qt | State | A NISS HTR | Its length, moves |
|---:|---|---|---:|
| 2 | `D B2 D'` | `D (D')` | 2 |
| 3 | `D' B2 D' B2 D'` | `D B2 D (D')` | 4 |
| 4 | `D B2 D' B2 D B2 D'` | `D B2 D' (D B2 D')` | 6 |
| 5 | `U' L2 U R2 U' L2 U R2 D` | `U (U R2 U' L2 U R2 D)` | 8 |

### 4.2 Pairs

Count the true pairs: a corner and an edge next to each other in the U or D layer with both touching stickers matching (16 places to look). This is the read that costs nothing, and it works at every qt.

Share of each corner subset finishing in 10, 11 and 12 or less, by number of true pairs. Each row is a corner subset and a target; each column is a number of pairs:

{{MAIN_PAIRS}}

Each pair is worth about 0.15 moves of average optimal. What that does to the odds depends on how rare the finish is. What one more pair multiplies the odds by, per corner subset:

| Odds of | 4a1, times | 2c4, times | 2c5, times |
|---|---:|---:|---:|
| a 12 | {= PPR('4a1',12) =} | {= PPR('2c4',12) =} | {= PPR('2c5',12) =} |
| an 11 | {= PPR('4a1',11) =} | {= PPR('2c4',11) =} | {= PPR('2c5',11) =} |
| a 10 | {= PPR('4a1',10) =} | {= PPR('2c4',10) =} | |

That last row has numbers for 4a1 and 2c4 only. So pairs matter more the lower your target and the higher the qt.

Levi's question, "has anyone noticed that blocky 2c4s are way better than not-so-blocky 2c4s?" ([[T6965]]): yes. For an 11, from {= pct(q(cs='2c4',pairs=0),11) =} with no pairs to {= pct(q(cs='2c4',pairs=5),11) =} with five or more, {= P05('2c4',11) =} times as often. The same step is worth ×{= P05('4a1',11) =} at 4a1, ×{= P05('2c3',11) =} at 2c3 and ×{= P05('2c5',11) =} at 2c5, so Levi's "it seems like block matter a lot more than with other DRs" holds against 4a1 and 2c3, not against 2c5. Appendix D has all 48 subsets, for 10, 11, 12 and 13.

On Rodney's finer split ([[T11478]]: "I suspect, however, that you won't get very clean stats from just the corner case plus bad edge count. You would need to break cases down by some kind of pair counts."): I also counted pseudo-pairs (both stickers opposite), side semi-pairs and top semi-pairs, defined as in Rodney's message. Knowing all four counts instead of just the true pairs moves the sd left from {= SDPAIRS(1) =} to {= SDPAIRS(4) =} (an sd over every DR state, **computer only**). Pairs with E-slice edges add even less. So for judging a DR, count true pairs and stop. Rodney's other use of the semi-pairs, breaking ties between DR-to-HTR moves ("If I have two choices for a move, and they both form the same number of true pairs, then I will prefer the one that results in the smallest number of semi-pairs"), isn't tested here.

You don't need to count again on the inverse scramble: a block stays a block, so the number of true pairs is the same on both sides for every DR state.

### 4.3 Corner case, on both sides

{{CORNER_SECTION}}

A warning: the bad corner *positions* don't always tell you the case. 2c4 has three different "both on one layer, adjacent" cases, at {= C1('2c4','8') =}, {= C1('2c4','7') =} and {= C1('2c4','2') =} (in 10 / 11 / 12). What separates them is the corner permutation, which you get the way you already get the subset (tracing, or whatever corner-case system you use). The column "a qt takes it straight to" is the quick tell: if some U or D quarter turn drops the corner qt count right away, you're in one of the good ones.

### 4.4 HTR length on both sides

Zagros asked for the square table ([[T11190]]); trangium posted one from samples of 20–100 per cell, and JTuu said "it should be tractable to compute the exact version of this table using levi's list of precomputed dr finishes" ([[T11195]]). Exact, for the four big high-qt subsets. Each row is a pair of HTR lengths, shorter side first; the columns are the share finishing in 10, 11 and 12 or less.

{{MAIN_SQUARES}}

One more move to HTR on both sides costs about half a move of average optimal. What it divides the odds by, for each step:

| HTR on both sides | Odds of a 12 divided by | Odds of an 11 divided by | Odds of a 10 divided by |
|---|---|---|---|
| from 7 and 7 to 8 and 8 | about two | about three | three to five |
| from 8 and 8 to 9 and 9 | about three | about five | more than ten |

Appendix F has every subset with share, average, fastest finish, and odds for 10 to 13. Section 3 has the same read as a plain rule against your target.

**By the longer side alone**, for a whole corner-qt group. This is the table to use when you have one HTR length per side and no time for more (rows under 0.1% of the group are left out). Each row is a qt group and a longer HTR length; the In columns are the share finishing in that many moves or less:

{{PIV_HTR}}

**Zagros's rule, "4c3 that is 9+ on both sides I throw away".** Each row is a part of 4c3, with its share, its average optimal and how it finishes:

{{MAIN_ZAGROS}}

So the rule halves your 4c3s, and what it costs depends on what you need. For an 11-move DR, which needs a 10 or an 11, it trades half of your 4c3s for 8% of the 10s and 17% of the 11s. For a 12 it throws away a quarter of the finishes. It does throw away real finds:

    U' L2 D' B2 U' B2 U L2 D     // 4c3 4e, 9 to HTR on both sides
    D' L2 U' B2 U B2 D L2 U      // its optimal finish: 9

Knowing the two HTR lengths does not give you a better *guarantee* than the longer one: in every subset some state finishes in exactly max(normal, inverse). The 4c3 4e just above is one, and Appendix G has one for every subset. It's an odds read.

### 4.5 Corner length and E-slice parity

Side half turns (R2 L2 F2 B2) each swap two E-slice edges, and U and D never touch the slice. So the number of side turns in *any* DR finish is even if the E-slice is an even permutation (solved, 3-cycle, 2e2e) and odd if it's odd (2-swap, 4-cycle). This is Rodney's fr-parity, used on the whole finish instead of after HTR.

> Find an optimal corner solution, length L. Count its side turns. If that's the wrong parity for the E-slice, there is no L-move finish. You need the best corner solution of the other parity.

What the other parity costs, over all corner states of each subset. Each row is a corner subset; each column is how much longer the best corner solution of the other parity is than the best one, as a share of its corner states:

| Corners | Same length | 1 move longer | 2 moves longer | More |
|---|---:|---:|---:|---:|
| 4a2, 0c3, 0c4 | | 100% | | |
| 4a3, 4b3 | 11% | 89% | | |
| 4a4, 4b4 | 6% | 94% | | |
| 2c4 | | 75% | 25% | |
| 2c5 | 2% | 80% | 18% | |
| 4b5 | 14% | 56% | 31% | |
| 4b2 | 3% | 73% | 25% | |
| 2c3 | 15% | 35% | 50% | |
| 4a1 | | 75% | 4% | 21% (+3 to +5) |
| 0c0 | 25% | | 50% | 25% (+3 to +6) |

This one is a true lower bound, proven in Lean: no finish is shorter than the best corner solution of the right parity. Share of DRs it proves "no" for (the table of what is proven in section 3 has more), by target and qt group:

| Target | 4qt DRs | 5qt DRs |
|---|---:|---:|
| a 12 | 5% | 13% |
| an 11 | 21% | 37% |
| a 10 | 48% | 73% |

It needs the *optimal* corner solutions of both parities, so it's a read for when you've written the skeletons down anyway.

Two DRs where it bites:

    U B2 U' F2 U B2 D2 L2 U' R2 U R2 U' L2 U2      // 2c4 4e, odd E-slice
    // best corner solution: 12, with an even number of side turns. Best with an odd number: 13.
    // So no 12. (Its optimal is 15.)

    U D L2 D' B2 U R2 F2 B2 D2 L2 D' R2 L2 D2 B2   // 2c3 6e, odd E-slice (Rodney's first random scramble)
    U' R2 U' R2 U                                   // corners in 5, but two side turns
    U R2 U2 R2 U R2 U                               // best with an odd number: 7

As an odds read, L does about what HTR length does from 3qt up, and less at 1–2qt (Appendix H). Appendix B splits the big high-qt subsets by L and parity. For 2c4 4e, each row is a corner length (and parity), with the share finishing in 10, 11 and 12 or less:

| Corner length | In 10 | In 11 | In 12 |
|---|---:|---:|---:|
| L = 8 | {= CELLS(T(q2(cs='2c4',e=4,L=8))) =} |
| L = 11 | {= CELLS(T(q2(cs='2c4',e=4,L=11))) =} |
| L = 12, E-slice even | {= CELLS(T(q2(cs='2c4',e=4,L=12,parity=0))) =} |
| the same, E-slice odd | {= CELLS(T(q2(cs='2c4',e=4,L=12,parity=1))) =} |

The E-slice parity on its own, without L, is a small read but it's free. It mostly decides whether the finish wants to be even or odd in length. Each row is a qt group and a target; the columns are the share finishing in that many or less, by E-slice parity:

| Corner qt and finish | Odd E-slice | Even E-slice |
|---|---:|---:|
| 4qt, in 12 | {= pct(q2(group='4qt',parity=1),12) =} | {= pct(q2(group='4qt',parity=0),12) =} |
| the same, in 11 | {= pct(q2(group='4qt',parity=1),11) =} | {= pct(q2(group='4qt',parity=0),11) =} |
| 5qt, in 13 | {= pct(q2(group='5qt',parity=1),13) =} | {= pct(q2(group='5qt',parity=0),13) =} |

Note the flip: the odd E-slice is ahead in the first row, the even one in the second.

### 4.6 The last DR move

Zagros asked what one invertible move is worth. If your DR ends in R, then R' is also a DR and its state is yours plus an R2, so you get the better of two finishes. Average optimal over all DRs: 13.58 for a pure DR, 13.26 when the last move can go either way. Each row is a qt group with the last move fixed or free to turn; the columns are the share finishing in 9 to 13 or less:

{{PIV_LASTMOVE}}

Over all DRs the other DR is one shorter {= LASTMOVE('shorter') =} of the time, one longer just as often, and the same otherwise, so it's worth {= LASTMOVE('gain') =} moves. By subset that runs from {= LASTMOVE('lo') =} to {= LASTMOVE('hi') =}; most subsets are within a few hundredths of a third. It multiplies the odds of a 10 or an 11 by 1.5 to 1.9 and of a 12 by 1.4 to 1.8. (If you could pick any of the four side half turns it would be 0.73.) An example:

    D' L2 D R2 B2 F2 U2 B2 R2 U L2 U'       // optimal 12
    D' L2 D R2 B2 F2 U2 B2 R2 U L2 U' L2    // the same DR with its last move (an L) turned the other way: optimal 11

---

## 5. Bounds people use, graded

A bound is only a bound if it never exceeds the optimal. Graded on all states; each row is a bound, with its average and the average optimal over the DRs it applies to:

| Bound | Ever too high? | Its average, moves | Average optimal there, moves |
|---|---|---:|---:|
| longer HTR, normal or inverse (all DRs) | never (proven) | 9.22 | 13.58 |
| best corner solution with the right E-parity (all DRs) | never (proven) | 9.44 | 13.58 |
| Levi's 1qt formula, $\text{HTR}_\text{normal} + \text{HTR}_\text{inverse} - 1$ (4a1 4e) | never for a finish with one quarter turn. A finish with three is shorter for 11.7% of 4a1 4e | 10.85 | 12.27 |
| setup + HTR, any qt (below) | never for a finish with the minimum number of quarter turns. A finish with more is shorter for 2.6% at 1–2qt and 0.002% above | see below | |

**Levi's formula.** $\text{HTR}_\text{normal} + \text{HTR}_\text{inverse} - 1$ bounds the finishes with one quarter turn, which is what Levi's doc uses it for. (The doc writes it as the path to the trigger on normal + on inverse + 1. An HTR is that path plus the quarter turn, so it's the same number.) Levi's 1qt example, the DR in Levi's doc after the 1qt reduction `R2 U' F2 U`:

```
R2 U' F2 U   // shortest HTR here is 7 on normal and 3 on inverse, each counting the qt
```

The formula counts the qt once, which gives Levi's $4 + 6 + 2 + 1 = 13$ ([wen, 28 Nov 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1311629216235913226)).

A 1qt state can also be solved with three quarter turns, and the number worth having is how often that is shorter. It's the case Jay raised: "one major issue i'm having with the bounding stuff rn is the fact that it isn't really equipped to handle higher qt stuff which is where optimal usually gets missed (basically anything involving 3-5 total qt when the subset needs two less qt optimally)" ([[T5687]]). Levi's answer: "Bounding could theoretically handle cases like this if the extra QTS come before the 1Q case, but I mostly just check bounding + extra QT stuff afterwards for subsets where extra QTS are common" ([[T5689]]). Over all 286,654,464 states of 4a1 4e, each row is where the optimal falls against the formula:

| The optimal is… | Share of 4a1 4e |
|---|---:|
| below the formula, so a 3qt finish is shorter | {= LEVI('below') =} |
| of those, below by 1 | {= LEVI(-1) =} |
| below by 2 | {= LEVI(-2) =} |
| below by 3 or more | {= LEVI('-3') =} |
| equal to the formula | {= LEVI('equal') =} |
| above the formula | {= LEVI('above') =} |

If the formula says 12 or less, a 3qt finish beats it 2.5% of the time, and 0.6% of the time if it says 11 or less. Example:

    U2 F2 R2 B2 U D2 B2 R2 B2 R2 F2   // 4a1 4e. HTR is 6 on normal, 5 on inverse, formula says 10
    U B2 L2 F2 D F2 D                  // 7

(Both lines are proven in Lean.) For 4a1 2e optimal is below the formula 44% of the time and for 4a1 0e 95%, so the formula is only for 4a1 4e (Levi's "1qt 4c4e"), like Levi says. (4a1 2e and 0e are fine DRs to solve. It's the formula that doesn't apply to them, because they can't be finished with one quarter turn.)

One more thing about 4a1 4e that I haven't seen written down: for 72 of its 432 cases (one in six) the shortest HTR is not a 1qt HTR at all. The shortest 1qt path is 8, 9 or 10 moves and a 3qt HTR does it in 7 or 8. So "shortest HTR" and "shortest way to the trigger" are different numbers there, and the formula wants the second. One where it happens on both sides:

    U L2 R2 U R2 B2 U L2          // 4a1 4e
    U L2 F2 L2 U B2 U             // shortest HTR on normal: 7, three quarter turns
    R2 F2 U2 R2 F2 U2 L2 D        // shortest HTR with one quarter turn: 8
    L2 U' B2 R2 U' R2 L2 U'       // optimal finish: 8

(The inverse is the same: 7 with three quarter turns, 8 with one.)

**The bound against the real leave slice** (count quackula's question). For 4a1 4e, each row is one value of leave slice minus formula, in moves, with the share of states that have it:

| Leave slice minus formula | Share of 4a1 4e |
|---:|---:|
| −3 or less | {= LEVILS(-3) =} |
| −2 | {= LEVILS(-2) =} |
| −1 | {= LEVILS(-1) =} |
| +0 | {= LEVILS(0) =} |
| +1 | {= LEVILS(1) =} |
| +2 | {= LEVILS(2) =} |
| +3 | {= LEVILS(3) =} |
| +4 or more | {= LEVILS(4) =} |

Average {= LEVILS('mean') =}. The leave slice is below the formula {= LEVILS('below') =} of the time, more often than the full finish is, because leaving the slice is easier. (The example above is one: formula 10, leave slice 7.)

**Setup + HTR at any qt.** trangium ([[T11428]]): "not sure if this has been explored / how useful this is, but you can get a true 2q bound by taking (shortest htr on one side) + (moves to set up to 1qt on the other)", good "if you don't use extra qts". The setup is the fewest half turns before the first qt on the other side. FakeMMAP's point was that a 2q bound is what you use on 3q and 4q DRs: "It's a 2q bound, so this is useful for 3q and 4q." ([[T11448]]). bpaul asked "actually doesn't this work for any number of quarter turns?" and took it back a few minutes later: "oh wait no this is wrong" ([[T11454]], [[T11455]]). A version that does work at any qt: on each side count the fewest half turns you need before some quarter turn lowers the qt count, add the shortest HTR of the other side, take the bigger of the two sums. At 1qt this is Levi's formula. Like Levi's, and with trangium's condition, it's only a bound for finishes that use the minimum number of qts.

Each row is a qt group; the columns are the share of its DRs where the bound is above the optimal (beaten by a finish with extra qts), equal to it, or under it by 1, 2, or 3 or more moves:

| Corner qt | Beaten by extra qts | Bound equals optimal | 1 under | 2 under | 3 or more under |
|---|---:|---:|---:|---:|---:|
| 1–2qt | 2.6% | 4.0% | 11% | 18% | 64% |
| 3qt | <0.01% | 0.3% | 2.3% | 9.5% | 88% |
| 4qt | <0.01% | 0.3% | 2.6% | 13% | 84% |
| 5qt | 0 | 0.1% | 0.8% | 6.3% | 93% |

The averages, in moves, on the same rows:

| Corner qt | Setup + HTR bound | Longer HTR | Optimal |
|---|---:|---:|---:|
| 1–2qt | 9.62 | 7.66 | 12.75 |
| 3qt | 9.22 | 8.60 | 13.23 |
| 4qt | 10.35 | 9.83 | 13.89 |
| 5qt | 10.47 | 10.47 | 14.30 |

How often a finish with extra quarter turns gets under it, by subset:

| Subset | Beaten, share of the subset |
|---|---:|
| 4a1 4e | {= SETUPBEAT('4a1 4e') =} |
| 4a2 4e | {= SETUPBEAT('4a2 4e') =} |
| 4a2 0e | {= SETUPBEAT('4a2 0e') =} |
| 4b2 4e | {= SETUPBEAT('4b2 4e') =} |
| 4a2 2e | {= SETUPBEAT('4a2 2e') =} |
| 4b2 0e | {= SETUPBEAT('4b2 0e') =} |
| 4b2 2e | {= SETUPBEAT('4b2 2e') =} |
| everything at 3qt and up | {= SETUPBEAT('3qt+') =} |

The first row is more than the 11.7% for Levi's formula, because this one uses the real setup (see above). So from 3qt it's as good as a true bound. One state for every subset where it happens (there are 13). Each row gives the state, the bound, and the optimal finish that beats it, with its length and its quarter turns against the fewest the subset needs (✓ Lean: each finish solves its state and is optimal; the bound column is computed):

| Subset | Scramble | Setup + HTR bound | Optimal finish | Its length | Quarter turns in it | Fewest the subset needs |
|---|---|---:|---|---:|---:|---:|
| 4a1 4e | `D' F2 R2 U' B2 F2 D` | 15 | `D' F2 B2 U R2 F2 D` | 7 | 3 | 1 |
| 4a2 0e | `D' F2 D2 L2 U F2 D' B2 U2 R2 U` | 13 | `U' R2 U2 B2 D F2 U' L2 D2 F2 D` | 11 | 4 | 2 |
| 4a2 2e | `D' L2 D' B2 F2 U' F2 D'` | 10 | `D F2 U F2 B2 D L2 D` | 8 | 4 | 2 |
| 4a2 4e | `D B2 D L2 D F2 U F2 U' L2 U` | 15 | `U' L2 U F2 U' F2 D' L2 D' B2 D'` | 11 | 6 | 2 |
| 4b2 0e | `D' R2 U' F2 U2 L2 U' R2 D` | 12 | `D' R2 U L2 U2 F2 U R2 D` | 9 | 4 | 2 |
| 4b2 2e | `D' F2 U B2 U F2 D'` | 8 | `D F2 U' B2 U' F2 D` | 7 | 4 | 2 |
| 4b2 4e | `D L2 U' R2 U' L2 F2 U'` | 12 | `U F2 L2 U R2 U L2 D'` | 8 | 4 | 2 |
| 0c3 4e | `U' F2 U F2 U' R2 D L2 U' L2 U R2 U` | 14 | `U' R2 U' L2 U L2 D' R2 U F2 U' F2 U` | 13 | 7 | 3 |
| 4c3 2e | `D' B2 D' L2 D' L2 U B2 U'` | 10 | `U B2 U' L2 D L2 D B2 D` | 9 | 5 | 3 |
| 4c3 4e | `U' L2 D' B2 U' B2 U L2 D` | 10 | `D' L2 U' B2 U B2 D L2 U` | 9 | 5 | 3 |
| 4c4 0e | `U F2 U' F2 U R2 U' F2 U F2 R2 U'` | 13 | `U R2 F2 U' F2 U R2 U' F2 U F2 U'` | 12 | 6 | 4 |
| 4c4 2e | `D B2 D R2 U' R2 D L2 D B2 D'` | 12 | `D B2 D' L2 D' R2 U R2 D' B2 D'` | 11 | 6 | 4 |
| 4c4 4e | `D B2 D' F2 D F2 D' F2 U F2 U'` | 12 | `U F2 U' F2 D F2 D' F2 D B2 D'` | 11 | 6 | 4 |

Daichi's objection, "Idk how well this bounds 4b2 0e, because HTR is always 6-9 moves and setup is always 0-3 moves, so the bound you're gonna get is 6-12 moves, when 90+% of 4b2 0e cases are 12-14 optimal" ([[T11457]]), holds everywhere: it adds two moves to the HTR bound at 2qt, half a move at 3–4qt, nothing at 5qt (a qt that lowers the count is always available right away), and it sits three or more under optimal for most DRs.

**Rodney's rules at 1qt** are graded in section 9: a true lower bound in all 216 cases, even against DR-breaking finishes.

**So for bounding error stats** (compLex's question): the guaranteed bounds you can compute by hand are on average four moves under optimal. The useful hand bound is still Rodney's, per skeleton, late.

---

## 6. Leave slice, the slice, and width

Both measures in this section come from the optimal finish and the optimal leave slice of every state, so they're **computer only**: the answer key to JTuu's questions, not something to check in an attempt.

**Cost of the slice** (JTuu's question, which went on "and ig #ht on the slice axis" ([[D7947]]); here by the corner qt of the DR only): optimal finish minus optimal leave slice. Each row is a qt group; the columns are the share of its DRs where the slice costs nothing, 1, 2, or 3 or more moves, and the average cost:

| Corner qt | Costs nothing | 1 move | 2 moves | 3 or more | Average, moves |
|---|---:|---:|---:|---:|---:|
| 0qt | {= SLICE('0qt', 0) =} | {= SLICE('0qt', 1) =} | {= SLICE('0qt', 2) =} | {= SLICE('0qt', 3) =} | {= SLICE('0qt', None) =} |
| 1–2qt | {= SLICE('1-2qt', 0) =} | {= SLICE('1-2qt', 1) =} | {= SLICE('1-2qt', 2) =} | {= SLICE('1-2qt', 3) =} | {= SLICE('1-2qt', None) =} |
| 3qt | {= SLICE('3qt', 0) =} | {= SLICE('3qt', 1) =} | {= SLICE('3qt', 2) =} | {= SLICE('3qt', 3) =} | {= SLICE('3qt', None) =} |
| 4qt | {= SLICE('4qt', 0) =} | {= SLICE('4qt', 1) =} | {= SLICE('4qt', 2) =} | {= SLICE('4qt', 3) =} | {= SLICE('4qt', None) =} |
| 5qt | {= SLICE('5qt', 0) =} | {= SLICE('5qt', 1) =} | {= SLICE('5qt', 2) =} | {= SLICE('5qt', 3) =} | {= SLICE('5qt', None) =} |
| all DRs | {= SLICE(None, 0) =} | {= SLICE(None, 1) =} | {= SLICE(None, 2) =} | {= SLICE(None, 3) =} | {= SLICE(None, None) =} |

The longer the finish, the more room to fit the slice for free. (+1 happens because the optimal finish doesn't have to be an optimal leave slice with a slice inserted.) Examples:

    D' U2 F2 U2               // leave slice 3, optimal finish 4: the slice costs +1
    U R2 D U'                 // leave slice 2, optimal finish 4: +2
    B2 F2 D' U L2 R2 D U'     // only the E-slice is unsolved and it takes 8: the most the slice can cost

**Width** (JTuu's question, a way to guess that a DR "likely has many solutions within 1 of optimal" ([[T11473]]); Zagros: "In my mind I assume higher qt means more opt+1" ([[T11475]])). What's measured here is narrower than either: how many of the ten moves start an optimal finish. Finishes one over optimal aren't counted (section 12), so Zagros's guess isn't tested. Each row is an optimal finish length; the last column is the share of those DRs with exactly one optimal first move:

| Optimal finish, moves | Average number of optimal first moves | Exactly one |
|---:|---:|---:|
| 10 | 1.3 | 78% |
| 11 | 1.4 | 73% |
| 12 | 1.6 | 64% |
| 13 | 2.0 | 47% |
| 14 | 2.8 | 29% |
| 15 | 4.3 | 8% |
| 16 | 7.6 | 0.2% |

Short finishes are narrow: when the optimal is 10 or 11, three times out of four exactly one first move gets it, and with a 12 two times out of three. Long finishes are wide. Higher qt DRs have more optimal first moves (3.1 on average at 5qt against 2.6 at 2qt) only because their optimals are longer. One of each:

    D' L2 D R2 B2 F2 U2 B2 R2 U L2 U'                  // optimal 12: only U or L2 starts an optimal finish
    D2 B2 U' R2 D R2 B2 R2 F2 U2 R2 D F2 U R2 U'       // optimal 16: nine of the ten moves do

---

## 7. What a computer can prove from the DR

**This whole section is computer only, the answer key.** Here the computer does the reading, from the DR alone. It shows where the information is and what any hand rule is up against. The hand versions are elsewhere: the two proven bounds and the setup + HTR bound (section 5), the plain rules, and Rodney's tracing per skeleton.

### You can't finish faster than the part you're looking at

Pick something to look at on a DR. Say, only the corners. Ask how many moves it takes to solve *just that*. The real finish solves everything, so it solves the corners too, so it can't be shorter. That's the corner-length bound, and it's the logic of every bound here. Look at more and the bound goes up. A solution read backwards solves the inverse scramble, so the same number computed on the inverse is also a lower bound, and you take the bigger one.

If you look at exactly what Rodney traces at 1qt (the corners, which slice each U/D-layer edge belongs to, its U/D colour, the E-parity) but on the DR state itself, you get one number that no skeleton and no variant can beat, at any qt. I call that NISS@DR. On HTR states with half turns only it *is* FakeMMAP's 216-case table. The catch is that at the DR it has 6,350,400 cases instead of 216.

