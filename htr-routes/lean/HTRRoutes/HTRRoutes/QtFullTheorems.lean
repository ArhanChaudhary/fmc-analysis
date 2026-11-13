/-
  HTRRoutes.QtFullTheorems — checked statements, part F: the fewest quarter turns of a finish, ready sides and the
  floor under rule 1 (see README.md).  The definitions and the kernel-checked steps are in `QtFull.lean`;
  `native_decide` runs the table checks and the tallies here.
-/
import HTRRoutes.QtFull

namespace HTRRoutes

set_option maxHeartbeats 0

open qtfull in
/-- The five checks of `QtFull.lean` hold on all 29,400 HTR cosets and all ten moves. -/
theorem qt_full_checked : Checked :=
  ⟨by native_decide, by native_decide, by native_decide, by native_decide, by native_decide⟩

open qtfull qtcos cosets in
/-- **The fewest quarter turns from a coset into HTR** (kernel-checked from `qt_full_checked`): every sequence of
DR moves from x into the HTR coset has at least qf x quarter turns, and some sequence has exactly qf x. -/
theorem qf_is_fewest {x : Nat} (hx : V x = true) :
    (∀ w : List Mv, run x w = GOAL → qf x ≤ qts w) ∧ (∃ w : List Mv, run x w = GOAL ∧ qts w = qf x) :=
  ⟨qf_lower qt_full_checked hx, qf_attained qt_full_checked hx⟩

open qtfull qtcos cosets in
/-- **Half turns never change it, and a quarter turn changes it by exactly one.** -/
theorem qf_steps {x : Nat} (hx : V x = true) (m : Mv) :
    (isQt m.val = false → qf (st x m.val) = qf x) ∧
    (isQt m.val = true → qf (st x m.val) + 1 = qf x ∨ qf (st x m.val) = qf x + 1) :=
  ⟨qf_half qt_full_checked hx m, qf_quarter qt_full_checked hx m⟩

open qtfull qtcos cosets in
/-- **No extra quarter turn.**  On a sequence from x into HTR with exactly qf x quarter turns, every quarter turn
lowers qf by one: with w = a ++ m :: b and m a quarter turn, qf after a ++ [m] is one less than qf after a. -/
theorem no_extra_every_qt_lowers {x : Nat} (hx : V x = true) (a : List Mv) (m : Mv) (b : List Mv)
    (hw : run x (a ++ m :: b) = GOAL) (ht : qts (a ++ m :: b) = qf x) (hq : isQt m.val = true) :
    qf (st (run x a) m.val) + 1 = qf (run x a) :=
  tight_lowers qt_full_checked hx a m b hw ht hq

open qtfull qtcos cosets in
/-- **The floor, and rule 1 the exact way.**  Let qf x be the corners' count.  A sequence from x into HTR with no
extra quarter turn, written p ++ m :: t with p half turns and m its first quarter turn, has at least sC x half
turns in p (the half turns the corners need).  In particular, if it starts with a quarter turn, x is ready. -/
theorem floor_and_rule_one {x : Nat} (hx : V x = true) (hrow : qf x = cq x) :
    (∀ (p : List Mv) (m : Mv) (t : List Mv), (∀ h ∈ p, isQt h.val = false) → isQt m.val = true →
      run x (p ++ m :: t) = GOAL → qts (p ++ m :: t) = qf x → sC x ≤ p.length) ∧
    (∀ (m : Mv) (t : List Mv), isQt m.val = true → run x (m :: t) = GOAL → qts (m :: t) = qf x →
      ready x = true) :=
  ⟨fun p m t => floor qt_full_checked hx hrow p m t, fun m t => rule_one qt_full_checked hx hrow m t⟩

open qtfull qtcos cosets in
/-- **The value of qf.**  3 on 4a1 0e and 4a1 2e (the corners' count is 1), 2 on every 0c0 coset but the HTR
coset itself (the corners' count is 0), and the corners' count on every other coset. -/
theorem qf_values :
    allV (fun x => qf x == (if lab48 x == "4a1 0e" || lab48 x == "4a1 2e" then 3
      else if cq x == 0 then (if x == GOAL then 0 else 2) else cq x)) = true := by
  native_decide

open qtfull in
/-- **Per subset × edges** (the 48 names): the values of qf on its cosets, the corners' count, and how many cosets
it has.  The page's column "Quarter turns in such a finish". -/
theorem qf_by_row : qfRows =
    [("0c0 0e", [0, 2], [0], 2), ("0c0 2e", [2], [0], 32), ("0c0 4e", [2], [0], 72), ("0c0 6e", [2], [0], 32),
     ("0c0 8e", [2], [0], 2),
     ("0c3 0e", [3], [3], 6), ("0c3 2e", [3], [3], 96), ("0c3 4e", [3], [3], 216), ("0c3 6e", [3], [3], 96),
     ("0c3 8e", [3], [3], 6),
     ("0c4 0e", [4], [4], 4), ("0c4 2e", [4], [4], 64), ("0c4 4e", [4], [4], 144), ("0c4 6e", [4], [4], 64),
     ("0c4 8e", [4], [4], 4),
     ("2c3 0e", [3], [3], 64), ("2c3 2e", [3], [3], 1024), ("2c3 4e", [3], [3], 2304), ("2c3 6e", [3], [3], 1024),
     ("2c3 8e", [3], [3], 64),
     ("2c4 0e", [4], [4], 96), ("2c4 2e", [4], [4], 1536), ("2c4 4e", [4], [4], 3456), ("2c4 6e", [4], [4], 1536),
     ("2c4 8e", [4], [4], 96),
     ("2c5 0e", [5], [5], 32), ("2c5 2e", [5], [5], 512), ("2c5 4e", [5], [5], 1152), ("2c5 6e", [5], [5], 512),
     ("2c5 8e", [5], [5], 32),
     ("4a1 0e", [3], [1], 24), ("4a1 2e", [3], [1], 384), ("4a1 4e", [1], [1], 432),
     ("4a2 0e", [2], [2], 24), ("4a2 2e", [2], [2], 384), ("4a2 4e", [2], [2], 432),
     ("4b2 0e", [2], [2], 96), ("4b2 2e", [2], [2], 1536), ("4b2 4e", [2], [2], 1728),
     ("4b5 0e", [5], [5], 96), ("4b5 2e", [5], [5], 1536), ("4b5 4e", [5], [5], 1728),
     ("4c3 0e", [3], [3], 96), ("4c3 2e", [3], [3], 1536), ("4c3 4e", [3], [3], 1728),
     ("4c4 0e", [4], [4], 96), ("4c4 2e", [4], [4], 1536), ("4c4 4e", [4], [4], 1728)] := by
  native_decide

open qtfull in
/-- **Ready, per corner subset.**  `ready` and the corners' setup count are read off the corner coset alone.  Per
corner subset: (name, corner cosets, ready ones, the values of the setup count).  2c5, 0c4 and 4b5 are always
ready; 0c0 has nothing to lower (255); the other eight (4a1, 4a2, 4b2, 0c3, 2c3, 4a3 / 4b3, 2c4, 4a4 / 4b4) have
ready cosets and cosets that need a setup; on 4a1, 4a2 and 4b2 the corners can need up to 3 half turns, on 4a3
up to 2, on the others at most 1. -/
theorem ready_by_subset :
    cornersOnly = true ∧
    readyRows =
      [("0c0", 2, 0, [255]), ("4a1", 12, 2, [0, 1, 2, 3]), ("4a2", 12, 2, [0, 1, 2, 3]),
       ("4b2", 48, 8, [0, 1, 2, 3]), ("0c3", 6, 2, [0, 1]), ("2c3", 64, 32, [0, 1]), ("4a3", 24, 8, [0, 1, 2]),
       ("4b3", 24, 8, [0, 1]), ("0c4", 4, 4, [0]), ("2c4", 96, 48, [0, 1]), ("4a4", 24, 8, [0, 1]),
       ("4b4", 24, 8, [0, 1]), ("2c5", 32, 32, [0]), ("4b5", 48, 48, [0])] := by
  native_decide

open qtfull in
/-- **Where a lowering quarter turn leads**, per corner subset (the side's own letter for 3 and 4 qt): 4a1 to 0c0,
4a2 and 4b2 to 4a1, 0c3 to 4a2, 2c3 to 4b2, 4a3 to 4b2, 4b3 to 4a2, 0c4 to 4a3, 2c4 to 2c3 or 4b3, 4a4 to 0c3 or
4a3, 4b4 to 4a3, 2c5 to 2c4 or 4b4, 4b5 to 2c4 or 4a4. -/
theorem lowering_turns : lowerRows =
    [("0c0", []), ("4a1", ["0c0"]), ("4a2", ["4a1"]), ("4b2", ["4a1"]), ("0c3", ["4a2"]), ("2c3", ["4b2"]),
     ("4a3", ["4b2"]), ("4b3", ["4a2"]), ("0c4", ["4a3"]), ("2c4", ["2c3", "4b3"]), ("4a4", ["0c3", "4a3"]),
     ("4b4", ["4a3"]), ("2c5", ["2c4", "4b4"]), ("4b5", ["2c4", "4a4"])] := by
  native_decide

end HTRRoutes
