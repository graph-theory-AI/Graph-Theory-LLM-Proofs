"""Extra stress of the Section-5 DP for d=2 and d=3 on tournaments engineered to
be NO-instances (near-transitive with a few long reversed arcs), n up to 9."""
import itertools, random

def brute(arc, n, d):
    for order in itertools.permutations(range(n)):
        pos = {v:i for i,v in enumerate(order)}
        deg=[0]*n
        for u in range(n):
            for v in range(n):
                if arc[u][v] and pos[u]>pos[v]: deg[u]+=1; deg[v]+=1
        if max(deg)<=d: return True
    return False

def dp(arc,n,d):
    outdeg=[sum(1 for v in range(n) if arc[u][v]) for u in range(n)]
    a=[n-outdeg[v] for v in range(n)]
    lo=[max(1,a[v]-d) for v in range(n)]; hi=[min(n,a[v]+d) for v in range(n)]
    for i in range(1,n):
        if len([v for v in range(n) if lo[v]<=i<hi[v]])>4*d: return False
    full=(1<<n)-1; layer={0}
    for i in range(n):
        nxt=set()
        for S in layer:
            for v in range(n):
                if S>>v&1: continue
                if not (lo[v]<=i+1<=hi[v]): continue
                beta=0
                for u in range(n):
                    if u==v: continue
                    if S>>u&1:
                        if arc[v][u]: beta+=1
                    else:
                        if arc[u][v]: beta+=1
                if beta>d: continue
                S2=S|(1<<v); ok=True
                for w in range(n):
                    if hi[w]<=i+1 and not(S2>>w&1): ok=False;break
                    if (S2>>w&1) and lo[w]>i+1: ok=False;break
                if ok: nxt.add(S2)
        layer=nxt
        if not layer: return False
    return full in layer

rng=random.Random(7)
for d in [2,3]:
    tot=no=mis=0
    for n in [7,8,9]:
        for trial in range(200):
            arc=[[False]*n for _ in range(n)]
            for i in range(n):
                for j in range(i+1,n): arc[i][j]=True
            k=rng.randint(1,5)
            for _ in range(k):
                i=rng.randrange(n); j=rng.randrange(n)
                if i==j: continue
                i,j=min(i,j),max(i,j)
                arc[i][j]=False; arc[j][i]=True
            # also fully random sometimes
            if trial%3==0:
                for i in range(n):
                    for j in range(i+1,n):
                        b=rng.random()<0.5; arc[i][j]=b; arc[j][i]=not b
            b=brute(arc,n,d); D=dp(arc,n,d); tot+=1; no += (not b)
            if b!=D:
                mis+=1; print("MISMATCH",d,n,arc)
    print(f"d={d}: {tot} tournaments, {no} NO-instances, {mis} mismatches")
