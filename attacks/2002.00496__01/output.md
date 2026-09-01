```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "Unavoidability is proved to be componentwise, yielding additional connected unavoidable graphs such as a K4 joined by a bridge or at a vertex to any cycle, while arbitrary connected Kelly minors remain unresolved.",
  "would_publish": false,
  "caveats": "The argument uses the excluded-grid theorem and the known unavoidability of ladders and K4; literature novelty was not checked."
}
```

# Mathematical writeup

## 1. Reformulation

All graphs and posets are finite. Write \(\operatorname{cov}(P)\) for the cover graph of a poset \(P\). For a graph \(H\), let

\[
d(H)=\sup\{\dim(P):\operatorname{cov}(P)\text{ is }H\text{-minor-free}\}.
\]

Thus \(H\) is unavoidable exactly when \(d(H)<\infty\).

Unavoidability is downward closed under minors: if \(H\preccurlyeq_m F\) and \(F\) is unavoidable, then \(H\) is unavoidable.

Kelly's construction supplies planar cover graphs of arbitrarily large dimension. Consequently, every unavoidable graph is planar: a nonplanar graph cannot be a minor of any of those planar cover graphs.

The main partial result proved below is the following.

### Theorem 1 — Componentwise unavoidability

A finite graph \(H\) is unavoidable if and only if every connected component of \(H\) is unavoidable.

The forward implication is immediate from minor-closedness. The converse requires some care because deleting vertices from a cover graph need not produce the cover graph of the induced subposet: new cover relations can appear. The next lemma handles precisely this issue.

---

## 2. Stability under deleting a bounded vertex set from the cover graph

### Lemma 2

Suppose every poset whose cover graph is \(H\)-minor-free has dimension at most \(d\). Let \(P\) be a poset, let \(G=\operatorname{cov}(P)\), and let \(X\subseteq V(G)\). If \(G-X\) is \(H\)-minor-free, then

\[
\dim(P)\le 2^{|X|}d+2|X|.
\tag{1}
\]

#### Proof

First recall the elementary inequality

\[
\dim(P)\le \dim(P-X)+2|X|.
\tag{2}
\]

It suffices to prove this when \(X=\{x\}\). Every linear extension of \(P-x\) extends to a linear extension of \(P\). Add two further linear extensions:

- one in which every element incomparable with \(x\) occurs below \(x\);
- one in which every element incomparable with \(x\) occurs above \(x\).

Such extensions exist: the strict downset of \(x\) is an initial set, as is the set consisting of the strict downset together with all elements incomparable with \(x\). These two extensions reverse every incomparable pair involving \(x\). Iterating proves (2).

It remains to bound \(\dim(P-X)\). For \(v\in P-X\) and \(x\in X\), record whether

\[
v<x,\qquad x<v,\qquad\text{or}\qquad v\parallel x.
\]

For each map \(\varepsilon:X\to\{-,+\}\), define

\[
S_\varepsilon=
\left\{
v\in P-X:
\begin{array}{ll}
\varepsilon(x)=- &\Longrightarrow x\nless v,\\
\varepsilon(x)=+ &\Longrightarrow v\nless x
\end{array}
\text{ for every }x\in X
\right\}.
\]

Thus the sign \(-\) permits elements below or incomparable with \(x\), while \(+\) permits elements above or incomparable with \(x\).

Each \(S_\varepsilon\) is order-convex in \(P\). Indeed, suppose \(a\le b\le c\) and \(a,c\in S_\varepsilon\). If \(\varepsilon(x)=-\) and \(x<b\), then \(x<c\), contrary to \(c\in S_\varepsilon\). The case \(\varepsilon(x)=+\) is dual. Hence \(b\in S_\varepsilon\).

It follows that

\[
\operatorname{cov}(P[S_\varepsilon])=G[S_\varepsilon].
\]

In particular this cover graph is a subgraph of \(G-X\), and therefore it is \(H\)-minor-free. Consequently,

\[
\dim(P[S_\varepsilon])\le d.
\tag{3}
\]

Every incomparable pair \(u,v\in P-X\) lies together in at least one \(S_\varepsilon\). For a fixed \(x\in X\), the only obstruction would be that one of \(u,v\) is below \(x\) and the other above \(x\); but then \(u,v\) would be comparable. Thus one can choose an allowed sign independently for every \(x\).

For every \(\varepsilon\), take a realizer of \(P[S_\varepsilon]\) of size at most \(d\), and extend each of its linear extensions to all of \(P-X\). Since every incomparable pair belongs to some \(S_\varepsilon\), the union of these extended realizers realizes \(P-X\). There are \(2^{|X|}\) choices of \(\varepsilon\), so

\[
\dim(P-X)\le 2^{|X|}d.
\]

Combining this with (2) proves (1). \(\square\)

This lemma may be viewed as saying that the class of cover graphs forcing bounded dimension remains dimension-bounded after adding a bounded number of apex vertices.

---

## 3. A tree-decomposition blocker lemma

We use two standard graph-theoretic facts.

1. If \(F\) is a fixed planar graph, then there is \(t(F)\) such that every \(F\)-minor-free graph has treewidth at most \(t(F)\). Indeed, \(F\) is a minor of a sufficiently large grid, and the excluded-grid theorem applies.

2. For a family of subtrees of a tree, the minimum number of tree vertices meeting all members equals the maximum number of pairwise disjoint members. Only the easy consequence is needed: if there are no \(c+1\) pairwise disjoint members, then \(c\) tree vertices meet all of them. This can be proved by induction, repeatedly deleting a leaf of the host tree.

We need the following slightly asymmetric extension.

### Lemma 3

Let \(\mathcal A\) be a family of subtrees of a tree \(T\). Let \(\mathcal B\) be a family in which every member is the union of at most \(c\) subtrees of \(T\). Suppose every member of \(\mathcal A\) intersects every member of \(\mathcal B\). Then either

- at most \(c\) vertices of \(T\) meet every member of \(\mathcal A\), or
- at most \(\binom{c+1}{2}\) vertices of \(T\) meet every member of \(\mathcal B\).

#### Proof

If \(\mathcal A\) has no \(c+1\) pairwise disjoint members, the subtree transversal property gives the first conclusion.

Otherwise choose pairwise disjoint \(A_1,\dots,A_{c+1}\in\mathcal A\). For each \(i<j\), choose a vertex \(z_{ij}\) on the unique path between \(A_i\) and \(A_j\).

Let \(B=R_1\cup\cdots\cup R_c\in\mathcal B\), where every \(R_\ell\) is a subtree. Since \(B\) meets every \(A_i\), by the pigeonhole principle some \(R_\ell\) meets both \(A_i\) and \(A_j\) for a pair \(i<j\). Being connected, \(R_\ell\) contains the path between \(A_i\) and \(A_j\), and hence contains \(z_{ij}\). Therefore

\[
\{z_{ij}:1\le i<j\le c+1\}
\]

meets every member of \(\mathcal B\). \(\square\)

For a tree decomposition \((T,\{B_t\})\), the set of nodes \(t\) whose bag meets a fixed connected vertex set of the graph is a subtree of \(T\). Thus Lemma 3 applies to footprints of connected minor models.

---

## 4. Proof of componentwise unavoidability

We prove the nontrivial implication of Theorem 1 in the following form.

### Theorem 4

Let \(H_1,\dots,H_r\) be connected planar unavoidable graphs. Then

\[
H_1\sqcup\cdots\sqcup H_r
\]

is unavoidable.

#### Proof

Proceed by induction on \(r\). The case \(r=1\) is the assumption.

Let

\[
A=H_1,\qquad B=H_2\sqcup\cdots\sqcup H_r,\qquad
F=A\sqcup B.
\]

By induction, \(B\) is unavoidable. Let \(d_A,d_B\) be dimension bounds for posets whose cover graphs exclude \(A,B\), respectively. Put \(c=r-1\), the number of connected components of \(B\).

Since \(F\) is planar, every \(F\)-minor-free graph has treewidth at most some fixed \(t=t(F)\).

Let \(P\) be a poset whose cover graph \(G\) is \(F\)-minor-free, and fix a tree decomposition of \(G\) of width at most \(t\).

For every \(A\)-minor model, the union of its branch sets is connected, so its footprint in the decomposition tree is a subtree. Let \(\mathcal A\) be the family of all these footprints.

A \(B\)-minor model consists of models of its \(c\) connected components. Its footprint is therefore the union of at most \(c\) subtrees. Let \(\mathcal B\) be the resulting family.

Every member of \(\mathcal A\) intersects every member of \(\mathcal B\). Indeed, if an \(A\)-model and a \(B\)-model had disjoint vertex sets, their union would be an \(F=A\sqcup B\) minor model.

Apply Lemma 3.

- In the first outcome, at most \(c\) decomposition nodes meet every \(A\)-model footprint. The union \(X\) of their bags has size at most
  \[
  c(t+1),
  \]
  and \(G-X\) is \(A\)-minor-free.

- In the second outcome, at most \(\binom{c+1}{2}\) decomposition nodes meet every \(B\)-model footprint. The union \(X\) of their bags has size at most
  \[
  \binom{c+1}{2}(t+1),
  \]
  and \(G-X\) is \(B\)-minor-free.

Lemma 2 now gives a finite dimension bound in either case. Explicitly, if

\[
\Phi(d,s)=2^s d+2s,
\]

then

\[
\dim(P)\le
\max\left\{
\Phi\!\left(d_A,c(t+1)\right),
\Phi\!\left(d_B,\binom{c+1}{2}(t+1)\right)
\right\}.
\]

Thus \(F\) is unavoidable. \(\square\)

### Corollary 5

A finite graph \(H\) is unavoidable if and only if every connected component of \(H\) is unavoidable.

#### Proof

If \(H\) is unavoidable, each component is a minor of \(H\), hence unavoidable.

Conversely, every unavoidable component is planar, by Kelly's planar examples. Theorem 4 then applies to their disjoint union. \(\square\)

In particular, the class of unavoidable graphs is closed under finite disjoint unions. This reduces the characterization problem, on the unavoidability side, to connected graphs.

---

## 5. Turning disjoint models into connected unavoidable graphs

There is also a useful connected consequence.

### Proposition 6

Let \(A\) and \(B\) be connected, vertex-transitive, unavoidable graphs. Then the following graphs are unavoidable:

1. the graph obtained from disjoint copies of \(A\) and \(B\) by adding one edge between prescribed vertices;
2. the graph obtained by identifying one prescribed vertex of \(A\) with one prescribed vertex of \(B\).

#### Proof

By Corollary 5, \(A\sqcup B\) is unavoidable.

For completeness, if the cover graph of a poset has components inducing posets \(P_1,\dots,P_s\), then

\[
\dim(P)=\max\left(2,\max_i\dim(P_i)\right)
\]

whenever there is more than one component. Indeed, realizers of the components can be concatenated in one component order in one linear extension and in the reverse component order in another.

Hence a poset of sufficiently large dimension has a connected cover-graph component of sufficiently large dimension. Inside that component, unavoidability of \(A\sqcup B\) gives vertex-disjoint minor models of \(A\) and \(B\).

Choose a shortest path between the two model vertex sets. Its internal vertices avoid both models. Its endpoints lie in branch sets corresponding to vertices \(a\in V(A)\) and \(b\in V(B)\). Vertex-transitivity permits relabeling the two models so that \(a,b\) are the prescribed attachment vertices. Contracting the internal part of the path gives a single edge between the two models. This proves the first assertion.

Contracting that added edge identifies the two attachment vertices, proving the second assertion by minor-closedness of unavoidability. \(\square\)

---

## 6. Explicit additional positive cases

For every \(m\ge3\), the cycle \(C_m\) is unavoidable. Indeed, for sufficiently large \(k\), the perimeter cycle \(C_{2k}\) of the ladder \(L_k\) has \(C_m\) as a minor. Since \(L_k\) is unavoidable, so is \(C_m\).

Both \(K_4\) and \(C_m\) are vertex-transitive. Proposition 6 therefore gives:

### Corollary 7

For every \(m\ge3\), each of the following is unavoidable:

- \(K_4\sqcup C_m\);
- a copy of \(K_4\) and a copy of \(C_m\) joined by a bridge;
- the vertex-sum of \(K_4\) and \(C_m\).

In particular, two copies of \(K_4\) joined by a bridge, or sharing one vertex, are unavoidable.

These connected graphs are not obtained merely by taking a minor of one of the previously listed positive graphs:

- they contain a \(K_4\), while every ladder has treewidth at most \(2\);
- they have more than four vertices, so they are not minors of \(K_4\).

Thus they give explicit positive cases beyond the individual minor closures of ladders and \(K_4\).

---

## 7. What remains open

The argument does not prove that every connected minor of a Kelly graph is unavoidable. In particular, it gives no general operation preserving unavoidability under arbitrary rooted sums, 2-sums, or the more highly connected configurations that can occur inside Kelly graphs.

The established progress is therefore:

1. unavoidability has an exact componentwise characterization;
2. bounded vertex perturbations of an \(H\)-minor-free cover graph preserve bounded dimension;
3. finite collections of already unavoidable connected graphs can be forced vertex-disjointly;
4. for vertex-transitive targets, two such models can be joined to obtain additional connected unavoidable graphs.

The conjectured characterization remains open in its essential connected case.