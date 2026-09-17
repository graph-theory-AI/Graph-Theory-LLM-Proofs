```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "Self-contained arguments prove the conjecture for planar graphs of maximum average degree at most 46/11, and for planar graphs with at most eleven undirected triangles.",
  "would_publish": false,
  "caveats": "The full conjecture remains unresolved by this argument; no novelty claim or computational verification is made."
}
```

# Partial results

All graphs below are finite. An **acyclic 2-colouring** of a digraph is a vertex colouring with two colours such that neither colour class contains a directed cycle.

I prove the following.

**Theorem.** Every orientation of a simple planar graph \(F\) has an acyclic 2-colouring if any one of these conditions holds:

1. \(\operatorname{mad}(F)\le 46/11\), where
   \[
   \operatorname{mad}(F)=
   \max_{\substack{J\subseteq F\\V(J)\ne\varnothing}}
   \frac{2|E(J)|}{|V(J)|};
   \]
2. \(F\) contains at most eleven undirected triangles;
3. at most two vertices of \(F\) have degree at least five.

The principal quantitative result is this necessary condition for a minimal counterexample:

> If \(D\) is a vertex-critical planar oriented graph without an acyclic 2-colouring, with \(n\) vertices and \(m\) arcs, then
> \[
> \boxed{11m\ge 23n+5.}
> \]
> Moreover, in every plane embedding its underlying graph has at least twelve triangular faces. If their number is \(t\), then
> \[
> \boxed{2n\le 11t-98.}
> \]

The supplied attempt's hole-rotation argument and cactus conclusion check out; I reprove them below. The new ingredient is a planar counting lemma for that cactus. It improves the supplied sparsity constant **for planar graphs** from \(25/6\) to \(46/11\), and the triangle-count special case from nine to eleven. No assertion of novelty relative to the literature is intended.

## 1. Low-degree vertices in a critical obstruction

Call an oriented graph \(D\) **critical** if it has no acyclic 2-colouring but every proper induced subdigraph does.

Every critical \(D\) satisfies
\[
d^+(v)\ge2,\qquad d^-(v)\ge2.
\tag{1}
\]
Indeed, if \(d^+(v)\le1\), colour \(D-v\) and give \(v\) a colour absent from its out-neighbours. No new monochromatic directed cycle can contain \(v\). The argument for in-degree is identical.

Let
\[
L=\{v:d^+(v)=d^-(v)=2\},\qquad H=V(D)\setminus L.
\]
Thus \(L\) consists precisely of the vertices of underlying degree four, and every vertex of \(H\) has degree at least five.

### Hole-moving and rotation

Suppose \(v\in L\), and colour \(D-v\). Its two out-neighbours have different colours: otherwise the missing colour could be assigned to \(v\). Its two in-neighbours likewise have different colours.

If \(u\in L\) is adjacent to the uncoloured vertex \(v\), uncolour \(u\) and give \(v\) the former colour of \(u\). This preserves acyclicity. For example, if \(v\to u\), then \(u\) was the unique out-neighbour of \(v\) of that colour; after uncolouring \(u\), no monochromatic directed cycle can contain \(v\). The other direction uses in-neighbours.

Consequently, the uncoloured vertex—the **hole**—can be moved along any walk in the underlying graph \(D[L]\).

Consider an undirected cycle
\[
C=v_0v_1\cdots v_{k-1}v_0
\]
in \(D[L]\), with hole \(v_0\). Moving the hole around \(C\) and back to \(v_0\) changes the colour word on \(v_1,\dots,v_{k-1}\) from
\[
(a_1,\dots,a_{k-1})
\quad\text{to}\quad
(a_2,\dots,a_{k-1},a_1).
\tag{2}
\]
Vertices outside \(C\) are unchanged. Two consequences follow.

* If \(v_0\) has exactly one out-neighbour in \(V(C)\), then \(C-v_0\) is monochromatic. Its other out-neighbour is outside \(C\), with a fixed colour, and repeated rotations bring every entry of the word to the internal out-neighbour's position.
* If both cycle edges at \(v_0\) point away from \(v_0\), then \(k\) is odd and both colours occur on \(C-v_0\). Indeed, the first and last entries in the word must differ after every rotation, so the circular word of length \(k-1\) alternates.

### The cactus lemma

**Lemma 1.** Every undirected cycle in \(D[L]\) is consistently directed. In particular, the underlying graph of \(D[L]\) is a cactus: its blocks are isolated vertices, edges, or cycles.

**Proof.** Choose a shortest cycle \(C\) in \(D[L]\) that is not consistently directed.

If \(C\) has a chord \(a\to b\), the two shorter cycles formed by the chord are consistently directed. Their paths avoiding the chord both run from \(b\) to \(a\).

Colour \(D-b\). In each shorter cycle, \(b\) has exactly one out-neighbour on that cycle, so the first rotation consequence makes the remaining vertices monochromatic. The two remaining vertex sets intersect at \(a\), so their colours agree. But they contain the two out-neighbours of \(b\), which must have different colours—a contradiction.

Thus \(C\) is chordless. Since its orientation is not consistent, it has a vertex \(v\) whose two cycle edges point outwards. With hole \(v\), the second rotation consequence shows that \(|C|\) is odd and both colours occur on \(C-v\).

An odd cycle cannot have sources and sinks alternating at every vertex. Hence some \(w\in V(C)\) has one incoming and one outgoing cycle edge. Move the hole along \(C\) from \(v\) to \(w\). The multiset of colours on the coloured vertices of \(C\) is preserved. But \(C\) is chordless, so \(w\) has exactly one out-neighbour in \(V(C)\); the first rotation consequence says that \(C-w\) is monochromatic. This is again a contradiction.

Finally, \(D[L]\) cannot contain a theta—three internally vertex-disjoint paths with the same endpoints. At one endpoint, two of the three incident edges have the same direction; the cycle formed by those two paths would not be consistently directed.

A graph without a theta has only edges and cycles as its nontrivial blocks. For completeness, a 2-connected block other than a cycle contains a cycle with either a chord or a path through vertices outside the cycle joining two distinct cycle vertices; either gives a theta. \(\square\)

## 2. A planar obstruction needs at least three high-degree vertices

**Lemma 2.** If \(D\) is critical and planar, then \(|H|\ge3\).

**Proof.** Write \(h=|H|\), and let \(K\) be the underlying graph of \(D[L]\).

If \(h\le1\), every vertex of \(K\) has degree at least \(4-h\ge3\). This is impossible for a nonempty cactus, which has a vertex of degree at most two. The case \(L=\varnothing\) is also impossible, since then \(D\) has at most one vertex.

Suppose \(h=2\), with \(H=\{a,b\}\). Every vertex of \(K\) has degree at least two. Furthermore, every vertex of degree two in \(K\) is adjacent to both \(a\) and \(b\).

First suppose a component \(Q\) of \(K\) is not a single cycle. A cactus of minimum degree at least two that is not a cycle has at least two leaf cycle-blocks.

Choose adjacent non-cutvertices \(x_1,x_2\) in one leaf cycle-block, and a non-cutvertex \(x_3\) in another. Then
\[
Q-\{x_1,x_2,x_3\}
\]
is nonempty and connected, and each \(x_i\) has a neighbour in it. Contract this connected graph to a vertex \(z\). Since every \(x_i\) has degree two in \(K\), it is adjacent to both \(a\) and \(b\). We obtain a \(K_{3,3}\) minor with parts
\[
\{a,b,z\},\qquad \{x_1,x_2,x_3\},
\]
contrary to planarity.

Thus every component of \(K\) is a cycle, and \(a,b\) are adjacent to every vertex of \(K\).

If \(ab\) is an edge, contracting one such cycle to a triangle gives a \(K_5\) minor. If \(K\) has two components, a vertex in the second component supplies an \(a\)-\(b\) path disjoint from the first cycle; contracting that path again gives a \(K_5\) minor.

Therefore \(K\) is one cycle \(C\), and \(a,b\) are nonadjacent. For any \(v\in V(C)\), the partition
\[
\{a,b,v\},\qquad V(C)\setminus\{v\}
\]
induces two undirected forests: a three-vertex path and a path. It is therefore an acyclic 2-colouring in every orientation, contradicting criticality. \(\square\)

This already proves Theorem 3: vertices of degree at least five in an induced subgraph must also have degree at least five in the original graph.

## 3. A planar counting lemma for the low-degree cactus

Here is the additional planar ingredient.

**Lemma 3.** Let \(G\) be a simple planar graph with a vertex partition \(L,H\), where:

* every vertex of \(L\) has degree four in \(G\);
* \(G[L]\) is a cactus;
* \(h=|H|\ge3\).

Let \(c\) be the number of components of \(G[L]\), and \(q\) its number of cycle-blocks. Then
\[
\boxed{q\le2h+c-5.}
\tag{3}
\]

**Proof.** The result is immediate if \(L=\varnothing\), so assume otherwise. All degrees and blocks in the following construction refer to \(G[L]\).

Let:

* \(p\) be its number of degree-one vertices;
* \(c_0\) be its number of isolated-vertex components;
* \(c_2\) be its number of components isomorphic to \(K_2\);
* \(c_\circ\) be its number of components consisting of a single cycle;
* \(\tau\) be the total number of incidences between cycle-blocks and cutvertices.

We first record
\[
\tau\le2q-2c+2c_0+p.
\tag{4}
\]
To verify this, let \(b\) be the number of bridge-blocks and \(x\) the number of cutvertices. Counting edges in the block-cut forest gives
\[
\tau+2b-p=q+b+x-c+c_0.
\]
Every cutvertex-node has degree at least two in that forest, so
\[
x\le q+b-c+c_0.
\]
Together these imply (4).

### Selecting vertices to expose a bipartite planar graph

In each cycle-block \(C\), let \(k(C)\) be its number of cutvertices. Select vertices as follows:

* if \(k(C)=0\) or \(1\), select two adjacent non-cutvertices;
* if \(k(C)=2\), select one non-cutvertex;
* if \(k(C)\ge3\), select none.

These choices exist because the graph is simple, so every cycle has length at least three. Deleting the selected vertices leaves a nonempty connected remainder in each cycle-block, containing all its cutvertices. Every selected vertex has a neighbour in that remainder.

Let \(s\) be the number selected. The selection gives
\[
s\ge3q-\tau-c_\circ
 \ge q+2c-2c_0-p-c_\circ.
\tag{5}
\]

Also select:

* every degree-one vertex, except that in each \(K_2\) component select only one endpoint;
* every isolated vertex.

Delete all selected vertices temporarily. The remaining graph \(R\) has exactly \(c-c_0\) components, each nonempty and connected. The exceptional \(K_2\) case was arranged precisely to ensure this.

Contract each component of \(R\) to one vertex. Retain the vertices of \(H\) and the selected vertices, and retain only these edges:

* each selected cycle vertex has its two edges to \(H\), and one edge to its contracted \(R\)-component;
* each selected degree-one vertex has its three edges to \(H\), and its edge to its contracted \(R\)-component;
* each selected isolated vertex has its four edges to \(H\).

Delete all other edges and any duplicate edges arising from contraction. The resulting graph \(B\) is simple, planar and bipartite, with the selected vertices on one side.

Its numbers of vertices and edges are
\[
|V(B)|=h+c+s+p-c_2,
\]
\[
|E(B)|=3s+4(p-c_2)+4c_0.
\]
Since \(h\ge3\), the usual bipartite planar bound applies:
\[
|E(B)|\le2|V(B)|-4.
\]
Thus
\[
s+2p-2c_2+4c_0\le2h+2c-4.
\]
Substituting (5) yields
\[
q+p+2c_0-c_\circ-2c_2\le2h-4.
\]
Because \(p\ge2c_2\), we obtain
\[
q\le2h+c_\circ-2c_0-4
 \le2h+c_\circ-4.
\tag{6}
\]

If not every component is a single cycle, then \(c_\circ\le c-1\), and (3) follows. If every component is a single cycle, then \(q=c\); since \(h\ge3\),
\[
q=c\le2h+c-6<2h+c-5.
\]
This covers every case. \(\square\)

## 4. The improved critical density bound

Let \(D\) be a critical planar oriented graph. Write
\[
\ell=|L|,\qquad h=|H|,\qquad n=\ell+h,
\]
and let \(e_H\) be the number of edges in its underlying graph induced by \(H\).

By Lemmas 1 and 2, Lemma 3 applies. Since a cactus with \(\ell\) vertices, \(c\) components and \(q\) cycle-blocks has
\[
e(L)=\ell-c+q,
\]
the degree-four condition gives
\[
e(L,H)=4\ell-2e(L)=2\ell+2c-2q.
\]
Consequently,
\[
m=e(L)+e(L,H)+e_H
  =3\ell+c-q+e_H.
\]
Using (3),
\[
m\ge3\ell-2h+5+e_H
  =5\ell-2n+5+e_H.
\tag{7}
\]

On the other hand, vertices in \(H\) have degree at least five, so
\[
2m\ge4\ell+5h=5n-\ell,
\]
or
\[
\ell\ge5n-2m.
\]
Substitution into (7) gives
\[
m\ge5(5n-2m)-2n+5+e_H.
\]
Therefore
\[
\boxed{11m\ge23n+5+e_H\ge23n+5.}
\tag{8}
\]

### Maximum-average-degree consequence

If an orientation of a simple planar graph \(F\) were not acyclically 2-colourable, it would contain a critical induced subdigraph \(D\). By (8), its underlying graph would have average degree
\[
\frac{2m}{n}
\ge \frac{46}{11}+\frac{10}{11n}
>\frac{46}{11}.
\]
This proves Theorem 1.

## 5. Triangular faces and the eleven-triangle result

The underlying graph of a critical \(D\) is 2-connected. Disconnected components can be coloured separately. If there is a cutvertex, colour each piece consisting of that vertex and a component of its deletion, exchanging colour names to agree at the cutvertex. Every directed cycle lies in one piece, so the colourings combine—a contradiction.

Fix a plane embedding, and let \(t\) be its number of triangular faces. Every other face has length at least four. Euler's formula gives
\[
2m\ge3t+4(f-t),\qquad f=2-n+m,
\]
and hence
\[
m\le2n-4+\frac t2.
\tag{9}
\]

By Lemma 2, at least three vertices have degree at least five, while all others have degree at least four. Thus
\[
2m\ge4n+3.
\]
The left side is even, so
\[
m\ge2n+2.
\tag{10}
\]
Combining (9) and (10) gives
\[
\boxed{t\ge12.}
\tag{11}
\]

Distinct triangular faces correspond to distinct undirected triangles here. A triangle could bound faces on both sides only if the whole connected graph were that triangle, which is excluded by minimum degree four.

Therefore, if the original planar graph contains at most eleven undirected triangles, its critical induced subgraph would have \(t\le11\), contradicting (11). This proves Theorem 2.

Finally, combining (8) and (9) gives
\[
23n+5\le11m
 \le22n-44+\frac{11t}{2},
\]
so
\[
\boxed{2n\le11t-98.}
\tag{12}
\]

In particular, every critical planar obstruction must have at least
\[
\max\left\{12,\left\lceil\frac{2n+98}{11}\right\rceil\right\}
\]
triangular faces.

## 6. What is—and is not—settled

The three stated special cases are proved completely. No external colouring theorem is used.

There is also a concrete finite-size consequence for the next triangle-count case. If an orientation of a planar graph with at most twelve undirected triangles were a counterexample, a critical induced subgraph would satisfy
\[
t=12,\qquad n\le17,\qquad m=2n+2.
\]
Its vertices of degree greater than four would have degree multiset either
\[
\{5,5,5,5\}\quad\text{or}\quad\{6,5,5\},
\]
and every nontriangular face would be a quadrilateral. I have **not** exhaustively checked these possibilities.

The full conjecture is not proved. Numerically, (8) remains compatible with ordinary planar density \(m\le3n-6\) for every \(n\ge8\). Thus these arguments do not eliminate a hypothetical obstruction with sufficiently many nearby triangles. No counterexample is constructed, and no claim that these partial results are new is made.