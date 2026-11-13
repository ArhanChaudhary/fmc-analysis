## 11. Computer-only rules: the answer key

Everything in this section is **computer only**. It says how far any rule could go, not what to do at the table. The search here is over pair-trace features; the half-turn and side-turn counts of sections 4 and 5 are not in it.

**The search.** For each DRM, every cross-table of 1, 2 or 3 of 38 features: the ARMs, pairs and their variants (fake, side, paired edges, bars, split pairs, AR bars, unpaired corners and edges), the corner case and suffix, twist split, layer layouts, JZP and anti-AR, and seven features that need a search in your head (moves to AR, moves to orient the corners, and the setup distance to each trigger family). I scored each rule by how much of the DRM it settles and kept it only if it holds on the RZP-weighted cases and the real attempts. The Pareto front, rule size against how much it settles. Each row is a rule: the features crossed, how many cells its table has, and the share of the DRM it settles:

{{search_pareto}}

- **The full setup distance is the perfect separator, and half of it is readable.** *How many U, D and half turns to an R/L-quarter-turn finish* settles all of 4c4e, and the same holds for 7c8e (R U L). Reading all of it means finding the DR, which is the server's habit of just NISS-tracing a promising case all the way. Zagros, on 4c2e: "For a drm that is mid on average but can be really good, skip all the stats and just niss trace and know 100% if you should switch." ([[D14199]]). But the distance is a sum: the half turns, which section 4 reads off the rings, and the U/D turns between them, which you only get by doing it. The half turns alone give the bands of section 4.3.
- **8c8e** needs {= E['c88_65']['cells'] =} cells (edge ARM × pairs × the orbit case of the out-of-AR corners) to settle {= pc(E['c88_65']['strict_sep_P1']) =}: a table to look things up in, not a rule.
- **The low DRMs** settle "completely" only because every cell is under 10%: that is the discard verdict. What the search asked for them is whether any traceable rule of up to three features finds a cell above 50% holding a real share of their sub-7s. One row per DRM: the best rule's share of that DRM's sub-7 cases in such cells:

| DRM | Sub-7s in cells above 50%, best rule (share of the DRM's sub-7s) |
|---|---|
| 4c6e | {= pc(E['low_best']['4c6e']) =} |
| 3c4e | {= pc(E['low_best']['3c4e']) =} |
| 3c6e | {= pc(E['low_best']['3c6e']) =} |
| 5c4e | {= pc(E['low_best']['5c4e']) =} |
| 5c6e | {= pc(E['low_best']['5c6e']) =} |
| 6c6e | {= pc(E['low_best']['6c6e']) =} |

  Short setups (section 5), which the search did not have, do better where you can see them. 4c6e at most one half turn before `R U2 L` is {= pcx((RJ['hqq']['4c6e']['first']['hits'] + RJ['short']['4c6e']['s2']['hits']) / (RJ['hqq']['4c6e']['first']['n'] + RJ['short']['4c6e']['s2']['n'])) =} and holds {= pcx(RJ['hqq']['4c6e']['first']['of_hits'] + RJ['short']['4c6e']['s2']['of_hits']) =} of 4c6e's sub-7s. Short 5c6e is {= pcx(RSHORT('5c6e')) =} and holds {= pcx(RSHORT('5c6e', 'short', 'of_hits')) =}. For 3c4e, 5c4e and 6c6e the short group stays under 50% ({= pcx(RSHORT('3c4e')) =}, {= pcx(RSHORT('5c4e')) =}, {= pcx(RSHORT('6c6e')) =}) until you add the pair count (section 5.5).

**Information.** JTuu asked when ARM is most informative ([[T4332]]). In information terms (the share of the uncertainty about sub-7 within the DRM that the feature removes), ARM removes {= Q4P('4c4e: entropy of sub-7 0.706 bits; explained by ARM / pairs / both', 0, ' / ') =}, pairs {= Q4P('4c4e: entropy of sub-7 0.706 bits; explained by ARM / pairs / both', 1, ' / ') =} and both {= Q4P('4c4e: entropy of sub-7 0.706 bits; explained by ARM / pairs / both', 2, ' / ') =} for 4c4e, and {= Q4P('8c8e: entropy of sub-7 0.597 bits; explained by ARM / pairs / both', 0, ' / ') =}, {= Q4P('8c8e: entropy of sub-7 0.597 bits; explained by ARM / pairs / both', 1, ' / ') =} and {= Q4P('8c8e: entropy of sub-7 0.597 bits; explained by ARM / pairs / both', 2, ' / ') =} for 8c8e: ARM tells more than pairs only in 8c8e, 3c6e and 6c6e. rodneykinney's score ([[T8327]], [[T8333]]) is the product $p(\text{sub-7} \mid \text{subset}) \times N(\text{sub-7 in subset})$, which ranks rules well but is not mutual information in the usual sense. The values for every DRM are in the study's repository, with the code.
