```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "Every claw-free cubic graph has an explicit signing of norm at most 1 + √3; the conjecture also holds for every regular graph admitting a partition into twin pairs.",
  "would_publish": false,
  "caveats": "The general non-bipartite case is not resolved; novelty of these special cases has not been checked; the substantive conjecture is interpreted for d >= 2."
}
```

# Two special cases

For a real symmetric signed adjacency matrix \(S\), the required quantity is
\[
\|S\|=\max_{\lambda\in\operatorname{Spec}(S)}|\lambda|.
\]
I work with finite simple graphs and the intended degree range \(d\ge 2\). At \(d=1\), \(K_2\) is a trivial exception to the displayed conjecture.

The principal result below is an elementary, constructive proof for **all claw-free cubic graphs**, with the stronger bound
\[
\boxed{\|S\|\le 1+\sqrt3<2\sqrt2.}
\]
Both ends of the spectrum are explicitly controlled.

A second result, using the bipartite MSS theorem, handles regular graphs partitionable into twin pairs. In particular, it removes the previous attempt’s large-blow-up requirement for **every even blow-up factor**. The relevant two-channel calculation is rederived below rather than assumed from that attempt.

I make no claim that these special cases are new.

## 1. Claw-free cubic graphs

Recall that a graph is claw-free if it has no induced \(K_{1,3}\).

### Theorem 1

Every finite simple claw-free \(3\)-regular graph has a symmetric signing \(S\) satisfying
\[
\|S\|\le 1+\sqrt3.
\]
Such a signing can be constructed in polynomial time.

### 1.1. Structural decomposition

First remove any components isomorphic to \(K_4\); these will be treated separately.

In a cubic claw-free graph, every vertex belongs to a triangle: otherwise its three neighbors would induce an independent set and form a claw with it.

Suppose two triangles share an edge \(uv\), and write their other vertices as \(p,q\). The four vertices induce either:

- \(K_4\), if \(pq\) is an edge; or
- a **diamond**, \(K_4-pq\), otherwise.

In the first case, cubicity makes this an entire \(K_4\) component. In the second case, \(u,v\) already have degree three inside the diamond. Each of \(p,q\), called its **tips**, has exactly one neighbor outside the diamond.

No triangle meeting this diamond can extend outside it. Indeed, a tip’s external neighbor cannot be adjacent to either central vertex, since those vertices already have degree three. Consequently, distinct diamonds are vertex-disjoint.

After removing all diamond vertices, the remaining vertices are covered by vertex-disjoint triangles. To see disjointness, two triangles sharing a vertex in a cubic graph necessarily share an edge, and hence would already belong to a diamond or a \(K_4\).

Thus every component under consideration is partitioned into:

- triangle blocks;
- diamond blocks.

The edges outside these blocks form a matching \(M\). They cover every triangle vertex and every diamond tip, and no diamond central vertex.

### 1.2. Boundary labels

Assign labels \(+\) and \(-\) to vertices incident with \(M\), subject to:

- the three vertices of each triangle receive the same label;
- the two tips of each diamond receive opposite labels.

Choose the diamond labels arbitrarily. Now choose the triangle labels so that
\[
\boxed{\text{each triangle has at most one incident matching edge with equally labelled ends.}}
\tag{1}
\]

This is always possible by a local-improvement algorithm. Start with arbitrary triangle labels. If a triangle has at least two such edges, reverse its label. If it had \(k\ge2\) equally labelled incident edges, this increases the number of oppositely labelled matching edges by
\[
k-(3-k)=2k-3>0.
\]
The process terminates after at most \(|M|\) flips. Its terminal labeling satisfies (1).

### 1.3. The signing

Give every edge of \(M\) sign \(+1\).

Inside each triangle, give all three edges sign equal to its common label.

Inside a diamond, order the vertices as
\[
u,v,p_+,p_-,
\]
where \(u,v\) are central and the subscripts specify the tip labels. Use the signed adjacency block
\[
F=
\begin{pmatrix}
0&1&1&1\\
1&0&1&-1\\
1&1&0&0\\
1&-1&0&0
\end{pmatrix}.
\tag{2}
\]
Thus the triangle through \(p_+\) has positive sign product, while the triangle through \(p_-\) has negative sign product.

Let \(C\) denote the resulting block-diagonal internal signed adjacency matrix. The full signed adjacency matrix is
\[
S=C+M.
\]

We next prove both spectral bounds.

### 1.4. A diagonal majorant for the external matching

Put
\[
r=\sqrt3,\qquad a=\frac1{\sqrt3},\qquad L=1+\sqrt3.
\]

Define a diagonal matrix \(D\), with diagonal zero on diamond central vertices. At an endpoint \(x\) of a matching edge \(xy\), set
\[
D_{xx}=
\begin{cases}
1,&x,y\text{ have the same label},\\
a,&x\text{ is labelled }+\text{ and }y\text{ is labelled }-,\\
r,&x\text{ is labelled }-\text{ and }y\text{ is labelled }+.
\end{cases}
\tag{3}
\]

For every matching edge \(xy\),
\[
D_{xx}D_{yy}=1.
\]
Its contribution to \(D-M\) is therefore
\[
\begin{pmatrix}
D_{xx}&-1\\
-1&D_{yy}
\end{pmatrix}\succeq0.
\]
Since matching edges have disjoint endpoints,
\[
D-M\succeq0.
\]
Here \(\succeq0\) denotes positive semidefiniteness. Consequently,
\[
S=C+M\preceq C+D.
\tag{4}
\]

It remains to bound each diagonal block of \(C+D\).

### 1.5. Triangle blocks

For a positively labelled triangle, condition (1) implies that, after permuting its vertices,
\[
D|_{\triangle}\preceq\operatorname{diag}(1,a,a).
\]
Thus its block in \(C+D\) is bounded above by
\[
P=
\begin{pmatrix}
1&1&1\\
1&a&1\\
1&1&a
\end{pmatrix}.
\]

On the antisymmetric vector \((0,1,-1)\), the eigenvalue is \(a-1\). On the complementary invariant subspace, the matrix is
\[
\begin{pmatrix}
1&\sqrt2\\
\sqrt2&1+a
\end{pmatrix}.
\]
Its largest eigenvalue is
\[
\frac{2+a+\sqrt{a^2+8}}2
=
\frac{2+1/\sqrt3+5/\sqrt3}{2}
=1+\sqrt3=L.
\]
Hence \(P\preceq LI\).

For a negatively labelled triangle, its internal matrix is \(I-J\), where \(J\) is the all-ones matrix. Since \(D|_{\triangle}\preceq rI\),
\[
C|_{\triangle}+D|_{\triangle}
\preceq (1+r)I-J
\preceq LI.
\tag{5}
\]

### 1.6. Diamond blocks

On a diamond, write the tip weights as \(w_+,w_-\). Equation (3) gives
\[
w_+\le1,\qquad w_-\le r.
\tag{6}
\]

Make the orthogonal change of basis
\[
\frac1{\sqrt2}
\begin{pmatrix}
1&1\\
1&-1
\end{pmatrix}
\]
on the two central coordinates, leaving the tips unchanged. After reordering coordinates, \(F+D|_{\diamond}\) becomes the direct sum
\[
\begin{pmatrix}
1&\sqrt2\\
\sqrt2&w_+
\end{pmatrix}
\oplus
\begin{pmatrix}
-1&\sqrt2\\
\sqrt2&w_-
\end{pmatrix}.
\tag{7}
\]

The first block has largest eigenvalue at most
\[
1+\sqrt2<L.
\]
For the second, it is enough to take \(w_-=r\). The difference from \(LI\) is
\[
\begin{pmatrix}
L+1&-\sqrt2\\
-\sqrt2&L-r
\end{pmatrix}
=
\begin{pmatrix}
r+2&-\sqrt2\\
-\sqrt2&1
\end{pmatrix},
\]
whose determinant is \(r>0\), with positive diagonal entries. It is positive definite.

Thus every diamond block is also bounded above by \(LI\). Together with (4)–(5),
\[
\lambda_{\max}(S)\le L.
\tag{8}
\]

### 1.7. The other end of the spectrum

We must separately prove
\[
\lambda_{\max}(-S)\le L.
\]

Reverse every boundary label and define \(D'\) by the same rule (3). Equality or inequality of endpoint labels is unchanged, so property (1) remains true. For every matching edge, the corresponding block of \(D'+M\) is positive semidefinite. Therefore
\[
-S=-C-M\preceq -C+D'.
\tag{9}
\]

The triangle estimates apply verbatim: their internal signs and labels have both reversed.

For a diamond, the old positive tip now has weight at most \(r\), and the old negative tip has weight at most \(1\). Under the same central change of basis, the two blocks for \(-F+D'\) are bounded above by
\[
\begin{pmatrix}
-1&-\sqrt2\\
-\sqrt2&r
\end{pmatrix},
\qquad
\begin{pmatrix}
1&-\sqrt2\\
-\sqrt2&1
\end{pmatrix}.
\]
These have exactly the eigenvalue bounds used in (7); the signs of their off-diagonal entries do not affect their spectra. Hence
\[
\lambda_{\max}(-S)\le L.
\tag{10}
\]

Equations (8) and (10) prove \(\|S\|\le L\).

### 1.8. The \(K_4\) components

Sign exactly one edge of \(K_4\) negatively. Its spectrum is
\[
\{-\sqrt5,-1,1,\sqrt5\}.
\]

For completeness, partition the vertices into the endpoints of the negative edge and the other two vertices. The antisymmetric vectors within those pairs have eigenvalues \(1,-1\), while the subspace constant on each pair has matrix
\[
\begin{pmatrix}
-1&2\\
2&1
\end{pmatrix},
\]
with eigenvalues \(\pm\sqrt5\).

These components therefore also satisfy the claimed bound. Finally,
\[
(1+\sqrt3)^2=4+2\sqrt3<8.
\]
This proves Theorem 1, including the conjectured cubic bound. \(\square\)

## 2. Regular graphs with twin pairs

Two vertices \(u,v\) are twins if
\[
N(u)\setminus\{v\}=N(v)\setminus\{u\}.
\]
They may be adjacent or nonadjacent.

The following result strengthens the blow-up direction of the previous attempt.

### Theorem 2

Let \(G\) be \(d\)-regular, where \(d\ge1\), and let \(\varepsilon\in\{0,1\}\). Replace each vertex by:

- two independent vertices if \(\varepsilon=0\);
- a copy of \(K_2\) if \(\varepsilon=1\);

and replace every original edge by all four edges between its two vertex pairs. Denote the resulting \((2d+\varepsilon)\)-regular graph by \(G[2;\varepsilon]\).

It has a symmetric signing \(S\) satisfying
\[
\boxed{
\|S\|^2\le
\begin{cases}
4+\varepsilon,&d=1,2,\\[2mm]
16\bigl(\lceil d/2\rceil-1\bigr)+\varepsilon,&d\ge3.
\end{cases}}
\tag{11}
\]
In every case,
\[
\|S\|\le2\sqrt{2d+\varepsilon-1}.
\]

### 2.1. The bipartite input

I use the bipartite MSS signing theorem supplied in the question, in the following equivalent maximum-degree form:

> A bipartite graph of maximum degree at most \(k\ge2\) has a signing of norm at most \(2\sqrt{k-1}\).

Here is a reduction from the regular version, so no additional signing theorem is required. Given a bipartite graph of maximum degree \(k\), take a disjoint copy with the bipartition reversed. Join each deficient-degree vertex to its copy. This increases every degree below \(k\) by one, preserves bipartiteness and simplicity, and leaves the original graph induced. Repeating at most \(k\) times produces a \(k\)-regular bipartite supergraph. Restrict an MSS signing of that graph to the original vertices.

For \(k=1\), the graph is a matching together with isolated vertices, and its norm is at most \(1\).

### 2.2. Balanced orientation

Orient \(G\) so that
\[
\deg^+(v),\deg^-(v)\le k:=\left\lceil\frac d2\right\rceil.
\tag{12}
\]
For even \(d\), Euler orientations do this. For odd \(d\), pair the vertices within each component, add those pairing edges temporarily, orient the resulting even-degree multigraph along Euler tours, and delete the added edges.

Construct an auxiliary bipartite graph \(F\) with vertex classes
\[
\{v_+:v\in V(G)\},\qquad \{v_-:v\in V(G)\}.
\]
For every oriented edge \(u\to v\), put the edge \(u_+v_-\) in \(F\). By (12), \(F\) has maximum degree at most \(k\).

Choose a signing of \(F\), and write its signed biadjacency matrix as \(T\). Thus
\[
\|T\|\le
\begin{cases}
1,&k=1,\\
2\sqrt{k-1},&k\ge2.
\end{cases}
\tag{13}
\]

### 2.3. Two orthogonal channels

Set
\[
h_+=\binom11,\qquad h_-=\binom1{-1},\qquad
Q=\frac1{\sqrt2}
\begin{pmatrix}
1&1\\
1&-1
\end{pmatrix}.
\]

For an oriented edge \(u\to v\), whose auxiliary edge has sign \(s_{uv}\), use the block
\[
B_{uv}=s_{uv}h_+h_-^{\mathsf T},
\qquad
B_{vu}=B_{uv}^{\mathsf T}.
\tag{14}
\]
Every entry of \(B_{uv}\) is \(1\) or \(-1\), as required.

Inside every vertex pair, use
\[
\varepsilon
\begin{pmatrix}
0&1\\
1&0
\end{pmatrix}.
\tag{15}
\]
Equations (14)–(15) define a symmetric signing \(S\) of \(G[2;\varepsilon]\).

Apply \(Q\) within every pair. The edge block in (14) becomes
\[
Q^{\mathsf T}B_{uv}Q
=2s_{uv}e_+e_-^{\mathsf T},
\]
while (15) becomes \(\operatorname{diag}(\varepsilon,-\varepsilon)\).

Ordering all \(+\) coordinates before all \(-\) coordinates, the transformed matrix is therefore
\[
S'\;=\;
\begin{pmatrix}
\varepsilon I&2T\\
2T^{\mathsf T}&-\varepsilon I
\end{pmatrix}.
\tag{16}
\]
In particular,
\[
(S')^2=
\begin{pmatrix}
\varepsilon I+4TT^{\mathsf T}&0\\
0&\varepsilon I+4T^{\mathsf T}T
\end{pmatrix},
\]
because \(\varepsilon^2=\varepsilon\). Hence
\[
\boxed{\|S\|^2=\varepsilon+4\|T\|^2.}
\tag{17}
\]
Combining (13) and (17) proves (11).

For \(d\ge3\),
\[
16\bigl(\lceil d/2\rceil-1\bigr)+\varepsilon
\le 8d-8+\varepsilon
<8d-4+4\varepsilon
=4(2d+\varepsilon-1).
\]
The cases \(d=1,2\) follow directly from the first line of (11). This proves the theorem. \(\square\)

### Corollary 2.1: arbitrary twin-pair partitions

Every regular graph of degree at least two whose vertices can be partitioned into twin pairs satisfies the conjecture.

Indeed, between two distinct twin pairs there are either all four possible edges or none. If the common degree is \(D\), a pair with internal-edge indicator \(\varepsilon_v\) satisfies
\[
D=2\deg_G(v)+\varepsilon_v
\]
in the quotient graph. Parity forces all \(\varepsilon_v\) to be equal. The quotient is therefore regular, and Theorem 2 applies.

### Corollary 2.2: every even independent-set blow-up

Let \(G\) be any \(d\)-regular graph with \(d\ge1\), and let \(t\ge2\) be even. Then its independent-set \(t\)-blow-up \(G^{(t)}\) satisfies the conjecture.

Writing \(t=2m\),
\[
G^{(t)}=\bigl(G^{(m)}\bigr)[2;0].
\]
Thus there is no requirement such as \(t\ge d\).

This still concerns blow-ups, not lifts: the resulting degree is \(dt\).

## 3. What is and is not established

The first theorem covers all claw-free cubic graphs, including ones with diamonds, bridges, or non-bipartite quotient structure. Its proof is self-contained. In particular, its lower spectral bound is not being inferred from a one-sided interlacing statement.

The second theorem uses MSS only on a genuinely bipartite auxiliary graph. The two-sided conclusion follows from the exact squared-matrix identity (17).

Neither argument settles the original conjecture:

- A general cubic graph need not admit the triangle–diamond decomposition.
- A general regular graph need not have twin pairs.
- Restricting the signing of \(G^{(2)}\) to one vertex from each pair does not repair this. The available norm bound is asymptotically \(2\sqrt{2d}\), whereas the original graph requires \(2\sqrt{d-1}\).

Thus these are complete special-case arguments, not a proof for arbitrary non-bipartite regular graphs. I have not checked whether either special case already appears in the literature, and would not present this as a publication-ready advance without that check.