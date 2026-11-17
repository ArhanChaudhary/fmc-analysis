# ImpliedEO: Lean 4 proofs for "Implied EOs"

Lean 4.35.0, no Mathlib (only the library that ships with Lean). About 900 lines written by hand and one generated file (`Sets.lean`, from `gen_sets.py`). `lake build` takes under a minute.

EO only depends on edges, so the model is the 24 edge stickers: a sticker spot is the face it is on and the other face of its edge, a quarter turn carries the spots of its layer round, and a scramble is a list of moves. EO on an axis is defined from stickers (each edge has a key sticker, each place a key spot), and `key_keeps` and `key_quarter` show it is the usual notion: quarter turns of the axis flip exactly the four edges they move, every other move flips nothing. An EO with NISS is an axis with normal moves and inverse moves, and `EO.holds X scr` says: the inverse moves undone in front of the scramble, the normal moves after it, and EO is solved.

Every theorem is about all scrambles (all move lists), not a sample.

## What is proved

| File | Theorem | It says |
|---|---|---|
| `Criterion.lean` | `EO.holds_iff` | N (I) is an EO on a scramble exactly when each edge is bad if and only if one of *its place is flipped by N* and *its home place is flipped by I* holds, not both. |
| | `change_axis` | Between two axes an edge changes good/bad exactly when one of its place and its home place, not both, is in the slice across the third axis. |
| | `EO.holds_iff_q` | The same test with torchlight's orientation (the one every quarter turn flips), where no axis is left in the statement. |
| | `EO.implies_iff_same`, `EO.equiv_iff_same` | One EO implies another exactly when they have the same two axis-free cases or both complemented, and then they hold on the same scrambles. The converse builds a scramble that has the first EO and not the second. |
| `Trick.lean` | `trick`, `trick_fb_rl`, `trick_fb_ud`, `trick_rl_fb`, `trick_rl_ud`, `trick_ud_fb`, `trick_ud_rl` | N (I) is an EO on one axis exactly when N G (I G) is an EO on the other, G the two quarter turns of the first axis and then two of the second. |
| | `trick_either_way` | Each of the four moves can be turned either way. |
| | `order_matters`, `wrong_order` | The scramble F U F' has EO on R/L; after F B R L (F B R L) it has EO on no axis; after R L F B (R L F B) it has EO on F/B. |
| | `fbfb`, `fb_fub` | F B (F B) with R L (R L) and U D (U D); F B (F U B) with R L (R U' L). |
| | `fbfb_iff_quarter_turn_orientation`, `good_on_one_or_three` | torchlight's and fabio's descriptions of the F B (F B) scrambles. |
| | `superflip_six`, `superflip_seven` | U D' F (U D' F) with R2 B2 R (R2 B2 R), and R L F (L U R F) with B U D F (B D F): implied, and with complemented cases, so not the trick. |
| `Census.lean` | `mem_layer` | The case of every sequence of k moves is in the computed layer k, so the checks below cover every sequence. |
| | `no_clash` | No EO of at most 5 moves has both cases complemented into an EO of at most 5 moves, on any pair of axes. |
| | `same_cases_of_implies`, `only_the_trick`, `same_axis` | So up to 5 moves an implied EO on another axis solves the same cases as the trick's N G (I G), and on the same axis it is the same EO solved differently. |
| | `cases_by_length`, `census` | 1, 2, 25, 202, 620, 900 EO cases of 0 to 5 moves; 239 shared pairs of cases for each two axes, 13 on all three: 691 sets. |
| `Probe.lean` | `probe`, `probe_fb`, `probe_rl`, `probe_ud` | One side translated, the other side whatever it is: F B (I) on F/B, R L (I F B R L) on R/L and U D (I F B U D) on U/D are EOs on the same scrambles for every I, and the same with normal and inverse swapped. |
| | `flip_rule` | The R/L case of I F B R L is the F/B case of I with the eight places of the U and D layers flipped; for U/D it is the places of the R and L layers. |
| | `ud_du2fu` | U D (D U2 F U), a 6-mover, with F B (F U2 B), a 5-mover. |
| | `probe_census` | The 230 R/L cases of at most 3 moves by their length and the length of the same case seen from F/B: 1, 2, 1, 24, 2, 10, 28, 162. |
| `Sets.lean` | `allSets_equiv` | In each of the 691 sets of the full list, every EO holds on the scrambles the first one holds on. |
| | `probeSets_ok` | Each of the 230 rows *after F B* of the full list: F B (pattern) and R L (case) have the same two cases. |

## Trust

The theorems of `Cube.lean`, `Criterion.lean` and `Trick.lean` are checked by Lean's kernel (`#print axioms` shows `propext` and `Quot.sound` only). Six statements are compiled computations (`native_decide`): `no_clash`, `cases_by_length`, `census`, `probe_census`, `allSets_ok` and `probeSets_ok`; the theorems that use them (`only_the_trick`, `allSets_equiv`, …) inherit that. There is no `sorry`.

Not in Lean: how often (sampled in `research/study.py` and `research/longer.py`), the grouping of the 691 sets into seven kinds, and the counts for longer applied sides and for the superflip in section 5 of the write-up.
