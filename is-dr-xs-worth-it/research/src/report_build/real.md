The same 500 random-state scrambles as the tally on the first study's examples page.

- **Normal DRs**: every DR of 12 moves or less that goes through an EO of 5 moves or less (cubelib-cli, NISS allowed; it lists no longer EOs), each finished optimally. Same run as the first study.
- **DR-xs**: every DR-1s of 8 moves or less and every DR-2s 8fe of 9 or less that starts from a slice-EO skip or a one-move slice EO, on normal or on inverse, and then keeps that axis's EO. That's the plain version of the tutorial's route (no EO-changing triggers, no NISS inside the route), taken exhaustively, so the counts are a floor on what's there. Plus every DR-2s 8fe of 9 or less after a normal EO of 4 moves or fewer (the wrong-colour DR, and the DR that would end in `U R L`).
- **Finishes**: as in section 5, the best of the method's form, written out as a full solution and replayed on the scramble: {= RL('n1s', f='{:,}') =} DR-1s and {= RL('n8', f='{:,}') =} DR-2s 8fe solutions, all correct. For the 8fe here I search setups up to 3 moves from either end, which finds the best for {= EIGHT3('same') =} of the random sample and is {= EIGHT3('avg') =} moves off on average.

Like in the first study, every finish is the answer key, **computer only**, not what you find in an hour, and nobody finishes this many. Read the counts as the size of the haystack and the last column of 7.2 as how good each straw is.

### 7.1 What is there

{{real_there}}

- **Nine scrambles in ten have a DR-1s of 8 or less** from a skip or a one-move slice EO, and there are {= TH('a DR-1s of 8 or less from a skip or a one-move slice EO', 1) =} of them on average, nearly as many as there are normal DRs of 10 or less.
- **Nearly half have one of 7 or less** ({= TH('a DR-1s of 7 or less from a skip or a one-move slice EO') =}), and a 6 is there on {= TH('a DR-1s of 6 or less from a skip or a one-move slice EO') =}. tseitsei89's "I can usually find some DR-fe in 8 moves. Occasionally 7." ([[T10809]]) was about what you find by hand; this is what's there by the plain route.
- Skips alone carry most of it; one-move slice EOs add a little under a third.
- **The 8fe rows** are a floor too, and you don't need a skip for one (6.3). There are {= E8START(None, 8) =} DR-2s 8fe of 8 moves or fewer on these scrambles. Where they start:

  | Start | How many |
  |---|---:|
  | a misoriented slice-EO skip | {= E8START('0', 8) =} |
  | a one-move slice EO | {= E8START('1', 8) =} |
  | an EO of 4 moves or less | {= E8START('4', 8) =} |

  Each is counted once, under the first of those three that reaches it, and I didn't take EOs of 5 moves for the 8fe, so the split leans towards the skips.

### 7.2 What each one is worth

For each kind of thing you could finish, how often its solution is as short as the best solution any normal DR of 12 or less gives on that scramble:

{{real_yield}}

The table is sorted by that share. Rows 2 to 4 (a DR-2s 8fe of 8 or less, a normal DR of 9 or less, a DR-1s of 7) are within sampling error of each other. So:

- a DR-1s of 7 is worth about what a normal DR of 9 or less is;
- a DR-1s of 8 is worth {= YX('1s8', 'dr11') =} eleven-move DRs and {= YX2('1s8', 'dr10') =} of a 10-move DR;
- a DR-2s 8fe of 9 comes out a little better than a 10-move DR on these scrambles.

That's kinder to DR-xs than the N + {= EXCH() =} of section 5, because on real scrambles the finish often cancels into the last move of the route (by {= RL('cancel_1s') =} moves on average for a DR-1s).

### 7.3 What it does to the result

Over the {= RL('H') =} scrambles that have a normal DR of 10 or less (the first study's base), the best solution when you finish:

{{real_result}}

- On top of every normal DR of 10 or less:

  | Add | More things to finish per scramble | Average result |
  |---|---:|---|
  | the DR-1s of 7 or less | {= POLN(1, 0) =} | from {= POL(0) =} to {= POL(1) =} |
  | those of 8 | {= POLN(2, 1) =} | another {= POLD(1, 2) =} |
  | the 11-move DRs (instead) | {= POLN(4, 0) =} | {= POLD(0, 4) =} better |
- Once every 11-mover is finished, DR-xs adds {= POLD(4, 5) =}; once every 12-mover is, {= POLD(6, 7) =}. Mostly DR-xs gets the same quality from fewer and shorter things to look at. Now and then it finds better, as the next table shows.

Scramble by scramble, over all 500:

{{real_head}}

### 7.4 Against 5-move EOs

The open question: once you've done the EOs of 4 or less, are slice EOs a better use of the time than more 5-move EOs? tseitsei89's take ([[D19521]]): "For sEO I currently believe skips are better than 5 move EOs but 1 movers might not be."

Counting EOs the way cubelib-cli does (every way to write one, with NISS):

- a scramble has {= EOV('eos4') =} EOs of 4 moves or less and {= EOV('eos5') =} of 5 or less; {= EOV('none4') =} of the 500 have none of 4 or less;
- the DRs of 10 or less that come from EOs of 4 or less are {= EOV('drs10_4') =} per scramble, and the 5-move EOs bring that to {= EOV('drs10_5') =}.

Over the {= RL('eo10', 'H', f='{:,}') =} scrambles that have a DR of 10 or less from an EO of 4 or less:

{{real_eo10}}

And with the DRs of 11 as well ({= RL('eo11', 'H', f='{:,}') =} scrambles):

{{real_eo11}}

- **The 5-move EOs are worth {= EOD('eo10', 0, 4) =}** on the average result at this budget, and they're about {= f'{REAL["eo10"]["policies"][4]["eos"] - REAL["eo10"]["policies"][0]["eos"]:,.0f}' =} more EOs to go through.
- **The slice-EO routes are worth {= EOD('eo10', 0, 2) =}** from the DR-1s of 8 or less ({= EOD('eo10', 0, 1) =} from those of 7 or less alone), and what you look through to get them is the slice-EO skips ({= SKIP('both', 'avg') =} per scramble on average over both sides) and the one-move slice EOs. No normal EO is added.
- **They combine**: both together give {= EOP('eo10', 5) =}, {= EOD('eo10', 0, 5) =} better than the start. That's less than the two gains added, because they often get to the same length. Neither replaces the other.
- **Per thing finished the 5-movers do better**: their gain comes from {= f'{REAL["eo10"]["policies"][4]["n"] - REAL["eo10"]["policies"][0]["n"]:,.0f}' =} more DRs to finish, the slice-EO gain from {= f'{REAL["eo10"]["policies"][2]["n"] - REAL["eo10"]["policies"][0]["n"]:,.0f}' =} more DR-1s. The slice EOs win on what you have to look through to get there.

This fits tseitsei89's order, sub-5 EOs first, then the slice-EO skips, then the 5-movers ([[T11014]]), on one condition: a skip and the DR-1s behind it have to be quick to find. The slice-EO routes give about half of what all the 5-move EOs give, for far fewer starts. What that costs in minutes is the part these tables can't tell you, and it's where the doubts were: zakimoshi's "isn't actually a very cost effective strategy time wise" ([[T11306]]), JTuu's "if it's even close, I feel like 5-move eos win for time management reasons" ([[D19528]]).

### 7.5 Do real DR-xs finish like random ones?

{{real_candidates}}

Close to it. A DR-1s you reach in few moves finishes slightly worse than a random one, by a tenth of a move or two. The 8fe ones of 8 and 9 moves finish about like random ones under the same 3-move setup search; the few of 7 moves finish worse.

### 7.6 Time

What these checks cost in an attempt isn't something the tables can tell you. What people wrote:

- "Computing orientation for 4 edges" "takes like 2 seconds" (tseitsei89, [[T11046]], [[T11045]]), and there are 9 slice-and-axis pairs to look at per side;
- "finding all the non-EO dr-fe's in like 5-10 mins" (trangium, [[T10541]]);
- a normal EO "takes 15 to 30 seconds" to check (Dunni, [[D16760]]).

You see a slice-EO skip directly, but you still have to find a DR-1s from it the way you find a DR from an EO, and then finish it with a method fewer people have practised.
