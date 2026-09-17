Attack the following open graph-theory problem.

Catalog id: domination_in_plane_triangulations
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory » Topological Graph Theory
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/domination_in_plane_triangulations/
Original entry: http://www.openproblemgarden.org/op/domination_in_plane_triangulations
Problem attributed to: Matheson, Lesley R., Tarjan, Robert E. (posted 2009-05-04)

=== Problem statement (OpenProblemGarden) ===
Title: Domination in plane triangulations
Conjecture Every sufficiently large plane triangulation $ G $ has a dominating set of size $ \le \frac{1}{4} |V(G)| $ .

=== Discussion / context (OpenProblemGarden) ===
Motivated by some problems in multigrid computations, Matheson and Tarjan [MT] considered the problem of finding small dominating sets in plane triangulations. They proved that every such graph $ G $ has a dominating set of size $ \le \frac{1}{3} |V(G)| $ and posed the above question. The Octahedron is a triangulation with 6 vertices for which every dominating set has size $ \ge 2 $ , so no constant better than $ \frac{1}{3} $ can be achieved in general. However, it appears that one can do better for larger graphs. The most extreme examples here (also from [MT]) are constructed as follows: Start with $ n $ disjoint copies of $ K_4 $ embedded in the plane, and then add edges to complete this graph to a triangulation (with $ 4n $ vertices). Now each of the original copies of $ K_4 $ has an inner vertex which has degree 3 in the final graph, and in order to cover it, one must take at least one vertex from this $ K_4 $ . It follows that every dominating set has size $ \ge n $ . Since the Matheson-Tarjan proof is short and instructive, we sketch it here. In fact, we shall prove (as they did) the stronger statement that every near-triangulation (a graph embedded in the plane with all finite faces of size three) has a (possibly improper) 3-coloring so that each color class is a dominating set and so that the subgraph induced by those vertices incident with the infinite face is properly colored. This stronger fact we prove by induction. If the infinite face is not bounded by a cycle or the infinite face is bounded by a cycle which has a chord, then the graph may be written as the union of two near-triangulations $ G_1,G_2 $ where $ G_1 $ and $ G_2 $ either share one vertex or two adjacent vertices and one edge. In either case, the result follows by applying induction to $ G_1 $ and $ G_2 $ . Otherwise, choose a vertex $ v $ on the infinite face, delete $ v $ and apply induction. Since the neighbors of $ v $ are all on the infinite face, and do not form an independent set, there are at least two colors, say $ 1 $ and $ 2 $ , which appear on the neighbors of $ v $ . Now giving $ v $ the color $ 3 $ gives a solution.

=== References listed by OpenProblemGarden ===
- [MT] L. R. Matheson, R. E. Tarjan, Dominating sets in planar graphs. European J. Combin. 17 (1996), no. 6, 565--568. MathSciNet

=== Catalog page (statement + literature review) ===
Domination in plane triangulations — Graph-theory open problems

 
 Status
 partial
 high confidence
 

 The Matheson–Tarjan conjecture that every sufficiently large plane triangulation has a dominating set of size at most $n/4$ remains open. The general upper bound has been steadily improved from $n/3$ to $17n/53$ (Špaçapan 2020) and then to $2n/7 \approx 0.286n$ (Christiansen–Rotenberg–Rutschmann 2023), while the full $n/4$ bound has been confirmed for the special case of plane triangulations with maximum degree at most 6 (King–Pelsmajer 2010).

 Cited literature (4)

 
 
 
partial Dominating sets in plane triangulations
 (2010)
 

 
 Erika L. C. King, Michael J. Pelsmajer · Discrete Mathematics · arXiv:0806.2421 · doi:10.1016/j.disc.2010.03.022

Proves the Matheson–Tarjan $n/4$ conjecture for the special case of plane triangulations with maximum degree at most 6.
 

 
 
partial Dominating Plane Triangulations
 (2016)
 

 
 Michael D. Plummer, Dong Ye, Xiaoya Zha · Discrete Applied Mathematics · arXiv:1408.4530

Proves that Hamiltonian plane triangulations with minimum degree at least 4 satisfy $\gamma(G) \le \lfloor 5n/16 \rfloor$ for $n \ge 26$, improving upon the $n/3$ bound for this class.
 

 
 
partial The domination number of plane triangulations
 (2020)
 

 
 Simon Špaçapan · Journal of Combinatorial Theory, Series B · arXiv:1806.06932

Improves the general upper bound on the domination number of plane triangulations from $n/3$ to $17n/53 \approx 0.321n$ for all $n > 6$.
 

 
 
partial Triangulations Admit Dominating Sets of Size $2n/7$
 (2023)
 

 
 Aleksander B. G. Christiansen, Eva Rotenberg, Daniel Rutschmann · arXiv preprint · arXiv:2310.11254

Proves that every plane triangulation on $n > 10$ vertices has a dominating set of size at most $2n/7 \approx 0.286n$, the current best general upper bound, substantially improving upon $17n/53$.
 

 

 Reviewer notes. The King–Pelsmajer arXiv preprint (0806.2421) was submitted June 2008, before the OPG posting date; the Discrete Mathematics journal version appeared in 2010 and is cited here. Search results suggest the Christiansen–Rotenberg–Rutschmann paper may have been published at SODA 2024, but this could not be confirmed via WebFetch (access denied); listed as arXiv preprint. DOIs for Špaçapan (J. Comb. Theory B 143:42–64, 2020) and Plummer–Ye–Zha (Discrete Appl. Math. 211:175–182, 2016) were not retrieved due to paywall restrictions, but their journal venues were confirmed via DBLP.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 05) (web search enabled).
 

Conjecture. Every sufficiently large plane triangulation $ G $ has a dominating set of size $ \le \frac{1}{4} |V(G)| $ .

Keywords:
coloring · domination · multigrid · planar graph · triangulation

Discussion

Motivated by some problems in multigrid computations, Matheson and Tarjan [MT] considered the problem of finding small dominating sets in plane triangulations. They proved that every such graph $ G $ has a dominating set of size $ \le \frac{1}{3} |V(G)| $ and posed the above question. The Octahedron is a triangulation with 6 vertices for which every dominating set has size $ \ge 2 $ , so no constant better than $ \frac{1}{3} $ can be achieved in general. However, it appears that one can do better for larger graphs. The most extreme examples here (also from [MT]) are constructed as follows: Start with $ n $ disjoint copies of $ K_4 $ embedded in the plane, and then add edges to complete this graph to a triangulation (with $ 4n $ vertices). Now each of the original copies of $ K_4 $ has an inner vertex which has degree 3 in the final graph, and in order to cover it, one must take at least one vertex from this $ K_4 $ . It follows that every dominating set has size $ \ge n $ . Since the Matheson-Tarjan proof is short and instructive, we sketch it here. In fact, we shall prove (as they did) the stronger statement that every near-triangulation (a graph embedded in the plane with all finite faces of size three) has a (possibly improper) 3-coloring so that each color class is a dominating set and so that the subgraph induced by those vertices incident with the infinite face is properly colored. This stronger fact we prove by induction. If the infinite face is not bounded by a cycle or the infinite face is bounded by a cycle which has a chord, then the graph may be written as the union of two near-triangulations $ G_1,G_2 $ where $ G_1 $ and $ G_2 $ either share one vertex or two adjacent vertices and one edge. In either case, the result follows by applying induction to $ G_1 $ and $ G_2 $ . Otherwise, choose a vertex $ v $ on the infinite face, delete $ v $ and apply induction. Since the neighbors of $ v $ are all on the infinite face, and do not form an independent set, there are at least two colors, say $ 1 $ and $ 2 $ , which appear on the neighbors of $ v $ . Now giving $ v $ the color $ 3 $ gives a solution.

Bibliography

 [MT]
 L. R. Matheson, R. E. Tarjan, Dominating sets in planar graphs. European J. Combin. 17 (1996), no. 6, 565--568. MathSciNet
 MathSciNet

========================================================================

=== A PREVIOUS, UNVERIFIED ATTEMPT ===
The problem above was already attacked by `gpt-6-astra`, which reported verdict `partial` at high confidence. That attempt is reproduced below.

Treat it as a lead, not as an authority: it is unverified, it may be wrong in ways neither model noticed, and its framing may be the reason it stalled. Check anything you reuse, and say so if you discard it. Your task is the original problem, not a critique of this attempt. If you can finish what it started, do that; if a different route is better, take it.

--- previous attempt ---
```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I prove gamma(G) <= floor(n/4+b/8), where b counts vertices with bipartite open neighborhoods, establishing the conjectured bound when b=0.",
  "would_publish": false,
  "caveats": "The general conjecture is not settled; novelty of this structural bound has not been checked."
}
```

## 1. A structural partial result

Let \(G\) be a finite simple plane triangulation with \(n\ge 4\) vertices. Write
\[
B(G)=\{v\in V(G):G[N(v)]\text{ is bipartite}\},
\qquad b=|B(G)|,
\]
where \(N(v)\) is the **open** neighborhood of \(v\).

I prove the following parameterized bound. I am not claiming that it is new.

**Theorem.**
\[
\boxed{\displaystyle
\gamma(G)\le \left\lfloor\frac n4+\frac b8\right\rfloor.}
\tag{1}
\]
More generally, if vertices have nonnegative costs \(w(v)\), then \(G\) has a dominating set \(D\) satisfying
\[
\boxed{\displaystyle
w(D)\le \frac{w(V(G))}{4}+\frac{w(B(G))}{8}.}
\tag{2}
\]

In particular, the conjectured bound holds whenever every open neighborhood is non-bipartite. An easily checked sufficient condition is:

> Every vertex either has odd degree or belongs to a copy of \(K_4\).

Thus the result includes all odd-degree plane triangulations and all stacked triangulations, as well as mixtures of these local conditions.

The proof uses the Four Color Theorem and a counting argument based on Kempe switches.

## 2. A switching lemma for proper four-colorings

Let \(\Omega\) be the set of all proper colorings
\[
f:V(G)\longrightarrow \{1,2,3,4\}.
\]
The Four Color Theorem guarantees that \(\Omega\ne\varnothing\).

Call a vertex \(v\) **colorful** in \(f\) if its closed neighborhood \(N[v]\) contains all four colors, and **deficient** otherwise.

The neighbors of every vertex of a plane triangulation occur in a cyclic order in which consecutive neighbors are adjacent. Consequently, every closed neighborhood contains at least three colors. A deficient vertex therefore sees exactly two colors on its open neighborhood. In particular,
\[
\{v:v\text{ is deficient in }f\}\subseteq B(G).
\tag{3}
\]

The useful point is that deficiency cannot occur in more than half of all proper four-colorings, at any fixed vertex.

**Lemma.** For every \(v\in V(G)\),
\[
|\{f\in\Omega:v\text{ is deficient}\}|
\le
|\{f\in\Omega:v\text{ is colorful}\}|.
\tag{4}
\]

### Proof

There is nothing to prove if \(v\) is never deficient. Otherwise, its degree is even, say \(2k\), with \(k\ge2\). Fix the cyclic ordering
\[
x_1,y_1,x_2,y_2,\ldots,x_k,y_k
\]
of its neighbors, and put
\[
A=\{x_1,\ldots,x_k\},\qquad B=\{y_1,\ldots,y_k\}.
\]

In any coloring in which \(v\) is deficient, the neighbor cycle alternates between two colors. Write these colors as \(a\) on \(A\) and \(b\) on \(B\), write \(c=f(v)\), and let \(d\) be the missing fourth color.

We construct an injection from deficient colorings to colorful colorings. Let \(H=G-v\).

A Kempe switch means interchanging two colors on a connected component of the subgraph induced by those colors.

### Case I: the \(a,d\)-component through \(x_1\) does not contain all of \(A\)

Let \(X\) be that component in \(H\), and interchange \(a\) and \(d\) on \(X\).

This preserves properness: \(v\) has color \(c\), which is neither switched color. Some vertices of \(A\), including \(x_1\), now have color \(d\), while other vertices of \(A\) retain color \(a\). The vertices of \(B\) retain color \(b\).

Thus \(N(v)\) contains \(a,b,d\), and \(v\), still colored \(c\), is colorful.

### Case II: the \(a,d\)-component through \(x_1\) contains all of \(A\)

Let \(Y\) be the \(b,c\)-component of \(H\) containing \(y_1\). I first claim that \(Y\) does not contain all of \(B\).

There is a simple \(a,d\)-colored path \(P\) in \(H\) joining \(x_1\) to \(x_2\). Together with \(vx_1\) and \(vx_2\), it forms a simple cycle. The cyclic ordering at \(v\) places \(y_1\) and \(y_2\) on opposite sides of this cycle: the edges \(vy_1\) and \(vy_2\) leave \(v\) on opposite sides and cannot meet the cycle elsewhere.

A \(b,c\)-colored path in \(H\) cannot meet this cycle. Its vertices cannot belong to \(P\), whose colors are \(a,d\), and it cannot use \(v\), which has been deleted. Planarity therefore excludes a \(b,c\)-colored path from \(y_1\) to \(y_2\). Hence \(y_2\notin Y\), proving the claim.

Now recolor \(v\) from \(c\) to \(d\), which is legal because \(d\) is absent from \(N(v)\). Interchange \(b\) and \(c\) on \(Y\). This is a legal Kempe switch after the recoloring of \(v\).

The set \(A\) remains monochromatic in color \(a\), while \(B\) now contains both \(b\) and \(c\). Since \(v\) has color \(d\), it is colorful.

### Injectivity

The two types of output are distinguishable:

- Case I produces an output in which \(A\) uses two colors and \(B\) is monochromatic.
- Case II produces an output in which \(A\) is monochromatic and \(B\) uses two colors.

For a Case I output, the original coloring is recovered by switching the two colors occurring on \(A\), on their component in \(H\) containing \(x_1\). A Kempe switch does not change the vertex set or connectivity of the corresponding two-color induced subgraph, so this uniquely reverses the operation.

For a Case II output, first switch the two colors occurring on \(B\), on their component in \(H\) containing \(y_1\). After this reversal, \(N(v)\) is again two-colored. Recolor \(v\) to the unique color absent from its current closed neighborhood. This uniquely recovers the original coloring.

Thus the map is injective, proving (4). \(\square\)

## 3. From colorings to dominating sets

Choose \(f\) uniformly from \(\Omega\), and let \(X(f)\) be its set of deficient vertices. By the lemma and (3),
\[
\mathbb P(v\in X(f))\le
\begin{cases}
1/2,&v\in B(G),\\
0,&v\notin B(G).
\end{cases}
\]
Therefore, for any nonnegative vertex costs,
\[
\mathbb E\,w(X(f))
\le \frac12 w(B(G)).
\tag{5}
\]
There exists a proper four-coloring \(f\) for which
\[
w(X(f))\le \frac12 w(B(G)).
\tag{6}
\]

Fix such a coloring and let
\[
C_i=f^{-1}(i),\qquad i=1,2,3,4.
\]
Define
\[
X_i=\{v:N[v]\cap C_i=\varnothing\},
\qquad
D_i=C_i\cup X_i.
\]
Each \(D_i\) is a dominating set: vertices not dominated by \(C_i\) are included in \(X_i\).

Every deficient vertex misses exactly one color, while every colorful vertex misses none. Thus the sets \(X_i\) partition \(X(f)\). Also \(C_i\cap X_i=\varnothing\). Consequently,
\[
\sum_{i=1}^4 w(D_i)
=
w(V(G))+w(X(f))
\le
w(V(G))+\frac12w(B(G)).
\]
At least one of these four dominating sets has cost at most one quarter of the right-hand side. This proves (2).

Taking \(w(v)=1\) for every vertex and using integrality proves (1). \(\square\)

## 4. Consequences for the conjecture

### 4.1. An exact \(n/4\) special case

The neighbors of a vertex \(v\) contain a cycle of length \(\deg(v)\). Hence odd degree implies that \(G[N(v)]\) is non-bipartite.

If \(v\) belongs to a \(K_4\), its neighborhood contains the triangle formed by the other three vertices, so again \(G[N(v)]\) is non-bipartite.

Therefore:

**Corollary.** If every vertex of a plane triangulation either has odd degree or belongs to a \(K_4\), then
\[
\gamma(G)\le \left\lfloor\frac n4\right\rfloor.
\]

In this case there is an especially direct interpretation: **every** proper four-coloring partitions \(V(G)\) into four dominating sets.

### 4.2. A small-exception extension

Write \(n=4q+r\), where \(0\le r\le3\). Bound (1) gives the conjectured inequality whenever
\[
b+2r\le7.
\tag{7}
\]
In particular, it holds if at most one vertex has a bipartite open neighborhood.

Conversely, any counterexample to \(\gamma(G)\le n/4\) must satisfy
\[
b\ge 8-2r.
\tag{8}
\]
This is only a local obstruction requirement, not a resolution of the conjecture.

For comparison with the general estimate quoted in the question, the unrounded bound in (1) is smaller than \(2n/7\) whenever
\[
b<\frac{2n}{7}.
\]

### 4.3. The coefficient \(1/4\) is sharp within the special case

The disjoint-\(K_4\) construction in the question already lies in the class \(b=0\).

For completeness, take \(m\) vertex-disjoint plane copies \(Q_1,\ldots,Q_m\) of \(K_4\), each with a vertex \(z_i\) inside the triangle formed by its other three vertices. Place the copies in disjoint regions and add noncrossing edges until the graph is a triangulation, without adding vertices.

No added edge can join \(z_i\) to a vertex outside \(Q_i\), because the enclosing triangle separates them. Thus
\[
N[z_i]=V(Q_i).
\]
These \(m\) closed neighborhoods are disjoint, so every dominating set contains at least \(m\) vertices.

Conversely, choosing one arbitrary vertex from each \(Q_i\) dominates all \(4m\) vertices. Hence
\[
\gamma(G)=m=\frac{|V(G)|}{4}.
\]
Every vertex belongs to one of the original \(K_4\)'s, so \(b=0\).

## 5. What remains unresolved

The error term \(b/8\) can be linear in \(n\); planarity does not force \(b\) to be small.

For an explicit example, take an even cycle \(C_{2k}\), \(k\ge2\), and add two nonadjacent poles, each adjacent to every cycle vertex, embedded on opposite sides of the cycle. This is a plane triangulation. Each pole has an even cycle as its induced neighborhood, while each cycle vertex has a \(4\)-cycle as its induced neighborhood. Therefore
\[
b=n.
\]
On this family, (1) gives only \(\gamma(G)\le\lfloor3n/8\rfloor\), although the two poles themselves form a dominating set.

Thus the argument proves the desired bound for a definite structural class and supplies a quantitative extension, but it does not address the conjecture adequately when a large proportion of vertices have bipartite open neighborhoods. No removal of that linear error term is established here.
