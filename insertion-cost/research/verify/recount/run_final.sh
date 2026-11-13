#!/bin/bash
# every file again with the one final binary (recount/), results in final/
cd /data/disk/verify_ins
while ! grep -q "^done" res/times3.txt; do sleep 15; done
B=recount/target/release/recount
one() { # name kind mode limit outprefix
  s=$(date +%s)
  $B $2 data/$1.tsv 4 $3 $4 > final/$5$1.tmp 2> final/$5$1.err && mv final/$5$1.tmp final/$5$1.out
  echo "$5$1 $(( $(date +%s)-s ))s" >> final/times.txt
}
for n in 20 10 16 30; do one sample_3c_n$n one-c x 20000 ""; done
one base_3c_n21 one-c x 20000 ""
one sample_3e_n20 one-e x 20000 ""
for t in 5c 2c2c-twisted 2c2c-pure 3c1t 3tc; do one sample_${t}_n20 two-c x 20000 ""; done
one sample_2tc_n20 two-c x 5000 ""
one base_5c_n19 two-c x 20000 ""
one base_3c1t_n19 two-c x 20000 ""
one base_2c2c-pure_n19 two-c x 20000 ""
for t in 5c 2c2c-twisted 2c2c-pure 3c1t 3tc; do one sample_${t}_n16 two-c x 20000 ""; done
one sample_2tc_n16 two-c x 5000 ""
one sample_3c_n20 one-c any 20000 any_
one sample_5c_n20 two-c any 2000 any_
one sample_2c2c-twisted_n20 two-c any 2000 any_
echo done >> final/times.txt
