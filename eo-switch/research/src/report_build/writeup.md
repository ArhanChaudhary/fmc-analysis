# When to switch an EO

You have an EO and an RZP, and you're deciding whether to switch: go to the inverse, keep the EO, and look for a short DR there. I put a number on every switch rule the server uses and look for better ones you can check at the table. The best one I found is a count, not a feature: how many turns of the side faces the DR needs when U and D turns are free. For 4c4e that is the number of half turns to two bars, and it runs from a certain sub-7 to a certain miss. The target is the usual one: a DR in 6 or less on the switched side (sub-7), EO kept. I solved every EO-solved state for one EO axis and one DR axis exactly ({= n(1082565) =} states) and graded the rules on three populations: those uniform states (what every existing table uses), the states an RZP actually reaches (counted exactly), and {= n(E['attempts_total']) =} real attempts (every EO of up to 6 moves on {= n(6000) =} uniformly random scrambles, with every RZP after it to a total of 4, 5 or 6 moves). The real attempts are a sample, with a share's standard error taken from batches of scrambles; everything else is exact.

November 2026. A date in brackets is a link to that message on the FMC solvers Discord (#fmc-theory, #fmc-discussion or #non-dr-discussion). Docs and sheets are listed with links at the end.

**This builds on** what the server already had:

- **Cale's [*DR setup stats*](https://docs.google.com/spreadsheets/d/11bTZ4Y7_6qKlIWo4a4TLW45M2ZkctQZAVxgQqEtlUs0)** and its [last-move version](https://docs.google.com/spreadsheets/d/1_2PmFv1KyBX335SjSb4oweS0sx804fIhbuP50D-gBj4): the EO to DR table per DRM. Cale also gave the observation that makes ARM a NISS tool: "the number of axially reduced pieces is always equal between one axis on normal and the other on inverse" ([[T4202]]).
- **Louis's [*DRM/ARM average optimals*](https://docs.google.com/spreadsheets/d/13fSwUROzP0hZQV1Cn96GndWbPy4UrsHiYTaWFSeWtJs)** ([[T4327]]) with its code ([github.com/LouisSart/DRM-ARM-stats](https://github.com/LouisSart/DRM-ARM-stats)): every DRM × ARM cell exactly.
- **rodneykinney's** corner cases (4a, 4b, 4c, 4d, "based on how the bad corners are split between the HTR orbits", [*DR - 4c4e Theory*](https://docs.google.com/document/d/1DsxAAB2WRfpgDR-VWZZrXq2W4y_YMXBufRRYNLAGGoU)), [*DRM corner variant+pair stats*](https://docs.google.com/spreadsheets/d/174ClwBFl-T2zJAq8MVyK1bKsIIuzxQU0_XmQGv82LPQ) ([[T8108]]), the [*DRM Subsets*](https://docs.google.com/document/d/1AUQVrecEFZyR6okXAyJgtQZA-A0AJmAUevhJZlQMjAs) doc and [decision trees](https://rodneykinney.github.io/DRM-ARM-stats/drm_trees/), [*DRM Subsets Meta*](https://docs.google.com/document/d/1Jnd1Qy_6b1W5dR5fZQScloMoMPR2LCAF7VPrgeTaRgg), the older [*Domino Setup Theory*](https://docs.google.com/document/d/1Z3O8BY1LbAMF6m55ufXtSdtBVwSJpMArtRrDT-p_CwM) and [*Axial Reduction Theory*](https://docs.google.com/document/d/1TomrUJ9XWAQXBp7ghSB-iXs1WpPm20FGUw5OBoKgn7g). The side-pair rule ("2 side pairs counts as one top pair", [[T9448]]) and "1.5+ pairs" ([[T9468]]) are rodneykinney's. *DR - 4c4e Theory* is also where section 4 starts from: "The final trigger must have two full “bars” formed with the bad corners and edges.", with a side half turn as "an opportunity to form a pair for free" and "An additional 0-2 moves may be needed to solve the E slice."
- **Evan's** sampled [*4c4e ARM subtype stats*](https://docs.google.com/spreadsheets/d/1PAVonITR4HLBMml1-uxJwGRwHIoRWIGdNsK-A_KG_yA) and [*arm/pairs*](https://docs.google.com/spreadsheets/d/1YZYyokxYXwDdBTgN7ojpPAFHKKz48hCyNO2l6-iwmVk).
- **Fanti's** rule sets with their measured performance (*armpairs_1.txt*, [[D15160]]), **Radek B's** tables from Louis's data, and **Levi Gibson's** (beef beans on Discord) [*Sub-7 simulations*](https://docs.google.com/spreadsheets/d/1Nqr2yICQqXuKrs1pkXWizsYw7-OU6FU4F7hzaE7pN2E).
- **The hand rules** of Yura Riabov, tseitsei89, wen, Jay, Noah Swor, Lewis Isom, caycala, compLex, Daichi, Zagros and Fanti; **torchlight's** point that an RZP biases the case it reaches ([[T4250]]); and **wen's** pair tracing in the [*Hitchhiker's Guide to DR*](https://docs.google.com/document/d/1E_5wSKvQFXXZY4f3xLM76qMUrVGp9Pe7vgotS0X-T4U).
- **My own EO-to-DR study** ([*EO to DR, and scramble to DR*](../eo-to-dr/)): the exact EO to DR distance of every EO-solved state, by DRM, with the EO's last turn free, the other DR axis and the inverse.

**What this adds**:

- **The two-ring picture**: U and D turns never change a pair, so a switched case is two rings and four E-slice places, a half turn swaps a row between the rings, and a quarter turn has a one-line rule. It is exact for every case.
- **For 4c4e, half turns to two bars**: 0 or 1 is a certain sub-7, 2 is {= pcx(RH(2)) =}, 3 is {= pcx(RH(3)) =}, 4 or 5 is {= pcx(RHG('ge4')) =}. How to count it from a pair trace, and what it costs.
- **For every DRM, side turns**: 2 or fewer is a certain sub-7, and 3 with no extra quarter turn is the switch group. It splits every card's groups, 7c8e with 5-6 pairs into {= pcx(RCROSS('7c8e', '5 or 6 pairs', 'short')) =} and {= pcx(RCROSS('7c8e', '5 or 6 pairs', 'not short')) =}.
- **One switch card per DRM for a pair trace alone**: a rule you check by tracing, with the sub-7 share of each verdict and how much of the DRM it settles. Each card is the best cheap rule the search found, and it holds up on the real attempts.
- **For 4c4e, a better pair rule than pairs or ARM**: count the paired edges, then look at edge ARM. It settles about twice as many cases as either one.
- **Three new readings from the normal side**, each checked on {= n(TRACE('side pairs', 'uniform')[0]) =} random cubes: the two rings with their holes, side pairs on the inverse, and edge ARM on the inverse without switching axes.
- **What a real RZP changes**: the RZP bias is gone once you switch, so the uniform tables are exactly right for switched cases. After a switch the RZP's last turn is worth nothing and the EO's last turn very little.
- **Every existing rule graded** the same way (how much it switches, how often that's a sub-7, how many sub-7s it throws away), on the uniform states and on the real attempts.
- **The claims checked**, the sheets reproduced cell by cell, and an [errata](errata.html) page with three corrections.

**Terms**, as the server uses them. *Switch* means NISS: after EO + RZP you go to the inverse and keep the EO ("switches means that after you go a certain path, you NISS?", "yeah", [[D18365]], [[D18367]]). *DRM* is the number of bad corners and bad edges, corners first (4c4e = 4e4c), counting all edges out of DR. *ARM* is two digits, corners then edges (21 = AR-2c1e). *Pairs* are top pairs, *side pairs* are E-slice pairs, *4a* to *4d* are rodneykinney's corner cases. *Sub-7* means a DR in at most 6 moves, keeping the EO (U, D, R, L, F2, B2 for an F/B EO). New here: a *ring* is the 8 places of the U or D layer, a *row* is the corner, edge, corner of a layer on one side face, a bad corner *points* at the edge place it would pair with, a *hole* is an E-slice place holding a U/D edge, *side turns* are the turns of R, L, F and B in a DR, and *half turns to two bars* is the 4c4e count of section 4. Section 3 has the full definitions. The rules are read on the switched side; section 7 says how to see each feature on normal before you switch.

**How to read it.**

- **Start with [section 1](#1-the-short-version)**, the short version: what is new, then what it confirms or corrects. If you read one thing after it, make it [section 4](#4-two-rings-count-the-half-turns-4c4e): the ring picture and the half-turn count.
- **The [worked examples](examples.html)** go with it: 200 real attempts from random scrambles, each with what you'd trace on normal (the rings included), the half-turn or side-turn count, the card's verdict, and the optimal DR after the switch, answers folded away. **The [errata](errata.html)** list what the numbers show is wrong in things said on the server, each with an example.
- **Sections 5 and 6** are the other DRMs and the cards for a pair trace alone. **Sections 8 to 13** are the details behind section 1. Anything marked **computer only** is an answer key, not advice: it can't be checked at the table.
- **✓ after a number: proved in Lean**, recounted on a Lean model of the cube, not only computed. [Appendix B](#appendix-b-how-it-was-computed-and-what-checks-it) lists what is proved and what is only computed.

---

{{CONTENTS}}

---

## 1. The short version

{{SEC_SHORT}}

---

## 2. What was asked

{{SEC_ASKED}}

---

{{SEC_DEFS}}

---

{{SEC_RINGS}}

---

{{SEC_SIDE}}

---

{{SEC_CARDS}}

---

{{SEC_READ}}

---

{{SEC_POP}}

---

{{SEC_GRADE}}

---

{{SEC_FEAT}}

---

{{SEC_COMP}}

---

{{SEC_SHEETS}}

---

{{SEC_CLAIMS}}

---

{{SEC_LIMITS}}

---

{{APP}}
