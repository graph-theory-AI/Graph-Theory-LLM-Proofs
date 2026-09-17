```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A randomly sparsified directed-triangle blow-up gives the necessary bound f(k) >= (68/441)k^2 - O(k^(3/2)sqrt(log k)), improving the supplied obstruction constant.",
  "would_publish": false,
  "caveats": "This is only a lower bound, not a proof that f(k) exists; the constant is not claimed optimal, and novelty has not been checked."
}
```

## 1. Partial result

I do not resolve Mader’s conjecture. I obtain a stronger asymptotic obstruction than the one in the supplied attempt, using a different construction.

All digraphs below are finite and simple. A subdivision has distinct branch vertices, and its replacement directed paths are internally vertex-disjoint and avoid all branch vertices internally. Write
\[
\delta^0(D)=\min\{\delta^+(D),\delta^-(D)\}.
\]

### Theorem
For every sufficiently large integer \(k\), there is an **oriented graph** \(D_k\) containing no subdivision of \(TT_k\) and satisfying
\[
\boxed{\displaystyle
\delta^0(D_k)\ge
\frac{68}{441}k^2-O\!\left(k^{3/2}\sqrt{\log k}\right).
}
\]
Consequently, every forcing function in the conjecture must satisfy
\[
\boxed{\displaystyle
f(k)\ge
\frac{68}{441}k^2-O\!\left(k^{3/2}\sqrt{\log k}\right).
}
\]

Here
\[
\frac{68}{441}=0.154195011\ldots
>
\frac{19}{128}=0.1484375.
\]
The comparison is with the leading constant in the supplied attempt, not with a verified best bound in the literature. I do not rely on that attempt’s four-cycle optimization; all counting needed here is proved below.

The construction starts with three independent classes whose possible arcs run cyclically between the classes, and then deletes each possible arc with probability \(4/21\). The useful feature is that a deleted forward arc cannot be replaced by a two-edge path: any replacement needs at least four edges.

## 2. A deterministic capacity lemma

Let \(D\) have three vertex classes
\[
V_0,V_1,V_2,\qquad |V_i|=t,
\]
with arcs allowed only from \(V_i\) to \(V_{i+1}\), indices modulo \(3\). Not all allowed arcs need be present.

Suppose \(D\) contains a subdivision of \(TT_k\), with branch vertices ordered according to the transitive tournament. Let
\[
n_i=\text{number of branch vertices in }V_i,\qquad
n_0+n_1+n_2=k.
\]
Put
\[
Q=n_0^2+n_1^2+n_2^2,\qquad
R=n_0^3+n_1^3+n_2^3,
\]
and
\[
C=n_0n_1+n_1n_2+n_2n_0.
\]

Classify the tournament arcs whose ends lie in different classes as follows:

- **Forward:** their direction agrees with the cyclic class orientation.
- **Backward:** their direction opposes it.

Let \(F\) and \(X\) be their respective numbers, so
\[
F+X=C.
\]
Let \(M\) be the number of forward tournament arcs for which the corresponding direct arc is absent from \(D\).

### Lemma
If
\[
M\ge \frac{4}{21}F-u,
\]
then
\[
\boxed{\displaystyle t\ge \frac{4}{21}k^2-u.} \tag{1}
\]

### Proof

Let \(\ell_i\) denote the number of vertices of the subdivision in \(V_i\), including branch vertices.

Every directed path advances cyclically through the classes. Therefore:

1. A path between distinct vertices in the same class has at least one internal vertex in each other class.
2. A backward cross-class path has an internal vertex in the third class.
3. A forward cross-class path whose direct arc is absent has length at least four, and thus has at least one internal vertex in **every** class.

Let \(X_i\) count backward tournament arcs whose ends lie in the other two classes, so their replacement paths must pass internally through \(V_i\). Then \(X=\sum_i X_i\). Internal vertex-disjointness gives, for each \(i\),
\[
\ell_i\ge
n_i+\sum_{j\ne i}\binom{n_j}{2}+X_i+M. \tag{2}
\]

#### Unweighted occupancy

Summing (2),
\[
3t\ge \sum_i\ell_i
\ge k+2\sum_i\binom{n_i}{2}+X+3M
=Q+X+3M.
\]
Hence
\[
t\ge \frac{Q+X}{3}+M. \tag{3}
\]

#### Weighted occupancy

Choose one branch vertex from each class. Among the three tournament arcs on these vertices, at least one is backward: otherwise they would form a directed triangle, impossible in a transitive tournament.

Counting all such triples gives
\[
\sum_i n_iX_i\ge n_0n_1n_2. \tag{4}
\]
This remains valid when a class contains no branch vertices.

Multiply (2) by \(n_i\), sum, and use (4):
\[
kt\ge \sum_i n_i\ell_i
\ge
Q+\sum_i\binom{n_i}{2}(k-n_i)+n_0n_1n_2+kM.
\]
The terms preceding \(kM\) simplify to
\[
\frac{k^3-R}{6}+\frac{3Q-k^2}{2}.
\]
Since \(Q\ge k^2/3\), we obtain
\[
t\ge \frac{k^3-R}{6k}+M. \tag{5}
\]

#### Combining the inequalities

Take \(3/7\) of (5) and \(4/7\) of (3):
\[
t\ge
\frac{k^2}{14}-\frac{R}{14k}
+\frac{4}{21}(Q+X)+M.
\]
Using \(M\ge (4/21)(C-X)-u\), the terms involving \(X\) cancel:
\[
t\ge
\frac{k^2}{14}-\frac{R}{14k}
+\frac{4}{21}(Q+C)-u.
\]
Because \(k^2=Q+2C\), this is
\[
t\ge
\frac{k^2}{6}+\frac{2Q}{21}-\frac{R}{14k}-u.
\]
A further elementary identity gives
\[
\frac{k^2}{6}+\frac{2Q}{21}-\frac{R}{14k}
=
\frac{4}{21}k^2+
\frac{kC-9n_0n_1n_2}{42k}.
\]
Finally,
\[
(n_0+n_1+n_2)(n_0n_1+n_1n_2+n_2n_0)
\ge 9n_0n_1n_2
\]
by AM–GM. Thus the last fraction is nonnegative, proving (1). \(\square\)

## 3. Random sparsification

Set
\[
q=\frac4{21},\qquad p=1-q=\frac{17}{21},
\]
and, with natural logarithms, define
\[
u=k^{3/2}\sqrt{\log k},
\qquad
t=\left\lceil qk^2-u\right\rceil-1.
\]
For sufficiently large \(k\), \(t\ge1\), and
\[
t<qk^2-u,\qquad
3t<3qk^2=\frac47k^2<k^2. \tag{6}
\]
For example, \(k\ge256\) suffices for these elementary inequalities.

Take three classes of size \(t\). Independently retain each possible arc from \(V_i\) to \(V_{i+1}\) with probability \(p\). The resulting graph is oriented.

We prove that with positive probability it simultaneously has:

- sufficiently many missing forward arcs for **every** ordered \(k\)-tuple of distinct vertices;
- large minimum outdegree and indegree.

### 3.1. Uniformly many missing forward arcs

Fix an ordered \(k\)-tuple of distinct vertices. Its class labels determine a set of \(F\) possible forward arcs. The number \(M\) of these arcs that are absent is binomial with mean \(qF\).

For \(F>0\), Hoeffding’s inequality gives
\[
\Pr(M<qF-u)
\le
\exp\!\left(-\frac{2u^2}{F}\right).
\]
Since \(F\le \binom{k}{2}<k^2/2\),
\[
\Pr(M<qF-u)
\le \exp(-4k\log k)=k^{-4k}. \tag{7}
\]
For \(F=0\), the desired inequality holds automatically.

There are at most
\[
(3t)^k\le k^{2k}
\]
ordered \(k\)-tuples. Thus, by the union bound,
\[
\Pr\bigl(\exists\text{ ordered \(k\)-tuple with }M<qF-u\bigr)
\le k^{-2k}. \tag{8}
\]

Consequently, except with probability at most \(k^{-2k}\), the hypothesis of the capacity lemma holds for every possible ordered set of branch vertices.

### 3.2. Minimum degrees

Every vertex has both its outdegree and indegree distributed as \(\operatorname{Bin}(t,p)\). Put
\[
v=\sqrt{2t\log k}.
\]
For each of these degree variables, Hoeffding’s inequality gives
\[
\Pr\bigl(\deg<pt-v\bigr)
\le \exp(-2v^2/t)=k^{-4}.
\]
There are \(6t<2k^2\) variables to check. Hence
\[
\Pr\bigl(\delta^0(D)<pt-v\bigr)\le 2k^{-2}. \tag{9}
\]

Combining (8) and (9), the probability that either desired property fails is at most
\[
k^{-2k}+2k^{-2}<1.
\]
Therefore a realization satisfying both properties exists.

### 3.3. Excluding the subdivision

Suppose such a realization contained a \(TT_k\)-subdivision. Order its branch vertices according to the transitive tournament. The uniform missing-arc property and the capacity lemma would imply
\[
t\ge qk^2-u,
\]
contradicting the strict inequality in (6).

Thus this realization contains no \(TT_k\)-subdivision.

Its minimum semidegree satisfies
\[
\begin{aligned}
\delta^0(D)
&\ge pt-\sqrt{2t\log k}\\
&\ge
pqk^2-pu-p-\sqrt{2q}\,k\sqrt{\log k}\\
&=
\frac{68}{441}k^2
-\frac{17}{21}k^{3/2}\sqrt{\log k}
-\sqrt{\frac8{21}}\,k\sqrt{\log k}
-\frac{17}{21}.
\end{aligned}
\]
This proves the theorem.

## 4. Consequence and the remaining gap

If a universal forcing threshold \(f(k)\) exists, the constructed graph gives
\[
f(k)>\delta^+(D_k),
\]
and hence the stated necessary quadratic lower bound.

This is an obstruction to **small thresholds**, not to the existence of a threshold. The construction lets \(k\) tend to infinity; it does not give arbitrarily large minimum outdegree while keeping \(k\) fixed.

In particular:

- no universal upper bound for arbitrary digraphs is obtained;
- the existence of \(f(5)\) is not established;
- the constant \(68/441\) is not claimed optimal;
- no novelty claim or literature-wide comparison is being made.

The precise progress is the self-contained sparsification construction and its asymptotically stronger lower-bound coefficient.