```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The general polynomial bound remains unresolved, but bipartite graphs have Kempe diameter at most 2n, and a refined lifting argument gives polynomial bounds for several structured degeneracy orders.",
  "would_publish": false,
  "caveats": "The unrestricted bounds obtained below are still exponential, and the novelty of these auxiliary estimates has not been literature-checked."
}
```

## 1. Statement and outcome

A Kempe change in a proper \(k\)-coloring interchanges two colors on one connected component of the subgraph induced by those colors. Let
\[
\operatorname{dist}_{K,G}(\alpha,\beta)
\]
denote the minimum number of Kempe changes between two \(k\)-colorings.

The question asks whether there is a polynomial \(p(n)\), uniformly for all \(k\), such that
\[
\operatorname{dist}_{K,G}(\alpha,\beta)\le p(n)
\]
whenever \(G\) is \((k-1)\)-degenerate.

I do not prove this. I obtain:

1. Every two \(k\)-colorings of an arbitrary bipartite \(n\)-vertex graph are at Kempe distance at most \(2n\).
2. A refined form of the usual vertex-deletion argument gives the uniform exponential bound
   \[
   \operatorname{dist}_{K,G}(\alpha,\beta)
   \le 2\left(\frac32\right)^n-2.
   \]
3. More generally, certain bounded-height degeneracy decompositions give polynomial bounds.
4. An ordering with only \(r\) nonsimplicial deletion steps gives a bound \(n(3/2)^r\), hence a polynomial whenever \(r=O(\log n)\).

These do not control arbitrary degeneracy orderings.

---

## 2. A linear bound for bipartite graphs

### Theorem 2.1

Let \(G\) be an \(n\)-vertex bipartite graph and \(k\ge 2\). Then any two proper \(k\)-colorings of \(G\) are joined by at most \(2n\) Kempe changes.

This does not require any degeneracy assumption.

### Proof

Fix a bipartition \(V(G)=A\cup B\), choosing one for each connected component, and define the canonical coloring
\[
\gamma(v)=
\begin{cases}
1,&v\in A,\\
2,&v\in B.
\end{cases}
\]

Let \(\alpha\) be an arbitrary \(k\)-coloring. Consider the connected components of \(G[\alpha^{-1}(\{1,2\})]\). On every nontrivial such component, the colors \(1,2\) alternate according to the fixed bipartition. Thus precisely one of the following holds:

- vertices in \(A\) have color \(1\) and vertices in \(B\) have color \(2\);
- vertices in \(A\) have color \(2\) and vertices in \(B\) have color \(1\).

In the second case, perform a Kempe change on that component. For an isolated vertex, swap it if its color is not the canonical one for its side.

After at most one change per \(1\)-\(2\) component, every vertex colored \(1\) lies in \(A\), and every vertex colored \(2\) lies in \(B\).

Now let \(v\in A\) have color \(c\notin\{1,2\}\). It has no neighbor of color \(c\), by properness, and no neighbor of color \(1\), since all its neighbors lie in \(B\), where color \(1\) is absent. Hence \(v\) is an isolated component of the subgraph induced by colors \(\{1,c\}\). One Kempe change recolors \(v\) to \(1\). Doing this for all such vertices makes every vertex of \(A\) color \(1\).

Afterwards, if \(v\in B\) has color \(c\notin\{1,2\}\), then \(v\) has neither a color-\(c\) neighbor nor a color-\(2\) neighbor, because all vertices in \(A\) now have color \(1\). Thus \(v\) is an isolated \(\{2,c\}\)-component and can be recolored to \(2\).

If initially \(m\) vertices have colors in \(\{1,2\}\), the first stage uses at most \(m\) changes and the remaining stages use \(n-m\). Therefore
\[
\operatorname{dist}_{K,G}(\alpha,\gamma)\le n.
\]
Applying this to both \(\alpha\) and \(\beta\), and reversing the sequence from \(\beta\) to \(\gamma\), gives
\[
\operatorname{dist}_{K,G}(\alpha,\beta)\le 2n.
\]
\(\square\)

The order of magnitude is best possible: on an edgeless graph, changing all \(n\) vertices from color \(1\) to color \(2\) requires \(n\) singleton Kempe changes.

---

## 3. A refined deletion/lifting lemma

The following isolates the loss in the standard degeneracy induction.

### Lemma 3.1 — independent-layer lifting

Let \(S\) be an independent set in \(G\), put \(H=G-S\), and suppose
\[
|N_G(x)\cap V(H)|\le k-1
\qquad\text{for every }x\in S.
\]
Let \(\alpha,\beta\) be \(k\)-colorings of \(G\), and let
\[
P=(\sigma_0,\sigma_1,\ldots,\sigma_L)
\]
be a Kempe sequence in \(H\) from \(\alpha|_H\) to \(\beta|_H\).

For \(x\in S\), define
\[
q_x(t)=\bigl|\{\sigma_t(y):y\in N_H(x)\}\bigr|.
\]
Let \(U_x\) and \(D_x\) respectively be the numbers of indices \(t\) for which
\[
q_x(t)=q_x(t-1)+1
\quad\text{and}\quad
q_x(t)=q_x(t-1)-1.
\]
Then
\[
\operatorname{dist}_{K,G}(\alpha,\beta)
\le
L+\min\left\{\sum_{x\in S}U_x,\sum_{x\in S}D_x\right\}+|S|.
\]
Consequently,
\[
\operatorname{dist}_{K,G}(\alpha,\beta)
\le
\left(1+\frac{|S|}{2}\right)L+|S|.
\tag{3.1}
\]

### Proof

We first lift \(P\) forward, starting from \(\alpha\).

Suppose the next change in \(H\) swaps colors \(a,b\) on an \((a,b)\)-component \(C\). A vertex \(x\in S\) can prevent \(C\) from remaining a separate component in \(G\) only in the following situation:

- the current color of \(x\) is \(a\), say;
- \(x\) has a \(b\)-colored neighbor in \(C\);
- \(x\) also has a \(b\)-colored neighbor in another \((a,b)\)-component of \(H\).

Call such a vertex obstructing. The symmetric case with \(a,b\) exchanged is identical.

An obstructing \(x\) has at least two neighbors of the same color \(b\). Hence its neighbors use at most
\[
\deg_H(x)-1\le k-2
\]
distinct colors. Its current color \(a\) is absent from its neighborhood, and there is therefore another color \(c\ne a\) absent from its neighborhood. Since \(S\) is independent, \(x\) is an isolated component of the subgraph induced by colors \(\{a,c\}\). Recolor \(x\) from \(a\) to \(c\) by one Kempe change.

After all obstructing vertices have been moved away from \(\{a,b\}\), the \((a,b)\)-component of \(G\) containing \(C\) intersects \(H\) precisely in \(C\). Indeed, any path from \(C\) to another \((a,b)\)-component of \(H\) would have to pass through an active-colored vertex of \(S\) adjacent to both components, and that vertex would have been declared obstructing. We may therefore perform one Kempe change whose restriction to \(H\) is exactly the prescribed change on \(C\).

Every obstruction at \(x\) forces \(q_x\) to increase by one: before the change, no neighbor of \(x\) has color \(a\), while color \(b\) occurs both in \(C\) and outside \(C\). Afterwards, an affected neighbor in \(C\) has color \(a\), while an unaffected neighbor still has color \(b\). No represented color is lost. Thus the number of extra changes in a forward lift is at most
\[
\sum_{x\in S}U_x.
\]

At the end, the coloring agrees with \(\beta\) on \(H\). For each \(x\in S\), both its current color and \(\beta(x)\) are absent from \(N_H(x)\). Since \(S\) is independent, \(x\) is an isolated component for those two colors and can be adjusted in at most one further change. This proves a forward bound
\[
L+\sum_x U_x+|S|.
\]

Running the path \(P\) backwards from \(\beta\), and then reversing the resulting lifted sequence, gives instead
\[
L+\sum_x D_x+|S|.
\]

A single Kempe change in \(H\) affects only two color labels, so each \(q_x\) changes by at most one. Hence
\[
U_x+D_x\le L.
\]
It follows that
\[
\min\left\{\sum_xU_x,\sum_xD_x\right\}
\le \frac12\sum_x(U_x+D_x)
\le \frac{|S|L}{2},
\]
which proves (3.1). \(\square\)

---

## 4. Consequences

### 4.1 A uniform explicit exponential bound

Taking \(S=\{v\}\) in Lemma 3.1 gives
\[
D(n)\le \frac32D(n-1)+1,
\]
where \(D(n)\) is the maximum Kempe diameter over \(n\)-vertex \((k-1)\)-degenerate graphs. Since \(D(0)=0\),
\[
D(n)\le 2\left(\frac32\right)^n-2.
\tag{4.1}
\]

This also gives a self-contained proof of Kempe connectivity at the degeneracy threshold, but remains exponential.

The improvement from the naive factor \(2\) comes from choosing whether to lift the sequence forward or backward: an obstruction corresponds to an increase of the neighborhood-color statistic in one direction and to a decrease in the other.

---

### 4.2 Bounded-height degeneracy decompositions

Call an ordered partition
\[
V(G)=S_1\cup\cdots\cup S_h
\]
a \(k\)-admissible layering if:

1. each \(S_i\) is independent;
2. for every \(v\in S_i\),
   \[
   \left|N(v)\cap\bigcup_{j>i}S_j\right|\le k-1.
   \]

Every such graph is \((k-1)\)-degenerate.

### Theorem 4.2

If \(G\) has a \(k\)-admissible layering \(S_1,\ldots,S_h\), then
\[
\operatorname{dist}_{K,G}(\alpha,\beta)
\le
2\prod_{i=1}^h\left(1+\frac{|S_i|}{2}\right)-2
\le
2\left(1+\frac{n}{2h}\right)^h-2.
\tag{4.2}
\]

In particular, for fixed \(h\), the Kempe diameter is \(O(n^h)\).

### Proof

Let \(G_i=G[S_i\cup\cdots\cup S_h]\), and let \(D_i\) be the maximum Kempe distance in \(G_i\). Applying Lemma 3.1 when adding \(S_i\) to \(G_{i+1}\) gives
\[
D_i\le \left(1+\frac{|S_i|}{2}\right)D_{i+1}+|S_i|.
\]
Equivalently,
\[
D_i+2
\le
\left(1+\frac{|S_i|}{2}\right)(D_{i+1}+2).
\]
Since \(D_{h+1}=0\), iteration gives the first inequality in (4.2). The second follows from AM–GM:
\[
\prod_{i=1}^h\left(1+\frac{|S_i|}{2}\right)
\le
\left(1+\frac{n}{2h}\right)^h.
\]
\(\square\)

This covers some nonbipartite graphs of unbounded treewidth. For example, let \(J\) be the \(1\)-subdivision of \(K_m\), with branch set \(B\) and subdivision set \(E\). Add a triangle \(xyz\) and one edge \(yb_0\), where \(b_0\in B\). Then, for \(k=3\),
\[
S_1=E\cup\{x\},\qquad S_2=\{y\},\qquad S_3=B\cup\{z\}
\]
is a \(3\)-admissible layering. The graph is \(2\)-degenerate, contains a triangle, and has treewidth at least \(m-1\) because it has a \(K_m\) minor. Formula (4.2) gives an \(O(m^3)=O(n^{3/2})\) Kempe bound for this family.

---

### 4.3 Few nonsimplicial deletion steps

Let \(v_1,\ldots,v_n\) be a degeneracy ordering and put
\[
G_i=G[\{v_i,\ldots,v_n\}].
\]
Call \(i\) defective if \(N_{G_i}(v_i)\) is not a clique.

If \(N_{G_i}(v_i)\) is a clique, then its vertices receive pairwise distinct colors in every proper coloring. Therefore the statistic \(q_{v_i}\) in Lemma 3.1 is constant along every sequence, and no extra lifting change is needed: a sequence of length \(L\) in \(G_{i+1}\) lifts in at most \(L+1\) changes.

At a defective step, Lemma 3.1 gives at most \((3/2)L+1\). Hence, if the ordering has \(r\) defective indices,
\[
\operatorname{dist}_{K,G}(\alpha,\beta)
\le n\left(\frac32\right)^r.
\tag{4.3}
\]
Thus any family admitting such an ordering with \(r=O(\log n)\) has polynomial Kempe diameter. In particular, a chordal graph with clique number at most \(k\) has \(r=0\) under a perfect elimination ordering and consequently has Kempe diameter at most \(n\).

---

## 5. Why this does not settle the conjecture

The obstruction in Lemma 3.1 is very specific: a deleted low-degree vertex can join two distinct bichromatic components of the remaining graph. Vacating that vertex costs one extra Kempe change. The neighborhood-color count \(q_x\) certifies such an event, but along an unrestricted Kempe sequence it may oscillate on a linear proportion of the steps. Choosing the better direction reduces the multiplicative loss from \(2\) to \(3/2\), but not to an additive loss.

For a general \((k-1)\)-degenerate graph:

- a \(k\)-admissible layering may require \(h=\Theta(n)\);
- every degeneracy ordering may have \(\Theta(n)\) defective steps;
- the bipartite canonicalization argument has no direct analogue once bichromatic components can meet three or more classes of a fixed target coloring.

Thus none of the bounds above yields a polynomial for the unrestricted problem, even for general \(3\)-colorings of \(2\)-degenerate graphs. No superpolynomial lower bound or counterexample is obtained either. I have not checked whether the elementary refinements above already occur in the full source paper or elsewhere, so I make no novelty claim.