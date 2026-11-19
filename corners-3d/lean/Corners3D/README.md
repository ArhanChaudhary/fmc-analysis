# Corners3D: a Lean 4 certificate for "corners in 3D"

Lean 4.35.0, no Mathlib.

The puzzle: the eight corners of the cube with DBL held fixed, turned by R, U and F only (3,674,160 states). The
target is HTR, the 24 states that R2, U2, F2 reach. Turns are counted in HTM, and separately in quarter turns with
half turns free.

- `Cube.lean`, `Pieces.lean` and `Search.lean` are copied, unchanged but for the namespace, from the project's other
  certificates (`corners-htr/lean/CornersHTR`): the 54-sticker model, the corner twist tables read off it, and the
  searches with their checks. No permutation is typed by hand.
- `Corners.lean` (coordinates, kinds, colour pictures, tables), `Checks.lean` (the checks, as compiled functions),
  `Theorems.lean` (the checks, run), `Proofs.lean` (what they mean for every sequence of turns), `Witness.lean` /
  `Examples.lean` (examples on the sticker model) and `Pages.lean` (every scramble the pages print) are new.

Build with `lake build`. It takes about 1.5 minutes and under 1 GB of memory on an 8-core machine.

## Words

A corner shows one of six **kinds**, written 0 … 5:

| Kind | In words |
|---|---|
| 0 | good: in its own tetrad, all three stickers on faces of their own axis |
| 1 | twisted clockwise: in its own tetrad, no sticker on a face of its own axis |
| 2 | twisted counter-clockwise: the same, the other way round |
| 3 | out: in the other tetrad, only the R/L sticker on a face of its axis |
| 4 | out: in the other tetrad, only the U/D sticker on a face of its axis |
| 5 | out: in the other tetrad, only the F/B sticker on a face of its axis |

The tetrad of a place is the sign of x·y·z: DBL's tetrad is DBL, UFL, UBR, DFR; the other is UFR, UBL, DFL, DBR.
The kinds of a state are written for the places UFR UFL UBR DFR UBL DFL DBR, in that order.

## What is proved

### By induction, for every sequence of turns (`Proofs.lean`, no `native_decide` in the file)

| Theorem | It says |
|---|---|
| `floor_of_check` | If f is 0 on the goal and no turn lowers f by more than 1, every sequence of turns from x into the goal has at least f x turns. |
| `wfloor_of_check` | If g is 0 on the goal, half turns do not lower it and a quarter turn lowers it by at most c, every solution has at least g x / c quarter turns. |
| `exact_of_check` | If moreover f is 0 only on the goal and some turn always lowers it by 1, f x is exactly the fewest turns: a sequence of f x turns exists and none is shorter. |
| `types_floor` | No sequence of turns reaches HTR in fewer turns than it takes to make every corner good (to reach triple DR). |
| `parity_floor` | Nor in fewer than it takes to make every corner good with an even placement. |
| `placement_floor` | Nor in fewer than the placement alone needs, twists ignored. |
| `weight_floor` | Count 1 per out corner and 2 per twisted corner: every solution has at least a quarter of that many quarter turns. |
| `quarter_floors` | Every solution has at least `qHTR` quarter turns, at least the quarter turns to all good (and to all good with even placement), and at least the placement-only count. |
| `floors_le_distance` | The three floors in turns never exceed the true distance. |
| `dHTR_exact`, `dGood_exact`, `dGoodEven_exact` | The three tables in turns are exact: a sequence of that length exists, and none is shorter. |
| `every_state_reached` | Every one of the 3,674,160 coordinates is reached from solved by a sequence of turns. |
| `same_kinds_stay_same` | Two states that show the same kinds show the same kinds after any sequence of turns. |
| `same_kinds_same_solution` | So a sequence that makes one of them all good makes the other all good. |
| `run_injective`, `run_invSeq`, `run_then_invSeq` | A sequence of turns never sends two states to one state, and its inverse sequence undoes it. |
| `types_solution_hits_every_good_state` | **The 1 in 6.** If a sequence makes x all good, then for every all-good state g exactly one state showing the same kinds as x is sent to g. With 144 all-good states, 24 of them HTR, and 144 states per kinds pattern: exactly 24 of the 144 states that show x's kinds land in HTR, the other 120 in a fake HTR. |
| `htr_iff` | A state is in HTR exactly when every corner is good, the D-coloured corners sit in one of six pictures, and the placement is even. |

### By computation over all states (`Theorems.lean`, each closed with `native_decide`)

| Theorem | It says |
|---|---|
| `model_ok` | Each of the nine turns carries each corner's sticker list onto its destination's, shifted cyclically; turns the corners by 0 mod 3 in total; leaves DBL alone. The coordinate maps are bijections. |
| `coords_follow_stickers` | On the 820 sticker states within 3 turns of solved and for each turn, the coordinate after the turn, read off the stickers, is `step` of the coordinate before. |
| `cord_is_counterclockwise`, `place_names_ok` | The sense in which twists are counted, and that the seven place names are the right ones. |
| `all_reached` | The table of turns from solved is exact and is the known 2x2x2 table: 1, 9, 54, 321, 1847, 9992, 50136, 227536, 870072, 1887748, 623800, 2644 (God's number 11). |
| `tetrad_theorem` | The states within 3 turns show all 148 (place, piece, twist) combinations. On them: a corner in its own tetrad has 3 oriented stickers or none, a corner in the other tetrad exactly 1, and the kind computed from the coordinates is the kind the stickers show. |
| `rule_in_words`, `rule_table` | What a turn does to a kind. A half turn changes nothing. A quarter turn about axis a makes good ↔ out with the axis-a sticker oriented, and twisted ↔ out with one of the other two stickers oriented; the table gives which. |
| `quarter_rule` | For every state and turn, the kinds after the turn are `kindStep` of the kinds before: the kinds follow a rule that looks at nothing but the kinds. |
| `closed_ok`, `inv_ok` | No turn leaves the coordinates; each turn is undone by its inverse. |
| `goal_HTR`, `good_counts` | HTR has 24 states and is exactly what half turns reach. 144 states are all good, 24 of them HTR, 72 even. |
| `dHTR_check`, `dHTR_hist` | Turns to HTR: 24, 72, 432, 2304, 13464, 65496, 296400, 1077072, 1813680, 401472, 3744. God's number 10. |
| `qHTR_exact`, `qHTR_hist` | Fewest quarter turns to HTR (half turns free): 24, 432, 6768, 86184, 780048, 1708416, 1049856, 42048, 384. Maximum 8. |
| `dGood_*`, `dGoodEven_*`, `qGood_*`, `qGoodEven_*` | The same for "every corner good" (at most 9 turns, 6 quarter turns) and "every corner good, even placement" (9 and 7). |
| `perm_tables` | Placements only, all nine turns: turns 24, 72, 360, 1128, 1440, 1776, 240; quarter turns 24, 144, 720, 1416, 1776, 960. |
| `types_floor_check`, `parity_floor_check`, `placement_floor_check`, `weight_floor_check`, `quarter_floor_checks` | The local conditions the floor theorems rest on. |
| `floor_gaps`, `quarter_floor_gaps`, `floors_below`, `weight_hist` | How far each floor is below the truth. Types floor: exact on 1,134,744 states. Parity floor: exact on 1,977,024. |
| `qt_surcharge` | Fewest quarter turns minus the placement-only count: 0 for 1,274,064 states, 2 for 2,019,456, 4 for 360,864, 6 for 19,392, 8 for 384. Never odd. |
| `fake_htr_far` | The 120 all-good states outside HTR are each exactly 9 turns from HTR; 72 (odd) need 3 quarter turns, 48 (even) need 4. |
| `six_pictures`, `htr_iff_check` | The six pictures of the D-coloured corners in HTR, by place, and the check behind `htr_iff`. |
| `three_reads_fix_distance` | States with the same kinds, the same D-colour picture and the same parity are equally far from HTR, in turns and in quarter turns. |
| `types_and_two_colours_fix_state` | The kinds, the D-colour picture and the B-colour picture determine the state. |
| `types_class_size` | 25,515 kinds patterns occur, each shown by exactly 144 states, 72 even and 72 odd. |
| `oriented_ok`, `dr_tables` | The states oriented on an axis, one per placement, and the DR-only tables over them, exact: at most 11 turns and 5 quarter turns. |
| `dr_qt_same` | On a state oriented on an axis, quarter turns of the other faces never save a quarter turn: the HTR subset number is the same with all nine turns. All three axes. |
| `dr_turns_saved` | In turns they do: leaving the DR turns saves 0 on 3,024 of the 5,040 oriented states, 1 on 1,488 and 2 on 528. All three axes. |
| `placement_qt_same_on_three_axes` | For every placement, the quarter-turn count of the oriented state is the same on all three axes and equals the placement-only count. |

### Examples (`Examples.lean`)

One theorem per scramble, written by `gen_examples.py` from the study's tables and checked by Lean on the sticker
model with its own tables:

    theorem ex_0003 : check "R U" "1243403" 2 2 2 2 "U' R" = true := by
      native_decide

`check scramble kinds d q ft fp solution`: the state the scramble makes shows these kinds, is d turns and q quarter
turns from HTR, has types floor ft and parity floor fp, and the d-turn solution takes it into HTR.
`checkLoose scramble d q solution` checks the distances and any solution, shortest or not; `reaches scramble
sequence` only that a sequence ends in HTR.

    python3 gen_examples.py            # the built-in sample
    python3 gen_examples.py FILE       # one scramble per line, '#' starts a note that becomes the docstring

### What the pages print (`Pages.lean`)

Written by `research/src/lean_witness.py`: every scramble the write-up and the examples page print (the count table's
rows, the catalogue, the 200 random states, the DR cases, the patterns within two quarter turns, the worked examples),
305 in all, as lists checked with `check`. Each one: the types line, turns and quarter turns to HTR, the types floor,
the types + parity floor, and the printed solution (exactly that many turns, ending in HTR). Also `dr_only_solutions`
(the DR-turn solutions end in HTR and use U, R2, F2 only), `wen_case` (the errata's first item: the two 13-move
sequences and the 12-move one all solve the corners) and `niss_example` (one turn on the inverse reaches HTR from a
state 4 turns away).

Not in Lean: the distances with NISS, the ceilings of the "which turn" tables, and the search over all eight corners
with U, D and the half turns behind the errata's "12 is the shortest" (those are the Python searches of
`research/src/extra.py`).

## Trust

The theorems of `Theorems.lean`, `Examples.lean` and `Pages.lean` are closed by `native_decide`, which trusts Lean's compiler, as in
the project's other certificates. The tables are filled by one piece of code (`search.bfs`, `bfs01`) and checked by
another (`exactOK`, `floorOK`, `wfloorOK`, `search.qtRule`, `search.distRule`), which only reads the table and the
step function.

The theorems of `Proofs.lean` use no `native_decide` themselves. Each depends on a few of the checks (for
`types_floor`: `closed_ok` and `types_floor_check`) and on Lean's three standard axioms; `#print axioms` lists them.

The exactness of the two quarter-turn tables rests on `search.qtRule` as a computation (its argument is in
`Search.lean`); that no solution has fewer quarter turns is also proved by induction (`quarter_floors`).

The step function rests on the sticker model through `coords_follow_stickers` and `model_ok`, and the kinds through
`tetrad_theorem`: each tests states within 3 turns of solved, which show every (place, piece, twist) combination,
and what a turn does to a corner depends only on its place.
