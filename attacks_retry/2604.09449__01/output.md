```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I prove exact balance for every single binary coarsening, including zero imbalance for k=2, but not simultaneous constant-error balance for arbitrarily many colours.",
  "would_publish": false,
  "caveats": "The multicolour conjecture remains unresolved; no novelty claim is made for the binary result."
}
```

# 1. Statement and partial result

For a colour-balanced \(k\)-colouring of \(K_{2kt}\), write
\[
m_i(M)=|\{e\in M:c(e)=i\}|.
\]
I use the recolouring-distance normalization
\[
f_c(M)=\sum_{i=1}^k(m_i(M)-t)_+
      =\frac12\sum_{i=1}^k|m_i(M)-t|.
\]
If the source uses the unhalved \(L^1\)-quantity, the exact-balance conclusions below are unchanged.

The main partial result is stronger than the binary bound in the supplied attempt.

**Theorem 1.** Let \(c\) be a colour-balanced \(k\)-colouring of \(K_{2kt}\). For every subset \(I\subseteq[k]\), there is a perfect matching \(M_I\) such that
\[
\sum_{i\in I}m_i(M_I)=|I|t.
\tag{1}
\]
In particular, every colour-balanced two-colouring of \(K_{4t}\) has an exactly colour-balanced perfect matching:
\[
\min_M f_c(M)=0\qquad(k=2).
\tag{2}
\]

The matching in (1) is allowed to depend on \(I\). That dependence is the unresolved obstacle: this does not give simultaneous balance for all colours.

I prove Theorem 1 through a parity-interpolation statement for binary edge-colourings. The argument is constructive and gives a quadratic-time algorithm for the binary conclusion.

# 2. Parity interpolation for perfect matchings

Consider an arbitrary red/blue colouring of \(K_{2m}\). Let \(E_R\) be its set of red edges and put
\[
r(M)=|M\cap E_R|.
\]

**Theorem 2 — parity interpolation.** Suppose \(a\) is an integer satisfying
\[
\min_{M\text{ perfect}}r(M)\le a\le
\max_{M\text{ perfect}}r(M),
\qquad
a\equiv |E_R|\pmod 2.
\tag{3}
\]
Then some perfect matching has exactly \(a\) red edges.

Notice that this does **not** assume that all perfect matchings have red counts of the same parity.

## Proof

A *switch* replaces two matching edges \(xx',yy'\) by either
\[
xy,x'y'
\quad\text{or}\quad
xy',x'y.
\]
The graph of perfect matchings under these switches is connected. Indeed, to move towards a prescribed perfect matching \(Q\), choose \(xy\in Q\setminus P\). If \(P\) matches \(x\) to \(x'\) and \(y\) to \(y'\), replacing \(xx',yy'\) by \(xy,x'y'\) increases \(|P\cap Q|\).

A switch changes the red count by at most two.

Suppose, for a contradiction, that no perfect matching has \(a\) red edges. By (3), there are matchings with red counts below and above \(a\). Along a switch path between them, there must therefore be consecutive matchings \(P,Q\) with
\[
r(P)=a-1,\qquad r(Q)=a+1.
\tag{4}
\]
The switch from \(P\) to \(Q\) removes two blue edges and adds two red edges.

Let \(S\) be the four vertices involved in this switch, and let
\[
R=P\cap Q.
\]
Thus \(R\) is a perfect matching of the vertices outside \(S\), and
\[
r(R)=a-1.
\tag{5}
\]

For two disjoint edges \(e,f\), let \(\Gamma(e,f)\) denote the four edges between their endpoint sets. These four edges split into the two alternative pairings of those endpoints.

We will show that every part of the graph except the individual edges of \(R\) contains an even number of red edges.

### A. Edges inside \(S\)

The six edges of \(K_S\) split into its three perfect matchings. The pairing used by \(P\) has no red edges, and the pairing used by \(Q\) has two.

The third pairing cannot have exactly one red edge: together with \(R\), it would give a perfect matching with \(a\) red edges. Thus
\[
|E_R\cap E(K_S)|\equiv0\pmod2.
\tag{6}
\]

### B. Edges between two different edges of \(R\)

Take distinct \(e,f\in R\).

* If both are blue, each alternative pairing must have zero or two red edges. A pairing with one red edge, substituted into \(P\), would give red count \(a\). Consequently \(\Gamma(e,f)\) contains an even number of red edges.

* If both are red, the same conclusion follows using \(Q\): replacing them by a pairing with one red edge would reduce its red count to \(a\).

* If one is red and the other blue, an alternative pairing cannot have two red edges, by applying the switch to \(P\). It also cannot have zero red edges, by applying it to \(Q\). Hence both alternative pairings have exactly one red edge, and \(\Gamma(e,f)\) has exactly two.

In every case,
\[
|E_R\cap\Gamma(e,f)|\equiv0\pmod2.
\tag{7}
\]

### C. Edges between \(S\) and an edge of \(R\)

Fix \(e\in R\).

If \(e\) is blue, partition \(S\) into the two blue edges of \(P\). For each such edge \(f\), the same blue–blue argument used above shows that \(\Gamma(e,f)\) has an even number of red edges. These two sets partition the edges between \(V(e)\) and \(S\).

If \(e\) is red, instead partition \(S\) into the two red edges of \(Q\), and use the red–red argument.

Thus, in either case,
\[
|E_R\cap E(S,V(e))|\equiv0\pmod2.
\tag{8}
\]

### D. Counting all red edges modulo two

The edges of \(K_{2m}\) partition into:

1. the edges inside \(S\);
2. the individual matching edges of \(R\);
3. the edges between distinct endpoint blocks of \(R\);
4. the edges between \(S\) and those blocks.

By (6)–(8), only the second part contributes to the parity of the total. Therefore
\[
|E_R|\equiv r(R)\equiv a-1\pmod2,
\]
contrary to (3). This proves the theorem. \(\square\)

# 3. An integer mean-value theorem

**Corollary 3.** If a red/blue colouring of \(K_{2m}\) has exactly
\[
a(2m-1)
\]
red edges, where \(a\) is an integer, then it has a perfect matching with exactly \(a\) red edges.

## Proof

In a uniformly random perfect matching, every edge is present with probability \(1/(2m-1)\). Hence
\[
\mathbb E\,r(M)=\frac{|E_R|}{2m-1}=a,
\]
so \(a\) lies between the minimum and maximum red counts.

Furthermore, \(2m-1\) is odd, and therefore
\[
|E_R|=a(2m-1)\equiv a\pmod2.
\]
Theorem 2 applies. \(\square\)

## Proof of Theorem 1

Put \(m=kt\). Each original colour class has
\[
\frac{\binom{2kt}{2}}{k}=t(2kt-1)
\]
edges.

Colour an edge red precisely when its original colour belongs to \(I\). The number of red edges is
\[
|I|t(2kt-1).
\]
Applying Corollary 3 with \(a=|I|t\) gives (1).

For \(k=2\), taking \(I\) to consist of one colour gives exactly \(t\) matching edges of that colour. The matching has \(2t\) edges, so it also has exactly \(t\) of the other colour. This proves (2). \(\square\)

# 4. Constructive consequence

The binary mean-value result admits an \(O(m^2)\)-time algorithm, given the colour matrix of \(K_{2m}\).

First, use the following explicit one-factorization. Identify the vertices with
\[
\{\infty\}\cup\mathbb Z_{2m-1}.
\]
For \(j\in\mathbb Z_{2m-1}\), let
\[
F_j=\{\infty j\}\cup
\bigl\{\{j+x,j-x\}:1\le x\le m-1\bigr\},
\]
where arithmetic is modulo \(2m-1\). These \(2m-1\) perfect matchings partition all edges.

When \(|E_R|=a(2m-1)\), their average red count is \(a\). Thus:

1. If some \(F_j\) has red count \(a\), return it.
2. Otherwise choose factors with red counts below and above \(a\), and connect them by the switch procedure from the proof.
3. If the path hits \(a\), return that matching. Otherwise it contains consecutive matchings \(P,Q\) with counts \(a-1,a+1\).
4. Examine all single-switch neighbours of \(P\) and \(Q\).

The last step must find red count \(a\). Indeed, every forbidden matching used in the parity proof is a single-switch neighbour of \(P\) or \(Q\). If none of those neighbours had count \(a\), that proof would give the same parity contradiction.

Computing the factor counts takes \(O(m^2)\) time; the path has at most \(m-1\) switches; and there are \(O(m^2)\) neighbours to inspect, each with a constant-time red-count update.

This is an algorithmic consequence, not a claim of an executed computational check.

# 5. The remaining multicolour problem

The shade-splitting and rainbow-matching reduction in the supplied attempt checks out. I include it to state exactly what remains unproved.

## Reduction to \(t=1\)

Set \(n=kt\). Each original colour class has \(t(2n-1)\) edges. Partition it into \(t\) shades of size \(2n-1\). This produces a colour-balanced \(n\)-colouring \(\widetilde c\) of \(K_{2n}\).

For a perfect matching \(M\), let \(m_{i,j}(M)\) count its edges of shade \((i,j)\). Then
\[
\begin{aligned}
f_c(M)
&=\frac12\sum_i
 \left|\sum_{j=1}^t(m_{i,j}(M)-1)\right|\\
&\le \frac12\sum_{i,j}|m_{i,j}(M)-1|
=f_{\widetilde c}(M).
\end{aligned}
\tag{9}
\]
Consequently, an absolute bound for \(t=1\) would imply the conjecture for every \(k,t\). The converse is immediate.

## Rainbow deficiency

For an \(n\)-colouring of \(K_{2n}\) with target one edge of each colour, let \(d(M)\) be the number of colours represented in \(M\). Then
\[
f_c(M)=n-d(M).
\tag{10}
\]
Let \(\rho(c)\) be the maximum size of a rainbow matching.

Selecting one edge of every represented colour gives a rainbow submatching, so \(d(M)\le\rho(c)\). Conversely, every rainbow matching extends to a perfect matching of the complete graph. Hence
\[
\min_{M\text{ perfect}} f_c(M)=n-\rho(c).
\tag{11}
\]

Thus the original conjecture is equivalent to bounding
\[
n-\rho(c)
\]
by an absolute constant over all colourings of \(K_{2n}\) with \(n\) colour classes, each of size \(2n-1\).

# 6. Gap and conclusion

The proved improvement is:

> Every individual binary aggregation of the colours can be balanced **exactly**, rather than merely within one edge.

In particular, the conjecture holds with zero imbalance for \(k=2\), for every \(t\).

However, the switches used in the proof control only one binary statistic. They need not preserve the counts of any other colours. Consequently, the argument cannot simply be iterated over colour subsets: the witnesses \(M_I\) in (1) may all be different.

I obtain neither an absolute bound on the rainbow deficiency in (11) nor an unbounded-deficiency construction. The simultaneous multicolour conjecture therefore remains unresolved by this attack.