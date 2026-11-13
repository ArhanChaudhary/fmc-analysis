## 5. The existing sheets, cell by cell

**Levi Gibson's *allcases*.** Its paths are linear chains in Jay's qt names, one path per state; the shares add to 1 per subset. Asked whether ties between optimal solutions were factored in, the answer was "Not factored in" ([[D8302]]). Pick one leave-slice optimal per state at random among the optimal finishes (5,000 states per subset × edges, seed 7) and you get the sheet back, over {= n(D171('d171_ls', 0)) =} paths:

| Random optimal per state | Mean difference from the sheet (points) | Correlation |
|---|---|---|
| leave slice | {= f1(D171('d171_ls', 1) * 100) =} | {= f3(D171('d171_ls', 2)) =} |
| E slice solved | {= f1(D171('d171_full', 1) * 100) =} | {= f3(D171('d171_full', 2)) =} |

So its shares are *the path of one optimal found by a solver*, a third reading between *some optimal* and *every optimal*. Where the sheet and the random pick differ, the sheet has the fewer-qt path more often, by more than the 5,000-state sample explains:

| Cell | Rows | Sheet | One optimal at random |
|---|---|---|---|
| 4b2 4e | 2qt | {= pc(E['ac_4b2_4e']['two']) =} | {= EV('C06', '2qt ') =} |
| 4a1 4e | 5qt | {= pc(E['ac_4a1_4e']['five']) =} | {= EV('C05', 'at random has 5+ qt ') =} |

So the solver behind it probably preferred fewer quarter turns among equal-length finishes.

**2qt(a) and 2qt(b).** The old names say "2qt(a)" and "2qt(b)" where today's say 4a2 and 4b2. The server worked most of this out: Tzak on *allcases*' letters, "good one, the bad one can't turn into 2c3" ([[D8300]]); its author, "And yes, a and b are swapped in line with the old naming scheme", "a is the R U2 R’ case" ([[D9464]], [[D9465]]); Zagros, "I think a and b might be flipped" ([[D9451]]). What the sheets themselves show:

- Aedan Bryant's *HTR Subset Stats* lists a trigger for every case. Played on a cube, its "2qt (a)" triggers are {= NM('doc15', '2qt (a) 4C') =}, {= NM('doc15', '2qt (a) 4C2E') =} and {= NM('doc15', '2qt (a) 4C4E') =}, and its "2qt (b)" ones are 4a2. For example:

  ```
  U R2 U   // the sheet's 2qt (a) 4C2E trigger
  ```
- *allcases* has no triggers, but its own data settles it: its "2qt(a)" rows go to a "3qt 2c" case with one qt ({= E['ac_a_to_2c'] =} rows do), none of its {= E['ac_b_rows'] =} "2qt(b)" rows does, and only 4b2 can reach 2c3 with one quarter turn. So 2qt(a) is 4b2 there too, as its author and Tzak said.
- The *Extra Quarter-Turn Stats* sheet has the letters the other way round: its own example triggers put "2qt(b)" on 4b2. That part is new.

So mrauo's "Only 1/3 of 2q 4b2e cases use 2qt for optimal wtf" ([[D9450]]) read the *allcases* row "2qt(b) 4c2e", which is 4a2 2e. Zagros answered "I think a and b might be flipped" and "Should be 60%" ([[D9451]], [[D9452]]), which is right: with one optimal at random, the 4b2 2e path is 2qt on {= E['claims']['C41']['evidence'].split(' is 2qt ')[1].split(' ')[0] =} of states, 4a2 2e on {= E['claims']['C41']['evidence'].split('4a2 2e: ')[1].split(',')[0] =}.

**Aedan Bryant's *HTR Subset Stats*** (1,000 states per subset): the mean optimal and the mean NISS HTR are within 0.06 of mine on {= E['d15_rows'] - len(E['d15_bad']) =} of its {= E['d15_rows'] =} rows. Of the others, four are rows the sheet carries with the numbers of another row, a copy slip. Lewis Isom spotted the 5qt 2C one in 2024 ("5qt 2c0e apparently has a case where NISS HTR only takes 6 moves, which is obviously impossible for any 5q case", [[T4102]]), and Cale agreed ("the impossible 6 move HTRs do seem like a mistake though", [[T4106]]):

| Sheet row | Has the numbers of |
|---|---|
| 4qt 4E | 4qt 2E |
| 4qt 4C2E | 4qt 4C |
| 5qt 2C | 4qt 4C4E |
| 5qt 4C | 5qt 2C8E |

The two fake-HTR rows are off by {= f2(E['d15_bad']['3qt Fake HTR'][1]) =} (0c3 0e) and {= f2(E['d15_bad']['4qt Fake HTR'][1]) =} (0c4 0e) in the mean optimal: the sheet's states were built around one trigger, as Aedan Bryant said when posting it: "might not be perfect because I just did 25 random move HTR scramble + trigger + 25 random move HTR scramble for all of the scrambles" ([[T615]]). For these two that covers only part of the subset. The remaining two differ by at most {= f2(max(max(v[1], v[2]) for k, v in E['d15_bad'].items() if k in ('3qt 4C4E', '5qt 2C2E'))) =}. Its "Linear HTR" is the normal side only, not the better of the two: on 4b2 2e the sheet has {= E['d15_4b2']['doc'] =}, the normal side {= E['d15_4b2']['normal'] =}, the better side {= E['d15_4b2']['best'] =}. Its "No E Difference" column already said that solving the slice costs well under a move for most subsets.

**Levi Gibson's *Extra Quarter-Turn Stats*.** Its "% with extra qts" is *every leave-slice optimal uses more qts than the corners need* ("The percentages are for if the dr CAN be solved optimally without extra qts", [[D8503]]). On that reading it agrees with my sample on every comparable row within sampling error (its 0c0 0e row counts only the states already in HTR, half of 0c0 0e; the other half is U D' times HTR).

**rodneykinney's *DR Finish Move Counts*** (10,000 solutions). rodneykinney's summary "2 qt or less is 17%, but 3 qt or less is 45%" ([[T274]]) is right: exactly {= pc(DOC9('P(corner QTs <= 2)', 'ours')) =} and {= pc(float(DOC9('P(corner QTs <= 2)', 'ours')) + float(DOC9('P(corner QTs = 3)', 'ours'))) =} over the 40,320 corner arrangements. The 4qt and 5qt shares are further off, more than its sample size explains:

| Corner qts | Sheet | Exact |
|---|---|---|
| 4 | {= pc(DOC9('P(corner QTs = 4)', 'doc9')) =} | {= pc(DOC9('P(corner QTs = 4)', 'ours')) =} |
| 5 | {= pc(DOC9('P(corner QTs = 5)', 'doc9')) =} | {= pc(DOC9('P(corner QTs = 5)', 'ours')) =} |

So its DRs probably weren't uniform DR states; the sheet doesn't say how they were made. Its extra-qt columns use one optimal per state and fall between my fewest-qt and most-qt readings.

**Joba's and DougCube's exact tables** are reproduced exactly: the optimal distribution of every subset ({= E['cells473'] =} cells of subset and length), the shortest DR-to-HTR length per subset, and the 663,552 HTR states with mean 10.13432557.
