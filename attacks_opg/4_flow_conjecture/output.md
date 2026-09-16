```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I prove the conjecture up to eleven vertices, using an eight-odd-vertex flow bound and a ten-odd-vertex special case.",
  "would_publish": false,
  "caveats": "Special cases only; no novelty is claimed, and the general conjecture is not resolved."
}
```

# Partial result

Write
\[
T(G)=\{v\in V(G):d_G(v)\text{ is odd}\}.
\]

I establish the following special cases without using an excluded-Petersen structural theorem or any of the recent literature listed in the question.

**Theorem.** Let \(G\) be a finite bridgeless graph. Parallel edges are allowed.

1. If \(|T(G)|\le 8\), then \(G\) has a nowhere-zero \(4\)-flow.
2. Suppose \(|T(G)|=10\) and the even-degree vertices form an independent set. If \(G\) has no nowhere-zero \(4\)-flow, then \(G\) has a Petersen minor.

Consequently, **every bridgeless Petersen-minor-free graph on at most eleven vertices has a nowhere-zero \(4\)-flow**.

Loops can be deleted throughout and restored independently. Thus independence in part 2 may be interpreted after deleting loops.

The proof also gives an explicit Petersen-minor certificate in part 2 when its flow constructions fail. These are limited special cases, not a claim of a new research theorem.

## 1. Group flows and cubic reduction

Let
\[
\Gamma=\mathbb F_2^2=\{0,a,b,c\},\qquad a+b+c=0.
\]
A nowhere-zero \(\Gamma\)-flow assigns a nonzero element to every edge, with the incident values summing to zero at every vertex. Orientations are immaterial in this group.

Such a flow produces an integer nowhere-zero \(4\)-flow. Indeed, its two coordinate supports \(A,B\) are even subgraphs and satisfy \(A\cup B=E(G)\). Orient each even subgraph Eulerianly. Relative to a fixed reference orientation, let their signed unit circulations be \(f_A,f_B\). Then
\[
f=f_A+2f_B
\]
is an integer circulation, and every edge has value in
\[
\{-3,-2,-1,1,2,3\}.
\]
It therefore suffices to construct nowhere-zero \(\Gamma\)-flows.

### An elementary splitting lemma

A **split** of two distinct edges \(vx,vy\) deletes them and adds an edge \(xy\), possibly a loop. It decreases \(d(v)\) by two.

**Lemma 1.** If \(G\) is connected, loopless and bridgeless, and \(d(v)\ge4\), some pair of edges at \(v\) can be split while preserving connectedness and bridgelessness.

**Proof.** Put \(K=G-v\).

For a split of \(vx,vy\), and a vertex set \(S\) not containing \(v\),
\[
|\delta_{G'}(S)|=
\begin{cases}
|\delta_G(S)|-2,&x,y\in S,\\
|\delta_G(S)|,&\text{otherwise}.
\end{cases}
\tag{1}
\]
Thus a new bridge can arise only from a \(3\)-edge cut of \(G\) containing both selected edges.

If \(K\) is disconnected, choose the two edges to enter different components of \(K\). Every component of \(K\) has at least two edges to \(v\), since \(G\) has no bridge, so the split preserves connectedness. Moreover, any set \(S\) containing both selected endpoints meets two components of \(K\). Each nonempty intersection contributes at least two edges to \(\delta_G(S)\), giving
\[
|\delta_G(S)|\ge4.
\]
Equation (1) therefore rules out a new bridge.

Now suppose \(K\) is connected. Every split preserves connectedness, since \(v\) retains at least two incident edges.

Label the edges incident with \(v\) as distinct ports. A pair of ports is bad precisely when some bridge of \(K\) has, on one side, exactly those two ports. To see this, a new bridge gives a set \(S\subseteq V(K)\) with \(|\delta_G(S)|=3\) containing both selected ports. Since \(K\) is connected and \(d(v)\ge4\), \(S\) is a proper subset of \(V(K)\), and necessarily
\[
|\delta_K(S)|=1,
\]
with exactly two ports entering \(S\). The converse follows from (1).

Fix one port \(e\). It cannot have two distinct bad partners \(f,g\). Otherwise two bridge cuts of \(K\) induce the port partitions
\[
\{e,f\}\mid\text{remaining ports},
\qquad
\{e,g\}\mid\text{remaining ports}.
\]
There is a fourth port because \(d(v)\ge4\), so these partitions cross: all four intersections of their sides are nonempty. But cuts defined by bridges of a connected graph do not cross, as is immediate from its bridge tree.

Thus \(e\) has at most one bad partner, and a permissible pair exists. \(\square\)

### The resulting cubic core

Apply the following operations repeatedly:

- delete loops;
- suppress degree-two vertices;
- use Lemma 1 at vertices of degree at least four;
- discard isolated vertices.

Bridgelessness is preserved. Each operation decreases the number of edges or vertices, so the process terminates. A nonisolated vertex in a bridgeless loopless graph cannot have degree one.

Splitting changes a degree by two and does not change any other degree parity. Consequently, the final nonempty graph \(H\) is a bridgeless cubic multigraph whose vertices are exactly the original odd-degree vertices:
\[
V(H)=T(G).
\tag{2}
\]

There is a useful precise record of this reduction. Associate every current edge with the trail in the original graph that it represents. Splitting and suppression concatenate edge-disjoint trails; deleted loops represent closed trails. At termination we obtain:

- edge-disjoint trails \(Q_e\), one for each \(e\in E(H)\), joining the corresponding original vertices;
- an even subgraph \(F\);

whose edge sets partition \(E(G)\).

A proper \(3\)-edge-coloring of \(H\), using \(a,b,c\), routes a nowhere-zero \(\Gamma\)-flow along these trails. Internal trail visits contribute two equal values and cancel. At a branch vertex the three endpoint values sum to zero. Give every edge of \(F\) any one fixed nonzero value.

Thus:
\[
H\text{ is \(3\)-edge-colorable}
\quad\Longrightarrow\quad
G\text{ has a nowhere-zero \(4\)-flow}.
\tag{3}
\]

If needed, closed subtrails can be removed from each \(Q_e\) and transferred into \(F\), so that the \(Q_e\) become simple paths.

## 2. Cubic graphs on at most ten vertices

**Lemma 2.**

1. Every bridgeless cubic multigraph on at most eight vertices is \(3\)-edge-colorable.
2. If a bridgeless cubic multigraph on at most ten vertices is not \(3\)-edge-colorable, it is isomorphic to the Petersen graph.

**Proof.** Components can be treated separately.

First, every bridgeless cubic graph has a perfect matching. Here is the standard application of Tutte’s perfect-matching criterion. For any \(S\subseteq V(H)\), each odd component \(C\) of \(H-S\) has
\[
|\delta_H(C)|\equiv 3|V(C)|\equiv1\pmod2.
\]
Such a component cannot be an entire cubic component of \(H\), since cubic components have even order. Bridgelessness therefore gives \(|\delta_H(C)|\ge3\). If there are \(q\) odd components, then
\[
3q\le \sum_C|\delta_H(C)|\le 3|S|,
\]
which is Tutte’s criterion.

We also use two elementary coloring reductions.

- **Triangle reduction.** Contract a triangle to one vertex. In a bridgeless cubic graph the triangle has three external edges: an additional internal parallel edge would leave a \(1\)-edge cut. Contraction preserves bridgelessness and cubicity. A coloring of the contracted graph extends, because its three external colors are distinct; color each triangle edge with the color missing at its two endpoints.

- **Parallel-edge reduction.** A two-vertex component consisting of three parallel edges is directly colorable. Otherwise, if \(u,v\) have two parallel edges and their remaining edges are \(ux,vy\), delete \(u,v\) and add \(xy\). Here \(x\ne y\), since otherwise the third edge at \(x\) would be a bridge. The reduction preserves bridgelessness: cycles traversing the \(u,v\) gadget become cycles using \(xy\), and every retained edge remains on a cycle. A coloring extends by giving \(ux,vy\) the color of \(xy\), and the parallel edges the other two colors.

Both reductions remove two vertices.

For part 1, use induction to dispose of triangles and parallel edges. In the remaining simple triangle-free graph, take a perfect matching \(M\). Its complement is a \(2\)-factor. Any odd cycle in this \(2\)-factor has length at least five. The number of odd cycles is even, because the graph has even order. Thus the presence of an odd cycle would require at least ten vertices.

All cycles of \(H-M\) are therefore even. Color \(M\) with one color and alternate the other two colors around these cycles.

For part 2, a noncolorable graph must have exactly ten vertices, by part 1. The two reductions show that it must be simple and triangle-free. Again take a perfect matching \(M\). Unless its complementary \(2\)-factor consists of two \(5\)-cycles, that \(2\)-factor is even and gives a coloring.

Write the two cycles as \(C,D\). No matching edge can be a chord of either \(5\)-cycle, since a chord would create a triangle. Hence \(M\) is a bijection between \(V(C)\) and \(V(D)\).

If two adjacent vertices of \(C\) are matched to adjacent vertices of \(D\), delete those two cycle edges and insert the corresponding two matching edges. The resulting two spanning paths join into a Hamilton cycle of length ten. Alternating two colors on that cycle and giving the complementary matching the third color colors \(H\).

Consequently, the matching bijection sends every edge of \(C\) to a nonedge of \(D\). The complement of a \(5\)-cycle is another \(5\)-cycle, so this determines the graph: with matching edges \(a_i b_i\), its other edges are
\[
a_i a_{i+1},\qquad b_i b_{i+2}
\quad(i\in\mathbb Z_5).
\]
This is the Petersen graph. \(\square\)

Combining Lemma 2(1) with (2)–(3) already proves part 1 of the theorem.

## 3. A Petersen switching lemma

Let \(P\) denote the Petersen graph.

**Lemma 3.** Given two independent edges \(ab,cd\) of \(P\), at least one of
\[
P-ab-cd+ac+bd,
\qquad
P-ab-cd+ad+bc
\tag{4}
\]
is bridgeless and \(3\)-edge-colorable. Parallel edges in these graphs are allowed.

**Proof.** In fact, both graphs in (4) are bridgeless.

We need two elementary properties of \(P\). It is cubic of order ten and girth five. For any nonempty proper vertex set, choose the smaller side \(S\), so \(|S|\le5\). The girth condition gives
\[
|E(P[S])|\le
\begin{cases}
|S|-1,&|S|\le4,\\
5,&|S|=5.
\end{cases}
\]
Using
\[
|\delta_P(S)|=3|S|-2|E(P[S])|,
\]
every cut has size at least three, and a cut of size three must isolate a single vertex.

It follows that \(P-ab-cd\) is connected and bridgeless. A bridge in it would produce a \(3\)-edge cut of \(P\) containing both \(ab\) and \(cd\), impossible because these edges are independent. Adding either replacement pair preserves bridgelessness.

Also, every two nonadjacent vertices of \(P\) have a common neighbor. Indeed, the vertices at distances zero, one and two from any vertex are all distinct by the girth condition, and number
\[
1+3+6=10.
\]

There is at most one additional edge among \(a,b,c,d\), besides \(ab,cd\); two additional edges would create a triangle or a \(4\)-cycle.

- If there is no additional edge, \(a,c\) have a common neighbor outside \(\{a,b,c,d\}\). Adding \(ac\) creates a triangle.
- If there is an additional edge, relabel so that it is \(ac\). Then \(b,d\) have a common neighbor outside these four vertices, so adding \(bd\) creates a triangle.

Thus one replacement graph in (4) has a triangle. Contract it, apply Lemma 2(1) to the resulting eight-vertex cubic graph, and extend the coloring back. \(\square\)

The following is the key consequence for a cubic core.

**Lemma 4.** Suppose the edge partition of Section 1 represents a Petersen core, and \(G\) has no nowhere-zero \(4\)-flow. If \(e,f\in E(P)\) are independent, then \(Q_e,Q_f\) are vertex-disjoint.

**Proof.** Suppose \(Q_{ab}\) and \(Q_{cd}\) meet at \(x\). Cut both paths at \(x\). Their four portions can be rejoined to realize either replacement pairing in (4), using exactly the same original edges.

The rejoined objects may be trails rather than simple paths, which is harmless for routing a group flow. Choose the \(3\)-edge-colorable replacement supplied by Lemma 3. Route its colors through the rejoined trails, retain the other paths, and give \(F\) a fixed nonzero value. This constructs a nowhere-zero \(\Gamma\)-flow on every edge of \(G\), a contradiction. \(\square\)

## 4. Extracting a Petersen minor when even vertices are independent

We now prove part 2 of the theorem.

Suppose
\[
|T(G)|=10,
\]
the set
\[
W=V(G)\setminus T(G)
\]
is independent, and \(G\) has no nowhere-zero \(4\)-flow.

Take its cubic core \(H\). By (3), \(H\) is not \(3\)-edge-colorable, so Lemma 2 gives
\[
H\cong P.
\]
Use the simple paths \(Q_e\) and even remainder \(F\) described above.

### Paths avoid other branch vertices

For \(e=ab\in E(P)\), the path \(Q_e\) cannot pass internally through another branch vertex \(z\in T(G)\).

Indeed, among the three Petersen edges incident with \(z\), at least one is independent of \(ab\): at most two can have their other endpoint in \(\{a,b\}\). Its representing path meets \(Q_e\) at \(z\), contrary to Lemma 4.

Thus every internal vertex of every \(Q_e\) lies in \(W\). Since \(W\) is independent, each \(Q_e\) has length one or two.

### Constructing disjoint branch sets

Fix a vertex \(w\in W\) used by the paths.

If several paths use \(w\), their corresponding Petersen edges are pairwise incident, by Lemma 4. In a triangle-free graph, a pairwise-incident family of at least two edges has a common endpoint. Assign \(w\) to that common Petersen endpoint.

If only one path \(Q_{uv}\) uses \(w\), assign \(w\) to either \(u\) or \(v\).

For each Petersen vertex \(u\), let
\[
B_u=\{u\}\cup
\{w\in W:w\text{ has been assigned to }u\}.
\]
These sets are pairwise disjoint. Each is connected: an assigned vertex \(w\) lies on a length-two path \(u-w-v\), and hence is adjacent to \(u\).

For every Petersen edge \(uv\):

- if \(Q_{uv}\) has length one, it directly joins \(B_u\) and \(B_v\);
- if \(Q_{uv}=u-w-v\), then \(w\) was assigned to one of \(u,v\), so one of its two edges joins \(B_u\) and \(B_v\).

Therefore the ten connected, pairwise disjoint sets \(B_u\) form a Petersen-minor model. This proves part 2.

### The eleven-vertex corollary

The number of odd-degree vertices is even. A graph on at most eleven vertices therefore has either:

- at most eight odd-degree vertices, covered by part 1; or
- exactly ten odd-degree vertices and at most one even-degree vertex, covered by part 2.

Hence the conjecture holds on at most eleven vertices.

## 5. What remains unresolved

The argument gives the following necessary conditions for a counterexample:

- it has at least ten odd-degree vertices;
- it has at least twelve vertices in total;
- if it has exactly ten odd-degree vertices, two of its even-degree vertices must be adjacent.

The essential general obstruction is still present: the cubic reduction produces an edge-disjoint path representation, **not necessarily a minor**.

For a concrete illustration, draw the Petersen graph using an outer regular pentagon, an inner pentagram, and five radial spokes. Replace the five crossings of the inner pentagram by degree-four vertices. The resulting graph is planar and bridgeless, hence Petersen-minor-free. Nevertheless, splitting each crossing along the original pentagram edges recovers the Petersen graph. Thus even bridgelessness-preserving splits can destroy Petersen-minor-freeness.

The independence assumption in part 2 makes the final minor extraction rigorous: every core path has at most one internal vertex, and shared internal vertices can be absorbed into disjoint star-shaped branch sets. I have not removed that assumption, nor handled larger noncolorable cubic cores. The general \(4\)-flow conjecture is therefore not resolved by this argument.