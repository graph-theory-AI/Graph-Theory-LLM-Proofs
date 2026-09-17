```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A one-ended cubic graph admitting a vertex enumeration whose sufficiently large initial segments have at most five outgoing edges cannot be uniquely Hamiltonian.",
  "would_publish": false,
  "caveats": "This is a restricted low-width obstruction, not a resolution of the general question; literature novelty is not claimed."
}
```

# A partial result: an eventual cutwidth obstruction

Write \(\delta(S)\) for the set of edges with exactly one endpoint in \(S\). All graphs below are simple, except for explicitly constructed finite auxiliary graphs.

I prove the following special case.

**Theorem.** Let \(G\) be a connected, locally finite, one-ended cubic graph. Suppose that its vertices have an enumeration
\[
V(G)=\{v_1,v_2,\ldots\}
\]
such that, for all sufficiently large \(n\),
\[
\left|\delta\bigl(\{v_1,\ldots,v_n\}\bigr)\right|\leq 5.
\tag{1}
\]
If \(G\) has a Hamilton circle, then it has at least two.

Thus a cubic counterexample to Mohar’s question would have to satisfy the following necessary condition:

> In every vertex enumeration, infinitely many initial segments have at least six outgoing edges.

The argument includes a class of graphs whose unique end has degree **four**, so the hypothesis is not merely another formulation of the end-degree-three case in the question. The relevant class consists of four-rail graphs with chronologically ordered rungs and an arbitrary finite cubic cap.

No claim of novelty is made for this obstruction.

## 1. Hamilton circles in a one-ended graph

In a locally finite one-ended graph, Hamilton circles correspond exactly to spanning double rays.

Indeed, deleting the unique end \(\omega\) from a Hamilton circle leaves an open arc containing every vertex. Its edges form a connected, spanning, 2-regular graph, hence a double ray. Conversely, both tails of a spanning double ray converge to \(\omega\), and adjoining \(\omega\) gives a circle in the Freudenthal compactification.

Consequently, throughout the proof we may work with spanning double rays.

If \(D\) is a spanning double ray and \(S\) is finite and nonempty, then \(D[S]\) is a disjoint union of finite paths, and
\[
|\delta_D(S)|=2\,c(D[S]),
\tag{2}
\]
where isolated vertices count as path components. In particular, if \(|\delta_G(S)|\leq 3\), then \(D[S]\) is one spanning path of \(G[S]\).

## 2. A finite parity lemma

We need a version of the usual path-rotation parity argument that allows one exceptional vertex.

**Lemma 1.** Let \(K\) be a finite loopless multigraph on at least three vertices, and let \(s\in V(K)\). Suppose every vertex other than \(s\) has odd degree. Then every edge incident with \(s\) belongs to an even number of Hamilton cycles.

Parallel edges are distinguished when cycles are counted.

**Proof.** Fix an oriented edge \(e=sv_2\). Consider all edge-labelled Hamilton paths
\[
P=(s,v_2,\ldots,v_N)
\]
whose first edge is \(e\).

Construct a finite rotation graph on these paths. At the terminal vertex \(t=v_N\), an edge to an internal vertex other than \(s\) permits the usual reversal of the terminal segment. Exclude the edge currently used as the last path edge. If another parallel edge joins \(t\) to its predecessor, the corresponding operation simply replaces the last edge. Every permitted operation has an inverse.

Writing \(m(s,t)\) for the number of edges between \(s\) and \(t\), the degree of \(P\) in this rotation graph is
\[
d_K(t)-1-m(s,t).
\]
Since \(t\neq s\), the first two terms have even difference. The handshaking identity therefore gives
\[
\sum_P m(s,\operatorname{last}(P))\equiv 0\pmod 2.
\]
The sum counts exactly the Hamilton cycles containing \(e\): orient such a cycle so that it starts with \(e\), and delete its closing edge at \(s\). ∎

## 3. Two small-cut obstructions

### 3.1 A finite two-edge boundary

**Lemma 2.** If a one-ended cubic Hamiltonian graph has a nonempty finite set \(S\) with \(|\delta(S)|=2\), then it is not uniquely Hamiltonian.

**Proof.** Let \(D\) be a spanning double ray. By (2), \(D[S]\) is a spanning path.

Replace everything outside \(S\) by a new vertex \(s\), retaining the two boundary edges as labelled edges incident with \(s\). The resulting finite graph has degree three at every original vertex and degree two at \(s\). The path \(D[S]\), together with the two edges at \(s\), is a Hamilton cycle.

Lemma 1 supplies a second Hamilton cycle. Since \(s\) has degree two, both cycles use the same two boundary edges. Thus they give two different spanning paths through \(S\) with the required attachments. Replacing \(D[S]\) by the other path produces another spanning double ray. ∎

### 3.2 Cofinal three-edge boundaries

Call a family \(\mathcal S\) of finite vertex sets **cofinal** if every finite vertex set is contained in a member of \(\mathcal S\).

**Lemma 3.** A one-ended cubic Hamiltonian graph with a cofinal family of finite sets \(S\) satisfying \(|\delta(S)|=3\) is not uniquely Hamiltonian.

**Proof.** Suppose, for a contradiction, that \(D\) is its unique spanning double ray.

By local finiteness and cofinality, choose finite sets \(S_1,S_2,\ldots\), each with boundary size three, such that
\[
N[S_n]\subseteq S_{n+1},\qquad \bigcup_n S_n=V(G),
\]
and \(|S_1|\geq 2\).

For each \(n\), construct a finite graph \(B_n\) from \(G[S_n]\) by replacing the exterior by one vertex \(z_n\). Label the three resulting edges at \(z_n\) by \(1,2,3\). Every vertex of \(B_n\) has degree three; parallel edges are allowed.

Let
\[
h_n(i)=
\#\{\text{Hamilton cycles of }B_n\text{ omitting boundary edge }i\}.
\]
Applying Lemma 1 to each of the three edges at \(z_n\) shows
\[
h_n(1)\equiv h_n(2)\equiv h_n(3)\pmod 2.
\tag{3}
\]

The double ray \(D\) determines a Hamilton cycle of \(B_n\). For its omitted-edge type, the count is exactly one: a second path with the same two boundary attachments could replace \(D[S_n]\). Hence (3) implies
\[
h_n(i)\text{ is positive and odd for every }i.
\tag{4}
\]

Now consider the annulus \(S_{n+1}\setminus S_n\). Replace \(S_n\) by an inner vertex \(x\), and the exterior of \(S_{n+1}\) by an outer vertex \(y\). Retain all six labelled boundary edges. Because \(N[S_n]\subseteq S_{n+1}\), these edges have their other endpoints in the annulus. The resulting finite auxiliary graph \(A_n\) is cubic.

Let \(t_{ij}\) count its Hamilton cycles omitting inner boundary edge \(i\) and outer boundary edge \(j\). Cutting and gluing along the inner boundary gives the exact identity
\[
h_{n+1}(j)=\sum_{i=1}^{3}h_n(i)t_{ij}.
\tag{5}
\]
For completeness, every Hamilton cycle counted on the left crosses the inner three-edge boundary in exactly two edges. Its restriction to \(S_n\) is therefore one spanning path. Contracting that path gives the corresponding Hamilton cycle of \(A_n\), and the decomposition is reversible.

By (4) and (5),
\[
\sum_i t_{ij}\equiv 1\pmod 2
\qquad\text{for each }j.
\tag{6}
\]
Put \(r_i=\sum_j t_{ij}\). Applying Lemma 1 to the three edges at the inner vertex \(x\) gives
\[
r_1\equiv r_2\equiv r_3\pmod 2.
\]
Equation (6) says that their total is odd. Consequently every \(r_i\) is odd, and in particular
\[
r_i>0\qquad(i=1,2,3).
\tag{7}
\]

Choose a Hamilton cycle of \(B_1\) whose omitted-edge type differs from that of \(D\). Such a cycle exists by (4). Equation (7) allows its spanning path through \(S_1\) to be extended through every successive annulus, retaining all previous choices.

The resulting finite spanning paths are nested. Their union is connected and spans \(G\). Every vertex eventually lies away from the boundary and has degree two in the union. Thus the union is a spanning double ray. It differs from \(D\) on \(\delta(S_1)\), a contradiction. ∎

## 4. Four rails with chronologically ordered rungs

Here is the additional special case needed to pass from boundary size three to the width-five theorem.

### The graph model

Start with a finite graph \(F\) having four distinct labelled ports \(p_1,p_2,p_3,p_4\). Each port has degree two in \(F\), and every other vertex has degree three.

At each step:

1. choose two different labels \(a,b\);
2. add one new vertex after the current port on rail \(a\), and one after the current port on rail \(b\);
3. join these two new vertices by a **rung**;
4. make them the new ports of rails \(a,b\).

Assume each label is chosen infinitely often. The limit is cubic and has four vertex-disjoint rail rays outside \(F\). Each finite construction prefix has exactly four outgoing edges, one at each current port.

Assume additionally that the limit graph is one-ended.

**Lemma 4.** A Hamiltonian graph constructed in this way is not uniquely Hamiltonian.

### Frontier states

An acyclic spanning partial Hamilton subgraph of a construction prefix can have either:

- **state \(P(I)\):** one spanning path whose two outgoing edges have labels \(I\subseteq\{1,2,3,4\}\), \(|I|=2\);
- **state \(Q(\Pi)\):** two spanning paths using all four outgoing edges, where \(\Pi\) is the pairing of their endpoint labels.

These are exactly the possibilities obtained by restricting a spanning double ray to a construction prefix.

Suppose the next rung uses the label pair \(A\). The following transitions are available:
\[
\begin{array}{c|c|c}
\text{Current state}&\text{Condition}&\text{Next state}\\ \hline
P(I)&A=I&P(I)\\
P(I)&|A\cap I|=1&P(I\triangle A)\\
P(I)&A=I^c&Q(\{I,I^c\})\\
Q(\Pi)&\text{always}&Q(\Pi)\\
Q(\Pi)&A\notin\Pi&P(A^c).
\end{array}
\tag{8}
\]

Here \(A\notin\Pi\) means that the two labels of \(A\) belong to different pairs of \(\Pi\).

To verify the table, inspect the two new vertices. A vertex whose incoming rail edge is unused must use the rung and its outgoing rail edge. If both incoming edges are used, one may pass straight along both rails, omitting the rung. Alternatively, using the rung joins the two incoming path ends. This is permitted precisely when they lie in different path components; otherwise it closes a finite cycle.

### Every admissible state extends

One-endedness implies the following fact:

> For any partition of the four rails into two nonempty classes, arbitrarily late rungs join the two classes.

Otherwise, deleting a finite prefix containing all cross-rungs would leave infinite rail tails in two different components.

It follows that every admissible frontier state extends to a spanning double ray. From a \(P\)-state, follow (8) until a \(Q\)-state is reached, if this ever happens. In a \(Q(\Pi)\)-state, pass straight until a rung joins the two pairs of \(\Pi\), and then use that rung to merge the two paths.

Repeat. Either the construction eventually remains in \(P\)-states, or it returns to \(P\)-states arbitrarily far out. In both cases, the union is spanning and 2-regular, and arbitrarily large prefixes lie in a single path. Hence the union is connected and is a spanning double ray.

Moreover, a \(Q\)-state has at least two different extensions. One may merge at one future cross-rung, or omit that rung and merge at a later cross-rung. Both choices extend, and their resulting edge sets differ.

### Proof of Lemma 4

Let \(D\) be a spanning double ray and restrict it to the initial cap \(F\).

If its state is \(Q\), the preceding paragraph already supplies two different spanning double rays.

Suppose its state is \(P\). Add a new vertex \(s\) to \(F\), adjacent to all four ports. Every vertex other than \(s\) now has degree three, while \(s\) has degree four. The path \(D[F]\), closed through \(s\), is a Hamilton cycle of this finite graph.

Choose either of its edges at \(s\). Lemma 1 gives a second Hamilton cycle containing that edge. Deleting \(s\) gives a different admissible spanning path through the cap. Both cap paths extend, by the extension argument above, to spanning double rays of the infinite graph. Their restrictions at the cap differ, so the double rays are distinct. ∎

These four-rail graphs have end-degree four: the four rails give four disjoint rays, while the cofinal four-edge boundaries exclude five disjoint rays. Thus Lemma 4 genuinely treats a class beyond end-degree three.

## 5. Proof of the eventual cutwidth theorem

Suppose, for a contradiction, that \(G\) satisfies (1) and has a unique spanning double ray \(D\). Put
\[
S_n=\{v_1,\ldots,v_n\}.
\]

By Lemma 2, no nonempty finite set has boundary size two. By Lemma 3, there is no cofinal family of finite sets with boundary size three.

Since \(G\) is cubic,
\[
|\delta(S_n)|
=3n-2|E(G[S_n])|
\equiv n\pmod 2.
\tag{9}
\]
Also, every finite nonempty set has at least two boundary edges, because it is crossed by \(D\).

If infinitely many \(S_n\) had boundary size three, they would form a cofinal family, contrary to Lemma 3. Combining this observation with (1), (9), and the absence of two-edge boundaries, we obtain, for all sufficiently large \(k\),
\[
|\delta(S_{2k})|=4,\qquad
|\delta(S_{2k+1})|=5.
\tag{10}
\]

Consider the consecutive vertices
\[
a=v_{2k+1},\qquad b=v_{2k+2}.
\]
The identity
\[
|\delta(S\cup\{v\})|
=|\delta(S)|+3-2|N(v)\cap S|
\]
and (10) show that:

- \(a\) has exactly one neighbour in \(S_{2k}\);
- \(b\) has exactly two neighbours in \(S_{2k}\cup\{a\}\).

If \(a\) and \(b\) are not adjacent, \(b\) has two neighbours already in \(S_{2k}\), so
\[
\left|\delta\bigl(S_{2k}\cup\{b\}\bigr)\right|
=4+3-4=3.
\tag{11}
\]
If this happened for infinitely many \(k\), the sets in (11) would be cofinal, again contradicting Lemma 3.

Consequently, after discarding a finite initial segment, every consecutive pair
\[
(v_{2k+1},v_{2k+2})
\]
is adjacent.

Delete the edge within each such pair temporarily. Each vertex in the remaining tail now has:

- exactly one neighbour earlier in the ordering;
- exactly one neighbour later in the ordering.

The four edges leaving an initial even prefix therefore generate four disjoint forward rays, and these rays contain every later vertex. Indeed, following predecessors strictly decreases the vertex index and must reach the finite prefix; following successors continues indefinitely.

Enlarge the finite prefix through complete pairs until each of the four rays has been entered. Its four outgoing edges then have distinct inner endpoints, giving four degree-two ports in the induced finite cap.

The two vertices in each subsequent consecutive pair lie on different rails. Otherwise, since they are consecutive in the ordering, their connecting rail edge would have to be their deleted pair edge. The graph is simple, so no such rail edge remains.

Restoring the deleted edges therefore gives exactly the four-rail construction of Section 4:

- each consecutive pair adds the next vertex on two different rails;
- their mutual edge is the rung;
- the order of these pairs respects the order along every rail.

The original graph is one-ended, so Lemma 4 applies and contradicts uniqueness. This proves the theorem. ∎

## 6. What remains unresolved

This does **not** answer Mohar’s question in general. In particular:

- it does not exclude arbitrary one-ended cubic graphs of end-degree four;
- it does not treat the general \(r\geq 4\) problem;
- it does not produce a uniquely Hamiltonian example.

The four-rail argument depends critically on a two-path frontier state using **all four** outgoing edges. One-endedness then guarantees later opportunities to merge the two paths. With wider frontiers, unused outgoing channels prevent this argument from going through.

The precise conclusion established here is the low-width obstruction: **a cubic counterexample must have initial edge-boundaries of size at least six infinitely often in every vertex ordering.**