```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture is proved here for 6-regular graphs of order at most 10, for those of girth at least five with a quantitative short-cycle extension, and for all 6-regular line graphs.",
  "would_publish": false,
  "caveats": "The dense short-cycle, non-line-graph case remains open, and the literature novelty of these partial results has not been checked."
}
```

# 1. Statement and conventions

All graphs below are finite and simple, as in the source paper. Simplicity is essential: if parallel edges are allowed, two vertices joined by six parallel edges form a 6-regular multigraph with no \(K_6\) minor.

The conjecture is:

> **Conjecture.** Every nonempty 6-regular simple graph contains a \(K_6\) minor.

I do not resolve the conjecture. I prove three partial results:

1. Every 6-regular graph on at most ten vertices contains a \(K_6\) minor.
2. Every 6-regular graph of girth at least five contains a \(K_6\) minor. More generally, a quantitative bound in terms of triangles and 4-cycles suffices.
3. Every 6-regular graph which is a line graph contains a \(K_6\) minor.

I use the sharp \(t=6\) form of Mader's theorem:

> **Mader's theorem.** If a simple graph \(Q\) has \(N\ge 6\) vertices and
> \[
> |E(Q)|\ge 4N-9,
> \]
> then \(Q\) contains a \(K_6\) minor.

---

# 2. Graphs of order at most ten

## Proposition 2.1

Every 6-regular simple graph on at most ten vertices contains a \(K_6\) minor.

### Proof

Let \(G\) be 6-regular on \(n\) vertices. Necessarily \(n\ge 7\), and
\[
|E(G)|=3n.
\]

For \(7\le n\le 9\),
\[
3n\ge 4n-9,
\]
so Mader's theorem applies.

It remains to consider \(n=10\). Let \(H=\overline G\). Then \(H\) is cubic.

For \(uv\in E(G)\), equivalently \(uv\notin E(H)\), let
\[
\lambda_H(u,v)=|N_H(u)\cap N_H(v)|.
\]
Among the other eight vertices, exactly
\[
8-\bigl|N_H(u)\cup N_H(v)\bigr|
 =8-(6-\lambda_H(u,v))
 =2+\lambda_H(u,v)
\]
are adjacent to both \(u\) and \(v\) in \(G\). Thus
\[
|N_G(u)\cap N_G(v)|=2+\lambda_H(u,v).
\]

If \(H\) has two nonadjacent vertices \(u,v\) with no common neighbor, contract the edge \(uv\) of \(G\). The contraction deletes \(uv\) and one duplicate edge for each common \(G\)-neighbor, hence the resulting nine-vertex graph has
\[
30-1-2=27=4\cdot 9-9
\]
edges. Mader's theorem then gives a \(K_6\) minor.

We may therefore assume that every two nonadjacent vertices of \(H\) have a common neighbor. Hence \(H\) is connected and has diameter at most two. The Moore bound for a cubic graph of diameter two is
\[
1+3+3\cdot 2=10.
\]
Since \(H\) has exactly ten vertices, equality holds. The usual equality argument shows that \(H\) is the Petersen graph:

- for a vertex \(x\), its three neighbors are independent;
- their six remaining neighbors are all distinct;
- these remaining six vertices induce a 6-cycle;
- the two vertices attached to any one neighbor of \(x\) are opposite on that 6-cycle.

This determines the Petersen graph uniquely.

Represent the Petersen graph as the Kneser graph on the 2-subsets of \([5]\), with disjoint pairs adjacent. Its complement is therefore the intersection graph of the edges of \(K_5\), namely
\[
G\cong L(K_5).
\]

Here is an explicit \(K_6\)-minor model in \(L(K_5)\). Label the vertices of \(L(K_5)\) by the edges \(ij\) of \(K_5\). Take the six branch sets
\[
\begin{aligned}
B_1&=\{12\},&
B_2&=\{13\},&
B_3&=\{14\},&
B_4&=\{15\},\\
B_5&=\{23,34,45\},&
B_6&=\{24,25,35\}.
\end{aligned}
\]
The first four are pairwise adjacent. Both \(B_5\) and \(B_6\) are connected and meet every vertex \(2,3,4,5\) of the underlying \(K_5\), so each is adjacent in the line graph to all of \(B_1,\dots,B_4\). Finally, \(B_5\) and \(B_6\) are adjacent, for example via the edges \(23\) and \(24\). Thus these are six pairwise adjacent connected disjoint branch sets. ∎

A useful one-edge version of the same calculation is the following.

## Lemma 2.2

Let \(G\) be 6-regular on \(n\) vertices. If some edge \(uv\) lies in at most \(12-n\) triangles, then \(G\) contains a \(K_6\) minor.

### Proof

Write \(c=|N(u)\cap N(v)|\). Contracting \(uv\) produces a graph on \(n-1\) vertices with
\[
3n-1-c
\]
edges. If \(c\le 12-n\), then
\[
3n-1-c\ge 4(n-1)-9,
\]
and Mader's theorem applies. ∎

For example, this settles any triangle-free 6-regular graph on at most twelve vertices.

---

# 3. A matching-contraction criterion

Let \(G\) be 6-regular on \(n\) vertices, and let \(M\) be a matching of size \(k\). Contract every edge of \(M\), and suppress parallel edges, obtaining \(Q_M\).

Before suppressing parallel edges, contraction removes exactly the \(k\) matching edges. Let \(D(M)\) denote the further number of edges lost when parallel edges are suppressed. Thus
\[
|V(Q_M)|=n-k,\qquad
|E(Q_M)|=3n-k-D(M).
\]

Consequently, if
\[
3k-D(M)\ge n-9, \tag{3.1}
\]
then
\[
|E(Q_M)|\ge 4|V(Q_M)|-9,
\]
and Mader's theorem gives a \(K_6\) minor.

## 3.1 High girth

## Theorem 3.1

Every 6-regular graph of girth at least five contains a \(K_6\) minor.

### Proof

By Vizing's theorem, the edges of \(G\) can be properly colored with at most seven colors. Since \(|E(G)|=3n\), some color class is a matching \(M\) with
\[
|M|\ge \frac{3n}{7}>\frac n3.
\]

We claim that contracting \(M\) creates no parallel edges.

- A singleton vertex cannot be adjacent to both ends of a matching edge, since that would give a triangle.
- If two matching edges had at least two edges between their endpoint pairs, then either two such edges share an endpoint, producing a triangle, or they are disjoint, producing a 4-cycle.

Thus \(D(M)=0\). Therefore
\[
3|M|>n,
\]
which is stronger than (3.1). Hence \(Q_M\), and therefore \(G\), has a \(K_6\) minor. ∎

This argument is independent of the bipartite theorem from the source paper and applies, in particular, to nonbipartite graphs of girth at least five.

## 3.2 A quantitative short-cycle extension

Let \(T(G)\) be the number of triangles of \(G\), and let \(C_4(G)\) be the number of 4-cycles, not necessarily induced.

## Theorem 3.2

Let \(G\) be a 6-regular graph on \(n\) vertices, and let \(q=\chi'(G)\in\{6,7\}\). If
\[
3T(G)+2C_4(G)\le (9-q)n+9q, \tag{3.2}
\]
then \(G\) contains a \(K_6\) minor.

In particular, by Vizing's theorem it suffices that
\[
3T(G)+2C_4(G)\le 2n+63. \tag{3.3}
\]
If \(G\) is class one, it suffices that
\[
3T(G)+2C_4(G)\le 3n+54. \tag{3.4}
\]

### Proof

Fix a proper \(q\)-edge-coloring, with color classes \(M_1,\dots,M_q\). Put \(k_i=|M_i|\).

For a matching \(M\), let:

- \(t(M)\) be the number of triangles containing an edge of \(M\);
- \(c(M)\) be the number of pairs \((C,\{e,f\})\), where \(C\) is a 4-cycle and \(e,f\in M\) are opposite edges of \(C\).

We claim
\[
D(M)\le t(M)+c(M). \tag{3.5}
\]

Indeed, consider two blocks after contracting \(M\).

- Between a singleton and a two-vertex block, two original edges produce one duplicate, and those two edges together with the matching edge form a triangle.
- For two two-vertex blocks, let \(r\) be the number of cross-edges between their endpoint pairs. The duplicate loss is \(\max\{0,r-1\}\). If \(r=2\), the two cross-edges either share an endpoint, giving a triangle, or are disjoint, giving a 4-cycle whose opposite edges are the two matching edges. If \(r=3\), there are two such triangles. If \(r=4\), there are four. Thus the duplicate loss is bounded by the indicated triangles and 4-cycles.

This proves (3.5).

Every triangle has its three edges in three distinct color classes, so
\[
\sum_{i=1}^q t(M_i)=3T(G).
\]
For each 4-cycle, each of its two opposite edge pairs can be monochromatic in at most one color. Hence
\[
\sum_{i=1}^q c(M_i)\le 2C_4(G).
\]
Also
\[
\sum_{i=1}^q k_i=|E(G)|=3n.
\]
Therefore
\[
\sum_{i=1}^q\bigl(3k_i-t(M_i)-c(M_i)\bigr)
 \ge 9n-3T(G)-2C_4(G).
\]
Under (3.2), the right-hand side is at least \(q(n-9)\). Hence for some \(i\),
\[
3k_i-t(M_i)-c(M_i)\ge n-9.
\]
By (3.5),
\[
3k_i-D(M_i)\ge n-9.
\]
The matching-contraction criterion now gives a \(K_6\) minor. For \(n\le10\), Proposition 2.1 already applies; for \(n\ge11\), the contracted graph has at least six vertices, as required by Mader's theorem. ∎

Thus any counterexample must satisfy
\[
3T(G)+2C_4(G)\ge 2n+64.
\]
In particular, a triangle-free counterexample would need at least \(n+32\) distinct 4-cycles.

---

# 4. The line-graph case

## Theorem 4.1

Every 6-regular graph which is a line graph contains a \(K_6\) minor.

The main ingredient is a result about line graphs of 4-regular graphs.

## Lemma 4.2

If \(H\) is a nonempty simple 4-regular graph, then \(L(H)\) contains a \(K_6\) minor.

### Proof

It suffices to treat a connected component of \(H\).

### Step 1: A 4-edge-connected multigraph

First let \(K\) be a loopless, 4-regular, 4-edge-connected multigraph on at least three vertices. Choose \(v\in V(K)\) and put
\[
F=K-v.
\]

We claim that \(F\) contains two edge-disjoint spanning trees. By the Nash-Williams–Tutte spanning-tree packing theorem, it is enough to show that every partition of \(V(F)\) into \(r\) nonempty parts has at least \(2(r-1)\) crossing edges.

Given such a partition, append \(\{v\}\) as one more part, obtaining a partition of \(V(K)\) into \(r+1\) parts. Every part has edge-boundary at least four. Summing boundaries and dividing by two shows that at least \(2(r+1)\) edges cross this partition. Exactly four of these are incident with \(v\), so at least
\[
2(r+1)-4=2(r-1)
\]
edges cross the original partition of \(F\). Thus \(F\) has two edge-disjoint spanning trees \(T_1,T_2\).

Let \(e_1,e_2,e_3,e_4\) be the four edges incident with \(v\). In \(L(K)\), take the six branch sets
\[
\{e_1\},\ \{e_2\},\ \{e_3\},\ \{e_4\},\ E(T_1),\ E(T_2).
\]
The four singleton sets are pairwise adjacent. Each \(T_j\) spans \(K-v\), so \(E(T_j)\) is connected in the line graph and is adjacent to every \(e_i\). Finally, \(E(T_1)\) and \(E(T_2)\) are adjacent because both trees have an incident edge at every vertex of \(K-v\). Hence these six sets form a \(K_6\)-minor model.

### Step 2: Reduction across a 2-edge cut

Now let \(H\) be connected, simple and 4-regular. Every edge cut of \(H\) has even size. Thus either \(H\) is 4-edge-connected, in which case Step 1 applies, or \(H\) has a 2-edge cut.

Choose \(X\subsetneq V(H)\), nonempty, with
\[
|\delta_H(X)|=2
\]
and \(|X|\) minimum. Both \(H[X]\) and \(H-X\) are connected: otherwise the positive, even boundary sizes of their components could not sum to two.

Write the two cut edges as
\[
aa',\qquad bb',
\]
where \(a,b\in X\). We have \(a\ne b\). For if \(a=b\), then \(a\) has two neighbors in \(X\), and \(X-\{a\}\) would be the shore of a smaller 2-edge cut.

Form a loopless 4-regular multigraph
\[
K=H[X]+ab,
\]
where the new edge \(ab\) is allowed to be parallel to an existing edge. The minimality of \(X\) implies that \(K\) has no 2-edge cut. Indeed, if \(Y\subsetneq X\) defined a 2-edge cut in \(K\), then:

- if the new edge \(ab\) crosses \(Y\), replacing it by the appropriate original cut edge gives a 2-edge cut of \(H\) with shore \(Y\);
- if neither \(a\) nor \(b\) lies in \(Y\), the same cut already exists in \(H\);
- if both lie in \(Y\), apply the previous case to \(X-Y\).

Each contradicts the minimality of \(X\). Therefore \(K\) is 4-edge-connected. Also \(|X|\ge3\), since a two-vertex simple subgraph cannot contain the required three internal edges. Step 1 gives a \(K_6\)-minor model in \(L(K)\).

It remains to lift that model to \(L(H)\). Since \(H-X\) is connected, the new edge \(ab\) can be replaced by an \(a\)-to-\(b\) path whose internal edges and vertices lie outside \(X\). In the line graph, the vertices corresponding to the edges of this path form a connected set, disjoint from all vertices corresponding to \(E(H[X])\), and have all adjacencies needed to replace the line-graph vertex corresponding to the artificial edge \(ab\). Thus every \(K_6\) model in \(L(K)\) lifts to one in \(L(H)\). ∎

We now prove Theorem 4.1.

### Proof of Theorem 4.1

Let \(G=L(H)\) be 6-regular, with \(H\) simple. We may restrict to a connected component of \(H\) containing an edge.

For every \(uv\in E(H)\),
\[
d_{L(H)}(uv)=d_H(u)+d_H(v)-2=6,
\]
so
\[
d_H(u)+d_H(v)=8. \tag{4.1}
\]

Along every path in \(H\), vertex degrees therefore alternate between \(a\) and \(8-a\). If \(H\) is nonbipartite, an odd cycle forces \(a=4\), so \(H\) is 4-regular and Lemma 4.2 applies.

If \(H\) is bipartite, it is semiregular. Up to exchanging its parts, the possible degree pairs are
\[
(1,7),\quad (2,6),\quad (3,5),\quad (4,4).
\]

- In the \((1,7)\) case, the seven edges incident with a degree-seven vertex give a \(K_7\) in \(L(H)\).
- In the \((2,6)\) case, the six edges incident with a degree-six vertex give a \(K_6\) in \(L(H)\).
- The \((4,4)\) case follows from Lemma 4.2.
- It remains to treat the \((3,5)\) case.

Let \(A,B\) be the bipartition, with every vertex of \(A\) of degree three and every vertex of \(B\) of degree five. There exists \(b\in B\) which is not a cutvertex. To see this, suppose every vertex of \(B\) were a cutvertex and choose an end block. Apart from at most one cutvertex, all vertices of this block are non-cutvertices and hence would lie in \(A\). Thus the block has only one \(B\)-vertex and is a star. A nontrivial star is not 2-connected, so the block would have to be a single bridge \(ba\). But then the non-cutvertex \(a\in A\) would have degree one, contrary to \(d(a)=3\).

Thus choose a non-cutvertex \(b\in B\). Then \(H-b\) is connected; let \(T\) be a spanning tree of \(H-b\). The five edges incident with \(b\) give five pairwise adjacent singleton branch sets in \(L(H)\). The edge set \(E(T)\) is a sixth connected branch set. Since \(T\) spans every neighbor of \(b\), it is adjacent to each of the five singleton branch sets. This gives a \(K_6\) minor. ∎

---

# 5. Further necessary conditions and the remaining gap

A 6-regular graph is never apex. Indeed, if \(G\) has \(n\) vertices and \(v\in V(G)\), then
\[
|E(G-v)|=3n-6,
\]
whereas a planar graph on \(n-1\) vertices has at most
\[
3(n-1)-6=3n-9
\]
edges.

Combining the source paper's bipartite theorem with the results above, any counterexample to the conjecture must satisfy all of the following:

1. It has at least eleven vertices.
2. It is nonbipartite.
3. It is not a line graph.
4. It is nonapex.
5. It has many short cycles:
   \[
   3T(G)+2C_4(G)\ge 2|V(G)|+64.
   \]

These conditions do not yield a contradiction. In particular, the matching-contraction argument loses effectiveness when many matching edges lie in triangles or as opposite edges of 4-cycles. Controlling precisely that dense local regime appears to be the principal unresolved gap in the present approach.