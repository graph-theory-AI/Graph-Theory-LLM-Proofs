```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture is not settled, but it holds with k=ceil(log2 s) for weight-at-most-two binary matroids and their complete lifts, while explicit non-frame examples force any general bound k(s) to be at least (s-3)/4.",
  "would_publish": false,
  "caveats": "Arbitrary binary matroids for fixed s at least 5 remain uncontrolled, and the linear lower-bound examples avoid I_s only because their rank is less than s."
}
```

# 1. Vector-space formulation

Represent a simple rank-\(r\) binary matroid \(M\) by a spanning set
\[
E\subseteq V\setminus\{0\},\qquad V=\mathbb F_2^r.
\]

In this language:

* \(M\) is triangle-free if and only if
  \[
  x,y\in E,\quad x\ne y\quad\Longrightarrow\quad x+y\notin E.
  \]
  Indeed, the three nonzero points of a two-dimensional binary subspace are \(x,y,x+y\).

* \(M\) has an induced \(I_s\)-restriction if and only if there is an \(s\)-dimensional subspace \(U\le V\) such that \(E\cap U\) is a basis of \(U\).

* The critical number is
  \[
  \chi(M)=\min\{\operatorname{codim}_V(H): H\le V,\ H\cap E=\varnothing\}.
  \]
  Equivalently, \(\chi(M)\) is the least \(k\) for which there is a linear map
  \[
  T:V\longrightarrow \mathbb F_2^k
  \]
  satisfying \(T(e)\ne0\) for every \(e\in E\).

According to the supplied literature review, the unrestricted conjecture is known for \(s\le4\), and remains open for \(s\ge5\).

# 2. A general covering consequence of induced-\(I_s\)-freeness

The following necessary condition applies to every triangle-free binary matroid.

## Proposition 2.1

Let \(s\ge3\), and let \(M=(E,V)\) be triangle-free, induced-\(I_s\)-free, and of rank \(r\ge s\). Then
\[
|E|\ge r+\left\lceil\frac{\binom r3}{\binom s3}\right\rceil.
\]

More precisely, with respect to every basis \(B\subseteq E\), the supports of the nonbasis elements of support size at most \(s\) cover all \(s\)-subsets of \(B\).

### Proof

Fix a basis \(B=\{b_1,\dots,b_r\}\subseteq E\). For every \(s\)-subset \(X\subseteq B\), the set \(X\) is independent. If
\[
E\cap\langle X\rangle=X,
\]
then \(X\) is an induced \(I_s\)-restriction. Thus there is some
\[
e_X\in (E\cap\langle X\rangle)\setminus X.
\]

Write \(e_X\) in the basis \(B\), and let \(F_X\subseteq X\) be its support. We have \(|F_X|\ge3\): support \(0\) is impossible, support \(1\) would make \(e_X\) a basis element, and support \(2\) would give a triangle consisting of two basis points and their sum.

Let
\[
\mathcal F=\{\operatorname{supp}_B(e):e\in E\setminus B,\ 3\le |\operatorname{supp}_B(e)|\le s\}.
\]
Every \(s\)-subset of \(B\) contains a member of \(\mathcal F\). A member \(F\in\mathcal F\) of size \(f\ge3\) is contained in
\[
\binom{r-f}{s-f}\le \binom{r-3}{s-3}
\]
different \(s\)-subsets of \(B\). Therefore
\[
\binom rs\le |\mathcal F|\binom{r-3}{s-3}.
\]
Hence
\[
|E|-r\ge |\mathcal F|
 \ge \frac{\binom rs}{\binom{r-3}{s-3}}
 =\frac{\binom r3}{\binom s3}.
\]
This proves the claim. \(\square\)

This gives a cubic lower bound in the rank, for fixed \(s\), but does not by itself produce a bounded-codimension subspace disjoint from \(E\).

# 3. The conjecture for weight-at-most-two representations

Call a binary matroid weight-at-most-two representable if it has a representation
\[
E\subseteq \mathbb F_2^X
\]
in which every column has Hamming weight one or two. This includes all graphic matroids.

## Theorem 3.1

Let \(s\ge2\). If \(M\) is a triangle-free, induced-\(I_s\)-free simple binary matroid admitting a weight-at-most-two representation, then
\[
\chi(M)\le \left\lceil\log_2 s\right\rceil.
\]

### Proof

Write the weight-two columns as \(e_x+e_y\), and form a simple graph \(G\) on \(X\) having edge \(xy\) precisely when \(e_x+e_y\in E\). Let
\[
Z=\{x\in X:e_x\in E\}
\]
be the set of coordinates supporting weight-one columns.

We first show
\[
\Delta(G)\le s-1.
\]
Suppose some vertex \(x\) has distinct neighbors \(y_1,\dots,y_s\). Set
\[
a_i=e_x+e_{y_i}.
\]
These \(s\) vectors are independent. For \(J\subseteq\{1,\dots,s\}\),
\[
\sum_{i\in J}a_i
 =(|J|\bmod 2)e_x+\sum_{i\in J}e_{y_i}.
\]
If \(|J|\ge3\), this vector has weight at least four. If \(|J|=2\), it is \(e_{y_i}+e_{y_j}\). Such a vector cannot belong to \(E\), since together with \(a_i,a_j\) it would form a triangle. Weight-one columns cannot occur in the span of the \(a_i\). Consequently
\[
E\cap\langle a_1,\dots,a_s\rangle=\{a_1,\dots,a_s\},
\]
an induced \(I_s\), a contradiction.

Next, \(Z\) is a stable set in \(G\): if \(x,y\in Z\) and \(xy\in E(G)\), then
\[
e_x,\ e_y,\ e_x+e_y
\]
form a triangle.

Use a palette of \(s\) colors. Precolor every vertex of \(Z\) with the same color. Since \(Z\) is stable, this is proper. Color the remaining vertices greedily. At each step a vertex has at most \(s-1\) colored neighbors, so some color remains available.

Put \(k=\lceil\log_2s\rceil\), and assign the \(s\) colors distinct vectors of \(\mathbb F_2^k\), choosing the common color of \(Z\) to be nonzero. Define
\[
T(e_x)=c(x),
\]
where \(c(x)\) is the vector assigned to the color of \(x\). Then:

* if \(e_x\in E\), we have \(x\in Z\), so \(T(e_x)=c(x)\ne0\);
* if \(e_x+e_y\in E\), then \(xy\in E(G)\), so \(c(x)\ne c(y)\), and hence
  \[
  T(e_x+e_y)=c(x)+c(y)\ne0.
  \]

Thus \(\ker T\) is disjoint from \(E\), and its codimension in \(\langle E\rangle\) is at most \(k\). \(\square\)

## Graphic specialization

For a nonempty simple graph \(G\),
\[
\chi(M(G))=\left\lceil\log_2\chi_{\mathrm{graph}}(G)\right\rceil.
\]

Indeed, in the standard representation an edge \(uv\) is \(e_u+e_v\). Vertex labels in \(\mathbb F_2^k\) define a linear map avoiding all edge vectors exactly when adjacent vertices receive different labels. Conversely, fixing one root in each component recovers vertex labels from any such linear map.

If \(G\) is triangle-free and \(M(G)\) is induced-\(I_s\)-free, the induced-star argument above gives \(\Delta(G)\le s-1\), and hence
\[
\chi_{\mathrm{graph}}(G)\le s,\qquad
\chi(M(G))\le\lceil\log_2s\rceil.
\]

As a small sharpness observation, \(M(C_5)\) is triangle-free, induced-\(I_4\)-free, and has critical number \(2\). Thus the supplied bound \(k=2\) for \(s=4\) is optimal.

## Complete lifts

The same conclusion holds for a somewhat larger class. Let
\[
\pi:V\twoheadrightarrow Q,\qquad E=\pi^{-1}(S),
\]
where \(S\subseteq Q\setminus\{0\}\) spans \(Q\). Then
\[
\chi(E)=\chi(S).
\]

To see this, preimages of subspaces disjoint from \(S\) are disjoint from \(E\), giving \(\chi(E)\le\chi(S)\). Conversely, if \(H\le V\) is disjoint from \(E\), then \(\pi(H)\) is disjoint from \(S\), and
\[
\operatorname{codim}_Q\pi(H)\le\operatorname{codim}_V H.
\]

Moreover, if \(S\) contained an induced \(I_s\) on a subspace \(U\le Q\), a linear section \(U\to V\) would give an induced \(I_s\) in \(E\). Similarly, a triangle in \(S\) lifts to a triangle in \(E\). Therefore Theorem 3.1 also applies when \(E\) is a complete inverse image of a weight-at-most-two matroid.

# 4. A linear lower bound on any possible \(k(s)\)

Define
\[
K(s)=\sup\{\chi(M):M\text{ is triangle-free and induced-}I_s\text{-free}\}.
\]
The conjecture asserts \(K(s)<\infty\). The next construction shows that \(K(s)\), if finite, must grow at least linearly.

## Theorem 4.1

For every \(m\ge1\), there is a triangle-free simple binary matroid \(M_m\) of rank at most \(2m\) such that
\[
\chi(M_m)\ge\left\lceil\frac m2\right\rceil.
\]

### Construction and triangle-freeness

Let \(F=\mathbb F_{2^m}\), regarded as an \(m\)-dimensional vector space over \(\mathbb F_2\), and put
\[
A_m=\{(x,x^3):x\in F^\times\}\subseteq F\times F.
\]
Let \(M_m\) be the binary matroid represented by \(A_m\) in its linear span.

Suppose distinct points \((x,x^3),(y,y^3)\in A_m\) had their sum in \(A_m\). Its first coordinate would force the third parameter to be \(x+y\), and hence
\[
x^3+y^3=(x+y)^3.
\]
In characteristic two,
\[
(x+y)^3+x^3+y^3=xy(x+y).
\]
For distinct nonzero \(x,y\), this is nonzero. Thus \(A_m\) is triangle-free.

### A polynomial parity lemma

If \(P_1,\dots,P_k:\mathbb F_2^m\to\mathbb F_2\) are polynomial functions with
\[
P_i(0)=0,\qquad \sum_i\deg P_i<m,
\]
then they have a common nonzero zero.

Indeed, modulo two the number \(N\) of common zeros is
\[
N\equiv
\sum_{x\in\mathbb F_2^m}\prod_{i=1}^k(1+P_i(x)).
\]
Every term in the expansion has degree less than \(m\). The sum over \(\mathbb F_2^m\) of any monomial of degree less than \(m\) is zero modulo two, since some variable is absent and summing over that coordinate contributes a factor \(2\). Thus \(N\) is even. Since \(0\) is a common zero, there must be another one.

### Critical-number lower bound

Let \(H\le F\times F\) have codimension \(k\), where \(2k<m\). Write \(H\) as the common kernel of \(k\) linear forms \(L_1,\dots,L_k\). Set
\[
P_i(x)=L_i(x,x^3).
\]
The Frobenius map \(x\mapsto x^2\) is \(\mathbb F_2\)-linear, and field multiplication is bilinear. Hence \(x\mapsto x^3=x\cdot x^2\) has coordinate degree at most two. Therefore each \(P_i\) has degree at most two.

Since \(2k<m\), the parity lemma supplies \(x\ne0\) with
\[
P_i(x)=0\quad\text{for all }i.
\]
Thus \((x,x^3)\in H\cap A_m\). Consequently every subspace of codimension \(k<m/2\) meets \(A_m\).

If \(W=\langle A_m\rangle\), any codimension-\(k\) subspace of \(W\) can be extended, using a complement of \(W\), to a codimension-\(k\) subspace of \(F\times F\). Hence the same lower bound holds for the critical number computed in \(W\):
\[
\chi(M_m)\ge\left\lceil\frac m2\right\rceil.
\]
This proves the theorem. \(\square\)

## Consequence for the conjectured bound

For \(s\ge3\), take
\[
m=\left\lfloor\frac{s-1}{2}\right\rfloor.
\]
Then
\[
r(M_m)\le2m<s,
\]
so \(M_m\) cannot contain an \(I_s\)-restriction at all. Therefore
\[
K(s)\ge
\left\lceil
\frac12\left\lfloor\frac{s-1}{2}\right\rfloor
\right\rceil
\ge \frac{s-3}{4}.
\]

Thus any proof of the conjecture must allow \(k(s)\) to be at least linear in \(s\). These examples are genuinely non-frame for large \(s\), since Theorem 3.1 gives only logarithmic critical number in the frame class.

# 5. Remaining gap

The frame proof relies on the fact that the span of a large star contains no additional columns of weight at most two, except leaf-to-leaf columns, which triangle-freeness forbids. In an arbitrary binary matroid, a vector such as
\[
a_1+a_2+a_3
\]
may itself be an element without creating a triangle. Such higher sums can destroy every prospective induced \(I_s\); Proposition 2.1 shows that many of them are in fact forced.

Neither the support-covering estimate nor the polynomial construction gives a bounded-codimension hole for arbitrary fixed \(s\). Consequently, no case \(s\ge5\) of the full conjecture is proved here.