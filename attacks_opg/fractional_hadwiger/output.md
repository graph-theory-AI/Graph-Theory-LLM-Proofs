```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "Part (c) holds for induced-2K2-free graphs with independence number at most six, and an additive bound holds for larger independence number.",
  "would_publish": false,
  "caveats": "Uses proved small-order Hadwiger cases; the unrestricted conjectures remain unresolved here, and novelty of the restricted result is not claimed."
}
```

## 1. A restricted theorem

Write \(h(G)=\operatorname{had}(G)\) and \(h_f(G)=\operatorname{had}_f(G)\). All graphs below are finite and simple.

A graph is **induced-\(2K_2\)-free** if it has no four vertices inducing exactly two disjoint edges.

**Theorem.** If \(G\) is induced-\(2K_2\)-free, then
\[
\boxed{\quad
\chi_f(G)\le h_f(G)+\max\{0,\alpha(G)-6\}.
\quad}                                                    \tag{1}
\]
Consequently, conjecture **(c)** holds for every induced-\(2K_2\)-free graph with \(\alpha(G)\le6\).

The only non-elementary input is the established small-order Hadwiger theorem:
\[
h(F)\le5\quad\Longrightarrow\quad \chi(F)\le h(F).           \tag{2}
\]
These are the proved cases concerning excluded complete minors of order at most six, not an assumption of an open case. Without this input, the argument gives the entirely elementary version of (1) with \(3\) in place of \(6\).

I do not obtain unrestricted (c), or a proof of (a) or (b).

## 2. Definitions and a useful sufficient condition

A **bramble** is a family of nonempty connected vertex sets that pairwise *touch*: two sets touch if they intersect or there is an edge between them. A fractional bramble packing assigns nonnegative weights \(w_B\) satisfying
\[
\sum_{B\ni v}w_B\le1\qquad(v\in V(G)).
\]
The maximum possible \(\sum_Bw_B\), over brambles and feasible weights, is \(h_f(G)\).

Ordinary clique-minor branch sets with weight \(1\) show that \(h(G)\le h_f(G)\). Also, \(h_f\) is monotone under taking induced subgraphs.

A **fractional perfect matching** in a graph \(F\) is a collection \(x_e\ge0\) such that
\[
\sum_{e\ni v}x_e=1\qquad(v\in V(F)).
\]
It need not be a convex combination of ordinary perfect matchings; an odd cycle, for example, admits one by weighting every edge \(1/2\).

We use the following elementary characterization.

**Lemma 1.** A graph \(F\) has a fractional perfect matching if and only if
\[
|N_F(I)|\ge |I|
\quad\text{for every independent set }I\subseteq V(F).     \tag{3}
\]

**Proof.** Necessity follows by summing the matching constraints over \(I\): all weight incident with \(I\) must also use capacity in \(N_F(I)\).

For sufficiency, form the bipartite double cover of \(F\), with left and right copies of \(V(F)\), and an edge \(u_Lv_R\) whenever \(uv\in E(F)\).

For an arbitrary set \(X\subseteq V(F)\), put
\[
\Gamma(X)=\bigcup_{x\in X}N_F(x),\qquad I=X\setminus\Gamma(X).
\]
Thus \(I\) consists of the isolated vertices of \(F[X]\). In particular, \(I\) is independent and
\[
N_F(I)\subseteq \Gamma(X)\setminus X.
\]
Consequently,
\[
|\Gamma(X)|
\ge |X|-|I|+|N_F(I)|
\ge |X|.
\]
Hall’s theorem gives a perfect matching \(M\) in the double cover. Set
\[
x_{uv}=\frac12\left(
\mathbf 1_{u_Lv_R\in M}+\mathbf 1_{v_Lu_R\in M}
\right).
\]
These weights sum to \(1\) at every vertex of \(F\). ∎

The relevance of induced-\(2K_2\)-freeness is particularly direct.

**Lemma 2.** Suppose \(G\) is induced-\(2K_2\)-free and both \(G\) and \(\overline G\) have fractional perfect matchings. Then
\[
\chi_f(G)\le \frac{|V(G)|}{2}\le h_f(G).                    \tag{4}
\]

**Proof.** All edges of \(G\), considered as two-vertex connected sets, form a bramble. Indeed, two disjoint edges that do not touch would induce a \(2K_2\).

A fractional perfect matching in \(G\) therefore gives a feasible fractional bramble packing. Its total weight is \(|V(G)|/2\).

Conversely, each edge of \(\overline G\) is a two-vertex independent set of \(G\). A fractional perfect matching in \(\overline G\) gives a fractional coloring of \(G\), again of total weight \(|V(G)|/2\). ∎

## 3. A reduction when the complement lacks a fractional perfect matching

For any graph \(G\), define its fractional Hadwiger gap by
\[
\Delta(G)=\chi_f(G)-h_f(G).
\]
For the empty graph, both parameters are taken to be zero.

The next reduction is valid for **arbitrary** graphs, not just induced-\(2K_2\)-free graphs.

**Lemma 3.** If \(\overline G\) has no fractional perfect matching, there is a proper induced subgraph \(G[R]\) such that
\[
\Delta(G)\le \Delta(G[R]).                                 \tag{5}
\]

**Proof.** Put \(H=\overline G\). By Lemma 1, choose an independent set \(S\) of \(H\) maximizing
\[
d(S)=|S|-|N_H(S)|,
\]
where this maximum is positive. Let
\[
T=N_H(S),\qquad R=V(G)\setminus(S\cup T).
\]

First, the bipartite graph of \(H\)-edges between \(S\) and \(T\) has a matching saturating \(T\). Otherwise, Hall’s theorem gives \(U\subseteq T\) with
\[
|N_H(U)\cap S|<|U|.
\]
Writing \(A=N_H(U)\cap S\), we have
\[
N_H(S\setminus A)\subseteq T\setminus U,
\]
and hence
\[
d(S\setminus A)
\ge |S|-|A|-|T|+|U|
>d(S),
\]
contrary to maximality.

In \(G\), the set \(S\) is a clique and is complete to \(R\). The matching just found partitions \(S\cup T\) into \(|S|\) independent sets of \(G\), each a matched pair or an unmatched singleton from \(S\). Thus
\[
\chi_f(G)\le |S|+\chi_f(G[R]).                              \tag{6}
\]

On the other hand, take a fractional bramble packing in \(G[R]\) and add every singleton from \(S\) with weight \(1\). These sets form a bramble because \(S\) is a clique complete to \(R\), and their capacities are disjoint. Therefore
\[
h_f(G)\ge |S|+h_f(G[R]).                                   \tag{7}
\]
Subtracting proves (5). Since \(d(S)>0\), the set \(S\) is nonempty, so \(R\) is proper. ∎

Thus a counterexample to (c) whose complement lacks a fractional perfect matching can always be reduced to a smaller counterexample without decreasing its gap.

## 4. Fractional criticality and degree

We also need a fractional version of the elementary low-degree extension argument.

**Lemma 4.** For every vertex \(v\),
\[
\chi_f(G)\le
\max\{\chi_f(G-v),\,d_G(v)+1\}.                             \tag{8}
\]

**Proof.** Represent a fractional coloring as a palette of real colors, with each vertex receiving a measurable set of colors of measure \(1\), and adjacent vertices receiving disjoint sets. This is equivalent to the usual weighted-independent-set definition, by splitting color weights as necessary.

Take a palette of length
\[
t=\max\{\chi_f(G-v),d_G(v)+1\}
\]
and color \(G-v\), padding with unused colors if necessary. The union of the colors assigned to neighbors of \(v\) has measure at most \(d_G(v)\). At least one unit of palette remains available for \(v\). ∎

In particular, if deleting any vertex strictly lowers \(\chi_f\), then
\[
\chi_f(G)\le d_G(v)+1\qquad\text{for every }v.              \tag{9}
\]

## 5. Proof of the theorem

Suppose first that \(\Delta(G)>0\). Among induced subgraphs \(F\) of \(G\) satisfying
\[
\Delta(F)\ge\Delta(G),
\]
choose one with the fewest vertices.

This choice has two consequences.

1. **Every vertex deletion strictly lowers \(\chi_f(F)\).**  
   Otherwise, if \(\chi_f(F-v)=\chi_f(F)\), monotonicity of \(h_f\) gives
   \[
   \Delta(F-v)\ge\Delta(F),
   \]
   contradicting the choice of \(F\).

2. **The complement \(\overline F\) has a fractional perfect matching.**  
   Otherwise Lemma 3 produces a proper induced subgraph with gap at least \(\Delta(F)\), again a contradiction.

The graph \(F\) remains induced-\(2K_2\)-free. It cannot itself have a fractional perfect matching: together with consequence 2, Lemma 2 would give \(\Delta(F)\le0\).

By Lemma 1, there is therefore a nonempty independent set \(I\) of \(F\) such that
\[
|N_F(I)|<|I|.
\]
Choose \(v\in I\). Consequence 1 and Lemma 4 imply
\[
\chi_f(F)
\le d_F(v)+1
\le |N_F(I)|+1
\le |I|
\le \alpha(F).                                            \tag{10}
\]

Now use the established small-order Hadwiger cases. Since \(\Delta(F)>0\), we cannot have \(h(F)\le5\), as (2) would give
\[
\chi_f(F)\le\chi(F)\le h(F)\le h_f(F).
\]
Hence
\[
h_f(F)\ge h(F)\ge6.                                       \tag{11}
\]

Combining (10) and (11),
\[
\Delta(G)
\le\Delta(F)
=\chi_f(F)-h_f(F)
\le\alpha(F)-6
\le\alpha(G)-6.                                           \tag{12}
\]

If instead \(\Delta(G)\le0\), the claimed bound is immediate. Together these cases prove
\[
\Delta(G)\le\max\{0,\alpha(G)-6\},
\]
which is (1). ∎

### Elementary version

The same proof works with \(3\) instead of \(6\), without using (2). A graph with positive gap cannot be bipartite, since bipartite graphs satisfy \(\chi_f\le h_f\). It therefore contains an odd cycle and hence a \(K_3\) minor, so its fractional Hadwiger number is at least \(3\).

Thus the elementary argument alone proves
\[
\chi_f(G)\le h_f(G)+\max\{0,\alpha(G)-3\}
\]
for induced-\(2K_2\)-free graphs.

## 6. What remains unresolved

The central obstruction to extending this argument is explicit: in a general graph, the edges of a fractional perfect matching need not form a bramble. The two edges of an induced \(2K_2\) are already incompatible.

The argument also genuinely uses fractional objects on both sides of (4). It does not supply an ordinary clique minor of order \(\chi_f(G)\), nor an ordinary coloring using at most \(h_f(G)\) colors. Thus it does not establish (a) or (b).

The restricted bound above is proved, but I make no claim that it is new or publication-worthy.