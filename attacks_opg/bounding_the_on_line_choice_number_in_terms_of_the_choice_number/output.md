```json
{
  "verdict": "already_resolved",
  "confidence": "high",
  "one_line": "Duraj, Gutowski, and Kozik resolved the question affirmatively: the online-minus-offline choice-number gap for K_{N,N} is of order log log N.",
  "would_publish": false,
  "caveats": "This is a literature-based resolution; the main chip-game theorem is cited rather than reproved."
}
```

## 1. Statement and status

The 2013 OpenProblemGarden question is no longer open. The relevant paper, also identified in the supplied catalog, is:

> L. Duraj, G. Gutowski, and J. Kozik, **Chip Games and Paintability**, *Electronic Journal of Combinatorics* (2016), DOI: **10.37236/5723**, arXiv:**1506.01148**.

Complete bipartite graphs already answer the question:
\[
\boxed{\operatorname{ch}^{\mathrm{OL}}(K_{N,N})
-\operatorname{ch}(K_{N,N})
=\Theta(\log\log N).}
\]

Below is a derivation from their chip-game theorem. I include elementary estimates for ordinary choosability, so that the only substantial external input is the chip-game result. All logarithms below are base \(2\), except where \(\ln\) is written.

## 2. The online parameter: \(\operatorname{ch}^{\mathrm{OL}}(K_{N,N})=\log N+O(1)\)

Recall the painting-game definition. Initially every vertex has \(k\) tokens. Each round, Lister marks a nonempty set of uncolored vertices and removes one token from each. Painter colors an independent subset of the marked vertices. Lister wins if, after Painter’s response, an uncolored vertex has no tokens. The least \(k\) for which Painter can win is \(\operatorname{ch}^{\mathrm{OL}}(G)\).

For \(K_{N,N}\), an independent set lies entirely in one bipartition class. Painter may therefore be assumed to color all marked vertices in one chosen class.

### The chip-game correspondence

Represent the two bipartition classes by two directed paths with positions
\[
k,k-1,\ldots,0.
\]
Each path initially has \(N\) chips at position \(k\). In a round:

* Pusher advances a nonempty collection of chips one position toward \(0\);
* Remover chooses one path and deletes all chips advanced on that path.

Pusher wins if a chip remains at position \(0\) after Remover’s response. Chips represent uncolored vertices, their positions represent remaining tokens, and deleted chips represent colored vertices. Consequently,
\[
\text{Pusher wins the }(k,N)\text{ chip game}
\quad\Longleftrightarrow\quad
K_{N,N}\text{ is not }k\text{-paintable}.
\]

The substantial theorem of Duraj–Gutowski–Kozik needed here is:

> **Chip-game theorem.** There is an absolute constant \(C\) such that Pusher has a winning strategy whenever
> \[
> N\ge C\,2^k.
> \]

Taking \(k=\lfloor\log(N/C)\rfloor\), for sufficiently large \(N\), gives
\[
\operatorname{ch}^{\mathrm{OL}}(K_{N,N})
\ge \log N-O(1).
\tag{1}
\]

For completeness, the matching upper bound has a short potential argument. Give a chip at position \(i\) weight \(2^{-i}\). Suppose the chips advanced on the two paths have total weights \(a\) and \(b\), measured before advancing. Advancing doubles their weights. Remover deletes the advanced chips on the path with larger total weight, so the surviving total weight changes by
\[
a+b-2\max\{a,b\}=-|a-b|\le 0.
\]
Initially the total weight is \(2N2^{-k}\). If this is less than \(1\), no chip of weight \(1\)—that is, no chip at position \(0\)—can survive a response. Thus Remover wins.

Choosing \(k=\lfloor\log N\rfloor+2\) yields
\[
\operatorname{ch}^{\mathrm{OL}}(K_{N,N})
\le \lfloor\log N\rfloor+2,
\]
and hence
\[
\boxed{\operatorname{ch}^{\mathrm{OL}}(K_{N,N})=\log N+O(1).}
\tag{2}
\]

## 3. The offline parameter is smaller by order \(\log\log N\)

A hypergraph has **Property B** if its vertices admit a red–blue coloring in which every edge contains both colors. Let \(m(k)\) be the minimum number of edges in a \(k\)-uniform hypergraph without Property B.

Two elementary implications connect this parameter to list coloring:
\[
2N<m(k)
\quad\Longrightarrow\quad
\operatorname{ch}(K_{N,N})\le k,
\tag{3}
\]
and
\[
N\ge m(k)
\quad\Longrightarrow\quad
\operatorname{ch}(K_{N,N})>k.
\tag{4}
\]

For (3), regard all \(2N\) lists as hyperedges on the color set. Property B supplies a red color from each left-side list and a blue color from each right-side list, producing a proper coloring.

For (4), take a non-Property-B family of \(m(k)\) lists and assign every list once on each side, adding duplicates if necessary. A proper coloring would make the set of colors used on the left intersect every list, while its complement would also intersect every list because each list occurs on the right. This would give Property B, a contradiction.

We need only the following elementary estimates:
\[
c\,k^{1/4}2^k\le m(k)\le 8k^2 2^k
\qquad(k\ge2),
\tag{5}
\]
where \(c>0\) is absolute.

### Lower bound in (5): random-order greedy coloring

Let \(\mathcal H\) have \(M\) edges, each of size \(k\ge2\). Order its vertices uniformly at random. Process them in that order, coloring a vertex red unless doing so would complete an all-red edge; in that case color it blue.

There is no all-red edge. Suppose an all-blue edge \(B\) results, and let \(v\) be its first vertex in the order. The reason \(v\) was colored blue is that some edge \(R\) had all its other vertices already colored red. Therefore
\[
R\cap B=\{v\},
\]
and the order satisfies
\[
R\setminus\{v\}\;<\;v\;<\;B\setminus\{v\}.
\]

For a fixed ordered pair \((R,B)\) intersecting in one vertex, the probability of this ordering is
\[
a_k=\frac{((k-1)!)^2}{(2k-1)!}.
\]
There are at most \(M^2\) possible ordered pairs. Thus the probability of failure is at most \(M^2a_k\). In particular, the hypergraph has Property B whenever \(M^2a_k<1\).

By Stirling’s formula,
\[
a_k=\Theta\!\left(\frac{4^{-k}}{\sqrt{k}}\right).
\]
It follows that
\[
m(k)\ge c\,k^{1/4}2^k.
\]

### Upper bound in (5): a random hypergraph

Take a ground set of \(q=2k^2\) vertices and choose \(M\) independent uniformly random \(k\)-subsets.

For any fixed red–blue coloring, one color class has at least \(k^2\) vertices. Hence a random edge is monochromatic with probability at least
\[
\frac{\binom{k^2}{k}}{\binom{2k^2}{k}}
\ge 2^{-k}\left(1-\frac1k\right)^k
\ge \frac{2^{-k}}4.
\]
The probability that this coloring makes every chosen edge bichromatic is therefore at most
\[
\exp\!\left(-\frac{M2^{-k}}4\right).
\]
There are \(2^{2k^2}\) colorings. Taking \(M=8k^2 2^k\), the union bound gives
\[
2^{2k^2}\exp(-2k^2)<1.
\]
Thus some resulting hypergraph has no proper red–blue coloring. Removing repeated edges preserves that property, proving the upper bound in (5).

### Inverting the estimates

Put \(L=\log N\). From (3) and the lower bound in (5), choosing
\[
k=\left\lceil L-\frac14\log L+A\right\rceil
\]
with a sufficiently large absolute constant \(A\) gives
\[
\operatorname{ch}(K_{N,N})
\le L-\frac14\log L+O(1).
\tag{6}
\]
Indeed, \(k\sim L\), so \(k^{1/4}2^k\) is an arbitrarily large constant multiple of \(N\) when \(A\) is chosen sufficiently large.

Similarly, (4) and the upper bound in (5), with
\[
k=\left\lfloor L-2\log L-B\right\rfloor,
\]
give, for a sufficiently large absolute constant \(B\),
\[
\operatorname{ch}(K_{N,N})
\ge L-2\log L-O(1).
\tag{7}
\]

These estimates are not the sharpest known Property-B bounds, but they suffice here.

## 4. The unbounded gap

Combining (2), (6), and (7), there is an absolute constant \(D\) such that, for all sufficiently large \(N\),
\[
\frac14\log\log N-D
\le
\operatorname{ch}^{\mathrm{OL}}(K_{N,N})
-\operatorname{ch}(K_{N,N})
\le
2\log\log N+D.
\]
Therefore
\[
\operatorname{ch}^{\mathrm{OL}}(K_{N,N})
-\operatorname{ch}(K_{N,N})
=\Theta(\log\log N),
\]
answering the question affirmatively.

For an explicit sequence, take
\[
G_t=K_{\,2^{2^t},\,2^{2^t}}.
\]
Then
\[
\operatorname{ch}^{\mathrm{OL}}(G_t)-\operatorname{ch}(G_t)
\ge \frac t4-O(1)\longrightarrow\infty.
\]

## 5. Dependence on literature and scope

The only substantial external input above is the established Duraj–Gutowski–Kozik winning strategy for \(N\ge C2^k\); its proof has not been reproduced here. The remaining reductions and estimates were proved explicitly.

This resolves the stated **unbounded additive gap** question. It does not resolve the broader search for the best general function bounding \(\operatorname{ch}^{\mathrm{OL}}\) in terms of \(\operatorname{ch}\), nor does it determine the online choice number of \(K_{3*k}\). Indeed, these bipartite examples still satisfy
\[
\frac{\operatorname{ch}^{\mathrm{OL}}(K_{N,N})}
{\operatorname{ch}(K_{N,N})}\longrightarrow 1.
\]