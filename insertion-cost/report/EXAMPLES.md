# Examples: what does this skeleton cost?

Worked examples for the write-up *Insertion cost by skeleton type*. First, five worked examples (one from the tutorial, four from the server) redone with the search: what the author inserted, and the best there is with 8-movers, with algs up to 10 moves and up to 12. Then 200 skeletons to play along with, 20 for each of ten kinds of leftover: put the scramble and the skeleton on a cube, look for the insertions, then unfold the answer. Then the tally.

The script that writes this page replays everything on it on a sticker-level cube: every scramble, skeleton, insertion and solution.

## From the tutorial and the server

Five worked examples, the first from the tutorial and four from the server, each with what was inserted at the time and then the best there is on the same skeleton: with 8 moves or less per insertion, with up to 10, and with up to 12. *A comm plus an alg* is two insertions of which only one has to be a 3-cycle; the other may be any alg of that length that leaves a 3c or solves what the comm left (write-up, section 3). It is shown when it beats everything else at that length.

### A 5c from the tutorial

The example of section 2.5.3 of Sebastiano Tronto's tutorial ("Classic PDR"). The tutorial takes it from Alexandre Campos's collection of PDR solves: "Alexandre has collected some PDR solves in a document … Let’s look at the first one as an example". 17 moves to five corners, then two comms.

Scramble: `R' U' F L2 U2 B' L2 F' U2 B L2 B R' B2 L U B L2 B' D' F2 R F R' U' F`

Skeleton: `D' R' U' F R2 L U R D F2 D2 B2 U2 L2 D R2 U` (17), leaves a corner 5-cycle: DBL → UBL → UFR → UBR → UFL → DBL

**By hand**: `D' R' U2 R D R' U2 R` (8-4) and `F2 R B2 R' F2 R B2 R'` (8-2). 27 moves.

```
Solution: D2 R' U2 R D R' U F' R B2 R' F2 R B2 R L U R D F2 D2 B2 U2 L2 D R2 U (27)
```

**8 moves or less per insertion** (two comms): 27 in all.

```
D' * R' U' F ^ R2 L U R D F2 D2 B2 U2 L2 D R2 U
* = D' R' U2 R D R' U2 R // (8-4/21)
^ = F2 R B2 R' F2 R B2 R' // (8-2/27)
Solution: D2 R' U2 R D R' U F' R B2 R' F2 R B2 R L U R D F2 D2 B2 U2 L2 D R2 U (27)
```

**Up to 10 moves per insertion**: nothing better with one comm, two comms or one alg.

**Up to 12 moves per insertion**: nothing better with one comm, two comms or one alg.

The two comms in the tutorial are the best pair of 8-movers, and nothing up to 12 moves beats them, a comm plus an alg included.

### A 5c where the comms are right and the alg list is not exhausted

jperm ([23 Jun 2024](https://discord.com/channels/1007840975726575667/1077216728683135046/1254564990942183455)): "theres a 19 to 5c that i found but could not find any good insertions". The skeleton is 21 moves. tseitsei89 found two comms for it by hand ([24 Jun 2024](https://discord.com/channels/1007840975726575667/1077216728683135046/1254712833237844018): "8 move comm and 3 moves cancel", "8 move comm and 2 cancel.") and then checked ([24 Jun 2024](https://discord.com/channels/1007840975726575667/1077216728683135046/1254714471423676456)): "IF says those are optimal insertions."

Scramble: `R' U' F U2 F D L' B2 L2 B2 L' F2 D2 F2 L B2 F U R2 F' U2 R D2 R' U' F`

Skeleton: `F L' F' D' L2 U D L U2 F' U F U2 L' F U D L D2 R' L'` (21), leaves a corner 5-cycle: DFL → DFR → UBL → DBR → UFL → DFL

**By hand**: `U' B2 U F2 U' B2 U F2` (8-3) and `F L2 F' R' F L2 F' R` (8-2). 32 moves.

```
Solution: F L' F' D' L2 U D L U2 F' B2 U F2 U' B2 U L2 F' R' F L2 F' R U2 L' F U D L D2 R' L' (32)
```

**8 moves or less per insertion** (two comms): 32 in all.

```
F L' F' D' L2 U D L U2 ^ F' * U F U2 L' F U D L D2 R' L'
* = B2 U F2 U' B2 U F2 U' // (8-3/26)
^ = R F' L2 F R' F' L2 F // (8-2/32)
Solution: F L' F' D' L2 U D L U2 R F' L2 F R' F' L2 B2 U F2 U' B2 U F' U2 L' F U D L D2 R' L' (32)
```

**Up to 10 moves per insertion** (one alg for the whole leftover): 30 in all.

```
F L' F' D' L2 U D L U2 F' U F U2 L' F U D * L D2 R' L'
* = D2 B D2 B' R' B D2 B' D2 R // (10-1/30)
Solution: F L' F' D' L2 U D L U2 F' U F U2 L' F U D' B D2 B' R' B D2 B' D2 R L D2 R' L' (30)
```

**Up to 10 moves per insertion, a comm plus an alg**: 29 in all.

```
F L' F' * D' L2 ^ U D L U2 F' U F U2 L' F U D L D2 R' L'
* = R' U' R F2 R' U R U' F2 U // (10-0/31)
^ = L2 U' D F2 U L2 F2 L2 F2 D' // (10-12/29)
Solution: F L' F' R' U' R F2 R' U R L2 F2 L2 F2 U L U2 F' U F U2 L' F U D L D2 R' L' (29)
```

**Up to 12 moves per insertion**: nothing better with one comm, two comms or one alg.

**Up to 12 moves per insertion, a comm plus an alg**: 26 in all.

```
F * L' F' D' L2 ^ U D L U2 F' U F U2 L' F U D L D2 R' L'
* = F D F2 D' F' L' F' U' F2 U F L // (12-5/28)
^ = L2 U' D F2 U L2 F2 L2 F2 D' // (10-12/26)
Solution: F2 D F2 D' F' L' F' L2 F2 L2 F2 U L U2 F' U F U2 L' F U D L D2 R' L' (26)
```

So the two comms found by hand are the best pair of 8-movers, as Insertion Finder said. Everything shorter needs a longer alg.

### A 3c where the 8-4 is the best 8-mover and a 10-mover cancels all ten

2014chri04 ([16 Oct 2024](https://discord.com/channels/1007840975726575667/1077216728683135046/1296311051121463346)), 23 to 3C: "& = [D R D', L'] cancels 4, IF verifies that this is optimal". With time left, 2014chri04 then found by hand that a stretch of the finished solution could be replaced by something shorter, for a 22, and asked how to find such things in general.

Scramble: `R' U' F U2 F2 D2 F2 L' B2 L D2 B2 L B2 R U' L' D' B D2 U' L R B' R' U' F`

Skeleton: `U' L2 B2 U' L F D' L2 D' F' D F2 B D2 F' B' L' D L D' B D B'` (23), leaves a corner 3-cycle: DBL → UBL → DFR → DBL

**By hand**: `D R D' L' D R' D' L` (8-4). 27 moves.

```
Solution: U' L2 B2 U' L F D' L2 D' F' D F2 B D2 F' B' D R D' L' D R' L D' B D B' (27)
```

**8 moves or less per insertion** (one comm): 27 in all.

```
U' L2 B2 U' L F D' L2 D' F' D F2 B D2 F' B' L' D * L D' B D B'
* = D' L D R D' L' D R' // (8-4/27)
Solution: U' L2 B2 U' L F D' L2 D' F' D F2 B D2 F' B' D R D' L' D R' L D' B D B' (27)
```

**Up to 10 moves per insertion** (one comm): 23 in all.

```
U' L2 B2 U' L F D' L2 D' F' D F2 B D2 F' B' L' D L D' * B D B'
* = D L' D' L F L' D L D' F' // (10-10/23)
Solution: U' L2 B2 U' L F D' L2 D' F' D F2 B D2 B' L' D L D' F' B D B' (23)
```

**Up to 12 moves per insertion**: nothing better with one comm, two comms or one alg.

**Up to 12 moves per insertion, a comm plus an alg**: 22 in all.

```
U' L2 B2 U' L F D' L2 D' F' D F2 B * D2 F' B' L' ^ D L D' B D B'
* = R D R' B' U D2 L' D' L U' B D2 // (12-4/31)
^ = L F U L' D L U' D' F' D L' D' // (12-21/22)
Solution: U' L2 B2 U' L F D' L2 D' F' D F2 B R D R' B' D F' B D B' (22)
```

The 8-4 is the best 8-mover. One 10-move comm at another spot cancels all ten of its moves. The last line is the length 2014chri04 reached by hand: a comm plus an alg wrapped around a stretch of the skeleton is the same thing as replacing that stretch, because the two algs and the moves between them cancel into something shorter.

### The 3C1T that Insertion Finder was given twice

alkamaass's 16-move skeleton ([4 Dec 2023](https://discord.com/channels/1007840975726575667/1007841273111117924/1181359859896164432)), which is alkamaass's 18-move skeleton after an 8-move comm that cancels 10 (write-up, section 9.5). Insertion Finder with every alg set on and greedy 6 gives 25 ([4 Dec 2023](https://discord.com/channels/1007840975726575667/1007841273111117924/1181359940737171587)).

Scramble: `R' U' F U2 L2 F2 D' R2 B2 L2 D' F2 L U' L' F R' F2 R' F L2 U F R' U' F`

Skeleton: `D B2 D2 R2 D B L' D' R' L B' L F2 B2 L U` (16), leaves a twisted corner 3-cycle and one twisted corner: UBL → DFR → UBR → UBL, DBR twisted clockwise

**By Insertion Finder**: `F D B2 D' F' D B2 D'` (8-5) and `L2 F2 B2 R2 U R2 F2 B2 L2 D` (10-4). 25 moves.

```
Solution: F D B2 D' F' D' R2 D B L F2 B2 R2 U R2 F2 B2 R' L' B' L F2 B2 L U (25)
```

**8 moves or less per insertion** (two comms): 27 in all.

```
D B2 D2 R2 * D B L' D' R' L B' L F2 B2 L U
* = R' U R D2 R' U' R D2 // (8-2/22)
D B2 D2 R U R D2 R' U' ^ R D' B L' D' R' L B' L F2 B2 L U
^ = U L' U' R' U L U' R // (8-3/27)
Solution: D B2 D2 R U R D2 R' L' U' R' U L U' R2 D' B L' D' R' L B' L F2 B2 L U (27)
```

**Up to 10 moves per insertion**: nothing better with one comm, two comms or one alg.

**Up to 10 moves per insertion, a comm plus an alg**: 25 in all.

```
^ D B2 D2 R2 D B L' * D' R' L B' L F2 B2 L U
* = L2 F2 B2 R2 U L2 F2 B2 R2 D // (10-4/22)
^ = F D B2 D' F' D B2 D' // (8-5/25)
Solution: F D B2 D' F' D' R2 D B L F2 B2 R2 U L2 F2 B2 R L B' L F2 B2 L U (25)
```

**Up to 12 moves per insertion**: nothing better with one comm, two comms or one alg.

**Up to 12 moves per insertion, a comm plus an alg**: 24 in all.

```
D B2 D2 R2 ^ D B * L' D' R' L B' L F2 B2 L U
* = R U2 R' L' D' R L U2 R' L' D L // (12-7/21)
^ = R2 D2 B2 D' F D B2 D' F' D' R2 // (11-8/24)
Solution: F D B2 D' F' D' R2 D B R U2 R' L' D' R L U2 R2 B' L F2 B2 L U (24)
```

Insertion Finder's result is the comm-plus-alg line at 10 moves. With every alg of up to 12 moves there is one move less.

### A 3e with a 10-9

DougCube ([22 Apr 2026](https://discord.com/channels/1007840975726575667/1077216728683135046/1496695239908397127)), 18 moves to three edges. The solve starts with "EO on LR-axis", and a later step is commented "but breaks EO": the three edges that are left are oriented on none of the three axes. Then: "insert 3e comm (10-9/19)". jisu101 ([23 Apr 2026](https://discord.com/channels/1007840975726575667/1077216728683135046/1496735435039445054)): "10-9 is also crazy ngl".

Scramble: `D F L' U L2 B2 U L B' L' U' L2 B2 L2 D' B2`

Skeleton: `D L' U' L2 F2 D2 F2 L' F' L B D2 B' D L' D' L D2` (18), leaves an edge 3-cycle: DL → DR → BL → DL

**By hand**: `D2 B' L' F' R' D2 R F L B` (10-9). 19 moves.

```
Solution: D L' U' L2 F2 D2 F2 L' F2 R' D2 R F L D L' D' L D2 (19)
```

**8 moves or less per insertion** (one comm): 26 in all.

```
D L' U' L2 F2 D2 F2 L' F' L B D2 B' D L' * D' L D2
* = U2 R2 B' D2 R2 U2 F' L2 // (8-0/26)
Solution: D L' U' L2 F2 D2 F2 L' F' L B D2 B' D L' U2 R2 B' D2 R2 U2 F' L2 D' L D2 (26)
```

**8 moves or less per insertion, a comm plus an alg**: 24 in all.

```
D L' U' L2 F2 D2 F2 ^ L' F' L * B D2 B' D L' D' L D2
* = B' D2 B2 D2 B2 D2 B' // (7-5/20)
^ = F2 D2 R' L B2 R L' F2 // (8-4/24)
Solution: D L' U' L2 F2 R' L B2 R L' F2 L' F' L B' D2 B2 D2 B D L' D' L D2 (24)
```

**Up to 10 moves per insertion** (one comm): 19 in all.

```
D L' U' L2 F2 D2 F2 L' F' L B D2 B' * D L' D' L D2
* = B D2 B' L' F' R' D2 R F L // (10-9/19)
Solution: D L' U' L2 F2 D2 F2 L' F2 R' D2 R F L D L' D' L D2 (19)
```

**Up to 12 moves per insertion**: nothing better with one comm, two comms or one alg.

The 10-9 is the best single alg of up to 12 moves, and a comm plus an alg of up to 10 moves each does no better. A comm plus an alg of up to 12 moves each was not searched to the end on this skeleton. With algs of 8 moves or fewer the best is far behind.


## 200 skeletons to play along with

For each kind of leftover, 20 skeletons of 16 to 22 moves. They are random move sequences, not solves: each move is drawn at random (no two in a row on one face), and the leftover is drawn at random among all leftovers of that kind. So there are no blocks to spot, only the insertion to find, and none of them is picked by how it comes out. The scramble is made to fit: the skeleton solves it up to that leftover.

### How to read them

- **Left**: what the skeleton leaves. `A → B` means the piece now at A belongs at B; `A ↔ B` is a swap. A piece that sits in its place but turned is listed as twisted (clockwise or counter-clockwise, looking at the corner) or flipped.
- **The answer** has two parts. *8 moves or less per insertion* is the best there is with pure 8-move comms (and, for edges, the 6- and 7-movers). *Up to 10 moves per insertion* also allows every 9- and 10-move alg, including one alg that does the whole leftover where such an alg exists. Each is the true minimum over every position and every alg of that length, with two insertions allowed to sit inside each other.
- **Marks.** `*` is the first insertion and `^` the second. When the second one goes into moves that the first one changed, the skeleton is written out again as it stands after the first, with `^` in it.
- `// (8-3/22)` is the usual note: an 8-move alg, 3 moves cancel, 22 moves so far.
- When the answer says "nothing better" for 10 moves, the 8-move answer is still the best one.

### 3c

A corner 3-cycle.

#### 3c, skeleton 1

Scramble: `R' U' F R2 B2 R2 B R2 U2 F2 U2 F L2 U2 F2 D2 L' D2 B' D' L2 D' R' F' L D' R' U' F`

Skeleton: `D2 L F2 B R2 U' R' F R2 U' B' U F U' D' F'` (16)

Left: DBL → UBL → DFL → DBL

<details>
<summary>Answer for 3c, skeleton 1</summary>

**8 moves or less per insertion** (one comm): +7, 23 in all.

```
D2 L F2 * B R2 U' R' F R2 U' B' U F U' D' F'
* = F L2 F' R' F L2 F' R // (8-1/23)
Solution: D2 L F' L2 F' R' F L2 F' R B R2 U' R' F R2 U' B' U F U' D' F' (23)
```

**Up to 10 moves per insertion** (one comm): +6, 22 in all.

```
D2 L F2 B R2 U' R' F R2 U' B' U F U' D' F' *
* = F D F' L2 F D' F' D L2 D' // (10-4/22)
Solution: D2 L F2 B R2 U' R' F R2 U' B' U F U' F' L2 F D' F' D L2 D' (22)
```

</details>

#### 3c, skeleton 2

Scramble: `R' U' F L2 F D2 L2 D2 B2 L2 B' U2 F' R2 U' L' U R' D' L D B2 F2 U' R' U' F`

Skeleton: `D R2 F' B' U' L B' U2 D' F D2 L B U2 L D' F` (17)

Left: DBL → DFL → UBL → DBL

<details>
<summary>Answer for 3c, skeleton 2</summary>

**8 moves or less per insertion** (one comm): +7, 24 in all.

```
D R2 F' B' U' L B' U2 * D' F D2 L B U2 L D' F
* = U L2 U' R2 U L2 U' R2 // (8-1/24)
Solution: D R2 F' B' U' L B' U' L2 U' R2 U L2 U' R2 D' F D2 L B U2 L D' F (24)
```

**Up to 10 moves per insertion**: nothing better, 24 stays the best.

</details>

#### 3c, skeleton 3

Scramble: `R' U' F R2 D U' F2 D' R2 U L2 B2 F2 R2 U' R' B' F2 U F' L' D L' D' U' R' U' F`

Skeleton: `D2 F' B U' R B2 L F' R2 U2 B' U' R B D B U F'` (18)

Left: UFL → DBR → UBR → UFL

<details>
<summary>Answer for 3c, skeleton 3</summary>

**8 moves or less per insertion** (one comm): +5, 23 in all.

```
D2 F' B U' R B2 L F' * R2 U2 B' U' R B D B U F'
* = F R B' R' F' R B R' // (8-3/23)
Solution: D2 F' B U' R B2 R L B' R' F' R B R U2 B' U' R B D B U F' (23)
```

**Up to 10 moves per insertion**: nothing better, 23 stays the best.

</details>

#### 3c, skeleton 4

Scramble: `R' U' F L2 R2 U' L2 U' B2 D2 L2 B2 D L2 B' U R D F L2 D U2 L' F R' U' F`

Skeleton: `B L B2 L U' F2 B' U2 F2 D' R B D B2 R D F U D2` (19)

Left: UBL → DBR → UBR → UBL

<details>
<summary>Answer for 3c, skeleton 4</summary>

**8 moves or less per insertion** (one comm): +6, 25 in all.

```
B * L B2 L U' F2 B' U2 F2 D' R B D B2 R D F U D2
* = B L' F L B' L' F' L // (8-2/25)
Solution: B2 L' F L B' L' F' L2 B2 L U' F2 B' U2 F2 D' R B D B2 R D F U D2 (25)
```

**Up to 10 moves per insertion**: nothing better, 25 stays the best.

</details>

#### 3c, skeleton 5

Scramble: `R' U' F U B2 R2 U' R2 D B2 F2 D2 L2 U L F R D L B' R' D2 F' D' R' U' F`

Skeleton: `B2 D2 F' R2 D2 B L U2 R U' D2 B2 D2 R B U F' B2 R' F` (20)

Left: DFL → UBL → DFR → DFL

<details>
<summary>Answer for 3c, skeleton 5</summary>

**8 moves or less per insertion** (one comm): +7, 27 in all.

```
B2 D2 F' R2 D2 B L U2 R U' D2 B2 D2 R B U F' * B2 R' F
* = F' L2 F R2 F' L2 F R2 // (8-1/27)
Solution: B2 D2 F' R2 D2 B L U2 R U' D2 B2 D2 R B U F2 L2 F R2 F' L2 F R2 B2 R' F (27)
```

**Up to 10 moves per insertion**: nothing better, 27 stays the best.

</details>

#### 3c, skeleton 6

Scramble: `R' U' F L2 B2 F' R2 D2 F U2 L2 U2 B2 R2 U F2 U' L' B U R D' L F' R' U' F`

Skeleton: `U B U L U' L2 B U' D R U2 F2 D' B R2 U F' R2 L2 D B` (21)

Left: DBR → UFR → UBR → DBR

<details>
<summary>Answer for 3c, skeleton 6</summary>

**8 moves or less per insertion** (one comm): +6, 27 in all.

```
U B U L U' L2 B U' D R U2 F2 D' B * R2 U F' R2 L2 D B
* = B L B' R B L' B' R' // (8-2/27)
Solution: U B U L U' L2 B U' D R U2 F2 D' B2 L B' R B L' B' R U F' R2 L2 D B (27)
```

**Up to 10 moves per insertion**: nothing better, 27 stays the best.

</details>

#### 3c, skeleton 7

Scramble: `R' U' F R2 B' F' R2 D2 F2 R2 B' L2 R2 U2 L' D' L2 B' F' R D2 B' U F2 R' U' F`

Skeleton: `U2 R F B2 U D2 F2 D B' U' R' D R2 F' U2 L' F' R2 F' L2 F' B` (22)

Left: DFL → DBR → UFL → DFL

<details>
<summary>Answer for 3c, skeleton 7</summary>

**8 moves or less per insertion** (one comm): +7, 29 in all.

```
U2 R F B2 U D2 F2 D B' U' R' D R2 F' U2 L' F' R2 F' L2 F' * B
* = F' L B L' F L B' L' // (8-1/29)
Solution: U2 R F B2 U D2 F2 D B' U' R' D R2 F' U2 L' F' R2 F' L2 F2 L B L' F L B' L' B (29)
```

**Up to 10 moves per insertion**: nothing better, 29 stays the best.

</details>

#### 3c, skeleton 8

Scramble: `R' U' F U' D L2 R2 D F2 R2 D L2 B2 D B2 D' U2 R' B L' F2 D U2 B2 L U R' U' F`

Skeleton: `L' F' R2 D B2 D2 B' R B2 L2 B2 L U B2 U2 D'` (16)

Left: DBL → DBR → UBL → DBL

<details>
<summary>Answer for 3c, skeleton 8</summary>

**8 moves or less per insertion** (one comm): +6, 22 in all.

```
L' F' R2 D B2 D2 B' * R B2 L2 B2 L U B2 U2 D'
* = B R2 B' L2 B R2 B' L2 // (8-2/22)
Solution: L' F' R2 D B2 D2 R2 B' L2 B R2 B' R L2 B2 L2 B2 L U B2 U2 D' (22)
```

**Up to 10 moves per insertion**: nothing better, 22 stays the best.

</details>

#### 3c, skeleton 9

Scramble: `R' U' F B' D2 B2 R2 B D2 F' L2 B D2 F' D2 R' U L2 U B F U2 B' R' U' F`

Skeleton: `D2 F2 B' R2 B' U L' U' F B' R F' U F2 L F2 L2` (17)

Left: DBL → DBR → DFR → DBL

<details>
<summary>Answer for 3c, skeleton 9</summary>

**8 moves or less per insertion** (one comm): +6, 23 in all.

```
D2 F2 B' R2 B' U L' U' F B' R F' U F2 L F2 * L2
* = F2 U B2 U' F2 U B2 U' // (8-2/23)
Solution: D2 F2 B' R2 B' U L' U' F B' R F' U F2 L U B2 U' F2 U B2 U' L2 (23)
```

**Up to 10 moves per insertion**: nothing better, 23 stays the best.

</details>

#### 3c, skeleton 10

Scramble: `R' U' F L2 F2 U L2 R2 D F2 D F2 D L2 D' L2 B L2 R' B' R' U' R D B' F R' U' F`

Skeleton: `B D2 R L U L B2 L2 D B D2 B2 D2 B U L U' F'` (18)

Left: UBL → DFR → UFR → UBL

<details>
<summary>Answer for 3c, skeleton 10</summary>

**8 moves or less per insertion** (one comm): +6, 24 in all.

```
B D2 R L U L B2 L2 D B D2 B2 * D2 B U L U' F'
* = B2 R' F' R B2 R' F R // (8-2/24)
Solution: B D2 R L U L B2 L2 D B D2 R' F' R B2 R' F R D2 B U L U' F' (24)
```

**Up to 10 moves per insertion**: nothing better, 24 stays the best.

</details>

#### 3c, skeleton 11

Scramble: `R' U' F R2 U2 F2 D2 U2 R2 B D2 U2 B D' B F2 D2 L D B2 R F2 R' U' F`

Skeleton: `D2 F' B' L2 B R2 L' U F L2 U2 L2 U' D F L2 B' R2 L` (19)

Left: DFL → DBR → DFR → DFL

<details>
<summary>Answer for 3c, skeleton 11</summary>

**8 moves or less per insertion** (one comm): +5, 24 in all.

```
D2 F' B' L2 B R2 L' U * F L2 U2 L2 U' D F L2 B' R2 L
* = U' F' D2 F U F' D2 F // (8-3/24)
Solution: D2 F' B' L2 B R2 L' F' D2 F U F' D2 F2 L2 U2 L2 U' D F L2 B' R2 L (24)
```

**Up to 10 moves per insertion**: nothing better, 24 stays the best.

</details>

#### 3c, skeleton 12

Scramble: `R' U' F D2 L2 U' R2 F2 D B2 U B2 D2 F2 L F2 U' R D L' U B' L' F' U' R' U' F`

Skeleton: `R' L2 B U D2 R U F2 B2 U2 B2 D2 B2 D' F2 D R U F' U'` (20)

Left: UBL → UBR → UFL → UBL

<details>
<summary>Answer for 3c, skeleton 12</summary>

**8 moves or less per insertion** (one comm): +6, 26 in all.

```
R' L2 B U D2 R U * F2 B2 U2 B2 D2 B2 D' F2 D R U F' U'
* = U2 F D2 F' U2 F D2 F' // (8-2/26)
Solution: R' L2 B U D2 R U' F D2 F' U2 F D2 F B2 U2 B2 D2 B2 D' F2 D R U F' U' (26)
```

**Up to 10 moves per insertion**: nothing better, 26 stays the best.

</details>

#### 3c, skeleton 13

Scramble: `R' U' F R F2 U2 L U2 R D2 U2 B2 F2 L' U2 L2 U' B' D' U L2 F2 U2 B' R' U' F`

Skeleton: `U' B2 L U R' F2 R' B2 R2 B' U' L' B' L2 F2 L2 F' U F U R2` (21)

Left: DFL → DFR → DBR → DFL

<details>
<summary>Answer for 3c, skeleton 13</summary>

**8 moves or less per insertion** (one comm): +6, 27 in all.

```
U' B2 L U R' F2 R' B2 R2 * B' U' L' B' L2 F2 L2 F' U F U R2
* = R F2 R' B2 R F2 R' B2 // (8-2/27)
Solution: U' B2 L U R' F2 R' B2 R' F2 R' B2 R F2 R' B U' L' B' L2 F2 L2 F' U F U R2 (27)
```

**Up to 10 moves per insertion**: nothing better, 27 stays the best.

</details>

#### 3c, skeleton 14

Scramble: `R' U' F U' L2 D' L2 B2 U L2 B2 D F2 D2 F2 D B' L' U' B D R2 F' U' F R' U' F`

Skeleton: `L F' R F' B D' R F2 B' R' B L' U2 F R2 B L2 D' R' D F' D2` (22)

Left: DBR → UFR → DFR → DBR

<details>
<summary>Answer for 3c, skeleton 14</summary>

**8 moves or less per insertion** (one comm): +4, 26 in all.

```
L F' R F' B D' R F2 B' R' * B L' U2 F R2 B L2 D' R' D F' D2
* = R B R' F2 R B' R' F2 // (8-4/26)
Solution: L F' R F' B D' R F2 R' F2 R B' R' F2 B L' U2 F R2 B L2 D' R' D F' D2 (26)
```

**Up to 10 moves per insertion**: nothing better, 26 stays the best.

</details>

#### 3c, skeleton 15

Scramble: `R' U' F B2 R2 U2 B D2 F2 R2 F2 U2 L2 F' R2 D' L' D2 R2 U2 F L2 B2 U2 R' U' F`

Skeleton: `R' B' R' D2 R2 B D2 B L U' B2 R B2 D2 B' U2` (16)

Left: UFL → DBR → UBR → UFL

<details>
<summary>Answer for 3c, skeleton 15</summary>

**8 moves or less per insertion** (one comm): +6, 22 in all.

```
R' B' R' D2 R2 B D2 B * L U' B2 R B2 D2 B' U2
* = B' U2 B D' B' U2 B D // (8-2/22)
Solution: R' B' R' D2 R2 B U2 D2 B D' B' U2 B D L U' B2 R B2 D2 B' U2 (22)
```

**Up to 10 moves per insertion**: nothing better, 22 stays the best.

</details>

#### 3c, skeleton 16

Scramble: `R' U' F R2 F2 U2 R U2 F2 R B2 R F2 R D B2 D' B' R' B2 L2 D' B L' R' U' F`

Skeleton: `R' F2 R D' B2 L' U' R D2 R2 U2 B' R' B2 U2 B U2` (17)

Left: DFL → UBR → DFR → DFL

<details>
<summary>Answer for 3c, skeleton 16</summary>

**8 moves or less per insertion** (one comm): +7, 24 in all.

```
R' F2 R D' B2 L' U' R D2 R2 U2 B' R' * B2 U2 B U2
* = L B R' B' L' B R B' // (8-1/24)
Solution: R' F2 R D' B2 L' U' R D2 R2 U2 B' R' L B R' B' L' B R B U2 B U2 (24)
```

**Up to 10 moves per insertion**: nothing better, 24 stays the best.

</details>

#### 3c, skeleton 17

Scramble: `R' U' F B2 L2 D2 B' R2 F2 D2 B R2 B' L2 B' L' U2 R2 U' R' D' L' D B2 U' R' U' F`

Skeleton: `B2 D B2 U2 R F2 L' U' L2 U2 L2 B2 D2 L' F' B2 L' B2` (18)

Left: UBL → DFR → UBR → UBL

<details>
<summary>Answer for 3c, skeleton 17</summary>

**8 moves or less per insertion** (one comm): +6, 24 in all.

```
B2 D B2 U2 R F2 L' U' L2 U2 L2 B2 D2 L' F' B2 L' * B2
* = L' F L B' L' F' L B // (8-2/24)
Solution: B2 D B2 U2 R F2 L' U' L2 U2 L2 B2 D2 L' F' B2 L2 F L B' L' F' L B' (24)
```

**Up to 10 moves per insertion**: nothing better, 24 stays the best.

</details>

#### 3c, skeleton 18

Scramble: `R' U' F L2 B2 U B2 D L2 D' L2 D B2 U L' F L' D' U2 B L R2 D2 B2 U' R' U' F`

Skeleton: `D R2 U' B L' B' D' L2 B' U F' R' L2 B D2 F L' U2 R'` (19)

Left: DFR → UFR → UBR → DFR

<details>
<summary>Answer for 3c, skeleton 18</summary>

**8 moves or less per insertion** (one comm): +7, 26 in all.

```
D R2 U' B L' B' D' * L2 B' U F' R' L2 B D2 F L' U2 R'
* = D' B' D F2 D' B D F2 // (8-1/26)
Solution: D R2 U' B L' B' D2 B' D F2 D' B D F2 L2 B' U F' R' L2 B D2 F L' U2 R' (26)
```

**Up to 10 moves per insertion**: nothing better, 26 stays the best.

</details>

#### 3c, skeleton 19

Scramble: `R' U' F L U2 B2 R U2 R' F2 D2 R' D2 B2 R' F2 L U B L' F2 R' D' F2 L B' R' U' F`

Skeleton: `U2 R' F2 R' F2 U' B2 R D2 B R' F' L' B U' F' B2 R2 B L` (20)

Left: DBL → DBR → DFL → DBL

<details>
<summary>Answer for 3c, skeleton 19</summary>

**8 moves or less per insertion** (one comm): +6, 26 in all.

```
U2 R' F2 R' F2 U' * B2 R D2 B R' F' L' B U' F' B2 R2 B L
* = U L' D2 L U' L' D2 L // (8-2/26)
Solution: U2 R' F2 R' F2 L' D2 L U' L' D2 L B2 R D2 B R' F' L' B U' F' B2 R2 B L (26)
```

**Up to 10 moves per insertion**: nothing better, 26 stays the best.

</details>

#### 3c, skeleton 20

Scramble: `R' U' F D2 B R2 F' D2 F' U2 F R2 B2 D2 L D' B2 L D L F D F2 R' U' F`

Skeleton: `R L' F2 U R' D F' U' F2 R' U B U' F2 B2 D B2 D2 F B2 U2` (21)

Left: DBL → DBR → UFL → DBL

<details>
<summary>Answer for 3c, skeleton 20</summary>

**8 moves or less per insertion** (one comm): +5, 26 in all.

```
R L' F2 U * R' D F' U' F2 R' U B U' F2 B2 D B2 D2 F B2 U2
* = U' F U B2 U' F' U B2 // (8-3/26)
Solution: R L' F' U B2 U' F' U B2 R' D F' U' F2 R' U B U' F2 B2 D B2 D2 F B2 U2 (26)
```

**Up to 10 moves per insertion**: nothing better, 26 stays the best.

</details>

### 5c

A corner 5-cycle.

#### 5c, skeleton 1

Scramble: `R' U' F U' L2 U' L2 F2 U L2 D B2 U' F2 U R B' L D R2 B U' R D2 U' R' U' F`

Skeleton: `D2 L F2 B R2 U' R' F R2 U' B' U F U' D' F'` (16)

Left: DFL → UFR → UBL → DBR → UFL → DFL

<details>
<summary>Answer for 5c, skeleton 1</summary>

**8 moves or less per insertion** (two comms): +10, 26 in all.

```
D2 L F2 B R2 * U' R' F R2 U' B' U F U' D' F'
* = L' D' L U L' D L U' // (8-1/23)
D2 L F2 B R2 L' D' ^ L U L' D L U2 R' F R2 U' B' U F U' D' F'
^ = D R2 D' L2 D R2 D' L2 // (8-5/26)
Solution: D2 L F2 B L' D' L2 D R2 D' L' U L' D L U2 R' F R2 U' B' U F U' D' F' (26)
```

**Up to 10 moves per insertion**: nothing better, 26 stays the best.

</details>

#### 5c, skeleton 2

Scramble: `R' U' F U' R2 F' R2 D2 U2 F' U2 F R2 B' L2 U2 F' D F D2 L U R2 B R U' R' U' F`

Skeleton: `D R2 F' B' U' L B' U2 D' F D2 L B U2 L D' F` (17)

Left: DBL → UBR → DFL → UBL → UFR → DBL

<details>
<summary>Answer for 5c, skeleton 2</summary>

**8 moves or less per insertion** (two comms): +12, 29 in all.

```
D R2 F' B' U' L B' U2 D' F D2 L B U2 L D' * F
* = R2 F L' F' R2 F L F' // (8-2/23)
D R2 F' B' U' L B' U2 D' F D2 L B U2 L D' R2 F L' F' R2 F L ^
^ = L' D' L U2 L' D L U2 // (8-2/29)
Solution: D R2 F' B' U' L B' U2 D' F D2 L B U2 L D' R2 F L' F' R2 F D' L U2 L' D L U2 (29)
```

**Up to 10 moves per insertion**: nothing better, 29 stays the best.

</details>

#### 5c, skeleton 3

Scramble: `R' U' F D' B2 F2 R2 U' R2 D B2 D2 U L2 F' L2 D' R U' B F U' L R' U' F`

Skeleton: `D2 F' B U' R B2 L F' R2 U2 B' U' R B D B U F'` (18)

Left: DBL → UBL → UBR → UFR → DFR → DBL

<details>
<summary>Answer for 5c, skeleton 3</summary>

**8 moves or less per insertion** (two comms): +11, 29 in all.

```
D2 F' B U' R B2 * L ^ F' R2 U2 B' U' R B D B U F'
* = U B' U' F U B U' F' // (8-0/26)
^ = L' F R2 F' L F R2 F' // (8-5/29)
Solution: D2 F' B U' R B2 U B' U' F U B U' R2 F' L F R2 F2 R2 U2 B' U' R B D B U F' (29)
```

**Up to 10 moves per insertion**: nothing better, 29 stays the best.

</details>

#### 5c, skeleton 4

Scramble: `R' U' F U2 F2 L' F2 L2 D2 U2 F2 L2 D2 R' U R B F D' R U' B F R' U' F`

Skeleton: `B L B2 L U' F2 B' U2 F2 D' R B D B2 R D F U D2` (19)

Left: DFL → UBL → DFR → DBR → UFR → DFL

<details>
<summary>Answer for 5c, skeleton 4</summary>

**8 moves or less per insertion** (two comms): +11, 30 in all.

```
B L B2 L U' F2 B' U2 F2 ^ D' R B D B2 R D * F U D2
* = D2 F U2 F' D2 F U2 F' // (8-4/23)
^ = F' R2 F L2 F' R2 F L2 // (8-1/30)
Solution: B L B2 L U' F2 B' U2 F R2 F L2 F' R2 F L2 D' R B D B2 R D' F U2 F' D2 F U' D2 (30)
```

**Up to 10 moves per insertion**: nothing better, 30 stays the best.

</details>

#### 5c, skeleton 5

Scramble: `R' U' F U' R2 D R2 U' F2 D R2 B2 F2 D L R2 B' D' R' U L B2 L' B F2 R' U' F`

Skeleton: `B2 D2 F' R2 D2 B L U2 R U' D2 B2 D2 R B U F' B2 R' F` (20)

Left: DBL → DFL → UBR → DBR → UFR → DBL

<details>
<summary>Answer for 5c, skeleton 5</summary>

**8 moves or less per insertion** (two comms): +9, 29 in all.

```
B2 ^ D2 F' R2 D2 B L U2 R U' D2 B2 D2 * R B U F' B2 R' F
* = B L2 B' R B L2 B' R' // (8-4/24)
^ = B U2 B' D2 B U2 B' D2 // (8-3/29)
Solution: B' U2 B' D2 B U2 F' B' R2 D2 B L U2 R U' D2 B2 D2 B L2 B' R B L2 U F' B2 R' F (29)
```

**Up to 10 moves per insertion**: nothing better, 29 stays the best.

</details>

#### 5c, skeleton 6

Scramble: `R' U' F R U2 L' F2 D2 R' U2 F2 R' B2 R2 U2 R U B' L2 U2 L D2 B' F2 L' D R' U' F`

Skeleton: `U B U L U' L2 B U' D R U2 F2 D' B R2 U F' R2 L2 D B` (21)

Left: DFL → UFL → DBR → DFR → UBL → DFL

<details>
<summary>Answer for 5c, skeleton 6</summary>

**8 moves or less per insertion** (two comms): +12, 33 in all.

```
U B U L U' L2 B U' D R U2 F2 D' B R2 U F' R2 L2 * D B
* = L' D R2 D' L D R2 D' // (8-3/26)
U B U L U' L2 B U' D R U2 F2 D' B R2 U F' R2 L D R2 D' L D ^ R2 B
^ = B2 R' F R B2 R' F' R // (8-1/33)
Solution: U B U L U' L2 B U' D R U2 F2 D' B R2 U F' R2 L D R2 D' L D B2 R' F R B2 R' F' R' B (33)
```

**Up to 10 moves per insertion** (two comms): +11, 32 in all.

```
U B U * L U' L2 B U' D R U2 F2 D' B R2 U F' R2 L2 D B
* = D' L' D B2 D' L D L' B2 L // (10-1/30)
U B U D' L' D B2 D' L D L' B2 ^ L2 U' L2 B U' D R U2 F2 D' B R2 U F' R2 L2 D B
^ = B2 L D' L' U2 L D L' U2 B2 // (10-8/32)
Solution: U B U D' L' D B2 U2 D' L D L' U2 B2 L2 U' L2 B U' D R U2 F2 D' B R2 U F' R2 L2 D B (32)
```

</details>

#### 5c, skeleton 7

Scramble: `R' U' F D2 B2 F2 U' F2 D2 U L2 U R2 B2 U F L' F' D' F R' D R2 U2 F R' U' F`

Skeleton: `U2 R F B2 U D2 F2 D B' U' R' D R2 F' U2 L' F' R2 F' L2 F' B` (22)

Left: DBL → UFR → DFL → DFR → DBR → DBL

<details>
<summary>Answer for 5c, skeleton 7</summary>

**8 moves or less per insertion** (two comms): +11, 33 in all.

```
U2 R F B2 U D2 * F2 D B' U' R' D R2 F' U2 L' F' R2 F' L2 F' B
* = U' F U B2 U' F' U B2 // (8-2/28)
U2 R F B2 ^ D2 F U B2 U' F' U F2 B2 D B' U' R' D R2 F' U2 L' F' R2 F' L2 F' B
^ = F' U2 F D F' U2 F D' // (8-3/33)
Solution: U2 R B2 U2 F D F' U2 F D F U B2 U' F' U F2 B2 D B' U' R' D R2 F' U2 L' F' R2 F' L2 F' B (33)
```

**Up to 10 moves per insertion**: nothing better, 33 stays the best.

</details>

#### 5c, skeleton 8

Scramble: `R' U' F D' R2 B2 L2 R2 D2 L2 F2 D2 U' R B2 U' R2 U' B R' U' R2 D2 R' U' F`

Skeleton: `L' F' R2 D B2 D2 B' R B2 L2 B2 L U B2 U2 D'` (16)

Left: DBL → DBR → UBL → DFL → UBR → DBL

<details>
<summary>Answer for 5c, skeleton 8</summary>

**8 moves or less per insertion** (two comms): +9, 25 in all.

```
L' F' R2 D B2 D2 B' R B2 L2 B2 L * U B2 U2 D'
* = L2 U R U' L2 U R' U' // (8-3/21)
L' F' R2 D B2 D2 B' R B2 L2 B2 L' U R ^ U' L2 U R' B2 U2 D'
^ = R' U L U' R U L' U' // (8-4/25)
Solution: L' F' R2 D B2 D2 B' R B2 L2 B2 L' U2 L U' R U L' U2 L2 U R' B2 U2 D' (25)
```

**Up to 10 moves per insertion**: nothing better, 25 stays the best.

</details>

#### 5c, skeleton 9

Scramble: `R' U' F B L2 B U2 F' L2 B' L2 F R2 D2 B2 R' B' D L D' B' L' F' R' U' F`

Skeleton: `D2 F2 B' R2 B' U L' U' F B' R F' U F2 L F2 L2` (17)

Left: UBL → UFR → UBR → DFR → UFL → UBL

<details>
<summary>Answer for 5c, skeleton 9</summary>

**8 moves or less per insertion** (two comms): +12, 29 in all.

```
D2 F2 * B' R2 B' U L' U' F B' R F' U F2 L F2 L2
* = R' U L' U' R U L U' // (8-0/25)
D2 F2 R' U L' ^ U' R U L U' B' R2 B' U L' U' F B' R F' U F2 L F2 L2
^ = L U' L' D2 L U L' D2 // (8-4/29)
Solution: D2 F2 R' L' D2 L U L' U' D2 R U L U' B' R2 B' U L' U' F B' R F' U F2 L F2 L2 (29)
```

**Up to 10 moves per insertion**: nothing better, 29 stays the best.

</details>

#### 5c, skeleton 10

Scramble: `R' U' F R2 B2 L D2 B2 L B2 L' D2 R U2 R D2 U2 F U' L' D' B L F L' F' R' U' F`

Skeleton: `B D2 R L U L B2 L2 D B D2 B2 D2 B U L U' F'` (18)

Left: DFL → DFR → UFR → UBL → UFL → DFL

<details>
<summary>Answer for 5c, skeleton 10</summary>

**8 moves or less per insertion** (two comms): +12, 30 in all.

```
B D2 ^ R L U L * B2 L2 D B D2 B2 D2 B U L U' F'
* = L D' L' U L D L' U' // (8-1/25)
^ = D L D' R D L' D' R' // (8-3/30)
Solution: B D' L D' R D L' D' L U L2 D' L' U L D L' U' B2 L2 D B D2 B2 D2 B U L U' F' (30)
```

**Up to 10 moves per insertion**: nothing better, 30 stays the best.

</details>

#### 5c, skeleton 11

Scramble: `R' U' F U B2 R2 U F2 U2 L2 B2 U F2 R D' F L2 U' L F2 U2 L2 U' R' U' F`

Skeleton: `D2 F' B' L2 B R2 L' U F L2 U2 L2 U' D F L2 B' R2 L` (19)

Left: UBL → UFR → UFL → DBR → DFR → UBL

<details>
<summary>Answer for 5c, skeleton 11</summary>

**8 moves or less per insertion** (two comms): +11, 30 in all.

```
D2 F' B' L2 ^ B R2 L' * U F L2 U2 L2 U' D F L2 B' R2 L
* = R' D' R U R' D R U' // (8-3/24)
^ = D2 B U2 B' D2 B U2 B' // (8-2/30)
Solution: D2 F' B' L2 D2 B U2 B' D2 B U2 R L' D' R U R' D R F L2 U2 L2 U' D F L2 B' R2 L (30)
```

**Up to 10 moves per insertion**: nothing better, 30 stays the best.

</details>

#### 5c, skeleton 12

Scramble: `R' U' F B2 L U2 R' B2 D2 U2 L B2 L2 R' B2 R2 B2 D2 B' D F2 D' F U' R' B' D2 R' U' F`

Skeleton: `R' L2 B U D2 R U F2 B2 U2 B2 D2 B2 D' F2 D R U F' U'` (20)

Left: UBL → DFR → UBR → UFR → UFL → UBL

<details>
<summary>Answer for 5c, skeleton 12</summary>

**8 moves or less per insertion** (two comms): +12, 32 in all.

```
R' L2 B U D2 R U F2 B2 U2 B2 ^ D2 B2 D' F2 D R U * F' U'
* = D F' U F D' F' U' F // (8-3/25)
^ = B' U' F' U B U' F U // (8-1/32)
Solution: R' L2 B U D2 R U F2 B2 U2 B U' F' U B U' F U D2 B2 D' F2 D R U D F' U F D' F' U2 (32)
```

**Up to 10 moves per insertion**: nothing better, 32 stays the best.

</details>

#### 5c, skeleton 13

Scramble: `R' U' F U2 B2 L F2 L' U2 R D2 B2 R' D2 F2 D' R2 F U2 L2 U' B D R' U' F`

Skeleton: `U' B2 L U R' F2 R' B2 R2 B' U' L' B' L2 F2 L2 F' U F U R2` (21)

Left: DBL → UBL → UFR → UFL → DFR → DBL

<details>
<summary>Answer for 5c, skeleton 13</summary>

**8 moves or less per insertion** (two comms): +9, 30 in all.

```
U' B2 L U R' F2 R' B2 R2 B' U' L' ^ B' L2 F2 L2 F' U * F U R2
* = D F U' F' D' F U F' // (8-3/26)
^ = R B' L2 B R' B' L2 B // (8-4/30)
Solution: U' B2 L U R' F2 R' B2 R2 B' U' R L' B' L2 B R' F2 B' L2 F' U D F U' F' D' F U2 R2 (30)
```

**Up to 10 moves per insertion**: nothing better, 30 stays the best.

</details>

#### 5c, skeleton 14

Scramble: `R' U' F L2 B2 L' U2 R B2 D2 L2 F2 D2 L' D2 B D F2 D R U2 F2 D' U' R' U' F`

Skeleton: `L F' R F' B D' R F2 B' R' B L' U2 F R2 B L2 D' R' D F' D2` (22)

Left: DBL → DFR → UFR → UBR → UFL → DBL

<details>
<summary>Answer for 5c, skeleton 14</summary>

**8 moves or less per insertion** (two comms): +9, 31 in all.

```
L F' R F' B ^ D' R F2 B' R' B L' U2 F R2 * B L2 D' R' D F' D2
* = R' B L' B' R B L B' // (8-4/26)
^ = B U' B' D' B U B' D // (8-3/31)
Solution: L F' R F' B2 U' B' D' B U B' R F2 B' R' B L' U2 F R B L' B' R B L' D' R' D F' D2 (31)
```

**Up to 10 moves per insertion**: nothing better, 31 stays the best.

</details>

#### 5c, skeleton 15

Scramble: `R' U' F B R2 D2 F U2 F D2 F' D2 F D2 F' D' B2 U' F2 U R2 F2 L B' R' U' F`

Skeleton: `R' B' R' D2 R2 B D2 B L U' B2 R B2 D2 B' U2` (16)

Left: DFL → DBR → UFL → UBL → UFR → DFL

<details>
<summary>Answer for 5c, skeleton 15</summary>

**8 moves or less per insertion** (two comms): +11, 27 in all.

```
R' B' R' D2 R2 B D2 B L ^ U' * B2 R B2 D2 B' U2
* = L U' L' D L U L' D' // (8-0/24)
^ = R2 U' L U R2 U' L' U // (8-5/27)
Solution: R' B' R' D2 R2 B D2 B R2 L U' L U R2 U2 L' D L U L' D' B2 R B2 D2 B' U2 (27)
```

**Up to 10 moves per insertion**: nothing better, 27 stays the best.

</details>

#### 5c, skeleton 16

Scramble: `R' U' F D2 L2 F D2 F2 L2 D2 F D2 F' D2 B2 R' B2 L D' U' B U L2 R' U' F`

Skeleton: `R' F2 R D' B2 L' U' R D2 R2 U2 B' R' B2 U2 B U2` (17)

Left: DBL → DFL → UFL → UBL → UBR → DBL

<details>
<summary>Answer for 5c, skeleton 16</summary>

**8 moves or less per insertion** (two comms): +11, 28 in all.

```
R' F2 R D' ^ B2 L' U' * R D2 R2 U2 B' R' B2 U2 B U2
* = U' R D R' U R D' R' // (8-4/21)
^ = D' B2 D F D' B2 D F' // (8-1/28)
Solution: R' F2 R D2 B2 D F D' B2 D F' B2 L' U2 R D R' U R D R2 U2 B' R' B2 U2 B U2 (28)
```

**Up to 10 moves per insertion** (two comms): +10, 27 in all.

```
R' F2 R D' B2 L' ^ U' R D2 R2 U2 B' R' B2 U2 * B U2
* = U L2 U' B U B' L2 B U' B' // (10-4/23)
^ = U2 R D R' U R D' R' U // (9-5/27)
Solution: R' F2 R D' B2 L' U2 R D R' U R D R2 U2 B' R' B2 U' L2 U' B U B' L2 B U (27)
```

</details>

#### 5c, skeleton 17

Scramble: `R' U' F U' R2 B2 U F2 D' L2 R2 F2 U' L2 U' R2 D2 B U2 L B2 U R' F2 R' U' F`

Skeleton: `B2 D B2 U2 R F2 L' U' L2 U2 L2 B2 D2 L' F' B2 L' B2` (18)

Left: DBL → DFL → DBR → UFL → UBL → DBL

<details>
<summary>Answer for 5c, skeleton 17</summary>

**8 moves or less per insertion** (two comms): +10, 28 in all.

```
B2 D B2 U2 R F2 L' U' L2 U2 L2 B2 D2 L' * F' B2 L' B2
* = L' B' R B L B' R' B // (8-2/24)
B2 D B2 U2 R F2 L' U' L2 U2 L2 B2 D2 L2 B' R B L ^ B' R' F' B' L' B2
^ = L' B R' B' L B R B' // (8-4/28)
Solution: B2 D B2 U2 R F2 L' U' L2 U2 L2 B2 D2 L2 B' R B2 R' B' L B R B2 R' F' B' L' B2 (28)
```

**Up to 10 moves per insertion**: nothing better, 28 stays the best.

</details>

#### 5c, skeleton 18

Scramble: `R' U' F D' B2 R2 U' R2 F2 L2 R2 U F2 U' F L' D' F2 L B' D B2 F D' R' U' F`

Skeleton: `D R2 U' B L' B' D' L2 B' U F' R' L2 B D2 F L' U2 R'` (19)

Left: DBL → DBR → UFL → UBL → UBR → DBL

<details>
<summary>Answer for 5c, skeleton 18</summary>

**8 moves or less per insertion** (two comms): +10, 29 in all.

```
D R2 U' B L' B' D' L2 B' U F' R' L2 * B D2 F L' U2 R'
* = R D2 R' U2 R D2 R' U2 // (8-2/25)
D R2 U' B L' B' D' L2 B' U F' L2 D2 R' U2 R D2 R' ^ U2 B D2 F L' U2 R'
^ = R D R' U R D' R' U' // (8-4/29)
Solution: D R2 U' B L' B' D' L2 B' U F' L2 D2 R' U2 R D' R' U R D' R' U B D2 F L' U2 R' (29)
```

**Up to 10 moves per insertion**: nothing better, 29 stays the best.

</details>

#### 5c, skeleton 19

Scramble: `R' U' F U2 L2 B U2 F' R2 U2 B' D2 F' D2 L2 F' U F' U' L D2 F2 U' B2 L2 U' R' U' F`

Skeleton: `U2 R' F2 R' F2 U' B2 R D2 B R' F' L' B U' F' B2 R2 B L` (20)

Left: DBL → UBR → DBR → UFR → UFL → DBL

<details>
<summary>Answer for 5c, skeleton 19</summary>

**8 moves or less per insertion** (two comms): +9, 29 in all.

```
U2 R' ^ F2 R' F2 * U' B2 R D2 B R' F' L' B U' F' B2 R2 B L
* = F' U' B2 U F U' B2 U // (8-5/23)
^ = R2 F' L' F R2 F' L F // (8-2/29)
Solution: U2 R F' L' F R2 F' L F' R' F U' B2 U F U' R D2 B R' F' L' B U' F' B2 R2 B L (29)
```

**Up to 10 moves per insertion**: nothing better, 29 stays the best.

</details>

#### 5c, skeleton 20

Scramble: `R' U' F R2 F2 D' F2 U' F2 D' L2 D2 F2 L2 U L U2 B' F D' B2 U' B U' R' U' F`

Skeleton: `R L' F2 U R' D F' U' F2 R' U B U' F2 B2 D B2 D2 F B2 U2` (21)

Left: UFL → UFR → DBR → DFR → UBR → UFL

<details>
<summary>Answer for 5c, skeleton 20</summary>

**8 moves or less per insertion** (two comms): +11, 32 in all.

```
R L' F2 U R' D F' U' F2 R' U B ^ U' F2 B2 D B2 D2 F B2 U2 *
* = U L U' R2 U L' U' R2 // (8-1/28)
^ = B2 U' F U B2 U' F' U // (8-4/32)
Solution: R L' F2 U R' D F' U' F2 R' U B' U' F U B2 U' F B2 D B2 D2 F B2 U' L U' R2 U L' U' R2 (32)
```

**Up to 10 moves per insertion** (one alg for the whole leftover): +9, 30 in all.

```
R L' F2 U R' D F' U' F2 R' U B U' F2 B2 D * B2 D2 F B2 U2
* = D2 B D2 R' D2 R B' R' D2 R // (10-1/30)
Solution: R L' F2 U R' D F' U' F2 R' U B U' F2 B2 D' B D2 R' D2 R B' R' D2 R B2 D2 F B2 U2 (30)
```

</details>

### Pure 2c2c

Two corner swaps, no twist.

#### Pure 2c2c, skeleton 1

Scramble: `R' U' F B2 U' R2 D2 R2 B2 U' R2 D B2 U' F2 R' B D' B L B L D2 F R' U' R' U' F`

Skeleton: `D2 L F2 B R2 U' R' F R2 U' B' U F U' D' F'` (16)

Left: DBL ↔ DFL, UBR ↔ UFR

<details>
<summary>Answer for pure 2c2c, skeleton 1</summary>

**8 moves or less per insertion** (two comms): +11, 27 in all.

```
D2 L F2 B R2 U' ^ R' F R2 U' B' U F U' D' * F'
* = U2 F' D F U2 F' D' F // (8-3/21)
^ = F' R' B' R F R' B R // (8-2/27)
Solution: D2 L F2 B R2 U' F' R' B' R F R' F B R2 U' B' U F U D' F' D F U2 F' D' (27)
```

**Up to 10 moves per insertion** (two comms): +10, 26 in all.

```
D2 L ^ F2 B R2 * U' R' F R2 U' B' U F U' D' F'
* = B L2 D R2 D' L2 D R2 D' B' // (10-0/26)
^ = R2 B' L2 F2 B' L2 B' R2 F2 B' // (10-10/26)
Solution: D2 R2 L B' L2 F2 B' D R2 D' L2 D R2 D' B' U' R' F R2 U' B' U F U' D' F' (26)
```

</details>

#### Pure 2c2c, skeleton 2

Scramble: `R' U' F D' R2 F2 U2 B2 F2 U' B2 D F2 D' F2 D F' R2 D' B' L U B U2 R U' R' U' F`

Skeleton: `D R2 F' B' U' L B' U2 D' F D2 L B U2 L D' F` (17)

Left: UFL ↔ UBR, DBR ↔ DFR

<details>
<summary>Answer for pure 2c2c, skeleton 2</summary>

**8 moves or less per insertion** (two comms): +10, 27 in all.

```
D R2 F' B' ^ U' L B' U2 D' F D2 L B U2 * L D' F
* = F2 L B2 L' F2 L B2 L' // (8-2/23)
^ = L D' L' U' L D L' U // (8-4/27)
Solution: D R2 F' B' L D' L' U' L D B' U2 D' F D2 L B U2 F2 L B2 L' F2 L B2 D' F (27)
```

**Up to 10 moves per insertion**: nothing better, 27 stays the best.

</details>

#### Pure 2c2c, skeleton 3

Scramble: `R' U' F D2 L2 B2 L2 U' L2 U F2 U' R2 B D2 F U F2 R' B U2 F2 L2 R' U' F`

Skeleton: `D2 F' B U' R B2 L F' R2 U2 B' U' R B D B U F'` (18)

Left: DBL ↔ DFR, UBL ↔ UBR

<details>
<summary>Answer for pure 2c2c, skeleton 3</summary>

**8 moves or less per insertion** (two comms): +9, 27 in all.

```
D2 * F' B ^ U' R B2 L F' R2 U2 B' U' R B D B U F'
* = U2 F' D2 F U2 F' D2 F // (8-2/24)
^ = B' D2 B U2 B' D2 B U2 // (8-5/27)
Solution: U2 D2 F' D2 F U2 F' B U2 B' D2 B U R B2 L F' R2 U2 B' U' R B D B U F' (27)
```

**Up to 10 moves per insertion** (one alg for the whole leftover): +7, 25 in all.

```
D2 F' B U' R B2 L F' R2 U2 B' U' * R B D B U F'
* = U L2 F2 B2 R2 D L2 F2 B2 R2 // (10-3/25)
Solution: D2 F' B U' R B2 L F' R2 U2 B' L2 F2 B2 R2 D L2 F2 B2 R' B D B U F' (25)
```

</details>

#### Pure 2c2c, skeleton 4

Scramble: `R' U' F B2 L2 U2 L2 D B2 L2 D R2 D L2 D R2 F' R2 F R F U' B' D2 L2 D' R' U' F`

Skeleton: `B L B2 L U' F2 B' U2 F2 D' R B D B2 R D F U D2` (19)

Left: DFL ↔ DBR, DFR ↔ UBR

<details>
<summary>Answer for pure 2c2c, skeleton 4</summary>

**8 moves or less per insertion** (two comms): +9, 28 in all.

```
B ^ L B2 L U' F2 B' U2 F2 D' R B D B2 * R D F U D2
* = U R D R' U' R D' R' // (8-4/23)
^ = B2 L F L' B2 L F' L' // (8-3/28)
Solution: B' L F L' B2 L F' B2 L U' F2 B' U2 F2 D' R B D B2 U R D R' U' R F U D2 (28)
```

**Up to 10 moves per insertion**: nothing better, 28 stays the best.

</details>

#### Pure 2c2c, skeleton 5

Scramble: `R' U' F L2 U2 R2 F2 D2 F' D2 L2 B2 R2 U' B L' R' U' F R2 D F R' U' F`

Skeleton: `B2 D2 F' R2 D2 B L U2 R U' D2 B2 D2 R B U F' B2 R' F` (20)

Left: DBL ↔ UFR, UFL ↔ DFR

<details>
<summary>Answer for pure 2c2c, skeleton 5</summary>

**8 moves or less per insertion** (two comms): +8, 28 in all.

```
B2 D2 F' R2 D2 ^ B L U2 R U' D2 B2 D2 R B U F' * B2 R' F
* = R' F2 R B2 R' F2 R B2 // (8-5/23)
^ = D' F' D B D' F D B' // (8-3/28)
Solution: B2 D2 F' R2 D F' D B D' F D L U2 R U' D2 B2 D2 R B U F' R' F2 R B2 R' F' (28)
```

**Up to 10 moves per insertion**: nothing better, 28 stays the best.

</details>

#### Pure 2c2c, skeleton 6

Scramble: `R' U' F D' F2 D' R2 B2 R2 D U F2 R2 U' R' U' L' R2 B' U2 F U' L' D2 U' R' U' F`

Skeleton: `U B U L U' L2 B U' D R U2 F2 D' B R2 U F' R2 L2 D B` (21)

Left: DFL ↔ DBR, UFL ↔ DFR

<details>
<summary>Answer for pure 2c2c, skeleton 6</summary>

**8 moves or less per insertion** (two comms): +7, 28 in all.

```
^ U B U * L U' L2 B U' D R U2 F2 D' B R2 U F' R2 L2 D B
* = U R U' L U R' U' L' // (8-4/25)
^ = F2 U B U' F2 U B' U' // (8-5/28)
Solution: F2 U B U' F2 U' R U' L U R' U2 L2 B U' D R U2 F2 D' B R2 U F' R2 L2 D B (28)
```

**Up to 10 moves per insertion**: nothing better, 28 stays the best.

</details>

#### Pure 2c2c, skeleton 7

Scramble: `R' U' F D B2 D2 L2 U R2 F2 D' R2 B2 D' B' F2 L R2 U B F' U' R F R' U' F`

Skeleton: `U2 R F B2 U D2 F2 D B' U' R' D R2 F' U2 L' F' R2 F' L2 F' B` (22)

Left: DBL ↔ DFR, DBR ↔ UBR

<details>
<summary>Answer for pure 2c2c, skeleton 7</summary>

**8 moves or less per insertion** (two comms): +7, 29 in all.

```
U2 R F B2 U D2 F2 D B' U' R' ^ D R2 F' U2 L' F' * R2 F' L2 F' B
* = F' L' F R2 F' L F R2 // (8-6/24)
^ = L2 D R' D' L2 D R D' // (8-3/29)
Solution: U2 R F B2 U D2 F2 D B' U' R' L2 D R' D' L2 D R' F' U2 L' F2 L' F R2 F' L' F' B (29)
```

**Up to 10 moves per insertion**: nothing better, 29 stays the best.

</details>

#### Pure 2c2c, skeleton 8

Scramble: `R' U' F L2 B2 D F2 L2 F2 U2 L2 U' B2 D L' B2 U2 F' L' U L' D2 R D2 U' R' U' F`

Skeleton: `L' F' R2 D B2 D2 B' R B2 L2 B2 L U B2 U2 D'` (16)

Left: DFL ↔ DFR, DBR ↔ UBR

<details>
<summary>Answer for pure 2c2c, skeleton 8</summary>

**8 moves or less per insertion** (two comms): +8, 24 in all.

```
L' ^ F' R2 D B2 D2 B' R B2 L2 B2 * L U B2 U2 D'
* = D2 L U L' D2 L U' L' // (8-4/20)
^ = L' F' R' F L F' R F // (8-4/24)
Solution: L2 F' R' F L F' R' D B2 D2 B' R B2 L2 B2 D2 L U L' D2 L B2 U2 D' (24)
```

**Up to 10 moves per insertion**: nothing better, 24 stays the best.

</details>

#### Pure 2c2c, skeleton 9

Scramble: `R' U' F B2 D' B2 D L2 D2 L2 R2 B2 D' B2 U2 B' R U R2 F' R2 U B F U' R' U' F`

Skeleton: `D2 F2 B' R2 B' U L' U' F B' R F' U F2 L F2 L2` (17)

Left: DFL ↔ UFL, UBL ↔ UFR

<details>
<summary>Answer for pure 2c2c, skeleton 9</summary>

**8 moves or less per insertion** (two comms): +10, 27 in all.

```
D2 F2 B' R2 B' U L' ^ U' F B' R F' U F2 L * F2 L2
* = L B L' F2 L B' L' F2 // (8-4/21)
^ = L2 U R' U' L2 U R U' // (8-2/27)
Solution: D2 F2 B' R2 B' U L U R' U' L2 U R U2 F B' R F' U F2 L2 B L' F2 L B' L (27)
```

**Up to 10 moves per insertion**: nothing better, 27 stays the best.

</details>

#### Pure 2c2c, skeleton 10

Scramble: `R' U' F B2 R2 B2 R2 F2 D' B2 U' L2 U2 L2 B U2 F' D' U R' U2 F L U2 D' R' U' F`

Skeleton: `B D2 R L U L B2 L2 D B D2 B2 D2 B U L U' F'` (18)

Left: UBL ↔ UFR, UFL ↔ DBR

<details>
<summary>Answer for pure 2c2c, skeleton 10</summary>

**8 moves or less per insertion** (two comms): +8, 26 in all.

```
B D2 R L U L B2 L2 D ^ B D2 B2 D2 B * U L U' F'
* = B D2 B' U B D2 B' U' // (8-3/23)
^ = U B D2 B' U' B D2 B' // (8-5/26)
Solution: B D2 R L U L B2 L2 U D B D2 B' U' B' D2 B2 D2 B' U B D2 B' L U' F' (26)
```

**Up to 10 moves per insertion**: nothing better, 26 stays the best.

</details>

#### Pure 2c2c, skeleton 11

Scramble: `R' U' F L2 D2 U2 R2 B L2 B2 D2 F' U2 B' L' R2 D R2 D R' D2 B' D B' F2 D' R' U' F`

Skeleton: `D2 F' B' L2 B R2 L' U F L2 U2 L2 U' D F L2 B' R2 L` (19)

Left: DBL ↔ DBR, UBL ↔ UBR

<details>
<summary>Answer for pure 2c2c, skeleton 11</summary>

**8 moves or less per insertion** (two comms): +10, 29 in all.

```
D2 F' B' L2 B ^ R2 L' U F L2 U2 L2 * U' D F L2 B' R2 L
* = L' D2 L U' L' D2 L U // (8-3/24)
^ = B R' B' L' B R B' L // (8-3/29)
Solution: D2 F' B' L2 B2 R' B' L' B R B' R2 U F L2 U2 L D2 L U' L' D2 L D F L2 B' R2 L (29)
```

**Up to 10 moves per insertion** (one alg for the whole leftover): +8, 27 in all.

```
D2 F' B' L2 B R2 L' U F L2 U2 L2 U' D * F L2 B' R2 L
* = U B2 L2 D' F2 D L2 B2 U' R2 // (10-2/27)
Solution: D2 F' B' L2 B R2 L' U F L2 U2 L2 D B2 L2 D' F2 D L2 B2 U' R2 F L2 B' R2 L (27)
```

</details>

#### Pure 2c2c, skeleton 12

Scramble: `R' U' F D2 B2 R' B2 L' D2 B2 R D2 B2 L' R2 U B2 R' D U2 B L' F' U' R' U' F`

Skeleton: `R' L2 B U D2 R U F2 B2 U2 B2 D2 B2 D' F2 D R U F' U'` (20)

Left: DBL ↔ DBR, DFL ↔ UFR

<details>
<summary>Answer for pure 2c2c, skeleton 12</summary>

**8 moves or less per insertion** (two comms): +8, 28 in all.

```
R' L2 B U D2 R U F2 B2 ^ U2 B2 D2 B2 D' F2 D * R U F' U'
* = D2 R U R' D2 R U' R' // (8-5/23)
^ = F2 U B' U' F2 U B U' // (8-3/28)
Solution: R' L2 B U D2 R U B2 U B' U' F2 U B U B2 D2 B2 D' F2 D' R U R' D2 R F' U' (28)
```

**Up to 10 moves per insertion**: nothing better, 28 stays the best.

</details>

#### Pure 2c2c, skeleton 13

Scramble: `R' U' F U' D L2 B2 F2 D R2 U2 B2 L2 R2 D F2 U L B F' R2 D' F' L R' U' F`

Skeleton: `U' B2 L U R' F2 R' B2 R2 B' U' L' B' L2 F2 L2 F' U F U R2` (21)

Left: DBL ↔ UFR, UBL ↔ UBR

<details>
<summary>Answer for pure 2c2c, skeleton 13</summary>

**8 moves or less per insertion** (two comms): +10, 31 in all.

```
* U' B2 L U R' F2 R' B2 R2 B' U' L' B' L2 F2 L2 F' U F U R2
* = F2 U' B U F2 U' B' U // (8-3/26)
F2 U' B U F2 U' B ^ L U R' F2 R' B2 R2 B' U' L' B' L2 F2 L2 F' U F U R2
^ = B' U' F2 U B U' F2 U // (8-3/31)
Solution: F2 U' B U F2 U2 F2 U B U' F2 U L U R' F2 R' B2 R2 B' U' L' B' L2 F2 L2 F' U F U R2 (31)
```

**Up to 10 moves per insertion**: nothing better, 31 stays the best.

</details>

#### Pure 2c2c, skeleton 14

Scramble: `R' U' F R2 U2 R2 F2 L2 F' L2 F2 D2 B' D2 L2 F L' D2 B U2 L' D2 U L D' R' U' F`

Skeleton: `L F' R F' B D' R F2 B' R' B L' U2 F R2 B L2 D' R' D F' D2` (22)

Left: DFL ↔ DFR, UFL ↔ UFR

<details>
<summary>Answer for pure 2c2c, skeleton 14</summary>

**8 moves or less per insertion** (two comms): +9, 31 in all.

```
L F' R F' B D' R F2 ^ B' R' B * L' U2 F R2 B L2 D' R' D F' D2
* = D2 L' U2 L D2 L' U2 L // (8-4/26)
^ = R F R' B' R F' R' B // (8-3/31)
Solution: L F' R F' B D' R F2 R F R' B' R F' R2 B D2 L' U2 L D2 L' F R2 B L2 D' R' D F' D2 (31)
```

**Up to 10 moves per insertion** (two comms): +5, 27 in all.

```
L F' R F' B D' R F2 B' R' B L' U2 F ^ R2 B L2 * D' R' D F' D2
* = F' D' F R' F' D F D' R D // (10-9/23)
^ = F' U2 L D2 L' U2 L D2 L' F // (10-6/27)
Solution: L F' R F' B D' R F2 B' R' B D2 L' U2 L D2 L' F R2 B L2 F' D' F R' F' D' (27)
```

</details>

#### Pure 2c2c, skeleton 15

Scramble: `R' U' F D2 R2 U2 F2 L2 B D2 U2 F' L2 D U2 B D L' F U2 L U' R' U' F`

Skeleton: `R' B' R' D2 R2 B D2 B L U' B2 R B2 D2 B' U2` (16)

Left: DBL ↔ UBR, DFL ↔ UBL

<details>
<summary>Answer for pure 2c2c, skeleton 15</summary>

**8 moves or less per insertion** (two comms): +10, 26 in all.

```
R' B' R' D2 R2 B D2 ^ B L U' B2 R B2 * D2 B' U2
* = B U2 B' D2 B U2 B' D2 // (8-4/20)
^ = L' B R' B' L B R B' // (8-2/26)
Solution: R' B' R' D2 R2 B D2 L' B R' B' L B R L U' B2 R B' U2 B' D2 B U2 B2 U2 (26)
```

**Up to 10 moves per insertion** (one alg for the whole leftover): +9, 25 in all.

```
R' B' R' D2 R2 B D2 B L U' B2 R B2 * D2 B' U2
* = B' L2 U2 B R2 F' L2 D2 F R2 // (10-1/25)
Solution: R' B' R' D2 R2 B D2 B L U' B2 R B L2 U2 B R2 F' L2 D2 F R2 D2 B' U2 (25)
```

</details>

#### Pure 2c2c, skeleton 16

Scramble: `R' U' F D2 F2 L B2 F2 D2 F2 R' B2 R2 D2 U' B' F' L U' L2 D2 L F' R' U' F`

Skeleton: `R' F2 R D' B2 L' U' R D2 R2 U2 B' R' B2 U2 B U2` (17)

Left: DFL ↔ UBR, UBL ↔ DBR

<details>
<summary>Answer for pure 2c2c, skeleton 16</summary>

**8 moves or less per insertion** (two comms): +9, 26 in all.

```
R' ^ F2 R D' B2 L' * U' R D2 R2 U2 B' R' B2 U2 B U2
* = R' D' R U' R' D R U // (8-3/22)
^ = R' B' R F2 R' B R F2 // (8-4/26)
Solution: R2 B' R F2 R' B R2 D' B2 R' L' D' R U' R' D R2 D2 R2 U2 B' R' B2 U2 B U2 (26)
```

**Up to 10 moves per insertion**: nothing better, 26 stays the best.

</details>

#### Pure 2c2c, skeleton 17

Scramble: `R' U' F U2 B' D2 L2 F2 U2 R2 F' R2 F L2 B' R U' L D' L' R' D' F2 R' U' F`

Skeleton: `B2 D B2 U2 R F2 L' U' L2 U2 L2 B2 D2 L' F' B2 L' B2` (18)

Left: DBL ↔ DFL, UBL ↔ DBR

<details>
<summary>Answer for pure 2c2c, skeleton 17</summary>

**8 moves or less per insertion** (two comms): +10, 28 in all.

```
B2 D B2 U2 R F2 L' U' L2 U2 L2 B2 D2 * L' F' B2 L' B2
* = B' R' B L' B' R B L // (8-3/23)
B2 D B2 U2 R F2 L' U' L2 U2 L2 B2 D2 B' R' B L' B' R F' B' ^ L' B2
^ = B R B' L2 B R' B' L2 // (8-3/28)
Solution: B2 D B2 U2 R F2 L' U' L2 U2 L2 B2 D2 B' R' B L' B' R F' R B' L2 B R' B' L B2 (28)
```

**Up to 10 moves per insertion** (one alg for the whole leftover): +7, 25 in all.

```
B2 D B2 U2 R F2 * L' U' L2 U2 L2 B2 D2 L' F' B2 L' B2
* = F2 D B2 R2 L2 F2 U B2 R2 L2 // (10-3/25)
Solution: B2 D B2 U2 R D B2 R2 L2 F2 U B2 R2 L U' L2 U2 L2 B2 D2 L' F' B2 L' B2 (25)
```

</details>

#### Pure 2c2c, skeleton 18

Scramble: `R' U' F L2 D' R2 B2 D' F2 D' B2 U R2 D R' D F2 R' B U' L F L2 R' U' F`

Skeleton: `D R2 U' B L' B' D' L2 B' U F' R' L2 B D2 F L' U2 R'` (19)

Left: UBL ↔ DBR, UFL ↔ DFR

<details>
<summary>Answer for pure 2c2c, skeleton 18</summary>

**8 moves or less per insertion** (two comms): +8, 27 in all.

```
D R2 U' B L' B' D' L2 B' ^ U F' R' L2 B D2 F L' * U2 R'
* = R' D' R U2 R' D R U2 // (8-4/23)
^ = B2 U F2 U' B2 U F2 U' // (8-4/27)
Solution: D R2 U' B L' B' D' L2 B U F2 U' B2 U F R' L2 B D2 F R' L' D' R U2 R' D (27)
```

**Up to 10 moves per insertion** (two comms): +7, 26 in all.

```
D R2 U' B L' B' D' * L2 B' U ^ F' R' L2 B D2 F L' U2 R'
* = D' B2 D B2 L2 U B2 U' B2 L2 // (10-4/25)
^ = U' B' U F2 U' B U F2 // (8-7/26)
Solution: D R2 U' B L' B' D2 B2 D B2 L2 U F2 B2 U' B U F R' L2 B D2 F L' U2 R' (26)
```

</details>

#### Pure 2c2c, skeleton 19

Scramble: `R' U' F U' L' U2 R D2 R B2 R F2 L2 F2 U2 F2 D R U L B L' R' D' R' U' F`

Skeleton: `U2 R' F2 R' F2 U' B2 R D2 B R' F' L' B U' F' B2 R2 B L` (20)

Left: DFL ↔ UFL, DFR ↔ UBR

<details>
<summary>Answer for pure 2c2c, skeleton 19</summary>

**8 moves or less per insertion** (two comms): +12, 32 in all.

```
U2 R' F2 ^ R' F2 U' B2 R D2 B R' F' L' B U' * F' B2 R2 B L
* = U' B2 U F2 U' B2 U F2 // (8-2/26)
^ = F L' F' R2 F L F' R2 // (8-2/32)
Solution: U2 R' F' L' F' R2 F L F' R F2 U' B2 R D2 B R' F' L' B U2 B2 U F2 U' B2 U F B2 R2 B L (32)
```

**Up to 10 moves per insertion**: nothing better, 32 stays the best.

</details>

#### Pure 2c2c, skeleton 20

Scramble: `R' U' F B D2 F' U2 B U2 R2 F2 L2 F' D2 F R2 D' U2 F' U L' R' U R U2 L' R' U' F`

Skeleton: `R L' F2 U R' D F' U' F2 R' U B U' F2 B2 D B2 D2 F B2 U2` (21)

Left: UFL ↔ DFR, UBR ↔ UFR

<details>
<summary>Answer for pure 2c2c, skeleton 20</summary>

**8 moves or less per insertion** (two comms): +6, 27 in all.

```
R L' F2 U R' * D F' U' F2 R' ^ U B U' F2 B2 D B2 D2 F B2 U2
* = F' U' F D F' U F D' // (8-7/22)
^ = R' U L2 U' R U L2 U' // (8-3/27)
Solution: R L' F2 U R' F' U' F D F R2 U L2 U' R U L2 B U' F2 B2 D B2 D2 F B2 U2 (27)
```

**Up to 10 moves per insertion**: nothing better, 27 stays the best.

</details>

### Twisted 2c2c

Two corner swaps, each with a twist.

#### Twisted 2c2c, skeleton 1

Scramble: `R' U' F U2 R B2 L' B2 D2 R F2 D2 L' B2 R F U2 B L' F L2 D R F R' U' F`

Skeleton: `D2 L F2 B R2 U' R' F R2 U' B' U F U' D' F'` (16)

Left: DFL ↔ UBL, DFR ↔ UBR

<details>
<summary>Answer for twisted 2c2c, skeleton 1</summary>

**8 moves or less per insertion** (two comms): +8, 24 in all.

```
D2 L F2 B R2 U' R' F R2 U' B' ^ U F U' D' F' *
* = F' U2 F D F' U2 F D' // (8-1/23)
^ = B' U F U' B U F' U' // (8-7/24)
Solution: D2 L F2 B R2 U' R' F R2 U' B2 U F U' B D' F2 U2 F D F' U2 F D' (24)
```

**Up to 10 moves per insertion**: nothing better, 24 stays the best.

</details>

#### Twisted 2c2c, skeleton 2

Scramble: `R' U' F R2 B D2 F2 D2 F R2 F L2 F' L2 D2 B D2 R U2 L' D2 R U B2 R U' R' U' F`

Skeleton: `D R2 F' B' U' L B' U2 D' F D2 L B U2 L D' F` (17)

Left: DBL ↔ UFR, DBR ↔ DFR

<details>
<summary>Answer for twisted 2c2c, skeleton 2</summary>

**8 moves or less per insertion** (two comms): +8, 25 in all.

```
D R2 F' B' U' L B' U2 D' F D2 L B U2 * L D' F
* = U L D L' U' L D' L' // (8-4/21)
D R2 F' B' U' L B' U2 D' F D2 L B U' L D L' U' ^ L D2 F
^ = U L' D2 L U' L' D2 L // (8-4/25)
Solution: D R2 F' B' U' L B' U2 D' F D2 L B U' L D L2 D2 L U' L' D2 L2 D2 F (25)
```

**Up to 10 moves per insertion**: nothing better, 25 stays the best.

</details>

#### Twisted 2c2c, skeleton 3

Scramble: `R' U' F U2 R2 U2 L2 D R2 U L2 R2 B2 D2 L2 U2 B' D' R' F' U F2 L2 B2 U' R' U' F`

Skeleton: `D2 F' B U' R B2 L F' R2 U2 B' U' R B D B U F'` (18)

Left: DBL ↔ DFL, DBR ↔ UFR

<details>
<summary>Answer for twisted 2c2c, skeleton 3</summary>

**8 moves or less per insertion** (two comms): +9, 27 in all.

```
D2 F' B U' * R B2 L F' R2 U2 B' U' R B D B U F'
* = U2 R D' R' U2 R D R' // (8-3/23)
D2 F' B U R D' ^ R' U2 R D B2 L F' R2 U2 B' U' R B D B U F'
^ = D R U' R' D' R U R' // (8-4/27)
Solution: D2 F' B U R2 U' R' D' R U R2 U2 R D B2 L F' R2 U2 B' U' R B D B U F' (27)
```

**Up to 10 moves per insertion**: nothing better, 27 stays the best.

</details>

#### Twisted 2c2c, skeleton 4

Scramble: `R' U' F U' D2 R2 U2 B2 D2 F' R2 B' R2 B U2 L D2 F R2 B2 U B' F2 D' R' U' F`

Skeleton: `B L B2 L U' F2 B' U2 F2 D' R B D B2 R D F U D2` (19)

Left: UBL ↔ UBR, UFL ↔ UFR

<details>
<summary>Answer for twisted 2c2c, skeleton 4</summary>

**8 moves or less per insertion** (two comms): +9, 28 in all.

```
B L B2 L * U' F2 B' ^ U2 F2 D' R B D B2 R D F U D2
* = B2 U' F2 U B2 U' F2 U // (8-4/23)
^ = B U2 B' D B U2 B' D' // (8-3/28)
Solution: B L B2 L B2 U' F2 U B2 U B' D B U2 B' U2 D' F2 D' R B D B2 R D F U D2 (28)
```

**Up to 10 moves per insertion**: nothing better, 28 stays the best.

</details>

#### Twisted 2c2c, skeleton 5

Scramble: `R' U' F D' F2 L2 D F2 L2 B2 U' F2 D' F U' L' D' R B2 D R2 B U D' R' U' F`

Skeleton: `B2 D2 F' R2 D2 B L U2 R U' D2 B2 D2 R B U F' B2 R' F` (20)

Left: DFL ↔ UFR, UFL ↔ DFR

<details>
<summary>Answer for twisted 2c2c, skeleton 5</summary>

**8 moves or less per insertion** (two comms): +10, 30 in all.

```
B2 D2 F' R2 D2 B L U2 R U' D2 B2 ^ D2 R B U F' B2 * R' F
* = F' L' F R' F' L F R // (8-4/24)
^ = B' U' B D' B' U B D // (8-2/30)
Solution: B2 D2 F' R2 D2 B L U2 R U' D2 B U' B D' B' U B D' R B U F2 B2 L' F R' F' L F2 (30)
```

**Up to 10 moves per insertion**: nothing better, 30 stays the best.

</details>

#### Twisted 2c2c, skeleton 6

Scramble: `R' U' F R F2 L B2 R' B2 U2 F2 D2 B2 L2 D2 B2 D' F' L U R D R2 U B R' U' F`

Skeleton: `U B U L U' L2 B U' D R U2 F2 D' B R2 U F' R2 L2 D B` (21)

Left: DBL ↔ UBR, UBL ↔ DFR

<details>
<summary>Answer for twisted 2c2c, skeleton 6</summary>

**8 moves or less per insertion** (two comms): +10, 31 in all.

```
U B U L U' L2 B U' D R U2 F2 D' B R2 * U F' R2 ^ L2 D B
* = F' U B U' F U B' U' // (8-2/27)
^ = R2 B L B' R2 B L' B' // (8-4/31)
Solution: U B U L U' L2 B U' D R U2 F2 D' B R2 F' U B U' F U F' L B' R2 B L' B' L2 D B (31)
```

**Up to 10 moves per insertion**: nothing better, 31 stays the best.

</details>

#### Twisted 2c2c, skeleton 7

Scramble: `R' U' F B2 R2 B' U2 L2 U2 L2 F2 U2 B D2 B' L2 R B' L' R2 U' F' R U R' U' R' U' F`

Skeleton: `U2 R F B2 U D2 F2 D B' U' R' D R2 F' U2 L' F' R2 F' L2 F' B` (22)

Left: DFL ↔ UFR, UFL ↔ UBR

<details>
<summary>Answer for twisted 2c2c, skeleton 7</summary>

**8 moves or less per insertion** (two comms): +9, 31 in all.

```
U2 ^ R F B2 U D2 F2 D * B' U' R' D R2 F' U2 L' F' R2 F' L2 F' B
* = D B' U B D' B' U' B // (8-4/26)
^ = B' L2 B R B' L2 B R' // (8-3/31)
Solution: U2 B' L2 B R B' L2 F B' U D2 F2 D2 B' U B D' B' U2 R' D R2 F' U2 L' F' R2 F' L2 F' B (31)
```

**Up to 10 moves per insertion**: nothing better, 31 stays the best.

</details>

#### Twisted 2c2c, skeleton 8

Scramble: `R' U' F R D2 B2 F2 R D2 R' B2 L' F2 L U2 B D U' B2 U L F2 R D' R' U' F`

Skeleton: `L' F' R2 D B2 D2 B' R B2 L2 B2 L U B2 U2 D'` (16)

Left: DBL ↔ DFR, UFL ↔ DBR

<details>
<summary>Answer for twisted 2c2c, skeleton 8</summary>

**8 moves or less per insertion** (two comms): +10, 26 in all.

```
L' F' R2 D B2 D2 ^ B' R B2 L2 B2 L U * B2 U2 D'
* = D F D' B2 D F' D' B2 // (8-3/21)
^ = D F2 D' B' D F2 D' B // (8-3/26)
Solution: L' F' R2 D B2 D' F2 D' B' D F2 D' R B2 L2 B2 L U D F D' B2 D F' U2 D2 (26)
```

**Up to 10 moves per insertion**: nothing better, 26 stays the best.

</details>

#### Twisted 2c2c, skeleton 9

Scramble: `R' U' F R2 U' R2 D L2 D B2 R2 F2 U2 B2 D U F R' F2 U R' B2 U' F R' U' F`

Skeleton: `D2 F2 B' R2 B' U L' U' F B' R F' U F2 L F2 L2` (17)

Left: DBL ↔ UBL, DBR ↔ DFR

<details>
<summary>Answer for twisted 2c2c, skeleton 9</summary>

**8 moves or less per insertion** (two comms): +9, 26 in all.

```
D2 F2 B' R2 B' ^ U L' * U' F B' R F' U F2 L F2 L2
* = F2 U' B' U F2 U' B U // (8-4/21)
^ = B' D2 B U B' D2 B U' // (8-3/26)
Solution: D2 F2 B' R2 B2 D2 B U B' D2 B L' F2 U' B' U F2 U' F R F' U F2 L F2 L2 (26)
```

**Up to 10 moves per insertion**: nothing better, 26 stays the best.

</details>

#### Twisted 2c2c, skeleton 10

Scramble: `R' U' F L' U2 L R U2 R' B2 U2 L' F2 D2 R' U R2 F U2 B' L' D' R2 F' L U' R' U' F`

Skeleton: `B D2 R L U L B2 L2 D B D2 B2 D2 B U L U' F'` (18)

Left: DBL ↔ UBR, UFL ↔ DFR

<details>
<summary>Answer for twisted 2c2c, skeleton 10</summary>

**8 moves or less per insertion** (two comms): +8, 26 in all.

```
B D2 R L U L B2 L2 D B D2 B2 D2 B U * L U' F'
* = D R' D' L D R D' L' // (8-2/24)
B D2 R L U L B2 L2 D B D2 B2 D2 B U D R' D' L D R U' ^ D' F'
^ = U R' D' R U' R' D R // (8-6/26)
Solution: B D2 R L U L B2 L2 D B D2 B2 D2 B U D R' D' R L U' R' D R D' F' (26)
```

**Up to 10 moves per insertion**: nothing better, 26 stays the best.

</details>

#### Twisted 2c2c, skeleton 11

Scramble: `R' U' F D2 L U2 R' F2 L2 B2 U2 F2 U2 L2 B D' B' F2 D L2 B D L R' U' F`

Skeleton: `D2 F' B' L2 B R2 L' U F L2 U2 L2 U' D F L2 B' R2 L` (19)

Left: DBL ↔ DFL, DBR ↔ UBR

<details>
<summary>Answer for twisted 2c2c, skeleton 11</summary>

**8 moves or less per insertion** (two comms): +9, 28 in all.

```
^ D2 F' B' L2 B R2 L' U F L2 U2 L2 U' D * F L2 B' R2 L
* = U' B2 U F U' B2 U F' // (8-3/24)
^ = F' U2 F D2 F' U2 F D2 // (8-4/28)
Solution: F' U2 F D2 F' U2 B' L2 B R2 L' U F L2 U2 L2 U2 D B2 U F U' B2 U L2 B' R2 L (28)
```

**Up to 10 moves per insertion**: nothing better, 28 stays the best.

</details>

#### Twisted 2c2c, skeleton 12

Scramble: `R' U' F U2 B L2 B R2 D2 F' D2 L2 F2 R2 D B L F L U R D' R' U' F`

Skeleton: `R' L2 B U D2 R U F2 B2 U2 B2 D2 B2 D' F2 D R U F' U'` (20)

Left: DFL ↔ UBR, UBL ↔ DBR

<details>
<summary>Answer for twisted 2c2c, skeleton 12</summary>

**8 moves or less per insertion** (two comms): +10, 30 in all.

```
R' L2 B U D2 R * U F2 B2 U2 B2 D2 B2 D' F2 D R U F' U'
* = R U' L U R' U' L' U // (8-2/26)
R' L2 B U D2 R2 U' L U R' U' ^ L' U2 F2 B2 U2 B2 D2 B2 D' F2 D R U F' U'
^ = U R D R' U' R D' R' // (8-4/30)
Solution: R' L2 B U D2 R2 U' L U D R' U' R D' R' L' U2 F2 B2 U2 B2 D2 B2 D' F2 D R U F' U' (30)
```

**Up to 10 moves per insertion**: nothing better, 30 stays the best.

</details>

#### Twisted 2c2c, skeleton 13

Scramble: `R' U' F B2 U2 L2 R' B2 U2 L' U2 R' U2 R' F2 D' F L2 U2 B2 L' D' L2 B' R' U' F`

Skeleton: `U' B2 L U R' F2 R' B2 R2 B' U' L' B' L2 F2 L2 F' U F U R2` (21)

Left: DFL ↔ DBR, UFL ↔ UFR

<details>
<summary>Answer for twisted 2c2c, skeleton 13</summary>

**8 moves or less per insertion** (two comms): +9, 30 in all.

```
U' B2 L ^ U R' F2 R' B2 R2 B' U' L' B' L2 F2 * L2 F' U F U R2
* = F' R' F L2 F' R F L2 // (8-5/24)
^ = F U B2 U' F' U B2 U' // (8-2/30)
Solution: U' B2 L F U B2 U' F' U B2 R' F2 R' B2 R2 B' U' L' B' L2 F R' F L2 F' R U F U R2 (30)
```

**Up to 10 moves per insertion**: nothing better, 30 stays the best.

</details>

#### Twisted 2c2c, skeleton 14

Scramble: `R' U' F B D2 L2 U2 B2 L2 B' U2 B2 R2 F' U2 L' D L U' L F' L F R' U' F`

Skeleton: `L F' R F' B D' R F2 B' R' B L' U2 F R2 B L2 D' R' D F' D2` (22)

Left: UBL ↔ UFR, UFL ↔ DFR

<details>
<summary>Answer for twisted 2c2c, skeleton 14</summary>

**8 moves or less per insertion** (two comms): +7, 29 in all.

```
^ L F' R F' B D' R F2 B' R' B L' U2 F R2 * B L2 D' R' D F' D2
* = R' B' L B R B' L' B // (8-2/28)
^ = F' R F L F' R' F L' // (8-7/29)
Solution: F' R F L F2 B D' R F2 B' R' B L' U2 F R B' L B R B' L' B2 L2 D' R' D F' D2 (29)
```

**Up to 10 moves per insertion**: nothing better, 29 stays the best.

</details>

#### Twisted 2c2c, skeleton 15

Scramble: `R' U' F R2 B2 D2 B' D2 L2 B' D2 B L2 B L' F' L R2 D' F2 L R2 B2 R' U' F`

Skeleton: `R' B' R' D2 R2 B D2 B L U' B2 R B2 D2 B' U2` (16)

Left: DBL ↔ DBR, DFL ↔ UBL

<details>
<summary>Answer for twisted 2c2c, skeleton 15</summary>

**8 moves or less per insertion** (two comms): +9, 25 in all.

```
R' ^ B' R' D2 R2 * B D2 B L U' B2 R B2 D2 B' U2
* = U2 B D2 B' U2 B D2 B' // (8-5/19)
^ = U2 B' D2 B U2 B' D2 B // (8-2/25)
Solution: R' U2 B' D2 B U2 B' D2 R' D2 R2 U2 B D2 B' U2 B2 L U' B2 R B2 D2 B' U2 (25)
```

**Up to 10 moves per insertion**: nothing better, 25 stays the best.

</details>

#### Twisted 2c2c, skeleton 16

Scramble: `R' U' F D' L2 D B2 U' R2 U R2 U2 R2 B2 L2 F' L' R2 U2 F' U F R D U2 R' U' F`

Skeleton: `R' F2 R D' B2 L' U' R D2 R2 U2 B' R' B2 U2 B U2` (17)

Left: DBL ↔ DBR, UBL ↔ UBR

<details>
<summary>Answer for twisted 2c2c, skeleton 16</summary>

**8 moves or less per insertion** (two comms): +9, 26 in all.

```
R' F2 R D' B2 ^ L' U' R D2 R2 U2 * B' R' B2 U2 B U2
* = U B' D' B U' B' D B // (8-3/22)
^ = D' L' U' L D L' U L // (8-4/26)
Solution: R' F2 R D' B2 D' L' U' L D R L' D2 R2 U' B' D' B U' B' D R' B2 U2 B U2 (26)
```

**Up to 10 moves per insertion**: nothing better, 26 stays the best.

</details>

#### Twisted 2c2c, skeleton 17

Scramble: `R' U' F U' R F2 L' D2 B2 U2 F2 L' F2 L' D2 F2 L' D L2 R2 B L R2 D F2 L' R' U' F`

Skeleton: `B2 D B2 U2 R F2 L' U' L2 U2 L2 B2 D2 L' F' B2 L' B2` (18)

Left: DBL ↔ UBL, DFL ↔ UFL

<details>
<summary>Answer for twisted 2c2c, skeleton 17</summary>

**8 moves or less per insertion** (two comms): +10, 28 in all.

```
B2 * D B2 U2 R F2 L' U' L2 U2 L2 B2 D2 L' F' B2 L' B2
* = B D B' U B D' B' U' // (8-1/25)
^ B' D B' U B D' B' U' D B2 U2 R F2 L' U' L2 U2 L2 B2 D2 L' F' B2 L' B2
^ = U2 B' D B U2 B' D' B // (8-5/28)
Solution: U2 B' D B U2 B2 U B D' B' U' D B2 U2 R F2 L' U' L2 U2 L2 B2 D2 L' F' B2 L' B2 (28)
```

**Up to 10 moves per insertion**: nothing better, 28 stays the best.

</details>

#### Twisted 2c2c, skeleton 18

Scramble: `R' U' F R2 F2 U2 B2 D2 L2 B2 R2 U' R2 U' B2 L' B' U' B' U2 R2 B D2 B2 U' R' U' F`

Skeleton: `D R2 U' B L' B' D' L2 B' U F' R' L2 B D2 F L' U2 R'` (19)

Left: DBL ↔ UFR, UFL ↔ DBR

<details>
<summary>Answer for twisted 2c2c, skeleton 18</summary>

**8 moves or less per insertion** (two comms): +9, 28 in all.

```
D R2 U' B ^ L' B' D' L2 B' U * F' R' L2 B D2 F L' U2 R'
* = L B' L' F' L B L' F // (8-3/24)
^ = F L' B' L F' L' B L // (8-4/28)
Solution: D R2 U' F B L' B' L F' L' D' L2 B' U L B' L' F' L B R' L B D2 F L' U2 R' (28)
```

**Up to 10 moves per insertion**: nothing better, 28 stays the best.

</details>

#### Twisted 2c2c, skeleton 19

Scramble: `R' U' F L' U2 R2 D B2 U F2 D2 R2 U' B2 L2 U' B2 L' U' R' B' U2 L' U2 R' B' D' R' U' F`

Skeleton: `U2 R' F2 R' F2 U' B2 R D2 B R' F' L' B U' F' B2 R2 B L` (20)

Left: DBL ↔ UBL, UBR ↔ UFR

<details>
<summary>Answer for twisted 2c2c, skeleton 19</summary>

**8 moves or less per insertion** (two comms): +8, 28 in all.

```
U2 R' F2 R' F2 ^ U' B2 R D2 B R' F' L' B U' F' * B2 R2 B L
* = R F' R' B2 R F R' B2 // (8-3/25)
^ = F U' B2 U F' U' B2 U // (8-5/28)
Solution: U2 R' F2 R' F' U' B2 U F' U' R D2 B R' F' L' B U' F' R F' R' B2 R F R B L (28)
```

**Up to 10 moves per insertion**: nothing better, 28 stays the best.

</details>

#### Twisted 2c2c, skeleton 20

Scramble: `R' U' F L2 R2 F U2 F U2 R2 B2 F' R2 B' D2 R2 F' D' R F2 D' U' F L2 D R' U' F`

Skeleton: `R L' F2 U R' D F' U' F2 R' U B U' F2 B2 D B2 D2 F B2 U2` (21)

Left: DBR ↔ DFR, UBR ↔ UFR

<details>
<summary>Answer for twisted 2c2c, skeleton 20</summary>

**8 moves or less per insertion** (two comms): +6, 27 in all.

```
R L' F2 U R' D F' U' F2 ^ R' U B U' F2 B2 * D B2 D2 F B2 U2
* = F D B2 D' F' D B2 D' // (8-6/23)
^ = D' R' U R D R' U' R // (8-4/27)
Solution: R L' F2 U R' D F' U' F2 D' R' U R D R' B U' F' B2 D B2 D' F' D' F B2 U2 (27)
```

**Up to 10 moves per insertion**: nothing better, 27 stays the best.

</details>

### 3c1t

A twisted corner 3-cycle and one twisted corner.

#### 3c1t, skeleton 1

Scramble: `R' U' F L2 B D2 B U2 B' L2 F' U2 L2 D2 F' U' R B L B2 U' L U2 F' R' U' F`

Skeleton: `D2 L F2 B R2 U' R' F R2 U' B' U F U' D' F'` (16)

Left: DFL → DFR → UBR → DFL, UBL twisted clockwise

<details>
<summary>Answer for 3c1t, skeleton 1</summary>

**8 moves or less per insertion** (two comms): +10, 26 in all.

```
D2 L F2 B R2 U' R' F R2 * U' B' U F U' D' F'
* = F' D F U' F' D' F U // (8-2/22)
D2 L F2 B R2 U' R' F R2 F' D F U' F' D' ^ F B' U F U' D' F'
^ = D F' D' B D F D' B' // (8-4/26)
Solution: D2 L F2 B R2 U' R' F R2 F' D F U' F2 D' B D F D' F B2 U F U' D' F' (26)
```

**Up to 10 moves per insertion**: nothing better, 26 stays the best.

</details>

#### 3c1t, skeleton 2

Scramble: `R' U' F L2 D2 B2 D' R2 D' U' B2 L2 B F2 L D L U L R D2 F2 U' R' U' F`

Skeleton: `D R2 F' B' U' L B' U2 D' F D2 L B U2 L D' F` (17)

Left: DBL → DBR → UBR → DBL, DFR twisted counter-clockwise

<details>
<summary>Answer for 3c1t, skeleton 2</summary>

**8 moves or less per insertion** (two comms): +11, 28 in all.

```
D ^ R2 F' B' * U' L B' U2 D' F D2 L B U2 L D' F
* = B' D B U' B' D' B U // (8-3/22)
^ = D2 R' U R D2 R' U' R // (8-2/28)
Solution: D' R' U R D2 R' U' R' F' B2 D B U' B' D' B L B' U2 D' F D2 L B U2 L D' F (28)
```

**Up to 10 moves per insertion**: nothing better, 28 stays the best.

</details>

#### 3c1t, skeleton 3

Scramble: `R' U' F U2 R2 F2 U L2 U F2 U2 L2 D B2 U L D F' L B U F L' D U' R' U' F`

Skeleton: `D2 F' B U' R B2 L F' R2 U2 B' U' R B D B U F'` (18)

Left: UBL → UBR → UFL → UBL, DFR twisted counter-clockwise

<details>
<summary>Answer for 3c1t, skeleton 3</summary>

**8 moves or less per insertion** (two comms): +9, 27 in all.

```
D2 F' B U' R B2 L F' R2 U2 B' U' R B D * B U F'
* = U F2 U' B U F2 U' B' // (8-5/21)
D2 F' B U' R B2 L F' R2 U2 B' U' R B U D F2 U' ^ B U F
^ = U2 B' D' B U2 B' D B // (8-2/27)
Solution: D2 F' B U' R B2 L F' R2 U2 B' U' R B U D F2 U B' D' B U2 B' D B2 U F (27)
```

**Up to 10 moves per insertion**: nothing better, 27 stays the best.

</details>

#### 3c1t, skeleton 4

Scramble: `R' U' F U' L2 R2 U' B2 D2 R2 B2 R2 U B2 L2 U2 B R' F D U2 L2 U2 B U' R' U' F`

Skeleton: `B L B2 L U' F2 B' U2 F2 D' R B D B2 R D F U D2` (19)

Left: DBL → UBR → DFL → DBL, UFL twisted counter-clockwise

<details>
<summary>Answer for 3c1t, skeleton 4</summary>

**8 moves or less per insertion** (two comms): +10, 29 in all.

```
B L B2 L ^ U' F2 B' U2 F2 * D' R B D B2 R D F U D2
* = L2 D' R2 D L2 D' R2 D // (8-3/24)
^ = B U' F' U B' U' F U // (8-3/29)
Solution: B L B2 L B U' F' U B' U' F' B' U2 F2 L2 D' R2 D L2 D' R' B D B2 R D F U D2 (29)
```

**Up to 10 moves per insertion**: nothing better, 29 stays the best.

</details>

#### 3c1t, skeleton 5

Scramble: `R' U' F D2 L2 D U2 B2 R2 U2 L2 D' L2 U' L2 R2 F' R D U L2 B' F2 R' B2 R' U' F`

Skeleton: `B2 D2 F' R2 D2 B L U2 R U' D2 B2 D2 R B U F' B2 R' F` (20)

Left: DFL → UBR → UFR → DFL, DFR twisted counter-clockwise

<details>
<summary>Answer for 3c1t, skeleton 5</summary>

**8 moves or less per insertion** (two comms): +9, 29 in all.

```
B2 D2 F' R2 D2 B L U2 R U' D2 B2 D2 R * B U ^ F' B2 R' F
* = L' B' R2 B L B' R2 B // (8-1/27)
^ = U' B2 U F' U' B2 U F // (8-6/29)
Solution: B2 D2 F' R2 D2 B L U2 R U' D2 B2 D2 R L' B' R2 B L B' R2 U F' U' B2 U B2 R' F (29)
```

**Up to 10 moves per insertion**: nothing better, 29 stays the best.

</details>

#### 3c1t, skeleton 6

Scramble: `R' U' F L2 B' R2 D2 U2 B' R2 F' D2 L2 F' L2 F L2 D' L R F' R U R' D B2 R' U' F`

Skeleton: `U B U L U' L2 B U' D R U2 F2 D' B R2 U F' R2 L2 D B` (21)

Left: DFR → UBR → UFR → DFR, UFL twisted clockwise

<details>
<summary>Answer for 3c1t, skeleton 6</summary>

**8 moves or less per insertion** (two comms): +10, 31 in all.

```
U ^ B U L U' L2 B U' * D R U2 F2 D' B R2 U F' R2 L2 D B
* = L D R D' L' D R' D' // (8-4/25)
^ = R' F' R B R' F R B' // (8-2/31)
Solution: U R' F' R B R' F R U L U' L2 B U' L D R D' L' U2 D F2 D' B R2 U F' R2 L2 D B (31)
```

**Up to 10 moves per insertion** (two comms): +9, 30 in all.

```
^ U B U L U' L2 B * U' D R U2 F2 D' B R2 U F' R2 L2 D B
* = U' L D R D' L' D R' U D' // (10-6/25)
^ = R U R' B R U' R' U B' U' // (10-5/30)
Solution: R U R' B R U' R' U2 L U' L2 B U' L D R D' L' U2 D F2 D' B R2 U F' R2 L2 D B (30)
```

</details>

#### 3c1t, skeleton 7

Scramble: `R' U' F R2 F R2 B' D2 L2 B' R2 D2 F L2 D2 B2 D2 R' U2 F D U2 F L D' L2 R' U' F`

Skeleton: `U2 R F B2 U D2 F2 D B' U' R' D R2 F' U2 L' F' R2 F' L2 F' B` (22)

Left: DBL → DFR → UBL → DBL, DBR twisted clockwise

<details>
<summary>Answer for 3c1t, skeleton 7</summary>

**8 moves or less per insertion** (two comms): +10, 32 in all.

```
U2 ^ R F B2 U D2 * F2 D B' U' R' D R2 F' U2 L' F' R2 F' L2 F' B
* = D' B D F2 D' B' D F2 // (8-4/26)
^ = D R U2 R' D' R U2 R' // (8-2/32)
Solution: U2 D R U2 R' D' R U2 F B2 U D B D F2 D' B' D2 B' U' R' D R2 F' U2 L' F' R2 F' L2 F' B (32)
```

**Up to 10 moves per insertion**: nothing better, 32 stays the best.

</details>

#### 3c1t, skeleton 8

Scramble: `R' U' F L2 U R2 F2 D F2 D' L2 D U2 L2 R B U' R2 B U' R' D' U R' U' F`

Skeleton: `L' F' R2 D B2 D2 B' R B2 L2 B2 L U B2 U2 D'` (16)

Left: DFL → UFL → UBR → DFL, DBR twisted clockwise

<details>
<summary>Answer for 3c1t, skeleton 8</summary>

**8 moves or less per insertion** (two comms): +11, 27 in all.

```
L' F' R2 D B2 D2 B' ^ R B2 L2 B2 * L U B2 U2 D'
* = B R2 B' L B R2 B' L' // (8-3/21)
^ = F L' F' R F L F' R' // (8-2/27)
Solution: L' F' R2 D B2 D2 F B' L' F' R F L F' B2 L2 B' R2 B' L B R2 B' U B2 U2 D' (27)
```

**Up to 10 moves per insertion**: nothing better, 27 stays the best.

</details>

#### 3c1t, skeleton 9

Scramble: `R' U' F R F2 R2 B2 D2 B2 R' D2 F2 R2 B2 L2 F' R U' L2 U B F2 R B' R' U' F`

Skeleton: `D2 F2 B' R2 B' U L' U' F B' R F' U F2 L F2 L2` (17)

Left: DBL → UFL → DFR → DBL, DBR twisted counter-clockwise

<details>
<summary>Answer for 3c1t, skeleton 9</summary>

**8 moves or less per insertion** (two comms): +10, 27 in all.

```
D2 F2 B' R2 B' U L' U' F B' R F' U ^ F2 * L F2 L2
* = B2 L F2 L' B2 L F2 L' // (8-5/20)
^ = U L U' R2 U L' U' R2 // (8-1/27)
Solution: D2 F2 B' R2 B' U L' U' F B' R F' U2 L U' R2 U L' U' R2 F2 B2 L F2 L' B2 L' (27)
```

**Up to 10 moves per insertion**: nothing better, 27 stays the best.

</details>

#### 3c1t, skeleton 10

Scramble: `R' U' F D U B2 U F2 U B2 U F2 L2 R2 B R B2 L F' U B D' U2 B D' R' U' F`

Skeleton: `B D2 R L U L B2 L2 D B D2 B2 D2 B U L U' F'` (18)

Left: UBL → DFR → UBR → UBL, DFL twisted counter-clockwise

<details>
<summary>Answer for 3c1t, skeleton 10</summary>

**8 moves or less per insertion** (two comms): +11, 29 in all.

```
^ B D2 R L U * L B2 L2 D B D2 B2 D2 B U L U' F'
* = U R' U' L U R U' L' // (8-3/23)
^ = R' F' R B R' F R B' // (8-2/29)
Solution: R' F' R B R' F R D2 R L U2 R' U' L U R U' B2 L2 D B D2 B2 D2 B U L U' F' (29)
```

**Up to 10 moves per insertion**: nothing better, 29 stays the best.

</details>

#### 3c1t, skeleton 11

Scramble: `R' U' F D2 L2 R' D2 U2 B2 L' B2 F2 L' R' B2 D' B' F D2 F L2 D B' L R' U' F`

Skeleton: `D2 F' B' L2 B R2 L' U F L2 U2 L2 U' D F L2 B' R2 L` (19)

Left: DFL → UBR → DBR → DFL, DBL twisted counter-clockwise

<details>
<summary>Answer for 3c1t, skeleton 11</summary>

**8 moves or less per insertion** (two comms): +9, 28 in all.

```
^ D2 F' B' L2 B * R2 L' U F L2 U2 L2 U' D F L2 B' R2 L
* = B L' F' L B' L' F L // (8-3/24)
^ = F' U2 F D2 F' U2 F D2 // (8-4/28)
Solution: F' U2 F D2 F' U2 B' L2 B2 L' F' L B' L' F R2 U F L2 U2 L2 U' D F L2 B' R2 L (28)
```

**Up to 10 moves per insertion**: nothing better, 28 stays the best.

</details>

#### 3c1t, skeleton 12

Scramble: `R' U' F R' D2 U2 R2 D2 R B2 L D2 F2 R' D R2 F L' R2 B U F L2 U' R' U' F`

Skeleton: `R' L2 B U D2 R U F2 B2 U2 B2 D2 B2 D' F2 D R U F' U'` (20)

Left: DFL → DBR → UFL → DFL, DFR twisted clockwise

<details>
<summary>Answer for 3c1t, skeleton 12</summary>

**8 moves or less per insertion** (two comms): +10, 30 in all.

```
R' L2 ^ B U D2 R U F2 B2 U2 B2 D2 B2 D' F2 * D R U F' U'
* = L' D R2 D' L D R2 D' // (8-3/25)
^ = D F2 D' B D F2 D' B' // (8-3/30)
Solution: R' L2 D F2 D' B D F2 U D R U F2 B2 U2 B2 D2 B2 D' F2 L' D R2 D' L D R' U F' U' (30)
```

**Up to 10 moves per insertion**: nothing better, 30 stays the best.

</details>

#### 3c1t, skeleton 13

Scramble: `R' U' F U2 B2 L2 F2 R' B2 F2 L' U2 B2 D2 B L2 F U F R2 B' U' B' R' U' F`

Skeleton: `U' B2 L U R' F2 R' B2 R2 B' U' L' B' L2 F2 L2 F' U F U R2` (21)

Left: UBL → UFR → DBR → UBL, UFL twisted clockwise

<details>
<summary>Answer for 3c1t, skeleton 13</summary>

**8 moves or less per insertion** (two comms): +10, 31 in all.

```
U' B2 L U R' F2 R' B2 R2 B' U' L' B' L2 F2 ^ L2 F' U * F U R2
* = U B2 U' F U B2 U' F' // (8-5/24)
^ = F' R' B' R F R' B R // (8-1/31)
Solution: U' B2 L U R' F2 R' B2 R2 B' U' L' B' L2 F R' B' R F R' B R L2 F' U2 B2 U' F U B2 R2 (31)
```

**Up to 10 moves per insertion**: nothing better, 31 stays the best.

</details>

#### 3c1t, skeleton 14

Scramble: `R' U' F U B2 L2 B2 R2 U' R2 D U2 B2 U R' B' F2 R U' R2 D2 U2 L' R' U' F`

Skeleton: `L F' R F' B D' R F2 B' R' B L' U2 F R2 B L2 D' R' D F' D2` (22)

Left: DBL → UBL → UFR → DBL, UBR twisted clockwise

<details>
<summary>Answer for 3c1t, skeleton 14</summary>

**8 moves or less per insertion** (two comms): +9, 31 in all.

```
L F' R F' * B ^ D' R F2 B' R' B L' U2 F R2 B L2 D' R' D F' D2
* = F' U2 F D F' U2 F D' // (8-1/29)
^ = B' D F D' B D F' D' // (8-6/31)
Solution: L F' R F2 U2 F D F' U2 F2 D' B D F' D2 R F2 B' R' B L' U2 F R2 B L2 D' R' D F' D2 (31)
```

**Up to 10 moves per insertion**: nothing better, 31 stays the best.

</details>

#### 3c1t, skeleton 15

Scramble: `R' U' F B2 L2 B' D2 R2 B' U2 F' L2 D2 F U' L2 B' D2 B D2 L B' R' U' F`

Skeleton: `R' B' R' D2 R2 B D2 B L U' B2 R B2 D2 B' U2` (16)

Left: UFL → DFR → UBR → UFL, DBL twisted counter-clockwise

<details>
<summary>Answer for 3c1t, skeleton 15</summary>

**8 moves or less per insertion** (two comms): +11, 27 in all.

```
R' B' R' D2 R2 B D2 B L U' B2 ^ R * B2 D2 B' U2
* = B U2 B' D2 B U2 B' D2 // (8-0/24)
^ = B L2 B' R B L2 B' R' // (8-5/27)
Solution: R' B' R' D2 R2 B D2 B L U' B' L2 B' R B L2 U2 B' D2 B U2 B' D2 B2 D2 B' U2 (27)
```

**Up to 10 moves per insertion** (two comms): +8, 24 in all.

```
R' B' R' D2 R2 B D2 B L U' * B2 R B2 D2 B' ^ U2
* = R D2 B2 L B2 L' D2 B2 R' B2 // (10-8/18)
^ = F' D F U2 F' D' F U2 // (8-2/24)
Solution: R' B' R' D2 R2 B D2 B L U' R D2 B2 L B2 L' F' B' D F U2 F' D' F (24)
```

</details>

#### 3c1t, skeleton 16

Scramble: `R' U' F U' R2 D F2 R2 B2 U2 L2 D' B2 D F2 D' B2 R' D2 F2 D2 R2 U' B' L' D' U R' U' F`

Skeleton: `R' F2 R D' B2 L' U' R D2 R2 U2 B' R' B2 U2 B U2` (17)

Left: DBL → UFR → UBR → DBL, UBL twisted clockwise

<details>
<summary>Answer for 3c1t, skeleton 16</summary>

**8 moves or less per insertion** (two comms): +10, 27 in all.

```
R' F2 ^ R D' B2 L' * U' R D2 R2 U2 B' R' B2 U2 B U2
* = L' U' R U L U' R' U // (8-5/20)
^ = B' L' B R2 B' L B R2 // (8-1/27)
Solution: R' F2 B' L' B R2 B' L B R' D' B2 L2 U' R U L U' D2 R2 U2 B' R' B2 U2 B U2 (27)
```

**Up to 10 moves per insertion**: nothing better, 27 stays the best.

</details>

#### 3c1t, skeleton 17

Scramble: `R' U' F U F2 D' R2 U2 R2 D' R2 F2 R2 U' L2 U' L D' B D' B2 L2 R' B2 U' R' U' F`

Skeleton: `B2 D B2 U2 R F2 L' U' L2 U2 L2 B2 D2 L' F' B2 L' B2` (18)

Left: UFL → UBR → DFR → UFL, DFL twisted counter-clockwise

<details>
<summary>Answer for 3c1t, skeleton 17</summary>

**8 moves or less per insertion** (two comms): +10, 28 in all.

```
B2 D B2 U2 R ^ F2 L' U' L2 U2 L2 B2 D2 * L' F' B2 L' B2
* = D L' U2 L D' L' U2 L // (8-3/23)
^ = R B R' F2 R B' R' F2 // (8-3/28)
Solution: B2 D B2 U2 R2 B R' F2 R B' R' L' U' L2 U2 L2 B2 D' L' U2 L D' L' U2 F' B2 L' B2 (28)
```

**Up to 10 moves per insertion**: nothing better, 28 stays the best.

</details>

#### 3c1t, skeleton 18

Scramble: `R' U' F D2 B2 D L2 R2 U' L2 D2 L2 B2 U' B2 F L B2 R2 U2 R B' U R U' R' U' F`

Skeleton: `D R2 U' B L' B' D' L2 B' U F' R' L2 B D2 F L' U2 R'` (19)

Left: DFL → DBR → UBL → DFL, UBR twisted clockwise

<details>
<summary>Answer for 3c1t, skeleton 18</summary>

**8 moves or less per insertion** (two comms): +8, 27 in all.

```
D R2 * U' B ^ L' B' D' L2 B' U F' R' L2 B D2 F L' U2 R'
* = R' U' L U R U' L' U // (8-3/24)
^ = B' L' F' L B L' F L // (8-5/27)
Solution: D R U' L U R U' L2 F' L B L' F B' D' L2 B' U F' R' L2 B D2 F L' U2 R' (27)
```

**Up to 10 moves per insertion**: nothing better, 27 stays the best.

</details>

#### 3c1t, skeleton 19

Scramble: `R' U' F D' F2 U2 F2 D2 B U2 L2 F R2 B R2 F D2 R' U B D2 B2 D' B U' R' U' F`

Skeleton: `U2 R' F2 R' F2 U' B2 R D2 B R' F' L' B U' F' B2 R2 B L` (20)

Left: DBL → UBL → DFL → DBL, DFR twisted clockwise

<details>
<summary>Answer for 3c1t, skeleton 19</summary>

**8 moves or less per insertion** (two comms): +8, 28 in all.

```
U2 R' F2 R' F2 U' B2 R D2 ^ B R' * F' L' B U' F' B2 R2 B L
* = L' B' L F' L' B L F // (8-5/23)
^ = D' B U2 B' D B U2 B' // (8-3/28)
Solution: U2 R' F2 R' F2 U' B2 R D B U2 B' D B U2 R' L' B' L F' L' B2 U' F' B2 R2 B L (28)
```

**Up to 10 moves per insertion**: nothing better, 28 stays the best.

</details>

#### 3c1t, skeleton 20

Scramble: `R' U' F B' L2 F L2 D2 F R2 F L2 B2 D2 U2 L2 U R' B D L2 B' U' F' D2 R' U' F`

Skeleton: `R L' F2 U R' D F' U' F2 R' U B U' F2 B2 D B2 D2 F B2 U2` (21)

Left: DBL → UBL → UFL → DBL, DFR twisted clockwise

<details>
<summary>Answer for 3c1t, skeleton 20</summary>

**8 moves or less per insertion** (two comms): +11, 32 in all.

```
R L' F2 U ^ R' D F' U' * F2 R' U B U' F2 B2 D B2 D2 F B2 U2
* = R B R' F2 R B' R' F2 // (8-3/26)
^ = U R D2 R' U' R D2 R' // (8-2/32)
Solution: R L' F2 U2 R D2 R' U' R D2 R2 D F' U' R B R' F2 R B' R2 U B U' F2 B2 D B2 D2 F B2 U2 (32)
```

**Up to 10 moves per insertion**: nothing better, 32 stays the best.

</details>

### 2tc

Two corners twisted in place.

#### 2tc, skeleton 1

Scramble: `R' U' F B R2 B' R2 U2 F L2 B' D2 F U2 R2 F' L U2 F2 R B' F2 D R F R' U' F`

Skeleton: `D2 L F2 B R2 U' R' F R2 U' B' U F U' D' F'` (16)

Left: DBL twisted counter-clockwise, DFL twisted clockwise

<details>
<summary>Answer for 2tc, skeleton 1</summary>

**8 moves or less per insertion** (two comms): +9, 25 in all.

```
D2 L F2 B R2 ^ U' R' F R2 U' B' U * F U' D' F'
* = D B2 D' F D B2 D' F' // (8-3/21)
^ = R D R' U' R D' R' U // (8-4/25)
Solution: D2 L F2 B R' D R' U' R D' R2 F R2 U' B' U D B2 D' F D B2 U' D2 F' (25)
```

**Up to 10 moves per insertion** (two comms): +6, 22 in all.

```
D2 L F2 B R2 U' R' F R2 U' B' U * F U' D' F' ^
* = L2 F D' F' D L2 D' F D F' // (10-4/22)
^ = F U F' D F U' F' D' // (8-8/22)
Solution: D2 L F2 B R2 U' R' F R2 U' B' U L2 F D' F' D L2 F U' F' D' (22)
```

</details>

#### 2tc, skeleton 2

Scramble: `R' U' F U2 B2 L2 D2 R2 F R2 B2 U2 F' D2 F' R2 D' F2 L D' L U L R U' R' U' F`

Skeleton: `D R2 F' B' U' L B' U2 D' F D2 L B U2 L D' F` (17)

Left: DBL twisted counter-clockwise, UBR twisted clockwise

<details>
<summary>Answer for 2tc, skeleton 2</summary>

**8 moves or less per insertion** (two comms): +8, 25 in all.

```
D R2 F' B' U' L B' U2 D' F D2 L ^ B * U2 L D' F
* = L D2 L' U2 L D2 L' U2 // (8-5/20)
^ = L2 B R B' L2 B R' B' // (8-3/25)
Solution: D R2 F' B' U' L B' U2 D' F D2 L' B R B' L2 B R' L D2 L' U2 L D F (25)
```

**Up to 10 moves per insertion**: nothing better, 25 stays the best.

</details>

#### 2tc, skeleton 3

Scramble: `R' U' F R2 U2 B F2 L2 D2 L2 F' D2 B2 F' D' B' D2 U' R U2 F L2 B2 U2 R' U' F`

Skeleton: `D2 F' B U' R B2 L F' R2 U2 B' U' R B D B U F'` (18)

Left: DFL twisted clockwise, DFR twisted counter-clockwise

<details>
<summary>Answer for 2tc, skeleton 3</summary>

**8 moves or less per insertion** (two comms): +8, 26 in all.

```
D2 F' B U' R B2 L F' R2 U2 ^ B' U' R B D B * U F'
* = F' D' F U F' D F U' // (8-4/22)
^ = D2 B' U' B D2 B' U B // (8-4/26)
Solution: D2 F' B U' R B2 L F' R2 U2 D2 B' U' B D2 B' R B D F' B D' F U F' D (26)
```

**Up to 10 moves per insertion**: nothing better, 26 stays the best.

</details>

#### 2tc, skeleton 4

Scramble: `R' U' F L2 B2 L2 B2 D' L2 D L2 B2 L2 U B U' F' R B' R' F2 D R' U2 R' U' F`

Skeleton: `B L B2 L U' F2 B' U2 F2 D' R B D B2 R D F U D2` (19)

Left: DFL twisted counter-clockwise, UFR twisted clockwise

<details>
<summary>Answer for 2tc, skeleton 4</summary>

**8 moves or less per insertion** (two comms): +7, 26 in all.

```
B L ^ B2 L * U' F2 B' U2 F2 D' R B D B2 R D F U D2
* = F D' F' U' F D F' U // (8-3/24)
^ = L F' L' B2 L F L' B2 // (8-6/26)
Solution: B L2 F' L' B2 L F2 D' F' U' F D F B' U2 F2 D' R B D B2 R D F U D2 (26)
```

**Up to 10 moves per insertion**: nothing better, 26 stays the best.

</details>

#### 2tc, skeleton 5

Scramble: `R' U' F B2 R' D2 F2 D2 B2 R F2 U2 L D2 R' B2 U R2 B L' F2 R2 U R D B' R' U' F`

Skeleton: `B2 D2 F' R2 D2 B L U2 R U' D2 B2 D2 R B U F' B2 R' F` (20)

Left: UBL twisted counter-clockwise, UFR twisted clockwise

<details>
<summary>Answer for 2tc, skeleton 5</summary>

**8 moves or less per insertion** (two comms): +9, 29 in all.

```
B2 D2 ^ F' R2 D2 B L U2 R U' D2 B2 D2 R * B U F' B2 R' F
* = D' B U B' D B U' B' // (8-5/23)
^ = D B' D' F2 D B D' F2 // (8-2/29)
Solution: B2 D' B' D' F2 D B D' F R2 D2 B L U2 R U' D2 B2 D2 R D' B U B' D F' B' R' F (29)
```

**Up to 10 moves per insertion** (two comms): +8, 28 in all.

```
B2 D2 F' R2 D2 B L U2 R U' D2 B2 D2 R B U F' B2 * R' F
* = F R' U2 R F' R' F U2 F' R // (10-6/24)
B2 D2 F' R2 D2 B L U2 R U' D2 B2 D2 R B U B2 R' U2 R ^ F' R' F U2
^ = R' U2 R' D' R U2 R' D R2 // (9-5/28)
Solution: B2 D2 F' R2 D2 B L U2 R U' D2 B2 D2 R B U B2 R2 D' R U2 R' D R2 F' R' F U2 (28)
```

</details>

#### 2tc, skeleton 6

Scramble: `R' U' F R D2 L U2 L' U2 B2 L' B2 R2 B2 U2 L' F2 D R2 B D2 U' R' U' L' D B R' U' F`

Skeleton: `U B U L U' L2 B U' D R U2 F2 D' B R2 U F' R2 L2 D B` (21)

Left: DFL twisted counter-clockwise, DFR twisted clockwise

<details>
<summary>Answer for 2tc, skeleton 6</summary>

**8 moves or less per insertion** (two comms): +9, 30 in all.

```
U B U L U' L2 B U' D R U2 F2 ^ D' B R2 U * F' R2 L2 D B
* = R F' L F R' F' L' F // (8-3/26)
^ = B U2 B' D' B U2 B' D // (8-4/30)
Solution: U B U L U' L2 B U' D R U2 F2 B U2 B' D' B U2 R2 U R F' L F R' F' R2 L D B (30)
```

**Up to 10 moves per insertion**: nothing better, 30 stays the best.

</details>

#### 2tc, skeleton 7

Scramble: `R' U' F L2 B' L2 F D2 L2 D2 U2 F' L2 R' B2 F L D2 U2 R U F' U R' U' F`

Skeleton: `U2 R F B2 U D2 F2 D B' U' R' D R2 F' U2 L' F' R2 F' L2 F' B` (22)

Left: UBL twisted counter-clockwise, DBR twisted clockwise

<details>
<summary>Answer for 2tc, skeleton 7</summary>

**8 moves or less per insertion** (two comms): +7, 29 in all.

```
U2 R F B2 U D2 F2 D ^ B' U' R' D R2 F' U2 * L' F' R2 F' L2 F' B
* = F' R F L' F' R' F L // (8-5/25)
^ = D2 B' U2 B D2 B' U2 B // (8-4/29)
Solution: U2 R F B2 U D2 F2 D' B' U2 B D2 B' U R' D R2 F' U2 F' R F L' F' R F' L2 F' B (29)
```

**Up to 10 moves per insertion**: nothing better, 29 stays the best.

</details>

#### 2tc, skeleton 8

Scramble: `R' U' F L F2 L B2 D2 R F2 L2 D2 L2 U2 B' U B2 U2 R' D2 L' D U2 R' U' F`

Skeleton: `L' F' R2 D B2 D2 B' R B2 L2 B2 L U B2 U2 D'` (16)

Left: DFL twisted counter-clockwise, UBR twisted clockwise

<details>
<summary>Answer for 2tc, skeleton 8</summary>

**8 moves or less per insertion** (two comms): +8, 24 in all.

```
L' * F' R2 D ^ B2 D2 B' R B2 L2 B2 L U B2 U2 D'
* = L' F' R' F L F' R F // (8-4/20)
^ = D F D' B2 D F' D' B2 // (8-4/24)
Solution: L2 F' R' F L F' R' D2 F D' B2 D F' D B' R B2 L2 B2 L U B2 U2 D' (24)
```

**Up to 10 moves per insertion**: nothing better, 24 stays the best.

</details>

#### 2tc, skeleton 9

Scramble: `R' U' F R2 D' L2 D F2 L2 R2 U' L2 U B2 D2 B' R B2 D2 L' R U2 L2 F' R' U' F`

Skeleton: `D2 F2 B' R2 B' U L' U' F B' R F' U F2 L F2 L2` (17)

Left: UBR twisted clockwise, UFR twisted counter-clockwise

<details>
<summary>Answer for 2tc, skeleton 9</summary>

**8 moves or less per insertion** (two comms): +8, 25 in all.

```
D2 F2 B' R2 B' U L' U' F B' ^ R F' * U F2 L F2 L2
* = R' D' R U2 R' D R U2 // (8-1/24)
^ = B2 R F' R' B2 R F R' // (8-7/25)
Solution: D2 F2 B' R2 B' U L' U' F B R F' R' B2 D' R U2 R' D R U' F2 L F2 L2 (25)
```

**Up to 10 moves per insertion** (two comms): +7, 24 in all.

```
D2 F2 B' R2 B' ^ U L' U' F B' R F' U * F2 L F2 L2
* = U2 R' F2 R F2 U2 L F2 L' F2 // (10-8/19)
^ = U2 L' D2 L U' L' D2 L U' // (9-4/24)
Solution: D2 F2 B' R2 B' U2 L' D2 L U' L' U' D2 F B' R F' U' R' F2 R F2 U2 L' (24)
```

</details>

#### 2tc, skeleton 10

Scramble: `R' U' F R2 U2 B2 L' F2 L' B2 R D2 F2 D2 R2 U F' L' D' B F U F' U' F2 R' U' F`

Skeleton: `B D2 R L U L B2 L2 D B D2 B2 D2 B U L U' F'` (18)

Left: DFL twisted clockwise, UFL twisted counter-clockwise

<details>
<summary>Answer for 2tc, skeleton 10</summary>

**8 moves or less per insertion** (two comms): +8, 26 in all.

```
* B D2 ^ R L U L B2 L2 D B D2 B2 D2 B U L U' F'
* = L F2 L' B L F2 L' B' // (8-2/24)
^ = D2 L U L' D2 L U' L' // (8-6/26)
Solution: L F2 L' B L F2 U L' D2 L U' R U L B2 L2 D B D2 B2 D2 B U L U' F' (26)
```

**Up to 10 moves per insertion**: nothing better, 26 stays the best.

</details>

#### 2tc, skeleton 11

Scramble: `R' U' F U' B2 L2 F2 U2 R2 D' R2 F2 D F2 L2 U L2 B D' R D2 F2 L U' R U R' U' F`

Skeleton: `D2 F' B' L2 B R2 L' U F L2 U2 L2 U' D F L2 B' R2 L` (19)

Left: DBR twisted counter-clockwise, UFR twisted clockwise

<details>
<summary>Answer for 2tc, skeleton 11</summary>

**8 moves or less per insertion** (two comms): +9, 28 in all.

```
D2 F' ^ B' L2 * B R2 L' U F L2 U2 L2 U' D F L2 B' R2 L
* = R' B L2 B' R B L2 B' // (8-3/24)
^ = L B' R' B L' B' R B // (8-4/28)
Solution: D2 F' L B' R' B L' B' L2 B L2 B' R B R2 L U F L2 U2 L2 U' D F L2 B' R2 L (28)
```

**Up to 10 moves per insertion** (two comms): +8, 27 in all.

```
D2 F' B' L2 B ^ R2 * L' U F L2 U2 L2 U' D F L2 B' R2 L
* = U L' F2 L U' L' U F2 U' L // (10-5/24)
^ = R' U L' U' R' U L U' R2 // (9-6/27)
Solution: D2 F' B' L2 B R' U L' U' R' U F2 L U' L' U F' L2 U2 L2 U' D F L2 B' R2 L (27)
```

</details>

#### 2tc, skeleton 12

Scramble: `R' U' F U' R2 D2 L2 B2 D' R2 D R2 B2 U R B F U' R' B' L2 D' L2 D2 R' U' F`

Skeleton: `R' L2 B U D2 R U F2 B2 U2 B2 D2 B2 D' F2 D R U F' U'` (20)

Left: DFL twisted clockwise, UBL twisted counter-clockwise

<details>
<summary>Answer for 2tc, skeleton 12</summary>

**8 moves or less per insertion** (two comms): +8, 28 in all.

```
R' L2 B U D2 R U ^ F2 B2 U2 B2 D2 * B2 D' F2 D R U F' U'
* = D' F D B2 D' F' D B2 // (8-6/22)
^ = U2 F D' F' U2 F D F' // (8-2/28)
Solution: R' L2 B U D2 R U' F D' F' U2 F D F B2 U2 B2 D F D B2 D' F D R U F' U' (28)
```

**Up to 10 moves per insertion**: nothing better, 28 stays the best.

</details>

#### 2tc, skeleton 13

Scramble: `R' U' F R2 U R2 B2 U' B2 L2 D' L2 U B2 U' B F2 R' F D L B L' F' R' U' R' U' F`

Skeleton: `U' B2 L U R' F2 R' B2 R2 B' U' L' B' L2 F2 L2 F' U F U R2` (21)

Left: UFL twisted counter-clockwise, UFR twisted clockwise

<details>
<summary>Answer for 2tc, skeleton 13</summary>

**8 moves or less per insertion** (two comms): +7, 28 in all.

```
U' B2 L ^ U R' F2 * R' B2 R2 B' U' L' B' L2 F2 L2 F' U F U R2
* = F R' B2 R F' R' B2 R // (8-6/23)
^ = L D L' U L D' L' U' // (8-3/28)
Solution: U' B2 L2 D L' U L D' R' L' F' R' B2 R F' R B' U' L' B' L2 F2 L2 F' U F U R2 (28)
```

**Up to 10 moves per insertion**: nothing better, 28 stays the best.

</details>

#### 2tc, skeleton 14

Scramble: `R' U' F U L2 B2 L2 F2 U B2 U' B2 U R2 B D' B' D' L F' L B2 L U' R' U' F`

Skeleton: `L F' R F' B D' R F2 B' R' B L' U2 F R2 B L2 D' R' D F' D2` (22)

Left: DBL twisted counter-clockwise, UFL twisted clockwise

<details>
<summary>Answer for 2tc, skeleton 14</summary>

**8 moves or less per insertion** (two comms): +7, 29 in all.

```
L F' R ^ F' B D' R F2 B' * R' B L' U2 F R2 B L2 D' R' D F' D2
* = F2 R' B R F2 R' B' R // (8-6/24)
^ = R2 F' L F R2 F' L' F // (8-3/29)
Solution: L F' R' F' L F R2 F' L' B D' R B' R' B R F2 R' L' U2 F R2 B L2 D' R' D F' D2 (29)
```

**Up to 10 moves per insertion**: nothing better, 29 stays the best.

</details>

#### 2tc, skeleton 15

Scramble: `R' U' F B2 L2 F U2 L2 R2 U2 B2 R2 D2 F' D2 B' U' L' D2 B' D2 F L F' R' U' F`

Skeleton: `R' B' R' D2 R2 B D2 B L U' B2 R B2 D2 B' U2` (16)

Left: DFL twisted clockwise, UBL twisted counter-clockwise

<details>
<summary>Answer for 2tc, skeleton 15</summary>

**8 moves or less per insertion** (two comms): +8, 24 in all.

```
R' B' R' D2 R2 B D2 ^ B L U' B2 R B2 D2 * B' U2
* = D' B' U2 B D B' U2 B // (8-5/19)
^ = D' F' D B D' F D B' // (8-3/24)
Solution: R' B' R' D2 R2 B D F' D B D' F D L U' B2 R B2 D B' U2 B D B' (24)
```

**Up to 10 moves per insertion**: nothing better, 24 stays the best.

</details>

#### 2tc, skeleton 16

Scramble: `R' U' F D2 U2 B2 R' U2 L2 D2 L2 D2 L' D' B F2 L2 R F2 R2 D' B R' U' F`

Skeleton: `R' F2 R D' B2 L' U' R D2 R2 U2 B' R' B2 U2 B U2` (17)

Left: UFL twisted clockwise, DBR twisted counter-clockwise

<details>
<summary>Answer for 2tc, skeleton 16</summary>

**8 moves or less per insertion** (two comms): +8, 25 in all.

```
R' F2 R D' B2 L' U' R D2 R2 U2 * B' ^ R' B2 U2 B U2
* = U R U' L U R' U' L' // (8-1/24)
^ = B L B' R' B L' B' R // (8-7/25)
Solution: R' F2 R D' B2 L' U' R D2 R2 U' R U' L U R' U' B' R' B L' B U2 B U2 (25)
```

**Up to 10 moves per insertion**: nothing better, 25 stays the best.

</details>

#### 2tc, skeleton 17

Scramble: `R' U' F B2 U' B2 U L2 U' R2 B2 L2 D2 L2 U F' R2 B' D' L' R' F' L F U' R' U' F`

Skeleton: `B2 D B2 U2 R F2 L' U' L2 U2 L2 B2 D2 L' F' B2 L' B2` (18)

Left: DBL twisted counter-clockwise, DBR twisted clockwise

<details>
<summary>Answer for 2tc, skeleton 17</summary>

**8 moves or less per insertion** (two comms): +8, 26 in all.

```
B2 D B2 U2 ^ R F2 L' U' L2 U2 L2 B2 D2 L' F' B2 * L' B2
* = F L' B L F' L' B' L // (8-5/21)
^ = U' R D' R' U R D R' // (8-3/26)
Solution: B2 D B2 U R D' R' U R D F2 L' U' L2 U2 L2 B2 D2 L' B2 L' B L F' L' B (26)
```

**Up to 10 moves per insertion**: nothing better, 26 stays the best.

</details>

#### 2tc, skeleton 18

Scramble: `R' U' F U' B R2 B2 D2 F U2 F' D2 B' D2 L2 F2 D U2 B' U L' R' D' L' D2 R' D' R' U' F`

Skeleton: `D R2 U' B L' B' D' L2 B' U F' R' L2 B D2 F L' U2 R'` (19)

Left: DBR twisted clockwise, DFR twisted counter-clockwise

<details>
<summary>Answer for 2tc, skeleton 18</summary>

**8 moves or less per insertion** (two comms): +9, 28 in all.

```
D R2 U' B L' B' D' L2 ^ B' U F' R' L2 B D2 F L' * U2 R'
* = R' D' R U2 R' D R U2 // (8-4/23)
^ = D B' U' B D' B' U B // (8-3/28)
Solution: D R2 U' B L' B' D' L2 D B' U' B D' B' U2 F' R' L2 B D2 F R' L' D' R U2 R' D (28)
```

**Up to 10 moves per insertion**: nothing better, 28 stays the best.

</details>

#### 2tc, skeleton 19

Scramble: `R' U' F U' L2 F L2 F R2 F2 R2 U2 B U2 F U2 B U' B' R' U L' D2 L' U' R' U' F`

Skeleton: `U2 R' F2 R' F2 U' B2 R D2 B R' F' L' B U' F' B2 R2 B L` (20)

Left: UFL twisted counter-clockwise, DBR twisted clockwise

<details>
<summary>Answer for 2tc, skeleton 19</summary>

**8 moves or less per insertion** (two comms): +8, 28 in all.

```
U2 R' ^ F2 R' F2 U' B2 R D2 * B R' F' L' B U' F' B2 R2 B L
* = D F2 D' B D F2 D' B' // (8-3/25)
^ = R' B' R F2 R' B R F2 // (8-5/28)
Solution: U2 R2 B' R F2 R' F2 B U' B2 R D' F2 D' B D F2 D' R' F' L' B U' F' B2 R2 B L (28)
```

**Up to 10 moves per insertion**: nothing better, 28 stays the best.

</details>

#### 2tc, skeleton 20

Scramble: `R' U' F U' R2 D2 L2 D' F2 D' L2 B2 D' B2 U' F' D' L' D' U B' D' L2 F R' U' F`

Skeleton: `R L' F2 U R' D F' U' F2 R' U B U' F2 B2 D B2 D2 F B2 U2` (21)

Left: UBL twisted clockwise, UBR twisted counter-clockwise

<details>
<summary>Answer for 2tc, skeleton 20</summary>

**8 moves or less per insertion** (two comms): +7, 28 in all.

```
R L' ^ F2 U R' D F' U' F2 R' U B U' F2 B2 * D B2 D2 F B2 U2
* = F2 D B2 D' F2 D B2 D' // (8-7/22)
^ = R' U2 R D2 R' U2 R D2 // (8-2/28)
Solution: L' U2 R D2 R' U2 R D2 F2 U R' D F' U' F2 R' U B U' B2 D B2 D' F2 D' F B2 U2 (28)
```

**Up to 10 moves per insertion**: nothing better, 28 stays the best.

</details>

### 3tc

Three corners twisted in place, all the same way.

#### 3tc, skeleton 1

Scramble: `R' U' F B' D2 B L2 B' L2 U2 L2 R2 B' D2 R2 F' L' U2 R F2 R B' D R F R' U' F`

Skeleton: `D2 L F2 B R2 U' R' F R2 U' B' U F U' D' F'` (16)

Left: DBL twisted clockwise, DFL twisted clockwise, UBL twisted clockwise

<details>
<summary>Answer for 3tc, skeleton 1</summary>

**8 moves or less per insertion** (two comms): +9, 25 in all.

```
D2 L F2 B R2 ^ U' R' F R2 U' * B' U F U' D' F'
* = D2 B' U B D2 B' U' B // (8-4/20)
^ = R' U' L U R U' L' U // (8-3/25)
Solution: D2 L F2 B R U' L U R U' R' L' F R2 U' D2 B' U B D2 F B' U' D' F' (25)
```

**Up to 10 moves per insertion**: nothing better, 25 stays the best.

</details>

#### 3tc, skeleton 2

Scramble: `R' U' F D2 F' U2 B R2 B' R2 D2 B' F' L2 U2 L B2 D' L2 R2 F2 R U' F2 R' U' F`

Skeleton: `D R2 F' B' U' L B' U2 D' F D2 L B U2 L D' F` (17)

Left: DBL twisted clockwise, DFL twisted clockwise, UFR twisted clockwise

<details>
<summary>Answer for 3tc, skeleton 2</summary>

**8 moves or less per insertion** (two comms): +10, 27 in all.

```
D R2 F' B' U' L B' U2 ^ D' F * D2 L B U2 L D' F
* = L' U L D2 L' U' L D2 // (8-3/22)
^ = B D' F2 D B' D' F2 D // (8-3/27)
Solution: D R2 F' B' U' L B' U2 B D' F2 D B' D' F' L' U L D2 L' U' L2 B U2 L D' F (27)
```

**Up to 10 moves per insertion**: nothing better, 27 stays the best.

</details>

#### 3tc, skeleton 3

Scramble: `R' U' F U' B2 R2 D L2 R2 D' R2 D' L2 U L2 D' L B R2 D2 L' U2 B U' B2 L' R' U' F`

Skeleton: `D2 F' B U' R B2 L F' R2 U2 B' U' R B D B U F'` (18)

Left: UBL twisted counter-clockwise, UFL twisted counter-clockwise, UBR twisted counter-clockwise

<details>
<summary>Answer for 3tc, skeleton 3</summary>

**8 moves or less per insertion** (two comms): +9, 27 in all.

```
D2 F' B ^ U' R B2 * L F' R2 U2 B' U' R B D B U F'
* = B R2 B' L B R2 B' L' // (8-3/23)
^ = L' U' R U L U' R' U // (8-4/27)
Solution: D2 F' B L' U' R U L U' B' R2 B' L B R2 F' B' R2 U2 B' U' R B D B U F' (27)
```

**Up to 10 moves per insertion**: nothing better, 27 stays the best.

</details>

#### 3tc, skeleton 4

Scramble: `R' U' F L2 B D2 F U2 F' L2 F D2 R2 F L2 D' L2 R' D B2 U' B2 F D' R' U' F`

Skeleton: `B L B2 L U' F2 B' U2 F2 D' R B D B2 R D F U D2` (19)

Left: UBL twisted clockwise, DBR twisted clockwise, DFR twisted clockwise

<details>
<summary>Answer for 3tc, skeleton 4</summary>

**8 moves or less per insertion** (two comms): +11, 30 in all.

```
B L B2 L U' F2 B' U2 F2 D' R B D B2 ^ R * D F U D2
* = B' D F D' B D F' D' // (8-5/22)
^ = L' U2 L D L' U2 L D' // (8-0/30)
Solution: B L B2 L U' F2 B' U2 F2 D' R B D B2 L' U2 L D L' U2 L D' R B' D F D' B U D' (30)
```

**Up to 10 moves per insertion**: nothing better, 30 stays the best.

</details>

#### 3tc, skeleton 5

Scramble: `R' U' F U2 B2 R' F2 U2 B2 D2 L2 R F2 L2 B2 U B' L U2 B' D' F U' L2 R' U' F`

Skeleton: `B2 D2 F' R2 D2 B L U2 R U' D2 B2 D2 R B U F' B2 R' F` (20)

Left: UBL twisted clockwise, UBR twisted clockwise, UFR twisted clockwise

<details>
<summary>Answer for 3tc, skeleton 5</summary>

**8 moves or less per insertion** (two comms): +10, 30 in all.

```
B2 D2 F' R2 D2 B L U2 R U' D2 B2 D2 R ^ B U F' * B2 R' F
* = R F2 R' B2 R F2 R' B2 // (8-3/25)
^ = D' B U2 B' D B U2 B' // (8-3/30)
Solution: B2 D2 F' R2 D2 B L U2 R U' D2 B2 D2 R D' B U2 B' D B U' F' R F2 R' B2 R F2 R2 F (30)
```

**Up to 10 moves per insertion**: nothing better, 30 stays the best.

</details>

#### 3tc, skeleton 6

Scramble: `R' U' F B2 D R2 B2 R2 D F2 D2 U' F2 U' L' B2 R2 D' F' L2 R' B L' D R' U' F`

Skeleton: `U B U L U' L2 B U' D R U2 F2 D' B R2 U F' R2 L2 D B` (21)

Left: UBL twisted clockwise, UFL twisted clockwise, UBR twisted clockwise

<details>
<summary>Answer for 3tc, skeleton 6</summary>

**8 moves or less per insertion** (two comms): +7, 28 in all.

```
U ^ B U L U' L2 B U' D R U2 F2 D' B R2 U * F' R2 L2 D B
* = L' F' R2 F L F' R2 F // (8-4/25)
^ = U F2 U' B U F2 U' B' // (8-5/28)
Solution: U2 F2 U' B U F2 L U' L2 B U' D R U2 F2 D' B R2 U L' F' R2 F L F' L2 D B (28)
```

**Up to 10 moves per insertion**: nothing better, 28 stays the best.

</details>

#### 3tc, skeleton 7

Scramble: `R' U' F R2 D2 L2 U2 R' B2 F2 D2 L' D2 R U' B2 U L' F L' U2 B' L R' U' F`

Skeleton: `U2 R F B2 U D2 F2 D B' U' R' D R2 F' U2 L' F' R2 F' L2 F' B` (22)

Left: DBL twisted clockwise, UFL twisted clockwise, UFR twisted clockwise

<details>
<summary>Answer for 3tc, skeleton 7</summary>

**8 moves or less per insertion** (two comms): +10, 32 in all.

```
U2 R F B2 U D2 F2 D ^ B' U' R' D R2 F' U2 L' F' R2 F' L2 F' B *
* = F U' B2 U F' U' B2 U // (8-2/28)
^ = U' F' U B' U' F U B // (8-4/32)
Solution: U2 R F B2 U D2 F2 U' D F' U B' U' F R' D R2 F' U2 L' F' R2 F' L2 B U' B2 U F' U' B2 U (32)
```

**Up to 10 moves per insertion**: nothing better, 32 stays the best.

</details>

#### 3tc, skeleton 8

Scramble: `R' U' F R2 F' U2 F' D2 R2 F L2 U2 B' U2 L2 F2 D L' F R U' L' D' U R' U' F`

Skeleton: `L' F' R2 D B2 D2 B' R B2 L2 B2 L U B2 U2 D'` (16)

Left: DBL twisted clockwise, UFL twisted clockwise, DBR twisted clockwise

<details>
<summary>Answer for 3tc, skeleton 8</summary>

**8 moves or less per insertion** (two comms): +11, 27 in all.

```
L' F' R2 D B2 D2 B' R B2 L2 B2 L U * B2 U2 D'
* = U F2 U' B2 U F2 U' B2 // (8-4/20)
L' F' R2 D B2 D2 B' R B2 L2 B2 L U2 F2 U' B2 U F2 ^ U D'
^ = L' D R' D' L D R D' // (8-1/27)
Solution: L' F' R2 D B2 D2 B' R B2 L2 B2 L U2 F2 U' B2 U F2 L' D R' D' L D R U D2 (27)
```

**Up to 10 moves per insertion**: nothing better, 27 stays the best.

</details>

#### 3tc, skeleton 9

Scramble: `R' U' F D2 F2 R2 F U2 L2 R2 B2 U2 R2 F' L2 B' U B2 U2 L2 B R B' F' D' R' U' F`

Skeleton: `D2 F2 B' R2 B' U L' U' F B' R F' U F2 L F2 L2` (17)

Left: DFL twisted counter-clockwise, UFL twisted counter-clockwise, DFR twisted counter-clockwise

<details>
<summary>Answer for 3tc, skeleton 9</summary>

**8 moves or less per insertion** (two comms): +8, 25 in all.

```
D2 F2 B' R2 B' U L' U' F B' * R F' U ^ F2 L F2 L2
* = F' L2 F R F' L2 F R' // (8-6/19)
^ = U2 F D2 F' U2 F D2 F' // (8-2/25)
Solution: D2 F2 B' R2 B' U L' U' B' L2 F R F' L2 U' F D2 F' U2 F D2 F L F2 L2 (25)
```

**Up to 10 moves per insertion**: nothing better, 25 stays the best.

</details>

#### 3tc, skeleton 10

Scramble: `R' U' F B2 L2 R2 D2 U' R2 U' B2 F2 D' F2 L' R' B R' F' D' U B F2 D' R' U' F`

Skeleton: `B D2 R L U L B2 L2 D B D2 B2 D2 B U L U' F'` (18)

Left: DBL twisted counter-clockwise, UBL twisted counter-clockwise, DFR twisted counter-clockwise

<details>
<summary>Answer for 3tc, skeleton 10</summary>

**8 moves or less per insertion** (two comms): +11, 29 in all.

```
B D2 R L U ^ L B2 L2 D B D2 * B2 D2 B U L U' F'
* = D F2 D' B D F2 D' B' // (8-2/24)
^ = F2 L B' L' F2 L B L' // (8-3/29)
Solution: B D2 R L U F2 L B' L' F2 L B' L2 D B D' F2 D' B D F2 D' B D2 B U L U' F' (29)
```

**Up to 10 moves per insertion**: nothing better, 29 stays the best.

</details>

#### 3tc, skeleton 11

Scramble: `R' U' F U' R2 B2 D L2 U F2 D R2 U' B2 U2 L' U' B' F2 D F R U2 R F R' U' F`

Skeleton: `D2 F' B' L2 B R2 L' U F L2 U2 L2 U' D F L2 B' R2 L` (19)

Left: DBR twisted clockwise, DFR twisted clockwise, UBR twisted clockwise

<details>
<summary>Answer for 3tc, skeleton 11</summary>

**8 moves or less per insertion** (two comms): +10, 29 in all.

```
D2 ^ F' B' L2 * B R2 L' U F L2 U2 L2 U' D F L2 B' R2 L
* = L' F' L B L' F L B' // (8-5/22)
^ = D' R2 D L2 D' R2 D L2 // (8-1/29)
Solution: D R2 D L2 D' R2 D L2 F' B' L F' L B L' F R2 U F L2 U2 L2 U' D F L2 B' R2 L (29)
```

**Up to 10 moves per insertion**: nothing better, 29 stays the best.

</details>

#### 3tc, skeleton 12

Scramble: `R' U' F D2 B' R2 U2 B2 D2 F' U2 F D2 B' L2 U2 R' U B L2 F R2 U' R B' R' U' F`

Skeleton: `R' L2 B U D2 R U F2 B2 U2 B2 D2 B2 D' F2 D R U F' U'` (20)

Left: DBL twisted counter-clockwise, UBL twisted counter-clockwise, DBR twisted counter-clockwise

<details>
<summary>Answer for 3tc, skeleton 12</summary>

**8 moves or less per insertion** (two comms): +12, 32 in all.

```
R' L2 B U D2 ^ R U F2 B2 U2 B2 D2 B2 D' F2 D * R U F' U'
* = U R D' R' U' R D R' // (8-2/26)
^ = D' L2 D R' D' L2 D R // (8-2/32)
Solution: R' L2 B U D L2 D R' D' L2 D R2 U F2 B2 U2 B2 D2 B2 D' F2 U D R D' R' U' R U D F' U' (32)
```

**Up to 10 moves per insertion**: nothing better, 32 stays the best.

</details>

#### 3tc, skeleton 13

Scramble: `R' U' F U' D2 B' U2 F L2 B2 U2 L2 D2 L2 F D2 F L U2 B' L2 B D' L B U2 R' U' F`

Skeleton: `U' B2 L U R' F2 R' B2 R2 B' U' L' B' L2 F2 L2 F' U F U R2` (21)

Left: UFL twisted clockwise, DFR twisted clockwise, UBR twisted clockwise

<details>
<summary>Answer for 3tc, skeleton 13</summary>

**8 moves or less per insertion** (two comms): +10, 31 in all.

```
U' B2 L U R' F2 R' B2 R2 B' ^ U' L' B' L2 F2 L2 F' * U F U R2
* = R' U L U' R U L' U' // (8-2/27)
^ = L' D L U' L' D' L U // (8-4/31)
Solution: U' B2 L U R' F2 R' B2 R2 B' L' D L U' L' D' B' L2 F2 L2 F' R' U L U' R U L' F U R2 (31)
```

**Up to 10 moves per insertion**: nothing better, 31 stays the best.

</details>

#### 3tc, skeleton 14

Scramble: `R' U' F L2 B2 D2 R B2 R2 B2 U2 R D2 R2 F U' L2 U L D2 F L2 D U' R' U' F`

Skeleton: `L F' R F' B D' R F2 B' R' B L' U2 F R2 B L2 D' R' D F' D2` (22)

Left: DFL twisted clockwise, DBR twisted clockwise, DFR twisted clockwise

<details>
<summary>Answer for 3tc, skeleton 14</summary>

**8 moves or less per insertion** (two comms): +11, 33 in all.

```
L F' R F' B D' R F2 B' R' B L' U2 F R2 ^ B L2 D' R' * D F' D2
* = R' U2 R D R' U2 R D' // (8-3/27)
^ = D F2 D' B D F2 D' B' // (8-2/33)
Solution: L F' R F' B D' R F2 B' R' B L' U2 F R2 D F2 D' B D F2 D' L2 D' R2 U2 R D R' U2 R F' D2 (33)
```

**Up to 10 moves per insertion**: nothing better, 33 stays the best.

</details>

#### 3tc, skeleton 15

Scramble: `R' U' F R2 U' R2 U L2 R2 U L2 R2 F2 U2 L2 F' D2 F2 L' R2 F U L2 R' U' F`

Skeleton: `R' B' R' D2 R2 B D2 B L U' B2 R B2 D2 B' U2` (16)

Left: DFL twisted counter-clockwise, UBR twisted counter-clockwise, UFR twisted counter-clockwise

<details>
<summary>Answer for 3tc, skeleton 15</summary>

**8 moves or less per insertion** (two comms): +8, 24 in all.

```
R' B' R' D2 R2 B D2 B * L U' B2 ^ R B2 D2 B' U2
* = D L U' L' D' L U L' // (8-4/20)
^ = B2 R F2 R' B2 R F2 R' // (8-4/24)
Solution: R' B' R' D2 R2 B D2 B D L U' L' D' R L F2 R' B2 R F2 B2 D2 B' U2 (24)
```

**Up to 10 moves per insertion**: nothing better, 24 stays the best.

</details>

#### 3tc, skeleton 16

Scramble: `R' U' F L2 D R2 D U B2 R2 B2 L2 D' B2 U' R B2 L2 U' B' L' D' L2 U2 L2 U' R' U' F`

Skeleton: `R' F2 R D' B2 L' U' R D2 R2 U2 B' R' B2 U2 B U2` (17)

Left: DBL twisted counter-clockwise, DFR twisted counter-clockwise, UBR twisted counter-clockwise

<details>
<summary>Answer for 3tc, skeleton 16</summary>

**8 moves or less per insertion** (two comms): +8, 25 in all.

```
^ R' F2 R D' B2 L' U' R D2 * R2 U2 B' R' B2 U2 B U2
* = F' L F R2 F' L' F R2 // (8-2/23)
^ = B R' F2 R B' R' F2 R // (8-6/25)
Solution: B R' F2 R B' D' B2 L' U' R D2 F' L F R2 F' L' F U2 B' R' B2 U2 B U2 (25)
```

**Up to 10 moves per insertion**: nothing better, 25 stays the best.

</details>

#### 3tc, skeleton 17

Scramble: `R' U' F L2 U2 L B2 R U2 R2 U2 B2 R' B2 L2 F' U L D' L F2 R' B L2 D' R' U' F`

Skeleton: `B2 D B2 U2 R F2 L' U' L2 U2 L2 B2 D2 L' F' B2 L' B2` (18)

Left: DBL twisted clockwise, DFL twisted clockwise, DFR twisted clockwise

<details>
<summary>Answer for 3tc, skeleton 17</summary>

**8 moves or less per insertion** (two comms): +9, 27 in all.

```
B2 ^ D B2 U2 R F2 L' U' L2 U2 L2 B2 D2 L' F' * B2 L' B2
* = L' F L B2 L' F' L B2 // (8-4/22)
^ = B' D F' D' B D F D' // (8-3/27)
Solution: B D F' D' B D F B2 U2 R F2 L' U' L2 U2 L2 B2 D2 L' F' L' F L B2 L' F' B2 (27)
```

**Up to 10 moves per insertion**: nothing better, 27 stays the best.

</details>

#### 3tc, skeleton 18

Scramble: `R' U' F D2 U2 B2 F2 R' B2 R' D2 R F2 R F2 U F' D2 B' F' U R2 D2 B R' U' F`

Skeleton: `D R2 U' B L' B' D' L2 B' U F' R' L2 B D2 F L' U2 R'` (19)

Left: UFL twisted counter-clockwise, DFR twisted counter-clockwise, UFR twisted counter-clockwise

<details>
<summary>Answer for 3tc, skeleton 18</summary>

**8 moves or less per insertion** (two comms): +10, 29 in all.

```
D R2 ^ U' B L' B' D' L2 B' U F' R' L2 B D2 F * L' U2 R'
* = F R' F' L' F R F' L // (8-3/24)
^ = R' D' R U' R' D R U // (8-3/29)
Solution: D R D' R U' R' D R B L' B' D' L2 B' U F' R' L2 B D2 F2 R' F' L' F R F' U2 R' (29)
```

**Up to 10 moves per insertion**: nothing better, 29 stays the best.

</details>

#### 3tc, skeleton 19

Scramble: `R' U' F U' F2 L' B2 R' F2 L' U2 R2 U2 B2 R' F2 D U2 F2 D' F' L R B2 D2 R2 U' R' U' F`

Skeleton: `U2 R' F2 R' F2 U' B2 R D2 B R' F' L' B U' F' B2 R2 B L` (20)

Left: DBL twisted clockwise, DFR twisted clockwise, UBR twisted clockwise

<details>
<summary>Answer for 3tc, skeleton 19</summary>

**8 moves or less per insertion** (two comms): +8, 28 in all.

```
U2 R' F2 R' F2 U' B2 R D2 ^ B R' F' L' * B U' F' B2 R2 B L
* = U' F2 U B U' F2 U B' // (8-5/23)
^ = L B R B' L' B R' B' // (8-3/28)
Solution: U2 R' F2 R' F2 U' B2 R D2 L B R B' L' B R2 F' L' U' F2 U B U' F B2 R2 B L (28)
```

**Up to 10 moves per insertion**: nothing better, 28 stays the best.

</details>

#### 3tc, skeleton 20

Scramble: `R' U' F B2 R2 F2 U B2 U B2 L2 F2 U B2 L R2 B' D' L2 R2 B' D F' R' F' R' U' F`

Skeleton: `R L' F2 U R' D F' U' F2 R' U B U' F2 B2 D B2 D2 F B2 U2` (21)

Left: UBL twisted counter-clockwise, DFR twisted counter-clockwise, UFR twisted counter-clockwise

<details>
<summary>Answer for 3tc, skeleton 20</summary>

**8 moves or less per insertion** (two comms): +11, 32 in all.

```
R L' F2 U R' D ^ F' U' F2 R' U B U' F2 B2 D B2 D2 F B2 * U2
* = B D2 B' U2 B D2 B' U2 // (8-3/26)
^ = R2 F' L' F R2 F' L F // (8-2/32)
Solution: R L' F2 U R' D R2 F' L' F R2 F' L U' F2 R' U B U' F2 B2 D B2 D2 F B' D2 B' U2 B D2 B' (32)
```

**Up to 10 moves per insertion** (two comms): +9, 30 in all.

```
R L' F2 ^ U R' * D F' U' F2 R' U B U' F2 B2 D B2 D2 F B2 U2
* = U D B2 U' F' U B2 U' F D' // (10-5/26)
^ = F U F' R' F U' F' U R U' // (10-6/30)
Solution: R L' F' U F' R' F U' F' U2 D B2 U' F' U B2 U2 F2 R' U B U' F2 B2 D B2 D2 F B2 U2 (30)
```

</details>

### 3e

An edge 3-cycle.

#### 3e, skeleton 1

Scramble: `R' U' F L' D2 F2 R2 B2 L D2 L' D2 R' D2 R2 U' R2 B L F' L2 R F R' U' F`

Skeleton: `D2 L F2 B R2 U' R' F R2 U' B' U F U' D' F'` (16)

Left: DL → DR → DF → DL

<details>
<summary>Answer for 3e, skeleton 1</summary>

**8 moves or less per insertion** (one comm): +6, 22 in all.

```
D2 L F2 B R2 U' R' F R2 U' B' U F * U' D' F'
* = F' R2 U2 L2 B' L2 U2 R2 // (8-2/22)
Solution: D2 L F2 B R2 U' R' F R2 U' B' U R2 U2 L2 B' L2 U2 R2 U' D' F' (22)
```

**Up to 10 moves per insertion**: nothing better, 22 stays the best.

</details>

#### 3e, skeleton 2

Scramble: `R' U' F D2 R2 F' L2 B2 L2 B L2 D2 B2 L' R' U B2 R' U2 R F2 R' U' F`

Skeleton: `D R2 F' B' U' L B' U2 D' F D2 L B U2 L D' F` (17)

Left: DF → UR → FR → DF

<details>
<summary>Answer for 3e, skeleton 2</summary>

**8 moves or less per insertion** (one comm): +8, 25 in all.

```
D * R2 F' B' U' L B' U2 D' F D2 L B U2 L D' F
* = U2 B2 L' D2 B2 U2 R' F2 // (8-0/25)
Solution: U2 D B2 L' D2 B2 U2 R' F2 R2 F' B' U' L B' U2 D' F D2 L B U2 L D' F (25)
```

**Up to 10 moves per insertion** (one comm): +7, 24 in all.

```
D R2 F' B' U' L B' U2 D' * F D2 L B U2 L D' F
* = U' D B' U' B U D' R' U R // (10-3/24)
Solution: D R2 F' B' U' L B' U B' U' B U D' R' U R F D2 L B U2 L D' F (24)
```

</details>

#### 3e, skeleton 3

Scramble: `R' U' F L2 F2 U2 B2 R2 D U' R2 U B2 R' U F2 L2 B' L2 D F U B' R' U' F`

Skeleton: `D2 F' B U' R B2 L F' R2 U2 B' U' R B D B U F'` (18)

Left: UL → FR → UR → UL

<details>
<summary>Answer for 3e, skeleton 3</summary>

**8 moves or less per insertion** (one comm): +5, 23 in all.

```
D2 F' B U' R B2 L F' R2 U2 B' U' R B D B U * F'
* = U' R' L F2 R L' U' // (7-2/23)
Solution: D2 F' B U' R B2 L F' R2 U2 B' U' R B D B R' L F2 R L' U' F' (23)
```

**Up to 10 moves per insertion**: nothing better, 23 stays the best.

</details>

#### 3e, skeleton 4

Scramble: `R' U' F U' D2 R2 U2 R2 U2 B D2 F2 U2 F L2 F L' U B L F D R' U2 L2 R' U' F`

Skeleton: `B L B2 L U' F2 B' U2 F2 D' R B D B2 R D F U D2` (19)

Left: BL → UF → DB → BL

<details>
<summary>Answer for 3e, skeleton 4</summary>

**8 moves or less per insertion** (one comm): +4, 23 in all.

```
B L * B2 L U' F2 B' U2 F2 D' R B D B2 R D F U D2
* = L' F' B D2 F B' L' // (7-3/23)
Solution: F' B2 D2 F B' L' B2 L U' F2 B' U2 F2 D' R B D B2 R D F U D2 (23)
```

**Up to 10 moves per insertion**: nothing better, 23 stays the best.

</details>

#### 3e, skeleton 5

Scramble: `R' U' F D2 F2 D2 F2 R2 U2 F2 L2 D R2 D' L D' U R' D B U2 R D2 U2 R' U' F`

Skeleton: `B2 D2 F' R2 D2 B L U2 R U' D2 B2 D2 R B U F' B2 R' F` (20)

Left: DB → UR → DF → DB

<details>
<summary>Answer for 3e, skeleton 5</summary>

**8 moves or less per insertion** (one comm): +2, 22 in all.

```
B2 D2 F' R2 D2 B L U2 R * U' D2 B2 D2 R B U F' B2 R' F
* = R' U2 R' L F2 R2 L' // (7-5/22)
Solution: B2 D2 F' R2 D2 B R' L2 F2 R2 L' U' D2 B2 D2 R B U F' B2 R' F (22)
```

**Up to 10 moves per insertion**: nothing better, 22 stays the best.

</details>

#### 3e, skeleton 6

Scramble: `R' U' F B' L2 D2 R2 F2 L2 B2 U2 B2 F' D2 L B' D' F' U' R' U' F L2 U' R' U' F`

Skeleton: `U B U L U' L2 B U' D R U2 F2 D' B R2 U F' R2 L2 D B` (21)

Left: DB → UF → DR → DB

<details>
<summary>Answer for 3e, skeleton 6</summary>

**8 moves or less per insertion** (one comm): +7, 28 in all.

```
U B U L U' L2 B U' D R U2 F2 D' B R2 U F' R2 L2 * D B
* = F U D' L2 U' D F // (7-0/28)
Solution: U B U L U' L2 B U' D R U2 F2 D' B R2 U F' R2 L2 F U D' L2 U' D F D B (28)
```

**Up to 10 moves per insertion** (one comm): +6, 27 in all.

```
U B U L U' L2 B U' D R U2 F2 D' B * R2 U F' R2 L2 D B
* = B' D B U2 D2 F' D' F U2 D2 // (10-4/27)
Solution: U B U L U' L2 B U' D R U2 F2 B U2 D2 F' D' F U2 D2 R2 U F' R2 L2 D B (27)
```

</details>

#### 3e, skeleton 7

Scramble: `R' U' F L F2 L' U2 L' R' B2 F2 R U2 B2 F2 D R2 F U2 R B' L' D2 R' U' F`

Skeleton: `U2 R F B2 U D2 F2 D B' U' R' D R2 F' U2 L' F' R2 F' L2 F' B` (22)

Left: DB → DF → UF → DB

<details>
<summary>Answer for 3e, skeleton 7</summary>

**8 moves or less per insertion** (one comm): +5, 27 in all.

```
U2 R F B2 U D2 F2 D B' U' R' D R2 F' U2 L' F' R2 F' L2 F' B *
* = F2 R' L D2 R L' // (6-1/27)
Solution: U2 R F B2 U D2 F2 D B' U' R' D R2 F' U2 L' F' R2 F' L2 F B R' L D2 R L' (27)
```

**Up to 10 moves per insertion**: nothing better, 27 stays the best.

</details>

#### 3e, skeleton 8

Scramble: `R' U' F U' B2 D' L2 D' B2 D' F2 U R2 B R F L' U R B' L2 R B' R' U' F`

Skeleton: `L' F' R2 D B2 D2 B' R B2 L2 B2 L U B2 U2 D'` (16)

Left: FL → UL → FR → FL

<details>
<summary>Answer for 3e, skeleton 8</summary>

**8 moves or less per insertion**: nothing fits anywhere in this skeleton.

**Up to 10 moves per insertion** (one comm): +6, 22 in all.

```
L' F' R2 D B2 D2 B' R B2 L2 B2 L U B2 * U2 D'
* = B' R' B U D' R' F R U' D // (10-4/22)
Solution: L' F' R2 D B2 D2 B' R B2 L2 B2 L U B R' B U D' R' F R U (22)
```

</details>

#### 3e, skeleton 9

Scramble: `R' U' F R2 B' U2 F' D2 B' U2 F R2 B' U2 L2 R D B' F' R' D' R' B' R' U' F`

Skeleton: `D2 F2 B' R2 B' U L' U' F B' R F' U F2 L F2 L2` (17)

Left: UB → DR → UR → UB

<details>
<summary>Answer for 3e, skeleton 9</summary>

**8 moves or less per insertion**: nothing fits anywhere in this skeleton.

**Up to 10 moves per insertion** (one comm): +8, 25 in all.

```
D2 F2 B' R2 B' U L' U' F B' R F' U * F2 L F2 L2
* = U R2 U' F' B L U2 L' F B' // (10-2/25)
Solution: D2 F2 B' R2 B' U L' U' F B' R F' U2 R2 U' F' B L U2 L' F' B' L F2 L2 (25)
```

</details>

#### 3e, skeleton 10

Scramble: `R' U' F U' B2 R2 U' L2 D' L2 U B2 U2 B2 U' B' F2 D R' F L2 U' B' D2 L' U2 R' U' F`

Skeleton: `B D2 R L U L B2 L2 D B D2 B2 D2 B U L U' F'` (18)

Left: BL → BR → DF → BL

<details>
<summary>Answer for 3e, skeleton 10</summary>

**8 moves or less per insertion** (one comm): +6, 24 in all.

```
B D2 R L U L B2 L2 D B D2 B2 * D2 B U L U' F'
* = B2 L2 D' L2 B2 R2 U' R2 // (8-2/24)
Solution: B D2 R L U L B2 L2 D B D2 L2 D' L2 B2 R2 U' R2 D2 B U L U' F' (24)
```

**Up to 10 moves per insertion**: nothing better, 24 stays the best.

</details>

#### 3e, skeleton 11

Scramble: `R' U' F U2 R2 B2 F2 R' F2 L' B2 D2 R B F2 L F L U B' F' D' B2 L' U' R' U' F`

Skeleton: `D2 F' B' L2 B R2 L' U F L2 U2 L2 U' D F L2 B' R2 L` (19)

Left: UL → DR → DB → UL

<details>
<summary>Answer for 3e, skeleton 11</summary>

**8 moves or less per insertion**: nothing fits anywhere in this skeleton.

**Up to 10 moves per insertion** (one comm): +7, 26 in all.

```
D2 F' B' L2 B R2 L' U F L2 U2 L2 U' D F L2 B' R2 L *
* = R2 U' R L' B2 R' L U' R2 // (9-2/26)
Solution: D2 F' B' L2 B R2 L' U F L2 U2 L2 U' D F L2 B' L U' R L' B2 R' L U' R2 (26)
```

</details>

#### 3e, skeleton 12

Scramble: `R' U' F D' L2 R2 D2 U' B2 U' F2 U' F2 D2 L' D' R' U' L R2 F U' B' L' R' U' F`

Skeleton: `R' L2 B U D2 R U F2 B2 U2 B2 D2 B2 D' F2 D R U F' U'` (20)

Left: FL → DB → UB → FL

<details>
<summary>Answer for 3e, skeleton 12</summary>

**8 moves or less per insertion**: nothing fits anywhere in this skeleton.

**Up to 10 moves per insertion** (one comm): +9, 29 in all.

```
R' L2 B U D2 R U F2 B2 U2 B2 D2 B2 D' F2 D R * U F' U'
* = R U' B' U R' L F' U F L' // (10-1/29)
Solution: R' L2 B U D2 R U F2 B2 U2 B2 D2 B2 D' F2 D R2 U' B' U R' L F' U F L' U F' U' (29)
```

</details>

#### 3e, skeleton 13

Scramble: `R' U' F U2 R F2 L R D2 R U2 F2 R2 F2 D' L2 B U F U2 B2 R2 D' R' U' F`

Skeleton: `U' B2 L U R' F2 R' B2 R2 B' U' L' B' L2 F2 L2 F' U F U R2` (21)

Left: BL → FR → UL → BL

<details>
<summary>Answer for 3e, skeleton 13</summary>

**8 moves or less per insertion** (one comm): +4, 25 in all.

```
U' B2 L * U R' F2 R' B2 R2 B' U' L' B' L2 F2 L2 F' U F U R2
* = L' F B' U2 F' B L' // (7-3/25)
Solution: U' F B U2 F' B L' U R' F2 R' B2 R2 B' U' L' B' L2 F2 L2 F' U F U R2 (25)
```

**Up to 10 moves per insertion**: nothing better, 25 stays the best.

</details>

#### 3e, skeleton 14

Scramble: `R' U' F U2 R2 F2 U L2 B2 F2 U F2 R2 U2 L R2 D' L2 B2 F' L R2 U' B2 R' U' F`

Skeleton: `L F' R F' B D' R F2 B' R' B L' U2 F R2 B L2 D' R' D F' D2` (22)

Left: BL → UB → UF → BL

<details>
<summary>Answer for 3e, skeleton 14</summary>

**8 moves or less per insertion**: nothing fits anywhere in this skeleton.

**Up to 10 moves per insertion** (one comm): +7, 29 in all.

```
L F' R F' B D' R F2 B' R' B L' U2 F * R2 B L2 D' R' D F' D2
* = F' R' L D R D' R L' F R' // (10-3/29)
Solution: L F' R F' B D' R F2 B' R' B L' U2 R' L D R D' R L' F R B L2 D' R' D F' D2 (29)
```

</details>

#### 3e, skeleton 15

Scramble: `R' U' F D2 L2 B D2 R2 B U2 L2 F D2 L2 B2 R D' L2 R' B F2 U L' R' U' F`

Skeleton: `R' B' R' D2 R2 B D2 B L U' B2 R B2 D2 B' U2` (16)

Left: FL → BR → UR → FL

<details>
<summary>Answer for 3e, skeleton 15</summary>

**8 moves or less per insertion**: nothing fits anywhere in this skeleton.

**Up to 10 moves per insertion** (one comm): +6, 22 in all.

```
R' B' R' D2 R2 B D2 B L * U' B2 R B2 D2 B' U2
* = L' F' B D L D' F B' L U' // (10-4/22)
Solution: R' B' R' D2 R2 B D2 F' B2 D L D' F B' L U2 B2 R B2 D2 B' U2 (22)
```

</details>

#### 3e, skeleton 16

Scramble: `R' U' F B2 D2 F D2 B L2 D2 L2 F2 L2 B' R2 U B' D' U2 L U R D B' R U' R' U' F`

Skeleton: `R' F2 R D' B2 L' U' R D2 R2 U2 B' R' B2 U2 B U2` (17)

Left: BL → DB → DF → BL

<details>
<summary>Answer for 3e, skeleton 16</summary>

**8 moves or less per insertion**: nothing fits anywhere in this skeleton.

**Up to 10 moves per insertion** (one comm): +7, 24 in all.

```
R' F2 R D' B2 L' U' R D2 R2 U2 B' * R' B2 U2 B U2
* = B D' B' R L' D F D' R' L // (10-3/24)
Solution: R' F2 R D' B2 L' U' R D2 R2 U2 D' B' R L' D F D' R2 L B2 U2 B U2 (24)
```

</details>

#### 3e, skeleton 17

Scramble: `R' U' F L2 D2 L2 F2 D2 B2 U2 R2 F D2 U2 L2 R D' U2 R D2 U F2 R' D R' U' F`

Skeleton: `B2 D B2 U2 R F2 L' U' L2 U2 L2 B2 D2 L' F' B2 L' B2` (18)

Left: DF → UB → DR → DF

<details>
<summary>Answer for 3e, skeleton 17</summary>

**8 moves or less per insertion** (one comm): +6, 24 in all.

```
B2 D B2 U2 R F2 L' U' L2 U2 L2 B2 D2 * L' F' B2 L' B2
* = D' R' L B2 R L' D' // (7-1/24)
Solution: B2 D B2 U2 R F2 L' U' L2 U2 L2 B2 D R' L B2 R L' D' L' F' B2 L' B2 (24)
```

**Up to 10 moves per insertion**: nothing better, 24 stays the best.

</details>

#### 3e, skeleton 18

Scramble: `R' U' F R2 U' R2 U F2 U2 L2 B2 U L2 U F2 R' F' D2 U B' F2 D2 B L2 U R' U' F`

Skeleton: `D R2 U' B L' B' D' L2 B' U F' R' L2 B D2 F L' U2 R'` (19)

Left: BL → FL → FR → BL

<details>
<summary>Answer for 3e, skeleton 18</summary>

**8 moves or less per insertion**: nothing fits anywhere in this skeleton.

**Up to 10 moves per insertion** (one comm): +7, 26 in all.

```
D R2 U' B L' B' D' L2 B' U F' * R' L2 B D2 F L' U2 R'
* = F R' L D' L' D R L' F' L // (10-3/26)
Solution: D R2 U' B L' B' D' L2 B' U R' L D' L' D R L' F' R' L' B D2 F L' U2 R' (26)
```

</details>

#### 3e, skeleton 19

Scramble: `R' U' F B2 D F2 U2 R2 F2 U' L2 B2 U' R2 F2 U F R F2 U R D U' F2 D R' U' F`

Skeleton: `U2 R' F2 R' F2 U' B2 R D2 B R' F' L' B U' F' B2 R2 B L` (20)

Left: UB → DR → BR → UB

<details>
<summary>Answer for 3e, skeleton 19</summary>

**8 moves or less per insertion** (one comm): +8, 28 in all.

```
U2 R' F2 R' F2 U' B2 R D2 B R' * F' L' B U' F' B2 R2 B L
* = U2 B2 D2 L D2 B2 U2 R // (8-0/28)
Solution: U2 R' F2 R' F2 U' B2 R D2 B R' U2 B2 D2 L D2 B2 U2 R F' L' B U' F' B2 R2 B L (28)
```

**Up to 10 moves per insertion** (one comm): +7, 27 in all.

```
U2 R' F2 R' F2 U' B2 R D2 B R' * F' L' B U' F' B2 R2 B L
* = R U2 D2 L' B2 L U2 D2 R' F2 // (10-3/27)
Solution: U2 R' F2 R' F2 U' B2 R D2 B U2 D2 L' B2 L U2 D2 R' F L' B U' F' B2 R2 B L (27)
```

</details>

#### 3e, skeleton 20

Scramble: `R' U' F R2 D2 B L2 F R2 B D2 U2 L2 B2 L B F' L F' D' U' R B2 R' U' F`

Skeleton: `R L' F2 U R' D F' U' F2 R' U B U' F2 B2 D B2 D2 F B2 U2` (21)

Left: UL → BR → UB → UL

<details>
<summary>Answer for 3e, skeleton 20</summary>

**8 moves or less per insertion** (one comm): +4, 25 in all.

```
R L' F2 U R' D F' U' F2 R' * U B U' F2 B2 D B2 D2 F B2 U2
* = R F2 D2 B2 L B2 D2 F2 // (8-4/25)
Solution: R L' F2 U R' D F' U' D2 B2 L B2 D2 F2 U B U' F2 B2 D B2 D2 F B2 U2 (25)
```

**Up to 10 moves per insertion**: nothing better, 25 stays the best.

</details>

### 2e2e

Two edge swaps, no flip.

#### 2e2e, skeleton 1

Scramble: `R' U' F U' L' U2 L' B2 L D2 B2 R' F2 L2 D2 B2 R F' D' U2 L' B R D2 U F2 R' U' F`

Skeleton: `D2 L F2 B R2 U' R' F R2 U' B' U F U' D' F'` (16)

Left: BL ↔ FL, UB ↔ FR

<details>
<summary>Answer for 2e2e, skeleton 1</summary>

**8 moves or less per insertion** (two comms): +9, 25 in all.

```
D2 L F2 B R2 U' ^ R' F R2 U' B' U F U' D' * F'
* = F U D' L2 U' D F // (7-2/21)
^ = U2 F2 D2 L B2 D2 F2 R // (8-4/25)
Solution: D2 L F2 B R2 U F2 D2 L B2 D2 F' R2 U' B' U F U' D' F U D' L2 U' D (25)
```

**Up to 10 moves per insertion** (one alg for the whole leftover): +6, 22 in all.

```
D2 L F2 B R2 U' * R' F R2 U' B' U F U' D' F'
* = U R2 D2 F2 L2 U D F2 R2 D // (10-4/22)
Solution: D2 L F2 B D2 F2 L2 U D F2 R2 D R' F R2 U' B' U F U' D' F' (22)
```

</details>

#### 2e2e, skeleton 2

Scramble: `R' U' F B2 D2 B' R2 F U2 L2 U2 B' L2 B U' F' L' R' F' U' F' U B2 U' R' U' F`

Skeleton: `D R2 F' B' U' L B' U2 D' F D2 L B U2 L D' F` (17)

Left: DF ↔ FR, UB ↔ UF

<details>
<summary>Answer for 2e2e, skeleton 2</summary>

**8 moves or less per insertion** (one alg for the whole leftover): +8, 25 in all.

```
D R2 F' B' U' L B' U2 D' F D2 L B U2 L D' F *
* = D2 L2 B U2 L2 D2 F R2 // (8-0/25)
Solution: D R2 F' B' U' L B' U2 D' F D2 L B U2 L D' F D2 L2 B U2 L2 D2 F R2 (25)
```

**Up to 10 moves per insertion** (one alg for the whole leftover): +7, 24 in all.

```
D R2 F' B' U' L * B' U2 D' F D2 L B U2 L D' F
* = L' B L D2 F L F' L' D2 B' // (10-3/24)
Solution: D R2 F' B' U' B L D2 F L F' L' D2 B2 U2 D' F D2 L B U2 L D' F (24)
```

</details>

#### 2e2e, skeleton 3

Scramble: `R' U' F U2 R2 D' F2 R2 B2 L2 R2 U2 B2 D L2 U' R B2 D F L D' U' B D2 R' U' F`

Skeleton: `D2 F' B U' R B2 L F' R2 U2 B' U' R B D B U F'` (18)

Left: FL ↔ FR, DR ↔ BR

<details>
<summary>Answer for 2e2e, skeleton 3</summary>

**8 moves or less per insertion** (two comms): +9, 27 in all.

```
D2 F' B ^ U' R B2 L F' R2 U2 B' U' R B * D B U F'
* = B2 L2 F2 U' F2 L2 B2 D' // (8-4/22)
^ = F R2 D2 L2 B D2 R2 U2 // (8-3/27)
Solution: D2 B R2 D2 L2 B D2 R2 U R B2 L F' R2 U2 B' U' R B' L2 F2 U' F2 L2 B' U F' (27)
```

**Up to 10 moves per insertion** (one alg for the whole leftover): +8, 26 in all.

```
D2 * F' B U' R B2 L F' R2 U2 B' U' R B D B U F'
* = U' D2 F2 L U2 F2 D2 R B2 U // (10-2/26)
Solution: U' F2 L U2 F2 D2 R B2 U F' B U' R B2 L F' R2 U2 B' U' R B D B U F' (26)
```

</details>

#### 2e2e, skeleton 4

Scramble: `R' U' F U' B D2 U2 B' R2 B L2 R2 D2 R2 F R' B' F U' R' U2 B' D U B' U' R' U' F`

Skeleton: `B L B2 L U' F2 B' U2 F2 D' R B D B2 R D F U D2` (19)

Left: DB ↔ UR, UF ↔ DR

<details>
<summary>Answer for 2e2e, skeleton 4</summary>

**8 moves or less per insertion** (one alg for the whole leftover): +6, 25 in all.

```
B L B2 L U' F2 B' U2 F2 D' R B D B2 R D F U D2 *
* = U' F2 L2 B2 L2 F2 R2 U // (8-2/25)
Solution: B L B2 L U' F2 B' U2 F2 D' R B D B2 R D F D2 F2 L2 B2 L2 F2 R2 U (25)
```

**Up to 10 moves per insertion**: nothing better, 25 stays the best.

</details>

#### 2e2e, skeleton 5

Scramble: `R' U' F B D2 U2 B L2 R2 F' L2 B' F' L2 D2 B2 D' R' F2 L F' U2 R' U2 L' R' U' F`

Skeleton: `B2 D2 F' R2 D2 B L U2 R U' D2 B2 D2 R B U F' B2 R' F` (20)

Left: FL ↔ DF, DB ↔ UF

<details>
<summary>Answer for 2e2e, skeleton 5</summary>

**8 moves or less per insertion** (two comms): +9, 29 in all.

```
B2 D2 ^ F' R2 D2 B L U2 R U' D2 * B2 D2 R B U F' B2 R' F
* = U2 L U2 B2 D2 R D2 B2 // (8-6/22)
^ = L' U' D F2 U D' L' // (7-0/29)
Solution: B2 D2 L' U' D F2 U D' L' F' R2 D2 B L U2 R U D2 L U2 B2 D2 R2 B U F' B2 R' F (29)
```

**Up to 10 moves per insertion**: nothing better, 29 stays the best.

</details>

#### 2e2e, skeleton 6

Scramble: `R' U' F D2 F L2 D2 F' L2 D2 B' L2 B2 D' U2 L2 B' F' U2 L' D' F R D' R' U' F`

Skeleton: `U B U L U' L2 B U' D R U2 F2 D' B R2 U F' R2 L2 D B` (21)

Left: BL ↔ DR, BR ↔ UR

<details>
<summary>Answer for 2e2e, skeleton 6</summary>

**8 moves or less per insertion** (one alg for the whole leftover): +7, 28 in all.

```
U B U L U' L2 B U' D * R U2 F2 D' B R2 U F' R2 L2 D B
* = D2 B2 L' U2 B2 D2 R' F2 // (8-1/28)
Solution: U B U L U' L2 B U' D' B2 L' U2 B2 D2 R' F2 R U2 F2 D' B R2 U F' R2 L2 D B (28)
```

**Up to 10 moves per insertion**: nothing better, 28 stays the best.

</details>

#### 2e2e, skeleton 7

Scramble: `R' U' F U' L2 D' B2 D F2 D F2 D2 R2 U R2 F R' D2 B' L R B2 D' L2 R2 U' R' U' F`

Skeleton: `U2 R F B2 U D2 F2 D B' U' R' D R2 F' U2 L' F' R2 F' L2 F' B` (22)

Left: BL ↔ BR, FL ↔ DF

<details>
<summary>Answer for 2e2e, skeleton 7</summary>

**8 moves or less per insertion** (two comms): +10, 32 in all.

```
* U2 R F B2 U D2 F2 D B' U' R' D R2 F' U2 L' F' R2 F' L2 F' B
* = F U2 L2 D2 B D2 L2 U2 // (8-2/28)
F U2 L2 D2 B D2 R L2 ^ F B2 U D2 F2 D B' U' R' D R2 F' U2 L' F' R2 F' L2 F' B
^ = L2 F2 D' L2 B2 R2 U' B2 // (8-4/32)
Solution: F U2 L2 D2 B D2 R F2 D' L2 B2 R2 U' F U D2 F2 D B' U' R' D R2 F' U2 L' F' R2 F' L2 F' B (32)
```

**Up to 10 moves per insertion** (two comms): +7, 29 in all.

```
U2 R F B2 U D2 F2 D B' U' R' D * R2 F' U2 L' F' R2 F' L2 F' B
* = F' R2 L2 B R2 B' R2 L2 F R2 // (10-4/28)
U2 R F B2 U D2 F2 D B' U' R' D ^ F' R2 L2 B R2 B' R2 L2 U2 L' F' R2 F' L2 F' B
^ = D F' R2 L2 B U' B' R2 L2 F // (10-9/29)
Solution: U2 R F B2 U D2 F2 D B' U' R' D2 F' R2 L2 B U' R2 B' R2 L2 U2 L' F' R2 F' L2 F' B (29)
```

</details>

#### 2e2e, skeleton 8

Scramble: `R' U' F B2 L2 D2 B2 R U2 B2 L D2 R2 U2 B2 L U' F2 R D2 L F U' L' R2 D' R' U' F`

Skeleton: `L' F' R2 D B2 D2 B' R B2 L2 B2 L U B2 U2 D'` (16)

Left: DL ↔ FL, UF ↔ DR

<details>
<summary>Answer for 2e2e, skeleton 8</summary>

**8 moves or less per insertion** (two comms): +12, 28 in all.

```
L' ^ F' R2 D B2 D2 * B' R B2 L2 B2 L U B2 U2 D'
* = R2 U2 L2 F L2 U2 R2 B // (8-3/21)
^ = U2 R2 D2 B' L2 D2 R2 F' // (8-1/28)
Solution: L' U2 R2 D2 B' L2 D2 R2 F2 R2 D B2 D2 R2 U2 L2 F L2 U2 R' B2 L2 B2 L U B2 U2 D' (28)
```

**Up to 10 moves per insertion** (two comms): +7, 23 in all.

```
L' * F' R2 D B2 D2 B' R B2 L2 B2 L U B2 U2 D'
* = L2 F' R2 L2 B L2 B' R2 L2 F // (10-5/21)
L F' R2 L2 B ^ L2 B' L2 D B2 D2 B' R B2 L2 B2 L U B2 U2 D'
^ = B' R2 L2 F U F' R2 L2 B D' // (10-8/23)
Solution: L U F' R2 L2 B D' L2 B' L2 D B2 D2 B' R B2 L2 B2 L U B2 U2 D' (23)
```

</details>

#### 2e2e, skeleton 9

Scramble: `R' U' F R2 D2 R2 U2 B' L2 B2 R2 D2 B2 F' D2 L' D' R2 D' B R2 D R F' R' U' F`

Skeleton: `D2 F2 B' R2 B' U L' U' F B' R F' U F2 L F2 L2` (17)

Left: BL ↔ UB, UF ↔ BR

<details>
<summary>Answer for 2e2e, skeleton 9</summary>

**8 moves or less per insertion** (one alg for the whole leftover): +7, 24 in all.

```
D2 F2 B' R2 B' U L' U' F B' R F' U F2 L F2 * L2
* = F R2 U2 R2 U2 R2 U2 F' // (8-1/24)
Solution: D2 F2 B' R2 B' U L' U' F B' R F' U F2 L F' R2 U2 R2 U2 R2 U2 F' L2 (24)
```

**Up to 10 moves per insertion**: nothing better, 24 stays the best.

</details>

#### 2e2e, skeleton 10

Scramble: `R' U' F D2 B2 R2 U2 L U2 L U2 B2 R' D2 R B R U F' D' L2 B' D2 U2 R' U' F`

Skeleton: `B D2 R L U L B2 L2 D B D2 B2 D2 B U L U' F'` (18)

Left: BL ↔ DR, UL ↔ UF

<details>
<summary>Answer for 2e2e, skeleton 10</summary>

**8 moves or less per insertion** (one alg for the whole leftover): +6, 24 in all.

```
B D2 R L U L B2 L2 D B D2 B2 D2 B * U L U' F'
* = B2 L D2 B2 U2 R F2 U2 // (8-2/24)
Solution: B D2 R L U L B2 L2 D B D2 B2 D2 B' L D2 B2 U2 R F2 U' L U' F' (24)
```

**Up to 10 moves per insertion**: nothing better, 24 stays the best.

</details>

#### 2e2e, skeleton 11

Scramble: `R' U' F U2 B L2 R2 B' U2 B' R2 B D2 R2 B U' L F' U2 B' R' D' L2 F2 R' U' F`

Skeleton: `D2 F' B' L2 B R2 L' U F L2 U2 L2 U' D F L2 B' R2 L` (19)

Left: DL ↔ BL, FL ↔ DB

<details>
<summary>Answer for 2e2e, skeleton 11</summary>

**8 moves or less per insertion** (two comms): +13, 32 in all.

```
D2 ^ F' B' L2 B R2 L' U F L2 U2 L2 U' D * F L2 B' R2 L
* = U2 L F2 D2 B2 R D2 F2 // (8-2/25)
^ = L2 D L2 B2 R2 U R2 B2 // (8-1/32)
Solution: D2 L2 D L2 B2 R2 U R2 F' B L2 B R2 L' U F L2 U2 L2 U D L F2 D2 B2 R D2 F' L2 B' R2 L (32)
```

**Up to 10 moves per insertion** (two comms): +6, 25 in all.

```
D2 F' B' L2 B R2 L' U F L2 U2 L2 * U' ^ D F L2 B' R2 L
* = D' R' U' B U R D L B' L' // (10-0/29)
^ = U L B L' U' D F L' F' D' // (10-14/25)
Solution: D2 F' B' L2 B R2 L' U F L2 U2 L2 D' R' U' B U R U' D2 F L B' R2 L (25)
```

</details>

#### 2e2e, skeleton 12

Scramble: `R' U' F B2 D' F2 R2 D' R2 D' R2 U2 L2 D' U2 L D' U L R B F' L2 U' L R' U' F`

Skeleton: `R' L2 B U D2 R U F2 B2 U2 B2 D2 B2 D' F2 D R U F' U'` (20)

Left: BL ↔ FL, DF ↔ BR

<details>
<summary>Answer for 2e2e, skeleton 12</summary>

**8 moves or less per insertion** (two comms): +6, 26 in all.

```
R' L2 B U D2 R U F2 B2 ^ U2 B2 D2 B2 * D' F2 D R U F' U'
* = U' F2 U D' L2 D // (6-2/24)
^ = R B2 D2 F2 L D2 B2 U2 // (8-6/26)
Solution: R' L2 B U D2 R U F2 B2 R B2 D2 F2 L B2 U' F2 U D' L2 F2 D R U F' U' (26)
```

**Up to 10 moves per insertion** (two comms): +5, 25 in all.

```
R' L2 B U D2 R U F2 ^ B2 U2 B2 D2 B2 * D' F2 D R U F' U'
* = U' R2 D B2 U D' R2 D' F2 D // (10-7/23)
^ = B2 L U2 B2 D2 R D2 B2 U2 B2 // (10-8/25)
Solution: R' L2 B U D2 R U F2 B2 L U2 B2 D2 R B2 U' R2 D B2 U D' R' U F' U' (25)
```

</details>

#### 2e2e, skeleton 13

Scramble: `R' U' F U2 B U2 L2 U2 B' D2 B2 F' L2 D2 F R' F D' R2 U B' D2 U F R' U' F`

Skeleton: `U' B2 L U R' F2 R' B2 R2 B' U' L' B' L2 F2 L2 F' U F U R2` (21)

Left: FL ↔ UF, UL ↔ DR

<details>
<summary>Answer for 2e2e, skeleton 13</summary>

**8 moves or less per insertion** (two comms): +11, 32 in all.

```
U' B2 L U R' ^ F2 R' B2 * R2 B' U' L' B' L2 F2 L2 F' U F U R2
* = U2 B L2 U2 R2 F D2 R2 // (8-2/27)
^ = U2 B2 L' D2 B2 U2 R' F2 // (8-3/32)
Solution: U' B2 L U R' U2 B2 L' D2 B2 U2 R2 B2 U2 B L2 U2 R2 F D2 B' U' L' B' L2 F2 L2 F' U F U R2 (32)
```

**Up to 10 moves per insertion** (one alg for the whole leftover): +8, 29 in all.

```
U' B2 * L U R' F2 R' B2 R2 B' U' L' B' L2 F2 L2 F' U F U R2
* = B D2 L F2 D2 B2 R U2 B // (9-1/29)
Solution: U' B' D2 L F2 D2 B2 R U2 B L U R' F2 R' B2 R2 B' U' L' B' L2 F2 L2 F' U F U R2 (29)
```

</details>

#### 2e2e, skeleton 14

Scramble: `R' U' F U B2 D L2 R2 D B2 U2 F2 L2 U' L2 B' D U2 R B' F2 D2 L' U B R' U' F`

Skeleton: `L F' R F' B D' R F2 B' R' B L' U2 F R2 B L2 D' R' D F' D2` (22)

Left: FL ↔ UB, DB ↔ DF

<details>
<summary>Answer for 2e2e, skeleton 14</summary>

**8 moves or less per insertion** (one alg for the whole leftover): +7, 29 in all.

```
L F' R F' * B D' R F2 B' R' B L' U2 F R2 B L2 D' R' D F' D2
* = R U2 L2 D2 L2 U2 R // (7-0/29)
Solution: L F' R F' R U2 L2 D2 L2 U2 R B D' R F2 B' R' B L' U2 F R2 B L2 D' R' D F' D2 (29)
```

**Up to 10 moves per insertion**: nothing better, 29 stays the best.

</details>

#### 2e2e, skeleton 15

Scramble: `R' U' F R2 B' R2 F L2 B2 U2 L2 F' R2 U2 B' R U R2 U2 B' L' R' B2 R' U' F`

Skeleton: `R' B' R' D2 R2 B D2 B L U' B2 R B2 D2 B' U2` (16)

Left: DL ↔ FL, DB ↔ DF

<details>
<summary>Answer for 2e2e, skeleton 15</summary>

**8 moves or less per insertion**: nothing fits anywhere in this skeleton.

**Up to 10 moves per insertion** (two comms): +11, 27 in all.

```
R' B' * R' ^ D2 R2 B D2 B L U' B2 R B2 D2 B' U2
* = L' D' R' B' R D L U B U' // (10-0/26)
^ = R U B' U' R' L F U F' L' // (10-9/27)
Solution: R' B' L' D' R' B' R D R' L2 F U F' L' D2 R2 B D2 B L U' B2 R B2 D2 B' U2 (27)
```

</details>

#### 2e2e, skeleton 16

Scramble: `R' U' F R2 B R2 F U2 B2 R2 U2 F D2 B2 L2 D' L D U2 R' U F D' U2 B2 U' R' U' F`

Skeleton: `R' F2 R D' B2 L' U' R D2 R2 U2 B' R' B2 U2 B U2` (17)

Left: DB ↔ FR, UF ↔ DR

<details>
<summary>Answer for 2e2e, skeleton 16</summary>

**8 moves or less per insertion** (two comms): +13, 30 in all.

```
R' F2 R D' ^ B2 L' U' R D2 R2 U2 B' R' B2 * U2 B U2
* = R' U2 F2 D2 L' D2 F2 U2 // (8-2/23)
^ = R2 U2 L2 F' D2 L2 U2 B' // (8-1/30)
Solution: R' F2 R D' R2 U2 L2 F' D2 L2 U2 B L' U' R D2 R2 U2 B' R' B2 R' U2 F2 D2 L' D2 F2 B U2 (30)
```

**Up to 10 moves per insertion** (two comms): +8, 25 in all.

```
R' F2 R D' B2 ^ L' U' R D2 R2 U2 * B' R' B2 U2 B U2
* = F' U' B2 U F B' R' B2 R B // (10-6/21)
^ = R' F' R F R L' U' R' U L // (10-6/25)
Solution: R' F2 R D' B2 R' F' R F R L' U' D2 R2 U2 F' U' B2 U F B' R' U2 B U2 (25)
```

</details>

#### 2e2e, skeleton 17

Scramble: `R' U' F U2 L U2 L2 F2 L U2 R D2 B2 U2 F2 U' L2 R' B L2 F2 U' B2 F2 R' U' F`

Skeleton: `B2 D B2 U2 R F2 L' U' L2 U2 L2 B2 D2 L' F' B2 L' B2` (18)

Left: FL ↔ FR, UF ↔ BR

<details>
<summary>Answer for 2e2e, skeleton 17</summary>

**8 moves or less per insertion** (two comms): +11, 29 in all.

```
B2 D B2 ^ U2 R F2 L' U' L2 U2 L2 B2 D2 L' F' * B2 L' B2
* = U B2 R2 F2 D F2 R2 B2 // (8-2/24)
^ = U2 F B' D2 F' B R2 U2 // (8-3/29)
Solution: B2 D B2 U2 F B' D2 F' B R' F2 L' U' L2 U2 L2 B2 D2 L' F' U B2 R2 F2 D F2 R2 L' B2 (29)
```

**Up to 10 moves per insertion** (one alg for the whole leftover): +8, 26 in all.

```
B2 D * B2 U2 R F2 L' U' L2 U2 L2 B2 D2 L' F' B2 L' B2
* = U' D' F' R2 D2 R2 F' U D F2 // (10-2/26)
Solution: B2 U' F' R2 D2 R2 F' U D F2 B2 U2 R F2 L' U' L2 U2 L2 B2 D2 L' F' B2 L' B2 (26)
```

</details>

#### 2e2e, skeleton 18

Scramble: `R' U' F D' L2 D' B2 L2 F2 L2 F2 U L2 F2 D L B2 D' R2 U2 B L' R2 F' L R' U' F`

Skeleton: `D R2 U' B L' B' D' L2 B' U F' R' L2 B D2 F L' U2 R'` (19)

Left: BL ↔ FL, UL ↔ BR

<details>
<summary>Answer for 2e2e, skeleton 18</summary>

**8 moves or less per insertion** (two comms): +11, 30 in all.

```
D R2 U' B L' B' D' L2 ^ B' U F' R' * L2 B D2 F L' U2 R'
* = D2 F' B R2 D2 F B' L2 // (8-4/23)
^ = R2 D R2 B2 L2 U L2 B2 // (8-1/30)
Solution: D R2 U' B L' B' D' R2 L2 D R2 B2 L2 U L2 B U F' R' D2 F' B R2 D2 F D2 F L' U2 R' (30)
```

**Up to 10 moves per insertion** (two comms): +8, 27 in all.

```
D R2 U' B L' B' D' ^ L2 B' U F' R' * L2 B D2 F L' U2 R'
* = F B' U2 B L2 F' B D2 B' L2 // (10-8/21)
^ = R2 F' U F R2 L2 B' D' B L2 // (10-4/27)
Solution: D R2 U' B L' B' D' R2 F' U F R2 L2 B' U D' F' R' F B' U2 B L2 B L' U2 R' (27)
```

</details>

#### 2e2e, skeleton 19

Scramble: `R' U' F D2 F2 R2 F2 L2 D R2 F2 D U2 R B L F2 L2 R D2 B' F2 U2 R' U' F`

Skeleton: `U2 R' F2 R' F2 U' B2 R D2 B R' F' L' B U' F' B2 R2 B L` (20)

Left: DL ↔ FL, DF ↔ BR

<details>
<summary>Answer for 2e2e, skeleton 19</summary>

**8 moves or less per insertion** (one alg for the whole leftover): +7, 27 in all.

```
U2 R' F2 R' F2 U' B2 R D2 B R' F' L' * B U' F' B2 R2 B L
* = L' F2 D2 B2 D2 F2 U2 L // (8-1/27)
Solution: U2 R' F2 R' F2 U' B2 R D2 B R' F' L2 F2 D2 B2 D2 F2 U2 L B U' F' B2 R2 B L (27)
```

**Up to 10 moves per insertion**: nothing better, 27 stays the best.

</details>

#### 2e2e, skeleton 20

Scramble: `R' U' F U' D L2 B2 F2 U F2 D2 R2 U2 L2 B2 R D' U R D' B F' U L2 D' U' R' U' F`

Skeleton: `R L' F2 U R' D F' U' F2 R' U B U' F2 B2 D B2 D2 F B2 U2` (21)

Left: BL ↔ DR, UB ↔ UF

<details>
<summary>Answer for 2e2e, skeleton 20</summary>

**8 moves or less per insertion** (two comms): +14, 35 in all.

```
R L' F2 U R' D F' U' F2 R' U B * U' F2 B2 D B2 D2 F B2 U2
* = R F' R2 F B' D2 B R' // (8-0/29)
R L' F2 U R' D F' U' F2 R' U B R F' ^ R2 F B' D2 B R' U' F2 B2 D B2 D2 F B2 U2
^ = F2 U2 B2 L' B2 U2 F2 R' // (8-2/35)
Solution: R L' F2 U R' D F' U' F2 R' U B R F U2 B2 L' B2 U2 F2 R F B' D2 B R' U' F2 B2 D B2 D2 F B2 U2 (35)
```

**Up to 10 moves per insertion** (one alg for the whole leftover): +9, 30 in all.

```
R L' F2 U R' D F' U' F2 R' U B U' * F2 B2 D B2 D2 F B2 U2
* = U' R' F2 B2 D2 F2 B2 U2 R U // (10-1/30)
Solution: R L' F2 U R' D F' U' F2 R' U B U2 R' F2 B2 D2 F2 B2 U2 R U F2 B2 D B2 D2 F B2 U2 (30)
```

</details>

### 5e

An edge 5-cycle.

#### 5e, skeleton 1

Scramble: `R' U' F B2 R2 D L2 U B2 U' L2 U L2 F2 R' U R2 F' U2 B L' R' F' D R' U' F`

Skeleton: `D2 L F2 B R2 U' R' F R2 U' B' U F U' D' F'` (16)

Left: DB → UR → UF → DF → FR → DB

<details>
<summary>Answer for 5e, skeleton 1</summary>

**8 moves or less per insertion** (two comms): +13, 29 in all.

```
D2 L F2 B R2 U' R' F R2 U' B' U F U' D' F' *
* = D B2 L2 F2 U L2 B2 R2 // (8-0/24)
D2 L F2 B R2 U' R' F R2 U' B' U F U' D' F' D B2 ^ L2 F2 U L2 B2 R2
^ = B2 U2 F2 R U2 B2 D2 L // (8-3/29)
Solution: D2 L F2 B R2 U' R' F R2 U' B' U F U' D' F' U2 D F2 R U2 B2 D2 L' F2 U L2 B2 R2 (29)
```

**Up to 10 moves per insertion** (two comms): +12, 28 in all.

```
D2 L F2 B R2 U' R' F R2 U' B' ^ U F * U' D' F'
* = F D' F' D' F' D' F D F D // (10-3/23)
^ = F B' R F2 R' F' B U F2 U' // (10-5/28)
Solution: D2 L F2 B R2 U' R' F R2 U' F B2 R F2 R' F' B U D' F' D' F' D' F D F U' F' (28)
```

</details>

#### 5e, skeleton 2

Scramble: `R' U' F L2 D2 U2 F' U2 B R2 F2 R2 B2 U2 R' U' L2 B' U L U B' F2 R' U' F`

Skeleton: `D R2 F' B' U' L B' U2 D' F D2 L B U2 L D' F` (17)

Left: BL → FL → UR → DF → UL → BL

<details>
<summary>Answer for 5e, skeleton 2</summary>

**8 moves or less per insertion** (one alg for the whole leftover): +7, 24 in all.

```
D R2 F' B' U' L B' U2 D' F D2 L B U2 * L D' F
* = F B D F' B R' B2 // (7-0/24)
Solution: D R2 F' B' U' L B' U2 D' F D2 L B U2 F B D F' B R' B2 L D' F (24)
```

**Up to 10 moves per insertion**: nothing better, 24 stays the best.

</details>

#### 5e, skeleton 3

Scramble: `R' U' F U2 R2 U2 F' D2 B D2 L2 R2 B2 D2 L D' U L2 F' L' D U2 F2 R' U' F`

Skeleton: `D2 F' B U' R B2 L F' R2 U2 B' U' R B D B U F'` (18)

Left: BL → UL → UB → DR → UF → BL

<details>
<summary>Answer for 5e, skeleton 3</summary>

**8 moves or less per insertion** (two comms): +12, 30 in all.

```
D2 F' B U' R ^ B2 L F' R2 U2 B' U' R B * D B U F'
* = R2 B R2 D2 L2 F L2 D2 // (8-1/25)
^ = U2 F2 R2 F2 U2 B2 L2 B2 // (8-3/30)
Solution: D2 F' B U' R U2 F2 R2 F2 U2 B2 L' F' R2 U2 B' U' R B R2 B R2 D2 L2 F L2 D' B U F' (30)
```

**Up to 10 moves per insertion** (two comms): +10, 28 in all.

```
D2 F' B ^ U' R B2 * L F' R2 U2 B' U' R B D B U F'
* = F B' U R U' F' B L U' L' // (10-3/25)
^ = U' R L2 F' B D2 F B' R' U // (10-7/28)
Solution: D2 F' B U' R L2 F' B D2 F2 U R U' F' B L U' F' R2 U2 B' U' R B D B U F' (28)
```

</details>

#### 5e, skeleton 4

Scramble: `R' U' F U2 R2 F' D2 F' L2 B U2 F' R2 D2 F L2 D' L F D U2 B2 L2 D L' R' U' F`

Skeleton: `B L B2 L U' F2 B' U2 F2 D' R B D B2 R D F U D2` (19)

Left: UL → DF → DR → FR → DB → UL

<details>
<summary>Answer for 5e, skeleton 4</summary>

**8 moves or less per insertion** (two comms): +11, 30 in all.

```
B L B2 L U' F2 B' ^ U2 F2 D' R B D B2 R D * F U D2
* = F R L' F2 R' L D2 F' // (8-4/23)
^ = R2 B2 L2 D L2 B2 R2 U // (8-1/30)
Solution: B L B2 L U' F2 B' R2 B2 L2 D L2 B2 R2 U' F2 D' R B D B2 R D F R L' F2 R' L U (30)
```

**Up to 10 moves per insertion** (two comms): +9, 28 in all.

```
B L B2 L U' F2 B' U2 F2 D' R * B D B2 R D F U D2
* = R L D' R2 B2 R2 D' R' L' D2 // (10-1/28)
B L B2 L U' F2 B' U2 F2 D' ^ R2 L D' R2 B2 R2 D' R' L' D2 B D B2 R D F U D2
^ = L B2 L2 U L2 B2 R2 D R2 L' // (10-10/28)
Solution: B L B2 L U' F2 B' U2 F2 D' L B2 L2 U R2 L2 D' R' L' D2 B D B2 R D F U D2 (28)
```

</details>

#### 5e, skeleton 5

Scramble: `R' U' F B2 D L2 D' R2 U' L2 B2 D F2 D2 B2 L R2 D B R B2 D' U B D2 R' U' F`

Skeleton: `B2 D2 F' R2 D2 B L U2 R U' D2 B2 D2 R B U F' B2 R' F` (20)

Left: FL → BR → UL → DF → UB → FL

<details>
<summary>Answer for 5e, skeleton 5</summary>

**8 moves or less per insertion** (two comms): +13, 33 in all.

```
* B2 D2 F' R2 D2 B L U2 R U' D2 B2 D2 R B U F' B2 R' F
* = U' B2 R' L U2 R L' U // (8-0/28)
U' B2 R' L U2 ^ R L' U B2 D2 F' R2 D2 B L U2 R U' D2 B2 D2 R B U F' B2 R' F
^ = U2 B' U2 R2 D2 F' D2 R2 // (8-3/33)
Solution: U' B2 R' L B' U2 R2 D2 F' D2 R' L' U B2 D2 F' R2 D2 B L U2 R U' D2 B2 D2 R B U F' B2 R' F (33)
```

**Up to 10 moves per insertion** (one alg for the whole leftover): +8, 28 in all.

```
B2 D2 F' R2 D2 B L U2 R U' D2 B2 D2 R B U F' B2 * R' F
* = F2 U2 F B' R F' B U F2 // (9-1/28)
Solution: B2 D2 F' R2 D2 B L U2 R U' D2 B2 D2 R B U F B2 U2 F B' R F' B U F2 R' F (28)
```

</details>

#### 5e, skeleton 6

Scramble: `R' U' F U2 R2 F D2 F2 U2 B' R2 B' F L2 D2 L D' R' D' L B F' L U2 F R' U' F`

Skeleton: `U B U L U' L2 B U' D R U2 F2 D' B R2 U F' R2 L2 D B` (21)

Left: DL → UL → UR → FR → BR → DL

<details>
<summary>Answer for 5e, skeleton 6</summary>

**8 moves or less per insertion** (two comms): +11, 32 in all.

```
U B U L U' L2 B ^ U' D R U2 F2 D' B R2 U F' R2 L2 * D B
* = D F U2 F' B L2 B' D' // (8-4/25)
^ = R2 B U2 R2 D2 F L2 D2 // (8-1/32)
Solution: U B U L U' L2 B R2 B U2 R2 D2 F L2 U' D' R U2 F2 D' B R2 U F' R2 L2 D F U2 F' B L2 (32)
```

**Up to 10 moves per insertion** (one alg for the whole leftover): +10, 31 in all.

```
U B U L U' L2 B U' D * R U2 F2 D' B R2 U F' R2 L2 D B
* = L' U2 B' U F' B L' F U2 L // (10-0/31)
Solution: U B U L U' L2 B U' D L' U2 B' U F' B L' F U2 R L U2 F2 D' B R2 U F' R2 L2 D B (31)
```

</details>

#### 5e, skeleton 7

Scramble: `R' U' F R' B2 R B2 R D2 U2 B2 L' D2 R' D2 F R D2 F L B D L2 F R' U' F`

Skeleton: `U2 R F B2 U D2 F2 D B' U' R' D R2 F' U2 L' F' R2 F' L2 F' B` (22)

Left: DL → FR → BL → UF → DF → DL

<details>
<summary>Answer for 5e, skeleton 7</summary>

**8 moves or less per insertion** (one alg for the whole leftover): +7, 29 in all.

```
U2 R F B2 U D2 F2 D B' U' R' D R2 F' U2 L' F' R2 F' L2 F' B *
* = F' U L' U' D F D' F // (8-1/29)
Solution: U2 R F B2 U D2 F2 D B' U' R' D R2 F' U2 L' F' R2 F' L2 F2 B U L' U' D F D' F (29)
```

**Up to 10 moves per insertion**: nothing better, 29 stays the best.

</details>

#### 5e, skeleton 8

Scramble: `R' U' F R2 U2 R2 U2 F2 U L2 U' B2 U' L' D B2 D2 B R D2 F L U R' U' F`

Skeleton: `L' F' R2 D B2 D2 B' R B2 L2 B2 L U B2 U2 D'` (16)

Left: FL → UL → DB → UF → UB → FL

<details>
<summary>Answer for 5e, skeleton 8</summary>

**8 moves or less per insertion** (two comms): +13, 29 in all.

```
L' F' R2 D B2 D2 B' R B2 L2 B2 L U B2 * U2 D'
* = L2 F' D2 R2 U2 B' R2 D2 // (8-1/23)
L' F' R2 D B2 D2 B' R B2 L2 B2 L U B2 L2 F' D2 ^ R2 U2 B' R2 U2 D
^ = D2 B2 L' D2 F2 U2 R' F2 // (8-2/29)
Solution: L' F' R2 D B2 D2 B' R B2 L2 B2 L U B2 L2 F' B2 L' D2 F2 U2 R' F2 R2 U2 B' R2 U2 D (29)
```

**Up to 10 moves per insertion** (one alg for the whole leftover): +9, 25 in all.

```
L' F' R2 D B2 D2 * B' R B2 L2 B2 L U B2 U2 D'
* = R' B2 R F B' D' F' B' R // (9-0/25)
Solution: L' F' R2 D B2 D2 R' B2 R F B' D' F' B' R B' R B2 L2 B2 L U B2 U2 D' (25)
```

</details>

#### 5e, skeleton 9

Scramble: `R' U' F R2 U F2 R2 B2 L2 R2 D F2 L2 U2 L' D2 F L' B' U F R B U R' U' F`

Skeleton: `D2 F2 B' R2 B' U L' U' F B' R F' U F2 L F2 L2` (17)

Left: DL → DB → UF → FR → UB → DL

<details>
<summary>Answer for 5e, skeleton 9</summary>

**8 moves or less per insertion**: nothing fits anywhere in this skeleton.

**Up to 10 moves per insertion** (one alg for the whole leftover): +9, 26 in all.

```
D2 F2 B' R2 B' U L' U' F B' R F' U F2 L * F2 L2
* = D B L F' B D' F B2 D' // (9-0/26)
Solution: D2 F2 B' R2 B' U L' U' F B' R F' U F2 L D B L F' B D' F B2 D' F2 L2 (26)
```

</details>

#### 5e, skeleton 10

Scramble: `R' U' F R2 U2 B2 R2 D2 U2 F L2 U2 B' R2 D2 U2 B L' D' B' D' R' D F U' L R' U' F`

Skeleton: `B D2 R L U L B2 L2 D B D2 B2 D2 B U L U' F'` (18)

Left: DL → UL → DB → DF → BR → DL

<details>
<summary>Answer for 5e, skeleton 10</summary>

**8 moves or less per insertion**: nothing fits anywhere in this skeleton.

**Up to 10 moves per insertion** (one alg for the whole leftover): +8, 26 in all.

```
B D2 R L * U L B2 L2 D B D2 B2 D2 B U L U' F'
* = L F2 B' D F' B R' F' L' // (9-1/26)
Solution: B D2 R L2 F2 B' D F' B R' F' L' U L B2 L2 D B D2 B2 D2 B U L U' F' (26)
```

</details>

#### 5e, skeleton 11

Scramble: `R' U' F D2 L2 U' F2 U' L2 B2 L2 F2 U' F2 D' B U' R F2 D B F' U' F U R' U' F`

Skeleton: `D2 F' B' L2 B R2 L' U F L2 U2 L2 U' D F L2 B' R2 L` (19)

Left: DL → UL → DR → BL → BR → DL

<details>
<summary>Answer for 5e, skeleton 11</summary>

**8 moves or less per insertion** (two comms): +10, 29 in all.

```
D2 F' * B' L2 B R2 L' U F L2 U2 L2 U' D F L2 B' R2 L
* = F2 R2 B2 D' B2 R2 F2 U' // (8-1/26)
D2 F R2 B2 D' B2 R2 ^ F2 U' B' L2 B R2 L' U F L2 U2 L2 U' D F L2 B' R2 L
^ = R2 B2 R L' D2 R L // (7-4/29)
Solution: D2 F R2 B2 D' R L' D2 R L F2 U' B' L2 B R2 L' U F L2 U2 L2 U' D F L2 B' R2 L (29)
```

**Up to 10 moves per insertion** (two comms): +9, 28 in all.

```
D2 * F' B' L2 B R2 L' U F L2 U2 L2 U' D F L2 B' R2 L
* = F D B2 L2 B2 D F' B' D2 B // (10-2/27)
D2 F D B2 L2 B2 D F' ^ B' D2 F' L2 B R2 L' U F L2 U2 L2 U' D F L2 B' R2 L
^ = F D' B2 L2 F2 U' F2 L2 F' B2 // (10-9/28)
Solution: D2 F D F2 B2 U' F2 L2 F' B D2 F' L2 B R2 L' U F L2 U2 L2 U' D F L2 B' R2 L (28)
```

</details>

#### 5e, skeleton 12

Scramble: `R' U' F U2 F2 R2 B2 D' R2 B2 U2 R2 D F2 D L' B2 U F U2 R' B' D' B U' R' U' F`

Skeleton: `R' L2 B U D2 R U F2 B2 U2 B2 D2 B2 D' F2 D R U F' U'` (20)

Left: DL → UR → DF → BL → BR → DL

<details>
<summary>Answer for 5e, skeleton 12</summary>

**8 moves or less per insertion** (two comms): +15, 35 in all.

```
R' L2 B U * D2 R U F2 B2 U2 B2 D2 B2 D' F2 D R U F' U'
* = B' R F2 R' L D2 L' B // (8-0/28)
R' L2 B U B' R F2 ^ R' L D2 L' B D2 R U F2 B2 U2 B2 D2 B2 D' F2 D R U F' U'
^ = D2 B R2 D2 L2 F U2 L2 // (8-1/35)
Solution: R' L2 B U B' R F2 D2 B R2 D2 L2 F U2 R' L' D2 L' B D2 R U F2 B2 U2 B2 D2 B2 D' F2 D R U F' U' (35)
```

**Up to 10 moves per insertion** (two comms): +11, 31 in all.

```
R' L2 B U * D2 R U F2 B2 U2 B2 D2 B2 D' F2 D R U F' U'
* = L F U' D R2 U D' F L' // (9-0/29)
R' L2 B U L F U' D R2 U ^ D' F L' D2 R U F2 B2 U2 B2 D2 B2 D' F2 D R U F' U'
^ = U' R2 U D R' D2 F2 D2 R' D' // (10-8/31)
Solution: R' L2 B U L F D2 R' D2 F2 D2 R' D2 F L' D2 R U F2 B2 U2 B2 D2 B2 D' F2 D R U F' U' (31)
```

</details>

#### 5e, skeleton 13

Scramble: `R' U' F B2 R2 D F2 U R2 D L2 R2 U' L2 B2 R F D F R D U2 B L2 R' U' F`

Skeleton: `U' B2 L U R' F2 R' B2 R2 B' U' L' B' L2 F2 L2 F' U F U R2` (21)

Left: DL → UF → DR → UL → BR → DL

<details>
<summary>Answer for 5e, skeleton 13</summary>

**8 moves or less per insertion** (two comms): +13, 34 in all.

```
U' B2 L U R' F2 R' B2 R2 B' U' L' B' L2 F2 L2 F' U F U * R2
* = L D2 B2 U2 R B2 D2 F2 // (8-0/29)
U' B2 L U R' F2 R' B2 R2 B' U' L' B' L2 F2 L2 F' U F U L D2 B2 U2 ^ R B2 D2 F2 R2
^ = U2 B L2 D2 R2 F D2 L2 // (8-3/34)
Solution: U' B2 L U R' F2 R' B2 R2 B' U' L' B' L2 F2 L2 F' U F U L D2 B' L2 D2 R2 F D2 R L2 B2 D2 F2 R2 (34)
```

**Up to 10 moves per insertion** (two comms): +10, 31 in all.

```
U' B2 L U R' F2 R' B2 R2 B' U' * L' B' L2 F2 L2 F' U F U R2
* = D F2 B2 U' R' U F2 B2 D' L // (10-2/29)
U' B2 L U R' F2 R' B2 R2 B' U' D F2 B2 U' R' U ^ F2 B2 D' B' L2 F2 L2 F' U F U R2
^ = U' R U F D B R' B' D' F' // (10-8/31)
Solution: U' B2 L U R' F2 R' B2 R2 B' U' D F' B2 D B R' B' D' F B2 D' B' L2 F2 L2 F' U F U R2 (31)
```

</details>

#### 5e, skeleton 14

Scramble: `R' U' F B2 R2 B' L2 U2 L2 D2 F U2 B' R2 F' D2 L' B' U R' B R D U2 L2 R' U' F`

Skeleton: `L F' R F' B D' R F2 B' R' B L' U2 F R2 B L2 D' R' D F' D2` (22)

Left: UL → BR → UB → DR → UF → UL

<details>
<summary>Answer for 5e, skeleton 14</summary>

**8 moves or less per insertion** (two comms): +12, 34 in all.

```
L * F' R F' B D' R F2 B' R' B L' U2 F R2 B L2 D' R' D F' D2
* = L2 D' L2 F2 R2 U' R2 F2 // (8-2/28)
L' D' L2 F2 R2 ^ U' R2 F R F' B D' R F2 B' R' B L' U2 F R2 B L2 D' R' D F' D2
^ = R U D' F2 U' D R // (7-1/34)
Solution: L' D' L2 F2 R' U D' F2 U' D R U' R2 F R F' B D' R F2 B' R' B L' U2 F R2 B L2 D' R' D F' D2 (34)
```

**Up to 10 moves per insertion** (one alg for the whole leftover): +10, 32 in all.

```
L F' R F' B D' R F2 B' R' B * L' U2 F R2 B L2 D' R' D F' D2
* = L2 F U F2 B2 D' B' D2 F B' // (10-0/32)
Solution: L F' R F' B D' R F2 B' R' B L2 F U F2 B2 D' B' D2 F B' L' U2 F R2 B L2 D' R' D F' D2 (32)
```

</details>

#### 5e, skeleton 15

Scramble: `R' U' F L2 B' U2 L2 U2 L2 B2 R2 F L2 D2 U' L' F R2 D L2 R F' U' F U' R' U' F`

Skeleton: `R' B' R' D2 R2 B D2 B L U' B2 R B2 D2 B' U2` (16)

Left: DL → UF → DR → UR → UB → DL

<details>
<summary>Answer for 5e, skeleton 15</summary>

**8 moves or less per insertion** (two comms): +14, 30 in all.

```
R' B' R' D2 R2 B * D2 B L U' B2 R B2 D2 B' U2
* = D' R L' U2 R' L F2 D // (8-1/23)
R' B' R' D2 R2 B D' R L' U2 ^ R' L F2 D' B L U' B2 R B2 D2 B' U2
^ = U F2 L2 B2 D B2 L2 F2 // (8-1/30)
Solution: R' B' R' D2 R2 B D' R L' U' F2 L2 B2 D B2 L2 F2 R' L F2 D' B L U' B2 R B2 D2 B' U2 (30)
```

**Up to 10 moves per insertion** (one alg for the whole leftover): +9, 25 in all.

```
R' B' R' D2 R2 B D2 * B L U' B2 R B2 D2 B' U2
* = U' B2 L B2 U2 B2 L B2 U' // (9-0/25)
Solution: R' B' R' D2 R2 B U' D2 B2 L B2 U2 B2 L B2 U' B L U' B2 R B2 D2 B' U2 (25)
```

</details>

#### 5e, skeleton 16

Scramble: `R' U' F U2 L2 F2 R U2 B2 D2 R2 B2 L' D2 R2 U' F D2 L' R' U B U2 B' F2 R' U' F`

Skeleton: `R' F2 R D' B2 L' U' R D2 R2 U2 B' R' B2 U2 B U2` (17)

Left: DL → BR → DB → FR → BL → DL

<details>
<summary>Answer for 5e, skeleton 16</summary>

**8 moves or less per insertion** (two comms): +11, 28 in all.

```
R' F2 R D' B2 L' * U' R D2 R2 U2 B' R' B2 U2 B U2
* = F2 D2 R D2 F2 U2 L U2 // (8-1/24)
R' F2 R D' B2 L' F2 D2 ^ R D2 F2 U2 L U R D2 R2 U2 B' R' B2 U2 B U2
^ = D2 F L2 D2 R2 B U2 R2 // (8-4/28)
Solution: R' F2 R D' B2 L' F' L2 D2 R2 B U2 R' D2 F2 U2 L U R D2 R2 U2 B' R' B2 U2 B U2 (28)
```

**Up to 10 moves per insertion** (two comms): +10, 27 in all.

```
R' F2 R D' B2 L' U' R D2 ^ R2 U2 B' R' B2 U2 * B U2
* = F' U' B2 L2 B2 U' F B U2 B' // (10-4/23)
^ = D2 R' U' D B2 U D' R' D2 // (9-5/27)
Solution: R' F2 R D' B2 L' U2 D B2 U D' R' D2 R2 U2 B' R' B2 U2 F' U' B2 L2 B2 U' F B (27)
```

</details>

#### 5e, skeleton 17

Scramble: `R' U' F D2 B R2 D2 F D2 F' D2 F R2 B D2 R2 D B2 R F' D2 U2 B' U' F' R' U' F`

Skeleton: `B2 D B2 U2 R F2 L' U' L2 U2 L2 B2 D2 L' F' B2 L' B2` (18)

Left: FL → UB → UF → DF → DB → FL

<details>
<summary>Answer for 5e, skeleton 17</summary>

**8 moves or less per insertion** (two comms): +13, 31 in all.

```
B2 D B2 * U2 R F2 L' U' L2 U2 L2 B2 D2 L' F' B2 L' B2
* = L2 F2 R2 D' R2 F2 L2 U' // (8-1/25)
B2 D B2 L2 F2 R2 D' R2 F2 ^ L2 U R F2 L' U' L2 U2 L2 B2 D2 L' F' B2 L' B2
^ = F2 U2 L' U2 F2 D2 R' D2 // (8-2/31)
Solution: B2 D B2 L2 F2 R2 D' R2 U2 L' U2 F2 D2 R' D2 L2 U R F2 L' U' L2 U2 L2 B2 D2 L' F' B2 L' B2 (31)
```

**Up to 10 moves per insertion** (two comms): +11, 29 in all.

```
B2 D B2 U2 R * F2 L' U' L2 U2 L2 B2 D2 L' F' B2 L' B2
* = R2 D' R' D R2 L2 U' R U L2 // (10-1/27)
B2 D B2 U2 R' D' R' D R2 L2 U' R U ^ L2 F2 L' U' L2 U2 L2 B2 D2 L' F' B2 L' B2
^ = U' R' U R2 U' D B2 D' R U // (10-8/29)
Solution: B2 D B2 U2 R' D' R' D L2 U' D B2 D' R U L2 F2 L' U' L2 U2 L2 B2 D2 L' F' B2 L' B2 (29)
```

</details>

#### 5e, skeleton 18

Scramble: `R' U' F R2 B' U2 F R2 F' R2 F U2 L2 F' L2 R2 D B2 R' F D2 U' B D2 L U' R' U' F`

Skeleton: `D R2 U' B L' B' D' L2 B' U F' R' L2 B D2 F L' U2 R'` (19)

Left: UL → UF → BR → UR → DB → UL

<details>
<summary>Answer for 5e, skeleton 18</summary>

**8 moves or less per insertion**: nothing fits anywhere in this skeleton.

**Up to 10 moves per insertion** (one alg for the whole leftover): +8, 27 in all.

```
D R2 U' B L' B' D' * L2 B' U F' R' L2 B D2 F L' U2 R'
* = D' B' R2 D' L' D F R2 D L // (10-2/27)
Solution: D R2 U' B L' B' D2 B' R2 D' L' D F R2 D L' B' U F' R' L2 B D2 F L' U2 R' (27)
```

</details>

#### 5e, skeleton 19

Scramble: `R' U' F U2 R2 B2 D2 F2 D L2 U' L2 D B2 L R' D B F L F U2 B2 L R' U' F`

Skeleton: `U2 R' F2 R' F2 U' B2 R D2 B R' F' L' B U' F' B2 R2 B L` (20)

Left: DL → UB → DB → DF → DR → DL

<details>
<summary>Answer for 5e, skeleton 19</summary>

**8 moves or less per insertion**: nothing fits anywhere in this skeleton.

**Up to 10 moves per insertion** (two comms): +8, 28 in all.

```
U2 R' F2 * R' F2 ^ U' B2 R D2 B R' F' L' B U' F' B2 R2 B L
* = U2 R' U D' F U2 F' U' D R // (10-2/28)
^ = F2 U D' L2 D' F2 U2 D2 B2 U // (10-10/28)
Solution: U2 R' F2 U2 R' U D' F U2 F' L2 D' F2 U2 D2 R D2 B R' F' L' B U' F' B2 R2 B L (28)
```

</details>

#### 5e, skeleton 20

Scramble: `R' U' F L2 U2 L2 U2 F2 D2 B R2 B' L2 B2 D2 F D' B F2 L D' F2 U B' R F' R' U' F`

Skeleton: `R L' F2 U R' D F' U' F2 R' U B U' F2 B2 D B2 D2 F B2 U2` (21)

Left: UL → DF → UR → UF → UB → UL

<details>
<summary>Answer for 5e, skeleton 20</summary>

**8 moves or less per insertion** (two comms): +9, 30 in all.

```
^ R L' * F2 U R' D F' U' F2 R' U B U' F2 B2 D B2 D2 F B2 U2
* = D R L' F2 R' L D // (7-0/28)
^ = U2 R L' B2 R' L // (6-4/30)
Solution: U2 R L' B2 D R L' F2 R' L D F2 U R' D F' U' F2 R' U B U' F2 B2 D B2 D2 F B2 U2 (30)
```

**Up to 10 moves per insertion** (two comms): +8, 29 in all.

```
R L' F2 U ^ R' D F' U' F2 R' U B U' F2 B2 D B2 D2 F B2 * U2
* = F' B L F2 L' F B' U F2 U' // (10-4/27)
^ = U' F2 R' L U2 R L' F2 B2 U // (10-8/29)
Solution: U2 R L' F2 B2 U R' D F' U' F2 R' U B U' F2 B2 D B2 D2 B' L F2 L' F B' U F2 U (29)
```

</details>

## The tally

Over the 20 skeletons of each kind above, next to the same numbers from the big samples of the write-up (20,000 random skeletons of 20 moves at 8 moves per insertion; fewer at 10, see the write-up). One row per leftover; the counts are of the 20 skeletons.

| Leftover | On this page: mean added, 8 moves or less | On this page: nothing fits at 8 | On this page: mean added, up to 10 | On this page: up to 10 beats 8 or less | Write-up, 20-move skeletons: mean added, 8 or less | Write-up: mean added, up to 10 |
|---|---:|---:|---:|---:|---:|---:|
| 3c | 6.05 | 0 of 20 | 6.00 | 1 of 20 | 5.90 | 5.85 |
| 5c | 10.60 | 0 of 20 | 10.40 | 3 of 20 | 10.37 | 10.03 |
| pure 2c2c | 8.95 | 0 of 20 | 8.25 | 7 of 20 | 9.13 | 8.48 |
| twisted 2c2c | 8.80 | 0 of 20 | 8.80 | 0 of 20 | 8.73 | 8.66 |
| 3c1t | 9.85 | 0 of 20 | 9.65 | 2 of 20 | 9.90 | 9.73 |
| 2tc | 8.00 | 0 of 20 | 7.70 | 4 of 20 | 7.71 | 7.34 |
| 3tc | 9.65 | 0 of 20 | 9.55 | 1 of 20 | 9.50 | 9.34 |
| 3e | 5.42 | 8 of 20 | 5.95 | 11 of 20 | 5.95 | 6.05 |
| 2e2e | 9.26 | 1 of 20 | 7.35 | 13 of 20 | 9.29 | 7.63 |
| 5e | 11.50 | 4 of 20 | 9.15 | 18 of 20 | 10.94 | 9.06 |

Twenty skeletons are a handful: the page is for practice, the write-up has the odds. Every answer is the best there is for its cap, the answer key, not what you find in the time you have.
