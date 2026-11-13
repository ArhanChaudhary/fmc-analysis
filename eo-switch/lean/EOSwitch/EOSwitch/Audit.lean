/- EOSwitch.Audit — which axioms does each theorem depend on?  (Build this file and read the messages.)
   `propext`, `Classical.choice`, `Quot.sound` are Lean's three standard axioms.  An axiom named
   `<theorem>._native.native_decide.ax_…` is what `native_decide` adds for that theorem: "the compiled program
   said true".  The theorems proved by `decide` need no such axiom. -/
import EOSwitch.Model
import EOSwitch.Theorems
import EOSwitch.Recount
import EOSwitch.RingsThm
namespace EOSwitch
-- A
#print axioms model_size
#print axioms places
#print axioms keep_fb_eo
#print axioms turns_permute_pieces
#print axioms coordinates_follow_stickers
#print axioms feature_places
#print axioms feature_examples
-- B
#print axioms dist_checked
#print axioms dist_hist
#print axioms dist_mean_digits
#print axioms drm_stats
-- C
#print axioms cells_4c4e_edges_paired
#print axioms cells_4c4e_edges_paired_same_slice
#print axioms cells_4c4e_pairs_edges_paired
#print axioms cells_4c2e_pairs_plus_half_side
#print axioms cells_7c8e_pairs
#print axioms cells_2c2e_edges_paired_jzp
#print axioms cells_3c2e
#print axioms headline_digits
-- D
#print axioms dist_matches_study
#print axioms variants_match_study
#print axioms summary_tables_match_study
#print axioms summary_2c2e_mean
-- E (Recount.lean)
#print axioms full_table
#print axioms corner_case_your_call
#print axioms errata_b_3qt
#print axioms errata_c_stacked
#print axioms corner_case_claims
#print axioms arm_4c4e
#print axioms paired_edge_arm_4c4e
#print axioms pairs4_7c8e
#print axioms bars_by_arm
#print axioms strict_separation
#print axioms rule_cards
#print axioms low_drm_pairs
#print axioms graded_rules
#print axioms last_turn_4c4e
#print axioms inverse_option
#print axioms example_labels
#print axioms coset_of_relabel
#print axioms rzp_last_turn
-- F (RingsThm.lean)
#print axioms ring_places
#print axioms compact_states
#print axioms ring_turns
#print axioms ring_faithful
#print axioms ring_records
#print axioms side_turns
#print axioms side_turns_certain
#print axioms side_turns_by_drm
#print axioms profiles_by_drm
#print axioms cross_by_drm
#print axioms ring_swaps_checked
#print axioms half_turns_to_bars
#print axioms bands_4c4e
#print axioms swaps_slot_4c4e
#print axioms pairs_bands_4c4e
#print axioms card_split_4c4e
#print axioms inside3_4c4e
#print axioms pair_change
#print axioms three_pair_rule
#print axioms patterns_le2
end EOSwitch
