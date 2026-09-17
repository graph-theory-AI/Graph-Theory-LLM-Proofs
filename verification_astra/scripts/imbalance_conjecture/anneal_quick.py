import sys, random, itertools
sys.path.insert(0,'/home/enatale/repos/lelarge/graph-theory-auto/verification_astra/scripts/imbalance_conjecture')
from check_lemma import is_graphic
def stats(n, adj):
    deg=[len(adj[i]) for i in range(n)]
    edges=[(u,v) for u in range(n) for v in adj[u] if u<v]
    if not edges: return None
    imb=sorted((abs(deg[u]-deg[v]) for u,v in edges), reverse=True)
    z=sum(1 for x in imb if x==0); D=max(deg)
    if D<2: return None
    return z, min(sum(min(k,x) for x in imb[k:])-k*(D-k) for k in range(1,D)), deg, imb
def anneal(n, iters, seed):
    rnd=random.Random(seed); adj=[set() for _ in range(n)]
    for u,v in itertools.combinations(range(n),2):
        if rnd.random()<0.3: adj[u].add(v); adj[v].add(u)
    best=None; cur=None
    for it in range(iters):
        u,v=rnd.sample(range(n),2)
        if v in adj[u]: adj[u].discard(v); adj[v].discard(u); undo='add'
        else: adj[u].add(v); adj[v].add(u); undo='del'
        s=stats(n,adj); sc=10**6 if s is None else 1000*s[0]+s[1]
        T=max(0.01,3.0*(1-it/iters))
        if cur is None or sc<=cur or rnd.random()<pow(2.718,-(sc-cur)/T):
            cur=sc
            if s and s[0]==0 and (best is None or s[1]<best[1]): best=s
        else:
            if undo=='add': adj[u].add(v); adj[v].add(u)
            else: adj[u].discard(v); adj[v].discard(u)
    return best
viol=0; nong=0; tot=0; gmin=None
for n in range(8,25):
    bn=None
    for seed in range(6):
        b=anneal(n,6000,seed*977+n)
        if b is None: continue
        tot+=1
        if bn is None or b[1]<bn[1]: bn=b
        if b[1]<0: viol+=1
        if not is_graphic(b[3]): nong+=1
    if bn:
        print(f"n={n:3d} min tail-slack={bn[1]:4d}")
        if gmin is None or bn[1]<gmin: gmin=bn[1]
print("instances:",tot," lemma violations:",viol," non-graphic M_G:",nong," global min slack:",gmin)
