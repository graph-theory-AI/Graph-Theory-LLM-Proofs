```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The unresolved part can be confined to graphs containing an induced C5: every connected non-bipartite C5-free example is a complete independent-set expansion of an odd cycle and has clique-width at most 4.",
  "would_publish": false,
  "caveats": "The C5-containing case remains open; the full C5-free corollary uses the known classification of S_{1,2,3}-free bipartite graphs."
}
```

# 1. Problem and partial result

All forbidden subgraphs below are induced. Let \(S_{1,2,3}\) be the subdivided claw whose three arms have lengths \(1,2,3\).

A **complete independent-set expansion** of a cycle \(C_g\) is a graph with a partition
\[
V(G)=B_0\mathbin{\dot\cup}\cdots\mathbin{\dot\cup}B_{g-1},
\]
where every \(B_i\) is a nonempty stable set, \(B_i\) is complete to \(B_{i-1}\) and \(B_{i+1}\), and there are no other edges between bags; indices are modulo \(g\).

The main partial result is the following.

## Theorem 1

Let \(G\) be a connected, triangle-free, \(C_5\)-free, \(S_{1,2,3}\)-free graph. Then either

1. \(G\) is bipartite; or
2. \(G\) is a complete independent-set expansion of an odd cycle \(C_g\), where \(g\ge 7\).

In the second case,
\[
\operatorname{cw}(G)\le 4.
\]

Consequently, using the established theorem that \(S_{1,2,3}\)-free bipartite graphs have bounded clique-width, the class of
\[
(K_3,C_5,S_{1,2,3})\text{-free graphs}
\]
has bounded clique-width.

Thus any counterexample to the original conjecture, if one exists, must contain an induced \(C_5\).

---

# 2. Proof of Theorem 1

Assume that \(G\) is non-bipartite. Let
\[
C=c_0c_1\cdots c_{g-1}c_0
\]
be a shortest odd cycle in \(G\). It is chordless, since a chord would produce a shorter odd cycle. Triangle-freeness and \(C_5\)-freeness give \(g\ge 7\).

## 2.1. Neighborhoods of the shortest odd cycle

We first determine the possible neighborhoods on \(C\) of a vertex outside \(C\).

### Lemma 2

For every \(x\in V(G)\setminus V(C)\), one of the following holds:

1. \(N_C(x)=\varnothing\);
2. \(N_C(x)=\{c_i\}\) for some \(i\);
3. \(N_C(x)=\{c_{i-1},c_{i+1}\}\) for some \(i\).

#### Proof

Triangle-freeness implies that no two consecutive vertices of \(C\) are both adjacent to \(x\).

Suppose \(x\) has \(r\ge 2\) neighbors on \(C\). List them cyclically and let
\[
d_1,\ldots,d_r
\]
be the lengths of the intervening arcs of \(C\). Each \(d_j\ge 2\), and
\[
d_1+\cdots+d_r=g.
\]
Since \(g\) is odd, some \(d_j\) is odd. The corresponding arc, together with \(x\), is an induced odd cycle of length \(d_j+2\).

If \(r\ge 3\), then
\[
d_j\le g-2(r-1)\le g-4,
\]
and hence \(d_j+2<g\), contradicting the choice of \(C\).

Thus \(r=2\). Of the two cyclic gaps, exactly one, say \(q\), is odd. Minimality of \(C\) gives
\[
q+2\ge g.
\]
The other gap is at least \(2\), so \(q\le g-2\). Therefore \(q=g-2\), and the other gap is \(2\). Hence the two neighbors of \(x\) are \(c_{i-1}\) and \(c_{i+1}\) for some \(i\). ∎

### Lemma 3

No vertex outside \(C\) has exactly one neighbor on \(C\).

#### Proof

Suppose \(N_C(x)=\{c_i\}\). The seven vertices
\[
c_i,\quad x,\quad c_{i+1},c_{i+2},\quad
c_{i-1},c_{i-2},c_{i-3}
\]
induce an \(S_{1,2,3}\) centered at \(c_i\), with arms
\[
c_ix,\qquad
c_ic_{i+1}c_{i+2},\qquad
c_ic_{i-1}c_{i-2}c_{i-3}.
\]
Because \(g\ge 7\), the two selected portions of \(C\) have no edge between them. This is a contradiction. ∎

### Lemma 4

Every vertex of \(G\) has a neighbor on \(C\).

#### Proof

Otherwise, since \(G\) is connected, there is a shortest path beginning on \(C\) whose first two outside vertices are \(x,y\), where \(x\) has a neighbor on \(C\) and \(y\) is anticomplete to \(C\).

By Lemmas 2 and 3,
\[
N_C(x)=\{c_{i-1},c_{i+1}\}
\]
for some \(i\). Then the vertices
\[
x,\quad y,\quad c_{i-1},c_{i-2},\quad
c_{i+1},c_{i+2},c_{i+3}
\]
induce an \(S_{1,2,3}\) centered at \(x\), with arms
\[
xy,\qquad
xc_{i-1}c_{i-2},\qquad
xc_{i+1}c_{i+2}c_{i+3}.
\]
Again \(g\ge7\) ensures that there are no unwanted cycle edges. ∎

It follows that every vertex belongs to one of the sets
\[
B_i=\{c_i\}\cup
\{x\notin C:N_C(x)=\{c_{i-1},c_{i+1}\}\}.
\]

These sets partition \(V(G)\).

## 2.2. Edges between the bags

Each \(B_i\) is stable. Indeed, two outside vertices in \(B_i\) have a common neighbor \(c_{i-1}\), so an edge between them would create a triangle; moreover, no outside vertex of \(B_i\) is adjacent to \(c_i\).

Similarly, there are no edges between \(B_i\) and \(B_{i+2}\), because every such pair has the common neighbor \(c_{i+1}\).

We next exclude all other nonconsecutive edges.

### Lemma 5

If \(x\in B_0\), \(y\in B_d\), and \(xy\in E(G)\), then \(d\equiv\pm1\pmod g\).

#### Proof

Take \(d\) with
\[
3\le d\le \frac{g-1}{2}.
\]

If \(d\) is even, then
\[
x,c_1,c_2,\ldots,c_{d-1},y,x
\]
is an induced odd cycle of length \(d+1<g\), a contradiction.

If \(d\) is odd, use the other side of \(C\):
\[
x,c_{-1},c_{-2},\ldots,c_{d+1},y,x.
\]
This is an induced odd cycle of length
\[
g-d+1<g,
\]
again a contradiction.

Distances \(0\) and \(2\) have already been excluded by triangle-freeness. Thus only cyclic distance \(1\) is possible. ∎

It remains to show that consecutive bags are completely joined.

### Lemma 6

For every \(i\), \(B_i\) is complete to \(B_{i+1}\).

#### Proof

Suppose, after shifting indices, that
\[
x\in B_0,\qquad y\in B_1,\qquad xy\notin E(G).
\]
The vertices
\[
c_2,\quad y,\quad c_3,c_4,\quad c_1,x,c_{-1}
\]
induce an \(S_{1,2,3}\) centered at \(c_2\), with arms
\[
c_2y,\qquad
c_2c_3c_4,\qquad
c_2c_1xc_{-1}.
\]
The prescribed neighborhoods of \(x\) and \(y\), together with \(xy\notin E(G)\), exclude every possible cross-edge. For \(g\ge7\), there is also no edge between \(c_4\) and \(c_{-1}\). This contradiction proves completeness. ∎

Lemmas 4–6 show that \(G\) is precisely a complete independent-set expansion of \(C_g\).

---

# 3. Clique-width of the expansion

Such an expansion has clique-width at most \(4\). An explicit construction uses labels \(1,2,3,4\).

1. Create all vertices of \(B_0\) with label \(1\).
2. Create all vertices of \(B_1\) with label \(2\), and join labels \(1\) and \(2\).
3. For \(i=2,\ldots,g-2\):
   - create \(B_i\) with label \(4\);
   - join labels \(2\) and \(4\);
   - relabel \(2\) to \(3\);
   - relabel \(4\) to \(2\).
4. Create \(B_{g-1}\) with label \(4\), join labels \(2\) and \(4\), and then join labels \(1\) and \(4\).

Label \(3\) is only a repository for bags whose future adjacencies have already been completed. Hence no unwanted edges are introduced.

For completeness, every complete independent-set expansion of an odd cycle is \(S_{1,2,3}\)-free. If the center of a supposed induced \(S_{1,2,3}\) lies in \(B_i\), its three first arm vertices lie in only \(B_{i-1}\cup B_{i+1}\). Two lie in the same bag, say \(B_{i+1}\). At least one of these two arms continues to a vertex in \(B_i\) or \(B_{i+2}\), and that continuation vertex is adjacent to the other first arm vertex, contradicting inducedness.

This completes the proof of Theorem 1.

---

# 4. The bipartite part

The relevant case of the known classification of \(H\)-free bipartite graphs says that \(S_{1,2,3}\)-free bipartite graphs have bounded clique-width. This is contained in the classification by K. K. Dąbrowski and D. Paulusma, *Classifying the clique-width of \(H\)-free bipartite graphs*, Discrete Applied Mathematics 200 (2016), 43–51.

Combining that theorem with Theorem 1 gives:

## Corollary 7

The class of \((K_3,C_5,S_{1,2,3})\)-free graphs has bounded clique-width.

Thus the induced \(C_5\) case is the only unresolved case.

---

# 5. Additional structure in the \(C_5\) case

There is also a useful localization around a \(C_5\).

## Proposition 8

Let \(G\) be connected, triangle-free and \(S_{1,2,3}\)-free, and let
\[
C=c_0c_1c_2c_3c_4c_0
\]
be an induced \(C_5\). Then:

1. every vertex of \(G\) has distance at most \(2\) from \(C\);
2. the set
   \[
   R=\{v\in V(G):N_C(v)=\varnothing\}
   \]
   is stable.

### Proof

Suppose first that there is a shortest path
\[
c_i-x_1-x_2-x_3
\]
from \(C\) to a vertex at distance \(3\). Then \(x_2,x_3\) are anticomplete to \(C\).

Because \(G\) is triangle-free, \(N_C(x_1)\) is an independent subset of \(C\), hence it consists of \(c_i\), possibly together with one of \(c_{i+2},c_{i-2}\).

If \(x_1\) is not adjacent to \(c_{i-2}\), use the two cycle arms
\[
c_ic_{i+1}
\quad\text{and}\quad
c_ic_{i-1}c_{i-2}.
\]
Otherwise use
\[
c_ic_{i-1}
\quad\text{and}\quad
c_ic_{i+1}c_{i+2}.
\]
Together with
\[
c_ix_1x_2x_3,
\]
these arms induce an \(S_{1,2,3}\), a contradiction. This proves the first assertion.

For the second, suppose \(rs\) is an edge inside \(R\). By the first assertion, \(r\) has a neighbor \(x\) that has a neighbor \(c_i\in C\). Triangle-freeness gives \(xs\notin E(G)\). The path
\[
c_i-x-r-s
\]
can again be combined with one of the two choices of cycle arms above, avoiding any second neighbor of \(x\) on \(C\). This induces an \(S_{1,2,3}\), a contradiction. Thus \(R\) is stable. ∎

After fixing \(C\), every vertex adjacent to \(C\) has one of only ten possible nonempty neighborhoods on \(C\):
\[
\{c_i\}\quad\text{or}\quad\{c_{i-1},c_{i+1}\}.
\]
Each corresponding type is stable, and \(R\) is stable by Proposition 8.

As a small independent consequence, the whole class is \(9\)-colorable. In the \(C_5\) case, color a vertex adjacent to \(C\) by the index of one chosen neighbor on \(C\). Adjacent vertices cannot receive the same such color, since they would form a triangle with that cycle vertex. This uses five colors; \(R\) uses a sixth color, and \(C\) uses three fresh colors. The bipartite and odd-cycle-expansion cases need at most three colors.

---

# 6. Remaining gap

The finite partition around a \(C_5\) is not enough by itself to bound clique-width: even bipartite graphs can have unbounded clique-width despite having only two stable color classes.

Nor can one simply delete the five cycle vertices and invoke the bipartite theorem. For example, take a complete independent-set expansion of \(C_5\) with every bag of size at least two. After choosing one vertex from each bag as the designated \(C_5\), another choice of one vertex from each bag still induces a \(C_5\) in \(G-C\). These graphs are nevertheless \(S_{1,2,3}\)-free.

Therefore the unresolved task is to control the adjacency matrices between the ten \(C_5\)-neighborhood types and the stable distance-two set \(R\), presumably via modules, boundedly many bipartite complementations, or a direct rank-width decomposition. The arguments above do not provide that control, so they do not settle the original conjecture.