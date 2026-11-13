# Examples: is there a DR-xs worth finishing?

Worked examples for the write-up *Is DR-xs worth it?*. First the tutorial's own example with the numbers. Then a hundred real scrambles: the slice-EO skips on each, the short DR-1s and DR-2s 8fe they lead to, and, folded away, how each one finishes and whether it beats the normal DRs on that scramble. Then the tally over all 500.

## The tutorial's first example, with the numbers

tseitsei89's DR-Xs tutorial walks through FMCL S9W3A2. Here are its steps, with what the tables say at each one.

```
R' U' F U R F B' U2 F' L2 U B2 L' F' R2 D2 F' R2 F B' L2 U' R' U' F // scramble
```

- **Slice-EO skips.** The tutorial lists two on normal and three on inverse. The count here: 2 on normal (E on F/B oriented, S on F/B oriented) and 3 on inverse (E on F/B oriented, M on U/D misoriented, M on F/B oriented).
- **`(R' D2 L U L)`**, the tutorial's "DR-2s in 5 moves": 2 slices, 2 flipped, 7 turns to DR. Two flipped edges with the centers right is a DR-2s by the table in section 3 of the write-up.
- **`(L' R)`** on top, which cancels to `(R' D2 L U R)`, the tutorial's "4a2-1s in 5": 1 slices, 4 flipped, 5 turns to DR. The tutorial says "The shortest possible setups for edges are 5 moves", which is the same count.
- **The finish.** The best finish of the form setup, slice, DR finish from that DR-1s is 15 moves, and its first move cancels with the last move of the route. Written out for the scramble:

  ```
  F2 U' L2 D' F2 R' L' U2 B D2 B R2 U2 B2 R U' L' D2 R // (19)
  ```

- The tutorial's own solution is 19 too. So on this DR-1s the method as taught finds the best there is of its form.

## 100 scrambles: what a slice EO gives you

The first hundred of the 500 random-state scrambles of the write-up's section 7. They're the same hundred as on the first study's examples page, with the same numbers, so you can put the normal DRs next to these.

**What's listed.** Every route here starts from a slice-EO skip or a one-move slice EO and then keeps the EO of that axis (the tutorial's route), or, for a DR-2s 8fe, may also start from a normal EO of 4 moves or fewer. Each scramble shows at most six DR-1s of 8 moves or less and at most two DR-2s 8fe of 9 or less, the shortest first, drawn at random among equals. Nothing is picked by how it finishes.

### How to read the tables

- **Skips**: the slice-EO skips of the scramble, on normal and on inverse, as slice, axis, and whether the four edges are all oriented or all misoriented.
- **Route**: the moves to the DR-xs. Brackets mean the whole route is on inverse. **Length**: its moves.
- **Kind**: DR-1s or DR-2s 8fe. **Starts from**: the slice EO the route starts from (for an 8fe possibly a normal EO).
- **Corner subset**: as in "4a2-1s". **Fewest turns to a real DR**: the fewest face turns from that state to a real DR (a DR-1s: 2 to 6, a DR-2s 8fe: 4).
- **Finish** (answers): the best finish of the method's form, setup, slice(s), DR finish. For the 8fe the setup is searched up to 3 moves from either end.
- **Solution** (answers): the whole solution for the scramble with all cancelling done; its length is the last column. A route on inverse is turned around for you.
- **Normal DRs** (answers): the best solution through any normal DR of 10, 11 and 12 moves or less on that scramble, each finished optimally (first study).

### The scrambles

#### Scramble 1

```
R' U' F L2 D' L2 F2 U' L2 D R2 U R2 B' R2 U R F U2 R' F R D' R U R' U' F // scramble
```

Skips: inverse: S slice on R/L, misoriented.

Each row is one route to a DR-xs on this scramble, shortest first; the last column is how far that DR-xs is from a real DR.

| # | Route | Length, moves | Kind | Starts from | Corner subset | Fewest turns to a real DR |
|---:|---|---:|---|---|---|---:|
| 1 | `(F R D L2 U B2 L)` | 7 | DR-1s | one-move slice EO: M slice on F/B, oriented | 4b3 | 5 |
| 2 | `(F R D L2 U B2 L')` | 7 | DR-1s | one-move slice EO: M slice on F/B, oriented | 4b3 | 6 |
| 3 | `(F' F2 R D L2 U B2 L')` | 8 | DR-1s | one-move slice EO: M slice on F/B, oriented | 4b3 | 6 |
| 4 | `(F L2 R' U L2 D F2 L')` | 8 | DR-1s | one-move slice EO: M slice on F/B, oriented | 4b3 | 6 |
| 5 | `(F R D L2 U' D2 F2 R)` | 8 | DR-1s | one-move slice EO: M slice on F/B, oriented | 4b3 | 5 |
| 6 | `(F R D B2 R2 D' F2 L)` | 8 | DR-1s | one-move slice EO: M slice on F/B, oriented | 4b3 | 6 |
| 7 | `(U' B' U' D L' R F' L)` | 8 | DR-2s 8fe | EO on U/D | 2c4 | 4 |
| 8 | `(U' B' U' D L' R F' L')` | 8 | DR-2s 8fe | EO on U/D | 2c4 | 4 |

Shown: 6 of the 14 DR-1s of 8 or less and 2 of the 26 DR-2s 8fe of 9 or less. Shortest normal DR: 10 moves.

<details>
<summary>Answers for scramble 1</summary>

Each row is the route with the same number above: the best finish of the method's form from it, then the whole solution written out for the scramble.

| # | Finish, moves | Solution | Solution length, moves |
|---:|---:|---|---:|
| 1 | 17 | `B2 D2 L' D2 R B2 U2 D2 L' F2 U D' B' L2 F D2 R2 L' B2 U' L2 D' R' F'` | 24 |
| 2 | 16 | `D2 L U2 F2 R B2 R' F2 U' D' B U2 F L2 F2 U2 L B2 U' L2 D' R' F'` | 23 |
| 3 | 16 | `D2 L U2 F2 R B2 R' F2 U' D' B U2 F L2 F2 U2 L B2 U' L2 D' R' F'` | 23 |
| 4 | 17 | `L U' D' F U2 B' D2 F L2 F2 D2 F' L2 F L2 U2 B L F2 D' L2 U' R L2 F'` | 25 |
| 5 | 16 | `F2 R2 D2 L' B2 L U' D B D2 L2 F R2 B2 R2 F' R' F2 U D2 L2 D' R' F'` | 24 |
| 6 | 17 | `U2 R2 F2 L' B2 R F2 B2 L' D2 L2 U D B L2 F L F2 D R2 B2 D' R' F'` | 24 |
| 7 | 14 | `F B' R L B' U2 B2 L2 B D2 R2 F' D2 B' L' F R' L U D' B U` | 22 |
| 8 | 14 | `U2 R D2 F2 L' F2 R2 B2 R F B R' L' B L F R' L U D' B U` | 22 |

Best of these: **22**, as short as the best through a normal DR of 10 or less. Normal DRs on this scramble: 22 through one of 10 or less, 20 through 11 or less, 20 through 12 or less.

</details>

#### Scramble 2

```
R' U' F L2 U L2 F2 D2 R2 B2 F2 D U' L' F2 R' F2 U B' D' L2 D2 F' U R' U' F // scramble
```

Skips: normal: M slice on F/B, oriented; inverse: E slice on U/D, misoriented.

Each row is one route to a DR-xs on this scramble, shortest first; the last column is how far that DR-xs is from a real DR.

| # | Route | Length, moves | Kind | Starts from | Corner subset | Fewest turns to a real DR |
|---:|---|---:|---|---|---|---:|
| 1 | `D2 L2 R' D R F2 R` | 7 | DR-1s | skip: M slice on F/B, oriented | 2c4 | 3 |
| 2 | `D2 L U' R' F2 L D` | 7 | DR-1s | skip: M slice on F/B, oriented | 4b5 | 5 |
| 3 | `D R U' R F2 D' L'` | 7 | DR-1s | skip: M slice on F/B, oriented | 4b2 | 5 |
| 4 | `D2 L2 R' D R F2 R'` | 7 | DR-1s | skip: M slice on F/B, oriented | 2c4 | 4 |
| 5 | `D2 L2 R' D L D2 L` | 7 | DR-1s | skip: M slice on F/B, oriented | 2c4 | 4 |
| 6 | `D R U' R F2 D' L` | 7 | DR-1s | skip: M slice on F/B, oriented | 4b2 | 4 |
| 7 | `(L' F U' F L2 D L2 U' B')` | 9 | DR-2s 8fe | one-move slice EO: E slice on R/L, misoriented | 2c3 | 4 |
| 8 | `(L' F U' F L2 D L2 U' B)` | 9 | DR-2s 8fe | one-move slice EO: E slice on R/L, misoriented | 2c3 | 4 |

Shown: 6 of the 66 DR-1s of 8 or less and 2 of the 2 DR-2s 8fe of 9 or less. Shortest normal DR: 9 moves.

<details>
<summary>Answers for scramble 2</summary>

Each row is the route with the same number above: the best finish of the method's form from it, then the whole solution written out for the scramble.

| # | Finish, moves | Solution | Solution length, moves |
|---:|---:|---|---:|
| 1 | 16 | `D2 R' L2 D R F2 R B U D B2 L U2 R2 B2 L F2 R F2 R' U2 L' F2` | 23 |
| 2 | 15 | `D2 L U' R' F2 L D' F R2 D2 B' U D R U2 B2 R F2 R B2 U2` | 21 |
| 3 | 15 | `D R U' R F2 D' L U2 F U D R' U2 L2 D2 F2 R' F2 L2 B2 R` | 21 |
| 4 | 17 | `D2 R' L2 D R F2 R B U D B2 L U2 R2 B2 L F2 R F2 R' U2 L' F2` | 23 |
| 5 | 15 | `D2 R' L2 D L D2 L U2 F D2 B2 U D R' B2 D2 R B2 R2 D2 L' B2` | 22 |
| 6 | 14 | `D R U' R F2 D' L U2 F U D R' U2 L2 D2 F2 R' F2 L2 B2 R` | 21 |
| 7 | 15 | `B2 U' B2 R2 D B2 U F2 R2 D R L U D R B U L2 D' L2 F' U F' L` | 24 |
| 8 | 15 | `U' D2 R' L' U D F2 B2 L B2 R B2 R2 B2 R2 B' U L2 D' L2 F' U F' L` | 24 |

Best of these: **21**, as short as the best through a normal DR of 11 or less. Normal DRs on this scramble: 22 through one of 10 or less, 21 through 11 or less, 20 through 12 or less.

</details>

#### Scramble 3

```
R' U' F L2 D2 L2 U2 R2 B2 R2 D F2 D' R' U' F' U2 L' U' B R U2 L2 U R' U' F // scramble
```

Skips: normal: E slice on R/L, oriented; inverse: E slice on F/B, oriented; inverse: S slice on F/B, misoriented.

Each row is one route to a DR-xs on this scramble, shortest first; the last column is how far that DR-xs is from a real DR.

| # | Route | Length, moves | Kind | Starts from | Corner subset | Fewest turns to a real DR |
|---:|---|---:|---|---|---|---:|
| 1 | `(R' U L2 D2 R2 U' L')` | 7 | DR-1s | skip: E slice on F/B, oriented | 2c4 | 5 |
| 2 | `(R' U L2 D2 R2 U' L)` | 7 | DR-1s | skip: E slice on F/B, oriented | 2c4 | 5 |
| 3 | `F' L' U' R' U' L' D2 L'` | 8 | DR-1s | one-move slice EO: M slice on F/B, misoriented | 2c3 | 5 |
| 4 | `(R' U2 D' B2 D2 F2 D' R')` | 8 | DR-1s | skip: E slice on F/B, oriented | 2c4 | 5 |
| 5 | `(R' U R2 L2 U2 L2 U L')` | 8 | DR-1s | skip: E slice on F/B, oriented | 2c4 | 5 |
| 6 | `(R' U L2 D2 R2 U' R2 L)` | 8 | DR-1s | skip: E slice on F/B, oriented | 2c4 | 6 |
| 7 | `F2 D2 F U' L F2 L` | 7 | DR-2s 8fe | EO on U/D | 2c4 | 4 |
| 8 | `F2 D2 F U' R U2 R'` | 7 | DR-2s 8fe | EO on U/D | 2c4 | 4 |

Shown: 6 of the 28 DR-1s of 8 or less and 2 of the 74 DR-2s 8fe of 9 or less. Shortest normal DR: 8 moves.

<details>
<summary>Answers for scramble 3</summary>

Each row is the route with the same number above: the best finish of the method's form from it, then the whole solution written out for the scramble.

| # | Finish, moves | Solution | Solution length, moves |
|---:|---:|---|---:|
| 1 | 15 | `F2 L2 B2 U' B2 L2 U D2 R L B' D2 B2 U2 F' L U R2 D2 L2 U' R` | 22 |
| 2 | 16 | `F2 L2 B2 U' B2 L2 U D2 R L B' D2 B2 U2 F' L U R2 D2 L2 U' R` | 22 |
| 3 | 15 | `F' L' U' R' U' L' D2 L' B2 U2 R2 U2 D F2 B2 R2 F2 U' R2 F' B L' B2` | 23 |
| 4 | 15 | `D R2 F2 U' B2 U F2 R2 F2 U' R L B' L2 F R D F2 D2 B2 U2 D R` | 23 |
| 5 | 16 | `U2 B2 U' R L' D2 L2 F D2 L2 D2 R2 B L2 B L' U' L2 U2 R2 L2 U' R` | 23 |
| 6 | 16 | `U' B2 R2 D2 B2 D' L2 D' L2 D' R L B' R2 F' U2 R2 L' U R2 D2 L2 U' R` | 24 |
| 7 | 16 | `F2 D2 F U' L F2 R' F B' L U2 L' F2 R U2 R F2 B2 R2 F2 B2` | 21 |
| 8 | 15 | `F2 D2 F U' R U2 R' B D2 L2 D2 L2 F R2 D2 B R' L F' B' R2 L` | 22 |

Best of these: **21**, longer than the best through a normal DR of 10 or less. Normal DRs on this scramble: 19 through one of 10 or less, 19 through 11 or less, 19 through 12 or less.

</details>

#### Scramble 4

```
R' U' F R2 B2 U2 F2 D U2 B2 D' L2 D' L B D U' L U' B2 F2 R2 F2 U' R' U' F // scramble
```

Skips: normal: M slice on U/D, oriented; inverse: M slice on R/L, oriented.

Each row is one route to a DR-xs on this scramble, shortest first; the last column is how far that DR-xs is from a real DR.

| # | Route | Length, moves | Kind | Starts from | Corner subset | Fewest turns to a real DR |
|---:|---|---:|---|---|---|---:|
| 1 | `F2 L2 R2 B' L2 R F'` | 7 | DR-1s | skip: M slice on U/D, oriented | 4b5 | 6 |
| 2 | `R' D2 B' U D2 B D` | 7 | DR-1s | one-move slice EO: M slice on R/L, oriented | 4b5 | 5 |
| 3 | `F2 L2 R2 B' L2 R F` | 7 | DR-1s | skip: M slice on U/D, oriented | 4b5 | 6 |
| 4 | `R' D2 F' L R2 B L` | 7 | DR-1s | skip: M slice on U/D, oriented | 4b5 | 5 |
| 5 | `R' D2 F' L R2 B L'` | 7 | DR-1s | skip: M slice on U/D, oriented | 4b5 | 5 |
| 6 | `R' D2 B' U D2 B D'` | 7 | DR-1s | one-move slice EO: M slice on R/L, oriented | 4b5 | 6 |
| 7 | `D2 R F U R U2 B2 R2 B` | 9 | DR-2s 8fe | EO on U/D | 4b5 | 4 |
| 8 | `D2 R F U R U2 F2 L2 B` | 9 | DR-2s 8fe | EO on U/D | 4b5 | 4 |

Shown: 6 of the 56 DR-1s of 8 or less and 2 of the 4 DR-2s 8fe of 9 or less. Shortest normal DR: 9 moves.

<details>
<summary>Answers for scramble 4</summary>

Each row is the route with the same number above: the best finish of the method's form from it, then the whole solution written out for the scramble.

| # | Finish, moves | Solution | Solution length, moves |
|---:|---:|---|---:|
| 1 | 17 | `F2 R2 L2 B' R L2 F' L2 D' F2 D' B2 D F B' U2 R U2 R2 D2 B2 R' F2 D2` | 24 |
| 2 | 17 | `R' D2 B' U D2 B U2 D B' L2 B U D L F2 B2 L2 F2 U2 L' D2 F2 B2 R` | 24 |
| 3 | 17 | `F2 R2 L2 B' R L2 F U L2 F2 D' F' B L' D2 R' F2 D2 L U2 R' F2 L B2` | 24 |
| 4 | 17 | `R' D2 F' R2 L B L U2 R2 D F B L' U2 L F2 B2 U2 R' U2 F2 L F2 B2` | 24 |
| 5 | 16 | `R' D2 F' R2 L B R2 L' D2 L2 D F B R' F2 L F2 U2 D2 R' D2 F2 R` | 23 |
| 6 | 17 | `R' D2 B' U D2 B D' F' L2 F' L2 F U' D L F2 D2 L B2 R2 F2 L B2 L` | 24 |
| 7 | 16 | `D2 R F U R U2 B2 R2 B' R' F B' R L F' D2 F R2 B L2 F2 R2 F D2` | 24 |
| 8 | 16 | `D2 R F U R U2 F2 L2 B R F2 D2 R' F2 L U2 F2 R F2 R' F B' R L' U2` | 25 |

Best of these: **23**, longer than the best through a normal DR of 10 or less. Normal DRs on this scramble: 20 through one of 10 or less, 20 through 11 or less, 19 through 12 or less.

</details>

#### Scramble 5

```
R' U' F U' L2 B2 R2 D R2 F2 D2 L2 R2 F' R2 D' F L U B' L' B L2 U R' U' F // scramble
```

Skips: none.

Each row is one route to a DR-xs on this scramble, shortest first; the last column is how far that DR-xs is from a real DR.

| # | Route | Length, moves | Kind | Starts from | Corner subset | Fewest turns to a real DR |
|---:|---|---:|---|---|---|---:|
| 1 | `U' L2 B' R' U2 D2 F' L` | 8 | DR-1s | one-move slice EO: E slice on U/D, oriented | 4b4 | 6 |
| 2 | `(F U' L U' L2 B2 U R)` | 8 | DR-1s | one-move slice EO: E slice on F/B, oriented | 2c3 | 6 |
| 3 | `(F U' L U' L2 B2 U R')` | 8 | DR-1s | one-move slice EO: E slice on F/B, oriented | 2c3 | 6 |
| 4 | `U' L2 B' R' U2 D2 F' L'` | 8 | DR-1s | one-move slice EO: E slice on U/D, oriented | 4b4 | 5 |
| 5 | `(F2 L' R2 F' R2 U' F2 R)` | 8 | DR-2s 8fe | EO on F/B | 4b5 | 4 |
| 6 | `(F2 L' R2 F L2 D B2 R')` | 8 | DR-2s 8fe | EO on F/B | 4b5 | 4 |

Shown: 4 of the 4 DR-1s of 8 or less and 2 of the 26 DR-2s 8fe of 9 or less. Shortest normal DR: 10 moves.

<details>
<summary>Answers for scramble 5</summary>

Each row is the route with the same number above: the best finish of the method's form from it, then the whole solution written out for the scramble.

| # | Finish, moves | Solution | Solution length, moves |
|---:|---:|---|---:|
| 1 | 16 | `U' L2 B' R' U2 D2 F' L B2 R2 U2 B D2 B L2 B R L' B2 D' R2 D B2 U` | 24 |
| 2 | 16 | `D2 F2 U D2 B2 R2 U F2 L2 B2 R' L' B L2 D2 B2 R' U' B2 L2 U L' U F'` | 24 |
| 3 | 15 | `U2 R2 F2 U2 D' L2 F2 D' R L F R2 U2 B2 R L2 U' B2 L2 U L' U F'` | 23 |
| 4 | 17 | `U' L2 B' R' U2 D2 F' L B2 R2 U2 B D2 B L2 B R L' B2 D' R2 D B2 U` | 24 |
| 5 | 16 | `U' D' R L' D' B2 U F2 U' F2 U R2 U' L2 U2 F2 R' F2 U R2 F R2 L F2` | 24 |
| 6 | 16 | `U2 F2 R U2 F2 L F2 L' B2 L U2 L' F2 U D L' B2 D' L2 F' R2 L F2` | 23 |

Best of these: **23**, longer than the best through a normal DR of 10 or less. Normal DRs on this scramble: 20 through one of 10 or less, 20 through 11 or less, 19 through 12 or less.

</details>

#### Scramble 6

```
R' U' F U R D2 L2 F' U R' F L' D2 B' R2 D2 R2 D F2 B2 D R2 U B2 R' U' F // scramble
```

Skips: normal: E slice on R/L, misoriented; normal: M slice on R/L, oriented; normal: S slice on R/L, misoriented.

Each row is one route to a DR-xs on this scramble, shortest first; the last column is how far that DR-xs is from a real DR.

| # | Route | Length, moves | Kind | Starts from | Corner subset | Fewest turns to a real DR |
|---:|---|---:|---|---|---|---:|
| 1 | `D B D' F U R2 L2 D'` | 8 | DR-1s | skip: E slice on R/L, misoriented | 2c5 | 4 |
| 2 | `U B D F2 L2 U' D' B'` | 8 | DR-1s | skip: S slice on R/L, misoriented | 2c5 | 5 |
| 3 | `U' D' F' U B' L2 F U` | 8 | DR-1s | skip: E slice on R/L, misoriented | 2c4 | 2 |
| 4 | `D' B2 F U2 B' D B2 U'` | 8 | DR-1s | skip: E slice on R/L, misoriented | 4b2 | 5 |
| 5 | `U B U D2 F2 D2 L2 B` | 8 | DR-1s | skip: S slice on R/L, misoriented | 2c5 | 5 |
| 6 | `U B U F' D2 B2 R2 B'` | 8 | DR-1s | skip: S slice on R/L, misoriented | 2c4 | 5 |
| 7 | `D' B' U' F' U L2 F D` | 8 | DR-2s 8fe | skip: E slice on R/L, misoriented | 4a2 | 4 |
| 8 | `U' D' F' U B' L2 F D'` | 8 | DR-2s 8fe | skip: E slice on R/L, misoriented | 2c4 | 4 |

Shown: 6 of the 76 DR-1s of 8 or less and 2 of the 34 DR-2s 8fe of 9 or less. Shortest normal DR: 9 moves.

<details>
<summary>Answers for scramble 6</summary>

Each row is the route with the same number above: the best finish of the method's form from it, then the whole solution written out for the scramble.

| # | Finish, moves | Solution | Solution length, moves |
|---:|---:|---|---:|
| 1 | 16 | `D B D' F U R2 L2 D' B2 D2 F U2 B' R2 B L2 U2 F2 U2 F R2 F R' L'` | 24 |
| 2 | 16 | `U B D F2 L2 U' D' B' L2 D' R2 F2 D' R2 U R2 U B2 U2 F2 U' B2 R' L'` | 24 |
| 3 | 14 | `U' D' F' U B' L2 F U B2 U2 R' L' D' B2 U R2 B2 U L2 F2 B2 U` | 22 |
| 4 | 14 | `D' F B2 U2 B' D B2 U' B2 U2 F U2 R2 L2 F L2 U2 B' U2 F' R L'` | 22 |
| 5 | 15 | `U B U D2 F2 D2 L2 B D' L2 B2 D B2 U' R2 U F2 U' D2 F2 R' L' B2` | 23 |
| 6 | 15 | `U B U F' D2 B2 R2 B L2 F2 R2 D F2 L2 U' L2 U R2 D' R L' D2` | 22 |
| 7 | 14 | `D' B' U' F' U L2 F D L F2 R2 U2 L' F2 L U D' R L F2 L2 D'` | 22 |
| 8 | 15 | `U' D' F' U B' L2 F D' R2 B2 L' U2 F2 R B2 L2 F2 L' U' D' R L D'` | 23 |

Best of these: **22**, longer than the best through a normal DR of 10 or less. Normal DRs on this scramble: 21 through one of 10 or less, 18 through 11 or less, 18 through 12 or less.

</details>

#### Scramble 7

```
R' U' F L2 U2 R2 U F2 U' L2 D' F2 D' F' L B' U' B2 L' D R' D F U' R' U' F // scramble
```

Skips: normal: M slice on U/D, misoriented; normal: S slice on F/B, misoriented; inverse: M slice on F/B, misoriented; inverse: S slice on U/D, misoriented.

Each row is one route to a DR-xs on this scramble, shortest first; the last column is how far that DR-xs is from a real DR.

| # | Route | Length, moves | Kind | Starts from | Corner subset | Fewest turns to a real DR |
|---:|---|---:|---|---|---|---:|
| 1 | `(D R U' L' F2 U L')` | 7 | DR-1s | skip: M slice on F/B, misoriented | 2c4 | 5 |
| 2 | `(R U' F2 R2 B2 U' L')` | 7 | DR-1s | skip: M slice on F/B, misoriented | 4a4 | 6 |
| 3 | `(D R U' L' F2 U L)` | 7 | DR-1s | skip: M slice on F/B, misoriented | 2c4 | 5 |
| 4 | `(R U' F2 R2 B2 U' L)` | 7 | DR-1s | skip: M slice on F/B, misoriented | 4a4 | 5 |
| 5 | `(R D L2 F2 L2 U L')` | 7 | DR-1s | skip: M slice on F/B, misoriented | 4a4 | 6 |
| 6 | `(R D L2 F2 L2 U L)` | 7 | DR-1s | skip: M slice on F/B, misoriented | 4a4 | 5 |
| 7 | `(F R L F B' L F' U2 L')` | 9 | DR-2s 8fe | skip: S slice on U/D, misoriented | 4b4 | 4 |
| 8 | `(F R L F B' L F' U2 L)` | 9 | DR-2s 8fe | skip: S slice on U/D, misoriented | 4b4 | 4 |

Shown: 6 of the 42 DR-1s of 8 or less and 2 of the 4 DR-2s 8fe of 9 or less. Shortest normal DR: 8 moves.

<details>
<summary>Answers for scramble 7</summary>

Each row is the route with the same number above: the best finish of the method's form from it, then the whole solution written out for the scramble.

| # | Finish, moves | Solution | Solution length, moves |
|---:|---:|---|---:|
| 1 | 17 | `F2 U2 R' U2 F' B U2 R2 F2 D' F2 D' B2 D B2 L2 U2 L U' F2 L U R' D'` | 24 |
| 2 | 18 | `U2 F2 R' F' B' U' L2 F2 D' R2 D' L2 B2 U2 B2 D B2 D L U B2 R2 F2 U R'` | 25 |
| 3 | 17 | `F2 U2 R' U2 F' B' U2 R2 F2 D F2 D' B2 D' R2 D2 B2 L' U' F2 L U R' D'` | 24 |
| 4 | 17 | `B2 D2 L' F B U2 R2 U' L2 U B2 U' R2 U B2 R2 U' L' U B2 R2 F2 U R'` | 24 |
| 5 | 17 | `U2 F2 R' D2 F B U2 L2 F2 U B2 U2 R2 U L2 D' F2 L U' L2 F2 L2 D' R'` | 24 |
| 6 | 17 | `D2 B2 L F' B' D L2 U2 L2 U' R2 D' F2 D' B2 U R2 L' U' L2 F2 L2 D' R'` | 24 |
| 7 | 15 | `F2 D2 L2 B' L2 F L2 F2 U2 B' U D F B' D L U2 F L' F' B R' L' F'` | 24 |
| 8 | 16 | `F2 D2 L2 B' L2 F L2 F2 U2 B' U D F B' D L U2 F L' F' B R' L' F'` | 24 |

Best of these: **24**, longer than the best through a normal DR of 10 or less. Normal DRs on this scramble: 21 through one of 10 or less, 21 through 11 or less, 20 through 12 or less.

</details>

#### Scramble 8

```
R' U' F D2 F2 L2 U2 F2 R2 D' F2 U L2 F L2 R' U B R2 F' U' R D2 R' U' F // scramble
```

Skips: normal: M slice on R/L, oriented; normal: M slice on F/B, oriented.

Each row is one route to a DR-xs on this scramble, shortest first; the last column is how far that DR-xs is from a real DR.

| # | Route | Length, moves | Kind | Starts from | Corner subset | Fewest turns to a real DR |
|---:|---|---:|---|---|---|---:|
| 1 | `B U R2 D' L2 F' D` | 7 | DR-1s | skip: M slice on R/L, oriented | 4a4 | 6 |
| 2 | `B U R2 D' L2 F' D'` | 7 | DR-1s | skip: M slice on R/L, oriented | 4a4 | 6 |
| 3 | `B D' F2 R2 U' L2 F' D` | 8 | DR-1s | skip: M slice on R/L, oriented | 4b2 | 4 |
| 4 | `B' U R2 U2 D R2 B' D'` | 8 | DR-1s | skip: M slice on R/L, oriented | 2c4 | 6 |
| 5 | `B U R2 D' L2 F' U2 D'` | 8 | DR-1s | skip: M slice on R/L, oriented | 4a4 | 6 |
| 6 | `B' D B2 U D2 L2 F' D'` | 8 | DR-1s | skip: M slice on R/L, oriented | 2c4 | 4 |

Shown: 6 of the 24 DR-1s of 8 or less and 0 of the 0 DR-2s 8fe of 9 or less. Shortest normal DR: 8 moves.

<details>
<summary>Answers for scramble 8</summary>

Each row is the route with the same number above: the best finish of the method's form from it, then the whole solution written out for the scramble.

| # | Finish, moves | Solution | Solution length, moves |
|---:|---:|---|---:|
| 1 | 17 | `B U R2 D' L2 F' D F R2 U2 F' U' D' F2 L' U2 L F2 U2 R B2 L' B2 L2` | 24 |
| 2 | 16 | `B U R2 D' L2 F' D' F' L2 B' L2 F2 U2 F U2 D2 L2 U D' R D2 R2 B2` | 23 |
| 3 | 16 | `B D' F2 R2 U' L2 F' D L2 F U2 F2 U D R L2 B2 L F2 R F2 B2 U2 B2` | 24 |
| 4 | 16 | `B' U R2 U2 D R2 B' D' F2 R2 B U2 B' R2 L2 F B' R2 U' D' R' U2 B2 L` | 24 |
| 5 | 17 | `B U R2 D' L2 F' U2 D F' L2 D2 F' B2 L2 D2 B2 U2 F U' D' L D2 L2 F2` | 24 |
| 6 | 16 | `B' D B2 U D2 L2 F' D' R2 L2 F2 U2 R2 F' U2 L2 F' L2 U D R' U2 B2 L` | 24 |

Best of these: **23**, longer than the best through a normal DR of 10 or less. Normal DRs on this scramble: 19 through one of 10 or less, 19 through 11 or less, 19 through 12 or less.

</details>

#### Scramble 9

```
R' U' F D2 B2 R2 F2 U L2 B2 D2 B2 U B R U R2 B' D2 L2 B' F' L' U R' U' F // scramble
```

Skips: normal: S slice on F/B, oriented; inverse: M slice on R/L, oriented.

Each row is one route to a DR-xs on this scramble, shortest first; the last column is how far that DR-xs is from a real DR.

| # | Route | Length, moves | Kind | Starts from | Corner subset | Fewest turns to a real DR |
|---:|---|---:|---|---|---|---:|
| 1 | `(F U R D' R' B2 U)` | 7 | DR-1s | one-move slice EO: M slice on F/B, oriented | 4b4 | 3 |
| 2 | `(F U R D' R' B2 U')` | 7 | DR-1s | one-move slice EO: M slice on F/B, oriented | 4b4 | 4 |
| 3 | `L' F' L2 F' D' B' L2 D` | 8 | DR-1s | one-move slice EO: S slice on R/L, oriented | 2c4 | 3 |
| 4 | `L' B2 D' R2 D' B D' B` | 8 | DR-1s | one-move slice EO: S slice on R/L, oriented | 4a4 | 5 |
| 5 | `(F U R D' L2 R F2 D')` | 8 | DR-1s | one-move slice EO: M slice on F/B, oriented | 4b4 | 5 |
| 6 | `(F U' D2 L D' L' F2 U)` | 8 | DR-1s | one-move slice EO: M slice on F/B, oriented | 4b4 | 4 |

Shown: 6 of the 34 DR-1s of 8 or less and 0 of the 0 DR-2s 8fe of 9 or less. Shortest normal DR: 9 moves.

<details>
<summary>Answers for scramble 9</summary>

Each row is the route with the same number above: the best finish of the method's form from it, then the whole solution written out for the scramble.

| # | Finish, moves | Solution | Solution length, moves |
|---:|---:|---|---:|
| 1 | 16 | `B2 U2 L' F2 L D2 F2 L2 B2 L U2 R2 U' D L2 F' U' B2 R D R' U' F'` | 23 |
| 2 | 17 | `B2 U2 L' F2 L D2 F2 L2 B2 L U2 R2 U' D L2 F' U' B2 R D R' U' F'` | 23 |
| 3 | 16 | `L' F' L2 F' D' B' L2 D R2 L U' D L2 F R2 B' D2 R2 B2 D2 R2 B' R2 L2` | 24 |
| 4 | 15 | `L' B2 D' R2 D' B D' B L2 B2 L2 D2 F2 L U D B' U2 B2 L2 B R2 B'` | 23 |
| 5 | 16 | `L D2 R' U2 B2 R' U2 R B2 L' U D' R2 B U2 D' F2 R' L2 D R' U' F'` | 23 |
| 6 | 17 | `R' F2 L B2 R' F2 R2 U2 L F2 D2 L U D F2 B' L2 U' F2 L D L' U D2 F'` | 25 |

Best of these: **23**, longer than the best through a normal DR of 10 or less. Normal DRs on this scramble: 19 through one of 10 or less, 19 through 11 or less, 18 through 12 or less.

</details>

#### Scramble 10

```
R' U' F D B2 D L2 D B2 D2 U' F2 R D B R2 U' R D2 U2 B2 R D' R' U' F // scramble
```

Skips: none.

Each row is one route to a DR-xs on this scramble, shortest first; the last column is how far that DR-xs is from a real DR.

| # | Route | Length, moves | Kind | Starts from | Corner subset | Fewest turns to a real DR |
|---:|---|---:|---|---|---|---:|
| 1 | `(U' L2 D2 L2 B' D2 F2 L')` | 8 | DR-1s | one-move slice EO: E slice on U/D, oriented | 4b4 | 5 |
| 2 | `(U' L2 F' B R2 D2 F R')` | 8 | DR-1s | one-move slice EO: E slice on U/D, oriented | 4b4 | 5 |
| 3 | `(U' L2 D2 L2 B' D2 F2 L)` | 8 | DR-1s | one-move slice EO: E slice on U/D, oriented | 4b4 | 6 |
| 4 | `(U' L2 F' B R2 D2 F R)` | 8 | DR-1s | one-move slice EO: E slice on U/D, oriented | 4b4 | 6 |
| 5 | `(U' L2 D2 L2 B' U2 B2 R)` | 8 | DR-1s | one-move slice EO: E slice on U/D, oriented | 4b4 | 6 |
| 6 | `(U' L2 D2 L2 B' U2 B2 R')` | 8 | DR-1s | one-move slice EO: E slice on U/D, oriented | 4b4 | 5 |

Shown: 6 of the 6 DR-1s of 8 or less and 0 of the 0 DR-2s 8fe of 9 or less. Shortest normal DR: 8 moves.

<details>
<summary>Answers for scramble 10</summary>

Each row is the route with the same number above: the best finish of the method's form from it, then the whole solution written out for the scramble.

| # | Finish, moves | Solution | Solution length, moves |
|---:|---:|---|---:|
| 1 | 16 | `L2 U2 B2 L2 U' R' L' F' R2 B2 U2 B' L2 F2 R2 B L F2 D2 B L2 D2 L2 U` | 24 |
| 2 | 15 | `U2 F2 R2 D' B2 R L B' L2 D2 F2 U2 F' D2 B' R F' D2 R2 F B' L2 U` | 23 |
| 3 | 17 | `D2 B2 L2 D' R L F' R2 B2 R2 D2 F' U2 B' D2 F2 D2 L' F2 D2 B L2 D2 L2 U` | 25 |
| 4 | 16 | `U2 F2 R2 D' B2 R L B' L2 D2 F2 U2 F' D2 B' R F' D2 R2 F B' L2 U` | 23 |
| 5 | 16 | `D2 F2 R2 U R' L' F B2 U2 R2 F2 R2 F' D2 B' R B2 U2 B L2 D2 L2 U` | 23 |
| 6 | 15 | `D2 F2 R2 U R' L' F B2 U2 R2 F2 R2 F' D2 B' R B2 U2 B L2 D2 L2 U` | 23 |

Best of these: **23**, longer than the best through a normal DR of 10 or less. Normal DRs on this scramble: 18 through one of 10 or less, 18 through 11 or less, 18 through 12 or less.

</details>

#### Scramble 11

```
R' U' F R2 D2 R2 U' B2 F2 D' L2 F2 R2 F' D2 L B2 U R' B' L2 B F U' R' U' F // scramble
```

Skips: normal: E slice on U/D, misoriented; inverse: S slice on U/D, misoriented; inverse: S slice on F/B, misoriented.

Each row is one route to a DR-xs on this scramble, shortest first; the last column is how far that DR-xs is from a real DR.

| # | Route | Length, moves | Kind | Starts from | Corner subset | Fewest turns to a real DR |
|---:|---|---:|---|---|---|---:|
| 1 | `(B L' B2 D2 R2 B2 U' R)` | 8 | DR-1s | one-move slice EO: E slice on F/B, oriented | 4a2 | 5 |
| 2 | `B L2 F2 U' L D' F2 R'` | 8 | DR-1s | one-move slice EO: M slice on F/B, oriented | 2c3 | 5 |
| 3 | `(B R' L' U2 D' L2 F2 R')` | 8 | DR-1s | one-move slice EO: E slice on F/B, oriented | 4b3 | 4 |
| 4 | `B L2 B2 D' R U' F2 L` | 8 | DR-1s | one-move slice EO: M slice on F/B, oriented | 2c3 | 6 |
| 5 | `D' F2 U2 F' L U2 R F'` | 8 | DR-1s | one-move slice EO: S slice on U/D, oriented | 4b5 | 6 |
| 6 | `(B L' U2 F2 U' R2 F2 L)` | 8 | DR-1s | one-move slice EO: E slice on F/B, oriented | 4a2 | 6 |

Shown: 6 of the 20 DR-1s of 8 or less and 0 of the 0 DR-2s 8fe of 9 or less. Shortest normal DR: 10 moves.

<details>
<summary>Answers for scramble 11</summary>

Each row is the route with the same number above: the best finish of the method's form from it, then the whole solution written out for the scramble.

| # | Finish, moves | Solution | Solution length, moves |
|---:|---:|---|---:|
| 1 | 14 | `U B2 D R L' F L2 B' U2 F' U2 L2 D2 B R' U B2 R2 D2 B2 L B'` | 22 |
| 2 | 15 | `B L2 F2 U' L D' F2 R' F2 L2 B' L2 F U2 R2 F' L2 F U D' L U2 B2` | 23 |
| 3 | 14 | `U2 R2 U F2 D2 L2 U B2 R L B U2 D2 R' F2 L2 U2 D R L B'` | 21 |
| 4 | 16 | `B L2 B2 D' R U' F2 L B2 L2 F U2 F D2 F' D2 L2 F' U D' R' F2 D2 F2` | 24 |
| 5 | 16 | `D' F2 U2 F' L U2 R F' D2 R2 L2 D L2 U R2 B2 U2 B2 U R L B U2 F` | 24 |
| 6 | 15 | `D L2 F2 U2 B2 U' R2 F2 U' R L' F U2 R2 F2 L' F2 R2 U F2 U2 L B'` | 23 |

Best of these: **21**, as short as the best through a normal DR of 11 or less. Normal DRs on this scramble: 21 through one of 10 or less, 21 through 11 or less, 20 through 12 or less.

</details>

#### Scramble 12

```
R' U' F R2 U' L2 U L B R' U D B D' L2 D B2 L2 B2 D' B2 D F2 R' U' F // scramble
```

Skips: none.

Each row is one route to a DR-xs on this scramble, shortest first; the last column is how far that DR-xs is from a real DR.

| # | Route | Length, moves | Kind | Starts from | Corner subset | Fewest turns to a real DR |
|---:|---|---:|---|---|---|---:|
| 1 | `L U' L2 U' B U L2 F'` | 8 | DR-1s | one-move slice EO: E slice on R/L, oriented | 4b4 | 6 |
| 2 | `L U' L2 U F U R2 B'` | 8 | DR-1s | one-move slice EO: E slice on R/L, oriented | 4b2 | 5 |
| 3 | `(D' R B' D2 B' L R' B)` | 8 | DR-1s | one-move slice EO: M slice on U/D, oriented | 2c3 | 6 |
| 4 | `L' B2 L2 U2 B L2 D' F'` | 8 | DR-1s | one-move slice EO: E slice on R/L, oriented | 4b2 | 5 |
| 5 | `L U' L2 U' B U L2 F` | 8 | DR-1s | one-move slice EO: E slice on R/L, oriented | 4b4 | 5 |
| 6 | `L R2 B U2 B' L2 D' B` | 8 | DR-1s | one-move slice EO: E slice on R/L, oriented | 4b5 | 5 |

Shown: 6 of the 14 DR-1s of 8 or less and 0 of the 0 DR-2s 8fe of 9 or less. Shortest normal DR: 10 moves.

<details>
<summary>Answers for scramble 12</summary>

Each row is the route with the same number above: the best finish of the method's form from it, then the whole solution written out for the scramble.

| # | Finish, moves | Solution | Solution length, moves |
|---:|---:|---|---:|
| 1 | 17 | `L U' L2 U' B U L2 F' D2 R' D2 R F B' D2 L2 F2 U B2 D' F2 D L2 U R2` | 25 |
| 2 | 16 | `L U' L2 U F U R2 B' R' F2 R F' B' D2 B2 U F2 D L2 F2 R2 L2 U2 B2` | 24 |
| 3 | 14 | `U2 B2 L U2 F B' U2 R2 B2 R2 D L2 D L2 B' R L' B D2 B R' D` | 22 |
| 4 | 16 | `L' B2 L2 U2 B L2 D' F' R' D2 R' U2 F' B' R2 D2 B2 D' F2 U F2 U2 R2 L2` | 24 |
| 5 | 17 | `L U' L2 U' B U L2 F R F2 R' F B' U2 L2 D' F2 U L2 D2 R2 B2 U' F2 U'` | 25 |
| 6 | 16 | `R2 L B U2 B' L2 D' B L D2 L F2 R' B2 U2 R' F B' U F2 U B2 D' R2` | 24 |

Best of these: **22**, longer than the best through a normal DR of 10 or less. Normal DRs on this scramble: 21 through one of 10 or less, 21 through 11 or less, 19 through 12 or less.

</details>

#### Scramble 13

```
R' U' F R2 D2 F2 U2 B2 L2 D U B2 U F L2 R2 D F' L' D' L U' L D' R' U' F // scramble
```

Skips: none.

No DR-1s of 8 moves or less and no DR-2s 8fe of 9 or less here. The shortest normal DR is 10 moves; the best solution through a normal DR of 12 or less is 20.

#### Scramble 14

```
R' U' F R2 F' R U R2 B' D2 L' F U' R U D' R2 L2 F2 R2 B2 D F2 B2 R' U' F // scramble
```

Skips: normal: M slice on U/D, misoriented.

Each row is one route to a DR-xs on this scramble, shortest first; the last column is how far that DR-xs is from a real DR.

| # | Route | Length, moves | Kind | Starts from | Corner subset | Fewest turns to a real DR |
|---:|---|---:|---|---|---|---:|
| 1 | `D2 R D2 L' U2 D2 F L` | 8 | DR-1s | skip: M slice on U/D, misoriented | 2c5 | 6 |
| 2 | `B' L2 R' B L' B F2 R'` | 8 | DR-1s | skip: M slice on U/D, misoriented | 4b3 | 5 |
| 3 | `(B L B2 U L D2 L U)` | 8 | DR-1s | one-move slice EO: S slice on F/B, oriented | 4b5 | 6 |
| 4 | `D2 R D2 L' U2 D2 F L'` | 8 | DR-1s | skip: M slice on U/D, misoriented | 2c5 | 5 |
| 5 | `(R' F2 U' L2 B R2 L2 D)` | 8 | DR-1s | one-move slice EO: E slice on R/L, misoriented | 4a3 | 5 |
| 6 | `(R' F2 U' L2 B R2 L2 D')` | 8 | DR-1s | one-move slice EO: E slice on R/L, misoriented | 4a3 | 6 |
| 7 | `L2 B F' L B R F R B'` | 9 | DR-2s 8fe | skip: M slice on U/D, misoriented | 4b5 | 4 |
| 8 | `L2 B F' L B R F R B` | 9 | DR-2s 8fe | skip: M slice on U/D, misoriented | 4b5 | 4 |

Shown: 6 of the 10 DR-1s of 8 or less and 2 of the 2 DR-2s 8fe of 9 or less. Shortest normal DR: 10 moves.

<details>
<summary>Answers for scramble 14</summary>

Each row is the route with the same number above: the best finish of the method's form from it, then the whole solution written out for the scramble.

| # | Finish, moves | Solution | Solution length, moves |
|---:|---:|---|---:|
| 1 | 17 | `D2 R D2 L' U2 D2 F L B R2 U2 F2 D2 F' D2 F' D2 L2 U' D R U2 L2 F2 L'` | 25 |
| 2 | 15 | `B' R' L2 B L' F2 B R' U2 F2 D2 B' U2 B U' D' L F2 U2 R U2 R D2` | 23 |
| 3 | 17 | `B R2 D2 F U' D' F2 R B2 R U2 B2 L2 B2 D2 L U L' D2 L' U' B2 L' B'` | 24 |
| 4 | 17 | `D2 R D2 L' U2 D2 F R2 L' F U2 F U' D' L F2 D2 R2 F2 R F2 B2 U2 R' L2` | 25 |
| 5 | 16 | `U F2 R2 D F2 D2 R' L' F' R2 B U2 D2 B U2 L2 D' R2 L2 B' L2 U F2 R` | 24 |
| 6 | 16 | `U' L2 D2 F2 R2 U' R' L' B2 D2 F' R2 F U2 D2 B D R2 L2 B' L2 U F2 R` | 24 |
| 7 | 16 | `L2 F' B L B R F R B' L2 U' R L' U D B2 L F2 R' D2 B2 L' B2 L B2` | 25 |
| 8 | 16 | `L2 F' B L B R F R B U L2 U2 F2 D' B2 U' R2 B2 D' R L' U D R' D2` | 25 |

Best of these: **23**, longer than the best through a normal DR of 10 or less. Normal DRs on this scramble: 21 through one of 10 or less, 21 through 11 or less, 19 through 12 or less.

</details>

#### Scramble 15

```
R' U' F U' B2 D' B2 U' B2 R2 B2 F2 D L U F' D2 L' D2 U' F' D' B2 R' U' F // scramble
```

Skips: none.

Each row is one route to a DR-xs on this scramble, shortest first; the last column is how far that DR-xs is from a real DR.

| # | Route | Length, moves | Kind | Starts from | Corner subset | Fewest turns to a real DR |
|---:|---|---:|---|---|---|---:|
| 1 | `U' B2 U2 R' B' L2 B' R` | 8 | DR-1s | one-move slice EO: S slice on U/D, oriented | 4b2 | 4 |
| 2 | `U' B2 U2 R' B' L2 B' R'` | 8 | DR-1s | one-move slice EO: S slice on U/D, oriented | 4b2 | 5 |

Shown: 2 of the 2 DR-1s of 8 or less and 0 of the 0 DR-2s 8fe of 9 or less. Shortest normal DR: 10 moves.

<details>
<summary>Answers for scramble 15</summary>

Each row is the route with the same number above: the best finish of the method's form from it, then the whole solution written out for the scramble.

| # | Finish, moves | Solution | Solution length, moves |
|---:|---:|---|---:|
| 1 | 16 | `U' B2 U2 R' B' L2 B' R L2 U2 D R' L' F R2 U2 D2 B U2 F2 U2 R2 D2 F'` | 24 |
| 2 | 15 | `U' B2 U2 R' B' L2 B' R' D' R2 L2 D R' L' B U2 F' R2 F' L2 U2 F' D2` | 23 |

Best of these: **23**, longer than the best through a normal DR of 10 or less. Normal DRs on this scramble: 21 through one of 10 or less, 21 through 11 or less, 21 through 12 or less.

</details>

#### Scramble 16

```
R' U' F R2 B' R2 U2 B2 D2 F' L2 D2 R2 D' L2 R F2 L' R F' U F2 U' F2 R' U' F // scramble
```

Skips: normal: S slice on R/L, oriented.

Each row is one route to a DR-xs on this scramble, shortest first; the last column is how far that DR-xs is from a real DR.

| # | Route | Length, moves | Kind | Starts from | Corner subset | Fewest turns to a real DR |
|---:|---|---:|---|---|---|---:|
| 1 | `F' U L2 B D2 F' U' B` | 8 | DR-1s | skip: S slice on R/L, oriented | 2c3 | 5 |
| 2 | `F' U L2 B D2 F' U' B'` | 8 | DR-1s | skip: S slice on R/L, oriented | 2c3 | 6 |

Shown: 2 of the 2 DR-1s of 8 or less and 0 of the 0 DR-2s 8fe of 9 or less. Shortest normal DR: 8 moves.

<details>
<summary>Answers for scramble 16</summary>

Each row is the route with the same number above: the best finish of the method's form from it, then the whole solution written out for the scramble.

| # | Finish, moves | Solution | Solution length, moves |
|---:|---:|---|---:|
| 1 | 16 | `F' U L2 B D2 F' U' B R2 D2 L U' D' F U2 B D2 B' D2 F2 U2 L2 B R2` | 24 |
| 2 | 15 | `F' U L2 B D2 F' U' B' R' F2 R2 D2 L' U2 R' B2 L' B2 U' D' B' U2 B2` | 23 |

Best of these: **23**, longer than the best through a normal DR of 10 or less. Normal DRs on this scramble: 19 through one of 10 or less, 19 through 11 or less, 19 through 12 or less.

</details>

#### Scramble 17

```
R' U' F L2 D2 L2 B2 D' B2 L2 R2 D2 U2 F U2 L' F2 D' F R D' B L' D R' U' F // scramble
```

Skips: none.

No DR-1s of 8 moves or less and no DR-2s 8fe of 9 or less here. The shortest normal DR is 10 moves; the best solution through a normal DR of 12 or less is 21.

#### Scramble 18

```
R' U' F L2 F2 L U2 B2 R D2 F2 L2 R U' D R' F' D' R2 U D2 F D R' U' F // scramble
```

Skips: normal: M slice on U/D, misoriented; normal: S slice on F/B, misoriented; inverse: M slice on F/B, misoriented; inverse: S slice on U/D, misoriented.

Each row is one route to a DR-xs on this scramble, shortest first; the last column is how far that DR-xs is from a real DR.

| # | Route | Length, moves | Kind | Starts from | Corner subset | Fewest turns to a real DR |
|---:|---|---:|---|---|---|---:|
| 1 | `L' D2 B' U2 F R'` | 6 | DR-1s | skip: M slice on U/D, misoriented | 4b5 | 5 |
| 2 | `L' D2 B' U2 F R` | 6 | DR-1s | skip: M slice on U/D, misoriented | 4b5 | 6 |
| 3 | `L2 B D2 B2 L' B2 L'` | 7 | DR-1s | skip: M slice on U/D, misoriented | 4a4 | 6 |
| 4 | `L U2 F D2 R2 F R'` | 7 | DR-1s | skip: M slice on U/D, misoriented | 4b5 | 6 |
| 5 | `L' F2 D2 B' U2 F R` | 7 | DR-1s | skip: M slice on U/D, misoriented | 2c3 | 6 |
| 6 | `L2 B D2 B2 R' U2 R` | 7 | DR-1s | skip: M slice on U/D, misoriented | 4a4 | 6 |
| 7 | `F L B' R' U L U L'` | 8 | DR-2s 8fe | EO on F/B | 2c5 | 4 |
| 8 | `F L B' R' U L U L` | 8 | DR-2s 8fe | EO on F/B | 2c5 | 4 |

Shown: 6 of the 144 DR-1s of 8 or less and 2 of the 38 DR-2s 8fe of 9 or less. Shortest normal DR: 8 moves.

<details>
<summary>Answers for scramble 18</summary>

Each row is the route with the same number above: the best finish of the method's form from it, then the whole solution written out for the scramble.

| # | Finish, moves | Solution | Solution length, moves |
|---:|---:|---|---:|
| 1 | 15 | `L' D2 B' U2 F R' F' U2 F' L2 U' D' L' B2 L U2 L2 B2 R D2 R2` | 21 |
| 2 | 16 | `L' D2 B' U2 F R' F' U2 F' L2 U' D' L' B2 L U2 L2 B2 R D2 R2` | 21 |
| 3 | 17 | `L2 B D2 B2 L' B2 R2 L' B D2 L2 F U' D B2 R2 U2 L B2 L2 B2 U2 R' U2` | 24 |
| 4 | 17 | `L U2 F D2 R2 F R' F' R2 D2 B' U D' F2 B2 D2 L D2 F2 L U2 R2 B2 R'` | 24 |
| 5 | 16 | `L' F2 D2 B' U2 F R D2 R2 B' R2 B U' D B2 R' L2 U2 B2 R F2 B2 L` | 23 |
| 6 | 18 | `L2 B D2 B2 R' U2 R L2 F2 R2 U2 F U' D' L D2 L' U2 L F2 R F2 L F2 B2` | 25 |
| 7 | 15 | `F L B' R' U L U R2 L' D B2 U' F2 L2 U' R2 U' D2 R L' U D L` | 23 |
| 8 | 16 | `F L B' R' U L U L U F2 R' L' U D' F2 L' F2 R U2 R2 L U2 F2 L` | 24 |

Best of these: **21**, as short as the best through a normal DR of 11 or less. Normal DRs on this scramble: 21 through one of 10 or less, 21 through 11 or less, 20 through 12 or less.

</details>

#### Scramble 19

```
R' U' F D2 F2 L2 F D2 F L2 F2 D2 F L R' B2 D R' D B2 R' B' D' R' U' F // scramble
```

Skips: normal: M slice on U/D, misoriented; normal: S slice on F/B, misoriented; inverse: M slice on F/B, misoriented.

Each row is one route to a DR-xs on this scramble, shortest first; the last column is how far that DR-xs is from a real DR.

| # | Route | Length, moves | Kind | Starts from | Corner subset | Fewest turns to a real DR |
|---:|---|---:|---|---|---|---:|
| 1 | `(F2 L2 R2 D L U2 R')` | 7 | DR-1s | skip: M slice on F/B, misoriented | 4a2 | 5 |
| 2 | `(F2 L2 R2 D R B2 L)` | 7 | DR-1s | skip: M slice on F/B, misoriented | 4a2 | 6 |
| 3 | `(F2 L2 R2 D R B2 L')` | 7 | DR-1s | skip: M slice on F/B, misoriented | 4a2 | 6 |
| 4 | `(F2 L2 R2 D L U2 R)` | 7 | DR-1s | skip: M slice on F/B, misoriented | 4a2 | 5 |
| 5 | `L2 F D2 R' B F D2 L` | 8 | DR-1s | skip: M slice on U/D, misoriented | 4b2 | 5 |
| 6 | `(F2 L2 R2 D L2 R' F2 L')` | 8 | DR-1s | skip: M slice on F/B, misoriented | 4a2 | 6 |
| 7 | `(F2 L2 R2 D L' U R2 D2 L')` | 9 | DR-2s 8fe | skip: M slice on F/B, misoriented | 4b3 | 4 |
| 8 | `F' R D2 L' F R2 F' D2 B'` | 9 | DR-2s 8fe | skip: M slice on U/D, misoriented | 2c3 | 4 |

Shown: 6 of the 40 DR-1s of 8 or less and 2 of the 24 DR-2s 8fe of 9 or less. Shortest normal DR: 9 moves.

<details>
<summary>Answers for scramble 19</summary>

Each row is the route with the same number above: the best finish of the method's form from it, then the whole solution written out for the scramble.

| # | Finish, moves | Solution | Solution length, moves |
|---:|---:|---|---:|
| 1 | 15 | `R' D2 R2 F2 L' F B U' B2 U2 L2 D' F2 U2 R L2 U2 L' D' R2 L2 F2` | 22 |
| 2 | 16 | `D2 F2 B2 L' D2 R2 U2 L2 B2 R' F' B U' L2 B2 U' L' B2 R' D' R2 L2 F2` | 23 |
| 3 | 17 | `D2 F2 B2 L' D2 R2 U2 L2 B2 R' F' B U' L2 B2 U' L' B2 R' D' R2 L2 F2` | 23 |
| 4 | 16 | `R' D2 R2 F2 L' F B U' B2 U2 L2 D' F2 U2 R L2 U2 L' D' R2 L2 F2` | 22 |
| 5 | 16 | `L2 F D2 R' F B D2 L B U2 B L2 U' D L2 D2 B2 L' D2 L' B2 L2 F2 D2` | 24 |
| 6 | 17 | `D2 F2 B2 L F2 R2 B2 L2 U2 R' F' B U' F2 R2 D L' F2 R L2 D' R2 L2 F2` | 24 |
| 7 | 14 | `U2 R F B R' L' F2 L2 B' L2 U2 B' R2 F2 L D2 R2 U' L D' R2 L2 F2` | 23 |
| 8 | 14 | `F' R D2 L' F R2 F' D2 B' R2 U F2 D B2 D F2 U R L U' D L' U2` | 23 |

Best of these: **22**, as short as the best through a normal DR of 10 or less. Normal DRs on this scramble: 22 through one of 10 or less, 21 through 11 or less, 21 through 12 or less.

</details>

#### Scramble 20

```
R' U' F R2 D2 U R2 D2 U' B2 F2 L2 B2 L B2 F2 R B U B D' L F2 U' R' U' F // scramble
```

Skips: normal: E slice on U/D, misoriented; normal: E slice on F/B, misoriented; normal: M slice on R/L, misoriented; inverse: E slice on U/D, misoriented; inverse: S slice on F/B, misoriented.

No DR-1s of 8 moves or less and no DR-2s 8fe of 9 or less here. The shortest normal DR is 10 moves; the best solution through a normal DR of 12 or less is 20.

#### Scramble 21

```
R' U' F U2 L2 D2 R2 U' L2 D L2 B2 D' L' D L' B' U' F' U L' D L2 U R' U' F // scramble
```

Skips: normal: E slice on R/L, misoriented; normal: S slice on R/L, oriented; inverse: E slice on U/D, misoriented; inverse: S slice on F/B, oriented.

Each row is one route to a DR-xs on this scramble, shortest first; the last column is how far that DR-xs is from a real DR.

| # | Route | Length, moves | Kind | Starts from | Corner subset | Fewest turns to a real DR |
|---:|---|---:|---|---|---|---:|
| 1 | `(D' R' U2 F' B2 R F' L')` | 8 | DR-1s | one-move slice EO: S slice on U/D, oriented | 4b5 | 6 |
| 2 | `R2 F D2 L2 D' B' U' F'` | 8 | DR-1s | skip: S slice on R/L, oriented | 4a2 | 6 |
| 3 | `R2 F' U2 B2 D F' U' B` | 8 | DR-1s | skip: S slice on R/L, oriented | 4b2 | 6 |
| 4 | `R2 F' U2 B2 D F' U' B'` | 8 | DR-1s | skip: S slice on R/L, oriented | 4b2 | 5 |
| 5 | `R2 B R2 U B D' B' U` | 8 | DR-1s | skip: S slice on R/L, oriented | 4a1 | 6 |
| 6 | `(D' R' U2 F' B2 R F' L)` | 8 | DR-1s | one-move slice EO: S slice on U/D, oriented | 4b5 | 6 |
| 7 | `R' D R B U' B2 R U'` | 8 | DR-2s 8fe | EO on F/B | 2c4 | 4 |
| 8 | `R' D R B U' B2 R U` | 8 | DR-2s 8fe | EO on F/B | 2c4 | 4 |

Shown: 6 of the 8 DR-1s of 8 or less and 2 of the 6 DR-2s 8fe of 9 or less. Shortest normal DR: 8 moves.

<details>
<summary>Answers for scramble 21</summary>

Each row is the route with the same number above: the best finish of the method's form from it, then the whole solution written out for the scramble.

| # | Finish, moves | Solution | Solution length, moves |
|---:|---:|---|---:|
| 1 | 17 | `D2 F' U2 L2 F R L U R2 D2 F2 U' F2 D F2 R2 U2 L F R' F B2 U2 R D` | 25 |
| 2 | 16 | `R2 F D2 L2 D' B' U' F L' F2 B2 U2 R2 F2 R F2 L U D F2 L2 F' R2` | 23 |
| 3 | 17 | `R2 F' U2 B2 D F' U' B' R' U2 L U' D' L2 F' R2 F2 B' D2 B' U2 R2 U2 F` | 24 |
| 4 | 16 | `R2 F' U2 B2 D F' U' B' R' U2 L U' D' L2 F' R2 F2 B' D2 B' U2 R2 U2 F` | 24 |
| 5 | 15 | `R2 B R2 U B D' B' U F2 B2 R L U2 R D2 R' F2 U' D L2 B' R2 L2` | 23 |
| 6 | 17 | `U2 L2 F D2 B' R2 F2 D2 R2 D2 B R' L' U B2 D' R2 L' F R' F B2 U2 R D` | 25 |
| 7 | 15 | `R' D R B U' B2 R D' R' L' D B2 R2 D F2 R2 D R2 F2 U' B2 D2` | 22 |
| 8 | 16 | `R' D R B U' B2 R D' R' L' D B2 R2 D F2 R2 D R2 F2 U' B2 D2` | 22 |

Best of these: **22**, longer than the best through a normal DR of 10 or less. Normal DRs on this scramble: 21 through one of 10 or less, 20 through 11 or less, 20 through 12 or less.

</details>

#### Scramble 22

```
R' U' F D2 F' R2 D2 B U2 B L2 B' L2 R B U2 L2 B' D' R' U' F U B2 F' R' U' F // scramble
```

Skips: none.

Each row is one route to a DR-xs on this scramble, shortest first; the last column is how far that DR-xs is from a real DR.

| # | Route | Length, moves | Kind | Starts from | Corner subset | Fewest turns to a real DR |
|---:|---|---:|---|---|---|---:|
| 1 | `(F' D' R D' L F2 U')` | 7 | DR-1s | one-move slice EO: E slice on F/B, misoriented | 2c3 | 3 |
| 2 | `(B U' D2 R D2 L' D)` | 7 | DR-1s | one-move slice EO: E slice on F/B, oriented | 0c4 | 6 |
| 3 | `(F' D' R D' L F2 U)` | 7 | DR-1s | one-move slice EO: E slice on F/B, misoriented | 2c3 | 4 |
| 4 | `(B' L' D L' U F2 L)` | 7 | DR-1s | one-move slice EO: E slice on F/B, oriented | 2c3 | 4 |
| 5 | `(B U' D2 R D2 L' D')` | 7 | DR-1s | one-move slice EO: E slice on F/B, oriented | 0c4 | 6 |
| 6 | `(B' L' D L' U F2 L')` | 7 | DR-1s | one-move slice EO: E slice on F/B, oriented | 2c3 | 3 |

Shown: 6 of the 36 DR-1s of 8 or less and 0 of the 0 DR-2s 8fe of 9 or less. Shortest normal DR: 9 moves.

<details>
<summary>Answers for scramble 22</summary>

Each row is the route with the same number above: the best finish of the method's form from it, then the whole solution written out for the scramble.

| # | Finish, moves | Solution | Solution length, moves |
|---:|---:|---|---:|
| 1 | 13 | `D F2 D' F2 D B2 D2 L2 U R2 F' B' L U F2 L' D R' D F` | 20 |
| 2 | 17 | `L2 U' B2 U L2 D2 B2 R2 L2 D B2 R L B R2 D2 F2 D' L D2 R' U D2 B'` | 24 |
| 3 | 14 | `D F2 D' F2 D B2 D2 L2 U R2 F' B' L U F2 L' D R' D F` | 20 |
| 4 | 15 | `U' R2 F2 U' R L F D2 F' L2 U2 L2 B U2 D2 L' F2 U' L D' L B` | 22 |
| 5 | 17 | `L2 F2 U B2 D' B2 U2 B2 R2 D F2 R L' B' L2 U2 B2 D L D2 R' U D2 B'` | 24 |
| 6 | 15 | `D2 L2 D F2 D2 R2 D R2 U B2 U R L F' B2 L F2 U' L D' L B` | 22 |

Best of these: **20**, as short as the best through a normal DR of 12 or less. Normal DRs on this scramble: 21 through one of 10 or less, 21 through 11 or less, 20 through 12 or less.

</details>

#### Scramble 23

```
R' U' F R2 D2 U' B2 U' R2 U' R2 L2 D R L2 D2 B L D' R' U2 F D' B2 R' U' F // scramble
```

Skips: normal: M slice on R/L, oriented.

Each row is one route to a DR-xs on this scramble, shortest first; the last column is how far that DR-xs is from a real DR.

| # | Route | Length, moves | Kind | Starts from | Corner subset | Fewest turns to a real DR |
|---:|---|---:|---|---|---|---:|
| 1 | `(L R2 F' D F2 U2 F D)` | 8 | DR-1s | one-move slice EO: E slice on R/L, oriented | 4b2 | 3 |
| 2 | `(L R2 F' D' B2 D2 F' D)` | 8 | DR-1s | one-move slice EO: E slice on R/L, oriented | 4b2 | 5 |
| 3 | `(L R2 F2 U F D2 R2 U')` | 8 | DR-1s | one-move slice EO: E slice on R/L, oriented | 2c5 | 6 |
| 4 | `(L R2 F2 U F U2 L2 U')` | 8 | DR-1s | one-move slice EO: E slice on R/L, oriented | 2c5 | 6 |
| 5 | `(L R2 F2 U F U2 L2 U)` | 8 | DR-1s | one-move slice EO: E slice on R/L, oriented | 2c5 | 5 |
| 6 | `(L R2 F' D' B2 D2 F' D')` | 8 | DR-1s | one-move slice EO: E slice on R/L, oriented | 4b2 | 4 |

Shown: 6 of the 8 DR-1s of 8 or less and 0 of the 0 DR-2s 8fe of 9 or less. Shortest normal DR: 9 moves.

<details>
<summary>Answers for scramble 23</summary>

Each row is the route with the same number above: the best finish of the method's form from it, then the whole solution written out for the scramble.

| # | Finish, moves | Solution | Solution length, moves |
|---:|---:|---|---:|
| 1 | 15 | `R2 U' F2 U B2 D F2 U' D2 B2 U F' B R2 L' D' F' U2 F2 D' F R2 L'` | 23 |
| 2 | 16 | `F2 R2 L2 U' F2 L2 D' F2 D' R2 U2 F' B R' D2 F2 D' F D2 B2 D F R2 L'` | 24 |
| 3 | 16 | `L2 D2 L2 U F2 D B2 L2 D L2 F' B' L F2 U2 R' U R2 D2 F' U' F2 R2 L'` | 24 |
| 4 | 17 | `B2 D2 L2 D R2 B2 U R2 U' F' B D2 B2 L' F2 D2 L' U L2 U2 F' U' F2 R2 L'` | 25 |
| 5 | 16 | `D2 F2 L2 U D2 B2 L2 D F' B' U2 R F2 R' B2 R' U' L2 U2 F' U' F2 R2 L'` | 24 |
| 6 | 16 | `F2 L2 B2 D' L2 D' L2 U2 F2 U D2 F' B D2 R F2 D F D2 B2 D F R2 L'` | 24 |

Best of these: **23**, longer than the best through a normal DR of 10 or less. Normal DRs on this scramble: 21 through one of 10 or less, 21 through 11 or less, 21 through 12 or less.

</details>

#### Scramble 24

```
R' U' F U' B2 U2 F2 U R2 F2 U' B2 U2 F L D' B L U L2 R' B' F' U R' U' F // scramble
```

Skips: inverse: M slice on F/B, misoriented.

Each row is one route to a DR-xs on this scramble, shortest first; the last column is how far that DR-xs is from a real DR.

| # | Route | Length, moves | Kind | Starts from | Corner subset | Fewest turns to a real DR |
|---:|---|---:|---|---|---|---:|
| 1 | `R' D F' U B2 U D' F'` | 8 | DR-1s | one-move slice EO: E slice on R/L, oriented | 4b2 | 5 |
| 2 | `R' D F2 D2 B D' L2 B` | 8 | DR-1s | one-move slice EO: E slice on R/L, oriented | 4b4 | 6 |
| 3 | `R F2 U2 F L2 U' D2 B'` | 8 | DR-1s | one-move slice EO: E slice on R/L, oriented | 2c5 | 6 |
| 4 | `R' D' B D2 F' D L2 B` | 8 | DR-1s | one-move slice EO: E slice on R/L, oriented | 2c3 | 6 |
| 5 | `(L2 U R2 U' R' D F2 R')` | 8 | DR-1s | skip: M slice on F/B, misoriented | 4a4 | 6 |
| 6 | `(L2 U R2 U' R' D F2 R)` | 8 | DR-1s | skip: M slice on F/B, misoriented | 4a4 | 6 |

Shown: 6 of the 10 DR-1s of 8 or less and 0 of the 0 DR-2s 8fe of 9 or less. Shortest normal DR: 9 moves.

<details>
<summary>Answers for scramble 24</summary>

Each row is the route with the same number above: the best finish of the method's form from it, then the whole solution written out for the scramble.

| # | Finish, moves | Solution | Solution length, moves |
|---:|---:|---|---:|
| 1 | 15 | `R' D F' U B2 U D' F' L2 B2 L' U2 B2 R' F2 L2 F2 D2 R F B' D L2` | 23 |
| 2 | 17 | `R' D F2 D2 B D' L2 B L B2 L2 D2 F2 B2 R' B2 L' F2 L B2 U2 L' F B D'` | 25 |
| 3 | 15 | `R F2 U2 F L2 U' D2 B D2 L U2 R F' B' D' F2 D R2 U B2 R2 B2` | 22 |
| 4 | 16 | `R' D' B D2 F' D L2 B R' U2 B2 L' F2 R' U2 F2 L2 B2 L D2 F' B' D' L2` | 24 |
| 5 | 16 | `L2 F2 R D2 R2 F2 L D2 F' B' U2 B2 D F2 L2 U R F2 D' R U R2 U' L2` | 24 |
| 6 | 17 | `U2 F2 R' U2 L2 B2 L' B2 L' F2 L F' B' U' R2 B2 U R' F2 D' R U R2 U' L2` | 25 |

Best of these: **22**, as short as the best through a normal DR of 10 or less. Normal DRs on this scramble: 22 through one of 10 or less, 20 through 11 or less, 20 through 12 or less.

</details>

#### Scramble 25

```
R' U' F L2 U' R D2 F' D2 R' B' L' R F' D' B2 D L2 R2 B2 U B2 L2 D' R' U' F // scramble
```

Skips: normal: S slice on F/B, oriented; inverse: E slice on R/L, misoriented; inverse: M slice on R/L, oriented; inverse: S slice on U/D, oriented; inverse: S slice on R/L, misoriented.

Each row is one route to a DR-xs on this scramble, shortest first; the last column is how far that DR-xs is from a real DR.

| # | Route | Length, moves | Kind | Starts from | Corner subset | Fewest turns to a real DR |
|---:|---|---:|---|---|---|---:|
| 1 | `L' D2 U2 F2 L' U'` | 6 | DR-1s | skip: S slice on F/B, oriented | 2c5 | 5 |
| 2 | `L' D2 U2 F2 L' U` | 6 | DR-1s | skip: S slice on F/B, oriented | 2c5 | 5 |
| 3 | `B2 R' F2 B2 D2 R' D'` | 7 | DR-1s | skip: S slice on F/B, oriented | 2c5 | 5 |
| 4 | `L' B2 R' B2 L2 F2 D` | 7 | DR-1s | skip: S slice on F/B, oriented | 2c5 | 6 |
| 5 | `L' D2 B2 R U2 F2 U` | 7 | DR-1s | skip: S slice on F/B, oriented | 2c5 | 5 |
| 6 | `L' B2 R' B2 L2 F2 D'` | 7 | DR-1s | skip: S slice on F/B, oriented | 2c5 | 6 |
| 7 | `(F' D' F' L2 U' L2 F2 D B')` | 9 | DR-2s 8fe | skip: S slice on R/L, misoriented | 2c4 | 4 |
| 8 | `(B' D L2 F2 U' B U B2 U)` | 9 | DR-2s 8fe | skip: S slice on R/L, misoriented | 4b4 | 4 |

Shown: 6 of the 196 DR-1s of 8 or less and 2 of the 22 DR-2s 8fe of 9 or less. Shortest normal DR: 8 moves.

<details>
<summary>Answers for scramble 25</summary>

Each row is the route with the same number above: the best finish of the method's form from it, then the whole solution written out for the scramble.

| # | Finish, moves | Solution | Solution length, moves |
|---:|---:|---|---:|
| 1 | 17 | `L' U2 D2 F2 L' U' L2 U2 B2 L U2 L U' D' F' R2 U2 D2 R2 D2 F L2 F` | 23 |
| 2 | 17 | `L' U2 D2 F2 L' U L2 D2 B2 R F2 R' D2 L D2 F2 U' D F U2 L2 F L2` | 23 |
| 3 | 17 | `B2 R' F2 B2 D2 R' U2 D' L D2 F2 L B2 R' F2 L2 U D B R2 D2 F U2 L2` | 24 |
| 4 | 16 | `L' B2 R' B2 L2 F2 D F2 B2 R2 L' D2 L' F2 U D F D2 B2 U2 F' L2 F` | 23 |
| 5 | 17 | `L' D2 B2 R U2 F2 U' R2 U2 L' U D F L2 D2 B U2 D2 L2 U2 B U2 B'` | 23 |
| 6 | 16 | `L' B2 R' B2 L2 F2 D' L' F2 L D2 R U D' F L2 D2 B D2 B L2 B' L2` | 23 |
| 7 | 15 | `R L F' B' L' U2 R D2 R F2 B2 L2 U2 R U2 B D' F2 L2 U L2 F D F` | 24 |
| 8 | 15 | `F' U2 F R' L F' B' U2 R2 U2 R U2 R' B2 R2 U' B2 U' B' U F2 L2 D' B` | 24 |

Best of these: **23**, longer than the best through a normal DR of 10 or less. Normal DRs on this scramble: 20 through one of 10 or less, 19 through 11 or less, 19 through 12 or less.

</details>

#### Scramble 26

```
R' U' F R' F2 R2 L F2 D2 R' D2 F' U' L' U' B2 U' F2 U' B2 L2 U2 R2 D' R' U' F // scramble
```

Skips: none.

Each row is one route to a DR-xs on this scramble, shortest first; the last column is how far that DR-xs is from a real DR.

| # | Route | Length, moves | Kind | Starts from | Corner subset | Fewest turns to a real DR |
|---:|---|---:|---|---|---|---:|
| 1 | `D' L F' B' R' U2 R2 F` | 8 | DR-1s | one-move slice EO: E slice on U/D, oriented | 4b2 | 6 |
| 2 | `D' L F' B' R' D2 L2 B'` | 8 | DR-1s | one-move slice EO: E slice on U/D, oriented | 4b2 | 5 |
| 3 | `D' L F' B' R' D2 L2 B` | 8 | DR-1s | one-move slice EO: E slice on U/D, oriented | 4b2 | 6 |
| 4 | `D' L2 B' L' U2 F2 R F'` | 8 | DR-1s | one-move slice EO: E slice on U/D, oriented | 2c3 | 6 |
| 5 | `D' L F' B' R' U2 R2 F'` | 8 | DR-1s | one-move slice EO: E slice on U/D, oriented | 4b2 | 5 |
| 6 | `D' L2 B' L' U2 F2 R F` | 8 | DR-1s | one-move slice EO: E slice on U/D, oriented | 2c3 | 6 |
| 7 | `F2 L' F U R D2 F2 R' D'` | 9 | DR-2s 8fe | EO on F/B | 2c4 | 4 |
| 8 | `B' U' F L F B R2 D F'` | 9 | DR-2s 8fe | EO on R/L | 4b2 | 4 |

Shown: 6 of the 6 DR-1s of 8 or less and 2 of the 4 DR-2s 8fe of 9 or less. Shortest normal DR: 8 moves.

<details>
<summary>Answers for scramble 26</summary>

Each row is the route with the same number above: the best finish of the method's form from it, then the whole solution written out for the scramble.

| # | Finish, moves | Solution | Solution length, moves |
|---:|---:|---|---:|
| 1 | 15 | `D' L F' B' R' U2 R2 F D2 L' D2 L B2 D2 R' L' F2 R' F B L2 B2 D'` | 23 |
| 2 | 14 | `D' L F' B' R' D2 L2 B' L' D2 L' B2 D2 R U2 F' B D' R2 B2 R2 B2` | 22 |
| 3 | 14 | `D' L F' B' R' D2 L2 F2 B D2 R D2 F2 R' U2 R2 U2 F2 R F' B D'` | 22 |
| 4 | 15 | `D' L2 B' L' U2 F2 R F' U2 L2 U2 F2 R' D2 L' B2 L' F2 B2 L F' B' D` | 23 |
| 5 | 15 | `D' L F' B' R' U2 R2 F' L' U2 F2 L' F2 L' U2 L D2 R' L2 U2 F B D'` | 23 |
| 6 | 15 | `D' L2 B' L' U2 F2 R F R' L' U2 F2 L' B2 R' B2 D2 F' B D2 L2 F2 D'` | 23 |
| 7 | 16 | `F2 L' F U R D2 F2 R' U' D2 R' L B2 D' F2 U L2 U' R2 U' R2 F2 D2 F2` | 24 |
| 8 | 12 | `B' U' F L F B R2 D F' B2 U D R2 D' B2 U' F' B' U D R2` | 21 |

Best of these: **21**, longer than the best through a normal DR of 10 or less. Normal DRs on this scramble: 18 through one of 10 or less, 18 through 11 or less, 18 through 12 or less.

</details>

#### Scramble 27

```
R' U' F D' R2 D L2 U' R2 D' B2 D' U' R U' F2 D2 B' F2 U F2 R' U' R' U' F // scramble
```

Skips: normal: M slice on F/B, misoriented; inverse: M slice on F/B, misoriented.

No DR-1s of 8 moves or less and no DR-2s 8fe of 9 or less here. The shortest normal DR is 11 moves; the best solution through a normal DR of 12 or less is 20.

#### Scramble 28

```
R' U' F U2 R2 D2 B2 R2 D' L2 D2 U' R2 B U' B' R F D2 F2 D' F L U R' U' F // scramble
```

Skips: normal: S slice on U/D, oriented.

Each row is one route to a DR-xs on this scramble, shortest first; the last column is how far that DR-xs is from a real DR.

| # | Route | Length, moves | Kind | Starts from | Corner subset | Fewest turns to a real DR |
|---:|---|---:|---|---|---|---:|
| 1 | `B' D2 L' F2 R' B` | 6 | DR-1s | skip: S slice on U/D, oriented | 2c3 | 5 |
| 2 | `B' D2 L' F2 R' B'` | 6 | DR-1s | skip: S slice on U/D, oriented | 2c3 | 5 |
| 3 | `D2 U2 F' L' D2 R' F` | 7 | DR-1s | skip: S slice on U/D, oriented | 4a3 | 5 |
| 4 | `U2 F' B2 L B' U2 B'` | 7 | DR-1s | skip: S slice on U/D, oriented | 4a1 | 6 |
| 5 | `L F R' F' R2 L' F'` | 7 | DR-1s | skip: S slice on U/D, oriented | 4b5 | 6 |
| 6 | `R F U2 B2 L F2 L'` | 7 | DR-1s | skip: S slice on U/D, oriented | 2c5 | 4 |
| 7 | `(F' L' D R' L2 F U' B2 D')` | 9 | DR-2s 8fe | EO on R/L | 4a4 | 4 |
| 8 | `(F' L' D R' L2 F D' R2 U')` | 9 | DR-2s 8fe | EO on R/L | 4a4 | 4 |

Shown: 6 of the 128 DR-1s of 8 or less and 2 of the 4 DR-2s 8fe of 9 or less. Shortest normal DR: 10 moves.

<details>
<summary>Answers for scramble 28</summary>

Each row is the route with the same number above: the best finish of the method's form from it, then the whole solution written out for the scramble.

| # | Finish, moves | Solution | Solution length, moves |
|---:|---:|---|---:|
| 1 | 16 | `B' D2 L' F2 R' B R2 D L2 U F2 U D2 F2 U F2 R L D2 F' U2 D2` | 22 |
| 2 | 15 | `B' D2 L' F2 R' B' D L2 D F2 R2 D B2 U' R' L F' R2 U2 R2 D2` | 21 |
| 3 | 16 | `U2 D2 F' L' D2 R' F R2 U L2 D B2 D' R2 B2 D2 R L' F' R2 F L2 D2` | 23 |
| 4 | 15 | `U2 F' B2 L B' U2 F2 B' D2 L2 F2 U' R L' F L2 F R2 F' B' D2 L2` | 22 |
| 5 | 14 | `L F R' F' R2 L' F' U' B2 D' B2 D R2 U' L2 F2 R L' B' U2 D2` | 21 |
| 6 | 15 | `R F U2 B2 L F2 L' D' L2 U' R2 B2 U' R2 F2 D' R L' D2 F R2 L2` | 22 |
| 7 | 17 | `U L2 D F2 R2 U2 L2 D R2 F2 D L2 U2 F' B' U B2 U F' R L2 D' L F` | 24 |
| 8 | 17 | `D L2 F2 R2 L2 D' F2 U2 L2 D R2 U' F2 U2 F B D' R2 D F' R L2 D' L F` | 25 |

Best of these: **21**, as short as the best through a normal DR of 11 or less. Normal DRs on this scramble: 21 through one of 10 or less, 21 through 11 or less, 20 through 12 or less.

</details>

#### Scramble 29

```
R' U' F U' F2 U2 B2 R2 B2 L2 F2 R2 U R B2 F U' L2 F' U B D' L U' R' U' F // scramble
```

Skips: inverse: S slice on U/D, oriented.

Each row is one route to a DR-xs on this scramble, shortest first; the last column is how far that DR-xs is from a real DR.

| # | Route | Length, moves | Kind | Starts from | Corner subset | Fewest turns to a real DR |
|---:|---|---:|---|---|---|---:|
| 1 | `(D2 U2 B R F U2 B' L)` | 8 | DR-1s | skip: S slice on U/D, oriented | 2c4 | 6 |
| 2 | `(D2 U2 B R F U2 B' L')` | 8 | DR-1s | skip: S slice on U/D, oriented | 2c4 | 5 |

Shown: 2 of the 2 DR-1s of 8 or less and 0 of the 0 DR-2s 8fe of 9 or less. Shortest normal DR: 8 moves.

<details>
<summary>Answers for scramble 29</summary>

Each row is the route with the same number above: the best finish of the method's form from it, then the whole solution written out for the scramble.

| # | Finish, moves | Solution | Solution length, moves |
|---:|---:|---|---:|
| 1 | 17 | `F2 U2 L2 F' L2 B L2 U2 F' L2 F2 R L U F2 D2 R2 L' B U2 F' R' B' U2 D2` | 25 |
| 2 | 17 | `B R2 L2 U2 B' L2 F' R2 B L2 F' R L' B2 D' B2 D2 L B U2 F' R' B' U2 D2` | 25 |

Best of these: **25**, longer than the best through a normal DR of 10 or less. Normal DRs on this scramble: 21 through one of 10 or less, 20 through 11 or less, 20 through 12 or less.

</details>

#### Scramble 30

```
R' U' F U2 L2 D' F2 U L2 R2 B2 U L2 F' U2 L' B' F2 D B U F2 U' R' U R' U' F // scramble
```

Skips: normal: M slice on R/L, misoriented; inverse: S slice on U/D, oriented.

Each row is one route to a DR-xs on this scramble, shortest first; the last column is how far that DR-xs is from a real DR.

| # | Route | Length, moves | Kind | Starts from | Corner subset | Fewest turns to a real DR |
|---:|---|---:|---|---|---|---:|
| 1 | `(F L' B R B D2 F L')` | 8 | DR-1s | skip: S slice on U/D, oriented | 4b5 | 5 |
| 2 | `(F L' B R B D2 F L)` | 8 | DR-1s | skip: S slice on U/D, oriented | 4b5 | 5 |

Shown: 2 of the 2 DR-1s of 8 or less and 0 of the 0 DR-2s 8fe of 9 or less. Shortest normal DR: 10 moves.

<details>
<summary>Answers for scramble 30</summary>

Each row is the route with the same number above: the best finish of the method's form from it, then the whole solution written out for the scramble.

| # | Finish, moves | Solution | Solution length, moves |
|---:|---:|---|---:|
| 1 | 17 | `F2 U2 B D2 R L U' F2 U L2 D B2 R2 U2 L2 D R2 L F' D2 B' R' B' L F'` | 25 |
| 2 | 16 | `B U2 F2 D2 B' U2 B' U2 R' L' D2 B2 R2 U B2 D' L' F' D2 B' R' B' L F'` | 24 |

Best of these: **24**, shorter than every normal DR of 10 or less gives. Normal DRs on this scramble: 25 through one of 10 or less, 22 through 11 or less, 20 through 12 or less.

</details>

#### Scramble 31

```
R' U' F D' F2 U L2 U L2 B2 R2 U2 R2 B F' D' B' U2 R F D' F2 U R' U' F // scramble
```

Skips: normal: S slice on R/L, oriented; inverse: E slice on F/B, misoriented.

Each row is one route to a DR-xs on this scramble, shortest first; the last column is how far that DR-xs is from a real DR.

| # | Route | Length, moves | Kind | Starts from | Corner subset | Fewest turns to a real DR |
|---:|---|---:|---|---|---|---:|
| 1 | `F B D B' D' B D'` | 7 | DR-1s | skip: S slice on R/L, oriented | 2c4 | 6 |
| 2 | `B D B' D' F B D'` | 7 | DR-1s | skip: S slice on R/L, oriented | 2c4 | 6 |
| 3 | `B D B' D F B D'` | 7 | DR-1s | skip: S slice on R/L, oriented | 2c4 | 4 |
| 4 | `F U' L2 U2 D2 B' U'` | 7 | DR-1s | skip: S slice on R/L, oriented | 4b3 | 6 |
| 5 | `F B D B' D' B D` | 7 | DR-1s | skip: S slice on R/L, oriented | 2c4 | 5 |
| 6 | `B D B' D F B D` | 7 | DR-1s | skip: S slice on R/L, oriented | 2c4 | 3 |

Shown: 6 of the 102 DR-1s of 8 or less and 0 of the 0 DR-2s 8fe of 9 or less. Shortest normal DR: 9 moves.

<details>
<summary>Answers for scramble 31</summary>

Each row is the route with the same number above: the best finish of the method's form from it, then the whole solution written out for the scramble.

| # | Finish, moves | Solution | Solution length, moves |
|---:|---:|---|---:|
| 1 | 15 | `F B D B' D' B U2 D' L2 F2 L' B2 U D F B2 R2 F L2 B L2 F2` | 22 |
| 2 | 16 | `B D B' D' F B D' B2 U2 L2 F2 L' B2 U D B' U2 B R2 B R2 U2 B2` | 23 |
| 3 | 16 | `B D B' D F B D R U D F' R2 F L2 B' D2 L2 F2 D2 F U2 B` | 22 |
| 4 | 13 | `F U' L2 U2 D2 B' U' L' F2 R U2 F2 L2 B2 R' U D F' L2 B` | 20 |
| 5 | 15 | `F B D B' D' B D R2 F2 R' F2 U D' F L2 F' L2 D2 F' B2 L2 B2` | 22 |
| 6 | 15 | `B D B' D F B D R U D F' R2 F L2 B' D2 L2 F2 D2 F U2 B` | 22 |

Best of these: **20**, longer than the best through a normal DR of 10 or less. Normal DRs on this scramble: 18 through one of 10 or less, 18 through 11 or less, 18 through 12 or less.

</details>

#### Scramble 32

```
R' U' F U2 R' B' R L2 U2 B L D' B U2 F B2 R2 D2 R2 L2 U L2 D' L2 D R' U' F // scramble
```

Skips: normal: S slice on U/D, misoriented.

Each row is one route to a DR-xs on this scramble, shortest first; the last column is how far that DR-xs is from a real DR.

| # | Route | Length, moves | Kind | Starts from | Corner subset | Fewest turns to a real DR |
|---:|---|---:|---|---|---|---:|
| 1 | `R D' L2 D B' R2 L2 F` | 8 | DR-1s | one-move slice EO: S slice on R/L, oriented | 4b4 | 5 |
| 2 | `R D' L2 D F' U2 D2 B'` | 8 | DR-1s | one-move slice EO: S slice on R/L, oriented | 4b4 | 4 |
| 3 | `R D' L2 D B' R2 L2 F'` | 8 | DR-1s | one-move slice EO: S slice on R/L, oriented | 4b4 | 4 |
| 4 | `R D' L2 D F U2 D2 B` | 8 | DR-1s | one-move slice EO: S slice on R/L, oriented | 4b4 | 5 |
| 5 | `R D' L2 D B R2 L2 F` | 8 | DR-1s | one-move slice EO: S slice on R/L, oriented | 4b4 | 5 |
| 6 | `R D' L2 D F U2 D2 B'` | 8 | DR-1s | one-move slice EO: S slice on R/L, oriented | 4b4 | 4 |

Shown: 6 of the 8 DR-1s of 8 or less and 0 of the 0 DR-2s 8fe of 9 or less. Shortest normal DR: 9 moves.

<details>
<summary>Answers for scramble 32</summary>

Each row is the route with the same number above: the best finish of the method's form from it, then the whole solution written out for the scramble.

| # | Finish, moves | Solution | Solution length, moves |
|---:|---:|---|---:|
| 1 | 17 | `R D' L2 D B' R2 L2 F B2 U2 R U D L2 F' D2 B2 R2 B R2 F' D2 L2 F2 U2` | 25 |
| 2 | 17 | `R D' L2 D F' U2 D2 B' D2 L U D R2 F B2 D2 F2 L2 B L2 F' U2 R2 B2 U2` | 25 |
| 3 | 17 | `R D' L2 D B' R2 L2 F' D2 L U D F B U2 F D2 R2 F2 D2 L2 B' U2 B R2` | 25 |
| 4 | 17 | `R D' L2 D F U2 D2 F2 B D2 L' U D F2 L2 F' U2 L2 F2 D2 L2 F' L2 F R2` | 25 |
| 5 | 17 | `R D' L2 D B R2 L2 F' D2 L' U' D' B' U2 L2 F' D2 L2 F' L2 B' D2 L2 B'` | 24 |
| 6 | 16 | `R D' L2 D F U2 D2 B' D2 R' F2 R U2 L' D2 R F2 U' D F' D2 B2 U2 F` | 24 |

Best of these: **24**, longer than the best through a normal DR of 10 or less. Normal DRs on this scramble: 20 through one of 10 or less, 20 through 11 or less, 20 through 12 or less.

</details>

#### Scramble 33

```
R' U' F U2 R2 U' L2 F2 D F2 D' R2 U2 L' F2 R2 F' R B' F2 D R D U2 R' U' F // scramble
```

Skips: none.

Each row is one route to a DR-xs on this scramble, shortest first; the last column is how far that DR-xs is from a real DR.

| # | Route | Length, moves | Kind | Starts from | Corner subset | Fewest turns to a real DR |
|---:|---|---:|---|---|---|---:|
| 1 | `D' F' L2 F' D2 R' F'` | 7 | DR-1s | one-move slice EO: S slice on U/D, oriented | 4b5 | 5 |
| 2 | `D' F' L2 F' D2 R' F` | 7 | DR-1s | one-move slice EO: S slice on U/D, oriented | 4b5 | 6 |
| 3 | `D D2 F' L2 F' D2 R' F` | 8 | DR-1s | one-move slice EO: S slice on U/D, oriented | 4b5 | 6 |
| 4 | `D D2 F' L2 F' D2 R' F'` | 8 | DR-1s | one-move slice EO: S slice on U/D, oriented | 4b5 | 5 |
| 5 | `U' B' L' B' R' F' L2 B'` | 8 | DR-1s | one-move slice EO: S slice on U/D, misoriented | 2c5 | 6 |
| 6 | `D F' L' F' D2 B2 L' F'` | 8 | DR-1s | one-move slice EO: S slice on U/D, oriented | 2c4 | 5 |
| 7 | `F D' R' B' R' F' B L F` | 9 | DR-2s 8fe | EO on U/D | 4b5 | 4 |
| 8 | `U' F2 B R' L F' R F' R'` | 9 | DR-2s 8fe | one-move slice EO: S slice on U/D, misoriented | 2c4 | 4 |

Shown: 6 of the 14 DR-1s of 8 or less and 2 of the 18 DR-2s 8fe of 9 or less. Shortest normal DR: 9 moves.

<details>
<summary>Answers for scramble 33</summary>

Each row is the route with the same number above: the best finish of the method's form from it, then the whole solution written out for the scramble.

| # | Finish, moves | Solution | Solution length, moves |
|---:|---:|---|---:|
| 1 | 17 | `D' F' L2 F' D2 R' F' B2 R2 D' L2 D B2 R L F R2 U2 F R2 F' U2 R2 L2` | 24 |
| 2 | 17 | `D' F' L2 F' D2 R' F L2 F2 U F2 D L2 U2 F2 U' R2 D R' L D2 F B2 L2` | 24 |
| 3 | 17 | `D' F' L2 F' D2 R' F L2 F2 U F2 D L2 U2 F2 U' R2 D R' L D2 F B2 L2` | 24 |
| 4 | 17 | `D' F' L2 F' D2 R' F' B2 R2 D' L2 D B2 R L F R2 U2 F R2 F' U2 R2 L2` | 24 |
| 5 | 16 | `U' B' L' B' R' F' L2 B' L D2 R U2 R2 B2 U2 D2 L' U2 L' U D F D2 F2` | 24 |
| 6 | 16 | `D F' L' F' D2 B2 L' F' B2 U' F2 U R L F R2 B2 R2 B U2 B U2 D2 F` | 24 |
| 7 | 16 | `F D' R' B' R' F' B L B R L' F2 D2 L2 F' U2 R2 B' L2 B R2 B' D2 F'` | 24 |
| 8 | 16 | `U' F2 B R' L F' R F' R' F B' U D F2 U2 D2 F' U2 B' L2 B D2 B' D2 B2` | 25 |

Best of these: **24**, longer than the best through a normal DR of 10 or less. Normal DRs on this scramble: 20 through one of 10 or less, 20 through 11 or less, 20 through 12 or less.

</details>

#### Scramble 34

```
R' U' F U' B D L F D2 B2 L' B' L B' R2 D L2 F2 L2 F2 U2 D' F2 D' R' U' F // scramble
```

Skips: none.

Each row is one route to a DR-xs on this scramble, shortest first; the last column is how far that DR-xs is from a real DR.

| # | Route | Length, moves | Kind | Starts from | Corner subset | Fewest turns to a real DR |
|---:|---|---:|---|---|---|---:|
| 1 | `(D' L F' D2 R L B R)` | 8 | DR-1s | one-move slice EO: E slice on U/D, oriented | 2c3 | 4 |
| 2 | `(D' L F' D2 R L B R')` | 8 | DR-1s | one-move slice EO: E slice on U/D, oriented | 2c3 | 5 |
| 3 | `(D' U2 R' U2 F R2 L B')` | 8 | DR-1s | one-move slice EO: E slice on U/D, oriented | 4a3 | 4 |
| 4 | `(D' U2 R' U2 F R2 L B)` | 8 | DR-1s | one-move slice EO: E slice on U/D, oriented | 4a3 | 5 |

Shown: 4 of the 4 DR-1s of 8 or less and 0 of the 0 DR-2s 8fe of 9 or less. Shortest normal DR: 9 moves.

<details>
<summary>Answers for scramble 34</summary>

Each row is the route with the same number above: the best finish of the method's form from it, then the whole solution written out for the scramble.

| # | Finish, moves | Solution | Solution length, moves |
|---:|---:|---|---:|
| 1 | 16 | `F2 R2 U R' L D2 L2 F D2 L2 F' R2 F' B' R2 D2 R' B' R' L' D2 F L' D` | 24 |
| 2 | 15 | `F2 R2 U' B2 R L' U2 B' R2 B R2 U2 F' D2 F R B' R' L' D2 F L' D` | 23 |
| 3 | 14 | `D B2 D2 F2 L2 F2 D L2 B2 U2 F B R' U2 B R2 L' F' U2 R U2 D` | 22 |
| 4 | 15 | `D B2 D2 F2 L2 F2 D L2 B2 U2 F B R' U2 B R2 L' F' U2 R U2 D` | 22 |

Best of these: **22**, longer than the best through a normal DR of 10 or less. Normal DRs on this scramble: 20 through one of 10 or less, 19 through 11 or less, 19 through 12 or less.

</details>

#### Scramble 35

```
R' U' F U B L2 U' L F2 D2 U' R B L D2 B2 R2 L2 B L2 B R2 D2 F' R' U' F // scramble
```

Skips: inverse: M slice on U/D, misoriented.

Each row is one route to a DR-xs on this scramble, shortest first; the last column is how far that DR-xs is from a real DR.

| # | Route | Length, moves | Kind | Starts from | Corner subset | Fewest turns to a real DR |
|---:|---|---:|---|---|---|---:|
| 1 | `(B2 R B D2 L U2 B R)` | 8 | DR-1s | skip: M slice on U/D, misoriented | 2c4 | 5 |
| 2 | `(L' R' F' R B' R' D2 R')` | 8 | DR-1s | skip: M slice on U/D, misoriented | 4b4 | 6 |
| 3 | `(B2 R B D2 L U2 B R')` | 8 | DR-1s | skip: M slice on U/D, misoriented | 2c4 | 6 |
| 4 | `(L' R' F' R B' R' D2 R)` | 8 | DR-1s | skip: M slice on U/D, misoriented | 4b4 | 6 |
| 5 | `(L' R' F' R B' L' F2 L)` | 8 | DR-1s | skip: M slice on U/D, misoriented | 4b4 | 6 |
| 6 | `(L' R' F' R B' L' F2 L')` | 8 | DR-1s | skip: M slice on U/D, misoriented | 4b4 | 5 |

Shown: 6 of the 6 DR-1s of 8 or less and 0 of the 0 DR-2s 8fe of 9 or less. Shortest normal DR: 9 moves.

<details>
<summary>Answers for scramble 35</summary>

Each row is the route with the same number above: the best finish of the method's form from it, then the whole solution written out for the scramble.

| # | Finish, moves | Solution | Solution length, moves |
|---:|---:|---|---:|
| 1 | 17 | `U2 R U2 B2 R B2 L' D2 L' D2 F2 R2 U' D' F' D2 B R' B' U2 L' D2 B' R' B2` | 25 |
| 2 | 17 | `R' F2 R D2 F2 R2 D2 B2 R2 L U D B' R2 F R2 B' R D2 R B R' F R L` | 25 |
| 3 | 16 | `B2 R U2 R' U D F U2 F2 L2 U2 F' L2 F' U2 B R B' U2 L' D2 B' R' B2` | 24 |
| 4 | 18 | `R' B2 R' F2 B2 L' B2 R F2 L B2 R' U D B U2 B R' L2 D2 R B R' F R L` | 26 |
| 5 | 17 | `F2 R' B2 R U2 L2 F2 B2 R' F2 U D B R2 B' D2 F' L' F2 L B R' F R L` | 25 |
| 6 | 18 | `F2 D2 B2 R L D2 B2 R F2 L F2 L2 U' D' F' L2 F' R2 L F2 L B R' F R L` | 26 |

Best of these: **24**, longer than the best through a normal DR of 10 or less. Normal DRs on this scramble: 21 through one of 10 or less, 21 through 11 or less, 20 through 12 or less.

</details>

#### Scramble 36

```
R' U' F D B2 R2 U' L2 B2 U F2 R2 F R' B' F' U L B2 D2 R' B U' R' U' F // scramble
```

Skips: normal: E slice on F/B, oriented; normal: M slice on U/D, oriented; normal: M slice on R/L, oriented; inverse: E slice on U/D, oriented; inverse: E slice on R/L, oriented.

Each row is one route to a DR-xs on this scramble, shortest first; the last column is how far that DR-xs is from a real DR.

| # | Route | Length, moves | Kind | Starts from | Corner subset | Fewest turns to a real DR |
|---:|---|---:|---|---|---|---:|
| 1 | `D' R U2 F2 D' L' D2 L` | 8 | DR-1s | skip: E slice on F/B, oriented | 4b3 | 6 |
| 2 | `(L2 F' U2 D2 R' F' B' L)` | 8 | DR-1s | skip: E slice on U/D, oriented | 2c5 | 4 |
| 3 | `(B' L2 F' U2 R F' B' L)` | 8 | DR-1s | skip: E slice on U/D, oriented | 4b2 | 5 |
| 4 | `(B2 R2 D B2 F' D2 B D)` | 8 | DR-1s | skip: E slice on R/L, oriented | 2c4 | 4 |
| 5 | `(F2 L2 U B2 F' U2 B U)` | 8 | DR-1s | skip: E slice on R/L, oriented | 2c4 | 5 |
| 6 | `D F' D L2 B U' R2 D` | 8 | DR-1s | skip: M slice on R/L, oriented | 2c4 | 6 |
| 7 | `L' U' R2 F' R' U F2 D L'` | 9 | DR-2s 8fe | EO on F/B | 4b5 | 4 |
| 8 | `B F L' F2 U' F' L2 F' D` | 9 | DR-2s 8fe | EO on R/L | 4b5 | 4 |

Shown: 6 of the 118 DR-1s of 8 or less and 2 of the 4 DR-2s 8fe of 9 or less. Shortest normal DR: 9 moves.

<details>
<summary>Answers for scramble 36</summary>

Each row is the route with the same number above: the best finish of the method's form from it, then the whole solution written out for the scramble.

| # | Finish, moves | Solution | Solution length, moves |
|---:|---:|---|---:|
| 1 | 15 | `D' R U2 F2 D' L' D2 L U2 F' R2 F D2 F L2 D2 F' B2 R L D L2 D2` | 23 |
| 2 | 17 | `U' R2 F2 U B2 U2 B2 L2 D F2 U R' L' F' D2 L2 U2 L' F B R U2 D2 F L2` | 25 |
| 3 | 16 | `U' L2 U' F2 R' L B2 R2 U2 L2 U2 L2 B' R2 B D2 L' F B R' U2 F L2 B` | 24 |
| 4 | 15 | `U R2 D L2 D F B' L' B2 L F2 L2 F2 U2 R D' B' D2 F B2 D' R2 B2` | 23 |
| 5 | 16 | `F2 U D2 R2 F2 B2 U2 B2 U' B2 U' F B R' B2 R2 U' B' U2 F B2 U' L2 F2` | 24 |
| 6 | 16 | `D F' D L2 B U' R2 D F L2 U2 B2 R2 B' U2 F' R2 F2 U' D R U2 B2 L2` | 24 |
| 7 | 16 | `L' U' R2 F' R' U F2 D L' U2 R L U D L B2 L2 D2 R B2 L B2 L' U2 L'` | 25 |
| 8 | 15 | `F B L' F2 U' F' L2 F' D F U D' F B D' B2 R2 L2 D B2 D' F2 R2 U` | 24 |

Best of these: **23**, longer than the best through a normal DR of 10 or less. Normal DRs on this scramble: 20 through one of 10 or less, 20 through 11 or less, 20 through 12 or less.

</details>

#### Scramble 37

```
R' U' F U2 B2 D2 R2 D' L2 D B2 U' L' B' D' U' B' D2 R D R' U2 F' R' U' F // scramble
```

Skips: normal: E slice on R/L, oriented; inverse: E slice on F/B, oriented.

Each row is one route to a DR-xs on this scramble, shortest first; the last column is how far that DR-xs is from a real DR.

| # | Route | Length, moves | Kind | Starts from | Corner subset | Fewest turns to a real DR |
|---:|---|---:|---|---|---|---:|
| 1 | `R2 D R2 F' U' L2 U'` | 7 | DR-1s | skip: E slice on R/L, oriented | 4b4 | 5 |
| 2 | `R2 D R2 F' D' B2 D` | 7 | DR-1s | skip: E slice on R/L, oriented | 4b4 | 5 |
| 3 | `(L2 F2 D L D R2 D)` | 7 | DR-1s | skip: E slice on F/B, oriented | 2c4 | 6 |
| 4 | `(L2 F2 D L U F2 U)` | 7 | DR-1s | skip: E slice on F/B, oriented | 2c4 | 5 |
| 5 | `(L2 F2 D L U F2 U')` | 7 | DR-1s | skip: E slice on F/B, oriented | 2c4 | 4 |
| 6 | `R2 D R2 F' U' L2 U` | 7 | DR-1s | skip: E slice on R/L, oriented | 4b4 | 4 |
| 7 | `(B U' D2 B' L D2 F2 U L')` | 9 | DR-2s 8fe | EO on F/B | 2c4 | 4 |
| 8 | `(B U' D2 B' L U2 B2 U R')` | 9 | DR-2s 8fe | EO on F/B | 2c4 | 4 |

Shown: 6 of the 66 DR-1s of 8 or less and 2 of the 8 DR-2s 8fe of 9 or less. Shortest normal DR: 8 moves.

<details>
<summary>Answers for scramble 37</summary>

Each row is the route with the same number above: the best finish of the method's form from it, then the whole solution written out for the scramble.

| # | Finish, moves | Solution | Solution length, moves |
|---:|---:|---|---:|
| 1 | 16 | `R2 D R2 F' U' L2 U' D2 R2 F2 L' B2 L' F2 L F' B' U' L2 D' R2 B2 D` | 23 |
| 2 | 14 | `R2 D R2 F' D' B2 D' R D2 B2 R D2 R2 F' B' D' B2 U2 D' R2` | 20 |
| 3 | 15 | `F2 U2 F2 R2 U' B2 D R2 U2 R L' F L2 D2 B' D' R2 D' L' D' F2 L2` | 22 |
| 4 | 15 | `F2 R2 U' F2 R2 L2 U F2 R L F U2 B2 R2 B' U' F2 U' L' D' F2 L2` | 22 |
| 5 | 16 | `F2 R2 U' F2 R2 L2 U F2 R L F U2 B2 R2 B' U' F2 U' L' D' F2 L2` | 22 |
| 6 | 17 | `R2 D R2 F' U' L2 U D2 R' U2 F2 R2 D2 R' B2 L2 F2 D2 F B' U R2 U R2` | 24 |
| 7 | 15 | `R' F2 L' D2 L2 F2 D2 L' B2 L' F2 L2 U D R U' F2 D2 L' B U D2 B'` | 23 |
| 8 | 15 | `L' U2 L U2 F2 R F2 L' B2 R2 D2 B2 U' D L' U' B2 U2 L' B U D2 B'` | 23 |

Best of these: **20**, longer than the best through a normal DR of 10 or less. Normal DRs on this scramble: 19 through one of 10 or less, 19 through 11 or less, 19 through 12 or less.

</details>

#### Scramble 38

```
R' U' F D B2 D2 L2 U L2 B2 U' L2 D2 F' R D' U2 F B' D' L B2 D2 B' U' R' U' F // scramble
```

Skips: normal: E slice on U/D, misoriented; normal: M slice on F/B, misoriented; inverse: E slice on F/B, misoriented; inverse: S slice on F/B, misoriented.

No DR-1s of 8 moves or less and no DR-2s 8fe of 9 or less here. The shortest normal DR is 11 moves; the best solution through a normal DR of 12 or less is 20.

#### Scramble 39

```
R' U' F D2 F2 D F2 U R2 F2 D R2 U2 B' D' L D2 F2 D' F2 U2 R D U' R' U' F // scramble
```

Skips: none.

Each row is one route to a DR-xs on this scramble, shortest first; the last column is how far that DR-xs is from a real DR.

| # | Route | Length, moves | Kind | Starts from | Corner subset | Fewest turns to a real DR |
|---:|---|---:|---|---|---|---:|
| 1 | `(L' D' B' U L' F' B R B')` | 9 | DR-2s 8fe | EO on U/D | 2c3 | 4 |
| 2 | `(L' D' B' U L' F' B R B)` | 9 | DR-2s 8fe | EO on U/D | 2c3 | 4 |

Shown: 0 of the 0 DR-1s of 8 or less and 2 of the 2 DR-2s 8fe of 9 or less. Shortest normal DR: 10 moves.

<details>
<summary>Answers for scramble 39</summary>

Each row is the route with the same number above: the best finish of the method's form from it, then the whole solution written out for the scramble.

| # | Finish, moves | Solution | Solution length, moves |
|---:|---:|---|---:|
| 1 | 15 | `B2 L2 D2 B2 L2 B D2 F D2 R' L' F' B R' B' R' F B' L U' B D L` | 23 |
| 2 | 14 | `B2 L2 D2 B2 L2 B D2 F D2 R' L' F' B R' B' R' F B' L U' B D L` | 23 |

Best of these: **23**, as short as the best through a normal DR of 10 or less. Normal DRs on this scramble: 23 through one of 10 or less, 22 through 11 or less, 21 through 12 or less.

</details>

#### Scramble 40

```
R' U' F U2 B2 R2 B2 U R2 U F2 D' U2 R F' U' R' D2 L2 B' U2 B' R' F' R' U' F // scramble
```

Skips: normal: S slice on U/D, misoriented; normal: S slice on F/B, misoriented; inverse: S slice on U/D, misoriented; inverse: S slice on F/B, misoriented.

Each row is one route to a DR-xs on this scramble, shortest first; the last column is how far that DR-xs is from a real DR.

| # | Route | Length, moves | Kind | Starts from | Corner subset | Fewest turns to a real DR |
|---:|---|---:|---|---|---|---:|
| 1 | `F2 B' L U2 F' R' B` | 7 | DR-1s | skip: S slice on U/D, misoriented | 4b2 | 6 |
| 2 | `F2 B' L U2 F' R' B'` | 7 | DR-1s | skip: S slice on U/D, misoriented | 4b2 | 6 |
| 3 | `R2 F2 L U2 F' B2 L' B'` | 8 | DR-1s | skip: S slice on U/D, misoriented | 2c3 | 5 |
| 4 | `F2 D2 B' L U2 F' R' B` | 8 | DR-1s | skip: S slice on U/D, misoriented | 4b2 | 6 |
| 5 | `(U2 F U2 R F L U2 B')` | 8 | DR-1s | skip: S slice on U/D, misoriented | 4b2 | 6 |
| 6 | `F B2 L' U2 R' B' R2 F` | 8 | DR-1s | skip: S slice on U/D, misoriented | 4a2 | 6 |
| 7 | `R' U2 B R F2 L F U2 F` | 9 | DR-2s 8fe | skip: S slice on U/D, misoriented | 2c3 | 4 |
| 8 | `B R2 F2 L' U2 F B2 L' F'` | 9 | DR-2s 8fe | skip: S slice on U/D, misoriented | 4a2 | 4 |

Shown: 6 of the 40 DR-1s of 8 or less and 2 of the 12 DR-2s 8fe of 9 or less. Shortest normal DR: 10 moves.

<details>
<summary>Answers for scramble 40</summary>

Each row is the route with the same number above: the best finish of the method's form from it, then the whole solution written out for the scramble.

| # | Finish, moves | Solution | Solution length, moves |
|---:|---:|---|---:|
| 1 | 15 | `F2 B' L U2 F' R' B' R2 D2 F2 R2 U2 R' D2 R' B2 U' D' F D2 B'` | 21 |
| 2 | 14 | `F2 B' L U2 F' R' B' R2 D2 F2 R2 U2 R' D2 R' B2 U' D' F D2 B'` | 21 |
| 3 | 15 | `R2 F2 L U2 F' B2 L' F2 B' U2 B2 R2 D2 L' F2 D2 F2 U D L2 B' L2 F'` | 23 |
| 4 | 16 | `F2 D2 B' L U2 F' R' B U2 L U2 F2 U2 L' U D F' U2 R2 L2 F R2 D2 L2` | 24 |
| 5 | 15 | `U2 F' U D' R D2 L2 U2 L' F2 R U2 L2 F2 B' U2 L' F' R' U2 F' U2` | 22 |
| 6 | 17 | `F B2 L' U2 R' B' R2 F B2 L2 D2 R D2 F2 R D2 L' F2 R' U' D' B L2 F' R2` | 25 |
| 7 | 14 | `R' U2 B R F2 L F U2 B U D R2 F2 B D2 L2 U2 D2 B' D2 R2 B` | 22 |
| 8 | 15 | `B R2 F2 L' U2 F B2 L' B U' D' B2 R2 F D2 B2 L2 D2 R2 U2 F' L2 D2` | 23 |

Best of these: **21**, as short as the best through a normal DR of 12 or less. Normal DRs on this scramble: 21 through one of 10 or less, 21 through 11 or less, 21 through 12 or less.

</details>

#### Scramble 41

```
R' U' F D2 R2 U R2 B2 D U2 F2 U L' R2 F' L2 U' R' B U' L2 R' U' R' U' F // scramble
```

Skips: none.

Each row is one route to a DR-xs on this scramble, shortest first; the last column is how far that DR-xs is from a real DR.

| # | Route | Length, moves | Kind | Starts from | Corner subset | Fewest turns to a real DR |
|---:|---|---:|---|---|---|---:|
| 1 | `(F R2 F2 R2 U2 R D')` | 7 | DR-1s | one-move slice EO: M slice on F/B, oriented | 2c4 | 6 |
| 2 | `(F L2 B2 R2 D2 R U')` | 7 | DR-1s | one-move slice EO: M slice on F/B, oriented | 2c4 | 5 |
| 3 | `(F R2 F2 R2 U2 R D)` | 7 | DR-1s | one-move slice EO: M slice on F/B, oriented | 2c4 | 6 |
| 4 | `(F L2 B2 R2 D2 R U)` | 7 | DR-1s | one-move slice EO: M slice on F/B, oriented | 2c4 | 5 |
| 5 | `(U' B' F2 U2 L' B' L' B)` | 8 | DR-1s | one-move slice EO: M slice on U/D, oriented | 2c3 | 5 |
| 6 | `(F' F2 R2 F2 R2 U2 R D')` | 8 | DR-1s | one-move slice EO: M slice on F/B, oriented | 2c4 | 6 |

Shown: 6 of the 26 DR-1s of 8 or less and 0 of the 0 DR-2s 8fe of 9 or less. Shortest normal DR: 9 moves.

<details>
<summary>Answers for scramble 41</summary>

Each row is the route with the same number above: the best finish of the method's form from it, then the whole solution written out for the scramble.

| # | Finish, moves | Solution | Solution length, moves |
|---:|---:|---|---:|
| 1 | 17 | `L F2 U2 R' U' D' F' R2 B2 L2 F' L2 D2 F U2 B' L2 D R' U2 R2 F2 R2 F'` | 24 |
| 2 | 16 | `L U2 B2 R2 U2 L' U2 L D2 L U D F' D2 B L2 U R' D2 R2 B2 L2 F'` | 23 |
| 3 | 16 | `U2 R B2 U2 L' U' D' L2 B2 R2 L2 B U2 F L2 U2 D' R' U2 R2 F2 R2 F'` | 23 |
| 4 | 16 | `B2 R2 U2 L U' D' F B2 D2 F R2 B' R2 F U2 B U' R' D2 R2 B2 L2 F'` | 23 |
| 5 | 15 | `F2 U2 L' D2 R L2 F' B' U2 F2 D B2 R2 F2 U2 B' L B L U2 F2 B U` | 23 |
| 6 | 17 | `L F2 U2 R' U' D' F' R2 B2 L2 F' L2 D2 F U2 B' L2 D R' U2 R2 F2 R2 F'` | 24 |

Best of these: **23**, longer than the best through a normal DR of 10 or less. Normal DRs on this scramble: 22 through one of 10 or less, 21 through 11 or less, 19 through 12 or less.

</details>

#### Scramble 42

```
R' U' F D2 U' B2 U R2 D' R2 B2 U' R' B2 D2 B2 F' U R2 D' R' B' L' U' R' U' F // scramble
```

Skips: normal: E slice on U/D, oriented; normal: E slice on R/L, oriented; normal: S slice on U/D, oriented; inverse: E slice on U/D, oriented; inverse: E slice on F/B, oriented; inverse: M slice on F/B, misoriented.

Each row is one route to a DR-xs on this scramble, shortest first; the last column is how far that DR-xs is from a real DR.

| # | Route | Length, moves | Kind | Starts from | Corner subset | Fewest turns to a real DR |
|---:|---|---:|---|---|---|---:|
| 1 | `R' D2 F2 U2 B2 D2 B' L'` | 8 | DR-1s | skip: S slice on U/D, oriented | 2c5 | 5 |
| 2 | `R' B2 D2 U2 B D2 F2 L'` | 8 | DR-1s | skip: S slice on U/D, oriented | 2c5 | 5 |
| 3 | `(L2 B L F B' D2 F' L')` | 8 | DR-1s | skip: E slice on U/D, oriented | 4b2 | 6 |
| 4 | `(F' D2 F' L' U2 R B R)` | 8 | DR-1s | skip: E slice on U/D, oriented | 4b2 | 6 |
| 5 | `(U2 B' R L2 U2 D2 F' L)` | 8 | DR-1s | skip: E slice on U/D, oriented | 4b2 | 5 |
| 6 | `(L2 B L F' B U2 F' R')` | 8 | DR-1s | skip: E slice on U/D, oriented | 4b2 | 5 |
| 7 | `R U' R U' B2 D2 F D2 L'` | 9 | DR-2s 8fe | EO on U/D | 4b4 | 4 |
| 8 | `R U' R U' B2 D2 F D2 L` | 9 | DR-2s 8fe | EO on U/D | 4b4 | 4 |

Shown: 6 of the 58 DR-1s of 8 or less and 2 of the 2 DR-2s 8fe of 9 or less. Shortest normal DR: 10 moves.

<details>
<summary>Answers for scramble 42</summary>

Each row is the route with the same number above: the best finish of the method's form from it, then the whole solution written out for the scramble.

| # | Finish, moves | Solution | Solution length, moves |
|---:|---:|---|---:|
| 1 | 15 | `R' D2 F2 U2 B2 D2 B' L' U' L2 U F2 R' L' F U2 F2 D2 L2 D2 B' L2 B'` | 23 |
| 2 | 17 | `R' B2 U2 D2 B D2 F2 L' D F2 D R L F2 D2 F D2 F' L2 F L2 B L2 U2 B` | 25 |
| 3 | 16 | `D' F2 D R' L B' U2 D2 L2 B' U2 R2 F2 R2 F2 L' F D2 F' B L' B' L2` | 23 |
| 4 | 16 | `B2 D' F2 D' R L B2 L2 F' L2 D2 F2 B2 D2 F U2 R' B' R' U2 L F D2 F` | 24 |
| 5 | 16 | `U F2 U' R2 D2 F2 D' B2 D R2 D R L' F U2 D2 L' F U2 D2 R' L2 B U2` | 24 |
| 6 | 16 | `D' B2 R2 L2 U R' L D2 R2 D2 F D2 B D2 R2 B2 R F U2 F B' L' B' L2` | 24 |
| 7 | 16 | `R U' R U' B2 D2 F D2 L' D2 B' R2 B R2 F D2 F' L2 U2 B' R' L F B L` | 25 |
| 8 | 16 | `R U' R U' B2 D2 F D2 R2 L F R L F B' L' B2 U2 R2 B2 U2 L F2 D2 L'` | 25 |

Best of these: **23**, longer than the best through a normal DR of 10 or less. Normal DRs on this scramble: 21 through one of 10 or less, 20 through 11 or less, 20 through 12 or less.

</details>

#### Scramble 43

```
R' U' F U B2 R2 F2 U' L2 D B2 U B2 R D2 F' L F' U2 F' D2 U F' U R' U' F // scramble
```

Skips: normal: E slice on U/D, misoriented; normal: E slice on R/L, misoriented.

Each row is one route to a DR-xs on this scramble, shortest first; the last column is how far that DR-xs is from a real DR.

| # | Route | Length, moves | Kind | Starts from | Corner subset | Fewest turns to a real DR |
|---:|---|---:|---|---|---|---:|
| 1 | `D2 B D' F R2 B U D` | 8 | DR-1s | skip: E slice on R/L, misoriented | 2c4 | 4 |
| 2 | `L2 B D B' U' D' F D'` | 8 | DR-1s | skip: E slice on R/L, misoriented | 2c3 | 5 |
| 3 | `B2 U2 F' U B U2 B' D` | 8 | DR-1s | skip: E slice on R/L, misoriented | 2c3 | 5 |
| 4 | `L2 D F' L2 U B F' D` | 8 | DR-1s | skip: E slice on R/L, misoriented | 4b4 | 5 |
| 5 | `D2 B D' B U2 F' U D'` | 8 | DR-1s | skip: E slice on R/L, misoriented | 2c4 | 4 |
| 6 | `D2 B D' F R2 B U' D'` | 8 | DR-1s | skip: E slice on R/L, misoriented | 2c4 | 4 |
| 7 | `L2 D' L2 F D B D' R2 B` | 9 | DR-2s 8fe | skip: E slice on R/L, misoriented | 2c4 | 4 |
| 8 | `F2 U B' D2 F L2 F' U' F` | 9 | DR-2s 8fe | skip: E slice on R/L, misoriented | 4b2 | 4 |

Shown: 6 of the 34 DR-1s of 8 or less and 2 of the 10 DR-2s 8fe of 9 or less. Shortest normal DR: 9 moves.

<details>
<summary>Answers for scramble 43</summary>

Each row is the route with the same number above: the best finish of the method's form from it, then the whole solution written out for the scramble.

| # | Finish, moves | Solution | Solution length, moves |
|---:|---:|---|---:|
| 1 | 17 | `D2 B D' F R2 B U' D F' B2 R L' U B2 U2 R2 D' B2 D' R2 D L2 B2 U` | 24 |
| 2 | 15 | `L2 B D B' U' D' F D' F D2 F R2 F D2 R2 D2 F R' L U' L2 U2 B2` | 23 |
| 3 | 14 | `B2 U2 F' U B U2 B' D F' U2 B2 D2 R2 L2 B R L' F2 D L2 D2 F2` | 22 |
| 4 | 17 | `L2 D F' L2 U F' B U2 D R2 F' R2 B' L2 F2 U2 F U2 R L' U' L2 U2 B2 L2` | 25 |
| 5 | 15 | `D2 B D' B U2 F' U D F R L' U2 R2 D F2 R2 U' L2 F2 D2 F2 D'` | 22 |
| 6 | 16 | `D2 B D' F R2 B U' D' B2 D2 F L2 B U2 L2 F R2 F' R' L D L2 F2 D'` | 24 |
| 7 | 14 | `L2 D' L2 F D B D' R2 B' R U D R L' D2 L2 U F2 R2 D' R2 U'` | 22 |
| 8 | 14 | `F2 U B' D2 F L2 F' U' F U D' R L F2 U L2 B2 U2 R2 D' R2 F2 B2` | 23 |

Best of these: **22**, longer than the best through a normal DR of 10 or less. Normal DRs on this scramble: 21 through one of 10 or less, 20 through 11 or less, 20 through 12 or less.

</details>

#### Scramble 44

```
R' U' F D' B2 U B2 D' F2 U2 B2 R' B2 R' B U F L' F' R2 B F' R' U' F // scramble
```

Skips: normal: S slice on U/D, misoriented; inverse: E slice on U/D, misoriented.

Each row is one route to a DR-xs on this scramble, shortest first; the last column is how far that DR-xs is from a real DR.

| # | Route | Length, moves | Kind | Starts from | Corner subset | Fewest turns to a real DR |
|---:|---|---:|---|---|---|---:|
| 1 | `F R2 B U2 L F' R F'` | 8 | DR-1s | skip: S slice on U/D, misoriented | 4b2 | 5 |
| 2 | `F U2 L2 F' R' B' L B` | 8 | DR-1s | skip: S slice on U/D, misoriented | 2c4 | 4 |
| 3 | `B2 L F2 U2 F' L' F B'` | 8 | DR-1s | skip: S slice on U/D, misoriented | 2c3 | 5 |
| 4 | `F2 U2 R2 B' R F' L F'` | 8 | DR-1s | skip: S slice on U/D, misoriented | 4b5 | 5 |
| 5 | `F U2 L2 F' R' B' L B'` | 8 | DR-1s | skip: S slice on U/D, misoriented | 2c4 | 5 |
| 6 | `B2 L B2 D2 F' R F' B'` | 8 | DR-1s | skip: S slice on U/D, misoriented | 2c3 | 5 |
| 7 | `(L D' F B' U D' F D' F')` | 9 | DR-2s 8fe | one-move slice EO: S slice on R/L, misoriented | 0c3 | 4 |
| 8 | `(L U F' B U D' F' U' B')` | 9 | DR-2s 8fe | one-move slice EO: S slice on R/L, misoriented | 0c3 | 4 |

Shown: 6 of the 54 DR-1s of 8 or less and 2 of the 6 DR-2s 8fe of 9 or less. Shortest normal DR: 10 moves.

<details>
<summary>Answers for scramble 44</summary>

Each row is the route with the same number above: the best finish of the method's form from it, then the whole solution written out for the scramble.

| # | Finish, moves | Solution | Solution length, moves |
|---:|---:|---|---:|
| 1 | 14 | `F R2 B U2 L F' R F' R2 D2 L2 D2 B2 R' L2 B2 U D F' U2 F' B'` | 22 |
| 2 | 15 | `F U2 L2 F' R' B' L F2 B R2 L U' D' B' D2 F R2 F D2 R2 D2 F2 D2` | 23 |
| 3 | 16 | `B2 L F2 U2 F' L' F' B' R' L2 F2 L U' D L2 B L2 B U2 R2 B2 R2 B'` | 23 |
| 4 | 16 | `F2 U2 R2 B' R F' L F' L2 F2 L U' D' F' R2 D2 F' U2 R2 B' D2 F2 R2 B'` | 24 |
| 5 | 16 | `F U2 L2 F' R' B' L F2 B R2 L U' D' B' D2 F R2 F D2 R2 D2 F2 D2` | 23 |
| 6 | 16 | `B2 L B2 D2 F' R F' B' L' U2 F2 D2 L' U' D' R2 B D2 B' U2 R2 D2 L2 B` | 24 |
| 7 | 15 | `B2 R' L F' B' L U2 B2 L2 B2 R F2 L2 U2 L' F D F' U' D F' B D L'` | 24 |
| 8 | 16 | `F2 R L F' B' R D2 F2 R2 F2 R B2 D2 L2 D2 L' B U F U' D F B' U' L'` | 25 |

Best of these: **22**, as short as the best through a normal DR of 10 or less. Normal DRs on this scramble: 22 through one of 10 or less, 21 through 11 or less, 20 through 12 or less.

</details>

#### Scramble 45

```
R' U' F U2 R2 F2 U' B2 D' R2 D' L2 U2 L' U B U B R U2 F' D' U F' R' U' F // scramble
```

Skips: none.

No DR-1s of 8 moves or less and no DR-2s 8fe of 9 or less here. The shortest normal DR is 10 moves; the best solution through a normal DR of 12 or less is 21.

#### Scramble 46

```
R' U' F U R L U R2 D2 B U R U2 L F B2 U' B2 D' F2 U' R2 F2 U' B2 R' U' F // scramble
```

Skips: normal: S slice on U/D, oriented; inverse: E slice on U/D, oriented.

Each row is one route to a DR-xs on this scramble, shortest first; the last column is how far that DR-xs is from a real DR.

| # | Route | Length, moves | Kind | Starts from | Corner subset | Fewest turns to a real DR |
|---:|---|---:|---|---|---|---:|
| 1 | `(U2 F2 B L' U2 L' F R')` | 8 | DR-1s | skip: E slice on U/D, oriented | 4b4 | 6 |
| 2 | `(F R' B L' F B2 R B)` | 8 | DR-1s | skip: E slice on U/D, oriented | 2c4 | 4 |
| 3 | `(U' F' D2 L F2 R2 F' R)` | 8 | DR-1s | one-move slice EO: M slice on U/D, misoriented | 2c4 | 6 |
| 4 | `F' R B2 U' B2 L' F2 U` | 8 | DR-1s | one-move slice EO: E slice on F/B, misoriented | 2c4 | 5 |
| 5 | `(U2 F2 B L' U2 L' F R)` | 8 | DR-1s | skip: E slice on U/D, oriented | 4b4 | 6 |
| 6 | `(R F' B2 D2 L U2 F' L')` | 8 | DR-1s | skip: E slice on U/D, oriented | 4b2 | 5 |
| 7 | `(B L R' D' U2 L2 F L)` | 8 | DR-2s 8fe | EO on U/D | 4b5 | 4 |
| 8 | `(B L R' D' U2 L2 F L')` | 8 | DR-2s 8fe | EO on U/D | 4b5 | 4 |

Shown: 6 of the 44 DR-1s of 8 or less and 2 of the 4 DR-2s 8fe of 9 or less. Shortest normal DR: 9 moves.

<details>
<summary>Answers for scramble 46</summary>

Each row is the route with the same number above: the best finish of the method's form from it, then the whole solution written out for the scramble.

| # | Finish, moves | Solution | Solution length, moves |
|---:|---:|---|---:|
| 1 | 17 | `D F2 R2 U' F2 L2 U2 R2 D R2 U' R L' B' R2 U2 F R F' L U2 L F2 B' U2` | 25 |
| 2 | 16 | `D B2 L2 B2 L2 D' L2 D' R2 U2 F2 U' F B R' L B' R' F' B2 L B' R F'` | 24 |
| 3 | 15 | `R D2 L D2 L B2 R' U D B R2 B U2 B2 D2 R' F R2 F2 L' D2 F U` | 23 |
| 4 | 16 | `F' R B2 U' B2 L' F2 U R2 U2 F2 U2 B2 L F B U B2 D' F2 D' L2 B2 U2` | 24 |
| 5 | 16 | `R2 D2 L2 F2 D R L F' R2 B2 L2 U2 B' U2 F' R' L2 F' L U2 L F2 B' U2` | 24 |
| 6 | 17 | `D2 B2 R2 U' R' L B2 D2 F R2 D2 R2 U2 B' D2 F D2 L F U2 L' D2 F B2 R'` | 25 |
| 7 | 16 | `L B2 R' U2 D2 L2 B2 L' B2 R B2 L F' B' R L2 F' L2 U2 D R L' B'` | 23 |
| 8 | 15 | `L' F B R L' F' U2 B R2 F' D2 F2 R2 B' D2 L F' L2 U2 D R L' B'` | 23 |

Best of these: **23**, longer than the best through a normal DR of 10 or less. Normal DRs on this scramble: 19 through one of 10 or less, 19 through 11 or less, 19 through 12 or less.

</details>

#### Scramble 47

```
R' U' F U B2 D R2 U2 R2 B2 R2 F2 D F' R D R2 D L2 B' D' F' B' D2 U' R' U' F // scramble
```

Skips: normal: S slice on R/L, misoriented; inverse: M slice on U/D, oriented; inverse: S slice on R/L, misoriented; inverse: S slice on F/B, misoriented.

Each row is one route to a DR-xs on this scramble, shortest first; the last column is how far that DR-xs is from a real DR.

| # | Route | Length, moves | Kind | Starts from | Corner subset | Fewest turns to a real DR |
|---:|---|---:|---|---|---|---:|
| 1 | `(U' D' F' U' D B)` | 6 | DR-1s | skip: S slice on R/L, misoriented | 2c4 | 5 |
| 2 | `(U D B' U' D F)` | 6 | DR-1s | skip: S slice on R/L, misoriented | 2c4 | 6 |
| 3 | `(U' D' F' U' D B')` | 6 | DR-1s | skip: S slice on R/L, misoriented | 2c4 | 5 |
| 4 | `(U D B' U' D F')` | 6 | DR-1s | skip: S slice on R/L, misoriented | 2c4 | 5 |
| 5 | `L B2 F' D L2 D2 F'` | 7 | DR-1s | one-move slice EO: E slice on R/L, oriented | 4b4 | 6 |
| 6 | `(D R2 D F' U D' B')` | 7 | DR-1s | skip: S slice on R/L, misoriented | 4a4 | 5 |
| 7 | `(B R' F' L' F' D2 F U)` | 8 | DR-2s 8fe | EO on R/L | 4b5 | 4 |
| 8 | `(B R' F' L' F' D2 F U')` | 8 | DR-2s 8fe | EO on R/L | 4b5 | 4 |

Shown: 6 of the 298 DR-1s of 8 or less and 2 of the 26 DR-2s 8fe of 9 or less. Shortest normal DR: 8 moves.

<details>
<summary>Answers for scramble 47</summary>

Each row is the route with the same number above: the best finish of the method's form from it, then the whole solution written out for the scramble.

| # | Finish, moves | Solution | Solution length, moves |
|---:|---:|---|---:|
| 1 | 15 | `R2 F' U2 F' R L B2 D' R2 L2 B2 U' R2 F2 L2 B' U D' F U D` | 21 |
| 2 | 16 | `R2 B U2 D2 B2 L2 F' R2 L2 U2 R' L' D' L2 B2 D F' U D' B U' D'` | 22 |
| 3 | 15 | `U2 F R2 F R' L B2 R2 D F2 D F2 L2 F2 L2 B U D' F U D` | 21 |
| 4 | 15 | `R2 F' U2 F' R' L D' L2 U' F2 D' R2 D' R2 L2 F U D' B U' D'` | 21 |
| 5 | 17 | `L F' B2 D L2 D2 F' L U2 R' F2 L D2 R2 B2 R' U2 F B D R2 B2 U F2` | 24 |
| 6 | 16 | `R2 L2 F2 B D2 B R2 B2 U2 F' R' L B2 D' L2 D2 B U' D F D' R2 D'` | 23 |
| 7 | 16 | `D R2 F B' U D' F L2 D2 F D2 B' U2 L2 F' L2 U' F' D2 F L F R B'` | 24 |
| 8 | 17 | `F2 L2 U R2 D' L2 F2 D' R2 F2 D' F2 U' F B' U2 D' F' D2 F L F R B'` | 24 |

Best of these: **21**, as short as the best through a normal DR of 11 or less. Normal DRs on this scramble: 21 through one of 10 or less, 21 through 11 or less, 20 through 12 or less.

</details>

#### Scramble 48

```
R' U' F U L2 B2 D B2 D F2 D2 B2 R2 F' R' B' D' U R U B2 U L2 F' U' R' U' F // scramble
```

Skips: normal: E slice on F/B, misoriented; normal: M slice on R/L, oriented; inverse: E slice on F/B, misoriented; inverse: M slice on R/L, oriented.

Each row is one route to a DR-xs on this scramble, shortest first; the last column is how far that DR-xs is from a real DR.

| # | Route | Length, moves | Kind | Starts from | Corner subset | Fewest turns to a real DR |
|---:|---|---:|---|---|---|---:|
| 1 | `(B D2 R2 D R2 F' U)` | 7 | DR-1s | skip: M slice on R/L, oriented | 2c5 | 6 |
| 2 | `(R' D2 R2 D R' L' D')` | 7 | DR-1s | skip: E slice on F/B, misoriented | 2c4 | 4 |
| 3 | `(R D' L2 B' D2 F2 D')` | 7 | DR-1s | one-move slice EO: S slice on R/L, oriented | 2c5 | 5 |
| 4 | `(R' D2 R2 D R' L' D)` | 7 | DR-1s | skip: E slice on F/B, misoriented | 2c4 | 4 |
| 5 | `(R D' L2 B U2 B2 D')` | 7 | DR-1s | one-move slice EO: S slice on R/L, oriented | 2c5 | 5 |
| 6 | `(F' U' F' R2 U2 F' U)` | 7 | DR-1s | skip: M slice on R/L, oriented | 2c4 | 5 |
| 7 | `(U2 L2 U' L U2 D2 L' U2 L)` | 9 | DR-2s 8fe | skip: E slice on F/B, misoriented | 2c5 | 4 |
| 8 | `F2 L2 U' F2 L2 U2 R F2 R` | 9 | DR-2s 8fe | skip: E slice on F/B, misoriented | 4b4 | 4 |

Shown: 6 of the 260 DR-1s of 8 or less and 2 of the 54 DR-2s 8fe of 9 or less. Shortest normal DR: 9 moves.

<details>
<summary>Answers for scramble 48</summary>

Each row is the route with the same number above: the best finish of the method's form from it, then the whole solution written out for the scramble.

| # | Finish, moves | Solution | Solution length, moves |
|---:|---:|---|---:|
| 1 | 17 | `D2 B2 U2 R' D2 R U2 F2 B2 L2 U' D B L2 F U2 F' U' F R2 D' R2 D2 B'` | 24 |
| 2 | 15 | `D' B2 U' R2 F2 U' L2 U' R2 D2 F B' D2 R' L D R L D' R2 D2 R` | 22 |
| 3 | 17 | `R2 F' U2 D2 R2 F' D2 F D2 F' U' D F2 R B2 L2 F2 D F2 D2 B L2 D R'` | 24 |
| 4 | 16 | `D' B2 U' R2 F2 U' L2 U' R2 D2 F B' D2 R' L D R L D' R2 D2 R` | 22 |
| 5 | 17 | `D2 L2 F R2 B' D2 F U D F2 L D2 F2 R' D2 L2 U2 D B2 U2 B' L2 D R'` | 24 |
| 6 | 16 | `R' F2 L' U2 L F2 B2 U2 F2 U' D F' R2 F' L2 B' U' F U2 R2 F U F` | 23 |
| 7 | 15 | `U R2 B2 D L2 U' F2 D F2 L2 F' B U' D' F L' U2 L U2 D2 L' U L2 U2` | 24 |
| 8 | 16 | `F2 L2 U' F2 L2 U2 R F2 R U2 F' U D' F' B' U R2 D2 F2 U' B2 U' R2 D2 L2` | 25 |

Best of these: **22**, longer than the best through a normal DR of 10 or less. Normal DRs on this scramble: 18 through one of 10 or less, 18 through 11 or less, 18 through 12 or less.

</details>

#### Scramble 49

```
R' U' F L' D' R L' U2 L2 F' U2 D' B L' U F2 D' B2 L2 F2 U2 R2 D2 R' U' F // scramble
```

Skips: normal: M slice on U/D, misoriented; inverse: S slice on F/B, oriented.

Each row is one route to a DR-xs on this scramble, shortest first; the last column is how far that DR-xs is from a real DR.

| # | Route | Length, moves | Kind | Starts from | Corner subset | Fewest turns to a real DR |
|---:|---|---:|---|---|---|---:|
| 1 | `(L2 B2 U2 R L' F2 R' U)` | 8 | DR-1s | skip: S slice on F/B, oriented | 2c4 | 5 |
| 2 | `F' L2 B2 R2 D2 R2 F R'` | 8 | DR-1s | skip: M slice on U/D, misoriented | 2c3 | 6 |
| 3 | `(R' F2 D2 U' R B2 D' L')` | 8 | DR-1s | skip: S slice on F/B, oriented | 4b3 | 6 |
| 4 | `(D' U R' L D2 R2 D' L)` | 8 | DR-1s | skip: S slice on F/B, oriented | 2c4 | 6 |
| 5 | `(D2 R2 F2 D2 R2 U2 L' D')` | 8 | DR-1s | skip: S slice on F/B, oriented | 2c4 | 5 |
| 6 | `F L2 B' F' R2 D2 F R` | 8 | DR-1s | skip: M slice on U/D, misoriented | 2c3 | 6 |
| 7 | `U2 B F2 D2 B U2 B' R` | 8 | DR-2s 8fe | skip: M slice on U/D, misoriented | 4a4 | 4 |
| 8 | `U2 B F2 D2 B U2 B' R'` | 8 | DR-2s 8fe | skip: M slice on U/D, misoriented | 4a4 | 4 |

Shown: 6 of the 124 DR-1s of 8 or less and 2 of the 48 DR-2s 8fe of 9 or less. Shortest normal DR: 9 moves.

<details>
<summary>Answers for scramble 49</summary>

Each row is the route with the same number above: the best finish of the method's form from it, then the whole solution written out for the scramble.

| # | Finish, moves | Solution | Solution length, moves |
|---:|---:|---|---:|
| 1 | 17 | `B U2 R2 B' D2 F' U2 B2 D2 L2 B' U D L' B2 R F2 U' R F2 R' L U2 B2 L2` | 25 |
| 2 | 15 | `F' L2 B2 R2 D2 R2 F R' B2 L2 D2 B' U' D R2 F2 L' B2 U2 R' U2 D2 R2` | 23 |
| 3 | 16 | `F U2 D2 B U2 R' L D B2 U2 L2 D' R2 U B2 L' D B2 R' U D2 F2 R` | 23 |
| 4 | 17 | `F' R2 F D2 B' D2 R2 L2 F D2 R' L' U' B2 D2 L2 D' L' D R2 D2 R L' U' D` | 25 |
| 5 | 16 | `B2 R2 B L2 U2 F R2 F' U2 F' R2 U' D' R' U2 L D L U2 R2 D2 F2 R2 D2` | 24 |
| 6 | 15 | `F L2 F' B' R2 D2 F R U2 L2 D2 L2 B2 R2 D2 F' U D' F2 L' U2 B2 R` | 23 |
| 7 | 16 | `U2 F2 B D2 B U2 B' R' D' B2 R2 U' F2 D2 L2 D' R2 U2 R' L' U D R` | 23 |
| 8 | 15 | `U2 F2 B D2 B U2 B' R' D' B2 R2 U' F2 D2 L2 D' R2 U2 R' L' U D R` | 23 |

Best of these: **23**, longer than the best through a normal DR of 10 or less. Normal DRs on this scramble: 20 through one of 10 or less, 20 through 11 or less, 20 through 12 or less.

</details>

#### Scramble 50

```
R' U' F L B' D' B2 R2 B2 R D R2 F' R F2 U' F2 U R2 B2 D' B2 R' U' F // scramble
```

Skips: normal: E slice on U/D, oriented; normal: M slice on R/L, misoriented; normal: M slice on F/B, misoriented; normal: S slice on U/D, misoriented; normal: S slice on R/L, oriented; normal: S slice on F/B, misoriented; inverse: E slice on U/D, misoriented; inverse: E slice on R/L, oriented; inverse: E slice on F/B, misoriented; inverse: M slice on F/B, misoriented; inverse: S slice on U/D, oriented; inverse: S slice on R/L, misoriented.

Each row is one route to a DR-xs on this scramble, shortest first; the last column is how far that DR-xs is from a real DR.

| # | Route | Length, moves | Kind | Starts from | Corner subset | Fewest turns to a real DR |
|---:|---|---:|---|---|---|---:|
| 1 | `(D2 R B R B' R L2 B)` | 8 | DR-1s | skip: S slice on U/D, oriented | 2c4 | 5 |
| 2 | `(D2 R B R B' R L2 B')` | 8 | DR-1s | skip: S slice on U/D, oriented | 2c4 | 6 |
| 3 | `(B' L' B' R' L2 F B' R)` | 8 | DR-1s | skip: S slice on U/D, oriented | 4b5 | 5 |
| 4 | `F' R2 U B' D L2 F' D` | 8 | DR-1s | skip: S slice on R/L, oriented | 2c4 | 5 |
| 5 | `(F R2 B R2 L' F' B L')` | 8 | DR-1s | skip: S slice on U/D, oriented | 2c4 | 6 |
| 6 | `(R' B U2 F R' F D2 F')` | 8 | DR-1s | skip: S slice on U/D, oriented | 4b2 | 6 |

Shown: 6 of the 16 DR-1s of 8 or less and 0 of the 0 DR-2s 8fe of 9 or less. Shortest normal DR: 10 moves.

<details>
<summary>Answers for scramble 50</summary>

Each row is the route with the same number above: the best finish of the method's form from it, then the whole solution written out for the scramble.

| # | Finish, moves | Solution | Solution length, moves |
|---:|---:|---|---:|
| 1 | 16 | `D2 F' B2 R2 U2 D2 F' U2 R' L D R2 U R2 F2 D2 B' R' L2 B R' B' R' D2` | 24 |
| 2 | 16 | `R2 L2 U2 B' R2 F U2 R' L U' R2 L2 B2 U F2 U2 B R' L2 B R' B' R' D2` | 24 |
| 3 | 17 | `B2 L2 U2 F D2 F L2 B' D2 B2 R L' U' L2 D F2 R' L2 F' B R L2 B L B` | 25 |
| 4 | 17 | `F' R2 U B' D L2 F' D R' B2 L' U D F' U2 F L2 B' R2 D2 F2 D2 F' D2 R2` | 25 |
| 5 | 17 | `D2 B' U2 L2 B L2 B' R2 U2 B' D2 R L' U B2 D L' F B' R2 L B' R2 F'` | 24 |
| 6 | 15 | `U2 F2 D2 R2 F R L' U F2 U F2 U2 F2 D' R2 F D2 F' R F' U2 B' R` | 23 |

Best of these: **23**, longer than the best through a normal DR of 10 or less. Normal DRs on this scramble: 22 through one of 10 or less, 21 through 11 or less, 21 through 12 or less.

</details>

#### Scramble 51

```
R' U' F U F2 L2 U R2 B2 F2 U' F2 U' R' B' U' B R D2 B L2 F' U' R' U' F // scramble
```

Skips: none.

Each row is one route to a DR-xs on this scramble, shortest first; the last column is how far that DR-xs is from a real DR.

| # | Route | Length, moves | Kind | Starts from | Corner subset | Fewest turns to a real DR |
|---:|---|---:|---|---|---|---:|
| 1 | `(F2 U' L' F' R' F2 L2 U' L)` | 9 | DR-2s 8fe | EO on F/B | 4a2 | 4 |
| 2 | `(F2 U' L' F' R' F2 L2 U' L')` | 9 | DR-2s 8fe | EO on F/B | 4a2 | 4 |

Shown: 0 of the 0 DR-1s of 8 or less and 2 of the 2 DR-2s 8fe of 9 or less. Shortest normal DR: 9 moves.

<details>
<summary>Answers for scramble 51</summary>

Each row is the route with the same number above: the best finish of the method's form from it, then the whole solution written out for the scramble.

| # | Finish, moves | Solution | Solution length, moves |
|---:|---:|---|---:|
| 1 | 14 | `R2 B2 D2 R L' U2 R' D2 L2 U' D R' L' U L' U L2 F2 R F L U F2` | 23 |
| 2 | 15 | `R2 B2 D2 R L' U2 R' D2 L2 U' D R' L' U L' U L2 F2 R F L U F2` | 23 |

Best of these: **23**, longer than the best through a normal DR of 10 or less. Normal DRs on this scramble: 21 through one of 10 or less, 20 through 11 or less, 20 through 12 or less.

</details>

#### Scramble 52

```
R' U' F R2 D' F2 R2 U2 B2 L2 U2 B2 F2 L F R F' R2 U' L2 F2 R' U2 B2 R' U' F // scramble
```

Skips: normal: M slice on F/B, oriented; normal: S slice on R/L, oriented; normal: S slice on F/B, oriented; inverse: M slice on R/L, oriented; inverse: M slice on F/B, oriented.

Each row is one route to a DR-xs on this scramble, shortest first; the last column is how far that DR-xs is from a real DR.

| # | Route | Length, moves | Kind | Starts from | Corner subset | Fewest turns to a real DR |
|---:|---|---:|---|---|---|---:|
| 1 | `B2 D2 R2 B' D' B` | 6 | DR-1s | skip: S slice on R/L, oriented | 4b2 | 4 |
| 2 | `B2 U2 L2 F' D' F` | 6 | DR-1s | skip: S slice on R/L, oriented | 4b2 | 5 |
| 3 | `B2 U2 L2 F' D' F'` | 6 | DR-1s | skip: S slice on R/L, oriented | 4b2 | 4 |
| 4 | `B2 D2 R2 B' D' B'` | 6 | DR-1s | skip: S slice on R/L, oriented | 4b2 | 5 |
| 5 | `F2 B2 U2 L2 F' D' F` | 7 | DR-1s | skip: S slice on R/L, oriented | 4a4 | 5 |
| 6 | `D2 F' U' B U F B` | 7 | DR-1s | skip: S slice on R/L, oriented | 4b3 | 6 |

Shown: 6 of the 673 DR-1s of 8 or less and 0 of the 0 DR-2s 8fe of 9 or less. Shortest normal DR: 8 moves.

<details>
<summary>Answers for scramble 52</summary>

Each row is the route with the same number above: the best finish of the method's form from it, then the whole solution written out for the scramble.

| # | Finish, moves | Solution | Solution length, moves |
|---:|---:|---|---:|
| 1 | 15 | `B2 D2 R2 B' D' B D2 L U D R2 U2 L2 F' R2 U2 B' R2 B2 L2 B` | 21 |
| 2 | 15 | `B2 U2 L2 F' D' F D2 F2 U2 D2 L D2 B2 L2 U' D' B' U2 B U2 B'` | 21 |
| 3 | 16 | `B2 U2 L2 F' D' F' U2 R2 L U D' B' U2 F2 D2 F' R2 F R2 B D2 B'` | 22 |
| 4 | 16 | `B2 D2 R2 B' D' B D2 L U D R2 U2 L2 F' R2 U2 B' R2 B2 L2 B` | 21 |
| 5 | 17 | `F2 B2 U2 L2 F' D' F B2 D2 R U' D L2 U2 F' D2 F2 U2 R2 B' L2 B' D2 R2` | 24 |
| 6 | 16 | `D2 F' U' B U F B L' B2 R F2 R2 F2 D2 R F2 U D B R2 L2 B' L2` | 23 |

Best of these: **21**, longer than the best through a normal DR of 10 or less. Normal DRs on this scramble: 20 through one of 10 or less, 19 through 11 or less, 19 through 12 or less.

</details>

#### Scramble 53

```
R' U' F U L2 U B2 R2 U F2 L2 U R' B2 D' U L' F' R2 F' D' B2 F R' U' F // scramble
```

Skips: none.

Each row is one route to a DR-xs on this scramble, shortest first; the last column is how far that DR-xs is from a real DR.

| # | Route | Length, moves | Kind | Starts from | Corner subset | Fewest turns to a real DR |
|---:|---|---:|---|---|---|---:|
| 1 | `(R' B' U' F U' R2 F2 D)` | 8 | DR-1s | one-move slice EO: E slice on R/L, misoriented | 0c4 | 5 |
| 2 | `(L' D' B' U F' U2 L2 F')` | 8 | DR-1s | one-move slice EO: E slice on R/L, oriented | 0c4 | 6 |
| 3 | `R D' L2 R2 F2 R2 D' B` | 8 | DR-1s | one-move slice EO: M slice on R/L, oriented | 4b2 | 5 |
| 4 | `R D' F2 L2 D' L2 R2 B` | 8 | DR-1s | one-move slice EO: M slice on R/L, oriented | 4b2 | 6 |
| 5 | `(L' D' B' U B' L2 D2 F')` | 8 | DR-1s | one-move slice EO: E slice on R/L, oriented | 0c4 | 4 |
| 6 | `R D' L2 R2 F2 R2 D' B'` | 8 | DR-1s | one-move slice EO: M slice on R/L, oriented | 4b2 | 6 |
| 7 | `(R D F2 U' F' U2 D B' D)` | 9 | DR-2s 8fe | one-move slice EO: E slice on R/L, misoriented | 2c3 | 4 |
| 8 | `(R D F2 U' F' U2 D B' D')` | 9 | DR-2s 8fe | one-move slice EO: E slice on R/L, misoriented | 2c3 | 4 |

Shown: 6 of the 36 DR-1s of 8 or less and 2 of the 2 DR-2s 8fe of 9 or less. Shortest normal DR: 9 moves.

<details>
<summary>Answers for scramble 53</summary>

Each row is the route with the same number above: the best finish of the method's form from it, then the whole solution written out for the scramble.

| # | Finish, moves | Solution | Solution length, moves |
|---:|---:|---|---:|
| 1 | 16 | `U' R2 D' L2 D2 B2 D' R L F' R2 B2 R2 U2 R2 D F2 R2 U F' U B R` | 23 |
| 2 | 15 | `D' R2 U F2 D F' B' L' D2 F2 B2 R' D2 R' F B2 L2 U2 F U' B D L` | 23 |
| 3 | 16 | `R D' R2 L2 F2 R2 D' B L2 D2 L2 U' F B' U2 R U2 L U2 L' B2 D2 F2 D2` | 24 |
| 4 | 16 | `R D' F2 L2 D' R2 L2 B' R2 D2 L2 U F' B D2 R D2 F2 L2 D2 R' U2 L'` | 23 |
| 5 | 15 | `D' F2 U' R2 D F B R2 U2 F2 R B2 L' F2 R F D2 L2 B U' B D L` | 23 |
| 6 | 16 | `R D' R2 L2 F2 R2 D' B' U' L2 F2 D F' B R2 D2 R B2 U2 F2 U2 L2 U2 R` | 24 |
| 7 | 15 | `R2 B2 U B2 L2 U R2 B2 D' F2 D2 F2 R' L' U B U2 D' F U F2 D' R'` | 23 |
| 8 | 15 | `R2 B2 U B2 L2 U R2 B2 D' F2 D2 F2 R' L' U B U2 D' F U F2 D' R'` | 23 |

Best of these: **23**, longer than the best through a normal DR of 10 or less. Normal DRs on this scramble: 18 through one of 10 or less, 18 through 11 or less, 18 through 12 or less.

</details>

#### Scramble 54

```
R' U' F U' L2 U2 F2 U' L2 R2 U B2 U R D' L' R B L U2 L2 F U L2 U' R' U' F // scramble
```

Skips: normal: E slice on R/L, oriented.

Each row is one route to a DR-xs on this scramble, shortest first; the last column is how far that DR-xs is from a real DR.

| # | Route | Length, moves | Kind | Starts from | Corner subset | Fewest turns to a real DR |
|---:|---|---:|---|---|---|---:|
| 1 | `R2 D R2 B' D' F' L2 U` | 8 | DR-1s | skip: E slice on R/L, oriented | 4b2 | 4 |
| 2 | `R2 D R2 B D' F' L2 U` | 8 | DR-1s | skip: E slice on R/L, oriented | 4a4 | 4 |
| 3 | `(U' F R2 B' L2 B2 L F')` | 8 | DR-1s | one-move slice EO: M slice on U/D, oriented | 2c4 | 5 |
| 4 | `R2 D R2 B' D' F' L2 U'` | 8 | DR-1s | skip: E slice on R/L, oriented | 4b2 | 5 |
| 5 | `(U' F R2 B' L2 B2 L F)` | 8 | DR-1s | one-move slice EO: M slice on U/D, oriented | 2c4 | 5 |
| 6 | `R2 D R2 B D' F' L2 U'` | 8 | DR-1s | skip: E slice on R/L, oriented | 4a4 | 5 |

Shown: 6 of the 6 DR-1s of 8 or less and 0 of the 0 DR-2s 8fe of 9 or less. Shortest normal DR: 9 moves.

<details>
<summary>Answers for scramble 54</summary>

Each row is the route with the same number above: the best finish of the method's form from it, then the whole solution written out for the scramble.

| # | Finish, moves | Solution | Solution length, moves |
|---:|---:|---|---:|
| 1 | 15 | `R2 D R2 B' D' F' L2 U D2 B2 U2 L F' B U2 F2 U B2 L2 B2 R2 U2 L2` | 23 |
| 2 | 16 | `R2 D R2 B D' F' L2 U F2 R' D2 F B U' L2 D' B2 L2 U' L2 U L2 D' R2` | 24 |
| 3 | 16 | `L2 D2 L' B2 D2 L F2 U2 R' D2 R2 F' B' D' B2 D2 F L' B2 L2 B R2 F' U` | 24 |
| 4 | 16 | `R2 D R2 B' D' F' L2 U' F2 U2 R' F' B' U R2 F2 D2 B2 D R2 F2 R2 D F2` | 24 |
| 5 | 17 | `L2 B2 U2 L B2 U2 L' U2 L D2 L2 D2 F B D F2 U2 F' L' B2 L2 B R2 F' U` | 25 |
| 6 | 16 | `R2 D R2 B D' F' L2 U' L' U2 R' D2 B2 R2 D2 F2 R' U2 F' B D2 F2 U R2` | 24 |

Best of these: **23**, longer than the best through a normal DR of 10 or less. Normal DRs on this scramble: 20 through one of 10 or less, 18 through 11 or less, 18 through 12 or less.

</details>

#### Scramble 55

```
R' U' F D' F2 U2 L2 D F2 U F2 B2 U F B2 D B U F R U2 F D' R' U2 R' U' F // scramble
```

Skips: normal: E slice on U/D, misoriented; normal: S slice on F/B, oriented; inverse: E slice on R/L, misoriented; inverse: M slice on F/B, oriented.

No DR-1s of 8 moves or less and no DR-2s 8fe of 9 or less here. The shortest normal DR is 9 moves; the best solution through a normal DR of 12 or less is 20.

#### Scramble 56

```
R' U' F L2 R2 B2 D2 U' L2 U F2 U L2 F' L U' B D' R B F L' R' B' U R' U' F // scramble
```

Skips: normal: E slice on R/L, misoriented; inverse: S slice on U/D, oriented; inverse: S slice on R/L, misoriented.

Each row is one route to a DR-xs on this scramble, shortest first; the last column is how far that DR-xs is from a real DR.

| # | Route | Length, moves | Kind | Starts from | Corner subset | Fewest turns to a real DR |
|---:|---|---:|---|---|---|---:|
| 1 | `(U D F2 B' U' D B')` | 7 | DR-1s | skip: S slice on R/L, misoriented | 2c5 | 5 |
| 2 | `(U D F2 B' U' D B)` | 7 | DR-1s | skip: S slice on R/L, misoriented | 2c5 | 5 |
| 3 | `(U2 L2 F R2 D F D' F)` | 8 | DR-1s | skip: S slice on R/L, misoriented | 2c4 | 5 |
| 4 | `(U2 L2 F R2 D F D' F')` | 8 | DR-1s | skip: S slice on R/L, misoriented | 2c4 | 5 |
| 5 | `R2 U F' D R2 U2 F' D` | 8 | DR-1s | skip: E slice on R/L, misoriented | 4a2 | 5 |
| 6 | `(U D F2 B' U' D F2 B)` | 8 | DR-1s | skip: S slice on R/L, misoriented | 2c5 | 6 |
| 7 | `F' R' D2 L2 U' D L' D'` | 8 | DR-2s 8fe | one-move slice EO: M slice on F/B, misoriented | 2c3 | 4 |
| 8 | `F' R' D2 L2 U' D L' D` | 8 | DR-2s 8fe | one-move slice EO: M slice on F/B, misoriented | 2c3 | 4 |

Shown: 6 of the 28 DR-1s of 8 or less and 2 of the 16 DR-2s 8fe of 9 or less. Shortest normal DR: 9 moves.

<details>
<summary>Answers for scramble 56</summary>

Each row is the route with the same number above: the best finish of the method's form from it, then the whole solution written out for the scramble.

| # | Finish, moves | Solution | Solution length, moves |
|---:|---:|---|---:|
| 1 | 17 | `U2 B' R' L' U L2 U2 B2 D R2 D' F2 D L2 D F2 D B U D' F2 B U' D'` | 24 |
| 2 | 16 | `B D2 F' L2 F D2 R L' D' L2 D B2 U F2 U L2 B' U D' F2 B U' D'` | 23 |
| 3 | 16 | `F' D2 F2 D2 R2 F' D2 B D2 B D2 R L' U' B2 D F' D F' D' R2 F' L2 U2` | 24 |
| 4 | 15 | `B2 L2 F' R2 F2 U2 R2 F R' L' U L2 D' B2 L2 F D F' D' R2 F' L2 U2` | 23 |
| 5 | 14 | `R2 U F' D R2 U2 F' U2 D' F2 B R' L D' F2 U' F2 R2 D2 L2 U` | 21 |
| 6 | 17 | `U2 D2 F L2 D2 F L2 B D2 F2 R L D' F2 D B2 R2 F2 B' U D' F2 B U' D'` | 25 |
| 7 | 14 | `F' R' D2 L2 U' D L' D' F U2 R L F' B' R2 B2 L' U2 L B2 D2 R2` | 22 |
| 8 | 15 | `F' R' D2 L2 U' D L' D B2 U2 B U2 D2 L2 F' R2 D2 B' D2 R' L' F B'` | 23 |

Best of these: **21**, longer than the best through a normal DR of 10 or less. Normal DRs on this scramble: 20 through one of 10 or less, 20 through 11 or less, 19 through 12 or less.

</details>

#### Scramble 57

```
R' U' F L2 U' F2 B2 U2 F2 R2 D R2 U2 F' U2 R' F' U2 B D B2 L' U2 R2 U' R' U' F // scramble
```

Skips: normal: M slice on R/L, oriented; normal: S slice on U/D, misoriented; inverse: E slice on R/L, oriented; inverse: E slice on F/B, misoriented; inverse: S slice on U/D, misoriented.

Each row is one route to a DR-xs on this scramble, shortest first; the last column is how far that DR-xs is from a real DR.

| # | Route | Length, moves | Kind | Starts from | Corner subset | Fewest turns to a real DR |
|---:|---|---:|---|---|---|---:|
| 1 | `L R2 F2 U' F L2 B` | 7 | DR-1s | one-move slice EO: S slice on R/L, oriented | 4a3 | 5 |
| 2 | `L R2 F2 U' B D2 F'` | 7 | DR-1s | one-move slice EO: S slice on R/L, oriented | 4a3 | 6 |
| 3 | `L R2 B2 D' B U2 F'` | 7 | DR-1s | one-move slice EO: S slice on R/L, oriented | 4a3 | 4 |
| 4 | `L R2 F2 U' B D2 F` | 7 | DR-1s | one-move slice EO: S slice on R/L, oriented | 4a3 | 6 |
| 5 | `L R2 B2 D' F R2 B` | 7 | DR-1s | one-move slice EO: S slice on R/L, oriented | 4a3 | 5 |
| 6 | `L R2 F2 U' F L2 B'` | 7 | DR-1s | one-move slice EO: S slice on R/L, oriented | 4a3 | 5 |
| 7 | `R2 B' U2 B U2 L F' L' F'` | 9 | DR-2s 8fe | skip: S slice on U/D, misoriented | 2c5 | 4 |
| 8 | `(F' R B2 U2 F U2 F' R' F')` | 9 | DR-2s 8fe | skip: S slice on U/D, misoriented | 4b3 | 4 |

Shown: 6 of the 118 DR-1s of 8 or less and 2 of the 4 DR-2s 8fe of 9 or less. Shortest normal DR: 9 moves.

<details>
<summary>Answers for scramble 57</summary>

Each row is the route with the same number above: the best finish of the method's form from it, then the whole solution written out for the scramble.

| # | Finish, moves | Solution | Solution length, moves |
|---:|---:|---|---:|
| 1 | 16 | `R2 L F2 U' F L2 B L2 F2 L' U' D' F' U2 F L2 B R2 D2 B R2 L2 F2` | 23 |
| 2 | 17 | `R2 L F2 U' B D2 F' L2 B2 L U2 L' U2 D2 R L2 B2 L' F2 U' D' B' L2 U2` | 24 |
| 3 | 16 | `R2 L B2 D' B U2 F R' B2 U' D' F' U2 B' L2 D2 B2 L2 U2 B' R2 F'` | 22 |
| 4 | 17 | `R2 L F2 U' B D2 F D2 F2 L2 D2 R' B2 U2 D2 L2 D2 R B2 U D' B' L2 U2` | 24 |
| 5 | 16 | `R2 L B2 D' F R2 B R2 U2 R F2 U D' B2 U2 B D2 B R2 B2 R2 U2 L2` | 23 |
| 6 | 17 | `R2 L F2 U' F L2 F2 B' R2 B2 L U D F U2 R2 F' L2 U2 B2 L2 B R2 B'` | 24 |
| 7 | 17 | `R2 B' U2 B U2 L F' L' F' U2 R2 U F2 U R2 D' R2 U B2 D' F' B' U D' F2 L2` | 26 |
| 8 | 15 | `B U2 F2 R2 F' D2 L2 F D2 F2 U D F' B R2 F R F U2 F' U2 B2 R' F` | 24 |

Best of these: **22**, longer than the best through a normal DR of 10 or less. Normal DRs on this scramble: 19 through one of 10 or less, 19 through 11 or less, 19 through 12 or less.

</details>

#### Scramble 58

```
R' U' F D2 L2 D B2 U' F2 R2 U' B2 U R' D' L F' U2 F U R2 B' R F2 R' U' F // scramble
```

Skips: normal: E slice on U/D, misoriented; normal: M slice on U/D, oriented; inverse: M slice on F/B, oriented.

Each row is one route to a DR-xs on this scramble, shortest first; the last column is how far that DR-xs is from a real DR.

| # | Route | Length, moves | Kind | Starts from | Corner subset | Fewest turns to a real DR |
|---:|---|---:|---|---|---|---:|
| 1 | `(D' R B L' B' R' F')` | 7 | DR-1s | one-move slice EO: S slice on U/D, misoriented | 2c5 | 6 |
| 2 | `(D L F' R' B2 R' B')` | 7 | DR-1s | one-move slice EO: S slice on U/D, misoriented | 4b4 | 6 |
| 3 | `(D L F' R' B2 R' B)` | 7 | DR-1s | one-move slice EO: S slice on U/D, misoriented | 4b4 | 6 |
| 4 | `(D' R B L' B' R' F)` | 7 | DR-1s | one-move slice EO: S slice on U/D, misoriented | 2c5 | 6 |
| 5 | `(D L F' B2 R' B2 R' B')` | 8 | DR-1s | one-move slice EO: S slice on U/D, misoriented | 4b2 | 6 |
| 6 | `(U L2 R2 F2 D' R2 D' L)` | 8 | DR-1s | skip: M slice on F/B, oriented | 2c4 | 5 |
| 7 | `(L' F' D R' B2 D' F)` | 7 | DR-2s 8fe | EO on R/L | 4a4 | 4 |
| 8 | `(L' F' D R' B2 D' F')` | 7 | DR-2s 8fe | EO on R/L | 4a4 | 4 |

Shown: 6 of the 24 DR-1s of 8 or less and 2 of the 54 DR-2s 8fe of 9 or less. Shortest normal DR: 9 moves.

<details>
<summary>Answers for scramble 58</summary>

Each row is the route with the same number above: the best finish of the method's form from it, then the whole solution written out for the scramble.

| # | Finish, moves | Solution | Solution length, moves |
|---:|---:|---|---:|
| 1 | 17 | `U2 B' L2 B U' D B2 R' D2 R2 D2 F2 L' D2 F2 R F B2 R B L B' R' D` | 24 |
| 2 | 16 | `R2 F' D2 F' U' D B2 R2 U2 R U2 R' B2 L2 D2 B' R B2 R F L' D'` | 22 |
| 3 | 15 | `R2 F' D2 F' U' D B2 R2 U2 R U2 R' B2 L2 D2 B' R B2 R F L' D'` | 22 |
| 4 | 17 | `U2 F' D2 F U D' F2 L' U2 L2 D2 F2 R2 L F2 D2 R F' R B L B' R' D` | 24 |
| 5 | 15 | `L2 F2 L2 U2 F B2 U2 F U' D' F2 L' F2 L D2 B R B2 R F B2 L' D'` | 23 |
| 6 | 16 | `R2 F2 L D2 L' U2 D2 R' F2 L' F2 U' D B D2 F L' D R2 D F2 R2 L2 U'` | 24 |
| 7 | 17 | `R2 F' D2 B' U2 B R2 U2 F R2 F' U2 F U' D B' D B2 R D' F L` | 22 |
| 8 | 17 | `R2 F' D2 B' U2 B R2 U2 F R2 F' U2 F U' D B' D B2 R D' F L` | 22 |

Best of these: **22**, as short as the best through a normal DR of 10 or less. Normal DRs on this scramble: 22 through one of 10 or less, 21 through 11 or less, 20 through 12 or less.

</details>

#### Scramble 59

```
R' U' F L D' F' R B L U F' R2 F2 R D' L2 U L2 D2 R2 L2 U R' U' F // scramble
```

Skips: normal: E slice on U/D, misoriented; normal: E slice on F/B, misoriented; inverse: E slice on U/D, misoriented; inverse: E slice on R/L, misoriented.

Each row is one route to a DR-xs on this scramble, shortest first; the last column is how far that DR-xs is from a real DR.

| # | Route | Length, moves | Kind | Starts from | Corner subset | Fewest turns to a real DR |
|---:|---|---:|---|---|---|---:|
| 1 | `(F' U' F2 U' B2 L2 R' U)` | 8 | DR-1s | one-move slice EO: M slice on F/B, oriented | 4a1 | 6 |
| 2 | `(F' D' L2 D' F2 L' R2 U)` | 8 | DR-1s | one-move slice EO: M slice on F/B, oriented | 4a1 | 6 |
| 3 | `(F' U' F2 U' B2 L2 R' U')` | 8 | DR-1s | one-move slice EO: M slice on F/B, oriented | 4a1 | 6 |
| 4 | `(F' D' L2 D' F2 L' R2 U')` | 8 | DR-1s | one-move slice EO: M slice on F/B, oriented | 4a1 | 6 |

Shown: 4 of the 4 DR-1s of 8 or less and 0 of the 0 DR-2s 8fe of 9 or less. Shortest normal DR: 10 moves.

<details>
<summary>Answers for scramble 59</summary>

Each row is the route with the same number above: the best finish of the method's form from it, then the whole solution written out for the scramble.

| # | Finish, moves | Solution | Solution length, moves |
|---:|---:|---|---:|
| 1 | 16 | `F2 R' D2 L' U' D F D2 L2 B2 U2 F B2 U2 D2 F' U' R L2 B2 U F2 U F` | 24 |
| 2 | 15 | `D2 R U2 D2 L' F2 R L U' D B L2 D2 F2 U R2 L F2 D L2 D F` | 22 |
| 3 | 15 | `U2 F2 L' F2 R' F2 D2 F2 L2 U D' F U2 L2 F2 U R L2 B2 U F2 U F` | 23 |
| 4 | 14 | `D2 R U2 D2 L' F2 R L U' D B L2 D2 F2 U R2 L F2 D L2 D F` | 22 |

Best of these: **22**, shorter than every normal DR of 10 or less gives. Normal DRs on this scramble: 23 through one of 10 or less, 19 through 11 or less, 19 through 12 or less.

</details>

#### Scramble 60

```
R' U' F L2 B2 L2 B2 U2 R2 D F2 D' U2 R U2 B2 D' R' U2 B D' U' F R' U' F // scramble
```

Skips: none.

Each row is one route to a DR-xs on this scramble, shortest first; the last column is how far that DR-xs is from a real DR.

| # | Route | Length, moves | Kind | Starts from | Corner subset | Fewest turns to a real DR |
|---:|---|---:|---|---|---|---:|
| 1 | `(D' U2 B2 L B2 U2 B R')` | 8 | DR-1s | one-move slice EO: M slice on U/D, oriented | 2c3 | 5 |
| 2 | `(D' U2 B2 L F2 D2 B L')` | 8 | DR-1s | one-move slice EO: M slice on U/D, oriented | 2c3 | 5 |
| 3 | `(D' U2 B2 L B2 U2 B R)` | 8 | DR-1s | one-move slice EO: M slice on U/D, oriented | 2c3 | 5 |
| 4 | `(D' U2 B2 L F2 D2 B L)` | 8 | DR-1s | one-move slice EO: M slice on U/D, oriented | 2c3 | 5 |
| 5 | `F2 U B' L R2 B2 D2 B' U'` | 9 | DR-2s 8fe | EO on R/L | 2c4 | 4 |
| 6 | `F2 U B' L R2 B2 D2 B' U` | 9 | DR-2s 8fe | EO on R/L | 2c4 | 4 |

Shown: 4 of the 4 DR-1s of 8 or less and 2 of the 2 DR-2s 8fe of 9 or less. Shortest normal DR: 8 moves.

<details>
<summary>Answers for scramble 60</summary>

Each row is the route with the same number above: the best finish of the method's form from it, then the whole solution written out for the scramble.

| # | Finish, moves | Solution | Solution length, moves |
|---:|---:|---|---:|
| 1 | 15 | `R2 U2 L F B' U R2 F2 D R2 D F2 U F2 R L2 B' U2 B2 L' B2 U2 D` | 23 |
| 2 | 16 | `D2 R' F2 R2 F2 D2 L' D2 L D2 R F B U R2 U2 L B' D2 F2 L' B2 U2 D` | 24 |
| 3 | 15 | `R2 D2 L U2 D2 L D2 F B L2 D' R2 U' L2 U' R' B' U2 B2 L' B2 U2 D` | 23 |
| 4 | 16 | `D2 L2 U2 R B2 R U2 F2 L F2 L F' B U' L2 D2 L' B' D2 F2 L' B2 U2 D` | 24 |
| 5 | 16 | `F2 U B' R2 L B2 D2 B' D F' B' L2 U' B2 L2 U' L2 F2 U' L2 F2 U' D2 B2` | 24 |
| 6 | 16 | `F2 U B' R2 L B2 D2 B' D F' B' L2 U' B2 L2 U' L2 F2 U' L2 F2 U' D2 B2` | 24 |

Best of these: **23**, longer than the best through a normal DR of 10 or less. Normal DRs on this scramble: 21 through one of 10 or less, 21 through 11 or less, 20 through 12 or less.

</details>

#### Scramble 61

```
R' U' F L2 B2 D' F' R2 U D' L' D2 F L2 D2 B2 D R2 U B2 D L2 D2 R' U' F // scramble
```

Skips: normal: S slice on F/B, oriented; inverse: E slice on U/D, oriented; inverse: S slice on F/B, oriented.

Each row is one route to a DR-xs on this scramble, shortest first; the last column is how far that DR-xs is from a real DR.

| # | Route | Length, moves | Kind | Starts from | Corner subset | Fewest turns to a real DR |
|---:|---|---:|---|---|---|---:|
| 1 | `(D2 U2 L D2 U R)` | 6 | DR-1s | skip: S slice on F/B, oriented | 4b2 | 5 |
| 2 | `(D2 U2 L D2 U R')` | 6 | DR-1s | skip: S slice on F/B, oriented | 4b2 | 6 |
| 3 | `(B2 D2 U2 L D2 U R')` | 7 | DR-1s | skip: S slice on F/B, oriented | 2c4 | 6 |
| 4 | `(U' L2 B2 R' D U2 L)` | 7 | DR-1s | skip: S slice on F/B, oriented | 4b5 | 5 |
| 5 | `(U' L2 B2 R' D U2 L')` | 7 | DR-1s | skip: S slice on F/B, oriented | 4b5 | 6 |
| 6 | `(R2 F2 D R D U2 L)` | 7 | DR-1s | skip: S slice on F/B, oriented | 2c3 | 5 |
| 7 | `U2 F' L U' B2 R B2 D R'` | 9 | DR-2s 8fe | EO on F/B | 2c3 | 4 |
| 8 | `U2 F' L U' B2 R B2 D R` | 9 | DR-2s 8fe | EO on F/B | 2c3 | 4 |

Shown: 6 of the 108 DR-1s of 8 or less and 2 of the 6 DR-2s 8fe of 9 or less. Shortest normal DR: 9 moves.

<details>
<summary>Answers for scramble 61</summary>

Each row is the route with the same number above: the best finish of the method's form from it, then the whole solution written out for the scramble.

| # | Finish, moves | Solution | Solution length, moves |
|---:|---:|---|---:|
| 1 | 15 | `B2 L2 U2 B R2 D2 B L2 F2 U2 R L D' B2 U R' U' D2 L' U2 D2` | 21 |
| 2 | 16 | `B2 L2 U2 B R2 D2 B L2 F2 U2 R L D' B2 U R' U' D2 L' U2 D2` | 21 |
| 3 | 17 | `U2 F R L D F2 U' R2 U B2 U' B2 L2 D2 R2 D R L2 U' D2 L' U2 D2 B2` | 24 |
| 4 | 16 | `F' U2 L2 F' L2 F R' L U L2 U L2 F2 U' B2 U L' U2 D' R B2 L2 U` | 23 |
| 5 | 16 | `U2 F' R L U L2 U' R2 U' L2 U' D' R2 D F2 B2 L U2 D' R B2 L2 U` | 23 |
| 6 | 16 | `B2 D2 F' L2 B' R2 U2 F D2 F R L' D' F2 U2 B2 L' U2 D' R' D' F2 R2` | 23 |
| 7 | 14 | `U2 F' L U' B2 R B2 D R' F2 D F2 U' L2 U2 D' R L' U D R F2 L'` | 23 |
| 8 | 13 | `U2 F' L U' B2 R B2 D R F2 U F2 U' L2 U' R L U' D R2 D2 B2` | 22 |

Best of these: **21**, longer than the best through a normal DR of 10 or less. Normal DRs on this scramble: 18 through one of 10 or less, 18 through 11 or less, 18 through 12 or less.

</details>

#### Scramble 62

```
R' U' F U' R2 U2 R2 U' L2 U' F2 R2 U' B' U F R2 F2 U R2 D R' F2 L' U' R' U' F // scramble
```

Skips: none.

Each row is one route to a DR-xs on this scramble, shortest first; the last column is how far that DR-xs is from a real DR.

| # | Route | Length, moves | Kind | Starts from | Corner subset | Fewest turns to a real DR |
|---:|---|---:|---|---|---|---:|
| 1 | `R' L2 F2 U' B U' R2 D` | 8 | DR-1s | one-move slice EO: E slice on R/L, misoriented | 2c5 | 6 |
| 2 | `R' L2 F2 U' B U' R2 D'` | 8 | DR-1s | one-move slice EO: E slice on R/L, misoriented | 2c5 | 6 |
| 3 | `R' L2 F2 U' B D' F2 U` | 8 | DR-1s | one-move slice EO: E slice on R/L, misoriented | 2c5 | 5 |
| 4 | `R' L2 F2 U' B D' F2 U'` | 8 | DR-1s | one-move slice EO: E slice on R/L, misoriented | 2c5 | 6 |

Shown: 4 of the 4 DR-1s of 8 or less and 0 of the 0 DR-2s 8fe of 9 or less. Shortest normal DR: 10 moves.

<details>
<summary>Answers for scramble 62</summary>

Each row is the route with the same number above: the best finish of the method's form from it, then the whole solution written out for the scramble.

| # | Finish, moves | Solution | Solution length, moves |
|---:|---:|---|---:|
| 1 | 17 | `R' L2 F2 U' B U' R2 U2 D R2 B D2 F U2 F2 R2 B U2 B2 R L U' F2 D' B2` | 25 |
| 2 | 17 | `R' L2 F2 U' B U' R2 U2 D' F U2 B' R L U L2 B2 U' R2 U2 B2 R2 U' L2 F2` | 25 |
| 3 | 17 | `R' L2 F2 U' B D' F2 U F' U2 B R' L' D B2 D2 L2 B2 U2 R2 F2 D' B2 D L2` | 25 |
| 4 | 16 | `R' L2 F2 U' B D' F2 U' F' U2 B2 D2 B R2 F R L D' R2 D2 F2 L2 F2 U` | 24 |

Best of these: **24**, longer than the best through a normal DR of 10 or less. Normal DRs on this scramble: 22 through one of 10 or less, 22 through 11 or less, 21 through 12 or less.

</details>

#### Scramble 63

```
R' U' F D2 B U2 D2 F L2 D2 F R2 F L' F' D L U L' B2 F U' R' U2 F' R' U' F // scramble
```

Skips: normal: E slice on F/B, misoriented; normal: M slice on F/B, misoriented; normal: S slice on R/L, oriented; normal: S slice on F/B, oriented; inverse: E slice on F/B, misoriented; inverse: S slice on U/D, oriented.

Each row is one route to a DR-xs on this scramble, shortest first; the last column is how far that DR-xs is from a real DR.

| # | Route | Length, moves | Kind | Starts from | Corner subset | Fewest turns to a real DR |
|---:|---|---:|---|---|---|---:|
| 1 | `R' F2 U2 L' D B2 D2 R` | 8 | DR-1s | skip: S slice on F/B, oriented | 4a4 | 4 |
| 2 | `(D' R B2 U F2 D R' U')` | 8 | DR-1s | skip: E slice on F/B, misoriented | 2c4 | 6 |
| 3 | `L' U2 R' F2 U2 L D L'` | 8 | DR-1s | skip: S slice on F/B, oriented | 0c3 | 5 |
| 4 | `R' F2 U2 L' D F2 U2 L'` | 8 | DR-1s | skip: S slice on F/B, oriented | 4a4 | 4 |
| 5 | `D' L B U2 L R' U2 B` | 8 | DR-1s | one-move slice EO: M slice on U/D, oriented | 4b2 | 4 |
| 6 | `D' L B' U2 L R' U2 B` | 8 | DR-1s | one-move slice EO: M slice on U/D, oriented | 4b2 | 5 |
| 7 | `(F B' U D2 L B2 L2 U R')` | 9 | DR-2s 8fe | EO on F/B | 4b2 | 4 |
| 8 | `(F B' U D2 L B2 L2 U R)` | 9 | DR-2s 8fe | EO on F/B | 4b2 | 4 |

Shown: 6 of the 40 DR-1s of 8 or less and 2 of the 6 DR-2s 8fe of 9 or less. Shortest normal DR: 9 moves.

<details>
<summary>Answers for scramble 63</summary>

Each row is the route with the same number above: the best finish of the method's form from it, then the whole solution written out for the scramble.

| # | Finish, moves | Solution | Solution length, moves |
|---:|---:|---|---:|
| 1 | 17 | `R' F2 U2 L' D B2 D2 R' D' R' L' F' R2 F U2 F2 U2 D2 B R2 F D2 B D2` | 24 |
| 2 | 16 | `D' R2 D' F' B L' F2 R' F2 L F2 R2 D2 R B2 U' R D' F2 U' B2 R' D` | 23 |
| 3 | 17 | `L' U2 R' F2 U2 L D L F2 D F2 U2 F2 L2 D' R2 B2 U2 B2 U' R L F B'` | 24 |
| 4 | 17 | `R' F2 U2 L' D F2 U2 R2 L' U B2 D2 R' L F L2 F D2 B' R2 F' L2 B2 U2 B'` | 25 |
| 5 | 16 | `D' L B U2 R' L U2 B L2 D L2 U L2 F2 L2 F2 U B2 R2 D2 F' B' L F2` | 24 |
| 6 | 15 | `D' L B' U2 R' L U2 B U B2 U' B2 R2 F2 L2 U2 R2 U L2 F' B' L' F2` | 23 |
| 7 | 14 | `R U2 B2 R B2 D2 B2 L' U2 L' U D L U' L2 B2 L' U' D2 F' B` | 21 |
| 8 | 14 | `R U2 B2 R B2 D2 B2 L' U2 L' U D L U' L2 B2 L' U' D2 F' B` | 21 |

Best of these: **21**, as short as the best through a normal DR of 10 or less. Normal DRs on this scramble: 21 through one of 10 or less, 20 through 11 or less, 20 through 12 or less.

</details>

#### Scramble 64

```
R' U' F D B2 R2 B2 R2 D' F2 L2 F2 U2 R D2 B' F2 D U R B U B2 R2 U' R' U' F // scramble
```

Skips: normal: M slice on U/D, oriented; normal: S slice on R/L, misoriented; inverse: S slice on R/L, misoriented.

Each row is one route to a DR-xs on this scramble, shortest first; the last column is how far that DR-xs is from a real DR.

| # | Route | Length, moves | Kind | Starts from | Corner subset | Fewest turns to a real DR |
|---:|---|---:|---|---|---|---:|
| 1 | `L2 B2 F' U2 R2 B2 R F'` | 8 | DR-1s | skip: M slice on U/D, oriented | 4b3 | 3 |
| 2 | `U2 R2 B F2 D2 B2 R F'` | 8 | DR-1s | skip: M slice on U/D, oriented | 4b3 | 3 |
| 3 | `U2 R2 B F2 D2 B2 R F` | 8 | DR-1s | skip: M slice on U/D, oriented | 4b3 | 4 |
| 4 | `F' U' B2 D2 R' F2 R D'` | 8 | DR-1s | one-move slice EO: E slice on F/B, oriented | 4b3 | 6 |
| 5 | `F' R B2 R2 D L' U2 L` | 8 | DR-1s | one-move slice EO: E slice on F/B, oriented | 2c5 | 6 |
| 6 | `L2 B2 F' U2 R2 B2 R F` | 8 | DR-1s | skip: M slice on U/D, oriented | 4b3 | 4 |
| 7 | `(F' D2 L2 F2 B' L2 F L2 D')` | 9 | DR-2s 8fe | skip: S slice on R/L, misoriented | 2c4 | 4 |
| 8 | `(F' D2 L2 F2 B' L2 F L2 D)` | 9 | DR-2s 8fe | skip: S slice on R/L, misoriented | 2c4 | 4 |

Shown: 6 of the 18 DR-1s of 8 or less and 2 of the 6 DR-2s 8fe of 9 or less. Shortest normal DR: 9 moves.

<details>
<summary>Answers for scramble 64</summary>

Each row is the route with the same number above: the best finish of the method's form from it, then the whole solution written out for the scramble.

| # | Finish, moves | Solution | Solution length, moves |
|---:|---:|---|---:|
| 1 | 15 | `L2 F' B2 U2 R2 B2 R F' U F' B' U2 R' B2 L2 D2 F2 U2 R' F2 L' F2 L` | 23 |
| 2 | 16 | `U2 R2 F2 B D2 B2 R F' U F B D2 L U2 D2 F2 L2 B2 L B2 U2 L' F2 L` | 24 |
| 3 | 15 | `U2 R2 F2 B D2 B2 R F U' D' F2 D' R2 F2 D F' B U2 R U2 R' F2 R` | 23 |
| 4 | 16 | `F' U' B2 D2 R' F2 R U2 D' F' L2 B R' L U R2 U L2 U2 B2 D R2 F2 B2` | 24 |
| 5 | 17 | `F' R B2 R2 D L' U2 L U2 D2 F U2 B R' L' U' R2 D B2 U R2 U' L2 D F2` | 25 |
| 6 | 15 | `L2 F' B2 U2 R2 B2 R F L2 F2 L2 U' F2 R2 D2 F B R F2 U2 R2 U2 R'` | 23 |
| 7 | 15 | `B R L F B L F2 R U2 L2 D2 B2 L U2 B2 D L2 F' L2 F2 B L2 D2 F` | 24 |
| 8 | 15 | `B2 U2 F2 B' D2 R2 F' L2 B R L' F' B' R L2 D' L2 F' L2 F2 B L2 D2 F` | 24 |

Best of these: **23**, longer than the best through a normal DR of 10 or less. Normal DRs on this scramble: 21 through one of 10 or less, 19 through 11 or less, 19 through 12 or less.

</details>

#### Scramble 65

```
R' U' F U' B2 R2 U' L2 U' F2 U2 B2 F2 R' D2 B2 F' U R B' D R U2 F R' U' F // scramble
```

Skips: normal: E slice on U/D, misoriented; normal: M slice on U/D, oriented; normal: M slice on F/B, misoriented; inverse: E slice on F/B, misoriented.

Each row is one route to a DR-xs on this scramble, shortest first; the last column is how far that DR-xs is from a real DR.

| # | Route | Length, moves | Kind | Starts from | Corner subset | Fewest turns to a real DR |
|---:|---|---:|---|---|---|---:|
| 1 | `(D' L U2 L D' R F2 D')` | 8 | DR-1s | skip: E slice on F/B, misoriented | 2c3 | 5 |
| 2 | `(D' L U2 L' D' R F2 D')` | 8 | DR-1s | skip: E slice on F/B, misoriented | 2c5 | 6 |
| 3 | `(D' L U2 L' D' R F2 D)` | 8 | DR-1s | skip: E slice on F/B, misoriented | 2c5 | 6 |
| 4 | `(D' L U2 L D' R F2 D)` | 8 | DR-1s | skip: E slice on F/B, misoriented | 2c3 | 5 |
| 5 | `(U R D' L' B2 R2 U2 D' R')` | 9 | DR-2s 8fe | skip: E slice on F/B, misoriented | 0c3 | 4 |
| 6 | `(U R D' L' B2 R2 U2 D' R)` | 9 | DR-2s 8fe | skip: E slice on F/B, misoriented | 0c3 | 4 |

Shown: 4 of the 4 DR-1s of 8 or less and 2 of the 2 DR-2s 8fe of 9 or less. Shortest normal DR: 10 moves.

<details>
<summary>Answers for scramble 65</summary>

Each row is the route with the same number above: the best finish of the method's form from it, then the whole solution written out for the scramble.

| # | Finish, moves | Solution | Solution length, moves |
|---:|---:|---|---:|
| 1 | 15 | `U' B2 D F' B' L B2 L' F2 R2 F2 U2 R' U2 D' F2 R' D L' U2 L' D` | 22 |
| 2 | 17 | `D2 B2 D R2 U F B U2 L F2 U2 R F2 U2 D2 R U2 D F2 R' D L U2 L' D` | 25 |
| 3 | 17 | `L2 U B2 R2 D B2 L2 U' R2 D2 F B R B2 L' D2 R2 D' F2 R' D L U2 L' D` | 25 |
| 4 | 14 | `U' B2 D F' B' L B2 L' F2 R2 F2 U2 R' U2 D' F2 R' D L' U2 L' D` | 22 |
| 5 | 17 | `R2 B2 D F2 B2 L2 U2 F2 U' F2 U2 L2 U' F' B U' D' R U2 D R2 B2 L D R' U'` | 26 |
| 6 | 16 | `F B U D' F D2 F2 U2 R2 F U2 F2 L2 F U2 R' L2 U2 D R2 B2 L D R' U'` | 25 |

Best of these: **22**, as short as the best through a normal DR of 12 or less. Normal DRs on this scramble: 22 through one of 10 or less, 22 through 11 or less, 22 through 12 or less.

</details>

#### Scramble 66

```
R' U' F U2 R2 B2 U2 B2 R' B2 R' U2 R' F R' U2 R2 D2 F U D2 L R' D2 R' U' F // scramble
```

Skips: none.

Each row is one route to a DR-xs on this scramble, shortest first; the last column is how far that DR-xs is from a real DR.

| # | Route | Length, moves | Kind | Starts from | Corner subset | Fewest turns to a real DR |
|---:|---|---:|---|---|---|---:|
| 1 | `U R' B R F' B2 L` | 7 | DR-1s | one-move slice EO: E slice on U/D, oriented | 4a3 | 3 |
| 2 | `U R' B R F' B2 L'` | 7 | DR-1s | one-move slice EO: E slice on U/D, oriented | 4a3 | 4 |
| 3 | `U R F R F2 B' L'` | 7 | DR-1s | one-move slice EO: E slice on U/D, oriented | 2c3 | 6 |
| 4 | `U R F R F2 B' L` | 7 | DR-1s | one-move slice EO: E slice on U/D, oriented | 2c3 | 5 |
| 5 | `U' U2 R' B R F' B2 L` | 8 | DR-1s | one-move slice EO: E slice on U/D, oriented | 4a3 | 3 |
| 6 | `U R' L2 B R F' B2 L'` | 8 | DR-1s | one-move slice EO: E slice on U/D, oriented | 2c3 | 5 |
| 7 | `U' F L F U' B' D2 B D` | 9 | DR-2s 8fe | EO on R/L | 4b5 | 4 |
| 8 | `U' F L F' U2 B' D' B' U'` | 9 | DR-2s 8fe | EO on R/L | 4b5 | 4 |

Shown: 6 of the 18 DR-1s of 8 or less and 2 of the 6 DR-2s 8fe of 9 or less. Shortest normal DR: 8 moves.

<details>
<summary>Answers for scramble 66</summary>

Each row is the route with the same number above: the best finish of the method's form from it, then the whole solution written out for the scramble.

| # | Finish, moves | Solution | Solution length, moves |
|---:|---:|---|---:|
| 1 | 17 | `U R' B R F' B2 L' U2 F2 R2 F L2 F R2 D2 F D2 R' L' D' L2 D R2` | 23 |
| 2 | 16 | `U R' B R F' B2 L' U2 F2 R2 F L2 F R2 D2 F D2 R' L' D' L2 D R2` | 23 |
| 3 | 15 | `U R F R F2 B' L' D2 R2 B2 D2 F' D2 L2 U2 F2 U2 R' L D' L2 D` | 22 |
| 4 | 16 | `U R F R F2 B' L F2 D2 B' R L' U2 R2 D B2 U' R2 U' F2 D F2 L2` | 23 |
| 5 | 17 | `U R' B R F' B2 L' U2 F2 R2 F L2 F R2 D2 F D2 R' L' D' L2 D R2` | 23 |
| 6 | 14 | `U R' L2 B R F' B2 L U2 L2 B2 D2 B' R L B2 D' R2 L2 B2 U` | 21 |
| 7 | 16 | `U' F L F U' B' D2 B U F B U B2 U L2 F2 D F2 D' B2 U' F2 B2 L2` | 24 |
| 8 | 16 | `U' F L F' U2 B' D' B' D' F' B' U R2 B2 D' B2 U B2 L2 D R2 D' R2 B2` | 24 |

Best of these: **21**, longer than the best through a normal DR of 10 or less. Normal DRs on this scramble: 20 through one of 10 or less, 19 through 11 or less, 17 through 12 or less.

</details>

#### Scramble 67

```
R' U' F U2 B2 D F2 L2 F2 R2 U' B2 L2 B' U' F' D' L2 B L F2 R F2 U2 R' U' F // scramble
```

Skips: none.

Each row is one route to a DR-xs on this scramble, shortest first; the last column is how far that DR-xs is from a real DR.

| # | Route | Length, moves | Kind | Starts from | Corner subset | Fewest turns to a real DR |
|---:|---|---:|---|---|---|---:|
| 1 | `L R2 F2 U F` | 5 | DR-1s | one-move slice EO: S slice on R/L, misoriented | 2c4 | 5 |
| 2 | `L R2 F2 U F'` | 5 | DR-1s | one-move slice EO: S slice on R/L, misoriented | 2c4 | 6 |
| 3 | `L' R2 L2 F2 U F` | 6 | DR-1s | one-move slice EO: S slice on R/L, misoriented | 2c4 | 5 |
| 4 | `L B2 D' F2 L2 F` | 6 | DR-1s | one-move slice EO: S slice on R/L, misoriented | 2c4 | 3 |
| 5 | `L B2 D' F2 L2 F'` | 6 | DR-1s | one-move slice EO: S slice on R/L, misoriented | 2c4 | 4 |
| 6 | `L B2 D' B2 R2 F'` | 6 | DR-1s | one-move slice EO: S slice on R/L, misoriented | 2c4 | 4 |
| 7 | `L R2 F2 B U2 F' U F` | 8 | DR-2s 8fe | one-move slice EO: S slice on R/L, misoriented | 2c4 | 4 |
| 8 | `L R2 F' R2 L2 B' D F'` | 8 | DR-2s 8fe | one-move slice EO: S slice on R/L, misoriented | 2c4 | 4 |

Shown: 6 of the 194 DR-1s of 8 or less and 2 of the 48 DR-2s 8fe of 9 or less. Shortest normal DR: 9 moves.

<details>
<summary>Answers for scramble 67</summary>

Each row is the route with the same number above: the best finish of the method's form from it, then the whole solution written out for the scramble.

| # | Finish, moves | Solution | Solution length, moves |
|---:|---:|---|---:|
| 1 | 15 | `R2 L F2 U F U F2 U' R2 B2 D2 R L' B R2 B L2 D2 F2 D2` | 20 |
| 2 | 16 | `R2 L F2 U F U F2 U' R2 B2 D2 R L' B R2 B L2 D2 F2 D2` | 20 |
| 3 | 15 | `R2 L F2 U F U F2 U' R2 B2 D2 R L' B R2 B L2 D2 F2 D2` | 20 |
| 4 | 14 | `L B2 D' F2 L2 F D' R' L F D2 L2 F R2 B' R2 B D2 F' L2` | 20 |
| 5 | 15 | `L B2 D' F2 L2 F D' R' L F D2 L2 F R2 B' R2 B D2 F' L2` | 20 |
| 6 | 15 | `L B2 D' B2 R2 F U' D2 R' L' B R2 B' U2 F R2 B' D2 R2 F` | 20 |
| 7 | 16 | `R2 L F2 B U2 F' U F2 B R' L F U2 F' D2 L2 B' R2 F2 L2 D2 F' U2` | 23 |
| 8 | 16 | `R2 L F' R2 L2 B' D F U2 F' B R L F' L2 D2 F B2 D2 F D2 B' R2` | 23 |

Best of these: **20**, longer than the best through a normal DR of 10 or less. Normal DRs on this scramble: 19 through one of 10 or less, 19 through 11 or less, 19 through 12 or less.

</details>

#### Scramble 68

```
R' U' F L2 B2 U L2 B2 U' B2 U L2 D' L U' F' R U' F L D2 F D B' R' U' F // scramble
```

Skips: normal: S slice on R/L, misoriented; inverse: E slice on F/B, oriented; inverse: S slice on F/B, misoriented.

Each row is one route to a DR-xs on this scramble, shortest first; the last column is how far that DR-xs is from a real DR.

| # | Route | Length, moves | Kind | Starts from | Corner subset | Fewest turns to a real DR |
|---:|---|---:|---|---|---|---:|
| 1 | `(F2 L' U2 L2 U' R)` | 6 | DR-1s | skip: E slice on F/B, oriented | 4b5 | 6 |
| 2 | `(F2 L' U2 L2 U' R')` | 6 | DR-1s | skip: E slice on F/B, oriented | 4b5 | 5 |
| 3 | `(F2 R2 L' D2 R2 U R')` | 7 | DR-1s | skip: E slice on F/B, oriented | 4b5 | 5 |
| 4 | `(F2 L' D2 R2 U D2 R)` | 7 | DR-1s | skip: E slice on F/B, oriented | 4b5 | 6 |
| 5 | `B' L' D2 L' F2 R D` | 7 | DR-1s | one-move slice EO: E slice on F/B, misoriented | 2c5 | 6 |
| 6 | `(F2 L' D2 R2 U D2 R')` | 7 | DR-1s | skip: E slice on F/B, oriented | 4b5 | 5 |

Shown: 6 of the 76 DR-1s of 8 or less and 0 of the 0 DR-2s 8fe of 9 or less. Shortest normal DR: 10 moves.

<details>
<summary>Answers for scramble 68</summary>

Each row is the route with the same number above: the best finish of the method's form from it, then the whole solution written out for the scramble.

| # | Finish, moves | Solution | Solution length, moves |
|---:|---:|---|---:|
| 1 | 17 | `D2 R2 U R2 U2 F2 D' R2 U F2 R' L' B U2 F D2 R U L2 U2 L F2` | 22 |
| 2 | 16 | `D2 R2 U R2 U2 F2 D' R2 U F2 R' L' B U2 F D2 R U L2 U2 L F2` | 22 |
| 3 | 17 | `L2 D' F2 L2 U' F2 D F2 U' L2 D B2 R' L B U2 F R U' R2 D2 R2 L F2` | 24 |
| 4 | 16 | `U R2 D' R2 F2 U2 F2 D' R' L' F' U2 B D2 B2 U2 R' U' D2 R2 D2 L F2` | 23 |
| 5 | 18 | `B' L' D2 L' F2 R D' R2 F2 L' B2 L F2 U2 D2 L' D2 L2 F' B D' B2 U L2` | 24 |
| 6 | 16 | `U L2 U2 L2 F2 D' B2 R L' F' R2 F D2 F' L2 F2 R U' D2 R2 D2 L F2` | 23 |

Best of these: **22**, longer than the best through a normal DR of 10 or less. Normal DRs on this scramble: 21 through one of 10 or less, 20 through 11 or less, 20 through 12 or less.

</details>

#### Scramble 69

```
R' U' F D L2 D' U2 B2 D2 R2 F2 L2 U F B2 R B' D L' B L2 D' R2 U' R' U' F // scramble
```

Skips: normal: M slice on R/L, oriented; inverse: M slice on R/L, oriented.

Each row is one route to a DR-xs on this scramble, shortest first; the last column is how far that DR-xs is from a real DR.

| # | Route | Length, moves | Kind | Starts from | Corner subset | Fewest turns to a real DR |
|---:|---|---:|---|---|---|---:|
| 1 | `(R' B L2 F2 U F)` | 6 | DR-1s | one-move slice EO: E slice on R/L, oriented | 2c3 | 4 |
| 2 | `(R' B' D' B2 L2 F')` | 6 | DR-1s | one-move slice EO: E slice on R/L, oriented | 2c3 | 4 |
| 3 | `(R' B' D' B2 L2 F)` | 6 | DR-1s | one-move slice EO: E slice on R/L, oriented | 2c3 | 5 |
| 4 | `(R' B' D' F2 R2 F')` | 6 | DR-1s | one-move slice EO: E slice on R/L, oriented | 2c3 | 4 |
| 5 | `(R' B' D' F2 R2 F)` | 6 | DR-1s | one-move slice EO: E slice on R/L, oriented | 2c3 | 3 |
| 6 | `(R' B L2 F2 U F')` | 6 | DR-1s | one-move slice EO: E slice on R/L, oriented | 2c3 | 5 |
| 7 | `(R' F2 R' F' U F2 R2 B' U)` | 9 | DR-2s 8fe | EO on R/L | 4b5 | 4 |
| 8 | `(R' F2 R' F' U B2 L2 B' D)` | 9 | DR-2s 8fe | EO on R/L | 4b5 | 4 |

Shown: 6 of the 161 DR-1s of 8 or less and 2 of the 4 DR-2s 8fe of 9 or less. Shortest normal DR: 9 moves.

<details>
<summary>Answers for scramble 69</summary>

Each row is the route with the same number above: the best finish of the method's form from it, then the whole solution written out for the scramble.

| # | Finish, moves | Solution | Solution length, moves |
|---:|---:|---|---:|
| 1 | 14 | `D' B2 R2 U' L2 D' R2 U F' B' L2 D2 R' F' B2 U' F2 L2 B' R` | 20 |
| 2 | 16 | `B2 R2 D2 B2 U' R2 U' D2 R2 F2 U2 F' B' U2 R' F B2 L2 B2 D B R` | 22 |
| 3 | 16 | `D2 L2 U' R2 U' F B' R F2 B2 L F2 U2 F2 U2 R F' L2 B2 D B R` | 22 |
| 4 | 16 | `D' L2 F2 L2 B2 U' L2 D' R2 U F' B' L2 D2 R' F' R2 F2 D B R` | 21 |
| 5 | 15 | `D' L2 F2 L2 B2 U' L2 D' R2 U F' B' L2 D2 R' F' R2 F2 D B R` | 21 |
| 6 | 15 | `D' B2 R2 U' L2 U' B2 D' L2 D2 F B R F' B2 U' F2 L2 B' R` | 20 |
| 7 | 16 | `D' R2 U B2 U' F2 U' F2 R2 U2 B2 U' F B U2 D B R2 F2 U' F R F2 R` | 24 |
| 8 | 15 | `D' L2 D' F B U' D F D2 F' L2 B L2 D2 B2 D' B L2 B2 U' F R F2 R` | 24 |

Best of these: **20**, longer than the best through a normal DR of 10 or less. Normal DRs on this scramble: 19 through one of 10 or less, 18 through 11 or less, 18 through 12 or less.

</details>

#### Scramble 70

```
R' U' F U2 L2 B2 L2 U B2 R2 D' R2 U B' D' L' F R2 F2 L2 R D B' F' U' R' U' F // scramble
```

Skips: normal: S slice on U/D, misoriented; inverse: S slice on U/D, misoriented; inverse: S slice on F/B, misoriented.

Each row is one route to a DR-xs on this scramble, shortest first; the last column is how far that DR-xs is from a real DR.

| # | Route | Length, moves | Kind | Starts from | Corner subset | Fewest turns to a real DR |
|---:|---|---:|---|---|---|---:|
| 1 | `B' R' L U L F2 D` | 7 | DR-1s | one-move slice EO: E slice on F/B, misoriented | 2c4 | 6 |
| 2 | `B R' L U' L F2 D'` | 7 | DR-1s | one-move slice EO: E slice on F/B, misoriented | 2c4 | 5 |
| 3 | `(F D R U' R2 U' L')` | 7 | DR-1s | one-move slice EO: M slice on F/B, oriented | 4b2 | 5 |
| 4 | `(F D R' U' R2 U' L)` | 7 | DR-1s | one-move slice EO: M slice on F/B, oriented | 2c4 | 6 |
| 5 | `B' R' L U L F2 D'` | 7 | DR-1s | one-move slice EO: E slice on F/B, misoriented | 2c4 | 6 |
| 6 | `B R' L U' L F2 D` | 7 | DR-1s | one-move slice EO: E slice on F/B, misoriented | 2c4 | 4 |
| 7 | `(F R U' L U2 D F' D' F)` | 9 | DR-2s 8fe | EO on R/L | 2c4 | 4 |
| 8 | `B' R U2 L D L' U L' U'` | 9 | DR-2s 8fe | one-move slice EO: E slice on F/B, misoriented | 2c4 | 4 |

Shown: 6 of the 56 DR-1s of 8 or less and 2 of the 6 DR-2s 8fe of 9 or less. Shortest normal DR: 9 moves.

<details>
<summary>Answers for scramble 70</summary>

Each row is the route with the same number above: the best finish of the method's form from it, then the whole solution written out for the scramble.

| # | Finish, moves | Solution | Solution length, moves |
|---:|---:|---|---:|
| 1 | 16 | `B' R' L U L F2 D F2 L2 U2 L' F B' U2 R2 L2 B2 U R2 D' F2 U' R2` | 23 |
| 2 | 17 | `B R' L U' L F2 U2 D' B2 R' F' B' U F2 L2 U F2 U B2 U' L2 U2 D F2` | 24 |
| 3 | 16 | `L2 D2 R2 D2 R' U2 L' F2 B2 U' D' B' L2 F R2 B2 L U R2 U R' D' F'` | 23 |
| 4 | 16 | `D2 B2 R2 D2 F2 L' U2 R' U' D' F L2 B' R2 F2 U2 L' U R2 U R D' F'` | 23 |
| 5 | 16 | `B' R' L U L F2 D' F2 L2 U2 L U2 D2 F' B' U R2 U' F2 R2 D2 L2 D` | 23 |
| 6 | 16 | `B R' L U' L F2 D F2 R2 L U2 R2 F B' U' R2 U' R2 B2 R2 B2 R2 D'` | 23 |
| 7 | 14 | `U2 F R2 B' D2 F R2 D2 B' R2 U D F2 B D F U2 D' L' U R' F'` | 22 |
| 8 | 16 | `B' R U2 L D L' U L' U2 D F' B' R2 U B2 D' L2 B2 U D2 F2 U F2 L2` | 24 |

Best of these: **22**, longer than the best through a normal DR of 10 or less. Normal DRs on this scramble: 21 through one of 10 or less, 18 through 11 or less, 18 through 12 or less.

</details>

#### Scramble 71

```
R' U' F U R2 F2 R' B' L F2 L2 D2 R B U' F2 U D L2 F2 R2 B2 U' B2 R' U' F // scramble
```

Skips: normal: E slice on U/D, misoriented; inverse: S slice on R/L, oriented.

Each row is one route to a DR-xs on this scramble, shortest first; the last column is how far that DR-xs is from a real DR.

| # | Route | Length, moves | Kind | Starts from | Corner subset | Fewest turns to a real DR |
|---:|---|---:|---|---|---|---:|
| 1 | `(U' L2 F2 D' R2 D' F)` | 7 | DR-1s | skip: S slice on R/L, oriented | 0c4 | 6 |
| 2 | `R' U2 D B R2 U' B'` | 7 | DR-1s | one-move slice EO: M slice on R/L, oriented | 2c3 | 5 |
| 3 | `R' U2 D B R2 U' B` | 7 | DR-1s | one-move slice EO: M slice on R/L, oriented | 2c3 | 6 |
| 4 | `(U' L2 F2 D' R2 D' F')` | 7 | DR-1s | skip: S slice on R/L, oriented | 0c4 | 6 |
| 5 | `(B D' R2 F' R2 F B2 U)` | 8 | DR-1s | skip: S slice on R/L, oriented | 2c3 | 4 |
| 6 | `R' U2 D B R2 U' F2 B'` | 8 | DR-1s | one-move slice EO: M slice on R/L, oriented | 2c3 | 5 |
| 7 | `B' U' D' R U' D' R2 B' D'` | 9 | DR-2s 8fe | EO on R/L | 4a4 | 4 |
| 8 | `B' U' D' R U' D' R2 B' D` | 9 | DR-2s 8fe | EO on R/L | 4a4 | 4 |

Shown: 6 of the 62 DR-1s of 8 or less and 2 of the 2 DR-2s 8fe of 9 or less. Shortest normal DR: 9 moves.

<details>
<summary>Answers for scramble 71</summary>

Each row is the route with the same number above: the best finish of the method's form from it, then the whole solution written out for the scramble.

| # | Finish, moves | Solution | Solution length, moves |
|---:|---:|---|---:|
| 1 | 16 | `B R2 D2 R2 U2 B R2 F2 R2 U D R' U2 F2 L F' B2 D R2 D F2 L2 U` | 23 |
| 2 | 16 | `R' U2 D B R2 U' B' L2 U2 F2 R2 L2 U B2 U F' B L' F2 D2 R' D2 L` | 23 |
| 3 | 16 | `R' U2 D B R2 U' B D F2 U' B2 R2 U' L2 B2 U' L2 F B' D2 R' D2 B2` | 23 |
| 4 | 16 | `L2 B2 D2 B' D2 R2 F L2 D2 F2 U' D' L' F2 D2 R F D R2 D F2 L2 U` | 23 |
| 5 | 13 | `F' L2 F' B' U2 F U2 L2 U D' R L2 F2 U' F' B2 R2 F R2 D B'` | 21 |
| 6 | 17 | `R' U2 D B R2 U' F2 B' U B2 U F B' L2 D2 L U2 L D2 B2 D2 R' D2 F2 B2` | 25 |
| 7 | 15 | `B' U' D' R U' D' R2 B' D' B' D2 F' L2 F2 L2 U2 B' U D F' B' U' D2 F2` | 24 |
| 8 | 16 | `B' U' D' R U' D' R2 B' U' F B R2 F2 U R2 U R2 D2 R2 F2 D B2 D F2` | 24 |

Best of these: **21**, longer than the best through a normal DR of 10 or less. Normal DRs on this scramble: 19 through one of 10 or less, 19 through 11 or less, 19 through 12 or less.

</details>

#### Scramble 72

```
R' U' F D F2 D' F2 L2 D2 U R2 B2 U2 L B2 F L U2 B2 F2 R2 U B2 F' R' U' F // scramble
```

Skips: normal: M slice on F/B, misoriented; inverse: M slice on R/L, misoriented.

Each row is one route to a DR-xs on this scramble, shortest first; the last column is how far that DR-xs is from a real DR.

| # | Route | Length, moves | Kind | Starts from | Corner subset | Fewest turns to a real DR |
|---:|---|---:|---|---|---|---:|
| 1 | `(B D R2 U L B2 L)` | 7 | DR-1s | one-move slice EO: S slice on F/B, oriented | 2c5 | 6 |
| 2 | `R' B2 D B2 R' D' L` | 7 | DR-1s | skip: M slice on F/B, misoriented | 4a1 | 5 |
| 3 | `(B' D2 B2 D L' F2 L)` | 7 | DR-1s | one-move slice EO: S slice on F/B, oriented | 2c4 | 6 |
| 4 | `(B D R2 U R D2 R')` | 7 | DR-1s | one-move slice EO: S slice on F/B, oriented | 2c5 | 6 |
| 5 | `(B D2 B2 D' R' D2 R')` | 7 | DR-1s | one-move slice EO: S slice on F/B, oriented | 2c4 | 6 |
| 6 | `(B' D2 B2 D L' F2 L')` | 7 | DR-1s | one-move slice EO: S slice on F/B, oriented | 2c4 | 6 |
| 7 | `D R D2 L' R2 U' R' D' L'` | 9 | DR-2s 8fe | skip: M slice on F/B, misoriented | 2c3 | 4 |
| 8 | `D R D2 L R2 U' R' D' L'` | 9 | DR-2s 8fe | skip: M slice on F/B, misoriented | 4a1 | 4 |

Shown: 6 of the 250 DR-1s of 8 or less and 2 of the 10 DR-2s 8fe of 9 or less. Shortest normal DR: 9 moves.

<details>
<summary>Answers for scramble 72</summary>

Each row is the route with the same number above: the best finish of the method's form from it, then the whole solution written out for the scramble.

| # | Finish, moves | Solution | Solution length, moves |
|---:|---:|---|---:|
| 1 | 16 | `D2 B2 L2 B R2 F L2 B2 R L F2 U F2 D R2 D' L' B2 L' U' R2 D' B'` | 23 |
| 2 | 15 | `R' B2 D B2 R' D' L B2 R2 D F2 U L2 D R2 F B R D2 L2 D2 L'` | 22 |
| 3 | 17 | `D2 B' R2 F' R' L' B2 U F2 U2 B2 L2 U2 L2 U F2 R2 L' F2 L D' B2 D2 B` | 24 |
| 4 | 15 | `D2 F' U2 B' D2 F2 R' L B2 R2 U' L2 U B2 D' R D2 R' U' R2 D' B'` | 22 |
| 5 | 16 | `R2 F D2 F L2 F' L2 F2 D2 R' L U F2 L2 U2 R L2 D2 R D B2 D2 B'` | 23 |
| 6 | 16 | `R2 L2 B R2 U2 B R2 F' R L U L2 B2 U' R2 D' L F2 L D' B2 D2 B` | 23 |
| 7 | 14 | `D R D2 R2 L' U' R' D' L B R L' F' B' R' F2 U2 R' L2 B2 U2 D2` | 22 |
| 8 | 14 | `D R D2 R2 L U' R' D' L F' R' L' F B R2 U2 B2 R' F2 B2 L' D2` | 22 |

Best of these: **22**, longer than the best through a normal DR of 10 or less. Normal DRs on this scramble: 20 through one of 10 or less, 20 through 11 or less, 20 through 12 or less.

</details>

#### Scramble 73

```
R' U' F U2 R2 D' L2 B2 U2 F2 R2 U' R' U L2 B' U B2 D U' R' B' U' R' U' F // scramble
```

Skips: normal: M slice on U/D, misoriented; normal: M slice on F/B, oriented; inverse: E slice on U/D, misoriented; inverse: E slice on R/L, misoriented; inverse: S slice on F/B, oriented.

Each row is one route to a DR-xs on this scramble, shortest first; the last column is how far that DR-xs is from a real DR.

| # | Route | Length, moves | Kind | Starts from | Corner subset | Fewest turns to a real DR |
|---:|---|---:|---|---|---|---:|
| 1 | `(L' B' D2 B' R2 L2 D)` | 7 | DR-1s | one-move slice EO: S slice on R/L, oriented | 4a3 | 6 |
| 2 | `(L' B' D2 B' R2 L2 D')` | 7 | DR-1s | one-move slice EO: S slice on R/L, oriented | 4a3 | 6 |
| 3 | `U L U' F2 R2 D F2 L'` | 8 | DR-1s | skip: M slice on F/B, oriented | 4a2 | 3 |
| 4 | `(L' B' L2 U2 F D2 L2 D)` | 8 | DR-1s | one-move slice EO: S slice on R/L, oriented | 4a3 | 6 |
| 5 | `(L' F' R2 B U' D' L2 B)` | 8 | DR-1s | one-move slice EO: S slice on R/L, oriented | 4a3 | 6 |
| 6 | `(L' F' R2 B U D R2 F)` | 8 | DR-1s | one-move slice EO: S slice on R/L, oriented | 4a3 | 6 |
| 7 | `B' D2 L B F2 R2 D2 R F` | 9 | DR-2s 8fe | skip: M slice on U/D, misoriented | 2c4 | 4 |
| 8 | `B' D2 L B F2 L2 U2 R B` | 9 | DR-2s 8fe | skip: M slice on U/D, misoriented | 2c4 | 4 |

Shown: 6 of the 52 DR-1s of 8 or less and 2 of the 4 DR-2s 8fe of 9 or less. Shortest normal DR: 9 moves.

<details>
<summary>Answers for scramble 73</summary>

Each row is the route with the same number above: the best finish of the method's form from it, then the whole solution written out for the scramble.

| # | Finish, moves | Solution | Solution length, moves |
|---:|---:|---|---:|
| 1 | 16 | `B' D2 B L2 B2 L2 D2 B' D2 L2 U' D L B2 R' U2 D' R2 L2 B D2 B L` | 23 |
| 2 | 16 | `F' R2 B' U2 D2 L2 D2 B U D L' U2 R B2 R2 F2 D R2 L2 B D2 B L` | 23 |
| 3 | 16 | `U L U' F2 R2 D F2 L' F U' D L B2 U2 L F2 R2 D2 F2 D2 F2 R D2 F2` | 24 |
| 4 | 17 | `B' L2 B' D2 B' U D B2 D2 F2 R' D2 L F2 D2 L2 B2 D' L2 D2 F' U2 L2 B L` | 25 |
| 5 | 16 | `B2 L2 D2 F U' D F2 U2 L U2 R B2 D2 L U2 L' B' L2 U D B' R2 F L` | 24 |
| 6 | 16 | `R2 F2 L2 D2 B U' D R D2 L' D2 R B2 L2 D2 L' F' R2 U' D' B' R2 F L` | 24 |
| 7 | 16 | `B' D2 L F2 B R2 D2 R F U D' R' L' U D L D2 R2 B2 R' D2 L' B2 D2 L'` | 25 |
| 8 | 15 | `B' D2 L F2 B L2 U2 R B L2 U' R L U' D L2 F2 D2 R2 L U2 L D2 R'` | 24 |

Best of these: **23**, longer than the best through a normal DR of 10 or less. Normal DRs on this scramble: 22 through one of 10 or less, 21 through 11 or less, 19 through 12 or less.

</details>

#### Scramble 74

```
R' U' F L2 U2 F2 L2 D L2 F2 D L2 U2 F' D' U B U R D U2 L F' R2 U' R' U' F // scramble
```

Skips: normal: M slice on F/B, misoriented; normal: S slice on U/D, misoriented; inverse: M slice on U/D, misoriented; inverse: S slice on R/L, misoriented.

Each row is one route to a DR-xs on this scramble, shortest first; the last column is how far that DR-xs is from a real DR.

| # | Route | Length, moves | Kind | Starts from | Corner subset | Fewest turns to a real DR |
|---:|---|---:|---|---|---|---:|
| 1 | `(L D' L2 D B R2 B)` | 7 | DR-1s | one-move slice EO: E slice on R/L, oriented | 2c3 | 6 |
| 2 | `(L D' L2 D F D2 F)` | 7 | DR-1s | one-move slice EO: E slice on R/L, oriented | 2c3 | 6 |
| 3 | `(L F' D2 R' B' F L)` | 7 | DR-1s | skip: M slice on U/D, misoriented | 4b2 | 6 |
| 4 | `(L D' L2 D F D2 F')` | 7 | DR-1s | one-move slice EO: E slice on R/L, oriented | 2c3 | 5 |
| 5 | `(B2 F' R' F' U2 F' L)` | 7 | DR-1s | skip: M slice on U/D, misoriented | 2c3 | 5 |
| 6 | `(L D' L2 D B R2 B')` | 7 | DR-1s | one-move slice EO: E slice on R/L, oriented | 2c3 | 6 |
| 7 | `(L2 D F B U' B' D2 B)` | 8 | DR-2s 8fe | skip: S slice on R/L, misoriented | 2c4 | 4 |
| 8 | `(L2 D F B U' F' R2 F)` | 8 | DR-2s 8fe | skip: S slice on R/L, misoriented | 2c4 | 4 |

Shown: 6 of the 112 DR-1s of 8 or less and 2 of the 20 DR-2s 8fe of 9 or less. Shortest normal DR: 9 moves.

<details>
<summary>Answers for scramble 74</summary>

Each row is the route with the same number above: the best finish of the method's form from it, then the whole solution written out for the scramble.

| # | Finish, moves | Solution | Solution length, moves |
|---:|---:|---|---:|
| 1 | 15 | `R2 U' F2 L2 F2 D' L2 U2 F B' R B2 R' U2 R B' R2 B' D' L2 D L'` | 22 |
| 2 | 15 | `U' F2 L2 F2 D F' B R2 L' U2 R' U2 D2 B2 R F' D2 F' D' L2 D L'` | 22 |
| 3 | 12 | `B2 R D2 R' F2 U D' B' U2 R2 F L F' B R D2 F L'` | 18 |
| 4 | 16 | `R2 D' B2 U L2 F' B R' U2 B2 U2 L U2 R F2 R2 F D2 F' D' L2 D L'` | 23 |
| 5 | 16 | `F2 D2 F2 R D2 L F2 D2 R U D' B U2 F L2 D2 L' F U2 F R F B2` | 23 |
| 6 | 16 | `R2 U' F2 L2 F2 D' L2 U2 F B' R B2 R' U2 R B' R2 B' D' L2 D L'` | 22 |
| 7 | 14 | `R2 F' D2 F' U2 F R2 U2 F' B2 R' L' F D2 B U F' B' D' L2` | 20 |
| 8 | 14 | `F' L2 F2 D2 B' R2 F L2 F' R L F' B L2 F' R2 F U F' B' D' L2` | 22 |

Best of these: **18**, as short as the best through a normal DR of 12 or less. Normal DRs on this scramble: 18 through one of 10 or less, 18 through 11 or less, 18 through 12 or less.

</details>

#### Scramble 75

```
R' U' F U2 L2 B' D2 B' F' L2 U2 L2 F2 R U L2 B D' B' L' F' L B' U R' U' F // scramble
```

Skips: normal: M slice on U/D, misoriented; normal: M slice on F/B, oriented; inverse: S slice on F/B, oriented.

Each row is one route to a DR-xs on this scramble, shortest first; the last column is how far that DR-xs is from a real DR.

| # | Route | Length, moves | Kind | Starts from | Corner subset | Fewest turns to a real DR |
|---:|---|---:|---|---|---|---:|
| 1 | `R U D B' U' B D2 F` | 8 | DR-1s | one-move slice EO: S slice on R/L, misoriented | 4b2 | 5 |
| 2 | `U L B' U2 L F2 L' F` | 8 | DR-1s | one-move slice EO: S slice on U/D, misoriented | 2c3 | 6 |
| 3 | `R U D B' U' F L2 B` | 8 | DR-1s | one-move slice EO: S slice on R/L, misoriented | 4b2 | 5 |
| 4 | `R U D B' U' B D2 F'` | 8 | DR-1s | one-move slice EO: S slice on R/L, misoriented | 4b2 | 5 |
| 5 | `R' U2 R2 U2 F' R2 D B'` | 8 | DR-1s | one-move slice EO: S slice on R/L, misoriented | 4a3 | 5 |
| 6 | `R' U2 R2 U2 F' R2 D B` | 8 | DR-1s | one-move slice EO: S slice on R/L, misoriented | 4a3 | 6 |
| 7 | `U D2 R' L2 U2 L2 B' L'` | 8 | DR-2s 8fe | one-move slice EO: S slice on U/D, misoriented | 4a1 | 4 |
| 8 | `U D2 R' L2 U2 L2 B' L` | 8 | DR-2s 8fe | one-move slice EO: S slice on U/D, misoriented | 4a1 | 4 |

Shown: 6 of the 8 DR-1s of 8 or less and 2 of the 10 DR-2s 8fe of 9 or less. Shortest normal DR: 10 moves.

<details>
<summary>Answers for scramble 75</summary>

Each row is the route with the same number above: the best finish of the method's form from it, then the whole solution written out for the scramble.

| # | Finish, moves | Solution | Solution length, moves |
|---:|---:|---|---:|
| 1 | 16 | `R U D B' U' B D2 F' U2 R2 D' R2 B2 U L2 F2 D' R L F' U2 B2 D2` | 23 |
| 2 | 16 | `U L B' U2 L F2 L' F' R' F2 R U' D B L2 U2 R2 B R2 B' U2 L2 D2` | 23 |
| 3 | 16 | `R U D B' U' F L2 B D L2 B2 L2 U' R L B' L2 U2 F U2 F R2 F' R2` | 24 |
| 4 | 15 | `R U D B' U' B D2 F' U2 R2 D' R2 B2 U L2 F2 D' R L F' U2 B2 D2` | 23 |
| 5 | 16 | `R' U2 R2 U2 F' R2 D B' U2 B2 U' R2 D' R L' U2 F R2 F R2 L2 D2 L2 F'` | 24 |
| 6 | 17 | `R' U2 R2 U2 F' R2 D B L2 F2 D2 B2 D' B2 D F2 B2 D F2 U' R' L' F' D2 F2` | 25 |
| 7 | 14 | `U D2 R' L2 U2 L2 B' R2 L' U F B' U D' F U2 L2 F2 B D2 B2 R2` | 22 |
| 8 | 15 | `U D2 R' L2 U2 L2 B' L D2 R2 B2 U D2 R2 D' R2 F2 R2 D F B U D` | 23 |

Best of these: **22**, longer than the best through a normal DR of 10 or less. Normal DRs on this scramble: 20 through one of 10 or less, 20 through 11 or less, 19 through 12 or less.

</details>

#### Scramble 76

```
R' U' F U F2 R F2 B2 L U L' B' R F L2 U2 B2 D B2 U F2 B2 R2 U' R' U' F // scramble
```

Skips: normal: M slice on R/L, misoriented; inverse: M slice on R/L, misoriented.

Each row is one route to a DR-xs on this scramble, shortest first; the last column is how far that DR-xs is from a real DR.

| # | Route | Length, moves | Kind | Starts from | Corner subset | Fewest turns to a real DR |
|---:|---|---:|---|---|---|---:|
| 1 | `F R D F2 R' B2 L' D'` | 8 | DR-1s | one-move slice EO: E slice on F/B, misoriented | 2c5 | 3 |
| 2 | `(L R2 U' F D' B' F' U)` | 8 | DR-1s | one-move slice EO: E slice on R/L, misoriented | 2c4 | 6 |
| 3 | `F R D F2 R' B2 L' D` | 8 | DR-1s | one-move slice EO: E slice on F/B, misoriented | 2c5 | 4 |
| 4 | `(L R2 U' F D' B' F' U')` | 8 | DR-1s | one-move slice EO: E slice on R/L, misoriented | 2c4 | 6 |
| 5 | `(L R2 U' F D B' F' U)` | 8 | DR-1s | one-move slice EO: E slice on R/L, misoriented | 2c4 | 6 |
| 6 | `(L' D B U B L2 B D)` | 8 | DR-1s | one-move slice EO: E slice on R/L, misoriented | 4a2 | 5 |

Shown: 6 of the 8 DR-1s of 8 or less and 0 of the 0 DR-2s 8fe of 9 or less. Shortest normal DR: 9 moves.

<details>
<summary>Answers for scramble 76</summary>

Each row is the route with the same number above: the best finish of the method's form from it, then the whole solution written out for the scramble.

| # | Finish, moves | Solution | Solution length, moves |
|---:|---:|---|---:|
| 1 | 15 | `F R D F2 R' B2 L' D' R' F B' L2 U L2 U' B2 L2 D' B2 L2 U' B2 L2` | 23 |
| 2 | 16 | `D' F2 U L2 D' R2 U' R L F R2 D2 L2 F' L2 B2 U' F B D F' U R2 L'` | 24 |
| 3 | 15 | `F R D F2 R' B2 L' D R F2 R B2 L' B2 R F' B' R2 D L2 U R2 U'` | 23 |
| 4 | 16 | `D F2 B2 D' R' L F2 L2 B' D2 F' R2 B U2 B' L2 U F B D F' U R2 L'` | 24 |
| 5 | 14 | `F2 B2 D R2 U2 R' L B U2 B L2 B D2 R2 U' F B D' F' U R2 L'` | 22 |
| 6 | 17 | `U2 D F2 B2 D R' L' B2 D2 F' R2 F2 R2 U2 F' R2 B2 D' B' L2 B' U' B' D' L` | 25 |

Best of these: **22**, longer than the best through a normal DR of 10 or less. Normal DRs on this scramble: 21 through one of 10 or less, 21 through 11 or less, 20 through 12 or less.

</details>

#### Scramble 77

```
R' U' F D2 B2 U2 L2 B2 L2 B2 U F2 U B' L' U2 B D2 U F U2 R' B2 D2 R' U' F // scramble
```

Skips: normal: M slice on U/D, misoriented; normal: S slice on U/D, oriented; inverse: S slice on R/L, oriented; inverse: S slice on F/B, oriented.

Each row is one route to a DR-xs on this scramble, shortest first; the last column is how far that DR-xs is from a real DR.

| # | Route | Length, moves | Kind | Starts from | Corner subset | Fewest turns to a real DR |
|---:|---|---:|---|---|---|---:|
| 1 | `(B F2 D B2 L' D)` | 6 | DR-1s | one-move slice EO: E slice on F/B, oriented | 2c4 | 6 |
| 2 | `(B F2 D B2 L' D')` | 6 | DR-1s | one-move slice EO: E slice on F/B, oriented | 2c4 | 6 |
| 3 | `R L' F R B' U2 B'` | 7 | DR-1s | skip: S slice on U/D, oriented | 4b2 | 6 |
| 4 | `R L' F R F' L2 F'` | 7 | DR-1s | skip: S slice on U/D, oriented | 4b2 | 6 |
| 5 | `F2 R F' L2 U2 F R'` | 7 | DR-1s | skip: S slice on U/D, oriented | 4b2 | 5 |
| 6 | `(B R' U F2 D L' D')` | 7 | DR-1s | one-move slice EO: E slice on F/B, oriented | 4a2 | 6 |

Shown: 6 of the 164 DR-1s of 8 or less and 0 of the 0 DR-2s 8fe of 9 or less. Shortest normal DR: 9 moves.

<details>
<summary>Answers for scramble 77</summary>

Each row is the route with the same number above: the best finish of the method's form from it, then the whole solution written out for the scramble.

| # | Finish, moves | Solution | Solution length, moves |
|---:|---:|---|---:|
| 1 | 16 | `R2 D2 B2 D' F2 U R2 B2 R2 B2 R' L' F' U2 F R2 D' L B2 D' F2 B'` | 22 |
| 2 | 17 | `D F2 U' R' L D2 L2 F L2 U2 B R2 D2 F D2 F L2 D L B2 D' F2 B'` | 23 |
| 3 | 16 | `R L' F R B' U2 B' D' L2 D2 F2 D F2 D' L2 D' B2 R2 U R L B' D2` | 23 |
| 4 | 15 | `R L' F R F' L2 F' U2 B2 D' B2 U F2 R' L F L2 B' L2 F' D2 B'` | 22 |
| 5 | 16 | `F2 R F' L2 U2 F R' U B2 R2 F2 U L2 U2 B2 U' R L' D2 F' D2 L2 F2` | 23 |
| 6 | 17 | `F2 B2 L2 D' B2 U2 L2 B2 U' F2 R L D2 B' D2 B D' L D' F2 U' R B'` | 23 |

Best of these: **22**, longer than the best through a normal DR of 10 or less. Normal DRs on this scramble: 19 through one of 10 or less, 19 through 11 or less, 19 through 12 or less.

</details>

#### Scramble 78

```
R' U' F R2 D' L2 D' L2 B2 D' F2 L2 U' B R U F2 D B2 U L' U2 R U2 R' U' F // scramble
```

Skips: normal: E slice on U/D, misoriented.

Each row is one route to a DR-xs on this scramble, shortest first; the last column is how far that DR-xs is from a real DR.

| # | Route | Length, moves | Kind | Starts from | Corner subset | Fewest turns to a real DR |
|---:|---|---:|---|---|---|---:|
| 1 | `U' R B' D2 L2 F R2 F'` | 8 | DR-1s | one-move slice EO: M slice on U/D, oriented | 4a4 | 6 |
| 2 | `U' R F' R2 D2 F U2 B` | 8 | DR-1s | one-move slice EO: M slice on U/D, oriented | 4a4 | 5 |
| 3 | `U' R B' D2 L2 B U2 B` | 8 | DR-1s | one-move slice EO: M slice on U/D, oriented | 4a4 | 5 |
| 4 | `U' R B' D2 L2 B U2 B'` | 8 | DR-1s | one-move slice EO: M slice on U/D, oriented | 4a4 | 6 |
| 5 | `U' R F' R2 D2 B L2 F'` | 8 | DR-1s | one-move slice EO: M slice on U/D, oriented | 4a4 | 5 |
| 6 | `U' R F' R2 D2 F U2 B'` | 8 | DR-1s | one-move slice EO: M slice on U/D, oriented | 4a4 | 6 |

Shown: 6 of the 7 DR-1s of 8 or less and 0 of the 0 DR-2s 8fe of 9 or less. Shortest normal DR: 9 moves.

<details>
<summary>Answers for scramble 78</summary>

Each row is the route with the same number above: the best finish of the method's form from it, then the whole solution written out for the scramble.

| # | Finish, moves | Solution | Solution length, moves |
|---:|---:|---|---:|
| 1 | 17 | `U' R B' D2 L2 F R2 F' B2 R2 U R2 D R2 U2 F2 U' B2 U2 F' B L' D2 B2 U2` | 25 |
| 2 | 17 | `U' R F' R2 D2 F U2 B R2 U' L2 D' R2 B2 D2 B2 D' F2 U R2 U' F B' R' F2` | 25 |
| 3 | 17 | `U' R B' D2 L2 B U2 B L2 U' B2 U' F' B D2 R D2 B2 R F2 L U2 R' B2 R2` | 25 |
| 4 | 16 | `U' R B' D2 L2 B U2 F2 B' L2 D L2 D F2 U' F B' L' B2 R' B2 U2 R2 L` | 24 |
| 5 | 16 | `U' R F' R2 D2 B L2 F' L2 U' R2 D' B2 R2 U' D' B2 D' F B R D2 F2 D2` | 24 |
| 6 | 18 | `U' R F' R2 D2 F U2 B' L2 U' L2 U' F B' L' B2 D2 B2 L F2 R2 U2 R F2 U2 L'` | 26 |

Best of these: **24**, longer than the best through a normal DR of 10 or less. Normal DRs on this scramble: 21 through one of 10 or less, 21 through 11 or less, 20 through 12 or less.

</details>

#### Scramble 79

```
R' U' F L2 U B2 L2 B2 D2 U' F2 D' B' U' L U B2 D L' B U' L2 R U' R' U' F // scramble
```

Skips: normal: E slice on F/B, misoriented; normal: S slice on U/D, oriented.

Each row is one route to a DR-xs on this scramble, shortest first; the last column is how far that DR-xs is from a real DR.

| # | Route | Length, moves | Kind | Starts from | Corner subset | Fewest turns to a real DR |
|---:|---|---:|---|---|---|---:|
| 1 | `B L2 D2 B R L2 B'` | 7 | DR-1s | skip: S slice on U/D, oriented | 2c5 | 4 |
| 2 | `L F R' B' D2 F' R` | 7 | DR-1s | skip: S slice on U/D, oriented | 2c3 | 5 |
| 3 | `L F R' B' D2 F' R'` | 7 | DR-1s | skip: S slice on U/D, oriented | 2c3 | 6 |
| 4 | `B L2 D2 B R L2 B` | 7 | DR-1s | skip: S slice on U/D, oriented | 2c5 | 5 |
| 5 | `L F R' F2 B U2 F' L` | 8 | DR-1s | skip: S slice on U/D, oriented | 2c3 | 6 |
| 6 | `B L2 D2 B R L2 F2 B'` | 8 | DR-1s | skip: S slice on U/D, oriented | 2c5 | 5 |

Shown: 6 of the 10 DR-1s of 8 or less and 0 of the 0 DR-2s 8fe of 9 or less. Shortest normal DR: 9 moves.

<details>
<summary>Answers for scramble 79</summary>

Each row is the route with the same number above: the best finish of the method's form from it, then the whole solution written out for the scramble.

| # | Finish, moves | Solution | Solution length, moves |
|---:|---:|---|---:|
| 1 | 17 | `B L2 D2 B R L2 F2 B' L2 F2 D R' L' U2 R2 U2 F R2 F' D2 L2 B' L2 B'` | 24 |
| 2 | 17 | `L F R' B' D2 F' R F2 D2 B2 U' R' L D2 F' D2 F2 B L2 U2 F' L2 F U2` | 24 |
| 3 | 16 | `L F R' B' D2 F' R' D' F2 L2 D' R' L D2 B' R2 F' D2 R2 D2 R2 B' U2` | 23 |
| 4 | 16 | `B L2 D2 B R L2 B L2 B2 D R L U2 L2 U2 F R2 F' D2 L2 B' L2 B'` | 23 |
| 5 | 16 | `L F R' F2 B U2 F' L B2 U2 R2 D' B2 L2 D' B2 R' L B' R2 D2 L2 B2 U2` | 24 |
| 6 | 16 | `B L2 D2 B R L2 F2 B' L2 F2 D R' L' U2 R2 U2 F R2 F' D2 L2 B' L2 B'` | 24 |

Best of these: **23**, longer than the best through a normal DR of 10 or less. Normal DRs on this scramble: 21 through one of 10 or less, 21 through 11 or less, 21 through 12 or less.

</details>

#### Scramble 80

```
R' U' F U L D R' U2 F B L2 D' B2 R L2 B L2 D2 B L2 B2 R2 B U2 R' U' F // scramble
```

Skips: inverse: M slice on F/B, misoriented.

Each row is one route to a DR-xs on this scramble, shortest first; the last column is how far that DR-xs is from a real DR.

| # | Route | Length, moves | Kind | Starts from | Corner subset | Fewest turns to a real DR |
|---:|---|---:|---|---|---|---:|
| 1 | `(R' D B2 U2 F2 B2 R')` | 7 | DR-1s | skip: M slice on F/B, misoriented | 4a4 | 6 |
| 2 | `(R' D F2 D2 F2 B2 L)` | 7 | DR-1s | skip: M slice on F/B, misoriented | 4a4 | 5 |
| 3 | `(D R' B2 U L' U' L')` | 7 | DR-1s | skip: M slice on F/B, misoriented | 2c3 | 5 |
| 4 | `(R' D F2 D2 F2 B2 L')` | 7 | DR-1s | skip: M slice on F/B, misoriented | 4a4 | 6 |
| 5 | `(D R' B2 U L' U' L)` | 7 | DR-1s | skip: M slice on F/B, misoriented | 2c3 | 6 |
| 6 | `(D R B2 U L' U' L')` | 7 | DR-1s | skip: M slice on F/B, misoriented | 2c3 | 6 |
| 7 | `(D F2 R B2 U L' U' R)` | 8 | DR-2s 8fe | skip: M slice on F/B, misoriented | 4b5 | 4 |
| 8 | `(D' B2 L F2 U' L' U' R')` | 8 | DR-2s 8fe | skip: M slice on F/B, misoriented | 2c5 | 4 |

Shown: 6 of the 110 DR-1s of 8 or less and 2 of the 60 DR-2s 8fe of 9 or less. Shortest normal DR: 9 moves.

<details>
<summary>Answers for scramble 80</summary>

Each row is the route with the same number above: the best finish of the method's form from it, then the whole solution written out for the scramble.

| # | Finish, moves | Solution | Solution length, moves |
|---:|---:|---|---:|
| 1 | 17 | `L' U2 L D2 R D2 L2 D2 F2 L F B U B2 U' B2 U2 R F2 B2 U2 B2 D' R` | 24 |
| 2 | 16 | `B2 R2 D2 L B2 U2 R B2 R' B2 L F' B' D' L2 D L' F2 B2 D2 F2 D' R` | 23 |
| 3 | 16 | `R B2 D2 R' B2 R2 U2 B2 R' F2 L F B' D' B2 U2 L U L U' B2 R D'` | 23 |
| 4 | 17 | `B2 R2 D2 L B2 U2 R B2 R' B2 L F' B' D' L2 D L' F2 B2 D2 F2 D' R` | 23 |
| 5 | 16 | `R2 F2 D2 L' D2 R' D2 L' U2 D2 F' B U R2 F2 U L' U L U' B2 R D'` | 23 |
| 6 | 15 | `D2 L' F2 L F B' D2 F2 R2 B2 L2 D F2 D2 R2 L U L U' B2 R' D'` | 22 |
| 7 | 16 | `F B R' L U2 F' L2 F U2 F2 B L2 F R2 F' R U L U' B2 R' F2 D'` | 23 |
| 8 | 17 | `L2 D2 B2 R D2 L' D2 F2 L' D2 L B2 L F B' L' U L U F2 L' B2 D` | 23 |

Best of these: **22**, longer than the best through a normal DR of 10 or less. Normal DRs on this scramble: 19 through one of 10 or less, 19 through 11 or less, 19 through 12 or less.

</details>

#### Scramble 81

```
R' U' F D2 R' F2 B2 U F B' U D2 L F D' F2 D' L2 D L2 U B2 D' F2 R' U' F // scramble
```

Skips: normal: S slice on U/D, oriented.

Each row is one route to a DR-xs on this scramble, shortest first; the last column is how far that DR-xs is from a real DR.

| # | Route | Length, moves | Kind | Starts from | Corner subset | Fewest turns to a real DR |
|---:|---|---:|---|---|---|---:|
| 1 | `(F' R' U2 D' R')` | 5 | DR-1s | one-move slice EO: M slice on F/B, misoriented | 2c4 | 6 |
| 2 | `(F' R' U2 D' R)` | 5 | DR-1s | one-move slice EO: M slice on F/B, misoriented | 2c4 | 6 |
| 3 | `(F' R' U2 D' L2 R')` | 6 | DR-1s | one-move slice EO: M slice on F/B, misoriented | 2c4 | 6 |
| 4 | `(F F2 R' U2 D' R)` | 6 | DR-1s | one-move slice EO: M slice on F/B, misoriented | 2c4 | 6 |
| 5 | `(F' R' U2 D' L2 R)` | 6 | DR-1s | one-move slice EO: M slice on F/B, misoriented | 2c4 | 6 |
| 6 | `(F F2 R' U2 D' R')` | 6 | DR-1s | one-move slice EO: M slice on F/B, misoriented | 2c4 | 6 |
| 7 | `(F R U' B2 U L D' B2 L)` | 9 | DR-2s 8fe | one-move slice EO: M slice on F/B, misoriented | 4b5 | 4 |
| 8 | `(F R U' B2 U L D' B2 L')` | 9 | DR-2s 8fe | one-move slice EO: M slice on F/B, misoriented | 4b5 | 4 |

Shown: 6 of the 154 DR-1s of 8 or less and 2 of the 2 DR-2s 8fe of 9 or less. Shortest normal DR: 9 moves.

<details>
<summary>Answers for scramble 81</summary>

Each row is the route with the same number above: the best finish of the method's form from it, then the whole solution written out for the scramble.

| # | Finish, moves | Solution | Solution length, moves |
|---:|---:|---|---:|
| 1 | 17 | `U2 L' D2 R U2 F' B U' B2 L2 F2 U' F2 U' F2 U' R' U2 D R F` | 21 |
| 2 | 16 | `U2 L' D2 R U2 F' B U' B2 L2 F2 U' F2 U' F2 U' R' U2 D R F` | 21 |
| 3 | 17 | `U2 R' B2 L F B L2 U F2 R2 F2 D L2 D L2 B2 U' R L2 U2 D R F` | 23 |
| 4 | 16 | `U2 L' D2 R U2 F' B U' B2 L2 F2 U' F2 U' F2 U' R' U2 D R F` | 21 |
| 5 | 16 | `B2 D2 L B2 R F' B D B2 U' R2 D' B2 U2 B2 D' R' L2 U2 D R F` | 22 |
| 6 | 17 | `U2 L' D2 R U2 F' B U' B2 L2 F2 U' F2 U' F2 U' R' U2 D R F` | 21 |
| 7 | 16 | `L2 D2 R' F2 D2 R' B2 L U2 R' F2 L F B' R L2 B2 D L' U' B2 U R' F'` | 24 |
| 8 | 16 | `L2 D2 R' F2 D2 R' B2 L U2 R' F2 L F B' R L2 B2 D L' U' B2 U R' F'` | 24 |

Best of these: **21**, as short as the best through a normal DR of 10 or less. Normal DRs on this scramble: 21 through one of 10 or less, 19 through 11 or less, 19 through 12 or less.

</details>

#### Scramble 82

```
R' U' F R2 D' U' L2 D L2 R2 U' B2 L2 F U F2 L U2 L2 B F L R2 U2 R' U' F // scramble
```

Skips: normal: S slice on U/D, misoriented; normal: S slice on R/L, oriented; normal: S slice on F/B, oriented; inverse: M slice on U/D, misoriented; inverse: M slice on R/L, oriented; inverse: M slice on F/B, oriented; inverse: S slice on F/B, misoriented.

Each row is one route to a DR-xs on this scramble, shortest first; the last column is how far that DR-xs is from a real DR.

| # | Route | Length, moves | Kind | Starts from | Corner subset | Fewest turns to a real DR |
|---:|---|---:|---|---|---|---:|
| 1 | `D' F2 D2 R' D R F2 D` | 8 | DR-1s | skip: S slice on F/B, oriented | 2c3 | 5 |
| 2 | `(U' F' D F' L2 D F' U')` | 8 | DR-1s | skip: M slice on R/L, oriented | 4b5 | 3 |
| 3 | `U L U' L2 D2 U L U` | 8 | DR-1s | skip: S slice on F/B, oriented | 2c4 | 6 |
| 4 | `(D' L' D L' B2 D L' D)` | 8 | DR-1s | skip: M slice on F/B, oriented | 4b5 | 6 |
| 5 | `D' L U' B2 D2 U R D` | 8 | DR-1s | skip: S slice on F/B, oriented | 0c4 | 6 |
| 6 | `(D L' D' F2 L U' L' U')` | 8 | DR-1s | skip: M slice on F/B, oriented | 2c3 | 6 |
| 7 | `F' L' U2 F' B2 R' B2 U2 B` | 9 | DR-2s 8fe | skip: S slice on U/D, misoriented | 2c3 | 4 |
| 8 | `L' U2 F' R2 L U2 L D2 F'` | 9 | DR-2s 8fe | skip: S slice on U/D, misoriented | 4a3 | 4 |

Shown: 6 of the 32 DR-1s of 8 or less and 2 of the 8 DR-2s 8fe of 9 or less. Shortest normal DR: 9 moves.

<details>
<summary>Answers for scramble 82</summary>

Each row is the route with the same number above: the best finish of the method's form from it, then the whole solution written out for the scramble.

| # | Finish, moves | Solution | Solution length, moves |
|---:|---:|---|---:|
| 1 | 15 | `D' F2 D2 R' D R F2 D R2 U2 L' B2 U2 L' U2 L B2 U' D L2 B' D2 F` | 23 |
| 2 | 15 | `L2 U2 L B2 R' U2 L D2 L' U D' L2 B2 U2 B' U F D' L2 F D' F U` | 23 |
| 3 | 16 | `U L U' L2 U D2 L U F2 R U2 L' B2 L' U2 R B2 D2 B2 U D B D2 F` | 24 |
| 4 | 16 | `R2 D2 R' D2 L2 F2 R' F2 L2 U D B' D2 B' D2 F' D' L D' B2 L D' L D` | 24 |
| 5 | 16 | `D' L U' B2 U D2 R D L' D2 B2 R' U D' R2 B2 D2 B L2 D2 L2 F2 D2 F'` | 24 |
| 6 | 16 | `F2 R L D2 L U' D R2 F' D2 B' U2 L2 U2 F2 U D2 L U L' F2 D L D'` | 24 |
| 7 | 13 | `F' L' U2 F' B2 R' B2 U2 B L2 U' F B U' D' F L2 B2 D2 L2 U2 F` | 22 |
| 8 | 16 | `L' U2 F' R2 L U2 L D2 B U D' B' R2 U2 F' L2 F U2 D2 R2 F L2 B'` | 23 |

Best of these: **22**, longer than the best through a normal DR of 10 or less. Normal DRs on this scramble: 20 through one of 10 or less, 20 through 11 or less, 19 through 12 or less.

</details>

#### Scramble 83

```
R' U' F U R B2 R' F2 D' L U' B' R L2 F2 D B2 U2 F2 R2 U' D' R' U' F // scramble
```

Skips: none.

Each row is one route to a DR-xs on this scramble, shortest first; the last column is how far that DR-xs is from a real DR.

| # | Route | Length, moves | Kind | Starts from | Corner subset | Fewest turns to a real DR |
|---:|---|---:|---|---|---|---:|
| 1 | `B' L' B2 L2 D' F2 R2 U` | 8 | DR-1s | one-move slice EO: S slice on F/B, oriented | 0c3 | 5 |
| 2 | `B' R D F2 D F2 U R` | 8 | DR-1s | one-move slice EO: S slice on F/B, oriented | 2c3 | 5 |
| 3 | `B' L' B2 R2 U' F2 L2 U'` | 8 | DR-1s | one-move slice EO: S slice on F/B, oriented | 0c3 | 3 |
| 4 | `B' R U R2 U L2 U R'` | 8 | DR-1s | one-move slice EO: S slice on F/B, oriented | 2c3 | 6 |
| 5 | `B' L' B2 L2 U' R2 B2 D` | 8 | DR-1s | one-move slice EO: S slice on F/B, oriented | 0c3 | 6 |
| 6 | `B' L' B2 R2 U' F2 L2 U` | 8 | DR-1s | one-move slice EO: S slice on F/B, oriented | 0c3 | 4 |

Shown: 6 of the 32 DR-1s of 8 or less and 0 of the 0 DR-2s 8fe of 9 or less. Shortest normal DR: 9 moves.

<details>
<summary>Answers for scramble 83</summary>

Each row is the route with the same number above: the best finish of the method's form from it, then the whole solution written out for the scramble.

| # | Finish, moves | Solution | Solution length, moves |
|---:|---:|---|---:|
| 1 | 17 | `B' L' B2 L2 D' F2 R2 U F2 L2 F2 R' B2 L' D2 L U2 R D2 L' U' D' F U2 B'` | 25 |
| 2 | 15 | `B' R D F2 D F2 U R D R2 B2 R2 U R2 D2 R2 L2 D R L B' R2 F'` | 23 |
| 3 | 17 | `B' L' B2 R2 U' F2 L2 U' R F2 U' D' F D2 R2 B D2 R2 F' R2 B R2 F' L2 B'` | 25 |
| 4 | 15 | `B' R U R2 U L2 U R' D B2 L2 U R L' F' R2 U2 D2 R2 F' R2 F B2` | 23 |
| 5 | 18 | `B' L' B2 L2 U' R2 B2 D R2 F2 L F2 D2 R2 D2 L B2 L' D2 L2 B2 U' D B R2 F'` | 26 |
| 6 | 17 | `B' L' B2 R2 U' F2 L2 U L D2 L' U2 R B2 U' D F' U2 B' R2 B R2 U2 B R2` | 25 |

Best of these: **23**, longer than the best through a normal DR of 10 or less. Normal DRs on this scramble: 22 through one of 10 or less, 20 through 11 or less, 20 through 12 or less.

</details>

#### Scramble 84

```
R' U' F U L D' L2 B2 D2 B D F2 B2 R' D F2 B2 U' F2 U D2 B2 R' U' F // scramble
```

Skips: normal: S slice on U/D, misoriented.

Each row is one route to a DR-xs on this scramble, shortest first; the last column is how far that DR-xs is from a real DR.

| # | Route | Length, moves | Kind | Starts from | Corner subset | Fewest turns to a real DR |
|---:|---|---:|---|---|---|---:|
| 1 | `L D2 R B L' B' L' B` | 8 | DR-1s | skip: S slice on U/D, misoriented | 0c4 | 6 |
| 2 | `B2 R L' B R B D2 B` | 8 | DR-1s | skip: S slice on U/D, misoriented | 2c3 | 6 |
| 3 | `L D2 F R B' R' U2 F'` | 8 | DR-1s | skip: S slice on U/D, misoriented | 4a3 | 3 |
| 4 | `B2 R L' B R F L2 F` | 8 | DR-1s | skip: S slice on U/D, misoriented | 2c3 | 5 |
| 5 | `L D2 R B L' B' L' B'` | 8 | DR-1s | skip: S slice on U/D, misoriented | 0c4 | 6 |
| 6 | `B2 R L' B R F L2 F'` | 8 | DR-1s | skip: S slice on U/D, misoriented | 2c3 | 5 |

Shown: 6 of the 8 DR-1s of 8 or less and 0 of the 0 DR-2s 8fe of 9 or less. Shortest normal DR: 8 moves.

<details>
<summary>Answers for scramble 84</summary>

Each row is the route with the same number above: the best finish of the method's form from it, then the whole solution written out for the scramble.

| # | Finish, moves | Solution | Solution length, moves |
|---:|---:|---|---:|
| 1 | 16 | `L D2 R B L' B' L' B' R' U2 R B2 R U D L2 F L2 F D2 B' R2 U2` | 23 |
| 2 | 14 | `B2 R L' B R B D2 B U2 L2 B2 L' U2 R F2 U' D F' U2 B' L2 F` | 22 |
| 3 | 17 | `L D2 F R B' R' U2 F' D2 R2 U2 B2 L' U2 D2 F2 R' B2 R U2 R U' D' B R2` | 25 |
| 4 | 15 | `B2 R L' B R F L2 F R2 F2 R' D2 L U2 D2 R' B2 R' B2 U' D' B' R2` | 23 |
| 5 | 15 | `L D2 R B L' B' L' B' R' U2 R B2 R U D L2 F L2 F D2 B' R2 U2` | 23 |
| 6 | 16 | `B2 R L' B R F L2 F' R D2 L' F2 U D' B R2 B' D2 R2 L2 U2 B' D2 R2` | 24 |

Best of these: **22**, longer than the best through a normal DR of 10 or less. Normal DRs on this scramble: 20 through one of 10 or less, 20 through 11 or less, 20 through 12 or less.

</details>

#### Scramble 85

```
R' U' F D L2 R2 U B2 L2 B2 L2 R2 U L' D R D L2 F B U2 L' R B' R' U' F // scramble
```

Skips: inverse: M slice on U/D, oriented.

Each row is one route to a DR-xs on this scramble, shortest first; the last column is how far that DR-xs is from a real DR.

| # | Route | Length, moves | Kind | Starts from | Corner subset | Fewest turns to a real DR |
|---:|---|---:|---|---|---|---:|
| 1 | `(R B' U2 B D2 L2 F' U')` | 8 | DR-1s | one-move slice EO: E slice on R/L, misoriented | 2c3 | 6 |
| 2 | `(D2 F' L F' R' B U2 L')` | 8 | DR-1s | skip: M slice on U/D, oriented | 2c4 | 4 |
| 3 | `(R B' U2 B D2 L2 F' U)` | 8 | DR-1s | one-move slice EO: E slice on R/L, misoriented | 2c3 | 6 |
| 4 | `(D2 F' L F' R' B U2 L)` | 8 | DR-1s | skip: M slice on U/D, oriented | 2c4 | 5 |
| 5 | `(R U2 F L R2 B' U2 L)` | 8 | DR-1s | skip: M slice on U/D, oriented | 4a3 | 5 |
| 6 | `(F2 R' B L2 U2 D2 L B)` | 8 | DR-1s | skip: M slice on U/D, oriented | 4a4 | 5 |
| 7 | `(R U2 B' R2 D' F' U R2 F)` | 9 | DR-2s 8fe | one-move slice EO: E slice on R/L, misoriented | 4b4 | 4 |
| 8 | `(R U2 B' R2 D' F' U R2 F')` | 9 | DR-2s 8fe | one-move slice EO: E slice on R/L, misoriented | 4b4 | 4 |

Shown: 6 of the 10 DR-1s of 8 or less and 2 of the 2 DR-2s 8fe of 9 or less. Shortest normal DR: 9 moves.

<details>
<summary>Answers for scramble 85</summary>

Each row is the route with the same number above: the best finish of the method's form from it, then the whole solution written out for the scramble.

| # | Finish, moves | Solution | Solution length, moves |
|---:|---:|---|---:|
| 1 | 15 | `D L2 D' R' L' B U2 B L2 D2 L2 D2 B L2 U' F L2 D2 B' U2 B R'` | 22 |
| 2 | 16 | `F2 B2 R' D2 R U2 L' F2 D2 L' U2 L F' B' D R2 L U2 B' R F L' F D2` | 24 |
| 3 | 14 | `D L2 D' R' L' B U2 B L2 D2 L2 D2 B L2 U' F L2 D2 B' U2 B R'` | 22 |
| 4 | 16 | `R2 U2 R F B' D2 L2 B2 L2 F2 U' F2 D L2 D' B2 L' U2 B' R F L' F D2` | 24 |
| 5 | 14 | `L' U2 R' F B L2 U2 F2 R2 U' B2 D F2 U L' U2 B R2 L' F' U2 R'` | 22 |
| 6 | 17 | `R U2 R2 L F2 L D2 F2 D2 L' F' B' D' B2 L2 U L2 B' L' U2 D2 L2 B' R F2` | 25 |
| 7 | 16 | `L2 F2 B2 U L2 U B2 U2 R2 D' B2 D' R L U' D F' R2 U' F D R2 B U2 R'` | 25 |
| 8 | 16 | `R L' U' D' L U2 L F2 L D2 L' B2 D2 R' D2 R' F R2 U' F D R2 B U2 R'` | 25 |

Best of these: **22**, longer than the best through a normal DR of 10 or less. Normal DRs on this scramble: 21 through one of 10 or less, 18 through 11 or less, 18 through 12 or less.

</details>

#### Scramble 86

```
R' U' F R2 D' R2 U B2 D U2 B2 L2 U' L B' L D2 F2 R' U L2 B D R' U' F // scramble
```

Skips: normal: S slice on F/B, oriented.

Each row is one route to a DR-xs on this scramble, shortest first; the last column is how far that DR-xs is from a real DR.

| # | Route | Length, moves | Kind | Starts from | Corner subset | Fewest turns to a real DR |
|---:|---|---:|---|---|---|---:|
| 1 | `(F' B2 D2 L2 U L B2 D')` | 8 | DR-1s | one-move slice EO: E slice on F/B, oriented | 2c5 | 6 |
| 2 | `(F' B2 D F2 U2 R' B2 U)` | 8 | DR-1s | one-move slice EO: E slice on F/B, oriented | 4b5 | 5 |
| 3 | `L2 U' L2 F2 L F2 U' R'` | 8 | DR-1s | skip: S slice on F/B, oriented | 2c3 | 5 |
| 4 | `(F' B2 D2 L2 U L B2 D)` | 8 | DR-1s | one-move slice EO: E slice on F/B, oriented | 2c5 | 6 |
| 5 | `(F' B2 D B2 D2 L F2 U')` | 8 | DR-1s | one-move slice EO: E slice on F/B, oriented | 4b5 | 5 |
| 6 | `(F' B2 D F2 U2 R' B2 U')` | 8 | DR-1s | one-move slice EO: E slice on F/B, oriented | 4b5 | 6 |
| 7 | `(L2 F D' R' D2 R2 B2 U' R)` | 9 | DR-2s 8fe | EO on F/B | 2c4 | 4 |
| 8 | `(L2 F' L U B2 U D' B2 L')` | 9 | DR-2s 8fe | EO on F/B | 4b3 | 4 |

Shown: 6 of the 16 DR-1s of 8 or less and 2 of the 20 DR-2s 8fe of 9 or less. Shortest normal DR: 8 moves.

<details>
<summary>Answers for scramble 86</summary>

Each row is the route with the same number above: the best finish of the method's form from it, then the whole solution written out for the scramble.

| # | Finish, moves | Solution | Solution length, moves |
|---:|---:|---|---:|
| 1 | 17 | `R2 U' B2 U' B2 R L B' U2 B' U2 B2 R2 U2 B D2 F2 D B2 L' U' L2 D2 F B2` | 25 |
| 2 | 16 | `D' F2 D' L2 F2 L2 B2 U' R' L' B L2 B D2 L2 F2 U' B2 R U2 F2 D' F B2` | 24 |
| 3 | 15 | `L2 U' L2 F2 L F2 U' R' U L2 U' F2 L2 U' L2 D' R2 F2 R' L' D2 F L2` | 23 |
| 4 | 16 | `U F2 D F2 U F2 B2 R' L' F2 D2 B' D2 B D2 B2 D' B2 L' U' L2 D2 F B2` | 24 |
| 5 | 16 | `U' L2 D R L F2 L2 D2 F D2 L2 D2 R2 F' D2 B U F2 L' D2 B2 D' F B2` | 24 |
| 6 | 17 | `D' F2 D' L2 F2 L2 B2 U' R' L' B L2 B D2 L2 F2 U' B2 R U2 F2 D' F B2` | 24 |
| 7 | 16 | `L F2 L' U2 D2 L' B2 L' F2 L' U2 L U' D' L U B2 R2 D2 R D F' L2` | 23 |
| 8 | 14 | `L' D2 L2 B2 L B2 R' U' D' R' L' U2 F2 U2 L B2 U' D B2 U' L' F L2` | 23 |

Best of these: **23**, longer than the best through a normal DR of 10 or less. Normal DRs on this scramble: 18 through one of 10 or less, 18 through 11 or less, 18 through 12 or less.

</details>

#### Scramble 87

```
R' U' F R2 U2 F2 D2 U L2 U2 B2 U' L2 F L2 U' F' R' U' B2 F L' B' U R' U' F // scramble
```

Skips: none.

Each row is one route to a DR-xs on this scramble, shortest first; the last column is how far that DR-xs is from a real DR.

| # | Route | Length, moves | Kind | Starts from | Corner subset | Fewest turns to a real DR |
|---:|---|---:|---|---|---|---:|
| 1 | `U' R U2 L' B' F2 R'` | 7 | DR-1s | one-move slice EO: M slice on U/D, oriented | 2c4 | 4 |
| 2 | `U' R U2 L' B' F2 R` | 7 | DR-1s | one-move slice EO: M slice on U/D, oriented | 2c4 | 5 |
| 3 | `(F' U2 R U' L2 D U2 R')` | 8 | DR-1s | one-move slice EO: S slice on F/B, oriented | 4a4 | 5 |
| 4 | `(D B' D2 F' L B2 F' L')` | 8 | DR-1s | one-move slice EO: M slice on U/D, misoriented | 2c3 | 6 |
| 5 | `U U2 R U2 L' B' F2 R` | 8 | DR-1s | one-move slice EO: M slice on U/D, oriented | 2c4 | 5 |
| 6 | `(F' U2 R D2 U R2 D' R')` | 8 | DR-1s | one-move slice EO: S slice on F/B, oriented | 4a4 | 6 |
| 7 | `(D B2 L' F U2 R F' L B)` | 9 | DR-2s 8fe | one-move slice EO: M slice on U/D, misoriented | 4b4 | 4 |
| 8 | `(D B2 L' F U2 R F' L B')` | 9 | DR-2s 8fe | one-move slice EO: M slice on U/D, misoriented | 4b4 | 4 |

Shown: 6 of the 12 DR-1s of 8 or less and 2 of the 2 DR-2s 8fe of 9 or less. Shortest normal DR: 10 moves.

<details>
<summary>Answers for scramble 87</summary>

Each row is the route with the same number above: the best finish of the method's form from it, then the whole solution written out for the scramble.

| # | Finish, moves | Solution | Solution length, moves |
|---:|---:|---|---:|
| 1 | 16 | `U' R U2 L' F2 B' R' U' L2 U' B2 D2 B2 D F2 U B2 L2 U R2 F' B' R'` | 23 |
| 2 | 15 | `U' R U2 L' F2 B' R B2 D R2 D' B2 U R2 U B2 U2 R2 D' F B R` | 22 |
| 3 | 16 | `U2 L2 F R' L U2 B2 U L2 U2 B2 D' R2 B2 D' R L2 U2 D' L2 U R' U2 F` | 24 |
| 4 | 15 | `R2 L2 D2 R' U' D L2 B U2 F' B' U2 L2 B L' F B2 L' F D2 B D'` | 22 |
| 5 | 15 | `U' R U2 L' F2 B' R B2 D R2 D' B2 U R2 U B2 U2 R2 D' F B R` | 22 |
| 6 | 18 | `U2 L2 F' U2 R' L U F2 U2 F2 R2 D F2 U B2 L2 F2 R L2 D R2 U' D2 R' U2 F` | 26 |
| 7 | 16 | `D2 L U' D R' L' F2 U R2 D2 B2 D' R2 B2 D R2 B' L' F R' U2 F' L B2 D'` | 25 |
| 8 | 16 | `L' U2 F2 L U2 L F2 R' F2 L U D' R' L' D' L2 B L' F R' U2 F' L B2 D'` | 25 |

Best of these: **22**, shorter than every normal DR of 10 or less gives. Normal DRs on this scramble: 23 through one of 10 or less, 20 through 11 or less, 20 through 12 or less.

</details>

#### Scramble 88

```
R' U' F D R2 U2 L2 D R2 F2 U' R2 F2 B' R F' B L U' L2 R' B2 U' R' U R' U' F // scramble
```

Skips: normal: E slice on R/L, oriented; inverse: M slice on F/B, misoriented.

Each row is one route to a DR-xs on this scramble, shortest first; the last column is how far that DR-xs is from a real DR.

| # | Route | Length, moves | Kind | Starts from | Corner subset | Fewest turns to a real DR |
|---:|---|---:|---|---|---|---:|
| 1 | `U F' L' B R` | 5 | DR-1s | one-move slice EO: M slice on U/D, oriented | 4b4 | 6 |
| 2 | `U F' L' B R'` | 5 | DR-1s | one-move slice EO: M slice on U/D, oriented | 4b4 | 6 |
| 3 | `U F' U2 R' F L'` | 6 | DR-1s | one-move slice EO: M slice on U/D, oriented | 4a4 | 6 |
| 4 | `U D2 F' L' B R` | 6 | DR-1s | one-move slice EO: M slice on U/D, oriented | 2c4 | 6 |
| 5 | `U F' L' B L2 R` | 6 | DR-1s | one-move slice EO: M slice on U/D, oriented | 4b4 | 5 |
| 6 | `U D2 F' L' B R'` | 6 | DR-1s | one-move slice EO: M slice on U/D, oriented | 2c4 | 6 |
| 7 | `(R2 F2 R' D F' L' D2 L')` | 8 | DR-2s 8fe | EO on U/D | 2c4 | 4 |
| 8 | `D R' F2 U2 D2 B R F'` | 8 | DR-2s 8fe | one-move slice EO: M slice on U/D, misoriented | 4b4 | 4 |

Shown: 6 of the 396 DR-1s of 8 or less and 2 of the 70 DR-2s 8fe of 9 or less. Shortest normal DR: 8 moves.

<details>
<summary>Answers for scramble 88</summary>

Each row is the route with the same number above: the best finish of the method's form from it, then the whole solution written out for the scramble.

| # | Finish, moves | Solution | Solution length, moves |
|---:|---:|---|---:|
| 1 | 17 | `U F' L' B R U F2 D' F2 U F B R' D2 R F2 R' B2 U2 L2 F2 U2` | 22 |
| 2 | 16 | `U F' L' B R' U F2 D L2 U' B2 L2 U F B R2 D2 R B2 L F2` | 21 |
| 3 | 16 | `U F' U2 R' F L' F2 U' R2 D' B2 D L2 B2 U L2 U F' B' D2 L' F2` | 22 |
| 4 | 16 | `U D2 F' L' B R U' B2 R2 U' L2 U F2 L2 D' F B L D2 R' F2 L2` | 22 |
| 5 | 16 | `U F' L' B R L2 U' R2 D B2 L2 D' F' B R' D2 R U2 F2 R' D2 B2` | 22 |
| 6 | 17 | `U D2 F' L' B R' U' R2 D R2 U' F B' D2 R2 L F2 R2 U2 R D2 L D2` | 23 |
| 7 | 16 | `B2 R B2 R' F2 U2 R' D2 L2 B2 D2 F2 L F B' R' D2 L F D' R F2 R2` | 23 |
| 8 | 15 | `D R' F2 U2 D2 B R F' D' B2 D B2 D' R2 F2 U' B2 D' R' L' U' D L'` | 23 |

Best of these: **21**, as short as the best through a normal DR of 10 or less. Normal DRs on this scramble: 21 through one of 10 or less, 19 through 11 or less, 19 through 12 or less.

</details>

#### Scramble 89

```
R' U' F D' L2 U' B2 U2 B2 U' F2 D' U' R' D2 U F R B' R' B2 R D L2 U R' U' F // scramble
```

Skips: normal: E slice on F/B, misoriented; normal: S slice on U/D, misoriented; inverse: E slice on F/B, misoriented; inverse: S slice on U/D, misoriented.

Each row is one route to a DR-xs on this scramble, shortest first; the last column is how far that DR-xs is from a real DR.

| # | Route | Length, moves | Kind | Starts from | Corner subset | Fewest turns to a real DR |
|---:|---|---:|---|---|---|---:|
| 1 | `(B L U2 L' R2 B2 U R)` | 8 | DR-1s | one-move slice EO: M slice on F/B, oriented | 4b5 | 6 |
| 2 | `R2 U2 R' D R' F2 R U'` | 8 | DR-1s | skip: E slice on F/B, misoriented | 2c3 | 5 |
| 3 | `B2 U' B2 D' R' L' B2 U'` | 8 | DR-1s | skip: E slice on F/B, misoriented | 4a3 | 6 |
| 4 | `(L B2 R U' R' D' L D)` | 8 | DR-1s | skip: E slice on F/B, misoriented | 2c3 | 5 |
| 5 | `D R D' F2 U2 D2 R' D'` | 8 | DR-1s | skip: E slice on F/B, misoriented | 2c3 | 5 |
| 6 | `(U R2 L D' B2 U2 L U)` | 8 | DR-1s | skip: E slice on F/B, misoriented | 2c3 | 6 |
| 7 | `(U R L2 U2 F2 R2 D' R)` | 8 | DR-2s 8fe | skip: E slice on F/B, misoriented | 4b2 | 4 |
| 8 | `(L2 B2 D' L2 D' F2 U' L)` | 8 | DR-2s 8fe | skip: E slice on F/B, misoriented | 4b4 | 4 |

Shown: 6 of the 38 DR-1s of 8 or less and 2 of the 50 DR-2s 8fe of 9 or less. Shortest normal DR: 10 moves.

<details>
<summary>Answers for scramble 89</summary>

Each row is the route with the same number above: the best finish of the method's form from it, then the whole solution written out for the scramble.

| # | Finish, moves | Solution | Solution length, moves |
|---:|---:|---|---:|
| 1 | 18 | `F2 R2 L' F2 U2 F2 U2 L D2 L' F2 L U D F U2 L2 F2 R' U' B2 R2 L U2 L' B'` | 26 |
| 2 | 15 | `R2 U2 R' D R' F2 R U' B2 U2 L' F2 L' D2 L2 F' B D L2 U2 R2 B2 U2` | 23 |
| 3 | 16 | `B2 U' B2 D' R' L' B2 U' L' F2 L2 D2 L F B' L2 U R2 U2 L2 F2 R2 U2 F2` | 24 |
| 4 | 15 | `L2 F2 U2 R2 F2 U R2 L2 F B L B2 R' L2 D L' D R U R' B2 L'` | 22 |
| 5 | 13 | `D R D' F2 U2 D2 R' D' F2 R' B2 L' D2 F' B' U F2 U2 R2 F2 B2` | 21 |
| 6 | 17 | `R2 U2 B2 D' R2 U' L2 U' F2 R2 D F' B R B2 R2 U L' U2 B2 D R2 L' U'` | 24 |
| 7 | 14 | `D R2 U F2 L2 U2 B2 D' B2 U F B' U' D R' D R2 F2 U2 R' L2 U'` | 22 |
| 8 | 16 | `U F2 D B2 D2 L2 D' B2 U' R2 U2 L2 F B U' D L' U F2 D L2 D B2 L2` | 24 |

Best of these: **21**, as short as the best through a normal DR of 10 or less. Normal DRs on this scramble: 21 through one of 10 or less, 20 through 11 or less, 19 through 12 or less.

</details>

#### Scramble 90

```
R' U' F U' B2 D' L2 B2 D' B2 U B2 U' L U F2 U L U' B' R' D L U2 R' U' F // scramble
```

Skips: none.

Each row is one route to a DR-xs on this scramble, shortest first; the last column is how far that DR-xs is from a real DR.

| # | Route | Length, moves | Kind | Starts from | Corner subset | Fewest turns to a real DR |
|---:|---|---:|---|---|---|---:|
| 1 | `B' R2 U2 F2 D' L B2 L` | 8 | DR-1s | one-move slice EO: E slice on F/B, oriented | 4b2 | 5 |
| 2 | `B' R2 U2 F2 D' R D2 R'` | 8 | DR-1s | one-move slice EO: E slice on F/B, oriented | 4b2 | 6 |
| 3 | `B' R2 U2 F2 D' L B2 L'` | 8 | DR-1s | one-move slice EO: E slice on F/B, oriented | 4b2 | 5 |
| 4 | `F U2 F2 U F2 U B2 R'` | 8 | DR-1s | one-move slice EO: M slice on F/B, oriented | 2c4 | 5 |
| 5 | `F U2 F2 U F2 U B2 R` | 8 | DR-1s | one-move slice EO: M slice on F/B, oriented | 2c4 | 4 |
| 6 | `F D2 B2 U B2 U F2 L` | 8 | DR-1s | one-move slice EO: M slice on F/B, oriented | 2c4 | 5 |

Shown: 6 of the 8 DR-1s of 8 or less and 0 of the 0 DR-2s 8fe of 9 or less. Shortest normal DR: 9 moves.

<details>
<summary>Answers for scramble 90</summary>

Each row is the route with the same number above: the best finish of the method's form from it, then the whole solution written out for the scramble.

| # | Finish, moves | Solution | Solution length, moves |
|---:|---:|---|---:|
| 1 | 13 | `B' R2 U2 F2 D' L B2 L F2 L2 U2 F' L2 B' U2 D2 R L' D' B2 D` | 21 |
| 2 | 15 | `B' R2 U2 F2 D' R D2 R' L2 B2 D2 F D2 B' U2 R' L' B2 U F2 R2 L2 D` | 23 |
| 3 | 14 | `B' R2 U2 F2 D' L B2 L' B' R2 F R' L U' F2 D R2 D2 F2 U' F2 D'` | 22 |
| 4 | 16 | `F U2 F2 U F2 U B2 R' F2 D2 L2 U2 B' U2 B' D2 L2 B' U D R' F2 U2 R2` | 24 |
| 5 | 17 | `F U2 F2 U F2 U B2 R' F2 D2 L2 U2 B' U2 B' D2 L2 B' U D R' F2 U2 R2` | 24 |
| 6 | 16 | `F D2 B2 U B2 U F2 L U2 R2 F' U' D' L2 F2 L F2 U2 R F2 B2 R2 F2 L` | 24 |

Best of these: **21**, longer than the best through a normal DR of 10 or less. Normal DRs on this scramble: 20 through one of 10 or less, 20 through 11 or less, 20 through 12 or less.

</details>

#### Scramble 91

```
R' U' F R' F R' U B' U2 F D' F2 B L' U D L2 B2 R2 D2 F2 U' R2 B2 R' U' F // scramble
```

Skips: normal: E slice on R/L, oriented; normal: M slice on R/L, oriented; inverse: E slice on R/L, oriented; inverse: S slice on U/D, misoriented; inverse: S slice on R/L, oriented.

Each row is one route to a DR-xs on this scramble, shortest first; the last column is how far that DR-xs is from a real DR.

| # | Route | Length, moves | Kind | Starts from | Corner subset | Fewest turns to a real DR |
|---:|---|---:|---|---|---|---:|
| 1 | `(U' D2 L F' R U2 B' L')` | 8 | DR-1s | one-move slice EO: E slice on U/D, oriented | 4b2 | 4 |
| 2 | `F' L2 R U' L2 U D' R` | 8 | DR-1s | one-move slice EO: M slice on F/B, oriented | 2c4 | 5 |
| 3 | `(D' F2 U' B' R2 D2 F' U)` | 8 | DR-1s | skip: S slice on R/L, oriented | 4b5 | 6 |
| 4 | `(F' D' F L2 U D F U')` | 8 | DR-1s | skip: S slice on R/L, oriented | 2c3 | 5 |
| 5 | `(U2 B' L2 D R2 B' U2 F)` | 8 | DR-1s | skip: S slice on R/L, oriented | 2c4 | 5 |
| 6 | `R2 B D2 F2 D' L2 B' D'` | 8 | DR-1s | skip: E slice on R/L, oriented | 4b2 | 5 |
| 7 | `D L B L F B' R2 U' F'` | 9 | DR-2s 8fe | EO on R/L | 2c4 | 4 |
| 8 | `F L' R2 B U' L R U' L` | 9 | DR-2s 8fe | EO on F/B | 4a4 | 4 |

Shown: 6 of the 36 DR-1s of 8 or less and 2 of the 4 DR-2s 8fe of 9 or less. Shortest normal DR: 9 moves.

<details>
<summary>Answers for scramble 91</summary>

Each row is the route with the same number above: the best finish of the method's form from it, then the whole solution written out for the scramble.

| # | Finish, moves | Solution | Solution length, moves |
|---:|---:|---|---:|
| 1 | 14 | `U2 L2 U2 L2 D F2 L2 D' R L F B' R2 D2 L B U2 R' F L' U D2` | 22 |
| 2 | 16 | `F' R L2 U' L2 U D' R' F' R2 B D2 F U' D L2 U2 R U2 L U2 D2 R` | 23 |
| 3 | 17 | `B U2 R2 L2 F' D2 B2 R2 F D2 F2 U D' L' U2 L' U F D2 R2 B U F2 D` | 24 |
| 4 | 16 | `L2 F L2 F D2 B U D F2 R' U2 D2 F2 R2 L' U' F' U' D' L2 F' D F` | 23 |
| 5 | 17 | `R2 F' D2 B' R2 B' D2 R2 L2 F' R2 F2 U' D' R F2 R F' U2 B R2 D' L2 B U2` | 25 |
| 6 | 15 | `R2 B D2 F2 D' L2 B' D' R' U2 D2 F2 D2 L' F2 R2 B2 U2 L U2 F' B U'` | 23 |
| 7 | 15 | `D L B L F B' R2 U' F' D' F' B' U D F2 U2 F' L2 D2 B' U2 B R2 F2` | 24 |
| 8 | 16 | `F R2 L' B U' R L U' L U B2 U' R L U' D R F2 R' B2 R B2 L B2 L2` | 25 |

Best of these: **22**, longer than the best through a normal DR of 10 or less. Normal DRs on this scramble: 21 through one of 10 or less, 21 through 11 or less, 20 through 12 or less.

</details>

#### Scramble 92

```
R' U' F D2 L2 R2 D L2 D2 R2 F2 R2 U' F D' R U R' U2 L D U2 B F2 U' R' U' F // scramble
```

Skips: inverse: S slice on F/B, oriented.

Each row is one route to a DR-xs on this scramble, shortest first; the last column is how far that DR-xs is from a real DR.

| # | Route | Length, moves | Kind | Starts from | Corner subset | Fewest turns to a real DR |
|---:|---|---:|---|---|---|---:|
| 1 | `(D' L' D R' D2 U' L U)` | 8 | DR-1s | skip: S slice on F/B, oriented | 4b4 | 4 |
| 2 | `(B2 L2 U F2 R D' R' U')` | 8 | DR-1s | skip: S slice on F/B, oriented | 2c4 | 5 |
| 3 | `(B2 L2 U F2 R D' R' U)` | 8 | DR-1s | skip: S slice on F/B, oriented | 2c4 | 6 |
| 4 | `(D' L' D R D2 U' L U)` | 8 | DR-1s | skip: S slice on F/B, oriented | 4b4 | 6 |
| 5 | `L B' D2 L2 D B' F2 D'` | 8 | DR-1s | one-move slice EO: E slice on R/L, oriented | 4b2 | 6 |
| 6 | `L B' D2 L2 D B' F2 D` | 8 | DR-1s | one-move slice EO: E slice on R/L, oriented | 4b2 | 6 |

Shown: 6 of the 12 DR-1s of 8 or less and 0 of the 0 DR-2s 8fe of 9 or less. Shortest normal DR: 8 moves.

<details>
<summary>Answers for scramble 92</summary>

Each row is the route with the same number above: the best finish of the method's form from it, then the whole solution written out for the scramble.

| # | Finish, moves | Solution | Solution length, moves |
|---:|---:|---|---:|
| 1 | 18 | `R2 F L2 D2 F U2 F D2 F' R2 F L2 U D L' F2 D2 B2 U' L' U D2 R D' L D` | 26 |
| 2 | 17 | `B L2 F' D2 B U' D' L F2 L2 U2 L' B2 U2 D2 R' B2 U R D R' F2 U' L2 B2` | 25 |
| 3 | 17 | `F R2 F2 B' R2 F2 L2 F' D2 F' U' D' R U2 R' U2 B2 U' R D R' F2 U' L2 B2` | 25 |
| 4 | 17 | `R2 B R2 F' U' D' L2 F2 L' B2 D2 L U2 F2 R U2 R' U' L' U D2 R' D' L D` | 25 |
| 5 | 15 | `L B' D2 L2 D F2 B' D' R F2 L F2 D2 R' F B D B2 L2 F2 L2 U2 B2` | 23 |
| 6 | 15 | `L B' D2 L2 D F2 B' D R2 U2 F2 L U2 F' B' U L2 U R2 D' B2 U2 F2` | 23 |

Best of these: **23**, longer than the best through a normal DR of 10 or less. Normal DRs on this scramble: 19 through one of 10 or less, 19 through 11 or less, 19 through 12 or less.

</details>

#### Scramble 93

```
R' U' F L2 F2 L2 U2 B2 D2 B2 D F2 U' L F2 U' B L' B' R2 U' F' R B' U R' U' F // scramble
```

Skips: none.

Each row is one route to a DR-xs on this scramble, shortest first; the last column is how far that DR-xs is from a real DR.

| # | Route | Length, moves | Kind | Starts from | Corner subset | Fewest turns to a real DR |
|---:|---|---:|---|---|---|---:|
| 1 | `R F' D B L2 F' U` | 7 | DR-1s | one-move slice EO: S slice on R/L, oriented | 2c4 | 6 |
| 2 | `R F' D B L2 F' U'` | 7 | DR-1s | one-move slice EO: S slice on R/L, oriented | 2c4 | 6 |
| 3 | `L' F' R2 U2 B' D2 F D` | 8 | DR-1s | one-move slice EO: E slice on R/L, misoriented | 2c3 | 6 |
| 4 | `R' D' R2 F2 U' B2 D F` | 8 | DR-1s | one-move slice EO: E slice on R/L, oriented | 2c3 | 6 |
| 5 | `L' B' F' R2 B' U2 B D'` | 8 | DR-1s | one-move slice EO: E slice on R/L, misoriented | 2c4 | 6 |
| 6 | `R' R2 F' D B L2 F' U` | 8 | DR-1s | one-move slice EO: S slice on R/L, oriented | 2c4 | 6 |

Shown: 6 of the 22 DR-1s of 8 or less and 0 of the 0 DR-2s 8fe of 9 or less. Shortest normal DR: 10 moves.

<details>
<summary>Answers for scramble 93</summary>

Each row is the route with the same number above: the best finish of the method's form from it, then the whole solution written out for the scramble.

| # | Finish, moves | Solution | Solution length, moves |
|---:|---:|---|---:|
| 1 | 17 | `R F' D B L2 F' U B2 R D2 R' U' D' F U2 F2 R2 F2 L2 D2 R2 B R2 B2` | 24 |
| 2 | 16 | `R F' D B L2 F' U' F2 R U2 R' F2 L U D R2 F2 R2 F' R2 B' R2 F` | 23 |
| 3 | 16 | `L' F' R2 U2 B' D2 F D' R2 B' L2 U2 D2 B R2 D2 B2 U2 R' L' U' B2 D2` | 23 |
| 4 | 15 | `R' D' R2 F2 U' B2 D F R' U2 R U2 R' F' B D' F2 U2 D L2 D2 R2 F2` | 23 |
| 5 | 16 | `L' F' B' R2 B' U2 B D' B2 D2 F U2 F2 L2 F R2 B' U2 B2 R' L U' F2 U2` | 24 |
| 6 | 17 | `R F' D B L2 F' U B2 R D2 R' U' D' F U2 F2 R2 F2 L2 D2 R2 B R2 B2` | 24 |

Best of these: **23**, longer than the best through a normal DR of 10 or less. Normal DRs on this scramble: 21 through one of 10 or less, 20 through 11 or less, 20 through 12 or less.

</details>

#### Scramble 94

```
R' U' F U' B2 D F2 D' L2 D L2 F2 U' B' D2 L B2 U' L' U' B' R' D' R' U' F // scramble
```

Skips: normal: E slice on U/D, misoriented; normal: M slice on R/L, oriented; normal: M slice on F/B, oriented; normal: S slice on R/L, misoriented; inverse: E slice on R/L, misoriented; inverse: M slice on F/B, oriented; inverse: S slice on U/D, misoriented.

Each row is one route to a DR-xs on this scramble, shortest first; the last column is how far that DR-xs is from a real DR.

| # | Route | Length, moves | Kind | Starts from | Corner subset | Fewest turns to a real DR |
|---:|---|---:|---|---|---|---:|
| 1 | `(U' L' D' L2 F2 U R' U)` | 8 | DR-1s | skip: M slice on F/B, oriented | 4b5 | 6 |
| 2 | `(U' L' D' R2 B2 D R' D)` | 8 | DR-1s | skip: M slice on F/B, oriented | 4b5 | 5 |
| 3 | `(U' L' U' F2 R2 D L' U')` | 8 | DR-1s | skip: M slice on F/B, oriented | 4b5 | 5 |
| 4 | `(U' L B2 L2 U D L' U)` | 8 | DR-1s | skip: M slice on F/B, oriented | 4b5 | 6 |
| 5 | `(U' L' U' B2 L2 U R' D')` | 8 | DR-1s | skip: M slice on F/B, oriented | 4b5 | 6 |
| 6 | `(U' L' D' L2 F2 U R' U')` | 8 | DR-1s | skip: M slice on F/B, oriented | 4b5 | 5 |

Shown: 6 of the 20 DR-1s of 8 or less and 0 of the 0 DR-2s 8fe of 9 or less. Shortest normal DR: 10 moves.

<details>
<summary>Answers for scramble 94</summary>

Each row is the route with the same number above: the best finish of the method's form from it, then the whole solution written out for the scramble.

| # | Finish, moves | Solution | Solution length, moves |
|---:|---:|---|---:|
| 1 | 17 | `B2 R' D2 L2 F2 R' U2 B2 R D2 R2 U' D' F' R2 D2 B U' R U' F2 L2 D L U` | 25 |
| 2 | 16 | `F2 D2 R U D F2 L2 F' R2 F' L2 F D2 B L2 U2 D' R D' B2 R2 D L U` | 24 |
| 3 | 16 | `F2 L' B2 R' U' D' F2 D2 F D2 L2 F' D2 B U2 B2 U L D' R2 F2 U L U` | 24 |
| 4 | 16 | `R U2 B2 L' U2 R U' D' F' R2 D2 F2 D2 B' R2 L2 U' L U' D' L2 B2 L' U` | 24 |
| 5 | 16 | `F2 U2 R U2 D2 F2 R B2 U' D' B D2 F' L2 B' U2 D R U' L2 B2 U L U` | 24 |
| 6 | 17 | `L F2 U2 L U2 L' F2 R2 D2 L B2 U' D' F U2 F' B' U R U' F2 L2 D L U` | 25 |

Best of these: **24**, longer than the best through a normal DR of 10 or less. Normal DRs on this scramble: 21 through one of 10 or less, 21 through 11 or less, 21 through 12 or less.

</details>

#### Scramble 95

```
R' U' F R2 U2 R2 B2 U' B2 L2 D R2 U' F D R' D L R F2 U' B' D2 U R' U' F // scramble
```

Skips: inverse: S slice on U/D, misoriented.

Each row is one route to a DR-xs on this scramble, shortest first; the last column is how far that DR-xs is from a real DR.

| # | Route | Length, moves | Kind | Starts from | Corner subset | Fewest turns to a real DR |
|---:|---|---:|---|---|---|---:|
| 1 | `(F2 R F B L2 D2 R' F)` | 8 | DR-1s | skip: S slice on U/D, misoriented | 2c3 | 6 |
| 2 | `(F' L B R L2 B D2 F)` | 8 | DR-1s | skip: S slice on U/D, misoriented | 4b4 | 5 |
| 3 | `(F2 R F B R2 U2 R' B)` | 8 | DR-1s | skip: S slice on U/D, misoriented | 2c3 | 6 |
| 4 | `(F2 R F B R2 U2 R' B')` | 8 | DR-1s | skip: S slice on U/D, misoriented | 2c3 | 6 |
| 5 | `(R' L D2 F B U2 R' B)` | 8 | DR-1s | skip: S slice on U/D, misoriented | 4b2 | 6 |
| 6 | `(F' L B R L2 F L2 B')` | 8 | DR-1s | skip: S slice on U/D, misoriented | 4b4 | 5 |
| 7 | `(F' L B' R B D2 B2 L' B)` | 9 | DR-2s 8fe | skip: S slice on U/D, misoriented | 2c3 | 4 |
| 8 | `(F' B' R B L D2 B2 L' B)` | 9 | DR-2s 8fe | skip: S slice on U/D, misoriented | 2c5 | 4 |

Shown: 6 of the 22 DR-1s of 8 or less and 2 of the 12 DR-2s 8fe of 9 or less. Shortest normal DR: 9 moves.

<details>
<summary>Answers for scramble 95</summary>

Each row is the route with the same number above: the best finish of the method's form from it, then the whole solution written out for the scramble.

| # | Finish, moves | Solution | Solution length, moves |
|---:|---:|---|---:|
| 1 | 15 | `R2 U2 F' L2 D2 F2 R2 F' R2 U D' R B2 U2 R2 F' R D2 L2 F' B' R' F2` | 23 |
| 2 | 16 | `L2 U2 L2 D2 F B2 U' D' R' U2 L2 B2 L F2 R F' B2 D2 B' R' L2 B' L' F` | 24 |
| 3 | 15 | `U2 F2 U2 L2 F D2 L2 F' U D B2 L U2 B2 R2 B' R U2 R2 F' B' R' F2` | 23 |
| 4 | 16 | `B R2 L2 B' U' D' L2 B2 R' B2 L F2 R' B2 R2 U2 B R U2 R2 F' B' R' F2` | 24 |
| 5 | 16 | `F' U2 D2 F' U D' R2 F2 R2 F2 D2 R D2 R' F2 B R U2 F' B' D2 R L'` | 23 |
| 6 | 16 | `L2 U2 L2 D2 F' L2 U' D' L U2 B2 R2 B2 L F2 R B L2 F' R' L2 B' L' F` | 24 |
| 7 | 14 | `U2 B' L2 U' D F B' U' R2 D L2 U2 R2 L2 B' L B2 D2 B' R' B L' F` | 23 |
| 8 | 17 | `R2 U2 F' L2 F L2 F' D2 F U2 B' L2 D2 F2 U' D F' L B2 D2 L' B' R' F B` | 25 |

Best of these: **23**, longer than the best through a normal DR of 10 or less. Normal DRs on this scramble: 22 through one of 10 or less, 20 through 11 or less, 20 through 12 or less.

</details>

#### Scramble 96

```
R' U' F U2 L2 D B2 F2 R2 D' F2 U F2 L' U2 L2 D' R2 U2 F U2 B' D' F2 R' U' F // scramble
```

Skips: normal: S slice on F/B, misoriented; inverse: E slice on U/D, misoriented.

Each row is one route to a DR-xs on this scramble, shortest first; the last column is how far that DR-xs is from a real DR.

| # | Route | Length, moves | Kind | Starts from | Corner subset | Fewest turns to a real DR |
|---:|---|---:|---|---|---|---:|
| 1 | `U' R2 U2 B D2 B U2 R` | 8 | DR-1s | one-move slice EO: M slice on U/D, misoriented | 2c4 | 5 |
| 2 | `U' R2 U2 B D2 B U2 R'` | 8 | DR-1s | one-move slice EO: M slice on U/D, misoriented | 2c4 | 6 |
| 3 | `U R F' R' B L B L` | 8 | DR-1s | one-move slice EO: M slice on U/D, misoriented | 2c4 | 6 |
| 4 | `U R F' R' B L B L'` | 8 | DR-1s | one-move slice EO: M slice on U/D, misoriented | 2c4 | 6 |

Shown: 4 of the 4 DR-1s of 8 or less and 0 of the 0 DR-2s 8fe of 9 or less. Shortest normal DR: 10 moves.

<details>
<summary>Answers for scramble 96</summary>

Each row is the route with the same number above: the best finish of the method's form from it, then the whole solution written out for the scramble.

| # | Finish, moves | Solution | Solution length, moves |
|---:|---:|---|---:|
| 1 | 15 | `U' R2 U2 B D2 B U2 R B' D2 F U' D R D2 L' U2 B2 L F2 R B2 L2` | 23 |
| 2 | 16 | `U' R2 U2 B D2 B U2 R B' D2 F U' D R D2 L' U2 B2 L F2 R B2 L2` | 23 |
| 3 | 17 | `U R F' R' B L B L B2 R2 U2 B' U' D' L F2 L' B2 L U2 D2 L' F2 R' F2` | 25 |
| 4 | 16 | `U R F' R' B L B L' F R2 B2 R2 D2 F U2 F' R2 F U' D' L' U2 F2 L'` | 24 |

Best of these: **23**, longer than the best through a normal DR of 10 or less. Normal DRs on this scramble: 21 through one of 10 or less, 21 through 11 or less, 21 through 12 or less.

</details>

#### Scramble 97

```
R' U' F R2 U' R' U' L' D F R' F' U2 F U D' F2 U F2 R2 U' R2 B2 R' U' F // scramble
```

Skips: inverse: M slice on U/D, misoriented.

Each row is one route to a DR-xs on this scramble, shortest first; the last column is how far that DR-xs is from a real DR.

| # | Route | Length, moves | Kind | Starts from | Corner subset | Fewest turns to a real DR |
|---:|---|---:|---|---|---|---:|
| 1 | `(L' R2 F' U2 F2 R')` | 6 | DR-1s | skip: M slice on U/D, misoriented | 2c4 | 5 |
| 2 | `(L' R2 F' D2 B2 L)` | 6 | DR-1s | skip: M slice on U/D, misoriented | 2c4 | 6 |
| 3 | `(L' R2 F' U2 F2 R)` | 6 | DR-1s | skip: M slice on U/D, misoriented | 2c4 | 6 |
| 4 | `(L' R2 F' D2 B2 L')` | 6 | DR-1s | skip: M slice on U/D, misoriented | 2c4 | 5 |
| 5 | `(L' R2 B2 F U2 B2 R')` | 7 | DR-1s | skip: M slice on U/D, misoriented | 2c4 | 6 |
| 6 | `(L' R2 B D2 B F' L')` | 7 | DR-1s | skip: M slice on U/D, misoriented | 2c4 | 6 |
| 7 | `(R2 U2 F2 R B2 D2 F' L)` | 8 | DR-2s 8fe | skip: M slice on U/D, misoriented | 4b2 | 4 |
| 8 | `(R2 U2 F2 R F2 U2 F' R)` | 8 | DR-2s 8fe | skip: M slice on U/D, misoriented | 4b2 | 4 |

Shown: 6 of the 224 DR-1s of 8 or less and 2 of the 36 DR-2s 8fe of 9 or less. Shortest normal DR: 10 moves.

<details>
<summary>Answers for scramble 97</summary>

Each row is the route with the same number above: the best finish of the method's form from it, then the whole solution written out for the scramble.

| # | Finish, moves | Solution | Solution length, moves |
|---:|---:|---|---:|
| 1 | 16 | `F2 L' D2 F2 L2 F2 B2 U2 D2 R' U D F' R2 F' R L2 F2 U2 F R2 L` | 22 |
| 2 | 15 | `R2 F2 D2 B2 R U D L2 F2 B' D2 B' D2 R2 B L' B2 D2 F R2 L` | 21 |
| 3 | 16 | `R' L2 U2 L F2 L2 U2 D2 L' U D F D2 B' L2 B' R' F2 U2 F R2 L` | 22 |
| 4 | 16 | `D2 F2 L F2 R' L' D2 B2 R' F2 U' D' F' U2 F' D2 L B2 D2 F R2 L` | 22 |
| 5 | 16 | `L' F2 L' B2 L' B2 R2 U2 L' B2 U' D' B' R2 B' R' B2 U2 F' B2 R2 L` | 22 |
| 6 | 15 | `U2 B2 L' U2 F2 R2 D2 B2 R' U D F' D2 F D2 L F B' D2 B' R2 L` | 22 |
| 7 | 13 | `F2 L' B2 U2 R' F2 L2 D2 B2 U' D' R F D2 B2 R' F2 U2 R2` | 19 |
| 8 | 13 | `U2 B2 L U' D R' L' B2 U' L2 B2 D2 B2 R' F U2 F2 R' F2 U2 R2` | 21 |

Best of these: **19**, as short as the best through a normal DR of 12 or less. Normal DRs on this scramble: 20 through one of 10 or less, 20 through 11 or less, 19 through 12 or less.

</details>

#### Scramble 98

```
R' U' F D2 B2 R2 D' R2 D' L2 D R' B D' F L B2 R2 B2 D R2 D2 U2 R' U' F // scramble
```

Skips: inverse: S slice on U/D, misoriented.

Each row is one route to a DR-xs on this scramble, shortest first; the last column is how far that DR-xs is from a real DR.

| # | Route | Length, moves | Kind | Starts from | Corner subset | Fewest turns to a real DR |
|---:|---|---:|---|---|---|---:|
| 1 | `(R2 U2 F2 R2 L F R2 B')` | 8 | DR-1s | skip: S slice on U/D, misoriented | 4a2 | 6 |
| 2 | `F' R' B2 U L' F2 R D` | 8 | DR-1s | one-move slice EO: M slice on F/B, oriented | 2c3 | 6 |
| 3 | `(R2 U2 F2 R2 L B U2 F')` | 8 | DR-1s | skip: S slice on U/D, misoriented | 4a2 | 5 |
| 4 | `(F R D2 R F' B' R B)` | 8 | DR-1s | skip: S slice on U/D, misoriented | 4b4 | 6 |
| 5 | `(R L F2 D2 R' F R2 B')` | 8 | DR-1s | skip: S slice on U/D, misoriented | 4a2 | 5 |
| 6 | `F' R' B2 U L' F2 R D'` | 8 | DR-1s | one-move slice EO: M slice on F/B, oriented | 2c3 | 5 |
| 7 | `(F R' L U2 B' L F' L2 B)` | 9 | DR-2s 8fe | skip: S slice on U/D, misoriented | 4b4 | 4 |
| 8 | `(F R' L U2 B' L B' U2 F')` | 9 | DR-2s 8fe | skip: S slice on U/D, misoriented | 4b4 | 4 |

Shown: 6 of the 12 DR-1s of 8 or less and 2 of the 4 DR-2s 8fe of 9 or less. Shortest normal DR: 10 moves.

<details>
<summary>Answers for scramble 98</summary>

Each row is the route with the same number above: the best finish of the method's form from it, then the whole solution written out for the scramble.

| # | Finish, moves | Solution | Solution length, moves |
|---:|---:|---|---:|
| 1 | 17 | `B' U2 R2 B' U2 B' D2 F' D2 F U' D' L' F2 U2 R2 U2 B R2 F' R2 L' F2 U2 R2` | 25 |
| 2 | 16 | `F' R' B2 U L' F2 R U2 D B2 R2 F L2 U' D' F2 D2 R B2 R2 L' D2 L2 D2` | 24 |
| 3 | 17 | `B D2 B' D2 F R2 D2 F' U2 D2 R2 F U' D' L' B2 L2 F U2 B' R2 L' F2 U2 R2` | 25 |
| 4 | 17 | `R2 F2 R2 U2 B L2 U2 B' R2 F2 U D R F2 L2 D2 R' B' R' F B R' D2 R' F'` | 25 |
| 5 | 17 | `U2 R2 F R2 U D' B2 L B2 L B2 L2 D2 R' D2 R2 B' R2 F' R D2 F2 R' L'` | 24 |
| 6 | 16 | `F' R' B2 U L' F2 R D' R2 B2 L2 B U' D' L2 U2 R2 L' U2 R' B2 L2 U2 B2` | 24 |
| 7 | 16 | `B2 D2 F' U2 B U2 F2 R2 F' R2 F D2 L2 U' D' F' L2 F L' B U2 R L' F'` | 24 |
| 8 | 17 | `L2 F' L2 B' L2 B2 D2 B D2 F2 L2 F' L2 F2 U' D' B' U2 B L' B U2 R L' F'` | 25 |

Best of these: **24**, longer than the best through a normal DR of 10 or less. Normal DRs on this scramble: 19 through one of 10 or less, 19 through 11 or less, 19 through 12 or less.

</details>

#### Scramble 99

```
R' U' F D2 B' R2 B' R2 U2 D2 B F L2 U' F R2 U2 L' F R' B D' L F R' U' F // scramble
```

Skips: none.

Each row is one route to a DR-xs on this scramble, shortest first; the last column is how far that DR-xs is from a real DR.

| # | Route | Length, moves | Kind | Starts from | Corner subset | Fewest turns to a real DR |
|---:|---|---:|---|---|---|---:|
| 1 | `(F' R2 L2 U2 B2 U' R D')` | 8 | DR-1s | one-move slice EO: E slice on F/B, oriented | 4b3 | 6 |
| 2 | `(F' L D2 R2 L U R D)` | 8 | DR-1s | one-move slice EO: E slice on F/B, oriented | 4b5 | 4 |
| 3 | `(F' R2 L2 U2 F2 D' L U')` | 8 | DR-1s | one-move slice EO: E slice on F/B, oriented | 4b3 | 5 |
| 4 | `(F U2 R' U' D' L' U L)` | 8 | DR-1s | one-move slice EO: E slice on F/B, oriented | 2c4 | 4 |
| 5 | `(F U2 R' U' D L' U L')` | 8 | DR-1s | one-move slice EO: E slice on F/B, oriented | 2c4 | 4 |
| 6 | `(F' R F2 R L2 U R D')` | 8 | DR-1s | one-move slice EO: E slice on F/B, oriented | 4b5 | 5 |

Shown: 6 of the 44 DR-1s of 8 or less and 0 of the 0 DR-2s 8fe of 9 or less. Shortest normal DR: 9 moves.

<details>
<summary>Answers for scramble 99</summary>

Each row is the route with the same number above: the best finish of the method's form from it, then the whole solution written out for the scramble.

| # | Finish, moves | Solution | Solution length, moves |
|---:|---:|---|---:|
| 1 | 16 | `U L2 B2 U' B2 L2 U' L2 U2 F2 R L' B' L2 U2 F D R' U B2 U2 R2 L2 F` | 24 |
| 2 | 15 | `R2 B2 U B2 U L2 D' F2 D' R L' B2 D2 F' R2 D' R' U' R2 L' D2 L' F` | 23 |
| 3 | 16 | `B2 D F2 R2 U2 L2 U' L2 U F2 D' R L' F' L2 U D2 L' D F2 U2 R2 L2 F` | 24 |
| 4 | 16 | `D' R2 U' R2 B2 U R2 D' B2 L2 D' B2 R' L F' L U' L U D R U2 F'` | 23 |
| 5 | 14 | `U' D2 B2 R L' F L2 U2 F D2 B2 L2 F R2 L U' L U D' R U2 F'` | 22 |
| 6 | 16 | `D' B2 L2 D2 F2 U B2 D B2 D' B2 R L' F' R2 D' R' U' R' L2 F2 R' F` | 23 |

Best of these: **22**, as short as the best through a normal DR of 10 or less. Normal DRs on this scramble: 22 through one of 10 or less, 21 through 11 or less, 21 through 12 or less.

</details>

#### Scramble 100

```
R' U' F U R2 B2 L2 D2 F2 D F2 U2 F2 B' L' D L F' R' U B D' R2 U R' U' F // scramble
```

Skips: none.

Each row is one route to a DR-xs on this scramble, shortest first; the last column is how far that DR-xs is from a real DR.

| # | Route | Length, moves | Kind | Starts from | Corner subset | Fewest turns to a real DR |
|---:|---|---:|---|---|---|---:|
| 1 | `(D B2 L2 B' U2 R2 L' B')` | 8 | DR-1s | one-move slice EO: S slice on U/D, oriented | 4b2 | 6 |
| 2 | `(R F' U R2 U' F' B2 U')` | 8 | DR-1s | one-move slice EO: M slice on R/L, oriented | 4b2 | 6 |
| 3 | `(D B2 U2 R2 F D2 L' B)` | 8 | DR-1s | one-move slice EO: S slice on U/D, oriented | 4b2 | 5 |
| 4 | `R F U' D2 F' D' B2 U` | 8 | DR-1s | one-move slice EO: M slice on R/L, oriented | 2c4 | 4 |
| 5 | `R F U' D2 F' D' B2 U'` | 8 | DR-1s | one-move slice EO: M slice on R/L, oriented | 2c4 | 5 |
| 6 | `(D B2 U2 R2 F D2 L' B')` | 8 | DR-1s | one-move slice EO: S slice on U/D, oriented | 4b2 | 6 |

Shown: 6 of the 10 DR-1s of 8 or less and 0 of the 0 DR-2s 8fe of 9 or less. Shortest normal DR: 9 moves.

<details>
<summary>Answers for scramble 100</summary>

Each row is the route with the same number above: the best finish of the method's form from it, then the whole solution written out for the scramble.

| # | Finish, moves | Solution | Solution length, moves |
|---:|---:|---|---:|
| 1 | 15 | `U2 R2 B L2 B L2 D2 R' L U' F2 R2 L2 D' B' R2 L U2 B L2 B2 D'` | 22 |
| 2 | 15 | `R' F2 U' D' B' D2 F' D2 R2 D2 R2 F' R2 F2 L2 U F B2 U R2 U' F R'` | 23 |
| 3 | 15 | `D2 F' L2 D2 L2 F' D2 F' U2 F' R' L' D' B2 D' B' L D2 F' R2 U2 B2 D'` | 23 |
| 4 | 16 | `R F U' D2 F' D' B2 U F2 D2 F D2 F L2 B' L2 F' R2 F2 U2 F' U' D' R` | 24 |
| 5 | 16 | `R F U' D2 F' D' B2 U' F L2 F' D2 F' R2 B2 U2 L2 F' R2 B' U' D R' L2` | 24 |
| 6 | 15 | `B L2 B R L' B2 R2 B2 D R2 D L2 F2 R2 L2 B L D2 F' R2 U2 B2 D'` | 23 |

Best of these: **22**, longer than the best through a normal DR of 10 or less. Normal DRs on this scramble: 19 through one of 10 or less, 18 through 11 or less, 18 through 12 or less.

</details>

### The tally

Of the hundred above: 69 where the best shown is longer than the best through a normal DR of 10 or less; 11 where the best shown is as short as the best through a normal DR of 10 or less; 7 have none listed; 5 where the best shown is as short as the best through a normal DR of 11 or less; 5 where the best shown is as short as the best through a normal DR of 12 or less; 3 where the best shown is shorter than every normal DR of 10 or less gives.

Over all 500 scrambles and every DR-xs of the kinds listed, not just the ones shown (write-up, section 7). How often one of them is as good as the best normal-DR solution of its scramble; each row is a kind of thing to finish, and the last column is the same share turned around:

| What you finish | How many per scramble | Share that reach the scramble's best normal-DR solution | One in this many reaches it |
|---|---:|---:|---:|
| a DR-1s of 6 or less | 0.5 | 8.6% | 12 |
| a DR-2s 8fe of 8 or less | 1.0 | 3.7% | 27 |
| a normal DR of 9 or less | 6.1 | 2.4% | 41 |
| a DR-1s of 7 | 5.4 | 2.1% | 49 |
| a DR-2s 8fe of 9 | 10.9 | 0.66% | 151 |
| a normal DR of 10 | 63.6 | 0.49% | 202 |
| a DR-1s of 8 | 57.1 | 0.48% | 210 |
| a normal DR of 11 | 651.0 | 0.11% | 952 |
| a normal DR of 12 | 6,400.7 | 0.02% | 4,031 |

And what finishing them does to the result, over the scrambles with a normal DR of 10 or less; each row is a set of things you finish:

| You finish | Things to finish, per scramble | Average best solution, moves | Best solution in 20 or less | 19 or less |
|---|---:|---:|---:|---:|
| every normal DR of 10 or less | 71 | 20.62 | 45% | 18% |
| normal DRs of 10 or less, and every DR-1s of 7 or less | 77 | 20.55 | 47% | 19% |
| normal DRs of 10 or less, and every DR-1s of 8 or less | 135 | 20.42 | 50% | 22% |
| normal DRs of 10 or less, every DR-1s of 8 or less and every DR-2s 8fe of 9 or less | 147 | 20.41 | 51% | 22% |
| every normal DR of 11 or less | 733 | 20.04 | 63% | 29% |
| normal DRs of 11 or less, every DR-1s of 8 or less and every DR-2s 8fe of 9 or less | 809 | 19.95 | 68% | 32% |
| every normal DR of 12 or less | 7,244 | 19.56 | 84% | 45% |
| normal DRs of 12 or less, every DR-1s of 8 or less and every DR-2s 8fe of 9 or less | 7,319 | 19.52 | 85% | 47% |

Every finish is the best of its form, the answer key, not what you find in an hour.
