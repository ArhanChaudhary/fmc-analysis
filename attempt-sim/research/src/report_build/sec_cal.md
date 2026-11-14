## 5. The baseline against real results

The real yardstick is the WCA export: the five solvers with the best official mean since 2024 (at least 40 attempts each), {{V:real_t5_n}} attempts. Their mean is {{V:real_t5_mean}}, not 20-21: 20-21 is a good mean of 3, not where the best solvers sit over many attempts. Yura Riabov's own log of 138 attempts from 2025 ([*FMC Jan-May 2025*](https://docs.google.com/spreadsheets/d/1Cb7M3KqB5W99sSNOIKLG3xqZ-k58koIexTLahUiPNhs/edit?usp=sharing), posted [[D12481]]) says the same: 21.99.

The baseline policy with the costs of section 4 lands within about a tenth of a move of them. One row per group of attempts; the simulator is run on random scrambles and, separately, on exactly the scrambles of the top 5's attempts (each scramble as many times as they had it):

{{T:cal_dist}}

The mean and the DNF rate are close. The spread isn't: the simulated solver has about a third as many sub-20s and a bit over half as many 24s or worse. Result by result, as a share of each group's attempts:

{{T:cal_hist}}

The simulated results pile up at 22 and 23. What it lacks at the good end is the finishes it can't make (section 12: DR-breaking finishes, insertions, other methods) and luck beyond the DR group; at the bad end, the mistakes it can't make (miswritten moves, ten minutes lost to a wrong scramble). So **read every ≤ 22 and sub-20 share on this page as a comparison between plans, not as a forecast of your own rate.** The differences between plans are what the runs measure well.

Does the simulator know which scrambles are hard? On the same scramble the real result and the simulated one go together, with correlation {{V:cal_corr}} ± {{V:cal_corr_se}} over {{V:cal_pairs}} attempts. Grouped by what the simulator got on the scramble, the top 5's mean on those same scrambles:

{{T:cal_same}}

The real solvers do better on the scrambles the simulator finds hardest than the simulator does, which fits the same picture: when the DRs are poor, a real solver has other ways out.

What the simulated attempt looks like, on average over the 4,000 scrambles (the real figures are Yura Riabov's log, and the sheets quoted in section 4):

| What | Simulated, per attempt | Real |
|---|---|---|
| EOs written | {{V:cal_eos}} | 40 checked per attempt, median (Yura Riabov's log, 138 attempts); 39 in the FMC League comments |
| RZP states worked | {{V:cal_rzp}} | Tom Nelson's league comments: 28 RZPs, median |
| switches | {{V:cal_sw}} | "I never plan on having time to switch more than 10" (Zagros, [[D14350]]) |
| DRs written (11 moves or less) | {{V:cal_drs}} | "i write down maybe 5 per attempt on average" (Yura Riabov, [[D8421]]); "20+ every  attempt" counting the ones seen and not written (Zagros, [[D8418]]) |
| DRs taken to a finish | {{V:cal_fin}} | "of those 1-3 are usually what i work on" (Yura Riabov, [[D8423]]); "2-3 DRs with corners worth considering" (wen, [[T495]]) |
| routes tried | {{V:cal_routes}} | |
| length of the result's DR, moves | {{V:cal_dr_len}} | 9.96 (Yura Riabov's log); 9.71 (the sub-22 official means) |
| finish optimal from its DR, % of results | {{V:cal_opt_from_dr}} | 0.38 moves missed from the DR on average (Yura Riabov's log) |
| minute the result's DR was written | {{V:cal_t_res_dr}} | |
| minute the result's finish was found | {{V:cal_t_res_sol}} | |
| minutes finding and writing EOs | {{V:cal_m_eo}} | "5-10 minutes: searching for and writing out eos" (*Hitchhiker's Guide to FMC*) |
| minutes glancing at EOs, working RZPs, writing DRs | {{V:cal_m_dr}} | "Up to 30-35 minutes: checking eos and searching for DR" (the same) |
| minutes reading DRs, trying routes, writing out finishes | {{V:cal_m_fin}} | "Until the end of the solve: solving the best dr" (the same) |
| minutes writing the solution down | {{V:cal_m_write}} | |
