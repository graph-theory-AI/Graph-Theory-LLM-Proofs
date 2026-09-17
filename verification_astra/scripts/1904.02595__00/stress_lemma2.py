"""Direct stress test of Lemma 2 (t + 2*rho(A) <= 2^n) at the quotient level.
Any irredundant set induces labels A (lonely cells), x_1..x_t (social cells) and y_1..y_t
(their private neighbours' cells) satisfying:
  (i)  A pairwise non-adjacent;              (ii)  x_k non-adjacent to every a in A;
  (iii) y_j non-adjacent to every a in A;     (iv)  y_j adjacent to x_j;
  (v)  y_j non-adjacent to x_k for j != k.
We search for configurations maximising t + 2*rho(A) and compare with 2^n."""
import itertools, random, sys
import numpy as np
import networkx as nx

def rho(A):
    if not A: return 0
    rows=[]
    for x in A:
        v=np.array([1.0])
        for a in x: v=np.kron(v,np.array([1.0,a+1.0]))
        rows.append(v)
    return int(np.linalg.matrix_rank(np.array(rows), tol=1e-8))
def adj(x,y): return all(x[i]!=y[i] for i in range(len(x)))

def max_t(A, Om):
    blocked=[z for z in Om if all(not adj(z,a) for a in A)]
    pairs=[(x,y) for x in blocked for y in blocked if adj(x,y)]
    if not pairs: return 0, []
    G=nx.Graph(); G.add_nodes_from(range(len(pairs)))
    for j,k in itertools.combinations(range(len(pairs)),2):
        (xj,yj),(xk,yk)=pairs[j],pairs[k]
        if xj!=xk and (not adj(yj,xk)) and (not adj(yk,xj)):
            G.add_edge(j,k)
    best=[]
    for cl in nx.find_cliques(G):
        if len(cl)>len(best): best=cl
    return len(best), [pairs[i] for i in best]

def run(n,q,indep_families, tag):
    worst=None; viol=0
    for A in indep_families:
        t,_=max_t(list(A), list(itertools.product(*[range(q)]*n)))
        r=rho(list(A)); slack=2**n-(t+2*r)
        if slack<0:
            viol+=1
            if viol<=3: print("   VIOLATION", A, t, r)
        if worst is None or slack<worst[0]: worst=(slack,A,t,r)
    print(f"{tag}: families tested={len(indep_families)} min slack(2^n - t - 2rho)={worst[0]} "
          f"at A={worst[1]} t={worst[2]} rho={worst[3]}; violations={viol}", flush=True)

def enum_indep(Om, maxsize):
    out=[]
    def rec(start,cur):
        if cur: out.append(tuple(cur))
        if len(cur)>=maxsize: return
        for i in range(start,len(Om)):
            x=Om[i]
            if all(not adj(x,y) for y in cur):
                cur.append(x); rec(i+1,cur); cur.pop()
    rec(0,[])
    return out

# n=2, q=3: all independent families (plus empty A)
Om2=list(itertools.product(*[range(3)]*2))
fams=[()]+enum_indep(Om2,3)
run(2,3,fams,"K_3^2, ALL A (incl. empty)")
# n=3, q=3: A of size <= 2 exhaustive + random larger
Om3=list(itertools.product(*[range(3)]*3))
fams=[()]+enum_indep(Om3,2)
run(3,3,fams,"K_3^3, A of size <= 2")
rng=random.Random(2)
big=[]
for _ in range(25):
    order=Om3[:]; rng.shuffle(order); cur=[]
    for x in order:
        if all(not adj(x,y) for y in cur): cur.append(x)
    k=rng.randint(3,len(cur))
    big.append(tuple(rng.sample(cur,k)))
run(3,3,big,"K_3^3, random larger A")
