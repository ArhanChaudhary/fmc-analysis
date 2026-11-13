/-
  HTRRoutes.QtFull — F: the fewest quarter turns of a finish, on the 29,400 HTR cosets, and what a quarter turn
  can do to it.  (The reference table "Half turns before the first quarter turn": its "no extra quarter turn",
  "ready" and the floor under rule 1.)

  On the HTR cosets of `Cosets.lean` (x = corner coset · 256 + edge pattern; moves act on the right, `qtcos.st`):

    qf x      the fewest quarter turns of any DR move sequence taking x to the HTR coset (half turns are free);
              computed by a layered search (`qfCompute`), not trusted: see the checks below.
    cq x      the corners' count: the qt count of the corner coset (`corners.qt`, the number in the subset's name).
    ready x   some U or D quarter turn lowers the corners' count by one, right away.
    sC x      the corners' setup count: the fewest half turns before some quarter turn lowers the corners' count
              (255 when the count is 0).  sF x: the same for qf (only used as a certificate).

  The checks (`chkStep` … `chkSetup`) are plain "for every coset, for every move" statements over the tables; they
  are run by `native_decide` in `QtFullTheorems.lean`.  Everything else in this file is proved from "the checks
  hold" (`Checked`) by Lean's kernel, for every coset and every move sequence:

    qf_lower        a sequence from x into HTR has at least qf x quarter turns;
    qf_attained     some sequence from x into HTR has exactly qf x;
    qf_half         a half turn keeps qf;       qf_quarter   a quarter turn changes it by exactly one;
    tight_lowers    on a sequence into HTR with exactly qf x quarter turns, every quarter turn lowers qf by one;
    floor           if qf x = cq x, such a sequence makes at least sC x half turns before its first quarter turn;
    rule_one        if qf x = cq x and such a sequence starts with a quarter turn, x is ready.

  A move sequence is a `List Mv`, `Mv = Fin 10` (the ten DR moves in the order U U2 U' D D2 D' R2 L2 F2 B2).
-/
import HTRRoutes.QtCosets

set_option compiler.extract_closed false

namespace HTRRoutes
namespace qtfull
open pieces corners cosets qtcos

/-- Move numbers 0, 2, 3, 5 are the quarter turns U U' D D'. -/
def isQt (m : Nat) : Bool := m == 0 || m == 2 || m == 3 || m == 5

/-! ### The tables -/

/-- Layered 0-1 search from the HTR coset: level d is spread over half turns (cost 0), then quarter turns lead to
level d + 1.  99 = not reached. -/
def qfCompute : Array Nat := Id.run do
  let mut q := Array.replicate N 99
  let mut cur : Array Nat := #[GOAL]
  q := q.set! GOAL 0
  for d in [0:12] do
    let mut i := 0
    while i < cur.size do
      let x := cur[i]!
      i := i + 1
      for m in HALF do
        let y := st x m
        if q[y]! == 99 then
          q := q.set! y d
          cur := cur.push y
    let mut nxt : Array Nat := #[]
    for x in cur do
      for m in QT do
        let y := st x m
        if q[y]! == 99 then
          q := q.set! y (d + 1)
          nxt := nxt.push y
    cur := nxt
  return q
def QF : Array Nat := qfCompute
/-- The fewest quarter turns from coset x into HTR. -/
def qf (x : Nat) : Nat := QF[x]!

/-- The corners' count of coset x. -/
def CQ : Array Nat := REPS.map qt
def cq (x : Nat) : Nat := CQ[x / 256]!

/-- x is one of the 29,400 HTR cosets. -/
def V (x : Nat) : Bool := decide (x < N) && valid x

def allV (p : Nat → Bool) : Bool := (List.range N).all fun x => !V x || p x
def allM (p : Nat → Bool) : Bool := (List.range 10).all p
def anyM (p : Nat → Bool) : Bool := (List.range 10).any p

/-- Some quarter turn lowers qf right away. -/
def lowersF (x : Nat) : Bool := anyM fun m => isQt m && qf (st x m) + 1 == qf x
/-- **Ready**: some quarter turn lowers the corners' count right away. -/
def ready (x : Nat) : Bool := anyM fun m => isQt m && cq (st x m) + 1 == cq x

def SFD : ByteArray := search.bfs N ((List.range N).filter fun x => V x && lowersF x) HALF st
def sF (x : Nat) : Nat := (SFD.get! x).toNat
def SCD : ByteArray := search.bfs N ((List.range N).filter fun x => V x && ready x) HALF st
/-- The corners' setup count. -/
def sC (x : Nat) : Nat := (SCD.get! x).toNat

/-! ### The checks -/

/-- The cosets are closed under the moves; a half turn keeps qf; a quarter turn changes it by exactly one. -/
def chkStep : Bool := V GOAL && allV fun x => allM fun m =>
  V (st x m) && (!isQt m || (qf (st x m) + 1 == qf x || qf (st x m) == qf x + 1)) &&
    (isQt m || qf (st x m) == qf x)
/-- qf is 0 exactly at the HTR coset. -/
def chkZero : Bool := allV fun x => (qf x == 0) == (x == GOAL)
/-- From qf > 0 there is a way down: a quarter turn that lowers qf (when sF = 0), or a half turn that lowers sF. -/
def chkDown : Bool := allV fun x => qf x == 0 ||
  (sF x != 0 || anyM fun m => isQt m && qf (st x m) + 1 == qf x) &&
    (sF x == 0 || anyM fun m => !isQt m && sF (st x m) + 1 == sF x)
/-- The corners' count is at most qf; a half turn keeps it; a quarter turn lowers it by at most one. -/
def chkCorner : Bool := allV fun x => decide (cq x ≤ qf x) && allM fun m =>
  (!isQt m || decide (cq x ≤ cq (st x m) + 1)) && (isQt m || cq (st x m) == cq x)
/-- sC is 0 exactly on the ready cosets; a half turn lowers it by at most one; from 0 < sC < 255 some half turn
lowers it by one; it is 255 exactly when the corners' count is 0. -/
def chkSetup : Bool := allV fun x =>
  (ready x == (sC x == 0)) && (allM fun m => isQt m || decide (sC x ≤ sC (st x m) + 1)) &&
    (sC x == 0 || sC x == 255 || anyM fun m => !isQt m && sC (st x m) + 1 == sC x) &&
    ((sC x == 255) == (cq x == 0))

structure Checked : Prop where
  step : chkStep = true
  zero : chkZero = true
  down : chkDown = true
  corner : chkCorner = true
  setup : chkSetup = true

/-! ### Move sequences -/

abbrev Mv := Fin 10

/-- The coset after the moves of `w`, done left to right. -/
def run : Nat → List Mv → Nat
  | x, [] => x
  | x, m :: w => run (st x m.val) w

/-- The number of quarter turns of `w`. -/
def qts : List Mv → Nat
  | [] => 0
  | m :: w => (isQt m.val).toNat + qts w

theorem run_append : ∀ (a b : List Mv) (x : Nat), run x (a ++ b) = run (run x a) b
  | [], _, _ => rfl
  | m :: a, b, x => by simp only [List.cons_append, run]; exact run_append a b _

theorem qts_append : ∀ (a b : List Mv), qts (a ++ b) = qts a + qts b
  | [], b => by simp [qts]
  | m :: a, b => by simp only [List.cons_append, qts, qts_append a b]; omega

/-! ### From the checks to statements about every coset and move -/

theorem allV_spec {p : Nat → Bool} (h : allV p = true) {x : Nat} (hx : V x = true) : p x = true := by
  have hlt : x < N := by
    simp only [V, Bool.and_eq_true, decide_eq_true_eq] at hx
    exact hx.1
  have h1 := List.all_eq_true.mp h x (List.mem_range.mpr hlt)
  rw [hx] at h1
  simpa using h1

theorem allM_spec {p : Nat → Bool} (h : allM p = true) (m : Mv) : p m.val = true :=
  List.all_eq_true.mp h m.val (List.mem_range.mpr m.isLt)

theorem anyM_spec {p : Nat → Bool} (h : anyM p = true) : ∃ m : Mv, p m.val = true := by
  obtain ⟨m, hm, hp⟩ := List.any_eq_true.mp h
  exact ⟨⟨m, List.mem_range.mp hm⟩, hp⟩

theorem anyM_intro {p : Nat → Bool} (m : Mv) (h : p m.val = true) : anyM p = true :=
  List.any_eq_true.mpr ⟨m.val, List.mem_range.mpr m.isLt, h⟩

theorem of_imp {b p : Bool} (h : (!b || p) = true) (hb : b = true) : p = true := by
  subst hb; simpa using h

theorem of_or {b p : Bool} (h : (b || p) = true) (hb : b = false) : p = true := by
  subst hb; simpa using h

theorem sF_lt (x : Nat) : sF x < 256 := UInt8.toNat_lt _

theorem ar1 (a b s t f : Nat) (h : 256 * a + s < f + 1) (hb : b + 1 = a) (ht : t < 256) : 256 * b + t < f := by
  omega
theorem ar2 (a b s t f : Nat) (h : 256 * a + s < f + 1) (hb : b = a) (ht : t + 1 = s) : 256 * b + t < f := by
  omega

section
variable (C : Checked)
include C

theorem V_goal : V GOAL = true := by
  have h := C.step
  simp only [chkStep, Bool.and_eq_true] at h
  exact h.1

theorem step_raw {x : Nat} (hx : V x = true) (m : Mv) :
    (V (st x m.val) && (!isQt m.val || (qf (st x m.val) + 1 == qf x || qf (st x m.val) == qf x + 1)) &&
      (isQt m.val || qf (st x m.val) == qf x)) = true := by
  have h := C.step
  simp only [chkStep, Bool.and_eq_true] at h
  exact allM_spec (allV_spec h.2 hx) m

/-- The cosets are closed under the moves. -/
theorem st_V {x : Nat} (hx : V x = true) (m : Mv) : V (st x m.val) = true := by
  have h := step_raw C hx m
  simp only [Bool.and_eq_true] at h
  exact h.1.1

/-- **A half turn keeps qf.** -/
theorem qf_half {x : Nat} (hx : V x = true) (m : Mv) (hq : isQt m.val = false) : qf (st x m.val) = qf x := by
  have h := step_raw C hx m
  simp only [Bool.and_eq_true] at h
  exact beq_iff_eq.mp (of_or h.2 hq)

/-- **A quarter turn changes qf by exactly one.** -/
theorem qf_quarter {x : Nat} (hx : V x = true) (m : Mv) (hq : isQt m.val = true) :
    qf (st x m.val) + 1 = qf x ∨ qf (st x m.val) = qf x + 1 := by
  have h := step_raw C hx m
  simp only [Bool.and_eq_true] at h
  have h2 := of_imp h.1.2 hq
  simp only [Bool.or_eq_true, beq_iff_eq] at h2
  exact h2

theorem run_V : ∀ (w : List Mv) {x : Nat}, V x = true → V (run x w) = true
  | [], _, h => h
  | m :: w, _, h => run_V w (st_V C h m)

theorem zero_iff {x : Nat} (hx : V x = true) : qf x = 0 ↔ x = GOAL := by
  have h := allV_spec C.zero hx
  have h' : (qf x == 0) = (x == GOAL) := by simpa using h
  constructor
  · intro e
    have h2 : (qf x == 0) = true := by simp [e]
    rw [h'] at h2
    exact beq_iff_eq.mp h2
  · intro e
    have h2 : (x == GOAL) = true := by simp [e]
    rw [← h'] at h2
    exact beq_iff_eq.mp h2

theorem qf_goal : qf GOAL = 0 := (zero_iff C (V_goal C)).mpr rfl

/-- A sequence with k quarter turns lowers qf by at most k. -/
theorem qf_le_run : ∀ (w : List Mv) {x : Nat}, V x = true → qf x ≤ qts w + qf (run x w)
  | [], x, _ => by simp [qts, run]
  | m :: w, x, h => by
    have ih := qf_le_run w (st_V C h m)
    simp only [qts, run]
    cases hq : isQt m.val with
    | true =>
      have h1 := qf_quarter C h m hq
      simp only [Bool.toNat_true]
      omega
    | false =>
      have h1 := qf_half C h m hq
      simp only [Bool.toNat_false]
      omega

/-- **Lower bound**: every sequence from x into HTR has at least qf x quarter turns. -/
theorem qf_lower {x : Nat} (hx : V x = true) (w : List Mv) (hw : run x w = GOAL) : qf x ≤ qts w := by
  have h := qf_le_run C w hx
  rw [hw, qf_goal C] at h
  omega

theorem attained_aux : ∀ (fuel : Nat) {x : Nat}, V x = true → 256 * qf x + sF x < fuel →
    ∃ w : List Mv, run x w = GOAL ∧ qts w = qf x
  | 0, _, _, h => absurd h (Nat.not_lt_zero _)
  | fuel + 1, x, hx, hf => by
    by_cases h0 : qf x = 0
    · exact ⟨[], (zero_iff C hx).mp h0, by simp [qts, h0]⟩
    · have hd := allV_spec C.down hx
      have h0' : (qf x == 0) = false := by simpa using h0
      have hd2 := of_or hd h0'
      simp only [Bool.and_eq_true] at hd2
      by_cases hs : sF x = 0
      · have hs' : (sF x != 0) = false := by simp [hs]
        obtain ⟨m, hm⟩ := anyM_spec (of_or hd2.1 hs')
        simp only [Bool.and_eq_true, beq_iff_eq] at hm
        obtain ⟨w, hw, hq⟩ := attained_aux fuel (st_V C hx m) (ar1 _ _ _ _ _ hf hm.2 (sF_lt _))
        refine ⟨m :: w, hw, ?_⟩
        simp only [qts, hm.1, Bool.toNat_true, hq]
        omega
      · have hs' : (sF x == 0) = false := by simpa using hs
        obtain ⟨m, hm⟩ := anyM_spec (of_or hd2.2 hs')
        simp only [Bool.and_eq_true, beq_iff_eq, Bool.not_eq_true'] at hm
        have hk := qf_half C hx m hm.1
        obtain ⟨w, hw, hq⟩ := attained_aux fuel (st_V C hx m) (ar2 _ _ _ _ _ hf hk hm.2)
        refine ⟨m :: w, hw, ?_⟩
        simp only [qts, hm.1, Bool.toNat_false, hq]
        omega

/-- **Attained**: some sequence from x into HTR has exactly qf x quarter turns.  So qf x is the fewest quarter
turns of any DR move sequence from x into HTR. -/
theorem qf_attained {x : Nat} (hx : V x = true) : ∃ w : List Mv, run x w = GOAL ∧ qts w = qf x :=
  attained_aux C (256 * qf x + sF x + 1) hx (Nat.lt_succ_self _)

/-- **On a sequence into HTR with no extra quarter turn, every quarter turn lowers qf by one.** -/
theorem tight_lowers {x : Nat} (hx : V x = true) (a : List Mv) (m : Mv) (b : List Mv)
    (hw : run x (a ++ m :: b) = GOAL) (ht : qts (a ++ m :: b) = qf x) (hq : isQt m.val = true) :
    qf (st (run x a) m.val) + 1 = qf (run x a) := by
  have hy := run_V C a hx
  have h1 := qf_le_run C a hx
  have hz := st_V C hy m
  have hb : run (st (run x a) m.val) b = GOAL := by
    rw [run_append] at hw
    exact hw
  have h2 := qf_lower C hz b hb
  have h3 : qts (a ++ m :: b) = qts a + 1 + qts b := by
    rw [qts_append]
    simp only [qts, hq, Bool.toNat_true]
    omega
  rcases qf_quarter C hy m hq with h | h <;> omega

theorem corner_raw {x : Nat} (hx : V x = true) :
    cq x ≤ qf x ∧ ∀ m : Mv, (isQt m.val = true → cq x ≤ cq (st x m.val) + 1) ∧
      (isQt m.val = false → cq (st x m.val) = cq x) := by
  have h := allV_spec C.corner hx
  simp only [Bool.and_eq_true, decide_eq_true_eq] at h
  refine ⟨h.1, fun m => ?_⟩
  have h2 := allM_spec h.2 m
  simp only [Bool.and_eq_true] at h2
  exact ⟨fun hq => of_decide_eq_true (of_imp h2.1 hq), fun hq => beq_iff_eq.mp (of_or h2.2 hq)⟩

theorem setup_raw {x : Nat} (hx : V x = true) :
    (ready x = true ↔ sC x = 0) ∧ ∀ m : Mv, isQt m.val = false → sC x ≤ sC (st x m.val) + 1 := by
  have h := allV_spec C.setup hx
  simp only [Bool.and_eq_true] at h
  refine ⟨?_, fun m hq => of_decide_eq_true (of_or (allM_spec h.1.1.2 m) hq)⟩
  have h' : ready x = (sC x == 0) := by simpa using h.1.1.1
  rw [h']
  exact beq_iff_eq

/-- Half turns keep qf and the corners' count. -/
theorem half_run : ∀ (p : List Mv) {x : Nat}, V x = true → (∀ h ∈ p, isQt h.val = false) →
    qf (run x p) = qf x ∧ cq (run x p) = cq x
  | [], _, _, _ => ⟨rfl, rfl⟩
  | m :: p, x, hx, hp => by
    have hm := hp m List.mem_cons_self
    have ih := half_run p (st_V C hx m) (fun h hh => hp h (List.mem_cons_of_mem _ hh))
    simp only [run]
    exact ⟨ih.1.trans (qf_half C hx m hm), ih.2.trans (((corner_raw C hx).2 m).2 hm)⟩

/-- k half turns lower the corners' setup count by at most k. -/
theorem sC_le_run : ∀ (p : List Mv) {x : Nat}, V x = true → (∀ h ∈ p, isQt h.val = false) →
    sC x ≤ p.length + sC (run x p)
  | [], _, _, _ => by simp [run]
  | m :: p, x, hx, hp => by
    have hm := hp m List.mem_cons_self
    have ih := sC_le_run p (st_V C hx m) (fun h hh => hp h (List.mem_cons_of_mem _ hh))
    have h1 := (setup_raw C hx).2 m hm
    simp only [run, List.length_cons]
    omega

/-- **The floor.**  If the fewest-qt number of x is the corners' count, a sequence into HTR with no extra quarter
turn makes at least sC x half turns before its first quarter turn: the first quarter turn cannot come before the
half turns the corners need. -/
theorem floor {x : Nat} (hx : V x = true) (hrow : qf x = cq x) (p : List Mv) (m : Mv) (t : List Mv)
    (hp : ∀ h ∈ p, isQt h.val = false) (hq : isQt m.val = true)
    (hw : run x (p ++ m :: t) = GOAL) (ht : qts (p ++ m :: t) = qf x) : sC x ≤ p.length := by
  have hy := run_V C p hx
  have hk := half_run C p hx hp
  have hl := tight_lowers C hx p m t hw ht hq
  have hz := st_V C hy m
  have c1 := (corner_raw C hz).1
  have c2 := ((corner_raw C hy).2 m).1 hq
  have hlow : cq (st (run x p) m.val) + 1 = cq (run x p) := by omega
  have hr : ready (run x p) = true :=
    anyM_intro m (by simp only [Bool.and_eq_true, beq_iff_eq]; exact ⟨hq, hlow⟩)
  have h0 := (setup_raw C hy).1.mp hr
  have h1 := sC_le_run C p hx hp
  omega

/-- **Rule 1, the exact half.**  If the fewest-qt number of x is the corners' count and a sequence into HTR with
no extra quarter turn starts with a quarter turn, then x is ready.  So from a coset that is not ready, no such
sequence starts with a quarter turn. -/
theorem rule_one {x : Nat} (hx : V x = true) (hrow : qf x = cq x) (m : Mv) (t : List Mv)
    (hq : isQt m.val = true) (hw : run x (m :: t) = GOAL) (ht : qts (m :: t) = qf x) : ready x = true := by
  have h := floor C hx hrow [] m t (fun _ hh => absurd hh List.not_mem_nil) hq hw ht
  exact (setup_raw C hx).1.mpr (by simpa using h)

end

/-! ### Tallies (for the statements of `QtFullTheorems.lean`) -/

/-- The 48-subset name of a coset ("4c3 2e"). -/
def lab48 (x : Nat) : String := label48 REPS[x / 256]! (x % 256)

/-- Per 48-subset name: (name, the values of qf on its cosets, the values of the corners' count, cosets). -/
@[noinline] def qfRows : List (String × List Nat × List Nat × Nat) := Id.run do
  let mut rows : List (String × Nat × Nat) := []
  for x in [0:N] do
    if V x then rows := (lab48 x, qf x, cq x) :: rows
  let keys := (rows.map (·.1)).eraseDups.mergeSort fun a b => decide (a < b)
  return keys.map fun k =>
    let r := rows.filter (·.1 == k)
    (k, (r.map (·.2.1)).eraseDups.mergeSort (· ≤ ·), (r.map (·.2.2)).eraseDups.mergeSort (· ≤ ·), r.length)

/-- The first coset number of corner coset k (edge pattern of the HTR coset). -/
def atK (k : Nat) : Nat := k * 256 + GOAL % 256

/-- `ready` and `sC` are read off the corners alone. -/
def cornersOnly : Bool := allV fun x => ready x == ready (atK (x / 256)) && sC x == sC (atK (x / 256))

/-- Per corner subset (14 names): (name, corner cosets, ready ones, the values of sC). -/
@[noinline] def readyRows : List (String × Nat × Nat × List Nat) :=
  (List.range 14).map fun t =>
    let ks := (List.range 420).filter fun k => sub REPS[k]! == t
    (NAMES[t]!, ks.length, (ks.filter fun k => ready (atK k)).length,
      (ks.map fun k => sC (atK k)).eraseDups.mergeSort (· ≤ ·))

/-- Per corner subset: the subsets a quarter turn that lowers the corners' count leads to. -/
@[noinline] def lowerRows : List (String × List String) :=
  (List.range 14).map fun t =>
    let ks := (List.range 420).filter fun k => sub REPS[k]! == t
    let to := ks.flatMap fun k => QT.filterMap fun m =>
      let y := st (atK k) m
      if cq y + 1 == cq (atK k) then some (sub REPS[y / 256]!) else none
    (NAMES[t]!, (to.eraseDups.mergeSort (· ≤ ·)).map fun u => NAMES[u]!)

end qtfull
end HTRRoutes
