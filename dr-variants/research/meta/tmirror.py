"""The mirror check over the whole sample: for every within-goal HTR, the other side holds a within-goal HTR on the
same skeleton whose extra moves before HTR are this solution's read backwards (its finish may be shorter still).
Also the number of HTRs in the sample and the counts of the two checks `drvar metatuple` ran.
usage: tmirror.py -> ../out/meta/mirror.json"""
import json
import numpy as np
from tcommon import T, path
res = {}
for m in (2, 3, 4):
    t = T(m, sections=True, uniss=False, hcap=False)        # a check of the reading: every HTR in reach, every skeleton in full on both sides
    ok = t.ok
    q = t.q[ok].astype(int); te = t.te[ok]; tn = t.tn[ok]; dr = t.dr[ok]; side = t.side[ok]; tL = t.tL[ok]
    own = {}
    for i in range(len(q)):
        k = (dr[i], side[i], q[i], tL[i]) + tuple(te[i, :q[i]])
        own[k] = min(own.get(k, 99), tn[i])
    miss = 0
    for i in range(len(q)):
        rev = list(reversed(list(te[i, :q[i]]) + [tn[i]]))
        k = (dr[i], 1 - side[i], q[i], tL[i]) + tuple(rev[:-1])
        if k not in own or own[k] > rev[-1]: miss += 1
    log = dict(l.rstrip('\n').split('\t')[:2] for l in open(path(f'tup{m}.log')) if not l.startswith('routes') and not l.startswith('within'))
    raw = [l.rstrip('\n').split('\t') for l in open(path(f'tup{m}.log'))]
    dp = [r for r in raw if r[0].startswith('routes')][0]; mi = [r for r in raw if r[0].startswith('within')][0]
    res[m] = dict(htrs=int(t.n), within_goal_htrs=int(len(q)), no_mirror=miss, dp_routes=int(dp[1]), dp_differ=int(dp[3]), mirror=int(mi[1]), mirror_bad=int(mi[3]))
    print(m, res[m], flush=True)
json.dump(res, open(path('mirror.json'), 'w'), indent=1)
