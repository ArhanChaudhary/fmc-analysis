## 12. The sheets, reproduced

I recomputed every published number I could match to a definition: exact tables to their printed rounding, sampled ones within three standard errors of the exact value. One row per source:

{{reproduce}}

{= n(E['repro']['match']) =} of {= n(E['repro']['n']) =} reproduce. The two that don't are both in **Evan's *arm/pairs***, far outside the sample's error. Each row is a sub-7 rate as a fraction, on the sheet and exact:

| Evan's *arm/pairs*, 4c4e | Sub-7 rate on the sheet | Sub-7 rate, exact | Distance in standard errors |
|---|---|---|---|
| 2 pairs | {= REP('4c4e 2 pairs sub-7', 'published', 'C13') =} | {= f3(REP('4c4e 2 pairs sub-7', 'ours', 'C13')) =} | ${= REP('4c4e 2 pairs sub-7', 'verdict', 'C13').split('(')[1].rstrip(')').replace('=', ' = ') =}$ |
| 3 pairs | {= REP('4c4e 3 pairs sub-7', 'published', 'C13') =} | {= f3(REP('4c4e 3 pairs sub-7', 'ours', 'C13')) =} | ${= REP('4c4e 3 pairs sub-7', 'verdict', 'C13').split('(')[1].rstrip(')').replace('=', ' = ') =}$ |

Its ARM 21 cell does match. The two cells are in the sheet's sampled tab, in a block of {= n(SH('evan', 'n')) =} samples whose own total row is {= f3(SH('evan', 'all6')) =} for sub-7: about {= round(SH('evan', 'z_plain')) =} standard errors under the uniform {= f3(SH('evan', 'uniform6')) =} ({= round(SH('evan', 'z_all')) =} at the least, the cell being rounded). The ARM block beside it is a separate sample (its fifteen ARM totals add up to exactly {= n(SH('evan', 'n_arm')) =}) and matches. So the pairs block is not a uniform sample of cases, and its two cells are low with the rest of it; its total is near the same-side rate after an RZP ({= pc(POP('4c4e', 1)) =}, section 8). The sheet's exact tab (*44-more*, all {= n(SH('evan', 'more_n')) =} cases) has the two cells at {= f3(SH('evan', 'more2')) =} and {= f2(SH('evan', 'more3')) =}, the exact values.

**rodneykinney's sheet folds corner ARM.** *DRM corner variant+pair stats* follows "Use up-to-rotation corner ARM numbers to cut the number of cases in half" ([[T8104]]): its 4a-0 row holds corner ARM 0 and 4, and so does 4b-0. *DRM Subsets* splits 4a-4 off. I follow each source as it is. For 4c2e the fold matters: 4a-0 with 2 pairs is {= pc(CX('T8147-3qt', 'arm0', 2)) =} with corner ARM 0 and {= pc(CX('T8147-3qt', 'arm4', 2)) =} with corner ARM 4 (section 13).

**Fanti's figures are any-turn.** Fanti's rule figures in *armpairs_1.txt* ([[D15160]]) match the optimum that allows F and B quarter turns exactly, not the EO-kept one (U, D, R, L, F2, B2) that the other tables use. EO-kept they move by about a point at most (section 13). I use EO-kept throughout: with an EO, you keep the EO.

**What is in a match.** rodneykinney's *DRM corner variant+pair stats* ({= E['repro_by']['C8'][0] =} cells) and the *DRM Subsets* ranking and trees ({= E['repro_by']['C9'][0] =}) match exactly. Louis's corner-case and twist-split figures, Radek B's tables from Louis's data and Cale's two sheets match. Evan's subtype stats and Levi Gibson's simulations are within their sample error. rodneykinney's "findable sub-7" numbers (the *DRM Subsets* trees) are not reproduced: they classify the one optimal solution the generator kept per case, so they depend on search order. Louis's README says so: "optimal sequence is only the first one that is found by the search algorithm, others are discarded".
