```
R' U' F B' U2 B2 L2 F U2 F L2 U2 L2 R B2 F L D' B' U B L2 B' R' U' F   // scramble
L' U' D B L' U' R D L D' R' L D' B2 U' B2 U2 B D' B'                   // skeleton (20)
```

It leaves a corner 3-cycle: DFR → UBR → UFR → DFR.

**The best 8-mover insertion**: 25 in all, the only 8-3 in the skeleton, after move 10.

```
L' U' D B L' U' R D L D' * R' L D' B2 U' B2 U2 B D' B'
* = D' L U' L' D L U L' // (8-3/25)
Solution: L' U' D B L' U' R D L D2 L U' L' D L U R' D' B2 U' B2 U2 B D' B' (25)
```

Counting spots from 0. Checking every other spot from the start, spot 8 is the first whose case has no alg shorter than 10 moves. One of them:

```
U' R' B2 R F R' B2 R F' U   // a 10-mover for spot 8
```

Two spots on, at spot 10, is the 8-3. Going three on instead lands on spot 11, and the walk (spots 0, 2, 4, 6, 8, 11, 13, 15, 17, 19, 20) finds nothing better than an 8-1.
