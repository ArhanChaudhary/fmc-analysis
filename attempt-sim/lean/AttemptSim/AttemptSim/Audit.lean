/-
  AttemptSim.Audit — the axioms behind every theorem of the certificate.  Expected: `propext`, `Classical.choice`,
  `Quot.sound` (Lean's standard axioms) and, for each `native_decide`, one `…._native…` axiom standing for "this Boolean
  computation, compiled and run, returned true" (`Lean.ofReduceBool`).  No `sorryAx` may appear.
-/
import AttemptSim.ModelThm
import AttemptSim.TablesThm
import AttemptSim.SampleThm
import AttemptSim.CompleteThm
import AttemptSim.DRLink

open AttemptSim

-- Perm.lean: sequences as permutations, NISS, cancel (kernel proofs over all sequences, finite facts by native_decide)
#print axioms perm.run_append
#print axioms perm.tabOk
#print axioms perm.invOk
#print axioms perm.mv_inv
#print axioms perm.mv_inv'
#print axioms perm.invert_cons
#print axioms perm.run_invert
#print axioms perm.run_invert'
#print axioms perm.solved_rotate
#print axioms perm.niss_convention
#print axioms perm.solvedB_iff
#print axioms perm.mergeOk
#print axioms perm.pushBack_run
#print axioms perm.push_run
#print axioms perm.foldl_push_run
#print axioms perm.cancel_run
#print axioms perm.cancel_solves
#print axioms perm.written_solution
-- ModelThm.lean: the simulator's model is the sticker cube
#print axioms sticker_model
#print axioms turn_directions
#print axioms model_shape
#print axioms moves_match
#print axioms cubie_follows_stickers
#print axioms then_inverse_follow
#print axioms compose_is_concatenation
#print axioms run_is_apply
#print axioms rotations_match
#print axioms conj_follows
#print axioms views_ok
#print axioms views_read_axes
#print axioms dr_numbering
#print axioms cancel_shape
-- TablesThm.lean: the tables the search trusts
#print axioms move_tables_match
#print axioms coords_follow
#print axioms coords_are_stickers
#print axioms eodist_checked
#print axioms drdist_checked
#print axioms dr_group
#print axioms cosets_ok
#print axioms htrdist_checked
-- DRLink.lean: the DR moves are judging-a-dr's
#print axioms drlink.dr_moves_are_drbound
#print axioms drlink.dr_sequences_follow_drbound
#print axioms drlink.sticker_dr_moves_are_drbound
-- SampleThm.lean: the sampled attempts
#print axioms sample_counts
#print axioms sample_attempts_ok
#print axioms sample_ledger
#print axioms sample_result_is_shortest
#print axioms sample_late_better_count
#print axioms sample_results_solve
#print axioms page_solutions_ok
-- CompleteThm.lean: the candidate lists are complete
#print axioms fast_tests_agree
#print axioms candidate_files
#print axioms eo_candidates_complete
#print axioms eo_candidates_are_eos
#print axioms dr_candidates_complete
#print axioms dr_candidates_are_drs
