## 6. How long on each step

From here on everything is compared against the tuned plan from section 1 (the baseline plus read cut-off 10, 7 minutes kept for writing, and switching as happily as staying). What a tuned-plan attempt looks like on average, over the held-out scrambles: {{V:ref_eos}} EOs written, {{V:ref_rzp}} RZP states worked, {{V:ref_drs}} DRs written and {{V:ref_fin}} taken to a finish with {{V:ref_routes}} routes tried. That's {{V:ref_m_eo}} minutes finding and writing EOs, {{V:ref_m_dr}} looking for DRs, {{V:ref_m_fin}} finishing and {{V:ref_m_write}} writing the solution. The DR of the result was written at minute {{V:ref_t_res_dr}} on average, and its finish found at minute {{V:ref_t_res_sol}}.

**The split between EOs, DRs and finishing.** Each row is the minute EO writing stops, each column the minute the DR search stops (finishing gets the rest), and each cell the score against the tuned plan, which stops at 8 and 35:

{{T:r3_e1_grid}}

Everything from 3 to 12 minutes of EOs and 25 to 40 minutes of DR search is within 0.03 moves. Writing EOs until minute 16 costs, and more so with a late DR stop: it leaves too little for finishing. So for Tzak's "at what time do people settle and work on some 2c4 vs trying for more drs" ([[D12301]]) and DRCubeur's "Is stopping checking EOs at a certain time even if I'm not finished worth it?" ([[D16707]]): with these costs anything from minute 25 to 40 is as good as anything else, and yes, stopping EO writing at minute 8-12 costs nothing.

**How many EOs.** No time limit on writing, a cap on the number written. Each row is a cap:

{{T:r3_e5_eo_cap}}

**How long an EO.** Each row is the longest EO looked for:

{{T:r3_e5_eo_len}}

EOs of 4 or less are nearly as good as EOs of 5 here. A likely reason, not measured separately: the plan works only one RZP state per 5-mover (section 3.2), so the 5-movers add few DRs.

**How many RZP states per EO.** Each row is the number of RZP states worked per EO of 4 or less:

{{T:r3_e5_rzp_per_eo}}

After how many DRs you finish, this is the steepest curve of the hour: 0 or 1 state per EO loses a lot. Going past 3 still gains a little, and 8 was the best value in this sweep, so I ran a second sweep past it, picked on the training scrambles and reported on the held-out ones:

{{T:edge}}

Past 8 it's flat. At that point the read cut-off is what decides which states you work, not the per-EO cap, so in practice it means "work every RZP state whose read looks good enough". What does still help is giving the 5-movers 2 RZP states instead of 1: {{V:edge_best}} scores {{V:edge_best_d}} against the tuned plan. So the tuned plan isn't the end of the road; that's just the best version I've measured so far.

**When the DR search stops**, with nothing else changed. Each row is the minute:

{{T:r3_e5_t_dr}}

**How many routes per DR.** Each row is the number of routes from the subset's checklist (htr-routes) tried on a DR:

{{T:r3_e5_htr_per_dr}}

**How many DRs to finish.** The solver takes DRs to a finish in order of expected total, skipping any whose chance of beating the best so far is under 3%. Each row is a cap on how many:

{{T:r3_e5_fin_max}}

With no cap the tuned plan finishes {{V:ref_fin}} DRs on average. Capping at 4 already costs {{V:dd_te5_fin_max_4}}. "of those 1-3 are usually what i work on" (Yura Riabov, [[D8423]]) is in the range where the cap costs a lot here. To be fair, a real solver's 1-3 are picked by a much sharper eye than the simulator's (section 12).

## 7. Breadth first or depth first

*Breadth first* is the guides' order and the tuned plan's: all EOs, then the DRs, then the finishes. *Depth first* takes each EO straight to a DR and each DR straight to a finish. In between are the quick looks: one route at once on a DR that promises a good result, and a backup (the best DR finished early, so there is something on the sheet). Each row is a plan:

{{T:r3_e2}}

Depth first is a little worse, {{V:d_te2_dfs}}. The runs don't say why. My guess: time spent finishing early DRs is time you don't spend finding the better DR that shows up later. The quick look at a promising DR comes out level with the tuned plan, and so do early backups. With 7 minutes kept for writing you almost never end with nothing on the sheet, so a backup doesn't buy much. Section 9 has the backup's other job, the safety of a result in hand.

## 8. Adapting to the scramble

Rules that change the plan by what the attempt shows: how many EOs turned up, whether a short DR came early, whether a result is already in hand. Each row is a plan:

{{T:r3_e3}}

Nothing beats the fixed plan by more than the noise. The rules that lose are the ones that search longer once a result is in hand (a 23 on the sheet, DR search to minute 50), and they lose for the same reason as a late DR stop in section 6. Two things are behind the flat result:

- The fixed plan's minutes are priorities, not walls: a solver who runs out of EOs to look at moves on, and one with nothing left to finish goes back to look for more. So a scramble rich in EOs already gets more EO time, and one with few EOs already gets less.
- The decisions that do matter (section 6) are about how much to look at per EO and per DR, not about when, and those don't depend much on the scramble.

What about a different plan for each kind of scramble? I took every plan of round 3 and picked the best one per scramble type on the training scrambles (bad edges on the best axis, rich or poor in EOs, shortest EO, number of EOs of 4 or less), then played each type's pick on the held-out scrambles:

{{T:pertype}}

So yeah, it helps a little, but only about as much as the best single tweak does on every scramble: 8 RZP states per short EO alone is {{V:d_te5_rzp_per_eo_8}}. Most of the picks *are* that tweak, and the training gains shrink a lot on new scrambles (that's just picking the luckiest plan out of 237). The one pick that looks like a real *adapt to the scramble* rule is on the hard ones (shortest EO 5 or more, or no axis with 4 bad edges or fewer): write DRs up to 12 instead of 11. That makes sense, a 12-move DR is worth having when nothing better is coming, but it's a small group and the gain isn't separately significant.

## 9. At most 22: the safety plan

The question is how to raise the share of attempts at 22 or better, and what it costs in mean. JTuu asked it from the other end: "when you have let's say 21 safety with 20 mins or so to look for better, anyone have advice for knowing when you should squeeze the 21 harder vs widen your search and prune very aggressively? I feel like I frequently do the wrong one" ([[D9642]]). Each row is a plan:

{{T:r3_e4}}

- **The time you keep for writing *is* the safety.** Below 4:30 the DNF rate shoots up: the last step before the reserve can run long, and so can the writing itself (section 4). Six or seven minutes is the sweet spot here, and 10 costs a little.
- **The quick look plus a written 22** raises ≤ 22 by {{V:dle22_te4_quick22p5_r1}} points for {{V:d_te4_quick22p5_r1}} in score: so the safe plan is actually slightly the better plan too.
- **Writing down every result at once** costs a little ({{V:d_te4_bankalways}}), and **writing down the first result** a lot ({{V:d_te4_bankfirst_rr180}}). In the model a rewrite takes as long as the first write, so writing early only pays off when you'd otherwise lose the result.
- **Committing early** (DR search stops at minute 25, a 22 written down) is level with the tuned plan.

None of these runs isolates JTuu's case, a 21 in hand with 20 minutes left. What they do say is general: spreading routes over more DRs beats squeezing one (8 routes per DR costs {{V:dd_te5_htr_per_dr_8}} over the hour, finishing fewer DRs costs more, section 6), and searching longer once a result is in hand doesn't pay (section 8).

## 10. How the result scales

**With the length of the attempt.** The same two plans, with the clock set to other lengths (2,000 held-out scrambles each; the policy's minutes scale with the length). Each row is a length:

{{T:r4_budget}}

Going from 30 minutes to an hour is worth 0.6 of a move, and from one hour to two about 0.35. The tuned plan beats the baseline at every length, mostly by not DNFing.

**With the solver.** The same plans for a faster or sharper solver. Each row is a solver:

{{T:r4_solver}}

Every step twice as fast is exactly the same as two hours: in the model, speed and time are the same thing. A read of an RZP state that is twice as sharp is worth about as much as 15 extra minutes. With all three together the tuned plan averages {{V:top_mean}}, with {{V:top_sub20}}% sub-20, still short of the real top 5's 7.4% sub-20. So what caps the simulator is its toolbox (section 12), not its clock.

**One decision at a time.** The read cut-off: work an RZP state only if its read promises a DR of at most this many moves. Each row is a cut-off:

{{T:r3_e5_read_max}}

The sweet spot is sharp, 9.5 to 10. Go lower and you skip states that would've given good DRs. Go higher and you burn time on states that rarely give a DR worth finishing. A switch: how much worse a look on the other side is ranked than one on the same side. Each row is a penalty:

{{T:r3_e5_switch_pen}}

Never switching costs {{V:dd_te5_switch_pen_99}}. Appendix A has the other one-at-a-time curves.
