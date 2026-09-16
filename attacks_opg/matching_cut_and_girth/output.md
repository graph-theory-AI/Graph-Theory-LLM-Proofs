```json
{
  "verdict": "disproved",
  "confidence": "high",
  "one_line": "For every girth bound there is a simple 7-regular graph with no matching cut, so d = 8 refutes the universal assertion.",
  "would_publish": false,
  "caveats": "Matching cuts are understood to use nonempty proper vertex sets; no novelty or optimal degree threshold is claimed."
}
```

## 1. Statement

The assertion is false. The obstruction is edge expansion.

I will prove, without relying on the literature claims in the prompt, the following.

**Theorem.** For every integer \(g\ge 3\), there exists a finite simple \(7\)-regular graph \(G\) of girth at least \(g\) such that
\[
|\delta_G(S)|>|S|
\qquad
\text{whenever }1\le |S|\le |V(G)|/2,
\tag{1}
\]
where \(\delta_G(S)=E(S,V(G)\setminus S)\). In particular, \(G\) has no matching cut.

Indeed, if \(\delta_G(S)\) were a matching, then, after choosing the smaller side of the cut,
\[
|\delta_G(S)|\le |S|,
\]
contrary to (1). Since \(\overline d(G)=7<8\), these graphs disprove the question at \(d=8\), and in fact at every \(d>7\).

The proof uses a fully specified random regular graph model. We show that (1) holds with probability tending to one, while, for every fixed \(g\), simplicity and girth at least \(g\) have probability bounded away from zero.

## 2. Random \(7\)-regular graphs have the required expansion

Let \(n\) tend to infinity through even integers. Give each of \(n\) labelled vertices seven labelled half-edges, and choose a uniformly random perfect matching of the \(7n\) half-edges. This produces a \(7\)-regular multigraph, initially allowing loops and parallel edges.

For \(1\le s\le n/2\), let \(B_s\) count the vertex sets \(S\) satisfying
\[
|S|=s,\qquad |\delta(S)|\le s.
\]
Such a set has at least
\[
\frac{7s-s}{2}=3s
\]
edges entirely inside it. Consequently, some set of \(6s\) of its half-edges is paired entirely within itself.

For a specified set of \(6s\) half-edges, the probability of this event is
\[
p_{n,s}
=
\frac{(6s-1)!!(7n-6s-1)!!}{(7n-1)!!}
=
\frac{\binom{7n/2}{3s}}{\binom{7n}{6s}}.
\]
A union bound therefore gives
\[
\mathbb E B_s
\le
\binom ns\binom{7s}{s}p_{n,s}.
\tag{2}
\]

We estimate (2) separately for small and large \(s\).

### Small sets

The product formula gives
\[
p_{n,s}
=
\prod_{j=0}^{3s-1}
\frac{6s-2j-1}{7n-2j-1}
\le
\left(\frac{s}{n}\right)^{3s}.
\]
Using \(\binom ab\le(ea/b)^b\), we obtain
\[
\mathbb E B_s
\le
\left[
7e^2\left(\frac{s}{n}\right)^2
\right]^s.
\]
Hence
\[
\sum_{1\le s\le\sqrt n}\mathbb E B_s
\le
\sum_{s\ge1}\left(\frac{7e^2}{n}\right)^s
=o(1).
\tag{3}
\]

### Large sets

Write
\[
H(x)=-x\log x-(1-x)\log(1-x),
\]
with the usual continuous definitions at \(0\) and \(1\). We use the elementary bounds
\[
\frac{1}{M+1}e^{M H(K/M)}
\le \binom MK
\le e^{M H(K/M)}.
\]
Putting \(x=s/n\) in (2) yields
\[
\mathbb E B_s
\le
(7n+1)\exp\!\bigl(nF(x)\bigr),
\tag{4}
\]
where
\[
F(x)
=
H(x)+7xH(1/7)-\frac72 H(6x/7).
\]

For \(0<x\le1/2\),
\[
F''(x)
=
\frac1x
\left(
\frac{3}{1-6x/7}-\frac{1}{1-x}
\right)>0.
\]
Thus \(F\) is convex on \([0,1/2]\). Moreover,
\[
F(0)=0,
\qquad
F(1/2)=\frac12\log\frac{16}{27}<0.
\]
A convex function lies below the chord joining two points of its graph, so
\[
F(x)\le x\log\frac{16}{27}
\qquad(0\le x\le1/2).
\]
Consequently, (4) implies
\[
\sum_{\sqrt n<s\le n/2}\mathbb E B_s
\le
(7n+1)\sum_{s>\sqrt n}\left(\frac{16}{27}\right)^s
=o(1).
\tag{5}
\]

Combining (3) and (5),
\[
\mathbb P\!\left(
\exists S:\ 1\le |S|\le n/2,\ |\delta(S)|\le |S|
\right)
\le \sum_{s=1}^{n/2}\mathbb E B_s
=o(1).
\tag{6}
\]
Thus the expansion property (1) holds with probability tending to one.

## 3. Arbitrarily large fixed girth is compatible with this expansion

Fix \(g\ge3\). In the same configuration model, let \(X\) count cycles of lengths \(1,\ldots,g-1\), where:

- a loop is a cycle of length \(1\);
- a pair of parallel edges is a cycle of length \(2\);
- longer cycles have distinct vertices and are counted without orientation.

Then \(X=0\) means precisely that the resulting graph is simple and has girth at least \(g\).

We will establish
\[
\mathbb P(X=0)
\longrightarrow
e^{-\lambda}>0,
\qquad
\lambda=\sum_{\ell=1}^{g-1}\frac{6^\ell}{2\ell}.
\tag{7}
\]

Here are the counting details, including the justification for the positive limiting probability.

For any fixed \(k\), expand the factorial moment \(\mathbb E[(X)_k]\) over ordered \(k\)-tuples of distinct cycles. For prescribed lengths
\(\ell_1,\ldots,\ell_k\), let \(L=\ell_1+\cdots+\ell_k\). The contribution from vertex-disjoint cycles is
\[
\frac{
(n)_L\,42^L
}{
\left(\prod_{i=1}^k2\ell_i\right)
\left(\prod_{j=0}^{L-1}(7n-2j-1)\right)
}
\longrightarrow
\prod_{i=1}^k\frac{6^{\ell_i}}{2\ell_i}.
\tag{8}
\]
The factor \(42=7\cdot6\) chooses the two ordered half-edges used at each cycle vertex.

The contribution from overlapping cycles is \(O(n^{-1})\). To see this, consider a consistent union of such cycles with \(v\) vertices and \(e\) edges. Every component contains a cycle, and at least one component contains two distinct cycles. Therefore \(e\ge v+1\). There are \(O(n^v)\) choices of its vertices and half-edges, while its prescribed pairings occur with probability \(O(n^{-e})\). For fixed \(g\) and \(k\), there are only finitely many union types.

Summing (8) over the possible lengths consequently gives
\[
\mathbb E[(X)_k]\longrightarrow \lambda^k.
\]

For completeness, these moment limits imply (7) directly by Bonferroni inequalities. For every integer \(m\ge0\),
\[
\sum_{j=0}^{2m+1}\frac{(-1)^j}{j!}\mathbb E[(X)_j]
\le \mathbb P(X=0)
\le
\sum_{j=0}^{2m}\frac{(-1)^j}{j!}\mathbb E[(X)_j].
\]
First let \(n\to\infty\), and then let \(m\to\infty\). Both bounding sums converge to \(e^{-\lambda}\), proving (7).

Crucially, \(g\) was fixed before \(n\) tended to infinity. The positive constant in (7) may be very small, but it is independent of \(n\).

## 4. Combining the properties

Let \(\mathcal E_n\) be the expansion event (1). By (6) and (7),
\[
\mathbb P\bigl(\mathcal E_n\cap\{X=0\}\bigr)
\ge
\mathbb P(X=0)-\mathbb P(\mathcal E_n^c)
=
e^{-\lambda}-o(1)>0
\]
for all sufficiently large even \(n\).

Therefore, for every fixed \(g\), some configuration gives a simple \(7\)-regular graph of girth at least \(g\) satisfying (1). Such a graph has no matching cut. It is also connected, since (1) excludes a nontrivial cut of size zero.

This proves the theorem and disproves the proposed universal statement. No case concerning the requested counterexample family is left open; the proof makes no assertion about the optimal degree threshold or about \(d\le7\).

## 5. The catalog’s logical issue

The supplied review’s concern that the exact average degrees of its asserted maximum-degree-\(60\) NO-instances are unknown is not an obstacle. Every such graph satisfies
\[
\overline d(G)\le\Delta(G)\le60<61.
\]
Thus, **if the bounded-degree hardness result is as quoted**, its promised NO-instances for every fixed girth bound already refute the universal assertion at \(d=61\). No assumption such as \(\mathrm P\ne\mathrm{NP}\) is needed: a reduction applied to an unsatisfiable source instance supplies a NO-instance.

The self-contained construction above is independent of that literature claim and gives the stronger counterexample degree \(7\).