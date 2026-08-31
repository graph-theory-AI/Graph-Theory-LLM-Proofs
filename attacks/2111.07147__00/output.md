```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture remains unresolved, but it admits an exact bounded-diameter edge-bipartization formulation, a useful plane-dual certificate, and a positive answer when the number of non-triangular faces is bounded.",
  "would_publish": false,
  "caveats": "The dual certificate is only sufficient, and I cannot derive it from the distance and non-separating-triangle hypotheses when the number of non-triangular faces is unbounded."
}
```

# 1. Statement and conventions

For a graph \(G\), write
\[
\operatorname{wdiam}_G(X)=\max_{x,y\in X}\operatorname{dist}_G(x,y).
\]
A 2-coloring has weak diameter at most \(D\) if every monochromatic connected component \(C\) satisfies
\(\operatorname{wdiam}_G(C)\le D\).

The question asks whether, for every fixed \(r\), there is a constant \(D(r)\) such that every plane graph \(G\) satisfying

1. \(G\) has no separating triangle, and
2. every vertex is at distance at most \(r\) from the boundary of a face of length at least four,

has a 2-coloring of weak diameter at most \(D(r)\).

I do not prove or disprove this. The following reductions and special cases are rigorous.

---

# 2. Exact reformulation as bounded-diameter edge bipartization

The coloring problem has a useful equivalent edge formulation.

## Lemma 2.1

For a graph \(G\) and an integer \(D\), the following are equivalent.

1. \(G\) has a 2-coloring of weak diameter at most \(D\).
2. There is a set \(M\subseteq E(G)\) such that:
   - \(G-M\) is bipartite, and
   - every component of the spanning subgraph \((V(G),M)\) has weak diameter at most \(D\), measured in \(G\).

### Proof

Suppose \(c\) is a 2-coloring of weak diameter at most \(D\), and let
\[
M=\{uv\in E(G):c(u)=c(v)\}.
\]
Every edge of \(G-M\) is bichromatic, so \(G-M\) is bipartite. Moreover, the nontrivial components of \((V(G),M)\) are exactly the monochromatic components of \(c\), and hence have weak diameter at most \(D\).

Conversely, suppose \(M\) satisfies the second condition. Properly 2-color every component of \(G-M\). Every monochromatic edge of the resulting coloring belongs to \(M\). Consequently, every monochromatic component is contained in a component of \((V(G),M)\), and hence has weak diameter at most \(D\). ∎

Thus the original problem is exactly the problem of finding an edge bipartization whose deleted-edge components have uniformly bounded weak diameter.

---

# 3. A plane-dual parity certificate

For a connected plane graph \(G\), call a face odd if its facial boundary walk has odd length. Let \(G^*\) be the geometric dual.

## Proposition 3.1

Let \(M\subseteq E(G)\). Suppose that:

1. the dual edge set \(M^*=\{e^*:e\in M\}\) is a forest in \(G^*\);
2. every component of the spanning dual forest \((V(G^*),M^*)\) contains an even number of odd faces of \(G\); and
3. every component of \((V(G),M)\) has weak diameter at most \(D\).

Then \(G\) has a 2-coloring of weak diameter at most \(D\).

### Proof

Because \(M^*\) is acyclic, \(G-M\) is connected. Indeed, if \(G-M\) were disconnected, a bond of \(G\) contained in \(M\) would dualize to a cycle contained in \(M^*\).

Deleting an edge of \(M\) corresponds in the dual to contracting the corresponding edge of \(M^*\). Thus the faces of \(G-M\) correspond to the components of \((V(G^*),M^*)\).

For such a component \(\mathcal C\), the parity of the boundary length of the corresponding face of \(G-M\) is
\[
\sum_{F\in V(\mathcal C)} |F| \pmod 2,
\]
because every deleted edge removes two boundary occurrences. By assumption this sum is even. Hence every face of \(G-M\) has even boundary length.

A connected plane graph is bipartite if and only if all of its facial boundary walks are even. Therefore \(G-M\) is bipartite. Lemma 2.1 now applies. ∎

This gives a concrete sufficient target in the dual: join the odd faces in even-sized groups by a dual forest, while ensuring that the crossed primal edges do not form large weak-diameter components.

## Corollary 3.2: adjacent pairing of odd faces

Suppose the odd faces of \(G\) can be paired across common edges, and let \(M\) consist of one common edge for each pair. If the components of \((V(G),M)\) have weak diameter at most \(D\), then \(G\) has a weak-diameter-\(D\) 2-coloring.

In particular, if the chosen primal edges form a matching, then \(D=1\).

Indeed, the corresponding dual edges form a matching saturating all odd-face vertices, so every dual component contains either zero or two odd faces.

For graphs in the conjectured class, the absence of separating triangles implies that every 3-cycle bounds a face on one side. Hence, if all non-triangular faces are even, the odd faces in Proposition 3.1 are precisely the triangular faces. One rigorous special case is therefore:

> If all non-triangular faces are even, the triangular faces can be paired across shared edges, and the selected shared primal edges have bounded-diameter components, then the desired 2-coloring exists.

The difficulty is that a perfectly good matching or linkage in the dual can correspond to primal edges concatenating into an arbitrarily long path. Controlling this primal concatenation is essentially the unresolved part.

---

# 4. Positive answer with a bounded number of non-triangular faces

The source paper mentions the case of exactly one non-triangular face. The same argument extends to any bounded number of witness faces.

## Theorem 4.1

For every pair of integers \(r,q\ge 0\), there is \(D(r,q)\) with the following property.

Let \(G\) be a plane graph, and suppose there are at most \(q\) faces \(F_1,\dots,F_q\) such that every vertex of \(G\) is at distance at most \(r\) from one of these faces. Then \(G\) has a 2-coloring of weak diameter at most \(D(r,q)\).

No assumption about separating triangles is needed.

### Proof

We may work componentwise, so assume \(G\) is connected. For every \(F_i\), add a new vertex \(x_i\) in the interior of \(F_i\), adjacent to every vertex incident with \(F_i\). Let the resulting planar graph be \(A\), and put
\[
X=\{x_1,\dots,x_q\},\qquad R=r+1.
\]
Every vertex of \(A\) is within distance \(R\) of \(X\).

We use the elementary observation that if a connected graph is covered by \(q\) balls of radius \(R\), then its diameter is at most
\[
2R+(q-1)(2R+1)=q(2R+1)-1.
\]
Indeed, form an auxiliary graph on the ball centers, joining two centers when their balls overlap or contain endpoints of a common edge. This auxiliary graph is connected, and adjacent centers are at distance at most \(2R+1\).

Consequently,
\[
\operatorname{diam}(A)\le q(2r+3)-1.
\]
A standard planar radius/treewidth bound gives
\[
\operatorname{tw}(A)\le 3q(2r+3)+O(1).
\]
Since \(G\) is a subgraph of \(A\), the same bound holds for \(\operatorname{tw}(G)\).

Finally, for every fixed \(k\), graphs of treewidth at most \(k\) have weak diameter chromatic number at most two, with a bound depending only on \(k\). This is the bounded-treewidth/asymptotic-dimension-one fact used in the source paper for the one-face case. Applying it with \(k=O(qr)\) proves the theorem. ∎

Thus any counterexample to the original conjecture must use an unbounded number of non-triangular faces.

---

# 5. A quantitative density bound

Although density alone does not settle the coloring problem, the hypotheses force a definite face-excess estimate.

Let \(G\) be a connected simple plane graph with \(n\ge 3\) vertices and \(m\) edges. Let

- \(h\) be the number of faces of length at least four,
- \(L\) be the sum of the lengths of those faces, and
- \(t\) be the number of triangular faces.

Euler's formula and the face-length sum give
\[
n-m+t+h=2,\qquad 2m=3t+L.
\]
Eliminating \(t\) yields the exact identity
\[
m=3n+3h-L-6. \tag{5.1}
\]

Since every non-triangular face has length at least four,
\[
h\le \frac L4.
\]
Therefore
\[
m\le 3n-\frac L4-6. \tag{5.2}
\]

## Corollary 5.1: the case \(r=0\)

If every vertex is incident with a face of length at least four, then \(L\ge n\), and hence
\[
m\le \frac{11}{4}n-6.
\]
Equivalently,
\[
\frac{2m}{n}\le \frac{11}{2}-\frac{12}{n}.
\]

This estimate does not use the absence of separating triangles.

## Corollary 5.2: bounded maximum degree

Suppose \(G\in\mathcal G_r\) and \(\Delta(G)\le\Delta\), where \(\Delta\ge2\). Define
\[
b_r(\Delta)=1+\Delta\sum_{i=0}^{r-1}(\Delta-1)^i.
\]
Let \(S\) be the set of vertices incident with non-triangular faces. The radius-\(r\) balls around \(S\) cover \(V(G)\), so
\[
n\le b_r(\Delta)|S|\le b_r(\Delta)L.
\]
Using (5.2),
\[
m\le
\left(3-\frac{1}{4b_r(\Delta)}\right)n-6.
\]

Thus, under a maximum-degree bound, the class has a uniform positive gap below the triangulation density \(3n-6\). I do not know how to turn this density gap into the required bounded weak-diameter 2-coloring.

As a very small additional special case, every graph of maximum degree at most three has a 2-coloring whose monochromatic components have at most two vertices: choose a cut with the maximum possible number of crossing edges. At each vertex the number of same-colored neighbors is then at most the number of oppositely colored neighbors, and hence is at most one.

---

# 6. The class still has unbounded treewidth

The bounded-number-of-faces theorem cannot be extended merely by proving bounded treewidth.

For each \(N\), start with the \((N+1)\times(N+1)\) square grid. Choose a collection of pairwise vertex-disjoint internal unit squares, and add one diagonal in each chosen square. Leave every other unit square untriangulated.

Then:

1. every vertex is incident with an untriangulated square or with the outer face, so the graph belongs to \(\mathcal G_0\);
2. every 3-cycle is one of the two facial triangles in a chosen square, so there is no separating triangle; and
3. the graph contains the original square grid as a subgraph, and hence has treewidth tending to infinity with \(N\).

For this particular family, the ordinary grid bipartition works: each chosen diagonal has same-colored endpoints, and because the selected squares are vertex-disjoint, the monochromatic components have diameter one. Thus this is not a counterexample, but it shows that any proof must exploit more than bounded treewidth.

---

# 7. Remaining gap

By Lemma 2.1, a complete proof would amount to constructing, for every \(G\in\mathcal G_r\), an edge set \(M\) such that

\[
G-M\text{ is bipartite}
\]
and every component of \((V(G),M)\) has weak diameter bounded solely in terms of \(r\).

Proposition 3.1 gives a natural sufficient way to do this by pairing or grouping odd faces in the dual. However:

- dual paths of bounded or well-controlled combinatorial form can cross primal edges forming an arbitrarily long connected chain;
- the hypothesis “every vertex is near a non-triangular face” is a primal metric condition and does not directly bound such dual linkages;
- non-triangular faces of odd length are themselves parity defects; and
- it is not clear that one may require the dual of \(M\) to be a forest without loss of generality.

I therefore do not obtain the required \(D(r)\), nor an explicit counterexample. The strongest complete new special case above is Theorem 4.1, where the number of non-triangular witness faces is bounded.