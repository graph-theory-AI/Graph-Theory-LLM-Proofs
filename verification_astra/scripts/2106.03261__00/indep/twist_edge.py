import sys
sys.path.insert(0,'/home/enatale/repos/lelarge/graph-theory-auto/verification_astra/scripts/2106.03261__00/indep')
import build as B
from build import PV, PE, PADJ
import itertools
from collections import defaultdict

def build_twist(q, twist_edge):
    k=(q-1)//10
    nz=list(range(1,q)); I={v:nz[i*k:(i+1)*k] for i,v in enumerate(PV)}
    V={v:[(x,y) for x in I[v] for y in range(q) if (2*y)%q!=(x*x)%q] for v in PV}
    c={e:(1 if set(e)==set(twist_edge) else 0) for e in PE}
    A={z:defaultdict(set) for v in PV for z in V[v]}
    for (u,v) in PE:
        cc=c[(u,v)]
        for (x,y) in V[u]:
            for xp in I[v]:
                yp=(x*xp-y+cc)%q
                if (2*yp)%q!=(xp*xp)%q:
                    A[(x,y)][v].add((xp,yp)); A[(xp,yp)][u].add((x,y))
    adj={z:set().union(*d.values()) if d else set() for z,d in A.items()}
    return dict(q=q,k=k,I=I,V=V,Vset={v:set(V[v]) for v in PV},A=A,adj=adj,c=c)

q=61
for e in [('a3','b3'),('a0','a1'),('b0','b2'),None]:
    D = build_twist(q, e) if e else build_twist(q, ('zz','zz'))
    n=sum(len(D['V'][v]) for v in PV)
    t,_=B.count_canonical(D)
    h=B.count_hom(D)
    # C4-freeness
    cod=defaultdict(int)
    for z,nb in D['adj'].items():
        for a,b in itertools.combinations(sorted(nb),2): cod[(a,b)]+=1
    print(f"q={q} twist={e}: n={n} maxcodeg={max(cod.values())} canonical={t} hom(P,G)={h}")
