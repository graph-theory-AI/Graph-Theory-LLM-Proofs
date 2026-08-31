```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A canonical matching–crown–half-graph trichotomy gives FPT on \(H_{t,t}\)-free graphs of bounded induced-matching number and settles \(t=2\), but the unrestricted mixed sparse–dense case remains open.",
  "would_publish": false,
  "caveats": "The main result has an additional bounded induced-matching hypothesis and uses the induced, or stronger semi-induced, interpretation of half-graph exclusion."
}
```

# Mathematical writeup

## 1. Conventions and results obtained

Let \(H_r=H_{r,r}\) be the bipartite graph with parts
\[
A=\{a_1,\ldots,a_r\},\qquad B=\{b_1,\ldots,b_r\},
\]
where
\[
a_i b_j\in E(H_r)\quad\Longleftrightarrow\quad i\le j.
\]

The meaningful interpretation of \(H_r\)-free here is induced exclusion. If ordinary subgraph exclusion were intended, then every \(K_{r,r}\) contains \(H_r\) as a subgraph, so the \(K_{r,r}\)-free algorithms reported in the prompt would already settle the question.

Write \(\Gamma(G)\) for the Grundy number. For the second problem, write \(\operatorname{bc}(G)\) for the largest \(r\) such that some induced subgraph of \(G\) has a proper \(r\)-coloring in which every color has a b-vertex. This is the bounded-certificate formulation underlying b-Chromatic Core.

I prove the following partial result.

### Theorem A

For every fixed \(t,d\), both Grundy Coloring and b-Chromatic Core are FPT, parameterized by \(k\), on the class
\[
\mathcal C_{t,d}=
\{G:G\text{ is induced-}H_t\text{-free and }\operatorname{im}(G)<d\},
\]
where \(\operatorname{im}(G)\) is the maximum number of edges in an induced matching.

More precisely, there is a computable \(F(k,t,d)\) such that every no-instance in \(\mathcal C_{t,d}\) has at most \(F(k,t,d)\) distinct open neighborhoods. Truncating each false-twin class then gives an equivalent instance with \(f(k,t,d)\) vertices.

The proof is based on a self-contained canonical matrix lemma: many distinct neighborhoods force one of a large matching matrix, a crown matrix, or a half-graph matrix. Crowns are immediate positive certificates for both problems, half-graphs are excluded, and the matching outcome is ruled out by the additional induced-matching hypothesis.

I also establish:

1. Both problems are FPT on graphs of bounded independence number, with a direct \(a(k-1)\)-vertex bound when \(\alpha(G)\le a\).
2. The case \(t=2\), where \(H_2=P_4\), is FPT for both problems.
3. An explicit family of \(H_3\)-free no-instances shows why neither bounded induced-matching number nor \(K_{s,s}\)-freeness alone captures the full problem.

---

## 2. Bounded certificates

A coloring \(c:V(H)\to[r]\) is a Grundy coloring if it is proper and every vertex of color \(i\) has a neighbor of every color \(j<i\).

### Lemma 2.1

If \(\Gamma(G)\ge k\), then \(G\) has an induced subgraph on at most
\[
q_\Gamma(k)=2^{k-1}
\]
vertices admitting a Grundy coloring with \(k\) colors.

#### Proof

Take a greedy coloring containing a vertex \(v\) of color \(k\). For every \(j<k\), choose a neighbor of \(v\) of color \(j\). Recursively, for every selected vertex of color \(i\), choose one neighbor of every smaller color.

If \(q_i\) is the maximum number of selected vertices needed below a root of color \(i\), then
\[
q_1=1,\qquad q_i\le 1+\sum_{j<i}q_j.
\]
Hence \(q_i\le 2^{i-1}\). The inherited coloring remains a Grundy coloring of the selected induced subgraph. ∎

### Lemma 2.2

If \(\operatorname{bc}(G)\ge k\), then \(G\) contains a \(k\)-color b-core on at most
\[
q_b(k)=k^2
\]
vertices.

#### Proof

First take any b-colored core with at least \(k\) colors and retain any \(k\) colors. For each retained color \(i\), choose a b-vertex \(d_i\). For every \(j\ne i\), choose one neighbor \(x_{ij}\) of \(d_i\) having color \(j\). The resulting set has at most
\[
k+k(k-1)=k^2
\]
vertices and remains properly colored, with every \(d_i\) still a b-vertex. ∎

Consequently, retaining \(q_\Gamma(k)\), respectively \(q_b(k)\), representatives from every false-twin class preserves the corresponding decision problem.

---

## 3. Three canonical bipartite patterns

Given disjoint sequences \(a_1,\ldots,a_r\) and \(b_1,\ldots,b_r\), impose no restrictions inside the two sequences and consider only cross-adjacencies.

- A **semi-induced matching** has
  \[
  a_i b_j\in E \iff i=j.
  \]
- A **semi-induced crown** has
  \[
  a_i b_j\in E \iff i\ne j.
  \]
- A **semi-induced half-graph** has
  \[
  a_i b_j\in E \iff i\le j.
  \]

### Lemma 3.1: crowns are positive certificates

If \(G\) contains either \(K_k\) or a semi-induced crown of order \(k\), then
\[
\Gamma(G)\ge k
\quad\text{and}\quad
\operatorname{bc}(G)\ge k.
\]

#### Proof

The clique case is immediate.

For a crown, give color \(i\) to the pair \(\{a_i,b_i\}\). This pair is nonadjacent. If \(j>i\), then \(a_j\) is adjacent to \(b_i\), and \(b_j\) is adjacent to \(a_i\). Thus this is a Grundy coloring.

It is also a b-coloring: \(a_i\) is adjacent to \(b_j\) for every \(j\ne i\), so \(a_i\) sees every other color. Edges inside the two sides are irrelevant because their vertices receive distinct colors. ∎

Thus any no-instance with target \(k\) contains neither \(K_k\) nor a semi-induced crown of order \(k\).

### Lemma 3.2: converting semi-induced half-graphs

Let \(R_r(s)\) denote the \(r\)-color diagonal Ramsey number. If \(G\) is induced-\(H_t\)-free and contains no \(K_k\), then \(G\) contains no semi-induced half-graph of order
\[
h=R_4(\max\{k,t\}).
\]

#### Proof

Suppose \(a_1,\ldots,a_h,b_1,\ldots,b_h\) form a semi-induced half-graph. Color each pair \(\{i,j\}\) by
\[
\bigl(\mathbf 1_{a_i a_j\in E(G)},\mathbf 1_{b_i b_j\in E(G)}\bigr)\in\{0,1\}^2.
\]
By four-color Ramsey, there is a set \(I\) of size \(\max\{k,t\}\) on which this pair is constant.

If either coordinate is \(1\), the corresponding side contains \(K_k\). If both coordinates are \(0\), then the selected vertices induce a half-graph containing an induced \(H_t\). Both alternatives contradict the assumptions. ∎

An identical argument gives the following.

### Lemma 3.3: converting semi-induced matchings

If \(G\) contains no \(K_k\) and \(\operatorname{im}(G)<d\), then it contains no semi-induced matching of order
\[
m=R_4(\max\{k,d\}).
\]

Indeed, applying the same four-color Ramsey argument to the internal edges of the two sides produces either a \(K_k\) or an induced matching of order \(d\).

---

## 4. A canonical set-system lemma

The following elementary lemma is the main combinatorial ingredient.

### Lemma 4.1: matching–crown–half-graph trichotomy

For \(s\ge1\), set
\[
B(s)=2^{\,2R_2(s+1)}.
\]
Let \(\mathcal F\) be a family of at least \(B(s)\) distinct subsets of a set \(X\). Then there are distinct sets
\[
F_1,\ldots,F_s\in\mathcal F
\]
and distinct elements
\[
x_1,\ldots,x_s\in X
\]
such that the incidence matrix \(\mathbf 1_{x_j\in F_i}\) is one of:

1. the identity matrix;
2. the complement of the identity matrix;
3. a half-graph matrix, after possibly reversing the indices.

#### Proof

Construct a binary decision tree for \(\mathcal F\). At a node containing at least two sets, choose an element \(x\) on which the sets disagree and split according to membership in \(x\). Continue until every leaf contains one set.

A binary tree with \(B(s)\) leaves has a root-to-leaf path with at least
\[
2R_2(s+1)
\]
internal nodes. Let these nodes be labeled \(x_1,\ldots,x_\ell\), in path order. Let \(p_i\in\{0,1\}\) be the membership decision taken by the main path at \(x_i\), and choose a set \(F_i\) from the sibling branch at that node.

Then:

- for \(j<i\), the set \(F_i\) followed the main path at \(x_j\), so
  \[
  \mathbf 1_{x_j\in F_i}=p_j;
  \]
- on the diagonal,
  \[
  \mathbf 1_{x_i\in F_i}=1-p_i;
  \]
- entries with \(j>i\) are initially unrestricted.

By pigeonhole, at least \(R_2(s+1)\) indices have the same value \(p_i=p\). For two such indices \(i<j\), color the pair by
\[
q_{ij}=\mathbf 1_{x_j\in F_i}.
\]
Ramsey's theorem gives \(s+1\) indices on which this value is constant, say \(q\).

The resulting matrix has:

- all entries below the diagonal equal to \(p\);
- diagonal entries equal to \(1-p\);
- all entries above the diagonal equal to \(q\).

There are four cases:

- \(p=q=0\): identity;
- \(p=q=1\): complement of identity;
- \(p=0,q=1\): the matrix \(1\iff i\le j\);
- \(p=1,q=0\): the strict lower-triangular matrix.

In the last case, delete the first row and last column and reindex; this gives a half-graph matrix of order \(s\). The labels \(x_i\) on one root-to-leaf path are distinct, since an element already fixed cannot split a descendant node. ∎

This is a finite and constructive statement; exact Ramsey numbers may be replaced by any standard computable upper bounds.

---

## 5. Bounding the number of neighborhood types

Let
\[
D(G)=\bigl|\{N_G(v):v\in V(G)\}\bigr|
\]
be the number of distinct open neighborhoods.

### Proposition 5.1

Fix \(k,t,d\ge2\). Define
\[
h=R_4(\max\{k,t\}),\qquad
m=R_4(\max\{k,d\}),
\]
\[
s=\max\{3h,\,3m,\,4k\},
\qquad
C(k,t,d)=B(s).
\]
If

- \(G\) is induced-\(H_t\)-free,
- \(\operatorname{im}(G)<d\), and
- either \(\Gamma(G)<k\) or \(\operatorname{bc}(G)<k\),

then
\[
D(G)<C(k,t,d).
\]

#### Proof

Suppose instead that \(D(G)\ge C(k,t,d)\). Choose one vertex for each distinct open neighborhood and apply Lemma 4.1 to the family of these neighborhoods. We obtain row vertices \(a_i\) and column vertices \(b_i\) forming a matching, crown, or half-graph incidence matrix of order \(s\).

The row and column sequences may overlap, so this must be addressed.

For indices with \(a_i\ne b_i\), define a graph on the index set by joining \(i\) and \(j\) whenever
\[
a_i=b_j\quad\text{or}\quad a_j=b_i.
\]
Since the \(a_i\)'s are distinct and the \(b_i\)'s are distinct, this collision graph has maximum degree at most \(2\). It therefore has an independent set containing at least one third of its vertices. On such a set of indices, the row and column vertex sets are disjoint.

For matching and half-graph matrices, diagonal entries are \(1\), so \(a_i\ne b_i\) automatically. We therefore obtain respectively:

- a disjoint semi-induced matching of order at least \(m\), contradicting Lemma 3.3;
- a disjoint semi-induced half-graph of order at least \(h\), contradicting Lemma 3.2.

For a crown matrix, diagonal entries are \(0\), so some \(a_i=b_i\) may occur. If this happens for \(k\) indices, those common vertices form a clique because all off-diagonal entries are \(1\). This is already a positive certificate. Otherwise, delete at most \(k-1\) such indices. Because \(s\ge4k\), the collision graph on the remaining indices has an independent set of size at least \(k\), giving a disjoint semi-induced crown of order \(k\). By Lemma 3.1, this is again a positive certificate.

Every outcome contradicts the assumption that the instance is negative. ∎

Equivalently, for every chosen \(d\), an \(H_t\)-free no-instance with many neighborhood types must contain an induced matching of order \(d\). Thus the only canonical matrix pattern not directly excluded by the two coloring problems is the sparse matching pattern.

---

## 6. Proof of Theorem A

Consider first Grundy Coloring. Compute the classes of vertices having identical open neighborhoods.

Vertices in one such class are pairwise nonadjacent: if \(u\) and \(v\) were adjacent and \(N(u)=N(v)\), then \(v\in N(u)=N(v)\), contradicting looplessness. Moreover, they are interchangeable false twins.

If the number of classes is at least \(C(k,t,d)\), Proposition 5.1 implies that the instance is positive.

Otherwise, retain at most
\[
q_\Gamma(k)=2^{k-1}
\]
vertices from each class. By Lemma 2.1, every positive instance has a witness using at most this many vertices in total, so the reduction preserves the answer in both directions. The reduced graph has fewer than
\[
C(k,t,d)\,2^{k-1}
\]
vertices. Its Grundy number can be computed by enumerating all vertex orders.

For b-Chromatic Core, use exactly the same argument with
\[
q_b(k)=k^2.
\]
The reduced graph has fewer than
\[
C(k,t,d)\,k^2
\]
vertices, and all subsets and \(k\)-colorings can be enumerated.

Thus both algorithms run in
\[
f(k,t,d)\,n^{O(1)}
\]
time. For fixed \(t,d\), this is FPT in \(k\). ∎

If the source uses the stronger notion of excluding a semi-induced half-graph, the theorem remains valid, and the Ramsey conversion in Lemma 3.2 can simply be replaced by the direct bound \(h=t\).

---

## 7. Two further tractable regimes

### 7.1 Bounded independence number

### Proposition 7.1

For every fixed \(a\), both problems are FPT on graphs satisfying \(\alpha(G)\le a\). In a negative instance,
\[
|V(G)|\le a(k-1).
\]

#### Proof

Since every color class in a proper coloring has size at most \(a\),
\[
\chi(G)\ge \left\lceil \frac{|V(G)|}{a}\right\rceil.
\]
Also \(\Gamma(G)\ge\chi(G)\).

For b-coloring, \(\operatorname{bc}(G)\ge\chi(G)\). Indeed, take a proper \(\chi(G)\)-coloring. If a color class had no b-vertex, every vertex in it would miss some other color entirely and could be recolored with such a missing color. Since the original color class is independent, all of its vertices can be recolored simultaneously, contradicting minimality of \(\chi(G)\).

Hence, if \(|V(G)|>a(k-1)\), both answers are positive. Otherwise the graph has \(O(ak)\) vertices and can be solved by brute force. ∎

Under the induced interpretation, every graph with \(\alpha(G)<t\) is automatically induced-\(H_t\)-free.

For \(\alpha(G)\le2\), one obtains an exact formula. Let \(F=\overline G\), which is triangle-free, and let \(\mu_{\min}^{\max}(F)\) be the minimum size of a maximal matching of \(F\). Then
\[
\Gamma(G)=|V(G)|-\mu_{\min}^{\max}(F).
\]

Indeed, every Grundy color class has size one or two. The two-vertex classes form a matching \(M\) in \(F\), and the singleton vertices form a clique in \(G\), so \(M\) is maximal in \(F\). Conversely, order the nonedge pairs of any maximal matching first and then the unmatched vertices as singleton classes. Triangle-freeness of \(F\) ensures that every later vertex sees each earlier pair, and maximality ensures that the unmatched vertices form a clique in \(G\).

### 7.2 The case \(t=2\)

Here \(H_2=P_4\), so induced-\(H_2\)-free graphs are cographs.

For disjoint union and complete join,
\[
\Gamma(G\mathbin{\dot\cup}H)=\max\{\Gamma(G),\Gamma(H)\},
\]
\[
\Gamma(G\vee H)=\Gamma(G)+\Gamma(H).
\]
The same recurrences hold for \(\chi\), and both invariants equal \(1\) on a single vertex. Consequently,
\[
\Gamma(G)=\chi(G)
\]
for every cograph, and Grundy Coloring is polynomial-time solvable from a cotree.

For b-Chromatic Core, let \(q=k^2\). At every cotree node, store all isomorphism types of induced subgraphs on at most \(q\) vertices realizable below that node. At a union node combine two stored types by disjoint union; at a join node combine them by complete join. The number of types depends only on \(q\), and at the root each stored graph can be tested by enumerating its \(k\)-colorings. This gives an \(f(k)n^{O(1)}\) algorithm.

Thus both questions are settled affirmatively for \(t=2\).

---

## 8. Why the bounded induced-matching hypothesis does not settle the problem

Large induced matchings do not themselves imply a positive answer: \(nK_2\) has induced-matching number \(n\), while both invariants are \(2\).

More significantly, large bicliques and large induced matchings can coexist in low-valued \(H_3\)-free graphs.

For \(n\ge2\), define \(F_n\) with
\[
A=\{a_1,\ldots,a_n\},\quad
B=\{b_1,\ldots,b_n\},\quad
X=\{x_1,\ldots,x_n\},
\]
and edges

- all edges between \(A\) and \(B\);
- the matching edges \(a_i x_i\);
- no other edges.

Then:

1. \(F_n\) contains \(K_{n,n}\) between \(A\) and \(B\);
2. \(\{a_i x_i:1\le i\le n\}\) is an induced matching;
3. \(F_n\) is induced-\(H_3\)-free;
4. \(\Gamma(F_n)=\operatorname{bc}(F_n)=3\).

For item 3, \(F_n\) is connected bipartite with parts \(A\) and \(B\cup X\). Relative to any three selected vertices of \(A\), a vertex of \(B\) has degree \(3\), while a vertex of \(X\) has degree at most \(1\). In \(H_3\), each side has a vertex of degree \(2\) into the other side, so no induced copy is possible.

For the lower bound \(\Gamma(F_n)\ge3\), order
\[
a_1,\ b_1,\ x_2,\ a_2.
\]
They receive colors \(1,2,1,3\).

There is no color-4 vertex. If a color-4 vertex lies in \(B\), it needs vertices of colors \(1,2,3\) in \(A\). The color-3 vertex in \(A\) needs a color-2 neighbor in \(B\cup X\). A color-2 neighbor in \(B\) is adjacent to the color-2 vertex in \(A\), violating properness, while a color-2 vertex \(x_i\) would need its sole neighbor—namely the color-3 vertex—to have color \(1\). The case of a color-4 vertex in \(A\) is symmetric, and vertices of \(X\) have degree one. Hence \(\Gamma(F_n)=3\).

A 3-color b-core is given by
\[
c(a_1)=1,\quad c(b_1)=2,\quad c(a_2)=3,\quad
c(x_1)=3,\quad c(x_2)=1.
\]
The vertices \(a_1,b_1,a_2\) are b-vertices.

For an upper bound, in any b-coloring with at least four colors, no \(x_i\) can be a b-vertex. If a b-vertex lies in \(B\), all other colors must occur in \(A\), so at most one color can have a b-vertex in \(B\). Every b-vertex in \(A\) can then see that one color through \(B\) and at most one additional color through its private neighbor \(x_i\), which is insufficient for four colors. If no b-vertex lies in \(B\), the conclusion is even more immediate. Thus \(\operatorname{bc}(F_n)=3\).

This family lies outside both currently tractable channels:

- it is not \(K_{s,s}\)-free for any fixed \(s\);
- its induced-matching number is unbounded.

It also has \(2n+1\) distinct open neighborhoods. In the canonical trichotomy, the unbounded neighborhood complexity is witnessed precisely by the matching pattern \(a_i x_i\).

---

## 9. Remaining gap

The unrestricted problem is not resolved.

The canonical lemma shows that, in an \(H_t\)-free no-instance, large neighborhood complexity cannot arise from crowns or half-graphs: it must pass through large induced matchings. The existing \(K_{s,s}\)-free algorithms handle globally biclique-free graphs, while Theorem A handles graphs where the induced-matching channel is bounded. What is missing is an algorithmic decomposition for graphs in which large complete bipartite pairs and large induced matchings coexist, as in \(F_n\).

A plausible route would be a bounded “flip” decomposition: \(F_n\), for example, becomes a matching after toggling the complete pair \(A\)-\(B\). I do not have a proof that every relevant \(H_t\)-free no-instance admits a bounded number of such flips, nor a proof that the known Grundy/b-core algorithms remain FPT under the required flips. Consequently, no full FPT algorithm or W[1]-hardness reduction is claimed.