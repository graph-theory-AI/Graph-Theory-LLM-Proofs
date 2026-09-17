```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A refined construction gives speed below 2^(n^(1+epsilon)) and label complexity Theta(n^((1+epsilon)/2)), ruling out epsilon>1/3 but leaving the intended small-epsilon assertion unresolved.",
  "would_publish": false,
  "caveats": "Speed bounds are interpreted asymptotically; the general case for sufficiently small epsilon is not resolved, and no originality claim is made."
}
```

## 1. Scope of the partial result

Let \(f_{\mathcal F}(n)\) count the members of \(\mathcal F\) with vertex set \([n]\), and let \(\lambda_{\mathcal F}(n)\) be the minimum label length for \(\mathcal F_n\). For the lower bounds, the decoder is allowed to depend arbitrarily on \(n\).

The question asks whether there exists an absolute \(\varepsilon_0>0\) such that every hereditary family satisfying, eventually,
\[
f_{\mathcal F}(n)<2^{n^{1+\varepsilon_0}}
\]
has
\[
\lambda_{\mathcal F}(n)=O(n^{2/3}\log n).
\]

I do not resolve this. I obtain the following sharpened version of the probabilistic lead supplied in the question.

### Theorem 1

For every fixed \(\alpha\in(1/2,1)\), there is a hereditary family \(\mathcal F_\alpha\) such that, for all sufficiently large \(n\),
\[
\log_2 f_{\mathcal F_\alpha}(n)<n^{2\alpha},
\qquad
\lambda_{\mathcal F_\alpha}(n)=\Theta(n^\alpha).
\]
The family can additionally be taken closed under disjoint unions.

Equivalently, for each fixed \(0<\varepsilon<1\), there is a hereditary family with
\[
f_{\mathcal F}(n)<2^{n^{1+\varepsilon}}
\quad\text{and}\quad
\lambda_{\mathcal F}(n)=\Theta\!\left(n^{(1+\varepsilon)/2}\right).
\]

Compared with the supplied attempt, this removes the logarithmic factor in the speed estimate and the resulting slack in the attainable label exponent. The decoder-counting argument and the \(\sqrt N\) restriction scale are re-proved below, rather than assumed. A matching upper bound on the label length is also established for the constructed family.

The consequence for the original question remains:
\[
\boxed{\text{Any affirmative threshold must be at most }1/3.}
\]
This does **not** rule out a sufficiently small positive threshold.

---

## 2. Many graphs with controlled small induced subgraphs

Fix
\[
\frac12<\alpha<1,\qquad
\delta=2\alpha-1>0,\qquad
\gamma=1-\alpha>0.
\]
Throughout this section, \(\ln\) denotes the natural logarithm.

Set
\[
\eta=\frac{\ln 2}{16},
\qquad
a=\frac{\eta}{e}.
\]
For sufficiently large \(N\), define
\[
Q_N=\binom N2,\qquad
p_N=\frac{aN^{-\gamma}}{\ln N},\qquad
k_N=\lfloor p_NQ_N\rfloor.
\]
We sample uniformly from the labeled \(N\)-vertex graphs with exactly \(k_N\) edges.

For \(m\ge2\), put
\[
t(m)=\left\lceil\frac{\eta m^{2\alpha}}{\ln m}\right\rceil.
\]

### Lemma 2

There is an integer \(m_0=m_0(\alpha)\) such that, for every sufficiently large \(N\), at least half of the \(k_N\)-edge graphs satisfy
\[
e(G[X])\le t(|X|)
\quad\text{whenever}\quad
m_0\le |X|\le\sqrt N.
\tag{2.1}
\]

#### Proof

Because \(\delta>0\), choose \(m_0\ge2\) so that, for every integer \(m\ge m_0\),
\[
\frac{\eta m^\delta}{\ln m}\ge4(1+\ln m),
\qquad
\frac{\eta\gamma m^\delta}{\ln m}\ge4.
\tag{2.2}
\]

Fix \(m_0\le m\le\sqrt N\), an \(m\)-set \(X\), and write \(t=t(m)\). If \(t>\binom m2\), the event \(e(G[X])\ge t\) is impossible. Otherwise, a union bound over prescribed sets of \(t\) edges gives
\[
\Pr(e(G[X])\ge t)
 \le \binom{\binom m2}{t}
       \left(\frac{k_N}{Q_N}\right)^t
 \le \left(\frac{e\binom m2p_N}{t}\right)^t.
\tag{2.3}
\]
Here a prescribed collection of \(t\) edges is present with probability at most \((k_N/Q_N)^t\).

Put
\[
r=\frac{N}{m^2}\ge1.
\]
Then
\[
\begin{aligned}
\frac{t}{e\binom m2p_N}
&\ge
 \frac{2\eta}{ea}\,
 N^\gamma m^{-2\gamma}\frac{\ln N}{\ln m}\\
&\ge 4r^\gamma,
\end{aligned}
\tag{2.4}
\]
using \(a=\eta/e\) and \(\ln N\ge2\ln m\).

The union bound over all \(m\)-sets therefore has natural logarithm at most
\[
m(1+\ln m+\ln r)-t(\ln4+\gamma\ln r).
\]
By (2.2), this is at most
\[
-3m(1+\ln m+\ln r).
\]
Consequently, the probability that any of the inequalities in (2.1) fails is at most
\[
\sum_{m=m_0}^{\lfloor\sqrt N\rfloor}
   \exp\bigl(-3m(1+\ln m)\bigr)
<\frac12.
\]
In fact the argument bounds the probability of the stronger bad event \(e(G[X])\ge t(|X|)\). ∎

Call these graphs **good**, and let \(\mathcal U_N\) be the set of good \(k_N\)-edge graphs.

### Lemma 3

There is a constant \(b=b(\alpha)>0\) such that, for all sufficiently large \(N\),
\[
|\mathcal U_N|\ge 2^{bN^{1+\alpha}}.
\tag{2.5}
\]

#### Proof

Lemma 2 gives
\[
|\mathcal U_N|\ge\frac12\binom{Q_N}{k_N}.
\]
For sufficiently large \(N\),
\[
k_N\ge \frac{a}{4}\frac{N^{1+\alpha}}{\ln N},
\qquad
\frac{Q_N}{k_N}\ge\frac1{p_N}\ge N^\gamma.
\]
Using \(\binom Qk\ge(Q/k)^k\), we obtain
\[
\begin{aligned}
\log_2|\mathcal U_N|
&\ge k_N\log_2(Q_N/k_N)-1\\
&\ge \frac{a\gamma}{4\ln2}N^{1+\alpha}-1.
\end{aligned}
\]
Thus, for example,
\[
b=\frac{a\gamma}{8\ln2}
\]
works for all sufficiently large \(N\). ∎

The factor \(1/\ln N\) in the edge density is important: the number of base graphs still has logarithm of order \(N^{1+\alpha}\), while the logarithm in the later sparse-graph count is canceled.

---

## 3. Small collections defeating every short-label decoder

Choose
\[
c=\min\{b/4,\,1/16\}.
\]
For a sufficiently large \(N\), let
\[
L=\lfloor cN^\alpha\rfloor,\qquad
M=2^L.
\]

There are at most
\[
2^{M^2}
\tag{3.1}
\]
Boolean decoders on ordered pairs of \(L\)-bit labels. Counting ordered-pair decoders also covers the usual symmetric-decoder convention.

For a fixed decoder \(D\), at most
\[
M^N
\tag{3.2}
\]
labeled \(N\)-vertex graphs are representable: every assignment of one of the \(M\) labels to each vertex determines at most one graph. Injectivity of the labeling is not assumed.

A uniformly sampled graph from \(\mathcal U_N\) is therefore representable by \(D\) with probability at most
\[
\frac{M^N}{|\mathcal U_N|}
\le
2^{-(b-c)N^{1+\alpha}}
\le
2^{-(b/2)N^{1+\alpha}}.
\tag{3.3}
\]

Independently sample
\[
s=M^2
\]
graphs from \(\mathcal U_N\). The probability that some \(L\)-bit decoder represents all of them is at most
\[
2^{M^2}
\left(2^{-(b/2)N^{1+\alpha}}\right)^s
=
2^{M^2(1-(b/2)N^{1+\alpha})}
<1
\]
for sufficiently large \(N\).

Hence there exists a collection \(\mathcal A_N\subseteq\mathcal U_N\) such that
\[
|\mathcal A_N|\le 2^{2cN^\alpha},
\tag{3.4}
\]
but no decoder using \(L\) bits per vertex represents all members of \(\mathcal A_N\). Repeated samples can simply be removed.

---

## 4. Hereditary closure and its speed

For every integer \(N\ge N_0\), choose such a collection \(\mathcal A_N\), where \(N_0\) is large enough for all preceding estimates. Define \(\mathcal F_\alpha\) to consist of all graphs isomorphic to induced subgraphs of members of
\[
\bigcup_{N\ge N_0}\mathcal A_N.
\]

This family is hereditary. Since \(\mathcal A_N\subseteq(\mathcal F_\alpha)_N\), the construction gives
\[
\lambda_{\mathcal F_\alpha}(N)>
\lfloor cN^\alpha\rfloor,
\]
and thus
\[
\lambda_{\mathcal F_\alpha}(N)=\Omega(N^\alpha)
\tag{4.1}
\]
for every sufficiently large \(N\).

We now bound the speed. Fix a sufficiently large \(m\). A member of \((\mathcal F_\alpha)_m\) comes from a generator of some order \(N\ge m\). Split the generators into two ranges.

### Range I: \(N\ge m^2\)

Here \(m\le\sqrt N\), so every contributed graph has at most \(t(m)\) edges.

The number of labeled \(m\)-vertex graphs with at most \(t(m)\) edges is at most
\[
\sum_{j=0}^{t(m)}\binom{\binom m2}{j}
\le (t(m)+1)m^{2t(m)}.
\]
Consequently, its base-two logarithm is at most
\[
\begin{aligned}
\log_2(t(m)+1)+2t(m)\log_2m
&=\left(\frac{2\eta}{\ln2}+o(1)\right)m^{2\alpha}\\
&=\left(\frac18+o(1)\right)m^{2\alpha}.
\end{aligned}
\tag{4.2}
\]

All infinitely many values \(N\ge m^2\) contribute graphs in this **same** sparse universe; no infinite summation is needed.

### Range II: \(m\le N<m^2\)

For a fixed \(N\), one generator has at most \(N^m\) labeled induced \(m\)-vertex subgraphs. By (3.4), the total contribution of this range is at most
\[
m^2\,2^{2cm^{2\alpha}}m^{2m}.
\]
Its base-two logarithm is at most
\[
2cm^{2\alpha}+2m\log_2m+2\log_2m
=
(2c+o(1))m^{2\alpha}.
\tag{4.3}
\]
Here \(m\log m=o(m^{2\alpha})\) because \(2\alpha>1\). Since \(c\le1/16\), the leading coefficient in (4.3) is at most \(1/8\).

Combining (4.2) and (4.3),
\[
\log_2 f_{\mathcal F_\alpha}(m)
\le
\left(\frac18+o(1)\right)m^{2\alpha}
<m^{2\alpha}
\tag{4.4}
\]
for sufficiently large \(m\).

This proves the asserted speed bound without a logarithmic loss.

---

## 5. Matching upper bound for the constructed family

The same local condition also gives
\[
\lambda_{\mathcal F_\alpha}(n)=O(n^\alpha).
\]

### Lemma 4

There is a constant \(C=C(\alpha)\) such that every \(H\in(\mathcal F_\alpha)_m\), \(m\ge2\), satisfies
\[
e(H)\le C\frac{m^{1+\alpha}}{\ln(m+1)}.
\tag{5.1}
\]

#### Proof

Suppose \(H\) is induced in a generator \(G\in\mathcal A_N\). Put
\[
k=\lfloor\sqrt N\rfloor,
\]
and increase \(N_0\), if needed, so that \(k\ge m_0\).

If \(m_0\le m\le k\), goodness gives
\[
e(H)\le t(m)
=O\!\left(\frac{m^{2\alpha}}{\ln m}\right)
=O\!\left(\frac{m^{1+\alpha}}{\ln m}\right).
\]

If \(m>k\), every induced \(k\)-vertex subgraph of \(H\) has at most \(t(k)\) edges. Averaging over its \(k\)-subsets gives
\[
e(H)\le
\frac{\binom m2}{\binom k2}t(k)
=
O\!\left(\frac{m^2N^{\alpha-1}}{\ln N}\right).
\]
Since \(m\le N\) and \(\alpha-1<0\),
\[
\frac{m^2N^{\alpha-1}}{\ln N}
\le
\frac{m^{1+\alpha}}{\ln m}.
\]
The finitely many sizes \(m<m_0\) are absorbed by enlarging \(C\). ∎

Because \(\mathcal F_\alpha\) is hereditary, (5.1) applies to every induced subgraph of every member. Successively removing a minimum-degree vertex therefore gives an orientation of each \(n\)-vertex member with maximum outdegree
\[
O\!\left(\frac{n^\alpha}{\ln n}\right).
\tag{5.2}
\]
We use here that \(x^\alpha/\ln(x+1)\) is eventually increasing; bounded smaller orders do not affect the estimate.

An orientation of maximum outdegree \(D\) gives labels of size \(O((D+1)\log n)\): store a unique vertex identifier and the identifiers of all outgoing neighbors. Two labels determine adjacency by testing whether either identifier appears in the other label’s outgoing list.

Applying (5.2) gives \(O(n^\alpha)\)-bit labels. Together with (4.1),
\[
\lambda_{\mathcal F_\alpha}(n)=\Theta(n^\alpha).
\]

### Closure under disjoint unions

If desired, replace \(\mathcal F_\alpha\) by its closure \(\mathcal F_\alpha^\oplus\) under finite disjoint unions. This remains hereditary.

By (4.4), there is a constant \(C_0\) such that, for every positive integer \(k\),
\[
\log_2 f_{\mathcal F_\alpha}(k)
\le \frac14 k^{2\alpha}+C_0k.
\]
Counting partitions of \([n]\) into blocks, and using
\(\sum_i |B_i|^{2\alpha}\le n^{2\alpha}\), gives
\[
\log_2 f_{\mathcal F_\alpha^\oplus}(n)
\le n\log_2n+\frac14 n^{2\alpha}+C_0n
<n^{2\alpha}
\]
eventually.

For labels, store a block identifier together with the label for the graph on that block. This still costs \(O(n^\alpha)\) bits. The lower bound survives because the original family is contained in the enlarged one. This completes Theorem 1.

---

## 6. Consequences for the \(2/3\) exponent

Let \(0<\varepsilon<1\), and take
\[
\alpha=\frac{1+\varepsilon}{2}.
\]
Theorem 1 gives
\[
f_{\mathcal F}(n)<2^{n^{1+\varepsilon}},
\qquad
\lambda_{\mathcal F}(n)
=\Theta\!\left(n^{(1+\varepsilon)/2}\right).
\]

If \(\varepsilon>1/3\), then
\[
\frac{n^{(1+\varepsilon)/2}}{n^{2/3}\log n}
=
\frac{n^{(3\varepsilon-1)/6}}{\log n}
\longrightarrow\infty.
\]
Thus the proposed conclusion is false for every fixed \(\varepsilon\in(1/3,1)\). It is also false for larger \(\varepsilon\), by using a counterexample for any smaller parameter in \((1/3,1)\).

More generally, under the speed bound \(2^{n^{1+\varepsilon}}\), no universal bound
\[
O(n^\beta(\log n)^K)
\]
can hold when
\[
\beta<\frac{1+\varepsilon}{2},
\]
for any fixed \(K\).

At the boundary \(\varepsilon=1/3\), however, the constructed family has label complexity \(\Theta(n^{2/3})\), so it satisfies the requested upper bound. For smaller \(\varepsilon\), its label exponent is smaller still.

---

## 7. A positive special case: edge-deletion closure

The positive statement from the supplied attempt is also valid.

### Proposition 5

Suppose \(\mathcal F\) is hereditary and closed under edge deletion, and eventually
\[
f_{\mathcal F}(n)<2^{n^{1+\varepsilon}}
\]
for a fixed \(\varepsilon>0\). Then
\[
\lambda_{\mathcal F}(n)=O(n^\varepsilon\log n).
\]
The same holds if the complement family is closed under edge deletion.

#### Proof

For \(H\in\mathcal F_k\), every spanning subgraph of \(H\) belongs to \(\mathcal F_k\). Hence
\[
2^{e(H)}\le f_{\mathcal F}(k).
\]
After enlarging a constant to handle bounded \(k\), this gives
\[
e(H)\le Ck^{1+\varepsilon}.
\]
By heredity, every induced subgraph of an \(n\)-vertex member has average degree at most \(2Cn^\varepsilon\). Greedy deletion gives an orientation with maximum outdegree \(O(n^\varepsilon)\), and the outgoing-neighbor encoding gives the claimed label length.

For a complement-monotone family, encode nonedges and invert the answer. ∎

Thus the desired conclusion holds in this special case whenever \(\varepsilon\le2/3\).

If speed is instead counted up to isomorphism, the proof uses
\[
2^{e(H)}\le k!\,f_{\mathcal F}(k);
\]
the additional \(O(k\log k)\) term is absorbed by \(O(k^{1+\varepsilon})\). The lower-bound construction already satisfies the stronger labeled-speed bound.

---

## 8. Remaining gap

The general assertion for sufficiently small fixed \(\varepsilon>0\) is not established.

The construction proves the precise attainable relation
\[
\text{speed exponent }2\alpha
\quad\longleftrightarrow\quad
\text{label exponent }\alpha,
\]
but supplies no implication in the opposite direction. Its improvement over the supplied attempt is in the sharp speed estimate and matching label upper bound—not in lowering the obstruction threshold below \(1/3\).

In particular, nothing here proves either:

- the requested upper bound for arbitrary hereditary families with \(0<\varepsilon\le1/3\); or
- a counterexample to that upper bound in this range.

Accordingly, this is a rigorous partial result, not a resolution of the catalogued problem.