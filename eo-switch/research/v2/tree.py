"""Grow a small decision tree over quick reads, first split on the pair count.  A split is scored by how much it
lowers the cell-optimal loss summed over several prices of a wasted switch (lam), so that the leaves rank well at
more than one cut.  The leaves, sorted by value per wasted switch, are the ranked card."""
import numpy as np, sys
from lib import *
from induce import atoms, QUICK
LAMS = (0.5, 1.0, 2.0)
def grow(m, feats=QUICK, K=6, w=None, max_leaves=12, min_gain=0.002, strat='pairs', lams=LAMS, verbose=True):
    idx = np.flatnonzero(m); n = idx.size; dd = d[idx]
    w = (weights(K) if w is None else w)[dd]; bad = (dd > K).astype(float)
    A = atoms(idx, feats); names = [a[1] for a in A]
    M = np.stack([a[2] for a in A]).astype(np.float32)
    st = np.asarray(F[strat])[idx]
    leaves = [([f'{strat}={p}'], st == p) for p in np.unique(st)]
    def cost(a, b): return sum(np.minimum(a, l * b) for l in lams)
    while len(leaves) < max_leaves:
        best = (min_gain * len(lams), None)
        for li, (desc, mask) in enumerate(leaves):
            mw = (w * mask).astype(np.float32); mb = (bad * mask).astype(np.float32)
            a0, b0 = mw.sum(), mb.sum()
            a1 = M @ mw; b1 = M @ mb
            gain = (cost(a0, b0) - cost(a1, b1) - cost(a0 - a1, b0 - b1)) / n
            cnt = M @ mask.astype(np.float32)
            gain[(cnt == 0) | (cnt == mask.sum())] = -1
            i = int(np.argmax(gain))
            if gain[i] > best[0]: best = (float(gain[i]), (li, i))
        if best[1] is None: break
        li, i = best[1]; desc, mask = leaves[li]
        yes = mask & (M[i] > 0); no = mask & ~(M[i] > 0)
        leaves[li:li + 1] = [(desc + [names[i]], yes), (desc + ['not ' + names[i]], no)]
        if verbose: print(f'split {" & ".join(desc)} on {names[i]}: gain {best[0]/len(lams):.4f}')
    out = []
    for desc, mask in leaves:
        h = np.bincount(dd[mask], minlength=11)
        a = w[mask].sum(); b = bad[mask].sum()
        out.append(dict(desc=desc, n=int(mask.sum()), le4=int(h[:K - 1].sum()), d5=int(h[K - 1]), d6=int(h[K]), bad=int(b), ratio=float(a / max(b, 1e-9)), mask=mask))
    out.sort(key=lambda r: -r['ratio'])
    return idx, out
def show(m, idx, leaves, K=6):
    n = idx.size; dd = d[idx]
    t4, t5, t6 = (dd <= K - 2).sum(), (dd == K - 1).sum(), (dd == K).sum()
    c = np.zeros(n, bool)
    print(f'{"group":70s} {"share":>6s} {"sub7":>6s} {"le4":>5s} {"d5":>5s} {"d6":>6s} {"ratio":>7s} | cum sw  miss4  miss5  miss6')
    for r in leaves:
        c |= r['mask']
        good = r['le4'] + r['d5'] + r['d6']
        print(f'{" & ".join(r["desc"]):70s} {100*r["n"]/n:5.1f}% {100*good/r["n"]:5.1f}% {r["le4"]:5d} {r["d5"]:5d} {r["d6"]:6d} {r["ratio"]:7.2f} | {100*c.mean():5.1f}% {100*((dd<=K-2)&~c).sum()/max(t4,1):5.1f}% {100*((dd==K-1)&~c).sum()/max(t5,1):5.1f}% {100*((dd==K)&~c).sum()/max(t6,1):5.1f}%')
if __name__ == '__main__':
    c, e = int(sys.argv[1]), int(sys.argv[2]); L = int(sys.argv[3]) if len(sys.argv) > 3 else 12
    feats = sys.argv[4].split(',') if len(sys.argv) > 4 else QUICK
    m = drm_mask(c, e)
    idx, leaves = grow(m, feats, max_leaves=L)
    show(m, idx, leaves)
