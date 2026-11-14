/-
  AttemptSim.SampleThm — checked statements, parts C and E: every attempt of the sample file replays, its time ledger
  adds up, and its result is the shortest solution it had found when its last in-time writing began.  The file is the simulator's own log, embedded byte for byte (data/lean_sample.jsonl; its sha256
  is in data/MANIFEST.txt and in `manifest.FILES`).
-/
import AttemptSim.Sample
import AttemptSim.SampleManifest

namespace AttemptSim
open sample perm

set_option maxHeartbeats 0

/-- The sample is what the generator counted: the embedded files have the manifest's sizes, and there are so many
attempts, and per policy so many attempts, DNFs, moves in all and solutions found (Lean's own reading of the file
against Python's). -/
theorem sample_counts :
    SAMPLE.utf8ByteSize = ((manifest.SAMPLE_FILES.lookup "lean_sample.jsonl").map (·.1)).getD 0 ∧
    PAGE.utf8ByteSize = ((manifest.SAMPLE_FILES.lookup "lean_page_solutions.tsv").map (·.1)).getD 0 ∧
    ATTEMPTS.size = manifest.SAMPLE_ATTEMPTS ∧ tally ATTEMPTS = manifest.SAMPLE_POLICIES ∧
    (ATTEMPTS.toList.map (·.steps.size)).foldl (· + ·) 0 = manifest.SAMPLE_STEPS := by
  native_decide

/-- **Every attempt of the sample passes `attemptOk`**: every solution found and the result solve the scramble in
the stated number of moves (HTM, nothing left to cancel); the step costs add up to the reported time; solutions and
banks sit at the ends of their `tail` and `write` steps; no examination starts after the hour; each bank writes the
shortest solution found before it started; the result is the last bank that ended inside the hour. -/
theorem sample_attempts_ok : ATTEMPTS.all attemptOk = true := by native_decide

/-- **The time ledger.**  For every sampled attempt, the costs of the steps in its log add up to the time it reports
(`t_end_ms`): the clock is nothing but the sum of the states examined, each at its cost. -/
theorem sample_ledger : ∀ a ∈ ATTEMPTS.toList, logTotal a = a.tEnd := by native_decide

/-- **The result is the shortest solution found before the last writing that ended in time began.**  For every
sampled attempt: if no writing ended inside the hour, the result is a DNF (length 0); otherwise the result's length is
the shortest length among the solutions whose finish was written out by the time that writing began.  (Solutions
found later, while writing or after, do not count: the solver had no time left to write them.) -/
theorem sample_result_is_shortest :
    ∀ a ∈ ATTEMPTS.toList,
      (lastInTime a).map (fun j => bestBy a (writeStart a j)) = if a.len = 0 then none else some (some a.len) := by
  native_decide

/-- How many sampled attempts found something shorter than their result (or anything, for a DNF) only after their last
in-time writing began: Lean's count equals the generator's. -/
theorem sample_late_better_count :
    (ATTEMPTS.toList.filter lateBetter).length = manifest.SAMPLE_LATE_BETTER := by native_decide

/-- Spelled out for the results: each attempt with `len > 0` has a solution X with `perm.solved (scramble ++ X)`
(every sticker back home) and |X| = len. -/
theorem sample_results_solve :
    ∀ a ∈ ATTEMPTS.toList, a.len > 0 →
      ∃ S X, a.scramble = some S ∧ a.solution = some X ∧ solved (S ++ X) ∧ X.length = a.len := by
  have h : (ATTEMPTS.toList.all fun a => a.len == 0 ||
      match a.scramble, a.solution with
      | some S, some X => solvedB (S ++ X) && X.length == a.len
      | _, _ => false) = true := by native_decide
  intro a ha hl
  have ha' := List.all_eq_true.mp h a ha
  have hl' : (a.len == 0) = false := by simp; omega
  simp only [hl', Bool.false_or] at ha'
  match hs : a.scramble, hx : a.solution with
  | some S, some X =>
    simp only [hs, hx, Bool.and_eq_true, beq_iff_eq] at ha'
    exact ⟨S, X, rfl, rfl, (solvedB_iff _).mp ha'.1, ha'.2⟩
  | none, _ => simp [hs] at ha'
  | some _, none => simp [hs, hx] at ha'

/-- **Every solution printed on the page** (data/lean_page_solutions.tsv) solves its scramble in the stated number
of moves, in HTM form.  The number of lines is the generator's count. -/
theorem page_solutions_ok : pageOk = true ∧ pageRows.length = manifest.PAGE_SOLUTIONS := by native_decide

end AttemptSim
