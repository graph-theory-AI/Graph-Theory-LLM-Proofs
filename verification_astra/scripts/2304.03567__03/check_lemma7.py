"""Lemma 7: OPT(B_h,R_h) <= 3N, N=2^h.
(a) exhaustive over all acyclic orientations (h<=3)
(b) DP upper bound using the writeup's own relaxation M_v <= min(A_x,B_y) -- this is an
    upper bound on OPT(B_h) and is checked against 3N
(c) local search lower bound for larger h
"""
import itertools, random, sys
from collections import defaultdict
from construction import build_B, realized

def requests_B(h):
    leaves=[''.join(s) for s in itertools.product('01',repeat=h)]
    R=[]
    for u in leaves:
        for i in range(h):
            v=u[:i]+('1' if u[i]=='0' else '0')+u[i+1:]
            if u<v: R.append((u,v))
    return leaves,R

# ---------- (a) exhaustive over acyclic orientations ----------
def exhaustive(h):
    V,E,M=build_B(h)
    leaves,R=requests_B(h)
    internal=[w for w in V if len(w)<h]
    best=0
    # per triangle: one of 6 linear orders of (w, w0, w1)
    tri=[(w,w+'0',w+'1') for w in internal]
    for choice in itertools.product(range(6),repeat=len(tri)):
        arcs=[]
        for (t,c) in zip(tri,choice):
            order=list(itertools.permutations(t))[c]
            for i in range(len(order)):
                for j in range(i+1,len(order)):
                    arcs.append((order[i],order[j]))
        # global topological order: arcs form a DAG on cactus; get one by toposort
        ad=defaultdict(list); indeg=defaultdict(int)
        for u,v in arcs: ad[u].append(v); indeg[v]+=1
        S=[v for v in V if indeg[v]==0]; topo=[]
        while S:
            u=S.pop(); topo.append(u)
            for v in ad[u]:
                indeg[v]-=1
                if indeg[v]==0: S.append(v)
        if len(topo)!=len(V): continue   # cyclic (cannot happen for triangle-acyclic cactus)
        best=max(best,realized(topo,arcs,leaves,R))
    return best

# ---------- (b) DP upper bound ----------
def dp_upper(h):
    """state: (A,B) -> best value for a subtree. leaves: (1,1)->0."""
    level={(1,1):0}
    for d in range(1,h+1):
        nxt={}
        items=list(level.items())
        for (Ax,Bx),vx in items:
            for (Ay,By),vy in items:
                base=vx+vy
                # 6 orders of (v, c1, c2); by symmetry treat children as (x,y) unordered:
                for (first,second) in ((0,1),(1,0)):
                    (A1,B1),(A2,B2)=((Ax,Bx),(Ay,By)) if first==0 else ((Ay,By),(Ax,Bx))
                    # child1 precedes child2 in the enumeration
                    M_bound=min(A1,B2)
                    for pos in range(3):   # v before both / between / after both
                        if pos==0:  Av,Bv=0,B1+B2
                        elif pos==1: Av,Bv=A1,B2
                        else: Av,Bv=A1+A2,0
                        val=base+M_bound
                        k=(Av,Bv)
                        if nxt.get(k,-1)<val: nxt[k]=val
        # Pareto prune: (A,B,val) dominated if some other has A'>=A,B'>=B,val'>=val
        st=sorted(nxt.items(), key=lambda kv:(-kv[1],-kv[0][0],-kv[0][1]))
        keep={}
        for (A,B),v in st:
            dom=False
            for (A2,B2),v2 in keep.items():
                if A2>=A and B2>=B and v2>=v: dom=True; break
            if not dom: keep[(A,B)]=v
        level=keep
    return max(level.values())

# ---------- (c) local search lower bound ----------
def local_search(h,iters=40000,seed=0):
    V,E,M=build_B(h); leaves,R=requests_B(h)
    rng=random.Random(seed)
    arcs_all=E
    order=list(V); rng.shuffle(order)
    def ev(o): 
        arcs=[]
        pos={v:i for i,v in enumerate(o)}
        for u,v in arcs_all:
            arcs.append((u,v) if pos[u]<pos[v] else (v,u))
        return realized(o,arcs,leaves,R)
    cur=ev(order); best=cur
    for it in range(iters):
        i,j=rng.randrange(len(order)),rng.randrange(len(order))
        if i==j: continue
        order[i],order[j]=order[j],order[i]
        val=ev(order)
        if val>=cur: cur=val; best=max(best,val)
        else: order[i],order[j]=order[j],order[i]
    return best

if __name__=='__main__':
    print(" h   N   |R|=h2^(h-1)   3N   exhaustiveOPT   DPupper   localsearchLB")
    for h in range(1,9):
        N=2**h; Rn=h*2**(h-1)
        ex = exhaustive(h) if h<=3 else None
        dp = dp_upper(h)
        ls = local_search(h, iters=(4000 if h<=5 else 1500), seed=h) if h<=6 else None
        print(f"{h:2d} {N:4d} {Rn:8d} {3*N:8d} {str(ex):>12}  {dp:8d} {str(ls):>12}   "
              f"{'OK' if dp<=3*N else '*** VIOLATION ***'}")
