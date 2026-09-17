#!/bin/bash
cd "$(dirname "$0")"
M=24
for r in $(seq 0 $((M-1))); do
  ( geng -q -C 9 $r/$M | python3 check_lemmas.py > out9_$r.txt 2>&1 ) &
done
wait
echo "=== n=9 summary ==="
cat out9_*.txt | grep -v "^checked" | sort | uniq -c
grep -h "^checked" out9_*.txt | awk '{s+=$2} END {print "total graphs checked:",s}'
