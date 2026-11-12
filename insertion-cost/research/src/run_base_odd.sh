#!/bin/bash
# Samples at the odd skeleton lengths 11..29 for the corner types of section 7 (cap 8 on 20,000 skeletons, 5,000 for
# 2tc; cap 10 on the usual smaller numbers), so that no odd length has to be read off between two even ones.
# 3c and 5c already have all of them (out/base_3c_n*.tsv, base_5c_n*.tsv).  One job at a time, memory capped.
set -e
source /data/fmc/env.sh
R=/data/fmc/insertion-cost/research
B=$R/instools/target/release/instools
CAP="systemd-run --user --scope -q -p MemoryMax=4500M"
$CAP $B runs 2tc 11,13,15,17,19,21,23,25,27,29 20000 2026 --L 8,10 --prefix base 2>> $R/out/runs_base.log
$CAP $B runs 3tc 11,15,17,19,21,23,25,27,29 20000 2026 --L 8,10 --prefix base 2>> $R/out/runs_base.log
$CAP $B runs 2c2c-pure 11,13,17,19,21,25,27,29 20000 2026 --L 8,10 --prefix base 2>> $R/out/runs_base.log
$CAP $B runs 2c2c-twisted 11,13,15,17,19,21,25,27,29 20000 2026 --L 8,10 --prefix base 2>> $R/out/runs_base.log
$CAP $B runs 3c1t 11,21,23,27,29 20000 2026 --L 8,10 --prefix base 2>> $R/out/runs_base.log
