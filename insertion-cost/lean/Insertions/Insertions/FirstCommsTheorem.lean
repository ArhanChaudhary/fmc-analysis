import Insertions.FirstComms
/- The theorem of `FirstComms.lean`, in a file of its own so that it runs the compiled definitions. -/

namespace Insertions

/-- First comms per spot, for every state of every type two corner 3-cycles make: 5c 5, 3c3c 2, 3c1t 9 (both twist
directions), 2c2c 24 (twisted and pure), 3c 54, 3tc 18 (both directions), 2tc 108 (and every 3-cycle for the solved
state).  Each type has one value only, so the count is the same at every spot and for every leftover of the type. -/
theorem first_comms_per_spot : first_comms_by_type () =
    [([(5, 0)], [5], 108864), ([(3, 0), (3, 0)], [2], 90720), ([(3, 1), (1, 2)], [9], 5040),
     ([(3, 2), (1, 1)], [9], 5040), ([(2, 2), (2, 1)], [24], 3780), ([(2, 0), (2, 0)], [24], 1890),
     ([(3, 0)], [54], 1008), ([(1, 1), (1, 1), (1, 1)], [18], 56), ([(1, 2), (1, 1)], [108], 56),
     ([(1, 2), (1, 2), (1, 2)], [18], 56), ([], [1008], 1)] := by native_decide

end Insertions
