# fmc-analysis

**Read the case studies: https://fmc.arhan.sh/**

fmc-analysis is a collection of AI-assisted case studies of various Rubik's Cube FMC (fewest move challenge) concepts, with an emphasis on formal verification. The goal of this project is to produce useful research that can be communicated to professional FMC solvers. This project was only made possible under the following few conditions:

- I recently attended YCombinator's [startup school](https://www.startupschool.org/) and was gifted 6 months of Anthropic's Claude Ultra plan;
- as well $10,000 in Microsoft Azure credits
- I have had an interest in computational Rubik's Cube theory

# Notice

The rest of this document, as well as every case study and the website, was entirely written using AI.

## Case studies

| Study | Question | Read |
|---|---|---|
| [`judging-a-dr/`](judging-a-dr/) | What can you read off a domino reduction (DR) by hand, how much does each read say about the finish, and which lower bounds hold? Measured on the exact optimal finish of all 19,508,428,800 DR states. | [Write-up](https://fmc.arhan.sh/judging-a-dr/) · [Worked examples](https://fmc.arhan.sh/judging-a-dr/examples.html) · [Errata](https://fmc.arhan.sh/judging-a-dr/errata.html) |
| [`is-dr-xs-worth-it/`](is-dr-xs-worth-it/) | What does it cost to leave slices unsolved at DR (DR-1s, DR-2s 8fe), how often is a slice EO there, and what does it buy on real scrambles? Counted over all 768 kinds of DR-xs state, 2.2 billion cosets, and 500 scrambles. | [Write-up](https://fmc.arhan.sh/is-dr-xs-worth-it/) · [Worked examples](https://fmc.arhan.sh/is-dr-xs-worth-it/examples.html) · [Errata](https://fmc.arhan.sh/is-dr-xs-worth-it/errata.html) |
| [`insertion-cost/`](insertion-cost/) | What does a 3c, a 5c, a 2c2c, a 3c1t or a pair of twisted corners add to a skeleton, by skeleton length and alg length, and how much shorter must one kind of skeleton be than another? Every skeleton searched exactly: random skeletons by type and length (20,000 each with 8-move comms, fewer with longer algs), and the worked examples people posted from real solves. | [Write-up](https://fmc.arhan.sh/insertion-cost/) · [Worked examples](https://fmc.arhan.sh/insertion-cost/examples.html) · [Errata](https://fmc.arhan.sh/insertion-cost/errata.html) |
| [`eo-to-dr/`](eo-to-dr/) | How far is a random scramble from DR on one axis, on the best of three, with the inverse and with NISS, and through the short EOs a solver writes down? How many EOs does a scramble have, and what does an EO leave with the other DR axis, the inverse, the last EO turn switched or EO-breaking turns? Exact distance tables on 50,000 uniformly random scrambles, and every EO-solved state exactly. | [Write-up](https://fmc.arhan.sh/eo-to-dr/) · [Worked examples](https://fmc.arhan.sh/eo-to-dr/examples.html) · [Errata](https://fmc.arhan.sh/eo-to-dr/errata.html) |
| [`htr-routes/`](htr-routes/) | Which routes to HTR find the optimal finish from a DR, subset by subset, in what order to try them and how long their HTRs are? How effective is DR bounding, and does FakeMMAP's reduction bound prune? 25,000 uniformly random DR states per subset × edges, every optimal and +1 finish in every NISS reading, on the exact table of all DR states. | [Write-up](https://fmc.arhan.sh/htr-routes/) · [Worked examples](https://fmc.arhan.sh/htr-routes/examples.html) · [Errata](https://fmc.arhan.sh/htr-routes/errata.html) |
| [`eo-switch/`](eo-switch/) | After EO + RZP, when should you switch to the inverse? A switch card per DRM that a solver checks by tracing, with the sub-7 share of each verdict; how to read each feature from the normal side; what a real RZP changes; every server rule graded. Every EO-solved case exactly, and 121.5 million real attempts from 6,000 uniformly random scrambles. | [Write-up](https://fmc.arhan.sh/eo-switch/) · [Worked examples](https://fmc.arhan.sh/eo-switch/examples.html) · [Errata](https://fmc.arhan.sh/eo-switch/errata.html) |

## Layout

Every study is one folder with the same shape:

| Path | What |
|---|---|
| `<study>/README.md` | What the study is, what is in the folder, how to reproduce it. |
| `<study>/report/` | The write-up (`WRITEUP.md`), worked examples (`EXAMPLES.md`), errata (`BUGS.md`) and the tables they include. |
| `<study>/research/` | The programs, the analysis scripts and the result tables. |
| `<study>/lean/` | The Lean proof, where a study has one. |

Shared by all studies:

| Path | What |
|---|---|
| `scripts/build-pages.sh`, `site/` | The website: a front page (`site/index.md`) and each study's reports as pages. Needs pandoc. |
| `.github/workflows/pages.yml` | Builds the site with that script on every push to `main` and deploys it to GitHub Pages. |
| `env.sh` | Tool paths on the machine the studies are built on. |

## What is not here

- The Discord export that the studies quote from, and the knowledge base built from it. They are other
  people's messages and documents. The reports link to each message they cite.
- Large generated tables. Each study's README says how to rebuild its own.

## The website

    scripts/build-pages.sh /tmp/fmc-site      # needs pandoc

A new study appears on the site once its folder has a `report/WRITEUP.md` and `site/index.md` links to it.
