#!/usr/bin/env python3
"""Audit the INTERNAL steps (3),(4),(5),(6) of the writeup's proof of the
truncated-tail lemma, on real graphs, for EVERY choice of S (not just top-k)
and every max-degree vertex v.  A failure here is an error in the PROOF even
if the lemma itself survives."""
import sys, itertools
from math import comb
sys.path.insert(0, __file__.rsplit('/',1)[0])
from check_lemma import g6_edges

fails = {i: [] for i in ('3','4','5','6','lemma')}
ngraph = 0
for line in sys.stdin:
    r = g6_edges(line)
    if r is None: continue
    n, edges = r
    if not edges: continue
    deg=[0]*n
    for u,v in edges: deg[u]+=1; deg[v]+=1
    a={e: abs(deg[e[0]]-deg[e[1]]) for e in edges}
    if any(x==0 for x in a.values()): continue
    m=len(edges); D=max(deg)
    if comb(m, min(m//2, D-1) if D>1 else 1) > 60000: continue   # keep it feasible
    ngraph += 1
    for v in [i for i in range(n) if deg[i]==D]:
        Ev=[e for e in edges if v in e]
        q=m-D
        for k in range(1, D):
            for S in itertools.combinations(edges, k):
                Sset=set(S)
                lhs=sum(min(k,a[e]) for e in edges if e not in Sset)
                s=sum(1 for e in Ev if e in Sset); t=k-s
                U=[(e[0] if e[1]==v else e[1]) for e in Ev if e not in Sset]
                rr=len(U); b=D-k
                assert rr==b+t, ("(2) r=b+t failed", rr, b, t)
                def_=sum(max(0,deg[u]-b) for u in U)
                # (3)
                rhs3 = q-t+k*rr-def_
                if lhs < rhs3: fails['3'].append((line.strip(),v,k,S,lhs,rhs3))
                # (4)
                L=[u for u in U if deg[u]>b]; ell=len(L)
                rhs4 = q+comb(ell,2)-(b-1)*ell
                if def_ > rhs4: fails['4'].append((line.strip(),v,k,S,def_,rhs4))
                # (5)
                Fb = comb(ell,2)-(b-1)*ell
                rhs5 = k*rr-t-Fb
                if lhs < rhs5: fails['5'].append((line.strip(),v,k,S,lhs,rhs5))
                # (6)
                if Fb > (k-1)*t: fails['6'].append((line.strip(),v,k,S,Fb,(k-1)*t,b,t,ell))
                # lemma
                if lhs < k*(D-k): fails['lemma'].append((line.strip(),v,k,S,lhs,k*(D-k)))
print("graphs audited (all S, all max-deg v):", ngraph)
for key in ('3','4','5','6','lemma'):
    print(f"  step ({key}) failures: {len(fails[key])}")
    for f in fails[key][:3]: print("     ", f)
