```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A support–parity argument gives sharp rich-edge bounds and characterizes the 15-rich-edge case, but does not establish existence in general.",
  "would_publish": false,
  "caveats": "These are self-contained structural results, not a solution or an improvement of the abnormal-edge bound; novelty is not claimed."
}
```

## 1. Scope and partial results

I do not have a proof or a counterexample to the full conjecture. I obtain the following structural results, including an explicit infinite family for which the number of rich edges is forced.

All graphs below are finite and loopless. Parallel edges are allowed, although the explicit family constructed below is simple. It suffices to consider connected graphs.

Write the Petersen graph as
\[
P=KG(5,2):
\]
its vertices are the two-element subsets of \([5]\), and two vertices are adjacent exactly when they are disjoint. A **Petersen coloring** is a map
\[
f:E(G)\longrightarrow E(P)
\]
such that, for every \(v\in V(G)\), the three incident edges map bijectively onto a vertex-star of \(P\). Denote that target vertex by \(\phi(v)\).

Call \(uv\in E(G)\):

- **poor** if \(\phi(u)=\phi(v)\);
- **rich** if \(\phi(u)\ne\phi(v)\).

These agree with the usual terminology for normal \(5\)-edge-colorings. Indeed, color an edge \(xy\) of \(P\) by the unique element
\[
\kappa(xy)\in[5]\setminus(x\cup y).
\]
The palette at target vertex \(x\) is \([5]\setminus x\). Thus \(\kappa\circ f\) is proper, and the union of the endpoint palettes has size \(3\) on poor edges and \(5\) on rich edges.

Conversely, from a normal \(5\)-edge-coloring, label each vertex by the two colors missing there. Adjacent labels are either equal or disjoint. The edge color then uniquely determines an incident Petersen edge, recovering \(f\).

### Partial theorem

Let \(G\) be connected, cubic, and not \(3\)-edge-colorable, and suppose \(f\) is a Petersen coloring. For \(h\in E(P)\), let \(r_h\) count the rich edges mapped to \(h\), and put
\[
R(f)=\sum_{h\in E(P)}r_h.
\]

Then:

1. All fifteen numbers \(r_h\) have the same parity. Moreover, the subgraph of \(P\) consisting of the edges with \(r_h>0\) contains \(P-x\) for some \(x\in V(P)\). Consequently,
   \[
   \begin{cases}
   R(f)\ge 15,&\text{if all }r_h\text{ are odd},\\[2mm]
   R(f)\ge 24,&\text{if all }r_h\text{ are even}.
   \end{cases}
   \]
   Both bounds are sharp.

2. Such a graph has a Petersen coloring with exactly \(15\) rich edges **if and only if** it is obtained from \(P\) by replacing each vertex with a connected, \(3\)-edge-colorable three-pole.

   Here a three-pole is a cubic fragment with three dangling edges; a single vertex with three dangling edges is permitted.

3. For every \(k\ge1\), there is an explicit connected simple bridgeless cubic graph \(G_k\) with
   \[
   |V(G_k)|=8k+2,\qquad |E(G_k)|=12k+3,
   \]
   which admits a Petersen coloring, and **every** Petersen coloring of \(G_k\) has exactly
   \[
   R(f)=9k+6
   \]
   rich edges.

The third conclusion shows that a strategy seeking Petersen colorings with only a bounded number of rich edges cannot work in general.

---

## 2. Elementary Petersen-graph facts

The proofs will use two facts about \(P\), established here.

### Lemma 1: the non-\(3\)-edge-colorable subgraphs of \(P\)

For a subgraph \(H\subseteq P\),
\[
H\text{ is not }3\text{-edge-colorable}
\quad\Longleftrightarrow\quad
P-x\subseteq H\text{ for some }x\in V(P).
\tag{1}
\]

#### First, \(P\) is not \(3\)-edge-colorable

Use the usual representation with outer edges \(a_i a_{i+1}\), inner edges \(b_i b_{i+2}\), and spokes \(a_i b_i\), with indices modulo \(5\).

A perfect matching uses an odd number of spokes. It cannot use exactly three: the two unmatched outer indices would have to be adjacent modulo \(5\), while the same two inner indices would have to differ by \(2\) modulo \(5\).

Thus a perfect matching uses one or five spokes. With five spokes, its complement is two \(5\)-cycles. With one spoke, rotate so that it is \(a_0b_0\). The other matching edges are forced, and the complementary cycles are
\[
a_0a_1b_1b_4a_4a_0
\quad\text{and}\quad
a_2a_3b_3b_0b_2a_2.
\]
Again they are two \(5\)-cycles.

In a proper \(3\)-edge-coloring, the complement of any color class would be a union of even cycles. Hence \(P\) has no such coloring.

#### Second, \(P-x\) is not \(3\)-edge-colorable

The graph \(P-x\) has nine vertices and twelve edges. In a proper \(3\)-edge-coloring, each color class would have size at most four, so all three would have size exactly four.

Each color would therefore be missing at exactly one vertex. The only vertices missing colors are the three neighbors of \(x\), each of degree two, and their missing colors would be distinct. Adding \(x\) and giving its incident edges those missing colors would produce a \(3\)-edge-coloring of \(P\), a contradiction.

#### Third, deleting two independent edges makes \(P\) \(3\)-edge-colorable

Abbreviate the vertex \(\{i,j\}\) by \(ij\). Permutations of \([5]\) act as automorphisms of \(P\). Fix
\[
e=12\,34.
\]
The stabilizer of \(e\) has two orbits on edges independent of \(e\), represented by
\[
13\,24,\qquad 14\,25.
\]
To check completeness: if neither endpoint of the second edge contains \(5\), it is one of the other two partitions of \(\{1,2,3,4\}\); otherwise the within-pair swaps and the interchange of \(\{1,2\}\) and \(\{3,4\}\) act transitively on the possibilities.

Consider the two disjoint \(5\)-cycles
\[
C_1=(12,34,15,23,45),\qquad
C_2=(13,24,35,14,25).
\]
The edge \(e\) lies on \(C_1\), and both representatives lie on \(C_2\). The five remaining Petersen edges form a perfect matching.

After deleting \(e\) and either representative, color that matching with color \(3\), and alternate colors \(1,2\) along each of the two remaining four-edge paths. This proves the claim for every independent pair.

Now suppose \(H\) is not \(3\)-edge-colorable. Its deleted-edge set
\[
D=E(P)\setminus E(H)
\]
cannot contain two independent edges. Since \(P\) is triangle-free, a set of pairwise incident edges is contained in one vertex-star. Thus \(D\subseteq\delta_P(x)\) for some \(x\), so \(P-x\subseteq H\). The reverse implication follows from the preceding non-colorability of \(P-x\). This proves (1). ∎

### Lemma 2: small cuts of \(P\)

The Petersen graph has no cut of size one or two, and every cut of size three is a vertex-star.

Indeed, \(P\) has girth five. In the two-subset representation, triangles would require six distinct elements, while a \(4\)-cycle would give two vertices with two common neighbors, which is impossible.

For a nontrivial cut, choose its shore \(A\) with \(1\le |A|\le5\). Then
\[
|\delta_P(A)|=3|A|-2|E(P[A])|.
\]
If \(2\le |A|\le4\), girth five makes \(P[A]\) a forest, giving
\[
|\delta_P(A)|\ge |A|+2\ge4.
\]
If \(|A|=5\), then \(|E(P[A])|\le5\): a cycle must use all five vertices, and any chord would create a shorter cycle. Hence the cut has size at least five. Only a singleton shore gives a cut of size three. ∎

---

## 3. The support–parity argument

For \(x\in V(P)\), set
\[
n_x=|\phi^{-1}(x)|.
\]
For a target edge \(h=xy\), let \(p_{x,h}\) count the poor source edges mapped to \(h\) whose two endpoints both have label \(x\).

Every vertex labeled \(x\) has exactly one incident edge mapped to \(h\). Counting these incidences gives
\[
n_x=r_h+2p_{x,h}.
\tag{2}
\]
Likewise,
\[
n_y=r_h+2p_{y,h}.
\tag{3}
\]
Therefore
\[
n_x\equiv r_h\equiv n_y\pmod2.
\]
Since \(P\) is connected, all \(n_x\) and all \(r_h\) have one common parity \(\varepsilon\).

Let
\[
H=\bigl(V(P),\{h:r_h>0\}\bigr)
\]
be the **rich support**.

### The rich support cannot be \(3\)-edge-colorable

Suppose, to the contrary, that \(H\) has a proper \(3\)-edge-coloring \(\psi\).

For every \(x\in V(P)\), extend the colors assigned by \(\psi\) on \(E(H)\cap\delta_P(x)\) to a bijection
\[
\sigma_x:\delta_P(x)\longrightarrow\{1,2,3\}.
\]
This is possible because \(\psi\) is proper.

For a source edge \(uv\), define its new color using
\[
\sigma_{\phi(u)}(f(uv)).
\]
This gives the same result at the other endpoint:

- if \(uv\) is poor, both endpoints use the same \(\sigma_x\);
- if it is rich and \(f(uv)=xy\), both endpoint assignments equal \(\psi(xy)\).

At every source vertex, the three incident edges receive three distinct colors. This would \(3\)-edge-color \(G\), a contradiction.

Consequently, Lemma 1 yields
\[
P-x\subseteq H
\quad\text{for some }x,
\qquad |E(H)|\ge12.
\tag{4}
\]

If \(\varepsilon=1\), all fifteen \(r_h\) are positive odd integers, so \(R(f)\ge15\). If \(\varepsilon=0\), every positive \(r_h\) is at least two, and (4) gives
\[
R(f)\ge2|E(H)|\ge24.
\]

This proves the first assertion.

It also gives a vertex-count consequence: an even-parity Petersen coloring of a non-\(3\)-edge-colorable graph uses at least nine target vertices, each with at least two preimages, so
\[
|V(G)|\ge18.
\tag{5}
\]

### Corollary: Petersen self-colorings are rigid

Every Petersen coloring \(P\to P\) is induced by a graph automorphism.

The source \(P\) is not \(3\)-edge-colorable and has only fifteen edges. Thus all fifteen source edges must be rich. Their multiplicities satisfy \(r_h=1\), and (2), with all poor-edge counts zero, gives \(n_x=1\) for every target vertex. Hence \(\phi\) is a vertex bijection preserving all edges. ∎

---

## 4. Classifying equality: exactly fifteen rich edges

Suppose \(R(f)=15\). Since all \(r_h\) have the same parity and their number is odd, they are all odd. Hence
\[
r_h=1\qquad(h\in E(P)).
\tag{6}
\]

Fix \(x\in V(P)\), and consider a connected component \(Q\) of the subgraph induced by the vertices labeled \(x\). For \(h\in\delta_P(x)\), let \(b_h(Q)\) count its boundary edges mapped to \(h\).

Equation (6) gives
\[
b_h(Q)\in\{0,1\}.
\]
Counting incidences mapped to \(h\) within \(Q\) gives
\[
b_h(Q)\equiv |V(Q)|\pmod2.
\tag{7}
\]
Thus, if \(Q\) meets the rich boundary at all, then
\[
b_h(Q)=1\qquad\text{for all }h\in\delta_P(x).
\]
It consumes all three boundary edges of the fiber \(\phi^{-1}(x)\).

Any other component of that fiber would have no boundary edges at all, and would consequently be a component of \(G\). Since \(G\) is connected, there is no other component.

Therefore each fiber is connected and has exactly three boundary edges, one for each incident Petersen edge. Regard these boundary edges as dangling edges. Their existing target-edge labels give a proper \(3\)-edge-coloring of the resulting three-pole. Contracting all ten fibers recovers \(P\).

This proves necessity.

### Converse construction

Take a connected \(3\)-edge-colorable three-pole \(Q_x\) for each \(x\in V(P)\).

A three-pole with \(q\) vertices and \(m\) internal edges satisfies
\[
3q=2m+3,
\]
so \(q\) is odd. In any proper \(3\)-edge-coloring, the number of dangling edges of each color is congruent to \(q\) modulo two. Since there are just three dangling edges, their colors are all distinct.

We may therefore relabel the three colors of \(Q_x\) by the three edges of \(\delta_P(x)\), matching its ports to the desired Petersen incidences. For every \(xy\in E(P)\), join the corresponding ports of \(Q_x\) and \(Q_y\), and map the resulting edge to \(xy\).

This is a Petersen coloring:

- internal three-pole edges are poor;
- the fifteen edges joining different three-poles are rich.

Thus \(R(f)=15\).

These graphs are not \(3\)-edge-colorable. If one had a proper \(3\)-edge-coloring, the same parity argument would make the three boundary colors of every pole distinct. Contracting all poles would then \(3\)-edge-color \(P\), which is impossible.

They are also bridgeless. More generally, every graph admitting a Petersen coloring is bridgeless: a binary cycle of \(P\) pulls back to an even subgraph, because it meets each target star in zero or two edges. Every Petersen edge belongs to a cycle, so every source edge belongs to an even subgraph and cannot be a bridge.

This completes the equality characterization.

---

## 5. Three-edge cuts and Petersen insertion

The preceding characterization does not cover every Petersen-colorable graph. A useful exact operation shows why.

### Lemma 3: every three-edge cut maps to a target star

Let \(D=\delta_G(A)\) have size three, and let \(f\) be a Petersen coloring. Then the three images of \(D\) are distinct and form a vertex-star of \(P\).

Let \(T\subseteq E(P)\) consist of the target edges occurring an odd number of times among the images of \(D\). For every binary cycle \(C\) of \(P\),
\[
|T\cap C|
\equiv |D\cap f^{-1}(C)|
\equiv0\pmod2.
\]
The last congruence holds because \(f^{-1}(C)\) is even.

By cut–cycle orthogonality, \(T\) is a cut of \(P\). This elementary fact can also be obtained by assigning vertex parities along the paths of a rooted spanning tree and then checking the non-tree edges using fundamental cycles.

Since \(D\) has three edges, \(|T|\) is either one or three. Lemma 2 excludes size one and says that size three means a vertex-star. Thus no images repeat, and the assertion follows. ∎

Consequently, one may cap either side of a three-edge cut with a new cubic vertex and retain a Petersen coloring.

### Petersen insertion

Given a cubic graph \(G\) and \(v\in V(G)\), define \(I_v(G)\) by:

1. deleting \(v\);
2. taking a fresh copy of \(P-w\);
3. joining the three former neighbors of \(v\) to the three neighbors of \(w\), through any chosen bijection.

Then
\[
G\text{ admits a Petersen coloring}
\quad\Longleftrightarrow\quad
I_v(G)\text{ admits a Petersen coloring}.
\tag{8}
\]

For the reverse implication, apply Lemma 3 to the cut surrounding the inserted \(P-w\), and cap the outside to recover \(G\).

For the forward implication, use an automorphism to color the inserted copy of \(P\), aligning its star at \(w\) with the three images at \(v\). Such alignment can realize any prescribed bijection of the three incident edges: permutations of \([5]\) act transitively on Petersen vertices, and the permutations of the three elements outside a fixed two-subset realize every permutation of its three neighbors.

There is an exact rich-edge count under this operation. Let \(f'\) be a Petersen coloring of \(I_v(G)\), and let \(f\) be the induced coloring of the capped outside graph \(G\). Write
\[
t_f(v)=|\{e\in\delta_G(v):e\text{ is rich in }f\}|.
\]
Then
\[
\boxed{R(f')=R(f)+15-2t_f(v).}
\tag{9}
\]

To prove this, cap the inserted piece as well. Its coloring becomes a Petersen self-coloring, hence an automorphism by the rigidity corollary. All twelve internal edges of \(P-w\) are therefore rich.

On each of the three boundary edges, richness is reversed. More explicitly, let its image be \(zx\), where the recovered cap vertex has label \(z\). The inserted endpoint has label \(x\). The outside endpoint has label either \(z\) or \(x\). Thus the edge is rich before insertion exactly when it is poor after insertion.

The three removed edges contribute \(t_f(v)\) rich edges, their replacements contribute \(3-t_f(v)\), and the inserted interior contributes twelve. This gives (9).

---

## 6. An explicit family with a forced rich-edge count

Set \(G_1=P\). Form \(G_2\) by a Petersen insertion at any vertex of \(G_1\).

For every subsequent insertion, use a vertex in the most recently inserted \(P-w\) that was not adjacent to \(w\) in that copy of \(P\). Its three incident edges are internal to that copy.

For a completely specified sequence, use the two-subset labels:

- in the first step, replace vertex \(12\);
- every inserted copy has \(w=12\);
- thereafter replace vertex \(13\) in the newest copy;
- match the three old and new terminals in lexicographic order.

The vertices \(12\) and \(13\) are nonadjacent, as required.

Each insertion adds eight vertices and twelve edges. Therefore
\[
|V(G_k)|=8k+2,\qquad |E(G_k)|=12k+3.
\]

Every \(G_k\) admits a Petersen coloring by (8). It is connected and simple by construction, and bridgeless because it admits such a coloring. For \(k\ge2\), it contains the newest, unmodified \(P-w\) as a subgraph, so Lemma 1 shows that it is not \(3\)-edge-colorable.

Now consider an arbitrary Petersen coloring of \(G_k\). Capping the newest inserted piece gives a self-coloring of \(P\), so all of that piece’s internal edges are rich. In particular, the designated vertex for the next insertion has three rich incident edges in **every** Petersen coloring.

Equation (9) consequently gives an increment of
\[
15-2\cdot3=9
\]
at each step. Since every Petersen coloring of \(G_1=P\) has fifteen rich edges, induction yields
\[
\boxed{R(f)=9k+6\quad\text{for every Petersen coloring of }G_k.}
\]

In particular:

- \(G_1=P\) attains the \(15\)-edge bound;
- \(G_2\) has eighteen vertices, and every Petersen coloring has exactly twenty-four rich edges.

Since the common multiplicity parity equals \(R(f)\bmod2\), \(G_2\) attains the even-parity bound. It also attains the vertex bound (5).

Finally,
\[
\frac{R(f)}{|E(G_k)|}
=\frac{9k+6}{12k+3}\longrightarrow\frac34.
\]
Thus even graphs built entirely from Petersen pieces can force a linear number of rich edges.

---

## 7. What remains missing

The support–parity argument starts with an existing Petersen coloring. It constrains that coloring but does not construct one for an arbitrary bridgeless cubic graph.

The equality characterization solves the explicit three-pole inflation class. Petersen insertion supplies a larger class and an exact counting rule. Neither argument addresses arbitrary cubic graphs without these decompositions—particularly arbitrary cyclically \(4\)-edge-connected instances.

Accordingly:

- there is no proof or counterexample to the full conjecture here;
- the quoted \(4/5\) bound on **normal** edges is not improved, since the bounds above distinguish rich from poor edges after full normality is assumed;
- the structural lemmas and constructions are proved here, but I have not established that they are new.