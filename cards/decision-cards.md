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

**Count the pairs on the inverse like you do now, then take one more look, and which one depends on the pair count. On 4c4e: 3 or 4 pairs, switch. 2 pairs on two edges, switch. 2 pairs on one edge, switch if there are 2 fake pairs or if the two E-slice edges that are out of the slice share red or orange. 1 pair, check ARM: with ARM 21 switch 4d corners, 4b corners unless there's exactly one side pair, and 4a corners in two columns (Evan's stacked corners) with a side pair; with ARM 20 or 22 only that last one. 0 pairs, only if there's no fake pair either and the misoriented corners are two white and two yellow. That switches 26.0% of 4c4e, the same as 2+ pairs (26.0%), and it misses no case of 4 or less (2+ pairs: 8.0%), 5.3% of the 5-movers (20.4%) and 32.8% of the 6-movers (42.8%).**

Switching means: after EO + RZP, go to the inverse, keep the EO and look for a DR there. All the odds on this card are for the switched side and are exact, over every EO-solved case of the DRM. They hold after any RZP, because given what you see on normal the switched case is spread evenly over its DRM ([section 3](eo-switch/#3-definitions-and-the-yardstick)). A case is an N-mover if its shortest DR after the switch has N moves.

*What you check:* everything is a colour match on the side you're on ([section 6](eo-switch/#6-reading-the-card-on-normal-and-how-long-it-takes)): the U/D edges in the E slice, the misoriented corners with the colour they show on the U/D face, and the E-slice edges that are out of the slice. Pairs by wen's tracing, edge by edge, so you know whether 2 pairs sit on one edge or on two. Fake pairs are the corners that have an edge's two colours the wrong way round. ARM is the red/orange on U/D and the green/blue on those edges.

**4c4e.** Each row is a group of switched cases. The last three columns say how much of all of 4c4e's 4-or-less, 5-movers and 6-movers sits in the row:

| What you read (4c4e) | Verdict | Share of 4c4e | Sub-7 rate | Of its 4-or-less | Of its 5-movers | Of its 6-movers |
|---|---|---|---|---|---|---|
| 3 or 4 pairs | **switch** | 3.6% | 79.9% | 57.4% | 21.0% | 11.0% |
| 2 pairs on two edges | **switch** | 11.9% | 53.9% | 31.1% | 46.5% | 30.4% |
| 2 pairs on one edge (a bar), holes on one R/L face | **switch** | 3.5% | 43.7% | 3.5% | 9.8% | 7.8% |
| 2 pairs on one edge (a bar), holes not on one R/L face, 2 fake pairs | **switch** | 0.68% | 41.7% | 0% | 0.97% | 1.7% |
| 1 pair, ARM 21, 4d corners | **switch** | 0.82% | 88.9% | 5.5% | 3.9% | 3.7% |
| 1 pair, ARM 21, 4b corners, 0 or 2 side pairs | **switch** | 2.8% | 50.4% | 0% | 6.4% | 8.0% |
| 1 pair, ARM 20, 21 or 22, 4a corners in two columns, 1+ side pairs | **switch** | 1.8% | 40.7% | 0% | 5.1% | 3.8% |
| 0 pairs, no fake pairs, corners 2 and 2 in the layers | **switch** | 0.82% | 21.9% | 2.4% | 0.97% | 0.84% |
| 2 pairs on one edge (a bar), holes not on one R/L face, 0 or 1 fake pairs | if you have time | 6.3% | 15.5% | 0% | 1.3% | 6.3% |
| 1 pair, ARM 10 or 11, 2 or 3 side pairs | if you have time | 4.1% | 23.3% | 0% | 0.64% | 6.2% |

Everything else is a skip.

**Against what people switch now.** Each row is a rule over all 4c4e cases:

| Policy | From | Switched | Missed: 4 or less | Missed: 5-movers | Missed: 6-movers | Cost per case |
|---|---|---|---|---|---|---|
| 2+ pairs | *DRM Subsets Meta*; tseitsei89, [25 Aug 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1409603207239307457) | 26.0% | 8.0% | 20.4% | 42.8% | 0.413 |
| 2+ pairs, or 1 pair with 4d corners | tseitsei89, [25 Aug 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1409579685716689018) | 27.7% | 2.4% | 16.6% | 39.2% | 0.381 |
| 2+ pairs; 1 pair with ARM 21; 0 pairs with JZP or ARM 42 | Fanti, [6 Nov 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1436034830046466069) | 35.2% | 1.4% | 5.8% | 27.0% | 0.345 |
| **the card** | this page | 26.0% | 0% | 5.3% | 32.8% | 0.282 |
| the card with its *if you have time* groups | this page | 36.4% | 0% | 3.4% | 20.3% | 0.304 |

So it beats 2+ pairs at every length for no more switches. Against the pairs + ARM list (2+ pairs, 1 pair with ARM 21, 0 pairs with JZP or ARM 42) it switches 9.3 points less, misses no 4-or-less and a few 5-movers fewer, and leaves more 6-movers. With the two *if you have time* rows it misses less at every length for 1.1 points more switches.

**The other DRMs.** What to switch, one row per group ([section 5](eo-switch/#5-the-cards) has the full cards, with the groups to add if you have time):

| DRM | Switch when | Share of the DRM | DR in 6 or less after the switch (share of the row) |
|---|---|---|---|
| 4c2e | 2 pairs (a bar) | 7.1% | 60.0% |
| 4c2e | 1 pair and a side pair | 15.1% | 55.5% |
| 4c2e | 0 pairs, JZP (ARM 00) with 4b corners | 0.71% | 66.7% |
| 4c2e | 1 pair, no side pair, 4b-0 corners | 1.8% | 43.3% |
| 3c2e | 1 pair | 37.5% | 88.7% |
| 3c2e | 0 pairs, a fake pair or a split pair | 44.6% | 56.5% |
| 7c8e | 6 pairs, not ARM 64 | 1.9% | 96.5% |
| 7c8e | 5 pairs, not ARM 20 or 54 | 13.9% | 55.9% |
| 7c8e | 4 pairs, ARM 21, 31 or 43 | 6.5% | 34.9% |
| 7c8e | 3 pairs, ARM 21 | 0.61% | 27.8% |
| 8c8e | 8 pairs | 0.07% | 100% |
| 8c8e | 6 pairs, corner ARM 4 | 3.7% | 50.0% |
| 8c8e | 5 pairs, edge ARM 1 or 3 | 11.7% | 45.5% |
| 8c8e | 2 pairs, ARM 42 | 2.7% | 32.5% |
| 8c8e | 4 pairs, ARM 42 | 9.8% | 25.2% |
| 2c2e | 1 pair | 21.4% | 62.5% |
| 2c2e | 2 pairs and a side pair | 0.45% | 100% |
| 2c2e | 0 pairs, 1 side pair, ARM 00 or 11 | 7.1% | 68.8% |
| 4c6e | 4 pairs on three edges | 0.85% | 74.0% |
| 4c6e | 3 pairs, JZP (ARM 00) | 0.31% | 61.1% |
| 4c6e | 3 pairs on three edges, the three bad edges in one layer | 0.27% | 62.5% |
| 4c6e | 3 pairs on three edges, corners 2 and 2 in the layers | 2.2% | 25.8% |
| 3c4e | 2 pairs and a side pair | 6.9% | 43.2% |
| 3c4e | 2 pairs, no side pair, a fake pair | 1.9% | 27.3% |
| 3c4e | 1 pair, 2 side pairs | 5.7% | 28.1% |
| 3c4e | 1 pair, ARM 21, 1 side pair, 2 fake pairs or holes on one R/L face | 2.6% | 40.3% |
| 3c6e | 2 pairs, ARM 21, 1 or 2 fake pairs | 4.1% | 31.3% |
| 3c6e | 2 pairs, ARM 12, 2 fake pairs | 1.4% | 38.6% |
| 3c6e | 2 pairs, ARM 01 | 1.5% | 22.9% |
| 5c4e | 3 pairs, 2+ side pairs | 2.2% | 38.3% |
| 5c4e | 2 pairs, ARM 21, 2+ side pairs | 2.8% | 32.7% |
| 5c4e | 1 pair, ARM 21, 2+ side pairs, 2+ fake pairs | 1.8% | 24.3% |
| 5c6e | 4 pairs | 3.1% | 37.9% |
| 5c6e | 3 pairs, ARM 21, 3 side pairs | 1.2% | 38.3% |
| 5c6e | 2 pairs, ARM 21, 3 side pairs | 2.0% | 20.6% |
| 6c6e | 5 or 6 pairs | 1.2% | 39.0% |
| 6c6e | 3 pairs, 3 fake pairs, corners 3 and 3 in the layers | 1.9% | 34.1% |

For 4c6e, 3c4e, 3c6e, 5c4e, 5c6e and 6c6e these are small pockets in DRMs that are 5% to 10% sub-7 overall. A short DR out of them costs about four times the tracing it costs on 4c4e, so they're for when the good DRMs have run dry.

**Half turns to two bars** (how many R2, L2, F2, B2 until each layer has a bar and both stuck E-slice edges are on that R/L side, U and D turns free) is a good read on a cube you can see: 2 or fewer is 74.1% sub-7 and holds every 4-or-less. Before switching it needs the place of all eight bad pieces on the inverse and then a search, and nobody has shown that done in a few seconds, so it's not on this card. If you can read it, *2 or fewer: switch* on top of the card takes the missed 5-movers from 5.3% to 3.2% ([section 7](eo-switch/#7-two-bars-evaluated)).

One more thing after you switch: checking the other DR axis beats turning the EO's last move the other way. On 4c4e it adds 5.9 percentage points to the share of switched cases with a DR in 6 or less, against 2.1 for the last move.

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

The DRM matters more than the RZP does. A natural 4c4e or 4c2e has a DR in 6 or fewer more moves about half the time with every option, a 6c6e about one time in four. And a 6-move RZP is a much tougher target than a 4 or 5. On real attempts, after a switch, the share of cases with a DR in 5 after a 6-move RZP is 3.2 to 10.3 times smaller than the share with a DR in 6 after a 5-move one, depending on the DRM ([section 10](eo-switch/#10-other-rzp-lengths-real-attempts-other-weights)). The DR lengths are optimal DRs after the EO, **computer only**. The DRM is the part you can actually read.

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
