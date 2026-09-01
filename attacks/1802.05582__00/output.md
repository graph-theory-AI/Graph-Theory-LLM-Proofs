```json
{
  "verdict": "proved",
  "confidence": "medium",
  "one_line": "In the intended deterministic LOCAL formulation, a high-degree-component decomposition gives a second algorithm running in O(n/d+polylog n) rounds, which combined with the quoted d-dependent algorithm yields a uniform o(n) bound.",
  "would_publish": false,
  "caveats": "This assumes the source's hereditary list-colorable setting and d>=3; the catalog's literal all-d degeneracy paraphrase includes a false two-coloring case."
}
```

# 1. Precise statement

The catalog prose is not a fully quantified conjecture. The source-style formulation associated with the quoted running time is the following.

> **Source-style problem.** In the deterministic LOCAL model, list-color an \(n\)-vertex graph \(G\) from lists of size at least \(d\), where \(d\ge 3\) and
> \[
> \operatorname{mad}(G):=\max_{\varnothing\ne H\subseteq G}\frac{2|E(H)|}{|V(H)|}<d.
> \]
> The source gives \(O(d^{4}\log ^3 n)\) rounds. Find a bound \(o(n)\) which is uniform in \(d\).

The same argument applies to the catalog's \(d\)-degenerate/\((1+\varepsilon)d\)-color formulation whenever its quoted small-\(d\) algorithm is valid. The essential parameter below is the actual number \(q\) of available colors, with \(q=\Theta(d)\).

I prove the following stronger wrapper theorem.

> **Theorem.** Let an \(n\)-vertex list-coloring instance have lists of size at least \(q\), and suppose the instance is list-colorable. In the deterministic LOCAL model it can be solved in
> \[
> O\!\left(\frac{n}{q}+\operatorname{polylog} n\right)
> \]
> rounds, provided arbitrary local computation is allowed.
>
> In the source sparse-graph setting, all local computations can moreover be implemented by ordinary greedy algorithms.

Combining this with the quoted \(O(d^4\log^3n)\) algorithm, for \(q=\Theta(d)\), gives
\[
O\!\left(n^{4/5}(\log n)^{3/5}+\operatorname{polylog}n\right)=o(n)
\]
uniformly over \(d\). Using instead the quoted \(d^3\,2^{O(\sqrt{\log n})}\) variant gives
\[
n^{3/4}2^{O(\sqrt{\log n})}=n^{3/4+o(1)},
\]
and a \(d^3\operatorname{polylog}n\) implementation gives \(\widetilde O(n^{3/4})\).

# 2. A generic degree-plus-one list-coloring lemma

We use the deterministic polylogarithmic network decomposition supplied in the question.

> **Lemma 1.** Let \(F\) be a graph with a list \(M(v)\) at every vertex satisfying
> \[
> |M(v)|\ge \deg_F(v)+1.
> \]
> Then \(F\) can be list-colored deterministically in \(\operatorname{polylog}n\) LOCAL rounds.

## Proof

Take a network decomposition of \(F\) into clusters with:

- \(\operatorname{polylog}n\) cluster colors;
- \(\operatorname{polylog}n\) weak diameter;
- no edge between two distinct clusters having the same cluster color.

Process the cluster colors sequentially. Clusters of the current color act simultaneously.

Suppose that some clusters have already been colored. For an uncolored vertex \(v\), delete from \(M(v)\) all colors used by its already colored neighbors. If \(b(v)\) is the number of such neighbors, then
\[
|M_{\mathrm{current}}(v)|
 \ge |M(v)|-b(v)
 \ge \deg_F(v)+1-b(v).
\]
The right-hand side equals one plus the number of currently uncolored neighbors of \(v\). In particular, if \(C\) is the cluster currently containing \(v\), then
\[
|M_{\mathrm{current}}(v)|\ge \deg_{F[C]}(v)+1.
\]
The entire induced graph \(F[C]\), together with its current lists, can be gathered within the weak-diameter bound. It can therefore be greedily list-colored inside the cluster. Since equally colored clusters are nonadjacent, all clusters in a phase may do this simultaneously.

The number of phases and the time per phase are both polylogarithmic. ∎

This elementary consequence of network decomposition is the only distributed-coloring subroutine needed below.

# 3. High-degree components have small weak diameter

For an integer \(q\ge1\), put
\[
H=\{v\in V(G):\deg_G(v)\ge q\}.
\]

> **Lemma 2.** Every connected component of \(G[H]\) has weak diameter at most
> \[
> \frac{5n}{q+1}+4
> \]
> in \(G\).

## Proof

Let \(C\) be a component of \(G[H]\). Choose a maximal set \(X\subseteq V(C)\) whose vertices have pairwise distance at least \(3\) in \(G\).

For distinct \(x,y\in X\), the closed neighborhoods \(N_G[x]\) and \(N_G[y]\) are disjoint. Since every \(x\in H\) has degree at least \(q\),
\[
(q+1)|X|
 \le \sum_{x\in X}|N_G[x]|
 \le n.
\]
Thus
\[
|X|\le \frac{n}{q+1}.
\]

By maximality, every vertex of \(C\) is within distance \(2\) in \(G\) of some member of \(X\). Form an auxiliary graph \(J\) on \(X\), joining \(x,y\) whenever
\[
\operatorname{dist}_G(x,y)\le5.
\]
The graph \(J\) is connected: along any path in the connected graph \(C\), map each path vertex to a member of \(X\) at distance at most \(2\); two consecutive path vertices are mapped either to the same member of \(X\) or to members at distance at most \(2+1+2=5\).

Consequently, for \(u,v\in C\), choose \(x,y\in X\) within distance \(2\) of them. A path in \(J\) from \(x\) to \(y\) has at most \(|X|-1\) edges, each corresponding to a \(G\)-path of length at most \(5\). Hence
\[
\operatorname{dist}_G(u,v)
 \le 2+5(|X|-1)+2
 \le \frac{5n}{q+1}+4.
\]
∎

The use of weak diameter is legitimate in LOCAL: messages may travel through vertices outside the component, and there is no congestion restriction.

# 4. The high-palette algorithm

Consider a list-coloring instance with lists \(L(v)\) of size at least \(q\).

## Step 1: Color the high-degree part

Let
\[
H=\{v:\deg_G(v)\ge q\},\qquad L=V(G)\setminus H.
\]

By Lemma 2, each component of \(G[H]\) has weak diameter \(O(n/q)\). In that many LOCAL rounds, every vertex of a component can gather the entire component, including its lists.

Each component of \(G[H]\) is list-colorable: a coloring of the whole promised instance restricts to one. Thus, with unrestricted LOCAL computation, a canonical coloring can be found by exhaustive search.

In the source setting no exhaustive search is necessary. If
\(\operatorname{mad}(G)<d=q\), then every nonempty subgraph has a vertex of degree at most \(d-1\). Hence each component of \(G[H]\) is \((d-1)\)-degenerate and can be \(d\)-list-colored centrally by a greedy deletion order. Likewise, in the catalog's \(d\)-degenerate formulation, every induced subgraph can be greedily colored from \(q\ge d+1\) colors.

Thus \(H\) is colored in
\[
O(n/q)
\]
rounds.

## Step 2: Color the low-degree part

For \(v\in L\), remove from \(L(v)\) the colors used by its neighbors in \(H\), and denote the resulting list by \(M(v)\). Then
\[
|M(v)|\ge q-\deg_H(v).
\]
Since \(v\notin H\), we have \(\deg_G(v)\le q-1\). Therefore
\[
q-\deg_H(v)
 \ge \deg_G(v)-\deg_H(v)+1
 =\deg_{G[L]}(v)+1.
\]
Thus the remaining instance on \(G[L]\) satisfies precisely the hypothesis of Lemma 1. It can be list-colored in \(\operatorname{polylog}n\) rounds.

All edges between \(H\) and \(L\) are proper because their colors were removed from the lists of the corresponding vertices in \(L\). This proves the wrapper theorem:
\[
T_{\mathrm{high}}(n,q)
 =O\!\left(\frac{n}{q}+\operatorname{polylog}n\right).
\]

# 5. Combining with the quoted algorithm

Assume first the exact source parametrization \(q=d\), with baseline running time
\[
T_{\mathrm{source}}(n,d)=O(d^4\log^3n).
\]
Let
\[
D=\left(\frac{n}{(\log n)^3}\right)^{1/5}.
\]

Use the source algorithm when \(d\le D\), and the high-palette algorithm when \(d>D\).

If \(d\le D\), then
\[
d^4\log^3n
 \le D^4\log^3n
 =n^{4/5}(\log n)^{3/5}.
\]

If \(d>D\), then
\[
\frac nd
 <\frac nD
 =n^{4/5}(\log n)^{3/5}.
\]

Consequently,
\[
T(n,d)
 =O\!\left(
 n^{4/5}(\log n)^{3/5}
 +\operatorname{polylog}n
 \right)
 =o(n),
\]
with no \(d\) in the final bound.

More generally, if the target palette has size \(q=\Theta(d)\), as in a fixed-\(\varepsilon\) \((1+\varepsilon)d\)-color formulation, the same calculation changes only the constant.

Using the alternative quoted estimate
\[
T_{\mathrm{source}}(n,d)=d^3S(n),
\]
choose
\[
D=\left(\frac{n}{S(n)}\right)^{1/4}.
\]
The resulting uniform bound is
\[
O\!\left(n^{3/4}S(n)^{1/4}+\operatorname{polylog}n\right).
\]
Hence:

- for \(S(n)=2^{O(\sqrt{\log n})}\), this is
  \[
  n^{3/4}2^{O(\sqrt{\log n})}=o(n);
  \]
- for \(S(n)=\operatorname{polylog}n\), it is
  \[
  \widetilde O(n^{3/4}).
  \]

Thus even the older network-decomposition variant, combined with the high-degree decomposition above, suffices for a uniform sublinear bound.

# 6. Important qualification concerning the catalog paraphrase

The sentence “all \(d\)-degenerate graphs with \(\lceil(1+\varepsilon)d\rceil\) colors” cannot literally include every \(d\ge1\) and every small \(\varepsilon>0\) in the deterministic LOCAL model.

For \(d=1\) and \(0<\varepsilon\le1\), the palette has only two colors. Properly 2-coloring paths requires linear time.

Here is a self-contained deterministic lower bound. Suppose a \(t\)-round algorithm 2-colors every \(n\)-vertex path and \(n\ge2t+4\). Fix consistent left/right port labels. For every ordered sequence of \(2t+1\) distinct identifiers, let \(f\) be the output at the center of an internal path segment having those identifiers. Correctness on adjacent internal vertices implies that for every sequence \(a_0,\ldots,a_{2t+1}\) of distinct identifiers,
\[
f(a_0,\ldots,a_{2t})
 \ne
f(a_1,\ldots,a_{2t+1}).
\]
Now choose \(2t+3\) distinct identifiers cyclically and apply this inequality to every consecutive cyclic window. The resulting \(2t+3\) values of \(f\) would properly 2-color an odd cycle, which is impossible. Therefore \(t>(n-4)/2\).

Accordingly, either:

1. \(d\) in the source is the target-density parameter with \(d\ge3\), as in the maximum-average-degree formulation; or
2. the degeneracy paraphrase needs an additional lower bound on the number of colors.

The positive proof above completely handles the intended source formulation and every parameter range in which the quoted \(d\)-dependent algorithm is valid.

# 7. Remaining caveats

- The proof is for the LOCAL model with unbounded messages. Gathering an entire weak-diameter component is not justified in CONGEST.
- It assumes the usual LOCAL convention that local computation is free. In the source sparse classes, the centralized steps are greedy and hence do not require exponential computation.
- The exact quantifiers and rounding convention in the catalog's \((1+\varepsilon)d\) paraphrase should be corrected before treating that paraphrase as a formal theorem.
- I have not verified whether this elementary wrapper argument has appeared elsewhere; the claimed literature novelty is therefore uncertain.