"""Exhaustive 1- and 2-edge perturbations of the two extremal families at n=12,13,14."""
import sys
from itertools import combinations
sys.path.insert(0,'/home/enatale/repos/lelarge/graph-theory-auto/verification_astra/scripts/1602.05184__00')
from search_large import eta_and_ok, two_connected, exceptional
from check_sharpness import cone_path, clique_plus_edge

for n in [12,13,14]:
    for name, mk in [("K1+P(n-1)", cone_path), ("clique+matching", clique_plus_edge)]:
        nn, A0 = mk(n)
        pairs = list(combinations(range(n),2))
        best = None; cnt=0
        for k in (1,2):
            for flips in combinations(pairs,k):
                A=[set(s) for s in A0]
                for (i,j) in flips:
                    if j in A[i]: A[i].discard(j); A[j].discard(i)
                    else: A[i].add(j); A[j].add(i)
                if not two_connected(n,A): continue
                if exceptional(n,A): continue
                e=eta_and_ok(n,A); cnt+=1
                if best is None or e<best: best=e
        print(f"n={n} {name}: {cnt} perturbed 2-connected non-exceptional graphs, min eta = {best}, 2n={2*n}")
        sys.stdout.flush()
