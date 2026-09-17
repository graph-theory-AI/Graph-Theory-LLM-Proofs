"""Construction of the writeup's family G_t and basic invariants.

G_t:  cycles C_i = a_i b_i c_i d_i a_i  (1<=i<=t),  K_4 gadgets Q_j on p_j q_j r_j s_j (0<=j<=t)
edges: a_i p_i, c_i q_i ;  d_i b_{i+1} (1<=i<t) ;  b_1 p_0 , d_t q_0.
"""
import itertools
import networkx as nx


def build(t):
    G = nx.Graph()
    for i in range(1, t + 1):
        a, b, c, d = (f"a{i}", f"b{i}", f"c{i}", f"d{i}")
        G.add_edges_from([(a, b), (b, c), (c, d), (d, a)])
    for j in range(0, t + 1):
        vs = [f"p{j}", f"q{j}", f"r{j}", f"s{j}"]
        for u, v in itertools.combinations(vs, 2):
            G.add_edge(u, v)
    for i in range(1, t + 1):
        G.add_edge(f"a{i}", f"p{i}")
        G.add_edge(f"c{i}", f"q{i}")
    for i in range(1, t):
        G.add_edge(f"d{i}", f"b{i+1}")
    G.add_edge("b1", "p0")
    G.add_edge(f"d{t}", "q0")
    return G


def all_cycles(G):
    """All simple cycles as frozensets of vertices (vertex sets of chordless-or-not cycles)."""
    return [frozenset(c) for c in nx.simple_cycles(G)]


def fvs_bruteforce(G):
    V = list(G.nodes())
    n = len(V)
    for k in range(0, n + 1):
        for S in itertools.combinations(V, k):
            H = G.copy()
            H.remove_nodes_from(S)
            if nx.is_forest(H):
                return k, S
    return None


def max_disjoint(cycle_sets):
    """Max number of pairwise vertex-disjoint cycles from the given list (exact, small instances)."""
    cycle_sets = sorted(set(cycle_sets), key=len)
    best = [0, None]

    def rec(idx, used, chosen):
        if len(chosen) > best[0]:
            best[0] = len(chosen)
            best[1] = list(chosen)
        for k in range(idx, len(cycle_sets)):
            C = cycle_sets[k]
            if not (C & used):
                chosen.append(C)
                rec(k + 1, used | C, chosen)
                chosen.pop()

    rec(0, frozenset(), [])
    return best


if __name__ == "__main__":
    for t in (1, 2, 3):
        G = build(t)
        print(f"=== t={t} ===")
        print("  n =", G.number_of_nodes(), " (claimed 8t+4 =", 8 * t + 4, ")")
        print("  m =", G.number_of_edges())
        degs = sorted(set(dict(G.degree()).values()))
        print("  degrees present:", degs, " max deg =", max(dict(G.degree()).values()))
        print("  simple:", not any(G.has_edge(u, u) for u in G))
        print("  planar:", nx.check_planarity(G)[0])
        print("  connectivity:", nx.node_connectivity(G))
        if t <= 2:
            k, S = fvs_bruteforce(G)
            print(f"  fvs = {k}   (claimed 3t+2 = {3*t+2})   witness {sorted(S)}")
            cycles = all_cycles(G)
            print("  #simple cycles:", len(cycles))
            cp, wit = max_disjoint(cycles)
            print(f"  cp  = {cp}   (claimed 2t+1 = {2*t+1})")
            # writeup's explicit fvs witness
            Sw = [f"a{i}" for i in range(1, t + 1)] + \
                 [f"p{j}" for j in range(t + 1)] + [f"q{j}" for j in range(t + 1)]
            H = G.copy(); H.remove_nodes_from(Sw)
            print(f"  writeup's S (size {len(Sw)}) leaves a forest:", nx.is_forest(H))
            # gadget claim: at most one cycle of a packing meets Q_j
            for j in range(t + 1):
                Q = {f"p{j}", f"q{j}", f"r{j}", f"s{j}"}
                meet = [C for C in set(cycles) if C & Q]
                bad = [(A, B) for A, B in itertools.combinations(meet, 2) if not (A & B)]
                print(f"  Q_{j}: {len(meet)} cycles meet it; disjoint pairs among them: {len(bad)}")
            # cycles avoiding all gadgets
            allQ = {f"{x}{j}" for j in range(t + 1) for x in "pqrs"}
            free = [C for C in set(cycles) if not (C & allQ)]
            print("  cycles avoiding every gadget:", sorted(sorted(C) for C in free))
