"""Lemma 4 for n=3,4: exhaustive over small independent families + random sampling of
(near-)maximal ones, with random part-size weights."""
import sys, itertools, random
sys.path.insert(0, '/home/enatale/repos/lelarge/graph-theory-auto/verification_astra/scripts/1904.02595__00')
from sympy import Matrix
import networkx as nx

def zvec(x):
    v = [1]
    for a in x: v = [c*t for c in v for t in (1, a+1)]
    return v
def rho(A):
    return Matrix([zvec(x) for x in A]).rank() if A else 0
def indep(x,y): return any(x[i]==y[i] for i in range(len(x)))
def wt(x,s):
    p=1
    for i,a in enumerate(x): p*=s[i][a]
    return p
def W(A,s): return sum(wt(x,s) for x in A)

def alpha_w(qs,s):
    Om=list(itertools.product(*[range(q) for q in qs]))
    G=nx.Graph()
    for x in Om: G.add_node(x,weight=wt(x,s))
    for x,y in itertools.combinations(Om,2):
        if indep(x,y): G.add_edge(x,y)
    return nx.max_weight_clique(G,weight='weight')[1]

def test(qs, s, maxsize, nrand, tag):
    n=len(qs); Om=list(itertools.product(*[range(q) for q in qs]))
    aw=alpha_w(qs,s)
    worst=(10**9,None); viol=0; tested=0
    def chk(A):
        nonlocal worst,viol,tested
        tested+=1
        r=rho(A); slack=(aw-W(A,s))-(2**n-2*r)
        if slack<0:
            viol+=1
            if viol<=3: print("   VIOLATION",A,"aw",aw,"W",W(A,s),"rho",r)
        if slack<worst[0]: worst=(slack,(tuple(A),r,W(A,s)))
    # exhaustive small families
    def rec(start,cur):
        if cur: chk(list(cur))
        if len(cur)>=maxsize: return
        for i in range(start,len(Om)):
            x=Om[i]
            if all(indep(x,y) for y in cur):
                cur.append(x); rec(i+1,cur); cur.pop()
    rec(0,[])
    ex=tested
    # random greedy maximal families and random subsets of them
    for _ in range(nrand):
        order=Om[:]; random.shuffle(order); cur=[]
        for x in order:
            if all(indep(x,y) for y in cur): cur.append(x)
        chk(cur)
        for _ in range(3):
            k=random.randint(1,len(cur))
            chk(random.sample(cur,k))
    print(f"{tag} q={qs} alpha_w={aw} exhaustive<= {maxsize}: {ex} fams, +random: total {tested}; min slack={worst[0]} at rho={worst[1][1]},W={worst[1][2]}; violations={viol}")

random.seed(11)
test((3,3,3), [[1,1,1]]*3, 3, 400, "n=3 unit")
for t in range(2):
    s=[sorted([random.randint(1,4) for _ in range(3)],reverse=True) for _ in range(3)]
    test((3,3,3), s, 3, 300, f"n=3 rand{t} s={s}")
test((3,3,3,3), [[1,1,1]]*4, 2, 400, "n=4 unit")
for t in range(2):
    s=[sorted([random.randint(1,3) for _ in range(3)],reverse=True) for _ in range(4)]
    test((3,3,3,3), s, 2, 300, f"n=4 rand{t} s={s}")
test((3,4,3), [[2,1,1],[3,2,1,1],[1,1,1]], 3, 200, "n=3 mixed")
