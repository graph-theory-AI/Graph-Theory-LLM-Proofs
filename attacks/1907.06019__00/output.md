```json
{
  "verdict": "proved",
  "confidence": "high",
  "one_line": "For n > 2r, the equality case of EKR makes the initial monomials a star, and a rigidity lemma forces the resulting graph map to be exterior multiplication by one vector.",
  "would_publish": true,
  "caveats": "This proves the strict range over the stated real field; the characterization is false at n = 2r, and publication priority has not been independently checked."
}
```

## Statement

Let \(V\) be an \(n\)-dimensional real vector space, let \(1\le r<n/2\), and let
\[
W\subseteq \bigwedge^r V
\]
be self-annihilating, meaning
\[
w\wedge w'=0\qquad\text{for all }w,w'\in W.
\]
If
\[
\dim W=\binom{n-1}{r-1},
\]
then there is a nonzero \(v\in V\) such that
\[
W=v\wedge\bigwedge^{r-1}V.
\]

In fact, the line \(\mathbb Rv\) is uniquely determined by \(W\).

The proof has two parts: an initial-monomial reduction to a coordinate star, followed by a rigidity lemma for linear maps between consecutive exterior powers.

---

## 1. The initial monomials form a star

Fix a basis \(e_0,\dots,e_{n-1}\) of \(V\). For a subset \(A=\{a_1<\cdots<a_r\}\), write
\[
e_A=e_{a_1}\wedge\cdots\wedge e_{a_r}.
\]
Give \(A\) the weight
\[
\omega(A)=\sum_{i\in A}2^i.
\]
All subset weights are distinct. Order the monomial basis of \(\bigwedge^rV\) by decreasing weight, and put a basis of \(W\) into row-echelon form in this order. Let
\[
\mathcal F\subseteq \binom{[n]}r
\]
be its set of pivot, or leading, supports. Then
\[
|\mathcal F|=\dim W.
\]

We claim that \(\mathcal F\) is intersecting. Indeed, suppose \(A,B\in\mathcal F\) were disjoint. Choose echelon vectors
\[
w_A=\alpha_A e_A+\sum_{\omega(P)<\omega(A)}\alpha_Pe_P,
\qquad
w_B=\beta_B e_B+\sum_{\omega(Q)<\omega(B)}\beta_Qe_Q,
\]
with \(\alpha_A\beta_B\ne0\).

In \(w_A\wedge w_B\), the contribution from \(e_A\wedge e_B\) is nonzero. It cannot be cancelled: if another pair \(P,Q\) contributed to the same monomial \(e_{A\cup B}\), then
\[
\omega(P)+\omega(Q)=\omega(A)+\omega(B).
\]
But \(\omega(P)\le\omega(A)\) and \(\omega(Q)\le\omega(B)\), with strict inequality unless \(P=A\) and \(Q=B\). Thus the coefficient of \(e_{A\cup B}\) is nonzero, contradicting \(W\wedge W=0\). Hence \(\mathcal F\) is intersecting.

Now
\[
|\mathcal F|=\binom{n-1}{r-1},
\]
and \(n>2r\). The standard strict equality case of the Erdős–Ko–Rado theorem therefore implies that \(\mathcal F\) is a full star. After relabelling,
\[
\mathcal F=\{A\in\tbinom{[n]}r:0\in A\}.
\]

Put
\[
U=\operatorname{span}(e_1,\dots,e_{n-1}),\qquad k=r-1.
\]
The monomial subspace corresponding to this star is
\[
E=e_0\wedge\bigwedge^kU.
\]
Since all monomials in \(E\) are pivot columns, the coordinate projection
\[
W\longrightarrow E
\]
is an isomorphism. Consequently there is a linear map
\[
f:\bigwedge^kU\longrightarrow\bigwedge^{k+1}U
\]
such that
\[
W=\{\,e_0\wedge x+f(x):x\in\bigwedge^kU\,\}. \tag{1}
\]

It remains to determine \(f\).

---

## 2. Rigidity lemma

### Lemma

Let \(U\) have dimension \(m\ge 2k+2\), where \(k\ge1\). Suppose
\[
f:\bigwedge^kU\longrightarrow\bigwedge^{k+1}U
\]
is linear and satisfies
\[
x\wedge f(y)=(-1)^k y\wedge f(x)
\qquad\text{for all }x,y\in\bigwedge^kU. \tag{2}
\]
Then there is a unique \(a\in U\) such that
\[
f(x)=a\wedge x
\qquad\text{for all }x\in\bigwedge^kU. \tag{3}
\]

### Proof

Choose a basis \(e_1,\dots,e_m\) of \(U\). For a \(k\)-set \(L\), expand
\[
f(e_L)=\sum_{|J|=k+1}c_{J,L}e_J.
\]

We first show that
\[
c_{J,L}\ne0\quad\Longrightarrow\quad L\subseteq J. \tag{4}
\]

Suppose instead that \(q\in L\setminus J\). Since
\[
m-(k+1)\ge k+1,
\]
we can choose a \(k\)-set
\[
I\subseteq [m]\setminus(J\cup\{q\}).
\]
Thus \(I\cap J=\varnothing\), while \(q\notin I\cup J\). Set \(K=I\cup J\), which has size \(2k+1\).

Apply (2) with \(x=e_I\) and \(y=e_L\). On the left, the coefficient of \(e_K\) is, up to a nonzero sign, \(c_{J,L}\): the only \((k+1)\)-set whose wedge with \(e_I\) has support \(K\) is \(J=K\setminus I\). On the right, every nonzero monomial in \(e_L\wedge f(e_I)\) has support containing \(L\), hence contains \(q\), whereas \(q\notin K\). Thus the coefficient of \(e_K\) on the right is zero. This proves (4).

It follows that for each \(k\)-set \(L\),
\[
f(e_L)=\sum_{a\notin L}\mu_{a,L}\,e_a\wedge e_L. \tag{5}
\]

Now fix \(a\), and let \(I,L\) be disjoint \(k\)-sets avoiding \(a\). Comparing in (2) the coefficient with support \(I\cup L\cup\{a\}\) gives
\[
\mu_{a,L}=\mu_{a,I}. \tag{6}
\]
Indeed,
\[
e_L\wedge e_a\wedge e_I=(-1)^k e_I\wedge e_a\wedge e_L,
\]
which cancels the prefactor \((-1)^k\) in (2).

For fixed \(a\), consider the graph whose vertices are the \(k\)-subsets of \([m]\setminus\{a\}\), with two vertices adjacent when they are disjoint. This graph is connected because \(m-1\ge2k+1\). To see this directly, the Johnson graph on the same vertex set is connected; if \(A,B\) differ by one element, then \(|A\cup B|=k+1\), so there is a \(k\)-set \(C\) disjoint from \(A\cup B\), giving the path
\[
A-C-B
\]
in the disjointness graph.

Therefore (6) shows that \(\mu_{a,L}\) is independent of \(L\); denote its value by \(\mu_a\). Let
\[
a_0=\sum_{a=1}^m\mu_a e_a.
\]
Equation (5) now gives
\[
f(e_L)=a_0\wedge e_L
\]
for every basis monomial \(e_L\), and hence \(f(x)=a_0\wedge x\) for all \(x\). Uniqueness is immediate from the coefficients \(\mu_a\). ∎

---

## 3. Applying the rigidity lemma

Return to the representation (1). For \(x,y\in\bigwedge^kU\), self-annihilation gives
\[
0=(e_0\wedge x+f(x))\wedge(e_0\wedge y+f(y)).
\]
Since \(f(x)\) has degree \(k+1\), this expands as
\[
0
=
e_0\wedge\left(
x\wedge f(y)+(-1)^{k+1}y\wedge f(x)
\right)
+
f(x)\wedge f(y).
\]
The two summands lie in the direct-sum components
\[
e_0\wedge\bigwedge^{2k+1}U
\quad\text{and}\quad
\bigwedge^{2k+2}U
\]
of \(\bigwedge^{2k+2}V\). Hence each component vanishes. In particular,
\[
x\wedge f(y)=(-1)^k y\wedge f(x).
\]
Here
\[
\dim U=n-1\ge 2r=2k+2,
\]
so the rigidity lemma applies. Therefore
\[
f(x)=a\wedge x
\]
for some \(a\in U\).

Substituting into (1),
\[
W
=
\{\,(e_0+a)\wedge x:x\in\bigwedge^kU\,\}.
\]
Let
\[
v=e_0+a.
\]
Since \(v\notin U\), we have \(V=\mathbb Rv\oplus U\), and therefore
\[
v\wedge\bigwedge^kV=v\wedge\bigwedge^kU.
\]
Consequently
\[
W=v\wedge\bigwedge^{r-1}V,
\]
as required.

For \(r=1\), the equality assumption is simply \(\dim W=1\), so the conclusion is immediate.

Finally, the line \(\mathbb Rv\) is unique: if \(u\wedge W=0\) and \(u,v\) were linearly independent, one could choose \(r-1\) further vectors so that their wedge with \(u\wedge v\) is nonzero, contradicting \(u\wedge W=0\).

---

## 4. Why the strict inequality is necessary

At the boundary \(n=2r\), the characterization is false for every \(r\ge2\). Let \(H\) be a hyperplane of \(V\), so \(\dim H=2r-1\), and take
\[
W=\bigwedge^rH.
\]
Then
\[
W\wedge W\subseteq\bigwedge^{2r}H=0,
\]
and
\[
\dim W=\binom{2r-1}{r}
      =\binom{2r-1}{r-1}.
\]
However, \(W\) is not of the form \(v\wedge\bigwedge^{r-1}V\): no nonzero vector \(v\) annihilates all of \(\bigwedge^rH\), whereas a star is annihilated by its defining vector.

Thus the proof covers exactly the catalogued strict range \(r<n/2\). The only external input is the established equality case of the Erdős–Ko–Rado theorem; there is no remaining mathematical gap.