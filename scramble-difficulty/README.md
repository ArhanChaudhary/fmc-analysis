# Easy or hard? Reading a scramble before you look for DRs

A draft study, unlisted on the site: can you tell an easy scramble from a hard one, and the DR axis worth searching, before you look for DRs? Measured on 23,879 scrambles (10,000 uniform states, the 8,108 padded official FMC scrambles of the WCA results export of 13 November 2026, and 5,771 scrambles made with tnoodle-lib's own solver), each with every EO-first DR of at most 10 moves and its exact optimal finish.

Main results: bad edges decide how many DRs a scramble has and corners don't; the shortest EO and the number of 4-move EOs get four fifths of what any model can predict; a DR on one axis is paid for by the EOs of the other two, so the best DR axis is the one whose own EOs are worst; the scramble's text is a NISS DR of 12 to 19 moves and predicts nothing on current official scrambles.

It builds on torchlight's guess about the axis, Levi Gibson's corner QT count and seven counts, Zagros's and rodneykinney's proposals, the EO-count heuristics of Tom Nelson, Yura Riabov, Lewis Isom and jisu101, JTuu's question about where the DRs come from, DougCube's sheet of official scrambles, TNoodle's source, and the earlier studies of this repository (judging-a-dr, eo-to-dr, eo-switch, and the DR population in `gaps/research`).

| Where | What |
|---|---|
| [report/WRITEUP.md](report/WRITEUP.md) | the write-up |
| [research/](research/) | the scripts (`src/`), the small outputs the tables are read from (`out/`), and how to rerun it (`README.md`) |
| [lean/ScrDiff/](lean/ScrDiff/) | the Lean project: 30 theorems about the example scrambles and DRs on the page |
| `UNLISTED` | marker file: the page is built but not linked from the front page |

The large inputs (the DR lists, the WCA export, the generated scrambles) are not in the repository.
