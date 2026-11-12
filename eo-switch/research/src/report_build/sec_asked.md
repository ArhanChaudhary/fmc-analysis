The questions, in the words of the people who asked them, with where each is answered. Most got an opinion or no answer at the time.

**The request (sections 4 and 5)**

- A professional solver asked me, through the site's author, for better switch guidelines than ARM, DRM, pairs and the corner orbit cases, closer to 100% or 0% sub-7, that a human can check quickly. *Answer*: the switch cards in section 4, read from the normal side as in section 5. The limit is in section 9: cheap checks top out around 60% for common cases.

**Which feature says most (sections 4, 8 and 9)**

- JTuu ([[T4332]]): "it might be useful to have a table comparing P(optimal < N | rzp) against P(optimal < N | rzp, arm). that is, when is the arm info most informative?" eff ([[T8206]], [[T8207]]): "yeah is there an objective comparison between the two yet", "arm-xcxe vs xy-z with n pairs". *Answer*: pairs settle more cases than ARM for 4c4e, 4c2e and 7c8e, ARM more for 8c8e and 2c2e, and for 4c4e paired edges plus edge ARM settle more than pairs and ARM together (section 8). The information measures are in section 9 (**computer only**).
- wen ([[D14349]]): "Interestingly now we have basically 3 criteria for NISS that we can trace, >1pair/ARM/corner structure", "if we pick 2 out of 3 to stick to, which gives the lowest false negative rate?" *Answer*: pairs + corner case, by a little over pairs + ARM; ARM + corner case is far behind. Paired edges + edge ARM, which isn't on wen's list, settles more cases than any two of the three (section 8).
- Zagros ([[T11345]]): "Is number of corners NOT in a pair a better heuristic across all DRM than number of pairs?" *Answer*: section 8. Once you know the DRM, they say the same.
- tseitsei89 ([[T9334]]): "It would be really nice to find a way to filter out good 1 pair cases but there doesnt seem to be one currently". *Answer*: edge ARM, then the corner case (section 4.1).
- bpaul ([[D12986]], [[D12987]]): "random thought i wonder whether looking at pair stats not just on the count but also based on the number of pairs per edge could be good", "sounds way harder to count for higher corner counts but maybe for 4c4e it would be helpful idk". *Answer*: yes, and it is the main 4c4e finding (sections 4.1 and 8).
- caycala ([[D11050]]): "i wonder what the probability is for 21 + no pairs+ 1 corner pair". *Answer*, reading "corner pair" as a side pair: 4c4e ARM 21 with no pairs and 1 side pair is {= pc(Q4('4c4e ARM 21, 0 pairs, 1 side pair(s)')) =}; with 2 side pairs it is {= pc(Q4('4c4e ARM 21, 0 pairs, 2 side pair(s)')) =}.
- FakeMMAP ([[D12097]]): "Do you think it's worthwhile to check for ARM if you have 0 pairs on the off-chance it's a short setup to F2 B2 R?" *Answer*: with 0 pairs, ARM 00 is {= pc(Q4('4c4e, 0 pairs, ARM 00')) =} and ARM 42 is {= pc(Q4('4c4e, 0 pairs, ARM 42')) =}, but each is only 36 of the 21,000 zero-pair cases. Every other ARM is {= pc(Q4('4c4e, 0 pairs, ARM 21')) =} or less (ARM 21 is the best of them). So it's worth it only if the ARM check costs you nothing.

**Real RZPs, the last turn and the other axis (section 6)**

- KrzychXyz ([[T4265]]): "Does this mean that DR-4c4e's occuring "naturally" are statistically better than those obtained by doing some post-EO moves?" (after torchlight's [[T4250]]). *Answer*: on the same side, yes, slightly; after a switch there is no difference at all.
- Jay ([[T6694]]): "i'm wondering if it's worth investigating the affects on sub 6/7% chance for DRM/ARM combos where you also account for what the DRM/ARM is when you "flip" the RZP via RLUD stuff?" *Answer*: flipping the RZP's last turn never changes the switched case (section 6).
- DanielEgdal ([[T3226]]), JTuu ([[T4324]]), Evan ([[D14213]]): whether the other DR axis was ever counted: "has anyone thought about whether it's useful to consider ARM on both dr axes for a given eo? (I have not)", "i don't think any research has been done on dual axis switching probabilities". *Answer*: section 6 (and my EO-to-DR study for the unswitched case).
- Lichi Fang ([[D4958]]): "Is there any practical approach to consistently find good DRs from DR-5c4e, DR-5c6e or DR-6e6c?" *Answer*: not by switching on cheap features (sections 4.6 and 9).

What this leaves open is in section 12.
