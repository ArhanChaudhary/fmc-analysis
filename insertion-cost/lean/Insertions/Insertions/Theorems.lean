/-
  Insertions.Theorems — the checked statements A to D: what one or two 3-cycles can make, for corners and edges.
  Every statement is closed (no free variable) and about the definitions in LeftoverTypes / Products / AllStates.
  Those marked `native_decide` are proved by running the definitions as compiled code and accepting the answer
  (this trusts the Lean compiler; see README.md); those marked `decide` are plain arithmetic checked by Lean's
  kernel; the two `…_whole_types` theorems are read off two earlier ones by the kernel.

  Reading aid:
    `8 3` after a function name     corners: 8 pieces, twists mod 3;   `12 2`: edges, 12 pieces, flips mod 2
    `∀ g ∈ l, P g`                  P holds for every g in the list l
    a type `[(3, 1), (1, 2)]`       a 3-cycle whose twists add up to 1 and one corner twisted by 2 in place
    `ident 8`                       the solved state
-/
import Insertions.AllStates

namespace Insertions

-- The checks run compiled code; Lean's default time-out for elaborating one statement does not fit them.
set_option maxHeartbeats 0

/-! ## A. The 3-cycles -/

/-- There are 1008 corner 3-cycles in the list, all different.  Each one is a state (a permutation of the 8
corners with twists below 3 that add up to 0) and is a single 3-cycle whose twists add up to 0, with nothing
else moved or twisted (`ctype`).  Each one is not the solved state and g·g·g is, so its order is 3.  Its
inverse is g·g (g·(g·g) and (g·g)·g are both solved), and g·g is in the list again.
(That 1008 is all of them: `corner_type_sizes`, type `[(3, 0)]`.) -/
theorem corner_three_cycles :
    (three_cycles 8 3).length = 1008 ∧ count_distinct (three_cycles 8 3) = 1008 ∧
    ∀ g ∈ three_cycles 8 3,
      is_permutation g.1 8 = true ∧ is_twist g.2 8 3 = true ∧ ctype g 3 = [(3, 0)] ∧
      g ≠ ident 8 ∧ mul (mul g g 3) g 3 = ident 8 ∧ mul g (mul g g 3) 3 = ident 8 ∧
      mul g g 3 ∈ three_cycles 8 3 := by native_decide

/-- The same for edges: 1760 edge 3-cycles, all different, each a state and a single 3-cycle with an even number
of flips and nothing else touched, each of order 3, and the inverse g·g of each is in the list.
(That 1760 is all of them: `edge_type_sizes`, type `[(3, 0)]`.) -/
theorem edge_three_cycles :
    (three_cycles 12 2).length = 1760 ∧ count_distinct (three_cycles 12 2) = 1760 ∧
    ∀ g ∈ three_cycles 12 2,
      is_permutation g.1 12 = true ∧ is_twist g.2 12 2 = true ∧ ctype g 2 = [(3, 0)] ∧
      g ≠ ident 12 ∧ mul (mul g g 2) g 2 = ident 12 ∧ mul g (mul g g 2) 2 = ident 12 ∧
      mul g g 2 ∈ three_cycles 12 2 := by native_decide

/-! ## B. Corners: products of two 3-cycles -/

/-- Multiplying every ordered pair of corner 3-cycles gives 216,511 different states.  The solved state is one
of them and so is each of the 1008 3-cycles.  By type they are: 108,864 5-cycles with twist sum 0; 90,720 pairs
of 3-cycles, each with twist sum 0; 5,040 + 5,040 3-cycles with twist sum 2 (1) plus a corner twisted by 1 (2);
3,780 pairs of swaps with twist sums 2 and 1; 1,890 pairs of swaps with twist sum 0; the 1008 3-cycles;
56 + 56 triples of corners all twisted by 2 (all by 1); 56 pairs of corners twisted by 2 and by 1; the solved
state.  No other type occurs. -/
theorem corner_products_of_two :
    (products_of_two 8 3).length = 216511 ∧ count_distinct (products_of_two 8 3) = 216511 ∧
    count_in [ident 8] (products_of_two 8 3) = 1 ∧
    count_in (three_cycles 8 3) (products_of_two 8 3) = 1008 ∧
    by_type (products_of_two 8 3) 3 =
      [([(5, 0)], 108864), ([(3, 0), (3, 0)], 90720), ([(3, 2), (1, 1)], 5040), ([(3, 1), (1, 2)], 5040),
       ([(2, 2), (2, 1)], 3780), ([(2, 0), (2, 0)], 1890), ([(3, 0)], 1008),
       ([(1, 2), (1, 2), (1, 2)], 56), ([(1, 2), (1, 1)], 56), ([(1, 1), (1, 1), (1, 1)], 56), ([], 1)] := by
  native_decide

/-- What leftover_types.py prints for corners (out/types.json), with its names for the types:
"3c1t" is the two types with 5,040 states together, "3tc" the two with 56. -/
theorem corner_run :
    run "corner" =
      { three_cycles := 1008,
        types := [("3c", 1, 1008), ("5c", 2, 108864), ("3c3c", 2, 90720), ("3c1t", 2, 10080),
                  ("2c2c-twisted", 2, 3780), ("2c2c-pure", 2, 1890), ("3tc", 2, 112), ("2tc", 2, 56)],
        states_within_two := 216511 } := by native_decide

/-! ## C. Corners: what two 3-cycles cannot make, and what they make in full -/

/-- C(1).  No product of two corner 3-cycles is a pair of 3-cycles that both have a twist sum other than 0:
its type is not `[(3, 2), (3, 1)]`, and more generally its type never holds two such 3-cycles, whatever else
it holds. -/
theorem corner_no_two_twisted_3_cycles :
    ∀ s ∈ products_of_two 8 3, ctype s 3 ≠ [(3, 2), (3, 1)] ∧ twisted_cycles (ctype s 3) 3 < 2 := by
  native_decide

/-- C(2).  No product of two corner 3-cycles is two swaps plus a corner twisted in place: its type never holds
two cycles of length 2 together with an entry of length 1. -/
theorem corner_no_two_swaps_with_twist :
    ∀ s ∈ products_of_two 8 3, ¬ (cycles (ctype s 3) 2 = 2 ∧ cycles (ctype s 3) 1 ≥ 1) := by
  native_decide

/-- The two lists that `type_sizes` goes through are complete, for up to 8 pieces and twists mod 2 or 3:
`permutations n` has n! entries, each a permutation of 0 .. n-1, and the entry at position i has `perm_index` i
(so no two are equal); `twists n m` has m^(n-1) entries, each a list of n numbers below m adding up to 0 mod m,
and the entry at position i has `twist_index` i. -/
theorem every_state_once : ∀ n ∈ [1, 2, 3, 4, 5, 6, 7, 8],
    (permutations n).length = fact n ∧
    (∀ p ∈ permutations n, is_permutation p n = true) ∧
    (permutations n).map perm_index = List.range (fact n) ∧
    ∀ m ∈ [2, 3],
      (twists n m).length = m ^ (n - 1) ∧
      (∀ t ∈ twists n m, is_twist t n m = true) ∧
      (twists n m).map (twist_index · m) = List.range (m ^ (n - 1)) := by native_decide

/-- The full size of 33 corner types, counted by going through all 8! x 3^7 = 88,179,840 corner states (every
permutation, every twist vector with total 0) and taking the type of each.  First the 11 types of
`corner_products_of_two` in its order, then the 22 types of `corner_fewest_up_to_three` (ThreeTheorems.lean)
that need three 3-cycles, in its order. -/
theorem corner_type_sizes :
    type_sizes 8 3
      [[(5, 0)], [(3, 0), (3, 0)], [(3, 2), (1, 1)], [(3, 1), (1, 2)], [(2, 2), (2, 1)], [(2, 0), (2, 0)], [(3, 0)],
       [(1, 2), (1, 2), (1, 2)], [(1, 2), (1, 1)], [(1, 1), (1, 1), (1, 1)], [],
       [(7, 0)], [(5, 0), (3, 0)], [(3, 2), (3, 0), (1, 1)], [(3, 1), (3, 0), (1, 2)], [(5, 2), (1, 1)],
       [(5, 1), (1, 2)], [(3, 0), (2, 2), (2, 1)], [(4, 2), (2, 1)], [(4, 1), (2, 2)], [(4, 0), (2, 0)],
       [(3, 2), (3, 1)], [(3, 0), (2, 0), (2, 0)], [(3, 0), (1, 2), (1, 1)], [(2, 2), (2, 0), (1, 1)],
       [(2, 1), (2, 0), (1, 2)], [(3, 2), (1, 2), (1, 2)], [(3, 1), (1, 1), (1, 1)],
       [(3, 0), (1, 2), (1, 2), (1, 2)], [(3, 0), (1, 1), (1, 1), (1, 1)], [(2, 2), (2, 2), (1, 2)],
       [(2, 1), (2, 1), (1, 1)], [(1, 2), (1, 2), (1, 1), (1, 1)]] =
      [108864, 90720, 5040, 5040, 3780, 1890, 1008, 56, 56, 56, 1,
       4199040, 1959552, 362880, 362880, 326592, 326592, 272160, 204120, 204120, 204120, 181440, 136080, 20160,
       15120, 15120, 10080, 10080, 10080, 10080, 7560, 7560, 420] := by native_decide

/-- C(3).  Every state of each type that two corner 3-cycles can make is a product of two 3-cycles: for each
type in the list of `corner_products_of_two`, the number of ALL corner states of that type (`type_sizes`) is the
number of products of that type.  The products are different states, so they are the whole type. -/
theorem corner_two_gives_whole_types :
    type_sizes 8 3 ((by_type (products_of_two 8 3) 3).map (·.1)) = (by_type (products_of_two 8 3) 3).map (·.2) := by
  rw [corner_products_of_two.2.2.2.2]
  exact congrArg (List.take 11) corner_type_sizes

/-- The sizes of the 10 types of `corner_products_of_two` other than the solved state, counted by hand (8 lines:
two pairs of types are mirror images with the same count).  `choose n k` is "n choose k", `fact n` is n!.  A
cycle of length L can be twisted in 3^(L-1) ways once its twist sum is given: L - 1 twists are free and the
last one is forced. -/
theorem corner_type_sizes_by_hand :
    -- a 5-cycle with twist sum 0: which 5 corners, 4! cyclic orders, 3^4 twists
    choose 8 5 * fact 4 * 3 ^ 4 = 108864 ∧
    -- two 3-cycles with twist sum 0: 3 corners and 3 more, in either order (/ 2); each 2 directions, 3^2 twists
    choose 8 3 * choose 5 3 / 2 * (2 * 3 ^ 2) * (2 * 3 ^ 2) = 90720 ∧
    -- a 3-cycle with twist sum 2 (or 1): 3 corners, 2 directions, 3^2 twists; and which of the other 5 is twisted
    choose 8 3 * 2 * 3 ^ 2 * 5 = 5040 ∧
    -- a swap with twist sum 2 and a swap with twist sum 1: 2 corners, 3 twists; 2 of the other 6, 3 twists
    choose 8 2 * 3 * (choose 6 2 * 3) = 3780 ∧
    -- two swaps with twist sum 0: 2 corners and 2 more, in either order (/ 2); 3 twists each
    choose 8 2 * choose 6 2 / 2 * 3 * 3 = 1890 ∧
    -- a 3-cycle with twist sum 0: 3 corners, 2 directions, 3^2 twists
    choose 8 3 * 2 * 3 ^ 2 = 1008 ∧
    -- three corners twisted the same way: which 3 (once for "all by 1", once for "all by 2")
    choose 8 3 = 56 ∧
    -- one corner twisted by 1 and one by 2: which is which
    8 * 7 = 56 := by decide

/-! ## D. Edges: products of two 3-cycles -/

/-- Multiplying every ordered pair of edge 3-cycles gives 925,035 different states.  The solved state is one of
them and so is each of the 1760 3-cycles.  By type they are: 591,360 pairs of unflipped 3-cycles; 304,128
unflipped 5-cycles; 15,840 flipped 3-cycles plus a flipped edge; 5,940 pairs of flipped swaps; 5,940 pairs of
unflipped swaps; the 1760 3-cycles; 66 pairs of flipped edges; the solved state.  No other type occurs (so, for
one, never two flipped 3-cycles). -/
theorem edge_products_of_two :
    (products_of_two 12 2).length = 925035 ∧ count_distinct (products_of_two 12 2) = 925035 ∧
    count_in [ident 12] (products_of_two 12 2) = 1 ∧
    count_in (three_cycles 12 2) (products_of_two 12 2) = 1760 ∧
    by_type (products_of_two 12 2) 2 =
      [([(3, 0), (3, 0)], 591360), ([(5, 0)], 304128), ([(3, 1), (1, 1)], 15840), ([(2, 1), (2, 1)], 5940),
       ([(2, 0), (2, 0)], 5940), ([(3, 0)], 1760), ([(1, 1), (1, 1)], 66), ([], 1)] := by
  native_decide

/-- What leftover_types.py prints for edges (out/types.json), with its names for the types. -/
theorem edge_run :
    run "edge" =
      { three_cycles := 1760,
        types := [("3e", 1, 1760), ("3e3e", 2, 591360), ("5e", 2, 304128), ("3e1f", 2, 15840),
                  ("2e2e", 2, 5940), ("2e2e-flipped", 2, 5940), ("2f", 2, 66)],
        states_within_two := 925035 } := by native_decide

/-- The full size of the 8 edge types of `edge_products_of_two`, in its order.  All 12! x 2^11 edge states are
too many to go through, so each size is (12 choose k) x (the number of states of that type on k places, counted
by going through all states on k places), where k is the number of places the type touches (6, 5, 4, 4, 4, 3,
2, 0). -/
theorem edge_type_sizes :
    [[(3, 0), (3, 0)], [(5, 0)], [(3, 1), (1, 1)], [(2, 1), (2, 1)], [(2, 0), (2, 0)], [(3, 0)], [(1, 1), (1, 1)], []].map
      (type_size_by_places 12 2) = [591360, 304128, 15840, 5940, 5940, 1760, 66, 1] := by native_decide

/-- The shortcut of `edge_type_sizes`, tried where the full count exists: for the corner types of
`corner_type_sizes` it gives the same sizes as going through all 88,179,840 corner states.  (32 of the 33 types;
the one left out, `[(5, 0), (3, 0)]`, touches all 8 places, so for it the shortcut is the full count itself.) -/
theorem corner_type_sizes_by_places :
    [[(5, 0)], [(3, 0), (3, 0)], [(3, 2), (1, 1)], [(3, 1), (1, 2)], [(2, 2), (2, 1)], [(2, 0), (2, 0)], [(3, 0)],
     [(1, 2), (1, 2), (1, 2)], [(1, 2), (1, 1)], [(1, 1), (1, 1), (1, 1)], [],
     [(7, 0)], [(3, 2), (3, 0), (1, 1)], [(3, 1), (3, 0), (1, 2)], [(5, 2), (1, 1)],
     [(5, 1), (1, 2)], [(3, 0), (2, 2), (2, 1)], [(4, 2), (2, 1)], [(4, 1), (2, 2)], [(4, 0), (2, 0)],
     [(3, 2), (3, 1)], [(3, 0), (2, 0), (2, 0)], [(3, 0), (1, 2), (1, 1)], [(2, 2), (2, 0), (1, 1)],
     [(2, 1), (2, 0), (1, 2)], [(3, 2), (1, 2), (1, 2)], [(3, 1), (1, 1), (1, 1)],
     [(3, 0), (1, 2), (1, 2), (1, 2)], [(3, 0), (1, 1), (1, 1), (1, 1)], [(2, 2), (2, 2), (1, 2)],
     [(2, 1), (2, 1), (1, 1)], [(1, 2), (1, 2), (1, 1), (1, 1)]].map (type_size_by_places 8 3) =
      [108864, 90720, 5040, 5040, 3780, 1890, 1008, 56, 56, 56, 1,
       4199040, 362880, 362880, 326592, 326592, 272160, 204120, 204120, 204120, 181440, 136080, 20160,
       15120, 15120, 10080, 10080, 10080, 10080, 7560, 7560, 420] := by native_decide

/-- Every state of each type that two edge 3-cycles can make is a product of two 3-cycles: for each type in the
list of `edge_products_of_two`, the full size of the type (as counted in `edge_type_sizes`) is the number of
products of that type. -/
theorem edge_two_gives_whole_types :
    ((by_type (products_of_two 12 2) 2).map (·.1)).map (type_size_by_places 12 2) =
      (by_type (products_of_two 12 2) 2).map (·.2) := by
  rw [edge_products_of_two.2.2.2.2]
  exact edge_type_sizes

/-- The sizes of the 7 types of `edge_products_of_two` other than the solved state, counted by hand (6 lines:
flipped and unflipped pairs of swaps have the same count).  A cycle of length L can be flipped in 2^(L-1) ways
once its flip sum is given. -/
theorem edge_type_sizes_by_hand :
    -- two unflipped 3-cycles: 3 edges and 3 more, in either order (/ 2); each 2 directions, 2^2 flips
    choose 12 3 * choose 9 3 / 2 * (2 * 2 ^ 2) * (2 * 2 ^ 2) = 591360 ∧
    -- an unflipped 5-cycle: which 5 edges, 4! cyclic orders, 2^4 flips
    choose 12 5 * fact 4 * 2 ^ 4 = 304128 ∧
    -- a flipped 3-cycle and a flipped edge: 3 edges, 2 directions, 2^2 flips; and which of the other 9
    choose 12 3 * 2 * 2 ^ 2 * 9 = 15840 ∧
    -- two flipped swaps (or two unflipped ones): 2 edges and 2 more, in either order (/ 2); 2 flips each
    choose 12 2 * choose 10 2 / 2 * 2 * 2 = 5940 ∧
    -- an unflipped 3-cycle: 3 edges, 2 directions, 2^2 flips
    choose 12 3 * 2 * 2 ^ 2 = 1760 ∧
    -- two flipped edges: which 2
    choose 12 2 = 66 := by decide

end Insertions
