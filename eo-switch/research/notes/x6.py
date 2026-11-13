import sys, numpy as np, collections
sys.path.insert(0,'/data/fmc/eo-switch/research/src')
import geom
from geom import N_CO,N_SL,N0,NAMES,move_ix,EOK
f=np.load('/data/fmc/eo-switch/research/out/big/feat.npz')
d=f['d']
UD=[m for m in range(18) if NAMES[m][0] in 'UD']
SIDE=[m for m in EOK if NAMES[m][0] not in 'UD']
print([NAMES[m] for m in SIDE])
INF=255
sig=np.full(N0,INF,np.uint8)
def closure(idx):
    seen=np.zeros(N0,bool); seen[idx]=True; fr=idx
    while fr.size:
        nx=np.unique(np.concatenate([move_ix(fr,m) for m in UD]))
        nx=nx[~seen[nx]]; seen[nx]=True; fr=nx
    return np.flatnonzero(seen)
fr=closure(np.array([geom.SOLVED_IX])); sig[fr]=0; k=0
while fr.size:
    nx=np.unique(np.concatenate([move_ix(fr,m) for m in SIDE]))
    nx=nx[sig[nx]==INF]
    if nx.size==0: break
    nx=closure(nx); nx=nx[sig[nx]==INF]
    k+=1; sig[nx]=k; fr=nx
print('sigma hist',np.bincount(sig))
np.save('/data/fmc/tmp/eosw2/sigma.npy',sig)
drm=f['drm_c'].astype(int)*10+f['drm_e'].astype(int)
print('overall: sigma -> n, sub7%')
for s in range(sig.max()+1):
    sel=sig==s; print(s, sel.sum(), '%.2f%%'%(100*sel.mean()), 'sub7 %.1f'%(100*(d[sel]<=6).mean()), 'd hist', np.bincount(d[sel],minlength=11))
print('by DRM')
for dm in [44,42,32,78,88,22,46,34,36,54,56,66,0]:
    sel=drm==dm
    if sel.sum()==0: continue
    out=[]
    for s in range(sig.max()+1):
        t=sel&(sig==s)
        if t.sum(): out.append('s%d: %.1f%% of DRM at %.1f%%'%(s,100*t.sum()/sel.sum(),100*(d[t]<=6).mean()))
    print('%dc%de'%(dm//10,dm%10), 'n',sel.sum(),'sub7 %.1f%%'%(100*(d[sel]<=6).mean()),' | '.join(out))
