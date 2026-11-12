# FakeMMAP's reduction bound (T11501–T11504): the model, the five terms, C and the α index

Working notes for section 9 of the HTR-routes study, written 12 Nov 2026 after a solver pointed out that the
published text wrongly said C "must be the shortest NISS HTR". Sources: FakeMMAP's messages of 8 Apr 2026 in
#fmc-theory (T11501–T11504 in the KB), read in full. Code: `src/bounding2.py`, `src/t11503_cex.py`,
`src/xlbdist.py`, `src/check_c_invariance.py`.

## 1. What FakeMMAP set up (T11501)

"Let's say we're looking for a finish in M moves (or less), assuming we're only allowed to use N>1 qts. We want to
know how long our reductions to 1q should be, in order to find that solution. Let R be the biggest possible length of
a reduction to 1q you have to check". Inputs: A ("Optimal HTR on normal"), B ("Optimal HTR on inverse"), C ("The entire
HTR subset: let the shortest possible HTR in the subset have length C (so 2c3 2e would have C=5, 4b2 0e would have
C=6)"), and α_i, "the bound for the ith section", sections "bounded by qts", numbered 0 to N ("4a3 2e would have
α_1=3, because you have to to the 4b2 parity fix").

## 2. The model

A DR finish with N quarter turns is

    F = h_0 q_1 h_1 q_2 ... q_N h_N

with h_i a run of half turns of length s_i ≥ α_i and q_k a quarter turn. Its length is L = N + Σ s_i ≤ M.

**Windows and reductions.** A reduction to 1q leaves one quarter turn with its two neighbouring sections as the 1q
finish, h_{k-1} q_k h_k: the moves before it (on normal) and after it (on inverse) are the reduction. FakeMMAP's
term 1, "M-α_i-α_{i+1}-1 (basically leaving those two as the 1q finish)", fixes the indexing: **window i
(i = 0..N-1) is sections i and i+1** (quarter turn q_{i+1}), and its reduction has length

    ρ_i = L − 1 − s_i − s_{i+1}.

The shortest reduction that finds F is min_i ρ_i, and R is the worst case over all finishes allowed by the
constraints: R = max over feasible s of min_i ρ_i.

**Constraints**, each a statement about a block of F that must be an HTR:

| | block | why it is an HTR | constraint |
|---|---|---|---|
| α | section i | the corner path forces at least α_i half turns there | s_i ≥ α_i |
| A | h_0 q_1 ... q_N (all but h_N) | what remains, h_N, is half turns only | L − s_N ≥ A |
| B | q_1 h_1 ... h_N (all but h_0), read on inverse | inverse of F minus h_0^{-1} leaves h_0^{-1} | L − s_0 ≥ B |
| C | q_1 h_1 ... q_N (all but h_0 and h_N) | a linear HTR of X·h_0 (the state after h_0), and X·h_0 has the same label as X | L − s_0 − s_N ≥ C |

For C to be FakeMMAP's C (the subset's shortest linear HTR) the label (corner subset × bad edges) must not change
when a half turn is applied to the state. In this study's conventions it does not, on either side:
`check_c_invariance.py` applies each of the 6 half turns after and before 3,000 random DR scrambles on the
independent sticker model and the label never changes (47 of the 48 labels occur;
`out/checks/check_c_invariance.txt`). This is also the stated design of the Rust labels (`model.rs`: labels are
functions of the HTR coset, unchanged by a half turn on the left). So C = min over the label's HTR cosets of the
linear HTR length (`out/checks/htr48.tsv`): 2c3 2e = 5, 4b2 0e = 6, FakeMMAP's two examples.

**What was wrong before.** `R_exact`/`LB_exact` used `for j in 1..N-1: L − s_j ≥ C`, i.e. removed one *middle*
section. What is left is a prefix (normal) plus a suffix (inverse), a NISS HTR of X itself, not a linear HTR of a
state in the subset. With C linear that family is false (NISS HTRs go below the linear minimum), so the model
failed, and plugging the state's own NISS HTR in for C made it valid again. Hence the published "C must be the
shortest NISS HTR". FakeMMAP's C enters only through the middle block, which is linear.

## 3. The five terms of T11502, derived

Fix any finish allowed by the constraints and let r = min_i ρ_i, so for every window i:
s_i + s_{i+1} ≤ L − 1 − r.

**Lemma.** Let S be a set of windows inside a run a..b−1 (sections a..b) with a ∈ S, b−1 ∈ S and no two
consecutive windows both missing (FakeMMAP's "for every j ... S ∩ {j,j+1} is nonempty"). Then every section a..b
lies in some window of S, and a section lies in two windows of S exactly when it is section i+1 with i, i+1 ∈ S.
Summing the window inequalities over S:

    Σ_{j=a..b} s_j + Σ_{i, i+1 ∈ S} s_{i+1}  ≤  |S| (L − 1 − r),

and s_{i+1} ≥ α_{i+1}, so with E(S) = Σ_{i, i+1 ∈ S} α_{i+1}:

    r ≤ L − 1 − (Σ_{j=a..b} s_j + E(S)) / |S|.                                   (*)

Each term is (*) with a lower bound for Σ_{j=a..b} s_j from one constraint, and L ≤ M (every term grows with L):

| term | windows S | sections | lower bound used | result (derived) | as written in T11502 |
|---|---|---|---|---|---|
| 1 | {i} | i, i+1 | s ≥ α | M − 1 − α_i − α_{i+1} | same |
| 2 | ⊂ {0..N−1}, ∋ 0, N−1 | 0..N | Σ_{0..N} s = L − N | ((\|S\|−1)M + (N−\|S\|) − E(S)) / \|S\| | ((\|S\|−1)M − (N−\|S\|) + Σα) / \|S\| |
| 3 | ⊂ {0..N−2}, ∋ 0, N−2 | 0..N−1 | L − N − s_N ≥ A − N | M − (A − (N−\|S\|) + E(S)) / \|S\| | same |
| 4 | ⊂ {1..N−1}, ∋ 1, N−1 | 1..N | L − N − s_0 ≥ B − N | M − (B − (N−\|S\|) + E(S)) / \|S\| | same |
| 5 | ⊂ {1..N−2}, ∋ 1, N−2 | 1..N−1 | L − N − s_0 − s_N ≥ C − N | M − (C − (N−\|S\|) + E(S)) / \|S\| | same |

(Terms 3–5: M − 1 − (X − N + E)/|S| = M − (X − (N − |S|) + E)/|S|.)

So:

- **Term 5 is the middle block, sections 1..N−1, the constraint L − s_0 − s_N ≥ C.** The windows that avoid both
  end sections are 1..N−2, exactly FakeMMAP's "subsets of {1,...,N-2} and C in place of A". For N = 2 there is no
  such window, so the family is empty: "if N=2, you should just discard this constraint". C is the subset's
  shortest linear HTR, as FakeMMAP defined it. Nothing in the derivation needs a NISS HTR.
- Term 3 is A (drops the last section, windows 0..N−2), term 4 is B (drops the first, windows 1..N−1), term 2 the
  total length, term 1 a single window.
- **Term 2's signs.** The derivation gives +(N−|S|) − E(S); T11502 prints −(N−|S|) + Σα. T11503's first lower bound
  is the same inequality solved for M with r ≥ R': |S|(R'+1) − N + E(S) ≤ (|S|−1)M, which is exactly
  "M \geq \frac{|S|(R'+1)-N+\sum_{i edge} \alpha_i}{|S|-1}", and solving it back for R' gives the derived term 2,
  not the printed one. So T11502 and T11503 disagree with each other, and T11503 agrees with the derivation.
  Example: N = 3, α = 0, M = 11, no A/B/C limit: sections 4, 0, 0, 4 (L = 11) have reductions 6, 10, 6, so a
  6-move reduction is needed; term 2 as printed with S = {0, 2} gives (11 − 1)/2 = 5, derived (11 + 1)/2 = 6.
- **The α index.** Windows i and i+1 share section i+1 (window i = sections i, i+1; window i+1 = sections i+1,
  i+2). The section counted twice is i+1, so the sum is α_{i+1}, not α_i as printed ("the sum is over all i's such
  that i, i+1 are both in S"). This follows from term 1's indexing alone, independently of any count; it applies to
  T11502's terms 2–5 and to T11503 alike. **Confirms the published α_{i+1} correction.**

## 4. Largest or smallest term

Every term is an upper bound on r for every allowed finish, so the bound the derivation gives is the **smallest**
term: R = ⌊min⌋. T11502 says "R is the max of the following". Read as printed, R is the largest term, which is
always at least term 1 (about M − 1), so it is sufficient but very loose. Three things point to "min" being meant:
the derivation; FakeMMAP's remark that term 1 is "unlikely to be the maximum, unless M is VERY small", which is
true of the smallest term and false of the largest (on every 97th sampled state, 19,688 (state, path) cases at the
optimum: term 1 is strictly the smallest term in 11%, but at least as large as every other printed term in 90%); and "you only need to consider minimal such S's", which is what a smallest-term reading
needs (the per-S bound drops as S shrinks), not a largest-term one. The study keeps "as written" = the largest
term (FakeMMAP's words) and reports the smallest-term reading next to it.

T11503 ("we've tried all reductions of length strictly smaller than R'") is the same inequalities with r ≥ R',
solved for M; each is a valid lower bound, so there the largest one is right. Its "very stupid bounds"
M ≥ A + α_N, M ≥ B + α_0 are the A and B rows with s_N ≥ α_N, s_0 ≥ α_0.

## 5. Completeness

FakeMMAP's five families are not the whole Fourier–Motzkin projection. Combinations it leaves out: A and B together
(L − s_0 − s_N ≥ A + B − L, i.e. C can be raised to A + B − M), C with an end section (L − s_N ≥ C + α_0,
L − s_0 ≥ C + α_N), and rarer ones. They make the smallest term at most slightly loose, never too short. On
random parameter sets (N 2..6, α 0..3, M 8..15, A, B, C random) the smallest derived term was never below the exact
integer optimum; it equalled it in 98.9% of a first batch of 2,320 sets, and raising A, B, C by those combinations
first brought a batch of 3,455 sets to 99.8% (the rest 1 above the integer optimum). In the same 2,320 sets the
smallest term as printed was below the exact optimum in 37%. On the real sample the smallest derived term equals
the exact model in 99.98% of cases at the optimum (section 7).

## 6. What is computed (bounding2.py)

- R_lit: largest term, as printed (α_i). R_no1: same without term 1.
- R_min: smallest term, term 2 with the derived signs, α_{i+1}. R_min_wr: smallest term exactly as printed (to
  show the slips matter).
- R_exact: enumeration over integer sections with α, L ≤ M, A, B, and C (N > 2). LB_exact: the shortest L with a
  finish whose every reduction is ≥ R'.
- Tried and dropped (our own addition, not FakeMMAP's): C also for N = 2, and for every middle section j,
  L − s_j ≥ the state's shortest NISS HTR (prefix + suffix skipping section j is a NISS HTR of X). Valid, but at the
  optimum it lowered R in 0.9% of (state, path) cases and the mean R by 0.01 (8.891 → 8.880), so not useful.

## 7. Results on the sample (bound2.tsv, 25,000 states per subset × edges, size-weighted)

Sufficiency, every (state, path, target) case, targets optimal, +1, M = 10, 11, 12: the largest term as written,
the same without term 1, the smallest derived term and the corrected exact model are **never too short** (0 cases
at every target). The smallest term with term 2 and α exactly as printed is too short in 9.2% of cases at the
optimum (8.7–9.8% at the other targets). Witness (W14, replayed by witness.py): 0c3 2e state #1489, optimal 14,
every optimal finish on 0c3 > 4a2 > 4a1 > HTR, N = 3, α = 0,3,3,0, A = B = 11, C = 9, sections 2,3,3,3 (or 3,3,3,2),
reductions 8,7,7 / 7,7,8, so 7 needed; term 2 printed with S = {0,2}: (14 − 1)/2 = 6.5 → 6; derived (14 + 1)/2 =
7.5 → 7.

At the optimum (path known), mean R: largest term 12.14, without term 1 11.14, smallest term 8.891, exact 8.891
(the smallest term equals the exact model in 99.98% of cases), smallest term as printed 8.17; needed 6.97, max 14.
Path unknown: 12.72 / 12.40 / 10.58 / 10.57; longest need per subset × edges 11.15 on average.

Withdrawn numbers for comparison (exact model with the wrong middle-section family and C = the state's NISS HTR):
exact 8.896 at the optimum, 10.57 path unknown; the linear-C version of that wrong family was too short in 0.1%.
The corrected model gives practically the same means (8.891, 10.57) because the wrong family and the right one
bind rarely; the difference is in which statement about C is true.

T11503 at the optimum, 1,914,809 (state, path) cases: as written (α_i) the bounds exceed the optimum in 923 cases
(904 the first bound, 19 the B one; subsets 0c4, 4b2, 4c3, 4c4; witness W13), with α_{i+1} in 0 (`out/checks/
t11503_counts.txt`). Typical corrected bound (`out/q9_lb_values.tsv`, now with C the subset's linear minimum; it
used the state's NISS HTR before): median M ≥ 13 on 0c3; 12 on 2c5, 4a2, 0c4, 4c4; 11 on 2c4, 2c3, 4c3, 4b5; 10 on
4a1; 9 on 4b2; 8 on 0c0. Changes against the withdrawn table: 0c4 11 → 12, 4b2 10 → 9, 4b5 12 → 11 (medians).

rodneykinney's table (A = B = C = the subset's linear minimum): the exact column changed in 4 of 141 cells (0c0 6e
M = 10: 7 → 6; 2c5 0e and 2c5 8e M = 11: 8 → 7; 0c3 4e M = 11: 4 → 3); never below the longest need.


## 8. Interpretive choices that remain

1. **Largest vs smallest term** (section 4). "As written" in the study is the largest term; the smallest is the
   derivation's bound.
2. **Term 2's signs** taken from T11503 (section 3) for the smallest-term reading.
3. **α_{i+1}** in every sum (section 3), for the smallest-term reading and the corrected T11503 bounds; the
   "as written" columns keep α_i.
4. **A and B are linear** ("Optimal HTR on normal/inverse" read as the shortest linear HTR on that side).
5. **C is per subset × bad edges** (FakeMMAP's examples name the edges: 2c3 2e, 4b2 0e), the shortest linear HTR
   over all states with that label.
6. **α_i per corner path**: fewest half turns section i needs over every corner arrangement following the path, path
   read on normal, corners only (edges could force more; using only corners keeps α a valid lower bound).
7. **N = 2: C dropped**, as FakeMMAP says; the constraint is still true (s_1 ≥ C − 2) but was only tried in the
   dropped variant of section 6.
8. **The reduction is the one around a single quarter turn** (prefix on normal, suffix on inverse), length
   L − 1 − s_i − s_{i+1}; a solver searching every reduction of at most R moves finds it.
9. **"M moves (or less)"**: R is taken over L ≤ M; all terms grow with M, so L = M is the worst case.
10. **Rounding**: R = ⌊term⌋, lower bounds ⌈term⌉.
11. FakeMMAP's practical advice (use C+1, A+1, B+1 after going through the optimal HTRs) is not modelled.

## 9. Re-read against FakeMMAP's text (12 Nov 2026)

Checked once more, phrase by phrase, against T11501–T11504:

- "Numbering these sections from 0 to N" and "4a3 2e would have \alpha_1=3, because you have to to the 4b2 parity
  fix": section 0 is before the first quarter turn, section 1 after it, as in the model.
- Term 1 "M-\alpha_i-\alpha_{i+1}-1 (basically leaving those two as the 1q finish ...)": window i = sections i, i+1.
- Terms 2–5: the index sets {0..N−1}, {0..N−2}, {1..N−1}, {1..N−2}, "0 and N-1 are contained in it", "for every
  j ... S ∩ {j,j+1} is nonempty", match the window runs of section 3; "Same as above" in term 5 is term 4's form with
  C, matching the derived term 5 exactly; "if N=2, you should just discard this constraint" matches the empty
  window set.
- "C in place of A" with C = "the shortest possible HTR in the subset (so 2c3 2e would have C=5, 4b2 0e would have
  C=6)": the subset's linear minimum, which the middle-block constraint needs. No NISS anywhere.
- T11503 "M \geq 1+R'+\frac{A-N+\sum_{i edge} \alpha_i}{|S|}", "similar for B and C": the derived bounds.

Remaining interpretive choices are the list in section 8; the two that change numbers are 1 (largest vs smallest
term) and 2–3 (term 2's signs and the α index, which only matter under the smallest-term reading or for T11503).
