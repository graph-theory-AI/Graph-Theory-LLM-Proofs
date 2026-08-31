```json
{
  "verdict": "proved",
  "confidence": "high",
  "one_line": "An alteration argument gives ES_l(n) <= ceil(l(4 ES_n(n))^((n-1)/(n-2))), so the source bound yields a uniform linear-in-l upper bound matching the lower bound in its l-dependence.",
  "would_publish": true,
  "caveats": "The subexponential gap in n remains, and I have not independently checked whether this transfer argument already appears elsewhere."
}
```

# Uniform linear dependence on \(\ell\)

## Statement

The advertised gap in the dependence on \(\ell\) can be closed.

### Theorem
There is an absolute constant \(C_1>0\) such that, for all integers \(\ell,n\ge 3\),
\[
ES_\ell(n)\le \ell\,2^{\,n+C_1\sqrt{n\log n}}.
\]
Together with the lower bound from the source paper, this gives
\[
\frac1{12}\,\ell\,2^n
   < ES_\ell(n)
   \le \ell\,2^{\,n+C_1\sqrt{n\log n}}.
\]
Thus the dependence on \(\ell\) is uniformly linear, with no restriction on the relative sizes of \(\ell\) and \(n\).

The key is the following general transfer inequality.

### Transfer inequality
For all \(k,\ell,n\ge3\),
\[
\boxed{\;
ES_\ell(n)
 \le
 \left\lceil
 \ell\bigl(4ES_k(n)\bigr)^{(k-1)/(k-2)}
 \right\rceil .
\;}
\]

Taking \(k=n\) and applying the source paper's bound to \(ES_n(n)\) proves the theorem.

---

## 1. Extracting a set with smaller collinearity

We first prove an elementary alteration lemma.

### Lemma
Let \(P\) be an \(N\)-point set in the plane with fewer than \(\ell\) points on every line. For every integer \(k\ge3\), \(P\) contains a subset \(Q\) with no \(k\) collinear points and
\[
|Q|\ge
\frac14\left(\frac{N}{\ell}\right)^{(k-2)/(k-1)}.
\]

### Proof

Form a \(k\)-uniform hypergraph \(H\) on vertex set \(P\), whose edges are the collinear \(k\)-subsets of \(P\). Let \(e=e(H)\).

For every line \(L\) containing at least \(k\) points of \(P\), put
\[
s_L=|P\cap L|.
\]
Since no line contains \(\ell\) points, \(s_L\le \ell-1\). Moreover,
\[
e=\sum_L\binom{s_L}{k}.
\]
Using
\[
\binom{s}{k}
=
\binom{s}{2}
\frac{\binom{s-2}{k-2}}{\binom{k}{2}}
\le
\binom{s}{2}\ell^{k-2},
\]
and the fact that each pair of points lies on a unique line, we obtain
\[
e
\le
\ell^{k-2}\sum_L\binom{s_L}{2}
\le
\ell^{k-2}\binom{N}{2}
<
N^2\ell^{k-2}.
\tag{1}
\]

Set
\[
a=\frac{k-2}{k-1}.
\]

If \(e<N/2\), delete at most one vertex for each edge. This leaves an independent set of size greater than \(N/2\), and hence of size at least
\[
\frac14\left(\frac N\ell\right)^a,
\]
because \((N/\ell)^a\le N\).

Now suppose \(e\ge N/2\). Choose each vertex independently with probability
\[
p=\left(\frac{N}{2e}\right)^{1/(k-1)}\le1.
\]
Let \(X\) be the number of chosen vertices and \(Y\) the number of hyperedges contained entirely in the chosen set. Then
\[
\mathbb E[X-Y]
=pN-p^ke
=\frac{pN}{2}.
\]
For some outcome, deleting at most one vertex from every surviving edge therefore leaves an independent set of size at least \(pN/2\). By (1),
\[
\begin{aligned}
\frac{pN}{2}
&\ge
\frac N2
\left(\frac{1}{2N\ell^{k-2}}\right)^{1/(k-1)}
\\
&=
2^{-1-1/(k-1)}
\left(\frac N\ell\right)^{(k-2)/(k-1)}
\\
&\ge
\frac14
\left(\frac N\ell\right)^{(k-2)/(k-1)}.
\end{aligned}
\]
An independent set in \(H\) is precisely a subset with no \(k\) collinear points. This proves the lemma. \(\square\)

---

## 2. Proof of the transfer inequality

Let
\[
M=ES_k(n),\qquad
r=\frac{k-1}{k-2},
\]
and take
\[
N=
\left\lceil \ell(4M)^r\right\rceil.
\]

Consider any \(N\)-point set \(P\). If \(P\) contains \(\ell\) collinear points, there is nothing to prove. Otherwise, the lemma gives a subset \(Q\subseteq P\) with no \(k\) collinear points and
\[
|Q|
\ge
\frac14\left(\frac N\ell\right)^{1/r}
\ge
\frac14\left((4M)^r\right)^{1/r}
=M.
\]
By the definition of \(M=ES_k(n)\), every \(M\)-point set contains either \(k\) collinear points or \(n\) points in convex position. The first alternative is impossible in \(Q\), so \(Q\), and hence \(P\), contains \(n\) points in convex position.

Therefore
\[
ES_\ell(n)
\le
\left\lceil
\ell\bigl(4ES_k(n)\bigr)^{(k-1)/(k-2)}
\right\rceil.
\qquad\square
\]

---

## 3. Applying the diagonal bound

Set \(k=n\). The transfer inequality becomes
\[
ES_\ell(n)
\le
\left\lceil
\ell\bigl(4ES_n(n)\bigr)^{(n-1)/(n-2)}
\right\rceil.
\tag{2}
\]

The theorem in the supplied source paper, applied with its two parameters both equal to \(n\), gives an absolute \(C_0\) such that
\[
ES_n(n)
<
n^2\,2^{\,n+C_0\sqrt{n\log n}}.
\tag{3}
\]

Let \(r=(n-1)/(n-2)=1+1/(n-2)\). Taking logarithms in (3),
\[
\begin{aligned}
\log_2\bigl(4ES_n(n)\bigr)^r
&\le
r\left(
n+2\log_2 n+2+C_0'\sqrt{n\log_2 n}
\right)\\
&=
n+C_0'\sqrt{n\log_2 n}+2\log_2 n+2\\
&\quad+
\frac{
n+C_0'\sqrt{n\log_2 n}+2\log_2 n+2
}{n-2}.
\end{aligned}
\]
For all \(n\ge3\), every term after \(n\) is
\[
O\!\left(\sqrt{n\log n}\right)
\]
with an absolute implied constant. Absorbing the ceiling in (2) into the same error term yields
\[
ES_\ell(n)
\le
\ell\,2^{\,n+C_1\sqrt{n\log n}}
\]
for some absolute \(C_1\).

Finally, the supplied lower bound
\[
(3\ell-1)2^{n-5}<ES_\ell(n)
\]
implies, since \(\ell\ge3\),
\[
ES_\ell(n)>\frac1{12}\ell\,2^n.
\]

Hence
\[
\frac1{12}\ell\,2^n
<
ES_\ell(n)
\le
\ell\,2^{\,n+C_1\sqrt{n\log n}},
\]
which establishes the correct, uniformly linear dependence on \(\ell\).

## Remaining gap

This argument does not close the factor \(2^{O(\sqrt{n\log n})}\) between the lower and upper bounds as functions of \(n\). It does, however, remove the extra factor of \(\ell\) from the source upper bound without worsening its \(n\)-dependence beyond changing the absolute constant in the subexponential term.