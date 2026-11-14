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

**Yeah, the slice EO skips: after your EOs of 4 or less, before the 5-movers.** By partial EO I mean what people here mean by it, a slice EO: one or two slices oriented and the rest fixed later ("Doing partial EO saves ~3 moves in the EO step", sqAree, [23 Jan 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1464341592952537128)). That gets you a DR-1s (one slice to fix) or a DR-2s 8fe.

*What you check:* whether an axis has a slice skip on either side, and then how long the DR-1s is. Rule of thumb: a DR-1s of $N$ is about as good as a normal DR of $N + 2$.

How much one is worth. On 500 real scrambles I counted how many of each thing you'd have to finish, on average, before one of them gives the best solution that any normal DR of 12 or less gives on that scramble (DR-xs, [section 7.2](is-dr-xs-worth-it/#72-what-each-one-is-worth)):

| What you finish | One in this many gets the scramble's best |
|---|---:|
| a DR-1s of 6 or less | 12 |
| a DR-1s of 7 | 49 |
| a normal DR of 9 or less | 41 |
| a DR-1s of 8 | 210 |
| a 10-move DR | 202 |
| an 11-move DR | 952 |

So a DR-1s of 7 is roughly a 9-move DR, and a DR-1s of 8 roughly a 10. On average the finish of a DR-1s is 2.27 moves longer than a DR's ([section 5.2](is-dr-xs-worth-it/#52-by-subset)).

Against 5-move EOs. Same scrambles, starting from the EOs of 4 or less and their DRs of 10 or less. Each row adds one more pile of stuff to finish, and the number is how much shorter the average best solution gets ([section 7.4](is-dr-xs-worth-it/#74-against-5-move-eos)):

| Added on top of the EOs of 4 or less | Average best solution shorter by, moves |
|---|---:|
| every DR-1s of 8 or less from a slice EO | 0.36 |
| only the DR-1s of 7 or less | 0.17 |
| every 5-move EO | 0.71 |
| both | 0.91 |

The 5-movers give more, but that's about 253 more EOs per scramble, and skips are way less looking. They're common too: 68.7953% of scrambles have one on normal, 79.3147% counting inverse (exact). They do clump, though: 2.25 per scramble on average over both sides, but 21% of scrambles have none at all ([section 6.1](is-dr-xs-worth-it/#61-how-often-there-is-a-slice-eo-skip)). The finishes behind both tables are the best the method allows, **computer only**. What you take from them is the order.

DR-2s 8fe is a different story: skips aren't how you get those ([section 6.3](is-dr-xs-worth-it/#63-to-a-dr-2s-8fe-the-same-problem-as-a-dr)).

### Should I stop looking for EOs and move to the next stage?

**Once your EOs of 4 or less give you a DR of 9 or better, move on: the 5-movers only beat it on 11.0% of those scrambles. If your best is 10 they beat it 44.5% of the time, at 11 it's 90.8%.** That's counting inverse and NISS EOs too. With normal EOs only, the 5-movers help less often in every row, and 9 or better is still where they stop being worth it (second table).

*What you check:* the best DR you've got through your EOs of 4 or less.

On 50,000 uniformly random scrambles I took the best DR through every EO of 4 or less (EO plus EO-keeping moves, total length, either of the other two axes, all three EO axes), then looked at what the EOs of exactly 5 add, and then the 6s. Each row is the best DR the short EOs gave:

| Best DR through your EOs of 4 or less | Share of scrambles | 5-move EOs give a shorter DR | Average shortening from the 5-movers, moves | Then 6-move EOs give a shorter DR still |
|---|---:|---:|---:|---:|
| 8 or less | 10.4% | 3.4% | 0.04 | 4.8% |
| 9 | 32.0% | 13.5% | 0.16 | 16.7% |
| 10 | 39.8% | 44.5% | 0.53 | 37.0% |
| 11 | 12.7% | 90.8% | 1.22 | 40.4% |
| 12 or more | 1.0% | 100.0% | 2.06 | 42.0% |
| no EO of 4 or less | 4.0% | 99.7% | – | 45.3% |

Same thing with normal EOs only (no inverse, no NISS):

| Best DR through your EOs of 4 or less | Share of scrambles | 5-move EOs give a shorter DR | Average shortening from the 5-movers, moves | Then 6-move EOs give a shorter DR still |
|---|---:|---:|---:|---:|
| 8 or less | 4.2% | 2.2% | 0.03 | 2.8% |
| 9 | 15.7% | 6.7% | 0.08 | 8.1% |
| 10 | 33.0% | 24.7% | 0.29 | 24.3% |
| 11 | 22.0% | 65.6% | 0.82 | 38.5% |
| 12 or more | 3.6% | 98.4% | 1.62 | 40.7% |
| no EO of 4 or less | 21.5% | 97.8% | – | 49.7% |

Read each row as "what's still out there". The DRs counted are the best that exist through each EO, **computer only**. By hand you find some of them, so your best is often a move worse than the row you're in, and the row one move better is closer to your actual odds. Two more numbers that help decide when you've seen enough EOs ([section 4.1](eo-to-dr/#41-how-many-eos-how-short), [section 3.3](eo-to-dr/#33-how-many-drs)):

- A scramble has 15.3 normal EOs of 4 or less on average over the three axes (median 12, counted the way nissy's `-a` lists them), and 43.9 with inverse and NISS EOs. 21.5% of scrambles have no normal EO of 4 or less at all.
- For a DR in 10, one EO of 4 or less is worth about ten 5-movers: 25 EOs of at most 4 give 4.0 DRs of 10 or less on average, 200 EOs of exactly 5 give 3.5. For a DR in 11 the 5-movers win (17.3 against 23.7).

## EO to DR

### Should I switch this EO?

**On 4c4e, keep switching what you switch now: 2 or more top pairs, or 1 top pair with ARM 21. Of all non-JZP 4c4e cases that have a DR in 5 or less after the switch, that rule switches 94.3%. What NISS tracing adds is which of those switches to work first (below). For the other DRMs, use the pair card further down. JZP you check directly.**

Switching means: after EO + RZP, go to the inverse, keep the EO and look for a DR there. All the odds on this card are for the switched side and are exact, over every EO-solved case of the DRM. They hold after any RZP, because the switched case is exactly uniform whatever path made it ([section 8](eo-switch/#8-real-rzps-does-the-uniform-table-apply-after-a-switch)).

*What you check:* NISS trace the switched case from normal: top pairs (wen's tracing), side pairs (rodneykinney's), ARM (the R/L stickers on U/D for corner ARM), and the corner case. On 4c4e with 2 or more top pairs, also trace the leftover bad corners and the two U/D edges stuck in the E slice, and work out the half turns to two bars, explained below.

**4c4e, your rule split up.** Each row is one group of switched non-JZP 4c4e cases, by what you trace. The second column says how common the group is among all non-JZP 4c4e cases. The next two say how often a case in that row has a DR in 6 (or 5) or less after the switch. The last says how much of all the 5-or-less cases sit in that row:

| What you NISS trace on the switched case | Share of all non-JZP 4c4e cases | DR in 6 or less after the switch (share of the row) | DR in 5 or less after the switch (share of the row) | Share of all non-JZP 4c4e cases with a DR in 5 or less |
|---|---:|---:|---:|---:|
| 2+ top pairs, 2 or fewer half turns to two bars | 12.0% | 73.6% | 26.5% | 77.5% |
| 2+ top pairs, 3 half turns to two bars | 12.3% | 21.2% | 1.2% | 3.5% |
| 2+ top pairs, 4 or 5 half turns to two bars | 0.7% | 8.7% | 0.8% | 0.1% |
| 1 top pair, ARM 21 | 9.3% | 31.2% | 5.8% | 13.2% |
| 1 top pair, other ARM | 35.3% | 8.5% | 0.4% | 3.6% |
| no top pair | 30.3% | 4.2% | 0.3% | 2.0% |

Your rule is the first four rows: 2+ top pairs, any number of half turns, plus 1 top pair with ARM 21. The 2+ top pair cases with 2 or fewer half turns to two bars are where the short DRs are, about 3 in 4 with a DR in 6 or less and 1 in 4 with a DR in 5 or less. The 2+ top pair cases with 3 or more are barely better than an average 4c4e, and almost never a 5. Your 1-pair ARM 21 rule sits in between, and it holds 13.2% of all the 5-or-less cases, so it's worth keeping.

The same thing as rules. Each row is a switch rule over all non-JZP 4c4e cases: how many it switches, how many of the switched have a DR in 6 or less, and how many of all the 6-or-less and 5-or-less cases it catches:

| Switch when | Share of all non-JZP 4c4e cases switched | DR in 6 or less, among the switched | Share of all non-JZP 4c4e cases with a DR in 6 or less that get switched | Share of all non-JZP 4c4e cases with a DR in 5 or less that get switched |
|---|---:|---:|---:|---:|
| 2+ top pairs, or 1 top pair with ARM 21 (what people switch now) | 34.4% | 42.0% | 77.2% | 94.3% |
| only 2+ top pairs with 2 or fewer half turns to two bars | 12.0% | 73.6% | 47.4% | 77.5% |
| that, plus 1 top pair with ARM 21 | 21.3% | 55.1% | 62.9% | 90.7% |

So if missing a short DR hurts you more than a wasted switch, keep your rule and use half turns to two bars only to order the switches: 2 or fewer first, then 1 top pair with ARM 21, then the 2+ top pair cases with 3 or more. Dropping that last group saves about 13.1% of all non-JZP 4c4e cases' worth of switches and loses 3.6% of the 5-or-less cases.

JZP is 1.8% of all 4c4e cases (on 4c4e it's exactly ARM 00), and 47.5% of those have a DR in 6 or less after the switch.

**Half turns to two bars, by NISS tracing.** A switched 4c4e is one R or L quarter turn away from DR when three things line up:

- each of the two bad U/D edges is a **bar**: it has a top pair on both sides, so both corners next to it are bad and both pair with it;
- the two bars are on the same R or L side, one in U and one in D;
- the two U/D edges stuck in the E slice (the ones you look at for side pairs) are on that same R/L side.

U and D turns are free, and each R2, L2, F2 or B2 swaps the corner, edge and corner of that side in U with the three in D. *Half turns to two bars* is the fewest of those R2/L2/F2/B2 that get you there. Here's how to read it off your tracing, by top pairs:

- **4 top pairs:** you have two bars already. If they're in different layers, you need 0 half turns for the bars. If they're both in one layer, you need 1 to move one over.
- **3 top pairs:** one bad corner is left over, and one bad edge is missing its second pair. Start at 1. Add 1 if the leftover corner is in the same layer as that edge. Add 1 if the leftover corner is blocked: a bad piece on its other side, meaning the neighbouring edge it would *not* pair with, or the corner just past that edge. Add 1 if both bad edges are in the same layer, opposite each other. This is exact on every 3-pair case ([section 4.4](eo-switch/#44-reading-the-count)).
- **2 top pairs:** check whether one half turn gets you to one of the four shapes that are a single half turn from two bars ([section 4.4](eo-switch/#44-reading-the-count) lists them; one of them has only 2 top pairs, one on each bad edge, with each layer holding the corner the other needs).
- **0 or 1 top pair:** it's always 2 or more, nearly always 3 or more, and by hand you can't tell a 3 from a 4 or 5. Use ARM instead (your ARM 21 rule, or the pair card).

Then the stuck E-slice edges: they cost nothing if they share an R/L colour (they're on one R/L side), 1 half turn if they share no colour, and 2 if they share an F/B colour. The answer is always the larger of the two numbers, bars and stuck edges (checked on every 4c4e case): you choose which side each half turn is on, so the turns that make the bars can fix the stuck edges at no extra cost. Every 4c4e with 0 or 1 half turns to two bars has a DR in 6 or less (1.0% of all 4c4e cases). Two bars as the target goes back to Andrew's 2019 video and rodneykinney's *DR - 4c4e Theory*. The exact count and its odds are the EO-switch study's ([section 4](eo-switch/#4-two-rings-count-the-half-turns-4c4e)).

**The pair card, every DRM.** Each row is one verdict group of a DRM: what you trace on the switched case, how much of that DRM lands in the group (share of all cases of the DRM), and how often a case in the group has a DR in 6 or less after the switch ([section 6](eo-switch/#6-the-switch-cards-drm-by-drm)). For 4c4e this card splits by paired edges instead of top pairs, so it's a bit different from your rule above:

| DRM | Verdict | What you NISS trace on the switched case | Share of all cases of this DRM | DR in 6 or less after the switch (share of the row) |
|---|---|---|---|---|
| 4c4e | **switch** | both bad U/D edges paired | 15.5% | 59.9% |
|  | **your call** | one paired, edge ARM 1 (the two bad edges in different slices) | 32.5% | 20.0% |
|  | **discard** | one paired, edge ARM 0 or 2 (both bad edges in one slice); no bad edge paired | 52.0% | 6.7% |
| 4c2e | **switch** | pairs + side pairs/2 is 1.5 or more | 22.3% | 57.0% |
|  | **your call** | pairs + side pairs/2 is exactly 1 | 24.6% | 15.7% |
|  | **discard** | pairs + side pairs/2 is 0 or 0.5 | 53.2% | 4.0% |
| 3c2e | **switch** | always | >99.9% | 61.6% |
| 7c8e | **switch** | 5 or 6 pairs | 16.3% | 59.0% |
|  | **your call** | 4 pairs | 33.7% | 15.9% |
|  | **discard** | 3 pairs or fewer | 50.0% | 2.9% |
| 8c8e | **your call** | corner ARM 0, 4 or 8 | 44.2% | 20.5% |
|  | **discard** | corner ARM 2, 3, 5 or 6 | 55.8% | 9.8% |
| 2c2e | **switch** | a bad U/D edge with a pair | 23.2% | 59.6% |
|  | **your call** | no pair, but JZP | 8.0% | 38.9% |
|  | **discard** | no pair, not JZP | 68.8% | 9.7% |
| 4c6e | **switch** | JZP | 0.61% | 61.1% |
|  | **your call** | 4 pairs | 1.2% | 47.9% |
|  | **discard** | anything else | 98.2% | 3.7% |
| 3c4e | **your call** | 2 pairs | 10.7% | 33.7% |
|  | **discard** | 0 or 1 pair | 89.3% | 7.1% |
| 3c6e | **discard** | always | >99.9% | 4.8% |
| 5c4e | **your call** | 3 pairs | 6.1% | 27.6% |
|  | **discard** | 2 pairs or fewer | 93.9% | 5.9% |
| 5c6e | **your call** | 4 pairs | 3.1% | 37.9% |
|  | **discard** | 3 pairs or fewer | 96.9% | 5.1% |
| 6c6e | **your call** | JZP, or 5 or 6 pairs | 1.3% | 39.0% |
|  | **discard** | anything else | 98.7% | 5.2% |

One more thing after you switch: checking the other DR axis beats turning the EO's last move the other way. On 4c4e it adds 5.9 percentage points to the share of switched cases with a DR in 6 or less, against 2.1 for the last move ([section 8](eo-switch/#8-real-rzps-does-the-uniform-table-apply-after-a-switch)).

### Should I add some random moves to this EO?

**Yeah, if the EO leaves room for them. Random moves are an RZP: setup moves into a DR trigger ("Doing random moves, but in polish it abreviates to rzp", Yura Riabov, [23 Nov 2023](https://discord.com/channels/1007840975726575667/1007841273111117924/1177348166576783443)). Over all EO-solved states, with every option checked, 79.6% have a DR in 7 or fewer more moves, 25.7% in 6 or fewer and 4.4% in 5 or fewer. So if you want a DR in 10: an EO of 3 or less is usually worth RZPing, a 4-mover depends on its DRM, and a 5-mover needs one of the good DRMs.**

*Every option* means both DR axes, normal or inverse, and the EO's last move either way, all keeping the EO. Keep the EO while you add moves: among routes through EOs of 5 or less, breaking the EO reaches the optimal DR where nothing EO-keeping does on only 4 of 50,000 scrambles ([section 1](eo-to-dr/#1-the-short-version)).

*What you check:* how long the EO is, and the DRM it leaves on each DR axis (bad corners and bad edges for that DR), normal and inverse, before you add anything.

With a single DR axis and normal only, the odds drop to 5.9% for 6 or fewer more and 30.6% for 7 ([section 5.1](eo-to-dr/#51-the-typical-eo-to-dr-with-each-option)). By the DRM you start from ([section 5.2](eo-to-dr/#52-by-case)): each row is the DRM on the DR axis you look at. The second column is how common it is among all EO-solved states. The others say how often a state with that DRM has a DR within 5, 6 or 7 more moves (every option), or within 6 on that axis alone:

| DRM on the DR axis you look at | Share of all EO-solved states | DR in 5 or fewer more moves, every option (share of the row) | DR in 6 or fewer more, every option (share of the row) | DR in 7 or fewer more, every option (share of the row) | DR in 6 or fewer more, that one DR axis, normal only (share of the row) |
|---|---:|---:|---:|---:|---:|
| 3c2e | 0.33% | 44.9% | 93.4% | 100.0% | 61.6% |
| 2c2e | 0.17% | 13.8% | 63.7% | 99.7% | 23.7% |
| 4c2e | 1.2% | 12.2% | 51.9% | 96.4% | 18.7% |
| 4c4e | 6.5% | 13.9% | 51.1% | 95.2% | 19.2% |
| 7c8e | 2.2% | 9.7% | 43.8% | 93.8% | 16.4% |
| 8c8e | 0.56% | 6.5% | 42.5% | 95.3% | 14.5% |
| 3c4e | 1.7% | 6.5% | 39.6% | 93.6% | 9.9% |
| 5c4e | 8.7% | 5.0% | 31.4% | 88.2% | 7.2% |
| 4c6e | 8.7% | 3.9% | 24.2% | 79.4% | 4.6% |
| 5c6e | 11.6% | 4.1% | 27.2% | 84.9% | 6.1% |
| 6c6e | 12.7% | 3.5% | 25.1% | 82.4% | 5.6% |
| 6c4e | 9.6% | 3.0% | 20.5% | 75.6% | 3.0% |
| 7c6e | 7.0% | 2.5% | 20.9% | 78.9% | 4.0% |
| 7c4e | 5.2% | 2.3% | 16.1% | 68.6% | 2.2% |
| 6c8e | 4.0% | 2.7% | 19.7% | 77.4% | 3.2% |
| 3c6e | 2.3% | 4.1% | 25.2% | 80.8% | 4.8% |

The DRM matters more than the RZP does. A natural 4c4e or 4c2e has a DR in 6 or fewer more moves about half the time with every option, a 6c6e about one time in four. And a 6-move RZP is a much tougher target than a 4 or 5. On real attempts, after a switch, the share of cases with a DR in 5 after a 6-move RZP is 3.2 to 10.3 times smaller than the share with a DR in 6 after a 5-move one, depending on the DRM ([section 8](eo-switch/#8-real-rzps-does-the-uniform-table-apply-after-a-switch)). The DR lengths are optimal DRs after the EO, **computer only**. The DRM is the part you can actually read.

## DR to HTR

### Should I continue checking variants of this route?

**Yes, at least until the HTRs you're getting are 2 moves longer than the shortest one you know for that DR. On every subset, one route checked that far finds optimal more often than three routes where you only look at their shortest HTRs.** By variant I mean another way to follow the same route (different setup, different qt), which usually means a longer HTR.

*How I read the question.* "Variants" on the server usually means variations of moves you already have, so you might have meant variations of the DR itself (the last DR move the other way, a different trigger), not more HTRs on one route. The DR's last move is the one I can answer: turned the other way it gives a finish one move shorter on 32.5% of DRs, never more than one ([section 7](htr-routes/#7-extra-quarter-turns-and-the-last-dr-move)), so that's always worth a look. Other DR variations (other triggers, other DRs off the same RZP) aren't measured here.

*What you check:* the subset (first route per subset is in the table) and how long the HTRs you've found on it are.

For each corner subset, how often the first route of the HTR study's checklist finds optimal as you let its HTRs get longer, against trying more routes instead ([section 4](htr-routes/#4-the-checklists-subset-by-subset); 25,000 uniformly random DR states per subset × edges, pooled by exact subset size). *Up to 1 longer* means HTRs at most a move longer than the DR's shortest NISS HTR. 4c3 is 4a3 on one side and 4b3 on the other, 4c4 is 4a4/4b4, and a route uses the letter of the side it starts on:

| Subset | First route | Shortest HTRs only | Up to 1 longer | Up to 2 longer | Any HTR length | Three routes, shortest HTRs only | Two routes, up to 2 longer |
|---|---|---:|---:|---:|---:|---:|---:|
| 0c0 | `0c0 4a1 0c0` | 20.5% | 32.1% | 42.3% | 59.2% | 32.8% | 55.9% |
| 4a1 | `4a1 4b2 4a1 0c0` | 5.3% | 16.8% | 29.3% | 73.0% | 23.3% | 44.8% |
| 4a2 | `4a2 4a1 (0c0)` | 18.1% | 31.3% | 41.6% | 50.6% | 35.0% | 64.1% |
| 4b2 | `4b2 4a1 0c0` | 18.8% | 30.0% | 37.6% | 45.0% | 26.6% | 53.3% |
| 0c3 | `0c3 4a2 (4a1 0c0)` | 47.7% | 68.1% | 74.4% | 76.0% | 53.2% | 88.8% |
| 2c3 | `2c3 4b2 4a1 0c0` | 16.3% | 33.6% | 53.5% | 82.5% | 31.0% | 75.7% |
| 4c3 | `4a3 4b2 (4a1 0c0)` | 25.8% | 46.7% | 64.3% | 72.6% | 32.8% | 71.3% |
| 0c4 | `0c4 4a3 4b2 (4a1 0c0)` | 34.6% | 61.7% | 83.8% | 90.0% | 37.5% | 85.1% |
| 2c4 | `2c4 2c3 (4b2 4a1 0c0)` | 17.4% | 40.5% | 66.0% | 94.2% | 31.0% | 83.5% |
| 4c4 | `4b4 4a3 4b2 (4a1 0c0)` | 26.2% | 51.0% | 68.1% | 72.9% | 31.6% | 75.0% |
| 2c5 | `2c5 2c4 2c3 (4b2 4a1 0c0)` | 20.0% | 48.1% | 72.8% | 95.3% | 30.8% | 85.5% |
| 4b5 | `4b5 2c4 (2c3 4b2 4a1 0c0)` | 14.2% | 39.7% | 64.7% | 89.5% | 31.1% | 87.4% |

So on 0c4 the first route with HTRs up to 2 longer finds optimal on 83.8%, and three routes with only their shortest HTRs on 37.5%. The reason is that optimal rarely goes through a shortest HTR. Over all DRs, the shortest HTR that any optimal uses is a shortest NISS HTR on only 32.9%, 1 longer on 31.8% and 2 longer on 22.5% ([section 6](htr-routes/#6-shortest-htr-against-the-optimal)).

Past 2 longer the first route still has more in it (the *Any HTR length* column), but the HTRs keep getting longer and there are more of them to write at each length. Going to the second route instead, checked to 2 longer, gets you the gap between *Two routes, up to 2 longer* and *Up to 2 longer*. Where exactly to stop is a time question, and this card doesn't answer that. Which finish a route gives is the answer key, **computer only**. The "+2" is the habit you can actually keep.

### Should I NISS in the middle of this route?

**Depends on the subset and where you are on the route:**

- **Switch** on 4a2 at 4a1; on 0c3 at 4a2; on 4c3, 0c4, 4c4 at 4b2; on 2c4, 2c5 at 2c3; on 4b5 at 2c4.
- **Keep going on normal** on 0c0, 4a1, 4b2.
- **About even** on 2c3: both work about as often, so check both.

A switch after more than 2 moves on one side is needed on about one DR in eight (13.2%, more below).

*What you check:* which subset you started from, and which subset you're at now on normal.

I followed each subset's first route on normal. After each qt, here's how often an optimal finish keeps going on normal with no switch, how often one switches right there, and how often either one works (HTRs up to 2 longer than the shortest, 25,000 uniformly random DR states per subset × edges; same data as [section 4](htr-routes/#4-the-checklists-subset-by-subset)). *Better* is whichever way is ahead by 5 points or more. Each row is a point on a route:

| Subset | Where you are, on normal | Quarter turns so far | Keep going on normal finds the optimal | Switch now finds the optimal | Either | Better |
|---|---|---:|---:|---:|---:|---|
| 0c0 | `0c0 4a1` | 1 | 47.4% | 36.0% | 67.1% | keep going |
| 4a1 | `4a1 4b2` | 1 | 30.2% | 22.4% | 43.2% | keep going |
| 4a1 | `4a1 4b2 4a1` | 2 | 29.5% | 18.0% | 41.1% | keep going |
| 4a2 | `4a2 4a1` | 1 | 53.1% | 64.2% | 78.6% | switch |
| 4b2 | `4b2 4a1` | 1 | 40.9% | 22.9% | 50.2% | keep going |
| 0c3 | `0c3 4a2` | 1 | 40.7% | 85.7% | 86.1% | switch |
| 2c3 | `2c3 4b2` | 1 | 54.5% | 53.5% | 78.7% | about even |
| 2c3 | `2c3 4b2 4a1` | 2 | 53.8% | 51.3% | 76.4% | about even |
| 4c3 | `4a3 4b2` | 1 | 28.7% | 68.2% | 72.2% | switch |
| 0c4 | `0c4 4a3` | 1 | 33.0% | 33.1% | 52.8% | about even |
| 0c4 | `0c4 4a3 4b2` | 2 | 33.0% | 84.9% | 86.5% | switch |
| 2c4 | `2c4 2c3` | 1 | 49.6% | 66.1% | 83.6% | switch |
| 4c4 | `4b4 4a3` | 1 | 23.4% | 35.5% | 47.2% | switch |
| 4c4 | `4b4 4a3 4b2` | 2 | 23.4% | 69.9% | 71.2% | switch |
| 2c5 | `2c5 2c4` | 1 | 50.7% | 45.9% | 70.6% | about even |
| 2c5 | `2c5 2c4 2c3` | 2 | 50.7% | 72.8% | 85.6% | switch |
| 4b5 | `4b5 2c4` | 1 | 43.9% | 67.5% | 80.9% | switch |

The *Either* column is the argument for checking both. On 2c3 after one qt, keeping going finds it 54.5% of the time and switching 53.5%, but one or the other 78.7%.

Late switches: with HTRs up to 2 longer, optimal needs a switch after more than 2 moves on 13.2% of DRs (7.8% of 4b2, 9.1% of 2c3), and after 4 or more on 5.1% ([section 11](htr-routes/#11-the-claims-checked)). Which finishes exist is **computer only**. Where to switch is the part you use.

---

Sources: the studies linked from each card ([DR-xs](is-dr-xs-worth-it/), [EO to DR](eo-to-dr/), [EO switch](eo-switch/), [HTR routes](htr-routes/)). The two tables made for this page (when to stop looking for EOs, and switching mid-route) come from those studies' data, computed by the scripts in the repo's `cards/` folder.
