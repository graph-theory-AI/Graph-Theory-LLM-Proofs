```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The general 5/6 bound remains unresolved here, but it holds for all sparse cases and for every plane quadrangulation having a bipartition class of maximum degree at most three.",
  "would_publish": false,
  "caveats": "Dense quadrangulations with degree at least four occurring in both bipartition classes are not covered, and no counterexample is produced."
}
```

## 1. Statement and reformulation

All graphs below are finite and simple. Write
\[
\tau(G):=\min\{|D|:G-D\text{ is 2-degenerate}\}.
\]
Then
\[
\tau(G)=|V(G)|-\alpha_2(G).
\]
Thus the proposed bound
\[
\alpha_2(G)\ge \frac56|V(G)|
\]
is equivalent, with the necessary rounding, to
\[
\tau(G)\le \left\lfloor\frac{|V(G)|}{6}\right\rfloor.
\tag{1}
\]

A graph is 2-degenerate exactly when iterative deletion of vertices of current degree at most two removes every vertex. I will use this peeling characterization throughout.

The parameter \(\alpha_2\) is additive over components, so it suffices to consider connected graphs.

---

## 2. Consequences of the theorem in the source paper

The quoted theorem of Dvořák and Kelly says that a connected triangle-free planar graph with \(n\) vertices and \(m\) edges satisfies
\[
\alpha_2(G)\ge \frac{6n-m-1}{5}.
\tag{2}
\]

### 2.1 A sparse-graph range proving the \(5/6\) bound

From (2),
\[
m\le \frac{11n-6}{6}
\quad\Longrightarrow\quad
\alpha_2(G)\ge \frac56n.
\tag{3}
\]

Indeed,
\[
\frac{6n-m-1}{5}
 \ge
\frac{6n-(11n-6)/6-1}{5}
=\frac56n.
\]

Thus only graphs with
\[
m>\frac{11n-6}{6}
\tag{4}
\]
can be counterexamples.

### 2.2 Girth at least five

If \(G\) has girth at least five, blockwise application of the usual planar girth bound gives
\[
m\le \frac53(n-1).
\]
For a 2-connected cyclic block \(B\), this follows from
\[
m(B)\le \frac53(|V(B)|-2);
\]
a bridge block also satisfies \(1\le \frac53(2-1)\), and
\(\sum_B(|V(B)|-1)=n-1\).

Substitution in (2) yields
\[
\alpha_2(G)
 \ge \frac{6n-\frac53(n-1)-1}{5}
 =\frac{13n+2}{15}
 =\frac56n+\frac{n+4}{30}.
\tag{5}
\]

Hence the \(5/6\) assertion is proved, with room to spare, for every planar graph of girth at least five. In particular, every counterexample must contain a 4-cycle.

### 2.3 A bound in terms of quadrilateral faces

Suppose \(G\) is given with a connected plane embedding in which every facial boundary walk has length at least four; this holds in particular when \(G\) is 2-connected and triangle-free. Let \(q\) be the number of faces of length four. All remaining faces have length at least five, so
\[
2m=\sum_f |\partial f|
   \ge 4q+5(f-q)=5f-q.
\]
Using \(f=m-n+2\), we obtain
\[
m\le \frac{5n+q-10}{3}.
\]
Consequently, (2) gives
\[
\alpha_2(G)\ge \frac{13n-q+7}{15}.
\tag{6}
\]
In particular,
\[
q\le \frac{n+14}{2}
\quad\Longrightarrow\quad
\alpha_2(G)\ge \frac56n.
\tag{7}
\]

Thus a 2-connected counterexample would have more than \((n+14)/2\) quadrilateral faces. This isolates the dense, 4-face-rich regime.

### 2.4 Small orders

Euler's inequality \(m\le 2n-4\) and (2) imply
\[
\alpha_2(G)\ge \frac{4n+3}{5}.
\tag{8}
\]
For \(n\le18\), this is at least \(5n/6\) without rounding. Integrality also covers \(19\le n\le22\):
\[
\begin{array}{c|cccc}
n&19&20&21&22\\ \hline
\left\lceil(4n+3)/5\right\rceil&16&17&18&19\\
\left\lceil5n/6\right\rceil&16&17&18&19.
\end{array}
\]
Therefore a connected counterexample has at least \(23\) vertices.

---

## 3. A dense special case: quadrangulations with a subcubic side

The following is the main self-contained partial result.

### Lemma 3.1: a common-face multigraph

Let \(L\) be a nonempty loopless plane multigraph. Suppose there is a face \(F\) incident with every edge of \(L\). Then \(L\) has a vertex of degree at most two.

#### Proof

Consider a connected component containing an edge and a leaf block \(B\) in its block-cutvertex tree. After deleting everything outside \(B\), the distinguished face becomes a face incident with every edge of \(B\).

If \(B\) is a bridge, its non-cutvertex endpoint has degree one in \(L\). Otherwise \(B\) is 2-connected. In a 2-connected plane multigraph, the boundary of each face is a cycle, allowing a 2-cycle formed by parallel edges. Since every edge of \(B\) is incident with the distinguished face, every edge occurs on that facial cycle. Hence \(B\) itself is a cycle. A vertex of this leaf block that is not a cutvertex has degree two in \(L\). ∎

### Lemma 3.2: the cone lemma

Let \(H\) be a planar bipartite graph with bipartition \((X,Y)\). Suppose

1. every \(x\in X\) has degree at most three, and
2. there is a vertex \(s\in Y\) adjacent to every degree-three vertex of \(X\).

Then \(H\) is 2-degenerate.

#### Proof

Suppose otherwise. Then \(H\) has a subgraph \(K\) of minimum degree at least three. We may assume \(K\) is induced on its vertex set.

Every vertex \(x\in X\cap V(K)\) must have degree exactly three in \(H\), and all three of its neighbors lie in \(K\). In particular, every such \(x\) is adjacent to \(s\), so \(s\in V(K)\).

Take the inherited plane embedding of \(K\) and delete \(s\). All the neighbors of \(s\), hence all vertices of \(X\cap V(K)\), are incident with the face opened by deleting \(s\). Each such \(x\) now has degree two. Suppress all these degree-two vertices. This produces a loopless plane multigraph \(L\) on
\[
(Y\cap V(K))\setminus\{s\}.
\]
Every resulting edge is incident with the face opened at \(s\). Moreover,
\[
d_L(y)=d_K(y)\ge3
\]
for every vertex \(y\) of \(L\). This contradicts Lemma 3.1. Thus \(H\) contains no subgraph of minimum degree three and is 2-degenerate. ∎

### Theorem 3.3: planar bipartite graphs with one subcubic side

Let \(Q\) be a planar bipartite graph with bipartition \((X,Y)\), where
\[
d_Q(x)\le3\qquad\text{for every }x\in X.
\]
Put \(b=|Y|\). If some vertex of \(X\) has degree three, then
\[
\tau(Q)\le \left\lfloor\frac b2\right\rfloor-1.
\tag{9}
\]
If every vertex of \(X\) has degree at most two, then \(Q\) itself is 2-degenerate.

#### Proof

For every degree-three vertex \(x\in X\), perform the local \(Y\)-to-\(\Delta\) operation: remove \(x\) and join its three neighbors pairwise. This operation preserves planarity, although it may produce parallel edges. Performing it successively for all degree-three vertices produces a plane multigraph on \(Y\). Its underlying simple graph \(T\) is planar, and the three neighbors of each degree-three vertex of \(X\) form a triangle in \(T\).

Apply the Four Colour Theorem to \(T\), allowing empty colour classes, and let \(S\) be the union of the two smallest colour classes. Then
\[
|S|\le \left\lfloor\frac b2\right\rfloor.
\tag{10}
\]
Each degree-three neighborhood forms a triangle in \(T\), so its vertices receive three distinct colours. Since the complement of \(S\) uses only two colours, every degree-three vertex \(x\in X\) has at least one neighbor in \(S\).

Choose any \(s\in S\) and put
\[
D=S\setminus\{s\}.
\]
Thus
\[
|D|\le \left\lfloor\frac b2\right\rfloor-1.
\]

Consider \(Q-D\). First peel:

- every vertex of \(X\) having degree at most two in \(Q\), and
- every degree-three vertex of \(X\) having a neighbor in \(D\).

All these vertices have current degree at most two.

Let \(X_0\) be the set of unpeeled vertices of \(X\). Every \(x\in X_0\) has degree three, has no neighbor in \(D\), and has some neighbor in \(S\). Since \(S\setminus D=\{s\}\), every \(x\in X_0\) is adjacent to \(s\).

The remaining graph therefore satisfies Lemma 3.2, with \(X_0\) as its subcubic side and \(s\) as the common neighbor of all its degree-three vertices. It is 2-degenerate. Concatenating the two peeling orders proves that \(Q-D\) is 2-degenerate. ∎

### Corollary 3.4: the \(5/6\) bound for a class of quadrangulations

Let \(Q\) be a connected plane quadrangulation with bipartition \((X,Y)\). If
\[
d_Q(x)\le3\qquad\text{for every }x\in X,
\]
then
\[
\alpha_2(Q)\ge \left\lceil\frac56|V(Q)|\right\rceil.
\tag{11}
\]

#### Proof

Write \(a=|X|\), \(b=|Y|\), and \(n=a+b\). A plane quadrangulation satisfies
\[
m=2n-4.
\]
Since every edge has exactly one endpoint in \(X\),
\[
2(a+b)-4=m=\sum_{x\in X}d(x)\le3a.
\]
Hence
\[
a\ge2b-4,\qquad n\ge3b-4.
\tag{12}
\]

By Theorem 3.3,
\[
\tau(Q)\le \left\lfloor\frac b2\right\rfloor-1,
\]
unless \(Q\) is already 2-degenerate.

If \(b=2k\), then \(n\ge6k-4\), and therefore
\[
\left\lfloor\frac n6\right\rfloor\ge k-1
=\left\lfloor\frac b2\right\rfloor-1.
\]
If \(b=2k+1\), then \(n\ge6k-1\), and again
\[
\left\lfloor\frac n6\right\rfloor\ge k-1
=\left\lfloor\frac b2\right\rfloor-1.
\]
Thus \(\tau(Q)\le\lfloor n/6\rfloor\), proving (11). ∎

A particularly natural subclass is obtained from a simple plane triangulation \(T\): its vertex-face incidence graph is a quadrangulation, and its face-side has degree exactly three. If \(T\) has \(N\) vertices, this incidence graph has \(3N-4\) vertices, and the proof deletes at most
\[
\left\lfloor\frac N2\right\rfloor-1
=
\left\lfloor\frac{3N-4}{6}\right\rfloor
\]
vertices.

---

## 4. Further degree-based special cases

### Proposition 4.1: subcubic graphs satisfy the stronger \(7/8\) bound

If \(G\) is triangle-free, planar, and \(\Delta(G)\le3\), then
\[
\alpha_2(G)\ge\frac78|V(G)|.
\tag{13}
\]

#### Proof

A connected subcubic component that is not cubic is already 2-degenerate. Indeed, a subgraph of minimum degree at least three would have to contain all three neighbors of each of its vertices, making it a whole connected cubic component.

For a connected cubic component \(C\), deleting any one vertex makes \(C\) 2-degenerate by the same argument. Moreover,
\[
\frac32|V(C)|=|E(C)|\le2|V(C)|-4,
\]
so \(|V(C)|\ge8\). Deleting one vertex from each cubic component therefore deletes at most one eighth of all vertices. ∎

The cube shows equality in this special case.

### Proposition 4.2: extreme numbers of low-degree vertices

Let \(t\) denote the number of vertices of degree at most three.

1. From the second theorem quoted in the prompt,
   \[
   t\le\frac n{432}
   \quad\Longrightarrow\quad
   \alpha_2(G)\ge\frac56n,
   \]
   because
   \[
   \frac78n-18t\ge\frac78n-\frac1{24}n=\frac56n.
   \]

2. If \(G\) is connected and \(t\ge5n/6\), then the \(5/6\) bound also holds.

For the second assertion, let \(H\) be the set of vertices of degree at least four. If \(H\neq\varnothing\), then \(G-H\) is 2-degenerate: a subgraph of \(G-H\) of minimum degree three would consist of degree-three vertices having all their neighbors inside that subgraph, and hence would be a component of the connected graph \(G\), disjoint from the nonempty set \(H\). Thus deleting \(H\), of size at most \(n/6\), suffices. If \(H=\varnothing\), Proposition 4.1 applies.

---

## 5. Necessary shape of a counterexample

Combining the preceding results, a vertex-minimal connected counterexample would have the following properties:

- \(n\ge23\);
- minimum degree at least three, since a vertex of degree at most two can always be added to an induced 2-degenerate subgraph;
- at least one 4-cycle;
- \(m>(11n-6)/6\);
- if it is 2-connected, more than \((n+14)/2\) quadrilateral faces;
- if \(t\) is the number of degree-three vertices, then
  \[
  \frac n{432}<t<\frac56n;
  \]
- it is not a quadrangulation having a bipartition class of maximum degree at most three.

For such a minimal counterexample, Euler's inequality also gives
\[
\sum_v(4-d(v))=4n-2m\ge8.
\]
Since its minimum degree is three,
\[
t\ge 8+\sum_{d(v)\ge5}(d(v)-4).
\tag{14}
\]

The unresolved regime is therefore genuinely the dense, predominantly quadrilateral regime in which vertices of degree at least four occur substantially on both sides of the bipartition. The proof of Theorem 3.3 relies on replacing every degree-three neighborhood by a planar triangle and then applying four-colouring. For a degree-four vertex, the analogous operation would require making four boundary neighbors into a \(K_4\); such simultaneous completions need not remain planar. This is the precise point at which the argument above stops.

No proof is given for that remaining regime, and no counterexample is found.