#!/bin/bash
# Independent recount for the htr-routes study (13 Nov 2026).  One job at a time, 3 threads, 3 GB cap.
# Build first:  cd vhtr && cargo build --release      (set V to the binary)
# Inputs: the first study's exact table (judging-a-dr/research/data/lean_exact_table.u8) and the per-state
# records of the main run (research/out/big).  Outputs: verify/out/*.txt.  About 50 minutes on the 4-core VM.
set -e
source /data/fmc/env.sh
B=/data/fmc/htr-routes/research
R=$B/out/big
O=$B/verify/out
V=${V:-$B/verify/vhtr/target/release/vhtr}
run() { RAYON_NUM_THREADS=3 systemd-run --user --scope -q -p MemoryMax=3G "$@"; }
mkdir -p $O

run $V check > $O/check_model.txt                          # table and coset sanity
run $V qtcos > $O/qt_cosets.txt                            # label x quarter turns to HTR, per HTR coset
awk -F'\t' '{split($3,a," "); n[$1]+=a[2]} END{for(k in n) print k"\t"n[k]}' $O/qt_cosets.txt | sort > $O/cosets_per_label.tsv
run $V s18 > $O/check_18.txt                               # every 18-move state: side half turns give 17
run $V lastmove > $O/lastmove.txt                          # exact share with X R2 one shorter
run $V nissall - > $O/niss_all.txt 2> $O/niss_all.log      # shortest NISS HTR of every DR state
run $V lsall $B/out/checks/lsdist48.tsv > $O/ls_all.txt 2> $O/ls_all.log   # leave-slice optimum of every state

for out in cmp_routes check_bound4 check_bound2 check_redcount_r7; do : > $O/$out.txt; done
for f in $R/run1/states_*.tsv; do
  c=$(basename $f .tsv); c=${c#states_}; name="${c/_/ }"
  # every H route at the optimum and at +1, HTR lengths, optimum, labels, NISS HTR: 500 states per subset x edges
  run $V cmp $f $R/run1/routes_$c.bin $R/run1/route_keys.tsv 12000 500 >> $O/cmp_routes.txt
  # bounding as stated, reductions up to 7 moves: 50 states
  run $V b4 $f $R/bound4.tsv "$name" 200 50 7 >> $O/check_bound4.txt
  # late-switch data and per-path window reductions (sections 9, 11, errata d and f): 300 states
  run $V b2 $f $R/bound2.tsv "$name" 12000 300 >> $O/check_bound2.txt
  # reduction counts by brute force, up to 7 moves: 10 states
  run $V rc $f $R/redcount2.tsv "$name" 100,101,102,103,104,105,106,107,108,109 7 >> $O/check_redcount_r7.txt
done

# aggregates, recomputed from the per-state records by separate scripts
for b in 0 2 99; do run python3 $B/verify/recount_checklist.py $b > $O/recount_checklist_b$b.txt; done   # 99 = no HTR limit
run python3 $B/verify/recount_via.py > $O/recount_via.txt
run python3 $B/verify/recount_t11503.py > $O/recount_t11503.txt
# the examples page, replayed
export VHTR=$V
run python3 $B/verify/check_examples_page.py > $O/check_examples_page.txt
# the errata examples
run $V ex "R2 D R2 F2 R2 D L2 D B2 R2 D2 B2 U" "R2 D R2 F2 R2 D L2 D B2 R2 D2 B2 U R2" \
  "D F2 R2 U2 B2 U' F2 U' F2 U L2 B2 U' R2 U'" "B2 U B2 R2 D' L2 U B2 D' F2 D' L2 F2 U' R2 U" \
  "F2 U' L2 U' F2 R2 F2 L2 U F2 D2 B2" "F2 D2 R2 D' R2 U2 B2 D' L2 U2 F2 U L2 R2" \
  "D2 F2 L2 U' B2 U' L2 U2 B2 U' L2 D R2 D2" "F2 U' B2 R2 B2 U R2" > $O/errata_examples.txt
run $V red "R2 B2 D2 B2 D U2 R2 U L2 F2 U' B2" 4 1 >> $O/errata_examples.txt
run $V red "R2 B2 D2 B2 D U2 R2 U L2 F2 U' B2" 5 1 >> $O/errata_examples.txt
