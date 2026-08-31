```json
{
  "verdict": "proved",
  "confidence": "high",
  "one_line": "A Gaussian quotient map, together with a localized Gaussian-width estimate for an absolute convex hull, gives the target dimension and uniformly bounded output norms.",
  "would_publish": true,
  "caveats": "Absolute constants absorb the floor; the proof uses the standard Gordon Gaussian min-max lemma, stated explicitly below."
}
```

## Statement

The following proves the conjecture, in a slightly stronger one-sided form.

### Theorem

There are absolute constants \(C,K>0\) such that the following holds. Let
\[
x_1,\dots,x_n,\quad y_1,\dots,y_m
\]
belong to the unit ball of a real Hilbert space \(H\), and let \(0<\varepsilon<1\). Then there are vectors
\[
p_1,\dots,p_n,\quad q_1,\dots,q_m\in\mathbb R^t,
\]
where
\[
t\le
C\frac{\log(2+\varepsilon^2 n)}{\varepsilon^2},
\]
such that
\[
\|p_i\|_2,\ \|q_j\|_2\le K
\]
and
\[
\left|\langle p_i,q_j\rangle-\langle x_i,y_j\rangle\right|
\le \varepsilon
\qquad(1\le i\le n,\ 1\le j\le m).
\]

In fact, after \(p_1,\ldots,p_n\) have been chosen, the conclusion holds simultaneously for every \(y\) in the unit ball of \(H\), with a suitable \(q=q(y)\).

Taking \(m=n\) proves the conjecture from the catalog.

---

## 1. A localized Gaussian-width estimate

For a bounded set \(L\) in a finite-dimensional Hilbert space, write
\[
w(L)=\mathbb E\sup_{z\in L}\langle g,z\rangle,
\]
where \(g\) is a standard Gaussian vector in the ambient span.

### Lemma 1

Let \(v_1,\dots,v_n\) belong to the unit ball of a Hilbert space, and put
\[
K=\operatorname{conv}\{0,\pm v_1,\dots,\pm v_n\}.
\]
For every \(R\ge1\),
\[
w(RK\cap B_2)
\le
C_1R\sqrt{\log\left(2+\frac n{R^2}\right)}
\]
for an absolute constant \(C_1\).

### Proof

Set \(m=\lceil R^2\rceil\), and let
\[
\mathcal A=\{0,\pm v_1,\dots,\pm v_n\}.
\]
Define the finite set
\[
\mathcal Z_m=
\left\{
\frac Rm\sum_{\ell=1}^m a_\ell:
a_\ell\in\mathcal A
\right\}.
\]
Since only the multiplicities of the atoms matter,
\[
|\mathcal Z_m|
\le
\binom{2n+m}{m}
=:N.
\]

Fix \(h\in RK\cap B_2\). There is an \(\mathcal A\)-valued random variable \(X\) such that
\[
\mathbb EX=\frac hR.
\]
Let \(X_1,\dots,X_m\) be independent copies of \(X\), and set
\[
Z=\frac Rm\sum_{\ell=1}^m X_\ell.
\]
Then \(\mathbb EZ=h\), while
\[
\begin{aligned}
\mathbb E\|Z\|_2^2
&=
\|h\|_2^2+
\frac{R^2}{m}
\left(\mathbb E\|X\|_2^2-\frac{\|h\|_2^2}{R^2}\right)\\
&\le 1+\frac{R^2}{m}
\le 2.
\end{aligned}
\]

Fix a Gaussian vector \(g\) and a number \(\lambda>0\). Since \(Z\in\mathcal Z_m\), some realization satisfies
\[
\langle g,Z\rangle-\lambda\|Z\|_2^2
\ge
\langle g,h\rangle-\lambda\mathbb E\|Z\|_2^2.
\]
Consequently,
\[
\langle g,h\rangle
\le
\max_{z\in\mathcal Z_m}
\bigl(\langle g,z\rangle-\lambda\|z\|_2^2\bigr)
+2\lambda.
\]
Taking the supremum over \(h\in RK\cap B_2\) and then expectation over \(g\), we obtain
\[
w(RK\cap B_2)
\le
\mathbb E\max_{z\in\mathcal Z_m}
\bigl(\langle g,z\rangle-\lambda\|z\|_2^2\bigr)
+2\lambda.
\]
The exponential-moment bound gives
\[
\begin{aligned}
\mathbb E\max_{z\in\mathcal Z_m}
\bigl(\langle g,z\rangle-\lambda\|z\|_2^2\bigr)
&\le
\frac1\lambda
\log\sum_{z\in\mathcal Z_m}
\mathbb E
e^{\lambda(\langle g,z\rangle-\lambda\|z\|_2^2)}\\
&=
\frac1\lambda
\log\sum_{z\in\mathcal Z_m}
e^{-\lambda^2\|z\|_2^2/2}\\
&\le \frac{\log N}{\lambda}.
\end{aligned}
\]
Choosing \(\lambda=\sqrt{\log N/2}\) yields
\[
w(RK\cap B_2)\le C\sqrt{\log N}.
\]

Finally,
\[
\log N
\le
m\log\left(e\left(1+\frac{2n}{m}\right)\right)
\le
C R^2\log\left(2+\frac n{R^2}\right).
\]
This proves the lemma. \(\square\)

---

## 2. A Gaussian escape lemma

We use the following standard consequence of Gordon's Gaussian min-max inequality.

### Lemma 2

Let \(S=-S\) be a compact subset of the unit sphere of a finite-dimensional Hilbert space, and let \(v_1,\dots,v_n\) be vectors of norm at most \(1\). If
\[
t\ge C_2\bigl(w(S)^2+\log(n+1)\bigr),
\]
then there is a linear map \(G:H\to\mathbb R^t\) satisfying
\[
\inf_{h\in S}\|Gh\|_2\ge \frac14
\]
and
\[
\max_{1\le i\le n}\|Gv_i\|_2\le 2.
\]

### Proof

Let \(\Gamma\) be a \(t\times\dim H\) matrix with independent \(N(0,1)\) entries, and put \(G=\Gamma/\sqrt t\).

Gordon's min-max inequality gives
\[
\mathbb E\inf_{h\in S}\|\Gamma h\|_2
\ge
\mathbb E\|g_t\|_2-w(S),
\]
where \(g_t\) is standard Gaussian in \(\mathbb R^t\). Since
\[
\mathbb E\|g_t\|_2\ge \sqrt t-1,
\]
the assumed lower bound on \(t\), followed by Gaussian concentration for the \(1\)-Lipschitz function
\[
\Gamma\longmapsto \inf_{h\in S}\|\Gamma h\|_2,
\]
shows that
\[
\inf_{h\in S}\|Gh\|_2\ge\frac14
\]
except with probability at most \(e^{-ct}\).

For each fixed \(v_i\) with \(\|v_i\|\le1\),
\[
\mathbb P\bigl(\|Gv_i\|_2>2\bigr)\le e^{-c't}.
\]
A union bound over \(i\), using \(t\ge C\log(n+1)\), shows that both asserted properties hold simultaneously with positive probability. \(\square\)

---

## 3. Construction of the bounded-norm factorization

Let
\[
H_0=\operatorname{span}\{x_1,\dots,x_n\}.
\]
Define the analysis operator
\[
T:H_0\longrightarrow\mathbb R^n,
\qquad
(Ty)_i=\langle x_i,y\rangle.
\]
Its adjoint is
\[
T^*z=\sum_{i=1}^n z_i x_i.
\]

On \(H_0\), define the atomic norm
\[
\rho(h)=
\inf\left\{
\sum_{i=1}^n|a_i|:
h=\sum_{i=1}^n a_i x_i
\right\}.
\]
Thus the unit ball of \(\rho\) is
\[
K=\operatorname{conv}\{0,\pm x_1,\dots,\pm x_n\}.
\]

Set
\[
R=\frac1\varepsilon
\]
and
\[
S_R=
\left\{
h\in H_0:
\|h\|_2=1,\ \rho(h)\le R
\right\}.
\]
By Lemma 1,
\[
w(S_R)
\le
C_1R\sqrt{\log\left(2+\frac n{R^2}\right)}
=
C_1\varepsilon^{-1}
\sqrt{\log(2+n\varepsilon^2)}.
\]
Moreover,
\[
R^2\log\left(2+\frac n{R^2}\right)
=
\varepsilon^{-2}\log(2+n\varepsilon^2)
\ge c\log(n+1),
\]
for \(R\ge1\). Hence Lemma 2 supplies a linear map
\[
G:H_0\longrightarrow\mathbb R^t,
\qquad
t\le C\varepsilon^{-2}\log(2+n\varepsilon^2),
\]
such that
\[
\inf_{h\in S_R}\|Gh\|_2\ge\frac14
\]
and
\[
\|Gx_i\|_2\le2
\qquad(1\le i\le n).
\]

Put
\[
p_i=Gx_i,
\]
and let \(P:\mathbb R^t\to\mathbb R^n\) be the operator
\[
(Pq)_i=\langle p_i,q\rangle.
\]
Then
\[
P^*z
=
\sum_i z_ip_i
=
G\left(\sum_i z_ix_i\right)
=
GT^*z.
\]

We claim that for every \(z\in\mathbb R^n\),
\[
\boxed{
\|T^*z\|_2
\le
4\|P^*z\|_2+\varepsilon\|z\|_1.
}
\tag{1}
\]

Indeed, let \(h=T^*z\). We always have
\[
\rho(h)\le\|z\|_1.
\]

If
\[
\rho(h)\le R\|h\|_2,
\]
then \(h/\|h\|_2\in S_R\), and therefore
\[
\|P^*z\|_2
=
\|Gh\|_2
\ge\frac14\|h\|_2.
\]

On the other hand, if
\[
\rho(h)>R\|h\|_2,
\]
then
\[
\|h\|_2
<
\frac{\rho(h)}R
\le
\frac{\|z\|_1}R
=
\varepsilon\|z\|_1.
\]
Thus (1) holds in both cases.

---

## 4. Duality gives all the right-hand vectors

Consider the two compact convex symmetric subsets of \(\mathbb R^n\)
\[
\mathcal C=T(B_{H_0})
\]
and
\[
\mathcal D=P(4B_2^t)+\varepsilon B_\infty^n.
\]
Their support functions satisfy
\[
h_{\mathcal C}(z)
=
\|T^*z\|_2
\]
and
\[
h_{\mathcal D}(z)
=
4\|P^*z\|_2+\varepsilon\|z\|_1.
\]
Inequality (1) therefore says
\[
h_{\mathcal C}(z)\le h_{\mathcal D}(z)
\qquad\text{for every }z\in\mathbb R^n.
\]
By the separating-hyperplane theorem,
\[
T(B_{H_0})
\subseteq
P(4B_2^t)+\varepsilon B_\infty^n.
\tag{2}
\]

Now let \(y\) be any vector of norm at most \(1\). Replacing \(y\) by its orthogonal projection onto \(H_0\) does not change \(Ty\). By (2), there is a vector \(q=q(y)\in\mathbb R^t\) with
\[
\|q\|_2\le4
\]
and
\[
\|Pq-Ty\|_\infty\le\varepsilon.
\]
Equivalently,
\[
\left|
\langle p_i,q\rangle-\langle x_i,y\rangle
\right|
\le\varepsilon
\qquad(1\le i\le n).
\]

Apply this to each \(y_j\), obtaining vectors \(q_j\) with \(\|q_j\|_2\le4\). Since \(\|p_i\|_2\le2\), all output norms are bounded by an absolute constant, and
\[
\left|
\langle p_i,q_j\rangle-\langle x_i,y_j\rangle
\right|
\le\varepsilon
\]
for every \(i,j\).

This proves the theorem.

---

## 5. Relation to the catalog formulation

For \(A_{ij}=\langle x_i,y_j\rangle\), the constructed matrix
\[
B_{ij}=\langle p_i,q_j\rangle
\]
satisfies
\[
\operatorname{rank}B\le t,\qquad
\|A-B\|_{\max}\le\varepsilon,
\]
and has a factorization with
\[
\max_i\|p_i\|_2\le2,\qquad
\max_j\|q_j\|_2\le4.
\]
Thus \(B\) has uniformly bounded \(\gamma_2\)-factorization norm.

If the dimension in the source is written as
\[
t=\left\lfloor
C\frac{\log(2+\varepsilon^2n)}{\varepsilon^2}
\right\rfloor,
\]
choose the absolute constant \(C\) sufficiently large and pad the vectors by zero coordinates. For \(\varepsilon\ge1\), the zero vectors already give error at most \(\varepsilon\). Hence all parameter cases are covered.

The construction is also algorithmic: sample the Gaussian map \(G\), and for each \(y_j\) solve the second-order-cone feasibility problem
\[
\|q_j\|_2\le4,\qquad
\|Pq_j-Ty_j\|_\infty\le\varepsilon.
\]
On the high-probability event used above, all these systems are feasible.