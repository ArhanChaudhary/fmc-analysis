/- EOSwitch.Audit — which axioms does each theorem depend on?  (Build this file and read the messages.)
   `propext`, `Classical.choice`, `Quot.sound` are Lean's three standard axioms.  An axiom named
   `<theorem>._native.native_decide.ax_…` is what `native_decide` adds for that theorem: "the compiled program
   said true".  The theorems proved by `decide` need no such axiom. -/
import EOSwitch.Model
import EOSwitch.Theorems
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
end EOSwitch
