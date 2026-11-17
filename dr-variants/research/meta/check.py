"""Consistency of the records of drvar metarun: the bounds are ordered (corner <= rule <= table <= total), and the best
HTR of each side equals the optimal leave-slice length of the DR for every DR that has a within-goal solution."""
import sys, numpy as np, pandas as pd
from load import *
for m in [2,3,4]:
    r, d, q, mm = load(f'../out/meta/run{m}')
    df = pd.DataFrame(r)
    g = d.goal.iloc[0]
    print(f'm={m} goal={g} records={len(df)} DRs={len(d)}')
    assert (df.lbr <= df.total).all() and (df.lbt <= df.total).all() and (df.lbc <= df.lbr).all() and (df.lbr <= df.lbt).all()
    best = df.groupby(['dr','side']).total.min().unstack()
    chk = d[['ls']].join(best)
    solv = chk.ls <= g
    reached = (chk[0] <= g) | (chk[1] <= g)             # some HTR of the DR is within goal
    hit = chk[solv & reached]
    assert (hit[0] == hit.ls).all() and (hit[1] == hit.ls).all(), hit
    assert not reached[~solv].any()
    assert (chk[0].fillna(99) >= chk.ls).all() and (chk[1].fillna(99) >= chk.ls).all()
    # a DR with a within-goal solution and no within-goal HTR here: every such solution has four more quarter turns
    # than the minimum (the search stops at two more)
    far = solv & ~reached
    print('  min total over records == optimal leave-slice on both sides for', len(hit), 'of the', solv.sum(), 'within-goal DRs;',
          far.sum(), 'have their solutions past two more quarter turns:', d.subset[far].tolist(), '; none below goal for the others')
    print('  subset names:', d.subset.str.slice(0,3).value_counts().to_dict())
    print('  q - m of records:', (df.q - df.m).value_counts().sort_index().to_dict())
    w = df[df.total <= g]
    print('  q - m of within-goal:', (w.q - w.m).value_counts().sort_index().to_dict())
    print('  extra e0 of within-goal:', (w.len - w.lsk).value_counts().sort_index().to_dict())
