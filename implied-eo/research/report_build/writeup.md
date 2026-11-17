# Implied EOs

Sometimes one EO on a scramble guarantees another one. The known case is F B (F B): if it's an EO, so are R L (R L) and U D (U D). This page lists every case where an EO of 5 moves or less (normal + inverse) implies another EO of 5 moves or less, says which theorems give them, and checks whether anything other than the F B R L trick is behind them. Everything is exact and proved in Lean, except the *how often* numbers, which are sampled.

November 2026. A date in brackets is a link to that message on the FMC solvers Discord (#fmc-theory or #fmc-discussion).

**This builds on** what the server worked out in October 2023 and after:

- **The observation and the first proof.** Cale noticed that F B (F B) came on all three axes, Jay posted it with five test scrambles ([[T3441]]), and Cale gave the proof the next hour ([[T3443]]): U D F B on both sides turns a state that keeps F/B EO into one that keeps U/D EO.
- **torchlight's orientation** ([[T3445]], [[T3446]], [[T3455]]): "there's another type of EO that's axis-independent: think of the shape of the edges on a mastermorphix", "(every quarter turn, no matter which axis, changes EO of the four moved edges)". fabio's version of it ([[T3452]]): "So I believe this kind of eo happens precisely when all edges are good on one axis or 3, but not 2."
- **Adding and cancelling.** wen's way of deriving new ones by adding U D (U D) and F B (F B) and cancelling ([[T3461]]). mrauo: "It looks like balancing chemical equations" ([[T3466]]).
- **The derived EOs**, found one at a time by Jay ([[T3441]], [[T3450]], [[T3458]], [[T3459]], [[T3463]]), trig0n ([[T3662]]), Cale ([[T3639]]), Zagros ([[D17329]]) and others. Section 8 has all of them.
- **F B R L on both sides** as the general form: Yura Riabov ([[D11880]]) and FakeMMAP ([[D20114]]).
- **Shota's count rule** for what a side becomes on another axis ([[T5343]]): "when F B () has x/y/z bads on M/E/S slice (perspective on F/B axis EO), U D () has x/4-z/4-y bads on M/S/E slice (perspective on U/D axis EO)".
- **The request this answers**, trig0n's ([[T3663]]): "Could anyone prepare a full list of these with the probability of appearing on random scrambles?" Nobody posted one.

**What it adds:**

- **The full list**: {= n(len(SETS)) =} sets of scrambles have two or more EOs of 5 moves or less. They come in seven kinds, and one small dictionary between axes produces all of them (section 4).
- **An exact test** for when one EO implies another, for any length: both must have the same two EO cases after a fixed change between axes. An implication always goes both ways (section 3).
- **Nothing but the trick up to 5 moves**, proved by exhaustion. There is a second source, a superflip on both sides, and it starts at 6-move EOs (section 6).
- **The order of the four moves matters**: for an F/B EO it's F B R L, for an R/L EO it's R L F B (section 3).
- **Sub-6 EOs implied by a longer EO you can see**: after F B and one trace you know every EO that starts with R L or U D on that side too. That's how F B (F U2 B) shows up from U D (section 5).
- **How often**: {= pc('any') =} of scrambles have such a pair (section 7).

**Terms.** An *EO* here is N (I): moves N on normal, moves I on inverse, and its length is the two together. Its axis is the axis of the last move on each side, so (L) B R L is an R/L EO. An *EO case* is a set of bad edges, and F and F' as the last move, or two solutions of one case, count as the same EO (Joba asked "Are F and F' separate EOs?", [[T9201]]; Radek B: "1-3 no", [[T9204]]). A *side* of an EO is its normal moves or its inverse moves. The *E slice* is FR, FL, BR, BL, the *M slice* UF, UB, DF, DB, the *S slice* UR, UL, DR, DL. *The trick* is adding four quarter turns, such as F B R L, to both sides.

**How to read this.** Using the list is a lookup, at a glance: you have found an EO, you look whether it's one of the seven kinds, and you write the other one down without tracing anything. Section 1 is all you need for that. Sections 3 and 6 are the theory, section 5 is what you can see on the cube without writing anything. Counts are exact. The percentages of sections 5 and 7 are from {= n(NS) =} uniformly random scrambles and carry their error bars.

{{CONTENTS}}

## 1. The short version

**Every implied EO of 5 moves or less is one of these seven kinds**, up to turning or mirroring the cube and swapping normal with inverse. Each row is one set of scrambles: every EO in the row is there exactly when the others are.

{{ t_kinds() }}

In kind 7, X is any move of U, D, F or B. Kinds 2 and 3 pair a 3-mover with 5-movers, so they also say when those 5-movers can exist at all.

- **They all come from one dictionary.** Take the two sides of an F/B EO and translate each one to R/L with the table of section 4 (F ↔ B R L, F B ↔ R L, R F B ↔ L, X R F B ↔ X L, F U B ↔ R U' L, R L F B ↔ nothing, nothing ↔ F B R L). If both sides are in the table, the translated EO is on the scramble too. That's the whole list.
- **The dictionary is the F B R L trick.** N (I) is an EO on F/B exactly when N F B R L (I F B R L) is an EO on R/L. The dictionary is what each side cancels down to. The order matters: the axis you're leaving goes first (section 3).
- **Nothing else up to 5 moves.** I checked all {= n(NPRES) =} EOs of 5 moves or less against each other. There is a second way for one EO to imply another, a superflip on both sides, but its shortest instance is a 6-mover implying a 6-mover: U D' F (U D' F) and R2 B2 R (R2 B2 R) (section 6).
- **A sub-6 EO can also be implied by a longer one that you'd never write but can see.** F B (F U2 B) isn't in the table: its partners are 6-movers. One of them is U D (D U2 F U), and you notice it as a shape: do U D, trace, and the other side has 8 bad with three of the four good edges in the E slice. In general one trace after F B gives you every EO that starts with R L or U D on that side as well (section 5). That reaches {= n(LF['sets_new']) =} five-movers the table doesn't have, and {= f"{100 * LF['p']:.1f}%" =} of scrambles have one of them.
- **An implication always goes both ways**, and each EO, as a pair of cases, is on exactly 1 scramble in 2,048.
- **How often.** {= pc('any') =} of scrambles have at least one such pair. Almost all of that is kind 7 ({= pc('P5') =}). A pair where both EOs are 4 moves or less is on {= pc('le4') =} of scrambles (section 7). Jay's guess was "anecdotally i feel like these new eo derivatives are present on more than 1/4 scrambles" ([[T3470]]), and that's right.
- **Everything said on the server checks out**: {= sum(1 for c in C if c['stated'] == 'same') =} stated implications and {= sum(1 for c in C if c['stated'] != 'same') =} stated coincidences (section 8). So there is no errata page.

[The full list](examples.html) has all {= n(len(SETS)) =} sets written out, each with a scramble to try it on.

## 2. What was asked

1. List every case where one EO of 5 moves or less implies another. *Answer*: sections 1 and 4, and the full list.
2. Which theorems give them? *Answer*: the four of section 3.
3. Are there implied EOs that don't come from the F B R L trick? *Answer*: not up to 5 moves. From 6 moves on, yes (section 6).
4. Is a sub-6 EO ever implied by a longer EO that you wouldn't write down but can notice on the cube, say after F B and a trace? *Answer*: yes, a lot of them (section 5).

## 3. The theorems

All four are proved in Lean for every scramble (appendix). Edges only: EO doesn't see corners.

**Theorem 1 (the two cases).** Take an EO N (I) on some axis. Call the EO case that N solves its *normal case* and the EO case that I solves its *inverse case*. Then N (I) is an EO on a scramble exactly when, on that axis, each edge is bad if and only if one of these is true and not both:

- the place it's in belongs to the normal case;
- its home place belongs to the inverse case.

*Example.* F (B) with green on F: the normal case is the four places of the F layer, the inverse case the four blue edges. So F (B) is an EO exactly when every edge in the F layer is bad unless it's blue, and every edge outside it is good unless it's blue. `{= fb_scr =}` is such a scramble.

*Why.* The inverse moves act as premoves, so they decide badness by which edge it is, and the normal moves decide it by where the edge is. This is by tracing: it's what a NISS EO looks like from normal.

**Theorem 2 (one edge on two axes).** Going from F/B to R/L, an edge changes between good and bad exactly when one of its place and its home place, not both, is in the E slice. For F/B and U/D it's the M slice, for R/L and U/D the S slice. Tzak's rule says the same thing by slices ([[T10074]]).

**Theorem 3 (when one EO implies another).** Put theorems 1 and 2 together. Two EOs are there on exactly the same scrambles if and only if:

- *same axis*: they have the same normal case and the same inverse case (it's the same EO solved differently), or both cases are complemented, all 12 edges toggled;
- *F/B and R/L*: both cases differ by the 4 edges of the E slice, or both differ by the other 8 edges. For other pairs of axes it's the slice across the third axis.

If neither holds, there is a scramble with the first EO and without the second. So *X implies Y* and *Y implies X* are the same statement. In counts this is Shota's rule quoted above: x/y/z bad on M/E/S becomes x/4-z/4-y.

**Theorem 4 (the trick).** For any scramble and any N and I:

N (I) is an EO on F/B ⟺ N F B R L (I F B R L) is an EO on R/L.

The same with F B U D for F/B to U/D, R L F B for R/L to F/B, and so on: the two quarter turns of the axis you're leaving come first, then two of the axis you're going to. Each of the four can be turned either way. In terms of theorem 3 this is the *other 8 edges* option. FakeMMAP said it as "Also if you have an FB EO you can do  FBRL(FBRL) and you get another EO." ([[D20114]]).

*The order matters.* Take the scramble `F U F'`. It has EO on R/L. After F B R L (F B R L) there is no EO on any axis. After R L F B (R L F B) there is EO on F/B.

*Why it works.* It's torchlight's orientation. Call an edge *qt-good* if it's an even number of quarter turns from home. Every quarter turn of any face flips that for the four edges it moves. For one edge, qt-good and good on F/B differ exactly when one of its place and its home place, not both, is in the S slice. F B on both sides flips an edge once for sitting off the S slice and once for belonging off it, which is that same difference. So F B on both sides turns *EO on F/B* into *every edge qt-good*, and R L on both sides turns that into *EO on R/L*. F B (F B) is the case with nothing in front, which is torchlight's "you have F B (F B) EO iff every edge piece is an even number of quarter turns away from solved" ([[T3455]]).

## 4. The list

**The dictionary.** One side of an F/B EO, and what that side is on R/L. Every side of up to 4 moves whose translation also has up to 4 moves is here:

{{ t_dict() }}

For another pair of axes turn the cube: F/B to U/D is the same table with R, L read as D, U and U, D read as R, L (F U B ↔ R U' L becomes F R B ↔ D R' U).

**How to use it.** You have an F/B EO. Translate its normal side and its inverse side. If both are in the table, the result is an R/L EO on the same scramble, and the table read right to left takes you back. Example: F B (F U B) has sides F B and F U B, which translate to R L and R U' L, so R L (R U' L) is an EO.

**Where a row comes from.** Add F B R L to the side and find the shortest sequence for the same EO case. F becomes F F B R L, and F2 B R L solves the same case as B R L. R F B becomes R F2 B2 R L, the same case as L. That's wen's cancelling ([[T3461]]). The rows above are the only ones that come out short.

**The seven kinds** are the ways to pick two rows so that both EOs have 5 moves or less:

{{ t_kind_rows() }}

Kinds 1 and 2 also have a U/D EO, because F B translates to U D as well. No other set has three.

**A scramble for each kind**, to try them on. These are ordinary random-move scrambles, picked because they have the EO:

{{ t_kind_scrambles() }}

**On scrambles people posted**, with the EOs they found:

{{ t_real() }}

**Counts.** There are {= n(NPRES) =} EOs of 5 moves or less, counted as an axis with two cases. They sit on {= n(NCLASS) =} different sets of scrambles. {= n(len(SETS)) =} of those sets have more than one EO: {= n(len(SETS) - THREE) =} have two and {= THREE =} have three. [The full list](examples.html) has every one.

## 5. Sub-6 EOs implied by a longer EO

Section 4 needs both EOs to have 5 moves or less. But by theorem 4 a sub-6 EO has a partner on each other axis whatever its length, and that partner is usually a 6- or 7-mover. You'd never write one of those down. You can still notice it, because you don't have to solve it: you apply its short side, trace, and recognise the case on the other side.

**The case to know.** F B (F U2 B) has no partner of 5 moves or less. Its U/D partner is U D (D U2 F U), a 6-mover. So: do U D and trace the other side on U/D. If it shows 8 bad edges with UB, FR, BR and BL good (three of the four good ones in the E slice and one outside it), then F B (F U2 B) is an EO. `{= pt_scr =}` has both. This is how Jay found F B (F R2 B) ([[T3636]]): "found it by seeing 2 opp qt to 8 bad on a different axis gave 8 bad with 3/4 good edges in the (relative) S slice but not 3 optimal". wen gave the same shortcut for F B (F U2 B) ([[D15005]]), and FakeMMAP the proof and the axis ([[D15042]], [[D15044]]).

**Theorem 5 (one trace, three axes).** For any moves I:

F B (I) on F/B ⟺ R L (I F B R L) on R/L ⟺ U D (I F B U D) on U/D,

and the same with normal and inverse swapped. On the cube this is *the flip rule*. Do F B and look at the bad edges of the other side, on F/B. Flip the eight places of the U and D layers, bad to good and good to bad, and keep the E slice: that's the case c for which R L (c) is an EO. Flip the eight places of the R and L layers instead, keeping the M slice, and it's the c for U D (c). This is by tracing, and it's one trace where checking F B, R L and U D one after the other takes three.

**What it reaches below 6 moves.** R L (c) has 5 moves or less when c takes 3 or less. There are 230 such c on R/L, so 230 things to see after F B:

{{ t_probe() }}

So after F B there are 215 patterns that give a sub-6 EO on R/L while the F/B EO they belong to has 6 or 7 moves, and as many for U/D. [The full list](examples.html) has all 230 with their edges.

**The shape people use.** 8 bad after the two quarter turns, three good edges in the slice across the axis and one somewhere else: that's 32 patterns. 16 of them are 3-movers themselves, F U B and the like (kind 6). For the other 16, the two quarter turns of exactly one other axis leave a 3-mover of the F U2 B type, and it's the axis of the other face of the lone good edge. In the example the lone good edge is UB and the EO is on F/B. So Jay's and wen's shortcut and FakeMMAP's rule for the axis are right.

**Other short sides.** Counts are for one choice of the two axes and of the side you apply the moves on, like the 215.

- *A setup move and a quarter turn.* After X F, if the other side shows the R L F B case, then X B R L is an EO on the side you're on: U F (R L F B) with U B R L, 24 of them. Those are linear, so you see them anyway. This is Jay's F R on the F L F B case ([[D13106]]).
- *Three moves applied*, like R F B, one move to 8 bad. Translate what you applied with the dictionary, flip the rest. That's {= n(BP['trick']['3'] // 2) =} more, too many to list. Zagros: "There are some 2+3s that you can only find with this method if you trace 1 move to 10 bad" ([[D17322]]).
- *Through the superflip* (section 6), with at most two moves applied: {= n((BP['trick+superflip']['1'] + BP['trick+superflip']['2']) // 2) =} between two axes and {= n(BP['superflip']['2'] // 2) =} on one axis. Example: after U' B, if the other side shows exactly UR, DR, FL and BL bad on F/B, then L2 B D' R (R) is an EO on R/L. `{= exs_scr =}` has both.

**How often.** There are {= n(LF['sets_all']) =} five-movers made of two opposite quarter turns on one side and a 3-mover on the other. {= n(LF['sets_all'] - LF['sets_new']) =} of them are in section 4. For the other {= n(LF['sets_new']) =} the partners on the other two axes have 6 or 7 moves, and {= f"{100 * LF['p']:.1f}% ± {100 * LF['ci']:.1f}" =} of scrambles have at least one of them ({= n(LF['n']) =} uniformly random scrambles).

## 6. Implied EOs that are not the trick

Theorem 3 leaves one more option between two axes: both cases differ by the 4 slice edges, where the trick gives the other 8. That's the trick plus a superflip on both sides. On one axis it's the superflip alone.

- **Up to 5 moves it never happens**, on any pair of axes or on one axis. This is the exhaustive check, done in Lean.
- **At 6 moves it starts.** U D' F (U D' F) on F/B and R2 B2 R (R2 B2 R) on R/L are EOs on the same scrambles: `{= six_scr =}` has both. There are {= n(BY['counts']['slice']['6']) =} such pairs of 6 moves or less for each two axes, next to {= n(BY['counts']['trick']['6']) =} from the trick.
- **On one axis it starts at 7.** R L F (L U R F) and B U D F (B D F) are both F/B EOs on the same scrambles: `{= seven_scr =}` has both.

So an implied EO that isn't the trick exists, and no 5-move EO has one.

## 7. How often

Each EO is on exactly 1 scramble in 2,048, so a scramble has {= f"{len(SETS) / 2048:.3f}" =} of the {= n(len(SETS)) =} sets on average. They overlap, so the share of scrambles with at least one is a bit lower. Sampled on {= n(NS) =} uniformly random scrambles, with 95% error bars:

{{ t_freq() }}

Kind 1 is exact: 1 in 2,048, as torchlight and FakeMMAP said ("1/2048", [[D3529]]; "Should be 1/2048.", [[D15059]]).

## 8. The claims, checked

Every pair of EOs I found stated on the server as going together, in the poster's notation. *Same scrambles* means the two cases agree (theorem 3) and the EOs were also tried on 300 scrambles each. The 6-movers and 7-movers people posted are in too.

{{ t_claims() }}

Statements that aren't a pair of sequences:

| Said | By | Check |
|---|---|---|
| "Again, F B (F B) is an EO iff R L (R L) is an EO iff U D (U D) is an EO." | FakeMMAP, [[D15050]] | Right (kind 1). |
| "These unique 5 move NISS EO's are only possible on scrambles that have such a 3 move EO" | Jay, [[T3441]] | Right: U D (B U D) and R L (B R L) are on a scramble exactly when F B (F) is (kind 2). |
| "you can add R L F B on both sides of the scramble and that preserves eo(and i'm pretty sure dr too)" | Yura Riabov, [[D11880]] | Right for EO when the EO is on R/L, which it was there (B F R L). For an F/B EO the order is F B R L (theorem 4). The DR part isn't checked here. |
| "F R2 B is 3/3/0, so if there's F B (F R2 B), U D (U R2 D) or R L (R F2 L) do not exist simultaneously." | Shota, [[T5344]] | Right that neither is implied (the two rows above with F R2 B). |
| "nah that's just coincidence", about B (F U2 B) with (D) D R2 U | Jay, [[T6837]] | Right. |
| "any time you see that case, it means the EO i described has to exist somewhere on one of the remaining two axes on that side of the scramble" | Jay, [[T3636]] | Right, for all 16 patterns of that shape that aren't 3-movers, and on exactly one of the two axes (section 5). |
| "If you spot F B -> 8 bad and it's 3 on S and one not on S, but it is NOT the 3 move 8 bad, then you know you have that funny 5 mover on a different axis" | wen, [[D15005]] | Right, the same 16 patterns. The axis is the one of the lone good edge's other face, as FakeMMAP said ([[D15044]]). |

## 9. What this does not cover

- **What comes after the EO.** trig0n's point that the RZP carries over ([[T3653]]), Cale's DR version ([[T3639]]) and wen's condition for it ([[D11884]]) are about corners too. This page is edges only.
- **A list for 6 moves and more.** Sections 5 and 6 have the counts. Theorem 3 decides any given pair.
- **Which of the two EOs is better.** They're different EOs on different axes, so each has its own DRs.
- **Things that often come together without being implied**, like Shota's 48% for F B (F R B) with (F B) F R B ([[T5345]]).

## Appendix: how it was computed, and what is proved in Lean

**The model.** 24 edge stickers and the six face turns as rotations of the layers. EO on F/B: an edge's key sticker is the U/D one if it has one, else the F/B one, and the edge is good when that sticker is on the U or D face, or on F or B in the E slice. The other axes are the same rule turned. A quarter turn of F or B flips exactly the four edges it moves and the other moves flip nothing, which is the usual definition.

**The enumeration.** Every EO case of 5 moves or less on each axis (1, 2, 25, 202, 620 and 900 cases of 0 to 5 moves), every pair of them with 5 moves or less in total, grouped by the test of theorem 3.

**Checks, by turning stickers.** Theorems 1 and 2 on 20,000 random scrambles. Every EO of every one of the {= n(len(SETS)) =} sets on a scramble built to have the set's first EO, and again on the random scramble of the full list. Every row of the dictionary. Every stated claim on 300 scrambles.

**Lean** (project *ImpliedEO*, no library, builds in under a minute). Everything is stated for all scrambles, as move sequences.

| Theorem | What it says |
|---|---|
| `EO.holds_iff` | Theorem 1. |
| `change_axis` | Theorem 2. |
| `EO.implies_iff_same`, `EO.equiv_iff_same` | Theorem 3, both directions: the two-case test is exactly *implies*, and exactly *same scrambles*. |
| `trick`, `trick_fb_rl` and the five others, `trick_either_way` | Theorem 4 for every pair of axes, each move turned either way. |
| `order_matters`, `wrong_order` | The F U F' example. |
| `fbfb`, `fb_fub` | F B (F B) with R L (R L) and U D (U D); F B (F U B) with R L (R U' L). |
| `fbfb_iff_quarter_turn_orientation`, `good_on_one_or_three` | torchlight's and fabio's statements. |
| `same_cases_of_implies`, `only_the_trick`, `same_axis` | Up to 5 moves an implied EO on another axis solves the same two cases as the trick's N F B R L (I F B R L), and on the same axis it's the same EO. |
| `census` | 239 pairs of cases for each two axes and 13 on all three: 3 × 239 − 2 × 13 = {= n(len(SETS)) =}. |
| `allSets_equiv` | Each of the {= n(len(SETS)) =} sets of the full list, as printed. |
| `probe`, `probe_fb`, `probe_rl`, `probe_ud` | Theorem 5: one side translated, the other side whatever it is. |
| `flip_rule` | The flip rule of section 5. |
| `ud_du2fu`, `probe_census`, `probeSets_ok` | U D (D U2 F U) with F B (F U2 B); the 230 cases after F B by length; each of the 230 rows of the full list. |
| `superflip_six`, `superflip_seven` | The two examples of section 6, and that their cases are complemented. |

The general theorems are checked by Lean's kernel. The exhaustive ones (`no_clash`, `cases_by_length`, `census`, `probe_census`, `allSets_ok`, `probeSets_ok`) are compiled computations. Not in Lean: the percentages of sections 5 and 7, the grouping into seven kinds, and the counts of section 5 other than the 230.
