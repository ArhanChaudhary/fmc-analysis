# When to switch an EO: corrections

*Goes with the write-up on when to switch an EO, but reads on its own. The write-up has the measurements and the tables.*

November 2026. A date in brackets is a link to that message on the FMC solvers Discord (#fmc-theory, #fmc-discussion or #non-dr-discussion).

**What everything below is measured against:**

- **The exact EO-kept distance to DR of every EO-solved case** ({= n(1082565) =} for one EO axis and one DR axis: corner twists × the places of the E-slice edges), from a breadth-first search with U, D, R, L, F2, B2. It agrees with Cale's table, my EO-to-DR study and nissy, and a Lean certificate proves its histogram.
- **The features** (ARM, pairs, side pairs, corner case) defined from stickers. They agree with rodneykinney's own code on every case.

Each example below is a scramble: apply it to a solved cube held with the EO on F/B, and you have the case. The DR given is optimal (EO kept), and every one was replayed on a sticker-level cube. Each item also says how much of its example is checked in Lean; the rest is computed, not proved. ✓ after a number: proved in Lean. Below are only the statements the numbers go against. Most of what was said holds up, and that's in the write-up's section 11.

---

**a. "10 total sets that can be sub 6 out of the 15 total sets (7/15 can be sub 5!)"** (Jay, [[T4256]], on which 4c4e ARM sets can be a DR in 5 or less after a switch).
There are 11 ✓. Jay's list (00; 21; 42; 10, 11, 31, 32; 01, 20, 22) leaves out AR-4c1e (ARM 41), whose shortest case is {= EV('T4256-sets', '41:', ',') =} ✓ moves. The sub-5 count, 7, is right. Shortest DR per ARM set: {= CL('T4256-sets').split('shortest per set ')[1] =}.
Example, a 4c4e with ARM 41:

```
{= WC('T4256-sets', 'setup') =}  // scramble: 4c4e, ARM 41, {= WC('T4256-sets', 'state').split('case ')[1] =} corners, {= WC('T4256-sets', 'state').split('pairs ')[1].split()[0] =} pairs
{= WC('T4256-sets', 'dr') =}      // DR ({= WC('T4256-sets', 'length') =} moves)
```

With NISS the same case is one move from DR: the inverse of the setup followed by L is a DR state (nissy and the sticker model).

```
U F2 B2 U L  // the inverse of the setup
L            // DR: the NISS DR is (L)
```

That is a quirk of a short setup, not a fault in the count: the counts here, like the write-up's, are of the EO-kept DR on the side you are solving, without NISS, and for that this case needs 5. *Lean-checked*: the case (4c4e, ARM 41, 2 pairs), its distance of 5 and the printed DR (`eo_switch_examples`), and the shortest case of every ARM set, so 11 sets sub-6 and 7 sub-5 (`arm_sets`); both are in the Lean library of my study [*Which HTR routes to try from a DR*](../htr-routes/), file lean/FakeBound/Corrections/Examples.lean in its folder. The NISS DR is Lean-checked too, and so are the corners (4a-4) (`example_labels` in the study's own Lean folder, lean/EOSwitch).

**b. "Because it’s a three move trigger, no number of pairs will save 3qt corners"** (rodneykinney, [[T8147]], on 4c2e).
For 4c2e with 3qt corners (4b-0), the sub-7 share is {= pc(EV('T8147-3qt', '4b-0 0p ', ',')) =} ✓ with no pair, {= pc(EV('T8147-3qt', '4b-0 1p ', ',')) =} ✓ with one and {= pc(EV('T8147-3qt', '4b-0 2p ')) =} ✓ with two. The trigger costs three moves, but the pairs make up for it. rodneykinney's own 4c2e table at the time ([[T8140]]) also switches 4b corners with pairs, so this is a slip in the explanation more than in the rule.
Example, a 4c2e with 4b-0 corners:

```
{= WC('T8147-3qt', 'setup') =}  // scramble: 4c2e, 4b-0 corners, {= WC('T8147-3qt', 'state').split('pairs ')[1].split()[0] =} pairs
{= WC('T8147-3qt', 'dr') =}    // DR ({= WC('T8147-3qt', 'length') =} moves)
```

*Lean-checked*: the case (4c2e, 2 pairs), its distance of 6 and the printed DR (`eo_switch_examples`). Its corner case (4b-0) and the three sub-7 shares are Lean-proved too (`example_labels`, `errata_b_3qt` in lean/EOSwitch).

**c. "a corners - ~34% if corners are stacked, < 5% otherwise"** (Evan, [[D14402]], for 4c4e with 1 pair and ARM 21; the same message has "b corners - 29%" and "d corners - 89%").
b and d are right ({= pc(EV('D14402-21-1p', 'b ', ',')) =} ✓ and {= pc(EV('D14402-21-1p', 'd ', ';')) =} ✓). Reading "stacked" as all four bad corners on one side face, stacked a corners are {= pc(EV('D14402-21-1p', 'a stacked ')) =} ✓, as Evan says. The other a cases are {= pc(EV('D14402-21-1p', 'a not stacked ')) =} ✓ ({= EV('D14402-21-1p', 'a not stacked ', ')').split('(')[1] =} ✓ cases), not under 5%. Read "otherwise" as about {= oneIn(EV('D14402-21-1p', 'a not stacked ', ' ')) =}, not as a discard.
Example, a 4c4e with ARM 21, 1 pair and 4a corners that are not stacked:

```
{= WC('D14402-21-1p', 'setup') =}  // scramble: 4c4e, ARM 21, 1 pair, 4a corners, not stacked
{= WC('D14402-21-1p', 'dr') =}      // DR ({= WC('D14402-21-1p', 'length') =} moves)
```

*Lean-checked*: the case (4c4e, ARM 21, 1 pair), its distance of 6 and the printed DR (`eo_switch_examples`). That its corners are 4a and not stacked, and the shares and the 1,680, are Lean-proved too (`example_labels`, `errata_c_stacked` in lean/EOSwitch).
