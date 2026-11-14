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

**On 4c4e, keep switching what you switch now: 2 or more top pairs, or 1 top pair with ARM 21. Of all non-JZP 4c4e cases that have a DR in 5 or less after the switch, that rule switches {= pc(SR('current', 'caught_le5')) =}. What NISS tracing adds is which of those switches to work first (below). For the other DRMs, use the pair card further down. JZP you check directly.**

Switching means: after EO + RZP, go to the inverse, keep the EO and look for a DR there. All the odds on this card are for the switched side and are exact, over every EO-solved case of the DRM. They hold after any RZP, because the switched case is exactly uniform whatever path made it ({{sec eo-switch 8}}).

*What you check:* NISS trace the switched case from normal: top pairs (wen's tracing), side pairs (rodneykinney's), ARM (the R/L stickers on U/D for corner ARM), and the corner case. On 4c4e with 2 or more top pairs, also trace the leftover bad corners and the two U/D edges stuck in the E slice, and work out the half turns to two bars, explained below.

**4c4e, your rule split up.** Each row is one group of switched non-JZP 4c4e cases, by what you trace. The second column says how common the group is among all non-JZP 4c4e cases. The next two say how often a case in that row has a DR in 6 (or 5) or less after the switch. The last says how much of all the 5-or-less cases sit in that row:

{{sw44_groups}}

Your rule is the first four rows: 2+ top pairs, any number of half turns, plus 1 top pair with ARM 21. The 2+ top pair cases with 2 or fewer half turns to two bars are where the short DRs are, about 3 in 4 with a DR in 6 or less and 1 in 4 with a DR in 5 or less. The 2+ top pair cases with 3 or more are barely better than an average 4c4e, and almost never a 5. Your 1-pair ARM 21 rule sits in between, and it holds {= pc(S44('p1_arm21', 'of_nonjzp_le5')) =} of all the 5-or-less cases, so it's worth keeping.

The same thing as rules. Each row is a switch rule over all non-JZP 4c4e cases: how many it switches, how many of the switched have a DR in 6 or less, and how many of all the 6-or-less and 5-or-less cases it catches:

{{sw44_rules}}

So if missing a short DR hurts you more than a wasted switch, keep your rule and use half turns to two bars only to order the switches: 2 or fewer first, then 1 top pair with ARM 21, then the 2+ top pair cases with 3 or more. Dropping that last group saves about {= pc(float(S44('p2_3', 'share_of_nonjzp')) + float(S44('p2_45', 'share_of_nonjzp'))) =} of all non-JZP 4c4e cases' worth of switches and loses {= pc(float(S44('p2_3', 'of_nonjzp_le5')) + float(S44('p2_45', 'of_nonjzp_le5'))) =} of the 5-or-less cases.

JZP is {= pc(S44('jzp', 'share_of_4c4e')) =} of all 4c4e cases (on 4c4e it's exactly ARM 00), and {= pc(S44('jzp', 'p_le6')) =} of those have a DR in 6 or less after the switch.

**Half turns to two bars, by NISS tracing.** A switched 4c4e is one R or L quarter turn away from DR when three things line up:

- each of the two bad U/D edges is a **bar**: it has a top pair on both sides, so both corners next to it are bad and both pair with it;
- the two bars are on the same R or L side, one in U and one in D;
- the two U/D edges stuck in the E slice (the ones you look at for side pairs) are on that same R/L side.

U and D turns are free, and each R2, L2, F2 or B2 swaps the corner, edge and corner of that side in U with the three in D. *Half turns to two bars* is the fewest of those R2/L2/F2/B2 that get you there. Here's how to read it off your tracing, by top pairs:

- **4 top pairs:** you have two bars already. If they're in different layers, you need 0 half turns for the bars. If they're both in one layer, you need 1 to move one over.
- **3 top pairs:** one bad corner is left over, and one bad edge is missing its second pair. Start at 1. Add 1 if the leftover corner is in the same layer as that edge. Add 1 if the leftover corner is blocked: a bad piece on its other side, meaning the neighbouring edge it would *not* pair with, or the corner just past that edge. Add 1 if both bad edges are in the same layer, opposite each other. This is exact on every 3-pair case ({{sec eo-switch 4.4}}).
- **2 top pairs:** check whether one half turn gets you to one of the four shapes that are a single half turn from two bars ({{sec eo-switch 4.4}} lists them; one of them has only 2 top pairs, one on each bad edge, with each layer holding the corner the other needs).
- **0 or 1 top pair:** it's always 2 or more, nearly always 3 or more, and by hand you can't tell a 3 from a 4 or 5. Use ARM instead (your ARM 21 rule, or the pair card).

Then the stuck E-slice edges: they cost nothing if they share an R/L colour (they're on one R/L side), 1 half turn if they share no colour, and 2 if they share an F/B colour. The answer is always the larger of the two numbers, bars and stuck edges (checked on every 4c4e case): you choose which side each half turn is on, so the turns that make the bars can fix the stuck edges at no extra cost. Every 4c4e with 0 or 1 half turns to two bars has a DR in 6 or less ({= eo-switch: pcx(RHG('le1', 'share')) =} of all 4c4e cases). Two bars as the target goes back to Andrew's 2019 video and rodneykinney's *DR - 4c4e Theory*. The exact count and its odds are the EO-switch study's ({{sec eo-switch 4}}).

**The pair card, every DRM.** Each row is one verdict group of a DRM: what you trace on the switched case, how much of that DRM lands in the group (share of all cases of the DRM), and how often a case in the group has a DR in 6 or less after the switch ({{sec eo-switch 6}}). For 4c4e this card splits by paired edges instead of top pairs, so it's a bit different from your rule above:

{{eoswitch_cards}}

One more thing after you switch: checking the other DR axis beats turning the EO's last move the other way. On 4c4e it adds {= eo-switch: f1((OPT('4c4e', 2) - OPT('4c4e', 0)) * 100) =} percentage points to the share of switched cases with a DR in 6 or less, against {= eo-switch: f1((OPT('4c4e', 1) - OPT('4c4e', 0)) * 100) =} for the last move ({{sec eo-switch 8}}).

### Should I add some random moves to this EO?

**Yeah, if the EO leaves room for them. Random moves are an RZP: setup moves into a DR trigger ("Doing random moves, but in polish it abreviates to rzp", Yura Riabov, [[D3759]]). Over all EO-solved states, with every option checked, {= eo-to-dr: CT('allkept', 'p_le7') =} have a DR in 7 or fewer more moves, {= eo-to-dr: CT('allkept', 'p_le6') =} in 6 or fewer and {= eo-to-dr: C6('all', 'all_eo_kept_p_le5') =} in 5 or fewer. So if you want a DR in 10: an EO of 3 or less is usually worth RZPing, a 4-mover depends on its DRM, and a 5-mover needs one of the good DRMs.**

*Every option* means both DR axes, normal or inverse, and the EO's last move either way, all keeping the EO. Keep the EO while you add moves: among routes through EOs of 5 or less, breaking the EO reaches the optimal DR where nothing EO-keeping does on only {= eo-to-dr: BRK(5) =} of {= eo-to-dr: n(X('n')) =} scrambles ({{sec eo-to-dr 1}}).

*What you check:* how long the EO is, and the DRM it leaves on each DR axis (bad corners and bad edges for that DR), normal and inverse, before you add anything.

With a single DR axis and normal only, the odds drop to {= eo-to-dr: CT('plain', 'p_le6') =} for 6 or fewer more and {= eo-to-dr: CT('plain', 'p_le7') =} for 7 ({{sec eo-to-dr 5.1}}). By the DRM you start from ({{sec eo-to-dr 5.2}}): each row is the DRM on the DR axis you look at. The second column is how common it is among all EO-solved states. The others say how often a state with that DRM has a DR within 5, 6 or 7 more moves (every option), or within 6 on that axis alone:

{{cases}}

The DRM matters more than the RZP does. A natural 4c4e or 4c2e has a DR in 6 or fewer more moves about half the time with every option, a 6c6e about one time in four. And a 6-move RZP is a much tougher target than a 4 or 5. On real attempts, after a switch, the share of cases with a DR in 5 after a 6-move RZP is {= eo-switch: f1(min(POP(d, 3) / POP(d, 4) for d in E['pop'])) =} to {= eo-switch: f1(max(POP(d, 3) / POP(d, 4) for d in E['pop'])) =} times smaller than the share with a DR in 6 after a 5-move one, depending on the DRM ({{sec eo-switch 8}}). The DR lengths are optimal DRs after the EO, **computer only**. The DRM is the part you can actually read.

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
