None of this is something you can do at the table, and that's the point of keeping it. The table sets it next to what a hand can do (section 3), for the finish you need. Each row is a qt group and a target; each number is a share of its DRs:

{{PIV_COMPARE}}

"Under 1%" is not a proof: it means the reads put the DR in a class where at most one in a hundred gets there. The next two columns are proofs.

The difference is not a feature anyone forgot to count. It's the exact relation between the corner state and where each edge sits, the thing you get from picking a skeleton and tracing. So a real hand bound at 4–5qt would have to be a faster way of doing what Rodney's method does per skeleton, across all skeletons at once.

Whether NISS@DR has a description compact enough for that, I don't know. The tables to test a guess against exist now.

---

{{GUIDE}}

---

## 9. The 216 NISS@1qt cases, three ways

{{C216}}

---

## 10. The proof, if you don't speak Lean

{{PROOF}}

---

## 11. How it was computed and checked

{{HOW}}

For the hand reads in sections 3 to 6:

- **Leave slice**: a second BFS over corners and U/D-layer edges only, reduced by the same 16 symmetries (111,605,760 reduced states, five seconds). It reaches all 19,508,428,800 states when each is counted with its 12 E-slice arrangements.
- **The reads**: four more passes over all DR states. Each computes the read for the state (and for its inverse where that's a different thing) and adds the state's optimal to a histogram. The fourth keeps every read together, normal and inverse apart, for the sd figures and "everything readable". Every pass counts exactly 19,508,428,800 states.
- **Pairs**: the four kinds are defined by the colours of the two touching sticker pairs, as in Rodney's message. Checked on Rodney's example: after `B2 L2 B2 R2` the UF edge has a top semi-pair on one side and a side semi-pair on the other, which is what Rodney says it sets up.
- **Corner cases**: classes of the 420 HTR corner cosets under the 16 symmetries and under turning both layers. There are 46.
- **Setup lengths** for the setup + HTR bound: breadth-first over the 29,400 HTR cosets with half turns only, until some quarter turn lowers the minimum qt count. At 1qt it has to give the shortest 1qt HTR minus one, and it does.
- **The 500 scrambles** (the guide's real-scramble numbers and the tally on the examples page): uniformly random states drawn with the EO → DR study's generator, written with R' U' F at both ends. Not nissy's scrambler, which isn't uniform ([EO → DR study, appendix B](https://fmc.arhan.sh/eo-to-dr/#appendix-b-how-it-was-computed-and-what-checks-it)).
- **Example scrambles**: every scramble quoted as an example of something was found by a search over all DR states, then re-read from its text alone (subset, HTR lengths, leave slice and optimal recomputed from the moves). The ones that stand against something a person wrote were also solved with nissy.
- **What the server has said**: I went through all of #fmc-theory and #fmc-discussion (about 33,000 messages, August 2022 to November 2026) line by line for what people read off a DR, how they discard, and what they asked for. Every quote above is checked against the export.

---

## 12. What this doesn't do

- **DR moves only.** "Optimal" here is U, D, R2, L2, F2, B2. A finish that breaks DR is shorter for {= '%.1f' % (GAPS()['g2']['uniform']['shorter'] * 100) =}% of DR states (± {= '%.1f' % (GAPS()['g2']['uniform']['se'] * 100) =} points), by one move in {= '%.0f' % GAPS()['by1'] =}% of those, {= '%.3f' % GAPS()['g2']['uniform']['mean_gain'] =} moves on average. That's {= '{:,}'.format(GAPS()['g2n']) =} uniform states, 1,000 per subset × edges, solved with all 18 face turns by nissy's `solve optimal`. On other sets of DRs, each row is a set and the share of it where a DR-breaking finish is shorter:

  | Which DRs | DR-breaking finish shorter, share |
  |---|---:|
  | real DRs, each DR counted once | {= '%.1f' % (GAPS()['g2']['dr11']['shorter'] * 100) =}% |
  | real DRs, each scramble counted once | {= '%.1f' % (GAPS()['g2']['scr11']['shorter'] * 100) =}% |
  | DR-move optimum 12 or less | {= '%.1f' % GAPS()['le12'] =}% |
  | DR-move optimum 15 | {= '%.1f' % GAPS()['at'][15] =}% |
  | DR-move optimum 16 | {= '%.0f' % GAPS()['at'][16] =}% |

  So it only climbs on long finishes. Most of it sits in three cells: {= ', '.join('%s %.0f%%' % (c, x) for c, x in GAPS()['worst']) =}. An example ({= GAPS()['ex']['subset'] =}, DR moves only, DR-move optimum {= GAPS()['ex']['dr_optimum'] =}):

  ```
  {= GAPS()['ex']['scramble_reaching_state'] =}   // the DR state
  {= GAPS()['ex_sol'] =}   // solves it in {= GAPS()['ex']['true_optimum'] =}
  ```

  At the HTR level that's 66 of the 216 cases. Computed with nissy, not in Lean: **computer only**, the answer key. Every solution quoted was replayed on a sticker model.
- **Uniform states.** Every DR state counts once. Against the DRs you actually reach, that's close to right. The test: {= '{:,}'.format(GAPS()['scr']) =} uniformly random scrambles, every EO-first DR of at most 11 moves cubelib-cli lists for each, as on the examples page ({= '{:,}'.format(GAPS()['dr11']) =} DRs), counted once per DR and once per scramble, standard errors clustered by scramble. Every corner subset comes out close to uniform. Each row is a measure, with the most any corner subset is off:

  | Per corner subset | Off from uniform by at most |
  |---|---|
  | share of DRs | {= '%.1f' % GAPS()['share'] =} points |
  | average optimal | {= '%.2f' % GAPS()['mean'] =} moves |
  | share finishing in 11, all but {= GAPS()['le11_at'] =} | {= '%.1f' % GAPS()['le11_ex'] =} points |
  | share finishing in 11, on {= GAPS()['le11_at'] =} | {= '%.1f' % GAPS()['le11'] =} points |

  The "all DRs" numbers hold too: the HTR routes study's all-DR headlines move by at most {= '%.1f' % GAPS()['q3all'] =} points. What does shift is the bad-edge mix inside a subset. With each scramble counted once, 0e is up to {= '%.0f' % GAPS()['e0'] =}% rarer than uniform and 6e up to {= '%.0f' % GAPS()['e6'] =}% commoner. Not modelled: CO-first or direct DRs, EOs over 5 moves, the twin of a DR with its last move turned the other way (counted once), and which DRs a solver chooses to keep. Computed, not proven; the full tables are in the [HTR routes study's real-DR section](https://fmc.arhan.sh/htr-routes/#12-real-drs).
- **No hand bound for a 12 at 4–5qt.** There isn't one. What's here is the measurement that says a feature count won't give one, the reads ranked by what they buy at each target, and the kill rules that do exist. For a 10 or an 11 the two proven hand bounds do rule out a good share of 4–5qt DRs (section 3), but those are DRs you were dropping anyway.
- **Your HTR may not be the shortest.** Every HTR number assumes the shortest HTR on each side. How often a solver finds it, and how fast, is not something a BFS can measure. Where a number needs a computer to use (the optimal finish of a given DR, the rankings by exact odds, the sd figures, NISS@DR), it's marked **computer only** where it appears.
- **Reads I didn't test.** Bigger blocks than pairs, anything you only see after a few moves (moves to FR, the shape after the first qt), and Rodney's NISS@1qt features per skeleton, which is section 7's table rather than a read.
- **Width is only first moves.** JTuu's real question, how many finishes are within one of optimal, needs a count of solutions per state. Not done.
- **Not done either**: what share of DRs have an optimal finish that goes through a shortest HTR ([[T10409]]), and how many U2/D2 an optimal has per subset ([[D17576]]).
- **Stats are counted, not proven.** The optimal of every state is a Lean theorem, and the table the stats are counted from is that same table, entry for entry. What isn't formal is the counting on top: the percentages, the reads, and the symmetry weights behind "1,352 states at 18".

---

## Appendix A: all 48 subsets

Exact over all DR states. Fastest and Longest are the shortest and the longest optimal finish in the subset (the longest is God's number for the subset in DR moves). Those two are the answer key, **computer only**; the odds are the subset read, for the attempt. Every column counts DR-move finishes. With all 18 face turns allowed a finish is sometimes shorter (section 12), so for any moves the "In N" shares are lower bounds; it matters on {= (lambda s: ', '.join(s[:-1]) + ' and ' + s[-1] if len(s) > 1 else s[0])(['%s (shorter on %.0f%% of states)' % (c, x) for c, x in GAPS()['worst']]) =}. The 18-move states were not solved with all moves. Each row is a subset (corner subset and bad edges):

{{APPA}}

---

## Appendix B: odds by corner length and E-slice parity

For the big 3–5qt subsets. L = optimal corner solution. "Fastest" is the shortest optimal finish in the row, so a fastest minus L of +1 means no L-move finish exists there. Each row is a subset, an L and an E-slice parity:

{{APPB}}

---

## Appendix C: the 216 NISS@1qt cases

{{APPC}}

---

## Appendix D: odds by true pairs, all 48 subsets

One table per target. Each cell: the share finishing in that many moves or less, for DRs of that subset with that many true pairs (corner + U/D-layer edge, both touching stickers matching, 16 places to look). An empty cell means the subset has no state with that many pairs.

{{PAIRS}}

---

## Appendix E: the 46 corner cases

A corner case is what the corners look like up to rotation, mirror and turning a layer. The columns:

- **Bad corners**: where the bad ones sit in the shortest setup (fewest bad corners).
- **L**: the range of optimal corner solution lengths the case can have.
- **A typical DR**: a state of that case whose optimal finish is the median for the case, with that optimal next to it. This is what the case usually looks like.
- **Shortest setup**: the shortest scramble that produces those corners, so you can put the layout on a cube quickly. As a DR it is one of the rare best ones of its case (it finishes in as many moves as the scramble is long), so don't judge the case by it.
- **A qt takes it straight to**: the corner subsets one U or D quarter turn can reach with one qt less.
- **Told apart from a look-alike by**: for a case with the same bad corners and the same answer in the column before as another case, what separates the two (a colour test, or only the corner solution).
- **Share** is of the corner subset, all edge counts together. **In 10 … In 13** are the shares whose optimal finish is that long or shorter.

Each subset has three tables (what the case looks like, a typical DR and the setup, how it finishes), then a both-sides table where each row is a pair of cases, one on normal and one on inverse, in either order.

{{CORNERS}}

---

## Appendix F: HTR length on both sides, all 48 subsets

One table per subset, one row per pair of HTR lengths (the shorter of normal and inverse, then the longer, so "7 and 8" is 7 on one side and 8 on the other). Fastest is the shortest optimal finish in the row. These are the true shortest HTRs.

{{SQUARES}}

---

## Appendix G: a scramble for every subset

For each of the 48 subsets: a state with the longest optimal finish in the subset, and a state that finishes in exactly its longer HTR (so the HTR length is all the bound you get from HTR lengths, in every subset). Do the scramble on a solved cube. ✓ Lean: every optimal and every HTR length in the table (the subset names are computed). Each row is a subset:

{{WITNESSES}}

---

## Appendix H: every read at every target

For each corner-qt group and each finish you might need, what each read is worth. "How you get it": look (count or see it), recognise (know the corner case on normal and on inverse), solve (find the shortest HTR on both sides, or the optimal corner solutions).

- **Best 10%, 25%, 50% keeps**: rank the group's DRs by the read, keep that share of them, and this is the share of the finishes in T you still have.
- **Drop, keeping 90%, 95%, 99%**: the share of the group's DRs you can drop while keeping that share of the finishes in T.
- **In classes under 1%**: the share of the group's DRs that the read puts in a class where at most one in a hundred finishes in T. The last column is the share of the finishes in T those classes hold.

Every number is the best any rule based on that read could do, so like the ranking tables earlier these are **computer only**: ceilings, not rules to carry. The hand versions are the plain rules and the guide per subset. Each group has two tables, ranking and throwing away.

{{PIV_FULL}}

---

## Docs and sheets referred to

{{DOCS}}
- Levi Gibson, sheet "Corner Solution Length x DR Finish length" (sampled; Appendix B is the exact version): https://docs.google.com/spreadsheets/d/14rZI1Nf84Og1jS8dN1MfT0sYhvdIWu9gPXkHDs1iVU4
