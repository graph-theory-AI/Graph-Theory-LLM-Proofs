"""Check 5b: stress the P-node DP as a pure scheduling claim, with RANDOM
(not necessarily graph-realizable) child profiles, and with more children."""
import itertools, random
from check5_pnode import pnode_dp, pnode_brute_orders

random.seed(17)
bad=0; tested=0; badmono=0; testedmono=0
for trial in range(4000):
    r=random.randint(2,5)
    cp=[]
    for _ in range(r):
        L=random.randint(1,4)
        F={d: random.randint(1,9) for d in range(L+1)}
        cp.append((L,F))
    Lam=sum(c[0] for c in cp)
    d=random.randint(0,Lam)
    tested+=1
    a=pnode_dp(cp,d); b=pnode_brute_orders(cp,d)
    if a!=b:
        bad+=1
        if bad<=5: print("RANDOM-PROFILE MISMATCH", cp, d, a, b)
# now with monotone nondecreasing, 1-Lipschitz profiles (as graph ones are)
for trial in range(4000):
    r=random.randint(2,5)
    cp=[]
    for _ in range(r):
        L=random.randint(1,4)
        base=random.randint(1,6); F={0:base}
        for d in range(1,L+1):
            F[d]=F[d-1]+random.choice([0,0,1])
        cp.append((L,F))
    Lam=sum(c[0] for c in cp)
    d=random.randint(0,Lam)
    testedmono+=1
    a=pnode_dp(cp,d); b=pnode_brute_orders(cp,d)
    if a!=b:
        badmono+=1
        if badmono<=5: print("MONOTONE-PROFILE MISMATCH", cp, d, a, b)
print(f"random profiles: {tested} cases, mismatches={bad}")
print(f"monotone 1-Lipschitz profiles: {testedmono} cases, mismatches={badmono}")
