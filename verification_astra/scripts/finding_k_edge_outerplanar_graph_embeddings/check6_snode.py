"""Check 6: the S-node recurrence (14): ell = min ell_i,
F_H(d) = max( max_i F_i(d), max over internal skeleton vertices w(v) )."""
import itertools, random
from comps import *
INF=float('inf')

lib=[edge_comp(), path2(0), path2(3), path3(0,2), cyc_pair(), k4me(), doubleedge()]
random.seed(23)
tested=0; bad=0
cases=[]
for r in (2,3):
    for combo in itertools.combinations_with_replacement(range(len(lib)), r):
        cases.append([lib[i] for i in combo])
random.shuffle(cases)
for children in cases[:40]:
    iw=[random.choice([0,0,2,4]) for _ in range(len(children)-1)]
    Sc=series(children, iw)
    g,rho,w=Sc.hat()
    if sum(max(len(g.inc[v])-1,0) for v in range(g.n))>13: continue
    Ltrue,Ftrue=Sc.brute_profile()
    cp=[c.brute_profile() for c in children]
    Lalg=min(c[0] for c in cp)
    if Ltrue!=Lalg:
        bad+=1; print("S ELL MISMATCH", [c.name for c in children], Ltrue, Lalg)
    for d in range(min(Ltrue,Lalg)+1):
        tested+=1
        alg=max(max(cp[i][1][d] for i in range(len(children))), max(iw) if iw else 0)
        if alg!=Ftrue[d]:
            bad+=1; print("S NODE MISMATCH", [c.name for c in children], iw, d, alg, Ftrue[d])
print(f"S-node: {tested} (composition,d) cases, mismatches={bad}")
