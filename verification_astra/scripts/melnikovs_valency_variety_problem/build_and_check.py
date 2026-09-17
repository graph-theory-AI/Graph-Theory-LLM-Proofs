"""Independent reconstruction of the 37-vertex graph claimed in
attacks_opg/melnikovs_valency_variety_problem/output.md, built strictly from the
prose of section 1, plus exact verification of every claimed property.
"""
import itertools, math
import networkx as nx

A = [f"a{i}" for i in range(1, 6)]          # a1..a5
B = [f"b{j}" for j in range(0, 6)]          # b0..b5
C = [f"c{j}" for j in range(0, 7)]          # c0..c6
T = [f"t{i}" for i in range(1, 7)]          # t1..t6
U = [f"u{i}" for i in range(1, 13)]         # u1..u12
Z = ["z"]

G = nx.Graph()
G.add_nodes_from(A + B + C + T + U + Z)

# (1) complete tripartite on A,B,C
for x, y in itertools.chain(itertools.product(A, B), itertools.product(A, C), itertools.product(B, C)):
    G.add_edge(x, y)

# (2) T joined to every vertex of B u C
for x, y in itertools.product(T, B + C):
    G.add_edge(x, y)

# (3) u7..u12 joined to every vertex of B
for i in range(7, 13):
    for b in B:
        G.add_edge(f"u{i}", b)

# (4) U-A edges
for i, nbrs in [(7, ["a5"]), (8, ["a4", "a5"]), (9, ["a3", "a4", "a5"])]:
    for a in nbrs:
        G.add_edge(f"u{i}", a)

# (5) u_i ~ c_j iff j >= 13-i, for i in {10,11,12}
for i in (10, 11, 12):
    for j in range(0, 7):
        if j >= 13 - i:
            G.add_edge(f"u{i}", f"c{j}")

# (6) for 1<=i<=6: u_i ~ b_j iff i+j >= 7
for i in range(1, 7):
    for j in range(0, 6):
        if i + j >= 7:
            G.add_edge(f"u{i}", f"b{j}")
# plus the six explicit U-C edges
for e in [("u1", "c4"), ("u2", "c5"), ("u3", "c5"), ("u4", "c6"), ("u5", "c6"), ("u6", "c6")]:
    G.add_edge(*e)

n = G.number_of_nodes()
print("n =", n, " m =", G.number_of_edges())
assert n == 37

deg = dict(G.degree())
print("degrees by vertex:")
for v in A + B + C + T + U + Z:
    print(f"  {v:>4}: {deg[v]}")

ds = sorted(set(deg.values()))
w = len(ds)
print("degree set =", ds)
print("w(G) =", w)
assert ds == list(range(30)), "degree set is NOT {0,...,29}"

# --- claimed degree table from the writeup ---
claimed = {}
claimed["z"] = 0
for i in range(1, 13):
    claimed[f"u{i}"] = i
for v in ["a1", "a2"] + T:
    claimed[v] = 13
claimed["a3"], claimed["a4"], claimed["a5"] = 14, 15, 16
for j in range(7):
    claimed[f"c{j}"] = 17 + j
for j in range(6):
    claimed[f"b{j}"] = 24 + j
mismatch = {v: (deg[v], claimed[v]) for v in deg if deg[v] != claimed[v]}
print("degree-table mismatches (actual, claimed):", mismatch)
assert not mismatch

# --- chromatic number ---
print("bipartite? ", nx.is_bipartite(G))            # must be False  => chi >= 3
tri = [t for t in itertools.combinations(G.nodes, 3)
       if G.has_edge(t[0], t[1]) and G.has_edge(t[1], t[2]) and G.has_edge(t[0], t[2])]
print("number of triangles:", len(tri), "  e.g.", tri[0] if tri else None)
print("is a1-b0-c0 a triangle?", G.has_edge("a1","b0") and G.has_edge("b0","c0") and G.has_edge("a1","c0"))

# claimed 3-colouring
I1 = set(A) | set(T) | {f"u{i}" for i in [1,2,3,4,5,6,10,11,12]} | {"z"}
I2 = set(B)
I3 = set(C) | {"u7", "u8", "u9"}
print("parts sizes:", len(I1), len(I2), len(I3), "union size:", len(I1 | I2 | I3))
assert I1 | I2 | I3 == set(G.nodes) and len(I1)+len(I2)+len(I3) == 37
for name, I in [("I1", I1), ("I2", I2), ("I3", I3)]:
    bad = [(x, y) for x, y in itertools.combinations(sorted(I), 2) if G.has_edge(x, y)]
    print(f"  {name} independent: {not bad}", bad[:3])
    assert not bad

# exact chi by exhaustive 2-colourability test (= bipartiteness, already done)
# and by an independent greedy/DSATUR + exact 3-SAT-free backtracking 3-colouring search
def k_colourable(Gr, k):
    nodes = sorted(Gr.nodes, key=lambda v: -Gr.degree(v))
    colour = {}
    def bt(idx):
        if idx == len(nodes):
            return True
        v = nodes[idx]
        used = {colour[u] for u in Gr[v] if u in colour}
        maxnew = (max(colour.values()) + 1) if colour else 0
        for c in range(min(k, maxnew + 1)):
            if c not in used:
                colour[v] = c
                if bt(idx + 1):
                    return True
                del colour[v]
        return False
    return bt(0)

print("2-colourable (backtracking):", k_colourable(G, 2))
print("3-colourable (backtracking):", k_colourable(G, 3))

chi = 3
t = n - w
rhs = math.ceil((w // 2) / t)
print(f"\nn={n}, w={w}, n-w={t}, floor(w/2)={w//2}, RHS=ceil({w//2}/{t})={rhs}, chi={chi}")
print("conjecture chi > RHS holds?", chi > rhs)
print("reformulation n <= (2k-1)t+1 :", n, "<=", (2*chi-1)*t+1, "?", n <= (2*chi-1)*t+1)

# --- the graph minus the isolated vertex ---
H = G.copy(); H.remove_node("z")
dh = sorted(set(dict(H.degree()).values()))
nh, wh = H.number_of_nodes(), len(dh)
th = nh - wh
print(f"\nG-z: n={nh}, degree set={dh[0]}..{dh[-1]} (size {wh}), n-w={th}, "
      f"RHS=ceil({wh//2}/{th})={math.ceil((wh//2)/th)}, chi=3 -> holds? {3 > math.ceil((wh//2)/th)}")
print("G-z connected?", nx.is_connected(H))
print("components of G:", [len(c) for c in nx.connected_components(G)])

# --- third, independent confirmation that chi = 3 ---
# chi >= 3: exhibit an odd cycle / triangle (done) AND verify no 2-colouring exists by
# propagating from every vertex of the 36-vertex component (a graph is 2-colourable iff
# every component is bipartite; we re-derive this by hand rather than trusting is_bipartite).
def two_colour_component(Gr, src):
    col = {src: 0}
    stack = [src]
    while stack:
        v = stack.pop()
        for u in Gr[v]:
            if u not in col:
                col[u] = 1 - col[v]
                stack.append(u)
            elif col[u] == col[v]:
                return None, (v, u)
    return col, None
for comp in nx.connected_components(G):
    src = next(iter(comp))
    col, conflict = two_colour_component(G, src)
    print("component of size", len(comp), "-> 2-colourable:", col is not None,
          "" if col else f"(monochromatic edge forced at {conflict})")
