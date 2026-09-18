"""Non-vacuity statistics for the lemma checks."""
import sys
from itertools import combinations
sys.path.insert(0,'/home/enatale/repos/lelarge/graph-theory-auto/verification_astra/scripts/1602.05184__00')
from check_lemmas import parse_g6, G, type_of, is_2connected, induced, is_C5

stat = {'graphs':0,'lowc_pairs':0,'typeI':0,'typeII':0,'both':0,
        'L4.2_applies':0,'L4.1_applies':0,'P4.3_applies':0,'dominated_pairs':0,
        'nonsimplicial_dominated':0,'eta_lt_2n':0}
for line in sys.stdin:
    line=line.strip()
    if not line: continue
    n,adj=parse_g6(line); g=G(n,adj); stat['graphs']+=1
    eta=g.eta()
    universal=[v for v in range(n) if len(adj[v])==n-1]
    if eta<2*n: stat['eta_lt_2n']+=1
    for a in range(n):
        if a in universal: continue
        if g.c(a)<=3:
            stat['lowc_pairs']+=1
            t=type_of(g,a)
            if t=='I': stat['typeI']+=1
            elif t=='II': stat['typeII']+=1
    for u in range(n):
        if any(v!=u and (adj[u]|{u})<=(adj[v]|{v}) for v in range(n)):
            stat['dominated_pairs']+=1
            if not all(y in adj[x] for x,y in combinations(adj[u],2)):
                stat['nonsimplicial_dominated']+=1
    if not universal:
        low=[a for a in range(n) if g.c(a)<=3]
        for a in low:
            if all(y in adj[x] for x,y in combinations(adj[a],2)): stat['L4.2_applies']+=1
        if low and not is_C5(n,adj):
            stat['L4.1_applies']+=1
            if eta<2*n: stat['P4.3_applies']+=1
print(f"n={n}", stat)
