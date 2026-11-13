/- HTRRoutes.Audit — which axioms does each theorem depend on?  (Build this file and read the messages.)
   `propext`, `Classical.choice`, `Quot.sound` are Lean's three standard axioms.  An axiom named
   `<theorem>._native.native_decide.ax_…` is what `native_decide` adds for that theorem: "the compiled program
   said true".  The theorems proved by `decide` need no such axiom. -/
import HTRRoutes.Model
import HTRRoutes.HtrTheorems
import HTRRoutes.CornerTheorems
import HTRRoutes.CosetTheorems
import HTRRoutes.QtCosetTheorems
import HTRRoutes.QtFullTheorems
namespace HTRRoutes
-- A
#print axioms model_size
#print axioms places
#print axioms dr_keeps_axes
#print axioms arrangements_follow_stickers
#print axioms half_turns_keep_parts
#print axioms ranks
-- B
#print axioms htr_coordinate_ok
#print axioms htr_group_matches_study
#print axioms htr_hist
#print axioms htr_parts
#print axioms htr_mean_digits
-- C
#print axioms htr_corners
#print axioms qt_checked
#print axioms subsets_well_defined
#print axioms subset_table
#print axioms inverse_subsets
#print axioms fake_htr
#print axioms fake_htr_as_study
#print axioms bare_quarter_turns
#print axioms bare_quarter_turns_as_study
#print axioms ht_checked
#print axioms alpha_example
#print axioms alpha_matches_study
-- D
#print axioms htr48_matches_study
#print axioms htr48_facts
#print axioms name_map_matches_study
#print axioms two_qt_letters
-- E
#print axioms qt1_is_4a1_4e
#print axioms qt2_cosets
-- F
#print axioms qt_full_checked
#print axioms qf_is_fewest
#print axioms qf_steps
#print axioms no_extra_every_qt_lowers
#print axioms floor_and_rule_one
#print axioms qf_values
#print axioms qf_by_row
#print axioms ready_by_subset
#print axioms lowering_turns
end HTRRoutes
