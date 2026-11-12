#!/bin/bash
# Rebuild every number of the HTR-routes study.  One heavy job at a time, each capped at 5 GB (the VM has 7.7 GB,
# no swap).  Needs the first study's tables in judging-a-dr/research/data (see that README), Rust, the Python venv
# (numpy) and nissy (for the checks), all put on PATH by /data/fmc/env.sh.
set -euo pipefail
source /data/fmc/env.sh
cd "$(dirname "$0")"
D=/data/fmc/judging-a-dr/research/data
CAP="systemd-run --user --scope -q -p MemoryMax=5G"
T=./htrtools/target/release/htrtools
mkdir -p out/checks out/big

(cd htrtools && cargo build --release)

# 1. checks before anything is used
$CAP $T dist $D/lean_exact_table.u8 out/checks                     # per-subset optimal, HTR states, DR->HTR per subset
(cd src && python3 check_dist.py)                                   # vs first study, Joba doc 580 / 566, DougCube

# 2. the main pass: 25,000 uniform states per subset, every optimal and +1 finish, every NISS reading, X and X*R2
$CAP $T routes $D/lean_exact_table.u8 $D/ls_depth.u8 25000 20261112 out/big/run1 2> out/big/run1.log

# 3. one optimal per state with a random tie-break (how doc 171 and "nissy's first optimal" read a state),
#    DR bounding read on every finish (same states as step 2), reductions a solver writes
$CAP $T tie $D/lean_exact_table.u8 5000 7 out/big/tie.tsv
$CAP $T tiels $D/lean_exact_table.u8 $D/ls_depth.u8 5000 7 out/big/tiels.tsv
$CAP $T bound $D/lean_exact_table.u8 25000 20261112 out/big/bound.tsv
$CAP $T redcount $D/lean_exact_table.u8 100 20261112 5 out/big/redcount.tsv
$CAP $T redcount2 $D/lean_exact_table.u8 4000 20261112 7 out/big/redcount2.tsv   # exact counts, checked against redcount
$CAP $T bound2 $D/lean_exact_table.u8 25000 20261112 out/big/bound2.tsv          # paths, sections, C11 / C13 data
$CAP $T bound4 $D/lean_exact_table.u8 4000 20261112 out/big/bound4.tsv           # Q8 as stated: exact search on reductions
$CAP $T redcount $D/lean_exact_table.u8 10 20261112 7 out/big/redcount_brute7.tsv # brute-force check of redcount2 up to r = 7

# 4. independent checks: sticker model, nissy
(cd src && python3 check_sticker.py 1000 60)
(cd src && python3 check_c_invariance.py 3000)                     # half turns never change the subset x edges label (FakeMMAP's C)

# 5. analysis
cd src
python3 map_names.py                 # what doc 15 / 66 / 171 row labels mean (their own examples)
python3 stats_analysis.py            # Q3, Q4, Q5 per state; docs 15, 66, 9
$CAP python3 routes_analysis.py      # Q1, Q2, Q5 per route class
python3 checklist_cost.py            # Q2 with HTR budgets (the main checklist), mirror aliases
python3 edge_gain.py                # what the edge count is worth: own vs pooled checklists
$CAP python3 edge_steps.py           # edge counts along the route (H keys), edge-path checklists
python3 alias_check.py               # mirror pairs cover the same states
python3 check_redcount7.py           # reduction counts vs brute force, r <= 7
python3 compare_docs.py doc171       # doc 171 (full finish and leave slice)
python3 bounding.py                  # Q8 first pass, Q9 with alpha = 0 (superseded by bounding2.py)
$CAP python3 bounding2.py            # Q8 (counts, standard errors, vs checklist), Q9 with alpha per path, C11 / C13
python3 q8_stated.py                 # Q8 as stated (reduction + optimal finish of the reduced state)
$CAP python3 t11503_cex.py           # T11503 lower bounds as written and with alpha_(i+1): the cases where they fail
$CAP python3 xlbdist.py              # T11503 corrected lower bounds: typical values (out/q9_lb_values.tsv)
python3 grade.py                     # Q6
python3 claims.py                    # Q7 -> out/claims.tsv
python3 summary.py specs             # out/witness_specs.json
python3 witness.py                   # out/witness.json (every printed finish replayed on the sticker model)
python3 summary.py                   # out/SUMMARY.md
