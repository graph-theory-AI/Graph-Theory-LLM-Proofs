```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The full programme remains open, but the sparse appearance threshold is Poisson for every fixed strictly balanced graph, while cherries admit an exact zero-tail rate and a rigorous localized moderate-upper-tail mechanism in G(n,m).",
  "would_publish": false,
  "caveats": "The catalog sentence is not a quantified conjecture, and the results below cover only endpoint and special-graph regimes."
}
```

# Mathematical writeup

## 1. Interpretation of the problem

The sentence in Remark 1.2 is a research programme rather than a truth-valued conjecture. A precise version must specify at least:

- the fixed graph \(H\);
- labeled or unlabeled copies;
- upper or lower tail;
- the normalization of the deviation;
- the joint asymptotics of the density and deviation size.

There cannot be one formula valid without qualifications: at the appearance threshold the count is Poisson, at larger densities collective fluctuations may be approximately Gaussian, and sufficiently large upper deviations can be generated more cheaply by a localized structure such as a high-degree vertex.

I give three rigorous partial results:

1. the Poisson endpoint for every strictly balanced \(H\), in both \(G(n,p)\) and \(G(n,m)\);
2. an exact lower-tail formula for the two-edge path in \(G(n,m)\);
3. a planted-star lower bound showing a genuine localized moderate-deviation regime for the same graph.

All copy counts below are non-induced and unlabeled.

---

## 2. The Poisson endpoint for general strictly balanced graphs

Let \(H\) be a fixed simple graph with
\[
v=v(H),\qquad e=e(H)\ge 2,
\]
and let \(a=|\operatorname{Aut}(H)|\). Say that \(H\) is strictly balanced if
\[
\frac{e(F)}{v(F)}<\frac ev
\]
for every nonempty proper subgraph \(F\subsetneq H\).

Let \(X_H(G)\) be the number of copies of \(H\) in \(G\).

### Theorem 2.1

Suppose that \(H\) is strictly balanced.

1. If \(G\sim G(n,p)\) and
   \[
   p\,n^{v/e}\longrightarrow c\in(0,\infty),
   \]
   then
   \[
   X_H(G)\ \xrightarrow{d}\ \operatorname{Poisson}\left(\frac{c^e}{a}\right).
   \]

2. Let \(N=\binom n2\), let \(G\sim G(n,m)\), and put \(t=m/N\). If
   \[
   t\,n^{v/e}\longrightarrow c\in(0,\infty),
   \]
   then
   \[
   X_H(G)\ \xrightarrow{d}\ \operatorname{Poisson}\left(\frac{c^e}{a}\right).
   \]

3. In the subcritical regime,
   \[
   p\,n^{v/e}\to0
   \]
   implies
   \[
   \mathbb P_{p}(X_H\ge1)
   \sim \mathbb E_pX_H
   =\frac{(n)_v}{a}p^e.
   \]
   Likewise, if \(m\to\infty\) and \(t n^{v/e}\to0\), then
   \[
   \mathbb P_m(X_H\ge1)
   \sim \mathbb E_mX_H
   =\frac{(n)_v}{a}\frac{(m)_e}{(N)_e}
   \sim \frac{n^v t^e}{a}.
   \]

Here \((x)_k=x(x-1)\cdots(x-k+1)\).

### Proof

Strict balance implies that \(H\) is connected. Indeed, if \(H\) had several components, one component would have density at least \(e/v\), contradicting strict balance.

We first record the needed union-density fact.

#### Lemma 2.2

Let \(H_1,\ldots,H_k\) be distinct copies of \(H\), and let \(U=\bigcup_iH_i\). Then
\[
e(U)\ge \frac ev v(U),
\]
with equality if and only if the copies \(H_i\) are pairwise vertex-disjoint.

#### Proof

Write \(d=e/v\) and define the excess
\[
\eta(J)=e(J)-d\,v(J).
\]
The first copy has excess zero. Suppose a further copy \(C\) is added to a previous union \(U_0\). Let its intersection with \(U_0\) have \(s\) vertices and \(f\) edges, counting shared vertices even when they are isolated in the intersection. If \(C\) is not already contained in \(U_0\), this intersection is a proper subgraph of \(C\), and hence
\[
f<ds
\]
when \(s>0\). Therefore
\[
\eta(U_0\cup C)-\eta(U_0)
=(e-f)-d(v-s)
=ds-f,
\]
which is positive when \(s>0\) and zero when \(s=0\).

If the earlier copies are vertex-disjoint, a distinct connected copy of \(H\) cannot be contained in their union: it would have to lie in one component and use all \(e\) edges of that component, hence would be the same copy. Thus the first vertex overlap strictly increases the excess, and subsequent additions never decrease it. ∎

For fixed \(k\), expand the factorial moment
\[
\mathbb E(X_H)_k
\]
over ordered \(k\)-tuples of distinct copies.

The number of ordered, vertex-disjoint \(k\)-tuples is
\[
\frac{(n)_{kv}}{a^k}.
\]
In \(G(n,p)\), their contribution is
\[
\frac{(n)_{kv}}{a^k}p^{ke}
\longrightarrow
\left(\frac{c^e}{a}\right)^k.
\]

Every non-vertex-disjoint intersection type has a union with, say, \(V\) vertices and \(E\) edges satisfying
\[
E>\frac ev V.
\]
There are \(O(n^V)\) realizations of that type, and their total contribution is
\[
O(n^Vp^E)
=
O\!\left(n^{\,V-(v/e)E}\right)
=o(1).
\]
There are only finitely many intersection types for fixed \(k\). Consequently,
\[
\mathbb E(X_H)_k\longrightarrow
\left(\frac{c^e}{a}\right)^k,
\]
which gives the Poisson limit by the factorial-moment criterion.

For \(G(n,m)\), a fixed set of \(q\) edges is present with probability
\[
\frac{(m)_q}{(N)_q}.
\]
Strict balance and \(e\ge2\) imply \(e/v>1/2\), so under the critical scaling \(m\to\infty\). Hence, for fixed \(q\),
\[
\frac{(m)_q}{(N)_q}=t^q(1+o(1)).
\]
The same factorial-moment argument applies.

For the subcritical assertion, let \(\mu=\mathbb EX_H=o(1)\). Bonferroni gives
\[
\mu-\mathbb E\binom{X_H}{2}
\le \mathbb P(X_H\ge1)\le\mu.
\]
Vertex-disjoint pairs contribute \(O(\mu^2)=o(\mu)\). If two copies intersect in \(s\ge1\) vertices and \(f\) edges, their contribution divided by \(\mu\) is, up to a constant,
\[
n^{v-s}p^{e-f}.
\]
Strict balance gives
\[
\frac{v-s}{e-f}<\frac ve,
\]
and therefore \(n^{v-s}p^{e-f}\to0\) when \(p n^{v/e}\to0\). The \(G(n,m)\) proof is identical when \(m\to\infty\), replacing \(p\) by \(t\). ∎

### Consequence for the open problem

At \(t\asymp n^{-v/e}\), fixed upper-tail probabilities converge to Poisson probabilities rather than having a nonzero speed tending to infinity. Below the threshold,
\[
\log \mathbb P(X_H\ge1)
=
\log \mathbb EX_H+o(1).
\]
Thus any dense quadratic rate necessarily has to change before reaching the appearance threshold.

---

## 3. Exact zero-tail rate for cherries in \(G(n,m)\)

Let \(P_3\) denote the path with two edges, and let
\[
X=X_{P_3}(G)=\sum_{u=1}^n\binom{d_G(u)}2.
\]
Thus \(X=0\) exactly when \(G\) is a matching.

### Proposition 3.1

For \(G\sim G(n,m)\) and \(m\le n/2\),
\[
\mathbb P(X=0)
=
\frac{(n)_{2m}}{2^m(N)_m}
=
\prod_{i=0}^{m-1}
\frac{\binom{n-2i}{2}}{N-i}.
\]
For \(m>n/2\), this probability is zero.

If \(m\to\infty\) and \(m=o(n)\), then
\[
\log \mathbb P(X=0)
=
-(2+o(1))\frac{m^2}{n}
=
-(1+o(1))\mathbb EX.
\]

If \(m/n\to c\in(0,1/2)\), then
\[
\frac1n\log\mathbb P(X=0)
\longrightarrow
-\Phi(c),
\]
where
\[
\Phi(c)=2c+(1-2c)\log(1-2c).
\]

### Proof

The number of \(m\)-edge matchings in \(K_n\) is
\[
\frac{n!}{(n-2m)!2^m m!}
=\frac{(n)_{2m}}{2^m m!}.
\]
Dividing by \(\binom Nm=(N)_m/m!\) proves the exact formula.

For \(m=o(n)\), write the product as
\[
\prod_{i=0}^{m-1}
\frac{(1-2i/n)(1-2i/(n-1))}
     {1-i/N}.
\]
Uniform Taylor expansion gives
\[
\begin{aligned}
\log\mathbb P(X=0)
={}&-\frac{m(m-1)}n-\frac{m(m-1)}{n-1}
 +\frac{m(m-1)}{n(n-1)}  \\
&\quad+O\!\left(\frac{m^3}{n^2}\right).
\end{aligned}
\]
Hence
\[
\log\mathbb P(X=0)=-(2+o(1))\frac{m^2}{n}.
\]

There are
\[
n\binom{n-1}{2}
\]
possible cherries, and a fixed pair of edges is present with probability \((m)_2/(N)_2\). Thus
\[
\mathbb EX
=
n\binom{n-1}{2}\frac{(m)_2}{(N)_2}
\sim \frac{2m^2}{n},
\]
proving the second equality.

Finally, if \(m/n\to c<1/2\), the logarithm of the product is a Riemann sum:
\[
\begin{aligned}
\frac1n\log\mathbb P(X=0)
&\longrightarrow
2\int_0^c\log(1-2x)\,dx\\
&=-2c-(1-2c)\log(1-2c).
\end{aligned}
\]
This is \(-\Phi(c)\). ∎

For example, if \(m/\sqrt n\to b\), then
\[
\mathbb P(X=0)\to e^{-2b^2},
\]
consistent with Theorem 2.1 since \(P_3\) has \(v=3\), \(e=2\), and two automorphisms.

---

## 4. A localized moderate-upper-tail mechanism in \(G(n,m)\)

The preceding lower-tail behavior is Poisson-like for \(m=o(n)\). Upper tails can nevertheless be much cheaper because one may plant a high-degree vertex.

### Proposition 4.1

Let \(G\sim G(n,m)\), where
\[
m=o(n),
\]
and let \(X\) count cherries. Put
\[
\mu=\mathbb EX
=
n\binom{n-1}{2}\frac{(m)_2}{(N)_2}
\sim\frac{2m^2}{n}.
\]
Let \(0<\delta=\delta_n\le1\) satisfy
\[
\frac{\delta^2m^2}{n}\longrightarrow\infty.
\]
Set
\[
r=\left\lceil3\sqrt{\delta\mu}\right\rceil.
\]
Then
\[
\mathbb P\!\left(X\ge(1+\delta)\mu\right)
\ge
(1-o(1))\frac{(m)_r}{(N)_r}.
\]
Consequently,
\[
-\log\mathbb P\!\left(X\ge(1+\delta)\mu\right)
\le
(3\sqrt2+o(1))
\frac{m\sqrt\delta}{\sqrt n}
\log\frac Nm.
\]

In particular, if
\[
\frac{\delta^{3/2}m}
{\sqrt n\,\log(N/m)}
\longrightarrow\infty,
\]
then
\[
-\log\mathbb P\!\left(X\ge(1+\delta)\mu\right)
=o(\delta^2\mu).
\]

### Proof

Fix a vertex \(v\) and a fixed set \(S\) of \(r\) edges incident with \(v\). The assumptions imply
\[
\delta^2\mu\to\infty,\qquad
\delta n\to\infty,
\]
and
\[
\frac rm
=O\!\left(\sqrt{\frac{\delta}{n}}\right)
=o(\delta).
\]
In particular, \(r\le n-1\) for all sufficiently large \(n\).

Condition on \(S\subseteq E(G)\). The remaining \(m-r\) edges are uniformly sampled from the other \(N-r\) edges. Let \(Y\) count cherries whose three vertices all lie in \(V(G)\setminus\{v\}\). Its conditional expectation is
\[
\nu
=
(n-1)\binom{n-2}{2}
\frac{(m-r)_2}{(N-r)_2}.
\]
Since
\[
\frac{(n-1)\binom{n-2}{2}}
{n\binom{n-1}{2}}
=1-\frac3n
\]
and \(r/m=o(\delta)\), it follows that
\[
\nu=(1-o(\delta))\mu.
\]

We also need concentration of \(Y\). Write \(Y\) as a sum of indicators of two-edge sets. Under sampling without replacement, indicators supported on disjoint edge sets have nonpositive covariance. Two distinct cherries with positive possible covariance must share one edge; there are \(O(n^4)\) ordered pairs of this kind. Therefore
\[
\operatorname{Var}(Y\mid S\subseteq E(G))
\le
O\!\left(
n^3\left(\frac m{n^2}\right)^2
+
n^4\left(\frac m{n^2}\right)^3
\right).
\]
Since \(m=o(n)\),
\[
\operatorname{Var}(Y\mid S\subseteq E(G))
=O\!\left(\frac{m^2}{n}\right)
=O(\mu).
\]
Chebyshev's inequality and \(\delta^2\mu\to\infty\) now give
\[
Y\ge \mu-\frac{\delta\mu}{2}
\]
with conditional probability \(1-o(1)\).

The forced edges \(S\) themselves create \(\binom r2\) cherries centered at \(v\). Since \(\delta\mu\to\infty\),
\[
\binom r2\ge\frac32\delta\mu
\]
for sufficiently large \(n\). Thus, with conditional probability \(1-o(1)\),
\[
X\ge
\left(\mu-\frac{\delta\mu}{2}\right)
+\frac32\delta\mu
=(1+\delta)\mu.
\]

The probability that the fixed set \(S\) is present is
\[
\mathbb P(S\subseteq E(G))=\frac{(m)_r}{(N)_r},
\]
proving the first assertion.

Finally, because \(r=o(m)\),
\[
-\log\frac{(m)_r}{(N)_r}
=
r\log\frac Nm+O\!\left(\frac{r^2}{m}\right)
=
(3+o(1))\sqrt{\delta\mu}\log\frac Nm.
\]
Using \(\mu\sim2m^2/n\) gives the displayed logarithmic bound. Dividing it by
\[
\delta^2\mu\sim \frac{2\delta^2m^2}{n}
\]
proves the final assertion. ∎

The additional condition is non-vacuous even for genuine moderate deviations. For instance,
\[
m=n^{3/4},\qquad \delta=n^{-1/10}
\]
satisfies the hypotheses. The planted-star cost is then \(O(n^{1/5}\log n)\), whereas the variance-scale benchmark \(\delta^2\mu\) has order \(n^{3/10}\).

An elementary covariance calculation also gives
\[
\operatorname{Var}X=(1+o(1))\mu
\qquad (m=o(n),\ m\to\infty),
\]
so \(\delta^2\mu\) is indeed the natural collective quadratic scale in this range. Proposition 4.1 shows that the upper tail can be exponentially larger than such a collective prediction.

---

## 5. What remains unresolved

These arguments do not determine the full sparse moderate-deviation rate.

1. The Poisson theorem concerns fixed counts at and below the appearance threshold, not growing moderate deviations.
2. Proposition 4.1 is only a lower bound on an upper-tail probability. It does not give a matching upper bound or the optimal localized constant.
3. Even for cherries, the transition between collective and localized mechanisms is not determined here.
4. General \(H\) can have several competing planted structures, and non-strictly-balanced graphs have additional clustering phenomena.
5. The answer depends essentially on the deviation scale; no single expression can cover all sparse densities without a phase diagram.

Thus the broad problem in Remark 1.2 is not resolved, but the results above rigorously identify the Poisson endpoint and exhibit a concrete sparse moderate-deviation obstruction to naively extending a quadratic dense-regime rate.