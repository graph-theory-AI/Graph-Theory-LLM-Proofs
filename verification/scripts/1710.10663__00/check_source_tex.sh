#!/bin/sh
# Reproduce the source check: download arXiv:1710.10663 (v2) TeX source and show
# the actual definition of c_L, tau_L, maxcode_L, Theorems 1-2 and the conjecture line.
set -e
d=$(mktemp -d)
cd "$d"
curl -sL -o src.tar.gz https://arxiv.org/e-print/1710.10663
tar xzf src.tar.gz
echo "=== c_L / conjecture / Levenshtein lines in listdecoding.tex ==="
grep -n "c_L=2^{-L}\|maxcode_2(\\\\veps)=\|We believe\|tau_L\\\\eqdef" listdecoding.tex
echo
sed -n '150,210p' listdecoding.tex
