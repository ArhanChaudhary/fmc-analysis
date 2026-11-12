## 4. The switch cards, DRM by DRM

**The cards.** One line per DRM: what to check on the switched case, and how much of the DRM falls into each verdict with its sub-7 rate. Exact over all cases of the DRM. A blank verdict means the card has no such group. *Settled* is the share of the DRM in the switch and discard groups. The last column is the share of the DRM's sub-7 cases that the card switches, and the share it throws away.

{{rule_cards}}

How the cards were chosen: every cross-table of one, two or three readable features (38 features, section 9) was scored per DRM by how much of the DRM it puts in cells under 10% or over 50%. A card is the best of the ones a solver can trace, kept only if every labelled cell stays in its band on the cases RZPs reach and on the real attempts. Each verdict above is its group's own band (checked when the tables are built). No check here was timed. The only timing on the server is Yura Riabov's for pairs + ARM on 4c4e, "Like 5 seconds", "±2", "That's for 4c4e btw, for 7c8e it's longer" ([[D14244]], [[D14245]], [[D14248]]). The cards ask for no more than that: a pair trace, and for 4c4e one look at the edges.

**The cards cell by cell, with the RZP length.** The same cells on the real attempts at a total of 5 (EO + RZP), and the share with a DR in 7 (enough after a 4-move RZP) and in 5 (needed after a 6-move RZP):

{{rule_cells}}

So after a 4-move RZP, almost every 4c4e case with a paired edge is a switch, and after a 6-move RZP almost nothing is. The cut-offs that solvers already use ("i'll add 1 to trigger if it's 3c2e specifically", Jay, [[D239]]) fit this: 3c2e is {= pc(RCELL('3c2e', 0, 'p5')) =} for DR in 5, about what 4c4e with both edges paired is ({= pc(RCELL('4c4e', 0, 'p5')) =}).

### 4.1 4c4e

Trace the pairs on the inverse as usual, but note which bad edges they sit on.

1. **Both bad edges paired: switch** ({= pc(RG('4c4e', 'switch')) =}). With 3 pairs it is {= CELL('c44_bars', '3 pairs on 2 edge(s)', 'Sub-7 (exact)') =}, with 4 pairs {= CELL('c44_bars', '4 pairs on 2 edge(s)', 'Sub-7 (exact)') =}.
2. **No bad edge paired: discard** ({= CELL('c44_paired_earm', '0 paired, edge ARM 1', 'Sub-7 (exact)') =} at most, whatever the edge ARM).
3. **One paired edge: look at edge ARM** (or just at where the two bad edges are). Both in one slice (edge ARM 0 or 2): **discard**, {= pc(RCELL('4c4e', 2)) =}. One in M and one in S (edge ARM 1): **your call**, {= pc(RCELL('4c4e', 1)) =}. A bar counts as one paired edge: two pairs on one edge are {= CELL('c44_bars', '2 pairs on 1 edge(s) (a bar)', 'Sub-7 (exact)') =}, against {= CELL('c44_bars', '1 pairs on 1 edge(s)', 'Sub-7 (exact)') =} for a single pair.

By paired edges and edge ARM:

{{c44_paired_earm}}

Edge ARM 1 is the same thing as *the two bad edges are in different slices*, so the slice is no extra check once you have ARM. It also matches rodneykinney's slice penalty in *DR - 4c4e Theory*: "The slice penalty applies if you reach 1qt with both bad edges in the same slice." This is the one place where ARM helps a lot on top of pairs, and only the edge digit matters for it.

**The your-call group, split.** If your cut is around 20% ("i switch for around 20% and above", [[D7082]]), you can switch all {= pc(RG('4c4e', 'check', 'share')) =}: they're {= pc(RG('4c4e', 'check')) =} as a group. With a higher cut, the corner case and the corner ARM split them:

{{c44_check}}

Read: 4d corners are rare but a near-certain switch (this is Evan's "4d+1 is extremely good for AR-21 (~90% sub-7)", [[D14342]]). ARM 21 with 4b corners is a third. Corner ARM 0 or 4 with 4b corners is a discard. So with one paired edge and edge ARM 1: corner ARM 2 means switch if your cut is 30% or less (4b, 4d) and think again with 4a; corner ARM 0 or 4 means switch only with 4a; corner ARM 1 or 3 is {= CELL('c44_check', 'corner ARM 1 or 3 (4c corners)', 'Sub-7 (exact)') =}.

Against the rules in use (section 7): *2+ pairs* switches {= pc(GR('44-2pairs', 'share_switched')) =} of 4c4e at {= pc(GR('44-2pairs', 'precision')) =}, rodneykinney's pairs + corner case {= pc(GR('44-rodney-case', 'share_switched')) =} at {= pc(GR('44-rodney-case', 'precision')) =}. The card's switch group is smaller ({= pc(RG('4c4e', 'switch', 'share')) =}) and better ({= pc(RG('4c4e', 'switch')) =}), and its discard group is half of all 4c4e at {= pc(RG('4c4e', 'discard')) =}, where *fewer than 2 pairs* is {= pc(1 - GR('44-2pairs', 'share_switched')) =} of 4c4e at {= pc(GR('44-2pairs', 'target_states_discarded') / (1 - GR('44-2pairs', 'share_switched'))) =}. The new part is the middle: you know which {= pc(RG('4c4e', 'check', 'share')) =} are worth a thought.

### 4.2 4c2e

**Pairs + side pairs/2: 1.5 or more, switch; exactly 1, your call; 0 or 0.5, discard.** This is rodneykinney's rule ([[T9466]], [[T9468]]), and it switches exactly the same cases as Jay's ([[T8144]]) and tseitsei89's ([[T9321]]). The card adds the discard end ({= pc(RG('4c2e', 'discard', 'share')) =} of 4c2e at {= pc(RG('4c2e', 'discard')) =}) and a way to read side pairs from normal (section 5). By cell:

{{c42_cells}}

The your-call group is 1 pair and no side pair ({= CELL('c42_cells', '1 pairs, 0 side pairs', 'Sub-7 (exact)') =}) or 2 side pairs and no pair ({= CELL('c42_cells', '0 pairs, 2 side pairs', 'Sub-7 (exact)') =}). Two pairs without a side pair are {= CELL('c42_cells', '2 pairs, 0 side pairs', 'Sub-7 (exact)') =}, just under the line. Nothing cheap splits the your-call group well. By corner ARM, edge ARM or corner case every part stays between {= min([CELL('c42_check', r, 'Sub-7 (exact)') for r in ['corner ARM 0', 'corner ARM 1', 'corner ARM 2', 'corner ARM 3', 'corner ARM 4', 'edge ARM 0', 'edge ARM 1', '4a corners', '4b corners', '4c corners', '4d corners']], key=lambda x: float(x.rstrip('%'))) =} and {= max([CELL('c42_check', r, 'Sub-7 (exact)') for r in ['corner ARM 0', 'corner ARM 1', 'corner ARM 2', 'corner ARM 3', 'corner ARM 4', 'edge ARM 0', 'edge ARM 1', '4a corners', '4b corners', '4c corners', '4d corners']], key=lambda x: float(x.rstrip('%'))) =}, and the best part is JZP ({= CELL('c42_check', 'JZP', 'Sub-7 (exact)') =}, {= CELL('c42_check', 'JZP', 'Share of the DRM') =} of 4c2e). Table in appendix A.

### 4.3 3c2e and 2c2e

**3c2e: always switch** ({= pc(RULE('3c2e', 'all', 'p6')) =}). With a pair it is {= CELL('c32_pairs', '1 pairs', 'Sub-7 (exact)') =}, without {= CELL('c32_pairs', '0 pairs', 'Sub-7 (exact)') =}. wen's rule (switch on a pair, a fake pair or a split pair, [[D16512]]) switches {= pc(GR('32-wen', 'share_switched')) =} at {= pc(GR('32-wen', 'precision')) =} and never drops a case of 5 or less, as wen said.

**2c2e: switch with a paired edge** ({= pc(RG('2c2e', 'switch')) =}), **your call with no pair but JZP** ({= pc(RG('2c2e', 'check')) =}), otherwise discard ({= pc(RG('2c2e', 'discard')) =}). It's rare: {= pc(VAR('2c2e', 'cosets') / 1082565) =} of EO-solved cases.

### 4.4 7c8e

**5 or 6 pairs: switch** ({= pc(RG('7c8e', 'switch')) =}, rodneykinney's "For 7c8e, it's 5 or 6 pairs", [[T8142]]). **3 or fewer: discard** ({= pc(RG('7c8e', 'discard')) =}). **4 pairs: your call** ({= pc(RG('7c8e', 'check')) =}), and here edge ARM is the split:

{{c78_check}}

So 4 pairs with edge ARM 1 is worth switching at a 30% cut, and 4 pairs otherwise is not. This is close to tseitsei89's "4 pairs = switch if edge arm < 2" ([[T9314]]). Edge ARM 0 is in it but empty of sub-7s, and it's only {= CELL('c78_check', '4 pairs, edge ARM 0', 'Share of the DRM') =} of 7c8e. By pairs alone:

{{c78_pairs}}

ARM on top of pairs adds little: the full pairs × ARM table settles {= pc(STRICT('7c8e', 'pairs+carm+earm')) =} of 7c8e, against {= pc(STRICT('7c8e', 'pairs')) =} for pairs alone (section 8).

### 4.5 8c8e

**No group is a switch.** The one cheap discard is corner ARM 2, 3, 5 or 6 ({= pc(RG('8c8e', 'discard', 'share')) =} of 8c8e at {= pc(RG('8c8e', 'discard')) =}). The rest (corner ARM 0, 4 or 8) is {= pc(RG('8c8e', 'check')) =}, your call:

{{c88_carm}}

Pairs don't help much for 8c8e: the best common pair count, 6, is {= CELL('c88_pairs', '6 pairs', 'Sub-7 (exact)') =} (appendix A). The best 1-3 feature rule needs {= E['c88_65']['cells'] =} cells (edge ARM × pairs × the orbit case of the out-of-AR corners) to settle {= pc(E['c88_65']['strict_sep_P1']) =}, which is **computer only**. The *correct 8c* check (R L gives JZP, Jay [[T3767]], Yura Riabov [[D16930]]) is always sub-7, but it covers {= pc(GR('88-correct', 'share_switched')) =} of 8c8e.

### 4.6 The low DRMs: 4c6e, 3c4e, 3c6e, 5c4e, 5c6e, 6c6e

**Discard**, with these exceptions worth knowing:

- **4c6e JZP: switch** ({= pc(RG('4c6e', 'switch')) =}, {= pc(RG('4c6e', 'switch', 'share')) =} of 4c6e), as Yura Riabov said: "You shouldn't switch 6e4c unless it's jzp" ([[D6915]]). 4c6e with 4 pairs is {= pc(RG('4c6e', 'check')) =} (Radek B's "Like only if there are 4 pairs (or if it's jzp)", [[D7471]]).
- **3c4e with 2 pairs** ({= pc(RG('3c4e', 'check')) =}, {= pc(RG('3c4e', 'check', 'share')) =} of 3c4e), **5c4e with 3 pairs** ({= pc(RG('5c4e', 'check')) =}), **5c6e with 4 pairs** ({= pc(RG('5c6e', 'check')) =}), **6c6e with JZP or 5-6 pairs** ({= pc(RG('6c6e', 'check')) =}): your call, all rare.
- **3c6e**: no pair count is above {= pc(E['pairs_max']['3c6e']) =}; Fanti's 3 pairs with ARM 00 or 2 pairs with ARM 21 ([[D15179]]) is {= pc(GR('36-fanti', 'precision')) =} on {= pc(GR('36-fanti', 'share_switched')) =} of 3c6e, and ARM 21 alone (Jay, [[D6982]]) {= pc(GR('36-jay', 'precision')) =}.

By pairs:

{{low_pairs}}

Together these exceptions catch few of the sub-7 cases: {= pc(RULE('4c6e', 'kept')) =} of 4c6e's in its switch group. No rule of up to three traceable features does much better (section 9).
