"""Lemma 2 stress test for n=4 (K_3^4): for random independent A, greedily build a large
admissible social/private configuration and check t + 2*rho(A) <= 16."""
import itertools, random
import numpy as np
def rho(A):
    if not A: return 0
    rows=[]
    for x in A:
        v=np.array([1.0])
        for a in x: v=np.kron(v,np.array([1.0,a+1.0]))
        rows.append(v)
    return int(np.linalg.matrix_rank(np.array(rows),tol=1e-8))
def adj(x,y): return all(x[i]!=y[i] for i in range(4))
Om=list(itertools.product(*[range(3)]*4))
rng=random.Random(5)
worst=None; viol=0
for trial in range(300):
    # random independent A (possibly empty)
    k=rng.randint(0,6); order=Om[:]; rng.shuffle(order); A=[]
    for x in order:
        if len(A)>=k: break
        if all(not adj(x,y) for y in A): A.append(x)
    blocked=[z for z in Om if all(not adj(z,a) for a in A)]
    pairs=[(x,y) for x in blocked for y in blocked if adj(x,y)]
    rng.shuffle(pairs)
    best_t=0
    for rep in range(30):
        rng.shuffle(pairs); chosen=[]
        for (x,y) in pairs:
            if any(x==x2 for x2,_ in chosen): continue
            if all((not adj(y,x2)) and (not adj(y2,x)) for x2,y2 in chosen):
                chosen.append((x,y))
        best_t=max(best_t,len(chosen))
    r=rho(A); slack=16-(best_t+2*r)
    if slack<0:
        viol+=1
        if viol<=3: print("  VIOLATION A=",A,"t=",best_t,"rho=",r)
    if worst is None or slack<worst[0]: worst=(slack,tuple(A),best_t,r)
print(f"K_3^4 Lemma-2 stress: 300 random A; min slack(16 - t - 2rho) = {worst[0]} "
      f"(|A|={len(worst[1])}, t={worst[2]}, rho={worst[3]}); violations={viol}")
