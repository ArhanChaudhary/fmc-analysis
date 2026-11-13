## 8. DR bounding

The method of Levi Gibson's *DR Bounding* doc: "1. Find many reductions to the 1qt 4c4e subset … 2. For each case, create a lower bound of how good the solution can be … 3. Start checking the 1qt cases from best to worst … 4. Once you find a solution, cross off all the 1QT cases that can not be solved in less moves than the solution you found." rodneykinney's *Advanced DR Bounding* sharpens the bounds and adds 2qt.

What I measure here is the method's ceiling. Write every reduction to 1q of at most R moves (on normal, on inverse, or split between them, section 3) and finish each reduced state optimally, with however many quarter turns that takes: how often is one of them the optimal finish of the DR, and how many reductions is that? The search over reductions is exact. Reductions are counted the way a solver writes them (each side's sequence empty or ending in a quarter turn), exactly, by table. Sampled: the first 4,000 states per subset × edges; shares have standard errors of at most {= f1(E['q8_se_max_corner'] * 100) =} points per corner subset.

Each row is a subset; each cell is the share of DRs where some reduction to 1q of at most R moves leads to an optimal finish:

{{bounding}}

How many reductions that is, the mean number of reductions of at most R moves per DR, same rows. The counts come from a counting table, not from writing the reductions out; the table equals a brute-force enumeration of every pair of sequences up to 5 moves on 4,800 states, and up to 7 moves on 520 (40 of 0c0, and 10 of every subset × edges), so every column is checked on every subset.

{{bounding_counts}}

Other targets, same rows: a finish within +1 with reductions of at most 4; a finish of 12 or better with reductions of at most 5 (for DRs that have one); and reductions to 2q of at most 3 moves, with how many there are:

{{bounding_other}}

What it says:

**Which subsets suit it depends on R.** Each row is a subset; each cell is the share where bounding finds the optimal:

| Subset | R ≤ 4 | R ≤ 6 |
|---|---|---|
| 0c0 | {= pc(Q8('0c0', '1', '4', 'found_opt')) =} | {= pc(Q8('0c0', '1', '6', 'found_opt')) =} |
| 4a2 | {= pc(Q8('4a2', '1', '4', 'found_opt')) =} | {= pc(Q8('4a2', '1', '6', 'found_opt')) =} |
| 4a1 | {= pc(Q8('4a1', '1', '4', 'found_opt')) =} | {= pc(Q8('4a1', '1', '6', 'found_opt')) =} |
| 4b2 | {= pc(Q8('4b2', '1', '4', 'found_opt')) =} | {= pc(Q8('4b2', '1', '6', 'found_opt')) =} |
| 2c3 | {= pc(Q8('2c3', '1', '4', 'found_opt')) =} | {= pc(Q8('2c3', '1', '6', 'found_opt')) =} |

So at R ≤ 6, 4a1, 4b2 and 2c3 overtake 4a2. On 2c5 and 4b5 no reduction of 5 or less reaches 4a1 4e at all (it takes at least 6), and 4c4 and 2c4 are close to that.

**Each extra move of reduction costs a lot.** The number of reductions grows {= f1(E['q8_growth'][0]) =} to {= f1(E['q8_growth'][1]) =} times from 5 to 6 moves. The mean number of reductions per DR, over all DRs:

| | R ≤ 4 | R ≤ 5 | R ≤ 6 |
|---|---|---|---|
| Reductions on average | {= n(round(float(Q8('all', '1', '4', 'mean_reductions_le_R')))) =} | {= n(round(float(Q8('all', '1', '5', 'mean_reductions_le_R')))) =} | {= n(round(float(Q8('all', '1', '6', 'mean_reductions_le_R')))) =} |

With the bounds doing their job you only finish a few of them, but you still write them, and NISS-trace them.

**2q needs much shorter reductions.** At most 3 moves to a 2q state reaches the optimal on {= pc(Q8('all', '2', '3', 'found_opt')) =} of all DRs, against {= pc(Q8('all', '1', '3', 'found_opt')) =} for 1q. But each 2q state still needs its own finish found by hand, and that's the hard part bounding at 1q avoids.

**Within +1** is much easier: at most 4 moves gives a finish within +1 on {= pc(Q8('all', '1', '4', 'found_p1')) =} of DRs.

**The one-quarter-turn reading** (the reduction, then a finish with exactly one quarter turn, which is what JTuu's simulation counted) finds less. Each row is a subset; each cell is the share where some reduction of at most 4 finds the optimal, read each way:

| Subset | One-qt finish | Any finish |
|---|---|---|
| 2c3 | {= pc(E['q8w']['2c3|1|4']['found_opt']) =} | {= pc(Q8('2c3', '1', '4', 'found_opt')) =} |
| 4b2 | {= pc(E['q8w']['4b2|1|4']['found_opt']) =} | {= pc(Q8('4b2', '1', '4', 'found_opt')) =} |

**Against the checklists.** How often does bounding find the optimal per subset, and how many reductions does that take? Here's the smallest R for which bounding finds the optimal on 80% of a subset, with the reductions that is, against how many routes the checklist of section 4 needs for 80%, one row per corner subset:

{{bounding_vs_checklist}}

Bounding gets to 80% with short reductions on 0c0 (3) and 4a1 (5), and to about 80% on 4a2 (5: {= pc(Q8('4a2', '1', '5', 'found_opt')) =}, on the line in every population of section 12). Those are where the budget-2 checklist struggles (0c0 and 4a1 stop short of 80% after eight routes). On 4b2 bounding needs every reduction up to 6, about {= n(round(float(Q8('4b2', '1', '6', 'mean_reductions_le_R')))) =} of them, where the checklist stops at {= BUD('4b2', '2', 8) =}. On 2c4, 2c5, 4b5, 0c3, 0c4, 4c3 and 4c4 one to five routes reach 80%, and bounding needs 6 or 7 moves of reduction or doesn't get there by 7. A route and a reduction aren't the same amount of work, so this only compares them in kind.

**For a human the bounding column is mostly out of reach.** Each extra move of reduction multiplies the reductions by about eight, and in an attempt you write tens, maybe a couple of hundred (R ≤ 4 is about {= n(round(float(Q8('all', '1', '4', 'mean_reductions_le_R')))) =} on average). So only the 0c0 entry (R = 3, about {= n(round(float(Q8('0c0', '1', '3', 'mean_reductions_le_R')))) =} reductions) is a practical recommendation. Every entry with R of 5 or more, thousands of reductions, is **computer only**: it shows where the optimal lies, not how to find it. Plan an attempt with the R ≤ 4 column of the first table above.

**Levi Gibson's verdicts per subset.** After "lots and lots of solves" ([[T7074]]): "0c0: Yes", "4a2: yes yes yes amazing muah chief's kiss", for 4a1 "if you get a 4a1 case randomly, bound it. Otherwise it's not great. For the 2e/6e case it's not great because you 99% of the time you want to find a 0c0 or 4b2 trigger", for 4b2 "just check the really short ones, and then just try triggers for the rest", for 2c3 "I only use it for the 6e subset now. Triggers will get you optimal usually for 2e and 4e", and "Bounding is actually REALLY good for 4c3". Row by row, bounding with every reduction of at most 4 and 5 moves against the first three and five budget-2 routes (4,000 states per subset × edges for bounding, 25,000 for the routes). Each row is a subset × edges; each cell is the share where that method finds the optimal:

{{bound_vs_routes_edges}}

Levi Gibson's verdicts against those rows, one row per corner subset:

| Subset | Verdict | Why |
|---|---|---|
| 0c0 | **agrees** | bounding is far ahead on every edge count |
| 4a2 | **agrees on 0e** | bounding finds {= CELL('bound_vs_routes_edges', '4a2 0e', 'Bounding, R ≤ 4') =} against {= CELL('bound_vs_routes_edges', '4a2 0e', 'Checklist, 3 routes') =} on 0e; the routes are a little ahead on 2e and level on 4e |
| 4a1 | **agrees** | on 4a1 4e (the case Levi Gibson would bound) bounding finds nearly every optimal; on 0e and 2e the routes are as good or better |
| 4b2 | **partly** | on 4b2 0e and 2e bounding with reductions of 4 already beats three routes, so it's worth writing more than the really short reductions; on 4b2 4e the routes are ahead |
| 2c3 | **agrees for 2e and 4e** (routes ahead), **not for 6e** | the routes are ahead on 6e too |
| 4c3 | **does not agree** | the routes are ahead on every edge count, by {= f1(min(float(CELL('bound_vs_routes_edges', s, 'Checklist, 3 routes').rstrip('%')) - float(CELL('bound_vs_routes_edges', s, 'Bounding, R ≤ 5').rstrip('%')) for s in ('4c3 0e', '4c3 2e', '4c3 4e'))) =} points or more against reductions of 5 |

On 4c3, Levi Gibson's reason was the b side ("On the b corners side there are sooooo many finecky ways to reduce to 4a1 in very few moves"); these numbers count both sides together.

**Levi Gibson's 75 to 80%.** Asked how many reductions to check, Levi Gibson wrote "I like to check all sub-5 reductions. This can be done super quick and gets optimal like 75% of the time, and it gets optimal +1 the rest of the time", then "If I REALLY want to solve a DR optimally I'll check all sub-6 reductions" ([[D9108]]), "sub-5" being "4 or less" ([[D9221]]). Later, asked "Would it be around 80 percent?" ([[D9208]]): "yeah something like that I'd guess" ([[D9209]]), "for 2c3 that is" ([[D9210]]), adding "The only thing it really misses is a bunch of half turns into a 5-move trigger, so check that in addition to bounding" ([[D9212]]). The subsets Levi Gibson named for full bounding were 4a2 and 2c3 ("I don't use it fully for any subsets other than 4a2 and 2c3", [[D9113]]). Bounding alone, every reduction of at most R moves. Each row is a target and R; each cell is the share of the subset's DRs where it is found:

| | 2c3 | 4a2 |
|---|---|---|
| Optimal, R ≤ 4 | {= pc(Q8('2c3', '1', '4', 'found_opt')) =} | {= pc(Q8('4a2', '1', '4', 'found_opt')) =} |
| Optimal, R ≤ 4, 2c3 2e only | {= pc(Q8('2c3 2e', '1', '4', 'found_opt')) =} | |
| Reductions on average, R ≤ 4 (a count, not a share) | {= n(round(float(Q8('2c3', '1', '4', 'mean_reductions_le_R')))) =} | {= n(round(float(Q8('4a2', '1', '4', 'mean_reductions_le_R')))) =} |
| Within +1, R ≤ 4 | {= pc(Q8('2c3', '1', '4', 'found_p1')) =} | {= pc(Q8('4a2', '1', '4', 'found_p1')) =} |
| Optimal, R ≤ 5 | {= pc(Q8('2c3', '1', '5', 'found_opt')) =} | {= pc(Q8('4a2', '1', '5', 'found_opt')) =} |

On 4a2 the 75% holds (Levi Gibson had just written "for the 4a2 subset I use full DR Bounding", [[D9106]]), but within +1 it's only the share in the *Within +1* row, not every DR. For 2c3 both halves are off for bounding alone: the optimal comes from a reduction of 4 or less on under half of 2c3, and on {= pc(1 - float(Q8('2c3', '1', '4', 'found_p1'))) =} not even +1 does. Yura Riabov expected that split in the same exchange: "i think it could be very good for 4a2 but for 2c3 trigger knowledge covers most cases" ([[D9112]]), and of 2c3 2e, "<3 half turns> U R2 U R2 U <5 half turns> often enough, and bounding won't catch that i think" ([[D9116]]). Levi Gibson agreed ("missing lots of half turns into a trigger is the blind spot that DR Bounding has", [[D9118]]) and does add the triggers ("For 2c3 2e and 4e I do full DR Bounding + checking the 5-move triggers, and that seems to catch everything", [[D9117]]); I haven't measured that combination. There's an example in the errata: a 2c3 2e where the best any reduction of at most 4 gives is +2.

**JTuu's simulation** for Kai Cui's question ([[T5733]]): 2,000 2c3 2e states with Tzak's definitions, "4 move reduction to 4c4e just means you can strip off <=4 moves total from either end and be left with a single qt" ([[T5742]]) and "7 move linear htr means if you drop 7 moves on either end, are you left with just half turns" ([[T5743]]). That's the one-quarter-turn reading. JTuu's result ([[T5744]]) against mine on uniform 2c3 2e states, same definitions. Each row is an option; JTuu's column is quoted, mine is the share of DRs:

| Option | JTuu | Uniform 2c3 2e |
|---|---|---|
| linear HTR in 7 | "946/2000 (47.30%)" | {= E['claims']['C26']['evidence'].split('(linear alone ')[1].split(',')[0] =} |
| 4a1 in 4 | "1071/2000 (53.55%)" | {= E['claims']['C26']['evidence'].split('bounding alone ')[1].split(')')[0] =} |
| both together | "1293/2000 (64.65%)" | {= E['claims']['C26']['evidence'].split('<= 4 in ')[1].split(' ')[0] =} |
| with 8 and 5 | "1721/2000 (86.05%)" | {= E['claims']['C26']['evidence'].split('<= 8 / <= 5: ')[1].split(' ')[0] =} |

Every number of mine is {= f1(min(a - b for a, b in JT())) =} to {= f1(max(a - b for a, b in JT())) =} points lower than JTuu's, far more than the standard error of 2,000 states (about {= SE(0.6465, 2000) =} points). JTuu didn't say how the states were drawn. Two things in Kai Cui's generator would explain a gap: its states are random half turns around one trigger ("(random ht 100-110) (U R2 U R2 U) (random ht 100-110)", [[T5573]]), not a uniform 2c3 2e, and it allowed the last DR move to be inverted ("this accounts for inverting last move of dr", [[T5573]]). I can't reproduce it exactly. The order of the four options is the same in both.
