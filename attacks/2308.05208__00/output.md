```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A Wronskian argument replaces the exponential dependence on r by O(r^4) when N=1 and gives polynomial bounds in further special cases, but the general multivariate problem remains open.",
  "would_publish": false,
  "caveats": "The general case N>=2 and the sharp r-exponent even for N=1 are not resolved."
}
```

# Mathematical writeup

## 1. Interpretation

The catalog item is a research direction rather than a formally quantified conjecture. I interpret it as asking whether the exponential dependence on the number \(r\) of radical summands in Theorem 2.2 can be replaced by a polynomial dependence while retaining polynomial dependence on the number \(m\) of functions.

I prove three partial results:

1. For \(N=1\), the number of proper sign patterns is \(O_\Delta(mr^4)\), independently of the radical order \(s\ge 2\).
2. In arbitrary dimension, the desired polynomial dependence holds when the radicands are squares of affine functions.
3. There is a direct lower construction giving \(\Omega_N((mr)^N)\) sign patterns in the relevant nonsaturated regime, showing that a linear factor \(r\) inside a Warren-type \(N\)-th power is genuinely necessary.

The first result is the main new upper bound.

---

## 2. A polynomial \(r\)-bound for \(N=1\)

Let
\[
F_i(x)=\sum_{j=1}^{r_i}a_{ij}P_{ij}(x)^{1/s},
\qquad r_i\le r,
\tag{2.1}
\]
where \(s\ge2\), \(a_{ij}\in\mathbb R\), and every \(P_{ij}\in\mathbb R[x]\) is nonnegative on \(\mathbb R\) and has degree at most \(\Delta\). The principal nonnegative \(s\)-th root is intended.

For \(F=(F_1,\dots,F_m)\), write
\[
\operatorname{Pat}(F)
 =
 \left\{
 (\operatorname{sgn}F_1(x),\dots,\operatorname{sgn}F_m(x)):
 F_i(x)\ne0\ \forall i
 \right\}.
\]

### Theorem 2.1

For \(\Delta\ge2\),
\[
\boxed{
|\operatorname{Pat}(F)|
\le
1+m\left(
r-1+\frac{(2\Delta-1)r^2(r^2-1)}6
\right).
}
\tag{2.2}
\]

In particular, for the quadratic square-root case \(\Delta=s=2\),
\[
|\operatorname{Pat}(F)|
\le
1+m\left(
\frac{r^2(r^2-1)}2+r-1
\right)
=O(mr^4).
\tag{2.3}
\]

Thus the exponential dependence on \(r\) can be replaced by a polynomial one in dimension one.

### 2.1. Wronskian degree bound

Put \(\alpha=1/s\). Let \(P\) be strictly positive and of degree at most \(\Delta\), and set \(h=P^\alpha\). For every \(\ell\ge0\),
\[
h^{(\ell)}=P^{\alpha-\ell}Q_\ell,
\tag{2.4}
\]
where \(Q_\ell\) is a polynomial satisfying
\[
\deg Q_\ell\le \ell(\Delta-1).
\tag{2.5}
\]

Indeed, \(Q_0=1\), and differentiation gives the recurrence
\[
Q_{\ell+1}=P Q_\ell'+(\alpha-\ell)P'Q_\ell.
\]

Now consider \(k\) functions
\[
h_j=P_j^\alpha,\qquad 1\le j\le k,
\]
with all \(P_j>0\). Their Wronskian is
\[
W_k=W(h_1,\dots,h_k)
 =\det\bigl(h_j^{(\ell)}\bigr)_
 {0\le\ell\le k-1,\ 1\le j\le k}.
\]

Factoring \(P_j^{\alpha-(k-1)}\) from column \(j\) yields
\[
W_k(x)=
\left(\prod_{j=1}^kP_j(x)^{\alpha-(k-1)}\right)R_k(x),
\tag{2.6}
\]
where \(R_k\) is a polynomial. In row \(\ell\), an entry of the remaining determinant has degree at most
\[
(k-1-\ell)\Delta+\ell(\Delta-1)
  =\Delta(k-1)-\ell.
\]
Consequently,
\[
\deg R_k
\le
\sum_{\ell=0}^{k-1}\bigl(\Delta(k-1)-\ell\bigr)
=
\left(\Delta-\frac12\right)k(k-1).
\tag{2.7}
\]

Thus, whenever \(W_k\not\equiv0\), it has at most
\[
\left(\Delta-\frac12\right)k(k-1)
\tag{2.8}
\]
distinct real zeros.

### 2.2. A standard Chebyshev-system lemma

We use the following elementary form of the Wronskian criterion.

**Lemma 2.2.**  
Let \(h_1,\dots,h_q\) be real analytic on an interval \(I\). If
\[
W(h_1,\dots,h_k)(x)\ne0
\quad
\text{for every }x\in I,\ 1\le k\le q,
\tag{2.9}
\]
then every nonzero linear combination of \(h_1,\dots,h_q\) has at most \(q-1\) distinct zeros in \(I\).

**Proof.** Induct on \(q\). Since \(h_1\) is nowhere zero, divide a linear combination \(H\) by \(h_1\) and differentiate. The resulting function is a linear combination of
\[
u_j=\left(\frac{h_{j+1}}{h_1}\right)',
\qquad 1\le j\le q-1.
\]
The determinant identity
\[
W(u_1,\dots,u_k)
=
\frac{W(h_1,\dots,h_{k+1})}{h_1^{k+1}}
\tag{2.10}
\]
shows that the \(u_j\) satisfy the same hypothesis. If \(H\) has \(z\) distinct zeros, Rolle's theorem gives at least \(z-1\) zeros of \((H/h_1)'\). Induction gives \(z-1\le q-2\). ∎

### 2.3. Counting zeros in the generic case

Suppose now that \(P_1,\dots,P_q\) are strictly positive and that every initial Wronskian \(W_k\) is not identically zero.

Let \(T\) be the union of the real zero sets of \(W_1,\dots,W_q\). By (2.7),
\[
|T|
\le
\left(\Delta-\frac12\right)
\sum_{k=1}^q k(k-1)
=
\left(\Delta-\frac12\right)\frac{q(q^2-1)}3.
\tag{2.11}
\]

On each of the \(|T|+1\) components of \(\mathbb R\setminus T\), Lemma 2.2 shows that a nonzero linear combination
\[
G=\sum_{j=1}^q a_jP_j^\alpha
\]
has at most \(q-1\) zeros. Allowing also zeros at points of \(T\),
\[
\begin{aligned}
Z(G)
&\le (q-1)(|T|+1)+|T|\\
&=q|T|+q-1\\
&\le
q-1+\frac{(2\Delta-1)q^2(q^2-1)}6.
\end{aligned}
\tag{2.12}
\]

This is the asserted per-function bound.

### 2.4. Removing the genericity hypothesis

This step is necessary: degenerate sums of absolute values can vanish identically on an interval.

We claim that any tuple of nonnegative radicands can be approximated by strictly positive radicands for which all initial Wronskians are nonzero as analytic functions.

Let \(D=2\lfloor\Delta/2\rfloor\), the largest even integer at most \(\Delta\). Consider the open convex cone of strictly positive, coercive polynomials of degree at most \(D\). Every globally nonnegative polynomial of degree at most \(\Delta\) lies in its closure, since
\[
P_\varepsilon(x)=P(x)+\varepsilon(1+x^D)
\]
is strictly positive for \(\varepsilon>0\).

For distinct positive constants \(c_1,\dots,c_q\), the functions
\[
(x^2+c_j)^\alpha,\qquad 1\le j\le q,
\tag{2.13}
\]
are linearly independent. Indeed, if their linear combination vanishes, then for large \(z=x^2\),
\[
0=\sum_j b_j(z+c_j)^\alpha
=z^\alpha
\sum_{n\ge0}\binom{\alpha}{n}z^{-n}
\left(\sum_j b_jc_j^n\right).
\]
Since \(0<\alpha<1\), all \(\binom{\alpha}{n}\) are nonzero. The first \(q\) resulting moment equations form a Vandermonde system, forcing all \(b_j=0\).

Therefore the relevant Wronskians are not identically zero for at least one tuple of positive radicands. Evaluating each Wronskian at a point where it is nonzero gives a nonzero real-analytic function of the polynomial coefficients. Its nonvanishing locus is dense in the connected positive cone. Intersecting these finitely many dense open sets proves the generic approximation claim.

Finally, let \(\Sigma=\operatorname{Pat}(F)\). Choose one point \(x_\sigma\) realizing each \(\sigma\in\Sigma\). There are finitely many such points and all \(F_i(x_\sigma)\) are nonzero. Approximate all radicands by generic strictly positive ones sufficiently closely that all these signs are preserved. Hence
\[
|\operatorname{Pat}(F)|
\le
|\operatorname{Pat}(\widetilde F)|.
\tag{2.14}
\]

Each generic \(\widetilde F_i\) has at most
\[
B_\Delta(r)
=
r-1+\frac{(2\Delta-1)r^2(r^2-1)}6
\]
zeros. The complement of the union of all zero sets has at most \(1+mB_\Delta(r)\) intervals, and the sign vector is constant on each. This proves Theorem 2.1. ∎

---

## 3. An arbitrary-dimensional polynomial case

The exponential \(r\)-dependence is also unnecessary in arbitrary dimension when every radicand is the square of an affine function.

### Proposition 3.1

Let
\[
F_i(x)=\sum_{j=1}^{r_i}a_{ij}|\ell_{ij}(x)|,
\qquad x\in\mathbb R^N,\quad r_i\le r,
\tag{3.1}
\]
where each \(\ell_{ij}\) is affine. Define
\[
H_N(t)=\sum_{k=0}^N\binom{t}{k}.
\]
Then
\[
\boxed{
|\operatorname{Pat}(F)|
\le
H_N(mr)\,H_N(m)
=
O_N(m^{2N}r^N).
}
\tag{3.2}
\]

**Proof.** The at most \(mr\) hyperplanes \(\ell_{ij}=0\) divide \(\mathbb R^N\) into at most \(H_N(mr)\) chambers. Any proper pattern realized on one of these hyperplanes is also realized at a nearby point off all the hyperplanes, since all the \(F_i\) are nonzero at the original point.

On a fixed chamber, every \(|\ell_{ij}|\) is either \(\ell_{ij}\) or \(-\ell_{ij}\). Thus all \(F_i\) restrict to affine functions. The number of their proper sign patterns on that chamber is at most the number of regions of an arrangement of \(m\) affine hyperplanes, namely \(H_N(m)\). Summing over the chambers proves (3.2). ∎

This includes the piecewise-linear absolute-value constructions used in the lower-bound examples, though the exponent of \(m\) in (3.2) is probably not optimal.

---

## 4. A direct \(\Omega((mr)^N)\) lower construction

The catalog notes a linear lower bound in \(r\). The following construction makes the corresponding \(r^N\) dependence explicit in dimension \(N\), without passing to the saturated regime where all \(2^m\) patterns are realized.

### Proposition 4.1

Let \(\mu,r\) be positive integers, put
\[
R=\left\lfloor\frac r6\right\rfloor,
\]
and assume \(1\le R\le\mu-1\). There exist \(\mu\) univariate functions, each a signed sum of at most \(r\) square roots of nonnegative quadratic polynomials, which realize at least
\[
\mu R
\tag{4.1}
\]
proper sign patterns.

Consequently, in \(\mathbb R^N\), there are \(M=N\mu\) such functions realizing at least
\[
\boxed{
(\mu R)^N
}
\tag{4.2}
\]
proper sign patterns.

### Proof

Identify the \(\mu\) sign coordinates with \(\mathbb Z/\mu\mathbb Z\). For
\[
1\le \ell\le R,\qquad 0\le t\le\mu-1,
\]
let
\[
S_{\ell,t}=\{t,t+1,\dots,t+\ell-1\}\pmod\mu.
\tag{4.3}
\]
These \(\mu R\) subsets are distinct.

List them in lexicographic order in \((\ell,t)\), and assign to each subset its incidence vector in \(\{\pm1\}^{\mu}\). For a fixed coordinate:

- during the \(\mu\) cyclic intervals of a fixed length \(\ell\), membership changes at most twice;
- between consecutive length-blocks, it changes at most once.

Thus each coordinate changes sign at most
\[
2R+(R-1)=3R-1
\tag{4.4}
\]
times along this list.

Place the \(\mu R\) sign vectors at consecutive integer sample points. For each coordinate, interpolate its \(\pm1\) values by a continuous piecewise-linear function, constant outside the sample range. If that coordinate changes sign \(e\) times, its slope changes at no more than \(2e\) points. Hence it has a representation
\[
A+Bx+\sum_{h=1}^{b}c_h|x-\tau_h|,
\qquad b\le2e.
\tag{4.5}
\]
On the nonnegative sample range, the affine term uses at most two further radical summands because
\[
A+Bx=(A-B)+B|x+1|.
\]
Moreover,
\[
c|x-\tau|
=
\operatorname{sgn}(c)\sqrt{c^2(x-\tau)^2},
\]
and a constant is likewise a signed square root of a nonnegative constant polynomial. Therefore the number of radical terms is at most
\[
2e+2\le 2(3R-1)+2=6R\le r.
\tag{4.6}
\]
At the sample points the constructed functions take precisely the prescribed values \(\pm1\), proving (4.1).

For the \(N\)-dimensional assertion, put an independent copy of this construction on each coordinate \(x_a\), using disjoint blocks of \(\mu\) functions. The choices on the \(N\) coordinates are independent, giving \((\mu R)^N\) distinct patterns. ∎

For \(r\ge12\) and \(\mu\ge r\),
\[
(\mu R)^N\ge\left(\frac{\mu r}{12}\right)^N
=
\left(\frac{Mr}{12N}\right)^N.
\tag{4.7}
\]
Thus any Warren-shaped upper bound
\[
C_N\bigl(M\,g(r)\bigr)^N
\]
must satisfy \(g(r)=\Omega_N(r)\). Equivalently, the natural multivariate lower dependence is \(r^N\), i.e. linear \(r\) inside the \(N\)-th power.

---

## 5. What remains open

The results above do not settle the source problem.

- For general \(N\ge2\) and genuinely non-square positive radicands, no polynomial \(r\)-bound is proved here.
- In dimension one, the bounds are
  \[
  \Omega(mr)
  \quad\text{versus}\quad
  O_\Delta(mr^4)
  \]
  in a broad parameter regime, so even the univariate sharp exponent remains open.
- The Wronskian argument is intrinsically one-dimensional. Bounding intersections with lines does not by itself control the number of components of a hypersurface in higher dimensions.
- Proposition 3.1 handles all dimensions but only for piecewise-affine radical expressions and has an extra factor \(m^N\) compared with the expected Warren scale.

Hence this is precise progress toward closing the exponential-versus-linear gap, not a resolution of the full catalog item.