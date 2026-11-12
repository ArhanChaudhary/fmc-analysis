# FMC case studies

*AI-assisted case studies of various FMC concepts.*

Each study takes one question from Rubik's cube fewest-moves solving, answers it against exhaustive data, and says what a solver can do with the answer.

## Judging a DR by hand

What a solver can read off a domino reduction before solving it, how much each read says about the finish, and which lower bounds hold. Measured on the exact optimal finish of all 19,508,428,800 DR states.

- [Write-up](judging-a-dr/): what the full BFS says. It opens with a guide per subset.
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
