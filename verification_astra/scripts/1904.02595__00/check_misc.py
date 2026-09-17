"""(a) rho(D) = |D cap {1,2}^n| for down-sets D (writeup eq. 5.2);
   (b) compression terminates in a down-set and rho non-increasing (Lemma 3 + 4.2);
   (c) seeded search for a big irredundant set in K_3^4."""
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
def indep(x,y): return any(x[i]==y[i] for i in range(len(x)))
def compress(A,i):
    fib={}
    for x in A: fib.setdefault(x[:i]+x[i+1:],[]).append(x[i])
    return sorted(k[:i]+(j,)+k[i:] for k,l in fib.items() for j in range(len(l)))
def full_compress(A,n):
    A=sorted(A)
    while True:
        for i in range(n):
            B=compress(A,i)
            if B!=A: A=B; break
        else: return A

rng=random.Random(0); bad=0; tested=0
for trial in range(400):
    n=rng.randint(1,4); q=rng.randint(3,5)
    Om=list(itertools.product(*[range(q)]*n))
    # random down-set
    D=set()
    for _ in range(rng.randint(1,8)):
        x=rng.choice(Om)
        for y in itertools.product(*[range(a+1) for a in x]): D.add(y)
    D=sorted(D); tested+=1
    r=rho(D); cnt=sum(1 for x in D if all(a<=1 for a in x))
    if r!=cnt:
        bad+=1
        if bad<=3: print("  (a) MISMATCH", n,q,D,r,cnt)
print(f"(a) rho(D)=|D cap {{1,2}}^n| on {tested} random down-sets: mismatches={bad}")

bad=0; tested=0
for trial in range(300):
    n=rng.randint(1,4); q=rng.randint(3,4)
    Om=list(itertools.product(*[range(q)]*n))
    A=rng.sample(Om, rng.randint(1,min(len(Om),8)))
    D=full_compress(A,n); tested+=1
    isdown=all(all(y in set(D) for y in itertools.product(*[range(a+1) for a in x])) for x in D)
    if not isdown or rho(D)>rho(A) or len(D)!=len(A):
        bad+=1
        if bad<=3: print("  (b) PROBLEM", A, D, isdown, rho(A), rho(D))
print(f"(b) full compression -> down-set, rank non-increasing, size preserved: {tested} random families, problems={bad}")

# (c) seeded irredundant-set search in K_3^4
factors=[[1,1,1]]*4
verts,N,Nc=build(factors); n=len(verts)
best=0
for seed in range(20):
    rng2=random.Random(seed)
    i=rng2.randrange(4); a=rng2.randrange(3)
    S=0; members=[]
    for idx,v in enumerate(verts):
        if v[i][0]==a: S|=1<<idx; members.append(idx)
    size=len(members)
    for it in range(20000):
        u=rng2.randrange(n)
        if S>>u&1: continue
        S2=S|(1<<u)
        if is_irredundant(S2,Nc,n): S,size=S2,size+1
        elif rng2.random()<0.3:
            m=[x for x in range(n) if S>>x&1]
            drop=rng2.choice(m); S3=(S & ~(1<<drop))|(1<<u)
            if is_irredundant(S3,Nc,n): S=S3
    best=max(best,size)
print(f"(c) K_3^4 (alpha=27): largest irredundant set found by seeded search = {best}")
