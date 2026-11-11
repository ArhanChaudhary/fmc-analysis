#!/usr/bin/env python3
"""The 216 NISS@1qt classes: half-turn-only value (FakeMMAP's first BFS), DR-move value (our KF table),
all-move optimum (meet in the middle, complete up to 10 moves), and FakeMMAP's later "HTR-breaking" table."""
import re, sys, json, subprocess, csv, collections
sys.path.insert(0, '/data/fmc/research/tool'); import fmccube as fc
lab = []
for line in open('/data/fmc/assets/attachments/1546077758189477989_0_message.txt'):
    m = re.match(r'^(\S+ \S) F-(\S) R-(\S)\s+(even|odd) E-parity: (\d+) Example scramble: ?(.*)$', line.rstrip('\n'))
    if m: lab.append(((m.group(1), m.group(2), m.group(3), m.group(4)), int(m.group(5)), m.group(6)))
inp = ''
for _, _, scr in lab:
    a = fc.to_dr_arrays(fc.state_after(scr)); inp += ' '.join(map(str, a[0] + a[1] + a[2])) + '\n'
out = subprocess.run(['/data/fmc/research/drtools/target/release/drtools', 'query', '/data/fmc/research/data/drbfs', '/data/fmc/research/data/tables'], input=inp, capture_output=True, text=True).stdout.strip().split('\n')
allm = json.load(open('/data/fmc/research/out/allmoves216.json'))
witn = json.load(open('/data/fmc/research/out/allmoves216_witness.json'))
# FakeMMAP's table with double slices and F R2 E2 R2 F'-type algs (T12175)
grid = {}
rows = list(csv.reader(open('/data/fmc/assets/attachments/1546599572644696075_0_RK_OBL_table_DS_2e.csv')))
i = 0
while i < len(rows):
    r = rows[i]
    heads = [(j, r[j].strip(), r[j + 1].strip()) for j in range(0, len(r) - 1, 5) if r[j].strip() and r[j + 1].strip() in ('even', 'odd')]
    if heads and i + 4 < len(rows):
        for j, corner, par in heads:
            cols = [c.strip()[2:] for c in rows[i + 1][j + 1:j + 4]]
            for k in range(3):
                rr = rows[i + 2 + k]; f = rr[j].strip()[2:]
                for t, c in enumerate(cols):
                    try: grid[(corner, f, c, par)] = int(float(rr[j + 1 + t]))
                    except ValueError: pass
        i += 5
    else: i += 1
print(f'labels {len(lab)}, FakeMMAP DS_2e cells parsed {len(grid)}')
tab = []; stat = collections.Counter()
for (key, hval, scr), line in zip(lab, out):
    kv = dict(t.split('=', 1) for t in line.split(' ') if '=' in t)
    dr = int(kv['KF'].split('/')[0]); c = kv['kfclass']
    am = min(allm[c]) if c in allm else dr
    fm = grid.get(key)
    tab.append((key, hval, dr, am, fm, witn.get(c, '')))
    stat[f'half-turn - DR-move = {hval - dr}'] += 1; stat[f'DR-move - all-move = {dr - am}'] += 1
    if fm is not None: stat[f'FakeMMAP(HTR-breaking table) - all-move = {fm - am}'] += 1
for k, v in sorted(stat.items()): print(f'{v:4d}  {k}')
print('\nclasses where quarter turns (DR moves) beat half turns:')
for t in tab:
    if t[1] != t[2]: print('  ', ' '.join(t[0][:1]), f'F-{t[0][1]} R-{t[0][2]} {t[0][3]}', 'half-turn', t[1], 'DR-move', t[2], 'all-move', t[3])
print('\nclasses where FakeMMAP\'s HTR-breaking table differs from the all-move optimum:')
for t in tab:
    if t[4] is not None and t[4] != t[3]: print('  ', t[0][0], f'F-{t[0][1]} R-{t[0][2]} {t[0][3]}', 'half-turn', t[1], 'DR-move', t[2], 'all-move', t[3], 'FakeMMAP', t[4], '| a state of this class is produced by:', t[5])
with open('/data/fmc/research/out/table216.csv', 'w') as f:
    f.write('corners,F_edges,R_edges,E_parity,half_turn_only,DR_moves,all_moves,FakeMMAP_HTR_breaking,shortest_sequence_producing_a_state_of_the_class\n')
    for t in tab: f.write(','.join([t[0][0], 'F-' + t[0][1], 'R-' + t[0][2], t[0][3], str(t[1]), str(t[2]), str(t[3]), '' if t[4] is None else str(t[4]), t[5]]) + '\n')
