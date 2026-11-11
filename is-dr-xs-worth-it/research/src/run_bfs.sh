#!/bin/bash
# Every search of the study: for each move rule and each target class, the fewest turns from every coset.
# One at a time, memory capped (the table is 2.2 GB in RAM).  About 1.5 minutes each.
cd /data/fmc/is-dr-xs-worth-it/research
for rule in all eo-fb eo-ud seo-fb seo-ud; do
  for tgt in dr 1s 2s8fe xs 1s_fix4; do
    out=out/bfs/${rule}_${tgt}
    [ -s $out.hist ] && continue
    systemd-run --user --scope -q -p MemoryMax=4G xstools/target/release/xstools bfs out/tables $rule out/targets/$tgt.txt $out.u8 > $out.hist.tmp 2> $out.log && mv $out.hist.tmp $out.hist
  done
done
echo ALL DONE
