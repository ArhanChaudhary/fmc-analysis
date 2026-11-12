# instools: specification

The computational core of the case study "Insertion cost by skeleton type" (fewest-moves solving of the Rubik's cube).
Everything is counted in HTM (the 18 face turns U U2 U' D .. B'), centers fixed.

## 1. Model

**Sequences.** A sequence is *reduced* when no two consecutive moves turn the same face and two consecutive moves on
opposite faces come in a fixed order (U before D, R before L, F before B). `cancel(seq)` merges every run of
consecutive moves about one axis face by face (R L R' -> L; R R -> R2; R L2 R' L2 -> nothing) and repeats until
nothing changes; the result is reduced. The reference implementation is `cancel` in `src/cube.py`.

**Skeleton and leftover.** A skeleton S = m1 .. mn (reduced) solves a scramble Z up to a leftover: Z·S = c, where c
moves or twists only a few pieces. (Sequences compose left to right: "A·B" = do A, then B. The state conventions are
those of `src/cube.py`: a sticker-level cube built from geometry; use it as the reference for every check.)

**Insertion.** At position i (0..n), with X = m1..mi and Y = m(i+1)..mn, inserting a sequence A gives the sequence
cancel(X + A + Y). It solves the scramble exactly when A, as a cube transformation, equals g_i = Y · c^-1 · Y^-1.
Its cost is len(cancel(X + A + Y)) - n.

**Insertion algorithms.** For a cube element g and a bound L, Algs_L(g) is the set of all reduced sequences of
length <= L whose product is g. No list of "known algorithms" is used: every sequence up to L counts.

**Simple elements** (what one insertion may do): by family
- `3c`: corner 3-cycles (3 corners cycle, everything else untouched; 1008 elements)
- `3e`: edge 3-cycles (1760 elements)
- direct families, used only in the "direct" model: `2c2c` (two disjoint corner swaps, any twists, 5670 elements),
  `2tc` (two corners twisted in place, 56), `3tc` (three corners twisted the same way, 112), `2e2e` (two disjoint
  edge swaps, 11880), `2f` (two edges flipped in place, 66).

**Leftover types** (what a skeleton leaves), each with a uniform distribution over its elements:
`3c`, `2tc`, `3tc`, `2c2c-pure` (both swaps untwisted: 1890 elements), `2c2c-twisted` (3780), `3c1t` (a 3-cycle with
net twist plus one twisted corner, 10080), `5c` (a corner 5-cycle, 108864), `3e`, `2f`, `2e2e` (both swaps unflipped,
5940), `2e2e-flipped` (5940), `3e1f` (a flipped 3-cycle plus one flipped edge, 15840), `5e` (an edge 5-cycle, 304128).
These are exactly the types that two 3-cycles can make, together with `3c3c` (90720) and `3e3e` (591360), which are
optional (`src/leftover_types.py`, `out/types.json`).
Check each count by enumeration.

**Solving a leftover with k insertions.** Insertions are done one after the other: the first into S, the second into
the sequence that results (so it may sit inside the first algorithm: a nested insertion), each of them an element of
an allowed simple family, the last one finishing the solve. The cost is the final length minus n.
Models (report all that apply):
- `one`: one insertion of family 3c (for type 3c) or 3e (for type 3e).
- `two`: two insertions of 3-cycles of the same kind of piece (corner types except 3c; edge types except 3e),
  nesting allowed.
- `two-separate`: as `two`, but the second insertion is at a position of the original skeleton and no move of the
  first algorithm cancels or merges with a move of the second (the two insertions do not touch). Drop this model if
  it is not easy to make exact, and say so.
- `direct`: one insertion of the direct family of the type, where the type has one.
- `best`: the minimum of the applicable models.
Each for L = 8 and L = 10; and L = 12 if the tables fit in memory and time (see limits).

Everything about one skeleton must be exact for its model: the minimum over every position and every algorithm in
Algs_L. If you prune, prune only with proven bounds.

## 2. What to build

A Rust crate `instools` in this folder (Rust, not C or C++; release profile with lto; rayon for parallelism; no
network dependencies beyond crates.io). Suggested subcommands:

1. `algs <L>`: build Algs_L for every simple family, by meet-in-the-middle over reduced sequences from the solved
   cube, using the 24 rotations of the cube and inversion to work on one representative per class of elements and
   to transport the lists to the other elements. Write (a) `out/cases_<family>.tsv`: one line per class: a
   representative (as a move sequence of minimal length and as a readable description of which pieces go where),
   class size, optimal length (the shortest sequence, or ">L"), and the number of algorithms of each length up to L;
   (b) a binary or text file with all algorithms, reloadable by the other subcommands.
2. `best <scramble> <skeleton>` (and a batch form reading lines `scramble<TAB>skeleton`): detect the leftover type,
   compute the cost under each model and bound, and print for each the insertions (position, algorithm, moves
   cancelled), the final solution with cancelling done, and its length.
3. `sample <type> <n> <count> <seed>`: random skeletons of length n (each move uniform among those that keep the
   sequence reduced), a uniformly random leftover of the type; output one line per skeleton with the cost under
   each model and bound, plus for the best solution: positions of the insertions, algorithm lengths, moves
   cancelled, whether it is nested. Deterministic for a given seed.
4. `corpus <file>`: the same statistics for skeletons taken from a file of move sequences (one per line), each with a
   uniformly random leftover of the given type.

Python (in `src/`): a checker that replays, on the sticker model, every solution printed by `best` and by a sample
of `sample` lines (the scramble is rebuilt from skeleton and leftover), and compares lengths.

## 3. Checks that must pass before you report

- The cube model in Rust agrees with `src/cube.py` on random sequences (states and `cancel`). Generate the move
  tables from `cube.py` rather than typing permutations.
- Family and type sizes as listed in section 1.
- The shortest corner 3-cycles are 8 moves (commutators such as `R U R' D R U' R' D'`; verify any algorithm on the
  sticker model before using it as a test). Report the distribution of optimal lengths per family as you find it.
- Brute force on small cases: for 200 random (skeleton, leftover) pairs of type 3c with n = 6, compare `one` at L = 8
  with a direct enumeration that inserts every 8-move sequence (all 18^8 are too many: enumerate the algorithms by
  an independent method, for example breadth-first search to depth 8 from the element with a different data
  structure, or all reduced sequences of length 8 filtered on the sticker model for a few elements).
- Every printed solution solves its scramble on the sticker model and has the printed length.
- Insertion Finder pages: the knowledge base has pages saved from the Insertion Finder with scramble, skeleton and its
  insertions (list them with `source /data/fmc/env.sh; /data/fmc/kb/fmcq docs "Insertion Finder Result"`, read the
  files it points to). For each page that parses, run `best` and report your best length under each model next to
  the Insertion Finder's. You should never be worse than it when its algorithms are within your bound; say where
  you are, and why.

## 4. Limits of this machine

4 cores, 7.7 GB RAM, no swap; other jobs may be running. Keep one heavy job at a time and stay under about 4 GB
(`systemd-run --user --scope -q -p MemoryMax=4G <command>`). Depth-6 meet-in-the-middle (L = 12) needs care: if it
does not fit, do L = 12 for the corner 3-cycles only, or stop at L = 11, and say so. Put large generated files under
`out/` (they will not be committed).

## 5. Runs to do once it works

- `algs` for L = 8 and 10 (and 12 if feasible).
- `sample` for every leftover type and n = 10, 12, 14, ..., 30: 20,000 skeletons each at L = 8 and at L = 10 (fewer
  where a model is too slow: say how many), and L = 12 where built. Write `out/sample_<type>_n<n>.tsv`.
- A summary table `out/summary.tsv`: type, n, model, L, number of skeletons, mean cost, and the share with cost
  <= 2, 3, ..., 12.

## 6. Report back

What was built and where; the checks of section 3 with their output; the optimal-length distribution of each
family; the summary table for n = 20 (all types, models and bounds); the Insertion Finder comparison; running times;
anything that did not go as specified and anything you are unsure about. Do not commit or push. Do not touch
anything outside /data/fmc/insertion-cost/ except reading.
