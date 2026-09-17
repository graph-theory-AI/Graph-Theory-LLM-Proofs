```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "Both conjectures hold for countable graphs with a finite dominating set, via a finite-boundary lifting theorem that also extends the finite-twin case.",
  "would_publish": false,
  "caveats": "The unrestricted conjectures remain unresolved; Hamilton circles use the Hausdorff vertex–end topology, and no novelty is claimed."
}
```

# A finite-boundary lifting theorem

Neither conjecture is resolved here. I prove a stronger special case than the finite-twin result in the previous attempt:

> **Corollary.** Let \(G\) be a countably infinite graph with a finite dominating set.
> - If \(G\) is connected, then \(G^3\) has a Hamilton circle.
> - If \(G\) is 2-connected, then \(G^2\) has a Hamilton circle.

The lifting theorem below also subsumes the previous finite-twin-inflation result and allows arbitrary adjacency patterns inside the infinite part.

The main improvement is an edge-selection argument: sufficiently many retained vertices in an infinite piece force the kernel’s Hamilton circle to use an edge **entirely inside that piece**. We can expand this edge without requiring any twin automorphisms.

I reprove the two-ray lemma and the end-control argument rather than rely on the unverified earlier proof. The only Hamiltonicity results used are the finite and locally finite square and cube theorems supplied in the question.

## 1. Conventions and main statement

Graphs are simple. For an integer \(k\geq 1\), vertices are adjacent in \(G^k\) when their distance in \(G\) is at most \(k\).

As in the previous attempt, \(\widehat H\) denotes the Hausdorff vertex–end realization of \(H\): ends are defined by finite vertex separators, and end neighbourhoods have their boundary edges cut in their interiors. Dominated ends are not identified with vertices. A Hamilton circle is a subspace homeomorphic to \(S^1\) containing every vertex.

All ends considered for a power \(G^k\) are ends of the **power graph**, not of \(G\).

### Theorem 1: finite-boundary lifting

Let \(G\) be countably infinite and connected. Set either

- \(k=3\); or
- \(k=2\), with the additional assumption that \(G\) is 2-connected.

Suppose there is a set \(U\subseteq V(G)\) such that:

1. \(G-U\) is locally finite;
2. the external boundary
   \[
   N_G(U)\setminus U
   \]
   is finite;
3. the induced graph
   \[
   G^k[U]
   \]
   has finite independence number.

Then \(G^k\) has a Hamilton circle.

Here \(G^k[U]\) is the subgraph induced by \(U\) **after taking the power**; it need not equal \((G[U])^k\).

In particular, taking \(U=V(G)\) proves the corresponding conjecture whenever the relevant power has finite independence number.

---

## 2. Two elementary lemmas

Call a countably infinite graph \(X\) **finitely deletion-connected** if
\[
X-A\text{ is connected for every finite }A\subseteq V(X).
\tag{1}
\]

### Lemma 2: a spanning arc

Suppose \(X\) satisfies (1). For any distinct \(a,b\in V(X)\), there are two vertex-disjoint rays starting at \(a\) and \(b\) whose vertex sets partition \(V(X)\).

If \(X\subseteq H\), these rays together with their common \(H\)-end form an arc in \(\widehat H\), with endpoints \(a,b\), containing every vertex of \(X\).

#### Proof

Enumerate \(V(X)\). Start with the two one-vertex paths \(P_a=a\) and \(P_b=b\).

Alternate between extending the two paths. At a stage, let \(p\) be the endpoint of the active path and let \(w\) be the first unused vertex in the enumeration. Delete all currently used vertices except \(p\). By (1), a finite \(p\)-\(w\) path remains. Choose it simple and append it to the active path.

Both paths grow at every second stage, remain disjoint, and exhaust the enumeration. Their unions are the required rays.

For any finite \(S\subseteq V(H)\), the graph \(X-(S\cap V(X))\) is connected. Thus the rays have tails in the same component of \(H-S\), so they represent the same end \(\omega\) of \(H\).

Parametrize one ray from \(a\) towards the midpoint of an interval and the other from that midpoint towards \(b\), mapping the midpoint to \(\omega\). Continuity at the midpoint follows from the definition of end neighbourhoods. This is a continuous injection from a compact interval into the Hausdorff space \(\widehat H\), hence an embedded arc. ∎

In particular, a graph satisfying (1) itself has a Hamilton circle: choose adjacent \(a,b\) and add the edge \(ab\) to the arc. The construction does not use \(ab\) in either ray.

### Lemma 3: finite independence gives finitely many robust pieces

Let \(J\) be a countable graph with \(\alpha(J)<\infty\). There is a finite set \(Z\subseteq V(J)\) such that \(J-Z\) has finitely many components, each infinite and finitely deletion-connected.

The family of components may be empty when \(J\) is finite.

#### Proof

The finite case is immediate, so suppose \(J\) is infinite and write \(m=\alpha(J)\).

Let \(D\) be the set of vertices of finite degree in \(J\). If \(D\) were infinite, greedily choosing vertices of \(D\) would produce an infinite independent set: each chosen vertex excludes only finitely many further choices. Hence \(D\) is finite.

For any finite \(Z\supseteq D\), every vertex of \(J-Z\) has infinite degree within its component. In particular, every component is infinite. Also, \(J-Z\) has at most \(m\) components, since representatives from distinct components form an independent set.

Start with \(Z=D\). If a component \(K\) of \(J-Z\) is not finitely deletion-connected, choose a finite \(A\subseteq V(K)\) such that \(K-A\) is disconnected, and replace \(Z\) by \(Z\cup A\).

This strictly increases the number of components. No other component disappears, and every new component is still infinite. Since the number of components is always at most \(m\), this process terminates after finitely many steps. At termination every component has the required property. ∎

The lifting argument will actually use only the conclusion of Lemma 3, not finite independence itself.

---

## 3. Finite 2-connected kernels

We will use the following standard fact, including for non-locally-finite graphs.

### Lemma 4

Every finite vertex set of a 2-connected graph \(G\) is contained in a finite 2-connected subgraph of \(G\).

#### Proof

Start with a finite cycle. Given a finite 2-connected subgraph \(B\) and a desired vertex \(x\notin V(B)\), 2-connectivity supplies two \(x\)-\(B\) paths, internally disjoint and ending at distinct vertices of \(B\). Truncating at their first intersections with \(B\), their union is an ear through \(x\). Adding it to \(B\) preserves 2-connectivity.

For completeness, the two-fan assertion reduces to finite Menger. Choose an \(x\)-\(B\) path \(P\). For each \(z\in V(P)\setminus\{x\}\), use connectivity of \(G-z\) to choose a finite path from \(x\) to \(V(B)\setminus\{z\}\) avoiding \(z\). In the finite union of these paths, \(P\), and \(B\), no single vertex separates \(x\) from \(B\). The finite two-fan lemma therefore applies.

Adding ears for the finitely many prescribed vertices finishes the construction. ∎

---

## 4. Proof of Theorem 1

Put
\[
H=G^k,\qquad R=V(G)\setminus U.
\]

Apply Lemma 3 to \(H[U]\). Obtain a finite \(Z\subseteq U\) such that
\[
H[U]-Z=H[U_1]\;\dot\cup\;\cdots\;\dot\cup\;H[U_t],
\tag{2}
\]
where each \(H[U_i]\) is infinite and finitely deletion-connected.

### 4.1. The boundary remains finite in the power

Let
\[
D=N_G(U)\setminus U,
\qquad
B=N_H(U)\setminus U.
\]

A \(G\)-path of length at most \(k\) from \(U\) to \(x\in R\), after its last departure from \(U\), starts at a vertex of \(D\) and stays in \(G[R]\). Consequently,
\[
B\subseteq
\{x\in R:d_{G[R]}(x,D)\leq k-1\}.
\]
The right-hand side is finite because \(D\) is finite and \(G[R]\) is locally finite. Thus
\[
|B|<\infty.
\tag{3}
\]

Moreover, by (2),
\[
N_H(U_i)\setminus U_i\subseteq B\cup Z
\quad\text{for every }i.
\tag{4}
\]

### 4.2. Constructing a locally finite kernel

Set
\[
q=|B|+|Z|+1.
\]
Choose \(q\) distinct vertices from each \(U_i\).

Choose a finite subgraph \(K\subseteq G\) containing:

- every vertex of \(B\cup Z\);
- all the chosen vertices;
- enough additional vertices to have at least three vertices.

For \(k=3\), choose \(K\) connected. For \(k=2\), choose \(K\) 2-connected, using Lemma 4.

Now define
\[
F=G[R\cup V(K)],
\qquad
T=U\cap V(F)=U\cap V(K).
\]
In particular, \(T\) is finite and \(Z\subseteq T\).

The graph \(F\) is locally finite. Indeed:

- a vertex in \(R\) has finitely many neighbours in \(G[R]\), plus at most \(|T|\) retained neighbours in \(U\);
- a vertex in \(T\) has its retained neighbours contained in the finite set \(T\cup D\).

Also, \(F\) is connected. To see this, take \(v\in V(F)\setminus V(K)\), so \(v\in R\), and follow a \(G\)-path from \(v\) to \(K\), stopping at its first vertex in \(K\). This initial segment cannot enter \(U\) earlier: its last vertex before entering \(U\) would belong to \(D\subseteq B\subseteq V(K)\). Hence the segment lies in \(F\).

When \(k=2\), the same argument works after deleting any \(x\in V(F)\). The graph \(K-x\) is connected, and connectivity of \(G-x\) supplies a path from every vertex outside \(K\) to \(K-x\). Its initial segment again lies in \(F-x\). Thus \(F\) is 2-connected.

Set
\[
H_0=F^k.
\]
Then \(H_0\) is locally finite and is a subgraph of \(H\). By the stipulated finite or locally finite theorem, \(H_0\) has a Hamilton circle \(C\).

Notice that we do **not** need distances between retained vertices to remain unchanged.

### 4.3. Controlling end identifications

We now justify regarding \(C\) as a circle in \(\widehat H\).

Delete
\[
S_*=B\cup T.
\]

First,
\[
H_0-S_*=H[R\setminus B].
\tag{5}
\]
The nontrivial inclusion follows as follows. If \(x,y\in R\setminus B\) are adjacent in \(H\), choose a \(G\)-path of length at most \(k\) between them. This path cannot meet \(U\), since otherwise \(x\) would belong to \(B\). The path therefore lies in \(G[R]\subseteq F\), so \(xy\in E(H_0)\).

Because \(B\) contains all external \(H\)-neighbours of \(U\), equations (2) and (5) give the exact decomposition
\[
H-S_*
=
(H_0-S_*)
\;\dot\cup\;
\bigdotcup_{i=1}^{t}H[U_i\setminus T].
\tag{6}
\]

Each \(H[U_i\setminus T]\) is still finitely deletion-connected. It therefore contributes exactly one end, say \(\omega_i\), of \(H\).

Equation (6) shows that:

- all ends of \(H_0\) remain distinct ends of \(H\);
- the ends \(\omega_1,\ldots,\omega_t\) are distinct from one another and from every old end;
- there are no other ends of \(H\).

At old ends, neighbourhoods can be chosen using finite separators containing \(S_*\); the component graphs there are unchanged by (6). Thus the inclusion of \(H_0\) extends continuously and injectively to its vertex–end realization. In particular, \(C\) remains an embedded circle in \(\widehat H\).

This finite-separator argument is what prevents accidental mergers of ends used by the construction.

### 4.4. Forcing suitable edges of the old circle

For every \(i\), the circle \(C\) contains at least \(q\) vertices of \(U_i\), because all selected vertices were retained in \(F\).

I claim that \(C\) has an edge with both endpoints in \(U_i\).

Otherwise, the two circle edges at each vertex of \(C\cap U_i\) would both leave \(U_i\). By (4), they would all meet \(B\cup Z\). But each vertex of \(B\cup Z\) has only two incident edges on \(C\). Therefore
\[
2|V(C)\cap U_i|\leq 2|B\cup Z|,
\]
contradicting
\[
|V(C)\cap U_i|\geq q>|B\cup Z|.
\]

Choose such an edge
\[
e_i=a_i b_i.
\]

This counting argument is the replacement for the twin assumption.

### 4.5. Expanding the selected edges

Define
\[
W_i=(U_i\setminus T)\cup\{a_i,b_i\}.
\]
The graph \(H[W_i]\) is obtained from \(H[U_i]\) by deleting finitely many vertices, so it remains finitely deletion-connected.

Apply Lemma 2 to obtain an arc \(A_i\) with endpoints \(a_i,b_i\) that contains every vertex of \(W_i\). Its end is \(\omega_i\).

The arc \(A_i\) meets \(C\) exactly at \(a_i,b_i\):

- its other vertices were not retained in \(F\);
- its end \(\omega_i\) is not an old end.

Different \(A_i\) are disjoint, including at their ends.

Replace each edge \(e_i\) of \(C\) by \(A_i\). These are finitely many replacements by internally disjoint arcs having the same endpoints. The result is again a circle: the replacement gives a continuous injection of \(S^1\) into the Hausdorff space \(\widehat H\).

Every vertex of \(F\) remains on the circle. Every vertex omitted from \(F\) belongs to some \(U_i\setminus T\), and hence lies on \(A_i\). The resulting circle is therefore Hamiltonian in \(H=G^k\). ∎

### Stronger form actually proved

The proof only used the following replacement for condition 3:

> There is a finite \(Z\subseteq U\) such that \(G^k[U]-Z\) has finitely many components, each infinite and finitely deletion-connected.

Thus this decomposition condition also suffices. Finite independence number is one convenient way to guarantee it.

---

## 5. Consequences

### 5.1. Finite dominating sets

Let \(D\) be a finite dominating set of \(G\). Every closed neighbourhood \(N_G[d]\), for \(d\in D\), is a clique in \(G^2\), and hence in \(G^3\). Since these finitely many sets cover \(V(G)\),
\[
\alpha(G^k)\leq |D| \qquad(k\geq2).
\]

Apply Theorem 1 with \(U=V(G)\). This proves both assertions announced at the beginning.

In particular, this extends the finite-vertex-cover conclusion of the previous attempt: in a connected nontrivial graph, a vertex cover is also a dominating set, but finite dominating sets allow completely arbitrary edges among the vertices outside the set.

### 5.2. Recovering the finite-twin class

For a finite twin inflation from the previous attempt, let \(U\) be the union of its finitely many infinite bags.

Then:

- \(G-U\) is locally finite;
- \(U\) has finite external boundary, because the quotient is locally finite and only finitely many bags are inflated;
- every bag is a clique in \(G^k\) for \(k\geq2\).

Consequently,
\[
\alpha(G^k[U])
\leq \text{number of infinite bags}.
\]
Theorem 1 applies. Thus the earlier special case is recovered without needing its distance-preserving retraction or any twin-based edge replacement.

### 5.3. A genuinely non-twin example

Take two disjoint rays
\[
x_0x_1x_2\ldots,\qquad y_0y_1y_2\ldots.
\]
Add vertices \(a,b\), all edges \(ax_i\) and \(by_i\), and the edges
\[
ab,\qquad x_0y_0.
\]

This graph is 2-connected. Deleting a hub leaves its ray attached to the other cone through \(x_0y_0\); deleting a ray vertex leaves all remaining vertices connected through the two hubs. The set \(\{a,b\}\) dominates the graph.

There is no infinite twin class: the ray vertices have distinct private adjacency patterns, while only the hubs have infinite degree. Thus this graph is not a finite twin inflation of a locally finite graph.

Nevertheless, its square has a Hamilton circle by the corollary. This is not merely a complete-square example: deleting \(\{a,b,x_0,y_0\}\) from the square leaves two infinite cliques with no edges between them, so the square has two ends.

---

## 6. Another cube case: almost every vertex has infinite degree

The stronger form of the lifting theorem gives an additional class not implied by finite independence.

### Proposition 5

If a countably infinite connected graph \(G\) has only finitely many vertices of finite degree, then \(G^3\) has a Hamilton circle.

#### Proof

First suppose a connected graph \(X\) has infinite degree at every vertex. For any finite \(A\subseteq V(X)\), choose a map
\[
r:V(X)\longrightarrow V(X)\setminus A
\]
that fixes vertices outside \(A\), and maps each \(v\in A\) to a neighbour outside \(A\).

For every edge \(uv\in E(X)\), the walk
\[
r(u),u,v,r(v)
\]
has length at most three, after stationary steps are omitted. Thus its images are equal or adjacent in \(X^3-A\). Mapping any finite \(X\)-path this way shows that \(X^3-A\) is connected. Hence \(X^3\) is finitely deletion-connected.

Now let
\[
L=\{v\in V(G):\deg_G(v)<\infty\},
\]
which is finite by hypothesis. If \(L\neq\varnothing\), then \(G-L\) has only finitely many components: each is incident with one of the finitely many edges leaving \(L\). If \(L=\varnothing\), there is just the component \(G\).

Every component \(X\) of \(G-L\) has infinite degree at every vertex, so \(X^3\) is finitely deletion-connected.

Put
\[
S=N_G[L],
\]
a finite set. Distinct components of \(G-L\) cannot have adjacent vertices in \(G^3-S\): any connecting \(G\)-path must meet \(L\), while both endpoints have distance at least two from \(L\), giving length at least four.

Consequently, \(G^3-S\) has finitely many components. Each contains, as a spanning subgraph, \(X^3-(S\cap V(X))\) for the corresponding component \(X\), so each is finitely deletion-connected.

Apply the stronger lifting theorem with \(U=V(G)\) and \(Z=S\). ∎

For example, this covers the countable tree in which every vertex has infinite degree. Its cube can have an infinite independent set: choose one depth-two vertex in each of infinitely many different root branches. Thus Proposition 5 is not a consequence of the finite-independence corollary.

---

## 7. What remains unresolved

The lifting proof requires two forms of control:

1. after the infinite region is trimmed, a locally finite kernel remains;
2. a **finite separator** distinguishes the kernel’s ends from finitely many new one-ended regions.

A general countable graph need not admit such a decomposition. Infinite-degree behaviour may occur throughout the graph, and infinite regions can have infinitely many different attachments or infinitely many finite-degree vertices in the relevant power. Then the finite edge-counting and finite arc-replacement argument does not apply.

In particular, this argument does not establish either unrestricted conjecture. Its proved contribution is the finite-boundary lifting theorem, the finite-dominating-set corollary, and the additional cube case in Proposition 5.