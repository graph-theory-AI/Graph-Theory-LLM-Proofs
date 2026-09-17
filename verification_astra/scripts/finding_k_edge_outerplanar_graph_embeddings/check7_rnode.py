"""Check 7: the R-node recurrence (12)-(13): substitute children into a
3-connected skeleton, compute C_Sigma(a,b) from the skeleton dual with child
lengths ell_i, and compare with the true brute-force profile."""
import itertools, random, heapq
from pl import Graph, embeddings
from comps import *
INF=float('inf')

def dijkstra(nf, adj, src):
    d=[INF]*nf; d[src]=0; pq=[(0,src)]
    while pq:
        dv,v=heapq.heappop(pq)
        if dv>d[v]: continue
        for u,wt in adj[v]:
            if dv+wt<d[u]:
                d[u]=dv+wt; heapq.heappush(pq,(d[u],u))
    return d

def skeleton_eval(skel, rho, cp, skelw, emb):
    """cp: dict edge index -> (ell, F).  Returns (ell(H), function C(a,b))."""
    A,B = emb.sides(rho)
    adj=[[] for _ in range(emb.nf)]
    for i in range(skel.m):
        if i==rho: continue
        x,y=emb.sides(i)
        L=cp[i][0]
        adj[x].append((y,L)); adj[y].append((x,L))
    dA=dijkstra(emb.nf,adj,A); dB=dijkstra(emb.nf,adj,B)
    ell=dA[B]
    s,t=skel.edges[rho]
    def C(a,b):
        delta=[min(a+dA[z], b+dB[z]) for z in range(emb.nf)]
        best=0
        for i in range(skel.m):
            if i==rho: continue
            x,y=emb.sides(i)
            L,F=cp[i]
            diff=abs(delta[x]-delta[y])
            assert diff<=L, ("Lipschitz violated", diff, L)
            best=max(best, min(delta[x],delta[y])+F[diff])
        for v in range(skel.n):
            if v in (s,t): continue
            if skelw.get(v,0)==0: continue
            best=max(best, skelw[v]+min(delta[f] for f in emb.faces_at_vertex(v)))
        return best
    return ell, C

def compose(skel, rho, children):
    """children: dict edge index -> Comp. Build the composed Comp."""
    s,t=skel.edges[rho]
    edges=[]; w={}; nxt=skel.n
    for i,(u,v) in enumerate(skel.edges):
        if i==rho: continue
        c=children[i]
        m={}; k=nxt
        for x in range(c.n):
            if x==c.s: m[x]=u
            elif x==c.t: m[x]=v
            else: m[x]=k; k+=1
        nxt=k
        edges += [(m[a],m[b]) for a,b in c.edges]
        for x,val in c.w.items():
            if x not in (c.s,c.t): w[m[x]]=val
    return Comp(nxt, edges, s, t, w, "R"), nxt

# skeletons: K4 and the 3-prism
K4=Graph(4,[(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)])
PRISM=Graph(6,[(0,1),(1,2),(2,0),(3,4),(4,5),(5,3),(0,3),(1,4),(2,5)])
lib=[edge_comp(), path2(0), path2(2), doubleedge(), path3(0,0)]

random.seed(29)
tested=0; bad=0; badell=0; badrefl=0
for trial in range(400):
    skel = K4 if random.random()<0.75 else PRISM
    rho = random.randrange(skel.m)
    children={}
    for i in range(skel.m):
        if i==rho: continue
        children[i]= lib[0] if random.random()<0.6 else random.choice(lib)
    skelw={v: random.choice([0,0,0,2]) for v in range(skel.n)}
    comp,_=compose(skel,rho,children)
    for v,val in skelw.items():
        if v not in (skel.edges[rho][0], skel.edges[rho][1]) and val: comp.w[v]=val
    g,r2,w=comp.hat()
    if sum(max(len(g.inc[v])-1,0) for v in range(g.n))>12: continue
    if g.n>8: continue
    try:
        Ltrue,Ftrue=comp.brute_profile()
    except Exception:
        continue
    cp={i:children[i].brute_profile() for i in children}
    skembs=[e for e in embeddings(skel)]
    vals={}
    ells=set()
    for emb in skembs:
        try:
            ell,C=skeleton_eval(skel,rho,cp,skelw,emb)
        except AssertionError as ex:
            print("LIPSCHITZ FAIL", ex); bad+=1; continue
        ells.add(ell)
        for d in range(ell+1):
            vals.setdefault(d,[]).append((C(0,d),C(d,0)))
    if len(ells)!=1 or list(ells)[0]!=Ltrue:
        badell+=1; print("R ELL MISMATCH", ells, Ltrue)
        continue
    for d in range(Ltrue+1):
        tested+=1
        # writeup's rule on ONE fixed embedding:
        v_writeup=min(vals[d][0])
        # min over all skeleton embeddings and both label orders:
        v_all=min(min(p) for p in vals[d])
        if v_writeup!=Ftrue[d]:
            bad+=1
            if bad<6: print("R NODE MISMATCH", skel.edges, rho, {i:children[i].name for i in children}, skelw, d, v_writeup, Ftrue[d])
        if v_all!=v_writeup: badrefl+=1
print(f"R-node: {tested} (composition,d) cases, mismatches={bad}, ell mismatches={badell}, reflection-rule discrepancies={badrefl}")
