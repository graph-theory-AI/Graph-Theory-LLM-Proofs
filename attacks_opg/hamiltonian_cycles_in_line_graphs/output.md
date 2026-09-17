```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture holds when a finite simple root has at most five degree-3 vertices, and a related path-cover bound follows for arbitrary roots.",
  "would_publish": false,
  "caveats": "The full conjecture is not settled here; no novelty is claimed for these sufficient conditions."
}
```

## 1. Partial result

All graphs below are finite. The root graph \(G\) is simple; auxiliary graphs obtained by suppression may have parallel edges.

Write
\[
k_3(G)=|\{v\in V(G):d_G(v)=3\}|.
\]
For a graph \(H\), let \(\operatorname{pc}(H)\) be the minimum number of vertex-disjoint paths covering \(V(H)\), with one-vertex paths allowed.

**Theorem.** Suppose that \(L(G)\) is 4-connected.

1. If \(k_3(G)\le 5\), then \(L(G)\) is Hamiltonian.
2. More generally,
   \[
   \operatorname{pc}(L(G))
   \le
   \max\left\{1,\left\lceil\frac{k_3(G)-5}{2}\right\rceil\right\}.
   \]
   In particular, if \(k_3(G)\le 7\), then \(L(G)\) has a Hamilton path.

The proof also gives a precise partition certificate that any counterexample must possess. The main non-elementary input is the classical Nash-Williams–Tutte spanning-tree packing theorem, stated where it is used.

## 2. The appropriate root-graph formulation

Call a subgraph \(F\subseteq G\) **dominating even** if:

- \(F\) is connected;
- every vertex of \(F\) has even degree in \(F\);
- every edge of \(G\) has an endpoint in \(V(F)\).

A one-vertex subgraph is permitted.

**Lemma 1.** If \(G\) has at least three edges, then \(L(G)\) is Hamiltonian if and only if \(G\) has a dominating even subgraph.

**Proof.** Suppose first that \(F\) is a dominating even subgraph with at least one edge. Take an Euler tour of \(F\), regarded as a cyclic ordering of its edges. Assign every edge of \(G-E(F)\) to one of its endpoints in \(V(F)\).

For each \(v\in V(F)\), choose one passage of the Euler tour through \(v\), and insert all edges assigned to \(v\) between the incoming and outgoing tour edges. Consecutive edges in the resulting cyclic ordering share an endpoint. Every edge of \(G\) occurs exactly once, giving a Hamilton cycle in \(L(G)\).

If \(F\) consists of a single vertex, every edge of \(G\) is incident with that vertex, so \(L(G)\) is complete.

Conversely, let
\[
e_1,e_2,\ldots,e_m,e_1
\]
be a Hamilton cycle of \(L(G)\). Choose a common endpoint \(v_i\) of \(e_i\) and \(e_{i+1}\), with indices modulo \(m\). Whenever \(v_{i-1}\ne v_i\), traverse \(e_i\) from \(v_{i-1}\) to \(v_i\); otherwise stay at that vertex and omit \(e_i\). This produces a closed trail, possibly of length zero, with no repeated edge.

Every \(e_i\) has an endpoint among the visited vertices. Thus a nonempty resulting trail gives a dominating even subgraph. If the trail is empty, all the \(v_i\) are equal and that one vertex dominates every edge. ∎

The important distinction from 4-edge-connectivity is now visible. Four-connectivity of \(L(G)\) permits small edge cuts of \(G\) that isolate vertices but leave no edges on that side.

For \(S\subseteq V(G)\), write \(\delta_G(S)\) for the edges with exactly one endpoint in \(S\). Since \(L(G)\) is 4-connected,
\[
E(G[S])\ne\varnothing,\quad E(G[V(G)\setminus S])\ne\varnothing
\quad\Longrightarrow\quad
|\delta_G(S)|\ge4. \tag{1}
\]
Indeed, deleting the vertices of \(L(G)\) corresponding to \(\delta_G(S)\) separates the two nonempty sets of internal edges.

Conversely, when \(|E(G)|\ge5\), condition (1) implies 4-connectivity of \(L(G)\), after ignoring isolated vertices of \(G\). Any disconnection of the line graph after deleting at most three vertices would leave two edge-containing components of the root graph, contradicting (1).

Also, for every \(uv\in E(G)\),
\[
4\le d_{L(G)}(uv)=d_G(u)+d_G(v)-2,
\]
so
\[
d_G(u)+d_G(v)\ge6. \tag{2}
\]

## 3. Removing leaves and suppressing degree-two vertices

Discard isolated vertices of \(G\). Then \(G\) is connected because \(L(G)\) is connected. If \(G\) is a star, its line graph is complete and the Hamiltonicity conclusion is immediate. Assume henceforth that \(G\) is not a star.

Let
\[
B=\{v\in V(G):d_G(v)\ge3\}.
\]

**Lemma 2.** There is a connected loopless multigraph \(K\), with vertex set \(B\), having the following properties:

1. \(\delta(K)\ge3\);
2. \(k_3(K)=k_3(G)\);
3. if a nontrivial cut \(\delta_K(S)\) has size at most three, then it has size exactly three and one of its shores is a single degree-3 vertex;
4. every connected spanning even subgraph of \(K\) lifts to a dominating even subgraph of \(G\).

**Proof.**

### Deleting leaves

Let \(P\) be the set of leaves of \(G\). If \(v\) has a leaf neighbour, put
\[
A=\{v\}\cup (N_G(v)\cap P).
\]
The graph \(G[A]\) contains an edge. Since \(G\) is not a star, \(G-A\) also contains an edge: otherwise every vertex outside \(A\) could only be adjacent to \(v\), making it another leaf already included in \(A\).

Consequently, (1) gives
\[
d_G(v)-|N_G(v)\cap P|=|\delta_G(A)|\ge4. \tag{3}
\]
Thus every vertex that loses leaf neighbours retains degree at least four.

Let \(G_0=G-P\). It is connected and has minimum degree at least two. By (3), its degree-two vertices are exactly the original degree-two vertices of \(G\).

### Suppressing degree-two vertices

By (2), every degree-two vertex has two neighbours of degree at least four. In particular, degree-two vertices are pairwise nonadjacent.

Suppress each degree-two vertex \(x\), replacing its path \(u x v\) by an edge \(uv\). Because \(G\) is simple, \(u\ne v\), so no loop is created. Parallel edges may be created. Denote the resulting multigraph by \(K\).

Suppression preserves the degrees of the remaining vertices. Together with (3), this proves
\[
\delta(K)\ge3,\qquad k_3(K)=k_3(G).
\]
The vertex set is exactly \(B\). Moreover, \(B\) is a vertex cover of \(G\), by (2). Since \(G\) is not a star, \(|B|\ge2\).

### Small cuts in \(K\)

Suppose that \(|\delta_K(S)|\le3\) and that both \(S\) and its complement contain at least two vertices. Minimum degree three implies that both shores contain internal edges: an independent shore with at least two vertices would have cut size at least six.

Lift this vertex partition to \(G\). Put each leaf on the side of its neighbour, and each suppressed vertex with endpoints on the same side on that side. For a suppressed path whose endpoints lie on opposite sides, put its internal vertex on either side. Each crossing edge of \(K\) then corresponds to exactly one crossing edge of \(G\).

Both lifted shores contain edges, contradicting (1). Hence one shore of the cut in \(K\) is a single vertex. Minimum degree three shows that the cut has size three and that vertex has degree three.

### Lifting an even subgraph

Let \(F\) be connected, spanning and even in \(K\). Replace every used suppressed edge by its corresponding two-edge path in \(G\). The resulting subgraph \(\widehat F\) is connected and even: degrees at \(B\) are unchanged, and each used suppressed vertex has degree two.

Because \(F\) spans \(K\), the subgraph \(\widehat F\) contains all of \(B\). Since \(B\) is a vertex cover of \(G\), \(\widehat F\) is dominating. ∎

## 4. Five cubic vertices force two spanning trees

Here is the central counting argument.

**Lemma 3.** Let \(K\) be a connected loopless multigraph satisfying properties 1 and 3 of Lemma 2. If \(k_3(K)\le5\), then \(K\) has two edge-disjoint spanning trees.

**Proof.** The Nash-Williams–Tutte theorem says that \(K\) has two edge-disjoint spanning trees if and only if every partition \(\mathcal P\) of \(V(K)\) into \(t\) nonempty parts has at least
\[
2(t-1)
\]
edges joining distinct parts.

For \(t=2\), every cut has size at least three, so the condition holds.

Now let \(t\ge3\), and let \(s\) be the number of parts that are singleton degree-3 vertices. Every other part has cut size at least four. Indeed, a cut of size at most three must have a singleton degree-3 shore; the complement of a part contains at least two vertices and therefore cannot be that shore.

If \(x\) is the number of edges joining distinct parts, then
\[
2x=\sum_{A\in\mathcal P}|\delta_K(A)|
   \ge 3s+4(t-s)
   =4t-s.
\]
Since \(s\le5\),
\[
2x\ge4t-5.
\]
The left side is even, so \(2x\ge4t-4\), and hence
\[
x\ge2(t-1).
\]
The spanning-tree packing theorem applies. ∎

Two edge-disjoint spanning trees yield more than connectivity.

**Lemma 4.** A multigraph with two edge-disjoint spanning trees has a connected spanning even subgraph.

**Proof.** Let the trees be \(T_1,T_2\), and let \(R\) be the set of odd-degree vertices of \(T_1\). The set \(R\) has even cardinality.

There is an edge set \(J\subseteq E(T_2)\) whose odd-degree vertices are exactly \(R\). For example, pair the vertices of \(R\) arbitrarily and take the symmetric difference of the corresponding paths in \(T_2\).

Since \(T_1\) and \(T_2\) are edge-disjoint,
\[
F=T_1\cup J
\]
has even degree at every vertex. It is connected and spanning because it contains \(T_1\). ∎

### Proof of the Hamiltonicity assertion

Suppose \(k_3(G)\le5\). The star case has already been handled. Otherwise, construct \(K\) using Lemma 2.

We have \(k_3(K)\le5\), so Lemmas 3 and 4 give a connected spanning even subgraph of \(K\). Lemma 2 lifts it to a dominating even subgraph of \(G\), and Lemma 1 gives a Hamilton cycle in \(L(G)\). This proves part 1 of the theorem.

## 5. The path-cover bound

Suppose now that \(k=k_3(G)\ge6\), and put
\[
r=\left\lceil\frac{k-5}{2}\right\rceil.
\]

Repeatedly choose two nonadjacent degree-3 vertices and add an edge between them, stopping when at most five degree-3 vertices remain.

Such a pair always exists while at least six degree-3 vertices remain: those vertices cannot form a clique, since each has degree only three. Each addition raises the degrees of exactly two degree-3 vertices to four. Thus exactly \(r\) edges are added.

Let the resulting simple graph be \(G^+\). We check that \(L(G^+)\) remains 4-connected. Adding a root edge \(uv\), with \(u,v\) nonadjacent and both currently of degree three, adds one vertex to the line graph adjacent to six distinct existing vertices. Adding a vertex with at least four neighbours to a 4-connected graph preserves 4-connectivity: after deletion of at most three vertices, the old graph remains connected and any surviving new vertex still has a surviving neighbour.

Therefore \(L(G^+)\) is 4-connected, and \(k_3(G^+)\le5\). Part 1 gives a Hamilton cycle \(C\) in \(L(G^+)\).

Delete from \(C\) the \(r\) vertices corresponding to the added root edges. What remains is a collection of at most \(r\) vertex-disjoint paths covering all vertices of \(L(G)\). Hence
\[
\operatorname{pc}(L(G))\le r.
\]
Together with part 1 for \(k\le5\), this proves the asserted bound.

## 6. A necessary certificate for any counterexample

The packing argument gives a useful structural restriction beyond the numerical bound.

Suppose \(G\) were a counterexample, and form its core \(K\). Then \(K\) cannot have two edge-disjoint spanning trees, because those would produce a Hamilton cycle in \(L(G)\).

Thus there is a partition \(\mathcal P\) into \(t\ge3\) parts with at most \(2t-3\) crossing edges. Let \(s\) be the number of singleton degree-3 parts, and define
\[
q=\sum_{\substack{A\in\mathcal P\\
A\text{ is not a singleton degree-3 vertex}}}
\bigl(|\delta_K(A)|-4\bigr).
\]
Every summand is nonnegative. Double-counting crossing edges gives
\[
2x=4t-s+q.
\]
Since \(x\le2t-3\), necessarily
\[
\boxed{s-q\ge6.}
\]
In particular, any counterexample must have a partition containing at least six singleton cubic parts; larger cut sizes of the remaining parts require still more such cubic parts.

### Why this does not settle the conjecture

The threshold five is sharp **for automatically forcing two spanning trees**, not for Hamiltonicity.

For example, \(K_{3,3}\) has six degree-3 vertices and only nine edges, whereas two edge-disjoint spanning trees would require ten edges. Nevertheless, \(L(K_{3,3})\) is 4-connected and Hamiltonian.

To verify the connectivity assertion directly, let a shore contain \(a\) vertices from one bipartition class and \(b\) from the other. If both shores contain edges, then \(a,b\in\{1,2\}\), and
\[
|\delta(S)|=3(a+b)-2ab\in\{4,5\}.
\]
Thus condition (1) holds. Hamiltonicity follows because a Hamilton cycle of \(K_{3,3}\) is a dominating even subgraph.

Consequently, failure of the two-tree condition is not an obstruction to Hamiltonicity. The unfilled gap is the construction of dominating even subgraphs when these deficient partitions occur. The argument above does not handle that general case and therefore neither proves nor disproves Thomassen’s conjecture.