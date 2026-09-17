"""Randomised stress test of Lemma 1.1 on larger graphs in C (8..16 vertices),
including deliberately C-shaped graphs: subdivisions of complete graphs with
extra pendant paths / cycles attached, then random contractions/subdivisions."""
import random, itertools
import networkx as nx
from check_class_closure import in_C, contract, subdivide, branch

random.seed(20260917)

def random_C_member(rng):
    """Build a random graph, keep only if in C. Bias towards structured ones."""
    kind = rng.random()
    if kind < 0.45:
        k = rng.randint(3, 6)
        G = nx.complete_graph(k)
        H = nx.Graph()
        for (u, v) in G.edges():
            L = rng.randint(1, 3)
            prev = ('b', u)
            for i in range(L - 1):
                cur = ('i', u, v, i)
                H.add_edge(prev, cur); prev = cur
            H.add_edge(prev, ('b', v))
        # optionally attach a pendant path or a loop-cycle at a branch vertex
        if rng.random() < 0.5:
            b = ('b', rng.randrange(k))
            L = rng.randint(1, 3)
            prev = b
            for i in range(L):
                cur = ('p', i, rng.random())
                H.add_edge(prev, cur); prev = cur
        if rng.random() < 0.4:
            b = ('b', rng.randrange(k))
            L = rng.randint(3, 5)
            prev = b
            nodes = []
            for i in range(L - 1):
                cur = ('c', i, rng.random())
                H.add_edge(prev, cur); prev = cur
            H.add_edge(prev, b)
        return H
    else:
        n = rng.randint(6, 11)
        p = rng.uniform(0.2, 0.6)
        H = nx.gnp_random_graph(n, p, seed=rng.randrange(10**9))
        if not nx.is_connected(H):
            return None
        if rng.random() < 0.7:  # subdivide a few edges
            for e in list(H.edges()):
                if rng.random() < 0.4:
                    H = subdivide(H, e)
        return H

tested = 0
members = 0
fail_c = 0
fail_s = 0
examples = []
trials = 0
while trials < 200000 and members < 20000:
    trials += 1
    H = random_C_member(random)
    if H is None or H.number_of_nodes() < 2 or not nx.is_connected(H):
        continue
    tested += 1
    if not in_C(H):
        continue
    members += 1
    for e in list(H.edges()):
        Hc = contract(H, e)
        if Hc.number_of_nodes() >= 2 and not in_C(Hc):
            fail_c += 1
            if len(examples) < 3:
                examples.append(('contract', sorted(map(str, H.edges())), str(e)))
        Hs = subdivide(H, e)
        if not in_C(Hs):
            fail_s += 1
            if len(examples) < 3:
                examples.append(('subdivide', sorted(map(str, H.edges())), str(e)))

print(f"trials={trials} connected candidates={tested} members of C={members}")
print(f"contraction failures={fail_c}  subdivision failures={fail_s}")
for ex in examples:
    print(ex)
