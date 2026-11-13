Nobody searches every pair of comms by hand. You find the best first comm, maybe write down a few more, and then look for the second comm in each. Insertion Finder's *greedy* setting is the same idea, in its own words: "Let's say when searching insertions for each step, the minimum moves of all skeletons is M. IF will keep all skeletons whose moves equal or less than M + N moves. 0 means always best first (human mode?)." So two questions: how good is the best first comm, and what do you lose by following only the best ones?

**The best first comm of a 5c, 8-movers, random skeletons ({= f"{G('5c', 'n', n=16):,}" =} per length; {= f"{G('5c', 'n'):,}" =} at 20 moves), next to the best comm of a 3c of the same length.**

{{greedy_first}}

- **The first comm of a 5c is much better than the comm of a 3c**: {= CELL('greedy_first', '20', '5c: best first comm, mean added') =} against {= CELL('greedy_first', '20', '3c: best comm, mean added') =} at 20 moves. You get five cycles to choose from at every spot (Not officially a David, [[N139]]: "And correct me if I’m wrong but for the first 5c insertion you have 5x more options than for the second"; Zagros, [[N3688]]: "there are 5 possible cycles, not 1").
- Ben ([[N5538]]): "you'll probably have at least an 8-3 or 8-4 for the first one". The best first comm on 5c skeletons:

  | Skeleton | 8-3 or better | 8-4 or better |
  |---|---:|---:|
  | 16 moves | {= CELL('greedy_first', '16', '5c: 8-3 or better') =} | {= CELL('greedy_first', '16', '5c: 8-4 or better') =} |
  | 20 moves | {= CELL('greedy_first', '20', '5c: 8-3 or better') =} | {= CELL('greedy_first', '20', '5c: 8-4 or better') =} |

  So you get an 8-3 most of the time, and an 8-4 about one time in {= GONEIN('16', '5c: 8-4 or better') =} on a 16-move skeleton.

**Following only the best first comms: two 8-move comms on random skeletons of 20 moves. *Best first comm only* is the best first comm (all that tie for it) followed by the best second; *within 1 move* also follows the first comms one move worse. *Loses* is the share of skeletons where the result is longer than the best pair. A rule that ends with no second comm after the first comms it follows counts as a loss and is left out of that rule's mean; for the best first comm only, the sixth column says on how many skeletons that happens.**

{{greedy}}

- **Taking the best first comm of a 5c and then the best second gets you {= CELL('greedy', '5c', 'Best first comm only: mean added') =} against {= CELL('greedy', '5c', 'Best pair of comms: mean added') =} for the best pair**, and misses the best pair on {= GLOSS('5c', 0) =} of skeletons. (All first comms that tie for the best are followed up.)
- **Also following up the first comms that are one move worse** brings that down to {= GLOSS('5c', 1) =}, and two moves worse to {= GLOSS('5c', 2) =}.
- This is what kyh ([[N5837]], [[N5838]]) and argonblue ([[N5842]]) ran into: "my pr single wouldve been a 30 if i didnt go look for sub optimal first insertions", "but its a 28"; "i just had to check a suboptimal first insertion (8-2 instead of 8-3) to get any cancellations in the second". The second comm depends on where the first one went, so the best first comm isn't always the one to follow.
- **What people say about the setting.** Ben ([[N5683]], [[N5684]]): "if you set greedy to 0 and only pick regular 3c comms then it basically shows human findable", "the main thing is setting it to greedy 0". And ([[N5688]], [[N5689]]): "greedy 1 is still reasonable if your skeleton is really good but anything higher isn't imo", "like if i have an 8-3 im not checking 8-1s ever". kyh ([[N5836]]): "i think 1 is realistic". I don't measure what's findable. Here's what each setting gives on a 20-move 5c with 8-movers:

  | Setting | Mean added |
  |---|---:|
  | greedy 0 | {= CELL('greedy', '5c', 'Best first comm only: mean added') =} |
  | greedy 1 | {= CELL('greedy', '5c', 'First comms within 1 move: mean added') =} |
  | the best pair | {= CELL('greedy', '5c', 'Best pair of comms: mean added') =} |

  By hand, greedy 1 means: when the best first comm is an 8-4, also follow up the 8-3s.
- **The other two-comm leftovers** are in the same table, with the same pattern: one move of slack on the first comm gets back most of the loss. A twisted 2c2c still loses on {= CELL('greedy', 'twisted 2c2c', 'Within 1 move: loses') =} of skeletons with it and a 3c3c on {= CELL('greedy', '3c3c', 'Within 1 move: loses') =}.

A skeleton where the best first comm is the wrong one to follow:

{{WIT_GREEDY}}

**More algs at greedy 0 can make it worse, but rarely.** bvcuber13 on a 17-move 5c ([[N5819]], [[N5821]]): "IF finds 30 🤮", "wait if i just do pure comms it finds a 29". tave_789 had the reason on the spot ([[N5825]]): "I forget how it works tbh but if 10-5 is the best first insertion it won’t find the optimals with a worse first insertion". Ben on a 14-move one ([[N6705]], [[N6707]]): "by enabling more corner algorithms on insertion finder with greedy 0 the result turns from 25 to 26", "with more obscure algs you can find a 10-4 for the first alg which doesn't give you the nested 8-4".

I see the same thing. I ran {= G10('run') =} random 5c skeletons of 20 moves with every 3c alg of up to 10 moves; on {= G10('n') =} of them the rule (best first comm, then the best second) ends with a solution under both lists. Against 8-movers only, the longer list gives:

| With the longer list | Skeletons |
|---|---:|
| a *longer* result | {= G10('worse') =} |
| a shorter result | {= G10('better') =} |

So it's real and uncommon. What the longer list changes more is how often the best first comm is the right one to follow: at cap 10 it misses the best pair on {= GLOSS('5c', 0, L=10) =} of skeletons, against {= GLOSS('5c', 0) =} with 8-movers. Their Insertion Finder runs also had alg sets that aren't 3-cycles, which I don't model.

One of the {= W('greedy10', 'n_cases') =} skeletons where the longer list gives the longer result:

{{WIT_GREEDY10}}
