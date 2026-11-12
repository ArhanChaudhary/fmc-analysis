## 10. The sheets, reproduced

Every published number that could be matched to a definition was recomputed: exact tables to their printed rounding, sampled ones within three standard errors of the exact value.

{{reproduce}}

{= n(E['repro']['match']) =} of {= n(E['repro']['n']) =} reproduce. The two that don't are both in **Evan's *arm/pairs***, 4c4e with 2 and 3 pairs. The sheet prints {= REP('4c4e 2 pairs sub-7', 'published', 'C13') =} and {= REP('4c4e 3 pairs sub-7', 'published', 'C13') =}. The exact values are {= f3(REP('4c4e 2 pairs sub-7', 'ours', 'C13')) =} and {= f3(REP('4c4e 3 pairs sub-7', 'ours', 'C13')) =}, far outside the sample's error ({= REP('4c4e 2 pairs sub-7', 'verdict', 'C13').split('(')[1].rstrip(')') =} and {= REP('4c4e 3 pairs sub-7', 'verdict', 'C13').split('(')[1].rstrip(')') =}). Its ARM 21 cell does match. No definition tried explains the gap (optimal with any turns, paired corners, edges with a pair).

**Fanti's figures are any-turn.** Fanti's rule figures in *armpairs_1.txt* ([[D15160]]) match the optimum that allows F and B quarter turns exactly, not the EO-kept one (U, D, R, L, F2, B2) that the other tables use. EO-kept they move by about a point at most (section 11). This study uses EO-kept throughout. With an EO you keep the EO.

**What is in a match.** rodneykinney's *DRM corner variant+pair stats* ({= E['repro_by']['C8'][0] =} cells) and the *DRM Subsets* ranking and trees ({= E['repro_by']['C9'][0] =}) match exactly. Louis's corner-case and twist-split figures, Radek B's tables from Louis's data and Cale's two sheets match. Evan's subtype stats and Levi Gibson's simulations are within their sample error. rodneykinney's "findable sub-7" numbers (the *DRM Subsets* trees) are not reproduced: they classify the one optimal solution the generator kept per case, so they depend on search order. Louis's README says so: "optimal sequence is only the first one that is found by the search algorithm, others are discarded".
