## 12. What this does not model

The simulated solver is a DR solver with a fixed toolbox. Here's what it leaves out, roughly in order of how much I think it matters:

- **Finishes outside the DR group.** No DR-breaking finishes, no leave-slice skeleton with an insertion, no blockbuilding. Real sub-20s often come from these; it is the main reason the simulated results spread less than real ones (section 5).
- **EOs of 6 moves or more, RZPs of more than 3 moves, DRs not through a written EO.** The search space is the one the guides describe; a solver who goes further has more to find and more to spend time on.
- **Variations of a DR beyond the last quarter turn.** The solver tries routes on the DR and on its twin (the last quarter turn made the other way), not on other DRs of the same RZP.
- **How a route is searched.** A route tried gives the best finish along it or nothing, in a fixed time. In reality some routes take seconds and some take minutes, and a finish one move worse is often found first.
- **The reading of an RZP state** is the exact distance blurred by symmetric noise. Real reads are biased per case (some DRMs look better than they are), and better solvers have a sharper and less biased read.
- **Mistakes**: miswritten moves, a wrong scramble, a solution that fails the check, a slip that costs ten minutes. The only DNF in the simulator is the clock.
- **Learning within the attempt.** The solver doesn't get faster on a scramble it knows, or use a written solution as a shorter scramble (Jay's trick, [[D10362]]).
- **Nerves and competition.** The pace varies from attempt to attempt, but there's no panic at the 30-minute call and no difference between home and comp, which people do describe: Dunni, "in comp as soon as 30 minutes is called put panic mode starts" ([[D13474]]), and Yura Riabov playing it safer in comp ([[D10379]]).
- **The solver is one person.** The costs are one set of numbers for a top solver; a 24-average solver is not just a slower version (they also see less, and that is a different column of section 4).
