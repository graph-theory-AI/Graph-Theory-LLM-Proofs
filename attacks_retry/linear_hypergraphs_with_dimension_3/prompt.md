Attack the following open graph-theory problem.

Catalog id: linear_hypergraphs_with_dimension_3
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory » Topological Graph Theory » Drawings
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/linear_hypergraphs_with_dimension_3/
Original entry: http://www.openproblemgarden.org/op/linear_hypergraphs_with_dimension_3
Problem attributed to: de Fraysseix, Hubert, Ossona de Mendez, Patrice, Rosenstiehl, Pierre (posted 2007-09-26)

=== Problem statement (OpenProblemGarden) ===
Title: Linear Hypergraphs with Dimension 3
Conjecture Any linear hypergraph with incidence poset of dimension at most 3 is the intersection hypergraph of a family of triangles and segments in the plane.

=== Discussion / context (OpenProblemGarden) ===
A hypergraph is linear if any two edges may share at most one vertex. The incidence poset of a hypergraph is the vertex-edge inclusion poset. The dimension of a poset $ P $ is the minimum number of linear extentions of $ P $ , whose intersection is $ P $ [DM]. Schnyder proved that the incidence poset of a graph $ G $ has dimension at most $ 3 $ if and only if $ G $ is planar [S89]. Fraysseix, Rosenstiehl and Ossona de Mendez proved that every planar graph has a representation by contacts of triangles [FOR94] and Scheinerman conjectured that every planar graph has a representation by intersection of segments [S84] (claimed to be proved by Gonçalves et al.). A hypergraph is planar if its vertex-edge incidence graph is planar [W]. Fraysseix, Rosenstiehl and Ossona de Mendez proved that every planar linear hypergraph has a representation by contacts of triangles [FOR07] and it has been conjectured that they have a representation by intersection of straight line segments [FO07] (cf Straight line representation of planar linear hypergraphs ). Although the incidence poset of a simple planar hypergraph has dimension at most $ 3 $ (what follows from [BT]), the converse is false: The linear hypergraph with vertices $ 1,\dots,5 $ and edge set $ \{\{1,2\},\{2,3\},\{3,4\},\{1,4\},\{1,3,5\},\{2,4,5\}\} $ has incidence dimension $ 3 $ but is not planar (its vertex-edge incidence graph is a subdivision of $ K_{3,3} $ ). It follows from [O] that the vertices of simple hypergraphs with incidence posets of dimensions $ d $ can be represented by convex sets of the Euclidean space of dimension $ d-1 $ , in such a way that the edges of the hypergraph are exactly the maximal subsets of vertices, such that the corresponding subset of convexes has a non-empty intersection.

=== References listed by OpenProblemGarden ===
- [BT] G.~Brightwell and W.T. Trotter, The order dimension of planar maps, SIAM journal on Discrete Mathematics 10 (1997), no.~4, 515--528.
- [DM] B.~Dushnik and E.W. Miller, Partially ordered sets, Amer. J. Math. 63 (1941), 600--610.
- [FO07] Hubert de Fraysseix, Patrice Ossona de Mendez: Stretching of Jordan arc contact systems, Discrete Applied Mathematics 155 (2007), no. 9, 1079--1095.
- [FOR94] H.~de Fraysseix, P.~Ossona~de Mendez, and P.~Rosenstiehl, On triangle contact graphs, Combinatorics, Probability and Computing 3 (1994), 233--246.
- *[FOR07] H.~de Fraysseix, P.~Ossona~de Mendez, and P.~Rosenstiehl, Representation of Planar Hypergraphs by Contacts of Triangles, Proc. of Graph Drawing '07, to appear.
- [O] P.~Ossona~de Mendez, Realization of posets, Journal of Graph Algorithms and Applications 6 (2002), no.~1, 149--153.
- [S84] E.R. Scheinerman, Intersection classes and multiple intersection parameters of graphs, Ph.D. thesis, Princeton University, 1984.
- [S89] W.~Schnyder, Planar graphs and poset dimension, Order 5 (1989), 323--343.
- [W] T.R.S. Walsh, Hypermaps versus bipartite maps, J. Combinatorial Theory 18(B) (1975), 155--163.

=== Catalog page (statement + literature review) ===
Linear Hypergraphs with Dimension 3 — Graph-theory open problems

 
 Status
 open
 medium confidence
 

 The conjecture that any linear hypergraph whose incidence poset has dimension at most 3 is the intersection hypergraph of a family of triangles and segments in the plane was posted in 2007 and remains open to the best of available evidence. No proof, disproof, or substantial partial result addressing the conjecture as stated could be found in the literature after the posting date. The closely related special case of planar linear hypergraphs was established by de Fraysseix, Ossona de Mendez, and Rosenstiehl (contacts of triangles), but the full poset-dimension-3 conjecture extends beyond planarity and no resolution has been verified.

 Reviewer notes. The Open Problem Garden page was unreachable (ECONNREFUSED), so no on-site status update could be verified. Searches turned up no post-2007 paper specifically addressing this conjecture. The arXiv paper 2411.13985 (Representing Hypergraphs by Point-Line Incidences, 2024) is thematically adjacent but does not address the incidence-poset-dimension-3 conjecture. The Sparsity and Dimension paper (arXiv:1507.01120) addresses poset dimension in the context of sparse graphs but not this hypergraph geometric realization conjecture. Confidence is medium rather than high because exhaustive search of Ossona de Mendez's publication list was not possible (arXiv search timed out).

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 01) (web search enabled).
 

Conjecture. Any linear hypergraph with incidence poset of dimension at most 3 is the intersection hypergraph of a family of triangles and segments in the plane.

Keywords:
Hypergraphs

Discussion

A hypergraph is linear if any two edges may share at most one vertex. The incidence poset of a hypergraph is the vertex-edge inclusion poset. The dimension of a poset $ P $ is the minimum number of linear extentions of $ P $ , whose intersection is $ P $ [DM]. Schnyder proved that the incidence poset of a graph $ G $ has dimension at most $ 3 $ if and only if $ G $ is planar [S89]. Fraysseix, Rosenstiehl and Ossona de Mendez proved that every planar graph has a representation by contacts of triangles [FOR94] and Scheinerman conjectured that every planar graph has a representation by intersection of segments [S84] (claimed to be proved by Gonçalves et al.). A hypergraph is planar if its vertex-edge incidence graph is planar [W]. Fraysseix, Rosenstiehl and Ossona de Mendez proved that every planar linear hypergraph has a representation by contacts of triangles [FOR07] and it has been conjectured that they have a representation by intersection of straight line segments [FO07] (cf Straight line representation of planar linear hypergraphs ). Although the incidence poset of a simple planar hypergraph has dimension at most $ 3 $ (what follows from [BT]), the converse is false: The linear hypergraph with vertices $ 1,\dots,5 $ and edge set $ \{\{1,2\},\{2,3\},\{3,4\},\{1,4\},\{1,3,5\},\{2,4,5\}\} $ has incidence dimension $ 3 $ but is not planar (its vertex-edge incidence graph is a subdivision of $ K_{3,3} $ ). It follows from [O] that the vertices of simple hypergraphs with incidence posets of dimensions $ d $ can be represented by convex sets of the Euclidean space of dimension $ d-1 $ , in such a way that the edges of the hypergraph are exactly the maximal subsets of vertices, such that the corresponding subset of convexes has a non-empty intersection.

Bibliography

 [BT]
 G.~Brightwell and W.T. Trotter, The order dimension of planar maps, SIAM journal on Discrete Mathematics 10 (1997), no.~4, 515--528.

 [DM]
 B.~Dushnik and E.W. Miller, Partially ordered sets, Amer. J. Math. 63 (1941), 600--610.

 [FO07]
 Hubert de Fraysseix, Patrice Ossona de Mendez: Stretching of Jordan arc contact systems, Discrete Applied Mathematics 155 (2007), no. 9, 1079--1095.

 [FOR94]
 H.~de Fraysseix, P.~Ossona~de Mendez, and P.~Rosenstiehl, On triangle contact graphs, Combinatorics, Probability and Computing 3 (1994), 233--246.

★ [FOR07]
 H.~de Fraysseix, P.~Ossona~de Mendez, and P.~Rosenstiehl, Representation of Planar Hypergraphs by Contacts of Triangles, Proc. of Graph Drawing '07, to appear.

 [O]
 P.~Ossona~de Mendez, Realization of posets, Journal of Graph Algorithms and Applications 6 (2002), no.~1, 149--153.

 [S84]
 E.R. Scheinerman, Intersection classes and multiple intersection parameters of graphs, Ph.D. thesis, Princeton University, 1984.

 [S89]
 W.~Schnyder, Planar graphs and poset dimension, Order 5 (1989), 323--343.

 [W]
 T.R.S. Walsh, Hypermaps versus bipartite maps, J. Combinatorial Theory 18(B) (1975), 155--163.

========================================================================

=== A PREVIOUS, UNVERIFIED ATTEMPT ===
The problem above was already attacked by `gpt-6-astra`, which reported verdict `partial` at high confidence. That attempt is reproduced below.

Treat it as a lead, not as an authority: it is unverified, it may be wrong in ways neither model noticed, and its framing may be the reason it stalled. Check anything you reuse, and say so if you discard it. Your task is the original problem, not a critique of this attempt. If you can finish what it started, do that; if a different route is better, take it.

--- previous attempt ---
```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture holds when every vertex belongs to at most three hyperedges, and every linear dimension-3 incidence graph is 3-degenerate.",
  "would_publish": false,
  "caveats": "The unrestricted conjecture is not settled here; these are self-contained consequences, but their novelty has not been checked."
}
```

# Partial results

I obtain two results:

1. **Bounded-incidence case.** If every vertex belongs to at most three hyperedges, then the desired representation exists. In fact, nondegenerate triangles suffice, and a supplied 3-realizer gives an explicit construction with integer coordinates of polynomial bit-length. Linearity is not needed for this result.
2. **Structural restriction.** For a linear hypergraph of incidence dimension at most \(3\), its incidence graph is \(3\)-degenerate. More precisely, writing
   \[
   n=|V|,\qquad m=|\mathcal E|,\qquad I=\sum_{e\in\mathcal E}|e|,
   \]
   if \(n,m\ge 3\), then
   \[
   I\le \min\{n+3m-6,\;m+3n-6\}.
   \tag{1}
   \]

Neither result resolves the case of unrestricted vertex-incidence degrees.

## Conventions

I use the maximal-intersection convention specified in the question: an edge is a maximal subfamily with nonempty common intersection. Accordingly, the hypergraph is taken to be a finite **Sperner hypergraph**, with nonempty edges covering its vertex set. Singleton components are allowed. If singleton intersections are ignored instead, isolated vertices can be represented by objects placed separately.

For such a hypergraph, it suffices to construct sets \(T_v\), \(v\in V\), satisfying
\[
\bigcap_{v\in S}T_v\ne\varnothing
\quad\Longleftrightarrow\quad
S\subseteq e\text{ for some }e\in\mathcal E
\tag{2}
\]
for every nonempty \(S\subseteq V\).

---

# 1. An explicit realization when every vertex has degree at most three

### Theorem 1

Let \(H=(V,\mathcal E)\) be a finite Sperner hypergraph whose incidence poset has dimension at most \(3\).

* If every vertex belongs to at most three edges, then \(H\) is the intersection hypergraph of nondegenerate closed triangles in the plane.
* If every vertex belongs to at most two edges, then nondegenerate closed segments suffice.

Given a 3-realizer of the incidence poset, these representations can be constructed in polynomial time, with integer coordinates having \(O(|V|+|\mathcal E|)\) bits.

The proof below is self-contained; it does not rely on the convex-realization result quoted in the question.

## 1.1. A robust convex-hull construction

Put \(N=|V|+|\mathcal E|\). Let \(L_1,L_2,L_3\) realize the incidence poset, repeating an order if necessary, and let \(r_i(x)\in\{1,\ldots,N\}\) be the position of \(x\) in \(L_i\).

For every edge \(e\), define
\[
q_e=
\left(
4^{N-r_1(e)},\,
4^{N-r_2(e)},\,
4^{N-r_3(e)}
\right)\in\mathbb Z^3.
\]
Project along the direction \((1,1,1)\) by
\[
\pi(x_1,x_2,x_3)=(x_1-x_3,\;x_2-x_3),
\]
and put
\[
p_e=\pi(q_e),\qquad
K_v=\operatorname{conv}\{p_e:v\in e\}.
\]

The important fact is stronger than merely saying that the \(K_v\) have the right intersections.

### Lemma 2

For every nonempty \(S\subseteq V\),
\[
\bigcap_{v\in S}\bigl(K_v+[-1,1]^2\bigr)\ne\varnothing
\quad\Longleftrightarrow\quad
S\subseteq e\text{ for some }e\in\mathcal E.
\tag{3}
\]

Here \(+\) denotes Minkowski sum.

### Proof

If \(S\subseteq e\), then \(p_e\in K_v\) for every \(v\in S\), proving one direction.

Suppose conversely that no edge contains \(S\), but
\[
z\in\bigcap_{v\in S}\bigl(K_v+[-1,1]^2\bigr).
\]

For each \(v\in S\), choose
\[
x^v\in\operatorname{conv}\{q_e:v\in e\},
\qquad
\delta^v\in[-1,1]^2
\]
such that
\[
z=\pi(x^v)+\delta^v.
\]

Define
\[
a_i(v)=4^{N-r_i(v)-1}.
\]
Whenever \(v\in e\), the relation \(v<e\) holds in all three orders, so
\[
(q_e)_i\le a_i(v).
\]
Consequently,
\[
x_i^v\le a_i(v).
\tag{4}
\]

Set
\[
R_i=\max_{v\in S}r_i(v),
\qquad
a_i=\min_{v\in S}a_i(v)=4^{N-R_i-1}.
\]
Every vertex has an incident edge, so \(r_i(v)\le N-1\); hence
\[
a_i\ge 1.
\tag{5}
\]

Now let
\[
y^v=x^v+(\delta_1^v,\delta_2^v,0).
\]
All the \(y^v\) project to \(z\), so their pairwise differences are multiples of \((1,1,1)\). Choose \(v_0\in S\) for which \(y^{v_0}_3\) is minimum. Then
\[
y^{v_0}\le y^v
\]
coordinatewise for every \(v\in S\).

Using (4) and \(|\delta_i^v|\le1\), we obtain
\[
x_i^{v_0}\le a_i+2\quad(i=1,2),
\qquad
x_3^{v_0}\le a_3.
\]
Thus, by (5),
\[
\sum_{i=1}^3\frac{x_i^{v_0}}{a_i}
\le 3+\frac2{a_1}+\frac2{a_2}
\le 7.
\tag{6}
\]

On the other hand, take any edge \(e\). Since \(S\nsubseteq e\), choose \(v\in S\setminus e\). The elements \(v,e\) are incomparable in the incidence poset. Therefore, in at least one realizing order, say \(L_i\), we have \(e<v\). Hence
\[
r_i(e)\le r_i(v)-1\le R_i-1,
\]
and therefore
\[
(q_e)_i
\ge 4^{N-R_i+1}
=16a_i.
\]
It follows that
\[
\sum_{i=1}^3\frac{(q_e)_i}{a_i}\ge16
\]
for every edge \(e\), and hence for every convex combination of the \(q_e\).

But \(x^{v_0}\) is such a convex combination, contradicting (6). This proves the lemma. \(\square\)

In particular, **any** choices of sets satisfying
\[
K_v\subseteq T_v\subseteq K_v+[-1,1]^2
\tag{7}
\]
preserve exactly the intersection pattern required in (2).

## 1.2. Replacing the hulls by triangles or segments

Suppose every vertex has incidence degree at most three. Each \(K_v\) is the convex hull of at most three integer points.

* If \(K_v\) is already a nondegenerate triangle, take \(T_v=K_v\).
* If \(K_v=[a,b]\) is a nondegenerate segment, choose a coordinate unit vector \(u\) not parallel to \(b-a\), and take
  \[
  T_v=\operatorname{conv}\{a,b,a+u\}.
  \]
* If \(K_v=\{p\}\), take
  \[
  T_v=\operatorname{conv}\{p,\ p+(1,0),\ p+(0,1)\}.
  \]

In every case \(T_v\) is a nondegenerate triangle satisfying (7). Lemma 2 proves that the resulting intersection hypergraph is exactly \(H\).

If every vertex has degree at most two, each \(K_v\) is a segment or a point. Keep every nondegenerate segment, and replace a point \(p\) by
\[
[p,p+(1,0)].
\]
Again (7) holds, giving the segment assertion.

All coordinates used above are integers of magnitude at most \(4^N+1\). Thus their bit-length is \(O(N)\), and the construction is polynomial-time when the three orders are supplied. This completes the proof of Theorem 1. \(\square\)

### A slightly broader certificate

The same construction succeeds whenever every \(K_v\) has at most three extreme points, even if some vertices have higher incidence degree. This is a directly checkable sufficient condition for a particular realizer.

## 1.3. A genuinely nonplanar instance covered by the result

The example in the question has vertex degrees
\[
(3,3,3,3,2),
\]
so Theorem 1 applies even though its incidence graph is nonplanar.

For that particular hypergraph, segments already suffice. One explicit representation is:

\[
\begin{array}{c|c}
v&\text{segment endpoints}\\ \hline
1&(0,0),\ (6,6)\\
2&(2,-2),\ (6,6)\\
3&(0,0),\ (6,-6)\\
4&(2,2),\ (6,-6)\\
5&(0,0),\ (3,0)
\end{array}
\]

The triple intersections are precisely
\[
\{1,3,5\}\text{ at }(0,0),
\qquad
\{2,4,5\}\text{ at }(3,0).
\]
The remaining maximal intersections are
\[
\{1,2\},\ \{2,3\},\ \{3,4\},\ \{1,4\},
\]
at the four other listed endpoints.

---

# 2. Planar supports and sparsity of the incidence graph

The dimension assumption also supplies a useful structural restriction, independent of the bounded-degree construction.

A **planar support** for a family of subsets of a set \(B\) is a planar graph on \(B\) in which each specified nonempty subset induces a connected subgraph.

### Lemma 3

Let \(P\) be a height-two poset of dimension at most \(3\), with designated lower and upper antichains \(A,B\). There is a planar support on \(B\) for the sets
\[
N(a)=\{b\in B:a<b\},\qquad a\in A.
\]

### Proof

Use the construction above, with one point \(q_b\) for each \(b\in B\), and define
\[
Q=\operatorname{conv}\{q_b:b\in B\}+\mathbb R_{\ge0}^3.
\]

For any poset element \(x\), put
\[
u_x=
\left(
4^{r_1(x)-N},\,
4^{r_2(x)-N},\,
4^{r_3(x)-N}
\right).
\]

First, every \(q_b\) is a vertex of \(Q\). Indeed,
\[
u_b\cdot q_b=3.
\]
For \(c\ne b\), incomparability of \(b,c\) gives an index \(i\) with \(r_i(b)>r_i(c)\), so
\[
u_b\cdot q_c\ge4.
\]
Since \(u_b\) is strictly positive, \(q_b\) is the unique minimizer of \(u_b\cdot x\) on \(Q\).

There are no other vertices: an extreme point of a convex hull plus the nonnegative orthant must be one of the generating points. Explicitly, a nonzero orthant summand permits a small perturbation in both directions of a coordinate axis, while a nontrivial convex combination also prevents extremality.

Let \(G\) be the graph consisting of the vertices and bounded edges of \(Q\). Its projection by \(\pi\) is a straight-line planar drawing. To see this, note that \(\pi\) is injective on \(\partial Q\): if distinct boundary points satisfy
\[
y=x+t(1,1,1),\qquad t>0,
\]
then
\[
y\in x+\operatorname{int}\mathbb R_{\ge0}^3\subseteq\operatorname{int}Q,
\]
a contradiction. Thus projected edges cannot cross or overlap except at their common endpoints.

It remains to show that \(G[N(a)]\) is connected. For \(b\in N(a)\),
\[
u_a\cdot q_b\le\frac34,
\]
whereas for \(b\notin N(a)\),
\[
u_a\cdot q_b\ge4.
\]
Thus \(N(a)\) is exactly the set of vertices below the level \(u_a\cdot x=1\).

Perturb \(u_a\) slightly, keeping it strictly positive and preserving this separation, so that its values on the vertices are distinct. From every vertex other than the unique minimum, there is an incident edge along which this linear functional decreases. This follows because the feasible tangent cone at a vertex is generated by its incident edge directions; if none decreased, that vertex would be a global minimum.

Such a decreasing edge cannot be unbounded: every recession direction of \(Q\) is nonnegative, and the functional is strictly positive. Following decreasing bounded edges therefore leads to the minimum vertex. Starting below level \(1\), the entire path remains below level \(1\).

Hence all vertices of \(N(a)\) are connected within \(G[N(a)]\). \(\square\)

## 2.1. Incidence bounds

Now assume \(H\) is linear.

Apply Lemma 3 to its incidence poset. We obtain a planar graph \(G\) on \(\mathcal E\) such that
\[
\mathcal E_v=\{e:v\in e\}
\]
induces a connected subgraph for every \(v\).

Choose a spanning tree of \(G[\mathcal E_v]\) for each vertex \(v\). These trees are edge-disjoint. Indeed, a shared graph edge \(\{e,f\}\) would mean that two distinct vertices belong to both \(e\) and \(f\), contrary to linearity.

Consequently, when \(m\ge3\),
\[
I-n
=\sum_{v\in V}\bigl(|\mathcal E_v|-1\bigr)
\le |E(G)|
\le3m-6.
\tag{8}
\]

Apply the same argument to the dual poset. Linearity is preserved under exchanging the two incidence classes. For \(n\ge3\), this gives
\[
I-m
=\sum_{e\in\mathcal E}(|e|-1)
\le3n-6.
\tag{9}
\]

Equations (8) and (9) prove (1). In particular, if \(n,m\ge3\),
\[
I\le2(n+m)-6.
\tag{10}
\]

### Corollary 4

The incidence graph of every finite linear hypergraph of incidence dimension at most \(3\) is \(3\)-degenerate.

### Proof

Suppose an induced subgraph of the incidence graph had minimum degree at least \(4\). Its corresponding restricted height-two poset still has dimension at most \(3\), and its incidence graph remains \(C_4\)-free, equivalently linear.

Both incidence classes have at least four elements, and neither contains isolated elements. Applying (10) to this restricted instance gives average degree
\[
\frac{2I'}{n'+m'}
\le4-\frac{12}{n'+m'}
<4,
\]
contradicting minimum degree at least \(4\). \(\square\)

## 2.2. A local form and a three-incidence budget

Restricting the poset to a subset \(X\subseteq V\), and applying the planar-support argument on \(X\), gives
\[
\sum_{e\in\mathcal E}\max\{|e\cap X|-1,0\}
\le3|X|-6
\qquad(|X|\ge3).
\tag{11}
\]
Repeated singleton neighborhoods cause no problem: they contribute zero to the sum.

One consequence is a useful combinatorial allocation.

### Corollary 5

One can choose a root \(r(e)\in e\) for every hyperedge so that each vertex \(v\) is a nonroot member of at most three incident edges.

### Proof

Write \(d(v)=|\mathcal E_v|\), and give vertex \(v\)
\[
b(v)=\max\{d(v)-3,0\}
\]
copies. Match these copies to incident hyperedges, using each hyperedge at most once.

For \(X\subseteq V\), let \(\mathcal N(X)\) be the set of edges meeting \(X\). Then
\[
\sum_{v\in X}d(v)-|\mathcal N(X)|
=
\sum_{e\in\mathcal E}\max\{|e\cap X|-1,0\}
\le3|X|.
\tag{12}
\]
For \(|X|\ge3\), this follows from (11). For \(|X|=1\) the left side is zero, and for \(|X|=2\) it is at most one by linearity.

For a collection of copies, let \(X\) be its underlying vertices. These vertices all have \(d(v)>3\), so the number of copies in the collection is at most
\[
\sum_{v\in X}(d(v)-3)\le|\mathcal N(X)|.
\]
Thus Hall's condition holds.

Root each matched edge at the vertex to which it is matched, and root every unmatched edge arbitrarily. Each vertex is then the root of at least \(d(v)-3\) edges whenever \(d(v)>3\), proving the assertion. \(\square\)

This allocation gives a combinatorial “three-incidence budget,” but it does not by itself yield a triangle representation.

---

# 3. The unresolved geometric step

The explicit construction proves the bounded-incidence theorem because
\[
K_v=\operatorname{conv}\{p_e:v\in e\}
\]
has at most three generating points.

For a higher-degree vertex, this hull may have more than three extreme points. The argument supplies no triangle \(T_v\) satisfying
\[
K_v\subseteq T_v\subseteq K_v+[-1,1]^2.
\]
An arbitrary enclosing triangle may introduce forbidden intersections. Carathéodory's theorem does not solve this: it does not give one inscribed triangle containing all prescribed witness points.

Likewise, \(3\)-degeneracy of the incidence graph does not justify a geometric induction. A low-degree incidence-graph vertex may be an edge-node, and even when it is an original vertex, an already chosen representation of the smaller instance need not admit the required extension.

The rooting in Corollary 5 highlights, rather than removes, the gap: trying to use nonroot incidences as triangle corners still leaves the rooted incidences to be accommodated while preserving all nonintersections.

Thus the rigorous outcome here is:

* an explicit triangle realization for all incidence-dimension-\(3\) instances with maximum vertex-incidence degree at most three;
* planar-support, sparsity, degeneracy, and rooting constraints for the full linear class;

but **no proof or counterexample for the unrestricted conjecture**.
