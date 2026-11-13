## 13. The claims, checked

Statements the numbers can settle, by theme. Questions and guesses are in section 2 unless a number was given. Each verdict is one of **True**, **Corrected**, **Depends** (true under one reading, not another), **Open** (not settled here) or **Withdrawn** (taken back at the time). Exact over all cases unless marked. Every correction has an example in the errata.

**4c4e.** One claim per row, with its verdict.

| Claim | Who | Verdict |
|---|---|---|
| "02, 12, 30 and 40 for 4e4c are never worth switching" | Yura Riabov [[D7086]] | **True**: {= CL('D7086-never') =}. |
| "02, 12, 03, 04 for 4e4c are like sub5 percent of sub7 dr" | Yura Riabov [[D7866]] | **True**, reading 03 and 04 as 30 and 40 (4c4e has no edge ARM above 2): 02 {= pc(EV('D7866-sub5', '02 ', ',')) =}, 12 {= pc(EV('D7866-sub5', '12 ', ';')) =}. |
| "00, 10, 21, 32 and 42 are more than 20% sub7 DR for 4c4e iirc" | tseitsei89 [[D7872]] | **True**: {= CL('D7872-20') =}. |
| "AR-3c-0/1/2e is the same as AR-1c-2/1/0e"; "not strictly symmetrical (AR-1c is not exactly the same as AR-3c : see 0.28 vs 0.29 for the 4c case." | rodneykinney [[T7438]]; Louis [[T7455]] | **True** to within a point, and Louis is right that it isn't exact: ARM 30 is {= EV('T7438-mirror', '30 ') =} against {= EV('T7438-mirror', '12 ', ';') =} for 12, 31 is {= EV('T7438-mirror', '31 ') =} against {= EV('T7438-mirror', '11 ', ';') =} for 11, 32 is {= EV('T7438-mirror', '32 ') =} against {= EV('T7438-mirror', '10 ') =} for 10. |
| "10 total sets that can be sub 6 out of the 15 total sets (7/15 can be sub 5!)" | Jay [[T4256]] | **Corrected** [a]: 11 of the 15 ARM sets have a case of at most 5 moves; AR-4c1e (shortest {= EV('T4256-sets', '41:', ',') =}) is missing from Jay's list. The 7 for sub-5 is right. |
| "For sure there aren't any 4-movers with 0 or 1 pairs, because any 4 moves from a solved cube always leaves at least 2 bad pairs." ("pairs" = bad pairs) | rodneykinney [[T597]], [[T596]] | **Depends** on what a pair is. Counting top and side pairs it is true (Radek B, [[T604]]: "0 or 1 top and side pairs => at best 5 moves", also **True**). Counting top pairs alone it is not: `{= WC('T597-4movers', 'dr') =}` is a {= WC('T597-4movers', 'length') =}-move 4c4e with no top pair, and Radek B listed its mirror `F2 B2 L` ([[T602]]). |
| "you can also recognize that all the corners are on U and know that's the only 02 case that can be sub-7 :)", "whopping 5.60%"; "corners on U, edges on D", "then it goes up to 33%!!!" | Evan [[D12760]], [[D12761]]; caycala [[D12762]], [[D12763]] | **True**: {= pc(EV('D12760-02U', 'corners on one layer ')) =}, the rest 0%; with the bad edges on the other layer {= pc(EV('D12760-02U', 'on the other ')) =}. |
| "4d+1 is extremely good for AR-21 (~90% sub-7) but 0% for other AR" | Evan [[D14342]] | **True**: {= CL('D14342-4d1') =}. |
| "b corners - 29%", "d corners - 89%", "a corners - ~34% if corners are stacked, < 5% otherwise" (1 pair + AR-21) | Evan [[D14402]] | **Corrected** [c]: b {= pc(EV('D14402-21-1p', 'b ', ',')) =} and d {= pc(EV('D14402-21-1p', 'd ', ';')) =} are right, and a with all four bad corners on one side face ("stacked") is {= pc(EV('D14402-21-1p', 'a stacked ')) =}, but the other a cases are {= pc(EV('D14402-21-1p', 'a not stacked ')) =}, not under 5%. |
| "interestingly 4a corners are basically the same for all ar-2X" | Evan [[D14348]] | **True**: {= CL('D14348-4a2X') =}. |
| "AR-0 can mean 4a-0, which is good, or 4b-0, which is bad (without pairs)" (and 4b-2 good, 4a-2 bad) | rodneykinney [[T8122]] | **True**: {= CL('T8122-a0b0') =}. |
| "To catch this case, you can switch 4a-0 and 4d-2, but only if there also are no fake pairs" (the 0-pair `F2 B2 R` case Nico asked about, [[T8107]]) | rodneykinney [[T8123]] | **Depends**: the `F2 B2 R` case itself is 4a-0 with no fake pairs and is caught, but one U/D turn earlier, `D F2 B2 R` (0 pairs, no fake pairs, {= WC('T8123-0p', 'length') =} moves), is 4b-2 and is discarded. |
| "It's simply:", "3-4 pairs: Always switch", "2 pairs: Switch unless 4b-0", "1 pair: Switch if 4d-2", "0 pairs: Don't switch" | rodneykinney [[T8108]] | **True** as a rule that beats "2+ pairs": {= pc(GR('44-rodney-case', 'share_switched')) =} switched at {= pc(GR('44-rodney-case', 'precision')) =}, against {= pc(GR('44-2pairs', 'precision')) =} (section 9). |
| "If you're looking to reach DR in ≤ 6 moves, then look for an inverse state with at least three pairs. Otherwise, you can save yourself the time of performing the NISS." | rodneykinney, *Domino Setup Theory* | **Depends** on your cut: 3+ pairs is {= pc(GR('44-3pairs', 'precision')) =} but holds only {= pc(GR('44-3pairs', 'recall')) =} of the sub-7 cases, and 2 pairs on two edges is {= CELL('c44_bars', '2 pairs on 2 edges', 'Sub-7 rate, exact') =}. rodneykinney moved to 2+ pairs later ([[T3225]]). |
| "the only 3+ pairs case i wouldn’t switch for is 3 pairs with all white or all yellow corners" | caycala [[D13393]] | **True** in effect: the rule is {= pc(GR('44-caycala-3p', 'precision')) =} against {= pc(GR('44-3pairs', 'precision')) =} for 3+ pairs. |
| "It seems like you should pretty much always switch a 4 move DR-4c4e." | Zagros [[D18940]] | **True** with DR in 7 as the target: {= pc(GR('44-always-4', 'precision')) =}; Daichi's refinement ([[D18953]]) is {= pc(GR('44-daichi-4', 'precision')) =} on {= pc(GR('44-daichi-4', 'share_switched')) =}. |
| "This is not accounting side pairs but you can quickly confirm that 0 or 1 top and side pairs => at best 5 moves" | Radek B [[T604]] | **True**: {= CL('T604-5') =}. |

**4c2e and 3c2e.** One claim per row, with its verdict.

| Claim | Who | Verdict |
|---|---|---|
| "Because it’s a three move trigger, no number of pairs will save 3qt corners" | rodneykinney [[T8147]] | **Corrected** [b]: 4c2e 4b-0 is {= pc(EV('T8147-3qt', '4b-0 0p ', ',')) =} with 0 pairs, {= pc(EV('T8147-3qt', '4b-0 1p ', ',')) =} with 1 and {= pc(EV('T8147-3qt', '4b-0 2p ')) =} with 2. |
| "4a-2 is good. 4b-2 is the bad case, because corners are 2qt, so 6 moves is the absolute minimum to DR" | rodneykinney [[T8149]] | **True**: {= CL('T8149-4b2') =}. |
| "Yeah I often check for 4a corners before switching 4c2e since that seems to almost always suck" | tseitsei89 [[D16268]] | **Depends**: 4c2e with 4a corners is {= pc(EV('D16266-4a', '4a ', ' ')) =}, about the 4c2e rate ({= pc(EV('D16266-4a', 'all 4c2e ')) =}); it is not worse in general. |
| "for 4c2e with 0p, I think niss tracing corner positions is worth it because JZP with b corners is way better than a corners" | Daichi [[D15161]] | **True**: b {= pc(EV('D15161-jzp-b', 'b ', ',')) =}, a {= pc(EV('D15161-jzp-b', 'a ')) =}. |
| "41 is 0% chance of sub 7 with 0 pairs?" | caycala [[D12737]] | **True**: {= CL('D12737-41') =}. |
| "3c2e is pretty much always worth NISSing, even as a 6 move rzp." | tseitsei89 [[D7286]] | **Depends** on the cut: after a 6-move RZP the target is DR in 5, and 3c2e is {= pc(EV('D7286-3c2e', 'DR <= 5 ')) =}. That is still the best of any DRM. |
| "At the very least you will never miss a 5 mover by doing this" (switch 3c2e on a pair, a fake pair or a split pair) | wen [[D16512]] | **True**: the {= EV('D16512-wen', 'three: ', ',') =} cases with none of the three are all 6 or more. |

**7c8e, 8c8e and the rest.** One claim per row, with its verdict.

| Claim | Who | Verdict |
|---|---|---|
| "DR-7C8E AR-2C1E is over 70% chance of sub7 dr" | Yura Riabov [[D7800]] | **True**: {= pc(CL('D7800-7c8e21')) =}. tseitsei89's 7c8e 2c1e without a sub-7 ([[D11819]]) is one of {= CL('E7-counter').split()[0] =} such cases out of {= CL('E7-counter').split()[2] =}. |
| "And for 7c8e in particular, half the cases are 0% chance of sub7 dr" | Yura Riabov [[D7887]] | **True** by ARM set: {= CL('D7884-half') =}, holding {= pc(CL('D7884-half', 'verdict').split('hold ')[1].split()[0]) =} of 7c8e cases. |
| "all that i've memorized is that 1C0E is always 5-6 and 2C1E is the only one that can give sub 4" | Jay [[D5086]] | **True**: {= CL('D5086-7c8e') =}. |
| "After revisiting the ARM stats I noticed that edge ARM =4 always has 0% chance for sub7." "And yes 3 seems to be much better than 2, but also only good if corner ARM >= 4" | tseitsei89 [[T9279]] | **True**: edge ARM 4 {= pc(EV('T9279-7c8e', 'edge ARM 4 ', ';')) =}; edge ARM 3 {= pc(EV('T9279-7c8e', 'edge ARM 3 ', ' ')) =} against edge ARM 2 {= pc(EV('T9279-7c8e', 'vs 2 ', ';')) =}. |
| "7c8e is actually the exception because with 8 bad edges, every bad in-ARM corner forms a side pair anyway." | rodneykinney [[T9450]] | **True**: {= CL('T9450-7c8e-side') =}. |
| "for 7c8e with 5p, 20/54 has a 0% chance of sub7"; "it's still 54% in general" | Daichi [[D15161]], Fanti [[D15170]] | **True**: {= CL('D15161-5p') =}. |
| "also 78 4p has a weird silver lining with 11/12/33/41/62 where they're all just slightly worse", "20-23% sub7, though keep in mind only 21 can have sub-6 on 4p" | Fanti [[D15175]], [[D15176]] | **True**: {= CL('D15175-4p') =}. |
| "AR-1C2E might be worth switching since it's exactly a 1-in-6 chance of sub 7 to DR" (7c8e) | Jay [[D10593]] | **True**: 7c8e ARM 12 is {= pc(E['arm_rate']['7c8e']['12']) =}. |
| "4b: 12%", "4a: 43%" (8c8e AR-4c2e by the corner case of the out-of-AR corners) | trangium [[T11493]] | **True**: {= CL('T11488-8c8e') =}. |
| "8e8c - R L but only if four corners are clockwise and four are ccw (7/1 is possible)" | Zagros [[T6505]] | **True**: every one of the {= n(RJ['c88']['n44']) =} 8c8e cases with a 4-4 twist split has a DR with two quarter turns (U, D and half turns free), and none of the {= n(RJ['c88']['n71']) =} with a 7-1 split has: they need three. Sub-7 is {= pcx(RJ['c88']['p44']) =} against {= pcx(RJ['c88']['p71']) =} (section 5.2). |
| "You shouldn't switch 6e4c unless it's jzp" | Yura Riabov [[D6915]] | **True**: JZP {= pc(RG('4c6e', 'switch')) =}, 4 pairs {= pc(RG('4c6e', 'check')) =}, everything else together {= pc(RG('4c6e', 'discard')) =}. |
| "even with full moveset sub-7 is 1 in 22" (4c6e) | Cale [[T1805]] | **True**: {= CL('T1805-4c6e') =}. |
| "it’s 1/7 for 7 moves instead of 1/3 for 4e4c, 8c8e, 8e7c, 2e4c etc" (3c6e) | Noah Swor [[D6979]] | **Depends**: the 1/3 fits DR in 6 on the better of normal and inverse (4c4e 1 in {= EV('D6979-3c6e', '4c4e 1 in ', ',') =}, 7c8e 1 in {= EV('D6979-3c6e', '7c8e 1 in ', ',') =}), and then 3c6e is 1 in {= EV('D6979-3c6e', '3c6e 1 in ', ',') =}, worse than 1/7. No reading gives both numbers. |
| "It could be worth it mathematically if it's AR-2C1E (only subset where +4 to DR is possible)" (3c6e) | Jay [[D6982]] | **True**: {= CL('D6982-3c6e') =}. |
| "21 which is the 4move trigger one is only 15%" (5c4e); "They all have around a 15% chance of getting sub-7" | Yura Riabov [[D7854]]; Levi Gibson [[D10597]] | **True**: {= CL('D7854-5c4e21') =}. |
| "For example, 5c4e with 2 pairs has 40% chance of sub-8." | rodneykinney [[T9348]] | **Open**: any optimal DR gives {= pc(EV('T9348-5c4e', 'DR <= 7: ', ' ')) =}; rodneykinney's numbers may count only findable solutions. |
| "Yes, that’s the conclusion" (the DRMs outside the top ten are not worth looking at) | rodneykinney [[T9480]], to zakimoshi [[T9479]] | **True** for the time it takes: some are better per case but very rare (0c2e and 2c0e have {= CL('T9480-rest', 'verdict').split('0c2e 1.000 (')[1].split()[0] =} and {= CL('T9480-rest', 'verdict').split('2c0e 0.714 (')[1].split()[0] =} sub-7 cases in all). |

**Switching, NISS and the tables.** One claim per row, with its verdict.

| Claim | Who | Verdict |
|---|---|---|
| "if the EO isn't already 4c4e, it means that the 4c4e case you get from RZP is 1 move away from something that is not 4c4e", "the 4c4e cases that can go out of 4c4e in more ways will thus be more likely to show up" | torchlight [[T4250]] | **True** on the same side ({= pc(POP('4c4e', 1)) =} against {= pc(POP('4c4e', 0)) =}), and it vanishes after a switch (section 8). |
| "the number of axially reduced pieces is always equal between one axis on normal and the other on inverse"; "Remember that ARM switches axis when you NISS" | Cale [[T4202]]; wen [[D7896]] | **True** on every sampled cube (section 7). |
| "It remains the same on the same axis." | Louis [[T4357]] | **Withdrawn** ("Yes you're right it makes total sense", [[T4361]]): it holds on about one cube in ten. |
| "It's easy to predict how many corners will be out of AR on inverse: count the number of R/L stickers on the U/D face." and the corner-case flow chart | rodneykinney, *DR - 4c4e Theory* | **True** on every sampled cube; checked by sampling, not proved (section 7). |
| "if the 2 stickers on the corner that are touching the E slice match with that E slice edge, then that's a pair on inverse" | wen, *Hitchhiker's Guide to DR* | **True** on every sampled cube (section 7). |
| "But if you assume the axes are independent (which is probably a reasonable approximation) then if one has 20% chance and the other has 10%, then the combined chance is 28%" | caycala [[D14218]] | **True** to within half a point for the named DRMs (section 8). |
| "like how DR-4e4c in 6 moves is 1 in 5.2 normally, but 1 in 3.6 if you can switch the last move" | Tom Nelson [[D2200]] | **True**: {= CL('C2-lastmove') =}. After a switch the last EO turn is worth much less (section 8). |
| "After EO, there are approximately 1 million distinct DR-equivalent cube states, of which approximately 64,000 have sub-7 solutions." | rodneykinney, *DRM Subsets* | **True**: {= CL('A1-64000') =}. |
| Fanti's rule figures for 4c4e, 4c2e, 7c8e, 3c2e and 3c4e ("= 35.2% switches", "42.6% sub-7 switch success (15.0% total)", "4.3% of cases will be discarded with sub-7" for 4c4e, and the rest) | Fanti, *armpairs_1.txt* [[D15160]] | **True**, exactly, with the any-turn optimum (F/B quarter turns allowed); EO-kept, 4c2e moves from {= pc(EV('doc583-4c2e', 'success ', ',')) =} to {= pc(EV('doc583-4c2e', 'EO-kept: success ', ',')) =} and the others by less (section 12). |
