## 10. Hand checklists, graded

I translate each checklist into route classes as closely as the route names allow and grade it on the same sample: the share of DRs where its steps so far find an optimal finish, and a finish within +1, with HTRs at most two over the shortest (budget 2), and with no HTR limit. Steps that depend on how many setup moves come before a trigger are graded as their whole route class, which flatters them a little. Sampled, {= n(25000) =} per subset × edges.

**Zagros's 4b2 order** ([[D15884]]): "1. check shortest HTR on normal by settings up to triggers and reasonable extensions", "2. check more linear 2qt HTRs by just reducing to 4a1 and doing the HTR even if it's long", "3. check shortest 4qt htr on normal if like <9 moves exists", "5. write shortest regressions to 2c3 2e or 4e", and on to "8. if it is seriously my only DR and I have nothing, try 2+2 HTRs". Steps 1 and 2 are graded together; 6 (the inverse) and 7 are already inside the others, since both sides are always graded. The last two columns take each step's HTR limit as Zagros stated it: none on steps 1 and 2 ("even if it's long"), under 9 moves on step 3, budget 2 on the rest. Each row is a step; each cell is the cumulative share of 4b2 DRs found after it:

{{grade_zagros}}

Zagros: "if I simply follow the system I have in my mind for each subset without getting distracted then it just produces optimal in 15 minutes like 80% of the time" ([[D15885]]). Done fully on 4b2 with near-shortest HTRs, it finds the optimal on {= GR('Zagros 4b2 order (D15884)', 5, 'cumulative_opt_htr_budget2') =} and +1 on {= GR('Zagros 4b2 order (D15884)', 5, 'cumulative_p1_htr_budget2') =}; with the HTR limits as Zagros stated them, on {= GR('Zagros 4b2 order (D15884)', 5, 'cumulative_opt_stated') =} and +1 on {= GR('Zagros 4b2 order (D15884)', 5, 'cumulative_p1_stated') =}; with HTRs of any length on every step, on {= GR('Zagros 4b2 order (D15884)', 5, 'cumulative_opt') =}. Zagros's 80% is about real attempts, where time is the limit, so I can't check it here, but nothing in the numbers contradicts it. After the first, the step that adds the most is table step {= BIGSTEP('Zagros 4b2 order (D15884)')[0] =} (Zagros's step 5, the regression to 2c3), {= BIGSTEP('Zagros 4b2 order (D15884)')[1] =} points.

**4b2 4e: regress to 2c3 first, or reduce to 1q first?** The thread:

- Yura Riabov ([[D6409]], [[D6411]], [[D6412]]): "4b2 4e is basically the best 4q subset", go to 2c3 "if it's not 1-2 moves to trigger", "i also try 2-3 moves to 4a1 and niss trace if i don't forget to do that".
- rogo asked whether it shouldn't be the other way round ([[D6422]]): "the first approach apart from R U2 F2 R to check should still be 'reduce to 1qt 4e and niss trace for short htrs' i think?"
- Adri agreed the label was the confusing part ([[D6424]]): "I agree that's why calling it the best 4qt subset seems confusing".
- Jay ([[D6439]]): "if you think of this subset as one where you only try to solve with U R2 F2 U, you're gonna miss optimal the vast majority of the time".

Asked "do you go to 2c3 2e or 4e or both", Yura Riabov answered "whatever is shortest" ([[D6414]], [[D6415]]), so step 2 is the regression to 2c3 2e or 4e. Yura's order, with the first step as a trigger with at most two setup moves (the setup limit is Yura's "1-2 moves"); each row is a step, each cell a cumulative share of 4b2 4e:

{{grade_yura}}

The other start, reducing to 1q and NISS-tracing, is DR bounding. On 4b2 4e, one row per start, share finding the optimal (budget-2 HTRs for the routes; bounding on 4,000 states, section 8):

| Start | Optimal found |
|---|---|
| Yura Riabov's first two steps (a ceiling, see below) | {= GR('Yura 4b2 4e order (D6409-D6416)', 2, 'cumulative_opt_htr_budget2') =} |
| every reduction to 1q of at most 3 moves | {= pc(Q8('4b2 4e', '1', '3', 'found_opt')) =} |
| every reduction to 1q of at most 4 moves | {= pc(Q8('4b2 4e', '1', '4', 'found_opt')) =} |
| every reduction to 1q of at most 5 moves | {= pc(Q8('4b2 4e', '1', '5', 'found_opt')) =} |

Yura also kept the setup short ("doing more than 1 half turn before reduction isn't worth it", [[D6416]]), which the route can't see, so {= GR('Yura 4b2 4e order (D6409-D6416)', 2, 'cumulative_opt_htr_budget2') =} is a ceiling for the order as stated. So the regression to 2c3 beats every reduction up to 4, and is a little behind every reduction up to 5 (about {= n(round(float(Q8('4b2 4e', '1', '5', 'mean_reductions_le_R')))) =} of them). The 4a1 switch adds {= f1(float(GR('Yura 4b2 4e order (D6409-D6416)', 3, 'cumulative_opt_htr_budget2').rstrip('%')) - float(GR('Yura 4b2 4e order (D6409-D6416)', 2, 'cumulative_opt_htr_budget2').rstrip('%'))) =} points after it. Jay is right too: the 2qt trigger alone (with at most two setup moves) finds {= GR('Yura 4b2 4e order (D6409-D6416)', 1, 'cumulative_opt_htr_budget2') =}. On 4b2 4e every optimal uses 4 quarter turns on {= E['claims']['C40']['evidence'].split('4qt ')[1].rstrip('.') =} of states, as Yura Riabov's [*Hitchhiker’s Guide to HTR*](https://docs.google.com/document/d/1_NMlyPh2Ifd1E0ivos-15Sp-by-KPxoOsj9JD4pJuHI) says ("it’s optimal with 4q more than half of the time").

Fanti's split ([[D10034]]; read off *allcases*, as Fanti said the next day: "i took the stats from here", [[D10038]]): "40% of opt 4b2 4e solutions use 2qt, 45% regress to 2c3", "only about 8% go to 0c0 2e/4e". Read as a checklist in that order, one row per step, cumulative shares of 4b2 4e:

{{grade_fanti}}

**Lewis Isom's 4a2 0e/2e list** ([[T6743]]): "1) Linear 2qt HTRs on both sides. This means the first qt makes 4a1 4e.", "2) Write down all the +1's and +2's to 4a1 4e, and NISS them.", then the U M2 U checks, the regression to 4c3, and to 0c3. One row per step, cumulative shares of 4a2 0e and 2e pooled:

{{grade_lewis}}

Levi Gibson's reply for 4a2 0e, "you don’t have to try reductions to 4a1 4e because the average optimal solution length for that path is like 17.2 to slice" ([[T6744]]), fits. On 4a2 0e one optimal picked at random is a 2qt path on only {= E['claims']['C42']['evidence'].split('is 2qt ')[1].split(' ')[0] =} of states, and steps 1 and 2 together find the optimal on {= GR('Lewis 4a2 0e/2e list (T6743)', 2, 'cumulative_opt_htr_budget2') =} of 4a2 0e and 2e pooled. After the first, the step that adds the most is step {= BIGSTEP('Lewis 4a2 0e/2e list (T6743)')[0] =} ({= BIGSTEP('Lewis 4a2 0e/2e list (T6743)')[2] =}, {= BIGSTEP('Lewis 4a2 0e/2e list (T6743)')[1] =} points). Next is step 4, the 4b3 regression with the switch, which is the first route of my 4a2 0e and 2e checklists.

**Jay's and rodneykinney's 3qt 2c0e checks.** Jay counted "11 total things" to check for every two half turns followed by a quarter turn ([[T328]]); rodneykinney: "I would count 9 cases" ([[T333]]), and later, with "some mind-bending inverse-prediction gymnastics", "You can check just F and R2 F" ([[T336]], [[T337]]). As a route class (one qt to 4b2 4e, switch, then 4a1 and HTR, any setup) it finds the optimal on {= GR('Jay/rodney 2c3 0e checks (T328-T344)', 1, 'cumulative_opt_htr_budget2') =} of 2c3 0e and +1 on {= GR('Jay/rodney 2c3 0e checks (T328-T344)', 1, 'cumulative_p1_htr_budget2') =}. The setup counts themselves aren't graded.

**Daichi's cheat sheet** ([[D18340]]), every listed route of each subset × edges together, against my checklist. Two rows need reading. The 0c4 row is "all: 4b2 switch (2e could be linear, except for 0c4 8e)", and the 2e there is the 4b2's, as in the next row ("all: 4b2 switch (prioritize 2e over 4e)" for 4c4) and in Daichi's "like, 0c4 says just check 4b2 switches" ([[D18330]]); so on 0c4 0e to 6e a linear route through 4b2 2e counts as well. The 4c3 row, "all: 3q, but always switch after 4b2 4e (except for the 4a3 0/4e 8 move trigger I think?)", is graded without the bracket. With it, counting linear routes through 4b2 4e on the 4a3 side with an HTR of 8 or less, 4c3 0e goes from {= GR('Daichi cheat sheet (D18340): 4c3 0e', 1, 'cumulative_opt_htr_budget2') =} to {= GR('Daichi cheat sheet with the 4a3 8-move trigger (D18340): 4c3 0e', 1, 'cumulative_opt_htr_budget2') =} and 4c3 4e from {= GR('Daichi cheat sheet (D18340): 4c3 4e', 1, 'cumulative_opt_htr_budget2') =} to {= GR('Daichi cheat sheet with the 4a3 8-move trigger (D18340): 4c3 4e', 1, 'cumulative_opt_htr_budget2') =}.

Daichi built the sheet from short finishes: "it's to filter routes to check rather than DRs itself, based on the sub13 DR route stats" ([[D18343]]). So the last two columns grade it on the DRs with an optimal of 12 or less, against the same first three routes of mine (chosen on all DRs). Each row is a subset × edges: the share where the sheet's routes find the optimal (or +1), the share of my first three routes and how many of my routes it takes to match the sheet, then the sheet and my first three on optimal ≤ 12 only, all with budget-2 HTRs unless the column says otherwise:

{{grade_daichi}}

The sheet against my first three, from those columns. *Level* means under {= str(int(E['daichi_level_pts'])) =} point apart, or within two standard errors of the difference on the same DRs. The sample has fewer short DRs on some subsets, so those rows are rougher: under 1,000 per subset × edges on {= E['daichi_n12']['small_text'] =}, and as few as {= n(E['daichi_n12']['min']) =} on {= E['daichi_n12']['min_at'] =}. Each row is a verdict, each cell the subsets × edges that get it:

| Sheet is | DRs with an optimal of 12 or less | All DRs |
|---|---|---|
| ahead | {= E['daichi_cmp']['le12']['ahead'] =} | {= E['daichi_cmp']['all']['ahead'] =} |
| level | {= E['daichi_cmp']['le12']['level'] =} | {= E['daichi_cmp']['all']['level'] =} |
| behind | {= E['daichi_cmp']['le12']['behind'] =} | {= E['daichi_cmp']['all']['behind'] =} |
