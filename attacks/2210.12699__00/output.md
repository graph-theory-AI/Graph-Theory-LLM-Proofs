```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A self-contained random regular-tournament construction improves the obstruction to s/2-d(s)=Omega(sqrt(s)), determining the polynomial exponent but leaving a sqrt(log s) factor.",
  "would_publish": false,
  "caveats": "The logarithmic factor in the upper bound remains, and possible overlap with the unverified 2024 follow-up has not been checked."
}
```

# Statement of the partial result

Write \(D[X]\) for the subdigraph induced by \(X\). Since deleting arcs cannot increase minimum outdegree, it is enough to consider induced subdigraphs.

I prove the following.

**Theorem.** There is an absolute constant \(c>0\) such that, for every sufficiently large integer \(s\),
\[
d(s)\le \frac{s}{2}-c\sqrt{s}.
\]
Consequently,
\[
c\sqrt{s}\le \frac{s}{2}-d(s)\le C\sqrt{s\log s}
\]
for suitable absolute constants \(c,C>0\).

Thus the polynomial order is determined:
\[
\frac{s}{2}-d(s)=s^{1/2+o(1)}.
\]
This does not determine the remaining factor between \(1\) and \(\sqrt{\log s}\).

The construction is a near-regular tournament obtained by deleting one vertex from a suitably chosen regular tournament.

# 1. An atom bound for tournament degree sequences

Let \(T_k\) be a uniformly random labeled tournament on \(k\) vertices, and define
\[
M_k=\max_{\mathbf a\in\mathbb Z^k}
 \Pr\bigl((d^+_{T_k}(1),\dots,d^+_{T_k}(k))=\mathbf a\bigr).
\]

## Lemma 1

There is an absolute constant \(A\) such that
\[
M_k\le A^k k^{-(k-1)/2}
\qquad(k\ge 1).
\]

### Proof

Let
\[
\beta_m=\max_r 2^{-m}\binom mr.
\]
The usual central-binomial estimate gives
\[
\beta_m\le Bm^{-1/2}
\]
for an absolute constant \(B\).

Partition the \(k\) vertices into sets \(U,W\) of sizes
\[
a=\lfloor k/2\rfloor,\qquad b=\lceil k/2\rceil.
\]
Fix a target degree vector and expose first all edges inside \(U\).

For each \(u\in U\), the number of edges directed from \(u\) to \(W\) is distributed as \(\operatorname{Bin}(b,1/2)\). These \(a\) random variables are independent, because they involve disjoint sets of cross-edges. Hence the probability that all vertices of \(U\) receive their prescribed total degrees is at most \(\beta_b^a\).

After the cross-edges have been exposed, the required internal degrees of the vertices in \(W\) form some prescribed vector. The probability that the random tournament on \(W\) realizes that vector is at most \(M_b\). Therefore
\[
M_k\le \beta_b^a M_b.
\]

Inductively, if \(M_b\le A^b b^{-(b-1)/2}\), then
\[
M_k
 \le B^aA^b b^{-(k-1)/2}.
\]
Since \(b\ge k/2\) and
\[
\left(\frac{k}{b}\right)^{(k-1)/2}\le 2^a,
\]
choosing \(A\ge 2B\), and increasing it to cover the initial cases, gives
\[
M_k\le A^k k^{-(k-1)/2}.
\]
\(\square\)

## Corollary 2

There is an absolute constant \(A_0\) such that, for all \(k\ge2\) and \(t\ge0\),
\[
\Pr\left(
 \delta^+(T_k)\ge \frac{k-1}{2}-t
\right)
\le
A_0^k
\left(\frac{t+1}{\sqrt{k}}\right)^{k-1}.
\]

### Proof

Put
\[
h=\left\lceil \frac{k-1}{2}-t\right\rceil.
\]
If every degree is at least \(h\), write
\[
d_i=h+z_i,\qquad z_i\ge0.
\]
Since every tournament has total outdegree \(\binom{k}{2}\),
\[
\sum_i z_i=\binom{k}{2}-kh\le kt.
\]
For any fixed value of this sum, the number of possible ordered vectors
\((z_1,\dots,z_k)\) is at most
\[
\binom{kt+k-1}{k-1}\le \bigl(C(t+1)\bigr)^{k-1}
\]
for an absolute constant \(C\). Lemma 1 bounds the probability of each degree vector by
\[
A^k k^{-(k-1)/2}.
\]
Multiplying the two estimates proves the result. \(\square\)

# 2. Regular tournaments are not too rare

A regular tournament on \(2n+1\) vertices has every outdegree equal to \(n\).

## Lemma 3

If a uniformly random tournament on \(N=2n+1\) vertices is regular with probability \(p_n\), then
\[
p_n\ge
2\left(\frac{\binom{2n}{n}}{4^n}\right)^{2n+1}.
\]
In particular, for an absolute \(c_0>0\),
\[
p_n\ge \left(\frac{c_0}{\sqrt n}\right)^{2n+1}.
\]

### Proof

This is a transition-system count.

At every vertex of \(K_{2n+1}\), pair its \(2n\) incident edges into \(n\) unordered pairs. There are
\[
(2n-1)!!
\]
possible pairings at each vertex. A choice of pairings at all vertices decomposes the edges into one or more edge-disjoint closed circuits. Orienting each circuit in either direction produces an Eulerian orientation of \(K_{2n+1}\), hence a regular tournament. If the transition system has \(q\) circuits, it gives \(2^q\ge2\) compatible regular orientations.

Conversely, fix a regular orientation. At each vertex there are \(n\) incoming and \(n\) outgoing edges. A compatible transition pairing must match every incoming edge to an outgoing edge, and hence there are exactly \(n!\) compatible pairings at each vertex.

If \(R_N\) denotes the number of regular tournaments, double-counting compatible pairs gives
\[
R_N(n!)^N
 =\sum_{\mathcal P}2^{q(\mathcal P)}
 \ge 2\bigl((2n-1)!!\bigr)^N.
\]
Since the total number of tournaments is \(2^{\binom N2}=2^{nN}\),
\[
p_n
\ge
2\left(\frac{(2n-1)!!}{n!\,2^n}\right)^N
=
2\left(\frac{\binom{2n}{n}}{4^n}\right)^N.
\]
The final bound follows from the standard estimate
\[
\binom{2n}{n}\ge c\,\frac{4^n}{\sqrt n}.
\]
\(\square\)

# 3. Half-sized subtournaments of a random regular tournament

## Proposition 4

There is an absolute \(\eta>0\) such that, for every sufficiently large \(n\), there is a regular tournament \(R\) on \(2n+1\) vertices satisfying
\[
\delta^+(R[X])
<
\frac{n-1}{2}-\eta\sqrt n
\]
for every \(X\subseteq V(R)\) with \(|X|=n\).

### Proof

Start with an unconditioned uniformly random tournament \(\mathbf T\) on
\[
N=2n+1
\]
vertices. Let \(\mathcal E\) be the event that \(\mathbf T\) is regular.

Fix an \(n\)-set \(X\), and let \(Y=V(\mathbf T)\setminus X\), so \(|Y|=n+1\). Fix an orientation \(H\) of the edges inside \(X\).

We first bound the probability that \(H\) can be completed to a regular tournament.

For each \(x\in X\), regularity requires exactly
\[
n-d_H^+(x)
\]
outgoing cross-edges from \(x\) to \(Y\). The cross-edge counts belonging to distinct vertices of \(X\) are independent \(\operatorname{Bin}(n+1,1/2)\) variables. Hence the probability that all these \(n\) row conditions hold is at most
\[
\beta_{n+1}^n\le C^n n^{-n/2}.
\]

Once all cross-edges have been exposed, regularity prescribes an exact internal outdegree for every vertex of \(Y\). Lemma 1, applied to the random tournament on \(Y\), bounds the probability of that prescribed vector by
\[
M_{n+1}\le C^n n^{-n/2}.
\]
Thus, uniformly over all \(H\),
\[
\Pr(\mathcal E\mid \mathbf T[X]=H)
 \le C_1^n n^{-n}. \tag{1}
\]

On the other hand, Lemma 3 gives
\[
\Pr(\mathcal E)
 \ge C_2^{-n}n^{-n-1/2}. \tag{2}
\]
Dividing (1) by (2), there is an absolute \(C_3\) such that
\[
\frac{\Pr(\mathcal E\mid \mathbf T[X]=H)}
     {\Pr(\mathcal E)}
\le
C_3^n\sqrt n. \tag{3}
\]

Let \(\mathcal G_X(t)\) be the event
\[
\delta^+(\mathbf T[X])
 \ge \frac{n-1}{2}-t.
\]
Summing (3) over the possible orientations \(H\) satisfying this condition and applying Corollary 2 gives
\[
\Pr(\mathcal G_X(t)\mid\mathcal E)
\le
C_3^n\sqrt n\,
\Pr\left(
 \delta^+(T_n)\ge \frac{n-1}{2}-t
\right)
\]
and hence
\[
\Pr(\mathcal G_X(t)\mid\mathcal E)
\le
\sqrt n\,C_4^n
\left(\frac{t+1}{\sqrt n}\right)^{n-1}. \tag{4}
\]

There are at most
\[
\binom{2n+1}{n}\le 2\cdot4^n
\]
choices for \(X\). Therefore, after absorbing the factor \(4^n\) into the constant,
\[
\Pr\left(
 \exists X,\ |X|=n:\mathcal G_X(t)
 \,\middle|\,\mathcal E
\right)
\le
2\sqrt n\,C_5^n
\left(\frac{t+1}{\sqrt n}\right)^{n-1}. \tag{5}
\]

Choose an absolute \(\eta>0\) sufficiently small and put
\[
t=\eta\sqrt n.
\]
For sufficiently large \(n\),
\[
\frac{t+1}{\sqrt n}\le2\eta.
\]
Taking \(\eta\) so that \(2C_5\eta<1\), the right side of (5) tends to zero. In particular, it is less than \(1\) for all sufficiently large \(n\).

Thus there is a regular tournament for which no \(n\)-set \(X\) satisfies \(\mathcal G_X(t)\), proving the proposition. \(\square\)

# 4. Translation to \(d(s)\)

Let \(R\) be supplied by Proposition 4, and delete any vertex \(z\). The resulting tournament \(D=R-z\) has \(2n\) vertices.

Every vertex of \(R\) had outdegree \(n\). Upon deleting \(z\), vertices which sent an edge to \(z\) lose one outgoing edge, while the others do not. Hence
\[
\delta^+(D)=n-1.
\]
Set
\[
s=n-1.
\]

For every \(n\)-set \(X\subseteq V(D)\),
\[
D[X]=R[X],
\]
so Proposition 4 gives
\[
\delta^+(D[X])
<
\frac{n-1}{2}-\eta\sqrt n
=
\frac{s}{2}-\eta\sqrt{s+1}.
\]
Thus this particular \(2n\)-vertex digraph witnesses
\[
d(s)
<
\frac{s}{2}-\eta\sqrt{s+1}.
\]
After decreasing the constant, for every sufficiently large \(s\),
\[
\boxed{\frac{s}{2}-d(s)\ge c\sqrt s}.
\]

# What remains open

Combining this with the quoted probabilistic upper bound gives
\[
\Omega(\sqrt s)
\le
\frac{s}{2}-d(s)
\le
O(\sqrt{s\log s}).
\]
Thus the exponent \(1/2\) is fixed, but the factor of at most \(\sqrt{\log s}\) remains unresolved.

The catalog mentions an inaccessible 2024 paper titled *New results on a problem of Alon*. I have not verified whether the \(\Omega(\sqrt s)\) construction above, or a stronger result, already appears there; no novelty claim is made.