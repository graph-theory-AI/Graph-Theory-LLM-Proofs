```json
{
  "verdict": "proved",
  "confidence": "high",
  "one_line": "For every fixed m, the first-moment quantity (n!)^(m-1)((r)_m/r^m)^(n choose 2) also gives the sufficient condition, yielding the required single integer threshold.",
  "would_publish": true,
  "caveats": "The argument assumes fixed m and independent uniform edge colors; it does not classify the permitted exceptional case r=r0 or growing m."
}
```

# 1. Statement of the result

Fix an integer \(m\ge 2\), and let
\[
N=\binom n2,\qquad
p_k(r)=\frac{(r)_k}{r^k}=\prod_{j=0}^{k-1}\left(1-\frac jr\right).
\]
Thus \(p_m(r)\) is the probability that \(m\) independent uniform colors from \([r]\) are all distinct.

Define the first-moment parameter
\[
\mu_n(r)=(n!)^{m-1}p_m(r)^N.
\]

I prove the following stronger assertion.

> **Theorem.** For fixed \(m\ge2\) and integer \(r=r(n)\):
> \[
> \mu_n(r)\longrightarrow0
> \quad\Longrightarrow\quad
> \Pr(\text{a rainbow stacking exists})\longrightarrow0,
> \]
> while
> \[
> \mu_n(r)\longrightarrow\infty
> \quad\Longrightarrow\quad
> \Pr(\text{a rainbow stacking exists})\longrightarrow1.
> \]

Since the logarithm of \(\mu_n(r)\) changes by \(\Theta(\log^2 n)\) when \(r\) is increased by one near its zero, this implies the requested single-threshold statement, with at most the value \(r=r_0(n)\) left unclassified.

The real first-moment root \(\rho_m(n)\) is determined by
\[
(n!)^{m-1}p_m(\rho_m(n))^N=1,
\]
and satisfies
\[
\rho_m(n)
=
\frac{mN}{2\log(n!)}+\frac{2m-1}{6}+o(1)
\sim \frac{mn}{4\log n}.
\]

# 2. Normalized stackings and the first moment

A simultaneous relabeling of all \(m\) copies of \(K_n\) does not affect whether a stacking is rainbow. We may therefore fix the placement of the first coloring and represent a normalized stacking by
\[
\boldsymbol{\sigma}=(\sigma_1,\ldots,\sigma_m),
\qquad
\sigma_1=\mathrm{id},\quad \sigma_i\in S_n.
\]
There are \((n!)^{m-1}\) normalized stackings.

For a fixed \(\boldsymbol{\sigma}\), the \(N\) edge positions use disjoint random variables, and the probability that all \(m\) colors at each position are distinct is
\[
p_m(r)^N.
\]
Let \(X\) count normalized rainbow stackings. Then
\[
\mathbb E X=(n!)^{m-1}p_m(r)^N=\mu_n(r).
\]
Thus \(\mu_n(r)\to0\) implies nonexistence with high probability by Markov's inequality.

It remains to prove the second-moment direction.

# 3. A bounded-degree chromatic expansion

We first need a uniform expansion for proper-coloring probabilities.

> **Lemma 1.** Fix \(\Delta\). Let \(G\) be a simple graph with \(v\) vertices, \(e\) edges, \(t\) triangles and maximum degree at most \(\Delta\). Then, uniformly over all such \(G\),
> \[
> \log\frac{P_G(q)}{q^v}
> =
> -\frac e q-\frac{e/2+t}{q^2}
> +O_\Delta\!\left(\frac v{q^3}\right)
> \]
> as \(q\to\infty\).

Here \(P_G(q)\) denotes the chromatic polynomial.

## Proof

Put \(z=1/q\). The inclusion-exclusion formula is
\[
\frac{P_G(q)}{q^v}
=
\sum_{A\subseteq E(G)}(-1)^{|A|}z^{v-c(A)},
\]
where \(c(A)\) counts all connected components of \((V(G),A)\), including isolated vertices.

Regrouping an edge set according to its nontrivial connected components gives a hard-core polymer expansion
\[
\frac{P_G(q)}{q^v}
=
\sum_{\Gamma\ \mathrm{pairwise\ disjoint}}
\prod_{S\in\Gamma}w(S),
\]
where \(S\) ranges over connected vertex sets of size at least two and
\[
w(S)
=
z^{|S|-1}
\sum_{\substack{A\subseteq E(G[S])\\(S,A)\text{ connected}}}
(-1)^{|A|}.
\]
For \(|S|=s\),
\[
|w(S)|\le |z|^{s-1}2^{\Delta s/2}.
\]
The number of connected \(s\)-vertex sets containing a prescribed vertex is at most \(C_\Delta^{s-1}\). Consequently, for sufficiently small \(|z|\),
\[
\sup_x\sum_{S\ni x}|w(S)|e^{|S|}
\le C'_\Delta |z|<1.
\]
The logarithm of the polymer partition function therefore has an absolutely convergent overlap-connected cluster expansion. The usual tree expansion of an overlap-connected family gives
\[
\left|[z^j]\log\frac{P_G(1/z)}{z^{-v}}\right|
\le v C_\Delta^j.
\]
Hence the terms of degree at least three contribute
\[
O_\Delta(v|z|^3).
\]

It remains to identify the first two coefficients. For a simple graph,
\[
P_G(q)
=
q^v-eq^{v-1}
+\left(\binom e2-t\right)q^{v-2}
+O(q^{v-3})
\]
as a formal polynomial expansion. Taking the logarithm gives
\[
-\frac e q
+
\frac{\binom e2-t-e^2/2}{q^2}
=
-\frac e q-\frac{e/2+t}{q^2}.
\]
This proves the lemma. \(\square\)

# 4. Joint rainbow events as edge-colorings of a bipartite multigraph

Consider two normalized stackings. Their joint rainbow conditions can be encoded by an \(m\)-regular bipartite multigraph \(B\):

- the \(N\) left vertices represent edge positions in the first stacking;
- the \(N\) right vertices represent edge positions in the second stacking;
- every random variable \(\chi_i(e)\) is an edge of \(B\), joining the two constraints in which it appears.

For each \(i\), the edges corresponding to \(\chi_i\) form a perfect matching. Thus \(B\) is the union of \(m\) perfect matchings. A color assignment to the edges of \(B\) satisfies both rainbow conditions exactly when it is a proper edge-coloring of \(B\).

For two vertices \(u,v\) in opposite sides of \(B\), let \(k_{uv}\) be the multiplicity of the corresponding parallel-edge bundle.

> **Lemma 2.** Uniformly over all such \(B\),
> \[
> \Pr(\text{a uniform \(r\)-edge-coloring of \(B\) is proper})
> =
> p_m(r)^{2N}
> \left(\prod_{uv:k_{uv}>0}p_{k_{uv}}(r)^{-1}\right)
> \exp\!\left(O_m\!\left(\frac N{r^3}\right)\right).
> \]

## Proof

Let \(G=L(B)\) be the simple line graph of \(B\). It has \(mN\) vertices and maximum degree at most \(2m-2\). Proper edge-colorings of \(B\) are proper vertex-colorings of \(G\).

Write
\[
F_2=\sum_{uv}\binom{k_{uv}}2,
\qquad
F_3=\sum_{uv}\binom{k_{uv}}3.
\]
Each of the \(2N\) vertices of \(B\) contributes a clique \(K_m\) to \(G\). Adjacencies corresponding to parallel pairs are counted at both endpoints, so
\[
e(G)=2N\binom m2-F_2.
\]

Because \(B\) is bipartite, every triangle in its line graph consists of three edges incident with a common vertex of \(B\). A triple of parallel edges is counted at both endpoints. Hence
\[
t(G)=2N\binom m3-F_3.
\]

Lemma 1 gives
\[
\log \Pr(G\text{ is properly \(r\)-colored})
=
-\frac{e(G)}r
-\frac{e(G)/2+t(G)}{r^2}
+O_m\!\left(\frac N{r^3}\right).
\]

On the other hand,
\[
-\log p_k(r)
=
\frac{\binom k2}{r}
+
\frac{\binom k2/2+\binom k3}{r^2}
+O_m(r^{-3}),
\]
uniformly for \(1\le k\le m\). It follows that
\[
\log\left(
p_m(r)^{2N}\prod_{uv}p_{k_{uv}}(r)^{-1}
\right)
=
-\frac{e(G)}r
-\frac{e(G)/2+t(G)}{r^2}
+O_m\!\left(\frac N{r^3}\right).
\]
Comparing the two expressions proves the lemma. \(\square\)

# 5. A permutation exponential-moment lemma

For \(\pi\in S_n\), let
\[
f(\pi)=\bigl|\{e\in\textstyle{\binom{[n]}2}:\pi(e)=e\}\bigr|
\]
be the number of unordered pairs fixed setwise by \(\pi\).

> **Lemma 3.** Let \(a=a(n)\ge0\) satisfy
> \[
> \frac{e^{aN}}{n!}\longrightarrow0.
> \]
> If \(\pi\) is uniform in \(S_n\), then
> \[
> \mathbb E_\pi e^{a f(\pi)}=1+o(1).
> \]

## Proof

Let \(K\) be the number of fixed points of \(\pi\), and let \(T\) be its number of 2-cycles. An unordered pair is fixed setwise precisely when its two vertices are both fixed or form a 2-cycle. Thus
\[
f(\pi)=\binom K2+T.
\]

The hypothesis implies
\[
aN-\log(n!)\to-\infty,
\]
and therefore
\[
an\le 2\log n-2+o(1),
\qquad a\to0.
\]

The factorial moments of \(T\) satisfy
\[
\mathbb E (T)_j=2^{-j}
\]
whenever \(2j\le n\). Consequently,
\[
\mathbb E e^{aT}
=
\sum_{j\ge0}\frac{(e^a-1)^j}{j!}\mathbb E(T)_j
\le
\exp\left(\frac{e^a-1}{2}\right)
=1+O(a).
\]

Set \(K_0=\lceil\log n\rceil\). On \(K\le K_0\),
\[
e^{a\binom K2}=1+o(1),
\]
so
\[
\mathbb E\left[e^{af(\pi)};K\le K_0\right]\le1+o(1).
\]

For the tail, conditioning on exactly \(k\) fixed points and dropping the requirement that the remaining permutation have no fixed points gives
\[
\mathbb E\left[e^{aT};K=k\right]
\le
\frac1{k!}\exp\left(\frac{e^a-1}{2}\right).
\]
It therefore suffices to show
\[
\sum_{k>K_0}\frac{e^{a\binom k2}}{k!}=o(1).
\]
Put
\[
b_k=\frac{e^{a\binom k2}}{k!}.
\]
Then
\[
\frac{b_{k+1}}{b_k}=\frac{e^{ak}}{k+1}.
\]

For \(K_0\le k\le n/2\), the last ratio has no interior maximum, while
\[
\frac{e^{aK_0}}{K_0+1}=o(1),
\qquad
\frac{e^{an/2}}{n/2+1}\le \frac2e+o(1)<1.
\]
Thus this portion of the sum is \(O(b_{K_0})=o(1)\).

For \(n/2\le k\le n\), use \(\log k!\ge k\log k-k\). If
\(an\le \frac32\log n\), then uniformly on this interval
\[
\log b_k\le -c n\log n
\]
for some absolute \(c>0\). If \(an>\frac32\log n\), the same estimate holds on \(n/2\le k\le3n/4\), while for \(k\ge3n/4\),
\[
\frac{b_{k+1}}{b_k}
\ge n^{1/8+o(1)}.
\]
Hence the final part of the sum is at most
\[
(1+o(1))b_n
=
(1+o(1))\frac{e^{aN}}{n!}
=o(1).
\]
This proves the required tail bound. Since \(e^{af(\pi)}\ge1\), the expectation is \(1+o(1)\). \(\square\)

# 6. The second moment

Assume now that
\[
\mu_n(r)=(n!)^{m-1}p_m(r)^N\longrightarrow\infty.
\]
Let
\[
h_k=-\log p_k(r),
\qquad
\lambda=\frac{h_m}{m-1}.
\]
Then
\[
\frac{e^{\lambda N}}{n!}
=
\mu_n(r)^{-1/(m-1)}
\longrightarrow0.
\]
Lemma 3 therefore gives
\[
A_n(\lambda):=
\mathbb E_{\pi\in S_n}e^{\lambda f(\pi)}
=1+o(1).
\]

Also,
\[
h_m\ge \frac{\binom m2}{r}.
\]
The assumption \(\mu_n(r)\to\infty\) consequently implies
\[
r\ge (1+o(1))\frac{mN}{2\log(n!)}
=\Theta\left(\frac n{\log n}\right).
\]
In particular,
\[
\frac N{r^3}=o(1).
\]

For a pair of stackings, let \(B\) be the associated bipartite multigraph, and write
\[
W(B)=\prod_{uv}p_{k_{uv}}(r)^{-1}.
\]
Lemma 2 yields, uniformly over all pairs,
\[
\frac{\Pr(\text{both stackings are rainbow})}{p_m(r)^{2N}}
=
(1+o(1))W(B).
\]

It remains to average \(W(B)\).

Let the \(m\) perfect matchings of \(B\) be induced by vertex permutations
\[
\pi_1=\mathrm{id},\pi_2,\ldots,\pi_m.
\]
For a bundle of size \(k\), its contribution to \(\log W\) is \(h_k\).

The ratios
\[
\frac{h_k}{\binom k2}
\]
are nondecreasing in \(k\). Indeed, if
\[
c_j=-\log\left(1-\frac jr\right),
\]
then
\[
h_k=\sum_{j=1}^{k-1}c_j,
\qquad
\binom k2=\sum_{j=1}^{k-1}j,
\]
and
\[
\frac{c_j}{j}
=
\sum_{\ell\ge1}\frac{j^{\ell-1}}{\ell r^\ell}
\]
is nondecreasing in \(j\). Therefore
\[
h_k\le
\frac{h_m}{\binom m2}\binom k2.
\]

Let
\[
F=\sum_{uv}\binom{k_{uv}}2.
\]
Equivalently,
\[
F=\sum_{1\le i<j\le m} f(\pi_i^{-1}\pi_j).
\]
It follows that
\[
\log W(B)
\le
\frac{h_m}{\binom m2}F
=
\frac{2\lambda}{m}F.
\]

For a spanning tree \(T\) on \([m]\), put
\[
S_T=\sum_{ij\in E(T)}f(\pi_i^{-1}\pi_j).
\]
In a uniform random spanning tree, every pair \(ij\) occurs with probability \(2/m\). Hence
\[
\mathbb E_T S_T=\frac2mF.
\]
Consequently,
\[
\log W(B)\le \lambda\max_T S_T.
\]
Thus, pointwise,
\[
W(B)-1
\le
\sum_T\left(e^{\lambda S_T}-1\right),
\]
where the sum is over the finitely many spanning trees on \([m]\).

For any fixed tree \(T\), the relative permutations
\[
\pi_i^{-1}\pi_j,\qquad ij\in E(T),
\]
are independent uniform permutations: after rooting \(T\), assigning these increments is a bijection from \((S_n)^{m-1}\) to itself. Therefore
\[
\mathbb E e^{\lambda S_T}
=
A_n(\lambda)^{m-1}
=
1+o(1).
\]
Since \(m\) is fixed,
\[
\mathbb E W(B)=1+o(1).
\]

Averaging the joint-probability estimate now gives
\[
\frac{\mathbb E X^2}{(\mathbb E X)^2}
=
1+o(1).
\]
Paley–Zygmund yields
\[
\Pr(X>0)\ge
\frac{(\mathbb E X)^2}{\mathbb E X^2}
=1-o(1).
\]
This completes the proof of the first-moment criterion.

# 7. Construction of the single threshold

For real \(x>m-1\), define
\[
\ell_n(x)
=
(m-1)\log(n!)+N\log p_m(x).
\]
This is strictly increasing. Let \(\rho_m(n)\) be its unique zero.

Among the integers bracketing \(\rho_m(n)\), choose \(k_n\) to minimize
\[
|\ell_n(k_n)|.
\]
Set
\[
r_0(n)=k_n.
\]

Near \(\rho_m(n)\),
\[
\ell_n(r+1)-\ell_n(r)
=
N\bigl(h_m(r)-h_m(r+1)\bigr)
=
(1+o(1))\frac{N\binom m2}{r^2}
=
\Theta(\log^2 n).
\]
Because \(k_n\) is the closer of the two bracketing integers, this implies
\[
\ell_n(k_n-1)\longrightarrow-\infty,
\qquad
\ell_n(k_n+1)\longrightarrow+\infty.
\]

Therefore, for any integer sequence \(r(n)<r_0(n)\),
\[
\mu_n(r(n))
\le \mu_n(k_n-1)\longrightarrow0,
\]
so no rainbow stacking exists with high probability. For any integer sequence \(r(n)>r_0(n)\),
\[
\mu_n(r(n))
\ge \mu_n(k_n+1)\longrightarrow\infty,
\]
so a rainbow stacking exists with high probability.

Finally,
\[
-\log p_m(r)
=
\frac{m(m-1)}{2r}
+
\frac{m(m-1)(2m-1)}{12r^2}
+O_m(r^{-3}),
\]
and solving \(\ell_n(\rho_m(n))=0\) gives
\[
\rho_m(n)
=
\frac{m\binom n2}{2\log(n!)}
+\frac{2m-1}{6}
+o(1).
\]

Thus \(r_0(n)\) may be chosen as the integer closest in logarithmic first-moment scale to this value. The posed strict inequalities intentionally leave the single value \(r=r_0(n)\) unrestricted.

# 8. Scope

The proof covers every fixed \(m\ge2\). The case \(m=1\) is trivial. Constants in the bounded-degree expansion and the number of spanning trees depend on \(m\), so no claim is made here when \(m=m(n)\) grows.