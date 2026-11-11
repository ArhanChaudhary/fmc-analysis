// dragg2.c — joint histogram of the exact finish length with the visible-feature lower bounds, per Mallard subset.
// Columns: subset, hmax = max(HTR length normal, inverse), bF_n / bF_i = KF bound on normal / inverse state,
//          b0 = max(K0 bound normal, inverse), depth, count.
#include "drquot.h"
#include <omp.h>
#include <fcntl.h>
#include <unistd.h>
#define ROW 483840ULL
#define ROWB 60480
#define MAXD 19
#define NB 17
int main(int argc, char **argv) {
    const char *dir = argc > 1 ? argv[1] : "/data/fmc/research/data/drbfs";
    dr_init(); drclass_init(); e630_init();
    Quot QF, Q0; quot_init(&QF, 1); quot_init(&Q0, 0);
    char fn[512]; snprintf(fn, sizeof fn, "%s/classes.bin", dir);
    FILE *f = fopen(fn, "rb"); int nclass; if (!f || fread(&nclass, 4, 1, f) != 1) return 1;
    int *crep = malloc(4 * nclass); uint8_t *nstab = malloc(nclass);
    if (fread(crep, 4, nclass, f) != (size_t)nclass || fread(nstab, 1, nclass, f) != (size_t)nclass) return 1; fclose(f);
    int fd[MAXD];
    for (int d = 0; d < MAXD; d++) { snprintf(fn, sizeof fn, "%s/depth_%02d.bits", dir, d); fd[d] = open(fn, O_RDONLY); if (fd[d] < 0) return 1; }
    size_t KEYS = (size_t)48 * 14 * NB * NB * NB * MAXD;
    int nth = omp_get_max_threads();
    uint64_t *H = calloc(KEYS * nth, 8); if (!H) { fprintf(stderr, "oom\n"); return 1; }
    long long viol = 0;
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
            int c = crep[k], ci = cinv[c], w = 16 / nstab[k];
            int a = ccos[c], ai = ccos[ci];
            for (int e = 0; e < NE; e++) {
                int ei = einv[e], b = epat[e], bi = epat[ei];
                int hn = htr_dist[a][b], hi = htr_dist[ai][bi], hm = hn > hi ? hn : hi, sub = sub48[a][b];
                int par = cpar[c] ^ epar[e];
                int fN = QF.T[qidx(&QF, QF.ccls[c], e630[e], par)], fI = QF.T[qidx(&QF, QF.ccls[ci], e630[ei], par)];
                int zN = Q0.T[qidx(&Q0, Q0.ccls[c], e630[e], par)], zI = Q0.T[qidx(&Q0, Q0.ccls[ci], e630[ei], par)];
                int z = zN > zI ? zN : zI;
                size_t base = (((((size_t)sub * 14 + hm) * NB + fN) * NB + fI) * NB + z) * MAXD;
                const uint8_t *dp = dep + (size_t)e * 12;
                for (int s12 = 0; s12 < 12; s12++) { int d = dp[s12]; if (d < z || d < fN || d < fI || d < hm) viol++; h[base + d] += w; }
            }
        }
        free(buf); free(dep);
    }
    for (int t = 1; t < nth; t++) for (size_t i = 0; i < KEYS; i++) H[i] += H[(size_t)t * KEYS + i];
    printf("subset,hmax,bFn,bFi,b0,depth,count\n");
    for (size_t i = 0; i < KEYS; i++) if (H[i]) {
        size_t x = i; int d = x % MAXD; x /= MAXD; int z = x % NB; x /= NB; int fI = x % NB; x /= NB; int fN = x % NB; x /= NB; int hm = x % 14; x /= 14;
        printf("%s,%d,%d,%d,%d,%d,%llu\n", sub48_name[x], hm, fN, fI, z, d, (unsigned long long)H[i]);
    }
    fprintf(stderr, "states where a claimed lower bound exceeds the true optimum: %lld (must be 0)\n", viol);
    return viol != 0;
}
