// drspec.h — the ladder of "visible feature" quotients (shared by drlattice.c, drq.c, drsharp.c).
#ifndef DRSPEC_H
#define DRSPEC_H
#include "drquot.h"
#include <omp.h>
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


static Quot QF_, Q0_;
static Spec *SPECS; static int NSPEC;
// build all maps and class move tables; tables T are either computed (do_bfs) or loaded from <tabdir>/T_<name>.u8
static void specs_init(int do_bfs, const char *tabdir) {
    quot_init(&QF_, 1); quot_init(&Q0_, 0);
    #define QF QF_
    #define Q0 Q0_
    map_none = calloc(NC, 2); map_exact = malloc(2 * NC); map_ccos16 = ccos; map_epat16 = malloc(2 * NC); e2520 = malloc(2 * NC);
    for (int c = 0; c < NC; c++) { map_exact[c] = c; map_epat16[c] = epat[c]; }
    { static int idx[1 << 16]; memset(idx, -1, sizeof idx); n2520 = 0;
      for (int e = 0; e < NE; e++) { uint8_t p[8]; unrank_n(e, 8, p); int key = 0; for (int k = 0; k < 8; k++) key |= (((p[k] & 1) << 1) | (p[k] >> 2)) << (2 * k);
        if (idx[key] < 0) idx[key] = n2520++; e2520[e] = idx[key]; }
      if (n2520 != 2520) { fprintf(stderr, "2520 classes expected, got %d\n", n2520); exit(1); } }
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
    SPECS = malloc(sizeof specs); memcpy(SPECS, specs, sizeof specs); NSPEC = nspec;
    for (int i = 0; i < nspec; i++) {
        Spec *S = &SPECS[i];
        switch (S->cm) { case C_NONE: S->cmap = map_none; S->nc = 1; break; case C_HTR: S->cmap = map_ccos16; S->nc = NCCOS; break;
            case C_VU2: S->cmap = QF.ccls; S->nc = QF.ncc; break; case C_V: S->cmap = Q0.ccls; S->nc = Q0.ncc; break; default: S->cmap = map_exact; S->nc = NC; }
        switch (S->em) { case E_NONE: S->emap = map_none; S->ne = 1; break; case E_MASK: S->emap = map_epat16; S->ne = NEPAT; break;
            case E_630: S->emap = e630; S->ne = NE630; break; case E_2520: S->emap = e2520; S->ne = n2520; break;
            case E_630S: S->emap = e630s; S->ne = NE630 * 4; break; default: S->emap = e2520s; S->ne = 2520 * 4; }
        build_moves(S);
        S->N = (size_t)S->nc * S->ne * (S->par ? 2 : 1);
        if (do_bfs) bfs(S);
        else if (tabdir) {
            char fn[600]; snprintf(fn, sizeof fn, "%s/T_%s.u8", tabdir, S->name);
            FILE *f = fopen(fn, "rb"); if (!f) { fprintf(stderr, "missing table %s\n", fn); exit(1); }
            S->T = malloc(S->N); if (fread(S->T, 1, S->N, f) != S->N) { fprintf(stderr, "short table %s\n", fn); exit(1); } fclose(f);
        }
    }
    #undef QF
    #undef Q0
}
static Spec *spec_by_name(const char *n) { for (int i = 0; i < NSPEC; i++) if (!strcmp(SPECS[i].name, n)) return &SPECS[i]; fprintf(stderr, "no spec %s\n", n); exit(1); }
#endif
