#!/usr/bin/env python3
"""Independent recount of "which edge count you pass on the way" (section 1): per state, the subsets x edges that
some budget-2 route to an optimal finish passes after a quarter turn and before HTR, from the per-state route
records; compared with out/q2_edge_steps_via.tsv.  Usage: recount_via.py"""
import sys, re, csv, collections, numpy as np
B='/data/fmc/htr-routes/research/'; RUN=B+'out/big/run1/'
size=collections.Counter()
for line in open(B+'verify/out/cosets_per_label.tsv'):
    lab,n=line.split('\t'); sub,e=lab.split()
    sub='4c3' if sub in('4a3','4b3') else '4c4' if sub in('4a4','4b4') else sub
    size[f'{sub} {e}']+=int(n)
via={}  # key id -> frozenset of intermediate labels
with open(RUN+'route_keys.tsv') as f:
    next(f)
    for line in f:
        i,k=line.rstrip('\n').split('\t',1)
        if not k.startswith('H:'): continue
        labs=[x.strip('()') for x in k[2:].rsplit(' | ',1)[0].split(' > ')]
        via[int(i)]=frozenset(labs[1:-1])
num=collections.Counter(); den=collections.Counter(); percell={}
for cell in sorted(size):
    rows=list(csv.DictReader(open(RUN+f'states_{cell.replace(" ","_")}.tsv'),delimiter='\t'))
    w=np.frombuffer(open(RUN+f'routes_{cell.replace(" ","_")}.bin','rb').read(),dtype='<u8')
    pos=0; wt=size[cell]/len(rows); cnt=collections.Counter()
    for r in rows:
        niss=int(r['htrNiss']); n=int(w[pos]); rec=w[pos+1:pos+1+n]; pos+=1+n; pos+=1+int(w[pos])
        s=set()
        for x in rec.tolist():
            kid=x>>11
            if kid in via and (x&1)==0 and ((x>>6)&31)<=niss+2: s|=via[kid]
        subs={l.split()[0] for l in s}
        for sb in subs: den[sb]+=wt
        for l in s: num[l]+=wt
        for l in s: cnt[l]+=1
        for sb in subs: cnt[sb+' *']+=1
    percell[cell]={k:v/len(rows) for k,v in cnt.items()}
    print(cell,'done',file=sys.stderr)
for sb,es in (('4b2',('2e','4e','0e')),('4a2',('4e','2e','0e')),('4a1',('4e','2e','0e'))):
    print(sb,{e:round(100*num[f'{sb} {e}']/den[sb],1) for e in es})
for c in ('2c3 2e','2c3 0e'):
    print(c,{k:round(100*percell[c].get(k,0),1) for k in ('4b2 2e','4b2 4e','4b2 *')})
# compare every cell x via with the study's table
pub={(r['subset'],r['via']):float(r['share']) for r in csv.DictReader(open(B+'out/q2_edge_steps_via.tsv'),delimiter='\t') if r['target']=='opt'}
worst=0; miss=0
for (c,v),s in pub.items():
    m=percell[c].get(v)
    if m is None: miss+=1; continue
    worst=max(worst,abs(m-s))
print('cells x via in the study table',len(pub),'missing here',miss,'largest difference',worst)
