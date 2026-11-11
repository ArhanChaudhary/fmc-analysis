// t_class.c — self-checks of the model against numbers stated in the Discord knowledge base.
#include "drclass.h"
int main(void) {
    dr_init(); drclass_init();
    // 1. subset sizes in units of corner cosets; expected from Joba's subsets_without_edges.txt (T6677):
    //    0c0 2, 4a1 12, 4a2 12, 4b2 48, 0c3 6, 2c3 64, 4c3 48, 0c4 4, 2c4 96, 4c4 48, 2c5 32, 4c5 48  (of 420)
    int cnt[NSUBSET] = {0}; long long elems[NSUBSET] = {0};
    for (int i = 0; i < NCCOS; i++) cnt[cc_subset[i]]++;
    printf("corner subset : cosets (of 420)\n");
    for (int i = 0; i < NSUBSET; i++) printf("  %s %d\n", SUBSET_NAME[i], cnt[i]);
    printf("Mallard-style subsets found: %d (expected 48)\n", NSUB48);
    { int n[64] = {0}; for (int a = 0; a < NCCOS; a++) for (int b = 0; b < NEPAT; b++) n[sub48[a][b]]++;
      for (int k = 0; k < NSUB48; k++) printf("  %-7s cosets %5d  (%.4f%% of DR states)%s", sub48_name[k], n[k], 100.0 * n[k] / 29400, k % 3 == 2 ? "\n" : ""); printf("\n"); }
    // 2. quarter-turn class sizes; expected (Oskar, T4615): 1/210, 1/35, 1/7, 59/210, 37/105, 4/21
    int q[8] = {0}; for (int i = 0; i < NCCOS; i++) q[cc_qt[i]]++;
    printf("qt class sizes /420:"); for (int k = 0; k < 8; k++) printf(" %d", q[k]); printf("   expected 2 12 60 118 148 80\n");
    // 3. bad edges
    int be[9] = {0}; for (int i = 0; i < NEPAT; i++) be[ep_nbad[i]]++;
    printf("edge patterns by #bad edges: 0:%d 2:%d 4:%d 6:%d 8:%d\n", be[0], be[2], be[4], be[6], be[8]);
    // 4. HTR length distribution over the 29,400 cosets, and max per subset
    int hd[20] = {0}, hmax = 0; for (int a = 0; a < NCCOS; a++) for (int b = 0; b < NEPAT; b++) { hd[htr_dist[a][b]]++; if (htr_dist[a][b] > hmax) hmax = htr_dist[a][b]; }
    printf("DR->HTR optimal length over 29400 cosets:"); for (int k = 0; k <= hmax; k++) printf(" %d:%d", k, hd[k]); printf("\n");
    // 5. inverse behaviour of subsets: which subset does the inverse of an element land in?
    printf("subset -> subsets of inverses (count of elements)\n");
    for (int si = 0; si < NSUBSET; si++) {
        long long inv[NSUBSET] = {0};
        for (int c = 0; c < NC; c++) if (cc_subset[ccos[c]] == si) inv[cc_subset[ccos[cinv[c]]]]++;
        printf("  %s ->", SUBSET_NAME[si]); for (int j = 0; j < NSUBSET; j++) if (inv[j]) printf(" %s:%lld", SUBSET_NAME[j], inv[j]); printf("\n");
    }
    // 6. optimal corner-solution length in DR moves (corners only, 40320 states)
    {
        uint8_t *d = malloc(NC); memset(d, 0xFF, NC); int *qq = malloc(sizeof(int) * NC); int qh = 0, qt = 0; d[0] = 0; qq[qt++] = 0;
        while (qh < qt) { int c = qq[qh++]; for (int m = 0; m < NMOVES; m++) { int c2 = cmove[m][c]; if (d[c2] == 0xFF) { d[c2] = d[c] + 1; qq[qt++] = c2; } } }
        int h[20] = {0}, mx = 0; for (int c = 0; c < NC; c++) { h[d[c]]++; if (d[c] > mx) mx = d[c]; }
        printf("corner-only optimal length (40320 corner states, DR moves):"); for (int k = 0; k <= mx; k++) printf(" %d:%d", k, h[k]); printf("\n");
        int mxs[NSUBSET] = {0}, mns[NSUBSET]; for (int i = 0; i < NSUBSET; i++) mns[i] = 99;
        for (int c = 0; c < NC; c++) { int s = cc_subset[ccos[c]]; if (d[c] > mxs[s]) mxs[s] = d[c]; if (d[c] < mns[s]) mns[s] = d[c]; }
        printf("corner length range per subset:"); for (int i = 0; i < NSUBSET; i++) printf(" %s %d-%d", SUBSET_NAME[i], mns[i], mxs[i]); printf("\n");
    }
    // 7. symmetry sanity: subset labels and HTR distance are invariant under the 16 symmetries
    for (int c = 0; c < NC; c += 7) for (int S = 0; S < NSYM; S++) {
        if (cc_subset[ccos[csym[S][c]]] != cc_subset[ccos[c]]) { printf("subset not symmetric!\n"); return 1; }
        if (htr_dist[ccos[csym[S][c]]][epat[esym[S][c]]] != htr_dist[ccos[c]][epat[c]]) { printf("htr dist not symmetric!\n"); return 1; }
    }
    printf("symmetry invariance of labels: ok\n");
    return 0;
}
