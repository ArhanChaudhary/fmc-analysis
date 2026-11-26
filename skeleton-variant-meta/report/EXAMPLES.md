# The skeleton/variant meta: example solves

26 Nov 2026

Example solves using the [skeleton/variant meta](WRITEUP.md), generated using JTuu's [subset generator](https://jtuu.be/subsets.html).

Every scramble is a DR on U/D. The goal is 12/13/14 moves from DR to a leave-slice finish for a 2qt/3qt/4qt DR; the 0c0 DRs are solved as 2qt ones, with goal 12. The 4a1 DRs also have goal 12; a skeleton with one quarter turn has no 2qt trigger, so its variants read +T(+N).

The solutions are found with an automated solver that implements the meta, and in each corner case the scrambles run from easiest to hardest: by the skeleton on which the solver first finds its shortest solution.

For each scramble:
 - Choose the 8 skeletons with the fewest moves to HTR
 - Include extensions to extra qt (if they are among the top 8)
   - Include extensions using null insertions such as U U'
   - These are treated like any other skeleton

Any solutions that use a different skeleton are listed as "hard to find"

For each skeleton:
 - Check all approaches to 2qt that use <= 1 extra move
 - Check all variants whose lower bound is <= spare moves
 - Skip variants that reach HTR with no move left for a finish
 - Show any successes and some near-misses

## How to read an example

```
Skeleton #8 U R2 U R2 U F2 U has HH corners, L=7, 5 spare moves. On inverse, (D' B2 U L2 D R2 D') has HH corners.

- (U') U
    - After L2 B2 L2 F2, 1qt edges will be RD (good) and FH (good): +0+3+2(+0)
        - L2 B2 L2 F2 U' F2 R2 L2 D // no good
- **D B2 D**
    - After L2, 1qt edges will be RH (good) and FH (good): +0+0+3(+0)
        - L2 U B2 L2 B2 L2 U' // no good
    - After R2, 1qt edges will be RH (good) and FH (good): +0+0+3(+0)
        - **R2 U L2 B2 L2 B2 U L2 R2 // 12**
- D (D')
    - After (B2 L2 B2 L2), 1qt edges will be FD (good) and RH (good): +0+3+2(+0)
        - (B2 L2 B2 L2 U' F2 R2 L2 D) // no good
- (U' L2 U)
    - After (F2 R2 B2 R2), 1qt edges will be RH (good) and FH (good): +0+3+0(+0)
        - (F2 R2 B2 R2 U' B2 U) // no good
```

**Skeleton #n ...** solves corners up to a possible corner swap; #n is its place in the order the skeletons are tried. NISS after 1 qt is allowed on both sides, and the variants of both sides are in one list
  - **(U') ... U**: the approach to 2qt (if any), in bold when it leads to a within-goal solution. Up to one extra move is allowed. With HH corners it can start with the skeleton's last quarter turn as a premove on the other side, like (U') or D
    - **After ...** setup to a 2qt trigger and the full penalty's lower bound
      - **X2 U Y2 D ...** the rest of the within-goal solution with the length of the whole, or the near-miss approach to HTR

## 2c4

### 2c4, scramble 1

`R' U' F R D2 L B' R' D L' R2 U2 B2 D2 F2 D R2 U' L2 D2 B' U2 F R' U' F`

2c4 4e, goal 14.

Skeleton #1 D B2 U' R2 U L2 D' R2 U2 has FV corners, L=9, 5 spare moves. On inverse, (U2 B2 D' F2 U R2 D' L2 D') has HH corners.

- D R2 B2 U
    - After L2 F2, 1qt edges will be FV (good) and RH (good): +1+1+2(+0)
        - L2 F2 U F2 R2 L2 D' // no good
- **D (U2 B2 D')**
    - After (B2), 1qt edges will be FH (bad) and RH (good): +0+0+2(+3)
        - **(B2 U F2 R2 L2 D' R2 F2 L2 F2) // 14**
    - After (F2 U2 L2 F2 L2), 1qt edges will be FD (good) and RH (good): +0+4+0(+0)
        - (F2 U2 L2 F2 L2 U F2 U') // no good
- (U2 F2 D' F2 L2 D')
    - After (F2 L2 F2 B2), 1qt edges will be RH (good) and FH (good): +1+3+0(+0)
        - (F2 L2 F2 B2 U' F2 U) // no good

Skeleton #2 D' F2 U B2 D' L2 U L2 U2 B2 has DD corners, L=10, 4 spare moves. On inverse, (L2 U2 B2 U R2 U' F2 U R2 D) has HH corners.

- D' B2 D
    - After R2 F2 R2 B2 R2, 1qt edges will be FV (good) and RD (good): +0+4+0(+0)
        - R2 F2 R2 B2 R2 U' F2 U // no good
- D' (F2 U2 R2 U)
    - After (R2 L2 F2), 1qt edges will be FD (good) and RH (good): +0+2+1(+0)
        - (R2 L2 F2 U F2 R2 D) // no good
- (F2 U2 R2 U L2 B2 U')
    - After (B2 R2), 1qt edges will be RH (good) and FH (good): +1+1+0(+0)
        - (B2 R2 U' R2 U') // no good

Skeleton #3 U2 F2 D' B2 D' L2 U R2 U L2 U2 B2 has DD corners, L=12, 2 spare moves. On inverse, (L2 U2 B2 U' R2 U F2 U' F2 U' R2 U2) has FV corners.

- On normal: all variants have lower bound > spare moves.
- (L2 U2 B2 U' R2 U)
    - After (R2 B2), 1qt edges will be FV (good) and RV (good): +0+1+0(+1)
        - (R2 B2 U B2 U) // no good

Skeleton #4 U2 F2 D B2 U F2 U' B2 D L2 U2 has FV corners, L=11, 3 spare moves. On inverse, (U2 B2 U L2 U' L2 U L2 U R2 U2) has FV corners.

- U2 B2 U F2 U
    - After F2, 1qt edges will be FV (good) and RH (good): +0+0+3(+0)
        - F2 U R2 B2 U2 L2 U // no good
- (U2 B2 U R2 U')
    - After (R2 F2), 1qt edges will be FD (bad) and RV (good), fr=1: +0+1+0(+2)
        - (R2 F2 U' F2 U') // no good

Skeleton #5 D F2 U2 R2 D' L2 U' R2 U R2 has FD corners, L=10, 4 spare moves. On inverse, (F2 D R2 U' R2 D B2 U2 L2 D') has HH corners.

- D' L2 B2 U2 B2 D'
    - After F2 B2 L2, 1qt edges will be FD (good) and RH (good): +1+2+0(+0)
        - F2 B2 L2 U' B2 U // no good
- D (F2 D)
    - After (R2), 1qt edges will be FV (good) and RD (good): +0+0+4(+0)
        - (R2 U F2 B2 R2 U2 L2 D) // no good
- (F2 U F2 U')
    - After (B2 R2 L2), 1qt edges will be RH (good) and FH (good): +0+2+1(+0)
        - (B2 R2 L2 U L2 F2 U2 F2 D) // no good

Skeleton #6 U2 F2 D L2 U2 F2 U L2 D' L2 U F2 has FD corners, L=12, 2 spare moves. On inverse, (F2 U' L2 U R2 U R2 U2 B2 U R2 U2) has FV corners.

- U2 B2 U B2 U2 B2 R2 U'
    - After F2, 1qt edges will be FD (good) and RH (good): +1+0+0(+0)
        - F2 U' L2 U // no good
- (F2 U' L2 U)
    - After (R2), 1qt edges will be FV (good) and RH (good): +0+0+0(+0)
        - (R2 U R2 U2 B2 U) // no good

Skeleton #7 D B2 U' R2 U L2 D L2 D U F2 has FD corners, L=11, 3 spare moves.

- All variants have lower bound > spare moves.

Skeleton #8 D F2 D' L2 U F2 D' L2 D' U has HH corners, L=10, 4 spare moves.

- (U') D B2 U' L2 D
    - After B2 L2, 1qt edges will be RH (good) and FH (good): +0+1+0(+0)
        - B2 L2 U F2 U' // no good
- Linearly: all variants have lower bound > spare moves, or reach HTR with no move left.

Optimal is 14. Found 14 on skeleton #1.

### 2c4, scramble 2

`R' U' F L2 F' L D2 L' F2 L' U2 R D2 B2 L2 U F2 D' L' U2 R2 F' U' R' U' F`

2c4 6e, goal 14.

Skeleton #1 D' B2 U' R2 U L2 D R2 has FD corners, L=8, 6 spare moves. On inverse, (B2 U B2 D L2 D' R2 D) has HH corners.

- D' R2 F2 U
    - After R2, 1qt edges will be FD (good) and RD (good): +1+0+3(+1)
        - R2 U F2 B2 U2 F2 U' // no good
- D' (B2 U)
    - After (B2 U2 R2 B2 R2), 1qt edges will be FD (good) and RD (good): +0+4+0(+1)
        - (B2 U2 R2 B2 R2 U R2 U) // no good
- **D (B2 U)**
    - After (F2), 1qt edges will be FD (bad) and RV (good): +0+0+0(+3)
        - **(F2 U R2 U F2 U2 F2 R2 D2 L2) // 13**
    - After (F2), 1qt edges will be FD (bad) and RV (good), fr=1: +0+0+2(+2)
        - **(F2 U' R2 U2 R2 U' R2 D2 B2 L2) // 13**
- **D (B2 U')**
    - After (F2 U2 F2), 1qt edges will be FD (bad) and RV (good), fr=1: +0+2+0(+2)
        - **(F2 U2 F2 U' R2 U R2 D2 B2 L2) // 13**
- **D' (L2 F2 D')**
    - After (B2 R2), 1qt edges will be FD (good) and RV (bad): +1+1+0(+3)
        - **(B2 R2 U R2 U F2 R2 B2 D2 B2) // 14**
- **(B2 D L2 U)**
    - After (B2 R2), 1qt edges will be RH (good) and FH (good): +0+1+0(+0)
        - **(B2 R2 U B2 U' R2 L2 U2) // 12**
- (L2 F2 U' B2 U')
    - After (B2 L2), 1qt edges will be RV (bad) and FH (good): +1+1+1(+3)
        - (B2 L2 U' L2 F2 D') // no good

Skeleton #2 D F2 U F2 U' R2 D' R2 has RD corners, L=8, 6 spare moves. On inverse, (L2 U F2 U F2 U' F2 D') has HH corners.

- D F2 U
    - After F2, 1qt edges will be RH (bad) and FD (good): +0+0+3(+3)
        - F2 U F2 L2 U2 F2 U' // no good
- **D (L2 U)**
    - After (L2 F2), 1qt edges will be FD (good) and RH (good): +0+1+3(+0)
        - **(L2 F2 U B2 L2 U2 F2 D L2 R2 B2) // 14**
- **D (L2 U')**
    - After (B2 U2 L2 F2), 1qt edges will be FD (good) and RH (good): +0+3+1(+0)
        - **(B2 U2 L2 F2 U B2 L2 D' R2 L2 F2) // 14**
- D (B2 R2 U')
    - After (B2), 1qt edges will be FD (good) and RV (bad): +1+0+2(+3)
        - (B2 U L2 U2 R2 U') // no good
- (R2 D B2 U')
    - After (F2 R2 U2 F2), 1qt edges will be RH (good) and FH (good): +0+3+1(+0)
        - (F2 R2 U2 F2 U' B2 R2 U') // no good

Skeleton #3 B2 D F2 U F2 U' R2 D' R2 has FD corners, L=9, 5 spare moves. On inverse, (B2 D' L2 U' L2 U B2 D R2) has FD corners.

- B2 D L2 B2 U'
    - After B2, 1qt edges will be FD (good) and RD (good): +1+0+3(+1)
        - B2 U' F2 U2 L2 B2 U' // no good
- **(F2 U' F2 R2 D)**
    - After (F2), 1qt edges will be FD (good) and RH (good): +1+0+2(+0)
        - **(F2 U F2 U2 B2 U F2 R2 L2) // 14**
    - After (F2), 1qt edges will be FD (good) and RH (good): +1+0+4(+0)
        - (F2 U B2 U2 R2 L2 F2 D') // no good
- **(F2 U' F2 R2 D')**
    - After (F2 U2 B2), 1qt edges will be FD (good) and RH (good): +1+2+0(+0)
        - **(F2 U2 B2 U B2 U' B2 L2 R2) // 14**

Skeleton #4 B2 D' B2 U' L2 U B2 D R2 has RD corners, L=9, 5 spare moves. On inverse, (L2 U' B2 U' L2 U L2 U F2) has FD corners.

- B2 D' R2 F2 U
    - After R2, 1qt edges will be RD (good) and FD (good): +1+0+3(+1)
        - R2 U' F2 B2 L2 F2 D // no good
- **R2 F2 U L2 U**
    - After F2 L2, 1qt edges will be RD (good) and FD (good): +1+1+1(+1)
        - **F2 L2 U R2 B2 D' L2 F2 // 13**
- **L2 B2 D R2 U**
    - After R2, 1qt edges will be RD (good) and FH (good): +1+0+4(+0)
        - **R2 U F2 R2 F2 U2 R2 U L2 // 14**
- **F2 U' L2 B2 D**
    - After B2, 1qt edges will be RD (good) and FH (good): +1+0+4(+0)
        - **B2 U R2 F2 L2 U2 B2 D L2 // 14**
- **(R2 D' F2 U')**
    - After (F2), 1qt edges will be FD (good) and RD (good): +0+0+4(+1)
        - (F2 U F2 R2 B2 L2 F2 D) // no good
        - **(F2 U' R2 F2 R2 U2 F2 U' F2 R2) // 14**

Skeleton #5 U B2 U2 L2 U B2 U' F2 D has HH corners, L=9, 5 spare moves. On inverse, (U' B2 U' B2 U F2 U2 R2 D) has HH corners.

- (D') U
    - After L2 B2 U2 F2, 1qt edges will be RV (bad) and FH (good): +0+1+1(+3)
        - L2 B2 U2 F2 U' R2 F2 D' // no good
- D L2 U2 F2 U
    - After L2, 1qt edges will be RV (bad) and FH (good): +0+0+1(+3)
        - L2 U' B2 R2 D' // no good
- **D' B2 U2 B2 R2 U**
    - After B2, 1qt edges will be RH (good) and FD (bad): +1+0+1(+3)
        - **B2 U R2 B2 U' R2 B2 R2 // 14**
- D' (U')
    - After (F2 U2 R2 F2 R2), 1qt edges will be FV (good) and RD (good): +0+4+1(+0)
        - (F2 U2 R2 F2 R2 U' L2 F2 D') // no good
- **(D' L2 U')**
    - After (F2), 1qt edges will be RH (good) and FH (good): +0+0+3(+0)
        - (F2 U' F2 L2 F2 R2 U2 B2 D') // no good
        - **(F2 U' B2 R2 B2 R2 U2 F2 U L2 R2) // 14**

Skeleton #6 B2 D L2 U2 F2 D F2 U' B2 D' has HH corners, L=10, 4 spare moves. On inverse, (D B2 U F2 U F2 U2 R2 D L2) has FD corners.

- (D) B2 D'
    - After L2 F2 L2 B2 R2 U2 R2, 1qt edges will be FD (good) and RH (good): +0+4+0(+0)
        - L2 F2 L2 B2 R2 U2 R2 U' L2 U // no good
- **B2 D' R2 F2 U2 F2 U**
    - After R2, 1qt edges will be RD (bad) and FH (good): +1+0+0(+3)
        - **R2 U R2 U F2 R2 B2 // 14**
- B2 D' B2 L2 U2 L2 U
    - After F2, 1qt edges will be RH (good) and FH (good): +1+0+2(+0)
        - F2 U F2 U2 F2 U' // no good
- On inverse: all variants have lower bound > spare moves.

Skeleton #7 L2 U F2 D B2 U R2 U2 B2 D B2 has FD corners, L=11, 3 spare moves. On inverse, (B2 D L2 U2 B2 U L2 U R2 D B2) has RD corners.

- **L2 U R2 F2 U'**
    - After R2 B2, 1qt edges will be FD (good) and RH (good): +1+1+1(+0)
        - **R2 B2 U' F2 L2 U2 L2 U F2 // 14**
- R2 U F2 R2 U'
    - After F2, 1qt edges will be FD (good) and RH (good): +1+0+2(+0)
        - F2 U B2 R2 U2 F2 L2 U' // no good
- **(B2 D R2 U2 B2 U)**
    - After (R2 B2), 1qt edges will be RD (good) and FD (good): +0+1+1(+1)
        - **(R2 B2 U' B2 R2 U R2 B2) // 14**
- **(B2 D' F2 U2 L2 U')**
    - After (L2 F2), 1qt edges will be RD (good) and FD (good): +0+1+1(+1)
        - **(L2 F2 U' F2 L2 U L2 F2) // 14**
- (B2 D L2 U2 B2 U)
    - After (B2 R2), 1qt edges will be RD (good) and FD (good): +0+1+0(+1)
        - (B2 R2 U' R2 U') // no good
- **(B2 D' F2 U2 F2 R2 U)**
    - After (L2 B2), 1qt edges will be RD (good) and FH (good): +1+1+1(+0)
        - **(L2 B2 U R2 B2 D' L2) // 14**

Skeleton #8 L2 U' R2 U' F2 U F2 U2 R2 U R2 has RD corners, L=11, 3 spare moves. On inverse, (L2 U L2 U2 B2 D F2 U' F2 D' F2) has RD corners.

- **R2 U' F2 U'**
    - After F2 L2, 1qt edges will be RD (good) and FH (good): +0+1+2(+0)
        - **F2 L2 U F2 L2 U2 B2 R2 D L2 // 14**
- **R2 U' R2 F2 U**
    - After B2, 1qt edges will be RD (good) and FH (good): +1+0+0(+0)
        - **B2 U R2 U2 F2 D L2 B2 F2 // 14**
        - **B2 U' F2 U2 R2 D' R2 F2 B2 // 14**
- R2 U' L2 B2 U
    - After F2 R2, 1qt edges will be RD (good) and FH (good): +1+1+1(+0)
        - F2 R2 U B2 U2 B2 L2 D // no good
- (R2 D B2 L2 U2 R2 U')
    - After (L2 F2), 1qt edges will be RD (good) and FH (good): +1+1+1(+0)
        - (L2 F2 U' L2 B2 U') // no good

Hard to find solutions:

Skeleton D L2 U F2 D B2 U L2 U' L2 U' B2 has RD corners, L=12, 2 spare moves. On inverse, (L2 U' B2 D' R2 U F2 D L2 U F2 D') has HH corners.

- **D L2 U F2 D F2 D**
    - After R2, 1qt edges will be RD (good) and FD (good): +0+0+0(+1)
        - **R2 U' B2 U' R2 B2 // 13**
- **D (B2 R2 U B2 D B2 D')**
    - After (R2), 1qt edges will be RD (good) and FH (good): +1+0+0(+0)
        - **(R2 U' B2 U' R2) // 13**

Optimal is 12. Found 12 on skeleton #1.

### 2c4, scramble 3

`R' U' F R2 U2 R' F' B R L B' R F' R2 U R2 D R2 U2 D' R2 F2 D R' U' F`

2c4 4e, goal 14.

Skeleton #1 U R2 U' R2 U R2 U R2 U2 F2 has DD corners, L=10, 4 spare moves. On inverse, (R2 U2 B2 U L2 U F2 U' F2 U') has HH corners.

- U R2 U'
    - After R2 U2 L2 B2 L2, 1qt edges will be FV (good) and RD (good): +0+4+0(+0)
        - R2 U2 L2 B2 L2 U F2 U' // no good
- U (B2 U2 L2 D)
    - After (B2), 1qt edges will be RD (good) and FD (good): +0+0+2(+1)
        - (B2 U' R2 L2 B2 D) // no good
- **U (B2 U2 F2 R2 U')**
    - After (L2), 1qt edges will be RD (good) and FH (good): +1+0+1(+0)
        - **(L2 U F2 R2 D B2 F2 R2) // 14**
- (B2 U2 R2 D L2 D')
    - After (R2 F2), 1qt edges will be RH (good) and FV (bad): +0+1+0(+3)
        - (R2 F2 U' L2 U) // no good

Skeleton #2 U' R2 U R2 U' R2 U F2 has RD corners, L=8, 6 spare moves. On inverse, (R2 U F2 U' F2 U F2 U) has HH corners.

- U' L2 U
    - After F2 U2 L2 B2 R2, 1qt edges will be RD (good) and FD (good): +0+4+1(+1)
        - F2 U2 L2 B2 R2 U' B2 R2 U' // no good
- U' (F2 R2 U')
    - After (F2 L2), 1qt edges will be RD (good) and FH (good): +1+1+4(+0)
        - (F2 L2 U L2 B2 R2 U2 B2 D) // no good
- (F2 L2 D' L2 D)
    - After (R2 F2 L2 B2 R2), 1qt edges will be RH (good) and FH (good): +1+4+0(+0)
        - (R2 F2 L2 B2 R2 U' B2 U) // no good

Skeleton #3 U2 R2 U' R2 U' L2 D R2 D' F2 has RD corners, L=10, 4 spare moves. On inverse, (R2 U' F2 D R2 U' R2 D' F2 U2) has RV corners.

- U2 R2 U' R2 U
    - After L2 U2 F2 L2, 1qt edges will be RD (good) and FH (good): +0+3+0(+0)
        - L2 U2 F2 L2 U L2 U // no good
- (R2 U' B2 D)
    - After (R2 F2), 1qt edges will be RH (bad) and FH (good), fr=1: +0+1+0(+2)
        - (R2 F2 U F2 U) // no good

Skeleton #4 U2 R2 U R2 U R2 U' R2 U R2 U2 F2 has DD corners, L=12, 2 spare moves. On inverse, (R2 U2 B2 D' B2 U' B2 U R2 D F2 U2) has RV corners.

- On normal: all variants have lower bound > spare moves.
- (B2 U2 L2 U' L2 U)
    - After (R2 F2), 1qt edges will be RV (good) and FH (good), fr=1: +0+1+0(+1)
        - (R2 F2 U B2 U') // no good

Skeleton #5 U R2 U2 F2 U' R2 U' F2 U R2 U2 has RV corners, L=11, 3 spare moves. On inverse, (U2 R2 U' B2 U B2 U F2 U2 R2 U') has HH corners.

- U' R2 U2 R2 F2 U'
    - After R2, 1qt edges will be RV (good) and FD (bad), fr=1: +1+0+0(+2)
        - R2 U' F2 U // no good
- On inverse, with the premove U: all variants have lower bound > spare moves.
- (U2 R2 U' L2 B2 U')
    - After (L2), 1qt edges will be RH (good) and FH (good): +1+0+1(+0)
        - (L2 U F2 U2 B2 L2 U') // no good

Skeleton #6 (R2 U F2 U' F2 U B2 U D' U) on inverse has HH corners, L=10, 4 spare moves.

- All variants have lower bound > spare moves.

Skeleton #7 U2 F2 U' L2 D' F2 D L2 U2 B2 U' R2 has RD corners, L=12, 2 spare moves. On inverse, (R2 U F2 U2 R2 U' R2 U' F2 U' R2 U2) has FV corners.

- All variants have lower bound > spare moves.

Skeleton #8 U R2 U' R2 U R2 U' R2 U D R2 has FD corners, L=11, 3 spare moves.

- U R2 U' L2 D R2 D'
    - After L2, 1qt edges will be FD (good) and RH (good): +0+0+3(+0)
        - L2 U' R2 F2 R2 U // no good

Optimal is 13. Found 14 on skeleton #1.

### 2c4, scramble 4

`R' U' F R2 F R2 B2 L2 F L2 B' L2 R2 D2 F2 U F R' D' B D2 B' F' R' U' F`

2c4 0e, goal 14.

Skeleton #1 B2 D' B2 D B2 D' B2 D R2 U2 F2 has DD corners, L=11, 3 spare moves. On inverse, (F2 U2 R2 U F2 U F2 U' F2 U F2) has FD corners.

- F2 U' L2 B2 U'
    - After R2, 1qt edges will be FD (good) and RV (good): +1+0+1(+0)
        - R2 U L2 B2 U // no good
- (F2 U2 R2 U B2 U)
    - After (L2), 1qt edges will be FD (good) and RD (good): +0+0+2(+1)
        - (L2 U B2 U2 B2 U') // no good

Skeleton #2 B2 D F2 D' R2 U L2 U' R2 U2 has FV corners, L=10, 4 spare moves. On inverse, (U2 B2 D' L2 D R2 U' L2 U R2) has FD corners.

- **B2 D L2 B2 U**
    - After F2, 1qt edges will be FD (bad) and RV (good), fr=1: +1+0+1(+2)
        - **F2 U' R2 F2 U L2 D2 F2 L2 // 14**
- F2 U R2 B2 U
    - After R2, 1qt edges will be FV (good) and RH (good), fr=1: +1+0+1(+1)
        - R2 U' F2 L2 D // no good
- (F2 U2 F2 U L2 U)
    - After (F2), 1qt edges will be FV (bad) and RH (good): +1+0+0(+3)
        - (F2 U' L2 U') // no good

Skeleton #3 U2 B2 U' B2 U L2 U' B2 U R2 U2 has FV corners, L=11, 3 spare moves. On inverse, (U2 B2 D L2 D' L2 D L2 D' R2 U2) has FV corners.

- U2 B2 U' B2 U
    - After L2, 1qt edges will be FH (bad) and RV (good), fr=1: +0+0+0(+2)
        - L2 U' B2 U // no good
- (U2 R2 B2 D' B2 D)
    - After (R2), 1qt edges will be FH (bad) and RH (good), fr=1: +1+0+0(+2)
        - (R2 U' L2 U) // no good

Skeleton #4 U2 B2 U B2 U' R2 U B2 U R2 U2 F2 has DD corners, L=12, 2 spare moves. On inverse, (F2 U2 R2 U' B2 U' L2 D F2 D' F2 U2) has FV corners.

- U2 B2 U F2 U'
    - After R2 F2, 1qt edges will be FV (good) and RV (good): +0+1+0(+1)
        - R2 F2 U' R2 U // no good
- (R2 U2 F2 U' R2 U)
    - After (F2 R2), 1qt edges will be FV (good) and RV (good): +0+1+0(+1)
        - (F2 R2 U F2 U') // no good

Skeleton #5 U2 B2 U L2 U2 B2 U' B2 U B2 U' R2 has FD corners, L=12, 2 spare moves. On inverse, (F2 U' F2 U R2 U R2 U2 F2 U' F2 U2) has FV corners.

- U2 F2 D' L2 F2 U2 F2 U'
    - After R2, 1qt edges will be FD (good) and RH (good): +1+0+1(+0)
        - R2 U' F2 L2 D' // no good
- (F2 U' L2 B2 U')
    - After (L2), 1qt edges will be FV (good) and RH (good): +1+0+1(+0)
        - (L2 U' R2 U2 R2 F2 D') // no good

Skeleton #6 B2 D B2 U2 L2 U' F2 U' B2 D L2 has FD corners, L=11, 3 spare moves. On inverse, (F2 U R2 U' F2 U R2 U2 F2 U' R2) has FD corners.

- B2 D L2 F2 U2 F2 U
    - After B2, 1qt edges will be FD (good) and RD (good): +1+0+1(+1)
        - B2 U R2 B2 U // no good
- **(F2 U B2 L2 U)**
    - After (B2), 1qt edges will be FD (good) and RD (good): +1+0+1(+1)
        - **(B2 U R2 U2 L2 B2 U B2 L2) // 14**
        - (B2 U R2 U2 R2 F2 D') // no good

Skeleton #7 B2 D' B2 D B2 D' B2 D' R2 U D L2 has FD corners, L=12, 2 spare moves.

- All variants have lower bound > spare moves.

Skeleton #8 B2 D' B2 D B2 D' B2 D R2 D U R2 has RD corners, L=12, 2 spare moves.

- All variants have lower bound > spare moves.

Hard to find solutions:

Skeleton U R2 U F2 D B2 D' R2 U F2 U R2 U2 F2 has DD corners, L=14, 0 spare moves. On inverse, (F2 U2 R2 D R2 U' L2 D L2 U' R2 U' L2 U') has HH corners.

- **U R2 U F2 D B2 D'**
    - After R2, 1qt edges will be FD (good) and RV (good): +0+0+0(+0)
        - **R2 U F2 U' L2 D2 F2 // 14**
- **U (F2 U2 R2 D L2 D' L2 U)**
    - After (L2), 1qt edges will be RD (good) and FH (good): +0+0+0(+0)
        - **(L2 U' B2 U' L2) // 14**

Skeleton B2 D' B2 D' F2 U F2 U' L2 U' B2 U L2 U2 has RV corners, L=14, 0 spare moves.

- **B2 D' F2 D' L2 U B2 U'**
    - After F2, 1qt edges will be RV (good) and FH (good): +0+0+0(+0)
        - **F2 U' F2 U R2 U2 // 14**

Optimal is 14. Found 14 on skeleton #2.

### 2c4, scramble 5

`R' U' F L U2 R L2 F' L B' D L F2 R2 U2 L' U2 L' B2 R' U2 L' B R' U' F`

2c4 2e, goal 14.

Skeleton #1 F2 U' R2 U B2 D' F2 D' B2 U2 has RV corners, L=10, 4 spare moves. On inverse, (U2 R2 D' F2 D' F2 D F2 D' L2) has FD corners.

- L2 F2 U F2 U'
    - After R2 B2, 1qt edges will be RV (good) and FH (good): +1+1+2(+0)
        - R2 B2 U F2 U2 F2 U // no good
- (R2 U2 L2 U F2 U')
    - After (R2 F2), 1qt edges will be FD (good) and RH (good): +1+1+1(+0)
        - (R2 F2 U' F2 R2 U') // no good

Skeleton #2 F2 U R2 U' F2 U R2 U F2 U2 has FV corners, L=10, 4 spare moves. On inverse, (U2 F2 D' L2 D' B2 U R2 U' B2) has FD corners.

- F2 U L2 U'
    - After B2 L2, 1qt edges will be FV (good) and RH (good): +0+1+2(+0)
        - B2 L2 U' B2 R2 L2 D' // no good
- (U2 B2 U' R2 U')
    - After (B2 L2 B2 L2), 1qt edges will be FD (good) and RD (good): +0+3+0(+1)
        - (B2 L2 B2 L2 U' L2 U') // no good
- **(U2 B2 U' L2 U')**
    - After (F2 R2), 1qt edges will be FH (bad) and RH (good): +0+1+0(+3)
        - **(F2 R2 U' L2 U L2 F2 L2 B2) // 14**
    - After (R2 F2 R2 F2), 1qt edges will be FD (good) and RD (good): +0+3+0(+1)
        - **(R2 F2 R2 F2 U' L2 U B2 R2) // 14**

Skeleton #3 R2 U2 F2 D F2 D' F2 U L2 U R2 U2 has FV corners, L=12, 2 spare moves. On inverse, (U2 F2 D L2 U L2 U' F2 D L2 U2 B2) has DD corners.

- R2 U2 F2 D F2 D'
    - After R2 L2 B2, 1qt edges will be FV (good) and RH (good): +0+2+0(+0)
        - R2 L2 B2 U B2 U // no good
- (B2 U2 F2 D' L2 U)
    - After (R2), 1qt edges will be FV (good) and RD (good): +1+0+1(+0)
        - (R2 U' B2 L2 D) // no good

Skeleton #4 R2 U2 F2 U L2 U2 F2 U' L2 U' F2 U' has HH corners, L=12, 2 spare moves. On inverse, (U R2 U' L2 U R2 U2 F2 U F2 U2 R2) has DD corners.

- (U) R2 U2 B2 U'
    - After B2 R2 U2 R2, 1qt edges will be RD (good) and FD (good): +0+1+0(+1)
        - B2 R2 U2 R2 U' R2 U // no good
- R2 U2 F2 D R2 B2 U2 B2 U
    - After B2, 1qt edges will be RH (good) and FH (good): +1+0+0(+0)
        - B2 U L2 U' // no good
- (U F2 L2 U)
    - After (L2), 1qt edges will be FV (good) and RD (good): +1+0+0(+0)
        - (L2 U L2 U2 F2 U') // no good

Skeleton #5 B2 U R2 U2 F2 U' L2 U R2 U has HH corners, L=10, 4 spare moves. On inverse, (U' B2 U R2 D L2 U2 B2 D' R2) has FD corners.

- (U') R2 B2 U
    - After R2 F2 U2 B2, 1qt edges will be FD (good) and RH (good): +1+1+2(+0)
        - R2 F2 U2 B2 U L2 F2 B2 D // no good
- F2 U B2 U2 L2 U'
    - After B2, 1qt edges will be RH (good) and FH (good): +0+0+3(+0)
        - B2 U' F2 L2 U2 F2 U // no good
- (U' F2 U)
    - After (B2 L2 F2 L2), 1qt edges will be FD (good) and RH (good): +0+3+1(+0)
        - (B2 L2 F2 L2 U' B2 U2 F2 R2 D) // no good

Skeleton #6 R2 U2 F2 D' B2 D L2 U' F2 U' R2 U2 has RV corners, L=12, 2 spare moves. On inverse, (U2 R2 D B2 U B2 D' B2 U F2 U2 R2) has DD corners.

- F2 U2 R2 D' R2 U'
    - After L2, 1qt edges will be RV (good) and FH (good): +0+0+1(+0)
        - L2 U F2 L2 U // no good
- (U2 F2 R2 D' L2 D')
    - After (B2), 1qt edges will be FV (good) and RD (good): +1+0+0(+0)
        - (B2 U R2 U') // no good

Skeleton #7 (U' B2 U R2 D R2 U D R2 U' L2) on inverse has FD corners, L=11, 3 spare moves.

- All variants have lower bound > spare moves.

Skeleton #8 (U' B2 U R2 D' F2 U D B2 U R2) on inverse has FD corners, L=11, 3 spare moves.

- All variants have lower bound > spare moves.

Optimal is 14. Found 14 on skeleton #2.

### 2c4, scramble 6

`R' U' F U2 R' U F B' U2 B D' B U2 L2 D2 R2 L2 F' D2 R2 B L2 F' R' U' F`

2c4 4e, goal 14.

Skeleton #1 U L2 U B2 U' B2 U R2 has RD corners, L=8, 6 spare moves. On inverse, (L2 D' L2 U L2 D' L2 U') has HH corners.

- U B2 R2 U'
    - After B2, 1qt edges will be RD (good) and FH (good): +1+0+3(+0)
        - B2 U F2 B2 R2 B2 D' // no good
- U (L2 D)
    - After (F2 L2 U2 F2), 1qt edges will be RD (good) and FV (bad), fr=1: +0+3+0(+3)
        - (F2 L2 U2 F2 U R2 U) // no good
- **(L2 D' B2 R2 U')**
    - After (L2), 1qt edges will be RH (good) and FH (good): +1+0+1(+0)
        - **(L2 U L2 B2 D' B2 L2 R2 F2) // 14**
        - (L2 U R2 F2 U) // no good

Skeleton #2 U' R2 U' R2 U R2 U' R2 U2 has RV corners, L=9, 5 spare moves. On inverse, (U2 R2 U R2 U' R2 U R2 U) has HH corners.

- **U' B2 R2 D**
    - After R2, 1qt edges will be RD (bad) and FV (good): +1+0+0(+3)
        - **R2 U' B2 U' L2 U2 R2 F2 U2 B2 // 14**
- **U' B2 L2 U'**
    - After L2 U2 L2, 1qt edges will be RV (good) and FH (good), fr=1: +1+2+1(+1)
        - **L2 U2 L2 U R2 F2 D L2 U2 R2 // 14**
- **U' F2 L2 U**
    - After F2 L2 F2 B2, 1qt edges will be RV (good) and FH (good): +1+3+0(+0)
        - **F2 L2 F2 B2 U L2 U' R2 U2 // 13**
- **U' B2 L2 U**
    - After L2, 1qt edges will be RV (good) and FH (good): +1+0+4(+0)
        - L2 U' F2 U2 B2 L2 F2 U // no good
        - **L2 U' B2 U2 B2 R2 F2 D L2 U2 // 14**
- **U' (U2 R2 U)**
    - After (L2), 1qt edges will be RD (good) and FD (good): +0+0+1(+1)
        - **(L2 U' L2 B2 U' R2 F2 R2 L2) // 13**
    - After (B2 R2), 1qt edges will be RD (good) and FV (bad): +0+1+1(+3)
        - (B2 R2 U L2 F2 D) // no good
    - After (L2), 1qt edges will be RD (good) and FD (good): +0+0+3(+1)
        - **(L2 U' F2 B2 L2 F2 U' L2 F2) // 13**
- **U' (U2 L2 D')**
    - After (F2 R2 B2 U2 B2), 1qt edges will be RD (good) and FD (good): +0+4+0(+1)
        - **(F2 R2 B2 U2 B2 U L2 U' L2 B2) // 14**
- **U' (R2 U2 L2 D')**
    - After (F2 R2), 1qt edges will be RD (good) and FD (good): +1+1+2(+1)
        - **(F2 R2 U' L2 U2 L2 U L2 B2) // 14**
- (U2 L2 D B2 L2 U)
    - After (F2), 1qt edges will be RV (bad) and FH (good): +1+0+1(+3)
        - (F2 U' R2 B2 D') // no good

Skeleton #3 L2 D' R2 U' F2 U B2 D' L2 has RD corners, L=9, 5 spare moves. On inverse, (L2 D R2 D' R2 U F2 U R2) has RD corners.

- **R2 U' F2 R2 U**
    - After F2, 1qt edges will be RD (good) and FH (good), fr=1: +1+0+1(+3)
        - **F2 U' R2 B2 D R2 U2 L2 D2 // 14**
    - After F2, 1qt edges will be RD (good) and FH (good): +1+0+3(+0)
        - **F2 U F2 U2 R2 B2 D R2 // 13**
        - F2 U F2 U2 L2 F2 U' // no good
    - After F2, 1qt edges will be RD (good) and FH (good): +1+0+4(+0)
        - **F2 U' R2 U2 F2 U2 B2 D R2 // 14**
- **(L2 D R2 D')**
    - After (R2), 1qt edges will be RD (good) and FH (good): +0+0+5(+0)
        - **(R2 U F2 R2 U2 R2 U2 L2 D' L2) // 14**
        - **(R2 U F2 L2 U2 L2 U2 R2 D' L2) // 14**
        - **(R2 U' R2 U2 F2 L2 U2 L2 D R2) // 14**
        - **(R2 U' L2 U2 F2 R2 U2 R2 D R2) // 14**
- (R2 U L2 U')
    - After (R2 B2), 1qt edges will be RD (good) and FD (good): +0+1+3(+1)
        - (R2 B2 U L2 F2 U2 L2 U') // no good

Skeleton #4 R2 U L2 U B2 U' B2 U R2 U2 has RV corners, L=10, 4 spare moves. On inverse, (U2 L2 D' R2 U B2 U' F2 D' L2) has RD corners.

- R2 U L2 U
    - After L2 F2, 1qt edges will be RD (bad) and FV (good), fr=1: +0+1+0(+2)
        - L2 F2 U F2 U // no good
- **(U2 F2 L2 D F2 D')**
    - After (B2 L2), 1qt edges will be RD (good) and FH (good): +1+1+2(+0)
        - **(B2 L2 U L2 U2 L2 U R2) // 14**
- (L2 U2 R2 U R2 U)
    - After (L2 B2), 1qt edges will be RD (good) and FD (good): +1+1+1(+1)
        - (L2 B2 U R2 F2 U') // no good

Skeleton #5 U L2 U2 B2 U F2 U R2 U F2 U2 R2 has DD corners, L=12, 2 spare moves. On inverse, (L2 U2 F2 D' R2 D' L2 U L2 U2 B2 U) has HH corners.

- **U B2 U2 R2 U**
    - After F2, 1qt edges will be FV (good) and RD (good): +0+0+1(+0)
        - **F2 U' R2 B2 D' F2 U2 F2 L2 // 14**
- **U' R2 U2 B2 U'**
    - After F2, 1qt edges will be FV (good) and RD (good): +0+0+1(+0)
        - **F2 U' R2 B2 D' F2 U2 F2 L2 // 14**
- U F2 U2 B2 R2 D'
    - After R2, 1qt edges will be FV (good) and RD (good): +1+0+0(+0)
        - R2 U F2 U // no good
- **U' L2 B2 U2 B2 U**
    - After L2, 1qt edges will be FD (good) and RV (good): +1+0+0(+0)
        - **L2 U' L2 U' L2 D2 L2 B2 // 14**
- **U' B2 U2 B2 R2 U**
    - After F2, 1qt edges will be FV (good) and RD (good): +1+0+1(+0)
        - **F2 U' R2 B2 D B2 D2 L2 // 14**
- U' (B2 U2 R2 U')
    - After (L2), 1qt edges will be FV (good) and RD (good): +0+0+2(+0)
        - (L2 U' R2 U2 L2 U) // no good
- **U' (L2 U2 F2 D')**
    - After (F2 L2), 1qt edges will be FV (good) and RV (good): +0+1+0(+1)
        - **(F2 L2 U B2 U' L2 F2 D2 B2) // 14**
- **U' (B2 L2 U2 R2 U)**
    - After (R2), 1qt edges will be FV (good) and RD (good): +1+0+0(+0)
        - **(R2 U R2 U' F2 D2 B2 L2) // 14**
- **U' (L2 F2 U2 F2 D)**
    - After (B2 R2), 1qt edges will be FV (good) and RD (good): +1+1+0(+0)
        - **(B2 R2 U F2 U B2 U2 R2) // 14**
- (B2 U2 R2 U' L2 U)
    - After (L2), 1qt edges will be RH (good) and FH (good): +0+0+1(+0)
        - (L2 U R2 F2 U2 B2 D') // no good

Skeleton #6 U L2 U B2 U' B2 U D U' B2 has RD corners, L=10, 4 spare moves.

- All variants have lower bound > spare moves.

Skeleton #7 F2 U' R2 D' L2 U B2 U2 R2 D' L2 has RD corners, L=11, 3 spare moves. On inverse, (L2 D R2 U2 F2 U' F2 D' R2 U' R2) has FD corners.

- L2 F2 U F2 U
    - After F2, 1qt edges will be RD (good) and FD (good): +1+0+1(+1)
        - F2 U' F2 U2 F2 L2 U' // no good
- On inverse: all variants have lower bound > spare moves.

Skeleton #8 (L2 D' L2 U L2 D' L2 U D U) on inverse has HH corners, L=10, 4 spare moves.

- U' (L2 D' R2 D R2 D')
    - After (L2), 1qt edges will be RH (good) and FH (good): +0+0+2(+0)
        - (L2 U R2 L2 D) // no good

Hard to find solutions:

Skeleton R2 U L2 U2 F2 U R2 U B2 U R2 U2 F2 has DD corners, L=13, 1 spare move.

- **R2 U F2 U2 R2 D**
    - After B2, 1qt edges will be FV (good) and RV (good): +0+0+0(+1)
        - **B2 U' L2 U R2 F2 U2 B2 // 14**
- **R2 U' R2 U2 F2 D'**
    - After F2, 1qt edges will be FV (good) and RV (good): +0+0+0(+1)
        - **F2 U' R2 U L2 B2 D2 B2 // 14**

Optimal is 13. Found 13 on skeleton #2.

### 2c4, scramble 7

`R' U' F U2 D2 R D F L2 U2 F D' L B2 R' D2 B2 R D2 L' F2 L B2 R' U' F`

2c4 6e, goal 14.

Skeleton #1 F2 U' L2 D R2 D' L2 U F2 U2 has RV corners, L=10, 4 spare moves. On inverse, (U2 L2 U F2 U' L2 U F2 U' R2) has FD corners.

- B2 D' R2 U
    - After R2, 1qt edges will be RV (good) and FH (good): +0+0+3(+0)
        - R2 U' L2 B2 R2 L2 U' // no good
- (U2 L2 U B2 D')
    - After (R2), 1qt edges will be FD (good) and RH (good): +0+0+3(+0)
        - (R2 U L2 F2 L2 F2 U') // no good

Skeleton #2 F2 U R2 U' L2 U F2 U F2 U2 R2 has DD corners, L=11, 3 spare moves. On inverse, (B2 U2 L2 U' F2 D F2 U' F2 D L2) has FD corners.

- F2 U R2 U'
    - After L2, 1qt edges will be FD (good) and RV (good): +0+0+3(+0)
        - L2 U F2 B2 R2 F2 D' // no good
- (R2 U2 F2 U' R2 U')
    - After (R2 F2), 1qt edges will be FD (good) and RH (good): +0+1+1(+0)
        - (R2 F2 U' L2 B2 D) // no good

Skeleton #3 F2 U2 L2 D' R2 U' F2 D L2 U' F2 U2 has RV corners, L=12, 2 spare moves. On inverse, (U2 L2 U' B2 D R2 U' F2 D B2 U2 L2) has DD corners.

- All variants have lower bound > spare moves.

Skeleton #4 F2 U B2 U2 L2 D' L2 D R2 U' F2 has RD corners, L=11, 3 spare moves. On inverse, (L2 U' B2 D F2 D L2 U2 B2 U' L2) has FD corners.

- F2 U R2 U2 F2 U'
    - After L2, 1qt edges will be RV (bad) and FH (good): +0+0+0(+3)
        - L2 U' L2 U' // no good
- **F2 U R2 B2 U2 F2 U**
    - After R2, 1qt edges will be RD (good) and FH (good): +1+0+2(+0)
        - **R2 U L2 U2 R2 U' L2 // 14**
- (R2 U' R2 U)
    - After (R2), 1qt edges will be FD (good) and RH (good), fr=1: +0+0+0(+3)
        - (R2 U R2 U2 F2 U) // no good
- **(R2 U' R2 U')**
    - After (L2 U2 R2), 1qt edges will be FD (good) and RH (good): +0+2+1(+0)
        - **(L2 U2 R2 U B2 U2 F2 L2 U' B2) // 14**

Skeleton #5 F2 U' L2 U F2 U' R2 U R2 D' U has HH corners, L=11, 3 spare moves.

- (U') B2 D' R2 D B2 U'
    - After R2, 1qt edges will be RH (good) and FV (bad): +0+0+0(+3)
        - R2 U R2 U' // no good
- Linearly: all variants have lower bound > spare moves.

Skeleton #6 F2 U R2 U' L2 U F2 U' B2 U D B2 has FD corners, L=12, 2 spare moves.

- All variants have lower bound > spare moves.

Skeleton #7 (L2 U' B2 D F2 D' F2 U D B2 D L2) on inverse has FD corners, L=12, 2 spare moves.

- All variants have lower bound > spare moves.

Skeleton #8 (L2 U' B2 D F2 D L2 U D L2 D' L2) on inverse has FD corners, L=12, 2 spare moves.

- All variants have lower bound > spare moves.

Optimal is 14. Found 14 on skeleton #4.

### 2c4, scramble 8

`R' U' F L B L' F' R' F2 R2 D R' U2 B2 L' U2 F2 B2 L2 B2 U F' R' U' F`

2c4 4e, goal 14.

Skeleton #1 U R2 U F2 U' F2 U F2 U2 has RV corners, L=9, 5 spare moves. On inverse, (U2 L2 U L2 D' B2 D F2 U') has HH corners.

- U L2 U
    - After B2 R2, 1qt edges will be RH (bad) and FV (good), fr=1: +0+1+1(+2)
        - B2 R2 U B2 R2 D // no good
- U (U2 L2 U')
    - After (R2 U2 L2 B2 R2 F2), 1qt edges will be RD (good) and FH (good): +0+5+0(+0)
        - (R2 U2 L2 B2 R2 F2 U' L2 U) // no good
- (R2 U2 L2 D' F2 D')
    - After (R2 B2 R2 F2), 1qt edges will be RH (good) and FH (good): +1+3+0(+0)
        - (R2 B2 R2 F2 U' R2 U) // no good

Skeleton #2 U' L2 U' R2 U B2 U F2 U2 R2 has DD corners, L=10, 4 spare moves. On inverse, (B2 U2 L2 U' F2 D R2 D' F2 U) has HH corners.

- U' B2 L2 U
    - After R2 B2, 1qt edges will be FV (good) and RD (good): +1+1+1(+0)
        - R2 B2 U F2 R2 U' // no good
- U' (F2 U2 R2 D')
    - After (L2 F2 B2), 1qt edges will be RD (good) and FH (good): +0+2+2(+0)
        - (L2 F2 B2 U B2 R2 L2 D') // no good
- (F2 U2 L2 D' B2 U)
    - After (R2), 1qt edges will be RH (good) and FH (good): +0+0+3(+0)
        - (R2 U' B2 L2 F2 L2 D') // no good

Skeleton #3 R2 D' R2 U' L2 U R2 D' B2 U2 has RV corners, L=10, 4 spare moves. On inverse, (U2 L2 D' F2 D L2 U' R2 U' F2) has RD corners.

- R2 D' L2 U'
    - After F2, 1qt edges will be RV (good) and FH (good), fr=1: +0+0+3(+1)
        - F2 U' F2 R2 U2 F2 U // no good
- (R2 U2 L2 D F2 D)
    - After (F2 R2), 1qt edges will be RD (good) and FH (good): +1+1+2(+0)
        - (F2 R2 U' L2 U2 L2 U) // no good

Skeleton #4 R2 D R2 D B2 D' B2 D B2 U2 L2 has DD corners, L=11, 3 spare moves. On inverse, (B2 U2 L2 U B2 U' L2 U L2 U F2) has RD corners.

- F2 L2 U' F2 U'
    - After F2, 1qt edges will be FV (good) and RD (good): +1+0+1(+0)
        - F2 U L2 B2 D' // no good
- **(B2 U2 L2 U B2 U')**
    - After (R2), 1qt edges will be RD (good) and FH (good): +0+0+3(+0)
        - **(R2 U' L2 B2 U2 L2 U R2) // 14**
- (L2 U2 R2 F2 D' F2 U')
    - After (L2 B2), 1qt edges will be RD (good) and FH (good): +1+1+0(+0)
        - (L2 B2 U' L2 U) // no good

Skeleton #5 U R2 U2 B2 U R2 D B2 D' F2 has RD corners, L=10, 4 spare moves. On inverse, (L2 U' R2 U B2 U F2 U2 R2 U) has HH corners.

- U L2 U2 F2 U
    - After R2, 1qt edges will be RD (good) and FH (good): +0+0+4(+0)
        - R2 U' F2 R2 F2 U2 B2 D' // no good
- U' (L2 U')
    - After (L2), 1qt edges will be FD (good) and RV (good): +0+0+3(+0)
        - (L2 U F2 R2 F2 B2 U) // no good
- (B2 L2 U B2 U')
    - After (L2 F2), 1qt edges will be RH (good) and FH (good): +1+1+1(+0)
        - (L2 F2 U' B2 L2 U2 R2 U') // no good

Skeleton #6 F2 U' B2 D' L2 U F2 U2 R2 D' L2 U2 has RV corners, L=12, 2 spare moves. On inverse, (U2 L2 D L2 U2 B2 D' F2 D L2 D B2) has FD corners.

- R2 F2 U R2 U
    - After F2, 1qt edges will be RV (good) and FH (good): +1+0+1(+0)
        - F2 U R2 U2 L2 F2 U // no good
- (U2 L2 D L2 U2 F2 U')
    - After (R2 B2), 1qt edges will be FD (good) and RH (good): +0+1+1(+0)
        - (R2 B2 U' F2 L2 D') // no good

Skeleton #7 R2 D B2 U2 L2 U B2 U' L2 D B2 has RD corners, L=11, 3 spare moves. On inverse, (L2 U B2 U' R2 U B2 U2 R2 U F2) has RD corners.

- L2 U R2 U2 R2 F2 U'
    - After F2 L2, 1qt edges will be RD (good) and FH (good): +1+1+0(+0)
        - F2 L2 U R2 U // no good
- (F2 L2 U' R2 U)
    - After (B2), 1qt edges will be RD (good) and FH (good): +1+0+2(+0)
        - (B2 U R2 U2 R2 L2 F2 D) // no good

Skeleton #8 U R2 U F2 U' F2 U' B2 D U R2 has RD corners, L=11, 3 spare moves.

- U B2 R2 U' L2 D F2 D
    - After R2, 1qt edges will be RD (good) and FH (good): +1+0+2(+0)
        - R2 U' R2 L2 D // no good

Optimal is 14. Found 14 on skeleton #4.

### 2c4, scramble 9

`R' U' F U' F' U' D2 L' B2 U' F' D2 R D2 L2 U2 L B2 R' B2 U2 B2 U' R' U' F`

2c4 6e, goal 14.

Skeleton #1 R2 D R2 U' B2 D B2 U B2 U2 has FV corners, L=10, 4 spare moves. On inverse, (U2 F2 U' R2 D' B2 D F2 U' R2) has RD corners.

- B2 R2 D' F2 U
    - After R2 F2, 1qt edges will be FV (good) and RH (good): +1+1+2(+0)
        - R2 F2 U' B2 U2 B2 U' // no good
- (U2 F2 U' F2 R2 U)
    - After (B2), 1qt edges will be RD (good) and FH (good): +1+0+3(+0)
        - (B2 U F2 L2 U2 B2 U') // no good

Skeleton #2 R2 D' R2 U F2 D' F2 U' B2 U2 has RV corners, L=10, 4 spare moves. On inverse, (U2 L2 D' B2 U' L2 D L2 U' F2) has RD corners.

- L2 U' L2 U
    - After R2 B2, 1qt edges will be RV (good) and FH (good): +0+1+1(+0)
        - R2 B2 U F2 R2 U' // no good
- (U2 R2 U' B2 D')
    - After (F2), 1qt edges will be RD (good) and FD (good): +0+0+3(+1)
        - (F2 U L2 F2 R2 B2 D) // no good

Skeleton #3 U2 L2 D L2 U' B2 U F2 D B2 U2 has RV corners, L=11, 3 spare moves. On inverse, (U2 L2 D B2 U R2 D' R2 U F2 U2) has RV corners.

- U2 R2 U R2 D'
    - After B2 L2 F2 B2, 1qt edges will be RV (good) and FH (good): +0+3+0(+0)
        - B2 L2 F2 B2 U' B2 U // no good
- (R2 U2 R2 U' B2 D)
    - After (R2 B2), 1qt edges will be RV (good) and FH (good), fr=1: +1+1+0(+1)
        - (R2 B2 U L2 U') // no good

Skeleton #4 U2 L2 D' R2 U R2 U' B2 D' B2 U2 has FV corners, L=11, 3 spare moves. On inverse, (U2 F2 U R2 D B2 U' B2 D L2 U2) has RV corners.

- U2 F2 L2 D F2 U'
    - After L2, 1qt edges will be FV (good) and RH (good), fr=1: +1+0+1(+1)
        - L2 U B2 R2 D // no good
- (U2 F2 U F2 R2 U')
    - After (B2), 1qt edges will be RV (good) and FH (good), fr=1: +1+0+1(+1)
        - (B2 U F2 R2 D') // no good

Skeleton #5 R2 U F2 U2 L2 U' R2 U' F2 U has HH corners, L=10, 4 spare moves. On inverse, (U' F2 U R2 U F2 U2 R2 U' R2) has RD corners.

- (U') R2 U
    - After F2 R2 U2 B2 R2, 1qt edges will be FD (good) and RD (good): +0+2+1(+1)
        - F2 R2 U2 B2 R2 U' F2 R2 U' // no good
- L2 U B2 U2 R2 D'
    - After R2 B2, 1qt edges will be RH (good) and FH (good): +0+1+2(+0)
        - R2 B2 U' L2 F2 B2 D // no good
- (U' R2 F2 U')
    - After (F2 R2 L2), 1qt edges will be RD (good) and FH (good): +1+2+1(+0)
        - (F2 R2 L2 U F2 U2 F2 L2 U) // no good

Skeleton #6 U2 L2 U B2 U2 R2 U' L2 U' F2 U' has HH corners, L=11, 3 spare moves. On inverse, (U L2 U' L2 U L2 U2 F2 U' R2 U2) has RV corners.

- **(U) U2 B2 R2 U'**
    - After R2 L2 F2 U2 R2, 1qt edges will be RD (good) and FH (good): +1+2+0(+0)
        - **R2 L2 F2 U2 R2 U L2 U L2 // 14**
- **(U) U2 B2 R2 U**
    - After R2 U2 B2 R2 L2, 1qt edges will be RD (good) and FH (good): +1+2+0(+0)
        - R2 U2 B2 R2 L2 U' B2 U' // no good
    - After L2 U2 R2 L2 F2, 1qt edges will be RD (good) and FH (good): +1+2+0(+0)
        - **L2 U2 R2 L2 F2 U' L2 U L2 // 14**
- U2 L2 D R2 U2 B2 D'
    - After B2, 1qt edges will be RV (bad) and FH (good): +0+0+0(+3)
        - B2 U' L2 U' // no good
- **(U L2 U')**
    - After (L2), 1qt edges will be RV (good) and FV (good), fr=1: +0+0+1(+2)
        - (L2 U F2 R2 U2 L2 U') // no good
        - **(L2 U F2 L2 U2 L2 U' R2 B2 U2 L2) // 14**
    - After (L2), 1qt edges will be RV (good) and FV (good): +0+0+2(+1)
        - **(L2 U F2 R2 L2 U2 L2 U' R2 B2 U2) // 14**
        - **(L2 U' R2 U2 F2 R2 L2 U R2 B2 U2) // 14**

Skeleton #7 (U' F2 U R2 U F2 D U B2 D' R2) on inverse has RD corners, L=11, 3 spare moves.

- All variants have lower bound > spare moves.

Skeleton #8 (U' F2 U R2 U' R2 U D R2 D L2) on inverse has RD corners, L=11, 3 spare moves.

- All variants have lower bound > spare moves.

Optimal is 14. Found 14 on skeleton #6.

### 2c4, scramble 10

`R' U' F R F U F D' F' U2 R' U' R' U2 F2 D2 B2 R2 B2 U R2 F2 B2 R' U' F`

2c4 6e, goal 14.

Skeleton #1 F2 D' L2 U F2 D' R2 U L2 has FD corners, L=9, 5 spare moves. On inverse, (F2 U F2 U' R2 U R2 U' R2) has FD corners.

- B2 U' R2 U
    - After F2 L2, 1qt edges will be FD (good) and RD (good): +0+1+3(+1)
        - F2 L2 U B2 R2 F2 B2 D' // no good
- (B2 D F2 U')
    - After (F2 R2 F2 R2), 1qt edges will be FD (good) and RH (good): +0+3+2(+0)
        - (F2 R2 F2 R2 U' R2 L2 B2 D) // no good

Skeleton #2 L2 U2 B2 D' F2 U F2 U' R2 D F2 has FD corners, L=11, 3 spare moves. On inverse, (B2 D' F2 U B2 U' F2 D F2 U2 R2) has DD corners.

- L2 U2 B2 D' L2 B2 U'
    - After R2 F2, 1qt edges will be FD (good) and RD (good): +1+1+0(+1)
        - R2 F2 U' F2 U // no good
- (F2 U' F2 U)
    - After (F2 R2), 1qt edges will be FD (good) and RV (good): +0+1+1(+0)
        - (F2 R2 U F2 R2 U') // no good

Skeleton #3 B2 U L2 U' B2 U L2 U' R2 U2 has FV corners, L=10, 4 spare moves. On inverse, (U2 F2 D' F2 U R2 U' L2 D R2) has FD corners.

- F2 D L2 U'
    - After F2, 1qt edges will be FV (good) and RH (good): +0+0+4(+0)
        - F2 U R2 U2 B2 L2 B2 U' // no good
- (U2 F2 D' F2 U)
    - After (R2), 1qt edges will be FD (good) and RD (good): +0+0+3(+1)
        - (R2 U' L2 F2 R2 F2 D') // no good

Skeleton #4 L2 U2 B2 D F2 U' F2 U L2 D' F2 U2 has FV corners, L=12, 2 spare moves. On inverse, (U2 B2 U F2 U' F2 D R2 D B2 U2 L2) has DD corners.

- L2 U2 B2 D B2 U'
    - After F2 R2, 1qt edges will be FV (good) and RV (good): +0+1+0(+1)
        - F2 R2 U' F2 U // no good
- On inverse: all variants have lower bound > spare moves.

Skeleton #5 U2 B2 D R2 U' R2 U R2 U2 B2 D' F2 has FD corners, L=12, 2 spare moves. On inverse, (B2 D B2 U2 L2 U' B2 U' L2 D L2 U2) has FV corners.

- U2 B2 D F2 L2 U
    - After R2, 1qt edges will be FD (good) and RH (good): +1+0+0(+0)
        - R2 U L2 U2 B2 D' // no good
- (F2 U F2 U2 R2 U')
    - After (R2), 1qt edges will be FV (good) and RV (good), fr=1: +0+0+0(+2)
        - (R2 U' R2 U') // no good

Skeleton #6 L2 U' R2 D L2 D' F2 U B2 U' R2 U' has HH corners, L=12, 2 spare moves. On inverse, (U R2 U B2 U' F2 U B2 U' R2 U R2) has RD corners.

- (U) R2 D' B2 L2 D' F2 D
    - After B2, 1qt edges will be RD (good) and FD (good): +1+0+0(+1)
        - B2 U' F2 U' // no good
- Linearly: all variants have lower bound > spare moves, or reach HTR with no move left.
- On inverse: all variants have lower bound > spare moves.

Skeleton #7 L2 U R2 U' R2 U F2 U' F2 U R2 U' has HH corners, L=12, 2 spare moves. On inverse, (U R2 U' F2 U F2 U' R2 U R2 U' R2) has RD corners.

- With the premove (U): all variants have lower bound > spare moves.
- R2 D R2 U' F2 D B2 D'
    - After B2 R2, 1qt edges will be RH (good) and FH (good): +0+1+0(+0)
        - B2 R2 U' L2 U // no good
- On inverse: all variants have lower bound > spare moves.

Skeleton #8 U L2 U R2 D F2 U' L2 U R2 D L2 has FD corners, L=12, 2 spare moves. On inverse, (B2 U R2 U B2 U' L2 U L2 U F2 U') has HH corners.

- All variants have lower bound > spare moves.

Optimal is 15. Found none.

## 2c3

### 2c3, scramble 1

`R' U' F R' F U2 D B R2 F2 D U2 B2 L' D2 F2 B2 R' L2 B2 U2 R2 U2 R' U' F`

2c3 2e, goal 13.

Skeleton #1 U2 B2 U L2 U' L2 U F2 has FD corners, L=8, 5 spare moves. On inverse, (F2 U' L2 U F2 U' F2 U2) has FV corners.

- **U2 L2 F2 U'**
    - After L2, 1qt edges will be FD (good) and RH (good): +1+0+3(+0)
        - **L2 U F2 B2 R2 F2 D B2 // 12**
- F2 U2 B2 U'
    - After B2 L2, 1qt edges will be FD (good) and RD (good): +1+1+2(+1)
        - B2 L2 U' R2 U2 L2 U' // no good
- **(B2 D')**
    - After (L2), 1qt edges will be FH (bad) and RV (good): +0+0+0(+3)
        - **(L2 U B2 U' R2 B2 R2 F2 R2 U2) // 12**
    - After (F2 R2 F2 B2), 1qt edges will be FV (good) and RV (good): +0+3+0(+1)
        - **(F2 R2 F2 B2 U' L2 U F2 L2 U2) // 12**
- (F2 U')
    - After (F2 L2 F2 B2), 1qt edges will be FV (good) and RV (good): +0+3+1(+1)
        - (F2 L2 F2 B2 U' L2 F2 D') // no good
- **(R2 F2 U)**
    - After (R2 B2), 1qt edges will be FV (good) and RH (good): +1+1+0(+0)
        - **(R2 B2 U B2 U' R2 L2 B2 U2) // 12**

Skeleton #2 F2 U' L2 U L2 U' F2 U2 has FV corners, L=8, 5 spare moves. On inverse, (U2 B2 U F2 U' L2 U F2) has FD corners.

- **F2 U'**
    - After B2 L2, 1qt edges will be FV (good) and RV (good): +0+1+0(+1)
        - **B2 L2 U' B2 U B2 L2 U2 R2 L2 // 12**
- L2 F2 U
    - After F2, 1qt edges will be FD (bad) and RH (good): +1+0+1(+3)
        - F2 U' L2 F2 U' // no good
- **(U2 B2 U)**
    - After (B2), 1qt edges will be FD (good) and RD (good): +0+0+1(+1)
        - **(B2 U' R2 B2 U R2 L2 U2 F2 L2) // 13**
- (U2 R2 B2 U')
    - After (F2 R2), 1qt edges will be FH (bad) and RH (good): +1+1+0(+3)
        - (F2 R2 U' F2 U) // no good

Skeleton #3 L2 U2 B2 U' R2 U B2 U R2 U2 F2 has DD corners, L=11, 2 spare moves. On inverse, (F2 U2 L2 U' B2 U' R2 U F2 U2 R2) has DD corners.

- L2 U2 F2 D'
    - After R2, 1qt edges will be FV (good) and RD (good): +0+0+0(+0)
        - R2 U F2 U' // no good
- **B2 U2 F2 R2 D**
    - After R2, 1qt edges will be FV (good) and RV (good): +1+0+0(+1)
        - **R2 U F2 U' B2 R2 D2 L2 // 13**
- (B2 U2 L2 D')
    - After (B2), 1qt edges will be FD (good) and RD (good): +0+0+0(+2)
        - (B2 U' L2 U') // no good
- **(L2 U2 L2 F2 D)**
    - After (L2), 1qt edges will be FV (good) and RV (good): +1+0+0(+1)
        - **(L2 U' F2 U' R2 F2 U2 B2) // 13**

Skeleton #4 (F2 U' L2 U' B2 U D R2 D B2 U2) on inverse has FV corners, L=11, 2 spare moves.

- All variants have lower bound > spare moves.

Skeleton #5 (B2 U' B2 U F2 U' L2 U D) on inverse has HH corners, L=9, 4 spare moves.

- D' (L2 F2 D R2 U')
    - After (F2), 1qt edges will be RH (good) and FH (good): +1+0+1(+0)
        - (F2 U R2 F2 U') // no good
- On inverse, linearly: all variants have lower bound > spare moves, or reach HTR with no move left.

Skeleton #6 (F2 U' L2 U F2 U B2 U D R2) on inverse has FD corners, L=10, 3 spare moves.

- All variants have lower bound > spare moves.

Skeleton #7 (B2 D' R2 D L2 D U' L2 D L2 U2) on inverse has FV corners, L=11, 2 spare moves.

- (F2 U' R2 U B2 D)
    - After (F2 B2), 1qt edges will be FV (good) and RH (good): +0+2+0(+0)
        - (F2 B2 U' R2 U) // no good

Skeleton #8 F2 D' B2 D L2 U' F2 D U has HH corners, L=9, 4 spare moves.

- (U') F2 D' R2 B2 U'
    - After R2, 1qt edges will be RH (good) and FH (good): +1+0+1(+0)
        - R2 U R2 F2 D' // no good
- Linearly: all variants have lower bound > spare moves, or reach HTR with no move left.

Optimal is 12. Found 12 on skeleton #1.

### 2c3, scramble 2

`R' U' F D' F2 L2 B2 D' B2 U2 R2 U2 R2 U' R' B L U L D' R' F' R' U' F`

2c3 6e, goal 13.

Skeleton #1 U F2 U' F2 D' has HH corners, L=5, 8 spare moves. On inverse, (D F2 D B2 U') has HH corners.

- **(D)**
    - After U2 F2 L2 F2, 1qt edges will be FD (good) and RD (good): +4+2(+1)
        - **U2 F2 L2 F2 U F2 B2 R2 D F2 R2 // 12**
    - After U2 F2 B2, 1qt edges will be FD (good) and RH (good): +3+4(+0)
        - U2 F2 B2 U' F2 R2 F2 L2 B2 D' // no good
- **(D')**
    - After R2 L2, 1qt edges will be FV (good) and RH (good): +2+0(+0)
        - **R2 L2 U R2 U R2 U2 R2 B2 D2 R2 F2 // 13**
    - After R2 L2, 1qt edges will be FV (good) and RH (good), fr=1: +2+2(+1)
        - **R2 L2 U' L2 U2 R2 U' R2 L2 B2 D2 F2 // 13**
- **U**
    - After R2 L2 B2, 1qt edges will be RD (bad) and FH (good): +0+2+3(+3)
        - **R2 L2 B2 U' R2 F2 L2 F2 D F2 L2 B2 // 13**
        - **R2 L2 B2 U' R2 B2 L2 B2 D B2 L2 F2 // 13**
- U'
    - After B2 L2 B2 U2 R2, 1qt edges will be RH (good) and FD (bad): +0+4+1(+3)
        - B2 L2 B2 U2 R2 U B2 L2 D' // no good
- **U**
    - After (F2 L2 F2), 1qt edges will be FD (good) and RH (good): +3+3(+0)
        - (F2 L2 F2 U' F2 L2 B2 L2 U') // no good
    - After (F2 R2 B2), 1qt edges will be FD (good) and RH (good): +3+3(+0)
        - **(F2 R2 B2 U' L2 B2 L2 F2 D B2 R2 L2) // 13**
    - After (B2 R2 F2), 1qt edges will be FD (good) and RH (good): +3+3(+0)
        - **(B2 R2 F2 U' R2 B2 R2 F2 D B2 R2 L2) // 13**
- **(D)**
    - After (R2 F2), 1qt edges will be RV (bad) and FH (good): +0+1+2(+3)
        - **(R2 F2 U' B2 R2 L2 D' F2 L2 F2 U2) // 12**
    - After (L2 B2), 1qt edges will be RV (bad) and FH (good): +0+1+4(+3)
        - (L2 B2 U' R2 U2 B2 L2 B2 U') // no good
- **(D')**
    - After (F2 U2 F2 R2 L2), 1qt edges will be RH (good) and FH (good): +0+4+2(+0)
        - **(F2 U2 F2 R2 L2 U L2 U2 R2 U L2 R2) // 13**
    - After (R2 L2 B2 U2 F2), 1qt edges will be RH (good) and FH (good): +0+4+2(+0)
        - **(R2 L2 B2 U2 F2 U R2 U2 L2 U R2 L2) // 13**
    - After (F2 L2 U2 F2 R2 U2 R2), 1qt edges will be RH (good) and FH (good): +0+6+0(+0)
        - **(F2 L2 U2 F2 R2 U2 R2 U' L2 U' L2 R2) // 13**
    - After (F2 R2 U2 F2 L2 U2 L2), 1qt edges will be RH (good) and FH (good): +0+6+0(+0)
        - **(F2 R2 U2 F2 L2 U2 L2 U' L2 U' L2 R2) // 13**

Skeleton #2 U2 F2 U F2 D R2 D B2 has FD corners, L=8, 5 spare moves. On inverse, (F2 D' B2 U' B2 D' B2 U2) has FV corners.

- U2 F2 U
    - After L2 B2, 1qt edges will be FD (good) and RD (good): +0+1+3(+1)
        - L2 B2 U' R2 B2 R2 L2 D // no good
- (F2 D')
    - After (L2 F2 L2 B2 R2), 1qt edges will be FV (good) and RH (good): +0+4+0(+0)
        - (L2 F2 L2 B2 R2 U' F2 U') // no good

Skeleton #3 U2 R2 U F2 U R2 U R2 has RD corners, L=8, 5 spare moves. On inverse, (R2 U' L2 D' R2 D' L2 U2) has RV corners.

- U2 R2 U
    - After F2, 1qt edges will be RD (good) and FD (good): +0+0+2(+1)
        - F2 U R2 F2 B2 D // no good
- (R2 U')
    - After (F2 R2), 1qt edges will be RV (good) and FV (good): +0+1+3(+1)
        - (F2 R2 U L2 F2 R2 L2 D') // no good

Skeleton #4 U F2 U D U R2 D' has HH corners, L=7, 6 spare moves. On inverse, (D F2 D U D' R2 U') has HH corners.

- **(D) U F2 U**
    - After R2 F2 R2, 1qt edges will be FD (good) and RH (good): +0+3+3(+0)
        - **R2 F2 R2 U' R2 F2 R2 U B2 // 13**
    - After L2 F2 L2, 1qt edges will be FD (good) and RH (good): +0+3+3(+0)
        - **L2 F2 L2 U' L2 F2 L2 U B2 // 13**
    - After R2 B2 L2, 1qt edges will be FD (good) and RH (good): +0+3+3(+0)
        - R2 B2 L2 U B2 L2 B2 U' // no good
- **U (D B2 U')**
    - After (R2 F2 R2), 1qt edges will be FD (good) and RH (good): +0+3+3(+0)
        - **(R2 F2 R2 U R2 F2 R2 U' F2) // 13**
    - After (L2 F2 L2), 1qt edges will be FD (good) and RH (good): +0+3+3(+0)
        - **(L2 F2 L2 U L2 F2 L2 U' F2) // 13**
    - After (R2 B2 L2), 1qt edges will be FD (good) and RH (good): +0+3+3(+0)
        - (R2 B2 L2 U' F2 R2 F2 U) // no good

Skeleton #5 U F2 U' B2 D U D has HH corners, L=7, 6 spare moves.

- (D') U L2 B2 D
    - After R2, 1qt edges will be RH (good) and FH (good): +1+0+3(+0)
        - R2 U' R2 B2 R2 U' // no good
- Linearly: all variants have lower bound > spare moves, or reach HTR with no move left.

Skeleton #6 (D F2 D B2 U D U) on inverse has HH corners, L=7, 6 spare moves.

- **U' (D L2 F2 D')**
    - After (L2), 1qt edges will be RD (bad) and FH (good): +1+0+2(+3)
        - **(L2 U R2 L2 D B2 L2 B2) // 13**
        - (L2 U' R2 L2 D) // no good
- On inverse, linearly: all variants have lower bound > spare moves, or reach HTR with no move left.

Skeleton #7 U F2 U B2 U D R2 D has HH corners, L=8, 5 spare moves. On inverse, (D' B2 U D L2 U' F2 U') has HH corners.

- With the premove (D'): all variants have lower bound > spare moves.
- Linearly: all variants have lower bound > spare moves.
- U (D' F2 U)
    - After (R2 L2), 1qt edges will be FV (bad) and RH (good), fr=1: +0+2+0(+3)
        - (R2 L2 U R2 U) // no good

Skeleton #8 U' F2 U D R2 D B2 D' has HH corners, L=8, 5 spare moves. On inverse, (D F2 D' F2 U D R2 U) has HH corners.

- (D) U' B2 U
    - After R2 L2, 1qt edges will be FV (bad) and RH (good), fr=1: +0+2+0(+3)
        - R2 L2 U R2 U' // no good
- On inverse, with the premove U': all variants have lower bound > spare moves.
- On inverse, linearly: all variants have lower bound > spare moves.

Hard to find solutions:

Skeleton U R2 U D' L2 D R2 D' has HH corners, L=8, 5 spare moves.

- **(D) U R2 U'**
    - After F2 L2 B2, 1qt edges will be FD (good) and RH (good): +0+3+0(+0)
        - **F2 L2 B2 U' B2 U' B2 L2 R2 // 13**

Optimal is 12. Found 12 on skeleton #1.

### 2c3, scramble 3

`R' U' F D F2 L' B2 R2 U2 R' D2 R' F2 U2 R F' R' B2 R' U' R D' R' U' F`

2c3 6e, goal 13.

Skeleton #1 U F2 U R2 U R2 has FD corners, L=6, 7 spare moves. On inverse, (B2 U B2 U R2 U') has HH corners.

- **U'**
    - After L2 F2 U2 L2, 1qt edges will be FD (good) and RD (good): +0+3+3(+1)
        - **L2 F2 U2 L2 U R2 B2 R2 L2 D F2 L2 // 13**
    - After R2 F2 U2 R2 F2 B2, 1qt edges will be FD (good) and RD (good): +0+5+1(+1)
        - R2 F2 U2 R2 F2 B2 U F2 R2 D' // no good
    - After R2 B2 U2 F2 B2 L2, 1qt edges will be FD (good) and RD (good): +0+5+1(+1)
        - **R2 B2 U2 F2 B2 L2 U R2 F2 D B2 R2 // 13**
- U
    - After (B2), 1qt edges will be FH (bad) and RD (good), fr=1: +0+3(+3)
        - (B2 U L2 F2 R2 L2 U') // no good
- **U'**
    - After (L2 F2), 1qt edges will be FD (bad) and RV (good), fr=1: +1+1(+2)
        - **(L2 F2 U' L2 F2 D' R2 F2 B2 D2 B2 R2) // 13**
    - After (L2 F2), 1qt edges will be FD (bad) and RV (good), fr=1: +1+3(+2)
        - **(L2 F2 U' F2 B2 L2 B2 D' L2 U2 F2 L2) // 13**
- (B2 U')
    - After (R2 B2 U2 B2 L2), 1qt edges will be RH (good) and FH (good): +0+4+2(+0)
        - (R2 B2 U2 B2 L2 U' R2 L2 B2 D) // no good

Skeleton #2 L2 U' L2 U' F2 U has HH corners, L=6, 7 spare moves. On inverse, (U' R2 D' L2 D' B2) has RD corners.

- With the premove (U'): all variants have lower bound > spare moves.
- F2 L2 U
    - After F2, 1qt edges will be RH (good) and FH (good): +1+0+5(+0)
        - F2 U F2 U2 B2 L2 U2 B2 D // no good
- (U')
    - After (F2 L2 B2 L2 F2), 1qt edges will be RD (good) and FH (good): +0+4+3(+0)
        - (F2 L2 B2 L2 F2 U B2 U2 L2 F2 U) // no good

Skeleton #3 B2 D' L2 U' B2 D' L2 has RD corners, L=7, 6 spare moves. On inverse, (R2 D L2 U F2 D B2) has FD corners.

- B2 D'
    - After B2 U2 F2 R2 U2 R2 B2, 1qt edges will be RD (good) and FH (good): +0+6+0(+0)
        - B2 U2 F2 R2 U2 R2 B2 U' R2 U // no good
- (R2 D)
    - After (B2 R2 F2 L2 F2), 1qt edges will be FD (good) and RH (good): +0+4+2(+0)
        - (B2 R2 F2 L2 F2 U' R2 U2 L2 U) // no good

Skeleton #4 U F2 U R2 U D U' B2 has FD corners, L=8, 5 spare moves.

- All variants have lower bound > spare moves.

Skeleton #5 (U' R2 D' L2 D U D R2) on inverse has RD corners, L=8, 5 spare moves.

- All variants have lower bound > spare moves.

Skeleton #6 (B2 U B2 U L2 U D' U') on inverse has HH corners, L=8, 5 spare moves.

- All variants have lower bound > spare moves.

Skeleton #7 L2 U' L2 U' B2 U D' U has HH corners, L=8, 5 spare moves.

- All variants have lower bound > spare moves.

Skeleton #8 (R2 D L2 U F2 D U D' R2) on inverse has FD corners, L=9, 4 spare moves.

- All variants have lower bound > spare moves.

Optimal is 13. Found 13 on skeleton #1.

### 2c3, scramble 4

`R' U' F R2 D2 B U F U2 F D' B2 D2 B2 L' U2 L' D2 L F' R D R' U' F`

2c3 6e, goal 13.

Skeleton #1 U2 R2 U' B2 U' R2 D' has HH corners, L=7, 6 spare moves. On inverse, (D L2 U L2 D L2 U2) has RV corners.

- (D)
    - After L2 U2 R2, 1qt edges will be RH (bad) and FH (good), fr=1: +1+2(+3)
        - L2 U2 R2 U F2 R2 L2 D // no good
- **U2 F2 L2 U**
    - After L2 B2, 1qt edges will be RH (good) and FD (bad): +1+1+1(+3)
        - **L2 B2 U' F2 L2 U L2 F2 R2 // 13**
        - L2 B2 U' B2 R2 D' // no good
- (D)
    - After (L2 U2 F2 B2), 1qt edges will be RH (bad) and FH (good): +0+3+0(+3)
        - (L2 U2 F2 B2 U' F2 U) // no good

Skeleton #2 U' F2 D B2 D L2 has RD corners, L=6, 7 spare moves. On inverse, (L2 U' L2 U' F2 U) has HH corners.

- **U'**
    - After L2 F2, 1qt edges will be RD (good) and FH (good): +0+1+4(+0)
        - L2 F2 U' B2 U2 L2 F2 R2 D' // no good
        - **L2 F2 U' B2 U2 R2 F2 L2 D' L2 B2 F2 // 13**
- **U'**
    - After (F2 B2 R2), 1qt edges will be FD (good) and RD (good): +2+4(+1)
        - (F2 B2 R2 U' R2 B2 R2 B2 R2 U') // no good
        - **(F2 B2 R2 U F2 R2 B2 U2 L2 D B2 R2) // 13**
- **(L2 U')**
    - After (B2 L2), 1qt edges will be RH (good) and FH (good): +0+1+3(+0)
        - **(B2 L2 U F2 L2 F2 B2 D' F2 B2 U2) // 13**
    - After (R2 L2 B2 R2), 1qt edges will be RH (good) and FH (good): +0+3+1(+0)
        - **(R2 L2 B2 R2 U B2 L2 D' F2 B2 U2) // 13**
- (F2 R2 U)
    - After (F2 B2 L2), 1qt edges will be RV (bad) and FH (good): +1+2+1(+3)
        - (F2 B2 L2 U R2 B2 U') // no good
- **(B2 R2 D)**
    - After (R2 B2 U2 F2 B2), 1qt edges will be RH (good) and FH (good): +1+4+0(+0)
        - **(R2 B2 U2 F2 B2 U R2 U L2 R2) // 13**
- **(B2 R2 D')**
    - After (F2 B2 U2 L2 B2), 1qt edges will be RH (good) and FH (good): +1+4+0(+0)
        - **(F2 B2 U2 L2 B2 U' L2 U R2 L2) // 13**

Skeleton #3 U2 B2 U' B2 U' B2 U' R2 has FD corners, L=8, 5 spare moves. On inverse, (F2 U' R2 U' R2 U' R2 U2) has FV corners.

- **U2 L2 F2 U**
    - After L2 B2, 1qt edges will be FD (good) and RH (good): +1+1+1(+0)
        - L2 B2 U' F2 L2 U // no good
    - After F2, 1qt edges will be FD (good) and RD (good): +1+0+3(+1)
        - **F2 U F2 L2 F2 B2 U' B2 R2 // 13**
- (F2 U')
    - After (R2), 1qt edges will be FD (bad) and RH (good), fr=1: +0+0+3(+2)
        - (R2 U F2 L2 U2 B2 U') // no good
- **(L2 F2 U)**
    - After (F2 B2 R2 B2), 1qt edges will be FV (good) and RV (good): +1+3+0(+1)
        - **(F2 B2 R2 B2 U' B2 U' B2 R2 D2) // 13**

Skeleton #4 U' F2 D B2 D U D' B2 has RD corners, L=8, 5 spare moves.

- All variants have lower bound > spare moves.

Skeleton #5 (L2 U' L2 U D U R2 U) on inverse has HH corners, L=8, 5 spare moves.

- All variants have lower bound > spare moves.

Skeleton #6 (L2 U' L2 U' F2 U D U') on inverse has HH corners, L=8, 5 spare moves.

- U (L2 U' B2 L2 U)
    - After (F2 R2), 1qt edges will be RH (good) and FH (good): +1+1+2(+0)
        - (F2 R2 U F2 B2 D') // no good
- On inverse, linearly: all variants have lower bound > spare moves.

Skeleton #7 U2 L2 D' L2 U D' L2 U B2 D' has HH corners, L=10, 3 spare moves. On inverse, (D L2 U B2 U D' B2 U' F2 U2) has RV corners.

- (D) U2 L2 D' R2 D
    - After F2 L2 F2, 1qt edges will be RD (good) and FH (good): +0+3+0(+0)
        - F2 L2 F2 U B2 U // no good
- On inverse: all variants have lower bound > spare moves.

Skeleton #8 U2 R2 U B2 U D L2 D L2 D' has HH corners, L=10, 3 spare moves. On inverse, (D L2 U' R2 U D F2 U' L2 U2) has RV corners.

- All variants have lower bound > spare moves.

Hard to find solutions:

Skeleton U2 R2 U' B2 D' F2 D' B2 D U' L2 has FD corners, L=11, 2 spare moves.

- **U2 R2 U' B2 D' F2 D'**
    - After F2, 1qt edges will be FD (good) and RH (good): +0+0+2(+0)
        - **F2 U' F2 B2 D F2 // 13**

Optimal is 13. Found 13 on skeleton #1.

### 2c3, scramble 5

`R' U' F R2 D' R' L' B U' F' L U2 L2 D' R2 F2 U2 L2 D2 L2 U R' B R' U' F`

2c3 4e, goal 13.

Skeleton #1 R2 U F2 D' L2 D R2 has FD corners, L=7, 6 spare moves. On inverse, (B2 D R2 U' R2 D B2) has RD corners.

- **L2 U**
    - After R2, 1qt edges will be FD (good) and RH (good): +0+0+4(+0)
        - R2 U F2 L2 F2 U2 L2 U // no good
    - After R2, 1qt edges will be FD (good) and RH (good): +0+0+6(+0)
        - **R2 U R2 L2 B2 R2 F2 U2 R2 D' F2 // 13**
        - **R2 U F2 R2 B2 R2 L2 U2 R2 D' F2 // 13**
        - **R2 U B2 R2 B2 U2 F2 B2 R2 D' B2 // 13**
- **(B2 D)**
    - After (R2 F2 B2 U2 B2 R2 B2), 1qt edges will be RD (good) and FH (good): +0+6+0(+0)
        - **(R2 F2 B2 U2 B2 R2 B2 U' R2 U' L2) // 13**
    - After (L2 U2 B2 L2 F2 R2 L2), 1qt edges will be RD (good) and FH (good): +0+6+0(+0)
        - **(L2 U2 B2 L2 F2 R2 L2 U' L2 U' R2) // 13**
    - After (L2 U2 R2 L2 F2 L2 B2), 1qt edges will be RD (good) and FH (good): +0+6+0(+0)
        - **(L2 U2 R2 L2 F2 L2 B2 U' L2 U' R2) // 13**
- **(F2 U)**
    - After (F2 B2 L2), 1qt edges will be RV (bad) and FH (good): +0+2+0(+3)
        - **(F2 B2 L2 U' F2 U' B2 R2 F2 D2 R2) // 13**
- (B2 D')
    - After (F2 R2 U2 B2), 1qt edges will be RD (good) and FD (good): +0+3+2(+1)
        - (F2 R2 U2 B2 U B2 U2 B2 U) // no good

Skeleton #2 U2 R2 U' B2 D L2 D' R2 U2 has FV corners, L=9, 4 spare moves. On inverse, (U2 F2 U' B2 U B2 U' F2 U2) has RV corners.

- U2 R2 U'
    - After F2, 1qt edges will be FH (bad) and RV (good), fr=1: +0+0+2(+2)
        - F2 U' R2 U2 R2 U' // no good
- (U2 L2 F2 U')
    - After (R2 U2 L2), 1qt edges will be RV (good) and FH (good), fr=1: +1+2+0(+1)
        - (R2 U2 L2 U F2 U') // no good

Skeleton #3 (B2 D R2 U' B2 U D' F2 U' R2) on inverse has RD corners, L=10, 3 spare moves.

- (B2 D R2 U' F2 U')
    - After (B2 L2 B2), 1qt edges will be RD (good) and FH (good): +0+3+0(+0)
        - (B2 L2 B2 U' B2 U) // no good

Skeleton #4 (B2 D R2 U' R2 D R2 U D' R2) on inverse has FD corners, L=10, 3 spare moves.

- (B2 D R2 U' R2 D)
    - After (B2 R2), 1qt edges will be FD (good) and RH (good): +0+1+2(+0)
        - (B2 R2 U R2 L2 D') // no good

Skeleton #5 (B2 D L2 D L2 D U F2 D' B2) on inverse has RD corners, L=10, 3 spare moves.

- All variants have lower bound > spare moves.

Skeleton #6 (B2 U F2 U' F2 U F2 D' U') on inverse has HH corners, L=9, 4 spare moves.

- U (B2 U L2 F2 U)
    - After (R2), 1qt edges will be RH (good) and FH (good): +1+0+1(+0)
        - (R2 U' R2 B2 D') // no good
- On inverse, linearly: all variants have lower bound > spare moves, or reach HTR with no move left.

Skeleton #7 U2 R2 D R2 U' L2 D B2 U L2 D has HH corners, L=11, 2 spare moves. On inverse, (D' F2 D F2 U R2 U' R2 U F2 U2) has RV corners.

- All variants have lower bound > spare moves, or reach HTR with no move left.

Skeleton #8 U' R2 D L2 D L2 D' L2 D L2 U2 has FV corners, L=11, 2 spare moves. On inverse, (U2 F2 U B2 U' F2 U R2 U F2 U) has HH corners.

- U' B2 L2 U' F2 U'
    - After L2, 1qt edges will be FV (good) and RH (good), fr=1: +1+0+0(+1)
        - L2 U F2 U // no good
- U' (F2 U2 F2 U' F2 U')
    - After (L2), 1qt edges will be RD (good) and FD (good): +1+0+0(+1)
        - (L2 U F2 U) // no good
- On inverse, linearly: all variants have lower bound > spare moves.

Optimal is 13. Found 13 on skeleton #1.

### 2c3, scramble 6

`R' U' F R2 F' D' R L2 U' R2 D' F' R2 U2 F2 R2 D F2 R2 F2 U R2 D' R' U' F`

2c3 4e, goal 13.

Skeleton #1 U2 F2 D B2 U' B2 D L2 has FD corners, L=8, 5 spare moves. On inverse, (F2 D L2 D' B2 U R2 U2) has FV corners.

- U2 B2 D
    - After R2, 1qt edges will be FD (good) and RH (good): +0+0+5(+0)
        - R2 U R2 U2 L2 F2 L2 B2 D // no good
- (F2 D)
    - After (R2), 1qt edges will be FD (bad) and RV (good), fr=1: +0+0+3(+2)
        - (R2 U R2 L2 U2 B2 D') // no good

Skeleton #2 F2 U' F2 D B2 D B2 U2 L2 has DD corners, L=9, 4 spare moves. On inverse, (L2 U2 B2 D L2 U' L2 D B2) has FD corners.

- B2 D'
    - After F2, 1qt edges will be FV (good) and RD (good): +0+0+3(+0)
        - F2 U B2 L2 F2 R2 D // no good
- **(B2 U2 L2 U)**
    - After (L2), 1qt edges will be FD (good) and RD (good): +0+0+2(+1)
        - (L2 U L2 F2 B2 D) // no good
    - After (L2), 1qt edges will be FD (good) and RD (good): +0+0+3(+1)
        - **(L2 U L2 U2 F2 B2 D B2 R2) // 13**
        - **(L2 U' F2 B2 U2 L2 D' F2 L2) // 13**

Skeleton #3 F2 U2 L2 U' L2 U' B2 U F2 U2 has FV corners, L=10, 3 spare moves. On inverse, (U2 B2 U' F2 D R2 D L2 U2 B2) has DD corners.

- F2 R2 U2 L2 U
    - After B2 R2, 1qt edges will be FV (good) and RV (good): +1+1+0(+1)
        - B2 R2 U L2 U' // no good
- On inverse: all variants have lower bound > spare moves.

Skeleton #4 (F2 D L2 U' R2 U L2 U' D) on inverse has HH corners, L=9, 4 spare moves.

- D' (B2 U R2 U)
    - After (F2 U2 L2 B2), 1qt edges will be RH (good) and FH (good): +0+3+0(+0)
        - (F2 U2 L2 B2 U R2 U') // no good
- On inverse, linearly: all variants have lower bound > spare moves.

Skeleton #5 (F2 D L2 D' B2 U' L2 U D B2) on inverse has FD corners, L=10, 3 spare moves.

- All variants have lower bound > spare moves.

Skeleton #6 F2 U' F2 D B2 D' B2 D U B2 has RD corners, L=10, 3 spare moves.

- All variants have lower bound > spare moves.

Skeleton #7 F2 U' F2 D B2 D' R2 D U R2 U2 has RV corners, L=11, 2 spare moves.

- All variants have lower bound > spare moves.

Skeleton #8 F2 U' F2 D B2 D B2 U D F2 has FD corners, L=10, 3 spare moves.

- All variants have lower bound > spare moves.

Optimal is 13. Found 13 on skeleton #2.

### 2c3, scramble 7

`R' U' F U' B2 R' D B' R' D' R2 D' F' D' L2 F2 D2 L2 B2 U B2 U B2 R' U' F`

2c3 2e, goal 13.

Skeleton #1 D' B2 D F2 U R2 U2 F2 has DD corners, L=8, 5 spare moves. On inverse, (L2 U2 F2 U' L2 U R2 D) has HH corners.

- **D'**
    - After F2 R2 B2 R2, 1qt edges will be FV (good) and RD (good): +0+3+0(+0)
        - **F2 R2 B2 R2 U' R2 U L2 U2 R2 F2 U2 // 13**
    - After F2 R2 B2 R2, 1qt edges will be FV (good) and RD (good): +0+3+2(+0)
        - **F2 R2 B2 R2 U L2 U2 R2 U' F2 U2 L2 // 13**
    - After F2 L2 B2 L2, 1qt edges will be FV (good) and RD (good): +0+3+2(+0)
        - F2 L2 B2 L2 U' L2 F2 B2 D' // no good
- **D'**
    - After (B2 U2 F2 R2), 1qt edges will be FH (bad) and RD (good): +1+0(+3)
        - (B2 U2 F2 R2 U R2 U) // no good
    - After (L2 U2 F2), 1qt edges will be FH (bad) and RH (good): +0+2(+3)
        - **(L2 U2 F2 U R2 U2 L2 U' R2 B2 R2 F2) // 13**
    - After (U2 F2 R2 U2 L2), 1qt edges will be FH (bad) and RH (good): +2+0(+3)
        - **(U2 F2 R2 U2 L2 U' R2 U R2 B2 R2 F2) // 13**
- (B2 U2 F2 L2 U)
    - After (F2), 1qt edges will be RH (good) and FD (bad): +1+0+1(+3)
        - (F2 U F2 R2 U) // no good

Skeleton #2 U2 L2 U' F2 U' F2 U F2 has FD corners, L=8, 5 spare moves. On inverse, (B2 D' L2 D R2 U R2 U2) has RV corners.

- **U2 F2 L2 U**
    - After R2 F2 L2 F2, 1qt edges will be FD (good) and RH (good): +1+3+0(+0)
        - **R2 F2 L2 F2 U' R2 U B2 // 12**
- R2 U2 R2 D
    - After L2 F2, 1qt edges will be FD (good) and RD (good): +1+1+2(+1)
        - L2 F2 U' F2 U2 B2 U' // no good
- **(F2 U')**
    - After (L2), 1qt edges will be RV (good) and FV (good): +0+0+3(+1)
        - **(L2 U B2 R2 B2 L2 U' R2 B2 D2) // 12**
        - (L2 U B2 R2 F2 R2 D') // no good

Skeleton #3 U2 B2 D' L2 D' B2 U L2 U2 has FV corners, L=9, 4 spare moves. On inverse, (U2 F2 U R2 U' F2 U' R2 U2) has FV corners.

- U2 F2 U'
    - After B2 R2, 1qt edges will be FV (good) and RV (good), fr=1: +0+1+1(+2)
        - B2 R2 U B2 L2 U' // no good
- (U2 R2 B2 U')
    - After (L2), 1qt edges will be FD (bad) and RV (good), fr=1: +1+0+1(+2)
        - (L2 U R2 B2 D) // no good

Skeleton #4 D' B2 D' B2 U D L2 D R2 U2 F2 has DD corners, L=11, 2 spare moves. On inverse, (B2 U2 R2 U F2 U D R2 D B2 D) has HH corners.

- D' B2 D' F2 D
    - After R2 L2, 1qt edges will be FV (good) and RD (good): +0+2+0(+0)
        - R2 L2 U F2 U' // no good
- D' (R2 U2 F2 U F2 U)
    - After (R2 L2), 1qt edges will be FD (good) and RH (good): +0+2+0(+0)
        - (R2 L2 U L2 U') // no good

Skeleton #5 D' B2 D F2 U B2 U D B2 U2 has FV corners, L=10, 3 spare moves.

- All variants have lower bound > spare moves.

Skeleton #6 D' B2 D F2 U' F2 U D B2 U2 has RV corners, L=10, 3 spare moves.

- D' B2 D R2 F2 U
    - After R2, 1qt edges will be RV (good) and FH (good): +1+0+2(+0)
        - R2 U F2 B2 D // no good

Skeleton #7 D' B2 D R2 D U' R2 D B2 U2 L2 has DD corners, L=11, 2 spare moves. On inverse, (L2 U2 F2 U' B2 U D' B2 D' B2 D) has HH corners.

- D' B2 D R2 D'
    - After R2 L2, 1qt edges will be FD (good) and RV (good): +0+2+0(+0)
        - R2 L2 U F2 U' // no good
- On inverse, with the premove D': all variants have lower bound > spare moves.

Skeleton #8 D' B2 D F2 U R2 U D R2 has FD corners, L=9, 4 spare moves.

- D' B2 D B2 D
    - After B2 R2, 1qt edges will be FD (good) and RH (good): +0+1+3(+0)
        - B2 R2 U' B2 L2 B2 U' // no good

Hard to find solutions:

Skeleton (L2 U' R2 U L2 U L2 U' R2 D') on inverse has HH corners, L=10, 3 spare moves.

- **D (L2 U' L2 U)**
    - After (B2), 1qt edges will be FH (bad) and RH (good): +0+0+0(+3)
        - **(B2 U L2 U' R2 B2 R2 B2) // 13**

Optimal is 12. Found 12 on skeleton #2.

### 2c3, scramble 8

`R' U' F U' D2 F' L B2 U2 R2 F U' F L2 F' L2 B' L2 U2 D2 B D2 R' U' F`

2c3 2e, goal 13.

Skeleton #1 L2 U B2 U' R2 U F2 has FD corners, L=7, 6 spare moves. On inverse, (F2 U' R2 U R2 U' R2) has RD corners.

- R2 U'
    - After F2 L2 U2 F2, 1qt edges will be FD (good) and RH (good): +0+3+1(+0)
        - F2 L2 U2 F2 U' R2 F2 U' // no good
- **(B2 D)**
    - After (B2 L2 U2 B2), 1qt edges will be RD (good) and FV (bad): +0+3+0(+3)
        - (B2 L2 U2 B2 U F2 U') // no good
    - After (L2 U2 L2 B2 L2 B2), 1qt edges will be RD (good) and FD (good): +0+5+0(+1)
        - **(L2 U2 L2 B2 L2 B2 U F2 U R2 B2) // 13**

Skeleton #2 U2 R2 U' B2 U L2 U R2 U2 F2 has DD corners, L=10, 3 spare moves. On inverse, (F2 U2 R2 U' R2 U' R2 U R2 U2) has RV corners.

- U2 F2 L2 D
    - After F2 L2, 1qt edges will be FV (good) and RD (good): +1+1+0(+0)
        - F2 L2 U B2 U' // no good
- (B2 U2 L2 D)
    - After (F2 B2 U2 F2), 1qt edges will be RV (good) and FH (good): +0+3+0(+0)
        - (F2 B2 U2 F2 U' L2 U') // no good

Skeleton #3 B2 U2 R2 U R2 U' F2 U R2 U2 has FV corners, L=10, 3 spare moves. On inverse, (U2 F2 U L2 U' L2 U F2 U2 R2) has DD corners.

- R2 U2 B2 U
    - After L2 B2, 1qt edges will be FV (good) and RH (good): +0+1+1(+0)
        - L2 B2 U' R2 B2 U // no good
- **B2 U2 R2 U**
    - After R2, 1qt edges will be FV (good) and RH (good): +0+0+3(+0)
        - **R2 U R2 F2 U2 L2 D F2 D2 // 13**
- **B2 U2 R2 U'**
    - After L2 U2 R2, 1qt edges will be FV (good) and RH (good): +0+2+1(+0)
        - **L2 U2 R2 U R2 F2 D' B2 U2 // 13**
- **B2 L2 U2 R2 U'**
    - After L2, 1qt edges will be FV (good) and RH (good): +1+0+1(+0)
        - **L2 U' R2 F2 D' B2 U2 // 12**
- **(U2 B2 D)**
    - After (F2 R2), 1qt edges will be FD (good) and RV (good): +0+1+0(+0)
        - **(F2 R2 U L2 U R2 U2 L2 B2) // 12**
    - After (F2 R2), 1qt edges will be FD (good) and RV (good): +0+1+2(+0)
        - **(F2 R2 U' R2 U2 L2 U R2 U2 B2) // 13**
- (U2 F2 U)
    - After (F2 R2), 1qt edges will be FV (good) and RD (good): +0+1+1(+0)
        - (F2 R2 U B2 L2 D) // no good
- **(U2 B2 D')**
    - After (R2 U2 B2 L2), 1qt edges will be FD (good) and RV (good): +0+3+0(+0)
        - **(R2 U2 B2 L2 U' L2 U' L2 D2 B2) // 13**

Skeleton #4 (F2 U' R2 U R2 U D U B2) on inverse has RD corners, L=9, 4 spare moves.

- All variants have lower bound > spare moves.

Skeleton #5 L2 U B2 U' R2 U D U' R2 has FD corners, L=9, 4 spare moves.

- All variants have lower bound > spare moves.

Skeleton #6 (F2 U' L2 U R2 U D' L2 D F2) on inverse has RD corners, L=10, 3 spare moves.

- All variants have lower bound > spare moves.

Skeleton #7 (F2 U' R2 U R2 U' F2 U D' F2) on inverse has FD corners, L=10, 3 spare moves.

- All variants have lower bound > spare moves.

Skeleton #8 (F2 U' L2 D L2 D' B2 U D') on inverse has HH corners, L=9, 4 spare moves.

- All variants have lower bound > spare moves, or reach HTR with no move left.

Optimal is 12. Found 12 on skeleton #3.

### 2c3, scramble 9

`R' U' F R F R' B' L2 F' R2 D' R' U2 F2 U2 L2 D' B2 R2 U2 L2 R' B2 R' U' F`

2c3 6e, goal 13.

Skeleton #1 U R2 U' F2 U has HH corners, L=5, 8 spare moves. On inverse, (U' R2 U' F2 U') has HH corners.

- (U')
    - After R2 F2 R2 F2 B2, 1qt edges will be RD (good) and FD (good): +5+2(+1)
        - R2 F2 R2 F2 B2 U L2 U2 R2 U' // no good
- U'
    - After R2 U2 R2 B2 L2 F2, 1qt edges will be RH (good) and FH (good): +0+5+1(+0)
        - R2 U2 R2 B2 L2 F2 U' R2 B2 D' // no good
- U
    - After (F2 L2 B2), 1qt edges will be RD (good) and FH (good): +3+3(+0)
        - (F2 L2 B2 U' F2 L2 U2 B2 U) // no good
- (U)
    - After (F2 R2 U2 R2 B2 L2 F2 R2), 1qt edges will be RH (good) and FH (good): +0+7+0(+0)
        - (F2 R2 U2 R2 B2 L2 F2 R2 U' L2 U) // no good

Skeleton #2 U2 F2 D B2 U B2 D B2 has RD corners, L=8, 5 spare moves. On inverse, (R2 U B2 U L2 U R2 U2) has FV corners.

- U2 F2 D'
    - After B2 U2 L2 F2 R2 L2, 1qt edges will be RD (good) and FH (good): +0+5+0(+0)
        - B2 U2 L2 F2 R2 L2 U B2 U' // no good
- (R2 U)
    - After (B2), 1qt edges will be FH (bad) and RV (good), fr=1: +0+0+3(+2)
        - (B2 U L2 U2 F2 B2 D') // no good

Skeleton #3 U2 R2 U B2 D F2 D L2 has FD corners, L=8, 5 spare moves. On inverse, (F2 U R2 U R2 U F2 U2) has RV corners.

- U2 R2 U
    - After R2 F2, 1qt edges will be FD (good) and RH (good): +0+1+4(+0)
        - R2 F2 U F2 L2 U2 L2 B2 U' // no good
- (F2 U)
    - After (R2), 1qt edges will be RD (bad) and FV (good), fr=1: +0+0+3(+2)
        - (R2 U L2 F2 L2 B2 U) // no good

Skeleton #4 (U' R2 U' F2 U D' U') on inverse has HH corners, L=7, 6 spare moves.

- All variants have lower bound > spare moves.

Skeleton #5 U R2 U' B2 U D' U has HH corners, L=7, 6 spare moves.

- All variants have lower bound > spare moves.

Skeleton #6 U R2 U D U R2 U has HH corners, L=7, 6 spare moves.

- All variants have lower bound > spare moves.

Skeleton #7 U F2 U D' F2 D R2 U has HH corners, L=8, 5 spare moves. On inverse, (U' R2 U' R2 U D' L2 U') has HH corners.

- All variants have lower bound > spare moves.

Skeleton #8 U' L2 U D B2 D B2 U has HH corners, L=8, 5 spare moves. On inverse, (U' R2 U F2 D U R2 U) has HH corners.

- All variants have lower bound > spare moves, or reach HTR with no move left.

Hard to find solutions:

Skeleton L2 D' F2 D' B2 U' L2 U B2 U' has HH corners, L=10, 3 spare moves. On inverse, (U R2 D F2 U' F2 D' R2 U' F2) has RD corners.

- **(U) L2 D' F2 D'**
    - After B2, 1qt edges will be RD (good) and FH (good): +0+0+3(+0)
        - **B2 U' L2 F2 R2 B2 D' L2 // 13**
- **(U L2 U F2 U')**
    - After (R2 B2), 1qt edges will be RD (good) and FD (good): +0+1+1(+1)
        - **(R2 B2 U B2 L2 D' R2 B2) // 13**

Optimal is 13. Found none. Findable but hard 13.

### 2c3, scramble 10

`R' U' F U' L2 B2 L D R B' R2 D' L B' R2 U2 F' B R2 F' D2 L2 D2 R' U' F`

2c3 2e, goal 13.

Skeleton #1 R2 U R2 U' R2 U F2 U2 R2 has DD corners, L=9, 4 spare moves. On inverse, (R2 U2 F2 U B2 U L2 U' R2) has RD corners.

- R2 U
    - After B2 L2, 1qt edges will be FH (bad) and RV (good): +0+1+0(+3)
        - B2 L2 U L2 U' // no good
- (B2 U2 R2 U)
    - After (B2 R2 L2), 1qt edges will be RD (good) and FD (good): +0+2+1(+1)
        - (B2 R2 L2 U' F2 L2 D') // no good

Skeleton #2 R2 U2 F2 U B2 U B2 U' R2 has RD corners, L=9, 4 spare moves. On inverse, (R2 U B2 U' R2 U F2 U2 R2) has DD corners.

- F2 U2 F2 L2 U'
    - After B2 R2, 1qt edges will be RD (good) and FH (good): +1+1+1(+0)
        - B2 R2 U' F2 R2 U // no good
- (F2 L2 D')
    - After (B2 L2), 1qt edges will be FD (good) and RV (good): +1+1+0(+0)
        - (B2 L2 U' F2 U) // no good

Skeleton #3 U2 R2 U' R2 U R2 U' F2 U2 has RV corners, L=9, 4 spare moves. On inverse, (U2 R2 D' R2 D B2 U' F2 U2) has RV corners.

- U2 B2 R2 U
    - After B2, 1qt edges will be RH (bad) and FV (good), fr=1: +1+0+1(+2)
        - B2 U' R2 B2 U' // no good
- (U2 B2 L2 U')
    - After (B2 U2 B2), 1qt edges will be RV (good) and FV (good): +1+2+0(+1)
        - (B2 U2 B2 U B2 U) // no good

Skeleton #4 R2 U R2 U' R2 U' F2 U D B2 has RD corners, L=10, 3 spare moves.

- All variants have lower bound > spare moves.

Skeleton #5 R2 U R2 U' R2 U B2 U D B2 has FD corners, L=10, 3 spare moves.

- L2 U F2 U' R2 D
    - After F2, 1qt edges will be FD (good) and RH (good): +0+0+3(+0)
        - F2 U' F2 L2 F2 U' // no good

Skeleton #6 (R2 U B2 U' R2 U' F2 U D B2) on inverse has RD corners, L=10, 3 spare moves.

- All variants have lower bound > spare moves.

Skeleton #7 (R2 U B2 U' R2 U F2 U D B2) on inverse has FD corners, L=10, 3 spare moves.

- (L2 D F2 D' R2 D)
    - After (B2), 1qt edges will be FD (good) and RH (good): +0+0+3(+0)
        - (B2 U B2 R2 B2 U) // no good

Skeleton #8 U' R2 U R2 U R2 U' R2 U F2 U2 has RV corners, L=11, 2 spare moves. On inverse, (U2 R2 U B2 U' B2 U B2 U F2 U) has HH corners.

- U' R2 U F2 L2 D'
    - After R2 B2, 1qt edges will be RV (good) and FH (good): +1+1+0(+0)
        - R2 B2 U' B2 U // no good
- U' (U2 F2 R2 U' R2 U)
    - After (F2), 1qt edges will be RD (good) and FH (good): +1+0+1(+0)
        - (F2 U' R2 F2 U) // no good
- On inverse, linearly: all variants have lower bound > spare moves.

Optimal is 14. Found none.

## 0c0

### 0c0, scramble 1

`R' U' F R2 B' D' R U2 D2 L2 F2 R' B U B2 U B2 D' F2 R2 U' F2 D R' U' F`

0c0 2e, goal 12.

Skeleton #1 U D B2 U2 R2 has DD corners, L=5, 7 spare moves. On inverse, (F2 U2 R2 U D) has HH corners.

- With no setup, 1qt edges will be FH (bad) and RD (good): +0+3(+3)
    - **U F2 R2 F2 U R2 U2 B2 L2 B2 L2 D2 // 12**
    - U F2 L2 B2 D // no good
    - **U B2 R2 B2 U R2 U2 B2 R2 B2 R2 D2 // 12**
- After (R2 F2 U2 F2), 1qt edges will be RH (good) and FD (bad): +1+3(+3)
    - (R2 F2 U2 F2 U R2 F2 R2 U') // no good

Skeleton #2 B2 U2 R2 U D has HH corners, L=5, 7 spare moves. On inverse, (U D B2 U2 R2) has DD corners.

- After B2 U2 R2, 1qt edges will be RH (good) and FV (bad): +0+3(+3)
    - **B2 U2 R2 U' R2 B2 R2 U' R2 B2 R2 D2 // 12**
    - **B2 U2 R2 U' L2 B2 L2 U' L2 B2 L2 D2 // 12**
- After B2 U2 F2 R2, 1qt edges will be RH (good) and FD (bad): +1+3(+3)
    - B2 U2 F2 R2 U' L2 B2 L2 U // no good
- On inverse: all variants have lower bound > spare moves.

Skeleton #3 B2 D U B2 U2 has RV corners, L=5, 7 spare moves. On inverse, (U2 R2 U D R2) has FD corners.

- After F2, 1qt edges will be RD (bad) and FV (good): +0+3(+3)
    - **F2 U B2 R2 B2 U' F2 D2 F2 L2 F2 // 11**
    - **F2 U B2 L2 F2 D R2 U2 R2 F2 U2 B2 // 12**
- After R2 B2, 1qt edges will be RV (good) and FV (good): +1+3(+1)
    - R2 B2 U' L2 F2 R2 D // no good
- After (U2 F2 L2), 1qt edges will be FD (good) and RD (good): +1+3(+1)
    - (U2 F2 L2 U L2 F2 L2 U') // no good

Skeleton #4 U2 R2 U D R2 has FD corners, L=5, 7 spare moves. On inverse, (F2 U D B2 U2) has RV corners.

- After U2 L2, 1qt edges will be FH (bad) and RH (good): +0+3(+3)
    - **U2 L2 U' F2 R2 F2 U R2 B2 L2 B2 // 11**
    - U2 L2 U' F2 L2 B2 D' // no good
    - **U2 L2 U' B2 R2 B2 U L2 B2 R2 B2 // 11**
- After U2 B2 L2, 1qt edges will be FD (good) and RH (good): +1+3(+0)
    - **U2 B2 L2 U' B2 R2 B2 U L2 R2 B2 // 11**
- After (B2), 1qt edges will be RV (good) and FV (good): +0+3(+1)
    - **(B2 U R2 B2 R2 U' F2 B2 L2 F2 D2) // 11**
- After (R2 B2), 1qt edges will be RH (bad) and FV (good): +1+3(+3)
    - (R2 B2 U R2 B2 R2 U') // no good
- After (F2 R2 L2), 1qt edges will be RV (good) and FV (good): +2+3(+1)
    - **(F2 R2 L2 U' F2 L2 F2 U R2 F2 D2) // 11**

Skeleton #5 L2 U D R2 has RD corners, L=4, 8 spare moves. On inverse, (L2 U D R2) has RD corners.

- After L2, 1qt edges will be RV (bad) and FH (good), fr=1: +0+3(+5)
    - L2 U F2 L2 B2 D // no good
- After (L2), 1qt edges will be RH (bad) and FH (good), fr=1: +0+3(+5)
    - (L2 U' F2 R2 B2 D') // no good

Skeleton #6 U2 F2 D U B2 U2 has FV corners, L=6, 6 spare moves. On inverse, (U2 F2 U D B2 U2) has FV corners.

- After U2 R2 F2, 1qt edges will be FD (bad) and RH (good), fr=1: +1+3(+2)
    - U2 R2 F2 U R2 F2 R2 U // no good
- After (U2 F2), 1qt edges will be FD (bad) and RV (good), fr=1: +0+3(+2)
    - (U2 F2 U L2 F2 L2 U) // no good

Skeleton #7 B2 U D B2 D U has HH corners, L=6, 6 spare moves.

- (U') B2 U
    - After R2 B2 R2, 1qt edges will be RD (bad) and FH (good): +0+3+0(+3)
        - R2 B2 R2 U' B2 U // no good

Skeleton #8 (F2 U D F2 D U) on inverse has HH corners, L=6, 6 spare moves.

- U' (B2 U)
    - After (R2 B2 R2), 1qt edges will be RH (good) and FH (good): +0+3+1(+0)
        - (R2 B2 R2 U' R2 F2 D') // no good

Optimal is 11. Found 11 on skeleton #3.

### 0c0, scramble 2

`R' U' F U L2 U B2 L U B2 L F L' B2 U2 F2 L' B2 R2 U2 L2 D2 R' U' F`

0c0 2e, goal 12.

Skeleton #1 D U' B2 has FD corners, L=3, 9 spare moves. On inverse, (B2 U D') has HH corners.

- After F2 R2 F2, 1qt edges will be FV (bad) and RD (good): +3+3(+3)
    - F2 R2 F2 U' R2 B2 R2 U' // no good
- After (B2), 1qt edges will be RV (bad) and FV (bad): +0+3(+6)
    - (B2 U F2 R2 F2 U') // no good

Skeleton #2 L2 D U' has HH corners, L=3, 9 spare moves. On inverse, (D U' R2) has RD corners.

- After F2 R2, 1qt edges will be RD (bad) and FH (good): +1+3(+3)
    - F2 R2 U' R2 F2 L2 D // no good
- After (F2 R2 F2), 1qt edges will be RD (good) and FD (good): +3+3(+1)
    - (F2 R2 F2 U' L2 B2 L2 U) // no good

Skeleton #3 F2 D U' B2 has RD corners, L=4, 8 spare moves. On inverse, (R2 U D' L2) has FD corners.

- After L2 B2, 1qt edges will be RD (good) and FH (good): +1+3(+0)
    - L2 B2 U B2 R2 B2 U' // no good
- After R2 F2, 1qt edges will be RD (good) and FH (good): +1+3(+0)
    - **R2 F2 U' R2 B2 R2 U R2 L2 U2 L2 // 11**
- After L2 B2, 1qt edges will be RD (good) and FH (good): +1+6(+0)
    - **L2 B2 U F2 L2 F2 U2 F2 B2 D' L2 // 11**
    - **L2 B2 U' F2 B2 U2 B2 L2 B2 D R2 // 11**
- After (R2), 1qt edges will be FD (good) and RD (good): +0+3(+1)
    - **(R2 U' L2 B2 L2 U F2 B2 D2 B2 R2) // 11**
- After (R2), 1qt edges will be FD (good) and RD (good): +0+6(+1)
    - **(R2 U R2 L2 U2 R2 F2 R2 D' B2 L2) // 11**
    - **(R2 U' L2 F2 L2 U2 R2 L2 D F2 R2) // 11**
- After (R2), 1qt edges will be FD (good) and RD (good): +0+7(+1)
    - (R2 U R2 F2 R2 U2 R2 B2 R2 U) // no good
    - **(R2 U' L2 U2 R2 L2 U2 F2 R2 D' B2 L2) // 12**
    - **(R2 U' L2 F2 U2 R2 L2 U2 R2 D' B2 L2) // 12**

Skeleton #4 U2 R2 U D B2 U2 has FV corners, L=6, 6 spare moves. On inverse, (U2 B2 U D R2 U2) has RV corners.

- After U2 R2, 1qt edges will be FV (good) and RH (good), fr=1: +0+3(+1)
    - **U2 R2 U' L2 F2 R2 D' B2 U2 F2 // 10**
- After L2 U2 R2, 1qt edges will be FV (good) and RH (good): +1+3(+0)
    - L2 U2 R2 U' R2 B2 R2 U' // no good
- After R2 U2 R2, 1qt edges will be FV (good) and RH (good): +1+3(+0)
    - **R2 U2 R2 U R2 B2 R2 U F2 R2 L2 U2 // 12**
- After U2 R2, 1qt edges will be FV (good) and RH (good): +0+6(+0)
    - **U2 R2 U' L2 U2 L2 U2 F2 R2 D' B2 U2 // 12**
    - **U2 R2 U' L2 F2 U2 L2 U2 R2 D' B2 U2 // 12**
- After (U2 B2), 1qt edges will be RV (good) and FH (good), fr=1: +0+3(+1)
    - **(U2 B2 U F2 R2 F2 U R2 F2 B2 D2 R2) // 12**
- After (F2 U2 B2), 1qt edges will be RV (good) and FH (good): +1+3(+0)
    - **(F2 U2 B2 U F2 L2 B2 D R2 U2) // 10**
- After (B2 U2 B2), 1qt edges will be RV (good) and FH (good): +1+3(+0)
    - **(B2 U2 B2 U' B2 L2 F2 D' L2 D2 R2 L2) // 12**
- After (U2 B2), 1qt edges will be RV (good) and FH (good): +0+6(+0)
    - **(U2 B2 U F2 U2 B2 U2 L2 B2 D R2 U2) // 12**
    - **(U2 B2 U F2 L2 U2 B2 U2 B2 D R2 U2) // 12**
    - (U2 B2 U B2 U2 B2 U2 R2 B2 U) // no good

Skeleton #5 F2 U2 R2 U D B2 U2 has RV corners, L=7, 5 spare moves. On inverse, (U2 R2 U D B2 U2 R2) has DD corners.

- After F2 U2 R2, 1qt edges will be RH (bad) and FH (good), fr=1: +0+3(+2)
    - F2 U2 R2 U' R2 F2 L2 D' // no good
- On inverse: all variants have lower bound > spare moves.

Skeleton #6 U2 B2 U D R2 U2 B2 has DD corners, L=7, 5 spare moves. On inverse, (R2 U2 B2 U D R2 U2) has FV corners.

- After U2 B2, 1qt edges will be FD (good) and RV (good): +0+3(+0)
    - **U2 B2 U F2 L2 B2 D R2 U2 F2 // 10**
- After F2 U2 B2, 1qt edges will be FD (good) and RV (good): +1+3(+0)
    - F2 U2 B2 U F2 L2 B2 D' // no good
- After (F2 U2 R2), 1qt edges will be FV (good) and RH (good): +0+3(+0)
    - **(F2 U2 R2 U' L2 F2 R2 D' B2 U2) // 10**
- After (B2 U2 L2), 1qt edges will be FV (good) and RH (good): +0+3(+0)
    - **(B2 U2 L2 U' F2 L2 B2 D' B2 D2 R2 L2) // 12**
- After (U2 R2 U2 F2), 1qt edges will be FV (good) and RH (good): +1+3(+0)
    - **(U2 R2 U2 F2 U L2 F2 R2 D' B2 U2) // 11**
- After (F2 R2 U2 R2), 1qt edges will be FV (good) and RH (good), fr=1: +1+3(+1)
    - (F2 R2 U2 R2 U L2 B2 L2 U) // no good

Skeleton #7 L2 U D U' D has HH corners, L=5, 7 spare moves.

- All variants have lower bound > spare moves, or reach HTR with no move left.

Skeleton #8 U D' B2 U' D' has HH corners, L=5, 7 spare moves. On inverse, (U D' R2 U' D') has HH corners.

- (D) U
    - After R2 F2 R2 B2 L2 F2, 1qt edges will be RH (good) and FH (good): +0+6+0(+0)
        - R2 F2 R2 B2 L2 F2 U' B2 U' // no good
- D (U')
    - After (B2 R2 B2), 1qt edges will be RH (good) and FD (bad): +0+3+0(+3)
        - (B2 R2 B2 U' R2 U) // no good

Hard to find solutions:

Skeleton (R2 U D' R2 U D') on inverse has HH corners, L=6, 6 spare moves.

- **D (L2 U')**
    - After (B2 R2 B2), 1qt edges will be RH (good) and FD (bad): +0+3+0(+3)
        - **(B2 R2 B2 U' R2 U' L2 F2 R2) // 12**

Optimal is 10. Found 10 on skeleton #4.

### 0c0, scramble 3

`R' U' F D2 F D' F D' R' U F2 R2 U2 F2 R2 B' L2 D2 R2 D2 B D2 R' U' F`

0c0 2e, goal 12.

Skeleton #1 U D R2 U2 B2 has DD corners, L=5, 7 spare moves. On inverse, (B2 U2 L2 U D) has HH corners.

- With no setup, 1qt edges will be FD (good) and RH (bad): +0+3(+3)
    - U F2 L2 F2 U' // no good
- After (F2 U2 L2), 1qt edges will be RV (bad) and FH (good): +0+3(+3)
    - (F2 U2 L2 U' R2 B2 R2 U') // no good

Skeleton #2 L2 U2 F2 U D has HH corners, L=5, 7 spare moves. On inverse, (U D B2 U2 R2) has DD corners.

- After L2 U2 B2, 1qt edges will be RD (bad) and FH (good): +0+3(+3)
    - L2 U2 B2 U' R2 B2 R2 U // no good
- With no setup on inverse, 1qt edges will be FV (good) and RH (bad): +0+3(+3)
    - (U R2 B2 R2 U) // no good
    - **(U L2 F2 R2 D' B2 D2 F2 L2 F2 L2 F2) // 12**
    - **(U R2 F2 L2 D' B2 D2 F2 L2 B2 L2 B2) // 12**

Skeleton #3 L2 U D R2 U2 has RV corners, L=5, 7 spare moves. On inverse, (U2 L2 U D R2) has RD corners.

- After F2 L2, 1qt edges will be RD (bad) and FV (good): +1+3(+3)
    - **F2 L2 U' L2 B2 R2 D F2 D2 B2 L2 B2 // 12**
- After B2 R2, 1qt edges will be RD (bad) and FV (good): +1+3(+3)
    - **B2 R2 U F2 R2 B2 D' B2 D2 B2 R2 F2 // 12**
- After F2 L2, 1qt edges will be RD (bad) and FV (good): +1+3(+3)
    - F2 L2 U' R2 F2 R2 U' // no good
- After (U2 F2 L2), 1qt edges will be RV (bad) and FD (good): +1+3(+3)
    - (U2 F2 L2 U' R2 F2 L2 D) // no good

Skeleton #4 F2 D U B2 has RD corners, L=4, 8 spare moves. On inverse, (R2 U D R2) has FD corners.

- After B2, 1qt edges will be RH (bad) and FV (bad), fr=1: +0+3(+5)
    - B2 U F2 R2 B2 D' // no good
- After (R2), 1qt edges will be FV (bad) and RD (good), fr=1: +0+3(+5)
    - **(R2 U R2 B2 R2 U L2 U2 B2 L2 U2) // 11**
    - (R2 U R2 F2 L2 D') // no good

Skeleton #5 U2 F2 U D B2 has FD corners, L=5, 7 spare moves. On inverse, (B2 U D B2 U2) has FV corners.

- After U2 F2, 1qt edges will be FH (bad) and RH (good): +0+3(+3)
    - U2 F2 U' F2 L2 F2 U // no good
- After (F2), 1qt edges will be FH (bad) and RH (good): +0+3(+3)
    - (F2 U R2 B2 R2 U) // no good

Skeleton #6 U2 L2 U D R2 U2 has FV corners, L=6, 6 spare moves. On inverse, (U2 F2 U D B2 U2) has RV corners.

- After U2 R2, 1qt edges will be FD (bad) and RV (good), fr=1: +0+3(+2)
    - U2 R2 U' F2 L2 F2 U' // no good
- After (U2 L2 F2), 1qt edges will be RV (good) and FD (bad), fr=1: +1+3(+2)
    - (U2 L2 F2 U' R2 B2 R2 U) // no good

Skeleton #7 L2 U D L2 D' U has HH corners, L=6, 6 spare moves.

- All variants have lower bound > spare moves.

Skeleton #8 (R2 U D R2 D U') on inverse has HH corners, L=6, 6 spare moves.

- All variants have lower bound > spare moves, or reach HTR with no move left.

Optimal is 11. Found 11 on skeleton #4.

### 0c0, scramble 4

`R' U' F D2 F2 U F2 D F' R' D2 L2 F2 B2 U F2 D' F2 D' L2 F R U' R' U' F`

0c0 2e, goal 12.

Skeleton #1 D U' has HH corners, L=2, 10 spare moves. On inverse, (D U') has HH corners.

- After F2 B2, 1qt edges will be RH (good) and FD (bad), fr=1: +2+3(+5)
    - F2 B2 U F2 R2 F2 U' // no good
- After (F2 B2), 1qt edges will be RH (good) and FV (bad), fr=1: +2+3(+5)
    - (F2 B2 U B2 R2 B2 U') // no good

Skeleton #2 B2 U D' L2 has RD corners, L=4, 8 spare moves. On inverse, (R2 U D' F2) has FD corners.

- After B2, 1qt edges will be RH (bad) and FV (bad), fr=1: +0+3(+5)
    - B2 U F2 R2 F2 U' // no good
- After (R2), 1qt edges will be FV (bad) and RV (bad), fr=1: +0+3(+5)
    - (R2 U' R2 F2 L2 D) // no good

Skeleton #3 R2 U D' F2 has FD corners, L=4, 8 spare moves. On inverse, (F2 D U' R2) has RD corners.

- After R2, 1qt edges will be FD (good) and RV (bad), fr=1: +0+3(+5)
    - R2 U' R2 B2 R2 U // no good
- After (B2), 1qt edges will be RH (bad) and FH (good), fr=1: +0+3(+5)
    - (B2 U B2 R2 B2 U') // no good

Skeleton #4 U2 F2 D U' R2 U2 has RV corners, L=6, 6 spare moves. On inverse, (U2 R2 U D' F2 U2) has FV corners.

- After U2 B2, 1qt edges will be RH (bad) and FH (good), fr=1: +0+3(+2)
    - U2 B2 U B2 R2 B2 U // no good
- After (U2 R2), 1qt edges will be FV (good) and RD (bad), fr=1: +0+3(+2)
    - (U2 R2 U' R2 B2 R2 U') // no good

Skeleton #5 U2 R2 U D' F2 U2 has FV corners, L=6, 6 spare moves. On inverse, (U2 B2 U D' L2 U2) has RV corners.

- All variants have lower bound > spare moves.

Skeleton #6 U D U' D has HH corners, L=4, 8 spare moves. On inverse, (U D U' D) has HH corners.

- All variants have lower bound > spare moves.

Skeleton #7 R2 U2 F2 U D R2 U2 B2 has DD corners, L=8, 4 spare moves. On inverse, (F2 U2 R2 U D B2 U2 R2) has DD corners.

- After F2 U2 R2, 1qt edges will be FV (good) and RD (good): +0+3(+0)
    - **F2 U2 R2 U' L2 F2 R2 D F2 D2 B2 L2 // 12**
    - F2 U2 R2 U' L2 B2 L2 U' // no good
- After B2 U2 L2, 1qt edges will be FV (good) and RD (good): +0+3(+0)
    - **B2 U2 L2 U' F2 L2 B2 D B2 D2 B2 R2 // 12**
- After (R2 U2 F2), 1qt edges will be FD (good) and RV (good): +0+3(+0)
    - (R2 U2 F2 U L2 F2 R2 D) // no good

Skeleton #8 B2 D U' L2 U' D' has HH corners, L=6, 6 spare moves.

- All variants have lower bound > spare moves.

Optimal is 12. Found 12 on skeleton #7.

### 0c0, scramble 5

`R' U' F U' L U' F' B D2 B R L F U' B2 R2 U F2 R2 D2 L2 F2 D' R' U' F`

0c0 6e, goal 12.

Skeleton #1 U D R2 has FD corners, L=3, 9 spare moves. On inverse, (F2 U D) has HH corners.

- All variants have lower bound > spare moves.

Skeleton #2 B2 U D R2 U2 has FV corners, L=5, 7 spare moves. On inverse, (U2 B2 U D R2) has FD corners.

- All variants have lower bound > spare moves.

Skeleton #3 R2 U D B2 U2 R2 has DD corners, L=6, 6 spare moves. On inverse, (R2 U2 B2 U D R2) has RD corners.

- After L2, 1qt edges will be FV (good) and RV (good): +0+5(+1)
    - L2 U R2 F2 L2 F2 B2 U' // no good
- After (L2 U2 B2), 1qt edges will be RD (good) and FD (good): +0+5(+1)
    - (L2 U2 B2 U L2 B2 R2 F2 B2 U') // no good

Skeleton #4 U2 R2 U D' L2 has RD corners, L=5, 7 spare moves. On inverse, (R2 U D' L2 U2) has RV corners.

- On normal: all variants have lower bound > spare moves.
- After (R2), 1qt edges will be RV (good) and FD (bad), fr=1: +0+5(+2)
    - (R2 U' R2 L2 B2 R2 F2 U) // no good

Skeleton #5 R2 U2 F2 U D B2 U2 has RV corners, L=7, 5 spare moves. On inverse, (U2 R2 D U R2 U2 B2) has DD corners.

- All variants have lower bound > spare moves.

Skeleton #6 U2 F2 D U' has HH corners, L=4, 8 spare moves.

- All variants have lower bound > spare moves.

Skeleton #7 U D R2 U D' has HH corners, L=5, 7 spare moves. On inverse, (U D' R2 D U) has HH corners.

- (D) U
    - After L2 B2 R2, 1qt edges will be RH (good) and FH (good): +0+3+3(+0)
        - L2 B2 R2 U F2 U2 R2 B2 U // no good
- On inverse, with the premove U': all variants have lower bound > spare moves.

Skeleton #8 B2 U D R2 U D has HH corners, L=6, 6 spare moves.

- (D') F2 D'
    - After F2 L2 B2, 1qt edges will be RH (good) and FD (bad): +0+3+0(+3)
        - F2 L2 B2 U R2 U // no good

Optimal is 13. Found none.

## 4c3

### 4c3, scramble 1

`R' U' F D R B2 R B2 R' B2 R' U2 B2 R B2 F L' R B U R' U F2 R' U' F`

4c3 6e, goal 13.

Skeleton #1 F2 U2 R2 D L2 D B2 U2 L2 D' has HH corners, L=10, 3 spare moves. On inverse, (D L2 U2 F2 D' F2 U R2 U2 F2) has DD corners.

- (D)
    - After R2 U2 R2 B2, 1qt edges will be FV (good) and RD (good): +1+2(+0)
        - R2 U2 R2 B2 U L2 U2 L2 U' // no good
- **(D')**
    - After B2 U2 R2, 1qt edges will be FH (bad) and RV (good): +0+0(+3)
        - **B2 U2 R2 U L2 U L2 D2 B2 R2 B2 R2 // 13**
- R2 U2 R2 B2 U'
    - After L2, 1qt edges will be RH (good) and FH (good): +1+0+1(+0)
        - L2 U R2 F2 U2 F2 U // no good
- **(D')**
    - After (L2 F2 L2 B2 U2 L2), 1qt edges will be FD (good) and RV (good): +0+3+0(+0)
        - (L2 F2 L2 B2 U2 L2 U' B2 U') // no good
    - After (R2 B2 R2 B2 U2 R2), 1qt edges will be FD (good) and RV (good): +0+3+0(+0)
        - **(R2 B2 R2 B2 U2 R2 U' R2 U' L2 D2 B2) // 13**

Skeleton #2 D' L2 U B2 U2 R2 D R2 U2 has RV corners, L=9, 4 spare moves. On inverse, (U2 R2 U R2 U2 B2 U R2 D) has HH corners.

- On normal: all variants have lower bound > spare moves.
- On inverse, with the premove D': all variants have lower bound > spare moves.
- (U2 R2 D')
    - After (L2 F2 R2 F2 U2 L2), 1qt edges will be RH (good) and FH (good): +0+3+0(+0)
        - (L2 F2 R2 F2 U2 L2 U R2 U') // no good

Skeleton #3 D' L2 U' F2 U D F2 U' F2 U2 has RV corners, L=10, 3 spare moves. On inverse, (U2 R2 U' L2 U D R2 D' F2 D) has HH corners.

- All variants have lower bound > spare moves.

Skeleton #4 D' L2 U B2 U D B2 U R2 U2 has RV corners, L=10, 3 spare moves. On inverse, (U2 R2 U' B2 U D B2 D' R2 D) has HH corners.

- On normal: all variants have lower bound > spare moves.
- D' (U2 L2 D' L2 F2 D)
    - After (R2 L2), 1qt edges will be RD (good) and FH (good): +1+2+0(+0)
        - (R2 L2 U F2 U) // no good

Skeleton #5 D' L2 U' R2 U D L2 U' R2 U2 has RV corners, L=10, 3 spare moves. On inverse, (U2 R2 U L2 U D R2 D L2 D) has HH corners.

- D' B2 L2 D L2 D
    - After R2 L2, 1qt edges will be RV (good) and FH (good): +1+2+0(+0)
        - R2 L2 U F2 U // no good
- D' (U2 R2 U L2 U)
    - After (F2 B2), 1qt edges will be RD (good) and FH (good): +0+2+1(+0)
        - (F2 B2 U F2 R2 D') // no good

Skeleton #6 D' L2 U L2 U D R2 U F2 U2 has RV corners, L=10, 3 spare moves. On inverse, (U2 R2 U B2 U D B2 D B2 D) has HH corners.

- All variants have lower bound > spare moves.

Skeleton #7 L2 U B2 U' R2 U' F2 U R2 D has HH corners, L=10, 3 spare moves. On inverse, (D' B2 U L2 U' F2 D' R2 U B2) has RD corners.

- (D') R2 D F2 D'
    - After R2 B2 L2 B2, 1qt edges will be FD (good) and RH (good): +0+3+0(+0)
        - R2 B2 L2 B2 U B2 U // no good
- B2 L2 D' B2 U R2 U
    - After R2, 1qt edges will be RH (good) and FH (good): +1+0+1(+0)
        - R2 U' F2 L2 D' // no good
- (D' B2 U B2 R2 U)
    - After (F2 R2 L2), 1qt edges will be RD (good) and FH (good): +1+2+0(+0)
        - (F2 R2 L2 U F2 U) // no good

Skeleton #8 U2 R2 D' L2 U L2 U R2 D' B2 D has HH corners, L=11, 2 spare moves. On inverse, (D' B2 U F2 U' L2 D' F2 U L2 U2) has RV corners.

- All variants have lower bound > spare moves.

Optimal is 13. Found 13 on skeleton #1.

### 4c3, scramble 2

`R' U' F R' U2 L2 U' F D' L D2 L U' F R2 L2 U2 R2 B2 U' R2 U2 F2 R' U' F`

4c3 4e, goal 13.

Skeleton #1 U2 B2 U R2 U2 B2 U' F2 U has HH corners, L=9, 4 spare moves. On inverse, (U' R2 U B2 U2 L2 U' F2 U2) has FV corners.

- **(U')**
    - After U2 B2, 1qt edges will be RH (bad) and FH (good): +0+1(+3)
        - **U2 B2 U B2 U2 F2 L2 D F2 R2 F2 R2 // 13**
    - After F2 U2 B2, 1qt edges will be RH (bad) and FH (good): +1+0(+3)
        - **F2 U2 B2 U B2 U2 L2 D F2 R2 F2 R2 // 13**
        - **F2 U2 B2 U' L2 U2 B2 D' B2 L2 B2 L2 // 13**
    - After R2 B2 U2 F2 R2, 1qt edges will be RD (good) and FH (good): +3+1(+0)
        - **R2 B2 U2 F2 R2 U' R2 U2 R2 B2 U L2 // 13**
    - After R2 B2 U2 B2 L2, 1qt edges will be RD (good) and FH (good): +3+1(+0)
        - R2 B2 U2 B2 L2 U L2 U2 L2 B2 U // no good
    - After L2 F2 U2 F2 R2, 1qt edges will be RD (good) and FH (good): +3+1(+0)
        - **L2 F2 U2 F2 R2 U' L2 U2 L2 F2 U R2 // 13**
    - After F2 U2 B2 L2 F2 L2, 1qt edges will be RD (good) and FH (good): +4+0(+0)
        - **F2 U2 B2 L2 F2 L2 U B2 U2 L2 D R2 // 13**
        - **F2 U2 B2 L2 F2 L2 U' L2 U2 B2 D' L2 // 13**
- U2 F2 U
    - After R2 U2 F2, 1qt edges will be RV (bad) and FH (good): +0+0+1(+3)
        - R2 U2 F2 U' F2 L2 U // no good
- **(U')**
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
        - (R2 F2 R2 F2 U L2 F2 U2 F2 D) // no good

Skeleton #2 (D' F2 D B2 U2 L2 D' L2 U D) on inverse has HH corners, L=10, 3 spare moves.

- D' (D' L2 F2 D')
    - After (B2 L2 U2 R2), 1qt edges will be RH (good) and FH (good): +1+1+0(+0)
        - (B2 L2 U2 R2 U' R2 U') // no good
- On inverse, linearly: all variants have lower bound > spare moves.

Skeleton #3 U2 B2 U B2 U D B2 D' R2 U has HH corners, L=10, 3 spare moves.

- All variants have lower bound > spare moves.

Skeleton #4 U2 B2 U' L2 D U R2 D L2 U has HH corners, L=10, 3 spare moves.

- All variants have lower bound > spare moves.

Skeleton #5 U2 B2 U' B2 U D B2 D B2 U has HH corners, L=10, 3 spare moves.

- All variants have lower bound > spare moves.

Skeleton #6 U2 B2 U R2 U D L2 D' F2 U has HH corners, L=10, 3 spare moves.

- All variants have lower bound > spare moves.

Optimal is 13. Found 13 on skeleton #1.

### 4c3, scramble 3

`R' U' F U F' R D F L F' R' U2 L2 D2 B2 U R2 U L2 D2 F' L' F' R' U' F`

4c3 6e, goal 13.

Skeleton #1 R2 U F2 U2 L2 U' F2 D' has HH corners, L=8, 5 spare moves. On inverse, (D B2 U B2 U2 R2 D' R2) has RD corners.

- With the premove (D): all variants have lower bound > spare moves.
- **L2 D**
    - After F2 U2 F2 L2, 1qt edges will be RV (bad) and FH (good): +0+1+0(+3)
        - **F2 U2 F2 L2 U F2 U' F2 L2 F2 D2 // 13**
- R2 U
    - After L2 B2 U2 B2, 1qt edges will be RD (bad) and FH (good): +0+1+1(+3)
        - L2 B2 U2 B2 U L2 F2 U' // no good
- **B2 L2 D'**
    - After B2 R2 U2 L2, 1qt edges will be RH (good) and FH (good): +1+1+0(+0)
        - **B2 R2 U2 L2 U' B2 U R2 L2 U2 // 13**
- On inverse: all variants have lower bound > spare moves.

Skeleton #2 R2 U F2 U D F2 D' F2 D' has HH corners, L=9, 4 spare moves. On inverse, (D B2 U B2 U D B2 U' L2) has RD corners.

- (D) B2 L2 D' R2 D
    - After F2 R2 B2, 1qt edges will be FD (good) and RH (good): +1+3+0(+0)
        - F2 R2 B2 U' L2 U // no good
- (D B2 U B2 U')
    - After (F2 R2 B2), 1qt edges will be RD (good) and FD (good): +0+3+0(+1)
        - (F2 R2 B2 U R2 U') // no good

Skeleton #3 R2 U' L2 U D R2 D B2 D' has HH corners, L=9, 4 spare moves. On inverse, (D B2 U' R2 U D L2 U L2) has RD corners.

- (D) L2 U' B2 U
    - After R2 L2, 1qt edges will be FD (good) and RD (good): +0+2+1(+1)
        - R2 L2 U L2 F2 D // no good
- (D B2 U' L2 U')
    - After (F2 B2), 1qt edges will be RD (good) and FH (good): +0+2+1(+0)
        - (F2 B2 U' B2 R2 D') // no good

Skeleton #4 L2 U' L2 U D L2 D L2 D' has HH corners, L=9, 4 spare moves. On inverse, (D B2 U L2 U D R2 U' B2) has RD corners.

- All variants have lower bound > spare moves.

Skeleton #5 L2 U B2 U D F2 D' R2 D' has HH corners, L=9, 4 spare moves. On inverse, (D B2 U' B2 U D B2 U B2) has RD corners.

- All variants have lower bound > spare moves.

Skeleton #6 R2 U F2 U' B2 U R2 U B2 U F2 has FD corners, L=11, 2 spare moves. On inverse, (B2 D' R2 U' F2 U' L2 U B2 D' L2) has RD corners.

- L2 D F2 U' F2 U
    - After F2 L2, 1qt edges will be FD (good) and RD (good): +0+1+0(+1)
        - F2 L2 U' L2 U // no good
- (R2 F2 U B2 D R2 U)
    - After (L2), 1qt edges will be RD (good) and FD (good): +1+0+0(+1)
        - (L2 U' L2 U') // no good

Skeleton #7 R2 U F2 U2 L2 U' B2 D U D has HH corners, L=10, 3 spare moves.

- All variants have lower bound > spare moves.

Skeleton #8 (U R2 U R2 U2 F2 U' L2 U D') on inverse has HH corners, L=10, 3 spare moves.

- D (U F2 R2 U')
    - After (L2 F2 U2 F2), 1qt edges will be RH (good) and FH (good): +1+1+0(+0)
        - (L2 F2 U2 F2 U' F2 U') // no good
- On inverse, linearly: all variants have lower bound > spare moves.

Optimal is 13. Found 13 on skeleton #1.

### 4c3, scramble 4

`R' U' F U R F R' B2 U2 D' F' U R2 U L2 D' L2 D2 B2 R2 U2 B2 R' U' F`

4c3 2e, goal 13.

Skeleton #1 L2 U B2 U2 R2 D' L2 D R2 has FD corners, L=9, 4 spare moves. On inverse, (B2 U F2 U R2 U2 B2 U' R2) has RD corners.

- B2 L2 U'
    - After B2 L2 U2 L2, 1qt edges will be FD (good) and RH (good): +1+1+1(+0)
        - B2 L2 U2 L2 U' F2 L2 U // no good
- (R2 F2 U')
    - After (F2), 1qt edges will be RH (bad) and FD (good): +1+0+0(+3)
        - (F2 U L2 U2 B2 D) // no good

Skeleton #2 (B2 U F2 U B2 U D B2 D' F2) on inverse has RD corners, L=10, 3 spare moves.

- **(B2 U B2 U L2 D)**
    - After (F2 L2 F2), 1qt edges will be RD (good) and FH (good): +0+3+0(+0)
        - **(F2 L2 F2 U' B2 U R2) // 13**
- (B2 U R2 F2 U' R2 U')
    - After (R2 L2), 1qt edges will be RD (good) and FH (good): +1+2+0(+0)
        - (R2 L2 U' R2 U') // no good

Skeleton #3 (B2 U F2 U' B2 U D B2 D L2) on inverse has RD corners, L=10, 3 spare moves.

- All variants have lower bound > spare moves.

Skeleton #4 (B2 U F2 U' R2 U D L2 D B2) on inverse has RD corners, L=10, 3 spare moves.

- (B2 U B2 U' F2 U')
    - After (B2 R2 B2), 1qt edges will be RD (good) and FH (good): +0+3+0(+0)
        - (B2 R2 B2 U B2 U) // no good

Skeleton #5 (B2 U F2 U R2 U D L2 D' R2) on inverse has RD corners, L=10, 3 spare moves.

- All variants have lower bound > spare moves.

Skeleton #6 L2 D' F2 D B2 U' F2 U' R2 D has HH corners, L=10, 3 spare moves. On inverse, (D' F2 U' L2 D' F2 D F2 D' B2) has RD corners.

- (D') L2 D' F2 D
    - After B2, 1qt edges will be FD (good) and RD (good): +0+0+0(+1)
        - B2 U' F2 U // no good
- L2 U' R2 D L2 U'
    - After R2, 1qt edges will be RH (good) and FH (good): +0+0+1(+0)
        - R2 U' R2 B2 D' // no good
- (D' R2 B2 D B2 D)
    - After (F2), 1qt edges will be RD (good) and FH (good): +1+0+2(+0)
        - (F2 U' R2 L2 F2 D') // no good

Skeleton #7 L2 D B2 U' B2 D B2 U L2 D has HH corners, L=10, 3 spare moves. On inverse, (D' R2 D' F2 U' F2 U R2 U' L2) has RD corners.

- With the premove (D'): all variants have lower bound > spare moves.
- Linearly: all variants have lower bound > spare moves, or reach HTR with no move left.
- (D' R2 D' B2 U)
    - After (R2 U2 R2), 1qt edges will be RD (good) and FH (good): +0+2+0(+0)
        - (R2 U2 R2 U' R2 U) // no good

Skeleton #8 L2 U' R2 D F2 U' F2 U' R2 D' R2 has RD corners, L=11, 2 spare moves. On inverse, (R2 D R2 D B2 U F2 U' F2 U L2) has RD corners.

- R2 D' B2 R2 U' R2 U
    - After F2, 1qt edges will be RD (good) and FH (good): +1+0+1(+0)
        - F2 U L2 B2 D' // no good
- (L2 U L2 D L2 F2 U')
    - After (L2 F2), 1qt edges will be RD (good) and FH (good): +1+1+0(+0)
        - (L2 F2 U' B2 U) // no good

Optimal is 13. Found 13 on skeleton #2.

### 4c3, scramble 5

`R' U' F R2 B2 R' U F2 U' F' U2 L' F2 R' U2 L' D2 F2 R F2 D' B2 D2 R' U' F`

4c3 6e, goal 13.

Skeleton #1 F2 D R2 U B2 U2 L2 D' R2 U2 has RV corners, L=10, 3 spare moves. On inverse, (U2 R2 U F2 U2 L2 D' R2 D' B2) has FD corners.

- B2 U
    - After R2, 1qt edges will be RH (bad) and FH (good), fr=1: +0+0+0(+2)
        - R2 U F2 U2 L2 U' // no good
- (U2 L2 D)
    - After (R2 U2 B2 L2 B2 L2), 1qt edges will be FD (good) and RH (good): +0+3+0(+0)
        - (R2 U2 B2 L2 B2 L2 U R2 U) // no good

Skeleton #2 F2 D R2 U B2 U D F2 U' L2 U2 has RV corners, L=11, 2 spare moves.

- All variants have lower bound > spare moves.

Skeleton #3 F2 D R2 U' L2 U D L2 U L2 U2 has RV corners, L=11, 2 spare moves.

- All variants have lower bound > spare moves.

Skeleton #4 F2 D R2 U R2 U D R2 U' B2 U2 has RV corners, L=11, 2 spare moves.

- All variants have lower bound > spare moves.

Skeleton #5 F2 D R2 U' F2 U D B2 U B2 U2 has RV corners, L=11, 2 spare moves.

- All variants have lower bound > spare moves.

Skeleton #6 U' F2 D' L2 U' L2 U B2 D' B2 U2 has RV corners, L=11, 2 spare moves. On inverse, (U2 R2 U' F2 D L2 U' B2 D' R2 U) has HH corners.

- U' R2 B2 U B2 D
    - After L2 F2, 1qt edges will be RV (good) and FH (good): +1+1+0(+0)
        - L2 F2 U B2 U' // no good
- On inverse, with the premove U': all variants have lower bound > spare moves.
- On inverse, linearly: all variants have lower bound > spare moves, or reach HTR with no move left.

Skeleton #7 U' R2 D' F2 U' L2 D B2 U' R2 U2 has RV corners, L=11, 2 spare moves. On inverse, (U2 R2 U F2 D' R2 U B2 D R2 U) has HH corners.

- On normal: all variants have lower bound > spare moves.
- On inverse, with the premove U': all variants have lower bound > spare moves.
- (R2 U2 L2 D' F2 U' F2 U)
    - After (L2), 1qt edges will be RH (good) and FH (good): +1+0+0(+0)
        - (L2 U F2 U') // no good

Skeleton #8 F2 U F2 U R2 U2 B2 U' L2 D U has HH corners, L=11, 2 spare moves.

- All variants have lower bound > spare moves.

Optimal is 14. Found none.

## 4b2

### 4b2, scramble 1

`R' U' F U F R2 F2 L' D2 L2 U2 B2 L' D2 U2 L F D L2 D2 F' L2 U2 R' U' F`

4b2 8e, goal 12.

Skeleton #1 U2 B2 U R2 U has HH corners, L=5, 7 spare moves. On inverse, (U R2 U R2 U2) has FV corners.

- After U2 F2, 1qt edges will be RH (good) and FD (bad): +0+3(+3)
    - U2 F2 U F2 R2 F2 R2 D' // no good
- With no setup on inverse, 1qt edges will be FV (good) and RV (good): +0+3(+1)
    - **(U L2 F2 R2 B2 U' R2 F2 D2 F2 L2 B2) // 12**
    - **(U L2 F2 L2 F2 D' R2 F2 U2 L2 B2 R2) // 12**
- After (F2 B2), 1qt edges will be FV (good) and RV (good): +2+3(+1)
    - (F2 B2 U F2 R2 B2 L2 U') // no good

Skeleton #2 U2 B2 U B2 D U' B2 D' has HH corners, L=8, 4 spare moves. On inverse, (U B2 D U' B2 D' F2 U2) has FV corners.

- U2 F2 U R2 D'
    - After R2 F2 L2, 1qt edges will be RH (good) and FH (good): +0+3+0(+0)
        - R2 F2 L2 U' R2 U // no good
- (U B2 D')
    - After (F2 R2 B2), 1qt edges will be FV (good) and RH (good): +0+3+0(+0)
        - (F2 R2 B2 U' B2 U) // no good

Skeleton #3 U D R2 D B2 U' has HH corners, L=6, 6 spare moves. On inverse, (U L2 U F2 U' D) has HH corners.

- (U) U
    - After B2 L2 F2, 1qt edges will be RD (good) and FH (good): +0+3+1(+0)
        - B2 L2 F2 U' R2 B2 D // no good
- D' (U)
    - After (F2 R2), 1qt edges will be RH (good) and FH (good): +0+1+4(+0)
        - (F2 R2 U' F2 U2 F2 R2 B2 D) // no good
- On inverse, linearly: all variants have lower bound > spare moves.

Skeleton #4 B2 U D R2 D' F2 U' has HH corners, L=7, 5 spare moves. On inverse, (U R2 U' R2 D U B2) has FD corners.

- All variants have lower bound > spare moves.

Skeleton #5 (U R2 U' B2 U D B2 U2 R2) on inverse has DD corners, L=9, 3 spare moves.

- (U L2 D')
    - After (F2), 1qt edges will be FD (good) and RV (good): +0+0+3(+0)
        - (F2 U L2 F2 R2 D) // no good

Skeleton #6 (U R2 U F2 U D' F2 U2) on inverse has RV corners, L=8, 4 spare moves.

- (U L2 D)
    - After (B2), 1qt edges will be RV (good) and FH (good): +0+0+3(+0)
        - (B2 U' R2 B2 L2 D') // no good

Skeleton #7 U2 B2 U' R2 D U B2 D' has HH corners, L=8, 4 spare moves. On inverse, (U' R2 D U B2 D' R2 U2) has FV corners.

- All variants have lower bound > spare moves.

Skeleton #8 U2 F2 U F2 U D' U' has HH corners, L=7, 5 spare moves.

- All variants have lower bound > spare moves.

Optimal is 12. Found 12 on skeleton #1.

### 4b2, scramble 2

`R' U' F L2 F U' B2 L' F2 R' U2 F2 R2 D2 B U2 F U2 D2 B' R' U2 R' U' F`

4b2 2e, goal 12.

Skeleton #1 F2 U' R2 U' F2 U2 has RV corners, L=6, 6 spare moves. On inverse, (U2 R2 U' R2 U' R2) has FD corners.

- After R2 L2 B2, 1qt edges will be RV (good) and FD (bad): +2+0(+3)
    - **R2 L2 B2 U' B2 U R2 B2 R2 U2 R2 U2 // 12**
- After R2 L2 B2, 1qt edges will be RV (good) and FD (bad), fr=1: +2+2(+2)
    - R2 L2 B2 U B2 U2 B2 U // no good
- After (U2 B2 L2), 1qt edges will be FV (bad) and RH (good): +1+2(+3)
    - (U2 B2 L2 U F2 B2 R2 D') // no good

Skeleton #2 F2 U' R2 U' R2 U D' L2 U2 has FV corners, L=9, 3 spare moves.

- All variants have lower bound > spare moves.

Skeleton #3 F2 U' R2 U' F2 D' U has HH corners, L=7, 5 spare moves.

- (U') F2 U'
    - After R2, 1qt edges will be RH (good) and FV (bad): +0+0+1(+3)
        - R2 U' R2 F2 U' // no good
- F2 U' R2 U'
    - After R2 F2, 1qt edges will be RH (good) and FH (good): +0+1+3(+0)
        - R2 F2 U R2 F2 R2 U' // no good

Skeleton #4 F2 U' R2 U F2 U D R2 has RD corners, L=8, 4 spare moves.

- All variants have lower bound > spare moves.

Skeleton #5 F2 U' R2 U L2 U D R2 U2 B2 has DD corners, L=10, 2 spare moves.

- All variants have lower bound > spare moves.

Skeleton #6 F2 U R2 U D B2 D B2 U2 has RV corners, L=9, 3 spare moves. On inverse, (U2 R2 U L2 U D B2 D L2) has FD corners.

- All variants have lower bound > spare moves.

Skeleton #7 F2 U' F2 U D' F2 D R2 U2 has RV corners, L=9, 3 spare moves. On inverse, (U2 R2 U' B2 U D' F2 D F2) has FD corners.

- B2 D' F2 D
    - After L2 B2 L2, 1qt edges will be RV (good) and FH (good): +0+3+0(+0)
        - L2 B2 L2 U R2 U' // no good
- (U2 R2 U' F2 U')
    - After (R2 B2 R2), 1qt edges will be FD (good) and RH (good): +0+3+0(+0)
        - (R2 B2 R2 U' B2 U') // no good

Skeleton #8 U R2 U R2 U F2 U has HH corners, L=7, 5 spare moves. On inverse, (D' B2 U L2 D R2 D') has HH corners.

- (U') U
    - After L2 B2 L2 F2, 1qt edges will be RD (good) and FH (good): +0+3+2(+0)
        - L2 B2 L2 F2 U' F2 R2 L2 D // no good
- **D B2 D**
    - After L2, 1qt edges will be RH (good) and FH (good): +0+0+3(+0)
        - L2 U B2 L2 B2 L2 U' // no good
    - After R2, 1qt edges will be RH (good) and FH (good): +0+0+3(+0)
        - **R2 U L2 B2 L2 B2 U L2 R2 // 12**
- D (D')
    - After (B2 L2 B2 L2), 1qt edges will be FD (good) and RH (good): +0+3+2(+0)
        - (B2 L2 B2 L2 U' F2 R2 L2 D) // no good
- (U' L2 U)
    - After (F2 R2 B2 R2), 1qt edges will be RH (good) and FH (good): +0+3+0(+0)
        - (F2 R2 B2 R2 U' B2 U) // no good

Hard to find solutions:

Skeleton (U2 R2 U' R2 U' B2 U D' F2) on inverse has RD corners, L=9, 3 spare moves.

- **(U2 R2 U' L2 D')**
    - After (F2), 1qt edges will be RD (good) and FH (good): +0+0+2(+0)
        - **(F2 U F2 B2 D' R2) // 11**

Optimal is 11. Found 12 on skeleton #1. Findable but hard 11.

### 4b2, scramble 3

`R' U' F D F2 D2 L2 R B2 U2 R D2 L' U2 R2 F2 D' U2 L' F U' L' F R' U' F`

4b2 6e, goal 12.

Skeleton #1 U2 F2 U' L2 U' F2 U2 has FV corners, L=7, 5 spare moves. On inverse, (U2 B2 U F2 U F2 U2) has FV corners.

- After U2 L2 B2, 1qt edges will be FV (good) and RV (good), fr=1: +1+0(+2)
    - U2 L2 B2 U R2 D' // no good
- After B2 U2 L2 B2, 1qt edges will be FV (good) and RV (good): +2+0(+1)
    - **B2 U2 L2 B2 U' R2 D B2 R2 U2 R2 L2 // 12**
- After (U2 B2), 1qt edges will be FD (bad) and RV (good), fr=1: +0+0(+2)
    - **(U2 B2 U B2 D' R2 B2 R2 F2 L2 U2 F2) // 12**
- After (U2 B2), 1qt edges will be FD (bad) and RV (good): +0+2(+3)
    - (U2 B2 U' B2 U2 B2 D) // no good

Skeleton #2 U' B2 U B2 U F2 D' has HH corners, L=7, 5 spare moves. On inverse, (U L2 U' L2 U' F2 U) has HH corners.

- (D) U'
    - After B2, 1qt edges will be FH (bad) and RD (good), fr=1: +0+0+1(+3)
        - B2 U R2 F2 D' // no good
- U' B2 D
    - After B2 R2, 1qt edges will be RH (good) and FH (good): +0+1+2(+0)
        - B2 R2 U R2 U2 L2 U' // no good
- U' (U)
    - After (B2 R2), 1qt edges will be FV (bad) and RH (good), fr=1: +0+1+1(+3)
        - (B2 R2 U B2 L2 U) // no good
- (D F2 U')
    - After (B2), 1qt edges will be RH (good) and FH (good): +0+0+4(+0)
        - (B2 U F2 U2 R2 L2 F2 D') // no good

Skeleton #3 U' R2 D B2 U L2 D B2 U2 has RV corners, L=9, 3 spare moves. On inverse, (U2 R2 U F2 U F2 U F2 U) has HH corners.

- On normal: all variants have lower bound > spare moves.
- U' (U2 B2 L2 U)
    - After (B2 U2 B2), 1qt edges will be RD (good) and FH (good): +1+2+0(+0)
        - (B2 U2 B2 U B2 U') // no good
- (U2 L2 U L2 D)
    - After (B2), 1qt edges will be RH (good) and FH (good): +0+0+2(+0)
        - (B2 U' B2 U2 F2 U) // no good

Skeleton #4 U2 L2 U' R2 U' R2 U' F2 D' has HH corners, L=9, 3 spare moves. On inverse, (D L2 U' L2 U' R2 D' F2 U2) has RV corners.

- (D) L2 U2 L2 U
    - After B2 R2, 1qt edges will be RD (good) and FH (good): +1+1+0(+0)
        - B2 R2 U B2 U' // no good
- Linearly: all variants have lower bound > spare moves.
- (D F2 L2 U)
    - After (B2), 1qt edges will be RV (good) and FH (good), fr=1: +1+0+1(+1)
        - (B2 U B2 L2 U) // no good

Skeleton #5 U2 F2 U R2 D U F2 D B2 U2 has FV corners, L=10, 2 spare moves. On inverse, (U2 B2 U' B2 D U R2 D' F2 U2) has FV corners.

- All variants have lower bound > spare moves.

Skeleton #6 U2 B2 U' R2 D U' L2 D L2 U2 has FV corners, L=10, 2 spare moves. On inverse, (U2 B2 U L2 U D' L2 D' L2 U2) has FV corners.

- All variants have lower bound > spare moves.

Skeleton #7 (U2 B2 U B2 U L2 D U) on inverse has HH corners, L=8, 4 spare moves.

- U' (U2 B2 U')
    - After (B2 U2 B2), 1qt edges will be RH (good) and FH (good): +0+2+1(+0)
        - (B2 U2 B2 U' F2 R2 D') // no good
- On inverse, linearly: all variants have lower bound > spare moves.

Skeleton #8 (U2 B2 U F2 U' F2 D U R2) on inverse has FD corners, L=9, 3 spare moves.

- All variants have lower bound > spare moves.

Optimal is 12. Found 12 on skeleton #1.

### 4b2, scramble 4

`R' U' F D2 B' U' F2 B' U' L F2 R2 U2 L2 U2 F R2 F2 B R2 U2 R U2 R' U' F`

4b2 6e, goal 12.

Skeleton #1 R2 U' R2 U F2 U2 has RV corners, L=6, 6 spare moves. On inverse, (U2 L2 U F2 U' F2) has RD corners.

- After R2 B2 L2 B2, 1qt edges will be RV (good) and FH (good), fr=1: +3+0(+1)
    - R2 B2 L2 B2 U B2 D' // no good
- After U2 R2 U2 L2, 1qt edges will be RV (good) and FV (good): +3+0(+1)
    - **U2 R2 U2 L2 U B2 D R2 F2 U2 F2 B2 // 12**
- After (B2 R2 U2 F2), 1qt edges will be RD (good) and FD (good): +2+0(+1)
    - (B2 R2 U2 F2 U L2 D) // no good
- After (R2 U2 L2), 1qt edges will be RH (bad) and FH (good): +1+2(+3)
    - **(R2 U2 L2 U' R2 L2 B2 U' B2 R2 B2 L2) // 12**
- After (F2 B2 U2 F2 R2), 1qt edges will be RD (good) and FH (good), fr=1: +3+0(+3)
    - **(F2 B2 U2 F2 R2 U' L2 D' L2 U2 R2 U2) // 12**

Skeleton #2 R2 U L2 D U B2 D' F2 U2 has RV corners, L=9, 3 spare moves. On inverse, (U2 L2 U' F2 D U R2 D B2) has RD corners.

- All variants have lower bound > spare moves.

Skeleton #3 R2 U' B2 D U' B2 D' R2 U2 has RV corners, L=9, 3 spare moves. On inverse, (U2 L2 U R2 U D' L2 D R2) has RD corners.

- All variants have lower bound > spare moves.

Skeleton #4 R2 U' R2 U R2 U D' L2 U2 has FV corners, L=9, 3 spare moves.

- All variants have lower bound > spare moves.

Skeleton #5 R2 U' R2 U' F2 U D R2 has RD corners, L=8, 4 spare moves.

- R2 U' L2 D'
    - After B2, 1qt edges will be RD (good) and FD (good): +0+0+3(+1)
        - B2 U B2 R2 B2 U' // no good

Skeleton #6 R2 U' L2 U L2 D' U has HH corners, L=7, 5 spare moves.

- All variants have lower bound > spare moves, or reach HTR with no move left.

Skeleton #7 U F2 U F2 U R2 U' F2 has RD corners, L=8, 4 spare moves. On inverse, (R2 U' F2 U F2 U R2 U') has HH corners.

- U F2 U
    - After F2, 1qt edges will be RD (good) and FD (good): +0+0+1(+1)
        - F2 U B2 L2 D // no good
- U (R2 U')
    - After (L2 B2), 1qt edges will be FD (good) and RD (good): +0+1+1(+1)
        - (L2 B2 U' L2 B2 U') // no good
- (F2 L2 D R2 U')
    - After (B2), 1qt edges will be RH (good) and FH (good): +1+0+1(+0)
        - (B2 U' R2 B2 U) // no good

Skeleton #8 U2 R2 U B2 U' B2 U' R2 U' has HH corners, L=9, 3 spare moves. On inverse, (U F2 D' B2 U' B2 D F2 U2) has RV corners.

- (U) U2 R2 U
    - After B2, 1qt edges will be FH (bad) and RD (good): +0+0+0(+3)
        - B2 U' B2 U' // no good
- U2 R2 U B2 D'
    - After R2, 1qt edges will be RH (good) and FH (good): +0+0+0(+0)
        - R2 U' B2 U // no good
- On inverse: all variants have lower bound > spare moves.

Hard to find solutions:

Skeleton U R2 U L2 U F2 U F2 U2 R2 has DD corners, L=10, 2 spare moves. On inverse, (B2 U2 L2 U' L2 U F2 U F2 U') has HH corners.

- **U L2 D**
    - After B2 L2, 1qt edges will be FD (good) and RV (good): +0+1+0(+0)
        - **B2 L2 U' F2 U' R2 U2 R2 B2 // 12**
- **U (B2 R2 U2 R2 U)**
    - After (F2), 1qt edges will be RD (good) and FH (good): +1+0+1(+0)
        - **(F2 U L2 B2 D' L2) // 12**

Optimal is 12. Found 12 on skeleton #1.

### 4b2, scramble 5

`R' U' F D' F B D2 B2 U' B' L F2 U F2 D2 F2 D2 R2 B2 L2 F2 D R' U' F`

4b2 4e, goal 12.

Skeleton #1 L2 U2 B2 U' L2 U' has HH corners, L=6, 6 spare moves. On inverse, (U' R2 U R2 U2 F2) has DD corners.

- After B2 U2 R2, 1qt edges will be RH (good) and FH (good): +0+1(+0)
    - B2 U2 R2 U' F2 R2 U' // no good
- With no setup on inverse, 1qt edges will be FD (good) and RV (good): +0+6(+0)
    - (U F2 R2 F2 R2 B2 U2 R2 D') // no good

Skeleton #2 B2 U D B2 D' R2 U has HH corners, L=7, 5 spare moves. On inverse, (U' R2 U R2 U D R2) has FD corners.

- (U') F2 D
    - After F2 B2 R2 B2 L2, 1qt edges will be RD (good) and FH (good): +0+5+0(+0)
        - F2 B2 R2 B2 L2 U' R2 U // no good
- On inverse: all variants have lower bound > spare moves.

Skeleton #3 L2 U D R2 D' F2 U has HH corners, L=7, 5 spare moves. On inverse, (U' R2 U' R2 U D R2) has RD corners.

- All variants have lower bound > spare moves.

Skeleton #4 B2 U2 R2 U' R2 U D' U has HH corners, L=8, 4 spare moves.

- All variants have lower bound > spare moves.

Skeleton #5 L2 D' B2 U F2 U B2 D F2 has RD corners, L=9, 3 spare moves. On inverse, (R2 U R2 U L2 U F2 U' F2) has RD corners.

- B2 L2 D L2 U'
    - After L2, 1qt edges will be RD (good) and FH (good): +1+0+2(+0)
        - L2 U F2 U2 B2 U' // no good
- On inverse: all variants have lower bound > spare moves.

Skeleton #6 U2 R2 D R2 U' L2 U' F2 D' R2 has RD corners, L=10, 2 spare moves. On inverse, (R2 U B2 D B2 U L2 D' R2 U2) has RV corners.

- All variants have lower bound > spare moves.

Skeleton #7 U2 B2 U D B2 D B2 U has HH corners, L=8, 4 spare moves.

- All variants have lower bound > spare moves.

Skeleton #8 U2 R2 U D L2 D L2 U has HH corners, L=8, 4 spare moves.

- (U') U2 B2 R2 U'
    - After L2 B2 R2, 1qt edges will be RD (good) and FH (good): +1+3+0(+0)
        - L2 B2 R2 U R2 U' // no good

Optimal is 13. Found none.

## 4a2

### 4a2, scramble 1

`R' U' F L' R' D2 B2 D2 F2 L U2 R' U L2 D R2 B2 L2 U2 F' D2 R' D2 R' U' F`

4a2 4e, goal 12.

Skeleton #1 (L2 U B2 U2 R2 U' R2) on inverse has RD corners, L=7, 5 spare moves.

- After (R2), 1qt edges will be RV (bad) and FH (good): +0+2(+3)
    - (R2 U L2 F2 U2 R2 F2 D') // no good
- After (F2 L2), 1qt edges will be RH (bad) and FH (good): +1+1(+3)
    - **(F2 L2 U' B2 U2 F2 L2 D' F2 R2 F2 R2) // 12**

Skeleton #2 L2 D' F2 D U F2 U R2 has RD corners, L=8, 4 spare moves. On inverse, (L2 U' R2 U D L2 D L2) has RD corners.

- All variants have lower bound > spare moves.

Skeleton #3 L2 D F2 D U F2 U' B2 has RD corners, L=8, 4 spare moves. On inverse, (L2 U' B2 U D B2 D B2) has RD corners.

- L2 D R2 B2 U
    - After R2 L2, 1qt edges will be RD (good) and FH (good): +1+2+0(+0)
        - R2 L2 U R2 U' // no good
- (L2 U' B2 U')
    - After (R2 L2), 1qt edges will be RD (good) and FH (good): +0+2+1(+0)
        - (R2 L2 U' L2 F2 D) // no good

Skeleton #4 L2 D R2 U D L2 U' L2 has RD corners, L=8, 4 spare moves. On inverse, (L2 U F2 D U F2 D' R2) has RD corners.

- All variants have lower bound > spare moves.

Skeleton #5 L2 D' R2 U D L2 U F2 has RD corners, L=8, 4 spare moves. On inverse, (L2 U R2 U D L2 D' F2) has RD corners.

- L2 D' R2 U'
    - After R2 B2 L2, 1qt edges will be RD (good) and FH (good): +0+3+1(+0)
        - R2 B2 L2 U L2 B2 U // no good
- (R2 U B2 U)
    - After (B2 L2 F2), 1qt edges will be RD (good) and FH (good): +0+3+1(+0)
        - (B2 L2 F2 U' F2 L2 U') // no good

Skeleton #6 (L2 D R2 U2 B2 U' L2 D U') on inverse has HH corners, L=9, 3 spare moves.

- U (L2 D')
    - After (F2 R2 U2 F2 R2), 1qt edges will be RH (good) and FH (good): +0+2+0(+0)
        - (F2 R2 U2 F2 R2 U L2 U') // no good
- On inverse, linearly: all variants have lower bound > spare moves, or reach HTR with no move left.

Skeleton #7 L2 D F2 U2 L2 U' R2 U' D' has HH corners, L=9, 3 spare moves.

- All variants have lower bound > spare moves, or reach HTR with no move left.

Optimal is 12. Found 12 on skeleton #1.

### 4a2, scramble 2

`R' U' F R B2 R' F' R D R2 D L' F' D L U2 L B2 R F2 U2 R2 D2 R' U' F`

4a2 4e, goal 12.

Skeleton #1 U R2 U2 F2 U has HH corners, L=5, 7 spare moves. On inverse, (U B2 U2 R2 U) has HH corners.

- After R2 L2, 1qt edges will be RH (good) and FV (bad): +2+1(+3)
    - R2 L2 U' F2 U2 F2 L2 U' // no good
- After R2 B2 L2, 1qt edges will be RH (good) and FD (bad): +3+1(+3)
    - **R2 B2 L2 U' F2 U2 F2 L2 U R2 F2 R2 // 12**
- After L2 B2 R2, 1qt edges will be RH (good) and FD (bad): +3+1(+3)
    - **L2 B2 R2 U' F2 U2 F2 L2 U L2 F2 L2 // 12**
- After (R2 B2 R2), 1qt edges will be RH (good) and FD (bad): +3+1(+3)
    - (R2 B2 R2 U B2 R2 U2 R2 U) // no good
    - **(R2 B2 R2 U' R2 B2 U2 B2 U L2 F2 R2) // 12**
- After (L2 B2 L2), 1qt edges will be RH (good) and FD (bad): +3+1(+3)
    - **(L2 B2 L2 U' R2 B2 U2 B2 U R2 F2 L2) // 12**

Skeleton #2 D B2 U D B2 U has HH corners, L=6, 6 spare moves. On inverse, (D' F2 U D B2 U') has HH corners.

- **(U) D**
    - After B2, 1qt edges will be RV (good) and FV (good), fr=1: +0+0+2(+2)
        - **B2 U F2 B2 D' F2 R2 U2 R2 F2 // 12**
- (U') D'
    - After B2 U2 F2, 1qt edges will be RD (good) and FD (good): +0+2+2(+1)
        - B2 U2 F2 U' F2 B2 D // no good
- U R2 U
    - After R2 L2, 1qt edges will be RH (good) and FH (good): +0+2+3(+0)
        - R2 L2 U' R2 U2 F2 R2 U // no good
- U (D')
    - After (L2 F2), 1qt edges will be RD (good) and FH (good), fr=1: +0+1+2(+2)
        - (L2 F2 U F2 B2 D') // no good
- **U (D)**
    - After (R2 B2 U2 B2 R2), 1qt edges will be RD (good) and FH (good): +0+4+2(+0)
        - **(R2 B2 U2 B2 R2 U F2 B2 D' R2) // 12**
    - After (L2 F2 U2 B2 R2), 1qt edges will be RD (good) and FH (good): +0+4+2(+0)
        - **(L2 F2 U2 B2 R2 U F2 B2 D' L2) // 12**
- (U' B2 L2 D')
    - After (F2 B2), 1qt edges will be RH (good) and FH (good): +1+2+2(+0)
        - (F2 B2 U L2 U2 L2 U') // no good

Skeleton #3 D' L2 U D R2 U' has HH corners, L=6, 6 spare moves. On inverse, (D L2 U D L2 U) has HH corners.

- With the premove (U): all variants have lower bound > spare moves.
- Linearly: all variants have lower bound > spare moves.
- U' (D)
    - After (R2), 1qt edges will be FD (good) and RH (good): +0+0+6(+0)
        - (R2 U R2 U2 B2 R2 U2 F2 D) // no good
- On inverse, linearly: all variants have lower bound > spare moves, or reach HTR with no move left.

Skeleton #4 D R2 U D L2 U' has HH corners, L=6, 6 spare moves. On inverse, (D B2 U D F2 U') has HH corners.

- With the premove (U): all variants have lower bound > spare moves.
- U B2 U
    - After R2 L2, 1qt edges will be RH (good) and FH (good): +0+2+3(+0)
        - R2 L2 U R2 B2 R2 L2 D // no good
- On inverse, with the premove U: all variants have lower bound > spare moves.
- (U F2 R2 U')
    - After (F2 L2 B2), 1qt edges will be RH (good) and FH (good): +1+3+1(+0)
        - (F2 L2 B2 U B2 R2 D) // no good

Skeleton #5 D' B2 D U B2 U has HH corners, L=6, 6 spare moves. On inverse, (D' L2 D U L2 U) has HH corners.

- With the premove (U'): all variants have lower bound > spare moves.
- Linearly: all variants have lower bound > spare moves, or reach HTR with no move left.
- U' (D')
    - After (F2 L2), 1qt edges will be RV (bad) and FH (good): +0+1+2(+3)
        - (F2 L2 U' F2 B2 D) // no good
- (U' R2 F2 U')
    - After (R2 L2), 1qt edges will be RH (good) and FH (good): +1+2+2(+0)
        - (R2 L2 U' F2 B2 L2 D) // no good

Skeleton #6 D B2 U2 R2 U D U' has HH corners, L=7, 5 spare moves.

- All variants have lower bound > spare moves.

Skeleton #7 D U D B2 U2 L2 U' has HH corners, L=7, 5 spare moves. On inverse, (D L2 U2 B2 U D U') has HH corners.

- All variants have lower bound > spare moves.

Skeleton #8 R2 U D' B2 D F2 U2 R2 U has HH corners, L=9, 3 spare moves. On inverse, (U B2 U2 R2 U R2 U D' F2) has RD corners.

- All variants have lower bound > spare moves.

Optimal is 12. Found 12 on skeleton #1.

### 4a2, scramble 3

`R' U' F U' D2 F D2 L2 F R2 L2 D' R' U2 L D2 F2 R2 D2 B2 D' L2 D' R' U' F`

4a2 2e, goal 12.

Skeleton #1 L2 D L2 U2 B2 D' R2 U2 has FV corners, L=8, 4 spare moves. On inverse, (U2 B2 U B2 U2 L2 U' F2) has RD corners.

- On normal: all variants have lower bound > spare moves.
- After (U2 B2), 1qt edges will be RD (good) and FD (good): +0+3(+1)
    - **(U2 B2 U' F2 R2 B2 R2 U2 B2 U' L2 B2) // 12**
    - (U2 B2 U' B2 L2 F2 R2 U2 F2 D) // no good

Skeleton #2 L2 D' F2 U D B2 U R2 U2 has FV corners, L=9, 3 spare moves. On inverse, (U2 B2 U B2 U D F2 D' F2) has RD corners.

- All variants have lower bound > spare moves.

Skeleton #3 R2 U' L2 U D L2 D B2 U2 has FV corners, L=9, 3 spare moves. On inverse, (U2 F2 U' R2 U D L2 D L2) has RD corners.

- On normal: all variants have lower bound > spare moves.
- (U2 B2 U' F2 U)
    - After (L2 B2 R2), 1qt edges will be RD (good) and FH (good): +0+3+0(+0)
        - (L2 B2 R2 U' L2 U') // no good

Skeleton #4 R2 U F2 U D B2 D' F2 U2 has FV corners, L=9, 3 spare moves. On inverse, (U2 F2 U F2 U D F2 D' R2) has RD corners.

- L2 D F2 D'
    - After L2 F2 R2, 1qt edges will be FV (good) and RH (good): +0+3+0(+0)
        - L2 F2 R2 U B2 U // no good
- (U2 F2 U B2 U)
    - After (R2 B2 L2), 1qt edges will be RD (good) and FH (good): +0+3+0(+0)
        - (R2 B2 L2 U' R2 U) // no good

Skeleton #5 L2 D R2 U D R2 U' L2 U2 has FV corners, L=9, 3 spare moves. On inverse, (U2 B2 U' L2 U D L2 D B2) has RD corners.

- All variants have lower bound > spare moves.

Skeleton #6 L2 U F2 U2 R2 U' F2 D' U has HH corners, L=9, 3 spare moves.

- (U') R2 U
    - After B2 U2 L2, 1qt edges will be RV (bad) and FH (good): +0+0+0(+3)
        - B2 U2 L2 U' B2 U' // no good
- Linearly: all variants have lower bound > spare moves, or reach HTR with no move left.

Skeleton #7 L2 D L2 U2 B2 D R2 U D F2 has FD corners, L=10, 2 spare moves.

- All variants have lower bound > spare moves.

Skeleton #8 (U2 B2 U B2 U2 L2 U' F2 D' U') on inverse has HH corners, L=10, 2 spare moves.

- All variants have lower bound > spare moves.

Optimal is 12. Found 12 on skeleton #1.

### 4a2, scramble 4

`R' U' F R' F' U' L2 D' F2 D2 B2 D L2 U' B2 R D L2 R' F2 U F U R' U' F`

4a2 4e, goal 12.

Skeleton #1 (L2 U R2 U2 F2 U' F2) on inverse has RD corners, L=7, 5 spare moves.

- After (R2), 1qt edges will be RV (bad) and FH (good): +0+1(+3)
    - (R2 U' L2 U2 L2 B2 D) // no good

Skeleton #2 R2 D' L2 U D L2 U F2 has RD corners, L=8, 4 spare moves. On inverse, (L2 U R2 U D R2 D' F2) has RD corners.

- L2 U' R2 U'
    - After F2 R2 B2, 1qt edges will be RD (good) and FH (good): +0+3+1(+0)
        - F2 R2 B2 U R2 B2 U // no good
- (F2 L2 U' F2 D)
    - After (F2 B2), 1qt edges will be RD (good) and FH (good): +1+2+0(+0)
        - (F2 B2 U L2 U') // no good

Skeleton #3 R2 D F2 D U B2 U' B2 has RD corners, L=8, 4 spare moves. On inverse, (L2 U' F2 U D B2 D B2) has RD corners.

- R2 D B2 U
    - After R2 B2 L2, 1qt edges will be RD (good) and FH (good): +0+3+1(+0)
        - R2 B2 L2 U' B2 R2 U' // no good
- (L2 U' F2 U)
    - After (R2 L2), 1qt edges will be RD (good) and FH (good): +0+2+1(+0)
        - (R2 L2 U L2 B2 D) // no good

Skeleton #4 R2 D' F2 D U B2 U R2 has RD corners, L=8, 4 spare moves. On inverse, (R2 U' B2 U D B2 D L2) has RD corners.

- All variants have lower bound > spare moves.

Skeleton #5 R2 D R2 U D R2 U' L2 has RD corners, L=8, 4 spare moves. On inverse, (R2 U L2 D U R2 D' R2) has RD corners.

- All variants have lower bound > spare moves.

Skeleton #6 R2 U R2 U2 F2 U' R2 D' U' has HH corners, L=9, 3 spare moves.

- All variants have lower bound > spare moves, or reach HTR with no move left.

Skeleton #7 (L2 U R2 U2 F2 U' B2 D' U') on inverse has HH corners, L=9, 3 spare moves.

- **U (L2 U)**
    - After (R2 U2 F2), 1qt edges will be RH (good) and FD (bad): +0+0+0(+3)
        - **(R2 U2 F2 U' B2 U' L2 F2 L2) // 12**
- **U (L2 U')**
    - After (F2 U2 R2), 1qt edges will be RH (good) and FD (bad): +0+0+0(+3)
        - **(F2 U2 R2 U B2 U' L2 F2 L2) // 12**
- U (R2 D')
    - After (B2 U2 B2 R2), 1qt edges will be RH (good) and FH (good): +0+1+0(+0)
        - (B2 U2 B2 R2 U' L2 U') // no good
- On inverse, linearly: all variants have lower bound > spare moves, or reach HTR with no move left.

Optimal is 12. Found 12 on skeleton #7.

### 4a2, scramble 5

`R' U' F D' L' U' B2 R2 U2 R2 F U' D2 F2 B2 L F2 R' B2 L' B2 R2 D2 R' U' F`

4a2 4e, goal 12.

Skeleton #1 U2 F2 U B2 U2 R2 U' R2 U2 has RV corners, L=9, 3 spare moves. On inverse, (U2 R2 U L2 U2 B2 U' R2 U2) has FV corners.

- After F2 U2 B2, 1qt edges will be RV (good) and FH (good), fr=1: +1+1(+1)
    - F2 U2 B2 U R2 U2 L2 B2 D' // no good
- After (U2 L2), 1qt edges will be FV (good) and RH (good): +0+1(+0)
    - (U2 L2 U' R2 U2 L2 B2 U') // no good

Skeleton #2 U2 F2 U L2 U2 B2 U' L2 D' U has HH corners, L=10, 2 spare moves.

- (U') U2 F2 U
    - After L2 U2 B2, 1qt edges will be RH (good) and FH (good): +0+0+0(+0)
        - L2 U2 B2 U' L2 U' // no good

Skeleton #3 (U2 R2 U L2 U2 B2 U' R2 D' U) on inverse has HH corners, L=10, 2 spare moves.

- All variants have lower bound > spare moves, or reach HTR with no move left.

Optimal is 14. Found none.

## 4a1

### 4a1, scramble 1

`R' U' F L2 B' D2 F2 D2 U2 F2 R2 F' D' B' L2 D' R F2 D B2 F2 R' U' F`

4a1 2e, goal 12.

Skeleton #1 U D L2 U R2 has FD corners, L=5, 7 spare moves. On inverse, (B2 D F2 D' U) has HH corners.

- U
    - After L2 F2 R2, 1qt edges will be FD (good) and RV (bad): +0+3+1(+3)
        - L2 F2 R2 U' L2 F2 U' // no good
- On inverse, with the premove U': all variants have lower bound > spare moves.
- **(F2 D)**
    - After (L2), 1qt edges will be RH (good) and FV (bad): +0+0+2(+3)
        - (L2 U R2 L2 D) // no good
        - **(L2 U' R2 L2 D R2 F2 L2 D2) // 11**

Skeleton #2 U2 B2 D U D' B2 has FD corners, L=6, 6 spare moves. On inverse, (F2 D U D' B2 U2) has FV corners.

- U2 B2 D
    - After L2 F2 R2, 1qt edges will be FD (good) and RH (good): +0+3+2(+0)
        - L2 F2 R2 U' R2 L2 D' // no good
- (B2 U')
    - After (R2 L2), 1qt edges will be FV (good) and RH (good): +0+2+3(+0)
        - (R2 L2 U F2 R2 B2 D') // no good

Skeleton #3 U2 B2 D L2 D' U' has HH corners, L=6, 6 spare moves. On inverse, (U D' L2 U L2 U2) has FV corners.

- **(U)**
    - After U2 F2, 1qt edges will be RH (good) and FD (bad): +0+0(+3)
        - **U2 F2 U R2 U' L2 B2 R2 F2 B2 // 11**
    - After U2 B2 L2 F2 R2, 1qt edges will be RH (good) and FH (good): +3+0(+0)
        - U2 B2 L2 F2 R2 U' B2 U // no good
- **U2 F2 U**
    - After R2, 1qt edges will be RH (good) and FH (good): +0+0+5(+0)
        - **R2 U' F2 B2 R2 B2 L2 U' // 11**
        - R2 U' R2 F2 R2 F2 B2 D // no good
- **(U)**
    - After (L2 B2 R2 F2 B2), 1qt edges will be FV (good) and RH (good): +0+5+0(+0)
        - **(L2 B2 R2 F2 B2 U R2 U' F2 U2) // 11**
    - After (F2 B2 R2 B2 L2), 1qt edges will be FV (good) and RH (good): +0+5+0(+0)
        - **(F2 B2 R2 B2 L2 U R2 U' F2 U2) // 11**
    - After (L2 F2 L2 U2 F2 B2), 1qt edges will be FV (good) and RH (good): +0+6+0(+0)
        - (L2 F2 L2 U2 F2 B2 U' F2 U') // no good

Skeleton #4 F2 U D L2 U' L2 has FD corners, L=6, 6 spare moves. On inverse, (B2 U' L2 U D B2) has FD corners.

- All variants have lower bound > spare moves.

Skeleton #5 U2 R2 U D' R2 U' F2 has FD corners, L=7, 5 spare moves. On inverse, (F2 D F2 U D' B2 U2) has RV corners.

- **U2 R2 U'**
    - After L2 F2 R2, 1qt edges will be FD (good) and RH (good): +0+3+1(+0)
        - **L2 F2 R2 U' R2 B2 D' B2 // 11**
        - L2 F2 R2 U' L2 F2 U // no good
- **(B2 U)**
    - After (R2 F2), 1qt edges will be RV (good) and FH (good): +0+1+3(+0)
        - **(R2 F2 U F2 L2 B2 D R2 U2) // 11**
- (R2 F2 D')
    - After (R2), 1qt edges will be RV (good) and FV (good): +1+0+3(+1)
        - (R2 U' R2 B2 R2 U') // no good

Skeleton #6 U2 B2 D F2 D U' F2 has RD corners, L=7, 5 spare moves. On inverse, (R2 U D' L2 U' F2 U2) has FV corners.

- U2 B2 D
    - After B2, 1qt edges will be RH (bad) and FD (good): +0+0+2(+3)
        - B2 U' F2 B2 D' // no good
- (R2 U)
    - After (L2 F2 R2), 1qt edges will be FV (good) and RH (good): +0+3+1(+0)
        - (L2 F2 R2 U R2 F2 U') // no good

Skeleton #7 R2 U2 B2 U D F2 D' R2 has FD corners, L=8, 4 spare moves. On inverse, (B2 U' F2 U D B2 U2 R2) has DD corners.

- L2 U2 B2 U'
    - After F2 B2, 1qt edges will be FD (good) and RD (good): +0+2+0(+1)
        - F2 B2 U' F2 U' // no good
- (L2 F2 D)
    - After (L2), 1qt edges will be FV (good) and RD (good): +1+0+2(+0)
        - (L2 U' R2 L2 D) // no good

Skeleton #8 U2 B2 D' R2 U D F2 U2 has FV corners, L=8, 4 spare moves. On inverse, (U2 B2 U D R2 U' L2 U2) has FV corners.

- On normal: all variants have lower bound > spare moves.
- (U2 F2 U)
    - After (R2 L2), 1qt edges will be FD (bad) and RH (good), fr=1: +0+2+0(+2)
        - (R2 L2 U L2 U) // no good

Optimal is 11. Found 11 on skeleton #1.

### 4a1, scramble 2

`R' U' F U2 R2 U2 R' U' D2 B' D L' U2 L2 U' L2 D L2 D L2 F2 U F2 R' U' F`

4a1 4e, goal 12.

Skeleton #1 U2 L2 D F2 U2 R2 has DD corners, L=6, 6 spare moves. On inverse, (R2 U2 F2 U' R2 U2) has RV corners.

- After B2 R2 U2 B2, 1qt edges are FD (good) and RD (good): +2(+2)
    - **B2 R2 U2 B2 U L2 F2 U2 R2 B2 D2 // 11**
- After F2 L2 U2 F2, 1qt edges are FD (good) and RD (good): +2(+2)
    - **F2 L2 U2 F2 D' R2 F2 R2 F2 U2 F2 L2 // 12**
- After B2 U2 B2 U2 R2, 1qt edges are FD (good) and RD (good): +3(+2)
    - **B2 U2 B2 U2 R2 U' L2 F2 U2 R2 B2 D2 // 12**
- After R2 L2 F2 L2 U2 B2, 1qt edges are FD (good) and RD (good): +4(+2)
    - R2 L2 F2 L2 U2 B2 U' // no good
- After B2 U2 B2 L2 U2 R2, 1qt edges are FD (good) and RD (good): +4(+2)
    - **B2 U2 B2 L2 U2 R2 U' L2 F2 U2 B2 D2 // 12**
- After (U2 L2 U2 L2 F2), 1qt edges are RD (bad) and FV (good), fr=1: +2(+2)
    - (U2 L2 U2 L2 F2 D) // no good
- After (U2 F2 U2 B2 R2), 1qt edges are RD (bad) and FV (good): +2(+3)
    - **(U2 F2 U2 B2 R2 U L2 U2 R2 F2 D2 B2) // 12**
- After (U2 F2 L2 U2 B2 R2), 1qt edges are RD (bad) and FV (good), fr=1: +3(+2)
    - **(U2 F2 L2 U2 B2 R2 U' F2 D2 R2 B2) // 11**
- After (R2 B2 U2 F2 R2 B2 L2), 1qt edges are RD (bad) and FV (good), fr=1: +4(+2)
    - **(R2 B2 U2 F2 R2 B2 L2 D B2 D2 L2 F2) // 12**
- After (L2 F2 U2 F2 R2 F2 R2), 1qt edges are RD (bad) and FV (good), fr=1: +4(+2)
    - **(L2 F2 U2 F2 R2 F2 R2 D F2 U2 L2 F2) // 12**

Skeleton #2 U D F2 U F2 U2 R2 has DD corners, L=7, 5 spare moves. On inverse, (L2 U2 F2 U' F2 D U) has HH corners.

- On normal: all variants have lower bound > spare moves.
- U'
    - After (U2 L2 B2 U2 L2 F2), 1qt edges will be RH (good) and FH (good): +3+1(+0)
        - (U2 L2 B2 U2 L2 F2 U R2 B2 U') // no good
- On inverse, linearly: all variants have lower bound > spare moves.

Skeleton #3 U2 L2 D B2 U D B2 has RD corners, L=7, 5 spare moves. On inverse, (R2 U D R2 D' R2 U2) has RV corners.

- All variants have lower bound > spare moves.

Skeleton #4 R2 U D B2 D B2 U2 L2 has DD corners, L=8, 4 spare moves. On inverse, (L2 U2 F2 D L2 U D B2) has RD corners.

- **L2 D**
    - After B2 R2 F2, 1qt edges will be FD (good) and RV (good): +0+3+0(+0)
        - **B2 R2 F2 U' B2 U' R2 D2 B2 // 11**
- R2 U
    - After F2 L2 B2, 1qt edges will be FD (good) and RV (good): +0+3+0(+0)
        - F2 L2 B2 U' L2 U' // no good
- **(B2 U2 L2 U)**
    - After (F2), 1qt edges will be RD (good) and FH (good): +0+0+3(+0)
        - **(F2 U B2 L2 F2 D' R2) // 11**
- (F2 U2 L2 D)
    - After (B2), 1qt edges will be RD (good) and FD (good): +0+0+3(+1)
        - (B2 U R2 F2 R2 U') // no good

Skeleton #5 U2 L2 D' F2 D U F2 has FD corners, L=7, 5 spare moves. On inverse, (F2 D U F2 U' B2 U2) has RV corners.

- All variants have lower bound > spare moves.

Skeleton #6 U2 L2 D' R2 D U L2 U2 has FV corners, L=8, 4 spare moves. On inverse, (U2 F2 U D B2 D L2 U2) has RV corners.

- **U2 R2 U'**
    - After F2 R2, 1qt edges will be FV (good) and RV (good): +0+1+2(+1)
        - **F2 R2 U' R2 L2 D' B2 L2 U2 // 12**
        - F2 R2 U R2 L2 D // no good
- On inverse: all variants have lower bound > spare moves.

Skeleton #7 (U2 L2 U D R2 U F2 U2) on inverse has RV corners, L=8, 4 spare moves.

- All variants have lower bound > spare moves.

Skeleton #8 U2 L2 U R2 U2 B2 D U' has HH corners, L=8, 4 spare moves. On inverse, (U D R2 U2 B2 D L2 U2) has RV corners.

- (U)
    - After L2 U2 L2, 1qt edges will be RH (good) and FH (good): +1+1(+0)
        - L2 U2 L2 U' R2 F2 U2 F2 D // no good
- **(U')**
    - After U2 L2, 1qt edges will be RH (good) and FH (good): +0+2(+0)
        - **U2 L2 U F2 R2 U2 B2 L2 U' L2 R2 // 12**
- U2 L2 D
    - After B2 U2 B2 R2, 1qt edges will be RH (good) and FH (good): +0+1+2(+0)
        - B2 U2 B2 R2 U R2 L2 D' // no good
- (U)
    - After (R2 L2), 1qt edges will be RV (good) and FH (good), fr=1: +0+2+1(+1)
        - (R2 L2 U B2 U2 F2 L2 D) // no good
- **(U')**
    - After (R2 L2), 1qt edges will be RV (good) and FH (good): +0+2+2(+0)
        - **(R2 L2 U R2 F2 U2 L2 B2 U' R2 D2) // 12**

Optimal is 11. Found 11 on skeleton #1.

### 4a1, scramble 3

`R' U' F U R U' D' L' F U2 B U R2 F' R2 F2 B' D2 R2 F' R2 B2 U2 R' U' F`

4a1 6e, goal 12.

Skeleton #1 U2 R2 D U D B2 has RD corners, L=6, 6 spare moves. On inverse, (L2 D U D' B2 U2) has RV corners.

- All variants have lower bound > spare moves.

Skeleton #2 D U B2 U' L2 has RD corners, L=5, 7 spare moves. On inverse, (L2 U F2 U D) has HH corners.

- D
    - After B2 L2 B2, 1qt edges will be RD (good) and FH (good): +0+3+4(+0)
        - B2 L2 B2 U' L2 U2 B2 R2 F2 D // no good
- D'
    - After (F2 L2 B2 R2 B2), 1qt edges will be RH (good) and FD (bad): +4+0(+3)
        - (F2 L2 B2 R2 B2 U F2 U) // no good
- (F2 L2 D')
    - After (F2), 1qt edges will be RV (bad) and FH (good): +1+0+3(+3)
        - (F2 U R2 F2 R2 U) // no good

Skeleton #3 U2 R2 U' B2 D U' has HH corners, L=6, 6 spare moves. On inverse, (U D' B2 U L2 U2) has RV corners.

- With the premove (U): all variants have lower bound > spare moves.
- Linearly: all variants have lower bound > spare moves.
- (U)
    - After (L2 B2 R2), 1qt edges will be RV (good) and FV (good): +0+3+1(+1)
        - (L2 B2 R2 U F2 R2 U) // no good

Skeleton #4 R2 U D B2 U R2 has RD corners, L=6, 6 spare moves. On inverse, (L2 D' L2 U D F2) has RD corners.

- **R2 U**
    - After R2 B2 R2, 1qt edges will be RD (good) and FH (good): +0+3+3(+0)
        - **R2 B2 R2 U R2 B2 U2 R2 D' L2 // 12**
    - After L2 B2 L2, 1qt edges will be RD (good) and FH (good): +0+3+3(+0)
        - L2 B2 L2 U R2 F2 U2 L2 U // no good
- **(L2 D)**
    - After (R2 U2 B2 R2), 1qt edges will be RD (good) and FH (good): +0+3+3(+0)
        - **(R2 U2 B2 R2 U' R2 B2 R2 U' R2) // 12**
    - After (L2 U2 F2 L2), 1qt edges will be RD (good) and FH (good): +0+3+3(+0)
        - (L2 U2 F2 L2 U' B2 L2 B2 U) // no good

Skeleton #5 R2 U2 F2 U D' B2 D' B2 has RD corners, L=8, 4 spare moves. On inverse, (L2 D' F2 U D F2 U2 L2) has DD corners.

- B2 U2 R2 U'
    - After B2 R2 B2, 1qt edges will be RD (good) and FH (good): +0+3+1(+0)
        - B2 R2 B2 U F2 L2 U // no good
- **B2 U2 F2 L2 U**
    - After R2 L2, 1qt edges will be RD (good) and FD (good): +1+2+0(+1)
        - **R2 L2 U F2 U' L2 B2 // 12**
- **(B2 L2 D)**
    - After (R2), 1qt edges will be FV (good) and RV (good): +1+0+2(+1)
        - **(R2 U' F2 B2 D' L2 F2 U2 B2) // 12**
        - (R2 U F2 B2 D) // no good

Skeleton #6 U2 F2 U D' B2 D F2 has RD corners, L=7, 5 spare moves. On inverse, (L2 D B2 U D' B2 U2) has FV corners.

- U2 B2 D'
    - After R2 L2, 1qt edges will be RD (good) and FH (good): +0+2+2(+0)
        - R2 L2 U F2 B2 L2 D // no good
- (F2 R2 U')
    - After (R2), 1qt edges will be FV (good) and RV (good): +1+0+2(+1)
        - (R2 U' R2 L2 D) // no good

Skeleton #7 U2 R2 D' F2 U D' F2 has FD corners, L=7, 5 spare moves. On inverse, (B2 U D' F2 D' B2 U2) has RV corners.

- U2 F2 L2 U
    - After R2, 1qt edges will be FD (good) and RH (good): +1+0+3(+0)
        - R2 U' R2 F2 L2 D' // no good
- (B2 U')
    - After (R2 L2), 1qt edges will be RV (good) and FH (good): +0+2+2(+0)
        - (R2 L2 U R2 L2 B2 D') // no good

Skeleton #8 U2 R2 D R2 U D B2 U2 has RV corners, L=8, 4 spare moves. On inverse, (U2 L2 D U F2 U' L2 U2) has RV corners.

- All variants have lower bound > spare moves.

Optimal is 12. Found 12 on skeleton #4.

### 4a1, scramble 4

`R' U' F U' R D2 R2 U F U' F L' F U2 R2 F R2 F2 U2 R2 F B D2 R' U' F`

4a1 6e, goal 12.

Skeleton #1 D U D R2 U2 has FV corners, L=5, 7 spare moves. On inverse, (U2 F2 D U D') has HH corners.

- All variants have lower bound > spare moves.

Skeleton #2 U' R2 D U has HH corners, L=4, 8 spare moves. On inverse, (U D R2 D) has HH corners.

- (U')
    - With no setup, 1qt edges will be RH (good) and FD (bad): +0+5(+3)
        - U' F2 L2 U2 B2 L2 F2 U' // no good
- Linearly: all variants have lower bound > spare moves.
- D'
    - With no setup, 1qt edges will be FV (bad) and RD (good): +0+5(+3)
        - (U' L2 F2 R2 F2 B2 U) // no good
- (U)
    - After (R2 B2 L2), 1qt edges will be RH (good) and FV (bad): +0+3+1(+3)
        - (R2 B2 L2 U' L2 F2 U) // no good

Skeleton #3 D B2 U D R2 has FD corners, L=5, 7 spare moves. On inverse, (B2 U D R2 D') has HH corners.

- On normal: all variants have lower bound > spare moves.
- On inverse, with the premove D: all variants have lower bound > spare moves.
- (B2 U')
    - After (R2 B2 L2), 1qt edges will be RH (good) and FH (good): +0+3+3(+0)
        - (R2 B2 L2 U' R2 B2 U2 L2 D) // no good

Skeleton #4 D' L2 U D' L2 U2 has RV corners, L=6, 6 spare moves. On inverse, (U2 R2 U D' L2 D) has HH corners.

- D'
    - After F2 L2, 1qt edges will be RV (good) and FH (good): +0+1+5(+0)
        - F2 L2 U F2 B2 L2 F2 L2 D // no good
- D'
    - After (U2 L2), 1qt edges will be RD (good) and FD (good): +0+5(+1)
        - (U2 L2 U L2 F2 R2 F2 B2 U) // no good
- (U2 R2 D')
    - After (R2 F2 R2), 1qt edges will be RD (bad) and FH (good): +0+3+0(+3)
        - (R2 F2 R2 U' F2 U) // no good

Skeleton #5 D R2 U D R2 U2 B2 has DD corners, L=7, 5 spare moves. On inverse, (R2 U2 F2 D U B2 D') has HH corners.

- On normal: all variants have lower bound > spare moves.
- On inverse, with the premove D: all variants have lower bound > spare moves.
- **(R2 U2 F2 D')**
    - After (R2 L2), 1qt edges will be RH (good) and FH (good): +0+2+0(+0)
        - **(R2 L2 U' R2 U' B2 F2) // 11**
    - After (R2 L2), 1qt edges will be RH (good) and FH (good): +0+2+2(+0)
        - (R2 L2 U' F2 B2 L2 D) // no good
- **(U2 F2 U2 R2 D)**
    - After (R2 L2), 1qt edges will be RH (good) and FH (good): +1+2+0(+0)
        - **(R2 L2 U' L2 U' F2 B2) // 12**

Skeleton #6 B2 U D' L2 D' B2 U2 has FV corners, L=7, 5 spare moves. On inverse, (U2 F2 U F2 U D' L2) has FD corners.

- F2 U'
    - After F2 B2, 1qt edges will be FV (good) and RH (good): +0+2+3(+0)
        - F2 B2 U R2 U2 F2 B2 D // no good
- On inverse: all variants have lower bound > spare moves.

Skeleton #7 R2 U D' F2 U' F2 U2 has FV corners, L=7, 5 spare moves. On inverse, (U2 F2 U R2 D U' B2) has RD corners.

- R2 U
    - After B2 R2 F2, 1qt edges will be FV (good) and RH (good): +0+3+1(+0)
        - B2 R2 F2 U B2 R2 D' // no good
- (U2 F2 U)
    - After (L2), 1qt edges will be RH (bad) and FD (good): +0+0+2(+3)
        - (L2 U' R2 L2 D') // no good

Skeleton #8 U2 R2 U D' B2 D F2 U2 has FV corners, L=8, 4 spare moves. On inverse, (U2 F2 U' R2 D U' B2 U2) has RV corners.

- All variants have lower bound > spare moves.

Optimal is 11. Found 11 on skeleton #5.

### 4a1, scramble 5

`R' U' F R U L U2 L' D2 B' U R2 B R2 F2 U L2 D L2 F2 U2 R' U' F`

4a1 6e, goal 12.

Skeleton #1 F2 U D U B2 U2 has FV corners, L=6, 6 spare moves. On inverse, (U2 B2 U D U B2) has FD corners.

- **F2 U**
    - After F2 B2, 1qt edges will be FV (good) and RH (good), fr=1: +0+2+3(+1)
        - **F2 B2 U F2 R2 F2 U B2 D2 B2 // 12**
- **F2 U'**
    - After F2 B2, 1qt edges will be FV (good) and RH (good), fr=1: +0+2+3(+1)
        - **F2 B2 U F2 R2 F2 U' B2 D2 F2 // 12**
- **B2 D**
    - After R2 B2 R2, 1qt edges will be FV (good) and RH (good), fr=1: +0+3+2(+1)
        - **R2 B2 R2 U R2 L2 D' F2 D2 B2 // 12**
    - After R2 F2 L2, 1qt edges will be FV (good) and RH (good), fr=1: +0+3+2(+1)
        - R2 F2 L2 U' F2 B2 D // no good
- On inverse: all variants have lower bound > spare moves.

Skeleton #2 U D' L2 D' L2 U2 has FV corners, L=6, 6 spare moves. On inverse, (U2 B2 D' F2 D' U') has HH corners.

- U'
    - After R2 F2 R2, 1qt edges will be FH (bad) and RV (good), fr=1: +0+3+1(+2)
        - R2 F2 R2 U' B2 R2 U // no good
- On inverse, with the premove U: all variants have lower bound > spare moves.
- On inverse, linearly: all variants have lower bound > spare moves.

Skeleton #3 F2 U' L2 D' U has HH corners, L=5, 7 spare moves. On inverse, (U D L2 D' R2) has FD corners.

- (U')
    - After R2 F2, 1qt edges will be RD (bad) and FH (good): +1+2(+3)
        - R2 F2 U' F2 U2 B2 U' // no good
- R2 F2 U'
    - After F2 U2 B2, 1qt edges will be RH (good) and FH (good): +1+2+3(+0)
        - F2 U2 B2 U F2 R2 F2 U // no good
- (U')
    - After (F2 B2), 1qt edges will be FD (good) and RV (bad): +0+2+2(+3)
        - (F2 B2 U R2 U2 L2 U) // no good

Skeleton #4 R2 U D' L2 D F2 U2 has FV corners, L=7, 5 spare moves. On inverse, (U2 B2 U' F2 D U' B2) has RD corners.

- **R2 U'**
    - After R2 F2 L2, 1qt edges will be FV (good) and RH (good), fr=1: +0+3+1(+1)
        - **R2 F2 L2 U' L2 F2 D' F2 D2 F2 // 12**
        - R2 F2 L2 U' R2 B2 U // no good
- On inverse: all variants have lower bound > spare moves.

Skeleton #5 F2 U' F2 D U' B2 U2 has RV corners, L=7, 5 spare moves. On inverse, (U2 R2 U D' R2 D F2) has FD corners.

- All variants have lower bound > spare moves.

Skeleton #6 F2 U B2 U D B2 U2 R2 has DD corners, L=8, 4 spare moves. On inverse, (F2 U2 R2 D U' L2 D' F2) has FD corners.

- On normal: all variants have lower bound > spare moves.
- **(F2 U2 R2 D)**
    - After (R2 B2 L2), 1qt edges will be FD (good) and RD (good): +0+3+0(+1)
        - **(R2 B2 L2 U L2 U B2 L2) // 12**
- (F2 U2 L2 U')
    - After (L2 B2 R2), 1qt edges will be FD (good) and RH (good): +0+3+1(+0)
        - (L2 B2 R2 U' L2 F2 U') // no good

Skeleton #7 F2 U L2 D U B2 has FD corners, L=6, 6 spare moves. On inverse, (F2 U D L2 D L2) has FD corners.

- F2 U
    - After R2, 1qt edges will be FV (bad) and RD (good): +0+0+3(+3)
        - R2 U' L2 B2 L2 U' // no good
- **L2 F2 U'**
    - After F2 R2 L2, 1qt edges will be FD (good) and RH (good): +1+2+2(+0)
        - **F2 R2 L2 U R2 L2 D B2 // 11**
- **(B2 U')**
    - After (F2 B2), 1qt edges will be FD (good) and RD (good): +0+2+0(+1)
        - (F2 B2 U' L2 U') // no good
    - After (F2 B2), 1qt edges will be FD (good) and RD (good): +0+2+2(+1)
        - **(F2 B2 U' F2 B2 R2 D B2 R2) // 11**

Skeleton #8 R2 U2 B2 U D R2 D' F2 U2 has FV corners, L=9, 3 spare moves. On inverse, (U2 B2 U B2 U D R2 U2 B2) has DD corners.

- All variants have lower bound > spare moves.

Hard to find solutions:

Skeleton F2 U L2 U2 F2 D U' B2 has RD corners, L=8, 4 spare moves.

- **F2 U**
    - After R2 U2 F2, 1qt edges will be RD (good) and FD (good): +0+0+3(+1)
        - **R2 U2 F2 U L2 B2 L2 U R2 B2 // 12**
- **F2 U'**
    - After F2 U2 R2, 1qt edges will be RD (good) and FD (good): +0+0+3(+1)
        - **F2 U2 R2 U' L2 B2 L2 U R2 B2 // 12**
    - After F2 U2 B2 L2, 1qt edges will be RD (good) and FH (good): +0+1+3(+0)
        - **F2 U2 B2 L2 U F2 R2 F2 U' L2 // 12**

Optimal is 11. Found 11 on skeleton #7.

### 4a1, scramble 6

`R' U' F D' L U' L F U2 F2 R B2 U2 D2 L2 B R2 F L2 F' D2 R D R' U' F`

4a1 2e, goal 12.

Skeleton #1 U D U B2 U2 R2 has DD corners, L=6, 6 spare moves. On inverse, (R2 U2 B2 U D' U) has HH corners.

- U
    - After F2 R2 F2, 1qt edges will be FD (good) and RV (good): +0+3+3(+0)
        - F2 R2 F2 U' F2 R2 F2 U // no good
- U'
    - After (R2 U2 B2), 1qt edges will be RH (good) and FV (bad): +0+3(+3)
        - (R2 U2 B2 U F2 L2 F2 U') // no good
- On inverse, linearly: all variants have lower bound > spare moves, or reach HTR with no move left.

Skeleton #2 U B2 U D B2 U2 has FV corners, L=6, 6 spare moves. On inverse, (U2 B2 U D B2 U') has HH corners.

- U
    - After F2, 1qt edges will be FV (good) and RD (bad): +0+0+3(+3)
        - F2 U L2 F2 L2 U' // no good
- U
    - After (U2 B2), 1qt edges will be FD (good) and RV (bad): +0+3(+3)
        - (U2 B2 U F2 L2 F2 U') // no good
- (U2 B2 U)
    - After (B2 R2 F2), 1qt edges will be RH (good) and FH (good): +0+3+1(+0)
        - (B2 R2 F2 U' F2 R2 U) // no good

Skeleton #3 U' R2 U D R2 has RD corners, L=5, 7 spare moves. On inverse, (R2 U D R2 U) has HH corners.

- **U'**
    - After L2, 1qt edges will be RH (bad) and FD (good): +0+0+3(+3)
        - **L2 U' F2 L2 F2 U F2 R2 F2 R2 F2 // 12**
        - **L2 U' B2 L2 B2 U F2 L2 B2 L2 B2 // 12**
    - After F2 L2, 1qt edges will be RH (bad) and FH (good): +0+1+3(+3)
        - **F2 L2 U' F2 L2 F2 U B2 R2 B2 R2 // 12**
        - **F2 L2 U' B2 L2 B2 U F2 R2 F2 R2 // 12**
    - After B2 R2, 1qt edges will be RH (bad) and FH (good): +0+1+3(+3)
        - **B2 R2 U R2 B2 R2 U' B2 L2 F2 R2 // 12**
        - **B2 R2 U L2 B2 L2 U' F2 L2 B2 R2 // 12**
    - After L2 F2 R2 F2, 1qt edges will be RD (good) and FD (good): +0+3+3(+1)
        - **L2 F2 R2 F2 U' F2 L2 F2 U R2 F2 // 12**
    - After L2 F2 L2 B2, 1qt edges will be RD (good) and FD (good): +0+3+3(+1)
        - **L2 F2 L2 B2 U L2 B2 L2 U' L2 B2 // 12**
    - After L2 B2 R2 B2, 1qt edges will be RD (good) and FD (good): +0+3+3(+1)
        - **L2 B2 R2 B2 U' B2 L2 B2 U R2 F2 // 12**
    - After L2 B2 L2 F2, 1qt edges will be RD (good) and FD (good): +0+3+3(+1)
        - **L2 B2 L2 F2 U R2 B2 R2 U' L2 B2 // 12**
    - After F2 L2 F2 R2 F2, 1qt edges will be RD (good) and FH (good): +0+4+3(+0)
        - **F2 L2 F2 R2 F2 U' B2 L2 B2 U R2 // 12**
    - After F2 L2 B2 R2 B2, 1qt edges will be RD (good) and FH (good): +0+4+3(+0)
        - **F2 L2 B2 R2 B2 U' F2 L2 F2 U R2 // 12**
    - After B2 R2 F2 L2 B2, 1qt edges will be RD (good) and FH (good): +0+4+3(+0)
        - **B2 R2 F2 L2 B2 U' B2 L2 B2 U R2 // 12**
    - After B2 R2 B2 L2 F2, 1qt edges will be RD (good) and FH (good): +0+4+3(+0)
        - **B2 R2 B2 L2 F2 U' F2 L2 F2 U R2 // 12**
    - After F2 L2 F2 L2 B2, 1qt edges will be RD (good) and FH (good): +0+4+3(+0)
        - F2 L2 F2 L2 B2 U L2 B2 L2 U' // no good
- **U'**
    - After (R2), 1qt edges will be RH (bad) and FD (good): +0+3(+3)
        - **(R2 U' F2 L2 F2 U F2 L2 B2 R2 B2) // 12**
        - **(R2 U' B2 L2 B2 U F2 R2 F2 L2 F2) // 12**
    - After (F2 R2), 1qt edges will be RH (bad) and FH (good): +1+3(+3)
        - **(F2 R2 U' F2 L2 F2 U F2 R2 F2 L2) // 12**
        - **(F2 R2 U' B2 L2 B2 U B2 R2 B2 L2) // 12**
    - After (B2 L2), 1qt edges will be RH (bad) and FH (good): +1+3(+3)
        - **(B2 L2 U R2 B2 R2 U' F2 L2 B2 L2) // 12**
        - **(B2 L2 U L2 B2 L2 U' B2 L2 F2 L2) // 12**
    - After (R2 F2 R2 F2), 1qt edges will be RD (good) and FD (good): +3+3(+1)
        - **(R2 F2 R2 F2 U' B2 L2 B2 U L2 F2) // 12**
    - After (R2 F2 L2 B2), 1qt edges will be RD (good) and FD (good): +3+3(+1)
        - **(R2 F2 L2 B2 U R2 B2 R2 U' R2 B2) // 12**
    - After (R2 B2 R2 B2), 1qt edges will be RD (good) and FD (good): +3+3(+1)
        - **(R2 B2 R2 B2 U' F2 L2 F2 U L2 F2) // 12**
    - After (R2 B2 L2 F2), 1qt edges will be RD (good) and FD (good): +3+3(+1)
        - **(R2 B2 L2 F2 U L2 B2 L2 U' R2 B2) // 12**
    - After (F2 R2 F2 R2 F2), 1qt edges will be RD (good) and FH (good): +4+3(+0)
        - **(F2 R2 F2 R2 F2 U' F2 L2 F2 U L2) // 12**
    - After (F2 R2 B2 R2 B2), 1qt edges will be RD (good) and FH (good): +4+3(+0)
        - **(F2 R2 B2 R2 B2 U' B2 L2 B2 U L2) // 12**
    - After (B2 L2 F2 L2 B2), 1qt edges will be RD (good) and FH (good): +4+3(+0)
        - **(B2 L2 F2 L2 B2 U' F2 L2 F2 U L2) // 12**
    - After (B2 L2 B2 L2 F2), 1qt edges will be RD (good) and FH (good): +4+3(+0)
        - **(B2 L2 B2 L2 F2 U' B2 L2 B2 U L2) // 12**
    - After (F2 R2 F2 L2 B2), 1qt edges will be RD (good) and FH (good): +4+3(+0)
        - (F2 R2 F2 L2 B2 U R2 B2 R2 U') // no good
- **(R2 D')**
    - After (R2 L2), 1qt edges will be RH (good) and FD (bad): +0+2+2(+3)
        - **(R2 L2 U' R2 L2 F2 D' L2 B2 R2) // 12**
- (F2 L2 U')
    - After (F2 B2), 1qt edges will be RH (good) and FH (good): +1+2+2(+0)
        - (F2 B2 U' R2 L2 B2 D') // no good
- **(B2 R2 D')**
    - After (L2 B2 L2), 1qt edges will be RH (good) and FD (bad): +1+3+0(+3)
        - **(L2 B2 L2 U R2 U' L2 F2 R2) // 12**

Skeleton #4 U' B2 U D B2 U2 has RV corners, L=6, 6 spare moves. On inverse, (U2 R2 U D R2 U) has HH corners.

- U'
    - After R2 B2, 1qt edges will be RH (bad) and FH (good), fr=1: +0+1+3(+2)
        - R2 B2 U L2 F2 R2 D' // no good
- U'
    - After (U2 R2), 1qt edges will be FD (good) and RV (bad), fr=1: +0+3(+3)
        - (U2 R2 U F2 R2 B2 D) // no good
- On inverse, linearly: all variants have lower bound > spare moves, or reach HTR with no move left.

Skeleton #5 U R2 U D R2 has FD corners, L=5, 7 spare moves. On inverse, (F2 U D B2 U') has HH corners.

- On normal: all variants have lower bound > spare moves.
- U
    - After (R2 F2), 1qt edges will be RH (bad) and FH (good), fr=1: +1+3(+3)
        - (R2 F2 U' B2 R2 F2 D') // no good
- (F2 U')
    - After (F2 B2), 1qt edges will be RV (bad) and FH (good): +0+2+2(+3)
        - (F2 B2 U F2 U2 F2 U) // no good

Skeleton #6 L2 U D' F2 U L2 U2 B2 has DD corners, L=8, 4 spare moves. On inverse, (R2 U2 B2 D' B2 U D' L2) has RD corners.

- R2 U'
    - After F2 B2, 1qt edges will be FD (good) and RV (good): +0+2+2(+0)
        - F2 B2 U R2 L2 F2 D' // no good
- (B2 R2 U2 R2 D)
    - After (L2), 1qt edges will be RD (good) and FH (good): +1+0+2(+0)
        - (L2 U R2 L2 D) // no good

Skeleton #7 B2 U D' R2 D R2 U2 F2 has DD corners, L=8, 4 spare moves. On inverse, (R2 U2 B2 D' L2 D U' B2) has FD corners.

- F2 U
    - After F2 L2 B2, 1qt edges will be FD (good) and RV (good): +0+3+1(+0)
        - F2 L2 B2 U R2 B2 D // no good
- On inverse: all variants have lower bound > spare moves.

Skeleton #8 U B2 U2 L2 D' U has HH corners, L=6, 6 spare moves. On inverse, (U D B2 U2 R2 U) has HH corners.

- **(U')**
    - With no setup, 1qt edges will be RD (bad) and FH (good): +0+2(+3)
        - **U R2 B2 U2 R2 B2 D' B2 L2 F2 // 11**
    - With no setup, 1qt edges will be RD (bad) and FH (good): +0+3(+3)
        - U B2 U2 R2 L2 F2 R2 U // no good
- U
    - After R2 F2 U2 L2 F2, 1qt edges will be RH (good) and FH (good): +0+2+3(+0)
        - R2 F2 U2 L2 F2 U' B2 L2 F2 D' // no good
- U'
    - With no setup, 1qt edges will be FD (good) and RD (good): +0+3(+1)
        - (U' F2 L2 F2 U') // no good
- **U**
    - With no setup, 1qt edges will be FV (good) and RV (good): +0+3(+1)
        - **(U' B2 R2 F2 D F2 L2 D2 B2 R2) // 11**
- (U')
    - After (F2 R2 B2), 1qt edges will be RH (good) and FH (good): +0+3+2(+0)
        - (F2 R2 B2 U L2 F2 U2 R2 F2 U) // no good

Optimal is 11. Found 11 on skeleton #8.
