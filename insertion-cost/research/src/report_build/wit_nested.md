Scramble: `R' U' F B2 R F2 L' B2 R D2 B2 D2 B2 D2 L2 F' U' R' B' L' D' R2 U' R' U' F`

Skeleton: `L' D' R F U' L2 U R2 F U' B D' L D F' D' B D' B2 R2` (20), leaves a corner 5-cycle: DBL → UBL → DBR → DFR → UFL → DBL

**Best with two 8-move comms**: 29 in all, the second inside the first.

```
L' D' R F U' L2 U * R2 F U' B D' L D F' D' B D' B2 R2
* = D' L' D R2 D' L D R2 // (8-2/26)
L' D' R F U' L2 U D' L' ^ D R2 D' L D F U' B D' L D F' D' B D' B2 R2
^ = L U' L' D2 L U L' D2 // (8-5/29)
Solution: L' D' R F U' L2 D' L' D2 L U L' D' R2 D' L D F U' B D' L D F' D' B D' B2 R2 (29)
```

**Best without nesting**: 31 in all.

```
L' D' R F U' L2 ^ U * R2 F U' B D' L D F' D' B D' B2 R2
* = D' L' D R2 D' L D R2 // (8-2/26)
^ = L' D L U L' D' L U' // (8-3/31)
Solution: L' D' R F U' L D L U L' D' L D' L' D R2 D' L D F U' B D' L D F' D' B D' B2 R2 (31)
```
