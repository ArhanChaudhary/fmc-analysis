/- FakeBound.Audit — the axioms each theorem rests on.  Parts 1 (Finish, Formula, Counter) use only Lean's
   standard axioms (no `native_decide`); Part 2 (Subset) adds one `native_decide` axiom per check. -/
import FakeBound.Finish
import FakeBound.Formula
import FakeBound.Counter
import FakeBound.Subset
namespace FakeBound
#print axioms cover_sum
#print axioms chain_bound
#print axioms term1_sound
#print axioms term2_sound
#print axioms term3_sound
#print axioms term4_sound
#print axioms term5_sound
#print axioms lower_stupid
#print axioms lower_free
#print axioms lower_A
#print axioms lower_B
#print axioms lower_C
#print axioms Rmin_sound
#print axioms Rmax_sound
#print axioms printed_term2_fails
#print axioms printed_term2_fails_any_ABC
#print axioms printed_term2_fails_small
#print axioms alpha_i_fails
#print axioms alpha_i_fails_any_ABC
#print axioms C_placement
#print axioms witness_0c3
#print axioms literal_min_fails
#print axioms Rmin_not_tight
#print axioms half_turns_keep_subset_data
#print axioms labels_keep
#print axioms fake_C_examples
#print axioms counter_alphas
end FakeBound
