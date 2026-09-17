"""Step 2: verify Lemmas 2, 3, Corollary 4 and Section 4 Case 2.

Lemma 2 and Lemma 3 are *local* statements (5 resp. 3 vertices), so the
enumerations below are COMPLETE proofs of them, not just samples.
"""
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tstar import *
from itertools import combinations, permutations, product

adj_T, _ = tstar()

# ---------- A. Lemma 2, exhaustive over the only free orientations ----------
# vertices 0=x, 1=y, 2=p, 3=z1, 4=z2
# forced:  x->y ; x->p, p->y (p in P(x,y)) ; y->zi, zi->x (zi in Z(x,y))
# free:    z1 vs z2 ; and the case split p->{z1,z2} vs {z1,z2}->p
def build(case, z1z2):
    a = [[False]*5 for _ in range(5)]
    def arc(u,v): a[u][v]=True
    arc(0,1); arc(0,2); arc(2,1)
    for z in (3,4): arc(1,z); arc(z,0)
    if case == 'p_beats':
        arc(2,3); arc(2,4)
    else:
        arc(3,2); arc(4,2)
    if z1z2: arc(3,4)
    else: arc(4,3)
    return a

print("== Lemma 2: both case-configurations induce T* (complete enumeration) ==")
allok = True
for case in ('p_beats','p_loses'):
    for z1z2 in (True, False):
        a = build(case, z1z2)
        assert is_tournament(a)
        ok = iso(a, adj_T)
        allok &= ok
        print(f"   case={case:8s} z1->z2={z1z2}: tournament={is_tournament(a)}  isomorphic to T*: {ok}")
print("   Lemma 2 local claim verified:", allok)

# and the pigeonhole: any 3 vertices of Z, 2 share orientation wrt p -- trivial, but
# verify the full statement on all 6-vertex configurations with |Z|>=3, P nonempty:
print("\n== Lemma 2 restated: no tournament has an arc with P != empty and |Z| >= 3 while being T*-free ==")
# vertices 0=x,1=y,2=p,3,4,5 = z1,z2,z3 ; free: p vs zi (8), zi vs zj (8) -> 64
cnt_bad = 0
for pz in product([0,1],repeat=3):
    for zz in product([0,1],repeat=3):
        a=[[False]*6 for _ in range(6)]
        def arc(u,v): a[u][v]=True
        arc(0,1); arc(0,2); arc(2,1)
        for z in (3,4,5): arc(1,z); arc(z,0)
        for i,z in enumerate((3,4,5)):
            if pz[i]: arc(2,z)
            else: arc(z,2)
        pairs=[(3,4),(3,5),(4,5)]
        for i,(u,v) in enumerate(pairs):
            if zz[i]: arc(u,v)
            else: arc(v,u)
        assert is_tournament(a)
        if not contains_tstar(a): cnt_bad += 1
print("   number of the 64 configurations that are T*-FREE:", cnt_bad, "(must be 0)")

# ---------- B. Lemma 3, exhaustive local check ----------
print("\n== Lemma 3: arcs with P(x,y)=empty form a graph of max degree <= 2 ==")
# local proof check: two out-arcs at x with P empty is impossible (3 vertices)
bad = 0
for d in (0,1):
    a=[[False]*3 for _ in range(3)]
    a[0][1]=True; a[0][2]=True
    if d: a[1][2]=True
    else: a[2][1]=True
    if not P(a,0,1) and not P(a,0,2): bad += 1
print("   3-vertex configs with two P-empty out-arcs at a vertex:", bad, "(must be 0)")
bad = 0
for d in (0,1):
    a=[[False]*3 for _ in range(3)]
    a[1][0]=True; a[2][0]=True
    if d: a[1][2]=True
    else: a[2][1]=True
    if not P(a,1,0) and not P(a,2,0): bad += 1
print("   3-vertex configs with two P-empty in-arcs at a vertex:", bad, "(must be 0)")

# ---------- C. Corollary 4's finite shadow, exhaustive for n<=6, random for larger ----------
def Jk(a, k=3):
    """undirected graph of arcs lying in >= k directed triangles"""
    n=len(a); E=[]
    for i in range(n):
        for j in range(n):
            if a[i][j] and len(Z(a,i,j))>=k: E.append((i,j))
    return E

def maxdeg(n, E):
    d=[0]*n
    for u,v in E: d[u]+=1; d[v]+=1
    return max(d) if n else 0

print("\n== Corollary 4 finite shadow: in every T*-free tournament, the arcs lying in")
print("   >= 3 directed triangles form a graph of max degree <= 2 ==")
for n in range(4,7):
    pairs=list(combinations(range(n),2))
    m=len(pairs); tot=0; free=0; worst=0; worstP=0
    for code in range(1<<m):
        a=[[False]*n for _ in range(n)]
        for b,(i,j) in enumerate(pairs):
            if code>>b & 1: a[i][j]=True
            else: a[j][i]=True
        tot+=1
        if contains_tstar(a): continue
        free+=1
        E=Jk(a,3)
        worst=max(worst, maxdeg(n,E))
        # also check Lemma 2's consequence directly
        for (i,j) in E:
            if P(a,i,j): worstP=1
    print(f"   n={n}: {tot} labelled tournaments, {free} T*-free; max degree of the >=3-triangle graph = {worst}; any such arc with P nonempty? {bool(worstP)}")

print("\n   n=7 exhaustive:")
n=7; pairs=list(combinations(range(n),2)); m=len(pairs)
# fast T*-freeness via 5-subset lookup
T5=set()
for p in permutations(range(5)):
    code=0
    for b,(i,j) in enumerate(combinations(range(5),2)):
        if adj_T[p[i]][p[j]]: code |= 1<<b
    T5.add(code)
pidx={pr:b for b,pr in enumerate(pairs)}
subs=[]
for S in combinations(range(n),5):
    mapping=[]
    for b,(i,j) in enumerate(combinations(range(5),2)):
        mapping.append((pidx[(S[i],S[j])], b))
    subs.append(mapping)
free=0; worst=0; anyP=False
for code in range(1<<m):
    ok=True
    for mapping in subs:
        sc=0
        for src,dst in mapping:
            if code>>src & 1: sc |= 1<<dst
        if sc in T5: ok=False; break
    if not ok: continue
    free+=1
    a=[[False]*n for _ in range(n)]
    for b,(i,j) in enumerate(pairs):
        if code>>b & 1: a[i][j]=True
        else: a[j][i]=True
    E=Jk(a,3)
    worst=max(worst,maxdeg(n,E))
    for (i,j) in E:
        if P(a,i,j): anyP=True
print(f"   n=7: {1<<m} labelled tournaments, {free} T*-free; max degree of the >=3-triangle graph = {worst}; any such arc with P nonempty? {anyP}")

# random larger
print("\n   random search, larger n (T*-free tournaments found by local search):")
random.seed(7)
def rand_tstar_free(n, tries=200000):
    a=[[False]*n for _ in range(n)]
    for i,j in combinations(range(n),2):
        if random.random()<0.5: a[i][j]=True
        else: a[j][i]=True
    # local repair: while contains T*, reverse a random arc of a found copy
    for _ in range(tries):
        found=None
        for S in combinations(range(n),5):
            if iso(induced(a,S), adj_T): found=S; break
        if found is None: return a
        i,j=random.sample(list(found),2)
        a[i][j],a[j][i]=a[j][i],a[i][j]
    return None
for n in (8,9,10,12):
    okall=True; got=0
    for t in range(6):
        a=rand_tstar_free(n, 4000)
        if a is None: continue
        got+=1
        E=Jk(a,3)
        if maxdeg(n,E)>2: okall=False
        for (i,j) in E:
            if P(a,i,j): okall=False
    print(f"   n={n}: {got} T*-free tournaments produced, all satisfy the degree<=2 / P-empty conclusions: {okall}")

# ---------- D. Section 4 Case 2 ----------
print("\n== Case 2: a transitive tournament with one arc reversed is T*-free ==")
for n in range(5,10):
    L=transitive_tournament(n)
    bad=[]
    for i,j in combinations(range(n),2):
        S=reverse_arc(L,i,j)
        if contains_tstar(S): bad.append((i,j))
    print(f"   TT_{n}: reversing each of the {n*(n-1)//2} arcs -> copies of T* created in {len(bad)} cases (must be 0)")
