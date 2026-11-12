```
R' U' F R U2 F2 D2 R' U2 F2 R' F2 L2 R F2 R U R F' L2 B U2 F' L F' R' U' F   // scramble
F2 D2 B2 U' D2 L2 F2 L' D R' B' R2 F U' F' B U2 B' L D                       // skeleton (20)
```

It leaves a corner 3-cycle: DBR → UBR → DFR → DBR.

**The best 8-mover insertion**: 25 in all, the only 8-3 in the skeleton, after move 16.

```
F2 D2 B2 U' D2 L2 F2 L' D R' B' R2 F U' F' B * U2 B' L D
* = F D F' U F D' F' U' // (8-3/25)
Solution: F2 D2 B2 U' D2 L2 F2 L' D R' B' R2 F U' B D F' U F D' F' U B' L D (25)
```

Counting spots from 0 (before the first move), the 8-3 is at spot 16. Checking the odd spots (1, 3, 5, 7, 9, 11, 13, 15, 17, 19) and both ends finds nothing better than an 8-1; the even spots would find it. The spot is right after the pair `F' B`.
