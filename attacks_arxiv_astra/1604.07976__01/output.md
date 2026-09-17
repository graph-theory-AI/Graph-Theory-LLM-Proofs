```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "An additive gluing formula gives the linear bound for arbitrary 1- and 2-clique-sums of fixed-apex planar pieces.",
  "would_publish": false,
  "caveats": "This does not resolve positive-genus torsos or general three-vertex adhesions; novelty of the composition result is not claimed."
}
```

## 1. A provable composition result

I do not obtain a proof or counterexample for the full conjecture. The main result below is an additive composition theorem: gluing along separators of order at most two incurs only linear total overhead, regardless of the number of pieces. I also give a small three-terminal refinement and identify precisely why it does not finish the argument.

All graphs are finite and simple unless auxiliary parallel edges are explicitly allowed. Write
\[
P_{\mathrm{ST}}(G)=\operatorname{conv}\{\chi^T:T\text{ is a spanning tree of }G\}.
\]
Extension complexity counts inequalities; equations are free.

Let \((\mathcal T,(B_t)_{t\in V(\mathcal T)})\) be a tree decomposition of a connected graph \(G\), with
\[
|B_s\cap B_t|\le 2\qquad(st\in E(\mathcal T)).
\]
Its torso at \(t\), denoted \(J_t\), is obtained from \(G[B_t]\) by adding the edge \(uv\) whenever
\[
B_s\cap B_t=\{u,v\}
\]
for a neighbor \(s\) of \(t\). Let \(h\) be the number of decomposition edges whose adhesion has size two.

### Theorem 1 — additive two-vertex gluing
For such a decomposition,
\[
\boxed{\quad
\operatorname{xc}(P_{\mathrm{ST}}(G))
\le
\sum_{t\in V(\mathcal T)}
\operatorname{xc}(P_{\mathrm{ST}}(J_t))+4h.
\quad} \tag{1}
\]

Consequently, suppose every torso satisfies
\[
\operatorname{xc}(P_{\mathrm{ST}}(J_t))\le c|B_t|
\]
for a fixed constant \(c\). Then
\[
\operatorname{xc}(P_{\mathrm{ST}}(G))\le (3c+4)|V(G)|. \tag{2}
\]

For the graph-class application, use the fixed-\(k\) apex-planar result stated in the question: for every fixed \(k\), connected graphs made planar by deleting at most \(k\) vertices have spanning-tree extension complexity \(O_k(n)\).

### Corollary 2
Fix \(k\). If \(G\) has a tree decomposition of adhesion at most two in which every torso is \(k\)-apex planar, then
\[
\operatorname{xc}(P_{\mathrm{ST}}(G))=O_k(|V(G)|).
\]

In particular, this applies to arbitrary iterated 1- and 2-clique-sums of \(k\)-apex planar graphs. The number of pieces is unrestricted, and different pieces may have different apex sets.

---

## 2. The exact two-piece formula

Let \(H_1,H_2\) be connected graphs, possibly with parallel edges. Their vertex sets intersect exactly in two distinct vertices \(u,v\). Give each graph a distinguished edge
\[
p_i=uv\in E(H_i).
\]
The distinguished edges are separate copies, as are all other edge coordinates. Define
\[
G=(H_1-p_1)\cup(H_2-p_2),
\]
and assume \(G\) is connected.

Let \(\pi\) delete the two distinguished-edge coordinates. Then
\[
P_{\mathrm{ST}}(G)=
\pi\left\{
(x^1,x^2):
\begin{array}{l}
x^i\in P_{\mathrm{ST}}(H_i)\quad(i=1,2),\\
x^1_{p_1}+x^2_{p_2}=1
\end{array}
\right\}. \tag{3}
\]

In particular,
\[
\operatorname{xc}(P_{\mathrm{ST}}(G))
\le
\operatorname{xc}(P_{\mathrm{ST}}(H_1))
+
\operatorname{xc}(P_{\mathrm{ST}}(H_2)). \tag{4}
\]

### Proof of the spanning-tree correspondence

Suppose \(T_i\) is a spanning tree of \(H_i\), and exactly one of \(p_1,p_2\) belongs to its respective tree.

On the side where the distinguished edge is absent, deleting it leaves a spanning tree. On the other side, deleting the distinguished edge produces two components, one containing \(u\) and the other containing \(v\). Their union is therefore connected. Its number of edges is
\[
(|V(H_1)|-1)+(|V(H_2)|-1)-1
=|V(G)|-1,
\]
so it is a spanning tree of \(G\).

Conversely, let \(T\) be a spanning tree of \(G\), and put
\[
F_i=T\cap E(H_i-p_i).
\]
Each component of \(F_i\), regarded as a spanning forest on \(V(H_i)\), must meet \(\{u,v\}\); otherwise it could not connect to the rest of \(T\). Thus \(F_i\) has \(c_i\in\{1,2\}\) components. Counting edges gives
\[
|V(G)|-1
=|V(H_1)|+|V(H_2)|-c_1-c_2,
\]
and hence \(c_1+c_2=3\). Exactly one restriction is connected. Add \(p_i\) on the disconnected side to obtain the required pair of local spanning trees.

### Why the polyhedral intersection is exact

It remains to justify that (3) creates no unwanted fractional points.

Take feasible \(x^1,x^2\), and choose distributions on spanning trees of \(H_i\) with these expectations. Put
\[
a=x^1_{p_1}=1-x^2_{p_2}.
\]
Couple the two distributions as follows:

- with probability \(a\), choose the first tree conditioned on containing \(p_1\), and the second conditioned on avoiding \(p_2\);
- with probability \(1-a\), use the opposite conditions.

Zero-probability cases are omitted. This preserves both marginal distributions, and every resulting pair satisfies the spanning-tree correspondence above. Its projection is therefore a spanning tree of \(G\). This proves (3).

For a one-vertex sum, the corresponding formula is simply
\[
P_{\mathrm{ST}}(H_1\cup H_2)
=
P_{\mathrm{ST}}(H_1)\times P_{\mathrm{ST}}(H_2),
\]
using disjoint edge coordinates.

The essential feature is that a two-vertex interface has a **single binary state**: the restriction is connected, or it has two components separating the interface vertices.

---

## 3. Proof of Theorem 1

### 3.1 Assigning edges to pieces

Assign each edge of \(G\) to one bag containing both endpoints. Let \(E_t\) be the edges assigned to \(t\).

Construct an auxiliary multigraph \(H_t\) on \(B_t\) consisting of:

1. the edges in \(E_t\);
2. one distinct virtual edge \(p_{ts}=uv\) for every neighbor \(s\) with
   \[
   B_t\cap B_s=\{u,v\}.
   \]

Virtual edges may be parallel to real edges or to other virtual edges.

Each \(H_t\) is connected. To see this, take a path in \(G\) between two vertices of \(B_t\). An excursion outside \(B_t\) lies on one side of an incident decomposition edge, so its endpoints belong to the corresponding adhesion. An excursion with distinct endpoints can therefore be replaced by a virtual edge. Likewise, an edge with both endpoints in \(B_t\) but assigned elsewhere can be replaced by a virtual edge along the first step toward its owner bag. This produces a walk in \(H_t\).

Now repeatedly remove leaves of the decomposition tree. At an adhesion of size one, apply the product formula; at an adhesion of size two, apply (3). The running-intersection property ensures that the two sides intersect exactly in the adhesion.

Consequently,
\[
\operatorname{xc}(P_{\mathrm{ST}}(G))
\le
\sum_t\operatorname{xc}(P_{\mathrm{ST}}(H_t)). \tag{5}
\]

### 3.2 Paying for parallel virtual edges

Let \(\overline H_t\) be the simplification of \(H_t\). It is a connected spanning subgraph of \(J_t\). Thus its spanning-tree polytope is obtained from that of \(J_t\) by setting deleted-edge coordinates to zero, so
\[
\operatorname{xc}(P_{\mathrm{ST}}(\overline H_t))
\le
\operatorname{xc}(P_{\mathrm{ST}}(J_t)). \tag{6}
\]

For completeness, parallel edges can be restored cheaply. If a simple edge \(e\) represents a parallel class \(C_e\), introduce variables \(x_f\) satisfying
\[
\sum_{f\in C_e}x_f=y_e,
\qquad x_f\ge0\quad(f\in C_e).
\tag{7}
\]
These constraints give exactly the spanning-tree polytope of the multigraph. Indeed, after choosing a simple spanning tree with expectation \(y\), replace a used edge \(e\) by \(f\in C_e\) with probability \(x_f/y_e\). Classes with \(y_e=0\) are never used.

Only classes of size at least two require new inequalities. If \(d_t\) is the number of surplus parallel copies, their cost is at most
\[
\sum_{|C_e|\ge2}|C_e|\le 2d_t.
\]
Since \(G\) is simple, every surplus copy is caused by a virtual edge. There are \(2h\) virtual edges altogether, so
\[
\sum_t d_t\le2h.
\]
Combining this with (5) and (6) proves (1).

### 3.3 Converting total bag size into \(O(n)\)

We may assume no bag is contained in an adjacent bag. Otherwise, remove the contained bag and attach its other neighbors to the containing bag.

This operation preserves the required properties. Indeed, a contained bag has size at most two; any newly required torso edge was already supplied by its adhesion to the containing bag. Remaining torsos only lose edges.

Root the reduced decomposition. Every nonroot bag introduces at least one vertex not in its parent, and these introduced-vertex sets are disjoint. Hence
\[
|V(\mathcal T)|\le n.
\]
The running-intersection property also gives the exact identity
\[
\sum_t|B_t|
=
n+\sum_{st\in E(\mathcal T)}|B_s\cap B_t|.
\]
Therefore
\[
\sum_t|B_t|\le n+2(|V(\mathcal T)|-1)\le3n-2,
\qquad
h\le n-1.
\]
Equation (2), and then Corollary 2, follow.

### Relation to proper minor-closed families

These graphs are contained in a proper minor-closed family: if all torsos are \(k\)-apex planar, then \(G\) has no \(K_{k+5}\)-minor.

Here is the relevant localization argument. Across a separation of order at most two, at most two branch sets of a clique-minor model meet the separator. All remaining branch sets must lie on the same side, because branch sets lying on opposite sides cannot be adjacent. Truncating the separator-meeting branch sets to that side and completing the separator to a clique preserves the model. Repeating this localizes any \(K_t\)-minor, for \(t\ge4\), to a torso.

But a \(k\)-apex planar torso cannot contain a \(K_{k+5}\)-minor: removing the at most \(k\) branch sets meeting its apex set would leave a \(K_5\)-minor in a planar graph.

---

## 4. A limited refinement for three terminals

There is also a useful linear-size formulation for the connectivity state at **one** three-vertex boundary.

Let \(H\) be a connected \(k\)-apex planar graph, let \(B\subseteq V(H)\) with \(1\le |B|\le3\), and let \(\rho\) be a partition of \(B\). Define
\[
Q_\rho(H,B)
=
\operatorname{conv}\left\{
\chi^F:
\begin{array}{l}
F\text{ is a spanning forest of }H,\\
\text{every component of }F\text{ meets }B,\\
F\text{ induces partition }\rho\text{ on }B
\end{array}
\right\}.
\]

### Proposition 3
Whenever nonempty,
\[
\operatorname{xc}(Q_\rho(H,B))=O_k(|V(H)|).
\]

### Proof

For a nonempty vertex set \(R\), let \(H/R\) denote the graph obtained by identifying all vertices of \(R\) into one vertex. Retain edge labels; resulting loops have coordinate zero.

A spanning tree of \(H/R\) corresponds exactly to a spanning forest of \(H\) having \(|R|\) components, each containing exactly one vertex of \(R\). To verify this, such a forest becomes connected after identification and has the correct number of edges. Conversely, a tree in the quotient cannot contain either an original cycle or a path between two distinct vertices of \(R\).

There are only three types of partition to handle.

1. **One block.** Then \(F\) must be connected:
   \[
   Q_\rho(H,B)=P_{\mathrm{ST}}(H).
   \]

2. **All singleton blocks.** Then
   \[
   Q_\rho(H,B)=P_{\mathrm{ST}}(H/B),
   \]
   interpreted in the original edge coordinates.

3. **Three terminals and two blocks.** Write
   \[
   B=\{a,b,c\},\qquad \rho=\{\{a,b\},\{c\}\}.
   \]
   Then
   \[
   Q_\rho(H,B)
   =
   P_{\mathrm{ST}}(H/\{a,c\})
   \cap
   P_{\mathrm{ST}}(H/\{b,c\}). \tag{8}
   \]

For the last equality, the common spanning-tree edge sets are exactly the two-component spanning forests separating \(c\) from both \(a\) and \(b\). Since there are only two components, \(a\) and \(b\) lie together.

Crucially, (8) is a polyhedral equality, not merely an equality of the integral points. The two polytopes are base polytopes of graphic matroids on the same edge ground set, both of rank \(|V(H)|-2\). The matroid-intersection integrality theorem implies that their intersection is the convex hull of their common bases.

Finally, all quotient graphs used above are \((k+3)\)-apex planar: delete the images of an apex set of \(H\), together with the images of \(B\). Their remaining graphs are planar. Also, \(H\) has \(O_k(|V(H)|)\) edges, so any parallel-edge overhead after identification remains linear. Applying the known fixed-apex bound and the parallel-edge formulation proves the proposition. ∎

This handles the five possible partitions of a single three-terminal boundary. It does **not** yet give an additive theorem for arbitrary 3-clique-sums.

---

## 5. The unresolved gap

There are two distinct limitations.

### 5.1 Many three-terminal interfaces require joint information

At a two-vertex interface, the state is represented by the incidence of one virtual edge. A local spanning-tree distribution automatically supplies a joint distribution for all such virtual-edge bits.

At a three-vertex interface, a state is a connectivity partition, not just an edge-incidence bit. Proposition 3 supplies a formulation for one prescribed partition at one interface. A large piece, however, may meet many different interfaces. One needs their **jointly realizable connectivity states**.

I have not constructed a linear-size simultaneous lift for those states. Simply intersecting separately constructed interface formulations does not establish the required convex-hull equality.

### 5.2 Even the two-vertex theorem misses basic toroidal graphs

The uncovered case is already concrete. Let
\[
G_r=C_r\square C_r,\qquad r\ge4.
\]
These graphs embed on the torus and are 3-connected.

Moreover, deleting at most \(r-4\) vertices cannot make \(G_r\) planar. Such a deletion leaves at least four completely intact rows and four completely intact columns. Their union contains a subdivision of
\[
C_4\square C_4.
\]
That graph is bipartite, with \(16\) vertices and \(32\) edges, so it is nonplanar because a simple planar bipartite graph on \(16\) vertices has at most \(28\) edges.

Thus, for every fixed \(k\), sufficiently large \(G_r\) are not \(k\)-apex planar. Since they are 3-connected, a reduced adhesion-at-most-two decomposition has just one bag. Corollary 2 therefore does not apply.

So the composition theorem genuinely avoids a multiplicative loss when many easy pieces are glued together, and Proposition 3 resolves a small local connectivity-state problem. Neither result improves the supplied general \(O(n^{3/2})\) bound or settles even this toroidal test family. The full conjecture remains unproved and undisproved here.