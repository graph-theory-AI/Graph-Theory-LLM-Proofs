"""Small two-terminal components and composition operators."""
from pl import Graph, embeddings
from prof import profile

class Comp:
    """n vertices 0..n-1, poles s,t, edge list, weights on internal vertices."""
    def __init__(self, n, edges, s, t, w=None, name=""):
        self.n=n; self.edges=list(edges); self.s=s; self.t=t
        self.w=dict(w or {}); self.name=name
    def hat(self):
        """Hhat = H + rho ; returns (Graph, rho index, weight dict)."""
        g = Graph(self.n, self.edges + [(self.s, self.t)])
        return g, len(self.edges), self.w
    def brute_profile(self):
        g, rho, w = self.hat()
        return profile(g, rho, w)

def relabel(c, off, smap, tmap):
    """shift internal vertices by off, map poles to smap,tmap."""
    m={}
    k=off
    for v in range(c.n):
        if v==c.s: m[v]=smap
        elif v==c.t: m[v]=tmap
        else:
            m[v]=k; k+=1
    edges=[(m[u],m[v]) for u,v in c.edges]
    w={m[v]:x for v,x in c.w.items() if v not in (c.s,c.t)}
    return edges, w, k

def parallel(children):
    """P-node: all children between common poles 0 (=s) and 1 (=t)."""
    edges=[]; w={}; nxt=2
    for c in children:
        e2,w2,nxt = relabel(c, nxt, 0, 1)
        edges += e2; w.update(w2)
    return Comp(nxt, edges, 0, 1, w, "P")

def series(children, internal_w=None):
    """S-node: children in series, poles 0 and 1, junctions 2,3,..."""
    r=len(children)
    # junction vertices: we allocate them first
    junc=[0]+[2+i for i in range(r-1)]+[1]
    nxt=2+(r-1)
    edges=[]; w={}
    for i,c in enumerate(children):
        e2,w2,nxt = relabel(c, nxt, junc[i], junc[i+1])
        edges+=e2; w.update(w2)
    if internal_w:
        for i,x in enumerate(internal_w):
            w[2+i]=x
    return Comp(nxt, edges, 0, 1, w, "S")

# --- a library of small components
def edge_comp():             return Comp(2, [(0,1)], 0, 1, {}, "edge")
def path2(wm=0):             return Comp(3, [(0,2),(2,1)], 0, 1, {2:wm}, "path2")
def path3(w1=0,w2=0):        return Comp(4, [(0,2),(2,3),(3,1)], 0, 1, {2:w1,3:w2}, "path3")
def cyc_pair():              return Comp(4, [(0,2),(2,1),(0,3),(3,1)], 0, 1, {}, "theta2")
def k4me():
    # K4 minus edge st, poles s=0,t=1, other vertices 2,3
    return Comp(4, [(0,2),(0,3),(1,2),(1,3),(2,3)], 0, 1, {}, "K4-e")
def triangle_ear():
    # s-a-t plus a triangle hanging: s-a, a-t, a-b, b-c, c-a
    return Comp(5, [(0,2),(2,1),(2,3),(3,4),(4,2)], 0, 1, {}, "tri-ear")
def doubleedge():            return Comp(2, [(0,1),(0,1)], 0, 1, {}, "2edge")
