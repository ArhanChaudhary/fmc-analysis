# Corners in 3D: errata

One thing said on the server that the exact search contradicts, with an example you can put on a cube. Everything that checked out, and one statement that depends on how you read it, is in section 11 of [the write-up](./).

## wen's 13-move 4a4 has a 12 inside DR turns

zakimoshi asked "What's the longest corner case that can happen post DR" ([12 May 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1239371389052522647)). wen ([12 May 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1239378220407722004), [12 May 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1239378373243830314)):

> "4a4 could be 13:" R2 U2 F2 U' R2 U R2 U2 F2 U' R2 U R2
>
> "Unless there's a 6 qt solution that's shorter"

Then, after trying the route through 0c3, "Nope, still a 13 mover:" U' F2 U R2 U2 F2 U R2 U2 F2 U' F2 U2 ([12 May 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1239379452383858738)). zakimoshi asked whether a half turn somewhere would get rid of the 3 in front, and the answer was "yeah it doesn't help because to make a qt of progress there you need to set it up to that shape and it's 3 moves no matter what" ([12 May 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1239380322391425087)).

A full search of the corners in DR turns (all eight corners, U, D and the six half turns, 40,320 placements) says that case is 12, with a 4-qt solution:

```
R2 U' R2 U F2 U2 R2 U' R2 U F2 U2 R2     // the case: 4 bad corners, 4 qt
U R2 U R2 U2 F2 U F2 U2 R2 U R2        // 12 moves, only U, R2 and F2
```

Both of wen's 13-move sequences do solve it, and so does torchlight's 11-mover with off-axis turns ([12 May 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1239391808585203763)).

**The server already had the right picture ten months later.** beef beans's sheet [*Corner Solution Length x DR Finish length*](https://docs.google.com/spreadsheets/d/14rZI1Nf84Og1jS8dN1MfT0sYhvdIWu9gPXkHDs1iVU4) ([4 Mar 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1346495904924045354)) stops at 12 for the subsets with 4 bad corners and goes to 13 only for 2c5, on a sample and without solutions that spend extra quarter turns. Zagros read it that way the same day: "No, 13 is only present in 5qt categories, so any extra qt solution would be at least 13 moves anyway" ([4 Mar 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1346550806052343849)).

The full search agrees with both. The longest corner solution in DR turns is 13 moves, all 256 placements that need it are 2c5 (2 or 6 bad corners, 5 qt), and no case with 4 bad corners needs more than 12. One of the 13s:

```
U L2 U' R2 U2 F2 U' F2 U2 R2 U' R2 U'     // a 2c5
U R2 U R2 U2 F2 U F2 U2 R2 U L2 U'     // 13 moves, and nothing shorter in DR turns
```
