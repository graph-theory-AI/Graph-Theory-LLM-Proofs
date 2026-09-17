```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "Reciprocal-permutation strategies require at most (1+o(1))n/log n colors, and none wins with n+1 colors for n>=3.",
  "would_publish": false,
  "caveats": "This covers a restricted, though fully nonlinear, strategy class; the unrestricted hat guessing number is not determined, and novelty of the restricted result was not checked."
}
```

# A spectral obstruction to reciprocal-permutation strategies

The unrestricted question is not resolved here. I obtain a stronger obstruction for the permutation ansatz proposed in the previous attempt: not only can it never attain \(n+1\) colors when \(n\ge3\), but its number of colors is at most
\[
(1+o(1))\frac{n}{\log n}.
\]

The argument is self-contained. In particular, I do not use the previous attempt’s affine-linear claims.

## 1. Strategies and the restricted result

Write the two hat vectors on \(K_{n,n}\) as \(x,y\in Q^n\), where \(|Q|=q\). A general strategy consists of maps
\[
F,G:Q^n\longrightarrow Q^n.
\]
The players on the first side guess \(F(y)\), and those on the second side guess \(G(x)\).

Call a strategy **reciprocal-permutation** if, for a bijection \(\pi:Q^n\to Q^n\),
\[
F=\pi,\qquad G=\pi^{-1}.
\]
No algebraic or coordinatewise restriction is imposed on \(\pi\).

### Theorem 1
Let \(q\ge3\), and put
\[
r=q-1,\qquad \rho=\left(\frac{q-1}{q}\right)^n.
\]
For every reciprocal-permutation strategy, the probability that all players guess incorrectly under a uniformly random hat assignment satisfies
\[
\boxed{\quad
p_{\mathrm{lose}}
\ge
\rho^2-\frac{2r}{r^2-1}\rho(1-\rho).
\quad}                                                     \tag{1}
\]

Consequently, a winning reciprocal-permutation strategy must satisfy
\[
\boxed{\quad
\left(\frac q{q-1}\right)^n
\ge
\frac{q^2-2}{2(q-1)}.
\quad}                                                     \tag{2}
\]
In particular, within this strategy class,
\[
q\le (1+o(1))\frac{n}{\log n}.
\]

Moreover, no reciprocal-permutation strategy wins with \(q=n+1\) colors when \(n\ge3\).

Here and below, logarithms are natural.

## 2. Translation into graph self-packing

Let
\[
H=K_q^{\times n}
\]
be the graph on \(Q^n\) whose adjacent vertices differ in every coordinate. Set
\[
N=q^n,\qquad d=(q-1)^n=r^n,
\]
so \(H\) has \(N\) vertices and is \(d\)-regular.

Under a reciprocal strategy, write \(x=\pi(u)\) and \(y=v\). The assignment is losing precisely when
\[
u\sim_H v
\quad\text{and}\quad
\pi(u)\sim_H\pi(v).
\]
Thus winning is equivalent to packing a permuted copy of \(H\) edge-disjointly with \(H\).

Let \(A\) be the adjacency matrix of \(H\), and let
\[
C=PAP^T,
\]
where \(P\) is the permutation matrix of \(\pi\). If \(L\) is the number of common unordered edges of the two graphs, then
\[
\operatorname{tr}(AC)=2L,
\qquad
p_{\mathrm{lose}}=\frac{\operatorname{tr}(AC)}{N^2}.          \tag{3}
\]

## 3. A uniform lower bound on the overlap

The adjacency matrix has the tensor form
\[
A=(J_q-I_q)^{\otimes n}.
\]
The matrix \(J_q-I_q\) has eigenvalue \(r\) on constants and eigenvalue \(-1\) on their orthogonal complement. Hence the distinct eigenvalues of \(A\) are
\[
\alpha_k=(-1)^k r^{n-k},
\qquad 0\le k\le n,
\]
with multiplicities
\[
m_k=\binom nk r^k.
\]

Let \(E_k\) be the corresponding orthogonal projections. Then
\[
A=\sum_{k=0}^n\alpha_kE_k,
\qquad
C=\sum_{\ell=0}^n\alpha_\ell E'_\ell,
\qquad
E'_\ell=PE_\ell P^T.
\]
Define
\[
h_{k\ell}=\operatorname{tr}(E_kE'_\ell).
\]
For orthogonal projections,
\[
0\le h_{k\ell}\le \min(m_k,m_\ell).
\]
Indeed, \(E_kE'_\ell E_k\) is positive semidefinite and bounded above by \(E_k\).

Both matrices have the same constant eigenspace, so
\[
h_{00}=1,\qquad h_{0\ell}=h_{\ell0}=0\quad(\ell>0).
\]
It follows that
\[
\operatorname{tr}(AC)
=d^2+\sum_{k,\ell\ge1}\alpha_k\alpha_\ell h_{k\ell}.          \tag{4}
\]

Terms with \(k+\ell\) even are nonnegative. For \(k<\ell\) with \(\ell-k\) odd,
\[
\begin{aligned}
|\alpha_k\alpha_\ell|(h_{k\ell}+h_{\ell k})
&\le 2r^{2n-k-\ell}m_k\\
&=2d^2\binom nk r^{-\ell}.
\end{aligned}
\]
Dropping the nonnegative terms from (4), and then summing the geometric series over odd positive differences, gives
\[
\begin{aligned}
\operatorname{tr}(AC)
&\ge d^2-
  2d^2\sum_{k=1}^{n-1}\binom nk r^{-k}
       \sum_{\substack{s\ge1\\s\text{ odd}}}r^{-s}\\
&\ge d^2\left[
1-\frac{2r}{r^2-1}
\left(\left(1+\frac1r\right)^n-1\right)
\right].                                                   \tag{5}
\end{aligned}
\]
Since
\[
\frac dN=\rho,\qquad
\left(1+\frac1r\right)^n=\rho^{-1},
\]
division by \(N^2\) proves (1).

If the strategy wins, the right side of (1) must be nonpositive. Because \(\rho>0\), this implies
\[
\rho\le \frac{2r}{r^2+2r-1}
       =\frac{2(q-1)}{q^2-2},
\]
which is exactly (2). ∎

## 4. Asymptotic consequences

Taking logarithms in (2) yields the explicit necessary condition
\[
n\ge
\frac{\log\!\left((q^2-2)/(2(q-1))\right)}
     {\log(q/(q-1))}.                                      \tag{6}
\]
As \(q\to\infty\), the right side is
\[
(1+o(1))(q-1)\log(q-1).
\]
Inverting this inequality gives
\[
q\le (1+o(1))\frac{n}{\log n}.
\]
Bounded values of \(q\) cause no issue in this asymptotic statement.

### Random permutations are asymptotically optimal in the linear regime

The overlap bound has a useful quantitative interpretation. Suppose
\[
q\to\infty,\qquad \frac{n}{q-1}\longrightarrow a\in(0,\infty).
\]
Then \(\rho\to e^{-a}\), and (1) gives, uniformly over all permutations,
\[
p_{\mathrm{lose}}\ge e^{-2a}-o(1).                          \tag{7}
\]

Conversely, for a uniformly random permutation \(\pi\), each ordered edge of \(H\) is mapped to an ordered edge with probability \(d/(N-1)\). Therefore
\[
\mathbb E_\pi p_{\mathrm{lose}}
=\frac{d^2}{N(N-1)}
=\rho^2\frac{N}{N-1}.
\]
Some permutation has losing probability at most this expectation. Consequently,
\[
\boxed{\quad
\min_\pi p_{\mathrm{lose}}\longrightarrow e^{-2a}.
\quad}                                                     \tag{8}
\]
For example, when \(q=n+1\), the best reciprocal-permutation strategies still lose on asymptotically an \(e^{-2}\) fraction of all assignments.

## 5. Excluding the endpoint for every \(n\ge3\)

The asymptotic obstruction alone does not cover every small case. Here is a complete endpoint argument.

### The case \(n\ge4\)

Set \(q=n+1\) in (2). A winning reciprocal strategy would require
\[
\left(1+\frac1n\right)^n
\ge
1+\frac n2-\frac1{2n}.
\]
But
\[
\left(1+\frac1n\right)^n<e
\quad\text{and}\quad
1+\frac n2-\frac1{2n}\ge\frac{23}{8}>e,
\]
a contradiction.

### The case \(n=3,\ q=4\)

Here \(N=64\), \(d=27\). The spectrum of \(A\) is
\[
27^{(1)},\qquad (-9)^{(9)},\qquad 3^{(27)},\qquad (-1)^{(27)}.
\]

Work on the \(63\)-dimensional space \(W=\mathbf1^\perp\). Let \(P_1,P_3\) be the projections onto the \(-9\) and \(-1\) eigenspaces, respectively. Put
\[
D=3P_1+P_3.
\]
Then
\[
A|_W=3I_W-4D,\qquad \operatorname{tr}D=54.
\]
For the permuted matrix, write similarly
\[
C|_W=3I_W-4D'.
\]
Expanding the trace gives
\[
\begin{aligned}
\operatorname{tr}(AC)
&=27^2+9\cdot63-12(54+54)+16\operatorname{tr}(DD')\\
&=16\operatorname{tr}(DD').                                \tag{9}
\end{aligned}
\]

Let
\[
E=P_1+P_3,\qquad E'=PEP^T.
\]
These are rank-\(36\) projections on \(W\), and \(D\ge E\), \(D'\ge E'\). Thus
\[
\operatorname{tr}(DD')\ge\operatorname{tr}(EE').
\]
Also,
\[
\operatorname{tr}(EE')
=36-\operatorname{tr}(E(I-E'))
\ge36-27=9.
\]
Combining this with (9),
\[
\operatorname{tr}(AC)\ge144.
\]
In particular,
\[
p_{\mathrm{lose}}\ge\frac{144}{64^2}=\frac9{256}>0.
\]
This excludes the remaining endpoint case.

### The \(n=2\) exception is genuine

With \(Q=\mathbb F_3\), take
\[
\pi(u,v)=(u+v,u-v).
\]
This is invertible. If two inputs differ in both coordinates, their difference is \((a,b)\) with \(a,b\ne0\). Over \(\mathbb F_3\), either \(a=b\) or \(a=-b\), so their images agree in one coordinate. Hence \(\pi\) maps every edge of \(K_3^{\times2}\) to a nonedge, and the reciprocal strategy wins.

Thus the endpoint obstruction correctly excludes \(n\ge3\), not \(n=2\).

## 6. What remains unresolved

The original game permits arbitrary maps \(F,G\). They may be noninjective, or they may be two unrelated permutations. There is no justification for replacing them by mutually inverse bijections.

That distinction is essential: the proof uses
\[
C=PAP^T
\]
and the resulting nonnegative overlaps of orthogonal eigenspaces. These features are unavailable for a general pair \(F,G\).

Accordingly:

- I have **not** improved the unrestricted upper bound \(HG(K_{n,n})\le n+1\).
- I have **not** determined whether \(HG(K_{3,3})=3\) or \(4\).
- I have ruled out the supplied attempt’s reciprocal-permutation endpoint ansatz completely, and proved the stronger \(O(n/\log n)\) color bound for that fully nonlinear restricted class.

No computational result or additional literature-status claim is used here.