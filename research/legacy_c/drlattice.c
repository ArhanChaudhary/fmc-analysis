// drlattice.c — a ladder of "visible feature" lower bounds for DR finishes, from coarse to fine, and how each compares
// with the exact optimum on all 19,508,428,800 DR states.
//
// Each rung is a subgroup K of the DR group described by what it lets you see:
//   corners : none | HTR coset (420) | exact up to {x2,y2,z2}x{U2} (5040) | up to {x2,y2,z2} (10080) | exact (40320)
//   edges   : none | which positions hold M-slice edges (70) | + U/D colour pattern of M and of S edges up to colour swap (630)
//             | position of the four types white-M, yellow-M, white-S, yellow-S (2520)
//   E parity: tracked or not
// T_K = BFS distance in the coset graph K\G = fewest DR moves to make the visible part look solved.
// Bound used for a state g:  max( T_K(g), T_K(g^-1) ).
#include "drquot.h"
#include <omp.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/stat.h>
#define ROW 483840ULL
#define ROWB 60480
#define MAXD 19

typedef struct { const char *name; const char *desc; int cm, em, par; int nc, ne; const uint16_t *cmap, *emap; uint16_t *cmv, *emv; uint8_t *T; size_t N; } Spec;
enum { C_NONE, C_HTR, C_VU2, C_V, C_EXACT };
enum { E_NONE, E_MASK, E_630, E_2520, E_630S, E_2520S };

static uint16_t *map_none, *map_exact, *map_ccos16, *map_epat16, *e2520, *e630s, *e2520s; static int n2520;

static void build_moves(Spec *S) {
    // move tables on classes via representatives, then verify on every element
    int *crep = malloc(sizeof(int) * S->nc), *erep = malloc(sizeof(int) * S->ne);
    for (int i = 0; i < S->nc; i++) crep[i] = -1;
    for (int i = 0; i < S->ne; i++) erep[i] = -1;
    for (int c = 0; c < NC; c++) { if (crep[S->cmap[c]] < 0) crep[S->cmap[c]] = c; if (erep[S->emap[c]] < 0) erep[S->emap[c]] = c; }
    S->cmv = malloc((size_t)S->nc * NMOVES * 2); S->emv = malloc((size_t)S->ne * NMOVES * 2);
    for (int i = 0; i < S->nc; i++) for (int m = 0; m < NMOVES; m++) S->cmv[i * NMOVES + m] = S->cmap[cmove[m][crep[i]]];
    for (int i = 0; i < S->ne; i++) for (int m = 0; m < NMOVES; m++) S->emv[i * NMOVES + m] = S->emap[emove[m][erep[i]]];
    for (int c = 0; c < NC; c++) for (int m = 0; m < NMOVES; m++) {
        if (S->cmap[cmove[m][c]] != S->cmv[S->cmap[c] * NMOVES + m] || S->emap[emove[m][c]] != S->emv[S->emap[c] * NMOVES + m]) { fprintf(stderr, "%s: class action not well defined\n", S->name); exit(1); }
    }
    free(crep); free(erep);
}
static inline size_t sidx(const Spec *S, int cc, int ee, int par) { return ((size_t)cc * S->ne + ee) * (S->par ? 2 : 1) + (S->par ? par : 0); }
static void bfs(Spec *S) {
    int P = S->par ? 2 : 1;
    S->N = (size_t)S->nc * S->ne * P; S->T = malloc(S->N); memset(S->T, 0xFF, S->N);
    S->T[sidx(S, S->cmap[0], S->emap[0], 0)] = 0;
    for (int d = 0;; d++) {
        size_t found = 0;
        #pragma omp parallel for reduction(+:found) schedule(dynamic, 64)
        for (int cc = 0; cc < S->nc; cc++) for (int ee = 0; ee < S->ne; ee++) for (int p = 0; p < P; p++) {
            if (S->T[sidx(S, cc, ee, p)] != d) continue;
            for (int m = 0; m < NMOVES; m++) {
                size_t j = sidx(S, S->cmv[cc * NMOVES + m], S->emv[ee * NMOVES + m], p ^ (m >= 6));
                if (S->T[j] == 0xFF) { S->T[j] = d + 1; found++; }
            }
        }
        if (!found) break;
    }
}

int main(int argc, char **argv) {
    const char *dir = argc > 1 ? argv[1] : "/data/fmc/research/data/drbfs";
    const char *outdir = argc > 2 ? argv[2] : "/data/fmc/research/data/tables";
    mkdir(outdir, 0755);
    dr_init(); drclass_init(); e630_init();
    Quot QF, Q0; quot_init(&QF, 1); quot_init(&Q0, 0);
    map_none = calloc(NC, 2); map_exact = malloc(2 * NC); map_ccos16 = ccos; map_epat16 = malloc(2 * NC); e2520 = malloc(2 * NC);
    for (int c = 0; c < NC; c++) { map_exact[c] = c; map_epat16[c] = epat[c]; }
    { static int idx[1 << 16]; memset(idx, -1, sizeof idx); n2520 = 0;
      for (int e = 0; e < NE; e++) { uint8_t p[8]; unrank_n(e, 8, p); int key = 0; for (int k = 0; k < 8; k++) key |= (((p[k] & 1) << 1) | (p[k] >> 2)) << (2 * k);
        if (idx[key] < 0) idx[key] = n2520++; e2520[e] = idx[key]; }
      if (n2520 != 2520) { fprintf(stderr, "2520 classes expected, got %d\n", n2520); return 1; } }
    // sign-split refinements: sM / sS = parity of the arrangement of the four M-slice (S-slice) edges read in position order.
    // Together with the corner class they carry FakeMMAP's "F-parity / R-parity" (the double-swap or H-perm parity, T12070, doc 428).
    e630s = malloc(2 * NC); e2520s = malloc(2 * NC);
    for (int e = 0; e < NE; e++) { uint8_t p[8], sq[2][4]; int n[2] = {0, 0}; unrank_n(e, 8, p);
        for (int k = 0; k < 8; k++) { int t = p[k] & 1; sq[t][n[t]++] = p[k] >> 1; }
        int sg[2]; for (int t = 0; t < 2; t++) { int inv = 0; for (int i = 0; i < 4; i++) for (int j = i + 1; j < 4; j++) if (sq[t][i] > sq[t][j]) inv++; sg[t] = inv & 1; }
        e630s[e] = e630[e] * 4 + sg[0] * 2 + sg[1]; e2520s[e] = e2520[e] * 4 + sg[0] * 2 + sg[1]; }
    Spec specs[] = {
        {"htr",        "HTR coset only (optimal DR->HTR length)",                         C_HTR, E_MASK, 0},
        {"c",          "corners exact, edges ignored (optimal corner solution length L)",  C_EXACT, E_NONE, 0},
        {"c+p",        "corners exact + E-slice parity",                                  C_EXACT, E_NONE, 1},
        {"e630+p",     "edges only: bad-edge positions + colour patterns + E parity",     C_NONE, E_630, 1},
        {"c+bad",      "corners exact + which edges are bad",                             C_EXACT, E_MASK, 0},
        {"c+bad+p",    "corners exact + which edges are bad + E parity",                  C_EXACT, E_MASK, 1},
        {"KF",         "FakeMMAP/Rodney features: corners up to rotation and U2, 630 edge classes, E parity", C_VU2, E_630, 1},
        {"K0",         "same without U2",                                                 C_V, E_630, 1},
        {"c+630+p",    "corners exact + 630 edge classes + E parity",                     C_EXACT, E_630, 1},
        {"c+2520+p",   "corners exact + layer and slice type of every U/D edge + E parity", C_EXACT, E_2520, 1},
        {"K0+F",       "K0 + double-swap parity (generalises FakeMMAP's OBL++ sheet)",    C_V, E_630S, 0},
        {"c+630+F",    "corners exact + 630 edge classes + double-swap parity",           C_EXACT, E_630S, 0},
        {"c+2520+F",   "corners exact + layer/slice type of every U/D edge + double-swap parity", C_EXACT, E_2520S, 0},
    };
    int nspec = sizeof specs / sizeof specs[0];
    for (int i = 0; i < nspec; i++) {
        Spec *S = &specs[i];
        switch (S->cm) { case C_NONE: S->cmap = map_none; S->nc = 1; break; case C_HTR: S->cmap = map_ccos16; S->nc = NCCOS; break;
            case C_VU2: S->cmap = QF.ccls; S->nc = QF.ncc; break; case C_V: S->cmap = Q0.ccls; S->nc = Q0.ncc; break; default: S->cmap = map_exact; S->nc = NC; }
        switch (S->em) { case E_NONE: S->emap = map_none; S->ne = 1; break; case E_MASK: S->emap = map_epat16; S->ne = NEPAT; break;
            case E_630: S->emap = e630; S->ne = NE630; break; case E_2520: S->emap = e2520; S->ne = n2520; break;
            case E_630S: S->emap = e630s; S->ne = NE630 * 4; break; default: S->emap = e2520s; S->ne = 2520 * 4; }
        build_moves(S); bfs(S);
        long h[24] = {0}; int mx = 0; for (size_t k = 0; k < S->N; k++) { if (S->T[k] == 0xFF) continue; h[S->T[k]]++; if (S->T[k] > mx) mx = S->T[k]; }
        fprintf(stderr, "%-9s %10ld classes (of %zu indexed), max %2d :", S->name, ({long t=0; for(int k=0;k<24;k++) t+=h[k]; t;}), S->N, mx); for (int k = 0; k <= mx; k++) fprintf(stderr, " %ld", h[k]); fprintf(stderr, "\n");
        char fn[512]; snprintf(fn, sizeof fn, "%s/T_%s.u8", outdir, S->name); FILE *f = fopen(fn, "wb"); fwrite(S->T, 1, S->N, f); fclose(f);
    }
    // sanity: rung "htr" must equal the HTR distance table
    for (int a = 0; a < NCCOS; a++) for (int b = 0; b < NEPAT; b++) if (specs[0].T[sidx(&specs[0], a, b, 0)] != htr_dist[a][b]) { fprintf(stderr, "htr rung mismatch\n"); return 1; }

    // ---- aggregate against exact distances
    char fn[512]; snprintf(fn, sizeof fn, "%s/classes.bin", dir);
    FILE *f = fopen(fn, "rb"); int nclass; if (!f || fread(&nclass, 4, 1, f) != 1) return 1;
    int *crep = malloc(4 * nclass); uint8_t *nstab = malloc(nclass);
    if (fread(crep, 4, nclass, f) != (size_t)nclass || fread(nstab, 1, nclass, f) != (size_t)nclass) return 1; fclose(f);
    int fd[MAXD];
    for (int d = 0; d < MAXD; d++) { snprintf(fn, sizeof fn, "%s/depth_%02d.bits", dir, d); fd[d] = open(fn, O_RDONLY); if (fd[d] < 0) return 1; }
    size_t KEYS = (size_t)nspec * 2 * 48 * MAXD * MAXD;      // [spec][one-sided(0)/two-sided(1)][subset][bound][depth]
    int nth = omp_get_max_threads(); uint64_t *H = calloc(KEYS * nth, 8); long long viol = 0;
    #pragma omp parallel reduction(+:viol)
    {
        uint64_t *h = H + (size_t)omp_get_thread_num() * KEYS;
        uint8_t *buf = malloc(ROWB), *dep = malloc(ROW);
        #pragma omp for schedule(dynamic, 8)
        for (int k = 0; k < nclass; k++) {
            memset(dep, 0xFF, ROW);
            for (int d = 0; d < MAXD; d++) {
                if (pread(fd[d], buf, ROWB, (off_t)k * ROWB) != ROWB) exit(1);
                for (int b = 0; b < ROWB; b++) { uint8_t x = buf[b]; while (x) { int t = __builtin_ctz(x); x &= x - 1; dep[(size_t)b * 8 + t] = d; } }
            }
            int c = crep[k], ci = cinv[c], w = 16 / nstab[k], a = ccos[c];
            for (int e = 0; e < NE; e++) {
                int ei = einv[e], sub = sub48[a][epat[e]], par = cpar[c] ^ epar[e];
                const uint8_t *dp = dep + (size_t)e * 12;
                uint32_t cnt[MAXD] = {0};
                for (int s12 = 0; s12 < 12; s12++) cnt[dp[s12]]++;
                for (int i = 0; i < nspec; i++) {
                    const Spec *S = &specs[i];
                    int bn = S->T[sidx(S, S->cmap[c], S->emap[e], par)], bi = S->T[sidx(S, S->cmap[ci], S->emap[ei], par)], b2 = bn > bi ? bn : bi;
                    if (bn == 0xFF || bi == 0xFF) { fprintf(stderr, "reached an unvisited class in %s\n", S->name); exit(1); }
                    size_t b1k = ((((size_t)i * 2 + 0) * 48 + sub) * MAXD + bn) * MAXD, b2k = ((((size_t)i * 2 + 1) * 48 + sub) * MAXD + b2) * MAXD;
                    for (int d = 0; d < MAXD; d++) if (cnt[d]) { if (d < b2) viol++; h[b1k + d] += (uint64_t)cnt[d] * w; h[b2k + d] += (uint64_t)cnt[d] * w; }
                }
            }
        }
        free(buf); free(dep);
    }
    for (int t = 1; t < nth; t++) for (size_t i = 0; i < KEYS; i++) H[i] += H[(size_t)t * KEYS + i];
    printf("spec,sides,subset,bound,depth,count\n");
    for (size_t i = 0; i < KEYS; i++) if (H[i]) {
        size_t x = i; int d = x % MAXD; x /= MAXD; int b = x % MAXD; x /= MAXD; int sub = x % 48; x /= 48; int two = x % 2; x /= 2;
        printf("%s,%d,%s,%d,%d,%llu\n", specs[x].name, two + 1, sub48_name[sub], b, d, (unsigned long long)H[i]);
    }
    fprintf(stderr, "bound violations: %lld (must be 0)\n", viol);
    return viol != 0;
}
