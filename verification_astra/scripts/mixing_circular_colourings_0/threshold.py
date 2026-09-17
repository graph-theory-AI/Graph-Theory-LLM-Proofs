"""Use the (independently validated) Q-graph algorithm to compute mixing status
over many ratios for larger graphs, then check the Theorem's prediction:
the bad set is a union of intervals with endpoints in E_{n+1}, and
sup B_G  lies in E_{n+1}  (reduced numerator <= n+1)."""
from fractions import Fraction
import sys
sys.path.insert(0, '/home/enatale/repos/lelarge/graph-theory-auto/verification_astra/scripts/mixing_circular_colourings_0')
from endtoend import Q_graph, E

G = {
 "C6":(6,[(0,1),(1,2),(2,3),(3,4),(4,5),(5,0)]),
 "C7":(7,[(0,1),(1,2),(2,3),(3,4),(4,5),(5,6),(6,0)]),
 "prism":(6,[(0,1),(1,2),(2,0),(3,4),(4,5),(5,3),(0,3),(1,4),(2,5)]),
 "K33":(6,[(0,3),(0,4),(0,5),(1,3),(1,4),(1,5),(2,3),(2,4),(2,5)]),
 "K5":(5,[(i,j) for i in range(5) for j in range(i+1,5)]),
 "W5":(6,[(0,1),(1,2),(2,3),(3,4),(4,0),(5,0),(5,1),(5,2),(5,3),(5,4)]),
}
KMAX = int(sys.argv[1]) if len(sys.argv)>1 else 16
for name in (sys.argv[2:] or list(G)):
    n, edges = G[name]
    En, En1 = E(n), E(n+1)
    res = {}
    for k in range(2, KMAX+1):
        for q in range(1, k//2+1):
            res.setdefault(Fraction(k,q), {})[(k,q)] = Q_graph(n, edges, k, q)
    bad = sorted(r for r,d in res.items() if not all(d.values()))
    good = sorted(r for r,d in res.items() if all(d.values()))
    repdep = [str(r) for r,d in res.items() if len(set(d.values()))>1]
    pts = sorted(x for x in En1 if x>2)
    viol = []
    for r1 in res:
        for r2 in res:
            if r1<=2 or r2<=r1: continue
            if any(r1<=p<=r2 for p in pts): continue
            if all(res[r1].values()) != all(res[r2].values()): viol.append((str(r1),str(r2)))
    mb = max(bad) if bad else None
    ga = [r for r in good if mb is not None and r>mb]
    mg = min(ga) if ga else None
    bracket = [str(p) for p in sorted(En1) if mb is not None and mb<=p<=(mg if mg else 10**9)]
    print(f"{name}: n={n} E_(n+1)={sorted(str(x) for x in En1)}")
    print(f"   max bad ratio tested = {mb}; min good ratio above = {mg}")
    print(f"   E_(n+1) points in [maxbad, mingood] (threshold must be one): {bracket}")
    print(f"   representation-dependent ratios: {repdep}")
    print(f"   local-constancy (Prop 4) violations: {viol[:5]} count={len(viol)}")
    print(f"   any bad ratio >= n+1 (would break Sec.5): {[str(r) for r in bad if r>=n+1]}")
