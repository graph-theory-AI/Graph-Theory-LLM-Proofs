"""Section 5: the finite witness F_m.  For m=7 (the smallest palette K_{7/2}) the writeup
takes the 2m+1 = 15 moment-curve lines and adjoins, for every triple, the lines of the
odd closed walk.  Check that every one of the C(15,3)=455 triples really yields a valid
odd closed walk, and measure how large F_m gets.
Also: check the SHARPNESS of the 'finite' hypothesis, i.e. that O itself is locally
bipartite (so the pigeonhole step is genuinely load-bearing)."""
import numpy as np, itertools, math, networkx as nx
NCAP = 3000

def frame(a, b, c):
    a = a/np.linalg.norm(a); b = b/np.linalg.norm(b); c = c/np.linalg.norm(c)
    if np.dot(a, b) < 0: b = -b
    e3 = a; bp = b - np.dot(b, a)*a; e1 = bp/np.linalg.norm(bp); e2 = np.cross(e3, e1)
    R = np.vstack([e1, e2, e3]); return R@a, R@b, R@c, R

def walk_for(a, b, c):
    """Return (walk, n).  Handles the perpendicular case separately."""
    a, b, c = (np.asarray(t, float) for t in (a, b, c))
    for p, q in itertools.combinations([a, b, c], 2):
        if abs(np.dot(p, q)) < 1e-12:
            return [p, q, np.cross(p, q), p], 'perp'
    A, B, C, R = frame(a, b, c); s, t = B[0], B[2]; u, v, w = C
    K = 4*t*w*(s*u + t*w)
    n = 0 if K <= 0 else max(0, math.ceil(math.log((s*v)**2/K)/(2*math.log(t))))
    if n > NCAP: return None, n
    E = np.array([[t**2, 0.], [0., 1.]]); F = np.array([[0., s*u + t*w], [-t*w, s*v]])
    M = np.linalg.matrix_power(E, n) @ F
    ev, evec = np.linalg.eig(M)
    assert np.max(np.abs(ev.imag)) < 1e-9
    k = int(np.argmax(np.abs(ev.real))); x0 = evec[:, k].real; x0 /= np.linalg.norm(x0)
    a1, b1, c1 = R.T@A, R.T@B, R.T@C
    x = R.T @ np.array([x0[0], x0[1], 0.])
    walk = [x]
    for d in [b1, c1, a1] + n*[b1, b1, a1, a1]:
        x = np.cross(d, x); x = x/np.linalg.norm(x); walk.append(x)
    return walk, n

L = [np.array([1., j, j*j]) for j in range(1, 16)]
lens, worst_err, bad, big = [], 0.0, 0, []
for i, j, k in itertools.combinations(range(15), 3):
    a, b, c = L[i], L[j], L[k]
    walk, n = walk_for(a, b, c)
    if walk is None:
        big.append((i+1, j+1, k+1, n)); continue
    ln = len(walk) - 1
    if ln % 2 != 1: bad += 1; print("EVEN LENGTH", i, j, k); continue
    for q in range(ln):
        worst_err = max(worst_err, abs(np.dot(walk[q], walk[q+1])))
    for p in walk:
        d = min(abs(np.dot(p, a/np.linalg.norm(a))), abs(np.dot(p, b/np.linalg.norm(b))),
                abs(np.dot(p, c/np.linalg.norm(c))))
        worst_err = max(worst_err, d)
    worst_err = max(worst_err, np.linalg.norm(np.cross(walk[0], walk[-1])))
    lens.append(ln)
print(f"triples fully built: {len(lens)}   invalid: {bad}   skipped (n>{NCAP}): {len(big)}")
print("  largest required n among skipped triples:", max([b[3] for b in big], default=0))
print(f"odd-walk lengths: min {min(lens)}, median {int(np.median(lens))}, max {max(lens)}")
print(f"total lines adjoined (with multiplicity): {sum(lens)}  -> |V(F_7)| <= {15 + sum(lens)}")
print(f"worst numerical violation over all checks (orthogonality / containment / closure): {worst_err:.3e}")

print("\nSharpness: is O itself locally bipartite?  N_O(L) = lines of the plane L^perp,")
print("in which each line has exactly one perpendicular -> a perfect matching -> bipartite.")
def canon(v):
    g = math.gcd(math.gcd(abs(v[0]), abs(v[1])), abs(v[2])); v = (v[0]//g, v[1]//g, v[2]//g)
    return v if (v[2], v[1], v[0]) > (0, 0, 0) else (-v[0], -v[1], -v[2])
V = sorted({canon(v) for v in itertools.product(range(-5, 6), repeat=3) if v != (0, 0, 0)})
G = nx.Graph(); G.add_nodes_from(V)
for x, y in itertools.combinations(V, 2):
    if x[0]*y[0]+x[1]*y[1]+x[2]*y[2] == 0: G.add_edge(x, y)
locb = all(nx.is_bipartite(G.subgraph(list(G.neighbors(v)))) for v in V)
maxdeg_in_nbhd = max((max((G.subgraph(list(G.neighbors(v))).degree(u) for u in G.neighbors(v)), default=0)
                      for v in V), default=0)
print(f"  integer-direction subgraph, sup-norm<=5: {G.number_of_nodes()} lines, {G.number_of_edges()} edges;"
      f" every neighbourhood bipartite: {locb}; max degree inside a neighbourhood: {maxdeg_in_nbhd}")
print("  => the 'finite' hypothesis on the target H is essential (O -> O is a homomorphism"
      " to a locally bipartite graph).")
