#!/usr/bin/env python3
"""Independent verification for attack 1809.05439__00.

Claim under review: the graph G (two subdivided 5-wheels H^1, H^2 sharing hub x,
plus z_j adjacent to u_0^j, u_1^j, and edge z_1 z_2) is triangle-free and planar,
and admits NO set coloring phi by subsets of {1..9} with |phi(v)| >= 3 for all v
and |phi(x)| = 5 (adjacent vertices getting disjoint sets).

WLOG reductions used in checks B and C (both preserve existence both ways):
  * shrinking: from any coloring with sizes >= 3 (and |phi(x)| >= 5) one gets a
    proper coloring with every non-x size EXACTLY 3 and |phi(x)| exactly 5 by
    discarding colors; so searching exact sizes suffices.
  * relabeling: the property is invariant under permutations of {1..9}, so we
    may fix phi(x) = {0,1,2,3,4} =: P (0-indexed colors).
Check D uses NO reductions at all (SAT, cardinality constraints ">= 3", ">= 5").

Checks performed:
  A. Structure of G: 23 vertices, 35 edges, planar, triangle-free, girth 4.
  B. Lemma rigidity on the single gadget H (subdivided 5-wheel): exhaustively
     enumerate ALL proper colorings of H with phi(x)=P, others exactly 3
     colors, and verify each satisfies the writeup's Lemma:
       1. phi(u_i) = Q minus {q_i} for some q_i in Q  (Q = {1..9} minus P);
       2. q_i in phi(v_i);
       3. q_i != q_{i+1};  consequence: phi(u_i) | phi(u_{i+1}) = Q.
     Also confirm at least one coloring of H exists (the gadget alone is NOT
     a counterexample; the paper's bound |phi(x)| <= 5k/9 is attained at k=9).
  C. Nonexistence of the coloring of G via an exact decomposition: the two
     copies of the rooted gadget H+z share only x and interact only through
     the edge z1z2, so G has the required coloring  <=>  there exist proper
     colorings phi_1, phi_2 of H+z (phi(x)=P fixed, all others exactly 3
     colors) with phi_1(z) and phi_2(z) disjoint. Enumerate ALL achievable
     phi(z) values and look for a disjoint pair.
  D. Fully independent double-check: SAT encoding of the ORIGINAL statement
     on G (boolean var per vertex-color pair; adjacent vertices never share a
     color; every vertex has >= 3 colors; x has >= 5). Expect UNSAT.
     Sanity controls: same encoding with |phi(x)| >= 4 on G (expect SAT,
     since Theorem 5-style colorings scale) and >= 5 on a single H (expect
     SAT, consistent with B).
"""

import itertools
import sys
import networkx as nx
from pysat.solvers import Minisat22
from pysat.card import CardEnc, EncType
from pysat.formula import IDPool

# ---------- Graphs ----------
def build_G():
    G = nx.Graph()
    for j in (1, 2):
        for i in range(5):
            G.add_edge('x', f'u{i}^{j}')
            G.add_edge(f'u{i}^{j}', f'v{i}^{j}')
            G.add_edge(f'v{i}^{j}', f'v{(i+1)%5}^{j}')
        G.add_edge(f'z{j}', f'u0^{j}')
        G.add_edge(f'z{j}', f'u1^{j}')
    G.add_edge('z1', 'z2')
    return G

def build_H(with_z=False):
    H = nx.Graph()
    for i in range(5):
        H.add_edge('x', f'u{i}')
        H.add_edge(f'u{i}', f'v{i}')
        H.add_edge(f'v{i}', f'v{(i+1)%5}')
    if with_z:
        H.add_edge('z', 'u0')
        H.add_edge('z', 'u1')
    return H

G = build_G()
H = build_H()
Hz = build_H(with_z=True)

print("=== A. Structure of G ===", flush=True)
n, m = G.number_of_nodes(), G.number_of_edges()
planar, _ = nx.check_planarity(G)
triangles = list(nx.simple_cycles(G, length_bound=3))
girth = nx.girth(G)
print(f"vertices = {n} (claimed 23), edges = {m} (claimed 35)")
print(f"planar = {planar}")
print(f"triangles (3-cycles) = {triangles}  (must be empty)")
print(f"girth = {girth} (writeup concedes girth 4 via cycles x-u0-z-u1)",
      flush=True)
assert n == 23 and m == 35 and planar and not triangles and girth == 4

# ---------- Backtracking machinery (bitmask sets over colors 0..8) ----------
FULL = (1 << 9) - 1
P = (1 << 5) - 1          # colors {0..4} = phi(x), WLOG
Q = FULL ^ P              # colors {5..8}

TRIPLES = [sum(1 << c for c in comb)
           for comb in itertools.combinations(range(9), 3)]

def enumerate_colorings(graph, x_set, order, callback):
    """All proper set colorings with phi('x') = x_set fixed, every other
    vertex exactly 3 colors, adjacent sets disjoint. Calls callback(assign)
    on each solution; returns the number of solutions."""
    assert set(order) == set(graph.nodes) - {'x'}
    adj = {v: list(graph.neighbors(v)) for v in graph.nodes}
    # precompute per-vertex candidate lists (filter against pre-assigned x)
    cands = {v: ([t for t in TRIPLES if not (t & x_set)]
                 if 'x' in adj[v] else TRIPLES) for v in order}
    assign = {'x': x_set}
    found = [0]

    def bt(idx):
        if idx == len(order):
            found[0] += 1
            callback(dict(assign))
            return
        v = order[idx]
        forbidden = 0
        for u in adj[v]:
            if u in assign:
                forbidden |= assign[u]
        for t in cands[v]:
            if t & forbidden:
                continue
            assign[v] = t
            bt(idx + 1)
            del assign[v]

    bt(0)
    return found[0]

print("\n=== B. Lemma rigidity on single gadget H ===", flush=True)
stats = {'count': 0, 'violations': 0}

def check_lemma(phi):
    stats['count'] += 1
    ok = True
    q = {}
    for i in range(5):
        ui = phi[f'u{i}']
        # claim 1: phi(u_i) = Q minus exactly one color q_i
        if (ui & P) or bin(Q ^ ui).count('1') != 1:
            ok = False
        q[i] = Q ^ ui
        # claim 2: q_i in phi(v_i)
        if not (phi[f'v{i}'] & q[i]):
            ok = False
    for i in range(5):
        if q[i] == q[(i + 1) % 5]:                       # claim 3
            ok = False
        if (phi[f'u{i}'] | phi[f'u{(i+1)%5}']) != Q:     # consequence
            ok = False
    if not ok:
        stats['violations'] += 1

orderH = ['u0', 'u1', 'u2', 'u3', 'u4', 'v0', 'v1', 'v2', 'v3', 'v4']
enumerate_colorings(H, P, orderH, check_lemma)
print(f"proper colorings of H with phi(x)={{0..4}}, others exactly 3 colors: "
      f"{stats['count']}")
print(f"colorings violating any Lemma claim (1),(2),(3) or consequence: "
      f"{stats['violations']}", flush=True)
assert stats['count'] > 0, "gadget alone must be colorable"
assert stats['violations'] == 0, "Lemma fails!"

print("\n=== C. Decomposition check on G ===", flush=True)
z_sets = set()
orderHz = ['u0', 'u1', 'u2', 'u3', 'u4', 'z', 'v0', 'v1', 'v2', 'v3', 'v4']
total_Hz = enumerate_colorings(Hz, P, orderHz,
                               lambda phi: z_sets.add(phi['z']))
print(f"proper colorings of rooted gadget H+z with phi(x)={{0..4}}: {total_Hz}")
print(f"achievable phi(z) values: {len(z_sets)}")
all_in_P = all((t & Q) == 0 for t in z_sets)
print(f"every achievable phi(z) is a subset of P = phi(x): {all_in_P}")
disjoint_pair = any(a & b == 0 for a in z_sets for b in z_sets)
print(f"exists disjoint pair (phi_1(z), phi_2(z)): {disjoint_pair}")
colorable_G = disjoint_pair   # exact: copies share only x; z1z2 only cross edge
print(f"==> G admits the conjectured coloring: {colorable_G}", flush=True)

print("\n=== D. SAT double-check (no WLOG reductions) ===", flush=True)
def sat_colorable(graph, x_min, other_min, ncolors=9, x_name='x'):
    """SAT: does graph have a set coloring by subsets of [ncolors] with
    adjacent sets disjoint, |phi(v)| >= other_min for v != x_name and
    |phi(x_name)| >= x_min?"""
    pool = IDPool()
    var = {(v, c): pool.id(f'{v}|{c}')
           for v in graph.nodes for c in range(ncolors)}
    clauses = []
    for a, b in graph.edges:
        for c in range(ncolors):
            clauses.append([-var[(a, c)], -var[(b, c)]])
    for v in graph.nodes:
        lits = [var[(v, c)] for c in range(ncolors)]
        bound = x_min if v == x_name else other_min
        enc = CardEnc.atleast(lits=lits, bound=bound, vpool=pool,
                              encoding=EncType.seqcounter)
        clauses.extend(enc.clauses)
    with Minisat22(bootstrap_with=clauses) as s:
        return s.solve()

r_main = sat_colorable(G, x_min=5, other_min=3)
print(f"G, all >= 3, |phi(x)| >= 5 : SAT = {r_main}   (claim: UNSAT/False)")
r_ctrl1 = sat_colorable(G, x_min=4, other_min=3)
print(f"G, all >= 3, |phi(x)| >= 4 : SAT = {r_ctrl1}  (control, expect True)")
r_ctrl2 = sat_colorable(H, x_min=5, other_min=3)
print(f"H, all >= 3, |phi(x)| >= 5 : SAT = {r_ctrl2}  (control, expect True)",
      flush=True)

ok = (not colorable_G) and (not r_main) and r_ctrl1 and r_ctrl2
print("\nVERDICT:", "counterexample VERIFIED (no valid coloring of G exists)"
      if ok else "verification FAILED — see above")
sys.exit(0 if ok else 1)
