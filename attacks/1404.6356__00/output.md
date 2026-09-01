```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "There is an exact 2^{O_Sigma(sqrt n)} algorithm in general and an O*(4^{4 gamma+t}) algorithm for graphs with t triangles, but neither yields polynomial time for unrestricted fixed-surface graphs.",
  "would_publish": false,
  "caveats": "These are consequences of standard separator and degree-choosability theorems; no unrestricted polynomial algorithm or hardness result is obtained."
}
```

# Mathematical writeup

## 1. Problem and conventions

Fix a closed surface \(\Sigma\) of Euler genus \(\gamma\). The input is a finite graph \(G\) embedded in \(\Sigma\), and the question is whether \(\chi(G)\le 4\).

Loops immediately give a negative answer, and parallel edges can be suppressed, so assume throughout that \(G\) is simple. For the sphere, the answer is always affirmative by the Four-Color Theorem. The issue is therefore fixed surfaces of positive genus.

I obtain two unconditional exact algorithms:

1. a general subexponential algorithm with running time
   \[
   2^{O(\sqrt{(\gamma+1)n})};
   \]
2. an FPT algorithm parameterized by the number of vertices of degree at least five in the \(4\)-core. On a surface, this gives
   \[
   O^*(4^{\,4\gamma+t}),
   \]
   where \(t\) is the number of triangles.

The second result gives polynomial time for every fixed surface when \(t=O(\log n)\), in particular for triangle-free graphs. It does not handle triangulations, where \(t\) and the number of degree-at-least-five vertices may both be linear.

---

## 2. General \(2^{O_\Sigma(\sqrt n)}\) algorithm

### Separator lemma

A standard constructive separator theorem for surface-embedded graphs states that an \(m\)-vertex graph of Euler genus at most \(\gamma\) has a vertex set \(S\) satisfying

\[
|S|\le a\sqrt{(\gamma+1)m},
\]

for an absolute constant \(a\), such that every component of \(G-S\) has at most \(2m/3\) vertices. Given the embedding, such a separator can be found in polynomial time.

Applying this recursively gives a tree decomposition whose width \(w(m)\) satisfies

\[
w(m)\le a\sqrt{(\gamma+1)m}+w(2m/3).
\]

Consequently,

\[
w(m)\le
\frac{a}{1-\sqrt{2/3}}\sqrt{(\gamma+1)m}
=O(\sqrt{(\gamma+1)m}).
\]

Indeed, when recursing on a component, add the current separator to every bag of the child decomposition; the separator sizes accumulated along a root-to-leaf path form a geometric series.

### Coloring dynamic program

On a tree decomposition of width \(w\), store for each bag \(B\) and each map

\[
\varphi:B\longrightarrow\{1,2,3,4\}
\]

whether \(\varphi\) is proper on \(G[B]\) and extends to the part of the graph below that bag. Standard introduce, forget, and join transitions decide 4-colorability using \(O(4^{w+1})\) states per bag.

Thus:

\[
\boxed{\text{4-colorability on Euler genus }\gamma
\text{ can be decided in }
2^{O(\sqrt{(\gamma+1)n})}\text{ time}.}
\]

For fixed \(\Sigma\), this is \(2^{O_\Sigma(\sqrt n)}\). This argument is exact and does not use the Four-Color Theorem, but it does not give polynomial time.

---

## 3. An FPT algorithm from the \(4\)-core

The more surface-specific partial result starts with a simple reduction.

### 3.1 The \(4\)-core

Repeatedly delete vertices whose current degree is at most three. Let \(K\) be the resulting \(4\)-core.

At each deletion, the current graph is 4-colorable if and only if the graph with that vertex deleted is 4-colorable: any coloring of the smaller graph extends greedily because the deleted vertex has at most three neighbors. Therefore

\[
G\text{ is 4-colorable}\quad\Longleftrightarrow\quad K\text{ is 4-colorable}.
\]

Deleted vertices can be reinserted in reverse order if an actual coloring is required.

Treat the connected components \(K_1,\dots,K_s\) independently. For one such component \(K_i\), put

\[
X_i=\{v\in V(K_i):d_{K_i}(v)\ge 5\},
\qquad h_i=|X_i|.
\]

Every vertex of \(K_i-X_i\) has degree exactly four in \(K_i\).

### 3.2 Enumerating the high-degree vertices

Enumerate the at most \(4^{h_i}\) maps

\[
c:X_i\longrightarrow\{1,2,3,4\},
\]

discarding maps that are improper on \(K_i[X_i]\). Let \(H=K_i-X_i\), and give each \(v\in V(H)\) the list

\[
L_c(v)=\{1,2,3,4\}\setminus
\{c(x):x\in N_{K_i}(v)\cap X_i\}.
\]

If \(a=|N_{K_i}(v)\cap X_i|\), then

\[
d_H(v)=4-a.
\]

At most \(a\) distinct colors are removed from the four-color palette, and hence

\[
|L_c(v)|\ge 4-a=d_H(v).
\tag{1}
\]

Thus the remaining problem is a special degree-list-coloring instance.

### 3.3 Degree-list lemma

Use the standard degree-choosability theorem:

> **Degree-list lemma.**  
> Let \(Q\) be a connected graph with at least two vertices, with lists satisfying
> \[
> |L(v)|\ge d_Q(v)
> \]
> for every \(v\). If \(Q\) is not \(L\)-colorable, then every block of \(Q\) is either a complete graph or an odd cycle.

Graphs whose blocks are all complete graphs or odd cycles are usually called Gallai trees. This is the list-coloring form of Brooks' theorem. Its proof is the usual greedy/block argument: a non-Gallai 2-connected block contains a suitable even-cycle configuration, which is degree-list-colorable, and the remaining vertices can be colored in an order in which each has an uncolored neighbor.

The exceptional Gallai-tree case is still algorithmically easy here. Compute the block-cutvertex tree and process it from the leaves:

- a complete block has at most five vertices because \(\Delta(H)\le4\), so all possibilities can be checked by constant-sized brute force;
- an odd-cycle block can be list-colored by a path dynamic program with four possible colors;
- a message from a block to its parent cutvertex is simply the subset of the four colors permitting an extension through that block.

Isolated vertices are checked directly, particularly because (1) allows an isolated vertex to have an empty list.

It follows that, for each fixed coloring of \(X_i\), extension to \(K_i\) can be decided in polynomial time. Therefore:

\[
\boxed{
\text{4-colorability can be decided in }
\sum_i 4^{h_i}(|V(K_i)|+|E(K_i)|)^{O(1)}
\text{ time}.}
\tag{2}
\]

This parameterized result is valid for arbitrary graphs, not only embedded ones.

---

## 4. Bounding \(h_i\) by genus and triangles

Let \(t_i\) be the number of distinct triangles in \(K_i\). I claim

\[
h_i\le 4\gamma+t_i-8.
\tag{3}
\]

If the right side is negative, this means that no such nonempty \(4\)-core component exists.

Take the inherited embedding of \(K_i\), pass to a regular neighborhood, and cap its boundary curves. This gives a cellular embedding in a surface of Euler genus \(\gamma_i\le\gamma\).

Let \(n_i,m_i,f_i\) denote its numbers of vertices, edges, and faces, and let \(f_{3,i}\) be its number of triangular faces. Since \(K_i\) is simple and has minimum degree at least four, every facial boundary has length at least three. Moreover, a given graph triangle cannot bound two different triangular faces: that would require its two incident edges to be consecutive on both sides at each of its three vertices, forcing those vertices to have degree two. Hence

\[
f_{3,i}\le t_i.
\]

Counting edge-sides around faces gives

\[
2m_i\ge 3f_{3,i}+4(f_i-f_{3,i})
=4f_i-f_{3,i}.
\]

Euler's formula now yields

\[
2-\gamma_i=n_i-m_i+f_i
\le n_i-\frac{m_i}{2}+\frac{f_{3,i}}4.
\]

Consequently,

\[
m_i\le 2n_i-4+2\gamma_i+\frac{f_{3,i}}2.
\]

Since every vertex of \(K_i\) has degree at least four,

\[
h_i
\le\sum_{v\in V(K_i)}(d(v)-4)
=2m_i-4n_i.
\]

Combining the last two inequalities gives

\[
h_i\le 4\gamma_i+f_{3,i}-8
\le4\gamma+t_i-8,
\]

proving (3).

Letting \(t\) be the number of triangles in the original graph, \(t_i\le t\), so (2) implies

\[
\boxed{
\text{4-colorability is decidable in }
O^*(4^{\,4\gamma+t}).
}
\]

In particular:

- for every fixed surface and bounded \(t\), this is polynomial time;
- it remains polynomial when \(t=O(\log n)\);
- for triangle-free graphs it is \(O^*(4^{4\gamma})\).

The algorithm itself need not enumerate the triangles: it can simply compute the sets \(X_i\). The triangle count is used only to establish the running-time bound.

---

## 5. An exact planar-piece reduction

There is also a useful safe reduction based directly on the Four-Color Theorem.

> **Planar clique-side rule.**  
> Suppose \(A\cup B=V(G)\), there are no edges between \(A\setminus B\) and \(B\setminus A\), and
> \[
> S=A\cap B
> \]
> induces a clique of order at most four. If \(G[A]\) is planar, then
> \[
> G\text{ is 4-colorable}\quad\Longleftrightarrow\quad G[B]\text{ is 4-colorable}.
> \]

Only the reverse implication needs proof. Given a 4-coloring of \(G[B]\), the Four-Color Theorem supplies a 4-coloring of \(G[A]\). Since \(S\) is a clique, both colorings assign distinct colors to the vertices of \(S\). A permutation of the four colors makes the two restrictions agree, after which the colorings can be combined.

Thus arbitrary planar pieces attached along cliques of order at most four can be stripped away. Such reductions can be found in polynomial time by enumerating sets \(S\) of size at most four and testing the resulting sides for planarity.

The clique condition is essential. Let \(P=K_5-xy\), where \(xy\) is the deleted edge. This graph is planar: take a triangle \(abc\), put \(x\) on one side and \(y\) on the other, and join both to \(a,b,c\). In every 4-coloring of \(P\), the triangle \(abc\) uses three colors and both \(x\) and \(y\) must use the fourth. Hence

\[
x\text{ and }y\text{ receive the same color in every 4-coloring of }P.
\]

So even a planar piece attached through two nonadjacent terminals can carry a nontrivial equality constraint. This is a concrete obstruction to treating all planar regions as freely extendable.

---

## 6. Remaining gap

The unrestricted fixed-surface problem is not settled by these arguments.

- In a large triangulation, the number of triangles can be \(\Theta(n)\).
- The \(4\)-core can have \(\Theta(n)\) vertices of degree at least five; for example, fixed-surface triangulations may be predominantly degree six.
- The separator algorithm then retains \(4^{\Theta(\sqrt n)}\) boundary states.
- Planar regions with nonclique boundaries can transmit genuine coloring constraints, as \(K_5-xy\) demonstrates, so the Four-Color Theorem alone does not collapse those states.

A polynomial algorithm would require an additional structural theorem, an irrelevant-vertex reduction, or a polynomially bounded representation of the coloring relations across long nonclique boundaries. I have not established such a result, nor an NP-hardness reduction for any fixed positive-genus surface.