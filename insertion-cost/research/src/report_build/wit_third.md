Scramble: `R' U' F R2 D F2 U2 L2 U F2 U' B2 U2 B2 L' F R2 D' R' B2 L' F D2 R' U' F`

Skeleton: `D' R2 U2 L U2 D' R' F2 L U L U' B U' R U2 R2 U2 D2 L2` (20), leaves a corner 3-cycle: UFL → DFR → UFR → UFL

**The best 8-mover insertion**: 25 in all, the only 8-3 in the skeleton, after move 4.

```
D' R2 U2 L * U2 D' R' F2 L U L U' B U' R U2 R2 U2 D2 L2
* = L U' L' D' L U L' D // (8-3/25)
Solution: D' R2 U2 L2 U' L' D' L U L' U2 R' F2 L U L U' B U' R U2 R2 U2 D2 L2 (25)
```

Counting spots from 0 (before the first move), the 8-3 is at spot 4. Every other spot from the start (0, 2, 4, and so on) passes it. Every third spot from the start (0, 3, 6, and so on, and the end) does not, and finds nothing better than an 8-1. Of the three ways to take every third spot, only the one that starts at spot 1 passes spot 4.
