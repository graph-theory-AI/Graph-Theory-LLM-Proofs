#!/bin/bash
cd "$(dirname "$0")"
M=72
rm -f r11_*.txt
for r in $(seq 0 $((M-1))); do
  ( geng -q -C 11 $r/$M | ./eta2 2 0 > r11_$r.txt ) &
done
wait
grep -h VIOLATION r11_*.txt > rviol11.txt
awk '{for(i=1;i<=NF;i++) if($i ~ /^non-exceptional-min-eta=/){split($i,a,"=");print a[2]}}' r11_*.txt | sort -n | head -1 > rmin11.txt
awk '{for(i=1;i<=NF;i++) if($i ~ /^graphs=/){split($i,a,"=");s+=a[2]}} END{print s}' r11_*.txt > rcount11.txt
echo "n=11 rerun done: min=$(cat rmin11.txt) graphs=$(cat rcount11.txt) violations=$(wc -l < rviol11.txt)"
