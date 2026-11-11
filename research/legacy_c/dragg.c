// dragg.c — one pass over the exact distance data: histogram of optimal finish length by
// (Mallard subset, 4a/4b letter on the normal side, HTR length normal, HTR length inverse, corner-only length, E-slice parity).
// Output: CSV with one line per non-empty cell.  Weights are 16/|stabiliser| so that counts are numbers of DR states.
#include "drclass.h"
#include <omp.h>
#include <fcntl.h>
#include <unistd.h>
#define ROW 483840ULL
#define ROWB 60480
#define MAXD 19
#define NH 14
#define NL 14
int main(int argc, char **argv) {
    const char *dir = argc > 1 ? argv[1] : "/data/fmc/research/data/drbfs";
    dr_init(); drclass_init();
    char fn[512]; snprintf(fn, sizeof fn, "%s/classes.bin", dir);
    FILE *f = fopen(fn, "rb"); int nclass; if (!f || fread(&nclass, 4, 1, f) != 1) { fprintf(stderr, "no classes.bin\n"); return 1; }
    int *crep = malloc(4 * nclass); uint8_t *nstab = malloc(nclass);
    if (fread(crep, 4, nclass, f) != (size_t)nclass || fread(nstab, 1, nclass, f) != (size_t)nclass) return 1; fclose(f);
    int fd[MAXD];
    for (int d = 0; d < MAXD; d++) { snprintf(fn, sizeof fn, "%s/depth_%02d.bits", dir, d); fd[d] = open(fn, O_RDONLY); if (fd[d] < 0) { fprintf(stderr, "missing %s\n", fn); return 1; } }
    // corner-only optimal length
    uint8_t *clen = malloc(NC); memset(clen, 0xFF, NC);
    { int *q = malloc(sizeof(int) * NC); int qh = 0, qt = 0; clen[0] = 0; q[qt++] = 0;
      while (qh < qt) { int c = q[qh++]; for (int m = 0; m < NMOVES; m++) { int c2 = cmove[m][c]; if (clen[c2] == 0xFF) { clen[c2] = clen[c] + 1; q[qt++] = c2; } } } free(q); }
    uint8_t s_from12[2][12]; { int n[2] = {0, 0}; for (int s = 0; s < NS; s++) s_from12[spar[s]][n[spar[s]]++] = s; }
    size_t KEYS = (size_t)48 * 2 * NH * NH * NL * 2 * MAXD;
    int nth = omp_get_max_threads();
    uint64_t *H = calloc(KEYS * nth, 8);
    if (!H) { fprintf(stderr, "oom\n"); return 1; }
    #pragma omp parallel
    {
        uint64_t *h = H + (size_t)omp_get_thread_num() * KEYS;
        uint8_t *buf = malloc(ROWB), *dep = malloc(ROW);
        #pragma omp for schedule(dynamic, 8)
        for (int k = 0; k < nclass; k++) {
            memset(dep, 0xFF, ROW);
            for (int d = 0; d < MAXD; d++) {
                if (pread(fd[d], buf, ROWB, (off_t)k * ROWB) != ROWB) { fprintf(stderr, "short read\n"); exit(1); }
                for (int b = 0; b < ROWB; b++) { uint8_t x = buf[b]; while (x) { int t = __builtin_ctz(x); x &= x - 1; dep[(size_t)b * 8 + t] = d; } }
            }
            int c = crep[k], w = 16 / nstab[k];
            int a = ccos[c], ai = ccos[cinv[c]], L = clen[c];
            int ab = cc_shape[a];
            for (int e = 0; e < NE; e++) {
                int b = epat[e], bi = epat[einv[e]];
                int hn = htr_dist[a][b], hi = htr_dist[ai][bi], sub = sub48[a][b];
                int par = cpar[c] ^ epar[e];
                size_t base = ((((((size_t)sub * 2 + ab) * NH + hn) * NH + hi) * NL + L) * 2 + par) * MAXD;
                const uint8_t *dp = dep + (size_t)e * 12;
                for (int s12 = 0; s12 < 12; s12++) {
                    if (dp[s12] == 0xFF) { fprintf(stderr, "unvisited state class %d e %d s %d\n", k, e, s12); exit(1); }
                    h[base + dp[s12]] += w;
                }
            }
        }
        free(buf); free(dep);
    }
    for (int t = 1; t < nth; t++) for (size_t i = 0; i < KEYS; i++) H[i] += H[(size_t)t * KEYS + i];
    printf("subset,ab,hN,hI,L,Epar,depth,count\n");
    unsigned long long tot = 0;
    for (size_t i = 0; i < KEYS; i++) if (H[i]) {
        size_t x = i; int d = x % MAXD; x /= MAXD; int par = x % 2; x /= 2; int L = x % NL; x /= NL; int hi = x % NH; x /= NH; int hn = x % NH; x /= NH; int ab = x % 2; x /= 2;
        printf("%s,%c,%d,%d,%d,%d,%d,%llu\n", sub48_name[x], sub48_nc[x] == 4 ? (ab ? 'b' : 'a') : '-', hn, hi, L, par, d, (unsigned long long)H[i]); tot += H[i];
    }
    fprintf(stderr, "total %llu\n", tot);
    return 0;
}
