```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "With high probability, any orthogonal conjugation supported on at most n/2 - 3n/log n vertices that produces another graph is just a relabelling.",
  "would_publish": false,
  "caveats": "Only localized similarities are excluded; globally supported cospectral mates remain uncontrolled, and novelty is not claimed."
}
```

## 1. Formulation and partial result

Write \(G\sim G(n,1/2)\), and let \(A\) be its adjacency matrix. The conjecture asks whether
\[
\Pr(G\text{ is determined by its adjacency spectrum})\longrightarrow 1.
\]
I do not establish this limit. The result below excludes a broad class of localized cospectral constructions, allowing arbitrary real orthogonal matrices—not just particular switching formulas.

An orthogonal matrix \(U\) is **localized to \(S\subseteq[n]\)** if
\[
Ue_j=e_j\qquad(j\notin S).
\]
Orthogonality then implies that, after ordering \(S\) first,
\[
U=Q\oplus I_{[n]\setminus S}
\]
for an orthogonal matrix \(Q\).

### Theorem: rigidity of localized orthogonal similarities

Let
\[
k_n=\left\lfloor \frac n2-\frac{3n}{\log n}\right\rfloor,
\]
where logarithms are natural. There is an absolute constant \(c>0\) such that, for all sufficiently large \(n\), the following holds with probability at least
\[
1-\exp\!\left(-\frac{cn}{(\log n)^2}\right).
\]

Simultaneously for every \(S\subseteq[n]\) with \(|S|\le k_n\) and every orthogonal matrix \(U\) localized to \(S\):
\[
U^{T}AU\text{ is a graph adjacency matrix}
\quad\Longrightarrow\quad
U\text{ is a permutation matrix}.
\]

In particular, no non-isomorphic cospectral mate can arise from an orthogonal conjugation localized to at most \(k_n\) vertices.

The proof uses only the block of edges between \(S\) and its complement.

## 2. A hypercube anti-concentration lemma

Let \(X\) be uniform on \(\{0,1\}^{r}\), and put
\[
p_r=\min\left\{\frac12,\frac4{\sqrt r}\right\}.
\]

We need two elementary facts.

**Lemma 1.**

1. If \(v\in\mathbb R^r\) has all coordinates nonzero, then
   \[
   \Pr(v^TX=0)\le p_r.
   \]
2. If \(q\in\mathbb R^r\) has all coordinates nonzero, \(\|q\|_2=1\), and \(q\) is not a positive coordinate vector, then
   \[
   \Pr(q^TX\in\{0,1\})\le p_r.
   \]

**Proof.** For the first assertion, pair cube vertices differing in one coordinate whose coefficient is nonzero. At most one member of each pair can give value zero. This gives the bound \(1/2\).

For the second assertion, suppose first that \(r\ge2\). Every nonzero coordinate of \(q\) then has absolute value strictly between zero and one. Flipping that coordinate changes \(q^TX\) by a number not in \(\{-1,0,1\}\). Thus both members of a pair cannot give values in \(\{0,1\}\). If \(r=1\), the only excluded-from-the-exception unit vector is \((-1)\), for which the probability is \(1/2\).

For the other bounds, flipping coordinates with negative coefficients reduces any level-set question to positive coefficients. A level set of a positive weighted sum is an antichain of subsets of \([r]\). Hence its size is at most
\[
\binom r{\lfloor r/2\rfloor}.
\]
For completeness, this antichain bound follows by taking a uniformly random maximal chain: it meets an antichain at most once, giving
\[
\sum_{F\text{ in the antichain}}\binom r{|F|}^{-1}\le1.
\]
The elementary central-binomial estimate gives
\[
2^{-r}\binom r{\lfloor r/2\rfloor}\le \frac2{\sqrt r}.
\]
One level therefore has probability at most \(2/\sqrt r\), and two levels have probability at most \(4/\sqrt r\). Combining the bounds proves the lemma. \(\square\)

## 3. A uniform random-cut lemma

For a vector \(v\in\mathbb R^n\), let \(R=\operatorname{supp}(v)\). Only vertices outside \(R\) will be counted in the following statements.

Set
\[
k=k_n,\qquad h=n-k.
\]

### Lemma 2

With probability at least
\[
1-\exp\!\left(-\frac{cn}{(\log n)^2}\right),
\]
both of the following hold:

1. There is no nonzero vector \(v\), supported on at most \(k\) coordinates, for which
   \[
   \#\{j\notin\operatorname{supp}(v):v^TAe_j=0\}\ge h.
   \]
2. There is no unit vector \(q\), other than a positive coordinate vector, supported on at most \(k\) coordinates, for which
   \[
   \#\{j\notin\operatorname{supp}(q):q^TAe_j\in\{0,1\}\}\ge h.
   \]

The important point is uniformity over all real vectors, including vectors chosen after seeing the graph.

### Proof

Call failures of the first and second assertions \(\mathcal Z\) and \(\mathcal B\), respectively. We first show that every failure has a finite witness.

#### Witnesses for \(\mathcal Z\)

Suppose a nonzero vector annihilates the columns indexed by some set \(D\) of \(h\) vertices outside its support.

Among nonzero vectors supported within its original support and annihilating those columns, choose \(v\) with minimum support. Write
\[
R=\operatorname{supp}(v),\qquad r=|R|.
\]
The vectors
\[
A[R,j]\in\mathbb R^r,\qquad j\in D,
\]
span a space of dimension exactly \(r-1\). Indeed, their annihilator contains \(v\). If its dimension were at least two, a nonzero linear combination of two annihilators could cancel a coordinate, contradicting minimality of the support.

Consequently, some \(I\subseteq D\), with \(|I|=r-1\), determines the direction of \(v\). For fixed \(R,I\), conditioning on \(A[R,I]\) therefore determines one candidate direction, provided the required rank and full-support conditions hold.

Among the remaining
\[
N=n-2r+1
\]
columns outside \(R\), at least
\[
L=h-r+1
\]
must give value zero.

#### Witnesses for \(\mathcal B\), outside \(\mathcal Z\)

Suppose \(\mathcal B\) holds but \(\mathcal Z\) does not. Take a witnessing unit vector \(q\) with support \(R\), \(|R|=r\), and choose \(h\) good vertices \(D\) outside \(R\).

The vectors \(A[R,j]\), \(j\in D\), must span \(\mathbb R^r\). Otherwise a nonzero annihilator, extended by zero outside \(R\), would witness \(\mathcal Z\).

Choose \(I\subseteq D\) of size \(r\) giving a basis. For fixed \(R,I\), each assignment
\[
q^TA[R,j]\in\{0,1\},\qquad j\in I,
\]
determines at most one \(q\). There are at most \(2^r\) assignments. Retain only candidates that have full support, have norm one, and are not positive coordinate vectors.

Among the remaining
\[
N=n-2r
\]
columns outside \(R\), at least
\[
L=h-r
\]
must be good.

When bounding these witnesses, we drop the condition that \(\mathcal Z\) fails; thus no conditioning on unexposed edges is being used.

#### Probability of a fixed witness

In either construction, write
\[
b=|I|\in\{r-1,r\}.
\]
There are at most
\[
\binom nr\binom{n-r}{b}2^r
\tag{1}
\]
candidate witnesses of the indicated type.

For each union-bound term, \(R\) and \(I\) are fixed. Conditional on \(A[R,I]\), the remaining columns \(A[R,j]\), \(j\notin R\cup I\), are independent and uniform on \(\{0,1\}^r\). Lemma 1 therefore applies to the candidate determined by the exposed columns.

In both cases,
\[
N=n-r-b,\qquad L=h-b.
\]
Put
\[
a=\frac{3n}{\log n}.
\]
Since \(h\ge n/2+a\), we have
\[
L-\frac N2
=h-\frac n2+\frac{r-b}{2}\ge a,
\tag{2}
\]
and, since \(r\le k\),
\[
L\ge h-r\ge h-k=n-2k\ge2a.
\tag{3}
\]

We divide the support sizes into two ranges.

#### Small supports

Let
\[
r_0=\left\lfloor\frac{n}{(\log n)^3}\right\rfloor.
\]
For \(r\le r_0\), summing (1) over both witness types and all such \(r\) gives at most
\[
2n\binom n{r_0}^{\,2}2^{r_0}
=
\exp\!\left(
O\!\left(\frac{n\log\log n}{(\log n)^3}\right)
\right)
=
\exp\!\left(o\!\left(\frac{n}{(\log n)^2}\right)\right)
\tag{4}
\]
witnesses. Here we used \(\binom nt\le(en/t)^t\).

For a fixed candidate, the success probability in each remaining column is at most \(1/2\). By (2) and the elementary binomial Chernoff bound,
\[
\Pr(\text{at least }L\text{ successes})
\le \exp\left(-\frac{2a^2}{N}\right)
\le \exp\left(-\frac{18n}{(\log n)^2}\right).
\tag{5}
\]
Multiplying (4) and (5), the small-support contribution is at most
\[
\exp\left(-\frac{(18-o(1))n}{(\log n)^2}\right).
\tag{6}
\]

#### Large supports

For \(r>r_0\), Lemma 1 gives
\[
p_r\le \frac{4(\log n)^{3/2}}{\sqrt n}.
\]
For sufficiently large \(n\), this is less than one.

For either witness type, the count in (1) is at most \(2^{2n}\). By a union bound over sets of \(L\) successful columns,
\[
\Pr(\text{at least }L\text{ successes})\le 2^N p_r^L.
\]
Using (3), the total large-support contribution is therefore at most
\[
2n\,2^{3n}
\left(\frac{4(\log n)^{3/2}}{\sqrt n}\right)^{6n/\log n}.
\]
Its logarithm is
\[
(3\log 2-3+o(1))n.
\]
Because \(3\log2<3\), this contribution is \(\exp(-\Omega(n))\).

Combining this with (6) proves Lemma 2. \(\square\)

## 4. Proof of the localized-rigidity theorem

Work on the event supplied by Lemma 2.

Let \(|S|\le k\), put \(T=[n]\setminus S\), and suppose
\[
U=Q\oplus I_T
\]
is orthogonal and
\[
B=U^TAU
\]
is a graph adjacency matrix.

Its off-diagonal block is
\[
B[S,T]=Q^TA[S,T].
\]

Take any row of \(Q^T\), and extend it by zero outside \(S\) to a vector \(q\in\mathbb R^n\). It has norm one and support contained in \(S\). For every \(j\in T\),
\[
q^TAe_j\in\{0,1\}.
\]
Thus \(q\) has at least
\[
|T|=n-|S|\ge h
\]
good vertices outside its support.

Lemma 2 forces \(q\) to be a positive coordinate vector. This holds for every row of \(Q^T\). Orthogonality forces these coordinate vectors to be distinct, so \(Q\), and hence \(U\), is a permutation matrix. \(\square\)

The assertion is invariant under vertex relabelling. Consequently, inserting arbitrary relabellings before or after the localized conjugation does not produce a non-isomorphic mate.

## 5. Consequence: ordinary one-cell Godsil–McKay switching is absent

Here is a consequence directly related to the construction mentioned in the problem.

A one-cell switching set \(S\), of even size \(r\ge4\), satisfies:

- \(G[S]\) is regular;
- every vertex outside \(S\) has \(0\), \(r/2\), or \(r\) neighbors in \(S\).

The associated orthogonal matrix is
\[
Q=\frac2rJ_r-I_r.
\]
For a binary column \(x\) with \(t\) ones,
\[
Qx=\frac{2t}{r}\mathbf1-x,
\]
which is binary under the stated condition. Regularity implies that \(A[S,S]\) commutes with \(J_r\), so conjugation by \(Q\) leaves the internal block unchanged. Thus \(Q\oplus I\) implements the usual cospectral switch. For \(r\ge4\), \(Q\) is not a permutation matrix.

The theorem excludes such sets of size at most \(n/4\), with high probability. Larger sets can be excluded by an elementary regularity estimate.

Fix \(S\) of size \(r\), and split it into parts of sizes
\[
a=\lfloor r/2\rfloor,\qquad b=\lceil r/2\rceil.
\]
Condition on the edges inside the first part. The cross-degrees of its \(a\) vertices are independent \(\operatorname{Bin}(b,1/2)\) variables. If \(G[S]\) is regular of degree \(d\), each cross-degree has one prescribed value. Hence, for an absolute \(C\),
\[
\Pr(G[S]\text{ is regular})
\le r\left(\frac C{\sqrt b}\right)^a
=\exp(-\Omega(r\log r)).
\]
Summing over all \(S\) with \(r>n/4\) gives
\[
\Pr(\exists S,\ |S|>n/4,\ G[S]\text{ regular})
\le 2^n\exp(-\Omega(n\log n))
=o(1).
\]

Therefore:

> With high probability, \(G(n,1/2)\) has no one-cell Godsil–McKay switching set of even order at least four.

This concerns the explicitly defined one-cell operation, not every partitioned generalization of switching.

## 6. What remains unresolved

Equality of spectra for real symmetric matrices guarantees an orthogonal similarity
\[
B=U^TAU.
\]
It does **not** guarantee that \(U\) fixes any substantial collection of vertex coordinate vectors. The theorem above leaves globally supported similarities completely uncontrolled.

There is also a natural limitation to the cut-matrix argument. If \(|S|=s\) and \(2s-n\ge2\), then the column span of \(A[S,[n]\setminus S]\) has codimension at least two in \(\mathbb R^s\). Non-permutation orthogonal rotations can fix that span pointwise. They preserve the cut block, although they need not send the internal adjacency block to a binary matrix. Thus cut information alone cannot force the same conclusion substantially beyond half the vertices.

Finally, “localized orthogonal conjugation” is not the same as “changing edges incident with a small vertex set.” No edit-distance conclusion is proved here.

The partial result excludes many localized mechanisms, including the stated one-cell switching mechanism, but it neither proves the conjectured density of spectrally determined graphs nor constructs a counterexample to that conjecture.