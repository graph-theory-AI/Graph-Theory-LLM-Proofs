"""Verify the concrete claims of attacks_retry/2509.09031__00/output.md Sections 4-6
on small explicit instances.

H = incidence graph of PG(2,3): 26 vertices, 4-regular, bipartite, girth 6.
    (A legitimate stand-in for the Cayley graph H_g of Section 4; we also check
     the Section-4 Cayley recipe separately in check_cayley.py.)
"""
import itertools, random
import networkx as nx
from build_instance import girth, mono_cycle_lengths, build_Hplus, build_G


# ---------- H : incidence graph of PG(2,3) ----------
def pg23_incidence():
    pts = []
    seen = set()
    for v in itertools.product(range(3), repeat=3):
        if v == (0, 0, 0):
            continue
        # normalise: first nonzero coordinate = 1
        for c in v:
            if c:
                inv = 1 if c == 1 else 2
                break
        w = tuple((x * inv) % 3 for x in v)
        if w not in seen:
            seen.add(w); pts.append(w)
    G = nx.Graph()
    for p in pts:
        for l in pts:
            if sum(a * b for a, b in zip(p, l)) % 3 == 0:
                G.add_edge(('P',) + p, ('L',) + l)
    return G


def two_factorisation(G, seed=0):
    """Petersen: split a 4-regular graph into two 2-factors via an Eulerian
    orientation + bipartite perfect matching."""
    rng = random.Random(seed)
    # Eulerian orientation
    M = nx.MultiGraph(G)
    orient = []
    for comp in nx.connected_components(M):
        sub = nx.MultiGraph(M.subgraph(comp))
        circ = list(nx.eulerian_circuit(sub))
        orient.extend(circ)
    # bipartite graph out/in
    B = nx.Graph()
    for (u, v) in orient:
        B.add_edge(('o', u), ('i', v))
    match = nx.algorithms.bipartite.maximum_matching(B, top_nodes=[n for n in B if n[0] == 'o'])
    red, blue = set(), set()
    for (u, v) in orient:
        e = (min(u, v), max(u, v))
        if match.get(('o', u)) == ('i', v):
            red.add(e)
        else:
            blue.add(e)
    return red, blue


def _main():
    pass

H = pg23_incidence()
n = H.number_of_nodes()
print(f"H: n={n}, edges={H.number_of_edges()}, degrees={set(dict(H.degree()).values())}, girth={girth(H)}")
red, blue = two_factorisation(H)
print(f"|red|={len(red)} |blue|={len(blue)}  (need {n} each)")
Sr = nx.Graph(); Sr.add_nodes_from(H); Sr.add_edges_from(red)
Sb = nx.Graph(); Sb.add_nodes_from(H); Sb.add_edges_from(blue)
print("red degrees", set(dict(Sr.degree()).values()), "blue degrees", set(dict(Sb.degree()).values()))
print("red cycle lengths", mono_cycle_lengths(H, red), "blue cycle lengths", mono_cycle_lengths(H, blue))

# ---------- check p : G -> H+ is an onto (2,1)-quasi-isometry ----------
def check_qi(H, red, blue, S, M, sample=None):
    Hp = build_Hplus(H, S, M)
    G = build_G(H, red, blue, S, M)

    def p(x):
        if x[0] == 'B':
            return ('B', x[1])
        tag = x[1]
        u, v = tag
        # corridor internal vertex i of corridor (u,v) in G  ->  same in H+
        return ('I', u, v, x[2])

    img = {p(x) for x in G}
    onto = img == set(Hp.nodes())
    dG = dict(nx.all_pairs_shortest_path_length(G))
    dH = dict(nx.all_pairs_shortest_path_length(Hp))
    nodes = list(G.nodes())
    if sample and len(nodes) > sample:
        nodes = random.Random(1).sample(nodes, sample)
    worst_up = worst_lo = 0
    for i, x in enumerate(nodes):
        for y in nodes[i:]:
            a = dG[x][y]; b = dH[p(x)][p(y)]
            worst_up = max(worst_up, b - a)              # need b <= 2a+1
            worst_lo = max(worst_lo, a - (2 * b + 1))     # need a <= 2b+1
    return onto, worst_up, worst_lo, G.number_of_nodes(), Hp.number_of_nodes()

if __name__ == '__main__':
  for (S, M) in [(3, 5), (4, 9), (6, 11)]:
    onto, wu, wl, gn, hn = check_qi(H, red, blue, S, M, sample=None)
    print(f"S={S} M={M}: |V(G)|={gn} |V(H+)|={hn} onto={onto} "
          f"max(d_H+ - d_G)={wu} (must be <=0)  max(d_G - (2 d_H+ +1))={wl} (must be <=0)")
