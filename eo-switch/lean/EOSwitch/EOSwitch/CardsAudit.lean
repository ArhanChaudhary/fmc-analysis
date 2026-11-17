/- EOSwitch.CardsAudit — which axioms does each theorem of part G depend on?  (Build this file and read the
   messages.)  As in Audit.lean: `propext`, `Classical.choice`, `Quot.sound` are Lean's three standard axioms, and an
   axiom named `<theorem>._native.native_decide.ax_…` is what `native_decide` adds for that theorem. -/
import EOSwitch.CardsThm
namespace EOSwitch
-- G (CardsThm.lean)
#print axioms cards_table
#print axioms cards_geometry
#print axioms card_reads_match_study
#print axioms dfbr_cases
#print axioms drm_totals_match_study
#print axioms cards_ref_shape
#print axioms card_4c4e_matches_study
#print axioms policies_4c4e_matches_study
#print axioms card_4c2e_matches_study
#print axioms policies_4c2e_matches_study
#print axioms card_3c2e_matches_study
#print axioms policies_3c2e_matches_study
#print axioms card_7c8e_matches_study
#print axioms policies_7c8e_matches_study
#print axioms card_8c8e_matches_study
#print axioms policies_8c8e_matches_study
#print axioms card_2c2e_matches_study
#print axioms policies_2c2e_matches_study
#print axioms card_4c6e_matches_study
#print axioms policies_4c6e_matches_study
#print axioms card_3c4e_matches_study
#print axioms policies_3c4e_matches_study
#print axioms card_3c6e_matches_study
#print axioms policies_3c6e_matches_study
#print axioms card_5c4e_matches_study
#print axioms policies_5c4e_matches_study
#print axioms card_5c6e_matches_study
#print axioms policies_5c6e_matches_study
#print axioms card_6c6e_matches_study
#print axioms policies_6c6e_matches_study
#print axioms card_headline
end EOSwitch
