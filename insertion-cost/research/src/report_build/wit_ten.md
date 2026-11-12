```
R' U' F U' D R2 F2 U L2 U B2 U2 R2 D' B' D L2 F U R' D' L U2 R D' R' U' F   // scramble
F D' R' D F' L2 B2 R U F' U2 D' B' R' D2 F L2 U' B2 U                       // skeleton (20)
```

It leaves a corner 3-cycle: UBL → DBR → UFL → UBL.

**Best with 8-movers**: 26 in all.

```
F D' R' D F' L2 B2 R U F' U2 D' B' * R' D2 F L2 U' B2 U
* = B' L' B R2 B' L B R2 // (8-2/26)
Solution: F D' R' D F' L2 B2 R U F' U2 D' B2 L' B R2 B' L B R D2 F L2 U' B2 U (26)
```

**Best with algs up to 10**: 25 in all, a 10-mover; no 9-mover does better than the 8-movers here.

```
F D' * R' D F' L2 B2 R U F' U2 D' B' R' D2 F L2 U' B2 U
* = D F' D' F R F' D F D' R' // (10-5/25)
Solution: D' F R F' D F D' R2 D F' L2 B2 R U F' U2 D' B' R' D2 F L2 U' B2 U (25)
```
