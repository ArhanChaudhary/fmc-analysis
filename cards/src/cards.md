# Decision cards

Six questions that come up mid-attempt, one card each, grouped by stage. Every card starts with the short answer, something you can actually use at the table, and then shows the numbers behind it and which study they're from. Nothing here is a guess: it's all exact counts or big uniform samples, same data as the studies.

- EO: [Should I add some partial EOs to my list?](#should-i-add-some-partial-eos-to-my-list) · [Should I stop looking for EOs and move to the next stage?](#should-i-stop-looking-for-eos-and-move-to-the-next-stage)
- EO to DR: [Should I switch this EO?](#should-i-switch-this-eo) · [Should I add some random moves to this EO?](#should-i-add-some-random-moves-to-this-eo)
- DR to HTR: [Should I continue checking variants of this route?](#should-i-continue-checking-variants-of-this-route) · [Should I NISS in the middle of this route?](#should-i-niss-in-the-middle-of-this-route)

**How I read the questions.** Three of them needed a reading. "Partial EOs" are slice EOs (the DR-1s / DR-2s 8fe approach), and "random moves" are RZP, the way people use both words here. "Variants of this route" I read as other ways through the same route; the card also answers the other likely reading, variations of the DR itself. If you meant something else by any of them, tell me and I'll redo that card.

**How to read these.** *What you check* is the stuff you can see during an attempt. Some numbers count every DR or every finish that exists, which nobody can search by hand. Those are marked **computer only**: treat them as the answer key, and use the comparison, not the move count. Shares are over uniformly random scrambles or states unless I say otherwise. There's no clock in any of this: the cards tell you what the next thing is worth, not how long it'll take you. Routes are written like in the HTR study, the subsets after each qt with the bracket on the other side: `4b2 2c3 (4b2 4a1 0c0)`.

November 2026. A date in brackets links to that message on the FMC solvers Discord.

## EO

### Should I add some partial EOs to my list?

**Yeah, the slice EO skips: after your EOs of 4 or less, before the 5-movers.** By partial EO I mean what people here mean by it, a slice EO: one or two slices oriented and the rest fixed later ("Doing partial EO saves ~3 moves in the EO step", sqAree, [[T10672]]). That gets you a DR-1s (one slice to fix) or a DR-2s 8fe.

*What you check:* whether an axis has a slice skip on either side, and then how long the DR-1s is. Rule of thumb: a DR-1s of $N$ is about as good as a normal DR of $N + 2$.

How much one is worth. On 500 real scrambles I counted how many of each thing you'd have to finish, on average, before one of them gives the best solution that any normal DR of 12 or less gives on that scramble (DR-xs, {{sec is-dr-xs-worth-it 7.2}}):

| What you finish | One in this many gets the scramble's best |
|---|---:|
| a DR-1s of 6 or less | {= is-dr-xs-worth-it: YIN('1s6') =} |
| a DR-1s of 7 | {= is-dr-xs-worth-it: YIN('1s7') =} |
| a normal DR of 9 or less | {= is-dr-xs-worth-it: YIN('dr9') =} |
| a DR-1s of 8 | {= is-dr-xs-worth-it: YIN('1s8') =} |
| a 10-move DR | {= is-dr-xs-worth-it: YIN('dr10') =} |
| an 11-move DR | {= is-dr-xs-worth-it: YIN('dr11') =} |

So a DR-1s of 7 is roughly a 9-move DR, and a DR-1s of 8 roughly a 10. On average the finish of a DR-1s is {= is-dr-xs-worth-it: D1() =} moves longer than a DR's ({{sec is-dr-xs-worth-it 5.2}}).

Against 5-move EOs. Same scrambles, starting from the EOs of 4 or less and their DRs of 10 or less. Each row adds one more pile of stuff to finish, and the number is how much shorter the average best solution gets ({{sec is-dr-xs-worth-it 7.4}}):

| Added on top of the EOs of 4 or less | Average best solution shorter by, moves |
|---|---:|
| every DR-1s of 8 or less from a slice EO | {= is-dr-xs-worth-it: EOD('eo10', 0, 2) =} |
| only the DR-1s of 7 or less | {= is-dr-xs-worth-it: EOD('eo10', 0, 1) =} |
| every 5-move EO | {= is-dr-xs-worth-it: EOD('eo10', 0, 4) =} |
| both | {= is-dr-xs-worth-it: EOD('eo10', 0, 5) =} |

The 5-movers give more, but that's about {= is-dr-xs-worth-it: f'{hu(REAL["eo10"]["policies"][4]["eos"] - REAL["eo10"]["policies"][0]["eos"]):,.0f}' =} more EOs per scramble, and skips are way less looking. They're common too: {= is-dr-xs-worth-it: SKIP4('normal') =} of scrambles have one on normal, {= is-dr-xs-worth-it: SKIP4('both') =} counting inverse (exact). They do clump, though: {= is-dr-xs-worth-it: SKIP('both', 'avg') =} per scramble on average over both sides, but {= is-dr-xs-worth-it: SKIP('both', 0) =} of scrambles have none at all ({{sec is-dr-xs-worth-it 6.1}}). The finishes behind both tables are the best the method allows, **computer only**. What you take from them is the order.

DR-2s 8fe is a different story: skips aren't how you get those ({{sec is-dr-xs-worth-it 6.3}}).

### Should I stop looking for EOs and move to the next stage?

**Once your EOs of 4 or less give you a DR of 9 or better, move on: the 5-movers only beat it on {= pc(STOPV('normal, inverse and NISS', '9 or less', 'five_better')) =} of those scrambles. If your best is 10 they beat it {= pc(STOPV('normal, inverse and NISS', '10', 'five_better')) =} of the time, at 11 it's {= pc(STOPV('normal, inverse and NISS', '11', 'five_better')) =}.** That's counting inverse and NISS EOs too. With normal EOs only, the 5-movers help less often in every row, and 9 or better is still where they stop being worth it (second table).

*What you check:* the best DR you've got through your EOs of 4 or less.

On 50,000 uniformly random scrambles I took the best DR through every EO of 4 or less (EO plus EO-keeping moves, total length, either of the other two axes, all three EO axes), then looked at what the EOs of exactly 5 add, and then the 6s. Each row is the best DR the short EOs gave:

{{stop_all}}

Same thing with normal EOs only (no inverse, no NISS):

{{stop_normal}}

Read each row as "what's still out there". The DRs counted are the best that exist through each EO, **computer only**. By hand you find some of them, so your best is often a move worse than the row you're in, and the row one move better is closer to your actual odds. Two more numbers that help decide when you've seen enough EOs ({{sec eo-to-dr 4.1}}, {{sec eo-to-dr 3.3}}):

- A scramble has {= eo-to-dr: B4('linear (normal)', 'all three axes', 4, 'mean_le') =} normal EOs of 4 or less on average over the three axes (median {= eo-to-dr: B4('linear (normal)', 'all three axes', 4, 'median_le') =}, counted the way nissy's `-a` lists them), and {= eo-to-dr: B4('NISS (normal, inverse, both)', 'all three axes', 4, 'mean_le') =} with inverse and NISS EOs. {= eo-to-dr: B4('linear (normal)', 'all three axes', 4, 'p_none_le') =} of scrambles have no normal EO of 4 or less at all.
- For a DR in 10, one EO of 4 or less is worth about ten 5-movers: 25 EOs of at most 4 give {= eo-to-dr: CELL('a3_yield', '≤ 10', 'Pairs from 25 EOs of ≤ 4') =} DRs of 10 or less on average, 200 EOs of exactly 5 give {= eo-to-dr: CELL('a3_yield', '≤ 10', 'Pairs from 200 EOs of exactly 5') =}. For a DR in 11 the 5-movers win ({= eo-to-dr: CELL('a3_yield', '≤ 11', 'Pairs from 25 EOs of ≤ 4') =} against {= eo-to-dr: CELL('a3_yield', '≤ 11', 'Pairs from 200 EOs of exactly 5') =}).

## EO to DR

### Should I switch this EO?

**On 4c4e, count the half turns to two bars, U and D moves free: 0 or 1, switch (it's guaranteed); 2, switch; 3, your call; 4 or 5, discard. For every other DRM use the pair card below.** Switching here means: after EO + RZP, go to inverse, keep the EO and look for DR there. Sub-7 means a DR in 6 or less on the switched side.

*What you check:* on 4c4e, the two rings and the count if you've got 2 or more pairs. Otherwise the card's pairs, side pairs, ARM or corner case on the switched case ({{sec eo-switch 4.4}}).

4c4e by half turns to two bars, exact over every 4c4e case ({{sec eo-switch 4.3}}):

| Half turns to two bars | Verdict | Share of 4c4e | Sub-7 rate |
|---|---|---:|---:|
| 0 or 1 | **switch**, guaranteed | {= eo-switch: pcx(RHG('le1', 'share')) =} | {= eo-switch: pcx(RHG('le1')) =} |
| 2 | **switch** | {= eo-switch: pcx(RH(2, 'share')) =} | {= eo-switch: pcx(RH(2)) =} |
| 3 | **your call** | {= eo-switch: pcx(RH(3, 'share')) =} | {= eo-switch: pcx(RH(3)) =} |
| 4 or 5 | **discard** | {= eo-switch: pcx(RHG('ge4', 'share')) =} | {= eo-switch: pcx(RHG('ge4')) =} |

By hand you can read the switch end, not the discard end. With 2+ pairs you can read the count (2 or fewer is {= eo-switch: pcx(RU('p2le2', 'share')) =} of 4c4e, and those are sub-7 {= eo-switch: pcx(RU('p2le2')) =} of the time). With 0 or 1 pair the reading only tells you "3 or more", so just use the card. Two bars as the target isn't new: it's in Andrew's 2019 video and rodneykinney's *DR - 4c4e Theory*. The exact count and the bands are what the study adds ({{sec eo-switch 4}}).

The pair card for every DRM, exact over all its cases ({{sec eo-switch 6}}). Each row is a verdict group: what you check on the switched case, how much of the DRM lands there, and how often it's sub-7:

{{eoswitch_cards}}

These hold after any RZP. The switched case is exactly uniform no matter how you got there, so the tables apply as they are ({{sec eo-switch 8}}). Also, after switching, checking the other DR axis is worth more than flipping the EO's last move: {= eo-switch: f1((OPT('4c4e', 2) - OPT('4c4e', 0)) * 100) =} points against {= eo-switch: f1((OPT('4c4e', 1) - OPT('4c4e', 0)) * 100) =} on 4c4e.

### Should I add some random moves to this EO?

**Yeah, if the EO leaves room for them. With every option checked, an EO-solved cube has a DR in 7 more moves or less {= eo-to-dr: CT('allkept', 'p_le7') =} of the time, in 6 or less {= eo-to-dr: CT('allkept', 'p_le6') =}, in 5 or less {= eo-to-dr: C6('all', 'all_eo_kept_p_le5') =}. So if you want a DR in 10: an EO of 3 or less is usually worth RZPing, a 4-mover depends on its case, and a 5-mover needs one of the good cases.** Random moves = RZP, setup moves into a DR trigger ("Doing random moves, but in polish it abreviates to rzp", Yura Riabov, [[D3759]]). Keep the EO while you do it: among routes through EOs of 5 or less, breaking the EO reaches the optimal DR where nothing EO-keeping does on {= eo-to-dr: BRK(5) =} of {= eo-to-dr: n(X('n')) =} scrambles ({{sec eo-to-dr 1}}).

*What you check:* how long the EO is, and its case (bad corners and edges out of place) on each DR axis, normal and inverse, before you add anything.

With every option (two DR axes, normal or inverse, the EO's last move either way, all keeping EO), the odds of a DR in 5, 6 or 7 more moves are {= eo-to-dr: C6('all', 'all_eo_kept_p_le5') =}, {= eo-to-dr: CT('allkept', 'p_le6') =} and {= eo-to-dr: CT('allkept', 'p_le7') =}. On one DR axis alone it's {= eo-to-dr: CT('plain', 'p_le6') =} for 6 and {= eo-to-dr: CT('plain', 'p_le7') =} for 7 ({{sec eo-to-dr 5.1}}). Here it is by the case you start from ({{sec eo-to-dr 5.2}}), the good named cases first and then the common ones. Each row is the case on the DR axis you're looking at. The middle columns use every option, the last one that axis alone:

{{cases}}

The case matters more than the RZP does: a natural 4c4e or 4c2e gets a DR in 6 more about half the time with every option, a 6c6e about one time in four. And a 6-move RZP is a much tougher target than a 4 or 5. On real attempts, after a switch, a DR in 5 after a 6-move RZP is {= eo-switch: f1(min(POP(d, 3) / POP(d, 4) for d in E['pop'])) =} to {= eo-switch: f1(max(POP(d, 3) / POP(d, 4) for d in E['pop'])) =} times rarer than a DR in 6 after a 5-move one, depending on the DRM ({{sec eo-switch 8}}). The DR lengths are optimal DRs after the EO, **computer only**. The case is the part you can actually read.

## DR to HTR

### Should I continue checking variants of this route?

**Yes, at least until the HTRs you're getting are 2 moves longer than the shortest one you know for that DR. On every subset, one route checked that far finds optimal more often than three routes where you only look at their shortest HTRs.** By variant I mean another way to follow the same route (different setup, different qt), which usually means a longer HTR.

*How I read the question.* "Variants" on the server usually means variations of moves you already have, so you might have meant variations of the DR itself (the last DR move the other way, a different trigger), not more HTRs on one route. The DR's last move is the one I can answer: turned the other way it gives a finish one move shorter on {= htr-routes: pc(Q5('all', 'share_variation_shorter')) =} of DRs, never more than one ({{sec htr-routes 7}}), so that's always worth a look. Other DR variations (other triggers, other DRs off the same RZP) aren't measured here.

*What you check:* the subset (first route per subset is in the table) and how long the HTRs you've found on it are.

For each corner subset, how often the first route of the HTR study's checklist finds optimal as you let its HTRs get longer, against trying more routes instead ({{sec htr-routes 4}}; 25,000 uniformly random DR states per subset × edges, pooled by exact subset size). *Up to 1 longer* means HTRs at most a move longer than the DR's shortest NISS HTR. 4c3 is 4a3 on one side and 4b3 on the other, 4c4 is 4a4/4b4, and a route uses the letter of the side it starts on:

{{variants}}

So on 0c4 the first route with HTRs up to 2 longer finds optimal on {= pc(BUDV('0c4', '2', 1)) =}, and three routes with only their shortest HTRs on {= pc(BUDV('0c4', '0', 3)) =}. The reason is that optimal rarely goes through a shortest HTR. Over all DRs, the shortest HTR that any optimal uses is a shortest NISS HTR on only {= htr-routes: pc(Q3('all', 'opt_uses_shortest_niss')) =}, 1 longer on {= htr-routes: pc(Q3('all', 'opt_htr_plus1')) =} and 2 longer on {= htr-routes: pc(Q3('all', 'opt_htr_plus2')) =} ({{sec htr-routes 6}}).

Past 2 longer the first route still has more in it (the *Any HTR length* column), but the HTRs keep getting longer and there are more of them to write at each length. Going to the second route instead, checked to 2 longer, gets you the gap between *Two routes, up to 2 longer* and *Up to 2 longer*. Where exactly to stop is a time question, and this card doesn't answer that. Which finish a route gives is the answer key, **computer only**. The "+2" is the habit you can actually keep.

### Should I NISS in the middle of this route?

**Depends on the subset and where you are on the route:**

{{mid_rule}}

A switch after more than 2 moves on one side is needed on about one DR in eight ({= htr-routes: pc(C11('all', 'budget2_needs_switch_after_gt2')) =}, more below).

*What you check:* which subset you started from, and which subset you're at now on normal.

I followed each subset's first route on normal. After each qt, here's how often an optimal finish keeps going on normal with no switch, how often one switches right there, and how often either one works (HTRs up to 2 longer than the shortest, 25,000 uniformly random DR states per subset × edges; same data as {{sec htr-routes 4}}). *Better* is whichever way is ahead by 5 points or more. Each row is a point on a route:

{{mid}}

The *Either* column is the argument for checking both. On 2c3 after one qt, keeping going finds it {= pc([r for r in MID if r['subset'] == '2c3' and r['qt_done'] == '1'][0]['continue_linear']) =} of the time and switching {= pc([r for r in MID if r['subset'] == '2c3' and r['qt_done'] == '1'][0]['switch_now']) =}, but one or the other {= pc([r for r in MID if r['subset'] == '2c3' and r['qt_done'] == '1'][0]['either']) =}.

Late switches: with HTRs up to 2 longer, optimal needs a switch after more than 2 moves on {= htr-routes: pc(C11('all', 'budget2_needs_switch_after_gt2')) =} of DRs ({= htr-routes: pc(C11('4b2', 'budget2_needs_switch_after_gt2')) =} of 4b2, {= htr-routes: pc(C11('2c3', 'budget2_needs_switch_after_gt2')) =} of 2c3), and after 4 or more on {= htr-routes: pc(C11('all', 'budget2_needs_switch_after_gt3')) =} ({{sec htr-routes 11}}). Which finishes exist is **computer only**. Where to switch is the part you use.

---

Sources: the studies linked from each card ([DR-xs](is-dr-xs-worth-it/), [EO to DR](eo-to-dr/), [EO switch](eo-switch/), [HTR routes](htr-routes/)). The two tables made for this page (when to stop looking for EOs, and switching mid-route) come from those studies' data, computed by the scripts in the repo's `cards/` folder.
