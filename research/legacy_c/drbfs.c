// drbfs.c — exact optimal length (DR moves, HTM) of every state of the DR group <U,D,R2,L2,F2,B2>.
// 19,508,428,800 states, reduced by the 16 symmetries that keep the U/D axis; one bit per reduced state and per depth.
// Memory: three bitsets of nclass*60480 bytes (~167 MB each). Each depth's frontier is written to <outdir>/depth_XX.bits.
//
// Reduced index: (class, e, s12)  with  class = symmetry class of the corner permutation (representative = smallest rank),
// e = U/D-edge permutation rank, s12 = rank of the E-slice permutation among the 12 with the parity forced by corners/edges.
// If a class representative has a non-trivial stabiliser, every (e, s) image under the stabiliser is marked, so that
// "number of states at depth d" = sum over set bits of 16/|stabiliser|.
#include "drcore.h"
#include <omp.h>
#include <sys/stat.h>

static uint16_t *cclass; static uint8_t *csymto; static int nclass; static int *crep;
static uint8_t (*stab)[NSYM]; static uint8_t *nstab;
static uint8_t s_to12[NS], s_from12[2][12];
#define ROW 483840ULL   /* 40320 * 12 */

int main(int argc, char **argv) {
    const char *outdir = argc > 1 ? argv[1] : "/data/fmc/research/data/drbfs";
    mkdir(outdir, 0755);
    dr_init();
    cclass = malloc(2 * NC); csymto = malloc(NC); crep = malloc(sizeof(int) * NC);
    for (int c = 0; c < NC; c++) cclass[c] = 0xFFFF;
    nclass = 0;
    for (int c = 0; c < NC; c++) {
        if (cclass[c] != 0xFFFF) continue;        // c is the smallest of its orbit because we scan upward
        crep[nclass] = c;
        for (int S = 0; S < NSYM; S++) { int d = csym[S][c]; if (cclass[d] == 0xFFFF) { cclass[d] = nclass; csymto[d] = sym_inv[S]; } }
        nclass++;
    }
    for (int c = 0; c < NC; c++) if (csym[csymto[c]][c] != crep[cclass[c]]) { fprintf(stderr, "sym table broken\n"); return 1; }
    stab = malloc((size_t)nclass * NSYM); nstab = calloc(nclass, 1);
    for (int k = 0; k < nclass; k++) for (int S = 0; S < NSYM; S++) if (csym[S][crep[k]] == crep[k]) stab[k][nstab[k]++] = S;
    { int n[2] = {0, 0}; for (int s = 0; s < NS; s++) { s_to12[s] = n[spar[s]]; s_from12[spar[s]][n[spar[s]]++] = s; } }
    uint64_t N = (uint64_t)nclass * ROW, NW = (N + 63) / 64;
    fprintf(stderr, "corner symmetry classes: %d ; reduced states: %llu ; bitset %.1f MB\n", nclass, (unsigned long long)N, NW * 8 / 1e6);
    uint64_t *vis = calloc(NW, 8), *cur = calloc(NW, 8), *nxt = calloc(NW, 8);
    if (!vis || !cur || !nxt) { fprintf(stderr, "out of memory\n"); return 1; }
    // per class: for each move, target class and the symmetry bringing the moved corner perm to its representative
    uint16_t (*mcl)[NMOVES] = malloc((size_t)nclass * sizeof *mcl); uint8_t (*msy)[NMOVES] = malloc((size_t)nclass * sizeof *msy);
    for (int k = 0; k < nclass; k++) for (int m = 0; m < NMOVES; m++) { int c2 = cmove[m][crep[k]]; mcl[k][m] = cclass[c2]; msy[k][m] = csymto[c2]; }

    #define SETBIT(a, i) __atomic_fetch_or(&(a)[(i) >> 6], 1ULL << ((i) & 63), __ATOMIC_RELAXED)
    {   // depth 0: the solved state (class of identity, e = 0, s = 0)
        uint64_t i0 = (uint64_t)cclass[0] * ROW + 0 * 12 + s_to12[0];
        vis[i0 >> 6] |= 1ULL << (i0 & 63); cur[i0 >> 6] |= 1ULL << (i0 & 63);
    }
    char fn[512]; FILE *log; snprintf(fn, sizeof fn, "%s/counts.txt", outdir); log = fopen(fn, "w");
    unsigned long long total = 0;
    for (int depth = 0;; depth++) {
        // count + save current frontier
        unsigned long long cnt = 0, bits = 0;
        #pragma omp parallel for reduction(+:cnt, bits) schedule(dynamic, 16)
        for (int k = 0; k < nclass; k++) {
            uint64_t lo = (uint64_t)k * ROW, hi = lo + ROW; unsigned long long b = 0;
            for (uint64_t i = lo; i < hi;) {
                if ((i & 63) == 0 && i + 64 <= hi) { b += __builtin_popcountll(cur[i >> 6]); i += 64; }
                else { b += cur[i >> 6] >> (i & 63) & 1; i++; }
            }
            bits += b; cnt += b * (16 / nstab[k]);
        }
        if (cnt == 0) break;
        total += cnt;
        fprintf(stderr, "depth %2d: %llu states (%llu reduced) total %llu\n", depth, cnt, bits, total);
        fprintf(log, "%d %llu %llu\n", depth, cnt, bits); fflush(log);
        snprintf(fn, sizeof fn, "%s/depth_%02d.bits", outdir, depth);
        FILE *f = fopen(fn, "wb"); fwrite(cur, 8, NW, f); fclose(f);
        // expand
        #pragma omp parallel for schedule(dynamic, 4)
        for (int k = 0; k < nclass; k++) {
            int c = crep[k]; uint64_t base = (uint64_t)k * ROW;
            for (int e = 0; e < NE; e++) {
                uint64_t i = base + (uint64_t)e * 12;
                uint64_t w = cur[i >> 6] >> (i & 63);
                if ((i & 63) > 52) w |= cur[(i >> 6) + 1] << (64 - (i & 63));
                w &= 0xFFF;
                if (!w) continue;
                int par = cpar[c] ^ epar[e];
                while (w) {
                    int s12 = __builtin_ctzll(w); w &= w - 1;
                    int s = s_from12[par][s12];
                    for (int m = 0; m < NMOVES; m++) {
                        int k2 = mcl[k][m], S = msy[k][m];
                        int e2 = esym[S][emove[m][e]], s2 = ssym[S][smove[m][s]];
                        uint64_t j = (uint64_t)k2 * ROW + (uint64_t)e2 * 12 + s_to12[s2];
                        if (vis[j >> 6] >> (j & 63) & 1) continue;
                        SETBIT(vis, j); SETBIT(nxt, j);
                        for (int t = 1; t < nstab[k2]; t++) {   // stab[k2][0] is the identity
                            int T = stab[k2][t];
                            uint64_t j2 = (uint64_t)k2 * ROW + (uint64_t)esym[T][e2] * 12 + s_to12[ssym[T][s2]];
                            SETBIT(vis, j2); SETBIT(nxt, j2);
                        }
                    }
                }
            }
        }
        uint64_t *t = cur; cur = nxt; nxt = t; memset(nxt, 0, NW * 8);
    }
    fprintf(stderr, "total %llu (expected 19508428800)\n", total);
    fprintf(log, "total %llu\n", total); fclose(log);
    // save the class tables so later passes agree on the indexing
    snprintf(fn, sizeof fn, "%s/classes.bin", outdir);
    FILE *f = fopen(fn, "wb"); fwrite(&nclass, 4, 1, f); fwrite(crep, 4, nclass, f); fwrite(nstab, 1, nclass, f); fclose(f);
    return total == 19508428800ULL ? 0 : 2;
}
