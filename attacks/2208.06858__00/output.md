```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture remains unresolved, but the standard construction gives a logarithmic lower bound, and the conjecture holds with matching order for canonical star-partition strategies and exactly for two other natural restricted classes.",
  "would_publish": false,
  "caveats": "No upper bound tending to zero is obtained for arbitrary intersecting fibers, and the convention excluding the empty set is essential."
}
```

# 1. Formal formulation

Write \(\Omega_n=2^{[n]}\), with uniform measure \(\mu_n\). A set
\[
W\subseteq \Omega_n^t
\]
is **fiber-intersecting** if, for every \(i\in[t]\) and every fixed choice \(A_{-i}=(A_j)_{j\ne i}\), the section
\[
W_i(A_{-i})
 =\{A_i:(A_1,\ldots,A_t)\in W\}
\]
is an intersecting family:
\[
A\cap B\ne\varnothing\qquad\text{for all }A,B\in W_i(A_{-i}).
\]
In particular, taking \(A=B\), no such section may contain \(\varnothing\).

Let
\[
p_{\mathrm I}(t,n)=\max\{\mu_n^t(W):W\text{ is fiber-intersecting}\},
\qquad
p_{\mathrm I}(t)=\lim_{n\to\infty}p_{\mathrm I}(t,n).
\]
The limit exists because one can ignore an additional ground-set element. The conjecture is
\[
p_{\mathrm I}(t)\longrightarrow 0.
\]

Equivalently, after deleting the vertex \(\varnothing\), let \(D_n\) be the graph on \(2^{[n]}\setminus\{\varnothing\}\) in which \(A\) and \(B\) are adjacent when \(A\cap B=\varnothing\). Then \(W\) is an independent set in the Cartesian power \(D_n^{\square t}\).

## Empty-set convention

This convention is indispensable. If a singleton family \(\{\varnothing\}\) were declared intersecting vacuously, then for \(n=1\) the parity family
\[
W=\left\{(x_1,\ldots,x_t)\in\{0,1\}^t:
  \sum_i x_i\equiv0\pmod 2\right\}
\]
would have density \(1/2\), and every fiber would be a singleton. Thus the conjecture would be false under the “distinct members only” convention.

# 2. Baseline bounds and a logarithmic construction

Every intersecting family in \(2^{[n]}\) has size at most \(2^{n-1}\), by pairing \(A\) with \(A^c\). Consequently,
\[
p_{\mathrm I}(t,n)\le \frac12.
\]
Also, every coordinate of every member of \(W\) is nonempty, so
\[
p_{\mathrm I}(t,n)\le (1-2^{-n})^t
 \le \exp(-t2^{-n}).
\]
Thus any construction of nonnegligible density must use \(n\gtrsim\log_2t\).

There is a matching logarithmic lower construction.

## Proposition 2.1

As \(t\to\infty\),
\[
p_{\mathrm I}(t)\ge \frac{1-o(1)}{\log_2t}.
\]

### Proof

Fix \(q\le n\), and for a set meeting \([q]\) define
\[
\kappa(A)=\min(A\cap[q]).
\]
The color class
\[
\mathcal D_j=\{A:\kappa(A)=j\}
\]
is intersecting, since every one of its members contains \(j\). Moreover,
\[
\mu_n(\mathcal D_j)=2^{-j}.
\]

For \(r\in\mathbb Z/q\mathbb Z\), define
\[
W_r=\left\{(A_1,\ldots,A_t):
  \kappa(A_i)\text{ is defined for all }i,\quad
  \sum_{i=1}^t\kappa(A_i)\equiv r\pmod q\right\}.
\]
After fixing all coordinates except \(i\), there is at most one possible value of \(\kappa(A_i)\). Hence the \(i\)-th fiber is contained in one \(\mathcal D_j\), and is intersecting.

The \(q\) families \(W_r\) partition all tuples for which every \(A_i\) meets \([q]\). Therefore some \(r\) satisfies
\[
\mu_n^t(W_r)\ge \frac{(1-2^{-q})^t}{q}.
\]
Taking
\[
q=\left\lceil \log_2t+2\log_2\log_2(t+2)\right\rceil
\]
gives \(t2^{-q}=o(1)\), and hence
\[
\frac{(1-2^{-q})^t}{q}
 =\frac{1-o(1)}{\log_2t}.
\]
\(\square\)

Thus, if the conjecture is true, its decay can be no faster than logarithmic in order of magnitude.

# 3. Matching order for the canonical star-partition class

The preceding construction belongs to a natural restricted class. Let
\[
p_j=2^{-j},\qquad j\in\mathbb N.
\]
A set \(C\subseteq\mathbb N^t\) will be called a **line code** if every axis-parallel line contains at most one point, equivalently if no two members of \(C\) differ in exactly one coordinate.

For such \(C\), the pullback
\[
W_C=\{(A_1,\ldots,A_t):(\min A_1,\ldots,\min A_t)\in C\}
\]
is fiber-intersecting: after fixing the other coordinates, all allowable \(A_i\)'s have the same minimum element.

Define
\[
\Lambda_t=\sup_C\sum_{c\in C}\prod_{i=1}^t2^{-c_i},
\]
where the supremum is over line codes \(C\subseteq\mathbb N^t\).

## Theorem 3.1

As \(t\to\infty\),
\[
\frac{1-o(1)}{\log_2t}
 \le \Lambda_t
 \le \frac{2+o(1)}{\log_2t}.
\]

Hence Conjecture 2.1 holds, with the correct logarithmic order up to a factor \(2+o(1)\), for all strategies obtained from the canonical minimum-element star partition.

### Lower bound

This is Proposition 2.1: restrict the alphabet to \([q]\) and take one residue class of the sum modulo \(q\).

### Upper bound

Fix a line code \(C\), let
\[
P=p^{\otimes t}(C)>0,
\]
and let \(Q\) be \(p^{\otimes t}\) conditioned on \(C\). Write \(Q_i\) for its \(i\)-th marginal and put
\[
R=P^{-1}.
\]

For each coordinate \(i\), the projection \(C\to\mathbb N^{t-1}\) deleting coordinate \(i\) is injective. Therefore the full cylinder over that projection has measure
\[
\sum_{c\in C}\prod_{j\ne i}p_{c_j}
 =P\,\mathbb E_Q\!\left[\frac1{p_{X_i}}\right]
 \le1.
\]
Since \(1/p_j=2^j\),
\[
\mathbb E_{Q_i}2^{X_i}\le R. \tag{3.1}
\]

On the other hand,
\[
D(Q\|p^{\otimes t})=\log R.
\]
The standard decomposition of relative entropy gives
\[
D(Q\|p^{\otimes t})
 =
D\!\left(Q\middle\|\bigotimes_iQ_i\right)
 +\sum_{i=1}^tD(Q_i\|p),
\]
and hence
\[
\log R\ge\sum_{i=1}^tD(Q_i\|p). \tag{3.2}
\]

We now lower-bound each marginal divergence using (3.1). Let
\[
L=\lceil R\rceil+1,\qquad f_L(j)=\min(2^j,2^L).
\]
For the geometric distribution \(p_j=2^{-j}\),
\[
\mathbb E_p f_L
 =\sum_{j\le L}1+2^L\sum_{j>L}2^{-j}
 =L+1.
\]
By (3.1),
\[
\mathbb E_{Q_i}f_L\le R.
\]
Thus
\[
\left|\mathbb E_p f_L-\mathbb E_{Q_i}f_L\right|
 \ge L+1-R\ge2.
\]
Since \(0\le f_L\le2^L\),
\[
\|Q_i-p\|_{\mathrm{TV}}\ge 2^{1-L}\ge2^{-R-1}.
\]
Pinsker's inequality, with natural logarithms, now gives
\[
D(Q_i\|p)\ge2\|Q_i-p\|_{\mathrm{TV}}^2
 \ge2^{-2R-1}.
\]
Substituting into (3.2),
\[
\log R\ge t\,2^{-2R-1}. \tag{3.3}
\]
In particular \(R\to\infty\). Rearranging (3.3),
\[
2R\ge \log_2t-1-\log_2\log R.
\]
If \(R\ge\log_2t\), the desired estimate is immediate. Otherwise the last logarithmic term is \(o(\log t)\), so
\[
R\ge\left(\frac12-o(1)\right)\log_2t.
\]
Therefore
\[
P=R^{-1}\le\frac{2+o(1)}{\log_2t}.
\]
Taking the supremum over \(C\) proves the theorem. \(\square\)

# 4. Two further classes for which vanishing is provable

## 4.1 Globally monotone winning sets

Call \(W\) increasing if
\[
(A_1,\ldots,A_t)\in W,\quad A_i\subseteq B_i\ \forall i
 \quad\Longrightarrow\quad
(B_1,\ldots,B_t)\in W.
\]

## Proposition 4.1

For increasing fiber-intersecting \(W\subseteq(2^{[n]})^t\),
\[
\mu_n^t(W)\le2^{-t}.
\]
This is sharp.

### Proof

For each \(i\), let
\[
\mathcal P_i=\{A_i:(A_1,\ldots,A_t)\in W
 \text{ for some }A_{-i}\}
\]
be the \(i\)-th projection.

Take \(A,B\in\mathcal P_i\), witnessed by \(x,y\in W\). For \(j\ne i\), put
\[
C_j=x_j\cup y_j.
\]
By monotonicity, both
\[
(A,C_{-i})\in W,\qquad (B,C_{-i})\in W.
\]
They belong to the same \(i\)-fiber, so \(A\cap B\ne\varnothing\). Hence every \(\mathcal P_i\) is intersecting and has measure at most \(1/2\). Since
\[
W\subseteq\mathcal P_1\times\cdots\times\mathcal P_t,
\]
we obtain
\[
\mu_n^t(W)\le\prod_i\mu_n(\mathcal P_i)\le2^{-t}.
\]

Equality is attained by taking a product of \(t\) dictatorships. \(\square\)

In particular, monotonicity cannot be imposed without loss of generality: doing so would make the conjecture easy and give exponential decay. Upward-closing fibers independently can destroy the intersecting condition in other coordinate directions.

## 4.2 Column-local weighted-majority certificates

Represent \(A_i\subseteq[n]\) by signs
\[
\xi_{ik}=2\mathbf 1_{\{k\in A_i\}}-1.
\]
For each \(i\), fix a nonnegative function
\[
w_i:\{-1,1\}^{t-1}\longrightarrow[0,\infty).
\]
Define
\[
L_i(\xi)=\sum_{k=1}^n
 w_i((\xi_{jk})_{j\ne i})\,\xi_{ik},
\]
and
\[
W(w,n)=\{\xi:L_i(\xi)>0\text{ for every }i\}.
\]

For fixed other rows, the weights in \(L_i\) are fixed and nonnegative. If two candidate sets \(A_i,B_i\) are disjoint, then coordinatewise
\[
\xi^{A_i}_k+\xi^{B_i}_k\le0,
\]
so their two \(L_i\)-scores cannot both be positive. Thus \(W(w,n)\) is fiber-intersecting.

## Theorem 4.2

For fixed \(t\) and fixed weights \(w_i\),
\[
\limsup_{n\to\infty}\mu_n^t(W(w,n))
 \le\frac1{t+1}.
\]
Moreover, equality is attainable. Hence \(1/(t+1)\) is the exact asymptotic optimum in this weighted-majority class.

### Proof

For one random column, put
\[
U_i=\xi_iw_i(\xi_{-i}),\qquad
\alpha_i=\mathbb E U_i^2=\mathbb E w_i(\xi_{-i})^2.
\]
If some \(\alpha_i=0\), the success event is empty. Otherwise the multivariate central limit theorem shows that the standardized vector
\[
\left(\frac{L_i}{\sqrt{n\alpha_i}}\right)_{i=1}^t
\]
converges to a centered Gaussian vector \(G\).

We claim that every pairwise correlation of \(G\) is at most \(1/2\). Fix \(i\ne j\), condition on the remaining signs \(R\), and write
\[
a_\pm=w_i(\xi_j=\pm1,R),\qquad
b_\pm=w_j(\xi_i=\pm1,R).
\]
Then
\[
\mathbb E_{\xi_i,\xi_j}[U_iU_j\mid R]
 =\frac14(a_+-a_-)(b_+-b_-).
\]
Since \(a_\pm,b_\pm\ge0\),
\[
(a_+-a_-)^2\le a_+^2+a_-^2.
\]
Cauchy–Schwarz therefore gives
\[
|\mathbb E U_iU_j|
 \le\frac14
 \sqrt{2\alpha_i\,2\alpha_j}
 =\frac12\sqrt{\alpha_i\alpha_j}.
\]
Thus \(\operatorname{Corr}(G_i,G_j)\le1/2\).

Let \(Y\) be the equicorrelated Gaussian vector with unit variances and all off-diagonal correlations \(1/2\). Slepian's comparison inequality yields
\[
\Pr(G_i>0\ \forall i)\le\Pr(Y_i>0\ \forall i).
\]
Represent
\[
Y_i=\frac{Z_0+Z_i}{\sqrt2}
\]
with \(Z_0,Z_1,\ldots,Z_t\) independent standard Gaussians. Then
\[
\Pr(Y_i>0\ \forall i)
 =\int_{\mathbb R}\phi(z)\Phi(z)^t\,dz
 =\frac1{t+1}.
\]
This proves the upper bound.

For equality, take
\[
w_i(\xi_{-i})=
 \mathbf 1_{\{\xi_j=1\text{ for every }j\ne i\}}.
\]
Let \(N_{\mathbf1}\) be the number of columns with all \(t\) signs equal to \(1\), and let \(N_i\) count columns with only the \(i\)-th sign equal to \(-1\). Then
\[
L_i=N_{\mathbf1}-N_i.
\]
The \(t+1\) relevant multinomial cells have equal probabilities \(2^{-t}\), so by symmetry
\[
\Pr(N_{\mathbf1}>N_i\ \forall i)\longrightarrow\frac1{t+1};
\]
the probability of ties tends to zero. \(\square\)

# 5. Remaining gap

None of the restricted results gives a global upper bound on \(p_{\mathrm I}(t)\):

* The logarithmic theorem only treats fibers lying in one class of a fixed canonical star partition.
* The weighted-majority theorem assumes a column-local halfspace certificate.
* The monotone theorem cannot be applied after an innocent monotonicization: enlarging a family in one coordinate can create disjoint pairs in fibers of another coordinate.

General intersecting sections may depend nonlocally on all \(n\) columns and on all other players, and may switch among unrelated majority-type and star-type families. The only unconditional upper bounds obtained here are
\[
p_{\mathrm I}(t,n)\le
\min\left\{\frac12,(1-2^{-n})^t\right\},
\]
which do not tend to zero after taking \(n\to\infty\).

Thus the full conjecture is neither proved nor disproved. The strongest concrete conclusion here is that the natural minimum-element/Latin-code mechanism has optimal order \(\Theta(1/\log t)\), while any counterexample with positive limiting probability would necessarily exploit substantially more general, globally coupled intersecting fibers.