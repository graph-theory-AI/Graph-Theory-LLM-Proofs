```json
{
  "verdict": "partial",
  "confidence": "medium",
  "one_line": "Every locally finite simple half-plane triangulation admits an acyclic interior Schnyder prewood and a finite-flip-extremal (3,2)-orientation, but the boundary coloring and at-infinity maximality of a genuine half-plane Schnyder wood remain unresolved.",
  "would_publish": false,
  "caveats": "The catalog excerpt omits the formal half-plane definitions; the results below concern standard finitary relaxations and exclude non-simple or non-locally-finite triangulations."
}
```

# 1. Scope and conventions

The excerpt does not reproduce the source paper’s formal definition of a half-plane Schnyder wood. This matters: in the infinite setting, one may require only the usual local orientation/color rules, or additionally require monochromatic rays to coalesce, to converge to prescribed ends, or maximality in a global order allowing changes at infinity. These notions are not equivalent.

I therefore do not claim to settle the stated problem. I prove two precise relaxations showing that there is no finite Eulerian, local-coloring, or finite-cycle obstruction in the locally finite simple case.

A **simple locally finite half-plane triangulation** is a connected simple plane graph \(T\), embedded in the closed upper half-plane, whose outer boundary is a double ray
\[
B=\ldots b_{-1}b_0b_1\ldots
\]
and whose other faces are triangles. All vertex degrees are finite.

# 2. A finite-flip-extremal \((3,2)\)-orientation

Define
\[
\alpha(v)=
\begin{cases}
3,&v\notin B,\\
2,&v\in B.
\end{cases}
\]
An \(\alpha\)-orientation directs every edge exactly once and has
\(d^+(v)=\alpha(v)\) at every vertex.

Call such an orientation **finitely upper-extremal** if it has no finite simple cycle directed clockwise. Reversing “clockwise” throughout gives the corresponding lower-extremal notion.

## Theorem 2.1

Every simple locally finite half-plane triangulation has both a finitely upper-extremal and a finitely lower-extremal \((3,2)\)-orientation.

The targets \(3\) and \(2\) arise naturally from Euler’s formula. If \(G\) is a finite triangulation of a disk with \(I\) interior vertices and boundary length \(p\), then
\[
|E(G)|=3I+2p-3.
\]
Thus one can prescribe outdegree \(3\) internally, outdegree \(2\) at boundary vertices, and place the three missing units at three exceptional boundary vertices. In the half-plane, those three exceptional vertices can be sent to infinity.

## 2.1 Finite disk lemma

Let \(G\) be a finite simple triangulation of a disk, with boundary cycle \(C\), and let \(R\subseteq V(C)\) consist of three distinct vertices. Put
\[
\alpha_R(v)=
\begin{cases}
3,&v\notin C,\\
2,&v\in C\setminus R,\\
1,&v\in R.
\end{cases}
\]

### Lemma 2.2

The graph \(G\) has an \(\alpha_R\)-orientation.

### Proof

We use the following elementary orientation criterion.

A finite graph \(H\) has an orientation with prescribed outdegrees
\(\beta(v)\) if and only if
\[
\sum_{v\in V(H)}\beta(v)=|E(H)|
\tag{2.1}
\]
and
\[
|E(H[X])|\leq \sum_{v\in X}\beta(v)
\quad\text{for every }X\subseteq V(H).
\tag{2.2}
\]
Indeed, make one node for each edge, \(\beta(v)\) slots at each vertex \(v\), and join an edge-node to the slots belonging to its two endpoints. A matching of all edge-nodes chooses the tail of every edge. Conditions (2.1)–(2.2) are precisely Hall’s condition; for a set \(F\) of edge-nodes, put \(X=V(F)\) and use
\[
|F|\leq |E(H[X])|\leq \beta(X).
\]

For \(G\), Euler’s formula gives
\[
|E(G)|=3I+2|C|-3=\sum_v\alpha_R(v).
\]

It remains to prove (2.2). Consider a connected component \(K\) of \(G[X]\), with
\[
n=|V(K)|,\qquad
b=|V(K)\cap V(C)|,\qquad
r=|V(K)\cap R|.
\]
If \(n\geq 3\), all \(b\) vertices inherited from \(C\) are incident with the outer face of \(K\). If \(e\) is the number of edges of \(K\) and \(f\) its number of bounded faces, then
\[
f=e-n+1.
\]
Every bounded face has boundary length at least three, while the outer facial walk contains all \(b\) distinguished boundary vertices. Hence
\[
2e\geq b+3f=b+3(e-n+1),
\]
so
\[
e\leq 3n-b-3.
\]
On the other hand,
\[
\alpha_R(V(K))=3n-b-r.
\]
Since \(r\leq3\),
\[
e\leq 3n-b-3\leq 3n-b-r=\alpha_R(V(K)).
\]
Components with one or two vertices satisfy the inequality directly. Summing over the components of \(G[X]\) proves (2.2). ∎

### Lemma 2.3

Among the \(\alpha_R\)-orientations of \(G\), there is one with no clockwise directed simple cycle, and one with no counterclockwise directed simple cycle.

### Proof

Fix one \(\alpha_R\)-orientation \(O_0\). The difference between any other \(\alpha_R\)-orientation \(O\) and \(O_0\), divided by two in the usual signed-edge representation, is an integral circulation: equality of the outdegrees implies zero divergence at every vertex.

For a finite plane graph, every integral circulation has a face potential \(h_O\), normalized by \(h_O(f_\infty)=0\). Choose the sign convention so that reversing a clockwise directed simple cycle increases \(h_O\) by one on every face inside that cycle.

The set of \(\alpha_R\)-orientations is finite. Choose \(O\) maximizing
\[
H(O)=\sum_{f\neq f_\infty}h_O(f).
\]
If \(O\) contained a clockwise directed cycle \(C\), reversing \(C\) would preserve every outdegree and would strictly increase \(H\), a contradiction. Minimizing the same functional gives the opposite extremum. ∎

## 2.2 Protected finite completions

We need a standard planar completion observation.

### Lemma 2.4

Let \(W\) be a finite vertex set in \(T\), and let \(L\) be a finite subgraph. There is a finite simple disk triangulation \(G\) containing \(L\) and every edge incident with \(W\), such that:

1. no new edge is incident with a vertex of \(W\);
2. vertices of \(W\cap B\) remain boundary vertices of \(G\);
3. vertices of \(W\setminus B\) are interior vertices of \(G\);
4. the boundary of \(G\) contains at least three fresh vertices.

### Proof sketch

Include the closed stars of all vertices in \(W\), and include a sufficiently long interval of \(B\) containing every boundary vertex under consideration strictly between its endpoints. The resulting plane graph is finite because \(T\) is locally finite.

Join the endpoints of the chosen boundary interval by a new arc through fresh vertices, drawn above the finite retained subgraph, thereby forming an outer cycle. Triangulate every remaining bounded region using fresh vertices and edges. Since the entire closed star of every protected interior vertex was retained, every face incident with it is already triangular. At a protected boundary vertex, the outer cycle follows the original boundary, and all regions on the interior side are likewise already triangulated. Thus no new edge need be added at a protected vertex.

If a complementary region has a nonsimple facial walk, first add a fresh collar inside it and then triangulate the resulting simple polygons. This also avoids loops and multiple edges. Subdividing the new closing arc supplies three fresh boundary vertices. ∎

## 2.3 Compactness proof of Theorem 2.1

Let
\[
\Omega=\prod_{e\in E(T)}\{\text{the two orientations of }e\}.
\]
This is compact.

For every vertex \(v\), let \(A_v\subseteq\Omega\) be the condition
\[
d^+(v)=\alpha(v).
\]
Because \(T\) is locally finite, \(A_v\) is a clopen cylinder condition.

For every finite simple cycle \(C\), let \(D_C\) be the condition that \(C\) is not directed clockwise. This is also clopen.

Consider finitely many constraints \(A_v\) and \(D_C\). Apply Lemma 2.4 with the constrained vertices protected and all constrained cycles retained. Choose the three exceptional vertices \(R\) among fresh boundary vertices of the finite completion. By Lemmas 2.2 and 2.3, the completion has an \(\alpha_R\)-orientation with no clockwise directed cycle. At every protected vertex, \(\alpha_R\) agrees with the desired half-plane target \(3\) or \(2\). Restrict this orientation to the retained edges and orient all other edges of \(T\) arbitrarily.

Thus every finite family of the conditions \(\{A_v,D_C\}\) is simultaneously satisfiable. Compactness gives
\[
\bigcap_v A_v\cap\bigcap_C D_C\neq\varnothing.
\]
This proves the upper-extremal assertion. The lower-extremal assertion is identical. ∎

# 3. An acyclic interior Schnyder prewood

There is also no obstruction to satisfying all ordinary Schnyder rules away from the infinite boundary.

A **Schnyder interior prewood** is an orientation and color in
\(\{0,1,2\}\) of every edge such that, at every interior vertex:

1. exactly one edge of each color points out;
2. the three outgoing edges occur in the prescribed cyclic color order;
3. incoming edges of color \(i\) lie in the usual sector between the two other outgoing colors.

No rule is imposed at boundary vertices. Call it **acyclic** if there is no finite monochromatic directed cycle.

## Proposition 3.1

Every simple locally finite half-plane triangulation has an acyclic Schnyder interior prewood.

### Proof

Give every edge one of the six possible oriented-color states. The product of these finite state spaces is compact.

The Schnyder rule at any fixed interior vertex is a cylinder condition because the degree is finite. The condition that a fixed cycle is not a monochromatic directed cycle is also a cylinder condition.

Take finitely many such conditions. Retain all involved edges and the closed stars of all involved interior vertices. Enclose this finite plane subgraph inside a new triangular outer face and triangulate the complementary regions without adding edges at the protected vertices. The resulting finite plane triangulation has an ordinary finite Schnyder wood. Its restriction satisfies all the selected local rules. Moreover, a color class in a finite Schnyder wood is directed toward its corresponding outer root, so it contains no monochromatic directed cycle.

The finite intersection property and compactness now give a labeling satisfying every interior rule and forbidding every finite monochromatic directed cycle. ∎

Consequently, each monochromatic path starting at an interior vertex either reaches the boundary or continues as an infinite ray. What has not been proved is that rays of the same color coalesce, have prescribed ends, or satisfy any source-specific boundary rule.

# 4. The only possible discrepancy between finite-flip extrema is at infinity

The following observation pinpoints why the finite uniqueness argument breaks down.

## Proposition 4.1

Let \(O\) and \(O'\) be two \((3,2)\)-orientations of \(T\), both having no clockwise directed finite cycle. If \(O\neq O'\), then their disagreement contains a directed double ray.

### Proof

Let \(D\) consist of the edges on which \(O\) and \(O'\) differ, directed as in \(O\). At every vertex,
\[
d_D^+(v)=d_D^-(v),
\]
because \(O\) and \(O'\) have the same prescribed outdegree.

Suppose \(D\) contained a directed finite cycle \(C\). The cycle is directed one way in \(O\) and the opposite way in \(O'\). If it is clockwise in \(O\), then \(O\) is forbidden; if it is counterclockwise in \(O\), then its reverse is clockwise in \(O'\). Thus \(D\) has no directed finite cycle.

Start with any edge of \(D\). Balance lets one continue indefinitely both forward and backward. Local finiteness, together with the absence of a directed cycle, ensures that neither continuation repeats a vertex and that the two continuations do not meet again. Their union is a directed double ray. ∎

On a finite graph, a nonempty balanced disagreement necessarily contains a directed cycle, which proves uniqueness of the finite extremal orientation. In the half-plane, a double ray can carry nonzero “circulation at infinity.” Finite face flips and finite face potentials do not detect it.

This is a concrete candidate for the missing obstruction in the full problem: a globally maximal Schnyder wood may need to select or exclude such fluxes at infinity.

# 5. Why compactness does not yet prove the conjecture

The preceding arguments transfer every condition whose violation has a finite witness. They do not transfer typical infinite-tree conditions. For example, two monochromatic paths may merge in every finite approximation, but with their first merger moving farther and farther away. The local limit then has two disjoint rays. An analogous example occurs on a ladder: make the two directed rails merge at column \(n\); as \(n\to\infty\), the merger escapes and the local limit has two noncoalescing rays.

Thus the following implications remain unproved:

1. **Boundary rule:** The \((3,2)\)-orientation and the interior coloring have not been produced simultaneously, and no source-specific colored boundary condition has been checked.
2. **Wood condition:** Absence of finite monochromatic cycles does not imply that color classes coalesce into the required trees or forests.
3. **Maximality at infinity:** “No finite clockwise cycle” only gives finite-flip extremality. It does not show that the orientation is a greatest element of an infinite flip order.
4. **Full generality:** The proof assumes simplicity and local finiteness. Multiple edges, loops, or infinite-degree vertices require separate treatment.

If the source paper’s definition of a maximal half-plane Schnyder wood were exactly a locally recoverable coloring of a \((3,2)\)-orientation with no clockwise finite cycle, Theorem 2.1 plus the same compactness argument for colors would prove existence in the locally finite simple case. The supplied excerpt is not sufficient to verify that equivalence, and the possible coalescence/end conditions are precisely where the argument can fail.

Accordingly, this is a structural partial result rather than a resolution: finite defects can always be pushed to infinity, and any genuine counterexample must exploit nonlocal boundary or ray behavior, equivalently some form of circulation or noncoalescence at infinity.