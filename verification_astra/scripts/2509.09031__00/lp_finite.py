"""Same LP as lp_turncost.py but on the FINITE 4-regular graph H (girth 6),
where the monochromatic subgraphs are unions of cycles.  This is the setting
in which the writeup's averaging step (6.9) applies."""
import itertools
import numpy as np
from scipy.optimize import linprog
from verify_construction import H, red, blue

S = 6
def colour(e):
    e = (min(e), max(e)); return 'R' if e in red else 'B'
E_H = sorted((min(u, v), max(u, v)) for u, v in H.edges())
idx = {e: i for i, e in enumerate(E_H)}
m = len(E_H)

def paths(s, mode):
    out = []
    for u in H:
        stack = [([u], [], None)]
        while stack:
            vs, es, lastc = stack.pop()
            if len(es) == s:
                out.append(tuple(es)); continue
            x = vs[-1]
            for y in H[x]:
                if y in vs: continue
                c = colour((x, y))
                if lastc is not None:
                    if mode == 'mono' and c != lastc: continue
                    if mode == 'alt' and c == lastc: continue
                stack.append((vs + [y], es + [idx[(min(x, y), max(x, y))]], c))
    return out

for s in (2, 3, 4, 5, 6, 7):
    mono, alt = paths(s, 'mono'), paths(s, 'alt')
    c = np.zeros(m + 1); c[-1] = 1.0
    rows, rhs = [], []
    for P in mono:
        r = np.zeros(m + 1)
        for e in P: r[e] += 1.0
        r[-1] = -1.0; rows.append(r); rhs.append(S * s + 2)
    for P in alt:
        r = np.zeros(m + 1)
        for e in P: r[e] -= 1.0
        r[-1] = -1.0; rows.append(r); rhs.append(-(S * s + s - 1))
    res = linprog(c, A_ub=np.array(rows), b_ub=np.array(rhs),
                  bounds=[(0, None)] * m + [(0, None)], method='highs')
    print(f"finite H (26 vtcs, girth 6, 2-factorised): s={s} #mono={len(mono)} #alt={len(alt)} "
          f"-> LP lower bound on additive error E = {res.fun:.4f}")
print("\n(compare: direct local search over all edge weightings reached 1.7465;")
print(" the same LP on an acyclic (tree) model returns 0, so step (6.9)'s averaging")
print(" over the monochromatic CYCLES is genuinely load-bearing.)")
