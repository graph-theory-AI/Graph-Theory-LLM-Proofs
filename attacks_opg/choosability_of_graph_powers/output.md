```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "Explicit bounds give subquadratic results for roots of sublinear degeneracy or with subexponential-size blocks, but do not settle the unrestricted question.",
  "would_publish": false,
  "caveats": "These elementary special cases and the logarithmic-gap example are not claimed to be new; no universal subquadratic bound is obtained."
}
```

## 1. A quantitative partial result

All graphs below are finite and simple. Write
\[
k=\chi(G^2),\qquad \Delta=\Delta(G),\qquad d=\operatorname{degeneracy}(G).
\]
Count bridges as two-vertex blocks, and let \(M\) be the maximum number of vertices in a block of \(G\).

The following gives two complementary regimes in which Noel’s question has a positive answer.

**Theorem.** If \(G\) contains an edge, then
\[
\boxed{\quad
\operatorname{ch}(G^2)
\le
\min\left\{
(2d-1)\Delta-d(d-1)+1,\;
\Delta+\left\lceil k\ln M\right\rceil
\right\}.
\quad} \tag{1}
\]

Since \(N_G[v]\) is a clique in \(G^2\), we have \(\Delta\le k-1\). Consequently:

* If \(d=o(k)\), then \(\operatorname{ch}(G^2)=o(k^2)\).
* If \(\ln M=o(k)\), then \(\operatorname{ch}(G^2)=o(k^2)\).
* If \(M\le k^A\), for a fixed constant \(A>0\), then
  \[
  \operatorname{ch}(G^2)\le A k\ln k+k.
  \tag{2}
  \]
  Thus the stronger, conjectured \(O(k\log k)\) estimate holds for roots with polynomial-size blocks, even if the entire graph has arbitrarily many vertices.

The order in (2) is necessary when blocks of quadratic size are allowed; a self-contained example appears in Section 3.

Edgeless nonempty graphs have \(k=\operatorname{ch}(G^2)=1\) and can be handled separately.

## 2. Proof of the upper bounds

### 2.1. The degeneracy bound

Choose an ordering of \(V(G)\) in which every vertex has at most \(d\) later neighbors in \(G\). Fix a vertex \(v\), and let \(p\le d\) be its number of later neighbors in \(G\).

We count vertices later than \(v\) that are adjacent to \(v\) in \(G^2\).

* Direct later neighbors contribute at most \(p\).
* Two-edge paths through a later neighbor of \(v\) contribute at most \(p(\Delta-1)\).
* If a two-edge path \(vwu\) goes through an earlier neighbor \(w\), then \(u\), being later than \(v\), is also later than \(w\). Since \(v\) is one of the at most \(d\) later neighbors of \(w\), there are at most \(d-1\) possible such \(u\).

Hence the number of later neighbors of \(v\) in \(G^2\) is at most
\[
\begin{aligned}
p+p(\Delta-1)+(\deg_G(v)-p)(d-1)
&\le p\Delta+(\Delta-p)(d-1)\\
&\le d\Delta+(\Delta-d)(d-1)\\
&=(2d-1)\Delta-d(d-1).
\end{aligned}
\]
The second inequality uses \(\Delta-d+1>0\).

Greedy list coloring in reverse order therefore gives
\[
\operatorname{ch}(G^2)
\le (2d-1)\Delta-d(d-1)+1.
\tag{3}
\]

Equivalently, the right-hand side is
\[
\Delta^2-(\Delta-d)(\Delta-d+1)+1.
\]
For forests, \(d=1\), and this recovers the exact bound
\(\operatorname{ch}(G^2)=\Delta+1\).

### 2.2. A bounded-order list-coloring lemma

**Lemma.** Every \(k\)-colorable graph \(H\) on \(n\ge1\) vertices satisfies
\[
\operatorname{ch}(H)\le \left\lceil k\ln n\right\rceil+1.
\tag{4}
\]

**Proof.** Fix a proper coloring with color classes \(V_1,\ldots,V_k\), and give each vertex a list of
\[
\ell=\left\lceil k\ln n\right\rceil+1
\]
colors.

Independently assign every color appearing in the lists to one of \(k\) palettes, uniformly at random. A vertex in \(V_i\) has no listed color in palette \(i\) with probability
\[
(1-1/k)^\ell\le e^{-\ell/k}.
\]
The probability that any vertex fails is at most
\[
n e^{-\ell/k}<1.
\]
Thus some palette assignment gives each vertex of \(V_i\) a listed color in palette \(i\). Choosing one such color at every vertex gives a proper coloring. \(\square\)

### 2.3. Localizing the problem to blocks

The useful point is that the bounded-order lemma need only be applied to individual blocks, not to the entire graph.

**Block lemma.** If \(G\) contains an edge, then
\[
\operatorname{ch}(G^2)
\le
\Delta(G)-1+
\max_{B\text{ a block of }G}\operatorname{ch}(B^2).
\tag{5}
\]

**Proof.** Put
\[
b=\max_B\operatorname{ch}(B^2).
\]
In particular, \(b\ge2\). If \(\Delta=1\), the assertion is immediate. Assume \(\Delta\ge2\), and consider lists of size
\[
L=\Delta-1+b.
\]

Work component by component. Root the block-cut tree of a component at a block and process blocks with parents before children. Color the root block first.

A subsequent block \(B\) meets the previously colored part in exactly its parent articulation vertex \(a\). Moreover:

1. every path from \(B-\{a\}\) to the previously colored part passes through \(a\);
2. \(G^2[V(B)]=B^2\), since a path outside \(B\) cannot connect two distinct vertices of \(B\).

Suppose first that \(B\) is not a bridge. Then \(\deg_B(a)\ge2\). For a new vertex \(v\in B-\{a\}\):

* If \(v\) is adjacent to \(a\), its previously colored square-neighbors are among \(a\) and the previously colored neighbors of \(a\). Their number is at most
  \[
  1+\Delta-\deg_B(a)\le\Delta-1.
  \]
* If \(v\) is not adjacent to \(a\), its only possible previously colored square-neighbor is \(a\), again giving at most \(\Delta-1\).

Delete the colors on these previously colored square-neighbors. Every new vertex retains at least \(b\) colors, so \(B^2-\{a\}\) can be list-colored.

If \(B\) is a bridge \(av\), only \(v\) is new. It has at most \(\Delta\) previously colored square-neighbors. Since \(L\ge\Delta+1\), at least one color remains for \(v\).

Continuing in this way colors \(G^2\). \(\square\)

For every block \(B\), the graph \(B^2\) is \(k\)-colorable and has at most \(M\) vertices. Applying (4) and then (5) gives
\[
\operatorname{ch}(G^2)
\le \Delta-1+\left(\left\lceil k\ln M\right\rceil+1\right)
=\Delta+\left\lceil k\ln M\right\rceil.
\]
Together with (3), this proves (1).

## 3. The polynomial-block-size result is order-sharp

Here is a self-contained construction exhibiting
\[
|V(G)|=O(k^2),
\qquad
\chi(G^2)=k,
\qquad
\operatorname{ch}(G^2)=\Omega(k\log k).
\]
This reproduces the logarithmic-gap phenomenon in the question; it does **not** disprove the requested subquadratic bound.

### 3.1. A complete multipartite list lower bound

Let \(K_{r\times r}\) denote the complete \(r\)-partite graph with \(r\) vertices in each part. For all sufficiently large \(r\),
\[
\operatorname{ch}(K_{r\times r})
>
\frac{r\log_2 r}{16}.
\tag{6}
\]

To prove this, set
\[
\ell=\left\lfloor\frac{r\log_2 r}{16}\right\rfloor,
\qquad m=2\ell.
\]
Independently give each vertex a uniformly random \(\ell\)-element list from a common \(m\)-color set.

In a proper coloring, no color can be used in two different parts. Thus any proper list coloring determines a partition
\[
S_1,\ldots,S_r
\]
of the color set such that every list in part \(i\) meets \(S_i\). Unused colors can be assigned arbitrarily to complete the partition.

Fix such a partition. At least \(r/2\) of its sets have size at most \(2m/r\). For one of these sets, of size \(s\), and \(r\ge8\),
\[
\begin{aligned}
\Pr(L(v)\cap S_i=\varnothing)
&=\frac{\binom{m-s}{\ell}}{\binom m\ell}\\
&=\prod_{j=0}^{s-1}\frac{m/2-j}{m-j}\\
&\ge 4^{-s}\\
&\ge 4^{-2m/r}
\ge r^{-1/2}.
\end{aligned}
\]
The product estimate uses \(s\le m/4\).

There are at least \(r^2/2\) vertices in these small-palette parts. Consequently, the probability that this fixed partition meets all their lists is at most
\[
(1-r^{-1/2})^{r^2/2}
\le e^{-r^{3/2}/2}.
\]
There are at most \(r^m\) partitions. Therefore the probability that any partition works is at most
\[
\exp\left(
\frac{r(\ln r)^2}{8\ln2}-\frac{r^{3/2}}2
\right)<1
\]
for all sufficiently large \(r\). Some \(\ell\)-list assignment is therefore uncolorable, proving (6).

### 3.2. A square containing \(K_{q\times q}\)

Let \(q\) be a prime. Construct a bipartite graph \(G_q\) with parts
\[
P=\{(x,y):x,y\in\mathbb F_q\},
\qquad
\mathcal L=\{[a,b]:a,b\in\mathbb F_q\},
\]
where
\[
(x,y)\sim[a,b]\quad\Longleftrightarrow\quad y=ax+b.
\]
Thus \(P\) consists of affine points and \(\mathcal L\) of nonvertical affine lines. The graph has \(2q^2\) vertices and is \(q\)-regular.

Put \(H_q=G_q^2\).

* Two points are adjacent in \(H_q\) exactly when their \(x\)-coordinates differ. Hence
  \[
  H_q[P]\cong K_{q\times q}.
  \]
* Two line vertices are adjacent exactly when their slopes differ.
* Between \(P\) and \(\mathcal L\), the edges of \(H_q\) are precisely the original incidence edges.

Coloring points by \(x\)-coordinate and lines by slope, using disjoint palettes, gives
\[
\chi(H_q)\le2q.
\]

Conversely, an independent set contains points from at most one vertical column and lines from at most one parallel class. Between any such column and parallel class, incidence is a perfect matching. Thus every independent set has size at most \(q\). Since \(H_q\) has \(2q^2\) vertices,
\[
\chi(H_q)\ge2q.
\]
Therefore
\[
\chi(H_q)=2q.
\tag{7}
\]

By (6),
\[
\operatorname{ch}(H_q)
\ge \operatorname{ch}(K_{q\times q})
=\Omega(q\log q).
\]
Writing \(k=2q\), we obtain
\[
|V(G_q)|=\frac{k^2}{2},
\qquad
\operatorname{ch}(G_q^2)=\Omega(k\log k).
\]
Together with (2), this establishes the sharp order \(k\log k\) in the class allowing blocks of order \(O(k^2)\).

## 4. What an unresolved obstruction must look like

The upper bounds impose quantitative conditions on any putative quadratic-gap sequence.

Suppose, for a fixed \(\varepsilon>0\),
\[
\operatorname{ch}(G^2)\ge\varepsilon k^2.
\]
From (1),
\[
\operatorname{ch}(G^2)\le 2d(k-1)+1,
\]
so
\[
d\ge \frac{\varepsilon k^2-1}{2(k-1)}.
\tag{8}
\]
Also,
\[
\operatorname{ch}(G^2)
\le \Delta+\lceil k\ln M\rceil
\le k\ln M+k,
\]
and consequently
\[
M\ge \exp(\varepsilon k-1).
\tag{9}
\]
Thus a quadratic-gap sequence would require both linear-in-\(k\) degeneracy and exponentially large blocks.

There is also a useful normalization showing that regular roots cannot simply be avoided.

**Regular-completion lemma.** Every \(G\) with \(\chi(G^2)=k\ge2\) is a subgraph of a graph \(F\) such that
\[
F\text{ is }(k-1)\text{-regular},
\qquad
\chi(F^2)=k,
\qquad
\operatorname{ch}(G^2)\le\operatorname{ch}(F^2).
\tag{10}
\]

**Proof.** Fix a proper \(k\)-coloring of \(G^2\), with classes \(V_1,\ldots,V_k\). Between any two classes, the edges of \(G\) form a matching: otherwise two vertices of one class would have a common neighbor.

Add isolated vertices to make all classes the same size. For every pair of classes, complete the existing matching to a perfect matching.

The resulting graph \(F\) has exactly one neighbor in every other class at each vertex, so it is \((k-1)\)-regular. The same classes properly color \(F^2\): no vertex has two neighbors in one class. Every closed neighborhood in \(F\) is a \(k\)-clique in \(F^2\), so \(\chi(F^2)=k\). Finally, \(G^2\) is a subgraph of \(F^2\), giving the choice-number inequality. \(\square\)

These \(F\) are finite covers of \(K_k\). In this normalized family, \(d=k-1\), and the degeneracy estimate returns exactly the original quadratic scale. The block-size estimate helps only when the blocks are not too large.

**Remaining gap.** I do not obtain an \(o(k^2)\) estimate for arbitrarily large regular covers of \(K_k\). The small-block palette argument cannot simply be made local: its random variables are colors, and lists at vertices arbitrarily far apart may share those colors. No bounded-dependency argument has been established here. Thus neither Noel’s unrestricted question nor its \(O(k\log k)\) strengthening is settled by these results.