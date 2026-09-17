Attack the following open graph-theory problem.

Catalog id: high_girth_low_degree_4_chromatic_graphs
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory » Coloring
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/high_girth_low_degree_4_chromatic_graphs/
Original entry: http://www.openproblemgarden.org/op/high_girth_low_degree_4_chromatic_graphs
Problem attributed to: Grunbaum, Branko (posted 2008-06-18)

=== Problem statement (OpenProblemGarden) ===
Title: 4-regular 4-chromatic graphs of high girth
Problem Do there exist 4-regular 4-chromatic graphs of arbitrarily high girth?

=== Discussion / context (OpenProblemGarden) ===
Grunbaum conjectured that for every $ m $ , there exist $ m $ -regular $ m $ -chromatic graphs of arbitrarily high girth. However, this was shown dramatically false by Johansson, who proved that every triangle free graph $ G $ with maximum degree $ \Delta $ satisfies $ \chi(G) \le C \frac{\Delta}{\log \Delta} $ for some fixed constant $ C $ . Neverless, some interesting smaller cases of Grunbaum's conjecture, such as the one highlighted above, might still be true. There are only a few 4-regular 4-chromatic graphs of girth $ \ge 4 $ which are known. These include the Chvatal graph , Brinkmann graph (discovered independently by Kostochka), and Grunbaum graph . To the best of my (M. DeVos') knowledge, this might be the full list of such graphs. There do exist 4-chromatic graphs of minimum degree $ \le 6 $ and arbitrarily high girth, but it is open wether there exist 4-chromatic graphs of minimum degree 5 and arbitrary girth.

=== Catalog page (statement + literature review) ===
4-regular 4-chromatic graphs of high girth — Graph-theory open problems

 
 Status
 open
 medium confidence
 

 The question whether 4-regular 4-chromatic graphs of arbitrarily high girth exist is still open. The general Grünbaum conjecture (every $m$-regular $m$-chromatic graph class admits arbitrarily high girth) is known to be false from Johansson's $\chi \le C\Delta/\log\Delta$ bound for triangle-free graphs, but that bound does not preclude the small-$m$ case considered here. Only a handful of 4-regular 4-chromatic graphs of girth $\ge 4$ are known (Chvátal at girth 4; Brinkmann and Grünbaum at girth 5); no construction or non-existence proof for higher girth has appeared in the searched literature.

 Reviewer notes. Searches surfaced Bucić–Davies (arXiv:2312.06898, 2023) on geometric graphs with exponential chromatic number and arbitrary girth, but that paper does not address the regular-graph version of the question, so it is not cited as evidence here. Status 'medium' rather than 'high' because absence of recent constructions in search results is not conclusive.

 
 Auto-reviewed 2026-05-08 with claude (main agent, web search + fetch) (web search enabled).
 

Problem. Do there exist 4-regular 4-chromatic graphs of arbitrarily high girth?

Keywords:
coloring · girth

Discussion

Grunbaum conjectured that for every $ m $ , there exist $ m $ -regular $ m $ -chromatic graphs of arbitrarily high girth. However, this was shown dramatically false by Johansson, who proved that every triangle free graph $ G $ with maximum degree $ \Delta $ satisfies $ \chi(G) \le C \frac{\Delta}{\log \Delta} $ for some fixed constant $ C $ . Neverless, some interesting smaller cases of Grunbaum's conjecture, such as the one highlighted above, might still be true. There are only a few 4-regular 4-chromatic graphs of girth $ \ge 4 $ which are known. These include the Chvatal graph , Brinkmann graph (discovered independently by Kostochka), and Grunbaum graph . To the best of my (M. DeVos') knowledge, this might be the full list of such graphs. There do exist 4-chromatic graphs of minimum degree $ \le 6 $ and arbitrarily high girth, but it is open wether there exist 4-chromatic graphs of minimum degree 5 and arbitrary girth.

========================================================================

=== A PREVIOUS, UNVERIFIED ATTEMPT ===
The problem above was already attacked by `gpt-6-astra`, which reported verdict `partial` at high confidence. That attempt is reproduced below.

Treat it as a lead, not as an authority: it is unverified, it may be wrong in ways neither model noticed, and its framing may be the reason it stalled. Check anything you reuse, and say so if you discard it. Your task is the original problem, not a critique of this attempt. If you can finish what it started, do that; if a different route is better, take it.

--- previous attempt ---
```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I obtain quantitative color-preserving regularization and a degree-6 construction of order O(5^g), but do not settle degree 4.",
  "would_publish": false,
  "caveats": "Auxiliary results only, with no claim of novelty; no degree-4 construction or nonexistence theorem is obtained."
}
```

## 1. What is established

All graphs in the conclusions below are finite and simple. Girth at least \(g\) means that there is no cycle of length less than \(g\).

I prove two auxiliary results.

**Theorem 1 — Quantitative color-preserving regularization.**  
Let \(r,k\ge 2\) and \(g\ge 3\), and put
\[
b_r(g)=1+r\sum_{i=0}^{g-3}(r-1)^i.
\]
Suppose \(H\) has maximum degree at most \(r\), girth at least \(g\), and a proper \(k\)-coloring. Then \(H\) is an induced subgraph of an \(r\)-regular graph \(F\) of girth at least \(g\), with a proper \(k\)-coloring, such that
\[
|V(F)|\le 2|V(H)|+2k\bigl(3b_r(g)+1\bigr).
\]
In particular, if \(\chi(H)=k\), then \(\chi(F)=k\).

Thus, for the stated problem, regularity can be imposed once a non-3-colorable graph of maximum degree \(4\) and sufficiently large girth is available.

**Theorem 2 — A degree-6 substitute.**  
For every integer \(g\ge 3\), there exists a \(6\)-regular, exactly \(4\)-chromatic graph of girth at least \(g\), with fewer than
\[
2002\cdot 5^g
\]
vertices.

The constants are not optimized. These results do **not** resolve the degree-4 question, and I do not assert that they are new.

## 2. Proof of the regularization theorem

The main ingredient is a matching-extension lemma.

### Lemma 3

Let \(G_0\) have maximum degree at most \(r\) and girth at least \(g\). Let \(A,B\) be disjoint vertex sets of the same size \(m\), with every vertex of \(A\cup B\) having degree at most \(r-1\). If
\[
m\ge 3b_r(g)+1,
\]
then a perfect matching between \(A\) and \(B\) can be added without creating a cycle of length less than \(g\).

### Proof

Write \(b=b_r(g)\). In any graph of maximum degree at most \(r\), a ball of radius \(g-2\) contains at most \(b\) vertices.

Choose a matching \(M\) between \(A\) and \(B\), disjoint from \(E(G_0)\), of maximum possible size subject to
\[
G=G_0+M
\]
having girth at least \(g\). Throughout, \(\Delta(G)\le r\).

Suppose \(M\) is not perfect. Choose unmatched vertices \(a\in A\) and \(b'\in B\). Every unmatched vertex of \(B\) must be at distance at most \(g-2\) from \(a\) in \(G\); otherwise its edge to \(a\) could be added. Consequently,
\[
m-|M|\le b,\qquad |M|\ge m-b\ge 2b+1.
\]

At most \(2b\) edges of \(M\) have an endpoint in the union of the radius-\((g-2)\) balls around \(a\) and \(b'\). Hence some \(xy\in M\), with \(x\in A\), \(y\in B\), has both endpoints outside that union.

Replace \(xy\) by \(ay\) and \(xb'\). The new edges are absent from \(G\), and this replacement increases the matching size by one. We check girth.

- A cycle using exactly one new edge has length at least \(g\), because the endpoints of that edge were at distance at least \(g-1\) in \(G\).
- A cycle using both new edges splits, after their removal, into paths in \(G-xy\). One possible pairing is \(a\) to \(x\) and \(b'\) to \(y\); these paths are long by the choice of \(xy\). The other pairing is \(a\) to \(b'\) and \(x\) to \(y\). Every \(x\)-\(y\) path in \(G-xy\) has length at least \(g-1\), since adding \(xy\) to a shorter path would give a short cycle in \(G\).

Thus no cycle of length less than \(g\) is created, contradicting maximality of \(M\). ∎

### Construction proving Theorem 1

Fix a proper coloring
\[
\varphi:V(H)\longrightarrow \{1,\ldots,k\},
\]
and let \(L=3b_r(g)+1\).

Add \(kL\) isolated vertices to \(H\), assigning exactly \(L\) of them each color. Call the resulting colored graph \(J\). Take two disjoint copies \(J_L,J_R\). On the left use \(\varphi\); on the right use \(\pi\circ\varphi\), where \(\pi\) is a fixed-point-free permutation of the \(k\) colors.

For \(v\in V(J)\), define its deficit
\[
\delta(v)=r-d_J(v).
\]
For each \(j=1,\ldots,r\) and each original color \(c\), let
\[
A_{c,j}=\{v_L:\varphi(v)=c,\ \delta(v)\ge j\},
\]
and define \(B_{c,j}\) analogously in \(J_R\).

These sets have equal size, at least \(L\), because the added isolated vertices participate at every stage. When this stage is reached, their vertices have degree at most \(r-1\). Apply Lemma 3 to add a perfect matching between them.

Every vertex receives exactly its deficit number of new edges, so the final graph is \(r\)-regular. Every new edge joins a vertex colored \(c\) on the left to one colored \(\pi(c)\ne c\) on the right. Hence the coloring remains proper. Girth is preserved at every stage.

No edges are added within either copy of \(J\), so the original copies of \(H\) remain induced. Finally,
\[
|V(F)|=2|V(H)|+2kL,
\]
as required. ∎

### Consequence for the original question

For each fixed \(g\ge 3\), the following are equivalent:

1. There is a \(4\)-regular, \(4\)-chromatic graph of girth at least \(g\).
2. There is a non-3-colorable graph of maximum degree at most \(4\) and girth at least \(g\).

Only the reverse implication needs proof. From a graph in (2), take an inclusion-minimal non-3-colorable subgraph \(H\). For every vertex \(v\), the graph \(H-v\) is 3-colorable, so giving \(v\) a fourth color proves \(\chi(H)=4\). Apply Theorem 1 with \(r=k=4\).

More explicitly, since
\[
b_4(g)=2\cdot 3^{g-2}-1,
\]
the completion has at most
\[
2|V(H)|+48\cdot 3^{g-2}-16
\]
vertices.

A minimal non-3-colorable graph is connected. If connectedness is desired, retain the component of the completion containing \(H\).

## 3. A robust random degree-6 construction

I next prove Theorem 2. The argument uses an alteration: first obtain a graph that remains non-3-colorable after a small vertex deletion, and then delete all short cycles.

### 3.1 Robust non-3-colorability

Use the configuration model with six distinguishable half-edges at each of \(n\) labeled vertices, paired uniformly. This initially gives a multigraph.

A **partial 3-coloring** is a function
\[
f:V\longrightarrow \{0,1,2,3\},
\]
where \(0\) means uncolored, and no edge has both endpoints assigned the same nonzero color. Let \(Y\) count such functions having at most \(n/1000\) uncolored vertices.

I claim that
\[
\mathbb E Y\le (6n+1)^{100}e^{-n/10}.
\tag{1}
\]

Here are the counting details.

Write \(a_i\) for the proportion of vertices assigned \(i\), for \(i=0,1,2,3\). Let \(P=(p_{ij})\) be the joint distribution of the colors at the two ends of a uniformly oriented edge. Then \(P\) is symmetric, its marginals are \(a\), and
\[
p_{11}=p_{22}=p_{33}=0.
\]

Use natural logarithms, and define
\[
H(a)=-\sum_i a_i\log a_i,\qquad
H(P)=-\sum_{i,j}p_{ij}\log p_{ij}.
\]
The mutual information is
\[
I(P)=2H(a)-H(P)=D(P\Vert a\otimes a).
\]

For completeness, if \(n_i=na_i\) and \(m_{ij}\) is the number of edges of color type \(ij\), with \(i\le j\), the number of pairings having those edge counts for a fixed vertex assignment is
\[
\frac{\prod_i(6n_i)!}
{\displaystyle
 \prod_i 2^{m_{ii}}m_{ii}!\,
 \prod_{i<j}m_{ij}!}.
\tag{2}
\]
Dividing by the total number
\[
(6n-1)!!=\frac{(6n)!}{2^{3n}(3n)!}
\]
of pairings, and multiplying by the multinomial number of vertex assignments, gives exponential term
\[
\exp\bigl(n[H(a)-3I(P)]\bigr).
\]

This estimate can be made uniform with a polynomial factor. There are at most \((6n+1)^{14}\) choices of vertex and edge counts, and the expression involves 21 factorials. The elementary uniform bound
\[
\left|\log(t!)-(t\log t-t)\right|
 \le 1+\log(6n+1)
\]
for \(0\le t\le 6n\), with \(0\log0=0\), shows that a factor \((6n+1)^{100}\) is more than sufficient.

It remains to bound the exponent.

Let
\[
Z=1-\sum_{i=1}^{3}a_i^2.
\]
The allowed color pairs have total probability \(Z\) under \(a\otimes a\). Normalizing \(a\otimes a\) on those pairs and using nonnegativity of relative entropy gives
\[
I(P)\ge-\log Z.
\tag{3}
\]
Put \(t=a_0\). Then
\[
H(a)\le h(t)+(1-t)\log3,
\qquad
Z\le 1-\frac{(1-t)^2}{3},
\]
where \(h(t)=-t\log t-(1-t)\log(1-t)\). Thus
\[
H(a)-3I(P)
\le h(t)+(1-t)\log3+
3\log\left(1-\frac{(1-t)^2}{3}\right).
\]
Using
\[
h(t)\le t\log(e/t)
\]
and
\[
1-\frac{(1-t)^2}{3}
=\frac23\left(1+t-\frac{t^2}{2}\right),
\]
we obtain
\[
H(a)-3I(P)
\le \log(8/9)+t\bigl(4+\log(1/t)\bigr).
\]
For \(0\le t\le 1/1000\), the right-hand side is less than \(-1/10\). For example,
\[
\log(9/8)\ge \frac19,\qquad \log1000<7
\]
give
\[
\log(8/9)+t\bigl(4+\log(1/t)\bigr)
<-\frac19+\frac{11}{1000}<-\frac1{10}.
\]
This proves (1).

Consequently, except with probability at most the right-hand side of (1), **deleting any set of at most \(n/1000\) vertices still leaves a non-3-colorable graph**. Indeed, a 3-coloring after such a deletion would give one of the partial colorings counted by \(Y\).

For \(n\ge125000\), the bound in (1) is less than \(1/4\).

### 3.2 Deleting short cycles

Fix \(g\ge3\), and take
\[
n=1000\cdot 5^g.
\]
For \(1\le \ell<g\), let \(C_\ell\) count cycles of length \(\ell\) in the configuration multigraph. Here \(C_1\) counts loops, and \(C_2\) counts unordered pairs of parallel edges.

Direct counting gives
\[
\mathbb E C_\ell
=
\frac{(n)_\ell\,30^\ell}
{2\ell\prod_{j=0}^{\ell-1}(6n-2j-1)}.
\tag{4}
\]
Since \(n\ge g^2\), for \(\ell<g\) this implies
\[
\mathbb E C_\ell\le \frac{5^\ell}{\ell}.
\tag{5}
\]
Indeed, after replacing \((n)_\ell\) by \(n^\ell\), the extra factor relative to \(5^\ell/(2\ell)\) is at most
\[
\left(1-\frac{g}{3n}\right)^{-\ell}
\le \exp\left(\frac{2g^2}{3n}\right)<2.
\]

Let
\[
T=\sum_{\ell=1}^{g-1}\ell C_\ell.
\]
The number of vertices lying on short cycles is at most \(T\), and
\[
\mathbb ET
\le\sum_{\ell=1}^{g-1}5^\ell
<\frac{5^g}{4}.
\]
Therefore
\[
\Pr(T>5^g)<\frac14.
\]

There is consequently a configuration satisfying both:

- it remains non-3-colorable after deletion of any set of at most \(n/1000=5^g\) vertices;
- at most \(5^g\) vertices lie on cycles of length less than \(g\).

Delete all vertices lying on those short cycles. The resulting graph \(G_0\) is simple, has maximum degree at most \(6\), has girth at least \(g\), and is not 3-colorable.

### 3.3 Making the graph exactly 4-chromatic and regular

Take an inclusion-minimal non-3-colorable subgraph \(H\subseteq G_0\). As before,
\[
\chi(H)=4,\qquad \Delta(H)\le6,\qquad |V(H)|\le n.
\]

Apply Theorem 1 with \(r=6\) and \(k=4\). Since
\[
b_6(g)=\frac{3\cdot5^{g-2}-1}{2},
\]
the resulting \(6\)-regular graph \(F\) satisfies
\[
\begin{aligned}
|V(F)|
&\le 2n+8\bigl(3b_6(g)+1\bigr)\\
&=2n+36\cdot5^{g-2}-4\\
&<2002\cdot5^g.
\end{aligned}
\]
It contains \(H\), admits a proper 4-coloring, and has girth at least \(g\). Hence \(\chi(F)=4\). This proves Theorem 2. ∎

## 4. Why this does not reach degree 4

There are two distinct gaps between the construction above and the requested result.

### The random-regular first moment is on the wrong side of its threshold

For ordinary proper 3-colorings in the \(d\)-regular configuration model, the same entropy calculation gives exponential base
\[
\beta_d=3(2/3)^{d/2}.
\]
In particular,
\[
\beta_4=\frac43>1,\qquad
\beta_5=\frac{4\sqrt6}{9}>1,\qquad
\beta_6=\frac89<1.
\]

This is not merely a loose upper-bound issue. When \(n\) is divisible by \(6\), let \(X_{\rm bal}\) count proper colorings with exactly \(n/3\) vertices of each color. Direct counting yields
\[
\mathbb E X_{\rm bal}
=
\frac{n!}{((n/3)!)^3}
\frac{((dn/3)!)^3}{((dn/6)!)^3}
\frac{2^{dn/2}(dn/2)!}{(dn)!}.
\]
Stirling’s formula gives
\[
\mathbb E X_{\rm bal}
=\Theta\!\left(n^{-1}\beta_d^n\right).
\]
Thus the unweighted first-moment argument cannot prove non-3-colorability at degree \(4\) by showing that the expected number of colorings tends to zero.

A large expectation does **not** prove that every graph, or even most graphs, are 3-colorable. It only identifies a limitation of this particular method.

### Criticality does not reduce maximum degree to 4

Passing to a minimal non-3-colorable subgraph ensures exact chromatic number \(4\), but it does not ensure maximum degree \(4\). Criticality forces minimum degree at least \(3\); vertices of degree \(5\) or \(6\) may remain.

Likewise, the regularization theorem fills degree deficits—it cannot lower existing degrees while preserving non-3-colorability.

## 5. Remaining unresolved claim

The argument supplies neither:

- non-3-colorable graphs of maximum degree \(4\) and unbounded girth; nor
- a constant \(g_0\) such that every maximum-degree-4 graph of girth at least \(g_0\) is 3-colorable.

So the original yes-or-no problem remains unresolved here. The definite conclusions are the quantitative regularization theorem and the explicit degree-6 substitute above.
