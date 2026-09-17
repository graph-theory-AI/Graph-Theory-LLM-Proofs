#!/bin/bash
cd "$(dirname "$0")"
M=48
for r in $(seq 0 $((M-1))); do
  ( geng -q -C 11 $r/$M | ./eta 2 0 > out11_$r.txt ) &
done
wait
grep -h VIOLATION out11_*.txt > viol11.txt
awk '{for(i=1;i<=NF;i++) if($i ~ /^non-exceptional-min-eta=/){split($i,a,"=");print a[2]}}' out11_*.txt | sort -n | head -1 > min11.txt
awk '{for(i=1;i<=NF;i++) if($i ~ /^graphs=/){split($i,a,"=");s+=a[2]}} END{print s}' out11_*.txt > count11.txt
echo done
