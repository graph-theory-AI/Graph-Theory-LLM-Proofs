"""Verify all claimed properties of the 13-vertex seed graph.

F = circulant on Z_13 with connection set {+-1, +-5}; G = complement of F.
Claims: omega(F)=2 (triangle-free), alpha(F)=4, hence omega(G)=4, alpha(G)=2;
chi(G)=7; zeta(G)=4; the explicit 7-coloring and cochromatic 4-partition are valid.
Pure Python brute force (13 vertices).
"""
import itertools

n = 13
D = {1, 5, 8, 12}  # +-1, +-5 mod 13

def F_adj(x, y):
    return (x - y) % n in D

def G_adj(x, y):
    return x != y and not F_adj(x, y)

V = list(range(n))

def is_clique(adj, S):
    return all(adj(a, b) for a, b in itertools.combinations(S, 2))

def is_indep(adj, S):
    return all(not adj(a, b) for a, b in itertools.combinations(S, 2))

def clique_number(adj):
    w = 1
    for k in range(2, n + 1):
        if any(is_clique(adj, S) for S in itertools.combinations(V, k)):
            w = k
        else:
            break
    return w

def independence_number(adj):
    a = 1
    for k in range(2, n + 1):
        if any(is_indep(adj, S) for S in itertools.combinations(V, k)):
            a = k
        else:
            break
    return a

wF = clique_number(F_adj)
aF = independence_number(F_adj)
wG = clique_number(G_adj)
aG = independence_number(G_adj)
print(f"omega(F) = {wF}  (claimed 2)")
print(f"alpha(F) = {aF}  (claimed 4)")
print(f"omega(G) = {wG}  (claimed 4)")
print(f"alpha(G) = {aG}  (claimed 2)")

# chi(G): exact chromatic number by trying k-colorings (greedy DFS with pruning)
def chromatic_number(adj):
    order = V[:]
    def color_with(k):
        colors = {}
        def bt(i):
            if i == len(order):
                return True
            v = order[i]
            used = {colors[u] for u in colors if adj(u, v)}
            maxc = max(colors.values(), default=-1)
            for c in range(min(maxc + 1, k - 1) + 1):
                if c not in used:
                    colors[v] = c
                    if bt(i + 1):
                        return True
                    del colors[v]
            return False
        return bt(0)
    k = 1
    while not color_with(k):
        k += 1
    return k

chiG = chromatic_number(G_adj)
print(f"chi(G) = {chiG}  (claimed 7)")

# explicit 7-coloring
coloring = [{0,1},{2,3},{4,5},{6,7},{8,9},{10,11},{12}]
assert set().union(*coloring) == set(V) and sum(len(c) for c in coloring) == n
assert all(is_indep(G_adj, c) for c in coloring)
print("explicit 7-coloring of G: valid (all classes independent in G)")

# zeta(G): minimum partition into cliques/independent sets, brute force.
# Search: min number of homogeneous parts covering V (a cover of size t yields a
# partition of size <= t since subsets of homogeneous sets are homogeneous).
def homogeneous_sets(adj):
    """All maximal cliques and maximal independent sets, as bitmasks."""
    sets = set()
    # enumerate all cliques / independent sets up to maximality (n=13, fine)
    for k in range(1, n + 1):
        for S in itertools.combinations(V, k):
            if is_clique(adj, S) or is_indep(adj, S):
                sets.add(frozenset(S))
    # keep only maximal ones
    maximal = [s for s in sets if not any(s < t for t in sets)]
    return maximal

def zeta(adj):
    maximal = homogeneous_sets(adj)
    full = frozenset(V)
    from functools import lru_cache
    best = [n + 1]
    def bb(uncovered, used):
        if used >= best[0]:
            return
        if not uncovered:
            best[0] = used
            return
        v = min(uncovered)
        for s in maximal:
            if v in s:
                bb(uncovered - s, used + 1)
    bb(full, 0)
    return best[0]

zG = zeta(G_adj)
print(f"zeta(G) = {zG}  (claimed 4)")

# explicit cochromatic partition
A = {0,2,4,6}; B = {1,5,7,11}; C = {3,10,12}; I = {8,9}
parts = [A,B,C,I]
assert set().union(*parts) == set(V) and sum(len(p) for p in parts) == n
assert is_clique(G_adj, A) and is_clique(G_adj, B) and is_clique(G_adj, C)
assert is_indep(G_adj, I)
print("explicit partition A,B,C cliques + I independent in G: valid")
print("SEED CHECK COMPLETE")
