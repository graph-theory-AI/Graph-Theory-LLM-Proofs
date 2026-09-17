```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "Both equality characterizations hold for graphs with at most two negative eigenvalues, and also for graphs with at most two positive eigenvalues and adjacency nullity at most one.",
  "would_publish": false,
  "caveats": "The general case remains open; the low-nullity argument excludes equality without proving the lower bound, and novelty of these special cases has not been checked."
}
```

# A low-inertia and low-nullity partial resolution

Let \(G\) be a connected simple graph. Write
\[
p=n_+(A_G),\qquad q=n_-(A_G),\qquad z=n_0(A_G).
\]
Thus \(p+q+z=n\).

The following results extend the one-positive-eigenvalue case in the previous attempt. The proofs below are self-contained apart from standard Perron–Frobenius theory, eigenvalue interlacing, and Sylvester’s law of inertia. In particular, I do not assume the previous phase-integral argument.

## Theorem
For a connected graph \(G\):

1. If \(p\le 2\) or \(q\le 2\), then
   \[
   s^+(G)=n-1\quad\Longleftrightarrow\quad G\text{ is a tree}.
   \]

2. If any of
   \[
   p\le1,\qquad q\le2,\qquad p=2\text{ and }z\le1
   \]
   holds, then
   \[
   s^-(G)=n-1
   \quad\Longleftrightarrow\quad
   G\text{ is a tree or a complete graph}.
   \]

Consequently:

- the positive equality characterization holds whenever \(\operatorname{rank}A_G\le5\);
- both characterizations hold whenever \(\operatorname{rank}A_G\le4\);
- both hold for every graph with at most two positive eigenvalues and adjacency nullity at most one.

The last assertion uses an arithmetic argument specific to equality. It does **not** establish \(s^-(G)\ge n-1\) throughout that class.

---

# 1. Preliminary identities

The case \(n=1\) is immediate, so assume \(n\ge2\).

Let the positive eigenvalues be
\[
\alpha_1,\ldots,\alpha_p
\]
and the negative eigenvalues be
\[
-\beta_1,\ldots,-\beta_q,
\]
where all \(\alpha_i,\beta_j>0\). Since \(\operatorname{tr}A_G=0\), put
\[
L=\sum_i\alpha_i=\sum_j\beta_j>0.
\]
Also set
\[
U=e_3(\alpha_1,\ldots,\alpha_p),\qquad
V=e_3(\beta_1,\ldots,\beta_q),
\]
with \(e_3=0\) when fewer than three arguments are present.

Let \(m=|E(G)|\), let \(\tau\) be the number of triangles, and let
\[
c=m-n+1.
\]
Then
\[
s^++s^-=2m.
\]

Newton’s identity
\[
\sum_i x_i^3
=\left(\sum_i x_i\right)^3
-3\left(\sum_i x_i\right)e_2(x)+3e_3(x)
\]
gives
\[
6\tau
=\frac{3L}{2}(s^+-s^-)+3(U-V).
\]
Therefore
\[
\boxed{\quad
s^+=m+\frac{2\tau+V-U}{L},\qquad
s^-=m-\frac{2\tau+V-U}{L}.
\quad} \tag{1}
\]

In particular, if \(p\le2\), then \(U=0\), and hence
\[
\boxed{s^+(G)\ge m.} \tag{2}
\]
Since a connected non-tree has \(m\ge n\), this proves the positive equality characterization whenever \(p\le2\).

For completeness, if \(G\) is bipartite, its spectrum is symmetric about zero, so
\[
s^+(G)=s^-(G)=m.
\]
Thus both equalities are characterized by trees within the bipartite class. A complete graph has spectrum \(n-1,-1,\ldots,-1\), giving \(s^-(K_n)=n-1\).

---

# 2. A triangle bound in terms of degeneracy and cycle rank

The arithmetic argument later will require a slightly sharpened version of the elementary bound \(\tau\le dc/2\).

For a possibly disconnected graph \(H\), define
\[
c(H)=|E(H)|-|V(H)|+\kappa(H),
\]
where \(\kappa(H)\) is its number of components. Let \(d(H)\) be its degeneracy, and put
\[
F(d)=\frac{d(d-1)(d-2)}{12}.
\]

## Lemma 2.1
Every graph \(H\) of degeneracy \(d\) satisfies
\[
\boxed{\quad
\tau(H)\le \frac d2\,c(H)-F(d).
\quad} \tag{3}
\]

### Proof

We first record that a graph of degeneracy \(h\) has
\[
c(H)\ge \binom h2. \tag{4}
\]
For \(h=0,1\), this is immediate. For \(h\ge2\), take a connected component \(J\) of an induced subgraph having minimum degree at least \(h\). If \(N=|V(J)|\), then \(N\ge h+1\) and
\[
c(J)\ge \frac{hN}{2}-N+1
\ge \frac{(h-2)(h+1)}2+1
=\binom h2.
\]
Cycle rank is monotone under taking supergraphs, proving (4).

We prove (3) by induction on the number of vertices. Edgeless graphs are immediate. Choose a vertex \(v\) of degree \(k\le d\), and let \(H'=H-v\). Let \(r\) be the number of components of \(H'\) containing a neighbor of \(v\), with respective neighbor counts \(k_1,\ldots,k_r\). Then
\[
c(H)-c(H')=k-r
\]
and
\[
\tau(H)-\tau(H')
\le \sum_{j=1}^r\binom{k_j}{2}
\le \frac d2\sum_{j=1}^r(k_j-1)
=\frac d2(k-r). \tag{5}
\]

Deleting one vertex lowers degeneracy by at most one. Indeed, deleting that vertex from a subgraph of minimum degree \(d\) leaves minimum degree at least \(d-1\). Thus \(d(H')\in\{d,d-1\}\).

If \(d(H')=d\), induction and (5) immediately give (3).

If \(d(H')=d-1\), induction gives
\[
\begin{aligned}
\tau(H)
&\le \frac{d-1}{2}c(H')-F(d-1)+\frac d2(k-r)\\
&=\frac d2c(H)-F(d-1)-\frac12c(H').
\end{aligned}
\]
By (4),
\[
\frac12c(H')\ge \frac{(d-1)(d-2)}4
=F(d)-F(d-1).
\]
This again yields (3). ∎

The constant is sharp, for example on complete graphs.

We also use the standard inequality
\[
d(G)\le \rho(G), \tag{6}
\]
where \(\rho(G)\) is the spectral radius: an induced subgraph of minimum degree \(d\) has spectral radius at least its average degree, hence at least \(d\).

## Corollary 2.2: a rigidity statement

Suppose \(G\) is connected and, for an integer \(r\ge2\),
\[
\rho(G)=r,\qquad
c(G)=\binom r2,\qquad
\tau(G)=\binom{r+1}{3}.
\]
Then \(G=K_{r+1}\).

### Proof

Let \(d=d(G)\le r\). At the fixed value \(c=\binom r2\), define
\[
f_d=\frac d2c-F(d).
\]
For \(0\le d<r\),
\[
f_{d+1}-f_d
=\frac{r(r-1)-d(d-1)}4>0.
\]
Moreover,
\[
f_r=\binom{r+1}{3}.
\]
Lemma 2.1 therefore forces \(d=r\).

There is an induced subgraph of minimum degree \(r\), whose spectral radius is at least \(r\). A proper induced subgraph of a connected graph has strictly smaller spectral radius, so this subgraph must be all of \(G\). Since \(\rho(G)=r\), the average-degree bound now forces \(G\) to be \(r\)-regular.

For \(r\ge3\),
\[
\binom r2=c(G)=\frac{n(r-2)}2+1
\]
gives \(n=r+1\), and \(G\) is complete. For \(r=2\), \(G\) is a cycle; the condition \(\tau(G)=1\) forces \(G=C_3\). ∎

---

# 3. Negative square energy when there are at most two negative eigenvalues

Suppose \(q\le2\). Then \(V=0\), so (1) and Lemma 2.1 give
\[
\begin{aligned}
s^-
&=m-\frac{2\tau}{L}+\frac UL\\
&\ge n-1+c\left(1-\frac dL\right)
  +\frac{2F(d)+U}{L}. \tag{7}
\end{aligned}
\]

If \(p\ge2\), then
\[
L>\rho(G)\ge d.
\]
Consequently, whenever \(G\) is not a tree, \(c\ge1\), and (7) yields
\[
\boxed{s^-(G)>n-1\qquad(q\le2,\ p\ge2,\ G\text{ not a tree}).} \tag{8}
\]

To cover \(p=1\), and also recover that case without restricting \(q\), we reprove the spectral-radius estimate used in the previous attempt.

## Lemma 3.1
For a connected graph of order \(n\ge2\),
\[
\rho^2\le 2m-n+1,
\]
with equality exactly for stars and complete graphs.

### Proof

Let \(x>0\) be a Perron vector, and choose \(v\) with \(x_v=\max_w x_w\). Then
\[
\rho^2x_v
=\sum_{u\sim v}\sum_{w\sim u}x_w
\le x_v\sum_{u\sim v}d(u)
\le x_v(2m-n+1).
\]
The final inequality uses that every vertex outside \(N[v]\) has degree at least one.

Suppose equality holds. Every vertex outside \(N[v]\) then has degree one, and every endpoint of a two-step walk from \(v\) has Perron coordinate \(x_v\).

If a vertex \(z\notin N[v]\) existed, connectedness and the degree-one condition would place it at distance two from \(v\). Hence \(x_z=x_v\), while its eigenvalue equation gives
\[
\rho x_z=x_u\le x_v=x_z.
\]
This implies \(\rho\le1\), contradicting the presence of a \(P_3\). Thus \(v\) is universal.

Let \(U\) be the nonisolated vertices of \(G-v\), and let \(k\) be the number of isolated vertices of \(G-v\). If \(U\) is empty, \(G\) is a star.

Otherwise, all vertices in \(U\) have coordinate \(x_v\), and their eigenvalue equations show that \(G[U]\) is \((\rho-1)\)-regular. Thus \(h=|U|\ge\rho\). The equation at \(v\) is
\[
\rho=h+\frac{k}{\rho},
\]
forcing \(h=\rho\) and \(k=0\). Hence \(G[U]\), and therefore \(G\), is complete.

Stars and complete graphs attain equality by direct calculation. ∎

If \(p=1\), then \(s^+=\rho^2\), so
\[
s^-=2m-\rho^2\ge n-1,
\]
with equality exactly for stars and complete graphs. Together with (8), this proves the negative characterization for \(q\le2\), and also for \(p\le1\).

---

# 4. Positive square energy when there are at most two negative eigenvalues

The following structural observation handles the portion not already covered by \(p\le2\).

## Lemma 4.1
Let \(G\) be connected with \(q\le2\). Then at least one of the following holds:

1. \(G\) is bipartite;
2. \(p\le2\);
3. \(G\) is an independent blow-up of \(C_5\).

Here an independent blow-up replaces each cycle vertex by a nonempty independent set, with all edges between consecutive sets and no other edges.

### Proof

Suppose first that \(G\) contains a triangle. Partition its adjacency matrix as
\[
A_G=
\begin{pmatrix}
C&B\\
B^T&D
\end{pmatrix},
\qquad C=A_{K_3}.
\]
The matrix \(C\) has inertia \((1,2,0)\), and
\[
C^{-1}=\tfrac12J-I.
\]
By Schur-complement congruence,
\[
S=D-B^TC^{-1}B\succeq0,
\]
because all two allowed negative eigenvalues have already occurred in \(C\).

For an outside vertex \(x\), let \(b_x\) be its incidence vector to the triangle and \(k_x=|b_x|\). Then
\[
S_{xx}=k_x-\frac{k_x^2}{2}.
\]
Thus \(k_x\in\{0,1,2\}\). Vertices with \(k_x=0\) or \(2\) have zero diagonal in \(S\), hence zero rows.

For the remaining vertices, \(b_x\) is a coordinate vector and \(S_{xx}=1/2\). For two such vertices,
\[
S_{xy}=A_{xy}+\mathbf1_{\{b_x=b_y\}}-\tfrac12.
\]
Positive semidefiniteness forces
\[
|S_{xy}|=\tfrac12.
\]
In a Gram representation of \(S\), all its nonzero vectors are therefore parallel. Hence \(\operatorname{rank}S\le1\), and
\[
p=1+\operatorname{rank}S\le2.
\]

Now suppose \(G\) is triangle-free and nonbipartite. A shortest odd cycle is induced. Every odd cycle of length at least seven has at least four negative eigenvalues, whereas \(C_5\) has two. Interlacing therefore supplies an induced \(C_5\).

Write \(C=A_{C_5}\) and again use the Schur complement
\[
S=D-B^TC^{-1}B\succeq0.
\]
Here
\[
C^{-1}=I+C-\tfrac12J.
\]
Since \(G\) is triangle-free, each outside neighborhood in \(C_5\) is independent and has size \(k\le2\). Thus
\[
S_{xx}=-\left(k-\frac{k^2}{2}\right).
\]
Positive semidefiniteness excludes \(k=1\); for \(k=0,2\), the diagonal is zero. Therefore \(S=0\).

A vertex with \(k=0\) would consequently be isolated, contrary to connectedness. Every outside vertex thus has two nonadjacent neighbors on the cycle, exactly the neighborhood of a unique cycle vertex \(i\). Its incidence vector is \(Ce_i\). The equality \(S=0\) forces the adjacencies between outside vertices to agree with those of their corresponding cycle vertices. Hence \(G\) is an independent blow-up of \(C_5\). ∎

Every such blow-up has diameter two. We use the following elementary bound.

## Lemma 4.2
If a connected graph has diameter at most two, then
\[
\rho^2\ge n-1.
\]

### Proof

Each ordered pair of distinct nonadjacent vertices has a common neighbor. Consequently,
\[
\mathbf1^TA^2\mathbf1
=\sum_v d(v)^2
\ge 2m+\bigl(n(n-1)-2m\bigr)
=n(n-1).
\]
The Rayleigh quotient for \(A^2\) gives the result. ∎

An independent blow-up of \(C_5\) contains an induced \(C_5\), so it has at least three positive eigenvalues. Hence
\[
s^+>\rho^2\ge n-1.
\]

Together with the bipartite case and (2), Lemma 4.1 proves the positive characterization whenever \(q\le2\).

---

# 5. An arithmetic obstruction for two positive eigenvalues

We now address graphs with \(p=2\) but potentially many negative eigenvalues. This is the part that goes beyond a lower-bound argument.

## Lemma 5.1: rational positive square energy

Suppose \(G\) is connected and nonbipartite, has exactly two positive eigenvalues
\[
\rho>\sigma>0,
\]
and \(\rho^2+\sigma^2\in\mathbb Q\). Then one of the following holds:

1. The polynomial
   \[
   (x-\rho)(x-\sigma)
   \]
   has integer coefficients, and the multiset of negative eigenvalues is Galois-invariant.

2. \(\rho\) is an integer, \(\sigma=\sqrt{k}\) for a nonsquare positive integer \(k\), and \(-\sqrt{k}\) is a simple eigenvalue. After removing
   \[
   \rho,\sqrt{k},-\sqrt{k}
   \]
   and the zero eigenvalues, the remaining negative eigenvalues form a Galois-invariant multiset.

### Proof

Work in the splitting field of the characteristic polynomial. For any Galois automorphism \(g\), set
\[
a=g(\rho),\qquad b=g(\sigma).
\]
These are adjacency eigenvalues and
\[
a^2+b^2=\rho^2+\sigma^2.
\]
All eigenvalue moduli are at most \(\rho\), so both \(|a|\) and \(|b|\) lie in \([\sigma,\rho]\). Therefore
\[
|a|+|b|\ge\rho+\sigma,
\]
with equality only when their moduli are \(\rho,\sigma\).

Because \(G\) is connected and nonbipartite, \(-\rho\) is not an eigenvalue. Thus, if both \(a,b\) were negative, their absolute values would sum to strictly more than \(\rho+\sigma\), contradicting
\[
\sum_{\lambda<0}|\lambda|=\rho+\sigma.
\]
If one image is positive, it is either \(\rho\) or \(\sigma\); the square-sum equation then shows that
\[
g\{\rho,\sigma\}\in
\bigl\{\{\rho,\sigma\},\{\rho,-\sigma\}\bigr\}. \tag{9}
\]

If every automorphism preserves the positive pair, its monic quadratic has rational algebraic-integer coefficients, hence integer coefficients. Its complement in the full spectral multiset is likewise invariant.

Otherwise \(-\sigma\) is an eigenvalue. In this situation every automorphism fixes \(\rho\): if \(g(\rho)\ne\rho\), (9) forces \(g(\sigma)=\rho\), and then \(g(-\sigma)=-\rho\), a contradiction. Hence \(\rho\in\mathbb Z\). Also \(g(\sigma)\in\{\sigma,-\sigma\}\), so \(\sigma^2=k\in\mathbb Z\). The nontrivial alternative requires \(k\) to be nonsquare. Since \(\sigma\) is simple, so is its conjugate \(-\sigma\). The remaining multiset is invariant. ∎

We need one elementary arithmetic gap.

## Lemma 5.2
Let \(\gamma_1,\ldots,\gamma_\ell>0\) be a Galois-invariant multiset of algebraic integers, with \(\ell\ge1\). Then either all \(\gamma_i=1\), or
\[
\sum_i\gamma_i^2>\ell+2.
\]

### Proof

Both \(\sum_i\gamma_i\) and \(\prod_i\gamma_i\) are positive integers. AM–GM gives
\[
\sum_i\gamma_i\ge\ell,
\]
with equality only when all \(\gamma_i=1\). Otherwise the integer sum is at least \(\ell+1\), and
\[
\sum_i\gamma_i^2
\ge \frac{(\ell+1)^2}{\ell}
=\ell+2+\frac1\ell.
\]
∎

## Proposition 5.3
A connected nonbipartite graph with \(p=2\) and \(z\le1\) cannot satisfy \(s^-=n-1\).

### Proof

Suppose otherwise. Since
\[
s^+=2m-(n-1),
\]
the positive square energy is an integer, and Lemma 5.1 applies.

Write \(q=n-2-z\).

### Case I: the positive quadratic is integral

The negative magnitudes form a Galois-invariant multiset, and
\[
\sum_{j=1}^q\beta_j^2=n-1=q+z+1\le q+2.
\]
Lemma 5.2 forces all \(\beta_j=1\), but then \(s^-=q<n-1\), a contradiction.

### Case II: there is a conjugate pair \(\pm\sqrt{k}\)

Remove the negative eigenvalue \(-\sqrt{k}\), and denote the remaining negative magnitudes by
\[
\gamma_1,\ldots,\gamma_\ell,\qquad \ell=q-1.
\]
The trace identity gives
\[
\rho=\sum_i\gamma_i,
\]
so \(\ell\ge1\). Also
\[
\sum_i\gamma_i^2
=n-1-k
=\ell+z+2-k
\le\ell+1,
\]
because \(k\ge2\) and \(z\le1\). Lemma 5.2 forces all \(\gamma_i=1\).

Thus
\[
\rho=\ell=:r,\qquad k=z+2,
\]
and the full spectrum is
\[
r,\ \sqrt{k},\ -\sqrt{k},\ 
\underbrace{-1,\ldots,-1}_{r\text{ times}},
\underbrace{0,\ldots,0}_{z\text{ times}}. \tag{10}
\]
Since \(r>\sqrt{k}\), we have \(r\ge2\).

Computing the second and third spectral moments from (10) gives
\[
c(G)=\binom r2,\qquad
\tau(G)=\binom{r+1}{3},\qquad
\rho(G)=r.
\]
Corollary 2.2 forces \(G=K_{r+1}\), contradicting the second positive eigenvalue.

Both cases are impossible. ∎

For bipartite graphs the characterization was already proved. Proposition 5.3 therefore completes the claimed low-nullity case.

---

# 6. A sharper description of the first remaining nullity case

The same arithmetic argument considerably restricts a possible additional equality graph with \(p=2\) and \(z=2\).

## Proposition 6.1
If a connected nonbipartite graph satisfies
\[
p=2,\qquad z=2,\qquad s^-=n-1,
\]
then its spectrum must have the form
\[
\boxed{\quad
\alpha,\ \beta,\ 0,\ 0,\ -2,\
\underbrace{-1,\ldots,-1}_{n-5\text{ times}},
\quad} \tag{11}
\]
where
\[
\alpha+\beta=n-3,\qquad \alpha\beta\in\mathbb Z_{>0}.
\]

### Proof

In Case II of Lemma 5.1, the remaining negative magnitudes would satisfy
\[
\sum_i\gamma_i^2=\ell+4-k\le\ell+2.
\]
Lemma 5.2 forces all of them to be one, giving \(k=4\), contrary to the nonsquare requirement. Hence Case I holds.

Here \(q=n-4\) and
\[
\sum_j\beta_j^2=q+3.
\]
The integer sum \(S=\sum_j\beta_j\) must equal \(q+1\): it cannot equal \(q\), and \(S\ge q+2\) would contradict Cauchy–Schwarz. Consequently,
\[
\sum_j(\beta_j-1)^2=1.
\]
Thus \(0<\beta_j\le2\).

If no \(\beta_j\) equals two, every algebraic conjugate of every \(\beta_j-1\) lies in \((-1,1)\). A nonzero algebraic integer cannot have this property, since its nonzero integer norm would have absolute value less than one. Hence some \(\beta_j=2\), and the displayed sum of squares then forces all other \(\beta_j=1\).

The assertions about \(\alpha+\beta\) and \(\alpha\beta\) follow from the integral positive quadratic. ∎

This is only a necessary spectral condition. I have not excluded all nonbipartite realizations of (11).

---

# 7. What remains unresolved

The results above impose the following necessary conditions on any additional equality example:

- For
  \[
  s^+(G)=n-1
  \]
  with \(G\) not a tree, one must have
  \[
  p\ge3,\qquad q\ge3.
  \]

- For
  \[
  s^-(G)=n-1
  \]
  with \(G\) neither a tree nor complete, one must have
  \[
  p\ge2,\qquad q\ge3.
  \]
  If \(p=2\), then necessarily \(z\ge2\); when \(z=2\), the spectrum must have the restricted form (11).

These are genuine exclusions, but they do not settle the general conjecture. In particular, the third-moment identity has uncontrolled contributions from both \(U\) and \(V\) when both inertias are large, and the arithmetic argument for two positive eigenvalues leaves a real gap once the nullity is at least two.

No complete proof or counterexample is claimed, and I have not verified the literature novelty of these special-case results.