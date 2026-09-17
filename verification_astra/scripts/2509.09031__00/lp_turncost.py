"""LP test of the quantitative core of Section 6.

The writeup's contradiction is purely linear in the edge lengths lambda:
  * every MONOCHROMATIC H-path P of length s obeys   lambda(P) <= S s + 2 + E
  * every ALTERNATING H-path P of length s obeys     lambda(P) >= S s + s - 1 - E
(the first from (6.8), the second from d_lambda >= d_G - E together with the
verified identity d_G((v_0)_R,(v_s)_R) = S s + s - 1).

Since only paths of length s matter and girth(H) >> s, we may model the local
structure of H exactly by the 4-regular tree with two red and two blue edges at
each vertex.  Minimising E over lambda >= 0 is then an LP; its optimum is a
lower bound on the additive error A that the writeup claims must exceed ~ g/10000.
"""
import itertools
import numpy as np
from scipy.optimize import linprog

S = 100  # corridor length; the LP optimum is independent of S


def tree(depth):
    """4-regular tree, root at (), each vertex has 2 red + 2 blue incident edges."""
    G = {}
    edges = {}

    def add(u, v, col):
        e = len(edges) if (u, v) not in edges and (v, u) not in edges else None
        key = (u, v)
        edges[key] = (len(edges), col)
        G.setdefault(u, []).append((v, edges[key][0], col))
        G.setdefault(v, []).append((u, edges[key][0], col))

    frontier = [((), None)]
    for d in range(depth):
        nxt = []
        for (u, incol) in frontier:
            cols = ['R', 'R', 'B', 'B']
            if incol is not None:
                cols.remove(incol)  # one slot of that colour already used
            for j, c in enumerate(cols):
                v = u + (d, j)
                add(u, v, c)
                nxt.append((v, c))
        frontier = nxt
    return G, len(edges)


def paths_of_length(G, s, mode):
    out = []
    for u in G:
        stack = [([u], [], None)]
        while stack:
            vs, es, lastc = stack.pop()
            if len(es) == s:
                out.append(tuple(es)); continue
            x = vs[-1]
            for (y, ei, c) in G[x]:
                if y in vs:
                    continue
                if lastc is not None:
                    if mode == 'mono' and c != lastc:
                        continue
                    if mode == 'alt' and c == lastc:
                        continue
                stack.append((vs + [y], es + [ei], c))
    return out


print(f"{'s':>3} {'#edges':>8} {'#mono':>8} {'#alt':>8} {'min E (LP)':>12} {'(s-3)/2':>9}")
for s in range(2, 8):   # acyclic model: optimum is 0 for every s (see report)
    G, m = tree(s)
    mono = paths_of_length(G, s, 'mono')
    alt = paths_of_length(G, s, 'alt')
    if not mono or not alt:
        continue
    # variables: lambda_0..lambda_{m-1}, E  ; minimise E
    c = np.zeros(m + 1); c[-1] = 1.0
    rows, rhs = [], []
    for P in mono:                       # lambda(P) - E <= S s + 2
        r = np.zeros(m + 1)
        for e in P: r[e] += 1.0
        r[-1] = -1.0
        rows.append(r); rhs.append(S * s + 2)
    for P in alt:                        # -lambda(P) - E <= -(S s + s - 1)
        r = np.zeros(m + 1)
        for e in P: r[e] -= 1.0
        r[-1] = -1.0
        rows.append(r); rhs.append(-(S * s + s - 1))
    res = linprog(c, A_ub=np.array(rows), b_ub=np.array(rhs),
                  bounds=[(0, None)] * m + [(0, None)], method='highs')
    print(f"{s:>3} {m:>8} {len(mono):>8} {len(alt):>8} {res.fun:>12.4f} {(s-3)/2:>9.2f}")
