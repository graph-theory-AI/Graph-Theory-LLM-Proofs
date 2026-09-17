```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "For H=C4+K1 and its complement I construct explicit hypercube components for every n≥12, and I give uniform sufficient conditions covering all odd cycles, all stars, and further infinite families.",
  "would_publish": false,
  "caveats": "The full characterization and optimal thresholds remain unresolved; novelty has not been checked."
}
```

# A partial answer: large non-singleton components

Throughout, \(H\)-free means **induced-\(H\)-free**. Write \(\mathcal G_{H,n}\) for the flip graph, and write \(F+J\) and \(F\vee J\) for disjoint union and join, respectively.

The main new result is the following.

## Theorem 1

Let
\[
H=C_4+K_1
\qquad\text{or}\qquad
H=\overline{C_4+K_1}=(2K_2)\vee K_1.
\]
For every \(n\ge 12\), the graph \(\mathcal G_{H,n}\) has a connected component isomorphic to
\[
Q_{D_n},
\qquad
D_n=\left\lfloor\frac{(n-10)^2}{4}\right\rfloor+5,
\]
where \(Q_d\) is the \(d\)-dimensional hypercube. In particular, \(\mathcal G_{H,n}\) is disconnected.

Thus these components contain \(2^{\Theta(n^2)}\) graphs, and none of their vertices is isolated. This proves disconnectedness without constructing an induced-saturated graph.

I also prove the following sufficient bounds:

\[
\begin{array}{c|c}
H\text{, and also }\overline H & \text{disconnected whenever}\\ \hline
C_{2k+1},\quad k\ge2 & n\ge (k+1)^2\\
K_{1,r},\quad r\ge2 & n\ge 3^{r-1}.
\end{array}
\]

Sections 4 and 5 give broader versions of these two families.

The persistence observation in the previous attempt is valid and is reproved below. The icosahedral graph from that attempt is also used, but all properties needed here are verified independently.

---

# 1. Two general observations

## 1.1 Complementation

Complementation gives an isomorphism
\[
\mathcal G_{H,n}\cong\mathcal G_{\overline H,n}.
\]
It preserves single-edge flips and exchanges induced copies of \(H\) and \(\overline H\).

## 1.2 Disconnectedness persists upward

### Proposition 2

Suppose \(|V(H)|\ge2\). If \(\mathcal G_{H,n}\) is disconnected, then \(\mathcal G_{H,m}\) is disconnected for every \(m\ge n\).

### Proof

There is a safe way to extend every \(H\)-free graph by one vertex:

- If \(H\) has no isolated vertex, add an isolated vertex.
- If \(H\) has an isolated vertex, then \(H\) has no universal vertex; add a universal vertex.

In either case, the extension remains \(H\)-free.

Let \(A,B\) lie in different components of \(\mathcal G_{H,n}\), and let \(A^+,B^+\) be their safe extensions. A path from \(A^+\) to \(B^+\) in \(\mathcal G_{H,n+1}\), restricted at every step to \([n]\), would give a walk from \(A\) to \(B\) in \(\mathcal G_{H,n}\): flips incident with the new vertex merely produce repeated restrictions. This is impossible.

Iterating proves the result. \(\square\)

Consequently, for nontrivial \(H\), “disconnected for all sufficiently large \(n\)” is equivalent to “disconnected for at least one \(n\).”

---

# 2. The icosahedral template

Let \(I\) have vertex set
\[
\{x,y\}\cup\{a_i,b_i:i\in\mathbb Z_5\}
\]
and edges
\[
xa_i,\quad yb_i,\quad
a_i a_{i+1},\quad b_i b_{i+1},\quad
a_i b_i,\quad a_i b_{i-1}.
\]

Define the antipodal pairs to be
\[
\{x,y\},
\qquad
\{a_i,b_{i+2}\}\quad(i\in\mathbb Z_5).
\]

We need three elementary properties of this graph.

## Lemma 3

1. Each antipodal pair is a nonedge. Between any two different antipodal pairs, the edges form a perfect matching.
2. The graph \(I\) is induced-\(C_4\)-free.
3. Automorphisms of \(I\), preserving its antipodal pairs, are transitive on:
   - vertices;
   - edges;
   - non-antipodal nonedges.

### Proof

The following permutations preserve the displayed edge set:

- the rotation
  \[
  a_i\mapsto a_{i+1},\qquad b_i\mapsto b_{i+1},
  \]
  fixing \(x,y\);
- the antipodal permutation
  \[
  x\leftrightarrow y,\qquad a_i\leftrightarrow b_{i+2};
  \]
- the permutation
  \[
  T=(x\,a_0)(y\,b_2)(a_2\,b_0)(a_3\,b_4).
  \]

Checking the six edge types in the definition verifies these assertions. All three permutations preserve the antipodal pairing.

These automorphisms are vertex-transitive: \(T\) sends \(x\) to \(a_0\), rotations reach every \(a_i\), and the antipodal permutation reaches \(y\) and every \(b_i\). The stabilizer of \(x\) contains the rotation, which is transitive both on
\[
N_I(x)=\{a_i:i\in\mathbb Z_5\}
\]
and on the non-antipodal nonneighbors \(\{b_i:i\in\mathbb Z_5\}\). This proves part 3.

The vertex \(x\) is adjacent to exactly one vertex in each other antipodal pair. Vertex-transitivity, preserving the pairing, proves part 1.

For part 2, it suffices by part 3 to examine the two types of nonedges:
\[
N_I(x)\cap N_I(y)=\varnothing,
\qquad
N_I(x)\cap N_I(b_0)=\{a_0,a_1\}.
\]
The latter two vertices are adjacent. An induced \(C_4\) would give a nonadjacent pair with two nonadjacent common neighbors, so no induced \(C_4\) exists. \(\square\)

These calculations also verify that \(I\) itself is \(C_4\)-induced-saturated:

- deleting \(xa_0\) creates the cycle \(x-a_4-a_0-a_1-x\);
- adding \(xb_0\) closes the induced path \(x-a_2-b_1-b_0\);
- adding \(xy\) closes the induced path \(x-a_0-b_0-y\).

The automorphisms cover all edge and nonedge types. The larger construction below uses more than this saturation property.

---

# 3. Hypercube components for \(C_4+K_1\)

Choose a partition of \([n]\) into twelve nonempty parts
\[
(V_z:z\in V(I)).
\]
Construct a family \(\mathscr C\) of graphs on this fixed partition as follows:

1. Every \(V_z\) is a clique.
2. If \(z,w\) belong to different antipodal pairs, put all edges between \(V_z,V_w\) when \(zw\in E(I)\), and no edges otherwise.
3. Between the two parts belonging to an antipodal pair, choose the edges arbitrarily.

Call the edges in item 3 the **free coordinates**. Their number is
\[
D=|V_x||V_y|
  +\sum_{i\in\mathbb Z_5}|V_{a_i}||V_{b_{i+2}}|.
\]
As an abstract flip graph, the family \(\mathscr C\) is a copy of \(Q_D\).

We prove that it is an entire connected component of \(\mathcal G_{C_4+K_1,n}\).

## 3.1 Every graph in \(\mathscr C\) is \(C_4+K_1\)-free

In fact, every induced \(C_4\) in a graph \(G\in\mathscr C\) is dominating.

First suppose a cycle uses vertices from both parts \(V_z,V_{z^*}\) of an antipodal pair. Every vertex in any other part is complete to one of these two parts, by Lemma 3(1). A vertex in \(V_z\cup V_{z^*}\) outside the cycle has a neighbor on the cycle in its own clique part. Thus the cycle is dominating.

It remains to show that every induced \(C_4\) does use both parts of some antipodal pair. Suppose not. Two cycle vertices in the same clique part would be adjacent and have identical adjacencies to the other cycle vertices: the only part permitting nonuniform adjacencies is the antipodal part, which is absent. But adjacent vertices of an induced \(C_4\) do not have identical adjacencies to the other two vertices.

Therefore the cycle uses four distinct parts, no two antipodal. All six relevant adjacencies are fixed by \(I\), so these four base vertices would induce a \(C_4\) in \(I\), contradicting Lemma 3.

Hence every induced \(C_4\) is dominating. No induced \(C_4+K_1\) exists.

## 3.2 Every flip of a fixed coordinate creates \(C_4+K_1\)

There are three types of fixed coordinates. By relabeling the base graph using Lemma 3, they reduce to the cases below. This does not require equal part sizes.

In the displayed witnesses, a base label such as \(a_i\) denotes an arbitrary chosen vertex of \(V_{a_i}\). All auxiliary parts are nonempty.

### Case A: deleting an edge inside a part

Normalize the part to \(V_x\), and delete \(uv\) with \(u,v\in V_x\).

Then
\[
u-a_0-v-a_2-u
\]
is an induced \(C_4\), and \(b_3\) is isolated from its four vertices. All relevant relations are fixed coordinates.

### Case B: adding a fixed cross-nonedge

Normalize the pair of parts to \(V_x,V_{b_0}\), and add \(uv\), where
\[
u\in V_x,\qquad v\in V_{b_0}.
\]
Then
\[
u-a_2-b_1-v-u
\]
is an induced \(C_4\), with \(b_3\) isolated from it.

Again, no antipodal free coordinate occurs in this witness.

### Case C: deleting a fixed cross-edge

Normalize the pair of parts to \(V_x,V_{a_0}\), and delete \(uv\), where
\[
u\in V_x,\qquad v\in V_{a_0}.
\]
Choose any \(w\in V_{b_2}\). The pair \(vw\) is a free coordinate, so there are two possibilities.

- **If \(vw\notin E(G)\):** use the induced cycle
  \[
  u-a_4-v-a_1-u,
  \]
  with \(w\) isolated.

- **If \(vw\in E(G)\):** use the induced cycle
  \[
  v-b_0-b_1-w-v,
  \]
  with \(u\) isolated.

The first witness uses the free coordinate \(vw\) as a nonedge; the second uses it as an edge. No other free coordinate affects either witness.

Thus every fixed-coordinate flip creates an induced \(C_4+K_1\), for every assignment of all free coordinates.

## 3.3 The exact component and its size

All free-coordinate assignments are \(C_4+K_1\)-free, and their flips form \(Q_D\). Every flip leaving this family creates the forbidden graph. Therefore \(\mathscr C\) is an entire connected component.

It is not the whole flip graph: the empty graph is \(C_4+K_1\)-free and does not belong to \(\mathscr C\).

For any \(n\ge12\), take the ten parts other than \(V_x,V_y\) to have size one, and choose
\[
|V_x|=\left\lfloor\frac{n-10}{2}\right\rfloor,
\qquad
|V_y|=\left\lceil\frac{n-10}{2}\right\rceil.
\]
Then
\[
D=\left\lfloor\frac{(n-10)^2}{4}\right\rfloor+5.
\]
Complementation gives the same conclusion for \((2K_2)\vee K_1\). This proves Theorem 1. \(\square\)

Importantly, this does **not** assert that these forbidden graphs have no finite induced-saturated graphs. It establishes a non-singleton component directly.

---

# 4. A rook-graph criterion and all odd cycles

Let
\[
R_q=L(K_{q,q}).
\]
Equivalently, \(V(R_q)=[q]^2\), with two cells adjacent precisely when they lie in the same row or column.

Let \(\mathcal R\) denote the class of line graphs of finite simple bipartite graphs.

## Proposition 4: two-perturbation criterion

Suppose \(H\notin\mathcal R\), but there exist
\[
e\in E(H),\qquad f\notin E(H)
\]
such that
\[
H-e\in\mathcal R,\qquad H+f\in\mathcal R.
\]
Then \(H\) has a finite induced-saturated graph. In particular, if \(h=|V(H)|\), then \(R_h\) is such a graph.

### Proof

The class \(\mathcal R\) is hereditary: an induced subgraph of \(L(B)\) is the line graph of the subgraph of \(B\) consisting of the corresponding edges. Thus \(R_h\) is \(H\)-free.

Every \(h\)-vertex graph in \(\mathcal R\) embeds inducedly into \(R_h\). Indeed, write it as \(L(B)\), remove isolated vertices of \(B\), and note that \(B\) has \(h\) edges and at most \(h\) vertices in each bipartition class.

The automorphisms of \(R_h\) are transitive on edges and on nonedges: row and column permutations handle each type, with transposition exchanging row-edges and column-edges.

For any nonedge of \(R_h\), embed \(H-e\), and then apply an automorphism mapping the designated nonedge \(e\) to it. Adding that nonedge creates \(H\).

For any edge of \(R_h\), use an embedding of \(H+f\), mapping the designated edge \(f\) to it. Deleting that edge creates \(H\). \(\square\)

The same proof works with \(R_q\) whenever both perturbations embed into \(R_q\).

## 4.1 Odd cycles

### Corollary 5

For every \(k\ge2\),
\[
R_{k+1}
\]
is \(C_{2k+1}\)-induced-saturated. Hence
\[
\mathcal G_{C_{2k+1},n}
\quad\text{and}\quad
\mathcal G_{\overline{C_{2k+1}},n}
\]
are disconnected for all \(n\ge(k+1)^2\).

### Proof

An induced cycle of length at least four in a rook graph must alternate row-edges and column-edges. At any cycle vertex, the two incident cycle edges cannot both be row-edges or both be column-edges, since that would give a chord. Thus every such induced cycle is even, and \(C_{2k+1}\notin\mathcal R\).

Deleting a cycle edge gives \(P_{2k+1}\), the line graph of \(P_{2k+2}\). Its bipartite root has \(k+1\) vertices in each part.

For the other perturbation, take a \(C_{2k}\) and attach one pendant edge to a cycle vertex. Its line graph consists of an induced \(C_{2k}\) plus one vertex adjacent exactly to the endpoints of one cycle edge. Equivalently, it is a \(C_{2k+1}\) with one distance-two chord added. The bipartite root has part sizes \(k\) and \(k+1\).

Both perturbations therefore embed into \(R_{k+1}\), and Proposition 4 applies. The empty and complete graphs are also \(C_{2k+1}\)-free, so an isolated witness gives disconnection. Proposition 2 and complementation finish the proof. \(\square\)

For example, \(R_3\), on nine vertices, is \(C_5\)-induced-saturated.

## 4.2 Disconnected forbidden graphs supplied by the criterion

Let \(F\in\mathcal R\), possibly empty. Proposition 4 also proves eventual disconnectedness for
\[
H=F+K_{1,3},\qquad
H=F+(K_4-e),\qquad
H=F+C_{2k+1}\quad(k\ge2),
\]
and for their complements.

For completeness, the perturbations of the first two distinguished components are
\[
\begin{array}{c|c|c}
H_0 & H_0-e & H_0+f\\ \hline
K_{1,3} & P_3+K_1 & \text{paw}\\
K_4-e & C_4 & K_4.
\end{array}
\]
All four graphs in the last two columns are line graphs of bipartite graphs. For instance, the paw is the line graph of a claw with one edge subdivided.

Rook graphs contain neither a claw nor a diamond: each vertex neighborhood is the disjoint union of two cliques. They also contain no induced odd cycle of length at least five. Thus each displayed \(H\) lies outside \(\mathcal R\), while both required perturbations lie inside it.

This gives an explicit sufficient threshold \(n\ge |V(H)|^2\), though it is generally not optimal.

---

# 5. Hamming graphs: stars and a larger family

The following construction improves the star-witness bound in the previous attempt.

Let
\[
H=K_1\vee\bigl(K_{a_1}+\cdots+K_{a_r}\bigr),
\]
where \(r\ge2\), all \(a_i\ge1\), and at least two of the \(a_i\) equal \(1\).

Put
\[
d=r-1,\qquad q=\max_i a_i+2.
\]
Let \(X\) be the Hamming graph on \([q]^d\), with two words adjacent exactly when they differ in one coordinate.

## Proposition 6

The graph \(X\), of order \(q^{r-1}\), is \(H\)-induced-saturated.

### Proof

For a word \(u\), let \(C_i(u)\) be the set of neighbors obtained by changing coordinate \(i\). Then
\[
N_X(u)=C_1(u)+\cdots+C_d(u),
\]
where every \(C_i(u)\) is a clique of size \(q-1\).

### \(H\)-freeness

An induced copy of \(H\), centered at \(u\), would require \(r\) nonempty, pairwise anticomplete clique branches in \(N_X(u)\). Different branches must occupy different coordinate cliques. There are only \(d=r-1\) of them, so this is impossible.

### Adding a nonedge

Let \(u,v\) be nonadjacent. Their Hamming distance is at least two.

In each \(C_i(u)\), at most one vertex is adjacent to \(v\):

- if \(u,v\) differ in at least three coordinates, there is none;
- if they differ in exactly two coordinates, only changing one of those coordinates to its value in \(v\) can produce a neighbor of \(v\).

Thus each coordinate clique has at least
\[
q-2=\max_i a_i
\]
vertices nonadjacent to \(v\).

Use \(v\) for one singleton branch of \(H\). In the \(d\) coordinate cliques of \(N_X(u)\), choose the remaining branches, avoiding neighbors of \(v\). Distinct coordinate cliques are anticomplete. After adding \(uv\), these vertices induce \(H\), centered at \(u\).

### Deleting an edge

Let \(u,v\) differ in coordinate \(i\). Choose \(w\) agreeing with them outside coordinate \(i\), and taking a third value in coordinate \(i\).

After deleting \(uv\), the vertices \(u,v\) form two singleton branches centered at \(w\). For each of the other \(d-1=r-2\) coordinates, use an appropriately sized clique in \(C_j(w)\) for one remaining branch.

Vertices in these other coordinate cliques are nonadjacent to both \(u\) and \(v\), and different coordinate cliques are anticomplete. Hence the selected vertices induce \(H\). \(\square\)

Taking every \(a_i=1\) yields the particularly simple consequence
\[
X=H(r-1,3)
\quad\text{is }K_{1,r}\text{-induced-saturated}.
\]
Therefore
\[
\mathcal G_{K_{1,r},n}
\quad\text{and}\quad
\mathcal G_{K_r+K_1,n}
\]
are disconnected whenever
\[
n\ge 3^{r-1}.
\]
For the claw, this is the nine-vertex rook graph \(R_3\), rather than the fifteen-vertex witness in the previous attempt.

---

# 6. What remains unresolved

These results do not characterize all finite \(H\).

The connected benchmark cases remain important:

- If \(H\) is a clique, deleting edges connects every \(H\)-free graph to the empty graph.
- If \(H\) is an independent set, adding edges connects every \(H\)-free graph to the complete graph.
- The supplied source establishes connectivity for \(H=P_4\).

The arguments here supply no necessary condition matching the sufficient constructions. For example, this writeup does not decide \(H=P_5\) or \(H=P_4+K_1\).

The principal advance is the explicit component construction for
\[
C_4+K_1
\quad\text{and}\quad
(2K_2)\vee K_1.
\]
It demonstrates a useful mechanism specific to the weaker flip-connectivity question: an entire set of independently adjustable edges can remain free, while **every change outside that set is forbidden**. The resulting obstruction is a large hypercube component, not an isolated graph. No claim is made that these forbidden graphs lack isolated vertices elsewhere, or that any threshold above is optimal.