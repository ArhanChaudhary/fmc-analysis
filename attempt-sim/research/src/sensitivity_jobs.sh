#!/bin/bash
# Job lines for the sensitivity stage: every time cost halved and doubled, and the human limits moved, each with the
# policies of policies/conclusions.toml on 2,000 held-out scrambles.  Writing slower (or faster) also scales the time the
# solver keeps for writing (cost.reserve_scale), since a solver knows their own writing speed.
# Prints one job per line: NAME POLICY SCRAMBLES FIRST COUNT [--set ...]
U="conclusions scrambles_uniform.txt 4000 2000"
echo "s_ref $U"
for k in look eo_write eo_eval rzp switch dr_read htr tail; do
  v=$(awk -v k=$k '$1 == k && $2 == "=" {print $3}' costs.toml)
  echo "s_${k}_h $U --set cost.$k=$(python3 -c "print($v/2)")"
  echo "s_${k}_d $U --set cost.$k=$(python3 -c "print($v*2)")"
done
echo "s_write_h $U --set cost.write=75 --set cost.reserve_scale=0.5"
echo "s_write_d $U --set cost.write=300 --set cost.reserve_scale=2"
echo "s_eo_scan_h $U --set cost.eo_scan=[0,1,1.5,2.5,5,15,60,200]"
echo "s_eo_scan_d $U --set cost.eo_scan=[0,4,6,10,20,60,240,800]"
echo "s_dr_find_h $U --set cost.dr_find=[1.5,1.5,2.5,4,6,10,15,22.5]"
echo "s_dr_find_d $U --set cost.dr_find=[6,6,10,16,24,40,60,90]"
echo "s_noise_h $U --set cost.noise_sigma=0.125"
echo "s_noise_d $U --set cost.noise_sigma=0.5"
echo "s_read_h $U --set human.read_sd=0.5"
echo "s_read_d $U --set human.read_sd=2"
echo "s_route_lo $U --set human.route_see=0.7"
echo "s_route_hi $U --set human.route_see=1"
echo "s_drsee_lo $U --set human.dr_see_work=[1,1,1,0.9,0.8,0.6,0.3,0.05] --set human.dr_see_glance=[1,1,0.9,0.75,0.4,0.1,0,0]"
echo "s_drsee_hi $U --set human.dr_see_work=[1,1,1,1,1,0.95,0.75,0.4] --set human.dr_see_glance=[1,1,1,1,0.8,0.5,0.2,0.05]"
echo "s_eosee_lo $U --set human.eo_see_lin=[1,1,1,1,0.85,0.5,0.1,0] --set human.eo_see_niss=[1,1,0.8,0.7,0.4,0.1,0,0]"
echo "s_eosee_hi $U --set human.eo_see_lin=[1,1,1,1,1,0.9,0.5,0.2] --set human.eo_see_niss=[1,1,1,1,0.9,0.6,0.2,0.05]"
