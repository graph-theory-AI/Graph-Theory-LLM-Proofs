"""Check 5: the P-node recurrence (sec. 6) -- the two-arm DP -- against
(a) brute force over all r! orderings using the writeup's own cost formula, and
(b) the true brute-force profile of the composed graph."""
import itertools, random
from comps import *
INF=float('inf')

def pnode_dp(children_prof, d):
    """children_prof: list of (ell_i, F_i dict). Returns F_H(d) per sec 6.2."""
    r=len(children_prof)
    L=[c[0] for c in children_prof]; F=[c[1] for c in children_prof]
    Lam=sum(L)
    p=[F[i][L[i]] for i in range(r)]
    q=[p[i]-L[i] for i in range(r)]
    best=INF
    for j in range(r):
        others=sorted([i for i in range(r) if i!=j], key=lambda i:-q[i])
        T={0:0}; S=0
        for i in others:
            nT={}
            for x,val in T.items():
                # left
                k=x+L[i]; c=max(val, x+p[i])
                if c<nT.get(k,INF): nT[k]=c
                # right
                c2=max(val, d+(S-x)+p[i])
                if c2<nT.get(x,INF): nT[x]=c2
            S+=L[i]; T=nT
        for X,val in T.items():
            Y=Lam-L[j]-X
            if abs(X-(d+Y))<=L[j]:
                tot=max(val, min(X,d+Y)+F[j][abs(X-(d+Y))])
                best=min(best,tot)
    return best

def pnode_brute_orders(children_prof, d):
    r=len(children_prof)
    L=[c[0] for c in children_prof]; F=[c[1] for c in children_prof]
    Lam=sum(L)
    best=INF
    for perm in itertools.permutations(range(r)):
        pos=0; cost=0
        for i in perm:
            a=min(pos, d+Lam-pos)
            b=min(pos+L[i], d+Lam-pos-L[i])
            cost=max(cost, min(a,b)+F[i][abs(a-b)])
            pos+=L[i]
        best=min(best,cost)
    return best

lib=[edge_comp(), path2(0), path2(3), path3(0,0), path3(4,1), cyc_pair(),
     k4me(), doubleedge(), triangle_ear()]
profs={}
for c in lib:
    profs[c.name+str(sorted(c.w.items()))]=c.brute_profile()

random.seed(13)
tested=0; bad_dp=0; bad_true=0
cases=[]
for r in (2,3):
    for combo in itertools.combinations_with_replacement(range(len(lib)), r):
        cases.append([lib[i] for i in combo])
random.shuffle(cases)
for children in cases[:60]:
    cp=[c.brute_profile() for c in children]
    P=parallel(children)
    g,rho,w=P.hat()
    size=sum(max(len(g.inc[v])-1,0) for v in range(g.n))
    if size>13: continue
    try:
        Ltrue,Ftrue = P.brute_profile()
    except Exception as ex:
        continue
    Lam=sum(c[0] for c in cp)
    if Ltrue!=Lam:
        print("ELL MISMATCH at P-node", [c.name for c in children], Ltrue, Lam); bad_true+=1
    for d in range(Lam+1):
        tested+=1
        v_dp=pnode_dp(cp,d); v_br=pnode_brute_orders(cp,d)
        v_true=Ftrue.get(d)
        if v_dp!=v_br:
            bad_dp+=1; print("DP != ORDER-BRUTE", [c.name for c in children], d, v_dp, v_br)
        if v_true is not None and v_br!=v_true:
            bad_true+=1; print("FORMULA != TRUE PROFILE", [c.name for c in children], d, v_br, v_true)
print(f"P-node: {tested} (composition,d) cases; DP vs ordering-brute mismatches={bad_dp}; formula vs true profile mismatches={bad_true}")
