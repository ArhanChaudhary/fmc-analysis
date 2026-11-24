"""Cap optimisation for the skeleton/variant meta.  A rule is P <= 1, the goal (L + P + S + T + N <= G with the N of the
bound), a floor on N from the mirror (0 none, 1 the mirror floor, 2 the same with T+N >= P+S on 3qt skeletons), a
least number of spare moves G-L a skeleton must have (0..3), and caps on single values or partial sums of (P,S,T,N):

    S, T, N, P+S, S+T, T+N, P+S+T, S+T+N, P+S+T+N

and the most-pairs step on what those let through (tcells.py; floor 2 only differs from the mirror floor on 3qt
skeletons, so the step reads the cells the same way under both).

Every rule with at most K active caps (values 0..8) is scored on each corner case: chance of missing a within-goal
finish, and mean HTRs to finish per DR.  Rules read cells only (tcells.py), so a batch of rules is one sparse product.
usage: topt.py K -> ../out/meta/opt{K}.npz   (K = 2 or 3)"""
import sys, itertools
import numpy as np
from tcells import Cells
from tcommon import BYQT, ORDER, path
from tmeta import PAIRS_MODE

CAPS = ['S', 'T', 'N', 'P+S', 'S+T', 'T+N', 'P+S+T', 'S+T+N', 'P+S+T+N']
VALS = list(range(0, 9)) + [99]

def quantities(c):
    return {'S': c.S, 'T': c.T, 'N': c.N, 'P+S': c.P + c.S, 'S+T': c.S + c.T, 'T+N': c.T + c.N, 'P+S+T': c.P + c.S + c.T,
            'S+T+N': c.S + c.T + c.N, 'P+S+T+N': c.P + c.S + c.T + c.N}

class Case:
    def __init__(self, z, case, bound='cca'):
        c = Cells(z, case, bound); self.c = c
        self.qv = quantities(c)
        row = np.searchsorted(c.wg, c.okdr)
        assert (c.wg[row] == c.okdr).all()
        self.M = np.zeros((c.nwg, len(c.cnt)), np.float32); self.M[row, c.okcell] = 1
        self.base = c.P <= 1
        half = np.where((c.q == 3) & ~c.nofloor, c.P + c.S - c.T, c.mirror_floor)
        self.floors = [np.ones(len(c.P), bool), c.P + c.S + c.T + np.maximum(c.N, c.mirror_floor) <= c.sp,
                       c.P + c.S + c.T + np.maximum(c.N, half) <= c.sp]
        # the most-pairs step under each floor
        if PAIRS_MODE == 'drop': self.floors = [f & c.top(i) for i, f in enumerate(self.floors)]
    def score(self, A):
        """A: cells x rules (bool).  Returns miss and work per rule."""
        Af = A.astype(np.float32)
        hit = (self.M @ Af) > 0
        return 1 - hit.mean(axis=0), (self.c.cnt.astype(np.float32) @ Af) / self.c.ndr
    def admit(self, names, floor, s0=0):
        """All value combinations of the named caps -> cells x 10^len(names)."""
        a = self.base & self.floors[floor] & (self.c.sp >= s0)
        A = a.reshape((-1,) + (1,) * len(names))
        for i, nm in enumerate(names):
            shp = [1] * (len(names) + 1); shp[0] = -1; shp[i + 1] = len(VALS)
            A = A & (self.qv[nm][:, None] <= np.array(VALS)[None, :]).reshape(shp)
        return A.reshape(len(a), -1)

def load_cases(bound='cca'):
    out = {}
    for m in (2, 3, 4):
        z = np.load(path(f'cells{m}.npz'))
        for case in BYQT[m]: out[case] = Case(z, case, bound)
    return out

if __name__ == '__main__':
    K = int(sys.argv[1])
    cases = load_cases()
    rules, miss, work = [], {c: [] for c in ORDER}, {c: [] for c in ORDER}
    for k in range(0, K + 1):
        for names in itertools.combinations(range(len(CAPS)), k):
            for floor, s0 in itertools.product((0, 1, 2), (0, 1, 2, 3)):
                # only combinations where every named cap is active (not 99), so each rule is listed once
                vals = np.array(list(itertools.product(range(len(VALS)), repeat=k)), dtype=np.int16).reshape(len(VALS) ** k, k)
                act = (vals < len(VALS) - 1).all(axis=1) if k else np.ones(1, bool)
                r = np.full((int(act.sum()), len(CAPS) + 2), 99, np.int16)
                r[:, len(CAPS)] = floor; r[:, len(CAPS) + 1] = s0
                for i, nm in enumerate(names): r[:, nm] = np.array(VALS)[vals[act, i]]
                rules.append(r)
                for cn, cs in cases.items():
                    mi, wo = cs.score(cs.admit([CAPS[i] for i in names], floor, s0))
                    miss[cn].append(mi[act]); work[cn].append(wo[act])
        print('caps', k, 'done', sum(len(r) for r in rules), flush=True)
    np.savez_compressed(path(f'opt{K}.npz'), rules=np.concatenate(rules),
                        miss=np.stack([np.concatenate(miss[c]) for c in ORDER], axis=1),
                        work=np.stack([np.concatenate(work[c]) for c in ORDER], axis=1))
