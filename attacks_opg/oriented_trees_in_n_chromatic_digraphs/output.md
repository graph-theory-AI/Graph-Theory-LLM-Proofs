```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "Burr’s bound holds for all oriented trees of diameter at most three, with the sharp family-wide threshold 2k-4 for genuine antidirected double-stars.",
  "would_publish": false,
  "caveats": "The general conjecture is not resolved here; novelty of these self-contained special-case arguments is not claimed."
}
```

# A partial result: all orientations of double-stars

I obtain a self-contained special-case result, rather than a proof of the full conjecture. The argument gives somewhat more than the conjectured bound for this family.

Throughout, chromatic number means the chromatic number of the underlying undirected graph. Copies are not required to be induced. A **genuine double-star** is a tree of diameter exactly three: its two non-leaf vertices are adjacent.

## Theorem

Let \(T\) be an oriented tree of order \(k\ge 2\).

1. If the underlying tree has diameter at most three, then every digraph of chromatic number at least \(2k-2\) contains \(T\).
2. In fact, unless \(T\) is a pure in-star or a pure out-star, chromatic number at least \(2k-3\) suffices for this family.
3. If \(T\) is a genuine antidirected double-star, then minimum underlying degree at least \(2k-5\) suffices. Consequently, chromatic number at least \(2k-4\) suffices. Both thresholds in this last statement are best possible uniformly over genuine antidirected double-stars of order \(k\).

I do not claim priority for these special cases.

We may work with oriented graphs: from a digraph containing opposite arcs, retain one direction on each adjacent pair. This preserves the underlying graph, and a copy found in the resulting oriented graph is also a copy in the original digraph.

---

## 1. Preliminary facts and oriented stars

We use three elementary observations.

### Bounded one-sided degree

If an oriented graph \(D\) satisfies \(d^+(v)\le r\) for every vertex, then
\[
\chi(D)\le 2r+1.
\]
Indeed, every induced subgraph \(F\) has at most \(r|V(F)|\) arcs, so its underlying graph has average degree at most \(2r\). Thus the underlying graph is \(2r\)-degenerate. The same statement holds with in-degree in place of out-degree.

### Critical subgraphs

If \(\chi(D)\ge r\), there is an induced subdigraph \(H\) with
\[
\chi(H)=r,\qquad \delta(G(H))\ge r-1.
\]
Choose an induced subdigraph minimal subject to having chromatic number at least \(r\), and apply the usual vertex-deletion coloring argument.

### Allocating leaves from two sets

Finite sets \(X,Y\) contain disjoint subsets of sizes \(p,q\), respectively, if and only if
\[
|X|\ge p,\qquad |Y|\ge q,\qquad |X\cup Y|\ge p+q.
\tag{1}
\]
This is the two-set instance of Hall’s theorem.

### Stars

A pure out-star with \(k-1\) leaves is forced by chromatic number \(2k-2\): otherwise every vertex has out-degree at most \(k-2\), giving \(\chi(D)\le 2k-3\). Reverse all arcs for in-stars.

Now let a mixed star have \(a\ge1\) incoming leaves and \(b\ge1\) outgoing leaves, where \(a+b=k-1\). If it is absent, every vertex has either in-degree at most \(a-1\) or out-degree at most \(b-1\). Partitioning accordingly gives
\[
\chi(D)\le (2a-1)+(2b-1)=2k-4.
\]
Hence every mixed star is \((2k-3)\)-universal.

---

## 2. An auxiliary bound for outward double-stars

Let \(B_{p,q}\), where \(p,q\ge1\), consist of an arc \(x\to y\), together with \(p\) additional leaves dominated by \(x\) and \(q\) leaves dominated by \(y\).

### Lemma 1
Every oriented graph of chromatic number at least
\[
2(p+q)
\]
contains \(B_{p,q}\).

Thus these \(k=p+q+2\)-vertex trees are \((2k-4)\)-universal. The same holds after reversing every arc.

### Proof

Write \(m=p+q\), and suppose that \(D\) is \(B_{p,q}\)-free.

#### Case 1: \(q\ge2\)

First,
\[
A=\{v:d_D^+(v)\ge m\}
\]
is independent. Otherwise, for an arc \(x\to y\) inside \(A\), put
\[
X=N^+(x)\setminus\{y\},\qquad Y=N^+(y).
\]
Both sets avoid the two centers, and
\[
|X|\ge m-1\ge p,\qquad |Y|\ge m\ge q,\qquad |X\cup Y|\ge m.
\]
By (1), the required leaves can be chosen.

We also claim that every oriented graph of minimum out-degree at least \(m-1\) contains \(B_{p,q}\). If not, then for every arc \(x\to y\), the same two sets satisfy
\[
|X|\ge m-2\ge p,\qquad |Y|\ge m-1\ge q.
\]
Their union must therefore have size at most \(m-1\). Since \(|Y|\ge m-1\), this implies
\[
N^+(x)\setminus\{y\}\subseteq N^+(y).
\tag{2}
\]
Choose two distinct out-neighbors \(y,z\) of \(x\), which is possible because \(m-1\ge2\). Applying (2) to \(x\to y\) and \(x\to z\) forces both \(y\to z\) and \(z\to y\), a contradiction.

Set \(C=V(D)\setminus A\). Every vertex of \(D[C]\) has out-degree at most \(m-1\). If
\(\chi(D[C])\ge2m-1\), take a \((2m-1)\)-critical induced subdigraph \(F\) of \(D[C]\). Then
\[
\delta(G(F))\ge2m-2,\qquad d_F^+(v)\le m-1.
\]
Summing degrees shows that equality holds throughout:
\[
|A(F)|=(m-1)|V(F)|,\qquad d_F^+(v)=m-1
\]
for every \(v\). The preceding claim embeds \(B_{p,q}\) in \(F\), a contradiction.

Consequently,
\[
\chi(D)\le \chi(D[C])+1\le2m-1.
\]

#### Case 2: \(q=1\)

Here \(p=m-1\). Absence of \(B_{m-1,1}\) imposes the following restrictions.

- If \(d^+(x)=m\), then \(N^+(x)\) is outgoing-closed: no arc leaves this set. Otherwise, an arc \(y\to z\) with \(y\in N^+(x)\) and \(z\notin N^+(x)\) supplies the subdivided arm, while the other \(m-1\) out-neighbors of \(x\) supply its direct leaves.
- If \(d^+(x)>m\), all out-neighbors of \(x\) are sinks. Indeed, any arc \(y\to z\) from an out-neighbor allows us to choose \(m-1\) further out-neighbors of \(x\), avoiding \(y,z\).

In particular, every vertex of out-degree at least \(m\) lies in a singleton strongly connected component.

We now properly color \(D\) with \(2m-1\) colors. Give all sinks color \(1\), and process the remaining strongly connected components in reverse topological order.

A singleton component whose vertex has out-degree \(m\) sees at most \(m<2m-1\) colors on already colored neighbors. A singleton of larger out-degree has only sinks as out-neighbors, all colored \(1\). Either can be colored.

Consider any other component \(Q\). Every vertex of \(Q\) has total out-degree at most \(m-1\). Let \(t(v)\) be the number of out-neighbors of \(v\) outside \(Q\). All these vertices are already colored, and no other neighbors outside \(Q\) are already colored. Thus the available-color list \(L(v)\) satisfies
\[
|L(v)|\ge2m-1-t(v).
\]
For every nonempty \(U\subseteq V(Q)\),
\[
\begin{aligned}
\sum_{v\in U}d_{G(D[U])}(v)
&=2|A(D[U])|\\
&\le 2\sum_{v\in U}(m-1-t(v))\\
&<\sum_{v\in U}(2m-1-t(v))\\
&\le\sum_{v\in U}|L(v)|.
\end{aligned}
\]
Therefore every such \(U\) contains a vertex whose degree in \(D[U]\) is smaller than its list size. Successive deletion and reverse greedy coloring properly color \(Q\) from these lists.

This completes a \((2m-1)\)-coloring of \(D\). Hence \(\chi(D)\ge2m\) forces \(B_{p,q}\). ∎

---

## 3. Antidirected double-stars: a sharp minimum-degree result

Let \(A_{p,q}\), with \(p,q\ge1\), consist of an arc \(x\to y\), \(p\) additional leaves dominated by \(x\), and \(q\) additional leaves dominating \(y\). Put
\[
m=p+q,\qquad k=m+2.
\]

We first locate a suitable central arc.

### Lemma 2
Every nonempty oriented graph with minimum underlying degree at least \(2r-1\) has an arc \(x\to y\) such that
\[
d^+(x)\ge r,\qquad d^-(y)\ge r.
\]

### Proof

Let
\[
X=\{v:d^+(v)\ge r\},\qquad Y=\{v:d^-(v)\ge r\}.
\]
The degree hypothesis gives \(X\cup Y=V(D)\). Also \(X\ne\varnothing\), since the average out-degree is at least \(r-\tfrac12\).

Suppose there is no arc from \(X\) to \(Y\). Every out-neighbor of a vertex in \(X\) then belongs to \(V(D)\setminus Y\subseteq X\). Hence
\[
|A(D[X])|\ge r|X|.
\]
On the other hand, all targets of these arcs have in-degree at most \(r-1\), so
\[
|A(D[X])|\le(r-1)|X|,
\]
a contradiction. ∎

### Lemma 3
If
\[
\delta(G(D))\ge2m-1,
\]
then \(D\) contains \(A_{p,q}\).

### Proof

Suppose otherwise. By Lemma 2, choose an arc \(x\to y\) with
\[
d^+(x)\ge m,\qquad d^-(y)\ge m.
\]
Set
\[
X=N^+(x)\setminus\{y\},\qquad
Y=N^-(y)\setminus\{x\}.
\]
Since \(p,q\ge1\), both sets have size at least \(m-1\ge\max\{p,q\}\). If their union has size at least \(m\), condition (1) embeds \(A_{p,q}\). Thus absence of the tree forces
\[
X=Y=S,\qquad |S|=m-1.
\tag{3}
\]
This conclusion applies to every arc whose tail has out-degree at least \(m\) and whose head has in-degree at least \(m\).

Choose \(z\in S\). We have \(x\to z\to y\), and the degree hypothesis gives either \(d^+(z)\ge m\) or \(d^-(z)\ge m\).

- If \(d^+(z)\ge m\), apply (3) to \(z\to y\). It gives
  \[
  N^+(z)\setminus\{y\}=N^-(y)\setminus\{z\}.
  \]
  The right-hand side contains \(x\), forcing \(z\to x\), contrary to \(x\to z\).

- If \(d^-(z)\ge m\), apply (3) to \(x\to z\). It gives
  \[
  N^+(x)\setminus\{z\}=N^-(z)\setminus\{x\}.
  \]
  The left-hand side contains \(y\), forcing \(y\to z\), contrary to \(z\to y\).

Both possibilities are impossible. ∎

Since \(2m-1=2k-5\), this proves the asserted minimum-degree bound. Passing to a \((2k-4)\)-critical induced subdigraph proves the chromatic bound \(2k-4\).

---

## 4. Arbitrary orientations of genuine double-stars

Let the central edge be oriented \(u\to v\). Describe the remaining arcs by four nonnegative integers:

- \(a\) leaves dominate \(u\);
- \(u\) dominates \(b\) leaves;
- \(c\) leaves dominate \(v\);
- \(v\) dominates \(d\) leaves.

Thus
\[
a+b+c+d=m=k-2,
\qquad a+b\ge1,\quad c+d\ge1.
\tag{4}
\]

If \(a=d=0\), the tree is antidirected and Section 3 applies. Assume henceforth that
\[
a+d>0.
\tag{5}
\]

We prove that \(\chi(D)\ge2m+1=2k-3\) suffices. Take an induced subdigraph \(H\) with
\[
\chi(H)=2m+1,\qquad \delta(G(H))\ge2m.
\]

Define degree thresholds
\[
h_+=
\begin{cases}
m,&a>0,\\
m+1,&a=0,
\end{cases}
\qquad
h_-=
\begin{cases}
m,&d>0,\\
m+1,&d=0.
\end{cases}
\]
By (5), \(h_++h_-\le2m+1\). Partition
\[
P=\{x:d_H^+(x)\ge h_+\},\qquad Q=V(H)\setminus P.
\]
Every vertex in \(Q\) has in-degree at least \(h_-\).

### The two pruned trees

Let \(T_{\mathrm{in}}\) be obtained from \(T\) by deleting its \(b+d\) outgoing leaves. It consists of \(u\to v\), the \(a\) leaves entering \(u\), and the \(c\) leaves entering \(v\).

The star bounds and Lemma 1 show that \(T_{\mathrm{in}}\) is \(\alpha\)-universal, where
\[
\alpha=
\begin{cases}
2c+2,&a=0,\\
2a+1,&a>0,\ c=0,\\
2(a+c),&a>0,\ c>0.
\end{cases}
\tag{6}
\]
The last case is the reversal of \(B_{c,a}\).

Likewise, delete the \(a+c\) incoming leaves to obtain \(T_{\mathrm{out}}\). It is \(\beta\)-universal, where
\[
\beta=
\begin{cases}
2b+2,&d=0,\\
2d+1,&d>0,\ b=0,\\
2(b+d),&d>0,\ b>0.
\end{cases}
\tag{7}
\]

### Extending the pruned embeddings

If \(\chi(H[P])\ge\alpha\), embed \(T_{\mathrm{in}}\) inside \(P\), then attach the deleted outgoing leaves greedily in \(H\).

Why are the available out-degrees sufficient?

- If \(a=0\), both centers have out-degree at least \(m+1=k-1\), which suffices for unrestricted greedy leaf attachment.
- If \(a>0\), both centers already have an embedded in-neighbor: \(u\) has one of its \(a\) incoming leaves, and \(v\) has \(u\). Before attaching any remaining leaf, at most \(k-1\) vertices are used. At most \(k-3\) of them can be out-neighbors of its parent, because the parent itself and its fixed in-neighbor are excluded. Out-degree at least \(m=k-2\) therefore suffices.

Symmetrically, if \(\chi(H[Q])\ge\beta\), embed \(T_{\mathrm{out}}\) inside \(Q\), then attach the incoming leaves. When \(d>0\), both centers already have an embedded out-neighbor; when \(d=0\), the stronger in-degree threshold \(k-1\) is available.

Thus, if \(H\) contains no \(T\),
\[
\chi(H[P])\le\alpha-1,\qquad
\chi(H[Q])\le\beta-1.
\tag{8}
\]

### The coloring budget

Equations (4)–(7) give
\[
\alpha+\beta\le2m+2.
\tag{9}
\]
Here are all cases:

- If \(a,d>0\), then
  \[
  \alpha\le2(a+c)+1,\qquad \beta\le2(b+d)+1.
  \]
- If \(a=0\), then \(b,d>0\), so
  \[
  \alpha=2c+2,\qquad \beta=2(b+d).
  \]
- If \(d=0\), then \(a,c>0\), so
  \[
  \alpha=2(a+c),\qquad \beta=2b+2.
  \]

Combining (8) and (9),
\[
\chi(H)
\le\chi(H[P])+\chi(H[Q])
\le\alpha+\beta-2
\le2m,
\]
contrary to \(\chi(H)=2m+1\).

Therefore every orientation of a genuine double-star is \((2k-3)\)-universal. Together with the star argument, this proves parts 1 and 2 of the theorem.

---

## 5. Sharpness

For each \(k\ge4\), consider the antidirected double-star \(A_{k-3,1}\). Its source center has out-degree \(k-2\).

A regular tournament on \(2k-5\) vertices has every out-degree equal to \(k-3\), so it avoids this tree. Its chromatic number and minimum underlying degree are
\[
2k-5,\qquad 2k-6,
\]
respectively. Thus the thresholds \(2k-4\) and \(2k-5\) from Section 3 cannot be lowered uniformly over genuine antidirected double-stars.

For completeness, such a tournament is explicit: use vertices
\(\mathbb Z_{2k-5}\), with
\[
i\to j
\quad\Longleftrightarrow\quad
j-i\pmod{2k-5}\in\{1,\ldots,k-3\}.
\]

The mixed-star bound is also exact. For a star with \(a,b\ge1\), take regular tournaments on \(2a-1\) and \(2b-1\) vertices and orient every cross-edge from the first to the second. Vertices in the first part have in-degree \(a-1\), while vertices in the second have out-degree \(b-1\). This tournament, of order \(2k-4\), avoids the mixed star.

Pure stars retain the original sharp threshold \(2k-2\).

---

## What remains unresolved

This does **not** establish Burr’s conjecture for arbitrary trees, nor does it improve the supplied general subquadratic bound.

The proof exploits the two-center structure. After deleting incoming or outgoing leaves, the remaining trees are stars or the explicitly handled two-level outward trees and their reversals. With three or more non-leaf vertices, these pruned trees need not have those forms, and the necessary coloring-budget inequality is not supplied by the argument.

Thus the full conjecture remains unresolved here. The contribution is a complete special-case proof, including a sharp threshold for the family of genuine antidirected double-stars, without a claim of literature novelty.