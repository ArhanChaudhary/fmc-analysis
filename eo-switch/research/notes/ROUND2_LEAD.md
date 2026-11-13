# Round 2 lead: side turns with U/D free, and the two-ring puzzle (2026-11-13, exploratory, numbers from x4/x6/x7/x8.py)

Setting as in the study: F/B EO, DR on U/D, 1,082,565 cosets, d = exact EO-kept DR distance (out/big/d.u8), sub-7 = d <= 6.

## 1. Side-turn count sigma (x6.py)
sigma(state) = fewest side-face turns (R, R', R2, L, L', L2, F2, B2) in any DR solution, U and D turns free (0-1 BFS).
Any solution with s side turns can be padded to at most 3s moves (U*, D* before each side turn), so sigma <= 2 => d <= 6: certain sub-7.
All states: sigma 0: 1; 1: 32; 2: 2,164 (all sub-7); 3: 111,488 (30.8% sub-7); 4: 914,232 (3.0%); 5: 54,648 (0.1%).
By DRM (share of DRM at sub-7 rate):
4c4e  s<=2 1.0% at 100 | s3 19.2% at 57.2 | s4 77.8% at 9.3 | s5 2.0% at 0
4c2e  s2 1.0% at 100 | s3 33.1% at 41.7 | s4 66.0% at 6.0
3c2e  s2 7.1% at 100 | s3 67.9% at 71.1 | s4 25.0% at 25.0
7c8e  s2 0.4% at 100 | s3 15.2% at 51.3 | s4 83.5% at 9.8 | s5 0.9% at 0
8c8e  s2 0.1% at 100 | s3 18.1% at 40.8 | s4 79.4% at 8.9 | s5 2.5% at 0
2c2e  s3 39.3% at 40.9 | s4 60.7% at 12.5
4c6e  s2 0.1% at 100 | s3 9.3% at 31.0 | s4 87.2% at 1.8 | s5 3.4% at 0.2
3c4e  s3 18.5% at 34.1 | s4 80.0% at 4.6 | s5 1.5% at 0
3c6e  s2 1.0% at 100 | s3 20.4% at 16.2 | s4 77.0% at 0.7 | s5 1.5% at 0
5c4e  s3 8.3% at 34.7 | s4 88.6% at 4.9 | s5 3.1% at 0
5c6e  s3 9.8% at 29.7 | s4 86.5% at 3.7 | s5 3.7% at 0.3
6c6e  s3 8.2% at 29.6 | s4 86.8% at 3.6 | s5 5.0% at 0.3

## 2. 4c4e: half turns to two bars (x4.py)
A 4c4e is one R/L quarter turn from DR exactly when both layers have a bar (corner, bad edge, corner, each corner twisted
to pair) on the same R or L face and the two U/D edges in the E slice are on that face (2 cosets). 82% of 4c4e sub-7s
finish with a single quarter turn (11,128 of 13,576); the other 2,448 need three quarter turns.
hmin = fewest half turns (R2 L2 F2 B2) to reach that, U/D free:
hmin 0: 32 states, 100% sub-7 | 1: 688, 100% | 2: 9,288 (13.2% of 4c4e), 72.1% | 3: 36,000 (51.0%), 16.0% | 4: 23,856 (33.8%), 1.7% | 5: 696, 0%.
(The published card: both edges paired 15.5% at 59.9%; one paired + edge ARM 1 32.5% at 20.0%; rest 52.0% at 6.7%.)

## 3. The two-ring puzzle (x7.py, x8.py)
U and D turns never change pairs. So forget how each layer is turned: a layer is a ring of 8 places (corner, edge,
corner, edge, ...) read clockwise from outside (U: UB UBR UR UFR UF UFL UL UBL; D: DB DBL DL DFL DF DFR DR DBR).
A bad corner is a hook: its U/D sticker is on one side face, and it pairs with the edge place on its other side face;
so it points clockwise or counter-clockwise along the ring. A pair = a hook pointing at a bad edge next to it; a bar =
bad edge hooked from both sides; a fake pair = hook next to a bad edge pointing away. Twist is unchanged by U, D and half
turns, so a hook keeps its direction for the whole setup; there are two of each direction.
A half turn at a face swaps the corner-edge-corner window of the U ring at that face with the D ring's window there,
keeping the clockwise order (R2: UBR UR UFR <-> DFR DR DBR), and swaps the two E-slice places on that face. With U and D
free, any U window can be swapped with any D window.
Checked on all 70,560 switched 4c4e cosets: hmin(cube) = max(hmin(rings), slot type), slot type = 0 if the two U/D
edges in the E slice share an R/L face, 1 if diagonal, 2 if they share an F/B face (F2/B2 move type 0<->1, R2/L2 move
1<->2). 780 ring pairs up to turning each layer.
Ring hmin -> classes, share of 4c4e, sub-7: 0: 1 class; 1: 12 (0 and 1 together 1.5%, 97% sub-7: 100% for slot type 0
or 1, 90-94% for type 2); 2: 95 classes, 12.7%, 71% (79 / 63 / 72 by slot type); 3: 392, 51.0%, 16%; 4: 268, 33.8%, 1.7%;
5: 12, 1.0%, 0%.
Pairs alone do not fix ring hmin: e.g. 3 pairs with the edges in different rings is 1, 2 or 3 swaps; two pairs on two
edges 1 to 4; one pair 2 to 4; no pair 2 to 5 (table in x8.py output).
Mental model that explains the lists (not yet a proved rule): a hook travels with the two places behind it (the edge
place and corner it points away from). A lone hook is inserted with one swap when it is in the other ring than the edge
that needs it, the two places behind it are clean, and the two places beyond the empty spot are clean. A hook in the
same ring as its edge but in the wrong place needs two swaps (out and back), unless a swap fixes two things at once
(two lone hooks can trade rings in one swap; a bar can change ring with one swap).
