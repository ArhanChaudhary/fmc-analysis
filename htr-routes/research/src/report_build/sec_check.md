## 4. The checklists, subset by subset

This is the main table. There's a checklist for every subset × edges, not just per corner subset, because the bad-edge count changes which routes are good (how much is measured below). Sampled, {= n(25000) =} states per subset × edges. Brackets are the part after the NISS switch, and a route ends at HTR (`0c0`). All 8 routes with their cumulative shares at the optimum and at +1, plus the no-limit lists, are in appendix A.

Each row is a subset × edges and the first three routes of its budget-2 checklist, in the order to try them:

{{checklist_edges}}

How far those routes get, same rows: the share of DRs where the first 1, 2, 3 or 5 routes find an optimal finish, and where the first three find a finish within +1:

{{checklist_edges_shares}}

The hardest row is 4a2 0e ({= BUD('4a2 0e', '2', 3) =} after three routes). Where the edge count changes the order, and by how much, is next.

**What the edge count is worth.** Take the checklist built for the subset × edges itself, and the corner subset's list with edge counts pooled (the pooled table further down), and run both on the same DRs. The difference is what knowing the DR's bad-edge count buys you. Averaged over all DRs, each subset × edges weighted by its real frequency, the own list is ahead by this many percentage points (own list's share minus pooled list's share):

| Target | Own list ahead after 1 route (points) | After 2 routes | After 3 routes | After 5 routes |
|---|---|---|---|---|
| Optimal | {= EGA('opt', 1) =} | {= EGA('opt', 2) =} | {= EGA('opt', 3) =} | {= EGA('opt', 5) =} |
| Within +1 | {= EGA('p1', 1) =} | {= EGA('p1', 2) =} | {= EGA('p1', 3) =} | {= EGA('p1', 5) =} |

Small on average, because the edge counts where it matters are mostly the rare ones. Inside a corner subset it can be a lot more. Each row is a corner subset at the step where the gap is largest:

| Corner subset | Own list ahead by (points) | After |
|---|---|---|
| 4a2 | {= EGC('4a2', 'opt', 1) =} | 1 route |
| 4a1 | {= EGC('4a1', 'opt', 2) =} | 2 routes |
| 2c3 | {= EGC('2c3', 'opt', 1) =} | 1 route |
| 0c0 | {= EGC('0c0', 'opt', 1) =} | 1 route |

Every subset × edges where the own list gains at least a point somewhere (optimal or +1, after 1, 2, 3 or 5 routes). Each row is one subset × edges; the last four columns are how many more DRs out of 100 its own checklist finds the optimal on than the pooled one, after that many routes:

{{edge_gain}}

*Pooled list's first route: place in own list* is where the pooled list's first route lands in the subset × edges list (computed to 60 routes). The same rows within +1, own minus pooled, in points:

{{edge_gain_p1}}

And the shares the gains come from, own list and pooled list on the same DRs (share finding the optimal after that many routes):

{{edge_gain_shares}}

A gain of +0.0 means both lists are equal up to that route; a small negative one means the pooled order happens to be ahead (greedy isn't optimal). Gains under a point or so are within what fitting the own list to the same {= n(25000) =} states gives you anyway.

Where knowing the edge count changes what to try first. Each row is a subset × edges; the two share columns are the DRs where the own list and the pooled list find the optimal after that many routes:

| Subset × edges | Own list starts with | After | Own list finds the optimal | Pooled list finds the optimal | Note |
|---|---|---|---|---|---|
| 0c0 0e | `0c0 > 4a1 > 0c0`, then {= BUD('0c0 0e', '2', 2, 'class') =} (the DR is already HTR) | 2 routes | {= EGR('0c0 0e', 2) =} | {= EGR('0c0 0e', 2, 'pooled') =} | the pooled order never tries it |
| 0c0 6e | {= EGF('0c0 6e') =}, switching before the last qt | 1 route | {= EGR('0c0 6e', 1) =} | {= EGR('0c0 6e', 1, 'pooled') =} | pooled first route is only {= EGRANK('0c0 6e') =}th here |
| 0c0 8e | the same switch first | 1 route | {= EGR('0c0 8e', 1) =} | {= EGR('0c0 8e', 1, 'pooled') =} | |
| 2c4 0e | linear, {= EGF('2c4 0e') =} | 1 route | {= EGR('2c4 0e', 1) =} | {= EGR('2c4 0e', 1, 'pooled') =} | pooled switches at 2c3 |
| 2c3 0e | switch at 4b2, {= EGF('2c3 0e') =} | 1 route | {= EGR('2c3 0e', 1) =} | {= EGR('2c3 0e', 1, 'pooled') =} | |
| 2c3 6e | the same | 1 route | {= EGR('2c3 6e', 1) =} | {= EGR('2c3 6e', 1, 'pooled') =} | |
| 2c3 8e | the same | 1 route | {= EGR('2c3 8e', 1) =} | {= EGR('2c3 8e', 1, 'pooled') =} | |
| 4a2 0e | the 4b3 regression {= EGF('4a2 0e') =} | 1 route | {= EGR('4a2 0e', 1) =} | {= EGR('4a2 0e', 1, 'pooled') =} | |
| 4a2 2e | the same | 1 route | {= EGR('4a2 2e', 1) =} | {= EGR('4a2 2e', 1, 'pooled') =} | |
| 4a2 4e | linear, {= EGF('4a2 4e') =} | 3 routes | {= EGR('4a2 4e', 3) =} | {= EGR('4a2 4e', 3, 'pooled') =} | |
| 4a1 0e | {= EGF('4a1 0e') =} | 3 routes | {= EGR('4a1 0e', 3) =} | {= EGR('4a1 0e', 3, 'pooled') =} | pooled first route is {= EGRANK('4a1 0e') =}th |
| 4a1 4e | the 1qt route {= EGF('4a1 4e') =} | 2 routes | {= EGR('4a1 4e', 2) =} | {= EGR('4a1 4e', 2, 'pooled') =} | |
| 4a1 2e | the pooled first route, but a different third | 3 routes | {= EGR('4a1 2e', 3) =} | {= EGR('4a1 2e', 3, 'pooled') =} | |

On 2c3 2e and 4e the linear route stays first. On 4a2 the pooled first route, {= EGF('4a2 0e', 'pooled_first') =}, is first on none of the three edge counts.

Where it doesn't matter: on 2c5, 0c3, 0c4, 4c3, 4c4 and 4b2 the first route is the same for every edge count, and the own list gains at most {= EGMAX(('2c5', '0c3', '0c4', '4c3', '4c4', '4b2')) =} points at any step. The pooled list is fine there, and on 2c4 2e to 8e too.

**Pooled over edges.** One list per corner subset, edge counts pooled by their real frequency, as a summary. Each row is a corner subset and its first three budget-2 routes:

{{checklist_corner}}

The shares, same rows: the DRs where the first 1, 2, 3 or 5 routes find the optimal, where the same three find a finish within +1, and for comparison three routes with no limit on HTR length:

{{checklist_corner_shares}}

How to read a row, with 4c3 (the pooled row; 4c3 2e and 4e start the same way). Try `4a3 > 4b2 > (4a1 > 0c0)` first: on the 4a3 side, one qt to 4b2, switch, and on the other side 4a1 and HTR. The same moves read the other way round are its mirror, `4b3 > 4a2 > 4a1 > (0c0)`: start on the 4b3 side, qt to 4a2, qt to 4a1, switch for the last qt. Every split of a finish has a mirror like this, and the table names both. As classes they aren't the same, since each also collects other finishes (only {= n(E['alias_pairs'][1]) =} of {= n(E['alias_pairs'][0]) =} mirror pairs cover exactly the same states), so the share is for the reading named first. With HTRs up to two over the shortest, that route alone finds the optimal on {= BUD('4c3', '2', 1) =} of 4c3. Then the b side, `4b3 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)`, then the regression through 2c3 on the a side. The b-side route through 4a2 read linearly, `4b3 > 4a2 > 4a1 > 0c0`, is fifth.

There are more in the [worked examples](examples.html); here's one, replayed:

```
{= WIT('W01', 'scramble') =} // 4c3 4e, {= WIT('W01', 'optimal') =} optimal
{= WIT('W01', 'normal_moves') =} // first route, normal
({= WIT('W01', 'inverse_moves') =}) // then inverse, HTR in {= WIT('W01', 'htr_length') =}
```

What the pooled table says, subset by subset. Each row is a corner subset, the share where its budget-2 checklist finds the optimal after that many routes, and what those routes are:

| Corner subset | Optimal found | After | What to try |
|---|---|---|---|
| 0c3 | {= BUD('0c3', '2', 3) =} | 3 routes | `4a2 4e`, then switch |
| 0c4 | {= BUD('0c4', '2', 3) =} | 3 routes | `4a3 > 4b2`, switch |
| 2c4 | {= BUD('2c4', '2', 3) =} | 3 routes | down the 2c chain to 2c3, switch at 2c3 (or one step earlier), or linear |
| 2c5 | {= BUD('2c5', '2', 3) =} | 3 routes | the same |
| 4b5 | {= BUD('4b5', '2', 3) =} | 3 routes | the same |
| 4c3 | {= BUD('4c3', '2', 5) =} | 5 routes | the first route does most of the work |
| 4c4 | {= BUD('4c4', '2', 5) =} | 5 routes | the same |
| 2c3 | {= BUD('2c3', '2', 5) =} | 5 routes | the same |
| 0c0 | {= BUD('0c0', '2', 8) =} | 8 routes | the optimal is spread over many routes |
| 4a1 | {= BUD('4a1', '2', 8) =} | 8 routes | the same |
| 4b2 | {= BUD('4b2', '2', 8) =} | 8 routes | the same |

- **0c3, 0c4, 2c4, 2c5, 4b5** are the easy ones for a checklist, and the routes are what Daichi's cheat sheet says.
- **4c3, 4c4, 2c3** need four or five routes for 80%.
- **4b2, 4a1, 0c0** are where checklists struggle, and where bounding does better (section 8). On 4b2 the 2qt route `4b2 > 4a1 > 0c0` comes first but alone finds only {= BUD('4b2', '2', 1) =}; the regressions through 2c3 come next.
- **Within +1** the same three routes reach {= ', '.join(f"{pc(SAMEF(g, '2', 3))} on {g}" for g in G12 if SAMEF(g, '2', 3) < 0.9) =}, and 90% or more on the other {= sum(1 for g in G12 if SAMEF(g, '2', 3) >= 0.9) =}. If you only need a finish within one move of optimal, three routes are enough nearly everywhere. (At +1 a route counts if any of its finishes within +1 has an HTR within the budget, which may be shorter than on its optimal finishes.)

**The budget.** The same checklists built for budget 0 (only the shortest HTRs), 1, 2 and no limit. Each row is a corner subset; each cell is the share where the first route finds the optimal with that budget:

{{budgets_1}}

The same after three routes:

{{budgets_3}}

With only the shortest HTRs, no subset gets past {= p0(max(BUDF(g, '0', 3) for g in G12)) =} with three routes: you have to write HTRs one or two moves longer than the shortest. With no limit, the first route alone covers most states. That's the *every route works if you allow the HTR to be long* effect of section 3, not a reason to try only one route.

**Cheap and marginal routes.** After the third route, each further route adds at most {= f1(E['marg_after3_max'] * 100) =} points, and less than 3 points in {= pc(E['marg_after3_share_lt3']) =} of the checklists (subsets × edges and corner subsets, budget 2). Routes 4 to 8 only pay at the margin. If you have time for more on 0c0, 4a1 and 4b2, a second DR or bounding (section 8) is probably the better use of it.

**Edge counts along the route.** It also matters how often you go through, say, 4b2 4e rather than 4b2 2e. Every state on a route has its own bad-edge count (counted as for the subset × edges groups), so a corner route splits into edge paths. From 2c3 2e, `2c3 > 4b2 > 4a1 > 0c0` is one of

```
2c3 2e > 4b2 2e > 4a1 4e > 0c0
2c3 2e > 4b2 4e > 4a1 4e > 0c0
```

Below, a DR *can pass* an intermediate subset if some route (after a qt, before HTR) that finds its optimal with budget 2 goes through it. One DR can pass several, so the edge columns add up to more than 100%. First the reverse view, over all DRs. Each row is an intermediate subset and a target: the share of DRs that can pass it, then, of those, the share that can pass it with each edge count.

{{edge_via_reverse}}

In short. Each row is an intermediate subset; each cell is the share, of the DRs that can pass it at all, that can pass it with that edge count:

| Intermediate subset | 0e | 2e | 4e | 6e |
|---|---|---|---|---|
| 4b2 | {= ESR('4b2', '0e') =} | {= ESR('4b2', '2e') =} | {= ESR('4b2', '4e') =} | |
| 4a1 | {= ESR('4a1', '0e') =} | {= ESR('4a1', '2e') =} | {= ESR('4a1', '4e') =} | |
| 4a2 | {= ESR('4a2', '0e') =} | {= ESR('4a2', '2e') =} | {= ESR('4a2', '4e') =} | |
| 2c3 | {= ESR('2c3', '0e') =} | {= ESR('2c3', '2e') =} | {= ESR('2c3', '4e') =} | {= ESR('2c3', '6e') =} |
| 4c3 | {= ESR('4c3', '0e') =} | {= ESR('4c3', '2e') =} | {= ESR('4c3', '4e') =} | |

So the 4b2 you go through is mostly 4b2 2e, the 4a1 before HTR is 4a1 4e, the 4a2 is 4a2 4e, 2c3 is split, and 4c3 is 2e or 4e about equally.

Per starting subset × edges, the share that can pass each intermediate subset at all, then per edge count, is in appendix A (one table per intermediate subset). What you can take from it, one row per starting subset × edges:

| From | Mostly through | Share that can pass it | Other edge count | Share that can pass it |
|---|---|---|---|---|
| 2c3 2e | 4b2 2e | {= ESV('2c3 2e', '4b2 2e') =} | 4b2 4e | {= ESV('2c3 2e', '4b2 4e') =} |
| 2c3 0e | 4b2 4e | {= ESV('2c3 0e', '4b2 4e') =} | 4b2 2e | {= ESV('2c3 0e', '4b2 2e') =} |
| 2c3 8e | 4b2 4e | {= ESV('2c3 8e', '4b2 4e') =} | 4b2 2e | {= ESV('2c3 8e', '4b2 2e') =} |
| 2c4 0e | 2c3 4e | {= ESV('2c4 0e', '2c3 4e') =} | 2c3 2e | {= ESV('2c4 0e', '2c3 2e') =} |
| 2c4 8e | 2c3 4e | {= ESV('2c4 8e', '2c3 4e') =} | 2c3 2e | {= ESV('2c4 8e', '2c3 2e') =} |
| 0c4 8e | 4b2 2e | {= ESV('0c4 8e', '4b2 2e') =} | 4b2 4e | {= ESV('0c4 8e', '4b2 4e') =} |
| 4b2 4e, regressing | 2c3 4e | {= ESV('4b2 4e', '2c3 4e') =} | 2c3 2e | {= ESV('4b2 4e', '2c3 2e') =} |
| | | | 2c3 6e | {= ESV('4b2 4e', '2c3 6e') =} |

From 0c4 in general the 4b2 is mostly 4b2 2e; 0c4 8e is the example in the table.

**Do edge paths make a better checklist?** No. An edge path lies inside its corner route, so a list of edge paths finds less per route; what it shows is how far a corner route is spread over edge paths. Built the same way (greedy, budget 2, per subset × edges). Each row is a kind of list; each cell is the share of all DRs where it finds the optimal:

| List | 1 route | 3 routes |
|---|---|---|
| Edge paths | {= ESA('opt', 'edge', 0) =} | {= ESA('opt', 'edge', 2) =} |
| Corner routes | {= ESA('opt', 'corner', 0) =} | {= ESA('opt', 'corner', 2) =} |

The first edge path is a piece of the first corner route (or its mirror) on {= E['es']['all']['opt']['n_same_first'] =} of {= E['es']['n'] =} subset × edges (not on {= ', '.join(ESL(lambda v: not v['first_same_corner'])) =}), so it doesn't change what to try. How many edge paths it takes to find everything the first corner route finds:

- **one**, on {= ESM(1) =} subset × edges ({= ', '.join(ESL(lambda v: v['match1'] == 1)) =}): there the corner route effectively is one edge path;
- **two**, on {= ESM(2) =};
- **up to eight**, on {= ', '.join(ESL(lambda v: v['match1'] == 8)) =}. There the first corner route is spread over many edge paths, and aiming for one edge count at each step would cost you most of it.

So check the corner route and take whatever edge count you land on. The edge-path checklists themselves, eight routes per subset × edges, are in appendix A, **computer only**: an answer key, not a list to check in an attempt.

Two more replayed examples, the first route on 2c4 and the 4b2 regression. The first is a no-limit instance: its HTR of {= WIT('W02', 'htr_length') =} is longer than budget 2 allows on that DR.

```
{= WIT('W02', 'scramble') =} // 2c4 4e, {= WIT('W02', 'optimal') =} optimal
({= WIT('W02', 'inverse_moves') =}) // inverse: 2c4 to 2c3
{= WIT('W02', 'normal_moves') =} // then normal
```

```
{= WIT('W03', 'scramble') =} // 4b2 4e, {= WIT('W03', 'optimal') =} optimal
{= WIT('W03', 'normal_moves') =} // to 2c3, switch
({= WIT('W03', 'inverse_moves') =}) // then inverse
```

**The last DR move** shifts every route about equally and changes no checklist (section 7).
