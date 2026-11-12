/-
  FakeBound.Subset — the cube facts the abstraction uses, checked on HTRRoutes' sticker model.

  Hypothesis C ≤ L - s_0 - s_N (FakeBound.Finish) says: the middle block Q_1 s_1 … s_{N-1} Q_N of a finish of a DR
  state X is a linear HTR of a DR state in X's HTR subset.  The middle block solves Y = s_N · X · s_0 (the
  half-turn sequence s_N done before X, s_0 after), and a sequence that solves Y is in particular a linear HTR of
  Y.  So what is needed is that half-turn pre-moves and post-moves keep a DR state's HTR subset, with its bad-edge
  count: Mallard's 48-subset name (`cosets.label48`, "4c3 2e") and the 14-name label (`cosets.label`, "4a3 2e").

  In HTRRoutes' model a DR state's arrangements multiply as `amul` (sequence a, then sequence b: `amul a b`).
  A pre-move h gives `amul H a`, a post-move `amul a H`, for corners (CMOV) and U/D edges (EMOV) alike.
  The checks run over all 40,320 corner arrangements and all 40,320 U/D-edge arrangements, for each of the six half
  turns, on both sides.  Since every half-turn sequence is a product of single half turns, the invariance for
  sequences follows by induction (`labels_keep`, stated for single moves; sequences are iterates).
-/
import HTRRoutes

namespace FakeBound
open HTRRoutes HTRRoutes.pieces HTRRoutes.corners

set_option maxHeartbeats 0

/-- Pre-move m on corner rank r: rank of (m, then r). -/
def preC (r m : Nat) : Nat := rank (amul CMOV[m]! ARR[r]!)

/-- Corners: a half turn before or after keeps the bad-corner count, the qt count, the a/b shape and the 14-name
subset. -/
def cornersKeep : Bool :=
  (List.range NC).all fun r => HALF.all fun m =>
    let p := preC r m
    let q := step r m
    NBAD[p]! == NBAD[r]! && qt p == qt r && SHAPEA[p]! == SHAPEA[r]! && sub p == sub r &&
    NBAD[q]! == NBAD[r]! && qt q == qt r && SHAPEA[q]! == SHAPEA[r]! && sub q == sub r &&
    q == rank (amul ARR[r]! CMOV[m]!)

/-- The 70 edge patterns of a DR state (4 of the 8 U/D-edge places hold M pieces). -/
def MASKS : List Nat := (List.range 256).filter fun x => (List.range 8).countP (fun k => (x >>> k) % 2 == 1) == 4

/-- U/D edges: a half turn before keeps the edge pattern (the set of places holding M pieces) itself; a half turn
after moves it by `maskMv` and keeps the bad-edge count; every pattern is one of the 70. -/
def edgesKeep : Bool :=
  (List.range NC).all fun k => HALF.all fun m =>
    let e := unrank 8 k
    MASKS.contains (mMask e) &&
    mMask (amul EMOV[m]! e) == mMask e &&
    mMask (amul e EMOV[m]!) == maskMv EMOV[m]! (mMask e) &&
    ebad (mMask (amul e EMOV[m]!)) == ebad (mMask e)

/-- The names themselves: for every corner rank, half turn and edge pattern, the 48-subset name and the 14-name
label of (m, then the state) and of (the state, then m) are those of the state. -/
def labelsKeep : Bool :=
  (List.range NC).all fun r => HALF.all fun m => MASKS.all fun mask =>
    cosets.label48 (preC r m) mask == cosets.label48 r mask &&
    cosets.label (preC r m) mask == cosets.label r mask &&
    cosets.label48 (step r m) (maskMv EMOV[m]! mask) == cosets.label48 r mask &&
    cosets.label (step r m) (maskMv EMOV[m]! mask) == cosets.label r mask

/-- **Checked on the cube**: for every corner arrangement, every U/D-edge arrangement and every half turn
(U2 D2 R2 L2 F2 B2), on either side, the corner data (bad corners, qt count, a/b shape, 14-name subset), the
bad-edge count, and the two subset names do not change. -/
theorem half_turns_keep_subset_data : cornersKeep = true ∧ edgesKeep = true ∧ labelsKeep = true := by
  native_decide

/-- **Half-turn pre- and post-moves keep the HTR subset with its bad edges.**  For every corner rank r < 40,320,
every U/D-edge arrangement e (rank k < 40,320) and every half turn m: the state "m then (r, e)" and the state
"(r, e) then m" have the same 48-subset name and the same 14-name label as (r, e).  Hence so does
s_N · X · s_0 for half-turn sequences s_N, s_0 (apply this move by move), and the middle block of a finish is a
linear HTR of a state in X's subset: C (the subset's shortest linear HTR) ≤ L - s_0 - s_N. -/
theorem labels_keep : ∀ r, r < NC → ∀ k, k < NC → ∀ m ∈ HALF,
    cosets.label48 (preC r m) (mMask (amul EMOV[m]! (unrank 8 k))) = cosets.label48 r (mMask (unrank 8 k)) ∧
    cosets.label48 (step r m) (mMask (amul (unrank 8 k) EMOV[m]!)) = cosets.label48 r (mMask (unrank 8 k)) ∧
    cosets.label (preC r m) (mMask (amul EMOV[m]! (unrank 8 k))) = cosets.label r (mMask (unrank 8 k)) ∧
    cosets.label (step r m) (mMask (amul (unrank 8 k) EMOV[m]!)) = cosets.label r (mMask (unrank 8 k)) := by
  intro r hr k hk m hm
  obtain ⟨_, he, hl⟩ := half_turns_keep_subset_data
  simp only [edgesKeep, labelsKeep, List.all_eq_true, List.mem_range, Bool.and_eq_true, beq_iff_eq] at he hl
  obtain ⟨⟨⟨hmem, e1⟩, e2⟩, _⟩ := he k hk m hm
  have hmem' : mMask (unrank 8 k) ∈ MASKS := by simpa using hmem
  obtain ⟨⟨⟨l1, l2⟩, l3⟩, l4⟩ := hl r hr m hm _ hmem'
  rw [e1, e2]
  exact ⟨l1, l3, l2, l4⟩

/-- FakeMMAP's examples of C (T11501: "so 2c3 2e would have C=5, 4b2 0e would have C=6"): in Lean's table of the
shortest linear HTR of every HTR coset (`htr48_matches_study`), the minimum over the cosets named 2c3 2e is 5 and
over 4b2 0e is 6. -/
theorem fake_C_examples :
    let shortest := fun (s : String) => ((cosets.run.table.filter (·.1 == s)).map (·.2.1)).foldl min 99
    shortest "2c3 2e" = 5 ∧ shortest "4b2 0e" = 6 := by native_decide

/-- α of the two corner paths used in FakeBound.Counter, computed from the cube as in HTRRoutes. -/
theorem counter_alphas :
    alphaOf HT (parsePath "4a1 > 0c0 > 4a1 > 0c0") = ([0, 0, 0, 0], true) ∧
    alphaOf HT (parsePath "4b2 > 4a3 > 4b2 > 4a1 > 0c0") = ([0, 0, 3, 1, 0], true) := by native_decide

end FakeBound
