"""Checks for the isolated-K2 'counterexample' in attacks/2211.01032__00/output.md.

1. An isolated K2 component has exactly 1 facial cycle (componentwise convention).
2. E[X2] = C(n,2) p (1-p)^(2n-4) exactly (verified by exhaustive enumeration for n=5
   and by Monte Carlo for n=8).
3. Numeric evaluation of E[X2] at p = log n/(3n) vs n^{1/3} log n / 6 for large n.
4. The paper's convention F(n,p) = F(M) - c(M) + 1 (arXiv:2211.01032v3, Section 7,
   'each isolated vertex (in fact any tree) always contributes zero') neutralizes the
   counterexample: Monte Carlo on sparse G(n,p) comparing componentwise total faces
   vs the paper's normalized count.
"""
import itertools, math, random

random.seed(20260902)

# ---------- generic face counting from a rotation system ----------
def faces_of_component(edges, rot):
    """edges: set of frozensets {u,v}; rot: dict v -> cyclic list of neighbours.
    Returns number of facial cycles of phi = R o L on darts (u,v) (dart with tail u
    pointing to v), where L(u,v)=(v,u) and R(v,u_prev)=(v, next neighbour of v after
    u_prev in rot[v]). Convention: phi(d) = R(L(d))."""
    darts = set()
    for e in edges:
        u, v = tuple(e)
        darts.add((u, v)); darts.add((v, u))
    nxt = {}
    for v, cyc in rot.items():
        k = len(cyc)
        for i, u in enumerate(cyc):
            nxt[(v, u)] = (v, cyc[(i + 1) % k])
    seen, nf = set(), 0
    for d in darts:
        if d in seen:
            continue
        nf += 1
        cur = d
        while cur not in seen:
            seen.add(cur)
            u, v = cur
            cur = nxt[(v, u)]  # phi = R(L(cur))
    return nf

def random_rotation(adj):
    rot = {}
    for v, nb in adj.items():
        nb = list(nb)
        random.shuffle(nb)
        rot[v] = nb
    return rot

def components(vertices, edges):
    adj = {v: set() for v in vertices}
    for e in edges:
        u, v = tuple(e)
        adj[u].add(v); adj[v].add(u)
    seen, comps = set(), []
    for s in vertices:
        if s in seen:
            continue
        stack, comp = [s], set()
        while stack:
            x = stack.pop()
            if x in comp:
                continue
            comp.add(x)
            stack.extend(adj[x] - comp)
        seen |= comp
        comps.append(comp)
    return comps, adj

def face_counts(vertices, edges):
    """Returns (componentwise_total_faces, paper_F) for ONE random rotation system.
    componentwise: sum of facial cycles over components that contain edges
    (isolated vertices carry no darts -> 0 facial cycles; topologically they'd add
    1 face each on their own sphere, which only helps the counterexample).
    paper_F: for components WITH edges we count facial cycles; a component that is a
    single vertex embeds in the sphere with 1 face. paper convention:
    F(M) - c(M) + 1 with every component (incl. isolated vertices) having >=1 face."""
    comps, adj = components(vertices, edges)
    total = 0
    n_comps = len(comps)
    for comp in comps:
        ce = {e for e in edges if next(iter(e)) in comp or list(e)[1] in comp}
        ce = {e for e in edges if set(e) <= comp}
        if not ce:
            total += 1  # isolated vertex on its own sphere: 1 face
            continue
        rot = random_rotation({v: adj[v] for v in comp})
        total += faces_of_component(ce, rot)
    edge_comp_faces = total - sum(1 for c in comps if not any(set(e) <= c for e in edges))
    paper_F = total - n_comps + 1
    return edge_comp_faces, paper_F, n_comps

# ---------- 1. isolated K2 has one face ----------
f = faces_of_component({frozenset((0, 1))}, {0: [1], 1: [0]})
print("[1] faces of isolated K2 (componentwise):", f, "(expected 1)")
assert f == 1

# ---------- 2. E[X2] formula ----------
def count_X2(n, edges):
    deg = {v: 0 for v in range(n)}
    for e in edges:
        u, v = tuple(e)
        deg[u] += 1; deg[v] += 1
    return sum(1 for e in edges if all(deg[x] == 1 for x in e))

n = 5
pairs = list(itertools.combinations(range(n), 2))
for p in (0.1, 0.3, 0.5):
    ex = 0.0
    for mask in range(1 << len(pairs)):
        edges = {frozenset(pairs[i]) for i in range(len(pairs)) if mask >> i & 1}
        w = p ** len(edges) * (1 - p) ** (len(pairs) - len(edges))
        ex += w * count_X2(n, edges)
    formula = math.comb(n, 2) * p * (1 - p) ** (2 * n - 4)
    print(f"[2] n=5 p={p}: exact E[X2]={ex:.6f}  formula C(n,2)p(1-p)^(2n-4)={formula:.6f}")
    assert abs(ex - formula) < 1e-9

p, T = 0.25, 200000
pairs8 = list(itertools.combinations(range(8), 2))
acc = 0
for _ in range(T):
    edges = {frozenset(e) for e in pairs8 if random.random() < p}
    acc += count_X2(8, edges)
mc = acc / T
formula = math.comb(8, 2) * p * (1 - p) ** (2 * 8 - 4)
print(f"[2] n=8 p={p}: MC E[X2]={mc:.4f} (T={T})  formula={formula:.4f}")

# ---------- 3. asymptotics at p = log n /(3n) ----------
print("[3] E[X2] at p=log n/(3n) vs n^(1/3) log n/6 and vs ln(p n^2):")
for n in (10**4, 10**6, 10**8, 10**10):
    p = math.log(n) / (3 * n)
    ex2 = math.comb(n, 2) * p * (1 - p) ** (2 * n - 4) if n <= 10**6 else \
        (n * (n - 1) / 2) * p * math.exp((2 * n - 4) * math.log1p(-p))
    approx = n ** (1 / 3) * math.log(n) / 6
    rhs = math.log(p * n * n)
    print(f"    n=1e{int(math.log10(n))}: E[X2]={ex2:.4g}  n^(1/3)ln(n)/6={approx:.4g}  ratio={ex2/approx:.4f}  ln(pn^2)={rhs:.3f}")

# ---------- 4. the paper's convention neutralizes the counterexample ----------
print("[4] sparse G(n,p), p=log n/(3n): componentwise faces vs paper's F-c+1 (MC):")
n, T = 300, 30
p = math.log(n) / (3 * n)
pairs_n = list(itertools.combinations(range(n), 2))
cw_acc = pf_acc = x2_acc = 0
for _ in range(T):
    edges = {frozenset(e) for e in pairs_n if random.random() < p}
    cw, pf, nc = face_counts(set(range(n)), edges)
    cw_acc += cw; pf_acc += pf; x2_acc += count_X2(n, edges)
print(f"    n={n}, p={p:.5f}, ln(pn^2)={math.log(p*n*n):.3f}, T={T}")
print(f"    mean componentwise faces (edge components) = {cw_acc/T:.2f}")
print(f"    mean paper F(n,p)=F(M)-c(M)+1              = {pf_acc/T:.2f}")
print(f"    mean X2 (isolated K2 count)                = {x2_acc/T:.2f}")
