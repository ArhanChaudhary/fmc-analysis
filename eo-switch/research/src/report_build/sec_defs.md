## 3. Definitions

Everything is written for an F/B EO and a DR on U/D. Other axes are the same up to a rotation.

**State, switched side.** What matters for the DR is the *case*: which corners are twisted and how, and which places hold the four E-slice edges ($2187 \times 495 = {= n(1082565).replace(',', '{,}') =}$ of them for one EO axis and one DR axis). After EO + RZP you have a case on normal. Switching means solving the DR on the inverse with the EO kept, so the case that matters is the inverse's, the *switched case*. All rules here are read on the switched case. Section 7 is about seeing it on normal.

**Sub-7.** A DR in at most 6 moves with turns that keep the EO (U, D, R, L, F2, B2), linear, on the switched side, the yardstick since "we are normally looking for rzp in 5 or less and dr in 11 or less. So sub-7 from 5 move rzp gives that" (tseitsei89, [[D15188]]). For other RZP lengths the target moves: DR in 7 after a 4-move RZP, DR in 5 after a 6-move RZP. The cards give those columns too.

**DRM.** Bad corners: corners whose U/D sticker is not on U or D. Bad edges: twice the number of E-slice edges outside the E slice, so all edges out of DR are counted. Written corners first (4c4e).

**ARM.** Corner ARM: bad corners whose U/D sticker is on R or L. Edge ARM: bad edges in the M slice, that is E-slice edges sitting at UF, UB, DF or DB. Written corner digit first (21 = AR-2c1e = corner ARM 2, edge ARM 1). *JZP* is ARM 00 with an even number of bad corners.

**Pairs.** A *pair* (top pair) is a bad edge in the U or D layer and a bad corner next to it in the same layer whose U/D sticker is on the side face the edge doesn't touch, as after R from a solved cube (which leaves 4 pairs: two bars). A *fake pair* is the same two pieces with the corner twisted the other way, its U/D sticker on the edge's side face. A *side pair* is a bad edge in the E slice (a U/D edge sitting there) and the corner above or below it, twisted to pair. These are the counts of Louis's and rodneykinney's code, which agree with each other on every case (appendix B). A bar (an edge paired on both sides) counts as 2 pairs.

**Paired edges.** In 4c4e and 4c2e there are two bad edges in the U/D layers. *Paired edges* is how many of them have at least one pair: 0, 1 or 2. Two pairs on one edge (a bar) is 1 paired edge, and two pairs on two edges is 2.

**Corner case.** rodneykinney's 4a, 4b, 4c, 4d for four bad corners, by how the bad corners split between the two HTR orbits (4d all in one, 4c 3-1, 4a and 4b 2-2, 4b if some U, D, R or L face has exactly 1 or 3 bad corners), with the corner ARM suffix ("4b-0", "4d-2").

**Rings, rows, holes.** A *ring* is the 8 places of the U or D layer, read clockwise as you look at that face (U: UB UBR UR UFR UF UFL UL UBL; D: DB DBL DL DFL DF DFR DR DBR). A bad corner *points* at the edge place next to it that its U/D sticker does not touch, the one it would pair with: so a pair is a bad corner pointing at a bad edge and a fake pair is one pointing away from the bad edge next to it. A *row* is the corner, edge, corner of one layer on one side face. A *hole* is an E-slice place holding a U/D edge. Ring strings (`>E<-o-o-`) are explained in section 4.1.

**Half turns to two bars** (4c4e). The fewest half turns (R2, L2, F2, B2) after which one R or L quarter turn gives DR, with U and D turns allowed anywhere and not counted. It equals the larger of the *row swaps* (fewest exchanges of a U row with a D row that leave a bar in each ring) and the hole number (0 if the two holes are on one R/L face, 1 if diagonal, 2 if on one F/B face).

**Side turns** (any DRM). The fewest turns of the side faces (R, L quarter or half turns, F2, B2) in any DR of the case, U and D turns not counted. A case is *short* if it needs 3 side turns or fewer with no more quarter turns than its DRM needs anyway (1 for 4c4e, 2 for the other named DRMs).

**Verdict bands.** A group of cases is *switch* if over 50% of it is sub-7, *discard* if under 10%, and *your call* in between. That's where the server's own cut-offs sit ("i think it's best to find the <10% ones and dont switch for those and switch everything else maybe", wen, [[D7081]]; "i switch for around 20% and above", Yura Riabov, [[D7082]]; "I would say below 20% is never and above 30% is pretty much always.", tseitsei89, [[T9318]]). A rule *settles* a case if its cell is switch or discard. *Settled* is the share of the DRM's cases that land in such cells. *Sub-7 states switched* (recall) and *sub-7 states discarded* are shares of the DRM's sub-7 cases and of all its cases.

**Populations.** *Uniform*: every case of the DRM counts once. That is what Cale's, Louis's and rodneykinney's tables count, and what the cards are graded on (exact). *After an RZP*: cases weighted by the number of RZPs of a given length that reach them from a uniform EO-solved cube (exact counts), on the same side or after the switch. *Real attempts*: {= n(6000) =} uniformly random scrambles, every EO of at most 6 moves on each axis, on normal and on inverse, both DR axes of each, and every RZP that first reaches its DRM at a total of 4, 5 or 6 moves ({= n(E['attempts_total']) =} attempts, about {= n(E['attempts_total'] / 6000) =} per scramble, so their errors come from batches of scrambles, not from the attempt count).
