```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "Under the intended O(n) interpretation the conjecture remains open, but permutation-invariant and low-degree algebraic colorings are rigorously ruled out, with a sharp classification for quadratic colorings.",
  "would_publish": false,
  "caveats": "Literal equality |H|=Cn is vacuous; the results below concern the intended uniform upper-bound formulation."
}
```

# 1. Precise formulation

Let \(V_n=\mathbb F_2^n\). The intended conjecture should be read as follows.

> **Conjecture.** There are constants \(C,n_0>0\) such that, for every \(n\ge n_0\), there is a coloring
> \[
> \chi:V_n\setminus\{0\}\to\{0,1\}
> \]
> for which every linear subspace \(H\le V_n\) with \(H\setminus\{0\}\) monochromatic satisfies
> \[
> |H|<Cn.
> \]

Equivalently, the largest monochromatic subspace should have dimension at most
\[
\log_2 n+O(1).
\]

The literal extracted wording, with equality \(|H|=Cn\), is not meaningful: every subspace has cardinality \(2^k\), so taking, for example, \(C=3\) makes \(2^k=3n\) impossible for every positive integer \(n\). Thus “size \(Cn\)” must mean “size at least \(Cn\)” or an \(O(n)\) upper bound.

Define the vector-space Ramsey number
\[
R(k)=\min\{n:\text{every two-coloring of }V_n\setminus\{0\}
\text{ has a monochromatic }k\text{-subspace}\}.
\]
Up to changes in constants, the conjecture is equivalent to
\[
R(k)=\Omega(2^k).
\]

# 2. The elementary \(O(n\log n)\) bound

The number of \(k\)-dimensional subspaces of \(V_n\) is the Gaussian coefficient
\[
{n\brack k}_2
 =2^{k(n-k)}
 \prod_{i=0}^{k-1}\frac{1-2^{i-n}}{1-2^{i-k}}
 <4\,2^{k(n-k)}.
\]
The constant \(4\) follows from
\[
\prod_{j=1}^{\infty}(1-2^{-j})>\frac14.
\]

In an independent uniform coloring, a fixed \(k\)-subspace is monochromatic with probability
\[
2\cdot 2^{-(2^k-1)}=2^{2-2^k}.
\]
Consequently a coloring with no monochromatic \(k\)-subspace exists whenever
\[
2^k>k(n-k)+4.
\tag{2.1}
\]

For example, writing \(L=\log_2 n\), for \(n\ge16\) one may take
\[
k=\left\lceil L+\log_2L\right\rceil+3.
\]
Then (2.1) holds, and every monochromatic subspace has cardinality less than
\[
2^{k-1}<8n\log_2 n.
\]
Thus the elementary bound is \(O(n\log n)\). The conjecture asks to remove the \(\log n\) factor.

# 3. Algebraic colorings

Every Boolean function on \(V_n\) has a unique multilinear algebraic normal form over \(\mathbb F_2\).

## 3.1 One color is automatically controlled by degree

The following elementary observation is useful.

> **Lemma 3.1.** Let \(q:V_n\to\mathbb F_2\) satisfy \(q(0)=0\) and \(\deg q<k\). Then there is no \(k\)-dimensional subspace \(H\) such that
> \[
> q(x)=1\qquad\text{for every }x\in H\setminus\{0\}.
> \]

**Proof.**
Choose a linear isomorphism \(L:\mathbb F_2^k\to H\). If \(q=1\) on \(H\setminus\{0\}\), then
\[
q(Ly)=
\begin{cases}
0,&y=0,\\
1,&y\ne0.
\end{cases}
\]
The algebraic normal form of this function is
\[
1+\prod_{i=1}^k(1+y_i),
\]
which has degree exactly \(k\). On the other hand, restriction along a linear map cannot increase algebraic degree, giving a contradiction. \(\square\)

Thus, for a degree-\((k-1)\) coloring with value \(0\) at the origin, it is enough to prevent \(k\)-subspaces on which the polynomial vanishes identically.

## 3.2 The random bound can be attained inside degree \(k-1\)

Let \(\mathcal P_{n,k-1}\) be the vector space of multilinear polynomials of degree at most \(k-1\) with zero constant term. Choose \(q\) uniformly from this space.

For any fixed \(k\)-subspace \(H\), the restriction map
\[
\mathcal P_{n,k-1}\longrightarrow
\{g:\mathbb F_2^k\to\mathbb F_2:\deg g\le k-1,\ g(0)=0\}
\]
is surjective. The target has dimension
\[
\sum_{i=1}^{k-1}\binom{k}{i}=2^k-2.
\]
Hence
\[
\Pr(q|_H\equiv0)=2^{-(2^k-2)}.
\]
It follows that
\[
\mathbb E\#\{H:q|_H\equiv0\}
 <4\,2^{k(n-k)-(2^k-2)}.
\]
Therefore:

> **Proposition 3.2.** If
> \[
> 2^k>k(n-k)+4,
> \]
> then there is a polynomial \(q\) of degree at most \(k-1\), with \(q(0)=0\), whose induced coloring has no monochromatic \(k\)-subspace.

This recovers the \(O(n\log n)\) result in a rather restricted algebraic class. It also isolates a sufficient route to the conjecture: construct a polynomial of degree below \(k=\log_2 n+O(1)\) which does not vanish identically on any \(k\)-subspace.

# 4. A general zero-subspace theorem for low-degree polynomials

The next theorem gives a substantial obstruction to low-degree approaches.

For integers \(r,t\ge0\), define
\[
D_r(t)=
\sum_{s=0}^{\min(t,r-1)}
(r-s)\binom{t}{s}.
\]

> **Theorem 4.1.** Let \(q:\mathbb F_2^n\to\mathbb F_2\) be a polynomial of degree at most \(r\), with \(q(0)=0\). Then \(q\) vanishes identically on a subspace of dimension \(t\), where
> \[
> n\le t+D_r(t).
> \tag{4.1}
> \]

## Proof

We first use the standard minimum-weight property of Boolean polynomials.

> **Minimum-weight lemma.** If a nonzero Boolean polynomial \(P\) in \(n\) variables has degree at most \(D\), then
> \[
> |\{x:P(x)=1\}|\ge 2^{n-D}.
> \]

This follows by induction on \(n\). Write
\[
P(x',x_n)=P_0(x')+x_nP_1(x').
\]
If \(P_1=0\), the weight is twice that of \(P_0\). If \(P_1\ne0\), then on every \(x'\) for which \(P_1(x')=1\), exactly one of
\(P_0(x')\) and \(P_0(x')+P_1(x')\) equals \(1\). Thus the weight of \(P\) is at least the weight of \(P_1\), whose degree is at most \(D-1\).

Now let \(U\) be a maximal linear subspace on which \(q\) vanishes identically, and write \(t=\dim U\). Fix a basis \(u_1,\dots,u_t\) of \(U\). Expand
\[
q\left(x+\sum_{i=1}^t y_i u_i\right)
 =\sum_{S\subseteq[t]} P_S(x)\prod_{i\in S}y_i
\tag{4.2}
\]
in algebraic normal form in the variables \(y_1,\dots,y_t\).

Because the left side has total degree at most \(r\),
\[
\deg P_S\le r-|S|.
\]
If \(|S|=r\), then \(P_S\) is constant. Evaluating at \(x=0\), all coefficients vanish because \(q|_U\equiv0\), so these constant terms are zero. Terms with \(|S|>r\) are also zero. Thus only the equations
\[
P_S(x)=0,\qquad |S|\le r-1,
\tag{4.3}
\]
are relevant.

Let \(Z\) be the common zero set of the polynomials in (4.3). By (4.2),
\[
x\in Z
\quad\Longleftrightarrow\quad
q\text{ vanishes on }x+U.
\]
Certainly \(U\subseteq Z\). If \(x\in Z\setminus U\), then \(q\) vanishes on
\[
\langle U,x\rangle=U\cup(x+U),
\]
contradicting maximality. Therefore \(Z=U\).

The polynomial
\[
Q(x)=\prod_{|S|\le r-1}(1+P_S(x))
\]
is the indicator of \(Z\). It is nonzero and has degree at most
\[
\sum_{s=0}^{\min(t,r-1)}
\binom ts(r-s)=D_r(t).
\]
The minimum-weight lemma now gives
\[
2^t=|Z|\ge2^{n-D_r(t)},
\]
which is exactly (4.1). \(\square\)

## 4.1 Consequences

For \(r=1\), Theorem 4.1 gives \(t\ge n-1\), as expected for a linear function.

For \(r=2\),
\[
D_2(t)=2+t,
\]
so
\[
t\ge \left\lfloor\frac{n-1}{2}\right\rfloor.
\tag{4.4}
\]

For fixed \(r\ge3\),
\[
D_r(t)=\binom{t}{r-1}+O_r(t^{r-2}),
\]
and hence
\[
t\ge ((r-1)!\,n)^{1/(r-1)}-O_r(1).
\tag{4.5}
\]
Thus every fixed-degree polynomial coloring contains a monochromatic subspace whose dimension is polynomial in \(n\), far larger than \(O(\log n)\).

For example, when \(r=3\),
\[
n\le \frac{(t+2)(t+3)}2,
\]
so every cubic coloring has a monochromatic zero-subspace of dimension at least
\[
\frac{\sqrt{8n+1}-5}{2}.
\]

There is also a necessary degree bound for any algebraic solution of the conjecture.

> **Corollary 4.2.** Suppose a coloring induced by a Boolean polynomial has all monochromatic subspaces of cardinality at most \(Cn\), where \(C\) is fixed. Then its normalized algebraic degree is at least
> \[
> \left(\frac12-o(1)\right)\log_2 n.
> \]

Indeed, put \(L=\lceil\log_2(Cn)\rceil\). The zero-subspace dimension in Theorem 4.1 is at most \(L\), so
\[
n\le L+D_r(L).
\]
If \(r\le(1/2-\varepsilon)L\), then, using the binary entropy function \(h_2\),
\[
D_r(L)
 \le L\sum_{s\le(1/2-\varepsilon)L}\binom Ls
 \le L\,2^{h_2(1/2-\varepsilon)L}
 =o(2^L)=o(n),
\]
a contradiction.

# 5. Sharp classification of quadratic colorings

The quadratic case can be settled exactly.

> **Proposition 5.1.** Let \(k\ge3\). A coloring induced by a polynomial of degree at most \(2\) can avoid monochromatic \(k\)-dimensional subspaces in \(\mathbb F_2^n\) if and only if
> \[
> n\le2k.
> \]

## Proof: impossibility for \(n\ge2k+1\)

After adding a constant and possibly swapping the color names, assume \(q(0)=0\). By (4.4), \(q\) vanishes on a subspace of dimension at least
\[
\left\lfloor\frac{n-1}{2}\right\rfloor\ge k.
\]
Any \(k\)-subspace of it is monochromatic.

## Proof: construction for \(n=2k\)

On \(\mathbb F_2^{2k}\), with coordinates
\[
(a_1,b_1,\dots,a_k,b_k),
\]
define
\[
q=a_1+b_1+a_1b_1+\sum_{i=2}^k a_i b_i.
\tag{5.1}
\]
Its polar form is nondegenerate. Relative to the standard symplectic basis, the Arf invariant of \(q\) is \(1\): the first pair has both basis vectors of \(q\)-value \(1\), while all remaining pairs have both values \(0\).

If there were a \(k\)-dimensional subspace \(H\) on which \(q\) vanished, then its polar form would vanish on \(H\). Thus \(H\) would be Lagrangian. Extending a basis of \(H\) to a symplectic basis would give Arf invariant \(0\), since \(q\) vanishes on all the first basis vectors. This contradicts the Arf invariant \(1\) of (5.1).

Hence there is no \(q=0\) monochromatic \(k\)-subspace. There is also no \(q=1\) punctured \(k\)-subspace, by Lemma 3.1 since \(2<k\).

For \(n<2k\), restrict (5.1) to any \(n\)-dimensional subspace. \(\square\)

Thus quadratic forms are optimal only in the regime \(k\ge n/2\), and cannot approach the conjectural regime \(k\sim\log_2 n\).

# 6. Permutation-invariant colorings fail very badly

A natural idea is to color a vector according only to its Hamming weight. This cannot work: such a coloring always has a monochromatic subspace of quadratic, rather than linear, cardinality.

> **Theorem 6.1.** Let
> \[
> \chi:\mathbb F_2^n\setminus\{0\}\to\{0,1\}
> \]
> depend only on Hamming weight. For every \(n\ge5\), there is a monochromatic subspace \(H\) such that
> \[
> |H|>\left(\frac{n+5}{10}\right)^2>\frac{n^2}{100}.
> \]

## Proof

Let \(t\) be maximal such that
\[
5(2^t-1)\le n,
\]
and put \(W=2^{t-1}\).

The binary simplex code \(S_t\) has dimension \(t\), length \(2^t-1\), and every nonzero codeword has weight \(W\). One realization has generator matrix whose columns are all nonzero vectors of \(\mathbb F_2^t\).

Repeating every coordinate \(r\) times produces a dimension-\(t\) code \(S_t^{(r)}\) of length
\[
r(2^t-1)
\]
in which every nonzero codeword has weight \(rW\).

Now color the integers \(1,\dots,5\) by assigning \(r\) the color of vectors of weight \(rW\). Every two-coloring of \(\{1,\dots,5\}\) contains a monochromatic Schur triple
\[
r,\ s,\ r+s.
\]
For completeness, assume \(1\) is red. Avoiding \(1+1=2\) forces \(2\) blue; avoiding \(2+2=4\) forces \(4\) red; then \(3\) must be blue to avoid \(1+3=4\); \(5\) must be red to avoid \(2+3=5\); but now \(1+4=5\) is red.

Take the direct sum
\[
S_t^{(r)}\oplus S_t^{(s)}
\]
on disjoint coordinate sets. Its dimension is \(2t\), its length is at most
\[
(r+s)(2^t-1)\le5(2^t-1)\le n,
\]
and zero coordinates may be appended to reach length \(n\).

Every nonzero codeword has weight one of
\[
rW,\qquad sW,\qquad (r+s)W,
\]
according to whether one or both components are nonzero. These three weights have the same color, so this is a monochromatic \(2t\)-dimensional subspace.

By maximality of \(t\),
\[
5(2^{t+1}-1)>n,
\]
and hence
\[
2^t>\frac{n+5}{10}.
\]
Therefore
\[
|H|=2^{2t}>\left(\frac{n+5}{10}\right)^2.
\]
\(\square\)

In particular, no coloring invariant under all coordinate permutations can satisfy the conjecture.

# 7. Remaining gap

The intended conjecture is not resolved here.

The quantitative obstruction to the elementary probabilistic method is clear. At the conjectural scale
\[
2^k=Cn,\qquad k=\log_2n+O(1),
\]
the number of \(k\)-subspaces has logarithm approximately \(kn\), while a fixed subspace is monochromatic with probability about \(2^{-2^k}\). Thus the first-moment exponent is
\[
kn-2^k=n(\log_2n-C+O(1)),
\]
which is strongly positive.

The results above show:

1. Random colorings, even restricted to degree \(k-1\), give \(O(n\log n)\).
2. Any fixed-degree polynomial construction is impossible.
3. A polynomial construction meeting \(O(n)\) must have degree at least \((1/2-o(1))\log_2n\).
4. Quadratic colorings are sharply limited to ambient dimension at most twice the forbidden subspace dimension.
5. Any Hamming-weight or fully coordinate-permutation-invariant coloring has a monochromatic subspace of size \(\Omega(n^2)\).

What is still missing is a genuinely nonsymmetric, degree-growing construction—or a non-first-moment existence argument—that prevents all \(k\)-subspaces at \(k=\log_2n+O(1)\).