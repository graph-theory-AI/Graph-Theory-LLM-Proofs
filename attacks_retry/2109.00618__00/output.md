```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "For off-diagonal entries in 2^Z and diagonal entries outside 2^Z, I prove n <= d + 3^(d-1)d!, while the zero-diagonal minimum rank is sqrt(2n)+O(1).",
  "would_publish": false,
  "caveats": "The sharp bound for arbitrary excluded diagonals and the uniform rank-r problem remain open; literature novelty has not been independently checked."
}
```

# 1. Precise results and the diagonal issue

Write
\[
\Gamma=2^{\mathbb Z}.
\]
A diagonal restriction is indispensable: without one, the all-ones matrix has rank \(1\).

The previous attempt’s modulo-\(3\) argument is correct **for zero diagonal**, but I do not assume that zero diagonal is the full source hypothesis. The main additional result here allows arbitrary complex diagonal entries outside \(\Gamma\).

## Theorem 1: arbitrary excluded diagonals

Let \(n\ge2\), and let \(A=(a_{ij})\in\mathbb C^{n\times n}\) satisfy
\[
a_{ij}\in\Gamma\quad(i\ne j),
\qquad
a_{ii}\notin\Gamma\quad(i\in[n]).
\]
If \(d=\operatorname{rank}_{\mathbb C}A\), then
\[
\boxed{\quad n\le d+3^{d-1}d!.\quad}
\tag{1}
\]
Consequently,
\[
\log n\le d\log d+O(d),
\qquad
d\ge (1-o(1))\frac{\log n}{\log\log n}.
\tag{2}
\]

Thus, for this particular multiplicative group, the bound quoted in the question can be improved from roughly \(\log n\lesssim d^8\) to \(\log n\le d\log d+O(d)\).

## Theorem 2: asymptotically sharp zero-diagonal bound

Define
\[
\rho_0(n)=
\min\left\{\operatorname{rank}A:
a_{ii}=0,\ a_{ij}\in\Gamma\ (i\ne j)\right\}.
\]
Then
\[
\boxed{\quad \rho_0(n)=\sqrt{2n}+O(1).\quad}
\tag{3}
\]
More precisely, putting
\[
\varepsilon_n=\mathbf 1_{\{n\equiv1\pmod3\}},
\]
every such matrix of rank \(d\) satisfies
\[
n-\varepsilon_n\le \binom{d+1}{2},
\tag{4}
\]
and for every \(m\ge3\) there is an example of order \(\binom m2\) and rank exactly \(m\).

Theorem 1 is proved below by an elementary \(2\)-adic counting argument and a dimension-reduction argument. Theorem 2 verifies and retains the useful part of the previous attempt.

# 2. Counting nondegenerate equations in powers of two

A solution of
\[
a_1z_1+\cdots+a_mz_m=0,
\qquad z_i\in\Gamma,
\tag{5}
\]
is **nondegenerate** if no nonempty proper subsum vanishes. Two solutions are identified if one is obtained from the other by multiplying every coordinate by the same element of \(\Gamma\).

## Lemma 3

For any nonzero complex coefficients \(a_1,\dots,a_m\), \(m\ge2\), equation (5) has at most
\[
B_m=(2m-3)!!
\tag{6}
\]
nondegenerate solutions up to common scaling.

### Proof

We first explain how to use a \(2\)-adic order with complex coefficients, without asserting that the usual \(2\)-adic valuation is defined on \(\mathbb C\).

Let \(E\) be the finite-dimensional \(\mathbb Q\)-vector space spanned by \(a_1,\dots,a_m\), and choose a \(\mathbb Q\)-basis \(b_1,\dots,b_h\). For
\[
c=\sum_{\ell=1}^h q_\ell b_\ell\ne0,
\]
define
\[
\nu(c)=\min_{\ell:q_\ell\ne0}v_2(q_\ell),
\qquad \nu(0)=+\infty.
\]
Then
\[
\nu(2^kc)=k+\nu(c).
\tag{7}
\]
Also, in any zero sum of nonzero elements of \(E\), the minimum of their \(\nu\)-values is attained at least twice. Indeed, if one term uniquely attained the minimum, a coordinate attaining that minimum could not cancel.

Consider a nondegenerate solution of (5). Choose two terms of minimum \(\nu\)-value and replace them by their sum. While more than two terms remain, that sum is nonzero, by nondegeneracy. Continue until the final two terms are merged to zero.

This procedure produces a rooted, non-plane, full binary tree whose leaves are labelled \(1,\dots,m\). At every internal node, its two child sums have equal \(\nu\)-value.

**A fixed tree determines at most one projective solution.** To see this, work upwards from its leaves. Once the relative variables in a child subtree are determined, its sum has the form
\[
c\,z_i
\]
for a fixed nonzero \(c\in E\) and a chosen representative leaf \(i\). If the two child sums are \(c z_i\) and \(c' z_j\), equality of their orders forces
\[
\frac{z_i}{z_j}=2^{\nu(c')-\nu(c)}.
\tag{8}
\]
Thus their relative scaling is uniquely determined. Proper subtree sums must be nonzero; a tree violating this requirement contributes no nondegenerate solution. At the root, the additional requirement that the sum vanish can only discard the candidate.

There are \((2m-3)!!\) rooted non-plane full binary trees with \(m\) labelled leaves. This count follows inductively by inserting the last leaf into one of \(2m-3\) positions, including the stem above the root. The claimed bound follows. ∎

In particular, for nonzero complex \(c_1,\dots,c_s\),
\[
c_1u_1+\cdots+c_su_s=1,\qquad u_i\in\Gamma,
\tag{9}
\]
has at most
\[
(2s-1)!!
\tag{10}
\]
nondegenerate solutions. Here nondegeneracy refers to the zero-sum equation obtained by moving \(1\) to the left.

# 3. An exceptional-evaluation lemma

The next lemma converts this counting result into a rank bound.

## Lemma 4

Suppose
\[
x_1,\dots,x_N\in\Gamma^q
\]
and \(f_1,\dots,f_N\) are complex homogeneous linear forms in \(q\) variables such that
\[
f_i(x_i)\notin\Gamma,
\qquad
f_i(x_j)\in\Gamma\quad(i\ne j).
\tag{11}
\]
Then
\[
N\le P_q:=3^{q-1}q!.
\tag{12}
\]

### Proof

We induct on \(q\).

For \(q=1\), write \(f_i(X)=c_iX\). Since \(x_i\in\Gamma\), the exceptional condition gives \(c_i\notin\Gamma\). But then \(c_i x_j\notin\Gamma\) for every \(j\). Hence \(N\le1=P_1\).

Now let \(q\ge2\). We may assume \(N\ge2\). Fix one of the forms, say
\[
f(X)=f_1(X)=\sum_{k\in T}c_kX_k,
\]
where all \(c_k\ne0\), and put \(t=|T|\). Necessarily \(t\ge2\): a zero or one-term form cannot have both an exceptional evaluation and a nonexceptional evaluation on \(\Gamma^q\).

## 3.1. Covering the other points by proper subspaces

Suppose \(x\in\Gamma^q\) and \(f(x)=y\in\Gamma\). In the zero-sum relation
\[
\sum_{k\in T}c_kx_k-y=0,
\]
choose an inclusion-minimal zero-sum subset containing \(-y\). It is nondegenerate: a zero subsum not containing \(-y\) could be removed, contradicting minimality.

Consequently, for some nonempty \(S\subseteq T\),
\[
\sum_{k\in S}c_ku_k=1,
\qquad
u_k=\frac{x_k}{y}\in\Gamma,
\tag{13}
\]
is nondegenerate.

For a fixed \(S\) of size \(s\), Lemma 3 gives at most
\[
C_s:=(2s-1)!!
\]
possibilities for \(u=(u_k)_{k\in S}\). Each possibility defines a linear subspace
\[
V_{S,u}
=
\{X\in\mathbb C^q:X_k=u_kf(X)\text{ for every }k\in S\}.
\tag{14}
\]
Thus all \(x_j\), \(j\ne1\), are covered by these subspaces.

Their dimensions are
\[
\dim V_{S,u}=
\begin{cases}
q-s,&S\ne T,\\
q-t+1,&S=T.
\end{cases}
\tag{15}
\]
Indeed, the defining rows are \(e_k^{\mathsf T}-u_kc^{\mathsf T}\). If \(S\ne T\), a coordinate of \(c\) outside \(S\) shows these rows are independent. If \(S=T\), the relation \(\sum_{k\in T}c_ku_k=1\) makes their rank exactly \(t-1\).

All these subspaces are proper. Moreover, none contains \(x_1\): membership in \(V_{S,u}\), together with \(x_1\in\Gamma^q\), would give
\[
f(x_1)=x_{1k}/u_k\in\Gamma.
\]

## 3.2. Restricting to a subspace preserves the problem

Let \(V\) be one of these subspaces, of dimension \(h\). Choose \(h\) original coordinate functions whose restrictions form coordinates on \(V\). The resulting coordinate projection
\[
\pi:V\longrightarrow\mathbb C^h
\]
is a linear isomorphism.

Every projected point \(\pi(x_j)\), \(x_j\in V\), still belongs to \(\Gamma^h\), because projection merely retains original coordinates. Restricting the corresponding forms \(f_j\) to \(V\), then composing with \(\pi^{-1}\), preserves (11). By induction, \(V\) contains at most \(P_h\) of the indexed points.

Counting points in the covering subspaces, allowing overlaps, gives
\[
N\le
1+
\sum_{s=1}^{t-1}\binom ts C_sP_{q-s}
+
C_tP_{q-t+1}.
\tag{16}
\]

## 3.3. Bounding the recurrence

Define
\[
b_s=\frac{C_s}{3^s s!},
\qquad
r_t=\frac1{3^{t-1}t!}.
\]
Since \(q\ge t\), division of (16) by \(P_q\) gives
\[
\frac{N}{P_q}
\le
R_t:=
r_t+\sum_{s=1}^{t-1}b_s+3b_t.
\tag{17}
\]
For the proper-subset terms, this uses
\[
\frac{\binom ts C_sP_{q-s}}{P_q}
=
\frac{\binom ts}{\binom qs}\frac{C_s}{3^ss!}
\le b_s.
\]
For the final term, it uses
\[
\frac{C_tP_{q-t+1}}{P_q}
\le \frac{C_t}{3^{t-1}t!}=3b_t.
\]

Now
\[
R_2=\frac16+\frac13+\frac12=1,
\]
and
\[
\frac{b_{t+1}}{b_t}=\frac{2t+1}{3(t+1)}.
\]
Therefore
\[
R_{t+1}-R_t
=
(r_{t+1}-r_t)+3b_{t+1}-2b_t
=
(r_{t+1}-r_t)-\frac{b_t}{t+1}<0.
\]
Thus \(R_t\le1\) for every \(t\ge2\). Equation (17) proves \(N\le P_q\), completing the induction. ∎

# 4. Proof of the factorial rank bound

Choose \(d\) linearly independent rows of \(A\), indexed by a set \(R\). For each column \(j\notin R\), define
\[
x_j=(a_{rj})_{r\in R}\in\Gamma^d.
\tag{18}
\]
These coordinates are all off-diagonal entries.

Every row \(i\notin R\) is a linear combination of the chosen rows. Let \(f_i\) be the corresponding homogeneous linear form. Then, for all \(i,j\notin R\),
\[
f_i(x_j)=a_{ij}.
\]
The diagonal and off-diagonal hypotheses give exactly the exceptional-evaluation conditions (11).

Lemma 4 therefore gives
\[
n-d\le P_d=3^{d-1}d!,
\]
proving Theorem 1.

Taking logarithms and using Stirling’s formula,
\[
\log n\le d\log d+(\log3-1)d+O(\log d).
\]
The asymptotic lower bound in (2) follows.

### Extension to rational cyclic groups

The same factorial bound holds with \(\Gamma=b^{\mathbb Z}\) for any positive rational \(b\ne1\). Choose a prime \(p\) with \(v_p(b)\ne0\), and replace the coordinatewise \(2\)-adic order by the corresponding \(p\)-adic order. Equality of two orders uniquely determines the exponent difference in \(b^{\mathbb Z}\), if such a difference exists. All subsequent arguments are unchanged.

# 5. Zero diagonal: the stronger, sharp-order result

Here the congruence argument gives much more than Theorem 1.

## 5.1. Lower bound

Let \(A\) have zero diagonal and off-diagonal entries in \(\Gamma\), and set
\[
C=A^{\circ2}=(a_{ij}^2).
\]
If \(\operatorname{rank}A=d\), then
\[
\operatorname{rank}C\le\binom{d+1}{2}.
\tag{19}
\]
Indeed, factoring \(a_{ij}=u_i\cdot v_j\), the expansion
\[
(u_i\cdot v_j)^2
=
\sum_pu_{ip}^2v_{jp}^2
+
2\sum_{p<q}u_{ip}u_{iq}v_{jp}v_{jq}
\]
factors \(C\) through the space of homogeneous quadratic monomials in \(d\) variables.

The entries of \(C\) lie in \(\mathbb Z[1/2]\). Reducing modulo \(3\),
\[
C\equiv J_n-I_n,
\tag{20}
\]
because \(4^k\equiv1\pmod3\) for every integer \(k\). Negative exponents cause no problem because \(2\) is invertible modulo \(3\).

Reduction cannot increase rank: every vanishing rational minor also vanishes after reduction. Hence
\[
\operatorname{rank}_{\mathbb F_3}(J_n-I_n)
\le \operatorname{rank}_{\mathbb Q}C
\le\binom{d+1}{2}.
\]
Finally,
\[
\operatorname{rank}_{\mathbb F_3}(J_n-I_n)=n-\varepsilon_n.
\]
To check this, if \((J-I)x=0\) and \(s=\sum_jx_j\), then \(x=s\mathbf1\) and \((n-1)s=0\).

This proves (4).

## 5.2. Matching leading-order construction

Fix \(m\ge3\), and index rows and columns by
\[
\mathcal E=\binom{[m]}2.
\]
Define
\[
D_{EF}=|E\triangle F|.
\]
Its diagonal entries are zero, and its off-diagonal entries are \(2\) or \(4\).

Let \(X\) be the \(\binom m2\times m\) incidence matrix of the two-element subsets. Then
\[
D=4J-2XX^{\mathsf T}
  =X(J_m-2I_m)X^{\mathsf T}.
\tag{21}
\]
Also,
\[
X^{\mathsf T}X=(m-2)I_m+J_m,
\]
so \(X\) has column rank \(m\). The matrix \(J_m-2I_m\) is invertible for \(m\ge3\). Consequently,
\[
\operatorname{rank}D=m.
\tag{22}
\]

For arbitrary \(n\ge2\), choose
\[
m=\left\lceil\frac{1+\sqrt{1+8n}}2\right\rceil
\]
and take an \(n\times n\) principal submatrix of this construction. Combining upper and lower bounds gives
\[
\left\lceil
\frac{\sqrt{1+8(n-\varepsilon_n)}-1}{2}
\right\rceil
\le \rho_0(n)\le
\left\lceil\frac{1+\sqrt{1+8n}}2\right\rceil.
\tag{23}
\]
Thus \(\rho_0(n)=\sqrt{2n}+O(1)\), as asserted.

# 6. What remains unresolved

1. **Arbitrary excluded diagonals.** The factorial bound is not shown to be sharp. The results here give a lower bound of order \(\log n/\log\log n\), while zero-diagonal examples provide an upper bound of order \(\sqrt n\) for the minimum rank in this broader class.

2. **General multiplicative groups of rank \(r\).** The proof exploits a special feature of rational cyclic groups: a nontrivial \(p\)-adic order uniquely determines an element’s exponent. It does not establish a comparable uniform bound for arbitrary rank-\(r\) multiplicative groups.

3. **Exact zero-diagonal extremal values.** Equation (23) leaves an additive \(O(1)\) uncertainty in rank.

4. **Literature status.** The arguments are self-contained, but I have not independently checked whether the factorial bound or its proof has appeared previously.

The crucial distinction from the previous attempt is that Theorem 1 genuinely permits nonzero diagonal entries outside \(2^{\mathbb Z}\). The modulo-\(3\) proof alone does not: for example, \(5\notin2^{\mathbb Z}\), but \(5^2\equiv1\pmod3\), so that reduction would fail to distinguish such a diagonal entry from an off-diagonal entry.