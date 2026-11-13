## 5. Every DRM: count the side turns

The same idea works for every DRM. Let U and D turn freely and count the turns of the side faces a DR needs: R and L quarter turns, and the half turns R2, L2, F2, B2. I call that number the case's *side turns*. A DR is never shorter than its side turns and never longer than three times them, and that already gives a certain class.

rodneykinney's *DRM Subsets* already sorts solutions by the trigger they end in (`R`, `R U R`, `R U2 R`, `R U L`, `R U2 L`, `R L`), from one stored optimal solution per case. Side turns count what comes before the trigger as well, and over every DR of the case.

### 5.1 Side turns

Over all {= n(1082565) =} cases, one row per number of side turns:

{{ring_sigma_all}}

**2 side turns or fewer is a certain sub-7.** With s side turns you need at most two U/D turns before each of them and none after the last, so at most 3s moves. All {= n(RJ['sig_all']['0']['n'] + RJ['sig_all']['1']['n'] + RJ['sig_all']['2']['n']) =} ✓ cases with 2 or fewer have a DR in 6 or less (`side_turns_certain`). At the other end, 5 side turns leaves room for one U/D turn at most, and {= pcx(RJ['sig_all']['5']['p6']) =} ✓ of those cases are sub-7.

By DRM, one row per number of side turns:

{{ring_sigma}}

So 3 side turns is where the sub-7s are: it holds between {= pcx(min(RSIG(d, 3, 'of_hits') for d in RJ['sig'])) =} and {= pcx(max(RSIG(d, 3, 'of_hits') for d in RJ['sig'])) =} of each DRM's sub-7 cases. And a 3 comes in two kinds.

### 5.2 Quarter turns and half turns

4c4e can be finished with one quarter turn and never with none. Every other named DRM needs two at least (some 8c8e cases need three). A 3 with an extra quarter turn is much worse than a 3 without. Each row is a DRM with the make-up of its shortest setups, U/D turns not counted (where two make-ups tie on side turns, the one with fewer quarter turns):

{{ring_profiles}}

- **4c2e**: 2 qt + 1 half turn is {= pcx(RPROF('4c2e', 2, 1)) =} ✓, 3 qt is {= pcx(RPROF('4c2e', 3, 0)) =} ✓.
- **7c8e**: 2 qt + 1 half turn is {= pcx(RPROF('7c8e', 2, 1)) =} ✓ on {= pcx(RPROF('7c8e', 2, 1, 'share')) =} ✓ of 7c8e. That is the closest thing to a certain switch outside the certain class.
- **3c2e**: 2 qt + 1 half turn is {= pcx(RPROF('3c2e', 2, 1)) =} ✓, and the cases that need a second half turn are {= pcx(RPROF('3c2e', 2, 2)) =} ✓. So *always switch* is really two groups.
- **The low DRMs**: 2 qt + 1 half turn is around a half for 4c6e ({= pcx(RPROF('4c6e', 2, 1)) =} ✓), 5c4e ({= pcx(RPROF('5c4e', 2, 1)) =} ✓) and 5c6e ({= pcx(RPROF('5c6e', 2, 1)) =} ✓), on 3% to 5% of each.

The same rows on the real attempts and for the other RZP lengths are in appendix A.

### 5.3 The cases with 2 side turns

These are the triggers the server sets up to, "4e4c - set up to R", "2e3c - set up to R U R or R U' R", "2e4c - set up to R U2 R" (compLex, [[T6504]]), "6e4c - R U2 L", "8e7c - R U L and R U' L" (Zagros, [[T6507]]), with any U and D turns around them: `R` for 4c4e, `R U2 R` for 4c2e, `R U R` for 3c2e, `R U L` for 7c8e, `R L` for 8c8e, `R U2 L` for 4c6e, `R U D2 L` for 3c6e, and for 4c4e also the cases one half turn from two bars. In ring notation, up to exchanging the layers and mirror image, one row per picture:

{{ring_triggers}}

2c2e, 3c4e, 5c4e, 5c6e and 6c6e have no case with 2 side turns. One example per DRM, each the longest of its kind:

```
{= RXF('4c2e_s2', '4c2e') =}

{= RXF('3c2e_s2', '3c2e') =}

{= RXF('7c8e_s2', '7c8e') =}

{= RXF('8c8e_s2', '8c8e') =}

{= RXF('4c6e_s2', '4c6e') =}

{= RXF('3c6e_s2', '3c6e') =}
```

### 5.4 One half turn away

A setup of 2 qt + 1 half turn has its half turn in one of two places. *Before both quarter turns*: one half turn (after any U/D turns) leaves a 2-side-turn case of section 5.3. *Between them*: one R or L quarter turn leaves a 4c4e that is one half turn from two bars. One row per DRM and place:

{{ring_hqq}}

For 2c2e, 3c4e, 5c4e, 5c6e and 6c6e it is always the second kind: the good cases are the ones where an R or L turn gives a 4c4e with 3 or 4 pairs and at most one row swap left.

```
{= RXF('7c8e_s3', '7c8e, one half turn from R U L') =}

{= RXF('7c8e_5p_long', '7c8e with 5 pairs, but 2 half turns needed') =}

{= RXF('5c4e_s3', '5c4e: L, then one half turn from two bars') =}
```

### 5.5 With the cards

The cards of section 6 and the side turns see different things, so they stack. *Short* means 3 side turns or fewer with no extra quarter turn (1 qt for 4c4e, 2 qt for the rest). Each row is a card group, split into its short cases and the others:

{{ring_cross}}

- **7c8e, 5 or 6 pairs**: short is {= pcx(RCROSS('7c8e', '5 or 6 pairs', 'short')) =} ✓, not short is {= pcx(RCROSS('7c8e', '5 or 6 pairs', 'not short')) =} ✓. The card's 59% was an average of those two.
- **4c2e, 1.5+ pairs**: {= pcx(RCROSS('4c2e', 'pairs + side pairs/2 is 1.5 or more', 'short')) =} ✓ against {= pcx(RCROSS('4c2e', 'pairs + side pairs/2 is 1.5 or more', 'not short')) =} ✓.
- **3c2e**: {= pcx(RCROSS('3c2e', 'any', 'short')) =} ✓ against {= pcx(RCROSS('3c2e', 'any', 'not short')) =} ✓.
- **2c2e with a paired edge**: {= pcx(RCROSS('2c2e', 'a bad edge with a pair', 'short')) =} ✓ against {= pcx(RCROSS('2c2e', 'a bad edge with a pair', 'not short')) =} ✓.
- **The discards get cleaner too.** 3c6e that is not short is {= pcx(RCROSS('3c6e', 'any', 'not short')) =} ✓ on {= pcx(RCROSS('3c6e', 'any', 'not short', 'share')) =} ✓ of it. 4c6e that is not short and has neither JZP nor 4 pairs is {= pcx(RCROSS('4c6e', 'anything else', 'not short')) =} ✓ on {= pcx(RCROSS('4c6e', 'anything else', 'not short', 'share')) =} ✓.

The real attempts follow the exact rates: in the rows with at least 5,000 attempts the largest gap is {= f1(max(abs(v['p6'] - v['q5']) for v in RJ['cross'].values() if v['a5'] >= 5000) * 100) =} points.

### 5.6 What of this you can read by hand

- **The 2-side-turn cases**: by hand. They are the trigger cases, and the pictures above are all of them.
- **One half turn before a trigger case**: by hand if you know the trigger pictures. It is the same row-swap look as for 4c4e, one swap deep, towards a picture of section 5.3 instead of two bars. I have no pair-count recipe for it like the 4c4e one.
- **A half turn between the quarter turns**: by hand as a two-step look. Do the R or L turn in your head with the quarter-turn rule of section 4.1 (on that face, good corners come out pointing at the face's edge, corners pointing at it come out good), then read the 4c4e you get with section 4.4.
- **Telling 3 side turns from 4 in general**: that is a search, not a read. If you don't see a short setup, treat the case as not short. The not-short rates above are then a floor for the group you end up with, because it also holds the short cases you missed.
