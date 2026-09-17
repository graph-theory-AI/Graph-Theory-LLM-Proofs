Attack the following open graph-theory problem.

Catalog id: fractional_hadwiger
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/fractional_hadwiger/
Original entry: http://www.openproblemgarden.org/op/fractional_hadwiger
Problem attributed to: Harvey, Daniel J., Reed, Bruce A., Seymour, Paul D., Wood, David R. (posted 2014-03-16)

=== Problem statement (OpenProblemGarden) ===
Title: Fractional Hadwiger
Conjecture For every graph $ G $ , (a) $ \chi_f(G)\leq\text{had}(G) $ (b) $ \chi(G)\leq\text{had}_f(G) $ (c) $ \chi_f(G)\leq\text{had}_f(G) $ .

=== Discussion / context (OpenProblemGarden) ===
Here $ \chi $ is the chromatic number, $ \chi_f $ is the fractional chromatic number, $ \text{had} $ is the Hadwiger number, and $ \text{had}_f $ is the fractional Hadwiger number (which was recently introduced independently by Fox [F] and Pedersen [P]). It is well known and easily proved (see [HW]) that $ \chi_f(G)\leq\chi(G)\text{ and }\text{had}(G)\leq\text{had}_f(G)\leq\text{tw}(G)+1, $ where $ \text{tw}(G) $ is the treewidth of $ G $ . Hadwiger's famous conjecture, $ \chi(G)\leq\text{had}(G) $ , bridges the gap in the above inequalities. The above conjectures therefore are weaker than Hadwiger's conjecture. Note that Conjecture (a) implies Conjecture (c), and Conjecture (b) implies Conjecture (c). Note that Reed and Seymour [RS] proved that $ \chi_f(G)\leq2\,\text{had}(G) $ . Conjecture (a) is due to Reed and Seymour [RS]. Conjecture (b) is due to Harvey and Wood [HW]. Conjecture (c) is independently due to Harvey and Wood [HW] and Pedersen [P]. Pedersen [P] presents a natural equivalent formulation of Conjecture (c).

=== References listed by OpenProblemGarden ===
- *[HW] Daniel J. Harvey, David R. Wood, Parameters tied to treewidth. arXiv:1312.3401, 2013.
- [F] Jacob Fox. Constructing dense graphs with sublinear Hadwiger number. J. Combin. Theory Ser. B (to appear).
- *[P] Anders Sune Pedersen. Contributions to the Theory of Colourings, Graph Minors, and Independent Sets, PhD thesis, Department of Mathematics and Computer Science University of Southern Denmark, 2011.
- *[RS] Bruce A. Reed, Paul D. Seymour, Fractional colouring and Hadwiger's conjecture. J. Combin. Theory Ser. B, 74(2), 147-152.

=== Catalog page (statement + literature review) ===
Fractional Hadwiger — Graph-theory open problems

 
 Status
 open
 medium confidence
 

 No verified post-2014 paper resolves any of the three conjectures (a) $\chi_f(G)\leq\mathrm{had}(G)$, (b) $\chi(G)\leq\mathrm{had}_f(G)$, or (c) $\chi_f(G)\leq\mathrm{had}_f(G)$. The best published upper bound on $\chi_f$ in terms of $\mathrm{had}$ remains Reed and Seymour's 1998 result $\chi_f(G)\leq 2\,\mathrm{had}(G)$; recent improvements toward Hadwiger's conjecture by Norin, Postle and Song concern $\chi(G)$ versus $\mathrm{had}(G)$ rather than the fractional variants.

 Reviewer notes. Searches surfaced recent work on the (integer) Hadwiger conjecture (Norin-Postle-Song, Steiner 2023 on topological bounds, Postle's improved bounds) and on related variants (odd Hadwiger, balanced chromatic number, strong chromatic index), but none of the verified items prove or disprove any of conjectures (a), (b), (c). The Fox 2011 paper (arXiv:1108.4953) introducing $\mathrm{had}_f$ predates the OPG posting date of 2014-03-16, so it cannot count as 'since posted'. I did not exhaustively search for unpublished theses or short notes, so a small probability remains that incremental progress exists in less indexed venues; status reported as 'open' rather than 'unclear' because the OPG-listed Reed-Seymour bound $\chi_f\leq 2\,\mathrm{had}$ from 1998 is still the state of the art quoted in surveys.

 
 Auto-reviewed 2026-05-08 with claude-sonnet (subagent) (web search enabled).
 

Conjecture. For every graph $ G $ , (a) $ \chi_f(G)\leq\text{had}(G) $ (b) $ \chi(G)\leq\text{had}_f(G) $ (c) $ \chi_f(G)\leq\text{had}_f(G) $ .

Keywords:
fractional coloring, minors

Discussion

Here $ \chi $ is the chromatic number, $ \chi_f $ is the fractional chromatic number, $ \text{had} $ is the Hadwiger number, and $ \text{had}_f $ is the fractional Hadwiger number (which was recently introduced independently by Fox [F] and Pedersen [P]). It is well known and easily proved (see [HW]) that $ \chi_f(G)\leq\chi(G)\text{ and }\text{had}(G)\leq\text{had}_f(G)\leq\text{tw}(G)+1, $ where $ \text{tw}(G) $ is the treewidth of $ G $ . Hadwiger's famous conjecture, $ \chi(G)\leq\text{had}(G) $ , bridges the gap in the above inequalities. The above conjectures therefore are weaker than Hadwiger's conjecture. Note that Conjecture (a) implies Conjecture (c), and Conjecture (b) implies Conjecture (c). Note that Reed and Seymour [RS] proved that $ \chi_f(G)\leq2\,\text{had}(G) $ . Conjecture (a) is due to Reed and Seymour [RS]. Conjecture (b) is due to Harvey and Wood [HW]. Conjecture (c) is independently due to Harvey and Wood [HW] and Pedersen [P]. Pedersen [P] presents a natural equivalent formulation of Conjecture (c).

Bibliography

★ [HW]
 Daniel J. Harvey, David R. Wood, Parameters tied to treewidth. arXiv:1312.3401 , 2013.
 arXiv:1312.3401

 [F]
 Jacob Fox. Constructing dense graphs with sublinear Hadwiger number . J. Combin. Theory Ser. B (to appear).
 Constructing dense graphs with sublinear Hadwiger number

★ [P]
 Anders Sune Pedersen. Contributions to the Theory of Colourings, Graph Minors, and Independent Sets , PhD thesis, Department of Mathematics and Computer Science University of Southern Denmark, 2011.
 Contributions to the Theory of Colourings, Graph Minors, and Independent Sets

★ [RS]
 Bruce A. Reed, Paul D. Seymour, Fractional colouring and Hadwiger's conjecture. J. Combin. Theory Ser. B, 74(2), 147-152.

Related conjectures

 
 implies
 Independence number lower bound in K_{t+1}-minor-free graphs
 open
 If G is K_{t+1}-minor-free then its Hadwiger number satisfies had(G) ≤ t. Part (a) of the Fractional Hadwiger conjecture gives χ_f(G) ≤ had(G) ≤ t. The standard inequality χ_f(G) ≥ n/α(G) (every fractional coloring covers each vertex by independent sets of size ≤ α, LP duality) then gives α(G) ≥ n/χ_f(G) ≥ n/t, which is exactly the target. Only part (a) of the source is needed, and the source conjecture asserts (a), (b), (c) jointly, so truth of the source forces the target. The target's own context confirms this is a weakening along exactly this chain (via Hadwiger). Direction correct.
 

 
 implies
 Seagull problem
 partial
 Part (a) of Fractional Hadwiger states chi_f(G) <= had(G). By LP duality (fractional covering by independent sets), chi_f(G) >= n/alpha(G) for every n-vertex G. If G has no independent set of size 3 then alpha(G) <= 2, so chi_f(G) >= n/2, whence had(G) >= n/2; since had(G) is an integer, G has a K_{ceil(n/2)} minor, i.e. a complete minor on >= n/2 vertices — exactly the Seagull problem. The source conjecture is the conjunction of (a),(b),(c), and (a) alone suffices, so the conjecture implies Seagull. (Part (b) alone would not obviously suffice, since had_f >= had; but the edge is from the full conjecture.) Direction correct: Fractional Hadwiger is the stronger statement.
 

 View in the relation graph
 — relations are AI-reviewed, not formally verified.

========================================================================

=== A PREVIOUS, UNVERIFIED ATTEMPT ===
The problem above was already attacked by `gpt-6-astra`, which reported verdict `partial` at high confidence. That attempt is reproduced below.

Treat it as a lead, not as an authority: it is unverified, it may be wrong in ways neither model noticed, and its framing may be the reason it stalled. Check anything you reuse, and say so if you discard it. Your task is the original problem, not a critique of this attempt. If you can finish what it started, do that; if a different route is better, take it.

--- previous attempt ---
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
