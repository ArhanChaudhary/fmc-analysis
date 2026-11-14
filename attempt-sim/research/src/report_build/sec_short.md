## 1. The short version

**Again, this is a draft.** Everything below rests on time costs that are my first guesses (section 4), and section 11 checks which answers survive halving or doubling each one. All comparisons are attempt by attempt on the same {{V:test_n}} uniformly random scrambles, which no plan was tuned on. *Score* counts a DNF as 30, *mean* leaves DNFs out, and *−0.02* means 0.02 moves better than the tuned plan.

**What's new**

- **Three tweaks to the guides' plan are worth about a quarter of a move.** The baseline is the hour the way the guides describe it (section 3.2). Each tweak on its own, on held-out scrambles (appendix A has the table):
  - Only work an RZP state if your read says it's a DR of 10 or less, not 11.5: {{V:r2d_e5_read_max_10}}.
  - Keep 7 minutes to write the solution, not 5: {{V:r2d_e4_reserve420}}, and DNFs go from {{V:r2_base_dnf}}% to {{V:r2_reserve_dnf}}%.
  - Be as happy to switch as to stay on the same side: {{V:r2d_e5_switch_pen_0}}.

  All three together make the *tuned plan*: mean {{V:ref_mean}}, against {{V:base_mean}} for the baseline. The baseline is {{V:base_minus_ref}} moves worse on score.
- **Once the plan is sensible, the time split barely matters.** Stop writing EOs anywhere from minute 3 to 12, stop looking for DRs anywhere from minute 25 to 40: every combination is within 0.03 moves of the tuned plan's score, and {{V:e1_within}} of the {{V:e1_n}} splits I tried are within 0.02. It's pretty flat on both ends too: stopping the DR search at 15 or at 50 costs {{V:dd_te5_t_dr_900}} and {{V:dd_te5_t_dr_3000}}. The one split that really costs is writing EOs until minute 16 ({{V:dd_te1_teo960_tdr2100}} to {{V:dd_te1_teo960_tdr3000}}), and so does stopping the DR search at 45 or 50 after a long EO phase (section 6).
- **What matters is how much you look at, not when.** Against the tuned plan:

  | Change | Score − tuned plan, moves |
  |---|---:|
  | finish only the best DR | {{V:d_te5_fin_max_1}} |
  | finish at most 4 DRs | {{V:d_te5_fin_max_4}} |
  | no RZP, only DRs you see straight from the EO | {{V:d_te5_rzp_per_eo_0}} |
  | 1 RZP state per short EO (the tuned plan does 3) | {{V:d_te5_rzp_per_eo_1}} |
  | 8 RZP states per short EO | {{V:d_te5_rzp_per_eo_8}} |
  | one route per DR (the tuned plan does 4) | {{V:d_te5_htr_per_dr_1}} |
  | 8 routes per DR | {{V:d_te5_htr_per_dr_8}} |
  | never switch | {{V:d_te5_switch_pen_99}} |
  | read cut-off 8 | {{V:d_te5_read_max_8}} |
  | read cut-off 12 | {{V:d_te5_read_max_12}} |

  So: finish every DR you think can beat what you've got, give each one 3 or 4 routes, and work every RZP state your read likes (no cap past 8 matters), plus a couple per 5-mover: with that last bit the score against the tuned plan is {{V:edge_best_d}} (section 6). The read cut-off has a pretty sharp sweet spot, 9.5 to 10 with these costs.
- **Depth first doesn't help, and adapting to the scramble doesn't add anything you can measure.**
  - Depth first all the way (each EO straight to DR, each DR straight to a finish): {{V:d_te2_dfs}}.
  - Every rule that reacts to the scramble (lots of EOs or few, a short DR early or none, a result already in hand) is within 0.01 of the fixed plan, except the ones that keep searching too long (sections 7, 8).
  - Picking the best plan per scramble type on training scrambles gains {{V:pertype_shortest}} on new ones, about what the single best tweak gives on every scramble (section 8).

  The fixed plan kind of adapts already, though. Its minutes are when priorities change, not hard walls, so if you run out of DRs to look at you just go back to the EOs.
- **Playing safe for ≤ 22 costs nothing.** Try one route right away on any DR that looks like 22 or better, and write the 22 down: {{V:d_te4_quick22p5_r1}} on score, {{V:dle22_te4_quick22p5_r1}} points of ≤ 22. Writing down the first solution you find is a different story, {{V:dd_te4_bankfirst_rr180}}, because the rewrite eats time (section 9).
- **How the result scales with time.** Tuned plan, mean by length of the attempt: 20 minutes 23.07, 30 minutes 22.48, an hour {{V:ref_mean}}, two hours 21.52 (section 10). Being twice as fast at every step gives exactly the two-hour result. Twice as fast plus a sharper read plus better DR vision gets you {{V:top_mean}}.

**How solid is this?** Section 11 reruns every comparison with each time cost halved and doubled. The how-much-you-look-at answers keep their verdict in pretty much every run, and so does the tuned plan's win over the baseline. Two things depend on you: the read cut-off (a much noisier read wants 9, not 10) and the time you keep for writing (if your step times swing a lot, keep 10 minutes, not 7). The single cost that moves the result most is how accurate your read of an RZP state is.

**What it confirms or corrects**

- **The top's mean is about 21.9, not 20-21.** The five best official means since 2024 average {{V:real_t5_mean}} over {{V:real_t5_n}} attempts, and Yura Riabov's 2025 log says 21.99. The baseline lands close, {{V:cal_mean}} on random scrambles. The simulated results are more bunched up than real ones though: fewer sub-20s and fewer 24s (section 5).
- **The guides' split holds up.** 5-10 minutes on EOs and up to 30-35 minutes looking for DRs (Yura Riabov's *Hitchhiker's Guide to FMC*), Lichi Fang's 7+28+25 and Tom Nelson's 10/25/25 are all in the flat part of section 6.
