"""Lemma 2 (t + 2 rho(A) <= 2^n) over ALL irredundant sets of K_3 x K_3 x K_3 (27 vertices),
and a local search for a large irredundant set in K_3^4 (81 vertices, alpha = 27), one of the
37 cases the source paper leaves open."""
import sys, itertools, random
sys.path.insert(0,'/home/enatale/repos/lelarge/graph-theory-auto/verification_astra/scripts/1904.02595__00')
from core import build, is_irredundant
import numpy as np

def rho(A):
    if not A: return 0
    rows=[]
    for x in A:
        v=np.array([1.0])
        for a in x: v=np.kron(v,np.array([1.0,a+1.0]))
        rows.append(v)
    return int(np.linalg.matrix_rank(np.array(rows), tol=1e-8))

def lemma2_all(factors):
    verts,N,Nc=build(factors); n=len(verts); k=len(factors)
    cell=[tuple(c[0] for c in v) for v in verts]
    worst=[10**9,None]; viol=[0]; cnt=[0]
    def rec(start,S,members):
        cnt[0]+=1
        if members:
            L=[v for v in members if not (N[v]&S)]
            t=len(members)-len(L)
            A=sorted({cell[v] for v in L})
            r=rho(A); slack=2**k-(t+2*r)
            if slack<0:
                viol[0]+=1
                if viol[0]<=3: print("  VIOLATION", members,t,r)
            if slack<worst[0]: worst[0],worst[1]=slack,(t,r,tuple(members))
        for v in range(start,n):
            S2=S|(1<<v)
            if is_irredundant(S2,Nc,n): rec(v+1,S2,members+[v])
    rec(0,0,[])
    print(f"Lemma2 over ALL irredundant sets of {factors}: {cnt[0]} sets, min slack {worst[0]} "
          f"(t={worst[1][0]},rho={worst[1][1]}), violations={viol[0]}", flush=True)

lemma2_all([[1,1,1]]*3)

# --- local search for a big irredundant set in K_3^4 ---
def big_irredundant(factors, iters=300000, seed=0, target=None):
    verts,N,Nc=build(factors); n=len(verts)
    rng=random.Random(seed)
    def irr(S):
        return is_irredundant(S,Nc,n)
    best=0; bestS=0
    S=0; size=0
    for it in range(iters):
        v=rng.randrange(n)
        if S>>v & 1:
            if rng.random()<0.15:
                S&=~(1<<v); size-=1
        else:
            S2=S|(1<<v)
            if irr(S2): S,size=S2,size+1
            elif rng.random()<0.05:
                # random restart-ish kick: drop a random member then try
                members=[u for u in range(n) if S>>u&1]
                if members:
                    u=rng.choice(members); S&=~(1<<u); size-=1
        if size>best:
            best,bestS=size,S
            if target and best>target: 
                print("  EXCEEDED alpha!", [verts[i] for i in range(n) if bestS>>i&1]); break
    return best
print("K_3^4 local search: largest irredundant set found =",
      big_irredundant([[1,1,1]]*4, iters=120000, seed=1, target=27), "(alpha = 27)", flush=True)
