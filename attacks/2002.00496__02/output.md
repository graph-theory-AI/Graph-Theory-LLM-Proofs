```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture remains open, but bounded deletion preserves dimension bounds, which yields planar packing closure and proves that the edge-sum of two copies of K4 is an unavoidable Kelly minor.",
  "would_publish": false,
  "caveats": "The horizontally subdivided K4 gadget and arbitrary connected Kelly chains remain unresolved here; standard established Erdős–Pósa, treewidth-two dimension, and block-pasting theorems are used."
}
```

## 1. Setup and status

For a finite poset \(P\), let \(C(P)\) denote its cover graph. A graph \(H\) is **unavoidable** when there is a constant \(D_H\) such that
\[
H\not\preceq C(P)\quad\Longrightarrow\quad \dim(P)\le D_H
\]
for every finite poset \(P\), where \(\preceq\) denotes the minor relation.

Two elementary observations are useful.

1. Unavoidability is minor-downward: if \(J\preceq H\) and \(H\) is unavoidable, then \(J\) is unavoidable.
2. Consequently, to prove the conjectured sufficiency it would be enough to prove that every full member of Kelly's construction is unavoidable.

I do not prove that. I obtain instead:

- a general bounded-deletion lemma for poset dimension;
- closure of planar unavoidable graphs under taking a fixed number of disjoint copies;
- a connected, treewidth-three special case directly relevant to Kelly's construction:
  \[
  K_4\oplus_{K_2}K_4
  \]
  is unavoidable, where the two copies of \(K_4\) are identified along an edge.

The latter graph is a minor of a two-cell Kelly graph: simply contract all designated horizontal subdivisions.

---

## 2. A bounded-deletion lemma

The main technical observation is that deleting vertices from a cover graph must be handled using an auxiliary poset, rather than the induced subposet, because deleting elements can create new cover relations.

### Lemma 2.1

Let \(P\) be a poset, let \(X\subseteq P\), with \(|X|=k\), and define a poset \(R=R(P,X)\) on \(P-X\) by
\[
u\le_R v
\]
if and only if \(u=v\), or the Hasse diagram of \(P\) contains a directed \(u\)-\(v\) path avoiding \(X\).

If \(\dim(R)\le d\), where \(d\ge 1\), then
\[
\boxed{\dim(P)\le 3^k d+2k.}
\]

Moreover,
\[
C(R)\subseteq C(P)-X.
\]

### Proof

The assertion \(C(R)\subseteq C(P)-X\) is immediate. If \(u\prec_R v\), then a directed \(u\)-\(v\) path in the Hasse diagram of \(P-X\) cannot have an internal vertex, since such a vertex would lie strictly between \(u\) and \(v\) in \(R\). Thus \(uv\) is already a cover edge of \(P\).

We use the standard critical-pair characterization of dimension:

- a collection of linear extensions is a realizer if it reverses every critical pair;
- a set of ordered incomparable pairs is reversible if and only if it contains no alternating cycle.

Let
\[
\mathcal L=\{L_1,\dots,L_d\}
\]
be a realizer of \(R\).

For \(v\in P-X\), define its \(X\)-profile
\[
\sigma(v)\in\{<,>,\parallel\}^{X}
\]
by recording, for each \(x\in X\), whether \(v<x\), \(x<v\), or \(v\parallel x\) in \(P\).

Consider a critical pair \((a,b)\) of \(P\) with \(a,b\notin X\). Since \(R\) is a suborder of \(P-X\), the elements \(a,b\) remain incomparable in \(R\). Choose an index \(i\) such that
\[
b<_{L_i}a,
\]
and color \((a,b)\) by
\[
(\sigma(b),i).
\]
There are at most \(3^k d\) such colors.

We claim that every color class is reversible. Suppose to the contrary that
\[
(a_1,b_1),\ldots,(a_m,b_m)
\]
is a monochromatic alternating cycle, with indices modulo \(m\). Thus
\[
a_j\le_P b_{j+1}
\]
for every \(j\), all the \(b_j\) have the same \(X\)-profile, and
\[
b_j<_{L_i}a_j
\]
for a common \(i\).

We claim that \(a_j\le_R b_{j+1}\) for every \(j\). If not, take a saturated \(a_j\)-\(b_{j+1}\) chain in \(P\). It must meet \(X\). Let \(x\in X\) be the last member of \(X\) on that chain. Then
\[
a_j\le_P x<_P b_{j+1}.
\]
Since \(b_j\) and \(b_{j+1}\) have the same \(X\)-profile, \(x<_P b_j\) as well. Hence
\[
a_j<_P b_j,
\]
contrary to their being incomparable. Therefore all connecting relations of the alternating cycle belong to \(R\).

But then in \(L_i\),
\[
b_1<_{L_i}a_1\le_{L_i}b_2<_{L_i}a_2
 \le_{L_i}\cdots\le_{L_i}b_1,
\]
which is impossible. Thus every one of the \(3^k d\) classes is reversible.

It remains to handle critical pairs having an endpoint in \(X\). For each \(x\in X\), put all critical pairs of the form \((x,b)\) in one class, and all remaining critical pairs of the form \((a,x)\) in another class. Each such class is reversible: an alternating cycle of pairs \((x,b_j)\) would require \(x\le b_{j+1}\), contradicting \(x\parallel b_{j+1}\), and the dual argument applies to pairs \((a_j,x)\).

Thus another \(2k\) reversible classes suffice. The critical-pair criterion now gives
\[
\dim(P)\le 3^k d+2k. \qedhere
\]

### Corollary 2.2

Suppose all posets whose cover graphs are \(H\)-minor-free have dimension at most \(D_H\). If \(X\subseteq V(C(P))\) has size \(k\) and
\[
C(P)-X
\]
is \(H\)-minor-free, then
\[
\dim(P)\le 3^k D_H+2k.
\]

Indeed, the auxiliary poset \(R(P,X)\) has cover graph contained in \(C(P)-X\).

This lemma is useful because it gives a dimension bound from a bounded minor-transversal, even though \(P-X\) itself may acquire many new cover edges.

---

## 3. A planar packing closure theorem

Write \(rH\) for the disjoint union of \(r\) copies of \(H\).

### Theorem 3.1

Let \(H\) be a connected planar unavoidable graph. Then \(rH\) is unavoidable for every fixed \(r\ge1\). Quantitatively, if

- \(D_H\) bounds the dimension of posets with \(H\)-minor-free cover graph, and
- \(\eta_H(r)\) is a planar-minor Erdős–Pósa bound,

then every poset whose cover graph excludes \(rH\) has dimension at most
\[
3^{\eta_H(r)}D_H+2\eta_H(r).
\]

### Proof

Use the established Erdős–Pósa theorem for planar minors: for fixed planar \(H\) and \(r\), every graph either has \(r\) vertex-disjoint \(H\)-minor models or has a vertex set \(X\), of size at most \(\eta_H(r)\), meeting every \(H\)-minor model.

If \(C(P)\) excludes \(rH\), the first outcome is impossible. Hence there is such an \(X\), and
\[
C(P)-X
\]
is \(H\)-minor-free. Apply Corollary 2.2. \(\square\)

Consequently, if \(J\preceq rH\), then \(J\) is also unavoidable.

### Applications

The source theorem says every fixed ladder \(L_s\) is unavoidable. Hence, for every \(r,s\),

\[
rL_s
\]
and every minor of \(rL_s\) are unavoidable.

It is also established that posets whose cover graphs have treewidth at most \(2\) have bounded dimension. Since \(K_4\)-minor-free graphs are exactly the graphs of treewidth at most \(2\), \(K_4\) is unavoidable. Therefore

\[
rK_4
\]
and every minor of \(rK_4\) are unavoidable.

These already give an infinite collection of, generally disconnected, Kelly minors for which the conjecture holds.

---

## 4. A connected Kelly minor: two \(K_4\)'s sharing an edge

Let
\[
F_2:=K_4\oplus_{K_2}K_4,
\]
the graph obtained from two copies of \(K_4\) by identifying an edge. This is planar, \(2\)-connected, and has treewidth \(3\).

### Lemma 4.1: a linking lemma

If a \(2\)-connected graph \(G\) contains two vertex-disjoint \(K_4\)-minor models, then
\[
F_2\preceq G.
\]

### Proof

Because \(K_4\) has maximum degree \(3\), every \(K_4\) minor contains a subdivision of \(K_4\). Let \(S_1,S_2\) be vertex-disjoint subdivisions of \(K_4\) in \(G\).

By the vertex version of Menger's theorem and \(2\)-connectivity, there are two vertex-disjoint \(S_1\)-\(S_2\) paths, internally disjoint from \(S_1\cup S_2\), with distinct endpoints
\[
x_1,x_2\in V(S_1),\qquad y_1,y_2\in V(S_2).
\]

We use the following elementary property of a subdivision \(S\) of \(K_4\):

> For any two distinct vertices \(x,y\in V(S)\), \(S\) has a \(K_4\)-minor model in which \(x\) and \(y\) belong to distinct branch sets.

To see this, regard \(S\) as six internally disjoint paths corresponding to the edges of an abstract \(K_4\). If \(x,y\) lie on the same branch path, assign them to its opposite ends. If they lie on distinct branch paths, choose distinct endpoints of those two abstract edges and contract toward those endpoints. This is always possible because two distinct edges of \(K_4\) have at least three endpoints between them. Contracting the remaining path segments gives the desired rooted \(K_4\) model.

Apply this observation in \(S_1\) to \(x_1,x_2\), and in \(S_2\) to \(y_1,y_2\). Now contract the first linking path so that the branch set containing \(x_1\) is identified with the one containing \(y_1\), and similarly contract the second linking path. The two resulting \(K_4\)'s share two distinct branch sets. Since every pair of vertices is adjacent in \(K_4\), those shared branch sets form the common edge. Deleting extra edges gives \(F_2\). \(\square\)

We also use the standard block-pasting theorem for posets:

> If every block \(B\) of the cover graph of \(P\) satisfies
> \[
> \dim(P[B])\le d,
> \]
> then
> \[
> \dim(P)\le d+2.
> \]

The extra two extensions account for incomparable pairs whose endpoints lie in different branches of the block-cut tree.

### Theorem 4.2

The graph
\[
\boxed{F_2=K_4\oplus_{K_2}K_4}
\]
is unavoidable.

### Proof

Let \(D_4\) be an absolute dimension bound for posets with \(K_4\)-minor-free cover graph. Such a bound exists by the established treewidth-two dimension theorem.

Let \(c\) be an Erdős–Pósa constant such that every graph either has two vertex-disjoint \(K_4\)-minor models or has a set of at most \(c\) vertices meeting all \(K_4\)-minor models.

Let \(P\) be a poset whose cover graph \(G=C(P)\) excludes \(F_2\), and let \(B\) be a block of \(G\).

If \(B\) is \(2\)-connected, Lemma 4.1 shows that \(B\) cannot contain two vertex-disjoint \(K_4\)-minor models. Therefore there exists
\[
X_B\subseteq V(B),\qquad |X_B|\le c,
\]
such that \(B-X_B\) is \(K_4\)-minor-free.

We must check that the induced subposet \(P[B]\) behaves correctly. Any saturated chain in \(P\) whose endpoints lie in \(B\) stays in \(B\): if its underlying simple path left \(B\) and re-entered at a different vertex, the outside subpath together with a path in \(B\) would lie in a larger \(2\)-connected subgraph, contradicting maximality of \(B\). Hence
\[
C(P[B])\subseteq B.
\]

Apply Lemma 2.1 to \(P[B]\) and \(X_B\). The resulting auxiliary poset has \(K_4\)-minor-free cover graph, so
\[
\dim(P[B])\le 3^cD_4+2c.
\]
The same bound is trivial for bridge blocks.

The block-pasting theorem now gives
\[
\dim(P)\le 3^cD_4+2c+2.
\]
This is independent of \(P\), proving that \(F_2\) is unavoidable. \(\square\)

Since contracting all horizontal subdivisions in two consecutive cells of Kelly's construction produces \(F_2\), this proves the conjecture for a genuine connected Kelly minor that is not series-parallel. By minor-downward closure, every minor of \(F_2\) is also unavoidable. Since \(F_2\) is planar, Theorem 3.1 additionally proves that \(rF_2\) and all its minors are unavoidable for every fixed \(r\).

---

## 5. Why the horizontally subdivided \(K_4\) remains difficult

Let \(Q\) be the graph obtained by subdividing two opposite edges of \(K_4\) once. It is isomorphic to
\[
K_{3,3}-e.
\]
This is the natural one-cell horizontal subdivision in the stated reformulation of Kelly's construction.

There is a second minimal triangle-free way for a \(K_4\) minor to occur. Let \(T\) be obtained by subdividing the three edges of one triangle of \(K_4\) once.

### Lemma 5.1

Every triangle-free graph with a \(K_4\) minor contains either \(Q\) or \(T\) as a minor.

### Proof

A \(K_4\) minor yields a subdivision \(S\) of \(K_4\). Call an abstract edge of \(K_4\) **long** if its corresponding path in \(S\) has an internal vertex.

Because the ambient graph is triangle-free, the set \(\mathcal E\) of long abstract edges meets every triangle of \(K_4\).

- If \(\mathcal E\) contains two disjoint edges, contract every other branch path to one edge and reduce those two paths to length two. This gives \(Q\).
- Otherwise, \(\mathcal E\) is a pairwise-intersecting family of edges of \(K_4\). Such a family lies in a star or in a triangle. A star misses the triangle avoiding its center, so it cannot meet every triangle. Hence \(\mathcal E\) contains the three edges of a triangle. Reducing those three paths to length two gives \(T\).

Thus one of \(Q,T\) occurs. \(\square\)

This dichotomy is sharp: \(T\) does not contain \(Q\) as a minor. Indeed, \(T\) has seven vertices and nine edges, while \(Q\) has six vertices and eight edges.

- Deleting one vertex of \(T\) leaves at most seven edges.
- Thus a \(Q\) minor would have to arise by contracting exactly one edge and deleting no edge.
- Contracting an edge incident with a subdivision vertex creates a triangle.
- Contracting one of the three unsubdivided spokes gives degree sequence
  \[
  (4,3,3,2,2,2),
  \]
  whereas \(Q\) has degree sequence
  \[
  (3,3,3,3,2,2).
  \]

Moreover, \(T\) is bipartite and therefore is itself the cover graph of a height-two poset.

This explains why simply invoking the known \(K_4\)-minor-free dimension theorem cannot prove unavoidability of \(Q\): a \(Q\)-minor-free cover graph may still contain many \(T\)-type \(K_4\) subdivisions.

There is nevertheless a necessary condition on any counterexample sequence. If \(P_n\) are \(Q\)-minor-free posets with \(\dim(P_n)\to\infty\), then the minimum size of a vertex set meeting every \(K_4\)-minor model in \(C(P_n)\) must tend to infinity. Otherwise Lemma 2.1 and the treewidth-two dimension bound would give a uniform dimension bound. By planar-minor Erdős–Pósa, such a sequence must contain arbitrarily many vertex-disjoint \(K_4\) models, and Lemma 5.1 then gives arbitrarily many vertex-disjoint \(T\) minors.

Thus any counterexample already for \(Q\) would have to exploit the global order-theoretic interaction of many \(T\)-type pieces, not merely one local alternative \(K_4\) subdivision.

---

## 6. Remaining gap

The argument does not control long path-like systems of \(2\)-separations with horizontally subdivided edges. In particular, it does not prove that \(Q\cong K_{3,3}-e\), or any full subdivided Kelly chain, is unavoidable.

The bounded-deletion lemma handles a bounded global transversal. The edge-sum theorem succeeds because excluding \(K_4\oplus_{K_2}K_4\) bounds the \(K_4\)-packing number inside each block. For \(Q\)-minor-free graphs, arbitrarily many \(T\)-type \(K_4\) pieces can survive, and a further composition theorem sensitive to their Hasse orientations and their arrangement through \(2\)-separations is needed.

No explicit unbounded-dimension \(Q\)-minor-free family is produced, so this is not a counterexample.