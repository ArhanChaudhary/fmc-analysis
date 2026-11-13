import Insertions.Ten
/-
  The algs of 10 moves or fewer (corners), and the cap-10 parts of the printed examples.  See `Ten.lean`.
-/
namespace Insertions
namespace ins
open cube

/-- Every corner-only alg of at most 10 moves, by what it does (type, length of the shortest alg, number of
states) and by length (type, length, number of sequences), and the examples.

Counts.  Corner 3-cycles: 528 have an 8-mover, 336 more a 9-mover, 80 more a 10-mover (864, 1,728 and 11,856
sequences).  A pure 2c2c `[(2, 0), (2, 0)]`: 132 states have a 10-mover and none has anything shorter.  10 moves
also do 1,152 5-cycles and 704 pairs of 3-cycles.  Nothing of 10 moves or fewer does a twisted 2c2c, a 3c1t, two or
three corners twisted in place: the only other types are a 4-cycle with a swap (from 9 moves), four swaps and two
4-cycles, which take three comms.

Examples (lengths of the best result; 0 = nothing fits).
`b`  [b]: 26 with 8-movers, 26 with algs up to 9, 25 with algs up to 10.
`i`  [i]: 28 with 8-movers, 27 with algs up to 10.
`k8`, `kShort`, `kTen`  [k]: the best 8-mover result at each spot 0 … 20: 25 at spot 10 only; the walk 0, 2, 4, 6,
     8, 11, 13, 15, 17, 19, 20 sees at best 27; the cases at spots 0, 2, 4, 6 have an 8-mover and the case at spot 8
     nothing shorter than 10; the printed 10-mover does what spot 8 needs.
`h`  [h]: 30 with algs up to 10.
`n8`, `n8Short`  the 20-move 3c with no 8-mover (6.1): 28 with algs up to 10; the shortest alg for the case at
     each spot (0 = more than 10), as printed.
`p`  the 23-move 3c of 9.5: 27 with 8-movers, 23 with algs up to 10. -/
theorem ten_facts : tenFacts () =
    { states := [([(3, 0)], 8, 528), ([(3, 0)], 9, 336), ([(4, 0), (2, 0)], 9, 24),
                 ([(2, 0), (2, 0), (2, 0), (2, 0)], 10, 3), ([(2, 0), (2, 0)], 10, 132), ([(3, 0), (3, 0)], 10, 704),
                 ([(3, 0)], 10, 80), ([(4, 0), (2, 0)], 10, 432), ([(4, 0), (4, 0)], 10, 18), ([(5, 0)], 10, 1152)],
      sequences := [([(3, 0)], 8, 864), ([(3, 0)], 9, 1728), ([(4, 0), (2, 0)], 9, 48),
                    ([(2, 0), (2, 0), (2, 0), (2, 0)], 10, 456), ([(2, 0), (2, 0)], 10, 1296),
                    ([(3, 0), (3, 0)], 10, 3480), ([(3, 0)], 10, 11856), ([(4, 0), (2, 0)], 10, 576),
                    ([(4, 0), (4, 0)], 10, 336), ([(5, 0)], 10, 1680)],
      b := [26, 26, 25],
      i := [28, 27],
      k8 := [27, 28, 27, 27, 28, 27, 28, 28, 0, 28, 25, 28, 28, 28, 28, 27, 0, 0, 0, 0, 0],
      kShort := [8, 8, 8, 8, 10],
      kTen := true,
      h := 30,
      n8 := 28,
      n8Short := [9, 0, 0, 0, 0, 10, 10, 9, 9, 0, 0, 9, 9, 9, 0, 0, 0, 9, 9, 9, 9],
      p := [27, 23] } := by native_decide

/-- The blocks of those examples replay as printed ([b], [i], [k], the 23-move 3c of 9.5: leftover, comm,
cancel, length after, solution), and the 22-move solution found by hand on the last one solves its scramble. -/
theorem ten_blocks_replay :
    checkBlock B_scramble B_block8 "UBL → DBR → UFL → UBL" ∧ checkBlock B_scramble B_block10 "UBL → DBR → UFL → UBL" ∧
    checkBlock I_scramble I_block8 "DBR → UBR → DFR → DBR" ∧ checkBlock I_scramble I_block10 "DBR → UBR → DFR → DBR" ∧
    checkBlock K_scramble K_block "DFR → UBR → UFR → DFR" ∧
    checkBlock P_scramble P_block8 "DBL → UBL → DFR → DBL" ∧ checkBlock P_scramble P_block10 "DBL → UBL → DFR → DBL" ∧
    stateOf (word P_scramble ++ word P_hand) = SOLVED ∧ (word P_hand).length = 22 ∧
    (normal (word P_hand)).length = 22 := by native_decide

end ins
end Insertions
