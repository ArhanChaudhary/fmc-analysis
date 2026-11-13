import pickle, collections, numpy as np
keys,typ,hr,states,dist=pickle.load(open('/data/fmc/tmp/eosw2/rings.pkl','rb'))
def s(r):
    e,h=r
    return ''.join(('E' if e[k] else '.')+{0:'o',1:'>',-1:'<'}[h[k]] for k in range(4))
def feats(k):
    out={}
    pairs=0; attached=[]; 
    for r in k:
        e,h=r
        for i in range(4):
            if e[i]:
                a=(h[(i-1)%4]==1)+(h[i]==-1); pairs+=a; attached.append(a)
    out['pairs']=pairs; out['att']=tuple(sorted(attached))
    out['same']=int(sum(k[0][0])!=1)
    out['hooksU']=sum(1 for x in k[0][1] if x); 
    return out
cnt=collections.Counter(keys)
rows=collections.defaultdict(list)
for k,h in dist.items():
    if k in cnt: rows[h].append(k)
for h in (0,1,2):
    print('== ring hmin',h,len(rows[h]),'classes')
    g=collections.defaultdict(list)
    for k in rows[h]:
        ft=feats(k); g[(ft['pairs'],ft['att'],ft['same'])].append(k)
    for kk in sorted(g):
        print(' pairs,att,same-ring',kk,len(g[kk]))
        for k in g[kk][:40]: print('    ',s(k[0]),'|',s(k[1]), cnt[k])
# table: pairs/att/same -> hmin distribution in classes and states
print('== (pairs, attachment per edge, edges same ring) -> classes by hmin / states by hmin')
g=collections.defaultdict(lambda: [collections.Counter(),collections.Counter()])
for k,h in dist.items():
    if k not in cnt: continue
    ft=feats(k); kk=(ft['pairs'],ft['att'],ft['same'])
    g[kk][0][h]+=1; g[kk][1][h]+=cnt[k]
for kk in sorted(g): print(kk,[g[kk][0][h] for h in range(6)],[g[kk][1][h] for h in range(6)])
