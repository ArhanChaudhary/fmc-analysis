## 8. What each feature adds

**How much each settles.** Exact. Each row is a feature (or two) to split by, using every value it takes; each cell is the share of that DRM that lands in cells under 10% or over 50%.

{{decided_by_feature}}

- **Pairs settle more than ARM** in 4c4e, 4c2e and 7c8e. In 8c8e and 2c2e ARM settles more. The corner case alone settles little anywhere: it is a refinement, not a first look. rodneykinney's corner orbit case is only worth reading inside a pair group (4c4e: the your-call group, section 4.1).
- **For 4c4e, the edges matter more than the count.** Paired edges plus edge ARM ({= pc(STRICT('4c4e', 'edges_paired+earm')) =} with all 9 cells, {= pc(RULE('4c4e', 'decided')) =} once edge ARM 0 and 2 are pooled as on the card) beat pairs + ARM ({= pc(STRICT('4c4e', 'pairs+carm+earm')) =}) and pairs + corner case ({= pc(STRICT('4c4e', 'pairs+corner_case+case_suffix')) =}).

**wen's 2 of 3** ([[D14349]]): switch the best {= pc(GR('44-2pairs', 'share_switched')) =} of 4c4e (as many as "2+ pairs" switches) by each pair of criteria, best cells first, which is a **computer-only** way to use them. Each row is a way to pick them; the column is the share of 4c4e's sub-7 cases you miss:

| Criteria (4c4e) | Sub-7s missed (share of 4c4e's sub-7s) |
|---|---|
| pairs + corner case | {= pc(float(Q4('4c4e, switching the best 0.260 of states (the share of 2+ pairs), pairs + corner case').split()[2])) =} |
| pairs + ARM | {= pc(float(Q4('4c4e, switching the best 0.260 of states (the share of 2+ pairs), pairs + ARM').split()[2])) =} |
| ARM + corner case | {= pc(float(Q4('4c4e, switching the best 0.260 of states (the share of 2+ pairs), ARM + corner case').split()[2])) =} |
| all three | {= pc(float(Q4('4c4e, switching the best 0.260 of states (the share of 2+ pairs), all three').split()[2])) =} |
| 2+ pairs alone | {= pc(float(Q4('4c4e, 2+ pairs alone').split()[2].rstrip(','))) =} |

**Bars against separate pairs.** In 4c4e, two pairs as a bar on one edge against two pairs on the two edges. One row per ARM: the two sub-7 rates, then how many states each rests on:

{{bars}}

Yura Riabov had it from experience: "From my experience with pairs 1 bar is worse than 2 pairs for most arms" ([[D12993]]), "Also a bar+fake pair sucks" ([[D12996]]). It holds in every ARM, by a wide margin. With a bar, the second pair is on an edge that is already paired, so the other bad edge has nothing. That's why the card counts paired edges.

**Unpaired corners or pairs?** Zagros asked whether "number of corners NOT in a pair" beats pairs across all DRMs ([[T11345]]). Pooled over the named DRMs without the DRM, unpaired corners carry more information ({= Q4('all named DRMs pooled, without the DRM: unpaired_corners').split()[1] =} against {= Q4('all named DRMs pooled, without the DRM: pairs').split()[1] =} bits, **computer only**). Once you know the DRM, which you always do, both add the same ({= Q4('all named DRMs pooled, without the DRM: pairs').split()[-2] =} bits), since within a DRM one is the other subtracted from a constant. So it's just convenience: count whichever is faster for you.

**Side pairs, outside 4c2e.** Jay thought side pairs aren't useful outside 4c2e ("I don't think they're any useful for other DRM's at the moment though", [[T8144]]). For 4c4e, pairs + side pairs/2 settles {= pc(STRICT('4c4e', 'pairs_plus_half_side_x2')) =}, more than pairs alone ({= pc(STRICT('4c4e', 'pairs')) =}) but less than the card. For 2c2e it settles {= pc(STRICT('2c2e', 'pairs_plus_half_side_x2')) =}, but the card's paired edge + JZP is simpler and settles more.
