#!/usr/bin/env python3
"""Per-subset table for the write-up (markdown): exact statistics and what each rung certifies."""
import csv, collections
H=collections.defaultdict(collections.Counter)
for r in csv.DictReader(open('/data/fmc/research/out/lattice.csv')):
    H[(r['spec'],int(r['sides']),r['subset'])][(int(r['bound']),int(r['depth']))]+=int(r['count'])
ORDER=['0c0','4a1','4a2','4b2','0c3','2c3','4c3','0c4','2c4','4c4','2c5','4b5']
subs=sorted({k[2] for k in H}, key=lambda n:(ORDER.index(n.split()[0]), int(n.split()[1][0])))
def P(c,f): t=sum(c.values()); return 100*sum(n for k,n in c.items() if f(*k))/t
out=['| Subset | share of all DRs | mean finish | min | finish ≤ 12 | finish ≤ 13 | certified ≥ 13: corner+parity | AdvDR features | everything visible | certified ≥ 14: everything visible |','|---|---|---|---|---|---|---|---|---|---|']
TOT=19508428800
for s in subs:
    c=H[('htr',2,s)]; t=sum(c.values()); mean=sum(d*n for (b,d),n in c.items())/t; mn=min(d for (b,d) in c)
    row=[s,f'{100*t/TOT:.2f}%',f'{mean:.2f}',str(mn),f'{P(c,lambda b,d:d<=12):.1f}%',f'{P(c,lambda b,d:d<=13):.1f}%']
    row+= [f"{P(H[(sp,2,s)],lambda b,d:b>=13):.0f}%" for sp in ('c+p','KF','c+2520+F')]
    row.append(f"{P(H[('c+2520+F',2,s)],lambda b,d:b>=14):.0f}%")
    out.append('| '+' | '.join(row)+' |')
open('/data/fmc/research/out/subset_table.md','w').write('\n'.join(out)+'\n')
print('\n'.join(out[:6])); print('...', len(out)-2, 'subsets')
