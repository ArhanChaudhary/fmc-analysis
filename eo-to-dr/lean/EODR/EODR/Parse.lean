/-
  EODR.Parse — reads the research's files of `Study.lean` into the shapes Lean computes.
  A file is split into lines and each line into tab-separated fields; the header line and empty lines are dropped.
-/
import EODR.Study

namespace EODR
namespace parse

/-- The data lines of a tab-separated file, each as its list of fields. -/
def table (txt : String) : List (List String) :=
  ((txt.splitOn "\n").drop 1 |>.filter (· != "")).map (·.splitOn "\t")

/-- eo_axis.tsv without its first column (the research's eo coordinate), each row [bad, optimal, n0, …, n8],
sorted. -/
def eoAxisRows : List (List Nat) :=
  ((table study.EO_AXIS_TSV).map fun r => (r.drop 1).map String.toNat!).mergeSort (fun a b => decide (a ≤ b))

/-- eo_layouts.tsv: ((bad_fb, bad_rl, bad_ud), states). -/
def layoutRows : List ((Nat × Nat × Nat) × Nat) :=
  (table study.EO_LAYOUTS_TSV).map fun r =>
    let n := r.map String.toNat!
    ((n[0]!, n[1]!, n[2]!), n[3]!)

/-- eodr_exact.tsv, the rows of the options "eo", "eo_switchF", "eo_switchB":
(corners, edges, option, [d0, …, d11]). -/
def eodrRows : List (Nat × Nat × String × List Nat) :=
  ((table study.EODR_EXACT_TSV).filter fun r => ["eo", "eo_switchF", "eo_switchB"].contains r[2]!).map fun r =>
    (r[0]!.toNat!, r[1]!.toNat!, r[2]!, (r.drop 3).map String.toNat!)

/-- eo0_hist_eo-fb_dr.txt: (distance, states). -/
def eo0Hist : List (Nat × Nat) :=
  (table study.EO0_HIST_EO_FB_DR_TXT).map fun r => (r[0]!.toNat!, r[1]!.toNat!)

end parse
end EODR
