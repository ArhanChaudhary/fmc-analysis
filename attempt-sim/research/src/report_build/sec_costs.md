## 4. The time costs and the human limits

Every number here is a first guess, and they are what you would tune. Each row has its value, where it comes from, and how sure I am of it. *High* means a stated rule or a measured fit, *medium* means several solvers' figures agree roughly, *low* means a guess with little or nothing behind it.

The time of one step, in seconds (nominal; the real time of each step is this times a random factor, see the last rows):

| Step | Cost, s | Source | Confidence |
|---|---|---|---|
| look: count bad edges on 3 axes | 15 | none measured; Enrico counts them before writing EOs ([[D3721]]) | low (small) |
| EO scan, one axis to length 1 / 2 / 3 / 4 / 5 | 2 / 3 / 5 / 10 / 30 | 50 s per axis to length 5, under 3 minutes for all three: Jay's "sub 2 minute passes" over the six axis-sides ([[T3679]]), Fanti "~1m30" for 2+2 EOs on all axes without writing ([[D11474]]) | medium |
| EO scan with NISS EOs too | × 1.5 | guess | low |
| EO write, per EO | 8 | Yura Riabov: 90 written in 11 minutes ([[D10122]]), 7.3 s each; Kai Cui about 50 in 10 minutes ([[D7299]]); FakeMMAP 26 in about 6 ([[D10128]]) | medium |
| glance at one EO | 5 | Yura Riabov: "3-5 to discard if it doesn't lead to short dr" for a 4-mover ([[D11076]]) | medium |
| work one RZP state | 15 | tseitsei89: "You should spend like 10-30s per rzp" ([[T8930]]) | medium |
| switch (set up the other side, work the state) | 25 | Jay: NISSing for trigger in 5 "tends to cost me around 30 seconds" ([[T487]]); Evan: "20 seconds to scramble" ([[D6530]]) | medium |
| write a DR seen 0 / 1 / 2 / 3 / 4 / 5 / 6 / 7 moves away | 3 / 3 / 5 / 8 / 12 / 20 / 30 / 45 | guess (longer DRs take longer to find and write) | low |
| read a DR (corner case and edges, last quarter turn either way) | 15 | no measured figure; Tom Nelson: "it takes like 0.5 seconds to note down" the bad-edge count ([[D3993]]) | low |
| try one HTR route | 40 | Tom Nelson: "5 seconds to see if it's good or not" for a long HTR ([[D3665]]), "30 seconds to check those kinds of variants" ([[D3649]]) | low |
| write out the finish a route gave | 30 | tseitsei89: a 4-QT slice "in probably less or at least around 1 minute" ([[T9121]]) | low |
| write the solution on the sheet and check it | 150 | Radek: with 16 of 21 moves written in the last minute, "realistically I needed an extra minute to submit 21" ([*Sub 22 Official Mean Stats*](https://docs.google.com/spreadsheets/d/17L6vArP8t_5yPIeCpiQpp66YBZcLcbxS10hzYtnB-XE/edit?gid=0), tab "Radek 21.00 (Euros 2024)") | medium-low |
| spread of one step's time (log-normal) | 0.25 | guess; it mostly sets how often the final write runs over | low |
| spread of the pace from attempt to attempt | {{V:cal_attempt_sigma}} | fitted: the baseline's DNF rate matches the top 5's (section 5) | fitted |

What the solver sees (chances, or a spread in moves):

| Limit | Value | Source | Confidence |
|---|---|---|---|
| an EO on one side, found when its axis is searched to its length: 3 / 4 / 5 moves | 1 / 0.95 / 0.75 | guess; jaye writes "all the sub 5 move eos/the obvious 5 movers" ([[D3722]]) | low |
| a NISS EO (moves on both sides): 2-3 / 4 / 5 moves | 0.9 / 0.7 / 0.3 | guess | low |
| a DR 3 / 4 / 5 / 6 moves away, seen at the glance | 0.9 / 0.6 / 0.25 / 0.05 | guess | low |
| a DR 4 / 5 / 6 / 7 moves away, seen from a worked RZP state | 0.95 / 0.8 / 0.5 / 0.15 | guess; *DR Miss* is the largest of Zagros's miss counts (34% of 34 solves, [[D20197]]) | low |
| a route with a short finish gives it when tried | 0.9 | guess; Yura Riabov's log marks a finish miss in 11 of 138 attempts | low |
| reading error of an RZP state's distance to DR, moves | 1.0 | about the EO-switch paired-edge card (section 3.2) | medium |
| ranking of RZP states: weight of moves already made | 0.6 | guess | low |
| spread of the form from attempt to attempt | {{V:cal_form_sigma}} | tried at 0.3 to 1.0: it makes bad days worse (more DNFs, a higher mean) but adds no sub-20s, so it can't produce the real spread (section 5); left out | tried |

### 4.1 What to tell me to tune them

These are the answers that would move the results most, in the order section 11 measured (how much the tuned plan's result moves when each one is halved or doubled):

1. **Your read of an RZP state.** When you look at an RZP state and think it's a DR in 6, how often is it? The simulator's read is off by about a move (spread 1). Twice as noisy costs half a move overall, half as noisy gains 0.15, so this is the big one. It also decides the read cut-off: with a much noisier read, 9 beats 10.
2. **What you see from an RZP.** From a state 4, 5 or 6 moves from DR, how often do you actually find that DR? The simulator uses 0.95, 0.8 and 0.5.
3. **Per route on a DR.** How long does trying one HTR route take you, finding the HTR and seeing its finish? The simulator uses 40 s and tries 4 routes on a DR it likes.
4. **How much your step times vary.** Some RZPs take 5 seconds and some take a minute. The simulator spreads every step's time by about 25%. If yours vary a lot more, keeping 10 minutes for writing starts to pay instead of 7.
5. **The final write.** How long do you need to write the solution down and check it? The simulator uses 2.5 minutes, and the tuned plan keeps 7 minutes for it.
6. **EOs.** Seconds to write one (8 here), to glance at one and throw it away (5), and how many 5-movers you miss.
7. **Writing out a finish, reading a DR, RZP and switch.** 30 s, 15 s, 15 s and 25 s here. Each of these moves the result by 0.05 or less when halved or doubled.
