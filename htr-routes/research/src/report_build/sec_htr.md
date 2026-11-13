## 6. Shortest HTR against the optimal

**Linear against NISS.** The shortest HTR per subset: with NISS (moves on both sides counted), linear on the better side, and on the normal side alone (what Aedan Bryant's sheet calls linear), and how often NISS is shorter. Sampled, {= n(25000) =} per subset × edges:

{{htr_lengths}}

So, for rodneykinney's question ([[T624]]):

- NISS saves nothing on about half of all DRs, one move on a third, and two or more on {= pc(Q3('all', 'niss_shorter_by_2plus')) =}.
- On 0c3 and 0c4 (fake HTR corners) it saves two or more on {= pc(Q3('0c3', 'niss_shorter_by_2plus')) =} and {= pc(Q3('0c4', 'niss_shorter_by_2plus')) =}.
- The two linear sides tie on {= pc(Q3('all', 'normal_eq_inverse')) =} of DRs and differ by two or more on {= pc(Q3('all', 'normal_inverse_differ_by_2plus')) =}.

**Which HTR the optimal uses.** For each DR, the shortest HTR among all readings of all its optimal finishes, against the DR's shortest NISS HTR (sampled, 25,000 per subset × edges, edges pooled by size; optimal finishes, NISS readings). Each row is a subset: the first four columns split its DRs by how much longer that HTR is than the shortest, then the 9-move columns and the mean number of moves after HTR:

{{htr_vs_opt}}

Some optimal goes through a shortest HTR on only a third of DRs. On the other two thirds you have to find an HTR at least a move longer than the shortest to get the optimal, and on {= pc(float(Q3('all', 'opt_htr_plus2')) + float(Q3('all', 'opt_htr_plus3more'))) =} at least two longer. That's why the checklists need budget 2 (section 4). On 0c3 a shortest HTR is used most often ({= pc(Q3('0c3', 'opt_uses_shortest_niss')) =}); on 2c4 and 4b5 about as often as on 4b2. *Post-HTR moves* is the rest of that optimal: {= f2(Q3('all', 'mean_post_htr_longest_in_an_optimal')) =} moves on average, more on low-qt subsets, as tseitsei89 described ([[T10862]]).

**Nine-move HTRs.** On {= pc(Q3('all', 'every_opt_htr_ge9')) =} of all DRs every optimal finish needs an HTR of 9 moves or more in every reading. On {= pc(float(Q3('all', 'every_opt_htr_ge9')) - float(Q3('all', 'niss_htr_ge9'))) =} of DRs that's the case even though the DR has an HTR of 8 or less. By the length L of a DR's shortest NISS HTR, the share of DRs where some optimal uses an HTR of exactly L moves (all DRs, sampled; the rows cover {= pc(E['bylen_cov']) =} of DRs, the rest having a shortest NISS HTR of {= ', '.join(E['bylen_out']) =} or 0 to 2):

{{htr_by_length}}

The chance that the shortest HTRs carry an optimal is about a third whatever their length, 6 to 9 alike. What a single 9-move HTR is worth once you've written many is a different question, and this doesn't measure it (there are many more 9-move HTRs than 6-move ones). An example where every optimal needs an HTR of 9 or more, replayed:

```
{= WIT('W05', 'scramble') =} // 2c3 2e, {= WIT('W05', 'optimal') =} optimal
```

The shortest HTR in any reading of any of its {= WIT('W05', 'n_optimal_finishes') =} optimal finishes is {= WIT('W05', 'shortest_htr_in_any_reading_of_any_optimal') =} moves.

## 7. Extra quarter turns, and the last DR move

**Extra quarter turns.** The share of DRs where every optimal uses more quarter turns than the corner subset needs, where some optimal does, and where every leave-slice optimal does (the *Extra Quarter-Turn Stats* reading). Sampled, 25,000 per subset × edges, edges pooled by size:

{{extra_qt}}

The three readings are far apart, and the numbers quoted on the server fit different ones.

- rodneykinney: "57% of the time, the optimal solution uses 4QT for a 2QT corner case" ([[T539]]). Radek B asked which reading ("Did you consider all optimals or just one that you had generated?", [[T548]]); there's no answer in the export (rodneykinney moved on to a thread, [[T552]]).
- Lichi Fang: "over 60% the optimal solution for htr subset 2qt(a) 4c4e … use 4qt rather than 2qt" ([[D2306]]), read off the first optimal nissy gave ("these are just the first solution nissy gave for optimal", Aedan Bryant, [[D2310]]).

Each reading on the cases they were talking about:

| Reading | 4a2 and 4b2: 4qt or more | 4b2 4e: 4qt |
|---|---|---|
| every optimal | {= E['claims']['C01']['evidence'].split('every optimal uses 4+ qt ')[1].split(';')[0] =} | {= E['claims']['C02']['evidence'].split('every optimal ')[1].split(';')[0] =} |
| some optimal | {= E['claims']['C01']['evidence'].split('some optimal does ')[1].split(';')[0] =} | |
| one optimal picked at random | {= E['claims']['C01']['evidence'].split('one optimal picked at random ')[1].split(' ')[0] =} | {= E['claims']['C02']['evidence'].split('uses 4+ qt ')[1].split(' ')[0] =} |
| one leave-slice optimal at random | {= E['claims']['C01']['evidence'].split('(leave-slice ')[1].split(')')[0] =} | |

The 57% fits a random leave-slice optimal or *every optimal*. Both quotes fit.

On 4b2 4e no optimal uses only 2 qts on {= E['claims']['C02']['evidence'].split('every optimal ')[1].split(';')[0] =} of states, and on those the 2qt route never gives the optimal. In this one no optimal finish follows the 2qt route `4b2 > 4a1 > 0c0` in any reading:

```
{= WIT('W04', 'scramble') =} // 4b2 4e, {= WIT('W04', 'optimal') =} optimal
{= WIT('W04', 'optimal_finish') =} // one of its {= WIT('W04', 'checked_all_optimal_finishes') =} optimal finishes
```

Both optimal finishes, that one and the other, were re-read on the sticker model at every split.

**Half turns before the first qt.** Kai Cui's 2c3 2e stats ([[T5574]]: "baically 85 percent chance that you dont need to check 2 ht before first qt"). Share where some optimal starts its first qt after 0 or 1 half turns:

| | On one of the two sides | On the normal side alone |
|---|---|---|
| 2c3 2e | {= pc(Q4('2c3 2e', 'ht_before_first_qt_lt2_either_side')) =} | {= pc(Q4('2c3 2e', 'ht_before_first_qt_lt2_normal')) =} |
| All DRs | {= pc(Q4('all', 'ht_before_first_qt_lt2_either_side')) =} | {= pc(Q4('all', 'ht_before_first_qt_lt2_normal')) =} |

**The last DR move.** With the last move either way (the better of X and X·R2; sampled, 25,000 per subset × edges, edges pooled by size; optimal lengths from the exact table):

{{variation}}

X·R2 is one move shorter on a third of DRs and never more than one shorter, in every subset alike; the first study had this exactly (*A third of the time the other DR is one shorter*). Yura Riabov's estimate in 2024 was 1/6 of a move ("so yeah, should be 1/6", [[T4606]]), from "2/3(chance of dr solution ending in 1 of 4 moves) * 1/4(chance of that move being the right one)". Yura called it "very rough" and added "i doubt it will be more than a half move difference with 1 move inverted" ([[T4610]]). The half-move ceiling holds; the 1/6 is half the real gain of {= f3(Q5('all', 'mean_gain')) =}.

Example, replayed. Think of the first line as the end of a DR on U/D whose last move was a quarter turn of R. Turning that move the other way is the same as adding R2 at the end:

```
{= WIT('W06', 'scramble') =} // as written: {= WIT('W06', 'optimal') =} optimal
{= WIT('W06', 'variation_scramble') =} // R2 added: {= WIT('W06', 'variation_optimal') =} optimal
{= WIT('W06', 'variation_finish') =} // its optimal finish
```

For routes the variation changes nothing in kind: every route's share goes up by about the same amount, and no checklist gains a route. It's worth its {= f2(Q5('all', 'mean_gain')) =} moves on every subset, so write both finishes' DRs down, but don't let it change which routes you try.

Aedan Bryant's sheet has a "qt break" column; Yura Riabov explained it as "you know that qt break is dr plus one move that can be inverted, right?" ([[T7157]]). One extra move that can go either way costs {= f2(Q5('all', 'qt_break_minus_opt')) =} moves over the plain optimal on average. That's a little more than the "around 0.5 worse, rather than 1 as you might expect" trangium described ([[T11127]]).
