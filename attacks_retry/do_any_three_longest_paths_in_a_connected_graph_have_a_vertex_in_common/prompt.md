Attack the following open graph-theory problem.

Catalog id: do_any_three_longest_paths_in_a_connected_graph_have_a_vertex_in_common
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/do_any_three_longest_paths_in_a_connected_graph_have_a_vertex_in_common/
Original entry: http://www.openproblemgarden.org/op/do_any_three_longest_paths_in_a_connected_graph_have_a_vertex_in_common
Problem attributed to: Gallai, Tibor (posted 2013-03-03)

=== Problem statement (OpenProblemGarden) ===
Title: Do any three longest paths in a connected graph have a vertex in common?
Conjecture Do any three longest paths in a connected graph have a vertex in common?

=== Discussion / context (OpenProblemGarden) ===
It is a well-known exercise that every two longest paths in a connected graph have a common vertex. Skupien [S] showed connected graphs where 7 longest paths do not share a common vertex.

=== References listed by OpenProblemGarden ===
- *[G] T. Gallai, Problem 6. In Theory of Graphs (Proc. Colloq., Tihany, 1966), 362 Academic Press, New York, 1968.
- Z. Skupień, Smallest sets of longest paths with empty intersection. Combin. Probab. Comput. 5 (1996), no. 4, 429–436.

=== Catalog page (statement + literature review) ===
Do any three longest paths in a connected graph have a vertex in common? — Graph-theory open problems

 
 Status
 partial
 high confidence
 

 Gallai's 1966 conjecture that any three longest paths in a connected graph share a common vertex remains open in general. Meaningful partial results confirm the conjecture for specific graph classes (series-parallel, outerplanar, split, $H$-free graphs with linear-forest $H$), and a 2025 paper improves the best known bound on the minimum vertex set hitting all longest paths to $O(\sqrt{n})$. An attempted general proof (arXiv:2006.16245, 2020) was withdrawn by its author as erroneous.

 Cited literature (2)

 
 
 
partial Non-Empty Intersection of Longest Paths in $H$-Free Graphs
 (2023)
 

 
 James A. Long Jr., Kevin G. Milans, Andrea Munaro · Electronic Journal of Combinatorics

Characterizes all graphs $H$ on at most 4 vertices for which every connected $H$-free graph has a single vertex meeting all longest paths; these are exactly the linear forests, confirming Gallai's property for those graph classes.
 

 
 
partial Small hitting sets for longest paths and cycles
 (2025)
 

 
 Sergey Norin, Raphael Steiner, Stephan Thomassé, Paul Wollan · arXiv preprint · arXiv:2505.08634

Proves every connected $n$-vertex graph has a set of at most $\sqrt{8n}$ vertices intersecting all longest paths, improving the previous $O(n^{2/3})$ state-of-the-art bound.
 

 

 Reviewer notes. arXiv:2006.16245 (Sarkar, 2020) claimed a full proof but was withdrawn as erroneous by the author. The Discrete Math. 2022 paper on chordal graphs (DOI 10.1016/j.disc.2022.113035) returned HTTP 403 and could not be verified; not cited. arXiv:2310.03849 (Gutiérrez–Valqui, 2023) focuses on Smith's and Hippchen's conjectures about pairwise cycle/path intersections in $k$-connected graphs, not the 3-path Gallai conjecture.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 02) (web search enabled).
 

Conjecture. Do any three longest paths in a connected graph have a vertex in common?

Discussion

It is a well-known exercise that every two longest paths in a connected graph have a common vertex. Skupien [S] showed connected graphs where 7 longest paths do not share a common vertex.

Bibliography

★ [G]
 T. Gallai, Problem 6. In Theory of Graphs (Proc. Colloq., Tihany, 1966) , 362 Academic Press, New York, 1968.

 [?]
 Z. Skupień, Smallest sets of longest paths with empty intersection. Combin. Probab. Comput. 5 (1996), no. 4, 429–436.

========================================================================

=== A PREVIOUS, UNVERIFIED ATTEMPT ===
The problem above was already attacked by `gpt-6-astra`, which reported verdict `partial` at high confidence. That attempt is reproduced below.

Treat it as a lead, not as an authority: it is unverified, it may be wrong in ways neither model noticed, and its framing may be the reason it stalled. Check anything you reuse, and say so if you discard it. Your task is the original problem, not a critique of this attempt. If you can finish what it started, do that; if a different route is better, take it.

--- previous attempt ---
```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture holds for graphs of cyclomatic number at most three, and for any triple in which two paths have at most two common vertices.",
  "would_publish": false,
  "caveats": "Self-contained special cases only; no general resolution or novelty claim."
}
```

# Partial results

Work throughout with finite, undirected, simple connected graphs. Path length means number of edges.

I do not obtain a proof or counterexample in general. I establish the following special cases and necessary conditions for a counterexample.

**Theorem.** Let \(P,Q\) be longest paths in \(G\), and put
\[
S=V(P)\cap V(Q).
\]
Each of the following conditions guarantees that every longest path meets \(S\):

1. The graph \(P\cap Q\), consisting of the common vertices and common edges, is connected.
2. \(|S|\le 2\).

Consequently:

3. Any three longest paths have a common vertex if
   \[
   \beta(G):=|E(G)|-|V(G)|+1\le 3.
   \]
4. In any counterexample triple, each pairwise path intersection has at least three vertices and at least two connected components.

Here “connected intersection” means connected using **common path edges**, not merely connected in the subgraph of \(G\) induced by the common vertices. No novelty is claimed for these special cases.

## 1. A connector formulation

First recall why two longest paths intersect. If disjoint longest paths \(A,B\), each of length \(L\), were joined by a shortest connecting path \(C\), then \(C\) would have positive length and its interior would avoid \(A\cup B\). At each attachment vertex, choose a longer half of the corresponding longest path. Concatenating those halves with \(C\) gives a simple path of length at least
\[
\frac L2+|E(C)|+\frac L2>L,
\]
a contradiction.

For the two paths \(P,Q\), let
\[
T=P\cup Q,\qquad S=V(P)\cap V(Q).
\]
Call a path \(C\) an **external connector** if its endpoints satisfy
\[
x\in V(P)\setminus S,\qquad y\in V(Q)\setminus S,
\]
and its internal vertices avoid \(T\).

If a component of \(G-S\) meets both \(P-S\) and \(Q-S\), such a connector exists: take a path in that component and look at two consecutive encounters with \(T\) at which the ownership changes from \(P\) to \(Q\).

Thus, to prove the theorem’s first two assertions, it suffices to prove the stronger separation statement
\[
\boxed{\text{No component of }G-S\text{ meets both }P-S\text{ and }Q-S.}
\tag{1}
\]
Indeed, a longest path avoiding \(S\) must nevertheless meet both \(P\) and \(Q\), contradicting (1).

## 2. When the intersection is a common subpath

Suppose \(P\cap Q\) is connected. Since it is a subgraph of a path, it is itself a path, say \(H\), with endpoints \(s,t\) and length \(c\). A one-vertex path, with \(s=t\) and \(c=0\), is allowed.

Orient both paths through \(H\) from \(s\) to \(t\). Let their left-tail lengths be \(a_P,a_Q\), and their right-tail lengths be \(b_P,b_Q\). The four tail interiors are pairwise disjoint and avoid \(H\).

Write \(L\) for the common longest-path length. Swapping left tails gives
\[
a_P+c+b_Q\le L=a_Q+c+b_Q,
\]
and
\[
a_Q+c+b_P\le L=a_P+c+b_P.
\]
Therefore
\[
a_P=a_Q=:a,\qquad b_P=b_Q=:b,
\qquad L=a+c+b.
\tag{2}
\]

Suppose an external connector \(C\) exists, with length \(d>0\). Up to reversing the paths and interchanging \(P,Q\), there are two cases.

### Case 1: Its endpoints lie in tails at the same end of \(H\)

Suppose \(x\) and \(y\) lie in the left tails, at distances \(\alpha,\gamma\) from \(s\).

Start at a right-tail endpoint, traverse that tail and \(H\), then take the left-tail prefix to \(x\), the connector, and the other left-tail suffix. Reversing the roles of \(x,y\) gives a second simple path. Their lengths are
\[
L+d+\alpha-\gamma,\qquad L+d+\gamma-\alpha.
\]
Their sum is \(2L+2d>2L\), so one is longer than \(L\).

### Case 2: Its endpoints lie at opposite ends of \(H\)

Suppose \(x\) lies in \(P\)'s left tail at distance \(\alpha\) from \(s\), and \(y\) lies in \(Q\)'s right tail at distance \(\gamma\) from \(t\).

One simple path starts at \(Q\)'s left endpoint, traverses \(H\), proceeds to \(y\), follows \(C\) backwards to \(x\), and finishes along \(P\)'s left-tail suffix. Its length is
\[
2a+c+\gamma-\alpha+d.
\]
Another starts at \(P\)'s right endpoint, traverses \(H\) backwards, proceeds to \(x\), follows \(C\), and finishes along \(Q\)'s right-tail suffix. Its length is
\[
2b+c+\alpha-\gamma+d.
\]
By (2), their sum is again \(2L+2d>2L\).

All these concatenations are simple because the tail interiors are disjoint and the connector avoids \(T\) internally. Zero-length tails cause no problem; a connector endpoint simply cannot lie in such a tail.

Both cases are impossible. Hence (1) holds, proving assertion 1.

## 3. When there are exactly two common vertices

The singleton case is already covered. Suppose now
\[
S=\{u,v\}.
\]
Orient \(P,Q\) so that both encounter \(u\) before \(v\), and denote their endpoints by \(p_-,p_+\) and \(q_-,q_+\).

Each path consists of a left tail, a \(u\)-to-\(v\) middle, and a right tail. Choosing each of these three blocks independently from \(P\) or \(Q\) always produces a simple path. Swapping one block at a time therefore shows that corresponding block lengths are equal:
\[
\begin{aligned}
|P[p_-,u]|&=|Q[q_-,u]|=a,\\
|P[u,v]|&=|Q[u,v]|=h,\\
|P[v,p_+]|&=|Q[v,q_+]|=b.
\end{aligned}
\]
In particular,
\[
L=a+h+b.
\tag{3}
\]

Suppose an external connector \(C\) exists, directed from \(x\in P-S\) to \(y\in Q-S\), and write \(d=|E(C)|>0\). Let \(\overline C\) denote its reverse.

There are four cases, up to interchanging \(P,Q\) and reversing both orientations. The following table gives two alternative simple paths in each case. Juxtaposition denotes concatenation.

| Locations of \(x,y\) | First alternative | Second alternative |
|---|---|---|
| left, left | \(P[p_+,x]\,C\,Q[y,q_-]\) | \(P[p_+,u]\,Q[u,y]\,\overline C\,P[x,p_-]\) |
| middle, middle | \(P[p_-,x]\,C\,Q[y,v]\,P[v,p_+]\) | \(P[p_-,u]\,Q[u,y]\,\overline C\,P[x,p_+]\) |
| left, right | \(Q[q_-,u]\,P[u,v]\,Q[v,y]\,\overline C\,P[x,p_-]\) | \(P[p_+,x]\,C\,Q[y,q_+]\) |
| left, middle | \(Q[q_-,u]\,P[u,x]\,C\,Q[y,v]\,P[v,p_+]\) | \(P[p_-,x]\,C\,Q[y,u]\,P[u,p_+]\) |

These are simple: the only common vertices of \(P,Q\) are \(u,v\), neither is repeated in any displayed route, and \(C\) avoids their union internally.

For completeness, the length calculations are:

- In the first, second, and fourth rows, let \(\alpha,\gamma\) be the distances of \(x,y\) from \(u\) along their respective blocks. The two lengths are
  \[
  L+d+\alpha-\gamma,\qquad L+d+\gamma-\alpha.
  \]
- In the third row, measure \(\alpha\) from \(u\) to \(x\), and \(\gamma\) from \(v\) to \(y\). The two lengths are
  \[
  L+d+a-b+\gamma-\alpha,\qquad
  L+d+b-a+\alpha-\gamma.
  \]

In every row, the sum is \(2L+2d>2L\). Thus one alternative is longer than \(L\), a contradiction.

The four rows exhaust all positions of the connector endpoints. Consequently no external connector exists, proving (1) and assertion 2.

## 4. The cyclomatic-number consequence

Suppose three longest paths \(P_1,P_2,P_3\) have empty common intersection. Let
\[
U=P_1\cup P_2\cup P_3,
\qquad
H_{ij}=P_i\cap P_j.
\]
Every \(H_{ij}\) is nonempty, by pairwise intersection of longest paths. It is a forest whose components are paths, including possibly isolated vertices. Write \(k_{ij}\) for its number of components.

By Section 2, none of the \(H_{ij}\) can be connected: otherwise the third longest path would meet its vertex set. Hence
\[
k_{12},k_{13},k_{23}\ge 2.
\tag{4}
\]

The union \(U\) is connected. Because there is no vertex common to all three paths, inclusion–exclusion has no triple-intersection term. Therefore
\[
\begin{aligned}
\beta(U)
&=|E(U)|-|V(U)|+1\\
&=\sum_{i=1}^3\bigl(|E(P_i)|-|V(P_i)|\bigr)
-\sum_{i<j}\bigl(|E(H_{ij})|-|V(H_{ij})|\bigr)+1.
\end{aligned}
\]
Each \(P_i\) is a tree, so its edge-minus-vertex count is \(-1\). Each \(H_{ij}\) is a forest with \(k_{ij}\) components, so its edge-minus-vertex count is \(-k_{ij}\). Thus
\[
\boxed{\beta(U)=k_{12}+k_{13}+k_{23}-2.}
\tag{5}
\]
Combining (4) and (5),
\[
\beta(U)\ge 4.
\]

Cyclomatic number is monotone under taking connected subgraphs: extend a spanning tree of \(U\) to one of \(G\). Thus
\[
\beta(G)\ge\beta(U)\ge4.
\]
This proves assertion 3.

Section 3 also shows that every \(H_{ij}\) in a counterexample triple must have at least three vertices, proving assertion 4.

## 5. Further restrictions on a counterexample

Two additional observations help delimit what remains.

### The union alone would be a counterexample

If a counterexample triple existed, deleting everything outside \(U=P_1\cup P_2\cup P_3\) would preserve the fact that the three paths are longest: a longer path in \(U\) would also be a longer path in \(G\).

Furthermore, every vertex of \(U\) belongs to at most two of the three paths. Consequently
\[
\Delta(U)\le4.
\]
Thus a counterexample could be chosen as the union of its three designated longest paths, with maximum degree at most four and cyclomatic number at least four.

### Intersections must interleave along each path

Let \(P=v_0v_1\cdots v_L\), and let \(Q\) be another longest path. If \(v_a\) and \(v_b\) are respectively the first and last vertices of \(P\) belonging to \(Q\), then
\[
a\le \left\lfloor\frac L2\right\rfloor,
\qquad
b\ge \left\lceil\frac L2\right\rceil.
\tag{6}
\]
Indeed, \(P[v_0,v_a]\) meets \(Q\) only at \(v_a\). Appending a longer half of \(Q\) gives
\[
a+\left\lceil L/2\right\rceil\le L.
\]
The other inequality follows from the terminal segment of \(P\).

Now suppose the triple intersection is empty. Along \(P_1\), label its intersection vertices according to whether they belong to \(P_2\) or \(P_3\). These labels are disjoint, and both occur. They cannot occur in just two runs—all \(P_2\)-labels followed by all \(P_3\)-labels, or vice versa—because (6) forces both intersection spans across the middle of \(P_1\). Hence there are at least three runs on each path.

## 6. The unresolved gap

The exchange arguments above handle a connected common segment or two common vertices. They do not control general disconnected intersections with larger components.

The counting argument reaches its first unexcluded component-count pattern at
\[
k_{12}=k_{13}=k_{23}=2,
\qquad \beta(U)=4.
\]
The small-intersection lemma further requires at least three vertices in each pairwise intersection, and the ordering observation imposes interleaving. But these restrictions do not themselves yield a contradiction.

Accordingly, the result is a complete proof of the stated special cases—not a proof of the general conjecture.
