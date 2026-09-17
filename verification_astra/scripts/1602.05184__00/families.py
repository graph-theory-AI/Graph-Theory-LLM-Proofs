"""Scan structured families of 2-connected graphs for eta(G) < 2n, n >= 12."""
import sys
from itertools import combinations
from collections import deque

def eta(n, adj):
    D=[]
    for s in range(n):
        d=[-1]*n; d[s]=0; q=deque([s])
        while q:
            v=q.popleft()
            for u in adj[v]:
                if d[u]<0: d[u]=d[v]+1; q.append(u)
        if any(x<0 for x in d): return None
        D.append(d)
    W=sum(D[i][j] for i in range(n) for j in range(i+1,n))
    Sz=0
    for u in range(n):
        for v in adj[u]:
            if v<u: continue
            nu=nv=0
            for w in range(n):
                if D[w][u]<D[w][v]: nu+=1
                elif D[w][v]<D[w][u]: nv+=1
            Sz+=nu*nv
    return Sz-W

def two_conn(n,adj):
    def conn(skip):
        vs=[x for x in range(n) if x!=skip]
        if not vs: return True
        seen={vs[0]}; st=[vs[0]]
        while st:
            v=st.pop()
            for u in adj[v]:
                if u!=skip and u not in seen: seen.add(u); st.append(u)
        return len(seen)==len(vs)
    return conn(None) and all(conn(v) for v in range(n))

def exceptional(n,adj):
    m=sum(len(s) for s in adj)//2; full=n*(n-1)//2
    if m>=full-1: return True
    for v in range(n):
        if len(adj[v])==2:
            rest=[x for x in range(n) if x!=v]
            if all(y in adj[x] for x,y in combinations(rest,2)): return True
    return False

def mk(n, edges):
    adj=[set() for _ in range(n)]
    for i,j in edges:
        adj[i].add(j); adj[j].add(i)
    return adj

def clique(vs):
    return [(i,j) for i,j in combinations(vs,2)]

def report(name,n,adj,out):
    if not two_conn(n,adj): return
    if exceptional(n,adj): return
    e=eta(n,adj)
    out.append((e-2*n, e, n, name))

def main():
    out=[]
    for n in range(12, 31):
        # F1: clique K_{n-k} + path of k vertices attached at two distinct clique vertices
        for k in range(2, min(n-3, 9)):
            c=n-k
            vs=list(range(c)); path=list(range(c,n))
            E=clique(vs)+[(path[i],path[i+1]) for i in range(k-1)]+[(0,path[0]),(1,path[-1])]
            report(f"clique{c}+path{k}(two ends)",n,mk(n,E),out)
        # F2: clique K_{n-2} + x,y adjacent, x~S_x, y~S_y of clique (sizes s,t, overlap o)
        c=n-2; x,y=c,c+1
        for s in range(1, min(c,5)+1):
            for t in range(1, min(c,5)+1):
                for o in range(0, min(s,t)+1):
                    if s+t-o>c: continue
                    Sx=set(range(s)); Sy=set(range(s-o, s-o+t))
                    if max(Sy)>=c: continue
                    E=clique(range(c))+[(x,y)]+[(x,v) for v in Sx]+[(y,v) for v in Sy]
                    report(f"clique{c}+edge xy,|Sx|={s},|Sy|={t},ov={o}",n,mk(n,E),out)
        # F3: clique K_{n-2} + x,y nonadjacent, x~Sx, y~Sy
        for s in range(1, min(c,5)+1):
            for t in range(1, min(c,5)+1):
                for o in range(0, min(s,t)+1):
                    if s+t-o>c: continue
                    Sx=set(range(s)); Sy=set(range(s-o, s-o+t))
                    if max(Sy)>=c: continue
                    E=clique(range(c))+[(x,v) for v in Sx]+[(y,v) for v in Sy]
                    report(f"clique{c}+x,y nonadj,|Sx|={s},|Sy|={t},ov={o}",n,mk(n,E),out)
        # F4: two cliques of sizes a,b joined by j edges (co-bipartite-ish)
        for a in range(2, n//2+1):
            b=n-a
            A=list(range(a)); B=list(range(a,n))
            base=clique(A)+clique(B)
            for j,extra in [(2,[(A[0],B[0]),(A[min(1,a-1)],B[1])]),
                            (2,[(A[0],B[0]),(A[0],B[1])] if a>=1 else []),
                            (3,[(A[0],B[0]),(A[min(1,a-1)],B[1]),(A[0],B[2])] if b>=3 else []),
                            (4,[(A[0],B[0]),(A[min(1,a-1)],B[1]),(A[0],B[2]),(A[min(1,a-1)],B[3])] if b>=4 else [])]:
                if not extra: continue
                report(f"K{a}+K{b}+{j}cross{extra}",n,mk(n,base+extra),out)
        # F5: clique K_{n-3} + triangle/path of 3 attached
        c=n-3
        if c>=3:
            vs=list(range(c)); z=[c,c+1,c+2]
            E=clique(vs)+[(z[0],z[1]),(z[1],z[2]),(z[0],z[2]),(0,z[0]),(1,z[1])]
            report(f"clique{c}+triangle 2 attach",n,mk(n,E),out)
        # F6: complete multipartite
        for parts in [[2]*(n//2), [3]*(n//3), [1,1]+[n-2], [n-2,2],[n-3,3],[2,2,n-4],[1,n-1]]:
            if sum(parts)!=n: continue
            lab=[]; 
            for i,p in enumerate(parts): lab += [i]*p
            E=[(i,j) for i,j in combinations(range(n),2) if lab[i]!=lab[j]]
            report(f"completemultipartite{parts}",n,mk(n,E),out)
        # F7: cycle powers C_n^k
        for k in range(2, 6):
            E=[(i,(i+d)%n) for i in range(n) for d in range(1,k+1)]
            E=[(min(a,b),max(a,b)) for a,b in E if a!=b]
            report(f"C{n}^{k}",n,mk(n,set(E)),out)
        # F8: clique with one edge subdivided repeatedly / clique + 2 paths between p,q
        for k1 in range(1,4):
            for k2 in range(1,4):
                c=n-k1-k2
                if c<3: continue
                vs=list(range(c)); P1=list(range(c,c+k1)); P2=list(range(c+k1,n))
                E=clique(vs)
                chain=[0]+P1+[1]; E+=[(chain[i],chain[i+1]) for i in range(len(chain)-1)]
                chain=[0]+P2+[1]; E+=[(chain[i],chain[i+1]) for i in range(len(chain)-1)]
                report(f"clique{c}+2paths({k1},{k2}) between same pair",n,mk(n,set(E)),out)
    out.sort()
    print("### lowest eta-2n over all families scanned (n=12..30):")
    for gap,e,n,name in out[:30]:
        print(f"  eta-2n={gap:4d}  eta={e:4d}  n={n:3d}  {name}")
    below=[r for r in out if r[0]<0]
    print("COUNTEREXAMPLES (eta<2n):", len(below))
    for r in below[:20]: print("   ",r)

main()
