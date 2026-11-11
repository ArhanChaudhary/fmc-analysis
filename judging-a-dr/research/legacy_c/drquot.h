// drquot.h — "what you can see" quotients of the DR group and their exact best-case finish tables.
//
// Principle (formalised in Lean, FMC/Quotient.lean): let K be a subgroup of the DR group G and T(Kg) the distance, in the
// graph of right cosets K\G with the 10 DR moves, from Kg to K.  Then
//      T(Kg) = min { optimal finish of k·g : k in K }      (so every state g needs at least T(Kg) moves),
// and the same holds for the inverse state:  optimal(g) >= T(K g^-1).
// A right coset Kg is "g up to renaming pieces by an element of K", i.e. a set of visible features of the position.
//
// Two subgroups are tabulated:
//   KF (order 3072) = HTR states whose corners are solved up to whole-cube half rotations and U2, whose M-slice edges have
//        both U-coloured edges in the same layer, likewise the S-slice edges, and whose E-slice permutation is even.
//        Restricted to HTR states and half-turn moves, K\H is exactly the 216-case table of FakeMMAP (T12059-T12076)
//        behind Rodney Kinney's "Advanced DR Bounding".  Features of a DR state modulo KF:
//          corners  : the corner permutation up to renaming by {id, x2, y2, z2} x {id, U2}                    5040 classes
//          edges    : which U/D-layer positions hold M-slice edges (70), and the U/D-colour pattern of the M-slice edges
//                     up to swapping the two colours, same for the S-slice edges (3 x 3)                        630 classes
//          E parity : parity of the E-slice permutation                                                         2
//   K0 (order 1536) = the same without U2 (corners solved up to whole-cube half rotations only): 10080 x 630 x 2 classes.
#ifndef DRQUOT_H
#define DRQUOT_H
#include "drclass.h"

#define NE630 630
static uint16_t *e630;              // UD-edge perm -> 0..629
static int e630_rep[NE630];
static uint16_t e630_mv[NE630][NMOVES];
static uint8_t e630_epat[NE630];

typedef struct {
    int ncc;                 // number of corner classes (5040 or 10080)
    uint16_t *ccls;          // corner perm -> class
    int *rep;
    uint16_t (*mv)[NMOVES];
    uint16_t *cc_ccos;       // class -> HTR corner coset
    uint8_t *T;              // [ncc*630*2] distance with all 10 DR moves
    uint8_t *TH;             // same graph, half-turn moves only (0xFF if unreachable): the HTR-only table
} Quot;

static inline size_t qidx(const Quot *Q, int cc, int ee, int par) { return ((size_t)cc * NE630 + ee) * 2 + par; }
static inline int qfeat_T(const Quot *Q, int c, int e, int s) { return Q->T[qidx(Q, Q->ccls[c], e630[e], spar[s])]; }

static void e630_init(void) {
    e630 = malloc(2 * NE);
    static int idx[1 << 16]; memset(idx, -1, sizeof idx); int n = 0;
    for (int e = 0; e < NE; e++) {
        uint8_t p[8]; unrank_n(e, 8, p);
        int mask = 0, lay = 0, flipM = -1, flipS = -1;
        for (int k = 0; k < 8; k++) {
            int isS = p[k] & 1, layer = p[k] >> 2;          // home layer of the piece: 0 = U (white), 1 = D (yellow)
            if (!isS) { mask |= 1 << k; if (flipM < 0) flipM = layer; layer ^= flipM; }
            else { if (flipS < 0) flipS = layer; layer ^= flipS; }
            lay |= layer << k;
        }
        int key = mask << 8 | lay;
        if (idx[key] < 0) { if (n >= NE630) { fprintf(stderr, "more than 630 edge classes\n"); exit(1); } idx[key] = n; e630_rep[n] = e; e630_epat[n] = epat[e]; n++; }
        e630[e] = idx[key];
    }
    if (n != NE630) { fprintf(stderr, "edge classes: %d, expected 630\n", n); exit(1); }
    for (int i = 0; i < NE630; i++) for (int m = 0; m < NMOVES; m++) e630_mv[i][m] = e630[emove[m][e630_rep[i]]];
    for (int e = 0; e < NE; e++) for (int m = 0; m < NMOVES; m++) if (e630[emove[m][e]] != e630_mv[e630[e]][m]) { fprintf(stderr, "edge class action not well defined\n"); exit(1); }
}

// withU2 = 1 -> KF ; 0 -> K0
static void quot_init(Quot *Q, int withU2) {
    // the renaming group on corners: V = {id, U2D2, R2L2, F2B2} (x <U2>)
    St el[8]; int nel = 0;
    St y2 = st_move(st_move(ST_ID, 1), 4), x2 = st_move(st_move(ST_ID, 6), 7), z2 = st_move(st_move(ST_ID, 8), 9), u2 = st_move(ST_ID, 1);
    St v[4] = {ST_ID, y2, x2, z2};
    for (int i = 0; i < 4; i++) { el[nel++] = v[i]; if (withU2) el[nel++] = st_mul(v[i], u2); }
    Q->ccls = malloc(2 * NC); Q->rep = malloc(sizeof(int) * NC);
    for (int c = 0; c < NC; c++) Q->ccls[c] = 0xFFFF;
    int n = 0;
    for (int c = 0; c < NC; c++) {
        if (Q->ccls[c] != 0xFFFF) continue;
        uint8_t p[8], r[8]; unrank_n(c, 8, p); Q->rep[n] = c;
        for (int i = 0; i < nel; i++) { for (int k = 0; k < 8; k++) r[k] = el[i].c[p[k]]; int d = rank_n(r, 8); if (Q->ccls[d] != 0xFFFF && Q->ccls[d] != n) { fprintf(stderr, "renaming set is not a group\n"); exit(1); } Q->ccls[d] = n; }
        n++;
    }
    Q->ncc = n;
    if (n != NC / nel) { fprintf(stderr, "corner classes %d, expected %d\n", n, NC / nel); exit(1); }
    Q->mv = malloc((size_t)n * sizeof *Q->mv); Q->cc_ccos = malloc(2 * n);
    for (int i = 0; i < n; i++) { Q->cc_ccos[i] = ccos[Q->rep[i]]; for (int m = 0; m < NMOVES; m++) Q->mv[i][m] = Q->ccls[cmove[m][Q->rep[i]]]; }
    for (int c = 0; c < NC; c++) { if (ccos[c] != Q->cc_ccos[Q->ccls[c]]) { fprintf(stderr, "class does not refine HTR coset\n"); exit(1); }
        for (int m = 0; m < NMOVES; m++) if (Q->ccls[cmove[m][c]] != Q->mv[Q->ccls[c]][m]) { fprintf(stderr, "corner class action not well defined\n"); exit(1); } }
    size_t N = (size_t)n * NE630 * 2;
    for (int pass = 0; pass < 2; pass++) {
        uint8_t *T = malloc(N); memset(T, 0xFF, N);
        uint32_t *q = malloc(sizeof(uint32_t) * N); size_t qh = 0, qt = 0;
        size_t s0 = qidx(Q, Q->ccls[0], e630[0], 0); T[s0] = 0; q[qt++] = s0;
        while (qh < qt) {
            size_t s = q[qh++]; int par = s & 1, ee = (s >> 1) % NE630, cc = (s >> 1) / NE630;
            for (int m = 0; m < NMOVES; m++) {
                if (pass == 1 && MOVE_IS_QT[m]) continue;
                size_t t = qidx(Q, Q->mv[cc][m], e630_mv[ee][m], par ^ (m >= 6));
                if (T[t] == 0xFF) { T[t] = T[s] + 1; q[qt++] = t; }
            }
        }
        if (pass == 0) { if (qt != N) { fprintf(stderr, "quotient graph not connected: %zu of %zu\n", qt, N); exit(1); } Q->T = T; } else Q->TH = T;
        free(q);
    }
}
#endif
