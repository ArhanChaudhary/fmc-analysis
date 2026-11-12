```
R' U' F L2 D' R2 F2 U R2 D' F2 R2 F2 R2 D L' F' L R' D U R F' D' L R' U' F   // scramble
R2 U2 D R' U B' L' U' F2 D2 F2 R2 L B2 D' B' R2 B' R2 L2                     // skeleton (20)
```

It leaves a corner 3-cycle: DFL → UBL → UFL → DFL.

**With 8-movers**: nothing. At none of the 21 spots does the case have an 8-move alg.

**Best with algs of up to 10 moves**: 28 in all, a 10-mover.

```
R2 U2 D R' U B' L' U' F2 D2 F2 R2 L B2 D' B' R2 * B' R2 L2
* = R B R' D2 R B' R' B D2 B' // (10-2/28)
Solution: R2 U2 D R' U B' L' U' F2 D2 F2 R2 L B2 D' B' R' B R' D2 R B' R' B D2 B2 R2 L2 (28)
```

Shortest alg for the case at each spot, from before the first move to after the last: 9, more than 10, more than 10, more than 10, more than 10, 10, 10, 9, 9, more than 10, more than 10, 9, 9, 9, more than 10, more than 10, more than 10, 9, 9, 9, 9.
