```json
{
  "verdict": "disproved",
  "confidence": "high",
  "one_line": "A cyclically invariant family defined by comparing the longest cyclic runs inside a support and its complement is intersecting and has only polynomially small density.",
  "would_publish": false,
  "caveats": "This uses the source definition of symmetry as invariance under a transitive coordinate group; the construction is not invariant under the full symmetric group."
}
```

# Counterexample

Throughout, “symmetric” means invariant under some transitive group of coordinate permutations, as in the source paper.

Fix \(k\ge 3\), and put
\[
p=\frac1k<\frac12.
\]
We first construct a cyclically symmetric intersecting family of subsets of \(\mathbb Z_n\).

## 1. A cyclically symmetric intersecting set family

For \(S\subseteq \mathbb Z_n\), let \(\ell(S)\) denote the maximum length of a cyclic interval contained in \(S\). Set \(\ell(\varnothing)=0\). Define
\[
\mathcal F_n=\{S\subseteq \mathbb Z_n:\ell(S)>\ell(S^c)\}.
\]

### Lemma 1
\(\mathcal F_n\) is increasing, intersecting, and invariant under cyclic rotations.

#### Proof

Rotation invariance is immediate because rotations preserve cyclic intervals.

If \(S\subseteq T\), then
\[
\ell(T)\ge \ell(S)
\qquad\text{and}\qquad
\ell(T^c)\le \ell(S^c).
\]
Consequently, \(\ell(S)>\ell(S^c)\) implies \(\ell(T)>\ell(T^c)\), so \(\mathcal F_n\) is increasing.

Moreover, \(\mathcal F_n\) is complement-free: if \(S\in\mathcal F_n\), then
\[
\ell(S)>\ell(S^c),
\]
and hence \(S^c\notin\mathcal F_n\).

Suppose now that \(S,T\in\mathcal F_n\) were disjoint. Then \(T\subseteq S^c\). Since \(\mathcal F_n\) is increasing, \(T\in\mathcal F_n\) would imply \(S^c\in\mathcal F_n\), contradicting complement-freeness. Thus \(\mathcal F_n\) is intersecting. \(\square\)

## 2. Its biased measure is only polynomially small

Let \(\mu_p\) be the \(p\)-biased product measure on \(2^{\mathbb Z_n}\). Write
\[
\lambda=-\log(1-p)=\log\frac1{1-p}>0
\]
and, for sufficiently large \(n\), set
\[
m=\left\lceil \frac{3\log n}{\lambda}\right\rceil<n.
\]

Fix one cyclic interval \(I\) of length \(m\). Consider a \(p\)-random set \(S\), conditioned on \(I\subseteq S\). There are \(n\) cyclic intervals of length \(m\). For each such interval \(J\),

- if \(J\cap I\ne\varnothing\), then \(J\subseteq S^c\) is impossible;
- if \(J\cap I=\varnothing\), then conditionally
  \[
  \Pr(J\subseteq S^c)=(1-p)^m.
  \]

Hence, by the union bound,
\[
\Pr\bigl(\ell(S^c)\ge m\mid I\subseteq S\bigr)
 \le n(1-p)^m
 \le n e^{-3\log n}
 =n^{-2}.
\]
On the complementary event,
\[
\ell(S)\ge m>\ell(S^c),
\]
so \(S\in\mathcal F_n\). Therefore
\[
\mu_p(\mathcal F_n)
 \ge p^m(1-n^{-2}).
\]

Since
\[
m\le \frac{3\log n}{\lambda}+1,
\]
we have
\[
p^m
 \ge p^{\,3\log n/\lambda+1}
 =p\,n^{-\gamma},
\qquad
\gamma=\frac{3\log(1/p)}{\log(1/(1-p))}.
\]
Thus, for all sufficiently large \(n\),
\[
\boxed{\mu_p(\mathcal F_n)\ge \frac p2\,n^{-\gamma}.}
\]

In particular, the density tends to zero only polynomially.

## 3. Lift to a vector family

For \(x=(x_i)_{i\in\mathbb Z_n}\in[k]^n\), define its \(1\)-support by
\[
S_1(x)=\{i\in\mathbb Z_n:x_i=1\}.
\]
Now let
\[
A_n=\{x\in[k]^n:S_1(x)\in\mathcal F_n\}.
\]

The cyclic rotation group acts transitively on the coordinates and preserves \(A_n\), so \(A_n\) is symmetric in the source-paper sense.

If \(x,y\in A_n\), then \(S_1(x),S_1(y)\in\mathcal F_n\). Since \(\mathcal F_n\) is intersecting, there is an \(i\) belonging to both supports. Hence
\[
x_i=y_i=1.
\]
Therefore \(A_n\) is intersecting.

For a uniformly random \(x\in[k]^n\), the indicators
\[
\mathbf 1_{\{x_i=1\}}
\]
are independent Bernoulli variables with parameter \(p=1/k\). Consequently,
\[
\frac{|A_n|}{k^n}=\mu_{1/k}(\mathcal F_n)
 \ge \frac{1}{2k}\,n^{-\gamma_k},
\]
where
\[
\gamma_k
 =\frac{3\log k}{\log(k/(k-1))}.
\]
It follows that
\[
\log_k|A_n|
 \ge n-\gamma_k\log_k n+\log_k\frac1{2k}
 =n-O_k(\log n).
\]

## 4. Contradiction to the proposed bound

If constants \(c,\delta>0\) existed such that every symmetric intersecting \(A\subseteq[k]^n\) satisfied
\[
\log_k|A|\le n-cn^\delta,
\]
then applying this to \(A_n\) would give
\[
c n^\delta
 \le \gamma_k\log_k n-\log_k\frac1{2k}.
\]
The right-hand side is \(O_k(\log n)\), whereas the left-hand side grows as \(n^\delta\). This is impossible for sufficiently large \(n\).

Thus the proposed stretched-exponential density bound is false. In fact, cyclically symmetric intersecting families can have density \(n^{-O_k(1)}\), so no universal deficit \(\omega(\log n)\) in \(\log_k|A|\) is possible under mere transitive coordinate symmetry.