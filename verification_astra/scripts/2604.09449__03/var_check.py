"""Exact check of the variance bound (23): sum over ordered edge pairs of |Cov(I_e,I_f)| <= 4 N^2 (L=1)."""
from itertools import combinations
from fractions import Fraction as F
def run(N):
    V=list(range(N)); a=(N+1)//2
    subs=[set(s) for s in combinations(V,a)]
    tot=len(subs)
    E=list(combinations(V,2))
    cross={e:[ (e[0] in S)!=(e[1] in S) for S in subs] for e in E}
    p={e:F(sum(cross[e]),tot) for e in E}
    S=F(0)
    for e in E:
        for f in E:
            joint=F(sum(1 for i in range(tot) if cross[e][i] and cross[f][i]),tot)
            S+=abs(joint-p[e]*p[f])
    claimed_bound = F(1,4)*len(E) + F(2,N)*3*len(list(combinations(V,3))) + F(8,N*N)*3*len(list(combinations(V,4)))
    return S, claimed_bound, F(17,8)*N*N, 4*N*N
for N in range(4,10):
    S,cb,c178,c4=run(N)
    print(N, "sum|Cov| =",float(S), " writeup's bound-expr =",float(cb), " (17/8)N^2 =",float(c178), " 4N^2 =",float(c4),
          " ok:", S<=cb, cb<=c178, cb<=c4)
