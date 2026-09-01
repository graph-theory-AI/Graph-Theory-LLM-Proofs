```json
{
  "verdict": "ill_posed",
  "confidence": "high",
  "one_line": "The catalog item is a research programme rather than a quantified conjecture; moreover, one natural universal Kendall-tau formulation is false in the canonical sampling model.",
  "would_publish": false,
  "caveats": "The negative result below concerns property-independent canonical induced-subpermutation testers, not fixed-property polynomial bounds or adaptive value-query models."
}
```

# Mathematical writeup

## 1. What is the proposed statement?

The sentence

> “It remains a major open problem if better bounds hold for the various property testing results”

does not specify:

- the class of properties;
- the distance;
- whether constants or exponents may depend on the property;
- one-sided, two-sided, or tolerant testing;
- the query oracle;
- what “better” means.

The only precise assertion in the supplied material is the theorem already reported by Fox and Wei: hereditary permutation properties admit a property-independent polynomial query bound for two-sided testing under rectangular distance.

For Kendall distance, at least the following two possible formulations are substantially different:

\[
\tag{U-K}
\exists q(\varepsilon)\ \forall\text{ hereditary }\mathcal P:
\mathcal P\text{ is }q(\varepsilon)\text{-testable},
\]
where \(q\) is independent of \(\mathcal P\), and

\[
\tag{P-K}
\forall\text{ hereditary }\mathcal P\ \exists C_{\mathcal P},c_{\mathcal P}:
q_{\mathcal P}(\varepsilon)\le C_{\mathcal P}\varepsilon^{-c_{\mathcal P}}.
\]

The result below disproves (U-K) in the standard canonical model where the tester only sees a uniformly sampled induced subpermutation. It says nothing against (P-K).

---

## 2. No property-independent Kendall bound for canonical testers

For \(\pi,\rho\in S_n\), write

\[
K(\pi,\rho)
 =
\#\bigl\{\{i,j\}:
(\pi(i)-\pi(j))(\rho(i)-\rho(j))<0
\bigr\}
\]

and normalize Kendall distance by

\[
d_K(\pi,\rho)=\frac{K(\pi,\rho)}{\binom n2}.
\]

For a property \(\mathcal P\), let

\[
d_K(\pi,\mathcal P)=\min_{\rho\in\mathcal P\cap S_n}d_K(\pi,\rho).
\]

A canonical \(q\)-sample tester chooses a uniformly random \(q\)-subset of positions and is shown only the pattern induced by those positions. Its decision rule may depend on \(n\) and on \(\mathcal P\), and may be randomized.

### Proposition

For every fixed \(q\), there is a hereditary permutation property \(\mathcal P\) such that no canonical \(q\)-sample tester distinguishes

\[
\pi\in\mathcal P
\qquad\text{from}\qquad
d_K(\pi,\mathcal P)\ge \frac14
\]

with completeness and soundness \(2/3\), for all sufficiently large \(n\).

Consequently, even at \(\varepsilon=1/4\), there is no query bound independent of the hereditary property in this model.

### Proof

#### Step 1: A finite permutation whose \(q\)-patterns are almost uniform

For \(\sigma\in S_M\), let \(D_q(\sigma)\) be the distribution of the pattern induced by a uniformly random \(q\)-subset of \([M]\).

For every fixed \(q\) and every \(\eta>0\), if \(M\) is sufficiently large, there is \(\sigma\in S_M\) such that

\[
\left\|D_q(\sigma)-\operatorname{Unif}(S_q)\right\|_{\mathrm{TV}}<\eta.
\]

Indeed, take \(\sigma\) uniformly from \(S_M\). For each \(\alpha\in S_q\), its induced density is an average over the \(\binom Mq\) position sets. Two summands belonging to disjoint position sets are independent. There are only \(O_q(M^{2q-1})\) intersecting ordered pairs, so

\[
\operatorname{Var}(t(\alpha,\sigma))=O_q(M^{-1}).
\]

Since \(S_q\) is finite, all \(q\)-pattern densities simultaneously converge in probability to \(1/q!\).

Choose \(M\) and \(\sigma\) so that

\[
\left\|D_q(\sigma)-\operatorname{Unif}(S_q)\right\|_{\mathrm{TV}}
  +\frac{\binom q2}{M}
<\frac1{12}.
\tag{1}
\]

#### Step 2: The hereditary property

For nonnegative integers \(a_1,\ldots,a_M\), let

\[
\sigma[\iota_{a_1},\ldots,\iota_{a_M}]
\]

denote the inflation of \(\sigma\) in which its \(i\)-th entry is replaced by an increasing block of length \(a_i\); zero-length blocks are simply omitted.

Define

\[
\mathcal P_\sigma
 =
\left\{
\sigma[\iota_{a_1},\ldots,\iota_{a_M}]
:\ a_i\ge 0
\right\}.
\]

This is hereditary: taking an induced subpermutation merely replaces each \(a_i\) by the number of selected elements from that block.

For each \(n\),

\[
|\mathcal P_\sigma\cap S_n|
 \le \#\{(a_1,\ldots,a_M):a_i\ge0,\ \sum_i a_i=n\}
 \le (n+1)^M.
\tag{2}
\]

#### Step 3: Almost every permutation is Kendall-far from \(\mathcal P_\sigma\)

Fix \(\rho\in S_n\), and let \(\Pi\) be uniform in \(S_n\). Then \(K(\Pi,\rho)\) has the same distribution as the inversion number of a uniform permutation.

The inversion number can be written as

\[
Z=\sum_{j=1}^n Z_j,
\]

where the \(Z_j\) are independent and \(Z_j\) is uniform on
\(\{0,\ldots,j-1\}\). Thus

\[
\mathbb EZ=\frac12\binom n2.
\]

Hoeffding's inequality gives, with \(N=\binom n2\),

\[
\Pr\left(Z<\frac N4\right)
 \le
 \exp\left(
 -\frac{N^2}{8\sum_{j=1}^n(j-1)^2}
 \right)
 \le e^{-3n/128}.
\tag{3}
\]

By (2), (3), and a union bound,

\[
\Pr\left(d_K(\Pi,\mathcal P_\sigma)<\frac14\right)
 \le (n+1)^M e^{-3n/128}
 =o(1)
\tag{4}
\]

as \(n\to\infty\), with \(M\) fixed.

#### Step 4: A member of the property has almost uniform \(q\)-patterns

Take \(n=Mr\) and the balanced inflation

\[
\rho_n=\sigma[\iota_r,\ldots,\iota_r]\in\mathcal P_\sigma.
\]

When \(q\) positions are sampled, the probability that two lie in the same block is at most

\[
\binom q2\frac{r-1}{Mr-1}
\le \frac{\binom q2}{M}.
\]

Conditional on meeting distinct blocks, the selected block set is a uniformly random \(q\)-subset of \([M]\), and the induced pattern has distribution \(D_q(\sigma)\). Hence, by (1),

\[
\left\|D_q(\rho_n)-\operatorname{Unif}(S_q)\right\|_{\mathrm{TV}}
<\frac1{12}.
\tag{5}
\]

#### Step 5: Contradiction to a canonical tester

Suppose there were a canonical \(q\)-sample tester. For each \(n\), let

\[
a_n(\alpha)\in[0,1]
\]

be its acceptance probability upon seeing \(\alpha\in S_q\).

Completeness on \(\rho_n\) and (5) imply

\[
\mathbb E_{\alpha\sim\operatorname{Unif}(S_q)}a_n(\alpha)
 \ge \frac23-\frac1{12}
 =\frac7{12}.
\tag{6}
\]

On the other hand, if \(\Pi\) is uniform in \(S_n\), its sampled \(q\)-pattern is exactly uniform in \(S_q\). By (4), \(\Pi\) is \(1/4\)-far from \(\mathcal P_\sigma\) with probability \(1-o(1)\). Soundness would therefore imply

\[
\mathbb E_{\alpha\sim\operatorname{Unif}(S_q)}a_n(\alpha)
 \le \frac13+o(1),
\tag{7}
\]

contradicting (6) for sufficiently large \(n\). ∎

### Consequence

The exact analogue of Fox–Wei's property-independent rectangular-distance bound cannot hold for Kendall distance in this canonical model—not merely polynomially, but with any finite \(q(1/4)\) independent of the property.

The construction varies \(\mathcal P_\sigma\) with \(q\), so it does not rule out a polynomial bound whose constants or exponent depend on the fixed property.

---

## 3. Why rectangular testing does not automatically transfer to Kendall distance

Under the standard same-order rectangular distance

\[
d_\square(\pi,\rho)
=
\frac1n
\max_{\substack{I,J\subseteq[n]\\ I,J\text{ intervals}}}
\left|
|\{i\in I:\pi(i)\in J\}|
-
|\{i\in I:\rho(i)\in J\}|
\right|,
\]

there is a useful one-way inequality.

### Lemma

For all \(\pi,\rho\in S_n\),

\[
d_\square(\pi,\rho)\le \sqrt{2d_K(\pi,\rho)}.
\]

#### Proof

Let \(K=K(\pi,\rho)\). For \(t\in[n]\), put

\[
A_t=\pi^{-1}([t]),\qquad B_t=\rho^{-1}([t]).
\]

Write \(X=A_t\setminus B_t\) and \(Y=B_t\setminus A_t\). Since both \(A_t\) and \(B_t\) have size \(t\),

\[
|X|=|Y|=:r.
\]

For every \(x\in X\) and \(y\in Y\),

\[
\pi(x)\le t<\pi(y),
\qquad
\rho(y)\le t<\rho(x),
\]

so \(\{x,y\}\) is Kendall-discordant. Thus \(K\ge r^2\).

For every interval \(I\),

\[
\bigl||A_t\cap I|-|B_t\cap I|\bigr|
 \le r\le\sqrt K.
\]

Writing a value interval \(J=[a,b]\) as the difference of the two prefixes
\([b]\) and \([a-1]\) gives rectangle discrepancy at most \(2\sqrt K\). Therefore

\[
d_\square(\pi,\rho)
\le \frac{2\sqrt K}{n}
=
\sqrt{2\frac{n-1}{n}d_K(\pi,\rho)}
\le \sqrt{2d_K(\pi,\rho)}.
\]
∎

The direction is insufficient for Kendall testing: Kendall-farness need not imply rectangular-farness.

Indeed, for independent uniform \(\pi_n,\rho_n\in S_n\), a hypergeometric concentration bound and a union bound over fewer than \(n^4\) interval rectangles give, with positive probability,

\[
d_\square(\pi_n,\rho_n)
 =O\left(\sqrt{\frac{\log n}{n}}\right),
\]

whereas \(d_K(\pi_n,\rho_n)\to 1/2\) in probability. Thus there is no converse inequality

\[
d_K\le f(d_\square)
\quad\text{with}\quad
f(x)\to0.
\]

Additional structure from the hereditary property would therefore be necessary to transfer rectangular testing results to Kendall distance.

---

## 4. A simple fixed-property positive case

For the hereditary property consisting only of increasing permutations,

\[
\mathcal I\cap S_n=\{\operatorname{id}_n\},
\]

one has

\[
d_K(\pi,\mathcal I)
=
\frac{\operatorname{inv}(\pi)}{\binom n2}.
\]

Sampling

\[
m=\left\lceil\frac{\log 3}{\varepsilon}\right\rceil
\]

independent uniformly random pairs and rejecting if any sampled pair is an inversion gives a one-sided tester using at most \(2m=O(1/\varepsilon)\) value queries. If \(d_K(\pi,\mathcal I)\ge\varepsilon\), its acceptance probability is at most

\[
(1-\varepsilon)^m\le e^{-\varepsilon m}\le\frac13.
\]

Thus property-dependent polynomial Kendall testing is possible in at least this basic case.

---

## 5. Remaining gaps

The arguments above do not settle any of the following precise questions:

1. Whether every fixed hereditary permutation property has
   \(C_{\mathcal P}\varepsilon^{-c_{\mathcal P}}\) query complexity under Kendall distance.
2. Whether a universal exponent is possible while constants depend on the property or its smallest forbidden pattern.
3. Adaptive testers receiving exact values \(\pi(i)\), rather than only an induced pattern.
4. One-sided or tolerant testing.
5. Analogous questions for earth-mover, footrule, deletion, or other metrics.

Consequently, the catalog item as written has no single provable or disprovable content. The strongest natural universal Kendall interpretation is false in the canonical model, while the weaker fixed-property polynomial question remains untouched by this argument.