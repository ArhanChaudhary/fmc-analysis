# When to switch an EO: corrections

*Goes with the write-up on when to switch an EO, but reads on its own. The write-up has the measurements and the tables.*

November 2026. A date in brackets is a link to that message on the FMC solvers Discord (#fmc-theory, #fmc-discussion or #non-dr-discussion).

**What everything below is measured against:**

- **The exact EO-kept distance to DR of every EO-solved case** (1,082,565 for one EO axis and one DR axis: corner twists × the places of the E-slice edges), from a breadth-first search with U, D, R, L, F2, B2. It agrees with Cale's table, my EO-to-DR study and nissy, and a Lean certificate proves its histogram.
- **The features** (ARM, pairs, side pairs, corner case) defined from stickers. They agree with rodneykinney's own code on every case.

The example below is a scramble: apply it to a solved cube held with the EO on F/B, and you have the case. The DR given is optimal (EO kept) and was replayed on a sticker-level cube. The item also says how much of its example is checked in Lean; the rest is computed, not proved. ✓ after a number: proved in Lean. Below is the one statement the numbers go against. Most of what was said holds up, and that's in the write-up's section 13.

---

**a. "I believe I now know which DR-4C4E sets actually have a chance of being 5 or less moves after you NISS" … "10 total sets that can be sub 6 out of the 15 total sets (7/15 can be sub 5!)"** (Jay, [9 Mar 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1215904716530384908), a count by hand from pruned sheets, before any DRM × ARM table existed).
There are 11 ✓. Jay's list (00; 21; 42; 10, 11, 31, 32; 01, 20, 22) leaves out AR-4c1e (ARM 41), whose shortest case is 5 ✓ moves: 24 of its 3,456 cases. The sub-5 count, 7, is right. Shortest DR per ARM set: 00:1, 01:5, 02:6, 10:4, 11:4, 12:6, 20:5, 21:2, 22:5, 30:6, 31:4, 32:4, 40:6, 41:5, 42:3. Louis's [*DRM/ARM average optimals*](https://docs.google.com/spreadsheets/d/13fSwUROzP0hZQV1Cn96GndWbPy4UrsHiYTaWFSeWtJs) ([27 Mar 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1222749709039435839)), 18 days later, has the 41 five-mover: its best 4c4e AR-4c1e solution is `D' B2 F2 D R'`.
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
