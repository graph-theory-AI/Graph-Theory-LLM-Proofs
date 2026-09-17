```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I prove linear induced removal for non-affine polynomial-identity families of arbitrarily high Cauchy–Schwarz complexity, uniformly over finite abelian groups.",
  "would_publish": false,
  "caveats": "Only special algebraic forbidden families are handled; arbitrary-pattern removal and the interval-Z direction remain unresolved, and novelty is not claimed."
}
```

# 1. The partial result

I take a different route from the previous attempt, using neither a safe color nor an ordinary removal lemma.

The special case is this:

> Color the nonzero points of \(\mathbb F_2^n\) with \(0,1\), and forbid every odd-parity coloring of a punctured \(k\)-dimensional linear subspace. If all these forbidden patterns are rare, the coloring is close to a polynomial of degree at most \(k-1\), with zero constant term.

The underlying system has Cauchy–Schwarz complexity exactly \(k-1\). In particular, \(k=3\) gives a non-affine complexity-\(2\) result. Its pattern-free colorings need not be close to constant, and both colors occur in the forbidden family.

I prove a more general theorem, uniform over finite abelian groups.

## Definitions

Let \(G,H\) be finite abelian groups, written additively. We use \(H\) as the color palette.

Fix \(k\ge 2\), and consider the \(m=2^k-1\) forms
\[
L_S(x_1,\ldots,x_k)=\sum_{i\in S}x_i,
\qquad \varnothing\ne S\subseteq[k].
\]
For \(f:G\to H\), define
\[
A_f(h_1,\ldots,h_k)
=
\sum_{\varnothing\ne S\subseteq[k]}
(-1)^{k-|S|}
f\left(\sum_{i\in S}h_i\right).
\tag{1}
\]
The forbidden color words are precisely those for which the alternating sum in (1) is nonzero.

Write
\[
\rho_k(f)=\Pr_{\mathbf h\in G^k}[A_f(\mathbf h)\ne0],
\]
and let
\[
\operatorname{dist}(f,q)
=\frac{|\{x\in G:f(x)\ne q(x)\}|}{|G|}.
\]

For \(h\in G\), set
\[
\Delta_h f(x)=f(x+h)-f(x).
\]
A **normalized polynomial map of degree at most \(k-1\)** is a map \(q:G\to H\) satisfying
\[
q(0)=0,\qquad
\Delta_{h_1}\cdots\Delta_{h_k}q(x)=0
\quad\text{for all }x,h_1,\ldots,h_k\in G.
\tag{2}
\]

## Theorem 1: uniform polynomial-identity removal

For every \(k\ge2\), put
\[
C_k=k2^{k+1}.
\]
For every pair of finite abelian groups \(G,H\) and every \(f:G\to H\), there is a normalized polynomial map \(q\) of degree at most \(k-1\) such that
\[
\operatorname{dist}(f,q)\le C_k\rho_k(f).
\tag{3}
\]

If \(\rho_k(f)<1/C_k\), the stronger bound
\[
\operatorname{dist}(f,q)
\le
\frac{2\rho_k(f)}{1-2k\rho_k(f)}
\le 3\rho_k(f)
\tag{4}
\]
holds.

Thus the removal bound is linear in the **total** forbidden-pattern density, with a constant independent of both groups.

### Colored-pattern formulation

Let \(r=|H|\ge2\). There are
\[
K_{r,k}=(r-1)r^{\,2^k-2}
\tag{5}
\]
forbidden color words: after fixing all colors except the one at \(S=[k]\), exactly one remaining color makes (1) zero.

Consequently, if each forbidden word occurs on at most \(\delta |G|^k\) parameter tuples, then all forbidden instances can be eliminated by recoloring at most
\[
C_kK_{r,k}\delta |G|
\tag{6}
\]
points, using the original palette.

The proof is elementary and follows.

# 2. A self-correction lemma for polynomial maps

All probabilities below use independent uniform elements of the indicated finite groups.

## Lemma 2

Let \(f:G\to H\), and put
\[
\tau=
\Pr_{x,h_1,\ldots,h_k}
\bigl[
\Delta_{h_1}\cdots\Delta_{h_k}f(x)\ne0
\bigr].
\]
If
\[
\tau<\frac1{k2^k},
\tag{7}
\]
then there exists \(q:G\to H\) with all \(k\)-fold derivatives identically zero and
\[
\operatorname{dist}(f,q)\le\frac{\tau}{1-k\tau}.
\tag{8}
\]
Here \(q(0)=0\) is not asserted.

### Proof

Write
\[
D_{\mathbf h}f(x)=\Delta_{h_1}\cdots\Delta_{h_k}f(x),
\]
and let \(T_a\) denote translation by \(a\).

### Step 1: concentration at every basepoint

Fix \(x\). Compare \(D_{\mathbf h}f(x)\) and \(D_{\mathbf h'}f(x)\), replacing the directions one at a time.

The identity
\[
\Delta_a-\Delta_b=T_b\Delta_{a-b}
\tag{9}
\]
shows that the difference arising from replacement of direction \(j\) is
\[
\Delta_{h'_1}\cdots\Delta_{h'_{j-1}}
\Delta_{h_j-h'_j}
\Delta_{h_{j+1}}\cdots\Delta_{h_k}
f(x+h'_j).
\]
Its basepoint and its \(k\) directions are independent and uniform: in particular,
\((h'_j,h_j-h'_j)\) is uniform on \(G^2\). It is therefore nonzero with probability \(\tau\).

A union bound gives, for every fixed \(x\),
\[
\Pr_{\mathbf h,\mathbf h'}
[D_{\mathbf h}f(x)\ne D_{\mathbf h'}f(x)]
\le k\tau.
\tag{10}
\]
If \(p_a=\Pr_{\mathbf h}[D_{\mathbf h}f(x)=a]\), then
\[
\sum_a p_a^2\ge1-k\tau,
\]
so
\[
\max_a p_a\ge1-k\tau.
\]
Because \(k\tau<2^{-k}\le1/2\), there is a unique value \(c(x)\in H\) satisfying
\[
\Pr_{\mathbf h}[D_{\mathbf h}f(x)=c(x)]\ge1-k\tau.
\tag{11}
\]

Define
\[
q(x)=f(x)-(-1)^k c(x).
\tag{12}
\]

### Step 2: the correction changes few points

If \(c(x)\ne0\), equation (11) implies that \(D_{\mathbf h}f(x)\ne0\) with probability at least \(1-k\tau\). Averaging over \(x\),
\[
\tau\ge(1-k\tau)\Pr_x[c(x)\ne0].
\]
Since \(q(x)\ne f(x)\) exactly when \(c(x)\ne0\), this proves (8).

### Step 3: every \(k\)-fold derivative of \(q\) vanishes

Fix arbitrary \(x,a_1,\ldots,a_k\). For \(S\subseteq[k]\), write
\[
x_S=x+\sum_{i\in S}a_i.
\]
Choose uniform \(h_1,\ldots,h_k\). For each \(S\), the tuple
\[
(h_i-\mathbf1_{i\in S}a_i)_{i=1}^k
\]
is uniform on \(G^k\). By (11), with failure probability at most \(k\tau\),
\[
D_{(h_i-\mathbf1_{i\in S}a_i)_i}f(x_S)=c(x_S).
\tag{13}
\]
There are \(2^k\) choices of \(S\). By (7), some choice of \(\mathbf h\) makes (13) hold simultaneously for every \(S\).

For this choice, commutativity of translation operators gives
\[
\begin{aligned}
\Delta_{a_1}\cdots\Delta_{a_k}c(x)
&=
\sum_{S\subseteq[k]}(-1)^{k-|S|}
D_{(h_i-\mathbf1_{i\in S}a_i)_i}f(x_S)\\
&=
\left[
\prod_{i=1}^k
\bigl(T_{a_i}\Delta_{h_i-a_i}-\Delta_{h_i}\bigr)
f
\right](x).
\end{aligned}
\]
But
\[
T_a\Delta_{h-a}-\Delta_h
=(T_h-T_a)-(T_h-I)
=-\Delta_a.
\]
Hence
\[
\Delta_{a_1}\cdots\Delta_{a_k}c(x)
=
(-1)^k\Delta_{a_1}\cdots\Delta_{a_k}f(x).
\]
Equation (12) now implies
\[
\Delta_{a_1}\cdots\Delta_{a_k}q(x)=0.
\]
The basepoint and directions were arbitrary. This proves the lemma. \(\square\)

# 3. Proof of Theorem 1

Let \(\rho=\rho_k(f)\).

The anchored expression (1) satisfies
\[
A_f(\mathbf h)
=
D_{\mathbf h}f(0)-(-1)^k f(0).
\tag{14}
\]
Also,
\[
D_{\mathbf h}f(x)
=
A_f(x+h_1,h_2,\ldots,h_k)
-
A_f(x,h_2,\ldots,h_k).
\tag{15}
\]
Indeed, this follows from
\[
\Delta_{x+h_1}-\Delta_x=T_x\Delta_{h_1}.
\]
Each expression on the right of (15), under uniform \(x,\mathbf h\), has the distribution defining \(\rho\). Therefore
\[
\tau\le2\rho.
\tag{16}
\]

If \(\rho\ge1/C_k\), take \(q=0\). Then
\[
\operatorname{dist}(f,q)\le1\le C_k\rho.
\]

Suppose henceforth that
\[
\rho<\frac1{k2^{k+1}}.
\]
Lemma 2 applies by (16), yielding a map \(q\) with vanishing \(k\)-fold derivatives and
\[
d:=\operatorname{dist}(f,q)
\le\frac{2\rho}{1-2k\rho}.
\tag{17}
\]

It remains to prove the essential normalization \(q(0)=0\).

Since all \(k\)-fold derivatives of \(q\) vanish, equation (14) gives
\[
A_q(\mathbf h)=(-1)^{k+1}q(0)
\quad\text{for every }\mathbf h.
\tag{18}
\]
If \(q(0)\ne0\), this expression is always nonzero. Thus, for every parameter tuple, either \(A_f\ne0\), or \(f\) and \(q\) differ at at least one of the \(2^k-1\) outputs.

Each nonempty subset sum of independent uniform group elements is uniform on \(G\). Consequently,
\[
1\le \rho+(2^k-1)d.
\tag{19}
\]
But (17) and the bound on \(\rho\) imply
\[
\begin{aligned}
\rho+(2^k-1)d
&\le
\rho+(2^k-1)\frac{2\rho}{1-2k\rho}\\
&<
\frac1{k2^{k+1}}+\frac1k
<1,
\end{aligned}
\]
where the last inequality uses \(k\ge2\). This contradicts (19), so \(q(0)=0\).

Moreover, \(2k\rho<2^{-k}\le1/4\), giving \(d\le3\rho\). This proves both (3) and (4).

Finally, (18) shows that the repaired coloring has no forbidden instance whatsoever. Conversely, an exactly forbidden-free coloring satisfies (2): normalization follows by setting every parameter to zero in (1), and polynomiality follows from (15). Thus the exact property being tested is precisely that of normalized polynomial maps. \(\square\)

# 4. The systems really have higher complexity

## Proposition 3

Over every field, the system
\[
\mathcal L_k=
\left(
\sum_{i\in S}x_i
\right)_{\varnothing\ne S\subseteq[k]}
\]
has Cauchy–Schwarz complexity exactly \(k-1\).

### Proof

Identify the coefficient vector of \(L_S\) with
\[
v_S=\mathbf1_S\in\mathbb F^k.
\]

For the upper bound, fix a nonempty \(S\) and choose \(a\in S\). Consider the following \(k\) linear functionals:
\[
X_i\quad(i\in S),\qquad X_a-X_j\quad(j\notin S).
\]
All take value \(1\) at \(v_S\). Every other \(v_T\) lies in at least one of their kernels:

* if \(S\nsubseteq T\), use \(X_i\) with \(i\in S\setminus T\);
* if \(S\subsetneq T\), use \(X_a-X_j\) with \(j\in T\setminus S\).

Assigning every other form to one such kernel gives a partition into at most \(k\) classes, none of whose spans contains \(v_S\). Hence the complexity is at most \(k-1\).

For the lower bound, suppose the other forms could be partitioned into \(t\le k-1\) classes whose spans avoid \(v_S\). Choose a linear functional \(\lambda_j\) vanishing on class \(j\) but not at \(v_S\), and put
\[
P=\prod_{j=1}^t\lambda_j.
\]
Then \(P(v_S)\ne0\), while \(P(v_T)=0\) for every other nonempty \(T\). Also \(P(0)=0\), and \(\deg P<k\).

Every monomial of degree less than \(k\) omits some variable. Pairing subsets according to that variable therefore gives
\[
\sum_{T\subseteq[k]}(-1)^{k-|T|}P(v_T)=0.
\]
In our case the only nonzero summand is
\[
(-1)^{k-|S|}P(v_S),
\]
a contradiction. \(\square\)

These systems are also non-affine: translating every output by a common nonzero element does not preserve
\[
L_{\{1\}}+L_{\{2\}}=L_{\{1,2\}}.
\]

For \(k=3\), they are genuinely beyond Fourier/complexity-\(1\) counting, not merely high-CS presentations of a Fourier-controlled system. For example, on \(V=\mathbb F_2^{2t}\), let
\[
u(v)=(-1)^{\sum_{j=1}^t v_{2j-1}v_{2j}}.
\]
The associated bilinear form is nondegenerate, so
\[
\|u\|_{U^2}^4=2^{-2t}\longrightarrow0.
\]
Nevertheless,
\[
\prod_{\varnothing\ne S\subseteq[3]}u(L_S(\mathbf x))=1
\]
for every \(\mathbf x\), because the exponent is the anchored third derivative of a zero-constant quadratic polynomial.

# 5. The punctured finite-field formulation

Take \(G=\mathbb F_2^n\), \(H=\mathbb F_2\), and let
\[
\phi:G\setminus\{0\}\to\mathbb F_2.
\]
Extend it by \(f(0)=0\).

Here all signs in (1) are identical, so the forbidden words are exactly the odd-parity words on the \(2^k-1\) nonzero points of \(\mathbb F_2^k\).

A parameter tuple \(\mathbf h\) is generic when
\[
T_{\mathbf h}:\mathbb F_2^k\to G,\qquad
a\mapsto\sum_i a_i h_i
\]
is injective.

If it is not injective, every point in its image has an even number of preimages. Thus
\[
\sum_{a\in\mathbb F_2^k}f(T_{\mathbf h}(a))=0.
\]
Since \(f(0)=0\), this says exactly that \(A_f(\mathbf h)=0\).

Therefore **all violations are generic**. There is no non-generic error term and no large-dimension proviso.

## Corollary 4

Fix \(k\ge2\). There are
\[
K=2^{\,2^k-2}
\]
odd-parity colored versions of \(\mathcal L_k\).

If each has at most \(\delta\,2^{nk}\) generic instances in \(\phi\), then \(\phi\) can be recolored on at most
\[
k2^{k+1}\,2^{\,2^k-2}\delta\,2^n
\tag{20}
\]
points so that none remains.

The repaired coloring is the restriction of a zero-constant Boolean polynomial of degree at most \(k-1\).

To justify the last description, every function \(\mathbb F_2^n\to\mathbb F_2\) has a unique squarefree polynomial representation. Vanishing of all \(k\)-fold derivatives is equivalent to absence of monomials of degree at least \(k\): coordinate derivatives remove their corresponding variables, and distinct surviving monomials remain distinct.

### Explicit complexity-\(2\) instance

For \(k=3\), the forms are
\[
x,\ y,\ z,\ x+y,\ x+z,\ y+z,\ x+y+z.
\]
Forbid all \(64\) color words with odd parity. If each occurs at most \(\delta\,2^{3n}\) times generically, at most
\[
3072\,\delta\,2^n
\]
recolorings suffice.

The exact free colorings are restrictions of
\[
q(v)=\sum_i a_i v_i+\sum_{i<j}b_{ij}v_iv_j.
\]
These can be far from constant. For instance, a nonzero linear map is balanced, and \(v_1v_2\) is a genuinely quadratic free coloring.

Thus this is not a consensus result. Nor is either color safe: changing a single point of a free coloring can create an odd-parity configuration.

# 6. What remains unproved

This establishes an explicit same-palette induced-removal theorem:

* for non-affine systems of unbounded finite CS complexity;
* uniformly over every finite abelian group;
* with a linear removal bound;
* and, over \(\mathbb F_2^n\setminus\{0\}\), with exact handling of generic instances.

Uniformity includes cyclic groups of arbitrary order, and hence periodic colorings of \(\mathbb Z\) when counts and distance are measured over a period.

It does **not** settle the catalogued conjecture. The crucial restriction is that the allowed color words satisfy a finite-difference identity in an abelian color group. The self-correction proof uses algebraic cancellation at every stage. An arbitrary forbidden family need not impose such an identity, so neither the concentration argument nor the exact repair has been justified there.

In particular, no removal theorem for arbitrary higher-complexity colored patterns, or for arbitrary colorings of integer intervals, is proved here. No claim of novelty is made for the polynomial self-correction mechanism.