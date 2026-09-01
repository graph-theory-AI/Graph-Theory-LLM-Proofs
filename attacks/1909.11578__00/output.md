```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A growing-uniformity hypergraph construction gives symmetric intersecting families of polynomial density on infinitely many dimensions, greatly improving the projective-plane lower bound, but it does not determine the general asymptotics.",
  "would_publish": false,
  "caveats": "The lower bound is presently only on a subsequence, the polynomial upper bound below applies only to set-derived families, and literature novelty has not been independently checked."
}
```

# Mathematical writeup

## 1. Statement of the partial result

Let \(M_k(n)\) be the maximum size of an intersecting family
\[
A\subset [k]^n
\]
whose coordinate-automorphism group acts transitively on \([n]\). All logarithms below are natural.

For fixed \(k\ge 3\), define
\[
\gamma_k
   :=\frac{\log(k-1)}{\log(k/(k-1))}.
\]

I prove the following.

### Theorem 1
For every fixed \(k\ge3\), there is an infinite sequence \(n_d\to\infty\) such that
\[
M_k(n_d)\ge k^{n_d}n_d^{-\gamma_k-o(1)}.
\]
Equivalently, for every \(\varepsilon>0\) and all sufficiently large \(d\),
\[
M_k(n_d)\ge \frac{k^{n_d}}{n_d^{\gamma_k+\varepsilon}}.
\]

Thus the density loss can be polynomial in \(n\), rather than \(k^{-\Theta(\sqrt n)}\). In particular,
\[
n^{-\gamma_k-o(1)}\gg k^{-\sqrt n}.
\]

The construction is set-derived: membership depends only on the set of coordinates carrying one distinguished symbol.

I also record two complementary results:

1. Every transitive set-derived construction has density at most \(n^{-c_k}\) for some \(c_k>0\), by the biased KKL sharp-threshold inequality. Hence polynomial density is the correct qualitative scale inside that subclass.
2. If “symmetric” is strengthened to invariance under the full coordinate group \(S_n\), the exact maximum is
   \[
   \sum_{j>n/2}\binom nj(k-1)^{n-j},
   \]
   which is exponentially smaller than \(k^n\).

The general coordinate-transitive vector problem remains open.

---

## 2. Lifting an intersecting set family to vectors

Let \(\Omega\) be a set of \(n\) coordinates, and let
\(\mathcal F\subset 2^\Omega\) be an intersecting family. Define
\[
A_{\mathcal F}
   :=\left\{x\in[k]^\Omega:
       \{e\in\Omega:x_e=1\}\in\mathcal F\right\}.
\]

Then:

- If \(x,y\in A_{\mathcal F}\), their symbol-\(1\) supports belong to \(\mathcal F\), hence meet in some \(e\). Thus \(x_e=y_e=1\), so \(A_{\mathcal F}\) is intersecting.
- If a transitive group on \(\Omega\) preserves \(\mathcal F\), it also preserves \(A_{\mathcal F}\).
- Under the uniform distribution on \([k]^\Omega\), the symbol-\(1\) support is a \(p\)-biased random subset of \(\Omega\), where
  \[
  p=\frac1k.
  \]
  Therefore
  \[
  \frac{|A_{\mathcal F}|}{k^n}=\mu_p(\mathcal F).
  \]

It is consequently enough to construct a transitive intersecting set family with large \(p\)-biased measure.

---

## 3. The clique-versus-independence family

Fix integers \(m>d\), and let
\[
\Omega=\binom{[m]}d.
\]
Thus elements of \(2^\Omega\) are \(d\)-uniform hypergraphs on vertex set \([m]\).

For \(H\subset\Omega\), write

\[
\omega(H)
 =\max\left\{|U|:\binom Ud\subset H\right\},
\]
the largest complete \(d\)-uniform subhypergraph, and
\[
\alpha(H)
 =\max\left\{|U|:\binom Ud\cap H=\varnothing\right\},
\]
the largest independent vertex set.

Define
\[
\mathcal F_{m,d}
   :=\{H\subset\Omega:\omega(H)>\alpha(H)\}.
\]

### Lemma 2
The family \(\mathcal F_{m,d}\) is increasing, intersecting, and invariant under a transitive group on \(\Omega\).

#### Proof

Adding hyperedges can only increase \(\omega\) and decrease \(\alpha\), so \(\mathcal F_{m,d}\) is increasing.

Let \(\overline H=\Omega\setminus H\). Then
\[
\omega(\overline H)=\alpha(H),
\qquad
\alpha(\overline H)=\omega(H).
\]
Consequently \(H\) and \(\overline H\) cannot both belong to \(\mathcal F_{m,d}\).

An increasing complement-free family is intersecting: if \(H_1,H_2\in\mathcal F_{m,d}\) were disjoint, then
\[
H_2\subset\overline{H_1}.
\]
By monotonicity, \(\overline{H_1}\in\mathcal F_{m,d}\), contradicting complement-freeness.

Finally, \(S_m\) acts transitively on \(\binom{[m]}d\) and preserves both \(\omega\) and \(\alpha\). ∎

---

## 4. Biased measure of the construction

Put
\[
p=\frac1k,\qquad q=1-p,
\]
and
\[
a=-\log q=\log\frac{k}{k-1},
\qquad
b=-\log p=\log k.
\]
Since \(k\ge3\), we have \(b>a\).

For each sufficiently large integer \(d\), set
\[
r=\lceil\sqrt d\rceil,\qquad
u=d+r,\qquad
L=\binom ud,
\qquad
\eta=\sqrt{\frac{u}{L}},
\]
and choose
\[
m=\left\lfloor
   \exp\left((1-\eta)\frac{aL}{u}\right)
  \right\rfloor.
\]
Finally let
\[
n=n_d=\binom md.
\]

Notice that \(L/u\to\infty\), indeed very rapidly, so \(\eta\to0\) and \(m\gg u\).

Let \(H\) be the \(p\)-random \(d\)-uniform hypergraph on \([m]\).

### 4.1. Typically there is no independent \(u\)-set

For a fixed \(U\in\binom{[m]}u\),
\[
\Pr(U\text{ is independent})=q^L.
\]
Hence
\[
\Pr(\alpha(H)\ge u)
   \le \binom mu q^L.
\]
Using \(\binom mu\le (em/u)^u\),
\[
\begin{aligned}
\log\left(\binom mu q^L\right)
 &\le u\log m+u-aL\\
 &\le (1-\eta)aL+u-aL\\
 &=-a\sqrt{uL}+u,
\end{aligned}
\]
which tends to \(-\infty\), since \(L/u\to\infty\). Therefore
\[
\Pr(\alpha(H)<u)=1-o(1).
\tag{1}
\]

### 4.2. Many independent candidate cliques

For \(R\in\binom{[m]}u\), let
\[
K_R=\binom Rd\subset\Omega.
\]
We seek many \(u\)-sets \(R\) for which the coordinate sets \(K_R\) are disjoint.

A greedy packing gives a family
\(\mathcal R\subset\binom{[m]}u\) with pairwise intersections smaller than \(d\) and
\[
|\mathcal R|\ge \frac{n}{L^2}.
\tag{2}
\]
Indeed, a fixed \(R\) conflicts with at most
\[
L\binom{m-d}{u-d}
\]
other \(u\)-sets: choose a shared \(d\)-subset of \(R\), then the remaining \(u-d\) vertices. Hence the greedy bound is
\[
\frac{\binom mu}
     {L\binom{m-d}{u-d}}
 =
\frac1L\cdot\frac{\binom md}{\binom ud}
 =\frac n{L^2}.
\]

Trim the packing so that
\[
J:=|\mathcal R|=\left\lfloor\frac n{L^2}\right\rfloor.
\]

For \(R\in\mathcal R\), let \(C_R\) be the event that \(R\) is a clique:
\[
C_R=\{K_R\subset H\}.
\]
The \(K_R\)'s are disjoint, so the events \(C_R\) are independent, each having probability \(p^L\). Let
\[
D=\bigcup_{R\in\mathcal R}C_R.
\]
Then
\[
\Pr(D)=1-(1-p^L)^J.
\tag{3}
\]

### 4.3. Relating \(L\) and the coordinate dimension \(n\)

Since \(m\) is enormous compared with \(d\),
\[
\log\binom md=d\log m+O(d\log d).
\]
Moreover \(L\gg d\log d\), \(d/u\to1\), and \(\eta\to0\). Thus
\[
\log n
 =d\log m+o(L)
 =(1-\eta)a\frac duL+o(L)
 =(a+o(1))L.
\tag{4}
\]

It follows from (2) and (4) that
\[
\log J=(a+o(1))L.
\tag{5}
\]
Consequently
\[
\log(Jp^L)=(a-b+o(1))L\longrightarrow-\infty.
\]
Equation (3) therefore gives
\[
\Pr(D)=(1+o(1))Jp^L.
\tag{6}
\]

### 4.4. Membership in \(\mathcal F_{m,d}\)

Both events \(D\) and \(\{\alpha(H)<u\}\) are increasing events in the hyperedge indicators. Harris's inequality for product measures, together with (1), gives
\[
\Pr\bigl(D\cap\{\alpha(H)<u\}\bigr)
 \ge \Pr(D)\Pr(\alpha(H)<u)
 =(1-o(1))\Pr(D).
\]
On this intersection, \(H\) has a clique of size at least \(u\) and an independent set of size strictly less than \(u\). Hence
\[
\omega(H)>\alpha(H),
\]
so \(H\in\mathcal F_{m,d}\). Therefore, by (5) and (6),
\[
\begin{aligned}
\log\mu_p(\mathcal F_{m,d})
 &\ge \log J+L\log p+o(L)\\
 &=-(b-a+o(1))L.
\end{aligned}
\]
Using (4),
\[
\mu_p(\mathcal F_{m,d})
 \ge n^{-(b-a)/a-o(1)}.
\]
Finally,
\[
\frac{b-a}{a}
 =\frac{\log(q/p)}{\log(1/q)}
 =\frac{\log(k-1)}{\log(k/(k-1))}
 =\gamma_k.
\]

Lifting \(\mathcal F_{m,d}\) to \([k]^n\) as in Section 2 proves Theorem 1. ∎

---

## 5. A polynomial upper bound for all set-derived constructions

Let \(\mathcal F\subset2^{[n]}\) be intersecting and invariant under a transitive coordinate group. Replacing \(\mathcal F\) by its upward closure preserves both properties and can only increase \(\mu_p(\mathcal F)\), so assume that \(\mathcal F\) is increasing.

Let
\[
f(r)=\mu_r(\mathcal F).
\]
Since \(\mathcal F\) is intersecting, at most one member of each complementary pair \(S,[n]\setminus S\) belongs to \(\mathcal F\). Thus
\[
f(1/2)\le\frac12.
\tag{7}
\]

The standard biased KKL inequality, combined with Russo's formula and transitivity, says that for fixed \(p_0>0\), there is \(c(p_0)>0\) such that, for
\(r\in[p_0,1-p_0]\),
\[
f'(r)\ge c(p_0)f(r)(1-f(r))\log n.
\tag{8}
\]
Apply this on \(r\in[1/k,1/2]\). Integrating (8),
\[
\left[
 \log\frac{f(r)}{1-f(r)}
\right]_{1/k}^{1/2}
 \ge c_k\log n
\]
for some \(c_k>0\). By (7), the upper endpoint is nonpositive, so
\[
\log\frac{f(1/k)}{1-f(1/k)}
 \le -c_k\log n.
\]
Hence
\[
\mu_{1/k}(\mathcal F)\le n^{-c_k}.
\tag{9}
\]

Thus, among transitive families obtained from the support of one distinguished symbol, the largest possible density is polynomially small, up to the unresolved value of the exponent. The construction above supplies a polynomial lower bound on an infinite sequence.

Equation (9) does not apply to an arbitrary vector family \(A\subset[k]^n\), because such a family need not be determined by a single symbol support.

---

## 6. Exact solution under full coordinate permutation symmetry

Here is a separate exactly solvable special case.

### Proposition 3
If \(A\subset[k]^n\) is intersecting and invariant under all of \(S_n\), then
\[
|A|\le
B_{n,k}:=
\sum_{j>n/2}\binom nj(k-1)^{n-j}.
\]
Equality is attained by
\[
A=\{x\in[k]^n:|\{i:x_i=1\}|>n/2\}.
\]

#### Proof

First, suppose a word \(x\) has symbol multiplicities \(c_1,\dots,c_k\), all at most \(n/2\). There is then a coordinate permutation \(\pi\) such that
\[
x_i\ne x_{\pi(i)}
\qquad\text{for every }i.
\tag{10}
\]
To see this, form a bipartite graph between two copies of the coordinate set, joining positions carrying different symbols. Hall's condition holds:

- for a set of left positions carrying one symbol \(a\), its neighborhood has size \(n-c_a\ge c_a\);
- a set containing at least two symbols has every right position as a neighbor.

Thus there is a perfect matching, proving (10).

If \(A\) is \(S_n\)-invariant and contains such an \(x\), then it also contains \(x\circ\pi\), contradicting intersection. Hence every word in \(A\) has a strict majority symbol.

There are \(kB_{n,k}\) words with a strict majority, since the majority symbol is unique. Let \(\tau\) be a \(k\)-cycle on the alphabet. Its orbits on these words have size \(k\), and any two distinct words in one orbit differ in every coordinate. An intersecting family therefore contains at most one word from each orbit. Thus
\[
|A|\le \frac{kB_{n,k}}k=B_{n,k}.
\]

The stated majority family is clearly intersecting and has size \(B_{n,k}\). ∎

For fixed \(k\ge3\),
\[
B_{n,k}
 =\Theta_k\!\left(
 n^{-1/2}(2\sqrt{k-1})^n
 \right),
\]
so its density is
\[
\Theta_k\!\left(
 n^{-1/2}
 \left(\frac{2\sqrt{k-1}}k\right)^n
 \right).
\]
Since \(2\sqrt{k-1}<k\) for \(k\ge3\), this is exponentially small.

---

## 7. Remaining gaps

The main problem is not resolved.

- The polynomial-density construction is only established for dimensions
  \[
  n_d=\binom{m_d}{d}
  \]
  arising from the chosen parameters.
- There is no matching lower bound for every \(n\).
- The KKL upper bound applies only to set-derived families. For arbitrary symmetric intersecting \(A\subset[k]^n\), the strongest conclusion used here remains the source theorem
  \[
  |A|=o(k^n).
  \]
- Even in the set-derived subclass, the exponent \(\gamma_k\) is not shown optimal.

Subject to an independent literature check, the main concrete progress is therefore the replacement of the projective-plane density \(k^{-\Theta(\sqrt n)}\) by the polynomial density
\[
n^{-\gamma_k-o(1)}
\]
on an infinite sequence of dimensions.