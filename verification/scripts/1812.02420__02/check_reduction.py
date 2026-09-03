#!/usr/bin/env python3
"""
Referee computational check for attack 1812.02420__02.

Writeup claim: for the two-layer construction R(D) (two copies of D, matching
digons between corresponding copies, no other cross arcs):

    chi_f_vec(R(D)) <= 2   <=>   chi_vec(D) <= 2,

where chi_f_vec is the fractional dichromatic number (LP over acyclic vertex
sets, digons count as directed 2-cycles) and chi_vec is the dichromatic number.

We verify:
  1. chi_vec(D) by brute force over 2-partitions.
  2. chi_f_vec(H) by solving the exact covering LP over all acyclic subsets
     (scipy linprog / HiGHS), for H = R(D).
  3. The forcing lemma consequence chi_f_vec(R(D)) >= 2 for nonempty D.
  4. The equivalence on named examples and on many random digraphs.
"""
import itertools
import random
import sys

import networkx as nx
from scipy.optimize import linprog


def is_acyclic_subset(D, S):
    """S subset of nodes; True iff D[S] has no directed cycle.
    D is a MultiDiGraph; a digon (antiparallel pair) is a directed 2-cycle."""
    H = D.subgraph(S)
    return nx.is_directed_acyclic_graph(H)


def acyclic_sets(D):
    nodes = list(D.nodes())
    out = []
    for r in range(1, len(nodes) + 1):
        for S in itertools.combinations(nodes, r):
            if is_acyclic_subset(D, S):
                out.append(frozenset(S))
    return out


def frac_dichromatic(D):
    """Exact-value LP min sum x_A st sum_{A ni v} x_A >= 1, x >= 0."""
    nodes = list(D.nodes())
    if not nodes:
        return 0.0, []
    A = acyclic_sets(D)
    if any(not is_acyclic_subset(D, [v]) for v in nodes):
        return float("inf"), []  # loop vertex: infeasible
    n, m = len(nodes), len(A)
    # linprog: min c x st A_ub x <= b_ub  ->  -coverage <= -1
    c = [1.0] * m
    A_ub = [[-1.0 if nodes[i] in A[j] else 0.0 for j in range(m)] for i in range(n)]
    b_ub = [-1.0] * n
    res = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=[(0, None)] * m, method="highs")
    assert res.status == 0, res.message
    support = [(A[j], res.x[j]) for j in range(m) if res.x[j] > 1e-9]
    return res.fun, support


def dichromatic_at_most_2(D):
    nodes = list(D.nodes())
    n = len(nodes)
    for mask in range(2 ** (n - 1) if n else 1):  # fix node 0's side by symmetry
        C0 = [nodes[0]] + [nodes[i + 1] for i in range(n - 1) if mask >> i & 1]
        C1 = [v for v in nodes if v not in set(C0)]
        if is_acyclic_subset(D, C0) and is_acyclic_subset(D, C1):
            return True
    return False if n else True


def R(D):
    """The writeup's construction: layers 0,1 each a copy of D; matching digons."""
    H = nx.MultiDiGraph()
    for v in D.nodes():
        H.add_node((v, 0))
        H.add_node((v, 1))
    for u, v in D.edges():  # multi-edges preserved
        H.add_edge((u, 0), (v, 0))
        H.add_edge((u, 1), (v, 1))
    for v in D.nodes():
        H.add_edge((v, 0), (v, 1))
        H.add_edge((v, 1), (v, 0))
    return H


def check(name, D, expect_chi2=None):
    chi2 = dichromatic_at_most_2(D)
    H = R(D)
    val, support = frac_dichromatic(H)
    ok_equiv = (val <= 2 + 1e-7) == chi2
    # forcing-lemma consequences when val ~ 2: support sets are digon transversals
    transversal_ok = True
    if chi2 and D.number_of_nodes() > 0:
        for A, w in support:
            for v in D.nodes():
                if len(A & {(v, 0), (v, 1)}) != 1:
                    transversal_ok = False
    lower_ok = (D.number_of_nodes() == 0) or (val >= 2 - 1e-7)
    status = "OK " if (ok_equiv and transversal_ok and lower_ok) else "FAIL"
    print(f"[{status}] {name}: n={D.number_of_nodes()} chi<=2: {chi2}  "
          f"chi_f(R(D)) = {val:.6f}  equiv:{ok_equiv} lower>=2:{lower_ok} "
          f"transversal-support:{transversal_ok}")
    if expect_chi2 is not None:
        assert chi2 == expect_chi2, f"{name}: expected chi<=2 == {expect_chi2}"
    return ok_equiv and transversal_ok and lower_ok


def bidirected_complete(n):
    D = nx.MultiDiGraph()
    D.add_nodes_from(range(n))
    for u in range(n):
        for v in range(n):
            if u != v:
                D.add_edge(u, v)
    return D


def paley7():
    # Paley tournament on 7 vertices, QR = {1,2,4}; dichromatic number 3.
    D = nx.MultiDiGraph()
    D.add_nodes_from(range(7))
    for u in range(7):
        for d in (1, 2, 4):
            D.add_edge(u, (u + d) % 7)
    return D


def main():
    random.seed(12345)
    allok = True

    C3 = nx.MultiDiGraph([(0, 1), (1, 2), (2, 0)])
    allok &= check("directed triangle C3 (chi=2)", C3, expect_chi2=True)

    K3s = bidirected_complete(3)
    allok &= check("bidirected K3 (chi=3)", K3s, expect_chi2=False)

    K2s = bidirected_complete(2)
    allok &= check("single digon K2s (chi=2)", K2s, expect_chi2=True)

    P7 = paley7()
    allok &= check("Paley tournament ST7 (digon-free, chi=3)", P7,
                   expect_chi2=False)

    one = nx.MultiDiGraph()
    one.add_node(0)
    allok &= check("single vertex", one, expect_chi2=True)

    # sanity: chi_f of R(C3) direct value and chi_f of C3 itself
    valC3, _ = frac_dichromatic(C3)
    print(f"  sanity: chi_f(C3) = {valC3:.6f} (expected 1.5 = 3/2)")

    # random digraphs, n up to 6, various densities, some with forced digons
    trials, nfail = 0, 0
    for t in range(120):
        n = random.randint(1, 6)
        p = random.choice([0.2, 0.35, 0.5, 0.7])
        D = nx.MultiDiGraph()
        D.add_nodes_from(range(n))
        for u in range(n):
            for v in range(n):
                if u != v and random.random() < p:
                    D.add_edge(u, v)
        trials += 1
        if not check(f"random #{t} (n={n}, p={p})", D):
            nfail += 1
            allok = False
    print(f"\nrandom trials: {trials}, failures: {nfail}")
    print("ALL CHECKS PASSED" if allok else "SOME CHECKS FAILED")
    sys.exit(0 if allok else 1)


if __name__ == "__main__":
    main()
