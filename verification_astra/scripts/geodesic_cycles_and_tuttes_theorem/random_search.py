"""Randomised / annealed search for a length assignment l on G with
'every l-geodesic cycle is peripheral', plus statistics corroborating the
writeup's intermediate claims (tight core edges, geodesic faces)."""
import itertools, random, math, networkx as nx

B = [f"b{i}" for i in range(1,5)]; S = [f"s{i}" for i in range(1,5)]
G = nx.Graph(); G.add_edges_from(itertools.combinations(B,2))
for i in range(1,5):
    for j in range(1,5):
        if i!=j: G.add_edge(f"s{i}", f"b{j}")
E = sorted(tuple(sorted(e)) for e in G.edges())
cycles = list(nx.simple_cycles(G))
def induced(c): return G.subgraph(c).number_of_edges()==len(c)
def peripheral(c):
    if not induced(c): return False
    H=G.copy(); H.remove_nodes_from(c); return nx.is_connected(H)
per = [c for c in cycles if peripheral(c)]
nonper = [c for c in cycles if not peripheral(c)]

def arcs(c,i,j):
    a1=[(c[t],c[t+1]) for t in range(i,j)]
    rot=c[j:]+c[:i+1]
    a2=[(rot[t],rot[t+1]) for t in range(len(rot)-1)]
    return a1,a2

def analyse(l):
    for e in E: G[e[0]][e[1]]['w']=l[e]
    d=dict(nx.all_pairs_dijkstra_path_length(G,weight='w'))
    def wt(es): return sum(l[tuple(sorted(e))] for e in es)
    def geodesic(c):
        k=len(c)
        for i,j in itertools.combinations(range(k),2):
            a1,a2=arcs(c,i,j)
            if d[c[i]][c[j]] < min(wt(a1),wt(a2))-1e-12: return False
        return True
    bad=[c for c in nonper if geodesic(c)]
    geo_per=[c for c in per if geodesic(c)]
    nontight=[e for e in E if l[e] > d[e[0]][e[1]]+1e-12]
    return bad, geo_per, nontight

def rnd(mode):
    if mode==0: return {e: random.uniform(0.01,1) for e in E}
    if mode==1: return {e: math.exp(random.uniform(-8,8)) for e in E}
    if mode==2: return {e: random.choice([1,2,3,5,10,100]) * random.uniform(.9,1.1) for e in E}
    return {e: random.expovariate(1.0) for e in E}

random.seed(1)
best=None; stats={}
N=40000
for t in range(N):
    l=rnd(t%4)
    bad,gp,nt=analyse(l)
    stats[len(bad)]=stats.get(len(bad),0)+1
    if best is None or len(bad)<len(best[0]): best=(bad,l,gp,nt)
    if not bad:
        print("FOUND assignment with no non-peripheral geodesic cycle:", l); break
print("random trials:", N, " distribution of #non-peripheral geodesic cycles:",
      dict(sorted(stats.items())))
bad,l,gp,nt = best
print("best found: %d non-peripheral geodesic cycles; #geodesic peripheral=%d; #non-tight core edges=%d"
      % (len(bad), len(gp), len([e for e in nt if e[0][0]=='b' and e[1][0]=='b'])))
print("example of the best assignment:", {f"{a}{b}": round(v,4) for (a,b),v in l.items()})
print("its non-peripheral geodesic cycles:", [sorted(c) for c in bad][:10])

# simulated annealing on log-lengths minimising #non-peripheral geodesic cycles
cur={e: math.exp(random.uniform(-2,2)) for e in E}
curval=len(analyse(cur)[0]); T0=2.0
for step in range(20000):
    T=T0*(1-step/20000)+1e-3
    cand=dict(cur); e=random.choice(E); cand[e]=cur[e]*math.exp(random.gauss(0,0.6))
    v=len(analyse(cand)[0])
    if v<=curval or random.random()<math.exp((curval-v)/T):
        cur,curval=cand,v
    if curval==0:
        print("ANNEALING FOUND A VALID ASSIGNMENT:", cur); break
print("annealing best #non-peripheral geodesic cycles:", curval)

# proof-structure corroboration: count how often >=2 core edges are non-tight
cnt={}
for t in range(3000):
    l=rnd(t%4); bad,gp,nt=analyse(l)
    ncore=len([e for e in nt if e[0][0]=='b' and e[1][0]=='b'])
    cnt[(ncore, 12-len(gp))]=cnt.get((ncore,12-len(gp)),0)+1
print("(#non-tight core edges, #non-geodesic faces) frequency:", dict(sorted(cnt.items())))
