```
R' U' F L R U2 B2 U2 F2 R U2 L2 F2 D2 R F' U' B2 R' D2 B R U2 F' R' U' F   // scramble
R' B' U' L' F' B' L' B' L2 U' F' L2 D2 L' D L U2 L2 U F2                   // skeleton (20)
```

It leaves a corner 3-cycle: DBR → UBR → DFR → DBR.

**Best with 8-movers**: 28 in all.

```
R' B' U' L' F' B' L' B' L2 U' F' L2 D2 L' D L U2 L2 U F2 *
* = D' F' D B' D' F D B // (8-0/28)
Solution: R' B' U' L' F' B' L' B' L2 U' F' L2 D2 L' D L U2 L2 U F2 D' F' D B' D' F D B (28)
```

**Best with algs of up to 10 moves**: 27 in all, a setup move, an 8-mover and the setup undone.

```
R' B' U' L' F' B' * L' B' L2 U' F' L2 D2 L' D L U2 L2 U F2
* = F B' R2 F' L2 F R2 F' L2 B // (10-3/27)
Solution: R' B' U' L' B2 R2 F' L2 F R2 F' L2 B L' B' L2 U' F' L2 D2 L' D L U2 L2 U F2 (27)
```

The 10-mover is this 8-mover between `B'` and `B`:

```
F R2 F' L2 F R2 F' L2   // the 8-mover inside the 10-mover
```

The same solution is that 8-mover put inside move 6 of the skeleton, the `B'` done in two parts: `B2`, the comm, `B`. No spot between two moves gives that with an 8-mover.
