```json
{
  "verdict": "proved",
  "confidence": "high",
  "one_line": "A random-composition fractional tiling, rounded by edge-colouring and a reservoir, proves M_k(n)=nk+o(k) for every fixed n.",
  "would_publish": true,
  "caveats": "Uses the classical Pippenger–Spencer edge-colouring theorem; no explicit convergence rate is obtained."
}
```

# Theorem

For every fixed positive integer \(n\),
\[
M_k(n)=nk+o(k)\qquad(k\to\infty).
\]

Here a translate of the progression with difference \(d\) is written
\[
A(d,a)=\{a,a+d,\ldots,a+(n-1)d\}.
\]
Thus \(M_k(n)\) is the least \(m\) such that one can choose pairwise disjoint sets \(A(d,a_d)\subseteq[m]\), one for every \(d\in[k]\).

The missing ingredient in the supplied attempt is an appropriate non-uniform fractional packing. Such a fractional packing can be constructed **exactly**, using a random composition of an integer. After a slight enlargement and removal of the smallest differences, its weights satisfy the hypotheses needed for rounding.

The case \(n=1\) is immediate, so below \(n\ge2\) is fixed.

## 1. An exact fractional packing from random compositions

We first construct fractional packings on the optimal number of points.

### Lemma 1

For every positive integer \(K\), there are nonnegative weights
\[
u_{d,a},
\qquad
1\le d\le K,\quad 1\le a\le nK-(n-1)d,
\]
with the following properties:

1. For every \(d\in[K]\),
   \[
   \sum_a u_{d,a}=1.
   \tag{1}
   \]

2. For every \(x\in[nK]\),
   \[
   \sum_{\substack{d,a\\x\in A(d,a)}}u_{d,a}=1.
   \tag{2}
   \]

3. For every \(d,a\),
   \[
   u_{d,a}\le \frac1d.
   \tag{3}
   \]

4. If \(k<K\le2k\), then, for every \(x\in[nK]\),
   \[
   \sum_{\substack{d\le k,\ a\\x\in A(d,a)}}u_{d,a}
   \le 1-\frac{K-k}{2K}.
   \tag{4}
   \]

### Proof

Generate a random composition of \(K\) as follows. When the remaining sum is \(r>0\), choose the next part uniformly from \(\{1,\ldots,r\}\), subtract it, and continue.

Let \(C_d(K)\) be the number of parts of size \(d\). We claim that
\[
\mathbb E C_d(K)=\frac1d
\qquad(1\le d\le K).
\tag{5}
\]
Indeed, writing \(f_r=\mathbb E C_d(r)\), we have \(f_r=0\) for \(r<d\), while, for \(r\ge d\),
\[
f_r=\frac1r+\frac1r\sum_{s=0}^{r-1}f_s.
\]
Induction gives
\[
f_r=\frac1r+\frac{r-d}{rd}=\frac1d.
\]

Suppose the generated composition is
\[
K=d_1+\cdots+d_\ell.
\]
Partition \([nK]\), from left to right, into consecutive blocks of lengths
\[
nd_1,\ldots,nd_\ell.
\]
A block of length \(nd\), beginning immediately after position \(b\), is tiled by the following \(d\) disjoint progressions:
\[
A(d,b+t)=\{b+t,b+t+d,\ldots,b+t+(n-1)d\},
\qquad 1\le t\le d.
\]
Thus the composition produces a tiling of \([nK]\) by \(n\)-term arithmetic progressions. It contains exactly \(dC_d(K)\) tiles of difference \(d\).

Finally, independently with probability \(1/2\), reflect the entire tiling by
\[
x\longmapsto nK+1-x.
\]
Reflection preserves every tile's difference.

Define \(u_{d,a}\) to be the probability that \(A(d,a)\) is a tile in the resulting random tiling. Equation (5) gives
\[
\sum_a u_{d,a}
=\mathbb E[dC_d(K)]
=1,
\]
proving (1). Every outcome tiles every point exactly once, proving (2).

The appearance of a particular tile of difference \(d\) requires \(C_d(K)\ge1\). Hence
\[
u_{d,a}\le\mathbb P(C_d(K)\ge1)
\le\mathbb E C_d(K)=\frac1d,
\]
which proves (3).

It remains to prove (4). The first part \(U\) of the composition is uniform on \([K]\). If \(U>k\), the first block has length
\[
nU\ge n(k+1)>\frac{nK}{2}.
\]
Consequently:

- for a point in the left half of \([nK]\), the event “no reflection and \(U>k\)” guarantees that it lies in a tile of difference greater than \(k\);
- for a point in the right half, the event “reflection and \(U>k\)” gives the same guarantee.

Each event has probability
\[
\frac12\frac{K-k}{K}.
\]
Thus, at every point, the total weight belonging to differences greater than \(k\) is at least \((K-k)/(2K)\). Subtracting this from (2) proves (4). ∎

The cancellation behind the construction is worth emphasizing: a part of size \(d\) occurs an expected \(1/d\) times and contributes exactly \(d\) tiles of difference \(d\).

## 2. The edge-colouring input

We use the following established consequence of the Pippenger–Spencer asymptotic edge-colouring theorem.

> **Edge-colouring theorem.** Fix \(r\ge2\). If \(H\) is an \(r\)-uniform hypergraph with maximum degree \(\Delta\to\infty\) and maximum pair-codegree \(o(\Delta)\), then
> \[
> \chi'(H)\le(1+o(1))\Delta.
> \tag{6}
> \]
> Equivalently, its edges can be partitioned into at most \((1+o(1))\Delta\) matchings.

For completeness, the standard regular form of the theorem implies precisely this maximum-degree formulation. Here is a regularization that avoids any hidden almost-regularity assumption.

Choose a prime \(p>\max\{r,\Delta\}\), and take copies of \(H\) indexed by
\[
(i,b)\in\{0,\ldots,r-1\}\times\mathbb F_p.
\]
Write a copied vertex as \((v,i,b)\). For every \(v\in V(H)\), choose a set
\[
S_v\subseteq\mathbb F_p,
\qquad |S_v|=\Delta-\deg_H(v).
\]
For each \(s\in S_v\) and \(b\in\mathbb F_p\), add the edge
\[
\{(v,i,b+is):0\le i<r\}.
\tag{7}
\]
Every copied vertex now has degree exactly \(\Delta\). Two vertices with different original identities acquire no additional common edge. Two distinct copies of the same original vertex lie together in at most one added edge: their two coordinates determine \(s\) and \(b\) uniquely. Thus the new hypergraph is simple, \(\Delta\)-regular, and has maximum pair-codegree at most
\[
\max\{\Delta_2(H),1\}.
\]
Apply the regular Pippenger–Spencer theorem and restrict its edge-colouring to one original copy of \(H\). This gives (6).

## 3. Rounding a spread fractional packing with slack

The reservoir argument suggested in the supplied attempt is valid. We give the needed weighted version, including the concentration and codegree checks.

### Lemma 2

Fix \(n\ge2\) and constants \(\alpha,C>0\), \(0<\delta<1\). Let \(S\subseteq[k]\), let \(m=O(k)\), and put
\[
L_d=m-(n-1)d.
\]
Suppose \(L_d\ge\alpha k\) for every \(d\in S\), and suppose there are nonnegative weights \(w_{d,a}\) on all admissible translates \(A(d,a)\subseteq[m]\), \(d\in S\), satisfying
\[
\sum_{a=1}^{L_d}w_{d,a}=1
\qquad(d\in S),
\tag{8}
\]
\[
w_{d,a}\le\frac Ck,
\tag{9}
\]
and
\[
\sum_{\substack{d\in S,\ a\\x\in A(d,a)}}w_{d,a}
\le1-\delta
\qquad(x\in[m]).
\tag{10}
\]
Then, for all sufficiently large \(k\), all the differences in \(S\) can be packed in \([m]\).

All asymptotic statements here keep \(n,\alpha,C,\delta\) and the constant in \(m=O(k)\) fixed.

### Proof

We may assume \(S\ne\varnothing\).

Choose a constant
\[
0<\rho<\delta,
\qquad \sigma=1-\rho.
\]
Independently put each point of \([m]\) into a reservoir \(R\) with probability \(\rho\), and let \(W=[m]\setminus R\).

Set
\[
D_0=\frac{k}{2C}.
\]
Independently for every admissible labelled progression, retain it with probability
\[
p_{d,a}=D_0w_{d,a}\le\frac12.
\]

Form an \((n+1)\)-uniform hypergraph \(H\) with:

- one formal label vertex for every \(d\in S\);
- the point vertices of \(W\);

and with an edge
\[
\{d\}\cup A(d,a)
\]
whenever \(A(d,a)\) was retained and is wholly contained in \(W\).

Let
\[
D=D_0\sigma^n.
\]
For every label \(d\), equation (8) gives
\[
\mathbb E\deg_H(d)=D_0\sigma^n=D.
\tag{11}
\]
For every point \(x\), conditional on \(x\in W\), equation (10) gives
\[
\mathbb E[\deg_H(x)\mid x\in W]
\le D_0\sigma^{n-1}(1-\delta)
=D\frac{1-\delta}{\sigma}.
\tag{12}
\]
Since \(\rho<\delta\), the last ratio is strictly less than \(1\).

We verify the bounded-codegree and concentration facts used below.

For a label \(d\) and a point \(x\), there are at most \(n\) candidate edges containing both. For two point vertices \(x<y\), a candidate edge containing both must satisfy
\[
y-x=qd
\]
for some \(q\in\{1,\ldots,n-1\}\). For a fixed \(q\), this determines \(d\), and there are at most \(n-q\) possible starts. Hence, deterministically,
\[
\Delta_2(H)
\le \max\left\{n,\sum_{q=1}^{n-1}(n-q)\right\}
=O_n(1).
\tag{13}
\]

For a fixed label degree, changing the reservoir status of one point changes the degree by at most \(n\). For a fixed point degree, after conditioning on that point belonging to \(W\), changing another point's status changes the degree by at most the bound in (13). Changing one retention coin changes a degree by at most one. Each of these degrees depends on only \(O(k)\) relevant independent variables.

The bounded-differences inequality, with deviation \(k^{2/3}\), therefore shows that, simultaneously for all labels and point vertices, with probability tending to one,
\[
\deg_H(d)=(1+o(1))D
\qquad(d\in S),
\tag{14}
\]
and
\[
\deg_H(x)\le(1-\gamma)D
\qquad(x\in W)
\tag{15}
\]
for some fixed \(\gamma>0\). Indeed, each failure probability is
\[
\exp(-\Omega(k^{1/3})),
\]
and there are only \(O(k)\) degrees to consider.

We also require a reservoir property. For \(d\in S\), let
\[
Y_d=\bigl|\{a:A(d,a)\subseteq R\}\bigr|.
\]
Then
\[
\mathbb EY_d=\rho^nL_d\ge\rho^n\alpha k.
\]
Changing the reservoir status of one point changes \(Y_d\) by at most \(n\). Another application of bounded differences shows that, simultaneously for every \(d\in S\), with probability tending to one,
\[
Y_d\ge \frac12\rho^n\alpha k=:ck,
\tag{16}
\]
where \(c>0\) is fixed.

Fix a realization satisfying (14)–(16). By (14)–(15),
\[
\Delta(H)=(1+o(1))D,
\]
and (13) gives \(\Delta_2(H)=o(D)\). The edge-colouring theorem partitions \(E(H)\) into at most
\[
(1+o(1))D
\]
matchings.

Writing \(N=|S|\), every edge contains exactly one label, so
\[
|E(H)|=\sum_{d\in S}\deg_H(d)=(1+o(1))ND.
\]
Some colour class is therefore a matching containing at least
\[
(1-o(1))N
\]
edges. It packs all but a set \(T\) of labels, where
\[
|T|=o(k).
\]

Pack the remaining labels greedily inside \(R\). For any new difference \(d\), a previously used point forbids at most \(n\) candidate starts. Thus one previously selected progression forbids at most \(n^2\) candidates. Throughout the completion, fewer than
\[
n^2|T|=o(k)
\]
candidates are forbidden, whereas (16) supplies at least \(ck\) candidates for every remaining label. The greedy completion succeeds for sufficiently large \(k\).

The first matching lies in \(W\), while the completion lies in \(R\), so the two packings are disjoint. ∎

## 4. The small differences cost only \(O_n(s)\)

We will put an arbitrarily small initial segment of differences in a separate interval.

For every \(s\ge1\),
\[
M_s(n)\le (n^2+n-1)s.
\tag{17}
\]
To see this, set
\[
m=(n^2+n-1)s
\]
and greedily place the differences \(1,\ldots,s\). Every difference \(d\le s\) has at least
\[
m-(n-1)d\ge n^2s
\]
admissible starts. Each previously used point forbids at most \(n\) starts, so after at most \(s-1\) progressions have been placed, at most
\[
n^2(s-1)
\]
starts are forbidden. There is always an available choice.

## 5. Proof of the theorem

Fix a constant
\[
0<\eta<\frac12.
\]
For sufficiently large \(k\), put
\[
K=\lceil(1+\eta)k\rceil,
\qquad
q=\lfloor\eta k\rfloor,
\qquad
m=nK.
\]
In particular,
\[
k<K\le2k.
\]

Take the weights from Lemma 1 on \([nK]\), but retain only labels
\[
S=\{q+1,\ldots,k\}.
\]
For \(d\in S\), set \(w_{d,a}=u_{d,a}\).

We check every hypothesis of Lemma 2:

- The label sums remain exactly one, by (1).
- By (3),
  \[
  w_{d,a}\le\frac1d
  \le\frac1{q+1}
  \le\frac1{\eta k}.
  \tag{18}
  \]
- Removing the labels greater than \(k\), and then also those at most \(q\), gives by (4)
  \[
  \sum_{\substack{d\in S,\ a\\x\in A(d,a)}}w_{d,a}
  \le1-\frac{K-k}{2K}
  \le1-\frac{\eta}{4}.
  \tag{19}
  \]
- Every retained difference has at least
  \[
  L_d=nK-(n-1)d
  \ge nK-(n-1)k
  \ge k
  \tag{20}
  \]
  admissible starts.
- Finally, \(m=nK\le2nk=O(k)\).

Thus Lemma 2 applies with, for example,
\[
\alpha=1,\qquad C=\frac1\eta,\qquad \delta=\frac\eta4.
\]
It packs all differences \(q+1,\ldots,k\) in \([nK]\), once \(k\) is sufficiently large.

By (17), the remaining differences \(1,\ldots,q\) can be packed in a separate interval of length
\[
(n^2+n-1)q.
\]
Concatenating the two intervals gives
\[
\begin{aligned}
M_k(n)
&\le nK+(n^2+n-1)q\\
&\le nk+(n^2+2n-1)\eta k+n.
\end{aligned}
\tag{21}
\]

Since \(\eta>0\) was arbitrary, first letting \(k\to\infty\) and then \(\eta\downarrow0\) yields
\[
\limsup_{k\to\infty}\frac{M_k(n)}k\le n.
\]
The \(k\) disjoint progressions contain \(nk\) points, so
\[
M_k(n)\ge nk.
\]
Consequently,
\[
\boxed{M_k(n)=nk+o(k)=(1+o(1))nk}
\]
for every fixed positive integer \(n\). ∎

## Scope and dependencies

The only non-elementary input is the established Pippenger–Spencer edge-colouring theorem; its applicability, including the maximum-degree formulation, was checked above. The argument leaves no unresolved fractional-packing or completion step.

The proof is asymptotic for **fixed** \(n\). It does not assert uniformity when \(n\) grows with \(k\), nor does it extract an explicit rate for the \(o(1)\) term.