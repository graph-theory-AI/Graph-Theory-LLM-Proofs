```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The general problem remains open, but MWIS is fixed-parameter tractable in the minimum transversal of an explicitly enumerable family containing every pyramid base, and is polynomial when this parameter is O(log n).",
  "would_publish": false,
  "caveats": "The parameter can be linear on connected even-hole-free graphs, so this gives neither a general polynomial algorithm nor an NP-hardness proof."
}
```

# 1. Problem and outcome

A hole is an induced cycle of length at least four. The problem is to determine the complexity of maximum independent set, or more generally maximum weighted independent set (MWIS), on even-hole-free graphs.

I do not resolve the polynomial-time versus NP-hard question. I prove a parameterized reduction to the polynomial-time algorithm from the source paper for \((\)even-hole, pyramid\()\)-free graphs. The parameter is obtained from a polynomially enumerable family of triangles that necessarily contains the base triangle of every induced pyramid.

Throughout, let \(T_{\mathrm{PF}}(n)=n^{O(1)}\) denote the running time of the source-paper MWIS algorithm on even-hole-free, pyramid-free graphs.

# 2. Triangles which can support pyramid arms

Let \(G\) be a graph and let
\[
B=\{b_1,b_2,b_3\}
\]
be a triangle. Define
\[
A_B=\{v\in V(G)\setminus B: |N_G(v)\cap B|\leq 1\},
\]
and, for \(i\in\{1,2,3\}\),
\[
P_i(B)=\{v\in A_B:N_G(v)\cap B=\{b_i\}\}.
\]

Call \(B\) an **arm-candidate triangle** if some connected component \(C\) of \(G[A_B]\) satisfies:

1. \(C\cap P_i(B)\neq\varnothing\) for all \(i=1,2,3\); and
2. for some distinct \(i,j\), there are nonadjacent vertices
   \[
   x_i\in C\cap P_i(B),\qquad x_j\in C\cap P_j(B).
   \]

Write \(\mathcal A(G)\) for the family of all arm-candidate triangles of \(G\).

## Lemma 2.1

The base triangle of every induced pyramid in \(G\) belongs to \(\mathcal A(G)\).

### Proof

Let the pyramid consist of chordless paths
\[
Q_i=a\cdots b_i,\qquad i=1,2,3,
\]
with common apex \(a\), base triangle \(B=\{b_1,b_2,b_3\}\), and at least two of the paths having length at least two.

For each \(i\), let \(y_i\) be the neighbor of \(b_i\) on \(Q_i\). If \(Q_i\) has length one, then \(y_i=a\).

The induced-pyramid conditions imply
\[
N_G(y_i)\cap B=\{b_i\}.
\]
Moreover, every vertex of
\[
\left(\bigcup_{i=1}^{3}V(Q_i)\right)\setminus B
\]
has at most one neighbor in \(B\). These vertices induce a connected subgraph contained in \(G[A_B]\), since the three arms meet at \(a\). Consequently, \(y_1,y_2,y_3\) belong to one component of \(G[A_B]\), with \(y_i\in P_i(B)\).

Choose two arms \(Q_i,Q_j\) of length at least two. Then \(y_i\) and \(y_j\) are distinct internal-arm vertices, and there is no edge \(y_iy_j\), since the pyramid has no edges between distinct arms other than the base-triangle edges. Thus \(B\in\mathcal A(G)\). ∎

## Corollary 2.2

If \(X\subseteq V(G)\) meets every triangle in \(\mathcal A(G)\), then \(G-X\) is pyramid-free.

### Proof

Suppose \(G-X\) contains an induced pyramid with base triangle \(B\). Because \(G-X\) is an induced subgraph of \(G\), this is also an induced pyramid in \(G\). Lemma 2.1 gives \(B\in\mathcal A(G)\). But \(B\subseteq V(G)\setminus X\), contradicting that \(X\) meets every member of \(\mathcal A(G)\). ∎

Notice that no even-hole-free hypothesis was needed for Lemma 2.1 or Corollary 2.2.

# 3. Computing the candidate family

The family \(\mathcal A(G)\) is polynomially enumerable.

For each of the at most \(\binom n3\) triangles \(B\):

1. compute \(A_B\);
2. compute the components of \(G[A_B]\);
3. in each component, record its intersections with \(P_1(B),P_2(B),P_3(B)\);
4. if all three intersections are nonempty, test whether some two corresponding sets contain a nonadjacent pair.

With an adjacency matrix, each triangle can be processed in \(O(n^2)\) time. Thus a direct implementation lists \(\mathcal A(G)\) in \(O(n^5)\) time. No recognition algorithm for pyramids is required.

# 4. A transversal-parameter algorithm

Define
\[
\tau_{\mathrm{ac}}(G)=
\min\bigl\{|X|:X\cap B\neq\varnothing\text{ for every }B\in\mathcal A(G)\bigr\}.
\]

## Theorem 4.1

On a promised even-hole-free graph \(G\), MWIS can be solved in time
\[
O\!\left(
n^5+3^{\tau_{\mathrm{ac}}(G)}n^{O(1)}
+2^{\tau_{\mathrm{ac}}(G)}T_{\mathrm{PF}}(n)
\right).
\]
In particular, MWIS is fixed-parameter tractable parameterized by \(\tau_{\mathrm{ac}}(G)\), and polynomial-time solvable whenever
\[
\tau_{\mathrm{ac}}(G)=O(\log n).
\]

### Proof

First list \(\mathcal A(G)\). It is a 3-uniform hypergraph on \(V(G)\). A minimum transversal can be found by the standard bounded-search-tree algorithm.

Given a budget \(k\), if an unhit triangle \(B=\{b_1,b_2,b_3\}\) remains, every transversal contains at least one of its three vertices. Branch on adding \(b_1,b_2\), or \(b_3\) to the transversal. The search tree has at most \(3^k\) leaves. Trying successive budgets \(k=0,1,\ldots,\tau_{\mathrm{ac}}(G)\) costs \(3^{\tau_{\mathrm{ac}}(G)}n^{O(1)}\).

Let \(X\) be the resulting minimum transversal. By Corollary 2.2, \(G-X\) is pyramid-free. It is also even-hole-free, since this property is hereditary.

For each independent set \(S\subseteq X\), define
\[
H_S=G-\bigl(X\cup N_G(S)\bigr).
\]
Then \(H_S\) is an induced subgraph of \(G-X\), and hence is both even-hole-free and pyramid-free. Apply the source-paper MWIS algorithm to \(H_S\).

The exact lifting identity is
\[
\alpha_w(G)=
\max_{\substack{S\subseteq X\\ S\text{ independent}}}
\left(
w(S)+\alpha_w(H_S)
\right).
\tag{1}
\]

Indeed, every independent set \(I\) of \(G\) has \(S=I\cap X\), and \(I\setminus X\) is an independent set of \(H_S\). Conversely, the union of \(S\) with any independent set of \(H_S\) is independent in \(G\). Thus (1) covers every possible optimum and introduces no approximation.

There are at most \(2^{|X|}=2^{\tau_{\mathrm{ac}}(G)}\) choices for \(S\). This proves the stated running time. ∎

# 5. A packing version with a \(4^m\) bound

A transversal need not be computed optimally. Greedily construct a maximal family
\[
B_1,\ldots,B_m\in\mathcal A(G)
\]
of pairwise vertex-disjoint arm-candidate triangles, and put
\[
X=\bigcup_{r=1}^{m}B_r.
\]

Maximality implies that \(X\) meets every member of \(\mathcal A(G)\), so \(G-X\) is pyramid-free.

Since each \(B_r\) is a clique, an independent subset of \(X\) contains at most one vertex from each \(B_r\). Thus all independent subsets of \(X\) can be generated by giving four choices for each \(B_r\): choose none of its vertices, or choose one of its three vertices. Choices containing cross-edges between distinct packed triangles are discarded.

Therefore:

## Theorem 5.1

Given a maximal pairwise vertex-disjoint family of \(m\) arm-candidate triangles, MWIS on a promised even-hole-free graph can be solved in time
\[
O\!\left(n^5+4^mT_{\mathrm{PF}}(n)\right).
\]

If \(\nu_{\mathrm{ac}}(G)\) denotes the maximum number of pairwise vertex-disjoint arm-candidate triangles, the greedy value satisfies \(m\leq\nu_{\mathrm{ac}}(G)\). Hence this is also an
\[
O\!\left(4^{\nu_{\mathrm{ac}}(G)}n^{O(1)}\right)
\]
fixed-parameter bound. In particular, the algorithm is polynomial on every class satisfying
\[
\nu_{\mathrm{ac}}(G)=O(\log n).
\]

No maximum packing needs to be computed.

# 6. A simpler natural corollary

One may avoid the arm-candidate definition entirely by packing arbitrary triangles.

Let \(B_1,\ldots,B_m\) be a maximal family of pairwise vertex-disjoint triangles and set \(X=\bigcup B_i\). Every triangle of \(G\) intersects \(X\), so \(G-X\) is triangle-free. A pyramid contains a base triangle, and therefore \(G-X\) is pyramid-free.

The same four-choice enumeration gives:

## Corollary 6.1

Let \(\nu_\triangle(G)\) be the maximum number of pairwise vertex-disjoint triangles in an even-hole-free graph \(G\). Then MWIS can be solved in time
\[
O\!\left(4^{\nu_\triangle(G)}T_{\mathrm{PF}}(n)+n^{O(1)}\right).
\]
Consequently, MWIS is polynomial-time solvable on even-hole-free graphs satisfying
\[
\nu_\triangle(G)=O(\log n).
\]

This applies to weighted independent set, not only the unweighted problem.

# 7. Why this does not extend immediately to all even-hole-free graphs

The parameters above are not bounded by \(O(\log n)\) on the full class.

For \(t\geq1\), construct \(G_t\) as follows. Take one vertex \(a\). For every \(r\in\{1,\ldots,t\}\), add vertices
\[
x_{r1},x_{r2},x_{r3},b_{r1},b_{r2},b_{r3},
\]
edges
\[
a x_{ri},\quad x_{ri}b_{ri}\qquad(i=1,2,3),
\]
and make \(\{b_{r1},b_{r2},b_{r3}\}\) a triangle. There are no further edges.

Each group indexed by \(r\), together with \(a\), is a pyramid whose three arms have length two. The base triangles are pairwise vertex-disjoint.

The graph is even-hole-free. Since \(a\) is a cut vertex separating the groups, every cycle is contained in one group. In one group, a cycle through \(a\) and two arms using a direct base edge has length five. A cycle using two base edges has the third base edge as a chord. Thus all holes have length five.

Every base triangle is an arm-candidate triangle, so
\[
\nu_{\mathrm{ac}}(G_t)\geq t,\qquad
\tau_{\mathrm{ac}}(G_t)\geq t,
\]
while
\[
|V(G_t)|=6t+1.
\]
Thus these parameters can be linear even for connected even-hole-free graphs.

The central unresolved difficulty remains the case of many interacting pyramids or pyramid-capable triangles. The argument above handles them only by explicitly guessing the optimum independent set’s intersection with a transversal.

# 8. Complexity-theoretic constraint on an NP-hardness proof

Accepting the catalog’s stated quasi-polynomial algorithm for the full class, the decision version belongs to
\[
n^{\log^{O(1)}n}.
\]

Therefore, an ordinary polynomial-time many-one NP-hardness reduction to promised even-hole-free instances would imply
\[
\mathrm{NP}\subseteq\mathrm{QP}.
\]
More concretely, a polynomial-size reduction from sparse \(N\)-variable 3-SAT followed by the quasi-polynomial algorithm would run in
\[
2^{(\log N)^{O(1)}}=2^{o(N)},
\]
contradicting the Exponential Time Hypothesis.

This is only a conditional obstruction: neither ETH nor \(\mathrm{NP}\nsubseteq\mathrm{QP}\) is proved. It does, however, mean that a conventional NP-hardness proof would have unexpectedly strong complexity consequences.

# 9. Remaining gaps

1. No bound on \(\tau_{\mathrm{ac}}(G)\) or \(\nu_{\mathrm{ac}}(G)\) is proved for general even-hole-free graphs; the example above rules out such a bound depending only logarithmically on \(n\).
2. Arm-candidate triangles form only a polynomially testable necessary superset of pyramid bases; no sufficiency claim is made.
3. The argument relies on the established polynomial MWIS algorithm for even-hole-free, pyramid-free graphs.
4. No general polynomial-time algorithm and no unconditional hardness result is obtained.
5. I have not checked whether this elementary parameterized consequence has already appeared in the literature, and it is not substantial enough by itself for a standalone submission.