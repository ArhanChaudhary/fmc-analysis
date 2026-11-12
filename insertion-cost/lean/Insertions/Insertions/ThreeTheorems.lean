/-
  Insertions.ThreeTheorems — statement E: the corner types that need exactly three 3-cycles.

  `corner_fewest_up_to_three` is the one long run (217 million products, between one and two minutes of compiled
  code on a quiet machine, accepted through `native_decide`).  The statements after it are read off from it by
  the kernel, without running again.  **Editing this file, Three.lean or anything they import, comments
  included, repeats the run.**
-/
import Insertions.Three
import Insertions.Theorems

namespace Insertions

-- The run takes longer than Lean's default time-out for elaborating one statement.
set_option maxHeartbeats 0

/-- E.  Multiplying the solved corner state by every 3-cycle, three times over: each row is (k, type, number of
states of that type that are a product of k 3-cycles and of no fewer).  k = 0 is the solved state, k = 1 the
1008 3-cycles, k = 2 the nine types of `corner_products_of_two` with the same numbers, and k = 3 gives 22 types:
7-cycles; a 5-cycle and a 3-cycle; a 5-cycle with twist sum 1 or 2 and a twisted corner; a 4-cycle and a swap
(twist sums 0 0, 2 1 or 1 2); two 3-cycles that both have a twist sum (2 and 1), the type two 3-cycles cannot
make; a 3-cycle and two swaps; two swaps and a twisted corner, the other type two 3-cycles cannot make; and so
on down to four twisted corners, two each way. -/
theorem corner_fewest_up_to_three :
    fewest_by_type 8 3 3 =
      [(0, [], 1),
       (1, [(3, 0)], 1008),
       (2, [(5, 0)], 108864), (2, [(3, 0), (3, 0)], 90720), (2, [(3, 2), (1, 1)], 5040), (2, [(3, 1), (1, 2)], 5040),
       (2, [(2, 2), (2, 1)], 3780), (2, [(2, 0), (2, 0)], 1890), (2, [(1, 2), (1, 2), (1, 2)], 56),
       (2, [(1, 2), (1, 1)], 56), (2, [(1, 1), (1, 1), (1, 1)], 56),
       (3, [(7, 0)], 4199040), (3, [(5, 0), (3, 0)], 1959552), (3, [(3, 2), (3, 0), (1, 1)], 362880),
       (3, [(3, 1), (3, 0), (1, 2)], 362880), (3, [(5, 2), (1, 1)], 326592), (3, [(5, 1), (1, 2)], 326592),
       (3, [(3, 0), (2, 2), (2, 1)], 272160), (3, [(4, 2), (2, 1)], 204120), (3, [(4, 1), (2, 2)], 204120),
       (3, [(4, 0), (2, 0)], 204120), (3, [(3, 2), (3, 1)], 181440), (3, [(3, 0), (2, 0), (2, 0)], 136080),
       (3, [(3, 0), (1, 2), (1, 1)], 20160), (3, [(2, 2), (2, 0), (1, 1)], 15120),
       (3, [(2, 1), (2, 0), (1, 2)], 15120), (3, [(3, 2), (1, 2), (1, 2)], 10080),
       (3, [(3, 1), (1, 1), (1, 1)], 10080), (3, [(3, 0), (1, 2), (1, 2), (1, 2)], 10080),
       (3, [(3, 0), (1, 1), (1, 1), (1, 1)], 10080), (3, [(2, 2), (2, 2), (1, 2)], 7560),
       (3, [(2, 1), (2, 1), (1, 1)], 7560), (3, [(1, 2), (1, 2), (1, 1), (1, 1)], 420)] := by
  native_decide

/-- So 22 corner types need exactly three 3-cycles, 8,845,836 states in all, and 9,062,347 corner states are a
product of at most three 3-cycles (of the 8! x 3^7 / 2 = 44,089,920 that 3-cycles can reach at all).
`rows_at 3` picks the rows with k = 3 as (type, number of states). -/
theorem corner_three_totals :
    (rows_at 3 (fewest_by_type 8 3 3)).length = 22 ∧
    ((rows_at 3 (fewest_by_type 8 3 3)).map (·.2)).sum = 8845836 ∧
    ((fewest_by_type 8 3 3).map (·.2.2)).sum = 9062347 ∧ fact 8 * 3 ^ 7 / 2 = 44089920 := by
  rw [corner_fewest_up_to_three]
  decide

/-- Every state of each of the 22 types needs exactly three 3-cycles: the number of ALL corner states of the type
(`corner_type_sizes`) is the number found at k = 3. -/
theorem corner_three_gives_whole_types :
    type_sizes 8 3 ((rows_at 3 (fewest_by_type 8 3 3)).map (·.1)) =
      (rows_at 3 (fewest_by_type 8 3 3)).map (·.2) := by
  rw [corner_fewest_up_to_three]
  exact congrArg (List.drop 11) corner_type_sizes

end Insertions
