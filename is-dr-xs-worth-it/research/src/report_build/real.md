The same 500 random-state scrambles as the tally on the first study's examples page.

- **Normal DRs**: every EO-first DR of 12 moves or less (cubelib-cli, NISS allowed), each finished optimally. This is the first study's run.
- **DR-xs**: every DR-1s of 8 moves or less and every DR-2s 8fe of 9 or less that starts from a slice-EO skip or a one-move slice EO, on normal or on inverse, and then keeps that axis's EO. That is the tutorial's route, taken exhaustively. Also every DR-2s 8fe of 9 or less after a normal EO of 4 moves or fewer (the wrong-colour DR, and the DR that would end in `U R L`).
- **Finishes**: as in section 5, the best of the method's form, written out as a full solution and replayed on the scramble: {= RL('n1s', f='{:,}') =} DR-1s and {= RL('n8', f='{:,}') =} DR-2s 8fe solutions, all correct. For the 8fe here the setup is searched up to 3 moves from either end, which finds the best for {= EIGHT3('same') =} of the random sample and is {= EIGHT3('avg') =} moves off on average.

As in the first study, every finish is the answer key, not what you find in an hour, and nobody finishes this many. Read the counts as the size of the haystack and the last column of 7.2 as how good each straw is.

### 7.1 What is there

{{real_there}}

- **Nine scrambles in ten have a DR-1s of 8 or less** from a skip or a one-move slice EO, and there are {= TH('a DR-1s of 8 or less from a skip or a one-move slice EO', 1) =} of them on average, more than there are normal DRs of 10 or less.
- **Half have one of 7 or less** ({= TH('a DR-1s of 7 or less from a skip or a one-move slice EO') =}), and a 6 is there on {= TH('a DR-1s of 6 or less from a skip or a one-move slice EO') =}. tseitsei89's "usually 8, occasionally 7" was about what one finds by hand; this is what exists.
- Skips alone carry most of it; one-move slice EOs add about a quarter.

### 7.2 What each one is worth

For each kind of thing you could finish: how often its solution is as short as the best solution any normal DR of 12 or less gives on that scramble.

{{real_yield}}

The table is sorted, so it is also the order to finish things in. So a DR-1s of 7 is worth about what a 9-move DR is, a DR-1s of 8 is worth {= YX('1s8', 'dr11') =} eleven-move DRs and about {= f2(float(YX('1s8', 'dr10'))) =} of a 10-move DR, and a DR-2s 8fe of 9 is a little better than a 10-move DR. The exchange rate of section 5 said N + 2.4 for a DR-1s; on real scrambles it comes out nearer N + 2, because the slice often cancels into the move before it (the route and the finish overlap by {= RL('cancel_1s') =} moves on average).

### 7.3 What it does to the result

Over the {= RL('H') =} scrambles that have a normal DR of 10 or less (the first study's base), the best solution when you finish:

{{real_result}}

- On top of every normal DR of 10 or less, the DR-1s of 7 or less are {= POLN(1, 0) =} more things to finish per scramble and take the average from {= POL(0) =} to {= POL(1) =}. Those of 8 are {= POLN(2, 1) =} more for another {= POLD(1, 2) =}. The 11-move DRs are {= POLN(4, 0) =} more for {= POLD(0, 4) =}.
- Once every 11-mover is finished, DR-xs adds {= POLD(4, 5) =}; once every 12-mover is, {= POLD(6, 7) =}. DR-xs does not find a different class of solution. It finds the same quality with fewer and shorter things to look at.

Scramble by scramble, over all 500:

{{real_head}}

### 7.4 Do real DR-xs finish like random ones?

{{real_candidates}}

Close to it. The ones reached in few moves finish slightly worse than a random one, by a tenth of a move or two. The 8fe column on the scrambles is the 3-move setup search, so it reads a little high.

### 7.5 Time

What these checks cost in an attempt is not something the tables can say. What people wrote: orienting on the four slice edges "takes like 2 seconds" (tseitsei89, [[T11045]]); there are 18 slices to look at, 9 per side; "finding all the non-EO dr-fe's in like 5-10 mins" (trangium, [[T10541]]); a normal EO "takes 15 to 30 seconds" to check (Dunni, [[D16760]]). A slice-EO skip is seen directly, but a DR-1s from it still has to be found the way a DR is found from an EO, and then finished with a method fewer people have practised.
