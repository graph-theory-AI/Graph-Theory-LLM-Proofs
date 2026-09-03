#!/usr/bin/env python3
"""Verification for referee report 2503.16882__00.

Checks every computational claim in attacks/2503.16882__00/output.md:
  1. Spec(K_3) = {2,-1,-1};  E_p^-(K_3) = 2 for all p.
  2. Spec(P_3) = {sqrt2, 0, -sqrt2};  E_p^-(P_3) = 2^{p/2}.
  3. 2^{p/2} > 2 for p > 2  (so K_3 violates the P_n-comparator form for p>2),
     and equality at p = 2 (no violation there).
  4. Spec(K_4 - e) = {(1+sqrt17)/2, 0, -1, (1-sqrt17)/2};
     E_4^-(K_4-e) = 1 + ((sqrt17-1)/2)^4 = (51 - 9 sqrt17)/2 < 7.
  5. Spec(P_4) negative part -> E_4^-(P_4) = 7.
  6. E_2^-(P_n) = n-1 = E_2^-(K_n) for a range of n (the p=2 coincidence).
  7. Exhaustive sanity sweep: all connected graphs on n <= 7 vertices at
     p in {3,4}: does any violate the K_n-comparator form E_p^-(G) >= n-1?
     (Expected: none, consistent with the source paper's theorem for p>=4
      and the follow-up for p>=3.)
"""
import itertools
import math

import networkx as nx
import numpy as np
import sympy as sp


def neg_p_energy_exact(G, p):
    A = sp.Matrix(nx.adjacency_matrix(G).todense())
    total = sp.Integer(0)
    for lam, mult in A.eigenvals().items():
        lam = sp.nsimplify(lam)
        # decide sign numerically to high precision (is_negative can be None on CRootOf)
        if sp.re(sp.N(lam, 50)) < 0:
            total += mult * (sp.Abs(lam)) ** p
    return sp.simplify(total)


def neg_p_energy_float(G, p):
    A = nx.adjacency_matrix(G).todense().astype(float)
    ev = np.linalg.eigvalsh(A)
    return float(sum(abs(l) ** p for l in ev if l < -1e-9))


print("== 1-3: K_3 vs P_3 ==")
K3 = nx.complete_graph(3)
P3 = nx.path_graph(3)
A3 = sp.Matrix(nx.adjacency_matrix(K3).todense())
print("Spec(K_3):", A3.eigenvals())
AP3 = sp.Matrix(nx.adjacency_matrix(P3).todense())
print("Spec(P_3):", AP3.eigenvals())
for p in [2, sp.Rational(5, 2), 3, 4, 5]:
    ek = neg_p_energy_exact(K3, p)
    ep = neg_p_energy_exact(P3, p)
    print(f"  p={p}: E^-_p(K3)={ek} ({float(ek):.6f}), "
          f"E^-_p(P3)={sp.simplify(ep)} ({float(ep):.6f}), "
          f"K3 >= P3 ? {sp.simplify(ek - ep) >= 0}")

print()
print("== 4-5: K_4 - e vs P_4 at p = 4 ==")
K4e = nx.complete_graph(4)
K4e.remove_edge(0, 1)
A = sp.Matrix(nx.adjacency_matrix(K4e).todense())
print("Spec(K_4 - e):", A.eigenvals())
e4 = neg_p_energy_exact(K4e, 4)
claimed = sp.Rational(51, 2) - sp.Rational(9, 2) * sp.sqrt(17)
print("E_4^-(K_4-e) =", sp.simplify(e4), "=", float(e4))
print("matches (51-9*sqrt17)/2 ?", sp.simplify(e4 - claimed) == 0)
p4 = neg_p_energy_exact(nx.path_graph(4), 4)
print("E_4^-(P_4) =", sp.simplify(p4), "=", float(p4))
print("K_4-e < P_4 at p=4 ?", sp.simplify(e4 - p4) < 0)
print("check 37 < 9*sqrt(17):  9^2*17 =", 81 * 17, "> 37^2 =", 37 * 37)

print()
print("== 6: E_2^-(P_n) = n-1 = E_2^-(K_n) ==")
for n in range(2, 11):
    epn = neg_p_energy_exact(nx.path_graph(n), 2)
    ekn = neg_p_energy_exact(nx.complete_graph(n), 2)
    ok = sp.simplify(epn - (n - 1)) == 0 and sp.simplify(ekn - (n - 1)) == 0
    print(f"  n={n}: E_2^-(P_n)={sp.simplify(epn)}, E_2^-(K_n)={sp.simplify(ekn)}, both = n-1 ? {ok}")

print()
print("== 7: sweep — K_n-comparator form E_p^-(G) >= n-1, connected G, n<=7, p in {3,4} ==")
viol = []
best = {}
for n in range(2, 8):
    for G in nx.graph_atlas_g():
        if G.number_of_nodes() == n and nx.is_connected(G) if G.number_of_nodes() > 0 else False:
            for p in (3, 4):
                v = neg_p_energy_float(G, p)
                key = (n, p)
                if key not in best or v < best[key][0]:
                    best[key] = (v, sorted(d for _, d in G.degree()))
                if v < n - 1 - 1e-8:
                    viol.append((n, p, v, nx.to_dict_of_lists(G)))
for (n, p), (v, degs) in sorted(best.items()):
    print(f"  n={n}, p={p}: min E_p^- over connected graphs = {v:.6f} (n-1 = {n-1}), degrees of minimizer {degs}")
print("violations of E_p^-(G) >= n-1:", viol if viol else "NONE")

print()
print("== extra: how badly does the P_n-comparator form fail? sweep n<=7, p=3,4 ==")
pn_viol_count = {}
for n in range(2, 8):
    Ppn = {p: neg_p_energy_float(nx.path_graph(n), p) for p in (3, 4)}
    for G in nx.graph_atlas_g():
        if G.number_of_nodes() == n and nx.is_connected(G):
            for p in (3, 4):
                if neg_p_energy_float(G, p) < Ppn[p] - 1e-8:
                    pn_viol_count[(n, p)] = pn_viol_count.get((n, p), 0) + 1
for k in sorted(pn_viol_count):
    print(f"  n={k[0]}, p={k[1]}: {pn_viol_count[k]} connected graphs with E_p^-(G) < E_p^-(P_n)")
