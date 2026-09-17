```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I prove that deleting at most half of the degree-at-least-five vertices of the 4-core makes a planar graph partitionable into two induced forests, improving the previous core-sensitive bound.",
  "would_publish": false,
  "caveats": "This is not a uniform improvement on 2n/5 and does not resolve the conjecture; novelty of the partial result is not claimed."
}
```

## 1. The partial result

All graphs are finite, simple, and undirected. Write
\[
a(G)=\max\{|S|:G[S]\text{ is a forest}\}.
\]
A **forest coloring** is a red-blue vertex coloring in which both color classes induce forests.

Let \(K\) be the \(4\)-core of a planar graph \(G\), obtained by repeatedly deleting vertices of current degree at most three. For a component \(C\) of \(K\), define
\[
h(C)=|\{v\in V(C):d_C(v)\ge5\}|.
\]
Put
\[
b(t)=
\begin{cases}
0,&0\le t\le2,\\[2mm]
\lfloor t/2\rfloor,&t\ge3,
\end{cases}
\qquad
\rho(G)=\sum_{C\in\operatorname{comp}(K)}b(h(C)).
\]

**Theorem 1.** There is a set \(X\subseteq V(K)\), consisting only of vertices of degree at least five in \(K\), such that
\[
|X|\le \rho(G)
\]
and \(G-X\) has a forest coloring. Consequently,
\[
\boxed{\displaystyle
a(G)\ge \left\lceil\frac{n-\rho(G)}2\right\rceil .}
\]

In particular, if \(h\) is the total number of vertices of degree at least five in \(K\), then
\[
\boxed{\displaystyle
a(G)\ge
\left\lceil\frac{n-\lfloor h/2\rfloor}{2}\right\rceil .}
\]

This improves the previous attempt’s defect
\[
\sum_C\max\{h(C)-2,0\}:
\]
our componentwise defect is no larger, and is strictly smaller whenever \(h(C)\ge5\).

The proof also gives a further special case of the original conjecture: **no deletion is needed when an explicit planar auxiliary graph is bipartite.** This includes graphs with arbitrarily many high-degree vertices in one \(4\)-core component; see Section 6.

I checked and retain the previous attempt’s two-terminal extension results. Their proofs are included below rather than treating that attempt as an authority. The additional step is the auxiliary-graph construction in Section 4.

---

## 2. A coloring extension lemma

The following elementary observation will be used repeatedly.

**Lemma 2.** Suppose \(S\subseteq V(Q)\) has a forest coloring, \(Q-S\) is nonempty and connected, and every vertex outside \(S\) has degree at most four in \(Q\). The coloring extends if either:

1. some \(z\in V(Q-S)\) has \(d_Q(z)\le3\); or
2. some \(z\in V(Q-S)\) has two neighbors in \(S\) belonging to different components of the same color.

**Proof.** Take a spanning tree of \(Q-S\), rooted at \(z\). Color all vertices other than \(z\) in an order in which each vertex precedes its parent.

At its turn, a vertex has an uncolored parent and hence at most three colored neighbors. One color occurs on at most one of those neighbors. Giving the vertex that color creates no monochromatic cycle. Moreover, this operation never joins two previously existing components of that color.

In case 1, the root also has at most three colored neighbors, so the same rule finishes.

In case 2, suppose the specified neighbors of \(z\) are red. They remain in different red components throughout the preceding operations. If \(z\) has at most one blue neighbor, color it blue. Otherwise, the degree bound forces its red neighbors to be exactly the specified two. Coloring \(z\) red joins two distinct red trees and creates no cycle. ∎

---

## 3. The planar extension facts

We need the following two facts.

**Proposition 3 — prescribed opposite colors on an edge.**  
Let \(pq\in E(Q)\), where \(Q\) is planar. If every vertex outside \(\{p,q\}\) has degree at most four, then prescribing different colors on \(p,q\) extends to a forest coloring of \(Q\).

**Proposition 4 — two exceptional vertices.**  
Every planar graph with at most two vertices of degree at least five has a forest coloring.

For completeness, here are proofs.

### 3.1 A planar configuration

We use two elementary outerplanar facts:

* If adding a universal vertex to a graph \(B\) gives a planar graph, then \(B\) is outerplanar: deleting the universal vertex from a plane embedding leaves all vertices of \(B\) incident with one face.
* A 2-connected outerplanar graph has at least two vertices of degree two. Indeed, triangulate its outer polygon. A polygon triangulation with at least four vertices has at least two ears, as follows from the leaves of its weak dual tree. Ear vertices have degree two in the original graph as well. The triangle case is immediate.

**Lemma 5.** Let \(P\) be a 2-connected planar graph, with distinct vertices \(p,q\). Suppose
\[
H=P-\{p,q\}
\]
is connected and every vertex of \(H\) has degree four in \(P\). Suppose also that either \(pq\in E(P)\), or \(p,q\) have no common neighbor in \(H\).

Then there are \(a\in\{p,q\}\) and \(z,b\in V(H)\) such that
\[
az,zb\in E(P),\qquad ab\notin E(P),
\qquad H-b\text{ is connected}.
\]

**Proof.** Suppose no such configuration exists. Since each vertex of \(H\) has at most two neighbors outside \(H\),
\[
\delta(H)\ge2.
\]

If \(H\) is 2-connected, set \(U=V(H)\). Otherwise take an endblock \(B\) of \(H\), let \(c\) be its unique cutvertex, and set \(U=V(B)\setminus\{c\}\). Such an endblock is 2-connected: a bridge endblock would give a vertex of degree one in \(H\).

In either case, \(H[U]\) is connected, and every vertex of \(U\) is a non-cutvertex of \(H\). For each \(a\in\{p,q\}\), either all of \(U\) is adjacent to \(a\), or none is. Otherwise a path in \(H[U]\) contains an edge \(zb\) with \(az\in E(P)\), \(ab\notin E(P)\), and \(H-b\) connected, contrary to assumption.

At least one of \(p,q\) has a neighbor in \(U\). For an endblock, otherwise \(c\) would disconnect \(P\). If \(U=V(H)\), each of \(p,q\) has a neighbor in \(H\), by 2-connectivity of \(P\), so both are adjacent to all of \(H\).

Consider an endblock for which exactly one terminal, say \(a\), is adjacent to \(U\). Then
\[
d_B(u)=3\qquad(u\in U).
\]
The only neighbors of \(U\) outside \(U\) are \(a\) and \(c\). There is an \(a\)-\(c\) path in \(P-U\). To see this, \(H-U\) is connected and contains a vertex besides \(c\); if no such path existed, deleting \(c\) would separate \(U\cup\{a\}\), together with any vertices connected to \(a\) outside \(U\), from those vertices of \(H-U\).

Contract this path to an edge, retaining its endpoints, and delete everything else outside \(B\cup\{a\}\). This gives a planar cone over \(B\). Thus \(B\) is outerplanar. But all its vertices except possibly \(c\) have degree three, contradicting the existence of two degree-two vertices.

Therefore both \(p,q\) are adjacent to every vertex of each chosen \(U\). In particular they have a common neighbor, so the hypothesis forces \(pq\in E(P)\).

If \(H\) is 2-connected, every vertex has degree two in \(H\), so \(H\) is a cycle. Choose adjacent \(u_1,u_2\) on it. The graph
\[
R=H-\{u_1,u_2\}
\]
is nonempty and connected; both \(u_i\) have a neighbor in \(R\), and both \(p,q\) have neighbors in \(R\). Contracting \(R\) gives a \(K_5\) minor on \(p,q,u_1,u_2\) and the contracted vertex.

If \(H\) has a cutvertex, then in each endblock \(B\), every vertex except its cutvertex has degree two in \(B\). Since \(B\) is 2-connected, this forces \(B\) to be a cycle. Choose adjacent \(u_1,u_2\in V(B)\setminus\{c\}\). Again \(R=H-\{u_1,u_2\}\) is connected, and both \(u_i\) have a neighbor in \(R\). A different endblock supplies a vertex of \(R\) adjacent to both \(p,q\). Contracting \(R\) again gives a \(K_5\) minor.

Both conclusions contradict planarity. ∎

### 3.2 Proof of Proposition 3

Suppose there is a counterexample \(Q\) with the fewest vertices.

A nonterminal vertex of degree at most three can be deleted and then reinserted in a color occurring on at most one neighbor. Thus every nonterminal vertex has degree four.

The counterexample is connected. A component not containing \(pq\) can be colored by minimality using any of its edges as a distinguished edge; isolated vertices are trivial.

There is no cutvertex. At a cutvertex \(c\), first color the piece containing \(pq\). For every other piece, choose an edge \(cu\), prescribe the already determined color on \(c\) and the opposite color on \(u\), and apply minimality. All vertices of that piece other than possibly \(c\) have degree at most four. The resulting monochromatic forests glue at only \(c\).

The graph with just the edge \(pq\) is not a counterexample, so \(Q\) is 2-connected.

Put \(H=Q-\{p,q\}\). If \(H\) is disconnected, color each graph induced by \(p,q\) and one component of \(H\), prescribing the same opposite colors on \(p,q\). Each red union glues only at one terminal, and each blue union only at the other. Thus \(H\) is connected.

Apply Lemma 5. It gives \(a,z,b\) as stated there. Precolor \(b\) with the color of \(a\), in addition to the prescribed colors of \(p,q\). The same-colored vertices \(a,b\) are nonadjacent and belong to different monochromatic components. Since
\[
Q-\{p,q,b\}=H-b
\]
is connected, Lemma 2, rooted at \(z\), completes the coloring. This is a contradiction. ∎

### 3.3 Proof of Proposition 4

Take a smallest counterexample \(G\). Deleting and reinserting a vertex of degree at most three shows that \(\delta(G)\ge4\). Colorings of components and of pieces at a cutvertex can be combined, swapping the two colors when necessary. Hence \(G\) is 2-connected.

If there is at most one high-degree vertex, use Proposition 3 with an edge containing it, or any edge if none exists. The same proposition applies if the two high-degree vertices are adjacent.

We may therefore suppose that there are exactly two high-degree vertices \(p,q\), that they are nonadjacent, and that every other vertex has degree four. Let \(H=G-\{p,q\}\).

* If \(H\) is disconnected, every component has a neighbor of each terminal, by 2-connectivity. For a component \(C\), the graph
  \[
  G[V(C)\cup\{p,q\}]+pq
  \]
  is planar: a different component supplies a \(p\)-\(q\) path whose internal vertices can be contracted to create the added edge. Apply Proposition 3 to each such graph with \(p\) red and \(q\) blue, then combine the colorings.

* If \(H\) is connected and \(p,q\) have a common neighbor, precolor both terminals red. They are nonadjacent, so Lemma 2, rooted at a common neighbor, applies.

* If \(H\) is connected and they have no common neighbor, apply Lemma 5. Precolor \(p,q\) differently and give its vertex \(b\) the color of the corresponding terminal \(a\). Lemma 2 applies again.

Every case contradicts the choice of \(G\). ∎

---

## 4. The new auxiliary-graph deletion argument

The principal addition is the following statement.

**Theorem 6.** Let \(Q\) be planar, and put
\[
H=\{v\in V(Q):d_Q(v)\ge5\},\qquad h=|H|.
\]
There exists \(X\subseteq H\) with
\[
|X|\le b(h)
\]
such that \(Q-X\) has a forest coloring.

**Proof.** We construct a planar auxiliary graph \(J\) on vertex set \(H\).

### Step 1: The auxiliary graph inside a block

Let \(B\) be a block of \(Q\), and put \(H_B=H\cap V(B)\). Blocks with \(|H_B|\le2\) require no auxiliary edges.

Suppose \(|H_B|\ge3\). Then \(B\) is 2-connected. For every component \(C\) of \(B-H_B\), let
\[
T_C=N_B(C)\cap H_B.
\]
We have \(|T_C|\ge2\): zero neighbors would disconnect \(B\), and a unique neighbor would be a cutvertex.

Construct \(J_B\) on \(H_B\) as follows:

* retain all edges of \(B[H_B]\);
* if \(T_C=\{p,q\}\), add the edge \(pq\);
* if \(|T_C|\ge3\), choose three distinct members of \(T_C\) and add a triangle on them.

The graph \(J_B\) is planar. Indeed, contract each connected \(C\) to one vertex, retaining only its two or three selected edges to \(H_B\). A degree-two vertex can be suppressed to an edge. A degree-three vertex can be replaced by a triangle among its neighbors, locally in the embedding. Delete loops and repeated edges.

Take the union of all the \(J_B\), including any unused vertices of \(H\) as isolated vertices. The result \(J\) is planar: its constituent graphs are glued along the block–cutvertex forest, and each gluing identifies at most one vertex.

### Step 2: Select the deletion set

Apply the Four Color Theorem to \(J\). Let \(X\) be the union of its two smallest color classes. Then
\[
|X|\le\lfloor h/2\rfloor.
\]
If \(h\le2\), at least two of the four classes are empty, so \(X=\varnothing\). Thus \(|X|\le b(h)\).

We now prove that every block of \(Q-X\), or more precisely every graph \(B-X\) for an original block \(B\), has a forest coloring.

### Step 3: Color a block

If \(|H_B|\le2\), Proposition 4 applies directly to \(B-X\), because every vertex outside those at most two vertices has degree at most four.

Suppose \(|H_B|\ge3\). The vertices \(H_B-X\) use only the two retained auxiliary colors. Interpret these as red and blue. Since \(J_B\) contains \(B[H_B]\), this initially gives independent red and blue sets.

Process the components \(C\) of \(B-H_B\).

**Case A: \(T_C\cap X\ne\varnothing\).**  
Choose \(z\in C\) adjacent to a deleted vertex. Since \(z\notin H\),
\[
d_{B-X}(z)\le3,
\]
and all vertices of \(C\) have degree at most four. Lemma 2, case 1, extends the current coloring over \(C\).

**Case B: \(T_C\cap X=\varnothing\).**  
Then \(|T_C|=2\). Otherwise the chosen triangle would use three distinct auxiliary colors, and could not avoid the two deleted color classes.

Write \(T_C=\{p,q\}\). The auxiliary edge \(pq\) ensures that \(p,q\) have opposite retained colors. We claim that
\[
P_C=B[V(C)\cup\{p,q\}]+pq
\]
is planar.

It suffices to find a \(p\)-\(q\) path in \(B-C\). If no such path existed, connectivity of \(B\) and the fact that \(C\) has only the two external neighbors \(p,q\) would imply that \(B-C\) has precisely two components, one containing each terminal. By 2-connectivity, the component containing \(p\) could contain no vertex other than \(p\), and similarly for \(q\); otherwise deleting the corresponding terminal would disconnect \(B\). This would give
\[
V(B)\setminus V(C)=\{p,q\},
\]
contrary to \(|H_B|\ge3\).

Thus the required outside path exists. Contracting it to an edge proves planarity of \(P_C\). Every vertex of \(C\) has degree at most four in \(P_C\), so Proposition 3 extends the prescribed opposite colors of \(p,q\) over \(C\).

This extension preserves the forest property in the entire already colored part: the new red subgraph meets the old red subgraph at only one terminal, and similarly for blue.

This finishes a forest coloring of \(B-X\).

### Step 4: Glue the blocks

After \(X\) is fixed, the red-blue colorings of different blocks need not maintain a common interpretation of the four auxiliary colors. Traverse the block–cutvertex forest and swap red and blue in a new block whenever needed to match the color at its attachment vertex. If that vertex was deleted, there is no matching requirement.

Every cycle lies in an original block. Therefore the combined coloring of \(Q-X\) has no monochromatic cycle. ∎

### Additional information supplied by the construction

The same proof gives:

* If \(J\) has a proper 3-coloring, deleting its smallest color class suffices, so one can take
  \[
  |X|\le\lfloor h/3\rfloor.
  \]
* If \(J\) is bipartite, no deletion is needed.

These are conditions on an explicitly constructed graph, not appeals to any unproved coloring conjecture.

---

## 5. Returning to the \(4\)-core

We now prove Theorem 1.

Apply Theorem 6 separately to every component \(C\) of \(K\). This gives a set \(X\subseteq V(K)\) satisfying
\[
|X|\le\sum_C b(h(C))=\rho(G),
\]
and a forest coloring of \(K-X\).

Reinsert the vertices removed in forming the \(4\)-core, in reverse deletion order. Each has at most three already present neighbors. Assign it a color occurring on at most one of those neighbors. This preserves both induced forests and colors all of \(G-X\).

The larger color class has at least
\[
\left\lceil\frac{n-|X|}{2}\right\rceil
\ge
\left\lceil\frac{n-\rho(G)}2\right\rceil
\]
vertices.

Finally,
\[
\rho(G)
\le \sum_C\lfloor h(C)/2\rfloor
\le \lfloor h/2\rfloor,
\]
giving the simpler bound in terms of the total number \(h\) of high-degree core vertices. ∎

### A further refinement when the degree-four part is connected

Suppose a component \(C\) of \(K\) has a nonempty high-degree set \(H\), and \(L=C-H\) is nonempty and connected. Then one can alternatively delete at most
\[
\left\lceil\frac{|H|}{3}\right\rceil
\]
vertices of \(H\) to obtain a forest coloring.

Choose \(x\in H\) adjacent to \(L\). Every planar graph is 5-degenerate, by Euler’s formula, and hence can be colored with three induced forests: in reverse degeneracy order, one of three colors occurs on at most one of the at most five colored neighbors.

Apply this to \(C[H-\{x\}]\). Delete \(x\) and a smallest color class, using at most
\[
1+\left\lfloor\frac{|H|-1}{3}\right\rfloor
=\left\lceil\frac{|H|}{3}\right\rceil
\]
vertices. The other two classes precolor the surviving high-degree vertices. A vertex of \(L\) adjacent to \(x\) now has degree at most three, so Lemma 2 extends this coloring over connected \(L\).

Thus, for such a component, \(b(h(C))\) may be replaced by
\[
\min\!\left\{b(h(C)),\,\left\lceil h(C)/3\right\rceil\right\}.
\]

---

## 6. A larger zero-deletion special case

Here is an intrinsic version of the bipartite-auxiliary-graph case.

**Corollary 7.** Let \(Q\) be a 2-connected planar graph, and let
\[
H=\{v:d_Q(v)\ge5\}.
\]
Suppose \(|H|\ge3\), every component of \(Q-H\) has exactly two neighbors in \(H\), and the graph
\[
T=Q[H]+\{\text{an edge joining those two neighbors for each component}\}
\]
is bipartite. Then \(Q\) has a forest coloring, and hence \(a(Q)\ge |V(Q)|/2\).

**Proof.** Here the auxiliary graph from Theorem 6 is precisely \(T\). Properly 2-coloring \(T\) allows both other auxiliary color classes to be empty, so \(X=\varnothing\). ∎

This accommodates arbitrarily many high-degree vertices in one \(4\)-core component. For example:

1. Start with an even cycle of length \(r\ge4\).
2. Along each cycle edge, attach a copy of the octahedral graph by identifying one of its edges with that cycle edge; all other vertices are new.

The graph is planar and 2-connected. Every original cycle vertex has degree eight, every new vertex has degree four, and the whole graph is its \(4\)-core. Deleting the original cycle vertices leaves one connected four-vertex piece for each cycle edge. The graph \(T\) is the original even cycle, so Corollary 7 applies.

In particular, this zero-deletion criterion is not restricted to cores with at most two high-degree vertices.

---

## 7. What is proved, and the remaining gap

Combining Theorem 1 with the acyclic-5-coloring bound stated in the question gives
\[
a(G)\ge
\max\left\{
\left\lceil\frac{2n}{5}\right\rceil,\,
\left\lceil\frac{n-\rho(G)}2\right\rceil
\right\}.
\]
The simpler unrounded estimate
\[
a(G)\ge \frac n2-\frac h4
\]
improves on \(2n/5\) when \(h<2n/5\).

The half-bound is sharp within the zero-defect class: disjoint copies of \(K_4\) have empty \(4\)-core and maximum induced forests containing exactly half their vertices.

The unresolved obstruction is substantial. A planar graph of minimum degree at least five has \(K=G\) and \(h=n\); the new main estimate then gives only approximately \(n/4\), weaker than \(2n/5\). The proof does not compensate for the vertices deleted from a dense high-degree core.

Thus the partial theorems above have complete proofs, but **no proof or counterexample for the unrestricted Albertson–Berman conjecture is obtained**.