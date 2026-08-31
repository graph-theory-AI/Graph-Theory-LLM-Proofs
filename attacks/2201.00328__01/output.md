```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The question remains open for genuinely small epsilon, but a probabilistic construction disproves the proposed conclusion for every epsilon greater than 1/3, while monotone families satisfy a stronger bound.",
  "would_publish": false,
  "caveats": "The general case for epsilon at most 1/3 is unresolved, and speed inequalities are interpreted asymptotically."
}
```

# 1. Statement and conventions

Let \(\lambda_{\mathcal F}(n)\) denote the minimum number of bits per vertex in an implicit representation of \(\mathcal F_n\). The decoder may depend on \(n\); thus lower bounds proved below also apply to the more restrictive convention of one decoder for all \(n\).

I interpret
\[
f_{\mathcal F}(n)<2^{n^{1+\varepsilon}}
\]
as holding for all sufficiently large \(n\), as is usual for an asymptotic speed condition.

The question asks whether there is an absolute \(\varepsilon_0>0\) such that
\[
\log_2 f_{\mathcal F}(n)<n^{1+\varepsilon_0}
\quad\Longrightarrow\quad
\lambda_{\mathcal F}(n)=O(n^{2/3}\log n)
\]
for every hereditary family \(\mathcal F\).

I do not resolve this for small \(\varepsilon\). I prove two partial results:

1. The assertion is false for every \(\varepsilon>1/3\). Hence any possible threshold must satisfy \(\varepsilon_0\le 1/3\).
2. For monotone hereditary families, the conclusion holds in the much stronger form \(O(n^\varepsilon\log n)\).

The first result is the substantive part.

---

# 2. A lower-bound tradeoff

## Theorem 2.1

For every fixed
\[
\frac12<\alpha<1
\]
there is a hereditary family \(\mathcal F_\alpha\) and constants \(c,C>0\) such that, for all sufficiently large \(n\),
\[
\lambda_{\mathcal F_\alpha}(n)\ge c n^\alpha,
\]
while
\[
\log_2 f_{\mathcal F_\alpha}(m)
   \le C m^{2\alpha}\log(m+1)
\]
for every \(m\).

Consequently, for every \(\varepsilon>1/3\), there is a hereditary family satisfying
\[
f_{\mathcal F}(n)<2^{n^{1+\varepsilon}}
\]
for all sufficiently large \(n\), but admitting no implicit representation of size \(O(n^{2/3}\log n)\).

More generally, under speed \(2^{n^{1+\varepsilon}}\), this construction gives lower bounds arbitrarily close to
\[
n^{(1+\varepsilon)/2}.
\]

The proof is a modification of the standard random-sampling strategy behind pathological implicit-representation lower bounds. I include all details.

---

## 2.1. A local sparsity lemma

Fix \(\alpha\in(1/2,1)\), and put
\[
p=N^{\alpha-1}.
\]

### Lemma 2.2

There is a constant \(C=C(\alpha)\) such that a random graph
\[
G\sim G(N,p)
\]
has, with probability at least \(1/2\), the following property:
\[
e(G[X])\le C|X|^{2\alpha}
\qquad
\text{for every }X\subseteq [N]\text{ with }2\le |X|\le \sqrt N.
\tag{2.1}
\]

### Proof

Write
\[
\delta=2\alpha-1>0,
\qquad
\gamma=1-\alpha>0.
\]
Fix \(m\le\sqrt N\), and set
\[
t=\left\lceil C m^{2\alpha}\right\rceil.
\]
If \(t>\binom m2\), there is nothing to prove. Otherwise, for a fixed \(m\)-set \(X\),
\[
e(G[X])\sim\operatorname{Bin}\left(\binom m2,p\right).
\]
The standard binomial tail estimate gives
\[
\Pr(e(G[X])\ge t)
 \le \left(\frac{e\binom m2p}{t}\right)^t.
\]
Let
\[
r=\frac{N}{m^2}\ge1.
\]
Since \(p=N^{-\gamma}\),
\[
\frac{t}{e\binom m2p}
 \ge \frac{2C}{e}m^{-2\gamma}N^\gamma
 =\frac{2C}{e}r^\gamma.
\]
After taking a union bound over the at most
\[
\binom Nm\le\left(\frac{eN}{m}\right)^m=(emr)^m
\]
sets \(X\), the logarithm of the resulting bound is at most
\[
m(1+\log m+\log r)
-
C m^{2\alpha}
  \left(\log(2C/e)+\gamma\log r\right).
\tag{2.2}
\]

Because \(2\alpha-1=\delta>0\), one can choose \(C\) so large that, for every integer \(m\ge2\),
\[
C m^\delta\log(2C/e)\ge4(1+\log m)
\]
and
\[
C m^\delta\gamma\ge4.
\]
Then (2.2) is at most
\[
-3m(1+\log m+\log r).
\]
Summing this over \(m\ge2\) gives total failure probability less than \(1/2\). ∎

Call graphs satisfying (2.1) **good**.

---

## 2.2. Small collections that defeat every decoder

Fix a sufficiently large \(N\). Let
\[
L=\lfloor cN^\alpha\rfloor,
\qquad
M=2^L,
\]
where \(c>0\) is a sufficiently small absolute constant.

A decoder on \(L\)-bit labels is a Boolean function on ordered pairs of labels. There are at most
\[
2^{M^2}
\tag{2.3}
\]
such decoders.

For any fixed decoder \(D\), the number of labeled \(N\)-vertex graphs representable by \(D\) is at most
\[
M^N,
\tag{2.4}
\]
because each of the \(N\) vertices can be assigned one of \(M\) labels.

We sample graphs from \(G(N,p)\), conditioned on being good. By Lemma 2.2, the conditioning event has probability at least \(1/2\).

For any particular graph \(H\), since \(p\le1/2\),
\[
\Pr(G(N,p)=H)\le (1-p)^{\binom N2}
 \le \exp\left(-p\binom N2\right).
\]
Therefore, under the conditioned distribution,
\[
\Pr(G=H\mid G\text{ good})
 \le 2\exp\left(-p\binom N2\right).
\]
Using (2.4), for a fixed decoder \(D\),
\[
\Pr(G\text{ is representable by }D\mid G\text{ good})
 \le 2M^N\exp\left(-p\binom N2\right).
\tag{2.5}
\]

Now
\[
p\binom N2\ge \frac13N^{1+\alpha}
\]
for large \(N\), while
\[
\log M^N=NL\log2\le c(\log2)N^{1+\alpha}.
\]
Taking, for example,
\[
c<\frac{1}{12\log2},
\]
the right side of (2.5) is at most
\[
q_N:=\exp(-c_0N^{1+\alpha})
\tag{2.6}
\]
for some \(c_0>0\).

Independently sample
\[
s=\lceil M^3\rceil
\]
good graphs. For a fixed decoder, the probability that it represents all \(s\) sampled graphs is at most \(q_N^s\). By (2.3), the probability that some \(L\)-bit decoder represents all of them is at most
\[
2^{M^2}q_N^s
\le
\exp\left((\log2)M^2-c_0N^{1+\alpha}M^3\right)<1
\]
for large \(N\).

Thus there exists a collection \(\mathcal A_N\) of good \(N\)-vertex graphs such that

\[
|\mathcal A_N|\le M^3\le 2^{C_0N^\alpha},
\tag{2.7}
\]
but no decoder using \(L\) bits per vertex represents every graph in \(\mathcal A_N\).

Removing repeated graphs, or repeated isomorphism types, does not affect this conclusion.

---

## 2.3. Forming the hereditary family

For every sufficiently large \(N\), choose such a collection \(\mathcal A_N\). Define \(\mathcal F_\alpha\) to consist of all graphs isomorphic to induced subgraphs of members of
\[
\bigcup_N\mathcal A_N.
\]
This is hereditary.

Since \(\mathcal A_N\subseteq(\mathcal F_\alpha)_N\), the construction above gives
\[
\lambda_{\mathcal F_\alpha}(N)>L
 =\Omega(N^\alpha)
\]
for every sufficiently large \(N\).

It remains to bound the speed.

Fix \(m\). A graph in \((\mathcal F_\alpha)_m\) arises as an induced \(m\)-vertex subgraph of some \(G\in\mathcal A_N\), with \(N\ge m\). Split the possible \(N\)'s into two ranges.

### Range I: \(N\ge m^2\)

Here \(m\le\sqrt N\). Since every graph in \(\mathcal A_N\) is good, every such induced \(m\)-vertex graph has at most
\[
Cm^{2\alpha}
\]
edges.

The total number of labeled \(m\)-vertex graphs with at most \(Cm^{2\alpha}\) edges is at most
\[
\sum_{j\le Cm^{2\alpha}}\binom{\binom m2}{j}
 \le 2^{C_1m^{2\alpha}\log(m+1)}.
\tag{2.8}
\]
For the finitely many \(m\) where \(Cm^{2\alpha}>\binom m2/2\), the constant \(C_1\) can be enlarged.

Crucially, all \(N\ge m^2\) contribute graphs lying in the same sparse universe counted in (2.8), so there is no infinite summation over \(N\).

### Range II: \(m\le N<m^2\)

For a fixed \(N\), each graph in \(\mathcal A_N\) has at most \(N^m\) labeled induced \(m\)-vertex subgraphs. By (2.7), the number contributed at this stage is at most
\[
2^{C_0N^\alpha}N^m.
\]
Since \(N<m^2\),
\[
C_0N^\alpha+m\log_2N
 \le C_0m^{2\alpha}+2m\log_2m
 =O(m^{2\alpha}\log(m+1)),
\]
where \(\alpha>1/2\) is used in the final estimate.

There are fewer than \(m^2\) integers \(N\) in this range, which only contributes an additional \(O(\log m)\) to the logarithm.

Combining both ranges,
\[
\log_2 f_{\mathcal F_\alpha}(m)
 \le C_2m^{2\alpha}\log(m+1).
\]
This proves Theorem 2.1. ∎

---

## 2.4. Consequence for the proposed \(2/3\) exponent

Let \(\varepsilon>1/3\). Choose
\[
\frac23<\alpha<\frac{1+\varepsilon}{2}.
\]
Then
\[
2\alpha<1+\varepsilon,
\]
so Theorem 2.1 gives, for sufficiently large \(n\),
\[
\log_2 f_{\mathcal F_\alpha}(n)
 \le Cn^{2\alpha}\log n
 <n^{1+\varepsilon}.
\]
On the other hand,
\[
\lambda_{\mathcal F_\alpha}(n)\ge cn^\alpha.
\]
Since \(\alpha>2/3\),
\[
\frac{n^\alpha}{n^{2/3}\log n}\longrightarrow\infty.
\]
Thus this family has no \(O(n^{2/3}\log n)\)-bit implicit representation.

Therefore:

\[
\boxed{\text{Any affirmative threshold }\varepsilon_0\text{ must satisfy }\varepsilon_0\le\frac13.}
\]

This does not settle the catalogued question, since it explicitly asks about sufficiently small \(\varepsilon\).

---

# 3. A positive result for monotone families

The difficulty is genuinely caused by non-monotonicity.

## Proposition 3.1

Let \(\mathcal F\) be hereditary and closed under edge deletion. Suppose, for some fixed \(\varepsilon>0\),
\[
f_{\mathcal F}(n)<2^{n^{1+\varepsilon}}
\]
for all sufficiently large \(n\). Then
\[
\lambda_{\mathcal F}(n)=O(n^\varepsilon\log n).
\]
In particular, if \(\varepsilon\le2/3\), then
\[
\lambda_{\mathcal F}(n)=O(n^{2/3}\log n).
\]

The analogous statement holds if the complement family is monotone.

### Proof

Let \(G\in\mathcal F_n\), and let \(H=G[S]\) have \(k\) vertices. Because \(\mathcal F\) is closed under edge deletion, all \(2^{e(H)}\) spanning subgraphs of \(H\) lie in \(\mathcal F_k\). Hence, under labeled speed,
\[
2^{e(H)}\le f_{\mathcal F}(k),
\]
so
\[
e(H)\le k^{1+\varepsilon}
\]
for all sufficiently large \(k\). Enlarging a constant handles the finitely many smaller \(k\).

Thus every induced subgraph \(H\) has average degree
\[
\frac{2e(H)}{|H|}=O(|H|^\varepsilon).
\]
Repeatedly remove a minimum-degree vertex. Orient each edge from the vertex removed first toward the vertex removed later. This gives an orientation of \(G\) with maximum outdegree
\[
O(n^\varepsilon).
\]

Assign every vertex a unique \(O(\log n)\)-bit identifier, together with the identifiers of its out-neighbours. Two labels determine adjacency by checking whether either identifier occurs in the other vertex's list. The label length is
\[
O(n^\varepsilon\log n).
\]
For complement-monotone families, encode nonedges instead. ∎

If speed is counted up to isomorphism, the same argument has an additional \(k!\) factor:
\[
2^{e(H)}\le k!\,f_{\mathcal F}(k),
\]
which does not change the stated asymptotic bound for fixed \(\varepsilon>0\).

---

# 4. A useful sufficient structural condition

The preceding encoding extends to graphs that are sparse after comparison with a bounded template.

Suppose there are constants \(q,C\) and a symmetric matrix
\[
B\in\{0,1\}^{q\times q}
\]
such that every \(G\in\mathcal F_n\) has a coloring \(c:V(G)\to[q]\) for which the error graph
\[
E_G=\bigl\{uv:
 \mathbf 1_{uv\in E(G)}\ne B_{c(u),c(v)}
 \bigr\}
\]
satisfies
\[
e(E_G[S])\le C|S|^{5/3}
\qquad\text{for every }S\subseteq V(G).
\tag{4.1}
\]

Then \(E_G\) is \(O(n^{2/3})\)-degenerate: every induced subgraph on \(k\) vertices has average error-degree at most \(2Ck^{2/3}\). Orient its error edges with maximum outdegree \(O(n^{2/3})\). A label stores:

- the vertex identifier;
- its color in \([q]\);
- the identifiers of its outgoing error-neighbours.

The decoder first predicts adjacency using \(B\), and flips the prediction exactly when the pair is an oriented error edge. This gives labels of size
\[
O(n^{2/3}\log n).
\]

Thus a possible route to the conjecture would be to derive a bounded-template decomposition satisfying (4.1) from the speed hypothesis. I do not know how to do this, and the probabilistic construction above shows that such a deduction cannot follow from a naive global counting argument alone.

---

# 5. Remaining gap

The results leave the following interval open:

\[
0<\varepsilon\le\frac13.
\]

The random construction naturally incurs speed approximately
\[
2^{n^{2\alpha+o(1)}}
\]
when it forces labels of order \(n^\alpha\). At the critical restriction size \(m\approx\sqrt N\), the entropy \(N^\alpha\) becomes \(m^{2\alpha}\). Consequently, forcing \(\alpha>2/3\) by this method necessarily gives speed above \(2^{n^{4/3-o(1)}}\), explaining the boundary \(\varepsilon=1/3\).

Crossing this boundary would require either:

1. a substantially more structured counterexample whose intermediate induced subgraphs coalesce far more than random restrictions do, or
2. a structural theorem converting speed below \(2^{n^{4/3}}\) into a sparse-template decomposition or another efficient universal-graph construction.

Neither is established here. Thus the catalogued question remains open for sufficiently small \(\varepsilon\).