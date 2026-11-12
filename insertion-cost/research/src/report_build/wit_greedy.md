```
R' U' F B2 L2 B2 U B2 D2 B2 U F2 R2 U' B2 R F U' B' R' U L F' L U' R' U' F   // scramble
F2 U2 L' D' F' R D2 F U B U' F2 R2 L2 D' L F2 U' D' F'                       // skeleton (20)
```

It leaves a corner 5-cycle: DFL → UFR → UBL → UFL → UBR → DFL.

**The best first comm, then the best second**: 33 in all, the first is the only 8-2 in the skeleton.

```
F2 U2 L' D' F' R D2 F U B U' F2 R2 L2 * D' L F2 U' ^ D' F'
* = R D L D' R' D L' D' // (8-2/26)
^ = U2 F' D2 F U2 F' D2 F // (8-1/33)
Solution: F2 U2 L' D' F' R D2 F U B U' F2 R' L2 D L D' R' D L' D2 L F2 U F' D2 F U2 F' D2 F D' F' (33)
```

**The best pair**: 31 in all.

```
F2 U2 L' D' F' R D2 F U B U' F2 R2 L2 D' * L F2 U' D' F'
* = D' R' U' R D R' U R // (8-1/27)
F2 U2 L' D' F' R D2 F U B U' F2 R2 L2 D2 R' U' R D R' U ^ R L F2 U' D' F'
^ = U' R2 U L2 U' R2 U L2 // (8-4/31)
Solution: F2 U2 L' D' F' R D2 F U B U' F2 R2 L2 D2 R' U' R D R U L2 U' R2 U R L' F2 U' D' F' (31)
```
