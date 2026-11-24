# The skeleton/variant meta: example solves

24 Nov 2026

The [skeleton/variant meta](WRITEUP.md), run by a solver on the 34 DRs of [*Advanced DR Bounding Examples*](https://docs.google.com/document/d/1xtvlA3Tg2zkl8H1D98XhLU66gITJ5S-oIPajsn68SOE) and written out the way that doc writes its solves.
Every scramble is a DR on U/D. The goal is 12/13/14 moves from DR to a leave-slice finish for a 2qt/3qt/4qt DR; the 0c0 DRs are solved as 2qt ones, with goal 12.
The sections are the doc's; its 4b3 DRs fall under 4c3 in the write-up, which counts 4a3 and 4b3 together.

Each example goes through up to 8 skeletons, taken from the ones with 2 or more spare moves. They come in order of their moves to HTR, and of two with the same number the one that keeps more pairs after its first quarter turn goes first, then after its second, and so on. On each of them every variant the meta lets through is taken to HTR. After that, up to 3 more finishes within goal from the other skeletons are listed as hard to find.

## How to read an example

```
Skeleton F2 U' R2 U' F2 U2 has RV corners, L=6, 6 spare moves.

- After R2 L2 B2, 1qt edges will be RV (good) and FD (bad): +2+0(+3)
    - R2 L2 B2 U' B2 U R2 B2 R2 U2 R2 U2 // 12
- After R2 L2 B2, 1qt edges will be RV (good) and FD (bad), fr=1: +2+2(+2)
    - R2 L2 B2 U B2 U2 B2 U // no good: 8 pairs, the most of 3

Check inverse. Skeleton (U2 R2 U' R2 U' R2) has FD corners.

- After (U2 B2 L2), 1qt edges will be FV (bad) and RH (good): +1+2(+3)
    - (U2 B2 L2 U F2 B2 R2 D') // no good: 6 pairs, the most of 5
```

- **Skeleton line.** The whole skeleton, in the way of writing it that keeps the most pairs, with the corners it leaves at NISS@1qt, its length L and the spare moves G−L. Its moves to HTR are L less the moves after its last quarter turn, counted on the side where that is fewer. A variant under it can start on other faces that do the same to the corners.
- **Check inverse.** The skeleton the inverse scramble reads the same solutions on, with the same L. Moves in parentheses are on the inverse. Normal always goes first.
- **Approach to 2qt** (first-level bullet): the moves up to 2qt, with P ≤ 1. Approaches with no extra move come first. Only the approaches of the variants that are shown are listed, and a 2qt skeleton has no approach, so its variants are the first level.
- **Variant line.** `After ...` gives the setup. The 1qt edges are the F and R edge cases at NISS@1qt as in [*Advanced DR Bounding*](https://docs.google.com/document/d/13F8HonrKJyHjU9EwfiHDRyY4X77vPriYeaVSrh5guq0), each with whether that slice is bad for these corners, and `fr=1` when the F/R parity is odd. Then the extra moves `+P+S+T(+N)`, or `+S+T(+N)` on a 2qt skeleton, where N is the corner-case-aware bound.
- **Moves.** Under a variant, the moves from the setup on (put the approach in front for the whole solution). Every variant that passes the meta is taken to HTR. A finish within goal is in bold, written out with its length. Of the variants of a skeleton side that are no good, only one is shown, stopped at HTR: the one with the most corner-edge pairs right after its last insertion (`// no good: 4 pairs, the most of 7`).
- **`No variant passes the meta`.** The skeleton was looked at, and nothing on that side gets through the caps and the bound.
- **Hard to find.** Finishes within goal on skeletons that are not gone through: past the first 8, or with fewer than 2 spare moves. At most 3 are shown, the first ones in the same order.
- **U or D.** A quarter turn on U and the same turn on D only differ by a turn of both layers, so they are one variant and only one is tried: the one that leaves 2 bad corners rather than 6 and, with 4 bad corners, 0 or 2 bad edges rather than 8 or 6.
- **Finish.** Leave-slice: the U and D layers are solved against each other, which can leave both of them a half turn off the centres.
- **Last line.** How many skeletons and HTRs it took, what was found on them, and the DR's optimal to a leave-slice finish.

A skeleton of 3 or more quarter turns that ends with its last one (HH corners) is gone through twice. First as [*Advanced DR Bounding*](https://docs.google.com/document/d/13F8HonrKJyHjU9EwfiHDRyY4X77vPriYeaVSrh5guq0) suggests: its last quarter turn is made first, on the other side, and the solve goes on from what is left. Then as it stands, under `The same skeleton in full`, for the solutions that go on after that quarter turn.

```
Skeleton (L2 U' R2 U L2 U L2 U' R2 D') on inverse has HH corners, L=10, 3 spare moves. Apply D and NISS: FD corners.

- (L2 U' L2 U)
    - After (B2), 1qt edges will be FH (bad) and RH (good): +0+0+0(+3)
        - (B2 U L2 U' R2 B2 R2 B2 D') // 13
```

- **`Apply ... and NISS`.** The premove, in parentheses when it is made on the inverse. It is the skeleton's last quarter turn, made on the other side. What is left is a DR with one quarter turn fewer and one move less to spend, and the line names the corners its skeleton leaves: HH again when the skeleton ends with two quarter turns in a row. The variants under it are that DR's, with `+S+T(+N)` when 2 quarter turns are left.
- **Moves after a premove.** A finish ends with the premove's quarter turn, turned the other way when that saves a U2 before it.

Left out, compared with the doc's own solves: fixable/unfixable, locked and reflected slices, the name of the insertion (a variant is given by its setup and its moves instead), cs parity, and a NISS in the middle of a skeleton.

## The examples at a glance

One row per example: what the meta finds on the skeletons it goes through, and how many more finishes within goal are listed as hard to find. "Best found" is empty when nothing within goal was found on those skeletons.

| Example | DR | Goal | DR optimal | Skeletons gone through | HTRs done | Finishes within goal | Best found | Hard to find |
|---|---|---|---|---|---|---|---|---|
| [4b2, scramble 1](#4b2-scramble-1) | 4b2 8e | 12 | 12 | 8 | 86 | 2 | 12 | 0 |
| [4b2, scramble 2](#4b2-scramble-2) | 4b2 2e | 12 | 11 | 8 | 120 | 2 | 12 | 1 |
| [4b2, scramble 3](#4b2-scramble-3) | 4b2 4e | 12 | 13 | 8 | 138 | 0 |  | 0 |
| [4b2, scramble 4](#4b2-scramble-4) | 4b2 0e | 12 | 13 | 8 | 32 | 0 |  | 0 |
| [4b2, scramble 5](#4b2-scramble-5) | 4b2 6e | 12 | 12 | 8 | 126 | 2 | 12 | 0 |
| [4b2, scramble 6](#4b2-scramble-6) | 4b2 6e | 12 | 12 | 8 | 98 | 3 | 12 | 2 |
| [4b3, scramble 1](#4b3-scramble-1) | 4b3 6e | 13 | 13 | 8 | 59 | 3 | 13 | 0 |
| [4b3, scramble 2](#4b3-scramble-2) | 4b3 6e | 13 | 14 | 8 | 8 | 0 |  | 0 |
| [4b3, scramble 3](#4b3-scramble-3) | 4b3 4e | 13 | 14 | 8 | 87 | 0 |  | 0 |
| [4b3, scramble 4](#4b3-scramble-4) | 4b3 6e | 13 | 14 | 8 | 281 | 0 |  | 0 |
| [4b3, scramble 5](#4b3-scramble-5) | 4b3 2e | 13 | 13 | 8 | 44 | 1 | 13 | 0 |
| [4b3, scramble 6](#4b3-scramble-6) | 4b3 4e | 13 | 14 | 8 | 57 | 0 |  | 0 |
| [4b3, scramble 7](#4b3-scramble-7) | 4b3 4e | 13 | 14 | 8 | 61 | 0 |  | 0 |
| [4b3, scramble 8](#4b3-scramble-8) | 4b3 4e | 13 | 13 | 6 | 522 | 14 | 13 | 0 |
| [0c0, scramble 1](#0c0-scramble-1) | 0c0 6e | 12 | 13 | 8 | 39 | 0 |  | 0 |
| [0c0, scramble 2](#0c0-scramble-2) | 0c0 2e | 12 | 11 | 8 | 135 | 11 | 11 | 0 |
| [2c3, scramble 1](#2c3-scramble-1) | 2c3 2e | 13 | 12 | 8 | 82 | 7 | 12 | 1 |
| [2c3, scramble 2](#2c3-scramble-2) | 2c3 4e | 13 | 13 | 8 | 103 | 2 | 13 | 0 |
| [2c3, scramble 3](#2c3-scramble-3) | 2c3 2e | 13 | 12 | 8 | 198 | 10 | 12 | 0 |
| [2c3, scramble 4](#2c3-scramble-4) | 2c3 2e | 13 | 12 | 8 | 325 | 6 | 12 | 3 |
| [2c3, scramble 5](#2c3-scramble-5) | 2c3 6e | 13 | 13 | 8 | 155 | 0 |  | 3 |
| [2c3, scramble 6](#2c3-scramble-6) | 2c3 6e | 13 | 12 | 8 | 147 | 6 | 12 | 1 |
| [2c3, scramble 7](#2c3-scramble-7) | 2c3 2e | 13 | 14 | 8 | 109 | 0 |  | 0 |
| [2c3, scramble 8](#2c3-scramble-8) | 2c3 6e | 13 | 13 | 8 | 126 | 2 | 13 | 0 |
| [2c3, scramble 9](#2c3-scramble-9) | 2c3 6e | 13 | 13 | 8 | 187 | 8 | 13 | 1 |
| [2c3, scramble 10](#2c3-scramble-10) | 2c3 4e | 13 | 14 | 8 | 102 | 0 |  | 0 |
| [2c3, scramble 11](#2c3-scramble-11) | 2c3 4e | 13 | 13 | 8 | 145 | 1 | 13 | 0 |
| [2c3, scramble 12](#2c3-scramble-12) | 2c3 6e | 13 | 14 | 8 | 110 | 0 |  | 0 |
| [2c4, scramble 1](#2c4-scramble-1) | 2c4 6e | 14 | 14 | 8 | 212 | 5 | 14 | 0 |
| [2c4, scramble 2](#2c4-scramble-2) | 2c4 6e | 14 | 15 | 8 | 144 | 0 |  | 0 |
| [2c4, scramble 3](#2c4-scramble-3) | 2c4 0e | 14 | 14 | 8 | 196 | 2 | 14 | 3 |
| [2c4, scramble 4](#2c4-scramble-4) | 2c4 2e | 14 | 14 | 8 | 185 | 2 | 14 | 0 |
| [2c4, scramble 5](#2c4-scramble-5) | 2c4 6e | 14 | 14 | 8 | 125 | 2 | 14 | 0 |
| [2c4, scramble 6](#2c4-scramble-6) | 2c4 4e | 14 | 14 | 8 | 457 | 2 | 14 | 0 |

22 of the 34 DRs have a finish within goal. The meta finds one on 21 of them on the skeletons it goes through, and on 20 of those it finds the DR's optimal. On 1 more the only ones it has are hard to find.

## 4b2

### 4b2, scramble 1

`R' U' F U F R2 F2 L' D2 L2 U2 B2 L' D2 U2 L F D L2 D2 F' L2 U2 R' U' F`

4b2 8e, goal 12.

Skeleton U2 B2 U R2 U has HH corners, L=5, 7 spare moves.

- After U2 F2, 1qt edges will be RH (good) and FD (bad): +0+3(+3)
    - U2 F2 U F2 R2 F2 R2 D' // no good: 4 pairs, the most of 24

Check inverse. Skeleton (U R2 U R2 U2) has FV corners.

- With no setup, 1qt edges will be FV (good) and RV (good): +0+3(+1)
    - **(U L2 F2 R2 B2 U' R2 F2 D2 F2 L2 B2) // 12**
    - **(U L2 F2 L2 F2 D' R2 F2 U2 L2 B2 R2) // 12**
- After (F2 B2), 1qt edges will be FV (good) and RV (good): +2+3(+1)
    - (F2 B2 U F2 R2 B2 L2 U') // no good: 10 pairs, the most of 18

Skeleton U2 B2 U B2 D U' B2 D' has HH corners, L=8, 4 spare moves.

- U2 F2 U R2 D'
    - After R2 F2 L2, 1qt edges will be RH (good) and FH (good): +0+3+0(+0)
        - R2 F2 L2 U' R2 U // no good: 3 pairs, the most of 4

Check inverse. Skeleton (U B2 D U' B2 D' F2 U2) has FV corners.

- (U B2 D')
    - After (F2 R2 B2), 1qt edges will be FV (good) and RH (good): +0+3+0(+0)
        - (F2 R2 B2 U' B2 U) // no good: 2 pairs, the most of 2

Skeleton U D R2 D B2 U' has HH corners, L=6, 6 spare moves. Apply (U) and NISS: RD corners.

- U
    - After B2 L2 F2, 1qt edges will be RD (good) and FH (good): +0+3+1(+0)
        - B2 L2 F2 U' R2 B2 D // no good: 6 pairs, the most of 16

Check inverse. Skeleton (U L2 U F2 U' D) has HH corners. Apply D' and NISS: HH corners.

- (U)
    - After (F2 R2), 1qt edges will be RH (good) and FH (good): +0+1+4(+0)
        - (F2 R2 U' F2 U2 F2 R2 B2 D) // no good: 4 pairs, the most of 12

The same skeleton in full, for the solutions that go on after its last quarter turn.

- No variant passes the meta.

Skeleton B2 U D R2 D' F2 U' has HH corners, L=7, 5 spare moves. Apply (U) and NISS: RD corners.

- No variant passes the meta.

Check inverse. Skeleton (U R2 U' R2 D U B2) has FD corners.

- No variant passes the meta.

Skeleton (U R2 U' B2 U D B2 U2 R2) on inverse has DD corners, L=9, 3 spare moves.

- (U L2 D')
    - After (F2), 1qt edges will be FD (good) and RV (good): +0+0+3(+0)
        - (F2 U L2 F2 R2 D) // no good: 4 pairs, the most of 4

Skeleton (U R2 U F2 U D' F2 U2) on inverse has RV corners, L=8, 4 spare moves.

- (U L2 D)
    - After (B2), 1qt edges will be RV (good) and FH (good): +0+0+3(+0)
        - (B2 U' R2 B2 L2 D') // no good: 6 pairs, the most of 4

Skeleton U2 B2 U' R2 D U B2 D' has HH corners, L=8, 4 spare moves.

- No variant passes the meta.

Check inverse. Skeleton (U' R2 D U B2 D' R2 U2) has FV corners.

- No variant passes the meta.

Skeleton U2 F2 U F2 U D' U' has HH corners, L=7, 5 spare moves. Apply (U) and NISS: HH corners.

- No variant passes the meta.

8 skeletons gone through, 86 HTRs: 2 finishes within goal (12, 12). This DR's optimal is 12.

### 4b2, scramble 2

`R' U' F L2 F U' B2 L' F2 R' U2 F2 R2 D2 B U2 F U2 D2 B' R' U2 R' U' F`

4b2 2e, goal 12.

Skeleton F2 U' R2 U' F2 U2 has RV corners, L=6, 6 spare moves.

- After R2 L2 B2, 1qt edges will be RV (good) and FD (bad): +2+0(+3)
    - **R2 L2 B2 U' B2 U R2 B2 R2 U2 R2 U2 // 12**
- After R2 L2 B2, 1qt edges will be RV (good) and FD (bad), fr=1: +2+2(+2)
    - R2 L2 B2 U B2 U2 B2 U // no good: 8 pairs, the most of 3

Check inverse. Skeleton (U2 R2 U' R2 U' R2) has FD corners.

- After (U2 B2 L2), 1qt edges will be FV (bad) and RH (good): +1+2(+3)
    - (U2 B2 L2 U F2 B2 R2 D') // no good: 6 pairs, the most of 5

Skeleton F2 U' R2 U' R2 U D' L2 U2 has FV corners, L=9, 3 spare moves.

- No variant passes the meta.

Skeleton F2 U' R2 U' F2 D' U has HH corners, L=7, 5 spare moves. Apply (U') and NISS: HH corners.

- F2 U'
    - After R2, 1qt edges will be RH (good) and FV (bad): +0+0+1(+3)
        - R2 U' R2 F2 U' // no good: 10 pairs, the most of 24

The same skeleton in full, for the solutions that go on after its last quarter turn.

- F2 U' R2 U'
    - After R2 F2, 1qt edges will be RH (good) and FH (good): +0+1+3(+0)
        - R2 F2 U R2 F2 R2 U' // no good: 8 pairs, the most of 16

Skeleton F2 U' R2 U F2 U D R2 has RD corners, L=8, 4 spare moves.

- No variant passes the meta.

Skeleton F2 U' R2 U L2 U D R2 U2 B2 has DD corners, L=10, 2 spare moves.

- No variant passes the meta.

Skeleton F2 U R2 U D B2 D B2 U2 has RV corners, L=9, 3 spare moves.

- No variant passes the meta.

Check inverse. Skeleton (U2 R2 U L2 U D B2 D L2) has FD corners.

- No variant passes the meta.

Skeleton F2 U' F2 U D' F2 D R2 U2 has RV corners, L=9, 3 spare moves.

- B2 D' F2 D
    - After L2 B2 L2, 1qt edges will be RV (good) and FH (good): +0+3+0(+0)
        - L2 B2 L2 U R2 U' // no good

Check inverse. Skeleton (U2 R2 U' B2 U D' F2 D F2) has FD corners.

- (U2 R2 U' F2 U')
    - After (R2 B2 R2), 1qt edges will be FD (good) and RH (good): +0+3+0(+0)
        - (R2 B2 R2 U' B2 U') // no good: 5 pairs, the most of 3

Skeleton U R2 U R2 U F2 U has HH corners, L=7, 5 spare moves. Apply (U') and NISS: RD corners.

- U
    - After L2 B2 L2 F2, 1qt edges will be RD (good) and FH (good): +0+3+2(+0)
        - L2 B2 L2 F2 U' F2 R2 L2 D // no good: 8 pairs, the most of 13

The same skeleton in full, for the solutions that go on after its last quarter turn.

- D B2 D
    - After R2, 1qt edges will be RH (good) and FH (good): +0+0+3(+0)
        - **R2 U L2 B2 L2 B2 U L2 R2 // 12**
    - After F2 B2 R2, 1qt edges will be RH (good) and FH (good): +0+2+3(+0)
        - F2 B2 R2 U R2 B2 R2 B2 U' // no good: 16 pairs, the most of 39

Check inverse. Skeleton (D' B2 U L2 D R2 D') has HH corners. Apply D and NISS: FD corners.

- (D')
    - After (B2 L2 B2 L2), 1qt edges will be FD (good) and RH (good): +0+3+2(+0)
        - (B2 L2 B2 L2 U' F2 R2 L2 D) // no good: 12 pairs, the most of 9

The same skeleton in full, for the solutions that go on after its last quarter turn.

- (U' L2 U)
    - After (F2 L2 B2 L2), 1qt edges will be RH (good) and FH (good): +0+3+2(+0)
        - (F2 L2 B2 L2 U' F2 R2 L2 D) // no good: 8 pairs, the most of 5

Hard to find, on skeletons that are not gone through:

Skeleton (U2 R2 U' R2 U' B2 U D' F2) on inverse has RD corners, L=9, 3 spare moves.

- (U2 R2 U' L2 D')
    - After (F2), 1qt edges will be RD (good) and FH (good): +0+0+2(+0)
        - **(F2 U F2 B2 D' R2) // 11**

8 skeletons gone through, 120 HTRs: 2 finishes within goal (12, 12). This DR's optimal is 11.

### 4b2, scramble 3

`R' U' F D' F B D2 B2 U' B' L F2 U F2 D2 F2 D2 R2 B2 L2 F2 D R' U' F`

4b2 4e, goal 12.

Skeleton L2 U2 B2 U' L2 U' has HH corners, L=6, 6 spare moves.

- After B2 U2 R2, 1qt edges will be RH (good) and FH (good): +0+1(+0)
    - B2 U2 R2 U' F2 R2 U' // no good: 8 pairs, the most of 120

Skeleton B2 U D B2 D' R2 U has HH corners, L=7, 5 spare moves. Apply (U') and NISS: RD corners.

- F2 D
    - After F2 B2 R2 B2 L2, 1qt edges will be RD (good) and FH (good): +0+5+0(+0)
        - F2 B2 R2 B2 L2 U' R2 U // no good: 5 pairs, the most of 12

Check inverse. Skeleton (U' R2 U R2 U D R2) has FD corners.

- No variant passes the meta.

Skeleton L2 U D R2 D' F2 U has HH corners, L=7, 5 spare moves. Apply (U') and NISS: RD corners.

- No variant passes the meta.

Check inverse. Skeleton (U' R2 U' R2 U D R2) has RD corners.

- No variant passes the meta.

Skeleton B2 U2 R2 U' R2 U D' U has HH corners, L=8, 4 spare moves. Apply (U') and NISS: HH corners.

- No variant passes the meta.

Skeleton L2 D' B2 U F2 U B2 D F2 has RD corners, L=9, 3 spare moves.

- B2 L2 D L2 U'
    - After L2, 1qt edges will be RD (good) and FH (good): +1+0+2(+0)
        - L2 U F2 U2 B2 U' // no good: 2 pairs, the most of 2

Check inverse. Skeleton (R2 U R2 U L2 U F2 U' F2) has RD corners.

- No variant passes the meta.

Skeleton U2 R2 D R2 U' L2 U' F2 D' R2 has RD corners, L=10, 2 spare moves.

- No variant passes the meta.

Check inverse. Skeleton (R2 U B2 D B2 U L2 D' R2 U2) has RV corners.

- No variant passes the meta.

Skeleton U2 B2 U D B2 D B2 U has HH corners, L=8, 4 spare moves. Apply (U') and NISS: RD corners.

- No variant passes the meta.

Skeleton U2 R2 U D L2 D L2 U has HH corners, L=8, 4 spare moves. Apply (U') and NISS: RD corners.

- U2 B2 R2 U'
    - After L2 B2 R2, 1qt edges will be RD (good) and FH (good): +1+3+0(+0)
        - L2 B2 R2 U R2 U' // no good: 4 pairs, the most of 4

8 skeletons gone through, 138 HTRs: nothing within goal. This DR's optimal is 13, over the goal.

### 4b2, scramble 4

`R' U' F U2 R2 F D R' L' U2 F' L2 U' L2 B2 U' R2 B2 D R2 L2 F D' R' U' F`

4b2 0e, goal 12.

Skeleton F2 U' R2 U F2 U2 has RV corners, L=6, 6 spare moves.

- No variant passes the meta.

Check inverse. Skeleton (U2 R2 U R2 U' R2) has FD corners.

- No variant passes the meta.

Skeleton F2 U' B2 U D' F2 D' L2 U2 has RV corners, L=9, 3 spare moves.

- No variant passes the meta.

Check inverse. Skeleton (U2 R2 U F2 U D' F2 D F2) has FD corners.

- No variant passes the meta.

Skeleton F2 U' R2 U' B2 D U R2 has RD corners, L=8, 4 spare moves.

- No variant passes the meta.

Skeleton F2 U' R2 U B2 D' U has HH corners, L=7, 5 spare moves. Apply (U') and NISS: HH corners.

- R2 F2 U
    - After F2 R2 F2 R2, 1qt edges will be RH (good) and FH (good): +1+3+0(+0)
        - F2 R2 F2 R2 U B2 U' // no good: 6 pairs, the most of 28

The same skeleton in full, for the solutions that go on after its last quarter turn.

- No variant passes the meta.

Skeleton F2 U' R2 U R2 U D' L2 U2 has FV corners, L=9, 3 spare moves.

- No variant passes the meta.

Skeleton U2 B2 U L2 U' L2 U' F2 U' has HH corners, L=9, 3 spare moves. Apply (U) and NISS: RD corners.

- F2 U2 F2 D'
    - After L2, 1qt edges will be RD (good) and FH (good): +1+0+2(+0)
        - L2 U' F2 R2 L2 D' // no good

The same skeleton in full, for the solutions that go on after its last quarter turn.

- No variant passes the meta.

Check inverse. Skeleton (U R2 U' L2 U' B2 U R2 U2) has FV corners.

- (U R2 U')
    - After (F2 L2), 1qt edges will be FD (bad) and RH (good), fr=1: +0+1+0(+2)
        - (F2 L2 U R2 U') // no good

Skeleton D L2 D F2 U B2 U B2 U2 L2 has DD corners, L=10, 2 spare moves.

- No variant passes the meta.

Check inverse. Skeleton (L2 U2 F2 D' L2 U' L2 D' L2 D') has HH corners. Apply D and NISS: RD corners.

- No variant passes the meta.

The same skeleton in full, for the solutions that go on after its last quarter turn.

- No variant passes the meta.

Skeleton D B2 D L2 U B2 U' B2 has RD corners, L=8, 4 spare moves.

- D F2 D'
    - After R2 L2 B2 U2 B2, 1qt edges will be RD (good) and FH (good): +0+4+0(+0)
        - R2 L2 B2 U2 B2 U' B2 U' // no good: 4 pairs, the most of 2

Check inverse. Skeleton (L2 D' R2 U B2 D R2 D') has HH corners. Apply D and NISS: FD corners.

- No variant passes the meta.

The same skeleton in full, for the solutions that go on after its last quarter turn.

- No variant passes the meta.

8 skeletons gone through, 32 HTRs: nothing within goal. This DR's optimal is 13, over the goal.

### 4b2, scramble 5

`R' U' F D F2 D2 L2 R B2 U2 R D2 L' U2 R2 F2 D' U2 L' F U' L' F R' U' F`

4b2 6e, goal 12.

Skeleton U2 F2 U' L2 U' F2 U2 has FV corners, L=7, 5 spare moves.

- After U2 L2 B2, 1qt edges will be FV (good) and RV (good), fr=1: +1+0(+2)
    - U2 L2 B2 U R2 D' // no good: 4 pairs, the most of 6
- After B2 U2 L2 B2, 1qt edges will be FV (good) and RV (good): +2+0(+1)
    - **B2 U2 L2 B2 U' R2 D B2 R2 U2 R2 L2 // 12**

Check inverse. Skeleton (U2 B2 U F2 U F2 U2) has FV corners.

- After (U2 B2), 1qt edges will be FD (bad) and RV (good), fr=1: +0+0(+2)
    - **(U2 B2 U B2 D' R2 B2 R2 F2 L2 U2 F2) // 12**
- After (U2 B2), 1qt edges will be FD (bad) and RV (good): +0+2(+3)
    - (U2 B2 U' B2 U2 B2 D) // no good: 6 pairs, the most of 9

Skeleton U' B2 U B2 U F2 D' has HH corners, L=7, 5 spare moves. Apply (D) and NISS: FD corners.

- U'
    - After B2, 1qt edges will be FH (bad) and RD (good), fr=1: +0+0+1(+3)
        - B2 U R2 F2 D' // no good: 6 pairs, the most of 8

The same skeleton in full, for the solutions that go on after its last quarter turn.

- U' B2 D
    - After B2 R2, 1qt edges will be RH (good) and FH (good): +0+1+2(+0)
        - B2 R2 U R2 U2 L2 U' // no good: 8 pairs, the most of 14

Check inverse. Skeleton (U L2 U' L2 U' F2 U) has HH corners. Apply U' and NISS: FD corners.

- (U)
    - After (B2 R2), 1qt edges will be FV (bad) and RH (good), fr=1: +0+1+1(+3)
        - (B2 R2 U B2 L2 U) // no good: 8 pairs, the most of 8

The same skeleton in full, for the solutions that go on after its last quarter turn.

- (D F2 U')
    - After (B2), 1qt edges will be RH (good) and FH (good): +0+0+4(+0)
        - (B2 U F2 U2 R2 L2 F2 D') // no good: 8 pairs, the most of 52

Skeleton U' R2 D B2 U L2 D B2 U2 has RV corners, L=9, 3 spare moves.

- No variant passes the meta.

Check inverse. Skeleton (U2 R2 U F2 U F2 U F2 U) has HH corners. Apply U' and NISS: RD corners.

- (U2 B2 L2 U)
    - After (B2 U2 B2), 1qt edges will be RD (good) and FH (good): +1+2+0(+0)
        - (B2 U2 B2 U B2 U') // no good

The same skeleton in full, for the solutions that go on after its last quarter turn.

- (U2 L2 U L2 D)
    - After (B2), 1qt edges will be RH (good) and FH (good): +0+0+2(+0)
        - (B2 U' B2 U2 F2 U) // no good: 4 pairs, the most of 5

Skeleton U2 L2 U' R2 U' R2 U' F2 D' has HH corners, L=9, 3 spare moves. Apply (D) and NISS: RD corners.

- L2 U2 L2 U
    - After B2 R2, 1qt edges will be RD (good) and FH (good): +1+1+0(+0)
        - B2 R2 U B2 U' // no good: 4 pairs, the most of 6

The same skeleton in full, for the solutions that go on after its last quarter turn.

- No variant passes the meta.

Check inverse. Skeleton (D L2 U' L2 U' R2 D' F2 U2) has RV corners.

- (D F2 L2 U)
    - After (B2), 1qt edges will be RV (good) and FH (good), fr=1: +1+0+1(+1)
        - (B2 U B2 L2 U) // no good: 6 pairs, the most of 4

Skeleton U2 F2 U R2 D U F2 D B2 U2 has FV corners, L=10, 2 spare moves.

- No variant passes the meta.

Check inverse. Skeleton (U2 B2 U' B2 D U R2 D' F2 U2) has FV corners.

- No variant passes the meta.

Skeleton U2 B2 U' R2 D U' L2 D L2 U2 has FV corners, L=10, 2 spare moves.

- No variant passes the meta.

Check inverse. Skeleton (U2 B2 U L2 U D' L2 D' L2 U2) has FV corners.

- No variant passes the meta.

Skeleton (U2 B2 U B2 U L2 D U) on inverse has HH corners, L=8, 4 spare moves. Apply U' and NISS: HH corners.

- (U2 B2 U')
    - After (B2 U2 B2), 1qt edges will be RH (good) and FH (good): +0+2+1(+0)
        - (B2 U2 B2 U' F2 R2 D') // no good: 8 pairs, the most of 11

The same skeleton in full, for the solutions that go on after its last quarter turn.

- No variant passes the meta.

Skeleton (U2 B2 U F2 U' F2 D U R2) on inverse has FD corners, L=9, 3 spare moves.

- No variant passes the meta.

8 skeletons gone through, 126 HTRs: 2 finishes within goal (12, 12). This DR's optimal is 12.

### 4b2, scramble 6

`R' U' F D2 B' U' F2 B' U' L F2 R2 U2 L2 U2 F R2 F2 B R2 U2 R U2 R' U' F`

4b2 6e, goal 12.

Skeleton R2 U' R2 U F2 U2 has RV corners, L=6, 6 spare moves.

- After R2 B2 L2 B2, 1qt edges will be RV (good) and FH (good), fr=1: +3+0(+1)
    - R2 B2 L2 B2 U B2 D' // no good: 4 pairs, the most of 24
- After U2 R2 U2 L2, 1qt edges will be RV (good) and FV (good): +3+0(+1)
    - **U2 R2 U2 L2 U B2 D R2 F2 U2 F2 B2 // 12**

Check inverse. Skeleton (U2 L2 U F2 U' F2) has RD corners.

- After (B2 R2 U2 F2), 1qt edges will be RD (good) and FD (good): +2+0(+1)
    - (B2 R2 U2 F2 U L2 D) // no good: 8 pairs, the most of 7
- After (R2 U2 L2), 1qt edges will be RH (bad) and FH (good): +1+2(+3)
    - **(R2 U2 L2 U' R2 L2 B2 U' B2 R2 B2 L2) // 12**
- After (F2 B2 U2 F2 R2), 1qt edges will be RD (good) and FH (good), fr=1: +3+0(+3)
    - **(F2 B2 U2 F2 R2 U' L2 D' L2 U2 R2 U2) // 12**

Skeleton R2 U L2 D U B2 D' F2 U2 has RV corners, L=9, 3 spare moves.

- No variant passes the meta.

Check inverse. Skeleton (U2 L2 U' F2 D U R2 D B2) has RD corners.

- No variant passes the meta.

Skeleton R2 U' B2 D U' B2 D' R2 U2 has RV corners, L=9, 3 spare moves.

- No variant passes the meta.

Check inverse. Skeleton (U2 L2 U R2 U D' L2 D R2) has RD corners.

- No variant passes the meta.

Skeleton R2 U' R2 U R2 U D' L2 U2 has FV corners, L=9, 3 spare moves.

- No variant passes the meta.

Skeleton R2 U' R2 U' F2 U D R2 has RD corners, L=8, 4 spare moves.

- R2 U' L2 D'
    - After B2, 1qt edges will be RD (good) and FD (good): +0+0+3(+1)
        - B2 U B2 R2 B2 U' // no good: 10 pairs, the most of 6

Skeleton R2 U' L2 U L2 D' U has HH corners, L=7, 5 spare moves. Apply (U') and NISS: HH corners.

- L2 U'
    - After L2 B2, 1qt edges will be RH (good) and FH (good): +0+1+4(+0)
        - L2 B2 U F2 R2 U2 R2 B2 U' // no good: 8 pairs, the most of 14

The same skeleton in full, for the solutions that go on after its last quarter turn.

- No variant passes the meta.

Skeleton U F2 U F2 U R2 U' F2 has RD corners, L=8, 4 spare moves.

- U F2 U
    - After F2, 1qt edges will be RD (good) and FD (good): +0+0+1(+1)
        - F2 U B2 L2 D // no good: 10 pairs, the most of 15

Check inverse. Skeleton (R2 U' F2 U F2 U R2 U') has HH corners. Apply U and NISS: FD corners.

- (R2 U')
    - After (L2 B2), 1qt edges will be FD (good) and RD (good): +0+1+1(+1)
        - (L2 B2 U' L2 B2 U') // no good: 6 pairs, the most of 10

The same skeleton in full, for the solutions that go on after its last quarter turn.

- (F2 L2 D R2 U')
    - After (B2), 1qt edges will be RH (good) and FH (good): +1+0+1(+0)
        - (B2 U' R2 B2 U) // no good: 8 pairs, the most of 9

Skeleton U2 R2 U B2 U' B2 U' R2 U' has HH corners, L=9, 3 spare moves. Apply (U) and NISS: FD corners.

- U2 R2 U
    - After B2, 1qt edges will be FH (bad) and RD (good): +0+0+0(+3)
        - B2 U' B2 U' // no good: 6 pairs, the most of 3

The same skeleton in full, for the solutions that go on after its last quarter turn.

- U2 R2 U B2 D'
    - After R2, 1qt edges will be RH (good) and FH (good): +0+0+0(+0)
        - R2 U' B2 U // no good: 8 pairs, the most of 7

Check inverse. Skeleton (U F2 D' B2 U' B2 D F2 U2) has RV corners.

- No variant passes the meta.

Hard to find, on skeletons that are not gone through:

Skeleton U R2 U L2 U F2 U F2 U2 R2 has DD corners, L=10, 2 spare moves.

- U L2 D
    - After B2 L2, 1qt edges will be FD (good) and RV (good): +0+1+0(+0)
        - **B2 L2 U' F2 U' R2 U2 R2 B2 // 12**

Skeleton (B2 U2 L2 U' L2 U F2 U F2 U') on inverse has HH corners, L=10, 2 spare moves. Apply U and NISS: RD corners.

- (B2 R2 U2 R2 U)
    - After (F2), 1qt edges will be RD (good) and FH (good): +1+0+1(+0)
        - **(F2 U L2 B2 D' L2 U') // 12**

8 skeletons gone through, 98 HTRs: 3 finishes within goal (12, 12, 12). This DR's optimal is 12.

## 4b3

### 4b3, scramble 1

`R' U' F D R B2 R B2 R' B2 R' U2 B2 R B2 F L' R B U R' U F2 R' U' F`

4b3 6e, goal 13.

Skeleton F2 U2 R2 D L2 D B2 U2 L2 D' has HH corners, L=10, 3 spare moves. Apply (D) and NISS: DD corners.

- After B2 U2 R2, 1qt edges will be FH (bad) and RD (good): +0+0(+3)
    - **B2 U2 R2 U L2 U L2 D2 B2 R2 B2 R2 D // 13**
- After R2 U2 R2 B2, 1qt edges will be FV (good) and RD (good): +1+2(+0)
    - R2 U2 R2 B2 U L2 U2 L2 U' // no good: 6 pairs, the most of 11

The same skeleton in full, for the solutions that go on after its last quarter turn.

- B2 U2 R2 D
    - After F2, 1qt edges will be RH (good) and FH (good): +0+0+3(+0)
        - F2 U B2 U2 R2 F2 L2 F2 D' // no good: 16 pairs, the most of 13
        - **F2 U F2 U2 R2 F2 R2 F2 U // 13**

Check inverse. Skeleton (D L2 U2 F2 D' F2 U R2 U2 F2) has DD corners.

- (D')
    - After (L2 F2 L2 B2 U2 L2), 1qt edges will be FD (good) and RV (good): +0+3+0(+0)
        - (L2 F2 L2 B2 U2 L2 U' B2 U') // no good: 6 pairs, the most of 12
    - After (R2 B2 R2 B2 U2 R2), 1qt edges will be FD (good) and RV (good): +0+3+0(+0)
        - **(R2 B2 R2 B2 U2 R2 U' R2 U' L2 D2 B2) // 13**

Skeleton D' L2 U B2 U2 R2 D R2 U2 has RV corners, L=9, 4 spare moves.

- No variant passes the meta.

Check inverse. Skeleton (U2 R2 U R2 U2 B2 U R2 D) has HH corners. Apply D' and NISS: RD corners.

- No variant passes the meta.

The same skeleton in full, for the solutions that go on after its last quarter turn.

- (U2 R2 D')
    - After (L2 F2 R2 F2 U2 L2), 1qt edges will be RH (good) and FH (good): +0+3+0(+0)
        - (L2 F2 R2 F2 U2 L2 U R2 U') // no good: 6 pairs, the most of 8

Skeleton D' L2 U' F2 U D F2 U' F2 U2 has RV corners, L=10, 3 spare moves.

- No variant passes the meta.

Check inverse. Skeleton (U2 R2 U' L2 U D R2 D' F2 D) has HH corners. Apply D' and NISS: RD corners.

- No variant passes the meta.

Skeleton D' L2 U B2 U D B2 U R2 U2 has RV corners, L=10, 3 spare moves.

- No variant passes the meta.

Check inverse. Skeleton (U2 R2 U' B2 U D B2 D' R2 D) has HH corners. Apply D' and NISS: RD corners.

- (U2 L2 D' L2 F2 D)
    - After (R2 L2), 1qt edges will be RD (good) and FH (good): +1+2+0(+0)
        - (R2 L2 U F2 U) // no good

Skeleton D' L2 U' R2 U D L2 U' R2 U2 has RV corners, L=10, 3 spare moves.

- D' B2 L2 D L2 D
    - After R2 L2, 1qt edges will be RV (good) and FH (good): +1+2+0(+0)
        - R2 L2 U F2 U // no good

Check inverse. Skeleton (U2 R2 U L2 U D R2 D L2 D) has HH corners. Apply D' and NISS: RD corners.

- (U2 R2 U L2 U)
    - After (F2 B2), 1qt edges will be RD (good) and FH (good): +0+2+1(+0)
        - (F2 B2 U F2 R2 D') // no good: 6 pairs, the most of 2

Skeleton D' L2 U L2 U D R2 U F2 U2 has RV corners, L=10, 3 spare moves.

- No variant passes the meta.

Check inverse. Skeleton (U2 R2 U B2 U D B2 D B2 D) has HH corners. Apply D' and NISS: RD corners.

- No variant passes the meta.

Skeleton L2 U B2 U' R2 U' F2 U R2 D has HH corners, L=10, 3 spare moves. Apply (D') and NISS: FD corners.

- R2 D F2 D'
    - After R2 B2 L2 B2, 1qt edges will be FD (good) and RH (good): +0+3+0(+0)
        - R2 B2 L2 B2 U B2 U // no good: 6 pairs, the most of 3

The same skeleton in full, for the solutions that go on after its last quarter turn.

- B2 L2 D' B2 U R2 U
    - After R2, 1qt edges will be RH (good) and FH (good): +1+0+1(+0)
        - R2 U' F2 L2 D' // no good: 8 pairs, the most of 4

Check inverse. Skeleton (D' B2 U L2 U' F2 D' R2 U B2) has RD corners.

- (D' B2 U B2 R2 U)
    - After (F2 R2 L2), 1qt edges will be RD (good) and FH (good): +1+2+0(+0)
        - (F2 R2 L2 U F2 U) // no good

Skeleton U2 R2 D' L2 U L2 U R2 D' B2 D has HH corners, L=11, 2 spare moves. Apply (D') and NISS: FD corners.

- No variant passes the meta.

The same skeleton in full, for the solutions that go on after its last quarter turn.

- No variant passes the meta.

Check inverse. Skeleton (D' B2 U F2 U' L2 D' F2 U L2 U2) has RV corners.

- No variant passes the meta.

8 skeletons gone through, 59 HTRs: 3 finishes within goal (13, 13, 13). This DR's optimal is 13.

### 4b3, scramble 2

`R' U' F R2 B2 R' U F2 U' F' U2 L' F2 R' U2 L' D2 F2 R F2 D' B2 D2 R' U' F`

4b3 6e, goal 13.

Skeleton F2 D R2 U B2 U2 L2 D' R2 U2 has RV corners, L=10, 3 spare moves.

- B2 U
    - After R2, 1qt edges will be RH (bad) and FH (good), fr=1: +0+0+0(+2)
        - R2 U F2 U2 L2 U' // no good: 4 pairs, the most of 2

Check inverse. Skeleton (U2 R2 U F2 U2 L2 D' R2 D' B2) has FD corners.

- (U2 L2 D)
    - After (R2 U2 B2 L2 B2 L2), 1qt edges will be FD (good) and RH (good): +0+3+0(+0)
        - (R2 U2 B2 L2 B2 L2 U R2 U) // no good: 0 pairs, the most of 2

Skeleton F2 D R2 U B2 U D F2 U' L2 U2 has RV corners, L=11, 2 spare moves.

- No variant passes the meta.

Skeleton F2 D R2 U' L2 U D L2 U L2 U2 has RV corners, L=11, 2 spare moves.

- No variant passes the meta.

Skeleton F2 D R2 U R2 U D R2 U' B2 U2 has RV corners, L=11, 2 spare moves.

- No variant passes the meta.

Skeleton F2 D R2 U' F2 U D B2 U B2 U2 has RV corners, L=11, 2 spare moves.

- No variant passes the meta.

Skeleton U' F2 D' L2 U' L2 U B2 D' B2 U2 has RV corners, L=11, 2 spare moves.

- U' R2 B2 U B2 D
    - After L2 F2, 1qt edges will be RV (good) and FH (good): +1+1+0(+0)
        - L2 F2 U B2 U' // no good

Check inverse. Skeleton (U2 R2 U' F2 D L2 U' B2 D' R2 U) has HH corners. Apply U' and NISS: FD corners.

- No variant passes the meta.

The same skeleton in full, for the solutions that go on after its last quarter turn.

- (U2 L2 D' F2 D B2 R2 D)
    - After (R2 F2), 1qt edges will be RH (good) and FH (good): +1+1+0(+0)
        - (R2 F2 U' L2 U') // no good: 6 pairs, the most of 2

Skeleton U' R2 D' F2 U' L2 D B2 U' R2 U2 has RV corners, L=11, 2 spare moves.

- No variant passes the meta.

Check inverse. Skeleton (U2 R2 U F2 D' R2 U B2 D R2 U) has HH corners. Apply U' and NISS: RD corners.

- No variant passes the meta.

The same skeleton in full, for the solutions that go on after its last quarter turn.

- (R2 U2 L2 D' F2 U' F2 U)
    - After (L2), 1qt edges will be RH (good) and FH (good): +1+0+0(+0)
        - (L2 U F2 U') // no good

Skeleton F2 U F2 U R2 U2 B2 U' L2 D U has HH corners, L=11, 2 spare moves. Apply (U') and NISS: HH corners.

- No variant passes the meta.

The same skeleton in full, for the solutions that go on after its last quarter turn.

- No variant passes the meta.

8 skeletons gone through, 8 HTRs: nothing within goal. This DR's optimal is 14, over the goal.

### 4b3, scramble 3

`R' U' F U2 F2 R2 B2 U' R' F B' R D L U' R2 U' D' F2 U2 D L2 D2 R' U' F`

4b3 4e, goal 13.

Skeleton U L2 U R2 U2 F2 D' has HH corners, L=7, 6 spare moves. Apply (D) and NISS: DD corners.

- With no setup, 1qt edges will be FV (good) and RH (bad): +0+3(+3)
    - U L2 F2 R2 B2 D // no good: 6 pairs, the most of 4

The same skeleton in full, for the solutions that go on after its last quarter turn.

- D
    - After F2, 1qt edges will be RH (good) and FV (bad): +0+0+3(+3)
        - F2 U R2 U2 B2 L2 B2 L2 U' // no good: 10 pairs, the most of 8

Check inverse. Skeleton (U R2 U2 B2 U' F2 D') has HH corners. Apply D and NISS: FD corners.

- With no setup, 1qt edges will be FH (bad) and RH (good): +0+3(+3)
    - (U' R2 U2 B2 L2 F2 R2 D') // no good: 6 pairs, the most of 16

The same skeleton in full, for the solutions that go on after its last quarter turn.

- (D)
    - After (L2 U2 B2), 1qt edges will be RV (bad) and FH (good): +0+0+3(+3)
        - (L2 U2 B2 U' B2 R2 B2 R2 U) // no good: 10 pairs, the most of 32

Skeleton U L2 U' R2 U D R2 D' has HH corners, L=8, 5 spare moves. Apply (D) and NISS: RD corners.

- No variant passes the meta.

The same skeleton in full, for the solutions that go on after its last quarter turn.

- D B2 D' F2 D
    - After R2 F2 L2, 1qt edges will be RH (good) and FH (good): +0+3+0(+0)
        - R2 F2 L2 U' B2 U // no good: 0 pairs, the most of 3

Check inverse. Skeleton (U B2 U D B2 D' R2 D') has HH corners. Apply D and NISS: FD corners.

- No variant passes the meta.

Skeleton U L2 U B2 D U B2 D has HH corners, L=8, 5 spare moves. Apply (D') and NISS: FD corners.

- No variant passes the meta.

The same skeleton in full, for the solutions that go on after its last quarter turn.

- D F2 U B2 R2 U'
    - After L2 F2 L2, 1qt edges will be RH (good) and FH (good): +1+3+0(+0)
        - L2 F2 L2 U B2 U' // no good: 6 pairs, the most of 6

Check inverse. Skeleton (U' R2 U D L2 D L2 D') has HH corners. Apply D and NISS: FD corners.

- (U' F2 L2 D)
    - After (R2 F2 R2), 1qt edges will be FD (good) and RH (good): +1+3+0(+0)
        - (R2 F2 R2 U' L2 U) // no good: 5 pairs, the most of 4

Skeleton U L2 U R2 U D R2 D' has HH corners, L=8, 5 spare moves. Apply (D) and NISS: FD corners.

- No variant passes the meta.

The same skeleton in full, for the solutions that go on after its last quarter turn.

- No variant passes the meta.

Check inverse. Skeleton (U R2 U D L2 D' F2 D') has HH corners. Apply D and NISS: FD corners.

- (U L2 U)
    - After (L2 B2 R2), 1qt edges will be FD (good) and RH (good): +0+3+2(+0)
        - (L2 B2 R2 U F2 U2 B2 U') // no good: 6 pairs, the most of 6

Skeleton U L2 U' F2 D U B2 D has HH corners, L=8, 5 spare moves. Apply (D') and NISS: RD corners.

- No variant passes the meta.

The same skeleton in full, for the solutions that go on after its last quarter turn.

- D F2 U' L2 U
    - After L2 B2 R2, 1qt edges will be RH (good) and FH (good): +0+3+2(+0)
        - L2 B2 R2 U B2 U2 B2 U // no good: 8 pairs, the most of 4

Check inverse. Skeleton (U' B2 U D B2 D B2 D') has HH corners. Apply D and NISS: FD corners.

- No variant passes the meta.

Skeleton U L2 U B2 U2 R2 D U' D has HH corners, L=9, 4 spare moves. Apply (D') and NISS: HH corners.

- No variant passes the meta.

Skeleton U2 L2 U R2 U F2 D R2 D' F2 D' has HH corners, L=11, 2 spare moves. Apply (D) and NISS: RD corners.

- No variant passes the meta.

The same skeleton in full, for the solutions that go on after its last quarter turn.

- No variant passes the meta.

Check inverse. Skeleton (D L2 U' B2 U F2 U L2 D B2 U2) has RV corners.

- No variant passes the meta.

Skeleton U2 F2 U B2 U B2 U B2 U' R2 D has HH corners, L=11, 2 spare moves. Apply (D') and NISS: RD corners.

- U2 F2 U F2 U'
    - After L2 U2 R2, 1qt edges will be RD (good) and FH (good): +0+2+0(+0)
        - L2 U2 R2 U' F2 U // no good: 4 pairs, the most of 2

The same skeleton in full, for the solutions that go on after its last quarter turn.

- No variant passes the meta.

Check inverse. Skeleton (D' R2 U B2 U' B2 U' F2 D' B2 U2) has FV corners.

- (D' R2 U F2 U)
    - After (R2 U2 L2), 1qt edges will be FV (good) and RH (good): +0+2+0(+0)
        - (R2 U2 L2 U F2 U') // no good: 6 pairs, the most of 2

8 skeletons gone through, 87 HTRs: nothing within goal. This DR's optimal is 14, over the goal.

### 4b3, scramble 4

`R' U' F R D' F2 L' D2 F2 R D2 B2 L D2 R2 B R' F L' D' R2 B F2 R' U' F`

4b3 6e, goal 13.

Skeleton U L2 U R2 U2 B2 U' F2 has RD corners, L=8, 5 spare moves.

- U
    - After B2 L2 F2 B2, 1qt edges will be RD (good) and FD (good): +0+3+1(+1)
        - B2 L2 F2 B2 U' F2 U2 F2 L2 D' // no good: 10 pairs, the most of 68

Check inverse. Skeleton (R2 D B2 U2 R2 D' F2 U') has HH corners. Apply U and NISS: RD corners.

- After (F2 R2 F2 B2), 1qt edges will be RD (good) and FD (good): +3+1(+1)
    - (F2 R2 F2 B2 U L2 U2 R2 B2 D) // no good: 10 pairs, the most of 120

The same skeleton in full, for the solutions that go on after its last quarter turn.

- (F2 R2 U')
    - After (L2 U2 R2 F2), 1qt edges will be RH (good) and FH (good): +1+1+2(+0)
        - (L2 U2 R2 F2 U' F2 R2 L2 D) // no good: 8 pairs, the most of 61

Skeleton U L2 U R2 U D L2 D' F2 has RD corners, L=9, 4 spare moves.

- No variant passes the meta.

Check inverse. Skeleton (R2 D' L2 D U R2 U F2 U') has HH corners. Apply U and NISS: RD corners.

- No variant passes the meta.

Skeleton U L2 U' B2 U D B2 D B2 has RD corners, L=9, 4 spare moves.

- No variant passes the meta.

Check inverse. Skeleton (R2 D B2 U D B2 U' B2 U') has HH corners. Apply U and NISS: RD corners.

- No variant passes the meta.

Skeleton U R2 U' F2 D U B2 D L2 has RD corners, L=9, 4 spare moves.

- U F2 R2 U L2 U'
    - After F2 B2, 1qt edges will be RD (good) and FH (good): +1+2+1(+0)
        - F2 B2 U' B2 L2 U' // no good: 6 pairs, the most of 8

Check inverse. Skeleton (L2 D' L2 D U L2 U R2 U') has HH corners. Apply U and NISS: RD corners.

- (R2 D' R2 F2 U')
    - After (R2 L2), 1qt edges will be RD (good) and FD (good): +1+2+0(+1)
        - (R2 L2 U' L2 U) // no good

Skeleton U R2 U L2 U D L2 D' R2 has RD corners, L=9, 4 spare moves.

- U B2 L2 U' R2 U
    - After F2 B2, 1qt edges will be RD (good) and FH (good): +1+2+1(+0)
        - F2 B2 U F2 L2 D' // no good: 8 pairs, the most of 8

Check inverse. Skeleton (L2 D F2 U D B2 U' L2 U') has HH corners. Apply U and NISS: RD corners.

- (L2 D R2 B2 U)
    - After (R2 L2), 1qt edges will be RD (good) and FD (good): +1+2+0(+1)
        - (R2 L2 U L2 U') // no good

Skeleton L2 D' R2 U' F2 D' L2 U R2 U' L2 has RD corners, L=11, 2 spare moves.

- R2 U' F2 R2 D R2 D
    - After R2 B2, 1qt edges will be RD (good) and FH (good): +1+1+0(+0)
        - R2 B2 U F2 U // no good

Check inverse. Skeleton (R2 U B2 U' R2 U F2 U F2 U R2) has RD corners.

- (R2 U B2 U' F2 L2 U')
    - After (B2), 1qt edges will be RD (good) and FD (good): +1+0+0(+1)
        - (B2 U' R2 U) // no good: 3 pairs, the most of 3

Skeleton B2 D' F2 D' R2 U' L2 U L2 U' B2 has RD corners, L=11, 2 spare moves.

- No variant passes the meta.

Check inverse. Skeleton (R2 U' B2 D R2 D' R2 U' B2 U' R2) has FD corners.

- (R2 U' B2 D L2 U)
    - After (R2 U2 L2), 1qt edges will be FD (good) and RH (good): +0+2+0(+0)
        - (R2 U2 L2 U F2 U') // no good

Skeleton B2 D' L2 D' B2 U' B2 D F2 D' L2 has RD corners, L=11, 2 spare moves.

- B2 D' R2 U' B2 D'
    - After R2, 1qt edges will be RD (good) and FH (good): +0+0+2(+0)
        - R2 U F2 B2 R2 D // no good: 2 pairs, the most of 4

Check inverse. Skeleton (L2 D F2 D' B2 D R2 U B2 D B2) has FD corners.

- (R2 U F2 D' B2 U)
    - After (R2), 1qt edges will be FD (good) and RH (good): +0+0+2(+0)
        - (R2 U R2 F2 B2 D') // no good: 6 pairs, the most of 5

8 skeletons gone through, 281 HTRs: nothing within goal. This DR's optimal is 14, over the goal.

### 4b3, scramble 5

`R' U' F U R F R' B2 U2 D' F' U R2 U L2 D' L2 D2 B2 R2 U2 B2 R' U' F`

4b3 2e, goal 13.

Skeleton L2 U B2 U2 R2 D' L2 D R2 has FD corners, L=9, 4 spare moves.

- B2 L2 U'
    - After B2 L2 U2 L2, 1qt edges will be FD (good) and RH (good): +1+1+1(+0)
        - B2 L2 U2 L2 U' F2 L2 U // no good: 8 pairs, the most of 17

Check inverse. Skeleton (B2 U F2 U R2 U2 B2 U' R2) has RD corners.

- (R2 F2 U')
    - After (F2), 1qt edges will be RH (bad) and FD (good): +1+0+0(+3)
        - (F2 U L2 U2 B2 D) // no good: 2 pairs, the most of 2

Skeleton (B2 U F2 U B2 U D B2 D' F2) on inverse has RD corners, L=10, 3 spare moves.

- (B2 U B2 U L2 D)
    - After (F2 L2 F2), 1qt edges will be RD (good) and FH (good): +0+3+0(+0)
        - **(F2 L2 F2 U' B2 U R2) // 13**
- (B2 U R2 F2 U' R2 U')
    - After (R2 L2), 1qt edges will be RD (good) and FH (good): +1+2+0(+0)
        - (R2 L2 U' R2 U') // no good: 6 pairs, the most of 4

Skeleton (B2 U F2 U' B2 U D B2 D L2) on inverse has RD corners, L=10, 3 spare moves.

- No variant passes the meta.

Skeleton (B2 U F2 U' R2 U D L2 D B2) on inverse has RD corners, L=10, 3 spare moves.

- (B2 U B2 U' F2 U')
    - After (B2 R2 B2), 1qt edges will be RD (good) and FH (good): +0+3+0(+0)
        - (B2 R2 B2 U B2 U) // no good: 0 pairs, the most of 2

Skeleton (B2 U F2 U R2 U D L2 D' R2) on inverse has RD corners, L=10, 3 spare moves.

- No variant passes the meta.

Skeleton L2 D' F2 D B2 U' F2 U' R2 D has HH corners, L=10, 3 spare moves. Apply (D') and NISS: FD corners.

- L2 D' F2 D
    - After B2, 1qt edges will be FD (good) and RD (good): +0+0+0(+1)
        - B2 U' F2 U // no good: 8 pairs, the most of 3

The same skeleton in full, for the solutions that go on after its last quarter turn.

- L2 U' R2 D L2 U'
    - After R2, 1qt edges will be RH (good) and FH (good): +0+0+1(+0)
        - R2 U' R2 B2 D' // no good: 16 pairs, the most of 5

Check inverse. Skeleton (D' F2 U' L2 D' F2 D F2 D' B2) has RD corners.

- (D' R2 B2 D B2 D)
    - After (F2), 1qt edges will be RD (good) and FH (good): +1+0+2(+0)
        - (F2 U' R2 L2 F2 D') // no good: 6 pairs, the most of 3

Skeleton L2 D B2 U' B2 D B2 U L2 D has HH corners, L=10, 3 spare moves. Apply (D') and NISS: RD corners.

- No variant passes the meta.

The same skeleton in full, for the solutions that go on after its last quarter turn.

- R2 D R2 U' F2 U'
    - After R2 U2 F2 R2, 1qt edges will be RH (good) and FH (good): +0+3+0(+0)
        - R2 U2 F2 R2 U L2 U' // no good

Check inverse. Skeleton (D' R2 D' F2 U' F2 U R2 U' L2) has RD corners.

- (D' R2 D' B2 U)
    - After (R2 U2 R2), 1qt edges will be RD (good) and FH (good): +0+2+0(+0)
        - (R2 U2 R2 U' R2 U) // no good

Skeleton L2 U' R2 D F2 U' F2 U' R2 D' R2 has RD corners, L=11, 2 spare moves.

- R2 D' B2 R2 U' R2 U
    - After F2, 1qt edges will be RD (good) and FH (good): +1+0+1(+0)
        - F2 U L2 B2 D' // no good: 4 pairs, the most of 3

Check inverse. Skeleton (R2 D R2 D B2 U F2 U' F2 U L2) has RD corners.

- (L2 U L2 D L2 F2 U')
    - After (L2 F2), 1qt edges will be RD (good) and FH (good): +1+1+0(+0)
        - (L2 F2 U' B2 U) // no good: 6 pairs, the most of 2

8 skeletons gone through, 44 HTRs: one finish within goal (13). This DR's optimal is 13.

### 4b3, scramble 6

`R' U' F D' R D' U' F2 D L2 F2 U R2 D F D L2 U' L F' R F2 R' U' F`

4b3 4e, goal 13.

Skeleton U2 B2 U' F2 U L2 U2 B2 U' R2 has RD corners, L=10, 3 spare moves.

- F2 U2 F2 U
    - After B2 L2, 1qt edges will be RD (good) and FH (good): +1+1+0(+0)
        - B2 L2 U B2 U2 L2 U' // no good: 1 pair, the most of 2

Check inverse. Skeleton (L2 U F2 U2 R2 D' R2 D F2 U2) has FV corners.

- (L2 U)
    - After (R2 U2 R2 B2), 1qt edges will be FV (good) and RH (good): +0+1+1(+0)
        - (R2 U2 R2 B2 U F2 L2 D') // no good: 6 pairs, the most of 8

Skeleton L2 D L2 D R2 U2 B2 U' B2 U2 has RV corners, L=10, 3 spare moves.

- F2 L2 U'
    - After R2, 1qt edges will be RD (bad) and FV (good), fr=1: +1+0+0(+2)
        - R2 U F2 U2 R2 D' // no good: 3 pairs, the most of 8

Check inverse. Skeleton (U2 R2 U B2 U2 L2 U' F2 U F2) has RD corners.

- (U2 F2 R2 D)
    - After (R2 U2 L2 B2), 1qt edges will be RD (good) and FD (good): +1+1+0(+1)
        - (R2 U2 L2 B2 U R2 U') // no good: 3 pairs, the most of 4

Skeleton D' B2 U' R2 U' F2 U L2 D' L2 U2 has RV corners, L=11, 2 spare moves.

- No variant passes the meta.

Check inverse. Skeleton (U2 R2 U R2 U' F2 D B2 D B2 D) has HH corners. Apply D' and NISS: FD corners.

- No variant passes the meta.

The same skeleton in full, for the solutions that go on after its last quarter turn.

- (L2 U2 L2 U' B2 U' R2 U)
    - After (F2 L2), 1qt edges will be RH (good) and FH (good): +1+1+0(+0)
        - (F2 L2 U' L2 U') // no good

Skeleton D' B2 U L2 U R2 D' R2 U L2 has RD corners, L=10, 3 spare moves.

- No variant passes the meta.

Check inverse. Skeleton (L2 U' R2 U R2 U' R2 U' F2 D) has HH corners. Apply D' and NISS: FD corners.

- No variant passes the meta.

The same skeleton in full, for the solutions that go on after its last quarter turn.

- (L2 U' R2 D B2 D')
    - After (B2 R2), 1qt edges will be RH (good) and FH (good): +0+1+2(+0)
        - (B2 R2 U' R2 U2 R2 U) // no good: 4 pairs, the most of 7

Skeleton D' R2 D B2 U F2 U' F2 U F2 has RD corners, L=10, 3 spare moves.

- D' F2 R2 D' L2 D'
    - After R2 L2 B2, 1qt edges will be RD (good) and FH (good): +1+2+0(+0)
        - R2 L2 B2 U L2 U // no good: 6 pairs, the most of 3

Check inverse. Skeleton (L2 U L2 U' B2 D F2 D B2 D) has HH corners. Apply D' and NISS: RD corners.

- (L2 U L2 U')
    - After (B2 R2 L2), 1qt edges will be RD (good) and FH (good): +0+2+0(+0)
        - (B2 R2 L2 U B2 U) // no good: 4 pairs, the most of 3

The same skeleton in full, for the solutions that go on after its last quarter turn.

- (R2 U F2 U' F2 R2 D')
    - After (L2 B2), 1qt edges will be RH (good) and FH (good): +1+1+0(+0)
        - (L2 B2 U B2 U') // no good: 3 pairs, the most of 2

Skeleton D' R2 D' B2 U' F2 U F2 U' B2 U2 has RV corners, L=11, 2 spare moves.

- D' R2 D' R2 B2 U
    - After R2, 1qt edges will be RV (good) and FV (good): +1+0+0(+1)
        - R2 U' F2 U // no good: 2 pairs, the most of 4

Check inverse. Skeleton (U2 R2 U' L2 U R2 U' F2 U' F2 D) has HH corners. Apply D' and NISS: RD corners.

- (U2 F2 L2 D F2 U')
    - After (R2), 1qt edges will be RD (good) and FH (good): +1+0+1(+0)
        - (R2 U R2 F2 D') // no good: 2 pairs, the most of 2

The same skeleton in full, for the solutions that go on after its last quarter turn.

- (U2 R2 U' B2 R2 U' R2 U)
    - After (B2), 1qt edges will be RH (good) and FH (good): +1+0+1(+0)
        - (B2 U F2 R2 D') // no good: 8 pairs, the most of 3

Skeleton F2 D R2 U' F2 U' L2 U B2 D' F2 has RD corners, L=11, 2 spare moves.

- No variant passes the meta.

Check inverse. Skeleton (L2 U' F2 D L2 U' R2 U' L2 D L2) has FD corners.

- No variant passes the meta.

Skeleton B2 U F2 U' L2 U' F2 U F2 U' R2 has RD corners, L=11, 2 spare moves.

- B2 U B2 D' L2 D'
    - After R2 F2 B2, 1qt edges will be RD (good) and FH (good): +0+2+0(+0)
        - R2 F2 B2 U F2 U // no good: 6 pairs, the most of 5

Check inverse. Skeleton (L2 U F2 D' B2 U B2 U F2 D' B2) has FD corners.

- (R2 U R2 D' L2 B2 D')
    - After (F2 L2), 1qt edges will be FD (good) and RH (good): +1+1+0(+0)
        - (F2 L2 U L2 U) // no good: 6 pairs, the most of 5

8 skeletons gone through, 57 HTRs: nothing within goal. This DR's optimal is 14, over the goal.

### 4b3, scramble 7

`R' U' F D R' B' D' L U' B2 R' F' U R2 U' F2 D' F2 L2 D' R2 L' D2 R' U' F`

4b3 4e, goal 13.

Skeleton U B2 U B2 U2 R2 U' R2 U2 has FV corners, L=9, 4 spare moves.

- U
    - After F2, 1qt edges will be FV (good) and RV (good): +0+0+3(+1)
        - F2 U F2 U2 L2 F2 L2 B2 U // no good: 4 pairs, the most of 8

Check inverse. Skeleton (U2 B2 U R2 U2 F2 U' F2 U') has HH corners. Apply U and NISS: FD corners.

- After (U2 R2 F2), 1qt edges will be FD (good) and RH (good): +1+3(+0)
    - (U2 R2 F2 U F2 U2 L2 F2 R2 B2 D') // no good: 4 pairs, the most of 16

The same skeleton in full, for the solutions that go on after its last quarter turn.

- (U2 R2 F2 U)
    - After (B2 U2 R2), 1qt edges will be RD (bad) and FH (good): +1+0+0(+3)
        - (B2 U2 R2 U' R2 U) // no good: 1 pair, the most of 4

Skeleton R2 U2 B2 U' L2 U F2 U2 R2 U' R2 has FD corners, L=11, 2 spare moves.

- B2 U2 L2 U'
    - After R2, 1qt edges will be FD (good) and RH (good): +0+0+2(+0)
        - R2 U' L2 F2 U2 L2 B2 U' // no good: 4 pairs, the most of 14

Check inverse. Skeleton (B2 U B2 U2 R2 U' B2 U F2 U2 R2) has DD corners.

- (F2 D)
    - After (L2 B2 U2 R2 B2), 1qt edges will be FD (good) and RV (good): +0+2+0(+0)
        - (L2 B2 U2 R2 B2 U' F2 U') // no good: 4 pairs, the most of 12

Skeleton U B2 U' R2 U D L2 D L2 U2 has FV corners, L=10, 3 spare moves.

- No variant passes the meta.

Check inverse. Skeleton (U2 B2 U F2 U D B2 D' R2 U') has HH corners. Apply U and NISS: FD corners.

- No variant passes the meta.

Skeleton U B2 U F2 U D F2 D' R2 U2 has FV corners, L=10, 3 spare moves.

- No variant passes the meta.

Check inverse. Skeleton (U2 B2 U' R2 U D R2 D L2 U') has HH corners. Apply U and NISS: FD corners.

- No variant passes the meta.

Skeleton U B2 U' F2 U D F2 D B2 U2 has FV corners, L=10, 3 spare moves.

- No variant passes the meta.

Check inverse. Skeleton (U2 B2 U' F2 U D B2 D B2 U') has HH corners. Apply U and NISS: FD corners.

- No variant passes the meta.

Skeleton U B2 U L2 U D R2 D' F2 U2 has FV corners, L=10, 3 spare moves.

- No variant passes the meta.

Check inverse. Skeleton (U2 B2 U R2 U D R2 D' F2 U') has HH corners. Apply U and NISS: FD corners.

- (U2 B2 U L2 U)
    - After (F2 R2 B2), 1qt edges will be FD (good) and RH (good): +0+3+0(+0)
        - (F2 R2 B2 U' B2 U) // no good: 2 pairs, the most of 2

Skeleton R2 U' F2 D R2 U L2 D' F2 U R2 has FD corners, L=11, 2 spare moves.

- No variant passes the meta.

Check inverse. Skeleton (B2 U L2 D' R2 U R2 U L2 D' B2) has RD corners.

- No variant passes the meta.

Skeleton R2 U' L2 D F2 U L2 U' F2 D B2 has FD corners, L=11, 2 spare moves.

- L2 D' F2 R2 D' R2 U'
    - After B2, 1qt edges will be FD (good) and RH (good): +1+0+0(+0)
        - B2 U L2 U' // no good: 5 pairs, the most of 3

Check inverse. Skeleton (B2 U' R2 U F2 U' L2 U' B2 U R2) has RD corners.

- (B2 U' R2 U L2 F2 U)
    - After (B2), 1qt edges will be RD (good) and FH (good): +1+0+0(+0)
        - (B2 U B2 U') // no good: 3 pairs, the most of 2

8 skeletons gone through, 61 HTRs: nothing within goal. This DR's optimal is 14, over the goal.

### 4b3, scramble 8

`R' U' F R' U2 L2 U' F D' L D2 L U' F R2 L2 U2 R2 B2 U' R2 U2 F2 R' U' F`

4b3 4e, goal 13.

Skeleton U2 B2 U R2 U2 B2 U' F2 U has HH corners, L=9, 4 spare moves. Apply (U') and NISS: RD corners.

- After U2 B2, 1qt edges will be RH (bad) and FH (good): +0+1(+3)
    - **U2 B2 U B2 U2 F2 L2 D F2 R2 F2 R2 U // 13**
- After F2 U2 B2, 1qt edges will be RH (bad) and FH (good): +1+0(+3)
    - **F2 U2 B2 U B2 U2 L2 D F2 R2 F2 R2 U // 13**
    - **F2 U2 B2 U' L2 U2 B2 D' B2 L2 B2 L2 U // 13**
- After R2 B2 U2 F2 R2, 1qt edges will be RD (good) and FH (good): +3+1(+0)
    - **R2 B2 U2 F2 R2 U' R2 U2 R2 B2 U L2 U // 13**
- After R2 B2 U2 B2 L2, 1qt edges will be RD (good) and FH (good): +3+1(+0)
    - R2 B2 U2 B2 L2 U L2 U2 L2 B2 U // no good: 12 pairs, the most of 229
- After L2 F2 U2 F2 R2, 1qt edges will be RD (good) and FH (good): +3+1(+0)
    - **L2 F2 U2 F2 R2 U' L2 U2 L2 F2 U R2 U // 13**
- After F2 U2 B2 L2 F2 L2, 1qt edges will be RD (good) and FH (good): +4+0(+0)
    - **F2 U2 B2 L2 F2 L2 U B2 U2 L2 D R2 U // 13**
    - **F2 U2 B2 L2 F2 L2 U' L2 U2 B2 D' L2 U // 13**

The same skeleton in full, for the solutions that go on after its last quarter turn.

- U2 F2 U
    - After R2 U2 L2 B2, 1qt edges will be RH (good) and FH (good): +0+1+3(+0)
        - R2 U2 L2 B2 U R2 L2 B2 R2 U // no good: 8 pairs, the most of 81
- U2 B2 D
    - After L2 U2 R2 F2, 1qt edges will be RH (good) and FH (good): +0+1+3(+0)
        - **L2 U2 R2 F2 U F2 R2 F2 R2 U // 13**

Check inverse. Skeleton (U' R2 U B2 U2 L2 U' F2 U2) has FV corners.

- (U')
    - After (R2), 1qt edges will be FD (bad) and RH (good), fr=1: +0+0+0(+2)
        - **(R2 U L2 U2 F2 D R2 B2 R2 F2 D2 F2) // 13**
        - **(R2 U' F2 U2 L2 D' L2 F2 L2 B2 U2 F2) // 13**
    - After (L2), 1qt edges will be FV (good) and RV (good), fr=1: +0+0+1(+2)
        - **(L2 U' B2 R2 U2 R2 U R2 F2 U2 B2 R2) // 13**
    - After (R2 F2 R2 F2), 1qt edges will be FV (good) and RH (good), fr=1: +0+3+0(+1)
        - **(R2 F2 R2 F2 U L2 U2 F2 D F2 D2 F2) // 13**
        - **(R2 F2 R2 F2 U' F2 U2 L2 D' B2 U2 F2) // 13**
    - After (R2 F2 R2 F2), 1qt edges will be FV (good) and RH (good): +0+3+1(+0)
        - **(R2 F2 R2 F2 U' F2 R2 U2 L2 D' B2 U2) // 13**
        - (R2 F2 R2 F2 U L2 F2 U2 F2 D) // no good: 8 pairs, the most of 176

Skeleton (D' F2 D B2 U2 L2 D' L2 U D) on inverse has HH corners, L=10, 3 spare moves. Apply D' and NISS: HH corners.

- (D' L2 F2 D)
    - After (L2 U2 F2), 1qt edges will be RH (good) and FH (good): +1+0+2(+0)
        - (L2 U2 F2 U L2 U2 R2 U) // no good: 8 pairs, the most of 22

The same skeleton in full, for the solutions that go on after its last quarter turn.

- No variant passes the meta.

Skeleton U2 B2 U B2 U D B2 D' R2 U has HH corners, L=10, 3 spare moves. Apply (U') and NISS: RD corners.

- No variant passes the meta.

Skeleton U2 B2 U' L2 D U R2 D L2 U has HH corners, L=10, 3 spare moves. Apply (U') and NISS: RD corners.

- No variant passes the meta.

Skeleton U2 B2 U' B2 U D B2 D B2 U has HH corners, L=10, 3 spare moves. Apply (U') and NISS: RD corners.

- No variant passes the meta.

Skeleton U2 B2 U R2 U D L2 D' F2 U has HH corners, L=10, 3 spare moves. Apply (U') and NISS: RD corners.

- No variant passes the meta.

6 skeletons gone through, 522 HTRs: 14 finishes within goal (13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13). This DR's optimal is 13.

## 0c0

### 0c0, scramble 1

`R' U' F U' L U' F' B D2 B R L F U' B2 R2 U F2 R2 D2 L2 F2 D' R' U' F`

0c0 6e, goal 12.

Skeleton U D R2 has FD corners, L=3, 9 spare moves.

- No variant passes the meta.

Check inverse. Skeleton (F2 U D) has HH corners.

- No variant passes the meta.

Skeleton B2 U D R2 U2 has FV corners, L=5, 7 spare moves.

- No variant passes the meta.

Check inverse. Skeleton (U2 B2 U D R2) has FD corners.

- No variant passes the meta.

Skeleton R2 U D B2 U2 R2 has DD corners, L=6, 6 spare moves.

- After L2, 1qt edges will be FV (good) and RV (good): +0+5(+1)
    - L2 U R2 F2 L2 F2 B2 U' // no good: 6 pairs, the most of 8

Check inverse. Skeleton (R2 U2 B2 U D R2) has RD corners.

- After (L2 U2 B2), 1qt edges will be RD (good) and FD (good): +0+5(+1)
    - (L2 U2 B2 U L2 B2 R2 F2 B2 U') // no good: 10 pairs, the most of 16

Skeleton U2 R2 U D' L2 has RD corners, L=5, 7 spare moves.

- No variant passes the meta.

Check inverse. Skeleton (R2 U D' L2 U2) has RV corners.

- After (R2), 1qt edges will be RV (good) and FD (bad), fr=1: +0+5(+2)
    - (R2 U' R2 L2 B2 R2 F2 U) // no good: 4 pairs, the most of 8

Skeleton R2 U2 F2 U D B2 U2 has RV corners, L=7, 5 spare moves.

- No variant passes the meta.

Check inverse. Skeleton (U2 R2 D U R2 U2 B2) has DD corners.

- No variant passes the meta.

Skeleton U2 F2 D U' has HH corners, L=4, 8 spare moves.

- No variant passes the meta.

Skeleton U D R2 U D' has HH corners, L=5, 7 spare moves. Apply (D) and NISS: HH corners.

- No variant passes the meta.

Check inverse. Skeleton (U D' R2 D U) has HH corners. Apply U' and NISS: HH corners.

- No variant passes the meta.

Skeleton B2 U D R2 U D has HH corners, L=6, 6 spare moves. Apply (D') and NISS: HH corners.

- F2 D'
    - After F2 L2 B2, 1qt edges will be RH (good) and FD (bad): +0+3+0(+3)
        - F2 L2 B2 U R2 U // no good: 2 pairs, the most of 7

8 skeletons gone through, 39 HTRs: nothing within goal. This DR's optimal is 13, over the goal.

### 0c0, scramble 2

`R' U' F R2 B' D' R U2 D2 L2 F2 R' B U B2 U B2 D' F2 R2 U' F2 D R' U' F`

0c0 2e, goal 12.

Skeleton U D B2 U2 R2 has DD corners, L=5, 7 spare moves.

- With no setup, 1qt edges will be FH (bad) and RD (good): +0+3(+3)
    - **U F2 R2 F2 U R2 U2 B2 L2 B2 L2 D2 // 12**
    - U F2 L2 B2 D // no good: 4 pairs, the most of 2
    - **U B2 R2 B2 U R2 U2 B2 R2 B2 R2 D2 // 12**

Check inverse. Skeleton (F2 U2 R2 U D) has HH corners.

- After (R2 F2 U2 F2), 1qt edges will be RH (good) and FD (bad): +1+3(+3)
    - (R2 F2 U2 F2 U R2 F2 R2 U') // no good: 10 pairs, the most of 16

Skeleton B2 U2 R2 U D has HH corners, L=5, 7 spare moves.

- After B2 U2 R2, 1qt edges will be RH (good) and FV (bad): +0+3(+3)
    - **B2 U2 R2 U' R2 B2 R2 U' R2 B2 R2 D2 // 12**
    - **B2 U2 R2 U' L2 B2 L2 U' L2 B2 L2 D2 // 12**
- After B2 U2 F2 R2, 1qt edges will be RH (good) and FD (bad): +1+3(+3)
    - B2 U2 F2 R2 U' L2 B2 L2 U // no good: 10 pairs, the most of 30

Check inverse. Skeleton (U D B2 U2 R2) has DD corners.

- No variant passes the meta.

Skeleton B2 D U B2 U2 has RV corners, L=5, 7 spare moves.

- After F2, 1qt edges will be RD (bad) and FV (good): +0+3(+3)
    - **F2 U B2 R2 B2 U' F2 D2 F2 L2 F2 // 11**
    - **F2 U B2 L2 F2 D R2 U2 R2 F2 U2 B2 // 12**
- After R2 B2, 1qt edges will be RV (good) and FV (good): +1+3(+1)
    - R2 B2 U' L2 F2 R2 D // no good: 10 pairs, the most of 10

Check inverse. Skeleton (U2 R2 U D R2) has FD corners.

- After (U2 F2 L2), 1qt edges will be FD (good) and RD (good): +1+3(+1)
    - (U2 F2 L2 U L2 F2 L2 U') // no good: 10 pairs, the most of 12

Skeleton U2 R2 U D R2 has FD corners, L=5, 7 spare moves.

- After U2 L2, 1qt edges will be FH (bad) and RH (good): +0+3(+3)
    - **U2 L2 U' F2 R2 F2 U R2 B2 L2 B2 // 11**
    - U2 L2 U' F2 L2 B2 D' // no good: 4 pairs, the most of 9
    - **U2 L2 U' B2 R2 B2 U L2 B2 R2 B2 // 11**
- After U2 B2 L2, 1qt edges will be FD (good) and RH (good): +1+3(+0)
    - **U2 B2 L2 U' B2 R2 B2 U L2 R2 B2 // 11**

Check inverse. Skeleton (F2 U D B2 U2) has RV corners.

- After (B2), 1qt edges will be RV (good) and FV (good): +0+3(+1)
    - **(B2 U R2 B2 R2 U' F2 B2 L2 F2 D2) // 11**
- After (R2 B2), 1qt edges will be RH (bad) and FV (good): +1+3(+3)
    - (R2 B2 U R2 B2 R2 U') // no good: 6 pairs, the most of 18
- After (F2 R2 L2), 1qt edges will be RV (good) and FV (good): +2+3(+1)
    - **(F2 R2 L2 U' F2 L2 F2 U R2 F2 D2) // 11**

Skeleton L2 U D R2 has RD corners, L=4, 8 spare moves.

- After L2, 1qt edges will be RV (bad) and FH (good), fr=1: +0+3(+5)
    - L2 U F2 L2 B2 D // no good: 8 pairs, the most of 4

Check inverse. Skeleton (L2 U D R2) has RD corners.

- After (L2), 1qt edges will be RH (bad) and FH (good), fr=1: +0+3(+5)
    - (L2 U' F2 R2 B2 D') // no good: 4 pairs, the most of 4

Skeleton U2 F2 D U B2 U2 has FV corners, L=6, 6 spare moves.

- After U2 R2 F2, 1qt edges will be FD (bad) and RH (good), fr=1: +1+3(+2)
    - U2 R2 F2 U R2 F2 R2 U // no good: 4 pairs, the most of 8

Check inverse. Skeleton (U2 F2 U D B2 U2) has FV corners.

- After (U2 F2), 1qt edges will be FD (bad) and RV (good), fr=1: +0+3(+2)
    - (U2 F2 U L2 F2 L2 U) // no good: 6 pairs, the most of 4

Skeleton B2 U D B2 D U has HH corners, L=6, 6 spare moves. Apply (U') and NISS: HH corners.

- B2 U
    - After R2 B2 R2, 1qt edges will be RD (bad) and FH (good): +0+3+0(+3)
        - R2 B2 R2 U' B2 U // no good

Skeleton (F2 U D F2 D U) on inverse has HH corners, L=6, 6 spare moves. Apply U' and NISS: HH corners.

- (B2 U)
    - After (R2 B2 R2), 1qt edges will be RH (good) and FH (good): +0+3+1(+0)
        - (R2 B2 R2 U' R2 F2 D') // no good: 8 pairs, the most of 6

8 skeletons gone through, 135 HTRs: 11 finishes within goal (11, 11, 11, 11, 11, 11, 12, 12, 12, 12, 12). This DR's optimal is 11.

## 2c3

### 2c3, scramble 1

`R' U' F U' D2 F' L B2 U2 R2 F U' F L2 F' L2 B' L2 U2 D2 B D2 R' U' F`

2c3 2e, goal 13.

Skeleton L2 U B2 U' R2 U F2 has FD corners, L=7, 6 spare moves.

- R2 U'
    - After F2 L2 U2 F2, 1qt edges will be FD (good) and RH (good): +0+3+1(+0)
        - F2 L2 U2 F2 U' R2 F2 U' // no good: 8 pairs, the most of 23

Check inverse. Skeleton (F2 U' R2 U R2 U' R2) has RD corners.

- (B2 D)
    - After (B2 L2 U2 B2), 1qt edges will be RD (good) and FV (bad): +0+3+0(+3)
        - (B2 L2 U2 B2 U F2 U') // no good: 5 pairs, the most of 11
    - After (L2 U2 L2 B2 L2 B2), 1qt edges will be RD (good) and FD (good): +0+5+0(+1)
        - **(L2 U2 L2 B2 L2 B2 U F2 U R2 B2) // 13**

Skeleton U2 R2 U' B2 U L2 U R2 U2 F2 has DD corners, L=10, 3 spare moves.

- U2 F2 L2 D
    - After F2 L2, 1qt edges will be FV (good) and RD (good): +1+1+0(+0)
        - F2 L2 U B2 U' // no good

Check inverse. Skeleton (F2 U2 R2 U' R2 U' R2 U R2 U2) has RV corners.

- (B2 U2 L2 D)
    - After (F2 B2 U2 F2), 1qt edges will be RV (good) and FH (good): +0+3+0(+0)
        - (F2 B2 U2 F2 U' L2 U') // no good: 4 pairs, the most of 8

Skeleton B2 U2 R2 U R2 U' F2 U R2 U2 has FV corners, L=10, 3 spare moves.

- R2 U2 B2 U
    - After L2 B2, 1qt edges will be FV (good) and RH (good): +0+1+1(+0)
        - L2 B2 U' R2 B2 U // no good: 6 pairs, the most of 19
- B2 U2 R2 U
    - After R2, 1qt edges will be FV (good) and RH (good): +0+0+3(+0)
        - **R2 U R2 F2 U2 L2 D F2 D2 // 13**
- B2 U2 R2 U'
    - After L2 U2 R2, 1qt edges will be FV (good) and RH (good): +0+2+1(+0)
        - **L2 U2 R2 U R2 F2 D' B2 U2 // 13**
- B2 L2 U2 R2 U'
    - After L2, 1qt edges will be FV (good) and RH (good): +1+0+1(+0)
        - **L2 U' R2 F2 D' B2 U2 // 12**

Check inverse. Skeleton (U2 F2 U L2 U' L2 U F2 U2 R2) has DD corners.

- (U2 B2 D)
    - After (F2 R2), 1qt edges will be FD (good) and RV (good): +0+1+0(+0)
        - **(F2 R2 U L2 U R2 U2 L2 B2) // 12**
    - After (F2 R2), 1qt edges will be FD (good) and RV (good): +0+1+2(+0)
        - **(F2 R2 U' R2 U2 L2 U R2 U2 B2) // 13**
- (U2 F2 U)
    - After (F2 R2), 1qt edges will be FV (good) and RD (good): +0+1+1(+0)
        - (F2 R2 U B2 L2 D) // no good: 4 pairs, the most of 8
- (U2 B2 D')
    - After (R2 U2 B2 L2), 1qt edges will be FD (good) and RV (good): +0+3+0(+0)
        - **(R2 U2 B2 L2 U' L2 U' L2 D2 B2) // 13**

Skeleton (F2 U' R2 U R2 U D U B2) on inverse has RD corners, L=9, 4 spare moves.

- No variant passes the meta.

Skeleton L2 U B2 U' R2 U D U' R2 has FD corners, L=9, 4 spare moves.

- No variant passes the meta.

Skeleton (F2 U' L2 U R2 U D' L2 D F2) on inverse has RD corners, L=10, 3 spare moves.

- No variant passes the meta.

Skeleton (F2 U' R2 U R2 U' F2 U D' F2) on inverse has FD corners, L=10, 3 spare moves.

- No variant passes the meta.

Skeleton (F2 U' L2 D L2 D' B2 U D') on inverse has HH corners, L=9, 4 spare moves. Apply D and NISS: HH corners.

- (B2 D' F2 R2 U')
    - After (B2), 1qt edges will be RH (good) and FH (good): +1+0+3(+0)
        - (B2 U' L2 F2 U2 L2 D) // no good: 8 pairs, the most of 5

The same skeleton in full, for the solutions that go on after its last quarter turn.

- No variant passes the meta.

Hard to find, on skeletons that are not gone through:

Skeleton B2 U2 R2 U L2 D' F2 U R2 D' U has HH corners, L=11, 2 spare moves. Apply (U') and NISS: HH corners.

- B2 L2 U2 R2 U' L2 D'
    - After F2 L2, 1qt edges will be RH (good) and FH (good): +1+1+0(+0)
        - **F2 L2 U' B2 U2 // 12**

8 skeletons gone through, 82 HTRs: 7 finishes within goal (12, 12, 13, 13, 13, 13, 13). This DR's optimal is 12.

### 2c3, scramble 2

`R' U' F R2 F' D' R L2 U' R2 D' F' R2 U2 F2 R2 D F2 R2 F2 U R2 D' R' U' F`

2c3 4e, goal 13.

Skeleton U2 F2 D B2 U' B2 D L2 has FD corners, L=8, 5 spare moves.

- U2 B2 D
    - After R2, 1qt edges will be FD (good) and RH (good): +0+0+5(+0)
        - R2 U R2 U2 L2 F2 L2 B2 D // no good: 8 pairs, the most of 41

Check inverse. Skeleton (F2 D L2 D' B2 U R2 U2) has FV corners.

- (F2 D)
    - After (R2), 1qt edges will be FD (bad) and RV (good), fr=1: +0+0+3(+2)
        - (R2 U R2 L2 U2 B2 D') // no good: 6 pairs, the most of 22

Skeleton F2 U' F2 D B2 D B2 U2 L2 has DD corners, L=9, 4 spare moves.

- B2 D'
    - After F2, 1qt edges will be FV (good) and RD (good): +0+0+3(+0)
        - F2 U B2 L2 F2 R2 D // no good: 4 pairs, the most of 8

Check inverse. Skeleton (L2 U2 B2 D L2 U' L2 D B2) has FD corners.

- (B2 U2 L2 U)
    - After (L2), 1qt edges will be FD (good) and RD (good): +0+0+2(+1)
        - (L2 U L2 F2 B2 D) // no good: 6 pairs, the most of 8
    - After (L2), 1qt edges will be FD (good) and RD (good): +0+0+3(+1)
        - **(L2 U L2 U2 F2 B2 D B2 R2) // 13**
        - **(L2 U' F2 B2 U2 L2 D' F2 L2) // 13**

Skeleton F2 U2 L2 U' L2 U' B2 U F2 U2 has FV corners, L=10, 3 spare moves.

- F2 R2 U2 L2 U
    - After B2 R2, 1qt edges will be FV (good) and RV (good): +1+1+0(+1)
        - B2 R2 U L2 U' // no good: 5 pairs, the most of 2

Check inverse. Skeleton (U2 B2 U' F2 D R2 D L2 U2 B2) has DD corners.

- No variant passes the meta.

Skeleton (F2 D L2 U' R2 U L2 U' D) on inverse has HH corners, L=9, 4 spare moves. Apply D' and NISS: HH corners.

- (B2 U R2 U)
    - After (F2 U2 L2 B2), 1qt edges will be RH (good) and FH (good): +0+3+0(+0)
        - (F2 U2 L2 B2 U R2 U') // no good: 4 pairs, the most of 20

The same skeleton in full, for the solutions that go on after its last quarter turn.

- No variant passes the meta.

Skeleton (F2 D L2 D' B2 U' L2 U D B2) on inverse has FD corners, L=10, 3 spare moves.

- No variant passes the meta.

Skeleton F2 U' F2 D B2 D' B2 D U B2 has RD corners, L=10, 3 spare moves.

- No variant passes the meta.

Skeleton F2 U' F2 D B2 D' R2 D U R2 U2 has RV corners, L=11, 2 spare moves.

- No variant passes the meta.

Skeleton F2 U' F2 D B2 D B2 U D F2 has FD corners, L=10, 3 spare moves.

- No variant passes the meta.

8 skeletons gone through, 103 HTRs: 2 finishes within goal (13, 13). This DR's optimal is 13.

### 2c3, scramble 3

`R' U' F R' F U2 D B R2 F2 D U2 B2 L' D2 F2 B2 R' L2 B2 U2 R2 U2 R' U' F`

2c3 2e, goal 13.

Skeleton U2 B2 U L2 U' L2 U F2 has FD corners, L=8, 5 spare moves.

- U2 L2 F2 U'
    - After L2, 1qt edges will be FD (good) and RH (good): +1+0+3(+0)
        - **L2 U F2 B2 R2 F2 D B2 // 12**
- F2 U2 B2 U'
    - After B2 L2, 1qt edges will be FD (good) and RD (good): +1+1+2(+1)
        - B2 L2 U' R2 U2 L2 U' // no good: 8 pairs, the most of 15

Check inverse. Skeleton (F2 U' L2 U F2 U' F2 U2) has FV corners.

- (B2 D')
    - After (L2), 1qt edges will be FH (bad) and RV (good): +0+0+0(+3)
        - **(L2 U B2 U' R2 B2 R2 F2 R2 U2) // 12**
    - After (F2 R2 F2 B2), 1qt edges will be FV (good) and RV (good): +0+3+0(+1)
        - **(F2 R2 F2 B2 U' L2 U F2 L2 U2) // 12**
- (F2 U')
    - After (F2 L2 F2 B2), 1qt edges will be FV (good) and RV (good): +0+3+1(+1)
        - (F2 L2 F2 B2 U' L2 F2 D') // no good: 10 pairs, the most of 30
- (R2 F2 U)
    - After (R2 B2), 1qt edges will be FV (good) and RH (good): +1+1+0(+0)
        - **(R2 B2 U B2 U' R2 L2 B2 U2) // 12**

Skeleton F2 U' L2 U L2 U' F2 U2 has FV corners, L=8, 5 spare moves.

- F2 U'
    - After B2 L2, 1qt edges will be FV (good) and RV (good): +0+1+0(+1)
        - **B2 L2 U' B2 U B2 L2 U2 R2 L2 // 12**
- L2 F2 U
    - After F2, 1qt edges will be FD (bad) and RH (good): +1+0+1(+3)
        - F2 U' L2 F2 U' // no good: 6 pairs, the most of 31

Check inverse. Skeleton (U2 B2 U F2 U' L2 U F2) has FD corners.

- (U2 B2 U)
    - After (B2), 1qt edges will be FD (good) and RD (good): +0+0+1(+1)
        - **(B2 U' R2 B2 U R2 L2 U2 F2 L2) // 13**
- (U2 R2 B2 U')
    - After (F2 R2), 1qt edges will be FH (bad) and RH (good): +1+1+0(+3)
        - (F2 R2 U' F2 U) // no good: 5 pairs, the most of 22

Skeleton L2 U2 B2 U' R2 U B2 U R2 U2 F2 has DD corners, L=11, 2 spare moves.

- L2 U2 F2 D'
    - After R2, 1qt edges will be FV (good) and RD (good): +0+0+0(+0)
        - R2 U F2 U' // no good: 4 pairs, the most of 6
- B2 U2 F2 R2 D
    - After R2, 1qt edges will be FV (good) and RV (good): +1+0+0(+1)
        - **R2 U F2 U' B2 R2 D2 L2 // 13**

Check inverse. Skeleton (F2 U2 L2 U' B2 U' R2 U F2 U2 R2) has DD corners.

- (B2 U2 L2 D')
    - After (B2), 1qt edges will be FD (good) and RD (good): +0+0+0(+2)
        - (B2 U' L2 U') // no good: 4 pairs, the most of 3
- (L2 U2 L2 F2 D)
    - After (L2), 1qt edges will be FV (good) and RV (good): +1+0+0(+1)
        - **(L2 U' F2 U' R2 F2 U2 B2) // 13**

Skeleton (F2 U' L2 U' B2 U D R2 D B2 U2) on inverse has FV corners, L=11, 2 spare moves.

- No variant passes the meta.

Skeleton (B2 U' B2 U F2 U' L2 U D) on inverse has HH corners, L=9, 4 spare moves. Apply D' and NISS: HH corners.

- (B2 U' F2 D)
    - After (F2), 1qt edges will be RH (good) and FH (good): +0+0+4(+0)
        - **(F2 U' R2 B2 L2 F2 R2 U2) // 12**
        - **(F2 U' L2 F2 L2 B2 L2 U2) // 12**
- (L2 F2 D R2 U')
    - After (F2), 1qt edges will be RH (good) and FH (good): +1+0+1(+0)
        - (F2 U R2 F2 U') // no good: 8 pairs, the most of 23

The same skeleton in full, for the solutions that go on after its last quarter turn.

- (L2 F2 U F2 U' L2 U)
    - After (F2 L2), 1qt edges will be RH (good) and FH (good): +1+1+2(+0)
        - (F2 L2 U F2 B2 D') // no good: 16 pairs, the most of 20

Skeleton (F2 U' L2 U F2 U B2 U D R2) on inverse has FD corners, L=10, 3 spare moves.

- No variant passes the meta.

Skeleton (B2 D' R2 D L2 D U' L2 D L2 U2) on inverse has FV corners, L=11, 2 spare moves.

- (F2 U' R2 U B2 D)
    - After (F2 B2), 1qt edges will be FV (good) and RH (good): +0+2+0(+0)
        - (F2 B2 U' R2 U) // no good

Skeleton F2 D' B2 D L2 U' F2 D U has HH corners, L=9, 4 spare moves. Apply (U') and NISS: HH corners.

- F2 D' R2 B2 U'
    - After R2, 1qt edges will be RH (good) and FH (good): +1+0+3(+0)
        - R2 U F2 B2 L2 F2 U' // no good: 16 pairs, the most of 25

The same skeleton in full, for the solutions that go on after its last quarter turn.

- F2 U' R2 U L2 F2 D
    - After R2, 1qt edges will be RH (good) and FH (good): +1+0+3(+0)
        - R2 U' F2 R2 B2 D // no good: 8 pairs, the most of 12

8 skeletons gone through, 198 HTRs: 10 finishes within goal (12, 12, 12, 12, 12, 12, 12, 13, 13, 13). This DR's optimal is 12.

### 2c3, scramble 4

`R' U' F U' B2 R' D B' R' D' R2 D' F' D' L2 F2 D2 L2 B2 U B2 U B2 R' U' F`

2c3 2e, goal 13.

Skeleton D' B2 D F2 U R2 U2 F2 has DD corners, L=8, 5 spare moves.

- D'
    - After F2 R2 B2 R2, 1qt edges will be FV (good) and RD (good): +0+3+0(+0)
        - **F2 R2 B2 R2 U' R2 U L2 U2 R2 F2 U2 // 13**
    - After F2 R2 B2 R2, 1qt edges will be FV (good) and RD (good): +0+3+2(+0)
        - **F2 R2 B2 R2 U L2 U2 R2 U' F2 U2 L2 // 13**
    - After F2 L2 B2 L2, 1qt edges will be FV (good) and RD (good): +0+3+2(+0)
        - F2 L2 B2 L2 U' L2 F2 B2 D' // no good: 6 pairs, the most of 45

Check inverse. Skeleton (L2 U2 F2 U' L2 U R2 D) has HH corners. Apply D' and NISS: FD corners.

- After (B2 U2 F2 R2), 1qt edges will be FH (bad) and RD (good): +1+0(+3)
    - (B2 U2 F2 R2 U R2 U) // no good: 6 pairs, the most of 69
- After (L2 U2 F2), 1qt edges will be FH (bad) and RH (good): +0+2(+3)
    - **(L2 U2 F2 U R2 U2 L2 U' R2 B2 R2 F2 D) // 13**
- After (U2 F2 R2 U2 L2), 1qt edges will be FH (bad) and RH (good): +2+0(+3)
    - **(U2 F2 R2 U2 L2 U' R2 U R2 B2 R2 F2 D) // 13**

The same skeleton in full, for the solutions that go on after its last quarter turn.

- (L2 U2 F2 U)
- (B2 U2 F2 L2 U)
    - After (F2), 1qt edges will be RH (good) and FD (bad): +1+0+1(+3)
        - (F2 U F2 R2 U) // no good: 10 pairs, the most of 135

Skeleton U2 L2 U' F2 U' F2 U F2 has FD corners, L=8, 5 spare moves.

- U2 F2 L2 U
    - After R2 F2 L2 F2, 1qt edges will be FD (good) and RH (good): +1+3+0(+0)
        - **R2 F2 L2 F2 U' R2 U B2 // 12**
- R2 U2 R2 D
    - After L2 F2, 1qt edges will be FD (good) and RD (good): +1+1+2(+1)
        - L2 F2 U' F2 U2 B2 U' // no good: 6 pairs, the most of 11

Check inverse. Skeleton (B2 D' L2 D R2 U R2 U2) has RV corners.

- (F2 U')
    - After (L2), 1qt edges will be RV (good) and FV (good): +0+0+3(+1)
        - **(L2 U B2 R2 B2 L2 U' R2 B2 D2) // 12**
        - (L2 U B2 R2 F2 R2 D') // no good: 6 pairs, the most of 18

Skeleton U2 B2 D' L2 D' B2 U L2 U2 has FV corners, L=9, 4 spare moves.

- U2 F2 U'
    - After B2 R2, 1qt edges will be FV (good) and RV (good), fr=1: +0+1+1(+2)
        - B2 R2 U B2 L2 U' // no good: 6 pairs, the most of 11

Check inverse. Skeleton (U2 F2 U R2 U' F2 U' R2 U2) has FV corners.

- (U2 R2 B2 U')
    - After (L2), 1qt edges will be FD (bad) and RV (good), fr=1: +1+0+1(+2)
        - (L2 U R2 B2 D) // no good: 6 pairs, the most of 14

Skeleton D' B2 D' B2 U D L2 D R2 U2 F2 has DD corners, L=11, 2 spare moves.

- D' B2 D' F2 D
    - After R2 L2, 1qt edges will be FV (good) and RD (good): +0+2+0(+0)
        - R2 L2 U F2 U' // no good

Check inverse. Skeleton (B2 U2 R2 U F2 U D R2 D B2 D) has HH corners. Apply D' and NISS: FD corners.

- (R2 U2 F2 U F2 U)
    - After (R2 L2), 1qt edges will be FD (good) and RH (good): +0+2+0(+0)
        - (R2 L2 U L2 U') // no good

Skeleton D' B2 D F2 U B2 U D B2 U2 has FV corners, L=10, 3 spare moves.

- No variant passes the meta.

Skeleton D' B2 D F2 U' F2 U D B2 U2 has RV corners, L=10, 3 spare moves.

- D' B2 D R2 F2 U
    - After R2, 1qt edges will be RV (good) and FH (good): +1+0+2(+0)
        - R2 U F2 B2 D // no good: 6 pairs, the most of 2

Skeleton D' B2 D R2 D U' R2 D B2 U2 L2 has DD corners, L=11, 2 spare moves.

- D' B2 D R2 D'
    - After R2 L2, 1qt edges will be FD (good) and RV (good): +0+2+0(+0)
        - R2 L2 U F2 U' // no good

Check inverse. Skeleton (L2 U2 F2 U' B2 U D' B2 D' B2 D) has HH corners. Apply D' and NISS: FD corners.

- No variant passes the meta.

Skeleton D' B2 D F2 U R2 U D R2 has FD corners, L=9, 4 spare moves.

- D' B2 D B2 D
    - After B2 R2, 1qt edges will be FD (good) and RH (good): +0+1+3(+0)
        - B2 R2 U' B2 L2 B2 U' // no good: 12 pairs, the most of 10

Hard to find, on skeletons that are not gone through:

Skeleton (B2 U' F2 U R2 U R2 U D) on inverse has HH corners, L=9, 4 spare moves. Apply D' and NISS: HH corners.

- (F2 D' B2 U)
    - After (R2 F2 R2 B2), 1qt edges will be RH (good) and FH (good): +0+3+1(+0)
        - **(R2 F2 R2 B2 U' F2 R2 U2) // 12**

Skeleton (L2 U' R2 U L2 U L2 U' R2 D') on inverse has HH corners, L=10, 3 spare moves. Apply D and NISS: FD corners.

- (L2 U' L2 U)
    - After (B2), 1qt edges will be FH (bad) and RH (good): +0+0+0(+3)
        - **(B2 U L2 U' R2 B2 R2 B2 D') // 13**

Skeleton (L2 D' F2 U B2 U B2 U' F2 D) on inverse has HH corners, L=10, 3 spare moves.

- (L2 D' B2 D B2 D)
    - After (F2), 1qt edges will be RH (good) and FH (good): +0+0+3(+0)
        - **(F2 U' B2 L2 B2 L2 U') // 13**

8 skeletons gone through, 325 HTRs: 6 finishes within goal (12, 12, 13, 13, 13, 13). This DR's optimal is 12.

### 2c3, scramble 5

`R' U' F R F R' B' L2 F' R2 D' R' U2 F2 U2 L2 D' B2 R2 U2 L2 R' B2 R' U' F`

2c3 6e, goal 13.

Skeleton U R2 U' F2 U has HH corners, L=5, 8 spare moves. Apply (U') and NISS: RD corners.

- With no setup, 1qt edges will be RD (good) and FV (bad), fr=1: +0+4(+3)
    - U R2 U2 F2 R2 F2 U // no good: 4 pairs, the most of 33

The same skeleton in full, for the solutions that go on after its last quarter turn.

- U
    - After F2 B2 L2, 1qt edges will be RD (bad) and FH (good): +0+2+3(+3)
        - F2 B2 L2 U B2 L2 U2 B2 D' // no good: 4 pairs, the most of 20

Check inverse. Skeleton (U' R2 U' F2 U') has HH corners. Apply U and NISS: RD corners.

- After (F2 B2), 1qt edges will be RD (good) and FV (bad): +2+3(+3)
    - (F2 B2 U R2 B2 U2 L2 U') // no good: 4 pairs, the most of 4

The same skeleton in full, for the solutions that go on after its last quarter turn.

- (U)
    - After (R2 U2 F2 L2 F2 B2), 1qt edges will be RH (good) and FD (bad): +0+5+0(+3)
        - (R2 U2 F2 L2 F2 B2 U' L2 U') // no good: 4 pairs, the most of 33

Skeleton U2 F2 D B2 U B2 D B2 has RD corners, L=8, 5 spare moves.

- U2 F2 D'
    - After B2 U2 L2 F2 R2 L2, 1qt edges will be RD (good) and FH (good): +0+5+0(+0)
        - B2 U2 L2 F2 R2 L2 U B2 U' // no good: 4 pairs, the most of 7

Check inverse. Skeleton (R2 U B2 U L2 U R2 U2) has FV corners.

- (R2 U)
    - After (B2), 1qt edges will be FH (bad) and RV (good), fr=1: +0+0+3(+2)
        - (B2 U L2 U2 F2 B2 D') // no good: 6 pairs, the most of 23

Skeleton U2 R2 U B2 D F2 D L2 has FD corners, L=8, 5 spare moves.

- U2 R2 U
    - After R2 F2, 1qt edges will be FD (good) and RH (good): +0+1+4(+0)
        - R2 F2 U F2 L2 U2 L2 B2 U' // no good: 6 pairs, the most of 7

Check inverse. Skeleton (F2 U R2 U R2 U F2 U2) has RV corners.

- (F2 U)
    - After (R2), 1qt edges will be RD (bad) and FV (good), fr=1: +0+0+3(+2)
        - (R2 U L2 F2 L2 B2 U) // no good: 6 pairs, the most of 16

Skeleton (U' R2 U' F2 U D' U') on inverse has HH corners, L=7, 6 spare moves. Apply U and NISS: HH corners.

- No variant passes the meta.

The same skeleton in full, for the solutions that go on after its last quarter turn.

- No variant passes the meta.

Skeleton U R2 U' B2 U D' U has HH corners, L=7, 6 spare moves. Apply (U') and NISS: HH corners.

- No variant passes the meta.

Skeleton U F2 U D' F2 D R2 U has HH corners, L=8, 5 spare moves. Apply (U') and NISS: RD corners.

- No variant passes the meta.

Check inverse. Skeleton (U' R2 U' R2 U D' L2 U') has HH corners. Apply U and NISS: FD corners.

- No variant passes the meta.

The same skeleton in full, for the solutions that go on after its last quarter turn.

- No variant passes the meta.

Skeleton U' L2 U D B2 D B2 U has HH corners, L=8, 5 spare moves. Apply (U') and NISS: RD corners.

- No variant passes the meta.

Check inverse. Skeleton (U' R2 U F2 D U R2 U) has HH corners. Apply U' and NISS: RD corners.

- No variant passes the meta.

The same skeleton in full, for the solutions that go on after its last quarter turn.

- (U' F2 R2 U' R2 U)
    - After (B2 R2 B2), 1qt edges will be RH (good) and FH (good): +1+3+1(+0)
        - (B2 R2 B2 U' L2 F2 D) // no good: 8 pairs, the most of 12

Skeleton (U' L2 D' B2 D' R2 U D' B2 U2) on inverse has FV corners, L=10, 3 spare moves.

- No variant passes the meta.

Hard to find, on skeletons that are not gone through:

Skeleton L2 D' F2 D' B2 U' L2 U B2 U' has HH corners, L=10, 3 spare moves. Apply (U) and NISS: RD corners.

- L2 D' F2 D'
    - After B2, 1qt edges will be RD (good) and FH (good): +0+0+3(+0)
        - **B2 U' L2 F2 R2 B2 D' L2 U' // 13**

Skeleton L2 U' R2 D' L2 U' F2 U L2 D has HH corners, L=10, 3 spare moves.

- L2 U' R2 D' L2 U'
    - After F2 R2 B2 L2, 1qt edges will be RH (good) and FH (good): +0+3+0(+0)
        - **F2 R2 B2 L2 U' R2 U' // 13**

Skeleton (U R2 D F2 U' F2 D' R2 U' F2) on inverse has RD corners, L=10, 3 spare moves.

- (U L2 U F2 U')
    - After (R2 B2), 1qt edges will be RD (good) and FD (good): +0+1+1(+1)
        - **(R2 B2 U B2 L2 D' R2 B2) // 13**

8 skeletons gone through, 155 HTRs: nothing within goal. This DR's optimal is 13.

### 2c3, scramble 6

`R' U' F D' F2 L2 B2 D' B2 U2 R2 U2 R2 U' R' B L U L D' R' F' R' U' F`

2c3 6e, goal 13.

Skeleton U F2 U' F2 D' has HH corners, L=5, 8 spare moves. Apply (D) and NISS: FD corners.

- After R2 L2, 1qt edges will be FD (good) and RH (good): +2+0(+0)
    - **R2 L2 U R2 U R2 U2 R2 B2 D2 R2 F2 D // 13**
- After R2 L2, 1qt edges will be FD (good) and RH (good), fr=1: +2+2(+2)
    - **R2 L2 U' L2 U2 R2 U' R2 L2 B2 D2 F2 D // 13**
- After F2 L2 B2, 1qt edges will be FD (good) and RV (bad), fr=1: +3+2(+3)
    - F2 L2 B2 U F2 U2 B2 U // no good: 6 pairs, the most of 14

The same skeleton in full, for the solutions that go on after its last quarter turn.

- U
    - After R2 L2 B2, 1qt edges will be RD (bad) and FH (good): +0+2+3(+3)
        - **R2 L2 B2 U' R2 F2 L2 F2 D F2 L2 B2 // 13**
        - **R2 L2 B2 U' R2 B2 L2 B2 D B2 L2 F2 // 13**
- U'
    - After B2 L2 B2 U2 R2, 1qt edges will be RH (good) and FD (bad): +0+4+1(+3)
        - B2 L2 B2 U2 R2 U B2 L2 D' // no good: 10 pairs, the most of 22

Check inverse. Skeleton (D F2 D B2 U') has HH corners. Apply U and NISS: FD corners.

- After (U2 R2 F2 R2), 1qt edges will be FV (bad) and RD (good): +4+1(+3)
    - (U2 R2 F2 R2 U R2 F2 D') // no good: 4 pairs, the most of 2

The same skeleton in full, for the solutions that go on after its last quarter turn.

- (D)
    - After (R2 F2), 1qt edges will be RV (bad) and FH (good): +0+1+2(+3)
        - **(R2 F2 U' B2 R2 L2 D' F2 L2 F2 U2) // 12**
    - After (L2 B2), 1qt edges will be RV (bad) and FH (good): +0+1+4(+3)
        - (L2 B2 U' R2 U2 B2 L2 B2 U') // no good: 10 pairs, the most of 45

Skeleton U2 F2 U F2 D R2 D B2 has FD corners, L=8, 5 spare moves.

- U2 F2 U
    - After L2 B2, 1qt edges will be FD (good) and RD (good): +0+1+3(+1)
        - L2 B2 U' R2 B2 R2 L2 D // no good: 10 pairs, the most of 6

Check inverse. Skeleton (F2 D' B2 U' B2 D' B2 U2) has FV corners.

- (F2 D')
    - After (L2 F2 L2 B2 R2), 1qt edges will be FV (good) and RH (good): +0+4+0(+0)
        - (L2 F2 L2 B2 R2 U' F2 U') // no good: 6 pairs, the most of 9

Skeleton U2 R2 U F2 U R2 U R2 has RD corners, L=8, 5 spare moves.

- U2 R2 U
    - After F2, 1qt edges will be RD (good) and FD (good): +0+0+2(+1)
        - F2 U R2 F2 B2 D // no good: 10 pairs, the most of 15

Check inverse. Skeleton (R2 U' L2 D' R2 D' L2 U2) has RV corners.

- (R2 U')
    - After (F2 R2), 1qt edges will be RV (good) and FV (good): +0+1+3(+1)
        - (F2 R2 U L2 F2 R2 L2 D') // no good: 10 pairs, the most of 7

Skeleton U F2 U D U R2 D' has HH corners, L=7, 6 spare moves. Apply (D) and NISS: FD corners.

- No variant passes the meta.

Check inverse. Skeleton (D F2 D U D' R2 U') has HH corners. Apply U and NISS: FD corners.

- No variant passes the meta.

Skeleton U F2 U' B2 D U D has HH corners, L=7, 6 spare moves. Apply (D') and NISS: HH corners.

- U L2 B2 D
    - After R2, 1qt edges will be RH (good) and FH (good): +1+0+3(+0)
        - R2 U' R2 B2 R2 U' // no good: 8 pairs, the most of 10

The same skeleton in full, for the solutions that go on after its last quarter turn.

- No variant passes the meta.

Skeleton (D F2 D B2 U D U) on inverse has HH corners, L=7, 6 spare moves. Apply U' and NISS: HH corners.

- (D L2 F2 D')
    - After (L2), 1qt edges will be RD (bad) and FH (good): +1+0+2(+3)
        - **(L2 U R2 L2 D B2 L2 B2 U) // 13**
        - (L2 U' R2 L2 D) // no good: 6 pairs, the most of 9

The same skeleton in full, for the solutions that go on after its last quarter turn.

- No variant passes the meta.

Skeleton U F2 U B2 U D R2 D has HH corners, L=8, 5 spare moves. Apply (D') and NISS: FD corners.

- No variant passes the meta.

The same skeleton in full, for the solutions that go on after its last quarter turn.

- No variant passes the meta.

Check inverse. Skeleton (D' B2 U D L2 U' F2 U') has HH corners. Apply U and NISS: FD corners.

- (D' F2 U)
    - After (R2 L2), 1qt edges will be FV (bad) and RH (good), fr=1: +0+2+0(+3)
        - (R2 L2 U R2 U) // no good

Skeleton U' F2 U D R2 D B2 D' has HH corners, L=8, 5 spare moves. Apply (D) and NISS: FD corners.

- U' B2 U
    - After R2 L2, 1qt edges will be FV (bad) and RH (good), fr=1: +0+2+0(+3)
        - R2 L2 U R2 U' // no good

Check inverse. Skeleton (D F2 D' F2 U D R2 U) has HH corners. Apply U' and NISS: FD corners.

- No variant passes the meta.

The same skeleton in full, for the solutions that go on after its last quarter turn.

- No variant passes the meta.

Hard to find, on skeletons that are not gone through:

Skeleton U R2 U D' L2 D R2 D' has HH corners, L=8, 5 spare moves. Apply (D) and NISS: FD corners.

- U R2 U'
    - After F2 L2 B2, 1qt edges will be FD (good) and RH (good): +0+3+0(+0)
        - **F2 L2 B2 U' B2 U' B2 L2 R2 D' // 13**

8 skeletons gone through, 147 HTRs: 6 finishes within goal (12, 13, 13, 13, 13, 13). This DR's optimal is 12.

### 2c3, scramble 7

`R' U' F U' L2 B2 L D R B' R2 D' L B' R2 U2 F' B R2 F' D2 L2 D2 R' U' F`

2c3 2e, goal 13.

Skeleton R2 U R2 U' R2 U F2 U2 R2 has DD corners, L=9, 4 spare moves.

- R2 U
    - After B2 L2, 1qt edges will be FH (bad) and RV (good): +0+1+0(+3)
        - B2 L2 U L2 U' // no good: 5 pairs, the most of 20

Check inverse. Skeleton (R2 U2 F2 U B2 U L2 U' R2) has RD corners.

- (B2 U2 R2 U)
    - After (B2 R2 L2), 1qt edges will be RD (good) and FD (good): +0+2+1(+1)
        - (B2 R2 L2 U' F2 L2 D') // no good: 10 pairs, the most of 28

Skeleton R2 U2 F2 U B2 U B2 U' R2 has RD corners, L=9, 4 spare moves.

- F2 U2 F2 L2 U'
    - After B2 R2, 1qt edges will be RD (good) and FH (good): +1+1+1(+0)
        - B2 R2 U' F2 R2 U // no good: 8 pairs, the most of 30

Check inverse. Skeleton (R2 U B2 U' R2 U F2 U2 R2) has DD corners.

- (F2 L2 D')
    - After (B2 L2), 1qt edges will be FD (good) and RV (good): +1+1+0(+0)
        - (B2 L2 U' F2 U) // no good: 4 pairs, the most of 5

Skeleton U2 R2 U' R2 U R2 U' F2 U2 has RV corners, L=9, 4 spare moves.

- U2 B2 R2 U
    - After B2, 1qt edges will be RH (bad) and FV (good), fr=1: +1+0+1(+2)
        - B2 U' R2 B2 U' // no good: 6 pairs, the most of 11

Check inverse. Skeleton (U2 R2 D' R2 D B2 U' F2 U2) has RV corners.

- (U2 B2 L2 U')
    - After (B2 U2 B2), 1qt edges will be RV (good) and FV (good): +1+2+0(+1)
        - (B2 U2 B2 U B2 U) // no good

Skeleton R2 U R2 U' R2 U' F2 U D B2 has RD corners, L=10, 3 spare moves.

- No variant passes the meta.

Skeleton R2 U R2 U' R2 U B2 U D B2 has FD corners, L=10, 3 spare moves.

- L2 U F2 U' R2 D
    - After F2, 1qt edges will be FD (good) and RH (good): +0+0+3(+0)
        - F2 U' F2 L2 F2 U' // no good: 4 pairs, the most of 4

Skeleton (R2 U B2 U' R2 U' F2 U D B2) on inverse has RD corners, L=10, 3 spare moves.

- No variant passes the meta.

Skeleton (R2 U B2 U' R2 U F2 U D B2) on inverse has FD corners, L=10, 3 spare moves.

- (L2 D F2 D' R2 D)
    - After (B2), 1qt edges will be FD (good) and RH (good): +0+0+3(+0)
        - (B2 U B2 R2 B2 U) // no good: 4 pairs, the most of 6

Skeleton U' R2 U R2 U R2 U' R2 U F2 U2 has RV corners, L=11, 2 spare moves.

- U' R2 U F2 L2 D'
    - After R2 B2, 1qt edges will be RV (good) and FH (good): +1+1+0(+0)
        - R2 B2 U' B2 U // no good: 4 pairs, the most of 2

Check inverse. Skeleton (U2 R2 U B2 U' B2 U B2 U F2 U) has HH corners. Apply U' and NISS: RD corners.

- (U2 F2 R2 U' R2 U)
    - After (F2), 1qt edges will be RD (good) and FH (good): +1+0+1(+0)
        - (F2 U' R2 F2 U) // no good: 2 pairs, the most of 2

The same skeleton in full, for the solutions that go on after its last quarter turn.

- No variant passes the meta.

8 skeletons gone through, 109 HTRs: nothing within goal. This DR's optimal is 14, over the goal.

### 2c3, scramble 8

`R' U' F D F2 L' B2 R2 U2 R' D2 R' F2 U2 R F' R' B2 R' U' R D' R' U' F`

2c3 6e, goal 13.

Skeleton U F2 U R2 U R2 has FD corners, L=6, 7 spare moves.

- No variant passes the meta.

Check inverse. Skeleton (B2 U B2 U R2 U') has HH corners. Apply U and NISS: FD corners.

- After (L2 F2), 1qt edges will be FV (bad) and RD (good), fr=1: +1+1(+3)
    - **(L2 F2 U' L2 F2 D' R2 F2 B2 D2 B2 R2 U) // 13**
- After (B2), 1qt edges will be FH (bad) and RD (good), fr=1: +0+3(+3)
    - (B2 U L2 F2 R2 L2 U') // no good: 6 pairs, the most of 18
- After (L2 F2), 1qt edges will be FV (bad) and RD (good), fr=1: +1+3(+3)
    - **(L2 F2 U' F2 B2 L2 B2 D' L2 U2 F2 L2 U) // 13**

The same skeleton in full, for the solutions that go on after its last quarter turn.

- (B2 U')
    - After (R2 B2 U2 B2 L2), 1qt edges will be RH (good) and FH (good): +0+4+0(+0)
        - (R2 B2 U2 B2 L2 U' F2 U) // no good: 6 pairs, the most of 21

Skeleton L2 U' L2 U' F2 U has HH corners, L=6, 7 spare moves. Apply (U') and NISS: RD corners.

- No variant passes the meta.

The same skeleton in full, for the solutions that go on after its last quarter turn.

- L2 U
    - After F2 R2 U2 R2 B2, 1qt edges will be RH (good) and FD (bad): +0+4+0(+3)
        - F2 R2 U2 R2 B2 U B2 U // no good: 5 pairs, the most of 12

Check inverse. Skeleton (U' R2 D' L2 D' B2) has RD corners.

- No variant passes the meta.

Skeleton B2 D' L2 U' B2 D' L2 has RD corners, L=7, 6 spare moves.

- B2 D'
    - After R2, 1qt edges will be RD (good) and FH (good): +0+0+4(+0)
        - R2 U R2 F2 B2 U2 L2 D' // no good: 4 pairs, the most of 50

Check inverse. Skeleton (R2 D L2 U F2 D B2) has FD corners.

- (R2 D)
    - After (F2 R2), 1qt edges will be FD (good) and RD (good): +0+1+4(+1)
        - (F2 R2 U F2 U2 B2 R2 L2 D) // no good: 4 pairs, the most of 23

Skeleton U F2 U R2 U D U' B2 has FD corners, L=8, 5 spare moves.

- No variant passes the meta.

Skeleton (U' R2 D' L2 D U D R2) on inverse has RD corners, L=8, 5 spare moves.

- No variant passes the meta.

Skeleton (B2 U B2 U L2 U D' U') on inverse has HH corners, L=8, 5 spare moves. Apply U and NISS: HH corners.

- No variant passes the meta.

The same skeleton in full, for the solutions that go on after its last quarter turn.

- No variant passes the meta.

Skeleton L2 U' L2 U' B2 U D' U has HH corners, L=8, 5 spare moves. Apply (U') and NISS: HH corners.

- No variant passes the meta.

The same skeleton in full, for the solutions that go on after its last quarter turn.

- No variant passes the meta.

Skeleton (R2 D L2 U F2 D U D' R2) on inverse has FD corners, L=9, 4 spare moves.

- No variant passes the meta.

8 skeletons gone through, 126 HTRs: 2 finishes within goal (13, 13). This DR's optimal is 13.

### 2c3, scramble 9

`R' U' F R2 D2 B U F U2 F D' B2 D2 B2 L' U2 L' D2 L F' R D R' U' F`

2c3 6e, goal 13.

Skeleton U2 R2 U' B2 U' R2 D' has HH corners, L=7, 6 spare moves. Apply (D) and NISS: RD corners.

- After L2 U2 R2, 1qt edges will be RH (bad) and FH (good), fr=1: +1+2(+3)
    - L2 U2 R2 U F2 R2 L2 D // no good: 8 pairs, the most of 13

The same skeleton in full, for the solutions that go on after its last quarter turn.

- U2 F2 L2 U
    - After L2 B2, 1qt edges will be RH (good) and FD (bad): +1+1+1(+3)
        - **L2 B2 U' F2 L2 U L2 F2 R2 // 13**
        - L2 B2 U' B2 R2 D' // no good: 6 pairs, the most of 10

Check inverse. Skeleton (D L2 U L2 D L2 U2) has RV corners.

- (D)
    - After (L2 U2 F2 B2), 1qt edges will be RH (bad) and FH (good): +0+3+0(+3)
        - (L2 U2 F2 B2 U' F2 U) // no good: 5 pairs, the most of 11

Skeleton U' F2 D B2 D L2 has RD corners, L=6, 7 spare moves.

- U'
    - After L2 F2, 1qt edges will be RD (good) and FH (good): +0+1+4(+0)
        - L2 F2 U' B2 U2 L2 F2 R2 D' // no good: 8 pairs, the most of 38
        - **L2 F2 U' B2 U2 R2 F2 L2 D' L2 B2 F2 // 13**

Check inverse. Skeleton (L2 U' L2 U' F2 U) has HH corners. Apply U' and NISS: FD corners.

- After (L2 F2 L2 F2), 1qt edges will be FD (good) and RH (good): +3+2(+0)
    - (L2 F2 L2 F2 U R2 L2 B2 D) // no good: 6 pairs, the most of 27

The same skeleton in full, for the solutions that go on after its last quarter turn.

- (L2 U')
    - After (B2 L2), 1qt edges will be RH (good) and FH (good): +0+1+3(+0)
        - **(B2 L2 U F2 L2 F2 B2 D' F2 B2 U2) // 13**
    - After (R2 L2 B2 R2), 1qt edges will be RH (good) and FH (good): +0+3+1(+0)
        - **(R2 L2 B2 R2 U B2 L2 D' F2 B2 U2) // 13**
- (F2 R2 U)
    - After (F2 B2 L2), 1qt edges will be RV (bad) and FH (good): +1+2+1(+3)
        - (F2 B2 L2 U R2 B2 U') // no good: 10 pairs, the most of 25
- (B2 R2 D)
    - After (R2 B2 U2 F2 B2), 1qt edges will be RH (good) and FH (good): +1+4+0(+0)
        - **(R2 B2 U2 F2 B2 U R2 U L2 R2) // 13**
- (B2 R2 D')
    - After (F2 B2 U2 L2 B2), 1qt edges will be RH (good) and FH (good): +1+4+0(+0)
        - **(F2 B2 U2 L2 B2 U' L2 U R2 L2) // 13**

Skeleton U2 B2 U' B2 U' B2 U' R2 has FD corners, L=8, 5 spare moves.

- U2 L2 F2 U
    - After L2 B2, 1qt edges will be FD (good) and RH (good): +1+1+1(+0)
        - L2 B2 U' F2 L2 U // no good: 8 pairs, the most of 37
    - After F2, 1qt edges will be FD (good) and RD (good): +1+0+3(+1)
        - **F2 U F2 L2 F2 B2 U' B2 R2 // 13**

Check inverse. Skeleton (F2 U' R2 U' R2 U' R2 U2) has FV corners.

- (F2 U')
    - After (R2), 1qt edges will be FD (bad) and RH (good), fr=1: +0+0+3(+2)
        - (R2 U F2 L2 U2 B2 U') // no good: 8 pairs, the most of 13
- (L2 F2 U)
    - After (F2 B2 R2 B2), 1qt edges will be FV (good) and RV (good): +1+3+0(+1)
        - **(F2 B2 R2 B2 U' B2 U' B2 R2 D2) // 13**

Skeleton U' F2 D B2 D U D' B2 has RD corners, L=8, 5 spare moves.

- No variant passes the meta.

Skeleton (L2 U' L2 U D U R2 U) on inverse has HH corners, L=8, 5 spare moves. Apply U' and NISS: FD corners.

- No variant passes the meta.

Skeleton (L2 U' L2 U' F2 U D U') on inverse has HH corners, L=8, 5 spare moves. Apply U and NISS: HH corners.

- (L2 U' B2 L2 U)
    - After (F2 R2), 1qt edges will be RH (good) and FH (good): +1+1+2(+0)
        - (F2 R2 U F2 B2 D') // no good: 0 pairs, the most of 4

The same skeleton in full, for the solutions that go on after its last quarter turn.

- No variant passes the meta.

Skeleton U2 L2 D' L2 U D' L2 U B2 D' has HH corners, L=10, 3 spare moves. Apply (D) and NISS: RD corners.

- U2 L2 D' R2 D
    - After F2 L2 F2, 1qt edges will be RD (good) and FH (good): +0+3+0(+0)
        - F2 L2 F2 U B2 U // no good

Check inverse. Skeleton (D L2 U B2 U D' B2 U' F2 U2) has RV corners.

- No variant passes the meta.

Skeleton U2 R2 U B2 U D L2 D L2 D' has HH corners, L=10, 3 spare moves. Apply (D) and NISS: RD corners.

- No variant passes the meta.

Check inverse. Skeleton (D L2 U' R2 U D F2 U' L2 U2) has RV corners.

- No variant passes the meta.

Hard to find, on skeletons that are not gone through:

Skeleton U2 R2 U' B2 D' F2 D' B2 D U' L2 has FD corners, L=11, 2 spare moves.

- U2 R2 U' B2 D' F2 D'
    - After F2, 1qt edges will be FD (good) and RH (good): +0+0+2(+0)
        - **F2 U' F2 B2 D F2 // 13**

8 skeletons gone through, 187 HTRs: 8 finishes within goal (13, 13, 13, 13, 13, 13, 13, 13). This DR's optimal is 13.

### 2c3, scramble 10

`R' U' F U L D2 B2 L B2 L' D2 R2 B2 L' B2 D2 B' R2 D B' R B' D R' U' F`

2c3 4e, goal 13.

Skeleton U2 F2 D B2 U' B2 D L2 has RD corners, L=8, 5 spare moves.

- U2 B2 U
    - After R2 F2, 1qt edges will be RD (good) and FH (good): +0+1+4(+0)
        - R2 F2 U' R2 B2 L2 U2 B2 D' // no good: 12 pairs, the most of 38

Check inverse. Skeleton (L2 U' B2 U B2 U' F2 U2) has FV corners.

- (L2 U')
    - After (B2 U2 L2 F2 R2), 1qt edges will be FV (good) and RH (good): +0+4+1(+0)
        - (B2 U2 L2 F2 R2 U R2 F2 U') // no good: 12 pairs, the most of 10

Skeleton B2 U' R2 U R2 U F2 U2 R2 has DD corners, L=9, 4 spare moves.

- F2 U'
    - After F2 L2 F2 L2, 1qt edges will be FD (good) and RV (good): +0+3+1(+0)
        - F2 L2 F2 L2 U' R2 B2 U // no good: 4 pairs, the most of 8

Check inverse. Skeleton (L2 U2 F2 U' L2 U' B2 U F2) has FD corners.

- (B2 U2 F2 R2 U)
    - After (R2), 1qt edges will be FV (bad) and RH (good): +1+0+0(+3)
        - (R2 U' F2 U') // no good: 6 pairs, the most of 6

Skeleton B2 U2 L2 D' R2 U' F2 D F2 U2 has RV corners, L=10, 3 spare moves.

- L2 U2 F2 D'
    - After B2 L2, 1qt edges will be RH (bad) and FH (good), fr=1: +0+1+0(+2)
        - B2 L2 U' L2 U // no good: 4 pairs, the most of 15

Check inverse. Skeleton (U2 L2 D F2 U' L2 D B2 U2 L2) has DD corners.

- No variant passes the meta.

Skeleton (L2 U' B2 U' F2 U D L2 D B2 U2) on inverse has FV corners, L=11, 2 spare moves.

- No variant passes the meta.

Skeleton (L2 U' B2 U F2 U' L2 U D) on inverse has HH corners, L=9, 4 spare moves. Apply D' and NISS: HH corners.

- (L2 U' L2 F2 U')
    - After (B2), 1qt edges will be RH (good) and FH (good): +1+0+3(+0)
        - (B2 U R2 B2 R2 F2 U) // no good: 8 pairs, the most of 9

The same skeleton in full, for the solutions that go on after its last quarter turn.

- (L2 U' F2 D F2 U')
    - After (R2 B2), 1qt edges will be RH (good) and FH (good): +0+1+3(+0)
        - (R2 B2 U R2 B2 R2 U) // no good: 8 pairs, the most of 16

Skeleton (L2 U' B2 U B2 U B2 U D R2) on inverse has FD corners, L=10, 3 spare moves.

- No variant passes the meta.

Skeleton (L2 U' B2 U L2 U D' R2 D R2 U2) on inverse has FV corners, L=11, 2 spare moves.

- No variant passes the meta.

Skeleton (L2 U' B2 U B2 U' R2 U D' L2 U2) on inverse has RV corners, L=11, 2 spare moves.

- No variant passes the meta.

8 skeletons gone through, 102 HTRs: nothing within goal. This DR's optimal is 14, over the goal.

### 2c3, scramble 11

`R' U' F R2 D' R' L' B U' F' L U2 L2 D' R2 F2 U2 L2 D2 L2 U R' B R' U' F`

2c3 4e, goal 13.

Skeleton R2 U F2 D' L2 D R2 has FD corners, L=7, 6 spare moves.

- L2 U
    - After R2, 1qt edges will be FD (good) and RH (good): +0+0+4(+0)
        - R2 U F2 L2 F2 U2 L2 U // no good: 12 pairs, the most of 58

Check inverse. Skeleton (B2 D R2 U' R2 D B2) has RD corners.

- (F2 U)
    - After (F2 B2 L2), 1qt edges will be RV (bad) and FH (good): +0+2+0(+3)
        - **(F2 B2 L2 U' F2 U' B2 R2 F2 D2 R2) // 13**
- (B2 D')
    - After (F2 R2 U2 B2), 1qt edges will be RD (good) and FD (good): +0+3+2(+1)
        - (F2 R2 U2 B2 U B2 U2 B2 U) // no good: 10 pairs, the most of 36

Skeleton U2 R2 U' B2 D L2 D' R2 U2 has FV corners, L=9, 4 spare moves.

- U2 R2 U'
    - After F2, 1qt edges will be FH (bad) and RV (good), fr=1: +0+0+2(+2)
        - F2 U' R2 U2 R2 U' // no good: 4 pairs, the most of 15

Check inverse. Skeleton (U2 F2 U' B2 U B2 U' F2 U2) has RV corners.

- (U2 L2 F2 U')
    - After (R2 U2 L2), 1qt edges will be RV (good) and FH (good), fr=1: +1+2+0(+1)
        - (R2 U2 L2 U F2 U') // no good

Skeleton (B2 D R2 U' B2 U D' F2 U' R2) on inverse has RD corners, L=10, 3 spare moves.

- (B2 D R2 U' F2 U')
    - After (B2 L2 B2), 1qt edges will be RD (good) and FH (good): +0+3+0(+0)
        - (B2 L2 B2 U' B2 U) // no good: 4 pairs, the most of 2

Skeleton (B2 D R2 U' R2 D R2 U D' R2) on inverse has FD corners, L=10, 3 spare moves.

- (B2 D R2 U' R2 D)
    - After (B2 R2), 1qt edges will be FD (good) and RH (good): +0+1+2(+0)
        - (B2 R2 U R2 L2 D') // no good: 6 pairs, the most of 6

Skeleton (B2 D L2 D L2 D U F2 D' B2) on inverse has RD corners, L=10, 3 spare moves.

- No variant passes the meta.

Skeleton (B2 U F2 U' F2 U F2 D' U') on inverse has HH corners, L=9, 4 spare moves. Apply U and NISS: HH corners.

- (B2 U L2 F2 U)
    - After (R2), 1qt edges will be RH (good) and FH (good): +1+0+1(+0)
        - (R2 U' R2 B2 D') // no good: 8 pairs, the most of 12

The same skeleton in full, for the solutions that go on after its last quarter turn.

- (F2 U F2 L2 U R2 U')
    - After (F2 L2), 1qt edges will be RH (good) and FH (good): +1+1+2(+0)
        - (F2 L2 U F2 B2 D') // no good: 8 pairs, the most of 4

Skeleton U2 R2 D R2 U' L2 D B2 U L2 D has HH corners, L=11, 2 spare moves. Apply (D') and NISS: FD corners.

- No variant passes the meta.

The same skeleton in full, for the solutions that go on after its last quarter turn.

- R2 U2 R2 U' F2 D' R2 U
    - After R2, 1qt edges will be RH (good) and FH (good): +1+0+1(+0)
        - R2 U F2 L2 D // no good: 8 pairs, the most of 2

Check inverse. Skeleton (D' F2 D F2 U R2 U' R2 U F2 U2) has RV corners.

- No variant passes the meta.

Skeleton U' R2 D L2 D L2 D' L2 D L2 U2 has FV corners, L=11, 2 spare moves.

- U' B2 L2 U' F2 U'
    - After L2, 1qt edges will be FV (good) and RH (good), fr=1: +1+0+0(+1)
        - L2 U F2 U // no good: 5 pairs, the most of 4

Check inverse. Skeleton (U2 F2 U B2 U' F2 U R2 U F2 U) has HH corners. Apply U' and NISS: RD corners.

- (F2 U2 F2 U' F2 U')
    - After (L2), 1qt edges will be RD (good) and FD (good): +1+0+0(+1)
        - (L2 U F2 U) // no good: 4 pairs, the most of 4

The same skeleton in full, for the solutions that go on after its last quarter turn.

- No variant passes the meta.

8 skeletons gone through, 145 HTRs: one finish within goal (13). This DR's optimal is 13.

### 2c3, scramble 12

`R' U' F R' U D L2 F2 B' R2 D2 L' F' B2 R' F2 R' F2 U2 R D2 F2 D2 R' U' F`

2c3 6e, goal 13.

Skeleton R2 U' F2 U R2 U' F2 has FD corners, L=7, 6 spare moves.

- B2 R2 U
    - After B2 R2, 1qt edges will be FD (good) and RD (good): +1+1+3(+1)
        - B2 R2 U B2 U2 R2 L2 D // no good: 6 pairs, the most of 58

Check inverse. Skeleton (F2 U L2 U' L2 U R2) has RD corners.

- (B2 D)
    - After (L2 F2 B2), 1qt edges will be RD (good) and FD (good): +0+2+3(+1)
        - (L2 F2 B2 U R2 L2 U2 F2 D) // no good: 10 pairs, the most of 35

Skeleton U2 R2 U F2 U' F2 U R2 U2 F2 has DD corners, L=10, 3 spare moves.

- U2 R2 U
    - After B2, 1qt edges will be FV (good) and RD (good): +0+0+3(+0)
        - B2 U F2 R2 U2 F2 U' // no good: 6 pairs, the most of 4

Check inverse. Skeleton (B2 U2 R2 U R2 D L2 D' R2 U2) has RV corners.

- (L2 U2 F2 U)
    - After (F2), 1qt edges will be RV (good) and FH (good): +0+0+3(+0)
        - (F2 U' R2 F2 R2 L2 D') // no good: 4 pairs, the most of 2

Skeleton R2 U2 F2 U' L2 D' R2 D F2 U2 has FV corners, L=10, 3 spare moves.

- No variant passes the meta.

Check inverse. Skeleton (U2 B2 U' F2 U R2 U F2 U2 R2) has DD corners.

- (U2 F2 D')
    - After (R2 L2 B2), 1qt edges will be FV (good) and RD (good): +0+2+0(+0)
        - (R2 L2 B2 U L2 U') // no good

Skeleton R2 U' F2 U B2 U D' F2 D R2 has FD corners, L=10, 3 spare moves.

- L2 D' B2 U L2 U
    - After R2 L2, 1qt edges will be FD (good) and RH (good): +0+2+0(+0)
        - R2 L2 U' L2 U // no good

Skeleton R2 U' F2 U' R2 U D B2 D B2 has FD corners, L=10, 3 spare moves.

- No variant passes the meta.

Skeleton R2 U' F2 D F2 U' F2 D U' has HH corners, L=9, 4 spare moves. Apply (U) and NISS: HH corners.

- B2 L2 D R2 U'
    - After F2 L2 B2 L2, 1qt edges will be RH (good) and FH (good): +1+3+0(+0)
        - F2 L2 B2 L2 U' R2 U' // no good: 6 pairs, the most of 5

The same skeleton in full, for the solutions that go on after its last quarter turn.

- R2 U' L2 B2 D' B2 D
    - After R2, 1qt edges will be RH (good) and FH (good): +1+0+3(+0)
        - R2 U R2 F2 R2 U' // no good: 0 pairs, the most of 4

Skeleton R2 U' F2 U R2 U' R2 U D' L2 has RD corners, L=10, 3 spare moves.

- No variant passes the meta.

Skeleton (B2 D R2 U B2 U D R2 U' L2) on inverse has RD corners, L=10, 3 spare moves.

- No variant passes the meta.

8 skeletons gone through, 110 HTRs: nothing within goal. This DR's optimal is 14, over the goal.

## 2c4

### 2c4, scramble 1

`R' U' F U' F' U' D2 L' B2 U' F' D2 R D2 L2 U2 L B2 R' B2 U2 B2 U' R' U' F`

2c4 6e, goal 14.

Skeleton R2 D R2 U' B2 D B2 U B2 U2 has FV corners, L=10, 4 spare moves.

- B2 R2 D' F2 U
    - After R2 F2, 1qt edges will be FV (good) and RH (good): +1+1+2(+0)
        - R2 F2 U' B2 U2 B2 U' // no good: 12 pairs, the most of 11

Check inverse. Skeleton (U2 F2 U' R2 D' B2 D F2 U' R2) has RD corners.

- (U2 F2 U' F2 R2 U)
    - After (B2), 1qt edges will be RD (good) and FH (good): +1+0+3(+0)
        - (B2 U F2 L2 U2 B2 U') // no good: 8 pairs, the most of 10

Skeleton R2 D' R2 U F2 D' F2 U' B2 U2 has RV corners, L=10, 4 spare moves.

- L2 U' L2 U
    - After R2 B2, 1qt edges will be RV (good) and FH (good): +0+1+1(+0)
        - R2 B2 U F2 R2 U' // no good: 2 pairs, the most of 6

Check inverse. Skeleton (U2 L2 D' B2 U' L2 D L2 U' F2) has RD corners.

- (U2 R2 U' B2 D')
    - After (F2), 1qt edges will be RD (good) and FD (good): +0+0+3(+1)
        - (F2 U L2 F2 R2 B2 D) // no good: 10 pairs, the most of 11

Skeleton U2 L2 D L2 U' B2 U F2 D B2 U2 has RV corners, L=11, 3 spare moves.

- U2 R2 U R2 D'
    - After B2 L2 F2 B2, 1qt edges will be RV (good) and FH (good): +0+3+0(+0)
        - B2 L2 F2 B2 U' B2 U // no good: 4 pairs, the most of 2

Check inverse. Skeleton (U2 L2 D B2 U R2 D' R2 U F2 U2) has RV corners.

- (R2 U2 R2 U' B2 D)
    - After (R2 B2), 1qt edges will be RV (good) and FH (good), fr=1: +1+1+0(+1)
        - (R2 B2 U L2 U') // no good

Skeleton U2 L2 D' R2 U R2 U' B2 D' B2 U2 has FV corners, L=11, 3 spare moves.

- U2 F2 L2 D F2 U'
    - After L2, 1qt edges will be FV (good) and RH (good), fr=1: +1+0+1(+1)
        - L2 U B2 R2 D // no good: 10 pairs, the most of 6

Check inverse. Skeleton (U2 F2 U R2 D B2 U' B2 D L2 U2) has RV corners.

- (U2 F2 U F2 R2 U')
    - After (B2), 1qt edges will be RV (good) and FH (good), fr=1: +1+0+1(+1)
        - (B2 U F2 R2 D') // no good: 10 pairs, the most of 4

Skeleton R2 U F2 U2 L2 U' R2 U' F2 U has HH corners, L=10, 4 spare moves. Apply (U') and NISS: FD corners.

- R2 U
    - After F2 R2 U2 B2 R2, 1qt edges will be FD (good) and RD (good): +0+2+1(+1)
        - F2 R2 U2 B2 R2 U' F2 R2 U' // no good: 10 pairs, the most of 20

The same skeleton in full, for the solutions that go on after its last quarter turn.

- L2 U B2 U2 R2 D'
    - After R2 B2, 1qt edges will be RH (good) and FH (good): +0+1+2(+0)
        - R2 B2 U' L2 F2 B2 D // no good: 8 pairs, the most of 62

Check inverse. Skeleton (U' F2 U R2 U F2 U2 R2 U' R2) has RD corners.

- (U' R2 F2 U')
    - After (F2 R2 L2), 1qt edges will be RD (good) and FH (good): +1+2+1(+0)
        - (F2 R2 L2 U F2 U2 F2 L2 U) // no good: 6 pairs, the most of 24

Skeleton U2 L2 U B2 U2 R2 U' L2 U' F2 U' has HH corners, L=11, 3 spare moves. Apply (U) and NISS: RD corners.

- U2 B2 R2 U'
    - After R2 L2 F2 U2 R2, 1qt edges will be RD (good) and FH (good): +1+2+0(+0)
        - **R2 L2 F2 U2 R2 U L2 U L2 U' // 14**
- U2 B2 R2 U
    - After R2 U2 B2 R2 L2, 1qt edges will be RD (good) and FH (good): +1+2+0(+0)
        - R2 U2 B2 R2 L2 U' B2 U' // no good: 10 pairs, the most of 16
    - After L2 U2 R2 L2 F2, 1qt edges will be RD (good) and FH (good): +1+2+0(+0)
        - **L2 U2 R2 L2 F2 U' L2 U L2 U' // 14**

The same skeleton in full, for the solutions that go on after its last quarter turn.

- U2 L2 D R2 U2 F2 U'
    - After B2, 1qt edges will be RH (good) and FH (good): +0+0+3(+0)
        - B2 U' F2 B2 L2 B2 D // no good: 8 pairs, the most of 17

Check inverse. Skeleton (U L2 U' L2 U L2 U2 F2 U' R2 U2) has RV corners.

- (U L2 U')
    - After (L2), 1qt edges will be RV (good) and FV (good), fr=1: +0+0+1(+2)
        - (L2 U F2 R2 U2 L2 U') // no good: 8 pairs, the most of 17
        - **(L2 U F2 L2 U2 L2 U' R2 B2 U2 L2) // 14**
    - After (L2), 1qt edges will be RV (good) and FV (good): +0+0+2(+1)
        - **(L2 U F2 R2 L2 U2 L2 U' R2 B2 U2) // 14**
        - **(L2 U' R2 U2 F2 R2 L2 U R2 B2 U2) // 14**

Skeleton (U' F2 U R2 U F2 D U B2 D' R2) on inverse has RD corners, L=11, 3 spare moves.

- No variant passes the meta.

Skeleton (U' F2 U R2 U' R2 U D R2 D L2) on inverse has RD corners, L=11, 3 spare moves.

- No variant passes the meta.

8 skeletons gone through, 212 HTRs: 5 finishes within goal (14, 14, 14, 14, 14). This DR's optimal is 14.

### 2c4, scramble 2

`R' U' F R F U F D' F' U2 R' U' R' U2 F2 D2 B2 R2 B2 U R2 F2 B2 R' U' F`

2c4 6e, goal 14.

Skeleton F2 D' L2 U F2 D' R2 U L2 has FD corners, L=9, 5 spare moves.

- B2 U' R2 U
    - After F2 L2, 1qt edges will be FD (good) and RD (good): +0+1+3(+1)
        - F2 L2 U B2 R2 F2 B2 D' // no good: 6 pairs, the most of 34

Check inverse. Skeleton (F2 U F2 U' R2 U R2 U' R2) has FD corners.

- (B2 D F2 U')
    - After (F2 R2 F2 R2), 1qt edges will be FD (good) and RH (good): +0+3+2(+0)
        - (F2 R2 F2 R2 U' R2 L2 B2 D) // no good: 8 pairs, the most of 47

Skeleton L2 U2 B2 D' F2 U F2 U' R2 D F2 has FD corners, L=11, 3 spare moves.

- L2 U2 B2 D' L2 B2 U'
    - After R2 F2, 1qt edges will be FD (good) and RD (good): +1+1+0(+1)
        - R2 F2 U' F2 U // no good: 6 pairs, the most of 4

Check inverse. Skeleton (B2 D' F2 U B2 U' F2 D F2 U2 R2) has DD corners.

- (F2 U' F2 U)
    - After (F2 R2), 1qt edges will be FD (good) and RV (good): +0+1+1(+0)
        - (F2 R2 U F2 R2 U') // no good: 4 pairs, the most of 10

Skeleton B2 U L2 U' B2 U L2 U' R2 U2 has FV corners, L=10, 4 spare moves.

- F2 D L2 U'
    - After F2, 1qt edges will be FV (good) and RH (good): +0+0+4(+0)
        - F2 U R2 U2 B2 L2 B2 U' // no good: 4 pairs, the most of 15

Check inverse. Skeleton (U2 F2 D' F2 U R2 U' L2 D R2) has FD corners.

- (U2 F2 D' F2 U)
    - After (R2), 1qt edges will be FD (good) and RD (good): +0+0+3(+1)
        - (R2 U' L2 F2 R2 F2 D') // no good: 10 pairs, the most of 15

Skeleton L2 U2 B2 D F2 U' F2 U L2 D' F2 U2 has FV corners, L=12, 2 spare moves.

- L2 U2 B2 D B2 U'
    - After F2 R2, 1qt edges will be FV (good) and RV (good): +0+1+0(+1)
        - F2 R2 U' F2 U // no good

Check inverse. Skeleton (U2 B2 U F2 U' F2 D R2 D B2 U2 L2) has DD corners.

- No variant passes the meta.

Skeleton U2 B2 D R2 U' R2 U R2 U2 B2 D' F2 has FD corners, L=12, 2 spare moves.

- U2 B2 D F2 L2 U
    - After R2, 1qt edges will be FD (good) and RH (good): +1+0+0(+0)
        - R2 U L2 U2 B2 D' // no good: 4 pairs, the most of 2

Check inverse. Skeleton (B2 D B2 U2 L2 U' B2 U' L2 D L2 U2) has FV corners.

- (F2 U F2 U2 R2 U')
    - After (R2), 1qt edges will be FV (good) and RV (good), fr=1: +0+0+0(+2)
        - (R2 U' R2 U') // no good: 2 pairs, the most of 5

Skeleton L2 U' R2 D L2 D' F2 U B2 U' R2 U' has HH corners, L=12, 2 spare moves. Apply (U) and NISS: RD corners.

- R2 D' B2 L2 D' F2 D
    - After B2, 1qt edges will be RD (good) and FD (good): +1+0+0(+1)
        - B2 U' F2 U' // no good

The same skeleton in full, for the solutions that go on after its last quarter turn.

- L2 U' F2 L2 D' R2 U R2 D'
    - After L2 B2, 1qt edges will be RH (good) and FH (good): +1+1+0(+0)
        - L2 B2 U' F2 U // no good: 6 pairs, the most of 2

Check inverse. Skeleton (U R2 U B2 U' F2 U B2 U' R2 U R2) has RD corners.

- No variant passes the meta.

Skeleton L2 U R2 U' R2 U F2 U' F2 U R2 U' has HH corners, L=12, 2 spare moves. Apply (U) and NISS: RD corners.

- No variant passes the meta.

The same skeleton in full, for the solutions that go on after its last quarter turn.

- R2 D R2 U' F2 D F2 U'
    - After B2 L2, 1qt edges will be RH (good) and FH (good): +0+1+1(+0)
        - B2 L2 U' L2 F2 D' // no good: 8 pairs, the most of 8

Check inverse. Skeleton (U R2 U' F2 U F2 U' R2 U R2 U' R2) has RD corners.

- No variant passes the meta.

Skeleton U L2 U R2 D F2 U' L2 U R2 D L2 has FD corners, L=12, 2 spare moves.

- No variant passes the meta.

Check inverse. Skeleton (B2 U R2 U B2 U' L2 U L2 U F2 U') has HH corners. Apply U and NISS: RD corners.

- No variant passes the meta.

The same skeleton in full, for the solutions that go on after its last quarter turn.

- No variant passes the meta.

8 skeletons gone through, 144 HTRs: nothing within goal. This DR's optimal is 15, over the goal.

### 2c4, scramble 3

`R' U' F R2 F R2 B2 L2 F L2 B' L2 R2 D2 F2 U F R' D' B D2 B' F' R' U' F`

2c4 0e, goal 14.

Skeleton B2 D' B2 D B2 D' B2 D R2 U2 F2 has DD corners, L=11, 3 spare moves.

- F2 U' L2 B2 U'
    - After R2, 1qt edges will be FD (good) and RV (good): +1+0+1(+0)
        - R2 U L2 B2 U // no good: 6 pairs, the most of 32

Check inverse. Skeleton (F2 U2 R2 U F2 U F2 U' F2 U F2) has FD corners.

- (F2 U2 R2 U B2 U)
    - After (L2), 1qt edges will be FD (good) and RD (good): +0+0+2(+1)
        - (L2 U B2 U2 B2 U') // no good: 10 pairs, the most of 32

Skeleton B2 D F2 D' R2 U L2 U' R2 U2 has FV corners, L=10, 4 spare moves.

- B2 D L2 B2 U
    - After F2, 1qt edges will be FD (bad) and RV (good), fr=1: +1+0+1(+2)
        - **F2 U' R2 F2 U L2 D2 F2 L2 // 14**
- F2 U R2 B2 U
    - After R2, 1qt edges will be FV (good) and RH (good), fr=1: +1+0+1(+1)
        - R2 U' F2 L2 D // no good: 6 pairs, the most of 45

Check inverse. Skeleton (U2 B2 D' L2 D R2 U' L2 U R2) has FD corners.

- (F2 U2 F2 U L2 U)
    - After (F2), 1qt edges will be FV (bad) and RH (good): +1+0+0(+3)
        - (F2 U' L2 U') // no good: 4 pairs, the most of 12

Skeleton U2 B2 U' B2 U L2 U' B2 U R2 U2 has FV corners, L=11, 3 spare moves.

- U2 B2 U' B2 U
    - After L2, 1qt edges will be FH (bad) and RV (good), fr=1: +0+0+0(+2)
        - L2 U' B2 U // no good: 6 pairs, the most of 16

Check inverse. Skeleton (U2 B2 D L2 D' L2 D L2 D' R2 U2) has FV corners.

- (U2 R2 B2 D' B2 D)
    - After (R2), 1qt edges will be FH (bad) and RH (good), fr=1: +1+0+0(+2)
        - (R2 U' L2 U) // no good: 5 pairs, the most of 32

Skeleton U2 B2 U B2 U' R2 U B2 U R2 U2 F2 has DD corners, L=12, 2 spare moves.

- U2 B2 U F2 U'
    - After R2 F2, 1qt edges will be FV (good) and RV (good): +0+1+0(+1)
        - R2 F2 U' R2 U // no good: 6 pairs, the most of 6

Check inverse. Skeleton (F2 U2 R2 U' B2 U' L2 D F2 D' F2 U2) has FV corners.

- (R2 U2 F2 U' R2 U)
    - After (F2 R2), 1qt edges will be FV (good) and RV (good): +0+1+0(+1)
        - (F2 R2 U F2 U') // no good: 8 pairs, the most of 4

Skeleton U2 B2 U L2 U2 B2 U' B2 U B2 U' R2 has FD corners, L=12, 2 spare moves.

- U2 F2 D' L2 F2 U2 F2 U'
    - After R2, 1qt edges will be FD (good) and RH (good): +1+0+1(+0)
        - R2 U' F2 L2 D' // no good: 2 pairs, the most of 4

Check inverse. Skeleton (F2 U' F2 U R2 U R2 U2 F2 U' F2 U2) has FV corners.

- (F2 U' L2 B2 U')
    - After (L2), 1qt edges will be FV (good) and RH (good): +1+0+1(+0)
        - (L2 U' R2 U2 R2 F2 D') // no good: 2 pairs, the most of 4

Skeleton B2 D B2 U2 L2 U' F2 U' B2 D L2 has FD corners, L=11, 3 spare moves.

- B2 D L2 F2 U2 F2 U
    - After B2, 1qt edges will be FD (good) and RD (good): +1+0+1(+1)
        - B2 U R2 B2 U // no good: 4 pairs, the most of 4

Check inverse. Skeleton (F2 U R2 U' F2 U R2 U2 F2 U' R2) has FD corners.

- (F2 U B2 L2 U)
    - After (B2), 1qt edges will be FD (good) and RD (good): +1+0+1(+1)
        - **(B2 U R2 U2 L2 B2 U B2 L2) // 14**
        - (B2 U R2 U2 R2 F2 D') // no good: 6 pairs, the most of 3

Skeleton B2 D' B2 D B2 D' B2 D' R2 U D L2 has FD corners, L=12, 2 spare moves.

- No variant passes the meta.

Skeleton B2 D' B2 D B2 D' B2 D R2 D U R2 has RD corners, L=12, 2 spare moves.

- No variant passes the meta.

Hard to find, on skeletons that are not gone through:

Skeleton U R2 U F2 D B2 D' R2 U F2 U R2 U2 F2 has DD corners, L=14, 0 spare moves.

- U R2 U F2 D B2 D'
    - After R2, 1qt edges will be FD (good) and RV (good): +0+0+0(+0)
        - **R2 U F2 U' L2 D2 F2 // 14**

Skeleton (F2 U2 R2 D R2 U' L2 D L2 U' R2 U' L2 U') on inverse has HH corners, L=14, 0 spare moves. Apply U and NISS: RD corners.

- (F2 U2 R2 D L2 D' L2 U)
    - After (L2), 1qt edges will be RD (good) and FH (good): +0+0+0(+0)
        - **(L2 U' B2 U' L2 U') // 14**

Skeleton (F2 U2 R2 U F2 U' B2 D B2 U' F2 U' B2 D') on inverse has HH corners, L=14, 0 spare moves.

- (F2 U2 R2 U B2 U' L2 D F2 D')
    - After (B2), 1qt edges will be RH (good) and FH (good): +0+0+0(+0)
        - **(B2 U' L2 U') // 14**

8 skeletons gone through, 196 HTRs: 2 finishes within goal (14, 14). This DR's optimal is 14.

### 2c4, scramble 4

`R' U' F L U2 R L2 F' L B' D L F2 R2 U2 L' U2 L' B2 R' U2 L' B R' U' F`

2c4 2e, goal 14.

Skeleton F2 U' R2 U B2 D' F2 D' B2 U2 has RV corners, L=10, 4 spare moves.

- L2 F2 U F2 U'
    - After R2 B2, 1qt edges will be RV (good) and FH (good): +1+1+2(+0)
        - R2 B2 U F2 U2 F2 U // no good: 6 pairs, the most of 3

Check inverse. Skeleton (U2 R2 D' F2 D' F2 D F2 D' L2) has FD corners.

- (R2 U2 L2 U F2 U')
    - After (R2 F2), 1qt edges will be FD (good) and RH (good): +1+1+1(+0)
        - (R2 F2 U' F2 R2 U') // no good: 6 pairs, the most of 18

Skeleton F2 U R2 U' F2 U R2 U F2 U2 has FV corners, L=10, 4 spare moves.

- F2 U L2 U'
    - After B2 L2, 1qt edges will be FV (good) and RH (good): +0+1+2(+0)
        - B2 L2 U' B2 R2 L2 D' // no good: 6 pairs, the most of 12

Check inverse. Skeleton (U2 F2 D' L2 D' B2 U R2 U' B2) has FD corners.

- (U2 B2 U' R2 U')
    - After (B2 L2 B2 L2), 1qt edges will be FD (good) and RD (good): +0+3+0(+1)
        - (B2 L2 B2 L2 U' L2 U') // no good: 5 pairs, the most of 13
- (U2 B2 U' L2 U')
    - After (F2 R2), 1qt edges will be FH (bad) and RH (good): +0+1+0(+3)
        - **(F2 R2 U' L2 U L2 F2 L2 B2) // 14**
    - After (R2 F2 R2 F2), 1qt edges will be FD (good) and RD (good): +0+3+0(+1)
        - **(R2 F2 R2 F2 U' L2 U B2 R2) // 14**

Skeleton R2 U2 F2 D F2 D' F2 U L2 U R2 U2 has FV corners, L=12, 2 spare moves.

- R2 U2 F2 D F2 D'
    - After R2 L2 B2, 1qt edges will be FV (good) and RH (good): +0+2+0(+0)
        - R2 L2 B2 U B2 U // no good: 5 pairs, the most of 2

Check inverse. Skeleton (U2 F2 D L2 U L2 U' F2 D L2 U2 B2) has DD corners.

- (B2 U2 F2 D' L2 U)
    - After (R2), 1qt edges will be FV (good) and RD (good): +1+0+1(+0)
        - (R2 U' B2 L2 D) // no good: 6 pairs, the most of 3

Skeleton R2 U2 F2 U L2 U2 F2 U' L2 U' F2 U' has HH corners, L=12, 2 spare moves. Apply (U) and NISS: RD corners.

- R2 U2 B2 U'
    - After B2 R2 U2 R2, 1qt edges will be RD (good) and FD (good): +0+1+0(+1)
        - B2 R2 U2 R2 U' R2 U // no good: 2 pairs, the most of 2

The same skeleton in full, for the solutions that go on after its last quarter turn.

- R2 U2 F2 D R2 B2 U2 B2 U
    - After B2, 1qt edges will be RH (good) and FH (good): +1+0+0(+0)
        - B2 U L2 U' // no good

Check inverse. Skeleton (U R2 U' L2 U R2 U2 F2 U F2 U2 R2) has DD corners.

- (U F2 L2 U)
    - After (L2), 1qt edges will be FV (good) and RD (good): +1+0+0(+0)
        - (L2 U L2 U2 F2 U') // no good: 4 pairs, the most of 6

Skeleton B2 U R2 U2 F2 U' L2 U R2 U has HH corners, L=10, 4 spare moves. Apply (U') and NISS: FD corners.

- R2 B2 U
    - After R2 F2 U2 B2, 1qt edges will be FD (good) and RH (good): +1+1+2(+0)
        - R2 F2 U2 B2 U L2 F2 B2 D // no good: 8 pairs, the most of 48

The same skeleton in full, for the solutions that go on after its last quarter turn.

- F2 U B2 U2 L2 U'
    - After B2, 1qt edges will be RH (good) and FH (good): +0+0+3(+0)
        - B2 U' F2 L2 U2 F2 U // no good: 8 pairs, the most of 35

Check inverse. Skeleton (U' B2 U R2 D L2 U2 B2 D' R2) has FD corners.

- (U' F2 U)
    - After (B2 L2 F2 L2), 1qt edges will be FD (good) and RH (good): +0+3+1(+0)
        - (B2 L2 F2 L2 U' B2 U2 F2 R2 D) // no good: 8 pairs, the most of 32

Skeleton R2 U2 F2 D' B2 D L2 U' F2 U' R2 U2 has RV corners, L=12, 2 spare moves.

- F2 U2 R2 D' R2 U'
    - After L2, 1qt edges will be RV (good) and FH (good): +0+0+1(+0)
        - L2 U F2 L2 U // no good: 6 pairs, the most of 6

Check inverse. Skeleton (U2 R2 D B2 U B2 D' B2 U F2 U2 R2) has DD corners.

- (U2 F2 R2 D' L2 D')
    - After (B2), 1qt edges will be FV (good) and RD (good): +1+0+0(+0)
        - (B2 U R2 U') // no good: 4 pairs, the most of 2

Skeleton (U' B2 U R2 D R2 U D R2 U' L2) on inverse has FD corners, L=11, 3 spare moves.

- No variant passes the meta.

Skeleton (U' B2 U R2 D' F2 U D B2 U R2) on inverse has FD corners, L=11, 3 spare moves.

- No variant passes the meta.

8 skeletons gone through, 185 HTRs: 2 finishes within goal (14, 14). This DR's optimal is 14.

### 2c4, scramble 5

`R' U' F U2 D2 R D F L2 U2 F D' L B2 R' D2 B2 R D2 L' F2 L B2 R' U' F`

2c4 6e, goal 14.

Skeleton F2 U' L2 D R2 D' L2 U F2 U2 has RV corners, L=10, 4 spare moves.

- B2 D' R2 U
    - After R2, 1qt edges will be RV (good) and FH (good): +0+0+3(+0)
        - R2 U' L2 B2 R2 L2 U' // no good: 4 pairs, the most of 10

Check inverse. Skeleton (U2 L2 U F2 U' L2 U F2 U' R2) has FD corners.

- (U2 L2 U B2 D')
    - After (R2), 1qt edges will be FD (good) and RH (good): +0+0+3(+0)
        - (R2 U L2 F2 L2 F2 U') // no good: 12 pairs, the most of 17

Skeleton F2 U R2 U' L2 U F2 U F2 U2 R2 has DD corners, L=11, 3 spare moves.

- F2 U R2 U'
    - After L2, 1qt edges will be FD (good) and RV (good): +0+0+3(+0)
        - L2 U F2 B2 R2 F2 D' // no good: 6 pairs, the most of 17

Check inverse. Skeleton (B2 U2 L2 U' F2 D F2 U' F2 D L2) has FD corners.

- (R2 U2 F2 U' R2 U')
    - After (R2 F2), 1qt edges will be FD (good) and RH (good): +0+1+1(+0)
        - (R2 F2 U' L2 B2 D) // no good: 6 pairs, the most of 12

Skeleton F2 U2 L2 D' R2 U' F2 D L2 U' F2 U2 has RV corners, L=12, 2 spare moves.

- No variant passes the meta.

Check inverse. Skeleton (U2 L2 U' B2 D R2 U' F2 D B2 U2 L2) has DD corners.

- No variant passes the meta.

Skeleton F2 U B2 U2 L2 D' L2 D R2 U' F2 has RD corners, L=11, 3 spare moves.

- F2 U R2 U2 F2 U'
    - After L2, 1qt edges will be RV (bad) and FH (good): +0+0+0(+3)
        - L2 U' L2 U' // no good: 6 pairs, the most of 12
- F2 U R2 B2 U2 F2 U
    - After R2, 1qt edges will be RD (good) and FH (good): +1+0+2(+0)
        - **R2 U L2 U2 R2 U' L2 // 14**

Check inverse. Skeleton (L2 U' B2 D F2 D L2 U2 B2 U' L2) has FD corners.

- (R2 U' R2 U)
    - After (R2), 1qt edges will be FD (good) and RH (good), fr=1: +0+0+0(+3)
        - (R2 U R2 U2 F2 U) // no good: 6 pairs, the most of 47
- (R2 U' R2 U')
    - After (L2 U2 R2), 1qt edges will be FD (good) and RH (good): +0+2+1(+0)
        - **(L2 U2 R2 U B2 U2 F2 L2 U' B2) // 14**

Skeleton F2 U' L2 U F2 U' R2 U R2 D' U has HH corners, L=11, 3 spare moves. Apply (U') and NISS: HH corners.

- B2 D' R2 D B2 U'
    - After F2 L2 F2 B2, 1qt edges will be RH (good) and FH (good): +0+3+0(+0)
        - F2 L2 F2 B2 U' B2 U' // no good: 4 pairs, the most of 8

The same skeleton in full, for the solutions that go on after its last quarter turn.

- No variant passes the meta.

Skeleton F2 U R2 U' L2 U F2 U' B2 U D B2 has FD corners, L=12, 2 spare moves.

- No variant passes the meta.

Skeleton (L2 U' B2 D F2 D' F2 U D B2 D L2) on inverse has FD corners, L=12, 2 spare moves.

- No variant passes the meta.

Skeleton (L2 U' B2 D F2 D L2 U D L2 D' L2) on inverse has FD corners, L=12, 2 spare moves.

- No variant passes the meta.

8 skeletons gone through, 125 HTRs: 2 finishes within goal (14, 14). This DR's optimal is 14.

### 2c4, scramble 6

`R' U' F R D2 L B' R' D L' R2 U2 B2 D2 F2 D R2 U' L2 D2 B' U2 F R' U' F`

2c4 4e, goal 14.

Skeleton D B2 U' R2 U L2 D' R2 U2 has FV corners, L=9, 5 spare moves.

- D R2 B2 U
    - After L2 F2, 1qt edges will be FV (good) and RH (good): +1+1+2(+0)
        - L2 F2 U F2 R2 L2 D' // no good: 6 pairs, the most of 26

Check inverse. Skeleton (U2 B2 D' F2 U R2 D' L2 D') has HH corners. Apply D and NISS: FD corners.

- (U2 B2 D')
    - After (B2), 1qt edges will be FH (bad) and RH (good): +0+0+2(+3)
        - **(B2 U F2 R2 L2 D' R2 F2 L2 F2 D') // 14**
    - After (F2 U2 L2 F2 L2), 1qt edges will be FD (good) and RH (good): +0+4+0(+0)
        - (F2 U2 L2 F2 L2 U F2 U') // no good: 6 pairs, the most of 18

The same skeleton in full, for the solutions that go on after its last quarter turn.

- (U2 B2 U' L2 U)
    - After (R2 F2 B2), 1qt edges will be RH (good) and FH (good): +0+2+3(+0)
        - **(R2 F2 B2 U' L2 B2 R2 B2 D') // 14**
        - (R2 F2 B2 U' L2 F2 L2 B2 U) // no good: 8 pairs, the most of 63

Skeleton D' F2 U B2 D' L2 U L2 U2 B2 has DD corners, L=10, 4 spare moves.

- D' B2 D
    - After R2 F2 R2 B2 R2, 1qt edges will be FV (good) and RD (good): +0+4+0(+0)
        - R2 F2 R2 B2 R2 U' F2 U // no good: 4 pairs, the most of 6

Check inverse. Skeleton (L2 U2 B2 U R2 U' F2 U R2 D) has HH corners. Apply D' and NISS: FD corners.

- (F2 U2 R2 U)
    - After (R2 L2 F2), 1qt edges will be FD (good) and RH (good): +0+2+1(+0)
        - (R2 L2 F2 U F2 R2 D) // no good: 6 pairs, the most of 9

The same skeleton in full, for the solutions that go on after its last quarter turn.

- (F2 U2 R2 U L2 B2 U')
    - After (B2 R2), 1qt edges will be RH (good) and FH (good): +1+1+2(+0)
        - (B2 R2 U' F2 B2 L2 D') // no good: 8 pairs, the most of 60

Skeleton U2 F2 D' B2 D' L2 U R2 U L2 U2 B2 has DD corners, L=12, 2 spare moves.

- No variant passes the meta.

Check inverse. Skeleton (L2 U2 B2 U' R2 U F2 U' F2 U' R2 U2) has FV corners.

- (L2 U2 B2 U' R2 U)
    - After (R2 B2), 1qt edges will be FV (good) and RV (good): +0+1+0(+1)
        - (R2 B2 U B2 U) // no good: 6 pairs, the most of 2

Skeleton U2 F2 D B2 U F2 U' B2 D L2 U2 has FV corners, L=11, 3 spare moves.

- U2 B2 U F2 U
    - After F2, 1qt edges will be FV (good) and RH (good): +0+0+3(+0)
        - F2 U R2 B2 U2 L2 U // no good: 8 pairs, the most of 3

Check inverse. Skeleton (U2 B2 U L2 U' L2 U L2 U R2 U2) has FV corners.

- (U2 B2 U R2 U')
    - After (R2 F2), 1qt edges will be FD (bad) and RV (good), fr=1: +0+1+0(+2)
        - (R2 F2 U' F2 U') // no good: 4 pairs, the most of 9

Skeleton D F2 U2 R2 D' L2 U' R2 U R2 has FD corners, L=10, 4 spare moves.

- D' L2 B2 U2 B2 D'
    - After F2 B2 L2, 1qt edges will be FD (good) and RH (good): +1+2+0(+0)
        - F2 B2 L2 U' B2 U // no good: 5 pairs, the most of 10

Check inverse. Skeleton (F2 D R2 U' R2 D B2 U2 L2 D') has HH corners. Apply D and NISS: DD corners.

- (F2 D)
    - After (R2), 1qt edges will be FV (good) and RD (good): +0+0+4(+0)
        - (R2 U F2 B2 R2 U2 L2 D) // no good: 6 pairs, the most of 27

The same skeleton in full, for the solutions that go on after its last quarter turn.

- (F2 U F2 U')
    - After (B2 R2 L2), 1qt edges will be RH (good) and FH (good): +0+2+1(+0)
        - (B2 R2 L2 U L2 F2 U2 F2 D) // no good: 8 pairs, the most of 186

Skeleton U2 F2 D L2 U2 F2 U L2 D' L2 U F2 has FD corners, L=12, 2 spare moves.

- U2 B2 U B2 U2 B2 R2 U'
    - After F2, 1qt edges will be FD (good) and RH (good): +1+0+0(+0)
        - F2 U' L2 U // no good

Check inverse. Skeleton (F2 U' L2 U R2 U R2 U2 B2 U R2 U2) has FV corners.

- (F2 U' L2 U)
    - After (R2), 1qt edges will be FV (good) and RH (good): +0+0+0(+0)
        - (R2 U R2 U2 B2 U) // no good: 6 pairs, the most of 20

Skeleton D B2 U' R2 U L2 D L2 D U F2 has FD corners, L=11, 3 spare moves.

- No variant passes the meta.

Skeleton D F2 D' L2 U F2 D' L2 D' U has HH corners, L=10, 4 spare moves. Apply (U') and NISS: HH corners.

- D L2 B2 U B2 D'
    - After F2 L2 F2 R2, 1qt edges will be RH (good) and FH (good): +1+3+0(+0)
        - F2 L2 F2 R2 U' L2 U' // no good: 6 pairs, the most of 11

The same skeleton in full, for the solutions that go on after its last quarter turn.

- D F2 D' B2 L2 D' B2 D
    - After B2, 1qt edges will be RH (good) and FH (good): +1+0+3(+0)
        - B2 U' F2 R2 B2 D // no good: 0 pairs, the most of 4

8 skeletons gone through, 457 HTRs: 2 finishes within goal (14, 14). This DR's optimal is 14.
