/-
  DRXs.SeoTheorems — statement F: how many of the 70,963,200 edge configurations have a slice-EO skip.

  `seo_skip_counts` is the one long run (all 70,963,200 configurations, about a minute of compiled code, accepted
  through `native_decide`).  The statements after it are read off from it by the kernel, without running again.
  **Editing this file or SeoSkip.lean, comments included, repeats the run.**
-/
import DRXs.SeoSkip

namespace DRXs
open seo_skip

-- The run takes longer than Lean's default time-out for elaborating one statement.
set_option maxHeartbeats 0

/-- The whole count: the number of configurations, and how many of them have exactly k slice-EO skips, on
normal and on normal and inverse together (the two tables 'normal' and 'both' of research/out/seo_skip.txt). -/
theorem seo_skip_counts : main () =
    { tot := 70963200,
      hist_normal := [(0, 22143888), (1, 26110080), (2, 16123104), (3, 5186256), (4, 1106784), (5, 272160),
                      (6, 15984), (7, 4896), (9, 48)],
      hist_both := [(0, 14678928), (1, 13374720), (2, 14827968), (3, 10153728), (4, 9929520), (5, 4174848),
                    (6, 2439312), (7, 580608), (8, 511632), (9, 165888), (10, 110448), (12, 13104), (14, 2448),
                    (18, 48)] } := by
  native_decide

/-- Of the 70,963,200 configurations, 22,143,888 have no slice-EO skip on normal, and 14,678,928 have none on
normal or inverse. -/
theorem seo_no_skip :
    (main ()).tot = 70963200 ∧ (main ()).none_normal = 22143888 ∧ (main ()).none_both = 14678928 := by
  rw [seo_skip_counts]; decide

/-- The configurations are the 34,650 placements times the 2,048 orientation vectors. -/
theorem seo_configurations : 34650 * 2048 = 70963200 := by decide

/-- So the share with at least one skip on normal is 68.7953 % to four places
(68.79525 % ≤ share < 68.79535 %) … -/
theorem seo_share_normal :
    687952500 * 70963200 ≤ 10 ^ 9 * (70963200 - 22143888) ∧
    10 ^ 9 * (70963200 - 22143888) < 687953500 * 70963200 := by decide

/-- … and on normal or inverse 79.3147 % (79.31465 % ≤ share < 79.31475 %). -/
theorem seo_share_both :
    793146500 * 70963200 ≤ 10 ^ 9 * (70963200 - 14678928) ∧
    10 ^ 9 * (70963200 - 14678928) < 793147500 * 70963200 := by decide

end DRXs
