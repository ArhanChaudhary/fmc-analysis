# FMC case studies

*AI-assisted case studies of various FMC concepts.*

Each study takes one question from Rubik's cube fewest-moves solving, answers it against exhaustive data, and says what a solver can do with the answer.

## Reference tables

Single tables that answer one question, too small for a study.

- [Half turns before the first quarter turn](tables/half-turns-before-first-qt.html): per subset × edges, how often an optimal finish needs 0, 1, 2 or more half turns before its first qt on the better side, for all DRs and for DRs with an optimal of 13 or less and 12 or less.

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

After EO + RZP, when to switch to the inverse and look for a DR there. Count the turns of the side faces with U and D turns free: for 4c4e the half turns to two bars sort it into certain (0 or 1), 72% (2), 16% (3) and under 2% (4 or 5), and every DRM has its short setups. Also a switch card per DRM for a plain pair trace; how to read it all from the normal side; what a real RZP changes; every switch rule from the server graded. Every EO-solved case solved exactly, and 121.5 million real attempts from 6,000 uniformly random scrambles.

- [Write-up](eo-switch/): the two rings and the half-turn count for 4c4e, side turns for every DRM, the switch cards, the tracings, the RZP bias and the last turns, the rules graded, the sheets reproduced and the claims check. It opens with the short version.
- [Worked examples](eo-switch/examples.html): 200 real attempts, with what to trace before switching, the rings and the count, the card's verdict and the optimal DR after the switch, answers folded away.
- [Errata](eo-switch/errata.html): what the numbers show is wrong in things said on the server, each with an example.
