#!/bin/bash
# The two data gaps (out/SUMMARY.md).  Steps as they were run; the heavy ones ran on the second VM (fmc2: 8 cores,
# 31 GB) and their outputs were copied back here.  Every heavy step under a memory cap.
set -euo pipefail
source /data/fmc/env.sh
cd "$(dirname "$0")"
D=/data/fmc/judging-a-dr/research/data
CAP="systemd-run --user --scope -q -p MemoryMax=5G"
(cd src/htrreal && cargo build --release)          # htrtools fork: GAPS_STATES list mode + `label`
T=src/htrreal/target/release/htrtools

# Gap 1: the population (10,000 uniform scrambles, every EO-first DR <= 11, cubelib-cli as judging-a-dr's examples page)
$CAP python3 src/population.py 10000 4                                             # big/pop_raw.tsv   ~60 min, 4 cores
awk -F'\t' 'NR>2{print $7" "$8" "$9}' big/pop_raw.tsv > big/pop_ces.txt
$CAP $T label $D/lean_exact_table.u8 $D/ls_depth.u8 < big/pop_ces.txt > big/pop_label.tsv   # 45 s on 8 cores (fmc2)
python3 src/check_pop.py big/pop_raw.tsv 1000 7                                    # 1,000 DRs: drtools read + sticker replay
$CAP python3 src/pop_stats.py                                                      # (a) out/a_*.tsv
$CAP python3 src/make_sample.py 25000 20261113                                     # big/real/{list.txt,meta.tsv}
GAPS_STATES=big/real/list.txt $CAP $T routes $D/lean_exact_table.u8 $D/ls_depth.u8 0 1 big/real/run 2> big/real/routes.log   # 8.5 min on 8 cores
GAPS_STATES=big/real/list.txt $CAP $T bound4 $D/lean_exact_table.u8 0 1 big/real/bound4.tsv                                   # 1.5 min
$CAP python3 src/real_analysis.py                                                  # (b) out/b_*.tsv (uniform run reproduced too)
python3 src/compare.py                                                             # out/cmp_*.tsv

# Gap 2: all-move optimum (nissy optimal, 3.1 GB table) of 48,000 uniform + 23,976 real-population DR states
# inputs: big/g2/uni1000.tsv (htr-routes run1, first 1,000 per subset x edges); big/g2/real_states1000.tsv (46,928 states:
# 1,000 per subset x edges of big/real, all where fewer), cut to its first 500 per subset x edges for the run:
awk -F'\t' 'c[$1]++<500' big/g2/real_states1000.tsv > big/g2/real_states.tsv                            # 23,976 states
systemd-run --user --scope -q -p MemoryMax=12G python3 src/g2_solve.py big/g2/uni1000.tsv big/g2/uni1000.out 8
systemd-run --user --scope -q -p MemoryMax=12G python3 src/g2_solve.py big/g2/real_states.tsv big/g2/real.out 8
python3 src/g2_analysis.py                                                         # out/g2.tsv
python3 src/g2_examples.py pick 8; python3 src/g2_examples.py list; python3 src/g2_examples.py replay   # out/g2_examples.json
