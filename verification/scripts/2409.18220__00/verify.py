#!/usr/bin/env python3
"""Referee verification for 2409.18220__00.

Checks:
  A. s(K_4), s(P_4), s(K_{1,3}), s(C_4)  (the claimed order-4 counterexamples)
  B. s(K_n) = n-1 and the threshold n-1 >= 4n/5 <=> n >= 5
  C. odd cycles C_5, C_7, C_9 vs 4n/5, and s(C_n) >= n-2 via eigenvalues
  D. min of s(G) - 4n/5 over ALL connected graphs with 4 <= n <= 7 (atlas)
  E. Proposition 1:  s(G) >= 2m/chi(G)  and ratio bound max ratio <= chi-1
  F. Proposition 2:  s(G) >= 4m^2/(2m + sum d_i^2)
"""
import itertools
import math
import networkx as nx
import numpy as np


def s_pm(G):
    ev = np.linalg.eigvalsh(nx.to_numpy_array(G))
    tol = 1e-9
    sp = float(sum(x * x for x in ev if x > tol))
    sm = float(sum(x * x for x in ev if x < -tol))
    return sp, sm


def s(G):
    sp, sm = s_pm(G)
    return min(sp, sm)


def chromatic_number(G):
    n = G.number_of_nodes()
    if G.number_of_edges() == 0:
        return 1 if n else 0
    nodes = list(G.nodes())
    for c in range(2, n + 1):
        # greedy feasibility via backtracking
        color = {}

        def bt(i):
            if i == len(nodes):
                return True
            v = nodes[i]
            used = {color[u] for u in G[v] if u in color}
            for col in range(c):
                if col not in used:
                    color[v] = col
                    if bt(i + 1):
                        return True
                    del color[v]
                if col not in used and col == max(color.values(), default=-1) + 1:
                    break  # symmetry: first use of a fresh color only once
            return False

        if bt(0):
            return c
    return n


print("== A. Order-4 counterexamples ==")
for name, G in [("K_4", nx.complete_graph(4)), ("P_4", nx.path_graph(4)),
                ("K_{1,3}", nx.star_graph(3)), ("C_4", nx.cycle_graph(4))]:
    sp, sm = s_pm(G)
    print(f"  {name}: s+ = {sp:.6f}, s- = {sm:.6f}, s = {min(sp,sm):.6f}, "
          f"4n/5 = {4*G.number_of_nodes()/5:.2f}, "
          f"violates 4n/5: {min(sp,sm) < 4*G.number_of_nodes()/5 - 1e-9}")

print("\n== B. Complete graphs ==")
for n in range(2, 13):
    v = s(nx.complete_graph(n))
    print(f"  K_{n}: s = {v:.6f} (n-1 = {n-1}), s >= 4n/5: {v >= 4*n/5 - 1e-9}")

print("\n== C. Odd cycles ==")
for n in [5, 7, 9, 11, 13]:
    sp, sm = s_pm(nx.cycle_graph(n))
    v = min(sp, sm)
    print(f"  C_{n}: s+ = {sp:.6f}, s- = {sm:.6f}, s = {v:.6f}, "
          f"4n/5 = {4*n/5:.2f}, ok: {v >= 4*n/5 - 1e-9}, s >= n-2: {v >= n-2-1e-9}")

print("\n== D. All connected graphs, 4 <= n <= 7 (graph atlas) ==")
atlas = nx.graph_atlas_g()
by_n = {}
for G in atlas:
    n = G.number_of_nodes()
    if 4 <= n <= 7 and n and nx.is_connected(G):
        by_n.setdefault(n, []).append(G)
for n in sorted(by_n):
    worst = None
    viol = []
    for G in by_n[n]:
        v = s(G)
        if worst is None or v < worst[0]:
            worst = (v, sorted(d for _, d in G.degree()), G.number_of_edges())
        if v < 4 * n / 5 - 1e-9:
            viol.append((v, sorted(map(str, (tuple(sorted(e)) for e in G.edges())))))
    print(f"  n={n}: {len(by_n[n])} connected graphs, min s = {worst[0]:.6f} "
          f"(4n/5 = {4*n/5:.2f}), violations of s >= 4n/5: {len(viol)}")
    for v, edges in viol:
        print(f"      violator: s = {v:.6f}, edges = {edges}")

print("\n== E. Proposition 1: s >= 2m/chi and ratio <= chi-1, all connected n<=7 ==")
bad1 = bad_ratio = 0
checked = 0
for n in sorted(by_n):
    for G in by_n[n]:
        m = G.number_of_edges()
        c = chromatic_number(G)
        sp, sm = s_pm(G)
        checked += 1
        if min(sp, sm) < 2 * m / c - 1e-7:
            bad1 += 1
            print(f"  PROP1 FAIL n={n} edges={list(G.edges())}")
        if max(sp / sm, sm / sp) > c - 1 + 1e-7:
            bad_ratio += 1
            print(f"  RATIO FAIL n={n} chi={c} edges={list(G.edges())}")
print(f"  checked {checked} graphs; Prop1 failures: {bad1}; ratio failures: {bad_ratio}")

print("\n== F. Proposition 2: s >= 4m^2/(2m + sum d_i^2), all connected n<=7 ==")
bad2 = 0
for n in sorted(by_n):
    for G in by_n[n]:
        m = G.number_of_edges()
        sd2 = sum(d * d for _, d in G.degree())
        sp, sm = s_pm(G)
        if min(sp, sm) < 4 * m * m / (2 * m + sd2) - 1e-7:
            bad2 += 1
            print(f"  PROP2 FAIL n={n} edges={list(G.edges())}")
print(f"  Prop2 failures: {bad2}")

print("\n== extra: 4n/5 vs n-1 crossover ==")
for n in range(4, 7):
    print(f"  n={n}: 4n/5 = {4*n/5:.2f}, n-1 = {n-1}, 4n/5 <= n-1: {4*n/5 <= n-1}")
