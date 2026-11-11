# Judging a DR by hand: what the full BFS says

*What you can read off a DR, how much it tells you about the finish, and which bounds hold. Every number is an exact count over all DR states.*

November 2026. A name with a date is a link to that message on the FMC solvers Discord (#fmc-theory or #fmc-discussion). Docs and sheets are listed with links at the end.

---

## Introduction

The question I started from: can Levi's and Rodney's DR bounding be pushed to 3qt, 4qt and 5qt DRs, so you can toss a DR because its bound is high instead of wasting time on it?

With a computer, yes. Look at part of the DR, tabulate the fewest moves that solve that part, and you have a lower bound at any qt with no skeleton. With the right table it proves "no finish in 12" for 59% of 5qt DRs. That was the first version of this doc and it is now section 7. The trouble is the tables have millions of cases, so nobody can use them in an attempt, and the bar on the server is clear:

> "is the lower bound fast to determine by human methods? If it takes too long to figure out the lower bound, you can just as well try to actually solve the DR" ([[T9871]])

> "I don't expect anyone to use the decision trees directly. I'm just hoping to use them to find the most important 2-3 features … then make some simple rules out of just those features" ([[T8337]])

So this version asks the human question. Take what you can actually read off a DR (subset, pairs, corner case, HTR length on both sides, corner solution length, E-slice parity) and measure exactly what each one tells you about the finish. I BFSed the whole DR group, 19,508,428,800 states, so nothing below is sampled.

What came out:

- **Nothing you can read is a clean yes/no.** The subset explains 35% of the variance of the optimal. Add pairs, corner length, parity and HTR length on both sides and you're at 48%. What's left has an sd of 0.78 moves (0.88 with the subset alone). Zagros's hunch that corner case + HTR on both sides pins the optimal to ~0.25 moves: it's 0.82.
- **The reads do move the odds, and they stack.** Cheapest first: pairs, corner case on both sides, HTR on both sides, corner length with E-parity. For 4qt DRs, if you keep only the best-looking quarter you keep 40% of the finishes in 12 going by subset alone, 53% going by pairs, 66% with everything.
- **A few real kill rules.** 2c5 with the bad corners stacked on both sides: no finish in 12 at all, 0.6% in 13. 2c4 stacked on both sides: 0.6% in 12. 0c3 4e that's 12 to HTR on both sides: 0.02% in 12. The tables are below.
- **Questions from the server, answered exactly**: stats by bad corner position (Daichi, JTuu, wen), by pairs (Rodney, Levi), the normal × inverse HTR table (Zagros), the 4a1 4e bound against the real leave slice (count quackula), the cost of the slice (JTuu), an invertible last move (Zagros), God's number per subset (compLex), optimal lengths of all corner cases (Evan).
- **Bounds measured.** Levi's 1qt formula, trangium's 2q bound taken to any qt, HTR length, corner length with parity. Which hold for every finish, how often a finish with extra quarter turns gets under the others, and how far below optimal they all sit.
- **Where the information is.** A computer that sees the corners exactly plus the edge colours proves "no 12" for 81% of 4qt and 95% of 5qt DRs. Everything readable put together can rule out 24% and 45% (to within 1%). The gap is the corner–edge relation, which is what Rodney's NISS@1qt tracing looks at. No count of visible features replaces it.
- **Proven in Lean**: the optimal finish of every DR state (so every stat here is a count over proven optimals), the HTR and corner-length-with-parity bounds, and the 216 HT-only values.

---

## 1. What people asked for

The gap, in the words of the people who bound in real solves:

- Jay: bounding "isn't really equipped to handle higher qt stuff which is where optimal usually gets missed" ([[T5687]]).
- Levi uses it at 2q and 3q. At 4q: "Too many variations unfortunately. It kinda works with 4q, but it is slower than just checking reductions to 2c3" ([[D10081]]). And: "If there are other metrics (i.e blocks, HTR patterns, etc) that you can bound 2q cases with that would be incredible" ([[T7084]]).
- Rodney: "+3 or lower penalties are really quite rare … That's what makes 4qt cases so intractable currently" ([[T12094]]).
- tseitsei89: "Being able to quickly tell when a DR has a short finish would be a real holy grail" ([[T10831]]). His test for a good stat: "Optimally you would only have 100% cases and 0% cases" ([[T8208]]).

And the specific questions, each with a section below:

| Asked | By | Where |
|---|---|---|
| Corner case + HTR on normal + HTR on inverse "can tell you the optimal solution with a standard deviation of like 0.25 moves"? | [[T11482]] | §3 |
| Stats by optimal corner length and longest direct HTR; "predict the opt finish length within ~1 move"? | [[T6905]] | §3 |
| A square table, moves to HTR on both sides. "4c3 that is 9+ on both sides I throw away" | [[T11190]] | §4.4 |
| "you won't get very clean stats from just the corner case plus bad edge count. You would need to break cases down by some kind of pair counts" | [[T11478]] | §4.2 |
| "blocky 2c4s are way better than not-so-blocky 2c4s?" | [[T6965]] | §4.2 |
| "stats on just bad corner positions for each subset", good/bad parity, on both sides | [[D17577]], [tseitsei89](@D17579) | §4.3 |
| "stats on 4c3 that take 4a3 corner position/parity into account?" | [[D18667]] | §4.3 |
| Average optimal of the 2c4 layouts: "double stack vs single stack vs no stack" | [[T12423]] | §4.3 |
| "is there a doc with optimal lengths for all corner cases?" | [[D16938]] | Appendix E |
| "average difference between a 4a1 4e bound and the actual leave slice? And how likely it is to be +0, +1, +2" | [[D16164]] | §5 |
| "publicly available statistics for the errors on bounding?" | [[T7177]] | §5 |
| trangium's "true 2q bound": how good is it, does it work at more qts? | [[T11428]] | §5 |
| "probability distribution of +N to solve slice given #qt" | [[D7946]] | §6 |
| "how does the optimal change from a pure DR vs. a DR in a solve where you have one move you can invert?" | [[T11467]] | §4.6 |
| The "width" of a DR | [[T11473]] | §6 |
| "are god's numbers known for htr subsets?" | [[T9096]] | Appendix A |

---

## 2. The data

- **Optimal finish of every DR state.** BFS of the group ⟨U, D, R2, L2, F2, B2⟩, all 19,508,428,800 states. "Optimal" means the shortest finish with those ten moves, same as nissy's `drudfin` and Joba's table. Average 13.58, max 18.
- **Optimal leave slice of every DR state.** Same thing ignoring the E-slice: fewest DR moves that solve corners and the eight U/D-layer edges. Average 13.29, and the max is 18 as well. (`U2 L2 D B2 U' B2 U' L2 D B2 R2 U R2 U R2 U2 R2 U'` needs 18 for the leave slice and 18 for the full finish.)
- **Every count treats each DR state as equally likely.** Real DRs aren't uniform across subsets, so read everything per subset.
- Bad corners and edges are counted the way the server counts them, up to turning a layer. The Q in 2c**4** is the corner qt count. 4c3 = 4a3 and 4b3 together (they swap on inverse), same for 4c4.
- "Finishes in 12" always means 12 or fewer.

How it was checked, and what's proven, is in sections 10 and 11.

---

## 3. How much can a read tell you?

Two ways to measure a read. First, how much scatter is left in the optimal once you know it (sd, in moves). Second, triage: rank the DRs of a qt group by the read, keep only the best-looking 10% / 25% / 50%, and count how many of the finishes in 12 you kept.

| What you know | sd left | 3qt: kept at 10 / 25 / 50% | 4qt | 5qt |
|---|---:|---:|---:|---:|
| nothing | 1.09 | 10 / 25 / 50 | 10 / 25 / 50 | 10 / 25 / 50 |
| subset | 0.88 | 21 / 43 / 72 | 18 / 40 / 73 | 12 / 31 / 56 |
| + true pairs | 0.85 | 24 / 48 / 74 | 29 / 53 / 80 | 32 / 55 / 78 |
| + corner case on both sides | 0.83 | 23 / 48 / 76 | 32 / 59 / 86 | 23 / 44 / 72 |
| + corner length L and E-parity | 0.83 | 23 / 47 / 75 | 30 / 57 / 86 | 26 / 49 / 78 |
| + HTR length on both sides | 0.82 | 24 / 49 / 77 | 32 / 60 / 86 | 28 / 48 / 76 |
| + pairs and L | 0.81 | 25 / 50 / 78 | 35 / 62 / 87 | 38 / 63 / 85 |
| + pairs, L, E-parity, HTR on both sides | 0.78 | 27 / 54 / 81 | 38 / 66 / 90 | 42 / 68 / 89 |
| *the optimal leave slice (for scale, you can't read this)* | 0.43 | 46 / 83 / 100 | 92 / 100 / 100 | 100 / 100 / 100 |

Only 20% of 3qt, 6.8% of 4qt and 2.1% of 5qt DRs finish in 12, so a perfect read would put all of them in the top 10% at 4–5qt. The best combination of everything readable gets 38–42% there.

The other direction, throwing away. Call a class "dead" if at most 1% of it finishes in 12:

| What you know | 3qt dead | 4qt dead | 5qt dead |
|---|---:|---:|---:|
| true pairs | 0.3% | 9% | 32% |
| HTR length on both sides | 3% | 19% | 18% |
| L and E-parity | 3% | 19% | 19% |
| pairs, L, E-parity, HTR on both sides | 6% | 24% | 45% |
| *really don't finish in 12* | *80%* | *93%* | *98%* |

If your target is a finish in 13 instead, no read kills more than 4% of any qt group.

So tseitsei89's "100% cases and 0% cases" don't exist at this level. There is no feature count that sorts DRs into good and bad. What exists is a set of reads that each roughly double your hit rate, and a handful of corners of the tables that really are dead.

**Zagros's two hunches.**

- *Corner case + HTR on both sides gives the optimal to ~0.25 moves* ([[T11482]]). The sd left is 0.82 over all DRs. By corner subset it runs from 0.74 (4c4) to 0.97 (0c0). Adding L and E-parity makes it 0.80.
- *L + longest HTR predicts within ~1 move* ([[T6905]]). True, 93.3% of DRs are within one move of the typical value for their (subset, L, longer HTR). But 91.3% are within one move of the typical value for their subset alone. The finish just doesn't vary much inside a subset.

A pair that shows what the first hunch is up against. Both are 2c4 4e, with the same corner case on normal and on inverse, 7 to HTR on both sides, and the same corner length (7):

    D F2 U' F2 D B2 D'                                 // optimal 7
    D' R2 B2 U' F2 D B2 U B2 F2 U' F2 U' L2 D' U'      // optimal 16

---

## 4. The reads, cheapest first

### 4.1 Subset

The baseline, and still the biggest single piece of information. Appendix A has all 48 with average, share finishing in 12 and 13, and the longest optimal in each (God's number per subset, which compLex asked about). The longest: 18 for 0c0 8e, 0c3 4e, 2c5 0e and 2c5 4e, 17 or 16 for most others, 13 for 0c0 0e. One of each 18:

    F2 L2 U B2 F2 R2 B2 F2 R2 U F2 R2 D U F2 R2 D' U'      // 0c0 8e
    F2 D' F2 D' F2 R2 U2 R2 U' B2 R2 B2 L2 U B2 U2 R2 U'   // 0c3 4e
    U2 L2 D B2 U' B2 U' L2 D B2 R2 U R2 U R2 U2 R2 U'      // 2c5 0e
    R2 F2 L2 D' F2 D' B2 F2 R2 U2 F2 D' B2 U2 L2 U' R2 U'  // 2c5 4e

Appendix G has a longest one for every subset.

The shortest possible HTR by corner qt is 1 / 3 / 5 / 7 / 9 moves for 1 to 5 qt. These five states have exactly that on both sides: `D`, `D B2 D'`, `D' B2 D' B2 D'`, `D B2 D' B2 D B2 D'`, `U' L2 U R2 U' L2 U R2 D`. Joba took 1 / 2 / 4 / 6 / 8 as a safe lower bound ([[T6639]]); the exact floor is one higher from 2qt up, on either side.

### 4.2 Pairs

Count the true pairs: a corner and an edge next to each other in the U or D layer with both touching stickers matching (16 places to look). This is the read that costs nothing, and it works at every qt.

Share of each corner subset finishing in 12, by number of true pairs:

| Corners | 0 pairs | 1 | 2 | 3 | 4 | 5 |
|---|---:|---:|---:|---:|---:|---:|
| 4b2 | 23% | 28% | 35% | 44% | 53% | 63% |
| 2c3 | 16% | 21% | 27% | 34% | 42% | 51% |
| 4c3 | 6.9% | 8.7% | 11% | 15% | 19% | 24% |
| 2c4 | 4.2% | 5.9% | 8.3% | 12% | 17% | 23% |
| 4c4 | 0.7% | 1.0% | 1.4% | 2.0% | 2.9% | 4.3% |
| 2c5 | 0.7% | 1.1% | 1.7% | 2.9% | 4.7% | 7.6% |
| 4b5 | 0.5% | 0.9% | 1.5% | 2.4% | 4.1% | 6.3% |
| share of all DRs | 14% | 27% | 27% | 18% | 9% | 4% |

Each pair is worth about 0.15 moves of average optimal and multiplies your odds of a 12 by about 1.4. So Levi is right about blocky 2c4s: from 4% with no pairs to 23% with five. It's not special to 2c4 though, the ratio is about the same in every subset. Appendix D has all 48 subsets, for 12 and 13.

On Rodney's finer split: I also counted pseudo-pairs (both stickers opposite), side semi-pairs and top semi-pairs, defined as in his message. Knowing all four counts instead of just the true pairs moves the sd left from 0.850 to 0.842. Pairs with E-slice edges add even less. So count true pairs and stop.

You don't need to count again on the inverse scramble: a block stays a block, so the number of true pairs is the same on both sides for every DR state.

### 4.3 Corner case, on both sides

This is what Daichi, JTuu and wen asked for. There are 46 corner cases once you merge rotations, mirrors and turning a layer. Inside a corner subset they are *not* equally good, and since the corner case on inverse is a different one, there are two reads.

**2c4** (wen's stacks). Seven cases:

| Bad corners | A qt takes it straight to | L | Share of 2c4 | Finishes in 12 | in 13 |
|---|---|---|---:|---:|---:|
| both on one layer, adjacent | 2c3 | 7–10 | 17% | 16.2% | 57% |
| one up one down, opposite | 4b3 | 8–10 | 8% | 13.2% | 51% |
| both on one layer, adjacent | 2c3 | 7–10 | 17% | 12.5% | 47% |
| both on one layer, adjacent | nothing, needs a setup | 8–11 | 17% | 7.0% | 33% |
| one up one down, stacked | 4b3 | 9–11 | 8% | 7.0% | 33% |
| one up one down, opposite | nothing, needs a setup | 8–11 | 17% | 6.4% | 31% |
| one up one down, stacked | nothing, needs a setup | 9–12 | 17% | 4.1% | 23% |

Both sides together: best is the first case on both sides, 26% in 12 and 75% in 13. Stacked-with-setup on both sides: 0.6% in 12 and 7.5% in 13. Any pair of stacked cases: 0.6–2.5% in 12. So "double stack" is as dead as a 5qt, and the best layout on both sides is as good as an average 2c3 4e (27%). The fastest any double-stacked 2c4 finishes is 11: `U2 L2 D' F2 U' R2 U F2 D L2 U2`.

**2c5.** Three cases: adjacent on one layer (half of 2c5, 3.4% in 12), one up one down opposite (1.9%), stacked (0.6%). Both sides adjacent: 4.7% in 12, 25% in 13. Both sides stacked: **0.0% in 12, 0.6% in 13**, average optimal 15.3. That's 6% of all 2c5 you can drop on sight, and with stacked on one side and opposite on the other (0.2% in 12) it's 19%. The fastest any double-stacked 2c5 finishes is 13: `U2 F2 U' R2 U F2 D' L2 U B2 U' L2 U2`.

**4c3** (JTuu's question). Nine cases, seven of them 4a3 and two 4b3. By the case you see on one side, the share finishing in 12 runs from 21.6% (a 4a3 with L 7–9) down to 3.6% (a 4a3 with L 9–11). The two 4b3 cases sit in the middle at 13.5% and 11.4%. With both sides: 23% down to 3%.

**4b2** (Daichi's four). They are exactly his list: 2-2 with L 3–6 (44% in 12), 3-1 with L 4–7 (40%), 3-1 with L 5–8 (33%), 2-2 with L 6–9 (30%). Both sides good 2-2: 50%. Both sides bad 2-2: 21%.

**4a2.** The widest spread of the low-qt subsets: 31% in 12 for the best case (L 5–8) down to 9% for the worst (L 8–11). Both sides worst: 2.3%.

**4c4**: 0.6% to 4.3%. **4b5**: 1.3% to 2.2%, nothing to see.

Appendix E lists all 46 cases with an example scramble for each, the L range (the optimal corner solution lengths the case can have, which is what Evan asked for), and the both-sides tables.

A warning: the bad corner *positions* don't always tell you the case. 2c4 has three different "both on one layer, adjacent" cases, at 16%, 12.5% and 7%. What separates them is the corner permutation, which you get the way you already get the subset (tracing, or whatever corner-case system you use). The column "a qt takes it straight to" is the quick tell: if some U or D quarter turn drops the corner qt count right away, you're in one of the good ones.

### 4.4 HTR length on both sides

Zagros asked for the square table ([[T11190]]); trangium posted one from samples of 20–100 per cell. Exact, for the four big high-qt subsets. Each cell: share finishing in 12.

**4c3 4e**, shorter side down, longer side across:

| | 7 | 8 | 9 | 10 | 11 |
|---|---:|---:|---:|---:|---:|
| 7 | 55% | 43% | 31% | 22% | 15% |
| 8 | | 30% | 20% | 13% | 4.6% |
| 9 | | | 11% | 5.6% | 1.8% |
| 10 | | | | 2.1% | 0.3% |

**2c4 4e**:

| | 7 | 8 | 9 | 10 | 11 |
|---|---:|---:|---:|---:|---:|
| 7 | 36% | 27% | 20% | 16% | 13% |
| 8 | | 17% | 11% | 7.4% | 5.8% |
| 9 | | | 6.0% | 2.9% | 1.9% |
| 10 | | | | 0.9% | 0.4% |

**2c5 4e**:

| | 9 | 10 | 11 | 12 |
|---|---:|---:|---:|---:|
| 9 | 13% | 6.7% | 3.0% | 1.1% |
| 10 | | 2.7% | 1.0% | 0.2% |
| 11 | | | 0.1% | 0.0% |

**0c3 4e**:

| | 10 | 11 | 12 | 13 |
|---|---:|---:|---:|---:|
| 10 | 12% | 7.8% | 4.2% | 0.0% |
| 11 | | 4.5% | 0.4% | 0.0% |
| 12 | | | 0.0% | 0.0% |

One more move to HTR on both sides costs about half a move of average optimal and cuts the odds of a 12 by two to three. Appendix F has the square table for all 48 subsets with share, average, and odds for 12 and 13.

**Zagros's rule, "4c3 that is 9+ on both sides I throw away".** That's 51% of all 4c3. Of those, 6.4% finish in 12 and 34% in 13 (average 13.74). Of the other half, 18% and 59% (average 13.22). So the rule halves your 4c3s and keeps 73% of the finishes in 12. If you can be pickier: 4c3 with 7 or less on at least one side is 10% of them and finishes in 12 28% of the time. The rule does throw away real finds: `U' L2 D' B2 U' B2 U L2 D` is a 4c3 4e that is 9 to HTR on both sides and finishes in 9 (`D' L2 U' B2 U B2 D L2 U`).

Knowing the two HTR lengths does not give you a better *guarantee* than the longer one: in every subset some state finishes in exactly max(normal, inverse). The 4c3 4e just above is one, and Appendix G has one for every subset. It's an odds read.

### 4.5 Corner length and E-slice parity

Side half turns (R2 L2 F2 B2) each swap two E-slice edges, and U and D never touch the slice. So the number of side turns in *any* DR finish is even if the E-slice is an even permutation (solved, 3-cycle, 2e2e) and odd if it's odd (2-swap, 4-cycle). This is Rodney's fr-parity, used on the whole finish instead of after HTR.

> Find an optimal corner solution, length L. Count its side turns. If that's the wrong parity for the E-slice, there is no L-move finish. You need the best corner solution of the other parity.

What the other parity costs, over all corner states of each subset:

| Corners | +0 | +1 | +2 | more |
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

This one is a true lower bound, proven in Lean: no finish is shorter than the best corner solution of the right parity. At 5qt it proves "no 12" for 13% of DRs, at 4qt for 5%. It needs the *optimal* corner solutions of both parities, so it's a read for when you've written the skeletons down anyway.

As an odds read, L does about what HTR length does (table in section 3). Appendix B splits the big high-qt subsets by L and parity. For 2c4 4e: with L = 8, 13–17% finish in 12. With L = 11, 2%. With L = 12, 1.6% if the E-slice is even and none if it's odd.

The E-slice parity on its own, without L, is a small read but it's free. It mostly decides whether the finish wants to be even or odd in length. At 4qt, 8.1% finish in 12 with an odd E-slice against 5.5% with an even one. At 5qt it's the other length that moves: 17.6% finish in 13 with an odd E-slice against 10.3% with an even one.

### 4.6 The last DR move

Zagros asked what one invertible move is worth. If your DR ends in R, then R' is also a DR and its state is yours plus an R2, so you get the better of two finishes.

| | Pure DR | Last move invertible |
|---|---:|---:|
| average optimal, all DRs | 13.58 | 13.26 |
| finishes in 12, 1–2qt | 35% | 49% |
| 3qt | 20% | 30% |
| 4qt | 6.8% | 11% |
| 5qt | 2.1% | 3.7% |

A third of the time the other DR is one shorter, a third the same, a third one longer, in every subset. So it's worth 0.33 moves flat. (If you could pick any of the four side half turns it would be 0.73.)

---

## 5. Bounds people use, graded

A bound is only a bound if it never exceeds the optimal. Graded on all states:

| Bound | Ever too high? | Its average | Average optimal there |
|---|---|---:|---:|
| longer HTR, normal or inverse (all DRs) | never (proven) | 9.22 | 13.58 |
| best corner solution with the right E-parity (all DRs) | never (proven) | 9.44 | 13.58 |
| Levi's 1qt formula, HTR normal + HTR inverse − 1 (4a1 4e) | never for a finish with one quarter turn. A finish with three is shorter for 11.7% of 4a1 4e | 10.85 | 12.27 |
| setup + HTR, any qt (below) | never for a finish with the minimum number of quarter turns. A finish with more is shorter for 2.6% at 1–2qt and 0.002% above | see below | |

**Levi's formula.** (HTR normal) + (HTR inverse) − 1 bounds the finishes with one quarter turn, which is what Levi's doc uses it for. (His doc writes it as the path to the trigger on normal + on inverse + 1. An HTR is that path plus the quarter turn, so it's the same number.) A 1qt state can also be solved with three quarter turns, and the number worth having is how often that is shorter. Over all 286,654,464 states of 4a1 4e, the optimal is below the formula for 11.7% (by 1 in 8.4%, by 2 in 2.7%, by 3+ in 0.6%), equal for 18.0%, above for 70.3%. If the formula says ≤ 12, a 3qt finish beats it 2.5% of the time. Example:

    U2 F2 R2 B2 U D2 B2 R2 B2 R2 F2   // 4a1 4e. HTR is 6 on normal, 5 on inverse, formula says 10
    U B2 L2 F2 D F2 D                  // 7

(Both lines are proven in Lean.) For 4a1 2e optimal is below the formula 44% of the time and for 4a1 0e 95%, so the formula is only for 4c4e, like Levi says. (4a1 2e and 0e are fine DRs to solve. It's the formula that doesn't apply to them, because they can't be finished with one quarter turn.)

One more thing about 4a1 4e that I haven't seen written down: for 72 of its 432 cases (one in six) the shortest HTR is not a 1qt HTR at all. The shortest 1qt path is 8, 9 or 10 moves and a 3qt HTR does it in 7 or 8. So "shortest HTR" and "shortest way to the trigger" are different numbers there, and the formula wants the second. One where it happens on both sides:

    U L2 R2 U R2 B2 U L2          // 4a1 4e
    U L2 F2 L2 U B2 U             // shortest HTR on normal: 7, three quarter turns
    R2 F2 U2 R2 F2 U2 L2 D        // shortest HTR with one quarter turn: 8
    L2 U' B2 R2 U' R2 L2 U'       // optimal finish: 8

(The inverse is the same: 7 with three quarter turns, 8 with one.)

**The bound against the real leave slice** (count quackula's question). For 4a1 4e, leave slice minus formula:

| −3 or less | −2 | −1 | +0 | +1 | +2 | +3 | +4 or more |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 1.7% | 5.4% | 12.6% | 26.9% | 25.8% | 15.9% | 7.9% | 3.8% |

Average +0.70. The leave slice is below the formula 19.7% of the time, more often than the full finish is, because leaving the slice is easier.

**Setup + HTR at any qt.** trangium's "true 2q bound" ([[T11428]]) is (shortest HTR on one side) + (half turns before the first qt on the other side). FakeMMAP pointed out it works for more qts. The general version: on each side count the fewest half turns you need before some quarter turn lowers the qt count, add the shortest HTR of the other side, take the bigger of the two sums. At 1qt this is Levi's formula. Like Levi's, it's only a bound for finishes that use the minimum number of qts.

| | Beaten by extra qts | Exact | 1 under | 2 under | 3+ under | Its average | Longer HTR | Optimal |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1–2qt | 2.6% | 4.0% | 11% | 18% | 64% | 9.62 | 7.66 | 12.75 |
| 3qt | 0.00% | 0.3% | 2.3% | 9.5% | 88% | 9.22 | 8.60 | 13.23 |
| 4qt | 0.00% | 0.3% | 2.6% | 13% | 84% | 10.35 | 9.83 | 13.89 |
| 5qt | 0.00% | 0.1% | 0.8% | 6.3% | 93% | 10.47 | 10.47 | 14.30 |

A finish with extra quarter turns gets under it for 23.8% of 4a1 4e (more than the 11.7% for Levi's formula because this one uses the real setup, see above), 2.2% of 4a2 4e, 1.3% of 4a2 0e, 0.9% of 4b2 4e, and for 0.002% of everything at 3qt and up. So from 3qt it's as good as a true bound. One state for every subset where it happens (there are 13):

| Subset | Scramble | Setup + HTR bound | Optimal finish |
|---|---|---:|---|
| 4a1 4e | `D' F2 R2 U' B2 F2 D` | 15 | `D' F2 B2 U R2 F2 D` (7, 3 quarter turns against a minimum of 1) |
| 4a2 0e | `D' F2 D2 L2 U F2 D' B2 U2 R2 U` | 13 | `U' R2 U2 B2 D F2 U' L2 D2 F2 D` (11, 4 quarter turns against a minimum of 2) |
| 4a2 2e | `D' L2 D' B2 F2 U' F2 D'` | 10 | `D F2 U F2 B2 D L2 D` (8, 4 quarter turns against a minimum of 2) |
| 4a2 4e | `D B2 D L2 D F2 U F2 U' L2 U` | 15 | `U' L2 U F2 U' F2 D' L2 D' B2 D'` (11, 6 quarter turns against a minimum of 2) |
| 4b2 0e | `D' R2 U' F2 U2 L2 U' R2 D` | 12 | `D' R2 U L2 U2 F2 U R2 D` (9, 4 quarter turns against a minimum of 2) |
| 4b2 2e | `D' F2 U B2 U F2 D'` | 8 | `D F2 U' B2 U' F2 D` (7, 4 quarter turns against a minimum of 2) |
| 4b2 4e | `D L2 U' R2 U' L2 F2 U'` | 12 | `U F2 L2 U R2 U L2 D'` (8, 4 quarter turns against a minimum of 2) |
| 0c3 4e | `U' F2 U F2 U' R2 D L2 U' L2 U R2 U` | 14 | `U' R2 U' L2 U L2 D' R2 U F2 U' F2 U` (13, 7 quarter turns against a minimum of 3) |
| 4c3 2e | `D' B2 D' L2 D' L2 U B2 U'` | 10 | `U B2 U' L2 D L2 D B2 D` (9, 5 quarter turns against a minimum of 3) |
| 4c3 4e | `U' L2 D' B2 U' B2 U L2 D` | 10 | `D' L2 U' B2 U B2 D L2 U` (9, 5 quarter turns against a minimum of 3) |
| 4c4 0e | `U F2 U' F2 U R2 U' F2 U F2 R2 U'` | 13 | `U R2 F2 U' F2 U R2 U' F2 U F2 U'` (12, 6 quarter turns against a minimum of 4) |
| 4c4 2e | `D B2 D R2 U' R2 D L2 D B2 D'` | 12 | `D B2 D' L2 D' R2 U R2 D' B2 D'` (11, 6 quarter turns against a minimum of 4) |
| 4c4 4e | `D B2 D' F2 D F2 D' F2 U F2 U'` | 12 | `U F2 U' F2 D F2 D' F2 D B2 D'` (11, 6 quarter turns against a minimum of 4) |

Daichi's objection ([[T11457]]) holds everywhere: it adds two moves to the HTR bound at 2qt, half a move at 3–4qt, nothing at 5qt (a qt that lowers the count is always available right away), and it sits three or more under optimal for most DRs.

**Rodney's rules at 1qt** are graded in section 9: a true lower bound in all 216 cases, even against DR-breaking finishes.

**So for bounding error stats** (compLex's question): the guaranteed bounds you can compute by hand are on average four moves under optimal. The useful hand bound is still Rodney's, per skeleton, late.

---

## 6. Leave slice, the slice, and width

**Cost of the slice** (JTuu's question): optimal finish minus optimal leave slice.

| | +0 | +1 | +2 | +3 or more | Average |
|---|---:|---:|---:|---:|---:|
| 0qt | 44% | 42% | 14% | 0.6% | +0.71 |
| 1–2qt | 56% | 39% | 5.4% | 0.1% | +0.50 |
| 3qt | 67% | 32% | 1.6% | | +0.35 |
| 4qt | 79% | 20% | 0.5% | | +0.21 |
| 5qt | 85% | 15% | 0.1% | | +0.15 |
| all DRs | 73% | 26% | 1.6% | | +0.29 |

The longer the finish, the more room to fit the slice for free. (+1 happens because the optimal finish doesn't have to be an optimal leave slice with a slice inserted.)

**Width** (JTuu, Zagros: "higher qt means more opt+1"). A cheap measure: how many of the ten moves start an optimal finish.

| Optimal | Average number of optimal first moves | Exactly one |
|---:|---:|---:|
| 10 | 1.3 | 78% |
| 11 | 1.4 | 73% |
| 12 | 1.6 | 64% |
| 13 | 2.0 | 47% |
| 14 | 2.8 | 29% |
| 15 | 4.3 | 8% |
| 16 | 7.6 | 0.2% |

Short finishes are narrow: when a DR has a 12, two times out of three there is exactly one first move that gets it. Long finishes are wide. Higher qt DRs have more optimal first moves (3.1 on average at 5qt against 2.6 at 2qt) only because their optimals are longer.

---

## 7. What a computer can prove from the DR

This is the first version of the doc, kept because it shows where the information is and what any hand rule is up against.

### You can't finish faster than the part you're looking at

Pick something to look at on a DR. Say, only the corners. Ask how many moves it takes to solve *just that*. The real finish solves everything, so it solves the corners too, so it can't be shorter. That's the corner-length bound, and it's the logic of every bound here. Look at more and the bound goes up. A solution read backwards solves the inverse scramble, so the same number computed on the inverse is also a lower bound, and you take the bigger one.

If you look at exactly what Rodney traces at 1qt (the corners, which slice each U/D-layer edge belongs to, its U/D colour, the E-parity) but on the DR state itself, you get one number that no skeleton and no variant can beat, at any qt. I call that NISS@DR. On HTR states with half turns only it *is* FakeMMAP's 216-case table. The catch is that at the DR it has 6,350,400 cases instead of 216.

