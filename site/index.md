# FMC case studies

*AI-assisted case studies of various FMC concepts.*

Each study takes one question from Rubik's cube fewest-moves solving, answers it against exhaustive data, and says what a solver can do with the answer.

## Decision cards

[Six questions from the middle of an attempt](decision-cards.html), answered from the studies' data: should I add partial EOs to my list, should I stop looking for EOs, should I switch this EO, should I add random moves to this EO, should I keep checking variants of this route, should I NISS in the middle of this route. Each card gives the rule, what you check at the table and the numbers behind it.

## Reference tables

Single tables that answer one question, too small for a study.

- [Half turns before the first quarter turn](tables/half-turns-before-first-qt.html): per subset × edges, how often an optimal finish needs 0, 1, 2 or more half turns before its first qt on the better side, for all DRs and for DRs with an optimal of 13 or less and 12 or less.

## HTR cases

[Every HTR case of a DR](htr-cases/), up to rotations, mirrors and the E slice: 1,272 cases by subset, bad edges and moves to HTR. Each is drawn in 3D with its bad pieces, with every HTR of 8 moves or less, its lookalikes and how to tell them apart (4b2 parity, 2c3 direction, a corner test). Type a scramble and your moves to find your own DR's case, with its HTRs in your orientation. For other programs: [a shortest generator of every case](htr-cases/htr-cases.txt).

## Judging a DR by hand

What a solver can read off a domino reduction before solving it, how much each read says about the finish, and which lower bounds hold. Measured on the exact optimal finish of all 19,508,428,800 DR states.

- [Write-up](judging-a-dr/): what the full BFS says. It opens with the short version, then a guide per subset.
- [Worked examples](judging-a-dr/examples.html): eleven DRs read step by step, then 100 scrambles with the DRs on the page and the answers folded away.
- [Errata](judging-a-dr/errata.html): what the full search shows is wrong in the docs and sheets involved and in things said on the server, each with an example.

## Is DR-xs worth it?

What it costs to leave slices unsolved at DR (DR-1s, DR-2s 8fe), how often a slice EO is there, and what it buys on real scrambles. Counted over all 768 kinds of DR-xs state, the 2.2 billion cosets of the DR group, and 500 scrambles.

- [Write-up](is-dr-xs-worth-it/): the costs, the odds and the claims check. It opens with the short version.
- [Worked examples](is-dr-xs-worth-it/examples.html): the tutorial's example with the numbers, then 100 scrambles with their slice-EO skips and the DR-xs routes on them, answers folded away.
- [Errata](is-dr-xs-worth-it/errata.html): what the numbers show is wrong in the docs involved and in things said on the server, each with an example.

## Insertion cost by skeleton type

What a 3c, a 5c, a 2c2c, a 3c1t or a pair of twisted corners adds to a skeleton, by skeleton length and by how long an alg you allow. Every skeleton searched exactly: random skeletons by type and length (20,000 each with 8-move comms, fewer with longer algs) and the worked examples people posted from real solves, with the leftover types and the algs of up to 12 moves counted exhaustively.

- [Write-up](insertion-cost/): the costs, the odds, the exchange rates between types and the claims check. It opens with the short version.
- [Worked examples](insertion-cost/examples.html): worked examples from the tutorial and the server redone with the search, then 200 skeletons to play along with, answers folded away.
- [Errata](insertion-cost/errata.html): what the numbers show is wrong in things said on the server, each with an example.

## EO to DR, and scramble to DR

How far a random scramble is from DR on one axis, on the best of three, with the inverse and with NISS, and through the short EOs a solver writes down; how many EOs a scramble has and how short; and what an EO leaves with the other DR axis, the inverse, the last EO turn switched or EO-breaking turns, case by case. Exact distance tables on 50,000 uniformly random scrambles, and every EO-solved state exactly.

- [Write-up](eo-to-dr/): the odds of a DR in 8, 9, 10 and 11, the EO inside the optimal DR, EO counts, EO to DR with every option, and the claims check. It opens with the short version.
- [Worked examples](eo-to-dr/examples.html): 150 scrambles with their shortest DRs and their best DRs through EOs of at most 4 and 5, then 60 EO-solved states by case, answers folded away.
- [Errata](eo-to-dr/errata.html): what the numbers show is wrong in things said on the server, each with an example.

## Which HTR routes to try from a DR

From a DR to HTR: which routes find the optimal finish on each of the 48 subsets, in what order to try them and how long their HTRs are; linear against NISS HTR; DR bounding measured per subset; FakeMMAP's reduction-length bound tested. 25,000 uniformly random DR states per subset, each with every optimal and +1 finish read in every NISS way, on the exact table of all 19,508,428,800 DR states.

- [Write-up](htr-routes/): the checklists per subset, the existing sheets, HTR lengths, bounding, FakeMMAP's bound, hand checklists and the claims check. It opens with the short version.
- [Worked examples](htr-routes/examples.html): 200 DR states from the 20 most common subsets, with the routes that find each optimal written out and the shortest bounding reduction, answers folded away.
- [Errata](htr-routes/errata.html): what the numbers show is wrong in things said on the server, each with an example.

## When to switch an EO

After EO + RZP, when to switch to the inverse and look for a DR there. Every policy is graded by what it misses: how much it switches, and which share of the 4-movers, 5-movers and 6-movers it leaves behind. The answer is a switch card per DRM, put together mostly from reads people on the server already had: count pairs first, then one more look that depends on the pair count (where 2 pairs sit and where the stuck E-slice edges are; ARM 20, 21 or 22 with the corner type and side pairs for 1 pair; no fake pairs for 0 pairs). ARM, the fast read, is on every 1-pair case; the slower reads on a minority. On 4c4e, 4c2e, 3c2e and 7c8e together it switches a little less than the pairs rule (27.0% against 27.6%) and misses none of the cases of 4 or less (5.1%), 3.3% of the 5-movers (12.8%) and 30.3% of the 6-movers (37.0%). Also: the half-turns-to-two-bars count judged as a switch test, what didn't help, and how far any rule could go. Every EO-solved case exactly, with a check on 8.4 million real attempts.

- [Write-up](eo-switch/): the yardstick, the current policies by what they miss, the cards, every read done on the normal side by colour, two bars evaluated, what didn't help, the ceilings, other RZP lengths. It opens with the short version.
- [Worked examples](eo-switch/examples.html): 201 real attempts, with what you see before switching, the reads, the card's verdict next to the pairs rule's, and the optimal DR after the switch, answers folded away.
- [Errata](eo-switch/errata.html): what the numbers show is wrong in something said on the server, with an example.

## Implied EOs

When one EO on a scramble guarantees another: F B (F B) with R L (R L) and U D (U D), F B (F) with R L (B R L), R F B (F) with L (B R L) and the rest. The full list for EOs of 5 moves or less (691 sets of scrambles in seven kinds, all from one small dictionary between axes), the exact test for any two EOs, the proof that nothing but the F B R L trick is behind them up to 5 moves, the other source that starts at 6 moves (a superflip on both sides), and how often a scramble has such a pair (26.9%). Also the sub-6 EOs implied by a longer EO that you never write but can see, like F B (F U2 B) from U D (D U2 F U): one trace after F B covers the EOs that start with R L and U D too. Proved in Lean for every scramble.

- [Write-up](implied-eo/): the seven kinds, the four theorems, the dictionary, the claims check. It opens with the short version.
- [The full list](implied-eo/examples.html): all 691 sets and the 230 patterns after F B, each with a random scramble that has its EOs.

## Pruning the search for a DR solution

Which HTRs are worth finishing when you look for a leave-slice solution from a 2qt, 3qt or 4qt DR in 12, 13 or 14. The rule bound of Advanced DR Bounding removes 96–97% of the HTRs in reach of the goal and never a within-goal one. A pair count at HTR does the same job again: with n moves left for the finish you need at least 16 − 4n pairs, proved in Lean. Together they leave a few dozen HTRs per DR out of thousands. Then the order to finish them in (most pairs first), what pairs say at 2qt and at HTR, which skeleton to start with, what NISS adds, and when to abandon the DR. Every HTR in reach finished exactly for about 2,000 uniformly random DRs of each kind, 66 million HTRs.

- [Write-up](dr-variants/): the two floors, the order of finishing, skeletons, NISS, abandoning, the meta step by step, ten worked scrambles and the claims check. It opens with the short version.

## The skeleton/variant meta

A search meta for DR finishes built on Advanced DR Bounding. On normal and inverse, take the variants of each corner skeleton with P+S+T ≤ 5, at most 1 extra move before 2qt and an HTR at least one move under the goal. Discard the ones whose corner-case-aware bound doesn't fit the goal, and finish the rest shortest HTR first, most pairs first among HTRs equally far. A skeleton that ends in HH gets a premove pass as well. Per corner case, from 4b2 to 4c4: how often it misses a within-goal finish (0–6.7%), how many fewer HTRs it finishes than a search without DR Bounding (11–18×), how soon a finish is found, and what other bounds and caps would change. About 2,000 uniformly random DRs of each kind, every HTR in reach finished exactly.

- [Write-up](skeleton-variant-meta/): the meta step by step, its stats per corner case, where the misses come from, what the cap on the moves to HTR and the premove pass change, the other bounds and caps, and the data and method.
- [Example solves](skeleton-variant-meta/examples.html): 46 scrambles from 2c4 to 4a1 solved with the meta, skeleton by skeleton: the 8 skeletons with the fewest moves to HTR, the variants checked on each, the solutions found and some near-misses.
- [HTR search order and limits](skeleton-variant-meta/order-and-limits.html): what going one skeleton at a time costs against finishing the shortest HTR first, which caps on HTR length keep 95% of the solutions for the fewest HTRs, and how much NISS is needed.

## Corners in 3D

The corners of any state, not just a DR, with DBL held and R, U, F turns: what you can see on them, what you can prove from it about the distance to HTR, and whether it tells you the turn that gets closer. A corner shows one of six types and a quarter turn changes them by one rule. Types alone find real HTR exactly 1 time in 6, with parity 1 in 3, with the D-colour corners 1 in 2, and the three together fix the case: HTR is every corner good, D-colour corners in a 4a picture, parity even. A fake HTR is exactly 9 moves from HTR even with off-axis turns. Floors with how tight each is (a count table read at a glance, the distance to triple DR, the parity and colour upgrades, which ones survive NISS), every rule for the next turn graded by distance, what the twist costs on top of the subset number of the placement (0, 2, 4, 6 or 8 quarter turns), and DR corner cases solved with and without leaving DR. Exact over all 3,674,160 corner states, proved in Lean.

- [Write-up](corners-3d/): the types and their rule, the three reads, the floors, the next turn, quarter turns, DR from outside, the mazes and the claims check. It opens with the short version.
- [Worked examples](corners-3d/examples.html): twelve states read step by step, every pattern within 3 moves of all good, 200 random states with the answers folded away, and DR cases in DR turns and with all turns.
- [Errata](corners-3d/errata.html): what the search shows is wrong in something said on the server, with an example.
- [Look up a state](corners-3d/tool/): type a scramble, get the corner types, the floors, the distance to HTR and the turns that get closer.
