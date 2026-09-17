```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "An explicit rooted coloring proves the conjecture for every triangulation obtained by repeatedly inserting icosahedra into triangular faces.",
  "would_publish": false,
  "caveats": "This gives an infinite minimum-degree-five special case and a reducible configuration, not a general solution; no novelty is claimed."
}
```

# A rooted icosahedral patch

I do not settle the conjecture for arbitrary planar graphs. The partial result below covers an infinite family of triangulations of minimum degree five, so it genuinely uses the omission of the condition for \(k=5\).

Throughout, a **valid coloring** means a coloring with palette \([5]\) satisfying exactly the conditions in the question, for \(1\leq k\leq4\).

## 1. Partial result and a gluing principle

**Proposition.** Start with a plane triangle. Repeatedly choose a triangular face and insert an icosahedron into it, identifying a facial triangle of the icosahedron with the chosen face boundary. Every graph obtained this way has a valid coloring.

More strongly, each insertion can preserve an already assigned valid coloring of the entire old graph.

After at least one insertion, these are simple planar triangulations of minimum degree five. Thus five colors are necessary for the requested property on this family.

The key is a coloring that allows the attachment triangle to be held until the end of every relevant degeneracy ordering.

### Rooted colorings

For a coloring \(c\), write
\[
G_S=G[c^{-1}(S)].
\]
Let \(R\) be a clique of \(G\). Call a proper coloring **\(R\)-rooted valid** if, for every nonempty \(S\subseteq[5]\) with \(|S|\leq4\), the vertices of \(G_S-R\) can be deleted successively with current degree at most \(|S|-1\), while all vertices of \(R\cap V(G_S)\) are retained.

Such a coloring is valid: after those deletions, the remaining graph is a clique on at most \(|S|\) vertices.

**Gluing lemma.** Suppose \(H\) has a valid coloring, and \(P\) has an \(R\)-rooted valid coloring. Identify \(R\) with a clique of \(H\), with the two colorings agreeing there, and otherwise keep the graphs disjoint. The resulting coloring is valid.

**Proof.** Fix \(S\), with \(k=|S|\leq4\). First use the rooted deletion order on \(P_S-R\). Its vertices have no neighbors in \(H-R\), so their deletion degrees remain at most \(k-1\). Then use a degeneracy order for \(H_S\). This supplies a \((k-1)\)-degeneracy order for the union. \(\square\)

I will now give a complete certificate for an icosahedron rooted at a facial triangle.

## 2. The labeled icosahedron and its coloring

Use vertices
\[
t,s,a_0,\ldots,a_4,b_0,\ldots,b_4,
\]
with indices modulo five, and edges
\[
ta_i,\quad sb_i,\quad a_i a_{i+1},\quad b_i b_{i+1},
\quad a_i b_i,\quad a_{i+1}b_i
\qquad(i\in\mathbb Z_5).
\]
This is the usual plane icosahedron \(I\). Every vertex has degree five. Take the facial triangle
\[
R=\{t,a_1,a_2\}.
\]

Assign the color classes
\[
\begin{array}{c|l}
\text{color}&\text{vertices}\\ \hline
1&a_0,a_2,b_3\\
2&a_1,a_3,s\\
3&a_4,b_2\\
4&b_1,b_4\\
5&t,b_0
\end{array}
\tag{1}
\]
The edge description immediately verifies that this coloring is proper.

I prove that (1) is \(R\)-rooted valid.

### Two colors

First consider the proper four-coloring \(c_0\) obtained from (1) by changing
\[
c_0(t)=4,\qquad c_0(b_0)=3.
\]
Its six bichromatic induced graphs are exactly the following paths; consecutive entries specify the path edges:
\[
\begin{array}{c|l}
\text{colors}&\text{path}\\ \hline
12&a_0,a_1,a_2,a_3,b_3,s\\
13&b_0,a_0,a_4,b_3,b_2,a_2\\
14&b_1,a_2,t,a_0,b_4,b_3\\
23&a_1,b_0,s,b_2,a_3,a_4\\
24&a_3,t,a_1,b_1,s,b_4\\
34&t,a_4,b_4,b_0,b_1,b_2
\end{array}
\tag{2}
\]

Consequently, under (1), every bichromatic graph whose colors belong to \(\{1,2,3,4\}\) is a forest.

A bichromatic cycle involving color \(5\) would have to use both \(t\) and \(b_0\), since these are the only vertices of color \(5\). It would therefore be a four-cycle. But
\[
N(t)\cap N(b_0)=\{a_0,a_1\},
\]
and these two common neighbors have different colors. Hence no such cycle exists.

This also establishes the rooted condition for two colors. The retained vertices \(R\cap V(I_S)\) form either an empty set, a vertex, or an edge. A forest can be stripped down to such a retained clique by deleting vertices of degree at most one. The one-color rooted condition follows from properness.

## 3. Certificates for all three-color sets

The following table supplies all ten required rooted deletion orders.

For each row, vertices with colors outside \(S\) are absent from the outset, and the vertices of \(R\cap V(I_S)\) are retained throughout. The middle column lists **every** vertex of \(I_S-R\). The last column gives its degree at the moment it is deleted.

\[
\begin{array}{c|l|l}
S&\text{deletion order outside }R&\text{deletion degrees}\\ \hline
123&a_0,a_4,s,b_3,a_3,b_2&2,2,2,2,2,1\\
124&a_0,a_3,b_4,b_3,s,b_1&2,2,2,1,1,2\\
125&s,b_3,a_3,b_0,a_0&2,1,2,2,2\\
134&a_0,a_4,b_4,b_3,b_2,b_1&2,2,1,1,2,1\\
135&b_0,a_0,a_4,b_3,b_2&1,2,2,1,1\\
145&b_3,b_4,a_0,b_0,b_1&1,2,2,1,1\\
234&a_3,a_4,b_4,s,b_2,b_1&2,1,1,2,1,1\\
235&a_4,a_3,b_2,s,b_0&2,2,1,1,1\\
245&a_3,b_4,s,b_1,b_0&1,2,2,2,1\\
345&b_2,b_1,b_0,b_4,a_4&1,1,1,1,1
\end{array}
\tag{3}
\]

These certificates are directly checkable from the edge formula above; no computational search is being asserted. Every listed degree is at most two, proving the rooted condition for every three-color set.

## 4. All four-color sets: propagation through triangular faces

Here there is a uniform argument instead of five long deletion orders.

Put
\[
D=I-R.
\]
In the embedding with \(R\) as the outer face of \(I\), the graph \(D\) is a triangulated hexagonal disk with boundary
\[
a_0b_0b_1b_2a_3a_4a_0.
\]
Its ten bounded triangular faces are
\[
(s,b_i,b_{i+1})\qquad(i\in\mathbb Z_5)
\]
and
\[
(a_0,b_4,b_0),\quad
(a_3,b_2,b_3),\quad
(a_3,a_4,b_3),\quad
(a_4,b_3,b_4),\quad
(a_4,a_0,b_4).
\tag{4}
\]
Their edge-adjacency graph is connected, and every vertex of \(D\) belongs to one of these faces.

### Propagation observation

Suppose both endpoints of an edge of \(D\) are already absent. Then every remaining vertex of \(D\) can be deleted with current degree at most three, while retaining every remaining vertex of \(R\).

Indeed, start with a bounded triangular face incident with that edge. Its third vertex, if still present, has two absent neighbors and therefore current degree at most
\[
5-2=3.
\]
Once that vertex is deleted, the whole face is absent. Traverse a spanning tree of the edge-adjacency graph of the bounded faces. Each new face shares an already absent edge with a previously processed face, allowing its third vertex to be deleted in the same way. By (4), this eventually deletes every vertex of \(D\).

### Starting the propagation

Let \(C_j\) denote color class \(j\) in (1). For a four-color set \(S=[5]\setminus\{j\}\), regard \(C_j\) as absent initially.

In each row below, \(x\notin R\) has the two indicated neighbors in \(C_j\). Thus \(x\) has current degree at most three and can be deleted. The last column is then an edge of \(D\) with both endpoints absent.

\[
\begin{array}{c|c|c|c}
j&\text{two absent neighbors of }x&x&
\text{absent edge in }D\\ \hline
1&a_0,b_3&a_4&a_0a_4\\
2&a_3,s&b_2&a_3b_2\\
3&a_4,b_2&a_3&a_4a_3\\
4&b_1,b_4&s&b_1s\\
5&t,b_0&a_0&b_0a_0
\end{array}
\tag{5}
\]

The propagation observation now deletes all of \(I_S-R\), retaining the vertices of \(R\cap V(I_S)\), with every deletion degree at most three.

This proves the rooted condition for all five four-color sets. Together with Sections 2–3, it establishes:

**Rooted-patch conclusion.** The coloring (1) is an \(R\)-rooted valid coloring of the icosahedron.

Because the three vertices of \(R\) have distinct colors, any prescribed proper coloring of the attachment triangle with colors from \([5]\) can be matched by a permutation of the palette.

## 5. Consequences for the conjecture

### An infinite family of minimum-degree-five triangulations

A triangle has a valid coloring. When an icosahedral disk is inserted into a triangular face, permute (1) to match the existing boundary colors and apply the gluing lemma. Induction proves the proposition.

After \(q\geq1\) insertions, the graph has
\[
n=3+9q
\]
vertices. Each insertion adds nine vertices, all initially of degree five, and increases the degree of each of the three attachment vertices by three. Hence every resulting graph has minimum degree at least five.

Five colors are necessary for the requested property on these graphs. If at most four colors were used, their union would be the entire graph and would have to be at most three-degenerate, contradicting minimum degree five.

Likewise, none of these graphs admits a *full* degenerate five-coloring that also imposes the condition for \(k=5\): that would require the entire graph to be four-degenerate. Thus this special case respects the precise distinction in the problem statement.

The result also holds for every subgraph of one of these triangulations, since the requested property is hereditary under taking subgraphs.

### A reducible configuration

The rooted-patch conclusion gives a structural restriction on a smallest counterexample, if one exists:

> A smallest counterexample cannot contain this nine-vertex icosahedral disk attached to the rest of the graph only through its boundary triangle.

Otherwise, delete the nine internal vertices, validly color the smaller planar graph, and extend over the disk by the gluing lemma.

## 6. What remains unresolved

The rooted patch and all its color-set cases are certified above. The missing step toward the full conjecture is a general reduction: an arbitrary planar triangulation need not contain such an icosahedral disk. In particular, the argument requires this exact patch, not merely a vertex of degree five.

Thus this establishes a restricted special case and a concrete reducible configuration, but neither a proof of the conjecture nor an improvement of the general color-count bounds.