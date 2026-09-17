```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The univariate bound improves to O_Delta(m r^3), and sums of absolute affine functions admit a sharp O_N((mr)^N) bound in every fixed dimension.",
  "would_publish": false,
  "caveats": "General multivariate radicals remain unresolved, as does the sharp univariate r-exponent; literature novelty has not been established."
}
```

# Polynomial \(r\)-dependence in two cases

I obtain two improvements over the supplied lead:

1. Its univariate \(O_\Delta(mr^4)\) bound can be improved to **\(O_\Delta(mr^3)\)**, independently of the radical order.
2. For sums of absolute affine functions, its \(O_N(m^{2N}r^N)\) bound can be improved to **\(O_N((mr)^N)\)**. An explicit construction shows that this second bound has the correct order in a substantial parameter range.

These do not settle the general multivariate problem.

## 1. Model and statements

Let
\[
F_i(x)=\sum_{j=1}^{r_i}a_{ij}P_{ij}(x)^{1/s},
\qquad 1\le i\le m,\qquad r_i\le r,
\]
where \(a_{ij}\in\mathbb R\), \(s\ge2\) is an integer, and each \(P_{ij}\) is a globally nonnegative polynomial on \(\mathbb R^N\) of degree at most \(\Delta\). Roots are the nonnegative real roots.

Write
\[
\operatorname{Pat}(F)=
\left\{
(\operatorname{sgn}F_1(x),\ldots,\operatorname{sgn}F_m(x)):
F_i(x)\ne0\text{ for every }i
\right\}.
\]

Thus \(r\) is a per-function summand bound. Both upper bounds below also apply when all functions use a common pool of \(r\) radicands.

### Theorem A: one variable

Suppose \(N=1\) and \(\Delta\ge2\), and put
\[
D=2\left\lfloor\frac{\Delta}{2}\right\rfloor.
\]
Define
\[
B_D(r)
=
r-1+\frac{2(D-1)}{3}(r-1)\bigl((r-1)^2+2\bigr).
\]
Then
\[
\boxed{\;
|\operatorname{Pat}(F)|\le 1+mB_D(r).
\;}
\tag{1}
\]

In particular, when \(\Delta=2\),
\[
\boxed{\;
|\operatorname{Pat}(F)|
\le
1+\frac m3\left(2(r-1)^3+7(r-1)\right)
=O(mr^3).
\;}
\tag{2}
\]

If \(\Delta\le1\), the globally nonnegative radicands are constant, so there is at most one proper pattern.

### Theorem B: absolute affine functions

Suppose
\[
F_i(x)=\sum_{j=1}^{r_i}a_{ij}|\ell_{ij}(x)|,
\qquad x\in\mathbb R^N,
\]
where the \(\ell_{ij}\) are affine and \(r_i\le r\). Then
\[
\boxed{\;
|\operatorname{Pat}(F)|
\le
\frac{2^N}{N!}\bigl((1+e)mr+N+1\bigr)^N
=O_N((mr)^N).
\;}
\tag{3}
\]

The same estimate permits an additional arbitrary affine term in each \(F_i\).

### Matching lower bound for Theorem B

For integers \(2\le r\le\mu\), there exist \(m=N\mu\) functions of the above absolute-affine form, each with at most \(r\) summands, such that
\[
\boxed{\;
|\operatorname{Pat}(F)|
\ge
\left(\frac{\mu r}{2}\right)^N
=
\left(\frac{mr}{2N}\right)^N.
\;}
\tag{4}
\]

Thus, for this subclass, the order \(O_N((mr)^N)\) is sharp when \(m=N\mu\) and \(2\le r\le\mu\).

---

# 2. Proof of the univariate bound

The Wronskian factorization suggested in the previous attempt is valid. The improvement comes from counting zeros globally using meromorphic Rolle inequalities, rather than partitioning the line at all Wronskian zeros and paying a factor \(r\) on every interval.

## 2.1. Reduction to positive radicands of a common degree

Choose one witness point for each proper sign pattern of the original family. This gives finitely many points.

Every globally nonnegative univariate polynomial of degree at most \(\Delta\) has degree at most \(D\). Replace every radicand by
\[
P_\varepsilon(x)=P(x)+\varepsilon(1+x^D).
\tag{5}
\]
For \(\varepsilon>0\), this is strictly positive and has degree exactly \(D\).

At each witness point, \(P_\varepsilon^{1/s}\to P^{1/s}\). Hence, for sufficiently small \(\varepsilon\), all witnessed signs are preserved. It therefore suffices to prove the upper bound for strictly positive radicands of degree exactly \(D\).

Consider a nonzero function
\[
G=\sum_j a_jP_j^\alpha,\qquad \alpha=1/s.
\]
Choose a representation of \(G\) using a minimal subcollection of these functions:
\[
G=\sum_{j=1}^q b_jh_j,\qquad h_j=P_j^\alpha,\qquad q\le r.
\tag{6}
\]
Then the \(h_j\) are linearly independent and every \(b_j\ne0\).

Put
\[
W_k=W(h_1,\ldots,h_k),\qquad W_0=1.
\]
Every \(W_k\) is nonzero as an analytic function. Indeed, independent analytic functions have independent analytic germs; constant column operations produce germs with distinct initial Taylor orders, whose Wronskian has a nonzero leading coefficient.

This avoids the generic-independence perturbation used in the previous attempt.

## 2.2. A Wronskian degree bound

For \(h=P^\alpha\), repeated differentiation gives
\[
h^{(\ell)}=P^{\alpha-\ell}Q_\ell,
\tag{7}
\]
where \(Q_\ell\) is polynomial. The recurrence is
\[
Q_{\ell+1}=PQ_\ell'+(\alpha-\ell)P'Q_\ell.
\tag{8}
\]

Factoring \(P_j^{\alpha-k+1}\) from column \(j\) of \(W_k\) therefore gives
\[
W_k=
\left(\prod_{j=1}^kP_j^{\alpha-k+1}\right)R_k
\tag{9}
\]
for a polynomial \(R_k\).

The common degree of the \(P_j\) improves the elementary degree estimate to
\[
\boxed{\;
\deg R_k\le (D-1)k(k-1).
\;}
\tag{10}
\]

Here is a proof of this refinement. Set
\[
\widetilde P_j(t)=t^DP_j(1/t),\qquad
g_j(t)=\widetilde P_j(t)^\alpha.
\]
Since \(\widetilde P_j(0)>0\), the \(g_j\) are analytic near \(0\). For large positive \(x\),
\[
h_j(x)=x^{D\alpha}g_j(1/x).
\]
The common-multiplier and change-of-variable identities for Wronskians give
\[
W_k(x)
=
x^{kD\alpha}(-x^{-2})^{k(k-1)/2}
W(g_1,\ldots,g_k)(1/x).
\]
Consequently,
\[
W_k(x)=O\!\left(x^{kD\alpha-k(k-1)}\right).
\]
Dividing by the prefactor in (9) shows
\[
R_k(x)=O\!\left(x^{(D-1)k(k-1)}\right),
\]
which proves (10).

Let \(z_k\) be the number of real zeros of \(W_k\), counted with multiplicity. Because the prefactor in (9) is analytic and nowhere zero,
\[
z_k\le (D-1)k(k-1).
\tag{11}
\]
In particular, \(z_0=z_1=0\).

## 2.3. A global meromorphic Rolle inequality

For a nonzero real-meromorphic function \(u\) with finitely many real zeros and poles, define
\[
\nu(u)
=
\#\{\text{real zeros, with multiplicity}\}
-
\#\{\text{real poles, with multiplicity}\}.
\]
Let \(p(u)\) denote its number of distinct real poles.

If \(u\) is nonconstant, then
\[
\boxed{\;
\nu(u)\le \nu(u')+2p(u)+1.
\;}
\tag{12}
\]

To see this, split the real line at the \(p(u)\) poles. Rolle's theorem, including multiplicities, gives
\[
Z(u)\le Z(u')+p(u)+1.
\]
At a pole of order \(b\), the derivative has a pole of order \(b+1\). Thus
\[
P(u')=P(u)+p(u),
\]
and subtracting pole multiplicities gives (12).

Also, whenever the quantities are finite,
\[
\nu(uv)=\nu(u)+\nu(v).
\tag{13}
\]

## 2.4. Applying the inequality to successive Wronskian quotients

Assume \(q\ge2\). For \(0\le k\le q-1\), put
\[
U_k
=
\frac{W(h_1,\ldots,h_k,G)}{W_{k+1}},
\tag{14}
\]
where the numerator for \(k=0\) means \(G\). Thus
\[
U_0=G/h_1,\qquad U_{q-1}=b_q.
\]

A determinant identity gives
\[
U_k'
=
\frac{W_kW_{k+2}}{W_{k+1}^2}\,U_{k+1},
\qquad 0\le k\le q-2.
\tag{15}
\]
For completeness, differentiating a Wronskian leaves only the term obtained by differentiating its last row: all other terms have repeated rows. Applying the \(2\times2\) minors identity to the resulting determinants yields (15).

All quotients in (14) are real-meromorphic, with poles only at zeros of their denominators. They are nonzero. Moreover, (15), starting with the nonzero constant \(U_{q-1}\), and Rolle's theorem show by descending induction that all have finitely many real zeros.

Set
\[
A_k=\frac{W_kW_{k+2}}{W_{k+1}^2}.
\]
Then
\[
\nu(A_k)=z_k+z_{k+2}-2z_{k+1},
\qquad
p(U_k)\le z_{k+1}.
\]
Applying (12) and (13) to (15), we obtain
\[
\begin{aligned}
\nu(U_k)
&\le \nu(U_k')+2p(U_k)+1\\
&\le \nu(U_{k+1})+z_k+z_{k+2}+1.
\end{aligned}
\tag{16}
\]

Since \(h_1>0\), \(U_0\) has precisely the zeros of \(G\) and has no real poles. Summing (16), and using \(\nu(U_{q-1})=0\), gives
\[
Z(G)
\le
q-1+\sum_{k=0}^{q-2}(z_k+z_{k+2}).
\tag{17}
\]
By (11),
\[
\begin{aligned}
Z(G)
&\le
q-1+(D-1)
\sum_{k=0}^{q-2}
\bigl(k(k-1)+(k+2)(k+1)\bigr)\\
&=
q-1+\frac{2(D-1)}3
(q-1)\bigl((q-1)^2+2\bigr)\\
&=B_D(q)\le B_D(r).
\end{aligned}
\tag{18}
\]
For \(q=1\), \(G\) is a nonzero multiple of a positive function, so the same conclusion holds with zero zeros.

## 2.5. From zeros to sign patterns

For the positively perturbed family, every \(F_i\) is nonzero as a function, because it remains nonzero at all the chosen witnesses. By (18), the union of their real zero sets contains at most \(mB_D(r)\) points. Its complement therefore has at most
\[
1+mB_D(r)
\]
intervals, and the sign vector is constant on each.

All original proper patterns survive the perturbation. This proves Theorem A.

Notice that this argument does **not** assert that an unperturbed function has finitely many zeros: sums of absolute values can vanish on intervals. The finite-witness perturbation is what handles that degeneracy.

---

# 3. Proof of the sharp absolute-affine upper bound

It is convenient to prove the slightly stronger statement allowing
\[
F_i(x)=b_i+v_i\cdot x+\sum_{j=1}^{r_i}a_{ij}|\ell_{ij}(x)|.
\tag{19}
\]

Let
\[
H_d(t)=\sum_{a=0}^d\binom ta.
\]
An arrangement of \(t\) affine hyperplanes in \(\mathbb R^d\) has at most \(H_d(t)\) chambers, by the usual induction that inserts one hyperplane at a time.

## 3.1. A harmless general-position reduction

Choose one witness for every proper pattern, and take a closed simplex \(K\) containing all witnesses in its interior.

We may make arbitrarily small perturbations preserving their signs such that:

1. the at most \(mr\) input hyperplanes \(\ell_{ij}=0\), together with the \(N+1\) facet hyperplanes of \(K\), are in general position;
2. on every affine piece and every intersection flat of the input and boundary hyperplanes, any nonempty intersection of output zero sets has the expected codimension.

Here is why the second condition is available. After fixing the input hyperplanes, restrict any selected output affine formulas to any selected intersection flat. If the resulting affine map has rank less than the number of selected outputs, the constant shifts for which those outputs have a common zero lie in a proper affine subspace of the space of shifts. There are only finitely many choices of formulas, flats, and outputs. Avoiding this finite union of proper affine subspaces gives the required condition.

The additional affine terms in (19) allow these output shifts without changing the number of absolute-value terms.

Put
\[
H=mr+N+1.
\]

## 3.2. Count cells through their vertices

Partition \(K\) first by all input hyperplanes and then, on every resulting chamber, by the output zero hyperplanes. The full-dimensional cells of this refinement are convex polyhedra.

Every proper pattern has a witness in a full-dimensional cell: a witness on an input hyperplane can be moved slightly off all input hyperplanes while preserving all nonzero output signs. Hence
\[
|\operatorname{Pat}(F)|
\le \#\{\text{full-dimensional cells}\}.
\tag{20}
\]

Each cell closure is a bounded full-dimensional polytope, and so has a vertex.

At a vertex, exactly \(N\) surfaces are active, by the general-position conditions. Suppose \(k\) are input or boundary hyperplanes and \(j\) are output zero sets. Then
\[
k+j=N.
\tag{21}
\]
A vertex belongs to at most \(2^N\) full-dimensional cells: the signs of inactive surfaces are fixed, and each active surface contributes at most two choices. A complete input/output sign vector determines at most one cell, because within an input chamber all output inequalities are affine.

If \(V\) denotes the number of vertices, it follows that
\[
|\operatorname{Pat}(F)|\le 2^N V.
\tag{22}
\]

## 3.3. Count vertices using only the outputs active there

Choose the \(k=N-j\) active input or boundary hyperplanes and the \(j\) active outputs.

The chosen hyperplanes meet in a \(j\)-dimensional affine flat \(L\). The chosen outputs involve at most \(jr\) input hyperplanes. Restricted to \(L\), these divide \(L\) into at most
\[
H_j(jr)
\]
chambers.

A vertex of the selected type lies in one of these relative open chambers: it cannot lie on an additional input hyperplane, because that would give more than \(N\) active surfaces. On each chamber, the \(j\) chosen outputs are affine functions on a \(j\)-dimensional space. The general-position condition gives at most one common zero.

Consequently,
\[
V
\le
\sum_{j=0}^N
\binom mj\binom H{N-j}H_j(jr).
\tag{23}
\]

For \(j\ge1\),
\[
H_j(jr)\le (er)^j,
\]
and the same convention holds for \(j=0\). Thus
\[
\begin{aligned}
V
&\le
\sum_{j=0}^N
\frac{m^j}{j!}
\frac{H^{N-j}}{(N-j)!}
(er)^j\\
&=
\frac{(H+emr)^N}{N!}.
\end{aligned}
\tag{24}
\]
Combining (22) and (24) proves
\[
|\operatorname{Pat}(F)|
\le
\frac{2^N}{N!}
\bigl((1+e)mr+N+1\bigr)^N.
\]

The original, possibly degenerate family has no more patterns than its sign-preserving perturbation, completing the proof.

The important improvement over the previous chamber-by-chamber bound is that a vertex involving \(j\) outputs only requires examining the input hyperplanes belonging to those \(j\) outputs—not all \(m\) outputs.

---

# 4. An explicit matching lower construction

The following construction uses a common set of \(r\) radical functions in one dimension.

Fix
\[
2\le r\le\mu,\qquad L=r-1,
\]
and identify the \(\mu\) output coordinates with \(\mathbb Z/\mu\mathbb Z\).

We construct \(\mu\) piecewise-linear functions on \([0,L]\). At each integer \(t\), all outputs have the same sign, alternating between negative and positive:
\[
g_j(t)=(-1)^{t+1}u_{t,j},\qquad u_{t,j}>0.
\tag{25}
\]

On the segment \([t,t+1]\), prescribe that the coordinates cross zero in cyclic order
\[
t,t+1,\ldots,t+\mu-1\pmod\mu.
\tag{26}
\]

These crossing orders can be realized simultaneously. Set \(u_{0,j}=1\). Choose distinct crossing fractions \(\lambda_{t,j}\in(0,1)\) in the order (26), for example the fractions
\[
\frac1{\mu+1},\frac2{\mu+1},\ldots,\frac{\mu}{\mu+1}.
\]
Then set recursively
\[
u_{t+1,j}
=
u_{t,j}\frac{1-\lambda_{t,j}}{\lambda_{t,j}}.
\tag{27}
\]
Linear interpolation between the two opposite-sign endpoint values crosses zero exactly at \(t+\lambda_{t,j}\).

## 4.1. Counting the distinct patterns

Represent a sign pattern by its set of positive coordinates.

For an even segment \(t\), the \(\mu-1\) intermediate proper subsets are the cyclic intervals
\[
\{t,t+1,\ldots,t+\ell-1\},
\qquad 1\le\ell\le\mu-1.
\tag{28}
\]
For an odd segment \(t\), its intermediate positive subset of size \(\ell\) starts at \(t-\ell\).

Two segments of the same parity have no intermediate pattern in common, since their cyclic starting indices are distinct. An even segment \(a\) and an odd segment \(b\) have exactly one intermediate pattern in common: its cardinality is the unique
\[
\ell\in\{1,\ldots,\mu-1\}
\quad\text{with}\quad
\ell\equiv b-a\pmod\mu.
\]
No intermediate pattern belongs to three segments.

There are \(\lceil L/2\rceil\) even segments and \(\lfloor L/2\rfloor\) odd segments. Including the all-negative and all-positive patterns, the number of distinct patterns is therefore exactly
\[
2+L(\mu-1)-\left\lfloor\frac{L^2}{4}\right\rfloor.
\tag{29}
\]
Since \(L=r-1\) and \(\mu\ge r\ge2\),
\[
2+L(\mu-1)-\left\lfloor\frac{L^2}{4}\right\rfloor
\ge \frac{\mu r}{2}.
\tag{30}
\]

## 4.2. Realization with \(r\) quadratic radicals

Extend each \(g_j\) affinely beyond the two ends of \([0,L]\). Its only possible breakpoints are
\[
1,\ldots,L-1.
\]
Consequently it has a representation
\[
g_j(x)=A_j+B_jx+\sum_{h=1}^{L-1}c_{jh}|x-h|.
\tag{31}
\]
This follows by assigning half the slope jump at \(h\) to \(c_{jh}\).

On \([0,L]\), \(x=|x|\). Thus
\[
F_j(x)
=
A_j+B_j|x|+\sum_{h=1}^{L-1}c_{jh}|x-h|
\tag{32}
\]
has all the patterns counted above. It uses at most
\[
1+1+(L-1)=r
\]
radical summands, since
\[
1=\sqrt1,\qquad |x-h|=\sqrt{(x-h)^2}.
\]
All the radicands are globally nonnegative quadratics or constants. If coefficients are required to be signs, their magnitudes can be absorbed into the radicands.

This proves the univariate lower bound \(\mu r/2\).

For dimension \(N\), put an independent copy on each coordinate \(x_a\), using a disjoint block of \(\mu\) outputs. The choices of sign pattern in the \(N\) blocks are independent, giving
\[
\left(\frac{\mu r}{2}\right)^N
\]
patterns among \(m=N\mu\) functions. This proves (4).

The whole construction uses only \(N(r-1)+1\) distinct unscaled radicands, so a common-pool formulation has the same fixed-\(N\) order after rescaling its radical budget by a constant depending on \(N\).

---

# 5. What this resolves—and what it does not

The verified conclusions are:

- **One variable, arbitrary globally nonnegative radicands of bounded degree:**
  \[
  |\operatorname{Pat}(F)|=O_\Delta(mr^3),
  \]
  uniformly in \(s\).

- **Any fixed dimension, square roots of squares of affine functions:**
  \[
  |\operatorname{Pat}(F)|=O_N((mr)^N),
  \]
  with a matching lower construction when \(2\le r\le m/N\), up to the stated divisibility convention.

The unresolved parts are substantial:

1. For \(N\ge2\) and general radicands—even genuinely positive quadratic radicands with \(s=2\)—no polynomial \(r\)-bound is established here.
2. In one dimension, the demonstrated scale remains
   \[
   \Omega(mr)\quad\text{versus}\quad O_\Delta(mr^3)
   \]
   in a broad nonsaturated regime.
3. The multivariate proof above fundamentally uses affine formulas on polyhedral pieces. The Wronskian proof bounds zeros on a line, but that alone does not bound the topology or simultaneous intersections of multivariate radical zero sets.

Thus this is a precise improvement in two cases, including a sharp result for the absolute-affine subclass, rather than a resolution of the full catalog problem.