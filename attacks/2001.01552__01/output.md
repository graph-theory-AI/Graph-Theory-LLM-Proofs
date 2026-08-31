```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture remains unresolved, but arbitrarily complicated graphs can be hidden in uniformly tame ball representations after sufficiently long subdivisions while retaining the sharp bound col_r <= 2r+1.",
  "would_publish": false,
  "caveats": "The catalog's singular-graph wording must be read uniformly over a graph class; the result below rules out a broad counterexample strategy but gives no universal representation theorem."
}
```

## 1. Precise interpretation of the problem

The informal statement cannot literally concern one finite graph. If \(G\) has \(n\) vertices, then
\[
\operatorname{col}_r(G)\le n
\]
for every \(r\), and all constants in any finite geometric representation may depend on \(G\). Thus every finite graph has coloring numbers bounded by a polynomial in \(r\) in this non-uniform sense.

The meaningful formulation is at the level of graph classes:

> Does there exist a class \(\mathcal G\) and a polynomial \(p\) such that
> \[
> \operatorname{col}_r(G)\le p(r)
> \qquad(G\in\mathcal G,\ r\ge1),
> \]
> but for every fixed choice of the tameness constant, scale parameter, and dimension, some \(G\in\mathcal G\) has no corresponding tame convex representation?

All constants must be uniform over \(\mathcal G\). I use this interpretation below.

Recall that, for a linear order \(\prec\) on \(V(G)\), a vertex \(u\) is strongly \(r\)-reachable from \(v\) if \(u\preceq v\) and there is a \(v\)-\(u\) path of length at most \(r\) whose internal vertices are all later than \(v\). The strong coloring number \(\operatorname{col}_r(G)\) is the minimum, over \(\prec\), of the maximum number of vertices strongly \(r\)-reachable from one vertex.

The partial result below is formulated so that it applies to the standard tameness notions in the source: the representations use only Euclidean balls, are \(2\)-ply, and satisfy a uniform piercing estimate for all intersecting balls of at least a given scale.

---

## 2. Long subdivisions have linear strong coloring numbers

For a graph \(H\), replace each edge \(e\) by an internally vertex-disjoint path with \(m_e\) internal vertices. Denote the resulting graph by \(S(H,\mathbf m)\).

### Proposition 1

Let \(H\) have \(n\) vertices, and suppose that \(m_e\ge n\) for every \(e\in E(H)\). Then
\[
\operatorname{col}_r\bigl(S(H,\mathbf m)\bigr)\le 2r+1
\qquad\text{for every }r\ge1.
\]

### Proof

Call the vertices inherited from \(H\) the branch vertices. Order all branch vertices before all subdivision vertices; within the two groups, use arbitrary orders.

Let \(G=S(H,\mathbf m)\).

First let \(v\) be a branch vertex. Every vertex \(u\preceq v\) is also a branch vertex. Distinct branch vertices are at distance at least \(n+1\), because every subdivided edge has at least \(n\) internal vertices. Hence:

- if \(r<n+1\), only \(v\) is strongly \(r\)-reachable from \(v\);
- if \(r\ge n+1\), at most all \(n\) branch vertices are strongly reachable, and \(n\le r\).

Now let \(v\) be a subdivision vertex lying on the path replacing an edge \(xy\in E(H)\). A strongly qualifying path starting at \(v\) cannot have a branch vertex as an internal vertex, since every branch vertex precedes \(v\). Consequently, such a path cannot leave the subdivided \(x\)-\(y\) path, except possibly by ending at \(x\) or \(y\). There are at most \(2r+1\) vertices on that path at distance at most \(r\) from \(v\).

Thus every vertex strongly \(r\)-reaches at most \(2r+1\) vertices in this order. ∎

The same bound holds for the induced-subgraph closure of any class of such subdivisions.

---

## 3. Every graph has a sufficiently long subdivision represented by balls in \(\mathbb R^3\)

### Proposition 2

For every finite graph \(H\) on \(n\) vertices, there are integers \(m_e\ge n\) such that \(S(H,\mathbf m)\) is the exact intersection graph of a \(2\)-ply family of closed Euclidean balls in \(\mathbb R^3\). The branch vertices are represented by balls of one radius \(R\), and all subdivision vertices by balls of a smaller common radius \(\varepsilon\).

### Proof

Label \(V(H)=\{1,\dots,n\}\) and place
\[
p_i=(i,i^2,i^3)\in\mathbb R^3.
\]
These points lie on the moment curve. Any four are affinely independent. Therefore two segments
\([p_i,p_j]\) and \([p_k,p_\ell]\) with disjoint endpoint sets are disjoint: an intersection would put their four endpoints in one plane. Similarly, two incident segments meet only at their common endpoint, and no segment contains a third \(p_k\).

Thus the straight-line drawing of \(H\) with vertex \(i\) at \(p_i\) has no intersections except at common endpoints.

Choose \(R>0\) sufficiently small that:

1. the balls \(B_i=\overline B(p_i,R)\) are pairwise disjoint;
2. every \(B_i\) is disjoint from every nonincident edge segment;
3. after deleting the interiors of the endpoint balls from each edge segment, the resulting compact truncated segments belonging to distinct edges are pairwise disjoint.

For incident edges, their truncated segments begin at distinct points of \(\partial B_i\), so this is possible. Since there are finitely many relevant compact sets, they have a positive mutual clearance.

Choose \(\varepsilon>0\) much smaller than this clearance, and also so small that each truncated edge segment can accommodate at least \(n\) balls. Along each edge \(e=ij\), place centers consecutively on the truncated segment, with consecutive center distance strictly between \(\varepsilon\) and \(2\varepsilon\). The first center is at distance \(R+\varepsilon/2\) from \(p_i\), and similarly at the other endpoint. By choosing the number of centers appropriately, the spacing can be made to lie in that interval.

Represent every subdivision vertex by a closed ball of radius \(\varepsilon\) about the corresponding center. Then:

- consecutive path balls intersect;
- nonconsecutive path balls on the same edge are disjoint, because their centers are more than \(2\varepsilon\) apart;
- the first path ball intersects its branch ball, but the second does not;
- balls belonging to distinct subdivided edges are disjoint;
- no path ball intersects a nonincident branch ball.

Hence the intersection graph is exactly \(S(H,\mathbf m)\), with \(m_e\ge n\).

No point belongs to three balls: distinct edge chains are disjoint, nonconsecutive balls in one chain are disjoint, and only the first ball of a chain meets its branch ball. Thus the representation is \(2\)-ply. ∎

Combining Propositions 1 and 2 gives the following.

### Corollary 3

There is a hereditary graph class \(\mathcal G_{\mathrm{route}}\) such that:

1. \(\operatorname{col}_r(G)\le2r+1\) for every \(G\in\mathcal G_{\mathrm{route}}\);
2. every \(G\in\mathcal G_{\mathrm{route}}\) has a \(2\)-ply ball representation in \(\mathbb R^3\);
3. for every finite graph \(H\), some subdivision of \(H\) belongs to \(\mathcal G_{\mathrm{route}}\).

Thus arbitrary graph-theoretic complexity can occur as an unbounded-depth topological minor inside a class having both linear strong coloring numbers and very well-behaved geometric representations.

---

## 4. Uniform tameness of the ball models

Here is a direct piercing estimate, independent of the combinatorics of the represented graph.

### Lemma 4

Let \(Q=\overline B(x,\rho)\subseteq\mathbb R^d\). The family of all balls of radius at least \(\rho\) which intersect \(Q\) can be pierced by at most \(5^d\) points.

### Proof

Let \(D=\overline B(y,R)\), where \(R\ge\rho\), intersect \(Q\). There is a point \(z\in \overline B(x,2\rho)\) such that
\[
\overline B(z,\rho)\subseteq D.
\]

Indeed, if \(\lVert x-y\rVert\le R-\rho\), take \(z=x\). Otherwise, move from \(y\) toward \(x\) by distance \(R-\rho\). The resulting \(z\) satisfies
\[
\lVert z-x\rVert
 \le (R+\rho)-(R-\rho)=2\rho,
\]
and \(\overline B(z,\rho)\subseteq D\).

Let \(P\) be a maximal \(\rho\)-separated subset of \(\overline B(x,2\rho)\). It is a \(\rho\)-net. The balls of radius \(\rho/2\) centered at points of \(P\) are disjoint and lie in \(\overline B(x,5\rho/2)\), so volume comparison gives
\[
|P|\le 5^d.
\]
Some \(p\in P\) satisfies \(\lVert p-z\rVert\le\rho\), and hence \(p\in D\). Thus \(P\) pierces every such \(D\). ∎

A fixed multiplicative slack in the size relation only changes \(5^d\) to a constant depending on that slack and \(d\). Consequently, under the source paper's scale-comparison relation \(\sqsubseteq_s\), ball families have a uniform \((c,\sqsubseteq_s)\)-tameness constant depending only on \(d\) and \(s\). In particular, the representations in Proposition 2 satisfy the relevant uniform geometric condition, not merely a graph-theoretic local-degree surrogate.

This eliminates a natural proposed route to the conjectured negative answer:

> Taking arbitrary dense or high-complexity graphs and subdividing every edge sufficiently many times does not produce a counterexample; such subdivisions can simultaneously have linear strong coloring numbers and uniformly tame ball representations in \(\mathbb R^3\).

---

## 5. A related prescribed-size representation lemma

The following further shows that simply forcing the geometric size order to realize a degeneracy order is not an obstruction.

### Proposition 5

Let \(G\) be \(k\)-degenerate, and let
\[
v_1,\dots,v_n
\]
be an order in which each \(v_i\) has at most \(k\) neighbors \(v_j\) with \(j>i\). Then \(G\) has an exact intersection representation by compact convex sets
\[
C_1,\dots,C_n\subseteq\mathbb R^{2k+3}
\]
such that
\[
\operatorname{diam}(C_1)<\operatorname{diam}(C_2)<\cdots<
\operatorname{diam}(C_n).
\]

Consequently, every \(C_i\) has at most \(k\) intersecting sets whose diameter is at least its own.

### Proof

Take points \(p_1,\dots,p_n\) on the moment curve in \(\mathbb R^{2k+2}\). The cyclic polytope they span is \((k+1)\)-neighborly, so every set of at most \(k+1\) of its vertices spans a face. Scale the configuration so that its diameter is at most \(1\).

Let
\[
S_i=\{i\}\cup\{j>i:v_iv_j\in E(G)\}.
\]
Then \(|S_i|\le k+1\), and
\[
F_i=\operatorname{conv}\{p_j:j\in S_i\}
\]
is a simplicial face of the cyclic polytope.

Choose rapidly increasing positive numbers \(t_1<\cdots<t_n\), for example \(t_i=3^i\), and define in
\(\mathbb R^{2k+2}\times\mathbb R\)
\[
C_i=\operatorname{conv}\left(
  \{(p_i,0)\}\cup(F_i\times\{t_i\})
\right).
\]

If \(i<j\) and \(v_iv_j\in E(G)\), then \(p_j\in F_i\), so
\[
(p_j,t_i)\in C_i.
\]
The set \(C_j\) contains the vertical segment
\[
\{p_j\}\times[0,t_j],
\]
and therefore also contains \((p_j,t_i)\). Thus adjacent vertices receive intersecting sets.

Suppose \(i<j\) and \(v_iv_j\notin E(G)\). Then neither \(p_i\) nor \(p_j\) belongs to the common face \(F_i\cap F_j\); its vertices, if any, correspond to common later neighbors of \(v_i\) and \(v_j\). Over this common face, \(C_i\) lies entirely at height \(t_i\), while \(C_j\) lies entirely at height \(t_j\). Since \(t_i\ne t_j\), the sets are disjoint. Hence the intersection graph is exactly \(G\).

Finally,
\[
t_i\le\operatorname{diam}(C_i)\le\sqrt{t_i^2+1}.
\]
The sequence \(t_i=3^i\) therefore gives strictly increasing diameters. ∎

This proposition does not settle the conjecture because the full tameness condition is a uniform geometric condition on comparable shapes, not merely the assertion that each represented vertex has few larger neighbors. The constructed polytopes can be extremely thin, and no uniform global tameness constant follows.

---

## 6. Remaining gap

No counterexample or universal representation theorem follows from the arguments above.

The negative conjecture would require a graph class whose obstruction survives all of the following freedoms:

- arbitrary compact convex shapes rather than boxes;
- arbitrary fixed dimension;
- strongly nonuniform scales;
- routing through very small objects;
- subdivision and induced-subgraph operations.

Propositions 1–4 show that stretched dense cores, by themselves, do not provide such an obstruction. Proposition 5 shows that realizing an optimal degeneracy order as a diameter order is also not the essential difficulty.

What remains missing is either:

1. a graph invariant forced by every uniformly tame convex representation in fixed dimension but not forced by polynomial strong coloring numbers; or
2. a construction turning a polynomial strong-coloring order into a globally tame convex representation.

I have neither, so the full conjecture remains open.