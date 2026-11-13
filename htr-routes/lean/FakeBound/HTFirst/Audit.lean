/- HTFirst.Audit — axioms of the theorems behind the reference table "Half turns before the first quarter turn".
   `propext`, `Classical.choice`, `Quot.sound` are Lean's three standard axioms; an axiom named
   `<theorem>._native.native_decide.ax_…` is what `native_decide` adds: "the compiled program said true". -/
import HTFirst.Examples
namespace HTFirst
#print axioms bridge_checked
#print axioms htr_count
#print axioms fewest_qt
#print axioms fewest_qt_value
#print axioms half_turn_keeps
#print axioms quarter_turn_by_one
#print axioms no_extra_qt_lowers
#print axioms first_qt_floor
#print axioms not_ready_no_qt_first
#print axioms mem_finishes
#print axioms table_run
#print axioms data_parse_ok
#print axioms examples_optimal
#print axioms examples_all_finishes
#print axioms examples_replay
#print axioms examples_lowering
#print axioms recount_rows
#print axioms recount_size
end HTFirst
