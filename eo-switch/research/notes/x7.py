import sys, numpy as np, collections, itertools
sys.path.insert(0,'/data/fmc/eo-switch/research/src')
import geom
from geom import N_CO,N_SL,N0,ESET,EDGES,CORNERS,CT,UD_FACE,C_NAME,E_NAME
f=np.load('/data/fmc/eo-switch/research/out/big/feat.npz')
d=f['d']; Dh=np.load('/data/fmc/tmp/eosw2/Dh.npy')
m44=np.flatnonzero((f['drm_c']==4)&(f['drm_e']==4))
hmin_cube=np.argmax(Dh[:,m44]<255,axis=0)
ci={n:i for i,n in enumerate(C_NAME)}; ei={n:i for i,n in enumerate(E_NAME)}
def nm(*alts):
    for a in alts:
        for perm in itertools.permutations(a):
            s=''.join(perm)
            if s in ci: return ci[s]
            if s in ei: return ei[s]
    raise KeyError(alts)
# ring orders (clockwise seen from outside): edges then the corner AFTER each edge
UE=[nm('UB'),nm('UR'),nm('UF'),nm('UL')]; UC=[nm('UBR'),nm('UFR'),nm('UFL'),nm('UBL')]   # corner k sits between edge k and edge k+1
DE=[nm('DB'),nm('DL'),nm('DF'),nm('DR')]; DC=[nm('DBL'),nm('DFL'),nm('DFR'),nm('DBR')]
FACE=lambda e: [c for c in E_NAME[e] if c not in 'UD'][0]
def ring(ct,sl,EE,CC):
    e=tuple(int(ESET[sl,x]) for x in EE)
    h=[]
    for k,c in enumerate(CC):
        if ct[c]==0: h.append(0); continue
        sf=UD_FACE[c][ct[c]]            # face holding the U/D sticker
        nxt=FACE(EE[(k+1)%4]); prv=FACE(EE[k])
        # points to the edge on the side face NOT holding the sticker
        h.append(1 if sf==prv else -1)   # sticker on previous edge's face -> hooks the next edge (cw)
        assert sf in (prv,nxt)
    return e,tuple(h)
def canon(r):
    e,h=r
    return min((e[k:]+e[:k],h[k:]+h[:k]) for k in range(4))
def swap(U,D,p,q):
    (ue,uh),(de,dh)=U,D
    ue,uh,de,dh=list(ue),list(uh),list(de),list(dh)
    # window at edge p: corners p-1 (before) and p (after)
    ue[p],de[q]=de[q],ue[p]
    uh[(p-1)%4],dh[(q-1)%4]=dh[(q-1)%4],uh[(p-1)%4]
    uh[p],dh[q]=dh[q],uh[p]
    return (tuple(ue),tuple(uh)),(tuple(de),tuple(dh))
def hasbar(r):
    e,h=r
    return any(e[k] and h[(k-1)%4]==1 and h[k]==-1 for k in range(4))
def key(U,D): return (canon(U),canon(D))
# all reduced states from the cube
ES=[i for i,p in enumerate(EDGES) if p[1]==0]
def slot_type(sl):
    bs=[EDGES[i] for i in ES if not ESET[sl,i]]
    a,b=bs
    return 0 if a[0]==b[0] else 2 if a[2]==b[2] else 1
states={}
keys=[]; typ=[]
for ix in m44:
    co,sl=divmod(int(ix),N_SL)
    U=ring(CT[co],sl,UE,UC); D=ring(CT[co],sl,DE,DC)
    k=key(U,D); keys.append(k); typ.append(slot_type(sl)); states[k]=(U,D)
print('reduced ring-pair classes',len(states))
# BFS on reduced classes
goal=[k for k,(U,D) in states.items() if hasbar(U) and hasbar(D)]
dist={k:0 for k in goal}; fr=goal; n=0
while fr:
    n+=1; nx=[]
    for k in fr:
        U,D=states[k]
        for p in range(4):
            for q in range(4):
                k2=key(*swap(U,D,p,q))
                if k2 not in dist: dist[k2]=n; nx.append(k2); states.setdefault(k2,swap(U,D,p,q))
    fr=nx
print('ring hmin hist',collections.Counter(dist.values()))
hr=np.array([dist[k] for k in keys]); typ=np.array(typ)
pred=np.maximum(hr,typ)
print('cube hmin == max(ring hmin, slot type):',(pred==hmin_cube).mean())
bad=pred!=hmin_cube
print('mismatch table (ring, type, cube):',collections.Counter(zip(hr[bad].tolist(),typ[bad].tolist(),hmin_cube[bad].tolist())))
y=d[m44]<=6
print('ring hmin x slot type -> n, sub7')
for a in range(hr.max()+1):
    for t in range(3):
        s=(hr==a)&(typ==t)
        if s.sum(): print(a,t,s.sum(),'%.1f%%'%(100*s.mean()),'sub7 %.1f'%(100*y[s].mean()))
import pickle; pickle.dump((keys,typ,hr,states,dist),open('/data/fmc/tmp/eosw2/rings.pkl','wb'))
