# The skeleton/variant meta: example solves

24 Nov 2026

The [skeleton/variant meta](WRITEUP.md), run by a solver on the 34 DRs of [*Advanced DR Bounding Examples*](https://docs.google.com/document/d/1xtvlA3Tg2zkl8H1D98XhLU66gITJ5S-oIPajsn68SOE) and written out the way that doc writes its solves.
Every scramble is a DR on U/D. The goal is 12/13/14 moves from DR to a leave-slice finish for a 2qt/3qt/4qt DR; the 0c0 DRs are solved as 2qt ones, with goal 12.
The sections are the doc's; its 4b3 DRs fall under 4c3 in the write-up, which counts 4a3 and 4b3 together.

Each example goes through the skeletons shortest first, in two passes: the first takes at most 3 variants of each skeleton to HTR (3 on normal and 3 on its inverse), and the second comes back for the rest in the same order. It stops after its second finish within goal, or after 10 HTRs, whichever comes first.

## How to read an example

```
Skeleton starting with F2 U' has FV corners, L=8, 5 spare moves.

- F2 U'
    - After B2 L2, 1qt edges will be FV (good) and RV (good): +0+1+0(+1)
        - B2 L2 U' B2 U B2 L2 U2 R2 L2 // 12
    - After R2 F2 R2 B2, 1qt edges will be FH (bad) and RH (good): +0+3+0(+3)
    - After B2 L2, 1qt edges will be FV (good) and RV (good): +0+1+4(+1)
- B2 U'
    - After L2 B2, 1qt edges will be FV (good) and RV (good): +0+1+1(+1)
        - L2 B2 U' R2 F2 D' // 2 pairs, no good
        - L2 B2 U' L2 B2 U' // 2 pairs, no good
    - After L2 F2, 1qt edges will be FD (bad) and RD (bad): +0+1+1(+5)
- 29 more variants of this skeleton pass the meta, not reached before the stop.

Check inverse. Skeleton starting with (U2 B2 U) has FD corners.
```

- **Skeleton line.** Skeletons come shortest first. A skeleton is named by how it starts (its moves up to 2qt; a 2qt skeleton by its setup), with the corners it leaves at NISS@1qt, its length L and the spare moves G−L.
- **Check inverse.** The skeleton the inverse scramble reads the same solutions on, with the same L. Moves in parentheses are on the inverse. Normal always goes first.
- **Approach to 2qt** (first-level bullet): the moves up to 2qt, with P ≤ 1. Approaches with no extra move come first. A 2qt skeleton has no approach, so its variants are the first level.
- **Variant line.** `After B2 L2` is the setup. The 1qt edges are the F and R edge cases at NISS@1qt as in [*Advanced DR Bounding*](https://docs.google.com/document/d/13F8HonrKJyHjU9EwfiHDRyY4X77vPriYeaVSrh5guq0), each with whether that slice is bad for these corners, and `fr=1` when the F/R parity is odd. Then the extra moves `+P+S+T(+N)`, or `+S+T(+N)` on a 2qt skeleton, where N is the corner-case-aware bound.
- **Moves.** Under a variant, the moves from the setup on (put the approach in front for the whole solution). A finish within goal is written out with its length; anything else stops at HTR with `// no good`. A skeleton's variants are taken in the meta's order across its approaches: fewest P+S+T first, then (P, S, T, N), then most pairs. The ones taken in the second pass are marked `second pass`.
- **Pairs.** `2 pairs` is the number of corner-edge pairs right after the variant's last insertion. It is shown when another variant of the skeleton has the same (P, S, T, N): of those, the one with more pairs goes first.
- **`more variants ... not reached before the stop`.** Variants of the skeleton that pass the meta and were still waiting when the example stopped.
- **A variant line with no moves under it.** A variant the meta does not let through. An approach (on a 2qt skeleton: the skeleton) shows at most 3 failed variants, counting the ones taken to HTR: the one with the smallest S+T, the one with the smallest N and the one with the smallest S+T+N, with ties drawn at random. `left to the inverse` (or `the normal scramble`) means it is only dropped because it comes earlier on the other side (step 4).
- **U or D.** A quarter turn on U and the same turn on D only differ by a turn of both layers, so they are one variant and only one is tried: the one that leaves 2 bad corners rather than 6 and, with 4 bad corners, 0 or 2 bad edges rather than 8 or 6.
- **Finish.** Leave-slice: the U and D layers are solved against each other, which can leave both of them a half turn off the centres.
- **Last line.** Why the example stops, what was found, and the DR's optimal to a leave-slice finish.

A skeleton of 3 or more quarter turns that ends with its last one (HH corners) is gone through twice. First as [*Advanced DR Bounding*](https://docs.google.com/document/d/13F8HonrKJyHjU9EwfiHDRyY4X77vPriYeaVSrh5guq0) suggests: its last quarter turn is made first, on the other side, and the solve goes on from what is left. Then as it stands, under `The same skeleton in full`, for the solutions that go on after that quarter turn.

```
Skeleton starting with R2 U2 F2 U has HH corners, L=10, 3 spare moves. Apply (D) and NISS: DD corners.

- After B2 U2 R2, 1qt edges will be FH (bad) and RD (good): +0+0(+3)
    - B2 U2 R2 U L2 U L2 D2 B2 R2 B2 R2 D // 13
```

- **`Apply (D) and NISS`.** The premove, in parentheses when it is made on the inverse. What is left is a DR with one quarter turn fewer and one move less to spend, and the line names the corners its skeleton leaves. The variants under it are that DR's, with `+S+T(+N)` when 2 quarter turns are left.
- **Moves after a premove.** They are written as turned after the premove, so a setup can sit on other faces than in the skeleton's name. A finish ends with the premove's quarter turn, turned the other way when that saves a U2 before it.

Left out, compared with the doc's own solves: fixable/unfixable, locked and reflected slices, the name of the insertion (a variant is given by its setup and its moves instead), cs parity, and a NISS in the middle of a skeleton.

## The examples at a glance

One row per example: what the meta finds before it stops, and how many HTRs it takes to reach its first finish within goal when nothing stops it. "Best found" is empty when nothing within goal was found, and the last column is empty when the DR has no finish within goal.

| Example | DR | Goal | DR optimal | HTRs done | Finishes within goal | Best found | HTRs to the first finish within goal |
|---|---|---|---|---|---|---|---|
| [4b2, scramble 1](#4b2-scramble-1) | 4b2 8e | 12 | 12 | 5 | 2 | 12 | 4 |
| [4b2, scramble 2](#4b2-scramble-2) | 4b2 2e | 12 | 11 | 10 | 1 | 12 | 1 |
| [4b2, scramble 3](#4b2-scramble-3) | 4b2 4e | 12 | 13 | 10 | 0 |  |  |
| [4b2, scramble 4](#4b2-scramble-4) | 4b2 0e | 12 | 13 | 10 | 0 |  |  |
| [4b2, scramble 5](#4b2-scramble-5) | 4b2 6e | 12 | 12 | 4 | 2 | 12 | 3 |
| [4b2, scramble 6](#4b2-scramble-6) | 4b2 6e | 12 | 12 | 6 | 2 | 12 | 2 |
| [4b3, scramble 1](#4b3-scramble-1) | 4b3 6e | 13 | 13 | 10 | 1 | 13 | 4 |
| [4b3, scramble 2](#4b3-scramble-2) | 4b3 6e | 13 | 14 | 10 | 0 |  |  |
| [4b3, scramble 3](#4b3-scramble-3) | 4b3 4e | 13 | 14 | 10 | 0 |  |  |
| [4b3, scramble 4](#4b3-scramble-4) | 4b3 6e | 13 | 14 | 10 | 0 |  |  |
| [4b3, scramble 5](#4b3-scramble-5) | 4b3 2e | 13 | 13 | 10 | 1 | 13 | 6 |
| [4b3, scramble 6](#4b3-scramble-6) | 4b3 4e | 13 | 14 | 10 | 0 |  |  |
| [4b3, scramble 7](#4b3-scramble-7) | 4b3 4e | 13 | 14 | 10 | 0 |  |  |
| [4b3, scramble 8](#4b3-scramble-8) | 4b3 4e | 13 | 13 | 10 | 1 | 13 | 9 |
| [0c0, scramble 1](#0c0-scramble-1) | 0c0 6e | 12 | 13 | 10 | 0 |  |  |
| [0c0, scramble 2](#0c0-scramble-2) | 0c0 2e | 12 | 11 | 9 | 2 | 12 | 7 |
| [2c3, scramble 1](#2c3-scramble-1) | 2c3 2e | 13 | 12 | 10 | 0 |  | 19 |
| [2c3, scramble 2](#2c3-scramble-2) | 2c3 4e | 13 | 13 | 10 | 0 |  | 12 |
| [2c3, scramble 3](#2c3-scramble-3) | 2c3 2e | 13 | 12 | 4 | 2 | 12 | 1 |
| [2c3, scramble 4](#2c3-scramble-4) | 2c3 2e | 13 | 12 | 10 | 0 |  | 35 |
| [2c3, scramble 5](#2c3-scramble-5) | 2c3 6e | 13 | 13 | 10 | 0 |  | 72 |
| [2c3, scramble 6](#2c3-scramble-6) | 2c3 6e | 13 | 12 | 9 | 2 | 12 | 1 |
| [2c3, scramble 7](#2c3-scramble-7) | 2c3 2e | 13 | 14 | 10 | 0 |  |  |
| [2c3, scramble 8](#2c3-scramble-8) | 2c3 6e | 13 | 13 | 10 | 1 | 13 | 2 |
| [2c3, scramble 9](#2c3-scramble-9) | 2c3 6e | 13 | 13 | 10 | 1 | 13 | 9 |
| [2c3, scramble 10](#2c3-scramble-10) | 2c3 4e | 13 | 14 | 10 | 0 |  |  |
| [2c3, scramble 11](#2c3-scramble-11) | 2c3 4e | 13 | 13 | 10 | 1 | 13 | 5 |
| [2c3, scramble 12](#2c3-scramble-12) | 2c3 6e | 13 | 14 | 10 | 0 |  |  |
| [2c4, scramble 1](#2c4-scramble-1) | 2c4 6e | 14 | 14 | 10 | 0 |  | 221 |
| [2c4, scramble 2](#2c4-scramble-2) | 2c4 6e | 14 | 15 | 10 | 0 |  |  |
| [2c4, scramble 3](#2c4-scramble-3) | 2c4 0e | 14 | 14 | 10 | 0 |  | 16 |
| [2c4, scramble 4](#2c4-scramble-4) | 2c4 2e | 14 | 14 | 10 | 1 | 14 | 4 |
| [2c4, scramble 5](#2c4-scramble-5) | 2c4 6e | 14 | 14 | 10 | 0 |  | 118 |
| [2c4, scramble 6](#2c4-scramble-6) | 2c4 4e | 14 | 14 | 10 | 1 | 14 | 4 |

22 of the 34 DRs have a finish within goal. The meta finds one on 15 of them before it stops, and on 13 of those it finds the DR's optimal. With nothing to stop it, it reaches a finish within goal on 22 of the 22, after 1 to 221 HTRs (median 5.5).

## 4b2

### 4b2, scramble 1

`R' U' F U F R2 F2 L' D2 L2 U2 B2 L' D2 U2 L F D L2 D2 F' L2 U2 R' U' F`

4b2 8e, goal 12.

Skeleton starting with U2 F2 has HH corners, L=5, 7 spare moves.

- After U2 F2, 1qt edges will be RH (good) and FD (bad): +0+3(+3)
    - U2 F2 U F2 R2 F2 R2 D' // 4 pairs, no good
- After U2 B2, 1qt edges will be RH (good) and FD (bad): +0+3(+3)
    - U2 B2 U L2 F2 L2 F2 D' // 4 pairs, no good
- After U2 F2, 1qt edges will be RH (good) and FD (bad): +0+3(+3)
    - U2 F2 U F2 R2 B2 L2 U' // 2 pairs, no good
- 21 more variants of this skeleton pass the meta, not reached before the stop.

Check inverse. Skeleton starting with (U) has FV corners.

- With no setup, 1qt edges will be FV (good) and RV (good): +0+3(+1)
    - (U L2 F2 R2 B2 U' R2 F2 D2 F2 L2 B2) // 2 pairs, 12
    - (U L2 F2 L2 F2 D' R2 F2 U2 L2 B2 R2) // 2 pairs, 12
- 18 more variants of this skeleton pass the meta, not reached before the stop.

Stop: 2 finishes within goal (12, 12), after 5 HTRs. This DR's optimal is 12.

### 4b2, scramble 2

`R' U' F L2 F U' B2 L' F2 R' U2 F2 R2 D2 B U2 F U2 D2 B' R' U2 R' U' F`

4b2 2e, goal 12.

Skeleton starting with F2 has RV corners, L=6, 6 spare moves.

- After R2 L2 B2, 1qt edges will be RV (good) and FD (bad): +2+0(+3)
    - R2 L2 B2 U' B2 U R2 B2 R2 U2 R2 U2 // 12
- After B2 L2 B2 L2, 1qt edges will be RV (good) and FH (good): +3+0(+0)
    - B2 L2 B2 L2 U R2 U // no good
- After R2 L2 B2, 1qt edges will be RV (good) and FD (bad), fr=1: +2+2(+2)
    - R2 L2 B2 U B2 U2 B2 U // 8 pairs, no good
- 1 more variant of this skeleton passes the meta, not reached before the stop.

Check inverse. Skeleton starting with (U2 R2) has FD corners.

- After (U2 B2 L2), 1qt edges will be FV (bad) and RH (good): +1+0(+3)
    - (U2 B2 L2 U L2 U) // no good
- After (U2 R2 F2 B2), 1qt edges will be FH (bad) and RH (good): +2+0(+3)
    - (U2 R2 F2 B2 U' F2 U) // no good
- After (U2 B2 L2), 1qt edges will be FV (bad) and RH (good): +1+2(+3)
    - (U2 B2 L2 U F2 B2 R2 D') // no good
- 2 more variants of this skeleton pass the meta, not reached before the stop.

Skeleton starting with D B2 D has HH corners, L=7, 5 spare moves. Apply (U') and NISS: RD corners.

- U
    - After R2, 1qt edges will be RH (bad) and FH (good): +0+0+0(+3)
        - R2 U R2 U' // no good
    - After R2, 1qt edges will be RH (bad) and FH (good): +0+0+2(+3)
        - R2 U F2 B2 L2 D' // 4 pairs, no good
    - After R2, 1qt edges will be RH (bad) and FH (good), fr=1: +0+0+2(+3)
        - R2 U' R2 U2 R2 U' // 4 pairs, no good
- 10 more variants of this skeleton pass the meta, not reached before the stop.

The same skeleton in full, for the solutions that go on after its last quarter turn.

- D B2 D
    - After L2, 1qt edges will be RH (good) and FH (good): +0+0+3(+0)
        - L2 U B2 L2 B2 L2 U' // 8 pairs, no good
- D F2 U
    - After F2 L2, 1qt edges will be RH (good) and FV (bad), fr=1: +0+1+3(+5)
    - After B2 R2, 1qt edges will be RH (good) and FV (bad): +0+1+4(+3)
- D B2 D'
    - After R2 U2 L2, 1qt edges will be RH (good) and FH (good), fr=1: +0+2+3(+5)
- D F2 U'
    - After R2 U2 B2 R2, 1qt edges will be RH (good) and FV (bad), fr=1: +0+3+1(+5)
    - After F2 L2 F2 U2 B2, 1qt edges will be RH (good) and FD (bad): +0+4+1(+3)
- D L2 B2 D
    - After B2 U2 B2, 1qt edges will be RV (bad) and FD (bad), fr=1: +1+2+0(+6)
- D L2 F2 U
    - After B2 U2 F2, 1qt edges will be RV (bad) and FV (bad), fr=1: +1+2+0(+6)
- D R2 B2 D
    - After F2 U2 F2, 1qt edges will be RV (bad) and FD (bad), fr=1: +1+2+0(+6)
- D R2 F2 U
    - After F2 U2 B2, 1qt edges will be RV (bad) and FV (bad), fr=1: +1+2+0(+6)
- D L2 B2 D'
    - After B2 L2 B2 L2, 1qt edges will be RV (bad) and FH (good): +1+3+0(+3)
    - After B2 U2 F2 B2, 1qt edges will be RV (bad) and FD (bad): +1+3+0(+6)
- D L2 F2 U'
    - After B2 R2 B2 R2, 1qt edges will be RV (bad) and FH (good): +1+3+0(+3)
    - After B2 U2 F2 B2, 1qt edges will be RV (bad) and FV (bad): +1+3+0(+6)
- D R2 B2 D'
    - After F2 R2 F2 R2, 1qt edges will be RV (bad) and FH (good): +1+3+0(+3)
    - After F2 U2 F2 B2, 1qt edges will be RV (bad) and FD (bad): +1+3+0(+6)
- D R2 F2 U'
    - After F2 L2 F2 L2, 1qt edges will be RV (bad) and FH (good): +1+3+0(+3)
- 39 more variants of this skeleton pass the meta, not reached before the stop.

Stop: 10 HTRs done, one finish within goal (12). This DR's optimal is 11.

### 4b2, scramble 3

`R' U' F D' F B D2 B2 U' B' L F2 U F2 D2 F2 D2 R2 B2 L2 F2 D R' U' F`

4b2 4e, goal 12.

Skeleton starting with B2 U2 R2 has HH corners, L=6, 6 spare moves.

- After B2 U2 R2, 1qt edges will be RH (good) and FH (good): +0+1(+0)
    - B2 U2 R2 U' F2 R2 U' // 8 pairs, no good
    - B2 U2 R2 U' B2 L2 D' // 8 pairs, no good
- After U2 R2 U2 B2, 1qt edges will be RH (good) and FH (good): +1+1(+0)
    - U2 R2 U2 B2 U F2 R2 U' // 8 pairs, no good
- 117 more variants of this skeleton pass the meta, not reached before the stop.

Skeleton starting with R2 U D has HH corners, L=7, 5 spare moves. Apply (U') and NISS: RD corners.

- L2 U'
    - After R2 L2, 1qt edges will be RV (bad) and FH (good): +0+2+3(+3)
- R2 U'
    - After F2 B2, 1qt edges will be RH (bad) and FD (good): +0+2+3(+3)

Check inverse. Skeleton starting with (U' L2 D') has RD corners.

- (U' L2 D')
    - After (R2), 1qt edges will be RV (bad) and FV (bad), fr=1: +0+0+5(+5)
- (U' R2 U')
    - After (L2), 1qt edges will be RV (bad) and FV (bad), fr=1: +0+0+5(+5)

Skeleton starting with F2 D U has HH corners, L=7, 5 spare moves. Apply (U') and NISS: RD corners.

- B2 U'
    - After F2 B2 L2 B2 R2, 1qt edges will be RD (good) and FD (good): +0+5+0(+1)
    - After F2 U2 F2 U2 F2, 1qt edges will be RD (good) and FV (bad), fr=1: +0+5+0(+5)
- F2 D'
    - After F2 B2 R2 F2 L2, 1qt edges will be RD (good) and FD (good): +0+5+0(+1)
    - After F2 L2 B2 R2 L2, 1qt edges will be RV (bad) and FV (bad): +0+5+0(+5)
- L2 F2 D
    - After R2 F2 L2, 1qt edges will be RD (good) and FH (good): +1+3+0(+0)
        - R2 F2 L2 U' R2 U' // 2 pairs, no good
- R2 B2 U'
    - After L2 F2 R2, 1qt edges will be RD (good) and FH (good): +1+3+0(+0)
        - L2 F2 R2 U F2 U // 2 pairs, no good
- R2 F2 D'
    - After R2 B2 L2, 1qt edges will be RD (good) and FH (good): +1+3+0(+0)
        - R2 B2 L2 U R2 U // 2 pairs, no good
- 9 more variants of this skeleton pass the meta, not reached before the stop.

Check inverse. Skeleton starting with (U' L2 D) has FD corners.

- (U' L2 D)
    - After (L2), 1qt edges will be FH (bad) and RV (bad): +0+0+5(+5)
- (U' R2 U)
    - After (R2), 1qt edges will be FH (bad) and RV (bad): +0+0+5(+5)

Skeleton starting with U D has HH corners, L=8, 4 spare moves. Apply (U') and NISS: RD corners.

- U
    - After R2 F2 R2, 1qt edges will be RD (good) and FH (good): +0+3+0(+0)
        - R2 F2 R2 U R2 U2 B2 U // 1 pair, no good
        - R2 F2 R2 U' B2 U2 R2 U' // 1 pair, no good
    - After L2 F2 L2, 1qt edges will be RD (good) and FH (good): +0+3+0(+0)
        - L2 F2 L2 U R2 U2 B2 U // 1 pair, no good
- U'
    - After R2 L2, 1qt edges will be RH (bad) and FH (good): +0+2+0(+3)
- 21 more variants of this skeleton pass the meta, not reached before the stop.

Skeleton starting with (U' R2 U) on inverse has HH corners, L=8, 4 spare moves. Apply U and NISS: HH corners.

- (U')
    - After (R2), 1qt edges will be RD (bad) and FH (good): +0+0+1(+3)
        - (R2 U' F2 U2 F2 R2 D) // 2 pairs, no good
    - After (R2), 1qt edges will be RD (bad) and FH (good), fr=1: +0+0+1(+5)
    - After (L2), 1qt edges will be RH (good) and FD (bad): +0+0+2(+3)
- (U)
    - After (R2 U2 L2), 1qt edges will be RH (good) and FD (bad): +0+2+0(+3)
- 19 more variants of this skeleton pass the meta, not reached before the stop.

Stop: 10 HTRs done, nothing within goal. This DR's optimal is 13, over the goal.

### 4b2, scramble 4

`R' U' F U2 R2 F D R' L' U2 F' L2 U' L2 B2 U' R2 B2 D R2 L2 F D' R' U' F`

4b2 0e, goal 12.

Skeleton starting with F2 has RV corners, L=6, 6 spare moves.

- After B2, 1qt edges will be RD (bad) and FD (bad): +0+3(+5)

Check inverse. Skeleton starting with (U2 R2) has FD corners.

- After (U2 R2), 1qt edges will be FV (bad) and RV (bad): +0+3(+5)

Skeleton starting with F2 U' R2 U has HH corners, L=7, 5 spare moves. Apply (U) and NISS: HH corners.

- B2 U
    - After B2 U2 L2 F2, 1qt edges will be RD (bad) and FV (bad), fr=1: +0+3+1(+6)
    - After B2 L2 F2 U2 L2, 1qt edges will be RH (good) and FV (bad): +0+4+1(+3)
- F2 U
    - After R2 U2 B2 R2, 1qt edges will be RV (bad) and FD (bad), fr=1: +0+3+1(+6)
    - After R2 B2 R2 U2 B2, 1qt edges will be RV (bad) and FH (good): +0+4+1(+3)
- R2 F2 U
    - After R2 F2, 1qt edges will be RD (bad) and FV (bad): +1+1+0(+6)
    - After F2 R2 F2 R2, 1qt edges will be RH (good) and FH (good): +1+3+0(+0)
        - F2 R2 F2 R2 U B2 U // 6 pairs, no good
- L2 B2 D
    - After R2 L2 B2, 1qt edges will be RH (good) and FD (bad): +1+2+0(+3)
    - After B2 L2 B2 L2, 1qt edges will be RH (good) and FH (good): +1+3+0(+0)
        - B2 L2 B2 L2 U R2 U // 6 pairs, no good
- L2 F2 D
    - After R2 F2 B2, 1qt edges will be RD (bad) and FH (good): +1+2+0(+3)
    - After L2 B2 L2 B2, 1qt edges will be RH (good) and FH (good): +1+3+0(+0)
        - L2 B2 L2 B2 U R2 U // 6 pairs, no good
- R2 B2 U'
    - After L2 U2 R2, 1qt edges will be RV (bad) and FH (good), fr=1: +1+2+0(+5)
    - After R2 L2 U2 R2, 1qt edges will be RV (bad) and FH (good): +1+3+0(+3)
    - After L2 U2 R2, 1qt edges will be RV (bad) and FH (good): +1+2+2(+3)
- L2 B2 D'
    - After L2 B2 U2 L2, 1qt edges will be RV (bad) and FV (bad), fr=1: +1+3+0(+6)
    - After F2 R2 F2 U2 R2, 1qt edges will be RV (bad) and FH (good): +1+4+0(+3)
- L2 F2 D'
    - After R2 U2 F2 L2, 1qt edges will be RD (bad) and FV (bad), fr=1: +1+3+0(+6)
    - After R2 F2 L2 U2 F2, 1qt edges will be RH (good) and FV (bad): +1+4+0(+3)
- R2 F2 U'
    - After B2 U2 R2 F2, 1qt edges will be RD (bad) and FV (bad), fr=1: +1+3+0(+6)
    - After B2 L2 B2 U2 R2, 1qt edges will be RD (bad) and FH (good): +1+4+0(+3)
- 25 more variants of this skeleton pass the meta, not reached before the stop.

The same skeleton in full, for the solutions that go on after its last quarter turn.

- B2 U' F2 U
    - After B2, 1qt edges will be RD (bad) and FV (bad): +0+0+3(+6)
    - After R2 B2, 1qt edges will be RH (good) and FV (bad): +0+1+3(+3)
- F2 U' R2 U
    - After B2, 1qt edges will be RD (bad) and FV (bad): +0+0+3(+6)
    - After R2 F2, 1qt edges will be RH (good) and FV (bad): +0+1+3(+3)
- B2 U' B2 D
    - After F2, 1qt edges will be RH (good) and FD (bad): +0+0+5(+3)
- F2 U' L2 D
    - After B2, 1qt edges will be RH (good) and FD (bad): +0+0+5(+3)
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

Skeleton starting with D B2 D has RD corners, L=8, 4 spare moves.

- D B2 D
    - After L2 U2 R2 L2, 1qt edges will be RV (bad) and FV (bad), fr=1: +0+3+0(+5)
    - After B2 L2 F2 R2 F2, 1qt edges will be RD (good) and FH (good), fr=1: +0+4+0(+3)
- D F2 D
    - After L2 B2, 1qt edges will be RV (bad) and FH (good), fr=1: +0+1+0(+5)
    - After L2 B2, 1qt edges will be RV (bad) and FH (good): +0+1+2(+3)
- D B2 D'
    - After L2 U2 L2, 1qt edges will be RV (bad) and FV (bad): +0+2+0(+5)
    - After B2 L2 U2 R2 F2, 1qt edges will be RV (bad) and FH (good): +0+4+0(+3)
- D F2 D'
    - After F2 U2 R2 F2, 1qt edges will be RV (bad) and FH (good): +0+3+0(+3)
    - After R2 L2 B2 U2 B2, 1qt edges will be RD (good) and FH (good): +0+4+0(+0)
        - R2 L2 B2 U2 B2 U' B2 U' // 4 pairs, no good
    - After F2 U2 B2 R2 L2, 1qt edges will be RD (good) and FH (good): +0+4+0(+0)
        - F2 U2 B2 R2 L2 U' F2 U' // 4 pairs, no good

Check inverse. Skeleton starting with (R2 U' R2 U) has HH corners. Apply D and NISS: FD corners.

- (R2 U')
    - After (R2 B2 R2 B2), 1qt edges will be FH (bad) and RH (good), fr=1: +0+3+0(+3)
- (L2 D')
    - After (L2 F2 B2), 1qt edges will be FH (bad) and RV (bad), fr=1: +0+2+0(+5)
    - After (R2 B2 R2 B2), 1qt edges will be FH (bad) and RH (good), fr=1: +0+3+0(+3)
- (R2 U)
    - After (R2 U2 L2), 1qt edges will be FH (bad) and RV (bad): +0+2+0(+5)
- (L2 D)
    - After (L2 U2 F2 R2), 1qt edges will be FV (bad) and RV (bad): +0+3+0(+5)
- (B2 R2 U)
    - After (R2 F2), 1qt edges will be FD (good) and RV (bad), fr=1: +1+1+0(+3)
- (F2 L2 D)
    - After (L2 F2), 1qt edges will be FV (bad) and RD (good), fr=1: +1+1+0(+3)
- (B2 L2 D)
    - After (R2 L2 B2), 1qt edges will be FD (good) and RH (good), fr=1: +1+2+0(+2)
- (F2 R2 U)
    - After (R2 L2 B2), 1qt edges will be FV (bad) and RH (good), fr=1: +1+2+0(+3)
- (F2 L2 D')
    - After (L2 F2 U2 R2), 1qt edges will be FD (good) and RD (good): +1+3+0(+1)
- (F2 R2 U')
    - After (R2 B2 U2 L2), 1qt edges will be FD (good) and RD (good): +1+3+0(+1)
- (B2 R2 U')
    - After (B2 U2 R2 F2), 1qt edges will be FD (good) and RV (bad): +1+3+0(+3)
    - After (R2 F2 U2 R2), 1qt edges will be FV (bad) and RV (bad): +1+3+0(+5)
- (B2 L2 D')
    - After (L2 B2 U2 L2), 1qt edges will be FV (bad) and RV (bad): +1+3+0(+5)

The same skeleton in full, for the solutions that go on after its last quarter turn.

- (L2 D' L2 D)
    - After (F2 U2 F2 B2), 1qt edges will be RH (good) and FD (bad), fr=1: +0+3+0(+5)
- (R2 U' L2 U)
    - After (B2 U2 F2 B2), 1qt edges will be RH (good) and FD (bad), fr=1: +0+3+0(+5)
- (L2 D' R2 D)
    - After (F2 L2), 1qt edges will be RD (bad) and FD (bad), fr=1: +0+1+0(+6)
    - After (L2 F2 L2 F2), 1qt edges will be RH (good) and FV (bad), fr=1: +0+3+0(+5)
- (R2 U' R2 U)
    - After (B2 L2), 1qt edges will be RD (bad) and FD (bad), fr=1: +0+1+0(+6)
    - After (B2 R2 B2 L2 F2), 1qt edges will be RH (good) and FD (bad), fr=1: +0+4+0(+5)
- (L2 D' L2 D')
    - After (F2 U2 F2), 1qt edges will be RH (good) and FD (bad): +0+2+0(+3)
- (R2 U' L2 U')
    - After (B2 U2 F2), 1qt edges will be RH (good) and FD (bad): +0+2+0(+3)
- (L2 D' R2 D')
    - After (F2 L2 U2 B2), 1qt edges will be RV (bad) and FD (bad): +0+3+0(+6)
    - After (R2 B2 R2 U2 B2), 1qt edges will be RH (good) and FD (bad), fr=1: +0+4+0(+5)
- (R2 U' R2 U')
    - After (R2 U2 B2 L2), 1qt edges will be RD (bad) and FD (bad): +0+3+0(+6)
    - After (R2 F2 R2 U2 B2), 1qt edges will be RH (good) and FD (bad), fr=1: +0+4+0(+5)
- (B2 L2 D F2 D')
    - After (R2 B2), 1qt edges will be RD (bad) and FV (bad), fr=1: +1+1+0(+6)
- (B2 R2 U B2 U')
    - After (R2 F2), 1qt edges will be RD (bad) and FV (bad), fr=1: +1+1+0(+6)
- (F2 L2 D B2 D')
    - After (L2 F2), 1qt edges will be RD (bad) and FV (bad), fr=1: +1+1+0(+6)
- (F2 R2 U F2 U')
    - After (L2 B2), 1qt edges will be RD (bad) and FV (bad), fr=1: +1+1+0(+6)
- (B2 L2 D B2 D)
    - After (R2 U2 R2), 1qt edges will be RD (bad) and FD (bad): +1+2+0(+6)
- (B2 R2 U F2 U)
    - After (R2 U2 L2), 1qt edges will be RD (bad) and FD (bad): +1+2+0(+6)
- (F2 L2 D F2 D)
    - After (L2 U2 L2), 1qt edges will be RD (bad) and FD (bad): +1+2+0(+6)
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

Skeleton starting with (U2 R2 U R2 U') on inverse has HH corners, L=8, 4 spare moves. Apply D and NISS: HH corners.

- (U2 L2 U)
    - After (F2), 1qt edges will be RH (good) and FV (bad), fr=1: +0+0+3(+5)
    - After (B2), 1qt edges will be RD (bad) and FH (good): +0+0+4(+3)
- (U2 R2 U)
    - After (R2), 1qt edges will be RH (good) and FD (bad), fr=1: +0+0+3(+5)
    - After (L2), 1qt edges will be RV (bad) and FH (good): +0+0+4(+3)
- (U2 L2 U')
    - After (B2 U2 F2), 1qt edges will be RH (good) and FV (bad), fr=1: +0+2+1(+5)
- (U2 R2 U')
    - After (L2 U2 L2), 1qt edges will be RV (bad) and FH (good), fr=1: +0+2+1(+5)
- (U2 F2 R2 D')
    - After (F2 L2), 1qt edges will be RD (bad) and FV (bad): +1+1+0(+6)
    - After (L2 F2 L2 F2), 1qt edges will be RH (good) and FH (good): +1+3+0(+0)
        - (L2 F2 L2 F2 U' B2 U') // 6 pairs, no good
- (U2 B2 L2 U')
    - After (F2 B2 R2), 1qt edges will be RV (bad) and FH (good): +1+2+0(+3)
    - After (R2 B2 R2 B2), 1qt edges will be RH (good) and FH (good): +1+3+0(+0)
        - (R2 B2 R2 B2 U' R2 U') // 6 pairs, no good
- (U2 B2 R2 U')
    - After (F2 R2 L2), 1qt edges will be RH (good) and FV (bad): +1+2+0(+3)
    - After (B2 R2 B2 R2), 1qt edges will be RH (good) and FH (good): +1+3+0(+0)
        - (B2 R2 B2 R2 U' R2 U') // 6 pairs, no good
- (U2 F2 L2 D)
    - After (B2 U2 B2), 1qt edges will be RH (good) and FD (bad), fr=1: +1+2+0(+5)
    - After (F2 B2 U2 B2), 1qt edges will be RH (good) and FD (bad): +1+3+0(+3)
- (U2 B2 L2 U)
    - After (B2 R2 U2 F2), 1qt edges will be RD (bad) and FD (bad), fr=1: +1+3+0(+6)
- (U2 B2 R2 U)
    - After (F2 U2 R2 F2), 1qt edges will be RD (bad) and FV (bad), fr=1: +1+3+0(+6)
- (U2 F2 R2 D)
    - After (R2 U2 B2 R2), 1qt edges will be RD (bad) and FV (bad), fr=1: +1+3+0(+6)
- 1 more variant of this skeleton passes the meta, not reached before the stop.

The same skeleton in full, for the solutions that go on after its last quarter turn.

- (U2 L2 U F2 U')
    - After (L2), 1qt edges will be RD (bad) and FV (bad): +0+0+3(+6)
    - After (B2 L2), 1qt edges will be RD (bad) and FH (good): +0+1+3(+3)
- (U2 R2 U R2 U')
    - After (L2), 1qt edges will be RD (bad) and FV (bad): +0+0+3(+6)
    - After (B2 R2), 1qt edges will be RD (bad) and FH (good): +0+1+3(+3)
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
    - After B2 L2 F2, 1qt edges will be RH (bad) and FD (bad): +0+3+0(+5)
- B2 U' L2 U'
    - After L2 F2 R2, 1qt edges will be RD (bad) and FH (good): +0+3+0(+3)
- B2 U' R2 U
    - After R2 F2 L2, 1qt edges will be RD (bad) and FV (good): +0+3+0(+3)
- B2 U' R2 U'
    - After B2 R2 F2, 1qt edges will be RV (good) and FD (bad): +0+3+0(+3)
- F2 U' B2 U
    - After L2 B2 R2, 1qt edges will be RD (bad) and FV (good): +0+3+0(+3)
    - After B2 R2 F2, 1qt edges will be RH (bad) and FD (bad): +0+3+0(+5)
- F2 U' B2 U'
    - After L2 B2 R2, 1qt edges will be RD (bad) and FH (good): +0+3+0(+3)
- F2 U' F2 U
    - After L2 F2 R2, 1qt edges will be RD (bad) and FV (good): +0+3+0(+3)
    - After B2 L2 F2, 1qt edges will be RH (bad) and FD (bad): +0+3+0(+5)
- F2 U' F2 U'
    - After L2 F2 R2, 1qt edges will be RD (bad) and FH (good): +0+3+0(+3)

Check inverse. Skeleton starting with (U2 L2 U L2 U) has FD corners.

- (U2 L2 U L2 U)
    - After (R2 B2 L2), 1qt edges will be FD (good) and RV (bad): +0+3+0(+3)
- (U2 L2 U L2 U')
    - After (B2 L2 F2), 1qt edges will be FV (bad) and RD (good): +0+3+0(+3)
    - After (L2 F2 R2), 1qt edges will be FH (bad) and RV (bad): +0+3+0(+5)
- (U2 L2 U R2 U)
    - After (B2 R2 F2), 1qt edges will be FV (bad) and RH (good): +0+3+0(+3)
- (U2 L2 U R2 U')
    - After (B2 R2 F2), 1qt edges will be FV (bad) and RD (good): +0+3+0(+3)
- (U2 R2 U B2 U)
    - After (L2 B2 R2), 1qt edges will be FD (good) and RV (bad): +0+3+0(+3)
- (U2 R2 U B2 U')
    - After (F2 L2 B2), 1qt edges will be FV (bad) and RD (good): +0+3+0(+3)
- (U2 R2 U F2 U)
    - After (B2 L2 F2), 1qt edges will be FV (bad) and RH (good): +0+3+0(+3)
- (U2 R2 U F2 U')
    - After (F2 R2 B2), 1qt edges will be FV (bad) and RD (good): +0+3+0(+3)
    - After (L2 F2 R2), 1qt edges will be FH (bad) and RV (bad): +0+3+0(+5)

Skeleton starting with B2 U' F2 U has FV corners, L=9, 3 spare moves.

- B2 U' F2 U
    - After R2, 1qt edges will be FD (bad) and RH (good): +0+0+3(+3)
- F2 U' R2 U
    - After L2, 1qt edges will be FD (bad) and RH (good): +0+0+3(+3)

Skeleton starting with L2 D' L2 D' has RD corners, L=9, 3 spare moves.

- L2 D' L2 D'
    - After B2 R2 L2, 1qt edges will be RH (bad) and FH (good), fr=1: +0+2+0(+5)
- R2 U' L2 U'
    - After F2 R2 L2, 1qt edges will be RH (bad) and FH (good), fr=1: +0+2+0(+5)
- L2 D' R2 D'
    - After F2 B2 R2, 1qt edges will be RV (bad) and FV (bad), fr=1: +0+2+0(+5)
- R2 U' R2 U'
    - After F2 B2 R2, 1qt edges will be RV (bad) and FV (bad), fr=1: +0+2+0(+5)
- L2 D' R2 D
    - After B2 R2 U2 B2, 1qt edges will be RD (good) and FH (good): +0+3+0(+0)
        - B2 R2 U2 B2 U' R2 U' // 4 pairs, no good
- R2 U' R2 U
    - After F2 R2 U2 B2, 1qt edges will be RD (good) and FH (good): +0+3+0(+0)
        - F2 R2 U2 B2 U' F2 U' // 5 pairs, no good
- L2 D' L2 D
    - After B2 U2 R2 F2, 1qt edges will be RV (bad) and FH (good): +0+3+0(+3)
- R2 U' L2 U
    - After F2 U2 L2 F2, 1qt edges will be RV (bad) and FH (good): +0+3+0(+3)

Stop: 10 HTRs done, nothing within goal. This DR's optimal is 13, over the goal.

### 4b2, scramble 5

`R' U' F D F2 D2 L2 R B2 U2 R D2 L' U2 R2 F2 D' U2 L' F U' L' F R' U' F`

4b2 6e, goal 12.

Skeleton starting with U2 F2 has FV corners, L=7, 5 spare moves.

- After U2 L2 B2, 1qt edges will be FV (good) and RV (good), fr=1: +1+0(+2)
    - U2 L2 B2 U R2 D' // no good
- After L2 B2 U2 L2, 1qt edges will be FV (good) and RH (good): +2+0(+0)
    - L2 B2 U2 L2 U' R2 D // no good
- After B2 U2 L2 B2, 1qt edges will be FV (good) and RV (good): +2+0(+1)
    - B2 U2 L2 B2 U' R2 D B2 R2 U2 R2 L2 // 12
- 4 more variants of this skeleton pass the meta, not reached before the stop.

Check inverse. Skeleton starting with (U2 B2) has FV corners.

- After (U2 B2), 1qt edges will be FD (bad) and RV (good), fr=1: +0+0(+2)
    - (U2 B2 U B2 D' R2 B2 R2 F2 L2 U2 F2) // 12
- After (F2 U2 B2), 1qt edges will be FD (bad) and RV (good): +1+2(+3)
- After (U2 B2), 1qt edges will be FD (bad) and RV (good), fr=1: +0+5(+2)
- 9 more variants of this skeleton pass the meta, not reached before the stop.

Stop: 2 finishes within goal (12, 12), after 4 HTRs. This DR's optimal is 12.

### 4b2, scramble 6

`R' U' F D2 B' U' F2 B' U' L F2 R2 U2 L2 U2 F R2 F2 B R2 U2 R U2 R' U' F`

4b2 6e, goal 12.

Skeleton starting with L2 has RV corners, L=6, 6 spare moves.

- After R2 B2 L2 B2, 1qt edges will be RV (good) and FH (good), fr=1: +3+0(+1)
    - R2 B2 L2 B2 U B2 D' // 4 pairs, no good
- After U2 R2 U2 L2, 1qt edges will be RV (good) and FV (good): +3+0(+1)
    - U2 R2 U2 L2 U B2 D R2 F2 U2 F2 B2 // 2 pairs, 12
- After B2 L2 F2 B2, 1qt edges will be RD (bad) and FV (good), fr=1: +3+0(+2)
    - B2 L2 F2 B2 U B2 D' // 3 pairs, no good
- 22 more variants of this skeleton pass the meta, not reached before the stop.

Check inverse. Skeleton starting with (U2 L2) has RD corners.

- After (R2 U2 L2), 1qt edges will be RH (bad) and FH (good): +1+0(+3)
    - (R2 U2 L2 U' F2 D) // no good
- After (B2 R2 U2 F2), 1qt edges will be RD (good) and FD (good): +2+0(+1)
    - (B2 R2 U2 F2 U L2 D) // no good
- After (R2 U2 L2), 1qt edges will be RH (bad) and FH (good): +1+2(+3)
    - (R2 U2 L2 U' R2 L2 B2 U' B2 R2 B2 L2) // 12
- 6 more variants of this skeleton pass the meta, not reached before the stop.

Stop: 2 finishes within goal (12, 12), after 6 HTRs. This DR's optimal is 12.

## 4b3

### 4b3, scramble 1

`R' U' F D R B2 R B2 R' B2 R' U2 B2 R B2 F L' R B U R' U F2 R' U' F`

4b3 6e, goal 13.

Skeleton starting with D' has RV corners, L=9, 4 spare moves.

- D'
    - After L2, 1qt edges will be RD (bad) and FV (good), fr=1: +0+0+3(+2)

Check inverse. Skeleton starting with (U2 R2 D) has HH corners. Apply D' and NISS: RD corners.

- After (U2 R2), 1qt edges will be RH (bad) and FD (good): +0+3(+3)

The same skeleton in full, for the solutions that go on after its last quarter turn.

- (U2 R2 D)
    - After (F2 L2 U2 R2), 1qt edges will be RV (bad) and FV (bad), fr=1: +0+1+0(+6)
    - After (R2 B2 U2 R2 L2 B2), 1qt edges will be RH (good) and FD (bad): +0+3+0(+3)
    - After (R2 U2 F2), 1qt edges will be RH (good) and FD (bad): +0+0+4(+3)
- (U2 R2 D')
    - After (L2 F2 R2 F2 U2 L2), 1qt edges will be RH (good) and FH (good): +0+3+0(+0)
        - (L2 F2 R2 F2 U2 L2 U R2 U') // 6 pairs, no good
    - After (R2 B2 L2 F2 U2 R2), 1qt edges will be RH (good) and FH (good): +0+3+0(+0)
        - (R2 B2 L2 F2 U2 R2 U F2 U') // 6 pairs, no good
    - After (L2 F2 R2 U2 L2 U2 F2), 1qt edges will be RH (good) and FH (good): +0+4+0(+0)
        - (L2 F2 R2 U2 L2 U2 F2 U' R2 U') // 6 pairs, no good
- (U2 L2 U)
    - After (L2 B2 U2 B2), 1qt edges will be RH (good) and FD (bad): +0+1+1(+3)
    - After (L2 B2 U2 F2), 1qt edges will be RV (bad) and FV (bad): +0+1+1(+6)
- (U2 L2 U')
    - After (F2 U2 L2), 1qt edges will be RV (bad) and FV (bad): +0+0+3(+6)
    - After (B2 L2 U2 B2 L2), 1qt edges will be RH (good) and FV (bad): +0+2+1(+3)
    - After (F2 L2 U2 F2 B2 L2), 1qt edges will be RH (good) and FD (bad): +0+3+1(+3)
- (R2 U2 R2 D)
    - After (L2 U2 F2), 1qt edges will be RV (bad) and FD (bad), fr=1: +1+0+0(+6)
    - After (B2 U2 F2 R2), 1qt edges will be RH (good) and FD (bad): +1+1+0(+3)
- (R2 U2 R2 D')
    - After (B2 U2 R2), 1qt edges will be RV (bad) and FD (bad), fr=1: +1+0+0(+6)
    - After (F2 B2 L2 U2 F2), 1qt edges will be RH (good) and FV (bad): +1+2+0(+3)
- (U2 B2 L2 U)
    - After (F2 U2 L2), 1qt edges will be RD (bad) and FD (bad): +1+0+0(+6)
- (U2 B2 L2 U')
    - After (L2 U2 F2), 1qt edges will be RD (bad) and FD (bad): +1+0+0(+6)
- (L2 U2 R2 D')
    - After (L2 U2 L2 F2), 1qt edges will be RH (good) and FD (bad): +1+1+0(+3)
- (U2 F2 R2 D')
    - After (B2 U2 B2 R2), 1qt edges will be RD (bad) and FV (bad), fr=1: +1+1+0(+6)
- (L2 U2 R2 D)
    - After (B2 U2 L2), 1qt edges will be RV (bad) and FD (bad): +1+0+2(+6)
    - After (R2 U2 B2 R2 L2), 1qt edges will be RH (good) and FV (bad), fr=1: +1+2+0(+5)
- (U2 F2 R2 D)
    - After (B2 U2 F2 B2 R2), 1qt edges will be RV (bad) and FV (bad): +1+2+0(+6)
- (L2 U2 L2 U)
    - After (R2 F2 U2 F2), 1qt edges will be RH (good) and FV (bad): +1+1+1(+3)
    - After (R2 F2 U2 B2), 1qt edges will be RV (bad) and FD (bad): +1+1+1(+6)
- (L2 U2 L2 U')
    - After (B2 L2 U2 L2), 1qt edges will be RH (good) and FV (bad): +1+1+1(+3)
- (R2 U2 L2 U')
    - After (R2 F2 U2 B2), 1qt edges will be RH (good) and FV (bad), fr=1: +1+1+1(+5)
    - After (R2 F2 U2 F2), 1qt edges will be RV (bad) and FD (bad), fr=1: +1+1+1(+6)
- (U2 B2 R2 U)
    - After (L2 B2 U2 F2), 1qt edges will be RV (bad) and FV (bad), fr=1: +1+1+1(+6)
- (U2 B2 R2 U')
    - After (F2 L2 U2 L2), 1qt edges will be RV (bad) and FV (bad), fr=1: +1+1+1(+6)
- (U2 F2 L2 U)
    - After (R2 B2 U2 B2), 1qt edges will be RV (bad) and FV (bad): +1+1+1(+6)
- 5 more variants of this skeleton pass the meta, not reached before the stop.

Skeleton starting with R2 U2 F2 U has HH corners, L=10, 3 spare moves. Apply (D) and NISS: DD corners.

- After B2 U2 R2, 1qt edges will be FH (bad) and RD (good): +0+0(+3)
    - B2 U2 R2 U L2 U L2 D2 B2 R2 B2 R2 D // 13
- After R2 U2 R2 B2, 1qt edges will be FV (good) and RD (good): +1+0(+0)
    - R2 U2 R2 B2 U' L2 U' // no good
- After U2 R2 U2 B2, 1qt edges will be FH (bad) and RD (good): +1+0(+3)
- After F2 R2 U2 F2 L2, 1qt edges will be FV (good) and RD (good): +2+0(+0)
    - F2 R2 U2 F2 L2 U B2 U // 4 pairs, no good
- 9 more variants of this skeleton pass the meta, not reached before the stop.

The same skeleton in full, for the solutions that go on after its last quarter turn.

- L2 U2 B2 U
    - After L2, 1qt edges will be RV (bad) and FV (bad), fr=1: +0+0+0(+6)
    - After R2, 1qt edges will be RH (good) and FD (bad): +0+0+1(+3)
    - After L2 U2 F2 B2, 1qt edges will be RH (good) and FD (bad): +0+3+0(+3)
- B2 U2 L2 U
    - After B2, 1qt edges will be RV (bad) and FH (good): +0+0+1(+3)
- L2 U2 F2 D
    - After R2, 1qt edges will be RV (bad) and FH (good): +0+0+3(+3)
- F2 U2 L2 U
    - After R2, 1qt edges will be RD (bad) and FD (bad), fr=1: +0+0+3(+6)
- R2 U2 B2 U
    - After F2, 1qt edges will be RD (bad) and FV (bad), fr=1: +0+0+3(+6)
- F2 U2 R2 U
    - After L2 B2, 1qt edges will be RD (bad) and FH (good): +0+1+1(+3)
    - After L2 F2, 1qt edges will be RV (bad) and FV (bad), fr=1: +0+1+1(+6)
- B2 U2 L2 U'
    - After F2 U2 B2, 1qt edges will be RV (bad) and FH (good): +0+2+0(+3)
    - After F2 U2 F2, 1qt edges will be RD (bad) and FV (bad), fr=1: +0+2+0(+6)
    - After F2 U2 L2 B2, 1qt edges will be RD (bad) and FH (good): +0+3+0(+3)
- L2 U2 B2 U'
    - After R2 U2 R2, 1qt edges will be RH (good) and FD (bad), fr=1: +0+2+1(+5)
    - After R2 L2 U2 R2, 1qt edges will be RH (good) and FD (bad): +0+3+0(+3)
- F2 U2 R2 U'
    - After F2 U2 L2 B2, 1qt edges will be RD (bad) and FH (good): +0+3+0(+3)
- F2 U2 B2 R2 U'
    - After L2, 1qt edges will be RH (good) and FH (good): +1+0+0(+0)
        - L2 U F2 U2 L2 D // 1 pair, no good
        - L2 U' L2 U2 F2 D' // 1 pair, no good
    - After R2, 1qt edges will be RV (bad) and FV (bad): +1+0+0(+6)
- L2 F2 U2 B2 U'
    - After L2, 1qt edges will be RH (good) and FV (bad): +1+0+0(+3)
- B2 L2 U2 L2 U'
    - After F2, 1qt edges will be RD (bad) and FV (bad), fr=1: +1+0+0(+6)
    - After B2, 1qt edges will be RV (bad) and FH (good): +1+0+1(+3)
- R2 U2 R2 B2 U'
    - After R2, 1qt edges will be RV (bad) and FV (bad), fr=1: +1+0+0(+6)
    - After L2, 1qt edges will be RH (good) and FH (good): +1+0+1(+0)
        - L2 U R2 F2 U2 F2 U // 8 pairs, no good
- U2 B2 U2 L2 U'
    - After R2, 1qt edges will be RH (good) and FD (bad), fr=1: +1+0+0(+5)
    - After R2, 1qt edges will be RH (good) and FD (bad): +1+0+1(+3)
- B2 R2 U2 L2 U'
    - After F2, 1qt edges will be RD (bad) and FH (good): +1+0+1(+3)
    - After F2, 1qt edges will be RD (bad) and FH (good), fr=1: +1+0+1(+5)
- F2 U2 F2 L2 U'
    - After F2, 1qt edges will be RV (bad) and FH (good): +1+0+1(+3)
    - After F2, 1qt edges will be RV (bad) and FH (good), fr=1: +1+0+1(+5)
- L2 B2 U2 B2 U'
    - After R2, 1qt edges will be RH (good) and FD (bad): +1+0+1(+3)
- R2 U2 L2 F2 U'
    - After F2, 1qt edges will be RV (bad) and FH (good): +1+0+1(+3)
    - After F2, 1qt edges will be RV (bad) and FH (good), fr=1: +1+0+1(+5)
- U2 L2 U2 B2 U'
    - After B2, 1qt edges will be RV (bad) and FH (good): +1+0+1(+3)
- 11 more variants of this skeleton pass the meta, not reached before the stop.

Check inverse. Skeleton starting with (D') has DD corners.

- (D')
    - After (B2 R2 U2 L2), 1qt edges will be FV (good) and RV (good): +0+1+0(+1)
        - (B2 R2 U2 L2 U' B2 U') // no good
- 12 more variants of this skeleton pass the meta, not reached before the stop.

Stop: 10 HTRs done, one finish within goal (13). This DR's optimal is 13.

### 4b3, scramble 2

`R' U' F R2 B2 R' U F2 U' F' U2 L' F2 R' U2 L' D2 F2 R F2 D' B2 D2 R' U' F`

4b3 6e, goal 13.

Skeleton starting with B2 U has RV corners, L=10, 3 spare moves.

- B2 U
    - After R2, 1qt edges will be RH (bad) and FH (good), fr=1: +0+0+0(+2)
        - R2 U F2 U2 L2 U' // 4 pairs, no good
        - R2 U' L2 U2 F2 U // 4 pairs, no good
- F2 D
    - After R2, 1qt edges will be RD (bad) and FV (good), fr=1: +0+0+3(+2)
    - After R2, 1qt edges will be RD (bad) and FV (good): +0+0+3(+3)
- B2 U'
    - After L2 U2 R2, 1qt edges will be RH (bad) and FH (good), fr=1: +0+2+1(+2)
    - After R2 L2 U2 L2, 1qt edges will be RD (bad) and FD (bad): +0+3+0(+5)

Check inverse. Skeleton starting with (U2 L2 D) has FD corners.

- (U2 L2 D)
    - After (F2 U2 R2), 1qt edges will be FH (bad) and RV (bad), fr=1: +0+0+0(+5)
    - After (R2 U2 B2 L2 B2 L2), 1qt edges will be FD (good) and RH (good): +0+3+0(+0)
        - (R2 U2 B2 L2 B2 L2 U R2 U) // 0 pairs, no good
    - After (L2 U2 B2 L2 F2 L2), 1qt edges will be FD (good) and RH (good): +0+3+0(+0)
        - (L2 U2 B2 L2 F2 L2 U B2 U) // 0 pairs, no good
- (U2 L2 D')
    - After (L2 U2 B2), 1qt edges will be FH (bad) and RV (bad), fr=1: +0+0+0(+5)
    - After (F2 U2 B2 R2), 1qt edges will be FH (bad) and RH (good): +0+1+0(+3)
    - After (F2 U2 R2 B2 R2 B2), 1qt edges will be FV (bad) and RD (good): +0+3+0(+3)
- (U2 R2 U)
    - After (L2 F2 U2 B2), 1qt edges will be FV (bad) and RH (good), fr=1: +0+1+1(+5)
- (U2 R2 U')
    - After (B2 R2 U2 R2), 1qt edges will be FH (bad) and RV (bad), fr=1: +0+1+1(+5)
    - After (L2 F2 U2 L2 B2), 1qt edges will be FH (bad) and RH (good): +0+2+1(+3)
- (R2 U2 L2 D)
    - After (L2 U2 B2), 1qt edges will be FH (bad) and RH (good): +1+0+0(+3)
- (R2 U2 L2 D')
    - After (F2 U2 R2), 1qt edges will be FH (bad) and RH (good): +1+0+0(+3)
- (L2 U2 L2 D)
    - After (F2 U2 L2), 1qt edges will be FH (bad) and RH (good), fr=1: +1+0+0(+5)
    - After (R2 U2 L2 B2), 1qt edges will be FV (bad) and RH (good): +1+1+0(+3)
- (L2 U2 L2 D')
    - After (R2 U2 B2), 1qt edges will be FH (bad) and RH (good), fr=1: +1+0+0(+5)
    - After (R2 F2 U2 B2), 1qt edges will be FH (bad) and RH (good): +1+1+0(+3)
- (U2 B2 R2 U)
    - After (F2 L2 U2 L2), 1qt edges will be FV (bad) and RD (good): +1+1+0(+3)
- (U2 F2 L2 D')
    - After (F2 L2 U2 R2), 1qt edges will be FV (bad) and RD (good), fr=1: +1+1+0(+5)

Skeleton starting with U' F2 D' R2 U' has RV corners, L=11, 2 spare moves.

- U' F2 D' R2 U'
    - After L2 F2, 1qt edges will be RV (good) and FD (bad): +0+1+0(+3)
- U' F2 D' L2 U'
    - After F2 L2, 1qt edges will be RV (good) and FD (bad): +0+1+1(+3)
- U' B2 U' F2 L2 U
    - After B2, 1qt edges will be RH (bad) and FD (bad): +1+0+0(+5)
- U' F2 D' F2 R2 U
    - After R2, 1qt edges will be RH (bad) and FV (good): +1+0+1(+3)
- U' R2 B2 U B2 D
    - After L2 F2, 1qt edges will be RV (good) and FH (good): +1+1+0(+0)
        - L2 F2 U B2 U' // no good
- U' F2 D' F2 L2 D
    - After F2 L2, 1qt edges will be RV (good) and FV (good): +1+1+0(+1)
- U' B2 U' F2 R2 U
    - After B2 L2, 1qt edges will be RV (good) and FD (bad): +1+1+0(+3)
- U' F2 D' B2 R2 U
    - After F2 L2, 1qt edges will be RH (bad) and FH (good): +1+1+0(+3)
- U' L2 F2 D B2 U
    - After F2 L2, 1qt edges will be RV (good) and FD (bad): +1+1+0(+3)

Check inverse. Skeleton starting with (U2 R2 U' F2 D R2 U') has HH corners. Apply U' and NISS: FD corners.

- (U2 L2 D' F2 U)
    - After (R2 F2), 1qt edges will be FH (bad) and RD (good): +0+1+1(+3)
- (L2 U2 R2 U F2 D)
    - After (L2 F2), 1qt edges will be FH (bad) and RV (bad), fr=1: +1+1+0(+5)

The same skeleton in full, for the solutions that go on after its last quarter turn.

- (U2 R2 U' F2 D R2 U')
    - After (R2), 1qt edges will be RD (bad) and FH (good): +0+0+0(+3)
- (U2 R2 U' B2 U L2 D')
    - After (L2), 1qt edges will be RD (bad) and FV (bad): +0+0+0(+6)
- (U2 L2 D' B2 U R2 U')
    - After (B2), 1qt edges will be RV (bad) and FH (good): +0+0+1(+3)
- (U2 L2 D' B2 U L2 U')
    - After (F2 L2), 1qt edges will be RV (bad) and FD (bad): +0+1+0(+6)
- (U2 R2 U' F2 D R2 U)
    - After (R2 U2 R2), 1qt edges will be RD (bad) and FH (good), fr=1: +0+2+0(+5)
- (U2 R2 U' B2 U L2 D)
    - After (L2 U2 R2), 1qt edges will be RD (bad) and FV (bad), fr=1: +0+2+0(+6)
- (L2 U2 R2 U B2 D L2 U')
    - After (L2), 1qt edges will be RD (bad) and FH (good), fr=1: +1+0+0(+5)
- (L2 U2 R2 U F2 U R2 D')
    - After (R2), 1qt edges will be RD (bad) and FV (bad), fr=1: +1+0+0(+6)
- (U2 L2 D' L2 B2 U' F2 U)
    - After (L2), 1qt edges will be RH (good) and FD (bad): +1+0+1(+3)
- (R2 U2 L2 D B2 U R2 U')
    - After (B2), 1qt edges will be RH (good) and FH (good), fr=1: +1+0+1(+5)
- (U2 L2 D' F2 D B2 R2 D)
    - After (R2 F2), 1qt edges will be RH (good) and FH (good): +1+1+0(+0)
        - (R2 F2 U' L2 U') // 6 pairs, no good
- (U2 L2 D' F2 D F2 R2 D)
    - After (L2 B2), 1qt edges will be RH (good) and FH (good): +1+1+0(+0)
        - (L2 B2 U' R2 U') // 0 pairs, no good
- (U2 L2 D' B2 U F2 L2 U)
    - After (L2 F2), 1qt edges will be RD (bad) and FH (good): +1+1+0(+3)
- (U2 R2 U' B2 U B2 L2 D)
    - After (L2 F2), 1qt edges will be RH (good) and FD (bad): +1+1+0(+3)
- (U2 R2 U' B2 U F2 R2 U)
    - After (R2 F2), 1qt edges will be RD (bad) and FH (good): +1+1+0(+3)
- (U2 R2 U' L2 F2 D' F2 D)
    - After (R2 B2), 1qt edges will be RH (good) and FD (bad): +1+1+0(+3)
- (R2 U2 L2 D B2 U L2 U')
    - After (F2 L2), 1qt edges will be RH (good) and FD (bad), fr=1: +1+1+0(+5)
- (U2 L2 D' F2 D B2 L2 U)
    - After (R2 B2), 1qt edges will be RV (bad) and FD (bad): +1+1+0(+6)
- (U2 L2 D' F2 D F2 L2 U)
    - After (L2 F2), 1qt edges will be RV (bad) and FD (bad): +1+1+0(+6)
- (U2 L2 D' L2 B2 U' B2 U)
    - After (R2 B2), 1qt edges will be RD (bad) and FD (bad): +1+1+0(+6)
- (U2 R2 U' F2 D B2 R2 U)
    - After (R2 F2), 1qt edges will be RV (bad) and FD (bad): +1+1+0(+6)
- (U2 R2 U' F2 D F2 L2 D)
    - After (L2 F2), 1qt edges will be RD (bad) and FV (bad): +1+1+0(+6)
- (U2 R2 U' R2 B2 U' F2 U)
    - After (B2 L2), 1qt edges will be RV (bad) and FD (bad): +1+1+0(+6)

Skeleton starting with U' R2 D' B2 U' has RV corners, L=11, 2 spare moves.

- U' R2 D' B2 U'
    - After R2 B2, 1qt edges will be RV (good) and FV (good), fr=1: +0+1+0(+2)
- U' L2 U' F2 U'
    - After B2 R2, 1qt edges will be RD (bad) and FV (good), fr=1: +0+1+1(+2)
- U' R2 D' F2 U
    - After L2 U2 R2, 1qt edges will be RH (bad) and FH (good): +0+2+0(+3)

Check inverse. Skeleton starting with (U2 R2 U F2 U' F2 D) has HH corners. Apply U' and NISS: RD corners.

- (U2 R2 U B2 D')
    - After (R2 L2 B2), 1qt edges will be RD (good) and FD (good), fr=1: +0+2+0(+4)
- (U2 L2 D F2 U')
    - After (R2 L2 B2), 1qt edges will be RH (bad) and FD (good), fr=1: +0+2+0(+5)
- (U2 R2 U F2 D')
    - After (L2 F2 B2), 1qt edges will be RH (bad) and FV (bad), fr=1: +0+2+0(+5)

The same skeleton in full, for the solutions that go on after its last quarter turn.

- (U2 L2 D F2 U' F2 U)
    - After (L2), 1qt edges will be RV (bad) and FH (good), fr=1: +0+0+0(+5)
    - After (L2), 1qt edges will be RV (bad) and FH (good): +0+0+2(+3)
- (U2 R2 U B2 D' B2 U)
    - After (B2), 1qt edges will be RD (bad) and FH (good), fr=1: +0+0+1(+5)
    - After (F2), 1qt edges will be RV (bad) and FV (bad), fr=1: +0+0+1(+6)
- (U2 L2 D F2 U' B2 U)
    - After (R2 F2), 1qt edges will be RH (good) and FV (bad), fr=1: +0+1+0(+5)
- (U2 L2 D F2 U' F2 U')
    - After (L2 U2 L2), 1qt edges will be RV (bad) and FH (good): +0+2+0(+3)
- (U2 L2 D B2 D' F2 D)
    - After (F2 B2 L2), 1qt edges will be RD (bad) and FH (good), fr=1: +0+2+0(+5)
- (U2 R2 U F2 U' B2 U)
    - After (F2 B2 R2), 1qt edges will be RV (bad) and FV (bad), fr=1: +0+2+0(+6)
- (U2 R2 U F2 U' F2 D)
    - After (F2 B2 L2), 1qt edges will be RD (bad) and FV (bad), fr=1: +0+2+0(+6)
- (R2 U2 L2 D' F2 U' F2 U)
    - After (L2), 1qt edges will be RH (good) and FH (good): +1+0+0(+0)
        - (L2 U F2 U') // no good
- (L2 U2 R2 U' F2 D' F2 U)
    - After (B2), 1qt edges will be RH (good) and FV (bad): +1+0+1(+3)
- (U2 R2 U B2 D' R2 B2 U')
    - After (L2), 1qt edges will be RD (bad) and FH (good), fr=1: +1+0+1(+5)
    - After (R2), 1qt edges will be RV (bad) and FD (bad), fr=1: +1+0+1(+6)
- (U2 R2 U L2 F2 U L2 U')
    - After (R2), 1qt edges will be RV (bad) and FH (good), fr=1: +1+0+1(+5)
- (L2 U2 L2 D' B2 U' F2 U)
    - After (R2 F2), 1qt edges will be RH (good) and FV (bad): +1+1+0(+3)
- (U2 F2 L2 D' L2 U L2 U')
    - After (L2 F2), 1qt edges will be RH (good) and FV (bad), fr=1: +1+1+0(+5)
- (U2 R2 U R2 B2 D L2 U')
    - After (L2 B2), 1qt edges will be RD (bad) and FH (good), fr=1: +1+1+0(+5)
- (U2 R2 U R2 B2 D R2 D')
    - After (L2 F2), 1qt edges will be RH (good) and FD (bad), fr=1: +1+1+0(+5)
- (R2 U2 L2 D' F2 U' B2 U)
    - After (R2 F2), 1qt edges will be RV (bad) and FV (bad): +1+1+0(+6)

Skeleton starting with F2 D L2 U' B2 U has RV corners, L=11, 2 spare moves.

- F2 D L2 U' B2 U
    - After F2 B2, 1qt edges will be RD (bad) and FH (good), fr=1: +0+2+0(+2)

Skeleton starting with F2 D L2 U F2 U has RV corners, L=11, 2 spare moves.

- F2 D L2 U F2 U
    - After F2 B2, 1qt edges will be RD (bad) and FD (bad): +0+2+0(+5)

Skeleton starting with F2 D L2 U L2 U' has RV corners, L=11, 2 spare moves.

- F2 D L2 U L2 U'
    - After R2 L2, 1qt edges will be RH (bad) and FV (good), fr=1: +0+2+0(+2)

Skeleton starting with F2 D L2 U' R2 U' has RV corners, L=11, 2 spare moves.

- F2 D L2 U' R2 U'
    - After R2 L2, 1qt edges will be RV (good) and FV (good): +0+2+0(+1)

Skeleton starting with F2 D R2 U B2 U2 L2 D' has HH corners, L=11, 2 spare moves. Apply (U) and NISS: HH corners.

- B2 U L2 U
    - After L2 U2 B2, 1qt edges will be RH (good) and FH (good), fr=1: +0+0+1(+5)
    - After L2 U2 F2, 1qt edges will be RV (bad) and FD (bad), fr=1: +0+0+1(+6)
- B2 U L2 U'
    - After B2 U2 L2, 1qt edges will be RH (good) and FH (good), fr=1: +0+0+1(+5)
    - After F2 U2 L2, 1qt edges will be RV (bad) and FD (bad), fr=1: +0+0+1(+6)
- F2 U F2 U
    - After R2 U2 B2, 1qt edges will be RH (good) and FV (bad), fr=1: +0+0+1(+5)
- F2 U F2 U'
    - After F2 U2 L2, 1qt edges will be RH (good) and FV (bad), fr=1: +0+0+1(+5)
- R2 B2 D' L2 U
    - After R2 U2 B2, 1qt edges will be RH (good) and FV (bad): +1+0+0(+3)
- R2 B2 D' L2 U'
    - After B2 U2 R2, 1qt edges will be RH (good) and FV (bad): +1+0+0(+3)
- L2 F2 U' R2 D
    - After L2 U2 F2, 1qt edges will be RV (bad) and FD (bad), fr=1: +1+0+0(+6)
- L2 F2 U' R2 D'
    - After B2 U2 R2, 1qt edges will be RV (bad) and FD (bad), fr=1: +1+0+0(+6)
- B2 U B2 R2 U
    - After L2 U2 B2, 1qt edges will be RH (good) and FV (bad): +1+0+1(+3)
    - After R2 U2 B2, 1qt edges will be RV (bad) and FD (bad): +1+0+1(+6)
- B2 U B2 R2 U'
    - After B2 U2 L2, 1qt edges will be RH (good) and FV (bad): +1+0+1(+3)
- F2 U R2 B2 U
    - After R2 U2 B2, 1qt edges will be RH (good) and FV (bad): +1+0+1(+3)
    - After R2 U2 F2, 1qt edges will be RV (bad) and FD (bad): +1+0+1(+6)
- F2 U R2 B2 U'
    - After F2 U2 L2, 1qt edges will be RH (good) and FV (bad): +1+0+1(+3)
    - After B2 U2 L2, 1qt edges will be RV (bad) and FD (bad): +1+0+1(+6)
- B2 U B2 L2 U
    - After L2 U2 B2, 1qt edges will be RD (bad) and FH (good), fr=1: +1+0+1(+5)
    - After R2 U2 B2, 1qt edges will be RV (bad) and FD (bad), fr=1: +1+0+1(+6)
- B2 U B2 L2 U'
    - After B2 U2 L2, 1qt edges will be RD (bad) and FH (good), fr=1: +1+0+1(+5)
- F2 U R2 F2 U
    - After R2 U2 F2, 1qt edges will be RD (bad) and FH (good), fr=1: +1+0+1(+5)
- F2 U R2 F2 U'
    - After F2 U2 L2, 1qt edges will be RH (good) and FV (bad), fr=1: +1+0+1(+5)
- L2 B2 U' B2 U'
    - After F2 L2 U2 R2, 1qt edges will be RV (bad) and FH (good): +1+1+0(+3)
    - After L2 U2 L2 F2, 1qt edges will be RV (bad) and FV (bad): +1+1+0(+6)
- R2 F2 D' B2 D'
    - After F2 R2 U2 R2, 1qt edges will be RH (good) and FH (good), fr=1: +1+1+0(+5)

The same skeleton in full, for the solutions that go on after its last quarter turn.

- F2 D L2 U L2 U2 F2 D'
    - After R2, 1qt edges will be RH (good) and FH (good), fr=1: +0+0+2(+5)
- F2 D L2 U' F2 U2 L2 D
    - After L2, 1qt edges will be RH (good) and FH (good), fr=1: +0+0+2(+5)

Skeleton starting with (F2 U2 R2 U) on inverse has RV corners, L=12, 1 spare move.

- (F2 U2 R2 U)
    - After (B2 U2 L2), 1qt edges will be RD (bad) and FH (good), fr=1: +0+0+0(+2)
- (F2 U2 R2 U')
    - After (L2 U2 B2), 1qt edges will be RD (bad) and FH (good), fr=1: +0+0+0(+2)
- (B2 U2 L2 D)
    - After (F2 U2 R2), 1qt edges will be RD (bad) and FH (good): +0+0+0(+3)
    - After (L2 U2 R2 B2), 1qt edges will be RD (bad) and FV (good), fr=1: +0+1+0(+2)
- (B2 U2 L2 D')
    - After (L2 U2 B2), 1qt edges will be RD (bad) and FH (good): +0+0+0(+3)
    - After (L2 F2 U2 B2), 1qt edges will be RD (bad) and FH (good), fr=1: +0+1+0(+2)
- (L2 U2 F2 D)
    - After (B2 U2 R2), 1qt edges will be RD (bad) and FD (bad), fr=1: +0+0+0(+5)
    - After (R2 B2 U2 B2), 1qt edges will be RV (good) and FV (good), fr=1: +0+1+0(+2)
- (L2 U2 F2 D')
    - After (L2 U2 F2), 1qt edges will be RD (bad) and FD (bad), fr=1: +0+0+0(+5)
    - After (B2 U2 F2 R2), 1qt edges will be RV (good) and FD (bad): +0+1+0(+3)
- (R2 U2 B2 U')
    - After (F2 L2 U2 L2), 1qt edges will be RV (good) and FV (good): +0+1+0(+1)

Skeleton starting with U' F2 D R2 U has DD corners, L=12, 1 spare move.

- U' F2 D R2 U
    - After L2 F2, 1qt edges will be FD (good) and RH (bad): +0+1+0(+3)

Check inverse. Skeleton starting with (R2 U2 F2 U R2 U R2 U') has HH corners. Apply U' and NISS: FD corners.

- (L2 U2 F2 D L2 U)
    - After (R2 B2), 1qt edges will be FD (good) and RH (good): +0+1+0(+0)
        - (R2 B2 U B2 U) // no good
- (B2 U2 L2 U F2 D')
    - After (B2 R2), 1qt edges will be FD (good) and RH (good), fr=1: +0+1+0(+3)

The same skeleton in full, for the solutions that go on after its last quarter turn.

- (F2 U2 R2 U B2 D' B2 D)
    - After (L2), 1qt edges will be RD (bad) and FH (good), fr=1: +0+0+0(+5)
- (L2 U2 B2 U L2 D L2 U')
    - After (L2), 1qt edges will be RD (bad) and FH (good): +0+0+1(+3)
- (F2 U2 L2 U L2 D' B2 U)
    - After (R2), 1qt edges will be RV (bad) and FH (good), fr=1: +0+0+1(+5)
- (R2 U2 F2 U L2 D L2 U')
    - After (R2), 1qt edges will be RV (bad) and FD (bad): +0+0+1(+6)
- (F2 U2 R2 U B2 D' F2 D)
    - After (R2 B2), 1qt edges will be RH (good) and FV (bad), fr=1: +0+1+0(+5)
- (L2 U2 F2 D R2 U L2 U')
    - After (B2 L2), 1qt edges will be RV (bad) and FD (bad): +0+1+0(+6)
- (R2 U2 F2 U L2 D R2 D')
    - After (B2 L2), 1qt edges will be RV (bad) and FV (bad): +0+1+0(+6)

Skeleton starting with U' B2 U R2 U2 F2 U has RD corners, L=12, 1 spare move.

- U' B2 U R2 U2 F2 U
    - After B2, 1qt edges will be RH (bad) and FH (good): +0+0+0(+3)
- U' B2 U' F2 U2 R2 U'
    - After B2, 1qt edges will be RH (bad) and FH (good): +0+0+0(+3)
- U' F2 D L2 U2 B2 D
    - After B2, 1qt edges will be RV (bad) and FH (good): +0+0+0(+3)
- U' F2 D' F2 U2 R2 D'
    - After B2, 1qt edges will be RV (bad) and FH (good): +0+0+0(+3)
- U' F2 D L2 U2 F2 U
    - After B2, 1qt edges will be RH (bad) and FH (good): +0+0+1(+3)
- U' F2 D' B2 U2 R2 U'
    - After F2, 1qt edges will be RH (bad) and FH (good): +0+0+1(+3)
- U' B2 U L2 U2 F2 U
    - After B2 R2, 1qt edges will be RD (good) and FH (good): +0+1+0(+0)
        - B2 R2 U' B2 U // 4 pairs, no good
- U' F2 D F2 U2 R2 D
    - After F2 R2, 1qt edges will be RH (bad) and FV (bad), fr=1: +0+1+0(+5)
- U' F2 D' L2 U2 B2 D'
    - After F2 R2, 1qt edges will be RH (bad) and FV (bad), fr=1: +0+1+0(+5)
- 1 more variant of this skeleton passes the meta, not reached before the stop.

Stop: 10 HTRs done, nothing within goal. This DR's optimal is 14, over the goal.

### 4b3, scramble 3

`R' U' F U2 F2 R2 B2 U' R' F B' R D L U' R2 U' D' F2 U2 D L2 D2 R' U' F`

4b3 4e, goal 13.

Skeleton starting with D has HH corners, L=7, 6 spare moves. Apply (D) and NISS: DD corners.

- With no setup, 1qt edges will be FV (good) and RH (bad): +0+3(+3)
    - U L2 F2 R2 B2 D // 6 pairs, no good
    - U L2 F2 L2 F2 U' // 6 pairs, no good
    - U L2 B2 R2 F2 D // 2 pairs, no good
- 1 more variant of this skeleton passes the meta, not reached before the stop.

The same skeleton in full, for the solutions that go on after its last quarter turn.

- D
    - After F2, 1qt edges will be RH (good) and FV (bad): +0+0+3(+3)
        - F2 U R2 U2 B2 L2 B2 L2 U' // 10 pairs, no good
        - F2 U L2 U2 B2 L2 F2 L2 D' // 10 pairs, no good
        - F2 U R2 U2 B2 L2 F2 R2 D // 8 pairs, no good
- D'
    - After F2 U2 B2, 1qt edges will be RH (good) and FV (bad): +0+2+3(+3)
    - After B2 U2 B2, 1qt edges will be RH (good) and FV (bad), fr=1: +0+2+3(+5)
- 5 more variants of this skeleton pass the meta, not reached before the stop.

Check inverse. Skeleton starting with (D) has HH corners. Apply D and NISS: FD corners.

- With no setup, 1qt edges will be FH (bad) and RH (good): +0+3(+3)
    - (U' R2 U2 B2 L2 F2 R2 D') // 6 pairs, no good
    - (U' R2 U2 B2 L2 B2 L2 U') // 6 pairs, no good
    - (U' L2 U2 B2 L2 F2 L2 D') // 6 pairs, no good
- 13 more variants of this skeleton pass the meta, not reached before the stop.

The same skeleton in full, for the solutions that go on after its last quarter turn.

- (D)
    - After (L2 U2 B2), 1qt edges will be RV (bad) and FH (good): +0+0+3(+3)
        - (L2 U2 B2 U' B2 R2 B2 R2 U) // 10 pairs, no good
    - After (F2 U2 R2), 1qt edges will be RD (bad) and FD (bad), fr=1: +0+0+3(+6)
    - After (L2 U2 R2 L2 F2), 1qt edges will be RV (bad) and FH (good): +0+2+3(+3)
- 31 more variants of this skeleton pass the meta, not reached before the stop.

Stop: 10 HTRs done, nothing within goal. This DR's optimal is 14, over the goal.

### 4b3, scramble 4

`R' U' F R D' F2 L' D2 F2 R D2 B2 L D2 R2 B R' F L' D' R2 B F2 R' U' F`

4b3 6e, goal 13.

Skeleton starting with U has RD corners, L=8, 5 spare moves.

- U
    - After R2, 1qt edges will be RH (bad) and FD (good): +0+0+1(+3)
        - R2 U L2 U2 R2 F2 D // 4 pairs, no good
    - After L2, 1qt edges will be RD (good) and FV (bad): +0+0+1(+3)
        - L2 U' R2 U2 R2 B2 U' // 4 pairs, no good
    - After R2, 1qt edges will be RH (bad) and FD (good): +0+0+1(+3)
        - R2 U L2 U2 L2 B2 U // 2 pairs, no good
- 65 more variants of this skeleton pass the meta, not reached before the stop.

Check inverse. Skeleton starting with (R2 U) has HH corners. Apply U and NISS: RD corners.

- After (F2 L2), 1qt edges will be RD (good) and FD (good): +1+1(+1)
    - (F2 L2 U' F2 U2 F2 R2 D') // 2 pairs, no good
    - (F2 L2 U' F2 U2 B2 L2 U') // 2 pairs, no good
- After (B2 R2), 1qt edges will be RD (good) and FD (good): +1+1(+1)
    - (B2 R2 U B2 U2 F2 L2 U) // 2 pairs, no good
- 117 more variants of this skeleton pass the meta, not reached before the stop.

The same skeleton in full, for the solutions that go on after its last quarter turn.

- (L2 D)
    - After (R2 F2 U2 L2 B2), 1qt edges will be RD (bad) and FH (good): +0+2+0(+3)
        - (R2 F2 U2 L2 B2 U' R2 U') // no good
    - After (F2 U2 F2 B2 R2), 1qt edges will be RD (bad) and FD (bad): +0+2+0(+6)
    - After (R2 U2 B2), 1qt edges will be RV (bad) and FH (good): +0+0+5(+3)
- (R2 U')
    - After (R2 B2 U2 B2), 1qt edges will be RD (bad) and FD (bad), fr=1: +0+1+1(+6)
    - After (R2 B2 U2 F2), 1qt edges will be RV (bad) and FH (good): +0+1+3(+3)
    - After (R2 U2 F2), 1qt edges will be RV (bad) and FH (good): +0+0+5(+3)
- (R2 U)
    - After (R2 B2 U2 R2 B2), 1qt edges will be RD (bad) and FH (good): +0+2+1(+3)
    - After (F2 L2 U2 B2 R2), 1qt edges will be RD (bad) and FH (good), fr=1: +0+2+1(+5)
    - After (L2 B2 U2 F2 B2 L2 B2), 1qt edges will be RD (bad) and FH (good): +0+4+1(+3)
- (F2 R2 U)
    - After (F2 U2 R2), 1qt edges will be RV (bad) and FH (good): +1+0+0(+3)
        - (F2 U2 R2 U' B2 U') // 1 pair, no good
- (F2 R2 U')
    - After (R2 U2 F2), 1qt edges will be RV (bad) and FH (good): +1+0+0(+3)
        - (R2 U2 F2 U B2 U') // 1 pair, no good
- (F2 L2 U)
    - After (B2 R2 U2 R2), 1qt edges will be RH (good) and FD (bad): +1+1+1(+3)
- (B2 R2 U')
    - After (L2 B2 U2 F2), 1qt edges will be RH (good) and FD (bad), fr=1: +1+1+1(+5)
- 58 more variants of this skeleton pass the meta, not reached before the stop.

Skeleton starting with U R2 U B2 U has RD corners, L=9, 4 spare moves.

- U R2 U B2 U
    - After R2 L2, 1qt edges will be RV (bad) and FV (bad), fr=1: +0+2+1(+5)
- U R2 U B2 U'
    - After F2 B2, 1qt edges will be RV (bad) and FV (bad), fr=1: +0+2+1(+5)
- U R2 U F2 U
    - After F2 L2 B2, 1qt edges will be RD (good) and FD (good), fr=1: +0+3+1(+4)
    - After B2 R2 F2, 1qt edges will be RH (bad) and FH (good), fr=1: +0+3+1(+5)
- U R2 U F2 U'
    - After R2 F2 L2, 1qt edges will be RD (good) and FD (good), fr=1: +0+3+1(+4)
- U L2 U L2 D
    - After R2 F2 B2 L2, 1qt edges will be RD (good) and FV (bad), fr=1: +0+4+0(+5)
- U L2 U L2 D'
    - After R2 F2 B2 L2, 1qt edges will be RD (good) and FV (bad), fr=1: +0+4+0(+5)
- U L2 U R2 U
    - After L2 F2 B2 R2, 1qt edges will be RD (good) and FV (bad), fr=1: +0+4+0(+5)
- U L2 U R2 U'
    - After L2 F2 B2 R2, 1qt edges will be RD (good) and FV (bad), fr=1: +0+4+0(+5)
- U B2 L2 U' B2 U
    - After F2 B2, 1qt edges will be RV (bad) and FD (good), fr=1: +1+2+1(+5)
- U B2 L2 U' B2 U'
    - After R2 L2, 1qt edges will be RV (bad) and FD (good), fr=1: +1+2+1(+5)
- U F2 L2 U' B2 U
    - After F2 B2, 1qt edges will be RV (bad) and FV (bad), fr=1: +1+2+1(+5)
- U F2 L2 U' B2 U'
    - After R2 L2, 1qt edges will be RV (bad) and FV (bad), fr=1: +1+2+1(+5)
- U R2 U L2 B2 U
    - After R2 L2, 1qt edges will be RV (bad) and FH (good), fr=1: +1+2+1(+5)
- U R2 U L2 B2 U'
    - After F2 B2, 1qt edges will be RV (bad) and FH (good), fr=1: +1+2+1(+5)
- U R2 U L2 F2 U
    - After R2 L2, 1qt edges will be RD (good) and FV (bad), fr=1: +1+2+1(+5)
- U R2 U L2 F2 U'
    - After F2 B2, 1qt edges will be RD (good) and FV (bad), fr=1: +1+2+1(+5)

Check inverse. Skeleton starting with (R2 U' F2 U D) has HH corners. Apply U and NISS: RD corners.

- (L2 D' F2 U)
    - After (F2 B2), 1qt edges will be RH (bad) and FH (good), fr=1: +0+2+0(+3)
- (R2 D' L2 D)
    - After (B2 R2 F2), 1qt edges will be RV (bad) and FV (bad), fr=1: +0+3+0(+5)
- (L2 D' F2 U')
    - After (L2 B2 L2), 1qt edges will be RH (bad) and FV (bad), fr=1: +0+3+0(+5)
- (R2 D' L2 D')
    - After (B2 R2 B2), 1qt edges will be RH (bad) and FV (bad), fr=1: +0+3+0(+5)
- (L2 D' B2 U)
    - After (F2 R2 B2), 1qt edges will be RD (good) and FD (good), fr=1: +0+3+1(+4)
- (R2 D' R2 U)
    - After (F2 R2 B2), 1qt edges will be RV (bad) and FH (good), fr=1: +0+3+1(+5)
- (L2 D' L2 B2 D)
    - After (R2 L2), 1qt edges will be RV (bad) and FH (good), fr=1: +1+2+0(+3)
- (R2 D' B2 L2 D')
    - After (F2 B2), 1qt edges will be RD (good) and FD (good), fr=1: +1+2+0(+3)
- (B2 L2 U F2 U)
    - After (F2 B2), 1qt edges will be RH (bad) and FD (good), fr=1: +1+2+1(+5)
- (B2 L2 U F2 U')
    - After (R2 L2), 1qt edges will be RH (bad) and FD (good), fr=1: +1+2+1(+5)
- (B2 R2 U R2 U)
    - After (F2 B2), 1qt edges will be RH (bad) and FH (good), fr=1: +1+2+1(+5)
- (B2 R2 U R2 U')
    - After (R2 L2), 1qt edges will be RH (bad) and FH (good), fr=1: +1+2+1(+5)
- (L2 D' R2 F2 U')
    - After (B2 R2 F2), 1qt edges will be RD (good) and FH (good), fr=1: +1+3+0(+3)
- (R2 D' F2 R2 U)
    - After (R2 B2 L2), 1qt edges will be RD (good) and FH (good), fr=1: +1+3+0(+3)
- (L2 D' L2 B2 D')
    - After (F2 R2 F2), 1qt edges will be RH (bad) and FH (good), fr=1: +1+3+0(+5)
- (L2 D' R2 F2 U)
    - After (B2 R2 B2), 1qt edges will be RH (bad) and FH (good), fr=1: +1+3+0(+5)
- (R2 D' B2 L2 D)
    - After (L2 B2 L2), 1qt edges will be RD (good) and FV (bad), fr=1: +1+3+0(+5)
- (R2 D' F2 R2 U')
    - After (R2 B2 R2), 1qt edges will be RD (good) and FV (bad), fr=1: +1+3+0(+5)

Skeleton starting with U L2 U' R2 U has RD corners, L=9, 4 spare moves.

- U L2 U' R2 U
    - After F2 B2, 1qt edges will be RH (bad) and FH (good): +0+2+1(+3)
    - After R2 B2 L2, 1qt edges will be RD (good) and FH (good): +0+3+1(+0)
        - R2 B2 L2 U' L2 B2 U' // 2 pairs, no good
- U L2 U' L2 U
    - After L2 B2 R2, 1qt edges will be RD (good) and FD (good): +0+3+1(+1)
    - After R2 F2 L2, 1qt edges will be RV (bad) and FV (bad): +0+3+1(+5)
- U L2 U' L2 U'
    - After F2 L2 B2, 1qt edges will be RD (good) and FD (good): +0+3+1(+1)
- U R2 U' B2 U
    - After F2 R2 L2 B2, 1qt edges will be RH (bad) and FD (good): +0+4+0(+3)
- U R2 U' B2 U'
    - After F2 R2 L2 B2, 1qt edges will be RH (bad) and FD (good): +0+4+0(+3)
- U R2 U' F2 D
    - After F2 R2 L2 B2, 1qt edges will be RH (bad) and FD (good): +0+4+0(+3)
- U R2 U' F2 D'
    - After B2 R2 L2 F2, 1qt edges will be RH (bad) and FD (good): +0+4+0(+3)
- U B2 R2 U L2 U
    - After R2 L2, 1qt edges will be RH (bad) and FH (good): +1+2+1(+3)
- U B2 R2 U L2 U'
    - After F2 B2, 1qt edges will be RH (bad) and FH (good): +1+2+1(+3)
- U L2 U' B2 L2 U
    - After F2 B2, 1qt edges will be RH (bad) and FD (good): +1+2+1(+3)
- U L2 U' B2 L2 U'
    - After R2 L2, 1qt edges will be RH (bad) and FD (good): +1+2+1(+3)
- U L2 U' B2 R2 U
    - After F2 B2, 1qt edges will be RV (bad) and FH (good): +1+2+1(+3)
- U L2 U' B2 R2 U'
    - After R2 L2, 1qt edges will be RV (bad) and FH (good): +1+2+1(+3)
- 7 more variants of this skeleton pass the meta, not reached before the stop.

Stop: 10 HTRs done, nothing within goal. This DR's optimal is 14, over the goal.

### 4b3, scramble 5

`R' U' F U R F R' B2 U2 D' F' U R2 U L2 D' L2 D2 B2 R2 U2 B2 R' U' F`

4b3 2e, goal 13.

Skeleton starting with R2 D' has FD corners, L=9, 4 spare moves.

- R2 D'
    - After B2 L2 U2 L2, 1qt edges will be FV (bad) and RH (good): +0+1+0(+3)
        - B2 L2 U2 L2 U' R2 U // 2 pairs, no good
    - After L2 U2 R2 F2, 1qt edges will be FH (bad) and RH (good): +0+1+0(+3)
        - L2 U2 R2 F2 U' B2 U' // 2 pairs, no good
- R2 D
    - After L2 U2 F2 R2 L2, 1qt edges will be FV (bad) and RH (good), fr=1: +0+2+0(+5)
    - After R2 F2 U2 R2 L2 B2, 1qt edges will be FV (bad) and RH (good): +0+3+0(+3)
    - After B2 L2 B2 U2 B2 U2 R2, 1qt edges will be FV (bad) and RD (good): +0+4+0(+3)
- L2 U'
    - After F2 L2 U2 R2, 1qt edges will be FV (bad) and RH (good): +0+1+1(+3)
    - After F2 L2 U2 L2, 1qt edges will be FH (bad) and RV (bad): +0+1+1(+5)
    - After F2 L2 U2 R2, 1qt edges will be FV (bad) and RH (good): +0+1+3(+3)
- L2 U
    - After R2 U2 F2, 1qt edges will be FV (bad) and RH (good): +0+0+3(+3)
    - After L2 F2 U2 L2 F2, 1qt edges will be FV (bad) and RV (bad): +0+2+1(+5)
    - After R2 F2 R2 L2 U2 B2, 1qt edges will be FV (bad) and RH (good): +0+3+1(+3)
- B2 R2 D
    - After F2 U2 R2, 1qt edges will be FH (bad) and RV (bad): +1+0+0(+5)
    - After R2 U2 B2 R2 L2, 1qt edges will be FD (good) and RH (good), fr=1: +1+2+0(+3)
- B2 R2 D'
    - After L2 U2 B2, 1qt edges will be FH (bad) and RV (bad): +1+0+0(+5)
    - After F2 L2 U2 R2, 1qt edges will be FD (good) and RH (good): +1+1+0(+0)
        - F2 L2 U2 R2 U' B2 U // no good
- F2 R2 U
    - After R2 B2 U2 F2, 1qt edges will be FD (good) and RH (good), fr=1: +1+1+1(+3)
- 14 more variants of this skeleton pass the meta, not reached before the stop.

Check inverse. Skeleton starting with (F2 U) has RD corners.

- (F2 U)
    - After (R2), 1qt edges will be RV (bad) and FH (good): +0+0+3(+3)
    - After (R2), 1qt edges will be RV (bad) and FH (good), fr=1: +0+0+3(+5)
    - After (R2), 1qt edges will be RV (bad) and FH (good): +0+0+4(+3)
- (B2 U')
    - After (R2 F2 U2 R2), 1qt edges will be RD (good) and FV (bad): +0+3+1(+3)
- (B2 U)
    - After (R2 B2 L2 B2 R2), 1qt edges will be RD (good) and FD (good): +0+4+0(+1)
    - After (L2 B2 L2 B2 L2), 1qt edges will be RD (good) and FD (good), fr=1: +0+4+0(+4)
- (R2 F2 U')
    - After (F2), 1qt edges will be RH (bad) and FD (good): +1+0+0(+3)
        - (F2 U L2 U2 B2 D) // 2 pairs, no good
        - (F2 U' B2 U2 L2 D') // 2 pairs, no good
- (L2 B2 U')
    - After (R2), 1qt edges will be RV (bad) and FD (good): +1+0+1(+3)
    - After (R2), 1qt edges will be RV (bad) and FD (good), fr=1: +1+0+1(+5)
    - After (R2), 1qt edges will be RV (bad) and FD (good): +1+0+2(+3)
- (L2 B2 U)
    - After (R2 U2 R2), 1qt edges will be RV (bad) and FD (good): +1+2+0(+3)
    - After (L2 U2 R2), 1qt edges will be RV (bad) and FD (good), fr=1: +1+2+0(+5)

Skeleton starting with (B2 U B2 U L2 D) on inverse has RD corners, L=10, 3 spare moves.

- (B2 U B2 U L2 D)
    - After (F2 L2 F2), 1qt edges will be RD (good) and FH (good): +0+3+0(+0)
        - (F2 L2 F2 U' B2 U R2) // 10 pairs, 13
    - After (L2 F2 L2), 1qt edges will be RH (bad) and FD (good): +0+3+0(+3)
- (B2 U B2 U R2 D)
    - After (B2 R2 B2), 1qt edges will be RD (good) and FH (good): +0+3+0(+0)
        - (B2 R2 B2 U' F2 U) // 2 pairs, no good
    - After (R2 B2 R2), 1qt edges will be RH (bad) and FD (good): +0+3+0(+3)
- (B2 U B2 U L2 D')
    - After (F2 L2 F2), 1qt edges will be RV (bad) and FH (good): +0+3+0(+3)
    - After (R2 B2 R2), 1qt edges will be RH (bad) and FV (bad): +0+3+0(+5)
- (B2 U B2 U R2 D')
    - After (B2 R2 B2), 1qt edges will be RV (bad) and FH (good): +0+3+0(+3)
- (F2 U L2 U F2 U)
    - After (R2 F2 R2), 1qt edges will be RV (bad) and FH (good): +0+3+0(+3)
- (F2 U L2 U F2 U')
    - After (R2 F2 L2), 1qt edges will be RV (bad) and FV (bad): +0+3+0(+5)
- (B2 U R2 F2 U' R2 U')
    - After (R2 L2), 1qt edges will be RD (good) and FH (good): +1+2+0(+0)
        - (R2 L2 U' R2 U') // 6 pairs, no good
- (B2 U L2 B2 D' R2 D')
    - After (R2 L2), 1qt edges will be RV (bad) and FH (good): +1+2+0(+3)
- (B2 U R2 B2 D' L2 D')
    - After (R2 L2), 1qt edges will be RV (bad) and FH (good): +1+2+0(+3)
- (F2 U L2 U L2 B2 D')
    - After (R2 L2), 1qt edges will be RH (bad) and FD (good): +1+2+0(+3)
- (F2 U B2 R2 D' R2 D')
    - After (R2 L2), 1qt edges will be RH (bad) and FV (bad): +1+2+0(+5)
- 2 more variants of this skeleton pass the meta, not reached before the stop.

Skeleton starting with (B2 U B2 U' L2 D) on inverse has RD corners, L=10, 3 spare moves.

- (B2 U B2 U' L2 D)
    - After (F2 L2 F2), 1qt edges will be RD (good) and FH (good), fr=1: +0+3+0(+3)
    - After (L2 F2 L2), 1qt edges will be RH (bad) and FD (good), fr=1: +0+3+0(+5)
- (B2 U B2 U' R2 D)
    - After (B2 R2 B2), 1qt edges will be RD (good) and FH (good), fr=1: +0+3+0(+3)
- (F2 U R2 U' L2 U)
    - After (B2 R2 F2), 1qt edges will be RD (good) and FH (good), fr=1: +0+3+0(+3)
- (F2 U R2 U' R2 U')
    - After (F2 R2 B2), 1qt edges will be RD (good) and FH (good), fr=1: +0+3+0(+3)
    - After (L2 F2 R2), 1qt edges will be RV (bad) and FV (bad), fr=1: +0+3+0(+5)
- (B2 U B2 U' L2 D')
    - After (F2 L2 F2), 1qt edges will be RV (bad) and FH (good), fr=1: +0+3+0(+5)
- (B2 U B2 U' R2 D')
    - After (L2 F2 L2), 1qt edges will be RH (bad) and FV (bad), fr=1: +0+3+0(+5)
- (F2 U L2 U' B2 U)
    - After (L2 B2 L2), 1qt edges will be RV (bad) and FH (good), fr=1: +0+3+0(+5)
- (F2 U L2 U' B2 U')
    - After (L2 B2 R2), 1qt edges will be RV (bad) and FD (good), fr=1: +0+3+0(+5)
- (F2 U R2 U' L2 U')
    - After (B2 R2 F2), 1qt edges will be RH (bad) and FH (good), fr=1: +0+3+0(+5)
- (F2 U R2 U' R2 U)
    - After (R2 B2 L2), 1qt edges will be RV (bad) and FD (good), fr=1: +0+3+0(+5)
- (F2 U B2 R2 D L2 D')
    - After (R2 L2), 1qt edges will be RD (good) and FV (bad), fr=1: +1+2+0(+5)
- (F2 U L2 U' R2 F2 D')
    - After (R2 L2), 1qt edges will be RD (good) and FV (bad), fr=1: +1+2+0(+5)
- (L2 F2 U' B2 U B2 U')
    - After (F2 B2), 1qt edges will be RD (good) and FV (bad), fr=1: +1+2+0(+5)

Skeleton starting with (B2 U B2 U' B2 U') on inverse has RD corners, L=10, 3 spare moves.

- (B2 U B2 U' B2 U')
    - After (F2 L2 F2), 1qt edges will be RD (good) and FH (good): +0+3+0(+0)
        - (F2 L2 F2 U F2 U) // 0 pairs, no good
    - After (R2 B2 R2), 1qt edges will be RH (bad) and FD (good): +0+3+0(+3)
- (B2 U B2 U' F2 U')
    - After (B2 R2 B2), 1qt edges will be RD (good) and FH (good): +0+3+0(+0)
        - (B2 R2 B2 U B2 U) // 0 pairs, no good
- (B2 U B2 U' B2 U)
    - After (B2 R2 B2), 1qt edges will be RV (bad) and FH (good): +0+3+0(+3)
    - After (R2 B2 R2), 1qt edges will be RH (bad) and FV (bad): +0+3+0(+5)
- (B2 U B2 U' F2 U)
    - After (F2 L2 F2), 1qt edges will be RV (bad) and FH (good): +0+3+0(+3)
- (F2 U L2 U' L2 U)
    - After (B2 L2 F2), 1qt edges will be RH (bad) and FH (good): +0+3+0(+3)
- (F2 U L2 U' L2 U')
    - After (B2 L2 B2), 1qt edges will be RV (bad) and FH (good): +0+3+0(+3)
- (F2 U B2 R2 D B2 D)
    - After (F2 B2), 1qt edges will be RV (bad) and FH (good): +1+2+0(+3)
- (F2 U L2 U' F2 R2 D)
    - After (F2 B2), 1qt edges will be RD (good) and FV (bad): +1+2+0(+3)
- (L2 F2 U' B2 U L2 U)
    - After (R2 L2), 1qt edges will be RH (bad) and FD (good): +1+2+0(+3)

Stop: 10 HTRs done, one finish within goal (13). This DR's optimal is 13.

### 4b3, scramble 6

`R' U' F D' R D' U' F2 D L2 F2 U R2 D F D L2 U' L F' R F2 R' U' F`

4b3 4e, goal 13.

Skeleton starting with L2 D has RV corners, L=10, 3 spare moves.

- L2 D
    - After R2, 1qt edges will be RV (good) and FV (good): +0+0+3(+1)
    - After R2, 1qt edges will be RV (good) and FV (good), fr=1: +0+0+3(+2)
- R2 D
    - After F2, 1qt edges will be RH (bad) and FH (good), fr=1: +0+0+3(+2)
    - After F2, 1qt edges will be RH (bad) and FH (good): +0+0+3(+3)
- F2 L2 U'
    - After R2, 1qt edges will be RD (bad) and FV (good), fr=1: +1+0+0(+2)
        - R2 U F2 U2 R2 D' // 3 pairs, no good
        - R2 U' R2 U2 F2 D // 3 pairs, no good
- F2 R2 U'
    - After B2, 1qt edges will be RV (good) and FV (good), fr=1: +1+0+0(+2)
        - B2 U B2 U2 L2 U // 2 pairs, no good
    - After F2, 1qt edges will be RH (bad) and FD (bad): +1+0+0(+5)
- 5 more variants of this skeleton pass the meta, not reached before the stop.

Check inverse. Skeleton starting with (U2 L2 U) has RD corners.

- (U2 L2 U)
    - After (F2 B2 L2 U2 B2), 1qt edges will be RV (bad) and FH (good): +0+2+1(+3)
- (U2 L2 U')
    - After (R2 U2 F2), 1qt edges will be RH (bad) and FD (good), fr=1: +0+0+3(+5)
    - After (B2 U2 L2 F2 B2), 1qt edges will be RD (good) and FV (bad): +0+2+1(+3)
- (U2 R2 U)
    - After (R2 L2 F2 U2 L2), 1qt edges will be RV (bad) and FH (good): +0+2+1(+3)
- (U2 R2 U')
    - After (L2 U2 F2 R2 L2), 1qt edges will be RH (bad) and FD (good): +0+2+1(+3)
- (U2 B2 L2 U')
    - After (B2 U2 F2 R2), 1qt edges will be RD (good) and FD (good): +1+1+0(+1)
        - (B2 U2 F2 R2 U' B2 U') // 3 pairs, no good
    - After (L2 F2 U2 B2), 1qt edges will be RH (bad) and FD (good): +1+1+0(+3)
- (U2 B2 R2 U')
    - After (L2 U2 L2 B2), 1qt edges will be RD (good) and FD (good): +1+1+0(+1)
        - (L2 U2 L2 B2 U' B2 U') // 2 pairs, no good
    - After (B2 R2 U2 R2), 1qt edges will be RD (good) and FV (bad): +1+1+0(+3)
- (U2 F2 R2 D)
    - After (R2 U2 L2 B2), 1qt edges will be RD (good) and FD (good): +1+1+0(+1)
        - (R2 U2 L2 B2 U R2 U') // 3 pairs, no good
- (U2 B2 L2 U)
    - After (F2 U2 B2 R2), 1qt edges will be RH (bad) and FV (bad), fr=1: +1+1+0(+5)
- (U2 B2 R2 U)
    - After (L2 U2 L2 F2), 1qt edges will be RH (bad) and FV (bad), fr=1: +1+1+0(+5)
- (U2 F2 L2 D')
    - After (B2 U2 B2 R2), 1qt edges will be RH (bad) and FV (bad), fr=1: +1+1+0(+5)
- (U2 F2 R2 D')
    - After (R2 U2 L2 F2), 1qt edges will be RH (bad) and FV (bad), fr=1: +1+1+0(+5)
- 1 more variant of this skeleton passes the meta, not reached before the stop.

Skeleton starting with U2 B2 U' has RD corners, L=10, 3 spare moves.

- U2 B2 U'
    - After B2, 1qt edges will be RH (bad) and FD (good): +0+0+1(+3)
    - After F2, 1qt edges will be RV (bad) and FV (bad), fr=1: +0+0+1(+5)
    - After B2, 1qt edges will be RH (bad) and FD (good): +0+0+3(+3)
- U2 F2 U'
    - After R2, 1qt edges will be RD (good) and FV (bad): +0+0+1(+3)
    - After R2, 1qt edges will be RD (good) and FV (bad), fr=1: +0+0+1(+5)
    - After L2, 1qt edges will be RH (bad) and FH (good): +0+0+2(+3)
- U2 B2 U
    - After F2 U2 B2, 1qt edges will be RH (bad) and FD (good): +0+2+0(+3)
    - After B2 U2 F2, 1qt edges will be RV (bad) and FV (bad), fr=1: +0+2+0(+5)
    - After B2 U2 B2, 1qt edges will be RH (bad) and FD (good): +0+2+1(+3)
- U2 F2 U
    - After L2 U2 R2, 1qt edges will be RD (good) and FV (bad): +0+2+0(+3)
    - After R2 U2 L2, 1qt edges will be RH (bad) and FH (good), fr=1: +0+2+0(+5)
    - After R2 U2 R2, 1qt edges will be RD (good) and FV (bad): +0+2+1(+3)
- F2 U2 B2 U
    - After F2, 1qt edges will be RH (bad) and FD (good): +1+0+0(+3)
- F2 U2 F2 U
    - After R2, 1qt edges will be RD (good) and FV (bad), fr=1: +1+0+0(+5)
    - After B2 L2, 1qt edges will be RD (good) and FH (good): +1+1+0(+0)
        - B2 L2 U B2 U2 L2 U' // 1 pair, no good
        - B2 L2 U' L2 U2 B2 U // 1 pair, no good

Check inverse. Skeleton starting with (L2 U) has FV corners.

- (L2 U)
    - After (R2 U2 R2 B2), 1qt edges will be FV (good) and RH (good): +0+1+1(+0)
        - (R2 U2 R2 B2 U F2 L2 D') // 6 pairs, no good
        - (R2 U2 R2 B2 U B2 R2 U') // 6 pairs, no good
- 6 more variants of this skeleton pass the meta, not reached before the stop.

Stop: 10 HTRs done, nothing within goal. This DR's optimal is 14, over the goal.

### 4b3, scramble 7

`R' U' F D R' B' D' L U' B2 R' F' U R2 U' F2 D' F2 L2 D' R2 L' D2 R' U' F`

4b3 4e, goal 13.

Skeleton starting with U has FV corners, L=9, 4 spare moves.

- U
    - After F2, 1qt edges will be FV (good) and RV (good): +0+0+3(+1)
        - F2 U F2 U2 L2 F2 L2 B2 U // 4 pairs, no good
        - F2 U B2 U2 L2 F2 R2 B2 D // 4 pairs, no good
        - F2 U F2 U2 L2 F2 R2 F2 D // 2 pairs, no good
- 5 more variants of this skeleton pass the meta, not reached before the stop.

Check inverse. Skeleton starting with (U2 F2 U) has HH corners. Apply U and NISS: FD corners.

- After (U2 R2 F2), 1qt edges will be FD (good) and RH (good): +1+3(+0)
    - (U2 R2 F2 U F2 U2 L2 F2 R2 B2 D') // 4 pairs, no good
    - (U2 R2 F2 U B2 U2 L2 F2 L2 B2 U) // 4 pairs, no good
- After (U2 L2 B2), 1qt edges will be FD (good) and RH (good): +1+3(+0)
    - (U2 L2 B2 U R2 F2 L2 B2 U2 L2 D') // 4 pairs, no good
- 13 more variants of this skeleton pass the meta, not reached before the stop.

The same skeleton in full, for the solutions that go on after its last quarter turn.

- (U2 B2 U)
    - After (R2 U2 R2 F2), 1qt edges will be RH (good) and FV (bad): +0+1+1(+3)
- (U2 F2 U)
    - After (F2 U2 B2 L2), 1qt edges will be RH (good) and FV (bad): +0+1+1(+3)
- (U2 F2 U')
    - After (L2 U2 L2 B2), 1qt edges will be RV (bad) and FH (good): +0+1+3(+3)
- (U2 B2 U')
    - After (L2 U2 L2 B2), 1qt edges will be RD (bad) and FD (bad), fr=1: +0+1+3(+6)
- (U2 R2 B2 U)
    - After (L2 U2 B2), 1qt edges will be RD (bad) and FH (good): +1+0+0(+3)
        - (L2 U2 B2 U' L2 U') // 1 pair, no good
    - After (B2 U2 R2), 1qt edges will be RV (bad) and FD (bad), fr=1: +1+0+0(+6)
    - After (L2 U2 B2), 1qt edges will be RD (bad) and FH (good): +1+0+2(+3)
- (U2 R2 B2 U')
    - After (B2 U2 L2), 1qt edges will be RD (bad) and FH (good): +1+0+0(+3)
        - (B2 U2 L2 U L2 U') // 1 pair, no good
    - After (R2 U2 B2), 1qt edges will be RV (bad) and FD (bad), fr=1: +1+0+0(+6)
    - After (B2 U2 L2), 1qt edges will be RD (bad) and FH (good): +1+0+2(+3)
- (U2 R2 F2 U)
    - After (B2 U2 R2), 1qt edges will be RD (bad) and FH (good): +1+0+0(+3)
        - (B2 U2 R2 U' R2 U) // 1 pair, no good
- (B2 U2 B2 U)
    - After (L2 U2 B2), 1qt edges will be RH (good) and FV (bad): +1+0+1(+3)
- (B2 U2 B2 U')
    - After (F2 U2 L2), 1qt edges will be RV (bad) and FH (good): +1+0+1(+3)
- (B2 U2 F2 U)
    - After (B2 U2 R2), 1qt edges will be RH (good) and FV (bad): +1+0+1(+3)
- (B2 U2 F2 U')
    - After (L2 U2 F2), 1qt edges will be RH (good) and FV (bad): +1+0+1(+3)
    - After (L2 U2 B2), 1qt edges will be RD (bad) and FD (bad): +1+0+1(+6)
- (U2 L2 B2 D)
    - After (L2 F2 U2 L2 B2), 1qt edges will be RV (bad) and FH (good): +1+2+0(+3)
- (U2 L2 B2 D')
    - After (B2 U2 L2), 1qt edges will be RD (bad) and FH (good), fr=1: +1+0+2(+5)
    - After (R2 F2 U2 R2 B2), 1qt edges will be RD (bad) and FD (bad), fr=1: +1+2+0(+6)
- (U2 L2 F2 D)
    - After (B2 U2 R2), 1qt edges will be RD (bad) and FH (good), fr=1: +1+0+2(+5)
    - After (F2 L2 U2 B2 L2), 1qt edges will be RD (bad) and FD (bad): +1+2+0(+6)
- (U2 L2 F2 D')
    - After (R2 F2 U2 R2 B2), 1qt edges will be RV (bad) and FH (good): +1+2+0(+3)
- 1 more variant of this skeleton passes the meta, not reached before the stop.

Skeleton starting with U B2 U' F2 U' has FV corners, L=10, 3 spare moves.

- U B2 U' F2 U'
    - After L2 F2 L2, 1qt edges will be FV (good) and RV (good): +0+3+0(+1)
- U B2 U' F2 U
    - After L2 F2 R2, 1qt edges will be FD (bad) and RV (good): +0+3+0(+3)
- U L2 F2 D L2 D
    - After R2 L2, 1qt edges will be FV (good) and RV (good): +1+2+0(+1)
- U B2 U' R2 B2 D
    - After R2 L2, 1qt edges will be FH (bad) and RD (bad): +1+2+0(+5)

Check inverse. Skeleton starting with (U2 F2 U' R2 D U) has HH corners. Apply U and NISS: FD corners.

- (U2 B2 U' B2 U)
    - After (F2 B2), 1qt edges will be FH (bad) and RH (good): +0+2+1(+3)
- (U2 B2 U' F2 U)
    - After (R2 L2), 1qt edges will be FV (bad) and RD (good): +0+2+1(+3)
- (U2 F2 D' F2 D)
    - After (L2 F2 L2), 1qt edges will be FD (good) and RV (bad): +0+3+0(+3)
- (U2 F2 D' F2 D')
    - After (L2 F2 R2), 1qt edges will be FH (bad) and RV (bad): +0+3+0(+5)
- (U2 R2 B2 U L2 U')
    - After (R2 L2), 1qt edges will be FD (good) and RD (good): +1+2+0(+1)
- (U2 F2 D' R2 B2 U')
    - After (R2 L2), 1qt edges will be FV (bad) and RD (good): +1+2+0(+3)
- (B2 U2 F2 D B2 D)
    - After (F2 B2), 1qt edges will be FH (bad) and RV (bad), fr=1: +1+2+0(+5)

Skeleton starting with U B2 U' L2 U' has FV corners, L=10, 3 spare moves.

- U B2 U' L2 U'
    - After F2 L2 B2, 1qt edges will be FV (good) and RH (good), fr=1: +0+3+0(+1)
- U F2 U' B2 U
    - After B2 L2 F2, 1qt edges will be FV (good) and RH (good), fr=1: +0+3+0(+1)
- U F2 U' F2 U'
    - After B2 R2 F2, 1qt edges will be FV (good) and RH (good), fr=1: +0+3+0(+1)
- U B2 U' L2 U
    - After F2 L2 F2, 1qt edges will be FV (good) and RV (good), fr=1: +0+3+0(+2)
- U F2 U' B2 U'
    - After F2 R2 B2, 1qt edges will be FV (good) and RD (bad), fr=1: +0+3+0(+2)
- U F2 U' F2 U
    - After F2 L2 B2, 1qt edges will be FV (good) and RD (bad), fr=1: +0+3+0(+2)
- U B2 U' B2 R2 D'
    - After F2 B2, 1qt edges will be FH (bad) and RD (bad), fr=1: +1+2+0(+5)
- U L2 F2 D F2 D'
    - After F2 B2, 1qt edges will be FH (bad) and RD (bad), fr=1: +1+2+0(+5)

Check inverse. Skeleton starting with (U2 F2 U R2 D U) has HH corners. Apply U and NISS: FD corners.

- (U2 F2 D B2 D)
    - After (R2 B2 R2), 1qt edges will be FD (good) and RV (bad), fr=1: +0+3+0(+5)
- (U2 F2 D B2 D')
    - After (R2 B2 L2), 1qt edges will be FV (bad) and RV (bad), fr=1: +0+3+0(+5)
- (B2 U2 F2 D' F2 D)
    - After (F2 B2), 1qt edges will be FV (bad) and RV (bad): +1+2+0(+5)
- (U2 F2 D L2 F2 U')
    - After (R2 L2), 1qt edges will be FH (bad) and RH (good), fr=1: +1+2+0(+5)
- (U2 R2 B2 U' R2 U')
    - After (R2 L2), 1qt edges will be FD (good) and RV (bad), fr=1: +1+2+0(+5)

Skeleton starting with U B2 U R2 U has FV corners, L=10, 3 spare moves.

- U B2 U R2 U
    - After B2 R2 B2, 1qt edges will be FV (good) and RV (good): +0+3+0(+1)
- U B2 U R2 U'
    - After B2 R2 F2, 1qt edges will be FV (good) and RD (bad): +0+3+0(+3)
- U B2 U F2 L2 D'
    - After F2 B2, 1qt edges will be FD (bad) and RH (good): +1+2+0(+3)
- U L2 F2 D' B2 D'
    - After F2 B2, 1qt edges will be FD (bad) and RD (bad): +1+2+0(+5)

Check inverse. Skeleton starting with (U2 F2 U F2 D U) has HH corners. Apply U and NISS: FD corners.

- (U2 B2 U L2 U)
    - After (F2 R2 B2), 1qt edges will be FD (good) and RH (good): +0+3+0(+0)
        - (F2 R2 B2 U' B2 U) // 2 pairs, no good
    - After (R2 B2 L2), 1qt edges will be FH (bad) and RV (bad): +0+3+0(+5)
- (U2 B2 U L2 U')
    - After (F2 R2 B2), 1qt edges will be FD (good) and RD (good): +0+3+0(+1)
- (U2 B2 U R2 U)
    - After (B2 R2 F2), 1qt edges will be FD (good) and RD (good): +0+3+0(+1)
- (U2 F2 D R2 D)
    - After (B2 R2 F2), 1qt edges will be FD (good) and RD (good): +0+3+0(+1)
- (U2 F2 D R2 D')
    - After (B2 R2 B2), 1qt edges will be FD (good) and RV (bad): +0+3+0(+3)
- (B2 U2 F2 D' R2 D')
    - After (R2 L2), 1qt edges will be FD (good) and RH (good), fr=1: +1+2+0(+3)
- (U2 F2 D F2 L2 U)
    - After (F2 B2), 1qt edges will be FH (bad) and RH (good): +1+2+0(+3)
- (U2 R2 B2 U' B2 U)
    - After (F2 B2), 1qt edges will be FH (bad) and RH (good): +1+2+0(+3)
- 1 more variant of this skeleton passes the meta, not reached before the stop.

Stop: 10 HTRs done, nothing within goal. This DR's optimal is 14, over the goal.

### 4b3, scramble 8

`R' U' F R' U2 L2 U' F D' L D2 L U' F R2 L2 U2 R2 B2 U' R2 U2 F2 R' U' F`

4b3 4e, goal 13.

Skeleton starting with U2 F2 U has HH corners, L=9, 4 spare moves. Apply (U') and NISS: RD corners.

- After U2 F2, 1qt edges will be RD (good) and FD (good): +0+1(+1)
    - U2 F2 U' F2 U2 F2 R2 U // 2 pairs, no good
    - U2 F2 U' F2 U2 B2 L2 D // 0 pairs, no good
- After U2 B2, 1qt edges will be RH (bad) and FH (good), fr=1: +0+1(+3)
    - U2 B2 U R2 U2 R2 B2 U' // 4 pairs, no good
- 233 more variants of this skeleton pass the meta, not reached before the stop.

The same skeleton in full, for the solutions that go on after its last quarter turn.

- U2 F2 U
    - After R2 U2 F2, 1qt edges will be RV (bad) and FH (good): +0+0+1(+3)
        - R2 U2 F2 U' F2 L2 U // 6 pairs, no good
        - R2 U2 F2 U' B2 R2 D' // 6 pairs, no good
- U2 F2 U'
    - After F2 U2 R2, 1qt edges will be RV (bad) and FH (good): +0+0+1(+3)
        - F2 U2 R2 U F2 L2 U // 6 pairs, no good
- U2 B2 D'
    - After B2 U2 R2, 1qt edges will be RV (bad) and FH (good): +0+0+3(+3)
- F2 U2 F2 U
    - After L2 U2 F2, 1qt edges will be RV (bad) and FD (bad): +1+0+1(+6)
    - After L2 U2 R2 B2, 1qt edges will be RH (good) and FD (bad): +1+1+1(+3)
- F2 U2 F2 U'
    - After F2 U2 L2, 1qt edges will be RV (bad) and FD (bad): +1+0+1(+6)
    - After B2 U2 F2 L2, 1qt edges will be RH (good) and FD (bad): +1+1+1(+3)
- U2 L2 F2 U
    - After B2 L2 U2 L2, 1qt edges will be RV (bad) and FH (good): +1+1+0(+3)
    - After R2 U2 R2 B2, 1qt edges will be RV (bad) and FD (bad): +1+1+0(+6)
    - After L2 U2 R2 L2 B2, 1qt edges will be RH (good) and FD (bad): +1+2+0(+3)
- U2 R2 F2 U
    - After F2 R2 U2 R2, 1qt edges will be RV (bad) and FH (good): +1+1+0(+3)
    - After L2 U2 L2 F2, 1qt edges will be RV (bad) and FD (bad): +1+1+0(+6)
    - After L2 U2 B2 R2 L2, 1qt edges will be RH (good) and FD (bad): +1+2+0(+3)
- U2 L2 B2 D'
    - After F2 R2 U2 L2, 1qt edges will be RV (bad) and FH (good), fr=1: +1+1+0(+5)
    - After F2 R2 L2 U2 L2, 1qt edges will be RV (bad) and FH (good): +1+2+0(+3)
- U2 R2 B2 D'
    - After B2 L2 U2 R2, 1qt edges will be RV (bad) and FH (good), fr=1: +1+1+0(+5)
    - After B2 R2 L2 U2 R2, 1qt edges will be RV (bad) and FH (good): +1+2+0(+3)
- 79 more variants of this skeleton pass the meta, not reached before the stop.

Check inverse. Skeleton starting with (U') has FV corners.

- (U')
    - After (L2), 1qt edges will be FV (good) and RV (good): +0+0+0(+1)
        - (L2 U R2 U2 B2 U') // 2 pairs, no good
        - (L2 U' B2 U2 R2 U) // 2 pairs, no good
    - After (R2), 1qt edges will be FD (bad) and RH (good), fr=1: +0+0+0(+2)
        - (R2 U L2 U2 F2 D R2 B2 R2 F2 D2 F2) // 4 pairs, 13
- 179 more variants of this skeleton pass the meta, not reached before the stop.

Skeleton starting with (U' R2 U R2 U2 F2 U') on inverse has HH corners, L=10, 3 spare moves. Apply D and NISS: HH corners.

- (D' F2 D)
    - After (R2 U2 B2), 1qt edges will be RH (good) and FH (good), fr=1: +0+0+0(+5)
    - After (R2 F2 U2 B2), 1qt edges will be RH (good) and FH (good): +0+1+0(+0)
        - (R2 F2 U2 B2 U B2 U) // 0 pairs, no good
- (D' B2 U')
    - After (L2 F2 U2 B2), 1qt edges will be RH (good) and FH (good), fr=1: +0+1+1(+5)
    - After (L2 F2 U2 F2), 1qt edges will be RV (bad) and FD (bad), fr=1: +0+1+1(+6)
    - After (L2 U2 B2), 1qt edges will be RH (good) and FH (good), fr=1: +0+0+3(+5)
- (D' B2 U)
    - After (L2 F2 U2 L2 B2), 1qt edges will be RV (bad) and FH (good): +0+2+1(+3)
- (D' L2 B2 U)
    - After (F2 L2 U2 R2), 1qt edges will be RH (good) and FH (good), fr=1: +1+1+1(+5)
    - After (F2 R2 U2 L2), 1qt edges will be RD (bad) and FD (bad), fr=1: +1+1+1(+6)
- (D' L2 B2 U')
    - After (L2 F2 U2 B2), 1qt edges will be RH (good) and FH (good), fr=1: +1+1+1(+5)
- 21 more variants of this skeleton pass the meta, not reached before the stop.

Stop: 10 HTRs done, one finish within goal (13). This DR's optimal is 13.

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
    - (R2 U' R2 L2 B2 R2 F2 U) // 4 pairs, no good
    - (R2 U' F2 R2 B2 R2 L2 U) // 4 pairs, no good
    - (R2 U' R2 L2 F2 L2 F2 D) // 2 pairs, no good
- 5 more variants of this skeleton pass the meta, not reached before the stop.

Skeleton starting with U D has HH corners, L=5, 7 spare moves. Apply (D) and NISS: HH corners.

- U
    - After L2 B2 R2, 1qt edges will be RH (good) and FH (good), fr=1: +0+3+1(+5)
    - After L2 B2 L2, 1qt edges will be RV (bad) and FV (bad), fr=1: +0+3+1(+6)

Check inverse. Skeleton starting with (D U') has HH corners. Apply U and NISS: HH corners.

- (U')
    - After (F2 B2), 1qt edges will be RD (bad) and FV (bad): +0+2+3(+6)

Skeleton starting with L2 has DD corners, L=6, 6 spare moves.

- After L2, 1qt edges will be FV (good) and RV (good): +0+5(+1)
    - L2 U R2 F2 L2 F2 B2 U' // 6 pairs, no good
    - L2 U F2 B2 L2 F2 R2 U' // 6 pairs, no good
    - L2 U R2 B2 R2 F2 B2 D' // 4 pairs, no good
- 5 more variants of this skeleton pass the meta, not reached before the stop.

Check inverse. Skeleton starting with (L2 U2 B2) has RD corners.

- After (L2 U2 B2), 1qt edges will be RD (good) and FD (good): +0+5(+1)
    - (L2 U2 B2 U L2 B2 R2 F2 B2 U') // 10 pairs, no good
    - (L2 U2 B2 U F2 B2 R2 B2 L2 U') // 10 pairs, no good
    - (L2 U2 B2 U R2 F2 R2 F2 B2 D') // 6 pairs, no good
- 13 more variants of this skeleton pass the meta, not reached before the stop.

Skeleton starting with F2 D U has HH corners, L=6, 6 spare moves. Apply (D) and NISS: HH corners.

- F2 D'
    - After R2 L2, 1qt edges will be RD (bad) and FV (bad): +0+2+0(+6)
    - After F2 L2 B2, 1qt edges will be RH (good) and FV (bad): +0+3+0(+3)
        - F2 L2 B2 U R2 U // no good
    - After F2 L2 B2, 1qt edges will be RH (good) and FV (bad): +0+3+2(+3)
- F2 D
    - After F2 L2 F2, 1qt edges will be RV (bad) and FV (bad): +0+3+0(+6)
    - After R2 F2 L2 F2 B2, 1qt edges will be RD (bad) and FH (good): +0+5+0(+3)
- L2 F2 D
    - After L2 B2 R2, 1qt edges will be RV (bad) and FH (good): +1+3+0(+3)
- R2 B2 U'
    - After L2 B2 R2, 1qt edges will be RV (bad) and FH (good): +1+3+0(+3)
- L2 F2 D'
    - After L2 B2 L2, 1qt edges will be RV (bad) and FD (bad): +1+3+0(+6)
- R2 B2 U
    - After L2 B2 L2, 1qt edges will be RV (bad) and FD (bad): +1+3+0(+6)
- 6 more variants of this skeleton pass the meta, not reached before the stop.

Stop: 10 HTRs done, nothing within goal. This DR's optimal is 13, over the goal.

### 0c0, scramble 2

`R' U' F R2 B' D' R U2 D2 L2 F2 R' B U B2 U B2 D' F2 R2 U' F2 D R' U' F`

0c0 2e, goal 12.

Skeleton starting with L2 has RD corners, L=4, 8 spare moves.

- After L2, 1qt edges will be RV (bad) and FH (good), fr=1: +0+3(+5)
    - L2 U F2 L2 B2 D // 8 pairs, no good
    - L2 U F2 R2 F2 U // 4 pairs, no good
    - L2 U B2 R2 B2 U // 4 pairs, no good
- 1 more variant of this skeleton passes the meta, not reached before the stop.

Check inverse. Skeleton starting with (L2) has RD corners.

- After (L2), 1qt edges will be RH (bad) and FH (good), fr=1: +0+3(+5)
    - (L2 U' F2 R2 B2 D') // 4 pairs, no good
    - (L2 U' F2 L2 F2 U') // 4 pairs, no good
    - (L2 U' B2 R2 F2 D') // 4 pairs, no good
- 1 more variant of this skeleton passes the meta, not reached before the stop.

Skeleton starting with U has DD corners, L=5, 7 spare moves.

- With no setup, 1qt edges will be FH (bad) and RD (good): +0+3(+3)
    - U F2 R2 F2 U R2 U2 B2 L2 B2 L2 D2 // 4 pairs, 12
    - U F2 L2 B2 D // 4 pairs, no good
    - U B2 R2 B2 U R2 U2 B2 R2 B2 R2 D2 // 4 pairs, 12
- 1 more variant of this skeleton passes the meta, not reached before the stop.

Stop: 2 finishes within goal (12, 12), after 9 HTRs. This DR's optimal is 11.

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
        - R2 B2 U' F2 U2 B2 U' // 4 pairs, no good
        - R2 B2 U' B2 U2 B2 U' // 4 pairs, no good
- F2 R2 U'
    - After F2, 1qt edges will be FV (bad) and RH (good), fr=1: +1+0+1(+5)
    - After F2, 1qt edges will be FV (bad) and RH (good): +1+0+4(+3)
- B2 R2 D'
    - After B2 R2, 1qt edges will be FH (bad) and RH (good), fr=1: +1+1+0(+5)
    - After B2 R2, 1qt edges will be FH (bad) and RH (good): +1+1+2(+3)
- F2 L2 U'
    - After B2 R2, 1qt edges will be FV (bad) and RV (bad), fr=1: +1+1+0(+5)
    - After L2 F2 B2, 1qt edges will be FD (good) and RV (bad): +1+2+2(+3)
- B2 L2 U'
    - After L2, 1qt edges will be FH (bad) and RH (good): +1+0+3(+3)
    - After R2, 1qt edges will be FV (bad) and RV (bad): +1+0+3(+5)
    - After L2, 1qt edges will be FH (bad) and RH (good): +1+0+4(+3)
- B2 L2 U
    - After R2 U2 L2, 1qt edges will be FH (bad) and RH (good): +1+2+1(+3)
- F2 L2 U
    - After F2 L2 U2 B2, 1qt edges will be FV (bad) and RH (good): +1+3+0(+3)
    - After L2 U2 B2 R2, 1qt edges will be FV (bad) and RV (bad): +1+3+0(+5)
    - After R2 F2 B2 U2 L2, 1qt edges will be FD (good) and RV (bad): +1+4+0(+3)
- F2 R2 U
    - After R2 B2 U2 R2, 1qt edges will be FV (bad) and RH (good): +1+3+1(+3)
    - After L2 F2 U2 R2, 1qt edges will be FH (bad) and RV (bad): +1+3+1(+5)
- 20 more variants of this skeleton pass the meta, not reached before the stop.

Check inverse. Skeleton starting with (F2 U') has RD corners.

- (F2 U')
    - After (L2), 1qt edges will be RH (bad) and FD (good), fr=1: +0+0+3(+5)
- (B2 D')
    - After (F2 R2), 1qt edges will be RV (bad) and FV (bad), fr=1: +0+1+0(+5)
        - (F2 R2 U' B2 U') // no good
    - After (L2 B2 U2 F2 U2 F2), 1qt edges will be RV (bad) and FD (good): +0+5+0(+3)
- (F2 U)
    - After (B2 L2 U2 B2), 1qt edges will be RD (good) and FV (bad): +0+3+1(+3)
- (B2 D)
    - After (B2 L2 U2 B2), 1qt edges will be RD (good) and FV (bad): +0+3+0(+3)
        - (B2 L2 U2 B2 U F2 U') // no good
- (L2 F2 U)
    - After (B2), 1qt edges will be RH (bad) and FV (bad), fr=1: +1+0+1(+5)
    - After (L2 F2), 1qt edges will be RH (bad) and FH (good): +1+1+3(+3)
- (L2 B2 D)
    - After (R2 F2), 1qt edges will be RH (bad) and FH (good), fr=1: +1+1+0(+5)
    - After (B2 R2 L2), 1qt edges will be RD (good) and FH (good), fr=1: +1+2+0(+3)
        - (B2 R2 L2 U' F2 U') // no good
    - After (F2 R2 L2 F2 B2), 1qt edges will be RD (good) and FH (good), fr=1: +1+4+0(+3)
- (R2 F2 U)
    - After (R2 F2), 1qt edges will be RV (bad) and FV (bad), fr=1: +1+1+0(+5)
    - After (B2 U2 L2 B2 R2), 1qt edges will be RD (good) and FH (good), fr=1: +1+4+0(+3)
- (R2 B2 U)
    - After (L2), 1qt edges will be RH (bad) and FH (good): +1+0+3(+3)
- (R2 B2 U')
    - After (R2 U2 L2), 1qt edges will be RH (bad) and FH (good): +1+2+1(+3)
    - After (R2 U2 R2), 1qt edges will be RV (bad) and FV (bad): +1+2+1(+5)
- (R2 F2 U')
    - After (L2 B2 U2 R2), 1qt edges will be RV (bad) and FH (good): +1+3+0(+3)
    - After (F2 U2 R2 F2), 1qt edges will be RV (bad) and FV (bad): +1+3+0(+5)
- (L2 F2 U')
    - After (L2 F2 U2 L2), 1qt edges will be RV (bad) and FH (good): +1+3+1(+3)
    - After (F2 B2 U2 F2), 1qt edges will be RV (bad) and FH (good), fr=1: +1+3+1(+5)
- 9 more variants of this skeleton pass the meta, not reached before the stop.

Skeleton starting with R2 U R2 U' B2 D has FD corners, L=9, 4 spare moves.

- R2 U R2 U' B2 D
    - After R2 L2, 1qt edges will be FD (good) and RD (good), fr=1: +0+2+2(+4)
- R2 U R2 U' B2 D'
    - After R2 L2, 1qt edges will be FD (good) and RD (good), fr=1: +0+2+2(+4)
- R2 U R2 U' F2 U
    - After F2 B2, 1qt edges will be FD (good) and RD (good), fr=1: +0+2+2(+4)
- R2 U R2 U' F2 U'
    - After F2 B2, 1qt edges will be FD (good) and RD (good), fr=1: +0+2+2(+4)

Skeleton starting with (F2 U' R2 U L2 D) on inverse has RD corners, L=9, 4 spare moves.

- (F2 U' R2 U L2 D)
    - After (F2 B2), 1qt edges will be RD (good) and FD (good), fr=1: +0+2+2(+4)
- (F2 U' R2 U L2 D')
    - After (R2 L2), 1qt edges will be RD (good) and FD (good), fr=1: +0+2+2(+4)
- (F2 U' R2 U R2 U)
    - After (R2 L2), 1qt edges will be RD (good) and FD (good), fr=1: +0+2+2(+4)
- (F2 U' R2 U R2 U')
    - After (R2 L2), 1qt edges will be RD (good) and FD (good), fr=1: +0+2+2(+4)

Skeleton starting with R2 U R2 U' F2 U has HH corners, L=9, 4 spare moves. Apply (U) and NISS: HH corners.

- L2 U B2 D'
    - After R2 F2, 1qt edges will be RV (bad) and FD (bad), fr=1: +0+1+0(+6)
    - After L2 F2 L2 B2 L2, 1qt edges will be RV (bad) and FH (good), fr=1: +0+4+0(+5)
- L2 U F2 U'
    - After F2, 1qt edges will be RH (good) and FV (bad): +0+0+3(+3)
    - After B2, 1qt edges will be RV (bad) and FD (bad): +0+0+3(+6)
- R2 D F2 U'
    - After B2, 1qt edges will be RD (bad) and FH (good), fr=1: +0+0+3(+5)
    - After F2, 1qt edges will be RH (good) and FD (bad): +0+0+4(+3)
- R2 D B2 U'
    - After L2, 1qt edges will be RD (bad) and FV (bad), fr=1: +0+0+3(+6)
- L2 U F2 U
    - After F2 U2 F2, 1qt edges will be RH (good) and FV (bad): +0+2+1(+3)
- L2 U B2 D
    - After L2 B2 U2 L2, 1qt edges will be RV (bad) and FV (bad): +0+3+0(+6)
    - After F2 R2 F2 U2 L2, 1qt edges will be RV (bad) and FH (good), fr=1: +0+4+0(+5)
- R2 D R2 B2 D
    - After L2, 1qt edges will be RV (bad) and FD (bad), fr=1: +1+0+0(+6)
- B2 R2 D' R2 U
    - After B2, 1qt edges will be RV (bad) and FH (good), fr=1: +1+0+1(+5)
    - After B2, 1qt edges will be RV (bad) and FH (good): +1+0+3(+3)
- F2 L2 U' L2 D
    - After R2 F2, 1qt edges will be RV (bad) and FH (good), fr=1: +1+1+0(+5)
    - After R2 F2, 1qt edges will be RV (bad) and FH (good): +1+1+2(+3)
- R2 D R2 F2 D
    - After L2 B2, 1qt edges will be RV (bad) and FH (good), fr=1: +1+1+0(+5)
    - After L2 B2, 1qt edges will be RV (bad) and FH (good): +1+1+2(+3)
- L2 U L2 B2 D
    - After F2 R2, 1qt edges will be RD (bad) and FV (bad), fr=1: +1+1+0(+6)
    - After L2 B2 L2 F2, 1qt edges will be RH (good) and FH (good), fr=1: +1+3+0(+5)
- R2 D L2 B2 U
    - After F2, 1qt edges will be RD (bad) and FV (bad), fr=1: +1+0+2(+6)
    - After L2 B2 R2 L2, 1qt edges will be RH (good) and FV (bad), fr=1: +1+3+0(+5)
- L2 U L2 F2 U
    - After F2 R2, 1qt edges will be RV (bad) and FD (bad), fr=1: +1+1+1(+6)
- L2 U R2 F2 U'
    - After R2 U2 R2, 1qt edges will be RV (bad) and FH (good): +1+2+0(+3)
- F2 R2 D' L2 U
    - After B2 R2 L2, 1qt edges will be RV (bad) and FH (good), fr=1: +1+2+0(+5)
- B2 R2 D' L2 U'
    - After R2 U2 R2, 1qt edges will be RD (bad) and FD (bad): +1+2+0(+6)
    - After B2 R2 U2 B2, 1qt edges will be RV (bad) and FH (good): +1+3+0(+3)
- F2 R2 D' R2 U
    - After F2 B2 R2, 1qt edges will be RD (bad) and FD (bad), fr=1: +1+2+0(+6)
- R2 D R2 B2 D'
    - After L2 U2 R2, 1qt edges will be RV (bad) and FD (bad): +1+2+0(+6)
- L2 U R2 B2 U
    - After B2, 1qt edges will be RH (good) and FH (good), fr=1: +1+0+3(+5)
- B2 L2 U' L2 D
    - After L2, 1qt edges will be RD (bad) and FD (bad), fr=1: +1+0+3(+6)
- F2 L2 U' R2 U
    - After B2, 1qt edges will be RD (bad) and FD (bad), fr=1: +1+0+3(+6)
- R2 D L2 F2 U
    - After R2 L2 F2 R2, 1qt edges will be RH (good) and FV (bad), fr=1: +1+3+0(+5)
- F2 R2 D' L2 U'
    - After B2 U2 R2 B2, 1qt edges will be RH (good) and FH (good): +1+3+0(+0)
        - B2 U2 R2 B2 U' B2 U' // 6 pairs, no good
- R2 D L2 B2 U'
    - After R2 F2 U2 L2, 1qt edges will be RH (good) and FH (good): +1+3+0(+0)
        - R2 F2 U2 L2 U' B2 U' // 4 pairs, no good
- F2 L2 U' L2 D'
    - After B2 U2 L2 B2, 1qt edges will be RV (bad) and FH (good): +1+3+0(+3)
    - After L2 B2 U2 L2, 1qt edges will be RV (bad) and FV (bad): +1+3+0(+6)
- F2 R2 D' R2 U'
    - After F2 R2 U2 B2, 1qt edges will be RH (good) and FV (bad): +1+3+0(+3)
- R2 D L2 F2 U'
    - After L2 U2 B2 R2, 1qt edges will be RH (good) and FV (bad): +1+3+0(+3)
- R2 D R2 F2 D'
    - After B2 U2 R2 F2, 1qt edges will be RV (bad) and FH (good): +1+3+0(+3)
    - After L2 B2 U2 R2, 1qt edges will be RV (bad) and FV (bad): +1+3+0(+6)
- B2 R2 D' L2 U
    - After B2 R2 F2 B2, 1qt edges will be RD (bad) and FH (good), fr=1: +1+3+0(+5)
    - After L2 U2 R2 L2, 1qt edges will be RD (bad) and FD (bad), fr=1: +1+3+0(+6)
- L2 U R2 F2 U
    - After L2 B2 R2 B2, 1qt edges will be RH (good) and FH (good), fr=1: +1+3+0(+5)
    - After B2 R2 F2 B2, 1qt edges will be RV (bad) and FD (bad), fr=1: +1+3+0(+6)
- L2 U L2 B2 D'
    - After R2 U2 B2 L2, 1qt edges will be RD (bad) and FV (bad): +1+3+0(+6)

The same skeleton in full, for the solutions that go on after its last quarter turn.

- R2 U L2 U' L2 U
    - After B2, 1qt edges will be RD (bad) and FH (good), fr=1: +0+0+3(+5)
- L2 U F2 U' F2 U
    - After B2, 1qt edges will be RD (bad) and FV (bad), fr=1: +0+0+3(+6)
    - After R2 B2, 1qt edges will be RH (good) and FV (bad), fr=1: +0+1+3(+5)
- L2 U B2 U' R2 U
    - After R2 F2, 1qt edges will be RH (good) and FV (bad), fr=1: +0+1+2(+5)
- L2 U F2 U' L2 B2 D'
    - After L2, 1qt edges will be RH (good) and FD (bad), fr=1: +1+0+2(+5)
- L2 U L2 B2 D R2 D'
    - After L2, 1qt edges will be RD (bad) and FH (good), fr=1: +1+0+2(+5)
- B2 R2 D' R2 D R2 D'
    - After L2, 1qt edges will be RD (bad) and FD (bad), fr=1: +1+0+2(+6)
- L2 U L2 F2 U L2 U'
    - After R2, 1qt edges will be RD (bad) and FH (good), fr=1: +1+0+3(+5)
- L2 U R2 F2 U R2 U'
    - After L2, 1qt edges will be RD (bad) and FH (good), fr=1: +1+0+3(+5)
- F2 L2 U' L2 U L2 U'
    - After R2, 1qt edges will be RD (bad) and FD (bad), fr=1: +1+0+3(+6)
- F2 R2 U' F2 U L2 D'
    - After L2, 1qt edges will be RD (bad) and FV (bad), fr=1: +1+0+3(+6)
- F2 R2 U' F2 U R2 U'
    - After L2, 1qt edges will be RV (bad) and FV (bad), fr=1: +1+0+3(+6)
- L2 U F2 U' L2 F2 U'
    - After R2, 1qt edges will be RV (bad) and FD (bad), fr=1: +1+0+3(+6)
- L2 U F2 U' R2 B2 D'
    - After L2, 1qt edges will be RD (bad) and FD (bad), fr=1: +1+0+3(+6)
- R2 U B2 L2 D R2 U'
    - After L2, 1qt edges will be RD (bad) and FV (bad), fr=1: +1+0+3(+6)
- R2 U B2 R2 U R2 D'
    - After L2, 1qt edges will be RD (bad) and FV (bad), fr=1: +1+0+3(+6)
- R2 U F2 L2 D L2 U'
    - After R2, 1qt edges will be RD (bad) and FV (bad), fr=1: +1+0+3(+6)
- R2 U F2 R2 U L2 D'
    - After R2, 1qt edges will be RD (bad) and FV (bad), fr=1: +1+0+3(+6)
- B2 L2 U' R2 U L2 D'
    - After B2 R2, 1qt edges will be RH (good) and FD (bad), fr=1: +1+1+2(+5)
- B2 L2 U' R2 U R2 U'
    - After F2 R2, 1qt edges will be RD (bad) and FH (good), fr=1: +1+1+2(+5)
- L2 U B2 U' B2 L2 D'
    - After B2 L2, 1qt edges will be RH (good) and FD (bad), fr=1: +1+1+2(+5)
- B2 L2 U' L2 U B2 D'
    - After F2 R2, 1qt edges will be RV (bad) and FD (bad), fr=1: +1+1+2(+6)
- B2 L2 U' L2 U F2 U'
    - After F2 L2, 1qt edges will be RD (bad) and FV (bad), fr=1: +1+1+2(+6)
- F2 L2 U' R2 U B2 U'
    - After F2 R2, 1qt edges will be RD (bad) and FV (bad), fr=1: +1+1+2(+6)
- L2 U B2 U' F2 L2 D'
    - After F2 R2, 1qt edges will be RV (bad) and FV (bad), fr=1: +1+1+2(+6)

Skeleton starting with (F2 U' R2 U R2 U') on inverse has HH corners, L=9, 4 spare moves. Apply D and NISS: HH corners.

- (F2 U' R2 U)
    - After (L2), 1qt edges will be RV (bad) and FD (bad), fr=1: +0+0+1(+6)
- (B2 D' L2 U)
    - After (F2), 1qt edges will be RV (bad) and FD (bad): +0+0+3(+6)
    - After (L2 F2), 1qt edges will be RV (bad) and FH (good): +0+1+3(+3)
- (F2 U' L2 D)
    - After (L2 F2 R2 F2), 1qt edges will be RH (good) and FH (good), fr=1: +0+3+0(+5)
    - After (F2 R2 F2 B2), 1qt edges will be RD (bad) and FD (bad), fr=1: +0+3+0(+6)
    - After (R2 F2 R2 L2 B2), 1qt edges will be RD (bad) and FH (good), fr=1: +0+4+0(+5)
- (B2 D' R2 U)
    - After (B2 L2), 1qt edges will be RD (bad) and FD (bad), fr=1: +0+1+3(+6)
- (F2 U' L2 D')
    - After (R2 U2 L2), 1qt edges will be RD (bad) and FH (good): +0+2+0(+3)
- (B2 D' L2 U')
    - After (F2 U2 R2 B2), 1qt edges will be RV (bad) and FH (good): +0+3+1(+3)
    - After (B2 U2 R2 F2), 1qt edges will be RD (bad) and FD (bad): +0+3+1(+6)
- (F2 U' R2 U')
    - After (R2 L2 U2 R2), 1qt edges will be RD (bad) and FV (bad), fr=1: +0+3+1(+6)
- (F2 U' B2 R2 U')
    - After (R2 B2), 1qt edges will be RD (bad) and FH (good), fr=1: +1+1+0(+5)
    - After (R2 B2), 1qt edges will be RD (bad) and FH (good): +1+1+2(+3)
- (R2 F2 U F2 D')
    - After (B2 R2), 1qt edges will be RD (bad) and FH (good), fr=1: +1+1+0(+5)
    - After (B2 R2), 1qt edges will be RD (bad) and FH (good): +1+1+2(+3)
- (L2 B2 D F2 U')
    - After (R2 B2), 1qt edges will be RD (bad) and FD (bad), fr=1: +1+1+0(+6)
    - After (F2 L2 F2 R2), 1qt edges will be RV (bad) and FH (good), fr=1: +1+3+0(+5)
- (L2 F2 U F2 D')
    - After (R2 F2), 1qt edges will be RD (bad) and FV (bad), fr=1: +1+1+0(+6)
- (F2 U' B2 L2 U')
    - After (B2 R2), 1qt edges will be RD (bad) and FH (good), fr=1: +1+1+1(+5)
    - After (B2 L2), 1qt edges will be RV (bad) and FV (bad), fr=1: +1+1+1(+6)
- (R2 F2 U B2 U')
    - After (B2 R2), 1qt edges will be RH (good) and FD (bad), fr=1: +1+1+1(+5)
- (F2 U' F2 L2 D)
    - After (B2 U2 F2), 1qt edges will be RH (good) and FV (bad): +1+2+0(+3)
- (L2 F2 U B2 D)
    - After (L2 U2 L2), 1qt edges will be RH (good) and FD (bad): +1+2+0(+3)
- (B2 D' F2 R2 U')
    - After (B2), 1qt edges will be RH (good) and FH (good): +1+0+3(+0)
        - (B2 U' L2 F2 U2 L2 D) // 8 pairs, no good
        - (B2 U' R2 B2 U2 R2 U) // 8 pairs, no good
- (L2 B2 D B2 U')
    - After (L2), 1qt edges will be RH (good) and FV (bad): +1+0+3(+3)
    - After (R2), 1qt edges will be RD (bad) and FD (bad): +1+0+3(+6)
- (F2 U' F2 R2 U')
    - After (F2), 1qt edges will be RH (good) and FD (bad), fr=1: +1+0+3(+5)
- (B2 D' B2 R2 U')
    - After (F2), 1qt edges will be RV (bad) and FV (bad): +1+0+3(+6)
- (R2 B2 D F2 U')
    - After (L2), 1qt edges will be RD (bad) and FD (bad), fr=1: +1+0+3(+6)
- (L2 B2 D B2 U)
    - After (R2 U2 L2), 1qt edges will be RH (good) and FV (bad): +1+2+1(+3)
- (F2 U' B2 R2 U)
    - After (B2 U2 R2 B2), 1qt edges will be RD (bad) and FH (good): +1+3+0(+3)
    - After (L2 F2 U2 R2), 1qt edges will be RD (bad) and FV (bad): +1+3+0(+6)
- (L2 F2 U F2 D)
    - After (R2 F2 U2 L2), 1qt edges will be RD (bad) and FH (good): +1+3+0(+3)
- (F2 U' F2 L2 D')
    - After (F2 L2 B2 L2), 1qt edges will be RH (good) and FD (bad), fr=1: +1+3+0(+5)
    - After (L2 B2 R2 L2), 1qt edges will be RV (bad) and FV (bad), fr=1: +1+3+0(+6)
- (L2 F2 U B2 D')
    - After (L2 U2 R2 L2), 1qt edges will be RH (good) and FD (bad), fr=1: +1+3+0(+5)
- (L2 B2 D F2 U)
    - After (L2 F2 U2 R2), 1qt edges will be RD (bad) and FV (bad): +1+3+0(+6)
- 3 more variants of this skeleton pass the meta, not reached before the stop.

Stop: 10 HTRs done, nothing within goal. This DR's optimal is 12.

### 2c3, scramble 2

`R' U' F R2 F' D' R L2 U' R2 D' F' R2 U2 F2 R2 D F2 R2 F2 U R2 D' R' U' F`

2c3 4e, goal 13.

Skeleton starting with U2 B2 D has FD corners, L=8, 5 spare moves.

- U2 F2 D
    - After R2 B2, 1qt edges will be FV (bad) and RV (bad), fr=1: +0+1+0(+5)
    - After B2 R2 B2 R2, 1qt edges will be FD (good) and RD (good): +0+3+2(+1)
- U2 B2 D'
    - After L2 U2 L2, 1qt edges will be FD (good) and RH (good): +0+2+0(+0)
        - L2 U2 L2 U R2 U // no good
    - After L2 U2 L2, 1qt edges will be FD (good) and RH (good): +0+2+2(+0)
        - L2 U2 L2 U F2 B2 L2 D // no good
- U2 F2 D'
    - After F2 U2 L2 F2, 1qt edges will be FV (bad) and RV (bad): +0+3+0(+5)
    - After F2 U2 B2 R2 L2, 1qt edges will be FV (bad) and RD (good): +0+4+0(+3)
    - After F2 U2 F2 R2 B2 R2, 1qt edges will be FH (bad) and RD (good): +0+5+0(+3)
- F2 U2 F2 D'
    - After L2 F2, 1qt edges will be FV (bad) and RH (good): +1+1+0(+3)
        - L2 F2 U R2 U // no good
- B2 U2 B2 D
    - After R2 U2 R2, 1qt edges will be FD (good) and RV (bad), fr=1: +1+2+0(+5)
    - After R2 L2 U2 R2, 1qt edges will be FD (good) and RV (bad): +1+3+0(+3)
- U2 R2 B2 U'
    - After R2, 1qt edges will be FD (good) and RV (bad): +1+0+3(+3)
- U2 R2 B2 U
    - After L2 U2 R2, 1qt edges will be FD (good) and RV (bad): +1+2+1(+3)
- B2 U2 F2 D
    - After R2 B2 U2 L2, 1qt edges will be FV (bad) and RV (bad), fr=1: +1+3+0(+5)
- F2 U2 F2 D
    - After B2 U2 R2 B2, 1qt edges will be FV (bad) and RH (good), fr=1: +1+3+0(+5)
- 38 more variants of this skeleton pass the meta, not reached before the stop.

Check inverse. Skeleton starting with (F2 D) has FV corners.

- (F2 D)
    - After (R2), 1qt edges will be FD (bad) and RV (good), fr=1: +0+0+2(+2)
        - (R2 U' B2 R2 L2 D) // no good
    - After (R2), 1qt edges will be FD (bad) and RV (good), fr=1: +0+0+3(+2)
        - (R2 U R2 L2 U2 B2 D') // 6 pairs, no good
        - (R2 U' B2 U2 R2 L2 D) // 6 pairs, no good
- (F2 D')
    - After (F2 R2 U2 F2), 1qt edges will be FH (bad) and RD (bad): +0+3+0(+5)
    - After (R2 B2 L2 U2 B2), 1qt edges will be FH (bad) and RH (good), fr=1: +0+4+0(+2)
    - After (R2 B2 U2 B2 U2 L2), 1qt edges will be FH (bad) and RH (good), fr=1: +0+5+0(+2)
- (R2 B2 U')
    - After (F2), 1qt edges will be FH (bad) and RH (good), fr=1: +1+0+3(+2)
- 19 more variants of this skeleton pass the meta, not reached before the stop.

Skeleton starting with B2 D' has DD corners, L=9, 4 spare moves.

- B2 D'
    - After F2, 1qt edges will be FV (good) and RD (good): +0+0+3(+0)
        - F2 U B2 L2 F2 R2 D // 4 pairs, no good
        - F2 U B2 L2 B2 L2 U // 4 pairs, no good
        - F2 U B2 R2 F2 L2 D // 4 pairs, no good
- F2 U'
    - After R2 F2, 1qt edges will be FV (good) and RH (bad): +0+1+3(+3)
- F2 U
    - After F2 U2 R2 F2, 1qt edges will be FV (good) and RH (bad): +0+3+1(+3)
- L2 B2 D
    - After F2 L2, 1qt edges will be FH (bad) and RV (good): +1+1+0(+3)
- L2 F2 U
    - After F2 R2, 1qt edges will be FV (good) and RH (bad): +1+1+0(+3)
- R2 B2 D
    - After B2 R2, 1qt edges will be FH (bad) and RV (good): +1+1+0(+3)
- R2 F2 U
    - After B2 L2, 1qt edges will be FV (good) and RH (bad): +1+1+0(+3)
- 5 more variants of this skeleton pass the meta, not reached before the stop.

Check inverse. Skeleton starting with (B2 U2 L2 U) has FD corners.

- (B2 U2 L2 U)
    - After (L2), 1qt edges will be FD (good) and RD (good): +0+0+2(+1)
        - (L2 U L2 F2 B2 D) // no good
- (L2 U2 B2 D)
    - After (R2 B2 R2 B2), 1qt edges will be FD (good) and RH (good), fr=1: +0+3+0(+3)
- (R2 U2 B2 U)
    - After (L2 B2 L2 B2), 1qt edges will be FD (good) and RH (good), fr=1: +0+3+0(+3)
    - After (L2 U2 R2 L2), 1qt edges will be FD (good) and RD (good), fr=1: +0+3+0(+4)
- (L2 U2 F2 D)
    - After (L2 F2), 1qt edges will be FH (bad) and RD (good), fr=1: +0+1+0(+5)
    - After (L2 U2 F2 U2 F2), 1qt edges will be FH (bad) and RD (good): +0+4+0(+3)
- (R2 U2 F2 U)
    - After (R2 F2), 1qt edges will be FV (bad) and RV (bad), fr=1: +0+1+0(+5)
    - After (F2 R2 F2 R2), 1qt edges will be FD (good) and RH (good), fr=1: +0+3+0(+3)
- (L2 U2 B2 D')
    - After (R2 U2 R2), 1qt edges will be FD (good) and RV (bad): +0+2+0(+3)
- (B2 U2 L2 U')
    - After (B2 L2 U2 F2), 1qt edges will be FH (bad) and RV (bad), fr=1: +0+3+0(+5)
    - After (F2 B2 U2 F2 L2), 1qt edges will be FH (bad) and RD (good): +0+4+0(+3)
- (F2 U2 L2 D')
    - After (F2 L2 U2 F2), 1qt edges will be FV (bad) and RD (good), fr=1: +0+3+0(+5)
    - After (L2 B2 R2 U2 B2), 1qt edges will be FV (bad) and RH (good): +0+4+0(+3)
- (L2 U2 F2 D')
    - After (B2 U2 R2 B2), 1qt edges will be FH (bad) and RD (good): +0+3+0(+3)
- (B2 U2 R2 U')
    - After (B2 U2 L2 F2), 1qt edges will be FV (bad) and RV (bad), fr=1: +0+3+0(+5)
    - After (B2 R2 B2 U2 L2), 1qt edges will be FD (good) and RV (bad): +0+4+0(+3)
- (F2 U2 R2 D')
    - After (F2 U2 R2 F2), 1qt edges will be FH (bad) and RD (good), fr=1: +0+3+0(+5)
    - After (F2 R2 F2 U2 R2), 1qt edges will be FD (good) and RD (good): +0+4+0(+1)
- (R2 U2 F2 U')
    - After (B2 U2 R2 F2), 1qt edges will be FV (bad) and RV (bad): +0+3+0(+5)
    - After (B2 U2 B2 R2 L2), 1qt edges will be FV (bad) and RH (good): +0+4+0(+3)
- (L2 B2 U2 F2 D')
    - After (L2 F2), 1qt edges will be FV (bad) and RD (good): +1+1+0(+3)
- (R2 B2 U2 F2 U')
    - After (L2 B2), 1qt edges will be FV (bad) and RD (good): +1+1+0(+3)
- (L2 F2 U2 F2 D')
    - After (R2 B2), 1qt edges will be FH (bad) and RV (bad): +1+1+0(+5)
- (R2 F2 U2 F2 U')
    - After (R2 F2), 1qt edges will be FH (bad) and RV (bad): +1+1+0(+5)
- (U2 F2 U2 L2 D')
    - After (R2 B2), 1qt edges will be FH (bad) and RD (good), fr=1: +1+1+0(+5)
- (U2 F2 U2 R2 U')
    - After (R2 F2), 1qt edges will be FV (bad) and RV (bad), fr=1: +1+1+0(+5)
- (U2 L2 U2 F2 D')
    - After (R2), 1qt edges will be FD (good) and RV (bad): +1+0+2(+3)
- (B2 R2 U2 L2 U')
    - After (R2), 1qt edges will be FD (good) and RD (good), fr=1: +1+0+2(+4)
- (F2 R2 U2 L2 D')
    - After (L2), 1qt edges will be FD (good) and RD (good), fr=1: +1+0+2(+4)
- (B2 L2 U2 L2 U')
    - After (L2), 1qt edges will be FD (good) and RV (bad), fr=1: +1+0+2(+5)
- (F2 L2 U2 L2 D')
    - After (R2), 1qt edges will be FD (good) and RV (bad), fr=1: +1+0+2(+5)
- (U2 B2 U2 L2 D)
    - After (L2 U2 L2), 1qt edges will be FD (good) and RV (bad): +1+2+0(+3)
- (L2 B2 U2 B2 D)
    - After (L2 U2 L2), 1qt edges will be FD (good) and RD (good), fr=1: +1+2+0(+4)
- (R2 B2 U2 B2 U)
    - After (L2 U2 R2), 1qt edges will be FD (good) and RD (good), fr=1: +1+2+0(+4)
- (L2 F2 U2 B2 D)
    - After (R2 U2 R2), 1qt edges will be FD (good) and RV (bad), fr=1: +1+2+0(+5)
- (R2 F2 U2 B2 U)
    - After (R2 U2 L2), 1qt edges will be FD (good) and RV (bad), fr=1: +1+2+0(+5)
- 9 more variants of this skeleton pass the meta, not reached before the stop.

Stop: 10 HTRs done, nothing within goal. This DR's optimal is 13.

### 2c3, scramble 3

`R' U' F R' F U2 D B R2 F2 D U2 B2 L' D2 F2 B2 R' L2 B2 U2 R2 U2 R' U' F`

2c3 2e, goal 13.

Skeleton starting with F2 U' has FV corners, L=8, 5 spare moves.

- F2 U'
    - After B2 L2, 1qt edges will be FV (good) and RV (good): +0+1+0(+1)
        - B2 L2 U' B2 U B2 L2 U2 R2 L2 // 12
    - After R2 F2 R2 B2, 1qt edges will be FH (bad) and RH (good): +0+3+0(+3)
    - After B2 L2, 1qt edges will be FV (good) and RV (good): +0+1+4(+1)
- B2 U'
    - After L2 B2, 1qt edges will be FV (good) and RV (good): +0+1+1(+1)
        - L2 B2 U' R2 F2 D' // 2 pairs, no good
        - L2 B2 U' L2 B2 U' // 2 pairs, no good
    - After L2 F2, 1qt edges will be FD (bad) and RD (bad): +0+1+1(+5)
- B2 U
    - After R2 L2 U2 R2 F2, 1qt edges will be FV (good) and RV (good): +0+4+1(+1)
    - After R2 L2 U2 R2 B2, 1qt edges will be FD (bad) and RD (bad): +0+4+1(+5)
- R2 F2 U
    - After L2 B2, 1qt edges will be FD (bad) and RD (bad): +1+1+0(+5)
    - After F2 R2 F2 L2, 1qt edges will be FH (bad) and RV (good): +1+3+0(+3)
- R2 F2 U'
    - After R2 F2 U2 L2, 1qt edges will be FV (good) and RD (bad), fr=1: +1+3+0(+2)
- 29 more variants of this skeleton pass the meta, not reached before the stop.

Check inverse. Skeleton starting with (U2 B2 U) has FD corners.

- (U2 B2 U)
    - After (B2), 1qt edges will be FD (good) and RD (good): +0+0+1(+1)
        - (B2 U' R2 B2 U R2 L2 U2 F2 L2) // 4 pairs, 13
    - After (B2 R2 L2), 1qt edges will be FH (bad) and RV (bad): +0+2+1(+5)
    - After (B2), 1qt edges will be FD (good) and RD (good): +0+0+5(+1)
- (U2 B2 U')
    - After (R2 B2 U2 L2), 1qt edges will be FD (good) and RD (good), fr=1: +0+3+1(+4)
    - After (B2 U2 B2), 1qt edges will be FD (good) and RD (good): +0+2+3(+1)
- (B2 U2 B2 U')
    - After (B2), 1qt edges will be FD (good) and RV (bad), fr=1: +1+0+1(+5)
    - After (B2), 1qt edges will be FD (good) and RV (bad): +1+0+3(+3)
- (F2 U2 F2 D')
    - After (L2 B2), 1qt edges will be FH (bad) and RV (bad), fr=1: +1+1+0(+5)
- (U2 R2 F2 U')
    - After (R2 B2), 1qt edges will be FD (good) and RV (bad): +1+1+1(+3)
- (U2 L2 F2 D)
    - After (R2 U2 L2), 1qt edges will be FV (bad) and RV (bad), fr=1: +1+2+0(+5)
    - After (B2 R2 U2 F2), 1qt edges will be FD (good) and RH (good), fr=1: +1+3+0(+3)
- (U2 L2 B2 U')
    - After (L2), 1qt edges will be FV (bad) and RD (good): +1+0+3(+3)
- (F2 U2 F2 D)
    - After (R2 F2 U2 R2), 1qt edges will be FD (good) and RV (bad): +1+3+0(+3)
    - After (F2 U2 R2 F2), 1qt edges will be FH (bad) and RV (bad): +1+3+0(+5)
- (U2 L2 F2 D')
    - After (B2 R2 F2 B2), 1qt edges will be FD (good) and RV (bad): +1+3+0(+3)
- (U2 R2 B2 U)
    - After (R2 U2 F2 R2), 1qt edges will be FH (bad) and RH (good), fr=1: +1+3+0(+5)
- 22 more variants of this skeleton pass the meta, not reached before the stop.

Stop: 2 finishes within goal (12, 13), after 4 HTRs. This DR's optimal is 12.

### 2c3, scramble 4

`R' U' F U' B2 R' D B' R' D' R2 D' F' D' L2 F2 D2 L2 B2 U B2 U B2 R' U' F`

2c3 2e, goal 13.

Skeleton starting with D' has DD corners, L=8, 5 spare moves.

- D'
    - After L2 F2, 1qt edges will be FD (good) and RV (good): +0+1+0(+0)
        - L2 F2 U' R2 U // no good
    - After B2 R2 L2, 1qt edges will be FD (good) and RD (good): +0+2+0(+2)
        - B2 R2 L2 U F2 U' // no good
    - After L2 F2, 1qt edges will be FD (good) and RV (good): +0+1+2(+0)
        - L2 F2 U L2 U2 R2 U // 4 pairs, no good
- 44 more variants of this skeleton pass the meta, not reached before the stop.

Check inverse. Skeleton starting with (R2 U2 F2 U') has HH corners. Apply D' and NISS: FD corners.

- After (L2 U2 F2), 1qt edges will be FH (bad) and RH (good), fr=1: +0+0(+3)
    - (L2 U2 F2 U' L2 U') // no good
- After (B2 U2 F2 R2), 1qt edges will be FH (bad) and RD (good): +1+0(+3)
    - (B2 U2 F2 R2 U R2 U) // 6 pairs, no good
- After (U2 F2 U2 L2), 1qt edges will be FH (bad) and RH (good), fr=1: +1+0(+3)
    - (U2 F2 U2 L2 U L2 U') // 4 pairs, no good
- 68 more variants of this skeleton pass the meta, not reached before the stop.

The same skeleton in full, for the solutions that go on after its last quarter turn.

- (F2 U2 R2 U')
    - After (R2), 1qt edges will be RH (good) and FV (bad): +0+0+0(+3)
        - (R2 U' R2 U') // no good
- (F2 U2 L2 U')
    - After (B2), 1qt edges will be RH (good) and FD (bad): +0+0+1(+3)
        - (B2 U' F2 L2 D) // 2 pairs, no good
        - (B2 U' B2 R2 U') // 2 pairs, no good
- (L2 U2 F2 U')
    - After (L2), 1qt edges will be RH (good) and FH (good), fr=1: +0+0+3(+5)
- (R2 U2 B2 U')
    - After (L2), 1qt edges will be RV (bad) and FD (bad): +0+0+3(+6)
- (R2 U2 B2 U)
    - After (L2 U2 L2), 1qt edges will be RV (bad) and FD (bad): +0+2+1(+6)
- (R2 U2 F2 U)
    - After (R2 B2 U2 L2), 1qt edges will be RV (bad) and FV (bad): +0+3+0(+6)
    - After (F2 R2 L2 U2 F2), 1qt edges will be RH (good) and FD (bad): +0+4+0(+3)
    - After (F2 L2 U2 F2 U2 R2), 1qt edges will be RH (good) and FD (bad): +0+5+0(+3)
- (B2 R2 U2 L2 D)
    - After (B2), 1qt edges will be RD (bad) and FH (good), fr=1: +1+0+0(+5)
    - After (B2), 1qt edges will be RD (bad) and FH (good): +1+0+2(+3)
- (F2 L2 U2 R2 U)
    - After (L2), 1qt edges will be RH (good) and FV (bad), fr=1: +1+0+0(+5)
    - After (L2), 1qt edges will be RH (good) and FV (bad): +1+0+2(+3)
- (L2 U2 R2 F2 U)
    - After (B2), 1qt edges will be RD (bad) and FD (bad), fr=1: +1+0+0(+6)
    - After (F2 L2 F2 R2), 1qt edges will be RD (bad) and FH (good), fr=1: +1+3+0(+5)
- (L2 U2 L2 F2 U)
    - After (B2), 1qt edges will be RH (good) and FD (bad), fr=1: +1+0+1(+5)
    - After (B2), 1qt edges will be RH (good) and FD (bad): +1+0+3(+3)
- (R2 B2 U2 B2 U)
    - After (L2), 1qt edges will be RV (bad) and FD (bad): +1+0+1(+6)
- (F2 R2 U2 R2 U)
    - After (B2 L2), 1qt edges will be RV (bad) and FH (good), fr=1: +1+1+0(+5)
    - After (B2 L2), 1qt edges will be RV (bad) and FH (good): +1+1+2(+3)
- (F2 U2 F2 R2 U)
    - After (L2 F2), 1qt edges will be RV (bad) and FD (bad): +1+1+0(+6)
    - After (B2 R2 B2 L2), 1qt edges will be RD (bad) and FH (good): +1+3+0(+3)
- (R2 U2 L2 B2 D)
    - After (F2 L2), 1qt edges will be RV (bad) and FD (bad), fr=1: +1+1+0(+6)
    - After (R2 F2 B2), 1qt edges will be RV (bad) and FH (good), fr=1: +1+2+0(+5)
- (U2 F2 U2 R2 U)
    - After (L2 F2), 1qt edges will be RV (bad) and FD (bad), fr=1: +1+1+0(+6)
    - After (B2 R2 B2 L2), 1qt edges will be RH (good) and FH (good), fr=1: +1+3+0(+5)
- (F2 U2 B2 R2 U)
    - After (L2 B2), 1qt edges will be RH (good) and FV (bad): +1+1+1(+3)
- (B2 R2 U2 R2 U)
    - After (L2 F2), 1qt edges will be RH (good) and FD (bad), fr=1: +1+1+1(+5)
- (R2 U2 R2 B2 U)
    - After (L2 F2), 1qt edges will be RH (good) and FV (bad), fr=1: +1+1+1(+5)
- (L2 B2 U2 F2 U)
    - After (B2 R2), 1qt edges will be RD (bad) and FD (bad): +1+1+1(+6)
- (B2 R2 U2 L2 D')
    - After (F2 U2 F2), 1qt edges will be RD (bad) and FH (good): +1+2+0(+3)
- (F2 L2 U2 R2 U')
    - After (R2 U2 L2), 1qt edges will be RH (good) and FV (bad): +1+2+0(+3)
- (U2 B2 U2 L2 D')
    - After (L2 U2 R2), 1qt edges will be RV (bad) and FH (good): +1+2+0(+3)
- (B2 U2 B2 L2 D')
    - After (L2 U2 R2), 1qt edges will be RV (bad) and FH (good), fr=1: +1+2+0(+5)
    - After (R2 L2 U2 R2), 1qt edges will be RV (bad) and FH (good): +1+3+0(+3)
- (B2 U2 F2 R2 U')
    - After (L2 U2 R2), 1qt edges will be RH (good) and FH (good), fr=1: +1+2+0(+5)
- (L2 B2 U2 B2 D')
    - After (L2 U2 R2), 1qt edges will be RD (bad) and FH (good), fr=1: +1+2+0(+5)
    - After (R2 L2 U2 R2), 1qt edges will be RD (bad) and FH (good): +1+3+0(+3)
- (L2 F2 U2 B2 D')
    - After (L2 U2 L2), 1qt edges will be RV (bad) and FH (good), fr=1: +1+2+0(+5)
- (R2 F2 U2 F2 U')
    - After (F2 U2 F2), 1qt edges will be RH (good) and FV (bad), fr=1: +1+2+0(+5)
    - After (F2 B2 U2 F2), 1qt edges will be RH (good) and FV (bad): +1+3+0(+3)
- (U2 L2 U2 B2 D')
    - After (F2 U2 B2), 1qt edges will be RD (bad) and FH (good), fr=1: +1+2+0(+5)
    - After (F2 B2 U2 B2), 1qt edges will be RD (bad) and FH (good): +1+3+0(+3)
- (U2 R2 U2 F2 U')
    - After (L2 U2 R2), 1qt edges will be RH (good) and FV (bad), fr=1: +1+2+0(+5)
- (F2 U2 B2 L2 D')
    - After (F2 U2 B2), 1qt edges will be RD (bad) and FV (bad), fr=1: +1+2+0(+6)
    - After (R2 F2 U2 L2), 1qt edges will be RH (good) and FD (bad), fr=1: +1+3+0(+5)
- (L2 U2 L2 B2 D')
    - After (F2 U2 B2), 1qt edges will be RD (bad) and FV (bad): +1+2+0(+6)
    - After (L2 F2 U2 R2), 1qt edges will be RH (good) and FD (bad): +1+3+0(+3)
- (L2 U2 R2 F2 U')
    - After (F2 U2 B2), 1qt edges will be RD (bad) and FD (bad): +1+2+0(+6)
- (F2 U2 F2 L2 U)
    - After (L2), 1qt edges will be RD (bad) and FH (good): +1+0+3(+3)
- (B2 U2 B2 R2 U)
    - After (R2), 1qt edges will be RH (good) and FV (bad), fr=1: +1+0+3(+5)
    - After (L2), 1qt edges will be RV (bad) and FD (bad), fr=1: +1+0+3(+6)
- (R2 U2 L2 F2 U)
    - After (R2), 1qt edges will be RD (bad) and FH (good), fr=1: +1+0+3(+5)
- (U2 F2 U2 L2 U)
    - After (L2), 1qt edges will be RH (good) and FH (good), fr=1: +1+0+3(+5)
- (B2 L2 U2 R2 U)
    - After (B2), 1qt edges will be RD (bad) and FV (bad), fr=1: +1+0+3(+6)
- (R2 F2 U2 B2 U)
    - After (R2), 1qt edges will be RD (bad) and FD (bad), fr=1: +1+0+3(+6)
- (U2 B2 U2 R2 U)
    - After (R2), 1qt edges will be RD (bad) and FV (bad): +1+0+3(+6)
- (F2 L2 U2 L2 U')
    - After (B2 U2 F2), 1qt edges will be RV (bad) and FH (good): +1+2+1(+3)
- (L2 U2 R2 B2 U')
    - After (R2 U2 L2), 1qt edges will be RH (good) and FV (bad): +1+2+1(+3)
- (B2 U2 B2 R2 U')
    - After (L2 U2 R2), 1qt edges will be RH (good) and FV (bad), fr=1: +1+2+1(+5)
- (R2 F2 U2 B2 U')
    - After (R2 U2 L2), 1qt edges will be RV (bad) and FV (bad), fr=1: +1+2+1(+6)
- (U2 B2 U2 R2 U')
    - After (L2 U2 R2), 1qt edges will be RD (bad) and FV (bad): +1+2+1(+6)
- (B2 U2 B2 L2 D)
    - After (R2 U2 R2 L2), 1qt edges will be RV (bad) and FH (good): +1+3+0(+3)
- (F2 U2 B2 L2 D)
    - After (R2 F2 R2 L2), 1qt edges will be RH (good) and FV (bad): +1+3+0(+3)
- (R2 U2 L2 B2 D')
    - After (B2 R2 U2 B2), 1qt edges will be RH (good) and FD (bad): +1+3+0(+3)
- (B2 L2 U2 L2 D)
    - After (L2 F2 R2 L2), 1qt edges will be RH (good) and FD (bad), fr=1: +1+3+0(+5)
- (L2 U2 L2 B2 D)
    - After (B2 L2 F2 L2), 1qt edges will be RD (bad) and FH (good), fr=1: +1+3+0(+5)
- (U2 B2 U2 L2 D)
    - After (R2 F2 L2 F2), 1qt edges will be RH (good) and FH (good), fr=1: +1+3+0(+5)
- (F2 U2 F2 R2 U')
    - After (F2 U2 L2 F2), 1qt edges will be RV (bad) and FD (bad), fr=1: +1+3+0(+6)
- (R2 B2 U2 F2 U')
    - After (L2 F2 U2 R2), 1qt edges will be RD (bad) and FV (bad), fr=1: +1+3+0(+6)
- (U2 F2 U2 R2 U')
    - After (F2 U2 L2 F2), 1qt edges will be RV (bad) and FD (bad): +1+3+0(+6)
- 133 more variants of this skeleton pass the meta, not reached before the stop.

Skeleton starting with U2 R2 D' has FD corners, L=8, 5 spare moves.

- U2 R2 D'
    - After R2 B2, 1qt edges will be FH (bad) and RD (good): +0+1+0(+3)
        - R2 B2 U F2 U' // no good
    - After R2 F2 U2 L2 B2 L2, 1qt edges will be FD (good) and RD (good): +0+5+0(+1)
- U2 L2 U'
    - After B2, 1qt edges will be FV (bad) and RH (good): +0+0+3(+3)
- U2 L2 U
    - After L2 B2 U2 R2, 1qt edges will be FD (good) and RD (good), fr=1: +0+3+1(+4)
    - After F2 R2 F2 U2 R2, 1qt edges will be FH (bad) and RD (good): +0+4+1(+3)
- U2 B2 L2 U
    - After L2, 1qt edges will be FH (bad) and RV (bad): +1+0+1(+5)
    - After L2 F2 B2, 1qt edges will be FV (bad) and RD (good): +1+2+1(+3)
- L2 U2 R2 D
    - After R2 F2, 1qt edges will be FH (bad) and RV (bad), fr=1: +1+1+0(+5)
- R2 U2 L2 U
    - After L2 B2, 1qt edges will be FD (good) and RD (good), fr=1: +1+1+1(+4)
    - After L2 F2, 1qt edges will be FH (bad) and RV (bad), fr=1: +1+1+1(+5)
- L2 U2 L2 U
    - After B2, 1qt edges will be FV (bad) and RH (good), fr=1: +1+0+3(+5)
- U2 F2 R2 U'
    - After B2 U2 B2, 1qt edges will be FV (bad) and RV (bad), fr=1: +1+2+1(+5)
- L2 U2 R2 D'
    - After L2 B2 U2 L2, 1qt edges will be FD (good) and RV (bad): +1+3+0(+3)
- U2 B2 R2 D'
    - After R2 U2 F2 L2, 1qt edges will be FV (bad) and RV (bad), fr=1: +1+3+0(+5)
- U2 F2 L2 U'
    - After L2 U2 B2 R2, 1qt edges will be FH (bad) and RD (good), fr=1: +1+3+0(+5)
- 11 more variants of this skeleton pass the meta, not reached before the stop.

Stop: 10 HTRs done, nothing within goal. This DR's optimal is 12.

### 2c3, scramble 5

`R' U' F R F R' B' L2 F' R2 D' R' U2 F2 U2 L2 D' B2 R2 U2 L2 R' B2 R' U' F`

2c3 6e, goal 13.

Skeleton starting with U has HH corners, L=5, 8 spare moves. Apply (U') and NISS: RD corners.

- With no setup, 1qt edges will be RD (good) and FV (bad), fr=1: +0+4(+3)
    - U R2 U2 F2 R2 F2 U // 4 pairs, no good
    - U R2 U2 F2 L2 B2 D // 2 pairs, no good
    - U R2 U2 B2 L2 F2 D // 2 pairs, no good
- 30 more variants of this skeleton pass the meta, not reached before the stop.

The same skeleton in full, for the solutions that go on after its last quarter turn.

- U
    - After F2 B2 L2, 1qt edges will be RD (bad) and FH (good): +0+2+3(+3)
        - F2 B2 L2 U B2 L2 U2 B2 D' // 4 pairs, no good
    - After F2 B2 R2, 1qt edges will be RH (good) and FD (bad): +0+2+3(+3)
        - F2 B2 R2 U L2 B2 U2 R2 D' // 2 pairs, no good
- U'
    - After R2 U2 R2, 1qt edges will be RD (bad) and FH (good): +0+2+3(+3)
        - R2 U2 R2 U L2 F2 R2 L2 D // 4 pairs, no good
- 17 more variants of this skeleton pass the meta, not reached before the stop.

Check inverse. Skeleton starting with (U') has HH corners. Apply U and NISS: RD corners.

- After (F2 B2), 1qt edges will be RD (good) and FV (bad): +2+3(+3)
    - (F2 B2 U R2 B2 U2 L2 U') // 4 pairs, no good
- After (R2 L2), 1qt edges will be RD (good) and FV (bad): +2+3(+3)
    - (R2 L2 U L2 B2 U2 L2 U) // 2 pairs, no good
- After (F2 B2), 1qt edges will be RD (good) and FV (bad): +2+3(+3)
    - (F2 B2 U L2 F2 U2 R2 D) // 2 pairs, no good
- 1 more variant of this skeleton passes the meta, not reached before the stop.

The same skeleton in full, for the solutions that go on after its last quarter turn.

- (U')
    - After (R2), 1qt edges will be RH (good) and FV (bad), fr=1: +0+0+2(+5)
        - (R2 U' F2 R2 L2 D) // no good
- 32 more variants of this skeleton pass the meta, not reached before the stop.

Stop: 10 HTRs done, nothing within goal. This DR's optimal is 13.

### 2c3, scramble 6

`R' U' F D' F2 L2 B2 D' B2 U2 R2 U2 R2 U' R' B L U L D' R' F' R' U' F`

2c3 6e, goal 13.

Skeleton starting with U has HH corners, L=5, 8 spare moves. Apply (D) and NISS: FD corners.

- After R2 L2, 1qt edges will be FD (good) and RH (good): +2+0(+0)
    - R2 L2 U R2 U R2 U2 R2 B2 D2 R2 F2 D // 13
- After F2 L2 B2, 1qt edges will be FD (good) and RV (bad): +3+0(+3)
    - F2 L2 B2 U' B2 U // no good
- After R2 L2, 1qt edges will be FD (good) and RH (good): +2+2(+0)
    - R2 L2 U F2 B2 L2 D // no good
- 13 more variants of this skeleton pass the meta, not reached before the stop.

The same skeleton in full, for the solutions that go on after its last quarter turn.

- U
    - After F2, 1qt edges will be RD (bad) and FH (good): +0+0+3(+3)
        - F2 U' B2 R2 F2 R2 D' // 6 pairs, no good
        - F2 U' B2 R2 B2 L2 U' // 6 pairs, no good
        - F2 U' B2 L2 F2 L2 D' // 6 pairs, no good
- 21 more variants of this skeleton pass the meta, not reached before the stop.

Check inverse. Skeleton starting with (D) has HH corners. Apply U and NISS: FD corners.

- After (U2 R2 F2 R2), 1qt edges will be FV (bad) and RD (good): +4+1(+3)
    - (U2 R2 F2 R2 U R2 F2 D') // 4 pairs, no good
    - (U2 R2 F2 R2 U L2 B2 U') // 2 pairs, no good
- After (U2 R2 F2 L2), 1qt edges will be FH (bad) and RV (bad): +4+1(+5)

The same skeleton in full, for the solutions that go on after its last quarter turn.

- (D)
    - After (R2 F2), 1qt edges will be RV (bad) and FH (good): +0+1+2(+3)
        - (R2 F2 U' B2 R2 L2 D' F2 L2 F2 U2) // 12
    - After (L2 U2 F2 U2 B2), 1qt edges will be RV (bad) and FH (good), fr=1: +0+4+0(+5)
    - After (R2 B2 L2 B2 R2), 1qt edges will be RV (bad) and FV (bad): +0+4+0(+6)
    - After (R2 F2), 1qt edges will be RV (bad) and FH (good), fr=1: +0+1+4(+5)
- 45 more variants of this skeleton pass the meta, not reached before the stop.

Stop: 2 finishes within goal (12, 13), after 9 HTRs. This DR's optimal is 12.

### 2c3, scramble 7

`R' U' F U' L2 B2 L D R B' R2 D' L B' R2 U2 F' B R2 F' D2 L2 D2 R' U' F`

2c3 2e, goal 13.

Skeleton starting with L2 U has DD corners, L=9, 4 spare moves.

- R2 U
    - After B2 L2, 1qt edges will be FH (bad) and RV (good): +0+1+0(+3)
        - B2 L2 U L2 U' // no good
    - After R2 F2 B2, 1qt edges will be FV (good) and RV (good): +0+2+0(+1)
        - R2 F2 B2 U' F2 U // no good
    - After R2 F2 B2, 1qt edges will be FV (good) and RV (good): +0+2+2(+1)
- R2 U'
    - After R2 U2 B2 L2, 1qt edges will be FH (bad) and RV (good): +0+3+0(+3)
    - After L2 F2 B2 U2 R2, 1qt edges will be FV (good) and RV (good): +0+4+0(+1)
- B2 L2 D'
    - After F2, 1qt edges will be FV (good) and RD (good): +1+0+0(+0)
        - F2 U L2 U // no good
- F2 R2 U'
    - After L2 B2, 1qt edges will be FD (good) and RH (bad): +1+1+0(+3)
    - After F2 R2 L2, 1qt edges will be FD (good) and RD (good): +1+2+0(+2)
- 17 more variants of this skeleton pass the meta, not reached before the stop.

Check inverse. Skeleton starting with (F2 U2 R2 D) has RD corners.

- (F2 U2 R2 D)
    - After (F2), 1qt edges will be RV (bad) and FH (good): +0+0+0(+3)
        - (F2 U' R2 U) // no good
- (B2 U2 R2 U)
    - After (B2), 1qt edges will be RH (bad) and FH (good): +0+0+1(+3)
        - (B2 U' R2 B2 U') // 6 pairs, no good
        - (B2 U' L2 F2 D') // 6 pairs, no good
    - After (B2 U2 F2 B2), 1qt edges will be RD (good) and FD (good): +0+3+1(+1)
- (L2 U2 B2 U)
    - After (B2), 1qt edges will be RH (bad) and FV (bad), fr=1: +0+0+1(+5)
- (L2 U2 F2 D)
    - After (R2 F2), 1qt edges will be RV (bad) and FV (bad), fr=1: +0+1+0(+5)
    - After (B2 L2 B2 R2), 1qt edges will be RD (good) and FH (good), fr=1: +0+3+0(+3)
- (R2 U2 B2 U)
    - After (F2 L2), 1qt edges will be RV (bad) and FV (bad), fr=1: +0+1+0(+5)
    - After (R2 F2 B2), 1qt edges will be RV (bad) and FH (good): +0+2+2(+3)
- (R2 U2 F2 U)
    - After (L2 F2), 1qt edges will be RV (bad) and FV (bad), fr=1: +0+1+1(+5)
    - After (L2 B2), 1qt edges will be RH (bad) and FD (good): +0+1+3(+3)
- (L2 U2 F2 D')
    - After (L2 B2 U2 L2), 1qt edges will be RV (bad) and FD (good): +0+3+0(+3)
    - After (F2 U2 L2 B2), 1qt edges will be RV (bad) and FV (bad): +0+3+0(+5)
    - After (L2 U2 L2 U2 B2), 1qt edges will be RV (bad) and FD (good): +0+4+0(+3)
- (R2 U2 B2 U')
    - After (R2 U2 F2 L2), 1qt edges will be RV (bad) and FV (bad): +0+3+0(+5)
    - After (L2 F2 B2 U2 R2), 1qt edges will be RV (bad) and FH (good): +0+4+0(+3)
- (B2 U2 R2 U')
    - After (F2 B2 U2 F2), 1qt edges will be RD (good) and FD (good): +0+3+1(+1)
    - After (L2 F2 U2 L2), 1qt edges will be RD (good) and FD (good), fr=1: +0+3+1(+4)
- (L2 U2 B2 U')
    - After (R2 B2 U2 L2), 1qt edges will be RV (bad) and FD (good): +0+3+1(+3)
- (F2 R2 U2 R2 D')
    - After (B2), 1qt edges will be RV (bad) and FD (good), fr=1: +1+0+0(+5)
    - After (B2), 1qt edges will be RV (bad) and FD (good): +1+0+2(+3)
- (R2 U2 R2 F2 D')
    - After (B2), 1qt edges will be RV (bad) and FV (bad), fr=1: +1+0+0(+5)
- (U2 R2 U2 B2 U')
    - After (B2), 1qt edges will be RH (bad) and FH (good): +1+0+1(+3)
- (B2 L2 U2 R2 U')
    - After (F2), 1qt edges will be RH (bad) and FD (good), fr=1: +1+0+1(+5)
- (F2 U2 B2 R2 U')
    - After (F2), 1qt edges will be RH (bad) and FV (bad): +1+0+1(+5)
    - After (R2 B2), 1qt edges will be RD (good) and FV (bad): +1+1+1(+3)
- (L2 B2 U2 B2 U')
    - After (B2), 1qt edges will be RV (bad) and FV (bad): +1+0+1(+5)
- (R2 U2 R2 B2 U')
    - After (B2), 1qt edges will be RH (bad) and FV (bad), fr=1: +1+0+1(+5)
- (U2 B2 U2 L2 U')
    - After (B2), 1qt edges will be RH (bad) and FV (bad), fr=1: +1+0+1(+5)
- (B2 U2 F2 R2 D')
    - After (R2 F2), 1qt edges will be RD (good) and FV (bad): +1+1+0(+3)
- (F2 U2 F2 R2 D')
    - After (B2 R2), 1qt edges will be RH (bad) and FD (good): +1+1+0(+3)
- (R2 B2 U2 B2 U')
    - After (F2 R2), 1qt edges will be RV (bad) and FD (good): +1+1+0(+3)
- (B2 L2 U2 L2 U')
    - After (B2 R2), 1qt edges will be RH (bad) and FH (good), fr=1: +1+1+0(+5)
- (L2 F2 U2 F2 D')
    - After (L2 B2), 1qt edges will be RH (bad) and FV (bad): +1+1+0(+5)
- (L2 U2 R2 F2 D')
    - After (F2 R2), 1qt edges will be RH (bad) and FD (good), fr=1: +1+1+0(+5)
- (R2 F2 U2 B2 U')
    - After (B2 R2), 1qt edges will be RH (bad) and FV (bad): +1+1+0(+5)
    - After (L2 F2 B2), 1qt edges will be RH (bad) and FH (good): +1+2+0(+3)
- (U2 B2 U2 R2 U')
    - After (F2 L2), 1qt edges will be RV (bad) and FV (bad), fr=1: +1+1+0(+5)
- (U2 F2 U2 L2 D')
    - After (L2 B2), 1qt edges will be RV (bad) and FV (bad), fr=1: +1+1+0(+5)
- (B2 U2 F2 L2 U')
    - After (R2 B2), 1qt edges will be RD (good) and FV (bad): +1+1+1(+3)
- (R2 B2 U2 F2 U')
    - After (R2 F2), 1qt edges will be RV (bad) and FD (good): +1+1+1(+3)
- (F2 L2 U2 L2 U')
    - After (R2 F2), 1qt edges will be RD (good) and FD (good), fr=1: +1+1+1(+4)
    - After (R2 B2), 1qt edges will be RH (bad) and FH (good), fr=1: +1+1+1(+5)
- (L2 U2 L2 F2 U')
    - After (R2 B2), 1qt edges will be RH (bad) and FD (good), fr=1: +1+1+1(+5)
- (U2 F2 U2 R2 U')
    - After (L2 B2), 1qt edges will be RH (bad) and FD (good), fr=1: +1+1+1(+5)
- (B2 R2 U2 L2 U)
    - After (L2 U2 L2), 1qt edges will be RD (good) and FV (bad): +1+2+0(+3)
- (F2 L2 U2 R2 D)
    - After (F2 U2 B2), 1qt edges will be RV (bad) and FH (good): +1+2+0(+3)
- (F2 R2 U2 R2 D)
    - After (F2 U2 F2), 1qt edges will be RV (bad) and FD (good): +1+2+0(+3)
- (R2 U2 L2 B2 U)
    - After (F2 U2 F2), 1qt edges will be RV (bad) and FD (good): +1+2+0(+3)
- (L2 B2 U2 F2 D)
    - After (F2 U2 B2), 1qt edges will be RD (good) and FD (good), fr=1: +1+2+0(+4)
- (B2 U2 B2 L2 U)
    - After (F2 U2 F2), 1qt edges will be RV (bad) and FD (good), fr=1: +1+2+0(+5)
- (R2 U2 R2 F2 D)
    - After (F2 U2 F2), 1qt edges will be RV (bad) and FV (bad): +1+2+0(+5)
- (U2 L2 U2 B2 U)
    - After (R2 U2 R2), 1qt edges will be RD (good) and FV (bad), fr=1: +1+2+0(+5)
- (U2 R2 U2 F2 D)
    - After (F2 U2 F2), 1qt edges will be RV (bad) and FH (good), fr=1: +1+2+0(+5)
- 25 more variants of this skeleton pass the meta, not reached before the stop.

Skeleton starting with U2 R2 U' has RV corners, L=9, 4 spare moves.

- U2 R2 U'
    - After L2, 1qt edges will be RV (good) and FV (good), fr=1: +0+0+3(+2)
- U2 L2 U
    - After F2 U2 F2, 1qt edges will be RV (good) and FH (good): +0+2+0(+0)
        - F2 U2 F2 U' F2 U' // no good
- U2 R2 U
    - After B2 R2 U2 B2, 1qt edges will be RD (bad) and FH (good): +0+3+1(+3)
- L2 U2 L2 U
    - After F2, 1qt edges will be RV (good) and FH (good): +1+0+0(+0)
        - F2 U F2 U' // no good
- U2 F2 R2 D
    - After L2, 1qt edges will be RH (bad) and FD (bad), fr=1: +1+0+0(+5)
- U2 B2 R2 U
    - After B2, 1qt edges will be RH (bad) and FV (good), fr=1: +1+0+1(+2)
        - B2 U' R2 B2 U' // 6 pairs, no good
- R2 U2 R2 U
    - After B2 R2, 1qt edges will be RD (bad) and FH (good): +1+1+1(+3)
- R2 U2 L2 U'
    - After B2 U2 B2, 1qt edges will be RV (good) and FD (bad), fr=1: +1+2+0(+2)
- U2 B2 L2 U'
    - After R2 U2 R2, 1qt edges will be RD (bad) and FD (bad): +1+2+0(+5)
- U2 F2 R2 D'
    - After R2 U2 R2, 1qt edges will be RH (bad) and FD (bad): +1+2+0(+5)
- 8 more variants of this skeleton pass the meta, not reached before the stop.

Check inverse. Skeleton starting with (U2 R2 D') has RV corners.

- (U2 R2 D')
    - After (L2), 1qt edges will be RH (bad) and FD (bad), fr=1: +0+0+0(+5)
    - After (F2 L2 B2 R2 B2), 1qt edges will be RV (good) and FV (good), fr=1: +0+4+0(+2)
- (U2 L2 U')
    - After (R2), 1qt edges will be RD (bad) and FH (good), fr=1: +0+0+4(+2)
- (U2 R2 D)
    - After (R2 U2 R2), 1qt edges will be RH (bad) and FD (bad): +0+2+0(+5)
    - After (F2 R2 F2 U2 B2), 1qt edges will be RD (bad) and FV (good), fr=1: +0+4+0(+2)
- (U2 L2 U)
    - After (R2 U2 L2), 1qt edges will be RH (bad) and FV (good): +0+2+1(+3)
- (R2 U2 R2 D)
    - After (R2), 1qt edges will be RH (bad) and FD (bad): +1+0+0(+5)
- (R2 U2 L2 U)
    - After (R2), 1qt edges will be RH (bad) and FV (good): +1+0+1(+3)
- (L2 U2 R2 D)
    - After (F2 R2), 1qt edges will be RD (bad) and FV (good): +1+1+0(+3)
- (U2 F2 R2 D)
    - After (R2 B2), 1qt edges will be RD (bad) and FD (bad), fr=1: +1+1+0(+5)
- (U2 F2 L2 U)
    - After (R2 B2), 1qt edges will be RH (bad) and FV (good), fr=1: +1+1+1(+2)
- (U2 B2 L2 U')
    - After (B2 U2 B2), 1qt edges will be RV (good) and FV (good): +1+2+0(+1)
        - (B2 U2 B2 U B2 U) // no good
- (R2 U2 R2 D')
    - After (L2 U2 L2), 1qt edges will be RH (bad) and FD (bad), fr=1: +1+2+0(+5)

Stop: 10 HTRs done, nothing within goal. This DR's optimal is 14, over the goal.

### 2c3, scramble 8

`R' U' F D F2 L' B2 R2 U2 R' D2 R' F2 U2 R F' R' B2 R' U' R D' R' U' F`

2c3 6e, goal 13.

Skeleton starting with U has FD corners, L=6, 7 spare moves.

- U
    - After F2, 1qt edges will be FH (bad) and RV (bad), fr=1: +0+0+3(+5)
- U'
    - After F2 R2 F2 U2 L2, 1qt edges will be FD (good) and RH (good), fr=1: +0+4+1(+3)

Check inverse. Skeleton starting with (F2 U) has HH corners. Apply U and NISS: FD corners.

- After (L2 F2), 1qt edges will be FV (bad) and RD (good), fr=1: +1+1(+3)
    - (L2 F2 U' R2 B2 U) // 4 pairs, no good
    - (L2 F2 U' L2 F2 D' R2 F2 B2 D2 B2 R2 U) // 2 pairs, 13
- After (B2), 1qt edges will be FH (bad) and RD (good), fr=1: +0+3(+3)
    - (B2 U L2 F2 R2 L2 U') // 6 pairs, no good
- 17 more variants of this skeleton pass the meta, not reached before the stop.

The same skeleton in full, for the solutions that go on after its last quarter turn.

- (F2 U)
    - After (L2), 1qt edges will be RV (bad) and FD (bad), fr=1: +0+0+3(+6)
- (F2 U')
    - After (L2 F2 L2 U2 F2), 1qt edges will be RH (good) and FH (good), fr=1: +0+4+1(+5)
- (B2 U')
    - After (B2 U2 R2 F2), 1qt edges will be RH (good) and FH (good): +0+3+0(+0)
        - (B2 U2 R2 F2 U L2 U) // no good
    - After (R2 B2 U2 B2 L2), 1qt edges will be RH (good) and FH (good): +0+4+0(+0)
        - (R2 B2 U2 B2 L2 U' F2 U) // 6 pairs, no good
    - After (L2 F2 U2 B2 L2), 1qt edges will be RH (good) and FH (good): +0+4+0(+0)
        - (L2 F2 U2 B2 L2 U' B2 U) // 6 pairs, no good
- (L2 B2 U')
    - After (L2), 1qt edges will be RD (bad) and FV (bad), fr=1: +1+0+2(+6)
    - After (R2 U2 B2 L2 B2), 1qt edges will be RH (good) and FV (bad), fr=1: +1+4+0(+5)
- (L2 F2 U')
    - After (R2 F2), 1qt edges will be RD (bad) and FD (bad), fr=1: +1+1+1(+6)
    - After (B2), 1qt edges will be RD (bad) and FH (good): +1+0+4(+3)
- (R2 F2 D')
    - After (F2 B2 R2), 1qt edges will be RH (good) and FV (bad), fr=1: +1+2+0(+5)
    - After (F2 B2 R2), 1qt edges will be RH (good) and FV (bad): +1+2+2(+3)
- (R2 F2 D)
    - After (L2 U2 F2 B2 L2), 1qt edges will be RH (good) and FV (bad): +1+4+0(+3)
- (L2 B2 U)
    - After (R2 U2 F2 B2 R2), 1qt edges will be RD (bad) and FV (bad): +1+4+0(+6)
- (L2 F2 U)
    - After (R2 F2 U2 R2), 1qt edges will be RD (bad) and FH (good): +1+3+1(+3)
- 18 more variants of this skeleton pass the meta, not reached before the stop.

Skeleton starting with R2 U' has HH corners, L=6, 7 spare moves. Apply (U') and NISS: RD corners.

- After F2 B2 L2, 1qt edges will be RD (good) and FV (bad): +2+3(+3)

The same skeleton in full, for the solutions that go on after its last quarter turn.

- R2 U'
    - After R2 B2, 1qt edges will be RH (good) and FD (bad), fr=1: +0+1+3(+5)
    - After R2 B2, 1qt edges will be RH (good) and FD (bad): +0+1+4(+3)
- L2 U
    - After L2 U2 F2 L2, 1qt edges will be RH (good) and FD (bad): +0+3+0(+3)
        - L2 U2 F2 L2 U' R2 U' // no good
    - After F2 R2 U2 R2 B2, 1qt edges will be RH (good) and FD (bad): +0+4+0(+3)
        - F2 R2 U2 R2 B2 U B2 U // 5 pairs, no good
    - After B2 L2 U2 R2 B2, 1qt edges will be RH (good) and FD (bad): +0+4+0(+3)
        - B2 L2 U2 R2 B2 U F2 U // 5 pairs, no good
- R2 U
    - After R2 B2 U2 F2 L2, 1qt edges will be RH (good) and FD (bad): +0+4+1(+3)
- B2 R2 D
    - After F2, 1qt edges will be RH (good) and FD (bad), fr=1: +1+0+2(+5)
    - After F2, 1qt edges will be RH (good) and FD (bad): +1+0+4(+3)
- B2 L2 U
    - After R2 F2, 1qt edges will be RV (bad) and FD (bad), fr=1: +1+1+1(+6)
    - After R2 L2 B2, 1qt edges will be RV (bad) and FH (good), fr=1: +1+2+1(+5)
- B2 R2 D'
    - After F2 U2 B2, 1qt edges will be RH (good) and FD (bad): +1+2+2(+3)
- B2 L2 U'
    - After R2 F2 U2 R2, 1qt edges will be RV (bad) and FH (good): +1+3+1(+3)
    - After L2 B2 U2 R2, 1qt edges will be RD (bad) and FD (bad): +1+3+1(+6)
- 9 more variants of this skeleton pass the meta, not reached before the stop.

Check inverse. Skeleton starting with (U') has RD corners.

- (U')
    - After (F2 R2), 1qt edges will be RD (good) and FV (bad), fr=1: +0+1+3(+5)
    - After (F2 L2), 1qt edges will be RV (bad) and FH (good): +0+1+4(+3)
- (U)
    - After (F2 R2 U2 L2 B2), 1qt edges will be RD (good) and FV (bad): +0+4+1(+3)

Skeleton starting with B2 D' has RD corners, L=7, 6 spare moves.

- B2 D'
    - After R2, 1qt edges will be RD (good) and FH (good), fr=1: +0+0+2(+3)
        - R2 U' L2 F2 B2 D // no good
- L2 F2 U
    - After R2 L2 B2, 1qt edges will be RH (bad) and FH (good), fr=1: +1+2+0(+5)
    - After R2 L2 B2, 1qt edges will be RH (bad) and FH (good): +1+2+2(+3)
- R2 F2 U
    - After F2, 1qt edges will be RH (bad) and FV (bad), fr=1: +1+0+3(+5)
- R2 B2 D
    - After B2 U2 R2 L2, 1qt edges will be RH (bad) and FD (good), fr=1: +1+3+0(+5)
    - After L2 U2 F2 U2 F2, 1qt edges will be RV (bad) and FD (good): +1+4+0(+3)
- R2 B2 D'
    - After B2 U2 R2 B2, 1qt edges will be RV (bad) and FD (good): +1+3+0(+3)
    - After R2 L2 U2 F2, 1qt edges will be RH (bad) and FD (good), fr=1: +1+3+0(+5)
    - After L2 B2 U2 F2 L2, 1qt edges will be RV (bad) and FD (good): +1+4+0(+3)
- L2 B2 U
    - After F2 L2, 1qt edges will be RD (good) and FH (good), fr=1: +1+1+3(+3)
    - After R2 L2 F2 L2, 1qt edges will be RV (bad) and FD (good), fr=1: +1+3+1(+5)
- L2 F2 U'
    - After B2 U2 F2, 1qt edges will be RH (bad) and FH (good): +1+2+2(+3)
    - After F2 R2 F2 U2 R2, 1qt edges will be RD (good) and FV (bad), fr=1: +1+4+0(+5)
- 49 more variants of this skeleton pass the meta, not reached before the stop.

Stop: 10 HTRs done, one finish within goal (13). This DR's optimal is 13.

### 2c3, scramble 9

`R' U' F R2 D2 B U F U2 F D' B2 D2 B2 L' U2 L' D2 L F' R D R' U' F`

2c3 6e, goal 13.

Skeleton starting with U' has RD corners, L=6, 7 spare moves.

- U'
    - After R2 B2, 1qt edges will be RD (good) and FH (good): +0+1+2(+0)
        - R2 B2 U' R2 F2 B2 D' // no good
    - After F2 B2 R2 F2, 1qt edges will be RD (good) and FH (good): +0+3+0(+0)
        - F2 B2 R2 F2 U' L2 U' // no good
- U
    - After F2 U2 L2 F2, 1qt edges will be RD (good) and FH (good), fr=1: +0+3+0(+3)
        - F2 U2 L2 F2 U B2 U // no good
- 36 more variants of this skeleton pass the meta, not reached before the stop.

Check inverse. Skeleton starting with (R2 D') has HH corners. Apply U' and NISS: FD corners.

- After (R2 F2 B2), 1qt edges will be FD (good) and RD (good): +2+0(+1)
    - (R2 F2 B2 U' R2 U') // no good
- After (B2 L2), 1qt edges will be FV (bad) and RD (good): +1+2(+3)
    - (B2 L2 U B2 R2 L2 D) // no good
- After (L2 F2 L2 F2), 1qt edges will be FD (good) and RH (good): +3+0(+0)
    - (L2 F2 L2 F2 U F2 U) // no good
- 24 more variants of this skeleton pass the meta, not reached before the stop.

The same skeleton in full, for the solutions that go on after its last quarter turn.

- (L2 U')
    - After (B2 L2), 1qt edges will be RH (good) and FH (good): +0+1+3(+0)
        - (B2 L2 U F2 L2 F2 B2 D' F2 B2 U2) // 8 pairs, 13
    - After (B2 R2), 1qt edges will be RD (bad) and FV (bad): +0+1+3(+6)
    - After (F2 R2 B2 L2 B2), 1qt edges will be RD (bad) and FH (good): +0+4+1(+3)
- (R2 D)
    - After (L2 U2 F2 R2), 1qt edges will be RD (bad) and FV (bad), fr=1: +0+3+0(+6)
    - After (B2 U2 F2 R2 U2 L2), 1qt edges will be RH (good) and FV (bad): +0+5+0(+3)
- (F2 R2 U)
    - After (B2 R2), 1qt edges will be RH (good) and FH (good): +1+1+1(+0)
        - (B2 R2 U' R2 F2 D') // 4 pairs, no good
        - (B2 R2 U' L2 B2 U') // 4 pairs, no good
- (F2 L2 U)
    - After (R2 F2), 1qt edges will be RV (bad) and FV (bad): +1+1+2(+6)
    - After (B2 U2 L2 F2 R2), 1qt edges will be RD (bad) and FH (good): +1+4+0(+3)
- (F2 L2 U')
    - After (R2 L2 U2 F2), 1qt edges will be RD (bad) and FV (bad): +1+3+0(+6)
- (F2 R2 U')
    - After (F2 B2 U2 R2), 1qt edges will be RH (good) and FV (bad): +1+3+1(+3)
    - After (F2 L2 U2 B2), 1qt edges will be RH (good) and FV (bad), fr=1: +1+3+1(+5)
- 26 more variants of this skeleton pass the meta, not reached before the stop.

Skeleton starting with U2 R2 U' has HH corners, L=7, 6 spare moves. Apply (D) and NISS: RD corners.

- After U2 F2 B2 L2, 1qt edges will be RH (bad) and FH (good): +2+0(+3)
    - U2 F2 B2 L2 U' L2 U' // no good
- After L2 F2 U2 L2 U2 L2 F2, 1qt edges will be RD (good) and FH (good), fr=1: +5+0(+2)
- 12 more variants of this skeleton pass the meta, not reached before the stop.

Stop: 10 HTRs done, one finish within goal (13). This DR's optimal is 13.

### 2c3, scramble 10

`R' U' F U L D2 B2 L B2 L' D2 R2 B2 L' B2 D2 B' R2 D B' R B' D R' U' F`

2c3 4e, goal 13.

Skeleton starting with U2 B2 U has RD corners, L=8, 5 spare moves.

- U2 B2 U
    - After B2, 1qt edges will be RV (bad) and FH (good): +0+0+0(+3)
        - B2 U' R2 U // no good
    - After B2, 1qt edges will be RV (bad) and FH (good): +0+0+2(+3)
        - B2 U' F2 B2 L2 D' // no good
- U2 F2 D
    - After B2, 1qt edges will be RV (bad) and FV (bad): +0+0+0(+5)
        - B2 U' F2 U' // no good
    - After R2 B2 U2 F2 L2 F2, 1qt edges will be RD (good) and FV (bad): +0+5+0(+3)
- U2 F2 D'
    - After B2 U2 F2, 1qt edges will be RV (bad) and FV (bad), fr=1: +0+2+0(+5)
    - After B2 L2 U2 L2 U2 B2, 1qt edges will be RH (bad) and FD (good): +0+5+0(+3)
- F2 U2 B2 U
    - After B2 U2 F2, 1qt edges will be RV (bad) and FH (good): +1+2+0(+3)
- B2 U2 B2 U'
    - After B2 R2 L2, 1qt edges will be RV (bad) and FV (bad), fr=1: +1+2+0(+5)
- B2 U2 F2 D'
    - After B2 R2 L2, 1qt edges will be RV (bad) and FH (good), fr=1: +1+2+0(+5)
- F2 U2 F2 D
    - After B2 U2 B2, 1qt edges will be RV (bad) and FV (bad): +1+2+0(+5)
- U2 R2 B2 U'
    - After L2, 1qt edges will be RH (bad) and FD (good): +1+0+3(+3)
- B2 U2 B2 U
    - After B2 U2 R2 B2, 1qt edges will be RD (good) and FV (bad): +1+3+0(+3)
- B2 U2 F2 D
    - After B2 U2 R2 F2, 1qt edges will be RH (bad) and FH (good): +1+3+0(+3)
- F2 U2 B2 U'
    - After B2 U2 F2 B2, 1qt edges will be RV (bad) and FH (good), fr=1: +1+3+0(+5)
- F2 U2 F2 D'
    - After B2 L2 B2 L2, 1qt edges will be RV (bad) and FD (good), fr=1: +1+3+0(+5)
- 35 more variants of this skeleton pass the meta, not reached before the stop.

Check inverse. Skeleton starting with (R2 U') has FV corners.

- (R2 U')
    - After (B2 L2), 1qt edges will be FD (bad) and RH (good): +0+1+3(+3)
- (F2 R2 D)
    - After (B2 L2), 1qt edges will be FH (bad) and RD (bad): +1+1+0(+5)
    - After (L2 B2 L2 B2), 1qt edges will be FV (good) and RV (good): +1+3+0(+1)
        - (L2 B2 L2 B2 U F2 U') // 2 pairs, no good
- (B2 L2 U)
    - After (F2 B2 R2), 1qt edges will be FV (good) and RH (good): +1+2+0(+0)
        - (F2 B2 R2 U' B2 U) // no good
- (F2 L2 D')
    - After (F2 U2 F2), 1qt edges will be FD (bad) and RV (good), fr=1: +1+2+0(+2)
        - (F2 U2 F2 U B2 U) // no good
- (F2 R2 D')
    - After (B2 L2 U2 F2), 1qt edges will be FH (bad) and RH (good), fr=1: +1+3+0(+2)
    - After (R2 U2 F2 R2), 1qt edges will be FH (bad) and RD (bad), fr=1: +1+3+0(+5)
- (B2 L2 U')
    - After (F2 R2 U2 B2), 1qt edges will be FD (bad) and RD (bad), fr=1: +1+3+0(+5)
- (B2 R2 U')
    - After (B2 U2 R2 B2), 1qt edges will be FH (bad) and RD (bad), fr=1: +1+3+0(+5)
- 7 more variants of this skeleton pass the meta, not reached before the stop.

Skeleton starting with B2 U' has DD corners, L=9, 4 spare moves.

- B2 U'
    - After R2 B2 R2 B2, 1qt edges will be FD (good) and RV (good): +0+3+1(+0)
        - R2 B2 R2 B2 U' R2 B2 U' // 4 pairs, no good
        - R2 B2 R2 B2 U' L2 F2 D // 4 pairs, no good
    - After L2 B2 L2 B2, 1qt edges will be FD (good) and RV (good): +0+3+1(+0)
        - L2 B2 L2 B2 U' F2 L2 D // 4 pairs, no good
- B2 U
    - After R2 L2 U2 R2, 1qt edges will be FV (good) and RV (good): +0+3+1(+1)
- 5 more variants of this skeleton pass the meta, not reached before the stop.

Check inverse. Skeleton starting with (B2 U2 R2 U') has FD corners.

- (B2 U2 R2 U')
    - After (B2), 1qt edges will be FD (good) and RV (bad): +0+0+3(+3)
    - After (L2 B2), 1qt edges will be FD (good) and RD (good): +0+1+3(+1)
- (F2 U2 L2 D')
    - After (R2), 1qt edges will be FV (bad) and RD (good): +0+0+3(+3)
    - After (B2 L2), 1qt edges will be FD (good) and RD (good): +0+1+3(+1)
- (L2 U2 B2 U')
    - After (F2), 1qt edges will be FD (good) and RV (bad): +0+0+3(+3)
    - After (L2 F2), 1qt edges will be FD (good) and RD (good): +0+1+3(+1)
- (R2 U2 F2 U')
    - After (F2), 1qt edges will be FD (good) and RV (bad): +0+0+3(+3)
    - After (L2 F2), 1qt edges will be FD (good) and RD (good): +0+1+3(+1)
- (L2 U2 F2 U')
    - After (R2), 1qt edges will be FH (bad) and RV (bad): +0+0+3(+5)
    - After (B2 R2), 1qt edges will be FH (bad) and RH (good): +0+1+3(+3)
- (R2 U2 B2 U')
    - After (R2), 1qt edges will be FH (bad) and RV (bad): +0+0+3(+5)
    - After (B2 R2), 1qt edges will be FH (bad) and RH (good): +0+1+3(+3)
- (B2 U2 L2 U')
    - After (B2 R2), 1qt edges will be FD (good) and RD (good), fr=1: +0+1+3(+4)
- (F2 U2 R2 U')
    - After (B2 R2), 1qt edges will be FD (good) and RD (good), fr=1: +0+1+3(+4)
- (L2 U2 B2 U)
    - After (F2 U2 B2), 1qt edges will be FV (bad) and RD (good): +0+2+1(+3)
    - After (B2 U2 R2 B2), 1qt edges will be FD (good) and RD (good): +0+3+1(+1)
- (L2 U2 F2 U)
    - After (L2 U2 L2), 1qt edges will be FV (bad) and RH (good): +0+2+1(+3)
    - After (R2 U2 R2), 1qt edges will be FH (bad) and RV (bad): +0+2+1(+5)
    - After (R2 U2 F2 L2), 1qt edges will be FH (bad) and RH (good): +0+3+1(+3)
- (R2 U2 B2 U)
    - After (L2 U2 L2), 1qt edges will be FV (bad) and RH (good): +0+2+1(+3)
- (R2 U2 F2 U)
    - After (B2 U2 F2), 1qt edges will be FD (good) and RV (bad): +0+2+1(+3)
    - After (B2 U2 R2 B2), 1qt edges will be FD (good) and RD (good): +0+3+1(+1)
- (B2 U2 L2 U)
    - After (L2 U2 F2 L2), 1qt edges will be FD (good) and RD (good), fr=1: +0+3+1(+4)
- (F2 U2 R2 U)
    - After (R2 U2 B2 R2), 1qt edges will be FD (good) and RD (good), fr=1: +0+3+1(+4)
- (B2 U2 F2 R2 U)
    - After (R2), 1qt edges will be FV (bad) and RH (good): +1+0+0(+3)
        - (R2 U' F2 U') // 6 pairs, no good
- (L2 U2 L2 F2 D)
    - After (L2), 1qt edges will be FV (bad) and RD (good), fr=1: +1+0+0(+5)
    - After (L2), 1qt edges will be FV (bad) and RD (good): +1+0+2(+3)
- (R2 U2 R2 F2 U)
    - After (R2), 1qt edges will be FV (bad) and RH (good), fr=1: +1+0+0(+5)
    - After (R2), 1qt edges will be FV (bad) and RH (good): +1+0+2(+3)
- (L2 F2 U2 B2 U)
    - After (F2), 1qt edges will be FV (bad) and RD (good): +1+0+1(+3)
- (L2 F2 U2 F2 U)
    - After (L2), 1qt edges will be FV (bad) and RH (good): +1+0+1(+3)
- (R2 B2 U2 B2 U)
    - After (L2), 1qt edges will be FV (bad) and RH (good): +1+0+1(+3)
    - After (R2), 1qt edges will be FH (bad) and RV (bad): +1+0+1(+5)
- (R2 B2 U2 F2 U)
    - After (F2), 1qt edges will be FV (bad) and RD (good): +1+0+1(+3)
- (F2 U2 B2 L2 D)
    - After (L2 B2), 1qt edges will be FH (bad) and RH (good): +1+1+0(+3)
- (F2 U2 F2 L2 D)
    - After (R2 F2), 1qt edges will be FH (bad) and RH (good): +1+1+0(+3)
- (R2 U2 R2 B2 U)
    - After (L2 B2), 1qt edges will be FD (good) and RD (good), fr=1: +1+1+0(+4)
- (L2 U2 L2 B2 D)
    - After (R2 B2), 1qt edges will be FH (bad) and RH (good), fr=1: +1+1+0(+5)
- (L2 U2 R2 F2 U)
    - After (F2), 1qt edges will be FD (good) and RV (bad), fr=1: +1+0+2(+5)
- (R2 U2 L2 F2 D)
    - After (F2), 1qt edges will be FH (bad) and RV (bad), fr=1: +1+0+2(+5)
- (L2 U2 L2 F2 D')
    - After (L2 U2 R2), 1qt edges will be FV (bad) and RD (good): +1+2+0(+3)
- (R2 U2 R2 F2 U')
    - After (R2 U2 R2), 1qt edges will be FV (bad) and RH (good): +1+2+0(+3)
- (B2 U2 B2 L2 D')
    - After (L2 U2 R2), 1qt edges will be FV (bad) and RD (good), fr=1: +1+2+0(+5)
- (B2 U2 B2 R2 U')
    - After (L2 U2 L2), 1qt edges will be FV (bad) and RH (good), fr=1: +1+2+0(+5)
- (B2 U2 F2 L2 D')
    - After (R2 U2 L2), 1qt edges will be FV (bad) and RD (good), fr=1: +1+2+0(+5)
- (B2 U2 F2 R2 U')
    - After (R2 U2 R2), 1qt edges will be FV (bad) and RH (good), fr=1: +1+2+0(+5)
- 5 more variants of this skeleton pass the meta, not reached before the stop.

Stop: 10 HTRs done, nothing within goal. This DR's optimal is 14, over the goal.

### 2c3, scramble 11

`R' U' F R2 D' R' L' B U' F' L U2 L2 D' R2 F2 U2 L2 D2 L2 U R' B R' U' F`

2c3 4e, goal 13.

Skeleton starting with R2 U has FD corners, L=7, 6 spare moves.

- R2 U
    - After B2, 1qt edges will be FH (bad) and RV (bad): +0+0+0(+5)
        - B2 U' R2 U // no good
    - After R2 F2, 1qt edges will be FH (bad) and RH (good): +0+1+4(+3)
- L2 U
    - After B2 L2, 1qt edges will be FH (bad) and RH (good): +0+1+0(+3)
        - B2 L2 U B2 U' // no good
- F2 L2 U'
    - After F2, 1qt edges will be FD (good) and RH (good): +1+0+1(+0)
        - F2 U R2 B2 D // 2 pairs, no good
    - After B2, 1qt edges will be FV (bad) and RV (bad): +1+0+1(+5)
- B2 L2 U'
    - After F2 L2 B2 R2, 1qt edges will be FD (good) and RV (bad): +1+3+1(+3)
- B2 R2 U'
    - After L2 F2 R2 B2, 1qt edges will be FD (good) and RV (bad): +1+3+1(+3)
- 55 more variants of this skeleton pass the meta, not reached before the stop.

Check inverse. Skeleton starting with (F2 U) has RD corners.

- (F2 U)
    - After (F2 B2 L2), 1qt edges will be RV (bad) and FH (good): +0+2+0(+3)
        - (F2 B2 L2 U' F2 U' B2 R2 F2 D2 R2) // 13
    - After (B2 L2 U2 F2 B2), 1qt edges will be RV (bad) and FD (good): +0+4+0(+3)
- (B2 D)
    - After (F2 R2), 1qt edges will be RV (bad) and FD (good): +0+1+0(+3)
        - (F2 R2 U B2 U) // no good
    - After (F2 R2), 1qt edges will be RV (bad) and FD (good): +0+1+2(+3)
        - (F2 R2 U R2 L2 F2 D) // no good
- (R2 B2 D)
    - After (F2 U2 F2), 1qt edges will be RH (bad) and FV (bad), fr=1: +1+2+0(+5)
    - After (B2 R2 F2 U2 R2), 1qt edges will be RV (bad) and FH (good): +1+4+0(+3)
- (R2 F2 U')
    - After (B2 R2 L2), 1qt edges will be RH (bad) and FV (bad): +1+2+0(+5)
    - After (F2 L2 F2 L2), 1qt edges will be RH (bad) and FH (good): +1+3+0(+3)
- (R2 B2 D')
    - After (F2 L2 F2 L2), 1qt edges will be RH (bad) and FH (good): +1+3+0(+3)
- (R2 F2 U)
    - After (B2 U2 L2 B2), 1qt edges will be RV (bad) and FV (bad), fr=1: +1+3+0(+5)
    - After (B2 R2 F2 U2 L2), 1qt edges will be RV (bad) and FH (good): +1+4+0(+3)
- 34 more variants of this skeleton pass the meta, not reached before the stop.

Skeleton starting with U2 R2 U' has FV corners, L=9, 4 spare moves.

- U2 R2 U'
    - After F2, 1qt edges will be FH (bad) and RV (good): +0+0+0(+3)
        - F2 U R2 U' // no good
    - After B2 U2 R2 B2 R2, 1qt edges will be FV (good) and RV (good): +0+4+0(+1)
- U2 L2 U'
    - After F2 L2, 1qt edges will be FH (bad) and RH (good): +0+1+0(+3)
        - F2 L2 U' F2 U // no good
    - After F2 L2, 1qt edges will be FH (bad) and RH (good), fr=1: +0+1+2(+2)
- U2 L2 U
    - After L2 U2 F2 L2, 1qt edges will be FH (bad) and RH (good), fr=1: +0+3+0(+2)
- R2 U2 R2 U
    - After F2, 1qt edges will be FH (bad) and RV (good), fr=1: +1+0+0(+2)
        - F2 U R2 U // 2 pairs, no good
- U2 B2 R2 U
    - After R2, 1qt edges will be FH (bad) and RV (good): +1+0+1(+3)
    - After L2, 1qt edges will be FD (bad) and RD (bad): +1+0+1(+5)
- L2 U2 L2 U
    - After F2 L2, 1qt edges will be FH (bad) and RD (bad), fr=1: +1+1+0(+5)
- R2 U2 R2 U'
    - After F2 U2 F2, 1qt edges will be FH (bad) and RV (good): +1+2+0(+3)
- 12 more variants of this skeleton pass the meta, not reached before the stop.

Check inverse. Skeleton starting with (U2 B2 U') has RV corners.

- (U2 B2 U')
    - After (L2), 1qt edges will be RH (bad) and FV (good), fr=1: +0+0+3(+2)
- (U2 F2 U')
    - After (B2), 1qt edges will be RH (bad) and FD (bad), fr=1: +0+0+3(+5)
    - After (L2 B2), 1qt edges will be RH (bad) and FH (good), fr=1: +0+1+3(+2)
- (U2 B2 U)
    - After (R2 U2 F2 R2), 1qt edges will be RH (bad) and FH (good), fr=1: +0+3+1(+2)
- (U2 F2 U)
    - After (B2 U2 R2 F2), 1qt edges will be RH (bad) and FH (good), fr=1: +0+3+1(+2)
    - After (F2 U2 R2 B2), 1qt edges will be RD (bad) and FD (bad), fr=1: +0+3+1(+5)
- (U2 L2 B2 U)
    - After (L2 B2), 1qt edges will be RD (bad) and FD (bad): +1+1+0(+5)
- (U2 L2 F2 U')
    - After (R2 U2 L2), 1qt edges will be RV (good) and FH (good), fr=1: +1+2+0(+1)
        - (R2 U2 L2 U F2 U') // no good
- (U2 R2 B2 D)
    - After (L2 F2 B2), 1qt edges will be RD (bad) and FH (good): +1+2+0(+3)
- (U2 R2 F2 D)
    - After (R2 L2 F2), 1qt edges will be RH (bad) and FV (good): +1+2+0(+3)

Stop: 10 HTRs done, one finish within goal (13). This DR's optimal is 13.

### 2c3, scramble 12

`R' U' F R' U D L2 F2 B' R2 D2 L' F' B2 R' F2 R' F2 U2 R D2 F2 D2 R' U' F`

2c3 6e, goal 13.

Skeleton starting with R2 U' has FD corners, L=7, 6 spare moves.

- L2 D'
    - After R2 B2, 1qt edges will be FD (good) and RD (good): +0+1+2(+1)
        - R2 B2 U' L2 F2 B2 D // no good
    - After F2 B2 R2 F2, 1qt edges will be FD (good) and RD (good): +0+3+0(+1)
        - F2 B2 R2 F2 U' R2 U' // no good
    - After B2 U2 R2 L2, 1qt edges will be FD (good) and RV (bad): +0+3+0(+3)
        - B2 U2 R2 L2 U' L2 U' // 2 pairs, no good
- R2 U
    - After B2 U2 B2, 1qt edges will be FD (good) and RD (good), fr=1: +0+2+3(+4)
- F2 L2 D
    - After R2, 1qt edges will be FV (bad) and RV (bad): +1+0+2(+5)
    - After L2 F2 L2 B2, 1qt edges will be FV (bad) and RH (good): +1+3+0(+3)
    - After B2 R2 B2 L2 B2, 1qt edges will be FH (bad) and RH (good): +1+4+0(+3)
- B2 L2 U
    - After F2, 1qt edges will be FV (bad) and RH (good): +1+0+3(+3)
- F2 L2 D'
    - After R2 U2 L2, 1qt edges will be FV (bad) and RV (bad), fr=1: +1+2+2(+5)
    - After R2 B2 L2 U2 F2, 1qt edges will be FH (bad) and RH (good): +1+4+0(+3)
- 55 more variants of this skeleton pass the meta, not reached before the stop.

Check inverse. Skeleton starting with (F2 U) has RD corners.

- (F2 U)
    - After (B2 L2), 1qt edges will be RV (bad) and FH (good): +0+1+1(+3)
        - (B2 L2 U R2 B2 U') // 2 pairs, no good
        - (B2 L2 U L2 F2 D') // 2 pairs, no good
- (B2 D)
    - After (F2 R2), 1qt edges will be RD (good) and FV (bad): +0+1+2(+3)
        - (F2 R2 U L2 F2 B2 D') // no good
- (R2 F2 U')
    - After (B2), 1qt edges will be RH (bad) and FV (bad): +1+0+3(+5)
- (R2 B2 D)
    - After (F2 U2 L2 B2), 1qt edges will be RV (bad) and FH (good), fr=1: +1+3+0(+5)
    - After (F2 B2 U2 L2 B2), 1qt edges will be RV (bad) and FH (good): +1+4+0(+3)
- (L2 F2 U)
    - After (B2 L2 F2 U2 L2), 1qt edges will be RD (good) and FV (bad): +1+4+0(+3)
- 32 more variants of this skeleton pass the meta, not reached before the stop.

Skeleton starting with R2 U' F2 U R2 U' has HH corners, L=9, 4 spare moves. Apply (U) and NISS: HH corners.

- L2 D' B2 U
    - After B2, 1qt edges will be RD (bad) and FV (bad): +0+0+2(+6)
    - After R2 B2 R2 F2 R2, 1qt edges will be RH (good) and FD (bad): +0+4+0(+3)
- R2 U' F2 D
    - After B2, 1qt edges will be RV (bad) and FV (bad): +0+0+3(+6)
    - After R2 B2, 1qt edges will be RH (good) and FV (bad): +0+1+3(+3)
- L2 D' F2 U
    - After F2 L2, 1qt edges will be RH (good) and FV (bad): +0+1+3(+3)
- R2 U' B2 U
    - After L2 B2, 1qt edges will be RD (bad) and FH (good), fr=1: +0+1+3(+5)
- L2 D' B2 U'
    - After B2 R2 F2 U2 R2, 1qt edges will be RH (good) and FD (bad): +0+4+0(+3)
- R2 U' B2 U'
    - After F2 U2 L2 F2, 1qt edges will be RH (good) and FV (bad), fr=1: +0+3+1(+5)
- F2 R2 U L2 D'
    - After B2, 1qt edges will be RH (good) and FD (bad): +1+0+2(+3)
- R2 U' L2 B2 U'
    - After L2, 1qt edges will be RH (good) and FD (bad): +1+0+2(+3)
- R2 U' R2 B2 U'
    - After R2, 1qt edges will be RH (good) and FD (bad): +1+0+2(+3)
- L2 D' L2 B2 U'
    - After L2, 1qt edges will be RV (bad) and FV (bad): +1+0+2(+6)
- R2 U' L2 F2 D'
    - After R2, 1qt edges will be RD (bad) and FD (bad): +1+0+2(+6)
    - After F2 L2 F2 B2, 1qt edges will be RD (bad) and FH (good): +1+3+0(+3)
- R2 U' R2 F2 D'
    - After L2, 1qt edges will be RD (bad) and FD (bad): +1+0+2(+6)
    - After B2 R2 F2 B2, 1qt edges will be RD (bad) and FH (good): +1+3+0(+3)
- L2 D' R2 B2 U'
    - After F2 R2, 1qt edges will be RH (good) and FD (bad): +1+1+1(+3)
    - After F2 B2 L2, 1qt edges will be RH (good) and FH (good): +1+2+1(+0)
        - F2 B2 L2 U F2 L2 D // 0 pairs, no good
- B2 L2 D L2 U'
    - After B2 L2, 1qt edges will be RD (bad) and FD (bad): +1+1+1(+6)
- L2 D' R2 F2 D'
    - After F2 B2 R2, 1qt edges will be RH (good) and FV (bad): +1+2+0(+3)
- F2 L2 D R2 U'
    - After R2, 1qt edges will be RH (good) and FH (good): +1+0+3(+0)
        - R2 U R2 B2 R2 L2 D' // 0 pairs, no good
        - R2 U L2 F2 R2 L2 U' // 0 pairs, no good
- F2 L2 D L2 U'
    - After B2, 1qt edges will be RH (good) and FV (bad): +1+0+3(+3)
- B2 R2 U L2 U'
    - After F2, 1qt edges will be RH (good) and FV (bad), fr=1: +1+0+3(+5)
- R2 U' L2 F2 D
    - After B2 R2 U2 B2, 1qt edges will be RH (good) and FH (good), fr=1: +1+3+0(+5)
- R2 U' R2 F2 D
    - After F2 L2 U2 F2, 1qt edges will be RH (good) and FH (good), fr=1: +1+3+0(+5)
- B2 L2 D R2 U
    - After B2 U2 R2 B2, 1qt edges will be RV (bad) and FV (bad), fr=1: +1+3+0(+6)
- R2 U' L2 B2 U
    - After B2 L2 U2 F2, 1qt edges will be RD (bad) and FV (bad), fr=1: +1+3+0(+6)
- R2 U' R2 B2 U
    - After F2 R2 U2 B2, 1qt edges will be RD (bad) and FV (bad), fr=1: +1+3+0(+6)
- 2 more variants of this skeleton pass the meta, not reached before the stop.

The same skeleton in full, for the solutions that go on after its last quarter turn.

- L2 D' B2 U F2 U'
    - After F2, 1qt edges will be RV (bad) and FD (bad): +0+0+3(+6)
- R2 U' B2 U B2 U'
    - After R2 B2, 1qt edges will be RV (bad) and FH (good): +0+1+2(+3)
- R2 U' B2 U F2 D'
    - After R2 F2, 1qt edges will be RH (good) and FV (bad): +0+1+2(+3)
- R2 U' F2 U L2 D'
    - After R2 B2, 1qt edges will be RD (bad) and FV (bad): +0+1+2(+6)
- R2 U' F2 U R2 U'
    - After L2 B2, 1qt edges will be RV (bad) and FD (bad): +0+1+2(+6)
- L2 D' B2 U R2 F2 U
    - After L2, 1qt edges will be RH (good) and FV (bad): +1+0+2(+3)
- R2 U' L2 B2 D' F2 U
    - After L2, 1qt edges will be RV (bad) and FH (good): +1+0+2(+3)
- R2 U' R2 B2 U' L2 D
    - After L2, 1qt edges will be RH (good) and FV (bad): +1+0+2(+3)
- R2 U' L2 B2 D' B2 D
    - After R2, 1qt edges will be RH (good) and FH (good): +1+0+3(+0)
        - R2 U R2 F2 R2 U' // 0 pairs, no good
- L2 D' F2 U F2 L2 U
    - After R2, 1qt edges will be RH (good) and FD (bad): +1+0+3(+3)
- L2 D' L2 F2 U' F2 U
    - After L2, 1qt edges will be RH (good) and FD (bad): +1+0+3(+3)
- R2 U' B2 U R2 B2 U
    - After L2, 1qt edges will be RH (good) and FD (bad): +1+0+3(+3)
- R2 U' F2 U B2 R2 U
    - After L2, 1qt edges will be RD (bad) and FH (good): +1+0+3(+3)
- R2 U' F2 U F2 L2 D
    - After L2, 1qt edges will be RV (bad) and FH (good): +1+0+3(+3)
- B2 L2 U F2 U' L2 U
    - After L2, 1qt edges will be RD (bad) and FV (bad): +1+0+3(+6)
- L2 D' B2 U L2 F2 U
    - After L2, 1qt edges will be RV (bad) and FV (bad): +1+0+3(+6)
- L2 D' B2 U R2 B2 D
    - After R2, 1qt edges will be RD (bad) and FV (bad): +1+0+3(+6)
- L2 D' F2 U B2 R2 D
    - After R2, 1qt edges will be RD (bad) and FD (bad): +1+0+3(+6)
- L2 D' L2 B2 U' R2 U
    - After R2, 1qt edges will be RD (bad) and FD (bad): +1+0+3(+6)
- R2 U' B2 U L2 F2 D
    - After R2, 1qt edges will be RV (bad) and FD (bad): +1+0+3(+6)
- R2 U' L2 F2 D' L2 U
    - After R2, 1qt edges will be RV (bad) and FV (bad): +1+0+3(+6)
- B2 R2 U R2 U' L2 D
    - After B2 R2, 1qt edges will be RH (good) and FD (bad): +1+1+2(+3)
- 3 more variants of this skeleton pass the meta, not reached before the stop.

Stop: 10 HTRs done, nothing within goal. This DR's optimal is 14, over the goal.

## 2c4

### 2c4, scramble 1

`R' U' F U' F' U' D2 L' B2 U' F' D2 R D2 L2 U2 L B2 R' B2 U2 B2 U' R' U' F`

2c4 6e, goal 14.

Skeleton starting with L2 U' L2 U has RV corners, L=10, 4 spare moves.

- L2 U' L2 U
    - After R2 B2, 1qt edges will be RV (good) and FH (good): +0+1+1(+0)
        - R2 B2 U F2 R2 U' // 2 pairs, no good
        - R2 B2 U B2 L2 D' // 2 pairs, no good
- R2 D' L2 U
    - After L2, 1qt edges will be RH (bad) and FD (bad), fr=1: +0+0+3(+5)
    - After F2 L2, 1qt edges will be RH (bad) and FH (good), fr=1: +0+1+3(+2)
- L2 U' R2 D
    - After F2 L2 B2 L2, 1qt edges will be RH (bad) and FV (good): +0+3+0(+3)
- R2 D' R2 U
    - After L2 B2, 1qt edges will be RD (bad) and FD (bad): +0+1+3(+5)
- L2 U' R2 D'
    - After B2 U2 L2 F2, 1qt edges will be RD (bad) and FD (bad), fr=1: +0+3+0(+5)
    - After B2 R2 B2 U2 L2, 1qt edges will be RD (bad) and FV (good): +0+4+0(+3)
- L2 U' L2 U'
    - After R2 B2 U2 R2, 1qt edges will be RV (good) and FD (bad), fr=1: +0+3+1(+2)
- R2 D' L2 U'
    - After R2 U2 B2 R2, 1qt edges will be RH (bad) and FH (good), fr=1: +0+3+1(+2)
    - After L2 U2 B2 L2, 1qt edges will be RD (bad) and FD (bad), fr=1: +0+3+1(+5)
- F2 L2 U F2 D'
    - After R2 F2, 1qt edges will be RH (bad) and FV (good): +1+1+0(+3)
    - After R2 F2, 1qt edges will be RH (bad) and FV (good), fr=1: +1+1+2(+2)
- B2 L2 U B2 D'
    - After B2, 1qt edges will be RV (good) and FD (bad): +1+0+2(+3)
- F2 R2 D F2 U'
    - After R2, 1qt edges will be RD (bad) and FH (good): +1+0+2(+3)
- L2 U' B2 L2 U'
    - After R2, 1qt edges will be RH (bad) and FV (good): +1+0+2(+3)
- F2 L2 U B2 D
    - After L2 U2 L2, 1qt edges will be RV (good) and FH (good), fr=1: +1+2+0(+1)
        - L2 U2 L2 U' R2 U' // no good
- R2 D' B2 R2 U'
    - After L2, 1qt edges will be RD (bad) and FH (good), fr=1: +1+0+3(+2)
- L2 U' F2 L2 U'
    - After R2, 1qt edges will be RD (bad) and FV (good): +1+0+3(+3)
- B2 R2 D F2 U'
    - After F2, 1qt edges will be RD (bad) and FD (bad): +1+0+3(+5)
- R2 D' F2 R2 U'
    - After R2, 1qt edges will be RH (bad) and FD (bad), fr=1: +1+0+3(+5)
- R2 D' B2 R2 U
    - After L2 U2 R2, 1qt edges will be RH (bad) and FV (good), fr=1: +1+2+1(+2)
- 3 more variants of this skeleton pass the meta, not reached before the stop.

Check inverse. Skeleton starting with (U2 L2 D' F2 U') has RD corners.

- (U2 L2 D' F2 U')
    - After (R2 L2 B2), 1qt edges will be RH (bad) and FD (good): +0+2+0(+3)
- (U2 R2 U' B2 D')
    - After (F2), 1qt edges will be RD (good) and FD (good): +0+0+3(+1)
        - (F2 U L2 F2 R2 B2 D) // 10 pairs, no good
        - (F2 U L2 F2 L2 F2 U) // 6 pairs, no good
        - (F2 U L2 B2 L2 B2 U) // 6 pairs, no good
- (U2 L2 D' B2 U')
    - After (R2), 1qt edges will be RH (bad) and FV (bad): +0+0+3(+5)
- (U2 R2 U' F2 U')
    - After (L2 B2), 1qt edges will be RH (bad) and FD (good), fr=1: +0+1+3(+5)
- (U2 L2 D' F2 U)
    - After (F2 R2 F2 U2 R2), 1qt edges will be RD (good) and FV (bad): +0+4+0(+3)
- (U2 R2 U' F2 U)
    - After (B2 U2 L2 B2), 1qt edges will be RH (bad) and FD (good), fr=1: +0+3+1(+5)
- (U2 B2 R2 U R2 D)
    - After (R2), 1qt edges will be RH (bad) and FH (good): +1+0+2(+3)
- (R2 U2 L2 D F2 U')
    - After (F2), 1qt edges will be RH (bad) and FD (good), fr=1: +1+0+2(+5)
- (U2 R2 U' L2 B2 D)
    - After (R2), 1qt edges will be RV (bad) and FV (bad): +1+0+2(+5)
- (U2 R2 U' L2 F2 U)
    - After (L2), 1qt edges will be RH (bad) and FV (bad): +1+0+2(+5)
- (U2 R2 U' R2 B2 D)
    - After (L2), 1qt edges will be RV (bad) and FV (bad): +1+0+2(+5)
- (U2 R2 U' R2 F2 U)
    - After (R2), 1qt edges will be RH (bad) and FV (bad): +1+0+2(+5)
- (U2 L2 D' R2 B2 U)
    - After (R2 B2), 1qt edges will be RV (bad) and FV (bad): +1+1+1(+5)
    - After (F2), 1qt edges will be RD (good) and FV (bad): +1+0+3(+3)
- (U2 F2 L2 D L2 U)
    - After (F2 B2 R2), 1qt edges will be RH (bad) and FD (good): +1+2+0(+3)
- (U2 L2 D' R2 F2 U)
    - After (F2 B2 L2), 1qt edges will be RV (bad) and FH (good): +1+2+0(+3)
- (L2 U2 R2 U F2 D')
    - After (R2 L2 F2), 1qt edges will be RD (good) and FD (good), fr=1: +1+2+0(+4)
- (L2 U2 L2 D B2 U')
    - After (R2 L2 F2), 1qt edges will be RV (bad) and FD (good), fr=1: +1+2+0(+5)
- (L2 U2 R2 U B2 D')
    - After (R2 F2 B2), 1qt edges will be RV (bad) and FV (bad), fr=1: +1+2+0(+5)
- (U2 B2 L2 D L2 U)
    - After (F2), 1qt edges will be RV (bad) and FD (good): +1+0+3(+3)
- (U2 B2 L2 D R2 U)
    - After (R2), 1qt edges will be RV (bad) and FH (good): +1+0+3(+3)
- (U2 F2 L2 D R2 U)
    - After (B2), 1qt edges will be RV (bad) and FD (good): +1+0+3(+3)
- (R2 U2 R2 U B2 D')
    - After (F2), 1qt edges will be RD (good) and FD (good), fr=1: +1+0+3(+4)
- (L2 U2 L2 D F2 U')
    - After (L2), 1qt edges will be RV (bad) and FV (bad), fr=1: +1+0+3(+5)
- (U2 F2 R2 U L2 U)
    - After (B2), 1qt edges will be RV (bad) and FD (good), fr=1: +1+0+3(+5)
- 8 more variants of this skeleton pass the meta, not reached before the stop.

Skeleton starting with L2 U L2 D' has FV corners, L=10, 4 spare moves.

- L2 U L2 D'
    - After F2 B2 R2, 1qt edges will be FD (bad) and RD (bad), fr=1: +0+2+0(+5)
    - After R2 F2 L2 F2, 1qt edges will be FD (bad) and RH (good), fr=1: +0+3+0(+2)
    - After B2 R2 F2 R2 F2, 1qt edges will be FH (bad) and RH (good), fr=1: +0+4+0(+2)
- L2 U R2 U'
    - After L2, 1qt edges will be FD (bad) and RH (good), fr=1: +0+0+3(+2)
- L2 U L2 D
    - After L2 B2 L2 U2 F2, 1qt edges will be FH (bad) and RH (good), fr=1: +0+4+0(+2)
- R2 D L2 U'
    - After L2 F2 R2 B2, 1qt edges will be FH (bad) and RH (good), fr=1: +0+3+1(+2)
- R2 D R2 U'
    - After F2 L2 B2 L2, 1qt edges will be FV (good) and RD (bad), fr=1: +0+3+1(+2)
- R2 D F2 L2 U
    - After F2, 1qt edges will be FV (good) and RH (good), fr=1: +1+0+0(+1)
        - F2 U' L2 U // no good
- B2 R2 D' F2 U
    - After R2 F2, 1qt edges will be FV (good) and RH (good), fr=1: +1+1+0(+1)
        - R2 F2 U B2 U // no good
- R2 D F2 R2 U
    - After F2 R2, 1qt edges will be FV (good) and RV (good), fr=1: +1+1+0(+2)
        - F2 R2 U F2 U' // no good
    - After F2 R2, 1qt edges will be FV (good) and RV (good): +1+1+2(+1)
- F2 R2 D' B2 U
    - After B2, 1qt edges will be FD (bad) and RV (good), fr=1: +1+0+2(+2)
- L2 U F2 R2 U
    - After B2, 1qt edges will be FH (bad) and RV (good), fr=1: +1+0+2(+2)
- B2 L2 U' F2 D
    - After R2, 1qt edges will be FH (bad) and RD (bad), fr=1: +1+0+2(+5)
- R2 D B2 L2 D
    - After L2, 1qt edges will be FH (bad) and RD (bad), fr=1: +1+0+2(+5)
- L2 U B2 L2 D
    - After R2 L2 F2, 1qt edges will be FV (good) and RV (good), fr=1: +1+2+0(+2)
- B2 R2 D' B2 U'
    - After L2 U2 R2, 1qt edges will be FH (bad) and RV (good): +1+2+0(+3)
- F2 L2 U' F2 D
    - After B2, 1qt edges will be FD (bad) and RD (bad), fr=1: +1+0+3(+5)
- R2 D B2 R2 D
    - After L2 F2, 1qt edges will be FD (bad) and RD (bad), fr=1: +1+1+2(+5)
- 8 more variants of this skeleton pass the meta, not reached before the stop.

Check inverse. Skeleton starting with (U2 B2 D' L2 U') has RD corners.

- (U2 B2 D' L2 U')
    - After (B2), 1qt edges will be RV (bad) and FD (good): +0+0+3(+3)
- (U2 F2 U' L2 U')
    - After (B2), 1qt edges will be RH (bad) and FH (good), fr=1: +0+0+3(+5)
- (U2 F2 U' R2 D')
    - After (L2 F2), 1qt edges will be RV (bad) and FD (good), fr=1: +0+1+0(+5)
    - After (L2 U2 F2 U2 F2), 1qt edges will be RV (bad) and FD (good): +0+4+0(+3)
- (U2 B2 D' R2 U')
    - After (B2 R2), 1qt edges will be RH (bad) and FD (good), fr=1: +0+1+3(+5)
- (U2 F2 U' R2 D)
    - After (B2 U2 R2 B2), 1qt edges will be RV (bad) and FD (good): +0+3+0(+3)
- (U2 F2 U' L2 U)
    - After (R2 F2 U2 R2), 1qt edges will be RD (good) and FD (good): +0+3+1(+1)
    - After (R2 F2 U2 L2), 1qt edges will be RV (bad) and FV (bad): +0+3+1(+5)
- (U2 B2 D' L2 U)
    - After (F2 U2 R2 B2), 1qt edges will be RH (bad) and FD (good): +0+3+1(+3)
- (B2 U2 F2 U L2 U')
    - After (R2), 1qt edges will be RV (bad) and FV (bad): +1+0+1(+5)
    - After (B2 L2), 1qt edges will be RV (bad) and FD (good): +1+1+1(+3)
- (U2 F2 U' B2 L2 U)
    - After (R2), 1qt edges will be RV (bad) and FH (good), fr=1: +1+0+1(+5)
    - After (B2 L2), 1qt edges will be RD (good) and FH (good), fr=1: +1+1+1(+3)
    - After (R2), 1qt edges will be RV (bad) and FH (good): +1+0+3(+3)
- (U2 R2 B2 D F2 U)
    - After (R2), 1qt edges will be RH (bad) and FV (bad), fr=1: +1+0+1(+5)
    - After (R2 F2 B2), 1qt edges will be RD (good) and FD (good), fr=1: +1+2+1(+4)
- (F2 U2 F2 U R2 D')
    - After (L2 F2), 1qt edges will be RV (bad) and FV (bad): +1+1+0(+5)
- (U2 F2 U' F2 L2 U)
    - After (F2 L2), 1qt edges will be RV (bad) and FD (good), fr=1: +1+1+0(+5)
    - After (F2 L2), 1qt edges will be RV (bad) and FD (good): +1+1+2(+3)
- (U2 L2 F2 U B2 D)
    - After (F2 L2), 1qt edges will be RH (bad) and FV (bad), fr=1: +1+1+0(+5)
- (U2 R2 F2 U B2 D)
    - After (R2 B2), 1qt edges will be RH (bad) and FH (good), fr=1: +1+1+0(+5)
    - After (R2 B2), 1qt edges will be RH (bad) and FH (good): +1+1+2(+3)
- (U2 R2 B2 D B2 U')
    - After (F2 U2 F2), 1qt edges will be RV (bad) and FD (good): +1+2+0(+3)
- (U2 R2 F2 U F2 D')
    - After (L2 U2 L2), 1qt edges will be RD (good) and FV (bad): +1+2+0(+3)
- (B2 U2 F2 U R2 D)
    - After (L2 U2 R2), 1qt edges will be RH (bad) and FH (good), fr=1: +1+2+0(+5)
- (U2 F2 U' F2 R2 U)
    - After (B2), 1qt edges will be RD (good) and FH (good): +1+0+3(+0)
        - (B2 U F2 L2 U2 B2 U') // 8 pairs, no good
    - After (F2), 1qt edges will be RV (bad) and FD (good): +1+0+3(+3)
- (F2 U2 F2 U L2 U')
    - After (B2), 1qt edges will be RH (bad) and FH (good): +1+0+3(+3)
- (B2 U2 B2 D R2 U')
    - After (F2), 1qt edges will be RV (bad) and FV (bad), fr=1: +1+0+3(+5)
- (U2 B2 D' F2 R2 U)
    - After (B2), 1qt edges will be RV (bad) and FV (bad): +1+0+3(+5)
- (U2 L2 B2 D B2 U)
    - After (L2), 1qt edges will be RH (bad) and FV (bad), fr=1: +1+0+3(+5)
- (U2 L2 F2 U F2 U)
    - After (R2), 1qt edges will be RV (bad) and FD (good), fr=1: +1+0+3(+5)
- 9 more variants of this skeleton pass the meta, not reached before the stop.

Stop: 10 HTRs done, nothing within goal. This DR's optimal is 14.

### 2c4, scramble 2

`R' U' F R F U F D' F' U2 R' U' R' U2 F2 D2 B2 R2 B2 U R2 F2 B2 R' U' F`

2c4 6e, goal 14.

Skeleton starting with B2 U' L2 D has FD corners, L=9, 5 spare moves.

- B2 U' L2 D
    - After L2, 1qt edges will be FV (bad) and RV (bad): +0+0+2(+5)
    - After R2 B2 R2 F2, 1qt edges will be FV (bad) and RH (good): +0+3+0(+3)
    - After F2 R2 U2 L2 F2 L2, 1qt edges will be FD (good) and RV (bad): +0+5+0(+3)
- F2 D' R2 U
    - After R2, 1qt edges will be FD (good) and RV (bad): +0+0+3(+3)
- B2 U' R2 U
    - After F2 L2, 1qt edges will be FD (good) and RD (good): +0+1+3(+1)
        - F2 L2 U B2 R2 F2 B2 D' // 6 pairs, no good
        - F2 L2 U F2 L2 F2 B2 U' // 4 pairs, no good
    - After R2 L2 F2 R2, 1qt edges will be FD (good) and RD (good): +0+3+1(+1)
        - R2 L2 F2 R2 U F2 R2 D' // 6 pairs, no good
- F2 D' L2 U
    - After R2 F2, 1qt edges will be FH (bad) and RV (bad), fr=1: +0+1+3(+5)
    - After B2 U2 B2 R2 F2, 1qt edges will be FH (bad) and RD (good): +0+4+1(+3)
- B2 U' L2 D'
    - After L2 F2 R2 U2 B2, 1qt edges will be FH (bad) and RH (good): +0+4+0(+3)
    - After R2 U2 F2 B2 L2, 1qt edges will be FV (bad) and RV (bad), fr=1: +0+4+0(+5)
    - After L2 F2 U2 B2 U2 R2, 1qt edges will be FH (bad) and RH (good): +0+5+0(+3)
- F2 D' R2 U'
    - After R2 U2 L2, 1qt edges will be FD (good) and RV (bad), fr=1: +0+2+3(+5)
- F2 D' L2 U'
    - After B2 U2 R2 B2, 1qt edges will be FV (bad) and RD (good), fr=1: +0+3+1(+5)
- B2 U' R2 U'
    - After R2 L2 U2 B2 R2, 1qt edges will be FD (good) and RD (good): +0+4+1(+1)
    - After R2 L2 U2 B2 L2, 1qt edges will be FH (bad) and RV (bad): +0+4+1(+5)
- B2 U' B2 L2 D'
    - After B2, 1qt edges will be FD (good) and RV (bad): +1+0+2(+3)
- R2 F2 D B2 U'
    - After L2, 1qt edges will be FH (bad) and RH (good): +1+0+2(+3)
- B2 U' F2 R2 U'
    - After R2 L2 F2, 1qt edges will be FH (bad) and RV (bad): +1+2+0(+5)
- R2 B2 U B2 U'
    - After B2, 1qt edges will be FV (bad) and RH (good): +1+0+3(+3)
- L2 F2 D B2 U'
    - After B2, 1qt edges will be FH (bad) and RV (bad), fr=1: +1+0+3(+5)
- L2 B2 U F2 D'
    - After R2 L2 B2 L2, 1qt edges will be FD (good) and RV (bad): +1+3+0(+3)
- F2 D' B2 L2 D
    - After L2 B2 U2 L2, 1qt edges will be FV (bad) and RV (bad), fr=1: +1+3+0(+5)
- F2 D' B2 R2 U
    - After L2 F2 U2 R2, 1qt edges will be FH (bad) and RD (good), fr=1: +1+3+0(+5)
- F2 D' F2 L2 D
    - After R2 F2 U2 R2, 1qt edges will be FV (bad) and RV (bad), fr=1: +1+3+0(+5)
- F2 D' F2 R2 U
    - After R2 B2 U2 L2, 1qt edges will be FH (bad) and RD (good), fr=1: +1+3+0(+5)
- L2 B2 U F2 D
    - After L2 U2 B2 R2, 1qt edges will be FD (good) and RV (bad), fr=1: +1+3+0(+5)
- L2 F2 D F2 U'
    - After F2 R2, 1qt edges will be FD (good) and RV (bad): +1+1+3(+3)
- B2 U' B2 L2 D
    - After B2 U2 F2, 1qt edges will be FD (good) and RV (bad), fr=1: +1+2+2(+5)
- B2 U' F2 R2 U
    - After F2 U2 B2, 1qt edges will be FH (bad) and RV (bad), fr=1: +1+2+2(+5)
- R2 F2 D B2 U
    - After L2 U2 L2, 1qt edges will be FH (bad) and RH (good), fr=1: +1+2+2(+5)
- L2 F2 D B2 U
    - After F2 U2 L2 F2, 1qt edges will be FH (bad) and RH (good), fr=1: +1+3+1(+5)
- 31 more variants of this skeleton pass the meta, not reached before the stop.

Check inverse. Skeleton starting with (B2 D F2 U') has FD corners.

- (B2 D F2 U')
    - After (R2 L2 F2), 1qt edges will be FV (bad) and RH (good): +0+2+0(+3)
        - (R2 L2 F2 U L2 U') // 2 pairs, no good
- (F2 U F2 U')
    - After (L2), 1qt edges will be FV (bad) and RH (good): +0+0+3(+3)
- (F2 U B2 D')
    - After (F2 R2), 1qt edges will be FD (good) and RD (good): +0+1+0(+1)
        - (F2 R2 U' B2 U) // no good
- (B2 D B2 U')
    - After (L2 F2 B2), 1qt edges will be FD (good) and RD (good): +0+2+0(+1)
        - (L2 F2 B2 U L2 U) // no good
- (B2 D F2 U)
    - After (R2 F2 U2 L2), 1qt edges will be FH (bad) and RV (bad), fr=1: +0+3+0(+5)
    - After (B2 L2 B2 U2 R2), 1qt edges will be FD (good) and RV (bad): +0+4+0(+3)
    - After (F2 B2 U2 B2), 1qt edges will be FV (bad) and RH (good): +0+3+2(+3)
- (F2 U F2 U)
    - After (B2 R2 U2 F2), 1qt edges will be FD (good) and RV (bad), fr=1: +0+3+1(+5)
    - After (R2 F2 R2 U2 B2), 1qt edges will be FD (good) and RD (good): +0+4+1(+1)
- (B2 D B2 U)
    - After (L2 U2 F2 L2), 1qt edges will be FH (bad) and RD (good), fr=1: +0+3+0(+5)
    - After (F2 B2 U2 F2 B2 R2), 1qt edges will be FD (good) and RD (good): +0+5+0(+1)
- (R2 F2 U' R2 U)
    - After (B2), 1qt edges will be FV (bad) and RD (good): +1+0+3(+3)
- (F2 U R2 B2 U)
    - After (R2), 1qt edges will be FD (good) and RD (good), fr=1: +1+0+3(+4)
    - After (R2), 1qt edges will be FD (good) and RD (good): +1+0+4(+1)
- (B2 D R2 B2 U)
    - After (B2), 1qt edges will be FV (bad) and RH (good), fr=1: +1+0+3(+5)
    - After (B2), 1qt edges will be FV (bad) and RH (good): +1+0+4(+3)
- (B2 D R2 F2 U)
    - After (R2), 1qt edges will be FH (bad) and RH (good), fr=1: +1+0+3(+5)
    - After (R2), 1qt edges will be FH (bad) and RH (good): +1+0+4(+3)
- (F2 U R2 B2 U')
    - After (R2 U2 R2), 1qt edges will be FD (good) and RD (good), fr=1: +1+2+1(+4)
- (F2 U L2 B2 D')
    - After (L2 B2 U2 L2), 1qt edges will be FD (good) and RH (good), fr=1: +1+3+0(+3)
- (R2 F2 U' L2 D')
    - After (B2 U2 L2 B2), 1qt edges will be FD (good) and RH (good), fr=1: +1+3+0(+3)
- (F2 U R2 F2 U')
    - After (F2 U2 R2 F2), 1qt edges will be FD (good) and RD (good), fr=1: +1+3+0(+4)
- (L2 B2 D' L2 U')
    - After (F2 U2 R2 F2), 1qt edges will be FD (good) and RD (good), fr=1: +1+3+0(+4)
- (L2 F2 U' R2 U)
    - After (B2 L2), 1qt edges will be FD (good) and RD (good): +1+1+3(+1)
- (B2 D L2 F2 U)
    - After (F2 R2), 1qt edges will be FH (bad) and RD (good): +1+1+3(+3)
- (B2 D L2 B2 U)
    - After (R2 F2), 1qt edges will be FV (bad) and RV (bad): +1+1+3(+5)
- (B2 D R2 B2 U')
    - After (B2 U2 L2 F2), 1qt edges will be FD (good) and RH (good), fr=1: +1+3+1(+3)
- (B2 D R2 F2 U')
    - After (L2 U2 F2 L2), 1qt edges will be FD (good) and RH (good), fr=1: +1+3+1(+3)
    - After (R2 U2 F2 R2), 1qt edges will be FH (bad) and RD (good), fr=1: +1+3+1(+5)
- (F2 U L2 F2 U')
    - After (R2 B2 U2 L2), 1qt edges will be FD (good) and RH (good), fr=1: +1+3+1(+3)
- (R2 B2 D' L2 U)
    - After (L2 B2 R2 F2), 1qt edges will be FV (bad) and RH (good): +1+3+1(+3)
- (R2 B2 D' R2 U)
    - After (B2 L2 F2 R2), 1qt edges will be FV (bad) and RH (good): +1+3+1(+3)
- (L2 F2 U' L2 U')
    - After (F2 U2 L2 B2), 1qt edges will be FD (good) and RD (good), fr=1: +1+3+1(+4)
- (R2 F2 U' R2 U')
    - After (L2 B2 U2 L2), 1qt edges will be FH (bad) and RH (good), fr=1: +1+3+1(+5)
- 44 more variants of this skeleton pass the meta, not reached before the stop.

Skeleton starting with B2 U R2 D' has FV corners, L=10, 4 spare moves.

- F2 D L2 U'
    - After B2 U2 F2 B2, 1qt edges will be FV (good) and RH (good): +0+3+0(+0)
        - B2 U2 F2 B2 U' L2 U' // 1 pair, no good
    - After B2 L2 B2 L2, 1qt edges will be FD (bad) and RH (good): +0+3+0(+3)
- F2 D R2 U'
    - After F2 R2, 1qt edges will be FH (bad) and RD (bad): +0+1+0(+5)
    - After R2 U2 F2 R2 F2, 1qt edges will be FD (bad) and RV (good): +0+4+0(+3)
- F2 D L2 U
    - After B2 U2 F2, 1qt edges will be FV (good) and RH (good), fr=1: +0+2+0(+1)
        - B2 U2 F2 U' L2 U // no good
    - After F2 B2 U2 F2, 1qt edges will be FV (good) and RH (good): +0+3+0(+0)
        - F2 B2 U2 F2 U L2 U' // 1 pair, no good
- B2 U R2 D
    - After F2 U2 B2, 1qt edges will be FD (bad) and RH (good), fr=1: +0+2+2(+2)
- F2 D R2 U
    - After F2 R2 U2 F2, 1qt edges will be FH (bad) and RV (good), fr=1: +0+3+0(+2)
    - After L2 U2 F2 R2, 1qt edges will be FH (bad) and RD (bad), fr=1: +0+3+0(+5)
- B2 U F2 R2 D
    - After R2, 1qt edges will be FH (bad) and RH (good): +1+0+2(+3)
- R2 F2 D' F2 U
    - After F2, 1qt edges will be FD (bad) and RD (bad): +1+0+2(+5)
- L2 B2 U' B2 D
    - After R2 L2 F2, 1qt edges will be FD (bad) and RV (good): +1+2+0(+3)
- F2 D F2 R2 U
    - After F2, 1qt edges will be FD (bad) and RV (good), fr=1: +1+0+3(+2)
- R2 B2 U' B2 U
    - After F2, 1qt edges will be FH (bad) and RV (good), fr=1: +1+0+3(+2)
- L2 B2 U' F2 U
    - After B2, 1qt edges will be FH (bad) and RV (good): +1+0+3(+3)
- B2 U B2 R2 U
    - After F2, 1qt edges will be FH (bad) and RD (bad): +1+0+3(+5)
- F2 D F2 L2 U
    - After R2, 1qt edges will be FD (bad) and RD (bad), fr=1: +1+0+3(+5)
- B2 U B2 L2 U
    - After B2 R2, 1qt edges will be FD (bad) and RV (good): +1+1+2(+3)
- 12 more variants of this skeleton pass the meta, not reached before the stop.

Check inverse. Skeleton starting with (U2 F2 D' B2 U) has FD corners.

- (U2 F2 D' B2 U')
    - After (B2 R2 B2 U2 R2), 1qt edges will be FD (good) and RV (bad): +0+4+0(+3)
- (U2 B2 U' B2 U)
    - After (R2 B2 L2 B2), 1qt edges will be FV (bad) and RD (good): +0+3+1(+3)
- (U2 B2 U' F2 U)
    - After (B2 R2 F2 L2), 1qt edges will be FD (good) and RV (bad): +0+3+1(+3)
- (U2 B2 U' L2 B2 D')
    - After (L2), 1qt edges will be FD (good) and RH (good): +1+0+0(+0)
        - (L2 U R2 U) // no good
- (U2 B2 U' L2 F2 D')
    - After (L2 F2), 1qt edges will be FV (bad) and RH (good): +1+1+0(+3)
- (U2 B2 U' R2 B2 U')
    - After (B2), 1qt edges will be FH (bad) and RV (bad): +1+0+2(+5)
- (U2 F2 D' L2 F2 D')
    - After (R2), 1qt edges will be FV (bad) and RV (bad): +1+0+2(+5)
- (B2 U2 F2 D B2 U)
    - After (L2 B2), 1qt edges will be FH (bad) and RV (bad), fr=1: +1+1+1(+5)
- (U2 B2 U' L2 B2 D)
    - After (L2 U2 R2), 1qt edges will be FD (good) and RH (good), fr=1: +1+2+0(+3)
- (U2 F2 D' R2 B2 U')
    - After (F2 B2 L2), 1qt edges will be FV (bad) and RH (good): +1+2+0(+3)
- (U2 R2 B2 U R2 D')
    - After (F2 B2 R2), 1qt edges will be FH (bad) and RD (good): +1+2+0(+3)
- (F2 U2 F2 D F2 U)
    - After (R2 L2 B2), 1qt edges will be FV (bad) and RD (good), fr=1: +1+2+0(+5)
- (F2 U2 B2 U F2 U)
    - After (L2), 1qt edges will be FD (good) and RD (good): +1+0+3(+1)
- (U2 L2 F2 D L2 U')
    - After (B2), 1qt edges will be FD (good) and RV (bad): +1+0+3(+3)
- (U2 R2 F2 D R2 U')
    - After (F2), 1qt edges will be FD (good) and RV (bad): +1+0+3(+3)
- (F2 U2 F2 D B2 U)
    - After (L2), 1qt edges will be FD (good) and RD (good), fr=1: +1+0+3(+4)
- (U2 L2 B2 U R2 D')
    - After (L2 B2), 1qt edges will be FD (good) and RD (good): +1+1+2(+1)
- (U2 B2 U' R2 F2 U')
    - After (B2 L2), 1qt edges will be FH (bad) and RD (good): +1+1+2(+3)
- (B2 U2 F2 D F2 U)
    - After (B2 R2), 1qt edges will be FV (bad) and RD (good), fr=1: +1+1+2(+5)
- 14 more variants of this skeleton pass the meta, not reached before the stop.

Stop: 10 HTRs done, nothing within goal. This DR's optimal is 15, over the goal.

### 2c4, scramble 3

`R' U' F R2 F R2 B2 L2 F L2 B' L2 R2 D2 F2 U F R' D' B D2 B' F' R' U' F`

2c4 0e, goal 14.

Skeleton starting with B2 D F2 D' has FV corners, L=10, 4 spare moves.

- B2 D F2 D'
    - After R2, 1qt edges will be FD (bad) and RD (bad), fr=1: +0+0+0(+5)
    - After B2 R2 B2 R2 B2, 1qt edges will be FV (good) and RH (good), fr=1: +0+4+0(+1)
- F2 U F2 U'
    - After L2, 1qt edges will be FD (bad) and RD (bad), fr=1: +0+0+0(+5)
    - After F2 R2 B2 R2 F2, 1qt edges will be FV (good) and RH (good), fr=1: +0+4+0(+1)
- B2 D B2 D'
    - After R2 B2, 1qt edges will be FV (good) and RD (bad), fr=1: +0+1+0(+2)
        - R2 B2 U' B2 U' // 4 pairs, no good
    - After F2, 1qt edges will be FV (good) and RH (good), fr=1: +0+0+4(+1)
- F2 U B2 U'
    - After L2 B2, 1qt edges will be FV (good) and RD (bad), fr=1: +0+1+0(+2)
        - L2 B2 U' L2 U' // 3 pairs, no good
    - After F2, 1qt edges will be FV (good) and RH (good), fr=1: +0+0+4(+1)
- B2 D F2 D
    - After R2 U2 L2, 1qt edges will be FD (bad) and RD (bad): +0+2+0(+5)
    - After R2 F2 R2 U2 F2, 1qt edges will be FV (good) and RH (good), fr=1: +0+4+0(+1)
- F2 U F2 U
    - After L2 U2 L2, 1qt edges will be FD (bad) and RD (bad): +0+2+0(+5)
    - After L2 F2 L2 U2 B2, 1qt edges will be FV (good) and RH (good), fr=1: +0+4+0(+1)
- R2 F2 U' R2 U
    - After B2, 1qt edges will be FV (good) and RD (bad), fr=1: +1+0+0(+2)
        - B2 U' R2 U' // 5 pairs, no good
- L2 B2 D' R2 D'
    - After F2 U2 B2, 1qt edges will be FV (good) and RD (bad): +1+2+0(+3)
- L2 F2 U' L2 U'
    - After F2 U2 F2, 1qt edges will be FV (good) and RD (bad): +1+2+0(+3)
- R2 B2 D' L2 D'
    - After B2 U2 F2, 1qt edges will be FV (good) and RD (bad): +1+2+0(+3)
- R2 F2 U' R2 U'
    - After B2 U2 B2, 1qt edges will be FV (good) and RD (bad): +1+2+0(+3)
- 43 more variants of this skeleton pass the meta, not reached before the stop.

Check inverse. Skeleton starting with (U2 B2 D' R2 D) has FD corners.

- (U2 B2 D' R2 D)
    - After (F2), 1qt edges will be FV (bad) and RH (good), fr=1: +0+0+0(+5)
    - After (F2), 1qt edges will be FV (bad) and RH (good): +0+0+2(+3)
- (U2 F2 U' L2 U)
    - After (F2), 1qt edges will be FV (bad) and RH (good), fr=1: +0+0+0(+5)
    - After (F2), 1qt edges will be FV (bad) and RH (good): +0+0+2(+3)
- (U2 B2 D' L2 D)
    - After (F2 L2), 1qt edges will be FV (bad) and RV (bad), fr=1: +0+1+0(+5)
- (U2 F2 U' R2 U)
    - After (F2 R2), 1qt edges will be FV (bad) and RV (bad), fr=1: +0+1+0(+5)
- (U2 B2 D' R2 D')
    - After (F2 U2 B2), 1qt edges will be FV (bad) and RH (good): +0+2+0(+3)
- (U2 F2 U' L2 U')
    - After (F2 U2 F2), 1qt edges will be FV (bad) and RH (good): +0+2+0(+3)
- (U2 B2 D' L2 D')
    - After (F2 L2 U2 B2), 1qt edges will be FV (bad) and RD (good): +0+3+0(+3)
    - After (F2 B2 U2 R2), 1qt edges will be FH (bad) and RV (bad), fr=1: +0+3+0(+5)
    - After (F2 U2 B2 U2 L2), 1qt edges will be FV (bad) and RD (good): +0+4+0(+3)
- (U2 F2 U' R2 U')
    - After (F2 R2 U2 F2), 1qt edges will be FV (bad) and RD (good): +0+3+0(+3)
    - After (R2 U2 F2 R2), 1qt edges will be FV (bad) and RV (bad): +0+3+0(+5)
- (B2 U2 F2 U R2 U)
    - After (B2), 1qt edges will be FV (bad) and RH (good): +1+0+0(+3)
        - (B2 U' R2 U') // 2 pairs, no good
- (F2 U2 B2 D R2 D)
    - After (F2), 1qt edges will be FV (bad) and RH (good): +1+0+0(+3)
        - (F2 U' B2 U') // 3 pairs, no good
- (F2 U2 F2 U L2 U)
    - After (F2), 1qt edges will be FV (bad) and RH (good): +1+0+0(+3)
        - (F2 U' L2 U') // 4 pairs, no good
- (U2 L2 B2 D F2 D')
    - After (R2), 1qt edges will be FH (bad) and RH (good), fr=1: +1+0+0(+5)
    - After (R2), 1qt edges will be FH (bad) and RH (good): +1+0+2(+3)
- (U2 L2 F2 U F2 U')
    - After (L2), 1qt edges will be FH (bad) and RH (good), fr=1: +1+0+0(+5)
    - After (L2), 1qt edges will be FH (bad) and RH (good): +1+0+2(+3)
- (U2 R2 B2 D B2 D')
    - After (L2), 1qt edges will be FH (bad) and RH (good), fr=1: +1+0+0(+5)
    - After (L2), 1qt edges will be FH (bad) and RH (good): +1+0+2(+3)
- (U2 R2 F2 U B2 U')
    - After (R2), 1qt edges will be FH (bad) and RH (good), fr=1: +1+0+0(+5)
    - After (R2), 1qt edges will be FH (bad) and RH (good): +1+0+2(+3)
- (U2 B2 D' B2 R2 U')
    - After (B2), 1qt edges will be FV (bad) and RH (good), fr=1: +1+0+1(+5)
    - After (F2), 1qt edges will be FH (bad) and RD (good): +1+0+3(+3)
- (U2 F2 U' B2 L2 U')
    - After (L2), 1qt edges will be FV (bad) and RH (good), fr=1: +1+0+1(+5)
    - After (R2), 1qt edges will be FH (bad) and RD (good): +1+0+3(+3)
- (B2 U2 B2 D R2 D)
    - After (B2 R2), 1qt edges will be FV (bad) and RD (good): +1+1+0(+3)
- (B2 U2 F2 U L2 U)
    - After (B2 L2), 1qt edges will be FV (bad) and RD (good): +1+1+0(+3)
- (F2 U2 B2 D L2 D)
    - After (F2 L2), 1qt edges will be FV (bad) and RD (good): +1+1+0(+3)
- (F2 U2 F2 U R2 U)
    - After (F2 R2), 1qt edges will be FV (bad) and RD (good): +1+1+0(+3)
- (U2 L2 B2 D B2 D')
    - After (R2 B2), 1qt edges will be FV (bad) and RH (good), fr=1: +1+1+0(+5)
    - After (R2 B2), 1qt edges will be FV (bad) and RH (good): +1+1+2(+3)
- (U2 L2 F2 U B2 U')
    - After (L2 B2), 1qt edges will be FV (bad) and RH (good), fr=1: +1+1+0(+5)
    - After (L2 B2), 1qt edges will be FV (bad) and RH (good): +1+1+2(+3)
- (U2 R2 B2 D F2 D')
    - After (L2 F2), 1qt edges will be FV (bad) and RH (good), fr=1: +1+1+0(+5)
    - After (L2 F2), 1qt edges will be FV (bad) and RH (good): +1+1+2(+3)
- (U2 R2 F2 U F2 U')
    - After (R2 F2), 1qt edges will be FV (bad) and RH (good), fr=1: +1+1+0(+5)
    - After (R2 F2), 1qt edges will be FV (bad) and RH (good): +1+1+2(+3)
- (U2 L2 B2 D F2 D)
    - After (R2 U2 L2), 1qt edges will be FH (bad) and RH (good): +1+2+0(+3)
- (U2 L2 F2 U F2 U)
    - After (L2 U2 L2), 1qt edges will be FH (bad) and RH (good): +1+2+0(+3)
- (U2 R2 B2 D B2 D)
    - After (L2 U2 R2), 1qt edges will be FH (bad) and RH (good): +1+2+0(+3)
- (U2 R2 F2 U B2 U)
    - After (R2 U2 R2), 1qt edges will be FH (bad) and RH (good): +1+2+0(+3)
- (B2 U2 B2 D L2 D')
    - After (B2 U2 F2), 1qt edges will be FV (bad) and RH (good), fr=1: +1+2+0(+5)
- (B2 U2 F2 U R2 U')
    - After (B2 U2 B2), 1qt edges will be FV (bad) and RH (good), fr=1: +1+2+0(+5)
- (F2 U2 B2 D R2 D')
    - After (F2 U2 B2), 1qt edges will be FV (bad) and RH (good), fr=1: +1+2+0(+5)
- (F2 U2 F2 U L2 U')
    - After (F2 U2 F2), 1qt edges will be FV (bad) and RH (good), fr=1: +1+2+0(+5)
- 9 more variants of this skeleton pass the meta, not reached before the stop.

Skeleton starting with B2 D' F2 D has DD corners, L=11, 3 spare moves.

- B2 D' F2 D
    - After L2, 1qt edges will be FD (good) and RD (good): +0+0+0(+2)
        - L2 U' R2 U' // 4 pairs, no good
- F2 U' F2 U
    - After R2, 1qt edges will be FD (good) and RD (good): +0+0+0(+2)
        - R2 U' F2 U' // 4 pairs, no good
- B2 D' B2 D
    - After L2 B2, 1qt edges will be FV (good) and RD (good): +0+1+0(+0)
        - L2 B2 U B2 U // 4 pairs, no good
- B2 D' F2 D'
    - After L2 U2 R2, 1qt edges will be FD (good) and RD (good): +0+2+0(+2)
- F2 U' F2 U'
    - After R2 U2 R2, 1qt edges will be FD (good) and RD (good): +0+2+0(+2)
- B2 D' R2 F2 U'
    - After R2, 1qt edges will be FD (good) and RD (good): +1+0+1(+2)
- F2 U' L2 F2 U'
    - After F2, 1qt edges will be FD (good) and RD (good): +1+0+1(+2)
    - After B2, 1qt edges will be FH (bad) and RH (bad): +1+0+1(+5)
- L2 B2 D L2 D'
    - After B2 L2, 1qt edges will be FV (good) and RH (bad): +1+1+0(+3)
- L2 F2 U R2 U'
    - After B2 R2, 1qt edges will be FV (good) and RH (bad): +1+1+0(+3)
- R2 B2 D R2 D'
    - After F2 R2, 1qt edges will be FV (good) and RH (bad): +1+1+0(+3)
- R2 F2 U L2 U'
    - After F2 L2, 1qt edges will be FV (good) and RH (bad): +1+1+0(+3)
- 29 more variants of this skeleton pass the meta, not reached before the stop.

Check inverse. Skeleton starting with (L2 U2 B2 U L2 U') has FD corners.

- (L2 U2 B2 U L2 U')
    - After (B2), 1qt edges will be FV (bad) and RD (good): +0+0+0(+3)
        - (B2 U L2 U) // 4 pairs, no good
- (B2 U2 L2 U F2 U)
    - After (L2 F2), 1qt edges will be FV (bad) and RD (good), fr=1: +0+1+0(+5)
    - After (L2 F2), 1qt edges will be FV (bad) and RD (good): +0+1+2(+3)
- (B2 U2 R2 D B2 D)
    - After (L2 B2), 1qt edges will be FV (bad) and RD (good), fr=1: +0+1+0(+5)
    - After (L2 B2), 1qt edges will be FV (bad) and RD (good): +0+1+2(+3)
- (F2 U2 L2 D B2 D)
    - After (L2 B2), 1qt edges will be FV (bad) and RD (good), fr=1: +0+1+0(+5)
    - After (L2 B2), 1qt edges will be FV (bad) and RD (good): +0+1+2(+3)
- (F2 U2 R2 U F2 U)
    - After (L2 F2), 1qt edges will be FV (bad) and RD (good), fr=1: +0+1+0(+5)
    - After (L2 F2), 1qt edges will be FV (bad) and RD (good): +0+1+2(+3)
- (L2 U2 B2 U R2 U')
    - After (B2 R2), 1qt edges will be FV (bad) and RV (bad): +0+1+0(+5)
    - After (L2 B2 R2 F2), 1qt edges will be FH (bad) and RD (good): +0+3+0(+3)
- (L2 U2 F2 D L2 D')
    - After (B2 L2), 1qt edges will be FV (bad) and RV (bad): +0+1+0(+5)
    - After (R2 B2 L2 F2), 1qt edges will be FH (bad) and RD (good): +0+3+0(+3)
- (R2 U2 B2 D L2 D')
    - After (B2 L2), 1qt edges will be FV (bad) and RV (bad): +0+1+0(+5)
    - After (R2 B2 L2 F2), 1qt edges will be FH (bad) and RD (good): +0+3+0(+3)
- (R2 U2 F2 U R2 U')
    - After (B2 R2), 1qt edges will be FV (bad) and RV (bad): +0+1+0(+5)
    - After (L2 B2 R2 F2), 1qt edges will be FH (bad) and RD (good): +0+3+0(+3)
- (L2 U2 B2 U L2 U)
    - After (B2 U2 B2), 1qt edges will be FV (bad) and RD (good), fr=1: +0+2+0(+5)
- (L2 U2 F2 D R2 D)
    - After (B2 U2 F2), 1qt edges will be FV (bad) and RD (good), fr=1: +0+2+0(+5)
- (R2 U2 B2 D R2 D)
    - After (B2 U2 F2), 1qt edges will be FV (bad) and RD (good), fr=1: +0+2+0(+5)
- (R2 U2 F2 U L2 U)
    - After (B2 U2 B2), 1qt edges will be FV (bad) and RD (good), fr=1: +0+2+0(+5)
- (B2 U2 L2 U F2 U')
    - After (F2 U2 L2 F2), 1qt edges will be FV (bad) and RD (good): +0+3+0(+3)
    - After (R2 L2 U2 F2), 1qt edges will be FV (bad) and RV (bad), fr=1: +0+3+0(+5)
- (B2 U2 R2 D B2 D')
    - After (L2 B2 U2 R2), 1qt edges will be FH (bad) and RD (good): +0+3+0(+3)
- (F2 U2 L2 D B2 D')
    - After (B2 U2 R2 F2), 1qt edges will be FV (bad) and RD (good): +0+3+0(+3)
- (F2 U2 R2 U F2 U')
    - After (F2 U2 L2 F2), 1qt edges will be FV (bad) and RD (good): +0+3+0(+3)
- (L2 U2 B2 U R2 U)
    - After (F2 B2 U2 R2), 1qt edges will be FH (bad) and RV (bad): +0+3+0(+5)
- (L2 U2 F2 D L2 D)
    - After (L2 U2 F2 R2), 1qt edges will be FV (bad) and RV (bad), fr=1: +0+3+0(+5)
- (R2 U2 B2 D L2 D)
    - After (F2 B2 U2 R2), 1qt edges will be FH (bad) and RV (bad): +0+3+0(+5)
- (R2 U2 F2 U R2 U)
    - After (B2 R2 U2 B2), 1qt edges will be FV (bad) and RH (good), fr=1: +0+3+0(+5)
- (L2 U2 L2 B2 U' B2 U)
    - After (L2), 1qt edges will be FH (bad) and RD (good): +1+0+0(+3)
- (L2 U2 L2 F2 D' B2 D)
    - After (R2), 1qt edges will be FH (bad) and RD (good): +1+0+0(+3)
- (L2 U2 R2 B2 U' F2 U)
    - After (R2), 1qt edges will be FH (bad) and RD (good): +1+0+0(+3)
- (L2 U2 R2 F2 D' F2 D)
    - After (L2), 1qt edges will be FH (bad) and RD (good): +1+0+0(+3)
- (R2 U2 L2 B2 D' F2 D)
    - After (L2), 1qt edges will be FH (bad) and RD (good): +1+0+0(+3)
- (R2 U2 L2 F2 U' F2 U)
    - After (R2), 1qt edges will be FH (bad) and RD (good): +1+0+0(+3)
- (R2 U2 R2 B2 D' B2 D)
    - After (R2), 1qt edges will be FH (bad) and RD (good): +1+0+0(+3)
- (R2 U2 R2 F2 U' B2 U)
    - After (L2), 1qt edges will be FH (bad) and RD (good): +1+0+0(+3)
- (U2 B2 U2 L2 U' L2 U')
    - After (B2), 1qt edges will be FV (bad) and RD (good): +1+0+0(+3)
- (U2 B2 U2 R2 D' L2 D')
    - After (F2), 1qt edges will be FV (bad) and RD (good): +1+0+0(+3)
- (U2 F2 U2 L2 D' L2 D')
    - After (F2), 1qt edges will be FV (bad) and RD (good): +1+0+0(+3)
- (U2 F2 U2 R2 U' L2 U')
    - After (B2), 1qt edges will be FV (bad) and RD (good): +1+0+0(+3)
- (U2 L2 U2 B2 U' B2 U)
    - After (L2), 1qt edges will be FD (good) and RD (good), fr=1: +1+0+0(+4)
    - After (L2), 1qt edges will be FD (good) and RD (good): +1+0+2(+1)
- (U2 L2 U2 F2 D' B2 D)
    - After (R2), 1qt edges will be FD (good) and RD (good), fr=1: +1+0+0(+4)
    - After (R2), 1qt edges will be FD (good) and RD (good): +1+0+2(+1)
- (U2 R2 U2 B2 D' B2 D)
    - After (R2), 1qt edges will be FD (good) and RD (good), fr=1: +1+0+0(+4)
    - After (R2), 1qt edges will be FD (good) and RD (good): +1+0+2(+1)
- (U2 R2 U2 F2 U' B2 U)
    - After (L2), 1qt edges will be FD (good) and RD (good), fr=1: +1+0+0(+4)
    - After (L2), 1qt edges will be FD (good) and RD (good): +1+0+2(+1)
- (B2 U2 B2 L2 U' L2 U')
    - After (B2), 1qt edges will be FV (bad) and RV (bad), fr=1: +1+0+0(+5)
- (B2 U2 B2 R2 D' L2 D')
    - After (F2), 1qt edges will be FV (bad) and RV (bad), fr=1: +1+0+0(+5)
- (B2 U2 F2 L2 U' R2 U')
    - After (F2), 1qt edges will be FV (bad) and RV (bad), fr=1: +1+0+0(+5)
- (B2 U2 F2 R2 D' R2 D')
    - After (B2), 1qt edges will be FV (bad) and RV (bad), fr=1: +1+0+0(+5)
- (F2 U2 B2 L2 D' R2 D')
    - After (B2), 1qt edges will be FV (bad) and RV (bad), fr=1: +1+0+0(+5)
- (F2 U2 B2 R2 U' R2 U')
    - After (F2), 1qt edges will be FV (bad) and RV (bad), fr=1: +1+0+0(+5)
- (F2 U2 F2 L2 D' L2 D')
    - After (F2), 1qt edges will be FV (bad) and RV (bad), fr=1: +1+0+0(+5)
- (F2 U2 F2 R2 U' L2 U')
    - After (B2), 1qt edges will be FV (bad) and RV (bad), fr=1: +1+0+0(+5)
- (L2 B2 U2 B2 U' L2 U')
    - After (B2), 1qt edges will be FV (bad) and RD (good), fr=1: +1+0+0(+5)
    - After (B2), 1qt edges will be FV (bad) and RD (good): +1+0+2(+3)
- (L2 B2 U2 F2 D' R2 D')
    - After (B2), 1qt edges will be FV (bad) and RD (good), fr=1: +1+0+0(+5)
    - After (B2), 1qt edges will be FV (bad) and RD (good): +1+0+2(+3)
- (L2 F2 U2 B2 U' R2 U')
    - After (F2), 1qt edges will be FV (bad) and RD (good), fr=1: +1+0+0(+5)
    - After (F2), 1qt edges will be FV (bad) and RD (good): +1+0+2(+3)
- (L2 F2 U2 F2 D' L2 D')
    - After (F2), 1qt edges will be FV (bad) and RD (good), fr=1: +1+0+0(+5)
    - After (F2), 1qt edges will be FV (bad) and RD (good): +1+0+2(+3)
- (R2 B2 U2 B2 D' L2 D')
    - After (F2), 1qt edges will be FV (bad) and RD (good), fr=1: +1+0+0(+5)
    - After (F2), 1qt edges will be FV (bad) and RD (good): +1+0+2(+3)
- (R2 B2 U2 F2 U' R2 U')
    - After (F2), 1qt edges will be FV (bad) and RD (good), fr=1: +1+0+0(+5)
    - After (F2), 1qt edges will be FV (bad) and RD (good): +1+0+2(+3)
- (R2 F2 U2 B2 D' R2 D')
    - After (B2), 1qt edges will be FV (bad) and RD (good), fr=1: +1+0+0(+5)
    - After (B2), 1qt edges will be FV (bad) and RD (good): +1+0+2(+3)
- (R2 F2 U2 F2 U' L2 U')
    - After (B2), 1qt edges will be FV (bad) and RD (good), fr=1: +1+0+0(+5)
    - After (B2), 1qt edges will be FV (bad) and RD (good): +1+0+2(+3)
- (B2 U2 L2 U R2 F2 U')
    - After (L2), 1qt edges will be FD (good) and RH (good), fr=1: +1+0+1(+3)
- (B2 U2 R2 D R2 B2 U')
    - After (F2), 1qt edges will be FD (good) and RH (good), fr=1: +1+0+1(+3)
- (F2 U2 L2 D R2 B2 U')
    - After (F2), 1qt edges will be FD (good) and RH (good), fr=1: +1+0+1(+3)
- (F2 U2 R2 U R2 F2 U')
    - After (L2), 1qt edges will be FD (good) and RH (good), fr=1: +1+0+1(+3)
- (L2 U2 B2 U F2 L2 U)
    - After (R2), 1qt edges will be FH (bad) and RH (good): +1+0+1(+3)
- (L2 U2 F2 D F2 R2 U)
    - After (B2), 1qt edges will be FH (bad) and RH (good): +1+0+1(+3)
- (R2 U2 B2 D F2 R2 U)
    - After (B2), 1qt edges will be FH (bad) and RH (good): +1+0+1(+3)
- (R2 U2 F2 U F2 L2 U)
    - After (R2), 1qt edges will be FH (bad) and RH (good): +1+0+1(+3)
- (B2 U2 L2 U R2 B2 U')
    - After (B2), 1qt edges will be FD (good) and RD (good), fr=1: +1+0+1(+4)
- (B2 U2 R2 D R2 F2 U')
    - After (R2), 1qt edges will be FD (good) and RD (good), fr=1: +1+0+1(+4)
    - After (L2), 1qt edges will be FH (bad) and RV (bad), fr=1: +1+0+1(+5)
- (F2 U2 L2 D R2 F2 U')
    - After (R2), 1qt edges will be FD (good) and RD (good), fr=1: +1+0+1(+4)
    - After (L2), 1qt edges will be FH (bad) and RV (bad), fr=1: +1+0+1(+5)
- (F2 U2 R2 U R2 B2 U')
    - After (B2), 1qt edges will be FD (good) and RD (good), fr=1: +1+0+1(+4)
- (B2 L2 U2 L2 U' F2 U)
    - After (L2 F2), 1qt edges will be FH (bad) and RD (good): +1+1+0(+3)
- (B2 L2 U2 R2 D' B2 D)
    - After (L2 B2), 1qt edges will be FH (bad) and RD (good): +1+1+0(+3)
- (B2 R2 U2 L2 U' B2 U)
    - After (R2 B2), 1qt edges will be FH (bad) and RD (good): +1+1+0(+3)
- (B2 R2 U2 R2 D' F2 D)
    - After (R2 F2), 1qt edges will be FH (bad) and RD (good): +1+1+0(+3)
- (F2 L2 U2 L2 D' F2 D)
    - After (R2 F2), 1qt edges will be FH (bad) and RD (good): +1+1+0(+3)
- (F2 L2 U2 R2 U' B2 U)
    - After (R2 B2), 1qt edges will be FH (bad) and RD (good): +1+1+0(+3)
- (F2 R2 U2 L2 D' B2 D)
    - After (L2 B2), 1qt edges will be FH (bad) and RD (good): +1+1+0(+3)
- (F2 R2 U2 R2 U' F2 U)
    - After (L2 F2), 1qt edges will be FH (bad) and RD (good): +1+1+0(+3)
- (L2 U2 L2 B2 U' F2 U)
    - After (L2 F2), 1qt edges will be FV (bad) and RD (good): +1+1+0(+3)
- (L2 U2 L2 F2 D' F2 D)
    - After (R2 F2), 1qt edges will be FV (bad) and RD (good): +1+1+0(+3)
- (L2 U2 R2 B2 U' B2 U)
    - After (R2 B2), 1qt edges will be FV (bad) and RD (good): +1+1+0(+3)
- (L2 U2 R2 F2 D' B2 D)
    - After (L2 B2), 1qt edges will be FV (bad) and RD (good): +1+1+0(+3)
- (R2 U2 L2 B2 D' B2 D)
    - After (L2 B2), 1qt edges will be FV (bad) and RD (good): +1+1+0(+3)
- (R2 U2 L2 F2 U' B2 U)
    - After (R2 B2), 1qt edges will be FV (bad) and RD (good): +1+1+0(+3)
- (R2 U2 R2 B2 D' F2 D)
    - After (R2 F2), 1qt edges will be FV (bad) and RD (good): +1+1+0(+3)
- (R2 U2 R2 F2 U' F2 U)
    - After (L2 F2), 1qt edges will be FV (bad) and RD (good): +1+1+0(+3)
- (B2 U2 B2 L2 U' R2 U')
    - After (B2 R2), 1qt edges will be FV (bad) and RD (good), fr=1: +1+1+0(+5)
- (B2 U2 B2 R2 D' R2 D')
    - After (F2 R2), 1qt edges will be FV (bad) and RD (good), fr=1: +1+1+0(+5)
- (B2 U2 F2 L2 U' L2 U')
    - After (F2 L2), 1qt edges will be FV (bad) and RD (good), fr=1: +1+1+0(+5)
- (B2 U2 F2 R2 D' L2 D')
    - After (B2 L2), 1qt edges will be FV (bad) and RD (good), fr=1: +1+1+0(+5)
- (F2 U2 B2 L2 D' L2 D')
    - After (B2 L2), 1qt edges will be FV (bad) and RD (good), fr=1: +1+1+0(+5)
- (F2 U2 B2 R2 U' L2 U')
    - After (F2 L2), 1qt edges will be FV (bad) and RD (good), fr=1: +1+1+0(+5)
- (F2 U2 F2 L2 D' R2 D')
    - After (F2 R2), 1qt edges will be FV (bad) and RD (good), fr=1: +1+1+0(+5)
- (F2 U2 F2 R2 U' R2 U')
    - After (B2 R2), 1qt edges will be FV (bad) and RD (good), fr=1: +1+1+0(+5)
- (L2 B2 U2 B2 U' R2 U')
    - After (B2 R2), 1qt edges will be FV (bad) and RH (good), fr=1: +1+1+0(+5)
- (L2 B2 U2 F2 D' L2 D')
    - After (B2 L2), 1qt edges will be FV (bad) and RH (good), fr=1: +1+1+0(+5)
- (L2 F2 U2 B2 U' L2 U')
    - After (F2 L2), 1qt edges will be FV (bad) and RH (good), fr=1: +1+1+0(+5)
- (L2 F2 U2 F2 D' R2 D')
    - After (F2 R2), 1qt edges will be FV (bad) and RH (good), fr=1: +1+1+0(+5)
- (R2 B2 U2 B2 D' R2 D')
    - After (F2 R2), 1qt edges will be FV (bad) and RH (good), fr=1: +1+1+0(+5)
- (R2 B2 U2 F2 U' L2 U')
    - After (F2 L2), 1qt edges will be FV (bad) and RH (good), fr=1: +1+1+0(+5)
- (R2 F2 U2 B2 D' L2 D')
    - After (B2 L2), 1qt edges will be FV (bad) and RH (good), fr=1: +1+1+0(+5)
- (R2 F2 U2 F2 U' R2 U')
    - After (B2 R2), 1qt edges will be FV (bad) and RH (good), fr=1: +1+1+0(+5)
- (U2 B2 U2 L2 U' R2 U')
    - After (B2 R2), 1qt edges will be FV (bad) and RV (bad): +1+1+0(+5)
- (U2 B2 U2 R2 D' R2 D')
    - After (F2 R2), 1qt edges will be FV (bad) and RV (bad): +1+1+0(+5)
- (U2 F2 U2 L2 D' R2 D')
    - After (F2 R2), 1qt edges will be FV (bad) and RV (bad): +1+1+0(+5)
- (U2 F2 U2 R2 U' R2 U')
    - After (B2 R2), 1qt edges will be FV (bad) and RV (bad): +1+1+0(+5)
- (U2 L2 U2 B2 U' F2 U)
    - After (L2 F2), 1qt edges will be FV (bad) and RD (good), fr=1: +1+1+0(+5)
- (U2 L2 U2 F2 D' F2 D)
    - After (R2 F2), 1qt edges will be FV (bad) and RD (good), fr=1: +1+1+0(+5)
- (U2 R2 U2 B2 D' F2 D)
    - After (R2 F2), 1qt edges will be FV (bad) and RD (good), fr=1: +1+1+0(+5)
- (U2 R2 U2 F2 U' F2 U)
    - After (L2 F2), 1qt edges will be FV (bad) and RD (good), fr=1: +1+1+0(+5)
- 31 more variants of this skeleton pass the meta, not reached before the stop.

Stop: 10 HTRs done, nothing within goal. This DR's optimal is 14.

### 2c4, scramble 4

`R' U' F L U2 R L2 F' L B' D L F2 R2 U2 L' U2 L' B2 R' U2 L' B R' U' F`

2c4 2e, goal 14.

Skeleton starting with F2 U R2 U' has FV corners, L=10, 4 spare moves.

- F2 U R2 U'
    - After F2, 1qt edges will be FH (bad) and RD (bad): +0+0+3(+5)
- F2 U L2 U'
    - After B2 L2, 1qt edges will be FV (good) and RH (good): +0+1+2(+0)
        - B2 L2 U' B2 R2 L2 D' // no good
    - After R2 L2 B2 R2, 1qt edges will be FV (good) and RH (good): +0+3+0(+0)
        - R2 L2 B2 R2 U' F2 U' // no good
- F2 U L2 U
    - After R2 U2 F2 R2, 1qt edges will be FV (good) and RH (good), fr=1: +0+3+0(+1)
        - R2 U2 F2 R2 U L2 U // no good
- B2 D L2 U'
    - After L2 B2 R2 B2, 1qt edges will be FD (bad) and RH (good): +0+3+1(+3)
- B2 D R2 U'
    - After F2 R2 B2 L2, 1qt edges will be FV (good) and RD (bad): +0+3+1(+3)
- B2 D B2 L2 U
    - After B2, 1qt edges will be FH (bad) and RD (bad): +1+0+0(+5)
- B2 D B2 R2 U
    - After B2 L2, 1qt edges will be FH (bad) and RH (good): +1+1+0(+3)
    - After B2 L2, 1qt edges will be FH (bad) and RH (good), fr=1: +1+1+2(+2)
- R2 B2 D' B2 D
    - After R2 L2 F2, 1qt edges will be FD (bad) and RH (good): +1+2+0(+3)
- B2 D B2 L2 U'
    - After B2 U2 B2, 1qt edges will be FH (bad) and RD (bad), fr=1: +1+2+0(+5)
- F2 U B2 L2 U
    - After B2, 1qt edges will be FV (good) and RH (good), fr=1: +1+0+3(+1)
    - After F2, 1qt edges will be FD (bad) and RD (bad), fr=1: +1+0+3(+5)
- R2 F2 U' B2 U
    - After F2, 1qt edges will be FH (bad) and RH (good), fr=1: +1+0+3(+2)
- L2 F2 U' F2 U
    - After B2, 1qt edges will be FH (bad) and RH (good): +1+0+3(+3)
- B2 D F2 R2 D
    - After R2 B2, 1qt edges will be FD (bad) and RV (good): +1+1+2(+3)
- R2 F2 U' F2 U
    - After F2 R2, 1qt edges will be FH (bad) and RH (good): +1+1+2(+3)
- F2 U F2 L2 U
    - After R2 F2, 1qt edges will be FD (bad) and RD (bad): +1+1+2(+5)
- L2 B2 D' F2 D
    - After L2 B2, 1qt edges will be FH (bad) and RD (bad): +1+1+2(+5)
- 9 more variants of this skeleton pass the meta, not reached before the stop.

Check inverse. Skeleton starting with (U2 F2 D' L2 D') has FD corners.

- (U2 B2 U' L2 U')
    - After (F2 R2), 1qt edges will be FH (bad) and RH (good): +0+1+0(+3)
        - (F2 R2 U' L2 U L2 F2 L2 B2) // 14
    - After (F2 R2), 1qt edges will be FH (bad) and RH (good): +0+1+2(+3)
    - After (F2 R2), 1qt edges will be FH (bad) and RH (good), fr=1: +0+1+2(+5)
    - After (B2 R2 F2 L2 F2), 1qt edges will be FH (bad) and RD (good): +0+4+0(+3)
- (U2 F2 D' R2 U')
    - After (R2 B2), 1qt edges will be FV (bad) and RH (good): +0+1+1(+3)
- (U2 B2 U' R2 U)
    - After (B2 U2 F2), 1qt edges will be FV (bad) and RD (good), fr=1: +0+2+0(+5)
    - After (F2 B2 U2 F2), 1qt edges will be FV (bad) and RD (good): +0+3+0(+3)
    - After (F2 R2 B2 U2 L2), 1qt edges will be FD (good) and RV (bad): +0+4+0(+3)
- (U2 B2 U' L2 U)
    - After (F2 R2 U2 F2), 1qt edges will be FH (bad) and RV (bad), fr=1: +0+3+0(+5)
    - After (L2 U2 L2 F2 B2), 1qt edges will be FD (good) and RH (good), fr=1: +0+4+0(+3)
- (U2 F2 D' B2 L2 D)
    - After (L2), 1qt edges will be FV (bad) and RD (good): +1+0+0(+3)
        - (L2 U' F2 U') // 3 pairs, no good
- (U2 L2 B2 U B2 U)
    - After (B2), 1qt edges will be FD (good) and RV (bad): +1+0+0(+3)
        - (B2 U' B2 U) // 1 pair, no good
- (F2 U2 F2 D R2 D')
    - After (F2), 1qt edges will be FV (bad) and RH (good), fr=1: +1+0+0(+5)
    - After (F2), 1qt edges will be FV (bad) and RH (good): +1+0+2(+3)
- (U2 R2 F2 D F2 D)
    - After (L2 B2), 1qt edges will be FV (bad) and RH (good): +1+1+0(+3)
- (B2 U2 B2 U L2 U')
    - After (F2 R2), 1qt edges will be FH (bad) and RV (bad), fr=1: +1+1+0(+5)
- (F2 U2 F2 D L2 U')
    - After (L2 B2), 1qt edges will be FH (bad) and RD (good), fr=1: +1+1+1(+5)
- (B2 U2 B2 U R2 U)
    - After (B2 U2 F2), 1qt edges will be FV (bad) and RD (good): +1+2+0(+3)
- (F2 U2 F2 D R2 D)
    - After (B2 U2 B2), 1qt edges will be FV (bad) and RH (good): +1+2+0(+3)
- (B2 U2 F2 D L2 D)
    - After (B2 U2 F2), 1qt edges will be FV (bad) and RV (bad): +1+2+0(+5)
- (U2 F2 D' B2 L2 D')
    - After (R2 U2 R2), 1qt edges will be FV (bad) and RD (good), fr=1: +1+2+0(+5)
- (U2 F2 D' F2 R2 U')
    - After (R2 U2 R2), 1qt edges will be FV (bad) and RH (good), fr=1: +1+2+0(+5)
- (U2 L2 B2 U B2 U')
    - After (F2 U2 B2), 1qt edges will be FD (good) and RV (bad), fr=1: +1+2+0(+5)
- (B2 U2 F2 D R2 U')
    - After (F2), 1qt edges will be FD (good) and RV (bad), fr=1: +1+0+3(+5)
- (F2 U2 B2 U L2 U')
    - After (F2), 1qt edges will be FV (bad) and RD (good), fr=1: +1+0+3(+5)
- (U2 B2 U' F2 L2 U)
    - After (B2), 1qt edges will be FV (bad) and RD (good), fr=1: +1+0+3(+5)
- (U2 B2 U' F2 R2 U)
    - After (L2), 1qt edges will be FH (bad) and RD (good), fr=1: +1+0+3(+5)
- (U2 L2 F2 D B2 U)
    - After (L2), 1qt edges will be FV (bad) and RV (bad), fr=1: +1+0+3(+5)
- (U2 B2 U' F2 R2 U')
    - After (R2 U2 R2), 1qt edges will be FD (good) and RH (good), fr=1: +1+2+1(+3)
    - After (L2 U2 L2), 1qt edges will be FH (bad) and RD (good), fr=1: +1+2+1(+5)
- (U2 F2 D' B2 R2 U')
    - After (R2 U2 R2), 1qt edges will be FD (good) and RH (good), fr=1: +1+2+1(+3)
- (U2 L2 B2 U F2 U')
    - After (R2 U2 R2), 1qt edges will be FD (good) and RH (good), fr=1: +1+2+1(+3)
    - After (R2 U2 L2), 1qt edges will be FH (bad) and RD (good), fr=1: +1+2+1(+5)
- (U2 L2 F2 D B2 U')
    - After (R2 U2 R2), 1qt edges will be FD (good) and RH (good), fr=1: +1+2+1(+3)
- (U2 B2 U' F2 L2 U')
    - After (B2 U2 F2), 1qt edges will be FD (good) and RV (bad), fr=1: +1+2+1(+5)
- 12 more variants of this skeleton pass the meta, not reached before the stop.

Skeleton starting with B2 D' L2 U has RV corners, L=10, 4 spare moves.

- B2 D' L2 U
    - After L2, 1qt edges will be RH (bad) and FV (good): +0+0+3(+3)
    - After R2, 1qt edges will be RD (bad) and FH (good), fr=1: +0+0+4(+2)
- F2 U' L2 U
    - After R2 L2 F2 L2, 1qt edges will be RH (bad) and FH (good), fr=1: +0+3+0(+2)
- B2 D' R2 U
    - After R2 F2, 1qt edges will be RH (bad) and FH (good), fr=1: +0+1+3(+2)
- F2 U' R2 U
    - After F2 B2 R2 B2, 1qt edges will be RH (bad) and FH (good), fr=1: +0+3+1(+2)
- B2 D' L2 U'
    - After L2 U2 R2, 1qt edges will be RD (bad) and FH (good): +0+2+1(+3)
- F2 U' L2 U'
    - After F2 B2 U2 R2, 1qt edges will be RH (bad) and FD (bad), fr=1: +0+3+0(+5)
    - After R2 B2 L2 U2 B2, 1qt edges will be RD (bad) and FH (good), fr=1: +0+4+0(+2)
- L2 F2 U F2 U'
    - After R2 B2, 1qt edges will be RV (good) and FH (good), fr=1: +1+1+0(+1)
        - R2 B2 U' F2 U // no good
    - After R2 B2, 1qt edges will be RV (good) and FH (good): +1+1+2(+0)
        - R2 B2 U F2 U2 F2 U // 6 pairs, no good
        - R2 B2 U B2 U2 F2 U // 6 pairs, no good
- F2 U' B2 L2 U'
    - After L2 B2, 1qt edges will be RV (good) and FV (good), fr=1: +1+1+1(+2)
    - After R2 L2 F2, 1qt edges will be RV (good) and FH (good), fr=1: +1+2+1(+1)
- R2 F2 U B2 U'
    - After L2 B2, 1qt edges will be RD (bad) and FH (good), fr=1: +1+1+1(+2)
- R2 F2 U F2 U'
    - After F2 B2 R2, 1qt edges will be RD (bad) and FV (good), fr=1: +1+2+0(+2)
- L2 F2 U B2 U
    - After L2 U2 R2, 1qt edges will be RD (bad) and FV (good): +1+2+0(+3)
- F2 U' F2 R2 U'
    - After L2, 1qt edges will be RV (good) and FV (good): +1+0+3(+1)
    - After R2, 1qt edges will be RD (bad) and FH (good): +1+0+3(+3)
- L2 B2 D B2 U'
    - After F2, 1qt edges will be RD (bad) and FV (good), fr=1: +1+0+3(+2)
- R2 B2 D F2 D'
    - After L2, 1qt edges will be RD (bad) and FV (good), fr=1: +1+0+3(+2)
- B2 D' B2 R2 U'
    - After L2, 1qt edges will be RD (bad) and FH (good): +1+0+3(+3)
- B2 D' F2 R2 U'
    - After R2, 1qt edges will be RH (bad) and FV (good): +1+0+3(+3)
- F2 U' B2 R2 D'
    - After R2 F2, 1qt edges will be RD (bad) and FH (good), fr=1: +1+1+2(+2)
- F2 U' F2 L2 U'
    - After L2 B2, 1qt edges will be RV (good) and FV (good), fr=1: +1+1+2(+2)
- L2 B2 D F2 D'
    - After R2 F2, 1qt edges will be RH (bad) and FH (good), fr=1: +1+1+2(+2)
- B2 D' F2 R2 U
    - After L2 U2 R2, 1qt edges will be RH (bad) and FV (good): +1+2+1(+3)

Check inverse. Skeleton starting with (U2 L2 U' F2 U') has FD corners.

- (U2 L2 U' F2 U')
    - After (R2), 1qt edges will be FD (good) and RH (good), fr=1: +0+0+0(+3)
        - (R2 U R2 U) // no good
- (U2 R2 D' B2 D')
    - After (R2 U2 R2 L2), 1qt edges will be FH (bad) and RH (good), fr=1: +0+3+0(+5)
- (U2 R2 D' F2 D')
    - After (L2 B2), 1qt edges will be FV (bad) and RD (good), fr=1: +0+1+0(+5)
    - After (L2 B2), 1qt edges will be FV (bad) and RD (good): +0+1+2(+3)
- (U2 L2 U' B2 U')
    - After (L2 F2), 1qt edges will be FH (bad) and RD (good), fr=1: +0+1+1(+5)
    - After (L2 F2), 1qt edges will be FH (bad) and RD (good): +0+1+3(+3)
- (U2 F2 R2 D R2 D)
    - After (R2), 1qt edges will be FD (good) and RV (bad), fr=1: +1+0+0(+5)
    - After (R2), 1qt edges will be FD (good) and RV (bad): +1+0+2(+3)
- (U2 L2 U' R2 F2 U)
    - After (F2), 1qt edges will be FH (bad) and RH (good), fr=1: +1+0+0(+5)
    - After (F2), 1qt edges will be FH (bad) and RH (good): +1+0+2(+3)
- (U2 B2 L2 U R2 U)
    - After (B2), 1qt edges will be FV (bad) and RV (bad), fr=1: +1+0+1(+5)
- (U2 L2 U' L2 F2 U)
    - After (F2), 1qt edges will be FH (bad) and RV (bad), fr=1: +1+0+1(+5)
- (U2 B2 L2 U L2 U)
    - After (F2 R2), 1qt edges will be FV (bad) and RH (good), fr=1: +1+1+0(+5)
    - After (L2 F2 B2), 1qt edges will be FD (good) and RH (good), fr=1: +1+2+0(+3)
    - After (F2 R2), 1qt edges will be FV (bad) and RH (good): +1+1+2(+3)
- (L2 U2 L2 U F2 U)
    - After (R2 U2 R2), 1qt edges will be FD (good) and RH (good), fr=1: +1+2+0(+3)
- (U2 F2 R2 D R2 D')
    - After (L2 U2 L2), 1qt edges will be FD (good) and RV (bad): +1+2+0(+3)
- (U2 L2 U' L2 B2 D')
    - After (B2 U2 F2), 1qt edges will be FV (bad) and RH (good): +1+2+0(+3)
- (U2 L2 U' R2 F2 U')
    - After (B2 U2 F2), 1qt edges will be FH (bad) and RH (good): +1+2+0(+3)
- (L2 U2 R2 D B2 D)
    - After (R2 U2 R2), 1qt edges will be FH (bad) and RH (good), fr=1: +1+2+0(+5)
- (R2 U2 L2 U B2 U)
    - After (R2 U2 L2), 1qt edges will be FV (bad) and RH (good), fr=1: +1+2+0(+5)
- (L2 U2 L2 U B2 U')
    - After (F2), 1qt edges will be FD (good) and RV (bad): +1+0+3(+3)
- (R2 U2 R2 D F2 D')
    - After (L2), 1qt edges will be FH (bad) and RH (good): +1+0+3(+3)
- (U2 R2 D' L2 B2 U)
    - After (L2), 1qt edges will be FH (bad) and RD (good): +1+0+3(+3)
- (U2 R2 D' L2 F2 U)
    - After (F2), 1qt edges will be FH (bad) and RH (good): +1+0+3(+3)
- (U2 F2 R2 D L2 U')
    - After (L2 U2 L2), 1qt edges will be FH (bad) and RD (good): +1+2+1(+3)
    - After (L2 U2 R2), 1qt edges will be FV (bad) and RV (bad): +1+2+1(+5)
- (U2 L2 U' R2 B2 U')
    - After (L2 U2 L2), 1qt edges will be FH (bad) and RD (good): +1+2+1(+3)
- (U2 R2 D' L2 B2 U')
    - After (R2 U2 L2), 1qt edges will be FH (bad) and RD (good): +1+2+1(+3)
- (U2 R2 D' L2 F2 U')
    - After (F2 U2 F2), 1qt edges will be FH (bad) and RH (good): +1+2+1(+3)
- 17 more variants of this skeleton pass the meta, not reached before the stop.

Stop: 10 HTRs done, one finish within goal (14). This DR's optimal is 14.

### 2c4, scramble 5

`R' U' F U2 D2 R D F L2 U2 F D' L B2 R' D2 B2 R D2 L' F2 L B2 R' U' F`

2c4 6e, goal 14.

Skeleton starting with F2 U' L2 D has RV corners, L=10, 4 spare moves.

- F2 U' L2 D
    - After F2 R2, 1qt edges will be RV (good) and FD (bad): +0+1+0(+3)
        - F2 R2 U L2 U' // no good
    - After L2, 1qt edges will be RV (good) and FV (good): +0+0+4(+1)
- B2 D' R2 U
    - After R2, 1qt edges will be RV (good) and FH (good): +0+0+3(+0)
        - R2 U' L2 B2 R2 L2 U' // 4 pairs, no good
- F2 U' R2 U
    - After R2, 1qt edges will be RH (bad) and FH (good), fr=1: +0+0+3(+2)
- B2 D' L2 U
    - After B2, 1qt edges will be RH (bad) and FV (good): +0+0+3(+3)
    - After F2 R2 B2 L2, 1qt edges will be RV (good) and FV (good): +0+3+1(+1)
- F2 U' R2 U'
    - After R2 U2 L2, 1qt edges will be RV (good) and FD (bad), fr=1: +0+2+1(+2)
- F2 U' L2 D'
    - After R2 U2 B2 L2, 1qt edges will be RV (good) and FD (bad), fr=1: +0+3+0(+2)
- B2 D' F2 L2 D'
    - After B2, 1qt edges will be RV (good) and FD (bad): +1+0+0(+3)
        - B2 U F2 U' // no good
    - After B2, 1qt edges will be RV (good) and FD (bad), fr=1: +1+0+2(+2)
- F2 U' B2 L2 D'
    - After R2 F2, 1qt edges will be RH (bad) and FV (good): +1+1+0(+3)
    - After R2 F2, 1qt edges will be RH (bad) and FV (good), fr=1: +1+1+2(+2)
- L2 B2 D B2 U'
    - After F2 R2, 1qt edges will be RD (bad) and FV (good): +1+1+0(+3)
    - After F2 R2, 1qt edges will be RD (bad) and FV (good), fr=1: +1+1+2(+2)
- R2 B2 D B2 U'
    - After R2 B2, 1qt edges will be RD (bad) and FH (good): +1+1+0(+3)
    - After R2 B2, 1qt edges will be RD (bad) and FH (good), fr=1: +1+1+2(+2)
- B2 D' F2 R2 D'
    - After B2 L2, 1qt edges will be RD (bad) and FD (bad): +1+1+0(+5)
- R2 F2 U B2 D'
    - After R2 F2, 1qt edges will be RD (bad) and FD (bad): +1+1+0(+5)
- B2 D' B2 L2 U'
    - After R2, 1qt edges will be RH (bad) and FV (good): +1+0+2(+3)
- F2 U' B2 R2 U'
    - After R2 B2, 1qt edges will be RH (bad) and FV (good): +1+1+1(+3)
- L2 B2 D F2 U'
    - After R2 F2, 1qt edges will be RD (bad) and FV (good): +1+1+1(+3)
- B2 D' F2 L2 D
    - After B2 U2 F2, 1qt edges will be RV (good) and FD (bad), fr=1: +1+2+0(+2)
- F2 U' F2 R2 U
    - After F2 U2 F2, 1qt edges will be RD (bad) and FD (bad), fr=1: +1+2+0(+5)
- R2 B2 D F2 U
    - After L2 U2 R2, 1qt edges will be RH (bad) and FD (bad), fr=1: +1+2+0(+5)
- R2 F2 U F2 U'
    - After F2, 1qt edges will be RH (bad) and FH (good), fr=1: +1+0+3(+2)
- F2 U' F2 L2 U'
    - After L2, 1qt edges will be RD (bad) and FH (good): +1+0+3(+3)
- L2 F2 U B2 D'
    - After R2, 1qt edges will be RD (bad) and FD (bad): +1+0+3(+5)
- B2 D' B2 R2 U'
    - After R2 B2, 1qt edges will be RH (bad) and FH (good): +1+1+2(+3)
- R2 F2 U F2 U
    - After F2 U2 F2, 1qt edges will be RH (bad) and FH (good), fr=1: +1+2+1(+2)
- 7 more variants of this skeleton pass the meta, not reached before the stop.

Check inverse. Skeleton starting with (U2 R2 D B2 U') has FD corners.

- (U2 R2 D B2 U')
    - After (R2 B2), 1qt edges will be FH (bad) and RV (bad): +0+1+1(+5)
    - After (R2 L2 F2), 1qt edges will be FH (bad) and RH (good): +0+2+1(+3)
    - After (R2 B2 R2 L2), 1qt edges will be FV (bad) and RH (good): +0+3+1(+3)
- (U2 L2 U B2 D')
    - After (R2), 1qt edges will be FD (good) and RH (good): +0+0+3(+0)
        - (R2 U L2 F2 L2 F2 U') // 12 pairs, no good
        - (R2 U L2 F2 R2 B2 D') // 6 pairs, no good
        - (R2 U L2 B2 R2 F2 D') // 6 pairs, no good
- (U2 L2 U F2 U')
    - After (F2 R2), 1qt edges will be FV (bad) and RH (good), fr=1: +0+1+3(+5)
- (U2 R2 D F2 U)
    - After (R2 U2 F2 R2), 1qt edges will be FV (bad) and RH (good), fr=1: +0+3+0(+5)
    - After (L2 U2 R2 F2 B2), 1qt edges will be FD (good) and RH (good), fr=1: +0+4+0(+3)
- (U2 L2 U F2 U)
    - After (R2 U2 B2 L2), 1qt edges will be FV (bad) and RH (good), fr=1: +0+3+1(+5)
- (U2 R2 D B2 U)
    - After (L2 F2 U2 R2), 1qt edges will be FH (bad) and RH (good), fr=1: +0+3+1(+5)
- (R2 U2 L2 U' B2 D')
    - After (L2 B2), 1qt edges will be FH (bad) and RD (good), fr=1: +1+1+0(+5)
    - After (L2 B2), 1qt edges will be FH (bad) and RD (good): +1+1+2(+3)
- (L2 U2 R2 D' F2 U')
    - After (R2), 1qt edges will be FD (good) and RV (bad), fr=1: +1+0+2(+5)
- (R2 U2 R2 D' F2 U')
    - After (L2 F2), 1qt edges will be FH (bad) and RV (bad), fr=1: +1+1+1(+5)
- (U2 B2 R2 D' L2 U)
    - After (B2), 1qt edges will be FD (good) and RD (good): +1+0+3(+1)
    - After (F2), 1qt edges will be FV (bad) and RH (good): +1+0+3(+3)
- (U2 B2 R2 D' R2 U)
    - After (L2), 1qt edges will be FD (good) and RV (bad): +1+0+3(+3)
- (U2 R2 D L2 B2 U)
    - After (L2), 1qt edges will be FV (bad) and RD (good): +1+0+3(+3)
- (L2 U2 L2 U' B2 D')
    - After (L2), 1qt edges will be FD (good) and RD (good), fr=1: +1+0+3(+4)
- (U2 F2 L2 U' L2 U)
    - After (B2), 1qt edges will be FV (bad) and RH (good), fr=1: +1+0+3(+5)
- (U2 L2 U L2 B2 D)
    - After (L2 F2), 1qt edges will be FH (bad) and RD (good): +1+1+2(+3)
- (U2 L2 U L2 F2 U)
    - After (R2 F2), 1qt edges will be FV (bad) and RH (good): +1+1+2(+3)
- (U2 L2 U R2 B2 D)
    - After (R2 B2), 1qt edges will be FH (bad) and RD (good): +1+1+2(+3)
- (U2 L2 U R2 F2 U)
    - After (L2 B2), 1qt edges will be FV (bad) and RH (good): +1+1+2(+3)
- (R2 U2 R2 D' B2 U')
    - After (F2 R2), 1qt edges will be FV (bad) and RD (good), fr=1: +1+1+2(+5)
- (U2 F2 R2 D' R2 U)
    - After (L2 B2), 1qt edges will be FV (bad) and RV (bad): +1+1+2(+5)
- (U2 R2 D L2 F2 U)
    - After (R2 F2), 1qt edges will be FH (bad) and RV (bad): +1+1+2(+5)
- 14 more variants of this skeleton pass the meta, not reached before the stop.

Skeleton starting with F2 U R2 U' has DD corners, L=11, 3 spare moves.

- F2 U R2 U'
    - After L2, 1qt edges will be FD (good) and RV (good): +0+0+1(+0)
        - L2 U R2 B2 D' // 2 pairs, no good
        - L2 U L2 F2 U // 2 pairs, no good
- F2 U L2 D
    - After R2 U2 L2, 1qt edges will be FV (good) and RD (good): +0+2+0(+0)
        - R2 U2 L2 U' F2 U // no good
- R2 F2 U' F2 U
    - After B2, 1qt edges will be FD (good) and RD (good): +1+0+1(+2)
- L2 B2 D' B2 U
    - After F2 R2, 1qt edges will be FD (good) and RD (good): +1+1+0(+2)
- 14 more variants of this skeleton pass the meta, not reached before the stop.

Check inverse. Skeleton starting with (L2 U2 B2 U' L2 D') has FD corners.

- (L2 U2 B2 U' L2 D')
    - After (B2), 1qt edges will be FH (bad) and RH (good): +0+0+2(+3)
- (B2 U2 L2 U' B2 U)
    - After (F2), 1qt edges will be FD (good) and RH (good), fr=1: +0+0+3(+3)
- (L2 U2 F2 D' R2 U')
    - After (B2), 1qt edges will be FV (bad) and RH (good): +0+0+3(+3)
- (R2 U2 B2 D' R2 U')
    - After (F2), 1qt edges will be FV (bad) and RH (good): +0+0+3(+3)
- (R2 U2 F2 U' L2 D')
    - After (R2 F2), 1qt edges will be FV (bad) and RD (good): +0+1+0(+3)
- (F2 U2 R2 U' B2 D)
    - After (F2 R2), 1qt edges will be FV (bad) and RH (good), fr=1: +0+1+0(+5)
    - After (F2 R2), 1qt edges will be FV (bad) and RH (good): +0+1+2(+3)
- (R2 U2 F2 U' R2 U')
    - After (R2 F2), 1qt edges will be FD (good) and RH (good): +0+1+1(+0)
        - (R2 F2 U' L2 B2 D) // 6 pairs, no good
    - After (R2 B2), 1qt edges will be FV (bad) and RD (good): +0+1+1(+3)
- (F2 U2 R2 U' F2 U)
    - After (F2 L2), 1qt edges will be FV (bad) and RH (good), fr=1: +0+1+1(+5)
- (B2 U2 R2 D' F2 U)
    - After (L2 F2 B2), 1qt edges will be FD (good) and RH (good), fr=1: +0+2+0(+3)
- (B2 U2 L2 U' F2 D)
    - After (R2 L2 B2), 1qt edges will be FV (bad) and RH (good), fr=1: +0+2+0(+5)
    - After (B2 L2 F2 L2), 1qt edges will be FD (good) and RH (good), fr=1: +0+3+0(+3)
- (B2 U2 R2 D' B2 U)
    - After (R2 L2 B2), 1qt edges will be FV (bad) and RD (good), fr=1: +0+2+0(+5)
    - After (B2 R2 B2 R2), 1qt edges will be FD (good) and RD (good), fr=1: +0+3+0(+4)
- (B2 U2 R2 D' F2 U')
    - After (L2 U2 B2 L2), 1qt edges will be FH (bad) and RH (good): +0+3+0(+3)
- (F2 U2 R2 U' B2 D')
    - After (R2 U2 B2 L2), 1qt edges will be FV (bad) and RH (good): +0+3+0(+3)
    - After (B2 L2 U2 B2), 1qt edges will be FV (bad) and RV (bad): +0+3+0(+5)
- (R2 U2 F2 U' L2 D)
    - After (L2 B2 U2 L2), 1qt edges will be FD (good) and RD (good), fr=1: +0+3+0(+4)
    - After (F2 U2 L2 B2), 1qt edges will be FV (bad) and RD (good), fr=1: +0+3+0(+5)
- (B2 U2 R2 D' B2 U')
    - After (R2 B2 U2 L2), 1qt edges will be FH (bad) and RV (bad): +0+3+0(+5)
- (R2 U2 B2 D' F2 R2 D)
    - After (B2), 1qt edges will be FV (bad) and RH (good): +1+0+0(+3)
- (R2 U2 F2 U' F2 L2 U)
    - After (B2), 1qt edges will be FH (bad) and RH (good): +1+0+1(+3)
- (F2 U2 R2 U' R2 B2 U')
    - After (L2), 1qt edges will be FD (good) and RD (good), fr=1: +1+0+1(+4)
- (F2 L2 U2 R2 U B2 D)
    - After (L2 F2), 1qt edges will be FD (good) and RV (bad): +1+1+0(+3)
- (R2 B2 U2 F2 U L2 D')
    - After (B2 R2), 1qt edges will be FD (good) and RH (good), fr=1: +1+1+0(+3)
- (R2 U2 B2 D' F2 L2 D)
    - After (B2 R2), 1qt edges will be FV (bad) and RD (good): +1+1+0(+3)
- (R2 U2 F2 U' F2 R2 U)
    - After (F2 R2), 1qt edges will be FH (bad) and RD (good): +1+1+0(+3)
- (R2 U2 R2 F2 U B2 D)
    - After (F2 R2), 1qt edges will be FV (bad) and RD (good): +1+1+0(+3)
- (U2 F2 U2 R2 U L2 D')
    - After (R2 F2), 1qt edges will be FV (bad) and RD (good): +1+1+0(+3)
- (R2 F2 U2 F2 U L2 D')
    - After (R2 F2), 1qt edges will be FD (good) and RD (good), fr=1: +1+1+0(+4)
- (F2 R2 U2 R2 U B2 D)
    - After (F2 R2), 1qt edges will be FV (bad) and RV (bad): +1+1+0(+5)
- (F2 U2 B2 L2 D L2 U')
    - After (F2 R2), 1qt edges will be FV (bad) and RH (good), fr=1: +1+1+0(+5)
- (F2 U2 B2 R2 U L2 D')
    - After (F2 L2), 1qt edges will be FV (bad) and RV (bad), fr=1: +1+1+0(+5)
- (F2 U2 F2 R2 U L2 D')
    - After (R2 F2), 1qt edges will be FV (bad) and RD (good), fr=1: +1+1+0(+5)
- (F2 U2 R2 U' L2 B2 D')
    - After (R2 F2), 1qt edges will be FD (good) and RV (bad), fr=1: +1+1+0(+5)
- (F2 U2 R2 U' R2 F2 U')
    - After (R2 F2), 1qt edges will be FV (bad) and RD (good), fr=1: +1+1+0(+5)
- (L2 F2 U2 F2 D R2 U')
    - After (F2 R2), 1qt edges will be FD (good) and RV (bad), fr=1: +1+1+0(+5)
- (U2 R2 U2 F2 U B2 D)
    - After (F2 R2), 1qt edges will be FV (bad) and RH (good), fr=1: +1+1+0(+5)
- (B2 L2 U2 L2 U F2 D)
    - After (F2), 1qt edges will be FV (bad) and RH (good): +1+0+2(+3)
- (B2 U2 B2 L2 U L2 D')
    - After (B2), 1qt edges will be FD (good) and RH (good), fr=1: +1+0+2(+3)
- (L2 U2 B2 U' B2 L2 D)
    - After (L2), 1qt edges will be FV (bad) and RH (good): +1+0+2(+3)
- (U2 B2 U2 L2 U L2 D')
    - After (B2), 1qt edges will be FH (bad) and RH (good): +1+0+2(+3)
- (B2 U2 L2 U' L2 B2 U')
    - After (R2), 1qt edges will be FH (bad) and RD (good), fr=1: +1+0+2(+5)
- (L2 F2 U2 B2 U R2 D')
    - After (F2), 1qt edges will be FH (bad) and RH (good), fr=1: +1+0+2(+5)
- (L2 U2 R2 F2 D B2 U)
    - After (B2), 1qt edges will be FV (bad) and RV (bad): +1+0+2(+5)
- (R2 U2 B2 D' B2 R2 U)
    - After (L2), 1qt edges will be FH (bad) and RV (bad): +1+0+2(+5)
- (R2 U2 R2 F2 U F2 U)
    - After (F2 L2), 1qt edges will be FV (bad) and RD (good): +1+1+1(+3)
- (R2 F2 U2 F2 U R2 U')
    - After (R2 B2), 1qt edges will be FD (good) and RD (good), fr=1: +1+1+1(+4)
- (B2 U2 F2 R2 D L2 U')
    - After (B2 L2), 1qt edges will be FD (good) and RV (bad), fr=1: +1+1+1(+5)
- (B2 U2 L2 U' R2 B2 U')
    - After (B2 L2), 1qt edges will be FD (good) and RV (bad), fr=1: +1+1+1(+5)
- (F2 U2 F2 R2 U R2 U')
    - After (R2 B2), 1qt edges will be FV (bad) and RD (good), fr=1: +1+1+1(+5)
- (L2 B2 U2 B2 U R2 U')
    - After (L2 B2), 1qt edges will be FH (bad) and RV (bad), fr=1: +1+1+1(+5)
- (U2 R2 U2 F2 U F2 U)
    - After (F2 R2), 1qt edges will be FD (good) and RV (bad), fr=1: +1+1+1(+5)
- 11 more variants of this skeleton pass the meta, not reached before the stop.

Stop: 10 HTRs done, nothing within goal. This DR's optimal is 14.

### 2c4, scramble 6

`R' U' F R D2 L B' R' D L' R2 U2 B2 D2 F2 D R2 U' L2 D2 B' U2 F R' U' F`

2c4 4e, goal 14.

Skeleton starting with D B2 U' has FV corners, L=9, 5 spare moves.

- D B2 U'
    - After B2 R2, 1qt edges will be FD (bad) and RV (good): +0+1+1(+3)
        - B2 R2 U' R2 F2 D // 4 pairs, no good
        - B2 R2 U' L2 B2 U' // 2 pairs, no good
    - After B2 R2, 1qt edges will be FD (bad) and RV (good), fr=1: +0+1+4(+2)
- D B2 U
    - After F2 L2 U2 B2, 1qt edges will be FH (bad) and RV (good), fr=1: +0+3+1(+2)
    - After F2 B2 U2 R2, 1qt edges will be FH (bad) and RV (good): +0+3+1(+3)
    - After F2 R2 U2 R2 B2, 1qt edges will be FD (bad) and RV (good), fr=1: +0+4+1(+2)
- D F2 D
    - After R2 U2 F2 L2, 1qt edges will be FH (bad) and RH (good), fr=1: +0+3+0(+2)
        - R2 U2 F2 L2 U F2 U // no good
    - After B2 U2 R2 U2 L2 B2, 1qt edges will be FV (good) and RV (good): +0+5+0(+1)
- D L2 F2 D
    - After R2 L2 F2, 1qt edges will be FD (bad) and RD (bad): +1+2+0(+5)
- D L2 B2 U
    - After B2, 1qt edges will be FH (bad) and RD (bad): +1+0+3(+5)
- D L2 F2 D'
    - After F2 U2 F2, 1qt edges will be FD (bad) and RD (bad), fr=1: +1+2+2(+5)
- 23 more variants of this skeleton pass the meta, not reached before the stop.

Check inverse. Skeleton starting with (U2 F2 D' L2 D) has HH corners. Apply D and NISS: FD corners.

- (U2 B2 D')
    - After (B2), 1qt edges will be FH (bad) and RH (good): +0+0+2(+3)
        - (B2 U F2 R2 L2 D' R2 F2 L2 F2 D') // 14
    - After (B2), 1qt edges will be FH (bad) and RH (good): +0+0+3(+3)
- (U2 F2 U')
    - After (R2 B2), 1qt edges will be FD (good) and RD (good): +0+1+3(+1)
        - (R2 B2 U' L2 F2 R2 L2 D') // 4 pairs, no good
    - After (R2 F2), 1qt edges will be FH (bad) and RV (bad): +0+1+3(+5)
    - After (L2 B2 U2 F2 B2), 1qt edges will be FD (good) and RD (good): +0+4+1(+1)
- (U2 F2 U)
    - After (F2 B2 U2 L2 F2), 1qt edges will be FD (good) and RD (good): +0+4+1(+1)
- (F2 U2 B2 D)
    - After (B2), 1qt edges will be FD (good) and RH (good), fr=1: +1+0+2(+2)
        - (B2 U F2 R2 L2 D) // no good
- (U2 R2 B2 U)
    - After (L2 F2), 1qt edges will be FV (bad) and RV (bad): +1+1+1(+5)
    - After (F2 B2 R2 B2), 1qt edges will be FD (good) and RD (good): +1+3+1(+1)
- (B2 U2 B2 D)
    - After (R2 L2 B2), 1qt edges will be FH (bad) and RH (good), fr=1: +1+2+0(+3)
- (U2 R2 F2 U)
    - After (F2 B2 R2), 1qt edges will be FH (bad) and RV (bad): +1+2+0(+5)
    - After (R2 F2 L2 F2), 1qt edges will be FH (bad) and RH (good): +1+3+0(+3)
    - After (R2 U2 B2 R2 F2), 1qt edges will be FH (bad) and RD (good): +1+4+0(+3)
- (F2 U2 F2 U)
    - After (B2), 1qt edges will be FV (bad) and RH (good), fr=1: +1+0+3(+3)
- (B2 U2 F2 U)
    - After (F2 B2 L2 F2), 1qt edges will be FD (good) and RV (bad), fr=1: +1+3+1(+5)
- (B2 U2 B2 D')
    - After (B2 U2 B2), 1qt edges will be FH (bad) and RH (good): +1+2+2(+3)
- (U2 R2 F2 U')
    - After (L2 B2 L2 U2 B2), 1qt edges will be FV (bad) and RH (good): +1+4+0(+3)
    - After (L2 U2 F2 B2 R2), 1qt edges will be FH (bad) and RV (bad), fr=1: +1+4+0(+5)
- (U2 R2 B2 U')
    - After (R2 L2 U2 F2), 1qt edges will be FV (bad) and RD (good): +1+3+1(+3)
    - After (L2 F2 U2 L2), 1qt edges will be FD (good) and RV (bad), fr=1: +1+3+1(+5)
- 16 more variants of this skeleton pass the meta, not reached before the stop.

The same skeleton in full, for the solutions that go on after its last quarter turn.

- (U2 F2 D' R2 U)
    - After (F2), 1qt edges will be RD (bad) and FH (good): +0+0+3(+3)
- (U2 B2 U' R2 U)
    - After (R2 B2), 1qt edges will be RV (bad) and FV (bad): +0+1+0(+6)
    - After (F2 R2 L2), 1qt edges will be RH (good) and FV (bad): +0+2+0(+3)
        - (F2 R2 L2 U' L2 U) // no good
- (U2 F2 D' L2 D)
    - After (L2 B2), 1qt edges will be RV (bad) and FD (bad): +0+1+0(+6)
    - After (B2 R2 F2 R2), 1qt edges will be RD (bad) and FH (good): +0+3+0(+3)
    - After (B2 R2 F2 R2), 1qt edges will be RD (bad) and FH (good): +0+3+2(+3)
- (U2 F2 D' R2 U')
    - After (R2 F2 U2 L2), 1qt edges will be RH (good) and FD (bad), fr=1: +0+3+1(+5)
    - After (B2 L2 B2 U2 L2), 1qt edges will be RH (good) and FV (bad): +0+4+1(+3)
- (U2 B2 U' L2 U')
    - After (F2 R2 U2 F2), 1qt edges will be RD (bad) and FV (bad), fr=1: +0+3+1(+6)
    - After (L2 U2 L2), 1qt edges will be RH (good) and FH (good), fr=1: +0+2+3(+5)
- (U2 B2 U' R2 U')
    - After (F2 U2 R2 B2), 1qt edges will be RV (bad) and FV (bad), fr=1: +0+3+0(+6)
    - After (F2 R2 B2 U2 R2), 1qt edges will be RV (bad) and FH (good): +0+4+0(+3)
    - After (L2 U2 B2 U2 F2 L2), 1qt edges will be RH (good) and FD (bad): +0+5+0(+3)
- (U2 F2 D' L2 D')
    - After (F2 U2 R2 F2), 1qt edges will be RV (bad) and FD (bad), fr=1: +0+3+0(+6)
    - After (F2 L2 B2 U2 R2), 1qt edges will be RV (bad) and FH (good): +0+4+0(+3)
    - After (F2 L2 U2 R2 U2 B2), 1qt edges will be RV (bad) and FH (good): +0+5+0(+3)
- (U2 L2 B2 U B2 D')
    - After (R2), 1qt edges will be RH (good) and FH (good): +1+0+0(+0)
        - (R2 U L2 U) // no good
- (U2 R2 F2 D F2 U')
    - After (R2), 1qt edges will be RD (bad) and FH (good): +1+0+0(+3)
        - (R2 U B2 U') // no good
- (U2 B2 U' B2 L2 D')
    - After (L2), 1qt edges will be RV (bad) and FD (bad): +1+0+0(+6)
    - After (R2 F2 R2 B2), 1qt edges will be RH (good) and FD (bad): +1+3+0(+3)
- (U2 F2 D' B2 R2 U')
    - After (R2), 1qt edges will be RV (bad) and FV (bad): +1+0+0(+6)
- (F2 U2 B2 U L2 U)
    - After (B2), 1qt edges will be RV (bad) and FD (bad), fr=1: +1+0+1(+6)
    - After (B2 U2 F2 B2), 1qt edges will be RH (good) and FV (bad), fr=1: +1+3+1(+5)
- (F2 U2 F2 D R2 U)
    - After (R2), 1qt edges will be RV (bad) and FV (bad), fr=1: +1+0+1(+6)
- (B2 U2 F2 D L2 D)
    - After (L2 F2), 1qt edges will be RH (good) and FD (bad), fr=1: +1+1+0(+5)
    - After (L2 F2), 1qt edges will be RH (good) and FD (bad): +1+1+2(+3)
- (B2 U2 B2 U R2 U)
    - After (R2 F2), 1qt edges will be RD (bad) and FV (bad), fr=1: +1+1+0(+6)
    - After (B2), 1qt edges will be RH (good) and FV (bad), fr=1: +1+0+4(+5)
- (U2 R2 F2 D B2 U')
    - After (R2 F2), 1qt edges will be RD (bad) and FD (bad): +1+1+0(+6)
    - After (B2 R2 F2 L2), 1qt edges will be RV (bad) and FH (good): +1+3+0(+3)
- (B2 U2 F2 D R2 U)
    - After (L2 F2), 1qt edges will be RV (bad) and FV (bad), fr=1: +1+1+1(+6)
    - After (L2 B2), 1qt edges will be RH (good) and FD (bad): +1+1+3(+3)
- (B2 U2 B2 U L2 U)
    - After (F2 R2), 1qt edges will be RD (bad) and FV (bad), fr=1: +1+1+1(+6)
- (F2 U2 F2 D L2 D')
    - After (L2 U2 R2), 1qt edges will be RD (bad) and FH (good): +1+2+0(+3)
- (U2 F2 D' F2 L2 D)
    - After (L2 U2 R2), 1qt edges will be RH (good) and FV (bad), fr=1: +1+2+0(+5)
    - After (R2 L2 U2 R2), 1qt edges will be RH (good) and FV (bad): +1+3+0(+3)
    - After (L2 U2 R2), 1qt edges will be RH (good) and FV (bad): +1+2+2(+3)
- (U2 R2 F2 D F2 U)
    - After (R2 U2 R2), 1qt edges will be RD (bad) and FH (good), fr=1: +1+2+0(+5)
    - After (R2 U2 R2), 1qt edges will be RD (bad) and FH (good): +1+2+2(+3)
- (U2 B2 U' B2 L2 D)
    - After (R2 U2 R2), 1qt edges will be RV (bad) and FD (bad), fr=1: +1+2+0(+6)
- (U2 B2 U' F2 R2 U)
    - After (R2 U2 R2), 1qt edges will be RD (bad) and FD (bad), fr=1: +1+2+0(+6)
    - After (F2 R2 U2 F2), 1qt edges will be RV (bad) and FH (good), fr=1: +1+3+0(+5)
- (U2 F2 D' B2 R2 U)
    - After (L2 U2 R2), 1qt edges will be RV (bad) and FV (bad), fr=1: +1+2+0(+6)
    - After (F2 L2 U2 F2), 1qt edges will be RH (good) and FD (bad), fr=1: +1+3+0(+5)
- (U2 B2 U' B2 R2 U)
    - After (R2 U2 R2), 1qt edges will be RD (bad) and FH (good), fr=1: +1+2+1(+5)
    - After (R2 U2 L2), 1qt edges will be RV (bad) and FV (bad), fr=1: +1+2+1(+6)
- (U2 F2 D' B2 L2 U)
    - After (B2 U2 F2), 1qt edges will be RH (good) and FH (good), fr=1: +1+2+1(+5)
    - After (B2 U2 B2), 1qt edges will be RV (bad) and FD (bad), fr=1: +1+2+1(+6)
- (B2 U2 F2 D L2 D')
    - After (F2 U2 R2 B2), 1qt edges will be RH (good) and FD (bad): +1+3+0(+3)
- (U2 B2 U' F2 R2 U')
    - After (F2 R2 F2 B2), 1qt edges will be RD (bad) and FH (good): +1+3+0(+3)
- (F2 U2 B2 U R2 U)
    - After (L2 U2 R2 L2), 1qt edges will be RH (good) and FH (good), fr=1: +1+3+0(+5)
- (F2 U2 F2 D L2 D)
    - After (R2 B2 L2 B2), 1qt edges will be RH (good) and FH (good), fr=1: +1+3+0(+5)
    - After (B2 L2 F2 B2), 1qt edges will be RD (bad) and FV (bad), fr=1: +1+3+0(+6)
- (U2 L2 B2 U F2 D)
    - After (R2 B2 U2 L2), 1qt edges will be RH (good) and FD (bad), fr=1: +1+3+0(+5)
- (B2 U2 B2 U R2 U')
    - After (L2 B2 U2 R2), 1qt edges will be RD (bad) and FD (bad): +1+3+0(+6)
- (U2 R2 F2 D B2 U)
    - After (F2 U2 R2 F2), 1qt edges will be RD (bad) and FD (bad), fr=1: +1+3+0(+6)
- (U2 B2 U' B2 R2 U')
    - After (R2), 1qt edges will be RD (bad) and FH (good): +1+0+4(+3)
    - After (L2), 1qt edges will be RV (bad) and FV (bad): +1+0+4(+6)
- (U2 L2 F2 D B2 U')
    - After (B2 R2), 1qt edges will be RD (bad) and FH (good), fr=1: +1+1+3(+5)
- (U2 L2 F2 D F2 U')
    - After (L2 F2), 1qt edges will be RD (bad) and FH (good), fr=1: +1+1+3(+5)
- (U2 R2 B2 U B2 U')
    - After (F2 L2), 1qt edges will be RH (good) and FH (good), fr=1: +1+1+3(+5)
- (U2 R2 B2 U F2 U')
    - After (R2 B2), 1qt edges will be RH (good) and FH (good), fr=1: +1+1+3(+5)
    - After (R2 F2), 1qt edges will be RD (bad) and FD (bad), fr=1: +1+1+3(+6)
- (F2 U2 B2 U L2 U')
    - After (L2 F2 U2 L2), 1qt edges will be RH (good) and FV (bad): +1+3+1(+3)
- (U2 F2 D' F2 R2 U)
    - After (R2 L2 U2 L2), 1qt edges will be RH (good) and FD (bad): +1+3+1(+3)
    - After (B2 L2 U2 B2), 1qt edges will be RV (bad) and FH (good), fr=1: +1+3+1(+5)
- (U2 B2 U' F2 L2 U)
    - After (R2 F2 U2 L2), 1qt edges will be RV (bad) and FH (good), fr=1: +1+3+1(+5)
    - After (F2 B2 U2 B2), 1qt edges will be RD (bad) and FV (bad): +1+3+1(+6)
- (U2 L2 F2 D B2 U)
    - After (R2 U2 F2 R2), 1qt edges will be RH (good) and FV (bad), fr=1: +1+3+1(+5)
- (U2 L2 F2 D F2 U)
    - After (B2 U2 R2 B2), 1qt edges will be RD (bad) and FH (good), fr=1: +1+3+1(+5)
- (U2 R2 B2 U B2 U)
    - After (L2 U2 B2 R2), 1qt edges will be RH (good) and FH (good), fr=1: +1+3+1(+5)
    - After (L2 U2 B2 L2), 1qt edges will be RD (bad) and FD (bad), fr=1: +1+3+1(+6)
- (U2 R2 B2 U F2 U)
    - After (F2 U2 L2 F2), 1qt edges will be RH (good) and FH (good), fr=1: +1+3+1(+5)
    - After (F2 U2 L2 B2), 1qt edges will be RD (bad) and FD (bad), fr=1: +1+3+1(+6)
- (F2 U2 F2 D R2 U')
    - After (F2 L2 U2 F2), 1qt edges will be RV (bad) and FV (bad): +1+3+1(+6)
- 61 more variants of this skeleton pass the meta, not reached before the stop.

Skeleton starting with D' B2 D has DD corners, L=10, 4 spare moves.

- D' B2 D
    - After F2, 1qt edges will be FD (good) and RH (bad): +0+0+2(+3)
    - After R2 F2 R2 B2 R2, 1qt edges will be FV (good) and RD (good): +0+4+0(+0)
        - R2 F2 R2 B2 R2 U' F2 U // 4 pairs, no good
- D' F2 U
    - After R2 F2, 1qt edges will be FH (bad) and RV (good): +0+1+3(+3)
    - After F2 B2 R2 F2, 1qt edges will be FD (good) and RD (good): +0+3+1(+2)
- D' R2 B2 U'
    - After R2 B2, 1qt edges will be FH (bad) and RV (good): +1+1+1(+3)
    - After F2, 1qt edges will be FV (good) and RV (good): +1+0+3(+1)
- D' L2 B2 D'
    - After F2 R2, 1qt edges will be FH (bad) and RV (good): +1+1+2(+3)
- 5 more variants of this skeleton pass the meta, not reached before the stop.

Stop: 10 HTRs done, one finish within goal (14). This DR's optimal is 14.
