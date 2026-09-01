```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The full complexity classification remains unresolved here, but proper-subdivision instances collapse exactly to cactus graphs, and both problems admit exact algorithms parameterized by natural deletion sets to the known polynomial subclasses.",
  "would_publish": false,
  "caveats": "No polynomial algorithm or NP-hardness reduction is obtained for either full class; the catalog's logarithmic-treewidth remark also requires verification."
}
```

# 1. Statement and conventions

Let

\[
\mathcal E_4=\{G:\ G\text{ has no even hole and no }K_4\}
\]

and

\[
\mathcal T_3=\{G:\ G\text{ has no induced theta and no triangle}\}.
\]

The question is whether Maximum Independent Set is polynomial-time solvable or NP-hard on either of these hereditary classes. I treat the problem as the unweighted, promised-input problem.

I do not obtain a complete classification. The main rigorous progress below is:

1. an exact characterization of all proper-subdivision instances in either class;
2. an explanation of why the standard subdivision reduction for Independent Set cannot establish hardness here;
3. local restrictions on how vertices attach to holes;
4. exact parameterized algorithms reducing the two questions to the known polynomial case of (even-hole, triangle)-free graphs;
5. clarification of the claimed \(O(\log n)\)-treewidth consequence.

# 2. Preliminary parity observation

## Lemma 2.1

Every even-hole-free graph is theta-free.

### Proof

Let an induced theta have branch vertices \(a,b\) and three internally vertex-disjoint induced \(a\)-\(b\) paths \(P_1,P_2,P_3\), each of length at least two, with no additional edges between the paths.

For every \(i\ne j\), \(P_i\cup P_j\) is a hole of length

\[
|E(P_i)|+|E(P_j)|.
\]

Among the three path lengths, two have the same parity. Their sum is even, and it is at least four. Thus the corresponding two paths induce an even hole, a contradiction. ∎

Consequently, the difference between the two target classes is not the presence of induced thetas in \(\mathcal E_4\): those are already excluded. Rather, \(\mathcal E_4\) permits triangles but excludes all even holes, while \(\mathcal T_3\) permits even holes but excludes triangles.

The classes are incomparable:

- \(C_4\in\mathcal T_3\setminus\mathcal E_4\).
- The wheel \(W_5\), consisting of a \(C_5\) and a universal center, belongs to \(\mathcal E_4\) but not to \(\mathcal T_3\). Indeed, its only hole is the rim \(C_5\), and its clique number is three.

# 3. Proper subdivisions collapse to cacti

A graph is a **proper subdivision** of a simple graph \(H\) if every edge of \(H\) is replaced by a path of length at least two, with all replacement paths internally vertex-disjoint.

Recall that a cactus is a graph every block of which is an edge or a cycle.

## Theorem 3.1

Let \(G\) be a proper subdivision of a simple graph \(H\).

1. \(G\) is theta-free if and only if \(H\) is a cactus.
2. \(G\) is even-hole-free if and only if \(H\) is a cactus and every cycle of \(H\), after subdivision, has odd total length.

In particular:

- \(G\in\mathcal T_3\) if and only if \(H\) is a cactus;
- \(G\in\mathcal E_4\) if and only if \(H\) is a cactus and every subdivided cycle has odd length.

### Proof

First observe that every proper subdivision is triangle-free, and hence also \(K_4\)-free.

Suppose that \(H\) is not a cactus. Then some 2-connected block \(B\) of \(H\) is neither an edge nor a cycle. Such a block contains three internally vertex-disjoint paths between a pair of vertices, where the paths are allowed to have length one in \(H\). One way to see this is to choose a cycle \(C\) in \(B\):

- if \(C\) has a chord, the chord and the two arcs of \(C\) give the three paths;
- otherwise, if \(C\) does not contain all of \(B\), 2-connectivity gives a \(C\)-path through \(B-V(C)\), which together with the two arcs of \(C\) gives the three paths.

Expand these paths in the proper subdivision \(G\). Every resulting path has length at least two. Moreover, extra edges of \(H\) do not become chords in the selected induced subgraph of \(G\): every unused edge of \(H\) was itself subdivided, and its internal vertices are absent. Thus the expanded three paths induce a theta in \(G\).

Therefore, if \(G\) is theta-free, \(H\) is a cactus.

Conversely, if \(H\) is a cactus, then its subdivision \(G\) is also a cactus. A theta is 2-connected and is not a cycle, so it cannot occur in a cactus, even as a non-induced subgraph. This proves part 1.

For part 2, even-hole-freeness implies theta-freeness by Lemma 2.1, so \(H\) must first be a cactus. In a subdivision of a cactus, every cycle is precisely the subdivision of one cycle block of \(H\), and it is induced. Hence \(G\) is even-hole-free exactly when all these subdivided cycles have odd length. ∎

## Corollary 3.2

Maximum Weight Independent Set, and hence Maximum Independent Set, is solvable in linear time on the proper-subdivision instances belonging to either target class.

### Justification

By Theorem 3.1, such a graph is a cactus and therefore has treewidth at most two. More directly, its block-cutvertex tree supports a two-state dynamic program at each cutvertex; within a cycle block, the required conditional stable-set values are obtained by the usual path recurrence.

This is a genuine structural special case, but it does not cover graphs such as wheels or the cube.

# 4. Why the standard subdivision hardness reduction fails

A common reduction to sparse triangle-free graphs replaces each edge \(uv\) by

\[
u-x_{uv}-y_{uv}-v.
\]

Let \(S_2(H)\) denote this two-subdivision of \(H\), and let \(m=|E(H)|\).

## Proposition 4.1

\[
\alpha(S_2(H))=m+\alpha(H).
\]

### Proof

Fix the set \(S\subseteq V(H)\) of original vertices chosen in an independent set of \(S_2(H)\). For an edge \(uv\):

- if at most one of \(u,v\) lies in \(S\), one of \(x_{uv},y_{uv}\) can be chosen;
- if both \(u,v\) lie in \(S\), neither internal vertex can be chosen.

Thus the best extension of \(S\) has size

\[
m+|S|-e_H(S),
\]

where \(e_H(S)\) is the number of edges with both ends in \(S\).

If \(S\) is not independent, remove a vertex \(v\) incident with an edge of \(H[S]\). The quantity \(|S|-e_H(S)\) changes by

\[
-1+d_{H[S]}(v)\ge 0.
\]

Repeating this produces an independent set without decreasing the quantity. Hence

\[
\max_{S\subseteq V(H)}\bigl(|S|-e_H(S)\bigr)=\alpha(H),
\]

which proves the formula. ∎

More generally, if each edge is subdivided \(2r\) times, so that its replacement path has length \(2r+1\), then

\[
\alpha(S_{2r}(H))=r|E(H)|+\alpha(H).
\]

This is normally an effective way to transfer NP-hardness to sparse triangle-free graphs. Theorem 3.1 shows exactly why it fails here:

- \(S_{2r}(H)\) is theta-free only when \(H\) is a cactus;
- it is even-hole-free only when \(H\) is a cactus and every expanded cycle is odd.

Maximum Independent Set is already easy on such \(H\). Thus no reduction based solely on replacing each edge independently by a nontrivial path can prove hardness for either target class. Any successful hardness construction must add unsubdivided chord-like interactions that destroy every induced topological theta or even cycle while preserving the optimization encoding.

# 5. Attachments to holes

The following elementary restrictions isolate the wheel-like configurations that are not handled by the subdivision argument.

## Lemma 5.1

Let \(G\in\mathcal T_3\), let \(C\) be a hole, and let \(x\notin V(C)\). Then

\[
|N_C(x)|\ne 2.
\]

Moreover, if \(|N_C(x)|\ge 3\), then \(N_C(x)\) is a stable subset of \(C\).

### Proof

If \(N_C(x)=\{u,v\}\), triangle-freeness implies that \(u,v\) are nonadjacent. The path \(u-x-v\) and the two \(u\)-\(v\) arcs of \(C\) then form an induced theta. This is impossible.

The second assertion follows immediately from triangle-freeness: two consecutive vertices of \(C\) together with \(x\) would induce a triangle. ∎

Thus a vertex outside a hole has zero, one, or at least three neighbors on it. The last possibility is a proper wheel and is the first serious obstruction to a cactus-like decomposition.

## Lemma 5.2

Let \(G\) be even-hole-free, let \(C\) be a hole, and let \(x\notin V(C)\).

1. The hole \(C\) is odd.
2. If \(x\) has exactly two neighbors on \(C\), then those two neighbors are adjacent.
3. List at least two neighbors of \(x\) cyclically around \(C\). Every sector between consecutive \(x\)-neighbors which has length at least two has odd length.

### Proof

The first assertion is the definition of even-hole-free.

For the second, suppose \(N_C(x)=\{u,v\}\) with \(u,v\) nonadjacent. The two \(u\)-\(v\) arcs of \(C\) have opposite parity because \(C\) is odd. Adding the two edges through \(x\) gives two induced cycles, one of which is even and has length at least four, a contradiction.

For the third, let \(Q\) be a sector of length \(q\ge2\) between consecutive \(x\)-neighbors \(u,v\). Since no internal vertex of \(Q\) is adjacent to \(x\), \(G[V(Q)\cup\{x\}]\) is a hole of length \(q+2\). It must be odd, so \(q\) is odd. ∎

For example, a \(C_9\) with a center adjacent to three rim vertices at cyclic distance three is triangle-free, \(K_4\)-free, and even-hole-free. Its three sectors have length three. Such odd-sector wheels show why merely analyzing vertices with at most two hole attachments will not settle either problem.

# 6. Exact algorithms from deletion to the known polynomial subclass

The prompt supplies polynomial algorithms for (even-hole, triangle)-free graphs. This gives the following general reduction.

## Lemma 6.1: Modulator enumeration

Let \(X\subseteq V(G)\) be such that \(G-X\) belongs to a hereditary class on which MIS is polynomial. Then MIS on \(G\) can be solved using at most \(2^{|X|}\) calls to that polynomial algorithm.

### Proof

Enumerate every independent set \(S\subseteq X\). Force \(S\) into the solution and solve MIS on

\[
G-X-N_G(S).
\]

This graph is an induced subgraph of \(G-X\). The candidate value is

\[
|S|+\alpha\bigl(G-X-N_G(S)\bigr).
\]

Every independent set \(I\) of \(G\) appears in the case \(S=I\cap X\), so taking the maximum is exact. ∎

## Corollary 6.2: Triangle-transversal parameter for \(\mathcal E_4\)

MIS on \(\mathcal E_4\) is fixed-parameter tractable parameterized by

\[
\tau_\triangle(G)=\min\{|X|:G-X\text{ is triangle-free}\}.
\]

Given \(k\), a triangle transversal of size at most \(k\), if one exists, can be found in \(O(3^k n^{O(1)})\) time: find a triangle and branch on deleting each of its three vertices. Once \(X\) is found, Lemma 6.1 gives runtime

\[
O\!\left(3^k n^{O(1)}+2^k n^{O(1)}\right).
\]

Indeed, \(G-X\) is both even-hole-free and triangle-free.

Equivalently, if a greedy maximal family of \(p\) vertex-disjoint triangles is used, the union of those triangles is a transversal of size \(3p\), giving an \(8^p n^{O(1)}\) exact algorithm.

This does not settle the full problem: \(\tau_\triangle\) can be linear even on connected chordal \(K_4\)-free graphs, for instance chains of triangles joined by bridges.

## Corollary 6.3: Even-hole transversal for \(\mathcal T_3\)

If \(G\in\mathcal T_3\) and an even-hole transversal \(X\) is supplied, then MIS is solvable in

\[
2^{|X|}n^{O(1)}
\]

time. After deleting \(X\), the graph is (even-hole, triangle)-free.

Finding such a transversal is more problematic because an even hole can have unbounded length. The direct branching algorithm has unbounded branching factor. For the restricted subclass in which every even hole has length at most a fixed \(L\), the same argument gives an \(L^k n^{O(L)}\) search for a transversal of size \(k\), followed by the \(2^k\) enumeration.

# 7. The logarithmic-treewidth issue

The catalog review says that an \(O(\log n)\) treewidth bound for \(\mathcal T_3\) “yields only quasi-polynomial MIS.” Taken literally, this inference is incorrect.

Given a tree decomposition of width \(w\), MIS is solvable by the standard bag-subset dynamic program in

\[
O(2^w n^{O(1)})
\]

time. Therefore, a constructible bound

\[
\operatorname{tw}(G)\le c\log n
\]

would give a polynomial-time algorithm, namely \(n^{c+O(1)}\).

However, the supplied abstract does not state such a global logarithmic bound for all of \(\mathcal T_3\); it states bounded treewidth only after additionally excluding a fixed \(S_{i,j,k}\). Thus I do not use the catalog sentence as a theorem. It may refer to another width parameter, include an omitted multiplicative parameter, or simply be an inaccurate review summary. The exact theorem in the source would have to be checked before drawing an algorithmic conclusion.

# 8. Limits of the partial results

The proper-subdivision theorem cannot be extended naively to all of \(\mathcal T_3\). For example, the 3-dimensional cube \(Q_3\) is triangle-free and theta-free but has minimum degree three and is not a cactus.

To verify theta-freeness, possible nonadjacent branch vertices have distance two or three:

- At distance two, the two common neighbors are forced to be two length-two theta paths. Every possible third path has a cross-edge to one of these common neighbors.
- For opposite vertices, deleting the branch vertices leaves a \(C_6\). Three internally disjoint paths would have to select a perfect matching of that \(C_6\), while the complementary matching supplies forbidden cross-edges.

Thus even quite small cubic configurations can use chords to destroy all induced thetas.

The unresolved cases are consequently concentrated around such chorded topological structures:

- proper wheels and nested wheel attachments in \(\mathcal T_3\);
- triangles and odd pyramidal/wheel structures in \(\mathcal E_4\).

I have neither a decomposition showing that these structures support polynomial MIS nor a gadget construction proving NP-hardness. Therefore the original two complexity questions remain open in this writeup.