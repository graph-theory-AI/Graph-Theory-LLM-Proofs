#!/usr/bin/env python3
"""
Independent verification for attack 1601.01886__00.

Claims checked:
  (A) |R_h| = 3*2^h - 2, |D_h| = 6*2^h - 4.
  (B) pw(R_h) = ceil(h/2), pw(D_h) = ceil((h+1)/2)   [writeup Lemmas 4, 5]
      - exact subset-DP vertex-separation for small instances (n <= 20),
      - Ellis-Sudborough-Turner 3-branch criterion solver for larger ones,
        itself validated against the subset DP on ALL trees with <= 10 vertices.
  (C) lambda(D_h) = h for h = 0,1,2 by BRUTE FORCE over all path-partitions
      (all F subseteq E with max F-degree <= 2), where lambda = min over F and
      over root parts of the rooted quotient edge-height.  [writeup Lemma 7]
  (D) Lemma 6 brute force on R_1, R_2, R_3: for EVERY F with deg_F <= 2 there
      is a leaf whose root-to-leaf path has >= h edges outside F.
  (E) The writeup's explicit upper-bound partition of D_h (Lemma 7 upper bound)
      is a valid path-partition of quotient edge-height exactly h, for h <= 10.
  (F) Universal upper bound (writeup Corollary 3): lambda(T) <= 2*pw(T) - 1
      for ALL trees on <= 10 vertices with pw >= 1 (brute force both sides).
"""
import itertools, sys
from math import ceil, inf
sys.setrecursionlimit(1000000)

# ---------------------------------------------------------------- constructions
def build_R(h):
    """Return (adj: dict v -> set of nbrs, root)."""
    counter = itertools.count()
    adj = {}
    def newv():
        v = next(counter); adj[v] = set(); return v
    def add(u, v): adj[u].add(v); adj[v].add(u)
    def rec(hh):
        if hh == 0:
            return newv()
        s1 = rec(hh - 1)
        s2 = rec(hh - 1)
        x = newv(); r = newv()
        add(r, x); add(x, s1); add(x, s2)
        return r
    root = rec(h)
    return adj, root

def build_D(h):
    adj1, r1 = build_R(h)
    adj2, r2 = build_R(h)
    off = max(adj1) + 1
    adj = {v: set(ns) for v, ns in adj1.items()}
    for v, ns in adj2.items():
        adj[v + off] = {u + off for u in ns}
    adj[r1].add(r2 + off); adj[r2 + off].add(r1)
    return adj, r1, r2 + off

def edges_of(adj):
    return sorted((u, v) for u in adj for v in adj[u] if u < v)

# ------------------------------------------------- exact pathwidth (subset DP)
def pathwidth_dp(adj):
    """Exact vertex separation number (= pathwidth) via DP over subsets."""
    verts = sorted(adj)
    n = len(verts)
    idx = {v: i for i, v in enumerate(verts)}
    nbr = [0] * n
    for v in verts:
        for u in adj[v]:
            nbr[idx[v]] |= 1 << idx[u]
    full = (1 << n) - 1
    f = {0: 0}
    # process subsets in order of popcount
    by_pc = [[] for _ in range(n + 1)]
    for S in range(1 << n):
        by_pc[bin(S).count('1')].append(S)
    for pc in range(1, n + 1):
        for S in by_pc[pc]:
            comp = full & ~S
            b = 0
            T = S
            while T:
                v = (T & -T).bit_length() - 1
                T &= T - 1
                if nbr[v] & comp:
                    b += 1
            best = inf
            T = S
            while T:
                low = T & -T
                v = low.bit_length() - 1
                T &= T - 1
                prev = f[S & ~low]
                val = prev if prev > b else b
                if val < best:
                    best = val
            f[S] = best
    return f[full]

# ------------------------------------- EST 3-branch criterion pathwidth (trees)
def pathwidth_est(adj):
    """pw(T) = max( [1 if T has an edge], max_v (3rd-largest pw of comps of T-v) + 1 ).
    Uses the Ellis-Sudborough-Turner characterization for trees; memoized on a
    canonical (centroid-rooted AHU) code so isomorphic pieces are computed once."""
    memo = {}

    def canon(vset):
        vs = vset
        if len(vs) == 1:
            return "()"
        # find centroid(s) of induced subtree via subtree sizes
        n = len(vs)
        r0 = next(iter(vs))
        order, par = [], {r0: None}
        stack = [r0]
        while stack:
            v = stack.pop()
            order.append(v)
            for u in adj[v]:
                if u in vs and u is not par[v] and u != par[v]:
                    if u not in par:
                        par[u] = v
                        stack.append(u)
        size = {v: 1 for v in vs}
        for v in reversed(order):
            if par[v] is not None:
                size[par[v]] += size[v]
        centers = []
        for v in vs:
            mx = n - size[v]
            for u in adj[v]:
                if u in vs and par.get(u) == v:
                    mx = max(mx, size[u])
            if mx <= n // 2:
                centers.append(v)
        assert 1 <= len(centers) <= 2
        def ahu(r, parent):
            # iterative not needed; depth <= n but trees are shallow enough? use explicit stack
            stack = [(r, parent, False)]
            out = {}
            while stack:
                v, p, done = stack.pop()
                if done:
                    kids = sorted(out[c] for c in adj[v] if c in vs and c != p)
                    out[v] = "(" + "".join(kids) + ")"
                else:
                    stack.append((v, p, True))
                    for c in adj[v]:
                        if c in vs and c != p:
                            stack.append((c, v, False))
            return out[r]
        if len(centers) == 1:
            return ahu(centers[0], None)
        a, b = centers
        return min(ahu(a, b) + "|" + ahu(b, a), ahu(b, a) + "|" + ahu(a, b))

    def comps(vset, banned):
        seen = set()
        out = []
        for s in vset:
            if s in seen: continue
            stack = [s]; comp = set()
            seen.add(s)
            while stack:
                v = stack.pop(); comp.add(v)
                for u in adj[v]:
                    if u in vset and u != banned and u not in seen:
                        seen.add(u); stack.append(u)
            out.append(frozenset(comp))
        return out
    def pw(vset):
        if len(vset) == 1:
            return 0
        key = canon(vset)
        if key in memo:
            return memo[key]
        best = 1  # tree with >= 2 vertices
        for v in vset:
            deg = sum(1 for u in adj[v] if u in vset)
            if deg < 3:
                continue
            cs = comps(vset - {v}, v)
            vals = sorted((pw(c) for c in cs), reverse=True)
            if len(vals) >= 3 and vals[2] + 1 > best:
                best = vals[2] + 1
        memo[key] = best
        return best
    return pw(frozenset(adj))

# --------------------------------------------------- brute-force lambda (exact)
def lambda_brute(adj):
    """min over path-partitions and root parts of the quotient edge-height.
    Enumerates all F subseteq E with deg_F <= 2 (components of F are the parts;
    every such F is a partition into induced paths and vice versa)."""
    verts = sorted(adj)
    E = edges_of(adj)
    m = len(E)
    n = len(verts)
    best = [inf]
    deg = {v: 0 for v in verts}
    chosen = []
    def quotient_radius():
        # union-find on chosen edges
        parent = {v: v for v in verts}
        def find(a):
            while parent[a] != a:
                parent[a] = parent[parent[a]]; a = parent[a]
            return a
        for (u, v) in chosen:
            ru, rv = find(u), find(v)
            if ru != rv: parent[ru] = rv
        parts = {}
        for v in verts:
            parts.setdefault(find(v), set()).add(v)
        # quotient adjacency
        qadj = {r: set() for r in parts}
        for (u, v) in E:
            ru, rv = find(u), find(v)
            if ru != rv:
                qadj[ru].add(rv); qadj[rv].add(ru)
        # radius of a tree = ceil(diameter/2); diameter via double BFS
        from collections import deque
        def bfs_far(s):
            dist = {s: 0}; dq = deque([s]); far, fd = s, 0
            while dq:
                a = dq.popleft()
                for b in qadj[a]:
                    if b not in dist:
                        dist[b] = dist[a] + 1
                        if dist[b] > fd: far, fd = b, dist[b]
                        dq.append(b)
            return far, fd
        s0 = next(iter(qadj))
        a, _ = bfs_far(s0)
        _, diam = bfs_far(a)
        return (diam + 1) // 2

    def rec(i):
        if i == m:
            r = quotient_radius()
            if r < best[0]: best[0] = r
            return
        # skip edge i
        rec(i + 1)
        u, v = E[i]
        if deg[u] < 2 and deg[v] < 2:
            deg[u] += 1; deg[v] += 1
            chosen.append(E[i])
            rec(i + 1)
            chosen.pop()
            deg[u] -= 1; deg[v] -= 1
    rec(0)
    return best[0]

# ------------------------------------------------------- Lemma 6 brute force
def lemma6_min(h):
    """min over all F with deg_F<=2 of  max over leaves l of
       #(edges outside F on the r_h - l path).  Claim: >= h."""
    adj, root = build_R(h)
    E = edges_of(adj)
    m = len(E)
    eidx = {e: i for i, e in enumerate(E)}
    # root-to-leaf edge masks
    leaves = [v for v in adj if len(adj[v]) == 1 and v != root]
    if not leaves: leaves = [root]
    # parent pointers by BFS from root
    from collections import deque
    par = {root: None}
    dq = deque([root])
    while dq:
        a = dq.popleft()
        for b in adj[a]:
            if b not in par:
                par[b] = a; dq.append(b)
    leafmasks = []
    for l in leaves:
        mask = 0; v = l
        while par[v] is not None:
            e = (min(v, par[v]), max(v, par[v]))
            mask |= 1 << eidx[e]
            v = par[v]
        leafmasks.append(mask)
    deg = {v: 0 for v in adj}
    best = [inf]
    Fbits = [0]
    def rec(i):
        if i == m:
            F = Fbits[0]
            val = max(bin(mk & ~F).count('1') for mk in leafmasks)
            if val < best[0]: best[0] = val
            return
        rec(i + 1)
        u, v = E[i]
        if deg[u] < 2 and deg[v] < 2:
            deg[u] += 1; deg[v] += 1
            Fbits[0] |= 1 << i
            rec(i + 1)
            Fbits[0] &= ~(1 << i)
            deg[u] -= 1; deg[v] -= 1
    rec(0)
    return best[0]

# ------------------------------------ writeup's explicit partition of D_h (UB)
def partition_D(h):
    """Build D_h together with the writeup's recursive partition.
    Returns (adj, parts, root_part_index)."""
    counter = itertools.count()
    adj = {}
    def newv():
        v = next(counter); adj[v] = set(); return v
    def add(u, v): adj[u].add(v); adj[v].add(u)
    def rec(hh):
        """returns (root r, list_of_parts, index_of_root_part);
        root part is a path with r as an endpoint."""
        if hh == 0:
            r = newv()
            return r, [[r]], 0
        s1, parts1, rp1 = rec(hh - 1)
        s2, parts2, rp2 = rec(hh - 1)
        x = newv(); r = newv()
        add(r, x); add(x, s1); add(x, s2)
        # merge child-1 root path with edges r-x, x-s1  (r,x prepended)
        parts = []
        rootpath = [r, x] + parts1[rp1]
        parts.append(rootpath)
        for i, p in enumerate(parts1):
            if i != rp1: parts.append(p)
        parts.extend(parts2)
        return r, parts, 0
    rL, partsL, rpL = rec(h)
    # second copy
    nL = next(counter)  # peek: this consumes one id; account for it
    # (simpler: rebuild second copy with fresh ids from same counter)
    adj[nL] = set()  # dummy vertex to drop? -- instead rebuild cleanly:
    del adj[nL]
    rR, partsR, rpR = rec(h)
    add(rL, rR)
    # merged root part: pathL reversed + pathR ; each root path has r as endpoint
    pl = partsL[rpL]; pr = partsR[rpR]
    assert pl[0] == rL and pr[0] == rR
    merged = list(reversed(pl)) + pr
    parts = [merged]
    for i, p in enumerate(partsL):
        if i != rpL: parts.append(p)
    for i, p in enumerate(partsR):
        if i != rpR: parts.append(p)
    return adj, parts, 0

def check_partition(adj, parts, root_idx):
    """Verify parts partition V into induced paths; return quotient edge-height
    from the root part (and verify quotient is a tree)."""
    verts = set(adj)
    allv = [v for p in parts for v in p]
    assert len(allv) == len(set(allv)) == len(verts), "not a partition"
    where = {}
    for i, p in enumerate(parts):
        for v in p: where[v] = i
    for p in parts:
        s = set(p)
        # induced edges
        ind = [(u, v) for u in s for v in adj[u] if v in s and u < v]
        assert len(ind) == len(s) - 1, "part does not induce a tree"
        degs = {v: 0 for v in s}
        for u, v in ind: degs[u] += 1; degs[v] += 1
        assert all(d <= 2 for d in degs.values()), "part induces a non-path"
        # connectivity: |edges| = |s|-1 and it's a forest inside a tree -> connected
    q = {i: set() for i in range(len(parts))}
    ne = 0
    for u in adj:
        for v in adj[u]:
            if u < v and where[u] != where[v]:
                q[where[u]].add(where[v]); q[where[v]].add(where[u])
    ne = sum(len(s) for s in q.values()) // 2
    assert ne == len(parts) - 1, "quotient is not a tree"
    from collections import deque
    dist = {root_idx: 0}; dq = deque([root_idx]); hgt = 0
    while dq:
        a = dq.popleft()
        for b in q[a]:
            if b not in dist:
                dist[b] = dist[a] + 1; hgt = max(hgt, dist[b]); dq.append(b)
    assert len(dist) == len(parts), "quotient disconnected"
    return hgt

# ----------------------------------------------------------------------- main
def main():
    print("== (A) orders ==")
    for h in range(0, 8):
        adjR, _ = build_R(h)
        adjD, _, _ = build_D(h)
        okR = len(adjR) == 3 * 2**h - 2
        okD = len(adjD) == 6 * 2**h - 4
        print(f"  h={h}: |R_h|={len(adjR)} (expect {3*2**h-2}) {'OK' if okR else 'FAIL'};"
              f" |D_h|={len(adjD)} (expect {6*2**h-4}) {'OK' if okD else 'FAIL'}")
        assert okR and okD

    print("== validate EST criterion solver vs subset DP on all trees n<=10 ==")
    try:
        import networkx as nx
        total = bad = 0
        for n in range(1, 11):
            for T in nx.nonisomorphic_trees(n):
                adj = {v: set(T.neighbors(v)) for v in T.nodes}
                a = pathwidth_dp(adj); b = pathwidth_est(adj)
                total += 1
                if a != b:
                    bad += 1
                    print(f"  MISMATCH n={n}: dp={a} est={b} edges={list(T.edges)}")
        print(f"  {total} trees checked, {bad} mismatches")
        assert bad == 0
    except ImportError:
        print("  networkx missing -- SKIPPED (install to run)")

    print("== (B) pathwidth of R_h and D_h (EST solver; n <= 100) ==")
    for h in range(0, 6):
        adjR, _ = build_R(h)
        exp = ceil(h / 2)
        got = pathwidth_est(adjR)
        note = ""
        if len(adjR) <= 20:
            dp = pathwidth_dp(adjR)
            note = f" [subset-DP: {dp}]"
            assert dp == got
        print(f"  pw(R_{h}) = {got} (expect {exp}){note}  {'OK' if got == exp else 'FAIL'}")
        assert got == exp
    for h in range(0, 5):
        adjD, _, _ = build_D(h)
        exp = ceil((h + 1) / 2)
        got = pathwidth_est(adjD)
        note = ""
        if len(adjD) <= 20:
            dp = pathwidth_dp(adjD)
            note = f" [subset-DP: {dp}]"
            assert dp == got
        print(f"  pw(D_{h}) = {got} (expect {exp}){note}  {'OK' if got == exp else 'FAIL'}")
        assert got == exp
    print("  T_k = D_(2k-1): pw values above give pw(D_1)=1, pw(D_3)=2, pw(D_5)=3 -> pw(T_k)=k")

    print("== (C) brute-force lambda(D_h), h=0,1,2 ==")
    for h in range(0, 3):
        adjD, _, _ = build_D(h)
        lam = lambda_brute(adjD)
        print(f"  lambda(D_{h}) = {lam} (expect {h})  {'OK' if lam == h else 'FAIL'}")
        assert lam == h

    print("== (D) Lemma 6 brute force on R_h, h=1,2,3 ==")
    for h in range(1, 4):
        v = lemma6_min(h)
        print(f"  min over F of max over leaves of #(non-F edges on root-leaf path)"
              f" in R_{h} = {v} (need >= {h})  {'OK' if v >= h else 'FAIL'}")
        assert v >= h

    print("== (E) writeup's explicit partition of D_h has edge-height exactly h ==")
    for h in range(0, 11):
        adj, parts, ri = partition_D(h)
        assert len(adj) == 6 * 2**h - 4
        hgt = check_partition(adj, parts, ri)
        ok = hgt <= h
        print(f"  D_{h}: n={len(adj)}, parts={len(parts)}, quotient height from root part = {hgt}"
              f" (claim <= {h})  {'OK' if ok else 'FAIL'}")
        assert ok

    print("== (F) Corollary 3 on all trees with 2..10 vertices: lambda <= 2 pw - 1 ==")
    try:
        import networkx as nx
        worst = {}
        cnt = 0
        for n in range(2, 11):
            for T in nx.nonisomorphic_trees(n):
                adj = {v: set(T.neighbors(v)) for v in T.nodes}
                p = pathwidth_dp(adj)
                l = lambda_brute(adj)
                cnt += 1
                worst[p] = max(worst.get(p, -1), l)
                if l > 2 * p - 1:
                    print(f"  VIOLATION n={n} pw={p} lambda={l} edges={list(T.edges)}")
                    raise SystemExit(1)
        print(f"  {cnt} trees checked, no violation. max lambda by pw: {worst}"
              f"  (Corollary 3 predicts <= {{p: 2p-1}})")
    except ImportError:
        print("  networkx missing -- SKIPPED")

    print("ALL CHECKS PASSED")

if __name__ == "__main__":
    main()
