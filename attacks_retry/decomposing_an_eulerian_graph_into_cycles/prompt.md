Attack the following open graph-theory problem.

Catalog id: decomposing_an_eulerian_graph_into_cycles
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory » Basic Graph Theory » Cycles
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/decomposing_an_eulerian_graph_into_cycles/
Original entry: http://www.openproblemgarden.org/op/decomposing_an_eulerian_graph_into_cycles
Problem attributed to: Hajós, G. (posted 2013-03-04)

=== Problem statement (OpenProblemGarden) ===
Title: Decomposing an eulerian graph into cycles.
Conjecture Every simple eulerian graph on $ n $ vertices can be decomposed into at most $ \frac{1}{2}(n-1) $ cycles.

=== Discussion / context (OpenProblemGarden) ===
This conjecture is tight because a complete graph on $ 2k+1 $ vertices cannot be covered by less than $ k $ cycles. There is a similar conjecture about decomposition of a connected graph into paths .

=== References listed by OpenProblemGarden ===
- * [L] L. Lovász, On covering of graphs. In Theory of Graphs (Proc. Colloq., Tihany, 1966), 231--236. Academic Press, New York, 1968.

=== Catalog page (statement + literature review) ===
Decomposing an eulerian graph into cycles. — Graph-theory open problems

 
 Status
 partial
 high confidence
 

 Hajós' 1968 conjecture — that every simple Eulerian graph on $n$ vertices decomposes into at most $\lfloor (n-1)/2 \rfloor$ cycles — is still open in general. Since the OPG posting date (2013), it has been verified for several restricted classes: graphs of treewidth at most 3 (Botler–Sambinelli–Coelho–Lee, 2017), Eulerian graphs of pathwidth at most 6 (Fuchs–Gellert–Heinrich, 2017), and computationally for all Eulerian graphs of order at most 12 (Heinrich–Natale–Streicher, 2017). Approximate versions in dense graphs and progress on the closely related Erdős–Gallai cycle decomposition problem (Bucić–Montgomery, 2022) have also appeared.

 Cited literature (3)

 
 
 
partial On Gallai's and Hajós' Conjectures for graphs with treewidth at most 3
 (2017)
 

 
 Fábio Botler, Maycon Sambinelli, Rafael S. Coelho, Orlando Lee · arXiv preprint · arXiv:1706.04334

Verifies both Gallai's path decomposition conjecture and Hajós' cycle decomposition conjecture for graphs of treewidth at most 3.
 

 
 
partial Cycle decompositions of pathwidth-6 graphs
 (2017)
 

 
 Elke Fuchs, Laura Gellert, Irene Heinrich · arXiv preprint (later in J. Graph Theory, 2020) · arXiv:1705.07066

Verifies Hajós' conjecture for Eulerian graphs of pathwidth at most 6 and shows these graphs satisfy the small cycle double cover conjecture.
 

 
 
partial Hajós' cycle conjecture for small graphs
 (2017)
 

 
 Irene Heinrich, Marco V. Natale, Manuel Streicher · arXiv preprint · arXiv:1705.08724

Computationally verifies Hajós' conjecture for all simple Eulerian graphs on at most 12 vertices using preprocessing, heuristics, and integer programming.
 

 

 Reviewer notes. Search results also mentioned an approximate Hajós result for dense graphs by Girão, Granet, Kühn, Osthus (Path and cycle decompositions of dense graphs, arXiv:1911.05501) — not verified in detail here. Bucić–Montgomery (arXiv:2211.07689) addresses the related Erdős–Gallai cycle decomposition conjecture, not Hajós directly, so it is not cited as evidence on this problem.

 
 Auto-reviewed 2026-05-08 with claude (main agent, web search + fetch) (web search enabled).
 

Conjecture. Every simple eulerian graph on $ n $ vertices can be decomposed into at most $ \frac{1}{2}(n-1) $ cycles.

Discussion

This conjecture is tight because a complete graph on $ 2k+1 $ vertices cannot be covered by less than $ k $ cycles. There is a similar conjecture about decomposition of a connected graph into paths .

Bibliography

★ [L]
 L. Lovász, On covering of graphs. In Theory of Graphs (Proc. Colloq., Tihany, 1966), 231--236. Academic Press, New York, 1968.

========================================================================

=== A PREVIOUS, UNVERIFIED ATTEMPT ===
The problem above was already attacked by `gpt-6-astra`, which reported verdict `partial` at high confidence. That attempt is reproduced below.

Treat it as a lead, not as an authority: it is unverified, it may be wrong in ways neither model noticed, and its framing may be the reason it stalled. Check anything you reuse, and say so if you discard it. Your task is the original problem, not a critique of this attempt. If you can finish what it started, do that; if a different route is better, take it.

--- previous attempt ---
```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "Hajós' bound is proved here for graphs of maximum degree four admitting a triangle decomposition, with the stronger bound n/3 in the 4-regular case.",
  "would_publish": false,
  "caveats": "This is a restricted-class result, not a resolution of the conjecture; novelty is not claimed."
}
```

## 1. A rigorous special case

Write \(c(G)\) for the minimum number of simple cycles in an edge-decomposition of an Eulerian graph \(G\).

The general conjecture is not resolved here. The following special case, including a stronger bound for its regular members, can be proved completely.

**Theorem.** Let \(G\) be a connected simple graph with at least one edge, maximum degree at most four, and an edge-decomposition into triangles. Then
\[
c(G)\le \left\lfloor\frac{|V(G)|-1}{2}\right\rfloor.
\]
If \(G\) is 4-regular, then the stronger bound
\[
c(G)\le \frac{|V(G)|}{3}
\]
holds.

The coefficient \(1/3\) in the second bound is asymptotically best possible within this class.

A triangle decomposition automatically makes all degrees even. Thus the theorem concerns a natural subclass of the graphs in Hajós’ conjecture. The proof uses the classical, proved perfect-matching theorem of Tutte; it does not assume another conjecture.

## 2. Encoding the triangle decomposition

Let \(\mathcal T\) be a triangle decomposition of \(G\). Every vertex of \(G\) belongs to either one or two members of \(\mathcal T\), according as its degree is two or four.

Construct a graph \(H\) as follows.

- For every triangle \(T\in\mathcal T\), introduce a vertex \(x_T\).
- A vertex of \(G\) belonging to two triangles \(T,U\) gives an edge \(x_Tx_U\).
- A vertex belonging to just one triangle \(T\) gives an edge from \(x_T\) to a new leaf.

Distinct triangles in an edge-decomposition cannot share two vertices: they would then share the edge between those vertices. Consequently, \(H\) is simple. Every \(x_T\) has degree three, and every other vertex has degree one.

There is a natural isomorphism
\[
G\cong L(H),
\]
where \(L(H)\) denotes the line graph of \(H\). Indeed, vertices of \(G\) correspond bijectively to edges of \(H\), and adjacency in \(G\) is precisely incidence at one of the vertices \(x_T\).

Thus it suffices to study line graphs of connected simple graphs whose degrees belong to \(\{1,3\}\). If \(G\) is 4-regular, its auxiliary graph \(H\) is cubic.

## 3. Recombining triangles along cycles

Suppose henceforth that \(H\) is simple and all its vertex degrees belong to \(\{1,3\}\). Let \(t\) be its number of degree-three vertices.

For each degree-three vertex \(v\), the three edges incident with \(v\) give a triangle \(T_v\) in \(L(H)\). These \(t\) triangles partition \(E(L(H))\).

For a family \(\mathcal F\) of vertex-disjoint cycles in \(H\), define
\[
W(\mathcal F)=\sum_{C\in\mathcal F}(|V(C)|-2).
\]

**Recombination lemma.**
\[
c(L(H))\le t-W(\mathcal F).
\tag{1}
\]

**Proof.** We show that the triangles corresponding to the vertices of any \(k\) vertex-disjoint cycles can be replaced by \(2k\) simple cycles.

At each vertex \(v\) of these cycles, let \(s_v\) be its unique incident edge outside the cycle family. Assign \(v\) one of two colors, red and blue, subject to the following condition: if
\[
s_v=s_w,
\]
then \(v,w\) receive opposite colors. These constraints form a matching, so such an assignment exists.

Consider one selected cycle
\[
C=v_1v_2\cdots v_\ell v_1,
\]
with edges \(e_i=v_iv_{i+1}\), subscripts taken cyclically. In \(L(H)\), the triangle \(T_{v_i}\) has vertices
\[
e_{i-1},e_i,s_{v_i}.
\]
It contains two edge-disjoint paths between \(e_{i-1}\) and \(e_i\): the direct edge and the two-edge path through \(s_{v_i}\).

Give the two-edge path to the color assigned to \(v_i\), and give the direct edge to the other color. Concatenating the red paths around \(C\) produces one cycle; concatenating the blue paths produces another.

These cycles are simple. The vertices \(e_i\) are distinct. An extra vertex \(s_v\) can coincide with \(s_w\) only when it represents the edge \(vw\), and the opposite-color condition prevents that vertex from appearing twice in either constructed cycle. Also, no \(s_v\) is an edge of the original cycle family.

The two cycles partition all edges of the triangles \(T_v\) with \(v\in V(C)\). Keeping the other triangles gives
\[
t-\sum_{C\in\mathcal F}|V(C)|+2|\mathcal F|
=t-W(\mathcal F)
\]
cycles, proving (1). \(\square\)

We now need a sufficiently heavy family of vertex-disjoint cycles in a subcubic graph.

## 4. A weighted cycle-packing lemma

We first record the matching fact used below.

**Matching fact.** In a connected bridgeless loopless cubic multigraph, every edge belongs to a perfect matching. Consequently, any specified edge can be omitted from some perfect matching.

**Proof.** Fix an edge \(uv\) of such a multigraph \(K\). For \(S\subseteq V(K)\setminus\{u,v\}\), let \(q\) be the number of odd components of
\[
K-\{u,v\}-S.
\]
Each such component has an odd edge-boundary in \(K\). Since \(K\) has no bridges, that boundary has size at least three. Counting edges from these components into \(S\cup\{u,v\}\) gives
\[
3q\le 3|S|+4.
\]
The term \(4\) is valid even with parallel edges, since at least one edge joins \(u\) to \(v\).

The order of a cubic multigraph is even, so
\[
q\equiv |S|\pmod 2.
\]
Together with \(q\le |S|+1\), this yields \(q\le |S|\). Tutte’s perfect-matching criterion therefore gives a perfect matching of \(K-\{u,v\}\); adding \(uv\) proves the first assertion.

For the second, choose a different edge incident with an endpoint of the specified edge and take a perfect matching containing that different edge. \(\square\)

**Weighted packing lemma.** Let \(B\) be a connected bridgeless simple graph with at least one edge and maximum degree at most three. Let \(s\) and \(d\) be its numbers of degree-three and degree-two vertices. There is a family \(\mathcal F\) of vertex-disjoint cycles covering every degree-three vertex such that
\[
W(\mathcal F)\ge
\begin{cases}
s/2,&d=0,\\[2mm]
s/2+1,&d>0.
\end{cases}
\tag{2}
\]

**Proof.** Since \(B\) is connected and bridgeless, its degrees are two or three, and \(s\) is even. We use induction on \(|V(B)|\).

If \(s=0\), then \(B\) is a cycle, and taking that cycle gives
\[
W=|V(B)|-2\ge 1.
\]
For \(B=K_4\), take a Hamilton cycle, obtaining \(W=2=s/2\). For \(B=K_4-e\), take its four-cycle, obtaining \(W=2=s/2+1\).

### Case 1: \(B\) is triangle-free

Suppose \(s>0\). Suppress all degree-two vertices to obtain a connected bridgeless cubic multigraph \(K\). It has no loops: a loop at a cubic vertex would force its remaining incident edge to be a bridge.

If \(d=0\), choose any perfect matching of \(K=B\). If \(d>0\), choose a degree-two vertex \(z\) of \(B\), and let \(e\) be the edge of \(K\) whose subdivided path contains \(z\). Choose a perfect matching of \(K\) omitting \(e\).

The complementary 2-factor lifts to vertex-disjoint cycles in \(B\), covering all its degree-three vertices and, when \(d>0\), also covering \(z\). Parallel-edge two-cycles in \(K\), if present, lift to simple cycles in \(B\).

Since \(B\) is triangle-free, every lifted cycle has length at least four. Hence
\[
W(\mathcal F)
=\sum_{C\in\mathcal F}(|V(C)|-2)
\ge \frac{|V(\mathcal F)|}{2}.
\]
This is at least \(s/2\) when \(d=0\). When \(d>0\), it is at least \((s+1)/2\), and integrality gives \(W(\mathcal F)\ge s/2+1\).

### Case 2: Two triangles share an edge

Apart from \(K_4\), two such triangles form a diamond. Denote their common edge by \(ab\), and their other vertices by \(c,d\).

The case \(B=K_4-e\) was handled above. Otherwise all four diamond vertices have degree three. Indeed, the vertices \(a,b\) already have degree three, while exactly one edge leaving the diamond would be a bridge.

Form
\[
B'=B-\{a,b\}+cd.
\]
Here \(cd\) was not already an edge, since otherwise \(B=K_4\). Thus \(B'\) is simple, with degree counts
\[
s'=s-4,\qquad d'=d+2.
\]
It is connected and bridgeless. For completeness, a bridge of \(B'\) other than \(cd\) would lift to a bridge of \(B\). If \(cd\) were a bridge, then the other edge incident with the degree-two vertex \(c\) would also be a bridge, again giving a contradiction.

Apply induction to \(B'\). Since \(c,d\) are adjacent degree-two vertices, a cycle family either uses both, including the edge \(cd\), or omits both.

- If it uses \(cd\), replace that edge by the path \(c\,a\,b\,d\).
- If it omits both vertices, add the four-cycle \(c\,a\,d\,b\,c\).

In either case all original degree-three vertices are covered, and the weight increases by two. Therefore
\[
W(\mathcal F)\ge \frac{s-4}{2}+1+2=\frac{s}{2}+1,
\]
which suffices in both alternatives of (2).

### Case 3: There is a triangle, but no two triangles share an edge

Choose a triangle \(T\). It has either two or three edges leaving it: zero would make \(B=T\), and one would be a bridge.

Its external neighbors are distinct. Otherwise two vertices of \(T\), together with a common external neighbor, would form another triangle sharing an edge with \(T\).

Contract \(T\) to a vertex \(x\), obtaining a simple connected bridgeless graph \(B'\) with
\[
s'=s-2,\qquad d'=d.
\]
Apply induction.

If \(x\) lies on a selected cycle, lift the passage through \(x\) to a path through all three vertices of \(T\). This increases the weight by two.

If \(x\) is omitted, it must have degree two, because all degree-three vertices are covered. Add \(T\) as a separate cycle, increasing the weight by one.

Thus in either event the weight increases by at least one, which gives precisely the required bound (2). All degree-three vertices remain covered.

These cases exhaust \(B\), completing the induction. \(\square\)

## 5. Applying the packing lemma

Return to a connected simple graph \(H\) whose degrees belong to \(\{1,3\}\). Put
\[
N=|E(H)|=|V(L(H))|,
\qquad
t=|\{v:d_H(v)=3\}|,
\]
and let
\[
r=|E(H)|-|V(H)|+1
\]
be its cycle rank. The degree sum gives
\[
N=2t+1-r.
\tag{3}
\]

### If \(H\) is bridgeless

Then \(H\) is cubic. The weighted packing lemma gives a cycle family of weight at least \(t/2\). By (1),
\[
c(L(H))\le \frac t2=\frac N3.
\tag{4}
\]
In particular this is at most \((N-1)/2\), since the relevant line graphs have \(N\ge 3\).

### If \(H\) has a bridge

Delete all bridges. Let \(B_1,\dots,B_q\) be the resulting components containing edges; ignore isolated vertices.

Each \(B_i\) is simple, connected, bridgeless and subcubic. Moreover, each has a degree-two vertex: it is incident in \(H\) with a deleted bridge, and \(H\) is connected.

If \(s_i\) is the number of degree-three vertices inside \(B_i\), then
\[
r(B_i)=\frac{s_i}{2}+1.
\]
The weighted packing lemma supplies a cycle family in \(B_i\) of weight at least \(r(B_i)\). These families are vertex-disjoint across components. Deleting bridges preserves total cycle rank, so their union \(\mathcal F\) satisfies
\[
W(\mathcal F)\ge \sum_i r(B_i)=r.
\]
Consequently, by (1) and (3),
\[
c(L(H))
\le t-r
=\frac{N-1-r}{2}
\le \frac{N-1}{2}.
\tag{5}
\]
Since the cycle count is integral, this proves Hajós’ bound.

If \(H\) is cubic and has a bridge, then \(r=t/2+1\), so (5) strengthens to
\[
c(L(H))\le \frac t2-1=\frac N3-1.
\tag{6}
\]

The encoding in Section 2 now proves the theorem. Disconnected graphs, if included in the convention for “Eulerian”, follow componentwise; isolated vertices cause no difficulty.

## 6. Sharpness within the special class

For the general part of the theorem, take a chain of \(k\) triangles, with successive triangles meeting in one vertex and no vertex belonging to three triangles. This graph has maximum degree four and \(2k+1\) vertices. Its cycle blocks are exactly those \(k\) triangles, so
\[
c(G)=k=\frac{|V(G)|-1}{2}.
\]

The stronger \(n/3\) coefficient for 4-regular graphs is also asymptotically sharp.

Take a tree with \(\ell\ge2\) leaves and all other vertices of degree three; it has \(\ell-2\) internal vertices. Replace each leaf by a copy of \(K_4\) with one edge subdivided once, attaching the former tree edge at the subdivision vertex. The resulting graph \(H_\ell\) is simple and cubic, with
\[
|V(H_\ell)|=5\ell+(\ell-2)=6\ell-2.
\]
Therefore
\[
G_\ell=L(H_\ell)
\]
is simple, connected, 4-regular and triangle-decomposable, with
\[
|V(G_\ell)|=9\ell-3.
\]

Its edge set separates into:

- \(\ell\) leaf-gadget pieces, each containing a vertex of degree four within that piece and hence requiring at least two cycles;
- \(\ell-2\) triangle pieces, each requiring one cycle.

These pieces are joined only at cutvertices. A simple cycle cannot use edges from different pieces. Thus
\[
c(G_\ell)\ge 2\ell+(\ell-2)=3\ell-2.
\]
Since \(H_\ell\) has bridges, (6) gives the reverse inequality. Hence
\[
c(G_\ell)=3\ell-2=\frac{|V(G_\ell)|}{3}-1.
\]

## 7. What remains unresolved

The essential restrictions are the **pre-existing triangle decomposition** and **maximum degree four**. Together they produce an auxiliary graph with degrees only one and three. Cubicity is what makes both the matching argument and the two-color recombination work.

An arbitrary Eulerian graph need not have this structure. Nothing above establishes Hajós’ conjecture outside the stated class.

I make no claim of novelty for this special case or its bounds; their literature status has not been independently checked here. The result is a complete restricted-class proof, not a proposed proof of the full conjecture.
