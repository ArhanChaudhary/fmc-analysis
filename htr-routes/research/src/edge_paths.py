#!/usr/bin/env python3
"""Edge paths of the optimal finish, read forward (section 4, "Edge paths of the finish").

Input: `htrtools edgepaths` (out/big/edgepaths/ep_<subset>.tsv, ep_keys.tsv) on the same 25,000 states per subset x
edges as the main pass (out/big/run1/states_<subset>.tsv).  For every finish of length <= optimum + 1, the label
(corner subset and bad edges) of the start and of the state after each quarter turn, up to the first state in HTR,
read forward on the normal side only.  The *form* of a finish is that edge path, written with HTR for its last state.

A DR *has* a form at a target if some finish of that length has it:
  opt  some optimal finish                        (HTR any length)
  opt2 some optimal finish whose HTR is at most the DR's shortest NISS HTR + 2 (budget 2, as the checklists)
  p1   some finish of length <= optimum + 1       (HTR any length)
One DR has several optimal finishes, so the shares of the forms of one row add up to more than 100%.

Outputs (all sampled, 25,000 per subset x edges):
  out/edge_paths.tsv         subset, target, rank, path, share, union of the first `rank` paths (paths >= 0.1%)
  out/edge_paths_step1.tsv   subset, target, next corner subset after the first quarter turn (or HTR), share with any
                             edge count, then per edge count (0e .. 8e)
  out/edge_paths_step2.tsv   subset, target, first step (label after the first qt), share that can take it, next corner
                             subset after the second qt, and of the DRs that can take the first step, the share that
                             can go on to it with any edge count / each edge count (the same finish)
  out/edge_paths_meta.json   per subset x edges: states, capped, mean number of forms per DR, share with one form
Light: one subset in memory at a time."""
import os, json, collections, csv
import numpy as np
from common import SUBS, OUT, RUN, load_states, fname

EP = os.path.join(OUT, 'big', 'edgepaths')
EDG = ('0e', '2e', '4e', '6e', '8e')
TGS = ('opt', 'opt2', 'p1')

def load_keys():
    K = {}
    with open(os.path.join(EP, 'ep_keys.tsv')) as f:
        next(f)
        for l in f:
            i, p = l.rstrip('\n').split('\t')
            K[int(i)] = p.split(' > ')
    return K

def fmt(labs):
    """'2c4 2e > 2c3 2e > 4b2 2e > 4a1 4e > HTR'; a start already in HTR is just 'HTR'"""
    return ' > '.join(labs[:-1] + ['HTR'])

def load_ep(sub):
    rows = []
    with open(os.path.join(EP, f'ep_{fname(sub)}.tsv')) as f:
        next(f)
        for l in f:
            v = l.rstrip('\n').split('\t')
            ent = []
            for x in v[4:]:
                i, dl, ho, ha = map(int, x.split(':'))
                ent.append((i, dl, ho, ha))
            rows.append((int(v[0]), int(v[1]), int(v[2]), int(v[3]), ent))
    rows.sort()
    return rows

def sets_of(rows, niss):
    """per state: the set of path ids it has at each target"""
    out = {t: [] for t in TGS}
    for (idx, d, cap, nopt, ent), nh in zip(rows, niss):
        out['opt'].append({i for i, dl, ho, ha in ent if dl == 0})
        out['opt2'].append({i for i, dl, ho, ha in ent if dl == 0 and ho <= nh + 2})
        out['p1'].append({i for i, dl, ho, ha in ent})          # every entry is a finish of length <= optimum + 1
    return out

def main():
    K = load_keys()
    fp = open(f'{OUT}/edge_paths.tsv', 'w'); fp.write('subset\ttarget\trank\tpath\tshare\tunion\n')
    f1 = open(f'{OUT}/edge_paths_step1.tsv', 'w')
    f1.write('subset\ttarget\tnext\tany\t' + '\t'.join(EDG) + '\n')
    f2 = open(f'{OUT}/edge_paths_step2.tsv', 'w')
    f2.write('subset\ttarget\tfirst\tfirst_share\tnext\tany\t' + '\t'.join(EDG) + '\n')
    meta = {}
    for s in SUBS:
        st = load_states(s)
        rows = load_ep(s)
        n = len(rows)
        assert [r[0] for r in rows] == list(st['idx']) and all(r[1] == d for r, d in zip(rows, st['d'])), s
        niss = st['htrNiss']
        S = sets_of(rows, niss)
        # every optimal finish of every state starts at the state's own label
        assert all(K[i][0] == st['lab_n'][j] for j, ss in enumerate(S['opt']) for i in ss), s
        nf = np.array([len(x) for x in S['opt']])
        meta[s] = {'states': n, 'capped': int(sum(r[2] for r in rows)), 'mean_forms': float(nf.mean()),
                   'one_form': float((nf == 1).mean()), 'already_htr': int(sum(1 for x in S['opt'] if any(len(K[i]) == 1 for i in x)))}
        for tg in TGS:
            sets = S[tg]
            cnt = collections.Counter(i for x in sets for i in x)
            ranked = sorted(cnt.items(), key=lambda kv: (-kv[1], fmt(K[kv[0]])))
            covered = np.zeros(n, bool)
            mem = collections.defaultdict(list)
            for j, x in enumerate(sets):
                for i in x: mem[i].append(j)
            for r, (i, c) in enumerate(ranked):
                if c / n < 0.001: break
                covered[mem[i]] = True
                fp.write(f'{s}\t{tg}\t{r + 1}\t{fmt(K[i])}\t{c / n:.4f}\t{covered.mean():.4f}\n')
            # first step: label after the first quarter turn ('HTR' if that state is in HTR)
            nxt = collections.defaultdict(set)      # label or 'corner *' -> states
            two = collections.defaultdict(set)      # (first label, next label / 'corner *') -> states
            for j, x in enumerate(sets):
                for i in x:
                    labs = K[i]
                    if len(labs) < 2: continue
                    a = 'HTR' if len(labs) == 2 else labs[1]
                    nxt[a].add(j)
                    if a != 'HTR': nxt[a.split()[0] + ' *'].add(j)
                    else: nxt['HTR *'].add(j)
                    if a == 'HTR': continue
                    b = 'HTR' if len(labs) == 3 else labs[2]
                    two[(a, b)].add(j); two[(a, (b.split()[0] if b != 'HTR' else 'HTR') + ' *')].add(j)
            for c in sorted({k.split()[0] for k in nxt}):
                tot = len(nxt[c + ' *'])
                if c == 'HTR':
                    f1.write(f'{s}\t{tg}\tHTR\t{tot / n:.4f}' + '\t' * len(EDG) + '\n'); continue
                f1.write(f'{s}\t{tg}\t{c}\t{tot / n:.4f}\t' + '\t'.join(f'{len(nxt[f"{c} {e}"]) / n:.4f}' for e in EDG) + '\n')
            for a in sorted(k for k in nxt if not k.endswith('*') and k != 'HTR'):
                na = len(nxt[a])
                for c in sorted({b.split()[0] for (a2, b) in two if a2 == a}):
                    tot = len(two[(a, c + ' *')])
                    if c == 'HTR':
                        f2.write(f'{s}\t{tg}\t{a}\t{na / n:.4f}\tHTR\t{tot / na:.4f}' + '\t' * len(EDG) + '\n'); continue
                    f2.write(f'{s}\t{tg}\t{a}\t{na / n:.4f}\t{c}\t{tot / na:.4f}\t' + '\t'.join(f'{len(two[(a, f"{c} {e}")]) / na:.4f}' for e in EDG) + '\n')
        fp.flush(); f1.flush(); f2.flush()
        print(s, meta[s], flush=True)
    json.dump(meta, open(f'{OUT}/edge_paths_meta.json', 'w'), indent=1)

if __name__ == '__main__':
    main()
