// genlean.c — print the move "source" maps (new[p] = old[src[p]]) for the Lean model, straight from the C model.
#include "drcore.h"
int main(void) {
    dr_init();
    for (int m = 0; m < NMOVES; m++) {
        St g = st_move(ST_ID, m);   // g.c[pos] = piece now at pos = position it came from
        printf("%-3s C:", MOVE_NAME[m]); for (int p = 0; p < 8; p++) printf(" %d", g.c[p]);
        printf("  E:"); for (int p = 0; p < 8; p++) printf(" %d", g.e[p]);
        printf("  S:"); for (int p = 0; p < 4; p++) printf(" %d", g.s[p]); printf("\n");
    }
    return 0;
}
