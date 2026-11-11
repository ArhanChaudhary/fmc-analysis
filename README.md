# AI-assisted case studies of various FMC concepts

Each study takes one question from Rubik's cube FMC (fewest moves), answers it against exhaustive data,
and says what a solver can do with the answer. The studies are written with Claude; the commits in this
repository are Claude's.

**Read them at [fmc.arhan.sh](https://fmc.arhan.sh).**

## Case studies

| Study | Question | Read |
|---|---|---|
| [`judging-a-dr/`](judging-a-dr/) | What can you read off a domino reduction (DR) by hand, how much does each read say about the finish, and which lower bounds hold? Measured on the exact optimal finish of all 19,508,428,800 DR states. | [Write-up](https://fmc.arhan.sh/judging-a-dr/) · [Worked examples](https://fmc.arhan.sh/judging-a-dr/examples.html) · [Errata](https://fmc.arhan.sh/judging-a-dr/errata.html) |

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
