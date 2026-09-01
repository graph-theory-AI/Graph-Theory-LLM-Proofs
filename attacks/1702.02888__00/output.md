```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The general problem remains open, but equality is completely characterized for 3-degenerate planar graphs by a K4-factor, and arbitrary instances reduce exactly to a minimum-degree-at-least-four core.",
  "would_publish": false,
  "caveats": "No characterization or polynomial algorithm is obtained for the residual degree-4/5 cores; novelty of the special-case results was not literature-checked."
}
```

# 1. Statement of the partial result

All graphs below are finite and simple. Write
\[
\sigma(G):=4\alpha(G)-|V(G)|.
\]
The Four Colour Theorem says that \(\sigma(G)\ge 0\) for every planar graph \(G\). The original decision problem asks whether \(\sigma(G)>0\).

The main partial result is the following.

**Theorem 1.**  
Let \(G\) be a 3-degenerate planar graph. Then the following are equivalent.

1. \(\alpha(G)=|V(G)|/4\).
2. \(G\) has a \(K_4\)-factor, i.e. \(V(G)\) can be partitioned into vertex-disjoint copies of \(K_4\).
3. \(G\) can be reduced to the empty graph by repeatedly choosing a degree-three vertex whose three neighbors form a triangle and deleting its closed neighborhood.

Consequently, on 3-degenerate planar graphs one can decide in polynomial time whether \(\alpha(G)>|V(G)|/4\), without computing a maximum independent set.

The degeneracy threshold is sharp for the \(K_4\)-factor characterization: the square antiprism is a 4-degenerate planar graph on eight vertices with independence number two and with no \(K_4\).

For unrestricted planar graphs, the same argument gives an exact reduction rule: repeatedly delete a degree-three vertex whose neighborhood is a triangle. This preserves \(\sigma\). If equality is still possible after all such reductions, every nonempty residual graph has minimum degree at least four.

# 2. General necessary conditions for equality

## 2.1 Components and divisibility

Since both order and independence number are additive over components,
\[
\sigma(G)=\sum_{C\in\mathcal C(G)}\sigma(C).
\]
Each summand is nonnegative by the Four Colour Theorem. Therefore:

**Lemma 2.** If \(\sigma(G)=0\), then every component \(C\) of \(G\) satisfies
\[
\alpha(C)=|V(C)|/4.
\]
In particular, every component has order divisible by four.

Thus instances whose order is not divisible by four are automatically YES-instances.

## 2.2 An exact expansion characterization

For \(S\subseteq V(G)\), let \(N(S)\) denote its open neighborhood.

**Proposition 3.** A planar graph \(G\) satisfies \(\alpha(G)=|V(G)|/4\) if and only if
\[
|N(S)|\ge 3|S|                                      \tag{1}
\]
for every independent set \(S\subseteq V(G)\).

**Proof.**

Suppose \(n=4k\) and \(\alpha(G)=k\). For an independent set \(S\), put
\[
R=G-N[S].
\]
The union of \(S\) with an independent set of \(R\) is independent in \(G\), and hence
\[
k\ge |S|+\alpha(R)\ge |S|+\frac{|V(R)|}{4}.
\]
Since
\[
n=|S|+|N(S)|+|V(R)|,
\]
multiplication by four and rearrangement give \(|N(S)|\ge 3|S|\).

Conversely, let \(I\) be a maximum independent set. It is maximal, so
\[
N(I)=V(G)\setminus I.
\]
Applying (1) to \(I\) gives
\[
n-\alpha(G)\ge 3\alpha(G),
\]
and hence \(\alpha(G)\le n/4\). The reverse inequality follows from the Four Colour Theorem. ∎

This characterization is structurally useful but is not an algorithmic solution: if \(\alpha(G)>n/4\), then a maximum independent set itself violates (1).

Taking \(|S|=1\) gives an immediate consequence.

**Corollary 4.** Every planar graph satisfying \(\alpha(G)=|V(G)|/4\) has minimum degree at least three.

There is also a Hall-type consequence. If \(I\) is a maximum independent set in an equality graph, then every \(S\subseteq I\) satisfies \(|N(S)|\ge3|S|\). Replacing every vertex of \(I\) by three clones and applying Hall's theorem shows:

**Corollary 5.** For every maximum independent set \(I\) of an equality graph, the bipartite graph between \(I\) and \(V(G)\setminus I\) contains a spanning collection of \(3\)-stars centered at the vertices of \(I\).

# 3. Four-colouring constraints

Suppose \(G\) has \(n=4k\) vertices and \(\alpha(G)=k\).

Every proper four-colouring of \(G\) has four colour classes of size exactly \(k\): each colour class has size at most \(k\), and their sizes sum to \(4k\).

Moreover, if \(C_i,C_j\) are two colour classes, then
\[
B=G[C_i\cup C_j]
\]
is bipartite on \(2k\) vertices and satisfies \(\alpha(B)\le k\). Since \(C_i\) itself is an independent set of size \(k\), \(\alpha(B)=k\). By König's theorem, \(B\) has a matching of size \(k\), hence a perfect matching.

Thus:

**Proposition 6.** In every proper four-colouring of an equality graph:

1. all four colour classes have equal size;
2. every bichromatic induced subgraph has a perfect matching;
3. every vertex has a neighbor in each of the other three colour classes.

These conditions for one particular colouring are not sufficient. The cube has a balanced colouring into its four antipodal pairs, and every pair of colour classes induces a perfect matching, but its independence number is \(4>8/4\).

Equality also implies substantial deletion robustness.

**Proposition 7.** If \(G\) has \(4k\) vertices and \(\alpha(G)=k\), then:

1. \(\alpha(G-X)=k\) for every \(X\subseteq V(G)\) with \(|X|\le3\);
2. for every vertex \(v\),
   \[
   \alpha(G-N[v])=k-1.
   \]

**Proof.**

For the first assertion,
\[
k\ge \alpha(G-X)\ge
\left\lceil\frac{4k-|X|}{4}\right\rceil=k.
\]

For the second, any independent set in \(G-N[v]\), together with \(v\), is independent in \(G\), giving the upper bound \(k-1\). Conversely, in any four-colouring the colour class containing \(v\) has size \(k\), and its other \(k-1\) vertices lie in \(G-N[v]\). ∎

# 4. The degree-three lemma

The key local fact is stronger than the minimum-degree conclusion.

**Lemma 8.** Let \(G\) be planar with \(\alpha(G)=|V(G)|/4\). If \(v\) has degree three, then its three neighbors are pairwise adjacent. Thus \(G[N[v]]\cong K_4\).

**Proof.**

Write \(n=4k\), and let \(N(v)=\{a,b,c\}\). Suppose, for example, that \(a\) and \(b\) are nonadjacent.

Fix a plane embedding. After deleting \(v\), the vertices \(a\) and \(b\) can be identified while preserving planarity: draw an auxiliary edge from \(a\) to \(b\) close to the former two-edge path \(a v b\), through the angular sector at \(v\) not containing the third incident edge, and then contract this auxiliary edge. Let \(H\) be the resulting planar graph, with parallel edges suppressed.

Four-colour \(H\). Pulling the colouring back to \(G-v\) gives a proper colouring in which \(a\) and \(b\) receive the same colour. Consequently, at most two colours occur on \(N(v)\). Let \(p\) and \(q\) be two colours absent from \(N(v)\).

Assigning either \(p\) or \(q\) to \(v\) gives a proper four-colouring of \(G\). Both colourings must have all four colour classes of size \(k\). If the \(p\)- and \(q\)-classes in \(G-v\) have sizes \(s_p,s_q\), the first extension requires
\[
s_p+1=k,\qquad s_q=k,
\]
whereas the second requires
\[
s_p=k,\qquad s_q+1=k,
\]
a contradiction. Hence \(ab\in E(G)\). Applying the same argument to each pair of neighbors proves that \(N(v)\) is a triangle. ∎

## 4.1 The exact reduction rule

Call \(N[v]\) a pendant tetrahedron if \(d(v)=3\) and \(N(v)\) is a triangle.

**Lemma 9.** If \(Q=N[v]\) is a pendant tetrahedron and \(R=G-Q\), then
\[
\alpha(G)=1+\alpha(R)
\quad\text{and}\quad
\sigma(G)=\sigma(R).
\]

**Proof.**

Since \(Q\cong K_4\), every independent set meets \(Q\) in at most one vertex. Thus
\[
\alpha(G)\le1+\alpha(R).
\]
The vertex \(v\) has no neighbors outside \(Q\), so \(v\) together with a maximum independent set of \(R\) gives the reverse inequality. Since \(|Q|=4\), the identity for \(\sigma\) follows. ∎

This rule does not assume that \(G\) is an equality graph.

# 5. Proof of Theorem 1

Suppose first that \(G\) has a \(K_4\)-factor consisting of \(t\) copies. Every independent set contains at most one vertex from each copy, so
\[
\alpha(G)\le t=\frac{|V(G)|}{4}.
\]
The Four Colour Theorem gives the reverse inequality. Hence equality holds.

Conversely, suppose that \(G\) is 3-degenerate and satisfies equality. If \(G\) is nonempty, it has a vertex \(v\) of degree at most three. Corollary 4 gives \(d(v)\ge3\), so \(d(v)=3\). By Lemma 8, \(N[v]\cong K_4\). Lemma 9 shows that
\[
G-N[v]
\]
is again an equality graph. It remains planar and 3-degenerate. Induction on \(|V(G)|\) gives a \(K_4\)-factor of the remainder, and adjoining \(N[v]\) gives a \(K_4\)-factor of \(G\).

The same induction shows that the tetrahedra can be deleted successively until the graph is empty. This proves all three equivalences. ∎

## 5.1 The promised polynomial-time algorithm

For a 3-degenerate planar input \(G\), run:

1. If the current graph is empty, return **NO**: \(\alpha(G)\) is not larger than \(n/4\).
2. Choose a vertex \(v\) of degree at most three.
3. If \(d(v)\le2\), return **YES**.
4. If \(d(v)=3\) but its neighbors do not form a triangle, return **YES**.
5. Otherwise delete \(N[v]\) and repeat.

A suitable vertex always exists because 3-degeneracy is hereditary. Lemmas 8 and 9 prove correctness. The procedure is plainly polynomial; standard degree-bucket data structures make all vertex deletions linear apart from adjacency queries.

Some immediate corollaries are:

- If \(\Delta(G)\le3\), equality holds exactly when every component is \(K_4\).
- If \(G\) is nonempty, planar, 3-degenerate, and \(K_4\)-free, then \(\alpha(G)>|V(G)|/4\).
- The theorem applies in particular to planar graphs of treewidth at most three.
- Since planar chordal graphs are 3-degenerate, a planar chordal graph is an equality graph exactly when it has a \(K_4\)-factor.

There is also a different exact special case.

**Proposition 10.** If \(G\) is a perfect planar graph, then
\[
\alpha(G)=|V(G)|/4
\]
if and only if \(G\) has a \(K_4\)-factor.

**Proof.**

Only necessity needs proof. Let \(n=4k\) and \(\alpha(G)=k\). The complement of a perfect graph is perfect, so
\[
\chi(\overline G)=\omega(\overline G)=\alpha(G)=k.
\]
A \(k\)-colouring of \(\overline G\) partitions \(V(G)\) into \(k\) cliques of \(G\). Every planar clique has at most four vertices. Since these \(k\) cliques cover \(4k\) vertices, they are all copies of \(K_4\). ∎

# 6. Sharpness: a degree-four equality core

Let \(A_4\) be the square antiprism. Its vertices are
\[
u_0,u_1,u_2,u_3,w_0,w_1,w_2,w_3,
\]
with indices modulo four, and its edges are
\[
u_i u_{i+1},\qquad w_iw_{i+1},\qquad
u_iw_i,\qquad u_iw_{i-1}.
\]
It is planar: the two four-cycles are the square faces, and the intervening annulus consists of eight triangular faces.

Every vertex has degree four, so \(A_4\) has degeneracy four. Its independence number is two:

- at most two \(u_i\)'s can be selected;
- if two are selected, they must be opposite, and their neighbors cover all four \(w_j\)'s;
- if exactly one \(u_i\) is selected, the two \(w_j\)'s not adjacent to it are adjacent to each other;
- with no \(u_i\), at most two vertices can be selected from the \(w\)-cycle.

Thus
\[
\alpha(A_4)=2=\frac{|V(A_4)|}{4}.
\]
On the other hand, the neighborhood of every vertex induces a four-vertex path, so \(A_4\) contains no \(K_4\). Therefore Theorem 1 cannot be extended from degeneracy three to degeneracy four with the same conclusion.

## 6.1 The residual cores are unbounded

The reduction to minimum degree at least four does not yield a bounded-size or bounded-treewidth kernel.

Let \(F\) be any plane graph of maximum degree at most four. Replace every vertex of \(F\) by a copy of \(A_4\), embedded with one square face as the outer face. Attach the incident edges of \(F\) to distinct vertices of that square in the prescribed cyclic order.

The resulting graph \(G_F\) is planar and has minimum degree at least four. If \(r=|V(F)|\), then
\[
|V(G_F)|=8r.
\]
Every independent set meets each antiprism block in at most two vertices, so
\[
\alpha(G_F)\le2r=\frac{|V(G_F)|}{4}.
\]
The Four Colour Theorem gives equality.

Moreover, contracting every antiprism block recovers \(F\) as a minor. Taking \(F\) from a family of planar grids shows that equality graphs of minimum degree at least four can have unbounded treewidth.

# 7. What remains open

For an arbitrary planar graph, repeatedly applying Lemma 9 gives the following rigorous reduction:

- if at any stage there is a vertex of degree at most two, equality is impossible;
- if there is a degree-three vertex whose neighborhood is not a triangle, equality is impossible;
- a degree-three vertex with triangular neighborhood can be removed without changing \(\sigma\);
- if the process does not decide the instance, it leaves a planar graph of minimum degree at least four with the same value of \(\sigma\).

Planarity then guarantees the presence of degree-four or degree-five vertices, but the square antiprism and the block-substitution construction show that such residual graphs can genuinely satisfy equality and can be arbitrarily complicated.

I do not have:

1. a reduction rule covering all degree-four or degree-five configurations;
2. a structural characterization of the resulting cores;
3. a polynomial-time algorithm for unrestricted planar graphs;
4. an NP-hardness proof for the unrestricted threshold problem.

Thus the catalogued problem is not resolved. The proved part is an exact characterization and polynomial algorithm for the substantial special class of 3-degenerate planar graphs, together with a sharp local reduction isolating the unresolved minimum-degree-four case.