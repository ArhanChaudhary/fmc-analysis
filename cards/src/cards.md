# Decision cards

Six questions that come up mid-attempt, one card each, by stage. Each card opens with the answer as a rule you can use at the table, then the numbers behind it and the study section they come from. Everything is measured, not guessed: exact counts or large uniform samples, the same data as the studies. The questions:

- EO: [Should I add some partial EOs to my list?](#should-i-add-some-partial-eos-to-my-list) · [Should I stop looking for EOs and move to the next stage?](#should-i-stop-looking-for-eos-and-move-to-the-next-stage)
- EO to DR: [Should I switch this EO?](#should-i-switch-this-eo) · [Should I add some random moves to this EO?](#should-i-add-some-random-moves-to-this-eo)
- DR to HTR: [Should I continue checking variants of this route?](#should-i-continue-checking-variants-of-this-route) · [Should I NISS in the middle of this route?](#should-i-niss-in-the-middle-of-this-route)

**How to read the cards.** *What you check* is what you can see in an attempt. Where a number counts every DR or every finish that exists, a search you can't do by hand, it says **computer only**: that's the answer key, and what carries over to an attempt is the comparison, not the length. Shares are of uniformly random scrambles or states unless a line says otherwise. None of these cards has a clock in it: they say what the next thing is worth, not how long it takes you. Routes are written as in the HTR study: subsets after each quarter turn, the part in brackets on the other side, `4b2 2c3 (4b2 4a1 0c0)`.

November 2026. A date in brackets is a link to that message on the FMC solvers Discord.

## EO

### Should I add some partial EOs to my list?

**Yes: the slice-EO skips, once your EOs of 4 or less are written, and before the 5-movers.** A partial EO on the server is a slice EO, with one or two slices' edges oriented and the rest fixed later ("Doing partial EO saves ~3 moves in the EO step", sqAree, [[T10672]]). It leads to a DR-1s (one slice to fix) or a DR-2s 8fe.

*What you check:* whether an EO axis has a slice skip on either side, and then the DR-1s length. Judge a DR-1s of $N$ like a normal DR of about $N + 2$.

How much one is worth. On 500 real scrambles, the number of each kind of thing you'd finish, on average, for one to give the best solution any normal DR of 12 or less gives on its scramble (DR-xs, {{sec is-dr-xs-worth-it 7.2}}). Each row is what you finish:

| What you finish | One in this many gets the scramble's best |
|---|---:|
| a DR-1s of 6 or less | {= is-dr-xs-worth-it: YIN('1s6') =} |
| a DR-1s of 7 | {= is-dr-xs-worth-it: YIN('1s7') =} |
| a normal DR of 9 or less | {= is-dr-xs-worth-it: YIN('dr9') =} |
| a DR-1s of 8 | {= is-dr-xs-worth-it: YIN('1s8') =} |
| a 10-move DR | {= is-dr-xs-worth-it: YIN('dr10') =} |
| an 11-move DR | {= is-dr-xs-worth-it: YIN('dr11') =} |

So a DR-1s of 7 is about a DR of 9 and a DR-1s of 8 about a DR of 10. On average a DR-1s costs {= is-dr-xs-worth-it: D1() =} more moves in the finish than a DR ({{sec is-dr-xs-worth-it 5.2}}).

What they add next to 5-move EOs. Same scrambles, starting from the EOs of 4 or less and their DRs of 10 or less; each row adds one set of things to finish, and the number is how much shorter the average best solution gets ({{sec is-dr-xs-worth-it 7.4}}):

| Added on top of the EOs of 4 or less | Average best solution shorter by, moves |
|---|---:|
| every DR-1s of 8 or less from a slice EO | {= is-dr-xs-worth-it: EOD('eo10', 0, 2) =} |
| only the DR-1s of 7 or less | {= is-dr-xs-worth-it: EOD('eo10', 0, 1) =} |
| every 5-move EO | {= is-dr-xs-worth-it: EOD('eo10', 0, 4) =} |
| both | {= is-dr-xs-worth-it: EOD('eo10', 0, 5) =} |

The 5-movers give more, but they are about {= is-dr-xs-worth-it: f'{hu(REAL["eo10"]["policies"][4]["eos"] - REAL["eo10"]["policies"][0]["eos"]):,.0f}' =} more EOs per scramble, and the slice EOs take far less looking. Skips are common: {= is-dr-xs-worth-it: SKIP4('normal') =} of scrambles have one on normal, {= is-dr-xs-worth-it: SKIP4('both') =} counting inverse (exact). They clump, though: {= is-dr-xs-worth-it: SKIP('both', 'avg') =} per scramble on average over both sides, and {= is-dr-xs-worth-it: SKIP('both', 0) =} of scrambles have none ({{sec is-dr-xs-worth-it 6.1}}). The finishes behind the two tables are the best of the method's form, **computer only**; the order is what you use.

A DR-2s 8fe is a different story: a skip isn't how you get one ({{sec is-dr-xs-worth-it 6.3}}).

### Should I stop looking for EOs and move to the next stage?

**Once your EOs of 4 or less give a DR of 9 or better, move on: the 5-movers beat it on {= pc(STOPV('normal, inverse and NISS', '9 or less', 'five_better')) =} of those scrambles. At 10 they beat it on {= pc(STOPV('normal, inverse and NISS', '10', 'five_better')) =}, at 11 on {= pc(STOPV('normal, inverse and NISS', '11', 'five_better')) =}.** That's counting EOs on both sides and NISS EOs; with normal EOs only the 5-movers help less often at each row, and 9 or better is still where they stop paying (table below).

*What you check:* the best DR you have through your EOs of 4 or less.

On 50,000 uniformly random scrambles, take the best DR through every EO of 4 or less (EO plus EO-keeping turns, total length, either of the two other axes; all three EO axes), and ask what the EOs of exactly 5 add, then the EOs of 6. Each row is the best DR the short EOs give:

{{stop_all}}

The same with normal EOs only (no inverse, no NISS):

{{stop_normal}}

Read the rows as "what's still out there": the DRs counted are the best that exist through each EO, **computer only**. By hand you find some of them, so your best is often a move worse than the row you're in, and the row one move better is closer to your odds. Two more numbers that help decide when you've seen enough EOs ({{sec eo-to-dr 4.1}}, {{sec eo-to-dr 3.3}}):

- A scramble has {= eo-to-dr: B4('linear (normal)', 'all three axes', 4, 'mean_le') =} normal EOs of 4 or less on average over the three axes (median {= eo-to-dr: B4('linear (normal)', 'all three axes', 4, 'median_le') =}, counted the way nissy's `-a` lists them), and {= eo-to-dr: B4('NISS (normal, inverse, both)', 'all three axes', 4, 'mean_le') =} with inverse and NISS EOs. {= eo-to-dr: B4('linear (normal)', 'all three axes', 4, 'p_none_le') =} of scrambles have no normal EO of 4 or less.
- For a DR in 10, one EO of 4 or less is worth about ten 5-movers: 25 EOs of at most 4 give {= eo-to-dr: CELL('a3_yield', '≤ 10', 'Pairs from 25 EOs of ≤ 4') =} DRs of 10 or less on average, 200 EOs of exactly 5 give {= eo-to-dr: CELL('a3_yield', '≤ 10', 'Pairs from 200 EOs of exactly 5') =}. For a DR in 11 the 5-movers win ({= eo-to-dr: CELL('a3_yield', '≤ 11', 'Pairs from 25 EOs of ≤ 4') =} against {= eo-to-dr: CELL('a3_yield', '≤ 11', 'Pairs from 200 EOs of exactly 5') =}).

## EO to DR

### Should I switch this EO?

**For 4c4e, count the half turns to two bars with U and D turns free: 0 or 1, switch (certain); 2, switch; 3, your call; 4 or 5, discard. For the other DRMs, use the pair card below.** Switch means: after EO + RZP, go to the inverse, keep the EO and look for a DR there. Sub-7 means a DR in 6 or less on the switched side.

*What you check:* on 4c4e, the two rings and the count when you have 2 or more pairs; otherwise the card's pairs, side pairs, ARM or corner case on the switched case ({{sec eo-switch 4.4}}).

4c4e by the half turns to two bars, exact over all 4c4e cases ({{sec eo-switch 4.3}}). Each row is a count:

| Half turns to two bars | Verdict | Share of 4c4e | Sub-7 rate |
|---|---|---:|---:|
| 0 or 1 | **switch**, certain | {= eo-switch: pcx(RHG('le1', 'share')) =} | {= eo-switch: pcx(RHG('le1')) =} |
| 2 | **switch** | {= eo-switch: pcx(RH(2, 'share')) =} | {= eo-switch: pcx(RH(2)) =} |
| 3 | **your call** | {= eo-switch: pcx(RH(3, 'share')) =} | {= eo-switch: pcx(RH(3)) =} |
| 4 or 5 | **discard** | {= eo-switch: pcx(RHG('ge4', 'share')) =} | {= eo-switch: pcx(RHG('ge4')) =} |

By hand you can read the switch end, not the discard end: with 2 or more pairs you can read the count (2 or fewer is {= eo-switch: pcx(RU('p2le2', 'share')) =} of 4c4e at {= eo-switch: pcx(RU('p2le2')) =}), and with 0 or 1 pair the reading only says "3 or more", so use the card. The two bars as the target come from Andrew's 2019 video and rodneykinney's *DR - 4c4e Theory*; the exact count and its bands are the study's ({{sec eo-switch 4}}).

The pair card for every DRM, exact over all its cases ({{sec eo-switch 6}}). Each row is one verdict group of a DRM's card: what to check on the switched case, the share of the DRM in the group, and its sub-7 rate:

{{eoswitch_cards}}

These hold after any RZP: the switched case is exactly uniform whatever path made it, so the tables apply as they are ({{sec eo-switch 8}}). After the switch, checking the other DR axis adds more than turning the EO's last move the other way: {= eo-switch: f1((OPT('4c4e', 2) - OPT('4c4e', 0)) * 100) =} points against {= eo-switch: f1((OPT('4c4e', 1) - OPT('4c4e', 0)) * 100) =} on 4c4e.

### Should I add some random moves to this EO?

**Yes, when the EO leaves room for them: with every option checked, an EO-solved cube has a DR within 7 more moves {= eo-to-dr: CT('allkept', 'p_le7') =} of the time, within 6 {= eo-to-dr: CT('allkept', 'p_le6') =}, within 5 {= eo-to-dr: C6('all', 'all_eo_kept_p_le5') =}. So toward a DR in 10, an EO of 3 or less is usually worth it, an EO of 4 depends on its case, and an EO of 5 needs one of the good cases.** Random moves are an RZP, setup moves to a DR trigger ("Doing random moves, but in polish it abreviates to rzp", Yura Riabov, [[D3759]]). Keep the EO while you do it: among routes through an EO of at most 5, turns that break the EO reach the optimal DR where no EO-keeping one does on {= eo-to-dr: BRK(5) =} of {= eo-to-dr: n(X('n')) =} scrambles ({{sec eo-to-dr 1}}).

*What you check:* the EO's length, and its case (bad corners and edges out of place) on each DR axis, normal and inverse, before any random moves.

With every option (two DR axes, normal or inverse, the EO's last turn either way, all keeping the EO), the chance of a DR within 5, 6 or 7 more moves is {= eo-to-dr: C6('all', 'all_eo_kept_p_le5') =}, {= eo-to-dr: CT('allkept', 'p_le6') =} and {= eo-to-dr: CT('allkept', 'p_le7') =}; on one DR axis alone it's {= eo-to-dr: CT('plain', 'p_le6') =} for 6 and {= eo-to-dr: CT('plain', 'p_le7') =} for 7 ({{sec eo-to-dr 5.1}}). By the case you start from ({{sec eo-to-dr 5.2}}), the named good cases first, then the common ones. Each row is the case on the DR axis you look at; the middle columns use every option, the last one that axis alone:

{{cases}}

The case decides more than the RZP does: a natural 4c4e or 4c2e has a DR within 6 more about half the time with every option, a 6c6e one time in four. A 6-move RZP has a much harder target than a 4- or 5-move one: on real attempts, after a switch, the chance of a DR in 5 after a 6-move RZP is {= eo-switch: f1(min(POP(d, 3) / POP(d, 4) for d in E['pop'])) =} to {= eo-switch: f1(max(POP(d, 3) / POP(d, 4) for d in E['pop'])) =} times smaller than the chance of a DR in 6 after a 5-move one, depending on the DRM ({{sec eo-switch 8}}). The DR lengths are optimal DRs after the EO, **computer only**; the case is what you read.

## DR to HTR

### Should I continue checking variants of this route?

**Yes, at least until the HTRs you're getting on it are 2 moves longer than the shortest HTR you know for the DR. On every subset, one route checked that far finds the optimal more often than three routes checked with their shortest HTRs only.** A variant here is another way of following the same route (another setup, another quarter turn), which usually means a longer HTR.

*What you check:* the subset (the first route per subset is below) and the length of the HTRs you've found on it.

For each corner subset, the share of DRs where the first route of the HTR study's checklist finds the optimal, as you let its HTRs get longer, against trying more routes ({{sec htr-routes 4}}; 25,000 uniformly random DR states per subset × edges, pooled by the exact subset sizes). *Up to 1 longer* means HTRs at most one move longer than the DR's shortest NISS HTR. Each row is a corner subset (4c3 is 4a3 on one side and 4b3 on the other, 4c4 is 4a4/4b4; a route names the side it starts on):

{{variants}}

So on 0c4 the first route with HTRs up to 2 longer finds the optimal on {= pc(BUDV('0c4', '2', 1)) =}, and three routes with shortest HTRs only on {= pc(BUDV('0c4', '0', 3)) =}. That's because the optimal finish rarely goes through a shortest HTR: over all DRs, the shortest HTR any optimal uses is a shortest NISS HTR on only {= htr-routes: pc(Q3('all', 'opt_uses_shortest_niss')) =}, 1 longer on {= htr-routes: pc(Q3('all', 'opt_htr_plus1')) =} and 2 longer on {= htr-routes: pc(Q3('all', 'opt_htr_plus2')) =} ({{sec htr-routes 6}}). Past 2 longer the first route still has more to give (*Any HTR length*), but through ever longer HTRs, with more of them to write at each length; the second route checked to 2 longer adds the difference between *Two routes, up to 2 longer* and *Up to 2 longer*. Where to stop is the time question this card doesn't answer. Which finish the route gives is the answer key, **computer only**; the budget is the habit you can keep.

### Should I NISS in the middle of this route?

**It depends on the subset and on where you are on the route:**

{{mid_rule}}

A switch after more than 2 moves on one side is needed on about one DR in eight ({= htr-routes: pc(C11('all', 'budget2_needs_switch_after_gt2')) =}, below).

*What you check:* the subset you started from and the subset you're at now on normal.

Follow the first route of each subset on normal. After each quarter turn, the share of the subset's DRs where an optimal finish keeps going on normal with no switch, where one switches right there, and where either does (HTRs up to 2 longer than the shortest, 25,000 uniformly random DR states per subset × edges; data of {{sec htr-routes 4}}). *Better* is the way that's ahead by 5 points or more. Each row is a point on a route:

{{mid}}

The *Either* column is the case for checking both: on 2c3 after one quarter turn, keeping going finds it on {= pc([r for r in MID if r['subset'] == '2c3' and r['qt_done'] == '1'][0]['continue_linear']) =} and switching on {= pc([r for r in MID if r['subset'] == '2c3' and r['qt_done'] == '1'][0]['switch_now']) =}, but one or the other on {= pc([r for r in MID if r['subset'] == '2c3' and r['qt_done'] == '1'][0]['either']) =}. Late switches: with HTRs up to 2 longer, the optimal needs a switch after more than 2 moves on {= htr-routes: pc(C11('all', 'budget2_needs_switch_after_gt2')) =} of DRs ({= htr-routes: pc(C11('4b2', 'budget2_needs_switch_after_gt2')) =} of 4b2, {= htr-routes: pc(C11('2c3', 'budget2_needs_switch_after_gt2')) =} of 2c3), and after 4 or more on {= htr-routes: pc(C11('all', 'budget2_needs_switch_after_gt3')) =} ({{sec htr-routes 11}}). Which finishes exist is **computer only**; where to switch is what you use.

---

Sources: the studies linked from each card ([DR-xs](is-dr-xs-worth-it/), [EO to DR](eo-to-dr/), [EO switch](eo-switch/), [HTR routes](htr-routes/)). The two tables made for this page (when to stop looking for EOs, and switching mid-route) are computed from those studies' data by the scripts in the repository's `cards/` folder.
