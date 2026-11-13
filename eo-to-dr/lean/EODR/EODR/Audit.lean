/- EODR.Audit — which axioms does each theorem depend on?  (Build this file and read the messages.)
   `propext`, `Classical.choice`, `Quot.sound` are Lean's three standard axioms.  An axiom named
   `<theorem>._native.native_decide.ax_…` is what `native_decide` adds for that theorem: "the compiled program
   said true".  The theorems proved by `decide` need no such axiom. -/
import EODR.Model
import EODR.EoTheorems
import EODR.LayoutTheorems
import EODR.EodrTheorems
import EODR.CaseTheorems
namespace EODR
-- A
#print axioms model_size
#print axioms places
#print axioms turns_permute_pieces
#print axioms flip_table
#print axioms keep_fb_eo
#print axioms corner_turns_cyclic
#print axioms coordinates_follow_stickers
-- B
#print axioms eo_table_checked
#print axioms eo_states
#print axioms eo_distance_hist
#print axioms eo_distance_sum
#print axioms eo_mean_digits
#print axioms eo_by_bad
#print axioms eo_solution_counts
#print axioms eo_le5_mean_digits
#print axioms eo_axis_matches_study
-- C
#print axioms badAt_rules
#print axioms arrangements_count
#print axioms layouts_matches_study
#print axioms layout_facts
#print axioms layout_share_digits
-- D
#print axioms eodr_matches_study
#print axioms eodr_states
#print axioms eodr_facts
#print axioms eo0_hist_matches_study
#print axioms eodr_digits
#print axioms twist_counts
-- E
#print axioms case_stats
#print axioms case_digits
#print axioms case_tables_match_page
#print axioms superflip_niss_eo
#print axioms nissy_modulo_bias
#print axioms binomial_digits
end EODR
