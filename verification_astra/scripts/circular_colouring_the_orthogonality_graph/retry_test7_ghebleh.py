"""Cross-check against Ghebleh (2007 SFU PhD thesis, section 4.4) — the real prior art.
G_n = subgraph of O induced by primitive integer vectors of sup-norm <= n.  The thesis
reports |V(G_3)|=145, |E(G_3)|=546, chi_c(G_1)=7/2, chi_c(H_2)=11/3 for a 44-vertex
H_2 subset G_2, and a (27,7)-colouring of G_3.  If the retry writeup theorem were too
strong it would collide with G_3 -> K_{27/7}; it must not, because G_3 is FINITE.
One-hot boolean encoding + z3 (much faster than the Int/mod encoding).
"""
import itertools, math, networkx as nx, z3, time
def canon(v):
    g = math.gcd(math.gcd(abs(v[0]), abs(v[1])), abs(v[2]))
    v = (v[0]//g, v[1]//g, v[2]//g)
    return v if (v[2], v[1], v[0]) > (0, 0, 0) else (-v[0], -v[1], -v[2])
def G(n):
    V = sorted({canon(v) for v in itertools.product(range(-n,n+1),repeat=3) if v!=(0,0,0)})
    g = nx.Graph(); g.add_nodes_from(V)
    for x,y in itertools.combinations(V,2):
        if x[0]*y[0]+x[1]*y[1]+x[2]*y[2]==0: g.add_edge(x,y)
    return g
def Kpq(p,q):
    H=nx.Graph(); H.add_nodes_from(range(p))
    for a in range(p):
        for b in range(a+1,p):
            d=(b-a)%p
            if q<=d<=p-q: H.add_edge(a,b)
    return H
def hom(Gg,H,tmo=300000):
    Hv=list(H); Hadj={u:set(H.neighbors(u)) for u in Hv}
    s=z3.Solver(); s.set("timeout",tmo)
    b={v:{c:z3.Bool("b_%d_%d"%(i,c)) for c in Hv} for i,v in enumerate(Gg)}
    for v in Gg:
        s.add(z3.Or([b[v][c] for c in Hv]))
        for c1,c2 in itertools.combinations(Hv,2): s.add(z3.Or(z3.Not(b[v][c1]),z3.Not(b[v][c2])))
    for u,v in Gg.edges():
        for c in Hv:
            for cc in Hv:
                if cc not in Hadj[c]: s.add(z3.Or(z3.Not(b[u][c]),z3.Not(b[v][cc])))
    t=time.time(); r=s.check(); el=time.time()-t
    col=None
    if r==z3.sat:
        m=s.model(); col={v:[c for c in Hv if z3.is_true(m.eval(b[v][c],True))][0] for v in Gg}
    return r,col,el
print("calibration (circular clique to circular clique):",flush=True)
for src,dst,exp in [((7,2),(7,2),"sat"),((11,3),(7,2),"unsat"),((7,2),(11,3),"sat"),
                    ((4,1),(15,4),"unsat"),((11,3),(27,7),"sat"),((27,7),(11,3),"unsat"),
                    ((4,1),(27,7),"unsat"),((15,4),(27,7),"sat")]:
    r,_,el=hom(Kpq(*src),Kpq(*dst))
    print("  K_%d/%d -> K_%d/%d: %s (expected %s) [%.1fs]%s"%(src[0],src[1],dst[0],dst[1],r,exp,el,
          "  OK" if str(r)==exp else "  *** MISMATCH ***"),flush=True)
gs={n:G(n) for n in (1,2,3)}
for n in (1,2,3): print("G_%d: %d vertices, %d edges"%(n,gs[n].number_of_nodes(),gs[n].number_of_edges()),flush=True)
for n in (1,2,3):
    for (p,q) in [(7,2),(11,3),(15,4),(27,7),(4,1)]:
        r,col,el=hom(gs[n],Kpq(p,q))
        extra=""
        if str(r)=="sat":
            bad=sum(1 for u,v in gs[n].edges() if not (q<=(col[v]-col[u])%p<=p-q))
            extra="  (colouring independently verified, %d bad edges)"%bad
        print("  G_%d -> K_{%d/%d} = %.4f: %s [%.1fs]%s"%(n,p,q,p/q,r,el,extra),flush=True)
