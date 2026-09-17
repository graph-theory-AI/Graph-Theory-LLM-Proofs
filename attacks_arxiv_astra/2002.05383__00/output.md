```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "Linear 7-coloring bounds hold for two explicit classes of planar graphs defined by the subgraph induced by their high-degree vertices, but the unrestricted minimum remains undetermined.",
  "would_publish": false,
  "caveats": "These are restricted-class results, with no novelty claim; they do not improve the supplied interval 7 <= kappa <= 10."
}
```

## 1. A proved special case

I do not determine \(\kappa\). The following gives a self-contained seven-color result for classes allowing arbitrarily large maximum degree.

All graphs below are finite and simple. Put
\[
X=\{v\in V(G):d_G(v)\ge 6\},\qquad Y=V(G)\setminus X.
\]
Thus every vertex of \(Y\) has degree at most five **in \(G\)**. Write
\[
a=|X|,\quad b=|Y|,\quad
p=|E(G[X])|,\quad q=|E(X,Y)|,\quad r=|E(G[Y])|.
\]
In particular, \(n=a+b\) and \(m=p+q+r\).

### Theorem
For every planar graph \(G\):

1. If \(\Delta(G[X])\le 5\), then
   \[
   \operatorname{diam}R_7(G)
   \le n+m+\frac52q
   \le 9n.
   \]
2. If \(G[X]\) is \(2\)-degenerate, then
   \[
   \operatorname{diam}R_7(G)
   \le 2a+b+2q+r
   \le 7n.
   \]

Both assertions also hold for reconfiguration with arbitrary vertex lists of size at least seven.

The number seven is necessary for each of these restricted classes. Neither structural hypothesis, however, follows from planarity.

## 2. Lifting a sequence through degree-five vertices

The following observation is the main mechanism.

### Lifting lemma
Let \(\alpha,\beta\) be proper seven-colorings of \(G\). Suppose there is a recoloring sequence from \(\alpha|_X\) to \(\beta|_X\) in \(G[X]\), changing each \(x\in X\) exactly \(t_x\) times. Then \(\alpha\) can be transformed into \(\beta\) in at most
\[
b+r+\sum_{x\in X}\bigl(1+d_Y(x)\bigr)t_x
\tag{1}
\]
single-vertex recolorings.

#### Proof
Simulate the sequence on \(G[X]\). Before a prescribed change \(x:c\to c'\), clear every neighbor \(y\in Y\) currently colored \(c'\).

Such a \(y\) can always be recolored: its neighbors forbid at most five colors, and additionally forbidding its current color leaves at most six forbidden colors. There are seven colors available. After these changes, recoloring \(x\) to \(c'\) is legal in all of \(G\).

Thus a prescribed change of \(x\) costs at most \(1+d_Y(x)\) changes in \(G\).

Once \(X\) has coloring \(\beta|_X\), fix the vertices of \(Y\), in any order, to their target colors. When fixing \(y\), recolor each neighbor in \(Y\) currently using \(\beta(y)\), then recolor \(y\) itself if necessary. The same degree-five argument makes every clearing move possible.

No previously fixed vertex blocks \(\beta(y)\), because previously fixed vertices have their target colors and \(\beta\) is proper. Likewise, no vertex of \(X\) blocks it. Each edge of \(G[Y]\) is charged at most once: only when its earlier endpoint is fixed can its later endpoint require a clearing move. This final phase therefore costs at most \(b+r\). ∎

A useful point is that the cost of recoloring \(x\in X\) is weighted by \(1+d_Y(x)\). An unweighted linear bound on \(G[X]\) alone would not automatically control this cost.

## 3. Proof when the high-degree subgraph has maximum degree five

We first prove a weighted bounded-degree statement.

### Weighted fixing lemma
Let \(F\) have maximum degree at most five, and assign each vertex a positive weight \(w(v)\). Any two proper seven-colorings of \(F\) can be joined by a sequence of weighted cost at most
\[
\sum_{v\in V(F)}w(v)
+\sum_{uv\in E(F)}\min\{w(u),w(v)\},
\tag{2}
\]
where recoloring \(v\) costs \(w(v)\).

#### Proof
Order the vertices by nonincreasing weight and fix them to their target colors in that order.

When fixing \(v\), every neighbor currently using its target color is still unfixed. Recolor each such neighbor to another available color. This is possible because its degree is at most five and seven colors are available. Then assign \(v\) its target color.

Each vertex incurs its own fixing cost at most once. For an edge \(uv\), a clearing cost can be charged only to its later endpoint, whose weight is \(\min\{w(u),w(v)\}\). Each edge is charged at most once. ∎

Apply this lemma to \(F=G[X]\), with
\[
w(x)=1+d_Y(x).
\]
The weighted cost of the resulting sequence on \(G[X]\) is at most
\[
\begin{aligned}
\sum_{x\in X}w(x)
+\sum_{xx'\in E(G[X])}\min\{w(x),w(x')\}
&=a+q+p+
  \sum_{xx'\in E(G[X])}\min\{d_Y(x),d_Y(x')\}\\
&\le a+q+p+
  \frac12\sum_{x\in X}d_X(x)d_Y(x)\\
&\le a+p+\frac72q.
\end{aligned}
\]
The last inequality uses \(d_X(x)\le5\).

Adding the \(b+r\) term from the lifting lemma gives
\[
\operatorname{dist}_{R_7(G)}(\alpha,\beta)
\le n+p+r+\frac72q
=n+m+\frac52q.
\tag{3}
\]

For a simple planar graph with \(n\ge3\),
\[
m\le3n-6.
\]
Moreover, the spanning subgraph consisting of the \(X\)-\(Y\) edges is bipartite and planar, so
\[
q\le2n-4.
\]
Consequently, (3) is at most
\[
n+(3n-6)+\frac52(2n-4)=9n-16.
\]
The cases \(n\le2\) are immediate, proving the first assertion.

## 4. Proof when the high-degree subgraph is \(2\)-degenerate

Here a particularly small per-vertex bound is available.

### Lemma
In a \(2\)-degenerate graph, any two proper seven-colorings can be joined by a sequence changing each vertex at most twice.

#### Proof
Induct on the number of vertices. Choose a vertex \(v\) of degree at most two. By induction, recolor \(F-v\) between the prescribed restrictions, changing each vertex at most twice.

During this sequence, each neighbor of \(v\) uses at most three distinct colors: its initial color and at most two subsequent colors. Thus at most six colors occur on the neighbors of \(v\) during the entire sequence.

Choose a seventh color \(c\) that never occurs on those neighbors. Recolor \(v\) to \(c\), if needed; execute the sequence on \(F-v\); and finally recolor \(v\) to its target color, if needed. All moves are proper, and \(v\) changes at most twice. ∎

Apply this to \(G[X]\). The lifting lemma gives
\[
\operatorname{dist}_{R_7(G)}(\alpha,\beta)
\le b+r+2\sum_{x\in X}(1+d_Y(x))
=2a+b+2q+r.
\tag{4}
\]
For \(n\ge3\), rewrite the right-hand side as
\[
n+a+m+q-p.
\]
The planar inequalities above yield
\[
n+a+m+q-p
\le6n+a-p-10
\le7n-10.
\]
Again, \(n\le2\) is immediate. This proves the second assertion.

### List-coloring extension

Every choice made in these proofs avoids at most six specified colors. Hence the same arguments work when each vertex has its own list of at least seven colors.

There is no existence issue: under either structural hypothesis, \(G\) is \(5\)-degenerate. Indeed, any subgraph containing a vertex of \(Y\) has a vertex of degree at most five, while a subgraph lying entirely in \(X\) has one by the relevant hypothesis. Greedy coloring therefore supplies a coloring from lists of size at least seven.

## 5. Seven is necessary in these restricted classes

Both classes contain every planar graph of maximum degree at most five, including the icosahedron.

Give antipodal vertices of the icosahedron the same color, using six colors. Each vertex has precisely one neighbor in each of the other five color classes. Thus no vertex can change color, and this coloring is isolated in \(R_6(G)\).

The same construction also supplies the smaller-color obstructions: restricting the icosahedron to any \(k\) of these color classes gives a planar graph of maximum degree \(k-1\) with a frozen \(k\)-coloring, for \(2\le k\le6\). A nontrivial permutation of the used colors supplies a distinct coloring, so its reconfiguration graph is disconnected.

Together with the usual requirement that all graphs in the class be colorable, this makes seven the exact minimum for each restricted family in the theorem.

## 6. What prevents this from answering the original problem?

The high-degree subgraph here means the subgraph induced by vertices of **ambient degree at least six**, not the usual \(6\)-core.

Its structure need not satisfy either hypothesis. For example, let \(T_s\) be the triangular-lattice graph induced by a hexagonal ball of radius \(s\). Boundary vertices have degree three or four, and all other vertices have degree six. Therefore, for \(s\ge2\), its high-degree subgraph is \(T_{s-1}\). This graph has minimum degree three and maximum degree six. It satisfies neither condition above.

One can iterate the lifting lemma through successive degree-five removal layers, but that does not close the gap. If the remaining graph has a sequence changing each vertex at most \(C\) times, the extension argument gives only
\[
C\longmapsto5C+1
\]
as a uniform per-vertex bound. The number of removal layers is unbounded in planar graphs; it grows with \(s\) for the lattice patches \(T_s\). Thus this iteration supplies no universal linear bound.

**Conclusion.** The argument proves exact seven-color thresholds for explicit subclasses, including an extension to seven-list recoloring. It does not establish a linear bound for all planar graphs at seven, eight, or nine colors, nor exclude seven. The unrestricted problem remains at the supplied bounds
\[
\boxed{7\le\kappa\le10}.
\]