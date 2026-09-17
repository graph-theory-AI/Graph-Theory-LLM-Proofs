```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A signed-minor argument establishes Hamiltonian extendability for matchings whose alternating cycles are all 4-cycles, including all uniquely restricted matchings.",
  "would_publish": false,
  "caveats": "The unrestricted conjecture is not resolved, and novelty of these special cases is not claimed."
}
```

## 1. Partial result

Write \(Q_d\) for the graph on \(\{0,1\}^d\), with adjacency given by changing one coordinate. Throughout, \(d\ge 2\).

An **\(M\)-alternating cycle** is a cycle whose edges alternate between belonging and not belonging to \(M\). A matching is **uniquely restricted** if it is the unique perfect matching of the subgraph induced by its endpoints; equivalently, it has no alternating cycle.

The following is the partial result established here.

**Theorem.** Let \(M\) be a matching of \(Q_d\). If every \(M\)-alternating cycle has length \(4\), then \(M\) extends to a perfect matching, and consequently to a Hamiltonian cycle.

In particular, every uniquely restricted matching extends to a Hamiltonian cycle.

The Hamiltonian conclusion uses Fink’s perfect-matching theorem stated in the question. The completion-to-a-perfect-matching argument below is self-contained.

There is also a quantitative consequence.

**Corollary.** If \(M\) is uniquely restricted and \(m=|M|\), then
\[
m\le 2^{d-2},
\]
and \(M\) is contained in at least
\[
d^{\,2^{d-2}-m}
\]
perfect matchings of \(Q_d\). The bound \(2^{d-2}\) on \(m\) is sharp.

These statements do not handle all matchings: already in \(Q_3\), a matching can fail to have any perfect-matching completion while still extending to a Hamiltonian cycle.

## 2. An orthogonal signing of the cube

Let \(E\) and \(O\) be the even- and odd-parity vertices of \(Q_d\), respectively, and put
\[
N=|E|=|O|=2^{d-1}.
\]

For an edge \(e=xx^{(i)}\), where \(x^{(i)}\) is obtained by changing coordinate \(i\), define
\[
s(e)=(-1)^{x_1+\cdots+x_{i-1}}.
\]
This is well-defined because changing coordinate \(i\) does not change the exponent.

Let \(A\) be the \(N\times N\) signed biadjacency matrix, with rows indexed by \(E\), columns by \(O\), and entries
\[
A_{xy}=
\begin{cases}
s(xy),&xy\in E(Q_d),\\
0,&\text{otherwise}.
\end{cases}
\]

We have
\[
AA^{\mathsf T}=dI_N. \tag{1}
\]

Indeed, every row has exactly \(d\) nonzero entries, all equal to \(\pm1\). Two distinct even vertices have common neighbors only when their distance is two. In that case there are exactly two common neighbors, corresponding to changing two coordinates in opposite orders. The resulting two contributions to their row inner product have opposite signs.

Thus
\[
A^{-1}=\frac1d A^{\mathsf T},
\qquad
|\det A|=d^{N/2}. \tag{2}
\]

The same cancellation also shows that, for every square \(C\) of the cube,
\[
\prod_{e\in E(C)}s(e)=-1. \tag{3}
\]

## 3. Complementary minors and perfect-matching completion

Let \(X\subseteq E\) and \(Y\subseteq O\) be the endpoints of \(M\), so that
\[
|X|=|Y|=m.
\]
Their complements consist of the vertices not covered by \(M\).

Jacobi’s complementary-minor identity, together with (2), gives
\[
\begin{aligned}
\bigl|\det A[X^c,Y^c]\bigr|
&=|\det A|\,
  \bigl|\det A^{-1}[Y,X]\bigr|\\
&=d^{N/2-m}\bigl|\det A[X,Y]\bigr|.
\end{aligned} \tag{4}
\]
Here an empty determinant is interpreted as \(1\).

In particular,
\[
\det A[X,Y]\ne0
\quad\Longrightarrow\quad
\det A[X^c,Y^c]\ne0. \tag{5}
\]

A nonzero determinant of \(A[X^c,Y^c]\) implies that its determinant expansion has a nonzero term. Such a term is a perfect matching of the graph induced by the uncovered vertices. Adding that perfect matching to \(M\) gives a perfect matching of \(Q_d\).

We have therefore proved the following sufficient condition:

> **Signed-minor criterion.** If the signed biadjacency matrix on the endpoints of \(M\) is nonsingular, then \(M\) extends to a perfect matching.

Nonsingularity is sufficient, not necessary: determinant terms can cancel even when the corresponding graph has perfect matchings.

## 4. Alternating squares prevent cancellation

Consider the determinant expansion of \(A[X,Y]\). Its nonzero terms correspond exactly to perfect matchings of \(Q_d[X\cup Y]\), one of which is \(M\).

For an \(M\)-alternating cycle \(C\) of length \(2k\), switching \(M\) along \(C\) changes the sign of its determinant term by the factor
\[
\varepsilon(C)
=
(-1)^{k-1}\prod_{e\in E(C)}s(e). \tag{6}
\]
The first factor is the sign of the associated \(k\)-cycle in the matching permutation; the second accounts for the signed matrix entries.

If \(C\) is a square, then \(k=2\), and (3) yields
\[
\varepsilon(C)=(-1)(-1)=1. \tag{7}
\]

Now suppose every \(M\)-alternating cycle has length four. For any perfect matching \(P\) of \(Q_d[X\cup Y]\), the symmetric difference
\[
M\triangle P
\]
is a vertex-disjoint union of \(M\)-alternating cycles. By hypothesis, all these cycles are squares. Switching them therefore leaves the determinant-term sign unchanged.

Consequently, **all nonzero terms in \(\det A[X,Y]\) have the same sign**. There is at least one such term, namely \(M\), so
\[
\det A[X,Y]\ne0.
\]
The signed-minor criterion gives a perfect matching containing \(M\). Fink’s theorem then gives a Hamiltonian cycle containing that perfect matching, and hence containing \(M\). This proves the theorem.

The proof actually establishes the slightly broader condition
\[
\varepsilon(C)=1
\quad\text{for every \(M\)-alternating cycle \(C\)}. \tag{8}
\]
Thus any matching that does not extend to a perfect matching must have an alternating cycle with \(\varepsilon(C)=-1\). In particular, it must have an alternating cycle of length at least six.

## 5. Uniquely restricted matchings: a sharp bound

Suppose \(M\) is uniquely restricted. Then the determinant expansion of \(A[X,Y]\) has exactly one nonzero term, so
\[
\bigl|\det A[X,Y]\bigr|=1.
\]
Equation (4) becomes
\[
\bigl|\det A[X^c,Y^c]\bigr|
=d^{N/2-m}. \tag{9}
\]

The left side is a positive integer. Since \(d\ge2\), the right side would lie strictly between zero and one if \(m>N/2\). Hence
\[
m\le N/2=2^{d-2}.
\]

Moreover, each perfect matching of the uncovered-vertex graph contributes either \(1\) or \(-1\) to its signed determinant. Its number of perfect matchings is therefore at least the absolute determinant in (9). These are precisely the perfect-matching completions of \(M\), proving the stated lower bound.

To attain the size bound, write vertices as \((b,z)\in\{0,1\}\times\{0,1\}^{d-1}\), and take
\[
M_*=
\left\{
(0,z)(1,z):
\sum_{j=1}^{d-1}z_j\equiv0\pmod2
\right\}.
\]
There are \(2^{d-2}\) such edges. Distinct even-parity strings \(z\) have distance at least two, so no edge joins endpoints of different members of \(M_*\). Thus \(M_*\) is induced, hence uniquely restricted.

The uniquely restricted condition is also readily recognizable: contract the matching edges conceptually, and put an arc from matching edge \(e\) to matching edge \(f\) whenever the even endpoint of \(e\) is adjacent to the odd endpoint of \(f\), excluding \(e=f\). Directed cycles correspond exactly to alternating cycles. Thus a directed-cycle test recognizes this special case once the graph is given explicitly.

## 6. The unresolved obstruction

The argument works by completing \(M\) to a perfect matching. That route genuinely fails for some matchings.

For example, in \(Q_3\), take
\[
M=\{001\,011,\;010\,110,\;100\,101\}.
\]
Its uncovered vertices are \(000\) and \(111\), which are nonadjacent. Therefore \(M\) has no perfect-matching completion.

Its saturated vertices induce the alternating six-cycle
\[
001,011,010,110,100,101,001.
\]
Nevertheless, \(M\) lies in the Hamiltonian cycle
\[
000,001,011,010,110,111,101,100,000.
\]

This example is not a counterexample to Ruskey–Savage. It shows exactly why the perfect-completion argument cannot resolve the conjecture: a successful general proof must also accommodate matchings with no perfect-matching completion.

**Conclusion.** The signed-minor method proves the stated special cases and the sharp bound for uniquely restricted matchings. It does not prove or disprove Hamiltonian extendability for arbitrary matchings. No novelty claim is made for these partial results.