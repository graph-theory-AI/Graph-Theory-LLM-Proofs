```json
{
  "verdict": "partial",
  "confidence": "medium",
  "one_line": "For canonical subproducts, I obtain 2^{(1/2-o(1))n^2} < R_2(2,n) <= 2^{2^{2n+O(log n)}}, but this does not settle the intended single-versus-double-exponential question.",
  "would_publish": false,
  "caveats": "The excerpt omits the formal copy definition and uses 'superexponential' ambiguously; the full paper may already contain the d=2 refinement."
}
```

# Mathematical writeup

## 1. Formal model and a necessary clarification

Write the two factors of \(K_N\square K_N\) as \(X\) and \(Y\), with
\[
|X|=|Y|=N.
\]
A coloring can be represented by two families of graph colorings:
\[
H_y:\binom X2\to\{0,1\}\qquad (y\in Y)
\]
for the horizontal edges, and
\[
V_x:\binom Y2\to\{0,1\}\qquad (x\in X)
\]
for the vertical edges.

For \(A\subseteq X\) and \(B\subseteq Y\), the canonical subproduct \(A\times B\) is strongly directionally monochromatic if there are colors \(\alpha,\beta\) such that
\[
H_y(e)=\alpha
\quad\text{for all }y\in B,\ e\in\binom A2,
\tag{1}
\]
and
\[
V_x(f)=\beta
\quad\text{for all }x\in A,\ f\in\binom B2.
\tag{2}
\]
This is the strongest natural interpretation of “the edges in each direction are monochromatic.” A weaker convention allows the color in (1) to depend on \(y\), and that in (2) to depend on \(x\).

The argument below treats the strong version. The random lower bound is proved even against the weaker version.

The canonical/direction-preserving qualification matters. If arbitrary non-induced graph copies were allowed, a monochromatic \(K_{n^2}\) inside one fiber \(K_N\) would contain a monochromatic copy of \(K_n\square K_n\), giving the elementary upper bound
\[
R_2(2,n)\le r_2(n^2)\le 4^{n^2}.
\]
Thus the open problem must be using canonical, induced, or otherwise direction-preserving copies.

For completeness, if “copy” means induced graph copy, then for \(n\ge3\) every induced \(K_n\square K_n\) in \(K_N\square K_N\) is canonical up to swapping the factors. Indeed, every clique of size at least three in a rook graph lies in a single row or column. The images of an intersecting source row and source column must lie in ambient lines of opposite orientations, since otherwise two source vertices differing in both coordinates would become adjacent. This forces the entire image to be \(A\times B\).

---

## 2. Bounds obtained

Let \(r_q(t)\) denote the ordinary \(q\)-color diagonal graph Ramsey number.

### Proposition

For the strong directional version,
\[
R_2^{\mathrm{str}}(2,n)
\le
2\binom{r_2(2n-1)}{2n-1}\,
r_{\,2^{2n-1}}(n).
\tag{3}
\]
Consequently,
\[
R_2^{\mathrm{str}}(2,n)
\le
2^{O(n^2 4^n)}
=
2^{\,2^{\,2n+O(\log n)}}.
\tag{4}
\]

For the weaker line-by-line version,
\[
R_2^{\mathrm{wk}}(2,n)
\le
\binom{r_2(n)}n\,r_{\,2^n}(n)
\le
2^{O(n^2 2^n)}
=
2^{\,2^{\,n+O(\log n)}}.
\tag{5}
\]

On the other hand, random coloring gives, for either version,
\[
R_2(2,n)\ge 2^{(1/2-o(1))n^2}.
\tag{6}
\]

Thus, under the canonical-subproduct interpretation,
\[
2^{(1/2-o(1))n^2}
<
R_2(2,n)
\le
2^{\,2^{\,2n+O(\log n)}}.
\tag{7}
\]

Relative to the bound \(2^{2^{O(n^2)}}\) quoted in the prompt for \(d=2\), (4) replaces the quadratic inner exponent by a linear one. I have not verified whether this specialization is already recorded in the full paper.

---

## 3. Random lower bound

Color all edges of \(K_N\square K_N\) independently and uniformly with two colors.

Fix \(A\in\binom Xn\) and \(B\in\binom Yn\). In the weak line-by-line version, the target contains \(2n\) edge-disjoint copies of \(K_n\): \(n\) horizontal lines and \(n\) vertical lines. A randomly colored \(K_n\) is monochromatic with probability
\[
2^{1-\binom n2}.
\]
Therefore
\[
\Pr(A\times B\text{ is weakly directionally monochromatic})
=
2^{-2n(\binom n2-1)}.
\]
Hence the expected number of such subproducts is at most
\[
\binom Nn^2\,2^{-2n(\binom n2-1)}.
\tag{8}
\]

Take
\[
N=\left\lfloor 2^{(1/2-\varepsilon)n^2}\right\rfloor
\]
for fixed \(\varepsilon>0\). Using \(\binom Nn\le(eN/n)^n\), the binary logarithm of (8) is at most
\[
2n\log_2(eN/n)-2n\left(\binom n2-1\right)
=
-2\varepsilon n^3+O(n^2),
\]
which is negative for sufficiently large \(n\). Thus some coloring contains no weakly directionally monochromatic canonical subproduct, proving (6).

For the strong version, the probability for a fixed \(A\times B\) is even smaller:
\[
4\cdot 2^{-2n\binom n2}
=
2^{2-n^2(n-1)}.
\]

---

## 4. A monochromatic-clique multiplicity lemma

The upper bound uses the following elementary supersaturation observation.

### Lemma

Let \(t\ge2\), let \(M\ge r_2(t)\), and color \(E(K_M)\) with two colors. The number of monochromatic \(t\)-sets is at least
\[
\frac{\binom Mt}{\binom{r_2(t)}t}.
\tag{9}
\]

### Proof

Put \(R=r_2(t)\). Every \(R\)-subset contains a monochromatic \(t\)-subset. Count pairs \((U,A)\) where
\[
A\subseteq U,\qquad |A|=t,\quad |U|=R,
\]
and \(A\) is monochromatic. There are at least \(\binom MR\) such pairs. If there are \(L\) monochromatic \(t\)-sets, there are exactly
\[
L\binom{M-t}{R-t}
\]
such pairs. Hence
\[
L\binom{M-t}{R-t}\ge\binom MR,
\]
and the quotient is
\[
L\ge
\frac{\binom MR}{\binom{M-t}{R-t}}
=
\frac{\binom Mt}{\binom Rt}.
\qedhere
\]

---

## 5. Proof of the upper bound

Set
\[
m=2n-1,\qquad R=r_2(m),\qquad q=2^m.
\]
Suppose
\[
N\ge 2\binom Rm\,r_q(n).
\tag{10}
\]

For every row \(y\in Y\), apply the lemma to the coloring \(H_y\). Thus \(H_y\) has at least
\[
\frac{\binom Nm}{\binom Rm}
\]
monochromatic \(m\)-sets.

Count triples \((y,A,\alpha)\) such that
\[
y\in Y,\quad A\in\binom Xm,\quad \alpha\in\{0,1\},
\]
and \(H_y\) is constantly \(\alpha\) on \(\binom A2\). There are at least
\[
N\frac{\binom Nm}{\binom Rm}
\]
such triples. Since there are \(2\binom Nm\) possible pairs \((A,\alpha)\), some \(A\in\binom Xm\) and some color \(\alpha\) have a supporting set
\[
S=\{y\in Y:H_y|_{\binom A2}\equiv\alpha\}
\]
of size at least
\[
|S|\ge \frac{N}{2\binom Rm}\ge r_q(n).
\tag{11}
\]

Now color every pair \(yy'\in\binom S2\) by the vector
\[
\mathbf c(yy')
=
\bigl(V_x(yy')\bigr)_{x\in A}
\in\{0,1\}^A.
\]
There are \(q=2^m\) possible vectors. By (11) and the definition of \(r_q(n)\), there is \(B\in\binom Sn\) and a fixed vector
\[
\mathbf w=(w_x)_{x\in A}
\]
such that
\[
V_x(yy')=w_x
\quad
\text{for every }x\in A,\ yy'\in\binom B2.
\tag{12}
\]

Because \(|A|=2n-1\), at least \(n\) coordinates of \(\mathbf w\) have the same value, say \(\beta\). Let \(A'\subseteq A\) be \(n\) such coordinates. Then:

- because \(B\subseteq S\), every horizontal edge of \(A'\times B\) has color \(\alpha\);
- by (12), every vertical edge of \(A'\times B\) has color \(\beta\).

Thus \(A'\times B\) is strongly directionally monochromatic. This proves (3).

### Numerical estimate

The elementary graph Ramsey bounds
\[
r_2(m)\le\binom{2m-2}{m-1}<4^m
\]
and
\[
r_q(n)
\le
\binom{q(n-1)}{n-1,\ldots,n-1}
\le q^{q(n-1)}
\tag{13}
\]
give
\[
\binom{r_2(m)}m\le 2^{2m^2}
\]
and, with \(q=2^m\),
\[
r_q(n)\le 2^{m(n-1)2^m}.
\]
Consequently
\[
\log_2 R_2^{\mathrm{str}}(2,n)
\le
1+2m^2+m(n-1)2^m
=
O(n^2 4^n),
\]
which is (4).

For the weak line-by-line version, one takes \(m=n\), does not pigeonhole a common horizontal color, and does not need the final majority step. This gives (5).

The same argument works for fixed \(r\): taking \(m=r(n-1)+1\),
\[
R_r^{\mathrm{str}}(2,n)
\le
r\binom{r_r(m)}m\,r_{r^m}(n).
\tag{14}
\]

---

## 6. A direct relation to 3-uniform Ramsey numbers

There is also a useful structural reduction. Let \(r_q^{(3)}(t)\) denote the \(q\)-color Ramsey number for 3-uniform complete hypergraphs.

Identify \(X\) and \(Y\) with two copies of \([N]\). For each \(i<j<k\), define a four-coloring of triples by
\[
\Psi(i,j,k)
=
\bigl(H_k(ij),\,V_i(jk)\bigr)
\in\{0,1\}^2.
\tag{15}
\]
If \(N\ge r_4^{(3)}(2n)\), there is
\[
S=\{s_1<\cdots<s_{2n}\}
\]
on which \(\Psi\) is constant, say equal to \((\alpha,\beta)\). Set
\[
A=\{s_1,\ldots,s_n\}\subseteq X,\qquad
B=\{s_{n+1},\ldots,s_{2n}\}\subseteq Y.
\]
For \(i<j\) in \(A\) and \(k\in B\), equation (15) gives
\[
H_k(ij)=\alpha.
\]
For \(i\in A\) and \(j<k\) in \(B\), it gives
\[
V_i(jk)=\beta.
\]
Thus
\[
R_2^{\mathrm{str}}(2,n)\le r_4^{(3)}(2n).
\tag{16}
\]

A standard vertex-exposure argument proves directly that, for fixed \(q\),
\[
r_q^{(3)}(t)\le 2^{2^{O_q(t)}}.
\]
Indeed, construct an ordered sequence \(v_1,\ldots,v_M\) such that the color of \(\{v_i,v_j,v_k\}\), for \(i<j<k\), is determined by \(i,j\). This requires at most a factor \(q^{j-1}\) loss at the \(j\)-th step. Taking
\[
M=r_q(t-1)+1=2^{O_q(t)}
\]
then produces a homogeneous \(t\)-set. This gives another proof of a bound \(2^{2^{O(n)}}\) for \(d=2\).

Moreover, any coloring with no desired grid gives through (15) a four-color 3-uniform coloring with no homogeneous \(2n\)-set. Therefore any lower bound of the form
\[
R_2(2,n)\ge 2^{\omega(n^2)}
\]
would simultaneously give
\[
r_4^{(3)}(2n)\ge 2^{\omega(n^2)}.
\]
This is not a converse, but it shows that an improvement beyond the first-moment \(2^{\Theta(n^2)}\) scale would have consequences for ordinary 3-uniform Ramsey lower bounds.

---

## 7. Why the upper-bound method remains double exponential

The vector-coloring step is not merely an artifact of a loose bound. The elementary construction
\[
r_q(n)>(n-1)^q
\tag{17}
\]
shows that simultaneous Ramsey problems for \(q\) colors can genuinely be enormous.

To prove (17), take vertex set \([n-1]^q\) and color a pair of distinct words by the first coordinate in which they differ. In a clique of color \(i\), all words agree before coordinate \(i\), while their \(i\)-th coordinates must be pairwise distinct. Thus such a clique has size at most \(n-1\).

For \(q=2^{2n-1}\), the right side of (17) is already doubly exponential in \(n\). Hence an argument which first freezes a set \(A\) and then treats all vertical color vectors as arbitrary \(q\)-colors cannot yield a singly exponential bound. A resolution would have to exploit the availability of many possible choices of \(A\), rather than freezing one and solving an arbitrary simultaneous Ramsey problem on its support.

---

## 8. What remains open and the terminology issue

Under the usual analytic definition,
\[
f(n)\text{ is superexponential}
\quad\Longleftrightarrow\quad
\frac{\log f(n)}n\longrightarrow\infty,
\]
the random lower bound (6) already answers the literal question affirmatively:
\[
\frac{\log R_2(2,n)}n\ge (1/2-o(1))n\log 2\longrightarrow\infty.
\]

Thus “superexponential” in Problem 4.1 cannot be read in that conventional \(C^n\) sense if the canonical definition is intended. The meaningful open alternatives appear to be one of:

1. whether
   \[
   R_2(2,n)\le 2^{n^{O(1)}}
   \]
   is possible; or

2. on the natural random-coloring scale, whether
   \[
   R_2(2,n)\ge 2^{\omega(n^2)}.
   \]

Neither is resolved here. The rigorous progress is the specialization
\[
R_2(2,n)\le 2^{2^{2n+O(\log n)}},
\]
together with the explicit reduction to four-color 3-uniform Ramsey and the identification of the simultaneous-Ramsey obstruction.