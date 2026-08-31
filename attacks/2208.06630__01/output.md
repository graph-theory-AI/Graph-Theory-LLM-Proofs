```json
{
  "verdict": "already_resolved",
  "confidence": "high",
  "one_line": "The conjecture is true: a support-plus-rank potential gives the lower bound 2n-3, matching the stated construction, and the current source note already reports a resolution.",
  "would_publish": false,
  "caveats": "The proof below is self-contained; I have not independently verified the bibliographic attribution of the post-v1 proof."
}
```

## Statement

A lazy transposition \((a,b,p)\) is independently equal to the transposition \((a\,b)\) with probability \(p\), and to the identity otherwise. A sequence is a \(2\)-uniformity network if its random composition sends the distinguished points \(1,2\) to a uniformly random ordered pair of distinct elements of \([n]\).

We prove:

**Theorem.** For every \(n\ge 2\), a \(2\)-uniformity network has length at least \(2n-3\). The bound is attained by the construction in the question.

Thus the conjectured minimum is exactly \(2n-3\).

## 1. The lower bound

Let \((X,Y)\) denote the current locations of the two distinguished points. Associate to its distribution the \(n\times n\) matrix
\[
M_{ij}=\Pr(X=i,\ Y=j).
\]
Because \(X\ne Y\), the diagonal of \(M\) is zero.

For a nonnegative zero-diagonal matrix \(M\), define its active set by
\[
A(M)=\{i:\text{row }i\text{ or column }i\text{ of }M\text{ is nonzero}\},
\]
and put
\[
a(M)=|A(M)|,\qquad
\Phi(M)=a(M)+\operatorname{rank}_{\mathbb R}M.
\]

We need the following one-step lemma.

### Lemma

Let \(S\) be the permutation matrix of a transposition, and let
\[
M'=(1-p)M+pSMS^{T},\qquad 0\le p\le1.
\]
If \(M\) is nonnegative with zero diagonal, then
\[
\Phi(M')\le \Phi(M)+1.
\]

### Proof

The cases \(p=0,1\) are immediate: \(M'\) is respectively \(M\) or a simultaneous permutation of its rows and columns. Assume henceforth that \(0<p<1\).

First we show
\[
\operatorname{rank}M'\le \operatorname{rank}M+1. \tag{1}
\]
Suppose the transposition interchanges \(a,b\). In an orthonormal basis whose first vector is proportional to \(e_a-e_b\), the matrix \(S\) is
\[
\begin{pmatrix}
-1&0\\
0&I
\end{pmatrix}.
\]
Write, in this basis,
\[
M=
\begin{pmatrix}
\alpha&r^{T}\\
c&B
\end{pmatrix}.
\]
With \(\lambda=1-2p\), we then have
\[
M'=
\begin{pmatrix}
\alpha&\lambda r^{T}\\
\lambda c&B
\end{pmatrix}.
\]
If \(\lambda\ne0\), let \(D=\operatorname{diag}(\lambda,1,\ldots,1)\). Then
\[
M'=DMD+(1-\lambda^{2})\alpha E_{11}.
\]
Since \(D\) is invertible and the second summand has rank at most one, (1) follows. If \(\lambda=0\), then
\[
M'=\begin{pmatrix}\alpha&0\\0&B\end{pmatrix},
\]
so
\[
\operatorname{rank}M'\le \operatorname{rank}B+1
   \le \operatorname{rank}M+1.
\]

Because \(M\) is nonnegative and \(0<p<1\),
\[
\operatorname{supp}M'
 =\operatorname{supp}M\cup\operatorname{supp}(SMS^{T}).
\]
Consequently, \(a(M')=a(M)\) unless exactly one of \(a,b\) is active, in which case
\[
a(M')=a(M)+1. \tag{2}
\]

It remains to check that in the latter case the rank does not also increase. Suppose, without loss of generality, that \(a\) is active and \(b\) is inactive. Thus row and column \(b\) of \(M\) are zero, and \(M_{aa}=0\). Define an invertible matrix \(L\) by
\[
Le_a=(1-p)e_a+pe_b,\qquad Le_i=e_i\quad(i\ne a).
\]
A direct check on the matrix units in \(M\) gives
\[
M'=LML^{T}.
\]
Therefore
\[
\operatorname{rank}M'=\operatorname{rank}M.
\]
Together with (1) and (2), this proves that at most one of the active-set term and the rank term can increase beyond its old value, and hence
\[
\Phi(M')\le\Phi(M)+1.
\]
\(\square\)

### Applying the lemma

Initially,
\[
M_0=E_{12},
\]
so
\[
a(M_0)=2,\qquad \operatorname{rank}M_0=1,\qquad \Phi(M_0)=3.
\]

In a \(2\)-uniformity network, the final matrix is
\[
M_{\mathrm{fin}}=\frac1{n(n-1)}(J-I).
\]
Every index is active, so \(a(M_{\mathrm{fin}})=n\). Moreover, \(J-I\) has eigenvalue \(n-1\) on the all-ones vector and eigenvalue \(-1\) with multiplicity \(n-1\). Thus
\[
\operatorname{rank}M_{\mathrm{fin}}=n,
\qquad
\Phi(M_{\mathrm{fin}})=2n.
\]

If the network has \(m\) lazy transpositions, repeated use of the lemma gives
\[
2n=\Phi(M_{\mathrm{fin}})
   \le \Phi(M_0)+m
   =3+m.
\]
Therefore
\[
m\ge 2n-3.
\]

## 2. The matching construction

For \(n\ge3\), consider the temporal sequence
\[
(1,2,\tfrac12),
\]
followed, for \(k=3,\ldots,n\), by
\[
(1,k,p_k),\quad (1,2,\tfrac12),
\qquad
p_k=\frac{2}{n-k+3}.
\]
This is exactly
\[
(1,2,\tfrac12),(1,3,\tfrac2n),(1,2,\tfrac12),
(1,4,\tfrac2{n-1}),\ldots,
(1,n,\tfrac23),(1,2,\tfrac12).
\]
Its length is
\[
1+2(n-2)=2n-3.
\]

We verify uniformity.

### Uniformity of the unordered pair

Regard positions \(1,2\) as a two-place reservoir. Once a distinguished point is moved to some \(k\ge3\), it remains there, since that vertex is never touched again.

Immediately before processing \(k\), the preceding fair transposition \((1,2,\tfrac12)\) ensures that, conditional on there being \(r\in\{0,1,2\}\) distinguished points left in the reservoir, their occupied positions form a uniformly random \(r\)-subset of \(\{1,2\}\).

At this moment there are
\[
d_k=n-k+3
\]
undecided candidate positions: \(k,k+1,\ldots,n\), together with reservoir positions \(1,2\). The probability that the point \(k\) is selected is
\[
\Pr(1\text{ occupied})p_k.
\]
For \(r=0,1,2\), this equals respectively
\[
0,\qquad \frac12\frac2{d_k}=\frac1{d_k},
\qquad \frac2{d_k},
\]
and hence in every case it is
\[
\frac{r}{d_k}.
\]

This is exactly the usual sequential rule for choosing a uniformly random \(r\)-subset from \(d_k\) candidates: include the current candidate with probability \(r/d_k\). The following fair \((1,2)\)-transposition restores uniformity inside the reservoir. Induction on the number of undecided candidates therefore shows that the final unordered pair is uniform over all \(\binom n2\) two-subsets.

### Uniformity of the ordering

After the initial fair transposition, the probability matrix is
\[
\frac12(E_{12}+E_{21}),
\]
which is symmetric. Every later update has the form
\[
M\longmapsto (1-p)M+pSMS^{T},
\]
and therefore preserves symmetry. Thus the two orientations of every final unordered pair have equal probability.

Since each unordered pair has probability \(1/\binom n2\), every ordered pair \(i\ne j\) has probability
\[
\frac{1}{2\binom n2}=\frac1{n(n-1)}.
\]
Hence the construction is a \(2\)-uniformity network.

For \(n=2\), the single lazy transposition \((1,2,\tfrac12)\) suffices.

## Conclusion and status

The lower and upper bounds coincide:
\[
\boxed{\min |T|=2n-3}.
\]

There are no mathematical gaps in the argument under the standard definition of independent lazy transpositions. The supplied note concerning arXiv:2208.06630v3 indicates that the conjecture was already resolved after the preliminary version, so the catalog’s “open” label appears stale. I have not identified or verified the external attribution mentioned in that note.