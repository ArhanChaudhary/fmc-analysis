// drsharp.c — computational check of sharpness: for every class of a rung, the smallest exact optimum among the
// states of the class equals the table value ("the bound is the best case of what you see").
#include "drspec.h"
#include <fcntl.h>
#include <unistd.h>
#define ROW 483840ULL
#define ROWB 60480
#define MAXD 19
int main(int argc, char **argv) {
    const char *dir = "/data/fmc/research/data/drbfs", *tab = "/data/fmc/research/data/tables";
    dr_init(); drclass_init(); e630_init(); specs_init(0, tab);
    char fn[512]; snprintf(fn, sizeof fn, "%s/classes.bin", dir);
    FILE *f = fopen(fn, "rb"); int nclass; if (!f || fread(&nclass, 4, 1, f) != 1) return 1;
    int *crep = malloc(4 * nclass); uint8_t *nstab = malloc(nclass);
    if (fread(crep, 4, nclass, f) != (size_t)nclass || fread(nstab, 1, nclass, f) != (size_t)nclass) return 1; fclose(f);
    int fd[MAXD]; for (int d = 0; d < MAXD; d++) { snprintf(fn, sizeof fn, "%s/depth_%02d.bits", dir, d); fd[d] = open(fn, O_RDONLY); if (fd[d] < 0) return 1; }
    for (int a = 1; a < argc; a++) {
        Spec *S = spec_by_name(argv[a]);
        uint8_t *mn = malloc(S->N); memset(mn, 0xFF, S->N);
        uint8_t *buf = malloc(ROWB), *dep = malloc(ROW);
        for (int k = 0; k < nclass; k++) {
            memset(dep, 0xFF, ROW);
            for (int d = 0; d < MAXD; d++) { if (pread(fd[d], buf, ROWB, (off_t)k * ROWB) != ROWB) return 1;
                for (int b = 0; b < ROWB; b++) { uint8_t x = buf[b]; while (x) { int t = __builtin_ctz(x); x &= x - 1; dep[(size_t)b * 8 + t] = d; } } }
            int c = crep[k];
            int full = S->cm != C_EXACT;      // classes mix several corner permutations: visit all 16 symmetric images
            for (int e = 0; e < NE; e++) { int par = cpar[c] ^ epar[e]; const uint8_t *dp = dep + (size_t)e * 12;
                uint8_t dm = 0xFF; for (int s = 0; s < 12; s++) if (dp[s] < dm) dm = dp[s];
                for (int Sy = 0; Sy < (full ? NSYM : 1); Sy++) {
                    size_t i = sidx(S, S->cmap[csym[Sy][c]], S->emap[esym[Sy][e]], par);
                    if (dm < mn[i]) mn[i] = dm; } }
        }
        size_t seen = 0, equal = 0, bad = 0;
        for (size_t i = 0; i < S->N; i++) if (mn[i] != 0xFF) { seen++; if (mn[i] == S->T[i]) equal++; else bad++; }
        printf("%-9s classes met: %zu ; best case of class == table value: %zu ; differ: %zu\n", S->name, seen, equal, bad);
        free(mn); free(buf); free(dep);
    }
    return 0;
}
