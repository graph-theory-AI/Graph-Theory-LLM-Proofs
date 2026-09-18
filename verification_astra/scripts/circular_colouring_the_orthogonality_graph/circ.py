"""Exact circular chromatic number of small finite graphs, plus helpers.

chi_c(G) = min{ p/q in lowest terms, p <= |V(G)|, G -> K_{p/q} }  (G with an edge).
K_{p/q}: vertices Z_p, a~b iff q <= (b-a mod p) <= p-q.
Homomorphism test by backtracking with forward checking (bitmask domains).
"""
from fractions import Fraction
from math import gcd
from itertools import combinations


def circ_clique_adj(p, q):
    """adjacency bitmasks of K_{p/q} on Z_p."""
    adj = [0] * p
    for a in range(p):
        m = 0
        for b in range(p):
            d = (b - a) % p
            if q <= d <= p - q:
                m |= 1 << b
        adj[a] = m
    return adj


def hom_exists(nbrs, n, p, q):
    """Is there a homomorphism from graph (nbrs = list of neighbour-bitmasks) to K_{p/q}?"""
    adj = circ_clique_adj(p, q)
    full = (1 << p) - 1
    # order vertices by a greedy max-connectivity-to-assigned order
    order = []
    placed = 0
    remaining = set(range(n))
    while remaining:
        best = max(remaining, key=lambda v: (bin(nbrs[v] & placed).count("1"), bin(nbrs[v]).count("1")))
        order.append(best)
        placed |= 1 << best
        remaining.discard(best)
    pos = {v: i for i, v in enumerate(order)}

    dom = [full] * n
    colour = [-1] * n

    def bt(i):
        if i == n:
            return True
        v = order[i]
        d = dom[v]
        if i == 0:
            d &= 1  # vertex-transitivity of K_{p/q}: fix first colour to 0
        while d:
            c = (d & -d).bit_length() - 1
            d &= d - 1
            colour[v] = c
            saved = []
            ok = True
            m = nbrs[v]
            while m:
                u = (m & -m).bit_length() - 1
                m &= m - 1
                if colour[u] == -1:
                    old = dom[u]
                    new = old & adj[c]
                    if new != old:
                        saved.append((u, old))
                        dom[u] = new
                    if new == 0:
                        ok = False
                        break
            if ok and bt(i + 1):
                return True
            for u, old in saved:
                dom[u] = old
            colour[v] = -1
        return False

    return bt(0)


def fractions_upto(n):
    """all p/q in lowest terms, 2 <= p/q, p <= n, q >= 1, sorted ascending."""
    out = set()
    for q in range(1, n // 2 + 1):
        for p in range(2 * q, n + 1):
            if gcd(p, q) == 1:
                out.add(Fraction(p, q))
    return sorted(out)


def chi_c(nbrs, n):
    if all(m == 0 for m in nbrs):
        return Fraction(1, 1)
    for f in fractions_upto(n):
        if hom_exists(nbrs, n, f.numerator, f.denominator):
            return f
    return None  # should not happen (chi_c <= n)


def to_nbrs(n, edges):
    nbrs = [0] * n
    for u, v in edges:
        if u != v:
            nbrs[u] |= 1 << v
            nbrs[v] |= 1 << u
    return nbrs


def common_neighbour_property(nbrs, n):
    """every pair of vertices (possibly equal) has a common neighbour."""
    for u in range(n):
        for v in range(u, n):
            if nbrs[u] & nbrs[v] == 0:
                return False
    return True
