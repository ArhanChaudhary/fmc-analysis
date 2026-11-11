// drclass.h — HTR cosets of the DR group and the community's "HTR subset" labels, all computed from scratch.
//
// H  = <U2, D2, R2, L2, F2, B2>  (HTR group).  A right coset H·g is "the state g up to renaming pieces by an HTR element",
// i.e. exactly the information that survives when you only look at which pieces are bad.  H\G = 420 corner cosets x 70 edge patterns.
// Definitions used for labels (source: wen's sheet "HTR better smh (v2)", KB doc 87; Jay/Jack Love T144-T172):
//   bad corner  = a corner sitting in a position of the other tetrad (tetrads = orbits of corner positions under half turns)
//   bad edge    = an M-slice edge (UF UB DF DB) sitting in an S-slice position (UL UR DL DR) or vice versa
//   The community counts bad pieces up to turning both outer layers by a quarter ("0 or 8 bad corners", "4C2E = 4C6E", T165):
//   renaming all pieces by the state U D' turns n bad corners into 8-n and n bad edges into 8-n.  Mallard (cubelib,
//   steps/htr/subsets.rs) builds its 48 subsets as: closure of H·g and H·(U D)·g under half turns on the right and inversion,
//   i.e. double cosets of Hhat = <H, U D> merged with their inverses.  We reproduce exactly that:
//   NcQ label   = N bad corners in the frame where N <= 4 (and, if N = 4, bad edges <= 4),
//                 Q = minimum number of quarter turns that bring the corners into H-corners or (U D')·H-corners ("qt_corners")
//   4a / 4b     = the four bad corners can / cannot be placed on a single face using half turns only (only for Q <= 2 and Q = 5;
//                 for Q = 3, 4 a state and its inverse have different letters, and Mallard writes 4c3 / 4c4)
#ifndef DRCLASS_H
#define DRCLASS_H
#include "drcore.h"

#define NCCOS 420
#define NEPAT 70
static const int HALF_MOVES[6] = {1, 4, 6, 7, 8, 9};

static uint16_t *ccos;              // corner perm -> corner coset 0..419
static uint8_t *epat;               // UD-edge perm -> edge pattern 0..69
static int ccos_rep[NCCOS];         // a representative corner perm of each coset
static int epat_rep[NEPAT], epat_mask[NEPAT];
static int ccos_mv[NCCOS][NMOVES], epat_mv[NEPAT][NMOVES];
static uint8_t htr_dist[NCCOS][NEPAT];   // optimal DR->HTR length (DR moves)
static uint8_t cc_qt[NCCOS];             // "qt_corners": min quarter turns to bring the corners to HTR up to the U D' rotation
static uint8_t qt_full[NCCOS][NEPAT];    // min quarter turns of any DR sequence reaching H exactly (corners and edges)
static int lmul_c[NCCOS], lmul_e[NEPAT]; // left multiplication by U D' (renaming pieces by a quarter rotation of both layers)
static uint8_t sub48[NCCOS][NEPAT];      // Mallard subset id 0..47 of each HTR coset
static int NSUB48;
static char sub48_name[64][12];
static uint8_t sub48_nc[64], sub48_ne[64], sub48_qt[64], sub48_letter[64];
static uint8_t cc_nbad[NCCOS];           // number of bad corners (0,2,4,6,8)
static uint8_t cc_shape[NCCOS];          // for 4 bad corners: 0 = 4a, 1 = 4b ; otherwise 0
static uint8_t cc_subset[NCCOS];         // index into SUBSET_NAME
static uint8_t ep_nbad[NEPAT];           // number of bad edges (0,2,4,6,8)
static int HC[96], NHC;                  // the 96 corner permutations of H

#define NSUBSET 14
static const char *SUBSET_NAME[NSUBSET] = {"0c0", "4a1", "4a2", "4b2", "0c3", "2c3", "4a3", "4b3", "0c4", "2c4", "4a4", "4b4", "2c5", "4b5"};

static int subset_index(int nbadclass, int qt, int shape) {
    // nbadclass 0,2,4
    if (nbadclass == 0) return qt == 0 ? 0 : qt == 3 ? 4 : qt == 4 ? 8 : -1;
    if (nbadclass == 2) return qt == 3 ? 5 : qt == 4 ? 9 : qt == 5 ? 12 : -1;
    if (shape == 0) return qt == 1 ? 1 : qt == 2 ? 2 : qt == 3 ? 6 : qt == 4 ? 10 : -1;
    return qt == 2 ? 3 : qt == 3 ? 7 : qt == 4 ? 11 : qt == 5 ? 13 : -1;
}

static void drclass_init(void) {
    ccos = malloc(2 * NC); epat = malloc(NE);
    // --- the HTR corner group
    {
        uint8_t *seen = calloc(NC, 1); int *q = malloc(sizeof(int) * NC); int qh = 0, qt = 0;
        q[qt++] = 0; seen[0] = 1;
        while (qh < qt) { int c = q[qh++]; for (int k = 0; k < 6; k++) { int d = cmove[HALF_MOVES[k]][c]; if (!seen[d]) { seen[d] = 1; q[qt++] = d; } } }
        NHC = qt; if (NHC != 96) { fprintf(stderr, "HTR corner group has %d elements, expected 96\n", NHC); exit(1); }
        memcpy(HC, q, sizeof(int) * 96); free(seen); free(q);
    }
    // --- right cosets H·c : relabel the pieces of c by every h in H
    {
        for (int c = 0; c < NC; c++) ccos[c] = 0xFFFF;
        int n = 0; uint8_t hp[96][8];
        for (int i = 0; i < 96; i++) unrank_n(HC[i], 8, hp[i]);
        for (int c = 0; c < NC; c++) {
            if (ccos[c] != 0xFFFF) continue;
            uint8_t p[8], r[8]; unrank_n(c, 8, p);
            if (n >= NCCOS) { fprintf(stderr, "more than 420 corner cosets\n"); exit(1); }
            ccos_rep[n] = c;
            for (int i = 0; i < 96; i++) { for (int k = 0; k < 8; k++) r[k] = hp[i][p[k]]; ccos[rank_n(r, 8)] = n; }
            n++;
        }
        if (n != NCCOS) { fprintf(stderr, "found %d corner cosets, expected 420\n", n); exit(1); }
    }
    // --- edge patterns: which positions hold M-slice pieces (pieces 0,2,4,6)
    {
        int idx[256]; memset(idx, -1, sizeof idx); int n = 0;
        for (int e = 0; e < NE; e++) {
            uint8_t p[8]; unrank_n(e, 8, p); int mask = 0;
            for (int k = 0; k < 8; k++) if ((p[k] & 1) == 0) mask |= 1 << k;
            if (idx[mask] < 0) { idx[mask] = n; epat_rep[n] = e; epat_mask[n] = mask; n++; }
            epat[e] = idx[mask];
        }
        if (n != NEPAT) { fprintf(stderr, "found %d edge patterns, expected 70\n", n); exit(1); }
        for (int i = 0; i < NEPAT; i++) { int b = 0; for (int k = 0; k < 8; k++) if ((k & 1) && (epat_mask[i] >> k & 1)) b++; ep_nbad[i] = 2 * b; }
    }
    for (int i = 0; i < NCCOS; i++) for (int m = 0; m < NMOVES; m++) ccos_mv[i][m] = ccos[cmove[m][ccos_rep[i]]];
    for (int i = 0; i < NEPAT; i++) for (int m = 0; m < NMOVES; m++) epat_mv[i][m] = epat[emove[m][epat_rep[i]]];
    // well-definedness check of the coset action (every element, every move)
    for (int c = 0; c < NC; c++) for (int m = 0; m < NMOVES; m++) {
        if (ccos[cmove[m][c]] != ccos_mv[ccos[c]][m]) { fprintf(stderr, "corner coset action not well defined\n"); exit(1); }
        if (epat[emove[m][c]] != epat_mv[epat[c]][m]) { fprintf(stderr, "edge pattern action not well defined\n"); exit(1); }
    }
    // --- DR->HTR distance (BFS over 420 x 70 from the coset of the identity)
    {
        memset(htr_dist, 0xFF, sizeof htr_dist);
        int *q = malloc(sizeof(int) * NCCOS * NEPAT); int qh = 0, qt = 0;
        int s0 = ccos[0] * NEPAT + epat[0]; htr_dist[ccos[0]][epat[0]] = 0; q[qt++] = s0;
        while (qh < qt) {
            int s = q[qh++], a = s / NEPAT, b = s % NEPAT;
            for (int m = 0; m < NMOVES; m++) { int a2 = ccos_mv[a][m], b2 = epat_mv[b][m]; if (htr_dist[a2][b2] == 0xFF) { htr_dist[a2][b2] = htr_dist[a][b] + 1; q[qt++] = a2 * NEPAT + b2; } }
        }
        if (qt != NCCOS * NEPAT) { fprintf(stderr, "HTR coset graph not connected (%d)\n", qt); exit(1); }
        free(q);
    }
    // --- left multiplication by X = U D' on cosets (X normalises H, so H·g -> H·X·g is well defined)
    {
        St X = st_move(st_move(ST_ID, 0), 5);
        for (int i = 0; i < NCCOS; i++) { St g = st_unrank(ccos_rep[i], 0, 0); St r = st_mul(X, g); lmul_c[i] = ccos[rank_n(r.c, 8)]; }
        for (int i = 0; i < NEPAT; i++) { St g = st_unrank(0, epat_rep[i], 0); St r = st_mul(X, g); lmul_e[i] = epat[rank_n(r.e, 8)]; }
        for (int c = 0; c < NC; c += 11) { St g = st_unrank(c, c, 0); St r = st_mul(X, g);
            if (ccos[rank_n(r.c, 8)] != lmul_c[ccos[c]] || epat[rank_n(r.e, 8)] != lmul_e[epat[c]]) { fprintf(stderr, "U D' does not normalise H\n"); exit(1); } }
    }
    // --- "qt_corners": half turns cost 0, quarter turns cost 1, targets = H-corners and (U D')·H-corners
    {
        for (int i = 0; i < NCCOS; i++) cc_qt[i] = 0xFF;
        cc_qt[ccos[0]] = 0; cc_qt[lmul_c[ccos[0]]] = 0;
        for (int d = 0; d < 12; d++) {
            int changed = 1;
            while (changed) {
                changed = 0;
                for (int i = 0; i < NCCOS; i++) if (cc_qt[i] == d) for (int k = 0; k < 6; k++) { int j = ccos_mv[i][HALF_MOVES[k]]; if (cc_qt[j] > d) { cc_qt[j] = d; changed = 1; } }
            }
            for (int i = 0; i < NCCOS; i++) if (cc_qt[i] == d) for (int m = 0; m < NMOVES; m++) if (MOVE_IS_QT[m]) { int j = ccos_mv[i][m]; if (cc_qt[j] == 0xFF) cc_qt[j] = d + 1; }
        }
    }
    // --- qt_full: min quarter turns to reach H exactly, over all 29,400 cosets
    {
        memset(qt_full, 0xFF, sizeof qt_full); qt_full[ccos[0]][epat[0]] = 0;
        for (int d = 0; d < 16; d++) {
            int changed = 1;
            while (changed) {
                changed = 0;
                for (int a = 0; a < NCCOS; a++) for (int b = 0; b < NEPAT; b++) if (qt_full[a][b] == d) for (int k = 0; k < 6; k++) {
                    int a2 = ccos_mv[a][HALF_MOVES[k]], b2 = epat_mv[b][HALF_MOVES[k]]; if (qt_full[a2][b2] > d) { qt_full[a2][b2] = d; changed = 1; } }
            }
            for (int a = 0; a < NCCOS; a++) for (int b = 0; b < NEPAT; b++) if (qt_full[a][b] == d) for (int m = 0; m < NMOVES; m++) if (MOVE_IS_QT[m]) {
                int a2 = ccos_mv[a][m], b2 = epat_mv[b][m]; if (qt_full[a2][b2] == 0xFF) qt_full[a2][b2] = d + 1; }
        }
    }
    // --- bad corners, 4a/4b, labels
    {
        static const int T1[8] = {1, 0, 1, 0, 0, 1, 0, 1};   // tetrad of each position: UFR UBL DFL DBR
        static const int FACE[6] = {0x0F, 0xF0, 0x33, 0xCC, 0x99, 0x66};  // U D F B R L as corner-position masks
        for (int i = 0; i < NCCOS; i++) {
            uint8_t p[8]; unrank_n(ccos_rep[i], 8, p);
            int mask = 0, n = 0;
            for (int k = 0; k < 8; k++) if (T1[k] != T1[p[k]]) { mask |= 1 << k; n++; }
            cc_nbad[i] = n; cc_shape[i] = 0;
            if (n == 4) {
                uint8_t seen[256] = {0}; int q[256], qh = 0, qt = 0, ok = 0; q[qt++] = mask; seen[mask] = 1;
                while (qh < qt) {
                    int mk = q[qh++];
                    for (int f = 0; f < 6; f++) if (mk == FACE[f]) ok = 1;
                    for (int k = 0; k < 6; k++) {
                        St g = st_move(ST_ID, HALF_MOVES[k]); int mk2 = 0;
                        for (int pos = 0; pos < 8; pos++) if (mk >> g.c[pos] & 1) mk2 |= 1 << pos;   // piece now at pos came from g.c[pos]
                        if (!seen[mk2]) { seen[mk2] = 1; q[qt++] = mk2; }
                    }
                }
                cc_shape[i] = ok ? 0 : 1;
            }
            int nb = n == 8 ? 0 : n == 6 ? 2 : n;
            int si = subset_index(nb, cc_qt[i], cc_shape[i]);
            if (si < 0) { fprintf(stderr, "unexpected corner class: nbad %d qt %d shape %d\n", n, cc_qt[i], cc_shape[i]); exit(1); }
            cc_subset[i] = si;
        }
    }
    // --- the 48 subsets: components of the 29,400 cosets under  half turns on the right, U D' on the left, inversion
    {
        static int parent[NCCOS * NEPAT];
        for (int i = 0; i < NCCOS * NEPAT; i++) parent[i] = i;
        #define FIND(x) ({ int _x = (x); while (parent[_x] != _x) { parent[_x] = parent[parent[_x]]; _x = parent[_x]; } _x; })
        #define UNION(x, y) do { int _a = FIND(x), _b = FIND(y); if (_a != _b) parent[_a] = _b; } while (0)
        for (int a = 0; a < NCCOS; a++) for (int b = 0; b < NEPAT; b++) {
            int x = a * NEPAT + b;
            for (int k = 0; k < 6; k++) UNION(x, ccos_mv[a][HALF_MOVES[k]] * NEPAT + epat_mv[b][HALF_MOVES[k]]);
            UNION(x, lmul_c[a] * NEPAT + lmul_e[b]);
            UNION(x, ccos[cinv[ccos_rep[a]]] * NEPAT + epat[einv[epat_rep[b]]]);
        }
        int id[NCCOS * NEPAT]; memset(id, -1, sizeof id); NSUB48 = 0;
        for (int a = 0; a < NCCOS; a++) for (int b = 0; b < NEPAT; b++) {
            int r = FIND(a * NEPAT + b);
            if (id[r] < 0) {
                id[r] = NSUB48;
                int nc = cc_nbad[a], ne = ep_nbad[b];
                if (nc > 4 || (nc == 4 && ne > 4)) { nc = 8 - nc; ne = 8 - ne; }
                int q = cc_qt[a];
                char letter = 'c';
                if (nc == 4 && (q <= 2 || q == 5)) letter = cc_shape[a] ? 'b' : 'a';
                sub48_nc[NSUB48] = nc; sub48_ne[NSUB48] = ne; sub48_qt[NSUB48] = q; sub48_letter[NSUB48] = letter;
                snprintf(sub48_name[NSUB48], 12, "%d%c%d %de", nc, letter, q, ne);
                NSUB48++;
                if (NSUB48 > 64) { fprintf(stderr, "too many subsets\n"); exit(1); }
            }
            sub48[a][b] = id[r];
        }
        // every coset of a component must carry the same label
        for (int a = 0; a < NCCOS; a++) for (int b = 0; b < NEPAT; b++) {
            int nc = cc_nbad[a], ne = ep_nbad[b];
            if (nc > 4 || (nc == 4 && ne > 4)) { nc = 8 - nc; ne = 8 - ne; }
            int k = sub48[a][b];
            if (sub48_nc[k] != nc || sub48_ne[k] != ne || sub48_qt[k] != cc_qt[a]) { fprintf(stderr, "subset label not constant on component %s (coset %d,%d: %dc%d %de)\n", sub48_name[k], a, b, nc, cc_qt[a], ne); exit(1); }
        }
    }
}
#endif
