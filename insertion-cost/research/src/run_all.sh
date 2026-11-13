#!/bin/bash
# Everything, in order.  Heavy steps run one at a time under a memory cap.
set -e
source /data/fmc/env.sh
R=/data/fmc/insertion-cost/research
B=$R/instools/target/release/instools
CAP="systemd-run --user --scope -q -p MemoryMax=4500M"
cd $R/src && python export_tables.py                      # move / rotation tables and test vectors from cube.py
cd $R/instools && cargo build --release --offline
$B selftest                                               # cube model and cancel against cube.py
$B count                                                  # sizes of the types, three ways
$CAP $B algs 8 --check all                                # all sequences <= 8, cases files, class-by-class check
$CAP $B algs 10 --check all                               # (about 9 minutes)
$CAP $B algs 12 --check simple > $R/out/algs_L12.log 2>&1 # (about 20 minutes; the class-by-class search is the slow part)
$B bf1 200 1; $B bf1 200 2 --type 3e                      # one insertion against a direct enumeration, L = 8, n = 6
$B bf1 30 4 --L 10 --n 6; $B bf1 30 4 --L 10 --n 6 --type 2e2e; $B bf1 30 4 --L 10 --n 6 --type 5c
python $R/src/check_algs_sticker.py 6 8                   # lists of sequences against an enumeration on the sticker model
for t in 2tc 3tc 2c2c-pure 2c2c-twisted 3c1t 5c 3c3c 2f 2e2e 2e2e-flipped 5e 3e1f 3e3e; do
  $B bf2 $t 12 300 7 8                                    # two insertions against the plain enumeration, L = 8
  $B bf2 $t 7 40 11 10                                    # and L = 10
done
$B bf2 5c 5 8 3 10 --mixed; $B bf2 3c1t 6 8 4 10 --mixed; $B bf2 2c2c-twisted 6 8 4 10 --mixed; $B bf2 5e 4 6 4 10 --mixed
$B best --file $R/out/if_cases.tsv --L 8,10,12 --mixed > $R/out/if_best.txt
python $R/src/check_solutions.py best $R/out/if_best.txt
# the sampling runs: out/sample_<type>_n<n>.tsv (n = 20 first); `two` on fewer skeletons at L = 10, see `plan` in main.rs
$CAP $B runs all 20,10,30,14,26,12,16,18,22,24,28 20000 2026 --L 8,10,12 2> $R/out/runs.log
python $R/src/check_solutions.py sample $R/out/sample_*_n*.tsv
python $R/src/summarize.py
# two smaller runs on the first skeletons of the n = 20 cells: the mixed model at L = 10, and `two` at L = 12
$CAP $B runs all 20 200 2026 --L 10 --two 10:200 --mixed 10:200 --prefix mixed 2> $R/out/runs_mixed.log
$CAP $B runs 3c3c,5c,3c1t,3tc,3e3e,5e,2c2c-pure,2c2c-twisted,3e1f 20 100 2026 --L 12 --two 12:100 --prefix two12 2> $R/out/runs_two12.log
python $R/src/summarize.py 'mixed_*_n20.tsv' summary_mixed.tsv
python $R/src/summarize.py 'two12_*_n20.tsv' summary_two12.tsv
python $R/src/if_table.py                                 # out/if_compare.tsv

# ---- added for the report (in this order)
$B selftest; $B count                                     # (again, recorded by checks.py)
python $R/src/histograms.py                               # out/hist.json from the sample files
python $R/src/py3.py                                      # all 3c / 3e sequences up to 10 moves from `instools list`, replayed on the sticker model
python $R/src/xone.py 10,12,14,16,18,20,22,24,26,28,30    # one comm spot by spot in Python: out/onepos_3c_n*.tsv; must equal the tool everywhere
python $R/src/facts.py                                    # out/facts.json
python $R/src/corpus_cyprian.py                           # out/corpus_cyprian.tsv (Kalbarczyk's example solves)
python $R/src/real_cases.py                               # the server's worked examples on the sticker model: out/real_cases.tsv, real_meta.json
python $R/src/real_run.py                                 # `best --L 8,10,12 --mixed` per case, 120 s limit (about 40 minutes the first time)
python $R/src/xreal.py --need                             # which odd-length cells the comparison needs; then, for each line it prints:
#   $CAP $B runs <type> <lengths> 20000 2026 --L 8,10 --prefix base     (and 3c 13,27 and 5c 19,23,27,29 for the corpus test)
$R/src/run_base_odd.sh                                    # samples at the odd lengths 11..29 for the corner types of section 7 (about 7 minutes)
$CAP $B twistmin 12 > $R/out/twistmin_L12.txt             # corner-only sequences of up to 12 moves that leave a corner twisted in place
python $R/src/histograms.py
python $R/src/xreal.py --corpus && python $R/src/xreal.py # real sequences with random leftovers; out/real.json and the real_* tables
$R/src/run_greedy.sh                                      # two comms the way people do them (about 25 minutes); out/greedy*.tsv, greedy.json
python $R/src/xdr.py                                      # trig0n's three kinds of 17-move skeleton
python $R/src/checks.py                                   # every check again, with its output: out/checks.txt, checks.json
python $R/src/xtables.py && python $R/src/witness.py      # report/data/*.md, the example scrambles
python $R/src/xexamples.py --cases                        # the 200 play-along skeletons (one two-phase solve each)
python $R/src/tables6.py                                  # the same tables at six decimals (out/data6): differences of two cells are taken from these
python $R/src/report_build/assemble.py --final && python $R/src/report_build/assemble.py --bugs --final
python $R/src/xexamples.py                                # report/EXAMPLES.md, then replays everything on the page
python $R/src/checks.py --report                          # witness blocks, examples page, quotations
