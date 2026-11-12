#!/bin/bash
# 50,000 random-state scrambles from nissy 2.0.8 `scramble` (four processes of 12,500, started a second apart),
# written to out/nissy_scrambles.txt (only for the uniformity check: nissy 2.0.8's
# scrambles are not uniform in corner orientation, see check_scrambles.py) after a check that no scramble repeats.
set -e
source /data/fmc/env.sh
cd "$(dirname "$0")/../out"
mkdir -p big
for i in 1 2 3 4; do
  (nissy scramble -n 12500 > big/scr_$i.txt) &
  sleep 1.5
done
wait
cat big/scr_[1-4].txt > nissy_scrambles.txt
n=$(wc -l < nissy_scrambles.txt); u=$(sort -u nissy_scrambles.txt | wc -l)
echo "scrambles: $n lines, $u distinct"
[ "$n" = "$u" ] && [ "$n" = 50000 ]
rm big/scr_[1-4].txt
