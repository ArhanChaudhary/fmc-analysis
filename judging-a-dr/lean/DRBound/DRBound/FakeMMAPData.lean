/-
  DRBound.FakeMMAPData — transcription of FakeMMAP's breadth-first-search listing
  (Discord "FMC solvers", #fmc-theory, 2026-09-06, attachment message.txt of message T12061).

  Each entry: an example scramble of half turns, and the number of half turns the search reports for the
  resulting case.  Case names (corner case, M-slice and S-slice edge patterns, E parity) are kept as comments.
  Generated mechanically from the attachment; do not edit by hand.
-/
import DRBound.Cube

namespace DRBound

def fakemmapCases : List (List Move × Nat) := [
  ([], 0),  -- H-H + F-H R-H even E-parity
  ([.R2], 1),  -- R-D + F-H R-D  odd E-parity
  ([.F2], 1),  -- F-D + F-D R-H  odd E-parity
  ([.R2, .U2], 2),  -- R-V + F-H R-V  odd E-parity
  ([.R2, .F2], 2),  -- R-D - F-D R-D even E-parity
  ([.F2, .U2], 2),  -- F-V + F-V R-H  odd E-parity
  ([.F2, .R2], 2),  -- F-D - F-D R-D even E-parity
  ([.R2, .U2, .R2], 3),  -- R-V + F-H R-V even E-parity
  ([.R2, .U2, .F2], 3),  -- D-D + F-D R-V even E-parity
  ([.R2, .F2, .U2], 3),  -- R-V - F-V R-V even E-parity
  ([.R2, .F2, .R2], 3),  -- H-H - F-D R-H  odd E-parity
  ([.F2, .U2, .R2], 3),  -- D-D - F-V R-D even E-parity
  ([.F2, .U2, .F2], 3),  -- F-V + F-V R-H even E-parity
  ([.F2, .R2, .U2], 3),  -- F-V - F-V R-V even E-parity
  ([.F2, .R2, .F2], 3),  -- H-H - F-H R-D  odd E-parity
  ([.R2, .U2, .R2, .U2], 4),  -- R-D + F-H R-D even E-parity
  ([.R2, .U2, .R2, .F2], 4),  -- D-D + F-D R-V  odd E-parity
  ([.R2, .U2, .F2, .R2], 4),  -- F-V - F-D R-V  odd E-parity
  ([.R2, .F2, .U2, .R2], 4),  -- R-V - F-V R-V  odd E-parity
  ([.R2, .F2, .U2, .F2], 4),  -- D-D - F-V R-V  odd E-parity
  ([.R2, .F2, .R2, .U2], 4),  -- H-H - F-V R-H  odd E-parity
  ([.R2, .F2, .R2, .F2], 4),  -- F-D - F-H R-H even E-parity
  ([.F2, .U2, .R2, .F2], 4),  -- R-V - F-V R-D  odd E-parity
  ([.F2, .U2, .F2, .U2], 4),  -- F-D + F-D R-H even E-parity
  ([.F2, .U2, .F2, .R2], 4),  -- D-D - F-V R-D  odd E-parity
  ([.F2, .R2, .U2, .R2], 4),  -- D-D + F-V R-V  odd E-parity
  ([.F2, .R2, .U2, .F2], 4),  -- F-V - F-V R-V  odd E-parity
  ([.F2, .R2, .F2, .U2], 4),  -- H-H - F-H R-V  odd E-parity
  ([.F2, .R2, .F2, .R2], 4),  -- R-D - F-H R-H even E-parity
  ([.R2, .U2, .R2, .U2, .R2], 5),  -- H-H + F-H R-H  odd E-parity
  ([.R2, .U2, .R2, .U2, .F2], 5),  -- R-D - F-D R-D  odd E-parity
  ([.R2, .U2, .R2, .F2, .R2], 5),  -- F-V - F-D R-V even E-parity
  ([.R2, .U2, .F2, .R2, .U2], 5),  -- F-D - F-V R-D  odd E-parity
  ([.R2, .U2, .F2, .R2, .F2], 5),  -- F-V - F-H R-V even E-parity
  ([.R2, .F2, .U2, .R2, .F2], 5),  -- D-D - F-V R-V even E-parity
  ([.R2, .F2, .U2, .F2, .U2], 5),  -- D-D + F-D R-D  odd E-parity
  ([.R2, .F2, .U2, .F2, .R2], 5),  -- F-V + F-V R-V even E-parity
  ([.R2, .F2, .R2, .U2, .R2], 5),  -- R-D - F-V R-D even E-parity
  ([.R2, .F2, .R2, .U2, .F2], 5),  -- F-D - F-V R-H even E-parity
  ([.R2, .F2, .R2, .F2, .U2], 5),  -- F-V - F-H R-H even E-parity
  ([.R2, .F2, .R2, .F2, .R2], 5),  -- F-D + F-H R-D  odd E-parity
  ([.F2, .U2, .R2, .F2, .U2], 5),  -- R-D - F-D R-V  odd E-parity
  ([.F2, .U2, .R2, .F2, .R2], 5),  -- R-V - F-V R-H even E-parity
  ([.F2, .U2, .F2, .U2, .R2], 5),  -- F-D - F-D R-D  odd E-parity
  ([.F2, .U2, .F2, .R2, .F2], 5),  -- R-V - F-V R-D even E-parity
  ([.F2, .R2, .U2, .R2, .U2], 5),  -- D-D - F-D R-D  odd E-parity
  ([.F2, .R2, .U2, .R2, .F2], 5),  -- R-V + F-V R-V even E-parity
  ([.F2, .R2, .U2, .F2, .R2], 5),  -- D-D + F-V R-V even E-parity
  ([.F2, .R2, .F2, .U2, .R2], 5),  -- R-D - F-H R-V even E-parity
  ([.F2, .R2, .F2, .U2, .F2], 5),  -- F-D - F-D R-V even E-parity
  ([.F2, .R2, .F2, .R2, .U2], 5),  -- R-V - F-H R-H even E-parity
  ([.F2, .R2, .F2, .R2, .F2], 5),  -- R-D + F-D R-H  odd E-parity
  ([.R2, .U2, .R2, .U2, .F2, .R2], 6),  -- H-H - F-D R-H even E-parity
  ([.R2, .U2, .R2, .F2, .R2, .U2], 6),  -- F-D - F-V R-D even E-parity
  ([.R2, .U2, .R2, .F2, .R2, .F2], 6),  -- F-V - F-H R-V  odd E-parity
  ([.R2, .U2, .F2, .R2, .U2, .R2], 6),  -- F-D + F-V R-H even E-parity
  ([.R2, .U2, .F2, .R2, .U2, .F2], 6),  -- H-H - F-V R-D even E-parity
  ([.R2, .U2, .F2, .R2, .F2, .U2], 6),  -- F-D - F-H R-D even E-parity
  ([.R2, .U2, .F2, .R2, .F2, .R2], 6),  -- D-D + F-H R-V  odd E-parity
  ([.R2, .F2, .U2, .R2, .F2, .U2], 6),  -- D-D + F-D R-D even E-parity
  ([.R2, .F2, .U2, .R2, .F2, .R2], 6),  -- F-V + F-V R-V  odd E-parity
  ([.R2, .F2, .U2, .F2, .U2, .R2], 6),  -- F-V - F-D R-H even E-parity
  ([.R2, .F2, .U2, .F2, .U2, .F2], 6),  -- R-V + F-H R-D even E-parity
  ([.R2, .F2, .U2, .F2, .R2, .U2], 6),  -- F-D + F-D R-D even E-parity
  ([.R2, .F2, .R2, .U2, .R2, .U2], 6),  -- R-V - F-D R-V even E-parity
  ([.R2, .F2, .R2, .U2, .R2, .F2], 6),  -- R-D + F-V R-D  odd E-parity
  ([.R2, .F2, .R2, .U2, .F2, .R2], 6),  -- F-D + F-V R-D  odd E-parity
  ([.R2, .F2, .R2, .F2, .U2, .R2], 6),  -- D-D + F-H R-D  odd E-parity
  ([.R2, .F2, .R2, .F2, .U2, .F2], 6),  -- F-V - F-D R-H  odd E-parity
  ([.R2, .F2, .R2, .F2, .R2, .U2], 6),  -- F-V + F-H R-V  odd E-parity
  ([.R2, .F2, .R2, .F2, .R2, .F2], 6),  -- H-H + F-D R-D even E-parity
  ([.F2, .U2, .R2, .F2, .U2, .R2], 6),  -- H-H - F-D R-V even E-parity
  ([.F2, .U2, .R2, .F2, .U2, .F2], 6),  -- R-D + F-H R-V even E-parity
  ([.F2, .U2, .R2, .F2, .R2, .U2], 6),  -- R-D - F-D R-H even E-parity
  ([.F2, .U2, .R2, .F2, .R2, .F2], 6),  -- D-D - F-V R-H  odd E-parity
  ([.F2, .U2, .F2, .U2, .R2, .F2], 6),  -- H-H - F-H R-D even E-parity
  ([.F2, .U2, .F2, .R2, .F2, .U2], 6),  -- R-D - F-D R-V even E-parity
  ([.F2, .U2, .F2, .R2, .F2, .R2], 6),  -- R-V - F-V R-H  odd E-parity
  ([.F2, .R2, .U2, .R2, .U2, .R2], 6),  -- F-V + F-D R-H even E-parity
  ([.F2, .R2, .U2, .R2, .U2, .F2], 6),  -- R-V - F-H R-D even E-parity
  ([.F2, .R2, .U2, .R2, .F2, .U2], 6),  -- R-D + F-D R-D even E-parity
  ([.F2, .R2, .U2, .R2, .F2, .R2], 6),  -- R-V + F-V R-V  odd E-parity
  ([.F2, .R2, .U2, .F2, .R2, .U2], 6),  -- D-D - F-D R-D even E-parity
  ([.F2, .R2, .F2, .U2, .R2, .F2], 6),  -- R-D + F-D R-V  odd E-parity
  ([.F2, .R2, .F2, .U2, .F2, .U2], 6),  -- F-V - F-V R-D even E-parity
  ([.F2, .R2, .F2, .U2, .F2, .R2], 6),  -- F-D + F-D R-V  odd E-parity
  ([.F2, .R2, .F2, .R2, .U2, .R2], 6),  -- R-V - F-H R-D  odd E-parity
  ([.F2, .R2, .F2, .R2, .U2, .F2], 6),  -- D-D - F-D R-H  odd E-parity
  ([.F2, .R2, .F2, .R2, .F2, .U2], 6),  -- R-V + F-V R-H  odd E-parity
  ([.R2, .U2, .R2, .U2, .F2, .R2, .U2], 7),  -- H-H - F-V R-H even E-parity
  ([.R2, .U2, .R2, .U2, .F2, .R2, .F2], 7),  -- F-D - F-H R-H  odd E-parity
  ([.R2, .U2, .R2, .F2, .R2, .U2, .R2], 7),  -- F-D + F-V R-H  odd E-parity
  ([.R2, .U2, .R2, .F2, .R2, .U2, .F2], 7),  -- H-H - F-V R-D  odd E-parity
  ([.R2, .U2, .R2, .F2, .R2, .F2, .U2], 7),  -- F-D - F-H R-D  odd E-parity
  ([.R2, .U2, .R2, .F2, .R2, .F2, .R2], 7),  -- D-D + F-H R-V even E-parity
  ([.R2, .U2, .F2, .R2, .U2, .R2, .F2], 7),  -- H-H + F-V R-H  odd E-parity
  ([.R2, .U2, .F2, .R2, .U2, .F2, .R2], 7),  -- R-D - F-V R-H  odd E-parity
  ([.R2, .U2, .F2, .R2, .F2, .U2, .R2], 7),  -- F-D + F-H R-H  odd E-parity
  ([.R2, .U2, .F2, .R2, .F2, .U2, .F2], 7),  -- H-H - F-D R-D  odd E-parity
  ([.R2, .U2, .F2, .R2, .F2, .R2, .U2], 7),  -- D-D - F-H R-D  odd E-parity
  ([.R2, .U2, .F2, .R2, .F2, .R2, .F2], 7),  -- R-V + F-D R-V even E-parity
  ([.R2, .F2, .U2, .R2, .F2, .U2, .F2], 7),  -- R-V + F-H R-D  odd E-parity
  ([.R2, .F2, .U2, .R2, .F2, .R2, .U2], 7),  -- F-D + F-D R-D  odd E-parity
  ([.R2, .F2, .U2, .F2, .U2, .R2, .F2], 7),  -- F-V - F-H R-H  odd E-parity
  ([.R2, .F2, .U2, .F2, .U2, .F2, .R2], 7),  -- R-V + F-H R-H  odd E-parity
  ([.R2, .F2, .U2, .F2, .R2, .U2, .R2], 7),  -- F-D - F-D R-H  odd E-parity
  ([.R2, .F2, .U2, .F2, .R2, .U2, .F2], 7),  -- H-H + F-H R-D  odd E-parity
  ([.R2, .F2, .R2, .U2, .R2, .U2, .R2], 7),  -- R-V - F-D R-V  odd E-parity
  ([.R2, .F2, .R2, .U2, .R2, .U2, .F2], 7),  -- D-D - F-H R-V  odd E-parity
  ([.R2, .F2, .R2, .U2, .R2, .F2, .U2], 7),  -- R-V + F-D R-V  odd E-parity
  ([.R2, .F2, .R2, .U2, .R2, .F2, .R2], 7),  -- H-H + F-V R-H even E-parity
  ([.R2, .F2, .R2, .U2, .F2, .R2, .U2], 7),  -- F-V + F-D R-V  odd E-parity
  ([.R2, .F2, .R2, .U2, .F2, .R2, .F2], 7),  -- H-H + F-V R-D even E-parity
  ([.R2, .F2, .R2, .F2, .U2, .R2, .F2], 7),  -- R-V + F-D R-D even E-parity
  ([.R2, .F2, .R2, .F2, .U2, .F2, .U2], 7),  -- F-D - F-V R-H  odd E-parity
  ([.R2, .F2, .R2, .F2, .R2, .U2, .R2], 7),  -- D-D - F-H R-V even E-parity
  ([.R2, .F2, .R2, .F2, .R2, .U2, .F2], 7),  -- F-V + F-D R-V even E-parity
  ([.R2, .F2, .R2, .F2, .R2, .F2, .U2], 7),  -- H-H + F-V R-V even E-parity
  ([.F2, .U2, .R2, .F2, .U2, .R2, .F2], 7),  -- F-D - F-H R-V  odd E-parity
  ([.F2, .U2, .R2, .F2, .U2, .F2, .R2], 7),  -- H-H + F-H R-V  odd E-parity
  ([.F2, .U2, .R2, .F2, .R2, .U2, .F2], 7),  -- R-D + F-H R-H  odd E-parity
  ([.F2, .U2, .R2, .F2, .R2, .F2, .U2], 7),  -- D-D + F-D R-H  odd E-parity
  ([.F2, .U2, .R2, .F2, .R2, .F2, .R2], 7),  -- F-V + F-V R-D even E-parity
  ([.F2, .U2, .F2, .U2, .R2, .F2, .U2], 7),  -- H-H - F-H R-V even E-parity
  ([.F2, .U2, .F2, .U2, .R2, .F2, .R2], 7),  -- R-D - F-H R-H  odd E-parity
  ([.F2, .U2, .F2, .R2, .F2, .U2, .R2], 7),  -- H-H - F-D R-V  odd E-parity
  ([.F2, .U2, .F2, .R2, .F2, .U2, .F2], 7),  -- R-D + F-H R-V  odd E-parity
  ([.F2, .U2, .F2, .R2, .F2, .R2, .U2], 7),  -- R-D - F-D R-H  odd E-parity
  ([.F2, .U2, .F2, .R2, .F2, .R2, .F2], 7),  -- D-D - F-V R-H even E-parity
  ([.F2, .R2, .U2, .R2, .U2, .R2, .F2], 7),  -- F-V + F-H R-H  odd E-parity
  ([.F2, .R2, .U2, .R2, .U2, .F2, .R2], 7),  -- R-V - F-H R-H  odd E-parity
  ([.F2, .R2, .U2, .R2, .F2, .U2, .R2], 7),  -- H-H + F-D R-H  odd E-parity
  ([.F2, .R2, .U2, .R2, .F2, .U2, .F2], 7),  -- R-D - F-H R-D  odd E-parity
  ([.F2, .R2, .U2, .R2, .F2, .R2, .U2], 7),  -- R-D + F-D R-D  odd E-parity
  ([.F2, .R2, .U2, .F2, .R2, .U2, .R2], 7),  -- F-V + F-D R-H  odd E-parity
  ([.F2, .R2, .F2, .U2, .R2, .F2, .U2], 7),  -- R-V + F-V R-D  odd E-parity
  ([.F2, .R2, .F2, .U2, .R2, .F2, .R2], 7),  -- H-H + F-D R-V even E-parity
  ([.F2, .R2, .F2, .U2, .F2, .U2, .R2], 7),  -- D-D + F-V R-H  odd E-parity
  ([.F2, .R2, .F2, .U2, .F2, .U2, .F2], 7),  -- F-V - F-V R-D  odd E-parity
  ([.F2, .R2, .F2, .U2, .F2, .R2, .U2], 7),  -- F-V + F-V R-D  odd E-parity
  ([.F2, .R2, .F2, .U2, .F2, .R2, .F2], 7),  -- H-H + F-H R-V even E-parity
  ([.F2, .R2, .F2, .R2, .U2, .R2, .U2], 7),  -- R-D - F-H R-V  odd E-parity
  ([.F2, .R2, .F2, .R2, .U2, .F2, .R2], 7),  -- F-V + F-D R-D even E-parity
  ([.F2, .R2, .F2, .R2, .F2, .U2, .R2], 7),  -- R-V + F-V R-D even E-parity
  ([.F2, .R2, .F2, .R2, .F2, .U2, .F2], 7),  -- D-D + F-V R-H even E-parity
  ([.R2, .U2, .R2, .U2, .F2, .R2, .U2, .R2], 8),  -- R-D - F-V R-D  odd E-parity
  ([.R2, .U2, .R2, .U2, .F2, .R2, .F2, .R2], 8),  -- F-D + F-H R-D even E-parity
  ([.R2, .U2, .R2, .F2, .R2, .U2, .F2, .R2], 8),  -- R-D - F-V R-H even E-parity
  ([.R2, .U2, .R2, .F2, .R2, .F2, .U2, .R2], 8),  -- F-D + F-H R-H even E-parity
  ([.R2, .U2, .R2, .F2, .R2, .F2, .U2, .F2], 8),  -- H-H - F-D R-D even E-parity
  ([.R2, .U2, .R2, .F2, .R2, .F2, .R2, .U2], 8),  -- D-D - F-H R-D even E-parity
  ([.R2, .U2, .F2, .R2, .U2, .R2, .F2, .R2], 8),  -- R-D + F-V R-D even E-parity
  ([.R2, .U2, .F2, .R2, .U2, .F2, .R2, .U2], 8),  -- R-V - F-D R-H  odd E-parity
  ([.R2, .U2, .F2, .R2, .U2, .F2, .R2, .F2], 8),  -- R-D + F-V R-H even E-parity
  ([.R2, .U2, .F2, .R2, .F2, .U2, .R2, .F2], 8),  -- H-H + F-D R-H even E-parity
  ([.R2, .U2, .F2, .R2, .F2, .U2, .F2, .U2], 8),  -- H-H - F-V R-V  odd E-parity
  ([.R2, .U2, .F2, .R2, .F2, .R2, .U2, .R2], 8),  -- F-V + F-H R-H even E-parity
  ([.R2, .U2, .F2, .R2, .F2, .R2, .U2, .F2], 8),  -- R-V - F-D R-D even E-parity
  ([.R2, .F2, .U2, .R2, .F2, .U2, .F2, .R2], 8),  -- R-V + F-H R-H even E-parity
  ([.R2, .F2, .U2, .R2, .F2, .R2, .U2, .R2], 8),  -- F-D - F-D R-H even E-parity
  ([.R2, .F2, .U2, .R2, .F2, .R2, .U2, .F2], 8),  -- H-H + F-H R-D even E-parity
  ([.R2, .F2, .U2, .F2, .U2, .R2, .F2, .R2], 8),  -- D-D + F-H R-D even E-parity
  ([.R2, .F2, .U2, .F2, .U2, .F2, .R2, .F2], 8),  -- D-D + F-D R-H even E-parity
  ([.R2, .F2, .U2, .F2, .R2, .U2, .R2, .U2], 8),  -- F-V - F-V R-H  odd E-parity
  ([.R2, .F2, .U2, .F2, .R2, .U2, .R2, .F2], 8),  -- H-H - F-H R-H even E-parity
  ([.R2, .F2, .U2, .F2, .R2, .U2, .F2, .R2], 8),  -- R-D + F-H R-H even E-parity
  ([.R2, .F2, .R2, .U2, .R2, .U2, .F2, .R2], 8),  -- F-V + F-H R-V even E-parity
  ([.R2, .F2, .R2, .U2, .F2, .R2, .U2, .R2], 8),  -- D-D - F-D R-V even E-parity
  ([.R2, .F2, .R2, .U2, .F2, .R2, .F2, .R2], 8),  -- R-D + F-V R-H  odd E-parity
  ([.R2, .F2, .R2, .F2, .U2, .R2, .F2, .U2], 8),  -- R-D + F-V R-V even E-parity
  ([.R2, .F2, .R2, .F2, .U2, .R2, .F2, .R2], 8),  -- R-V + F-D R-H  odd E-parity
  ([.R2, .F2, .R2, .F2, .U2, .F2, .U2, .R2], 8),  -- F-D + F-V R-D even E-parity
  ([.R2, .F2, .R2, .F2, .R2, .U2, .F2, .R2], 8),  -- D-D - F-D R-V  odd E-parity
  ([.R2, .F2, .R2, .F2, .R2, .F2, .U2, .R2], 8),  -- R-D + F-V R-V  odd E-parity
  ([.R2, .F2, .R2, .F2, .R2, .F2, .U2, .F2], 8),  -- F-D + F-V R-V  odd E-parity
  ([.F2, .U2, .R2, .F2, .U2, .R2, .F2, .U2], 8),  -- F-V - F-H R-D  odd E-parity
  ([.F2, .U2, .R2, .F2, .U2, .R2, .F2, .R2], 8),  -- F-D + F-H R-V even E-parity
  ([.F2, .U2, .R2, .F2, .U2, .F2, .R2, .F2], 8),  -- F-D + F-D R-V even E-parity
  ([.F2, .U2, .R2, .F2, .R2, .F2, .U2, .R2], 8),  -- F-V - F-D R-D even E-parity
  ([.F2, .U2, .F2, .U2, .R2, .F2, .U2, .F2], 8),  -- F-D - F-D R-V  odd E-parity
  ([.F2, .U2, .F2, .U2, .R2, .F2, .R2, .F2], 8),  -- R-D + F-D R-H even E-parity
  ([.F2, .U2, .F2, .R2, .F2, .U2, .R2, .F2], 8),  -- F-D - F-H R-V even E-parity
  ([.F2, .R2, .U2, .R2, .U2, .F2, .R2, .F2], 8),  -- D-D - F-D R-H even E-parity
  ([.F2, .R2, .U2, .R2, .F2, .U2, .F2, .U2], 8),  -- R-V - F-H R-V  odd E-parity
  ([.F2, .R2, .U2, .R2, .F2, .R2, .U2, .F2], 8),  -- R-D - F-H R-D even E-parity
  ([.F2, .R2, .F2, .U2, .R2, .F2, .U2, .R2], 8),  -- R-V + F-V R-H even E-parity
  ([.F2, .R2, .F2, .U2, .R2, .F2, .U2, .F2], 8),  -- D-D + F-V R-D even E-parity
  ([.F2, .R2, .F2, .U2, .R2, .F2, .R2, .F2], 8),  -- F-D + F-H R-V  odd E-parity
  ([.F2, .R2, .F2, .R2, .U2, .R2, .U2, .F2], 8),  -- R-D + F-D R-V even E-parity
  ([.F2, .R2, .F2, .R2, .U2, .F2, .R2, .U2], 8),  -- F-D + F-V R-V even E-parity
  ([.F2, .R2, .F2, .R2, .U2, .F2, .R2, .F2], 8),  -- F-V + F-H R-D  odd E-parity
  ([.F2, .R2, .F2, .R2, .F2, .U2, .R2, .F2], 8),  -- D-D + F-V R-D  odd E-parity
  ([.R2, .U2, .R2, .U2, .F2, .R2, .F2, .R2, .F2], 9),  -- H-H + F-D R-D  odd E-parity
  ([.R2, .U2, .R2, .F2, .R2, .U2, .F2, .R2, .U2], 9),  -- R-V - F-D R-H even E-parity
  ([.R2, .U2, .R2, .F2, .R2, .F2, .U2, .F2, .U2], 9),  -- H-H - F-V R-V even E-parity
  ([.R2, .U2, .R2, .F2, .R2, .F2, .R2, .U2, .F2], 9),  -- R-V - F-D R-D  odd E-parity
  ([.R2, .U2, .F2, .R2, .U2, .F2, .R2, .U2, .F2], 9),  -- D-D - F-H R-H even E-parity
  ([.R2, .U2, .F2, .R2, .U2, .F2, .R2, .F2, .U2], 9),  -- R-V + F-D R-H even E-parity
  ([.R2, .U2, .F2, .R2, .U2, .F2, .R2, .F2, .R2], 9),  -- H-H + F-V R-D  odd E-parity
  ([.R2, .U2, .F2, .R2, .F2, .U2, .F2, .U2, .R2], 9),  -- R-D - F-V R-V even E-parity
  ([.R2, .U2, .F2, .R2, .F2, .U2, .F2, .U2, .F2], 9),  -- F-D - F-V R-V even E-parity
  ([.R2, .F2, .U2, .R2, .F2, .R2, .U2, .R2, .U2], 9),  -- F-V - F-V R-H even E-parity
  ([.R2, .F2, .U2, .R2, .F2, .R2, .U2, .R2, .F2], 9),  -- H-H - F-H R-H  odd E-parity
  ([.R2, .F2, .U2, .F2, .U2, .R2, .F2, .R2, .F2], 9),  -- R-V + F-D R-D  odd E-parity
  ([.R2, .F2, .U2, .F2, .U2, .F2, .R2, .F2, .R2], 9),  -- F-V - F-D R-D  odd E-parity
  ([.R2, .F2, .R2, .F2, .U2, .R2, .F2, .U2, .R2], 9),  -- H-H + F-V R-V  odd E-parity
  ([.R2, .F2, .R2, .F2, .U2, .R2, .F2, .U2, .F2], 9),  -- R-D - F-V R-V  odd E-parity
  ([.R2, .F2, .R2, .F2, .U2, .R2, .F2, .R2, .F2], 9),  -- D-D + F-H R-H even E-parity
  ([.R2, .F2, .R2, .F2, .R2, .U2, .F2, .R2, .F2], 9),  -- R-V - F-H R-V even E-parity
  ([.R2, .F2, .R2, .F2, .R2, .F2, .U2, .F2, .U2], 9),  -- F-V + F-D R-D  odd E-parity
  ([.F2, .U2, .R2, .F2, .U2, .R2, .F2, .R2, .U2], 9),  -- F-V + F-H R-D even E-parity
  ([.F2, .U2, .R2, .F2, .U2, .R2, .F2, .R2, .F2], 9),  -- H-H + F-D R-V  odd E-parity
  ([.F2, .U2, .F2, .R2, .F2, .U2, .R2, .F2, .U2], 9),  -- F-V - F-H R-D even E-parity
  ([.F2, .R2, .F2, .R2, .U2, .F2, .R2, .U2, .R2], 9),  -- F-D - F-V R-V  odd E-parity
  ([.R2, .U2, .R2, .F2, .R2, .U2, .F2, .R2, .U2, .F2], 10),  -- D-D - F-H R-H  odd E-parity
  ([.R2, .U2, .F2, .R2, .U2, .F2, .R2, .F2, .U2, .F2], 10)  -- D-D + F-H R-H  odd E-parity
]

end DRBound
