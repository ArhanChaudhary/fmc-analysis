## 12. What this does not cover

- **Time.** I didn't time any check. The cards use the same tracing solvers already do, but whether a given solver should spend the extra look on edge ARM, or on the corner case inside the your-call group, depends on their speed. Section 4 says which looks pay off most.
- **Findability.** Sub-7 means some DR of 6 or less exists, not that you find it. rodneykinney's "findable" versions and the server's worry about rare shapes ("the "% of sub-7" stat has a couple of flaws", Evan, [[T9341]]) are not modelled.
- **Beyond sub-7.** The target is a DR in 6 (or 5, or 7). The finish after the DR, and the value of variations such as AR and anti-AR cases, are not counted. A 7-move DR into a good HTR case can beat a 6-move one.
- **The real attempts** count every EO of up to 6 moves equally, not the ones a solver finds first, and the many attempts of one scramble are not independent (errors are from batches of scrambles). Rule rates on them are a check, not the source.
- **NISS EOs.** For an EO found partly on each side, the last turn on each side can change, and pair counts read before the EO is finished can be off. The cards assume the case after EO + RZP is what you trace.
- **Two DR axes at once.** Section 6 gives the gain from the second axis. I didn't build a combined rule over both axes of one EO.
- **The tracings** in section 5 are checked on {= n(TRACE('side pairs', 'uniform')[0]) =} random cubes each, not proved.
