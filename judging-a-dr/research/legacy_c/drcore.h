// drcore.h — the domino-reduction (DR) group <U, D, R2, L2, F2, B2> as coordinates + tables.
//
// Conventions (everything else is derived from these few lines):
//   corner positions : 0 UFR 1 UFL 2 UBL 3 UBR 4 DFR 5 DFL 6 DBL 7 DBR
//   U/D-layer edges  : 0 UF 1 UL 2 UB 3 UR 4 DF 5 DL 6 DB 7 DR
//   E-slice edges    : 0 FR 1 FL 2 BL 3 BR
//   A state is "which piece sits at each position" (pieces are named by their home position).
//   Applying a move that carries position p to position t[p]:  new[t[p]] = old[p].
//   If A and B are move sequences, state(A then B)[pos] = state(A)[ state(B)[pos] ].
//   Moves: 0 U 1 U2 2 U' 3 D 4 D2 5 D' 6 R2 7 L2 8 F2 9 B2   (U clockwise seen from above: UFR->UFL->UBL->UBR)
#ifndef DRCORE_H
#define DRCORE_H
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define NC 40320
#define NE 40320
#define NS 24
#define NMOVES 10
#define NSYM 16

static const char *MOVE_NAME[NMOVES] = {"U", "U2", "U'", "D", "D2", "D'", "R2", "L2", "F2", "B2"};
static const int MOVE_INV[NMOVES] = {2, 1, 0, 5, 4, 3, 6, 7, 8, 9};
static const int MOVE_IS_QT[NMOVES] = {1, 0, 1, 1, 0, 1, 0, 0, 0, 0};
static const int MOVE_FACE[NMOVES] = {0, 0, 0, 1, 1, 1, 2, 3, 4, 5};

typedef struct { uint8_t c[8], e[8], s[4]; } St;

// position maps t[p] of the generating moves
static const uint8_t U_C[8] = {1, 2, 3, 0, 4, 5, 6, 7}, U_E[8] = {1, 2, 3, 0, 4, 5, 6, 7}, U_S[4] = {0, 1, 2, 3};
// D clockwise seen from below: DFL->DFR->DBR->DBL ; DF->DR->DB->DL
static const uint8_t D_C[8] = {0, 1, 2, 3, 7, 4, 5, 6}, D_E[8] = {0, 1, 2, 3, 7, 4, 5, 6}, D_S[4] = {0, 1, 2, 3};
static const uint8_t R2_C[8] = {7, 1, 2, 4, 3, 5, 6, 0}, R2_E[8] = {0, 1, 2, 7, 4, 5, 6, 3}, R2_S[4] = {3, 1, 2, 0};
static const uint8_t L2_C[8] = {0, 6, 5, 3, 4, 2, 1, 7}, L2_E[8] = {0, 5, 2, 3, 4, 1, 6, 7}, L2_S[4] = {0, 2, 1, 3};
static const uint8_t F2_C[8] = {5, 4, 2, 3, 1, 0, 6, 7}, F2_E[8] = {4, 1, 2, 3, 0, 5, 6, 7}, F2_S[4] = {1, 0, 2, 3};
static const uint8_t B2_C[8] = {0, 1, 7, 6, 4, 5, 3, 2}, B2_E[8] = {0, 1, 6, 3, 4, 5, 2, 7}, B2_S[4] = {0, 1, 3, 2};

static St ST_ID = {{0, 1, 2, 3, 4, 5, 6, 7}, {0, 1, 2, 3, 4, 5, 6, 7}, {0, 1, 2, 3}};

static inline St st_apply_map(St a, const uint8_t *tc, const uint8_t *te, const uint8_t *ts) {
    St r;
    for (int p = 0; p < 8; p++) { r.c[tc[p]] = a.c[p]; r.e[te[p]] = a.e[p]; }
    for (int p = 0; p < 4; p++) r.s[ts[p]] = a.s[p];
    return r;
}
static inline St st_move(St a, int m) {
    switch (m) {
    case 0: return st_apply_map(a, U_C, U_E, U_S);
    case 1: return st_move(st_move(a, 0), 0);
    case 2: return st_move(st_move(st_move(a, 0), 0), 0);
    case 3: return st_apply_map(a, D_C, D_E, D_S);
    case 4: return st_move(st_move(a, 3), 3);
    case 5: return st_move(st_move(st_move(a, 3), 3), 3);
    case 6: return st_apply_map(a, R2_C, R2_E, R2_S);
    case 7: return st_apply_map(a, L2_C, L2_E, L2_S);
    case 8: return st_apply_map(a, F2_C, F2_E, F2_S);
    default: return st_apply_map(a, B2_C, B2_E, B2_S);
    }
}
// state(A then B)
static inline St st_mul(St A, St B) {
    St r;
    for (int p = 0; p < 8; p++) { r.c[p] = A.c[B.c[p]]; r.e[p] = A.e[B.e[p]]; }
    for (int p = 0; p < 4; p++) r.s[p] = A.s[B.s[p]];
    return r;
}
static inline St st_inv(St a) {
    St r;
    for (int p = 0; p < 8; p++) { r.c[a.c[p]] = p; r.e[a.e[p]] = p; }
    for (int p = 0; p < 4; p++) r.s[a.s[p]] = p;
    return r;
}

// ---- permutation ranking (lexicographic / Lehmer)
static const int FACT[9] = {1, 1, 2, 6, 24, 120, 720, 5040, 40320};
static inline int rank_n(const uint8_t *p, int n) {
    int r = 0;
    for (int i = 0; i < n; i++) {
        int k = 0;
        for (int j = i + 1; j < n; j++) if (p[j] < p[i]) k++;
        r += k * FACT[n - 1 - i];
    }
    return r;
}
static inline void unrank_n(int r, int n, uint8_t *p) {
    uint8_t used[8] = {0};
    for (int i = 0; i < n; i++) {
        int k = r / FACT[n - 1 - i];
        r %= FACT[n - 1 - i];
        int j = 0;
        for (;; j++) if (!used[j]) { if (k == 0) break; k--; }
        p[i] = j; used[j] = 1;
    }
}
static inline int perm_parity(const uint8_t *p, int n) {
    int par = 0; uint8_t seen[8] = {0};
    for (int i = 0; i < n; i++) if (!seen[i]) { int j = i, len = 0; while (!seen[j]) { seen[j] = 1; j = p[j]; len++; } par ^= (len + 1) & 1; }
    return par;
}

// ---- symmetries: 16 = <y, x2, mirror(L<->R)> ; position maps
static const uint8_t SY_C[8] = {1, 2, 3, 0, 5, 6, 7, 4}, SY_E[8] = {1, 2, 3, 0, 5, 6, 7, 4}, SY_S[4] = {1, 2, 3, 0};
static const uint8_t SX2_C[8] = {7, 6, 5, 4, 3, 2, 1, 0}, SX2_E[8] = {6, 5, 4, 7, 2, 1, 0, 3}, SX2_S[4] = {3, 2, 1, 0};
static const uint8_t SM_C[8] = {1, 0, 3, 2, 5, 4, 7, 6}, SM_E[8] = {0, 3, 2, 1, 4, 7, 6, 5}, SM_S[4] = {1, 0, 3, 2};

// ---- global tables
static uint16_t (*cmove)[NC], (*emove)[NE];
static uint8_t smove[NMOVES][NS];
static uint16_t (*csym)[NC], (*esym)[NE];
static uint8_t ssym[NSYM][NS];
static uint16_t *cinv, *einv;
static uint8_t sinv[NS], *cpar, *epar, spar[NS];
static uint8_t SYMC[NSYM][8], SYME[NSYM][8], SYMS[NSYM][4];  // position maps of the 16 symmetries
static int sym_move[NSYM][NMOVES];                           // S m S^-1 as a move
static int sym_inv[NSYM], sym_mul[NSYM][NSYM];

static inline St st_unrank(int c, int e, int s) { St a; unrank_n(c, 8, a.c); unrank_n(e, 8, a.e); unrank_n(s, 4, a.s); return a; }
static inline St st_conj(St a, int S) {   // S a S^-1
    St r;
    for (int p = 0; p < 8; p++) { r.c[SYMC[S][p]] = SYMC[S][a.c[p]]; r.e[SYME[S][p]] = SYME[S][a.e[p]]; }
    for (int p = 0; p < 4; p++) r.s[SYMS[S][p]] = SYMS[S][a.s[p]];
    return r;
}

static void dr_init(void) {
    cmove = malloc(sizeof(uint16_t[NMOVES][NC])); emove = malloc(sizeof(uint16_t[NMOVES][NE]));
    csym = malloc(sizeof(uint16_t[NSYM][NC])); esym = malloc(sizeof(uint16_t[NSYM][NE]));
    cinv = malloc(2 * NC); einv = malloc(2 * NE); cpar = malloc(NC); epar = malloc(NE);
    // symmetry group elements: index = mir*8 + x2*4 + ypow  (S = M^mir * X2^x2 * Y^ypow as position maps composed left to right)
    for (int S = 0; S < NSYM; S++) {
        uint8_t c[8], e[8], s[4];
        for (int p = 0; p < 8; p++) c[p] = e[p] = p;
        for (int p = 0; p < 4; p++) s[p] = p;
        if (S & 8) { for (int p = 0; p < 8; p++) { c[p] = SM_C[c[p]]; e[p] = SM_E[e[p]]; } for (int p = 0; p < 4; p++) s[p] = SM_S[s[p]]; }
        if (S & 4) { for (int p = 0; p < 8; p++) { c[p] = SX2_C[c[p]]; e[p] = SX2_E[e[p]]; } for (int p = 0; p < 4; p++) s[p] = SX2_S[s[p]]; }
        for (int k = 0; k < (S & 3); k++) { for (int p = 0; p < 8; p++) { c[p] = SY_C[c[p]]; e[p] = SY_E[e[p]]; } for (int p = 0; p < 4; p++) s[p] = SY_S[s[p]]; }
        memcpy(SYMC[S], c, 8); memcpy(SYME[S], e, 8); memcpy(SYMS[S], s, 4);
    }
    for (int c = 0; c < NC; c++) {
        St a = st_unrank(c, c, c % NS);
        cpar[c] = perm_parity(a.c, 8); epar[c] = cpar[c];
        St iv = st_inv(a); cinv[c] = rank_n(iv.c, 8); einv[c] = cinv[c];
        for (int m = 0; m < NMOVES; m++) { St b = st_move(a, m); cmove[m][c] = rank_n(b.c, 8); emove[m][c] = rank_n(b.e, 8); }
        for (int S = 0; S < NSYM; S++) { St b = st_conj(a, S); csym[S][c] = rank_n(b.c, 8); esym[S][c] = rank_n(b.e, 8); }
    }
    for (int s = 0; s < NS; s++) {
        St a = st_unrank(0, 0, s);
        spar[s] = perm_parity(a.s, 4);
        St iv = st_inv(a); sinv[s] = rank_n(iv.s, 4);
        for (int m = 0; m < NMOVES; m++) { St b = st_move(a, m); smove[m][s] = rank_n(b.s, 4); }
        for (int S = 0; S < NSYM; S++) { St b = st_conj(a, S); ssym[S][s] = rank_n(b.s, 4); }
    }
    // how symmetries act on moves, their inverses and products
    St gen[NMOVES];
    for (int m = 0; m < NMOVES; m++) gen[m] = st_move(ST_ID, m);
    for (int S = 0; S < NSYM; S++) {
        for (int m = 0; m < NMOVES; m++) {
            St b = st_conj(gen[m], S); sym_move[S][m] = -1;
            for (int k = 0; k < NMOVES; k++) if (!memcmp(&b, &gen[k], sizeof(St))) sym_move[S][m] = k;
            if (sym_move[S][m] < 0) { fprintf(stderr, "symmetry %d does not map move %d to a move\n", S, m); exit(1); }
        }
        for (int T = 0; T < NSYM; T++) {
            uint8_t c[8]; for (int p = 0; p < 8; p++) c[p] = SYMC[T][SYMC[S][p]];   // first S then T
            sym_mul[S][T] = -1;
            for (int W = 0; W < NSYM; W++) if (!memcmp(c, SYMC[W], 8)) sym_mul[S][T] = W;
            if (sym_mul[S][T] < 0) { fprintf(stderr, "symmetry set not closed\n"); exit(1); }
            if (sym_mul[S][T] == 0) sym_inv[S] = T;
        }
    }
}

// ---- move-sequence parsing (DR moves only; accepts ' and 2, also Unicode right quote)
static int parse_moves(const char *txt, int *out, int maxn) {
    int n = 0;
    for (const char *p = txt; *p;) {
        int f = -1;
        switch (*p) { case 'U': f = 0; break; case 'D': f = 1; break; case 'R': f = 2; break; case 'L': f = 3; break; case 'F': f = 4; break; case 'B': f = 5; break; }
        if (f < 0) { p++; continue; }
        p++;
        int two = 0, prime = 0;
        for (;; p++) {
            if (*p == '2') two = 1;
            else if (*p == '\'') prime = 1;
            else if ((unsigned char)p[0] == 0xE2 && (unsigned char)p[1] == 0x80 && (unsigned char)p[2] == 0x99) { prime = 1; p += 2; }
            else break;
        }
        int m;
        if (f == 0) m = two ? 1 : (prime ? 2 : 0);
        else if (f == 1) m = two ? 4 : (prime ? 5 : 3);
        else { if (!two) return -1; m = 4 + f; }
        if (n < maxn) out[n++] = m;
    }
    return n;
}
#endif
