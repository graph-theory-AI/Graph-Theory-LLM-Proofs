Attack the following open graph-theory problem.

Catalog id: large_induced_forest_in_a_planar_graph
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory » Topological Graph Theory
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/large_induced_forest_in_a_planar_graph/
Original entry: http://www.openproblemgarden.org/op/large_induced_forest_in_a_planar_graph
Problem attributed to: Abertson, Michael O., Berman, David M. (posted 2013-03-04)

=== Problem statement (OpenProblemGarden) ===
Title: Large induced forest in a planar graph.
Conjecture Every planar graph on $ n $ verices has an induced forest with at least $ n/2 $ vertices.

=== Discussion / context (OpenProblemGarden) ===
This conjecture is best possible. (See [AW]). It follows from Borodin's theorem stating that every planar graph has an acyclic $ 5 $ -colouring that every planar graph on $ n $ verices has an induced forest with at least $ 2n/5 $ vertices. The conjecture holds for planar graph with girth at least $ 5 $ , because they can be partitionned into a stable set and a forest [BG] (see also [KT]). Akiyama-Watanabe [AW] conjectured an even larger induced forest for bipartite planar graphs. Conjecture Every bipartite planar graph on $ n $ verices has an induced forest with at least $ 5n/8 $ vertices. This conjecture is also best possible. (See [AW]).

=== References listed by OpenProblemGarden ===
- *[AB] M. O. Albertson and D. M. Berman. A conjecture on planar graphs. Graph Theory and Related Topics (J. A. Bondy and U. S. R. Murty, eds.), (Academic Press, 1979), 357.
- [AW] J. Akiyama and M. Watanabe. Maximum induced forests of planar graphs. Graphs and Combinatorics 3 (1987), 201--202.
- [B] O. V. Borodin. A proof of B. Grünbaum's conjecture on the acyclic 5-colorability of planar graphs. (Russian) Dokl. Akad. Nauk SSSR 231 (1976), no. 1, 18--20.
- [BG] O. V. Borodin and A. N. Glebov. On the partition of a planar graph of girth 5 into an empty graph and an acyclic subgraph. Diskretn. Anal. Issled. Oper. Ser. 1 8:34–53, 2001
- [KT] K. Kawarabayashi and C. Thomassen. Decomposing a planar graph of girth 5 into an independent set and a forest. Journal of Combinatorial Theory, Series B 99(4):674–684, 2009.

=== Catalog page (statement + literature review) ===
Large induced forest in a planar graph. — Graph-theory open problems

 
 Status
 partial
 high confidence
 

 The Albertson–Berman conjecture that every planar graph on $n$ vertices has an induced forest on at least $n/2$ vertices remains open; the best known lower bound for general planar graphs is still $2n/5$ from Borodin's acyclic 5-coloring theorem (proved before the problem was posted). Since 2013, meaningful partial progress has been made for special graph classes: improved bounds for triangle-free planar graphs (up to $(6n+7)/11$), for bipartite planar graphs (up to $\lceil(4n+3)/7\rceil$, toward the Akiyama–Watanabe conjecture of $5n/8$), and an extension of the problem to multigraphs.

 Cited literature (5)

 
 
 
partial Large induced forests in planar graphs with girth 4 or 5
 (2014)
 

 
 François Dross, Mickael Montassier, Alexandre Pinlou · arXiv preprint · arXiv:1409.1348

Proves that every triangle-free planar graph on $n$ vertices has an induced forest on at least $(6n+7)/11$ vertices, and every planar graph of girth $\geq 5$ has one on at least $(44n+50)/69$ vertices, improving on Salavatipour's bounds.
 

 
 
partial A lower bound on the order of the largest induced forest in planar graphs with high girth
 (2015)
 

 
 François Dross, Mickael Montassier, Alexandre Pinlou · arXiv preprint · arXiv:1504.01949

Shows that a planar graph with girth $g$ and $m$ edges has a feedback vertex set of size at most $4m/(3g)$, improving on the trivial bound $2m/g$ and giving stronger induced-forest lower bounds for high-girth planar graphs.
 

 
 
partial Induced Forests in Bipartite Planar Graphs
 (2016)
 

 
 Yan Wang, Qiqin Xie, Xingxing Yu · arXiv preprint · arXiv:1605.00047

Proves via the discharging method that every simple bipartite planar graph on $n$ vertices contains an induced forest on at least $\lceil(4n+3)/7\rceil \approx 4n/7$ vertices, making progress toward the Akiyama–Watanabe conjecture of $5n/8$.
 

 
 
partial Contributions to conjectures on planar graphs: Induced Subgraphs, Treewidth, and Dominating Sets
 (2025)
 

 
 Kengo Enami, Naoki Matsumoto, Takamasa Yashima · arXiv preprint · arXiv:2506.10471

Establishes that if a planar graph has a $K_4$-minor-free induced subgraph of order at least $2n/3$, then it contains an induced forest of order at least $4n/9$, conditionally improving Borodin's $2n/5$ bound; also clarifies relations between induced outerplanar subgraphs and the Albertson–Berman conjecture.
 

 
 
partial Large induced forests in planar multigraphs
 (2026)
 

 
 Mikhail Makarov · arXiv preprint · arXiv:2601.04637

Extends the Albertson–Berman problem to multigraphs, proving $a(M) \geq n/4$ for any planar multigraph and the stronger bound $a(M) \geq 2n/5 - k/10$ when exactly $k$ vertex pairs carry parallel edges.
 

 

 Reviewer notes. The 2018 Springer paper 'A Better Bound on the Largest Induced Forests in Triangle-Free Planar Graph' by Dross, Montassier, Pinlou (Graphs and Combinatorics 34:1217–1246, 2018) reportedly improves the triangle-free bound further to 5n/9 ≈ 0.556n, but could not be verified via WebFetch due to paywall redirect; no arXiv preprint was found, so it was excluded from since_posted. The main Albertson–Berman conjecture for general planar graphs (best unconditional bound still 2n/5) remains open as of 2026.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 08) (web search enabled).
 

Conjecture. Every planar graph on $ n $ verices has an induced forest with at least $ n/2 $ vertices.

Discussion

This conjecture is best possible. (See [AW]). It follows from Borodin's theorem stating that every planar graph has an acyclic $ 5 $ -colouring that every planar graph on $ n $ verices has an induced forest with at least $ 2n/5 $ vertices. The conjecture holds for planar graph with girth at least $ 5 $ , because they can be partitionned into a stable set and a forest [BG] (see also [KT]). Akiyama-Watanabe [AW] conjectured an even larger induced forest for bipartite planar graphs. Conjecture Every bipartite planar graph on $ n $ verices has an induced forest with at least $ 5n/8 $ vertices. This conjecture is also best possible. (See [AW]).

Bibliography

★ [AB]
 M. O. Albertson and D. M. Berman. A conjecture on planar graphs. Graph Theory and Related Topics (J. A. Bondy and U. S. R. Murty, eds.), (Academic Press, 1979), 357.

 [AW]
 J. Akiyama and M. Watanabe. Maximum induced forests of planar graphs. Graphs and Combinatorics 3 (1987), 201--202.

 [B]
 O. V. Borodin. A proof of B. Grünbaum's conjecture on the acyclic 5-colorability of planar graphs. (Russian) Dokl. Akad. Nauk SSSR 231 (1976), no. 1, 18--20.

 [BG]
 O. V. Borodin and A. N. Glebov. On the partition of a planar graph of girth 5 into an empty graph and an acyclic subgraph. Diskretn. Anal. Issled. Oper. Ser. 1 8:34–53, 2001

 [KT]
 K. Kawarabayashi and C. Thomassen. Decomposing a planar graph of girth 5 into an independent set and a forest. Journal of Combinatorial Theory, Series B 99(4):674–684, 2009.

Related conjectures

 
 implied by
 Fractional vertex-arboricity ≤ 2 planar graphs
 open
 Standard fractional-covering bound, stated explicitly in the source paper's own context: |V(G)|/a(G) <= va_f(G), where a(G) is the maximum size of an induced forest. Proof: va_f is the minimum total weight of a fractional cover of V(G) by induced forests; if the total weight is w, then n = sum_v sum_{F containing v} w_F <= sum_F w_F |F| <= w * a(G). So va_f(G) <= 2 for every planar G forces a(G) >= n/2, exactly the Albertson-Berman conjecture (the target). Direction correct: the fractional statement is stronger; the converse is not claimed. Hypothesis classes match (all planar graphs on both sides).
 

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
  "one_line": "The conjecture holds in the stronger two-forest partition form when each component of the 4-core has at most two vertices of degree at least five within that core.",
  "would_publish": false,
  "caveats": "The general conjecture remains unresolved by this argument; novelty of the structural special case is not claimed."
}
```

## 1. A structural partial result

All graphs below are finite, simple, and undirected. Write
\[
a(G)=\max\{|S|:G[S]\text{ is a forest}\}.
\]

The following gives a restricted result without invoking another conjecture.

**Theorem.** Let \(K\) be the \(4\)-core of a planar graph \(G\): repeatedly delete vertices of current degree at most three. For each component \(C\) of \(K\), put
\[
h(C)=|\{v\in V(C):d_K(v)\ge 5\}|,
\qquad
\eta(G)=\sum_{C\in\operatorname{comp}(K)}\max\{h(C)-2,0\}.
\]
Then there is a set \(X\subseteq V(K)\), of size \(\eta(G)\), such that \(G-X\) can be partitioned into two induced forests. Consequently,
\[
\boxed{\quad
a(G)\ge \left\lceil\frac{|V(G)|-\eta(G)}2\right\rceil .
\quad}
\]

In particular, if every component of the \(4\)-core has at most two vertices of degree at least five, then \(G\) can be partitioned into two induced forests. This proves the conjectured \(n/2\) bound for that class. It also proves the weighted half-bound for that class, since one of the two forests has at least half the total nonnegative vertex weight.

The main ingredient is the following stronger-than-needed special case:

> **Two-exceptional-vertices theorem.** Every planar graph with at most two vertices of degree at least five can be partitioned into two induced forests.

I give a self-contained proof. I do not claim this special case is new.

## 2. A forest-coloring ordering lemma

Think of a partition into two induced forests as a red-blue vertex coloring.

**Lemma 1.** Suppose \(S\subseteq V(Q)\) is already colored red and blue, with each color inducing a forest in \(Q[S]\). Assume:

1. \(Q-S\) is connected;
2. every vertex outside \(S\) has degree at most four in \(Q\);
3. two red vertices \(r_1,r_2\in S\), lying in different red components, have a common neighbor \(z\notin S\).

Then the coloring extends to a partition of \(Q\) into two induced forests.

**Proof.** Choose a spanning tree of \(Q-S\), rooted at \(z\). Color its vertices other than \(z\) in an order in which every vertex precedes its parent.

When a vertex is colored, its parent is still uncolored, so it has at most three colored neighbors. One color therefore occurs on at most one of those neighbors. Assign that color. This creates no monochromatic cycle.

Moreover, such a step never joins two previously existing components of the assigned color. Thus \(r_1\) and \(r_2\) remain in different red components.

Finally color \(z\). If it has at most one blue neighbor, give it blue. Otherwise, its degree bound and its two red neighbors \(r_1,r_2\) imply that it has exactly those two red neighbors and exactly two blue neighbors. Giving \(z\) red joins two different red trees through a new vertex, again creating no cycle. ∎

## 3. A planar configuration lemma

We will use two elementary planar facts:

- If the graph obtained from \(B\) by adding a universal vertex is planar, then \(B\) is outerplanar: delete the universal vertex from a plane embedding, and all vertices of \(B\) lie on the resulting common face.
- A 2-connected outerplanar graph has at least two vertices of degree two. To see this, triangulate its outer polygon. For more than three vertices, the weak dual of the triangulation is a tree with at least two leaves, giving two ears; the triangle case is immediate.

**Lemma 2.** Let \(P\) be a 2-connected planar graph, and let \(p,q\) be distinct vertices. Suppose
\[
H=P-\{p,q\}
\]
is connected and every vertex of \(H\) has degree four in \(P\). Suppose also that either

- \(pq\in E(P)\), or
- \(p\) and \(q\) have no common neighbor in \(H\).

Then there are \(a\in\{p,q\}\) and \(z,b\in V(H)\) such that
\[
az,zb\in E(P),\qquad ab\notin E(P),
\qquad H-b\text{ is connected}.
\]

**Proof.** Suppose no such configuration exists. Notice first that \(\delta(H)\ge2\).

If \(H\) is 2-connected, let \(U=V(H)\). Otherwise, take any endblock \(B\) of \(H\), let \(c\) be its unique cutvertex, and put
\[
U=V(B)\setminus\{c\}.
\]
Such an endblock is 2-connected: a bridge endblock would have a non-cutvertex of degree one in \(H\), contradicting \(\delta(H)\ge2\).

In either situation, \(H[U]\) is connected and every vertex of \(U\) is a non-cutvertex of \(H\). Consequently, for each \(a\in\{p,q\}\), either every vertex of \(U\) is adjacent to \(a\), or none is. Indeed, otherwise a path in \(H[U]\) contains an edge \(zb\) with \(z\) adjacent to \(a\) and \(b\) not adjacent to \(a\); since \(b\) is a non-cutvertex of \(H\), this is the forbidden configuration.

At least one of \(p,q\) is adjacent to \(U\). For an endblock, otherwise \(c\) would be a cutvertex of \(P\). When \(U=V(H)\), both \(p\) and \(q\) have a neighbor in \(H\), by 2-connectivity of \(P\), and hence both are adjacent to all of \(U\).

We next rule out an endblock for which exactly one of \(p,q\), say \(a\), is adjacent to \(U\). Every \(u\in U\) then has
\[
d_B(u)=4-1=3.
\]
The only neighbors of \(U\) outside \(U\) are \(a\) and \(c\). There is an \(a\)-\(c\) path in \(P-U\): otherwise, since \(H-U\) is connected and contains a vertex besides \(c\), deleting \(c\) would disconnect \(P\).

Contract this path to an edge, without identifying its endpoints, and delete everything else outside \(B\cup\{a\}\). The resulting planar minor is the cone over \(B\). Thus \(B\) is outerplanar. But every vertex of \(B\) except possibly \(c\) has degree three, contradicting the existence of two degree-two vertices in a 2-connected outerplanar graph.

It follows that both \(p\) and \(q\) are adjacent to every vertex of every such \(U\). In particular, they have a common neighbor. The hypothesis therefore forces
\[
pq\in E(P).
\]

There are now two cases.

- **\(H\) is 2-connected.** Every vertex of \(H\) has degree two in \(H\), so \(H\) is a cycle. Choose adjacent vertices \(u_1,u_2\). The graph
  \[
  R=H-\{u_1,u_2\}
  \]
  is nonempty and connected. Each \(u_i\) has a neighbor in \(R\), and every vertex of \(R\) is adjacent to both \(p,q\). Contracting \(R\) gives a \(K_5\) minor on \(p,q,u_1,u_2\) and the contracted vertex.

- **\(H\) has a cutvertex.** For each endblock \(B\), every vertex of \(B-c\) has degree two in \(B\), so 2-connectivity forces \(B\) to be a cycle. Choose adjacent \(u_1,u_2\in V(B)\setminus\{c\}\). Then \(R=H-\{u_1,u_2\}\) is connected, and each \(u_i\) has a neighbor in \(R\). A different endblock supplies a vertex of \(R\) adjacent to both \(p,q\). Again, contracting \(R\) gives a \(K_5\) minor.

Both cases contradict planarity. ∎

## 4. Extending a prescribed coloring of an edge

**Proposition 3.** Let \(Q\) be planar, and let \(pq\in E(Q)\). If every vertex outside \(\{p,q\}\) has degree at most four, then any prescribed distinct colors on \(p,q\) extend to a partition of \(Q\) into two induced forests.

**Proof.** Suppose otherwise, and take a counterexample with the fewest vertices.

A nonterminal vertex of degree at most three can be deleted, followed by induction and reinsertion in a color occurring on at most one neighbor. Thus every nonterminal vertex has degree four.

The counterexample is connected. Components not containing \(pq\) can be colored by minimality, using any edge as the distinguished edge; isolated vertices are trivial.

It has no cutvertex either. At a cutvertex, first color the piece containing \(pq\). In every other piece, all vertices except possibly the attachment vertex have degree at most four. Apply minimality with an edge incident with that attachment as the distinguished edge, prescribing its color to agree with the first piece. Forests glued at one vertex remain forests.

The two-vertex case is immediate, so \(Q\) is 2-connected.

Put \(H=Q-\{p,q\}\). If \(H\) is disconnected, apply minimality to each graph consisting of one component of \(H\) together with \(p,q\). Prescribe the same distinct colors on \(p,q\) in every piece. Each monochromatic union glues only at one of \(p,q\), so the color classes remain forests. Hence \(H\) is connected.

Apply Lemma 2. It gives \(a\in\{p,q\}\) and \(z,b\in H\) with
\[
az,zb\in E(Q),\quad ab\notin E(Q),\quad H-b\text{ connected}.
\]
Give \(b\) the prescribed color of \(a\). In the precolored set \(\{p,q,b\}\), the same-colored vertices \(a,b\) are nonadjacent and therefore belong to different monochromatic components. Lemma 1, rooted at \(z\), completes the coloring. This is a contradiction. ∎

## 5. Proof of the two-exceptional-vertices theorem

**Proposition 4.** Every planar graph with at most two vertices of degree at least five can be partitioned into two induced forests.

**Proof.** Take a smallest counterexample \(G\). The usual deletion and gluing arguments show that \(G\) is 2-connected and has minimum degree at least four:

- a vertex of degree at most three can be reinserted in a color occurring on at most one neighbor;
- colorings of pieces at a cutvertex can be matched by interchanging red and blue in individual pieces.

If there is at most one vertex of degree at least five, choose an edge containing it, or any edge if there is no such vertex. Proposition 3 applies. The same proposition applies if the two high-degree vertices are adjacent.

Thus there are exactly two high-degree vertices \(p,q\), they are nonadjacent, and every other vertex has degree four. Put
\[
H=G-\{p,q\}.
\]

### Case 1: \(H\) is disconnected

Every component of \(H\) has a neighbor of each of \(p,q\), since \(G\) is 2-connected.

For a component \(C\), define
\[
G_C=G[V(C)\cup\{p,q\}]+pq.
\]
This graph is planar. Indeed, another component of \(H\) contains the internal vertices of a \(p\)-\(q\) path; contracting that path to an edge, while retaining \(p,q\), exhibits \(G_C\) as a planar minor.

Apply Proposition 3 to each \(G_C\), prescribing \(p\) red and \(q\) blue. Delete the added edge and combine the colorings. Red pieces meet only at \(p\), and blue pieces only at \(q\), so both color classes are forests.

### Case 2: \(H\) is connected and \(p,q\) have a common neighbor

Precolor \(p,q\) red. They are nonadjacent, hence lie in different red components. Lemma 1, rooted at a common neighbor, completes the coloring.

### Case 3: \(H\) is connected and \(p,q\) have no common neighbor

Apply Lemma 2. Precolor \(p,q\) differently, and give its vertex \(b\) the color of the corresponding terminal \(a\). Lemma 1 again completes the coloring.

All cases contradict the choice of \(G\). ∎

## 6. Passing to the \(4\)-core

We now prove the theorem from Section 1.

In each component \(C\) of \(K\), delete all but two of its vertices of degree at least five, deleting none if there are at most two. Let \(X\) be the resulting deletion set. Then
\[
|X|=\eta(G).
\]

Every component of \(K-X\) has at most two vertices of degree at least five: deletion cannot increase degrees or join components. Proposition 4 therefore partitions \(K-X\) into two induced forests.

Now reinsert the vertices deleted during the construction of the \(4\)-core, in reverse order. Each has at most three already present neighbors. It can consequently be assigned a color appearing on at most one of those neighbors. This preserves both induced forests and produces a two-forest partition of \(G-X\).

The larger color class has size at least
\[
\left\lceil\frac{n-|X|}{2}\right\rceil
=
\left\lceil\frac{n-\eta(G)}2\right\rceil,
\]
as claimed. ∎

There is also a blockwise strengthening of the zero-defect case:

> It suffices that every block of the \(4\)-core has at most two vertices of degree at least five **measured within that block**.

Apply Proposition 4 block by block, matching colors at cutvertices, and then reinsert the peeled vertices.

## 7. What this achieves—and what remains open

Combining the parameterized bound with the \(2n/5\) bound supplied in the question gives
\[
a(G)\ge
\max\left\{
\left\lceil\frac{2n}{5}\right\rceil,\,
\left\lceil\frac{n-\eta(G)}2\right\rceil
\right\}.
\]
The second unrounded bound improves on \(2n/5\) when \(\eta(G)<n/5\).

The half-bound is sharp even in the zero-defect class: disjoint copies of \(K_4\) have empty \(4\)-core, and every induced forest contains at most two vertices from each copy.

The limitation is explicit. For a connected planar graph of minimum degree at least five,
\[
K=G,\qquad \eta(G)=n-2,
\]
so the new parameterized estimate alone gives only \(a(G)\ge1\). Thus this argument does not control a core containing many high-degree vertices—the case needed for a general resolution.

**No proof or counterexample for the unrestricted Albertson–Berman conjecture is obtained.**
