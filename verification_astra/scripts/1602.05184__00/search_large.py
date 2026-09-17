"""Hill-climbing / annealing search for a 2-connected graph on n >= 12 vertices,
outside the three exceptional families, with eta(G) < 2n."""
import random, sys
from itertools import combinations
from collections import deque

def eta_and_ok(n, A):
    # A: list of sets. BFS distances
    D=[]
    for s in range(n):
        d=[-1]*n; d[s]=0; q=deque([s])
        while q:
            v=q.popleft()
            for u in A[v]:
                if d[u]<0: d[u]=d[v]+1; q.append(u)
        if any(x<0 for x in d): return None
        D.append(d)
    W=sum(D[i][j] for i in range(n) for j in range(i+1,n))
    Sz=0
    for u in range(n):
        for v in A[u]:
            if v<u: continue
            nu=nv=0
            for w in range(n):
                if D[w][u]<D[w][v]: nu+=1
                elif D[w][v]<D[w][u]: nv+=1
            Sz+=nu*nv
    return Sz-W

def two_connected(n,A):
    def conn(skip):
        st=[x for x in range(n) if x!=skip][:1]
        if not st: return True
        seen=set(st)
        while st:
            v=st.pop()
            for u in A[v]:
                if u!=skip and u not in seen: seen.add(u); st.append(u)
        return len(seen)==n-(1 if skip is not None else 0)
    if not conn(None): return False
    return all(conn(v) for v in range(n))

def exceptional(n,A):
    m=sum(len(s) for s in A)//2; full=n*(n-1)//2
    if m>=full-1: return True
    for v in range(n):
        if len(A[v])==2:
            rest=[x for x in range(n) if x!=v]
            if all(y in A[x] for x,y in combinations(rest,2)): return True
    return False

def random_2conn(n, p=0.4):
    while True:
        A=[set() for _ in range(n)]
        for i in range(n):
            j=(i+1)%n; A[i].add(j); A[j].add(i)      # hamiltonian cycle base
        for i,j in combinations(range(n),2):
            if j not in A[i] and random.random()<p:
                A[i].add(j); A[j].add(i)
        if two_connected(n,A): return A

random.seed(20260917)
for n in [12,13,14,16,20]:
    best=None; bestA=None
    for restart in range(12):
        A=random_2conn(n, random.choice([0.1,0.2,0.35,0.6]))
        cur=eta_and_ok(n,A)
        T=6.0
        for it in range(4000):
            T=max(0.02, T*0.9988)
            i,j=random.sample(range(n),2)
            if j in A[i]: A[i].discard(j); A[j].discard(i); added=False
            else: A[i].add(j); A[j].add(i); added=True
            ok = two_connected(n,A)
            new = eta_and_ok(n,A) if ok else None
            accept = ok and (new<=cur or random.random()<pow(2.718,-(new-cur)/T))
            if accept:
                cur=new
                if not exceptional(n,A) and (best is None or cur<best):
                    best=cur; bestA=[set(s) for s in A]
            else:
                if added: A[i].discard(j); A[j].discard(i)
                else: A[i].add(j); A[j].add(i)
    print(f"n={n}: best non-exceptional eta found = {best}   (2n = {2*n}, 3n-10 = {3*n-10})")
    sys.stdout.flush()
