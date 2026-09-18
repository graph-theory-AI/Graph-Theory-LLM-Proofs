"""Brute-force check of Lemma 2 (crossing closure) and Lemma 3 (exact port-reachability
representation by an oriented sub-forest of Q or Q/xy), for the core K built from
several NORMALIZED NO-instances of directed two-linkage."""
import itertools, random, sys
from collections import defaultdict
from construction import (G_NO, core_arcs, adj_of, reach, two_linkage_answer,
                          normalized_ok)

PORTS=['a','b','l','r']

def port_reach(arcs, verts):
    ad=adj_of(arcs)
    rel=set()
    for p in PORTS:
        for q in reach(ad,p):
            if q in PORTS and q!=p: rel.add((p,q))
    return frozenset(rel)

def acyclic(arcs, verts):
    ad=adj_of(arcs); color={}
    def dfs(u):
        color[u]=1
        for v in ad.get(u,()):
            if color.get(v,0)==1: return False
            if color.get(v,0)==0 and not dfs(v): return False
        color[u]=2; return True
    for v in verts:
        if color.get(v,0)==0 and not dfs(v): return False
    return True

# ---- representable relations from Q and Q/xy ----
def representable_set():
    reps=set()
    # Q: vertices a,b,l,r,x,y ; edges ax,bx,xy,yl,yr
    Qedges=[('a','x'),('b','x'),('x','y'),('y','l'),('y','r')]
    for st in itertools.product([0,1,2],repeat=len(Qedges)):
        arcs=[]
        for (u,v),s in zip(Qedges,st):
            if s==1: arcs.append((u,v))
            elif s==2: arcs.append((v,u))
        reps.add(port_reach(arcs,['a','b','l','r','x','y']))
    # Q/xy: star with centre c, leaves a,b,l,r
    Sedges=[('a','c'),('b','c'),('c','l'),('c','r')]
    for st in itertools.product([0,1,2],repeat=len(Sedges)):
        arcs=[]
        for (u,v),s in zip(Sedges,st):
            if s==1: arcs.append((u,v))
            elif s==2: arcs.append((v,u))
        reps.add(port_reach(arcs,['a','b','l','r','c']))
    return reps

REPS=representable_set()

def check_core(G,label):
    arcs,inner=core_arcs(G,'0','a','b','l','r')
    verts=PORTS+inner
    n=len(arcs)
    assert n<=22, n
    bad2=bad3=0; seen=set()
    for mask in range(1<<n):
        sub=[arcs[i] for i in range(n) if (mask>>i)&1]
        if not acyclic(sub,verts): continue
        rel=port_reach(sub,verts)
        seen.add(rel)
        # Lemma 2 (2)
        if ('a','l') in rel and ('r','b') in rel:
            if not (('a','b') in rel and ('r','l') in rel): bad2+=1
        # Lemma 2 (3)
        if ('b','l') in rel and ('r','a') in rel:
            if not (('b','a') in rel and ('r','l') in rel): bad2+=1
        if rel not in REPS: bad3+=1
    print(f"{label}: |V(K)|={len(verts)} |A(K)|={n} distinct port-relations over acyclic subgraphs={len(seen)}")
    print(f"   Lemma 2 violations: {bad2}   Lemma 3 (non-representable) violations: {bad3}")
    return bad2,bad3,seen

def random_no_instance(rng,nextra):
    while True:
        extra=['u%d'%i for i in range(nextra)]
        V=['s1','s2','t1','t2']+extra
        mid=extra
        A=set()
        for u in ['s1','s2']:
            for v in mid: 
                if rng.random()<0.6: A.add((u,v))
        for u in mid:
            for v in ['t1','t2']:
                if rng.random()<0.6: A.add((u,v))
        for u in mid:
            for v in mid:
                if u!=v and rng.random()<0.35: A.add((u,v))
        G=dict(V=V,A=sorted(A))
        ok,_=normalized_ok(G)
        if ok and not two_linkage_answer(G): return G

if __name__=='__main__':
    tot2=tot3=0
    b2,b3,seen_no=check_core(G_NO,'fixed NO gadget (s1,s2->z->t1,t2)')
    tot2+=b2; tot3+=b3
    rng=random.Random(7)
    allseen=set(seen_no)
    for k in range(6):
        G=random_no_instance(rng,2)
        b2,b3,s=check_core(G,'random NO instance #%d (%d arcs in G)'%(k,len(G['A'])))
        tot2+=b2; tot3+=b3; allseen|=s
    print()
    print('TOTAL Lemma2 violations:',tot2,'  TOTAL Lemma3 violations:',tot3)
    print('distinct achievable port-relations across all NO cores:',len(allseen))
    print('number of Q/Q-contracted representable relations:',len(REPS))
    # also: check that on a YES instance Lemma 2 genuinely FAILS (so the NO hypothesis is load-bearing)
    from construction import G_YES
    arcs,inner=core_arcs(G_YES,'0','a','b','l','r'); verts=PORTS+inner
    cnt=0
    for mask in range(1<<len(arcs)):
        sub=[arcs[i] for i in range(len(arcs)) if (mask>>i)&1]
        if not acyclic(sub,verts): continue
        rel=port_reach(sub,verts)
        if ('a','l') in rel and ('r','b') in rel and not (('a','b') in rel): cnt+=1
    print('YES-core: acyclic subgraphs with both crossings but NOT a->b (Lemma 2 fails, as it must):',cnt)
