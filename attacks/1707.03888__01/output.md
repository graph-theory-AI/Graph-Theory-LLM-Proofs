```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "After correcting a parameter mismatch, the unrestricted problem remains open for q at least 2, but the q=1 case has optimal additive error 1 and a natural near-K5-minor-free subclass admits additive error t-4.",
  "would_publish": false,
  "caveats": "Hardness assumes P != NP; the catalog mixes two parameters, and the subclass result does not cover all K_t-minor-free graphs."
}
```

## 1. Parameter correction and precise statement

Let \(\operatorname{Excl}(K_t)\) denote the class of \(K_t\)-minor-free graphs, and let \(a(t)\) be the least nonnegative integer \(c\) for which there is, for fixed \(t\), a polynomial-time algorithm producing a proper coloring with at most
\[
\chi(G)+c
\]
colors for every \(G\in\operatorname{Excl}(K_t)\).

Only integer errors matter, since the number of colors and \(\chi(G)\) are integers.

The source theorem uses a parameter \(q\) and states that, unless \(P=NP\), there is no polynomial-time algorithm coloring every \(K_{4q+1}\)-minor-free graph with at most
\[
\chi(G)+q-1
\]
colors. Thus
\[
a(4q+1)\ge q.
\]
The cited positive result gives
\[
a(t)\le t-2,
\]
and hence
\[
q\le a(4q+1)\le 4q-1.
\]

Therefore the corrected open range for \(K_{4q+1}\)-minor-free graphs is
\[
q\le c\le 4q-2.
\]
Equivalently, in terms of the forbidden-minor order \(t\), the known range is approximately
\[
\frac{t}{4}\le a(t)\le t-2.
\]

The catalog sentence combines the two parameterizations: it writes \(K_{4k_0+1}\) but then uses the bounds appropriate when \(k_0\) is the forbidden-minor order. Read literally, it is not an open question. Indeed, if \(k_0=q\), any error \(c<q-2\) is already smaller than the prohibited error \(q-1\), and hence is impossible unless \(P=NP\).

For general \(t\ge5\), the source hardness also gives
\[
a(t)\ge \left\lfloor\frac{t-1}{4}\right\rfloor.
\]
To see this, put \(q=\lfloor(t-1)/4\rfloor\). Then \(4q+1\le t\), so every \(K_{4q+1}\)-minor-free graph is also \(K_t\)-minor-free. An additive-\((q-1)\) algorithm for the latter class would therefore contradict the source theorem.

## 2. The first case is completely resolved

### Proposition 1
Assuming \(P\ne NP\),
\[
a(5)=1.
\]

### Proof: upper bound

There is a polynomial-time algorithm that 4-colors every \(K_5\)-minor-free graph. One standard construction uses Wagner's characterization of edge-maximal \(K_5\)-minor-free graphs as clique-sums, along cliques of order at most three, of planar triangulations and copies of the Wagner graph.

Algorithmically, one may:

1. greedily add edges while preserving \(K_5\)-minor-freeness, using a fixed-\(K_5\) minor test;
2. compute the Wagner decomposition;
3. 4-color every planar piece using a constructive Four Color Theorem algorithm and directly color each Wagner-graph piece;
4. glue colorings across an adhesion clique by permuting the four colors on one side.

The gluing is valid because the vertices of an adhesion clique receive distinct colors, and any prescribed bijection between the colors used on that clique extends to a permutation of the four-color palette.

Now, on input \(G\in\operatorname{Excl}(K_5)\):

- if \(G\) is edgeless, color it with one color;
- if \(G\) is bipartite and has an edge, 2-color it;
- otherwise \(G\) is non-bipartite, so \(\chi(G)\ge3\), and a 4-coloring uses at most \(\chi(G)+1\) colors.

Thus \(a(5)\le1\).

### Proof: lower bound

If \(a(5)=0\), then one could optimally color every planar graph, since every planar graph is \(K_5\)-minor-free. In particular, one could decide planar 3-colorability by checking whether the returned coloring uses at most three colors. Planar 3-colorability is NP-complete. Hence \(a(5)\ge1\) unless \(P=NP\).

Therefore \(a(5)=1\). \(\square\)

For completeness, \(a(t)=0\) for \(t\le4\). In particular, every \(K_4\)-minor-free graph is 2-degenerate and hence 3-colorable; its chromatic number is determined exactly by testing whether it is edgeless or bipartite.

Thus the corrected problem is completely settled at \(q=1\), where the forbidden minor is \(K_5\). The genuinely open cases begin at \(q=2\), namely \(K_9\)-minor-free graphs.

## 3. A lifting lemma for graphs close to a smaller minor-closed class

The following gives a strict two-color improvement over the \(t-2\) bound on a natural subclass.

### Lemma 2
Let \(2\le s\le t\) be fixed. Suppose \(\operatorname{Excl}(K_s)\) has a polynomial-time additive-\(c_s\) coloring algorithm. Consider graphs \(G\) for which there is a set \(X\subseteq V(G)\) satisfying
\[
|X|\le t-s
\qquad\text{and}\qquad
G-X\in\operatorname{Excl}(K_s).
\]
Then:

1. \(G\) is \(K_t\)-minor-free;
2. \(G\) can be colored in polynomial time with at most
   \[
   \chi(G)+(t-s)+c_s
   \]
   colors.

### Proof

Suppose first that \(G\) contained a \(K_t\)-minor model. Its \(t\) branch sets are pairwise disjoint, so at most \(|X|\) of them can meet \(X\). At least
\[
t-|X|\ge s
\]
branch sets avoid \(X\). Those branch sets, together with their pairwise adjacency edges, form a \(K_s\)-minor model in \(G-X\), a contradiction. Thus \(G\) is \(K_t\)-minor-free.

For the algorithm, since \(t-s\) is fixed, enumerate all subsets of at most \(t-s\) vertices and use a fixed-\(K_s\) minor test to find a suitable \(X\). Apply the additive-\(c_s\) algorithm to \(G-X\), and give every vertex of \(X\) its own new color. The number of colors is at most
\[
\chi(G-X)+c_s+|X|
   \le \chi(G)+c_s+t-s.
\]
The use of fresh colors also makes all edges within \(X\) and between \(X\) and \(G-X\) proper. \(\square\)

### Corollary 3
For every fixed \(t\ge5\), graphs satisfying
\[
\exists X,\quad |X|\le t-5,\quad G-X\in\operatorname{Excl}(K_5)
\]
are \(K_t\)-minor-free and admit a polynomial-time additive-\((t-4)\) coloring algorithm.

Indeed, Proposition 1 gives \(c_5=1\), so Lemma 2 gives
\[
(t-5)+1=t-4.
\]

For \(t=4q+1\), this is additive error
\[
4q-3,
\]
as opposed to the general \(4q-1\) bound. For \(q\ge2\),
\[
q<4q-3<4q-1,
\]
so this lies strictly inside the corrected open interval, albeit only on the stated subclass.

The running time obtained by direct enumeration is
\[
n^{\,t-5+O(1)},
\]
which is polynomial for every fixed forbidden minor \(K_t\).

## 4. Clique-sum extension

The preceding subclass can be enlarged without accumulating additive errors.

Call \(G\) a strict clique-sum of \(G_1\) and \(G_2\) if
\[
G=G_1\cup G_2,\qquad S=V(G_1)\cap V(G_2)
\]
is a clique in both graphs, and there are no edges between
\(V(G_1)\setminus S\) and \(V(G_2)\setminus S\).

For such a sum,
\[
\chi(G)=\max\{\chi(G_1),\chi(G_2)\}.
\]
Indeed, optimal colorings of the two pieces can be padded to the same palette size and then made to agree on \(S\) by a color permutation.

The same argument works for approximate colorings: if each \(G_i\) is colored with at most \(\chi(G_i)+c\) colors, the colorings can be glued using at most
\[
\max_i\bigl(\chi(G_i)+c\bigr)=\chi(G)+c
\]
colors. Consequently, a decomposition tree whose pieces satisfy Corollary 3 can be colored with additive error \(t-4\), not with the sum of the piecewise errors.

Such clique-sums remain \(K_t\)-minor-free. Briefly, in any hypothetical \(K_t\)-minor model, the branch sets avoiding the adhesion clique must all lie on the same side, because they are pairwise adjacent and there are no cross-edges. Restricting the branch sets meeting the adhesion to that same side remains valid because the adhesion is a clique. This would place the entire \(K_t\)-model in one summand.

Thus the additive-\((t-4)\) result also holds for the strict clique-sum closure of the near-\(K_5\)-minor-free pieces, provided such a decomposition is supplied or recovered.

## 5. Why this does not solve the unrestricted problem

The missing step is substantial: exclusion of \(K_t\) does not imply the existence of a single set of at most \(t-5\) vertices whose deletion makes the graph \(K_5\)-minor-free.

For example, for \(t\ge6\), arbitrarily many copies of \(K_5\), disjoint or linked by bridges, remain \(K_t\)-minor-free, but one must delete at least one vertex from every copy to eliminate all \(K_5\)-minors. Clique-sum gluing handles this particular obstruction, but no argument above shows that every clique-separator atom of a \(K_t\)-minor-free graph has the required bounded modulator.

Consequently:

- the literal catalog wording is inconsistent and, under its literal parameter choice, conditionally ruled out by the source hardness;
- the corrected unrestricted problem is solved optimally for \(K_5\)-minor-free graphs;
- a strict improvement from \(t-2\) to \(t-4\) holds for the stated modulator and clique-sum subclasses;
- no improved bound is proved here for all \(K_{4q+1}\)-minor-free graphs when \(q\ge2\).