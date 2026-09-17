#!/usr/bin/env python3
"""Structured large-n check: families where the hypothesis imb(e)>0 holds and
the truncated-tail lemma might plausibly be stressed (stars, double stars,
antiregular/threshold graphs, complete split graphs, spiders, brooms, caterpillars,
random trees, random threshold graphs).  For each: verify M_G graphic (Erdos-Gallai)
and the lemma for every 1<=k<D with the worst S (top-k), reporting min slack."""
import sys, random, itertools
sys.path.insert(0, __file__.rsplit('/',1)[0])
from check_lemma import is_graphic

def check(name, n, edges):
    deg=[0]*n
    for u,v in edges: deg[u]+=1; deg[v]+=1
    a=sorted((abs(deg[u]-deg[v]) for u,v in edges), reverse=True)
    if not a or a[-1]==0: return None
    D=max(deg)
    sl=min((sum(min(k,x) for x in a[k:])-k*(D-k)) for k in range(1,D)) if D>=2 else None
    return (name, n, len(edges), D, is_graphic(a), sl)

rows=[]
# stars
for D in (5,20,100,500): rows.append(check(f"star K_1,{D}", D+1, [(0,i) for i in range(1,D+1)]))
# double stars: centres u,v adjacent with p and q leaves, p!=q
for p,q in ((3,4),(10,11),(50,77),(200,313)):
    n=p+q+2; E=[(0,1)]+[(0,2+i) for i in range(p)]+[(1,2+p+i) for i in range(q)]
    rows.append(check(f"double star {p},{q}", n, E))
# antiregular (maximally irregular) threshold graph on n vertices
def antiregular(n):
    # standard construction: vertex i adjacent to j iff i+j >= n  (0-indexed), no loops
    return [(i,j) for i in range(n) for j in range(i+1,n) if i+j>=n]
for n in (6,9,20,60,150): rows.append(check(f"antiregular n={n}", n, antiregular(n)))
# complete split graph K_a + empty_b  (clique a joined to independent b)
for a,b in ((2,5),(3,10),(7,40),(20,200)):
    n=a+b; E=[(i,j) for i in range(a) for j in range(i+1,a)]+[(i,a+j) for i in range(a) for j in range(b)]
    rows.append(check(f"split K_{a}+bar K_{b}", n, E))
# random trees & random threshold graphs, keep only those with all imbalances positive
rnd=random.Random(1)
kept=0; tested=0
worst=None
for trial in range(4000):
    n=rnd.randint(5,60)
    E=[(rnd.randint(0,i-1), i) for i in range(1,n)]     # random labelled tree
    tested+=1
    r=check("random tree", n, E)
    if r and r[5] is not None:
        kept+=1
        if not r[4]: print("NON-GRAPHIC random tree!", n, E)
        if worst is None or r[5]<worst[5]: worst=r
for trial in range(4000):
    n=rnd.randint(5,40); seq=[rnd.randint(0,1) for _ in range(n)]
    adj=set()
    # threshold graph build
    order=list(range(n))
    for i in range(1,n):
        if seq[i]:
            for j in order[:i]: adj.add((j,i))
    E=sorted(adj)
    if not E: continue
    r=check("random threshold", n, E)
    if r and r[5] is not None:
        kept+=1
        if not r[4]: print("NON-GRAPHIC random threshold!", n, E)
        if worst is None or r[5]<worst[5]: worst=r
for r in rows:
    if r: print(f"{r[0]:28s} n={r[1]:4d} m={r[2]:6d} D={r[3]:4d} graphic={r[4]} lemma_min_slack={r[5]}")
    
print(f"\nrandom families: {kept} hypothesis-satisfying instances checked, worst lemma slack = {worst[5] if worst else None} ({worst[0] if worst else '-'} n={worst[1] if worst else '-'})")
