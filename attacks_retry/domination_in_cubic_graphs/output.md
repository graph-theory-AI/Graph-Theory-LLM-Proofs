```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I prove the conjectured bound when deleting vertex-disjoint triangles and at most one additional vertex leaves a forest.",
  "would_publish": false,
  "caveats": "Structural special case only; novelty is not verified, and the general 3-connected case is not resolved."
}
```

# A feedback-forest special case

All graphs below are finite and simple. I do not prove or disprove the full conjecture.

The following result allows branching outside the triangles, unlike the previous attempt’s path/cycle decomposition. I do not use that attempt’s theorem as a black box. The elementary triangle-selection observation is verified directly below; the main ingredient is a boundary-domination lemma for forests.

## The partial result

**Theorem.** Let \(G\) be a cubic graph, let \(\mathcal T\) be a family of vertex-disjoint triangles, and put
\[
U=\bigcup_{T\in\mathcal T}V(T).
\]
Suppose \(Z\subseteq V(G)\setminus U\) and
\[
F=G-(U\cup Z)
\]
is a forest. Then
\[
\boxed{\displaystyle
\gamma(G)\le
|\mathcal T|+|Z|+\left\lfloor\frac{|V(F)|}{3}\right\rfloor
=
\left\lfloor\frac{|V(G)|+2|Z|}{3}\right\rfloor .}
\]

No connectivity hypothesis is needed.

In particular:

- If deleting the triangles leaves a forest, then
  \[
  \gamma(G)\le \left\lfloor\frac{|V(G)|}{3}\right\rfloor.
  \]
- If deleting the triangles and at most one additional vertex leaves a forest, then
  \[
  \gamma(G)\le \left\lceil\frac{|V(G)|}{3}\right\rceil.
  \]

The vertices outside the triangles need not have neighbors in triangles: the remaining forest can have degree-three vertices and arbitrarily large components.

## 1. Three boundary conditions on a forest

For a graph \(H\) and \(X\subseteq V(H)\), define
\[
\gamma(H\mid X)
=
\min\bigl\{|S|:S\subseteq V(H),\quad V(H)\setminus X\subseteq N_H[S]\bigr\}.
\]
Thus vertices of \(X\) are regarded as already dominated. They are still allowed to belong to \(S\).

**Lemma.** Let \(F\) be a forest, and let \(X_1,X_2,X_3\subseteq V(F)\). Suppose every vertex of degree at most one belongs to at least two of the sets \(X_1,X_2,X_3\). Then
\[
\gamma(F\mid X_1)+\gamma(F\mid X_2)+\gamma(F\mid X_3)
\le |V(F)|.
\tag{1}
\]

The sets \(X_i\) may overlap arbitrarily. The lemma holds for forests of arbitrary maximum degree.

### Proof

We use induction on \(|V(F)|\). The assertion is additive over components, so it suffices to consider a tree \(T\). The empty forest is immediate.

#### Paths

Suppose \(T\) is a path on \(m\) vertices.

- If \(m=3k\), each of the three partial domination numbers is at most \(k\).

- If \(m=3k+1\), choose an endpoint \(x\). In at least two of the boundary conditions, \(x\) is already dominated. In either such condition, deleting \(x\) leaves a path on \(3k\) vertices, which can be dominated by \(k\) vertices. In the remaining condition, \(k+1\) vertices suffice. Thus the sum is at most
  \[
  k+k+(k+1)=3k+1.
  \]
  This also covers \(m=1\).

- If \(m=3k+2\), each endpoint belongs to at least two of the three sets. Consequently, both endpoints belong to some common \(X_i\). In that condition, deleting both endpoints leaves a path on \(3k\) vertices, so \(k\) vertices suffice. In each other condition, \(k+1\) suffice. The sum is at most
  \[
  k+(k+1)+(k+1)=3k+2.
  \]

This proves (1) for paths.

#### A pendant path with at least three vertices

Now suppose \(T\) is not a path. Root it at a leaf and choose a vertex \(b\) of degree at least three farthest from the root. Every branch below \(b\) is a path ending at a leaf.

Suppose one such pendant path contains at least three vertices besides \(b\). Let its last three vertices, in order toward the leaf, be
\[
x_1,x_2,x_3,
\]
and let \(w\) be the neighbor of \(x_1\) outside this triple. Delete the triple to obtain \(T'\).

For each \(i\), make the following choices:

- If \(x_3\in X_i\), select \(x_1\), and add \(w\) to the new boundary set \(X_i'\).
- If \(x_3\notin X_i\), select \(x_2\), and make no additional boundary declaration.

In both cases, retain \(X_i\cap V(T')\) in \(X_i'\).

The selected vertex dominates every deleted vertex that was not already in \(X_i\). Any newly declared boundary vertex \(w\) is genuinely dominated by the selected \(x_1\).

The only possible newly created leaf is \(w\). Since \(x_3\) belongs to at least two of the original boundary sets, \(w\) belongs to at least two of the new ones. No isolated vertex is created in this reduction. Hence the induction hypothesis applies to \(T'\).

Exactly one vertex was selected in each of the three conditions, so
\[
\sum_{i=1}^3\gamma(T\mid X_i)
\le 3+|V(T')|
=|V(T)|.
\]

#### All pendant branches have one or two vertices

We may therefore suppose that every branch below \(b\) has length one or two.

Write \(d=\deg_T(b)\), and let \(r\) be the number of length-two branches below \(b\). There are \(d-1\) downward branches altogether. Delete \(b\) and all these branches. The deleted set has
\[
1+(d-1)+r=d+r
\]
vertices. Let \(u\) be the parent of \(b\), and call the remaining tree \(T'\).

For each boundary condition \(i\):

1. select \(b\);
2. on every length-two branch whose leaf is not in \(X_i\), also select its internal vertex.

These selections dominate all deleted vertices outside \(X_i\). They also dominate \(u\), so put
\[
X_i'=(X_i\cap V(T'))\cup\{u\}.
\]

Each terminal leaf of a length-two branch is absent from at most one of the three sets \(X_i\). Therefore the total number of selected vertices, summed over all three conditions, is at most
\[
3+r\le d+r,
\]
because \(d\ge3\).

Any newly created leaf or isolated vertex of \(T'\) is \(u\), which belongs to all three new boundary sets. Induction gives
\[
\sum_{i=1}^3\gamma(T\mid X_i)
\le |V(T')|+(d+r)
=|V(T)|.
\]

All cases are covered. \(\square\)

## 2. Coordinating the triangle choices

We now prove the theorem.

Write
\[
t=|\mathcal T|,\qquad z=|Z|,\qquad f=|V(F)|,
\]
so that
\[
|V(G)|=3t+z+f.
\tag{2}
\]

Construct a bipartite incidence multigraph \(B\) with parts

- \(V(F)\);
- the triangles in \(\mathcal T\).

For every edge of \(G\) joining \(v\in V(F)\) to a vertex of a triangle \(T\), include an edge \(vT\) in \(B\). Parallel edges are allowed.

The maximum degree of \(B\) is at most three. On the triangle side, this follows because each vertex of a triangle already has two neighbors inside that triangle, leaving exactly three outgoing edges in total.

The edges of \(B\) can be properly colored with three colors. For completeness, one can add dummy vertices and edges to obtain a 3-regular bipartite multigraph. Hall’s theorem gives a perfect matching; removing it and repeating decomposes its edges into three matchings. Restricting those colors to \(B\) gives the required coloring.

Let \(M_1,M_2,M_3\) be the color classes.

For each \(i\), choose a set \(A_i\) containing exactly one vertex from each triangle:

- If \(T\) is incident with an edge of \(M_i\), choose the triangle vertex corresponding to that edge of \(G\).
- Otherwise, choose any vertex of \(T\).

This is well-defined because \(M_i\) is a matching. The chosen vertex dominates its entire triangle. It also dominates the prescribed vertex of \(F\), when there is one.

Define
\[
X_i=
\bigl(N_G(Z)\cap V(F)\bigr)
\;\cup\;
\{v\in V(F):v\text{ is incident with an edge of }M_i\}.
\tag{3}
\]
Every vertex of \(X_i\) is dominated by \(Z\cup A_i\).

We check the hypothesis of the forest lemma. Let \(v\) have degree at most one in \(F\).

- If \(v\) has a neighbor in \(Z\), then \(v\in X_i\) for all three \(i\).
- Otherwise, cubicity gives
  \[
  \deg_B(v)=3-\deg_F(v)\ge2.
  \]
  Proper edge-coloring gives these incident edges distinct colors, so \(v\) belongs to at least two of the sets \(X_i\).

The lemma therefore supplies sets \(S_i\subseteq V(F)\) dominating \(V(F)\setminus X_i\), with
\[
|S_1|+|S_2|+|S_3|\le f.
\tag{4}
\]

For each \(i\), the set
\[
D_i=Z\cup A_i\cup S_i
\]
dominates \(G\):

- \(Z\) is selected;
- every triangle is dominated by its vertex in \(A_i\);
- \(X_i\) is dominated by \(Z\cup A_i\);
- the remaining vertices of \(F\) are dominated by \(S_i\).

Using (2) and (4),
\[
\sum_{i=1}^3 |D_i|
\le 3z+3t+f
=|V(G)|+2z.
\]
Thus at least one \(D_i\) has size at most
\[
\left\lfloor\frac{|V(G)|+2z}{3}\right\rfloor,
\]
as asserted. \(\square\)

Given \(\mathcal T\) and \(Z\), the proof is constructive in polynomial time: it uses bipartite matchings and the explicit forest reductions above.

## 3. Consequences for the original conjecture

For fixed \(\mathcal T\), let \(\tau(G-U)\) denote the minimum number of vertices whose deletion makes \(G-U\) a forest. The theorem gives the parameterized bound
\[
\gamma(G)\le
\left\lfloor
\frac{|V(G)|+2\tau(G-U)}{3}
\right\rfloor.
\tag{5}
\]

When \(\tau(G-U)\le1\), this proves the conjectured bound because
\[
\left\lfloor\frac{n+2}{3}\right\rfloor
=
\left\lceil\frac n3\right\rceil.
\]
Also, \(\tau(G-U)\le2\) suffices when \(n\equiv1\pmod3\).

In a 3-connected cubic graph other than \(K_4\), one may take \(\mathcal T\) to consist of **all** triangles. Here is the verification that they are vertex-disjoint. Two intersecting triangles must share an edge, by cubicity; write them \(abc\) and \(abd\). If \(cd\) is an edge, these vertices form a \(K_4\) component, so the graph is \(K_4\). Otherwise, deleting \(c,d\) separates \(a,b\) from the rest, contradicting 3-connectivity. The graph \(K_4\) itself has domination number one.

Consequently, any counterexample to the original conjecture must retain a cycle after deleting all triangle vertices and any one additional vertex. If its order is \(1\bmod3\), it must retain a cycle even after deleting any two additional vertices.

## 4. The remaining gap

The feedback-forest hypothesis is not a consequence of 3-connectivity. In particular, this argument does not settle the triangle-free case.

There is also a concrete obstruction to extending the forest lemma mechanically to cycles. On a cycle
\[
C=v_0v_1v_2v_3v_4v_0,
\]
take
\[
X_1=\{v_0,v_2\},\qquad
X_2=\{v_1,v_3\},\qquad
X_3=\{v_4\}.
\]
Every vertex belongs to exactly one boundary set, as would naturally occur when each cycle vertex has one edge to a triangle. Nevertheless,
\[
\gamma(C\mid X_1)=\gamma(C\mid X_2)=\gamma(C\mid X_3)=2,
\]
so their sum is \(6>5\). Indeed, a single vertex of \(C_5\) leaves two adjacent vertices undominated, whereas each \(X_i\) is independent.

This is an obstruction to the averaging method, **not** a counterexample to Reed’s conjecture. Resolving general residual cyclic structures requires an additional idea.

Thus the result establishes a branching, feedback-forest special case and the bound (5), but leaves the original 3-connected cubic conjecture unresolved.