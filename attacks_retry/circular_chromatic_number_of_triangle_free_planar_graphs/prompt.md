Attack the following open graph-theory problem.

Catalog id: circular_chromatic_number_of_triangle_free_planar_graphs
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory » Coloring » Vertex coloring
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/circular_chromatic_number_of_triangle_free_planar_graphs/
Original entry: http://www.openproblemgarden.org/op/circular_chromatic_number_of_triangle_free_planar_graphs
Problem attributed to: Ghebleh, Mohammad, Zhu, Xuding (posted 2007-06-20)

=== Problem statement (OpenProblemGarden) ===
Title: Circular coloring triangle-free subcubic planar graphs
Problem Does every triangle-free planar graph of maximum degree three have circular chromatic number at most $ \frac{20}{7} $ ?

=== Discussion / context (OpenProblemGarden) ===
Throughout, we let $ \chi_c(G) $ denote the circular chromatic number of the graph $ G $ . A well-known Question of Nesetril asks if $ \chi_c(G) \le \frac{5}{2} $ for all cubic graphs $ G $ of sufficiently high girth. A conjecture of Jaeger asserts that $ \chi_c(G) \le 2 + \frac{1}{k} $ for every planar graph $ G $ of girth $ 4k+1 $ . There are numerous partial results on these problems, and there are many interesting questions concerning the circular chromatic numbers of restricted families of graphs. Here we are restricted to planar graphs of girth $ \ge 4 $ with maximum degree $ \le 3 $ . The dodecahedron lives in this class and has $ \chi_c = \frac{20}{7} $ . It remains unclear if anyone else in this class might have $ \chi_c $ larger. A related conjecture of X. Zhu asserts that for every triangle-free planar graph $ G $ with $ \Delta(G)\le 4 $ and $ |V(G)|<3k $ one has $ \chi_c(G)\le 3-1/k $ .

=== Catalog page (statement + literature review) ===
Circular coloring triangle-free subcubic planar graphs — Graph-theory open problems

 
 Status
 open
 medium confidence
 

 The problem of whether every triangle-free planar graph of maximum degree three satisfies $\chi_c(G) \leq 20/7$ remains open as of all accessible literature. The bound is tight: the dodecahedron belongs to this class and achieves $\chi_c = 20/7$. No proof or counterexample was found in the literature reachable by web search and verified fetch.

 Reviewer notes. Zhu's personal open-problems status page (math.nsysu.edu.tw/~zhu/open-problems/status.htm and chic-k3free-planar.htm) returned TLS certificate errors and could not be fetched; it may contain updates. The OPG page itself was also unreachable (ECONNREFUSED). The paper arXiv:2204.12683 (Dvořák et al., 2022/2025) establishes $\chi_f(G) \leq 11/4$ for subcubic triangle-free graphs (up to two exceptions including the Petersen graph; the dodecahedron likely being a second exception with $\chi_f = \chi_c = 20/7$), but this concerns the fractional chromatic number — a different and weaker parameter since $\chi_f \leq \chi_c$ — and does not resolve the circular coloring question. No arXiv papers combining all three key terms (circular chromatic, triangle-free, planar, subcubic/degree-3) were returned by any search.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (web search enabled) · 232s.
 

Problem. Does every triangle-free planar graph of maximum degree three have circular chromatic number at most $ \frac{20}{7} $ ?

Keywords:
circular coloring · planar graph · triangle free

Discussion

Throughout, we let $ \chi_c(G) $ denote the circular chromatic number of the graph $ G $ . A well-known Question of Nesetril asks if $ \chi_c(G) \le \frac{5}{2} $ for all cubic graphs $ G $ of sufficiently high girth. A conjecture of Jaeger asserts that $ \chi_c(G) \le 2 + \frac{1}{k} $ for every planar graph $ G $ of girth $ 4k+1 $ . There are numerous partial results on these problems, and there are many interesting questions concerning the circular chromatic numbers of restricted families of graphs. Here we are restricted to planar graphs of girth $ \ge 4 $ with maximum degree $ \le 3 $ . The dodecahedron lives in this class and has $ \chi_c = \frac{20}{7} $ . It remains unclear if anyone else in this class might have $ \chi_c $ larger. A related conjecture of X. Zhu asserts that for every triangle-free planar graph $ G $ with $ \Delta(G)\le 4 $ and $ |V(G)|<3k $ one has $ \chi_c(G)\le 3-1/k $ .

========================================================================

=== A PREVIOUS, UNVERIFIED ATTEMPT ===
The problem above was already attacked by `gpt-6-astra`, which reported verdict `partial` at high confidence. That attempt is reproduced below.

Treat it as a lead, not as an authority: it is unverified, it may be wrong in ways neither model noticed, and its framing may be the reason it stalled. Check anything you reuse, and say so if you discard it. Your task is the original problem, not a critique of this attempt. If you can finish what it started, do that; if a different route is better, take it.

--- previous attempt ---
```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I prove a sharp 8/3 bound when the degree-three vertices induce a matching, but do not resolve the full 20/7 conjecture.",
  "would_publish": false,
  "caveats": "The genuinely cubic case is not covered; novelty of the special case has not been checked."
}
```

## A sharp special case

The full conjecture is not settled below. The partial result is the following.

**Theorem.** Let \(G\) be a finite simple triangle-free planar graph of maximum degree at most three. Suppose that every degree-three vertex has at most one degree-three neighbor. Then
\[
\chi_c(G)\le \frac83<\frac{20}{7}.
\]
The bound \(8/3\) is sharp under these hypotheses.

Thus the additional hypothesis is that the subgraph induced by the degree-three vertices is a matching together with isolated vertices. The proof is constructive and self-contained.

An **\((8,3)\)-coloring** is a map \(f:V(G)\to\mathbb Z_8\) such that
\[
f(v)-f(u)\in\{3,4,5\}\pmod 8
\qquad(uv\in E(G)).
\]
Such a coloring certifies \(\chi_c(G)\le 8/3\).

### 1. Extension along paths

Let \(R_\ell\subseteq\mathbb Z_8\) be the possible differences between the endpoint colors of an \((8,3)\)-colored path of length \(\ell\). Taking sums of elements of \(\{3,4,5\}\) gives
\[
\begin{array}{c|c}
\ell &R_\ell\\ \hline
1&\{3,4,5\}\\
2&\{0,1,2,6,7\}\\
3&\mathbb Z_8\setminus\{0\}\\
\ell\ge4&\mathbb Z_8 .
\end{array}
\tag{1}
\]
For the last row, four steps already give every residue, and adding another step preserves this property.

Consequently:

* a two-edge path can be filled precisely when its endpoint colors have cyclic distance at most two;
* a three-edge path can be filled precisely when its endpoint colors are distinct;
* a path of length at least four can be filled with arbitrary endpoint colors.

Call the first of these endpoint relations \(T\), and the second \(U\).

### 2. An elementary four-state constraint lemma

We first prove the auxiliary result that will supply most of the coloring.

**Lemma.** Let \(Q\) be a connected loopless planar multigraph of maximum degree at most four, counting multiplicities. Label each edge \(e\) by \(\sigma_e\in\mathbb Z_2\). At each vertex choose a state
\[
(a_v,b_v)\in\mathbb Z_2^2,
\]
subject to the condition that an edge \(uv\) forbids
\[
a_u=a_v
\quad\text{and}\quad
b_u+b_v=\sigma_{uv}.
\tag{2}
\]
Delete repeated copies of parallel edges having the same label. A valid state assignment exists unless the resulting multigraph is an odd cycle with two parallel edges, one of each label, between each consecutive pair of vertices.

**Proof.** Each edge forbids exactly one of the four states at one endpoint once the other endpoint is assigned.

If some vertex has degree at most three, root a spanning tree there and assign states in reverse tree order. Every nonroot vertex has an unassigned parent and hence at most three incident constraints from assigned vertices. The root has at most three constraints altogether.

We may therefore assume that the simplified multigraph is 4-regular. If it has a cutvertex \(v\), each piece consisting of \(v\) and a component of \(Q-v\) has degree at most three at \(v\), so the preceding greedy argument colors each piece. The transformations
\[
(a,b)\longmapsto(a+\alpha,b+\beta),
\qquad \alpha,\beta\in\mathbb Z_2,
\]
preserve all constraints and act transitively on the four states. Thus the piece colorings can be made to agree at \(v\).

It remains to consider the case in which the underlying simple graph \(H\) is 2-connected. Each pair of vertices has at most two edges between it.

If \(H\) is a cycle, 4-regularity forces every edge to be doubled with both labels. Such a pair of edges requires different \(a\)-coordinates. Hence an even cycle is colorable, and an odd cycle is the stated obstruction.

If \(H\) is complete, planarity and the degree bound leave only \(K_4\), apart from cases already covered. The doubled edges of \(Q\) then form a perfect matching of \(K_4\). Give their endpoints different \(a\)-coordinates, with two vertices in each \(a\)-class. Within each class only one single edge remains, and its constraint can be satisfied by choosing the \(b\)-coordinates.

For the remaining case, use the following ordering fact.

> **Ordering fact.** If a 2-connected simple graph \(H\) is neither complete nor a cycle, there are nonadjacent vertices \(x,z\) with a common neighbor \(y\) such that \(H-\{x,z\}\) is connected.

Here is a proof. Suppose first that some vertex \(y\) of degree at least three has \(H-y\) not 2-connected. Choose two endblocks of \(H-y\). By 2-connectivity of \(H\), each contains a neighbor of \(y\) other than its attachment cutvertex; call these neighbors \(x,z\). They are nonadjacent, deleting them leaves \(H-y\) connected, and a third neighbor of \(y\) remains. Thus \(H-\{x,z\}\) is connected.

Otherwise, deleting any vertex of degree at least three leaves a 2-connected graph. Such a vertex cannot have a degree-two neighbor, since that neighbor would become a leaf after deletion. Because \(H\) is connected and is not a cycle, it follows that every vertex has degree at least three. Take any induced path \(x,y,z\). Then \(H-x\) is 2-connected, so \(H-\{x,z\}\) is connected. This proves the fact.

Apply the ordering fact to \(H\). Preassign states to \(x,z\) so that one constraint from \(xy\) and one from \(zy\) forbid the same state at \(y\). This is possible because an edge constraint is a perfect matching between the four states, and \(x,z\) are nonadjacent.

Now root a spanning tree of \(H-\{x,z\}\) at \(y\) and color in reverse tree order. Every vertex other than \(y\) has at most three constraints from already assigned vertices. At \(y\), two of its four incident constraints forbid the same state, so again at most three states are forbidden. This completes the assignment. \(\square\)

### 3. Encoding the graph by four-state constraints

Delete vertices of degree at most one repeatedly. Any coloring of what remains extends back, since every color has a neighbor in the \((8,3)\)-target. The hypothesis on degree-three vertices is preserved.

A component with no degree-three vertex is a cycle of length at least four, and is colorable by (1). Consider another component.

Call its degree-three vertices **branch vertices**. Its edges decompose into maximal paths with internal vertices of degree two, which we call **threads**. The threads of length one form a matching \(M\), by hypothesis.

Contract each edge of \(M\). A resulting vertex represents either:

* one branch vertex, with at most three thread incidences; or
* a matched pair of branch vertices, with at most four remaining thread incidences.

For a matched pair distinguish its two vertices as ports \(r=0,1\). A singleton has just port \(r=0\). Given a state \((a,b)\in\mathbb Z_2^2\), assign port \(r\) the color
\[
2a+4(b+r)\pmod8.
\tag{3}
\]
The two ports of a matched pair differ by four, so their edge is properly colored.

Ignore threads of length at least four. A length-two or length-three thread becomes, respectively, a \(T\)-edge or a \(U\)-edge between the corresponding vertices.

There are no \(T\)-loops: such a loop would come from a length-two thread joining the ends of an edge of \(M\), creating a triangle. A \(U\)-loop joins the two ports of one matched pair, whose colors differ by four, so its constraint is automatically satisfied and it can be discarded. Threads beginning and ending at the same branch vertex have length at least four and have already been ignored.

This gives a loopless planar multigraph \(Q\) of maximum degree at most four.

For an edge joining ports \(r_i,r_j\), substitution in (3) gives exactly the constraint (2), with
\[
\sigma_e=
\begin{cases}
1+r_i+r_j,&e\text{ has type }T,\\
r_i+r_j,&e\text{ has type }U,
\end{cases}
\pmod2.
\tag{4}
\]
Indeed, different \(a\)-coordinates give endpoint colors at cyclic distance two, satisfying both relations. Equal \(a\)-coordinates give equal or antipodal colors: \(T\) permits equality and forbids antipodality, while \(U\) does the reverse.

The lemma therefore handles every component except a possible odd doubled cycle. It remains to repair precisely this obstruction.

### 4. Repairing an odd doubled cycle

Suppose the simplified constraint graph has an exceptional component
\[
C_m,\qquad m\text{ odd},
\]
with two oppositely labelled edges between each consecutive pair.

Every vertex has degree four. Since the graph before simplification also had maximum degree four, no constraint incident with this component was discarded as a duplicate. Moreover, every vertex represents a matched pair, and all four available thread incidences are present.

Refer to the matched pairs as **columns**, cyclically ordered. Each column has two ports and two thread incidences at each port.

For column \(i\), put \(d_i=0\) if its two threads toward the previous column meet the same port, and \(d_i=1\) if they meet different ports. Its two threads toward the next column have the same incidence type, since each port has exactly two available incidences.

For two consecutive columns, equations (4) and the opposite edge labels imply
\[
\begin{cases}
\text{the two threads have different types},&d_i=d_{i+1},\\
\text{the two threads have the same type},&d_i\ne d_{i+1}.
\end{cases}
\tag{5}
\]
In particular, not all threads have type \(T\): otherwise the \(d_i\)'s would alternate around an odd cycle.

Choose a column \(i\) incident with a \(U\)-thread. On the remaining path of columns, alternate phases \(a=0,1\). Its two ends—column \(i\)'s neighbors—then have opposite phases. Write
\[
P_0=\{0,4\},\qquad P_1=\{2,6\}.
\]
Every ordinary column in phase \(a\) receives the two colors of \(P_a\), in either order. Threads between different phases satisfy both \(T\) and \(U\), independently of these orders.

Thus the port orders at the two neighbors of column \(i\) may be chosen independently. We will color column \(i\), allowing its two colors to differ by three rather than insisting on four.

#### Case A: \(d_i=0\)

Both left threads meet one port, of color \(x\), and both right threads meet the other, of color \(y\). Give the left neighbor phase zero and the right neighbor phase one.

For a neighbor in phase \(a\), the possibilities prescribed by (5) are:
\[
\begin{array}{c|c|c}
\text{neighbor incidence}&\text{thread types}
&\text{allowed color at the port of column }i\\ \hline
\text{same port}&T,U&\mathbb Z_8\setminus P_a\\
\text{different ports}&T,T&P_{1-a}\\
\text{different ports}&U,U&\mathbb Z_8\setminus P_a .
\end{array}
\tag{6}
\]
These follow directly from the two sets \(P_a\). For example, the colors within cyclic distance two of both members of \(P_a\) are precisely \(P_{1-a}\).

At least one side contains a \(U\)-thread.

* If the left side contains \(U\), take \((x,y)=(1,4)\).
* Otherwise the left side is \(T,T\) and the right contains \(U\); take \((x,y)=(2,5)\).

Both choices satisfy (6), and the two port colors differ by three.

#### Case B: \(d_i=1\)

Each side meets both ports of column \(i\).

If neither side consists of two \(T\)-threads, use port colors \(1,5\). A side consisting of two \(U\)-threads is satisfied because the neighbor's colors are even. For a mixed \(T,U\) side, choose the neighbor's port order to satisfy the \(T\)-thread; its other, even color is automatically different from the odd color at the \(U\)-thread's endpoint.

Otherwise one side consists of two \(T\)-threads. The other side contains \(U\), because column \(i\) was chosen incident with \(U\). By shifting all colors by two if necessary, assume the \(T,T\) neighbor has phase zero.

Use port colors \(\{2,5\}\). Both are within cyclic distance two of \(4\), so the \(T,T\) side is satisfied by assigning color \(4\) to the appropriate port of its neighbor.

The other neighbor has phase one:

* if its two threads are \(U,U\), use color \(6\) at their common port;
* if they are mixed \(T,U\), put color \(2\) at column \(i\)'s \(T\)-port, and assign colors \(2,6\) to the corresponding ports of the neighboring column.

Again all constraints hold, and the two colors at column \(i\) differ by three.

This covers every exceptional component. Finally, fill all threads using (1), and restore the deleted degree-at-most-one vertices. The theorem follows. \(\square\)

## Sharpness

Start with \(K_4\) on vertices \(a,b,c,d\). Retain the matching edges \(ab,cd\), and subdivide each of
\[
ac,\ ad,\ bc,\ bd
\]
once. Call the resulting graph \(F\).

It is planar, triangle-free, and subcubic. Its degree-three vertices induce exactly the matching \(\{ab,cd\}\).

An explicit \((8,3)\)-coloring gives \(a,b,c,d\) colors
\[
0,4,2,6,
\]
respectively, and gives the subdivision vertices on \(ac,ad,bc,bd\) colors
\[
5,3,7,1,
\]
respectively.

To prove the matching lower bound, suppose \(F\) had a circular \(r\)-coloring with
\[
2\le r<\frac83.
\]
Use the circle of circumference \(r\), with adjacent vertices required to have circular distance at least one. Put \(\delta=r-2\). The endpoints of a two-edge path must be at circular distance at most \(\delta\): the sum of two allowed directed edge differences belongs to
\[
[2,2r-2]=[r-\delta,r+\delta].
\]

Hence the colors of both \(c\) and \(d\) must lie within distance \(\delta\) of each of the colors of \(a,b\).

Place \(a\) at \(0\), and \(b\) at \(t\), where
\[
1\le t\le r/2.
\]
Since
\[
2\delta<r/2
\quad\text{and}\quad
\delta<1,
\]
the intersection of the radius-\(\delta\) neighborhoods of \(0,t\), if nonempty, is the single interval
\[
[t-\delta,\delta].
\]
Its length is at most
\[
2\delta-1<1.
\]
The colors of \(c,d\) therefore have distance less than one, contradicting the edge \(cd\). Thus
\[
\chi_c(F)=\frac83.
\]

## What remains unresolved

The theorem does **not** cover the main extremal regime: in a cubic graph every vertex has three degree-three neighbors. In particular, it does not cover the dodecahedron.

Subdividing edges until the additional hypothesis holds does not bridge this gap: a circular coloring of a subdivision need not descend to the original graph. The result therefore establishes a sharp conditional bound, not a proof or counterexample for the original \(20/7\) assertion. No claim about the novelty of this special case or an updated literature resolution is made.
