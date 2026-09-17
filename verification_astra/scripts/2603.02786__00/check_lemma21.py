"""Lemma 2.1: colour {A_a(N) : a<=N} (unshifted, A_a(N)=multiples of a in [1,N])
into few classes of pairwise-DISJOINT progressions.  Edge  a~b  iff lcm(a,b)<=N.
Checks (i) the divisor bound tau(t) = O(t^{1/10}), (ii) the degree bound
O(sqrt(N)*max tau), (iii) actual greedy chromatic number vs K0*N^{3/5}."""
import math
from math import gcd

def divisor_counts(N):
    tau=[0]*(N+1)
    for d in range(1,N+1):
        for m in range(d,N+1,d): tau[m]+=1
    return tau

for N in [200,1000,5000,20000,60000]:
    tau=divisor_counts(N)
    maxtau=max(tau[1:])
    K_tau=max(tau[t]/t**0.1 for t in range(1,N+1))
    root=math.isqrt(N)
    # build graph only on a>root (a<=root get private classes)
    big=[a for a in range(root+1,N+1)]
    adj={a:set() for a in big}
    for a in big:
        for k in range(1,N//a+1):
            m=k*a
            for b in range(1,int(math.isqrt(m))+1):
                if m%b==0:
                    for cand in (b,m//b):
                        if cand>root and cand!=a and (a*cand)//gcd(a,cand)<=N:
                            adj[a].add(cand)
    maxdeg=max((len(v) for v in adj.values()),default=0)
    # greedy colouring, largest-degree first
    order=sorted(big,key=lambda a:-len(adj[a]))
    col={}
    for a in order:
        used={col[b] for b in adj[a] if b in col}
        c=0
        while c in used: c+=1
        col[a]=c
    ncol=(max(col.values())+1) if col else 0
    R=root+ncol
    print(f"N={N:6d}  maxtau={maxtau:3d}  max tau(t)/t^.1={K_tau:5.2f}  maxdeg(big)={maxdeg:5d}"
          f"  bound sqrt(N)*maxtau={root*maxtau:7d}  greedy colours(big)={ncol:4d}"
          f"  R(N)={R:5d}   R/N^0.6={R/N**0.6:5.2f}")
