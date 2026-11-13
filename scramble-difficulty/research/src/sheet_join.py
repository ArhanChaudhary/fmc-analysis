"""Join DougCube's 'All WCA Scrambles' FMC tab (kb copy, last updated 2026-07-16) to the export scrambles by text:
optimal length per official scramble (out/opt_real.tsv), and a cross-check of this study's optimal linear EO
(min over axes, normal only) against the sheet's 'EO (linr)' column."""
import csv, collections
sheet = {}
for r in csv.DictReader(open('/data/fmc/kb/docs/gsheet/183AYpjKz4fZZAy5Hx5lxEthD2f356ReZG-uHPm_HWcY/FMC.csv')):
    sheet[' '.join(r['Scramble'].split())] = r
ids = {l.split('\t')[1].strip(): l.split('\t')[0] for l in open('../big/in_real.tsv')}
feat = {r['id']: r for r in csv.DictReader(open('../out/feat_real.tsv'), delimiter='\t')}
n = agree = 0; dis = collections.Counter()
with open('../out/opt_real.tsv', 'w') as f:
    f.write('id\topt\n')
    for s, k in ids.items():
        r = sheet.get(s)
        if not r: continue
        f.write(f"{k}\t{int(float(r['Optimal Length']))}\n")
        mine = min(int(feat[k][f'eo_opt_{e}_N']) for e in ('UD', 'FB', 'RL'))
        n += 1; agree += mine == int(float(r['EO (linr)']))
        if mine != int(float(r['EO (linr)'])): dis[(mine, r['EO (linr)'])] += 1
print(f'matched {n} of {len(ids)} official scrambles; optimal linear EO agrees on {agree}; disagreements {dict(dis)}')
