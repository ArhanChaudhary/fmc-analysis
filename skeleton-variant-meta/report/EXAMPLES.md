# The skeleton/variant meta: example solves

23 Nov 2026

The [skeleton/variant meta](WRITEUP.md), run by a solver on the 34 DRs of [*Advanced DR Bounding Examples*](https://docs.google.com/document/d/1xtvlA3Tg2zkl8H1D98XhLU66gITJ5S-oIPajsn68SOE) and written out the way that doc writes its solves.
Every scramble is a DR on U/D. The goal is 12/13/14 moves from DR to a leave-slice finish for a 2qt/3qt/4qt DR; the 0c0 DRs are solved as 2qt ones, with goal 12.
The sections are the doc's; its 4b3 DRs fall under 4c3 in the write-up, which counts 4a3 and 4b3 together.

Each example goes through the skeletons in the meta's order and stops after its second finish within goal, or after 10 HTRs, whichever comes first.

## How to read an example

```
Skeleton starting with L2 U has FD corners, L=7, 6 spare moves.

- L2 U
    - After R2 B2, 1qt edges will be FH (bad) and RH (good), fr=1: +0+1+0(+5)
        - R2 B2 U B2 U // no good

Check inverse. Skeleton starting with (F2 U') has RD corners.
```

- **Skeleton line.** Skeletons come shortest first. A skeleton is named by how it starts (its moves up to 2qt; a 2qt skeleton by its setup), with the corners it leaves at NISS@1qt, its length L and the spare moves G−L.
- **Check inverse.** The skeleton the inverse scramble reads the same solutions on, with the same L. Moves in parentheses are on the inverse. Normal always goes first.
- **Approach to 2qt** (first-level bullet): the moves up to 2qt, with P ≤ 1. Approaches with no extra move come first. A 2qt skeleton has no approach, so its variants are the first level.
- **Variant line.** `After R2 B2` is the setup. The 1qt edges are the F and R edge cases at NISS@1qt as in [*Advanced DR Bounding*](https://docs.google.com/document/d/13F8HonrKJyHjU9EwfiHDRyY4X77vPriYeaVSrh5guq0), each with whether that slice is bad for these corners, and `fr=1` when the F/R parity is odd. Then the extra moves `+P+S+T(+N)`, or `+S+T(+N)` on a 2qt skeleton, where N is the corner-case-aware bound.
- **Moves.** Under a variant, the moves from the setup on (put the approach in front for the whole solution). A finish within goal is written out with its length; anything else stops at HTR with `// no good`. Variants are in the meta's order: fewest P+S+T first, then (P, S, T, N).
- **A variant line with no moves under it.** No variant of that approach (on a 2qt skeleton: of that skeleton) passes the meta, and the line is the closest one, to show why. `left to the inverse` (or `the normal scramble`) means it is only dropped because it comes earlier on the other side (step 4).
- **Last line.** Why the example stops, what was found, and the DR's optimal to a leave-slice finish.

Left out, compared with the doc's own solves: fixable/unfixable, locked and reflected slices, the name of the insertion (a variant is given by its setup and its moves instead), cs parity, and a NISS in the middle of a skeleton.

## The examples at a glance

One row per example: what the meta finds before it stops, and how many HTRs it takes to reach its first finish within goal when nothing stops it. "Best found" is empty when nothing within goal was found, and the last column is empty when the DR has no finish within goal.

| Example | DR | Goal | DR optimal | HTRs done | Finishes within goal | Best found | HTRs to the first finish within goal |
|---|---|---|---|---|---|---|---|
| [4b2, scramble 1](#4b2-scramble-1) | 4b2 8e | 12 | 12 | 10 | 0 |  | 25 |
| [4b2, scramble 2](#4b2-scramble-2) | 4b2 2e | 12 | 11 | 10 | 1 | 12 | 1 |
| [4b2, scramble 3](#4b2-scramble-3) | 4b2 4e | 12 | 13 | 10 | 0 |  |  |
| [4b2, scramble 4](#4b2-scramble-4) | 4b2 0e | 12 | 13 | 10 | 0 |  |  |
| [4b2, scramble 5](#4b2-scramble-5) | 4b2 6e | 12 | 12 | 8 | 2 | 12 | 3 |
| [4b2, scramble 6](#4b2-scramble-6) | 4b2 6e | 12 | 12 | 10 | 1 | 12 | 1 |
| [4b3, scramble 1](#4b3-scramble-1) | 4b3 6e | 13 | 13 | 10 | 0 |  | 15 |
| [4b3, scramble 2](#4b3-scramble-2) | 4b3 6e | 13 | 14 | 10 | 0 |  |  |
| [4b3, scramble 3](#4b3-scramble-3) | 4b3 4e | 13 | 14 | 10 | 0 |  |  |
| [4b3, scramble 4](#4b3-scramble-4) | 4b3 6e | 13 | 14 | 10 | 0 |  |  |
| [4b3, scramble 5](#4b3-scramble-5) | 4b3 2e | 13 | 13 | 10 | 0 |  | 20 |
| [4b3, scramble 6](#4b3-scramble-6) | 4b3 4e | 13 | 14 | 10 | 0 |  |  |
| [4b3, scramble 7](#4b3-scramble-7) | 4b3 4e | 13 | 14 | 10 | 0 |  |  |
| [4b3, scramble 8](#4b3-scramble-8) | 4b3 4e | 13 | 13 | 10 | 0 |  | 62 |
| [0c0, scramble 1](#0c0-scramble-1) | 0c0 6e | 12 | 13 | 10 | 0 |  |  |
| [0c0, scramble 2](#0c0-scramble-2) | 0c0 2e | 12 | 11 | 10 | 1 | 12 | 9 |
| [2c3, scramble 1](#2c3-scramble-1) | 2c3 2e | 13 | 12 | 10 | 0 |  | 31 |
| [2c3, scramble 2](#2c3-scramble-2) | 2c3 4e | 13 | 13 | 10 | 0 |  | 73 |
| [2c3, scramble 3](#2c3-scramble-3) | 2c3 2e | 13 | 12 | 10 | 1 | 12 | 1 |
| [2c3, scramble 4](#2c3-scramble-4) | 2c3 2e | 13 | 12 | 10 | 1 | 13 | 6 |
| [2c3, scramble 5](#2c3-scramble-5) | 2c3 6e | 13 | 13 | 10 | 0 |  | 170 |
| [2c3, scramble 6](#2c3-scramble-6) | 2c3 6e | 13 | 12 | 10 | 0 |  | 14 |
| [2c3, scramble 7](#2c3-scramble-7) | 2c3 2e | 13 | 14 | 10 | 0 |  |  |
| [2c3, scramble 8](#2c3-scramble-8) | 2c3 6e | 13 | 13 | 10 | 0 |  | never |
| [2c3, scramble 9](#2c3-scramble-9) | 2c3 6e | 13 | 13 | 10 | 0 |  | 19 |
| [2c3, scramble 10](#2c3-scramble-10) | 2c3 4e | 13 | 14 | 10 | 0 |  |  |
| [2c3, scramble 11](#2c3-scramble-11) | 2c3 4e | 13 | 13 | 10 | 0 |  | 59 |
| [2c3, scramble 12](#2c3-scramble-12) | 2c3 6e | 13 | 14 | 10 | 0 |  |  |
| [2c4, scramble 1](#2c4-scramble-1) | 2c4 6e | 14 | 14 | 10 | 0 |  | 158 |
| [2c4, scramble 2](#2c4-scramble-2) | 2c4 6e | 14 | 15 | 10 | 0 |  |  |
| [2c4, scramble 3](#2c4-scramble-3) | 2c4 0e | 14 | 14 | 10 | 0 |  | 17 |
| [2c4, scramble 4](#2c4-scramble-4) | 2c4 2e | 14 | 14 | 10 | 0 |  | 16 |
| [2c4, scramble 5](#2c4-scramble-5) | 2c4 6e | 14 | 14 | 10 | 0 |  | 62 |
| [2c4, scramble 6](#2c4-scramble-6) | 2c4 4e | 14 | 14 | 10 | 0 |  | 41 |

22 of the 34 DRs have a finish within goal. The meta finds one on 6 of them before it stops, and on 3 of those it finds the DR's optimal. With nothing to stop it, it reaches a finish within goal on 21 of the 22, after 1 to 170 HTRs (median 19).

The one it never solves within goal is 2c3, scramble 8: it has 2 HTRs within goal on normal and 2 on inverse, and every one of them has P+S+T of 6 or more. For example `U' R2 B2 D2 F2 B2 R2 D F2 L2 U F2 L2` (13) has a 6-move skeleton and reads (P, S, T, N) = (0, 5, 1, 1).

## 4b2

### 4b2, scramble 1

`R' U' F U F R2 F2 L' D2 L2 U2 B2 L' D2 U2 L F D L2 D2 F' L2 U2 R' U' F`

4b2 8e, goal 12.

Skeleton starting with U2 F2 has HH corners, L=5, 7 spare moves.

- After U2 F2, 1qt edges will be RH (good) and FD (bad): +0+3(+3)
    - U2 F2 D R2 B2 R2 B2 U' // no good
    - U2 F2 U F2 R2 B2 L2 U' // no good
    - U2 F2 D R2 F2 R2 F2 U' // no good
    - U2 F2 U F2 L2 B2 R2 U // no good
- After U2 B2, 1qt edges will be RH (good) and FD (bad): +0+3(+3)
    - U2 B2 U L2 F2 R2 B2 U // no good
    - U2 B2 D F2 R2 F2 R2 U' // no good
    - U2 B2 U L2 B2 R2 F2 U' // no good
    - U2 B2 D F2 L2 F2 L2 U' // no good
- After U2 R2 F2, 1qt edges will be RH (good) and FH (good): +1+3(+0)
    - U2 R2 F2 D' F2 L2 F2 L2 U // no good
    - U2 R2 F2 U' R2 F2 L2 B2 U // no good

Stop: 10 HTRs done, nothing within goal. This DR's optimal is 12.

### 4b2, scramble 2

`R' U' F L2 F U' B2 L' F2 R' U2 F2 R2 D2 B U2 F U2 D2 B' R' U2 R' U' F`

4b2 2e, goal 12.

Skeleton starting with F2 has RV corners, L=6, 6 spare moves.

- After R2 L2 B2, 1qt edges will be RV (good) and FD (bad): +2+0(+3)
    - R2 L2 B2 U' B2 U R2 B2 R2 U2 R2 U2 // 12
- After B2 L2 B2 L2, 1qt edges will be RV (good) and FH (good): +3+0(+0)
    - B2 L2 B2 L2 U R2 U // no good
- After R2 L2 B2, 1qt edges will be RV (good) and FD (bad), fr=1: +2+2(+2)
    - R2 L2 B2 U F2 U2 B2 U' // no good
    - R2 L2 B2 U B2 U2 B2 U // no good

Check inverse. Skeleton starting with (U2 R2) has FD corners.

- After (U2 B2 L2), 1qt edges will be FV (bad) and RH (good): +1+0(+3)
    - (U2 B2 L2 U L2 U) // no good
- After (U2 R2 F2 B2), 1qt edges will be FH (bad) and RH (good): +2+0(+3)
    - (U2 R2 F2 B2 U' F2 U) // no good
- After (U2 B2 L2), 1qt edges will be FV (bad) and RH (good): +1+2(+3)
    - (U2 B2 L2 D R2 L2 B2 U') // no good
- After (F2 R2 B2 U2 B2), 1qt edges will be FV (bad) and RD (good): +3+0(+3)
    - (F2 R2 B2 U2 B2 U R2 U') // no good
- After (B2 L2 F2 U2 F2), 1qt edges will be FV (bad) and RD (good): +3+0(+3)
    - (B2 L2 F2 U2 F2 U B2 U') // no good

Skeleton starting with U R2 U has HH corners, L=7, 5 spare moves.

- U R2 U
    - After R2, 1qt edges will be RH (good) and FH (good): +0+0+3(+0)
        - R2 U F2 R2 F2 R2 U' // no good

Stop: 10 HTRs done, one finish within goal (12). This DR's optimal is 11.

### 4b2, scramble 3

`R' U' F D' F B D2 B2 U' B' L F2 U F2 D2 F2 D2 R2 B2 L2 F2 D R' U' F`

4b2 4e, goal 12.

Skeleton starting with B2 U2 R2 has HH corners, L=6, 6 spare moves.

- After B2 U2 R2, 1qt edges will be RH (good) and FH (good): +0+1(+0)
    - B2 U2 R2 U' F2 R2 U' // no good
    - B2 U2 R2 D' R2 B2 U' // no good
- After U2 R2 U2 B2, 1qt edges will be RH (good) and FH (good): +1+1(+0)
    - U2 R2 U2 B2 U F2 R2 U' // no good
    - U2 R2 U2 B2 D L2 F2 U' // no good
- After F2 U2 B2 R2, 1qt edges will be RH (good) and FV (bad): +1+1(+3)
    - F2 U2 B2 R2 D R2 F2 U' // no good
    - F2 U2 B2 R2 U B2 R2 U // no good
- After B2 U2 B2 L2, 1qt edges will be RV (bad) and FH (good): +1+1(+3)
    - B2 U2 B2 L2 U F2 L2 U' // no good
    - B2 U2 B2 L2 D L2 B2 U // no good
- After F2 U2 L2, 1qt edges will be RH (good) and FH (good): +0+3(+0)
    - F2 U2 L2 U' F2 L2 F2 B2 U' // no good
    - F2 U2 L2 D' R2 F2 R2 L2 U' // no good

Stop: 10 HTRs done, nothing within goal. This DR's optimal is 13, over the goal.

### 4b2, scramble 4

`R' U' F U2 R2 F D R' L' U2 F' L2 U' L2 B2 U' R2 B2 D R2 L2 F D' R' U' F`

4b2 0e, goal 12.

Skeleton starting with F2 has RV corners, L=6, 6 spare moves.

- After F2, 1qt edges will be RD (bad) and FD (bad): +0+3(+5)

Check inverse. Skeleton starting with (U2 R2) has FD corners.

- After (U2 R2), 1qt edges will be FV (bad) and RV (bad): +0+3(+5)

Skeleton starting with B2 U' F2 U has HH corners, L=7, 5 spare moves.

- B2 U' F2 U
    - After R2 B2, 1qt edges will be RH (good) and FV (bad): +0+1+3(+3)
- F2 U' R2 U
    - After R2 F2, 1qt edges will be RH (good) and FV (bad): +0+1+3(+3)
- B2 U' B2 U
    - After L2, 1qt edges will be RH (good) and FD (bad): +0+0+5(+3)
- F2 U' L2 U
    - After R2, 1qt edges will be RH (good) and FD (bad): +0+0+5(+3)
- B2 U' F2 U'
    - After F2 U2 B2, 1qt edges will be RD (bad) and FV (bad), fr=1: +0+2+3(+6)
- F2 U' R2 U'
    - After F2 U2 B2, 1qt edges will be RD (bad) and FV (bad), fr=1: +0+2+3(+6)
- L2 B2 U R2 U'
    - After L2, 1qt edges will be RD (bad) and FD (bad): +1+0+3(+6)
- L2 F2 U B2 U'
    - After R2, 1qt edges will be RD (bad) and FD (bad): +1+0+3(+6)
- R2 B2 U L2 U'
    - After R2, 1qt edges will be RD (bad) and FD (bad): +1+0+3(+6)
- R2 F2 U F2 U'
    - After L2, 1qt edges will be RD (bad) and FD (bad): +1+0+3(+6)

Skeleton starting with U R2 U has RD corners, L=8, 4 spare moves.

- U R2 U
    - After F2 R2 B2 L2 B2, 1qt edges will be RD (good) and FH (good), fr=1: +0+4+0(+3)
- U L2 U
    - After R2 F2, 1qt edges will be RV (bad) and FH (good), fr=1: +0+1+0(+5)
- U R2 U'
    - After L2 U2 L2, 1qt edges will be RV (bad) and FV (bad): +0+2+0(+5)
- U L2 U'
    - After R2 L2 B2 U2 B2, 1qt edges will be RD (good) and FH (good): +0+4+0(+0)
        - R2 L2 B2 U2 B2 U' B2 U' // no good
    - After F2 U2 B2 R2 L2, 1qt edges will be RD (good) and FH (good): +0+4+0(+0)
        - F2 U2 B2 R2 L2 U' F2 U' // no good

Check inverse. Skeleton starting with (L2 U' F2 U) has HH corners.

- (L2 U' F2 U)
    - After (F2 U2 F2 B2), 1qt edges will be RH (good) and FD (bad), fr=1: +0+3+0(+5)
- (R2 U' L2 U)
    - After (B2 U2 F2 B2), 1qt edges will be RH (good) and FD (bad), fr=1: +0+3+0(+5)
- (L2 U' B2 U)
    - After (F2 L2), 1qt edges will be RD (bad) and FD (bad), fr=1: +0+1+0(+6)
- (R2 U' R2 U)
    - After (B2 L2), 1qt edges will be RD (bad) and FD (bad), fr=1: +0+1+0(+6)
- (L2 U' F2 U')
    - After (B2 U2 B2), 1qt edges will be RH (good) and FD (bad): +0+2+0(+3)
- (R2 U' L2 U')
    - After (B2 U2 F2), 1qt edges will be RH (good) and FD (bad): +0+2+0(+3)
- (L2 U' B2 U')
    - After (L2 U2 F2 L2), 1qt edges will be RD (bad) and FD (bad): +0+3+0(+6)
- (R2 U' R2 U')
    - After (R2 U2 B2 L2), 1qt edges will be RD (bad) and FD (bad): +0+3+0(+6)
- (B2 L2 U L2 U')
    - After (R2 B2), 1qt edges will be RD (bad) and FV (bad), fr=1: +1+1+0(+6)
- (B2 R2 U B2 U')
    - After (R2 F2), 1qt edges will be RD (bad) and FV (bad), fr=1: +1+1+0(+6)
- (F2 L2 U R2 U')
    - After (L2 F2), 1qt edges will be RD (bad) and FV (bad), fr=1: +1+1+0(+6)
- (F2 R2 U F2 U')
    - After (L2 B2), 1qt edges will be RD (bad) and FV (bad), fr=1: +1+1+0(+6)
- (B2 L2 U R2 U)
    - After (L2 U2 L2), 1qt edges will be RD (bad) and FD (bad): +1+2+0(+6)
- (B2 R2 U F2 U)
    - After (R2 U2 L2), 1qt edges will be RD (bad) and FD (bad): +1+2+0(+6)
- (F2 L2 U L2 U)
    - After (R2 U2 R2), 1qt edges will be RD (bad) and FD (bad): +1+2+0(+6)
- (F2 R2 U B2 U)
    - After (L2 U2 R2), 1qt edges will be RD (bad) and FD (bad): +1+2+0(+6)

Skeleton starting with B2 U' F2 U' has RD corners, L=8, 4 spare moves.

- B2 U' F2 U'
    - After B2, 1qt edges will be RD (good) and FH (good), fr=1: +0+0+3(+3)
- F2 U' R2 U'
    - After F2, 1qt edges will be RD (good) and FH (good), fr=1: +0+0+3(+3)
- L2 B2 U R2 U
    - After L2, 1qt edges will be RV (bad) and FD (good), fr=1: +1+0+3(+5)
- L2 F2 U B2 U
    - After L2, 1qt edges will be RV (bad) and FD (good), fr=1: +1+0+3(+5)
- R2 B2 U L2 U
    - After R2, 1qt edges will be RV (bad) and FD (good), fr=1: +1+0+3(+5)
- R2 F2 U F2 U
    - After R2, 1qt edges will be RV (bad) and FD (good), fr=1: +1+0+3(+5)

Skeleton starting with (U2 L2 U F2 U') on inverse has HH corners, L=8, 4 spare moves.

- (U2 L2 U F2 U')
    - After (F2 R2), 1qt edges will be RD (bad) and FH (good): +0+1+3(+3)
- (U2 R2 U R2 U')
    - After (F2 L2), 1qt edges will be RD (bad) and FH (good): +0+1+3(+3)
- (L2 U2 L2 U' F2 U')
    - After (L2), 1qt edges will be RD (bad) and FV (bad), fr=1: +1+0+3(+6)
- (L2 U2 R2 U' L2 U')
    - After (R2), 1qt edges will be RD (bad) and FV (bad), fr=1: +1+0+3(+6)
- (R2 U2 L2 U' B2 U')
    - After (R2), 1qt edges will be RD (bad) and FV (bad), fr=1: +1+0+3(+6)
- (R2 U2 R2 U' R2 U')
    - After (L2), 1qt edges will be RD (bad) and FV (bad), fr=1: +1+0+3(+6)
- (U2 B2 L2 U' R2 U)
    - After (B2), 1qt edges will be RV (bad) and FV (bad): +1+0+3(+6)
- (U2 B2 R2 U' B2 U)
    - After (F2), 1qt edges will be RV (bad) and FV (bad): +1+0+3(+6)
- (U2 F2 L2 U' L2 U)
    - After (F2), 1qt edges will be RV (bad) and FV (bad): +1+0+3(+6)
- (U2 F2 R2 U' F2 U)
    - After (B2), 1qt edges will be RV (bad) and FV (bad): +1+0+3(+6)

Skeleton starting with B2 U' L2 U has RV corners, L=9, 3 spare moves.

- B2 U' L2 U
    - After R2 B2 L2, 1qt edges will be RD (bad) and FV (good): +0+3+0(+3)
- B2 U' L2 U'
    - After L2 F2 R2, 1qt edges will be RD (bad) and FH (good): +0+3+0(+3)
- B2 U' R2 U
    - After R2 F2 L2, 1qt edges will be RD (bad) and FV (good): +0+3+0(+3)
- B2 U' R2 U'
    - After L2 B2 R2, 1qt edges will be RD (bad) and FH (good): +0+3+0(+3)
- F2 U' B2 U
    - After L2 B2 R2, 1qt edges will be RD (bad) and FV (good): +0+3+0(+3)
- F2 U' B2 U'
    - After L2 B2 R2, 1qt edges will be RD (bad) and FH (good): +0+3+0(+3)
- F2 U' F2 U
    - After L2 F2 R2, 1qt edges will be RD (bad) and FV (good): +0+3+0(+3)
- F2 U' F2 U'
    - After L2 F2 R2, 1qt edges will be RD (bad) and FH (good): +0+3+0(+3)

Check inverse. Skeleton starting with (U2 L2 U L2 U) has FD corners.

- (U2 L2 U L2 U)
    - After (R2 B2 L2), 1qt edges will be FD (good) and RV (bad): +0+3+0(+3)
- (U2 L2 U L2 U')
    - After (B2 L2 F2), 1qt edges will be FV (bad) and RD (good): +0+3+0(+3)
- (U2 L2 U R2 U)
    - After (R2 F2 L2), 1qt edges will be FD (good) and RV (bad): +0+3+0(+3)
- (U2 L2 U R2 U')
    - After (B2 R2 F2), 1qt edges will be FV (bad) and RD (good): +0+3+0(+3)
- (U2 R2 U B2 U)
    - After (L2 B2 R2), 1qt edges will be FD (good) and RV (bad): +0+3+0(+3)
- (U2 R2 U B2 U')
    - After (F2 L2 B2), 1qt edges will be FV (bad) and RD (good): +0+3+0(+3)
- (U2 R2 U F2 U)
    - After (L2 F2 R2), 1qt edges will be FD (good) and RV (bad): +0+3+0(+3)
- (U2 R2 U F2 U')
    - After (F2 R2 B2), 1qt edges will be FV (bad) and RD (good): +0+3+0(+3)

Skeleton starting with B2 U' F2 U has FV corners, L=9, 3 spare moves.

- B2 U' F2 U
    - After R2, 1qt edges will be FD (bad) and RH (good): +0+0+3(+3)
- F2 U' R2 U
    - After L2, 1qt edges will be FD (bad) and RH (good): +0+0+3(+3)

Skeleton starting with L2 U' F2 U' has RD corners, L=9, 3 spare moves.

- L2 U' F2 U'
    - After F2 R2 L2, 1qt edges will be RH (bad) and FH (good), fr=1: +0+2+0(+5)
- R2 U' L2 U'
    - After F2 R2 L2, 1qt edges will be RH (bad) and FH (good), fr=1: +0+2+0(+5)
- L2 U' B2 U'
    - After F2 B2 L2, 1qt edges will be RV (bad) and FV (bad), fr=1: +0+2+0(+5)
- R2 U' R2 U'
    - After F2 B2 R2, 1qt edges will be RV (bad) and FV (bad), fr=1: +0+2+0(+5)
- L2 U' B2 U
    - After B2 R2 U2 B2, 1qt edges will be RD (good) and FH (good): +0+3+0(+0)
        - B2 R2 U2 B2 U' R2 U' // no good
- R2 U' R2 U
    - After F2 R2 U2 B2, 1qt edges will be RD (good) and FH (good): +0+3+0(+0)
        - F2 R2 U2 B2 U' F2 U' // no good
- L2 U' F2 U
    - After B2 U2 R2 F2, 1qt edges will be RV (bad) and FH (good): +0+3+0(+3)
- R2 U' L2 U
    - After F2 U2 L2 F2, 1qt edges will be RV (bad) and FH (good): +0+3+0(+3)

Check inverse. Skeleton starting with (L2 U' R2 U) has RD corners.

- (L2 U' R2 U)
    - After (R2 F2 B2), 1qt edges will be RD (good) and FV (bad), fr=1: +0+2+0(+5)
- (R2 U' B2 U)
    - After (R2 F2 B2), 1qt edges will be RD (good) and FV (bad), fr=1: +0+2+0(+5)
- (L2 U' L2 U)
    - After (R2 L2 B2), 1qt edges will be RH (bad) and FD (good), fr=1: +0+2+0(+5)
- (R2 U' F2 U)
    - After (R2 L2 F2), 1qt edges will be RH (bad) and FD (good), fr=1: +0+2+0(+5)
- (L2 U' L2 U')
    - After (L2 F2 U2 L2), 1qt edges will be RD (good) and FH (good): +0+3+0(+0)
        - (L2 F2 U2 L2 U F2 U') // no good
- (R2 U' F2 U')
    - After (R2 F2 U2 L2), 1qt edges will be RD (good) and FH (good): +0+3+0(+0)
        - (R2 F2 U2 L2 U R2 U') // no good
- (L2 U' R2 U')
    - After (L2 U2 F2 R2), 1qt edges will be RD (good) and FD (good): +0+3+0(+1)
- (R2 U' B2 U')
    - After (R2 U2 B2 R2), 1qt edges will be RD (good) and FD (good): +0+3+0(+1)

Skeleton starting with (U2 L2 U F2 U') on inverse has RD corners, L=9, 3 spare moves.

- (U2 L2 U F2 U')
    - After (B2), 1qt edges will be RV (bad) and FH (good): +0+0+3(+3)
- (U2 R2 U R2 U')
    - After (F2), 1qt edges will be RV (bad) and FH (good): +0+0+3(+3)

Skeleton starting with U2 B2 U R2 U' has HH corners, L=9, 3 spare moves.

- U2 B2 U R2 U'
    - After L2 F2, 1qt edges will be RV (bad) and FV (bad), fr=1: +0+1+0(+6)
- U2 F2 U B2 U'
    - After R2 F2, 1qt edges will be RV (bad) and FV (bad), fr=1: +0+1+0(+6)
- U2 B2 U L2 U
    - After R2 U2 R2, 1qt edges will be RV (bad) and FH (good): +0+2+0(+3)
- U2 F2 U F2 U
    - After R2 U2 L2, 1qt edges will be RV (bad) and FH (good): +0+2+0(+3)
- U2 B2 U L2 U'
    - After L2 U2 R2 L2, 1qt edges will be RV (bad) and FH (good), fr=1: +0+3+0(+5)
- U2 F2 U F2 U'
    - After R2 U2 R2 L2, 1qt edges will be RV (bad) and FH (good), fr=1: +0+3+0(+5)
- U2 B2 U R2 U
    - After R2 B2 U2 L2, 1qt edges will be RV (bad) and FD (bad): +0+3+0(+6)
- U2 F2 U B2 U
    - After R2 F2 U2 R2, 1qt edges will be RV (bad) and FD (bad): +0+3+0(+6)
- B2 U2 B2 U' R2 U'
    - After L2 F2, 1qt edges will be RH (good) and FV (bad): +1+1+0(+3)
- B2 U2 F2 U' F2 U'
    - After L2 B2, 1qt edges will be RH (good) and FV (bad): +1+1+0(+3)
- F2 U2 B2 U' L2 U'
    - After R2 B2, 1qt edges will be RH (good) and FV (bad): +1+1+0(+3)
- F2 U2 F2 U' B2 U'
    - After R2 F2, 1qt edges will be RH (good) and FV (bad): +1+1+0(+3)
- U2 L2 B2 U' F2 U
    - After B2 R2, 1qt edges will be RD (bad) and FV (bad), fr=1: +1+1+0(+6)
- U2 L2 F2 U' R2 U
    - After B2 L2, 1qt edges will be RD (bad) and FV (bad), fr=1: +1+1+0(+6)
- U2 R2 B2 U' B2 U
    - After F2 L2, 1qt edges will be RD (bad) and FV (bad), fr=1: +1+1+0(+6)
- U2 R2 F2 U' L2 U
    - After F2 R2, 1qt edges will be RD (bad) and FV (bad), fr=1: +1+1+0(+6)

Check inverse. Skeleton starting with (U R2 U') has FV corners.

- (U R2 U')
    - After (F2 L2), 1qt edges will be FD (bad) and RH (good), fr=1: +0+1+0(+2)
        - (F2 L2 U R2 U') // no good
- (U L2 U)
    - After (F2 U2 B2), 1qt edges will be FD (bad) and RD (bad): +0+2+0(+5)
- (U L2 U')
    - After (F2 L2 F2 L2), 1qt edges will be FV (good) and RD (bad), fr=1: +0+3+0(+2)
- (U R2 U)
    - After (R2 U2 F2 L2), 1qt edges will be FD (bad) and RH (good): +0+3+0(+3)

Skeleton starting with U F2 U has DD corners, L=10, 2 spare moves.

- U F2 U
    - After F2 B2 L2, 1qt edges will be FV (good) and RV (good): +0+2+0(+1)
- U B2 U
    - After B2 R2 L2, 1qt edges will be FH (bad) and RD (good): +0+2+0(+3)

Check inverse. Skeleton starting with (B2 U2 L2 U' B2 U) has HH corners.

- (B2 U2 L2 U' B2 U)
    - After (B2 R2 L2), 1qt edges will be RV (bad) and FH (good): +0+2+0(+3)
- (B2 U2 R2 U' R2 U)
    - After (F2 R2 L2), 1qt edges will be RV (bad) and FH (good): +0+2+0(+3)
- (F2 U2 L2 U' R2 U)
    - After (F2 R2 L2), 1qt edges will be RV (bad) and FH (good): +0+2+0(+3)
- (F2 U2 R2 U' B2 U)
    - After (B2 R2 L2), 1qt edges will be RV (bad) and FH (good): +0+2+0(+3)
- (L2 U2 B2 U' L2 U')
    - After (L2 F2 B2), 1qt edges will be RD (bad) and FH (good), fr=1: +0+2+0(+5)
- (L2 U2 B2 U' R2 U')
    - After (R2 L2 B2), 1qt edges will be RH (good) and FD (bad), fr=1: +0+2+0(+5)
- (L2 U2 F2 U' B2 U')
    - After (L2 F2 B2), 1qt edges will be RD (bad) and FH (good), fr=1: +0+2+0(+5)
- (L2 U2 F2 U' F2 U')
    - After (R2 L2 F2), 1qt edges will be RH (good) and FD (bad), fr=1: +0+2+0(+5)
- (R2 U2 B2 U' B2 U')
    - After (L2 F2 B2), 1qt edges will be RD (bad) and FH (good), fr=1: +0+2+0(+5)
- (R2 U2 B2 U' F2 U')
    - After (R2 L2 F2), 1qt edges will be RH (good) and FD (bad), fr=1: +0+2+0(+5)
- (R2 U2 F2 U' L2 U')
    - After (L2 F2 B2), 1qt edges will be RD (bad) and FH (good), fr=1: +0+2+0(+5)
- (R2 U2 F2 U' R2 U')
    - After (R2 L2 B2), 1qt edges will be RH (good) and FD (bad), fr=1: +0+2+0(+5)
- (B2 U2 L2 U' F2 U)
    - After (F2 B2 L2), 1qt edges will be RD (bad) and FD (bad): +0+2+0(+6)
- (B2 U2 R2 U' L2 U)
    - After (F2 B2 L2), 1qt edges will be RD (bad) and FD (bad): +0+2+0(+6)
- (F2 U2 L2 U' L2 U)
    - After (F2 B2 L2), 1qt edges will be RD (bad) and FD (bad): +0+2+0(+6)
- (F2 U2 R2 U' F2 U)
    - After (F2 B2 L2), 1qt edges will be RD (bad) and FD (bad): +0+2+0(+6)

Skeleton starting with B2 U2 L2 U' F2 U' has HH corners, L=10, 2 spare moves.

- B2 U2 L2 U' F2 U'
    - After R2 F2 B2, 1qt edges will be RH (good) and FD (bad): +0+2+0(+3)
- B2 U2 R2 U' L2 U'
    - After L2 F2 B2, 1qt edges will be RH (good) and FD (bad): +0+2+0(+3)
- F2 U2 L2 U' L2 U'
    - After L2 F2 B2, 1qt edges will be RH (good) and FD (bad): +0+2+0(+3)
- F2 U2 R2 U' F2 U'
    - After R2 F2 B2, 1qt edges will be RH (good) and FD (bad): +0+2+0(+3)
- L2 U2 B2 U' L2 U
    - After F2 B2 L2, 1qt edges will be RV (bad) and FH (good), fr=1: +0+2+0(+5)
- L2 U2 B2 U' R2 U
    - After F2 R2 L2, 1qt edges will be RH (good) and FV (bad), fr=1: +0+2+0(+5)
- L2 U2 F2 U' B2 U
    - After F2 B2 R2, 1qt edges will be RV (bad) and FH (good), fr=1: +0+2+0(+5)
- L2 U2 F2 U' F2 U
    - After F2 R2 L2, 1qt edges will be RH (good) and FV (bad), fr=1: +0+2+0(+5)
- R2 U2 B2 U' B2 U
    - After F2 B2 R2, 1qt edges will be RV (bad) and FH (good), fr=1: +0+2+0(+5)
- R2 U2 B2 U' F2 U
    - After F2 R2 L2, 1qt edges will be RH (good) and FV (bad), fr=1: +0+2+0(+5)
- R2 U2 F2 U' L2 U
    - After F2 B2 L2, 1qt edges will be RV (bad) and FH (good), fr=1: +0+2+0(+5)
- R2 U2 F2 U' R2 U
    - After F2 R2 L2, 1qt edges will be RH (good) and FV (bad), fr=1: +0+2+0(+5)
- B2 U2 L2 U' B2 U'
    - After R2 L2 B2, 1qt edges will be RV (bad) and FV (bad): +0+2+0(+6)
- B2 U2 R2 U' R2 U'
    - After R2 L2 B2, 1qt edges will be RV (bad) and FV (bad): +0+2+0(+6)
- F2 U2 L2 U' R2 U'
    - After R2 L2 B2, 1qt edges will be RV (bad) and FV (bad): +0+2+0(+6)
- F2 U2 R2 U' B2 U'
    - After R2 L2 B2, 1qt edges will be RV (bad) and FV (bad): +0+2+0(+6)

Check inverse. Skeleton starting with (U B2 U') has DD corners.

- (U B2 U')
    - After (R2 L2 B2), 1qt edges will be FD (good) and RD (good): +0+2+0(+2)
- (U F2 U')
    - After (R2 F2 B2), 1qt edges will be FV (good) and RH (bad): +0+2+0(+3)

Skeleton starting with L2 U' L2 U' has DD corners, L=11, 1 spare move.

- L2 U' L2 U'
    - After R2 B2, 1qt edges will be FH (bad) and RV (good): +0+1+0(+3)
- R2 U' F2 U'
    - After L2 B2, 1qt edges will be FH (bad) and RV (good): +0+1+0(+3)

Check inverse. Skeleton starting with (B2 U2 L2 U' L2 U) has RD corners.

- (B2 U2 L2 U' L2 U)
    - After (R2 F2), 1qt edges will be RD (good) and FH (good): +0+1+0(+0)
        - (R2 F2 U' L2 U') // no good
- (B2 U2 R2 U' F2 U)
    - After (R2 B2), 1qt edges will be RD (good) and FH (good): +0+1+0(+0)
        - (R2 B2 U' F2 U') // no good
- (F2 U2 L2 U' F2 U)
    - After (R2 B2), 1qt edges will be RD (good) and FH (good): +0+1+0(+0)
        - (R2 B2 U' F2 U') // no good

Stop: 10 HTRs done, nothing within goal. This DR's optimal is 13, over the goal.

### 4b2, scramble 5

`R' U' F D F2 D2 L2 R B2 U2 R D2 L' U2 R2 F2 D' U2 L' F U' L' F R' U' F`

4b2 6e, goal 12.

Skeleton starting with U2 F2 has FV corners, L=7, 5 spare moves.

- After U2 L2 B2, 1qt edges will be FV (good) and RV (good), fr=1: +1+0(+2)
    - U2 L2 B2 D B2 U' // no good
- After L2 B2 U2 L2, 1qt edges will be FV (good) and RH (good): +2+0(+0)
    - L2 B2 U2 L2 D' F2 U // no good
- After B2 U2 L2 B2, 1qt edges will be FV (good) and RV (good): +2+0(+1)
    - B2 U2 L2 B2 D' F2 U F2 L2 D2 R2 L2 // 12
- After U2 F2 R2 L2, 1qt edges will be FH (bad) and RV (good), fr=1: +2+0(+2)
    - U2 F2 R2 L2 D' R2 U' // no good
- After U2 L2 B2, 1qt edges will be FV (good) and RV (good): +1+2(+1)
    - U2 L2 B2 D' F2 U2 F2 U' // no good
    - U2 L2 B2 D' B2 U2 F2 U' // no good
- After U2 L2 B2, 1qt edges will be FV (good) and RV (good), fr=1: +1+2(+2)
    - U2 L2 B2 U F2 B2 L2 U' // no good

Check inverse. Skeleton starting with (U2 B2) has FV corners.

- After (U2 B2), 1qt edges will be FD (bad) and RV (good), fr=1: +0+0(+2)
    - (U2 B2 D L2 U' R2 B2 L2 F2 L2 D2 F2) // 12

Stop: 2 finishes within goal (12, 12), after 8 HTRs. This DR's optimal is 12.

### 4b2, scramble 6

`R' U' F D2 B' U' F2 B' U' L F2 R2 U2 L2 U2 F R2 F2 B R2 U2 R U2 R' U' F`

4b2 6e, goal 12.

Skeleton starting with L2 has RV corners, L=6, 6 spare moves.

- After U2 R2 U2 L2, 1qt edges will be RV (good) and FV (good): +3+0(+1)
    - U2 R2 U2 L2 D L2 U R2 F2 U2 F2 B2 // 12
- After R2 B2 L2 B2, 1qt edges will be RV (good) and FH (good), fr=1: +3+0(+1)
    - R2 B2 L2 B2 D L2 U' // no good
- After R2 U2 R2 L2, 1qt edges will be RV (good) and FV (good), fr=1: +3+0(+2)
    - R2 U2 R2 L2 D L2 U' // no good
- After B2 L2 F2 B2, 1qt edges will be RD (bad) and FV (good), fr=1: +3+0(+2)
    - B2 L2 F2 B2 D L2 U' // no good
- After L2, 1qt edges will be RV (good) and FV (good), fr=1: +0+4(+2)
    - L2 U' F2 U2 R2 F2 L2 U' // no good
    - L2 D' L2 U2 F2 R2 F2 U' // no good
    - L2 U' F2 U2 L2 F2 R2 U' // no good
    - L2 D' L2 U2 B2 R2 B2 U' // no good
- After F2 B2 R2, 1qt edges will be RV (good) and FV (good), fr=1: +2+2(+2)
    - F2 B2 R2 U' R2 F2 B2 U' // no good
- After L2, 1qt edges will be RV (good) and FV (good): +0+5(+1)
    - L2 D B2 U2 F2 U2 B2 L2 U // no good

Stop: 10 HTRs done, one finish within goal (12). This DR's optimal is 12.

## 4b3

### 4b3, scramble 1

`R' U' F D R B2 R B2 R' B2 R' U2 B2 R B2 F L' R B U R' U F2 R' U' F`

4b3 6e, goal 13.

Skeleton starting with U' has RV corners, L=9, 4 spare moves.

- U'
    - After F2, 1qt edges will be RD (bad) and FV (good), fr=1: +0+0+3(+2)

Check inverse. Skeleton starting with (U2 R2 U) has HH corners.

- (U2 R2 U)
    - After (F2 L2 U2 L2), 1qt edges will be RH (good) and FD (bad): +0+1+2(+3)
- (U2 R2 U')
    - After (F2 R2 B2 R2 U2 F2), 1qt edges will be RH (good) and FH (good): +0+3+0(+0)
        - (F2 R2 B2 R2 U2 F2 D L2 U') // no good
    - After (B2 L2 F2 R2 U2 B2), 1qt edges will be RH (good) and FH (good): +0+3+0(+0)
        - (B2 L2 F2 R2 U2 B2 D B2 U') // no good
    - After (F2 U2 F2 R2 B2 R2 B2), 1qt edges will be RH (good) and FH (good): +0+4+0(+0)
        - (F2 U2 F2 R2 B2 R2 B2 D' L2 U') // no good
    - After (F2 U2 B2 L2 B2 L2 F2), 1qt edges will be RH (good) and FH (good): +0+4+0(+0)
        - (F2 U2 B2 L2 B2 L2 F2 D' L2 U') // no good
    - After (F2 R2 B2 U2 F2 U2 R2), 1qt edges will be RH (good) and FH (good): +0+4+0(+0)
        - (F2 R2 B2 U2 F2 U2 R2 D' R2 U') // no good
    - After (B2 U2 F2 L2 B2 R2 F2), 1qt edges will be RH (good) and FH (good): +0+4+0(+0)
        - (B2 U2 F2 L2 B2 R2 F2 D' B2 U') // no good
    - After (B2 U2 B2 R2 B2 L2 B2), 1qt edges will be RH (good) and FH (good): +0+4+0(+0)
        - (B2 U2 B2 R2 B2 L2 B2 D' B2 U') // no good
    - After (B2 L2 F2 U2 B2 U2 R2), 1qt edges will be RH (good) and FH (good): +0+4+0(+0)
        - (B2 L2 F2 U2 B2 U2 R2 D' F2 U') // no good
- (U2 L2 U)
    - After (L2 B2 U2 B2), 1qt edges will be RH (good) and FD (bad): +0+1+1(+3)
- (U2 L2 U')
    - After (B2 U2 L2), 1qt edges will be RH (good) and FD (bad): +0+0+3(+3)
- (R2 U2 R2 U)
    - After (R2 U2 L2 F2), 1qt edges will be RH (good) and FD (bad): +1+1+0(+3)
- (R2 U2 R2 U')
    - After (R2 L2 F2 U2 R2), 1qt edges will be RH (good) and FV (bad): +1+2+0(+3)
- (U2 B2 L2 U)
    - After (F2 U2 L2), 1qt edges will be RD (bad) and FD (bad): +1+0+0(+6)
- (U2 B2 L2 U')
    - After (L2 U2 F2), 1qt edges will be RD (bad) and FD (bad): +1+0+0(+6)
- (L2 U2 R2 U')
    - After (R2 F2 U2 B2), 1qt edges will be RH (good) and FV (bad): +1+1+0(+3)
- (U2 F2 R2 U')
    - After (L2 U2 L2 B2), 1qt edges will be RD (bad) and FV (bad), fr=1: +1+1+0(+6)
- (L2 U2 R2 U)
    - After (F2 U2 R2 F2 B2), 1qt edges will be RH (good) and FV (bad), fr=1: +1+2+0(+5)
- (U2 F2 R2 U)
    - After (B2 U2 R2), 1qt edges will be RD (bad) and FD (bad), fr=1: +1+0+2(+6)
- (L2 U2 L2 U)
    - After (R2 F2 U2 F2), 1qt edges will be RH (good) and FV (bad): +1+1+1(+3)
- (L2 U2 L2 U')
    - After (F2 L2 U2 R2), 1qt edges will be RH (good) and FV (bad): +1+1+1(+3)
- (R2 U2 L2 U')
    - After (R2 F2 U2 B2), 1qt edges will be RH (good) and FV (bad), fr=1: +1+1+1(+5)
- (U2 B2 R2 U)
    - After (R2 F2 U2 F2), 1qt edges will be RD (bad) and FD (bad), fr=1: +1+1+1(+6)
- (U2 B2 R2 U')
    - After (F2 L2 U2 R2), 1qt edges will be RD (bad) and FD (bad), fr=1: +1+1+1(+6)
- (U2 F2 L2 U)
    - After (R2 B2 U2 F2), 1qt edges will be RD (bad) and FD (bad): +1+1+1(+6)

Skeleton starting with L2 U2 B2 U has HH corners, L=10, 3 spare moves.

- L2 U2 B2 U
    - After R2, 1qt edges will be RH (good) and FD (bad): +0+0+1(+3)
- B2 U2 L2 U
    - After B2, 1qt edges will be RV (bad) and FH (good): +0+0+1(+3)
- B2 U2 R2 U
    - After L2, 1qt edges will be RH (good) and FH (good): +0+0+3(+0)
        - L2 D B2 U2 R2 B2 R2 F2 U' // no good
        - L2 U R2 U2 F2 R2 B2 R2 U' // no good

Stop: 10 HTRs done, nothing within goal. This DR's optimal is 13.

### 4b3, scramble 2

`R' U' F R2 B2 R' U F2 U' F' U2 L' F2 R' U2 L' D2 F2 R F2 D' B2 D2 R' U' F`

4b3 6e, goal 13.

Skeleton starting with B2 U has RV corners, L=10, 3 spare moves.

- B2 U
    - After R2, 1qt edges will be RH (bad) and FH (good), fr=1: +0+0+0(+2)
        - R2 U F2 U2 L2 U' // no good
        - R2 U' L2 U2 F2 U // no good
- F2 U
    - After F2, 1qt edges will be RD (bad) and FV (good), fr=1: +0+0+3(+2)
- B2 U'
    - After R2 U2 R2, 1qt edges will be RH (bad) and FH (good), fr=1: +0+2+1(+2)

Check inverse. Skeleton starting with (U2 L2 U) has FD corners.

- (U2 L2 U)
    - After (F2 U2 R2 B2 R2 B2), 1qt edges will be FD (good) and RH (good): +0+3+0(+0)
        - (F2 U2 R2 B2 R2 B2 D R2 U) // no good
    - After (B2 U2 R2 B2 L2 B2), 1qt edges will be FD (good) and RH (good): +0+3+0(+0)
        - (B2 U2 R2 B2 L2 B2 D B2 U) // no good
- (U2 L2 U')
    - After (R2 U2 L2 B2), 1qt edges will be FH (bad) and RH (good): +0+1+0(+3)
- (U2 R2 U)
    - After (L2 F2 U2 F2), 1qt edges will be FH (bad) and RV (bad), fr=1: +0+1+1(+5)
- (U2 R2 U')
    - After (R2 B2 U2 L2 B2), 1qt edges will be FH (bad) and RH (good): +0+2+1(+3)
- (R2 U2 L2 U)
    - After (B2 U2 R2), 1qt edges will be FH (bad) and RH (good): +1+0+0(+3)
- (R2 U2 L2 U')
    - After (R2 U2 B2), 1qt edges will be FH (bad) and RH (good): +1+0+0(+3)
- (L2 U2 L2 U)
    - After (L2 B2 U2 B2), 1qt edges will be FH (bad) and RH (good): +1+1+0(+3)
- (L2 U2 L2 U')
    - After (B2 R2 U2 L2), 1qt edges will be FH (bad) and RH (good): +1+1+0(+3)
- (U2 B2 R2 U)
    - After (L2 U2 R2 B2), 1qt edges will be FH (bad) and RD (good): +1+1+0(+3)
- (U2 F2 L2 U')
    - After (R2 F2 U2 B2), 1qt edges will be FV (bad) and RD (good), fr=1: +1+1+0(+5)

Skeleton starting with U' F2 U' B2 U' has RV corners, L=11, 2 spare moves.

- U' F2 U' B2 U'
    - After F2 R2, 1qt edges will be RV (good) and FD (bad): +0+1+0(+3)
- U' F2 U' F2 U'
    - After R2 F2, 1qt edges will be RV (good) and FD (bad): +0+1+1(+3)
- U' B2 U' F2 L2 U
    - After B2, 1qt edges will be RH (bad) and FD (bad): +1+0+0(+5)
- U' F2 U' R2 B2 U
    - After B2, 1qt edges will be RH (bad) and FV (good): +1+0+1(+3)
- U' R2 B2 U B2 U
    - After B2 L2, 1qt edges will be RV (good) and FH (good): +1+1+0(+0)
        - B2 L2 D B2 U' // no good
- U' F2 U' R2 F2 U
    - After F2 L2, 1qt edges will be RV (good) and FV (good): +1+1+0(+1)
- U' B2 U' F2 R2 U
    - After B2 L2, 1qt edges will be RV (good) and FD (bad): +1+1+0(+3)
- U' F2 U' L2 B2 U
    - After R2 F2, 1qt edges will be RH (bad) and FH (good): +1+1+0(+3)
- U' L2 F2 U R2 U
    - After L2 B2, 1qt edges will be RV (good) and FD (bad): +1+1+0(+3)

Check inverse. Skeleton starting with (U2 R2 U' F2 U F2 U') has HH corners.

- (U2 R2 U' F2 U F2 U')
    - After (F2), 1qt edges will be RD (bad) and FH (good): +0+0+0(+3)
- (U2 R2 U' B2 U L2 U')
    - After (F2), 1qt edges will be RD (bad) and FV (bad): +0+0+0(+6)
- (U2 L2 U' L2 U B2 U')
    - After (L2), 1qt edges will be RV (bad) and FH (good): +0+0+1(+3)
- (U2 L2 U' L2 U F2 U')
    - After (R2 F2), 1qt edges will be RV (bad) and FD (bad): +0+1+0(+6)
- (U2 R2 U' F2 U F2 U)
    - After (F2 U2 F2), 1qt edges will be RD (bad) and FH (good), fr=1: +0+2+0(+5)
- (U2 R2 U' B2 U L2 U)
    - After (B2 U2 F2), 1qt edges will be RD (bad) and FV (bad), fr=1: +0+2+0(+6)
- (L2 U2 R2 U B2 U B2 U')
    - After (B2), 1qt edges will be RD (bad) and FH (good), fr=1: +1+0+0(+5)
- (L2 U2 R2 U F2 U R2 U')
    - After (B2), 1qt edges will be RD (bad) and FV (bad), fr=1: +1+0+0(+6)
- (U2 L2 U' F2 L2 U' R2 U)
    - After (F2), 1qt edges will be RH (good) and FD (bad): +1+0+1(+3)
- (R2 U2 L2 U R2 U F2 U')
    - After (R2), 1qt edges will be RH (good) and FH (good), fr=1: +1+0+1(+5)
- (U2 L2 U' R2 U B2 R2 U)
    - After (F2 L2), 1qt edges will be RH (good) and FH (good): +1+1+0(+0)
        - (F2 L2 D' R2 U') // no good
- (U2 L2 U' R2 U F2 R2 U)
    - After (B2 R2), 1qt edges will be RH (good) and FH (good): +1+1+0(+0)
        - (B2 R2 D' L2 U') // no good
- (U2 L2 U' L2 U R2 F2 U)
    - After (F2 R2), 1qt edges will be RD (bad) and FH (good): +1+1+0(+3)
- (U2 R2 U' B2 U B2 L2 U)
    - After (B2 L2), 1qt edges will be RH (good) and FD (bad): +1+1+0(+3)
- (U2 R2 U' B2 U F2 R2 U)
    - After (R2 F2), 1qt edges will be RD (bad) and FH (good): +1+1+0(+3)
- (U2 R2 U' L2 F2 U' R2 U)
    - After (R2 B2), 1qt edges will be RH (good) and FD (bad): +1+1+0(+3)
- (R2 U2 L2 U R2 U B2 U')
    - After (L2 B2), 1qt edges will be RH (good) and FD (bad), fr=1: +1+1+0(+5)
- (U2 L2 U' F2 L2 U' L2 U)
    - After (B2 L2), 1qt edges will be RD (bad) and FD (bad): +1+1+0(+6)
- (U2 L2 U' R2 U B2 L2 U)
    - After (R2 B2), 1qt edges will be RV (bad) and FD (bad): +1+1+0(+6)
- (U2 L2 U' R2 U F2 L2 U)
    - After (L2 F2), 1qt edges will be RV (bad) and FD (bad): +1+1+0(+6)
- (U2 R2 U' F2 U L2 B2 U)
    - After (R2 B2), 1qt edges will be RD (bad) and FV (bad): +1+1+0(+6)
- (U2 R2 U' F2 U R2 F2 U)
    - After (F2 L2), 1qt edges will be RV (bad) and FD (bad): +1+1+0(+6)
- (U2 R2 U' R2 B2 U' F2 U)
    - After (B2 L2), 1qt edges will be RV (bad) and FD (bad): +1+1+0(+6)

Skeleton starting with U' R2 U' L2 U' has RV corners, L=11, 2 spare moves.

- U' R2 U' L2 U'
    - After B2 L2, 1qt edges will be RV (good) and FV (good), fr=1: +0+1+0(+2)
- U' L2 U' F2 U'
    - After B2 R2, 1qt edges will be RD (bad) and FV (good), fr=1: +0+1+1(+2)
- U' R2 U' R2 U
    - After F2 U2 B2, 1qt edges will be RH (bad) and FH (good): +0+2+0(+3)

Check inverse. Skeleton starting with (U2 L2 U L2 U' L2 U) has HH corners.

- (U2 L2 U L2 U' L2 U)
    - After (B2), 1qt edges will be RV (bad) and FH (good), fr=1: +0+0+0(+5)
- (U2 R2 U B2 U' L2 U)
    - After (L2), 1qt edges will be RD (bad) and FH (good), fr=1: +0+0+1(+5)
- (U2 L2 U L2 U' R2 U)
    - After (F2 L2), 1qt edges will be RH (good) and FV (bad), fr=1: +0+1+0(+5)
- (U2 L2 U L2 U' L2 U')
    - After (B2 U2 B2), 1qt edges will be RV (bad) and FH (good): +0+2+0(+3)
- (U2 L2 U R2 U' F2 U)
    - After (R2 L2 B2), 1qt edges will be RD (bad) and FH (good), fr=1: +0+2+0(+5)
- (U2 R2 U F2 U' B2 U)
    - After (F2 B2 R2), 1qt edges will be RV (bad) and FV (bad), fr=1: +0+2+0(+6)
- (U2 R2 U F2 U' F2 U)
    - After (R2 L2 B2), 1qt edges will be RD (bad) and FV (bad), fr=1: +0+2+0(+6)
- (R2 U2 L2 U' R2 U' R2 U)
    - After (F2), 1qt edges will be RH (good) and FH (good): +1+0+0(+0)
        - (F2 D B2 U') // no good
- (L2 U2 R2 U' F2 U' R2 U)
    - After (R2), 1qt edges will be RD (bad) and FH (good): +1+0+1(+3)
- (U2 R2 U B2 U' B2 L2 U')
    - After (F2), 1qt edges will be RD (bad) and FH (good), fr=1: +1+0+1(+5)
- (U2 R2 U L2 F2 U L2 U')
    - After (R2), 1qt edges will be RV (bad) and FH (good), fr=1: +1+0+1(+5)
- (L2 U2 L2 U' L2 U' R2 U)
    - After (B2 R2), 1qt edges will be RH (good) and FV (bad): +1+1+0(+3)
- (U2 F2 L2 U' F2 U F2 U')
    - After (F2 R2), 1qt edges will be RH (good) and FV (bad), fr=1: +1+1+0(+5)
- (U2 R2 U R2 B2 U B2 U')
    - After (B2 R2), 1qt edges will be RD (bad) and FH (good), fr=1: +1+1+0(+5)
- (U2 R2 U R2 B2 U F2 U')
    - After (L2 F2), 1qt edges will be RH (good) and FD (bad), fr=1: +1+1+0(+5)
- (R2 U2 L2 U' R2 U' L2 U)
    - After (B2 R2), 1qt edges will be RV (bad) and FV (bad): +1+1+0(+6)

Skeleton starting with F2 U B2 U' R2 U has RV corners, L=11, 2 spare moves.

- F2 U B2 U' R2 U
    - After R2 L2, 1qt edges will be RD (bad) and FH (good), fr=1: +0+2+0(+2)

Skeleton starting with F2 U B2 U L2 U has RV corners, L=11, 2 spare moves.

- F2 U B2 U L2 U
    - After R2 L2, 1qt edges will be RD (bad) and FD (bad): +0+2+0(+5)

Skeleton starting with F2 U B2 U B2 U' has RV corners, L=11, 2 spare moves.

- F2 U B2 U B2 U'
    - After F2 B2, 1qt edges will be RH (bad) and FV (good), fr=1: +0+2+0(+2)

Skeleton starting with F2 U B2 U' F2 U' has RV corners, L=11, 2 spare moves.

- F2 U B2 U' F2 U'
    - After F2 B2, 1qt edges will be RV (good) and FV (good): +0+2+0(+1)

Skeleton starting with F2 U B2 U B2 U2 L2 U' has HH corners, L=11, 2 spare moves.

- F2 U B2 U B2 U2 L2 U'
    - After R2, 1qt edges will be RH (good) and FH (good), fr=1: +0+0+2(+5)
- F2 U B2 U' L2 U2 B2 U
    - After R2, 1qt edges will be RH (good) and FH (good), fr=1: +0+0+2(+5)

Skeleton starting with (F2 U2 R2 U) on inverse has RV corners, L=12, 1 spare move.

- (F2 U2 R2 U)
    - After (B2 U2 L2), 1qt edges will be RD (bad) and FH (good), fr=1: +0+0+0(+2)
- (F2 U2 R2 U')
    - After (L2 U2 B2), 1qt edges will be RD (bad) and FH (good), fr=1: +0+0+0(+2)
- (B2 U2 L2 U)
    - After (L2 U2 F2), 1qt edges will be RD (bad) and FH (good): +0+0+0(+3)
- (B2 U2 L2 U')
    - After (F2 U2 L2), 1qt edges will be RD (bad) and FH (good): +0+0+0(+3)
- (L2 U2 F2 U)
    - After (L2 U2 L2 F2), 1qt edges will be RD (bad) and FV (good), fr=1: +0+1+0(+2)
- (L2 U2 F2 U')
    - After (L2 U2 R2 B2), 1qt edges will be RV (good) and FD (bad): +0+1+0(+3)
- (R2 U2 B2 U')
    - After (F2 L2 U2 L2), 1qt edges will be RV (good) and FV (good): +0+1+0(+1)

Skeleton starting with U' F2 U F2 U has DD corners, L=12, 1 spare move.

- U' F2 U F2 U
    - After B2 L2, 1qt edges will be FD (good) and RH (bad): +0+1+0(+3)

Check inverse. Skeleton starting with (F2 U2 R2 U B2 U' L2 U) has HH corners.

- (F2 U2 R2 U B2 U' L2 U)
    - After (L2), 1qt edges will be RD (bad) and FH (good), fr=1: +0+0+0(+5)
- (L2 U2 B2 U L2 U B2 U')
    - After (B2), 1qt edges will be RD (bad) and FH (good): +0+0+1(+3)
- (F2 U2 L2 U L2 U' L2 U)
    - After (B2), 1qt edges will be RV (bad) and FH (good), fr=1: +0+0+1(+5)
- (R2 U2 F2 U L2 U B2 U')
    - After (F2), 1qt edges will be RV (bad) and FD (bad): +0+0+1(+6)
- (F2 U2 R2 U B2 U' R2 U)
    - After (R2 B2), 1qt edges will be RH (good) and FV (bad), fr=1: +0+1+0(+5)
- (L2 U2 F2 U F2 U B2 U')
    - After (R2 B2), 1qt edges will be RV (bad) and FD (bad): +0+1+0(+6)
- (R2 U2 F2 U L2 U F2 U')
    - After (B2 L2), 1qt edges will be RV (bad) and FV (bad): +0+1+0(+6)

Skeleton starting with U' B2 U R2 U2 F2 U has RD corners, L=12, 1 spare move.

- U' B2 U R2 U2 F2 U
    - After B2, 1qt edges will be RH (bad) and FH (good): +0+0+0(+3)
- U' B2 U' F2 U2 R2 U'
    - After B2, 1qt edges will be RH (bad) and FH (good): +0+0+0(+3)
- U' F2 U B2 U2 R2 U
    - After F2, 1qt edges will be RV (bad) and FH (good): +0+0+0(+3)
- U' F2 U' R2 U2 B2 U'
    - After F2, 1qt edges will be RV (bad) and FH (good): +0+0+0(+3)
- U' F2 U B2 U2 L2 U
    - After R2, 1qt edges will be RH (bad) and FH (good): +0+0+1(+3)
- U' F2 U' L2 U2 B2 U'
    - After R2, 1qt edges will be RH (bad) and FH (good): +0+0+1(+3)
- U' B2 U L2 U2 F2 U
    - After B2 R2, 1qt edges will be RD (good) and FH (good): +0+1+0(+0)
        - B2 R2 U' B2 U // no good
- U' B2 U' F2 U2 L2 U'
    - After B2 R2, 1qt edges will be RD (good) and FH (good): +0+1+0(+0)
        - B2 R2 U' B2 U // no good

Stop: 10 HTRs done, nothing within goal. This DR's optimal is 14, over the goal.

### 4b3, scramble 3

`R' U' F U2 F2 R2 B2 U' R' F B' R D L U' R2 U' D' F2 U2 D L2 D2 R' U' F`

4b3 4e, goal 13.

Skeleton starting with U has HH corners, L=7, 6 spare moves.

- U
    - After L2, 1qt edges will be RH (good) and FV (bad): +0+0+3(+3)
        - L2 D R2 U2 B2 R2 B2 R2 U' // no good
        - L2 U F2 U2 R2 F2 L2 B2 U' // no good
        - L2 D R2 U2 B2 L2 B2 L2 U' // no good
        - L2 U F2 U2 R2 B2 L2 F2 U // no good
        - L2 D L2 U2 B2 R2 B2 L2 U // no good
        - L2 U B2 U2 R2 F2 L2 F2 U' // no good
        - L2 D L2 U2 B2 L2 B2 R2 U' // no good
        - L2 U B2 U2 R2 B2 L2 B2 U' // no good
- U'
    - After R2 U2 L2, 1qt edges will be RH (good) and FV (bad): +0+2+3(+3)

Check inverse. Skeleton starting with (U) has HH corners.

- (U)
    - After (F2 U2 R2), 1qt edges will be RV (bad) and FH (good): +0+0+3(+3)
        - (F2 U2 R2 U' B2 R2 F2 L2 U') // no good
        - (F2 U2 R2 D' R2 F2 R2 F2 U) // no good

Stop: 10 HTRs done, nothing within goal. This DR's optimal is 14, over the goal.

### 4b3, scramble 4

`R' U' F R D' F2 L' D2 F2 R D2 B2 L D2 R2 B R' F L' D' R2 B F2 R' U' F`

4b3 6e, goal 13.

Skeleton starting with U has RD corners, L=8, 5 spare moves.

- U
    - After R2, 1qt edges will be RH (bad) and FD (good): +0+0+1(+3)
        - R2 D F2 U2 B2 R2 U // no good
        - R2 U L2 U2 L2 B2 U // no good
    - After L2, 1qt edges will be RD (good) and FV (bad): +0+0+1(+3)
        - L2 U' R2 U2 R2 B2 U' // no good
        - L2 D' F2 U2 B2 L2 U // no good
    - After R2, 1qt edges will be RH (bad) and FD (good): +0+0+2(+3)
        - R2 D L2 B2 U2 R2 B2 U // no good
        - R2 U B2 R2 U2 B2 L2 U // no good
        - R2 U B2 L2 U2 F2 R2 D' // no good
        - R2 U B2 L2 U2 B2 L2 U // no good
    - After L2, 1qt edges will be RD (good) and FV (bad): +0+0+2(+3)
        - L2 D' R2 F2 U2 L2 B2 U' // no good
        - L2 U' B2 R2 U2 B2 R2 U // no good

Stop: 10 HTRs done, nothing within goal. This DR's optimal is 14, over the goal.

### 4b3, scramble 5

`R' U' F U R F R' B2 U2 D' F' U R2 U L2 D' L2 D2 B2 R2 U2 B2 R' U' F`

4b3 2e, goal 13.

Skeleton starting with R2 U' has FD corners, L=9, 4 spare moves.

- R2 U'
    - After L2 F2 U2 F2, 1qt edges will be FV (bad) and RH (good): +0+1+0(+3)
        - L2 F2 U2 F2 D' R2 U // no good
    - After F2 U2 B2 R2, 1qt edges will be FH (bad) and RH (good): +0+1+0(+3)
        - F2 U2 B2 R2 D' B2 U' // no good
    - After F2 L2 F2 L2 U2 B2, 1qt edges will be FD (good) and RH (good): +0+3+0(+0)
        - F2 L2 F2 L2 U2 B2 D' B2 U // no good
    - After B2 R2 B2 L2 U2 F2, 1qt edges will be FD (good) and RH (good): +0+3+0(+0)
        - B2 R2 B2 L2 U2 F2 D' R2 U // no good
    - After F2 U2 F2 R2 F2 L2 F2, 1qt edges will be FD (good) and RH (good): +0+4+0(+0)
        - F2 U2 F2 R2 F2 L2 F2 D L2 U // no good
    - After F2 U2 B2 L2 F2 R2 B2, 1qt edges will be FD (good) and RH (good): +0+4+0(+0)
        - F2 U2 B2 L2 F2 R2 B2 D L2 U // no good
    - After F2 L2 F2 U2 B2 U2 L2, 1qt edges will be FD (good) and RH (good): +0+4+0(+0)
        - F2 L2 F2 U2 B2 U2 L2 D F2 U // no good
    - After B2 U2 F2 L2 F2 L2 B2, 1qt edges will be FD (good) and RH (good): +0+4+0(+0)
        - B2 U2 F2 L2 F2 L2 B2 D F2 U // no good
    - After B2 U2 B2 R2 F2 R2 F2, 1qt edges will be FD (good) and RH (good): +0+4+0(+0)
        - B2 U2 B2 R2 F2 R2 F2 D F2 U // no good
    - After B2 R2 B2 U2 F2 U2 L2, 1qt edges will be FD (good) and RH (good): +0+4+0(+0)
        - B2 R2 B2 U2 F2 U2 L2 D L2 U // no good

Stop: 10 HTRs done, nothing within goal. This DR's optimal is 13.

### 4b3, scramble 6

`R' U' F D' R D' U' F2 D L2 F2 U R2 D F D L2 U' L F' R F2 R' U' F`

4b3 4e, goal 13.

Skeleton starting with L2 U has RV corners, L=10, 3 spare moves.

- L2 U
    - After F2, 1qt edges will be RV (good) and FV (good): +0+0+3(+1)
- R2 U
    - After L2, 1qt edges will be RH (bad) and FH (good), fr=1: +0+0+3(+2)
- F2 L2 U'
    - After R2, 1qt edges will be RD (bad) and FV (good), fr=1: +1+0+0(+2)
        - R2 D R2 U2 B2 U' // no good
        - R2 D' F2 U2 L2 U // no good
- F2 R2 U'
    - After B2, 1qt edges will be RV (good) and FV (good), fr=1: +1+0+0(+2)
        - B2 U B2 U2 L2 U // no good
        - B2 U' L2 U2 B2 U' // no good
    - After B2, 1qt edges will be RV (good) and FV (good): +1+0+1(+1)
        - B2 U B2 R2 U2 L2 U // no good
        - B2 U B2 L2 U2 L2 U // no good
        - B2 U' L2 F2 U2 B2 U' // no good
        - B2 U' L2 B2 U2 B2 U' // no good

Check inverse. Skeleton starting with (U2 L2 U) has RD corners.

- (U2 L2 U)
    - After (R2 F2 B2 U2 F2), 1qt edges will be RV (bad) and FH (good): +0+2+1(+3)
- (U2 L2 U')
    - After (F2 U2 R2 F2 B2), 1qt edges will be RD (good) and FV (bad): +0+2+1(+3)
- (U2 R2 U)
    - After (R2 L2 F2 U2 R2), 1qt edges will be RH (bad) and FD (good): +0+2+1(+3)
- (U2 R2 U')
    - After (R2 U2 R2 L2 F2), 1qt edges will be RV (bad) and FH (good): +0+2+1(+3)
- (U2 B2 L2 U')
    - After (B2 U2 F2 R2), 1qt edges will be RD (good) and FD (good): +1+1+0(+1)
        - (B2 U2 F2 R2 U' B2 U') // no good
- (U2 B2 R2 U')
    - After (L2 U2 L2 B2), 1qt edges will be RD (good) and FD (good): +1+1+0(+1)
        - (L2 U2 L2 B2 U' B2 U') // no good

Stop: 10 HTRs done, nothing within goal. This DR's optimal is 14, over the goal.

### 4b3, scramble 7

`R' U' F D R' B' D' L U' B2 R' F' U R2 U' F2 D' F2 L2 D' R2 L' D2 R' U' F`

4b3 4e, goal 13.

Skeleton starting with U has FV corners, L=9, 4 spare moves.

- U
    - After F2, 1qt edges will be FV (good) and RV (good): +0+0+3(+1)
        - F2 D R2 U2 F2 R2 B2 R2 U // no good
        - F2 U F2 U2 L2 F2 L2 B2 U // no good
        - F2 D R2 U2 F2 L2 B2 L2 U // no good
        - F2 U F2 U2 L2 B2 L2 F2 U // no good
        - F2 D L2 U2 F2 R2 B2 L2 U // no good
        - F2 U B2 U2 L2 F2 L2 F2 U // no good
        - F2 D L2 U2 F2 L2 B2 R2 U // no good
        - F2 U B2 U2 L2 B2 L2 B2 U // no good

Check inverse. Skeleton starting with (U2 B2 U) has HH corners.

- (U2 B2 U)
    - After (R2 U2 R2 F2), 1qt edges will be RH (good) and FV (bad): +0+1+1(+3)
- (U2 F2 U)
    - After (F2 U2 B2 L2), 1qt edges will be RH (good) and FV (bad): +0+1+1(+3)
- (U2 F2 U')
    - After (R2 U2 R2 F2), 1qt edges will be RV (bad) and FH (good): +0+1+3(+3)
- (U2 B2 U')
    - After (R2 U2 R2 F2), 1qt edges will be RD (bad) and FD (bad), fr=1: +0+1+3(+6)
- (U2 R2 B2 U)
    - After (L2 U2 B2), 1qt edges will be RD (bad) and FH (good): +1+0+0(+3)
        - (L2 U2 B2 U' L2 U') // no good
- (U2 R2 B2 U')
    - After (B2 U2 L2), 1qt edges will be RD (bad) and FH (good): +1+0+0(+3)
        - (B2 U2 L2 U L2 U') // no good

Stop: 10 HTRs done, nothing within goal. This DR's optimal is 14, over the goal.

### 4b3, scramble 8

`R' U' F R' U2 L2 U' F D' L D2 L U' F R2 L2 U2 R2 B2 U' R2 U2 F2 R' U' F`

4b3 4e, goal 13.

Skeleton starting with U2 F2 U has HH corners, L=9, 4 spare moves.

- U2 F2 U
    - After R2 U2 F2, 1qt edges will be RV (bad) and FH (good): +0+0+1(+3)
        - R2 U2 F2 U' F2 L2 U // no good
        - R2 U2 F2 D' R2 F2 U' // no good
    - After R2 U2 L2 B2, 1qt edges will be RH (good) and FH (good): +0+1+1(+0)
        - R2 U2 L2 B2 D R2 B2 U' // no good
        - R2 U2 L2 B2 U B2 L2 U // no good
    - After R2 U2 L2 B2, 1qt edges will be RH (good) and FH (good): +0+1+3(+0)
        - R2 U2 L2 B2 D F2 B2 R2 F2 U' // no good
        - R2 U2 L2 B2 U R2 L2 B2 R2 U // no good
    - After L2 U2 R2 F2, 1qt edges will be RH (good) and FH (good): +0+1+3(+0)
        - L2 U2 R2 F2 D R2 F2 R2 L2 U' // no good
        - L2 U2 R2 F2 U B2 R2 F2 B2 U' // no good
    - After F2 U2 F2 R2, 1qt edges will be RH (good) and FH (good): +0+1+3(+0)
        - F2 U2 F2 R2 U' R2 U2 F2 L2 U // no good
        - F2 U2 F2 R2 D' F2 U2 R2 F2 U // no good

Stop: 10 HTRs done, nothing within goal. This DR's optimal is 13.

## 0c0

### 0c0, scramble 1

`R' U' F U' L U' F' B D2 B R L F U' B2 R2 U F2 R2 D2 L2 F2 D' R' U' F`

0c0 6e, goal 12.

Skeleton starting with U has FD corners, L=3, 9 spare moves.

- With no setup, 1qt edges will be FD (good) and RV (bad), fr=1: +0+5(+5)

Check inverse. Skeleton starting with (F2) has HH corners.

- After (F2), 1qt edges will be RH (good) and FV (bad), fr=1: +0+5(+5)

Skeleton starting with U2 B2 has HH corners, L=4, 8 spare moves.

- After U2 B2, 1qt edges will be RH (good) and FD (bad), fr=1: +0+5(+5)

Skeleton starting with B2 has FV corners, L=5, 7 spare moves.

- After B2, 1qt edges will be FD (bad) and RD (bad): +0+5(+5)

Check inverse. Skeleton starting with (U2 B2) has FD corners.

- After (U2 B2), 1qt edges will be FV (bad) and RD (good): +0+5(+3)

Skeleton starting with U2 R2 has RD corners, L=5, 7 spare moves.

- After U2 R2, 1qt edges will be RV (bad) and FH (good), fr=1: +0+5(+5)

Check inverse. Skeleton starting with (R2) has RV corners.

- After (R2), 1qt edges will be RV (good) and FD (bad), fr=1: +0+5(+2)
    - (R2 U' R2 L2 F2 R2 B2 U') // no good
    - (R2 D' F2 B2 L2 B2 L2 U) // no good
    - (R2 U' R2 L2 B2 R2 F2 U) // no good
    - (R2 D' F2 B2 R2 B2 R2 U) // no good
    - (R2 U' F2 R2 B2 R2 L2 U) // no good
    - (R2 D' L2 B2 L2 F2 B2 U) // no good
    - (R2 U' B2 R2 F2 R2 L2 U') // no good
    - (R2 D' R2 B2 R2 F2 B2 U) // no good

Skeleton starting with L2 has DD corners, L=6, 6 spare moves.

- After L2, 1qt edges will be FV (good) and RV (good): +0+5(+1)
    - L2 U R2 F2 L2 F2 B2 U' // no good
    - L2 D B2 L2 B2 R2 L2 U' // no good

Stop: 10 HTRs done, nothing within goal. This DR's optimal is 13, over the goal.

### 0c0, scramble 2

`R' U' F R2 B' D' R U2 D2 L2 F2 R' B U B2 U B2 D' F2 R2 U' F2 D R' U' F`

0c0 2e, goal 12.

Skeleton starting with L2 has RD corners, L=4, 8 spare moves.

- After L2, 1qt edges will be RV (bad) and FH (good), fr=1: +0+3(+5)
    - L2 U F2 R2 F2 U // no good
    - L2 D R2 F2 L2 U // no good
    - L2 U B2 R2 B2 U // no good
    - L2 D L2 F2 R2 U // no good

Check inverse. Skeleton starting with (L2) has RD corners.

- After (L2), 1qt edges will be RH (bad) and FH (good), fr=1: +0+3(+5)
    - (L2 D' L2 F2 R2 U') // no good
    - (L2 U' F2 L2 F2 U') // no good
    - (L2 D' R2 F2 L2 U') // no good
    - (L2 U' B2 L2 B2 U') // no good

Skeleton starting with U has DD corners, L=5, 7 spare moves.

- With no setup, 1qt edges will be FH (bad) and RD (good): +0+3(+3)
    - U F2 R2 F2 U R2 U2 B2 L2 B2 L2 D2 // 12
    - D R2 F2 L2 U // no good

Stop: 10 HTRs done, one finish within goal (12). This DR's optimal is 11.

## 2c3

### 2c3, scramble 1

`R' U' F U' D2 F' L B2 U2 R2 F U' F L2 F' L2 B' L2 U2 D2 B D2 R' U' F`

2c3 2e, goal 13.

Skeleton starting with R2 U has FD corners, L=7, 6 spare moves.

- R2 U
    - After L2, 1qt edges will be FV (bad) and RD (good), fr=1: +0+0+3(+5)
- L2 U
    - After R2 B2, 1qt edges will be FH (bad) and RH (good), fr=1: +0+1+0(+5)
        - R2 B2 U B2 U // no good
    - After R2 B2, 1qt edges will be FH (bad) and RH (good): +0+1+2(+3)
        - R2 B2 U' F2 U2 B2 U' // no good
        - R2 B2 U' B2 U2 B2 U' // no good
    - After R2 U2 R2 F2 U2 R2, 1qt edges will be FD (good) and RD (good): +0+5+0(+1)
        - R2 U2 R2 F2 U2 R2 U F2 U // no good
    - After L2 U2 L2 F2 U2 L2, 1qt edges will be FD (good) and RD (good): +0+5+0(+1)
        - L2 U2 L2 F2 U2 L2 U F2 U // no good
- R2 U'
    - After F2 R2 U2 B2, 1qt edges will be FD (good) and RH (good): +0+3+1(+0)
        - F2 R2 U2 B2 U' R2 F2 U' // no good
        - F2 R2 U2 B2 D' B2 R2 U' // no good
    - After F2 L2 U2 F2, 1qt edges will be FD (good) and RH (good): +0+3+1(+0)
        - F2 L2 U2 F2 U' R2 F2 U' // no good
        - F2 L2 U2 F2 D' B2 R2 U' // no good
    - After F2 U2 F2 U2 L2, 1qt edges will be FD (good) and RH (good): +0+4+1(+0)
        - F2 U2 F2 U2 L2 U R2 F2 U' // no good

Stop: 10 HTRs done, nothing within goal. This DR's optimal is 12.

### 2c3, scramble 2

`R' U' F R2 F' D' R L2 U' R2 D' F' R2 U2 F2 R2 D F2 R2 F2 U R2 D' R' U' F`

2c3 4e, goal 13.

Skeleton starting with U2 B2 U has FD corners, L=8, 5 spare moves.

- U2 B2 U
    - After F2, 1qt edges will be FD (good) and RH (good): +0+0+5(+0)
        - F2 D B2 U2 B2 U2 B2 L2 U // no good
        - F2 U R2 U2 R2 U2 L2 F2 U // no good
        - F2 U L2 U2 L2 U2 R2 F2 U // no good
        - F2 D F2 U2 F2 U2 F2 L2 U // no good
        - F2 D R2 U2 L2 B2 R2 B2 U' // no good
        - F2 U F2 D2 F2 L2 F2 R2 U // no good
        - F2 D R2 U2 L2 F2 R2 F2 U' // no good
        - F2 U F2 D2 F2 R2 F2 L2 U // no good
        - F2 U B2 U2 B2 R2 F2 L2 U' // no good
        - F2 D L2 U2 L2 B2 L2 B2 U' // no good

Stop: 10 HTRs done, nothing within goal. This DR's optimal is 13.

### 2c3, scramble 3

`R' U' F R' F U2 D B R2 F2 D U2 B2 L' D2 F2 B2 R' L2 B2 U2 R2 U2 R' U' F`

2c3 2e, goal 13.

Skeleton starting with F2 U' has FV corners, L=8, 5 spare moves.

- F2 U'
    - After B2 L2, 1qt edges will be FV (good) and RV (good): +0+1+0(+1)
        - B2 L2 U' B2 U B2 L2 U2 R2 L2 // 12
    - After B2 L2, 1qt edges will be FV (good) and RV (good): +0+1+2(+1)
        - B2 L2 D' F2 B2 L2 U // no good
    - After B2 L2, 1qt edges will be FV (good) and RV (good), fr=1: +0+1+2(+2)
        - B2 L2 U F2 U2 B2 U // no good
        - B2 L2 U B2 U2 B2 U // no good
    - After B2 L2, 1qt edges will be FV (good) and RV (good): +0+1+3(+1)
        - B2 L2 U F2 B2 U2 B2 U // no good
        - B2 L2 U' F2 U2 F2 B2 U' // no good
    - After F2 L2 F2 R2 F2, 1qt edges will be FV (good) and RH (good): +0+4+0(+0)
        - F2 L2 F2 R2 F2 U R2 U' // no good
    - After B2 R2 F2 L2 B2, 1qt edges will be FV (good) and RH (good): +0+4+0(+0)
        - B2 R2 F2 L2 B2 U R2 U' // no good
- B2 U'
    - After L2 B2, 1qt edges will be FV (good) and RV (good): +0+1+1(+1)
        - L2 B2 D' F2 L2 U' // no good
        - L2 B2 U' L2 B2 U' // no good

Stop: 10 HTRs done, one finish within goal (12). This DR's optimal is 12.

### 2c3, scramble 4

`R' U' F U' B2 R' D B' R' D' R2 D' F' D' L2 F2 D2 L2 B2 U B2 U B2 R' U' F`

2c3 2e, goal 13.

Skeleton starting with U' has DD corners, L=8, 5 spare moves.

- U'
    - After F2 R2, 1qt edges will be FD (good) and RV (good): +0+1+0(+0)
        - F2 R2 D' R2 U // no good
    - After L2 F2 B2, 1qt edges will be FD (good) and RD (good): +0+2+0(+2)
        - L2 F2 B2 D B2 U' // no good
    - After F2 R2, 1qt edges will be FD (good) and RV (good): +0+1+2(+0)
        - F2 R2 D R2 U2 L2 U // no good
        - F2 R2 D L2 U2 L2 U // no good
        - F2 R2 U' R2 L2 F2 U' // no good
    - After R2 B2 L2 B2, 1qt edges will be FV (good) and RD (good): +0+3+0(+0)
        - R2 B2 L2 B2 D' R2 U L2 U2 R2 F2 U2 // 13
    - After F2 R2, 1qt edges will be FD (good) and RV (good): +0+1+3(+0)
        - F2 R2 D R2 L2 U2 L2 U' // no good
        - F2 R2 D' L2 U2 R2 L2 U // no good
    - After F2 U2 R2 U2 R2, 1qt edges will be FD (good) and RV (good): +0+4+0(+0)
        - F2 U2 R2 U2 R2 D L2 U' // no good
    - After F2 L2 F2 L2 B2, 1qt edges will be FV (good) and RV (good): +0+4+0(+1)
        - F2 L2 F2 L2 B2 D B2 U // no good

Stop: 10 HTRs done, one finish within goal (13). This DR's optimal is 12.

### 2c3, scramble 5

`R' U' F R F R' B' L2 F' R2 D' R' U2 F2 U2 L2 D' B2 R2 U2 L2 R' B2 R' U' F`

2c3 6e, goal 13.

Skeleton starting with U has HH corners, L=5, 8 spare moves.

- U
    - After F2 B2 R2, 1qt edges will be RH (good) and FD (bad): +0+2+3(+3)
        - F2 B2 R2 U R2 F2 U2 L2 U' // no good
        - F2 B2 R2 D F2 L2 U2 B2 U' // no good
    - After F2 B2 L2, 1qt edges will be RD (bad) and FH (good): +0+2+3(+3)
        - F2 B2 L2 U F2 R2 U2 F2 U' // no good
        - F2 B2 L2 D L2 F2 U2 L2 U' // no good
- U'
    - After R2 U2 R2, 1qt edges will be RD (bad) and FH (good): +0+2+3(+3)
        - R2 U2 R2 U R2 B2 R2 L2 U // no good
        - R2 U2 R2 D F2 R2 F2 B2 U // no good
    - After R2 U2 L2, 1qt edges will be RH (good) and FD (bad): +0+2+3(+3)
        - R2 U2 L2 U F2 L2 F2 B2 U // no good
        - R2 U2 L2 D L2 B2 R2 L2 U // no good
    - After L2 U2 R2 F2 B2, 1qt edges will be RH (good) and FD (bad): +0+4+1(+3)
        - L2 U2 R2 F2 B2 U F2 R2 U // no good
        - L2 U2 R2 F2 B2 D L2 F2 U // no good

Stop: 10 HTRs done, nothing within goal. This DR's optimal is 13.

### 2c3, scramble 6

`R' U' F D' F2 L2 B2 D' B2 U2 R2 U2 R2 U' R' B L U L D' R' F' R' U' F`

2c3 6e, goal 13.

Skeleton starting with U has HH corners, L=5, 8 spare moves.

- U
    - After F2, 1qt edges will be RD (bad) and FH (good): +0+0+3(+3)
        - F2 D' R2 F2 L2 F2 U' // no good
        - F2 U' B2 R2 B2 L2 U' // no good
        - F2 D' R2 B2 L2 B2 U' // no good
        - F2 U' B2 L2 B2 R2 U' // no good
    - After F2, 1qt edges will be RD (bad) and FH (good): +0+0+5(+3)
        - F2 U' R2 L2 F2 R2 F2 R2 U' // no good
        - F2 D' F2 B2 L2 F2 R2 B2 U' // no good
        - F2 U' R2 L2 F2 L2 F2 L2 U' // no good
        - F2 D' F2 B2 L2 B2 R2 F2 U' // no good
        - F2 D' L2 F2 L2 F2 R2 L2 U' // no good
        - F2 U' F2 R2 B2 L2 F2 B2 U' // no good

Stop: 10 HTRs done, nothing within goal. This DR's optimal is 12.

### 2c3, scramble 7

`R' U' F U' L2 B2 L D R B' R2 D' L B' R2 U2 F' B R2 F' D2 L2 D2 R' U' F`

2c3 2e, goal 13.

Skeleton starting with L2 U has DD corners, L=9, 4 spare moves.

- L2 U
    - After F2 R2 L2, 1qt edges will be FD (good) and RV (good): +0+2+1(+0)
        - F2 R2 L2 D' F2 R2 U' // no good
        - F2 R2 L2 U' L2 F2 U // no good
    - After F2 U2 F2 B2, 1qt edges will be FD (good) and RV (good): +0+3+1(+0)
        - F2 U2 F2 B2 D B2 L2 U' // no good
        - F2 U2 F2 B2 U L2 F2 U // no good
- R2 U
    - After B2 L2, 1qt edges will be FH (bad) and RV (good): +0+1+0(+3)
        - B2 L2 U L2 U' // no good
    - After R2 F2 B2, 1qt edges will be FV (good) and RV (good): +0+2+0(+1)
        - R2 F2 B2 U' F2 U // no good
    - After L2 F2 R2 F2, 1qt edges will be FV (good) and RD (good): +0+3+0(+0)
        - L2 F2 R2 F2 U L2 U // no good
    - After R2 U2 R2 B2 R2, 1qt edges will be FD (good) and RV (good): +0+4+0(+0)
        - R2 U2 R2 B2 R2 U' B2 U // no good
    - After L2 U2 R2 F2 R2, 1qt edges will be FD (good) and RV (good): +0+4+0(+0)
        - L2 U2 R2 F2 R2 U' L2 U // no good
- R2 U'
    - After L2 F2 B2 U2 R2, 1qt edges will be FV (good) and RV (good): +0+4+0(+1)
- L2 U'
    - After R2 F2 U2 L2, 1qt edges will be FD (good) and RV (good): +0+3+1(+0)
        - R2 F2 U2 L2 U' F2 R2 U // no good

Stop: 10 HTRs done, nothing within goal. This DR's optimal is 14, over the goal.

### 2c3, scramble 8

`R' U' F D F2 L' B2 R2 U2 R' D2 R' F2 U2 R F' R' B2 R' U' R D' R' U' F`

2c3 6e, goal 13.

Skeleton starting with U has FD corners, L=6, 7 spare moves.

- U
    - After F2, 1qt edges will be FH (bad) and RV (bad), fr=1: +0+0+3(+5)
- U'
    - After F2 R2 F2 U2 L2, 1qt edges will be FD (good) and RH (good), fr=1: +0+4+1(+3)

Check inverse. Skeleton starting with (F2 U) has HH corners.

- (F2 U)
    - After (L2), 1qt edges will be RV (bad) and FD (bad), fr=1: +0+0+3(+6)
- (B2 U)
    - After (R2 U2 B2 U2 F2), 1qt edges will be RH (good) and FH (good): +0+4+0(+0)
        - (R2 U2 B2 U2 F2 U L2 U) // no good
    - After (L2 B2), 1qt edges will be RH (good) and FH (good): +0+1+4(+0)
        - (L2 B2 D F2 B2 R2 U2 L2 U) // no good
        - (L2 B2 D F2 B2 L2 U2 L2 U') // no good
        - (L2 B2 D R2 U2 L2 F2 B2 U') // no good
        - (L2 B2 D R2 F2 B2 U2 L2 U) // no good
        - (L2 B2 D L2 D2 R2 F2 B2 U) // no good
        - (L2 B2 D L2 F2 B2 U2 L2 U') // no good
    - After (F2 B2 L2 F2), 1qt edges will be RH (good) and FH (good): +0+3+2(+0)
        - (F2 B2 L2 F2 U F2 U2 F2 U') // no good
        - (F2 B2 L2 F2 U B2 U2 F2 U') // no good
- (F2 U')
    - After (L2 F2 R2 U2 B2), 1qt edges will be RH (good) and FH (good), fr=1: +0+4+1(+5)
- (B2 U')
    - After (B2 U2 R2 F2), 1qt edges will be RH (good) and FH (good): +0+3+0(+0)
        - (B2 U2 R2 F2 U L2 U) // no good

Stop: 10 HTRs done, nothing within goal. This DR's optimal is 13.

### 2c3, scramble 9

`R' U' F R2 D2 B U F U2 F D' B2 D2 B2 L' U2 L' D2 L F' R D R' U' F`

2c3 6e, goal 13.

Skeleton starting with U' has RD corners, L=6, 7 spare moves.

- U'
    - After R2 B2, 1qt edges will be RD (good) and FH (good): +0+1+2(+0)
        - R2 B2 D' F2 R2 L2 U' // no good
    - After F2 B2 R2 F2, 1qt edges will be RD (good) and FH (good): +0+3+0(+0)
        - F2 B2 R2 F2 U' L2 U' // no good
    - After R2 B2, 1qt edges will be RD (good) and FH (good): +0+1+3(+0)
        - R2 B2 D R2 L2 U2 B2 U' // no good
        - R2 B2 D' F2 U2 R2 L2 U // no good
    - After F2 R2 L2, 1qt edges will be RH (bad) and FH (good): +0+2+2(+3)
        - F2 R2 L2 D R2 F2 B2 U // no good
    - After L2 B2 U2 F2 B2, 1qt edges will be RD (good) and FH (good): +0+4+0(+0)
        - L2 B2 U2 F2 B2 U F2 U' // no good
    - After R2 F2 L2 F2 R2, 1qt edges will be RD (good) and FV (bad): +0+4+0(+3)
        - R2 F2 L2 F2 R2 U B2 U // no good
    - After L2 U2 F2 U2 F2, 1qt edges will be RD (good) and FH (good), fr=1: +0+4+0(+3)
        - L2 U2 F2 U2 F2 U B2 U // no good
    - After L2 B2 L2 B2 L2, 1qt edges will be RD (good) and FV (bad): +0+4+0(+3)
        - L2 B2 L2 B2 L2 U B2 U // no good
    - After F2 U2 F2 L2 F2, 1qt edges will be RV (bad) and FH (good): +0+4+0(+3)
        - F2 U2 F2 L2 F2 U B2 U // no good

Stop: 10 HTRs done, nothing within goal. This DR's optimal is 13.

### 2c3, scramble 10

`R' U' F U L D2 B2 L B2 L' D2 R2 B2 L' B2 D2 B' R2 D B' R B' D R' U' F`

2c3 4e, goal 13.

Skeleton starting with U2 B2 U has RD corners, L=8, 5 spare moves.

- U2 B2 U
    - After B2, 1qt edges will be RV (bad) and FH (good): +0+0+0(+3)
        - B2 U' R2 U // no good
    - After B2, 1qt edges will be RV (bad) and FH (good): +0+0+2(+3)
        - B2 D' R2 L2 B2 U' // no good
    - After R2 F2 L2 F2 R2, 1qt edges will be RD (good) and FD (good): +0+4+0(+1)
        - R2 F2 L2 F2 R2 U' R2 U // no good
    - After L2 B2 L2 B2 L2, 1qt edges will be RD (good) and FD (good): +0+4+0(+1)
        - L2 B2 L2 B2 L2 U' R2 U // no good
    - After R2 F2, 1qt edges will be RD (good) and FH (good): +0+1+4(+0)
        - R2 F2 U F2 R2 F2 R2 F2 U' // no good
        - R2 F2 D R2 B2 R2 F2 L2 U' // no good
        - R2 F2 U F2 R2 B2 R2 B2 U' // no good
        - R2 F2 D R2 B2 L2 F2 R2 U' // no good
        - R2 F2 D L2 F2 R2 B2 R2 U' // no good
        - R2 F2 U B2 L2 F2 L2 B2 U' // no good

Stop: 10 HTRs done, nothing within goal. This DR's optimal is 14, over the goal.

### 2c3, scramble 11

`R' U' F R2 D' R' L' B U' F' L U2 L2 D' R2 F2 U2 L2 D2 L2 U R' B R' U' F`

2c3 4e, goal 13.

Skeleton starting with R2 U has FD corners, L=7, 6 spare moves.

- R2 U
    - After B2, 1qt edges will be FH (bad) and RV (bad): +0+0+0(+5)
        - B2 U' R2 U // no good
    - After F2 L2 B2 R2, 1qt edges will be FD (good) and RV (bad): +0+3+0(+3)
        - F2 L2 B2 R2 U F2 U // no good
    - After R2 F2 L2 F2 R2, 1qt edges will be FD (good) and RH (good): +0+4+0(+0)
        - R2 F2 L2 F2 R2 U' R2 U // no good
    - After L2 B2 L2 B2 L2, 1qt edges will be FD (good) and RH (good): +0+4+0(+0)
        - L2 B2 L2 B2 L2 U' R2 U // no good
- L2 U
    - After B2 L2, 1qt edges will be FH (bad) and RH (good): +0+1+0(+3)
        - B2 L2 U B2 U' // no good
    - After B2 L2, 1qt edges will be FH (bad) and RH (good): +0+1+2(+3)
        - B2 L2 D F2 B2 R2 U' // no good
    - After L2 U2 F2 B2, 1qt edges will be FD (good) and RH (good): +0+3+0(+0)
        - L2 U2 F2 B2 U F2 U // no good
    - After R2 B2 L2 F2, 1qt edges will be FD (good) and RV (bad): +0+3+0(+3)
        - R2 B2 L2 F2 U B2 U // no good
    - After R2, 1qt edges will be FD (good) and RH (good): +0+0+4(+0)
        - R2 D R2 B2 L2 U2 B2 U // no good
        - R2 U F2 L2 F2 U2 L2 U // no good

Stop: 10 HTRs done, nothing within goal. This DR's optimal is 13.

### 2c3, scramble 12

`R' U' F R' U D L2 F2 B' R2 D2 L' F' B2 R' F2 R' F2 U2 R D2 F2 D2 R' U' F`

2c3 6e, goal 13.

Skeleton starting with R2 U' has FD corners, L=7, 6 spare moves.

- R2 U'
    - After B2, 1qt edges will be FD (good) and RD (good): +0+0+4(+1)
        - B2 D' F2 R2 F2 U2 B2 U' // no good
        - B2 D' F2 R2 B2 U2 B2 U' // no good
        - B2 U' L2 F2 R2 U2 R2 U' // no good
        - B2 U' L2 F2 L2 U2 R2 U // no good
    - After B2, 1qt edges will be FD (good) and RD (good): +0+0+5(+1)
        - B2 U R2 B2 U2 R2 F2 R2 U // no good
        - B2 D B2 L2 U2 B2 L2 F2 U // no good
        - B2 U R2 B2 U2 L2 F2 L2 U // no good
        - B2 D B2 L2 U2 F2 L2 B2 U // no good
        - B2 U L2 F2 U2 R2 F2 L2 U // no good
        - B2 D F2 R2 U2 B2 L2 B2 U // no good

Stop: 10 HTRs done, nothing within goal. This DR's optimal is 14, over the goal.

## 2c4

### 2c4, scramble 1

`R' U' F U' F' U' D2 L' B2 U' F' D2 R D2 L2 U2 L B2 R' B2 U2 B2 U' R' U' F`

2c4 6e, goal 14.

Skeleton starting with L2 U' L2 U has RV corners, L=10, 4 spare moves.

- L2 U' L2 U
    - After R2 B2, 1qt edges will be RV (good) and FH (good): +0+1+1(+0)
        - R2 B2 U F2 R2 U' // no good
        - R2 B2 D L2 F2 U' // no good
    - After R2 B2, 1qt edges will be RV (good) and FH (good): +0+1+3(+0)
        - R2 B2 U R2 L2 F2 L2 U' // no good
        - R2 B2 D F2 B2 L2 B2 U' // no good
- R2 U' F2 U
    - After R2 F2, 1qt edges will be RH (bad) and FH (good), fr=1: +0+1+3(+2)
- L2 U' R2 U
    - After L2 B2 R2 B2, 1qt edges will be RH (bad) and FV (good): +0+3+0(+3)
- R2 U' B2 U
    - After F2 L2, 1qt edges will be RD (bad) and FD (bad): +0+1+3(+5)
- L2 U' R2 U'
    - After L2 B2 L2 U2 F2, 1qt edges will be RD (bad) and FV (good): +0+4+0(+3)
- L2 U' L2 U'
    - After R2 B2 U2 R2, 1qt edges will be RV (good) and FD (bad), fr=1: +0+3+1(+2)
- R2 U' F2 U'
    - After B2 U2 L2 B2, 1qt edges will be RH (bad) and FH (good), fr=1: +0+3+1(+2)
- F2 L2 U F2 U'
    - After B2 R2, 1qt edges will be RH (bad) and FV (good): +1+1+0(+3)
- B2 L2 U B2 U'
    - After L2, 1qt edges will be RV (good) and FD (bad): +1+0+2(+3)
- F2 R2 U L2 U'
    - After F2, 1qt edges will be RD (bad) and FH (good): +1+0+2(+3)
- L2 U' B2 L2 U'
    - After R2, 1qt edges will be RH (bad) and FV (good): +1+0+2(+3)
- F2 L2 U B2 U
    - After B2 U2 B2, 1qt edges will be RV (good) and FH (good), fr=1: +1+2+0(+1)
        - B2 U2 B2 D' L2 U' // no good
- R2 U' L2 B2 U'
    - After F2, 1qt edges will be RD (bad) and FH (good), fr=1: +1+0+3(+2)
- L2 U' F2 L2 U'
    - After R2, 1qt edges will be RD (bad) and FV (good): +1+0+3(+3)
- B2 R2 U L2 U'
    - After R2, 1qt edges will be RD (bad) and FD (bad): +1+0+3(+5)
- R2 U' R2 B2 U'
    - After B2, 1qt edges will be RH (bad) and FD (bad), fr=1: +1+0+3(+5)
- L2 U' F2 R2 U'
    - After L2 B2, 1qt edges will be RV (good) and FH (good): +1+1+2(+0)
        - L2 B2 U' F2 R2 L2 U' // no good
- R2 U' L2 B2 U
    - After F2 U2 B2, 1qt edges will be RH (bad) and FV (good), fr=1: +1+2+1(+2)

Check inverse. Skeleton starting with (U2 L2 U' R2 U') has RD corners.

- (U2 L2 U' R2 U')
    - After (F2 B2 L2), 1qt edges will be RH (bad) and FD (good): +0+2+0(+3)
- (U2 R2 U' B2 U')
    - After (R2), 1qt edges will be RD (good) and FD (good): +0+0+3(+1)
        - (R2 D R2 B2 R2 B2 U) // no good
        - (R2 U F2 R2 B2 L2 U) // no good
        - (R2 D R2 F2 R2 F2 U) // no good
        - (R2 U F2 L2 B2 R2 U) // no good

Stop: 10 HTRs done, nothing within goal. This DR's optimal is 14.

### 2c4, scramble 2

`R' U' F R F U F D' F' U2 R' U' R' U2 F2 D2 B2 R2 B2 U R2 F2 B2 R' U' F`

2c4 6e, goal 14.

Skeleton starting with B2 U' L2 U has FD corners, L=9, 5 spare moves.

- B2 U' L2 U
    - After F2 R2 F2 L2, 1qt edges will be FV (bad) and RH (good): +0+3+0(+3)
- F2 U' B2 U
    - After F2, 1qt edges will be FD (good) and RV (bad): +0+0+3(+3)
- B2 U' R2 U
    - After F2 L2, 1qt edges will be FD (good) and RD (good): +0+1+3(+1)
        - F2 L2 U F2 L2 F2 B2 U' // no good
        - F2 L2 D L2 B2 R2 L2 U' // no good
    - After R2 L2 F2 R2, 1qt edges will be FD (good) and RD (good): +0+3+1(+1)
        - R2 L2 F2 R2 D R2 B2 U' // no good
        - R2 L2 F2 R2 U B2 L2 U' // no good
- F2 U' F2 U
    - After B2 L2, 1qt edges will be FV (bad) and RD (good): +0+1+4(+3)
- B2 U' L2 U'
    - After F2 R2 B2 U2 L2, 1qt edges will be FH (bad) and RH (good): +0+4+0(+3)
- F2 U' B2 U'
    - After F2 U2 F2, 1qt edges will be FD (good) and RV (bad), fr=1: +0+2+3(+5)
- F2 U' F2 U'
    - After L2 U2 B2 R2, 1qt edges will be FH (bad) and RV (bad), fr=1: +0+3+1(+5)
- B2 U' R2 U'
    - After R2 L2 U2 B2 R2, 1qt edges will be FD (good) and RD (good): +0+4+1(+1)
- B2 U' B2 L2 U'
    - After L2, 1qt edges will be FD (good) and RV (bad): +1+0+2(+3)
- F2 U' L2 B2 U'
    - After L2 F2 R2 B2, 1qt edges will be FD (good) and RH (good): +1+3+0(+0)
        - L2 F2 R2 B2 D' L2 U // no good
- F2 U' L2 F2 U'
    - After B2 R2 F2 L2, 1qt edges will be FD (good) and RH (good): +1+3+0(+0)
        - B2 R2 F2 L2 U' B2 U // no good
- F2 U' R2 B2 U'
    - After R2 B2 L2 F2, 1qt edges will be FD (good) and RH (good): +1+3+0(+0)
        - R2 B2 L2 F2 D' R2 U // no good
- F2 U' R2 F2 U'
    - After F2 L2 B2 R2, 1qt edges will be FD (good) and RH (good): +1+3+0(+0)
        - F2 L2 B2 R2 U' F2 U // no good
- R2 F2 U R2 U'
    - After B2, 1qt edges will be FH (bad) and RH (good): +1+0+2(+3)
- B2 U' F2 L2 U'
    - After L2, 1qt edges will be FD (good) and RH (good): +1+0+3(+0)
        - L2 D B2 R2 F2 B2 U // no good
        - L2 U L2 B2 R2 L2 U // no good

Stop: 10 HTRs done, nothing within goal. This DR's optimal is 15, over the goal.

### 2c4, scramble 3

`R' U' F R2 F R2 B2 L2 F L2 B' L2 R2 D2 F2 U F R' D' B D2 B' F' R' U' F`

2c4 0e, goal 14.

Skeleton starting with B2 U L2 U' has FV corners, L=10, 4 spare moves.

- B2 U L2 U'
    - After R2, 1qt edges will be FD (bad) and RD (bad), fr=1: +0+0+0(+5)
- F2 U F2 U'
    - After L2, 1qt edges will be FD (bad) and RD (bad), fr=1: +0+0+0(+5)
- B2 U R2 U'
    - After R2 B2, 1qt edges will be FV (good) and RD (bad), fr=1: +0+1+0(+2)
        - R2 B2 U' B2 U' // no good
    - After B2 U2 R2 L2, 1qt edges will be FV (good) and RH (good), fr=1: +0+3+0(+1)
        - B2 U2 R2 L2 U' B2 U // no good
- F2 U B2 U'
    - After L2 B2, 1qt edges will be FV (good) and RD (bad), fr=1: +0+1+0(+2)
        - L2 B2 U' L2 U' // no good
    - After B2 U2 R2 L2, 1qt edges will be FV (good) and RH (good), fr=1: +0+3+0(+1)
        - B2 U2 R2 L2 U' R2 U // no good
- B2 U L2 U
    - After L2 B2 L2 U2 B2, 1qt edges will be FV (good) and RH (good), fr=1: +0+4+0(+1)
- F2 U F2 U
    - After L2 F2 L2 U2 B2, 1qt edges will be FV (good) and RH (good), fr=1: +0+4+0(+1)
- B2 U R2 U
    - After R2 L2 U2 B2, 1qt edges will be FV (good) and RH (good), fr=1: +0+3+0(+1)
        - R2 L2 U2 B2 U B2 U // no good
    - After R2 L2 F2 U2 B2, 1qt edges will be FV (good) and RH (good): +0+4+0(+0)
        - R2 L2 F2 U2 B2 U' F2 U' // no good
    - After B2 U2 B2 R2 L2, 1qt edges will be FV (good) and RH (good): +0+4+0(+0)
        - B2 U2 B2 R2 L2 U' B2 U' // no good
- F2 U B2 U
    - After R2 L2 U2 B2, 1qt edges will be FV (good) and RH (good), fr=1: +0+3+0(+1)
        - R2 L2 U2 B2 U R2 U // no good
    - After R2 L2 B2 U2 B2, 1qt edges will be FV (good) and RH (good): +0+4+0(+0)
        - R2 L2 B2 U2 B2 U' R2 U' // no good
    - After F2 U2 B2 R2 L2, 1qt edges will be FV (good) and RH (good): +0+4+0(+0)
        - F2 U2 B2 R2 L2 U' L2 U' // no good

Stop: 10 HTRs done, nothing within goal. This DR's optimal is 14.

### 2c4, scramble 4

`R' U' F L U2 R L2 F' L B' D L F2 R2 U2 L' U2 L' B2 R' U2 L' B R' U' F`

2c4 2e, goal 14.

Skeleton starting with F2 U R2 U' has FV corners, L=10, 4 spare moves.

- F2 U R2 U'
    - After F2, 1qt edges will be FH (bad) and RD (bad): +0+0+3(+5)
- F2 U L2 U'
    - After B2 L2, 1qt edges will be FV (good) and RH (good): +0+1+2(+0)
        - B2 L2 D' R2 F2 B2 U' // no good
    - After R2 L2 B2 R2, 1qt edges will be FV (good) and RH (good): +0+3+0(+0)
        - R2 L2 B2 R2 U' F2 U' // no good
    - After B2 L2, 1qt edges will be FV (good) and RH (good): +0+1+3(+0)
        - B2 L2 D F2 B2 U2 L2 U' // no good
        - B2 L2 D' R2 U2 F2 B2 U // no good
    - After F2 L2 U2 R2 L2, 1qt edges will be FV (good) and RH (good): +0+4+0(+0)
        - F2 L2 U2 R2 L2 U R2 U' // no good
- F2 U L2 U
    - After R2 U2 F2 R2, 1qt edges will be FV (good) and RH (good), fr=1: +0+3+0(+1)
        - R2 U2 F2 R2 U L2 U // no good
    - After R2 L2 U2 F2 R2, 1qt edges will be FV (good) and RH (good): +0+4+0(+0)
        - R2 L2 U2 F2 R2 U' R2 U' // no good
- B2 U B2 U'
    - After F2 L2 B2 R2, 1qt edges will be FV (good) and RD (bad): +0+3+1(+3)
- B2 U F2 U'
    - After R2 B2 L2 F2, 1qt edges will be FV (good) and RD (bad): +0+3+1(+3)
- B2 U R2 B2 U
    - After R2, 1qt edges will be FH (bad) and RD (bad): +1+0+0(+5)
- B2 U R2 F2 U
    - After R2 B2, 1qt edges will be FH (bad) and RH (good): +1+1+0(+3)
- B2 U L2 B2 U
    - After L2, 1qt edges will be FV (good) and RV (good): +1+0+2(+1)
        - L2 D' L2 F2 B2 U' // no good
- F2 U F2 R2 U
    - After B2 R2, 1qt edges will be FV (good) and RH (good): +1+1+1(+0)
        - B2 R2 U F2 L2 U' // no good
        - B2 R2 D L2 B2 U' // no good

Stop: 10 HTRs done, nothing within goal. This DR's optimal is 14.

### 2c4, scramble 5

`R' U' F U2 D2 R D F L2 U2 F D' L B2 R' D2 B2 R D2 L' F2 L B2 R' U' F`

2c4 6e, goal 14.

Skeleton starting with F2 U' L2 U has RV corners, L=10, 4 spare moves.

- F2 U' L2 U
    - After L2 F2, 1qt edges will be RV (good) and FD (bad): +0+1+0(+3)
        - L2 F2 D L2 U' // no good
    - After F2 U2 B2 R2 F2, 1qt edges will be RV (good) and FH (good): +0+4+0(+0)
        - F2 U2 B2 R2 F2 D' B2 U // no good
    - After B2 U2 B2 L2 F2, 1qt edges will be RV (good) and FH (good): +0+4+0(+0)
        - B2 U2 B2 L2 F2 D' L2 U // no good
- B2 U' B2 U
    - After B2, 1qt edges will be RV (good) and FH (good): +0+0+3(+0)
        - B2 D' L2 B2 R2 L2 U' // no good
        - B2 U' B2 R2 F2 B2 U // no good
    - After B2, 1qt edges will be RV (good) and FH (good): +0+0+4(+0)
        - B2 U F2 B2 U2 F2 R2 U' // no good
        - B2 D R2 L2 U2 L2 F2 U // no good
        - B2 D' L2 B2 U2 R2 L2 U' // no good
        - B2 U' B2 R2 U2 F2 B2 U // no good
- F2 U' R2 U
    - After R2, 1qt edges will be RH (bad) and FH (good), fr=1: +0+0+3(+2)
- B2 U' F2 U
    - After R2 B2 L2 F2, 1qt edges will be RV (good) and FV (good): +0+3+1(+1)
- F2 U' R2 U'
    - After R2 U2 R2, 1qt edges will be RH (bad) and FH (good), fr=1: +0+2+1(+2)
- F2 U' L2 U'
    - After B2 U2 L2 F2, 1qt edges will be RV (good) and FD (bad), fr=1: +0+3+0(+2)
- B2 U' R2 F2 U'
    - After F2, 1qt edges will be RV (good) and FD (bad): +1+0+0(+3)
        - F2 U B2 U' // no good

Stop: 10 HTRs done, nothing within goal. This DR's optimal is 14.

### 2c4, scramble 6

`R' U' F R D2 L B' R' D L' R2 U2 B2 D2 F2 D R2 U' L2 D2 B' U2 F R' U' F`

2c4 4e, goal 14.

Skeleton starting with U R2 U' has FV corners, L=9, 5 spare moves.

- U R2 U'
    - After R2 F2, 1qt edges will be FD (bad) and RV (good): +0+1+1(+3)
        - R2 F2 U' F2 L2 U // no good
        - R2 F2 D' R2 F2 U' // no good
- U L2 U'
    - After R2 F2 B2, 1qt edges will be FV (good) and RH (good): +0+2+2(+0)
        - R2 F2 B2 D R2 F2 B2 U' // no good
    - After L2 U2 F2 R2 F2, 1qt edges will be FV (good) and RV (good): +0+4+0(+1)
        - L2 U2 F2 R2 F2 U L2 U // no good
    - After R2 F2 B2, 1qt edges will be FV (good) and RH (good): +0+2+3(+0)
        - R2 F2 B2 D R2 U2 F2 B2 U // no good
        - R2 F2 B2 D' F2 B2 U2 L2 U' // no good
    - After R2 U2 F2 R2 L2 F2, 1qt edges will be FV (good) and RH (good): +0+5+0(+0)
        - R2 U2 F2 R2 L2 F2 U' R2 U' // no good
    - After R2 U2 B2 R2 L2 B2, 1qt edges will be FV (good) and RH (good): +0+5+0(+0)
        - R2 U2 B2 R2 L2 B2 U' R2 U' // no good
    - After L2 U2 R2 L2 F2 B2, 1qt edges will be FV (good) and RH (good): +0+5+0(+0)
        - L2 U2 R2 L2 F2 B2 U' F2 U' // no good
    - After L2 U2 F2 B2 R2 L2, 1qt edges will be FV (good) and RH (good): +0+5+0(+0)
        - L2 U2 F2 B2 R2 L2 U' F2 U' // no good

Stop: 10 HTRs done, nothing within goal. This DR's optimal is 14.
