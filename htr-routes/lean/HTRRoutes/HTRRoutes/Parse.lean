/-
  HTRRoutes.Parse — reads the research's files of `Study.lean` into the shapes Lean computes.
  A file is split into lines and each line into tab-separated fields; the header line and empty lines are dropped.
-/
import HTRRoutes.Study

namespace HTRRoutes
namespace parse

/-- The data lines of a tab-separated file, each as its list of fields. -/
def table (txt : String) : List (List String) :=
  ((txt.splitOn "\n").drop 1 |>.filter (· != "")).map (·.splitOn "\t")

/-- htr_states.tsv: (depth, states with that optimal finish in DR moves, … in half turns). -/
def htrStates : List (Nat × Nat × Nat) :=
  (table study.HTR_STATES_TSV).map fun r => (r[0]!.toNat!, r[1]!.toNat!, r[2]!.toNat!)

/-- The half-turn column as (depth, states), without the zero rows. -/
def htrHalfHist : List (Nat × Nat) := (htrStates.map fun r => (r.1, r.2.2)).filter (·.2 != 0)

/-- Order on (name, length, count) rows: by name, then length, then count. -/
def rowLe (a b : String × Nat × Nat) : Bool :=
  a.1 < b.1 || (a.1 == b.1 && (a.2.1 < b.2.1 || (a.2.1 == b.2.1 && a.2.2 ≤ b.2.2)))

/-- htr48.tsv: (subset, shortest linear HTR, cosets), sorted. -/
def htr48 : List (String × Nat × Nat) :=
  ((table study.HTR48_TSV).map fun r => (r[0]!, r[1]!.toNat!, r[2]!.toNat!)).mergeSort rowLe

/-- q9_alpha.tsv: (path, N, [α_0, …, α_N]). -/
def alphaRows : List (String × Nat × List Nat) :=
  (table study.Q9_ALPHA_TSV).map fun r => (r[0]!, r[1]!.toNat!, (r[2]!.splitOn ",").map String.toNat!)

/-- name_map.tsv: (doc, label, example, our_subset, normal_label, inverse_label). -/
def nameRows : List (String × String × String × String × String × String) :=
  (table study.NAME_MAP_TSV).map fun r => (r[0]!, r[1]!, r[2]!, r[3]!, r[4]!, r[5]!)

/-- `sub` occurs in `s`. -/
def says (s sub : String) : Bool := (s.splitOn sub).length > 1

end parse
end HTRRoutes
