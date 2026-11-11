// drq.c — look up one or more DR states: subset, HTR lengths, every lower bound of the ladder (normal and inverse side),
// and the exact optimal DR finish (from the full table on disk).
// Input, one state per line on stdin:   20 numbers  c0..c7 e0..e7 s0..s3   (piece at each position, see drcore.h)
//                              or      a sequence of DR moves (applied to the solved cube), e.g.  U R2 U' F2 ...
// Output: one line of key=value pairs per state.
#include "drspec.h"
#include <fcntl.h>
#include <unistd.h>
#include <ctype.h>
#define ROW 483840ULL
#define MAXD 19
static uint16_t *cclass; static uint8_t *csymto; static uint8_t s_to12[NS];
static int fd[MAXD];
static int exact_depth(int c, int e, int s) {
    int k = cclass[c], S = csymto[c];
    uint64_t j = (uint64_t)k * ROW + (uint64_t)esym[S][e] * 12 + s_to12[ssym[S][s]];
    for (int d = 0; d < MAXD; d++) { uint8_t b; if (pread(fd[d], &b, 1, (off_t)(j >> 3)) != 1) return -1; if (b >> (j & 7) & 1) return d; }
    return -1;
}
int main(int argc, char **argv) {
    const char *dir = "/data/fmc/research/data/drbfs", *tab = "/data/fmc/research/data/tables";
    dr_init(); drclass_init(); e630_init(); specs_init(0, tab);
    cclass = malloc(2 * NC); csymto = malloc(NC);
    for (int c = 0; c < NC; c++) cclass[c] = 0xFFFF;
    int nclass = 0;
    for (int c = 0; c < NC; c++) { if (cclass[c] != 0xFFFF) continue; for (int S = 0; S < NSYM; S++) { int d = csym[S][c]; if (cclass[d] == 0xFFFF) { cclass[d] = nclass; csymto[d] = sym_inv[S]; } } nclass++; }
    { int n[2] = {0, 0}; for (int s = 0; s < NS; s++) s_to12[s] = n[spar[s]]++; }
    char fn[512]; for (int d = 0; d < MAXD; d++) { snprintf(fn, sizeof fn, "%s/depth_%02d.bits", dir, d); fd[d] = open(fn, O_RDONLY); if (fd[d] < 0) { fprintf(stderr, "missing %s\n", fn); return 1; } }
    uint8_t *clen = SPECS[1].T;   // rung "c": corner-only optimal length (40320 entries)
    char line[4096];
    while (fgets(line, sizeof line, stdin)) {
        St g = ST_ID; int nums[20], n = 0; char *p = line;
        while (*p && isspace((unsigned char)*p)) p++;
        if (!*p) continue;
        if (isdigit((unsigned char)*p)) {
            while (n < 20) { char *q; long v = strtol(p, &q, 10); if (q == p) break; nums[n++] = v; p = q; }
            if (n != 20) { printf("error=need 20 numbers\n"); continue; }
            for (int i = 0; i < 8; i++) { g.c[i] = nums[i]; g.e[i] = nums[8 + i]; } for (int i = 0; i < 4; i++) g.s[i] = nums[16 + i];
        } else {
            int mv[512]; int k = parse_moves(line, mv, 512); if (k < 0) { printf("error=not a DR move sequence\n"); continue; }
            for (int i = 0; i < k; i++) g = st_move(g, mv[i]);
        }
        int c = rank_n(g.c, 8), e = rank_n(g.e, 8), s = rank_n(g.s, 4);
        St gi = st_inv(g); int ci = rank_n(gi.c, 8), ei = rank_n(gi.e, 8);
        int par = spar[s];
        if ((cpar[c] ^ epar[e]) != par) { printf("error=parity: not a reachable DR state\n"); continue; }
        int a = ccos[c], b = epat[e], ai = ccos[ci], bi = epat[ei];
        printf("subset=%s corners_normal=%s corners_inverse=%s bad_corners=%d bad_edges=%d qt_corners=%d qt_min=%d E_parity=%s htr_normal=%d htr_inverse=%d corner_len=%d",
            sub48_name[sub48[a][b]], SUBSET_NAME[cc_subset[a]], SUBSET_NAME[cc_subset[ai]], cc_nbad[a], ep_nbad[b], cc_qt[a], qt_full[a][b], par ? "odd" : "even",
            htr_dist[a][b], htr_dist[ai][bi], clen[c]);
        int best = 0;
        for (int i = 0; i < NSPEC; i++) {
            Spec *S = &SPECS[i];
            int bn = S->T[sidx(S, S->cmap[c], S->emap[e], par)], bI = S->T[sidx(S, S->cmap[ci], S->emap[ei], par)];
            printf(" %s=%d/%d", S->name, bn, bI); if (bn > best) best = bn; if (bI > best) best = bI;
        }
        { Spec *K = spec_by_name("KF"); printf(" kfclass=%zu", sidx(K, K->cmap[c], K->emap[e], par)); }
        printf(" best_bound=%d exact=%d\n", best, getenv("DRQ_NOEXACT") ? -1 : exact_depth(c, e, s));
        fflush(stdout);
    }
    return 0;
}
