"""Brute-force check of Lemma 1.1 of attacks_retry/2509.09031__00/output.md.

C = { J connected simple : every two distinct vertices of B(J)={v: deg>=3}
      are joined by a *thread* = path whose internal vertices have degree 2 in J }.

Claim: C is closed under edge subdivision and edge contraction
(contraction on simple graphs, i.e. suppressing loops/parallel edges).
"""
import itertools, sys
import networkx as nx
from networkx.generators.atlas import graph_atlas_g


def branch(J):
    return {v for v in J if J.degree(v) >= 3}


def threads_from(J, u):
    """All maximal degree-2 chains starting at u; return set of other endpoints
    reachable by a path whose internal vertices all have degree 2."""
    ends = set()
    for w in J.neighbors(u):
        prev, cur = u, w
        seen = {u}
        while J.degree(cur) == 2 and cur not in seen:
            seen.add(cur)
            nbrs = [x for x in J.neighbors(cur) if x != prev]
            if not nbrs:
                break
            prev, cur = cur, nbrs[0]
        if J.degree(cur) != 2:
            ends.add(cur)
    return ends


def in_C(J):
    if J.number_of_nodes() == 0 or not nx.is_connected(J):
        return False
    B = branch(J)
    for u, v in itertools.combinations(B, 2):
        if v not in threads_from(J, u):
            return False
    return True


def contract(J, e):
    K = nx.contracted_edge(J, e, self_loops=False)
    return nx.Graph(K)  # drop contraction attributes / parallel edges


def subdivide(J, e):
    K = J.copy()
    u, v = e
    new = ('s', u, v)
    K.remove_edge(u, v)
    K.add_edge(u, new)
    K.add_edge(new, v)
    return K


def main():
    atlas = graph_atlas_g()
    tested = 0
    members = 0
    bad_c = []
    bad_s = []
    for J in atlas:
        if J.number_of_nodes() < 2 or not nx.is_connected(J):
            continue
        tested += 1
        if not in_C(J):
            continue
        members += 1
        for e in list(J.edges()):
            Jc = contract(J, e)
            if Jc.number_of_nodes() >= 2 and not in_C(Jc):
                bad_c.append((sorted(J.edges()), e))
            Js = subdivide(J, e)
            if not in_C(Js):
                bad_s.append((sorted(J.edges()), e))
    print(f"connected atlas graphs tested: {tested}")
    print(f"members of C: {members}")
    print(f"contraction failures: {len(bad_c)}")
    for x in bad_c[:5]:
        print("   ", x)
    print(f"subdivision failures: {len(bad_s)}")
    for x in bad_s[:5]:
        print("   ", x)


if __name__ == '__main__':
    main()
