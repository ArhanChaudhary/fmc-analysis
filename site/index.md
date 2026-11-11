# FMC case studies

*AI-assisted case studies of various FMC concepts.*

Each study takes one question from Rubik's cube fewest-moves solving, answers it against exhaustive data, and says what a solver can do with the answer.

## Judging a DR by hand

What a solver can read off a domino reduction before solving it, how much each read says about the finish, and which lower bounds hold. Measured on the exact optimal finish of all 19,508,428,800 DR states.

- [Write-up](judging-a-dr/): what the full BFS says. It opens with a guide per subset.
- [Worked examples](judging-a-dr/examples.html): eleven DRs read step by step, then 100 scrambles with the DRs on the page and the answers folded away.
- [Errata](judging-a-dr/errata.html): corrections to the docs and sheets involved, and claims from the server that the full search settles.

## Is DR-xs worth it?

What it costs to leave slices unsolved at DR (DR-1s, DR-2s 8fe), how often a slice EO is there, and what it buys on real scrambles. Counted over all 768 kinds of DR-xs state, the 2.2 billion cosets of the DR group, and 500 scrambles.

- [Write-up](is-dr-xs-worth-it/): the costs, the odds and the claims check. It opens with the short version.
- [Worked examples](is-dr-xs-worth-it/examples.html): the tutorial's example with the numbers, then 100 scrambles with their slice-EO skips and the DR-xs routes on them, answers folded away.
- [Errata](is-dr-xs-worth-it/errata.html): corrections to the docs involved, and what the numbers settle.
