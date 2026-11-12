#!/bin/bash
# The greedy runs of section 8.4 (Python, three workers; about 25 minutes in all).
set -e
cd /data/fmc/insertion-cost/research/src
P=/data/fmc/venv/bin/python
$P xgreedy.py 5c 20 8 20000 --full          # every first comm followed up: must equal the tool's `two` on all 20,000
$P xgreedy.py 5c 20 8 20000
for n in 12 14 16 18 24; do $P xgreedy.py 5c $n 8 5000; done
for t in 2tc 3tc 2c2c-pure 2c2c-twisted 3c1t 3c3c; do $P xgreedy.py $t 20 8 5000; done
$P xgreedy.py 5c 20 10 2000
$P xgreedy_sum.py
