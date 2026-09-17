"""Exhaustive 1-,2-,3-edge perturbations of the two extremal families at n=12,13."""
import sys
from itertools import combinations
sys.path.insert(0,'/home/enatale/repos/lelarge/graph-theory-auto/verification_astra/scripts/1602.05184__00')
from families import eta, two_conn, exceptional
from check_sharpness import cone_path, clique_plus_edge
for n in [12,13]:
    for name, mk in [("K1+P(n-1)", cone_path), ("clique+matching", clique_plus_edge)]:
        nn, A0 = mk(n)
        A0=[set(s) for s in A0]
        pairs=list(combinations(range(n),2)); best=None; cnt=0; bad=0
        for k in (1,2,3):
            for flips in combinations(pairs,k):
                A=[set(s) for s in A0]
                for (i,j) in flips:
                    if j in A[i]: A[i].discard(j); A[j].discard(i)
                    else: A[i].add(j); A[j].add(i)
                if not two_conn(n,A) or exceptional(n,A): continue
                e=eta(n,A); cnt+=1
                if best is None or e<best: best=e
                if e<2*n: bad+=1
        print(f"n={n} {name}: {cnt} perturbed graphs (<=3 flips), min eta={best}, 2n={2*n}, below2n={bad}")
        sys.stdout.flush()
