```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture remains open, but it is equivalent to the case of forbidden square grids and holds in polynomial time on every fixed-surface input class, with an additional lifting rule for isolated components.",
  "would_publish": false,
  "caveats": "The argument gives no quasipolynomial algorithm for unrestricted graphs of unbounded minor edge-excess, including the general grid-forbidden case."
}
```

## 1. Statement and notation

All graphs are finite and simple. Write \(A\preceq_{\mathrm{im}}B\) when \(A\) is an induced minor of \(B\).

An induced-minor model of \(A\) in \(B\) consists of pairwise disjoint connected branch sets
\[
(B_v:v\in V(A))
\]
such that there is an edge between \(B_u\) and \(B_v\) in \(B\) if and only if \(uv\in E(A)\).

Two elementary facts will be used repeatedly:

1. Induced-minor containment is transitive.
2. If \(A\preceq_{\mathrm{im}}B\), then every \(A\)-induced-minor-free graph is also \(B\)-induced-minor-free. Thus an algorithm for the \(B\)-free class also applies to the \(A\)-free class.

The full conjecture is not proved below. I establish:

- a reduction showing that it suffices to consider square grids as forbidden induced minors;
- a polynomial-time algorithm on every fixed-surface input class, and a quasipolynomial algorithm when the Euler genus is polylogarithmic;
- a generic lifting lemma for adding isolated components to the forbidden graph.

---

## 2. Every planar graph is an induced minor of a square grid

### Lemma 2.1: Induced completion to a triangulation

Every planar graph \(H\) is an induced subgraph of a finite simple plane triangulation \(T\). Moreover, \(T\) can be chosen with \(O(|V(H)|+1)\) vertices.

#### Proof

Start with a plane embedding of \(H\). Using auxiliary vertices and edges, augment it to a simple plane triangulation \(R\) containing \(H\) as a subgraph. One elementary construction is:

- join the components through the outer face;
- around each cutvertex, join consecutive blocks within the intervening face until the graph is 2-connected;
- put a new vertex into each remaining face and join it to every vertex on that facial boundary.

These operations require only linearly many auxiliary vertices and edges.

Some edges of \(R\) may join two vertices of \(H\) that are nonadjacent in \(H\). Subdivide every such edge once, and call the resulting graph \(R'\). Subdivision preserves 2-connectivity, and now
\[
R'[V(H)]=H.
\]

Every facial boundary of \(R'\) is a cycle. For every face \(f\), put a new vertex \(z_f\) in \(f\) and join \(z_f\) to every vertex on its boundary. The resulting graph \(T\) is a plane triangulation. No new edge with both endpoints in \(V(R')\) was added, so
\[
T[V(H)]=H.
\]
The number of added vertices remains linear. ∎

### Lemma 2.2: Triangulation models in planar graphs are automatically induced

Let \(T\) be a plane triangulation. If a planar graph \(G\) contains \(T\) as an ordinary minor, then it contains \(T\) as an induced minor.

#### Proof

Take an ordinary minor model \((B_v:v\in V(T))\). Form a simple graph \(Q\) on \(V(T)\) by putting \(uv\in E(Q)\) precisely when some edge of \(G\) joins \(B_u\) to \(B_v\).

The graph \(Q\) is a minor of \(G\), hence planar. It contains \(T\) as a spanning subgraph. If \(t=|V(T)|\), then
\[
|E(T)|=3t-6.
\]
A simple planar graph on \(t\) vertices has at most \(3t-6\) edges. Consequently \(Q=T\), so there is no adjacency between branch sets corresponding to a nonedge of \(T\). The model is therefore induced. ∎

### Theorem 2.3: Square grids are induced-minor cofinal among planar graphs

For every planar graph \(H\), there is an integer \(r\) such that
\[
H\preceq_{\mathrm{im}} \Gamma_r,
\]
where \(\Gamma_r=P_r\square P_r\) is the \(r\times r\) square grid.

#### Proof

By Lemma 2.1, choose a plane triangulation \(T\) containing \(H\) as an induced subgraph. Every fixed planar graph is an ordinary minor of a sufficiently large square grid, so choose \(r\) with
\[
T\preceq_{\mathrm m}\Gamma_r.
\]
Since \(\Gamma_r\) is planar, Lemma 2.2 upgrades this to
\[
T\preceq_{\mathrm{im}}\Gamma_r.
\]
As \(H\preceq_{\mathrm{im}}T\), transitivity gives \(H\preceq_{\mathrm{im}}\Gamma_r\). ∎

### Consequence

The original question is equivalent to its restriction to square grids:

> MIS is quasipolynomial-time solvable for every planar-\(H\)-induced-minor-free class if and only if it is quasipolynomial-time solvable for every \(\Gamma_r\)-induced-minor-free class.

Indeed, the forward implication is immediate. For the converse, given planar \(H\), choose \(r\) as in Theorem 2.3. An \(H\)-induced-minor-free graph is then necessarily \(\Gamma_r\)-induced-minor-free.

Thus it suffices to settle the problem for connected bipartite planar forbidden graphs of maximum degree at most four. This reduction does not itself solve the grid case.

---

## 3. A bounded-minor-excess theorem

Define the planar minor excess of \(G\) by
\[
\operatorname{pex}(G)=
\max\left(
\{0\}\cup
\left\{
|E(Q)|-3|V(Q)|+6:
Q\preceq_{\mathrm m}G,\ |V(Q)|\ge 3
\right\}
\right),
\]
where minors are simplified to simple graphs.

Thus \(\operatorname{pex}(G)\) measures how many edges a minor of \(G\) can have beyond the planar extremal bound.

### Theorem 3.1

For every fixed planar graph \(H\), there are constants \(c_H,d_H\) such that every \(H\)-induced-minor-free graph \(G\) satisfies
\[
\operatorname{tw}(G)
\le
c_H\bigl(\operatorname{pex}(G)+1\bigr)^{d_H}.
\]

#### Proof

Fix a plane triangulation \(T\) containing \(H\) as an induced subgraph, as in Lemma 2.1. Let
\[
b=\operatorname{pex}(G),\qquad k=b+1.
\]

Apply Lemma 2.1 to the disjoint union of \(k\) copies of \(T\). This gives a plane triangulation \(F_k\) containing pairwise vertex-disjoint induced copies
\[
T_1,\ldots,T_k
\]
of \(T\). The construction can be made linear in \(k\), so
\[
|V(F_k)|=O_H(k).
\]

We claim that if \(G\) contains \(F_k\) as an ordinary minor, then \(G\) contains \(H\) as an induced minor.

Take an \(F_k\)-minor model in \(G\), and let \(Q\) be its branch-set adjacency graph. Then:

- \(Q\) is a simple minor of \(G\);
- \(F_k\) is a spanning subgraph of \(Q\);
- writing \(N=|V(F_k)|\), we have \(|E(F_k)|=3N-6\).

Therefore
\[
|E(Q)\setminus E(F_k)|
=
|E(Q)|-(3N-6)
\le b.
\]

Call a copy \(T_i\) dirty if two vertices nonadjacent in \(T_i\) are adjacent in \(Q\). Since \(T_i\) is induced in \(F_k\), every such dirty adjacency belongs to \(E(Q)\setminus E(F_k)\). The copies are vertex-disjoint, so one extra edge can dirty at most one copy. As there are \(k=b+1\) copies but at most \(b\) extra edges, at least one \(T_i\) is clean.

Restricting the branch model to that clean copy gives an induced-minor model of \(T\) in \(G\), and hence one of \(H\). This proves the claim.

Consequently, if \(G\) is \(H\)-induced-minor-free, then it is \(F_k\)-minor-free. The polynomial excluded-grid theorem implies that an \(m\)-vertex planar-minor-free graph has treewidth at most \(m^{O(1)}\). Since
\[
|V(F_k)|=O_H(b+1),
\]
we obtain
\[
\operatorname{tw}(G)
\le c_H(b+1)^{d_H}.
\]
∎

For fixed \(b\), the bounded-treewidth conclusion only needs the qualitative grid-minor theorem. Polynomial dependence on \(b\) uses the established polynomial excluded-grid bound.

---

## 4. Bounded-genus consequences

Let \(\gamma(G)\) denote the Euler genus of \(G\). Every simple graph \(Q\) of Euler genus at most \(\gamma\) satisfies
\[
|E(Q)|\le 3|V(Q)|-6+3\gamma
\]
when \(|V(Q)|\ge3\). Euler genus is minor-monotone, so
\[
\operatorname{pex}(G)\le 3\gamma(G).
\]

Combining this with Theorem 3.1 gives:

### Corollary 4.1

For every fixed planar \(H\), there are constants \(c_H,d_H\) such that every \(H\)-induced-minor-free graph \(G\) satisfies
\[
\operatorname{tw}(G)
\le
c_H\bigl(\gamma(G)+1\bigr)^{d_H}.
\]

In particular:

1. For every fixed surface \(\Sigma\), MIS is polynomial-time solvable on the \(\Sigma\)-embeddable graphs excluding \(H\) as an induced minor.
2. If
   \[
   \gamma(G)\le(\log n)^a
   \]
   for a fixed \(a\), then MIS is solvable in quasipolynomial time on the \(H\)-induced-minor-free graphs satisfying this genus bound.

#### Algorithmic justification

Let
\[
W=c_H(\gamma+1)^{d_H}.
\]
A standard fixed-width treewidth algorithm can find a width-\(W\) decomposition in time \(n^{O(W)}\). Maximum Independent Set is then computed by the usual dynamic program over independent subsets of each bag.

Thus the running time can be bounded by
\[
n^{(\gamma+1)^{O_H(1)}}.
\]
For fixed \(\gamma\), this is polynomial; for \(\gamma=(\log n)^{O(1)}\), it is quasipolynomial.

The argument in fact applies to Maximum Weight Independent Set as well.

For planar inputs, \(\gamma=0\), so this also proves the structural statement that, for every planar \(H\), planar \(H\)-induced-minor-free graphs have bounded treewidth.

---

## 5. Adding isolated components to the forbidden graph

The following lifting rule applies in unrestricted graphs.

### Lemma 5.1

Fix a graph \(F\) and \(s\ge1\). If MIS on \(F\)-induced-minor-free graphs is solvable in time \(T_F(n)\), then MIS on
\[
(F\uplus sK_1)\text{-induced-minor-free graphs}
\]
is solvable in time
\[
n^{s+O(1)}+n^sT_F(n).
\]

#### Proof

Let \(G\) exclude \(F\uplus sK_1\) as an induced minor. For every independent set \(S\subseteq V(G)\) of size \(s\), put
\[
A_S=V(G)\setminus N_G[S].
\]

Then \(G[A_S]\) is \(F\)-induced-minor-free. Otherwise, an induced-minor model of \(F\) in \(A_S\), together with the \(s\) singleton branch sets corresponding to \(S\), would form a model of \(F\uplus sK_1\).

If \(\alpha(G)\ge s\), then
\[
\alpha(G)
=
\max_{\substack{S\subseteq V(G)\\ |S|=s,\ S\text{ independent}}}
\left(
s+\alpha(G[A_S])
\right).
\]
Indeed, every term on the right describes an independent set in \(G\). Conversely, choose \(S\) as any \(s\)-element subset of a maximum independent set \(I\); then
\[
I\setminus S\subseteq A_S.
\]

If \(\alpha(G)<s\), it can be found by enumerating all subsets of size less than \(s\). There are at most \(n^s\) calls to the \(F\)-free algorithm. ∎

### Concrete consequences from the cases in the prompt

- Since the \(C_t\)-induced-minor-free case has a quasipolynomial algorithm, so does the
  \[
  (C_t\uplus sK_1)\text{-induced-minor-free}
  \]
  case for every fixed \(t,s\).

- Since the friendship-graph case \(K_1+tK_2\) has a polynomial algorithm, so does
  \[
  ((K_1+tK_2)\uplus sK_1)\text{-induced-minor-free},
  \]
  with an additional factor \(n^s\).

- More generally, the same conclusion applies after adding any fixed number of isolated vertices to every established positive case.

As another transfer consequence, every fixed linear forest is an induced subgraph of a sufficiently large cycle. Hence the known cycle result already gives an exact quasipolynomial algorithm for excluding any fixed linear forest as an induced minor.

---

## 6. What remains open

The square-grid reduction is only a normal form: the unrestricted \(\Gamma_r\)-induced-minor-free case remains as hard as the original question.

The bounded-excess argument works because an ordinary minor model of a large triangulation has only boundedly many unwanted branch-set adjacencies. In an unrestricted graph, the branch-set adjacency graph can contain arbitrarily many such extra edges. The pigeonhole cleaning argument then fails: one extra edge can be placed inside each of the many candidate copies.

This is not merely an artificial parameter issue. For every noncomplete planar \(H\), complete graphs are \(H\)-induced-minor-free, while their planar minor excess is quadratic and their treewidth is linear. Complete graphs themselves are easy for MIS, but the present argument gives no decomposition combining this dense easy regime with the bounded-treewidth regime.

Thus the missing step is an algorithmic treatment of high-excess minor models—presumably by exploiting clique, join, or homogeneous-set structure. No such general recursion is established here, so the original conjecture remains unresolved.