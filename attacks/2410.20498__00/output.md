```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture remains open, but the limit is shown to exist, Poisson-quasirandom families satisfy the conjectured bound, and all affine-subspace constructions have the strictly smaller asymptotic optimum 0.288788...",
  "would_publish": false,
  "caveats": "No argument controls arbitrary high-influence, non-Poisson, nonlinear families."
}
```

# 1. Statement and notation

Write \(Q_n=\{0,1\}^n\). An axis-parallel \(d\)-subcube is specified by a set \(D\in\binom{[n]}d\) of varying coordinates and an assignment to the other \(n-d\) coordinates. Thus there are
\[
\binom nd2^{n-d}
\]
such subcubes.

For \(A\subseteq Q_n\), let
\[
p_d^{(n)}(A)
 =\Pr_C\bigl(|A\cap C|=1\bigr),
\]
where \(C\) is a uniformly random axis-parallel \(d\)-subcube. Then
\[
\lambda(n,d,1)=\max_{A\subseteq Q_n}p_d^{(n)}(A),
\qquad
\lambda_d:=\lambda(d,1)=\lim_{n\to\infty}\lambda(n,d,1).
\]

The random construction, taking every vertex independently with probability \(2^{-d}\), gives
\[
\lambda_d\ge
\left(1-2^{-d}\right)^{2^d-1}
=e^{-1}\left(1+O(2^{-d})\right).
\]
The problem is to prove the matching asymptotic upper bound.

I do not obtain that upper bound. I give four rigorous partial results.

---

# 2. Monotonicity in \(d\)

## Proposition 2.1

For every \(d\ge1\),
\[
\lambda_{d+1}\le \lambda_d.
\]
Consequently,
\[
L:=\lim_{d\to\infty}\lambda_d
\]
exists, and \(L\ge e^{-1}\). Thus the conjecture is equivalent to \(L=e^{-1}\).

## Proof

Fix \(A\subseteq Q_n\). For a coordinate \(i\in[n]\), define its OR-projection
\[
B_i=\left\{y\in Q_{n-1}:
\text{at least one of the two lifts of \(y\) in coordinate \(i\) belongs to \(A\)}
\right\}.
\]

Choose a uniformly random \((d+1)\)-subcube \(C\), and then choose uniformly one of its \(d+1\) varying coordinates \(i\). Collapsing the \(i\)-direction turns \(C\) into a uniformly random \(d\)-subcube \(C'\) of \(Q_{n-1}\).

If \(C\cap A\) consists of exactly one vertex, then \(C'\cap B_i\) consists of exactly one vertex. Therefore
\[
p_{d+1}^{(n)}(A)
\le \frac1n\sum_{i=1}^n p_d^{(n-1)}(B_i)
\le \lambda(n-1,d,1).
\]
Maximizing over \(A\), then taking \(n\to\infty\), proves
\[
\lambda_{d+1}\le\lambda_d.
\]

The random lower bound gives
\[
L\ge\lim_{d\to\infty}
(1-2^{-d})^{2^d-1}=e^{-1}.
\]
\(\square\)

This monotonicity does not identify \(L\), but it rules out oscillatory behavior in \(d\).

---

# 3. A boundary and influence obstruction

Let \(f=1_A\). Use the standard total influence
\[
I(A)=\sum_{i=1}^n
\Pr_{x\in Q_n}\bigl(f(x)\ne f(x\oplus e_i)\bigr).
\]

## Proposition 3.1

For every \(A\subseteq Q_n\),
\[
p_d^{(n)}(A)\le \frac{2^{d-1}}n I(A).
\]

## Proof

For \(a\in A\), let
\[
b_A(a)=
\bigl|\{i\in[n]:a\oplus e_i\notin A\}\bigr|.
\]
If a \(d\)-cube has unique \(A\)-vertex \(a\), then all of its \(d\) varying coordinate directions must belong to this set of \(b_A(a)\) boundary directions. Hence the number of singleton \(d\)-cubes is at most
\[
\sum_{a\in A}\binom{b_A(a)}d.
\]
Since
\[
\frac{\binom bd}{\binom nd}\le \frac bn
\qquad(0\le b\le n),
\]
this is at most
\[
\frac1n\binom nd\sum_{a\in A}b_A(a).
\]

Now \(\sum_{a\in A}b_A(a)=|\partial A|\), the number of undirected boundary edges of \(A\), and
\[
I(A)=\frac{2|\partial A|}{2^n}.
\]
Dividing by the total number \(\binom nd2^{n-d}\) of \(d\)-cubes gives
\[
p_d^{(n)}(A)
\le
\frac{2^d|\partial A|}{n2^n}
=\frac{2^{d-1}}n I(A).
\]
\(\square\)

## Corollary 3.2

If \(d\) is fixed and \(I(A_n)=o(n)\), then
\[
p_d^{(n)}(A_n)\longrightarrow0.
\]

Thus any sequence contributing a positive amount to \(\lambda_d\) must have total influence linear in \(n\).

## Corollary 3.3: monotone families do not contribute

If every \(A_n\subseteq Q_n\) is monotone increasing or monotone decreasing, then for every fixed \(d\),
\[
p_d^{(n)}(A_n)\longrightarrow0.
\]

### Proof

For a monotone Boolean function, writing
\[
S(x)=\sum_{i=1}^n(2x_i-1),
\]
we have
\[
\frac12 I(A)=\mathbb E[fS].
\]
Since \(\mathbb E S=0\), \(\operatorname{Var}(S)=n\), and
\(\operatorname{Var}(f)=\alpha(1-\alpha)\), Cauchy–Schwarz gives
\[
I(A)\le 2\sqrt{\alpha(1-\alpha)n}\le\sqrt n.
\]
Proposition 3.1 now yields
\[
p_d^{(n)}(A)\le \frac{2^{d-1}}{\sqrt n}\longrightarrow0.
\]
\(\square\)

This eliminates all low-influence constructions, including monotone and threshold-type candidates. It does not control the relevant high-influence regime: a random set of density \(2^{-d}\) has \(I(A)=\Theta(n2^{-d})\).

---

# 4. The conjectured upper bound for Poisson-quasirandom families

Let \(C_j\) be a random \(d_j\)-cube, where \(d_j\to\infty\), and put
\[
X_j=|A_j\cap C_j|,\qquad N_j=2^{d_j}.
\]

## Proposition 4.1

Suppose
\[
\mathbb E X_j=N_j\frac{|A_j|}{2^{n_j}}\longrightarrow\mu<\infty
\]
and, for every fixed \(k\ge1\),
\[
\mathbb E (X_j)_k\longrightarrow\mu^k,
\]
where
\[
(x)_k=x(x-1)\cdots(x-k+1).
\]
Then
\[
\Pr(X_j=1)\longrightarrow \mu e^{-\mu}\le e^{-1}.
\]

## Proof

For an integer \(m\ge1\), set
\[
T_m(x)=\sum_{k=1}^m(-1)^{k-1}k\binom{x}{k}.
\]
For integer \(x\ge0\),
\[
T_{2\ell}(x)\le 1_{\{x=1\}}\le T_{2\ell+1}(x).
\]
Indeed, for \(x>m\),
\[
T_m(x)=(-1)^{m-1}x\binom{x-2}{m-1},
\]
while for \(m\ge x\) the full inclusion-exclusion sum equals
\(1_{\{x=1\}}\).

Taking expectations and using
\[
k\binom{X_j}{k}=\frac{(X_j)_k}{(k-1)!},
\]
we obtain, for each fixed \(m\),
\[
\mathbb E T_m(X_j)
\longrightarrow
\mu\sum_{\ell=0}^{m-1}\frac{(-\mu)^\ell}{\ell!}.
\]
Letting the even and odd truncation lengths tend to infinity gives
\[
\Pr(X_j=1)\longrightarrow\mu e^{-\mu}.
\]
The elementary maximum of \(x e^{-x}\) over \(x\ge0\) is \(e^{-1}\).
\(\square\)

A sufficient “cube-quasirandomness” formulation is the following: for every fixed \(k\), the average probability that \(k\) ordered distinct vertices of a random \(d_j\)-cube all belong to \(A_j\) is
\[
(1+o(1))\left(\frac{|A_j|}{2^{n_j}}\right)^k.
\]
If additionally \(N_j|A_j|/2^{n_j}\to\mu\), then the factorial-moment hypothesis follows.

Hence the conjecture is valid for all asymptotically Poisson cube restrictions. Any counterexample must display non-Poisson correlations at some bounded order, or have an unbounded mean cube occupancy together with a persistent singleton component.

---

# 5. Complete analysis of affine-subspace constructions

This section gives a more substantive special case.

Call \(A\subseteq Q_n\) affine if, over \(\mathbb F_2\),
\[
A=\{x\in\mathbb F_2^n:Hx=b\},
\]
where \(H\) has rank \(r\). Thus \(|A|=2^{n-r}\).

## Proposition 5.1: exact formula for a fixed affine space

Let \(h_1,\dots,h_n\in\mathbb F_2^r\) be the columns of \(H\). Then
\[
p_d^{(n)}(A)
=
2^{d-r}
\Pr_{D\in\binom{[n]}d}
\bigl(\{h_i:i\in D\}\text{ is linearly independent}\bigr).
\]

## Proof

Fix \(D\in\binom{[n]}d\), and write \(H_D\) for the corresponding \(r\times d\) submatrix. Once the coordinates outside \(D\) are fixed, the points of \(A\) in the corresponding \(d\)-cube are the solutions of a system
\[
H_Dx_D=c.
\]
Every nonempty solution set has size
\[
2^{d-\operatorname{rank}H_D}.
\]
Thus a fiber can be a singleton exactly when \(\operatorname{rank}H_D=d\).

If \(H_D\) has full column rank, projection of \(A\) to the coordinates outside \(D\) is injective. Hence exactly \(|A|=2^{n-r}\) of the \(2^{n-d}\) fibers are singletons. Their fraction is
\[
\frac{2^{n-r}}{2^{n-d}}=2^{d-r}.
\]
Averaging over \(D\) proves the formula.
\(\square\)

We next optimize the independence probability. I use the established matroid basis-polynomial log-concavity theorem: the basis-generating polynomial of every finite matroid is log-concave on the positive orthant. This is a proved consequence of the Lorentzian-polynomial theory.

## Lemma 5.2

Let \(X_1,\dots,X_d\) be iid with an arbitrary distribution on \(\mathbb F_2^r\), where \(r\ge d\). Then
\[
\Pr(X_1,\dots,X_d\text{ independent})
\le
\prod_{i=0}^{d-1}\frac{2^r-2^i}{2^r-1}.
\]
Equality is attained by the uniform distribution on
\(\mathbb F_2^r\setminus\{0\}\).

## Proof

Consider the rank-\(d\) truncation of the vector matroid on the nonzero vectors of \(\mathbb F_2^r\). Its bases are precisely the linearly independent \(d\)-subsets. If \(p_v\) is the probability of vector \(v\), then
\[
\Pr(X_1,\dots,X_d\text{ independent})
=d!\sum_{\substack{B\subseteq\mathbb F_2^r\setminus\{0\}\\
|B|=d,\ B\text{ independent}}}\prod_{v\in B}p_v.
\]
The sum is the matroid basis-generating polynomial.

Mass at \(0\) can only decrease this homogeneous polynomial, so assume \(p_0=0\). The group \(\mathrm{GL}(r,2)\) acts transitively on the nonzero vectors and preserves the polynomial. By log-concavity, averaging \(p\) over this group cannot decrease the polynomial. The averaged distribution is uniform on the \(2^r-1\) nonzero vectors.

For that distribution, after \(i\) independent vectors have been selected, their span contains \(2^i-1\) nonzero vectors. Thus the probability that the next vector lies outside the span is
\[
\frac{2^r-2^i}{2^r-1}.
\]
Multiplication over \(i=0,\dots,d-1\) gives the result.
\(\square\)

Define \(\lambda_{\mathrm{aff}}(d,1)\) by restricting the maximizing sets to affine subspaces. Combining the last two results gives the exact limiting formula
\[
\boxed{
\lambda_{\mathrm{aff}}(d,1)
=
\sup_{r\ge d}
2^{d-r}
\prod_{i=0}^{d-1}
\frac{2^r-2^i}{2^r-1}.
}
\]
The upper bound is attained asymptotically in \(n\) by taking the columns of \(H\) with asymptotically uniform frequencies over all nonzero vectors of \(\mathbb F_2^r\).

## Corollary 5.3

Let
\[
q=\prod_{j=1}^{\infty}(1-2^{-j})
=0.288788095\ldots.
\]
Then
\[
\lambda_{\mathrm{aff}}(d,1)\longrightarrow q.
\]

## Proof

Write \(r=d+c\). For fixed \(c\ge0\),
\[
2^{d-r}
\prod_{i=0}^{d-1}
\frac{2^r-2^i}{2^r-1}
\longrightarrow
2^{-c}\prod_{j=c+1}^\infty(1-2^{-j}).
\]
For \(c=0\), this is \(q\). For \(c=1\), it is also
\[
\frac12\prod_{j=2}^\infty(1-2^{-j})=q.
\]
For \(c\ge2\), the whole expression is at most \(2^{-c}\le1/4<q\). Hence the supremum tends to \(q\).
\(\square\)

Thus affine subspaces are asymptotically far from extremal:
\[
0.288788095\ldots
<
e^{-1}=0.367879441\ldots.
\]

For orientation, the affine construction with \(r=d\) gives
\[
\begin{array}{c|c}
d&\text{value}\\ \hline
2&2/3\\
3&24/49\\
4&1344/3375\\
5&322560/923521
\end{array}
\]
and thereafter converges downward toward \(q\). It beats the independent random construction for some small \(d\), but not asymptotically.

---

# 6. What remains open

The unrestricted conjecture would follow from a theorem forcing approximately Poisson factorial moments for every near-extremal sequence. Nothing above establishes such a theorem.

The main uncovered regime consists of families that are simultaneously:

1. highly nonmonotone;
2. of total influence \(\Theta(n)\) for each fixed \(d\);
3. nonlinear, rather than affine fibers;
4. non-Poisson on random \(d\)-cubes.

In particular, the affine calculation cannot be extended merely by linearizing an arbitrary family: unions of many affine cosets can have substantially different occupancy distributions.

The precise remaining gap is the upper bound
\[
\limsup_{d\to\infty}\lambda(d,1)\le e^{-1}.
\]
The results above show that neither low-influence structure nor affine algebraic structure can furnish a counterexample, and that any sufficiently quasirandom candidate automatically has the conjectured asymptotic, but they do not rule out a genuinely nonlinear correlated construction.