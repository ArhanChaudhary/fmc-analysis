// drparity.c — the "E-slice parity rule": L = optimal corner length, Lp = optimal corner length among corner solutions
// whose number of side half turns has the parity of the E-slice permutation.  Distribution of Lp - L per corner subset.
#include "drspec.h"
int main(void) {
    dr_init(); drclass_init(); e630_init(); specs_init(0, "/data/fmc/judging-a-dr/research/data/tables");
    Spec *A = spec_by_name("c"), *B = spec_by_name("c+p");
    long h[NSUBSET][8] = {{0}}, hl[NSUBSET][16][8] = {{{0}}};
    for (int c = 0; c < NC; c++) for (int p = 0; p < 2; p++) {
        int L = A->T[sidx(A, c, 0, 0)], Lp = B->T[sidx(B, c, 0, p)];
        h[cc_subset[ccos[c]]][Lp - L]++; hl[cc_subset[ccos[c]]][L][Lp - L]++;
    }
    printf("corner subset: share of (corner state, E parity) pairs with Lp-L = 0,1,2,3,...   [wrong-parity cost: Lp(other parity) - L]\n");
    for (int s = 0; s < NSUBSET; s++) { long t = 0; for (int k = 0; k < 8; k++) t += h[s][k];
        printf("  %s:", SUBSET_NAME[s]); for (int k = 0; k < 8; k++) if (h[s][k]) printf("  +%d: %.1f%%", k, 100.0 * h[s][k] / t); printf("\n"); }
    // for each corner state: which parity is the cheap one, and the extra cost of the other
    long d[NSUBSET][8] = {{0}};
    for (int c = 0; c < NC; c++) { int a = B->T[sidx(B, c, 0, 0)], b = B->T[sidx(B, c, 0, 1)]; int x = a > b ? a - b : b - a; d[cc_subset[ccos[c]]][x]++; }
    printf("corner subset: |Lp(even) - Lp(odd)| distribution over corner states\n");
    for (int s = 0; s < NSUBSET; s++) { long t = 0; for (int k = 0; k < 8; k++) t += d[s][k];
        printf("  %s:", SUBSET_NAME[s]); for (int k = 0; k < 8; k++) if (d[s][k]) printf("  %d: %.1f%%", k, 100.0 * d[s][k] / t); printf("\n"); }
    return 0;
}
