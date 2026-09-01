```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "No full characterization is obtained, but even a compact box-dimension-zero set meeting every affine line in at most two points can have uniform concentration probability one.",
  "would_publish": false,
  "caveats": "The question is open-ended; anti-concentration is interpreted as a bound tending to zero uniformly over the nonzero vectors."
}
```

# Mathematical writeup

## 1. A precise formulation

Let \(\xi_1,\ldots,\xi_n\) be independent uniform signs and define, for fixed \(S\subseteq\mathbb R^d\),
\[
q_n(S):=
\sup_{a_1,\ldots,a_n\in\mathbb R^d\setminus\{0\}}
\Pr\left(\sum_{i=1}^n a_i\xi_i\in S\right).
\]
The natural anti-concentration interpretation of the question is to find geometric hypotheses implying
\[
q_n(S)\longrightarrow 0,
\]
preferably with a polynomial rate.

The original question is not a single falsifiable conjecture because neither “geometric constraints” nor “non-trivial” is specified. The results below delimit what such constraints can look like.

---

## 2. Why excluding line segments is necessary

Suppose that
\[
[c-v,c+v]=\{c+tv:-1\le t\le1\}\subseteq S,
\qquad v\ne0.
\]

If \(c=0\), take \(a_i=v/n\). Then
\[
\sum_{i=1}^n a_i\xi_i
=\frac{\xi_1+\cdots+\xi_n}{n}v\in[-v,v]\subseteq S
\]
with probability one. Thus \(q_n(S)=1\).

If \(c\ne0\) and \(n\ge2\), take
\[
a_1=c,\qquad a_2=\cdots=a_n=\frac{v}{n-1}.
\]
Conditioned on \(\xi_1=1\), the sum belongs to \([c-v,c+v]\). Hence
\[
q_n(S)\ge\frac12.
\]

Thus the absence of a line segment is necessary for \(q_n(S)=o(1)\). It is very far from sufficient without a global tameness assumption.

---

## 3. A strong geometric counterexample

The following construction shows that compactness, dimension zero, and an extremely strong line-incidence condition still do not suffice.

### Theorem 3.1

There exists a compact countable set \(K\subseteq\mathbb R^2\) such that:

1. every affine line contains at most two points of \(K\);
2. \(K\) has Hausdorff dimension and upper box dimension zero;
3. \(q_n(K)=1\) for every \(n\).

Moreover, the witnessing vectors \(a_1,\ldots,a_n\) may be chosen pairwise nonparallel.

### Generic projection lemma

Let \(E_n=\{-1,1\}^n\). Let \(A\subseteq\mathbb R^2\setminus\{0\}\) be finite and contain no three collinear points. Then the linear maps
\[
L:\mathbb R^n\longrightarrow\mathbb R^2
\]
for which

- \(L\) is injective on \(E_n\);
- \(L(E_n)\cap(A\cup\{0\})=\varnothing\);
- \(A\cup L(E_n)\) contains no three collinear points;
- \(L(e_i)\ne0\) for every \(i\);

form a dense open subset of the space of linear maps. We may additionally require the vectors \(L(e_i)\) to be pairwise nonparallel.

#### Proof

Every forbidden event is the zero set of a nonzero polynomial in the entries of \(L\).

For three distinct \(x,y,z\in E_n\), the vectors \(y-x\) and \(z-x\) are linearly independent. Indeed, the nonzero coordinates of \(y-x\) are exactly \(-2x_i\) on the coordinates where \(x\) and \(y\) differ. If \(z-x\) were proportional to \(y-x\), they would have the same support and the proportionality factor would be \(1\), forcing \(z=y\). Consequently
\[
\det\big(L(y-x),L(z-x)\big)
\]
is not the zero polynomial.

For \(p\in A\) and distinct \(x,y\in E_n\), the condition that \(p,Lx,Ly\) are collinear is also proper. If \(x,y\) are linearly independent, their images can be prescribed arbitrarily. If \(y=-x\), choose \(Lx\) not parallel to \(p\); then \(p,Lx,-Lx\) are not collinear because \(p\ne0\).

The condition that \(Lx\) lies on the line through two fixed points of \(A\) is proper since \(Lx\) can be prescribed arbitrarily. Collisions and zero images are proper linear conditions. Pairwise parallelism of \(L(e_i),L(e_j)\) is given by the proper equation
\[
\det(L(e_i),L(e_j))=0.
\]
A finite union of proper real algebraic subsets has empty interior, proving the lemma. \(\square\)

### Construction of \(K\)

Fix \(p=(1,0)\) and let
\[
r_n=e^{-n^2}.
\]
Inductively construct linear maps \(L_n:\mathbb R^n\to\mathbb R^2\). Suppose that \(L_1,\ldots,L_{n-1}\) have been chosen and that
\[
A_{n-1}:=\{p,-p\}\cup\bigcup_{m<n}L_m(E_m)
\]
contains no three collinear points and does not contain \(0\).

Apply the generic projection lemma inside the nonempty open set
\[
\mathcal U_n=
\left\{
L:
\|L(e_1)-p\|+\sum_{i=2}^n\|L(e_i)\|<r_n
\right\}.
\]
Choose \(L_n\in\mathcal U_n\) satisfying all conclusions of the lemma relative to \(A_{n-1}\). Put
\[
B_n=L_n(E_n)
\]
and finally
\[
K=\{p,-p\}\cup\bigcup_{n\ge1}B_n.
\]

By induction, \(K\) has no three collinear points. Hence every affine line meets \(K\) in at most two points.

If \(\varepsilon_1=1\), then
\[
\|L_n\varepsilon-p\|
\le \|L_n(e_1)-p\|+\sum_{i=2}^n\|L_n(e_i)\|
<r_n.
\]
If \(\varepsilon_1=-1\), similarly
\[
\|L_n\varepsilon+p\|<r_n.
\]
Thus every point of \(B_n\) lies within \(r_n\) of either \(p\) or \(-p\). Since \(r_n\to0\), the only accumulation points are \(p\) and \(-p\), both of which belong to \(K\). Therefore \(K\) is compact.

For the upper box dimension, let \(N(K,\epsilon)\) denote the minimum number of radius-\(\epsilon\) balls needed to cover \(K\). Choose \(N\) such that
\[
r_{N+1}<\epsilon\le r_N.
\]
All blocks \(B_n\) with \(n>N\) are covered by two balls centered at \(p\) and \(-p\). The earlier blocks contain fewer than \(2^{N+1}\) points. Hence
\[
N(K,\epsilon)\le 2+\sum_{n=1}^N2^n<2^{N+1}+2.
\]
On the other hand,
\[
\log(1/\epsilon)\ge\log(1/r_N)=N^2.
\]
Therefore
\[
\overline{\dim}_{\rm B}K
=
\limsup_{\epsilon\downarrow0}
\frac{\log N(K,\epsilon)}{\log(1/\epsilon)}
=0.
\]
Countability also gives Hausdorff dimension zero.

Finally, for each \(n\), take
\[
a_i=L_n(e_i),\qquad 1\le i\le n.
\]
These vectors are nonzero, and
\[
\sum_{i=1}^n a_i\xi_i=L_n(\xi_1,\ldots,\xi_n)\in B_n\subseteq K
\]
for every sign vector. Hence
\[
q_n(K)=1.
\]
This proves the theorem. \(\square\)

### Consequence

Even the conjunction of all the following conditions does not imply any upper bound smaller than \(1\):

- \(S\) is compact;
- \(S\) is countable;
- \(S\) has upper box dimension zero;
- \(S\) contains no line segment;
- no three points of \(S\) are collinear.

Thus bounds on dimensions or on intersections with lines cannot by themselves solve the problem.

---

## 4. Explicit and smooth counterexamples

The preceding example is obtained by generic induction. There are also very explicit examples showing that differential regularity is insufficient.

### 4.1 An explicit compact zero-dimensional example in \(\mathbb R\)

Let
\[
\delta_n=e^{-n^3}
\]
and define
\[
F=\{0\}\cup
\bigcup_{n\ge1}
\left\{
\delta_n(2j-n):0\le j\le n
\right\}.
\]
For the \(n\)-th problem take
\[
a_1=\cdots=a_n=\delta_n.
\]
Then
\[
\sum_{i=1}^n a_i\xi_i
\in
\{\delta_n(2j-n):0\le j\le n\}
\subseteq F
\]
with probability one. Thus
\[
q_n(F)=1\qquad\text{for every }n.
\]

The largest absolute value in the \(n\)-th block is
\[
\rho_n=n e^{-n^3}\longrightarrow0,
\]
so \(F\) is compact. It is countable and hence contains no interval.

It also has upper box dimension zero. If
\[
\rho_{N+1}<\epsilon\le\rho_N,
\]
then all blocks after \(N\) lie in \([-\epsilon,\epsilon]\), while the first \(N\) blocks contain \(O(N^2)\) points. Hence
\[
N(F,\epsilon)=O(N^2),
\qquad
\log(1/\epsilon)\ge N^3-\log N,
\]
which gives \(\overline{\dim}_{\rm B}F=0\).

This is the basic obstruction: a set may contain centered arithmetic progressions of every required length while remaining compact and dimension zero.

---

### 4.2 A compact \(C^\infty\) embedded curve

There is a nonnegative \(C^\infty\) function \(f:\mathbb R\to\mathbb R\) whose zero set is exactly \(F\) and which is not affine on any interval.

For completeness, write the components of \(\mathbb R\setminus F\) as \(I_j\). On each bounded component \(I_j=(\alpha_j,\beta_j)\), let
\[
\psi_j(x)=
\begin{cases}
\exp\left(-\dfrac1{(x-\alpha_j)^2}
          -\dfrac1{(\beta_j-x)^2}\right),
&x\in I_j,\\[1ex]
0,&x\notin I_j.
\end{cases}
\]
Use the analogous one-sided flat function on an unbounded component. Each \(\psi_j\) is \(C^\infty\), positive exactly on \(I_j\), and real analytic and non-affine within \(I_j\).

Choose constants \(c_j>0\) sufficiently small that
\[
\|c_j\psi_j^{(k)}\|_\infty\le2^{-j}
\qquad(0\le k\le j),
\]
and put
\[
f=\sum_j c_j\psi_j.
\]
For every fixed \(k\), the series of \(k\)-th derivatives converges uniformly, so \(f\in C^\infty\). It is positive off \(F\) and zero on \(F\).

If \(f\) were affine on a nonempty interval, that interval would contain a subinterval of some \(I_j\). There \(f=c_j\psi_j\), contradicting analyticity and non-affineness of \(\psi_j\).

Now let
\[
S_{\rm sm}=\{(x,f(x)):-1\le x\le1\}.
\]
This is a compact \(C^\infty\) embedded arc. It contains no line segment: a nonvertical segment in the graph would force \(f\) to be affine on an interval, while a vertical segment cannot lie in a graph.

Taking
\[
a_i=(\delta_n,0)
\]
gives
\[
\sum_{i=1}^n a_i\xi_i=(x,0)
\]
with \(x\in F\), and therefore \((x,0)=(x,f(x))\in S_{\rm sm}\). Consequently
\[
q_n(S_{\rm sm})=1\qquad\text{for every }n.
\]

Thus even compactness, connectedness, smooth embedded-manifold structure, and absence of line segments do not suffice.

---

### 4.3 A real-analytic curved example

Let
\[
g(x)=1-\cos(2\pi x)
\]
and
\[
S_{\rm an}=\{(x,g(x)):x\in\mathbb R\}.
\]
This is a closed real-analytic embedded curve with no line segment. Taking
\[
a_1=\cdots=a_n=(1,0)
\]
gives
\[
\sum_{i=1}^n a_i\xi_i=(k,0)
\]
for an integer \(k\), and \(g(k)=0\). Hence
\[
q_n(S_{\rm an})=1
\qquad\text{for every }n.
\]

Moreover,
\[
g'(k)=0,\qquad g''(k)=4\pi^2,
\]
so the curve has nonzero curvature at every point carrying probability mass. Thus local curvature at the relevant points also does not suffice.

There is no conflict with the o-minimal theorem in the source paper: the globally periodic graph above cannot be definable in an o-minimal structure, since its intersection with the \(x\)-axis projects to the infinite discrete set \(\mathbb Z\).

---

## 5. Two elementary positive bounds

### 5.1 Finite sets

Let
\[
\beta_n=2^{-n}\binom{n}{\lfloor n/2\rfloor}
=O(n^{-1/2}).
\]

For every point \(x\in\mathbb R^d\),
\[
\Pr\left(\sum_{i=1}^n a_i\xi_i=x\right)\le\beta_n.
\]

Indeed, choose a linear functional \(u\) such that \(u(a_i)\ne0\) for every \(i\). Flip the signs of the \(a_i\), which does not change the distribution, so that \(u(a_i)>0\). If a sign vector is represented by the subset \(A\subseteq[n]\) on which \(\xi_i=1\), then the scalar equation
\[
u\left(\sum_i a_i\xi_i\right)=u(x)
\]
cannot hold for two comparable subsets \(A\subsetneq B\), since all \(u(a_i)\) are positive. Thus the solution subsets form an antichain. Sperner's theorem gives at most
\(\binom{n}{\lfloor n/2\rfloor}\) solutions.

Consequently, if \(|S|=m<\infty\), then
\[
q_n(S)\le m\beta_n=O(mn^{-1/2}).
\]
This is a simple genuine class of geometric constraints yielding decay.

### 5.2 A constant bound from antipodal exclusion

Suppose \(0\in S\) and every affine line meets \(S\) in at most two points. Then \(S\) cannot contain both \(x\) and \(-x\) for any \(x\ne0\), since \(0,x,-x\) would be collinear.

The law of \(X=\sum_i a_i\xi_i\) is centrally symmetric. Pairing its nonzero support points into antipodal pairs gives
\[
\Pr(X\in S)
\le
\Pr(X=0)+\frac{1-\Pr(X=0)}2
=
\frac12+\frac12\Pr(X=0).
\]
Using the point-mass bound,
\[
q_n(S)\le \frac12+\frac{\beta_n}{2}.
\]
This is a nontrivial uniform constant bound, but it does not tend to zero. The condition \(0\in S\) is essential: the compact set \(K\) from Theorem 3.1 avoids \(0\) and has \(q_n(K)=1\).

---

## 6. The exact combinatorial obstruction

Every choice of vectors is a linear map
\[
L:\mathbb R^n\to\mathbb R^d,\qquad L(e_i)=a_i.
\]
Therefore
\[
q_n(S)
=
2^{-n}
\sup_{\substack{L:\mathbb R^n\to\mathbb R^d\\L(e_i)\ne0}}
\left|
\{\varepsilon\in\{-1,1\}^n:L\varepsilon\in S\}
\right|.
\]

Thus the problem is exactly one of bounding the weighted intersections of \(S\) with all linear images of Boolean cubes. In particular, equal vectors give the lower bound
\[
q_n(S)\ge
2^{-n}\sum_{j=0}^n
\binom nj
\mathbf 1_S\big((2j-n)a\big)
\]
for every \(a\ne0\).

The compact constructions above show that ordinary notions of geometric smallness can coexist with complete Boolean-cube containment. Any successful general hypothesis must therefore impose some uniform global complexity or additive-incidence control, not merely:

- small measure or small Hausdorff dimension;
- compactness or connectedness;
- smoothness or real analyticity;
- nonzero local curvature;
- absence of line segments;
- bounded intersection with every affine line.

The o-minimal result in the supplied source does impose precisely such global tameness. The arguments here do not provide a general characterization or improve the known bounds for tame, algebraic, convex, or o-minimal classes.