"""Step 1: verify the explicit five-vertex object T* = C3[TT2,TT2,1] and the
properties of it that the writeup's Section 4 (Case 2) uses."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tstar import *
from itertools import combinations, permutations

adj, V = tstar()
print("T* vertices:", V)
print("is_tournament:", is_tournament(adj))
print("arcs:", [(V[i],V[j]) for i in range(5) for j in range(5) if adj[i][j]])
print("outdegrees:", {V[i]: sum(adj[i]) for i in range(5)})
print("is_transitive:", is_transitive(adj))

tris = directed_triangles(adj)
# canonicalise as arc sets
def arcset(t):
    a,b,c = t
    return frozenset([(a,b),(b,c),(c,a)])
uniq = {arcset(t) for t in tris}
print("number of directed triangles:", len(uniq))
for s in uniq:
    print("   triangle arcs:", sorted((V[u],V[w]) for u,w in s))

# two arc-disjoint directed triangles?
found = None
for s1, s2 in combinations(uniq, 2):
    if not (s1 & s2):
        found = (s1, s2)
print("exists pair of ARC-DISJOINT directed triangles:", found is not None)
if found:
    print("   ", sorted((V[u],V[w]) for u,w in found[0]), "and", sorted((V[u],V[w]) for u,w in found[1]))

# is every directed triangle of T* forced to share one common arc?
common = set.intersection(*[set(s) for s in uniq])
print("arcs common to ALL directed triangles of T*:", [(V[u],V[w]) for u,w in common])

# inversion number iota(T*) = min over linear orders of #backward arcs
best = 99
for p in permutations(range(5)):
    pos = {v:i for i,v in enumerate(p)}
    back = sum(1 for i in range(5) for j in range(5) if adj[i][j] and pos[i] > pos[j])
    best = min(best, back)
print("inversion number iota(T*) =", best, "(>=2 means the previous attempt's Thm 2.1 does NOT cover T*)")

# modules of T*
mods = []
for k in range(2,5):
    for S in combinations(range(5),k):
        Sset = set(S)
        ok = True
        for w in range(5):
            if w in Sset: continue
            vals = {adj[w][s] for s in S}
            if len(vals) > 1: ok = False; break
        if ok: mods.append([V[s] for s in S])
print("nontrivial modules of T*:", mods, "=> prime:", len(mods)==0)

# strong connectivity / 3-vertex-strong
def strong(a):
    n=len(a)
    if n==0: return True
    seen={0}; st=[0]
    while st:
        u=st.pop()
        for v in range(n):
            if a[u][v] and v not in seen: seen.add(v); st.append(v)
    if len(seen)!=n: return False
    seen={0}; st=[0]
    while st:
        u=st.pop()
        for v in range(n):
            if a[v][u] and v not in seen: seen.add(v); st.append(v)
    return len(seen)==n
print("T* strongly connected:", strong(adj))
print("T* - {c} strongly connected:", strong(induced(adj,[0,1,2,3])))

# locally transitive?
lt = True
for v in range(5):
    O=[u for u in range(5) if adj[v][u]]; I=[u for u in range(5) if adj[u][v]]
    if not is_transitive(induced(adj,O)) or not is_transitive(induced(adj,I)): lt=False
print("T* locally transitive:", lt)
