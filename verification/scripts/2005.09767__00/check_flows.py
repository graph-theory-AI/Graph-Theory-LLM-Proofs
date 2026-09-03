"""Check the writeup's claimed bounds for 2005.09767__00 on explicit 3-edge-connected graphs.

For each graph G (edges oriented arbitrarily) and each k in {6, 7}:
  enumerate the whole Z_k-flow space (k^r points, r = m - n + 1) via a fundamental-
  cycle basis, and for many (or all) forbidden functions f count
      N(G, f) = #{flows phi : phi(e) != f(e) for all e}.
Compare with the writeup's bounds:
  Z_7 : N >= 7^(r - m/6)                (Section 2)
  Z_6 : N >= 3^((4r - m)/6)             (Section 3, = 3^((3m-4n+4)/6))
"""
import itertools, random
import numpy as np

def cycle_space_basis(n, edges):
    """Fundamental cycle basis. Returns list of integer vectors (len m)."""
    m = len(edges)
    adj = {v: [] for v in range(n)}
    for i, (u, v) in enumerate(edges):
        adj[u].append((v, i, 1))
        adj[v].append((u, i, -1))
    parent = {0: None}
    seen = {0}
    tree_edges = set()
    queue = [0]
    while queue:
        u = queue.pop(0)
        for (v, i, s) in adj[u]:
            if v not in seen:
                seen.add(v); parent[v] = (u, i, s); tree_edges.add(i)
                queue.append(v)
    assert len(seen) == n, "graph not connected"
    def path_to_root(v):
        out = {}
        while parent[v] is not None:
            u, i, s = parent[v]
            out[i] = out.get(i, 0) + s
            v = u
        return out
    basis = []
    for i, (u, v) in enumerate(edges):
        if i in tree_edges:
            continue
        vec = [0] * m
        vec[i] += 1
        for j, s in path_to_root(u).items():
            vec[j] += s
        for j, s in path_to_root(v).items():
            vec[j] -= s
        basis.append(vec)
    return basis

def all_flows(n, edges, k):
    """Return (k^r, m) numpy array of all Z_k-flows."""
    m = len(edges)
    basis = np.array(cycle_space_basis(n, edges), dtype=np.int64)
    r = len(basis)
    assert r == m - n + 1, (r, m, n)
    coeffs = np.array(list(itertools.product(range(k), repeat=r)), dtype=np.int64)
    flows = coeffs @ basis % k
    assert len({tuple(x) for x in flows}) == k ** r, "basis dependent mod k"
    # verify conservation on all flows
    net = np.zeros((len(flows), n), dtype=np.int64)
    for j, (u, v) in enumerate(edges):
        net[:, u] -= flows[:, j]
        net[:, v] += flows[:, j]
    assert np.all(net % k == 0), "not flows!"
    return flows

def min_avoiding(flows, fs, chunk=200):
    """min over rows f of fs of  #{phi in flows : phi != f everywhere}."""
    best = None; arg = None
    for lo in range(0, len(fs), chunk):
        F = fs[lo:lo + chunk]                      # (c, m)
        diff = flows[None, :, :] != F[:, None, :]  # (c, |flows|, m)
        counts = diff.all(axis=2).sum(axis=1)      # (c,)
        i = int(counts.argmin())
        if best is None or counts[i] < best:
            best = int(counts[i]); arg = tuple(int(x) for x in F[i])
    return best, arg

GRAPHS = {
    "theta(2v,3e)": (2, [(0, 1), (0, 1), (0, 1)]),
    "banana(2v,4e)": (2, [(0, 1), (0, 1), (0, 1), (1, 0)]),
    "triple-triangle(3v,6e)": (3, [(0,1),(0,1),(1,2),(1,2),(2,0),(2,0)]),
    "K4": (4, [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]),
    "K4+loop": (4, [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3),(1,1)]),
    "K4_doubled_edge": (4, [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3),(0,1)]),
    "prism": (6, [(0,1),(1,2),(2,0),(3,4),(4,5),(5,3),(0,3),(1,4),(2,5)]),
    "K33": (6, [(0,3),(0,4),(0,5),(1,3),(1,4),(1,5),(2,3),(2,4),(2,5)]),
    "wheel5": (6, [(0,1),(1,2),(2,3),(3,4),(4,0),(5,0),(5,1),(5,2),(5,3),(5,4)]),
    "petersen": (10, [(0,1),(1,2),(2,3),(3,4),(4,0),
                      (0,5),(1,6),(2,7),(3,8),(4,9),
                      (5,7),(7,9),(9,6),(6,8),(8,5)]),
}

def z7_bound(n, m, r):
    return 7.0 ** (r - m / 6)

def z6_bound(n, m, r):
    return 3.0 ** ((4 * r - m) / 6)

def check(name, n, edges, k, bound_fn, exhaustive_limit=400000, random_trials=500):
    m = len(edges)
    r = m - n + 1
    if k ** r > 6 ** 7:
        print(f"{name:22s} k={k}: flow space too big, skipped")
        return True
    flows = all_flows(n, edges, k)
    b = bound_fn(n, m, r)
    rng = random.Random(hash((name, k)) & 0xffff)
    if k ** m <= exhaustive_limit:
        fs = np.array(list(itertools.product(range(k), repeat=m)), dtype=np.int64)
        mode = f"exhaustive {k}^{m} f's"
    else:
        cand = [[rng.randrange(k) for _ in range(m)] for _ in range(random_trials)]
        cand += [[c] * m for c in range(k)]
        for _ in range(80):   # adversarial: perturbations of actual flows
            phi = list(flows[rng.randrange(len(flows))])
            cand.append([(int(x) + rng.randrange(1, k) * (rng.random() < .6)) % k
                         for x in phi])
        fs = np.array(cand, dtype=np.int64)
        mode = f"{len(fs)} sampled f's"
    minN, arg = min_avoiding(flows, fs)
    ok = minN >= b - 1e-9
    print(f"{name:22s} k={k} n={n} m={m} r={r}  bound={b:10.3f}  min N={minN:8d}"
          f"  ({mode})  {'OK' if ok else '*** VIOLATION *** f=' + str(arg)}")
    return ok

if __name__ == "__main__":
    all_ok = True
    for name, (n, edges) in GRAPHS.items():
        all_ok &= check(name, n, edges, 7, z7_bound)
        all_ok &= check(name, n, edges, 6, z6_bound)
    print("ALL OK" if all_ok else "SOME VIOLATION FOUND")
