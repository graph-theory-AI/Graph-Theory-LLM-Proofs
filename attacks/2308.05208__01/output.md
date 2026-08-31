```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A self-contained Wronskian argument gives a cubic general upper bound and proves that the linear bound 2r-1 is exact when the quadratics span a two-dimensional pencil.",
  "would_publish": false,
  "caveats": "The generic three-dimensional case remains open, and no literature-priority claim is made."
}
```

# Partial resolution: a cubic upper bound

## 1. Statement

Let \(M_r\) be the maximum number of connected components of
\[
\mathbb R\setminus V(f),\qquad
f(x)=\sum_{i=1}^r c_i\sqrt{q_i(x)},
\]
where \(c_i\in\mathbb R\) and each \(q_i\in\mathbb R[x]\) has degree at most \(2\) and is strictly positive on \(\mathbb R\).

I prove
\[
\boxed{
M_r\le
\min\left\{
2^{r-1}+1,\,
\frac{2r^3-6r^2+13r-6}{3}
\right\}.}
\]
Thus the exponential upper bound can be replaced asymptotically by
\[
M_r\le \frac23r^3+O(r^2).
\]

More precisely, every nonzero such \(f\) has at most
\[
\boxed{
\frac{2r^3-6r^2+13r-9}{3}}
\]
real zeros, counted with multiplicity.

I also prove that if
\[
\dim \operatorname{span}_{\mathbb R}\{q_1,\dots,q_r\}\le 2,
\]
then
\[
\#V(f)\le 2r-2,
\]
so the sharp component bound in this pencil case is exactly \(2r-1\).

The global gap therefore becomes
\[
2r-1\le M_r\le
\min\left\{
2^{r-1}+1,\,
\frac{2r^3-6r^2+13r-6}{3}
\right\}.
\]

Throughout, zeros are counted with multiplicity unless explicitly stated otherwise. Since \(f\) is real analytic, a nonzero \(f\) has one more complementary component than distinct real zeros. The identically zero function has empty complement and is harmless.

---

## 2. A Rolle lemma for Wronskians

Write
\[
W(u,v)=uv'-u'v.
\]

### Lemma 2.1
Let \(u,v\) be nonzero real-analytic functions on \(\mathbb R\), with \(W(u,v)\not\equiv0\), and suppose the relevant zero sets are finite. Then
\[
\nu(v)\le \nu(W(u,v))+\nu(u)+1,
\]
where \(\nu(g)\) denotes the number of real zeros of \(g\), counted with multiplicity.

### Proof
Let \(x_1,\dots,x_s\) be the distinct real zeros of \(u\), with multiplicities \(a_1,\dots,a_s\). Let \(b_j\) be the multiplicity of \(v\) at \(x_j\), with \(b_j=0\) if \(v(x_j)\ne0\). Put
\[
A=\sum_j a_j,\qquad B=\sum_j b_j.
\]

Let \(N_0\) be the number, with multiplicity, of zeros of \(v\) away from the \(x_j\). On each component of
\[
\mathbb R\setminus\{x_1,\dots,x_s\},
\]
the function \(v/u\) has exactly the zeros of \(v\). Rolle's theorem, including multiplicities, therefore gives at least
\[
N_0-(s+1)
\]
zeros of \((v/u)'\) away from the \(x_j\). Since
\[
W(u,v)=u^2(v/u)',
\]
if \(C\) is the number of zeros of \(W(u,v)\) away from the \(x_j\), then
\[
N_0\le C+s+1. \tag{2.1}
\]

At \(x_j\), write locally \(u=t^{a_j}U\) and \(v=t^{b_j}V\), where \(U,V\) do not vanish. If \(a_j\ne b_j\), then
\[
\operatorname{ord}_{x_j}W(u,v)=a_j+b_j-1.
\]
If \(a_j=b_j\), then \(W=u^2(v/u)'\) has order at least \(2a_j\), unless it vanishes identically. In either case,
\[
\operatorname{ord}_{x_j}W(u,v)\ge a_j+b_j-1.
\]
Consequently,
\[
\nu(W(u,v))\ge C+A+B-s.
\]
Using (2.1) and \(A\ge s\),
\[
\begin{aligned}
\nu(v)
 &=N_0+B\\
 &\le C+s+1+B\\
 &\le C+A+B-s+A+1\\
 &\le \nu(W(u,v))+\nu(u)+1.
\end{aligned}
\]
This proves the lemma. \(\square\)

---

## 3. Wronskians of square roots of positive quadratics

The key algebraic estimate is the following.

### Lemma 3.1
Let
\[
u_i(x)=\sqrt{q_i(x)},\qquad 1\le i\le k,
\]
where the \(q_i\) are everywhere-positive quadratics, and suppose \(u_1,\dots,u_k\) are linearly independent. Then their Wronskian
\[
W_k=W(u_1,\dots,u_k)
\]
has at most
\[
k(k-1)
\]
real zeros, counted with multiplicity.

### Proof

Positive scalar multiples of the \(q_i\) only rescale columns of the Wronskian. Thus every nonconstant \(q_i\) may be normalized as
\[
q_i(x)=(x-h_i)^2+s_i^2,\qquad s_i>0.
\]

For \(u=\sqrt q\), write
\[
u^{(j)}=P_jq^{1/2-j},
\]
where
\[
P_0=1,\qquad
P_{j+1}=qP_j'+\left(\frac12-j\right)q'P_j.
\]
Hence, for \(k\ge2\), multiplying the \(i\)-th Wronskian column by \(q_i^{k-3/2}\) gives polynomial entries
\[
P_{i,j}q_i^{k-1-j},\qquad 0\le j\le k-1.
\]
It follows that
\[
W_k(x)=\frac{R_k(x)}
{\prod_{i=1}^k q_i(x)^{k-3/2}}                 \tag{3.1}
\]
for some real polynomial \(R_k\).

It remains to bound \(\deg R_k\). As \(x\to+\infty\),
\[
u_i(x)
=x\left(1-\frac{2h_i}{x}
+\frac{h_i^2+s_i^2}{x^2}\right)^{1/2},
\]
so \(u_i\) has a convergent Laurent expansion whose exponents belong to
\[
1,0,-1,-2,\dots .
\]

For real numbers \(\lambda_1,\dots,\lambda_k\),
\[
W(x^{\lambda_1},\dots,x^{\lambda_k})
=
\left(\prod_{i<j}(\lambda_j-\lambda_i)\right)
x^{\sum_i\lambda_i-k(k-1)/2},
\]
up to an irrelevant sign. A term vanishes if two \(\lambda_i\) coincide. The largest sum of \(k\) distinct exponents chosen from
\[
1,0,-1,-2,\dots
\]
is
\[
1+0-1-\cdots-(k-2)=\frac{k(3-k)}2.
\]
Therefore
\[
W_k(x)=O\!\left(x^{-k(k-2)}\right).             \tag{3.2}
\]

The denominator in (3.1) grows as
\[
x^{k(2k-3)}.
\]
Combining this with (3.2) gives
\[
R_k(x)=O\!\left(x^{k(2k-3)-k(k-2)}\right)
      =O\!\left(x^{k(k-1)}\right).
\]
Thus
\[
\deg R_k\le k(k-1).
\]

A positive polynomial of degree less than \(2\) is constant. An independent family contains at most one constant radical; repeating the same argument then gives the still smaller estimate
\[
\deg R_k\le k^2-3k+3\le k(k-1).
\]

Finally, linearly independent real-analytic functions have a Wronskian that is not identically zero. Thus \(R_k\not\equiv0\). Since every \(q_i\) is positive on \(\mathbb R\), the denominator in (3.1) has no real zeros, and hence
\[
\nu(W_k)\le\deg R_k\le k(k-1).
\]
\(\square\)

---

## 4. Proof of the cubic bound

After passing to a maximal linearly independent subfamily and removing basis functions having zero coefficient in the resulting representation, write
\[
f=\sum_{i=1}^m c_i u_i,
\qquad c_i\ne0,
\qquad m\le r,
\]
where the \(u_i=\sqrt{q_i}\) are linearly independent. Every \(u_i\) is strictly positive.

Set
\[
W_k=W(u_1,\dots,u_k),\qquad W_0=1,
\]
and
\[
F_k=W(u_1,\dots,u_{k-1},f),\qquad 1\le k\le m.
\]
Thus \(F_1=f\), while
\[
F_m=c_mW_m.
\]

The Sylvester identity for Wronskians gives, up to sign,
\[
W(W_k,F_k)=W_{k-1}F_{k+1},
\qquad 1\le k<m.                              \tag{4.1}
\]
Indeed, this is the determinant identity
\[
W\!\left(
W(g_1,\dots,g_\ell,u),
W(g_1,\dots,g_\ell,v)
\right)
=
W(g_1,\dots,g_\ell)\,
W(g_1,\dots,g_\ell,u,v)
\]
with \(g_1,\dots,g_\ell=u_1,\dots,u_{k-1}\).

All functions in (4.1) are nonzero: for \(k<m\), \(f\) does not belong to the span of \(u_1,\dots,u_k\). Applying Lemma 2.1 to \(u=W_k\) and \(v=F_k\), and then using (4.1), yields
\[
\nu(F_k)
\le
\nu(F_{k+1})+\nu(W_{k-1})+\nu(W_k)+1.          \tag{4.2}
\]

Iterating (4.2),
\[
\nu(f)
\le
\nu(W_m)+(m-1)
+\sum_{k=1}^{m-1}
\bigl(\nu(W_{k-1})+\nu(W_k)\bigr).             \tag{4.3}
\]

By Lemma 3.1,
\[
\nu(W_k)\le D_k:=k(k-1),
\qquad D_0=D_1=0.
\]
Substitution into (4.3) gives
\[
\begin{aligned}
\nu(f)
&\le (m-1)+D_m
 +\sum_{k=1}^{m-1}(D_{k-1}+D_k)\\
&=(m-1)+m(m-1)
 +\frac{(m-2)^3-(m-2)}3
 +\frac{(m-1)^3-(m-1)}3\\
&=\frac{2m^3-6m^2+13m-9}{3}.
\end{aligned}
\]
This formula also gives \(0\) when \(m=1\).

The corresponding number of complementary components is therefore at most
\[
\frac{2m^3-6m^2+13m-6}{3}.
\]
This expression is increasing in \(m\), since its increment from \(m\) to \(m+1\) is
\[
2m^2-2m+3>0.
\]
As \(m\le r\), the claimed bound follows:
\[
M_r\le
\frac{2r^3-6r^2+13r-6}{3}.
\]

Combining this with the quoted conjugate-product bound gives
\[
M_r\le
\min\left\{
2^{r-1}+1,\,
\frac{2r^3-6r^2+13r-6}{3}
\right\}.
\]
Numerically, the cubic estimate first improves the quoted exponential one at \(r=10\):
\[
508<513.
\]

---

## 5. Exact solution when the quadratics span a pencil

### Theorem 5.1
Suppose
\[
\dim\operatorname{span}\{q_1,\dots,q_r\}\le2.
\]
Then every nonzero linear combination
\[
f=\sum_{i=1}^r c_i\sqrt{q_i}
\]
has at most \(2r-2\) distinct real zeros. This is sharp.

### Proof

The one-dimensional span case is immediate, so assume the span has dimension \(2\). Since \(q_i(0)>0\), normalize by evaluation at \(0\). There exist a positive quadratic \(p\), a quadratic \(s\), positive numbers \(\lambda_i\), and distinct real parameters \(a_i\), after combining proportional terms, such that
\[
q_i=\lambda_i(p+a_i s).
\]
Indeed, take \(p=q_1/q_1(0)\); all normalized polynomials \(q_i/q_i(0)\) lie on the affine line obtained by intersecting the two-dimensional span with the hyperplane \(q(0)=1\).

Set
\[
t(x)=\frac{s(x)}{p(x)},\qquad
d_i=c_i\sqrt{\lambda_i}.
\]
Then
\[
f(x)=\sqrt{p(x)}\,F(t(x)),
\qquad
F(y)=\sum_i d_i\sqrt{1+a_i y}.                \tag{5.1}
\]

Consider
\[
\psi_i(y)=\sqrt{1+a_i y}
\]
on an interval where all radicands are positive. If
\[
\alpha_j=\left(\frac12\right)
\left(\frac12-1\right)\cdots
\left(\frac12-j+1\right),
\]
then
\[
\psi_i^{(j)}(y)
=
\alpha_j\psi_i(y)
\left(\frac{a_i}{1+a_i y}\right)^j.
\]
Consequently,
\[
\begin{aligned}
W(\psi_1,\dots,\psi_k)
&=
\left(\prod_{j=0}^{k-1}\alpha_j\right)
\left(\prod_{i=1}^k\psi_i(y)\right)\\
&\quad{}\times
\prod_{i<\ell}
\left(
\frac{a_\ell}{1+a_\ell y}
-
\frac{a_i}{1+a_i y}
\right).
\end{aligned}
\]
But
\[
\frac{a_\ell}{1+a_\ell y}
-
\frac{a_i}{1+a_i y}
=
\frac{a_\ell-a_i}
{(1+a_i y)(1+a_\ell y)},
\]
so every initial Wronskian is nonzero.

Thus \(\{\psi_i\}\) is an extended complete Chebyshev system: every nonzero linear combination \(F\) has at most \(r-1\) zeros, counted with multiplicity, on the relevant \(y\)-interval. This follows directly by induction from Rolle's theorem after dividing by \(\psi_1\).

For each zero \(y_0\) of \(F\), its preimages under \(t\) satisfy
\[
s(x)-y_0p(x)=0,
\]
a polynomial equation of degree at most \(2\). Since \(t\) is nonconstant in the two-dimensional case, it has at most two real solutions. Hence
\[
\#V(f)\le 2(r-1).
\]

### Sharpness

Take
\[
q_i(x)=1+i x^2,\qquad 1\le i\le r.
\]
These quadratics span \(\operatorname{span}\{1,x^2\}\). Let
\[
A_{ji}=\sqrt{1+ij},
\qquad
1\le j\le r-1,\quad 1\le i\le r.
\]
Let \(d=(d_1,\dots,d_r)\) be the signed maximal-minor vector of this \((r-1)\times r\) matrix, so \(Ad=0\). The Chebyshev property above implies every maximal minor is nonzero, hence all \(d_i\ne0\).

Then
\[
f(x)=\sum_{i=1}^r d_i\sqrt{1+i x^2}
\]
vanishes at
\[
x=\pm\sqrt{j},
\qquad 1\le j\le r-1.
\]
These are \(2r-2\) distinct roots. The Chebyshev bound shows there are no further roots and that the corresponding roots in \(x^2\) are simple. Therefore
\[
\#\pi_0(\mathbb R\setminus V(f))=2r-1.
\]
This proves sharpness in the pencil case. \(\square\)

---

## 6. Remaining gap

The argument leaves the genuinely generic case
\[
\dim\operatorname{span}\{q_1,\dots,q_r\}=3
\]
unresolved. In particular, it neither proves that the global maximum is \(2r-1\) nor produces any superlinear construction.

The current outcome is therefore the strict asymptotic narrowing
\[
\boxed{
2r-1
\le M_r
\le
\frac{2r^3-6r^2+13r-6}{3}
=
\frac23r^3+O(r^2).}
\]

The Wronskian estimate is likely not optimal: it separately charges the real zeros of all initial Wronskians. Improving the cubic bound would require exploiting additional relations among those Wronskians or the fact that all \(q_i\) belong to the three-dimensional space of quadratic polynomials. I have not established such a relation.