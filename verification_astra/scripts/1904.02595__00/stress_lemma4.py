"""Stress test Lemma 4 in unit-weight K_3^n (n=3,4,5): maximise |A| - 2*rho(A) over nonempty
independent A.  Lemma 4 is equivalent to  max <= alpha - 2^n  (1, 11, 49 for n=3,4,5).
Uses (a) random maximal independent families, (b) simulated annealing, (c) explicit families."""
import sys, itertools, random
import numpy as np

def zmat(A):
    rows=[]
    for x in A:
        v=np.array([1.0])
        for a in x: v=np.kron(v, np.array([1.0, a+1.0]))
        rows.append(v)
    return np.array(rows)
def rho(A):
    return 0 if not A else int(np.linalg.matrix_rank(zmat(A), tol=1e-7))
def indep(x,y): return any(x[i]==y[i] for i in range(len(x)))
def val(A): return len(A)-2*rho(A)

def maximal_from(seed_pts, Om, rng):
    A=list(seed_pts)
    order=Om[:]; rng.shuffle(order)
    for x in order:
        if x in A: continue
        if all(indep(x,y) for y in A): A.append(x)
    return A

def run(n, q=3, alpha=None, trials=300, anneal=4000, seed=1):
    rng=random.Random(seed)
    Om=list(itertools.product(*[range(q)]*n))
    best=-10**9; bestA=None
    # (a) random maximal families and random subsets
    for _ in range(trials):
        A=maximal_from([], Om, rng)
        for cand in [A]+[rng.sample(A, rng.randint(1,len(A))) for _ in range(3)]:
            v=val(cand)
            if v>best: best,bestA=v,cand[:]
    # (b) simulated annealing from a random maximal family
    A=maximal_from([], Om, rng); cur=val(A)
    T=2.0
    for it in range(anneal):
        T=max(0.05, 2.0*(1-it/anneal))
        if rng.random()<0.5 and len(A)>1:
            A2=A[:]; A2.pop(rng.randrange(len(A2)))
        else:
            x=rng.choice(Om)
            if x in A: continue
            A2=[y for y in A if indep(x,y)]+[x]
        v=val(A2)
        if v>=cur or rng.random()<pow(2.718,(v-cur)/T):
            A,cur=A2,v
            if v>best: best,bestA=v,A[:]
    # (c) explicit canonical families: fix coordinate i to value a
    for i in range(n):
        for a in range(q):
            A=[x for x in Om if x[i]==a]
            v=val(A)
            if v>best: best,bestA=v,A
    print(f"K_{q}^{n}: bound alpha-2^n = {alpha-2**n}; max found |A|-2rho = {best} "
          f"(|A|={len(bestA)}, rho={rho(bestA)}) -> "
          + ("OK" if best<=alpha-2**n else "LEMMA 4 VIOLATED"), flush=True)

run(3, alpha=9,  seed=3, trials=400, anneal=6000)
run(4, alpha=27, seed=4, trials=400, anneal=6000)
run(5, alpha=81, seed=5, trials=150, anneal=3000)
