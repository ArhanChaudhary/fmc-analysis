# Judging a DR by hand: what the full BFS says

*What you can read off a DR, how much it tells you about the finish, and which bounds hold. Every number is an exact count over all DR states.*

November 2026. A name with a date is a link to that message on the FMC solvers Discord (#fmc-theory or #fmc-discussion). Docs and sheets are listed with links at the end.

---

## Introduction

The question I started from: can Levi's and Rodney's DR bounding be pushed to 3qt, 4qt and 5qt DRs, so you can toss a DR because its bound is high instead of wasting time on it?

With a computer, yes. Look at part of the DR, tabulate the fewest moves that solve that part, and you have a lower bound at any qt with no skeleton. With the right table it proves "no finish in 12" for 59% of 5qt DRs and "no finish in 11" for 94%. That was the first version of this doc and it is now section 7. The trouble is the tables have millions of cases, so nobody can use them in an attempt, and the bar on the server is clear:

> "is the lower bound fast to determine by human methods? If it takes too long to figure out the lower bound, you can just as well try to actually solve the DR" ([[T9871]])

> "I don't expect anyone to use the decision trees directly. I'm just hoping to use them to find the most important 2-3 features … then make some simple rules out of just those features" ([[T8337]])

So this version asks the human question. Take what you can actually read off a DR (subset, pairs, corner case, HTR length on both sides, corner solution length, E-slice parity) and measure exactly what each one tells you about the finish. I BFSed the whole DR group, 19,508,428,800 states, so nothing below is sampled.

**Which finish.** A 9- or 10-move DR gets checked whatever it looks like. The DRs worth pruning are the 11- and 12-movers, and what they need is a finish in 10 or 11 (one more if the first finish move merges with the last DR move). So every table gives the share finishing in 10, 11, 12 and 13 or less, and the pruning is measured at each target from 9 to 13.

What came out:

- **For a 10 or an 11, the subset does most of the pruning.** In 11: 10% of 1–2qt DRs, 4.6% of 3qt, 1.1% of 4qt, 0.24% of 5qt. In 10: 2.4%, 0.87%, 0.16%, 0.02%.
- **The lower the target, the more the reads tell you.** Keep only the best-looking quarter of 4qt DRs, going by pairs and corner case, which need no solving. It holds 65% of the finishes in 12, 77% of those in 11 and 89% of those in 10. At 3qt: 52%, 63%, 74%. HTR length on both sides adds a few points on top, and at 1–2qt it is the best single read.
- **Still no clean yes/no.** The subset explains 35% of the variance of the optimal, everything readable together 48%, and what's left has an sd of 0.78 moves. Zagros's hunch that corner case + HTR on both sides pins the optimal to ~0.25 moves: it's 0.80.
- **Plain rules, with their price.** Zagros's "9+ on both sides, toss", moved to your target T: drop every DR that is T−1 or more to HTR on both sides. For an 11 that's 10+ on both sides, and it drops 8% of 3qt and 31% of 4qt DRs for 0.2% and 2.5% of the 11s. T−2 or more (9+ for an 11) drops 28% and 67% and costs 5% and 20% of them. With no solving: dropping every DR without a pair drops 14% and costs 2–7% of the 11s. And a five-line prune list that needs no solving (section 8) throws away {= PRUNE('drop') =} of all DR states and keeps {= PRUNE('keep',11) =} of the finishes in 11.
- **The two guaranteed hand bounds wake up at low targets.** The longer HTR and the corner solution with the right E-parity prove almost nothing for a 12 (5% of 4qt DRs, 13% of 5qt). For a 10 they rule out half of 4qt and 80% of 5qt DRs.
- **A few real kill rules.** 2c5 with the bad corners stacked on both sides: no 12 at all. 2c5 stacked on one side and opposite on the other: no 11, 0.24% in 12. 2c4 stacked on both sides: no 10, 0.06% in 11, 1.1% in 12. 4a2 2e with all four bad corners on one layer on both sides: no 12 at all.
- **Questions from the server, answered exactly**: stats by bad corner position (Daichi, JTuu, wen), by pairs (Rodney, Levi), the normal × inverse HTR table (Zagros), the 4a1 4e bound against the real leave slice (count quackula), the cost of the slice (JTuu), an invertible last move (Zagros), God's number per subset (compLex), optimal lengths of all corner cases (Evan).
- **Bounds measured.** Levi's 1qt formula, trangium's 2q bound taken to any qt, HTR length, corner length with parity. Which hold for every finish, how often a finish with extra quarter turns gets under the others, and how far below optimal they all sit.
- **Where the information is.** A computer that sees the corners exactly plus the edge colours proves "no 12" for 81% of 4qt and 95% of 5qt DRs, and "no 11" for 97% and 99%. Everything readable put together gets 24% and 45% of them under 1% for a 12. The gap is the corner–edge relation, which is what Rodney's NISS@1qt tracing looks at. No count of visible features replaces it.
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
- "In 11" always means an optimal finish of 11 moves or fewer. A cell that says 0 means no state at all; "<0.01%" means a few.

How it was checked, and what's proven, is in sections 10 and 11.

---

## 3. How much can a read tell you?

**Which finish you need.** Your result is the DR length plus the finish (one less if the first finish move merges with the last DR move). A 9- or 10-move DR gets a look whatever it is, and a 12 from it is a good result. The DRs you want to prune are the 11- and 12-movers, and those need a 10 or an 11. So this section measures everything for each target from 9 to 13.

How rare each target is, as a share of all DR states of the kind:

{{PIV_BASE}}

For a 10 or an 11 the subset has already done most of the pruning: one 4qt DR in 90 finishes in 11, one 5qt DR in 400. The reads matter most where the odds are still alive, at 1–3qt, and for finding the few high-qt DRs worth keeping. (The tables below go by corner-qt group from 1–2qt up. 0c0, half a percent of DR states, has its own row in section 8.)

**Two kinds of read.** Some need no solving: the subset, the true pairs, the corner case on normal and on inverse. Some need you to solve something: the shortest HTR on both sides, the optimal corner solution and its parity. The tables keep the two apart, because a read you have to work for costs time, and because the HTR numbers assume you found the *shortest* HTR. If yours is longer than the shortest, the DR looks worse than it is, and an HTR rule drops more than it should.

### Ranking

Rank the DRs of a qt group by what the read says, keep only the best-looking quarter, and count how many of the finishes in T you kept. With no information that's 25%. Each number is the best any rule based on that read could do.

{{PIV_RANK}}

- **The lower the target, the more a read tells you.** At 4qt, pairs and corner cases put 65% of the 12s in the best-looking quarter, 77% of the 11s and 89% of the 10s. At 3qt: 52%, 63%, 74%. For a 13 nothing does much.
- **Most of it needs no solving.** From 3qt up, pairs plus the corner case on both sides rank better than the two HTR lengths do, at every target from 10 up. Adding the HTR lengths on top is worth 1 to 7 points.
- **At 1–2qt it's the other way round.** HTR length is the best single read there (72% of the 10s against 64% for pairs and corner cases), and at 1–2qt you find the HTR quickly anyway.

### Throwing away

The other direction: how many DRs can you drop and still keep 95% of the finishes in T?

{{PIV_DROP}}

For an 11 that's a third of the 1–2qt DRs, two in five at 3qt and more than half at 4–5qt. For a 12 it's a fifth to two in five.

Another way to cut it. Say a class of DRs is "under 1%" if at most one in a hundred of it finishes in T. Share of DRs in such classes, and in brackets the share of all the finishes in T those classes hold, which is what you lose by dropping them:

{{PIV_DEAD}}

Read the row "4qt, 11 or less" like this. By subset alone 35% of 4qt DRs are under 1% (that's 4c4 and 0c4). With pairs and corner cases it's 69%, and those 69% hold 17% of the 11s. For a 10, all of 4qt is under 1% as a group, and the reads work the other way: with pairs, corner cases and HTR they pick out the 4% of 4qt DRs that hold half of the 10s. For a 13 no read puts more than 4% of any qt group under 1%.

So tseitsei89's "100% cases and 0% cases" don't exist at any target. There is no feature count that sorts DRs into good and bad. What exists is a set of reads that each multiply your hit rate by two or three, more the lower your target, and a handful of corners of the tables that really are dead.

### Plain rules

The tables above are ceilings: a rule that reaches them needs a table of thousands of classes. These are rules you can carry in your head.

**HTR length against your target** (needs the shortest HTR on both sides). This is Zagros's "4c3 that is 9+ on both sides I throw away" ([[T11190]]) moved to the finish you need, T. Each cell: share of the qt group the rule drops, and in brackets the share of the finishes in T it loses.

{{PIV_RULES}}

- **The first column is a proof**: no finish is shorter than the longer HTR. For a 12 it is next to nothing (0.15% of 4qt DRs). For a 10 it rules out a quarter of 4qt and 44% of 5qt.
- **"Both sides T−1 or more" is the safe rule.** For an 11 that's 10+ on both sides: it drops 31% of 4qt DRs and loses 2.5% of the 11s, and at 3qt it drops 8% and loses 0.2%.
- **"Both sides T−2 or more" is the aggressive one**, and for an 11 it is exactly 9+ on both sides: it drops 28% of 3qt and 67% of 4qt DRs and loses 5% and 20% of the 11s.
- A DR that is exactly T to HTR on the longer side can still finish in T. `U' L2 D' B2 U' B2 U L2 D` (4c3 4e) is 9 to HTR on both sides and finishes in 9, and Appendix G has such a state for every subset.

**Pairs against your target** (no solving). Share of the qt group dropped, and in brackets the share of the finishes in T lost:

{{PIV_PAIR_RULES}}

Pairs are spread the same way in every qt group, so each rule drops the same share everywhere. What changes is the price: dropping the DRs with no pairs costs 2–7% of the 11s, dropping one pair or none costs 9–23%.

The corner-case rules are per subset. They are in section 8 and section 4.3.

**What is proven at each target.** Two bounds hold for every finish and can be worked out by hand: the longer HTR, and the best corner solution with the right E-parity (section 4.5). Share of DRs for which they prove there is no finish in T, next to two of the computer tables of section 7:

{{PIV_BOUNDS}}

For a 12 the hand bounds prove next to nothing below 5qt. For a 10 they rule out half of the 4qt DRs and 80% of the 5qt ones, and for an 11 a fifth and 38%. So the lower your target, the more a guaranteed bound is worth working out, on the high-qt DRs where it bites.

The setup + HTR bound of section 5 (trangium's 2q bound taken to any qt) is not a proof, because a finish with extra quarter turns can get under it. From 3qt up that almost never happens: it is wrong about 0.2% of the finishes in T at most. It is the hand bound that does something at 3qt, where it rules out 19% of the DRs for a 10 and 6% for an 11, more than the two proven bounds together. At 1–2qt it rules out a third of the DRs for a 10 and a sixth for an 11, and is wrong about 5–7% of those finishes.

Appendix H has every read at every target with more cut-offs (best 10%, 25%, 50%; keeping 90%, 95%, 99%).

### Scatter

The same thing without a target: how much scatter is left in the optimal once you know the read (sd, in moves).

| What you know | Needs solving | sd left |
|---|---|---:|
| nothing | | 1.09 |
| subset | no | 0.88 |
| + true pairs | no | 0.85 |
| + corner case on both sides | no | 0.83 |
| + pairs and corner cases | no | 0.80 |
| + HTR length on both sides | yes | 0.82 |
| + corner length L and E-parity | yes | 0.83 |
| + pairs, corner cases and HTR | yes | 0.78 |
| + pairs, HTR, L and E-parity | yes | 0.78 |
| *the optimal leave slice (for scale, you can't read this)* | | 0.43 |

**Zagros's two hunches.**

- *Corner case + HTR on both sides gives the optimal to ~0.25 moves* ([[T11482]]). The sd left is 0.80 over all DRs. Adding pairs makes it 0.78.
- *L + longest HTR predicts within ~1 move* ([[T6905]]). True, 93.3% of DRs are within one move of the typical value for their (subset, L, longer HTR). But 91.3% are within one move of the typical value for their subset alone. The finish just doesn't vary much inside a subset.

A pair that shows what the first hunch is up against. Both are 2c4 4e, with the same corner case on normal and on inverse, 7 to HTR on both sides, and the same corner length (7):

    D F2 U' F2 D B2 D'                                 // optimal 7
    D' R2 B2 U' F2 D B2 U B2 F2 U' F2 U' L2 D' U'      // optimal 16

---

## 4. The reads, cheapest first

### 4.1 Subset

The baseline, and still the biggest single piece of information. Appendix A has all 48 with average, share finishing in 9 to 13, and the fastest and longest optimal in each (God's number per subset, which compLex asked about). The longest: 18 for 0c0 8e, 0c3 4e, 2c5 0e and 2c5 4e, 17 or 16 for most others, 13 for 0c0 0e. One of each 18:

    F2 L2 U B2 F2 R2 B2 F2 R2 U F2 R2 D U F2 R2 D' U'      // 0c0 8e
    F2 D' F2 D' F2 R2 U2 R2 U' B2 R2 B2 L2 U B2 U2 R2 U'   // 0c3 4e
    U2 L2 D B2 U' B2 U' L2 D B2 R2 U R2 U R2 U2 R2 U'      // 2c5 0e
    R2 F2 L2 D' F2 D' B2 F2 R2 U2 F2 D' B2 U2 L2 U' R2 U'  // 2c5 4e

Appendix G has a longest one for every subset.

The shortest possible HTR by corner qt:

| Corner qt | Shortest HTR | A state with exactly that on both sides |
|---:|---:|---|
| 1 | 1 | `D` |
| 2 | 3 | `D B2 D'` |
| 3 | 5 | `D' B2 D' B2 D'` |
| 4 | 7 | `D B2 D' B2 D B2 D'` |
| 5 | 9 | `U' L2 U R2 U' L2 U R2 D` |

Joba took 1 / 2 / 4 / 6 / 8 as a safe lower bound ([[T6639]]); the exact floor is one higher from 2qt up, on either side.

### 4.2 Pairs

Count the true pairs: a corner and an edge next to each other in the U or D layer with both touching stickers matching (16 places to look). This is the read that costs nothing, and it works at every qt.

Share of each corner subset finishing in 10, 11 and 12 or less, by number of true pairs:

{{MAIN_PAIRS}}

Each pair is worth about 0.15 moves of average optimal. It multiplies your odds of a 12 by about 1.4, of an 11 by 1.4 to 1.7 (2 at 5qt), and of a 10 by 1.5 to 2. So pairs matter more the lower your target. Levi is right about blocky 2c4s: for an 11, from {= pct(q(cs='2c4',pairs=0),11) =} with no pairs to {= pct(q(cs='2c4',pairs=5),11) =} with five or more. It's not special to 2c4 though, the ratio is about the same in every subset. Appendix D has all 48 subsets, for 10, 11, 12 and 13.

On Rodney's finer split: I also counted pseudo-pairs (both stickers opposite), side semi-pairs and top semi-pairs, defined as in his message. Knowing all four counts instead of just the true pairs moves the sd left from 0.850 to 0.842. Pairs with E-slice edges add even less. So count true pairs and stop.

You don't need to count again on the inverse scramble: a block stays a block, so the number of true pairs is the same on both sides for every DR state.

### 4.3 Corner case, on both sides

{{CORNER_SECTION}}

A warning: the bad corner *positions* don't always tell you the case. 2c4 has three different "both on one layer, adjacent" cases, at {= pct(q(cs='2c4',cc=S('8')),12) =}, {= pct(q(cs='2c4',cc=S('7')),12) =} and {= pct(q(cs='2c4',cc=S('2')),12) =} in 12. What separates them is the corner permutation, which you get the way you already get the subset (tracing, or whatever corner-case system you use). The column "a qt takes it straight to" is the quick tell: if some U or D quarter turn drops the corner qt count right away, you're in one of the good ones.

### 4.4 HTR length on both sides

Zagros asked for the square table ([[T11190]]); trangium posted one from samples of 20–100 per cell. Exact, for the four big high-qt subsets. Each cell: share finishing in 10 / 11 / 12.

{{MAIN_SQUARES}}

One more move to HTR on both sides costs about half a move of average optimal. It cuts the odds of a 12 by three to six, of an 11 by five or more, and of a 10 by ten or more. Appendix F has every subset with share, average, fastest finish, and odds for 10 to 13. Section 3 has the same read as a plain rule against your target.

**By the longer side alone**, for a whole corner-qt group. This is the table to use when you have one HTR length per side and no time for more (rows under 0.1% of the group are left out):

{{PIV_HTR}}

**Zagros's rule, "4c3 that is 9+ on both sides I throw away".**

{{MAIN_ZAGROS}}

So the rule halves your 4c3s, and what it costs depends on what you need. For an 11-move DR, which needs a 10 or an 11, it is a good rule. For a 12 it throws away a quarter of the finishes. It does throw away real finds:

    U' L2 D' B2 U' B2 U L2 D     // 4c3 4e, 9 to HTR on both sides
    D' L2 U' B2 U B2 D L2 U      // its optimal finish: 9

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

This one is a true lower bound, proven in Lean: no finish is shorter than the best corner solution of the right parity. For a 12 it proves "no" for 13% of 5qt DRs and 5% of 4qt. For an 11: 37% and 21%. For a 10: 73% and 48% (the table of what is proven in section 3). It needs the *optimal* corner solutions of both parities, so it's a read for when you've written the skeletons down anyway.

Two DRs where it bites:

    U B2 U' F2 U B2 D2 L2 U' R2 U R2 U' L2 U2      // 2c4 4e, odd E-slice
    // best corner solution: 12, with an even number of side turns. Best with an odd number: 13.
    // So no 12. (Its optimal is 15.)

    U D L2 D' B2 U R2 F2 B2 D2 L2 D' R2 L2 D2 B2   // 2c3 6e, odd E-slice (Rodney's first random scramble)
    U' R2 U' R2 U                                   // corners in 5, but two side turns
    U R2 U2 R2 U R2 U                               // best with an odd number: 7

As an odds read, L does about what HTR length does (Appendix H). Appendix B splits the big high-qt subsets by L and parity. For 2c4 4e, in 10 / 11 / 12: with L = 8, {= T(q2(cs='2c4',e=4,L=8)) =}. With L = 11, {= T(q2(cs='2c4',e=4,L=11)) =}. With L = 12, {= T(q2(cs='2c4',e=4,L=12,parity=0)) =} if the E-slice is even and {= T(q2(cs='2c4',e=4,L=12,parity=1)) =} if it's odd.

The E-slice parity on its own, without L, is a small read but it's free. It mostly decides whether the finish wants to be even or odd in length. At 4qt, {= pct(q2(group='4qt',parity=1),12) =} finish in 12 with an odd E-slice against {= pct(q2(group='4qt',parity=0),12) =} with an even one, and in 11 it's the even one that is ahead, {= pct(q2(group='4qt',parity=0),11) =} against {= pct(q2(group='4qt',parity=1),11) =}. At 5qt, {= pct(q2(group='5qt',parity=1),13) =} finish in 13 with an odd E-slice against {= pct(q2(group='5qt',parity=0),13) =} with an even one.

### 4.6 The last DR move

Zagros asked what one invertible move is worth. If your DR ends in R, then R' is also a DR and its state is yours plus an R2, so you get the better of two finishes. Average optimal over all DRs: 13.58 for a pure DR, 13.26 when the last move can go either way.

{{PIV_LASTMOVE}}

A third of the time the other DR is one shorter, a third the same, a third one longer, in every subset. So it's worth 0.33 moves flat, and it raises the odds of an 11 or a 12 by half or more. (If you could pick any of the four side half turns it would be 0.73.) An example:

    D' L2 D R2 B2 F2 U2 B2 R2 U L2 U'       // optimal 12
    D' L2 D R2 B2 F2 U2 B2 R2 U L2 U' L2    // the same DR with its last move (an L) turned the other way: optimal 11

---

## 5. Bounds people use, graded

A bound is only a bound if it never exceeds the optimal. Graded on all states:

| Bound | Ever too high? | Its average | Average optimal there |
|---|---|---:|---:|
| longer HTR, normal or inverse (all DRs) | never (proven) | 9.22 | 13.58 |
| best corner solution with the right E-parity (all DRs) | never (proven) | 9.44 | 13.58 |
| Levi's 1qt formula, HTR normal + HTR inverse − 1 (4a1 4e) | never for a finish with one quarter turn. A finish with three is shorter for 11.7% of 4a1 4e | 10.85 | 12.27 |
| setup + HTR, any qt (below) | never for a finish with the minimum number of quarter turns. A finish with more is shorter for 2.6% at 1–2qt and 0.002% above | see below | |

**Levi's formula.** (HTR normal) + (HTR inverse) − 1 bounds the finishes with one quarter turn, which is what Levi's doc uses it for. (His doc writes it as the path to the trigger on normal + on inverse + 1. An HTR is that path plus the quarter turn, so it's the same number.)

A 1qt state can also be solved with three quarter turns, and the number worth having is how often that is shorter. Over all 286,654,464 states of 4a1 4e:

| The optimal is… | Share of 4a1 4e |
|---|---:|
| below the formula, so a 3qt finish is shorter (by 1: 8.4%, by 2: 2.7%, by 3 or more: 0.6%) | 11.7% |
| equal to the formula | 18.0% |
| above the formula | 70.3% |

If the formula says 12 or less, a 3qt finish beats it 2.5% of the time, and 0.6% of the time if it says 11 or less. Example:

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

Average +0.70. The leave slice is below the formula 19.7% of the time, more often than the full finish is, because leaving the slice is easier. (The example above is one: formula 10, leave slice 7.)

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

The longer the finish, the more room to fit the slice for free. (+1 happens because the optimal finish doesn't have to be an optimal leave slice with a slice inserted.) Examples:

    D' U2 F2 U2               // leave slice 3, optimal finish 4: the slice costs +1
    U R2 D U'                 // leave slice 2, optimal finish 4: +2
    B2 F2 D' U L2 R2 D U'     // only the E-slice is unsolved and it takes 8: the most the slice can cost

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

Short finishes are narrow: when a DR has a 12, two times out of three there is exactly one first move that gets it. Long finishes are wide. Higher qt DRs have more optimal first moves (3.1 on average at 5qt against 2.6 at 2qt) only because their optimals are longer. One of each:

    D' L2 D R2 B2 F2 U2 B2 R2 U L2 U'                  // optimal 12: only U or L2 starts an optimal finish
    D2 B2 U' R2 D R2 B2 R2 F2 U2 R2 D F2 U R2 U'       // optimal 16: nine of the ten moves do

---

## 7. What a computer can prove from the DR

This is the first version of the doc, kept because it shows where the information is and what any hand rule is up against.

### You can't finish faster than the part you're looking at

Pick something to look at on a DR. Say, only the corners. Ask how many moves it takes to solve *just that*. The real finish solves everything, so it solves the corners too, so it can't be shorter. That's the corner-length bound, and it's the logic of every bound here. Look at more and the bound goes up. A solution read backwards solves the inverse scramble, so the same number computed on the inverse is also a lower bound, and you take the bigger one.

If you look at exactly what Rodney traces at 1qt (the corners, which slice each U/D-layer edge belongs to, its U/D colour, the E-parity) but on the DR state itself, you get one number that no skeleton and no variant can beat, at any qt. I call that NISS@DR. On HTR states with half turns only it *is* FakeMMAP's 216-case table. The catch is that at the DR it has 6,350,400 cases instead of 216.

