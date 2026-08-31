```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjectured range holds for graphs with fractional chromatic number \u03c7_f(G) satisfying \u03c7_f(G)d\\log n=o(n), in particular for every bipartite regular graph, while for arbitrary regular graphs one obtains optimal one-bin variance and concentration of a natural spacing predictor.",
  "would_publish": false,
  "caveats": "The simultaneous result for arbitrary high-chromatic regular graphs remains open; novelty relative to the literature has not been checked."
}
```

# 1. Statement of the problem

Let \(G\) be a finite simple \(d\)-regular graph on \(n\) vertices. Assign independent \(X_v\sim\mathrm{Unif}[0,1]\), and retain \(uv\in E(G)\) precisely when
\[
X_u+X_v\ge 1.
\]
Write
\[
m_k=m(H,k)=\bigl|\{v:\deg_H(v)=k\}\bigr|,\qquad 0\le k\le d,
\]
and put
\[
\mu=\frac{n}{d+1}.
\]

The conjecture asks whether, whenever \(d=o(n/\log n)\),
\[
\max_{0\le k\le d}|m_k-\mu|=o(\mu)
\]
with high probability, uniformly over all \(d\)-regular \(G\).

I do not prove this for arbitrary \(G\). I prove the following special case and two general estimates.

---

## Theorem A: the conjectured range for fractionally low-chromatic graphs

There are absolute constants \(c,C>0\) such that, for every \(d\ge1\), every \(d\)-regular graph \(G\), every \(0\le k\le d\), and \(W=\chi_f(G)\),
\[
\Pr\bigl(|m_k-\mu|\ge t\bigr)
 \le
2\exp\left[-c\min\left\{
\frac{t^2}{Wn/d},\,\frac{t}{W}
\right\}\right].
\tag{1}
\]

Consequently, if
\[
\chi_f(G)\,d\log n=o(n),
\tag{2}
\]
then with high probability
\[
m_k=(1+o(1))\frac{n}{d+1}
\qquad\text{simultaneously for all }0\le k\le d.
\tag{3}
\]

In particular, since a bipartite graph has \(\chi_f(G)\le2\), the original conjectured range
\[
d=o(n/\log n)
\]
is valid for every sequence of bipartite \(d\)-regular graphs. The same holds for every class of uniformly bounded chromatic number.

---

## Theorem B: an optimally concentrated predictor for arbitrary graphs

For every \(v\) and \(k\), let
\[
p_{v,k}=\Pr(\deg_H(v)=k\mid (X_u)_{u\in N(v)})
\]
and define
\[
S_k=\sum_v p_{v,k}.
\]
Then \(\mathbb E S_k=\mu\), and
\[
\Pr\bigl(|S_k-\mu|\ge t\bigr)
 \le
2\exp\left[-c\min\left\{
\frac{t^2}{n/d},\,t
\right\}\right].
\tag{4}
\]
Thus, under \(d=o(n/\log n)\),
\[
\max_{0\le k\le d}|S_k-\mu|=o(\mu)
\]
with high probability for every \(d\)-regular graph.

---

## Theorem C: optimal one-bin variance for arbitrary graphs

For every \(d\)-regular \(G\) and every \(k\),
\[
\operatorname{Var}(m_k)\le C\frac nd.
\tag{5}
\]
Consequently, for any choice \(k=k(n)\), if \(d=o(n)\), then
\[
m_k=(1+o_{\mathbb P}(1))\frac{n}{d+1}.
\tag{6}
\]
Moreover,
\[
\mathbb E\left[
\frac1{d+1}\sum_{k=0}^d
 \left(\frac{m_k-\mu}{\mu}\right)^2
\right]
 \le C\frac dn.
\tag{7}
\]
Hence, for \(d=o(n)\), all but \(o_{\mathbb P}(d)\) degree values \(k\) satisfy the desired asymptotic. What is missing is control of the maximum over all \(k\).

# 2. Spacings and a read-\(R\) Hölder inequality

Set
\[
T_u=1-X_u.
\]
Conditional on \(X_v=x\),
\[
\deg_H(v)=\bigl|\{u\in N(v):T_u\le x\}\bigr|.
\]

Order the \(d\) values \((T_u)_{u\in N(v)}\) as
\[
0=T_{v,(0)}<T_{v,(1)}<\cdots<T_{v,(d)}<T_{v,(d+1)}=1.
\]
Then
\[
p_{v,k}=T_{v,(k+1)}-T_{v,(k)}.
\tag{8}
\]
Every spacing in \(d\) independent uniform points has the \(\operatorname{Beta}(1,d)\) distribution. Thus
\[
\mathbb E p_{v,k}=\frac1{d+1}.
\tag{9}
\]

We use the following standard product-space Hölder inequality.

### Lemma 2.1

Let \(Z_1,\dots,Z_N\) be independent. Suppose nonnegative \(f_i\) depends only on coordinates indexed by \(A_i\), and each coordinate belongs to at most \(R\) of the sets \(A_i\). Then
\[
\mathbb E\prod_i f_i
 \le
\prod_i\bigl(\mathbb E f_i^R\bigr)^{1/R}.
\tag{10}
\]

More generally, if weights \(\alpha_i\ge0\) satisfy
\[
\sum_{i:j\in A_i}\alpha_i\le1
\]
for every coordinate \(j\), then
\[
\mathbb E\prod_i f_i^{\alpha_i}
 \le
\prod_i(\mathbb E f_i)^{\alpha_i}.
\]
This follows by repeated generalized Hölder integration over the independent coordinates. Equation (10) is obtained by taking \(\alpha_i=1/R\) and replacing \(f_i\) by \(f_i^R\).

Let \(B\sim\operatorname{Beta}(1,d)\) and \(Y=dB\). Then
\[
\Pr(Y\ge y)=\left(1-\frac yd\right)^d\le e^{-y},
\qquad 0\le y\le d.
\tag{11}
\]
In particular, uniformly in \(d\),
\[
\log\mathbb E e^{\theta Y}-\theta\mathbb EY\le C\theta^2
\qquad (|\theta|\le \theta_0)
\tag{12}
\]
for absolute \(C,\theta_0>0\). One can also see this from
\[
\mathbb E Y^r
 =d^r\frac{r!\,d!}{(d+r)!}\le r!.
\]

# 3. Concentration on an independent vertex set

Let \(I\subseteq V(G)\) be independent, \(s=|I|\), and define
\[
M_{I,k}=\sum_{v\in I}\mathbf 1_{\{\deg_H(v)=k\}}.
\]

Condition on all labels outside \(I\). Since \(I\) is independent, every neighborhood \(N(v)\), \(v\in I\), lies outside \(I\). Therefore the indicators indexed by \(I\) are conditionally independent Bernoulli variables with respective success probabilities \(p_{v,k}\). Hence, for any real \(\lambda\),
\[
\begin{aligned}
\mathbb E\left[e^{\lambda M_{I,k}}\mid (X_u)_{u\notin I}\right]
 &=\prod_{v\in I}\left(1+(e^\lambda-1)p_{v,k}\right)\\
 &\le \exp\left((e^\lambda-1)\sum_{v\in I}p_{v,k}\right).
\end{aligned}
\tag{13}
\]

Each outside label occurs in at most \(d\) of the functions \(p_{v,k}\). Applying Lemma 2.1 with
\[
a=e^\lambda-1
\]
gives
\[
\mathbb E e^{\lambda M_{I,k}}
 \le
\left(\mathbb E e^{adB}\right)^{s/d}.
\tag{14}
\]
Since
\[
\mathbb E M_{I,k}=\frac{s}{d+1}
 =\frac sd\,\mathbb EY,
\]
(12), together with \(e^\lambda-1-\lambda=O(\lambda^2)\), yields
\[
\log\mathbb E
 \exp\left(\lambda\left(M_{I,k}-\frac{s}{d+1}\right)\right)
 \le C\frac sd\,\lambda^2
\qquad (|\lambda|\le\lambda_0).
\tag{15}
\]
Chernoff optimization gives
\[
\Pr\left(
\left|M_{I,k}-\frac{s}{d+1}\right|\ge t
\right)
 \le
2\exp\left[-c\min\left\{
\frac{t^2}{s/d},\,t
\right\}\right].
\tag{16}
\]

This is the main estimate behind Theorem A.

# 4. Fractional colorings

We use an exact fractional decomposition into independent sets. Namely, there are independent sets \(I_j\) and weights \(a_j\ge0\) such that
\[
\sum_{j:v\in I_j}a_j=1\quad\text{for every }v,
\qquad
\sum_j a_j=W,
\tag{17}
\]
where \(W\) may be taken arbitrarily close to \(\chi_f(G)\).

The equality version of (17) is equivalent to the usual covering definition. Indeed, if a fractional coloring overcovers some vertex, split the weight of each independent set among its subsets, retaining each occurrence of vertex \(v\) with the appropriate probability; subsets of independent sets remain independent.

From (17),
\[
m_k=\sum_j a_jM_{I_j,k}
\]
and
\[
\mu=\sum_j a_j\frac{|I_j|}{d+1}.
\]

Apply Hölder with exponents
\[
q_j=\frac W{a_j}.
\]
Since \(\sum_j1/q_j=1\),
\[
\begin{aligned}
\mathbb E e^{\lambda(m_k-\mu)}
&\le
\prod_j
\left[
\mathbb E
 e^{\lambda W(M_{I_j,k}-|I_j|/(d+1))}
\right]^{a_j/W}\\
&\le
\exp\left(
C\frac{Wn}{d}\lambda^2
\right),
\qquad |\lambda|\le \frac{\lambda_0}{W}.
\end{aligned}
\tag{18}
\]
Here we used
\[
\sum_j a_j|I_j|=n.
\]
Chernoff optimization proves (1).

For \(0<\varepsilon\le1\), since \(\mu\asymp n/d\),
\[
\Pr\bigl(|m_k-\mu|\ge\varepsilon\mu\bigr)
 \le
2\exp\left(-c\varepsilon^2\frac{n}{Wd}\right).
\tag{19}
\]
Taking a union bound over \(d+1\le n\) degree values proves Theorem A. Explicitly, if
\[
L_n=\frac{n}{Wd\log n}\longrightarrow\infty,
\]
choose \(\varepsilon_n=L_n^{-1/4}\). Then
\[
(d+1)\exp\left(-c\varepsilon_n^2\frac{n}{Wd}\right)
 \le
n\exp(-cL_n^{1/2}\log n)=o(1).
\]

# 5. The spacing predictor for arbitrary graphs

Define
\[
S_k=\sum_{v\in V(G)}p_{v,k}.
\]
Each \(p_{v,k}\) depends on the \(d\) labels in \(N(v)\), and every label \(X_u\) occurs in exactly \(d\) such neighborhood functions. Hence Lemma 2.1 gives
\[
\mathbb E e^{\theta S_k}
 \le
\left(\mathbb E e^{\theta dB}\right)^{n/d}.
\tag{20}
\]
Since \(\mathbb ES_k=n/(d+1)\), (12) implies
\[
\log\mathbb E e^{\theta(S_k-\mu)}
 \le C\frac nd\,\theta^2
\qquad (|\theta|\le\theta_0).
\tag{21}
\]
This proves (4).

In particular, for \(0<\varepsilon\le1\),
\[
\Pr\bigl(|S_k-\mu|\ge\varepsilon\mu\bigr)
 \le 2e^{-c\varepsilon^2n/d}.
\tag{22}
\]
Thus the predictors \(S_k\) satisfy Property \((*)\) simultaneously throughout the conjectured range.

# 6. Variance of the residual

Let
\[
I_{v,k}=\mathbf 1_{\{\deg_H(v)=k\}},
\qquad
A_{v,k}=I_{v,k}-p_{v,k},
\qquad
R_k=\sum_v A_{v,k}.
\]
Then
\[
m_k=S_k+R_k.
\tag{23}
\]

We prove
\[
\operatorname{Var}(R_k)\le C\frac nd.
\tag{24}
\]

First,
\[
\mathbb E A_{v,k}^2
 =\mathbb E[p_{v,k}(1-p_{v,k})]
 \le\frac1{d+1}.
\tag{25}
\]

If \(v\) and \(w\) are nonadjacent, condition on all labels except \(X_v,X_w\). Under this conditioning \(A_{v,k}\) is a mean-zero function of \(X_v\), and \(A_{w,k}\) is a mean-zero function of \(X_w\). Therefore
\[
\mathbb E[A_{v,k}A_{w,k}]=0
\qquad (vw\notin E(G)).
\tag{26}
\]

It remains to control adjacent pairs. Fix \(vw\in E(G)\). Let
\[
U_v=\left\{
x:\left|\{u\in N(v)\setminus\{w\}:T_u\le x\}\right|
 \in\{k-1,k\}
\right\},
\]
with invalid counts omitted, and set \(Q_v=|U_v|\). Define \(U_w,Q_w\) analogously.

The set \(U_v\) is the union of at most two consecutive spacings determined by \(d-1\) independent uniform points. Therefore
\[
\mathbb E Q_v^2\le \frac{6}{d(d+1)}\le\frac6{d^2}.
\tag{27}
\]
Moreover,
\[
I_{v,k}\le\mathbf 1_{\{X_v\in U_v\}},
\qquad
p_{v,k}\le Q_v.
\tag{28}
\]
The variables \(Q_v,Q_w\) do not depend on \(X_v,X_w\). Hence, by conditioning on all other labels and then using Cauchy–Schwarz,
\[
\begin{aligned}
\mathbb E[I_{v,k}I_{w,k}]&\le\mathbb E[Q_vQ_w]\le \frac6{d^2},\\
\mathbb E[I_{v,k}p_{w,k}]&\le\mathbb E[Q_vQ_w]\le \frac6{d^2},\\
\mathbb E[p_{v,k}I_{w,k}]&\le\mathbb E[Q_vQ_w]\le \frac6{d^2},\\
\mathbb E[p_{v,k}p_{w,k}]&\le\mathbb E[Q_vQ_w]\le \frac6{d^2}.
\end{aligned}
\tag{29}
\]
Consequently,
\[
\left|\mathbb E[A_{v,k}A_{w,k}]\right|
 \le\frac{24}{d^2}.
\tag{30}
\]

Since \(G\) has \(nd/2\) edges, (25), (26), and (30) give
\[
\operatorname{Var}(R_k)
 \le \frac{n}{d+1}
   +2\frac{nd}{2}\frac{24}{d^2}
 \le C\frac nd.
\]
Together with (21),
\[
\operatorname{Var}(S_k)\le C\frac nd.
\]
Finally,
\[
\operatorname{Var}(m_k)
 \le2\operatorname{Var}(S_k)+2\operatorname{Var}(R_k)
 \le C\frac nd,
\]
proving Theorem C.

# 7. Consequences and the remaining gap

Chebyshev's inequality gives, for every \(k\),
\[
\Pr\bigl(|m_k-\mu|\ge\varepsilon\mu\bigr)
 \le C\frac{d}{\varepsilon^2n}.
\tag{31}
\]
This proves the one-bin assertion whenever \(d=o(n)\).

Summing the variance bound over \(k\) gives
\[
\begin{aligned}
\mathbb E\left[
\frac1{d+1}\sum_{k=0}^d
 \left(\frac{m_k-\mu}{\mu}\right)^2
\right]
&\le
\frac{C(n/d)}{\mu^2}\\
&\le C\frac dn,
\end{aligned}
\]
which proves (7).

The missing step for arbitrary \(G\) is an exponential-tail estimate for
\[
R_k=\sum_v\left(
\mathbf 1_{\{\deg_H(v)=k\}}-p_{v,k}
\right).
\]
The variance calculation shows the correct scale \(n/d\), and nonadjacent summands are exactly orthogonal, even when their neighborhoods overlap. However, they are not independent: higher-order correlations can pass through shared neighbors. A bound of the form
\[
\Pr(|R_k|\ge t)
 \le
2\exp\left[-c\min\left\{
\frac{t^2}{n/d},\,t
\right\}\right]
\tag{32}
\]
would complete the conjecture immediately, because \(S_k\) already satisfies this estimate. I do not have a proof of (32) for arbitrary high-chromatic regular graphs. The fractional-coloring argument proves the required concentration when \(\chi_f(G)d\log n=o(n)\), but its loss of a factor \(\chi_f(G)\) is prohibitive for graphs such as unions of large cliques.