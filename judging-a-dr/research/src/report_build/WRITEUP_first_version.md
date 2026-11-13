# DR Bounding at any qt

*Levi's and Rodney's bounding, pushed from 1qt/2qt to every HTR subset. Full BFS numbers, a tool, and a Lean proof.*

November 2026. A name with a date is a link to that message on the FMC solvers Discord (#fmc-theory or #fmc-discussion). Docs and sheets are listed with links at the end.

---

## Introduction

DR Bounding as we have it works late in the solve. Levi's version needs you to be at 1qt 4c4e. Rodney's Advanced DR Bounding lets you bound at 2qt, but only after you've picked a corner skeleton and walked it down, and the bound you get is for that variant, not for the DR.

That's the wrong end of the solve for the cases that hurt most. With a 4qt or 5qt DR you have a pile of skeletons (2c5 has 27 qt-optimal normal forms, [FakeMMAP, 14 Jan 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1461009596217950296)), each with a pile of variants, and almost all of them are bad. What you want is to look at the DR, before any of that, and know "this can't be sub-13, next".

Turns out you can, and it's the same idea as before, just applied to the DR state itself instead of the 1qt state:

- **One principle covers everything we already use**: shortest HTR, corner length, Levi's bound, Rodney's NISS@1qt penalties, FakeMMAP's 216-case table. They are all "how fast can the part I'm looking at be solved". I'll make that precise below; it's short.
- **You can read Rodney's NISS@1qt features straight off the DR** (and off its inverse), at 3qt, 4qt, 5qt, whatever. I call that **NISS@DR**. The bound you get is already minimised over every skeleton, every variant, every insertion and any number of extra qts, because it never mentions a skeleton.
- I BFSed the full DR group (all 19,508,428,800 states) so every bound can be compared with the real optimal. For 5qt DRs, NISS@DR proves "no 12-move finish" for 59% of them. If you look at everything that's visible it's 95% (the truth is 98%). Shortest HTR on both sides proves it for 0.0%.
- A few things fall out that you can use at the table with no computer: an **E-slice parity rule** that adds +1 or +2 to the corner length for about half of all DRs, exact odds for every subset, and a warning about Levi's formula (it's not actually a lower bound 11.7% of the time).
- The 216 NISS@1qt cases are now settled for HT-only, DR moves, and DR-breaking finishes. FakeMMAP's HTR-breaking table is right in 211 of 216 cells.
- All of the bounds are **proven in Lean**: valid for every DR state, both sides, any DR-move finish. So is the optimal itself: for every one of the 19.5 billion DR states there's a Lean theorem giving the exact length of its shortest DR-move finish, which makes "18 is God's number for DR moves" a formal theorem too. About 2,500 lines, no gaps.

What it isn't: a method you can run in your head for the strong versions. The strongest table has 406 million cases. The top levels are for tools, training and stats. The parity rule and the odds are for solves.

**What's proven and what's "only" computed.** Proven in Lean: every bound is a true lower bound (both sides), each table is the exact best case for what it looks at, the match with FakeMMAP's 216 HT-only values, a concrete counterexample to Levi's formula, and the exact optimal of every DR state (no finish is shorter, one of exactly that length exists, and the maximum is 18). Computed, not formally proven: all the percentages and averages below, and the DR-breaking optimals in the 216-case section. The percentages are counts made by a separate Rust program over its own BFS table, cross-checked against Joba's numbers and nissy. That table is the same as the Lean-proven one in all 1,339,269,120 entries, so what's unproven there is the counting, not the optimals.

---

## Where this comes from

- **Levi Gibson's "DR Bounding" doc** (posted [27 Nov 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1311464464737898589) in #fmc-discussion). At 1qt 4c4e the finish is `[A] U [B]` with A and B all half turns. A can't be shorter than the shortest path to the trigger on normal, B can't be shorter than on inverse. So finish ≥ (HTR normal) + (HTR inverse) − 1.
- **Rodney Kinney's "Advanced DR Bounding [Beta]" doc** (posted [29 Aug 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1543125354120609832), reworked [8 Sep 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1547045595556872202)). Solution = L + S + T + N: corner skeleton, extra moves to set up the trigger, extra moves in the trigger, extra moves after HTR. N gets bounded from what you NISS-trace at 1qt: HH/RD/RV/DD corners, H/D/V edge pairs, cs-parity, fr-parity, bad slices.
- **FakeMMAP's BFS** ([6 Sep 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1546077655328104509) onwards; the listing, the script and the tables are attached to those posts). 216 cases = 12 corner cases × 3 M-slice patterns × 3 S-slice patterns × E-parity, with the exact HT-only movecount for each. Rodney tuned the rules against it ([Rodney, 18 Sep 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1550363053625708656); the "Adv DR Bounding" sheet). FakeMMAP's newer "OBL++" sheet ([10 Nov 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1569733747526598676)) splits by F/R parity and adds some HTR-breaking stuff.
- **Stats we already had**: Joba's optimal DR finish distribution for all 48 subsets over every DR state ([Joba, 17 Aug 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1406633631165714492)), the 48 subsets ([Jack Love, 8 Oct 2022](https://discord.com/channels/1007840975726575667/1007841335434285126/1028291202849705984); Mallard builds its subset table from them), wen's corner subset sheet "HTR better smh (v2)".
- **Earlier shots at higher qt**: trangium's "true 2q bound" ([trangium, 27 Mar 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1487207920256024738), only valid if you don't use extra qts), the h-sequence inequalities from compLex and FakeMMAP ([compLex, 12 Sep 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1416104938710372434)), Zagros's hunch that corner case + HTR length on both sides predicts optimal ([Zagros, 4 Apr 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1490097940641878216)).

Terms are used the way the server uses them. Bad corners/edges are counted up to turning both layers (that's why wen's sheet says "0 or 8 bad corners" and 4C2E is the same subset as 4C6E, [Jay, 10 Oct 2022](https://discord.com/channels/1007840975726575667/1007841335434285126/1029189050336280627)). The Q in 2c**4** is the corner qt count.

---

## The idea

### You can't finish faster than the part you're looking at

Pick something to look at on a DR. Say, only the corners. Ask how many moves it takes to solve *just that*. The real finish solves everything, so it solves the corners too, so it can't be shorter. That's the corner-length bound, and that's the whole logic of every bound in this doc.

Look at more and the bound goes up:

| What you look at | What the bound is |
|---|---|
| which corners and edges are bad | shortest HTR |
| the corners | L, the optimal corner solution |
| corners + bad edges + E-parity | best possible L+S+T: the shortest HTR that also solves corners, with the right number of side turns |
| corners + Rodney's NISS@1qt edge info + E-parity | best possible L+S+T(+N), over every skeleton and variant at once |

The last row is the new thing. In Rodney's method you fix a skeleton, go to 2qt, trace at 1qt on inverse and get +N for *that variant*. If instead you ask "what's the fewest moves to get corners solved and those edge features into their solved pattern, starting from this DR", you get one number that no variant can beat. No skeleton needed, so you can do it at 5qt.

And since a solution read backwards solves the inverse scramble, the same number computed on the inverse is also a lower bound. Take the bigger one. That's all NISS tracing ever was in bounding.

### Why it's a real lower bound

For any choice of "what you look at" there's a table: for everything you might see, the fewest moves to make it look solved. Two things need to hold, and both get checked case by case by computer (that's the Lean part):

1. What you see after a move only depends on what you saw before and the move. (New corners depend on old corners and the move, not on the edges.)
2. One move changes the table value by at most 1.

A finish of n moves starts at the table value and ends at 0, dropping at most 1 per move. So n ≥ table value. Done.

### It's also the best you can do with that info

For every table here, each value is actually reached: among all DRs that look the same, at least one finishes in exactly that many. So you can't squeeze a better bound out of the same info. If you want more, you have to look at more. (Checked for every case of every table against the exact optimal of every DR state. The Lean proof gives the slightly weaker "the part you look at can be solved in exactly that many".)

### One trap

It's tempting to say "half turns don't change the HTR subset, so only qts matter". True for half turns you do *after* a state. False for the half turns of the scramble that come *before* it, and that difference is exactly normal vs inverse. Shortest HTR depends on one, shortest HTR on inverse on the other. (For the group theory people: the HT group isn't normal in the DR group, and the 48 subsets are double cosets merged with their inverses, as KrzychXyz said ([28 Mar 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1355272481208008824); see also [alison40, 28 Jun 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1256200687528841278), [KrzychXyz, 28 Jun 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1256208836235100181)).) I got this wrong in my first sketch.

---

## What to look at: seven levels

All tables use the ten DR moves. "Cases" means positions that look the same at that level. Each row is a level, from least to most information (✓ Lean: the largest value of the first six levels, so 13 is the longest DR → HTR):

| Level | What you look at | Cases | Largest value, moves |
|---|---|---:|---:|
| HTR length | which corners and edges are bad | 29,400 | 13 |
| Corner length L | corners | 40,320 | 13 |
| L with parity | corners + E-slice parity | 80,640 | 14 |
| L+S+T | corners + which edges are bad + E-parity | 5,644,800 | 15 |
| **NISS@DR** | Rodney's NISS@1qt info: corners up to a free U2; where the M-slice and S-slice edges sit; their U/D colours up to swapping white and yellow within a slice; E-parity | 6,350,400 | 15 |
| NISS@DR + H-perm parity | same, no free U2, plus the double-swap parity | 25,401,600 | 16 |
| Everything visible | corners; slice and colour of the edge in every U/D position; double-swap parity | 406,425,600 | 17 |

The real optimal maxes out at 18 (1,352 states, the number Reid gave, quoted by [Tomas Rokicki, 31 May 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1510792489236430968)).

A few notes on the levels:

- **NISS@DR on HTR states with half turns only *is* FakeMMAP's table.** FakeMMAP's 216 example scrambles are 216 different cases and every value matches (both proven in Lean). So NISS@DR is that table grown from 216 cases to 6.35 million: one for every corner state and edge layout a DR can have.
- **"Up to swapping white and yellow"** is Rodney's *reflection* ("yellow FH edges with white HH corners", +2). The last level looks at the actual colours, so reflection is built in.
- **Double-swap parity** is the H-perm thing FakeMMAP and Rodney went back and forth on ([here](https://discord.com/channels/1007840975726575667/1007841335434285126/1546101477334978650) and [here](https://discord.com/channels/1007840975726575667/1007841335434285126/1546232388013785088)): are the four M-slice edges, read in order, an even or odd arrangement, and same for S. On HTR states that's the parity of F2/B2 turns and of R2/L2 turns separately, the F-parity and R-parity of FakeMMAP's "OBL++" sheet. Rodney's guess was about the bound at 1qt: "If there's a way to compute this kind of double-swap parity, the bound would basically be exact" ([Rodney, 6 Sep 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1546126576247247028)). The next table shows what it does at the DR.
- **What the last level still can't see**: which of the two white M-slice edges is which (same for the other three pairs), and the E-slice beyond its parity. So H-perm-style 2e2e's inside a slice and E-slice 3-cycles are the only blind spot.

---

## How good is it

Everything here is an exact count over all 19,508,428,800 DR states. "Bound" = the bigger of normal and inverse.

### How close each level gets

Each row is a level; the columns are its average over all DR states and the share of states where it equals the optimal, or is within one move of it:

| Level | Average bound, moves | Equal to optimal | Within 1 move |
|---|---:|---:|---:|
| HTR length (longer side) | 9.22 | 0.1% | 0.7% |
| Corner length L | 8.86 | 0.1% | 0.8% |
| L with parity | 9.44 | 0.8% | 2.4% |
| L+S+T | 10.99 | 3.4% | 13.6% |
| NISS@DR | 11.68 | 7.6% | 32.8% |
| NISS@DR + H-perm parity | 12.14 | 17.1% | 52.1% |
| Everything visible | 12.86 | 43.8% | 85.8% |
| actual optimal | 13.58 | | |

Carried to the DR, the H-perm parity takes NISS@DR from exact 7.6% of the time to 17.1%, and from within one 32.8% to 52.1%. It takes the real colours as well to get to 43.8% and 85.8%. How close the parity gets the bound at 1qt, where Rodney's guess was made, isn't measured here.

### Throwing DRs away

How often does a level *prove* the finish is 13+ (so no 12)? Percentages are of all DR states in the row.

| Corner qt | Really 13+ | HTR | L+parity | L+S+T | NISS@DR | +H-perm | Everything | Really 14+ | Everything proves 14+ |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1–2qt (4a1, 4a2, 4b2) | 64.7% | 0.0% | 0.0% | 1.9% | 3.8% | 8.2% | 23.9% | 21.2% | 3.8% |
| 3qt (0c3, 2c3, 4c3) | 79.9% | 0.4% | 0.7% | 4.6% | 9.2% | 21.6% | 48.9% | 41.2% | 12.6% |
| 4qt (0c4, 2c4, 4c4) | 93.2% | 0.2% | 5.0% | 16.5% | 34.0% | 53.5% | 81.3% | 70.3% | 41.3% |
| 5qt (2c5, 4b5) | 97.9% | 0.0% | 12.9% | 28.4% | 58.6% | 76.1% | 94.8% | 86.1% | 66.2% |

"The longer your HTR, the more useful it is to have a lower bound" ([Rodney, 6 Sep 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1546184215542898760)). Here's that in numbers. At 1–2qt bounding from the DR does almost nothing, so bound late like Levi and Rodney do. At 4–5qt it kills most DRs on sight.

Rows go by the Q in the subset name, the corner qt count. A few subsets need more actual qts than that: every 0c0 with bad edges needs 2, and 4a1 0e and 4a1 2e need 3.

All 48 subsets are in Appendix A. The big ones:

| Subset | Share of all DRs | Avg optimal | ≤ 12 | ≤ 13 | NISS@DR proves 13+ | Everything proves 13+ |
|---|---:|---:|---:|---:|---:|---:|
| 4b2 4e | 5.88% | 12.73 | 34.4% | 81.9% | 0% | 21% |
| 2c3 4e | 7.84% | 12.94 | 26.7% | 72.5% | 0% | 31% |
| 4c3 4e | 5.88% | 13.50 | 12.0% | 45.3% | 14% | 68% |
| 2c4 4e | 11.76% | 13.66 | 9.1% | 37.9% | 18% | 74% |
| 0c3 4e | 0.73% | 14.64 | 1.5% | 8.9% | 93% | 96% |
| 4c4 4e | 5.88% | 14.38 | 1.8% | 11.8% | 67% | 97% |
| 2c5 4e | 3.92% | 14.30 | 2.6% | 15.3% | 61% | 93% |
| 4b5 4e | 5.88% | 14.29 | 1.8% | 13.3% | 60% | 96% |

---

## Examples

I wrote a small lookup tool for this: give it a scramble and the moves to DR (NISS in brackets) and it prints every level on both sides plus the real optimal, straight from the precomputed tables. The numbers below are its output.

**Rodney's first random scramble** (from the Advanced DR Bounding doc):

    U D L2 D' B2 U R2 F2 B2 D2 L2 D' R2 L2 D2 B2   // 2c3 6e

Rodney goes through three skeletons, kills about a dozen triggers with bounding, finds a 13 and says "to strictly prove it, we'd have to try inserting corner swaps in front of the first qt". From the DR alone:

    HTR length          9 / 7      (normal / inverse)
    corner length L     5 / 5
    L with parity       7 / 7
    L+S+T              10 / 9
    NISS@DR            10 / 11
    + H-perm parity    11 / 12
    everything         13 / 13
    optimal            13

So 13 is optimal, and the last level proves it without picking a skeleton. (✓ Lean: every line but "everything".)

**Rodney's 4a4 example:**

    U R2 L2 F2 U' B2 D2 F2 D L2 U B2 R2 U' F2 U   // 4a4 on normal, 4b4 on inverse, 4e

    HTR 11 / 10,  L 11 / 11,  L+S+T 13 / 11,  NISS@DR 13 / 12,  optimal 13

Here plain NISS@DR on the normal side already says 13. Rodney's 13-mover is optimal, read off a 4qt DR. (✓ Lean: all five.)

**Levi's example** (from the DR Bounding doc), a 10-move 3qt DR:

```
(D2 B' L' B U' F2 D L U2 R)   // 4c3 4e
```

    HTR 9 / 10,  NISS@DR 12 / 12,  everything 14 / 14,  optimal DR finish 15

Levi says "14-move optimal finish, giving a 24". Both are right. The DR ends in R, a finish that starts with a turn of that face merges with it, and the same DR with R' instead has optimal 14. The tool prints both.

---

## What you can use in an actual solve

### The E-slice parity rule

Side half turns (R2 L2 F2 B2) each swap two E-slice edges. U and D never touch the slice. So the number of side turns in *any* DR finish is even if the E-slice is an even permutation (solved, 3-cycle, 2e2e) and odd if it's odd (2-swap, 4-cycle). This is Rodney's fr-parity, used on the whole finish instead of after HTR.

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

So for every 4a2, 0c3 and 0c4, and for most of the rest, exactly one E-parity lets you finish in L. With the wrong one you're at L+1 or L+2 before you've looked at a single edge. At 5qt this alone proves 13+ for 13% of DRs. (Proven in Lean.)

### Odds per subset

For a DR of length d and a target t you need a finish ≤ t − d (one more if the first finish move merges with the last DR move). Share of each subset that finishes in 12 / in 13:

- 4c4, 2c5, 4b5, 0c3: 1.2–5.7% / 9–26%
- 2c4, 4c3: 4.5–20% / 24–59%
- 4a1 and 4b2 with 2e or 4e: 34–53% / 82–91%
- 4a2: 10–26% / 40–64%

Appendix B splits the big high-qt subsets by L and E-parity. For 2c4 4e: with L = 8, 13–17% finish in 12. With L = 11, 2%. With L = 12, 1.6% if the E-slice is even and zero if it's odd.

### HTR length on both sides

Knowing the shortest HTR on normal and inverse (hN, hI) doesn't give a better guarantee than the longer one: in every subset there are states that finish in exactly max(hN, hI). It does move the odds. For 2c4 4e the average optimal goes from 12.67 at (7, 7) to 14.4 at (11, 11), about 0.2 per extra HTR move on either side (0.3–0.4 going from 7 to 8, under 0.15 from 10 to 11). I have that table for every subset if anyone wants one.

### Levi's formula is not quite a lower bound

(HTR normal) + (HTR inverse) − 1 is exact if the finish has one qt. But a 1qt state can also be solved with three, and sometimes that's shorter. Over all 286,654,464 states of 4a1 4e:

| | |
|---|---:|
| optimal is below the formula | 11.7% |
| equal | 18.0% |
| above | 70.3% |

If the formula says ≤ 12, optimal is below it 2.5% of the time. At ≤ 11, 0.6%. So for pruning short targets it's fine, but it's not a strict bound. Example:

    U2 F2 R2 B2 U D2 B2 R2 B2 R2 F2   // 4a1 4e. HTR is 6 on normal, 5 on inverse, formula says 10
    U B2 L2 F2 D F2 D                  // 7

(Both lines are proven in Lean: the two HTR lengths, and that the 7-mover solves it.) For 4a1 2e optimal is below the formula 44% of the time and for 4a1 0e 95%, so only use it on 4c4e like Levi says.

### What I'd do per subset

| Subsets | |
|---|---|
| 0c3, 4c4, 2c5, 4b5 | Skip unless the DR is very short. 1–6% finish in 12, and for 51–93% (depends on the subset) NISS@DR proves 13+. If you do keep one: get L, check E-parity first. |
| 0c4, 2c4, 4c3 | Get L and E-parity before looking for any HTR. For 2c4 4e, L ≥ 11 means about 2% chance of a 12, and L = 12 with an odd E-slice means none. Then Rodney's method on the shortest skeletons only. |
| 2c3, 4b2, 4a2 | Rodney's method as written, this is where it lives. The parity rule tells you at the DR which fr-parity your skeleton has to end with. For 2c3, half of all corner states pay +2 for the wrong one. |
| 4a1 | Levi's formula, read as "almost always". Not with 0e or 2e. |
| 0c0 | 0e/2e/4e are short. For 6e/8e go for the setup first (Rodney's examples in [Rodney, 23 Oct 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1563054901871902741)). |

---

## The 216 NISS@1qt cases, three ways

FakeMMAP's tables, in order:

- the first one is HT only;
- the next adds HTR-breaking finishes from a list of algs: $\le 7$ is proven, and 8/9/10 might secretly be 7-movers ([FakeMMAP, 6 Sep 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1546263650015256606), [FakeMMAP, 7 Sep 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1546599572644696075));
- the newer OBL++ sheet. FakeMMAP on what's in it: "They do include some HTR-breaking stuff." ([[T12425]]) "Maybe all." "But I'm not mathematically 100% sure." ([same day](@T12427)).

Rodney's "Adv DR Bounding" sheet uses those optimals.

Here are all three (the full table is Appendix C). Each row is a move set, how its values were found, and what came out:

| Moves allowed | How | Result |
|---|---|---|
| Half turns | BFS over the 216 cases | same as FakeMMAP's listing, all 216 (proven in Lean) |
| DR moves | same BFS with U and D qts | 214 the same, 2 shorter: "R-D − F-V R-V even" and its mirror "F-D − F-V R-V even" go from 9 to 8 (the count of 2 is proven in Lean) |
| Any face turn (HTM) | every sequence of $\le 10$ moves is two sequences of $\le 5$ glued together, so I listed all 624,124 of those twice, matched the pairs that can land in HTR, and tested each hit | shorter for some cases; the next table has the counts |

How the any-move values compare. Each row is the move set compared against; the columns count the 216 cases by how much shorter any move makes them:

| Compared with | The same | Shorter by 1 | By 2 | By 3 | By 4 |
|---|---:|---:|---:|---:|---:|
| DR moves | 150 | 37 | 22 | 6 | 1 |
| half turns | 150 | 35 | 24 | 6 | 1 |

DR-move values never go above 10, so anything shorter is $\le 9$ moves and a search that's complete to 10 can't miss it.

The two that get shorter with quarter turns, explicitly (with half turns alone both cases need 9):

    L2 B2 D B2 L2 R2 F2 U'      // a state of "R-D − F-V R-V even"
    U F2 R2 L2 B2 D' B2 L2      // solves it in 8

    B2 L2 D L2 B2 F2 R2 U'      // a state of "F-D − F-V R-V even"
    U R2 F2 B2 L2 D' L2 B2      // solves it in 8

- **FakeMMAP's HTR-breaking table ([FakeMMAP, 7 Sep 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1546599572644696075)) is right in 211 of 216 cells.** Two cells labelled 7 are 6-movers, which goes against "Anything labeled with 7 or less is proven to be a lower bound, and the lower bound is proven optimal" ([[T12129]]). Each row is one of the two, with the table's value, the real optimal and a state of the case:

  | Case | Table value, moves | Real optimal, moves | A state of that case |
  |---|---:|---:|---|
  | F-D + F-V R-H odd | 7 | 6 | `R L' B2 D2 R L'` |
  | R-D + F-H R-V odd | 7 | 6 | `F' B R2 D2 F B'` |

  Three of the 9s are 8. Those are inside the caveat FakeMMAP gave for these values: "Again, anything higher than 7 is not proven, those cases could be 7-movers" ([[T12145]]). No 8, 9 or 10 drops to 7. The same columns for the three 9s:

  | Case | Table value, moves | Real optimal, moves | A state of that case |
  |---|---:|---:|---|
  | H-H + F-D R-D odd | 9 | 8 | `R D2 F2 B2 R' L F2 R'` |
  | H-H + F-V R-D odd | 9 | 8 | `L' F2 R L' F2 B2 D2 L` |
  | H-H + F-D R-V odd | 9 | 8 | `F L2 F B' R2 L2 D2 F'` |

  (The inverse of each sequence solves it.)
- **Rodney's sheet** has no optimal column: its Penalty is the finish length minus the corner case's setup (1 move for F-D and R-D corners, 2 for F-V, 0 for H-H). It's built on the same optimals, so the same five are one too high, and the other 211 agree:

  | Case | Sheet penalty | Should be |
  |---|---:|---:|
  | F-D + F-V R-H odd | 6 | 5 |
  | R-D + F-H R-V odd | 6 | 5 |
  | H-H + F-D R-D odd | 9 | 8 |
  | H-H + F-V R-D odd | 9 | 8 |
  | H-H + F-D R-V odd | 9 | 8 |

  One more row, labelled F-V / F-D / R-H, has an alg for a different case. The R2 is a typo for F2, and the same line is in FakeMMAP's 7 Sep listing, where the sheet's algs come from ([[T12144]]):

  ```
  M R2 U2 M'   // the sheet's alg: gives R-V + F-D R-V odd
  M F2 U2 M'   // the labelled case in 6 moves, the sheet's penalty of 4 after the 2-move F-V setup
  ```
- **Rodney's rules are still a true lower bound in all 216 cases**, even against the shorter optimals. The "100%" survives.
- **OBL++** has a finer grid and I didn't grade it cell by cell. Collapsed to these 216 labels it covers 144 cases, matches on 140 of them and already has four of the five fixes above. It's one *lower* in four (D-D ± F-H R-H even, two cases; R-V + F-D R-H even; R-V + F-D R-D odd: 8 vs my 9).

  For those four I ran nissy on all 3,072 states of each case and none has a solution of 8 or fewer, so 9 stands for the cases as I label them. Whether those cells are off or just mean something slightly different, I don't know.

Two sanity checks on my side: listing the HTR group directly gives 663,552 states in 216 cases of exactly 3,072 each, and all 216 sequences in Appendix C land in the case they claim.

This part is a Python script, not Lean. Nothing in either sheet beats its values, including Rodney's `F R2 E2 R2 F'` algs.

---

## The proof, if you don't speak Lean

Lean is a proof checker. You write a statement and a proof, and a small trusted program checks every step. The project is about 2,500 lines, no Mathlib, and it's in this repo under lean/DRBound.

**What's stated.** A DR state is three lists: the piece in each of the 8 corner positions, the 8 U/D edge positions, the 4 E-slice positions. Each of the ten moves shuffles those lists in a fixed way, written out as tables (that file is 150 lines and it's the one to read if you want to convince yourself it's the cube). A solution is a list of moves that puts all three lists in order.

For each level `R` these are the theorems, copied from the files:

```lean
-- every DR-move solution w of a legal state g is at least as long as the bound
theorem Rung.lower_bound (ok : R.Checked) (g : State) (hg : g.Valid) (w : List Move)
    (hw : g.apply w = solved) : R.bound g ≤ w.length

-- same with the bound read off h, the inverse of g
theorem Rung.lower_bound_inverse (ok : R.Checked) (g h : State) (hg : g.Valid)
    (hh : h.IsInverseOf g) (w : List Move) (hw : g.apply w = solved) : R.bound h ≤ w.length

-- and the bound is reached: d moves make g look solved to R
theorem Rung.bound_attained (ok : R.Checked) : ∀ (d : Nat) (g : State), g.Valid → R.bound g = d → d < 255 →
    ∃ w : List Move, w.length = d ∧ R.index (g.apply w) = R.index solved
```

(`d < 255` is there because 255 marks combinations a real cube can't show.) `R.Checked` is the brute-force part, see below.

**How.**

1. A two-page general lemma: if what you see after a move depends only on what you saw and the move, and one move changes the table by at most 1, then n moves change it by at most n. Plain induction on the number of moves, nothing about cubes in it.
2. `R.Checked` is three brute-force checks, done by a program Lean runs:
   - for each of the $8^8 = 16{,}777{,}216$ ways to fill eight positions, if it's a permutation, the case number is in range and the case move table agrees with actually doing each of the ten moves (once for corners, once for edges);
   - on the E-slice, side turns flip the parity and the other moves don't;
   - for every table entry and every move the neighbour differs by at most 1, only the solved case has 0, and every positive entry has a neighbour that's one lower.
3. The table isn't trusted. Lean builds it with its own BFS, but nothing is assumed about that BFS, only the checks are used. A wrong table or a wrong feature would fail a check and the file wouldn't compile.
4. The inverse side needs one more fact, proven by hand: if w solves g, the inverse of g is exactly what w does to a solved cube. So its table value is at most the length of w.

**The optimal itself.** Same trick, one size up: take the table of *everything*, one entry per DR state, holding its optimal. That's 19.5 billion entries, so it's stored up to the 16 symmetries that keep the U/D axis, one byte per entry:

$$\underbrace{2{,}768}_{\text{corner classes}} \times \underbrace{40{,}320}_{\text{edge arrangements}} \times \underbrace{12}_{\text{E-slice arrangements}} = 1{,}339{,}269{,}120 \text{ entries}$$

Lean builds it with its own BFS and then checks every entry against each of the ten moves for the same three things as before: a move changes the value by at most 1, only the solved cube has 0, and every positive entry has a move that goes down by 1. On top of that it checks

- that entries the symmetries identify hold the same value,
- nine brute-force facts about the bookkeeping: the 16 symmetries map legal states to legal states, turn each move into a move and form a group; every corner arrangement is carried to the representative of its class; moves change the three parities the way they should; and the numbering of edge and E-slice arrangements round-trips.

From those:

```lean
-- every solution of g has at least exactDist g moves
theorem exact_lower (g : State) (hg : g.Valid) (hp : g.ParityOK) (w : List Move)
    (hw : g.apply w = solved) : exactDist g ≤ w.length

-- and some solution has exactly that many
theorem exact_attained (g : State) (hg : g.Valid) (hp : g.ParityOK) :
    ∃ w : List Move, w.length = exactDist g ∧ g.apply w = solved

-- nothing needs more than 18, and something does need 18
theorem exact_le_18 (g : State) (hg : g.Valid) : exactDist g ≤ 18
theorem exact_needs_18 : ∃ g : State, g.Valid ∧ g.ParityOK ∧ exactDist g = 18 ∧
    ∀ w : List Move, g.apply w = solved → 18 ≤ w.length
```

`Valid` says the three lists are permutations, `ParityOK` is the usual parity condition (corner parity + U/D edge parity = E-slice parity). Together that's exactly the states DR moves can reach: Lean proves both directions (anything you can scramble to satisfies them, and anything that satisfies them gets solved by `exact_attained`). `exactDist g` is the table entry of g's symmetry-reduced image. The witness:

```
U2 L2 D B2 U' B2 U' L2 D B2 R2 U R2 U R2 U2 R2 U'   // needs 18
```

In the same run Lean counts the table, at depths 0 to 18:

1, 10, 67, 456, 3079, 19948, 123074, 736850, 4185118, 22630733, 116767872, 552538680, 2176344160, 5627785188, 7172925794, 3608731814, 224058996, 1575608, 1352

That's 19,508,428,800 in total, where an entry counts $16/s$ times, $s$ being the number of symmetries fixing the representative of its corner class. Same numbers as the Rust BFS.

The one step that is *not* formalised is that this weighting counts states: that an entry stands for exactly that many of them. It's the standard orbit count, but here it's a paper argument, not a Lean theorem. So "1,352 states at 18" is proven up to that step, and "some state needs 18, none needs more" is proven outright.

**What's proven.** `R.Checked` for all seven levels, so all seven bounds, both sides. Plus the HT-only version of NISS@DR, that it equals FakeMMAP's 216 values, that exactly 2 of them get shorter with qts, a 4a1 4e where a 3qt finish beats Levi's formula, and the exact optimal of every DR state with its maximum of 18.

**The examples on this page.** The DR states this write-up prints with an optimal finish or an HTR length are in a list Lean reads back from the page. It has 198 stated optimals, of 167 different states: the typical DR of every corner case (section 4.3 and Appendix E), both columns of Appendix G, the setup + HTR examples of section 5, and the ones in the text. (Not in it: the sequences of Appendix C, which are any-move values, and the corner setups of Appendix E.) Proven for that list:

- each stated optimal is exact (a lookup in the table above, so the same theorem);
- each of the 20 printed finishes solves its state in the length given;
- the 55 stated HTR lengths, on normal and on inverse, and the two printed HTRs of section 5;
- the levels printed for Rodney's two examples in section 7 (all but "everything") and the corner length with parity of the two examples in section 4.5;
- the largest value of the first six levels: 13, 13, 14, 15, 15, 16. The first is the longest DR → HTR, so 13 and not 12;
- for the two 2c4 4e of section 3 that finish in 7 and in 16: 7 to HTR and corner length 7 on both sides (not the corner case);
- with NISS the longest DR → HTR isn't 11 either. This 0c3 4e, 13 on both sides, has no NISS HTR of 11 or less and one of 12:

  ```
  B2 U B2 R2 D' L2 U B2 D' F2 D' L2 F2 U' R2 U
  U R2 U2 F2 U' F2 R2 U (B2 U L2 U)                // 12 to HTR, the bracket on inverse
  ```

  Lean runs through every way to put up to five moves on one side and takes the shortest HTR from there, on normal and on inverse. That covers every NISS HTR of 11 or less, because one of its two sides has five moves or fewer. That last sentence is the one step that's an argument and not a Lean theorem.

The errata's scrambles are proven the same way (subset names included), in the Lean project of the HTR routes study.

The two biggest checks Lean runs, one per row:

| Check | Entries read (against ten moves each) | Time | Memory |
|---|---:|---|---|
| biggest bound check | 406,425,600 | about 4.5 minutes | 0.9 GB |
| exact-optimal check | 1,339,269,120 | 17 minutes | 1.9 GB |
| the examples on this page | the table built once more, then looked up | 16 minutes | 1.9 GB |

The first two build in under half an hour, in 3 GB of RAM if the exact-optimal check is run on its own. The examples are a separate run.

**What you have to trust.**

- That the move tables are the cube. They're short, and the same tables drive a separate Rust program (and an older C one with byte-identical output) whose results match Joba's per-subset counts and nissy on 40 random DRs.
- Lean's kernel, and its compiler: the brute-force checks run as compiled code (`native_decide`), which adds one axiom per check on top of the three standard ones. The general lemma itself uses none of them.

**What's not in Lean.** The stats (they're counts over the optimal of every state: the optimal is proven now, the counting isn't), the weights in the depth distribution above, the subset labels, corner cases and pair counts, the leave slice and the setup lengths, and the DR-breaking search.

---

## How it was computed and checked

- **Optimal for every DR state**: a Rust program does a BFS over the DR group reduced by the 16 symmetries that keep the U/D axis (1.34 billion reduced states, one bit per state per depth, under a minute on 4 cores, 500 MB of RAM).
- **The seven tables**: BFS over the cases of each level, then one pass over all DR states comparing bound and optimal.
- **The 216 cases with any move**: a Python script, as described above, plus nissy for the disputed cells.
- **The proof**: the Lean project builds its own tables from its own definitions. It shares nothing with the Rust code except the ten move tables and, for the exact table, the numbering of the symmetry-reduced states (so the two tables can be compared entry by entry).

What agreed with what. Each row is a check (with what it was checked against, where that is someone else's result) and its result:

| Check | Result |
|---|---|
| Total and depth distribution | 19,508,428,800; 1,352 at 18 ([Tomas Rokicki, 31 May 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1510792489236430968)) |
| Joba's optimal distribution, all 48 subsets ([Joba, 17 Aug 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1406633631165714492)) | same in every cell |
| Subset sizes, qt class sizes ([Oskar, 10 Jun 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1249777335239184405), [Joba, 3 Apr 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1357402650441945299)), 4a3↔4b3 on inverse (wen's "HTR better smh (v2)" sheet) | same |
| FakeMMAP's 216 values ([FakeMMAP, 6 Sep 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1546077758189477989)) | same |
| FakeMMAP's corner counts per qt from 0qt to 5qt, 24, 144, 720, 1416, 1776 and 960 of 5040 ([FakeMMAP, 26 Aug 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1144917908078723112), FakeMMAP asked someone to check them) | confirmed |
| Lean's proven optimal table vs the Rust BFS | same in all 1,339,269,120 entries, and the same depth distribution |
| Lean vs the Rust program, bound tables | same case counts (96, 420, 70, 5040, 630, 10080), same distribution of the corner and HTR tables, same bounds on the examples |
| Rust vs the first C version | every output byte-identical |
| nissy `drudfin` on 40 random DRs | same optimal on all 40 |
| Bounds vs optimal | never above it, any level, any of the 19.5 billion states |

---

## What this doesn't do

- **DR moves only.** "Optimal" here is U, D, R2, L2, F2, B2, same as nissy's `drudfin` and the stats on the server. DR-breaking finishes can be shorter: at the HTR level that's 66 of the 216 cases. A bound that holds for all 18 moves over the whole DR group is too big for this machine.
- **The last DR move.** A finish that starts on the face of the last DR move merges with it. Compare the bound with target − DR length + 1, or bound the DR with its last move inverted as well (my tool does both).
- **Not human at the top.** Parity rule and odds: yes. NISS@DR for 2qt subsets: that's what Rodney's rules already are. The stronger levels are for software.
- **What the best level misses.** The last 0.72 moves on average are 2e2e's inside a slice and the E-slice. A "leave slice" level that sees all U/D edges exactly has 1.6 billion cases and can be done the same way.
- **Stats are counted, not proven.** The optimal of every state is a Lean theorem, and the Rust table the stats are counted from is that same table, entry for entry. What isn't formal is the counting on top: the percentages, the per-subset splits, and the symmetry weights behind "1,352 states at 18".
- **Rules.** Rodney's bad-slice rules are a compact description of NISS@1qt. Whether NISS@DR at 3–5qt has an equally compact description, I don't know. The tables to test a guess against exist now.

---

## Appendix A: all 48 subsets

Exact over all DR states. "Proves 13+" = share of the subset where that level, on the better of normal and inverse, shows there is no 12-move finish.

| Subset | Share of all DRs | Avg optimal | Min | ≤ 12 | ≤ 13 | L+parity proves 13+ | NISS@DR proves 13+ | Everything proves 13+ | Everything proves 14+ |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0c0 0e | 0.01% | 9.95 | 0 | 99.2% | 100.0% | 0% | 0% | 0% | 0% |
| 0c0 2e | 0.11% | 11.69 | 5 | 79.9% | 99.0% | 0% | 0% | 1% | 0% |
| 0c0 4e | 0.24% | 12.31 | 4 | 53.1% | 92.5% | 0% | 0% | 8% | 0% |
| 0c0 6e | 0.11% | 12.92 | 7 | 27.0% | 75.2% | 0% | 1% | 21% | 1% |
| 0c0 8e | 0.01% | 12.69 | 6 | 38.6% | 78.0% | 0% | 3% | 20% | 3% |
| 4a1 0e | 0.08% | 13.01 | 7 | 24.0% | 70.3% | 0% | 12% | 43% | 6% |
| 4a1 2e | 1.31% | 12.56 | 6 | 42.3% | 87.8% | 0% | 0% | 11% | 0% |
| 4a1 4e | 1.47% | 12.27 | 1 | 53.2% | 91.1% | 0% | 0% | 9% | 0% |
| 4a2 0e | 0.08% | 13.91 | 9 | 6.1% | 28.5% | 0% | 57% | 84% | 48% |
| 4a2 2e | 1.31% | 13.65 | 8 | 10.0% | 39.5% | 0% | 28% | 69% | 28% |
| 4a2 4e | 1.47% | 13.05 | 5 | 26.4% | 63.7% | 0% | 16% | 46% | 13% |
| 4b2 0e | 0.33% | 12.89 | 6 | 28.5% | 74.3% | 0% | 1% | 33% | 2% |
| 4b2 2e | 5.22% | 12.61 | 3 | 39.3% | 84.9% | 0% | 0% | 15% | 0% |
| 4b2 4e | 5.88% | 12.73 | 4 | 34.4% | 81.9% | 0% | 0% | 21% | 0% |
| 0c3 0e | 0.02% | 14.08 | 10 | 5.7% | 25.9% | 14% | 80% | 86% | 61% |
| 0c3 2e | 0.33% | 14.27 | 9 | 3.7% | 17.4% | 14% | 67% | 93% | 71% |
| 0c3 4e | 0.73% | 14.64 | 10 | 1.5% | 8.9% | 14% | 93% | 96% | 83% |
| 0c3 6e | 0.33% | 14.29 | 9 | 3.7% | 17.6% | 14% | 66% | 93% | 71% |
| 0c3 8e | 0.02% | 14.14 | 10 | 5.6% | 24.8% | 14% | 80% | 86% | 62% |
| 2c3 0e | 0.22% | 13.39 | 9 | 12.4% | 51.9% | 0% | 11% | 63% | 13% |
| 2c3 2e | 3.48% | 12.55 | 5 | 42.0% | 87.9% | 0% | 0% | 10% | 0% |
| 2c3 4e | 7.84% | 12.94 | 5 | 26.7% | 72.5% | 0% | 0% | 31% | 1% |
| 2c3 6e | 3.48% | 13.20 | 7 | 17.4% | 61.1% | 0% | 0% | 45% | 2% |
| 2c3 8e | 0.22% | 13.52 | 9 | 9.6% | 44.8% | 0% | 11% | 67% | 15% |
| 4c3 0e | 0.33% | 13.31 | 8 | 17.0% | 54.1% | 0% | 16% | 58% | 17% |
| 4c3 2e | 5.22% | 13.48 | 7 | 12.0% | 45.8% | 0% | 9% | 67% | 18% |
| 4c3 4e | 5.88% | 13.50 | 7 | 12.0% | 45.3% | 0% | 14% | 68% | 20% |
| 0c4 0e | 0.01% | 13.22 | 9 | 17.4% | 60.7% | 0% | 0% | 46% | 2% |
| 0c4 2e | 0.22% | 13.52 | 9 | 8.9% | 43.8% | 0% | 4% | 77% | 11% |
| 0c4 4e | 0.49% | 13.64 | 9 | 6.9% | 37.2% | 0% | 9% | 82% | 16% |
| 0c4 6e | 0.22% | 13.90 | 10 | 3.6% | 24.5% | 0% | 27% | 90% | 35% |
| 0c4 8e | 0.01% | 14.18 | 11 | 1.9% | 15.6% | 0% | 56% | 92% | 51% |
| 2c4 0e | 0.33% | 13.22 | 7 | 20.0% | 58.5% | 1% | 15% | 50% | 12% |
| 2c4 2e | 5.22% | 13.53 | 7 | 11.5% | 44.1% | 1% | 12% | 68% | 20% |
| 2c4 4e | 11.76% | 13.66 | 7 | 9.1% | 37.9% | 1% | 18% | 74% | 26% |
| 2c4 6e | 5.22% | 13.73 | 8 | 7.7% | 34.9% | 1% | 20% | 78% | 30% |
| 2c4 8e | 0.33% | 14.02 | 9 | 4.5% | 24.1% | 1% | 47% | 83% | 44% |
| 4c4 0e | 0.33% | 14.54 | 10 | 1.2% | 8.8% | 14% | 75% | 96% | 76% |
| 4c4 2e | 5.22% | 14.42 | 9 | 1.5% | 10.6% | 14% | 71% | 97% | 76% |
| 4c4 4e | 5.88% | 14.38 | 9 | 1.8% | 11.8% | 14% | 67% | 97% | 73% |
| 2c5 0e | 0.11% | 14.42 | 10 | 1.5% | 11.4% | 22% | 78% | 95% | 71% |
| 2c5 2e | 1.74% | 14.28 | 9 | 2.5% | 15.5% | 22% | 59% | 93% | 62% |
| 2c5 4e | 3.92% | 14.30 | 9 | 2.6% | 15.3% | 22% | 61% | 93% | 63% |
| 2c5 6e | 1.74% | 14.42 | 9 | 1.7% | 11.7% | 22% | 65% | 95% | 70% |
| 2c5 8e | 0.11% | 14.46 | 10 | 1.5% | 11.0% | 22% | 81% | 95% | 72% |
| 4b5 0e | 0.33% | 14.30 | 9 | 2.0% | 13.1% | 7% | 62% | 94% | 66% |
| 4b5 2e | 5.22% | 14.26 | 9 | 2.0% | 14.0% | 7% | 51% | 96% | 66% |
| 4b5 4e | 5.88% | 14.29 | 9 | 1.8% | 13.3% | 7% | 60% | 96% | 69% |

## Appendix B: odds by corner length and E-slice parity

For the big 3–5qt subsets. L = optimal corner solution. "Min" is the best case for that row, so `L+1` means no L-move finish exists there.

| Subset | L | E-slice | Share of subset | Min | Avg optimal | ≤ 12 | ≤ 13 |
|---|---:|---|---:|---|---:|---:|---:|
| 4c3 4e | 7 | even | 2.8% | 8 (L+1) | 13.03 | 22.0% | 67.7% |
| 4c3 4e | 7 | odd | 2.8% | 7 (L+0) | 12.95 | 28.8% | 69.7% |
| 4c3 4e | 8 | even | 11.1% | 8 (L+0) | 13.15 | 19.1% | 63.9% |
| 4c3 4e | 8 | odd | 11.1% | 9 (L+1) | 13.20 | 19.0% | 59.7% |
| 4c3 4e | 9 | even | 19.4% | 9 (L+0) | 13.43 | 10.8% | 49.0% |
| 4c3 4e | 9 | odd | 19.4% | 9 (L+0) | 13.45 | 13.2% | 47.4% |
| 4c3 4e | 10 | even | 13.9% | 11 (L+1) | 13.80 | 3.6% | 32.4% |
| 4c3 4e | 10 | odd | 13.9% | 10 (L+0) | 13.86 | 7.5% | 25.4% |
| 4c3 4e | 11 | even | 2.8% | 11 (L+0) | 14.05 | 2.5% | 16.9% |
| 4c3 4e | 11 | odd | 2.8% | 11 (L+0) | 14.13 | 2.8% | 21.1% |
| 0c3 4e | 9 | even | 2.8% | 11 (L+2) | 13.68 | 4.5% | 38.0% |
| 0c3 4e | 9 | odd | 2.8% | 10 (L+1) | 13.86 | 8.7% | 30.3% |
| 0c3 4e | 10 | even | 11.1% | 11 (L+1) | 14.22 | 0.9% | 22.1% |
| 0c3 4e | 10 | odd | 11.1% | 12 (L+2) | 14.16 | 6.5% | 10.0% |
| 0c3 4e | 11 | even | 22.2% | 12 (L+1) | 14.73 | 0.4% | 8.4% |
| 0c3 4e | 11 | odd | 22.2% | 12 (L+1) | 14.72 | 0.8% | 4.6% |
| 0c3 4e | 12 | even | 13.9% | 13 (L+1) | 14.96 | 0.0% | 0.2% |
| 0c3 4e | 12 | odd | 13.9% | 13 (L+1) | 15.09 | 0.0% | 4.0% |
| 2c4 4e | 7 | even | 2.8% | 8 (L+1) | 13.15 | 15.0% | 66.3% |
| 2c4 4e | 7 | odd | 2.8% | 7 (L+0) | 13.15 | 23.2% | 58.7% |
| 2c4 4e | 8 | even | 11.1% | 8 (L+0) | 13.29 | 13.4% | 58.6% |
| 2c4 4e | 8 | odd | 11.1% | 9 (L+1) | 13.37 | 16.6% | 49.4% |
| 2c4 4e | 9 | even | 17.0% | 9 (L+0) | 13.61 | 6.6% | 41.1% |
| 2c4 4e | 9 | odd | 17.0% | 9 (L+0) | 13.58 | 11.4% | 38.8% |
| 2c4 4e | 10 | even | 13.2% | 10 (L+0) | 13.84 | 3.9% | 30.8% |
| 2c4 4e | 10 | odd | 13.2% | 10 (L+0) | 13.90 | 6.5% | 23.7% |
| 2c4 4e | 11 | even | 5.2% | 11 (L+0) | 14.16 | 2.0% | 13.7% |
| 2c4 4e | 11 | odd | 5.2% | 11 (L+0) | 14.28 | 1.9% | 16.1% |
| 2c4 4e | 12 | even | 0.7% | 12 (L+0) | 14.37 | 1.6% | 2.8% |
| 2c4 4e | 12 | odd | 0.7% | 13 (L+1) | 14.55 | 0.0% | 12.3% |
| 4c4 4e | 9 | even | 2.8% | 9 (L+0) | 13.79 | 4.4% | 30.8% |
| 4c4 4e | 9 | odd | 2.8% | 10 (L+1) | 13.85 | 7.2% | 29.4% |
| 4c4 4e | 10 | even | 11.1% | 11 (L+1) | 14.03 | 2.9% | 21.1% |
| 4c4 4e | 10 | odd | 11.1% | 10 (L+0) | 14.05 | 4.5% | 18.8% |
| 4c4 4e | 11 | even | 22.2% | 11 (L+0) | 14.37 | 1.4% | 8.1% |
| 4c4 4e | 11 | odd | 22.2% | 11 (L+0) | 14.42 | 1.1% | 13.1% |
| 4c4 4e | 12 | even | 13.9% | 12 (L+0) | 14.68 | 0.6% | 1.6% |
| 4c4 4e | 12 | odd | 13.9% | 13 (L+1) | 14.79 | 0.0% | 5.8% |
| 0c4 4e | 9 | even | 16.7% | 9 (L+0) | 13.62 | 5.4% | 36.5% |
| 0c4 4e | 9 | odd | 16.7% | 10 (L+1) | 13.64 | 8.6% | 39.4% |
| 0c4 4e | 10 | even | 33.3% | 11 (L+1) | 13.62 | 5.6% | 36.7% |
| 0c4 4e | 10 | odd | 33.3% | 10 (L+0) | 13.67 | 8.1% | 37.0% |
| 2c5 4e | 9 | even | 4.2% | 9 (L+0) | 13.75 | 5.8% | 29.3% |
| 2c5 4e | 9 | odd | 4.2% | 10 (L+1) | 13.96 | 4.4% | 31.2% |
| 2c5 4e | 10 | even | 14.6% | 11 (L+1) | 14.04 | 3.7% | 16.0% |
| 2c5 4e | 10 | odd | 14.6% | 10 (L+0) | 13.96 | 6.1% | 26.6% |
| 2c5 4e | 11 | even | 17.2% | 11 (L+0) | 14.20 | 2.4% | 12.9% |
| 2c5 4e | 11 | odd | 17.2% | 11 (L+0) | 14.41 | 0.8% | 17.1% |
| 2c5 4e | 12 | even | 9.9% | 12 (L+0) | 14.49 | 1.3% | 2.4% |
| 2c5 4e | 12 | odd | 9.9% | 12 (L+0) | 14.64 | 0.2% | 10.6% |
| 2c5 4e | 13 | even | 4.2% | 13 (L+0) | 15.01 | 0.0% | 1.3% |
| 2c5 4e | 13 | odd | 4.2% | 13 (L+0) | 15.30 | 0.0% | 1.8% |
| 4b5 4e | 9 | even | 5.6% | 9 (L+0) | 13.96 | 3.9% | 17.0% |
| 4b5 4e | 9 | odd | 5.6% | 10 (L+1) | 14.16 | 2.0% | 25.6% |
| 4b5 4e | 10 | even | 20.8% | 11 (L+1) | 14.19 | 2.5% | 8.8% |
| 4b5 4e | 10 | odd | 20.8% | 10 (L+0) | 14.22 | 2.6% | 20.9% |
| 4b5 4e | 11 | even | 20.8% | 11 (L+0) | 14.31 | 1.5% | 8.5% |
| 4b5 4e | 11 | odd | 20.8% | 11 (L+0) | 14.52 | 0.4% | 12.7% |
| 4b5 4e | 12 | even | 2.8% | 12 (L+0) | 14.49 | 1.0% | 1.9% |
| 4b5 4e | 12 | odd | 2.8% | 12 (L+0) | 14.50 | 0.7% | 10.8% |

## Appendix C: the 216 NISS@1qt cases

Labels are FakeMMAP's (corner case with cs sign, M-slice edges, S-slice edges, E-parity). The three optimal columns are for half turns only (FakeMMAP's first BFS), DR moves, and any of the 18 face turns. The sequence makes a state of the case in the any-move optimal, so its inverse is an optimal solution. Each row is one case:

| Corners | M-slice edges (F) | S-slice edges (R) | E-parity | Optimal, half turns | Optimal, DR moves | Optimal, any move | Sequence |
|---|---|---|---|---:|---:|---:|---|
| H-H + | F-H | R-H | even | 0 | 0 | 0 | (solved: nothing to do) |
| R-D + | F-H | R-D | odd | 1 | 1 | 1 | `L2` |
| F-D + | F-D | R-H | odd | 1 | 1 | 1 | `B2` |
| R-V + | F-H | R-V | odd | 2 | 2 | 2 | `L2 D2` |
| R-D - | F-D | R-D | even | 2 | 2 | 2 | `L2 B2` |
| F-V + | F-V | R-H | odd | 2 | 2 | 2 | `B2 D2` |
| F-D - | F-D | R-D | even | 2 | 2 | 2 | `B2 L2` |
| R-V + | F-H | R-V | even | 3 | 3 | 3 | `L2 D2 L2` |
| D-D + | F-D | R-V | even | 3 | 3 | 3 | `L2 D2 B2` |
| R-V - | F-V | R-V | even | 3 | 3 | 3 | `L2 B2 D2` |
| H-H - | F-D | R-H | odd | 3 | 3 | 3 | `L2 B2 L2` |
| D-D - | F-V | R-D | even | 3 | 3 | 3 | `B2 D2 L2` |
| F-V + | F-V | R-H | even | 3 | 3 | 3 | `B2 D2 B2` |
| F-V - | F-V | R-V | even | 3 | 3 | 3 | `B2 L2 D2` |
| H-H - | F-H | R-D | odd | 3 | 3 | 3 | `F2 R2 F2` |
| R-D + | F-H | R-D | even | 4 | 4 | 4 | `L2 D2 L2 D2` |
| D-D + | F-D | R-V | odd | 4 | 4 | 4 | `L2 D2 L2 B2` |
| F-V - | F-D | R-V | odd | 4 | 4 | 4 | `L2 D2 B2 L2` |
| R-V - | F-V | R-V | odd | 4 | 4 | 4 | `L2 B2 D2 L2` |
| D-D - | F-V | R-V | odd | 4 | 4 | 4 | `L2 F2 U2 F2` |
| H-H - | F-V | R-H | odd | 4 | 4 | 4 | `L2 B2 L2 D2` |
| F-D - | F-H | R-H | even | 4 | 4 | 4 | `L2 B2 L2 B2` |
| R-V - | F-V | R-D | odd | 4 | 4 | 4 | `F2 U2 R2 F2` |
| F-D + | F-D | R-H | even | 4 | 4 | 4 | `B2 D2 B2 D2` |
| D-D - | F-V | R-D | odd | 4 | 4 | 4 | `F2 U2 F2 L2` |
| D-D + | F-V | R-V | odd | 4 | 4 | 4 | `B2 L2 D2 L2` |
| F-V - | F-V | R-V | odd | 4 | 4 | 4 | `B2 L2 D2 B2` |
| H-H - | F-H | R-V | odd | 4 | 4 | 4 | `F2 R2 F2 D2` |
| R-D - | F-H | R-H | even | 4 | 4 | 4 | `B2 L2 B2 L2` |
| H-H + | F-H | R-H | odd | 5 | 5 | 5 | `R2 U2 L2 U2 R2` |
| R-D - | F-D | R-D | odd | 5 | 5 | 5 | `L2 D2 L2 D2 B2` |
| F-V - | F-D | R-V | even | 5 | 5 | 5 | `R2 D2 L2 B2 R2` |
| F-D - | F-V | R-D | odd | 5 | 5 | 5 | `L2 D2 B2 L2 D2` |
| F-V - | F-H | R-V | even | 5 | 5 | 5 | `L2 D2 F2 R2 F2` |
| D-D - | F-V | R-V | even | 5 | 5 | 5 | `L2 F2 U2 R2 F2` |
| D-D + | F-D | R-D | odd | 5 | 5 | 5 | `L2 F2 U2 F2 D2` |
| F-V + | F-V | R-V | even | 5 | 5 | 5 | `R2 B2 D2 B2 R2` |
| R-D - | F-V | R-D | even | 5 | 5 | 5 | `R2 B2 L2 D2 R2` |
| F-D - | F-V | R-H | even | 5 | 5 | 5 | `L2 B2 L2 D2 B2` |
| F-V - | F-H | R-H | even | 5 | 5 | 5 | `L2 B2 L2 B2 D2` |
| F-D + | F-H | R-D | odd | 5 | 5 | 5 | `R2 B2 R2 B2 R2` |
| R-D - | F-D | R-V | odd | 5 | 5 | 5 | `F2 U2 R2 F2 D2` |
| R-V - | F-V | R-H | even | 5 | 5 | 5 | `B2 D2 L2 B2 L2` |
| F-D - | F-D | R-D | odd | 5 | 5 | 5 | `B2 D2 B2 D2 L2` |
| R-V - | F-V | R-D | even | 5 | 5 | 5 | `B2 D2 F2 R2 F2` |
| D-D - | F-D | R-D | odd | 5 | 5 | 5 | `B2 L2 D2 L2 D2` |
| R-V + | F-V | R-V | even | 5 | 5 | 5 | `F2 R2 U2 R2 F2` |
| D-D + | F-V | R-V | even | 5 | 5 | 5 | `F2 R2 U2 F2 L2` |
| R-D - | F-H | R-V | even | 5 | 5 | 5 | `F2 R2 F2 D2 L2` |
| F-D - | F-D | R-V | even | 5 | 5 | 5 | `F2 R2 F2 D2 B2` |
| R-V - | F-H | R-H | even | 5 | 5 | 5 | `B2 L2 B2 L2 D2` |
| R-D + | F-D | R-H | odd | 5 | 5 | 5 | `F2 R2 B2 R2 F2` |
| H-H - | F-D | R-H | even | 6 | 6 | 6 | `L2 B2 D2 L2 D2 L2` |
| F-D - | F-V | R-D | even | 6 | 6 | 6 | `R2 U2 R2 F2 L2 U2` |
| F-V - | F-H | R-V | odd | 6 | 6 | 6 | `R2 D2 L2 F2 L2 F2` |
| F-D + | F-V | R-H | even | 6 | 6 | 6 | `R2 U2 F2 L2 U2 R2` |
| H-H - | F-V | R-D | even | 6 | 6 | 6 | `L2 D2 F2 R2 U2 F2` |
| F-D - | F-H | R-D | even | 6 | 6 | 5 | `R L' D2 R' L'` |
| D-D + | F-H | R-V | odd | 6 | 6 | 6 | `F2 R' L' F2 R L` |
| D-D + | F-D | R-D | even | 6 | 6 | 6 | `L2 F2 U2 R2 F2 D2` |
| F-V + | F-V | R-V | odd | 6 | 6 | 6 | `F' B R2 F B D2` |
| F-V - | F-D | R-H | even | 6 | 6 | 6 | `L2 B2 D2 B2 D2 L2` |
| R-V + | F-H | R-D | even | 6 | 6 | 6 | `L2 B2 D2 F2 U2 F2` |
| F-D + | F-D | R-D | even | 6 | 6 | 6 | `R2 B2 D2 B2 R2 D2` |
| R-V - | F-D | R-V | even | 6 | 6 | 6 | `R2 B2 L2 D2 R2 D2` |
| R-D + | F-V | R-D | odd | 6 | 6 | 6 | `R2 F2 R2 U2 L2 F2` |
| F-D + | F-V | R-D | odd | 6 | 6 | 6 | `R2 B2 R2 D2 B2 R2` |
| D-D + | F-H | R-D | odd | 6 | 6 | 6 | `R2 F2 R2 F2 D2 R2` |
| F-V - | F-D | R-H | odd | 6 | 6 | 6 | `L2 B2 L2 B2 D2 B2` |
| F-V + | F-H | R-V | odd | 6 | 6 | 6 | `R2 B2 R2 B2 R2 D2` |
| H-H + | F-D | R-D | even | 6 | 6 | 6 | `R2 F2 L2 B2 L2 F2` |
| H-H - | F-D | R-V | even | 6 | 6 | 6 | `F2 U2 R2 F2 D2 L2` |
| R-D + | F-H | R-V | even | 6 | 6 | 6 | `F2 U2 R2 F2 D2 B2` |
| R-D - | F-D | R-H | even | 6 | 6 | 5 | `F' B D2 F B` |
| D-D - | F-V | R-H | odd | 6 | 6 | 6 | `L2 F B L2 F' B'` |
| H-H - | F-H | R-D | even | 6 | 6 | 6 | `F2 U2 B2 U2 R2 F2` |
| R-D - | F-D | R-V | even | 6 | 6 | 6 | `F' B R2 D2 F B` |
| R-V - | F-V | R-H | odd | 6 | 6 | 6 | `B2 D2 B2 L2 B2 L2` |
| F-V + | F-D | R-H | even | 6 | 6 | 6 | `B2 R2 U2 L2 U2 R2` |
| R-V - | F-H | R-D | even | 6 | 6 | 6 | `F2 R2 U2 R2 U2 F2` |
| R-D + | F-D | R-D | even | 6 | 6 | 6 | `F2 R2 U2 R2 F2 D2` |
| R-V + | F-V | R-V | odd | 6 | 6 | 6 | `R' L B2 R L D2` |
| D-D - | F-D | R-D | even | 6 | 6 | 6 | `R' L D2 B2 R' L'` |
| R-D + | F-D | R-V | odd | 6 | 6 | 6 | `F2 R2 F2 D2 L2 B2` |
| F-V - | F-V | R-D | even | 6 | 6 | 6 | `F' B' D2 R2 F B'` |
| F-D + | F-D | R-V | odd | 6 | 6 | 6 | `B2 R2 B2 D2 B2 R2` |
| R-V - | F-H | R-D | odd | 6 | 6 | 6 | `F2 L2 F2 L2 D2 R2` |
| D-D - | F-D | R-H | odd | 6 | 6 | 6 | `B2 L2 B2 L2 D2 B2` |
| R-V + | F-V | R-H | odd | 6 | 6 | 6 | `F2 R2 B2 R2 F2 D2` |
| H-H - | F-V | R-H | even | 7 | 7 | 7 | `L2 B2 U2 R2 D2 R2 U2` |
| F-D - | F-H | R-H | odd | 7 | 7 | 7 | `L2 B2 D2 L2 D2 L2 B2` |
| F-D + | F-V | R-H | odd | 7 | 7 | 6 | `R L' B2 D2 R L'` |
| H-H - | F-V | R-D | odd | 7 | 7 | 6 | `B2 R L D2 R' L` |
| F-D - | F-H | R-D | odd | 7 | 7 | 7 | `R2 D2 L2 F2 L2 F2 D2` |
| D-D + | F-H | R-V | even | 7 | 7 | 6 | `R' L' F2 R' L F2` |
| H-H + | F-V | R-H | odd | 7 | 7 | 7 | `R2 U2 B2 R2 D2 L2 F2` |
| R-D - | F-V | R-H | odd | 7 | 7 | 7 | `L2 D2 B2 L2 D2 B2 L2` |
| F-D + | F-H | R-H | odd | 7 | 7 | 5 | `R L' D2 R' L` |
| H-H - | F-D | R-D | odd | 7 | 7 | 6 | `R L' D2 R' L' B2` |
| D-D - | F-H | R-D | odd | 7 | 7 | 7 | `R' L' F2 R L F2 D2` |
| R-V + | F-D | R-V | even | 7 | 7 | 5 | `R' L' B2 R L` |
| R-V + | F-H | R-D | odd | 7 | 7 | 6 | `F' B D2 R2 F B'` |
| F-D + | F-D | R-D | odd | 7 | 7 | 5 | `F' B R2 F B` |
| F-V - | F-H | R-H | odd | 7 | 7 | 7 | `L2 B2 D2 B2 D2 L2 B2` |
| R-V + | F-H | R-H | odd | 7 | 7 | 6 | `L2 F B' L2 F' B` |
| F-D - | F-D | R-H | odd | 7 | 7 | 7 | `R2 F2 U2 F2 R2 D2 L2` |
| H-H + | F-H | R-D | odd | 7 | 7 | 6 | `L B2 U2 D2 F2 R'` |
| R-V - | F-D | R-V | odd | 7 | 7 | 6 | `R' L' D2 B2 R' L'` |
| D-D - | F-H | R-V | odd | 7 | 7 | 7 | `R2 F2 R2 F2 D2 R2 D2` |
| R-V + | F-D | R-V | odd | 7 | 7 | 5 | `R' L' B2 R L'` |
| H-H + | F-V | R-H | even | 7 | 7 | 6 | `B2 R L' D2 R' L` |
| F-V + | F-D | R-V | odd | 7 | 7 | 7 | `L2 F2 R2 U2 F2 L2 D2` |
| H-H + | F-V | R-D | even | 7 | 7 | 7 | `R2 F2 L2 U2 B2 L2 F2` |
| R-V + | F-D | R-D | even | 7 | 7 | 7 | `R2 F2 R2 F2 D2 R2 B2` |
| F-D - | F-V | R-H | odd | 7 | 7 | 7 | `L2 B2 L2 B2 D2 B2 D2` |
| D-D - | F-H | R-V | even | 7 | 7 | 7 | `R2 F2 R2 F2 R2 D2 R2` |
| F-V + | F-D | R-V | even | 7 | 7 | 7 | `L2 F2 R2 F2 L2 D2 B2` |
| H-H + | F-V | R-V | even | 7 | 7 | 7 | `F2 R2 F2 L2 B2 L2 D2` |
| F-D - | F-H | R-V | odd | 7 | 7 | 7 | `F2 U2 R2 F2 D2 L2 B2` |
| H-H + | F-H | R-V | odd | 7 | 7 | 7 | `F2 U2 L2 B2 U2 F2 R2` |
| R-D + | F-H | R-H | odd | 7 | 7 | 5 | `F' B D2 F B'` |
| D-D + | F-D | R-H | odd | 7 | 7 | 7 | `L2 F B' L2 U2 F' B'` |
| F-V + | F-V | R-D | even | 7 | 7 | 5 | `F' B' R2 F B` |
| H-H - | F-H | R-V | even | 7 | 7 | 7 | `F2 U2 B2 U2 R2 F2 D2` |
| R-D - | F-H | R-H | odd | 7 | 7 | 7 | `B2 L2 D2 B2 D2 B2 L2` |
| H-H - | F-D | R-V | odd | 7 | 7 | 6 | `L2 F B U2 F' B` |
| R-D + | F-H | R-V | odd | 7 | 7 | 6 | `F' B R2 D2 F B'` |
| R-D - | F-D | R-H | odd | 7 | 7 | 7 | `B2 D2 B2 L2 B2 L2 D2` |
| D-D - | F-V | R-H | even | 7 | 7 | 6 | `F B L2 F' B L2` |
| F-V + | F-H | R-H | odd | 7 | 7 | 6 | `B2 R' L B2 R L'` |
| R-V - | F-H | R-H | odd | 7 | 7 | 7 | `B2 L2 D2 L2 D2 B2 L2` |
| H-H + | F-D | R-H | odd | 7 | 7 | 6 | `F L2 U2 D2 R2 B'` |
| R-D - | F-H | R-D | odd | 7 | 7 | 7 | `F2 R2 U2 R2 B2 U2 F2` |
| R-D + | F-D | R-D | odd | 7 | 7 | 5 | `R' L B2 R L` |
| F-V + | F-D | R-H | odd | 7 | 7 | 6 | `R' L D2 B2 R' L` |
| R-V + | F-V | R-D | odd | 7 | 7 | 7 | `F2 R2 F2 D2 L2 B2 D2` |
| H-H + | F-D | R-V | even | 7 | 7 | 7 | `F2 R2 F2 D2 L2 B2 L2` |
| D-D + | F-V | R-H | odd | 7 | 7 | 7 | `F B U2 L2 B F' L2` |
| F-V - | F-V | R-D | odd | 7 | 7 | 6 | `F' B' D2 R2 F B` |
| F-V + | F-V | R-D | odd | 7 | 7 | 5 | `F' B' R2 F B'` |
| H-H + | F-H | R-V | even | 7 | 7 | 6 | `R2 F B' D2 F' B` |
| R-D - | F-H | R-V | odd | 7 | 7 | 7 | `F2 L2 F2 L2 U2 L2 U2` |
| F-V + | F-D | R-D | even | 7 | 7 | 7 | `B2 R2 B2 R2 D2 B2 R2` |
| R-V + | F-V | R-D | even | 7 | 7 | 7 | `B2 R2 F2 R2 F2 D2 R2` |
| D-D + | F-V | R-H | even | 7 | 7 | 7 | `F2 R2 B2 R2 F2 D2 B2` |
| R-D - | F-V | R-D | odd | 8 | 8 | 7 | `R' L' F2 R L U2 F2` |
| F-D + | F-H | R-D | even | 8 | 8 | 8 | `L2 F2 U2 R2 U2 R2 F2 L2` |
| R-D - | F-V | R-H | even | 8 | 8 | 6 | `B2 R L D2 R' L'` |
| F-D + | F-H | R-H | even | 8 | 8 | 6 | `F L2 U2 D2 R2 B` |
| H-H - | F-D | R-D | even | 8 | 8 | 8 | `F2 U2 B2 R2 F2 L2 D2 L2` |
| D-D - | F-H | R-D | even | 8 | 8 | 6 | `F2 R L' F2 R L` |
| R-D + | F-V | R-D | even | 8 | 8 | 6 | `R' L' B2 R L D2` |
| R-V - | F-D | R-H | odd | 8 | 8 | 8 | `B2 D2 B2 R L D2 R' L'` |
| R-D + | F-V | R-H | even | 8 | 8 | 8 | `L2 D2 F2 R2 U2 B2 R2 F2` |
| H-H + | F-D | R-H | even | 8 | 8 | 5 | `R' L B2 R L'` |
| H-H - | F-V | R-V | odd | 8 | 8 | 7 | `F2 R' L' U2 F2 R' L` |
| F-V + | F-H | R-H | even | 8 | 8 | 7 | `F2 R' L F2 D2 R L'` |
| R-V - | F-D | R-D | even | 8 | 8 | 8 | `R' L' F2 R L F2 D2 B2` |
| R-V + | F-H | R-H | even | 8 | 8 | 7 | `L2 F B' L2 U2 F' B` |
| F-D - | F-D | R-H | even | 8 | 8 | 5 | `F' B' D2 F B'` |
| H-H + | F-H | R-D | even | 8 | 8 | 5 | `F' B R2 F B'` |
| D-D + | F-H | R-D | even | 8 | 8 | 8 | `R2 F2 R2 F2 R2 U2 L2 U2` |
| D-D + | F-D | R-H | even | 8 | 8 | 6 | `L2 F B' L2 F' B'` |
| F-V - | F-V | R-H | odd | 8 | 8 | 7 | `F2 R2 F B' R2 F B` |
| H-H - | F-H | R-H | even | 8 | 8 | 8 | `R2 F2 U2 B2 L2 U2 R2 F2` |
| R-D + | F-H | R-H | even | 8 | 8 | 6 | `R B2 U2 D2 F2 L` |
| F-V + | F-H | R-V | even | 8 | 8 | 8 | `L2 F2 R' L F2 D2 R L` |
| D-D - | F-D | R-V | even | 8 | 8 | 8 | `L2 B2 U2 R L U2 R' L` |
| R-D + | F-V | R-H | odd | 8 | 8 | 7 | `F2 R L U2 R' L' F2` |
| R-D + | F-V | R-V | even | 8 | 8 | 8 | `R2 F2 R2 F2 D2 R2 B2 D2` |
| R-V + | F-D | R-H | odd | 8 | 8 | 8 | `L2 F2 R2 B2 U2 R2 F2 L2` |
| F-D + | F-V | R-D | even | 8 | 8 | 8 | `L2 F2 R2 F2 L2 D2 B2 D2` |
| D-D - | F-D | R-V | odd | 8 | 8 | 7 | `R L D2 R' L D2 B2` |
| R-D + | F-V | R-V | odd | 8 | 8 | 8 | `R2 F2 R2 F2 R2 B2 D2 R2` |
| F-D + | F-V | R-V | odd | 8 | 8 | 8 | `L2 F2 R2 F2 L2 B2 D2 B2` |
| F-V - | F-H | R-D | odd | 8 | 8 | 8 | `F2 U2 R2 F2 D2 L2 B2 D2` |
| F-D + | F-H | R-V | even | 8 | 8 | 8 | `B2 D2 R2 B2 D2 R2 B2 R2` |
| F-D + | F-D | R-V | even | 8 | 8 | 6 | `F' B' R2 F B D2` |
| F-V - | F-D | R-D | even | 8 | 8 | 8 | `R2 F' B R2 D2 F B R2` |
| F-D - | F-D | R-V | odd | 8 | 8 | 7 | `F' B' D2 R2 B F D2` |
| R-D + | F-D | R-H | even | 8 | 8 | 8 | `F2 R2 U2 B2 U2 B2 R2 F2` |
| F-D - | F-H | R-V | even | 8 | 8 | 6 | `L2 F B U2 F' B'` |
| D-D - | F-D | R-H | even | 8 | 8 | 8 | `F2 R2 B2 R2 F2 D2 B2 D2` |
| R-V - | F-H | R-V | odd | 8 | 8 | 7 | `L2 F2 R L' F2 R L` |
| R-D - | F-H | R-D | even | 8 | 8 | 5 | `R L D2 R' L` |
| R-V + | F-V | R-H | even | 8 | 8 | 8 | `F2 R2 F B' R2 D2 F B` |
| D-D + | F-V | R-D | even | 8 | 8 | 8 | `F2 R2 F2 D2 L2 B2 D2 B2` |
| F-D + | F-H | R-V | odd | 8 | 8 | 7 | `R2 F B D2 F' B' R2` |
| R-D + | F-D | R-V | even | 8 | 8 | 8 | `B2 R2 F2 R2 F2 D2 R2 D2` |
| F-D + | F-V | R-V | even | 8 | 8 | 8 | `B2 L2 F2 R2 U2 F2 L2 D2` |
| F-V + | F-H | R-D | odd | 8 | 8 | 8 | `B2 R2 F2 L2 U2 B2 L2 F2` |
| D-D + | F-V | R-D | odd | 8 | 8 | 7 | `F' B' D2 F B' D2 L2` |
| H-H + | F-D | R-D | odd | 9 | 9 | 8 | `R D2 F2 B2 R' L F2 R'` |
| R-V - | F-D | R-H | even | 9 | 9 | 7 | `B2 D2 R L D2 R' L'` |
| H-H - | F-V | R-V | even | 9 | 9 | 9 | `F2 U2 B2 R2 F2 L2 D2 L2 D2` |
| R-V - | F-D | R-D | odd | 9 | 9 | 7 | `F2 R L' F2 R L B2` |
| D-D - | F-H | R-H | even | 9 | 9 | 9 | `R2 D2 F2 R2 D2 F2 R2 D2 F2` |
| R-V + | F-D | R-H | even | 9 | 9 | 9 | `L2 D2 F2 R2 D2 F2 L2 B2 U2` |
| H-H + | F-V | R-D | odd | 9 | 9 | 8 | `L' F2 R L' F2 B2 D2 L` |
| R-D - | F-V | R-V | even | 9 | 8 | 7 | `F2 R' L' U2 F2 R' L'` |
| F-D - | F-V | R-V | even | 9 | 8 | 7 | `L2 F B U2 L2 F' B'` |
| F-V - | F-V | R-H | even | 9 | 9 | 6 | `F' B' D2 F B' D2` |
| H-H - | F-H | R-H | odd | 9 | 9 | 5 | `F' B' D2 F B` |
| R-V + | F-D | R-D | odd | 9 | 9 | 9 | `L2 F2 R2 U2 B2 U2 F2 L2 B2` |
| F-V - | F-D | R-D | odd | 9 | 9 | 7 | `L2 F' B R2 F B L2` |
| H-H + | F-V | R-V | odd | 9 | 9 | 9 | `L2 F2 R2 F2 D2 L2 B2 D2 L2` |
| R-D - | F-V | R-V | odd | 9 | 9 | 8 | `F2 R L' F2 L R B2 D2` |
| D-D + | F-H | R-H | even | 9 | 9 | 9 | `F2 D2 R2 F2 D2 R2 F2 D2 R2` |
| R-V - | F-H | R-V | even | 9 | 9 | 6 | `R L D2 R' L D2` |
| F-V + | F-D | R-D | odd | 9 | 9 | 9 | `B2 L2 F2 R2 F2 L2 D2 B2 D2` |
| F-V + | F-H | R-D | even | 9 | 9 | 9 | `B2 D2 L2 F2 D2 L2 B2 R2 U2` |
| H-H + | F-D | R-V | odd | 9 | 9 | 8 | `F L2 F B' R2 L2 D2 F'` |
| F-V - | F-H | R-D | even | 9 | 9 | 7 | `L2 D2 F B U2 F' B'` |
| F-D - | F-V | R-V | odd | 9 | 9 | 8 | `L2 U2 F B U2 F B' U2` |
| D-D - | F-H | R-H | odd | 10 | 10 | 8 | `B2 D2 R L D2 R' L' B2` |
| D-D + | F-H | R-H | odd | 10 | 10 | 8 | `L2 D2 F' B' D2 F B L2` |

## Docs and sheets referred to

- Levi Gibson, "DR Bounding": https://docs.google.com/document/d/1q7rig4GEo26GunBMtuagZdGyzyjCGlduH84CHLpGLSA
- Rodney Kinney, "Advanced DR Bounding [Beta]": https://docs.google.com/document/d/13F8HonrKJyHjU9EwfiHDRyY4X77vPriYeaVSrh5guq0
- Rodney Kinney, sheet "Adv DR Bounding" (rules vs the 216 computed cases): https://docs.google.com/spreadsheets/d/1jRvikzLlm3yHlDQmQ0DLyj3Aw6uinL3Oa-U9_U7R5mY
- FakeMMAP, sheet "OBL++": https://docs.google.com/spreadsheets/d/1kax7evfA85p_4ArXKO7si3FrCpj7PEeFwoz4GY5wRAE
- wen, sheet "HTR better smh (v2)" (the corner subsets): https://docs.google.com/spreadsheets/d/1ZhulzHeNgv2Hiy4x9R1MzsMRlPlI-E8DRiHFJlPlboM
- FakeMMAP's BFS listing, script and tables are attachments on FakeMMAP's posts of 6–10 Sep 2026 in #fmc-theory.
- Mallard (cubelib) source, for how the 48 subsets are built: https://github.com/Jobarion/cubelib
