```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "Under the source's zero-diagonal hypothesis, reduction modulo 3 of the Hadamard square proves that the minimum rank is sqrt(2n)+O(1), and a two-subset distance matrix shows this is asymptotically sharp.",
  "would_publish": false,
  "caveats": "This asymptotically settles only the integer-powers-of-2 case; the exact extremal value and the general small-rank-group problem remain open, and without zero diagonal no rank bound is possible."
}
```

## 1. Precise formulation

A diagonal hypothesis is indispensable. If the diagonal is unrestricted, the all-ones matrix has rank \(1\) and all its off-diagonal entries are \(1=2^0\). I therefore use the zero-diagonal formulation underlying the source theorem.

For \(n\ge 2\), define
\[
\rho_2(n)=\min \left\{\operatorname{rank}_{\mathbb Q}A:
a_{ii}=0,\quad a_{ij}=2^{k_{ij}}\ (i\ne j),\quad k_{ij}\in\mathbb Z\right\}.
\]
Ranks over \(\mathbb Q,\mathbb R,\mathbb C\) agree here because all entries are rational.

The following gives an asymptotically sharp answer to the highlighted powers-of-two case.

### Theorem

Let \(A\) be an \(n\times n\) zero-diagonal matrix whose off-diagonal entries are integer powers of \(2\), and put \(d=\operatorname{rank}A\). Define
\[
\varepsilon_n=
\begin{cases}
1,& n\equiv 1\pmod 3,\\
0,& n\not\equiv 1\pmod 3.
\end{cases}
\]
Then
\[
n-\varepsilon_n\leq \binom{d+1}{2}.
\tag{1}
\]
In particular,
\[
d\geq
\left\lceil
\frac{\sqrt{1+8(n-\varepsilon_n)}-1}{2}
\right\rceil
\geq
\left\lceil
\frac{\sqrt{8n-7}-1}{2}
\right\rceil .
\tag{2}
\]

Conversely, for every \(d\geq3\), there is such a matrix of order
\[
n=\binom d2
\]
and rank exactly \(d\). Consequently,
\[
\rho_2(n)=\sqrt{2n}+O(1).
\tag{3}
\]

Thus the quoted bound \(\log n\lesssim d^8\) for rank-one multiplicative groups can, in this particular case, be replaced by the asymptotically sharp polynomial bound
\[
n\leq \frac{d(d+1)}2+1.
\]

The same lower bound applies if signs \(\pm2^k\) are also allowed.

---

## 2. Hadamard-square rank lemma

For a matrix \(M=(m_{ij})\), write
\[
M^{\circ 2}=(m_{ij}^2)
\]
for its entrywise square.

### Lemma
If \(M\) has rank \(d\) over a field of characteristic different from \(2\), then
\[
\operatorname{rank}(M^{\circ2})\leq \binom{d+1}{2}.
\tag{4}
\]

### Proof
Factor \(M=UV^{\mathsf T}\), where the rows of \(U,V\) are vectors \(u_i,v_j\in F^d\). Then
\[
m_{ij}^2=(u_i\cdot v_j)^2
=\sum_{p=1}^d u_{ip}^2v_{jp}^2
+2\sum_{1\leq p<q\leq d}
u_{ip}u_{iq}v_{jp}v_{jq}.
\]
This factors \(M^{\circ2}\) through the vector space of homogeneous quadratic monomials in \(d\) variables, of dimension \(\binom{d+1}{2}\). ∎

---

## 3. Proof of the lower bound

Set
\[
C=A^{\circ2}.
\]
By the lemma,
\[
\operatorname{rank}_{\mathbb Q}C\leq \binom{d+1}{2}.
\tag{5}
\]

All entries of \(C\) lie in the localization \(\mathbb Z[1/2]\). There is a reduction homomorphism
\[
\phi:\mathbb Z[1/2]\longrightarrow \mathbb F_3,
\qquad 2\longmapsto -1.
\]
This also handles negative exponents because \(2\) is invertible modulo \(3\).

For \(i\ne j\),
\[
c_{ij}=2^{2k_{ij}}=4^{k_{ij}}\equiv1\pmod3,
\]
while \(c_{ii}=0\). Hence
\[
\phi(C)=J_n-I_n
\tag{6}
\]
over \(\mathbb F_3\).

Reduction modulo \(3\) cannot increase rank: if \(C\) has rational rank \(t\), all its \((t+1)\)-minors vanish in \(\mathbb Z[1/2]\), and therefore their reductions vanish. Thus
\[
\operatorname{rank}_{\mathbb F_3}(J_n-I_n)
\leq \operatorname{rank}_{\mathbb Q}C
\leq \binom{d+1}{2}.
\tag{7}
\]

It remains to calculate the rank of \(J_n-I_n\) over \(\mathbb F_3\). If
\[
(J_n-I_n)x=0
\]
and \(s=\sum_jx_j\), then every coordinate satisfies \(x_i=s\). Summing gives
\[
s=ns,
\qquad\text{so}\qquad
(n-1)s=0.
\]
Therefore
\[
\operatorname{rank}_{\mathbb F_3}(J_n-I_n)=
\begin{cases}
n-1,&n\equiv1\pmod3,\\
n,&n\not\equiv1\pmod3.
\end{cases}
\tag{8}
\]
Combining (7) and (8) proves (1) and (2). ∎

---

## 4. Construction showing asymptotic sharpness

Fix \(m\geq3\), and index rows and columns by the two-element subsets
\[
\mathcal E=\binom{[m]}2,
\qquad N=|\mathcal E|=\binom m2.
\]
For \(E,F\in\mathcal E\), define
\[
D_{EF}=\|\mathbf 1_E-\mathbf 1_F\|_2^2=|E\triangle F|.
\]
Then
\[
D_{EF}=
\begin{cases}
0,&E=F,\\
2,&|E\cap F|=1,\\
4,&E\cap F=\varnothing.
\end{cases}
\]
Thus every off-diagonal entry is either \(2\) or \(4\).

Let \(X\) be the \(N\times m\) incidence matrix of the two-subsets:
\[
X_{E,i}=1_{\{i\in E\}}.
\]
Since every row of \(X\) has sum \(2\),
\[
D=4J_N-2XX^{\mathsf T}
   =X(J_m-2I_m)X^{\mathsf T}.
\tag{9}
\]

Now
\[
X^{\mathsf T}X=(m-2)I_m+J_m.
\]
Its eigenvalues are \(m-2\) on \(\mathbf1^\perp\) and \(2m-2\) on the all-ones vector, so \(X\) has column rank \(m\). Moreover, \(J_m-2I_m\) has eigenvalues \(-2\) on \(\mathbf1^\perp\) and \(m-2\) on the all-ones vector, hence it is invertible for \(m\geq3\). It follows from (9) that
\[
\operatorname{rank}D=m.
\]

Therefore, for every \(d\geq3\), there is a valid matrix of rank \(d\) and order \(\binom d2\).

For arbitrary \(n\), choose
\[
m=\left\lceil\frac{1+\sqrt{1+8n}}2\right\rceil,
\]
so that \(\binom m2\geq n\), and take any \(n\times n\) principal submatrix of \(D\). This gives
\[
\rho_2(n)\leq
\left\lceil\frac{1+\sqrt{1+8n}}2\right\rceil.
\tag{10}
\]
Together with (2), this proves
\[
\rho_2(n)=\sqrt{2n}+O(1).
\]

Equivalently, if \(M_2(d)\) is the largest order of such a matrix of rank at most \(d\), then
\[
\binom d2\leq M_2(d)\leq \binom{d+1}{2}+1,
\]
and hence
\[
M_2(d)=\frac12d^2+O(d).
\]

---

## 5. A general finite-field version

The same method applies whenever the allowed multiplicative group has a finite-field specialization of small exponent.

Suppose an integer \(b\) is nonzero modulo a prime \(p\), and its multiplicative order modulo \(p\) is \(t\). For a zero-diagonal matrix with off-diagonal entries in \(b^{\mathbb Z}\), the \(t\)-th Hadamard power reduces modulo \(p\) to \(J-I\). Since
\[
\operatorname{rank}(A^{\circ t})\leq \binom{d+t-1}{t},
\]
one obtains
\[
n-\mathbf1_{\,n\equiv1\pmod p}
\leq \binom{d+t-1}{t}.
\]
The powers-of-two result is the particularly strong case \(p=3\), \(t=2\).

---

## 6. Remaining gaps and scope

1. The exact finite-\(n\) value of \(\rho_2(n)\) is not determined. The lower and upper bounds differ by only \(O(1)\) in rank, but this additive gap remains.
2. This does not improve the uniform bound for arbitrary multiplicative groups of rank \(r\); it exploits the special congruence \(2^2\equiv1\pmod3\).
3. If arbitrary real powers \(2^\alpha\), rather than integer powers, are allowed, reduction modulo \(3\) is unavailable.
4. If the diagonal is not required to be zero or otherwise separated from the multiplicative group, the all-ones matrix is an immediate rank-one counterexample.
5. I have not independently verified whether this elementary modulo-\(3\) argument has appeared elsewhere, so no claim of literature novelty is made.