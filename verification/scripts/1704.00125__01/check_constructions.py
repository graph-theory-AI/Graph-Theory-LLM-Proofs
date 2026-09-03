"""Verify the writeup's finite constructions by brute force. Self-contained.

A) The Lemma's random 20-matching bipartite graph, for m = 24 (N = 48):
   exhaustively check that NO partition V = A|B|X with |X| <= m/6 = 4,
   2m/3 = 16 <= |A| <= 32 = 4m/3 and no A-B edge exists.
   (Key fact: any such A must be a union of components of G - X, so we
   enumerate all X with |X| <= 4 and do a subset-sum over component sizes.)
B) Konig / Gallai: alpha(G) = n - max_matching on random bipartite graphs,
   vs brute-force maximum independent set.
C) K_{m,m}: every balanced separator (components <= 2N/3) has >= N/3 vertices.
D) Expansion lower-bound gadget G_r (r = 1,2,3): max degree <= 3, bipartite,
   tree branch sets of radius <= r, contraction gives K_{q,q} with q = 2^r.
"""
import random
import sys
from itertools import combinations

sys.setrecursionlimit(100000)
random.seed(20250902)
ok = True


def check(name, cond):
    global ok
    print(f"  [{'PASS' if cond else 'FAIL'}] {name}")
    ok = ok and cond


# ---------- helpers ----------
def components(n, adj, removed):
    """Connected components of graph on [0,n) minus 'removed' (a set)."""
    seen = [False] * n
    comps = []
    for s in range(n):
        if seen[s] or s in removed:
            continue
        stack, comp = [s], []
        seen[s] = True
        while stack:
            u = stack.pop()
            comp.append(u)
            for w in adj[u]:
                if not seen[w] and w not in removed:
                    seen[w] = True
                    stack.append(w)
        comps.append(comp)
    return comps


def max_matching_bipartite(m, nbrs):
    """Hungarian augmenting-path matching. nbrs[l] = list of right-neighbors."""
    match_r = [-1] * m

    def try_kuhn(l, vis):
        for r in nbrs[l]:
            if not vis[r]:
                vis[r] = True
                if match_r[r] == -1 or try_kuhn(match_r[r], vis):
                    match_r[r] = l
                    return True
        return False

    size = 0
    for l in range(m):
        if try_kuhn(l, [False] * m):
            size += 1
    return size


def brute_alpha(n, adjmask):
    best = 0
    for S in range(1 << n):
        okS = True
        s = S
        while s:
            v = (s & -s).bit_length() - 1
            if adjmask[v] & S:
                okS = False
                break
            s &= s - 1
        if okS:
            best = max(best, bin(S).count("1"))
    return best


# ---------- A) Lemma instance, m = 24, d = 20 ----------
print("A) Lemma graph: m=24, union of 20 random perfect matchings")
m, d = 24, 20
n = 2 * m  # vertices 0..m-1 = L, m..2m-1 = R
edges = set()
for _ in range(d):
    perm = list(range(m))
    random.shuffle(perm)
    for l in range(m):
        edges.add((l, m + perm[l]))
adj = [[] for _ in range(n)]
for a, b in edges:
    adj[a].append(b)
    adj[b].append(a)
deg = [len(a) for a in adj]
check(f"bipartite by construction; max degree = {max(deg)} <= 20", max(deg) <= 20)

lo, hi, xmax = 2 * m // 3, 4 * m // 3, m // 6  # 16, 32, 4
print(f"   forbidden partition: |X| <= {xmax}, {lo} <= |A| <= {hi}, no A-B edge")


def has_forbidden_A(comp_sizes, total_rest):
    """Is there a sub-collection of components with total size in [lo, hi],
    whose complement (B) may be empty or not (lemma allows any B)?"""
    reachable = 1  # bitset over sums
    for c in comp_sizes:
        reachable |= reachable << c
    for s in range(lo, hi + 1):
        if (reachable >> s) & 1:
            return True
    return False


found = None
count_X = 0
verts = list(range(n))
for xsize in range(0, xmax + 1):
    for X in combinations(verts, xsize):
        count_X += 1
        Xs = set(X)
        comps = components(n, adj, Xs)
        sizes = [len(c) for c in comps]
        if has_forbidden_A(sizes, n - xsize):
            found = (X, sizes)
            break
    if found:
        break
print(f"   examined {count_X} separator candidates X")
check("no forbidden partition exists (lemma instance verified exhaustively)",
      found is None)
if found:
    print("   COUNTEREXAMPLE:", found)
check("hence every balanced separator of this graph has size > N/12 = 4",
      found is None)

# ---------- B) Konig / Gallai ----------
print("B) alpha(G) = n - max_matching on bipartite graphs (Konig + Gallai)")
good = True
for trial in range(200):
    mm = random.randint(1, 6)
    nbrs = [[] for _ in range(mm)]
    adjmask = [0] * (2 * mm)
    for l in range(mm):
        for r in range(mm):
            if random.random() < 0.4:
                nbrs[l].append(r)
                adjmask[l] |= 1 << (mm + r)
                adjmask[mm + r] |= 1 << l
    nu = max_matching_bipartite(mm, nbrs)
    alpha = brute_alpha(2 * mm, adjmask)
    if alpha != 2 * mm - nu:
        good = False
        print("   mismatch:", mm, nu, alpha)
check("alpha = n - nu on 200 random bipartite graphs (brute force)", good)

# ---------- C) K_{m,m} separators ----------
print("C) K_{m,m}: every X leaving all components <= 2N/3 has |X| >= N/3")
good = True
for mm in [2, 3, 4]:
    N = 2 * mm
    adjK = [[] for _ in range(N)]
    for l in range(mm):
        for r in range(mm):
            adjK[l].append(mm + r)
            adjK[mm + r].append(l)
    best = N
    for xsize in range(N + 1):
        done = False
        for X in combinations(range(N), xsize):
            comps = components(N, adjK, set(X))
            if all(len(c) <= 2 * N / 3 for c in comps):
                best = min(best, xsize)
                done = True
                break
        if done:
            break
    if best < N / 3:
        good = False
    print(f"   m={mm}: min balanced separator = {best}, N/3 = {N/3:.2f}")
check("min balanced separator of K_{m,m} >= N/3 for m=2,3,4", good)

# ---------- D) Expansion gadget ----------
print("D) Expansion gadget G_r for r=1,2,3")
for r in [1, 2, 3]:
    q = 2 ** r
    # K_{q,q} vertices: ('L',i), ('R',j); build binary tree per vertex
    node_id = {}
    adjG = []

    def nid(x):
        if x not in node_id:
            node_id[x] = len(adjG)
            adjG.append([])
        return node_id[x]

    def add_edge(x, y):
        a, b = nid(x), nid(y)
        adjG[a].append(b)
        adjG[b].append(a)

    hosts = [('L', i) for i in range(q)] + [('R', j) for j in range(q)]
    for v in hosts:
        # binary tree nodes (v, depth, index)
        for depth in range(r):
            for idx in range(2 ** depth):
                add_edge((v, depth, idx), (v, depth + 1, 2 * idx))
                add_edge((v, depth, idx), (v, depth + 1, 2 * idx + 1))
    # leaves (v, r, 0..q-1); edge (Li,Rj) of K_qq assigned to leaf j of Li
    # and leaf i of Rj  -> bijective per vertex
    for i in range(q):
        for j in range(q):
            add_edge((('L', i), r, j), (('R', j), r, i))
    nG = len(adjG)
    maxdeg = max(len(a) for a in adjG)
    # bipartiteness by BFS 2-coloring
    color = [-1] * nG
    bip = True
    for s in range(nG):
        if color[s] == -1:
            color[s] = 0
            stack = [s]
            while stack:
                u = stack.pop()
                for w in adjG[u]:
                    if color[w] == -1:
                        color[w] = 1 - color[u]
                        stack.append(w)
                    elif color[w] == color[u]:
                        bip = False
    # branch set radius: eccentricity of root within its tree = r by construction
    # verify contraction gives K_{q,q}: for every (i,j) there must be an edge
    # between tree of Li and tree of Rj; trees are disjoint & connected by constr.
    branch = {}
    for x, ident in node_id.items():
        v = x if x in hosts else x[0]
        # roots are (v,0,0); represent host v by its tree node set
        branch.setdefault(v if x in hosts else x[0], set()).add(ident)
    # note: hosts themselves are not graph nodes; only tuples (v,depth,idx) are
    branch = {}
    for x, ident in node_id.items():
        branch.setdefault(x[0], set()).add(ident)
    pairs_ok = True
    for i in range(q):
        for j in range(q):
            ti, tj = branch[('L', i)], branch[('R', j)]
            if not any(w in tj for u in ti for w in adjG[u]):
                pairs_ok = False
    # radius of each branch set from root
    def ecc_from_root(v):
        root = node_id[(v, 0, 0)]
        members = branch[v]
        dist = {root: 0}
        stack = [root]
        while stack:
            u = stack.pop(0)
            for w in adjG[u]:
                if w in members and w not in dist:
                    dist[w] = dist[u] + 1
                    stack.append(w)
        return max(dist.values()), len(dist) == len(members)

    radii = [ecc_from_root(v) for v in hosts]
    conn = all(c for _, c in radii)
    maxrad = max(rr for rr, _ in radii)
    dens = q * q / (2 * q)
    print(f"   r={r}: |V|={nG}, maxdeg={maxdeg}, bipartite={bip}, "
          f"branch sets connected={conn}, max radius={maxrad}, "
          f"K_qq minor complete={pairs_ok}, density q/2={dens} vs 2^(r-1)={2**(r-1)}")
    check(f"r={r} gadget valid",
          maxdeg <= 3 and bip and conn and maxrad <= r and pairs_ok
          and dens == 2 ** (r - 1))

print("\nALL PASS" if ok else "\nSOME CHECKS FAILED")
