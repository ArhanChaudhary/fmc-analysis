/- Insertions.Audit — which axioms does each theorem depend on?  (Build this file and read the messages.)
   `propext`, `Classical.choice`, `Quot.sound` are Lean's three standard axioms.  An axiom named
   `<theorem>._native.native_decide.ax_…` is what `native_decide` adds for that theorem: "the compiled program
   said true".  A theorem that lists another theorem's axiom was read off that theorem by the kernel. -/
import Insertions.Theorems
import Insertions.ThreeTheorems
import Insertions.FirstCommsTheorem
import Insertions.ErrataTheorems
import Insertions.WitnessTheorems
import Insertions.TenTheorems
namespace Insertions
-- A
#print axioms corner_three_cycles
#print axioms edge_three_cycles
-- B
#print axioms corner_products_of_two
#print axioms corner_run
-- C
#print axioms corner_no_two_twisted_3_cycles
#print axioms corner_no_two_swaps_with_twist
#print axioms every_state_once
#print axioms corner_type_sizes
#print axioms corner_two_gives_whole_types
#print axioms corner_type_sizes_by_hand
-- D
#print axioms edge_products_of_two
#print axioms edge_run
#print axioms edge_type_sizes
#print axioms corner_type_sizes_by_places
#print axioms edge_two_gives_whole_types
#print axioms edge_type_sizes_by_hand
-- E
#print axioms corner_fewest_up_to_three
#print axioms corner_three_totals
#print axioms corner_three_gives_whole_types
-- F (first comms per spot)
#print axioms first_comms_per_spot
-- G (sticker cube, algs of 8 moves or fewer, the printed examples)
#print axioms ins.moves_agree_with_python
#print axioms ins.corner_algs_up_to_8
#print axioms ins.A1_blocks_replay
#print axioms ins.A1_best_two
#print axioms ins.A2_example
#print axioms ins.A2_pair_swapped
#print axioms ins.A3_example
#print axioms ins.example_d_negative
#print axioms ins.example_e_nested
#print axioms ins.example_j_third
#print axioms ins.examples_no_8_mover
#print axioms ins.corner_counts
#print axioms ins.jay_oriented_8_mover
#print axioms ins.edge_counts
-- H (algs of 10 moves or fewer, cap-10 examples)
#print axioms ins.ten_facts
#print axioms ins.ten_blocks_replay
end Insertions
