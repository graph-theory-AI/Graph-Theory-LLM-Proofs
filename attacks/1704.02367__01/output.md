```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "Polynomial removal bounds are proved for the genuinely two-dimensional family of nonsingular fixed-size binary patterns, for every finite one-row or one-column family, and for a monochromatic-anchor class, but not for arbitrary finite families.",
  "would_publish": false,
  "caveats": "Only structured finite families are handled; no polynomial or exponential bound is obtained for arbitrary mixed two-dimensional families, and novelty was not checked."
}
```

# Mathematical writeup

## 1. Formalization

For an \(r\times s\) binary matrix \(F\) and an \(N\times N\) binary matrix \(M\), let
\[
\operatorname{cop}_F(M)
\]
be the number of pairs of increasing index sequences
\[
i_1<\cdots<i_r,\qquad j_1<\cdots<j_s
\]
for which \(M[i_a,j_b]=F[a,b]\) for every \(a,b\).

For a fixed finite family \(\mathcal F\), a polynomial removal lemma means that there are constants \(c_{\mathcal F},C_{\mathcal F}>0\) such that every \(M\) which is \(\varepsilon\)-far from being \(\mathcal F\)-free contains some \(F\in\mathcal F\) satisfying
\[
\operatorname{cop}_F(M)\ge c_{\mathcal F}\varepsilon^{C_{\mathcal F}}
  N^{r(F)+s(F)}.
\]

The general finite-family problem is not resolved below. Three structured classes admit direct polynomial bounds.

---

## 2. A genuinely two-dimensional finite family: bounded binary rank

Let \(t=k+1\), and define
\[
\mathcal I_t=\{A\in\{0,1\}^{t\times t}:\det_{\mathbb F_2}A=1\}.
\]
This is a finite family of
\[
|\mathcal I_t|=|\operatorname{GL}(t,2)|
=\prod_{j=0}^{t-1}(2^t-2^j)
\]
patterns. None contains another, since they all have the same dimensions.

### Theorem 2.1

If an \(N\times N\) binary matrix \(M\) is \(\varepsilon\)-far in Hamming distance from having rank at most \(k\) over \(\mathbb F_2\), then some \(A\in\mathcal I_t\) satisfies
\[
\operatorname{cop}_A(M)
\ge
\frac{(\varepsilon/2)^{2t}}
     {(t!)^2|\operatorname{GL}(t,2)|}\,N^{2t}.
\]

Consequently, the finite forbidden family \(\mathcal I_t\) has a polynomial ordered-matrix removal lemma.

### Proof

A binary matrix is \(\mathcal I_t\)-free exactly when its rank over \(\mathbb F_2\) is at most \(t-1=k\).

Set \(\alpha=\varepsilon/2\). We first construct many ordered sequences of \(t\) robustly independent rows.

Suppose rows \(v_1,\dots,v_{i-1}\) have already been chosen, where \(i\le t\), and put
\[
S_{i-1}=\operatorname{span}_{\mathbb F_2}\{v_1,\dots,v_{i-1}\}.
\]
For each row \(v\) of \(M\), let \(d(v,S_{i-1})\) denote its Hamming distance from the nearest vector in \(S_{i-1}\).

Replacing each row independently by a nearest vector of \(S_{i-1}\) produces a matrix of rank at most \(i-1\le k\). Hence
\[
\sum_{v\text{ row of }M}d(v,S_{i-1})\ge \varepsilon N^2.
\]
There must therefore be at least \(\alpha N\) rows \(v\) satisfying
\[
d(v,S_{i-1})\ge \alpha N.
\]
Indeed, if fewer than \(\alpha N\) rows had this property, the total distance would be strictly less than
\[
\alpha N\cdot N+N\cdot\alpha N=\varepsilon N^2.
\]

Thus there are at least
\[
(\alpha N)^t
\]
ordered row sequences \(v_1,\dots,v_t\) such that
\[
d(v_i,\operatorname{span}(v_1,\dots,v_{i-1}))\ge\alpha N
\quad\text{for every }i.
\]

Fix one such row sequence. We count ordered column sequences \(c_1,\dots,c_t\) for which the resulting \(t\times t\) matrix is nonsingular.

Inductively suppose \(c_1,\dots,c_{i-1}\) have been selected so that
\[
(v_a(c_b))_{1\le a,b\le i-1}
\]
is nonsingular. There is a unique vector
\[
u\in\operatorname{span}(v_1,\dots,v_{i-1})
\]
which agrees with \(v_i\) on \(c_1,\dots,c_{i-1}\). The vector \(v_i-u\) has weight at least \(\alpha N\), and vanishes on the previously selected columns. Every column \(c_i\) on which \(v_i-u\) equals \(1\) extends the minor to a nonsingular \(i\times i\) minor. Hence there are at least \(\alpha N\) choices at each step.

It follows that every robust ordered row sequence admits at least \((\alpha N)^t\) ordered column sequences yielding a nonsingular minor. Altogether there are at least
\[
(\alpha N)^{2t}
\]
such ordered pairs of row and column sequences.

A fixed pair of unordered row and column sets is counted at most \((t!)^2\) times. Therefore \(M\) has at least
\[
\frac{(\alpha N)^{2t}}{(t!)^2}
\]
distinct nonsingular \(t\times t\) ordered submatrices. Pigeonholing among the \(|\operatorname{GL}(t,2)|\) possible binary nonsingular patterns gives the claimed bound. ∎

This gives, for example, a polynomial removal lemma for the six invertible \(2\times2\) binary matrices, namely the hereditary property “rank at most one.”

---

## 3. Arbitrary finite families of one-row patterns

Here the interaction between different forbidden patterns can also be handled completely.

Let \(\mathcal W\) be a finite nonempty collection of nonempty binary words. Regard each \(w\in\mathcal W\) as a \(1\times |w|\) ordered matrix. Put
\[
q=|\mathcal W|,\qquad L=\max_{w\in\mathcal W}|w|.
\]

### Theorem 3.1

Let \(M\) be an \(R\times S\) binary matrix which is \(\varepsilon\)-far from having every row avoid every word in \(\mathcal W\) as a subsequence. Then some \(w\in\mathcal W\) satisfies
\[
\operatorname{cop}_{1\times w}(M)
\ge
\frac1q\left(\frac{\varepsilon}{200L^2}\right)^{2L}
R\,S^{|w|}.
\]

In particular,
\[
\delta_{\mathcal W}(\varepsilon)^{-1}
\le q(200L^2)^{2L}\varepsilon^{-2L}.
\]
By transposition, the same conclusion holds for arbitrary finite families all of whose members have one column.

The proof rests on a one-dimensional removal lemma.

### Lemma 3.2

Let \(x\in\{0,1\}^n\) and \(0<\eta\le1\). At least one of the following holds:

1. \(x\) can be changed in fewer than \(\eta n\) positions to a word avoiding every member of \(\mathcal W\);
2. some \(w\in\mathcal W\) has at least
   \[
   \left(\frac{\eta}{200L^2}\right)^{2L}n^{|w|}
   \]
   occurrences as a subsequence of \(x\).

#### Proof

Set
\[
t=\left\lceil\frac{8L}{\eta}\right\rceil,
\qquad
\rho=\frac{\eta}{8},
\qquad
\Gamma=\left(\frac{\eta}{200L^2}\right)^{2L}.
\]

First suppose \(n<4Lt\). If \(x\) is not \(\mathcal W\)-free, it contains at least one copy of some \(w\in\mathcal W\). Since
\[
t\le\frac{9L}{\eta}
\quad\text{and hence}\quad
n<\frac{36L^2}{\eta},
\]
for every \(\ell\le L\),
\[
\Gamma n^\ell
\le
\left(\frac{\eta}{200L^2}\right)^{2L}
\left(\frac{36L^2}{\eta}\right)^L
<1.
\]
Thus one occurrence is enough for alternative 2. If \(x\) is free, alternative 1 holds.

Now assume \(n\ge4Lt\). Partition \(x\) into \(t\) consecutive intervals, each of size \(b\) or \(b+1\), where \(b=\lfloor n/t\rfloor\). Call an interval balanced if each symbol occurs in it at least \(\rho b\) times.

Fix one word \(w^*\in\mathcal W\), of length \(\ell^*\). If at least \(\ell^*\) intervals are balanced, choose them in increasing order and select, from the \(j\)-th chosen interval, a position carrying \(w^*_j\). This gives at least
\[
(\rho b)^{\ell^*}
\ge
\left(\frac{\eta^2}{144L}\right)^{\ell^*}n^{\ell^*}
\ge \Gamma n^{\ell^*}
\]
copies of \(w^*\).

We may therefore assume that fewer than \(\ell^*\le L\) intervals are balanced. In every unbalanced interval, change all minority symbols to the majority symbol; do the same in the balanced intervals, breaking ties arbitrarily. Let the resulting block-constant word be \(y\).

The number of changes in unbalanced intervals is less than
\[
t\rho b\le \frac{\eta n}{8}.
\]
There are fewer than \(L\) balanced intervals, and their total modification cost is at most
\[
\frac{L(b+1)}2\le\frac{Ln}{t}\le\frac{\eta n}{8}.
\]
Thus \(d_H(x,y)<\eta n\).

If \(y\) is \(\mathcal W\)-free, alternative 1 holds. Otherwise, let an occurrence of \(w\in\mathcal W\), \(|w|=\ell\), be fixed in \(y\). Suppose this occurrence uses \(k\) positions from a particular interval. Since \(y\) is constant there, all these \(k\) symbols are the majority symbol of that interval. In \(x\), that symbol occurs at least \(b/2\) times. Since \(b\ge4L\),
\[
\binom{b/2}{k}\ge\left(\frac{b}{2L}\right)^k.
\]
Multiplying over all intervals used by the occurrence gives at least
\[
\left(\frac{b}{2L}\right)^\ell
\ge
\left(\frac{\eta}{36L^2}\right)^\ell n^\ell
\ge \Gamma n^\ell
\]
copies of \(w\) in \(x\). This is alternative 2. ∎

### Proof of Theorem 3.1

For row \(i\), let \(d_i\) be its minimum Hamming distance from a \(\mathcal W\)-free word of length \(S\). Since the constraints act independently on the rows,
\[
\sum_{i=1}^R d_i\ge\varepsilon RS.
\]

For every \(i\) with \(d_i>0\), apply Lemma 3.2 with
\[
\eta_i=d_i/S.
\]
The first alternative would contradict the minimality of \(d_i\). Hence there is \(w_i\in\mathcal W\) such that row \(i\) contains at least
\[
\left(\frac{d_i/S}{200L^2}\right)^{2L}S^{|w_i|}
\]
copies of \(w_i\).

Assign each row to one such \(w_i\). For some \(w\in\mathcal W\),
\[
\sum_{i:w_i=w}\left(\frac{d_i}{S}\right)^{2L}
\ge
\frac1q\sum_{i=1}^R\left(\frac{d_i}{S}\right)^{2L}.
\]
By convexity,
\[
\sum_{i=1}^R\left(\frac{d_i}{S}\right)^{2L}
\ge
R\left(\frac{\sum_i d_i}{RS}\right)^{2L}
\ge R\varepsilon^{2L}.
\]
Summing the copies over the assigned rows proves
\[
\operatorname{cop}_{1\times w}(M)
\ge
\frac1q
\left(\frac{\varepsilon}{200L^2}\right)^{2L}
R\,S^{|w|}.
\]
∎

If there is no \(\mathcal W\)-free word of length \(S\), Lemma 3.2 applied to every row with \(\eta=\varepsilon\) gives the same conclusion directly.

---

## 4. A monochromatic-anchor class

The following elementary criterion gives another genuinely two-dimensional finite-family class.

### Proposition 4.1

Let \(\mathcal F\) be a finite family such that:

1. every \(F\in\mathcal F\) has at least one \(1\); and
2. \(\mathcal F\) contains the all-one \(r\times s\) matrix \(J_{r,s}\).

Then \(\mathcal F\) has a polynomial ordered-matrix removal lemma.

More explicitly, put
\[
D=\max_{F\in\mathcal F}\bigl(r(F)+s(F)\bigr).
\]
There is \(c_{\mathcal F}>0\) such that every \(N\times N\) matrix \(M\) which is \(\varepsilon\)-far from being \(\mathcal F\)-free contains some \(F\in\mathcal F\) with
\[
\operatorname{cop}_F(M)
\ge c_{\mathcal F}\varepsilon^{rsD}N^{r(F)+s(F)}.
\]

### Proof

The all-zero matrix is \(\mathcal F\)-free. Hence an \(\varepsilon\)-far matrix \(M\) has at least \(\varepsilon N^2\) entries equal to \(1\). Write their density as \(p\ge\varepsilon\).

The number of labeled homomorphisms of \(K_{r,s}\) into the \(1\)-entries of \(M\), allowing repeated vertices, is at least
\[
p^{rs}N^{r+s}.
\]
For completeness, if \(c(x_1,\dots,x_r)\) denotes the size of the common \(1\)-neighborhood of an ordered row tuple, then two applications of convexity give
\[
\sum_{x_1,\dots,x_r}c(x_1,\dots,x_r)^s
\ge p^{rs}N^{r+s}.
\]

At most
\[
A N^{r+s-1},
\qquad
A=\binom r2+\binom s2,
\]
of these maps repeat a row or a column. Thus, whenever
\[
N\ge 2A\varepsilon^{-rs},
\]
there are at least
\[
\frac{\varepsilon^{rs}}{2r!s!}N^{r+s}
\]
ordered copies of \(J_{r,s}\).

For smaller \(N\), an \(\varepsilon\)-far matrix is not itself \(\mathcal F\)-free, so it has at least one copy of some \(F\in\mathcal F\). Since \(N=O_{\mathcal F}(\varepsilon^{-rs})\), this one copy is at least
\[
c_{\mathcal F}\varepsilon^{rsD}N^{r(F)+s(F)}
\]
for a sufficiently small fixed \(c_{\mathcal F}>0\). Combining the two ranges proves the claim. ∎

The color-complemented statement also holds: every forbidden pattern has a zero and the family contains an all-zero rectangle.

---

## 5. Necessary dependence on the family

No exponent uniform over all finite families is possible. For example, take the one-row family
\[
\mathcal W=\{1^L\}.
\]
A row is \(\mathcal W\)-free exactly when it has at most \(L-1\) ones. Let every row of an \(R\times S\) matrix have
\[
L-1+\lceil\varepsilon S\rceil
\]
ones. The matrix is \(\varepsilon\)-far from being \(\mathcal W\)-free, while
\[
\frac{\operatorname{cop}_{1\times 1^L}(M)}{RS^L}
=
\frac{\binom{L-1+\lceil\varepsilon S\rceil}{L}}{S^L}
\longrightarrow \frac{\varepsilon^L}{L!}.
\]
Thus the polynomial exponent must be allowed to depend on the forbidden dimensions.

Also, if \(F_0\in\mathcal F\) is an ordered submatrix of every member of \(\mathcal F\), then \(\mathcal F\)-freeness is exactly \(F_0\)-freeness. Such families reduce immediately to the known single-pattern result quoted in the problem statement.

---

## 6. Remaining gap

The proofs above use special structure:

- bounded rank supplies a robust linear-algebraic basis construction;
- one-row patterns make the edit distance decompose row by row;
- the monochromatic-anchor case reduces distance to global density.

For a general finite family of mixed \(r\times s\) patterns with \(r,s\ge2\), none of these mechanisms is available. In particular, being far from
\[
\bigcap_{F\in\mathcal F}\{F\text{-free matrices}\}
\]
does not imply being far from any one constituent \(F\)-free property, and repairing one forbidden pattern can create exact copies of another. The argument therefore yields neither a polynomial nor an exponential bound for arbitrary finite families.