## 3. The simulated attempt

The simulator plays an attempt pretty much the way the guides describe one: write EOs, glance at each one and work the promising RZPs, write down the DRs you see, then try HTR routes on the best DRs and write the best solution down. Everything the solver looks at costs time, and then the hour runs out. The cube part is real: it runs on real scrambles, every EO, RZP, DR, HTR and finish it writes down actually exists on that scramble, and every solution it submits solves it (all of them get replayed). What's *modelled* is the solver: how long each step takes, what you see and what you miss, and the plan that decides what to look at next.

### 3.1 The steps and what each one costs

One attempt is a sequence of steps, each with a time cost. The clock is the sum of the costs. The steps, in the order an attempt meets them:

| Step | What the solver does | What it reveals to the solver |
|---|---|---|
| look | count the bad edges on the three axes | the bad-edge counts |
| EO scan | search one axis (both sides) for EOs one move longer than before | the EOs of that length on that axis that the solver *sees* (some are missed) |
| EO write | write one EO down | |
| glance | look at one EO on both DR axes, for each way of making its last quarter turn | each line's DRM, read as a guess of the distance to DR, and any DR in plain sight |
| RZP | work one RZP state: one more EO-keeping turn on the side the EO ended | the state's read; the DR if it is close enough and the solver sees it |
| switch | set up the other side and work the state there (NISS) | the same, on the other side |
| DR write | write a DR down | its length |
| DR read | read a DR's corner case and edges, for the last quarter turn either way | its subset, so a guess of its finish |
| route | try one HTR route on a DR, from the htr-routes checklist of its subset | a finish along that route, if the solver finds it |
| finish write | write out the finish the route gave | a full solution and its length |
| write | write the solution on the sheet and check it on the cube | the attempt's result, if it ends inside the hour |

Two kinds of randomness make it play like a person. First, time: each step takes its nominal cost times a random factor (one draw per step and object, so the same EO costs the same under every plan), and the whole attempt runs at a pace drawn once per attempt, so some attempts are just slower. Second, misses: a 5-move EO is seen with some chance, a DR 5 moves from an RZP state with some chance, a route that has a short finish gives it with some chance. There's also a *form* setting (missing less on a good day), but it's switched off in every run here (section 4 says why). Section 4 lists every cost and every chance.

### 3.2 What the solver knows and how it picks

The solver never sees the answer key. It knows only what its steps revealed: lengths, bad edges, the DRM of a state as a *read* of how far the DR is, the subsets of the DRs it read, the finishes it found. The read of a state is its true EO-keeping distance to DR plus a reading error (spread 1 move, see section 4). That spread is calibrated against the EO-switch study: with it, the solver flags 18.5% of 4c4e cases as 6 or less to DR and 60.8% of those are, close to the paired-edge card of that study (15.5% at 59.9%).

How the hour is spent is the *policy*. The baseline policy is the guides' plan, breadth first:

1. Count bad edges. Scan the axes for EOs up to 5 moves (NISS EOs included), the axes with the fewest bad edges first, and write them down until minute 8 or 40 EOs.
2. From minute 8: glance at the EOs, shortest first. Work up to 3 RZP states per EO of 4 moves or less (1 for 5-movers), most promising read first, a switch ranked 0.3 moves worse than staying on the same side, at most 3 RZP moves, only states whose read promises a DR of 11.5 moves or less. Write down every DR of 11 or less that is seen, and read its subset.
3. From minute 35: finish the DRs, the lowest expected total first, up to 4 routes each, skipping a DR whose chance (by subset) of beating the best solution so far is under 3%.
4. Keep 5 minutes to write the best solution down.

When a phase runs out of work early the solver goes back to whatever is left (more RZP states per EO, a looser read limit, more EOs), so the minutes in the plan are when the solver *switches priority*, not walls: a solver who has finished their DRs at minute 40 goes back to looking for more.

### 3.3 Finishing a DR

A DR in the simulator is a state of the DR group with a known subset (judging-a-dr's model). The solver tries routes to HTR from the htr-routes checklist of that subset (the *main checklist* of that study: level C, optimum, HTR budget 2), in its order, over both ways of making the DR's last quarter turn. A route tried gives the shortest finish that follows it with an HTR at most 2 moves over the shortest NISS HTR, if that finish is at most 2 moves over the DR's optimal finish; otherwise nothing. The finish is found with a chance (0.9) when it exists. What a route finds is computed on the cube from the DR state, not drawn from statistics.

### 3.4 What the simulated solver can do that a human can't

These are simplifications, and each one makes the simulated solver a bit better than its costs would suggest.

- **Its read of an RZP state is centred on the truth.** A human's read of a DRM is biased in ways that depend on the case; here the error is symmetric noise around the exact distance.
- **A DR seen is written optimally**: from a state d moves from DR the solver writes a d-move DR, never a longer one.
- **A route tried gives the best finish along it** (within 2 moves of the DR's optimum), or nothing. A human trying a route might find a worse finish along it.
- **The solver knows each subset's finish distribution** (all 19.5 billion DR states, from htr-routes) when it weighs a DR.
- **No mistakes**: no miswritten moves, no wrong scramble, no solution that fails the check. A DNF comes only from the clock.

And what a human can do that the simulator doesn't (section 12): EOs of 6 or more, DRs not through a written EO, DR-breaking finishes, insertions, blockbuilding, using a written solution as a faster scramble.

### 3.5 Runs

Every plan plays the same scrambles with the same random draws (the same EO gets missed, the same step takes the same time, the same attempt is a slow one under every plan). So two plans get compared attempt by attempt, and the difference has a way smaller error than either mean. Scrambles are uniform random states. Policies are chosen on training scrambles, and every comparison on this page is on 4,000 held-out scrambles (4,000 to 7,999) that no policy was chosen on (appendix B). One simulated attempt takes about 10 ms of computer time.
