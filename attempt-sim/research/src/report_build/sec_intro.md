# How to spend the hour: a simulated FMC attempt

**This is a draft.** The time costs are my first guesses and the conclusions depend on them. Section 4 has every cost with where it comes from, and section 11 says which conclusions still hold when you halve or double each one.

How long should you write EOs? When do you stop looking for DRs? Is it worth finishing a good DR the moment you find it? When should you write a backup down? Everyone here has an answer, but nobody can do the same scramble twice to check. So I wrote a program that can. It plays an hour-long DR attempt on a real scramble the way the guides describe one (EO, RZP, DR, HTR, finish), charges a time cost for everything it looks at, misses stuff the way a person does, and writes down what it has when the hour runs out. Then it plays the same scrambles again with a different plan and compares, attempt by attempt. It's all sampled: {{V:n_train}} random scrambles to pick plans on, {{V:n_test}} others to check them on, plus the {{V:n_off_scr}} official scrambles of the top 5's recent attempts.

November 2026. A date in brackets links to that message on the FMC solvers Discord (#fmc-theory, #fmc-discussion or #non-dr-discussion). Docs and sheets are linked at the end.

**This builds on** stuff that was already on the server:

- **The splits people use.** Yura Riabov's [*Hitchhiker's Guide to FMC*](https://docs.google.com/document/d/16nu10y1JkUmVDC11c1h_ULzAl4Vze7zR/edit) (5-10 minutes writing EOs, up to 30-35 minutes checking them for DRs, the rest finishing), the thread where beef beans, kalindumaxxer, mrauo, Jay and rogo compared their search/finish splits ([[D9627]] and the replies), Lichi Fang's 7+28+25 ([[D10811]]) and Tom Nelson's 10/25/25 ([[T492]]).
- **How long each step takes.** What people have said: an EO written in 7 to 20 seconds, 3-5 seconds to throw away a 4-mover, 10-30 seconds per RZP, 20-30 seconds per switch, over a minute to write and check the final solution (all quoted in section 4).
- **Backup and safety habits.** Yura Riabov writing the best solution down around minute 50 in comp, and anything sub-24 or sub-23 right away ([[D10379]], [[D10380]]). Jay's and Yura's quick check of the easiest paths on a DR that feels 22/21able ([[D9634]], [[D14418]]). Zagros on the difference between a backup and committing early ([[D10395]]).
- **The idea of simulating it.**
  - Tom Nelson suggested simulating 100k solves with human-findable steps ([[D3238]]), and did the arithmetic by hand ([[T459]], [[T463]]).
  - rodneykinney posed "the cost-optimized FMC search strategy" with time as the cost ([[T6582]]).
  - Spencer asked for a heuristic for how many paths a human can check, "and then run simulations about how many we should check at each stage" ([[T2682]]).

  As far as I can find, nobody posted one for a DR attempt. DougCube mentions private simulations for blockbuilding ([[N2471]]), and Jack Love's *100 Example Solves* are computer solutions, not a model of the search.
- **Tables from the other studies on this site**, used as they are:
  - the exact optimal finish of every DR state (proved in Lean), from [*Judging a DR by hand*](../judging-a-dr/);
  - the HTR route checklist per subset, from [*Which HTR routes to try from a DR*](../htr-routes/);
  - the EO-kept distance to DR of every EO-solved case (proved in Lean), from [*EO to DR, and scramble to DR*](../eo-to-dr/) and [*When to switch an EO*](../eo-switch/);
  - the scramble features (bad edges per axis, shortest EO, number of 4-move EOs), from [*Easy or hard? Reading a scramble before you look for DRs*](../scramble-difficulty/).

**What this adds**: a simulator of the whole hour, and the first measured answers to the time-management questions, with the costs out in the open so people can argue with them.

- How the result depends on when you stop writing EOs and when you stop looking for DRs, on the same scrambles.
- Breadth first vs depth first, and the quick check of a good DR the moment it shows up.
- Whether a plan that reacts to the scramble (lots of EOs or few, a short DR early, a backup in hand) beats a fixed one, checked on scrambles it wasn't tuned on.
- The best plan for *22 or better*, and what it costs in mean.
- How the mean moves with the length of the attempt and with each budgeting decision, and which of these conclusions flip when a time cost is halved or doubled.

**Terms.** The usual ones: *EO*, *RZP*, *DR*, *HTR*, *switch* (NISS on an RZP), *subset* (corner case plus bad edges, `4b2 4e`), *route* (the subsets a finish goes through to HTR, in the HTR study's notation), *backup* or *safety* (a solution written on the sheet before the end). Plus a few of my own for this page:

- *Policy* or *plan*: the plan for the hour, a handful of numbers (when to stop writing EOs, how many RZP states per EO, when to stop looking for DRs, how many routes per DR, when to write a backup). The *baseline* is the guides' plan (section 3.2). The *tuned plan* is the baseline with three changes that turned out better (section 1).
- *Score*: the result with a DNF counted as 30 moves. A plan's score is the mean over all attempts, DNFs included. *Mean* on its own leaves DNFs out, like your own average does.
- *Score − tuned plan*: the difference attempt by attempt on the same scrambles, with its standard error. Negative is better.
- *≤ 22*: the share of attempts that end at 22 or better (a DNF doesn't count).
- *Robust* / *depends on the costs*: whether a conclusion keeps its sign when each time cost is halved and doubled (section 11).

**How to read it.**

- **Start with [section 1](#1-the-short-version)**: the answers, a paragraph or a table each. Section 4 is the table of costs, with the questions that would tune them.
- **Sections 6 to 10** take one question each, and **section 11** tests every conclusion against the costs. **Section 12** is what the simulator leaves out.
- Anything marked **computer only** is something the simulated solver can do and you can't, or an answer key.

---

| Section | What's in it |
|---|---|
| [1. The short version](#1-the-short-version) | The answers, with their numbers and how much they depend on the costs. |
| [2. What was asked](#2-what-was-asked) | The questions, and the ones people asked on the server before. |
| [3. The simulated attempt](#3-the-simulated-attempt) | The steps, what each one shows, the baseline plan, finishing, what the simulated solver can do that you can't. |
| [4. The time costs and the human limits](#4-the-time-costs-and-the-human-limits) | Every cost and limit with its source and how sure I am, and what to tell me to tune them. |
| [5. The baseline against real results](#5-the-baseline-against-real-results) | The simulated solver against the top 5's official attempts and Yura Riabov's log, whole distribution. |
| [6. How long on each step](#6-how-long-on-each-step) | Minutes on EOs, when to stop the DR search, how much to look at per EO and per DR. |
| [7. Breadth first or depth first](#7-breadth-first-or-depth-first) | Finishing a DR when you find it, taking short EOs straight to DR, early backups. |
| [8. Adapting to the scramble](#8-adapting-to-the-scramble) | Rules that react to what the attempt shows, checked on new scrambles. |
| [9. At most 22: the safety plan](#9-at-most-22-the-safety-plan) | Plans that push ≤ 22 up, and what they cost in mean. |
| [10. How the result scales](#10-how-the-result-scales) | The result against the length of the attempt, the speed of the solver, and one decision at a time. |
| [11. What depends on the costs](#11-what-depends-on-the-costs) | Each conclusion with every cost halved and doubled. |
| [12. What this does not model](#12-what-this-does-not-model) | Limits. |
| [Appendix A: full tables](#appendix-a-full-tables) | Every plan run. |
| [Appendix B: how it was computed, and what checks it](#appendix-b-how-it-was-computed-and-what-checks-it) | The program, the runs, the checks, the Lean certificate. |
| [Docs referred to](#docs-referred-to) | Links. |
