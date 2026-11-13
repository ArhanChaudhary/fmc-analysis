#!/usr/bin/env python3
"""One worked DR per rule of the "half turns before the first qt" part, and a sticker-model check of the reads.

Witnesses (out/ht_first_witness.json).  Each is a sampled state picked by the reads of ht_first.py; then, without
those reads:
  * every optimal finish is enumerated with check_ht_first.py's own search on the exact table;
  * the scramble is the inverse of the first finish; every finish is replayed on the sticker model (sticker.py) and
    must solve it; the subset x edges on normal and inverse is the sticker model's label;
  * per finish, the half turns before its first quarter turn (normal) and after its last (inverse) are counted from the
    move names;
  * "trigger-ready" and the corner setup count are recomputed on the sticker model for both sides (corner arrangement
    of the scrambled cube and of its inverse; sticker.QTC is the corners' quarter-turn count);
  * the first study's reader (judging-a-dr/research/tool/drread, its own cube model and its drbfs table) gives the
    subset, the optimum and the corner case on both sides from the scramble alone.
Reads check (out/checks/check_ht_first_reads.txt): for the first K states of every subset x edges, the corner setup
count on both sides from the sticker model against ht_first.py's coset tables; for the first J of the key rows, the
corner case names against drread.
usage: ht_first_witness.py [K] [J]"""
import sys, os, json, subprocess, re, collections
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import ht_first as H, common, sticker
import check_ht_first as C
from sticker import do, SOLVED, inv_seq, QT, HALF
R = H.R; OUT = os.path.join(R, 'out')
DRREAD = ['/data/fmc/venv/bin/python', '/data/fmc/judging-a-dr/research/tool/drread']
K = int(sys.argv[1]) if len(sys.argv) > 1 else 100
J = int(sys.argv[2]) if len(sys.argv) > 2 else 40
NAMES = C.NAMES

def setup_sticker(arr):
    """fewest half turns before a U or D quarter turn lowers the corners' quarter-turn count (sticker model);
    also the quarter turns that lower it right now"""
    q = sticker.QTC[arr]
    if q == 0: return 9, []
    now = [m for m in sorted(QT) if sticker.QTC[sticker.cmul(arr, sticker.CMOV[m])] == q - 1]
    seen = {arr}; fr = [arr]; h = 0
    while fr:
        if any(sticker.QTC[sticker.cmul(x, sticker.CMOV[m])] == q - 1 for x in fr for m in QT): return h, now
        nx = []
        for x in fr:
            for m in HALF:
                y = sticker.cmul(x, sticker.CMOV[m])
                if y not in seen: seen.add(y); nx.append(y)
        fr = nx; h += 1
    raise AssertionError

def merged(lab):          # the sticker model names 4c3 / 4c4 by side (4a3 or 4b3, 4a4 or 4b4)
    return ('4c' + lab[2:]) if lab[:2] in ('4a', '4b') and lab[2] in '34' else lab

def scramble_of(c, e, s):
    d = C.depth(c, e, s)
    fs = C.finishes(c, e, s, d)
    return d, fs, inv_seq([NAMES[m] for m in fs[0]])

def drread(scrs):
    out = []
    for i in range(0, len(scrs), 20):
        p = subprocess.run(DRREAD + sum((['--dr', ' '.join(x)] for x in scrs[i:i + 20]), []), capture_output=True, text=True, check=True)
        for block in p.stdout.strip().split('\n\n'):
            m = re.search(r'subset (\S+ \S+);', block); cc = re.search(r'corner case: (\S+) on normal, (\S+) on inverse', block)
            opt = re.search(r'truth: optimal finish (\d+)', block)
            out.append(dict(subset=m.group(1), case_normal=cc.group(1), case_inverse=cc.group(2), optimal=int(opt.group(1))))
    assert len(out) == len(scrs)
    return out

def main():
    X = H.Data(); D = X.D
    SC = np.minimum(X.sC[0], X.sC[1]); SCmax = np.maximum(X.sC[0], X.sC[1])
    nopt = np.zeros(X.n, np.int64)
    for s in common.SUBS:
        m = X.sub == s; nopt[m] = common.load_states(s)['nopt']
    name = np.array([X.case_name[k] for k in range(max(X.case_name) + 1)])
    cn, ci = name[X.case[0]], name[X.case[1]]
    def pick(mask, want_nopt=(2, 3, 4, 1, 5, 6)):
        idx = np.where(mask)[0]
        for w in want_nopt:
            hit = idx[nopt[idx] == w]
            if len(hit): return int(hit[0])
        return int(idx[0])
    specs = [
        ('H1', 'rule 1: a 2c4 2e that is trigger-ready on neither side and needs one half turn before the first qt on both sides',
         (X.sub == '2c4 2e') & (X.d <= 13) & (SC == 1) & (X.t0 == 1)),
        ('H2', 'rule 1, the other way: a 2c4 2e that is trigger-ready on a side and whose optimal starts with that qt',
         (X.sub == '2c4 2e') & (X.d <= 13) & (X.sC[0] == 0) & ((D['q0n'] & X.qC_t[D['ccn']]) != 0) & (X.sC[1] >= 1) & (D['a0i'] >= 1)),
        ('H3', 'rule 2: a 4a2 4e whose corners need two half turns on both sides, and whose optimal needs two half turns before the first qt',
         (X.sub == '4a2 4e') & (X.d <= 13) & (X.sC[0] == 2) & (X.sC[1] == 2) & (X.t0 == 2)),
        ('H4', 'the limit of the reads: a 2c4 2e that is trigger-ready on both sides and still needs two half turns before the first qt on both sides',
         (X.sub == '2c4 2e') & (X.d <= 13) & (SCmax == 0) & (X.t0 == 2)),
        ('H5', 'a 4a2 4e with 4-0 corners on both sides: three half turns before the first qt',
         (X.sub == '4a2 4e') & (X.d <= 13) & (X.sC[0] == 3) & (X.sC[1] == 3) & (X.t0 == 3)),
        ('H6', 'a 4b2 2e that is ready on neither side and whose optimal starts with a quarter turn all the same: every optimal finish has 4 quarter turns',
         (X.sub == '4b2 2e') & (X.d <= 13) & (SC >= 1) & (X.t0 == 0) & (D['a0n'] == 0) & ~X.hasmin),
    ]
    wit = []; ok_all = True
    for wid, finding, mask in specs:
        i = pick(mask)
        c, e, s = int(D['c'][i]), int(D['e'][i]), int(D['s'][i])
        d, fs, scr = scramble_of(c, e, s)
        st = do(SOLVED, scr); sti = do(SOLVED, inv_seq(scr))
        fin = []
        ok = True
        for x in fs:
            mv = [NAMES[m] for m in x]
            ok &= do(st, mv) == SOLVED and len(mv) == d
            fin.append(dict(finish=' '.join(mv), half_turns_before_first_qt_normal=C.lead(x), half_turns_before_first_qt_inverse=C.trail(x),
                            quarter_turns=sum(1 for m in x if C.ISQ[m])))
        sn, nown = setup_sticker(sticker.corners(st)); si, nowi = setup_sticker(sticker.corners(sti))
        dr = drread([scr])[0]
        ent = dict(id=wid, finding=finding, state=f'#{c},{e},{s}', sample=f'{X.sub[i]} #{int(D["idx"][i])}', scramble=' '.join(scr), optimal=d,
                   subset_normal=sticker.label(st), subset_inverse=sticker.label(sti), n_optimal_finishes=len(fs), optimal_finishes=fin,
                   fewest_half_turns_before_first_qt=dict(normal=min(f['half_turns_before_first_qt_normal'] for f in fin),
                                                          inverse=min(f['half_turns_before_first_qt_inverse'] for f in fin)),
                   corner_setup_sticker=dict(normal=sn, inverse=si), qt_that_lowers_now=dict(normal=nown, inverse=nowi),
                   corner_case=dict(normal=dr['case_normal'], inverse=dr['case_inverse']), drread_subset=dr['subset'], drread_optimal=dr['optimal'])
        ok &= dr['optimal'] == d and dr['subset'] == X.sub[i] == merged(ent['subset_normal'])
        ok &= (sn, si) == (int(X.sC[0][i]), int(X.sC[1][i])) and (dr['case_normal'], dr['case_inverse']) == (cn[i], ci[i])
        ok &= ent['fewest_half_turns_before_first_qt'] == dict(normal=int(D['a0n'][i]), inverse=int(D['a0i'][i]))
        # quarter turns: the fewest any finish can have (the data's qtf; on the subsets used here it is the corners' count,
        # which the sticker model gives), and whether some optimal finish has no extra one
        ent['fewest_quarter_turns_of_any_finish'] = int(X.qtf[i]); ent['corner_quarter_turns_sticker'] = int(sticker.QTC[sticker.corners(st)])
        ent['an_optimal_has_no_extra_quarter_turn'] = any(f['quarter_turns'] == ent['fewest_quarter_turns_of_any_finish'] for f in fin)
        ok &= ent['fewest_quarter_turns_of_any_finish'] == ent['corner_quarter_turns_sticker'] and ent['an_optimal_has_no_extra_quarter_turn'] == bool(X.hasmin[i])
        ent['replayed_ok'] = bool(ok); ok_all &= ok
        wit.append(ent)
        print(wid, ent['sample'], ent['scramble'], '| optimal', d, '|', len(fs), 'finishes | setup', sn, si, '| cases', dr['case_normal'], dr['case_inverse'], '| ok', ok, flush=True)
        for f in fin: print('    ', f['finish'], f['half_turns_before_first_qt_normal'], f['half_turns_before_first_qt_inverse'])
    json.dump(wit, open(f'{OUT}/ht_first_witness.json', 'w'), indent=1)

    if not (K or J):            # witnesses only: the reads check file is left as it is
        print('witnesses', len(wit), 'all replayed and re-read:', ok_all); return
    # reads check
    lines = [f'ht_first_witness.py {K} {J}: the reads of ht_first.py against the sticker model and against drread']
    tot = collections.Counter()
    for s in common.SUBS:
        idx = np.where(X.sub == s)[0][:K]
        for i in idx:
            c, e, sl = int(D['c'][i]), int(D['e'][i]), int(D['s'][i])
            d, fs, scr = scramble_of(c, e, sl)
            st = do(SOLVED, scr); sti = do(SOLVED, inv_seq(scr))
            sn, _ = setup_sticker(sticker.corners(st)); si, _ = setup_sticker(sticker.corners(sti))
            tot['states'] += 1
            tot['setup_mismatch'] += (sn, si) != (int(X.sC[0][i]), int(X.sC[1][i]))
            tot['label_mismatch'] += merged(sticker.label(st)) != s
    todo = []
    for s in ('2c4 2e', '2c3 2e', '4a2 4e', '4a1 4e', '4b2 2e', '4c3 2e', '0c3 4e', '2c5 2e', '4c4 2e', '4b5 2e', '0c4 2e'):
        for i in np.where(X.sub == s)[0][:J]:
            d, fs, scr = scramble_of(int(D['c'][i]), int(D['e'][i]), int(D['s'][i]))
            todo.append((i, scr, d))
    for (i, scr, d), dr in zip(todo, drread([t[1] for t in todo])):
        tot['drread_states'] += 1
        tot['case_mismatch'] += (dr['case_normal'], dr['case_inverse']) != (cn[i], ci[i])
        tot['drread_optimal_mismatch'] += dr['optimal'] != d
        tot['drread_subset_mismatch'] += dr['subset'] != X.sub[i]
    for k in ('states', 'setup_mismatch', 'label_mismatch', 'drread_states', 'case_mismatch', 'drread_optimal_mismatch', 'drread_subset_mismatch'):
        lines.append(f'{k}\t{tot[k]}')
    lines.append(f'witnesses\t{len(wit)}\tall replayed and re-read: {ok_all}')
    good = ok_all and all(tot[k] == 0 for k in tot if 'mismatch' in k)
    lines.append('ALL EQUAL' if good else 'DIFFERENCES FOUND')
    open(f'{OUT}/checks/check_ht_first_reads.txt', 'w').write('\n'.join(lines) + '\n')
    print('\n'.join(lines))

if __name__ == '__main__':
    main()
