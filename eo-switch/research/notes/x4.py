import sys, numpy as np, collections
sys.path.insert(0,'/data/fmc/eo-switch/research/src')
import geom
from geom import N_CO,N_SL,N0,NAMES,move_ix
f=np.load('/data/fmc/eo-switch/research/out/big/feat.npz')
d=f['d']
UD=[m for m in range(18) if NAMES[m][0] in 'UD']
HT=[m for m in range(18) if NAMES[m].endswith('2') and NAMES[m][0] not in 'UD']
QT=[m for m in range(18) if NAMES[m][0] in 'RL' and not NAMES[m].endswith('2')]
m44=(f['drm_c']==4)&(f['drm_e']==4)
tg=np.zeros(N0,bool); tg[[int(move_ix(geom.SOLVED_IX,m)) for m in QT]]=True
print('targets',tg.sum())
s1=geom.bfs(tg,UD+HT)
print('setup hist on 4c4e',np.bincount(s1[m44]))
dd=d[m44]; ss=s1[m44]
print('d hist 4c4e',np.bincount(dd))
print('d==s1+1 share among sub7:',((dd<=6)&(dd==ss+1)).sum()/(dd<=6).sum(), 'sub7 needing 3 qt:',((dd<=6)&(dd<ss+1)).sum())
for k in range(1,8): print('d',k,'n',(dd==k).sum(),'via q1',((dd==k)&(ss+1==k)).sum())
# min half turns among optimal q1 setups: layered BFS over (h used)
INF=255
best=np.full((6,N0),INF,np.uint8)   # best[h][s] = min setup length using exactly <=h half turns
cur=np.full(N0,INF,np.uint8)
res={}
prev=None
for h in range(0,6):
    # dist with at most h half turns: dynamic: D_h = closure under UD moves of (D_{h-1} extended by one HT)
    D=np.full(N0,INF,np.int16)
    if h==0:
        D[tg]=0
    else:
        D=prev.copy()
        # one more half turn from prev
    # relax: Bellman-Ford style with UD moves (cost 1) and, for h>0, HT from prev (cost 1)
    changed=True
    while changed:
        changed=False
        idx=np.flatnonzero(D<INF)
        for m in UD:
            j=move_ix(idx,m); nd=D[idx]+1
            upd=nd<D[j]
            if upd.any():
                # handle duplicates: use minimum.at
                np.minimum.at(D,j[upd],nd[upd]); changed=True
        if h>0:
            idx=np.flatnonzero(prev<INF)
            for m in HT:
                j=move_ix(idx,m); nd=prev[idx]+1
                upd=nd<D[j]
                if upd.any():
                    np.minimum.at(D,j[upd],nd[upd]); changed=True
    prev=D; res[h]=D.copy()
    print('h<=',h,'reachable 4c4e',(D[m44]<INF).sum(),'with setup<=5:',(D[m44]<=5).sum())
np.save('/data/fmc/tmp/eosw2/s1.npy',s1)
np.save('/data/fmc/tmp/eosw2/Dh.npy',np.stack([res[h] for h in range(6)]))
