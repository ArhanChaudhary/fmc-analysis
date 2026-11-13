# Decision cards

Six questions that come up mid-attempt, one card each, by stage. Each card opens with the answer as a rule you can use at the table, then the numbers behind it and the study section they come from. Everything is measured, not guessed: exact counts or large uniform samples, the same data as the studies. The questions:

- EO: [Should I add some partial EOs to my list?](#should-i-add-some-partial-eos-to-my-list) · [Should I stop looking for EOs and move to the next stage?](#should-i-stop-looking-for-eos-and-move-to-the-next-stage)
- EO to DR: [Should I switch this EO?](#should-i-switch-this-eo) · [Should I add some random moves to this EO?](#should-i-add-some-random-moves-to-this-eo)
- DR to HTR: [Should I continue checking variants of this route?](#should-i-continue-checking-variants-of-this-route) · [Should I NISS in the middle of this route?](#should-i-niss-in-the-middle-of-this-route)

**How to read the cards.** *What you check* is what you can see in an attempt. Where a number counts every DR or every finish that exists, a search you can't do by hand, it says **computer only**: that's the answer key, and what carries over to an attempt is the comparison, not the length. Shares are of uniformly random scrambles or states unless a line says otherwise. None of these cards has a clock in it: they say what the next thing is worth, not how long it takes you. Routes are written as in the HTR study: subsets after each quarter turn, the part in brackets on the other side, `4b2 2c3 (4b2 4a1 0c0)`.

November 2026. A date in brackets is a link to that message on the FMC solvers Discord.

## EO

### Should I add some partial EOs to my list?

**Yes: the slice-EO skips, once your EOs of 4 or less are written, and before the 5-movers.** A partial EO on the server is a slice EO, with one or two slices' edges oriented and the rest fixed later ("Doing partial EO saves ~3 moves in the EO step", sqAree, [23 Jan 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1464341592952537128)). It leads to a DR-1s (one slice to fix) or a DR-2s 8fe.

*What you check:* whether an EO axis has a slice skip on either side, and then the DR-1s length. Judge a DR-1s of $N$ like a normal DR of about $N + 2$.

How much one is worth. On 500 real scrambles, the number of each kind of thing you'd finish, on average, for one to give the best solution any normal DR of 12 or less gives on its scramble (DR-xs, [section 7.2](is-dr-xs-worth-it/#72-what-each-one-is-worth)). Each row is what you finish:

| What you finish | One in this many gets the scramble's best |
|---|---:|
| a DR-1s of 6 or less | 12 |
| a DR-1s of 7 | 49 |
| a normal DR of 9 or less | 41 |
| a DR-1s of 8 | 210 |
| a 10-move DR | 202 |
| an 11-move DR | 952 |

So a DR-1s of 7 is about a DR of 9 and a DR-1s of 8 about a DR of 10. On average a DR-1s costs 2.27 more moves in the finish than a DR ([section 5.2](is-dr-xs-worth-it/#52-by-subset)).

What they add next to 5-move EOs. Same scrambles, starting from the EOs of 4 or less and their DRs of 10 or less; each row adds one set of things to finish, and the number is how much shorter the average best solution gets ([section 7.4](is-dr-xs-worth-it/#74-against-5-move-eos)):

| Added on top of the EOs of 4 or less | Average best solution shorter by, moves |
|---|---:|
| every DR-1s of 8 or less from a slice EO | 0.36 |
| only the DR-1s of 7 or less | 0.17 |
| every 5-move EO | 0.71 |
| both | 0.91 |

The 5-movers give more, but they are about 253 more EOs per scramble, and the slice EOs take far less looking. Skips are common: 68.7953% of scrambles have one on normal, 79.3147% counting inverse (exact). They clump, though: 2.25 per scramble on average over both sides, and 21% of scrambles have none ([section 6.1](is-dr-xs-worth-it/#61-how-often-there-is-a-slice-eo-skip)). The finishes behind the two tables are the best of the method's form, **computer only**; the order is what you use.

A DR-2s 8fe is a different story: a skip isn't how you get one ([section 6.3](is-dr-xs-worth-it/#63-to-a-dr-2s-8fe-the-same-problem-as-a-dr)).

### Should I stop looking for EOs and move to the next stage?

**Once your EOs of 4 or less give a DR of 9 or better, move on: the 5-movers beat it on 11.0% of those scrambles. At 10 they beat it on 44.5%, at 11 on 90.8%.** That's counting EOs on both sides and NISS EOs; with normal EOs only the 5-movers help less often at each row, and 9 or better is still where they stop paying (table below).

*What you check:* the best DR you have through your EOs of 4 or less.

On 50,000 uniformly random scrambles, take the best DR through every EO of 4 or less (EO plus EO-keeping turns, total length, either of the two other axes; all three EO axes), and ask what the EOs of exactly 5 add, then the EOs of 6. Each row is the best DR the short EOs give:

| Best DR through your EOs of 4 or less | Share of scrambles | 5-move EOs give a shorter DR | Average shortening from the 5-movers, moves | Then 6-move EOs give a shorter DR still |
|---|---:|---:|---:|---:|
| 8 or less | 10.4% | 3.4% | 0.04 | 4.8% |
| 9 | 32.0% | 13.5% | 0.16 | 16.7% |
| 10 | 39.8% | 44.5% | 0.53 | 37.0% |
| 11 | 12.7% | 90.8% | 1.22 | 40.4% |
| 12 or more | 1.0% | 100.0% | 2.06 | 42.0% |
| no EO of 4 or less | 4.0% | 99.7% | – | 45.3% |

The same with normal EOs only (no inverse, no NISS):

| Best DR through your EOs of 4 or less | Share of scrambles | 5-move EOs give a shorter DR | Average shortening from the 5-movers, moves | Then 6-move EOs give a shorter DR still |
|---|---:|---:|---:|---:|
| 8 or less | 4.2% | 2.2% | 0.03 | 2.8% |
| 9 | 15.7% | 6.7% | 0.08 | 8.1% |
| 10 | 33.0% | 24.7% | 0.29 | 24.3% |
| 11 | 22.0% | 65.6% | 0.82 | 38.5% |
| 12 or more | 3.6% | 98.4% | 1.62 | 40.7% |
| no EO of 4 or less | 21.5% | 97.8% | – | 49.7% |

Read the rows as "what's still out there": the DRs counted are the best that exist through each EO, **computer only**. By hand you find some of them, so your best is often a move worse than the row you're in, and the row one move better is closer to your odds. Two more numbers that help decide when you've seen enough EOs ([section 4.1](eo-to-dr/#41-how-many-eos-how-short), [section 3.3](eo-to-dr/#33-how-many-drs)):

- A scramble has 15.3 normal EOs of 4 or less on average over the three axes (median 12, counted the way nissy's `-a` lists them), and 43.9 with inverse and NISS EOs. 21.5% of scrambles have no normal EO of 4 or less.
- For a DR in 10, one EO of 4 or less is worth about ten 5-movers: 25 EOs of at most 4 give 4.0 DRs of 10 or less on average, 200 EOs of exactly 5 give 3.5. For a DR in 11 the 5-movers win (17.3 against 23.7).

## EO to DR

### Should I switch this EO?

**For 4c4e, count the half turns to two bars with U and D turns free: 0 or 1, switch (certain); 2, switch; 3, your call; 4 or 5, discard. For the other DRMs, use the pair card below.** Switch means: after EO + RZP, go to the inverse, keep the EO and look for a DR there. Sub-7 means a DR in 6 or less on the switched side.

*What you check:* on 4c4e, the two rings and the count when you have 2 or more pairs; otherwise the card's pairs, side pairs, ARM or corner case on the switched case ([section 4.4](eo-switch/#44-reading-the-count)).

4c4e by the half turns to two bars, exact over all 4c4e cases ([section 4.3](eo-switch/#43-the-bands)). Each row is a count:

| Half turns to two bars | Verdict | Share of 4c4e | Sub-7 rate |
|---|---|---:|---:|
| 0 or 1 | **switch**, certain | 1.0% | 100% |
| 2 | **switch** | 13.2% | 72.1% |
| 3 | **your call** | 51.0% | 16.0% |
| 4 or 5 | **discard** | 34.8% | 1.7% |

By hand you can read the switch end, not the discard end: with 2 or more pairs you can read the count (2 or fewer is 12.4% of 4c4e at 74.1%), and with 0 or 1 pair the reading only says "3 or more", so use the card. The two bars as the target come from Andrew's 2019 video and rodneykinney's *DR - 4c4e Theory*; the exact count and its bands are the study's ([section 4](eo-switch/#4-two-rings-count-the-half-turns-4c4e)).

The pair card for every DRM, exact over all its cases ([section 6](eo-switch/#6-the-switch-cards-drm-by-drm)). Each row is one verdict group of a DRM's card: what to check on the switched case, the share of the DRM in the group, and its sub-7 rate:

| DRM | Verdict | What the switched case shows | Share of the DRM | Sub-7 rate |
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

These hold after any RZP: the switched case is exactly uniform whatever path made it, so the tables apply as they are ([section 8](eo-switch/#8-real-rzps-does-the-uniform-table-apply-after-a-switch)). After the switch, checking the other DR axis adds more than turning the EO's last move the other way: 5.9 points against 2.1 on 4c4e.

### Should I add some random moves to this EO?

**Yes, when the EO leaves room for them: with every option checked, an EO-solved cube has a DR within 7 more moves 79.6% of the time, within 6 25.7%, within 5 4.4%. So toward a DR in 10, an EO of 3 or less is usually worth it, an EO of 4 depends on its case, and an EO of 5 needs one of the good cases.** Random moves are an RZP, setup moves to a DR trigger ("Doing random moves, but in polish it abreviates to rzp", Yura Riabov, [23 Nov 2023](https://discord.com/channels/1007840975726575667/1007841273111117924/1177348166576783443)). Keep the EO while you do it: among routes through an EO of at most 5, turns that break the EO reach the optimal DR where no EO-keeping one does on 4 of 50,000 scrambles ([section 1](eo-to-dr/#1-the-short-version)).

*What you check:* the EO's length, and its case (bad corners and edges out of place) on each DR axis, normal and inverse, before any random moves.

With every option (two DR axes, normal or inverse, the EO's last turn either way, all keeping the EO), the chance of a DR within 5, 6 or 7 more moves is 4.4%, 25.7% and 79.6%; on one DR axis alone it's 5.9% for 6 and 30.6% for 7 ([section 5.1](eo-to-dr/#51-the-typical-eo-to-dr-with-each-option)). By the case you start from ([section 5.2](eo-to-dr/#52-by-case)), the named good cases first, then the common ones. Each row is the case on the DR axis you look at; the middle columns use every option, the last one that axis alone:

| Case on the DR axis | Share of EO-solved states | DR in ≤ 5 more | DR in ≤ 6 more | DR in ≤ 7 more | DR in ≤ 6 more, that axis alone |
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

The case decides more than the RZP does: a natural 4c4e or 4c2e has a DR within 6 more about half the time with every option, a 6c6e one time in four. A 6-move RZP has a much harder target than a 4- or 5-move one: on real attempts, after a switch, the chance of a DR in 5 after a 6-move RZP is 3.2 to 10.3 times smaller than the chance of a DR in 6 after a 5-move one, depending on the DRM ([section 8](eo-switch/#8-real-rzps-does-the-uniform-table-apply-after-a-switch)). The DR lengths are optimal DRs after the EO, **computer only**; the case is what you read.

## DR to HTR

### Should I continue checking variants of this route?

**Yes, at least until the HTRs you're getting on it are 2 moves longer than the shortest HTR you know for the DR. On every subset, one route checked that far finds the optimal more often than three routes checked with their shortest HTRs only.** A variant here is another way of following the same route (another setup, another quarter turn), which usually means a longer HTR.

*What you check:* the subset (the first route per subset is below) and the length of the HTRs you've found on it.

For each corner subset, the share of DRs where the first route of the HTR study's checklist finds the optimal, as you let its HTRs get longer, against trying more routes ([section 4](htr-routes/#4-the-checklists-subset-by-subset); 25,000 uniformly random DR states per subset × edges, pooled by the exact subset sizes). *Up to 1 longer* means HTRs at most one move longer than the DR's shortest NISS HTR. Each row is a corner subset (4c3 is 4a3 on one side and 4b3 on the other, 4c4 is 4a4/4b4; a route names the side it starts on):

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

So on 0c4 the first route with HTRs up to 2 longer finds the optimal on 83.8%, and three routes with shortest HTRs only on 37.5%. That's because the optimal finish rarely goes through a shortest HTR: over all DRs, the shortest HTR any optimal uses is a shortest NISS HTR on only 32.9%, 1 longer on 31.8% and 2 longer on 22.5% ([section 6](htr-routes/#6-shortest-htr-against-the-optimal)). Past 2 longer the first route still has more to give (*Any HTR length*), but through ever longer HTRs, with more of them to write at each length; the second route checked to 2 longer adds the difference between *Two routes, up to 2 longer* and *Up to 2 longer*. Where to stop is the time question this card doesn't answer. Which finish the route gives is the answer key, **computer only**; the budget is the habit you can keep.

### Should I NISS in the middle of this route?

**It depends on the subset and on where you are on the route:**

- **Switch** on 4a2 at 4a1; on 0c3 at 4a2; on 4c3, 0c4, 4c4 at 4b2; on 2c4, 2c5 at 2c3; on 4b5 at 2c4.
- **Keep going on normal** on 0c0, 4a1, 4b2.
- **About even** on 2c3: either works about as often, and checking both is what pays.

A switch after more than 2 moves on one side is needed on about one DR in eight (13.2%, below).

*What you check:* the subset you started from and the subset you're at now on normal.

Follow the first route of each subset on normal. After each quarter turn, the share of the subset's DRs where an optimal finish keeps going on normal with no switch, where one switches right there, and where either does (HTRs up to 2 longer than the shortest, 25,000 uniformly random DR states per subset × edges; data of [section 4](htr-routes/#4-the-checklists-subset-by-subset)). *Better* is the way that's ahead by 5 points or more. Each row is a point on a route:

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

The *Either* column is the case for checking both: on 2c3 after one quarter turn, keeping going finds it on 54.5% and switching on 53.5%, but one or the other on 78.7%. Late switches: with HTRs up to 2 longer, the optimal needs a switch after more than 2 moves on 13.2% of DRs (7.8% of 4b2, 9.1% of 2c3), and after 4 or more on 5.1% ([section 11](htr-routes/#11-the-claims-checked)). Which finishes exist is **computer only**; where to switch is what you use.

---

Sources: the studies linked from each card ([DR-xs](is-dr-xs-worth-it/), [EO to DR](eo-to-dr/), [EO switch](eo-switch/), [HTR routes](htr-routes/)). The two tables made for this page (when to stop looking for EOs, and switching mid-route) are computed from those studies' data by the scripts in the repository's `cards/` folder.
