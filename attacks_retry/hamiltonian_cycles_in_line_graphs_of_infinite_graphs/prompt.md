Attack the following open graph-theory problem.

Catalog id: hamiltonian_cycles_in_line_graphs_of_infinite_graphs
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory » Infinite Graphs
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/hamiltonian_cycles_in_line_graphs_of_infinite_graphs/
Original entry: http://www.openproblemgarden.org/op/hamiltonian_cycles_in_line_graphs_of_infinite_graphs
Problem attributed to: Georgakopoulos, Agelos (posted 2007-07-24)

=== Problem statement (OpenProblemGarden) ===
Title: Hamiltonian cycles in line graphs of infinite graphs
Conjecture \item If $ G $ is a 4-edge-connected locally finite graph, then its line graph is hamiltonian. \item If the line graph $ L(G) $ of a locally finite graph $ G $ is 4-connected, then $ L(G) $ is hamiltonian.

=== Discussion / context (OpenProblemGarden) ===
(Reproduced from [M].) A locally finite graph is hamiltonian, if its Freudenthal compactification (also called the end compactification, see [D]) contains a hamilton circle, i.e. a homeomorphic copy of $ S^1 $ containing all vertices. The first part is known for finite graphs. The proof uses the existence of two edge-disjoint spanning trees in 4-edge-connected graphs. In the infinite case, it would be enough to prove that a 4-edge-connected locally finite graph $ G $ has two edge-disjoint topological spanning trees (see [D]), one of which is connected as a subgraph of $ G $ . The problem is open even for the 1-ended case (where hamilton circles correspond to 2-way-infinite paths). The second part is widely open even in the finite case, where it was proposed by Thomassen [T].

=== References listed by OpenProblemGarden ===
- [D] Reinhard Diestel, Graph Theory, Third Edition, Springer, 2005.
- *[G] A. Georgakopoulos, Oberwolfach reports, 2007.
- [M] Bojan Mohar, Problem of the Month
- [T] Carsten Thomassen, Reflections on graph theory, J. Graph Theory 10 (1986) 309-324, MathSciNet

=== Catalog page (statement + literature review) ===
Hamiltonian cycles in line graphs of infinite graphs — Graph-theory open problems

 
 Status
 partial
 medium confidence
 

 The conjecture has seen partial progress on Part 1: Florian Lehner proved (arXiv:1109.6787, JCTB 2014) that the line graph of every locally finite, highly edge-connected graph (≥6-edge-connected, in the sense of the end-faithful spanning tree packing result) has a Hamiltonian circle, extending the classical finite result; this is a weakening of the 4-edge-connected threshold asked in the conjecture. Part 2 (4-connected line graph implies Hamiltonian) remains widely open even for finite graphs, and Part 1 in its full 4-edge-connected form is still open.

 Cited literature (2)

 
 
 
partial On spanning tree packings of highly edge connected graphs
 (2014)
 

 
 Florian Lehner · Journal of Combinatorial Theory, Series B · arXiv:1109.6787

Extends the Tutte/Nash-Williams tree-packing theorem to end-faithful packings in certain locally finite graphs, establishing that the line graph of every locally finite, sufficiently highly edge-connected graph has a Hamiltonian circle (a partial result toward the 4-edge-connected conjecture).
 

 
 
partial Extending Cycles Locally to Hamilton Cycles
 (2016)
 

 
 Matthias Hamann, Florian Lehner, Julian Pott · Electronic Journal of Combinatorics

Proves that every connected, locally connected, locally finite, claw-free graph has a Hamilton circle; since line graphs are claw-free, this has implications for Hamiltonicity of line graphs of locally finite graphs with sufficient edge-connectivity.
 

 

 Reviewer notes. PDFs at florian-lehner.net and math.uni-hamburg.de were not text-readable via WebFetch, so exact theorem statements could not be directly verified. The claim that the Lehner 2014 paper covers the '6-edge-connected' case is consistently reported in secondary sources (including Mohar's problem page and search result abstracts) but could not be confirmed by reading the theorem directly. The Hamann-Lehner-Pott 2016 paper's abstract emphasizes claw-free locally connected graphs rather than mentioning line graphs explicitly; a corollary for line graphs may follow but was not directly verified. Both conjectures (4-edge-connected and 4-connected line graph) appear to remain open as of the search date.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 07) (web search enabled).
 

Conjecture. \item If $ G $ is a 4-edge-connected locally finite graph, then its line graph is hamiltonian. \item If the line graph $ L(G) $ of a locally finite graph $ G $ is 4-connected, then $ L(G) $ is hamiltonian.

Keywords:
hamiltonian · infinite graph · line graphs

Discussion

(Reproduced from [M].) A locally finite graph is hamiltonian, if its Freudenthal compactification (also called the end compactification, see [D]) contains a hamilton circle, i.e. a homeomorphic copy of $ S^1 $ containing all vertices. The first part is known for finite graphs. The proof uses the existence of two edge-disjoint spanning trees in 4-edge-connected graphs. In the infinite case, it would be enough to prove that a 4-edge-connected locally finite graph $ G $ has two edge-disjoint topological spanning trees (see [D]), one of which is connected as a subgraph of $ G $ . The problem is open even for the 1-ended case (where hamilton circles correspond to 2-way-infinite paths). The second part is widely open even in the finite case, where it was proposed by Thomassen [T].

Bibliography

 [D]
 Reinhard Diestel, Graph Theory, Third Edition, Springer, 2005.

★ [G]
 A. Georgakopoulos, Oberwolfach reports, 2007.

 [M]
 Bojan Mohar, Problem of the Month
 Problem of the Month

 [T]
 Carsten Thomassen, Reflections on graph theory, J. Graph Theory 10 (1986) 309-324, MathSciNet
 MathSciNet

Related conjectures

 
 implies
 Hamiltonian cycles in line graphs
 partial
 Item 2 of the source asserts: for every locally finite graph G with L(G) 4-connected, L(G) has a Hamilton circle in its Freudenthal compactification. Finite graphs are locally finite and the compactification of a finite graph adds no ends, so a Hamilton circle there is exactly a Hamilton cycle; thus item 2 restricted to finite graphs is verbatim Thomassen's conjecture (every 4-connected line graph is hamiltonian). Truth of the source (a conjunction including item 2) therefore forces the target. The source's own context confirms: 'The second part is widely open even in the finite case, where it was proposed by Thomassen [T].' Direction as claimed is correct: infinite version is the stronger statement.
 

 View in the relation graph
 — relations are AI-reviewed, not formally verified.

========================================================================

=== A PREVIOUS, UNVERIFIED ATTEMPT ===
The problem above was already attacked by `gpt-6-astra`, which reported verdict `partial` at high confidence. That attempt is reproduced below.

Treat it as a lead, not as an authority: it is unverified, it may be wrong in ways neither model noticed, and its framing may be the reason it stalled. Check anything you reuse, and say so if you discard it. Your task is the original problem, not a critique of this attempt. If you can finish what it started, do that; if a different route is better, take it.

--- previous attempt ---
```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "Rigorous special cases include one-ended even-degree graphs and exact-4-edge-connected tree products, but neither full conjecture is settled.",
  "would_publish": false,
  "caveats": "Special-case deductions only; novelty and an updated literature status are not claimed."
}
```

# Partial results

I do not prove or disprove either conjecture. I establish two special cases:

1. **One-ended even-degree graphs:** If \(G\) is connected, locally finite, one-ended, and every vertex has even degree, then \(L(G)\) has a Hamilton circle. No edge-connectivity assumption is needed here.
2. **Tree-amalgams of finite pieces:** A finite-piece condition, stated below, guarantees a Hamilton circle in \(L(G)\). In particular,
   \[
   L(T\square K_4)
   \]
   has a Hamilton circle for every locally finite infinite tree \(T\). Each \(T\square K_4\) is exactly \(4\)-edge-connected.

The second result allows arbitrary end spaces arising from locally finite trees. When \(T\) is a ray, it also gives a one-ended example in which all but four vertices have odd degree, so it is not subsumed by the first result.

All graphs in the arguments below are simple.

## 1. The one-ended even-degree case

### Theorem 1
Let \(X\) be a connected, locally finite, one-ended graph in which every vertex has even degree. Then \(X\) has an Euler double trail: a two-way-infinite walk that traverses every edge exactly once. Consequently, \(L(X)\) has a Hamilton circle.

The relevant issue is not merely producing finite Euler tours, but arranging them so that their limit is a single double trail.

### Lemma 1.1: finite Eulerian completion

Every finite set of edges of \(X\) is contained in a finite connected even subgraph \(Y\). Moreover, \(Y\) can be chosen so that all edges of \(X-E(Y)\) belong to a single infinite component.

#### Proof

Enlarge the prescribed edge set to a finite connected subgraph \(P\). Let
\[
O=\{v:d_P(v)\text{ is odd}\}.
\]
The set \(O\) is finite and has even cardinality.

Deleting \(E(P)\) leaves exactly one infinite component. For every finite component \(C\) of \(X-E(P)\),
\[
|O\cap V(C)|
 \equiv \sum_{v\in V(C)}d_P(v)
 \equiv |\delta_X(V(C))|
 \equiv 0 \pmod 2.
\]
The last congruence follows because \(C\) is finite and all degrees in \(X\) are even. It follows, using \(|O|\equiv0\pmod2\), that the infinite component also contains an even number of vertices of \(O\).

Within each component, pair its vertices of \(O\) and choose finite paths joining the pairs. The symmetric difference \(J\) of these paths is a finite edge set, disjoint from \(E(P)\), whose odd-degree vertex set is \(O\). Thus \(P\cup J\) is even. Retain the component containing \(P\), obtaining a finite connected even subgraph \(Y\).

The graph \(X-E(Y)\) is again even and has exactly one infinite component. It has only finitely many components, since only finitely many edges were deleted. Add to \(Y\) all finite components having at least one edge. Each is even and meets \(V(Y)\), by connectedness of \(X\). This preserves finiteness, connectedness, and even degrees, and leaves just one component containing all remaining edges. ∎

### Construction of the Euler double trail

Enumerate \(E(X)\). We construct finite connected even subgraphs
\[
H_0\subseteq H_1\subseteq H_2\subseteq\cdots
\]
and closed Euler trails \(P_n\) of \(H_n\), such that \(P_n\) is a contiguous subwalk of \(P_{n+1}\), with a nonempty extension at both ends.

Start with a single vertex \(x_0\), no edges, and the length-zero walk \(P_0\). Maintain the following properties:

- all edges outside \(H_n\) belong to one infinite connected even graph \(R_n\);
- \(x_n\in V(H_n)\cap V(R_n)\);
- \(P_n\) starts and ends at \(x_n\).

At stage \(n\), apply Lemma 1.1 inside \(R_n\) to obtain a finite connected even subgraph \(K_{n+1}\) containing:

- every edge of \(R_n\) incident with \(V(H_n)\);
- the first edge in the enumeration not already in \(H_n\).

Choose it with a single infinite residual edge-containing component \(R_{n+1}\), and put
\[
H_{n+1}=H_n\cup K_{n+1}.
\]
The two edge sets are disjoint.

By connectedness of \(X\), \(H_{n+1}\) and \(R_{n+1}\) share a vertex \(x_{n+1}\). Since all residual edges incident with \(V(H_n)\) were put into \(K_{n+1}\),
\[
x_{n+1}\notin V(H_n).
\]
In particular, \(x_{n+1}\ne x_n\), and both vertices belong to \(K_{n+1}\).

Take an Euler circuit of \(K_{n+1}\), starting at \(x_{n+1}\), and split it at an occurrence of \(x_n\):
\[
A_n:x_{n+1}\longrightarrow x_n,
\qquad
B_n:x_n\longrightarrow x_{n+1}.
\]
Both walks are nonempty. Define
\[
P_{n+1}=A_nP_nB_n.
\]
This is a closed Euler trail of \(H_{n+1}\) with the required extension property.

The limit is a two-way-infinite edge sequence. Every edge occurs exactly once: there are no repetitions at any finite stage, and the enumeration condition ensures eventual inclusion of every edge.

Its edge sequence is therefore a spanning double ray in \(L(X)\). Also, \(L(X)\) has exactly one end: deleting finitely many vertices of \(L(X)\) corresponds to deleting finitely many edges of \(X\). Both tails of the spanning double ray converge to this end. Adding that end gives a homeomorphic copy of \(S^1\), containing every vertex of \(L(X)\). ∎

Thus Part 1 holds, in particular, for its **one-ended even-degree subclass**, including the one-ended \(4\)-regular case.

---

## 2. A tree-amalgamation theorem

Here is a different mechanism, accommodating odd degrees and arbitrarily many ends.

### Theorem 2
Let \(G\) be a locally finite graph with a partition
\[
V(G)=\bigsqcup_{t\in V(T)}V_t,
\]
where \(T\) is a locally finite infinite tree. Suppose:

1. every \(V_t\) is finite and has at least two vertices;
2. every edge of \(G\) is either internal to a bag \(V_t\), or joins bags indexed by adjacent vertices of \(T\);
3. for each \(tu\in E(T)\), at least two edges join \(V_t\) to \(V_u\);
4. every \(G[V_t]\) contains two edge-disjoint spanning trees.

Then \(L(G)\) has a Hamilton circle.

### 2.1. Constructing an even spanning scaffold

For each \(tu\in E(T)\), choose two edges between \(V_t\) and \(V_u\). Let \(P\) be the union of these selected edges.

For each bag, choose edge-disjoint spanning trees \(A_t,B_t\) of \(G[V_t]\), and set
\[
O_t=\{v\in V_t:d_{A_t}(v)+d_P(v)\text{ is odd}\}.
\]
This set has even cardinality, because
\[
\sum_{v\in V_t}\bigl(d_{A_t}(v)+d_P(v)\bigr)
   =2(|V_t|-1)+2d_T(t).
\]

There is an \(O_t\)-join \(J_t\subseteq E(B_t)\): its odd-degree vertex set is exactly \(O_t\). Explicitly, root \(B_t\), and include an edge precisely when the component below it contains an odd number of vertices of \(O_t\).

Define
\[
H=P\;\cup\;\bigcup_{t\in V(T)}(A_t\cup J_t).
\]
Then:

- \(H[V_t]\) is connected and spans \(V_t\);
- every vertex of \(H\) has even degree;
- exactly two edges of \(H\) join \(V_t\) and \(V_u\) for every \(tu\in E(T)\);
- \(H\) is connected and spans \(G\).

We next turn this scaffold into a Hamilton circle in \(L(G)\), including the edges of \(G\) outside \(H\).

### 2.2. Finite local circuits

For a bag \(V_t\), form a finite auxiliary multigraph \(M_t\):

- retain \(H[V_t]\);
- for every neighbor \(u\) of \(t\), introduce a dummy vertex \(z_{tu}\);
- replace the two selected \(V_t\)-\(V_u\) edges by two stubs joining their endpoints in \(V_t\) to \(z_{tu}\).

Original vertices have the same degrees as in \(H\), and every dummy vertex has degree two. Thus \(M_t\) is connected and even, and has an Euler circuit.

Label every edge of \(M_t\) by the corresponding edge of \(G\). The Euler circuit gives a cyclic list of distinct labels. Consecutive labels correspond to adjacent vertices of \(L(G)\), except possibly at a dummy vertex. At \(z_{tu}\), the two selected crossing-edge labels are consecutive; mark this adjacency **virtual**.

Now incorporate \(E(G)\setminus E(H)\). Assign each such edge to one of its endpoints \(v\), and hence to the bag containing \(v\). Each bag receives finitely many assignments. At an Euler-circuit transition through \(v\), insert all edge labels assigned to \(v\). Every new consecutive pair shares \(v\), so these are genuine adjacencies in \(L(G)\).

The resulting finite abstract cycle \(C_t\) has these properties:

- all its nonvirtual edges are edges of \(L(G)\);
- its virtual edges are pairwise vertex-disjoint;
- for each \(tu\in E(T)\), the cycles \(C_t,C_u\) share exactly the two selected crossing-edge labels, which are the endpoints of their corresponding virtual edges;
- every other label belongs to exactly one local cycle.

### 2.3. Gluing the circuits, including at ends

For each \(tu\in E(T)\), delete the corresponding virtual edges in \(C_t,C_u\), identifying equally labelled endpoints.

Over a finite subtree, this operation produces one cycle: attaching a new local cycle simply replaces a virtual edge by the complementary path around that local cycle.

Over the whole tree, it produces a spanning \(2\)-regular subgraph \(Q\) of \(L(G)\). **Degree two alone is not enough** to conclude that its closure is a circle. We therefore verify the topology directly.

Root \(T\). Glue the cycles belonging to the first \(n\) levels, leaving virtual edges toward unprocessed children. This gives a finite cycle \(D_n\). Real edges, once introduced, are never changed.

Parametrize \(D_0\) by \(S^1\). Whenever a virtual edge is replaced by a path, subdivide its parameter interval into positive-length intervals for the new path edges. Do this so that every new virtual interval has at most half the length of its parent interval. This is possible because a replacement path has at least two edges.

Furthermore, each new virtual interval lies strictly inside its parent interval: the virtual edges in a local cycle have disjoint endpoints.

Consequently:

- every real edge of \(Q\) receives a fixed nondegenerate parameter interval;
- every vertex of \(Q\) appears at a finite stage;
- every remaining parameter point is specified by a nested sequence of virtual intervals, and hence by a ray of \(T\);
- these intervals have diameters tending to zero, so each end of \(T\) corresponds to exactly one remaining parameter point.

The ends of \(L(G)\) are naturally identified with those of \(T\). Indeed, the bags are finite and connected, and edges occur only within bags or between adjacent bags. Deleting the finitely many edges incident with a finite collection of bags separates the corresponding components of the remaining tree. These separators give the required end-neighborhood basis.

Map the remaining parameter point for an end of \(T\) to the corresponding end of \(L(G)\). Together with the parametrizations of real edges, this defines a bijection
\[
f:S^1\longrightarrow Q\cup\Omega(L(G)).
\]

Continuity at ordinary edge points and vertices follows from the finite-stage construction. For continuity at an end, take a prescribed finite vertex set of \(L(G)\). A sufficiently deep descendant subtree uses none of these vertices, nor edges incident with their bags, and lies in the appropriate end component. The corresponding virtual interval is therefore mapped into the desired end neighborhood.

Thus \(f\) is continuous. Since \(S^1\) is compact and the Freudenthal compactification is Hausdorff, \(f\) is a homeomorphism onto its image. Every edge label of \(G\), and hence every vertex of \(L(G)\), appears in that image. This proves Theorem 2. ∎

---

## 3. Consequences at connectivity four

### 3.1. Finite \(4\)-edge-connected pieces

Suppose the bags in Theorem 2 induce finite \(4\)-edge-connected graphs, and at least four edges join each pair of adjacent bags. Then \(G\) is \(4\)-edge-connected and \(L(G)\) has a Hamilton circle.

For the spanning-tree hypothesis, use the standard finite spanning-tree-packing theorem. For a partition of a finite \(4\)-edge-connected graph into \(r\ge2\) nonempty parts, the number of crossing edges is at least
\[
\frac{4r}{2}\ge 2(r-1),
\]
so two edge-disjoint spanning trees exist.

To verify global \(4\)-edge-connectivity, consider a nontrivial vertex bipartition of \(G\). If it splits a bag, that bag contributes at least four crossing edges. Otherwise it is a union-of-bags bipartition, and some edge of the connected tree \(T\) has its endpoint bags on opposite sides, again contributing at least four edges.

This gives a subclass of Part 1 with arbitrary tree-like end structure.

### 3.2. An explicit natural family: \(T\square K_4\)

### Corollary 3
For every locally finite infinite tree \(T\),
\[
G=T\square K_4
\]
is exactly \(4\)-edge-connected, and \(L(G)\) has a Hamilton circle.

#### Hamiltonicity

Use the \(K_4\)-fibres as bags. Between adjacent fibres there are four matching edges. The two paths
\[
1-2-3-4
\qquad\text{and}\qquad
3-1-4-2
\]
are edge-disjoint spanning trees of \(K_4\). Theorem 2 applies.

#### Edge-connectivity

Let \(S\) be a nonempty proper subset of \(V(G)\).

- If no fibre is split by \(S\), some tree edge has its two fibres on opposite sides, giving four cut edges.
- If at least two fibres are split, each split \(K_4\) contributes at least three internal cut edges.
- Suppose exactly one fibre is split, with \(k\) of its vertices in \(S\). Its internal contribution is
  \[
  k(4-k).
  \]
  This is four when \(k=2\). When \(k=1\) or \(3\), it is three; a neighboring, unsplit fibre contributes at least one further matching edge.

Thus every nontrivial cut has size at least four. Conversely, deleting the four matching edges corresponding to any edge of \(T\) disconnects \(G\). Hence its edge-connectivity is exactly four. ∎

If \(T\) is a ray, vertices in its initial fibre have degree four and all other vertices have degree five. Thus this one-ended case has infinitely many odd-degree vertices and genuinely uses the second construction.

### 3.3. Consequences for Part 2

For an infinite \(4\)-edge-connected graph \(G\), its line graph is \(4\)-connected: deleting at most three vertices of \(L(G)\) amounts to deleting at most three edges of \(G\), and the remaining line graph is connected. Thus the preceding families satisfy both hypotheses in the question.

There is also a simple extension whose underlying graphs need not be \(4\)-edge-connected. Start with \(G_0=T\square K_4\), and attach finitely many pendant edges at each vertex, maintaining local finiteness. Call the resulting graph \(G\).

Then:

- **\(L(G)\) is \(4\)-connected.** After deleting at most three edge-labels, the surviving core \(G_0\) is connected. Every surviving pendant edge is adjacent in the line graph to a surviving core edge at its attachment vertex, since its core degree is at least four.
- **\(L(G)\) has a Hamilton circle.** Insert each pendant-edge label at a local Euler transition through its attachment vertex in the construction above. There are only finitely many such insertions in each bag, and pendant attachments introduce no new ends.

This supplies a special case of Part 2 in which the root graph can have bridges.

---

## 4. What remains unproved

The two proofs use additional structure not supplied by the conjectured hypotheses.

- Theorem 1 relies essentially on even degrees. Its finite Eulerian-completion argument does not furnish the needed parity correction for a general \(4\)-edge-connected one-ended graph.
- Theorem 2 requires finite pieces with substantial internal connectivity. Global \(4\)-edge-connectivity does not imply this condition. For example, a finite induced subgraph of the square grid on \(n\ge2\) vertices has at most \(2n-3\) edges, fewer than the \(2n-2\) needed for two edge-disjoint spanning trees.
- In the tree-amalgamation proof, the two designated crossing edges at each tree cut provide explicit control at every end. No analogous end-control construction has been established here for an arbitrary \(4\)-edge-connected graph.
- Nothing in these arguments proves that an arbitrary finite \(4\)-connected line graph is Hamiltonian.

Accordingly, these are rigorous special-case deductions, not a resolution of either conjecture. Their novelty is not asserted.
