#!/usr/bin/env python3
"""
Referee verification for 2505.24100__01.

Writeup claim: if F is a simple cubic hypohamiltonian graph on m vertices (m even),
then G = L(F) has 3m/2 vertices, no induced C_m, and G - e contains an induced C_m
for every edge e of G.  With m = 2t-2 this answers Question 1.8 (deletion half)
with |V(G)| = 3t-3 for every t such that a cubic hypohamiltonian graph on 2t-2
vertices exists (all even 2t-2 >= 26 by Goedgebeur-Zamfirescu Thm 3.6).

Checks performed here:
  A. Lemma 1 (induced C_l in L(F) <-> cycle C_l in F, l >= 4) verified
     exhaustively on random simple graphs.
  B. For F in {Petersen (m=10), flower snark J5 (m=20), flower snark J7 (m=28)}:
       1. F is simple and cubic;
       2. F is hypohamiltonian (brute-force Hamiltonian-cycle search);
       3. L(F) has 3m/2 vertices;
       4. L(F) has NO chordless cycle of length m (exhaustive chordless-cycle
          enumeration with length_bound=m);
       5. for EVERY edge e of L(F), L(F)-e has an induced C_m:
          - via the explicit witness S = E(Q) + {z} from the writeup's Lemma 2
            (the witness is checked directly: the induced subgraph of L(F)-e on S
            must be a connected 2-regular graph on m vertices), and
          - for Petersen additionally by an independent exhaustive
            chordless-cycle enumeration of L(F)-e.

Run:  uv run --with networkx python3 verify.py
"""

import itertools
import random
import sys

import networkx as nx


# ---------------------------------------------------------------- Hamiltonicity

def hamiltonian_cycle(G):
    """Return a Hamiltonian cycle (list of vertices) or None. Backtracking DFS."""
    n = G.number_of_nodes()
    if n < 3:
        return None
    nodes = list(G.nodes())
    start = nodes[0]
    adj = {v: sorted(G.neighbors(v), key=str) for v in G.nodes()}
    path = [start]
    on_path = {start}

    def extend():
        v = path[-1]
        if len(path) == n:
            return start in adj[v]
        for w in adj[v]:
            if w in on_path:
                continue
            # prune: any unvisited vertex (other than w) with all remaining
            # neighbours visited (except start) cannot be reached any more
            path.append(w)
            on_path.add(w)
            if extend():
                return True
            path.pop()
            on_path.remove(w)
        return False

    return list(path) if extend() else None


def is_hypohamiltonian(F, verbose=True):
    """Brute-force check: F non-Hamiltonian, F-v Hamiltonian for every v."""
    hc = hamiltonian_cycle(F)
    if hc is not None:
        if verbose:
            print(f"    F IS Hamiltonian: {hc}")
        return False
    for v in F.nodes():
        H = F.copy()
        H.remove_node(v)
        if hamiltonian_cycle(H) is None:
            if verbose:
                print(f"    F-{v} is NOT Hamiltonian")
            return False
    return True


# ---------------------------------------------------------------- graph builders

def flower_snark(k):
    """Isaacs flower snark J_k (k odd >= 5): 4k vertices, cubic, girth >= 5."""
    G = nx.Graph()
    for i in range(k):
        A, B, C, D = ("A", i), ("B", i), ("C", i), ("D", i)
        G.add_edges_from([(A, B), (A, C), (A, D)])
        G.add_edge(("B", i), ("B", (i + 1) % k))
    for i in range(k - 1):
        G.add_edge(("C", i), ("C", i + 1))
        G.add_edge(("D", i), ("D", i + 1))
    G.add_edge(("C", k - 1), ("D", 0))
    G.add_edge(("D", k - 1), ("C", 0))
    return G


# ---------------------------------------------------------------- Lemma 1 check

def cycle_lengths_in_graph(F, lo=3):
    """Set of lengths of simple cycles in F (exhaustive via nx.simple_cycles)."""
    return {len(c) for c in nx.simple_cycles(F) if len(c) >= lo}


def chordless_cycle_lengths(G, bound=None, lo=3):
    """Set of lengths of chordless (induced) cycles in G."""
    return {len(c) for c in nx.chordless_cycles(G, length_bound=bound)
            if len(c) >= lo}


def check_lemma1(trials=30, seed=12345):
    rng = random.Random(seed)
    for trial in range(trials):
        n = rng.randint(7, 11)
        p = rng.uniform(0.2, 0.45)
        F = nx.gnp_random_graph(n, p, seed=rng.randint(0, 10**9))
        L = nx.line_graph(F)
        a = {l for l in cycle_lengths_in_graph(F) if l >= 4}
        b = {l for l in chordless_cycle_lengths(L) if l >= 4}
        if a != b:
            print(f"  LEMMA 1 FAILS on trial {trial}: n={n} p={p:.2f}")
            print(f"    cycle lengths in F  (>=4): {sorted(a)}")
            print(f"    induced cycles in L (>=4): {sorted(b)}")
            print(f"    edges of F: {sorted(map(sorted, F.edges()))}")
            return False
    print(f"  Lemma 1 verified on {trials} random graphs (n in 7..11): "
          f"induced C_l in L(F) <-> C_l in F for all l >= 4.")
    return True


# ---------------------------------------------------------------- Lemma 2 check

def canon(L):
    """Map frozenset of endpoints -> line-graph node."""
    return {frozenset(v): v for v in L.nodes()}


def witness_set(F, L, e):
    """Build the writeup's witness S for edge e = (x,y) of L(F). Returns S or a
    string describing the failure."""
    x, y = e
    shared = set(x) & set(y)
    if len(shared) != 1:
        return f"endpoints of {e} share {len(shared)} vertices"
    c = shared.pop()
    others = [frozenset(ed) for ed in F.edges(c)
              if frozenset(ed) not in (frozenset(x), frozenset(y))]
    if len(others) != 1:
        return f"vertex {c} has {2 + len(others)} incident edges (not cubic?)"
    z = others[0]
    (d,) = set(z) - {c}
    H = F.copy()
    H.remove_node(d)
    Q = hamiltonian_cycle(H)
    if Q is None:
        return f"F-{d} not Hamiltonian"
    cmap = canon(L)
    S = [cmap[frozenset((Q[i], Q[(i + 1) % len(Q)]))] for i in range(len(Q))]
    S.append(cmap[z])
    return S


def is_cycle_graph(G, m):
    return (G.number_of_nodes() == m
            and all(d == 2 for _, d in G.degree())
            and nx.is_connected(G))


def check_construction(name, F, exhaustive_per_edge=False):
    m = F.number_of_nodes()
    print(f"  --- {name}: m = {m}, t = {m // 2 + 1} ---")
    assert all(d == 3 for _, d in F.degree()), "not cubic"
    assert nx.is_connected(F)
    assert not any(True for _ in nx.selfloop_edges(F))
    print(f"    simple, connected, cubic: OK ({F.number_of_edges()} edges)")

    if not is_hypohamiltonian(F):
        print("    NOT hypohamiltonian -- FATAL for this test graph")
        return False
    print("    hypohamiltonian (non-Ham.; F-v Ham. for all v): OK")

    L = nx.line_graph(F)
    nL = L.number_of_nodes()
    assert nL == 3 * m // 2, f"|V(L)| = {nL} != 3m/2"
    print(f"    |V(L(F))| = {nL} = 3m/2: OK")

    # no induced C_m in L(F): exhaustive chordless-cycle enumeration
    count_m = 0
    total = 0
    for c in nx.chordless_cycles(L, length_bound=m):
        total += 1
        if len(c) == m:
            count_m += 1
    print(f"    chordless cycles of L(F) with length <= {m}: {total}; "
          f"of length exactly {m}: {count_m}")
    if count_m != 0:
        print("    FATAL: L(F) contains an induced C_m")
        return False

    # every edge deletion creates an induced C_m
    edges = list(L.edges())
    ok = 0
    for e in edges:
        S = witness_set(F, L, e)
        if isinstance(S, str):
            print(f"    edge {e}: witness construction failed: {S}")
            return False
        Lmm = L.copy()
        Lmm.remove_edge(*e)
        sub = Lmm.subgraph(S)
        if not is_cycle_graph(sub, m):
            print(f"    edge {e}: witness S does NOT induce C_{m} in L-e")
            return False
        ok += 1
    print(f"    witness check: L(F)-e has an induced C_{m} "
          f"for all {ok}/{len(edges)} edges e: OK")

    if exhaustive_per_edge:
        for e in edges:
            Lmm = L.copy()
            Lmm.remove_edge(*e)
            found = any(len(c) == m
                        for c in nx.chordless_cycles(Lmm, length_bound=m))
            if not found:
                print(f"    edge {e}: exhaustive search finds NO induced C_{m}")
                return False
        print(f"    exhaustive per-edge chordless-cycle search "
              f"({len(edges)} edges): OK")
    return True


def main():
    random.seed(0)
    print("A. Lemma 1 (line-graph induced cycles):")
    ok = check_lemma1()

    print("B. Lemma 2 / construction on concrete cubic hypohamiltonian graphs:")
    ok &= check_construction("Petersen graph", nx.petersen_graph(),
                             exhaustive_per_edge=True)
    ok &= check_construction("flower snark J5", flower_snark(5))
    ok &= check_construction("flower snark J7 (m=28 => t=15, in the t>=14 "
                             "regime of the writeup)", flower_snark(7))

    print()
    print("ALL CHECKS PASSED" if ok else "SOME CHECK FAILED")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
