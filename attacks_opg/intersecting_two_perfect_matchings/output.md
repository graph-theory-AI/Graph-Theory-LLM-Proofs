```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A fractional-matching argument proves the conjecture for fewer than 70 vertices and gives broader sufficient conditions, while a sharp construction shows that the first matching cannot be prescribed arbitrarily.",
  "would_publish": false,
  "caveats": "The unrestricted conjecture is not settled, and novelty of the partial results is not claimed."
}
```

## 1. Results obtained

I do not obtain a proof or counterexample for the unrestricted conjecture. I prove:

1. Every bridgeless cubic graph with at most **68 vertices** satisfies the conjecture. In fact, such a graph has three perfect matchings with empty common intersection.
2. A parameterized sufficient condition involving odd cuts contained in a chosen perfect matching.
3. An order-independent sufficient condition involving the number of cycles in its complementary 2-factor.
4. For the variant in which the first perfect matching is prescribed:
   - every instance on at most **28 vertices** is positive;
   - this order bound is sharp, with an explicit **30-vertex** negative instance;
   - the decision problem is NP-complete.

The last item is **not** a counterexample to the original conjecture.

All graphs below are finite and loopless; parallel edges cause no difficulty. It suffices to work with connected graphs, since the conclusions combine componentwise.

## 2. A useful exact certificate

Write \(\delta(X)\) for the edges with exactly one endpoint in \(X\). Cubicity gives
\[
|\delta(X)|\equiv |X|\pmod 2.
\]

**Lemma 1.** For any \(I\subseteq E(G)\), the following are equivalent:

- \(I\) contains no odd edge-cut;
- every component of \(G-I\) has even order.

**Proof.** If \(K\) is an odd-order component of \(G-I\), then
\(\delta(V(K))\subseteq I\), and this cut has odd size.

Conversely, if an odd cut \(\delta(X)\) is contained in \(I\), then \(X\) is a union of components of \(G-I\). Since \(|X|\) is odd, at least one of those components has odd order. \(\square\)

Thus a proposed pair of perfect matchings can be checked in linear time: delete their intersection and inspect component orders.

## 3. A fractional-matching criterion

I use the standard perfect-matching polytope theorem: the convex hull of perfect-matching incidence vectors is
\[
\left\{
x\in\mathbb R_{\ge0}^{E(G)}:
x(\delta(v))=1\ \text{for all }v,\quad
x(\delta(X))\ge1\ \text{for every odd }X
\right\}.
\]

Recall also that every perfect matching meets an odd cut in a positive odd number of edges.

### Parameterized lemma

**Lemma 2.** Let \(P\) be a perfect matching of a bridgeless cubic graph \(G\), and let \(q\ge3\) be odd. Suppose that \(P\) contains no odd edge-cut of size less than \(q\).

Then there is a perfect matching \(Q\) such that
\[
|P\cap Q|\le \left\lfloor\frac{|V(G)|}{2q}\right\rfloor,
\]
and every \(q\)-edge-cut contained in \(P\) meets \(Q\) exactly once. Moreover, \(Q\) can be chosen to meet every 3-edge-cut exactly once.

Consequently, \(P\cap Q\) contains no odd cut of size at most \(q\).

**Proof.** Define
\[
x_e=
\begin{cases}
1/q,&e\in P,\\[2mm]
(q-1)/(2q),&e\notin P.
\end{cases}
\]
At each vertex the incident weights sum to \(1\).

Consider an odd cut \(C\). Put
\[
c=|C|,\qquad k=|C\setminus P|.
\]
Since \(|C\cap P|\) and \(c\) are odd, \(k\) is even. Furthermore,
\[
x(C)=\frac{c}{q}+\frac{q-3}{2q}k.
\]

If \(k=0\), the hypothesis gives \(c\ge q\), so \(x(C)\ge1\). If \(k\ge2\), bridgelessness gives \(c\ge3\), and hence
\[
x(C)\ge\frac{c+q-3}{q}\ge1.
\]
Thus \(x\) belongs to the perfect-matching polytope.

Take a convex decomposition of \(x\) into perfect matchings. For a random matching \(Q\) drawn according to this decomposition,
\[
\mathbb E|P\cap Q|
=\sum_{e\in P}x_e
=\frac{|V(G)|}{2q}.
\]

If \(C\subseteq P\) is a \(q\)-edge-cut, then \(x(C)=1\). Every perfect matching meets \(C\) at least once, so every matching occurring with positive coefficient in the decomposition meets \(C\) exactly once.

Every 3-edge-cut is also tight. For \(q=3\), \(x\) is the constant vector \(1/3\). For \(q>3\), the hypothesis forces \(P\) to meet each 3-edge-cut once, and its \(x\)-weight is again \(1\).

Choosing a matching from the decomposition with intersection size no larger than the average proves the assertions. \(\square\)

**Corollary 3.** Under the hypotheses of Lemma 2, the desired pair exists whenever
\[
|V(G)|<2q(q+2).
\]

Indeed, any odd cut contained in \(P\cap Q\) would have size at least \(q+2\), whereas
\[
|P\cap Q|<q+2.
\]

### Obtaining \(q=5\) unconditionally

The constant vector \(x_e=1/3\) belongs to the perfect-matching polytope of every bridgeless cubic graph. Every 3-edge-cut has weight exactly \(1\). Therefore every matching in a convex decomposition of this vector meets every 3-edge-cut exactly once.

Choose one such matching \(P\). It contains no 3-edge-cut, so Lemma 2 applies with \(q=5\). We obtain a perfect matching \(Q\) satisfying
\[
|P\cap Q|\le\left\lfloor\frac{|V(G)|}{10}\right\rfloor,
\]
such that \(P\cap Q\) contains neither a 3-edge-cut nor a 5-edge-cut.

This proves:

**Theorem 4.** Every bridgeless cubic graph with at most \(68\) vertices satisfies the conjecture.

At that order, the intersection has at most six edges, while any odd cut it contains would have at least seven.

### A stronger conclusion at the same order

For the pair \(P,Q\) just constructed, define
\[
y_e=\frac{3-\mathbf1_P(e)-\mathbf1_Q(e)}7.
\]
The vertex equations hold. For an odd cut \(C\):

- if \(|C|=3\), both matchings meet it once, so \(y(C)=1\);
- if \(|C|=5\), they cannot both contain all of \(C\), and therefore
  \[
  |P\cap C|+|Q\cap C|\le8,
  \qquad y(C)\ge\frac{15-8}{7}=1;
  \]
- if \(|C|\ge7\), every edge has \(y_e\ge1/7\), so \(y(C)\ge1\).

Thus \(y\) is another fractional perfect matching. Writing \(I=P\cap Q\), a perfect matching \(R\) drawn from its decomposition satisfies
\[
\mathbb E|R\cap I|=\frac{|I|}{7}.
\]
When \(|V(G)|\le68\), this is at most \(6/7\). Some \(R\) therefore has
\[
P\cap Q\cap R=\varnothing.
\]

This proves the stronger triple-intersection conclusion in that order range.

### A connectivity application

If an edge-cut is contained in a matching, every vertex on either side has internal degree at least two. Both sides therefore contain cycles.

Consequently, if \(G\) has no cyclic odd cut smaller than \(q\), the hypothesis of Lemma 2 holds for **every** perfect matching \(P\). For example, every cyclically 6-edge-connected cubic graph on at most \(124\) vertices satisfies the conjecture: use \(q=7\) and
\[
124<2\cdot7\cdot9.
\]

## 4. A sufficient condition with no order bound

The same fractional point gives another criterion.

**Theorem 5.** Under the hypotheses of Lemma 2, suppose that \(G-P\) has at most \(q+1\) cycles. Then there is a perfect matching \(Q\) such that \(P\cap Q\) contains no odd edge-cut.

**Proof.** Contract each cycle of \(G-P\) to a vertex, retaining the edges of \(P\). The resulting multigraph \(K\) is connected. Let \(B\subseteq P\) correspond to a spanning tree of \(K\).

Draw \(Q\) from the decomposition of the fractional matching in Lemma 2. Each edge of \(B\) belongs to \(Q\) with probability \(1/q\), so
\[
\mathbb E|B\cap Q|=\frac{|B|}{q}\le1.
\]

If \(|B|<q\), some \(Q\) avoids \(B\). Then \(G-(P\cap Q)\) contains \(G-P\) together with all of \(B\), and is connected. Its order is even, so Lemma 1 applies.

It remains to consider \(|B|=q\). Suppose, for contradiction, that every matching in the decomposition is unsuccessful. No such matching can avoid \(B\), and the expectation above is \(1\). Hence every one meets \(B\) in exactly one edge.

Fix \(e\in B\). Deleting \(e\) partitions the spanning tree into two parts. Let \(U_e\) be the union of the original cycles belonging to one part, and put
\[
D_e=\delta_G(U_e).
\]
All edges of \(D_e\) belong to \(P\).

Whenever \(e\in Q\), all other edges of \(B\) survive in \(G-(P\cap Q)\). Thus each side of \(D_e\) is connected in that graph. If any edge of \(D_e\) survived, the whole graph would be connected and the pair would succeed. Consequently, under our contradiction assumption,
\[
e\in Q\quad\Longrightarrow\quad D_e\subseteq Q.
\]
Moreover, the two resulting components must be odd, so \(D_e\) is an odd cut.

Write \(c_e=|D_e|\). Since \(\Pr(e\in Q)=1/q\), and every perfect matching meets \(D_e\) at least once,
\[
\mathbb E|Q\cap D_e|
\ge \frac{c_e}{q}+\left(1-\frac1q\right)
>\frac{c_e}{q}.
\]
But every edge of \(D_e\subseteq P\) has marginal probability \(1/q\), giving the contradictory equality
\[
\mathbb E|Q\cap D_e|=\frac{c_e}{q}.
\]
\(\square\)

In particular:

- any perfect matching whose complementary 2-factor has at most **four cycles** can serve as the first matching;
- a perfect matching meeting every 3-edge-cut once and having at most **six complementary cycles** is sufficient.

## 5. Why an arbitrary first matching cannot be fixed

Consider the prescribed-first-matching problem:

> Given a bridgeless cubic graph \(G\) and a specified perfect matching \(P\), does there exist a perfect matching \(Q\) such that \(P\cap Q\) contains no odd edge-cut?

Lemma 2 with \(q=3\) proves that every such instance with fewer than \(30\) vertices is positive. The following construction shows that this is sharp.

### Triangle expansion

Let \(H\) be a bridgeless cubic graph. Replace every vertex \(v\) by a triangle with one vertex for each edge incident with \(v\). For every original edge \(uv\), join its corresponding triangle vertices. Call the resulting cubic graph \(T(H)\).

Let \(P\) consist of all these edges joining different triangles. It is a perfect matching.

The graph \(T(H)\) is bridgeless: triangle edges lie on triangles, and every edge joining triangles lies on a lifted cycle of \(H\).

For any perfect matching \(Q\) of \(T(H)\), the number of its external edges at a triangle is either one or three. Define
\[
S=\{e\in E(H):\text{the corresponding external edge is not in }Q\}.
\]
Then every vertex has degree zero or two in \(H[S]\). Thus \(H[S]\) is a disjoint union of cycles and isolated vertices.

All triangle edges remain in \(T(H)-(P\cap Q)\). Contracting the triangles gives exactly \(H[S]\). A component with \(t\) vertices in \(H[S]\) lifts to a component with \(3t\) vertices. Therefore Lemma 1 gives
\[
\begin{aligned}
P\cap Q\text{ contains no odd cut}
&\iff H[S]\text{ has only even-order components}\\
&\iff S\text{ is a spanning union of even cycles}.
\end{aligned}
\]

A cubic graph has a spanning union of even cycles exactly when it is 3-edge-colourable. Conversely, any such even 2-factor \(S\) produces \(Q\): use the external edges corresponding to \(E(H)\setminus S\), and in each triangle match the other two vertices internally.

Hence
\[
\boxed{
(T(H),P)\text{ is a positive prescribed-matching instance}
\iff H\text{ is 3-edge-colourable}.
}
\]

### An explicit 30-vertex negative instance

Take \(H\) to be the Petersen graph, with vertices \(u_i,v_i\), \(i\in\mathbb Z_5\), and edges
\[
u_iu_{i+1},\qquad v_iv_{i+2},\qquad u_iv_i.
\]

For completeness, its non-3-edge-colourability can be checked directly through its perfect matchings. A perfect matching uses one, three, or five spokes \(u_iv_i\). Three spokes are impossible: the two remaining indices would have to be adjacent both on the outer pentagon and on the inner pentagram.

With one spoke, rotation lets us assume it is \(u_0v_0\), and the matching is necessarily
\[
\{u_0v_0,u_1u_2,u_3u_4,v_1v_3,v_2v_4\}.
\]
Its complement consists of the two 5-cycles
\[
u_0u_1v_1v_4u_4u_0,
\qquad
u_2u_3v_3v_0v_2u_2.
\]
The matching consisting of all five spokes also has two complementary 5-cycles. These cases cover every perfect matching, so there is no even 2-factor.

Thus \(T(H)\) has \(30\) vertices, and its prescribed external matching \(P\) has **no** suitable partner \(Q\).

This disproves only the prescribed-first-matching variant. Theorem 4 guarantees that this same 30-vertex graph has a suitable pair when both matchings may be chosen.

### Complexity consequence

Using the classical NP-completeness of cubic 3-edge-colourability, the triangle-expansion equivalence proves NP-hardness of the prescribed-first-matching problem.

The restriction to bridgeless inputs causes no problem: a cubic graph with a bridge is not 3-edge-colourable, so such inputs can be sent to the fixed Petersen-based negative instance above. Membership in NP follows from Lemma 1.

Therefore the prescribed-first-matching problem is **NP-complete**, even for simple bridgeless cubic graphs.

The reduction uses prescribed matchings containing many 3-edge-cuts. It does not establish hardness, or a counterexample, for the more restricted choice of \(P\) used in the \(q=5\) argument.

## 6. Remaining gap

The unconditional construction produces two perfect matchings with
\[
|P\cap Q|\le |V(G)|/10
\]
and excludes odd cuts of sizes three and five from their intersection.

At \(70\) vertices, this still permits an intersection of seven edges containing a 7-edge-cut. The argument does not exclude that possibility, nor does it control larger odd cuts at arbitrary order. The few-cycle criterion resolves some additional graphs, but not all bridgeless cubic graphs.

Thus the original conjecture remains unresolved by this attack. The proved conclusions are the quantitative and structural sufficient conditions above, together with the sharp obstruction and complexity classification for prescribing the first matching.