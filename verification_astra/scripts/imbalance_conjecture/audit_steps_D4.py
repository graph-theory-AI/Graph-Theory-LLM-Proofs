#!/usr/bin/env python3
"""Independent re-audit of the writeup's proof of the truncated-tail lemma.

The writeup disposes of D<=3 by hand and then ASSUMES D>=4, 2<=k<D for the
chain (3)-(7).  So steps (2)-(7) are audited only in that regime; the
special cases D<=3 are audited separately by their own hand argument.

Checks, for every graph with all imbalances positive, every max-degree
vertex v, every 2<=k<D and EVERY S subset E with |S|=k:
   (2) r = b + t
   (3) LHS >= q-t+k*r-sum_{u in U}(d(u)-b)_+
   (4) sum_{u in U}(d(u)-b)_+ <= q + C(l,2) - (b-1)l
   (5) LHS >= k r - t - F_b(l)
   (6) F_b(l) <= (k-1) t          [only claimed for D>=4]
   (7) F_b(l) <= max(0, C(t+1,2)-C(b,2))
   (1) LHS >= k(D-k)              [the lemma itself, all 1<=k<D]
plus the D<=3 hand cases.
"""
import sys, itertools
from math import comb
sys.path.insert(0, __file__.rsplit('/',1)[0])
from check_lemma import g6_edges

fails = {i: [] for i in ('2','3','4','5','6','7','lemma','D3')}
ngraph = 0
skipped = 0
for line in sys.stdin:
    r0 = g6_edges(line)
    if r0 is None: continue
    n, edges = r0
    if not edges: continue
    deg=[0]*n
    for u,v in edges: deg[u]+=1; deg[v]+=1
    a={e: abs(deg[e[0]]-deg[e[1]]) for e in edges}
    if any(x==0 for x in a.values()): continue
    m=len(edges); D=max(deg)
    if D >= 2 and sum(comb(m,k) for k in range(1,D)) > 200000:
        skipped += 1; continue
    ngraph += 1
    for v in [i for i in range(n) if deg[i]==D]:
        Ev=[e for e in edges if v in e]
        q=m-D
        for k in range(1, D):
            for S in itertools.combinations(edges, k):
                Sset=set(S)
                lhs=sum(min(k,a[e]) for e in edges if e not in Sset)
                if lhs < k*(D-k):
                    fails['lemma'].append((line.strip(),v,k,S,lhs,k*(D-k)))
                # D<=3 hand cases
                if D<=3:
                    if D==3 and k==2 and lhs < 2:
                        fails['D3'].append((line.strip(),v,k,S,lhs))
                    continue
                if k < 2: continue   # k=1 handled by its own one-liner
                s=sum(1 for e in Ev if e in Sset); t=k-s
                U=[(e[0] if e[1]==v else e[1]) for e in Ev if e not in Sset]
                rr=len(U); b=D-k
                if rr != b+t: fails['2'].append((line.strip(),v,k,S,rr,b,t))
                dpl=sum(max(0,deg[u]-b) for u in U)
                if lhs < q-t+k*rr-dpl: fails['3'].append((line.strip(),v,k,S,lhs,q-t+k*rr-dpl))
                L=[u for u in U if deg[u]>b]; ell=len(L)
                if dpl > q+comb(ell,2)-(b-1)*ell: fails['4'].append((line.strip(),v,k,S,dpl))
                Fb = comb(ell,2)-(b-1)*ell
                if lhs < k*rr-t-Fb: fails['5'].append((line.strip(),v,k,S,lhs,k*rr-t-Fb))
                if Fb > (k-1)*t: fails['6'].append((line.strip(),v,k,S,Fb,(k-1)*t,b,t,ell,D))
                if Fb > max(0, comb(t+1,2)-comb(b,2)): fails['7'].append((line.strip(),v,k,S,Fb,b,t,ell))
print("graphs audited:", ngraph, " skipped (too many S):", skipped)
for key in ('2','3','4','5','6','7','lemma','D3'):
    print(f"  step ({key}) failures: {len(fails[key])}")
    for f in fails[key][:3]: print("     ", f)
