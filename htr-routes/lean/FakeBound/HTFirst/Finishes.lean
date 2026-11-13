/-
  HTFirst.Finishes — every optimal finish of a DR state, enumerated against DRBound's exact table, and the counts
  the reference table "Half turns before the first quarter turn" takes over them.

    desc T d g        the move sequences of length d on which every move lowers the table value by exactly one,
                      starting from g with value d (a search guided by the table, in the order of the moves
                      U U2 U' D D2 D' R2 L2 F2 B2);
    finishes T g      desc T (table value of g) g.

  `mem_finishes` (kernel-checked, from DRBound's `exact_lower` and `exact_attained`): with DRBound's proved table,
  `finishes exactTable g` lists exactly the optimal finishes of g: the sequences w of `exactDist g` moves with
  `g.apply w = solved`.

    lead w            the number of moves before the first quarter turn of w (they are all half turns);
                      99 when w has no quarter turn;        trail w   the same read from the last move;
    summary           the per-state numbers of the study, from the list of optimal finishes.

  `exactTable` is not compiled (building it takes minutes); `HTFirst.Table` runs these functions once on
  `mkTable 18`, the same table.
-/
import HTFirst.Bridge

namespace HTFirst
open DRBound DRBound.Exact HTRRoutes

/-- The ways down the table: d moves, each lowering the table value by exactly one. -/
def desc (T : ByteArray) : Nat → State → List (List Move)
  | 0, _ => [[]]
  | d + 1, g => Move.all.flatMap fun m =>
      if tv T (ridx (g.move m)) = d then (desc T d (g.move m)).map (m :: ·) else []

/-- The optimal finishes of g, read off the table T. -/
def finishes (T : ByteArray) (g : State) : List (List Move) := desc T (tv T (ridx g)) g

/-- Plain arithmetic on variables (`omega` must not see `exactDist`: it would start evaluating the table). -/
theorem sandwich (a b d l l2 : Nat) (h1 : a ≤ l) (hl : l = d) (hd : b = d + 1) (h2 : b ≤ l2 + 1) (hl2 : l2 = a) :
    a = d := by omega

theorem mem_desc : ∀ (d : Nat) (g : State), g.Valid → g.ParityOK → exactDist g = d → ∀ w : List Move,
    (w ∈ desc exactTable d g ↔ (w.length = d ∧ g.apply w = solved))
  | 0, g, hv, hp, hd, w => by
    simp only [desc, List.mem_singleton]
    constructor
    · intro hw
      subst hw
      obtain ⟨w0, hl, hs⟩ := exact_attained g hv hp
      rw [hd] at hl
      have h0 : w0 = [] := List.length_eq_zero_iff.mp hl
      subst h0
      exact ⟨rfl, hs⟩
    · intro h
      exact List.length_eq_zero_iff.mp h.1
  | d + 1, g, hv, hp, hd, w => by
    simp only [desc, List.mem_flatMap]
    constructor
    · intro h
      obtain ⟨m, _, hm⟩ := h
      have hvm := exact_model_checked.valid_move g hv m
      have hpm := exact_model_checked.parityOK_move g hv hp m
      by_cases hc : tv exactTable (ridx (g.move m)) = d
      · rw [if_pos hc] at hm
        obtain ⟨w', hw', hcons⟩ := List.mem_map.mp hm
        subst hcons
        have ih := (mem_desc d (g.move m) hvm hpm hc w').mp hw'
        exact ⟨by rw [List.length_cons, ih.1], ih.2⟩
      · rw [if_neg hc] at hm
        exact absurd hm List.not_mem_nil
    · intro h
      obtain ⟨hl, hs⟩ := h
      match w, hl, hs with
      | [], hl, _ => exact absurd hl (by simp)
      | m :: w', hl, hs =>
        have hl' : w'.length = d := Nat.add_right_cancel hl
        have hs' : (g.move m).apply w' = solved := hs
        have hvm := exact_model_checked.valid_move g hv m
        have hpm := exact_model_checked.parityOK_move g hv hp m
        have h1 := exact_lower (g.move m) hvm hpm w' hs'
        obtain ⟨w2, hl2, hs2⟩ := exact_attained (g.move m) hvm hpm
        have h2 := exact_lower g hv hp (m :: w2) hs2
        rw [List.length_cons] at h2
        have hc : tv exactTable (ridx (g.move m)) = d :=
          sandwich (exactDist (g.move m)) (exactDist g) d w'.length w2.length h1 hl' hd h2 hl2
        refine ⟨m, Move.mem_all m, ?_⟩
        rw [if_pos hc]
        exact List.mem_map.mpr ⟨w', (mem_desc d (g.move m) hvm hpm hc w').mpr ⟨hl', hs'⟩, rfl⟩

/-- **`finishes exactTable g` is the list of all optimal finishes of g**: a sequence of DR moves is in it exactly
when it has `exactDist g` moves (the optimal length, `exact_optimal`) and solves g. -/
theorem mem_finishes (g : State) (hv : g.Valid) (hp : g.ParityOK) (w : List Move) :
    w ∈ finishes exactTable g ↔ (w.length = exactDist g ∧ g.apply w = solved) :=
  mem_desc (exactDist g) g hv hp rfl w

/-! ### The counts over the optimal finishes -/

/-- The number of moves before the first quarter turn (all of them half turns); 99 when there is no quarter turn. -/
def lead : List Move → Nat
  | [] => 99
  | m :: w => if m.isHalf then (if lead w == 99 then 99 else lead w + 1) else 0

/-- The same read from the last move: the half turns after the last quarter turn. -/
def trail (w : List Move) : Nat := lead w.reverse

def minOf (l : List Nat) : Nat := l.foldl min 99

/-- [optimal, optimal finishes, fewest quarter turns among them, most, fewest half turns before the first quarter
turn read from the first move, read from the last move, fewest quarter turns of any finish (`qf`), 1 if some
optimal finish has exactly `qf` quarter turns, and the two half-turn counts over those finishes (99 = none)]. -/
def summary (qf d : Nat) (F : List (List Move)) : List Nat :=
  let E := F.filter fun w => quarterTurns w == qf
  [d, F.length, (F.map quarterTurns).foldl min 99, (F.map quarterTurns).foldl max 0, minOf (F.map lead),
   minOf (F.map trail), qf, if E.isEmpty then 0 else 1, minOf (E.map lead), minOf (E.map trail)]

/-! ### Scrambles -/

/-- DR moves of a string, `none` if any token is not one of the ten. -/
def drMoves? (s : String) : Option (List Move) :=
  ((s.splitOn " ").filter (· != "")).mapM fun t =>
    match t with
    | "U" => some .U | "U2" => some .U2 | "U'" => some .U' | "D" => some .D | "D2" => some .D2 | "D'" => some .D'
    | "R2" => some .R2 | "L2" => some .L2 | "F2" => some .F2 | "B2" => some .B2 | _ => none
def drMoves (s : String) : List Move := (drMoves? s).getD []
def inv : Move → Move
  | .U => .U' | .U' => .U | .D => .D' | .D' => .D | m => m
/-- The DR a scramble makes from solved, and its inverse (the inverse scramble from solved). -/
abbrev st (scr : String) : State := solved.apply (drMoves scr)
abbrev stInv (scr : String) : State := solved.apply ((drMoves scr).reverse.map inv)

/-- The table run: for the states `ex`, the table value and the list of optimal finishes; for the states `rc`,
the summary.  The table is built once. -/
def tableRun (depth : Nat) (ex rc : List State) : List (Nat × List (List Move)) × List (List Nat) :=
  let T := mkTable depth
  (ex.map fun g => (tv T (ridx g), finishes T g),
   rc.map fun g => summary (qtfull.qf (cosetOf g)) (tv T (ridx g)) (finishes T g))

/-- `tableRun 18` is the same thing said with DRBound's `exactTable` and `exactDist`. -/
theorem tableRun_eq (ex rc : List State) :
    tableRun 18 ex rc = (ex.map fun g => (exactDist g, finishes exactTable g),
      rc.map fun g => summary (qtfull.qf (cosetOf g)) (exactDist g) (finishes exactTable g)) := rfl

end HTFirst
