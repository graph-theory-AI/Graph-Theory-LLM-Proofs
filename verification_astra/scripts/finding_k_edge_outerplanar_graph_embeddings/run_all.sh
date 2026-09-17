#!/bin/sh
# Reproduce every check (python3 with networkx 3.6.1).
for f in check1_lemma1.py check2_ell.py check3_profile.py check4_toplevel.py \
         check5_pnode.py check5b_pnode_random.py check6_snode.py check7_rnode.py \
         check8_cutvertex.py check9_hard.py check10_endtoend.py check11_sweep.py ; do
  echo "=== $f ==="
  python3 "$f"
done
