Scramble: `R' U' F L2 B2 U2 B2 F2 D R2 U F2 D' L2 U' L U2 F' L' B2 D B' R2 D' L R' U' F`

Skeleton: `D2 L D' L2 B' U F' R F2 L' U' D B' L2 F' R2 B' U D' F` (20), leaves a corner 5-cycle: DBL → UBL → UBR → UFL → DFR → DBL

**Best first comm, then the best second, 8-movers only**: 30 in all, the first comm is an 8-2 (2 first comms tie for the best; this is the one whose second comm is best).

```
D2 L D' L2 B' U F' R F2 L' U' D B' L2 F' R2 B' U D' * F
* = D' B' D F2 D' B D F2 // (8-2/26)
D2 L D' L2 B' U F' R F2 L' U' D B' L2 F' R2 B' U D2 B' ^ D F2 D' B D F'
^ = B U B' D' B U' B' D // (8-4/30)
Solution: D2 L D' L2 B' U F' R F2 L' U' D B' L2 F' R2 B' U2 D2 B' D' B U' B' D2 F2 D' B D F' (30)
```

**The same rule with every 3c alg of up to 10 moves**: 32 in all, the first comm is now a 10-5 (3 first comms tie for the best; this is the one whose second comm is best), one move better than the 8-2, and the second comes out worse.

```
D2 L D' * L2 B' U F' R F2 L' U' D B' L2 F' R2 B' U D' F ^
* = D L' D' L F L' D L D' F' // (10-5/25)
^ = F' U B' D2 B U' B' D2 F B // (10-3/32)
Solution: D L F L' D L D' F' L2 B' U F' R F2 L' U' D B' L2 F' R2 B' U2 D' B' D2 B U' B' D2 F B (32)
```
