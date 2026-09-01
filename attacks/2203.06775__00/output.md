```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture holds when the packing number of pairwise base-disjoint pyramids is bounded, hence in particular for t at most 3, and a bounded-rank triangle-free skeleton reduction identifies permitted pyramids as the central obstruction.",
  "would_publish": false,
  "caveats": "No uniform bound or counterexample is obtained; the packing result uses Theorem 1.4 of the supplied source, and post-catalog literature was not independently verified."
}
```

# Mathematical writeup

## 1. Statement and status

All graphs below are finite and simple, and all forbidden-subgraph conditions are induced. As usual, \(t\) is a positive integer.

Let \(\mathcal C_t^*\) be the class of
\[
(C_4,\text{diamond},\text{theta},\text{prism},\text{even wheel},K_t)
\text{-free}
\]
graphs. The conjecture asks whether
\[
\sup\{\operatorname{tw}(G):G\in\mathcal C_t^*\}<\infty
\]
for each fixed \(t\).

I do not obtain a proof or a counterexample. I prove two reductions:

1. A bound in terms of a natural packing parameter for pyramids. In particular, the conjecture holds whenever the number of pyramids with pairwise vertex-disjoint bases is bounded.
2. A bounded-rank transformation of \(G\) into a triangle-free, \(C_4\)-free graph of comparable treewidth. Under this transformation, induced pyramids become a precise class of induced thetas. This makes explicit why reducing to the triangle-free case does not settle the conjecture.

The first genuinely open clique bound is \(t=4\).

---

## 2. A pyramid-packing bound

We use the following consequence of Theorem 1.4 of the supplied source.

> **Known base theorem.** For every \(t\), there is a constant \(d_t\) such that
> \[
> \operatorname{tw}(H)\le d_t
> \]
> whenever \(H\in\mathcal C_t^*\) is additionally pyramid-free.

Define:

- \(\tau_{\mathrm{pyr}}(G)\): the minimum size of a vertex set meeting every induced pyramid of \(G\);
- \(\beta(G)\): the maximum size of a family of induced pyramids whose base triangles are pairwise vertex-disjoint;
- \(\nu_\triangle(G)\): the maximum number of pairwise vertex-disjoint triangles in \(G\).

### Proposition 2.1

For every \(G\in\mathcal C_t^*\),
\[
\operatorname{tw}(G)
   \le d_t+\tau_{\mathrm{pyr}}(G)
   \le d_t+3\beta(G)
   \le d_t+3\nu_\triangle(G).
\]

#### Proof

Let \(X\) meet every induced pyramid of \(G\). Then \(G-X\) is pyramid-free: an induced pyramid in \(G-X\) would also be an induced pyramid of \(G\) disjoint from \(X\). Since all the other defining conditions of \(\mathcal C_t^*\) are hereditary,
\[
G-X\in\mathcal C_t^*.
\]
The base theorem gives
\[
\operatorname{tw}(G-X)\le d_t.
\]
Adding \(X\) to every bag of a tree decomposition of \(G-X\) gives
\[
\operatorname{tw}(G)\le d_t+|X|.
\]
Minimizing over \(X\) proves the first inequality.

Now take a maximal family \(P_1,\dots,P_m\) of pyramids whose base triangles \(B_1,\dots,B_m\) are pairwise vertex-disjoint. Put
\[
X=B_1\cup\cdots\cup B_m.
\]
If another pyramid had base disjoint from \(X\), it could be added to the family. Hence \(X\) meets the base, and therefore the vertex set, of every pyramid. Thus
\[
\tau_{\mathrm{pyr}}(G)\le |X|=3m\le 3\beta(G).
\]
Finally, the bases in such a family are pairwise vertex-disjoint triangles, so
\[
\beta(G)\le \nu_\triangle(G).
\]
This proves all claimed inequalities. \(\square\)

### Consequences

1. For every fixed \(t,k\), the subclass
   \[
   \{G\in\mathcal C_t^*:\beta(G)\le k\}
   \]
   has treewidth at most \(d_t+3k\).

2. Any counterexample sequence \(G_n\in\mathcal C_t^*\) with
   \(\operatorname{tw}(G_n)\to\infty\) must satisfy
   \[
   \beta(G_n)\ge \frac{\operatorname{tw}(G_n)-d_t}{3}\to\infty.
   \]
   Thus a counterexample cannot have all pyramids localized around a bounded vertex set; it must contain arbitrarily many pyramids with pairwise disjoint base triangles.

3. For \(t=3\), every graph in \(\mathcal C_3^*\) is triangle-free and hence pyramid-free. Therefore the conjecture follows from the base theorem for \(t=3\). The cases \(t=1,2\) are trivial. Consequently, \(t=4\) is the first unresolved case.

The parameter \(\beta\) itself is not bounded in terms of \(t\). For example, let \(P\) have a base triangle \(b_1b_2b_3\), an apex \(a\), and arms
\[
a-u_i-b_i\qquad (i=1,2,3).
\]
Its only holes are the three \(5\)-cycles obtained from pairs of arms and one base edge. It is \(K_4\)-free, diamond-free, \(C_4\)-free, and has maximum degree three; it belongs to \(\mathcal C_t^*\) for every \(t\ge4\). A disjoint union of \(m\) copies has \(\beta=m\) but treewidth \(3\). Thus the outstanding issue is interaction among many pyramids, not merely their number.

---

## 3. Clique-cutset reduction

A standard reduction is useful here.

### Lemma 3.1

If \(K\) is a clique cutset of \(G\), and \(C_1,\dots,C_s\) are the components of \(G-K\), then
\[
\operatorname{tw}(G)
 =
\max_i\operatorname{tw}\bigl(G[K\cup C_i]\bigr).
\]

#### Proof

Each graph \(G[K\cup C_i]\) is an induced subgraph of \(G\), giving one inequality. Conversely, every tree decomposition of \(G[K\cup C_i]\) has a bag containing the clique \(K\). The decompositions can be glued together at such bags. \(\square\)

Hence, if the conjecture fails, it fails on clique-cutset-free atoms. Since a \(K_t\)-free graph has clique separators of size at most \(t-1\), no width is lost in this reduction.

---

## 4. Linear maximal cliques in diamond-free graphs

### Lemma 4.1

In a diamond-free graph, two distinct maximal cliques intersect in at most one vertex.

#### Proof

Suppose distinct maximal cliques \(K,L\) contain two common vertices \(u,v\). Choose \(x\in K\setminus L\). Since \(L\) is maximal and \(x\notin L\), there is \(y\in L\) nonadjacent to \(x\). Necessarily \(y\notin K\). The graph induced by
\[
\{u,v,x,y\}
\]
has every edge except \(xy\), and hence is a diamond, a contradiction. \(\square\)

Thus every edge lying in a triangle belongs to a unique maximal clique of size at least three.

---

## 5. The triangle-free incidence skeleton

Let \(\mathcal K\) be the family of maximal cliques of \(G\) having size at least three. Construct \(S(G)\) as follows:

- retain every vertex of \(G\);
- for each \(K\in\mathcal K\), add a new vertex \(q_K\);
- delete all edges having both ends in some \(K\in\mathcal K\);
- add all edges \(q_Kv\) for \(v\in K\);
- retain all edges of \(G\) that belong to no triangle.

Thus every nontrivial maximal clique is replaced by a star. Let
\[
Q=\{q_K:K\in\mathcal K\}.
\]

### Proposition 5.1

If \(G\) is diamond-free and \(C_4\)-free, then:

1. \(S(G)\) is triangle-free and \(C_4\)-free;
2. \(Q\) is stable;
3. if \(G\) is \(K_t\)-free, every \(q_K\in Q\) has degree at most \(t-1\).

#### Proof

The set \(Q\) is stable by construction, and
\[
\deg_{S(G)}(q_K)=|K|\le t-1.
\]

A triangle of \(S(G)\) cannot contain two vertices of \(Q\). A triangle on three original vertices would be a triangle of \(G\), so its edges would have been deleted. A triangle \(q_Kuvq_K\) is also impossible because \(u,v\in K\), and hence \(uv\) was deleted. Thus \(S(G)\) is triangle-free.

Consider a \(4\)-cycle in \(S(G)\).

- If all four vertices are original, all four cycle edges were retained. A diagonal in \(G\) would form a triangle with two consecutive cycle edges, contradicting that those edges were retained. Thus these four vertices induce a \(C_4\) in \(G\), impossible.
- If exactly one vertex is \(q_K\), the cycle has the form
  \[
  q_K-u-v-w-q_K.
  \]
  Since \(u,w\in K\), \(uw\in E(G)\). Hence \(uvw\) is a triangle in \(G\), contradicting the retention of \(uv\) and \(vw\).
- If two vertices lie in \(Q\), they must alternate:
  \[
  q_K-u-q_L-v-q_K.
  \]
  Then \(u,v\in K\cap L\), contradicting Lemma 4.1.

Therefore \(S(G)\) is also \(C_4\)-free. \(\square\)

In particular, \(S(G)\) has girth at least five.

### Proposition 5.2: treewidth comparison

Let \(r=\omega(G)\). Then
\[
\operatorname{tw}(S(G))
 \le \max\{\operatorname{tw}(G),r\},
\]
and
\[
\operatorname{tw}(G)
 \le r\bigl(\operatorname{tw}(S(G))+1\bigr)-1.
\]

For \(G\in\mathcal C_t^*\), one may take \(r\le t-1\).

#### Proof

Start with a tree decomposition of \(G\). Every clique \(K\) is contained in a bag. For each \(K\in\mathcal K\), attach a leaf bag
\[
K\cup\{q_K\}
\]
to a bag containing \(K\). This covers all edges incident with \(q_K\), and gives the first inequality.

Conversely, let \((T,\mathcal B)\) be a tree decomposition of \(S(G)\). Replace every occurrence of \(q_K\) in a bag by all vertices of \(K\):
\[
B'_x=
 (B_x\cap V(G))
 \cup\bigcup_{q_K\in B_x}K.
\]
Each new bag has size at most \(r|B_x|\).

For a fixed original vertex \(v\), the bags containing \(v\) after expansion are the union of its original bag-subtree and the subtrees belonging to all \(q_K\) with \(v\in K\). Because \(vq_K\in E(S(G))\), each such subtree intersects the original subtree of \(v\); their union is connected.

An edge of \(G\) not lying in a triangle was retained in \(S(G)\). If \(uv\) lies in a maximal clique \(K\), any bag containing \(q_K\) expands to a bag containing both \(u\) and \(v\). Thus the expanded bags form a tree decomposition of \(G\), proving the second inequality. \(\square\)

Therefore, for each fixed \(t\),
\[
\sup_{G\in\mathcal C_t^*}\operatorname{tw}(G)<\infty
\quad\Longleftrightarrow\quad
\sup_{G\in\mathcal C_t^*}\operatorname{tw}(S(G))<\infty.
\]
This is an exact quantitative reformulation in terms of triangle-free, \(C_4\)-free graphs with a distinguished stable set \(Q\) of bounded-degree vertices.

---

## 6. Pyramids become mixed thetas

The skeleton does not generally belong to \(\mathcal C_3^*\): a permitted pyramid in \(G\) turns into an induced theta in \(S(G)\).

Call an induced theta \(\Theta\) in \(S(G)\) **faithful** if, for every \(K\in\mathcal K\) with \(q_K\notin V(\Theta)\),
\[
|K\cap V(\Theta)\cap V(G)|\le1.
\]
This condition says that no edge of \(G\) between selected original vertices is hidden through a clique node omitted from \(\Theta\).

### Proposition 6.1

There is the following correspondence.

1. Every induced pyramid of \(G\) expands in \(S(G)\) to a faithful induced theta with one branch vertex in \(Q\) and the other in \(V(G)\).
2. Conversely, every faithful induced theta of \(S(G)\) with one branch vertex in \(Q\) and the other in \(V(G)\) contracts to an induced pyramid of \(G\).

#### Proof

Let \(P\) be an induced pyramid with apex \(a\), base \(b_1b_2b_3\), and arms \(R_i\) from \(a\) to \(b_i\). Let \(K\) be the unique maximal clique containing the base triangle.

Replace the base triangle by the star
\[
q_Kb_1,\ q_Kb_2,\ q_Kb_3.
\]
Whenever an arm edge \(uv\) lies in a maximal clique \(L\), replace that edge by \(u-q_L-v\). The three expanded arms, together with \(q_K\), form three internally disjoint \(q_K\)-\(a\) paths.

There are no unwanted edges. Indeed, if an inserted \(q_L\) had a third selected neighbor, then the corresponding clique \(L\) would produce an extra edge in the induced pyramid. Likewise, two selected vertices in an omitted maximal clique would be adjacent in \(G\), contrary to the inducedness of the pyramid. Hence the resulting theta is induced and faithful.

Conversely, let \(\Theta\) be a faithful theta with branch vertices \(q_K\) and \(a\in V(G)\). Let \(b_1,b_2,b_3\) be the three neighbors of \(q_K\) in \(\Theta\). They lie in \(K\) and form a triangle in \(G\).

Suppress each other clique node \(q_L\) occurring internally on a theta path, replacing
\[
u-q_L-v
\]
by the edge \(uv\). Delete \(q_K\). This gives three internally vertex-disjoint paths from \(a\) to \(b_1,b_2,b_3\).

At most one of these paths can have length one. Suppose \(a\) is adjacent to \(b_1,b_2\). If \(a\) is not adjacent to \(b_3\), then
\[
G[\{a,b_1,b_2,b_3\}]
\]
is a diamond. If \(a\) is adjacent to all three, then these four vertices lie in a maximal clique \(L\). The cliques \(K\) and \(L\) share at least \(b_1,b_2\), so Lemma 4.1 gives \(K=L\). Hence \(a\in K\), and \(aq_K\in E(S(G))\), contradicting that \(a,q_K\) are nonadjacent branch vertices of an induced theta.

Finally, there are no extra edges after suppression. An edge of \(G\) between two selected original vertices is either:

- an edge retained in \(S(G)\), in which case inducedness of \(\Theta\) makes it a path edge; or
- contained in a maximal clique \(L\). If \(q_L\in\Theta\), its two selected neighbors are consecutive on one path. If \(q_L\notin\Theta\), faithfulness forbids two selected vertices of \(L\), except for the intended base clique \(K\).

Thus the contracted graph is precisely an induced pyramid. \(\square\)

There are analogous restrictions on other faithful thetas:

- If both branch vertices are original and none of the three theta paths is of the form
  \[
  x-q_K-y,
  \]
  contraction gives an induced theta in \(G\), which is forbidden.
- If both branch vertices are clique nodes \(q_K,q_L\), and their two triples of theta-neighbors are disjoint, contraction gives an induced prism in \(G\), also forbidden.

Consequently, faithful thetas in \(S(G)\) can only be:

1. mixed \(Q\)-to-\(V(G)\) thetas, corresponding to pyramids;
2. original-to-original thetas having a length-two clique shortcut;
3. clique-node-to-clique-node thetas in which the endpoint triangles overlap in a selected vertex.

Not every theta of \(S(G)\) is necessarily faithful, and controlling the nonfaithful ones is part of the unresolved difficulty.

---

## 7. Lower bounds on any possible constant

Two elementary examples show that any valid \(c_t\) must satisfy
\[
c_t\ge \max\{t-2,3\}\qquad (t\ge3).
\]

First, \(K_{t-1}\in\mathcal C_t^*\): every induced subgraph of a complete graph is complete, so it contains none of the noncomplete forbidden configurations. Since
\[
\operatorname{tw}(K_{t-1})=t-2,
\]
we have \(c_t\ge t-2\).

For the second lower bound, let \(W\) consist of a \(9\)-cycle with three equally spaced vertices \(x_1,x_2,x_3\), together with a vertex \(c\) adjacent exactly to \(x_1,x_2,x_3\). Thus each of the three rim sectors between consecutive \(x_i\)'s has length three.

The only induced holes of \(W\) are:

- the rim \(C_9\);
- the three \(C_5\)'s formed by \(c\) and one rim sector.

Hence every hole is odd. The graph is triangle-free, has no \(C_4\), and has maximum degree three. It therefore has no diamond or prism, no even wheel, and no induced theta: an induced theta always contains an even hole, since among its three path lengths two have the same parity.

Suppressing the degree-two rim vertices turns \(W\) into \(K_4\). Thus \(W\) is a subdivision of \(K_4\), and
\[
\operatorname{tw}(W)=3.
\]
Since \(W\in\mathcal C_t^*\) for every \(t\ge3\), this gives \(c_t\ge3\).

---

## 8. Precise remaining gap

The reductions above leave the following unresolved core.

For a hypothetical counterexample sequence, one may assume:

1. the graphs are clique-cutset-free;
2. they contain arbitrarily many induced pyramids with pairwise vertex-disjoint base triangles;
3. their skeletons \(S(G)\) have unbounded treewidth, girth at least five, and a distinguished stable set \(Q\) whose vertices have degree between \(3\) and \(t-1\);
4. faithful induced thetas in the skeleton have only the exceptional forms described above.

The missing theorem would have to show that these translated restrictions, together with the even-wheel prohibition in the original graph, force bounded treewidth. I do not have such an argument.

In particular, the natural attempt “replace every maximal clique by a star and apply the triangle-free case” fails exactly because an allowed pyramid becomes a mixed induced theta. For the seven-vertex pyramid with arms \(a-u_i-b_i\), the skeleton is the theta consisting of the three paths
\[
q_K-b_i-u_i-a,\qquad i=1,2,3.
\]
Thus the skeleton reduction is quantitatively exact but does not itself complete the proof. No explicit unbounded-treewidth family satisfying all the original forbidden conditions is produced here.