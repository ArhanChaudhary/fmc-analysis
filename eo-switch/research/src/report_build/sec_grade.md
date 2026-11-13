## 9. The existing rules, graded

Every rule from the server I could pin down, graded the same way on the switched case, one rule per row, each as its author stated it. *Switches*: the share of the DRM it switches. *Sub-7 among switched*: how often a switch finds a DR in 6 (precision). *Sub-7 states switched*: the share of the DRM's sub-7 cases it switches (recall). *Sub-7 states discarded*: sub-7 cases it throws away, as a share of all the DRM's cases. Exact, every case once. The last column is the same precision on the real attempts at a total of 5. The card's rows come first (bold), then the rules by precision. The two 4-move rules (Daichi, Zagros) are graded against DR in 7 and Fanti's 6-move 3c2e rule against DR in 5, since that's what they're for.

Not every row is a rule its author stands by. Some are a habit, a first sketch or an aside, and a grade is not a verdict on those. One row per such entry, with how its author put it:

{{grades_notes}}

Left out, as they are not switch rules: the subsets that rodneykinney's *DRM Subsets* and *DRM Subsets Meta* give for 5c4e, 5c6e, 4c6e and 6c6e, which say what to try on normal (the NISS column of the Meta says "Never" for all four), and their 4c4e corner-case table, headed "Recommendations for normal scramble" (for the switch, "the general 4c4e rule above is good enough for deciding whether to NISS").

The grades, one rule per row:

{{grades}}

**The counts of sections 4 and 5 as switch rules**, in the same columns. One row per rule:

{{ring_grades}}

What the table says:

- **Real attempts change nothing.** The last column is close to the exact precision everywhere (the RZP bias is gone after a switch, section 8). The largest gap is Lewis Isom's 8c8e list, a small and rare group ({= pc(GR('88-lewis', 'precision')) =} exact, {= pc(GR('88-lewis', 'p3')) =} in attempts).
- **4c4e.**
  - The rules built on 2+ pairs all land between {= pc(min(GR(i, 'precision') for i in PAIRRULES)) =} and {= pc(max(GR(i, 'precision') for i in PAIRRULES)) =} precision while switching {= pc(min(GR(i, 'share_switched') for i in PAIRRULES)) =} to {= pc(max(GR(i, 'share_switched') for i in PAIRRULES)) =} of 4c4e. Corner-case refinements (rodneykinney, compLex, tseitsei89, Jay, wen) move each by a point or two. The most precise is Yura Riabov's ARM first, then pairs ({= pc(GR('44-armthenpairs', 'precision')) =} on {= pc(GR('44-armthenpairs', 'share_switched')) =}).
  - ARM-only rules switch more at lower precision. Yura Riabov's "good" list is {= pc(GR('44-yura-good', 'precision')) =}, and *anything but trash* keeps almost every sub-7 at {= pc(GR('44-yura-nottrash', 'precision')) =}. Those are discard rules, and good ones: Yura Riabov's four "trash" ARMs throw away only {= pc(GR('44-yura-nottrash', 'target_states_discarded')) =} of 4c4e as lost sub-7s.
  - Fanti's rule switches the most of the pair rules ({= pc(GR('44-fanti', 'share_switched')) =}) and keeps {= pc(GR('44-fanti', 'recall')) =} of the sub-7s.
- **The 4c4e card** gives a smaller, better switch group, and with the your-call group added it keeps {= pcx(RULE('4c4e', 'kept') + RG('4c4e', 'check', 'hits') / RULE('4c4e', 'all', 'hits')) =} of the sub-7s, more than any pair rule, at {= pc((RG('4c4e', 'switch', 'hits') + RG('4c4e', 'check', 'hits')) / (RG('4c4e', 'switch', 'n') + RG('4c4e', 'check', 'n'))) =}.
- **The half-turn count** beats every 4c4e row above at its own size: *2 half turns or fewer* switches {= pcx(RHG('le2', 'share')) =} at {= pcx(RHG('le2')) =}, where the pair rules of that size are at {= pcx(RCARD('switch')) =} or less, and *3 or fewer* keeps {= pcx(1 - RHG('ge4', 'of_hits')) =} of the sub-7s while dropping {= pcx(RHG('ge4', 'share')) =} of 4c4e. It costs a look where the others cost a count (section 4.4).
- **4c2e.** Four rules are the same rule ("1.5+ pairs"); rodneykinney's stricter 1 pair and 1 side pair is a little more precise and switches less. ARM-only rules are well behind.
- **7c8e.** 5-6 pairs is the core. The rules that add 4-pair cases by ARM (caycala's chart [[D11016]], Fanti, tseitsei89) keep about three quarters of the sub-7s at about 50%. Lewis Isom's ARM list is precise ({= pc(GR('78-lewis', 'precision')) =}) but switches only {= pc(GR('78-lewis', 'share_switched')) =}.
- **8c8e.** rodneykinney's decision tree is the best rule there: "The decision tree for 8c8e (all difficulties) actually identifies fake pairs <= 3 as the most important feature" ([[T9558]]). 3 fake pairs or fewer with edge ARM not 2 switches {= pc(GR('88-tree', 'share_switched')) =} of 8c8e at {= pc(GR('88-tree', 'precision')) =}, against a base rate of {= pcx(RULE('8c8e', 'all', 'p6')) =}. With the tree's 6-pair branch it is {= pc(GR('88-tree-6p', 'share_switched')) =} at {= pc(GR('88-tree-6p', 'precision')) =}, holding {= pc(GR('88-tree-6p', 'recall')) =} of the sub-7s. tseitsei89 read the tree out for zakimoshi ([[T9568]], where it is typed ">=3"; the tree's box is 3 or fewer). Lewis Isom's ARM list is close in precision ({= pc(GR('88-lewis', 'precision')) =}) on {= pc(GR('88-lewis', 'share_switched')) =} of 8c8e.
- **The low DRMs.** The rules here are for 4c6e, 3c4e and 3c6e (for 5c4e, 5c6e and 6c6e I found none, and *DRM Subsets Meta* says "Never"). The best is 4c6e JZP with b corners (tseitsei89, {= pc(GR('46-tseitsei', 'precision')) =} on {= pc(GR('46-tseitsei', 'share_switched')) =}). For 3c4e, 2+ pairs is {= pc(GR('34-rodney', 'precision')) =} on {= pc(GR('34-rodney', 'share_switched')) =}; the 3c6e rows are {= pc(GR('36-fanti', 'precision')) =} or less.
