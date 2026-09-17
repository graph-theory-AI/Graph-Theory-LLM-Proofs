```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "An all-girth sparsification bound proves the conjectured conclusion under a polynomial maximum-degree restriction.",
  "would_publish": false,
  "caveats": "The unrestricted conjecture is not settled, and novelty of the partial bound is not claimed."
}
```

## 1. A quantitative partial result

All graphs below are finite and simple; forests have infinite girth. Write \(\log\) for the natural logarithm.

The unrestricted case \(g\ge 5\) is not resolved here. The following maximum-degree-sensitive bound gives a precise partial result.

**Theorem.** Let \(g\ge4\), and let \(G\) have maximum degree \(\Delta\ge1\). Set
\[
a=\frac{g-3}{g-2},
\qquad
d=\left\lceil 32\Delta^a\log(16\Delta)\right\rceil.
\]
Then \(G\) has a spanning subgraph \(H\) of girth at least \(g\) such that every independent set \(I\) of \(H\) induces a \(d\)-colorable graph \(G[I]\). Consequently,
\[
\boxed{\displaystyle
\chi_f(H)\ge
\frac{\chi_f(G)}
{\left\lceil32\Delta^{(g-3)/(g-2)}\log(16\Delta)\right\rceil}.}
\tag{1}
\]

In particular, fix \(C\ge1\) and
\[
1\le q<\frac{g-2}{g-3}.
\]
The conjectured conclusion holds, for every \(x\), on the class of graphs satisfying
\[
\Delta(G)\le C\chi_f(G)^q.
\tag{2}
\]

For example, when \(\Delta(G)\le C\chi_f(G)\), the theorem produces
\[
\chi_f(H)
=\Omega_{C,g}\!\left(
\frac{\chi_f(G)^{1/(g-2)}}{\log\chi_f(G)}
\right)
\]
as \(\chi_f(G)\to\infty\).

## 2. Proof of the sparsification theorem

The key is not to preserve the original independent sets exactly. Instead, we ensure that every *new* independent set can be partitioned into at most \(d\) original independent sets.

### 2.1. Counting connected vertex sets

For any vertex \(v\), the number of connected \(s\)-vertex sets containing \(v\) is at most
\[
(4\Delta)^{s-1}.
\tag{3}
\]

Indeed, every such set has a spanning tree rooted at \(v\). There are at most \(4^{s-1}\) rooted plane tree shapes on \(s\) vertices. For a fixed shape, mapping its root to \(v\) and each child to a neighbor of its parent gives at most \(\Delta^{s-1}\) maps. This overcounts, which is harmless.

Also, a fixed edge belongs to at most
\[
\Delta^{\ell-2}
\tag{4}
\]
cycles of length \(\ell\): specify the \(\ell-2\) internal vertices of the complementary path between its endpoints.

### 2.2. Random sampling and bad events

Put
\[
p=\frac18\Delta^{-a}.
\]
Retain each edge of \(G\) independently with probability \(p\), obtaining a random spanning subgraph \(F\). Notice that
\[
d=\left\lceil\frac4p\log(16\Delta)\right\rceil,
\qquad d\ge2,
\qquad p\Delta\ge\frac18.
\tag{5}
\]

We exclude two families of bad events.

* For every cycle \(C\) with \(3\le |C|<g\), let \(A_C\) be the event that all its edges are retained.
* For every vertex set \(U\) such that \(G[U]\) is connected and
  \(\delta(G[U])\ge d\), let \(B_U\) be the event that no edge of \(G[U]\) is retained.

Write \(m_U=|E(G[U])|\). Assign the local-lemma parameters
\[
z_C=(2p)^{|C|},
\qquad
z_U=\exp(-pm_U/2).
\tag{6}
\]

Use the dependency graph in which two bad events are adjacent if their sets of edge variables intersect. We will verify the asymmetric Lovász local lemma.

### 2.3. Bounding the load on one edge

Fix an edge \(e\).

First consider cycle events. For \(3\le\ell\le g-1\),
\[
\ell-2-a(\ell-1)
=\frac{\ell-g+1}{g-2}\le0.
\]
Consequently, by (4),
\[
\begin{aligned}
\sum_{C:\,e\in E(C)}z_C
&\le \sum_{\ell=3}^{g-1}\Delta^{\ell-2}(2p)^\ell\\
&\le p\sum_{\ell=3}^{\infty}\frac{2^\ell}{8^{\ell-1}}
=\frac p6.
\end{aligned}
\tag{7}
\]

Next consider the events \(B_U\). If \(s=|U|\), then
\[
s\ge d+1,\qquad m_U\ge \frac{ds}{2}.
\]
By the definition of \(d\),
\[
z_U
\le \exp(-pds/4)
\le (16\Delta)^{-s}.
\]
Using (3), with either endpoint of \(e\) as the specified vertex,
\[
\begin{aligned}
\sum_{U:\,e\in E(G[U])}z_U
&\le
\sum_{s=d+1}^{\infty}
(4\Delta)^{s-1}(16\Delta)^{-s}\\
&=\frac{1}{12\Delta\,4^d}\\
&\le\frac{1}{192\Delta}
\le\frac p{24}.
\end{aligned}
\tag{8}
\]

Thus the total parameter load on any edge is at most
\[
\frac p6+\frac p{24}=\frac{5p}{24}<\frac p4.
\tag{9}
\]

### 2.4. Verifying the local lemma

All the parameters in (6) are at most \(1/2\). For cycle events this follows from \(p\le1/8\); for \(B_U\) it follows from \(z_U\le(16\Delta)^{-|U|}\).

Suppose a bad event \(E\) depends on \(m\) edge variables. Equation (9) gives
\[
\sum_{E'\sim E}z_{E'}\le \frac{mp}{4}.
\]
Using \(1-z\ge e^{-2z}\) for \(0\le z\le1/2\), we obtain
\[
\prod_{E'\sim E}(1-z_{E'})
\ge \exp(-mp/2).
\tag{10}
\]

For a cycle \(C\) of length \(\ell\),
\[
\Pr(A_C)=p^\ell
\le (2p)^\ell e^{-p\ell/2}
\le z_C\prod_{E'\sim A_C}(1-z_{E'}),
\]
where the first inequality holds because \(2e^{-p/2}>1\).

For a set \(U\),
\[
\Pr(B_U)=(1-p)^{m_U}
\le e^{-pm_U}
=z_Ue^{-pm_U/2}
\le z_U\prod_{E'\sim B_U}(1-z_{E'}).
\]

These are precisely the asymmetric local-lemma inequalities. Therefore there is an outcome \(H\) in which none of the bad events occurs.

No \(A_C\) occurs, so \(H\) has girth at least \(g\).

### 2.5. Controlling independent sets and fractional colorings

Let \(I\) be independent in \(H\). I claim that \(G[I]\) is \((d-1)\)-degenerate.

Otherwise, some induced subgraph of \(G[I]\) has minimum degree at least \(d\). Taking a connected component gives a set \(U\subseteq I\) for which \(G[U]\) is connected and has minimum degree at least \(d\). Since \(I\) is independent in \(H\), no edge of \(G[U]\) was retained. Thus \(B_U\) occurs, a contradiction.

Hence \(G[I]\) is \(d\)-colorable.

Now take a fractional coloring of \(H\). For each independent set \(I\) receiving weight \(\lambda_I\), partition \(I\) into at most \(d\) independent sets of \(G\), and give each part weight \(\lambda_I\). Every vertex retains its original total coverage, while total coloring weight increases by at most a factor \(d\). Therefore
\[
\chi_f(G)\le d\,\chi_f(H),
\]
which proves (1). \(\square\)

## 3. The resulting restricted version of the conjecture

Here is the maximum-degree restriction with all quantifiers explicit.

**Corollary.** Fix \(g\ge4\), \(C\ge1\), and
\[
1\le q<\frac{g-2}{g-3}.
\]
For every \(x\ge1\), there exists \(k_{C,q}(x,g)\) such that every graph \(G\) satisfying
\[
\chi_f(G)\ge k_{C,q}(x,g),
\qquad
\Delta(G)\le C\chi_f(G)^q
\]
contains a subgraph of girth at least \(g\) and fractional chromatic number at least \(x\).

**Proof.** Write
\[
K=\chi_f(G),\qquad
a=\frac{g-3}{g-2},\qquad
\varepsilon=1-qa>0.
\]
The theorem and the degree hypothesis give
\[
\chi_f(H)
\ge
\frac{K^\varepsilon}
{32C^a\bigl(\log(16C)+q\log K\bigr)+1}.
\tag{11}
\]
The right-hand side tends to infinity with \(K\).

An explicit, deliberately loose threshold is available. Set
\[
B=
32C^a\left(\log(16C)+\frac{2q}{\varepsilon}\right)+1.
\]
For \(K\ge1\), the inequality
\[
\log K\le \frac{2}{\varepsilon}K^{\varepsilon/2}
\]
shows that (11) is at least \(K^{\varepsilon/2}/B\). Thus one may take
\[
\boxed{\displaystyle
k_{C,q}(x,g)=(Bx)^{2/\varepsilon}.}
\]
\(\square\)

For the first case not covered by the supplied triangle-free theorem, \(g=5\), this proves the desired conclusion whenever
\[
\Delta(G)\le C\chi_f(G)^q
\quad\text{for a fixed }q<\frac32.
\]

## 4. What remains unresolved

The unrestricted conjecture has no upper bound on \(\Delta(G)\) in terms of \(\chi_f(G)\). In that regime, the denominator in (1) can overwhelm the numerator, and the bound gives no growing fractional chromatic number.

The argument also does **not** establish that an arbitrary graph of large fractional chromatic number has a subgraph retaining large fractional chromatic number while satisfying the required maximum-degree restriction. Such an extraction would be an additional substantive step, not a consequence proved here.

Thus the result is an all-girth, maximum-degree-dependent partial bound—not a proof or disproof of Conjecture 4.