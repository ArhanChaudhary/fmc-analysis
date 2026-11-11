// t_quot.c — build the KF / K0 tables and check the half-turn-only restriction against FakeMMAP's 216-case BFS listing.
#include "drquot.h"
int main(int argc, char **argv) {
    dr_init(); drclass_init(); e630_init();
    Quot QF, Q0; quot_init(&QF, 1); quot_init(&Q0, 0);
    for (int w = 0; w < 2; w++) {
        Quot *Q = w ? &Q0 : &QF; size_t N = (size_t)Q->ncc * NE630 * 2; long h[24] = {0}, hh[24] = {0}; int mx = 0, nh = 0;
        for (size_t i = 0; i < N; i++) { h[Q->T[i]]++; if (Q->T[i] > mx) mx = Q->T[i]; if (Q->TH[i] != 0xFF) { hh[Q->TH[i]]++; nh++; } }
        printf("%s: %zu classes; DR-move distance distribution:", w ? "K0" : "KF", N); for (int k = 0; k <= mx; k++) printf(" %d:%ld", k, h[k]); printf("\n");
        printf("   half-turn-only component: %d classes:", nh); for (int k = 0; k < 24; k++) if (hh[k]) printf(" %d:%ld", k, hh[k]); printf("\n");
        // does allowing quarter turns shorten any HTR-class?
        int shorter = 0; for (size_t i = 0; i < N; i++) if (Q->TH[i] != 0xFF && Q->T[i] < Q->TH[i]) shorter++;
        printf("   HTR classes whose distance drops when quarter turns are allowed: %d\n", shorter);
    }
    // FakeMMAP's listing: "<case>: <n> Example scramble: <half turns>"
    const char *fn = argc > 1 ? argv[1] : "/data/fmc/assets/attachments/1546077758189477989_0_message.txt";
    FILE *f = fopen(fn, "r"); char line[512]; int n = 0, okH = 0, okDR = 0; static uint8_t seen[5040 * 630 * 2]; int distinct = 0;
    while (f && fgets(line, sizeof line, f)) {
        char *col = strstr(line, "parity: "); if (!col) continue;
        int val = atoi(col + 8); char *sc = strstr(line, "scramble:"); if (!sc) continue;
        int mv[64]; int k = parse_moves(sc + 9, mv, 64);
        St g = ST_ID; for (int i = 0; i < k; i++) g = st_move(g, mv[i]);
        size_t id = qidx(&QF, QF.ccls[rank_n(g.c, 8)], e630[rank_n(g.e, 8)], spar[rank_n(g.s, 4)]);
        if (!seen[id]) { seen[id] = 1; distinct++; }
        n++; if (QF.TH[id] == val) okH++; else printf("   differs: %.40s  listed %d, ours (half turns) %d\n", line, val, QF.TH[id]);
        if (QF.T[id] == val) okDR++;
    }
    printf("FakeMMAP listing: %d cases, %d distinct KF classes, half-turn-only distance equal in %d, DR-move distance equal in %d\n", n, distinct, okH, okDR);
    return 0;
}
