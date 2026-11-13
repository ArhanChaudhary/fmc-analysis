/- DRXs.Audit — which axioms does each theorem depend on?  (Build this file and read the messages.)
   `propext`, `Classical.choice`, `Quot.sound` are Lean's three standard axioms.  An axiom named
   `<theorem>._native.native_decide.ax_…` is what `native_decide` adds for that theorem: "the compiled program
   said true".  The last three theorems need no axiom at all. -/
import DRXs.Theorems
import DRXs.SeoTheorems
import DRXs.Theorems2
import DRXs.EightFeTheorems
namespace DRXs
-- A
#print axioms model_size
#print axioms moves_are_permutations
#print axioms quarter_turn_four_times
#print axioms turns_of_a_face
#print axioms sexy_move_order
#print axioms RU_order
#print axioms order_1260
#print axioms turn_directions
#print axioms moves_agree_with_python
-- B
#print axioms gens_well_formed
#print axioms explore_asserts_hold
#print axioms kinds_count
#print axioms kinds_closed
#print axioms moves_keep_corners_and_edges
#print axioms signature_is_complete_invariant
#print axioms kinds_by_face_axis
#print axioms one_real_dr
#print axioms slices_hist
-- C, D, E
#print axioms dr1s_turns_hist
#print axioms dr1s_turns_le_6
#print axioms dr2s_turns_hist
#print axioms dr3s_turns_hist
#print axioms dr3s_to_2s_hist
#print axioms dr2s_to_1s_hist
#print axioms tables_satisfy_rule
#print axioms to0_is_dmv
-- F
#print axioms seo_skip_counts
#print axioms seo_no_skip
#print axioms seo_configurations
#print axioms seo_share_normal
#print axioms seo_share_both
-- G to K (2026-11-13)
#print axioms eo_reference_free
#print axioms eo_moves
#print axioms slice_eo_rule
#print axioms eo_inverse
#print axioms kinds_of_places
#print axioms seo_skip_average
#print axioms seo_skip_average_digits
#print axioms seo_dist_states
#print axioms seo_dist_hists
#print axioms seo_dist_digits
#print axioms after_trigger_better
#print axioms after_trigger_worse
#print axioms dr1s_layouts
#print axioms simon_count
#print axioms simon13_rows_U
#print axioms simon13_rows_D
#print axioms errata_B1
#print axioms colour2_kinds
#print axioms errata_B2_six
#print axioms errata_B3
#print axioms errata_B3_nissy
#print axioms rename_conjugates
#print axioms rename_is_python_rename
#print axioms eight_fe_is_renamed_dr
#print axioms eight_fe_full_eo
#print axioms eight_fe_mean_digits
end DRXs
