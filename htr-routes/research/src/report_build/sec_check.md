## 4. The checklists, subset by subset

This is the main table. For each corner subset (edge counts pooled by their real frequency): the first three routes of the budget-2 checklist, the share of DRs where the routes so far find an optimal finish after 1, 2, 3 and 5 routes, the share where the same three find a finish within +1, and, for comparison, three routes with no limit on HTR length. Sampled, {= n(25000) =} states per subset × edges; brackets are the part after the NISS switch; a route ends at HTR (`0c0`).

{{checklist_corner}}

How to read a row, with 4c3: try `4a3 > 4b2 > (4a1 > 0c0)` first: on the 4a3 side, one qt to 4b2, switch, and on the other side 4a1 and HTR. The same moves read the other way round are its mirror, `4b3 > 4a2 > 4a1 > (0c0)`: starting on the 4b3 side, qt to 4a2, qt to 4a1, switch for the last qt. Every split of a finish has such a mirror, and the table names both; as classes they are not the same (each also collects other finishes, and only {= n(E['alias_pairs'][1]) =} of {= n(E['alias_pairs'][0]) =} mirror pairs cover exactly the same states), so the share is for the reading named first. With HTRs up to two over the shortest that route alone finds the optimal on {= BUD('4c3', '2', 1) =} of 4c3. Then the b side: `4b3 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)`, then the regression through 2c3 on the a side. The b-side route through 4a2 read linearly, `4b3 > 4a2 > 4a1 > 0c0`, is fifth. An example is in the [worked examples](examples.html) and this one: the 4c3 4e reached by `{= WIT('W01', 'scramble') =}` is {= WIT('W01', 'optimal') =} optimal, and the first route finds it as `{= WIT('W01', 'normal_moves') =}` on normal, then `({= WIT('W01', 'inverse_moves') =})` on inverse, HTR in {= WIT('W01', 'htr_length') =} (replayed).

What the table says, subset by subset, in words:

- **0c3, 0c4, 2c4, 2c5, 4b5** are the easy ones for a checklist: three routes cover {= BUD('0c3', '2', 3) =}, {= BUD('0c4', '2', 3) =}, {= BUD('2c4', '2', 3) =}, {= BUD('2c5', '2', 3) =} and {= BUD('4b5', '2', 3) =}. 0c3: `4a2 4e` then switch. 0c4: `4a3 > 4b2`, switch. 2c4, 2c5, 4b5: down the 2c chain to 2c3, switch at 2c3 (or one step earlier), or linear. This is what Daichi's cheat sheet says.
- **4c3, 4c4, 2c3** need four or five routes for 80% ({= BUD('4c3', '2', 5) =}, {= BUD('4c4', '2', 5) =}, {= BUD('2c3', '2', 5) =} after five); the first one does most of the work.
- **4b2, 4a1, 0c0** are where checklists struggle: the optimal is spread over many routes, and eight routes stop at {= BUD('0c0', '2', 8) =} (0c0), {= BUD('4a1', '2', 8) =} (4a1), {= BUD('4b2', '2', 8) =} (4b2). These are the subsets where bounding does better (section 8). On 4b2 the 2qt route `4b2 > 4a1 > 0c0` comes first but alone finds only {= BUD('4b2', '2', 1) =}; the regressions through 2c3 come next.
- **Within +1** the same three routes reach {= ', '.join(f"{pc(SAMEF(g, '2', 3))} on {g}" for g in G12 if SAMEF(g, '2', 3) < 0.9) =}, and 90% or more on the other {= sum(1 for g in G12 if SAMEF(g, '2', 3) >= 0.9) =}. If you only need a finish within one move of optimal, three routes are enough nearly everywhere. (At +1 a route counts if any of its finishes within +1 has an HTR within the budget, which may be shorter than on its optimal finishes.)

**The budget.** The same checklists built for budget 0 (only the shortest HTRs), 1, 2 and no limit, after 1 and 3 routes:

{{budgets}}

With only shortest HTRs, no subset gets past {= p0(max(BUDF(g, '0', 3) for g in G12)) =} with three routes: you have to write HTRs one or two moves longer than the shortest. With no limit, the first route alone covers most states: that is the *every route works if you allow the HTR to be long* effect of section 3, not a reason to try only one route.

**Cheap and marginal routes.** After the third route, each further route adds at most {= f1(E['marg_after3_max'] * 100) =} points, and in {= pc(E['marg_after3_share_lt3']) =} of the checklists (subsets × edges and corner subsets) less than 3 points (budget 2). Routes 4 to 8 pay only at the margin, so if you have time for more, a second DR or bounding (section 8) is likely the better use of it on 0c0, 4a1 and 4b2.

**By edges.** The checklist for each subset × edges, first three routes (all 8 routes with their cumulative shares at the optimum and at +1, and the no-limit lists, are in appendix A):

{{checklist_edges}}

Where the edges change the order: 4a2 0e and 2e start with the 4b3 regression (`4a2 > 4b3 > 4a2 > 4a1 > (0c0)`), 4a2 4e with the 2qt route; 4a1 0e with the 0c0 route and a switch, 4a1 2e through 4b2, 4a1 4e with the 1qt route; 2c4 0e linear, the other 2c4 with a switch at 2c3. The hardest row is 4a2 0e ({= BUD('4a2 0e', '2', 3) =} after three routes).

Two examples of the first route on 2c4 and of the 4b2 regression, both replayed (the first is a no-limit instance: its HTR of {= WIT('W02', 'htr_length') =} is longer than budget 2 allows on that DR): the 2c4 4e of `{= WIT('W02', 'scramble') =}` ({= WIT('W02', 'optimal') =} optimal) is found by `({= WIT('W02', 'inverse_moves') =})` on inverse (2c4 to 2c3), then `{= WIT('W02', 'normal_moves') =}` on normal; the 4b2 4e of `{= WIT('W03', 'scramble') =}` ({= WIT('W03', 'optimal') =} optimal) by `{= WIT('W03', 'normal_moves') =}` (to 2c3), switch, then `({= WIT('W03', 'inverse_moves') =})`.

**The last DR move** shifts every route about equally and changes no checklist (section 7).
