#!/usr/bin/env python3
"""Verify the two load-bearing identities of the writeup:

(1) p_G(x) = mu_G(x) - 2*mu_F(x), where F = G - V(C), for unicyclic G
    (mu = matching polynomial), tested exactly (integer arithmetic) on
    all unicyclic graphs up to n=10.

(8) D(G) = s+(G) - s-(G) = -(4*eta/pi) * Int_0^inf t*arctan(2*M_F(t)/M_G(t)) dt,
    with eta = (-1)^((k-1)/2), tested numerically on all odd-cycle unicyclic
    graphs up to n=9 (adaptive quadrature vs eigenvalue computation).
"""
import itertools
import networkx as nx
import numpy as np
from scipy.integrate import quad

def matching_generating_counts(G):
    """Return list m[j] = number of j-edge matchings of G (m[0]=1)."""
    edges = list(G.edges())
    nodes = list(G.nodes())
    idx = {v: i for i, v in enumerate(nodes)}
    # DP over edges with bitmask of used vertices would be 2^n; instead use
    # recursive deletion: m(G) = m(G-e) + m(G-{u,v}) on edge e.
    from functools import lru_cache
    E = tuple(sorted((min(idx[u], idx[v]), max(idx[u], idx[v])) for u, v in edges))

    def rec(edge_list):
        if not edge_list:
            return [1]
        u, v = edge_list[0]
        rest = edge_list[1:]
        a = rec(rest)                      # e not in matching
        rest2 = tuple(e for e in rest if u not in e and v not in e)
        b = rec(rest2)                     # e in matching
        out = list(a)
        for j, c in enumerate(b):
            if j + 1 >= len(out):
                out.append(0)
            out[j + 1] += c
        return out

    return rec(E)

def matching_poly_coeffs(G):
    """mu_G(x) = sum_j (-1)^j m_j x^(h-2j); return numpy poly coeffs (highest first)."""
    h = G.number_of_nodes()
    m = matching_generating_counts(G)
    coeffs = [0] * (h + 1)
    for j, mj in enumerate(m):
        coeffs[2 * j] += ((-1) ** j) * mj   # coefficient of x^(h-2j)
    return np.array(coeffs, dtype=float)

def M_poly_vals(G, t):
    """M_H(t) = sum_j m_j t^(h-2j), for t>0 array."""
    h = G.number_of_nodes()
    m = matching_generating_counts(G)
    return sum(mj * t ** (h - 2 * j) for j, mj in enumerate(m))

def char_poly_coeffs(G):
    A = nx.to_numpy_array(G)
    return np.poly(A)  # det(xI - A), highest first

# ---------- Part 1: identity (1), exact on integers ----------
print("== Identity (1): p_G = mu_G - 2 mu_F ==")
fails = 0
checked = 0
for n in range(3, 11):
    for T in nx.nonisomorphic_trees(n):
        for u, v in itertools.combinations(list(T.nodes()), 2):
            if T.has_edge(u, v):
                continue
            G = T.copy(); G.add_edge(u, v)
            cyc_nodes = set()
            for a, b in nx.find_cycle(G):
                cyc_nodes.add(a); cyc_nodes.add(b)
            F = G.copy(); F.remove_nodes_from(cyc_nodes)
            muG = matching_poly_coeffs(G)
            h_f = F.number_of_nodes()
            muF = matching_poly_coeffs(F) if h_f > 0 else np.array([1.0])
            # pad muF to length n+1 (align by degree: mu_F has degree n-k)
            rhs = muG.copy()
            rhs[n - h_f:] -= 2 * muF
            pG = np.round(char_poly_coeffs(G))
            if not np.allclose(rhs, pG, atol=1e-6):
                fails += 1
                if fails <= 5:
                    print("  FAIL:", n, sorted(G.edges()), rhs, pG)
            checked += 1
print(f"checked {checked} unicyclic graphs (n<=10), identity failures: {fails}")

# ---------- Part 2: formula (8), numeric ----------
print("\n== Formula (8): D(G) = -(4 eta/pi) * Int t*arctan(2 M_F/M_G) dt ==")
worst = 0.0
checked = 0
fails8 = 0
for n in range(3, 10):
    for T in nx.nonisomorphic_trees(n):
        for u, v in itertools.combinations(list(T.nodes()), 2):
            if T.has_edge(u, v):
                continue
            G = T.copy(); G.add_edge(u, v)
            cyc = nx.find_cycle(G)
            k = len(cyc)
            if k % 2 == 0:
                continue
            cyc_nodes = set()
            for a, b in cyc:
                cyc_nodes.add(a); cyc_nodes.add(b)
            F = G.copy(); F.remove_nodes_from(cyc_nodes)
            ev = np.linalg.eigvalsh(nx.to_numpy_array(G))
            D_direct = float(np.sum(np.sign(np.where(np.abs(ev) < 1e-9, 0, ev)) * ev ** 2))
            eta = (-1) ** ((k - 1) // 2)
            mG = matching_generating_counts(G)
            mF = matching_generating_counts(F) if F.number_of_nodes() > 0 else [1]
            hF = F.number_of_nodes()

            def integrand(t):
                MG = sum(mj * t ** (n - 2 * j) for j, mj in enumerate(mG))
                MF = sum(mj * t ** (hF - 2 * j) for j, mj in enumerate(mF))
                return t * np.arctan(2 * MF / MG)

            I, err = quad(integrand, 0, np.inf, limit=400)
            D_formula = -(4 * eta / np.pi) * I
            diff = abs(D_direct - D_formula)
            worst = max(worst, diff)
            checked += 1
            if diff > 1e-6:
                fails8 += 1
                if fails8 <= 5:
                    print("  FAIL:", n, k, sorted(G.edges()), D_direct, D_formula)
print(f"checked {checked} odd-cycle unicyclic graphs (n<=9); max |direct-formula| = {worst:.3g}; failures: {fails8}")
