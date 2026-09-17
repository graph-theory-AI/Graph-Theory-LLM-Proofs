```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "Every sufficiently long uniform subdivision of an arbitrary connected graph admits a pivot Gray code, without assuming a code exists for the original graph.",
  "would_publish": false,
  "caveats": "The original conjecture remains open; the subdivision bound is not optimized, and literature novelty has not been checked."
}
```

# An unconditional result for sufficiently long subdivisions

I do not resolve the conjecture for arbitrary graphs. I prove an unconditional subdivision theorem: the base graph need not already admit a pivot Gray code.

The chamber decomposition suggested in the previous attempt is useful and is proved again below. The additional ingredients are Hamiltonian cycles with reserved edges inside even grids, Hamiltonian paths with reserved edges inside odd grids, and cycle splicing along a spanning tree.

Throughout, graphs are finite, connected, loopless, and simple. A **cyclic pivot Gray code** means a Hamiltonian cycle in the pivot flip graph, so it is stronger than the Hamiltonian path requested in the question.

## 1. Main result

Write
\[
d=\beta(H)=|E(H)|-|V(H)|+1.
\]
For positive integers \(\ell_e\), let \(H^\ell\) be obtained by replacing each edge \(e\) of \(H\) by an internally vertex-disjoint path of length \(\ell_e\).

### Theorem 1

Let \(H\) be a connected simple graph with \(d=\beta(H)\ge 2\), and suppose
\[
\ell_e\ge 2d+3\qquad(e\in E(H)).
\]
Put
\[
A=\{e\in E(H):\ell_e\text{ is even}\}.
\]
If either

1. \(A=\varnothing\), or
2. the subgraph with edge set \(A\) contains a cycle,

then \(H^\ell\) admits a cyclic pivot Gray code.

In particular, the hypotheses hold when all replacement lengths have the same parity.

### Corollary 2

Let \(H\) be any connected simple graph. For every integer
\[
L\ge 2\beta(H)+3,
\]
the graph obtained by replacing every edge of \(H\) by a path of length \(L\) admits a pivot Gray code. If \(H\) contains a cycle, the code can be cyclic.

The cases \(\beta(H)=0,1\) are elementary and are addressed at the end. The substantial assertion is for arbitrary \(H\) with \(\beta(H)\ge2\).

---

## 2. Chambers and their interfaces

Let \(\mathcal F(H)\) denote the pivot flip graph: its vertices are the spanning trees of \(H\), and
\[
S\sim S'
\quad\Longleftrightarrow\quad
S'=S-f+e
\]
for two edges \(e,f\) sharing an endpoint.

### Lemma 3: chamber decomposition

The spanning trees of \(H^\ell\) are uniquely described by:

- a spanning tree \(S\) of \(H\);
- one omitted edge of the replacement path \(P_e\), for every \(e\notin S\).

For \(e\in S\), all of \(P_e\) is present.

#### Proof

A connected spanning subgraph cannot omit two edges of one replacement path: the vertices between two consecutive omitted edges would be disconnected from both ends of the path.

Given a spanning tree of \(H^\ell\), let \(S\) consist of the base edges whose replacement paths are intact. The original vertices of \(H\) can be connected only through intact replacement paths, so \(S\) is connected. A cycle in \(S\) would lift to a cycle in the subdivided tree. Hence \(S\) is a spanning tree.

Conversely, an intact subdivision of a spanning tree \(S\), together with all but one edge of each remaining replacement path, is a spanning tree of \(H^\ell\). ∎

Choose an orientation of each replacement path solely to number its edges from \(1\) to \(\ell_e\). For a fixed \(S\), its **chamber** is therefore the rectangular grid
\[
Q_S=\mathop{\square}_{e\notin S} P_{\ell_e}.
\]
A coordinate records the position of the omitted edge. Changing a coordinate from \(j\) to \(j+1\) is a pivot, since it exchanges consecutive edges of one replacement path.

Every chamber has \(d\) coordinates.

### Interfaces

Suppose
\[
S'=S-f+e,
\]
where \(e,f\) share the base vertex \(v\). There is a matching between two chamber faces:

- in \(Q_S\), the omitted edge of \(P_e\) is its terminal edge at \(v\);
- in \(Q_{S'}\), the omitted edge of \(P_f\) is its terminal edge at \(v\);
- all coordinates indexed by
  \[
  (E(H)\setminus S)\cap(E(H)\setminus S')
  \]
  agree.

Each matching edge is a pivot: restore the terminal edge of \(P_e\) and delete the terminal edge of \(P_f\).

Consequently, a grid edge in a common coordinate, together with its corresponding grid edge on the other face, forms a \(4\)-cycle using two interface pivots. These \(4\)-cycles will be used for splicing.

---

## 3. The base flip graph and a splicing mechanism

### Lemma 4

If \(H\) is simple, then \(\mathcal F(H)\) is connected and \(2d\)-regular.

#### Proof

For a spanning tree \(S\) and an edge \(xy\notin S\), adding \(xy\) creates a fundamental cycle. A removed edge must lie on that cycle. To share an endpoint with \(xy\), it must be one of the two edges of the \(x\)-\(y\) path in \(S\) incident with \(x\) or \(y\). These are distinct because \(H\) is simple. Thus each of the \(d\) non-tree edges gives exactly two neighbors.

For connectivity, first recall the elementary exchange argument: unrestricted spanning-tree exchanges connect any two spanning trees. An unrestricted exchange \(S\mapsto S-f+e\) can be implemented by pivots inside the unicyclic graph \(S+e\): move the omitted edge from \(e\) to \(f\), one step at a time around its unique cycle. ∎

We use two standard, elementary splices.

- **Cycle–cycle splice.** Delete one edge from each of two disjoint cycles and join corresponding endpoints by two cross edges. The result is one cycle.
- **Path–cycle splice.** Make the same operation with a path and a disjoint cycle. The result is a path with the original path’s endpoints.

The deleted edges need not be vertex-disjoint from edges used in earlier splices. It is sufficient that each deleted edge is still present when used.

### Selected coordinate pairs

Fix a total order on \(E(H)\). For each chamber \(Q_S\), select the first two elements of \(E(H)\setminus S\).

If \(S,S'\) are adjacent in \(\mathcal F(H)\), their selected pairs intersect. Indeed, the least element of
\[
(E(H)\setminus S)\cap(E(H)\setminus S')
\]
belongs to both selected pairs: each non-tree set has only one element outside the intersection.

For a rectangular grid with two selected coordinates, call an edge a **selected side edge at level \(j\)** if:

- it changes one selected coordinate from \(j\) to \(j+1\);
- the other selected coordinate is at one of its two endpoints;
- the remaining coordinates are arbitrary.

Thus these are side edges in the two-dimensional layers determined by the selected pair.

### Lemma 5: reservoir splicing

Suppose the chambers have been grouped, and for each group there is one cycle covering exactly all vertices in its chambers. Suppose also that, in every chamber, this cycle contains all selected side edges at levels
\[
j_1,\ldots,j_K,
\]
where the levels are distinct.

Choose a spanning tree of the quotient of \(\mathcal F(H)\) obtained by contracting the groups, and choose a representative base flip for every quotient-tree edge. Let \(D\) be the graph of these representative flips on the spanning trees of \(H\).

If \(\Delta(D)\le K\), all the group cycles can be spliced into one Hamiltonian cycle of \(\mathcal F(H^\ell)\).

#### Proof

The representative edges form a forest: their images are distinct edges of a tree. Hence \(D\) has a proper edge coloring with \(K\) colors.

Consider a representative flip \(S'=S-f+e\), with exchanged edges meeting at \(v\), and give it color \(c\). Choose a coordinate \(h\) belonging to both selected pairs.

In the matching interface between \(Q_S\) and \(Q_{S'}\), choose the corresponding grid edges obtained by:

- changing coordinate \(h\) from \(j_c\) to \(j_c+1\);
- setting all other common coordinates to \(1\);
- setting coordinate \(e\), respectively \(f\), to its terminal position at \(v\).

These are selected side edges in both chambers. Indeed, the other selected coordinate is either the interface coordinate, at an endpoint, or a common coordinate set to \(1\).

The two chosen edges form opposite sides of an interface \(4\)-cycle. Use it for a cycle–cycle splice.

No chamber edge is selected twice. Edges selected in different coordinate directions are different; if the direction is the same, distinct incident colors give distinct levels.

Process the quotient-tree edges in any order. Each splice joins two cycles belonging to different components of the already processed forest, and every unused reserved edge remains present. At the end there is one cycle covering all vertices. ∎

---

## 4. Grid constructions with reserved side edges

The following grid facts supply the reservoirs required by Lemma 5.

A rectangular grid has a Hamiltonian path starting at any prescribed corner: traverse successive layers alternately forward and backward. We will use this elementary snake construction without further comment.

### Lemma 6: even rectangles

Let \(a,b\ge4\), with \(ab\) even. The grid \(P_a\square P_b\) has a Hamiltonian cycle containing every outer-boundary edge except possibly
\[
\{(a-2,1),(a-1,1)\}.
\]
Moreover, it has at least two cycle edges whose endpoints are both in the interior rectangle
\[
\{2,\ldots,a-1\}\times\{2,\ldots,b-1\}.
\]

#### Proof

A rectangular grid with both dimensions at least \(2\), and at least one even dimension, has a Hamiltonian cycle. For example, when \(a\) is even, reserve the row \(y=1\), snake through \(y=2,\ldots,b\) in successive columns, and return along the reserved row.

Apply this to the interior rectangle. Its dimensions are \(a-2,b-2\), so its order is even. Any Hamiltonian cycle in it contains
\[
\{(a-2,2),(a-1,2)\},
\]
because this edge is incident with an interior-rectangle corner.

Splice this interior cycle with the outer perimeter, using that edge and
\[
\{(a-2,1),(a-1,1)\}.
\]
Only the displayed outer-boundary edge is lost. At least three edges of the interior cycle remain, so two can be retained for later use. ∎

### Lemma 7: even grid chambers

Let \(Q\) be a rectangular grid with two selected coordinates of lengths \(a,b\). Suppose

- \(ab\) is even;
- \(a,b\ge K+3\).

Then \(Q\) has a Hamiltonian cycle containing every selected side edge at levels
\[
1,\ldots,K.
\]

#### Proof

In the selected two-dimensional rectangle, take the cycle from Lemma 6. Its omitted boundary edge has level \(a-2>K\), so all required side edges are present. Choose two distinct cycle edges \(p_0,p_1\) lying in its interior.

Use an identical copy of this cycle in every layer of the other coordinates. List those layers along a grid Hamiltonian path. Merge consecutive layer cycles, alternately using the corresponding copies of \(p_0\) and \(p_1\).

Each layer is involved in at most two merges, using different edges. All required side edges survive, and the result is one Hamiltonian cycle. ∎

The odd case needs paths with prescribed corner endpoints.

### Lemma 8: odd grid paths with a side-edge reservoir

Let
\[
Q=P_{a_1}\square\cdots\square P_{a_t},\qquad t\ge2,
\]
where all \(a_i\) are odd and at least \(7\). Select any two coordinates.

Between any two distinct corners of \(Q\), there is a Hamiltonian path containing every selected side edge whose level \(j\), in its changing coordinate of length \(a\), satisfies
\[
3\le j\le a-3.
\]

#### Proof

We first prove the two-dimensional assertion.

**Opposite corners.** Consider endpoints \((1,1)\) and \((a,b)\). Delete from the outer perimeter the two edges
\[
\{(1,1),(2,1)\},\qquad
\{(a-1,b),(a,b)\}.
\]
The remaining boundary consists of two paths, each containing one desired endpoint.

Connect their other endpoints through a Hamiltonian path of the interior rectangle, from \((a-1,b-1)\) to \((2,2)\). Such a path exists by the ordinary row snake, since both interior dimensions are odd. This gives the desired spanning path. Only two boundary edges next to corners are absent.

**Adjacent corners.** By symmetry take endpoints \((1,1)\) and \((a,1)\). Let \(P\) run from the first endpoint up the left side, across the top, and down the right side to the second endpoint.

The remaining vertices form the even rectangle
\[
R=\{2,\ldots,a-1\}\times\{1,\ldots,b-1\}.
\]
Use Lemma 6, reflected if necessary, to obtain a Hamiltonian cycle of \(R\) retaining its entire bottom boundary. Its upper-left corner edge
\[
\{(2,b-1),(3,b-1)\}
\]
is present. Splice this cycle into \(P\) using that edge and
\[
\{(2,b),(3,b)\}.
\]
On the original rectangle, the only missing boundary edges are the two bottom edges incident with the desired endpoints and the top edge at level \(2\).

Reflections and coordinate interchange show that every pair of distinct corners is covered, while every boundary edge at levels \(3,\ldots,a-3\), or \(3,\ldots,b-3\), is retained.

These two-dimensional paths also contain an edge with both endpoints in the interior: a vertex at distance at least two from the boundary has only interior neighbors.

Now induct on \(t\). Write the grid as a product of its selected rectangle and a grid \(Z\) of the remaining coordinates. Write the desired corners as
\[
(u,z),\qquad(v,w),
\]
where \(u,v\) are rectangle corners and \(z,w\) are corners of \(Z\).

If \(z\ne w\), use induction to find a Hamiltonian path
\[
z=z_1,\ldots,z_M=w
\]
in \(Z\); for one-dimensional \(Z\), use its ordinary path. Here \(M\ge3\).

Choose rectangle corners
\[
c_0=u,c_1,\ldots,c_M=v
\]
with consecutive corners distinct. This is always possible using the four rectangle corners: choose the intermediate corners successively, choosing the last intermediate corner different from both its predecessor and \(v\).

In layer \(z_i\), use the two-dimensional path from \(c_{i-1}\) to \(c_i\). Join successive layers at \(c_i\). All reserved side edges survive.

If \(z=w\), then \(u\ne v\). Take one of the two-dimensional paths \(L\) from \(u\) to \(v\), and choose an interior edge \(p\) of \(L\). List the layers by a Hamiltonian path
\[
z=z_1,z_2,\ldots,z_M.
\]
The number \(M\) is odd.

Keep \(L\) as a path in layer \(z_1\). Pair the other layers as
\[
(z_2,z_3),\ (z_4,z_5),\ \ldots.
\]
In each pair, two copies of \(L\), joined at their corresponding endpoints \(u\) and \(v\), form a cycle.

Attach these cycles successively to the initial path, using corresponding copies of \(p\) between layers
\[
(z_1,z_2),\ (z_3,z_4),\ldots.
\]
Each layer supplies \(p\) to at most one splice. The resulting Hamiltonian path has the required endpoints, and only interior rectangle edges were removed.

This proves the induction. ∎

---

## 5. Proof when the even-length base edges contain a cycle

Suppose \(A\) contains a cycle. Every spanning tree \(S\) omits at least one edge of \(A\). Thus every chamber has at least one even-length coordinate.

Order the base edges with all even-length edges first, and select the first two non-tree edges in each chamber. The selected rectangle has even order.

Set
\[
K=2d.
\]
The length hypothesis gives
\[
\ell_e\ge K+3.
\]
By Lemma 7, every chamber has a Hamiltonian cycle retaining all selected side edges at levels \(1,\ldots,K\).

Take a spanning tree of \(\mathcal F(H)\). Its maximum degree is at most \(2d=K\), by Lemma 4. Apply Lemma 5 with each chamber as a separate group.

This produces a Hamiltonian cycle of \(\mathcal F(H^\ell)\).

---

## 6. Compatible corners around a base cycle

For the all-odd case, individual chambers have odd order and cannot have grid Hamiltonian cycles. Instead, first group them along a cycle cover of the base flip graph.

The following lemma ensures that chamber Hamiltonian paths can be connected around any base cycle.

### Lemma 9: corner compatibility

Let
\[
S_1,S_2,\ldots,S_m,S_1
\]
be a simple cycle in \(\mathcal F(H)\), where \(d\ge2\), and suppose all replacement paths have length at least \(2\).

One can choose an entry corner and an exit corner in each \(Q_{S_i}\) such that:

1. the exit corner of \(Q_{S_i}\) and entry corner of \(Q_{S_{i+1}}\) are joined by the appropriate interface pivot;
2. the entry and exit corners of every chamber are distinct.

#### Proof

Encode each coordinate endpoint by a bit. Across an interface, the disappearing and appearing coordinates have prescribed endpoint bits, while all \(d-1\) common coordinates may be chosen freely.

Begin with any compatible choices. Call a chamber **bad** if its entry and exit corners agree.

Suppose first that \(d\ge3\). At a bad chamber \(i\), flip one common-coordinate bit on its outgoing interface. This changes the exit corner of \(i\) and the entry corner of \(i+1\), and makes chamber \(i\) good.

There are at least two available common coordinates. If chamber \(i+1\) is good and its entry and exit differ in exactly one coordinate, choose a different coordinate to flip. Then it stays good. If it has at least two differing coordinates, any one-coordinate flip keeps it good; if it is bad, the flip makes it good.

Thus the number of bad chambers decreases. Repeating finishes the construction.

It remains to handle \(d=2\). Let \(g_i\) be the unique coordinate common to chambers \(i\) and \(i+1\), and let \(t_i\) be its freely chosen interface bit.

At chamber \(i\), there are three possible forms of the distinctness constraint.

- If \(g_{i-1}=g_i\) and the other coordinate has different prescribed entry and exit bits, there is no constraint.
- If \(g_{i-1}=g_i\) and those prescribed bits agree, the constraint is
  \[
  t_{i-1}\ne t_i.
  \]
- If \(g_{i-1}\ne g_i\), exactly one of the four pairs \((t_{i-1},t_i)\) is forbidden.

Each of these relations has a nonempty row and a nonempty column for each bit value.

If there is an unconstrained chamber, break the cyclic system there and assign the bits successively. If there is a chamber forbidding exactly one pair, choose its first bit different from the forbidden first bit. Its constraint is then automatic, and assign the remaining bits backwards around the cycle.

The only potentially obstructed case is that every constraint is an inequality. Then every \(g_i\) is the same edge \(g\), and
\[
E(H)\setminus S_i=\{g,h_i\}.
\]
The graph \(H-g\) is connected and unicyclic. Its spanning trees are obtained by omitting one edge of its unique cycle, and its pivot flip graph is precisely that cycle.

Our simple cycle \(S_1,\ldots,S_m,S_1\) must therefore go once around this unicyclic flip graph. At each \(h_i\), the incoming and outgoing pivots use opposite endpoints of \(h_i\). Its prescribed entry and exit bits are consequently different, contradicting the assumption that every constraint was an inequality.

Hence the corner choices always exist. ∎

---

## 7. Proof for all-odd replacement lengths

Assume every \(\ell_e\) is odd.

### A cycle cover of the base flip graph

The connected \(2d\)-regular graph \(\mathcal F(H)\) has a spanning collection of vertex-disjoint cycles. Here is a self-contained justification.

Orient an Euler tour. Each vertex then has indegree and outdegree \(d\). Form the bipartite graph with left and right copies of the vertices, and an edge \(u_Lv_R\) for every oriented edge \(u\to v\). This bipartite graph is \(d\)-regular, so Hall’s condition follows by counting edges, and it has a perfect matching.

The selected arcs give indegree and outdegree one at every vertex. They therefore form directed cycles. There are no loops or directed \(2\)-cycles, since the original simple graph had each edge oriented in only one direction. Thus their underlying cycles form a \(2\)-factor.

### Lift each factor cycle

Fix any total order on \(E(H)\), and select the first two non-tree coordinates in each chamber.

For each cycle of the \(2\)-factor, use Lemma 9 to choose compatible, distinct entry and exit corners. By Lemma 8, traverse each chamber by a Hamiltonian path between those corners. Join them around the factor cycle using interface pivots.

We now have disjoint cycles covering all spanning trees of \(H^\ell\), with every chamber wholly contained in one cycle.

Set
\[
K=2d-2.
\]
Since
\[
\ell_e\ge 2d+3=K+5,
\]
Lemma 8 ensures that all selected side edges at the \(K\) levels
\[
3,4,\ldots,K+2
=
3,4,\ldots,2d
\]
are present in these cycles.

### Merge the lifted cycles

Contract the factor cycles in \(\mathcal F(H)\), choose a spanning tree of the resulting connected quotient, and choose representative flips for its edges.

At each base spanning tree, two incident flip edges belong to the \(2\)-factor. Therefore the representative connector graph has maximum degree at most
\[
2d-2=K.
\]

Apply Lemma 5 with color \(c\) assigned level \(c+2\). All lifted cycles merge into one Hamiltonian cycle of \(\mathcal F(H^\ell)\).

This finishes the proof of Theorem 1. ∎

---

## 8. Uniform subdivisions and the small cyclomatic cases

For a uniform replacement length \(L\):

- if \(L\) is odd, \(A=\varnothing\);
- if \(L\) is even, \(A=E(H)\), which contains a cycle whenever \(\beta(H)\ge1\).

Thus Theorem 1 proves Corollary 2 for \(\beta(H)\ge2\).

If \(\beta(H)=0\), every subdivision is a tree and has just one spanning tree.

If \(\beta(H)=1\), every subdivision is unicyclic. Every spanning tree is obtained by deleting one edge of its unique cycle; consecutive omitted edges around that cycle give a cyclic pivot Gray code.

For example, \(\beta(K_{3,3})=4\), so every uniform \(L\)-subdivision of \(K_{3,3}\) with \(L\ge11\) has a cyclic pivot Gray code. More importantly, the theorem applies to base graphs of arbitrary structure and arbitrary treewidth, without any prior Hamiltonicity assumption on their flip graphs.

## 9. What remains unresolved

The general conjecture is still not proved.

The construction uses long replacement paths to supply many reserved grid edges. There is no argument here that allows these subdivisions to be contracted while preserving a Hamiltonian path in the pivot flip graph.

Indeed, after the splices, projecting the resulting Hamiltonian cycle onto the base chambers generally revisits a base spanning tree many times. It does **not** produce a Hamiltonian path of \(\mathcal F(H)\).

The theorem also leaves untreated the general mixed-parity case in which the even-length base edges form a nonempty forest.

All arguments above are self-contained; no computational checks or unverified literature results are used. I have not checked whether this eventual-subdivision theorem, or a sharper version of it, already appears in the literature.