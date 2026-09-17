```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A uniform exponential-moment bound for configuration-model maps proves the conjectured a.a.s. logarithmic bound when np=O(sqrt(log n)).",
  "would_publish": false,
  "caveats": "The general density range remains unresolved by this argument; no priority claim is made for the sparse-range consequence."
}
```

## 1. Convention and partial result

I use the paper’s stated convention for disconnected graphs. If \(G\) has components \(G_1,\dots,G_c\), then
\[
F(G,\rho)=1+\sum_{i=1}^c\bigl(F(G_i,\rho_i)-1\bigr).
\]
An isolated vertex is assigned one face. Thus every tree component has zero net contribution to the sum. In particular, the isolated-edge argument in the previous attempt does not apply.

Write
\[
f(G)=\mathbb E_\rho[F(G,\rho)],
\]
where the local rotations are independent and uniform.

The following is a self-contained partial result. All logarithms below are natural.

### Theorem
Let \(G\sim G(n,p)\), where \(n\ge2\) and \(0\le p\le \tfrac12\), and put \(d=np\). For every \(t\ge0\),
\[
\boxed{
\mathbb P\!\left(
f(G)>
\frac{\ln 2+\frac32\ln(n^2p+2)+d+d^2+t}{\ln 2}
\right)
\le e^{-t}.
}
\tag{1}
\]

Consequently,
\[
f(G)=O\bigl(\log n+(np)^2\bigr)
\qquad\text{a.a.s.}
\tag{2}
\]
In particular, the conjecture holds for every density function satisfying
\[
np=O(\sqrt{\log n}).
\tag{3}
\]

The proof controls the conditional expectation \(f(G)\) for most sampled graphs, not merely the joint expectation over graphs and embeddings.

---

## 2. An exponential-moment bound for configuration-model maps

A configuration-model map consists of:

- a prescribed number of distinguishable stubs at each vertex;
- a fixed cyclic order of the stubs at each vertex;
- a uniformly random perfect matching of all stubs.

Matched stubs form edges, allowing loops and parallel edges. The cyclic orders define an orientable embedding.

### Lemma
For any degree sequence with total degree \(2m\), and any fixed cyclic orders of its stubs, the normalized face count of the resulting configuration-model map satisfies
\[
\mathbb E[2^F]\le 2(m+1)^{3/2}.
\tag{4}
\]

The bound is independent of the degree sequence and the number of vertices.

### Proof when all degrees are at least two

Let \(\sigma\) be the permutation whose cycles are the prescribed vertex rotations, and let \(\alpha\) be the uniform perfect matching, viewed as a fixed-point-free involution. Let
\[
Z=\#\operatorname{cycles}(\sigma\alpha).
\]
Thus \(Z\) is the unnormalized sum of the face counts of the components.

We first prove
\[
\mathbb E_\alpha[2^Z]
\le
\frac{2^m(m+1)!}{(2m-1)!!}.
\tag{5}
\]

Consider the \(2\times2\) Hermitian Gaussian matrix
\[
X=
\begin{pmatrix}
A & (C+iD)/\sqrt2\\
(C-iD)/\sqrt2 & B
\end{pmatrix},
\]
where \(A,B,C,D\) are independent standard real Gaussian variables. Its entries satisfy
\[
\mathbb E[X_{ab}X_{cd}]=\delta_{ad}\delta_{bc}.
\tag{6}
\]

If the vertex degrees are \(d_1,\dots,d_k\), the Gaussian pairing formula gives
\[
\mathbb E_X\!\left[\prod_{v=1}^k\operatorname{tr}(X^{d_v})\right]
=
\sum_{\alpha}2^{\#\operatorname{cycles}(\sigma\alpha)},
\tag{7}
\]
where the sum is over all perfect matchings of the \(2m\) stubs.

For completeness, expand the traces using indices \(i_h\in\{1,2\}\) attached to the stubs:
\[
\prod_v\operatorname{tr}(X^{d_v})
=
\sum_{(i_h)}
\prod_h X_{i_h,i_{\sigma(h)}}.
\]
In the Gaussian pairing indexed by \(\alpha\), equation (6) identifies precisely the indices belonging to the same cycle of \(\sigma\alpha\). Each such cycle therefore contributes a factor \(2\). This proves (7). The Gaussian pairing formula itself follows by repeated Gaussian integration by parts.

For every Hermitian matrix and every integer \(r\ge2\),
\[
\bigl|\operatorname{tr}(X^r)\bigr|
\le \bigl(\operatorname{tr}(X^2)\bigr)^{r/2}.
\tag{8}
\]
Indeed, this follows by applying
\[
|x|^r+|y|^r\le (x^2+y^2)^{r/2}
\]
to the two eigenvalues.

Since every \(d_v\ge2\) and \(\sum_vd_v=2m\), equations (7)–(8) imply
\[
\sum_\alpha 2^{\#\operatorname{cycles}(\sigma\alpha)}
\le
\mathbb E\bigl[(\operatorname{tr}(X^2))^m\bigr].
\]
Here
\[
\operatorname{tr}(X^2)=A^2+B^2+C^2+D^2,
\]
so its \(m\)-th moment is
\[
\mathbb E\bigl[(\operatorname{tr}(X^2))^m\bigr]
=2^m(m+1)!.
\]
There are \((2m-1)!!\) perfect matchings, proving (5).

Finally,
\[
\frac{2^m(m+1)!}{(2m-1)!!}
=
\frac{(m+1)4^m}{\binom{2m}{m}}
\le 2(m+1)\sqrt m
\le 2(m+1)^{3/2},
\tag{9}
\]
using the elementary estimate
\[
\binom{2m}{m}\ge \frac{4^m}{2\sqrt m}\qquad(m\ge1).
\]

If the map has \(c\ge1\) components, its normalized face count is \(F=Z-c+1\le Z\). Thus (4) follows in this case.

### Removing the minimum-degree assumption

Discard isolated vertices. While a vertex has exactly one remaining stub, expose that stub’s matching partner, remove the resulting pendant edge, and discard any isolated vertices that arise.

Deleting a pendant edge and its leaf does not change the number of faces of its component. Deleting an entire tree component also does not change the normalized statistic. Hence this procedure preserves \(F\).

Each exposure leaves a uniform matching on the remaining stubs. The stopping rule depends only on information already exposed. Consequently, conditional on the entire pruning history, the residual matching is uniform, and every residual vertex has degree at least two.

If the residual graph has \(m'\ge1\) edges, the preceding argument gives, conditionally on that history,
\[
\mathbb E[2^F\mid\text{pruning history}]
\le 2(m'+1)^{3/2}
\le 2(m+1)^{3/2}.
\]
If the residual graph is empty, the original graph was a forest and \(F=1\), so the same bound holds. This proves the lemma. \(\square\)

---

## 3. Poissonization and conditioning on simplicity

Fix \(0\le p<1\), and set
\[
\lambda=\frac{p}{1-p},
\qquad
\mu=\frac{\lambda n^2}{2}.
\]

Construct a random configuration-model map as follows:

1. Sample \(M\sim\operatorname{Poisson}(\mu)\).
2. Conditional on \(M=m\), sample
   \[
   (d_1,\dots,d_n)\sim
   \operatorname{Multinomial}(2m;1/n,\dots,1/n).
   \]
3. Give each vertex its stubs in a fixed cyclic order and choose a uniform perfect matching of all stubs.

The underlying multigraph has the same law as \(M\) independently sampled edges whose two endpoints are independent uniform vertices. Therefore:

- for each unordered pair \(u\ne v\), its edge multiplicity is \(\operatorname{Poisson}(\lambda)\);
- at each vertex, its loop multiplicity is \(\operatorname{Poisson}(\lambda/2)\);
- all these multiplicities are independent.

Let \(S\) be the event that the resulting multigraph is simple. Conditional on \(S\), each potential nonloop edge is present independently with probability
\[
\frac{\lambda}{1+\lambda}=p.
\]
Thus the conditional underlying graph is exactly \(G(n,p)\).

The conditional local rotations are also independent and uniform. To see this, fix a simple graph \(H\). At a vertex of degree \(r\ge1\), its incident edges can be assigned to its distinguishable stubs in \(r!\) ways. Each cyclic order of its incident edges is induced by exactly \(r\) such assignments. These assignments are independent across vertices.

### Probability of simplicity

Writing \(N=\binom n2\), independence of the multiplicities gives
\[
\mathbb P(S)
=e^{-\lambda n/2}
\bigl(e^{-\lambda}(1+\lambda)\bigr)^N
=e^{-A},
\tag{10}
\]
where
\[
A=\frac{\lambda n}{2}
+N\bigl(\lambda-\ln(1+\lambda)\bigr).
\tag{11}
\]

### The unconditional moment

By the lemma,
\[
\mathbb E[2^F]\le 2\,\mathbb E[(M+1)^{3/2}].
\]
Using the second moment of a Poisson variable,
\[
\begin{aligned}
\mathbb E[(M+1)^{3/2}]
&\le \bigl(\mathbb E[(M+1)^2]\bigr)^{3/4}\\
&=(\mu^2+3\mu+1)^{3/4}\\
&\le(\mu+2)^{3/2}.
\end{aligned}
\]
Hence
\[
\mathbb E[2^F]\le 2(\mu+2)^{3/2}.
\tag{12}
\]

---

## 4. Passing to the conditional expectation \(f(G)\)

For each fixed simple graph \(G\), Jensen’s inequality gives
\[
2^{f(G)}
=
2^{\mathbb E_\rho F(G,\rho)}
\le
\mathbb E_\rho[2^{F(G,\rho)}].
\tag{13}
\]
Therefore, using the conditional distribution established above,
\[
\begin{aligned}
\mathbb E_{G(n,p)}[2^{f(G)}]
&\le \mathbb E[2^F\mid S]\\
&\le \frac{\mathbb E[2^F]}{\mathbb P(S)}\\
&\le 2(\mu+2)^{3/2}e^A.
\end{aligned}
\tag{14}
\]

This is the step that supplies a high-probability result for \(f(G)\), rather than just a bound on its mean.

For \(p\le\tfrac12\), we have \(\lambda\le2p\), and consequently
\[
\mu\le n^2p.
\tag{15}
\]
Also,
\[
\lambda-\ln(1+\lambda)\le\frac{\lambda^2}{2},
\]
so
\[
A
\le \frac{\lambda n}{2}+\frac{N\lambda^2}{2}
\le np+n^2p^2
=d+d^2.
\tag{16}
\]
Combining (14)–(16),
\[
\mathbb E_{G(n,p)}[2^{f(G)}]
\le
2(n^2p+2)^{3/2}e^{d+d^2}.
\tag{17}
\]
Markov’s inequality now proves (1).

The same estimate also yields the joint-mean bound
\[
\mathbb E_{G(n,p)}[f(G)]
\le
\frac{\ln 2+\frac32\ln(n^2p+2)+d+d^2}{\ln 2}.
\tag{18}
\]

Taking \(t=2\ln n\) in (1) proves (2), with failure probability at most \(n^{-2}\). If \(d=O(\sqrt{\log n})\), its right-hand threshold is \(O(\log n)\), proving (3).

---

## 5. What remains unresolved

This does **not** prove the conjecture for arbitrary \(p(n)\).

The loss is explicit: we bounded the moment conditioned on simplicity by dividing by \(\mathbb P(S)\). In the sparse regime \(p=o(1)\),
\[
A=(1+o(1))
\left(\frac{np}{2}+\frac{(np)^2}{4}\right).
\]
Thus the conditioning cost is polynomial in \(n\) when \(np=O(\sqrt{\log n})\), but can be superpolynomial beyond that range. The argument then gives an additional \((np)^2\) term rather than a logarithmic bound.

Removing or substantially reducing this conditioning loss would require an additional argument controlling the dependence between simplicity and the face statistic; no such argument is supplied here.

The established result is therefore a rigorous sparse-density special case, together with the quantitative tail bound (1). I do not assert that this consequence is new relative to the full parameter range of Section 8 of the source paper.