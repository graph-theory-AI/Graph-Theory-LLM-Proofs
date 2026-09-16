```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A self-contained sparsity bound proves the conjecture for planar graphs with at most nine undirected triangles, and for those whose distinct triangles have pairwise distance at least three.",
  "would_publish": false,
  "caveats": "The general conjecture is not resolved; no novelty claim is made for these partial results."
}
```

# Partial results

An **acyclic 2-colouring** of a digraph is a colouring of its vertices with two colours such that neither colour class contains a directed cycle.

I prove the following statements without using the literature cited in the question.

**Theorem 1 — Sparsity criterion.**  
Let \(F\) be a finite simple graph. If
\[
\operatorname{mad}(F):=
\max_{\substack{J\subseteq F\\ |V(J)|>0}}
\frac{2|E(J)|}{|V(J)|}
\le \frac{25}{6},
\]
then every orientation of \(F\) has an acyclic 2-colouring.

**Theorem 2 — Planar special cases.**  
Every orientation of a finite simple planar graph \(F\) has an acyclic 2-colouring if either:

1. \(F\) contains at most nine triangles; or
2. every two distinct triangles of \(F\) have distance at least three.

Here a triangle means **any undirected 3-cycle**, not merely a directed triangle or a triangular face. The distance between two triangles is the minimum distance between their vertex sets.

Both special cases allow directed triangles. The argument rests on a structural restriction on vertices of degree four in a minimal obstruction.

## 1. Critical obstructions and a recolouring operation

Call an oriented graph \(D\) **critical** if it has no acyclic 2-colouring, but every proper induced subdigraph does.

Every critical \(D\) satisfies
\[
d^+(v)\ge 2,\qquad d^-(v)\ge 2
\tag{1}
\]
for every vertex \(v\). Indeed, if \(d^+(v)\le 1\), colour \(D-v\) and give \(v\) a colour absent from its out-neighbours. No monochromatic directed cycle can then contain \(v\). The argument for in-degree is identical.

Let
\[
L=\{v\in V(D):d^+(v)=d^-(v)=2\}.
\]
By (1), these are exactly the vertices of underlying degree four.

### Moving an uncoloured vertex

Suppose \(v\in L\) and \(D-v\) has an acyclic 2-colouring. The two out-neighbours of \(v\) must have different colours; otherwise the missing colour extends the colouring to \(v\). Likewise, its two in-neighbours must have different colours.

If \(u\in L\) is adjacent to \(v\), we may:

- uncolour \(u\);
- give \(v\) the former colour of \(u\).

The resulting colouring of \(D-u\) is acyclic. For example, if \(v\to u\), then \(u\) was the unique out-neighbour of \(v\) with that colour. After uncolouring \(u\), no monochromatic directed cycle can pass through \(v\). The reverse orientation is handled using in-neighbours.

Thus the uncoloured vertex—the **hole**—can be moved along any walk in the underlying graph induced by \(L\).

### Rotating around a cycle

Let
\[
C=v_0v_1\cdots v_{k-1}v_0
\]
be an undirected cycle contained in \(L\), initially with hole \(v_0\). Move the hole once around \(C\), returning to \(v_0\). If the initial colours on \(v_1,\ldots,v_{k-1}\) are
\[
(a_1,a_2,\ldots,a_{k-1}),
\]
their new colours are
\[
(a_2,a_3,\ldots,a_{k-1},a_1).
\tag{2}
\]
All vertices outside \(C\) retain their colours.

Two consequences will be useful.

**Rotation consequence A.**  
If \(v_0\) has exactly one out-neighbour in \(V(C)\), then all vertices of \(C-v_0\) have the same colour.

Indeed, the other out-neighbour lies outside \(C\), so its colour remains fixed under rotations. The internal out-neighbour must always have the opposite colour. Repeated applications of (2) bring every colour on \(C-v_0\) to that position.

**Rotation consequence B.**  
If both cycle edges incident with \(v_0\) point away from \(v_0\), then \(k\) is odd, and both colours occur on \(C-v_0\).

The colours at \(v_1\) and \(v_{k-1}\) must differ after every rotation. Consequently the circular word
\[
a_1a_2\cdots a_{k-1}
\]
alternates between the two colours. Its length \(k-1\) is therefore even.

## 2. The degree-four vertices induce a cactus

**Lemma.**  
In a critical oriented graph \(D\), every undirected cycle in the graph induced by \(L\) is consistently directed. Consequently, the underlying graph induced by \(L\) is a cactus: each block is an isolated vertex, an edge, or a cycle.

**Proof.**  
Suppose otherwise, and choose a shortest undirected cycle \(C\subseteq L\) that is not consistently directed.

### Case 1: \(C\) has a chord

Let the chord be \(a\to b\). It divides \(C\) into two shorter cycles \(C_1,C_2\), both consistently directed by minimality.

The two paths obtained by removing the chord from these cycles therefore run from \(b\) to \(a\). Their first vertices are the two distinct out-neighbours of \(b\).

Fix an acyclic 2-colouring of \(D-b\). In each \(C_i\), the vertex \(b\) has exactly one out-neighbour on that cycle, with its other out-neighbour outside it. Rotation consequence A says that \(C_i-b\) is monochromatic.

But \(C_1-b\) and \(C_2-b\) both contain \(a\), so their colours agree. The two out-neighbours of \(b\) consequently have the same colour, a contradiction.

### Case 2: \(C\) is chordless

A cycle orientation that is not consistently directed has a vertex \(v\) whose two incident cycle edges point away from it.

Start with an acyclic 2-colouring of \(D-v\). Rotation consequence B shows that \(|C|\) is odd and that both colours occur on \(C-v\).

An odd cycle cannot have every vertex be a source or a sink on the cycle: sources and sinks would have to alternate. Hence some vertex \(w\in V(C)\) has one incoming and one outgoing cycle edge.

Move the hole from \(v\) to \(w\) along \(C\). This preserves the multiset of colours on the coloured vertices of \(C\), so both colours still occur.

Because \(C\) is chordless, \(w\) has exactly one out-neighbour in \(V(C)\). Rotation consequence A now says that \(C-w\) is monochromatic, a contradiction.

This proves that every cycle in \(L\) is consistently directed.

Finally, the underlying graph induced by \(L\) cannot contain a theta: three internally vertex-disjoint paths with the same two endpoints. At one endpoint, two of the three incident edges have the same direction. The cycle formed by those two paths is not consistently directed.

A graph containing no theta has only edges and cycles as its nontrivial blocks, and hence is a cactus. \(\square\)

## 3. A density bound for every critical obstruction

Write
\[
n=|V(D)|,\qquad m=|A(D)|,
\]
and partition the vertices into \(L\) and \(H=V(D)\setminus L\). Put
\[
\ell=|L|,\qquad h=|H|.
\]

Suppose first that \(L\neq\varnothing\), and let \(c\ge 1\) be the number of components of its underlying graph.

A simple cactus on \(\ell\) vertices with \(c\) components has at most
\[
\frac32(\ell-c)
\tag{3}
\]
edges. To see this, each cycle contributes one edge beyond a forest and uses at least two of the \(\ell-c\) edges in a spanning forest.

Every vertex in \(L\) has degree four, so (3) gives
\[
e(L,H)
=4\ell-2e(L)
\ge \ell+3c.
\tag{4}
\]

Every vertex of \(H\) has degree at least five. Therefore
\[
2m\ge 4\ell+5h=5n-\ell.
\tag{5}
\]
Also, using (4),
\[
2m
=4\ell+\sum_{v\in H}d(v)
\ge 4\ell+e(L,H)
\ge 5\ell+3c.
\tag{6}
\]
Adding five times (5) to (6) yields
\[
12m\ge 25n+3c\ge 25n+3.
\tag{7}
\]

If \(L=\varnothing\), all vertices have degree at least five, and
\[
12m\ge 30n\ge 25n+3.
\]
Thus every critical oriented graph satisfies
\[
\boxed{\quad m\ge \frac{25n+3}{12}.\quad}
\tag{8}
\]

### Proof of Theorem 1

If an orientation of \(F\) were not acyclically 2-colourable, it would contain a critical induced subdigraph \(D\). By (8), its underlying graph would have average degree
\[
\frac{2m}{n}
\ge \frac{25}{6}+\frac{1}{2n}
> \frac{25}{6},
\]
contrary to the hypothesis on \(\operatorname{mad}(F)\). \(\square\)

## 4. Applying the bound to planar graphs

Suppose a planar orientation is not acyclically 2-colourable, and take a critical induced subdigraph \(D\).

Its underlying graph is 2-connected. Otherwise, colour the proper pieces separated by a cutvertex, exchange the two colour names as necessary so that they agree at the cutvertex, and combine the colourings. Every directed cycle lies in one piece, giving a contradiction. Disconnected graphs are even easier.

Fix a plane embedding of this underlying graph, and let \(t\) be its number of triangular faces. All other faces have length at least four, so Euler’s formula gives
\[
2m\ge 3t+4(f-t),
\qquad f=2-n+m.
\]
Rearranging,
\[
m\le 2n-4+\frac t2.
\tag{9}
\]

Combining (8) and (9),
\[
25n+3
\le 12m
\le 24n-48+6t.
\]
Hence every critical planar obstruction must satisfy
\[
\boxed{\quad n\le 6t-51.\quad}
\tag{10}
\]
Equivalently, it must have at least
\[
\left\lceil\frac{n+51}{6}\right\rceil
\]
triangular faces.

### At most nine triangles

Distinct triangular faces here correspond to distinct undirected triangles. A triangle can bound faces on both sides only when the entire connected graph is that triangle, which is impossible because \(D\) has minimum degree at least four.

If the original planar graph contains at most nine triangles, then \(t\le 9\). Equation (10) gives
\[
n\le 3,
\]
contradicting minimum degree at least four.

This proves Theorem 2(1).

### Triangles at pairwise distance at least three

The distance condition is preserved when taking subgraphs: no new triangles appear, and distances cannot decrease.

Consider a triangular face with boundary \(T\). Each of its three vertices has at least two neighbours outside \(T\). These six outside neighbours are distinct: a vertex adjacent to two vertices of \(T\) would create another triangle intersecting \(T\), contrary to the distance condition. Therefore the closed neighbourhood satisfies
\[
|N[T]|\ge 9.
\]

The closed neighbourhoods of distinct triangles are disjoint, since an intersection would put those triangles at distance at most two. Applying this to the \(t\) triangular faces gives
\[
n\ge 9t.
\tag{11}
\]
Together, (10) and (11) imply
\[
9t\le 6t-51,
\]
which is impossible.

This proves Theorem 2(2). \(\square\)

## 5. What remains unresolved

These arguments do **not** establish the full Two Color Conjecture.

The obstruction-density bound is compatible with ordinary planar density:
\[
\frac{25n+3}{12}\le 3n-6
\]
already holds for every integer \(n\ge 7\). Thus Euler’s formula alone does not close the argument. A hypothetical counterexample may have many nearby triangles and enough vertices of degree at least five to satisfy all the inequalities above.

The concrete progress is:

- a self-contained cactus restriction on the degree-four vertices of a critical obstruction;
- the critical density bound \(12m\ge 25n+3\);
- two planar special cases that permit directed triangles.

No counterexample is constructed, and I have not established that these partial results are new.