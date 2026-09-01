```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The c=2 assertion holds with ell=1 for chordal graphs, more generally for bounded-radius tree decompositions, and with ell=2 whenever S union T equals V(G).",
  "would_publish": false,
  "caveats": "Finite graphs are assumed; the unrestricted case remains open, and the literature novelty of these special cases has not been checked."
}
```

# Mathematical writeup

## 1. Statement and conventions

For paths \(P,Q\) in a finite simple graph \(G\), write
\[
d_G(P,Q)=\min\{d_G(p,q):p\in V(P),\ q\in V(Q)\}.
\]
Thus \(d_G(P,Q)\ge 2\) precisely when \(P,Q\) are vertex-disjoint and there is no edge between them. Write \(B_G(x,r)\) for the closed radius-\(r\) ball about \(x\).

The general \(c=2\) conjecture is not resolved below. I prove two uniform special cases:

1. all chordal graphs, with \(\ell=1\);
2. all instances satisfying \(S\cup T=V(G)\), with \(\ell=2\).

The first follows from a more general tree-decomposition criterion.

---

## 2. A transversal lemma for subtrees

### Lemma 2.1
Let \(\mathcal F\) be a finite family of subtrees of a tree \(R\). Then
\[
\min\{|Z|:Z\subseteq V(R),\ Z\cap F\neq\varnothing\text{ for every }F\in\mathcal F\}
=
\max\{|\mathcal A|:\mathcal A\subseteq\mathcal F
\text{ consists of pairwise disjoint subtrees}\}.
\]

### Proof
Root \(R\). For a nonempty subtree \(F\), let \(a(F)\) be its unique vertex nearest the root.

Choose \(F\in\mathcal F\) for which \(a(F)\) is as deep as possible. Put \(a(F)\) into the transversal and delete every member of \(\mathcal F\) containing \(a(F)\).

The chosen subtree \(F\) is disjoint from every undeleted subtree \(F'\). Indeed, suppose \(x\in F\cap F'\) but \(a(F)\notin F'\). Since \(x\) is below \(a(F)\), connectedness of \(F'\) implies that \(a(F')\) is a strict descendant of \(a(F)\); otherwise the \(a(F')\)-\(x\) path would contain \(a(F)\). This contradicts the maximal choice of the depth of \(a(F)\).

Iterating therefore produces simultaneously:

- a set \(Z\) meeting every member of \(\mathcal F\);
- the same number of pairwise disjoint members of \(\mathcal F\).

Conversely, any transversal needs distinct vertices for pairwise disjoint subtrees. Hence the two optima are equal. \(\square\)

---

## 3. Bounded-radius tree decompositions

Call a tree decomposition
\[
\mathcal D=(R,(B_r:r\in V(R)))
\]
a radius-\(\rho\) decomposition if, for every \(r\in V(R)\), there is a vertex \(c_r\in V(G)\) such that
\[
B_r\subseteq B_G(c_r,\rho).
\]

### Theorem 3.1
Suppose \(G\) has a radius-\(\rho\) tree decomposition. For every \(k\ge1\) and \(S,T\subseteq V(G)\), either

1. there are \(k\) \(S\)-\(T\) paths pairwise at distance at least \(2\), or
2. there is \(X\subseteq V(G)\), with \(|X|\le k-1\), such that every \(S\)-\(T\) path meets \(B_G(X,\rho)\).

In fact, the same statement holds for any finite family of connected subgraphs in place of the family of \(S\)-\(T\) paths.

### Proof
For an \(S\)-\(T\) path \(P\), define its trace in the decomposition tree by
\[
R(P)=\{r\in V(R):B_r\cap V(P)\neq\varnothing\}.
\]
This is a subtree of \(R\). Indeed, for each \(v\in V(P)\), the bags containing \(v\) induce a subtree, and the subtrees associated with consecutive vertices of \(P\) intersect because some bag contains both ends of every edge of \(P\).

If \(R(P)\) and \(R(Q)\) are disjoint, then \(d_G(P,Q)\ge2\). Otherwise either:

- \(P,Q\) share a vertex, in which case a bag containing it belongs to both traces; or
- some \(p\in P\) is adjacent to some \(q\in Q\), in which case a bag containing \(p,q\) belongs to both traces.

Consequently, \(k\) pairwise disjoint traces would give \(k\) pairwise distance-\(2\) \(S\)-\(T\) paths. If the first outcome does not hold, the family of traces has subtree-packing number at most \(k-1\). By Lemma 2.1, there are nodes
\[
r_1,\dots,r_m,\qquad m\le k-1,
\]
such that every trace contains some \(r_i\).

Choose a center \(c_{r_i}\) with
\[
B_{r_i}\subseteq B_G(c_{r_i},\rho),
\]
and set \(X=\{c_{r_i}:1\le i\le m\}\). Every \(S\)-\(T\) path meets one of the bags \(B_{r_i}\), and hence contains a vertex within distance \(\rho\) of \(X\). Also \(|X|\le m\le k-1\). \(\square\)

---

## 4. Chordal graphs

### Corollary 4.1
For every finite chordal graph \(G\), every \(k\ge1\), and all \(S,T\subseteq V(G)\), either there are \(k\) \(S\)-\(T\) paths pairwise at distance at least \(2\), or there is a set \(X\) of at most \(k-1\) vertices such that every \(S\)-\(T\) path meets \(B_G(X,1)\).

Thus the \(c=2\) conjecture holds for chordal graphs with the uniform choice
\[
\ell=1.
\]

### Proof
A finite chordal graph has a tree decomposition all of whose bags are cliques—the standard clique-tree characterization of chordal graphs. Every nonempty clique \(C\) is contained in the closed neighborhood of any vertex of \(C\). Hence this is a radius-\(1\) tree decomposition, and Theorem 3.1 applies. \(\square\)

The radius \(1\) cannot in general be replaced by \(0\). Let \(G=K_4\), with
\[
S=\{a,b\},\qquad T=\{c,d\},\qquad k=2.
\]
No two nonempty paths in \(K_4\) are at distance at least \(2\). On the other hand, the \(S\)-\(T\) edge-paths \(ac\) and \(bd\) are disjoint, so no single vertex meets every \(S\)-\(T\) path. One radius-\(1\) ball does meet them all.

A slightly more general formulation is useful:

### Corollary 4.2
Suppose \(G\) has a chordal supergraph \(H\) on the same vertex set such that every maximal clique of \(H\) is contained in a radius-\(\rho\) ball of \(G\). Then the conclusion holds with \(\ell=\rho\).

Indeed, a clique tree for \(H\) is also a tree decomposition of \(G\). In particular, if the graph power \(G^\rho\) is chordal, then the conclusion holds with \(\ell=\rho\), since every clique of \(G^\rho\) lies in a radius-\(\rho\) ball of \(G\).

---

## 5. Instances with terminals covering all vertices

There is a second argument that does not impose any structural restriction on \(G\).

### Proposition 5.1
Suppose there is an integer \(d\) such that every \(S\)-\(T\) path contains, as a subpath, an \(S\)-\(T\) path of length at most \(d\). Then the \(c=2\) conclusion holds with
\[
\ell=\left\lceil\frac d2\right\rceil+1.
\]

### Proof
Let \(\mathcal Q\) be the family of \(S\)-\(T\) paths of length at most \(d\). Choose an inclusion-maximal family
\[
Q_1,\dots,Q_r\in\mathcal Q
\]
pairwise at distance at least \(2\). If \(r\ge k\), the first outcome holds. Otherwise \(r\le k-1\).

Choose a middle vertex \(x_i\) of each \(Q_i\). Then
\[
V(Q_i)\subseteq B_G\left(x_i,\left\lceil\frac d2\right\rceil\right).
\]
Let \(P\) be any \(S\)-\(T\) path, and choose a short \(S\)-\(T\) subpath \(Q\subseteq P\). By maximality, \(Q\) is at distance at most \(1\) from some \(Q_i\). Hence \(P\) contains a vertex within distance
\[
\left\lceil\frac d2\right\rceil+1
\]
of \(x_i\). Taking \(X=\{x_1,\dots,x_r\}\) proves the assertion. \(\square\)

### Corollary 5.2
If \(S\cup T=V(G)\), then the conclusion holds with \(\ell=2\).

### Proof
Every \(S\)-\(T\) path contains an \(S\)-\(T\) subpath of length at most \(1\). If it contains a vertex in \(S\cap T\), that singleton is such a subpath. Otherwise its vertices are labelled \(S\setminus T\) or \(T\setminus S\); since its endpoints have opposite labels, some edge changes label. Apply Proposition 5.1 with \(d=1\). \(\square\)

When \(S,T\) partition \(V(G)\), this can equivalently be phrased through induced matchings in the cut \(\delta(S)\): pairwise distance-\(2\) one-edge \(S\)-\(T\) paths are exactly induced matchings in that cut. A maximal induced matching of size at most \(k-1\), with one chosen endpoint per matching edge, has radius-\(2\) balls meeting every cut edge and hence every \(S\)-\(T\) path.

---

## 6. Remaining gap

Theorem 3.1 always converts the problem into finding at most \(k-1\) bags of a tree decomposition that meet all \(S\)-\(T\) paths. The unresolved metric step is to ensure that those bags can each be covered by one ball of radius depending only on \(k\).

For chordal graphs, clique bags have radius \(1\). In a general graph, bags arising from a chordal completion may contain vertices very far apart in the original graph. Splitting such a bag among several centers loses the exact bound \(|X|\le k-1\). Neither the tree-decomposition argument nor the short-subpath argument gives a uniform bound for arbitrary graphs with long terminal-free path segments.

Thus these arguments establish genuine uniform special cases but do not settle or refute the general \(c=2\) conjecture.