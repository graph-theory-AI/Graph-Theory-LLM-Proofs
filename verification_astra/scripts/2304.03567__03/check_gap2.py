"""Stronger end-to-end test of eq. (21):  NO-instance => OPT(F_h,R_h) <= 3*2^h.

Instead of annealing over permutations of V(F_h) (hopeless at |V|~1000), we search in
the natural space: independently choose, for every core copy, one acyclic subgraph of K
(one maximal representative per achievable port-relation -- 24 of them for the fixed NO
gadget), and for every base copy F_0 one of the 4 maximal orientations. Global
acyclicity is then checked, and the realized request count computed. Hill-climbing with
random restarts over this space.
"""
import itertools, random, sys
from collections import defaultdict
from construction import *
from check_lemmas_2_3 import port_reach, acyclic, PORTS

def core_options(G):
    """maximal acyclic subgraphs of K, one per achievable port relation"""
    arcs,inner=core_arcs(G,'0','a','b','l','r'); verts=PORTS+inner
    best={}
    for mask in range(1<<len(arcs)):
        sub=[arcs[i] for i in range(len(arcs)) if (mask>>i)&1]
        if not acyclic(sub,verts): continue
        rel=port_reach(sub,verts)
        if rel not in best or len(sub)>len(best[rel][0]):
            best[rel]=(sub,mask)
    # keep the arc index sets
    return [m for (_,m) in best.values()], arcs

def build_options(G,h):
    """returns V, marked, requests, and a list of 'slots'; each slot is a list of
    candidate arc-sets (in terms of the *identified* vertex names)."""
    dsu=DSU(); verts=set(); marked={}; slots=[]
    def A_(w): return ('A',w)
    def B_(w): return ('B',w)
    core_masks, core_arclist = core_options(G)
    def rec(w,d):
        verts.add(A_(w)); verts.add(B_(w))
        if d==0:
            z=('Z',w); verts.add(z); marked[w]=z
            opts=[]
            for d1 in (0,1):
                for d2 in (0,1):
                    e1=(A_(w),z) if d1 else (z,A_(w))
                    e2=(z,B_(w)) if d2 else (B_(w),z)
                    opts.append([e1,e2])
            slots.append(opts)
        else:
            rec(w+'0',d-1); rec(w+'1',d-1)
            dsu.union(B_(w+'0'),A_(w+'1'))
            ell=A_(w+'0'); r=B_(w+'1')
            ca,cv=core_arcs(G,w,A_(w),B_(w),ell,r)
            verts.update(cv)
            sub={'a':A_(w),'b':B_(w),'l':ell,'r':r}
            # map the abstract core arc list onto this copy, in the SAME order
            ab,_=core_arcs(G,w,'a','b','l','r')
            def tr(x): return sub[x] if x in sub else x
            opts=[]
            for m in core_masks:
                opts.append([(tr(u),tr(v)) for i,(u,v) in enumerate(ab) if (m>>i)&1])
            slots.append(opts)
    rec('',h)
    f=dsu.find
    V={f(v) for v in verts}
    slots=[[ [(f(u),f(v)) for u,v in o] for o in opts] for opts in slots]
    M={w:f(z) for w,z in marked.items()}
    return V,M,slots

def evaluate(V,M,slots,choice,R,ml):
    arcs=[]
    for s,c in zip(slots,choice): arcs.extend(s[c])
    # global acyclicity + reachability by DFS-based topological sort
    out=defaultdict(list)
    for u,v in arcs: out[u].append(v)
    color={}; topo=[]
    for s in V:
        if color.get(s,0): continue
        st=[(s,iter(out.get(s,())))]; color[s]=1
        while st:
            u,it=st[-1]
            adv=False
            for v in it:
                c=color.get(v,0)
                if c==1: return None       # cycle
                if c==0:
                    color[v]=1; st.append((v,iter(out.get(v,())))); adv=True; break
            if not adv:
                color[u]=2; topo.append(u); st.pop()
    idx={v:i for i,v in enumerate(ml)}
    bits={}
    for v in topo:      # topo is reverse topological order (post-order)
        b=1<<idx[v] if v in idx else 0
        for w in out.get(v,()): b|=bits[w]
        bits[v]=b
    c=0
    for x,y in R:
        if (bits[x]>>idx[y])&1 or (bits[y]>>idx[x])&1: c+=1
    return c

def search(G,h,restarts,sweeps,seed=0):
    V,M,slots=build_options(G,h)
    R=hypercube_requests(M,h); ml=sorted(M.values())
    rng=random.Random(seed); best=0; bestchoice=None
    for rs in range(restarts):
        ch=[rng.randrange(len(s)) for s in slots]
        while evaluate(V,M,slots,ch,R,ml) is None:
            ch=[rng.randrange(len(s)) for s in slots]
        cur=evaluate(V,M,slots,ch,R,ml)
        for sw in range(sweeps):
            improved=False
            order=list(range(len(slots))); rng.shuffle(order)
            for i in order:
                old=ch[i]; bl=cur; bv=old
                for c in range(len(slots[i])):
                    if c==old: continue
                    ch[i]=c
                    v=evaluate(V,M,slots,ch,R,ml)
                    if v is not None and v>bl: bl=v; bv=c
                ch[i]=bv
                if bl>cur: cur=bl; improved=True
            if not improved: break
        if cur>best: best=cur; bestchoice=list(ch)
    return best,len(V),len(R)

if __name__=='__main__':
    OPT_B={1:1,2:4,3:10}; UB_B={4:24,5:52,6:114,7:244,8:516}
    for h,rst,sw in [(2,40,6),(3,25,6),(4,10,5),(5,4,4)]:
        best,nV,nR=search(G_NO,h,rst,sw,seed=h)
        ref=OPT_B.get(h) or UB_B[h]; N=2**h
        print(f"h={h}: |V(F_h)|={nV} |R_h|={nR}  best found on NO-instance = {best}"
              f"   [OPT/UB(B_h)={ref}, 3*2^h={3*N}]  "
              f"{'OK' if best<=ref and best<=3*N else '*** EXCEEDS BOUND ***'}")
        sys.stdout.flush()
