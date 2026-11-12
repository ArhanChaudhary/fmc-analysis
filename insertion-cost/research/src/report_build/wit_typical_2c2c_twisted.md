```
R' U' F L B2 L B2 F2 U2 L B2 U2 B2 R' D2 F' R B' U2 F R2 U' R U R' U' F   // scramble
U' R2 F2 D' R' D' B R' U2 B' L' U F L' D2 B D2 R2 B' R2                   // skeleton (20)
```

It leaves two corner swaps, each with a twist: DFL ↔ UFR, DBR ↔ DFR.

**Best with two 8-move comms**: 29 in all.

```
U' R2 F2 D' R' D' B R' U2 B' L' U F L' D2 * B D2 R2 B' R2
* = U' B D' B' U B D B' // (8-3/25)
U' R2 F2 D' R' D' B R' U2 B' L' U F L' U' D2 B D' ^ B' U B D' R2 B' R2
^ = D B U2 B' D' B U2 B' // (8-4/29)
Solution: U' R2 F2 D' R' D' B R' U2 B' L' U F L' U' D2 B2 U2 B' D' B U2 B2 U B D' R2 B' R2 (29)
```
