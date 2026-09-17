```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "An independently checked Wronskian argument gives a sharper cubic upper bound, and the linear bound is sharp for pencils and an additional genuinely three-dimensional four-term class.",
  "would_publish": false,
  "caveats": "The unrestricted maximum remains undetermined; no literature-priority claim is made."
}
```

# A cubic upper bound and two sharp linear cases

Let \(M_r\) be the maximum number of connected components of
\[
\mathbb R\setminus V(f),\qquad
f(x)=\sum_{i=1}^r c_i\sqrt{q_i(x)},
\]
where \(c_i\in\mathbb R\) and the \(q_i\) are everywhere-positive quadratic polynomials. The results below also allow positive constant polynomials.

Define
\[
B(r)=\frac23(r-1)\bigl((r-1)^2+2\bigr).
\]

I prove
\[
\boxed{
2r-1\le M_r\le
\min\left\{2^{r-1}+1,\;B(r)+1\right\}.
}
\tag{1}
\]
More strongly, every nonzero \(f\) has at most \(B(r)\) real zeros counted with multiplicity.

This independently rederives the main Wronskian estimate in the supplied attempt. Passing to the real projective line removes its additive \(r-1\) loss. For example, at \(r=10\), the resulting component bound is \(499\), rather than \(508\) in that attempt or \(513\) from conjugate multiplication.

I also prove:

* If the quadratics span a space of dimension at most two, then the sharp component bound is \(2r-1\).
* For the genuinely three-dimensional four-term family
  \[
  f=\sqrt{q_1}+\sqrt{q_2}+\sqrt{q_3}-\sqrt{q_4},
  \qquad
  q_1+q_2+q_3=\tau q_4,
  \qquad
  \frac13<\tau\le\frac12,
  \tag{2}
  \]
  the sharp component bound is \(7\).

The unrestricted linear-versus-cubic gap remains open.

---

## 1. A cyclic Rolle inequality

For real-analytic functions, write
\[
W(u,v)=uv'-u'v.
\]
On a circle, let \(\nu(g)\) denote the total multiplicity of the zeros of a nonzero real-analytic function \(g\).

### Lemma 1
If \(u,v\), and \(W(u,v)\) are nonzero real-analytic functions on a circle, then
\[
\nu(v)\le \nu(W(u,v))+\nu(u).
\tag{3}
\]

On an interval, provided the zero counts are finite, the corresponding inequality is
\[
\nu(v)\le \nu(W(u,v))+\nu(u)+1.
\tag{4}
\]

### Proof

Suppose first that \(u\) has \(s>0\) distinct zeros, of multiplicities \(a_1,\ldots,a_s\). Let \(b_j\) be the multiplicity of \(v\) at the \(j\)-th such point, with \(b_j=0\) if \(v\) does not vanish there. Put
\[
A=\sum_j a_j,\qquad B=\sum_j b_j.
\]

Let \(N_0\) count the zeros of \(v\) away from these points, and let \(C\) count the zeros of \(W(u,v)\) away from them. On each of the \(s\) intervening open arcs,
\[
W(u,v)=u^2(v/u)'.
\]
Rolle's theorem, including multiplicities, gives
\[
N_0\le C+s.
\tag{5}
\]

Locally, writing \(u=t^aU\) and \(v=t^bV\), with \(U,V\) nonvanishing, gives
\[
\operatorname{ord}W(u,v)\ge a+b-1.
\]
Consequently,
\[
\nu(W(u,v))\ge C+A+B-s.
\]
Together with (5),
\[
\nu(v)\le C+s+B
\le \nu(W(u,v))-A+2s
\le \nu(W(u,v))+A.
\]

If \(u\) has no zeros, apply cyclic Rolle directly to the periodic function \(v/u\).

For an interval, the zeros of \(u\) leave \(s+1\) subintervals rather than \(s\) arcs. The same argument gives (4). \(\square\)

---

## 2. Wronskians of square roots of quadratics

Write
\[
W(u_1,\ldots,u_k)
=\det\bigl(u_i^{(j)}\bigr)_{\substack{0\le j\le k-1\\1\le i\le k}}.
\]

### Lemma 2
Let \(u_i=\sqrt{q_i}\), where the \(q_i\) are everywhere-positive quadratic polynomials. For \(k\ge2\),
\[
W(u_1,\ldots,u_k)
=
\frac{R_k(x)}
{\prod_{i=1}^k q_i(x)^{\,k-3/2}},
\tag{6}
\]
where \(R_k\) is a polynomial satisfying
\[
\deg R_k\le k(k-1).
\tag{7}
\]

If exactly one \(q_i\) is constant, then
\[
\deg R_k\le k^2-3k+3.
\tag{8}
\]

### Proof

For \(u=\sqrt q\), write
\[
u^{(j)}=P_jq^{1/2-j}.
\]
Here \(P_0=1\), and differentiation gives
\[
P_{j+1}
=qP_j'+\left(\frac12-j\right)q'P_j.
\]
Multiplying the \(i\)-th Wronskian column by \(q_i^{k-3/2}\) therefore produces the polynomial entries
\[
P_{i,j}q_i^{k-1-j},\qquad 0\le j\le k-1.
\]
This proves (6).

For the degree bound, every nonconstant \(u_i\) has a convergent Laurent expansion at \(+\infty\) with exponents in
\[
1,0,-1,-2,\ldots.
\]
The same statement holds for a constant \(u_i\).

For monomials,
\[
W(x^{\lambda_1},\ldots,x^{\lambda_k})
=
\left(\prod_{i<j}(\lambda_j-\lambda_i)\right)
x^{\sum_i\lambda_i-k(k-1)/2}.
\tag{9}
\]
In particular, a term with repeated exponents vanishes. The largest sum of \(k\) distinct available exponents is
\[
1+0-1-\cdots-(k-2)=\frac{k(3-k)}2.
\]
Termwise differentiation and multilinearity of the determinant thus give
\[
W(u_1,\ldots,u_k)=O\!\left(x^{-k(k-2)}\right).
\tag{10}
\]

If all \(q_i\) have degree two, the denominator in (6) has growth
\[
x^{k(2k-3)}.
\]
Hence
\[
\deg R_k\le k(2k-3)-k(k-2)=k(k-1).
\]

With one constant quadratic, its contribution to the denominator's growth disappears, giving
\[
\deg R_k\le (k-1)(2k-3)-k(k-2)=k^2-3k+3.
\]
\(\square\)

### Projective form of the estimate

Suppose now that all the \(q_i\) have degree exactly two. Their homogenizations \(Q_i(X,Y)\) are positive definite. Set
\[
h_i(\theta)=\sqrt{Q_i(\sin\theta,\cos\theta)}.
\]
These are positive, real-analytic, \(\pi\)-periodic functions.

On \(-\pi/2<\theta<\pi/2\), putting \(x=\tan\theta\) gives
\[
h_i(\theta)=\cos\theta\,u_i(x).
\]
The usual Wronskian transformation rule yields
\[
W_\theta(h_1,\ldots,h_k)
=
\cos^{k(2-k)}\theta\,
W_x(u_1,\ldots,u_k).
\]
Using (6), this becomes
\[
W_\theta(h_1,\ldots,h_k)
=
\frac{
\cos^{k(k-1)}\theta\,R_k(\tan\theta)}
{\prod_{i=1}^k Q_i(\sin\theta,\cos\theta)^{\,k-3/2}}.
\tag{11}
\]

The numerator is the homogenization of \(R_k\) to degree \(k(k-1)\), evaluated at \((\sin\theta,\cos\theta)\). Therefore, if the \(h_i\) are linearly independent,
\[
\boxed{
\nu\bigl(W_\theta(h_1,\ldots,h_k)\bigr)\le k(k-1).
}
\tag{12}
\]
This counts zeros on the projective circle, including the point corresponding to \(x=\infty\).

Here the Wronskian is not identically zero because the functions are real analytic and linearly independent. The analytic hypothesis is essential for this familiar implication.

---

## 3. Proof of the cubic upper bound

Discard the identically zero function. Choose a linearly independent subfamily representing \(f\), and discard any zero coefficients in that representation:
\[
f=\sum_{i=1}^m c_i u_i,\qquad c_i\ne0,\qquad m\le r.
\tag{13}
\]

### 3.1. Genuine quadratics

First suppose every \(q_i\) has degree two, and use the projective functions \(h_i\) above. Put
\[
H=\sum_{i=1}^m c_i h_i,
\]
and define
\[
W_k=W(h_1,\ldots,h_k),\qquad W_0=1,
\]
\[
F_k=W(h_1,\ldots,h_{k-1},H).
\]
Thus \(F_1=H\) and \(F_m=c_mW_m\).

The determinantal identity
\[
W\!\left(W(g_1,\ldots,g_\ell,u),
         W(g_1,\ldots,g_\ell,v)\right)
=
W(g_1,\ldots,g_\ell)\,
W(g_1,\ldots,g_\ell,u,v)
\]
gives
\[
W(W_k,F_k)=W_{k-1}F_{k+1},\qquad k<m.
\tag{14}
\]
This is the standard two-by-two minor identity applied to the relevant Wronskian matrix.

All functions occurring in (14) are nonzero. Indeed, \(H\) does not lie in the span of \(h_1,\ldots,h_k\) when \(k<m\).

Applying Lemma 1 and then (14),
\[
\nu(F_k)
\le \nu(F_{k+1})+\nu(W_{k-1})+\nu(W_k).
\]
Iteration gives
\[
\nu(H)
\le
\nu(W_m)+\nu(W_{m-1})
+2\sum_{k=1}^{m-2}\nu(W_k).
\tag{15}
\]

Since \(h_1>0\), \(\nu(W_1)=0\). By (12), for \(m\ge2\),
\[
\begin{aligned}
\nu(H)
&\le m(m-1)+(m-1)(m-2)
   +2\sum_{k=2}^{m-2}k(k-1)\\
&=\frac23(m-1)(m^2-2m+3)\\
&=B(m).
\end{aligned}
\tag{16}
\]
For \(m=1\), the zero count is \(0=B(1)\).

Every finite real zero of \(f\), with its multiplicity, is a zero of \(H\). Thus
\[
\nu_{\mathbb R}(f)\le B(m)\le B(r).
\tag{17}
\]

### 3.2. Positive constants are also covered

An independent family contains at most one constant radical. If one occurs, order it first and use the ordinary interval inequality (4).

For every initial Wronskian of size \(k\ge2\), Lemma 2 gives the bound
\[
E_k=k^2-3k+3,
\qquad E_0=E_1=0.
\]
The same iteration now gives
\[
\nu_{\mathbb R}(f)
\le
(m-1)+E_m+E_{m-1}
+2\sum_{k=2}^{m-2}E_k.
\tag{18}
\]
For \(m\ge3\), the right-hand side equals
\[
B(m)-\bigl(2m^2-9m+11\bigr)
=
B(m)-\bigl((m-3)(2m-3)+2\bigr)
\le B(m).
\]
For \(m=2\), (18) gives \(2=B(2)\); \(m=1\) is immediate.

The finite-zero hypothesis needed here causes no difficulty: all relevant functions are algebraic. A nonzero algebraic function satisfies a polynomial equation \(P(x,g(x))=0\) with \(P(x,0)\not\equiv0\), so its real zeros lie in a finite set.

This completes the proof of (17) in all cases.

### 3.3. The exponential bound, checked directly

For completeness, it is not necessary to take the quoted conjugate-product bound on trust.

For the independent representation (13), with \(m\ge2\), form
\[
P(x)=
\prod_{\varepsilon_2,\ldots,\varepsilon_m\in\{-1,1\}}
\left(c_1u_1+\sum_{i=2}^m\varepsilon_i c_i u_i\right).
\]
As a formal expression in \(c_i u_i\), this product is invariant under changing the sign of any one variable. It is consequently a polynomial in the quantities \(c_i^2q_i(x)\), of degree at most \(2^{m-1}\) in \(x\).

No factor is identically zero, by independence, so \(P\not\equiv0\). Since \(f\) is one factor,
\[
\nu_{\mathbb R}(f)\le 2^{m-1}.
\]

Combining this with (17), and observing that a nonzero \(f\) has one more complementary component than distinct real zeros, proves the upper bound in (1).

---

## 4. Exact solution for a two-dimensional pencil

### Theorem 3
If
\[
\dim\operatorname{span}_{\mathbb R}\{q_1,\ldots,q_r\}\le2,
\]
then every nonzero \(f\) has at most \(2r-2\) real zeros, counted with multiplicity. The resulting component bound \(2r-1\) is sharp.

### Proof

The one-dimensional case is immediate. In dimension two, normalize the polynomials by their values at \(0\). After combining proportional terms, write
\[
q_i=\lambda_i(p+a_i s),
\]
where \(p>0\), the \(a_i\) are distinct, and \(\lambda_i>0\).

Set
\[
t(x)=\frac{s(x)}{p(x)},\qquad d_i=c_i\sqrt{\lambda_i}.
\]
Then
\[
f(x)=\sqrt{p(x)}\,F(t(x)),
\qquad
F(y)=\sum_i d_i\sqrt{1+a_i y}.
\tag{19}
\]
The range of \(t\) lies in the interval
\[
J=\{y:1+a_i y>0\text{ for every }i\}.
\]

For \(\psi_i(y)=\sqrt{1+a_i y}\), let
\[
\alpha_j=\prod_{\ell=0}^{j-1}\left(\frac12-\ell\right),
\qquad \alpha_0=1.
\]
Then
\[
\psi_i^{(j)}(y)
=
\alpha_j\psi_i(y)
\left(\frac{a_i}{1+a_i y}\right)^j.
\]
Thus each initial Wronskian is a nonzero Vandermonde determinant, since
\[
\frac{a_\ell}{1+a_\ell y}-\frac{a_i}{1+a_i y}
=
\frac{a_\ell-a_i}{(1+a_i y)(1+a_\ell y)}.
\]
The interval version of the Wronskian/Rolle iteration therefore gives at most \(r-1\) zeros of \(F\) in \(J\), counted with multiplicity.

For any fixed \(y_0\), the equation \(t(x)=y_0\) is
\[
s(x)-y_0p(x)=0.
\]
It is a nonzero polynomial equation of degree at most two. Counting multiplicities in the composition (19) gives at most twice the zero count of \(F\), hence at most \(2r-2\).

### Sharpness

Take
\[
q_i(x)=1+i x^2,\qquad 1\le i\le r.
\]
For \(r\ge2\), form the \((r-1)\times r\) matrix
\[
A_{ji}=\sqrt{1+ij},
\qquad 1\le j\le r-1.
\]
Let \(d_i=(-1)^i\det A_{\widehat i}\), where \(A_{\widehat i}\) deletes column \(i\).

The just-proved Chebyshev property implies every maximal minor is nonzero. Hence \(d\ne0\), \(Ad=0\), and
\[
f(x)=\sum_{i=1}^r d_i\sqrt{1+i x^2}
\]
vanishes at
\[
x=\pm\sqrt j,\qquad 1\le j\le r-1.
\]
These are \(2r-2\) distinct roots. The upper bound shows there are no others. This proves both sharpness and the lower bound in (1). \(\square\)

---

## 5. A sharp four-term case beyond pencils

The next result is not confined to a two-dimensional span.

### Theorem 4
Suppose
\[
f=\sqrt{q_1}+\sqrt{q_2}+\sqrt{q_3}-\sqrt{q_4},
\]
where the \(q_i\) are everywhere positive and
\[
q_1+q_2+q_3=\tau q_4,
\qquad \frac13<\tau\le\frac12.
\tag{20}
\]
Then every nonzero \(f\) has at most six distinct real zeros. The bound is attained by families whose quadratics span the full three-dimensional space of quadratic polynomials.

### Proof

The pencil case follows from Theorem 3, so assume the span has dimension three. In particular, \(q_4\) is a genuine quadratic.

Homogenize and make an invertible real linear change of the two homogeneous coordinates so that \(Q_4=X^2+Y^2\). The normalized quantities
\[
v_i=\frac{Q_i}{Q_4},\qquad i=1,2,3,
\]
then trace a nondegenerate ellipse \(E\) in the plane
\[
v_1+v_2+v_3=\tau
\]
as the real projective parameter varies. Indeed, on the unit circle each \(v_i\) is an affine combination of \(1,\cos t,\sin t\), and the dimension-three assumption makes the resulting ellipse nondegenerate.

At a zero of \(f\), put \(u_i=\sqrt{v_i}\). Then
\[
u_1+u_2+u_3=1,
\qquad
u_1^2+u_2^2+u_3^2=\tau.
\]
This circle has the parametrization
\[
u_j=\frac13+R\cos\left(\phi+\frac{2\pi j}{3}\right),
\qquad j=0,1,2,
\tag{21}
\]
where
\[
R=\sqrt{\frac23\left(\tau-\frac13\right)}
\quad\text{satisfies}\quad 0<R\le\frac13.
\]
All the coordinates in (21) are therefore nonnegative.

Let \(\Gamma\) be the curve \(v_j=u_j^2\). The projective zeros of \(f\) correspond to intersections \(E\cap\Gamma\).

Use the complex coordinate
\[
z=\sum_{j=0}^2 v_j\omega^j,\qquad \omega=e^{2\pi i/3}.
\]
Expanding (21), and writing \(w=e^{-i\phi}\), gives
\[
z=aw+bw^{-2},
\qquad
a=R,\qquad b=\frac{3R^2}{4}.
\tag{22}
\]
In particular,
\[
0<b\le \frac a4.
\tag{23}
\]

Every nondegenerate ellipse has an equation
\[
|z|^2+\operatorname{Re}(\beta z^2)
+2\operatorname{Re}(\gamma z)+\delta=0,
\qquad |\beta|<1.
\tag{24}
\]
Substitute (22) into (24), for \(|w|=1\), obtaining a real trigonometric polynomial \(T\) of degree at most four.

If \(\beta=0\), its degree is at most three, so it has at most six zeros counted with multiplicity.

Suppose \(\beta\ne0\). Then
\[
P(w)=w^4T(w)
\]
is a degree-eight polynomial. Its leading two coefficients are
\[
[w^8]P=\frac{b^2}{2}\overline\beta,
\qquad
[w^7]P=ab.
\tag{25}
\]
In particular, \(T\not\equiv0\).

The total multiplicity of the zeros of a nonzero real-analytic periodic function is even. Thus, if \(T\) had more than six zeros counted with multiplicity on the circle, all eight roots of \(P\) would lie on the unit circle. Vieta's formula would then imply
\[
\left|\frac{[w^7]P}{[w^8]P}\right|
=\left|\sum_{\rho:P(\rho)=0}\rho\right|
\le8.
\]
But (23) and (25) give
\[
\left|\frac{[w^7]P}{[w^8]P}\right|
=\frac{2a}{b|\beta|}
\ge\frac8{|\beta|}
>8,
\]
a contradiction.

Hence \(E\cap\Gamma\), and therefore the real projective zero set of \(f\), has at most six points. The affine real zero set has no more. \(\square\)

### A three-dimensional family attaining six zeros

Choose any \(0<R<1/6\), for example \(R=1/12\), and put
\[
\tau=\frac13+\frac{3R^2}{2},\qquad q_4(x)=1+x^2.
\]
For \(j=0,1,2\), define
\[
q_{j+1}(x)
=
\frac{\tau}{3}(1+x^2)
+\frac{2R}{3}
\left(
(1-x^2)\cos\frac{2\pi j}{3}
+2x\sin\frac{2\pi j}{3}
\right).
\tag{26}
\]
These quadratics are positive definite because \(\tau>2R\). They span a three-dimensional space and satisfy (20).

With \(t=2\arctan x\), the ellipse \(E\) in the preceding proof is simply
\[
z=R e^{it}.
\]
Its intersections with \(\Gamma\), where \(a=R\) and \(b=3R^2/4\), satisfy
\[
|aw+bw^{-2}|^2=a^2,
\]
or
\[
\cos(3\phi)=-\frac{b}{2a}=-\frac{3R}{8}.
\]
There are exactly six distinct solutions modulo \(2\pi\).

The parametrization \(w\mapsto aw+bw^{-2}\) is injective on the unit circle when \(a>2b\): if two distinct unit numbers had the same image, division by their difference would give \(a\le2b\). Hence these six solutions give six distinct intersections.

Finally, the omitted affine point \(x=\infty\) corresponds to \(z=-a\). The only real points of \(\Gamma\) are \(a+b\) and \(-a+b\), so none of the six intersections is at infinity. Thus (26) gives exactly six finite real zeros and seven complementary components.

---

## 6. What remains unresolved

The proved general bound is
\[
\boxed{
2r-1\le M_r\le
\min\left\{
2^{r-1}+1,\;
1+\frac23(r-1)\bigl((r-1)^2+2\bigr)
\right\}.
}
\]

The supplied Wronskian approach survives independent checking, and its additive loss can be reduced by working projectively. The additional four-term theorem establishes the linear bound for a non-pencil family.

However:

* the optimal asymptotic growth of \(M_r\) is not determined;
* no superlinear lower-bound construction is obtained;
* even the unrestricted four-term case remains between \(7\) and \(9\) components.

All proved assertions above are self-contained. I make no claim that these bounds or methods are new in the literature.