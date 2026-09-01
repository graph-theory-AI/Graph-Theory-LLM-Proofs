```json
{
  "verdict": "disproved",
  "confidence": "high",
  "one_line": "The planar dual of Tutte's 46-vertex non-Hamiltonian cubic polyhedral graph is a 25-vertex triangulation with fractional vertex-arboricity at least 88/43>2.",
  "would_publish": false,
  "caveats": "This uses the standard LP definition of fractional vertex-arboricity and the classical verified non-Hamiltonicity of the explicit Tutte graph; publication priority has not been checked."
}
```

# Statement

Under the standard definition, let \(\mathcal F(G)\) be the family of vertex sets inducing forests in \(G\). Then
\[
\operatorname{va}_f(G)=
 \min\left\{
 \sum_{F\in\mathcal F(G)}x_F:
 x_F\ge 0,\ 
 \sum_{F\ni v}x_F\ge 1\ \text{for every }v
 \right\}.
\]
Its LP dual is
\[
\operatorname{va}_f(G)=
 \max\left\{
 \sum_{v\in V(G)}z_v:
 z_v\ge 0,\ 
 \sum_{v\in F}z_v\le 1\ \text{for every }F\in\mathcal F(G)
 \right\}.
\]

I will prove the following stronger statement.

## Proposition

Let \(G\) be a simple plane triangulation on \(n\ge 4\) vertices. If \(G\) is not vertex-2-arborable, then
\[
\operatorname{va}_f(G)\ge
\frac{4n-12}{2n-7}
=2+\frac{2}{2n-7}>2.
\]

Consequently, the dual of any non-Hamiltonian cubic polyhedral graph is a counterexample to Conjecture 1.1.

# 1. A degree-weight inequality for triangulations

For \(v\in V(G)\), set
\[
w(v)=d_G(v)-2.
\]
Since \(G\) is a triangulation on at least four vertices, \(d_G(v)\ge3\), so these weights are positive. As
\[
|E(G)|=3n-6,
\]
their total is
\[
W:=\sum_{v\in V(G)}w(v)
 =2|E(G)|-2n
 =4n-12.
\]

Let \(F\subseteq V(G)\) induce a nonempty forest with \(c(F)\) components, and let \(\delta(F)\) denote the set of edges with exactly one endpoint in \(F\). Since
\[
|E(G[F])|=|F|-c(F),
\]
we have
\[
\begin{aligned}
w(F)
 &=\sum_{v\in F}(d_G(v)-2)\\
 &=2|E(G[F])|+|\delta(F)|-2|F|\\
 &=|\delta(F)|-2c(F).
\end{aligned}
\]

The graph consisting of the edges \(\delta(F)\) is a simple bipartite planar graph on at most \(n\) nonisolated vertices and hence
\[
|\delta(F)|\le 2n-4.
\]
Therefore
\[
w(F)\le 2n-4-2c(F)\le 2n-6=\frac W2.
\tag{1}
\]

Thus \(w/(\,2n-6\,)\) is always a feasible dual weighting, showing in particular that every plane triangulation has fractional vertex-arboricity at least \(2\).

# 2. Characterizing equality

We next show that equality in (1) is possible precisely when \(G\) can be partitioned into two induced trees.

Suppose that an induced forest \(F\) satisfies
\[
w(F)=2n-6.
\]
Every inequality above is then an equality. Hence

1. \(G[F]\) is connected, so it is a tree;
2. \(|\delta(F)|=2n-4\).

A triangulation has \(2n-4\) faces. Every facial triangle contains either zero or two edges of the cut \(\delta(F)\). Counting incidences between cut edges and faces gives
\[
\sum_{\text{faces }Q}|\delta(F)\cap E(Q)|
 =2|\delta(F)|
 =4n-8
 =2(2n-4).
\]
Since each summand is at most two, every facial triangle contains exactly two cut edges. In particular, every face meets both \(F\) and \(S:=V(G)\setminus F\).

Now
\[
\begin{aligned}
|E(G[S])|
 &= (3n-6)-(2n-4)-(|F|-1)\\
 &=n-|F|-1\\
 &=|S|-1.
\end{aligned}
\tag{2}
\]

Moreover, \(G[S]\) contains no cycle. Indeed, if \(C\) were a cycle in \(G[S]\), then the connected graph \(G[F]\), being disjoint from the Jordan curve \(C\), would lie entirely on one side of \(C\). The other side contains at least one facial triangle of the triangulation, all of whose vertices would lie in \(S\), contradicting the fact that every face meets \(F\).

Thus \(G[S]\) is a forest, and (2) shows that it is connected. Hence it is a tree.

Conversely, if \(V(G)=A\sqcup B\) with both \(G[A]\) and \(G[B]\) forests, then writing their numbers of components as \(c_A,c_B\),
\[
|E(G[A])|+|E(G[B])|
 =n-c_A-c_B.
\]
Thus
\[
|\delta(A)|=3n-6-(n-c_A-c_B)
           =2n-6+c_A+c_B.
\]
The bipartite planar bound gives \(|\delta(A)|\le2n-4\), so \(c_A+c_B\le2\). Both sets are nonempty, hence \(c_A=c_B=1\). Therefore both color classes are trees, and either class attains equality in (1).

We have proved:

\[
\boxed{
\text{A plane triangulation has an induced forest of weight }W/2
\iff
\operatorname{va}(G)\le2.
}
\tag{3}
\]

# 3. Strict fractional lower bound

If \(G\) is not vertex-2-arborable, (3) says that equality in (1) never occurs. Since all weights are integral,
\[
w(F)\le 2n-7
\qquad
\text{for every induced forest }F.
\]
Consequently,
\[
z_v:=\frac{d_G(v)-2}{2n-7}
\]
is feasible for the dual LP. Its objective value is
\[
\sum_v z_v
 =\frac{4n-12}{2n-7}
 =2+\frac{2}{2n-7}>2.
\]
This proves the proposition.

In particular, for triangulations there is no fractional relaxation at the threshold \(2\):
\[
\operatorname{va}_f(G)\le2
\quad\Longleftrightarrow\quad
\operatorname{va}(G)\le2.
\tag{4}
\]

# 4. An explicit planar counterexample

Let \(H\) be the classical Tutte graph: Tutte's explicit simple, 3-connected, cubic planar graph on \(46\) vertices having no Hamiltonian cycle. This is the standard counterexample to Tait's Hamiltonicity assertion; see W. T. Tutte, *On Hamiltonian circuits*, J. London Math. Soc. 21 (1946), 98–101.

Let
\[
G=H^*
\]
be its plane dual. Because \(H\) is cubic and polyhedral, \(G\) is a simple plane triangulation. Since
\[
|V(H)|=46,\qquad |E(H)|=69,
\]
Euler's formula gives
\[
|V(G)|=|F(H)|=69-46+2=25.
\]

It remains to see that \(G\) is not vertex-2-arborable. Suppose that
\[
V(G)=A\sqcup B
\]
with both color classes inducing forests. By the equality argument above, both induced forests are trees and every facial triangle of \(G\) is bichromatic. Therefore the duals of the cut edges \(\delta(A)\) have degree two at every vertex of \(H\). Since both \(G[A]\) and \(G[B]\) are connected, \(\delta(A)\) is a bond, so its dual is one cycle rather than a disjoint union of cycles. It passes through every dual vertex and is consequently a Hamiltonian cycle of \(H\), contradicting the defining property of the Tutte graph.

Thus \(\operatorname{va}(G)>2\). Applying the proposition with \(n=25\) gives
\[
\boxed{
\operatorname{va}_f(G)
 \ge \frac{4\cdot25-12}{2\cdot25-7}
 =\frac{88}{43}
 >2.
}
\]

Equivalently, the explicit dual LP certificate is
\[
z_v=\frac{d_G(v)-2}{43}.
\]
Every induced forest \(F\) satisfies \(\sum_{v\in F}(d_G(v)-2)\le43\), while
\[
\sum_{v\in V(G)}(d_G(v)-2)=88.
\]

Hence \(G\), the 25-vertex planar dual of the Tutte graph, disproves Conjecture 1.1.

# 5. Reproducible identification of the graph

The standard Tutte graph is also the graph returned by `networkx.tutte_graph()`. Since it is 3-connected, its planar embedding is unique up to reflection, so taking the planar dual is unambiguous up to isomorphism. The following constructs the 25-vertex graph:

```python
import networkx as nx

H = nx.tutte_graph()
assert H.number_of_nodes() == 46
assert H.number_of_edges() == 69
assert set(dict(H.degree()).values()) == {3}

planar, emb = nx.check_planarity(H)
assert planar

seen = set()
faces = []
halfedge_face = {}

for u in H:
    for v in emb.neighbors_cw_order(u):
        if (u, v) not in seen:
            face = emb.traverse_face(u, v, seen)
            i = len(faces)
            faces.append(face)
            for j in range(len(face)):
                a = face[j]
                b = face[(j + 1) % len(face)]
                halfedge_face[(a, b)] = i

G = nx.Graph()
G.add_nodes_from(range(len(faces)))
for u, v in H.edges():
    G.add_edge(halfedge_face[(u, v)],
               halfedge_face[(v, u)])

assert G.number_of_nodes() == 25
assert G.number_of_edges() == 69
assert nx.check_planarity(G)[0]
```

No computational assertion about fractional vertex-arboricity is needed: the weighting argument above is an exact certificate.

# Gaps and status

There is no mathematical gap provided that the catalog uses the standard fractional-cover definition stated at the beginning. The only external input is the classical proved fact that the explicit Tutte graph is cubic, polyhedral, and non-Hamiltonian. I have not checked whether this short disproof has already appeared in comments, an erratum, or subsequent literature.