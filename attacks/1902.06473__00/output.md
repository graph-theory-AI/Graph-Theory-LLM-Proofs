```json
{
  "verdict": "proved",
  "confidence": "medium",
  "one_line": "Under normalized Lebesgue averaging on the chain polytope, QLB(P) lies between ln e(P) and (ln 2)^{-1}ln e(P), and hence between LB(P)/2 and LB(P)/ln 2.",
  "would_publish": false,
  "caveats": "The catalog omits the law used in QH(P), and the source conjecture is corrupted; the proof applies to uniform chain-polytope averaging, equivalently to the extension-gap formula derived below."
}
```

# Statement and interpretation

Let \(P\) be an \(n\)-element poset, let \(\mathcal L(P)\) be its set of linear extensions, and write
\[
e(P):=|\mathcal L(P)|.
\]
I interpret \(C(P)\) as the chain polytope
\[
C(P)=\left\{z\in \mathbb R_{\ge 0}^{P}:
  \sum_{v\in D}z_v\le 1\ \text{for every chain }D\subseteq P
 \right\},
\]
with normalized Lebesgue measure, and
\[
h(z)=-\frac1n\sum_{v\in P}\ln z_v,
\quad
H(P)=\min_{z\in C(P)}h(z),
\quad
QH(P)=\frac1{\operatorname{vol} C(P)}\int_{C(P)}h(z)\,dz.
\]
As in the question,
\[
\operatorname{LB}(P)=n(\ln n-H(P)),
\qquad
\operatorname{QLB}(P)=n(H_n-QH(P)),
\]
where \(H_m=\sum_{j=1}^m1/j\) and \(H_0=0\).

Under these definitions, I prove
\[
\boxed{\quad
 \ln e(P)\le \operatorname{QLB}(P)
 \le \frac{\ln e(P)}{\ln 2}.
 \quad}
\tag{1}
\]
The standard entropy–linear-extension estimate
\[
\ln e(P)\le \operatorname{LB}(P)\le 2\ln e(P)
\tag{2}
\]
then gives
\[
\boxed{\quad
 \frac12\operatorname{LB}(P)
 \le \operatorname{QLB}(P)
 \le \frac1{\ln 2}\operatorname{LB}(P).
 \quad}
\tag{3}
\]

Thus the inferred constant-factor conjecture follows, with explicit constants.

---

# 1. A linear-extension formula for \(\operatorname{QLB}\)

For a linear extension \(\sigma:P\to[n]\) and \(v\in P\), define
\[
p_\sigma(v)=
\max\bigl(\{\,\sigma(u):u<_P v\,\}\cup\{0\}\bigr),
\]
and
\[
r_\sigma(v)=\sigma(v)-p_\sigma(v)-1.
\tag{4}
\]
Thus \(r_\sigma(v)\) is the number of positions strictly between \(v\) and its latest predecessor in \(\sigma\).

## Lemma 1
Under normalized Lebesgue averaging on \(C(P)\),
\[
\operatorname{QLB}(P)
=
\frac1{e(P)}
\sum_{\sigma\in\mathcal L(P)}
\sum_{v\in P}H_{r_\sigma(v)}.
\tag{5}
\]

### Proof

Consider the order polytope
\[
O(P)=\{x\in[0,1]^P:x_u\le x_v\text{ whenever }u\le_Pv\}.
\]
It has the usual triangulation into the \(e(P)\) simplices
\[
0\le x_{\sigma^{-1}(1)}
   \le\cdots\le x_{\sigma^{-1}(n)}
   \le1,
\qquad \sigma\in\mathcal L(P),
\]
each of volume \(1/n!\).

The transfer map
\[
\Phi(x)_v=x_v-\max\bigl(\{x_u:u<_Pv\}\cup\{0\}\bigr)
\tag{6}
\]
is a piecewise-linear, measure-preserving bijection from \(O(P)\) to \(C(P)\). Consequently, a uniform point of \(C(P)\) may be obtained by:

1. choosing \(\sigma\in\mathcal L(P)\) uniformly;
2. choosing \(0\le t_1\le\cdots\le t_n\le1\) uniformly in the standard ordered simplex;
3. putting \(x_v=t_{\sigma(v)}\) and \(z=\Phi(x)\).

Let \(i=\sigma(v)\), \(p=p_\sigma(v)\), and \(d=i-p=r_\sigma(v)+1\). Then
\[
z_v=t_i-t_p,\qquad t_0:=0.
\]
The \(n+1\) spacings
\[
t_1,\ t_2-t_1,\ldots,t_n-t_{n-1},\ 1-t_n
\]
have the Dirichlet\((1,\ldots,1)\) distribution. Hence \(t_i-t_p\), a sum of \(d\) consecutive spacings, has the Beta\((d,n+1-d)\) distribution. Therefore
\[
\mathbb E[-\ln z_v]
 =\psi(n+1)-\psi(d)
 =H_n-H_{d-1}
 =H_n-H_{r_\sigma(v)}.
\]
Summing over \(v\) gives
\[
nQH(P)
=
nH_n-
\frac1{e(P)}
\sum_{\sigma\in\mathcal L(P)}
\sum_{v\in P}H_{r_\sigma(v)},
\]
which is equivalent to (5). ∎

For brevity, write
\[
F(P):=
\mathbb E_{\sigma\in\mathcal L(P)}
\sum_{v\in P}H_{r_\sigma(v)}.
\]
Lemma 1 says \(F(P)=\operatorname{QLB}(P)\).

---

# 2. Two one-dimensional inequalities

We need one classical theorem about linear extensions.

## Fixed-element rank log-concavity

If \(R\) is a finite poset, \(x\in R\), and \(N_j\) denotes the number of linear extensions of \(R\) in which \(x\) occupies position \(j\), then
\[
N_j^2\ge N_{j-1}N_{j+1}.
\tag{7}
\]
This is the standard fixed-element rank-log-concavity theorem for linear extensions, proved via the Alexandrov–Fenchel inequalities. It is a theorem, not the unrelated Neggers–Stanley conjecture.

We use the following elementary consequence.

## Lemma 2
Let \(a_0,a_1,\ldots,a_m\) be a nonnegative, nonincreasing, log-concave sequence with \(a_0=1\). Then
\[
\sum_{k=1}^m\frac{a_k}{k}
\ge
\ln\left(\sum_{k=0}^m a_k\right).
\tag{8}
\]

### Proof

Log-concavity implies that the successive ratios \(a_k/a_{k-1}\) are nonincreasing, up to the first zero. Hence
\[
a_{i+j}\le a_i a_j
\tag{9}
\]
whenever \(i+j\le m\).

Set
\[
A(z)=\sum_{k=0}^m a_kz^k,
\qquad
B(z)=\sum_{k=1}^m\frac{a_k}{k}z^k.
\]
The coefficient of \(z^{r-1}\) in \(A(z)B'(z)-A'(z)\) is
\[
\sum_{k=1}^r a_{r-k}a_k-r a_r.
\]
Each of the \(r\) summands is at least \(a_r\) by (9), so this coefficient is nonnegative. Thus, for \(0\le z\le1\),
\[
\frac{A'(z)}{A(z)}\le B'(z).
\]
Integrating from \(0\) to \(1\), and using \(A(0)=1\) and \(B(0)=0\), yields (8). ∎

We also need an upper estimate.

## Lemma 3
For every nonnegative integer-valued random variable \(L\),
\[
\mathbb E H_L
\le
\frac1{\ln2}\ln\bigl(\mathbb E(L+1)\bigr).
\tag{10}
\]

### Proof

Let \(\widehat H(t)\) be the piecewise-linear interpolation of \(H_m\) on \([0,\infty)\). Since the increments \(H_{m+1}-H_m=1/(m+1)\) decrease, \(\widehat H\) is concave. Hence
\[
\mathbb EH_L\le \widehat H(\mathbb EL).
\]

For every integer \(m\ge0\),
\[
H_m\le \frac{\ln(m+1)}{\ln2}.
\tag{11}
\]
Indeed, equality holds for \(m=0,1\), and
\[
\frac1{m+1}
\le
\frac1{\ln2}\ln\frac{m+2}{m+1},
\]
because \(r\ln(1+1/r)\ge\ln2\) for \(r=m+1\ge1\). Concavity of \(t\mapsto\ln(t+1)\) extends (11) from the integers to the piecewise-linear interpolation. Therefore
\[
\mathbb EH_L
\le \widehat H(\mathbb EL)
\le\frac1{\ln2}\ln(\mathbb EL+1).
\]
∎

---

# 3. Induction on the last element

Let \(v\) be maximal in \(P\), and put \(P_v=P-v\). A uniformly random linear extension of \(P\) ends in \(v\) with probability
\[
q_v=\frac{e(P_v)}{e(P)}.
\tag{12}
\]

For \(\tau\in\mathcal L(P_v)\), let
\[
L_v(\tau)
=
(n-1)-
\max\bigl(\{\,\tau(u):u<_Pv\,\}\cup\{0\}\bigr).
\tag{13}
\]
This is exactly the number of elements of \(\tau\) after the latest predecessor of \(v\). Therefore, in the extension \(\tau v\),
\[
r_{\tau v}(v)=L_v(\tau).
\]

Since \(v\) is maximal, deleting \(v\) does not change any \(r_\sigma(u)\) for \(u\ne v\). Consequently,
\[
F(P)
=
\sum_{v\in\max P}
q_v\left(F(P_v)+c_v\right),
\tag{14}
\]
where
\[
c_v=\mathbb E_{\tau\in\mathcal L(P_v)} H_{L_v(\tau)}.
\tag{15}
\]

## Lemma 4
For every maximal \(v\),
\[
\ln\frac{e(P)}{e(P_v)}
\le c_v
\le
\frac1{\ln2}\ln\frac{e(P)}{e(P_v)}.
\tag{16}
\]

### Proof: lower bound

Set
\[
a_k=\Pr(L_v\ge k),\qquad k\ge0.
\]
Then \(a_0=1\) and \(a_k\) is nonincreasing.

For each \(k\), inserting \(v\) into \(\tau\in\mathcal L(P_v)\) so that exactly \(k\) elements lie after \(v\) is possible precisely when \(L_v(\tau)\ge k\). Thus
\[
e(P_v)a_k
\]
is the number of linear extensions of \(P\) having exactly \(k\) elements after \(v\). By fixed-element rank log-concavity, the sequence \((a_k)\) is log-concave.

Moreover,
\[
c_v
=\mathbb EH_{L_v}
=\sum_{k\ge1}\frac{\Pr(L_v\ge k)}k
=\sum_{k\ge1}\frac{a_k}{k}.
\]
Lemma 2 gives
\[
c_v\ge \ln\left(\sum_{k\ge0}a_k\right).
\]
But
\[
\sum_{k\ge0}a_k
=\mathbb E(L_v+1).
\]
For a fixed \(\tau\), there are exactly \(L_v(\tau)+1\) valid positions in which to insert \(v\). Counting all extensions of \(P\) by first deleting \(v\) therefore gives
\[
e(P)=e(P_v)\mathbb E(L_v+1).
\]
Hence
\[
c_v\ge \ln\frac{e(P)}{e(P_v)}.
\]

### Proof: upper bound

Lemma 3 and the same insertion identity give
\[
c_v
\le\frac1{\ln2}\ln\mathbb E(L_v+1)
=\frac1{\ln2}\ln\frac{e(P)}{e(P_v)}.
\]
∎

## Proposition 5
For every finite poset \(P\),
\[
\ln e(P)\le F(P)\le\frac1{\ln2}\ln e(P).
\tag{17}
\]

### Proof

Induct on \(|P|\). The assertion is immediate for the empty poset and for a chain.

For the lower bound, using (14), Lemma 4, and induction,
\[
\begin{aligned}
F(P)
&\ge
\sum_{v\in\max P}q_v
\left(
 \ln e(P_v)+\ln\frac{e(P)}{e(P_v)}
\right)\\
&=
\sum_{v\in\max P}q_v\ln e(P)
=\ln e(P).
\end{aligned}
\]

For the upper bound,
\[
\begin{aligned}
F(P)
&\le
\sum_{v\in\max P}q_v
\left(
 \frac{\ln e(P_v)}{\ln2}
 +\frac1{\ln2}\ln\frac{e(P)}{e(P_v)}
\right)\\
&=
\frac{\ln e(P)}{\ln2}.
\end{aligned}
\]
This proves (17). Since \(F(P)=\operatorname{QLB}(P)\), it also proves (1). ∎

---

# 4. Comparison with \(\operatorname{LB}(P)\)

The standard entropy–linear-extension inequality for posets is
\[
\ln e(P)
\le n(\ln n-H(P))
\le 2\ln e(P).
\tag{18}
\]
In graph language, if \(G(P)\) is the comparability graph, perfect-graph entropy duality identifies
\[
n(\ln n-H(P))
\]
with \(n\) times the entropy of the incomparability graph, and (18) is the classical entropy estimate for the number of linear extensions.

For normalization, the first inequality can also be checked directly. If \(z^*\) maximizes \(\prod_v z_v\) on \(C(P)\), then
\[
\prod_v z_v^*=e^{-nH(P)}.
\]
The first-order optimality condition gives
\[
C(P)\subseteq
\left\{z\ge0:\sum_v\frac{z_v}{z_v^*}\le n\right\}.
\]
The containing simplex has volume
\[
\frac{n^n\prod_v z_v^*}{n!}.
\]
Since
\[
\operatorname{vol}C(P)=\frac{e(P)}{n!},
\]
we obtain
\[
e(P)\le n^n e^{-nH(P)}
       =e^{\operatorname{LB}(P)}.
\]

Combining (17) with both sides of (18),
\[
\operatorname{QLB}(P)
\ge\ln e(P)
\ge\frac12\operatorname{LB}(P),
\]
and
\[
\operatorname{QLB}(P)
\le\frac{\ln e(P)}{\ln2}
\le\frac1{\ln2}\operatorname{LB}(P).
\]
This is (3), covering every finite poset, including chains where all quantities vanish.

# Caveat about the catalog formulation

The expression
\[
\mathbb E_{z\in C(P)}[h(z)]
\]
is not formally defined until a probability measure is specified. The proof above uses normalized Lebesgue measure on the chain polytope. Equivalently, it applies to any definition of \(QH\) for which the extension-gap identity (5) is the defining or previously established formula. If the source used a different averaging law, Lemma 1 would have to be rechecked; the catalog’s corrupted statement does not permit that normalization issue to be settled from the supplied text alone.