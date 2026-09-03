#!/usr/bin/env python3
"""
Independent verification of the writeup for catalog id 1811.12650__00.

Writeup claim (Theorem): for every connected graph G != K_{Delta+1},
    |Frozen(G)| / |Omega_{Delta+1}(G)| <= 4/(n+4).

We verify, by brute force on families of graphs that actually possess frozen
colourings (cycles C_n with q=3; all connected 2-lifts of K_4 with q=4, n=8;
all connected 2-lifts of K_5 with q=5, n=10; 3-lifts of K_3 i.e. C_9):

  A. the setup facts of Section 2 (frozen => Delta-regular, rainbow closed nbhds);
  B. Lemma 1: sigma^{xy} is proper, and frozen iff N[x]=N[y];
  C. Lemma 2: every tau has at most 2 preimages under Phi;
  D. inequality (2): 2|E_circ| >= n for connected non-complete G with Frozen != 0;
  E. the final bound F/C <= 4/(n+4);
  F. Section 6's appeal to Feghali-Johnson-Paulusma: for Delta >= 3 examples the
     non-frozen colourings form ONE component of the recolouring graph, while for
     Delta = 2 (cycles) they do NOT (FJP needs Delta >= 3) -- exposing the missing
     hypothesis in Section 6 of the writeup.

Pure Python (no external deps).
"""
import itertools
from collections import defaultdict

# ---------- basic machinery ----------

def neighbours(n, edges):
    N = [set() for _ in range(n)]
    for u, v in edges:
        N[u].add(v); N[v].add(u)
    return N

def is_connected(n, N):
    seen = {0}; stack = [0]
    while stack:
        u = stack.pop()
        for w in N[u]:
            if w not in seen:
                seen.add(w); stack.append(w)
    return len(seen) == n

def proper_colourings(n, N, q):
    """Backtracking enumeration of proper q-colourings (as tuples)."""
    out = []
    col = [-1] * n
    def bt(i):
        if i == n:
            out.append(tuple(col)); return
        used = {col[w] for w in N[i] if w < i}
        for c in range(q):
            if c not in used:
                col[i] = c
                bt(i + 1)
        col[i] = -1
    bt(0)
    return out

def is_frozen(col, n, N, q):
    """No vertex can be recoloured: every colour != col[v] appears in N(v)."""
    for v in range(n):
        seen = {col[w] for w in N[v]}
        for c in range(q):
            if c != col[v] and c not in seen:
                return False
    return True

def closed_nb(v, N):
    return N[v] | {v}

# ---------- graph families ----------

def cycle(n):
    return n, [(i, (i + 1) % n) for i in range(n)]

def lift_of_complete(k, m, matchings):
    """m-lift of K_k. Vertices (u,i) -> u*m+i. matchings: dict keyed by
    (u,v) with u<v, value = a permutation p of range(m); edge (u,i)-(v,p[i])."""
    n = k * m
    edges = []
    for (u, v), p in matchings.items():
        for i in range(m):
            edges.append((u * m + i, v * m + p[i]))
    return n, edges

def all_2lifts(k):
    """All 2-lifts of K_k: each edge gets identity (0,1) or swap (1,0)."""
    ekeys = [(u, v) for u in range(k) for v in range(u + 1, k)]
    perms = [(0, 1), (1, 0)]
    for choice in itertools.product(range(2), repeat=len(ekeys)):
        matchings = {e: perms[c] for e, c in zip(ekeys, choice)}
        yield lift_of_complete(k, 2, matchings)

def all_3lifts_K3():
    ekeys = [(0, 1), (0, 2), (1, 2)]
    perms = list(itertools.permutations(range(3)))
    for choice in itertools.product(range(6), repeat=3):
        matchings = {e: perms[c] for e, c in zip(ekeys, choice)}
        yield lift_of_complete(3, 3, matchings)

# ---------- the checks ----------

def check_graph(name, n, edges, q, build_recol_graph=False):
    N = neighbours(n, edges)
    Delta = max(len(N[v]) for v in range(n))
    assert q == Delta + 1, (name, q, Delta)
    conn = is_connected(n, N)
    complete = all(len(N[v]) == n - 1 for v in range(n))
    Omega = proper_colourings(n, N, q)
    C = len(Omega)
    frozen = [c for c in Omega if is_frozen(c, n, N, q)]
    F = len(frozen)
    report = dict(name=name, n=n, Delta=Delta, q=q, connected=conn,
                  complete=complete, C=C, F=F)
    if not conn or complete:
        return report  # outside the theorem's hypotheses

    # --- A. Section 2 facts
    for col in frozen:
        assert all(len(N[v]) == Delta for v in range(n)), "frozen but not regular"
        for v in range(n):
            cols = sorted(col[w] for w in closed_nb(v, N))
            assert cols == list(range(q)), "closed nbhd not rainbow"

    # true-twin edges / E_circ
    E = [(u, v) for u in range(n) for v in N[u] if u < v]
    Ecirc = [(u, v) for (u, v) in E if closed_nb(u, N) != closed_nb(v, N)]
    report["E"] = len(E); report["Ecirc"] = len(Ecirc)

    # --- D. inequality (2)
    if F > 0:
        assert 2 * len(Ecirc) >= n, f"{name}: 2|Ecirc| < n"

    # --- B, C. Lemma 1 and Lemma 2
    frozen_set = set(frozen)
    preimages = defaultdict(int)
    def edge_check(col):
        for (u, v) in E:
            new = list(col); new[u], new[v] = col[v], col[u]
            new = tuple(new)
            # properness
            for a in range(n):
                for b in N[a]:
                    assert new[a] != new[b], f"{name}: switched colouring improper"
            fz = is_frozen(new, n, N, q)
            twin = closed_nb(u, N) == closed_nb(v, N)
            assert fz == twin, f"{name}: Lemma 1 frozen-iff-twin fails on {(u,v)}"
            if (u, v) in set(Ecirc):
                assert not fz
                preimages[new] += 1
    for col in frozen:
        edge_check(col)
    maxpre = max(preimages.values()) if preimages else 0
    report["max_preimages"] = maxpre
    assert maxpre <= 2, f"{name}: Lemma 2 fails, {maxpre} preimages"
    # double count identity: F*|Ecirc| = sum of preimage counts <= 2*(C-F)
    total = sum(preimages.values())
    assert total == F * len(Ecirc)
    assert total <= 2 * (C - F), f"{name}: inequality (1) fails"

    # --- E. final bound
    if C > 0:
        ratio = F / C
        bound = 4 / (n + 4)
        assert ratio <= bound + 1e-12, f"{name}: F/C={ratio} > 4/(n+4)={bound}"
        report["ratio"] = ratio; report["bound"] = bound

    # --- F. component structure of the recolouring graph (Section 6 / FJP)
    if build_recol_graph:
        idx = {c: i for i, c in enumerate(Omega)}
        parent = list(range(C))
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]; x = parent[x]
            return x
        def union(a, b):
            ra, rb = find(a), find(b)
            if ra != rb: parent[ra] = rb
        for col in Omega:
            for v in range(n):
                seen = {col[w] for w in N[v]}
                for c in range(q):
                    if c != col[v] and c not in seen:
                        new = list(col); new[v] = c
                        union(idx[col], idx[tuple(new)])
        comps = defaultdict(list)
        for c in Omega:
            comps[find(idx[c])].append(c)
        nonfrozen_comp_sizes = sorted(
            (len(v) for v in comps.values() if len(v) > 1), reverse=True)
        iso = sum(1 for v in comps.values() if len(v) == 1)
        report["nontrivial_components"] = nonfrozen_comp_sizes
        report["isolated"] = iso
        assert iso == F, f"{name}: isolated vertices != frozen count"
    return report


def main():
    results = []

    # cycles, q = 3 (Delta = 2)
    for n in range(4, 13):
        nn, e = cycle(n)
        results.append(check_graph(f"C_{n}", nn, e, 3,
                                   build_recol_graph=(n <= 9)))

    # all 2-lifts of K_4 (n=8, q=4); the connected ones have frozen colourings
    seen = 0
    for i, (nn, e) in enumerate(all_2lifts(4)):
        r = check_graph(f"2lift_K4_#{i}", nn, e, 4, build_recol_graph=True)
        results.append(r); seen += 1

    # all 3-lifts of K_3 (n=9, q=3)
    for i, (nn, e) in enumerate(all_3lifts_K3()):
        r = check_graph(f"3lift_K3_#{i}", nn, e, 3, build_recol_graph=False)
        results.append(r)

    # all 2-lifts of K_5 (n=10, q=5): heavier, no recolouring graph
    for i, (nn, e) in enumerate(all_2lifts(5)):
        r = check_graph(f"2lift_K5_#{i}", nn, e, 5, build_recol_graph=False)
        results.append(r)

    # ---- summarize ----
    interesting = [r for r in results if r.get("F", 0) > 0
                   and r.get("connected") and not r.get("complete")]
    print(f"graphs tested: {len(results)}")
    print(f"connected, non-complete graphs WITH frozen colourings: "
          f"{len(interesting)}")
    worst = max(interesting, key=lambda r: r["ratio"])
    print("worst ratio F/C among them: "
          f"{worst['ratio']:.6f} <= bound {worst['bound']:.6f}  ({worst['name']}: "
          f"n={worst['n']}, Delta={worst['Delta']}, F={worst['F']}, C={worst['C']})")
    mp = max(r.get("max_preimages", 0) for r in interesting)
    print(f"max preimage multiplicity observed (Lemma 2 says <=2): {mp}")

    # samples
    for nm in ["C_6", "C_9", "C_12"]:
        for r in results:
            if r["name"] == nm:
                print(f"{nm}: F={r['F']}, C={r['C']}, "
                      f"ratio={r.get('ratio', 0):.5f}, "
                      f"Ecirc={r.get('Ecirc')}, "
                      f"nontrivial comps={r.get('nontrivial_components')}, "
                      f"isolated={r.get('isolated')}")

    # component structure summary for Delta>=3 examples with frozen colourings
    bad_fjp = []
    for r in results:
        if r.get("nontrivial_components") is None:
            continue
        k = len(r["nontrivial_components"])
        if r.get("connected") and not r.get("complete"):
            if r["Delta"] >= 3 and k > 1:
                bad_fjp.append(r["name"])
    print(f"Delta>=3 connected noncomplete examples whose NONFROZEN colourings "
          f"split into >1 component (should be none by FJP): {bad_fjp}")

    cyc_multi = [r["name"] for r in results
                 if r.get("nontrivial_components") is not None
                 and r["Delta"] == 2 and len(r["nontrivial_components"]) > 1]
    print(f"Delta=2 cycles whose nonfrozen colourings split into >1 component "
          f"(FJP hypothesis Delta>=3 is real): {cyc_multi}")

    print("ALL ASSERTIONS PASSED")


if __name__ == "__main__":
    main()
