```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The full characterization is not obtained, but stars and all trees with at most three leaves are proved positive, together with a sharp characterization of when expansions contain bounded-size cores.",
  "would_publish": false,
  "caveats": "Assumes finite simple host graphs and the standard minor-model definition of expansion; no unresolved ladder case or full characterization is settled."
}
```

# Partial results on edge-Erdős–Pósa for expansions

## 1. Definitions and statement of the partial results

Throughout, graphs are finite and simple. A \(J\)-expansion is the union of a minor model of \(J\); equivalently, it is a subgraph containing \(J\) as a minor, trimmed to the chosen model. Two expansions are edge-disjoint when their edge sets are disjoint, although they may share vertices.

For a fixed connected graph \(J\) with at least one edge, write

\[
\nu_J^e(G)
\]

for the maximum number of pairwise edge-disjoint \(J\)-expansions in \(G\), and

\[
\tau_J^e(G)
\]

for the minimum number of edges meeting every \(J\)-expansion.

Let \(p_J(k)\) be a vertex-Erdős–Pósa bound for \(J\)-expansions: if \(G\) has no \(k\) vertex-disjoint \(J\)-expansions, then some set of at most \(p_J(k)\) vertices meets every \(J\)-expansion. The Robertson–Seymour result quoted in the problem guarantees such a function whenever \(J\) is planar.

I prove the following.

### Theorem A: bounded-degree hosts

For every connected planar \(J\) with \(E(J)\neq\varnothing\), if \(\Delta(G)\le D\) and \(\nu_J^e(G)<k\), then

\[
\tau_J^e(G)\le D\,p_J(k).
\]

Thus any family witnessing failure of the edge-EP property for a planar \(J\) must have unbounded maximum degree.

### Theorem B: all stars are positive

For every \(r\ge 2\), the \(K_{1,r}\)-expansions have the edge-EP property. More precisely, if \(G\) has no \(k\) edge-disjoint \(K_{1,r}\)-expansions, then there is an edge transversal of size at most

\[
r(k-1)+(r-1)p_{K_{1,r}}(k).
\]

### Theorem C: trees with at most three leaves

Let \(T\) be a tree with at least one edge and at most three leaves. Then

\[
\tau_T^e(G)\le |E(T)|\,\nu_T^e(G)
\]

for every graph \(G\). In particular, if \(\nu_T^e(G)<k\), then

\[
\tau_T^e(G)\le |E(T)|(k-1).
\]

This includes every path and every subdivision of \(K_{1,3}\).

The same argument applies to a forest \(J\) with at least one edge provided every nontrivial component has at most three leaves.

### Theorem D: exact boundary of the bounded-core argument

Call a connected graph \(J\) bounded-core if there is a constant \(b_J\) such that every \(J\)-expansion contains a \(J\)-expansion with at most \(b_J\) edges.

Then a connected graph \(J\) with at least one edge is bounded-core if and only if \(J\) is a path or a subdivision of \(K_{1,3}\), equivalently, if and only if \(J\) is a tree with at most three leaves.

This is not a characterization of the edge-EP property: cycles have the edge-EP property by the theorem in the source paper but are not bounded-core, and Theorem B shows that \(K_{1,r}\) is another example for every \(r\ge4\).

---

## 2. Bounded-degree hosts

Suppose \(\Delta(G)\le D\) and \(G\) has no \(k\) edge-disjoint \(J\)-expansions. Then it certainly has no \(k\) vertex-disjoint \(J\)-expansions. Since \(J\) is planar, there is a set

\[
X\subseteq V(G),\qquad |X|\le p_J(k),
\]

meeting every \(J\)-expansion.

Let \(F\) be the set of all edges incident with \(X\). Then

\[
|F|\le \sum_{x\in X}d_G(x)\le D|X|\le Dp_J(k).
\]

Deleting \(F\) isolates every vertex in \(X\). Since \(J\) is connected and has an edge, a surviving \(J\)-expansion cannot use an isolated vertex. Hence any \(J\)-expansion in \(G-F\) would avoid \(X\), contradicting the choice of \(X\). This proves Theorem A.

---

## 3. Stars

Let \(S_r=K_{1,r}\), where \(r\ge2\), and suppose that \(G\) contains no \(k\) edge-disjoint \(S_r\)-expansions.

Choose a maximal family

\[
Q_1,\ldots,Q_s
\]

of edge-disjoint literal copies of \(S_r\). Every such copy is an \(S_r\)-expansion, so \(s\le k-1\). Put

\[
F_0=\bigcup_{i=1}^s E(Q_i).
\]

Then

\[
|F_0|=rs\le r(k-1).
\]

Let \(G_0=G-F_0\). By maximality, \(G_0\) has no literal copy of \(S_r\). Because the host graph is simple, this implies

\[
\Delta(G_0)\le r-1:
\]

a vertex of degree at least \(r\) together with \(r\) of its incident edges would give another literal \(S_r\), edge-disjoint from all the \(Q_i\).

The graph \(G_0\) still has no \(k\) edge-disjoint \(S_r\)-expansions. Applying Theorem A with \(D=r-1\), there is a set \(F_1\subseteq E(G_0)\) such that

\[
|F_1|\le (r-1)p_{S_r}(k)
\]

and \(G_0-F_1\) has no \(S_r\)-expansion.

Consequently \(F_0\cup F_1\) meets every \(S_r\)-expansion of \(G\), and

\[
|F_0\cup F_1|
 \le r(k-1)+(r-1)p_{S_r}(k).
\]

This proves Theorem B. The argument only uses the established vertex-EP theorem for the planar graph \(K_{1,r}\).

---

## 4. Subcubic minor models

The following standard elementary fact is useful.

### Lemma 4.1

If \(H\) has maximum degree at most \(3\) and \(H\) is a minor of \(G\), then \(G\) contains a subdivision of \(H\).

#### Proof

Take a minor model with pairwise disjoint connected branch sets \(B_v\), \(v\in V(H)\), and choose one model edge for each edge of \(H\).

Inside \(B_v\), consider the endpoints of the at most three chosen model edges incident with \(v\). A minimal tree connecting these attachment vertices has a vertex \(x_v\) from which there are internally disjoint routes to all the attachments:

- for one attachment this is immediate;
- for two attachments use their connecting path;
- for three attachments use the median vertex of the minimal connecting tree.

Combining these routes with the chosen inter-branch-set edges gives internally disjoint paths corresponding to the edges of \(H\), meeting only at the vertices \(x_v\). Thus their union is a subdivision of \(H\). ∎

---

## 5. Trees with at most three leaves

Let \(T\) be a tree with \(m=|E(T)|\) and at most three leaves.

If \(T\) has at most two leaves, then \(T\) is a path. Any subdivision of \(T\) is a path of length at least \(m\), and therefore contains a literal \(m\)-edge copy of \(T\).

If \(T\) has exactly three leaves, it has exactly one vertex of degree \(3\). Thus it is a tripod with arm lengths \(a_1,a_2,a_3\), where

\[
a_1+a_2+a_3=m.
\]

By Lemma 4.1, every \(T\)-expansion contains a subdivision of \(T\). From the image of the unique degree-\(3\) vertex, each subdivided arm has length at least \(a_i\). Keeping only the first \(a_i\) edges on each arm produces a literal copy of \(T\) with exactly \(m\) edges.

We have therefore proved:

> Every \(T\)-expansion contains a literal copy of \(T\).

Now choose a maximal family \(T_1,\ldots,T_s\) of edge-disjoint literal copies of \(T\), and put

\[
F=\bigcup_{i=1}^s E(T_i).
\]

If some \(T\)-expansion avoided \(F\), it would contain a literal copy of \(T\) avoiding \(F\), contradicting maximality. Hence \(F\) is an edge transversal. Moreover,

\[
|F|=ms\le m\,\nu_T^e(G).
\]

This proves Theorem C.

For a forest whose nontrivial components each have at most three leaves, Lemma 4.1 and the same truncation can be applied componentwise, producing a literal copy of the whole forest inside each expansion. The identical maximal-packing argument then applies.

---

## 6. Characterizing the bounded-core method

Define the bounded-core property by requiring a constant \(b_J\) such that every \(J\)-expansion contains a subgraph with at most \(b_J\) edges that still contains \(J\) as a minor.

The preceding argument proves the positive direction for paths and subdivisions of \(K_{1,3}\), with

\[
b_J=|E(J)|.
\]

It remains to show that no other connected graph has this property.

### 6.1. Graphs containing a cycle

Suppose \(J\) contains a cycle. For \(N\ge1\), let \(X_N\) be obtained from \(J\) by replacing every edge by a path of length \(N\). Then \(X_N\) is a \(J\)-expansion.

Every cycle of \(X_N\) has length at least \(N\) (indeed at least \(N\) times the girth of \(J\)). If a subgraph \(Y\subseteq X_N\) contains \(J\) as a minor, then \(Y\) cannot be a forest, since every minor of a forest is a forest. Hence \(Y\) contains a cycle and therefore

\[
|E(Y)|\ge N.
\]

Thus no uniform bounded core exists for any cyclic \(J\).

### 6.2. Trees with at least four leaves

Let \(T\) be a tree with \(L\ge4\) leaves.

First construct a subcubic refinement \(S\) of \(T\): replace every vertex \(v\) of degree \(d\ge4\) by a tree of maximum degree \(3\) with \(d\) designated ports, and attach the former incident edges at the ports. Contracting each replacement tree recovers \(T\). This operation introduces no new leaves, so \(S\) also has exactly \(L\) leaves.

For a subcubic tree \(R\), the degree-sum identity gives

\[
\ell(R)=2+n_3(R),
\]

where \(\ell(R)\) is the number of leaves and \(n_3(R)\) the number of degree-\(3\) vertices. Hence \(S\) has exactly

\[
q=L-2\ge2
\]

degree-\(3\) vertices.

Let \(X_N\) be obtained by replacing every edge of \(S\) by a path of length \(N\). Then \(X_N\) is still subcubic, has the same \(L\) leaves and the same \(q\) degree-\(3\) vertices, and contains \(T\) as a minor. Distinct degree-\(3\) vertices of \(X_N\) are at distance at least \(N\).

We use the elementary fact that leaf number cannot increase when taking a minor of a tree. One way to see this is:

1. any connected subtree has no more leaves than the original tree—each new boundary leaf can be assigned to a distinct original leaf in the branch cut off there; and
2. contracting an edge of a tree does not increase its number of leaves.

Now let \(Y\subseteq X_N\) be a connected subgraph containing \(T\) as a minor. Since \(T\) has \(L\) leaves,

\[
\ell(Y)\ge L.
\]

On the other hand, \(Y\) is subcubic, and every degree-\(3\) vertex of \(Y\) must be one of the \(q\) degree-\(3\) vertices of \(X_N\). Therefore

\[
\ell(Y)=2+n_3(Y)\le 2+q=L.
\]

Equality holds throughout. In particular, \(Y\) contains all \(q\) degree-\(3\) vertices of \(X_N\). Since \(q\ge2\), it contains the unique path between two such vertices, whose length is at least \(N\). Consequently

\[
|E(Y)|\ge N.
\]

As \(N\) is arbitrary, \(T\) has no bounded core.

Combining the cyclic and tree cases proves Theorem D.

---

## 7. Consequences and remaining gap

The arguments give the following certified positive subclasses of planar targets:

- all paths;
- all subdivisions of \(K_{1,3}\);
- all stars \(K_{1,r}\), including \(r\ge4\);
- all cycles, by the long-cycle theorem stated in the supplied source.

The bounded-core theorem is a sharp description of when the simplest hypergraph argument works: if every expansion contains a bounded-size expansion, a maximal edge-disjoint family immediately yields a linear transversal. It is not a characterization of edge-EP itself. In particular:

- a long chordless cycle has no bounded cyclic subexpansion, yet cycles have edge-EP;
- for \(r\ge4\), a \(K_{1,r}\)-expansion can be a large subcubic tree with \(r\) leaves and no bounded \(K_{1,r}\)-subexpansion, yet Theorem B proves edge-EP by first reducing the host to bounded degree.

For targets such as ladders, both mechanisms fail directly. Arbitrarily large stars contain no ladder, so excluding bounded ladder models does not control maximum degree; and subdivided ladders have no bounded cores because they contain cycles. Thus the argument does not decide any of the unresolved intermediate ladder cases, nor does it prove the proposed condensed-wall characterization.

No claim of novelty is made for these elementary special cases. The full characterization remains open.