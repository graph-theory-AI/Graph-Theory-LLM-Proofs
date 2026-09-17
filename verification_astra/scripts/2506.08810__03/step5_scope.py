"""Step 5: how special is T*?  For every tournament T on 4..6 vertices, test the two
ingredients of the writeup's disproof:
  (A) every 6-vertex configuration [x->y, p in P(x,y), z1,z2,z3 in Z(x,y)] contains T
      (this is Lemma 2's engine; it forces J(S) to have max degree <= 2 for T-free S)
  (B) T has two ARC-disjoint directed triangles (this is Case 2's engine)
If (A) and (B) both hold and T is nontransitive, the identical argument disproves
Conjecture 24 for T.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tstar import *
from itertools import combinations, permutations, product

def canon(a):
    n=len(a); best=None
    for p in permutations(range(n)):
        code=0
        for b,(i,j) in enumerate(combinations(range(n),2)):
            if a[p[i]][p[j]]: code |= 1<<b
        if best is None or code<best: best=code
    return best

def decode(code, n):
    a=[[False]*n for _ in range(n)]
    for b,(i,j) in enumerate(combinations(range(n),2)):
        if code>>b & 1: a[i][j]=True
        else: a[j][i]=True
    return a

def contains(a, T):
    n=len(a); k=len(T)
    for S in combinations(range(n),k):
        if iso(induced(a,S), T): return True
    return False

def configs6():
    out=[]
    for pz in product([0,1],repeat=3):
        for zz in product([0,1],repeat=3):
            a=[[False]*6 for _ in range(6)]
            def arc(u,v): a[u][v]=True
            arc(0,1); arc(0,2); arc(2,1)
            for z in (3,4,5): arc(1,z); arc(z,0)
            for i,z in enumerate((3,4,5)):
                if pz[i]: arc(2,z)
                else: arc(z,2)
            for i,(u,v) in enumerate([(3,4),(3,5),(4,5)]):
                if zz[i]: arc(u,v)
                else: arc(v,u)
            out.append(a)
    return out
C6 = configs6()

def arc_disjoint_triangles(T):
    def arcset(t):
        x,y,z=t; return frozenset([(x,y),(y,z),(z,x)])
    tris={arcset(t) for t in directed_triangles(T)}
    for s1,s2 in combinations(tris,2):
        if not (s1&s2): return True
    return False

adjT,_ = tstar()
ct = canon(adjT)
for n in (4,5,6):
    seen={}
    for code in range(1<<(n*(n-1)//2)):
        a=decode(code,n)
        c=canon(a)
        if c not in seen: seen[c]=a
    print(f"n={n}: {len(seen)} tournaments up to isomorphism")
    winners=[]
    for c,T in seen.items():
        if is_transitive(T): continue
        if not arc_disjoint_triangles(T): continue
        if all(contains(a,T) for a in C6):
            winners.append((c,T))
    for c,T in winners:
        tag = " <-- T* (the writeup's counterexample)" if (n==5 and c==ct) else ""
        print(f"    DISPROVES Conj.24 by the same argument: canon={c}  outdegrees={sorted(sum(r) for r in T)}{tag}")
    if not winners: print("    none")
