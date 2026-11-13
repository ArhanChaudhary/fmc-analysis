## 9. The existing rules, graded

Every rule from the server I could pin down, graded the same way on the switched case, one rule per row. *Switches*: the share of the DRM it switches. *Sub-7 among switched*: how often a switch finds a DR in 6 (precision). *Sub-7 states switched*: the share of the DRM's sub-7 cases it switches (recall). *Sub-7 states discarded*: sub-7 cases it throws away, as a share of all the DRM's cases. Exact, every case once. The last column is the same precision on the real attempts at a total of 5. The card's rows come first (bold), then the rules by precision. The two 4-move rules (Daichi, Zagros) are graded against DR in 7 and Fanti's 6-move 3c2e rule against DR in 5, since that's what they're for.

{{grades}}

**The counts of sections 4 and 5 as switch rules**, in the same columns. One row per rule:

{{ring_grades}}

What the table says:

- **Real attempts change nothing.** The last column is close to the exact precision everywhere (the RZP bias is gone after a switch, section 8). The largest gap is Lewis Isom's 8c8e list, a small and rare group ({= pc(GR('88-lewis', 'precision')) =} exact, {= pc(GR('88-lewis', 'p3')) =} in attempts).
- **4c4e.**
  - The rules built on 2+ pairs all land between {= pc(min(GR(i, 'precision') for i in ['44-2pairs', '44-rodney-case', '44-rodney-case+0p', '44-tetrad', '44-complex', '44-tseitsei', '44-subsets', '44-jay', '44-wen', '44-armthenpairs', '44-caycala-5', '44-caycala-5-strict'])) =} and {= pc(max(GR(i, 'precision') for i in ['44-2pairs', '44-rodney-case', '44-rodney-case+0p', '44-tetrad', '44-complex', '44-tseitsei', '44-subsets', '44-jay', '44-wen', '44-armthenpairs', '44-caycala-5', '44-caycala-5-strict'])) =} precision while switching {= pc(min(GR(i, 'share_switched') for i in ['44-2pairs', '44-rodney-case', '44-rodney-case+0p', '44-tetrad', '44-complex', '44-tseitsei', '44-subsets', '44-jay', '44-wen', '44-armthenpairs', '44-caycala-5', '44-caycala-5-strict'])) =} to {= pc(max(GR(i, 'share_switched') for i in ['44-2pairs', '44-rodney-case', '44-rodney-case+0p', '44-tetrad', '44-complex', '44-tseitsei', '44-subsets', '44-jay', '44-wen', '44-armthenpairs', '44-caycala-5', '44-caycala-5-strict'])) =} of 4c4e. Corner-case refinements (rodneykinney, compLex, tseitsei89, Jay, wen) move each by a point or two.
  - ARM-only rules switch more at lower precision. Yura Riabov's "good" list is {= pc(GR('44-yura-good', 'precision')) =}, and *anything but trash* keeps almost every sub-7 at {= pc(GR('44-yura-nottrash', 'precision')) =}. Those are discard rules, and good ones: Yura Riabov's four "trash" ARMs throw away only {= pc(GR('44-yura-nottrash', 'target_states_discarded')) =} of 4c4e as lost sub-7s.
  - Fanti's rule switches the most of the pair rules ({= pc(GR('44-fanti', 'share_switched')) =}) and keeps {= pc(GR('44-fanti', 'recall')) =} of the sub-7s.
- **The 4c4e card** gives a smaller, better switch group, and with the your-call group added it keeps {= pcx(RULE('4c4e', 'kept') + RG('4c4e', 'check', 'hits') / RULE('4c4e', 'all', 'hits')) =} of the sub-7s, more than any pair rule, at {= pc((RG('4c4e', 'switch', 'hits') + RG('4c4e', 'check', 'hits')) / (RG('4c4e', 'switch', 'n') + RG('4c4e', 'check', 'n'))) =}.
- **The half-turn count** beats every 4c4e row above at its own size: *2 half turns or fewer* switches {= pcx(RHG('le2', 'share')) =} at {= pcx(RHG('le2')) =}, where the pair rules of that size are at {= pcx(RCARD('switch')) =} or less, and *3 or fewer* keeps {= pcx(1 - RHG('ge4', 'of_hits')) =} of the sub-7s while dropping {= pcx(RHG('ge4', 'share')) =} of 4c4e. It costs a look where the others cost a count (section 4.4).
- **4c2e.** Four rules are the same rule ("1.5+ pairs"); rodneykinney's stricter 1 pair and 1 side pair is a little more precise and switches less. ARM-only rules are well behind.
- **7c8e.** 5-6 pairs is the core. The rules that add 4-pair cases by ARM (the chart in Brayan's question [[D13502]], Fanti, tseitsei89) keep about three quarters of the sub-7s at about 50%. Lewis Isom's ARM list is precise ({= pc(GR('78-lewis', 'precision')) =}) but switches only {= pc(GR('78-lewis', 'share_switched')) =}.
- **8c8e.** No rule is both precise and common. tseitsei89's fake-pair rule is {= pc(GR('88-tseitsei', 'precision')) =}, about the 8c8e base rate ({= pcx(RULE('8c8e', 'all', 'p6')) =}).
- **The low DRMs.** The rules there either switch a few percent of cases or switch at about the base rate. The best is 4c6e JZP with b corners (tseitsei89, {= pc(GR('46-tseitsei', 'precision')) =} on {= pc(GR('46-tseitsei', 'share_switched')) =}).
