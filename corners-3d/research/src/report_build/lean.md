The certificate is in `lean/Corners3D` of the repository (Lean 4, no Mathlib; it builds in about two minutes). It redoes everything from a 54-sticker model of the cube, so no table of this page is taken on trust.

Proved by induction, for every sequence of turns:

- `floor_of_check`: the general floor argument of 6.1. `types_floor`, `parity_floor`, `placement_floor` and `weight_floor` are the floors of sections 6.2, 6.5 and 4.3, and `quarter_floors` the ones in quarter turns.
- `same_kinds_stay_same` and `types_solution_hits_every_good_state`: the 1 in 6 of section 5.2. If a sequence makes a state all good, every all-good state is hit by exactly one of the states with the same types.
- `htr_iff`: the test for HTR of section 5.3.
- `dHTR_exact`: the distance table is exact, so are the two floor tables.

Checked over all {= n(N) =} states by running a compiled check (`native_decide`):

- `tetrad_theorem` and `quarter_rule`: the six types and the rule of section 4, with the table of 4.2 as `rule_table`.
- `dHTR_hist`, `qHTR_hist`: the two tables of section 3. `fake_htr_far`: every fake HTR is 9 turns away.
- `three_reads_fix_distance`, `types_and_two_colours_fix_state`, `types_class_size`: section 5.4.
- `floor_gaps`, `quarter_floor_gaps`, `qt_surcharge`: how far the floors are below the truth, and what the twist costs.
- `dr_qt_same`, `dr_turns_saved`, `placement_qt_same_on_three_axes`: section 9.1 and 9.2, and beef beans' count on three axes.
- `Pages.lean`: all 305 scrambles these pages print, each with its types line, moves, quarter turns, both floors and the printed solution.

Not in Lean: the distances with NISS, the *best rule* tables of section 7, the count table's rows (they're minima over the certified distance table, taken in Python), and the search over all eight corners behind the errata. Those are the Python and Rust searches of the repository, and every scramble they print is replayed on a second sticker model.
