```json
{
  "verdict": "ill_posed",
  "confidence": "high",
  "one_line": "The quoted remark does not specify a forbidden family or an if-and-only-if assertion, so it has no determinate truth value as a conjecture.",
  "would_publish": false,
  "caveats": "A precise completeness conjecture may be recoverable from the paper's defined examples, but it is not present in the supplied statement."
}
```

## 1. Statement and logical status

A graph is **strongly perfect** if every induced subgraph has a stable set meeting every nonempty maximal clique. This is a hereditary property, so it always has the tautological characterization

\[
G\text{ is strongly perfect}
\quad\Longleftrightarrow\quad
G\text{ contains no induced minimally non-strongly-perfect graph}.
\]

Thus the assertion that outerplanar strongly perfect graphs “can be characterized through minimal examples” is substantive only after specifying a family \(\mathcal F\) and asserting, for example,

\[
G\text{ outerplanar is strongly perfect}
\quad\Longleftrightarrow\quad
G\text{ has no induced subgraph in }\mathcal F. \tag{1}
\]

The supplied statement does not define \(\mathcal F\), say which operations on the paper’s examples are allowed, or explicitly assert the sufficiency direction in (1). Consequently, it is not a proposition that can presently be proved or disproved.

The following gives rigorous partial structure that any precise formulation must accommodate.

---

## 2. Exact-one formulation for outerplanar graphs

For a finite graph \(H\), a stable set \(S\) meets every maximal clique if and only if

\[
|S\cap Q|=1
\]

for every maximal clique \(Q\) of \(H\). The forward implication uses stability. Conversely, if the displayed equations hold and two adjacent vertices belonged to \(S\), an extension of that edge to a maximal clique would meet \(S\) at least twice.

Since an outerplanar graph has no \(K_4\), its maximal cliques are precisely:

1. isolated vertices;
2. edges contained in no triangle;
3. triangles.

Therefore, writing \(x_v=1\) when \(v\in S\), an outerplanar graph \(H\) has a strong stable set exactly when the following system has a \(0\)-\(1\) solution:

\[
\begin{aligned}
x_v&=1 &&\text{for every isolated vertex }v,\\
x_u+x_v&=1 &&\text{for every edge }uv\text{ contained in no triangle},\\
x_a+x_b+x_c&=1 &&\text{for every triangle }abc.
\end{aligned} \tag{2}
\]

This formulation is useful, but strong perfection requires (2) to be feasible for every induced subgraph; deleting vertices can turn formerly triangular edges into maximal edges.

### Triangle-free special case

If \(H\) is triangle-free, then it has a strong stable set if and only if it is bipartite.

Indeed, in a strong stable set every edge has exactly one endpoint in \(S\), so both \(S\) and \(V(H)\setminus S\) are stable. Conversely, in each nontrivial bipartite component one bipartition class meets every edge, and all isolated vertices can be added.

Hence:

\[
\boxed{\text{A triangle-free graph is strongly perfect if and only if it is bipartite.}}
\]

In particular, the minimally non-strongly-perfect triangle-free outerplanar graphs are exactly the odd holes.

---

## 3. A structural restriction on minimal obstructions

A vertex \(v\) is simplicial if \(N[v]\) is a clique.

### Lemma

If \(v\) is simplicial and \(G-v\) has a strong stable set, then \(G\) has a strong stable set.

### Proof

Let \(S\) be a strong stable set of \(G-v\). The clique \(N[v]\) is maximal in \(G\).

- If \(S\cap N(v)\neq\varnothing\), retain \(S\).
- If \(S\cap N(v)=\varnothing\), use \(S\cup\{v\}\).

Every maximal clique other than \(N[v]\) is a maximal clique of \(G-v\), so it is already met. ∎

Consequently, an induced-minimal non-strongly-perfect graph has no simplicial vertex. It is also connected. Since every outerplanar graph is \(2\)-degenerate, every minimal outerplanar obstruction has a degree-two vertex, and every such vertex has two nonadjacent neighbors. This is a useful starting point for any attempted completeness proof.

---

## 4. Odd-ear decorations of maximal outerplanar graphs

An **odd ear on an edge \(uv\)** will mean an induced \(u\)-\(v\) path of odd length at least three, internally disjoint from the rest of the graph, while the edge \(uv\) itself remains present.

Let \(T\) be a maximal outerplanar graph with its unique proper \(3\)-coloring

\[
\kappa:V(T)\longrightarrow \{1,2,3\}.
\]

Let \(M\) be a set of boundary edges of \(T\), and add an internally disjoint odd ear to each edge of \(M\). Call the resulting outerplanar graph \(G(T,M)\). For \(e=uv\in M\), let \(m(e)\) be the unique color not occurring on \(u,v\).

### Proposition

The graph \(G(T,M)\) has a strong stable set if and only if

\[
\{m(e):e\in M\}\neq \{1,2,3\}. \tag{3}
\]

### Proof

The maximal cliques inherited from \(T\) are its triangular faces. If \(x_v\) satisfies the triangle equations in (2), then on two adjacent triangles \(uvz\) and \(uvw\),

\[
x_u+x_v+x_z=1,\qquad x_u+x_v+x_w=1,
\]

and hence \(x_z=x_w\). Traversing the weak dual tree shows that the selected vertices of \(T\) must be exactly one of its three color classes. Conversely, each color class meets every triangle exactly once.

An odd ear on \(uv\) consists entirely of maximal edges. Alternation along its odd number of edges forces \(x_u\neq x_v\). Thus a chosen color class extends over this ear exactly when that color occurs on one of \(u,v\), equivalently when it is not \(m(uv)\). A common color class exists for all ears exactly when some color is absent from the set of missing colors. ∎

This completely determines whether the graph itself has a strong stable set for this substantial subclass. It does not by itself characterize strong perfection, because induced subgraphs must also be considered.

---

## 5. An explicit outerplanar minimal obstruction family

Let \(a_1a_2a_3a_1\) be a triangle. For each \(i\) modulo \(3\), add an internally disjoint induced path \(P_i\) from \(a_i\) to \(a_{i+1}\), of odd length at least three, with no additional edges. Denote the graph by

\[
F(\ell_1,\ell_2,\ell_3),
\]

where \(\ell_i\) is the length of \(P_i\). This graph is outerplanar: put the three paths consecutively on the outer boundary and draw the central triangle as three noncrossing chords.

### Proposition

Every \(F(\ell_1,\ell_2,\ell_3)\) is minimally non-strongly-perfect.

### Proof

Along each \(P_i\), the maximal-edge equations force

\[
x_{a_i}+x_{a_{i+1}}=1.
\]

Summing these three equations gives

\[
2(x_{a_1}+x_{a_2}+x_{a_3})=3,
\]

which is impossible. Thus \(F\) has no strong stable set.

Now let \(H\) be a proper induced subgraph of \(F\).

If at least one of \(a_1,a_2,a_3\) is absent, then \(H\) is bipartite. For example, after deleting \(a_3\), the only possible cycle is \(P_1+a_1a_2\), which is even; everything else is a collection of attached paths. Hence \(H\) has a strong stable set.

Suppose all three central vertices remain. Since \(H\neq F\), at most two of the paths \(P_i\) remain intact. Choose exactly one central vertex as follows:

- if no \(P_i\) is intact, choose any \(a_i\);
- if one \(P_i\) is intact, choose one endpoint of that path;
- if two \(P_i\) are intact, choose their common endpoint.

This meets the central triangle exactly once and gives opposite values at the endpoints of each intact odd path. Every broken path is a disjoint union of path fragments, each of which can be assigned alternating values; isolated retained vertices are selected. Thus (2) is feasible.

Every induced subgraph of a proper induced subgraph is again a proper induced subgraph of \(F\). Therefore every proper induced subgraph is strongly perfect, proving minimality. ∎

These graphs are also perfect: an induced subgraph missing a central vertex is bipartite, while one retaining the central triangle is \(3\)-colorable and has clique number three. Thus odd holes alone are far from characterizing outerplanar strongly perfect graphs.

---

## 6. A cut-vertex obstruction family

There are also minimal outerplanar obstructions arising from incompatible requirements at a cut vertex.

Take two triangles \(xab\) and \(xcd\), intersecting only in \(x\). Add internally disjoint odd ears on \(xa\), \(xb\), and \(cd\), and no other edges. Call the resulting graph \(D\).

The two odd ears in the first triangle give

\[
x_x+x_a=1,\qquad x_x+x_b=1,
\]

while \(x_x+x_a+x_b=1\). Hence every strong stable set of that block would have

\[
x_x=1,\qquad x_a=x_b=0.
\]

In the second block, the odd ear on \(cd\) gives \(x_c+x_d=1\), and the triangle equation gives

\[
x_x+x_c+x_d=1,
\]

forcing \(x_x=0\). Hence \(D\) has no strong stable set.

It is also induced-minimal. The key local observations are:

- In the \(xab\)-block, once any vertex of either odd ear or of the triangle other than \(x\) is deleted, the remaining induced subgraph admits solutions with either prescribed value of \(x\).
- In the \(xcd\)-block, once the block is not retained in full, it likewise admits either prescribed value of \(x\).

These assertions follow directly from (2): a broken ear imposes no relation between its two original endpoints, while its retained fragments can be alternated; if a triangle loses a vertex, its surviving edge becomes a maximal edge and merely forces opposite endpoint values.

Thus, in every proper induced subgraph retaining \(x\), at least one of the two blocks is no longer complete:

- if the first block is complete, choose \(x=1\) and extend through the incomplete second block;
- if the second is complete, choose \(x=0\) and extend through the incomplete first block;
- if both are incomplete, choose either value consistently.

If \(x\) is deleted, the first block becomes a forest and the second becomes an induced subgraph of an even cycle, so the result is bipartite. Hence every proper induced subgraph has a strong stable set, and \(D\) is minimally non-strongly-perfect.

This family shows that a complete characterization must account not only for 2-connected configurations but also for compatibility across cut vertices.

---

## 7. Complexity result for the outerplanar problem

Although a forbidden-subgraph characterization is not obtained here, recognition is tractable in a strong formal sense.

Strong perfection is expressible in monadic second-order logic by

\[
\forall U\subseteq V\ \exists S\subseteq U:
\left[
\operatorname{Stable}(S)
\land
\forall K\subseteq U\,
\bigl(\operatorname{MaxClique}(K,U)\Rightarrow K\cap S\neq\varnothing\bigr)
\right].
\]

Here \(\operatorname{MaxClique}(K,U)\) is expressible by saying that \(K\) is a nonempty clique contained in \(U\), and that no vertex of \(U\setminus K\) is adjacent to every vertex of \(K\).

Outerplanar graphs have treewidth at most two. Therefore the standard bounded-treewidth MSO model-checking theorem yields:

\[
\boxed{\text{Strong perfection of a promised outerplanar graph is decidable in }O(|V(G)|)\text{ time}.}
\]

This is an algorithmic recognition result rather than a human-readable structural characterization.

---

## 8. Remaining gap

The substantive unproved statement would have to be something like:

> For an explicitly defined collection \(\mathcal F\) of the paper’s parameterized examples, every outerplanar graph with no induced member of \(\mathcal F\) is strongly perfect.

Nothing above proves that sufficiency direction. The exact-one reduction, structural lemma, decorated-triangulation proposition, and explicit minimal obstruction families provide concrete ingredients and tests, but they do not establish that the examples in the source paper are exhaustive. Without an explicit definition of the intended family \(\mathcal F\), there is no precise conjecture to resolve.