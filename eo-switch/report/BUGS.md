# When to switch an EO: corrections

*Goes with the write-up on when to switch an EO, but reads on its own. The write-up has the measurements and the tables.*

November 2026. A date in brackets is a link to that message on the FMC solvers Discord (#fmc-theory, #fmc-discussion or #non-dr-discussion).

**What everything below is measured against:**

- **The exact EO-kept distance to DR of every EO-solved case** (1,082,565 for one EO axis and one DR axis: corner twists × the places of the E-slice edges), from a breadth-first search with U, D, R, L, F2, B2. It agrees with Cale's table, my EO-to-DR study and nissy, and a Lean certificate proves its histogram.
- **The features** (ARM, pairs, side pairs, corner case) defined from stickers. They agree with rodneykinney's own code on every case.

Each example below is a scramble: apply it to a solved cube held with the EO on F/B, and you have the case. The DR given is optimal (EO kept), and every one was replayed on a sticker-level cube. Each item also says how much of its example is checked in Lean; the rest is computed, not proved. ✓ after a number: proved in Lean. Below are only the statements the numbers go against. Most of what was said holds up, and that's in the write-up's section 11.

---

**a. "10 total sets that can be sub 6 out of the 15 total sets (7/15 can be sub 5!)"** (Jay, [9 Mar 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1215904716530384908), on which 4c4e ARM sets can be a DR in 5 or less after a switch).
There are 11 ✓. Jay's list (00; 21; 42; 10, 11, 31, 32; 01, 20, 22) leaves out AR-4c1e (ARM 41), whose shortest case is 5 ✓ moves. The sub-5 count, 7, is right. Shortest DR per ARM set: 00:1, 01:5, 02:6, 10:4, 11:4, 12:6, 20:5, 21:2, 22:5, 30:6, 31:4, 32:4, 40:6, 41:5, 42:3.
Example, a 4c4e with ARM 41:

```
L' U' B2 F2 U'  // scramble: 4c4e, ARM 41, 4a-4 corners, 2 pairs
U F2 B2 U L      // DR (5 moves)
```

With NISS the same case is one move from DR: the inverse of the setup followed by L is a DR state (nissy and the sticker model).

```
U F2 B2 U L  // the inverse of the setup
L            // DR: the NISS DR is (L)
```

That is a quirk of a short setup, not a fault in the count: the counts here, like the write-up's, are of the EO-kept DR on the side you are solving, without NISS, and for that this case needs 5. *Lean-checked*: the case (4c4e, ARM 41, 2 pairs), its distance of 5 and the printed DR (`eo_switch_examples`), and the shortest case of every ARM set, so 11 sets sub-6 and 7 sub-5 (`arm_sets`); both are in the Lean library of my study [*Which HTR routes to try from a DR*](../htr-routes/), file lean/FakeBound/Corrections/Examples.lean in its folder. The NISS DR is Lean-checked too, and so are the corners (4a-4) (`example_labels` in the study's own Lean folder, lean/EOSwitch).

**b. "Because it’s a three move trigger, no number of pairs will save 3qt corners"** (rodneykinney, [15 Jun 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1383677247545933874), on 4c2e).
For 4c2e with 3qt corners (4b-0), the sub-7 share is 8.3% ✓ with no pair, 60.4% ✓ with one and 79.2% ✓ with two. The trigger costs three moves, but the pairs make up for it. rodneykinney's own 4c2e table at the time ([14 Jun 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1383638325281292389)) also switches 4b corners with pairs, so this is a slip in the explanation more than in the rule.
Example, a 4c2e with 4b-0 corners:

```
R' D2 R F2 D' U'  // scramble: 4c2e, 4b-0 corners, 2 pairs
U D F2 R' D2 R    // DR (6 moves)
```

*Lean-checked*: the case (4c2e, 2 pairs), its distance of 6 and the printed DR (`eo_switch_examples`). Its corner case (4b-0) and the three sub-7 shares are Lean-proved too (`example_labels`, `errata_b_3qt` in lean/EOSwitch).

**c. "a corners - ~34% if corners are stacked, < 5% otherwise"** (Evan, [18 Sep 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1418283868007436308), for 4c4e with 1 pair and ARM 21; the same message has "b corners - 29%" and "d corners - 89%").
b and d are right (28.7% ✓ and 88.9% ✓). Reading "stacked" as all four bad corners on one side face, stacked a corners are 35.7% ✓, as Evan says. The other a cases are 16.2% ✓ (1,680 ✓ cases), not under 5%. Read "otherwise" as about 1 in 6.2, not as a discard.
Example, a 4c4e with ARM 21, 1 pair and 4a corners that are not stacked:

```
L' B2 D' L2 D' U2  // scramble: 4c4e, ARM 21, 1 pair, 4a corners, not stacked
U2 D L2 D B2 L      // DR (6 moves)
```

*Lean-checked*: the case (4c4e, ARM 21, 1 pair), its distance of 6 and the printed DR (`eo_switch_examples`). That its corners are 4a and not stacked, and the shares and the 1,680, are Lean-proved too (`example_labels`, `errata_c_stacked` in lean/EOSwitch).
