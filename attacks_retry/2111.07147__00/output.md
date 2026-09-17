```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "For a fixed number q of witness faces, I prove the explicit weak-diameter bound 6q(2r+1)-1, which has optimal order in r, but I do not settle the unrestricted conjecture.",
  "would_publish": false,
  "caveats": "The bound depends on q; the case of unboundedly many witness faces remains unresolved here, and novelty of the quantitative special case has not been assessed."
}
```

# 1. Main partial result

All graphs below are finite and simple, except that intermediate planar contractions and dual graphs may have loops or parallel edges. Distance from a vertex to a face means distance to its incident vertex set.

For \(X\subseteq V(G)\), put
\[
\operatorname{wdiam}_G(X)=\max_{x,y\in X}\operatorname{dist}_G(x,y).
\]

I obtain the following quantitative strengthening of the bounded-number-of-faces case from the previous attempt.

## Theorem 1

Let \(r\ge 0\) and \(q\ge 1\). Suppose a plane graph \(G\) has faces \(F_1,\dots,F_q\) such that every vertex is at distance at most \(r\) from at least one \(F_i\). Then \(G\) has a 2-coloring whose monochromatic components have weak diameter at most
\[
\boxed{6q(2r+1)-1.}
\]

Neither the absence of separating triangles nor a restriction on the lengths of the witness faces is needed.

In particular, the one-witness-face case has the explicit bound
\[
D\le 12r+5.
\]
Section 3 gives examples with exactly one non-triangular face requiring weak diameter at least \(2r+1\). Thus the dependence on \(r\) in Theorem 1 is optimal up to a constant factor for every fixed \(q\).

The proof below is self-contained and does not use the bounded-treewidth/asymptotic-dimension result invoked in the previous attempt. I also verify and strengthen its dual approach: the dual-forest restriction can be imposed without loss of generality.

# 2. Proof of the quantitative upper bound

The main elementary ingredient is a BFS coloring lemma.

## Lemma 2: excluding \(K_{2,t}\)

For every \(t\ge 3\), every graph with no \(K_{2,t}\) minor has a 2-coloring of weak diameter at most
\[
3t-4.
\]

### Proof

Work in a connected graph \(H\), choose a root \(z\), and let
\[
L_i=\{v:\operatorname{dist}_H(z,v)=i\}.
\]
Color each vertex by the parity of its level.

Every edge joins vertices in the same or consecutive levels. Consequently, every monochromatic component is a component of some \(H[L_i]\).

Let \(C\) be a component of \(H[L_i]\), where \(i\ge 2\), and define its shadow
\[
S=N_H(C)\cap L_{i-1}.
\]
The ball
\[
B=L_0\cup\cdots\cup L_{i-2}
\]
is connected. Every vertex of \(S\) has a neighbor in \(B\) and a neighbor in \(C\). Contracting \(B\) and \(C\) separately, and retaining the vertices of \(S\), produces a \(K_{2,|S|}\) minor. Therefore
\[
1\le |S|\le t-1. \tag{2.1}
\]

Every vertex of \(C\) has a neighbor in \(S\). Form an auxiliary graph \(Q\) on \(S\), joining distinct \(a,b\in S\) if some \(x\in N_H(a)\cap C\) and \(y\in N_H(b)\cap C\) satisfy either \(x=y\) or \(xy\in E(H)\). Each edge of \(Q\) corresponds to a path of length at most three in \(H\).

The graph \(Q\) is connected. Indeed, choose for each vertex of \(C\) one neighbor in \(S\). A path in \(C\) gives a walk between its chosen neighbors in \(Q\); any vertex of \(S\) not chosen in this way is adjacent in \(Q\) to a chosen neighbor of one of its neighbors in \(C\).

It follows that, for \(x,y\in C\),
\[
\operatorname{dist}_H(x,y)
 \le 1+3(|S|-1)+1
 =3|S|-1
 \le 3t-4.
\]
A component in \(L_1\) has weak diameter at most two, via \(z\), and \(L_0\) is a singleton. This proves the lemma. ∎

We next record how a bounded face cover gives the required excluded minor.

## Lemma 3: domination by external planar vertices

Suppose \(H\) is a subgraph of a planar graph \(A\), and
\[
V(A)=V(H)\mathbin{\dot\cup}X,\qquad |X|\le q,
\]
where every vertex of \(H\) has a neighbor in \(X\). Then \(H\) has no \(K_{2,2q+1}\) minor.

### Proof

Suppose there were such a minor, with connected, pairwise disjoint branch sets
\[
U,\ W,\ Z_1,\dots,Z_{2q+1},
\]
where each \(Z_i\) is adjacent to both \(U\) and \(W\).

Each \(Z_i\) has a neighbor in \(X\). By the pigeonhole principle, some \(x\in X\) has neighbors in three distinct sets \(Z_i,Z_j,Z_k\). Contracting these five branch sets in \(A\) produces a \(K_{3,3}\) subgraph with bipartition
\[
\{U,W,x\},\qquad \{Z_i,Z_j,Z_k\}.
\]
This contradicts planarity. ∎

## Proof of Theorem 1

We may assume that \(G\) is connected. For a disconnected graph, apply the argument separately to each component: each original witness face is contained in a face of the component, so at most \(q\) witness faces still suffice. Their lengths are irrelevant here.

Let
\[
S=\bigcup_{i=1}^q V(F_i).
\]
Choose a spanning forest rooted at \(S\) by giving every vertex outside \(S\) a parent whose distance to \(S\) is one smaller. Every tree of this forest has exactly one root in \(S\), and every vertex is at tree-distance at most \(r\) from its root.

Contract each tree to a single vertex, and suppress loops and parallel edges. Call the resulting graph \(H\). Each contraction fiber has diameter at most \(2r\) using paths entirely within that fiber in the original graph \(G\).

For each \(i\), add a vertex \(x_i\) inside \(F_i\), adjacent to every vertex incident with \(F_i\). This standard facial augmentation is planar; repeated boundary occurrences can temporarily give parallel edges, which may be discarded. Perform the same forest contractions, without contracting any \(x_i\).

The resulting planar graph consists of \(H\) together with at most \(q\) additional vertices \(x_i\). Every vertex of \(H\) has a neighbor among the \(x_i\), since its contraction fiber contains a root in \(S\). Lemma 3 therefore implies that \(H\) has no \(K_{2,2q+1}\) minor.

By Lemma 2, \(H\) has a 2-coloring of weak diameter at most
\[
3(2q+1)-4=6q-1.
\]
Give every vertex of \(G\) the color of its contraction fiber.

Let \(u,v\) lie in one monochromatic component of \(G\). Their images lie in one monochromatic component of \(H\), so there is an \(H\)-path between their images of length
\[
d\le 6q-1.
\]
This path need not be monochromatic, which is permissible for weak diameter.

Lift the path to \(G\). Each of its \(d\) edges costs one edge of \(G\), and travel within each of its \(d+1\) fibers costs at most \(2r\). Hence
\[
\begin{aligned}
\operatorname{dist}_G(u,v)
&\le d+2r(d+1)\\
&\le (6q-1)(2r+1)+2r\\
&=6q(2r+1)-1.
\end{aligned}
\]
Crucially, no metric shortcut through an added face vertex is used in this estimate. All lifted paths are in \(G\). ∎

# 3. Linear lower bounds already with one non-triangular face

Let \(T_n\) have vertex set
\[
\{0,1,\dots,n\}^2,
\]
with horizontal and vertical grid edges and, in every unit square, the diagonal
\[
(i,j)(i+1,j+1).
\]

All bounded faces are triangles, and the outer face has length \(4n\). Every 3-cycle is one of the two triangles in a unit square, so there is no separating triangle.

Every vertex \((i,j)\) is at distance at most
\[
\min\{i,j,n-i,n-j\}\le \lfloor n/2\rfloor
\]
from the outer face. Thus
\[
T_{2r+1}\in\mathcal G_r,
\]
with exactly one non-triangular face.

The Hex lemma for a triangulated rectangle says that every red-blue coloring has either a red left-to-right path or a blue bottom-to-top path. One way to see this is to trace the boundary of the red vertices reachable from the left side. If that set misses the right side, its separating boundary yields a blue top-to-bottom walk: consecutive blue vertices encountered along the boundary are equal or adjacent because every interior face is triangular.

Every edge of \(T_n\) changes each coordinate by at most one. Therefore, endpoints of a left-to-right or bottom-to-top path have graph distance at least \(n\). Consequently,
\[
\boxed{D(r)\ge 2r+1} \tag{3.1}
\]
for any bound answering the original question.

There is also a small improvement at \(r=0\):
\[
D(0)\ge 2.
\]
Take the outerplane fan \(K_1\vee P_7\). It belongs to \(\mathcal G_0\). If the universal vertex is red in a weak-diameter-one coloring, all red path vertices must be pairwise adjacent. There are therefore at most two of them, and if there are two they are consecutive. Deleting them leaves a blue interval of at least three vertices, whose first and last vertices are not adjacent—a contradiction.

Thus any prospective uniform bound must satisfy
\[
D(r)\ge \max\{2,2r+1\}.
\]

# 4. The dual-forest formulation is exact

Here is a correction to the unresolved caveat in the previous attempt. Requiring a dual forest does **not** lose generality.

Let \(G\) be connected and plane, and let
\[
T=\{f\in V(G^*): |f|\text{ is odd}\}.
\]
A \(T\)-join is an edge set \(J\subseteq E(G^*)\) whose odd-degree vertices are exactly \(T\), with loops counted twice in degrees.

## Proposition 4

For an integer \(D\ge 0\), the following are equivalent.

1. \(G\) has a 2-coloring of weak diameter at most \(D\).
2. There is a \(T\)-join \(J\) such that every component of the primal edge set
   \[
   M=\{e\in E(G):e^*\in J\}
   \]
   has weak diameter at most \(D\).
3. Such a \(T\)-join \(J\) exists and is a forest.

### Proof

**\(1\Rightarrow2\).** Let \(M\) be the monochromatic edges of the coloring. Around each facial boundary walk, the number of color changes is even. Therefore
\[
\deg_{M^*}(f)\equiv |f|\pmod 2,
\]
so \(M^*\) is a \(T\)-join. Components of the spanning graph \((V(G),M)\) are precisely the monochromatic components.

**\(2\Rightarrow1\).** Put \(B=E(G)\setminus M\). The \(T\)-join condition says that every facial boundary walk contains an even number of occurrences of edges in \(B\).

By summing facial boundaries modulo two inside a cycle, every cycle contains an even number of edges of \(B\). Consequently, the parity of the number of \(B\)-edges on a root-to-vertex path is well-defined. Use that parity as the vertex color.

An edge is bichromatic exactly when it belongs to \(B\), and monochromatic exactly when it belongs to \(M\). The component bound follows.

**\(2\Rightarrow3\).** If \(J\) contains a cycle, delete all edges of that cycle. This preserves every degree parity, hence preserves the \(T\)-join condition. Repeat until a forest remains.

The crossed primal edge set only shrinks. Its components are therefore contained in the old components and retain their weak-diameter bound. ∎

In particular, the previous attempt's condition

> “a dual forest whose components contain even numbers of odd faces, with bounded-diameter crossed primal components”

is exact as an **existence formulation**. Indeed, such a forest contains a \(T\)-join: root each tree and select a parent edge precisely when its descendant subtree contains an odd number of vertices of \(T\).

This removes the forest caveat, but does not yet construct the required forest.

# 5. What the two hypotheses supply in the dual

The original hypotheses give two useful, rigorous structural facts.

## Lemma 5: non-triangular faces cannot be separated by three dual edges

Let \(G\) have no separating triangle. Any two distinct faces of length at least four are joined in \(G^*\) by four edge-disjoint paths.

### Proof

Suppose a dual edge cut of size at most three separates the two faces. Choose a minimal such cut; it is a bond. Its primal dual is a cycle of length at most three.

Since \(G\) is simple, this must be a triangle. It has a non-triangular face on each side, so neither side can be an empty triangular disk. Thus the triangle has vertices on both sides and is separating, a contradiction.

The conclusion follows from the edge version of Menger's theorem. ∎

## Lemma 6: local access to a non-triangular face

If \(G\in\mathcal G_r\), then every triangular face can be joined to a non-triangular face by a dual path whose crossed primal edges have their entire endpoint set of weak diameter at most
\[
r+2.
\]

### Proof

Let \(f\) be a triangular face and choose \(v\in V(f)\). There is a path \(P\) of length at most \(r\) from \(v\) to a vertex incident with a non-triangular face \(h\).

For any vertex \(u\), the duals of edges incident with \(u\) connect all faces incident with \(u\): they trace the cyclic order around \(u\). For consecutive vertices of \(P\), these connected dual subgraphs intersect. Their union therefore contains a dual \(f\)-\(h\) path.

Every crossed primal edge has an endpoint on \(P\). Hence any two endpoints of crossed edges are at distance at most
\[
1+|P|+1\le r+2
\]
in \(G\). ∎

Thus the hypotheses give both:

- four-edge connectivity between the non-triangular dual vertices; and
- access from every triangular dual vertex to one of them using a primal-small set of crossed edges.

These facts are stronger than merely knowing that non-triangular faces exist.

# 6. Remaining gap

The complete quantitative result is
\[
D\le 6q(2r+1)-1
\]
when \(q\) witness faces suffice. For fixed \(q\), its linear dependence on \(r\) is necessary.

However, \(q\) is unbounded in \(\mathcal G_r\), including in \(\mathcal G_0\). The theorem therefore does not answer the question.

The exact dual formulation isolates the missing construction: one needs a \(T\)-join forest whose crossed primal edges have components of weak diameter bounded solely by \(r\).

Lemmas 5 and 6 do not provide that global control. Although each individual access path crosses a primal set of diameter at most \(r+2\), crossed edges from many such paths can concatenate into an arbitrarily long primal component. Acyclicity in the dual does not prevent this primal concatenation. Odd non-triangular faces must also satisfy the \(T\)-join parity requirements.

I do not have a construction overcoming this obstruction, nor a counterexample to the original conjecture.