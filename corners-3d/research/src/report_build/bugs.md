# Corners in 3D: errata

One thing said on the server that the exact search contradicts, with an example you can put on a cube. Everything that checked out, and one statement that depends on how you read it, is in section 11 of [the write-up](./).

## wen's 13-move 4a4 has a 12 inside DR turns

zakimoshi asked "What's the longest corner case that can happen post DR" ([[T4553]]). wen ([[T4557]], [[T4558]]):

> "4a4 could be 13:" R2 U2 F2 U' R2 U R2 U2 F2 U' R2 U R2
>
> "Unless there's a 6 qt solution that's shorter"

Then, after trying the route through 0c3, "Nope, still a 13 mover:" U' F2 U R2 U2 F2 U R2 U2 F2 U' F2 U2 ([[T4561]]). zakimoshi asked whether a half turn somewhere would get rid of the 3 in front, and the answer was "yeah it doesn't help because to make a qt of progress there you need to set it up to that shape and it's 3 moves no matter what" ([[T4563]]).

A full search of the corners in DR turns (all eight corners, U, D and the six half turns, {= n(X['eight']['placements']) =} placements) says that case is {= X['eight']['wen_true'] =}, with a 4-qt solution:

```
{= X['eight']['wen_case'] =}     // the case: {= X['eight']['wen_bad'] =} bad corners, {= X['eight']['wen_q'] =} qt
{= X['eight']['wen_sol'] =}        // {= len(X['eight']['wen_sol'].split()) =} moves, only U, R2 and F2
```

Both of wen's 13-move sequences do solve it, and so does torchlight's 11-mover with off-axis turns ([[T4565]]).

**The server already had the right picture ten months later.** beef beans's sheet [*Corner Solution Length x DR Finish length*](https://docs.google.com/spreadsheets/d/14rZI1Nf84Og1jS8dN1MfT0sYhvdIWu9gPXkHDs1iVU4) ([[T6599]]) stops at 12 for the subsets with 4 bad corners and goes to 13 only for 2c5, on a sample and without solutions that spend extra quarter turns. Zagros read it that way the same day: "No, 13 is only present in 5qt categories, so any extra qt solution would be at least 13 moves anyway" ([[T6627]]).

The full search agrees with both. The longest corner solution in DR turns is {= X['eight']['max_solved'] =} moves, all {= X['eight']['antipodes'] =} placements that need it are 2c5 (2 or 6 bad corners, 5 qt), and no case with 4 bad corners needs more than {= max(v for k, v in X['eight']['longest'].items() if k.startswith('4 bad')) =}. One of the 13s:

```
{= X['eight']['thirteen_scramble'] =}     // a 2c5
{= X['eight']['thirteen_sol'] =}     // 13 moves, and nothing shorter in DR turns
```
